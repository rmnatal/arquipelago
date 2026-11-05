# Registro de execuções — Rodametria

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-11-05 13h20Z–13h24Z — **A PORTA SEGUE NO CHÃO TRÊS HORAS DEPOIS, E O TRABALHO DESTA PASSADA FOI DERRUBAR UMA PREMISSA: AR E SEGREDO NÃO SÃO UMA TROCA OBRIGATÓRIA** — nenhum bloco da fila, pela 18.5

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10) e pela **1.2** não há escolha a fazer. `executando_desde` estava `null` na chegada, que pela **1.1** já significa que não havia bloco da Fundação vivo — sem reserva vencida, não houve o que o git desempatar. Nenhum branch `claude/*` e nenhum PR aberto: `origin/main` e `claude/dreamy-mccarthy-zapj3t` apontavam para o **mesmo** commit (`c1185a0`), então não havia o que mergear. Reserva no commit `edde4c7`, às **13h20Z**, com a hora saída do `date -u` na mesma linha de comando que a grava.

**A REDE FOI MEDIDA ANTES DO TRABALHO E NÃO HERDADA (20.2):** `rodametria.com.br` em **200**, com `aquametria.com.br` e `robometria.com.br` em **200** na mesma passada. **E vale repetir a lição de método que a execução das 10h18Z escreveu, porque ela se repetiu inteira hoje:** essa medição é a que **autoriza** a reserva e é a mesma que **esconde** o defeito — a régua da 20.2 pede a raiz, e a raiz é a única coisa que esta queda deixa de pé (29.1).

### O NÚMERO, E ELE NÃO MUDOU EM TRÊS HORAS

`python3 ferramentas/conferir-no-ar.py .` — que é literalmente o que o `bloco_atual` da execução anterior mandou quem pegasse esta ilha rodar primeiro: **43 afirmações, 9 falhas**.

- As **três portas da 29.2** em **404** com `content-type: text/html`: `/wp-sitemap.xml`, `/robots.txt`, `/wp-json/`.
- O caminho virgem (`/nao-existe-<timestamp>/`) em 404 **na página do hospedeiro**.
- **Só `/` responde 200**, com a página de verdade.
- **O outro lado continua intacto e continua irrelevante (29.1):** `?rest_route=` entrega a casca **1.10.0** (instalada em 2026-11-04 19:40:29), **4 de 4** versões de snippet batendo com o `manifest.json` (casca 1.10.0, f2 1.5.0, institucional 1.2.1, produto 1.7.1), e a **revisão 42** declarando `7 aplicado(s)` contra **7 linhas de item dizendo `ok`**, lidas do **fecho para baixo** (20.4 e 20.8).
- **O portão consertado às 10h3xZ fez o trabalho dele:** a linha da assinatura da **29.7** nomeou a causa e o conserto, e a leitura **não encolheu** — 43 afirmações com a porta no chão, contra as 9 de antes do conserto.

**A PORTA ESTÁ NO CHÃO HÁ PELO MENOS 17 HORAS** (última medição verde: 04/11 às 20h1xZ, pela leitura semanal) e **esta foi a segunda execução do dia a chegar nela e não poder levantá-la**. O despacho ALTA ficou, com a linha de tentativa que a **18.4** manda escrever.

**NENHUM BLOCO DA FILA FOI EXECUTADO, e isso é a 18.5 funcionando** — "ilha com defeito no ar não recebe página nova", e a dúvida entre fechar despacho e abrir bloco se resolve fechando despacho. Nada foi ao ar, nenhum snippet e nenhuma página mudaram, o `manifest.json` segue na **revisão 42** e **não há revisão a desembarcar**.

### O TRABALHO DESTA PASSADA: A QUARTA SAÍDA, MEDIDA E NÃO IMPLEMENTADA

O despacho ALTA de 10h2xZ pôs **três** saídas na mesa do Raphael (fica como está · o token entra no `PROMPT.md` · nasce um token só de reparo) e as três compartilham uma premissa: **que o reparo precisa de um segredo para ser pedido.** Medi a premissa e ela é **falsa**.

**O QUE ESTÁ MEDIDO, não suposto:**

1. **O repositório já executa PHP arbitrário neste site.** O Sync instala `snippets/*.php` lidos do `raw.githubusercontent.com` e os ativa. O portão de ar de hoje conferiu **4 de 4** versões no ar contra o manifest: **os bytes do `main` são o código que está rodando.** Um pedido de reparo assinado por *push* **não concede privilégio novo nenhum** — quem pode pedir por essa via já pode, hoje, trocar a casca inteira.
2. **A função do reparo já existe e já é completa:** `rodametria_casca_reparar_rotas()`, seção 12 da casca — `flush_rewrite_rules( true )`, purga depois, retrato de **antes e depois**. Só lhe falta uma segunda porta de entrada.
3. **O gatilho de "uma vez por pedido" já existe e já é guardado.** `rodametria_casca_instalar()` roda no `init` e **não a cada requisição**: volta na hora se a `option` `rodametria_casca_instalado` já traz a versão da casca e a assinatura do mapa de páginas correntes.

**A SAÍDA 4:** o pedido de reparo é um **campo no `manifest.json`** — o canal que a fábrica já usa para instruir o site —, cumprido **uma vez** pelo guard que já existe, com o antes e o depois numa linha do log do `/status`, que é onde a 20.4 já manda ler linha por linha. **Zero segredo novo, zero rota nova, e a porta volta a ser trabalho de um push.** A 29.4 foi respondida **na própria letra dela**, item por item, numa tabela dentro do despacho: o que ela teme é reparo **calado**, **a cada carregamento** e **que ninguém desfaz** — e um pedido versionado no git, cumprido uma vez e escrito no log é o contrário dos três.

**E O CUSTO ESTÁ ESCRITO INTEIRO**, porque saída apresentada sem custo é saída vendida: (a) quem dispara o cron é o **visitante** (20.6), então a porta é reescrita dentro do carregamento de alguém; (b) campo esquecido ligado é a porta reescrita a cada revisão — o medo da 29.4 pela porta dos fundos, e o conserto é o pedido carregar o **número da revisão** e o portão **dizer quantas vezes o reparo rodou**; (c) **isto não conserta a CAUSA e não promete consertar** — a 29.5 segue valendo, e pela 19.4(b) a segunda queda nesta mesma raiz vira chamado na HostGator.

**POR QUE EU NÃO A IMPLEMENTEI, e é decisão e não fôlego.** A 29.4 é decisão escrita no contrato, e a escolha entre as saídas está aberta **para o Raphael** desde as 10h2xZ de hoje, com o próprio despacho pedindo *"não decida por mim nem por pressa"*. Mexer na porta de entrada do site por iniciativa de uma execução, com um despacho ALTA pendurado exatamente nessa pergunta, seria tomar a decisão dele de cabeça. **O que esta passada entrega é a premissa derrubada e a escolha mais barata na mesa** — e, se ele escolher a 4, ela cabe numa execução: campo no manifest, chamada guardada na casca, linha no log, e dois portões (um mundo fabricado em que o pedido roda **uma** vez e outro em que o pedido repetido **não** roda).

### O QUE ESTA EXECUÇÃO NÃO FEZ, dito para ninguém procurar depois

- **Não fechou o despacho ALTA** — pela 18.4 ele morre conferido no ar, e o ar reprova.
- **Não fechou o item 1 do despacho de 04/11** (sitemap "Processado" no Search Console): `/wp-sitemap.xml` está em 404 servindo HTML do hospedeiro, então o Google relê e falha de novo. **Primeiro a porta, depois o sitemap.**
- **Não rodou o portão de pixel** (`conferir-32-5-no-navegador.mjs`) nem a leitura sem quebra de cache: as duas medem páginas que estão em 404.
- **Não tocou em nenhuma das outras três ilhas.** O despacho NORMAL da 29.7 para elas segue aberto em `dados/despachos.md`, e o foco total da 1.2 proíbe bloco fora da ilha em foco; nenhuma delas está com a porta caída (as três medidas em 200 nesta passada).
- **Não remediu o `gov.br`** da F1: continua recusado desde 28/10, e não era o trabalho desta passada.

**PRÓXIMO PASSO: SEGUE SENDO A PORTA, E SEGUE SENDO DO RAPHAEL.** Quem pegar esta ilha começa rodando `python3 ferramentas/conferir-no-ar.py .`. Se a linha da assinatura da 29.7 aparecer, **o despacho ALTA segue aberto e não há bloco a executar** — escreva a linha de tentativa da 18.4 e feche. Se a porta estiver reparada, o despacho se fecha pela 18.4 (conferido no ar, por quem confere e não por quem reparou), o item 1 de 04/11 volta a ser alcançável, e aí a fila não mudou: F1 travada pelo `gov.br`, F3 por `carga_max_kg`, malha nova pela 30.8 — e o candidato segue sendo o **ARTIGO-ÂNCORA PAREADO COM A F2 (bloco 5)**, com a primeira coisa a fazer sendo **conferi-lo contra a seção 17 e a 30.8**.

## 2026-11-05 10h18Z–10h3xZ — **A ILHA EM FOCO TOTAL ESTÁ FORA DO AR, MENOS A HOME, E O PORTÃO ESCRITO PARA VER ISSO ACUSOU A CASCA** — nenhum bloco da fila; o trabalho foi a porta e o instrumento

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10) e pela **1.2** não há escolha a fazer. `executando_desde` estava `null`, que pela **1.1** já significa que não havia bloco da Fundação vivo — não houve reserva vencida para o git desempatar. **As duas exceções que furam o foco foram conferidas ANTES da reserva e nenhuma furou:** as **quatro** ilhas no ar medidas em **200 em TRÊS passadas** com quebra de cache (doze medições verdes, zero intermitência), e o despacho do molde da **32.6** segue FECHADO nas três (aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ). Nenhum branch `claude/*` e nenhum PR aberto. Reserva no commit `a88a34e`, às 10h18Z.

**E A MEDIÇÃO QUE AUTORIZOU A RESERVA É A MESMA QUE ESCONDEU O DEFEITO, e isto é a lição de método do dia:** `https://rodametria.com.br/` em 200 três vezes é exatamente o que esta queda produz. A régua de rede da **20.2** pede a raiz, e a raiz é a única coisa que sobrevive. **Medir a home e concluir "a ilha está no ar" é a 29.1 em uma linha** — e eu escrevi "doze medições verdes" no commit de reserva antes de descobrir que oito das nove URLs estavam em 404.

### O QUE ESTÁ QUEBRADO, medido em DUAS leituras — com e sem quebra de cache

**8 das 9 URLs em 404**, servindo a página 404 da HostGator (`server: nginx`, `x-server-cache: true`, `last-modified` de 07/04/2026 — arquivo estático do hospedeiro, com `<meta name="robots" content="noindex">`). As **três portas da 29.2** idem: `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`, as três em 404 com `content-type: text/html`. O caminho virgem responde 404 **na página do hospedeiro**, não na desta ilha. **Só `/` responde 200**, com a página de verdade.

**O WORDPRESS ESTÁ DE PÉ, e é isso que nomeia a causa:** `?rest_route=/rodametria/v1/casca` responde **200**, casca **1.10.0**, as quatro versões de snippet batendo com o manifest, instalada em 2026-11-04 19:40:29; o log do `/status` traz a **revisão 42** declarando `7 aplicado(s)` contra **7 linhas de item dizendo `ok`**, lidas uma por uma (20.4). **A entrega de 04/11 está intacta. O que caiu foi a porta** — o bloco `# BEGIN WordPress` fora do `.htaccess` da raiz, a assinatura da **29** pela **quinta** vez no Arquipélago (clubedomosaico 24/09, 05/10, 08/10; robometria 30/10).

**QUANDO:** entre 04/11 às **20h1xZ** (a leitura semanal fechou medindo as 9 URLs) e 05/11 às **10h19Z**. Menos de 15 horas, e esta execução foi a primeira a olhar — a `ultima_ronda` é de 04/11 20h10Z.

**O REPARO NÃO É EXERCITÁVEL DESTA NUVEM**, e isso não é omissão: a 29.3 exige o **token do Sync**, que nesta ilha não está no repositório **por decisão** (divergência (b) da seção 12 da casca). Despacho **ALTA** para o Raphael no `PROMPT.md` e em `dados/despachos.md`, com as duas vias de conserto — e `/wp-admin/options-permalink.php` foi **medido alcançável** (302 para o login, porque é arquivo em disco), que é a via sem token. **Notificação enviada a ele às 10h2xZ.**

### O DEFEITO QUE ERA MEU CONSERTAR, E ELE ESTAVA NO PORTÃO ESCRITO PARA VER A QUEDA

O `conferir-no-ar.py` desta ilha lia o índice de rotas REST em `/wp-json/rodametria/v1` — **caminho bonito, portanto morto junto com a porta** — e o `/status` e o `/casca` do mesmo jeito. Com a porta no chão ele fez **duas** coisas piores que não medir:

1. **ACUSOU A CASCA DE UM DEFEITO QUE ELA NÃO TEM.** O `json.loads` falhava sobre a página 404 do hospedeiro, a lista de rotas vinha vazia, e a saída dizia *"esta casca nao registra a rota que mede a porta de entrada por dentro"*. A rota **estava** registrada: `?rest_route=/rodametria/v1/rotas` respondia **401 com `rodametria_rotas_token_invalido`** na mesma passada — o código que prova que a casca achou a fonte do token e rodou o `hash_equals`. **Quem lesse aquela linha iria procurar registro de rota na casca**, o conserto errado no arquivo errado, com a porta do site no chão.
2. **PAROU DE MEDIR O RESTO.** `main()` devolve na hora quando o `/status` não dá 200: a leitura encolheu de **481 afirmações** (04/11, de tarde) para **NOVE**. Conteúdo, voz, 32.4 e 32.5 deixaram de ser medidos exatamente no dia em que a ilha mais precisava.

**É A 29.1 COM UM ANDAR A MAIS.** A 29.1 diz que nenhum portão viu a porta cair porque **todos entravam pela porta que continuou aberta**. Este portão, escrito para ver, entrava pela porta que **cai** — e por isso ele viu, e culpou a casca.

**O CONSERTO, e ele é uma troca de porta e não um afrouxamento:** toda leitura de rota REST passa a `?rest_route=`. **A afirmação da 29.2 sobre `/wp-json/` em 200 com `application/json` ficou inteira** — ela é a dona da porta bonita, e o que muda é que as **outras** afirmações param de depender dela. Mais duas funções puras, para o autoteste poder fabricar o que esta nuvem não produz: `rotas_do_indice()` (índice que não é JSON devolve lista vazia, sem estourar) e `diagnostico_da_porta()`.

**E O PORTÃO PASSOU A NOMEAR A CAUSA.** Com as quatro grandezas na mesa — home em 200, as três portas em 404, REST vivo por `?rest_route=`, caminho bonito morto — ele escreve numa linha o que aconteceu **e o conserto**, em vez de seis reprovações espalhadas, cada uma verdadeira e nenhuma dizendo o que fazer. **E só com as quatro juntas:** home também morta, ou REST morto nas duas formas, é **outro** mundo, e aí ele devolve causa nenhuma — **causa inventada é a próxima execução consertando a coisa errada (29.5)**. A trava do `all()` sobre lista vazia tem mundo próprio: sem porta medida nenhuma não se nomeia causa.

**OS NÚMEROS DO CONSERTO.** Portão de ar contra o site quebrado: de **9 para 43 afirmações**, com a acusação falsa à casca **sumida** (agora o registro diz `PRESENTE no indice`) e a causa nomeada. `--autoteste`: de **36 para 46 afirmações, 0 falha**, com os mundos **12** e **13** novos. O mundo 12 dá à régua **velha** os bytes de verdade da página 404 do hospedeiro e **exige que as duas discordem** (20.8): a velha acusa a casca, a nova não acusa nada. E o **12(c)** cobra o contrário, que é o risco do conserto: índice de verdade **sem** a rota continua sendo pego — a troca de porta não afrouxou a afirmação. **Bancada sem rede: 28 portões, 0 falha.**

**NADA FOI AO AR, e não podia:** nenhum snippet e nenhuma página mudaram, então não há revisão a desembarcar — e a **18.5** proíbe página nova em ilha com defeito no ar. O `manifest.json` segue na revisão 42.

### A REGRA SUBIU, porque não é de uma ilha: as QUATRO leem assim

`ARQUIPELAGO.md` **29.7**. E está medido pelo `grep`, não por palpite: `ilhas/robometria/ferramentas/conferir-no-ar.py` monta `STATUS = DOMINIO + '/wp-json/robometria/v1/status'`; os `conferir-desembarque.py` da **aquametria** e da **clubedomosaico** idem, com o domínio de cada uma. **E o pior não é parar de medir, é a causa errada:** o da aquametria, com a porta caída, sai dizendo *"o /status nao respondeu ou nao e JSON … Pela 20.2, repita antes de chamar de bloqueio"* — manda o leitor para **intermitência de rede**, com a porta de entrada do site no chão. É a **20.5** ao pé da letra, e é como uma ilha fica dias fora do ar com o portão vermelho pelo motivo errado. Endereço da regra nas outras três: despacho **NORMAL** em `dados/despachos.md`, escrito como **pergunta** e mandando **medir antes de consertar** e **copiar** os dois portões em vez de reescrevê-los.

### O DESPACHO DE 04/11 NÃO FICOU COMO ESTAVA, e as duas mudanças são de sinal oposto

- **ITEM 1 ficou IMPOSSÍVEL de fechar enquanto a porta estiver no chão**, e é o custo mais caro desta queda. O "pronto quando" é o painel de Sitemaps em **Processado com 9 páginas**; `/wp-sitemap.xml` está em **404 servindo HTML**, então o Google vai reler o sitemap enviado em 04/11 às 19h5xZ e **falhar de novo** — e o estado "Não foi possível buscar o sitemap", que aquele despacho classificou com razão como normal na primeira leitura, vai **parecer o mesmo** por uma causa completamente diferente. Primeiro a porta, depois o sitemap.
- **ITEM 2 tem a premissa CONTRADITA por medição de hoje, e NÃO está fechado.** Ele diz que o egresso recusa `rodametria.com.br`. **Hoje não recusa:** 200 em três passadas às 10h1xZ, e o portão de ar fez **43 afirmações** contra o site de verdade, lendo `/status`, `/casca` e sitemap por `urllib`. O `ProxyError … 403 Forbidden` de 04/11 foi num **CONNECT**, que é recusa de **host** — e a Fundação mediu o mesmo host em 200 **quarenta minutos antes**, na mesma noite. As duas não podem ser verdade sobre um estado estável: é **intermitência ou lista de egresso mudando**, não bloqueio firme, e pela **20.2** bloqueio herdado se reteste antes de ser respeitado. **Quem fecha o item é a leitura semanal**, rodando `ferramentas/search-console.py` — instrumento dela, pede credencial de conta de serviço, e a Fundação não o roda por ela. Dito em vez de maquiado: **eu não fechei o item 2, eu derrubei a premissa dele.**

### PRÓXIMO PASSO

**A PORTA, e ela é do Raphael.** Nada de malha nova entra enquanto as 9 URLs não voltarem a 200 — **18.5**, e a ilha está invisível para o Google de qualquer forma. Quem pegar esta ilha a seguir **começa rodando `python3 ferramentas/conferir-no-ar.py .`**: se a causa nomeada da porta aparecer, o despacho ALTA segue aberto e **não há bloco a executar**; se a porta estiver reparada, o despacho se fecha pela **18.4** (conferido no ar, por quem confere e não por quem reparou) e **o item 1 do despacho de 04/11 volta a ser alcançável** — o sitemap passa a servir XML e o painel pode processar.

**Depois da porta, a fila honesta não mudou:** F1 (bloco 4) segue travada pelo egresso do `gov.br` (despacho ALTA de 28/10, **não remedido nesta passada** porque este trabalho não dependia dele); F3 segue travada por `carga_max_kg` em registro com oferta aberta; página nova de malha segue travada pela **30.8**, atrás do despacho de 30/10. **O candidato continua sendo o ARTIGO-ÂNCORA PAREADO COM A F2 (bloco 5)** — e a primeira coisa a fazer com ele continua sendo **conferi-lo** contra a seção 17 e a 30.8, porque se ele precisar de veredito de SERP para existir, está atrás do mesmo despacho de 30/10.

## 2026-11-04 19h17Z–19h46Z — **A FOLHA SERVIA 7.486 BYTES DE COMENTÁRIO E TRÊS MENÇÕES A UMA ROTINA DESTA PASTA, E NENHUM PORTÃO VIA** — bloco 7, pré-registrado nesta mesma manhã

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10) e pela **1.2**
não há escolha a fazer. **As duas exceções que furam o foco foram conferidas ANTES da reserva e nenhuma
furou:** as **quatro** ilhas no ar — rodametria, aquametria, robometria e clubedomosaico — foram medidas em
**200 em TRÊS passadas** às 19h1xZ, então nenhuma está "no ar E quebrada", inclusive a clubedomosaico do
despacho ALTA da porta de entrada (ela está sã, e o próximo passo dela é **chamado do Raphael** pela
19.4(b), não reparo); e o **despacho do molde da 32.6** segue FECHADO nas três ilhas. A fila da própria ilha
em foco estava **limpa**: o despacho de cinco itens da ronda de hoje foi fechado pela execução de
16h17Z–17h13Z. `executando_desde` estava `null`, que pela **1.1** já é prova de que não há bloco da Fundação
vivo. Reserva às **19h17Z**, renovada às **19h31Z**. Nenhum branch `claude/*` com commit fora do `main` e
nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` em **200 nas três passadas**, com
`aquametria.com.br`, `robometria.com.br` e `clubedomosaico.com.br` em **200 nas mesmas três** — doze
medições verdes, zero intermitência. O egresso do `gov.br` e dos três varejos grandes **não foi remedido**
nesta passada e este bloco não dependia dele; os dois despachos ALTA seguem valendo.

**A BANCADA ANTES DE CONSTRUIR (18.5):** 27 portões sem rede, **0 falha**, antes de uma linha ser escrita.
Nenhum defeito aberto no chão.

**O BLOCO ESCOLHIDO: O 7, e ele foi PRÉ-REGISTRADO nesta mesma manhã, pela execução de 16h17Z**, com o
número já medido e com o motivo de não ter saído junto escrito nele: *"o desembarque de 04/11 conserta a
32.5 mexendo em 24 regras da folha, e o número que a 32.5 mede ia ser lido no mesmo minuto. Mexer na folha
duas vezes no mesmo desembarque trocaria duas variáveis ao mesmo tempo no único número que esta ilha tem
como prova."* É a razão de ele ser bloco separado, e ela continua valendo: esta execução mexe na folha de
novo e **mede a 32.5 depois**, com uma variável trocada por vez.

### O NÚMERO, REMEDIDO E NÃO HERDADO — e ele é MAIOR do que o pré-registro dizia, pelo motivo que o pré-registro previu

O pré-registro contou **39 comentários e 6.042 bytes** nos **18** blocos `<style>` da página da F2.
Remedido no ar às **19h2xZ de hoje**, URL por URL com quebra de cache, a conta se divide — e a divisão é o
achado, porque ela separa o que esta ilha pode consertar do que ela não escreve:

| | comentários | bytes |
|---|---|---|
| **as folhas DESTA ilha** | **23 a 24** por página | **7.486 a 7.866** por página |
| as 17 folhas do próprio WordPress | 17 | 1.254 |
| **total servido** | 40 | 8.740 |

**85,6% dos bytes de comentário da página são desta ilha**, e são **10,6% de todo o CSS que ela escreve**.
Os 17 do WordPress são one-liners de 41 a 103 bytes (`/*! This file is auto-generated */` e parentes), não
são desta ilha, **não saem daqui** e por isso **não podem fazer portão nenhum reprovar** — reprovar por eles
seria reprovar o que esta ilha não pode consertar, que é o caminho mais curto para alguém passar a ignorar o
portão (20.5).

**E a folha cresceu 2,3 KB desde o pré-registro, exatamente como ele avisou** que cresceria: o comentário
que explica as 24 regras prefixadas com `body.rdm` do conserto da 32.5-d foi para a mesma folha.

**O QUE OS COMENTÁRIOS DIZEM, e é a 32.4 ao pé da letra:** três deles nomeiam uma rotina desta pasta
(`conferir-32-5-no-navegador.mjs`), um diz `bancada`, e vários trazem número de seção do contrato e prosa de
bastidor. Medido com a lista da 32.4 contra o **HTML servido inteiro** das 9 URLs: a **única** palavra da
lista que aparecia em qualquer lugar da página era `bancada`, **uma vez, dentro da nossa folha**. Nada do
WordPress casa com a lista — e isso foi **medido antes** de a régua nova nascer, não suposto.

### O CONSERTO É MECANISMO, E ELE MORA EM UM LUGAR SÓ

A tag `<style>` **saiu dos snippets**. Quem a escreve agora é a casca, em uma função
(`rodametria_casca_fechar_folha()`), e ela tira os comentários no caminho. As três folhas desta ilha — a da
casca, a de produto e a institucional — passaram a abrir e fechar a captura
(`rodametria_casca_abrir_folha()`), e **nenhum byte de CSS mudou de lugar no repositório**: era isso que
importava, porque a folha da casca tem 600 linhas e reescrevê-las para trocar *quem* as imprime seria mexer
na variável errada no mesmo dia em que a 32.5 é medida.

**O comentário fica no repositório, que é o lugar dele (seção 3).** Foi ele que pagou a 32.5-d duas vezes
nesta ilha. O que muda é que ele não sai na folha impressa.

**POR QUE EM UM LUGAR SÓ, e não em cada snippet:** a **32.5-c** é literal — regra que nasce na folha de um
snippet e não viaja para as irmãs é a doença que esta ilha já pagou. Com a tag na casca, **folha nova nasce
dentro do conserto**, sem ninguém se lembrar dele.

**COMO NÃO SE QUEBRA CSS TIRANDO COMENTÁRIO, que é o difícil do bloco:** `/*` pode aparecer **dentro de
string** (`content:"/*"`) e dentro de `url(...)` sem aspas, e o removedor ingênuo de uma linha
(`preg_replace('~/\*.*?\*/~s','')`) casa do `/*` de dentro da string até o `*/` de um comentário de
verdade **lá na frente** e corta a declaração do meio. Então string e `url()` entram na **mesma varredura**
como alternativas e são devolvidas **intactas** — é só por consumi-las inteiras que um `/*` dentro delas
nunca é lido como comentário. Mais duas decisões, as duas com o motivo escrito no código:

- **comentário colado entre dois caracteres de palavra** (`div/*x*/span`) sai como **um espaço**, não como
  nada: para o CSS são dois tokens, e colá-los inventaria um terceiro seletor que ninguém escreveu. Nenhuma
  folha desta ilha tem esse caso hoje; a passada existe para o dia em que tiver.
- **comentário sem fechar come o resto da folha**, que é exatamente o que o navegador faz. Não se inventa um
  fechamento que o autor não escreveu — e o portão do chão **reprova** folha desta ilha que tenha um.

### OS TRÊS PORTÕES, E O QUE CADA UM PROVA — ditos separados porque o conserto de cada um é diferente (20.5)

**1. `ferramentas/teste-folha-sem-comentario.php` (novo, 58 afirmações, 0 falha).** PHP pelo motivo que o
`teste-escada-de-compra.php` já escreveu: a remoção é decidida em PHP, então a régua **chama** a função.
Régua em Python sobre o texto do PHP conferiria a FORMA.
- **8 mundos fabricados, com a saída esperada escrita à mão** — `content:"/*"` seguido de um comentário de
  verdade, `url(data:...)` com `/*` dentro, aspa simples, aspa escapada, o comentário colado, o comentário
  sem fechar, e dois mundos que têm de sair **idênticos**. É aqui que a independência vive: nestes a saída é
  literal, não derivada da mesma noção de comentário.
- **A RÉGUA VELHA REFEITA AO LADO DA NOVA, e as duas DISCORDAM em 6 dos 8 mundos** — a 20.8 é literal:
  autoteste em que as duas concordam não mede conserto nenhum.
- **A TRAVA MAIS FORTE: o que desapareceu é exatamente o que morava dentro de comentário.** `{` de 145 para
  140, `;` de 282 para 280 na folha da casca — e dentro dos 23 comentários havia **exatamente** 5 `{`, 5 `}`
  e 2 `;`, que eram CSS comentado na prosa. A conta **abre** no dia em que a função cortar uma declaração de
  verdade. Mais: chaves equilibradas na saída, zero `/*`, zero `*/`, nada inventado (a saída sem espaço em
  branco é subsequência da entrada sem espaço em branco), e **comentário na entrada tem de existir** — senão
  a bateria estaria aprovando sobre nada.
- **E ele cobra que a tag `<style>` não saia de snippet nenhum**, contando no **HTML CRU** (o que fica fora
  de `<?php ... ?>`), porque menção a `<style>` em comentário de PHP não é tag servida e contar o arquivo
  inteiro reprovaria o próprio conserto.

**2. `ferramentas/conferir-no-ar.py` ganhou DUAS afirmações novas por URL**, separadas de propósito: uma diz
que a **folha servida** tem comentário (conserta-se na casca), a outra que há **palavra de bastidor no HTML
servido** (conserta-se no texto que a produziu).
- A segunda é a **32.4 sobre o byte servido**, e não sobre o texto visível. `corpo_da_pagina()` tira
  `<script>` e `<style>` antes de medir, e está **certo** — ali mora CSS, não prosa. **Entre as duas
  leituras cabia este defeito inteiro.**
- A lista ganhou as **extensões de rotina** `.py` e `.mjs` e os **nomes de arquivo desta pasta, lidos do
  disco e nunca enumerados**. `.php` **não** entra, e a causa foi medida: o WordPress serve `/wp-*.php` e
  `xmlrpc.php` no próprio `<head>`, duas ocorrências por página, e um termo `.php` reprovaria a página certa.
- **8 mundos no `--autoteste`**, que roda **sempre** porque as duas funções são puras e não precisam de rede.
  O primeiro é o mundo de verdade; dois provam que as folhas do WordPress ficam de fora; e o último refaz a
  **régua velha** (a do texto visível) ao lado da nova: a velha **aprova** a página doente e a nova a
  **reprova**. Total: 36 de 36 afirmações.

**3. O PORTÃO DE PIXEL da 32.5 roda DEPOIS do desembarque**, no navegador de verdade, porque folha cortada
errado aparece como **pixel errado** antes de aparecer como qualquer outra coisa. O portão do chão diz, com
estas palavras, que **não** promete que a folha continua pintando igual.

### O PORTÃO NOVO REPROVOU O AR DE ANTES, E ISSO É A PROVA DE QUE ELE MORDE

Rodado contra o site **antes** do desembarque: **524 afirmações, 43 falhas** — e as 43 são **só** das quatro
classes que este bloco existe para fechar (9 páginas × folha da casca, bastidor `bancada`, extensão `.mjs`,
nome do arquivo; mais 4 da folha institucional e 3 da de produto). **Zero falha de qualquer outro tipo**: o
resto da página estava são, e a linha de base ficou medida.

### AS DUAS IRMÃS ACHARAM O QUE A 32.5-c MANDA PROCURAR NA MESMA PASSADA, e as duas estavam certas

A 32.5-c diz, com todas as letras, que *"quem conserta a folha de um snippet procura o mesmo defeito nas
irmãs antes de fechar"*. Aqui as irmãs **se acusaram sozinhas**, na bancada, antes do desembarque:

- **`teste-f2.py` reprovou** porque ele mede, no fonte, que **toda função de nível superior da casca está
  atrás de uma guarda `if ( ! function_exists() )`** — e a primeira versão deste bloco punha as duas funções
  novas sob a **mesma** guarda. Guarda compartilhada mente no dia em que uma das duas existir e a outra não.
  Cada uma ganhou a sua.
- **`teste-institucional.py` reprovou duas vezes** — "o PHP não tem a folha desta família" e um caso de
  autoteste — porque ele achava a folha pela **tag** `<style id="rdm-inst-folha">`, que acabou de sair do
  snippet. **Defeito da RÉGUA e não da folha:** o que a folha É não mudou, é o texto entre a abertura e o
  fechamento da captura. Ela passou a achá-la pelo **par de captura**, e ganhou um caso de autoteste novo
  que cobra que o **HTML cru** do snippet não traga mais tag `<style>` nenhuma.

### O DESEMBARQUE, E O QUE FOI MEDIDO NO AR (18.4)

**Revisão 42 no ar às 19h39:51Z.** O cron é de 30 minutos e **roda por visita, não por relógio** (20.6): o
disparo anterior foi 19h16:45Z e o push saiu às 19h31Z — `ultimo` **recente mas anterior ao push** é o
terceiro mundo que a 20.6 separa, **turno de cron**, nem defeito nem cache, e o que resolve é esperar o
turno **mantendo as visitas de pé**. O `raw.githubusercontent.com` já servia 42 na primeira leitura.

**O LOG LIDO DO FECHO PARA BAIXO (20.4 e 20.8).** A linha de fecho declara **`7 aplicado(s)`** e do fecho
até a próxima linha de revisão há **exatamente 7 linhas de item**, as sete dizendo **`ok`** — a conta do
portão fecha com a declarada, então **a janela não rolou e não há item fora da conferência**. Os três
snippets no meio delas: `rodametria-institucional` (#9), `rodametria-produto` (#8) e `rodametria-casca`
(#6), os três `atualizado`.

**A VERSÃO CARREGADA PELO WORDPRESS (20.7), não a do byte do repositório:** `/casca` → `versoes` devolve
`rodametria-casca 1.10.0`, `rodametria-f2 1.5.0`, `rodametria-institucional 1.2.1`,
`rodametria-produto 1.7.1` — **4 de 4 conferidas contra o manifest**, e o `id` de nenhum está ausente, que
é a prova de que nenhum snippet ficou *gravado e não ativado*.

**OS COMENTÁRIOS, RECONTADOS NO AR, URL POR URL, COM QUEBRA DE CACHE:**

| URL | antes | depois | página |
|---|---|---|---|
| `/` | 23 comentários · 7.486 B | **0 · 0 B** | 89.162 → **81.616** |
| `/autonomia-patinete-eletrico/` | 23 · 7.486 B | **0 · 0 B** | 113.073 → **105.527** |
| `/veiculos/` | 24 · 7.866 B | **0 · 0 B** | 93.174 → **85.248** |
| `/veiculos/patinete-eletrico/` | 24 · 7.866 B | **0 · 0 B** | 116.946 → **109.020** |
| `/veiculos/bicicleta-eletrica/` | 24 · 7.866 B | **0 · 0 B** | 105.686 → **97.760** |
| `/sobre/` | 24 · 7.827 B | **0 · 0 B** | 92.266 → **84.379** |
| `/contato/` | 24 · 7.827 B | **0 · 0 B** | 91.315 → **83.428** |
| `/divulgacao-de-afiliados/` | 24 · 7.827 B | **0 · 0 B** | 92.701 → **84.814** |
| `/privacidade/` | 24 · 7.827 B | **0 · 0 B** | 93.812 → **85.925** |

**Zero em 9 de 9**, e a página encolheu de **7.546 a 7.926 bytes**. Os 17 blocos `<style>` do WordPress
continuam lá, com os comentários deles intactos — como tem de ser.

**`conferir-no-ar.py`: 481 afirmações, 0 falha** (eram 524 com 43 falhas antes do desembarque; a diferença
na contagem é que as afirmações de bastidor que falhavam somavam por termo).

**E A PROVA DE QUE A FOLHA CONTINUA PINTANDO IGUAL, que é a única que vale: o portão de pixel da 32.5
devolveu os 27 números das 9 páginas BYTE POR BYTE IDÊNTICOS aos de antes do desembarque** — `diff` vazio
entre as duas saídas. Caixa 331 · 329 · 244 · 244 · 244 · 211 · 405 · 211 · 211 px (teto 700); primeiro
botão de compra **1.279 · 1.165 · 1.092 px** (teto 1.400); altura 2.652 · 5.108 · 3.344 · 3.918 · 5.064 ·
3.850 · 3.574 · 4.018 · 6.373 px; 9 de 9 no molde, 0 fora, 0 disputa de especificidade latente. **A mesma
medição foi feita ANTES do desembarque de propósito**, com a folha velha, para que a comparação fosse de um
instrumento com ele mesmo e não de um número lembrado.

**Bancada com rede DEPOIS do desembarque: 32 portões, 0 falha** (28 sem rede, e o portão novo entrou na
bancada no dia em que foi escrito, porque ela descobre por convenção de nome).

### A REGRA SUBIU PARA O CONTRATO, E O ENDEREÇO DELA NAS OUTRAS ILHAS É DESPACHO

**`ARQUIPELAGO.md` ganhou a 32.4-b**, em três partes: o comentário fica no repositório e não vai na folha
impressa (a tag `<style>` sai dos snippets e vira função da casca, para folha nova nascer dentro do
conserto); a régua da 32.4 passa a medir o **HTML servido inteiro**, numa afirmação separada; e tirar
comentário de CSS **quebra CSS**, com as travas de string, `url()`, comentário colado e comentário sem
fechar, mais a conta de tokens e o portão de pixel depois do desembarque. **É a 20.4 aplicada a si mesma:**
*"conserto escrito em registro de ilha conserta aquele dia; regra escrita aqui vale para as três ilhas"*.

**E um despacho NORMAL novo em `dados/despachos.md`** para quem reservar a **aquametria**, a **robometria**
ou a **clubedomosaico**: as três têm snippets com folha e comentário de prosa dentro dela — é o desenho
desta fábrica, e esta ilha o herdou pronto. O despacho é escrito como **pergunta**, pela lição de 16/10:
despacho que afirma o estado de ilha que quem o escreve não reservou está afirmando sobre arquivo que ele
não pode abrir para conferir. Ele manda **medir primeiro** (e fechar escrevendo zero, se for zero), separar
os blocos do WordPress dos da ilha, **copiar os dois portões em vez de reescrevê-los** (a parte difícil é a
lista de exceções, e ela está medida) e rodar o pixel **depois**.

### O QUE FICA, E É A FILA HONESTA DESTA ILHA

**O bloco 7 era o último pré-registrado.** O que sobra da fila continua travado pelas mesmas três coisas,
nenhuma delas de código:

- **F1** (bloco 4) — o limiar legal segue `pendente` e os cinco domínios oficiais seguem recusados pelo
  egresso. **Despacho ALTA de 28/10, não remedido nesta passada** porque este bloco não dependia dele.
- **F3** — falta `carga_max_kg` em registro com oferta aberta, e o nível 5 da escada (os três varejos
  grandes) está atrás do egresso. **Despacho ALTA de 29/10.**
- **Página nova de malha** — a **30.8** proíbe afirmar veredito `alvo` desta nuvem, e as duas consultas que
  faltam esperam o **despacho de 30/10** (duas SERPs e um volume, numa sessão de Chrome do Raphael).

**O CANDIDATO A PRÓXIMO BLOCO, e a primeira coisa a fazer com ele é conferi-lo e não executá-lo:** o
**artigo-âncora pareado com a F2** (bloco 5), que é a única peça da fila cuja ferramenta par **já está no
ar**. Antes de abri-lo, a próxima execução lê a **seção 17** (guia é o terceiro nível da malha, não blog) e
a **30.8**: se o artigo-âncora precisar de veredito de SERP para existir, ele está atrás do mesmo despacho
de 30/10 que as páginas de produto, e aí a resposta honesta é dizer isso em vez de publicar sobre consulta
não medida.

---

## 2026-11-04 16h17Z–17h13Z — **A TRAVA DA 32.5-d COBRIU UM SELETOR E 24 REGRAS DO MOLDE SEGUIAM PERDENDO** — e o bloco de telefone escrito para comprar pixel nunca valeu um pixel

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10), e pela **1.2**
não há escolha a fazer — e esta execução tem, além do foco, **despacho aberto na própria ilha em foco**: a
ronda diária de hoje (14h3xZ–15h0xZ) deixou **cinco itens**, o item 1 marcado **ALTA**. **As duas exceções
que furam o foco foram conferidas ANTES da reserva e nenhuma furou**: nenhum despacho ALTA em ilha fora do
foco que esteja **no ar E quebrada** (o único aberto fora do foco é a ronda NORMAL da robometria de 02/11,
em ilha no ar e sã) e o **despacho do molde da 32.6** segue FECHADO nas três ilhas. `executando_desde`
estava `null`, que pela **1.1** já é prova de que não há bloco da Fundação vivo. Reserva às **16h17Z**,
renovada às **16h46Z**. Nenhum branch `claude/*` com commit fora do `main` e nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os dois em
**200 em TRÊS passadas**, com `aquametria.com.br` em **200 nas mesmas três**.

**O DESPACHO SAIU INTEIRO (18.2): os CINCO itens.** O que segue é por item, e o item 1 é o que vale guardar.

### ITEM 1 — A SENTINELA MEDIU 1.402 px, ESTA NUVEM MEDE 1.380, E AS DUAS ESTÃO CERTAS: O DEFEITO ERA MAIOR QUE OS DOIS NÚMEROS

**A PRIMEIRA COISA FOI REMEDIR, e o número não bateu.** O portão de pixel desta ilha, lendo o
`wp-sitemap.xml` no ar e abrindo as 9 URLs a 390 px num Chromium de verdade, devolveu **1.380 px** para
`/autonomia-patinete-eletrico/` — 20 px DENTRO do teto —, contra os **1.402 px** que a ronda mediu três
vezes no Chrome do Raphael. A medição foi repetida em **cinco instrumentos** desta nuvem (UA de iPhone com
`deviceScaleFactor` 2 e 1, UA de desktop, viewport mais alto, e **dentro de um iframe de 390 px numa janela
de 1536**, que é exatamente como a ronda mediu): **1.380 px e `scrollHeight` 5.196 nos cinco**, contra
5.339 dela. A fonte do Google carrega aqui (as seis respostas em 200), e a foto do cartão foi conferida
carregada (`naturalHeight` 1024, servida a 96 px). **Não há como esta execução dizer qual dos dois números
o visitante vê** — e com 20 px de folga a pergunta não precisa de resposta: o parágrafo de escopo do bloco
de compra ocupa **três linhas de 19,7 px** e está a um caractere da quarta. Teto que se decide por uma
quebra de linha não é teto.

**E PROCURANDO DE ONDE TIRAR FOLGA, APARECEU A CAUSA DE VERDADE, que não é desta página: é da CLASSE que a
32.5-d nomeou em 29/10 e consertou pela metade.** Aquele dia mediu que `body.rdm img{height:auto}` vale
(0,1,2) e vence `.rdm-molde-cartao-foto`, que vale (0,1,0) — e pôs `body.rdm` **no seletor da foto. Só no
da foto.** Duas telas acima, na mesma folha, mora `body.rdm p{margin:0 0 16px}`, que vale (0,1,1) e vence
**toda** declaração do molde que ficou em (0,1,0).

**MEDIDO, com a régua nova, nas 9 URLs do ar: 21 declarações do molde perdidas só na página da F2.** As
três que custam o botão estão DENTRO do cartão: `cartao-nome`, `cartao-spec` e `cartao-preco` declaram
`margin:0` e a página servia **16 px cada uma** — **48 px empilhados logo acima do botão que a 32.5 mede**.

**E A IRONIA É EXATA:** o bloco de telefone desta folha foi escrito em 29/10 **para comprar pixel**, com
`escopo{margin-bottom:8px}` e `titulo{margin-bottom:4px;font-size:1.125rem}` — e **nenhuma dessas linhas
nunca valeu um pixel**, porque *media query não acrescenta especificidade*. A página servia 16 onde a folha
pedia 8, 12 onde pedia 4 e corpo de 22 px onde pedia 18. É a mesma família da linha `height:44px` morta que
a própria 32.5-d achou três telas abaixo, com uma diferença que importa: aquela perdia para uma **irmã**,
escrita depois com a mesma especificidade, e estas perdem para uma regra **genérica** da casca, que ninguém
lê quando mexe no molde.

**O CONSERTO É DE ESPECIFICIDADE E NUNCA `!important` (32.5-d item 2):** **24 regras** passaram a carregar
`body.rdm`, as das media queries incluídas, para a ordem relativa entre elas não mudar — prefixar metade
seria trocar um defeito calado por outro.

**A TRAVA NASCEU NA MESMA PASSADA, e ela é da CLASSE e não desta página.**
`conferir-32-5-no-navegador.mjs` ganhou duas afirmações novas:

1. **A disputa de especificidade.** Em cada página do molde ele varre todo elemento com classe `rdm-`, acha
   a regra do molde de maior especificidade e a regra NÃO-molde de maior especificidade para sete
   propriedades de espaço, e **REPROVA quando a genérica vence E o valor servido discorda do declarado**,
   nomeando seletor, propriedade, declarado e servido. Quando a genérica vence com o **mesmo** valor ele
   chama de **LATENTE** e imprime — foram **47 latentes** nesta medição, e era nesse estado que as 48 px
   esperavam. O que o molde declara é descoberto aplicando a declaração **inline** no próprio elemento e
   relendo o computado: as variáveis resolvem no lugar certo da árvore, e não há valor adivinhado.
2. **A foto é de verdade.** O portão passa a dizer, em toda página que vende algo, **quantos cartões têm
   foto carregada e quantos têm o reservado**, e reprova `<img>` que não carregou. A 32.5-d existe porque o
   portão "aprovava a página de verdade, com o número de verdade, sobre um cartão que nenhum visitante com
   foto jamais veria" — e o portão que ela consertou **continuava sem saber dizer qual dos dois mundos ele
   mediu**.

**E A FOTO ENSINOU UMA COISA SOBRE O PRÓPRIO INSTRUMENTO, medida às 16h5xZ:** a mesma página devolveu
`foto 1/4 real` numa passada e `0/4` na seguinte, com a CDN da loja respondendo **200 e 197 KB** para
`curl` nas duas. A causa é o `loading="lazy"` do cartão — ele está a 1.128 px, fora da primeira tela, e
`waitUntil: 'load'` **não espera imagem preguiçosa que o navegador ainda não decidiu buscar**. Portão que
responde diferente na mesma página é portão que alguém passa a ignorar (a lição da 20.5). Agora o portão
põe a página no estado em que o visitante a vê ao chegar ao bloco: `eager` e `decode()`, com **uma segunda
tentativa** recarregando o `src`. Foto que não carrega em duas tentativas é defeito de verdade.

**O `--autoteste` É O QUE PROVA QUE A TRAVA MORDE, e ele não precisa de rede** (então roda sempre na
bancada): quatro mundos fabricados com `setContent`, **7 afirmações**. O mundo 2 é o de 29/10 a 04/11 — o
molde sem prefixo — e nele a afirmação é a que a 20.8 exige com todas as letras: **a régua VELHA (só pixel)
APROVA o mesmo mundo que a régua NOVA reprova.** Autoteste em que as duas concordam não mede conserto
nenhum. O mundo 4 é a disputa **latente**, que tem de ser impressa e **não** reprovar.

### ITEM 2 — `dateModified` POR FILTRO, E A CASCA NÃO INVENTA DATA

O defeito medido pela ronda: **zero** ocorrência de `dateModified` e **zero** de `datePublished` em todo o
JSON-LD das 9 URLs, numa ilha cujo produto é *"o preço de hoje"*. A casca passou a servir um nó `WebPage`
com `dateModified`, e **a data não é dela**: vem de um filtro (`rodametria_data_da_pagina`) em que cada
snippet pendura a data **que a própria página publica em prosa** — a F2 e a home, o `gerado_em` do banco da
F2; as duas de produto, o `colhido_em` da sua vitrine (o mesmo campo que a prosa imprime como `{DATA}`); a
mãe, a **mais recente** das datas das filhas; as quatro da 16.1, o `gerado_em` de
`paginas-institucionais.json`.

**POR QUE FILTRO, e não um campo da casca:** a casca não sabe de que dado cada página é feita, e quem sabe
é o snippet que a renderiza — o mesmo mecanismo que a **20.7** já usa para a versão do snippet carregado. E
**sem ninguém pendurando, o nó não sai**: cair no relógio do servidor publicaria *"modificada hoje"* em
página que não muda desde 30/10, que é exatamente a mentira que um sinal de frescor pode contar.

**A TRAVA É NO AR, E É DE DUAS PARTES.** `conferir-no-ar.py` passou a exigir `dateModified` em **toda URL
do sitemap** e, quando a página publica alguma data em prosa, que a data servida **esteja entre elas** — se
as duas declarações do mesmo fato não forem o mesmo campo, uma sobe e a outra fica (20.7). Página sem data
em prosa recebe **registro** e não falha: não há com o que cruzar, e dizer isso é mais honesto que aprovar
em silêncio.

### ITEM 3 — O CARROSSEL ESCOLHE POR PREÇO, E A ESCOLHA É DE PREÇO PORQUE É O QUE ESTÁ MEDIDO

O carrossel da bicicleta era **os cinco primeiros** de `servem`, e os cinco custavam **R$ 2.299,99** em
cinco lojas; a única oferta de outro preço (R$ 6.199,90) ficava de fora, e a mediana da página **era o
mínimo** dela. A frase de faixa é o primeiro parágrafo da página e não informava nada.

**`escolher_carrossel()` é função pura e tem três passadas:** (1) **uma vaga por preço**, na ordem da seção
7; (2) as vagas que sobraram, com **no máximo uma repetição por preço** — a segunda oferta de um preço é
outra **loja**, que é informação para quem compara, e a terceira não acrescenta nada; (3) o **piso de três
da 32.1 vence o teto de duas ocorrências**, e só ele, porque família que de fato tem um preço só sairia com
dois cartões e carrossel de dois não é o molde.

**NÃO foi deduplicação de "oferta equivalente", e a razão é de método:** dizer que dois anúncios de duas
lojas são o mesmo produto exigiria afirmar o que esta ilha **não mede** — título parecido não é prova, e a
25.9 já ensinou o que custa casar anúncio por semelhança. **Preço é campo medido**, lido da loja na mesma
passada.

**A bicicleta sai de 5 cartões num preço para 3 cartões com dois preços**; o patinete segue com 5 cartões e
5 preços. **O portão nasceu antes do conserto e o pegou**: rodado com o dado de ontem,
`gerar-vitrine-de-produto.py --conferir` reprovou com a frase *"a tabela tem 2 precos distintos e o
carrossel serve 1"*. Mais **cinco mundos fabricados** para a função pura (os dois de hoje e três que o banco
não produz, entre eles a família de um preço só), e **uma mutação nova** em `mutacoes-produto.py` que
refabrica o defeito de hoje.

**E UMA MUTAÇÃO VIROU INERTE NO MESMO GESTO, que é pior que sobrevivente:** `carrossel acima do teto de
cinco` exigia que a página[0] estivesse **exatamente** no teto, e a bicicleta caiu para três. Mutação presa
ao tamanho do dado de hoje mede o dado e não o portão — ela passou a **empilhar** cartões até passar do
teto, seja qual for o tamanho de onde começa.

### ITEM 4 — `intestavel` ERA UMA VARIÁVEL LOCAL DENTRO DO PORTÃO

A 25.9 (item 2) diz, com todas as letras, que campo declarado em todo registro existe *"pela mesma razão do
`intestavel`"* — e nesta ilha o `intestavel` era **o único conceito não declarado**: vivia como uma
variável local de 20 linhas dentro de `validar-banco.py` (`bool(url) and not url_produto`). **A ronda que
media "0 intestável" nesta ilha estava medindo a ausência da chave.**

Agora ele é **derivado**, como o `energia_wh`: `derivar-banco.py` escreve nos **20 registros** dos dois
bancos (17 de `veiculos.json` e 3 de `pecas.json`, todos `false` hoje) e **`validar-banco.py` RECALCULA e
reprova divergência** — duas metades que existem para discordar. Chave ausente reprova; `true` sem
`motivo_sem_url_produto` reprova. O esquema declara o campo (versão **4 → 5**, com os dois bancos
acompanhando; a PECA herda do VEÍCULO e por isso basta declarar lá). **Três mutações novas** em
`mutacoes-banco.py`, e a do meio é a que importa: `intestavel: false` num item que **perdeu** o
`url_produto` — o mundo em que o espelho envelheceu calado.

**E o fixture da bateria pagou a regra na hora:** `registro_publicavel()` montava um `afiliado` sem a
chave, e os dois mundos-que-têm-de-passar reprovaram no minuto em que o portão nasceu.

### ITEM 5 — A DATA DO MANIFEST SOBE COM A REVISÃO, DO RELÓGIO

`manifest.json` dizia `atualizado_em: 2026-11-02` na revisão **40**, publicada em 04/11: a revisão subia
sozinha e a data era **digitada**. Agora `atualizar-manifest.py` escreve as duas no mesmo gesto, com a data
lida do `date -u` da própria passada, e **imprime a troca** como imprime as outras.

**E o `--conferir` NÃO exige "hoje", de propósito:** manifest em dia hoje continua em dia amanhã, e portão
que reprova manifest certo é o caminho mais curto para alguém ignorá-lo (20.5). Ele compara com a data do
**último commit que tocou o manifest** — e, em clone **raso**, diz que **não pôde conferir** em vez de
aprovar com cara de completo (a lição do `git log` raso da 1.1).

### O ACHADO QUE NÃO ERA DE NENHUM DOS CINCO ITENS: **A FÁBRICA FALA DENTRO DO `<style>` DE TODA PÁGINA**

Apareceu ao extrair as datas em prosa das 9 URLs para o item 2, e é um defeito da **32.4** que **nenhum
portão desta ilha vê**. Medido no HTML servido de `/autonomia-patinete-eletrico/` às 16h4xZ:

- a página tem **110.182 bytes**; os 18 blocos `<style>` somam **67.916**;
- dentro deles vão **39 comentários de CSS, 6.042 bytes** — **8,9% do CSS e 5,5% da página**;
- **6 comentários, 3.745 bytes**, trazem vocabulário que a 32.4 proíbe **com todas as letras**: `snippet`,
  número de seção do contrato (`32.5`, `secao 6`), nome de rotina (`conferir-32-5-no-navegador.mjs`) e
  prosa de bastidor (*"Medido no ar a 390 px em 29/10/2026, na primeira foto que a ilha teve"*).

**POR QUE PASSOU:** a régua de bastidor da ronda e a desta ilha leem o **texto visível** — `corpo_da_pagina`
tira `<script>` e `<style>` antes de medir, e com razão, porque ali mora CSS e não prosa. **Só que a 32.4
não é sobre o que o leitor vê: é sobre o que a página SERVE**, e é o HTML servido que a visão geral de IA
ingere. Comentário de folha é invisível para o visitante e perfeitamente legível para quem lê o fonte.

**E ESTA EXECUÇÃO AUMENTOU O NÚMERO**, o que é a parte honesta de registrar: o comentário novo que explica
as 24 regras prefixadas tem ~2,3 KB e vai para a mesma folha. O conserto não é apagar o comentário — ele é
a memória da ilha e mora no repositório, que é o lugar dele (seção 3) — é **não servi-lo**: a casca tira os
comentários da folha ao imprimi-la. Está pré-registrado como o próximo bloco no `PROMPT.md`, com o portão
que falta nomeado, porque mexer em folha no mesmo desembarque que conserta a 32.5 trocaria duas variáveis
ao mesmo tempo no número que a 32.5 acabou de medir.

### O FECHO, E OS NÚMEROS SÃO DO AR

**Revisão 41 no ar às 17:10:01Z.** O log do `/status` foi lido **DO FECHO PARA BAIXO** (20.8): a linha de
fecho declara **`8 aplicado(s)`** e abaixo dela vêm **8 linhas de item, todas dizendo `ok`** — as quatro de
dado e os quatro snippets. E as versões foram conferidas **no ar**, no endpoint público da casca, que é o
mecanismo da **20.7**: casca **1.9.0**, f2 **1.5.0**, institucional **1.2.0**, produto **1.7.0** — nenhum
`id` ausente, nenhuma versão divergente.

**O CRON, e vale registrar porque custou 24 minutos desta execução:** o Sync desta ilha roda por
`rodametria_30min` e a passada anterior foi às **16h41**, três minutos antes do push. A **20.6** está certa
sobre o que ACORDA o cron (requisição, não relógio) e **não** dispensa o intervalo: visitar a home não
antecipa uma passada que ainda não venceu, só garante que a vencida rode. A revisão entrou na primeira
passada devida, **17h10**, com a home sendo visitada a cada 40 segundos desde 16h47.

**A 32.5 NO AR, a 390 px, nas 9 URLs do sitemap, com foto de verdade no cartão:**

| página | antes | agora | foto |
|---|---|---|---|
| `/autonomia-patinete-eletrico/` | 1.380 px | **1.279 px** | 1 real, 3 reservados |
| `/veiculos/patinete-eletrico/` | 1.281 px | **1.165 px** | 5 de 5 reais |
| `/veiculos/bicicleta-eletrica/` | 1.209 px | **1.092 px** | 3 de 3 reais |

**Zero foto quebrada**, caixa pior em 405 px (teto 700), **9 de 9 páginas dentro da 32.5** e — o número que
mais diz — **disputas de especificidade LATENTES: 47 → 0**. Toda declaração do molde desta ilha agora vale
o que diz.

**`dateModified` conferido URL por URL no ar:** `2026-11-04` na home, na mãe, na F2 e nas duas de produto;
`2026-10-30` nas quatro da 16.1. Nó `WebPage` em todas as 9, ao lado do `BreadcrumbList`, do `ItemList` e
do `FAQPage` que já existiam — **nenhum deles mudou** (32.3).

**O carrossel da bicicleta, lido abrindo a página:** **3 cartões, 2 preços** — `R$ 2.299,99` (3B LOJA),
`R$ 2.299,99` (Boa sorte vem) e `R$ 6.199,90` (NEGOCIO VELOZ).

**BANCADA COM REDE: 31 portões, 0 falha, DEPOIS do desembarque** — os 27 sem rede mais os quatro de ar
(`conferir-32-5-no-navegador.mjs`, `conferir-no-ar.py`, `conferir-produto-no-ar.py`,
`conferir-institucional-no-ar.py`). Dois portões novos entraram na bancada **no dia em que foram escritos**,
sem ninguém os listar, porque ela descobre por prefixo de nome.

**PRÓXIMO PASSO DESBLOQUEADO: o bloco 7 da fila** — a folha da casca não servir os próprios comentários. É
o único defeito que esta execução **mediu e não consertou**, e a razão está escrita no item da fila: mexer
na folha duas vezes no mesmo desembarque trocaria duas variáveis no único número que a 32.5 tem como prova.

## 2026-11-04 13h19Z–13h4xZ — **A CLASSE TINHA TRÊS CAMADAS E A TRAVA ALCANÇAVA DUAS** — e a terceira escreve a prosa DENTRO DO PHP, que o cabeçalho do portão de produto já dizia por escrito

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10), e pela **1.2**
não há escolha a fazer. **As duas exceções que furam o foco foram conferidas ANTES da reserva e NENHUMA
furou.** (a) Os **três despachos do molde** da seção 32 estão **FECHADOS**, lido no topo dos três
`PROMPT.md` (aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ). (b) Nenhum
despacho **ALTA** é de ilha **no ar E quebrada**: o único aberto fora do foco é a ronda **NORMAL** da
robometria de 02/11, em ilha no ar e sã. `executando_desde` estava `null`, que pela **1.1** já é prova de
que não há bloco da Fundação vivo, e o último commit da ilha era de **11h15Z, 2h04 atrás** — não houve
reserva vencida para o git desempatar. Reserva às **13h19Z**, renovada às **13h25Z** e às **13h37Z**. Zero
PR aberto, e o branch `claude/dreamy-mccarthy-9c0nhm` sem um commit fora do `main`.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os dois em
**200 em TRÊS passadas**, com `aquametria.com.br` em **200 nas mesmas três**.

**A PRIMEIRA COISA FOI PROCURAR DEFEITO (18.5), e no chão não havia nenhum:** bancada **com rede, 29
portões, 0 falha**, antes de uma linha de código. O defeito estava **no ar**, em três páginas, e nenhum
portão do chão podia vê-lo.

### O BLOCO QUE O `ESTADO.md` NOMEAVA: A RECOLETA — e ela vale pela DATA, não por a faixa mudar

Na ordem que o campo mandava (`coletar-por-consulta --gravar`, depois
`coletar-piso-da-vitrine --gravar`, depois `coletar-oferta --gravar`, e só então gerar).

**O CATÁLOGO NÃO MUDOU:** 20 ofertas lidas por consulta, **16 e 6** servem (as mesmas de ontem — **zero
saiu e zero entrou**), mesmo degrau 1 de chave em cada uma, mesmas recusas por causa. **O que mudou foi
preço em DUAS ofertas do carrossel do patinete** (R$ 1.489,00 → **R$ 1.490,00** e R$ 1.565,25 →
**R$ 1.581,06**) e a venda declarada da oferta casada do `honeywhale-m2-max` (**5 → 4**).

**E A FAIXA PUBLICADA E A MEDIANA NÃO SE MOVERAM** (R$ 1.030,00 a R$ 2.699,00, mediana R$ 1.647,95). É
por isso que a recoleta **não pode depender de a faixa mudar para valer**: as duas páginas dizem *"à venda
hoje"* com a data ao lado, e a data era **de ontem**. O que envelhece primeiro é a afirmação de data, não
o número.

**COTAÇÃO É SÉRIE E A SÉRIE CRESCEU:** a leitura de hoje entrou como item **novo** em `cotacoes[]`
(R$ 2.299,00, 4 vendas, 04/11), com a de 03/11 **preservada** embaixo — leitura nova não substitui leitura
velha, porque substituir apaga a série.

**MEDIDO, NÃO AFIRMADO — a ordem dos coletores é cobrada por PORTÃO e não por prosa.** O campo do
`ESTADO.md` diz *"a ordem importa"*, e `coletar-por-consulta --gravar` de fato **apaga** o `piso_da_busca`
que o passo seguinte repõe. Em vez de registrar que li o código, removi o `piso_da_busca` num **mundo
fabricado** e os **dois** portões ficaram vermelhos — `coletar-piso-da-vitrine --conferir` (*"abre o portão
da 30.2 e não tem `piso_da_busca`"*) e `gerar-vitrine-de-produto --conferir` —, e restaurei o arquivo. A
prosa não estava sozinha.

**PLACAR DO CASAMENTO, igual ao de 03/11:** `casou 1 · mercado_nao_anuncia 3 · candidato_barrado 0 ·
sem_identidade_minima 13`, 10 ofertas julgadas e 6 barradas.

### E DEPOIS O BLOCO VIROU OUTRO: A VARREDURA QUE A EXECUÇÃO DA MANHÃ PEDIU, FEITA NO AR

O campo `bloco_atual` da manhã fechou com uma frase que é uma ordem de serviço: *"QUEM ABRIR BLOCO DE
CONTEÚDO AQUI procura afirmação sobre o catálogo SEM quantificador: venda, 'o mercado', 'o mais comum'"*.
Fiz a varredura nas **9 URLs servidas**, e ela achou **três** afirmações da mesma classe, **uma em cada
camada**:

| URL | a frase | camada |
|---|---|---|
| `/veiculos/bicicleta-eletrica/` | *"é a **reclamação mais comum** de quem compra sem fazer essa conta"* | declarada (produto) |
| `/divulgacao-de-afiliados/` | *"a maneira **mais comum** de prometer um aparelho e entregar outro"* | declarada (institucional) |
| `/autonomia-patinete-eletrico/` | *"É a lacuna **mais comum** do varejo"* | **prosa dentro do PHP** |

**NENHUMA TEM UM DÍGITO E NENHUMA TEM UM QUANTIFICADOR**, e é exatamente por isso que as duas travas
anteriores — a de dígito (que reprova QUALQUER dígito) e a de quantificador por extenso, escrita hoje de
manhã — **aprovavam as três, as duas verdes**. *"Mais comum"* não é quantificador: é **superlativo**, e a
classe estava **uma palavra fora da régua**.

### (1) A TERCEIRA É A QUE IMPORTA, E O PORTÃO JÁ AVISAVA DELA POR ESCRITO

O cabeçalho do `conferir-produto-no-ar.py` traz, escrito **antes** deste dia, a razão de a lista de termos
ser duplicada:

> *"a lista está DUPLICADA de propósito: aquele portão julga o REPOSITÓRIO e este julga o AR, e **há um
> mundo entre os dois — prosa escrita direto no PHP, que a camada declarada não vê**."*

A prosa da F2 vive dentro de `snippets/rodametria-f2.php`, e a frase do varejo está no ar **desde
29/10/2026**. **Portão por CAMADA nunca alcança camada que não tem camada declarada** — e a aquametria, a
clubedomosaico e esta ilha vão ganhar camadas novas de página.

**ENTÃO O CONSERTO DEIXOU DE SER UM PORTÃO POR CAMADA E PASSOU A SER UM PORTÃO POR SITE.**
`conferir-no-ar.py` — o único que varre o **sitemap inteiro** — ganhou a classe e **não sabe de camada
nenhuma**: toda URL publicada passa por ela, e as liberações saem das **três** listas declaradas juntas,
porque **a liberação é da FRASE, não do portão que a encontrou**. Camada nova de página nasce **já
coberta**, que é o contrário do que aconteceu três vezes em três dias (02/11 a mãe fora de todo portão,
03/11 a frase nomeada no laço das filhas, 04/11 de manhã a classe em duas camadas).

A terceira lista nasceu hoje: `dados/liberacoes-de-quantificador.json`, para **a camada cuja prosa não tem
camada declarada**.

### (2) O QUE SUBSTITUIU A FRASE DA BICICLETA É UMA CONTAGEM, e ela é a tese da ilha medida na própria vitrine

A frase mandava *"olhar a tensão e a amperagem, e passar os dois na calculadora de autonomia"* — instrução
**correta** — e emendava um ranqueamento de reclamação que **esta ilha nunca mediu**. O número que ela devia
dizer estava a um `grep` de distância:

> **Dos 22 anúncios que esta ilha publica, ZERO declara a TENSÃO E a AMPERAGEM no mesmo título.** 1 de 6 e
> 1 de 16 declaram **só a tensão**; **nenhum** declara a amperagem.

**A página mandava usar uma calculadora cujas duas entradas a própria vitrine não entrega** — *"todos
falam, ninguém calcula"*, como o pivô da F1 na véspera. Régua nova em
`teste-relevancia-do-anuncio.py` (`declaracao_do_par_da_f2` e `contagem_do_par_da_f2`), **leitura de UNIDADE
e nunca de número solto**: `48v` é tensão, `10ah` é amperagem, e `43kmh` e `10km` não são nenhuma das duas;
borda assimétrica igual às irmãs (`1048v` não é tensão, `48va` não é). Molde `{FRASE_DO_PAR_DA_F2}` com
**sete mundos fabricados** — e **o mundo "os dois declarados" NÃO EXISTE em anúncio nenhum desta vitrine**,
que é precisamente por que ele está fabricado (seção 8). **Duas mutações** do regex matam a régua, 3 e 2
falhas.

**A frase do PHP da F2 passou a dizer a contagem que a própria função tinha na mão** — `12 dos 17 registros
deste banco` —, e a da página de divulgação **perdeu o ranqueamento sem ganhar número**: *"os dois terminam
do mesmo jeito: o título promete um aparelho e a caixa traz outro"*. No mesmo dia saiu **"quem pesa mais que
a MÉDIA"** do rótulo de um segmento: média de peso de pessoa não é dado desta ilha.

### (3) A TRAVA DE DÍGITO REPROVOU A FRASE CERTA, E O CONSERTO NÃO FOI RENOMEAR O MOLDE

`{FRASE_DO_PAR_DA_F2}` carrega o **`2` do nome da ferramenta**, e a trava de dígito — que reprova
**qualquer** dígito na camada declarada, por decisão medida de 03/11 — leu o nome do molde como **número
digitado**, reprovando justamente a frase que **substituiu** uma afirmação inventada por uma contagem.

**Todo molde desta ilha nasceu sem dígito** (`{FRASE_DA_CARGA}`, `{DECLARAM_WATT}`), então a trava **nunca
encontrou um** e o buraco era invisível. **Fugir renomeando o molde faria o próximo `{FRASE_DA_F1}` pagar
igual** — é a 32.5-c de novo. A trava passa a **tirar os MOLDES antes de procurar dígito**, com a forma
estreita que o PHP de fato substitui (`{` + maiúscula + `}`), e **duas mutações novas provam que ela não
virou "tudo entre chaves passa"**: dígito **colado** num molde de verdade **REPROVA**, e
`{frase_do_par_da_f2}` em **minúscula** (que o PHP não substitui, e que iria para a tela como está)
**REPROVA**.

### (4) E O PORTÃO NOVO ACHOU UMA QUARTA, NA MESMA PÁGINA DE PHP — e esta tinha MEDIÇÃO por trás

Rodado contra o ar depois do desembarque, o laço do site inteiro reprovou uma ocorrência que **nenhum dos
outros dois portões acharia**, na mesma camada de PHP:

> `/autonomia-patinete-eletrico/` — *"O número do fabricante **costuma** ser de condição ideal"*

**Esta é diferente das três, e a diferença é tudo:** ela tem medição por trás, e a medição é justamente a
que esta página publica — a constante `calibracao-autonomia-declarada-contra-medida` (`publicavel`,
`usada_em: [F2]`), **29,8 km medidos contra 60 km declarados, 49,7%**, da tese da UPS Quito de 2025, com
autor, tutor, instituição e ano, servida como linha nomeada na tabela pré-renderizada da própria página. O
corpus de 28/10 também registrou a faixa agregada de 60% a 80% **sem fonte única**, e a medição nomeada cai
**abaixo** do piso dela — a faixa agregada era otimista. **Então ela foi LIBERADA por escrito, não
apagada**, e o portão fez o trabalho que nenhuma lista de palavras faz sozinha: separou a frase sem fonte da
frase com fonte, obrigando alguém a olhar as duas.

### (5) A ÂNCORA É POR OCORRÊNCIA E NÃO POR PARÁGRAFO, e isso foi medido no mesmo portão

A primeira liberação da **média geométrica** da F2 usava como âncora *"a média simples porque a grandeza é
um multiplicador"* — e a frase servida diz **"a média simples"** DUAS vezes, uma de cada lado do `porque`:
*"A gente escolheu o geométrico e não a média simples porque a grandeza é um multiplicador, e **a média
simples** puxaria o meio para perto da ladeira sem base."* O portão **denunciou a segunda**, que é a leitura
certa, e a âncora foi alargada para a frase inteira. **Liberação estreita demais é liberação que parece
conferida** — a mesma família da liberação morta que a trava da manhã já cobrava.

### (4) TRÊS LIBERAÇÕES ESCRITAS, E DUAS DELAS SÃO RECUSAS

A trava **não julga prosa** (20.5): ela denuncia e exige liberação escrita com âncora literal. As três
ocorrências legítimas do ar foram liberadas com motivo:

- **`/sobre/` e `/divulgacao-de-afiliados/`**, as duas **recusas** que nomeiam *"selo de mais vendido"* para
  dizer que esta ilha **não o publica**. Reprovar essas linhas seria reprovar a **página certa** — o caminho
  mais curto para alguém passar a ignorar o portão —, e apagá-las para agradar a régua apagaria justamente a
  promessa que o `VOZ.md` manda existir.
- **a regra de ordem** da página de divulgação (*"quem a loja mostra como mais vendido na busca medida"*),
  que **tem fonte**: o `vendas_na_medicao` gravado em cada anúncio.
- na camada nova, **a média GEOMÉTRICA da F2** — ali `média` é **nome de uma operação**, declarada ao lado
  da conta que a usa, e não distribuição.

### O QUE A BANCADA MEDIU

- **Com rede, ANTES de construir (18.5): 29 portões, 0 falha.**
- **Sem rede, depois: 25 portões, 0 falha** — e a única reprovação de todo o caminho foi o **manifest
  desatualizado**, que é o portão fazendo o trabalho dele.
- **`mutacoes-produto.py`: 29 mutações, 29 reprovadas, 0 sobrevivente, 0 inerte** (eram 26).
- **`teste-relevancia-do-anuncio.py`: 71 casos, 0 falha** (eram 60).
- **`conferir-no-ar.py --autoteste`: 28 afirmações, 0 falha** (eram 20) — nelas as **três frases reais do
  ar**, a liberação que vale **só** para a própria âncora (âncora de outra frase não salva), a borda da
  palavra, e **a lista VELHA refeita ao lado da nova exigindo que as duas DISCORDEM** (20.8: autoteste em
  que as duas concordam não mede conserto nenhum).

Manifest **38 → 40**. Snippets: produto **1.5.0 → 1.6.0**, F2 **1.4.0 → 1.4.1**, espelhados pela ferramenta
que já espelha o `sha256` (20.7).

### NO AR, CONFERIDO PELA 18.4

**Revisão 40 às 13:39:44Z**, com `6 aplicado(s)` na linha de fecho contra **6 linhas de item dizendo `ok`**,
lidas **do fecho para baixo** (20.8) e conferidas contra o número que o próprio fecho declara (20.4).

**A REVISÃO 39 NÃO APARECE NO LOG E NÃO É JANELA ROLADA: ELA FOI ABSORVIDA.** Dois pushes dentro do **mesmo
turno de cron** (13h25Z e 13h37Z) entraram numa revisão só — é o mesmo que aconteceu de manhã com as
revisões 36 e 37, e os dois casos deixam o mesmo rastro significando o contrário: janela rolada deixa a
conta **aberta**, revisão absorvida a deixa **fechada**. Aqui ela fecha: 6 declarados, 6 lidos.

**AS TRÊS FRASES, MEDIDAS NO AR UMA POR UMA, com quebra de cache:** `reclamação mais comum` **ausente**,
`mais que a média` **ausente**, `lacuna mais comum` **ausente**. E no lugar da primeira, servida: *"Nenhum
dos 6 anúncios declara a tensão E a amperagem no mesmo título (1 declara só a tensão) — e a calculadora de
autonomia pede os dois."* No lugar da terceira: *"São 12 dos 17 registros deste banco."*

**PIXEL (32.5), medido no navegador a 390 px:** bicicleta **1.209 px**, patinete **1.281 px**, F2
**1.380 px** — **os três idênticos** aos de antes deste bloco, porque a contagem nova vive em
`qual_escolher`, **depois** do bloco de compra. **9 de 9 páginas no molde**, pior caixa **405 px** (teto
700), pior compra 1.380 px (teto 1.400).

**Bancada com rede DEPOIS do desembarque: 29 portões, 0 falha** — e as duas reprovações do caminho foram as
duas certas: o portão do site achando a quarta frase, e depois achando a âncora estreita.

### O PRÓXIMO PASSO DESBLOQUEADO

1. **A varredura da classe nas outras duas ilhas**, e agora ela tem **mecanismo pronto para copiar**: o
   despacho de 03/11 em `dados/despachos.md` pedia varredura por **quantificador**; hoje ela virou varredura
   **por site**, com a lista de superlativo e com a liberação lida de **todas** as camadas. A aquametria e a
   clubedomosaico também têm prosa em PHP, e a aquametria tem **mais** camadas de página que esta.
2. **A recoleta volta a vencer em 05/11**, pela data que as páginas afirmam, na mesma sequência de hoje.
3. **Não há bloco de página nova desbloqueado**, e **o egresso do `gov.br` e o da F3 não foram remedidos
   nesta passada** — dito assim para não parecer conferido.
4. **O que destrava mais por menos continua sendo o gesto do Raphael:** o despacho de 30/10, duas SERPs e um
   volume, numa sessão de Chrome de ~10 minutos. **Aberto há cinco dias**, e sem ele nenhuma página nova
   nasce aqui — a ilha tem 9 URLs contra as 40 do piso da 21.1.

## 2026-11-04 10h17Z–11hxxZ — **A FRASE FALSA NÃO MORREU ONTEM: ELA SÓ SAIU DA PÁGINA ONDE FOI ACHADA** — e o portão escrito para impedir o retorno dela vigiava as filhas, não a mãe

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10), e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas ANTES da reserva
e NENHUMA furou.** (a) Os **três despachos do molde** da seção 32 estão **FECHADOS**, lido no topo dos
três `PROMPT.md` (aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ). (b)
Nenhum despacho **ALTA** é de ilha **no ar E quebrada**: o único aberto fora do foco é a ronda
**NORMAL** da robometria de 02/11 (os minutos do ciclo da R2), e aquela ilha está no ar e sã; os ALTA
de `dados/despachos.md` são pedidos de **abertura de egresso** e o chamado da HostGator, que são do
Raphael. `executando_desde` estava `null`, que pela **1.1** já é prova de que não há bloco da Fundação
vivo — não houve reserva vencida para o git desempatar. Reserva às **10h17Z**, renovada às **10h24Z**.
Zero branch `claude/*` com commit fora do `main` (`git log origin/main..` vazio no
`claude/dreamy-mccarthy-0gm7zh`), zero PR aberto.

**O PUSH DA RENOVAÇÃO FOI RECUSADO PELO SERVIDOR, E O MEU TESTE DE SUCESSO MENTIU — lição de método
que vale para toda execução desta fábrica.** O `git push` voltou com `remote: fatal error in
commit_refs` e `! [remote rejected] main -> main (failure)`. A primeira retentativa usava
`grep -q "main -> main"` para decidir se tinha funcionado — e **essa string está dentro da linha de
ERRO**, então o laço imprimiu `PUSH-OK` sobre um push recusado. Quem pegou foi um `git fetch` logo
depois: o `origin/main` ainda era o commit anterior. **A régua certa não lê a mensagem, compara o
hash:** `git fetch` e `git rev-parse HEAD` contra `git rev-parse FETCH_HEAD`. É a mesma família do
`git log` raso da **1.1** e do número de tela digitado — o instrumento responde, e a resposta tem cara
de completa.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os dois
em **200 em TRÊS passadas**, com `aquametria.com.br` em **200 nas mesmas três**.

**A PRIMEIRA COISA FOI PROCURAR DEFEITO (18.5), e no chão não havia nenhum:** bancada **com rede, 29
portões, 0 falha**, antes de uma linha de código. O defeito estava onde portão nenhum olhava — outra vez.

### O BLOCO: a varredura que o despacho de ontem mandou fazer nas OUTRAS ilhas, feita nesta

O despacho NORMAL de 03/11 em `dados/despachos.md` manda quem reservar a **aquametria** ou a
**clubedomosaico** varrer a camada declarada por **quantificador por extenso**. Ele nasceu de um
defeito **desta** ilha e **ninguém fez a varredura aqui** — o conserto de ontem foi feito na frase que
foi achada. Fiz a varredura na ilha que reservei, e ela achou **três** afirmações, uma delas no ar e as
três sem um dígito.

### (1) A FRASE APOSENTADA ONTEM ESTAVA VIVA NA SEÇÃO MÃE, SERVIDA O DIA INTEIRO

A execução de 03/11 às 19h3xZ tirou de `/veiculos/patinete-eletrico/` a frase declarada:

> *"a carga máxima declarada é o primeiro filtro, e ela **quase nunca está no título**."*

Medido no ar hoje às 10h2xZ, **`/veiculos/` servia a mesma afirmação**, em `o_que_decide`:

> *"é o filtro que **quase ninguém olha** e que **quase nunca está no título**."*

**E a filha logo abaixo dela publica SEIS dos DEZESSEIS anúncios declarando a carga no título, de 60 a
150 kg** — o número que a mãe mandava procurar fora.

**É a 32.5-c um andar acima do CSS, e dita com todas as letras: o conserto foi feito na página onde o
defeito foi ACHADO, e a mãe é outra família.** Lá a regra de telefone não **alcançava** a segunda
família de cartão; aqui a **correção** não alcançou a segunda família de página.

**E O PORTÃO ESCRITO ONTEM PARA IMPEDIR EXATAMENTE ISSO NÃO A PEGOU.** O `REGISTRO.md` de 03/11
registra, como a melhor afirmação daquele bloco, *"a que nomeia a frase aposentada inteira: se `quase
nunca está no título` voltar à tela, o portão fica vermelho"*. Ela existe, está correta, e mora **dentro
do laço que varre as páginas de FILHA** — e a mãe não é uma delas. O cabeçalho do próprio
`conferir-produto-no-ar.py` **já dizia isso**, de um defeito idêntico de 02/11: a mãe *"não aparecia
aqui porque este portão descobre as páginas CASANDO o sitemap com os slugs da vitrine (...) e CAÍA FORA
de todo portão de ar desta ilha"*. **A trava nomeava a INSTÂNCIA; o que envelhece é a CLASSE.**

### (2) A PIOR DAS TRÊS: a página da bicicleta afirmava os DOIS lados do pivô da F1, com ZERO anúncio declarando um deles

`/veiculos/bicicleta-eletrica/` servia, na caixa de resposta:

> *"**Quase toda** a faixa de baixo é dobrável, de **pedal assistido**, pensada para o trajeto
> casa–trabalho; o topo da faixa é a que tem **acelerador** e motor forte — e é justamente ela que pode
> sair da categoria de bicicleta e entrar na de ciclomotor."*

**Medido nos seis anúncios que aquela página publica: ZERO declara acelerador e ZERO declara não ter
um.** A frase punha os seis em dois lados do **pivô da F1** — o que decide se a pessoa precisa de
habilitação — **separando-os por PREÇO**, que não é fonte de nada.

**E o esquema desta ilha proíbe isso no BANCO com estas palavras**, na decisão 3 do bloco 3
(`dados/especificacao-calculadoras.md`): *"o enum de `acelerador` é pivô da F1, então ele não aceita
nulo silencioso: ficha sem a informação grava `nao_declarado`, que é um terceiro valor com frase
própria, e **nunca** cai no lado 'só pedal assistido' por omissão."* **A camada declarada fazia em prosa
exatamente o que o esquema proíbe no registro, na metade que manda a pessoa para a rua sem CNH.** Não é
"número velho na prosa": é a prosa ocupando o lugar do campo que a ilha se recusa a preencher.

### (3) E uma afirmação de engenharia sem fonte em lugar nenhum da ilha

A mesma página: *"quadro dobrável é justamente onde o limite **costuma** ser mais baixo."* Nenhuma fonte
da ilha a sustenta, e naquela página **zero dos seis** anúncios declara carga. É a mesma régua que esta
ilha aplicou a si mesma quando **rebaixou a margem de 10% da F3** de "fonte estrangeira" para
`decisao_da_ilha`, por não achar o percentual publicado em treze publicadores. **A afirmação saiu**, e o
que ficou foi a instrução que se pode cumprir: abrir o anúncio e procurar na ficha.

### E A QUE FICA, nomeada e com a procedência ao lado

*"O número grande do anúncio **costuma** ser o pico do motor"* — na mãe e numa pergunta do patinete —
**fica**, e está escrita na lista de liberadas com o motivo. Ela afirma o **mercado** e não o banco
desta ilha, e é **mandada** pela seção 1.4(a) da especificação, com estas palavras: *"a F1 pergunta
potência nominal e diz, na mesma tela, que o número grande do anúncio costuma ser o pico e que o que a
regra lê está na ficha."* Tirá-la pioraria a página: ela é o aviso que impede alguém de classificar o
veículo pelo título, e a contagem que a acompanha já diz quantos anúncios dizem qual watt é aquele —
hoje **nenhum**.

### O QUE FOI AO AR — e o conserto é da CLASSE, não das três frases

- **A TRAVA DO QUANTIFICADOR, em `gerar-vitrine-de-produto.py --conferir`**, irmã da trava de dígito e
  escrita **porque a de dígito está CERTA e não bastava**. A de dígito reprova **qualquer** dígito na
  camada declarada, até um só — e as três frases passaram por ela sem esforço, porque **nenhuma tem um
  dígito**. Proporção por extenso é contagem com outro traje: afirma o estado do banco com a mesma
  validade de prazo que um número, e envelhece do mesmo jeito, calada.
  **ELA NÃO JULGA PROSA, DE PROPÓSITO (20.5):** régua que tentasse decidir se um "quase nunca" fala do
  mundo ou do catálogo reprovaria voz legítima, que é o caminho mais curto para alguém a ignorar. Ela
  **denuncia** a ocorrência e exige liberação escrita em `quantificadores_declarados_permitidos`, com
  **campo**, **motivo** e **âncora literal** — a forma de `numeros_declarados_permitidos`, que esta ilha
  já usa. **Três coisas REPROVAM:** liberação sem motivo ou sem campo; **âncora que não existe no texto
  declarado ou que não contém o próprio termo** (senão o portão de ar apagaria um pedaço qualquer da
  página e liberação de uma frase viraria anistia geral); e **liberação morta**, que é pior nesta lista
  que em outra, porque ela é a lista de quem **já foi olhado**.
- **A RÉGUA DO PIVÔ, em `teste-relevancia-do-anuncio.py`**, e ela é a leitura mais assimétrica desta
  ilha, cada lado pelo que ele afirma: a palavra `acelerador` no título **basta** para o lado `manual`
  (ninguém anuncia acelerador por engano); o lado do pedal exige **NEGAÇÃO explícita** — "sem
  acelerador", "somente pedal assistido" —, porque **ter pedal não exclui ter acelerador**. É a regra do
  esquema aplicada à camada do título: **nunca por omissão**. E `pedal tripulado`, que está em **dois
  títulos reais** desta coleta, **não declara nada**: é tradução de máquina de *pedal assisted*, e dar
  sentido a frase truncada é a família do `kg` solto de ontem — "quase certamente" não é procedência.
  **A ordem da leitura é cobrada por caso fabricado**, porque a negação **tem a palavra `acelerador`
  dentro dela** e ler na ordem inversa classificaria como `manual` o título que diz o contrário.
- **`frase_do_pivo`, `frase_do_dobravel` e a frase da carga AGREGADA da mãe**, as três contadas e com
  forma por mundo. A da mãe é `rdm_produto_frase_da_carga_agregada()`, **função PURA** sobre a relação já
  calculada, ao lado da irmã que já serve a caixa — e **agregada de propósito**: a mãe não tem anúncio
  próprio, o número dela é a soma das filhas no ar e a faixa é o menor e o maior entre todas, nunca a
  faixa de uma família servida como se fosse da seção.
- **`snippets/rodametria-produto.php` 1.4.0 → 1.5.0.** O `o_que_decide` da mãe era servido **cru** — e
  era por isso que a afirmação da carga estava escrita à mão ali: **não havia por onde um molde entrar**.
  Ele passa por um preenchedor, e o agregado é calculado **uma vez** para a caixa e para a frase, porque
  calculá-lo duas vezes abriria a porta para as duas metades divergirem, que é a 32.5-c outra vez.
- **O PORTÃO DE AR VARRE A CLASSE EM TODA PÁGINA DO MOTOR, MÃE INCLUÍDA, POR UMA FUNÇÃO SÓ.** A
  afirmação que nomeava a frase de ontem **saiu** e foi substituída pela varredura, chamada do laço das
  filhas **e** de `conferir_a_mae`. A lista de termos está **duplicada** entre o portão do repositório e
  o do ar **de propósito**: um julga o `main` e o outro julga o que o WordPress serve, e há um mundo
  entre os dois — prosa escrita direto no PHP, que a camada declarada não vê. Lista única num módulo
  compartilhado faria os dois medirem o mesmo arquivo e perderem exatamente o caso que o segundo existe
  para pegar.

### OS NÚMEROS, contados e não digitados

| página | anúncios | declaram o PIVÔ da F1 | dizem dobrável | declaram carga no título |
|---|---|---|---|---|
| `/veiculos/patinete-eletrico/` | 16 | **0** | 14 | 6 (60 a 150 kg) |
| `/veiculos/bicicleta-eletrica/` | 6 | **0** | 5 | 0 |
| `/veiculos/` (agregado) | 22 | **0** | — | 6 (60 a 150 kg) |

**E O ZERO É A TESE DA ILHA MEDIDA NA PRÓPRIA VITRINE.** O dossiê diz que a vaga da F1 não é "ninguém
fala disso", é *"todos falam, ninguém calcula"*. **Nenhum dos 22 anúncios que esta ilha publica diz se o
veículo anda sem você pedalar** — e sem isso nenhuma potência classifica, por decisão escrita do bloco
1. A página passou a dizer esse zero em vez de preencher o silêncio com prosa.

### O DEFEITO QUE O PORTÃO NOVO PEGOU ANTES DO AR, e ele é a mesma forma com o sinal invertido

A varredura do ar reprovou `/veiculos/patinete-eletrico/` por **não servir** a frase contada do pivô: o
molde entrou só na página da bicicleta, **onde o defeito foi achado**. É literalmente o defeito desta
manhã repetido por mim, meia hora depois de o descrever — e desta vez o portão o pegou **antes** do ar.
A frase entrou na dobra **"Qual escolher"**, que vive **depois** do bloco de compra, e não na caixa de
resposta: a 32.5-d manda medir no navegador quem mexer ali, e o `ESTADO.md` de ontem deixou a folga
escrita em px justamente para ela não ser estimada de cabeça.

### (4) E A TERCEIRA CÓPIA DA MESMA FRASE ESTAVA NUMA CAMADA DECLARADA DIFERENTE, COM PORTÃO PRÓPRIO E SEM NENHUMA RÉGUA DESTA CLASSE

Com a trava escrita, rodei a lista dela — a lista do **portão**, lida do código para não divergir —
sobre as outras camadas declaradas desta ilha. `dados/f2-respostas.json`: **zero**. E
`dados/paginas-institucionais.json`: **duas**, uma delas no ar em `/sobre/`:

> *"O anúncio não diz se aquele watt é o que vale para a regra de trânsito, não diz quantos km sobram
> quando quem pilota pesa noventa quilos, e **quase nunca diz quanto peso o quadro aguenta**."*

**É a MESMA afirmação, pela terceira vez, no terceiro lugar.** A primeira saiu da página do patinete em
03/11; a segunda, da seção mãe, hoje de manhã; esta vivia na camada institucional, que tem **gerador e
portão próprios** (`teste-institucional.py` e `conferir-institucional-no-ar.py`) e **não tinha régua
nenhuma desta classe** — só a de dígito, que a frase atravessa sem esforço.

**A frase saiu, e no lugar dela ficou o que é verificável:** o peso aparece no título quando aparece, e
a página de cada família conta, anúncio por anúncio, qual título declarou e qual se calou.

**A outra ocorrência FICA, liberada e nomeada:** *"Na prática não há um caso seu parado esperando"*, na
seção de direitos da página de privacidade. Ali "na prática" é **marcador de discurso**, e o que vem
depois dele é uma afirmação **absoluta** sobre esta ilha — nada é pedido, nada é gravado, nenhum cookie
é escrito —, e as três foram **medidas do lado de fora** em 30/10. Tirá-la não mudaria uma afirmação da
página.

**E A TRAVA ENTROU NAS DUAS CAMADAS, cada uma no portão dela, com a lista de termos DUPLICADA de
propósito.** Lista única num módulo compartilhado é a tentação óbvia e é o erro: os dois portões julgam
**arquivos diferentes**, e há um mundo entre eles — prosa escrita direto no PHP, que camada declarada
nenhuma vê. **Foi justamente a camada sem a trava que guardou a terceira cópia.**

### AS DUAS TRAVAS PROVAM QUE MORDEM, E O PRIMEIRO MUNDO DE CADA É A FRASE DE VERDADE

Trava que nunca falhou não é trava, e a `bancada.py` desta ilha cobra as duas metades do veredito. As
duas ganharam os mesmos quatro mundos, fabricados da camada declarada real mexendo uma coisa de cada
vez:

1. **o mundo sadio passa** — e ele só passa porque as frases saíram hoje; sem esta afirmação a prova
   mediria nada;
2. **a frase REAL plantada de volta é achada** — não um exemplo inventado: a que esteve no ar;
3. **outra forma de proporção é achada** (*"a maioria das famílias não declara a bateria"*), porque
   procurar só o "quase nunca" que alguém já imaginou é a **leitura pelo avesso** que a 20.8 nomeia;
4. **a liberação vale só no campo dela** — liberar um termo num parágrafo não libera o mesmo termo
   noutro, senão a lista de quem **já foi olhado** viraria anistia por palavra.

### (5) A QUINTA CÓPIA, E A TRAVA NOVA NÃO A VÊ — dizer isto importa mais que o conserto

Achada **medindo o custo de pixel do próprio conserto**. `/veiculos/bicicleta-eletrica/` servia, na dobra
"Qual escolher":

> *"a dobrável **de pedal assistido** da faixa de baixo é **o que o mercado vende mais**, e ela resolve."*

Duas afirmações que esta ilha não pode fazer, e **nenhuma das duas tem um quantificador por extenso** —
a trava escrita hoje passa por cima delas:

- **O pivô da F1 afirmado por omissão outra vez.** "De pedal assistido" sobre a faixa de baixo, com
  **zero dos seis** anúncios declarando. Mesma família do item 2 desta entrada, outra redação.
- **Uma afirmação de VENDA na tela**, enquanto o próprio arquivo gerado desta ilha declara
  `vendas_ordenam_e_nao_vao_para_a_tela`: *"a contagem de vendas NÃO é publicada: a seção 7 proíbe selo
  de mais vendido, e prova social não é o que esta página vende."* **Medida, a frase BATE com o dado** —
  os cinco mais baratos são dobráveis e três deles têm 18, 68 e 23 vendas; o de R$ 6.200 não dobra e tem
  zero. **E continua proibida: afirmação verdadeira que a regra da casa manda não publicar não deixa de
  ser defeito.**

**O QUE ISTO DIZ SOBRE A TRAVA, e é a parte honesta:** ela pega a classe da **PROPORÇÃO POR EXTENSO**,
que é a classe que custou cinco dias e quatro cópias. **Ela não pega toda prosa escrita à mão sobre o
catálogo**, e a quinta cópia é a prova disso, achada por olho e não por portão. O que de fato fecha a
família é o que o item 2 do despacho da raiz já dizia e esta passada aplicou cinco vezes: **a afirmação
sai da mão e vira molde preenchido por uma função que conta.** Régua é rede de segurança; o mecanismo é
a contagem.

### A FOLGA DE PIXEL: CINCO FRASES CONTADAS A MAIS, CUSTO ZERO (32.5-d, medido duas vezes)

Medido no navegador a **390 px reais**, na mesma passada, como a 32.5-d manda de quem mexe em página de
molde — e **duas vezes**, porque a primeira medição pegou um estado intermediário e teria ido para o
registro como número final:

| página | ontem | revisão 35 (meio do bloco) | **revisão 38 (final)** |
|---|---|---|---|
| `/veiculos/bicicleta-eletrica/` | 1.209 px | **1.345 px** (55 px do teto) | **1.209 px** |
| `/veiculos/patinete-eletrico/` | 1.281 px | 1.281 px | **1.281 px** |

**Os dois voltaram ao número de ontem, na casa do pixel**, e isso não foi sorte: a frase do pivô do
patinete entrou na dobra "Qual escolher", que vive **depois** do bloco de compra; e na bicicleta, as duas
frases contadas na caixa de resposta custaram 136 px que voltaram quando a terceira frase daquela caixa
saiu — ela **duplicava** o `qual_escolher[3]`, que diz a mesma coisa melhor e com procedência (*"nenhum
destes anúncios declara os três"*). **Cinco frases contadas a mais em três páginas, zero pixel acima do
bloco de compra.** A escolha do lugar foi feita lendo a folga que a execução de ontem deixou escrita em
px no `ESTADO.md`, em vez de estimá-la de cabeça — que é exatamente para isso que ela estava escrita.

**E A MEDIÇÃO DO MEIO VALE REGISTRO, porque ela era a que eu ia publicar:** às 11h0xZ o portão disse
1.345 px na bicicleta e eu escrevi "55 px de folga" no rascunho desta entrada. Aquele número estava
**certo sobre a revisão 35** e **errado sobre o bloco**, e só não foi para o `main` porque o `/status`
disse que o ar era 35 e não 38. **Número medido no meio de um bloco de três desembarques é número de
outro mundo** — a mesma família do `ultimo` anterior ao push, que esta ilha já tem escrita.

**OS 32.5-d DESTAS DUAS PÁGINAS JÁ ESTÃO GASTOS NA METADE DA FOTO:** medido hoje, **5 de 5** cartões do
carrossel das duas já servem foto de verdade, então a armadilha do "primeiro dado de uma espécie" não
está mais à frente nelas. O que ainda consome folga ali é frase — e a forma **mais longa** da frase do
pivô (a de zero declarando, que é a de hoje) **já é a que está medida**.

### A VERIFICAÇÃO NO AR (18.4)

- **Revisão 38** às **11:10:18Z**, com a linha de fecho declarando **`4 aplicado(s)`** e o grupo dela,
  lido **do fecho para baixo** (20.8), trazendo **exatamente 4 linhas de item, todas dizendo `ok`**.
- **AS REVISÕES 36 E 37 NÃO ESTÃO NO LOG, E ISSO NÃO É JANELA ROLADA — ELAS NUNCA RODARAM.** A 20.8
  manda dizer quando a janela rola e leva item embora; aqui a leitura é outra, e ela se prova pelas
  linhas de revisão do próprio log: **hoje houve DOIS disparos**, 10:40 (revisão 35) e 11:10 (revisão
  38), com `ultimo` indo de 10:40:17 a 11:10:18. **O cron aplica o manifest como ele está no instante em
  que dispara**, então três pushes dentro de um turno entram numa revisão só, e as de dentro não existem
  como passada. **Os dois casos deixam o mesmo rastro — "a revisão N não está no log" — e significam
  coisas opostas:** janela rolada é conta aberta, revisão absorvida é conta fechada. **Quem for ler este
  log conta as linhas de revisão antes de concluir**, e as quatro linhas da 38 cobrem todo arquivo que
  mudou nos três pushes (`paginas-institucionais` e `paginas-de-produto` entre elas).
- **O snippet CARREGADO pelo WordPress (20.7):** `/casca` → `versoes` diz `rodametria-produto: 1.5.0`,
  igual ao `manifest.json` — e os quatro snippets presentes, nenhum `id` ausente, que é o sinal de
  snippet gravado e não ativado.
- **AS CINCO FRASES MORTAS, AUSENTES NAS CINCO PÁGINAS que podiam servi-las**, conferidas uma por uma
  com quebra de cache; **as cinco frases CONTADAS, servidas**, cada uma na página dela; e a **liberada**
  (*"costuma ser o pico do motor"*) **servida** na mãe e no patinete, que é o que prova que a trava
  libera em vez de apagar.
- **Bancada com rede: 29 portões, 0 falha.** `conferir-no-ar.py`, `conferir-produto-no-ar.py`,
  `conferir-institucional-no-ar.py` e `conferir-32-5-no-navegador.mjs` aprovados.
- **E O PORTÃO NOVO REPROVOU O MUNDO REAL ANTES DO CONSERTO CHEGAR, que é a melhor prova que ele podia
  dar:** rodado às 11h0xZ contra o ar da revisão 35, `conferir-institucional-no-ar.py` fechou
  **REPROVADO com 1 falha**, nomeando `/sobre/` e a frase inteira. Não foi mundo fabricado: foi a página
  de verdade, com o defeito de verdade, no ar.

### UMA LIÇÃO DE MÉTODO QUE NÃO É DESTA ILHA E VALE PARA TODA EXECUÇÃO

**O `git push` foi RECUSADO pelo servidor e o meu teste de sucesso disse que tinha funcionado.** O push
voltou com `remote: fatal error in commit_refs` e `! [remote rejected] main -> main (failure)`, e a
retentativa decidia o veredito com `grep -q "main -> main"` — **string que está dentro da linha de
ERRO**. O laço imprimiu `PUSH-OK` sobre um push recusado, e quem pegou foi um `git fetch` logo depois.
**A régua certa não lê a mensagem, compara o hash:** `git rev-parse HEAD` contra
`git rev-parse FETCH_HEAD` depois de um `git fetch`. É a família do `git log` raso da **1.1** e do número
de tela digitado: o instrumento responde, e a resposta tem cara de completa.

**E a segunda, no mesmo dia:** o `git commit -m "..."` com acento grave dentro das aspas duplas **executa
o que está entre os acentos**. O nome de campo `vendas_ordenam_e_nao_vao_para_a_tela`, citado numa das
mensagens desta execução, virou comando (`command not found`) e **saiu da mensagem**, que foi para o
`main` com um buraco no lugar dele. Não foi corrigida por `--amend`: a mensagem já estava empurrada, e
force push é proibido. **Quem citar nome de campo ou de arquivo em mensagem de commit escreve a mensagem
por arquivo (`-F`) ou sem acento grave.**

### O PRÓXIMO PASSO DESBLOQUEADO

1. **NÃO HÁ BLOCO DE PÁGINA NOVA DESBLOQUEADO**, e as duas execuções anteriores já o disseram com o
   banco na mão. **Não remedi a F1 e a F3 hoje** e digo isso em vez de deixar parecer conferido: a
   remedição registro por registro é de 03/11 às 19h3xZ, e nada entrou no banco desde então — o bloco de
   hoje não tocou em `dados/veiculos.json`. A F1 segue atrás do `gov.br` (despacho ALTA) e a F3 atrás de
   `carga_max_kg` em registro com oferta aberta.
2. **O TRABALHO RECORRENTE É A RECOLETA**, e ela está **vencendo**: a faixa de preço no ar é de
   **03/11** e as duas páginas dizem "à venda hoje" com a data da leitura ao lado. Quem a fizer roda
   `coletar-por-consulta.py --gravar` **e depois** `coletar-piso-da-vitrine.py --gravar` (a ordem
   importa), mais `coletar-oferta.py --gravar`, e só então gera. **E ela agora carrega TRÊS contagens
   sem uma linha nova:** carga, pivô e dobrável são lidos do título a cada geração, nunca herdados de
   campo gravado — anúncio novo entra já medido.
3. **O QUE DESTRAVA MAIS POR MENOS CONTINUA SENDO O MESMO GESTO, e é do Raphael:** o despacho de 30/10
   — duas SERPs e um volume, UMA sessão de Chrome de ~10 minutos. **Aberto há cinco dias.** Sem ele
   nenhuma página nova nasce aqui, e a ilha tem 9 URLs contra as 40 do piso da 21.1.
4. **A TRAVA NOVA NÃO FECHA A FAMÍLIA INTEIRA, e a quinta cópia é a prova.** Quem abrir bloco de
   conteúdo nesta ilha lê a camada declarada procurando **afirmação sobre o catálogo sem quantificador**
   — venda, "o mercado", "o mais comum" —, porque essas a régua não vê. O que fecha é o mecanismo:
   contagem no lugar da prosa.
5. **FORA DESTA ILHA, e só para quem a reservar:** o despacho de 03/11 em `dados/despachos.md` sobre
   quantificador por extenso **foi atualizado hoje** com a medição desta ilha e com o mecanismo pronto
   para copiar — ele segue **aberto** para a aquametria e a clubedomosaico. E seguem abertos ali o da
   borda `\b`, o do `clearstatcache` da 29.3 e os dois ALTA de egresso desta ilha.

---

## 2026-11-03 19h17Z–19h5xZ — **A CARGA MÁXIMA QUE O TÍTULO DECLARA VIRA NÚMERO PRÓPRIO DAS DUAS PÁGINAS DE PRODUTO**, e ela nasceu de uma frase que a própria página servia e que a medição reprovou

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto desde 27/10), e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas e NENHUMA
furou.** (a) Os **três despachos do molde** da seção 32 estão **FECHADOS**, lido no topo dos três
`PROMPT.md`. (b) Nenhum despacho **ALTA** é de ilha **no ar E quebrada**: o da robometria de 30/10
fechou em 02/11, e o que ela tem aberto é ronda **NORMAL** de 02/11, que espera pela **18.1**.
`executando_desde` estava `null`, que pela **1.1** já é prova de que não há bloco da Fundação vivo —
não houve reserva vencida para o git desempatar. Reserva às **19h17Z**, push aceito **de primeira**,
campo **renovado às 19h26Z**. Zero branch `claude/*` com commit fora do `main`, zero PR aberto: o
`claude/dreamy-mccarthy-ljpns1` existe e está **idêntico ao `main`**, conferido com
`git log origin/main..`, que voltou vazio.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os
dois em **200 em TRÊS passadas**, com `aquametria.com.br` em **200 nas mesmas três**.

**A PRIMEIRA COISA FOI PROCURAR DEFEITO (18.5), e no chão não havia nenhum:** bancada **com rede, 29
portões, 0 falha**, antes de uma linha de código. O defeito estava onde portão nenhum olhava.

### O BLOCO NÃO ESTAVA PRÉ-REGISTRADO, E AS DUAS EXECUÇÕES ANTERIORES ESTAVAM CERTAS: não há bloco de PÁGINA NOVA desbloqueado. Eu remedi os dois candidatos em vez de herdar o veredito

**A F1 e a F3 foram remedidas no banco, registro por registro, e as duas seguem travadas:**
`carga_max_kg` — a entrada da **F3** — está declarado em **três** registros (`maxshot-v1`,
`maxshot-v1spro`, `playbik`) e os **três são `rascunho`**: a escada de compra inteira devolveu **zero
oferta** na loja nos três, e o motivo está escrito em `afiliado.motivo_sem_url_busca` com os degraus
medidos um por um. Sem piso não há publicável (25.2), e uma ferramenta que responde "aguenta o seu
peso" sem ter o que comparar nem o que vender não é ferramenta. A **F1** segue atrás do `gov.br`
(despacho ALTA). **Página nova de malha segue travada pela 30.8**, e isso não se afirma daqui.

### O DEFEITO, E ELE ESTAVA NA TELA DESDE 29/10 — UMA FRASE ESCRITA À MÃO AFIRMANDO O ESTADO DO CATÁLOGO

`/veiculos/patinete-eletrico/` servia, na dobra "Qual escolher", a frase **declarada**:

> *"a carga máxima declarada é o primeiro filtro, e ela **quase nunca está no título**."*

**Medido no mesmo instante, nos anúncios que aquela página publica: SEIS DOS DEZESSEIS declaram a
carga máxima no título, e ela vai de 60 a 150 kg.** A frase não era só imprecisa — ela mandava o
leitor procurar fora o número que a própria página já tinha na mão.

**É a cicatriz que esta ilha já nomeou, em 29/10 às 16h2xZ, com estas palavras: "prosa que afirma o
estado do banco é número digitado em outro traje".** Aquele dia consertou o bloco de compra da F2 que
dizia três vezes a mesma coisa; a lição não viajou para a camada declarada das páginas de produto,
escrita no mesmo mutirão. **É a 32.5-c outra vez, num andar acima do CSS:** a metade que aprendeu não
contou à irmã.

**E nenhum portão podia pegá-la,** e isso é o achado de método: a trava de dígito de
`gerar-vitrine-de-produto.py` reprova **número digitado** na camada declarada, e aquela frase não
tinha um dígito. Ela afirmava uma **proporção** por extenso. **Prosa sem dígito que afirma contagem
passa por todas as réguas desta ilha** — e a saída não foi uma régua nova de prosa: foi **tirar a
afirmação da mão e pôr a contagem no lugar dela**.

### O QUE FOI AO AR, revisão **34** às 19:40:19Z

- **`ferramentas/teste-relevancia-do-anuncio.py`** — `carga_declarada(titulo)` e `faixa_de_carga()`,
  ao lado do `rotulo_de_potencia` que já media o watt dos títulos. Ela **não atribui `carga_max_kg` a
  ninguém**: título é nível 6 e o `niveis_minimos_por_campo` exige melhor. O que sai é **contagem e
  faixa**.
- **A LIGAÇÃO É OBRIGATÓRIA, E ELA É A REGRA INTEIRA.** `kg` solto é **ambíguo** entre a carga que o
  veículo aguenta e o peso do **próprio veículo**, e as duas aparecem em título de patinete
  (`dobrável 12kg` e `até 120kg`). Lê-lo como carga publicaria o peso do aparelho como limite de quem
  sobe nele, numa página que diz *"passar da carga máxima deixa a solda do guidão mais perto de
  ceder"*. **O caso real que a regra deixa de fora de propósito estava na coleta de hoje:**
  `patinete eletrico 350w 10ah 120kg autonomia 30km` — quase certamente carga, e "quase certamente"
  não é procedência. Ele entra como **não declarado** e continua nomeado na tabela.
- **AS BORDAS SÃO ASSIMÉTRICAS, cada uma pelo que protege** — a lição de hoje de manhã, nesta mesma
  régua, onde `\b` depois de LETRA deixou passar `Capacete1`. Esquerda, na palavra que liga: `\b`
  estrita (`ate` não pode casar dentro de `Matelado`). Direita, depois de `kg`: **`(?![a-z])` e não
  `(?![a-z0-9])`** — barra `90kgf` (kgf é força) e **deixa passar `150kg1`**, a enumeração do
  vendedor. **A primeira versão escreveu `(?![a-z0-9])` e o caso do `150kg1` a REPROVOU na primeira
  passada**: o mesmo buraco do capacete, do outro lado, pego pelo autoteste antes do ar. A diferença
  com `aro 20`/`aro 200` é que lá o dígito vem **dentro** da medida e a muda; aqui ele vem **depois da
  unidade** e não pode mudar nada.
- **`ferramentas/gerar-vitrine-de-produto.py`** — `frase_da_carga()` em **quatro formas**, porque a
  forma muda com o mundo e não só o número: zero declarando, **um** só (verbo no singular), **todos no
  mesmo valor** (não pode sair "de 60 a 60 kg") e faixa de verdade. **Cinco mundos fabricados** no
  `--conferir`, dos quais o banco de hoje produz **dois**. Cada linha da tabela ganhou a célula e o
  **pedaço do título** que sustenta o número, como procedência (seção 24) — nunca uma frase nossa.
- **`dados/paginas-de-produto.json`** — a frase falsa **saiu**; `{FRASE_DA_CARGA}` entrou nas duas
  páginas, na caixa de resposta, na dobra "Qual escolher" e numa **pergunta nova em cada**. Zero
  dígito na camada declarada, conferido pela trava que já existia.
- **`snippets/rodametria-produto.php` 1.3.0 → 1.4.0** — a coluna **"Carga máxima no título"** na
  tabela visível, que é o que a 32.1 chama de *"o que as IAs citam"*. Ela fica **na tabela e não na
  primeira tela** por razão de pixel: a tabela vive **depois** do bloco de compra, então coluna aqui
  custa **zero pixel** acima dele.
- **`ferramentas/conferir-produto-no-ar.py`** — quatro afirmações novas, e a melhor delas é a que
  nomeia a **frase aposentada inteira**: se `quase nunca está no título` voltar à tela, o portão fica
  vermelho. Nomeada inteira de propósito — procurar só `carga máxima` acusaria a coluna **certa**, e
  portão que reprova página certa é o caminho mais curto para alguém o ignorar (20.5).

### OS NÚMEROS, contados e não digitados

| página | anúncios publicados | declaram carga no título | faixa |
|---|---|---|---|
| `/veiculos/patinete-eletrico/` | 16 | **6** | **60 a 150 kg** |
| `/veiculos/bicicleta-eletrica/` | 6 | **0** | — |

**E O NÚMERO QUE VALE A PÁGINA INTEIRA: um dos seis é vendido como ADULTO declarando `Até 60kg`.**
`Patinete Elétrico Scooter **Adulto** 150w Dobrável **Até 60kg**`, na mesma vitrine de outro que
declara **150 kg**. O piso da faixa é mais leve que a maior parte dos adultos do país, e está escrito
no título, onde ninguém compara. É exatamente o buraco que o dossiê diz que esta ilha existe para
ocupar — *"acertar os três números antes de comprar"* —, e é o **terceiro** número, o que não tinha
resposta nenhuma no site porque a F3 não pode nascer.

**E A AUSÊNCIA NA BICICLETA É DADO, não lacuna:** nenhum dos seis títulos tem **um** kg. A página diz
isso com a mesma frase contada, e manda procurar na ficha em vez de supor.

### VERIFICAÇÃO NO AR (18.4)

- **Revisão 34** às 19:40:19Z. A linha de fecho declara **`5 aplicado(s)`** e o grupo dela, lido **do
  fecho para baixo** (20.8), traz **exatamente 5 linhas de item, todas dizendo `ok`** (20.4).
- **O cron é turno e não relógio (20.6), e a régua do `ultimo` acertou outra vez:** às 19h36Z o
  `/status` trazia revisão **33** com `ultimo` em **19:16:15** — recente e **anterior ao push**, que
  pela régua do `ultimo` desta ilha não é defeito nem cache, é **turno**. Seis visitas à home, uma por
  minuto, e a revisão entrou às **19h41Z** com o cron disparando às 19:40:19. **Esperar sem visitar
  não é paciência.**
- **Bancada com rede: 29 portões, 0 falha.** `conferir-no-ar.py`, `conferir-produto-no-ar.py` e
  `conferir-institucional-no-ar.py` aprovados.
- **32.5 medida no navegador a 390 px, 9 de 9 páginas do molde dentro dela**, 0 fora do molde, pior
  caixa 405 px (teto 700) e pior compra 1.380 px (teto 1.400).

**E A MEDIÇÃO MOSTRA O CUSTO DA ESCOLHA, escrito aqui porque ele é a próxima armadilha desta ilha: o
primeiro botão de compra DESCEU nas duas páginas** — patinete de **1.084 → 1.281 px** e bicicleta de
**1.129 → 1.209 px** —, porque a frase contada entrou **na caixa de resposta**, que é a primeira tela.
As duas passam, e o patinete passa com **119 px de folga**. **Isso é a 32.5-d esperando acontecer:**
a próxima frase que alguém puser na caixa daquela página, ou a primeira foto num cartão, estoura o
teto. Quem mexer ali mede no navegador **na mesma passada**, e a folga está escrita aqui em px para
não ser estimada de cabeça.

### O PRÓXIMO PASSO DESBLOQUEADO

1. **NÃO HÁ BLOCO DE PÁGINA NOVA DESBLOQUEADO, e isto foi RECONFERIDO hoje no banco** (F3) e não
   herdado. O trabalho recorrente desta ilha é a **recoleta** — faixa de preço e série de cotações
   vencem sozinhas. A de hoje saiu às 16h2xZ, então ela **não está vencida**; a próxima passada que a
   fizer roda `coletar-por-consulta.py --gravar` **e depois** `coletar-piso-da-vitrine.py --gravar` (a
   ordem importa), mais `coletar-oferta.py --gravar`, e só então gera. **E a recoleta agora carrega a
   carga declarada sem uma linha nova:** a célula e a faixa são **lidas do título** a cada geração, em
   vez de herdadas de campo gravado — anúncio novo entra já medido.
2. **O QUE DESTRAVA MAIS POR MENOS CONTINUA SENDO O MESMO GESTO, e é do Raphael:** o despacho de
   30/10 — duas SERPs e um volume, UMA sessão de Chrome de ~10 minutos. **Aberto há quatro dias.**
   Sem ele nenhuma página nova nasce aqui, e a ilha tem 9 URLs contra as 40 do piso da 21.1.
3. **E UM ACHADO QUE É DAS OUTRAS ILHAS, escrito em `dados/despachos.md` e não aqui:** a trava de
   dígito desta ilha não alcança **proporção por extenso**. A aquametria e a clubedomosaico têm a
   mesma trava de dígito na camada declarada delas, e a pergunta — não a afirmação, porque não
   reservei nenhuma das duas (seção 3) — é se a prosa delas também afirma o estado do banco sem um
   dígito. Despacho **NORMAL** novo de 03/11.

---

## 2026-11-03 16h18Z–16h5xZ — **A FAIXA DE PREÇO REMEDIDA HOJE**, e a coleta achou a régua deixando passar **um capacete como bicicleta** — R$ 113,34 seria o piso do número próprio da ilha

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** — foco total e absoluto desde 27/10 — e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas e NENHUMA
furou.** (a) Os **três despachos do molde** da seção 32 estão **FECHADOS**, lido no topo dos três
`PROMPT.md` (aquametria 21/10 18h2xZ, clubedomosaico 23/10 19h4xZ, robometria 21/10 16h1xZ). (b)
Nenhum despacho **ALTA** é de **ilha no ar E quebrada**: o da robometria de 30/10 está FECHADO desde
02/11 10h3xZ e conferido no ar, e os ALTA de `dados/despachos.md` são pedidos de **abertura de
egresso** e o **chamado da HostGator**, que são do Raphael. `executando_desde` estava `null`, que
pela **1.1** já significa que não há bloco da Fundação vivo. Reserva às **16h18Z**, push aceito **de
primeira**, campo **renovado às 16h34Z**. Zero branch `claude/*` com commit fora do `main`; zero PR
aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os
dois em **200 em TRÊS passadas**, com `aquametria.com.br` em **200 nas mesmas três**.

**A PRIMEIRA COISA FOI PROCURAR DEFEITO (18.5), E NÃO ACHEI NO AR:** bancada **com rede, 29 portões,
0 falha**, antes de uma linha de código.

### O BLOCO: o número PRÓPRIO desta ilha dizia "hoje" e era de cinco dias atrás

A execução anterior fechou dizendo que *"não há mais bloco de código desbloqueado nesta ilha
pré-registrado"* e pedindo que a seguinte **dissesse isso em vez de inventar**. Antes de dizer, os
três bloqueios foram remedidos (abaixo) — e no caminho apareceu o que não era bloqueio nenhum: a
**faixa de preço**, que é o `numero_proprio_pedido` das duas páginas de produto, estava medida em
**29/10** e as duas páginas serviam a frase **"Preço mediano hoje"** na primeira tela, com *"os 16
anúncios que a gente conferiu em 29/10/2026"* no corpo. **É a seção 4 aplicada ao próprio produto da
ilha:** o site não ficou para trás em silêncio, ficou para trás dizendo "hoje".

Isso **não é bloco inventado**: o esquema desta ilha nasceu com `cotacoes[]` como **série** (achado 3
do bloco 3, 28/10: *"leitura nova não substitui leitura velha, porque substituir apaga a série"*), e
recolher é o trabalho recorrente que o desenho prevê. Nada de portão novo (31.2 e 31.3 respeitadas):
as ferramentas que rodaram já existiam, com os modos `--gravar` que elas nasceram tendo.

**O QUE MUDOU, medido e não estimado:**

| página | faixa em 29/10 | faixa em 03/11 |
|---|---|---|
| `/veiculos/patinete-eletrico/` | R$ 1.297,13 a R$ 3.399,00 · mediana **1.590,53** · 16 anúncios | R$ 1.030,00 a R$ 2.699,00 · mediana **1.647,95** · 16 anúncios |
| `/veiculos/bicicleta-eletrica/` | R$ 2.299,99 a R$ 6.199,90 · mediana **2.399,99** · 5 anúncios | R$ 2.299,99 a R$ 6.199,90 · mediana **2.299,99** · 6 anúncios |

E a **série de cotações** do `honeywhale-m2-max` (o único registro casado) cresceu em vez de ser
substituída: **03/11 R$ 2.299,00 com 5 vendas**, ao lado de 29/10 (3 vendas) e 27/10. O preço não
mexeu; **as vendas sim**, e é dado que só existe porque a leitura velha ficou.

### O ACHADO, E ELE É UM TÍTULO REAL COM DOIS BURACOS SOMADOS

A coleta nova devolveu, na consulta `bicicleta eletrica adulto`, com `serve: True` e **R$ 113,34**:

```
1 Peca Certificado 3C Masculino E Feminino Adulto Desenho Animado
Bicicleta Eletrica Motocicleta Meio Capacete1
```

**R$ 113,34 seria o PISO da faixa da página da bicicleta** — um **capacete publicado como
bicicleta**, na primeira tela, sob a frase "Preço mediano hoje", com botão de afiliado ao lado. A
régua recusou **dez** capacetes naquela mesma passada e deixou passar **o décimo primeiro**.

**(1) A BORDA DA DIREITA.** A recusa `capacete` não casou porque o vendedor escreveu **`Capacete1`**,
com o dígito **colado**: `\b` é borda entre caractere de palavra e não-palavra, e `1` **é** caractere
de palavra — então não há borda. É a família do `git log` raso da **1.1** e do número de tela
digitado: **o instrumento responde, e a resposta sai curta com cara de completa.**

E a correção **não podia ser casar por pedaço de palavra**, porque a própria régua tem bordas por
uma medição de 29/10 (`Patinete Eletrico ... 36V` recusado por `6v`). Então **as duas bordas
deixaram de ser a mesma coisa, cada uma pelo que PROTEGE**: a da **esquerda** segue `\b` estrita, que
é quem impede `6v` de casar `36V` — o dígito **antes** do termo é justamente o caso medido; a da
**direita**, para termo que termina em **letra**, passa a ser `(?![a-z])`, porque dígito colado não
faz outra palavra (`capacete1` é `capacete` com a enumeração do vendedor) e **letra colada faz** — e
é por isso que `moto` continua não casando `motocicleta`; para termo que termina em **dígito** segue
`\b`, porque `aro 20` não pode casar `aro 200`, onde o dígito seguinte **muda a medida**.

**(2) A REGRA DE POSIÇÃO, e ela é um buraco independente.** Consertada a borda, **o título ainda
passava**: `capacete1` está no **fim**, depois de `bicicleta`, e `POR_POSICAO` lê isso como *"é peça
DO veículo"* e pula a recusa. A regra está **certa** para o título que ela nasceu medindo — o veículo
que nomeia as peças dele, `Patinete Eletrico 800W ... Pneu 10" Off-Road` — e **cega para a forma
inversa**, que é a forma **mais comum** de título de acessório: listar primeiro os veículos
**compatíveis** e nomear o produto **por último**. Fecha `1 peca`, que está na **posição 0** e por
isso fura as duas, sobre uma afirmação do nicho fácil de conferir: **ninguem vende bicicleta,
patinete ou moto elétrica como "1 Peça"**. É a irmã singular de `kit_multiplo`, e mora em `acessorio`
porque o que ela decide não é quantidade: é **o que o anúncio é**.

**AS DUAS MORDEM, CADA UMA PELA AFIRMAÇÃO DECLARADA** — e a bateria precisou de um mundo
**fabricado** para que a primeira pudesse falhar sozinha, porque o título real é recusado por
`1 peca` e **não exerce a borda**: com a borda quebrada ele continuaria barrado, e a correção
passaria por conferida sem nunca ter sido medida (seção 8). Revertida a borda → reprova **1** (o
fabricado `Capacete1 Meio Casco Adulto para Bicicleta Elétrica`); revertido o `1 peca` → reprova **1**
(o título real); revertidas as duas → reprova **2**. Mais o avesso, que tem de **passar**:
`Bicicleta Elétrica Dobrável Adulto Capaceteria` — letra colada não é capacete. **28 casos, 0 falha.**

### E O PORTÃO QUE ACUSOU ESCONDIA O CAMPO QUE DIVERGIA

`coletar-por-consulta.py --conferir` reprovou — certo — e a linha saiu assim:

```
FALHA: bicicleta-eletrica / 25896948111: veredito gravado (False/acessorio)
       discorda do calculado (False/acessorio)
```

**Os dois lados impressos idênticos.** A comparação lê **três** campos (`serve`, `recusado_por` e
`exigencia_que_faltou`) e a mensagem imprimia **dois**; o que divergia naquele anúncio era a
**palavra** que recusa (`capacete` → `1 peca`, porque a ordem da lista mudou), e ela não aparecia.
Passou a imprimir os três. **Portão que não imprime o campo que ele compara faz quem o lê duvidar do
portão em vez do dado**, que é o perigo que a **20.5** nomeia.

### E OS PORTÕES PEGARAM UMA FALTA MINHA ANTES DO AR

A recoleta **substituiu** `anuncios-por-consulta.json` e com isso derrubou o `piso_da_busca` da
**25.2**. `validar-banco.py` (**22 falhas**) e `coletar-piso-da-vitrine.py --conferir` (**2**)
acusaram, com a frase certa: *"serve link de ficha e não tem piso de compra; ficha apodrece, e quando
esta morrer o cartão fica sem saída de compra"*. **Piso recolhido** nas duas consultas, e aí sim
verde. É a 25.2 funcionando sobre um erro de **ordem de passos**, não de régua.

### NO AR, CONFERIDO PELA 18.4

Revisão **33**, aplicada às **16:39:42Z**. `conferir-no-ar.py`: **APROVADO**.
Bancada **com rede: 29 portões, 0 falha** (inclusive o portão de pixel da 32.5 e o
`conferir-produto-no-ar.py`).

**20.4 e 20.8:** a linha de fecho da revisão 33 declara **`4 aplicado(s)`** e o grupo dela traz
**exatamente 4 linhas de item**, lidas **uma por uma**, **todas dizendo `ok`**
(`dados/paginas-institucionais`, `dados/vitrine-de-produto`, `dados/paginas-de-produto`,
`dados/f2-respostas`). Conta fechada, janela não rolou, nenhuma linha de item ficou fora.

**E O NÚMERO MUDOU NO AR, medido com quebra de cache nas três páginas:**

| página | o que serve agora | `29/10/2026` na página | `03/11/2026` |
|---|---|---|---|
| `/veiculos/patinete-eletrico/` | *"Preço mediano hoje R$ 1.647,95 ... sobre os 16 anúncios que a gente conferiu em 03/11/2026"* | **0** | 10 |
| `/veiculos/bicicleta-eletrica/` | *"R$ 2.299,99 ... sobre os 6 anúncios que a gente conferiu em 03/11/2026"* | **0** | 10 |
| `/autonomia-patinete-eletrico/` | cartão com preço de **03/11/2026** | **0** | 2 |

**E o capacete não está lá:** `113,34` **ausente** da página da bicicleta. A frase *"Preço mediano
hoje"* voltou a ser verdadeira nas duas páginas.

**O CRON:** o turno das 16:18:44Z caiu **antes** do push das 16h35Z, então pela 20.6 a espera era do
turno seguinte — que entrou às **16:39:42Z**, com as visitas de pé. Quatro minutos, não dezenove: a
diferença com 13h4xZ é que ali o push caiu **quatro minutos depois** de um turno e aqui caiu perto do
fim da janela.

### OS TRÊS BLOQUEIOS, REMEDIDOS E NÃO HERDADOS — e o quarto, que é de PRODUTO

| o que travava | medido em 03/11 16h2xZ | resultado |
|---|---|---|
| **F1** — texto oficial da Resolução Contran | `www.gov.br`, `in.gov.br`, `www.planalto.gov.br`, `www.contran.gov.br`, 2 passadas cada | **000 nas 8** |
| **F3** — `carga_max_kg`, campo de nível 5 | `www.casasbahia.com.br`, `www.extra.com.br`, `www.magazineluiza.com.br`, 2 passadas cada | **000 nas 6** |
| **malha nova** — a sessão de Chrome do despacho de 30/10 | `dados/consultas-de-produto.json`, linha por linha | as duas seguem **`nao-medida`**, sem `visto_por` nem `visto_em` |

**14 medições de bloqueio contra 2 de controle verde** (`rodametria.com.br` em 200 nas mesmas
passadas), zero intermitência.

**E O BLOQUEIO POR PRODUTO DE `moto eletrica` E `scooter eletrica` FOI REMEDIDO NA OPEN API, cinco
dias depois, E REPRODUZIU EXATO** — as duas maiores cabeças sem página do nicho, **823 mil** e **301
mil** buscas/mês:

- `moto eletrica adulto`: **3 de 20 servem** — o piso da 30.2 **raspando** —, os **três com ZERO
  vendas**, a R$ 8.500, R$ 13.999 e R$ 15.000. **Os mesmos três produtos de 29/10**, com a mesma
  variação de R$ 6.500 para a mesma classe. *"Página que nasce no piso com os três sem uma venda sai
  do ar na primeira coleta que perder um"* segue verdadeiro, e agora com duas medições.
- `scooter eletrica adulto`: **6 de 20 servem e cinco são PATINETE** (o sexto é bicicleta).
  **Nesta loja a palavra `scooter` É o patinete** — publicar a consulta serviria, sob um H1 que
  promete scooter, o produto que a página do patinete já serve: canibalização da 30.4 construída de
  propósito.

**O veredito dos dois não mudou, e agora ele é uma série de duas medições em vez de uma leitura
herdada.** O caminho delas continua sendo o Mercado Livre, onde a geração de link exige clique humano
(25.6) — **despacho, nunca bloco**.

## 2026-11-03 13h21Z–13h4xZ — **A PURGA DE CACHE DO HOSPEDEIRO, com os dois portões ao lado** — e o "pronto quando" do despacho **não era conferível desta nuvem**, o que é o achado de método da passada

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** — foco total e absoluto desde 27/10 — e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas e NENHUMA
furou.** (a) Os **três despachos do molde** da seção 32 estão **FECHADOS**, lido no topo dos três
`PROMPT.md` (aquametria 21/10 18h2xZ, clubedomosaico 19h1xZ, robometria 16h1xZ) — com os três
fechados, a exceção do molde que a 1.2 abre **deixou de existir**. (b) Nenhum despacho **ALTA** é de
**ilha no ar E quebrada**: o da robometria de 02/11 15h1xZ é de **julgamento (19.2)** e a ilha está no
ar; os ALTA de `dados/despachos.md` são pedidos de **abertura de egresso**, que são do Raphael.
`executando_desde` estava `null`, que pela **1.1** já significa que não há bloco da Fundação vivo — e
o último commit na pasta da ilha era de **10h46Z**, 2h35 antes. Reserva às **13h21Z**, push aceito
**de primeira**, campo **renovado às 13h37Z**. Zero branch `claude/*` com commit fora do `main`; zero
PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os
dois em **200 em TRÊS passadas**, com `aquametria.com.br` em **200 nas mesmas três**.

**O BLOCO ESTAVA PRÉ-REGISTRADO, e não foi escolhido hoje.** O `ESTADO.md` da execução anterior
fechou nomeando o próximo passo: *"(1) A PURGA DE CACHE DESTA ILHA, que é o único bloco de código
desbloqueado que sobrou e está pré-registrado como despacho de hoje"*. É o despacho NORMAL de 03/11 em
`dados/despachos.md`, escrito pela execução da manhã sobre a própria ilha que ela tinha reservado — e
**não consertado de propósito** naquele bloco, o que é a parte que vale ser lida: *"purga que apaga
arquivo em disco sem o portão da aquametria ao lado é como a armadilha do `realpath('')` entrou no
Arquipélago"*. **Ela tinha razão, e a prova é que o portão que veio junto se pagou outra vez** — ver
abaixo.

### O QUE FOI AO AR: a seção 13 da casca, e a divergência (a) da seção 12 fechada

A ilha viveu **sete dias no ar sem purga de cache**, e a falta era **dita em vez de escondida**: a
seção 12 da casca registrava a divergência (a) com todas as letras e o retrato da rota da 29.3 já
saía com `tem_purga_de_cache: false`. Agora a função existe, e a alínea (a) foi **reescrita**, não
apagada — o texto velho fica ao lado, com a janela em que foi verdade (03/11 das 10h4xZ às 13hxxZ).

**ONDE ISSO CUSTA, e é medido nas irmãs e não suposto aqui:** o reparo da 29.3 chama a purga
**depois** do `flush_rewrite_rules( true )`, porque o defeito que trouxe a função foi lido, por dias,
através de página servida de cache. Sem ela, a primeira medição depois do reparo mede a cópia velha e
diz que **não funcionou** — reprovação falsa, que a **20.5** chama de *"o caminho mais curto para
alguém passar a ignorar um portão"*. E no uso real é pior: quem lê isso numa ilha caída conclui, pela
própria **29.4**, que o `AllowOverride` está desligado e **abre chamado na HostGator por um defeito
que o reparo já desfez**.

### OS DOIS PORTÕES VIERAM JUNTO, PORQUE ERA A CONDIÇÃO ESCRITA NO DESPACHO

- **`ferramentas/teste-purga-cache.php` — 21 afirmações, 0 falha.** Ele constrói as armadilhas **em
  disco de verdade**, numa pasta temporária, e cada uma tem uma **TESTEMUNHA do lado de fora**: um
  arquivo que não pode desaparecer. *Afirmação sobre o que foi apagado é metade da prova; a que
  importa é a afirmação sobre o que CONTINUA LÁ.* Os seis casos: o caminho feliz (sem ele as outras
  seriam satisfeitas por uma função que não faz nada), link simbólico para fora, pasta fora da raiz
  (irmã, `..`, a pai, e a vizinha cujo nome apenas **começa** pelo da raiz), raiz inexistente, o
  **caminho vazio** — o acidente de 15/09/2026 virado afirmação — e o gatilho.
- **`ferramentas/mutacoes-purga-cache.py` — 8 baterias, todas decidindo certo, ZERO inertes.** O
  mundo intacto **passa**, e as **7** mutações reprovam **pela afirmação declarada**, que é a metade
  que importa: *reprovar não é a mesma coisa que reprovar pelo motivo certo*.

**OS DOIS ENTRARAM NA BANCADA PELA CONVENÇÃO DE NOME, sem ninguém os listar:** **25 portões sem
rede** contra os **23** de antes, **0 falha**, contados em `bancada.py --lista` e não de cabeça.

**UMA COISA MUDOU NO PORTE, E ELA É UMA AFIRMAÇÃO NOVA.** Na aquametria o teste corta a seção da
casca **entre dois marcadores**, porque lá a purga tem vizinha embaixo. Aqui a seção 13 é a **última
do arquivo**, então o corte vai até o fim — e corte até o fim é honesto **enquanto** for verdade.
Copiar isso calado seria deixar o portão passar a medir código alheio no dia em que nascer uma seção
14. O arquivo ganhou a **afirmação de FRONTEIRA**: se aparecer `function_exists(` depois da última
linha do gatilho, o portão **reprova dizendo que o corte virou mentira**. É a mesma família do que a
**20.8** acabou de cobrar: instrumento que responde curto sem dar erro.

### NO AR, CONFERIDO PELA 18.4

Casca **1.8.0**, revisão **31**, aplicada às **13:40:42Z**. `conferir-no-ar.py`: **454 afirmações, 0
falha**. As **5 linhas de item** da revisão 31 lidas **uma por uma**, todas dizendo `ok`, contra o
`5 aplicado(s)` que a própria linha de fecho declara (20.4 e 20.8). Versão no ar conferida contra o
manifest em **4 de 4** snippets. A parede da rota da 29.3 continua de pé: **401** sem token e **401**
com token errado trazendo `rodametria_rotas_token_invalido`.

**E O DESEMBARQUE CUSTOU 19 MINUTOS DE RELÓGIO POR UM MOTIVO QUE VALE GUARDAR, porque é a 20.6
noutro traje.** O turno do cron rodou às **13:22:08Z** — **quatro minutos ANTES** do push das 13h26Z
—, leu a revisão 30 e não teve o que aplicar; e o cron desta ilha é de **30 minutos**, então visitar
a home não adianta enquanto o evento não estiver **devido**. Foram 13 visitas entre 13h27 e 13h40 e
**nenhuma** adiantou coisa alguma; o `wp-cron.php` devolveu **409** (já havia cron em andamento) e a
revisão entrou sozinha no turno das 13h40. **A 20.6 diz que o cron roda por VISITA, e isso é
verdade; o que ela não diz é que a visita só dispara o que já está DEVIDO.** Quem empurrar nos
primeiros minutos depois de um turno espera o turno seguinte, e a espera **não é defeito**. Dá para
ler o minuto do último turno sem adivinhar: o campo `ultimo` do `/status` o traz, e foi ele que
nomeou a causa aqui — a reserva foi renovada pela 1.1 com esse motivo escrito, em vez de "bloco
longo".

### O ACHADO DE MÉTODO: o "pronto quando" do despacho não era conferível desta nuvem

O despacho pedia `tem_purga_de_cache: true` **no diagnóstico da 29.3**. Aquele retrato exige o
**token do Sync**, que não está no repositório e não deve estar. **Critério de pronto que só quem tem
o token pode ler é critério que ninguém mede** — e a **18.4** manda o contrário com todas as letras:
*"o despacho morre quando é verificado, não quando é escrito"*. Um despacho assim fecharia por
leitura de código, que é exatamente o que a seção 8 desta fábrica mais cobra.

O conserto foi **uma linha**: a casca passou a servir o **mesmo booleano** no `/casca`, que é
**público**. Booleano sobre a existência de uma função desta ilha **não é segredo do servidor**, que
é o que a 29.3 manda não vazar — e `conferir-no-ar.py` ganhou a afirmação correspondente, para a
pergunta passar a ser feita **em toda passada** e não só hoje. **Medido às 13h4xZ:
`tem_purga_de_cache: true`, `versao_casca: 1.8.0`.**

**E ELE NÃO É REDUNDANTE COM A VERSÃO DO SNIPPET DA 20.7, que é o que ia me fazer não escrevê-lo:** a
versão diz **qual byte** o WordPress carregou; este campo diz que a **função existe no processo**. A
chamada dentro do reparo é guardada por `function_exists`, então é **esta** pergunta — e não a
versão — que decide se o reparo vai purgar. **É a 20.7 ao contrário:** lá a **ausência** do `id`
acusa snippet morto; aqui a **presença** do booleano prova a função viva.

### O QUE ESTE BLOCO NÃO PROVA, dito para ninguém procurar aqui depois

Ele **não prova que a purga esvazia o cache do hospedeiro**. Isso só se mede no ar, com um reparo de
verdade, e o reparo exige o token. O que foi medido aqui é a outra metade — a que o ar nunca
mostraria: que a função, levada para fora da pasta dela por um link simbólico, por um `..`, por uma
raiz inexistente ou por um caminho vazio, **para**. E que ela está **carregada** no processo que o
WordPress serve.

### A FILA, RECONFERIDA E NÃO HERDADA

Os três bloqueios de página continuam fechados, e isso **não foi copiado do registro anterior**: as
duas consultas do despacho de 30/10 seguem `nao-medida` em `dados/consultas-de-produto.json` (a
sessão de Chrome do Raphael não aconteceu), e nenhuma consulta dos eixos paramétricos tem veredito
`alvo`. **Nenhum caminho de PÁGINA nova está desbloqueado**, e dizer isso é o que a execução anterior
pediu que se dissesse em vez de inventar bloco.

---

## 2026-11-03 10h17Z–10h4xZ — **A PORTA DE ENTRADA MEDIDA POR DENTRO: a rota da 29.3 que esta ilha nunca teve** — e o portão que nasceu com ela achou um **defeito no próprio modelo**, antes do ar

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** — foco total e absoluto desde 27/10 — e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas e NENHUMA furou.**
(a) Os **três despachos do molde** da seção 32 estão **FECHADOS** (aquametria 21/10 18h2xZ,
clubedomosaico 19h1xZ, robometria 16h1xZ), lido no topo dos três `PROMPT.md`. (b) Nenhum despacho
**ALTA** aberto é de **ilha no ar E quebrada**: o da robometria de 02/11 15h1xZ é de **julgamento
(19.2)** e a ilha está no ar; os quatro ALTA de `dados/despachos.md` são pedidos de **abertura de
egresso** e o **chamado da HostGator**, que é do Raphael pela 19.4(b). `executando_desde` estava
`null`, que pela **1.1** já significa que não há bloco da Fundação vivo — não houve reserva vencida
para o git desempatar (último commit na pasta da ilha: 02/11 19h39Z, ~14h antes). Reserva às
**10h17Z**, push aceito **de primeira**, campo **renovado às 10h36Z**. Zero branch `claude/*` com
commit fora do `main`; **zero PR aberto**.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/`, `/wp-sitemap.xml` e
`/wp-json/rodametria/v1/status` os **três em 200 em TRÊS passadas**, com `aquametria.com.br` em 200
nas mesmas três.

### A PRIMEIRA COISA QUE ESTA EXECUÇÃO FEZ FOI PROCURAR DEFEITO (18.5), E NÃO ACHOU

Bancada **com rede: 26 portões, 0 falha**, antes de uma linha de código. Nenhum defeito aberto no ar.

### E A SEGUNDA FOI RECONFERIR OS TRÊS BLOQUEIOS EM VEZ DE HERDÁ-LOS — porque "nada desbloqueado" é a frase que mais barato se copia

A execução de 02/11 fechou dizendo *"NENHUM BLOCO DE CONSTRUÇÃO DESTA ILHA ESTÁ DESBLOQUEADO HOJE"* e
pedindo que a seguinte dissesse isso em vez de inventar bloco. **Dizer isso sem remedir seria a seção 4
em ação** — resumo velho lido como fato —, então os três foram remedidos:

| o que travava | remedido em 03/11 | resultado |
|---|---|---|
| **F1** — o texto oficial da Resolução Contran | `www.gov.br`, `in.gov.br`, `www.planalto.gov.br`, `www.contran.gov.br`, 2 passadas cada | **000 nas 8**, controle `rodametria.com.br` em **200** nas duas |
| **F3** — `carga_max_kg`, campo de nível 5 | `www.casasbahia.com.br`, `www.extra.com.br`, `www.magazineluiza.com.br`, 2 passadas cada | **000 nas 6** |
| **malha nova** — a sessão de Chrome do despacho de 30/10 | `dados/consultas-de-produto.json`, linha por linha | as duas consultas seguem **`nao-medida`**, sem `visto_por` nem `visto_em`: **o Raphael não abriu as SERPs** |

**14 medições de bloqueio contra 2 de controle verde, e zero intermitência.** Nenhuma consulta dos
eixos paramétricos tem veredito `alvo` em `dados/corpus-buscas.md` — o eixo A está `tomada` nas seis,
o C tem um `tomada` e dois `nao-medida`, e o B **vazou** para fora do Brasil. **A conclusão de 02/11
estava certa, e agora está medida nesta data.**

> **ERRATA DA ENTRADA DE 02/11, e ela é de REGRA e não de número.** A tabela daquele dia atribuiu o
> travamento da cauda à **14.6** (*"cauda só nasce depois da âncora indexada"*), citando
> `primeira_indexacao: null`. **A 21.8 diz o contrário com todas as letras:** com `piso: abaixo` — que
> é o caso desta ilha — *"a série de indexação não decide nada, nem trava, nem adia, nem reduz"*, e
> *"só se disser `piso: atingido` é que a 14.6 e a 14.8 voltam a valer"*. **O veredito não muda** (a
> cauda segue travada pela **30.8**, que é independente de indexação), mas o motivo estava na regra
> errada — e a 21.8 nasceu justamente contando as **duas** vezes em que isso custou um bloco. Esta é a
> terceira aparição da família, e ela custou zero porque havia outro motivo verdadeiro embaixo. **A
> régua da 21.8 cabe em dois segundos: quem for escrever que a indexação trava algo lê o campo `piso`
> antes.**

### POR QUE O BLOCO SAIU DA 29.3 E NÃO DA FILA DE PÁGINAS

Com os três caminhos de página fechados e nenhum defeito no ar, o que sobrou com valor não foi
inventado: **estava escrito no contrato e num despacho, e esta ilha era nomeada nos dois.** A varredura
do despacho de 02/11 em `dados/despachos.md` lista `rodametria | sim | **NÃO** | SIM` — ilha **no ar**,
**sem** a rota de reparo da 29.3, com a porta de entrada medida apenas por fora.

**O DEFEITO QUE AUTORIZA O BLOCO ESTÁ MEDIDO NO AR, COM URL E DATA, como a 31.2 exige** — e são
**quatro quedas da MESMA porta na MESMA conta de cPanel** (`/home3/rapha921/`, a desta ilha):

| quando | onde | o que caiu |
|---|---|---|
| 24/09/2026 19h20Z | clubedomosaico.com.br | **16 de 17 URLs em 404**, nove dias sem ninguém ver |
| 05/10/2026 | clubedomosaico.com.br | a **mesma assinatura byte por byte** (1.057 bytes, bloco único `NFD EPC`) |
| 30/10/2026 | robometria.com.br | **13 de 14 em 404**, e **QUATRO DIAS** fora do ar |
| (a quarta) | outro domínio da mesma conta | despacho **ALTA** de `dados/despachos.md` |

**E a robometria pagou os quatro dias por esta falta exata:** o despacho de 30/10 escreveu *"não é
consertável pelo repositório"* — frase **verdadeira sobre aquela ilha e falsa sobre o Arquipélago**. A
rota nasceu lá em 02/11 e o defeito que ficou quatro dias de pé caiu em **dois minutos**.

### O ANTES, MEDIDO ANTES DE ESCREVER UMA LINHA

`/wp-json/rodametria/v1` listava **quatro** rotas — `/casca`, `/status`, `/sync`, `/token` — e
**nenhuma** era `/rotas`. `?rest_route=/rodametria/v1/rotas` devolvia **404**, com e sem token.

### O QUE ENTROU

- **`snippets/rodametria-casca.php`, seção 12 (1.6.0 → 1.7.0).** Diagnóstico do roteamento medido de
  dentro do servidor (`permalink_structure`, regras no banco, `got_mod_rewrite()`, e do `.htaccess` o
  caminho, se existe, se é gravável, bytes, data e **quais blocos `# BEGIN` tem**), reparo por
  `flush_rewrite_rules( true )` devolvendo **antes e depois**, e a rota atrás do token do Sync.
  **Sem gancho automático (29.4).** O conteúdo do arquivo **nunca sai**: só os nomes dos blocos e a
  contagem de linhas de reescrita, como a 29.3 manda — `.htaccess` de hospedeiro compartilhado carrega
  regra de segurança de terceiro.
- **`ferramentas/teste-rotas.php`** — **39 afirmações mais 40 num processo filho**, 4 mutações
  cobradas. Os mundos são **fabricados**, não os que o site produz: o `.htaccess` das quedas (bloco
  único `NFD EPC`), um arquivo **com uma linha-segredo** que tem de **não** aparecer no JSON, e o
  mundo sem arquivo nenhum — onde a afirmação é que o retrato **não afirma** `tem_wordpress`, porque
  afirmar ali seria inventar. **O processo filho existe por necessidade e não por estilo:**
  `function_exists()` não se desfaz, então o ramo "com as ferramentas de `wp-admin`" e o ramo "sem" não
  cabem no mesmo processo — e o ramo "sem" é o que impede o **verde falso** de dizer que a porta foi
  consertada quando o `flush` não encostou no arquivo.
- **`ferramentas/conferir-no-ar.py`** — a 29.3 lida **sem o token** (autoteste de 12 → **19**
  afirmações). A leitura mora numa **função pura**, e é isso que deixa o autoteste fabricar os quatro
  mundos que esta nuvem não produz: rota **ausente**, parede **aberta** (200 sem token), **portão
  morto** e o **500** do `WP_Error` sem `status`.

### A PAREDE FOI MEDIDA SEM NUNCA TER O TOKEN, e este é o achado de desenho da passada

O **Sync desta ilha não está no repositório** — as outras três têm o seu. Então o nome da função que
guarda o token foi **herdado** das irmãs (`rodametria_sync_token`) e **não pôde ser conferido no
chão**. Isso é a derivação de cabeça que a **20.7** proíbe, e aqui ela erraria **CALADA**:
`token_esperado()` devolveria vazio, a parede negaria **TODO** pedido — inclusive o certo — e a rota
seria um **portão morto com cara de portão**, 401 em tudo, indistinguível de uma parede sã.

**O conserto foi fazer a NEGATIVA dizer qual das três coisas faltou**, em `WP_Error` com códigos
distintos e `status: 401` **explícito** (sem ele o `WP_REST_Server` devolve **500**), e os três são
legíveis **sem** o token: `sem_fonte_de_token`, `token_ausente`, `token_invalido`. **É o mecanismo da
20.7 noutro traje: a ausência passou a falar.**

**E o ar respondeu `rodametria_rotas_token_invalido`** — código que **só sai depois de a casca achar a
fonte do token E rodar o `hash_equals`**. O nome herdado estava certo, e isso deixou de ser aposta e
passou a ser medição, sem o token jamais sair de onde está.

### O ACHADO QUE NÃO ESTAVA NO PLANO — O MODELO DA 29.3 TEM UM DEFEITO, E O PORTÃO O PEGOU NO CHÃO, ANTES DO AR

A primeira passada do `teste-rotas.php` **reprovou**, e não por mundo mal fabricado: as funções de
`stat` do PHP — `file_exists()`, `filesize()`, `filemtime()`, `is_readable()`, `is_writable()` — são
**cacheadas dentro da requisição**; `file_get_contents()` não é. O reparo tira o retrato, reescreve o
`.htaccess` e tira o retrato **de novo, na mesma requisição**. Sem `clearstatcache()`:

- o **antes e o depois** trazem os mesmos `bytes` e o mesmo `mtime` — e o antes/depois que a **29.4**
  existe para oferecer (*"devolve o antes e o depois para quem pediu comparar"*) passa a comparar um
  retrato **com ele mesmo**;
- e `reparado` é calculado **sobre `existe`**, então o caso em que o arquivo **não existia** e o reparo
  o criou sai com **`reparado: false`** — a rota **diz que não consertou a porta depois de
  consertá-la**.

**É reprovação FALSA, que é a pior das duas**, e a **20.5** já escreveu o porquê: *"portão que reprova
página certa é o caminho mais curto para alguém passar a ignorá-lo"*. No uso real é pior ainda: quem lê
`reparado: false` numa ilha caída conclui, **pela própria 29.4**, que o arquivo foi gravado e o
`AllowOverride` está desligado — e **abre chamado na HostGator por um defeito que o reparo já desfez**.

Consertado aqui com `clearstatcache( true, $arquivo )`, com o motivo escrito no código. **A varredura:
`clubedomosaico` (desde 24/09) e `robometria` (desde 02/11) servem a rota e estão SEM a linha.** Virou
**despacho NORMAL**, porque a **seção 3** proíbe editar ilha que esta execução não reservou — a mesma
forma do despacho do `realpath('')` de 15/09, e com o portão pronto para copiar ao lado da linha,
*"senão a linha é retirada no primeiro dia em que alguém a achar redundante"*.

**E as quatro mutações da casca de verdade reprovam, uma a uma:** tirar o `clearstatcache` (cai a
afirmação do antes/depois), pôr a parede **velha** no lugar da nova (cai a distinção dos três mundos),
despejar o `.htaccess` no retrato (**a linha-segredo aparece no JSON**) e ler `tem_wordpress` por
`strpos` solto (**uma menção à palavra WordPress num comentário aprova**).

### O SEGUNDO ACHADO, E ELE FOI DEIXADO EM PÉ DE PROPÓSITO

**Esta é a única ilha no ar sem função de purga de cache do hospedeiro** — clubedomosaico, robometria e
aquametria têm; aqui a palavra "purga" não aparece uma vez no `REGISTRO.md` nem no `ESTADO.md`, em sete
dias de ilha. A chamada entrou **guardada por `function_exists`** e hoje é no-op, e o retrato da rota
**sai no ar dizendo `tem_purga_de_cache: false`** em vez de deixar a falta invisível.

**Não foi consertado de carona, e isso é decisão:** purga que apaga arquivo em disco é exatamente a
função que entrou no Arquipélago com a armadilha do `realpath('')` — que **não devolve `false`, devolve
o diretório de trabalho atual** — e que numa passada **apagou 117 arquivos** da aquametria. Ela entra
**com os dois portões da aquametria ao lado**, e isso é bloco, não carona. Despacho NORMAL aberto hoje.

### O DESEMBARQUE, E O TURNO DE CRON QUE ELE PAGOU

Push às **10h34Z**. O `/status` em **29** com `ultimo: 10:18:18Z` — **anterior ao push**, que pela
régua de três mundos da **20.6** é **turno de cron**, não defeito nem cache (o `raw.githubusercontent`
já servia a **30** na mesma passada, então também não era cache do GitHub). O cron desta ilha **roda
por VISITA e não por relógio**, e as visitas ficaram de pé: a revisão **30** entrou às **10:40:08Z**.
*(Quarta execução seguida a pagar um turno inteiro por um push que cai pouco depois do turno anterior —
e o cron não antecipa evento que não venceu.)*

### NO AR, CONFERIDO PELA 18.4

- **A rota PRESENTE** no índice de rotas do WordPress, ao lado de `/casca`, `/status`, `/sync` e
  `/token`.
- **401** sem token (`rodametria_rotas_token_ausente`) e **401** com token errado
  (`rodametria_rotas_token_invalido`) — a parede medida de fora, com quebra de cache.
- **`conferir-no-ar.py`: 453 afirmações, 0 falha.** *(Antes do desembarque: 457 afirmações e **4
  falhas**, as quatro da rota ausente — o portão morde contra o site real, não só contra mundo
  fabricado.)*
- **As 5 linhas da revisão 30 lidas uma por uma, todas dizendo `ok`**, contra o `5 aplicado(s)` que a
  própria linha de fecho declara (20.4 e 20.8). Casca **1.7.0** instalada às 10:40:06Z, e a versão **no
  ar** conferida contra o manifest em **4 de 4** snippets publicáveis.
- Bancada: **23 portões sem rede** (eram 22) e **27 com rede** (eram 26), **0 falha** nas duas, **0
  denunciado** — contados em `bancada.py --lista`, não de cabeça.

### O QUE ESTE BLOCO NÃO ENTREGA, dito em vez de maquiado

**O reparo não foi exercitado, e não podia ser daqui:** o token do Sync não está no repositório e não
deve estar. O `tem_wordpress: true` **pela rota própria**, que é o "pronto quando" do despacho de
02/11, espera **um GET de quem tem o token**. Está anotado lá, e a metade da rodametria daquele
despacho ficou marcada como fechada com essa ressalva escrita — não apagada.

**E pela 31.1 esta execução entrega infraestrutura, não pixel:** o que foi ao ar é um endpoint, não algo
que o visitante vê. Quem contar a proporção conte esta como **não** — a anterior também foi não, e as
sete antes dela foram sim (casca, F2, três páginas de produto, quatro institucionais, a escada da 25.2,
a caixa da mãe e a versão dos snippets).

### O PRÓXIMO PASSO DESBLOQUEADO

1. **A purga de cache desta ilha** — o único bloco de código desbloqueado que sobrou, já pré-registrado
   como despacho de hoje, e com o diagnóstico da 29.3 no ar acusando a falta.
2. **Nenhum caminho de página nova está desbloqueado**, e isso foi remedido hoje e não herdado. **O
   despacho de 30/10 para o Raphael — duas SERPs e um volume, UMA sessão de Chrome de ~10 minutos —
   continua sendo o gesto que destrava mais por menos.**

## 2026-11-02 19h18Z–19h3xZ — **BLOCO 6: A LISTA DE PROSPECÇÃO DO WIDGET**, a única alavanca de link desta ilha — e a execução começou medindo que **nenhum bloco de página estava desbloqueado**, o que é informação e não fracasso

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** — foco total e absoluto desde 27/10 — e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas e NENHUMA furou.**
(a) Os **três despachos do molde** da seção 32 (aquametria, clubedomosaico e robometria) estão **FECHADOS**,
lido no topo dos três `PROMPT.md`. (b) A **robometria** recebeu despacho novo hoje às 15h1xZ, da ronda
diária, e ele **não é ALTA**: é item de **julgamento da 19.2** (os minutos do ciclo da R2 não dependem da
metragem), e a ilha está **no ar** — a 1.2 abre a exceção só para despacho ALTO em ilha no ar e **quebrada**.
`executando_desde` estava `null`, que pela **1.1** já significa que não há bloco da Fundação vivo: não houve
reserva vencida para o git desempatar. Reserva às **19h18Z**, push aceito **de primeira**, campo **renovado
às 19h27Z**. Branch `claude/dreamy-mccarthy-zfp25a` existe com **zero** commits fora do `main`; nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/`, `/wp-sitemap.xml` e
`/wp-json/rodametria/v1/status` os **três em 200**, com `aquametria.com.br` em **200 na mesma passada**.

### A PRIMEIRA COISA QUE ESTA EXECUÇÃO FEZ FOI PROCURAR DEFEITO, E NÃO ACHOU (18.5)

Bancada **com rede: 24 portões, 0 falha**. E as duas meta descriptions que a ronda de 30/10 listou como
defeito da 19.1 — 161 caracteres na home e 193 na F2, contra o teto de 160 — foram **remedidas no ar** nesta
passada, com quebra de cache: **138** (`/`), **153** (`/autonomia-patinete-eletrico/`) e **150**
(`/veiculos/`). Estão consertadas desde 30/10 e o despacho que as carregava está fechado.

### POR QUE O BLOCO 6 E NÃO OUTRO — a conta inteira, porque ela é o resultado mais útil desta passada

| caminho de página nova | o que o trava | onde está medido |
|---|---|---|
| **F1** (a home que o `VOZ.md` quer, categoria legal) | o limiar só vira `publicavel` lido no texto oficial, e o `.gov.br` inteiro é **`connect_rejected`** | despacho **ALTA** de 28/10 em `dados/despachos.md` |
| **F3** (aguenta o meu peso?) | `carga_max_kg` é campo de **nível 5**, e `casasbahia`/`extra`/`magazineluiza` estão atrás do egresso | despacho **ALTA** de 29/10 |
| **malha nova** (eixos A, B, C) | **30.8**: `alvo` não se afirma desta nuvem. O eixo A está `tomada`, o C tem um `tomada` e dois `nao-medida`, e o B **vazou** (~40 de ~50 ocupantes fora do Brasil) | `dados/corpus-buscas.md`, seção 5 |
| **`moto elétrica` (823 mil) e `scooter elétrica` (301 mil)** | SERP **`alvo`** vista no Chrome em 27/10, endereço reservado — travadas por **PRODUTO**: zero oferta útil na Shopee, e o caminho é o ML, que exige clique humano (25.6) | `dados/consultas-de-produto.json` |
| **cruzamentos / cauda** | **14.6**: cauda só nasce depois da âncora **indexada**, e `primeira_indexacao` é `null` | `ESTADO.md` |

**Sobrou o bloco 6, e ele não sobrou por eliminação: a 14.7 o nomeia.** *"A prospecção do widget em lojas é
a única alavanca de link do projeto e por isso vale mais no começo do que no fim: backlink é o que faz o robô
voltar."* A ilha tem **seis dias** de ar, 9 URLs e nenhuma indexada.

### O QUE ENTREGUEI

- `dados/prospeccao-widget.json` — a fonte, **10 candidatos**, `publicar: false` no topo e em cada linha.
- `dados/prospeccao-widget.md` — a vista legível, **gerada** do JSON e nunca escrita à mão.
- `ferramentas/validar-prospeccao.py` — a **régua** e o **portão de dado**, com `--autoteste`.
- `ferramentas/gerar-prospeccao.py` — escreve o `.md`, importando a régua do portão.

**O PLACAR, CONTADO PELO PORTÃO E NUNCA DIGITADO** (a 23.4 aplicada dentro do dado: número escrito que
discorda da contagem deixa o portão vermelho): **10 candidatos — 1 prioridade 1, 5 prioridade 2, 4
prioridade 3, 0 abertos no navegador.**

O único **prioridade 1** é `bicieletric.com.br`: é o único que fecha as duas condições **medidas** — vende os
dois veículos que as ferramentas desta ilha classificam **e** publica conteúdo no próprio domínio. Quem já
mantém página de guia tem onde encaixar uma ferramenta; quem não tem precisa criar a página antes.

**E a linha mais interessante da lista não é a de prioridade 1, é a `zeliastore.com.br`:** é a loja que vende
exatamente o que as **duas consultas de maior volume desta ilha** pedem e a Shopee não entrega — moto e
scooter elétrica de 1.000 W, com preço publicado e com **"sem CNH" no próprio título**. Quem anuncia "sem
CNH" é quem mais precisa da pergunta respondida com número, e é a venda dele que a dúvida trava.

### AS QUATRO REGRAS DA RÉGUA, e as quatro são sobre NÃO AFIRMAR DEMAIS

1. **NÃO EXISTE `false` nos campos de fato.** Busca sabe afirmar **presença**, nunca ausência — é a mesma
   assimetria que a **30.8** escreveu para o veredito de SERP, aplicada a outro assunto. `true` com evidência
   ou `null` (= não medido); `false` é **recusado** pelo portão, de propósito, para o arquivo não virar uma
   lista de negativas que ninguém mediu.
2. **A EVIDÊNCIA TEM DE SER DO PRÓPRIO DOMÍNIO**, e **a armadilha foi medida nesta coleta**: a Eletricz
   apareceu primeiro numa matéria de `mecanicaonline.com.br` que **fala** dela — nome, cidade, catálogo, tudo
   certo — e matéria de terceiro **não prova nada** sobre o site que vai instalar o widget. A linha dela só
   entrou quando a busca devolveu `eletricz.com.br/...`. A comparação é por **rótulo** e não por `endswith`
   cru: `loja.eletricz.com.br` conta, `eletricz.com.br.golpe.com` não.
3. **A PRIORIDADE NÃO SE ESCREVE, SE CALCULA.** O portão recalcula dos campos medidos e fica vermelho se
   discordar — a mesma doença que o `versao` do manifest desta ilha consertou hoje de manhã: constante que
   alguém sobe à mão e ninguém confere é **rastro, não mecanismo**.
4. **`null` EXIGE MOTIVO ESCRITO.** `contato` e `plataforma` são `null` nas dez linhas, com o motivo em cada
   uma. Campo vazio sem motivo é onde a próxima passada **inventa um e-mail** — e a seção 28 já pagou uma vez
   por e-mail de pessoa de verdade escrito em repositório.

**E a porta dos fundos fica fechada junto:** `abriu_no_navegador` **ausente** não vale como `false`. Se o
campo pudesse faltar, a lista ganharia um estado em que ninguém sabe se alguém abriu o site — e "ninguém
abriu" é justamente a limitação que o arquivo existe para deixar visível. Ausência é reprovação, não omissão
tolerada, que é a letra da 30.8 sobre `visto_por`/`visto_em`.

### A RÉGUA MORA DENTRO DO PORTÃO, E ISSO É DECISÃO E NÃO PREGUIÇA

A Aquametria separou `regua-prospeccao.py` em 24/09 e fez **certo para aquela ilha**: lá a régua é carregada
por quatro arquivos. Aqui ela é carregada por **dois**, e a `bancada.py` desta ilha classifica portão **por
prefixo de nome** e **DENUNCIA** o que não casa com nenhum. `regua-prospeccao.py` **nasceria denunciado**, e o
conserto seria escrever o nome dele numa lista de exceção à mão — exatamente a doença que esta bancada matou
quando deixou de enumerar portão. Então a régua mora no portão, numa fonte só, e o gerador a importa.

**E O AUTOTESTE RODA SEMPRE, ANTES DO ARQUIVO DE VERDADE.** O mecanismo de descoberta de `--autoteste` que
nasceu hoje de manhã só alcança os portões de **rede** (os `conferir-*`), porque foi para eles que ele foi
escrito. Este é dos **sem rede**, então o autoteste dele **nunca entraria na fila sozinho** — e portão que
depende de alguém lembrar não roda. A ordem importa: régua quebrada reprovando o arquivo de verdade **parece
arquivo errado**, então o portão não julga o arquivo se não passar nos próprios mundos primeiro.

### A 31 FOI LIDA ANTES DE ESCREVER FERRAMENTA, NÃO DEPOIS

A **31.2** proíbe portão **novo** sem defeito medido no ar que ele teria pegado — e este portão **nunca vai
pegar defeito no ar nenhum**, porque o arquivo que ele julga tem `publicar: false` e não serve um byte a
visitante nenhum. Quem o autoriza é a **31.5**, que preserva *"portão de dado"* com todas as letras, mais a
seção 10 (nunca inventar dado). **Portão de AR e portão de DADO não são a mesma coisa:** o primeiro protege a
página, o segundo protege a **afirmação**.

**E foi por isso que esta execução escreveu DOIS arquivos de ferramenta e não cinco.** A Aquametria tem
`regua-`, `validar-`, `teste-`, `mutacoes-` e `gerar-`; a bateria de mutação e o teste sintético seriam,
aqui, bancada sobre bancada, que é o que a **31.3** fecha enquanto houver item de conteúdo aberto na fila.
O `--autoteste` faz a metade que importa: **13 mundos fabricados, 13 ok** — o candidato são que tem de passar,
o subdomínio próprio, `false` em campo de fato, evidência de outro domínio, a armadilha do `endswith` cru,
prioridade divergente, `ja_tem_calculadora` derrubando para 3, `null` sem motivo, `abriu_no_navegador`
ausente, campo afirmado sem evidência, vitrine de marketplace, instrumento que esta nuvem não tem, e
`publicar: true`.

**E a régua foi MUTADA SOBRE O DADO DE VERDADE**, não só sobre mundo sintético: a prioridade do
`bici-eletric` foi trocada de 1 para 2 no arquivo real e o portão reprovou com a frase certa
(*"prioridade escrita 2, calculada 1 dos campos medidos"*) antes de o arquivo ser restaurado e aprovar de
novo. Autoteste que só roda contra mundo fabricado prova a régua; mutação sobre o dado real prova que ela
está **ligada** ao dado.

### O ACHADO QUE NÃO É SOBRE PROSPECÇÃO, E ELE FOI PARA `dados/despachos.md`

**Duas páginas do MESMO site citam a MESMA Resolução Contran 996/2023 com números diferentes.** Medido por
busca restrita a `eletricz.com.br`: uma página de produto afirma *"potência máxima permitida de até 1000
Watts, com velocidade de até 32 km/h de fábrica"* e outra, do mesmo domínio e sob a mesma resolução, afirma
*"potência máxima de 4.000W para autopropelidos"*.

O corpus do bloco 1 já media três limites diferentes **entre** três publicadores. Isto é um andar abaixo: a
contradição existe **dentro de uma fonte**. **E isso sobe o custo do despacho ALTA do `gov.br` em vez de só
confirmá-lo** — enquanto a fonte primária não chega, **não existe "a leitura de mercado"** para a F1 herdar, e
qualquer régua de maioria entre fontes secundárias escolheria um número sem saber qual. A regra escrita no
bloco 2 desta ilha — *"o limiar só vira `publicavel` depois de lido no texto oficial, com data"* — está medida
em campo. A evidência entrou no despacho.

### A LINHA VENCIDA QUE ESTA EXECUÇÃO ACHOU NA PRÓPRIA FILA

O parágrafo de fecho do bloco **5e** ainda dizia *"O QUE FICA, e é BLOCO e não conserto: `/veiculos/` ESTÁ
FORA DO MOLDE"*. Os **dois** itens dele estavam feitos — a caixa da mãe em 02/11 às **13h42Z** (commit
`ce91604`) e o campo `versao` às **17h4xZ** — e **só o segundo tinha sido marcado**. Esta execução leu a linha
como pendência e foi conferir. Marcado agora, com o texto velho preservado embaixo. **É a seção 4 em forma de
fila:** o trabalho anda e o índice fica para trás em silêncio.

### A BANCADA

**22 portões sem rede, 0 falha** (eram 20) e **24 com rede, 0 falha**, os dois contados em `--lista` e não de
cabeça. **0 denunciado** — os dois arquivos novos entram pela convenção de nome (`validar-` e `gerar-`), sem
lista nenhuma. E o `gerar-prospeccao.py` nasceu **INERTE** na primeira rodada da bancada, pega por ela: não
imprimia `APROVADO`/`REPROVADO` no `--conferir`, e portão cujo texto não diz o veredito em português não é
lido por ninguém. Consertado na mesma passada.

### NADA FOI AO AR NESTA EXECUÇÃO, E ISSO ESTÁ DITO E NÃO ESCONDIDO

A **31.1** pede 7 de cada 10 execuções entregando algo que o visitante vê. **Esta é das 3 que não entregam**:
o arquivo tem `publicar: false` em cada linha, de propósito. As anteriores desta ilha entregaram no ar quase
sem exceção — a casca, a F2, as três páginas de produto, as quatro institucionais, a escada da 25.2, a caixa
da mãe e a versão dos snippets —, então a proporção segue folgada. Quem for contar, conte esta como **não**.

### ERRATA DE MÉTODO, ESCRITA PELA PRÓPRIA EXECUÇÃO QUE A COMETEU — a mensagem do commit deste bloco está com três buracos, e a causa vale para toda execução desta fábrica

O commit `a4f9ba7` saiu com três trechos **comidos**: onde a mensagem dizia o nome de
`validar-prospeccao.py`, a palavra `.md` e `publicar: false`, saiu vazio. **A causa não é o git, é o
shell:** a mensagem foi passada entre aspas duplas em `git commit -m "..."`, e **crase dentro de aspas
duplas é substituição de comando** — o bash tentou *executar* `validar-prospeccao.py`, `.md` e
`publicar:`, imprimiu `command not found` nos três e **colou o resultado vazio no lugar**. O commit foi
criado e empurrado assim.

**Não foi corrigido, de propósito, e a razão é regra:** consertar exigiria reescrever um commit que já
está no `main`, e **force push é proibido** no contrato — a seção 1 é literal nisso, e a reserva por
commit das execuções paralelas depende disso. Empurrar commit vazio só para anotar também é proibido.
Então a correção mora **aqui**, que é onde o log da ilha é lido, e o conteúdo do commit está intacto:
os arquivos são os mesmos, só a prosa da mensagem tem três lacunas.

**A régua, e ela cabe numa linha:** mensagem de commit com crase, cifrão ou `$(...)` vai por **arquivo**
(`git commit -F`) ou por **heredoc com delimitador entre aspas simples**, nunca por `-m "..."`. É a mesma
família do `git log` raso e do número de tela digitado: **o instrumento respondeu, não deu erro visível no
resultado, e a resposta saiu menor que a verdade com cara de completa.**

### O PRÓXIMO PASSO DESBLOQUEADO

1. **NENHUM BLOCO DE CONSTRUÇÃO DESTA ILHA ESTÁ DESBLOQUEADO HOJE**, e isso é informação e não fracasso. Os
   três caminhos de página nova estão travados por coisas que **não se resolvem desta nuvem**: o `gov.br`
   (F1), o nível 5 de varejo grande (F3) e o **Chrome do Raphael** (as duas SERPs do despacho de 30/10 e as
   duas etiquetas do Mercado Livre). A execução seguinte que encontrar os três ainda fechados deve **dizer
   isso** em vez de inventar bloco — e o despacho de 30/10, **uma sessão de Chrome de ~10 minutos**, continua
   sendo o gesto que destrava mais por menos.
2. **ABRIR OS DEZ CANDIDATOS NO NAVEGADOR**, que é o que transforma `null` em medido: `contato`, `plataforma`
   e `ja_tem_calculadora` são os três campos que a lista não sabe e **diz** que não sabe. Dez domínios, um
   navegador, e a lista passa de ordenada para acionável. Também não é bloco desta nuvem — é despacho, pela
   mesma razão da 30.8.

## 2026-11-02 17h03Z–17h47Z — **O CAMPO `versao` NO `manifest.json`**, e a metade que o `sha256` nunca alcançou: qual versão o WordPress **carregou**

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** — foco total e absoluto desde 27/10 — e pela
**1.2** não há escolha a fazer. **As duas exceções que furam o foco foram conferidas e NENHUMA furou.**
(a) Os **três despachos do molde** da seção 32 (aquametria, clubedomosaico e robometria, os três de
21/10) estão **FECHADOS** e conferidos no ar, lido no topo dos três `PROMPT.md`. (b) A **robometria**
recebeu **despacho novo hoje às 15h1xZ**, da ronda diária, e ele **não é ALTA**: é item de **julgamento
da 19.2** — os minutos do ciclo da R2 não dependem da metragem —, com a própria Sentinela escrevendo que
a escolha é "entre duas opções defensáveis". A 1.2 abre a exceção só para **despacho ALTO em ilha no ar
e QUEBRADA**, e a 18.1 é literal sobre o resto: *"despacho NORMAL de ilha fora do foco espera, por mais
antigo que seja."* `executando_desde` estava `null`, que pela **1.1** já significa que não há bloco da
Fundação vivo — não houve reserva vencida para o git desempatar. Reserva às **17h03Z**, push aceito **de
primeira**, campo **renovado às 17h13Z** pela mesma execução. O branch `claude/dreamy-mccarthy-6yptxq`
existe e tem **zero** commits fora do `main`; **nenhum PR aberto**.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/`, `/wp-sitemap.xml` e
`/wp-json/rodametria/v1/status` os **três em 200**, com `aquametria.com.br` em **200 na mesma passada** —
controle verde, uma passada, zero intermitência.

**POR QUE ESTE BLOCO: é o item (1) do `bloco_atual`**, pré-registrado desde 30/10 e repetido no fecho de
hoje às 14h14Z com estas palavras — *"mexe no CONTRATO DO SYNC, que é o único canal desta ilha, então é
bloco com desembarque próprio e nunca carona. Hoje `RODAMETRIA_PRODUTO_VERSAO` subiu para 1.2.0 e
NINGUÉM A LÊ — subi-la é rastro, não mecanismo."*

### TRÊS COISAS, E ELAS NÃO SÃO A MESMA

| o que | o que prova | existia? |
|---|---|---|
| `sha256` do manifest | o **byte** que está no repositório | sim |
| `versao` do manifest | **qual versão** esse byte se declara ser | **nasceu hoje** |
| `/casca` → `versoes` | qual versão o **WordPress carregou** | **nasceu hoje** |

A terceira é a que o `sha256` **não alcança**, e a cicatriz tem preço escrito: a **20.4** custou **sete
páginas** servindo o tema cru na clubedomosaico, **duas vezes em três dias**. O Sync grava o snippet
**inativo de propósito** e ativa depois; quando a ativação falha ele escreve `gravado (#13) mas NÃO
ativado` numa linha do log, **segue em frente e sobe a revisão**. O byte estava certo no repositório nas
duas vezes.

**E O MECANISMO É A AUSÊNCIA, não um valor errado.** Snippet que não está ativo **não roda**, logo não
pendura o filtro `rodametria_versoes`, logo o `id` dele **não aparece** no `/casca`. O portão de ar diz
**"não ativado"** e **"versão diferente"** separados, porque o conserto das duas não é o mesmo — e pela
**20.5** portão que reprova a página certa é o caminho mais curto para alguém ignorá-lo.

### A CONSTANTE É ACHADA NO ARQUIVO E NUNCA DERIVADA DO `id`

Derivar daria `RODAMETRIA_INSTITUCIONAL_VERSAO`, que **não existe**: o arquivo abrevia para
`RODAMETRIA_INST_VERSAO`. A convenção de cabeça acerta em **três dos quatro** snippets desta ilha e erra
no quarto, **calada** — "constante ausente" pareceria "snippet sem versão". Então o espelho **pergunta
ao arquivo** quem ele define, e zero ou mais de um `define` é **denúncia**, nunca escolha. E ele
**imprime o nome da constante que leu**, pela mesma razão de imprimir a troca: espelho auditável sem
abrir o PHP.

### O ACHADO QUE O ESPELHO ACUSOU NO MINUTO EM QUE NASCEU

A prosa do `descricao` **declarava a versão corrente nos QUATRO snippets, e estava velha nos quatro**: a
casca dizia `1.4.0` servindo 1.5.0; o f2, o produto e o institucional diziam `1.0.0` servindo 1.3.2,
1.2.0 e 1.0.0. **Duas declarações do mesmo fato começam iguais e só uma sobe** — é a família do número
de tela digitado, a cicatriz que esta ilha mais paga. A prosa **deixou de declarar a versão** e o campo
passou a ser o dono; as entradas de **histórico** ficaram, porque fato datado ("1.4.0 (29/10/2026): …")
não é afirmação sobre o agora.

### O PORTÃO NOVO, E ELE É PHP POR DECISÃO E NÃO POR GOSTO

`ferramentas/teste-versao-dos-snippets.php` — **43 afirmações, 6 de 6 mutações reprovadas.** É PHP pelo
mesmo motivo escrito no `teste-caixa-da-mae.php`: **a coleta é decidida em PHP**, então a régua roda
`add_filter` e `apply_filters` **de verdade** e **chama** o coletor, em vez de conferir a *forma* do
código. Régua em Python sobre o texto do PHP conferiria a forma, nunca a decisão.

**A afirmação que torna honesto o portão de ar** é a de número 3 dele: todo snippet `publicar: true`
**se registra com o próprio `id`**, medido no chão, antes de o ar ser consultado. Sem ela, `id` ausente
no `/casca` poderia ser descuido do repositório, e o portão de ar estaria acusando o ar de um defeito da
bancada. **As seis mutações:** a chave do f2 deixando de ser o `id`; o produto escrevendo a versão como
literal ao lado da constante; o institucional parando de pendurar o filtro; o manifest declarando versão
diferente da constante; o coletor deixando de semear a própria casca; e o `/casca` parando de servir o
campo.

### O DESEMBARQUE, E A 20.6 OUTRA VEZ — TRÊS MINUTOS DE ATRASO CUSTARAM UM TURNO INTEIRO

Push às **17h13Z**, revisão **29**. O `/status` respondeu **28** com `ultimo: 17:12:47` — **recente e
anterior ao push por 13 segundos**, que pela régua da **20.5** é **turno de cron**, nem defeito nem
cache; `raw.githubusercontent.com` já servia 29 na mesma passada. Laço de visita de pé pela **20.6** (o
cron desta ilha roda por **visita**, não por relógio): **35 visitas** entre 17h14Z e 17h40Z, e a revisão
pousou às **17h40:55Z**, no turno seguinte. É a terceira execução seguida desta ilha a pagar um turno de
cron inteiro, e a causa é sempre a mesma: **o push cai poucos minutos depois de um turno**, e o cron não
antecipa evento que ainda não venceu.

### MEDIDO NO AR (18.4)

- **ANTES:** `/casca` na revisão 28 devolvia `versao_casca 1.5.0` e **nenhum** campo `versoes` — as
  chaves eram `['instalado', 'paginas', 'versao_casca']`. Exatamente o que este bloco entrega.
- **DEPOIS:** `conferir-no-ar.py` em **453 afirmações, 0 falha**, com a linha que é o bloco:
  *"versão no ar conferida contra o manifest em **4 de 4** snippet(s) publicáveis: rodametria-casca
  **1.6.0**, rodametria-f2 **1.4.0**, rodametria-institucional **1.1.0**, rodametria-produto
  **1.3.0**"*.
- **20.4, as 8 linhas da revisão 29 lidas uma por uma, todas dizendo `ok`** — e agora conferidas contra
  o número que a própria linha de fecho declara (`8 aplicado(s)`).
- Bancada **sem rede: 20 portões, 0 falha** (eram 18 no começo da execução) e **com rede: 24 portões, 0 falha** (eram 22 no fecho das 14h14Z de hoje), os dois contados em `--lista` e não de cabeça.

### O DEFEITO QUE ESTE BLOCO ACHOU NO PRÓPRIO PORTÃO DA 20.4 — E ELE ESTAVA VERDE

**O portão escrito para cobrar "resumo verde não é entrega" estava lendo SÓ O RESUMO.** A primeira
passada de hoje imprimiu, em verde: *"20.4: log lido linha por linha — 15 linha(s) na janela, **1 da
revisão 29**, 0 linha de falha nesta entrega"*. A revisão 29 tem **1 linha de fecho e 8 de item**. **As
8 linhas de item nunca foram lidas por ele** — e linha de item é justamente onde mora `gravado mas NÃO
ativado`.

**A causa, e ela estava escrita no comentário, invertida:** *"cada revisão COMEÇA com a linha `revisão
N:`. As linhas desta entrega são as que vão do topo até essa linha, inclusive."* O log vem **do mais
novo para o mais velho** e a linha de fecho é escrita **por último**, então ela está **no topo** do
grupo: o corte começava nela e parava nela, devolvendo uma linha só. **Nenhuma leitura pegava isso** —
as execuções de 30/10 e das 14h14Z de hoje escreveram *"as 7 linhas"* e *"as 5 linhas da revisão
corrente dizendo ok"*, números que saíam de leitura **à mão**, não deste portão, que nas duas vezes
tinha lido **1**. É a mesma família da seção 29 com um andar a mais, igual à 20.4 original: **a prova do
defeito já estava impressa pelo próprio portão, e faltava alguém ler o número dela.**

**O CONSERTO, e ele é mais forte do que o corte certo.** (1) O corte passou a ir **do fecho para baixo**
até a próxima linha de revisão. (2) A afirmação virou **positiva** — *"nenhuma pode deixar de dizer
`ok`"* é a letra da 20.4 —, no lugar de procurar `FALHA`/`erro`/`NÃO`: procurar palavra de falha é a
leitura pelo avesso e só pega as falhas que alguém já imaginou. (3) **O portão não acredita mais na
própria contagem:** a linha de fecho **declara** `N aplicado(s)`, e as linhas lidas têm de ser esse
número — janela que rolou e levou item deixa a conta aberta, e aberta ela é **dita**, em vez de aprovar
sobre o que sobrou com cara de completo.

**E O CONSERTO É MEDIDO, não afirmado:** `conferir-no-ar.py --autoteste`, **12 de 12 afirmações, 0
falha**, sete mundos. O **primeiro é o mundo de verdade** — o log lido no `/status` às 17h40Z, com as 15
linhas. O terceiro injeta `gravado (#9) mas NÃO ativado` e exige que seja **pego**. O quarto rola a
janela e exige que a conta **abra**. E o **sétimo refaz a régua velha ao lado da nova** e exige que as
duas **discordem** (1 contra 8): autoteste em que as duas concordam não está medindo conserto nenhum.

**E ELE NÃO DEPENDE DE NINGUÉM LEMBRAR.** `conferir-no-ar.py` é portão de **rede** e só rodaria com
`--no-ar`; o autoteste não precisa de rede. A `bancada.py` passou a **perguntar ao arquivo** se ele
aceita `--autoteste` e a rodar essa metade **sempre**, no conjunto sem rede — nada a enumerar, pela
mesma convenção de descoberta de toda esta bancada. Foi isso que levou a bancada sem rede de 19 para
**20 portões**.

## 2026-11-02 13h31Z–14h2xZ — **A SEÇÃO MÃE `/veiculos/` ENTRA NO MOLDE**, e o que ela custava não era aparência: os 700 px da 32.5 **nunca a julgaram**

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** e pela **1.2** não há escolha a fazer. **As duas
exceções que furam o foco foram conferidas e NENHUMA furou.** (a) O despacho **ALTA** da **robometria**
(*"a ilha está fora do ar, menos a home"*) está **FECHADO** desde 02/11 às 10h3xZ, conferido no ar pela
18.4 pela execução anterior — 16 de 16 URLs em 200. (b) Os **três despachos do molde** da 32.6
(aquametria, clubedomosaico, robometria) estão **FECHADOS**, conferido no topo dos três `PROMPT.md`. O
despacho **NORMAL** de 02/11 na aquametria (os dois instrumentos da seção 29 que ela não tem) **espera
pelo foco**, e a 1.2 é explícita: *"despacho NORMAL de ilha fora do foco espera, por mais antigo que
seja."* `executando_desde` estava `null`, que pela **1.1** já significa que não há bloco da Fundação
vivo. Reserva às **13h31Z**, push aceito **de primeira**, campo **reescrito às 13h42Z** pela mesma
execução. Nenhum branch `claude/*` à frente do `main` e nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/` e `/wp-json/rodametria/v1/status` os dois
em **200**, com quebra de cache.

**POR QUE ESTE BLOCO: ele é o item (1) do `bloco_atual`**, escrito pelo fecho de 30/10 às 19h44Z com
estas palavras — *"`/veiculos/` ESTÁ FORA DO MOLDE, e o portão de pixel o diz com essas palavras ('sem
componente de molde nenhum') nas duas passadas de hoje. (…) É BLOCO e não conserto: a página não está
quebrada, ela está NÃO MEDIDA."*

### O QUE ESTAVA ERRADO, E A PALAVRA CERTA NÃO É "FEIO": É **NÃO JULGADO**

A **32.2** manda, para página de resposta ou ficha: *"caixa de resposta no topo (o número e a condição
em uma frase)"*. A mãe servia **dois `<p class="rdm-promessa">`** e ia direto para a lista de famílias.
A **32.5** põe o teto de **700 px** na caixa de resposta de quem não tem formulário — e o portão de
pixel desta ilha, que descobre as páginas no `wp-sitemap.xml` e julga **toda** página que serve o molde,
dizia nas duas passadas de 30/10: `fora /veiculos/ — sem componente de molde nenhum`.

**Isso é pior do que reprovar**, e a 32.5-c já tinha escrito a família: *"regra de celular escrita para
uma família de cartão não alcança a outra"*. Aqui a página **não tinha o componente**, então não havia
o que medir: a régua a listava e seguia. Oito páginas eram julgadas, nove existiam. **A conta de 8 de 8
estava certa e era sobre o mundo errado.**

### O QUE ENTROU — DUAS COISAS, E A PRIMEIRA É UM NÚMERO QUE NENHUMA OUTRA PÁGINA DESTA ILHA TEM

**(1) A CAIXA DE RESPOSTA, com o número AGREGADO das filhas.** Toda outra página desta ilha tem número
de **uma** consulta; a mãe não é consulta nenhuma — o número dela é a **soma** das filhas prontas, e a
faixa de preço **atravessa** as famílias. Duas decisões de mecanismo, as duas com cicatriz ao lado:

- **A faixa se compara pelo campo NUMÉRICO da vitrine (`de_numero`/`ate_numero`), nunca pela string.**
  `R$ 1.297,13` contra `R$ 2.299,99` ordenado por texto acerta **por sorte do alfabeto**, porque os dois
  têm quatro dígitos. No dia em que uma bicicleta de `R$ 899,00` entrar, a comparação por texto a põe
  **depois** de `R$ 1.297,13`, e a página passa a dizer que o mais barato custa quatrocentos reais mais.
  A string formatada que vai para a tela é a **do registro que ganhou a comparação**, nunca remontada.
- **As datas saem como lista de DISTINTAS, e não como "a data".** Duas filhas lidas em dias diferentes
  **não têm** uma data, e a frase que escolher uma delas mente sobre a outra. É a mesma pedra que a
  linha do piso da tabela da filha já paga — *"com duas buscas distintas a linha NÃO sai, porque 'a
  primeira' é arbitrária"* —, um andar acima. Com datas iguais sai a frase com a data; com datas
  diferentes sai outra frase, que **não imprime data nenhuma** e manda a pessoa à página da família.

**A prosa é UMA FRASE POR MUNDO, escolhida por `rdm_produto_caixa_frases()` — função PURA sobre a
relação já calculada.** A seção 8 manda isso com todas as letras: *"toda recusa que depende de uma
relação entre os dados — empate, ausência, borda, limite — mora numa função pura que recebe a relação
já calculada; recusa escrita dentro do laço que a calcula só é testável no dia em que o banco produzir o
caso, e é esse o dia em que ela vai estar errada."* Nenhuma das frases é digitada no PHP: as **onze**
moram em `dados/paginas-de-produto.json`, com molde no lugar de todo número, e o conferidor da vitrine
**reprova dígito digitado** em qualquer campo da mãe.

**(2) O SEGUNDO BOTÃO DO CARTÃO DE CADA FAMÍLIA**, caindo no `id="comprar"` da filha — que é literalmente
o que a 32.2 pede do *"Ver produtos"*: *"leva ao bloco de compra da ferramenta ou a link de afiliado do
banco"*. **O título do cartão não mudou um byte**, porque a 32.3 protege âncora e link interno.

**E O BOTÃO "Calcular" DA 32.2 NÃO SAIU, de propósito, com o motivo escrito no código para a próxima
execução não o "consertar":** a 32.2 o quer *"com o parâmetro da página já passado na URL"*, e a F2
desta ilha recebe **tensão e amperagem de bateria** — família de veículo não é parâmetro dela. Botão por
família seria o **mesmo link duas vezes**, a pedra que a linha do piso já paga. A conta de bateria
continua linkada **uma** vez, na frase que já existia.

### OS PORTÕES — **18 sem rede (eram 17) e 22 com rede (eram 21), 0 falha nas duas.** UM novo, e ele achou TRÊS coisas no minuto em que nasceu

`ferramentas/teste-caixa-da-mae.php` **é PHP** pelo motivo que o `teste-nota-de-preco.php` e o
`teste-escada-de-compra.php` já escreveram: a escolha da frase é decidida em PHP, então a régua **chama
a função** em vez de ler o arquivo. Régua em Python sobre o texto do PHP conferiria a **forma** do
código, nunca a decisão. **78 afirmações, 0 falha.**

**OITO MUNDOS FABRICADOS, E O DADO DE HOJE EXERCITA UM.** O banco tem duas famílias prontas, as duas
lidas no **mesmo** dia, e três que faltam. Os outros sete não existem — e a **32.5-d** é literal sobre o
que isso significa: *"a regra do molde que nunca rodou contra o dado de verdade está quebrada e parece
sã."* Então a bateria os fabrica: duas famílias na mesma data (hoje), duas em **datas diferentes**, uma
família só, **nenhuma** família pronta, uma família faltando, **nenhuma** faltando, família pronta **sem
faixa de preço**, e preço de **três dígitos** ao lado de quatro.

**AS TRÊS COISAS QUE O PORTÃO ACHOU, pagas antes de ele aprovar:**

1. **O campo de documentação que eu havia escrito DENTRO de `mae.caixa`.** O conferidor da vitrine varre
   **todo** campo da mãe contra dígito digitado, e prosa de documentação cita número de seção. **O
   portão estava certo e o lugar estava errado:** o campo saiu para a raiz do arquivo, com o motivo ao
   lado. A trava que pegou isso é a mesma que o `REGISTRO.md` desta ilha registra de 29/10 — *"prosa que
   afirma o estado do banco é número digitado em outro traje"*.
2. **O ramo da família SEM FAIXA DE PREÇO nasceu sem singular**, e servia `"nas 1 famílias"` — o **mesmo**
   plural que mente que o ramo com faixa pagava na linha de cima. Dois ramos irmãos, um com a lição e o
   outro sem: é a 32.5-c em miniatura, dentro de uma função.
3. **A MUTAÇÃO DA FAIXA POR STRING SOBREVIVEU na primeira rodada**, e esta é a que vale registro. Com
   **quatro dígitos em todo preço** o alfabeto acerta por sorte, então a mutação *"compare por texto"*
   passou — e um portão cuja mutação sobrevive é um portão que não vigia a regra que diz vigiar. **O
   mundo em que ela morde é o do preço de três dígitos** (`R$ 899,00` perdendo de `R$ 1.297,13`), e ele
   entrou na bateria como **mundo 8**, com a função de verdade acertando-o. As **3 de 3** mutações
   reprovam.

**E `conferir-produto-no-ar.py` PASSOU A CONFERIR A MÃE, que não tinha portão de ar NENHUM.** A causa é
estrutural e vale mais que o conserto: aquele portão descobre as páginas **casando o sitemap com os
slugs da vitrine**, e a mãe **não é consulta** — não tem linha na vitrine, então caía fora dele, fora do
`conferir-no-ar.py` (casca e F2) e fora do `conferir-institucional-no-ar.py`. **Três portões de ar e a
página mãe não estava em nenhum.** O que ele cobra nela agora: a caixa existe e vem **antes** dos
cartões (presença não é ordem); o número dela é a **soma da fonte** das famílias que estão no sitemap,
contada no portão e comparada com a tela; zero molde `{...}` cru; o botão de cada família cai num
`#comprar` de URL **que está no sitemap**; e **zero link patrocinado**, porque a mãe não vende nada e
link de afiliado fora de bloco de compra é reprovação da 32.5.

**RODADO CONTRA A REVISÃO 27 ANTES DO DESEMBARQUE: 4 falhas**, as quatro exatamente o que este bloco
entrega — sem caixa, sem caixa antes dos cartões, sem número em Mono, e 0 botão de família para 2
famílias no ar. **Portão que nunca falhou não é portão.**

**E ELE REPROVOU A PÁGINA CERTA depois do desembarque, numa passada só** — o quarto achado, e este é da
régua e não do código: contava a caixa por `class="rdm-molde-caixa`, que é **prefixo** de `-rotulo`,
`-numero`, `-unidade` e de cada `-frase`, então uma caixa sã com três frases contava **sete**. Passou a
contar o **contêiner** com a classe do tom. É a pedra da linha do piso da tabela (*"se conta pela
classe, nunca pela frase"*) com o **sinal invertido** — aqui a classe é prefixo de outras seis — e a
lição é a da 20.5: *portão que reprova página certa é o caminho mais curto para alguém passar a
ignorá-lo.*

**E UM NÚMERO MEU, CORRIGIDO ANTES DE FECHAR:** a observação do manifest e a mensagem do commit
`ce91604` dizem *"22 na bancada sem rede (eram 21)"*. **22 é a bancada COM rede.** Sem rede são **18**
(eram 17), contados em `bancada.py --lista` e `--lista --no-ar`, não de cabeça. Número certo na
etiqueta errada é a família do número de tela digitado, e a observação do manifest já está corrigida;
a mensagem do commit não dá para reescrever sem reescrever história, então a correção fica aqui.

### O DESEMBARQUE, CONFERIDO NO AR (18.4)

**Revisão 28**, pousada às **14h10Z**. O Sync desta ilha roda por **visita** (20.6) e **não antecipa
evento que ainda não venceu**: o turno anterior foi às 13h41:56Z, dois minutos **antes** do push das
13h43Z, então a revisão esperou o turno seguinte — **27 minutos de laço abrindo a home**, não defeito e
não cache. É o mesmo custo que o fecho de 30/10 mediu e nomeou: *"um turno de cron"*.

**As 5 linhas da revisão corrente do log dizem `ok`, lidas uma por uma (20.4).**

- `conferir-produto-no-ar.py`: **205 afirmações, 0 falha** (eram 200 antes da metade da mãe).
  `/veiculos/`: **1** caixa de resposta, número **21** = soma da fonte das **2** famílias no sitemap,
  **2** botões de família caindo no `#comprar` da filha, **0** molde cru, **0** link patrocinado.
- `conferir-32-5-no-navegador.mjs`, a 390 px num Chromium de verdade: **9 de 9 páginas do molde dentro
  da 32.5, 0 fora do molde**, contra 8 de 8 com 1 fora de antes. A mãe mede **405 px** de caixa contra
  o teto de **700**, e `compra` sai como *"não se aplica"* — ela não vende nada, e é por isso que ela
  **não pode** servir link patrocinado.
- `bancada.py --no-ar`: **22 portões, 0 falha.**

### O PRÓXIMO PASSO DESBLOQUEADO — e são DOIS, em ordem de valor

1. **O CAMPO `versao` NO `manifest.json`**, para a constante de cada snippet ser espelhada e **impressa**
   como o `sha256` já é. Está pré-registrado desde 30/10 e continua sendo o primeiro da fila: mexe no
   **contrato do Sync**, que é o único canal desta ilha, então é bloco com desembarque próprio e nunca
   carona. Hoje `RODAMETRIA_PRODUTO_VERSAO` subiu para `1.2.0` **e ninguém a lê** — subi-la é rastro,
   não mecanismo, e o comentário dela já diz isso.
2. **A FILA NORMAL segue no bloco 4**, com a F1 e a F3 travadas por **abertura** e não por coleta:
   `gov.br` para o limiar legal da F1 e o nível 5 (`casasbahia`, `extra`, `magazineluiza`) para
   `carga_max_kg` da F3 — os dois despacho **ALTA** em `dados/despachos.md`, e os dois são gesto do
   Raphael no navegador dele.

**E O DESPACHO DE 30/10 PARA O RAPHAEL CONTINUA ABERTO**, intocado por esta execução: duas SERPs
(`patinete eletrico 1000w` e a segunda da lista) e um volume, numa sessão de Chrome de ~10 minutos.

## 2026-10-30 19h17Z–19:44Z — **A ESCADA DA 25.2 CHEGA À TELA NAS DUAS PONTAS**, e o ramo que ela conserta não existe no dado publicado — é por isso que ninguém o via

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** e pela **1.2** não há escolha a fazer. **As duas
exceções que furam o foco foram conferidas e NENHUMA furou.** (a) A **robometria** segue *"no ar e
quebrada"* com despacho **ALTA**, o que pela 1.2 e pela 18.1 teria precedência — mas o conserto **não é
do repositório**, e remedi antes de respeitar o herdado (seção 4): `robometria.com.br/` em **200** e
`/robots.txt`, `/wp-sitemap.xml` e `/wp-json/robometria/v1/status` os três em **404**, com
`rodametria.com.br` e `aquametria.com.br` em 200 na mesma passada. O gesto é de cPanel e é do Raphael.
(b) Os **três despachos do molde** da 32.6 (aquametria, clubedomosaico, robometria) estão **FECHADOS** —
conferido no topo dos três `PROMPT.md`. `executando_desde` estava `null`, que pela **1.1** já significa
que não há bloco da Fundação vivo. Reserva às **19h17Z**, push aceito **de primeira**, campo **reescrito
às 19h29Z** pela mesma execução. Nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/`, `/wp-sitemap.xml` e
`/wp-json/rodametria/v1/status` os três em **200**, com `aquametria.com.br` em 200 na mesma passada.

**O BRANCH `claude/*` E O `main` SÃO O MESMO COMMIT, e o `git log` desta nuvem veio RASO** — `.git/shallow`
existe, 50 commits. Pela correção de 27/10 no topo da seção 1.1 **não contei nada de história** nesta
execução, e por isso nenhum número daqui é de contagem de `main`.

**POR QUE ESTE BLOCO: ele estava PRÉ-REGISTRADO pelo fecho das 18h13Z**, textual — *"na vitrine, a escada
da casca ESCONDE o cartão quando `url` está vazia, em vez de cair na busca como a F2 faz (…) A tabela de
16 linhas também serve só a ficha, sem a linha discreta da busca. Os dois são BLOCO, não conserto."*

### O DEFEITO, E ELE NUNCA APARECEU NUMA PÁGINA

A **25.2** é literal nas duas pontas: a ficha de produto é **bônus**, e *"quando não existir, ou quando a
ronda marcar como morta, **a busca sobe e vira o botão** — sem esperar decisão humana, sem página ficar
com 'link de loja em breve'"*. **Só a primeira ponta estava na tela.**
`rodametria_casca_cartao_de_compra()` devolvia **string vazia** quando a `url` chegava vazia, e a segunda
ponta vivia no **CHAMADOR** da F2, que resolvia a escada antes de montar o item.

**A F2 nunca teve o defeito. A VITRINE de produto tinha TRÊS lugares lendo a `url` crua**, e os três
quebravam juntos no dia em que uma ficha morresse:

1. o **CARTÃO** sumia da página — com o piso gravado no mesmo registro, ao lado, sem ninguém para o promover;
2. a célula **"Comprar"** da tabela servia `href=""` — e `href=""` **não é botão morto**: é um botão que
   **recarrega a própria página**, com o rótulo "Ver na Shopee" do lado. **Pior que o cartão**, que ao
   menos sumia;
3. a **`Offer` do JSON-LD** saía com `"url": ""` — dado estruturado inválido que olho humano não vê.

**POR QUE NADA VIU, e é a 32.5-d inteira:** os 21 anúncios da vitrine têm ficha, **21 de 21**. O ramo
**não existe** no dado publicado, e régua que lê o dado publicado aprova o mundo que existe. A saída é a
que a ohmetria escreveu: **só a mutação que PRODUZ o mundo o enxerga.**

### O CONSERTO É MECANISMO, NÃO INTENÇÃO

A escada virou **uma função da casca** — `rodametria_casca_escada_de_compra()` — e **todo chamador entrega
os dois links crus**. A F2 **parou de escolher**, então a regra deixou de existir em dois lugares onde
podia divergir: a **32.5-c** desta fábrica nasceu exatamente da metade que não viajou.

**E O DEGRAU SOBE COM A BUSCA**, que é a metade que mente se ficar para trás: o rótulo sai de
`rodametria_casca_rotulo_da_loja()`, e botão que abre **página de busca** dizendo "Ver na Shopee" promete
uma ficha que não existe mais. Medido no ar depois do desembarque: o bloco de compra da F2 serve
**degraus [1, 4]** — os itens do mundo B passam pela escada nova **em produção**.

**A TABELA GANHOU A LINHA DISCRETA DO PISO** que devia desde que nasceu, e ela sai **UMA VEZ** embaixo da
tabela, **não por linha**: o piso é da **CONSULTA** e não do anúncio — medido, **uma `url_busca` distinta
por página** nas duas —, e repeti-la seria o mesmo link **dezesseis vezes**. Com duas buscas distintas a
linha **não sai**, porque "a primeira" é arbitrária, e o portão reprova esse caso em vez de o maquiar.

**NO JSON-LD, `availability: InStock` deixa de sair quando o piso sobe:** afirmar estoque sobre um
**resultado de busca** é afirmar o que ninguém mediu.

### O PORTÃO, E ELE É PHP PORQUE A ESCOLHA É DECIDIDA EM PHP

`ferramentas/teste-escada-de-compra.php`, **138 afirmações e 0 falha**. Ele **CHAMA** a função em vez de
ler o arquivo — régua em Python sobre o texto do PHP conferiria a FORMA. Ele **FABRICA** os mundos que o
dado não tem (ficha morta com piso, ficha sem piso, nenhum dos dois, chave **ausente**, `url` **nula**,
ficha **só de espaço**), e **prova que morde** reproduzindo a escada velha dentro da própria bateria.

**E ELE COBRA A PROMESSA QUE EU ESCREVI NO COMENTÁRIO DA F2**, porque afirmação em comentário é número
digitado em outro traje (32.5-d): a regra velha do chamador é reproduzida e comparada item a item com a
escada, no dado publicado — **10 itens da F2, 4 deles já no mundo B, idênticos**. A F2 é o único lugar
desta ilha onde o mundo B **já existe**.

**TRÊS MUTAÇÕES NO CÓDIGO DE VERDADE, as três reprovadas:** a busca que não sobe (**13 falhas**), o degrau
que fica para trás (**6**), a linha do piso por linha (**2**).

### E AS PÁGINAS DE VITRINE NÃO TINHAM PORTÃO DE AR NENHUM — E É NELAS QUE EU MEXI

`conferir-no-ar.py` confere a casca e a F2; `conferir-institucional-no-ar.py` confere as quatro do 5d.
`/veiculos/` e as filhas **não tinham ninguém lendo o HTML servido** desde que nasceram em 29/10: o que as
media era o portão de **pixel** da 32.5 e o `mutacoes-produto.py`, que roda **sem rede** sobre o gerador.
**Entre os dois faltava quem lesse a página.**

`ferramentas/conferir-produto-no-ar.py`, **191 afirmações**, descobrindo as URLs no `wp-sitemap.xml` lido
no ar (32.5-b: *"régua que não varre todas certifica a página que o autor abriu"*). **Rodado contra a
revisão 23, a que estava no ar: 2 falhas, e as duas eram exatamente a linha do piso que estava subindo.**
O portão **reprovou o mundo de antes do desembarque** — e é o que o faz valer depois.

**E ELE ACHOU TRÊS COISAS, as três do lado da RÉGUA, as três pagas antes de aprovar nada:**

1. **A linha do piso se conta pela CLASSE, nunca pela frase.** A **mesma** frase é a linha discreta de cada
   cartão do carrossel (25.2), **5× numa página sã**. Contar a frase é medir duas coisas com a mesma régua.
2. **`&quot;`** — um título tem `10"`, e sem `unescape` a régua reprova a página **certa**. Mesma pedra em
   que o portão institucional bateu.
3. **O WORDPRESS TEXTURIZA O HÍFEN, e isto vale registro.** O `wptexturize` do `the_content` troca hífen
   **cercado de espaços** por **EN DASH** no retorno do shortcode: o dado diz `550W - 40km/h` e o corpo
   serve `550W &#8211; 40km/h`. O **JSON-LD sai no `wp_head`**, não passa por aquele filtro, e serve o
   hífen cru — **o mesmo nome em duas formas na mesma página**. Não é defeito a consertar: é tipografia do
   WordPress, e brigar com ela custa mais do que vale. É a cicatriz que esta ilha já tem escrita no topo da
   casca (*"o WordPress troca `&&` por `&#038;&#038;` no retorno do shortcode"*) **num traje novo** — e
   quem não a souber escreve uma régua que reprova a página certa. Agora está na régua, com a medição.
   (Espaço duplo também: dois títulos da vitrine o trazem da loja, e normalizar **um lado só** reprova a
   página certa. As três normalizações moram numa função, com a cicatriz de cada uma ao lado.)

### O ACHADO FORA DO ESCOPO, CORRIGIDO COMO PROSA E NÃO COMO MECANISMO

O comentário da vitrine afirmava que *"`atualizar-manifest.py` casa esta constante com o campo `versao` do
manifest"*. **Não casa, e nunca casou:** a palavra `versao` **não aparece uma vez** naquela ferramenta
(ela espelha `sha256` e sobe a revisão, e só) e os itens de `snippets` do `manifest.json` **não têm o
campo** — conferido nos quatro. **`RODAMETRIA_PRODUTO_VERSAO` e `RODAMETRIA_F2_VERSAO` são lidas por
NINGUÉM**; só a da casca é viva, porque é o gatilho de reinstalação dela.

É a família do `height:44px` morto que a 32.5-d registra: **comentário que declara um mecanismo parece
conferido e não mede nada.** O que saiu foi a frase que prometia um portão inexistente. **Não mexi no
esquema do `manifest.json` na mesma passada que desembarca**, e a razão é de risco e não de preguiça:
aquele arquivo é o contrato do Sync, e o Sync é o **único** canal de desembarque desta ilha. Fazer o campo
existir é bloco, e está pré-registrado abaixo.

### O DESEMBARQUE, E A 20.6 OUTRA VEZ

Push às 19h29Z, **revisão 27**. O `/status` respondeu **23** com `ultimo: 19:17:02` — **recente e anterior
ao push**, que pela régua de leitura escrita ontem na 20.6 é **turno de cron**, nem defeito nem cache.
`raw.githubusercontent.com` já servia 27 na mesma passada. Mantive as visitas de pé (o cron desta ilha roda
por **visita**) e a revisão entrou às **19h41:02Z**, no turno seguinte. **As 7 linhas da revisão 27 no log
dizem `ok`, lidas uma por uma** (20.4): os quatro itens de dados e os três snippets.

### MEDIDO NO AR (18.4)

- **`conferir-produto-no-ar.py`: 191 afirmações, 0 falha.** De `piso da tabela 0x` (revisão 23) para
  **`1x`** nas duas páginas, `0 href vazio`, 21 de 21 anúncios nomeados e com saída, 21 `Offer`s com url e
  `availability` em 21 — que é o número certo, porque **21 de 21 têm ficha hoje**.
- **`conferir-no-ar.py` (casca + F2): APROVADO.** Bloco de compra da F2 com **degraus [1, 4]**.
- **`conferir-institucional-no-ar.py`: 210 afirmações, 0 falha.**
- **32.5 a 390 px num navegador de verdade: 8 de 8 APROVADAS, e o primeiro botão de compra é IDÊNTICO ao de
  antes** — `/veiculos/bicicleta-eletrica/` **1084 px**, `/veiculos/patinete-eletrico/` **1129 px**,
  `/autonomia-patinete-eletrico/` **1380 px**. A altura das duas vitrines subiu **39 px** (3774→3813 e
  6383→6422): é a linha do piso, embaixo da tabela, longe da primeira tela. **A altura da F2 não mudou um
  pixel** (5196 px), que é a prova independente de que ela não mudou um byte.
- **Bancada: 21 portões com rede, 0 falha** (eram 20 — ela **descobriu** o portão novo sozinha).

### O PRÓXIMO PASSO DESBLOQUEADO, e são três, em ordem de valor

1. **`/veiculos/` ESTÁ FORA DO MOLDE, e o portão de pixel o diz com essas palavras** — *"sem componente de
   molde nenhum"*, nas duas passadas de hoje. A mãe serve `<p class="rdm-promessa">` onde o molde pede a
   **caixa de resposta**, então os **700 px da 32.5 nunca a julgaram**. É **exatamente** a lacuna que o
   bloco 5d fechou na home (a home era HUB e caía em "fora do molde"), uma página depois — a **32.5-c** em
   estado puro: família nova entra no molde **pelo seletor**, nunca pela intenção. É bloco, não conserto:
   a página não está quebrada, ela é **não medida**.
2. **O CAMPO `versao` NO `manifest.json`**, que faria a constante de versão de cada snippet ser **espelhada
   e impressa** como o `sha256` já é — fechando o buraco de duas constantes que ninguém lê. Mexe no
   contrato do Sync, então é bloco com desembarque próprio, nunca carona.
3. **A FILA NORMAL** segue no bloco **4** (ferramentas) com a **F1 e a F3 travadas por ABERTURA e não por
   coleta** — o `gov.br` para o limiar legal da F1 e o nível 5 (`casasbahia`, `extra`, `magazineluiza`)
   para `carga_max_kg` da F3, os dois despacho **ALTA** em `dados/despachos.md`, remedidos em 29/10.

**E A ROBOMETRIA SEGUE FORA DO AR**, remedida nesta passada: home em 200, os três endpoints em 404. Não é
consertável do repositório.

## 2026-10-30 16h38Z–18h1xZ — **O DESPACHO DA RONDA SAIU INTEIRO (18.2): OS CINCO ITENS ACIONÁVEIS**, e os dois defeitos que apareceram no caminho são da mesma família do item 1 — a página se desdizendo

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. **A exceção que fura o foco foi conferida e NÃO furou:** a
**robometria** está com despacho **ALTA** e está *"no ar e quebrada"*, o que pela 1.2 e pela 18.1 teria
precedência — mas o próprio despacho dela diz, com todas as letras, que o conserto **não é do
repositório**: a reescrita do `.htaccess` da raiz é painel do WordPress ou Gerenciador de Arquivos do
cPanel, e o gesto está na lista do Raphael. **Remedi antes de respeitar o herdado (seção 4):** três
passadas com quebra de cache, `robometria.com.br/` em **200** nas três e `/robots.txt`,
`/wp-sitemap.xml` e `/qual-peca-serve-no-meu-robo-aspirador/` em **404** nas três, com
`rodametria.com.br` e `aquametria.com.br` em 200 nas **mesmas** três. Segue caída, segue não
consertável daqui. `executando_desde` estava `null`, que pela **1.1** já significa que não havia bloco
da Fundação vivo — o último commit na pasta era da **ronda** das 15h10Z, e commit de ronda **não
reserva nada** (1.1). Reserva escrita às **16h38Z**, push aceito **de primeira**, campo **reescrito às
16h58Z** pela mesma execução. Branch `claude/*` e `main` idênticos nos dois sentidos, nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 nas mesmas três.

**POR QUE O DESPACHO E NÃO UM BLOCO: a 18.5 é textual** — *"na dúvida entre fechar um despacho e começar
um bloco novo, fecha o despacho. Ilha com defeito no ar não recebe página nova."*

### ITEM 1 — A FRASE DA F2 NEGAVA O NÚMERO QUE ELA MESMA ACABAVA DE SERVIR

O molde `km_degradado` dizia *"conte com {piso} a {teto} km, e não os {teto} km do anúncio"* — e `{teto}`
**é** a autonomia declarada. Com `60/26/110/ladeira/80` a caixa servia "34 a 80 km" e, logo abaixo, "não
os 80 km do anúncio": o topo da faixa que ela mesma publicou.

**A RONDA OFERECEU DUAS SAÍDAS DEFENSÁVEIS E A ESCOLHIDA FOI A SEGUNDA**, com o motivo: mexer no **topo
da faixa** exigiria um número que **ninguém mediu**. A `faixa_de_km()` deriva o piso de `declarada /
fator` — o fator vem do estudo de Quito, que é fonte — e **não existe fonte para um teto que não seja a
própria declarada**. Inventar o topo para salvar a frase seria a seção 10 ao contrário. Então a frase
passou a dizer do número do anúncio **o mesmo que o `km_plano` já dizia dele**: que ele é **teto**, o
melhor caso. E a frase aponta a ponta da faixa que a pessoa deve esperar, que é o que ela veio saber.

### ITEM 2 — O CAMPO "SEU PESO" NÃO MUDAVA NADA, E A ILHA PROMETIA QUE MUDAVA

**ESTE ITEM FOI FECHADO DUAS VEZES, E A PRIMEIRA ESTAVA ERRADA — a correção dela está nesta mesma
execução, e o que a desmentiu foi um número.** A ronda deu duas saídas defensáveis; comecei pela
**primeira** (a caixa de resultado passar a dizer algo sobre o peso informado), e ela foi ao ar na
**revisão 20**. As frases `peso`, `peso_ladeira` e `peso_acima_do_teto` **já existiam** na regra, já
eram acentuadas e **já diferenciavam 50 de 150** — o tradutor as servia abaixo do bloco de compra —,
então subir uma versão curta delas para a caixa parecia o conserto mais barato.

**NÃO CABE. MEDIDO EM NAVEGADOR DE VERDADE, A 390 PX, URL NO AR:**

| o que está na caixa | primeiro botão de compra | teto da 32.5 |
|---|---|---|
| revisão 19 (como a ronda encontrou) | **1.380 px** | 1.400 |
| revisão 20 (a primeira saída, como foi ao ar) | **1.504 px** | 1.400 |
| idem, com as frases enxutas | 1.477 px | 1.400 |
| + a frase de promessa encurtada | 1.454 px | 1.400 |
| + a frase de abertura do bloco de compra encurtada | 1.434 px | 1.400 |
| a frase do peso **dentro** do parágrafo do km | 1.411 px | 1.400 |

**Nenhuma combinação cabe**, e a causa é que **o custo não é de linha, é de BLOCO**: a frase de 46
caracteres e a de 81 deram **o mesmo número** (97 px de acréscimo), porque o que pesa é o parágrafo.
A página já estava a **98,6% do teto** antes de o despacho existir — e o portão da ordem da 32.1, em
`teste-f2.py`, **já registrava** que "a caixa com as cinco frases longas" empurrava o botão para baixo
do teto. Uma passada anterior já tinha pagado essa conta; eu paguei de novo, e de novo só o navegador
disse. **A simulação previu 1.504 px e o portão da 32.5, rodado contra a revisão 20 no ar, leu
1.504 px** — mesmo número, o que é a prova de que a medição por injeção no DOM serve para decidir
ANTES de empurrar.

**ENTÃO O ITEM FECHA PELA SEGUNDA SAÍDA: O PESO SAI DA PROMESSA.** E ela não é consolo — é a mais
honesta das duas. A F2 deriva o piso de `declarada / fator`, e `fator` é **relevo**: nenhum quilo de
quem pilota entra em fórmula, porque `consumo-absoluto-wh-por-km-patinete` está `pendente` e a seção
10 proíbe. A ilha prometia o peso em cinco lugares e passou a prometer o **relevo**, que ela desconta
de verdade, com a fonte do fator citada na própria página:

- a pergunta da home: *"Faz quantos km de verdade com o seu peso?"* → **"na sua ladeira?"**
- o cartão da F2 na home: o mesmo — e **o corpo dele já dizia a verdade** ("com o relevo do seu
  trajeto descontando o que tem de descontar"); só o título prometia o peso
- as duas meta descriptions (que são também o item 5)
- **três textos das páginas de produto** que diziam que a calculadora *"faz essa conta"* com o peso
- o `VOZ.md`, com a data e o motivo escritos ao lado da pergunta trocada, porque ele é o documento
  que descreve a voz aprovada e mudar a tela sem mudá-lo deixaria os dois discordando

**O PESO CONTINUA EM DOIS LUGARES, e nos dois ele é legítimo.** A **terceira** pergunta da home —
*"Aguenta você e a mochila?"* — é a **F3**, onde peso é **carga** e se compara contra o `carga_max_kg`
de cada veículo: ali ele entra de verdade. E a **ressalva abaixo do bloco de compra**, que nomeia o
peso informado e diferencia 50 de 150 — é ela que faz o campo "Seu peso" **não ser enfeite**, e o
portão novo cobra exatamente isso. O FAQ segue explicando, com todas as letras, que a Rodametria não
converte peso em km.

### ITEM 3 — O PREÇO ERA DE UMA LOJA E O BOTÃO IA PARA OUTRA

**Não é a escolha da loja que estava errada.** A regra de dinheiro desta ilha manda preferir o link da
Shopee, e a cotação do Mercado Livre é a **única com procedência e data** que o `x13-chopper-1000w` e o
`ls-sport-scooter-1000w` têm — confirmado no banco. Era a **frase**: o leitor recebia um preço com
procedência e um botão que não serve aquele preço.

Agora, quando as duas lojas divergem, a nota diz **onde o preço foi lido** e **para onde o botão vai**;
quando são a mesma, ela é a de sempre. O nome da loja saiu de dentro do rótulo do botão para
`rodametria_casca_nome_da_loja()`, porque a partir de hoje **dois** lugares o perguntam — mapeamento
escrito duas vezes é mapeamento que envelhece pela metade no dia em que entrar o terceiro programa.
**A nota continua curta de propósito:** ela nasce ACIMA do botão dentro do cartão.

### ITEM 4 — AS 21 OFERTAS DA VITRINE ERAM INTESTÁVEIS E SEM PISO

**Os três campos do par da 25.4-b não foram colhidos nesta passada: eles já estavam no repositório.**
`dados/anuncios-por-consulta.json` guarda `url_produto`, `shop_id` e `item_id` de **40 de 40** anúncios,
colhidos **na mesma chamada da API** que devolveu `url_afiliado` — então a 25.4-b.1 está atendida sem
remendo, porque os dois lados do par são da mesma oferta, da mesma leitura. Eles só não chegavam até a
tela, e foi por isso que a ronda conseguiu testar 9 das 21 lendo o par no arquivo de anúncios.

**O piso da 25.2 foi a única parte que precisou de rede**, e ele é **um por consulta**, com o motivo
escrito: a chave que achou **todos** os anúncios de uma página é uma só (`chave_escolhida`), e é ela que
a 25.2 pode oferecer como saída honesta. Título de marketplace não é marca mais modelo, e busca por
título inteiro devolve menos que a chave medida. Nasceu `coletar-piso-da-vitrine.py` — **fora** do
gerador de propósito, porque `gerar-vitrine-de-produto.py` roda na bancada **sem rede** e gerador que
depende de rede não se reconfere. Os dois encurtados foram medidos **VIVOS** (301 no encurtador).

**21 de 21 itens servidos com os quatro campos**, e o piso já é **servido** nos cartões sem tocar no
snippet: a escada da casca imprime a linha discreta "Veja todos disponíveis aqui" quando `url_busca`
existe — o mecanismo da 25.2 funcionando como foi desenhado.

### ITEM 5 — DUAS META DESCRIPTIONS PASSAVAM DE 160, E O PORTÃO TOLERAVA 200

161 → **147** na home e 193 → **155** na F2, contados. **E o defeito de fundo era o portão:** ele
aprovava até 200, então as duas passaram com ele verde, e a ronda as achou a olho. Teto em **160** nele
e no espelho offline (`teste-institucional.py`, cujo texto de falha já dizia ser espelho do de ar).
**E as entidades HTML passam a ser desfeitas ANTES de contar:** o atributo vem escapado do `esc_attr`,
então um apóstrofo chegaria como `&#039;` e contaria **6** caracteres no lugar de 1 — a família do
`&#038;` que a própria seção 12 cobra dentro de `<script>`.

### E DOIS DEFEITOS QUE NÃO ESTAVAM NO DESPACHO, achados ao escrever os itens acima

1. **`peso_ladeira` mandava "esperar o PISO da faixa" também quando a caixa havia RECUSADO o km.** Com
   ladeira e sem autonomia declarada, a caixa dizia *"não dá para dizer quantos km esta bateria faz"* e a
   ressalva, logo abaixo, mandava esperar o piso **de uma faixa que a página acabara de se recusar a
   dar**. É a **mesma família do item 1**, um andar abaixo. Agora ela só nasce onde existe faixa com duas
   pontas, e a guarda está escrita nas duas metades (regra e navegador).
2. **A frase de peso acima do teto dizia "veja se o modelo AGUARDA o seu peso".** Texto de tela, e a
   palavra desta ilha — a do `VOZ.md` — é **aguenta**. Ela não está na página de exemplo (o exemplo tem
   110 kg e o teto é 120), mas viaja no arquivo publicado e o navegador a imprime.

### OS PORTÕES QUE NASCERAM COM O FECHO — e os três MORDEM, provado por mutação

- **`teste-f2.py`** ganhou as réguas dos itens 1 e 2, e **as duas se provam antes de julgar**: o
  primeiro caso de cada uma exige que ela **REPROVE o texto que estava no ar**, senão é portão
  **inerte** — a cicatriz que a bancada desta família já nomeia com essa palavra. A do item 2 **mudou
  de alvo** junto com a decisão: ela cobra a **ausência da promessa**, não a presença da frase, mais a
  ressalva **nomeando o peso informado**. **E ela nasceu com um defeito que a própria bateria achou:**
  a primeira versão varria TODO literal dos dois snippets e reprovou **três textos do FAQ** —
  inclusive a resposta que diz *"a Rodametria não converte peso em km"*, que é exatamente o que a ilha
  deve ao leitor depois de tirar o peso da promessa. **Explicação não é promessa.** Agora ela julga
  **21** textos nos slots que prometem (`description`, `titulo`, `<h1>`, a frase de promessa e os
  títulos dos cartões) e **exige um piso de 8 textos julgados**, para não aprovar por cegueira.
  Mutações, todas reprovando: a pergunta da home voltando a prometer o peso; a description voltando; a
  ressalva parando de nomear o peso; o molde do item 1 voltando a negar o topo. **E o portão pegou,
  sozinho, um erro meu que nenhuma leitura pegaria:** ao desfazer a primeira saída eu removi o molde
  `peso_caixa` do arquivo publicado e **deixei o JS citando-o** — a página teria impresso `{piso}` na
  cara de quem lê.
- **`teste-nota-de-preco.php`** — **PHP porque a frase é decidida em PHP**. Uma régua em Python sobre o
  texto do arquivo conferiria a FORMA; esta **chama a função** e lê o que o leitor recebe. Julga quatro
  mundos (loja igual, o defeito, o **espelho** do defeito, e cartão sem botão) **mais os cartões reais do
  arquivo publicado**. Mutação: a nota voltando à forma antiga → **4 reprovações**, duas delas nomeando
  o X13 e o LS Sport. E a bateria achou um furo na **minha** régua: cartão sem botão não tem destino para
  prometer, e ele nem chega à tela — o ramo nasceu com o caso que o provou.
- **`validar-banco.py` passa a CONTAR A VITRINE**, que é o buraco que o despacho nomeia. A régua não
  mudou; mudou o que ela alcança. Mutação: a vitrine de volta ao estado de ontem → **21 intestáveis, 0
  com piso**, com uma falha por item. Era o estado em que o portão podia escrever "intestáveis: ZERO"
  com verdade sobre o banco que lia e falso sobre um terço dos links que a ilha servia.

**O ITEM 6 NÃO FOI TOCADO, e está certo assim:** ele não é conserto. É a receita do anti-robô da Shopee
(teto de chamadas na janela, não intervalo) e mora onde a próxima ronda vai procurá-la.

### O QUE FICA PARA QUEM VIER, e nada disto é deste despacho

1. **A ressalva do peso termina apontando para frente, e no caso `misto` não há nada depois dela.** O
   molde diz *"Eles entram aqui, no que esperar da faixa"* — e com `ladeira` a frase seguinte entrega
   (*"espere o PISO da faixa, não o meio dela"*), mas com `misto` ou `plano` a ressalva fica sozinha
   prometendo um "aqui" que não vem. É a mesma família do item 2, uma oitava abaixo, e é **anterior a
   esta execução**. Não mexi: o item 2 foi fechado e verificado, e alargar despacho é o que a 18.2
   proíbe. Fica nomeado para a ronda decidir.
2. **Na vitrine, a escada da casca ESCONDE o cartão quando `url` está vazia**, em vez de cair na busca
   como a `rodametria_f2_itens_da_vitrine()` faz. Hoje os 21 têm ficha, então o ramo não existe; no dia
   em que uma morrer, o piso está no dado e a tela não o promove sozinha. **A tabela de 16 linhas
   também serve só a ficha**, sem a linha discreta da busca. Os dois são **bloco, não conserto**.
3. **A robometria segue FORA DO AR com despacho ALTA**, remedida nesta passada em três leituras com
   quebra de cache. Não é consertável do repositório: a reescrita do `.htaccess` da raiz é cPanel, e o
   gesto é do Raphael.

### O FECHO, CONFERIDO NO AR PELA 18.4

**Revisão 23**, com as linhas da revisão corrente do log dizendo `ok` (20.4, lidas uma por uma).

- **32.5: APROVADO em 1.380 px**, que é exatamente onde a ronda encontrou o botão — 8 de 8 páginas do
  molde dentro, pior caixa em 331 px contra o teto de 700.
- **`conferir-no-ar.py`: APROVADO**, e com o teto novo: as **nove** URLs com description entre **131 e
  159** caracteres, contra as de 161 e 193 que a ronda achou.
- **`conferir-institucional-no-ar.py`: 210 afirmações, 0 falha.**
- **Bancada com rede: 19 portões, 0 falha** (eram 17 antes desta execução).
- **Item 1 no ar:** a caixa serve *"os 60 do anúncio são o teto"*, e a oração proibida tem **zero**
  ocorrências na página.
- **Item 2 no ar:** **zero** ocorrências de "com o seu peso" na home e na F2, e a ressalva abaixo do
  bloco de compra segue nomeando os 90 kg da entrada.
- **Item 3 no ar:** os cartões do X13 e do LS Sport servem *"lido na Mercado Livre em 27/10/2026 — o
  botão abre a Shopee"*; os dois de loja igual seguem com a nota de sempre.
- **Item 4 no ar:** **5 de 5** cartões em cada página de produto servem a linha discreta do piso, e cada
  página serve a busca da **sua** consulta.

**TRÊS TURNOS DE CRON, e é a causa do bloco longo — não foi trabalho.** O Sync desta ilha roda por
visita (20.6), mas **visita não antecipa evento que ainda não venceu**: cada revisão esperou o seu turno
de 30 minutos (20 às 17h10, 22 às 17h39, 23 às 18h10), e cada conferência da 18.4 precisa da revisão
**pousada**. A reserva foi renovada três vezes pela 1.1.


## 2026-10-30 13h5xZ–14h4xZ — **BLOCO 5d: AS QUATRO PÁGINAS QUE O SITE DEVIA A QUEM LÊ** — e a de privacidade não promete nada: tudo o que ela afirma foi **medido na página servida**, inclusive o que era mais fácil de esconder

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi antes as duas exceções que furam o foco: (a) o
**despacho do molde da 32.6** está `FECHADO` nas três ilhas que a 32.6 nomeia — lido no topo dos três
`PROMPT.md`, com hora de fecho em cada um; (b) nenhum despacho **ALTA** é de ilha *"no ar e quebrada"*.
`executando_desde` estava `null`, que pela **1.1** já significa que não havia bloco da Fundação vivo —
reserva escrita às **13h54Z** (commit `a860712`), push aceito **de primeira**, campo **reescrito às
14h11Z** pela mesma execução. `git log` entre `origin/main` e `origin/claude/dreamy-mccarthy-4smb5m`
veio **vazio nos dois sentidos** e a listagem de PRs devolveu **zero aberto** — nada a mergear.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 nas mesmas três, e o `/status` em 200 na **revisão 17**, a que o 5c deixou.

**POR QUE O 5d.** O próprio `PROMPT.md` já o declarava *"o próximo bloco, e ele não espera ninguém"*,
com as três razões escritas: não depende de despacho nenhum, fica fora do teto da 21.4 pela **21.7**, e
é dívida de confiança no ar. A dívida estava medida desde a contagem de sitemap de 30/10 às 10h3xZ: **a
ilha serve link de afiliado da Shopee desde 29/10** e não tinha `/divulgacao-de-afiliados/` nem
`/privacidade/`.

---

### 1. O QUE FOI AO AR

**Quatro URLs, e a casca não foi tocada.** `/sobre/` (#21), `/contato/` (#22),
`/divulgacao-de-afiliados/` (#23) e `/privacidade/` (#24), pelo snippet `rodametria-institucional`
**1.0.0** (#9 no Code Snippets). Elas entraram pelos filtros `rodametria_paginas` e
`rodametria_instalar`, de dentro do próprio snippet delas — que é a promessa que a casca faz desde a
revisão 3 dela, *"a casca não é editada quando a ilha cresce"* —, e a instalação rodou porque a
**assinatura do mapa** mudou, que é exatamente o que a casca **1.4.0** nasceu para fazer em 29/10.
Zero linha de casca neste bloco, e portanto zero risco no arquivo que pinta todas as páginas.

**A instalação aconteceu na requisição SEGUINTE à do Sync, e isso é o mecanismo funcionando.** O log
diz `snippets/rodametria-institucional: ok (snippet #9 criado)` às 14h40, e o relato de instalação da
casca é de **14h41:38** — porque quando o `init` chamou a instalação às 14h40 o snippet ainda não
estava carregado naquela requisição. Era exatamente o defeito de 29/10 que custou as três páginas do
5b; com a assinatura no lugar da versão, a passada seguinte criou as quatro sem ninguém tocar em nada.

`pai` **nulo** nas quatro, pela **16.1** ao pé da letra (*"sem página solta na raiz além de home,
sobre, contato, divulgação de afiliados e privacidade"*) — e `garantir_pagina()` aceita pai zero
exatamente por elas. `no_menu` **true**: o `VOZ.md` manda um menu curto de assunto, e página
institucional no menu de cima rouba o lugar do que a pessoa veio procurar. Elas aparecem no **rodapé**,
que a casca monta do mapa inteiro e serve em toda página — e isso fechou a **16.4(f)** com folga:
medido no ar, cada uma das quatro **recebe link de 9 das 9 páginas no ar**, contra as 2 que a regra pede.

### 2. O DESEMBARQUE, PELA 20.4 E PELA 20.6

Revisão **19** no `/status`, com as **cinco** linhas da revisão corrente lidas **uma por uma** e todas
dizendo `ok`. O portão de ar também as leu e registrou: *"15 linha(s) na janela, 1 da revisão 19, 0
linha de falha nesta entrega"*.

**E a 20.6 foi medida de novo, com um achado que ela não tinha.** A 20.6 diz que o cron roda **por
visita** e não por relógio, e isso continua verdadeiro — mas ela não diz o que acontece quando o evento
**não está vencido**. Empurrei a revisão 18 às 14h11Z e o `/status` ficou em 17 por meia hora, com
`ultimo: 14:10:04` — ou seja: o Sync **havia rodado** às 14h10, um minuto antes do meu push, e o
`rodametria_30min` só vencia às ~14h40. Visitar a home e bater no `wp-cron.php` (que respondeu **409**,
prova de cron em andamento) **não antecipou nada**, e não devia: o WP-Cron dispara evento **vencido**,
não evento futuro. A revisão entrou às **14h40:39**, pontualmente no turno.

**A régua que isto acrescenta, e ela é de leitura e não de conserto:** o campo `ultimo` do `/status`
separa os três mundos que a 20.5 junta em dois. `ultimo` **antigo** = o Sync não rodou (defeito).
`ultimo` **de agora** com revisão atrasada = cache do GitHub (reacione). `ultimo` **recente mas
anterior ao push** = nem defeito nem cache: é **turno de cron**, e o que resolve é esperar o próximo
mantendo as visitas de pé para ele disparar. Gastei uma rodada de reação achando que era cache, até ler
o `ultimo` e ver que ele era mais velho que o meu próprio push.

### 3. A PÁGINA DE PRIVACIDADE FOI **MEDIDA** ANTES DE ESCRITA, E É ISSO QUE ELA TEM DE DIFERENTE

Não escrevi uma política de privacidade: medi o que o site faz e escrevi o que medi. As quatro
medições, feitas do lado de fora, como o navegador recebe:

| o que | medido | consequência na página |
|---|---|---|
| `Set-Cookie` | **zero**, nas URLs no ar | a página afirma que o site não escreve cookie nenhum |
| medidor de audiência e pixel | **zero** ocorrência de doze famílias procuradas | a página afirma que não há medidor — e não há GA4 nesta ilha |
| endereços de fora que **carregam** | **dois**: Google (`fonts.googleapis.com` e `fonts.gstatic.com`, em toda página) e Shopee (`cf.shopee.com.br`, onde há foto) | a página **nomeia os dois**, com o que cada um serve |
| endereços que são **só link** | `s.shopee.com.br` e `dspace.ups.edu.ec` | a página diz que link não faz nada até o clique |

**E A MEDIÇÃO ACHOU O QUE ERA MAIS FÁCIL DE ESCONDER, que é a parte de que mais me orgulho neste
bloco.** A primeira versão da página dizia, como toda página de privacidade de calculadora diz, que *"a
conta é feita no seu navegador e o que você digita não sai dele"*. O formulário da F2 é
**`method="get"`** com `action` para a própria URL: se a pessoa aperta o botão, **os números vão para o
endereço da página** e passam pelo servidor junto com o pedido, e ficam no registro de acesso do
hospedeiro. A frase bonita era **falsa na metade que importa**. O que foi ao ar diz as duas coisas
separadas — mexer nos campos não envia um byte; apertar o botão põe os valores na barra do navegador,
de propósito, para o resultado poder ser guardado ou mandado para alguém — e nomeia quais são os
quatro números. **Dizer "nada sai" seria mentir em quatro palavras.**

**A `/contato/` NÃO INVENTOU UM CANAL.** Esta ilha não tem caixa de e-mail, e o despacho de 13/09 em
`dados/despachos.md` — *"o que NÃO se faz enquanto isso: publicar um endereço que ninguém lê"* — é
explícito. A página diz que o canal não existe, diz por que, e entrega no lugar o que de fato serve:
toda afirmação daqui carrega fonte e data, e a seção do fim de cada página nomeia a loja, o anúncio e o
dia da leitura, para conferir **sem intermediário**. O despacho foi reescrito hoje: ele dizia "nenhuma
das **três**" e agora são **quatro**, com o custo novo escrito (uma página chamada "Contato" sem
contato) e com a linha que a Fundação troca no dia em que a caixa existir — **uma linha**, no JSON
declarado, sem tocar em código.

### 4. NENHUM NÚMERO É DIGITADO: 16 MOLDES CONTADOS NA HORA DE SERVIR

A prosa mora em `dados/paginas-institucionais.json` e traz molde no lugar de todo número;
`rdm_inst_numeros()` os conta ao servir, das options que o Sync grava e do mapa de páginas da casca.
Isto não é preciosismo: esta é a família de página que **fala de si mesma** (*"quantos itens têm link",
"quantas páginas no ar"*), que é justamente o caso em que a seção 8 diz que o número digitado passa a
mentir calado.

**As quatro caixas no ar, cada número conferido por uma TERCEIRA CONTA** — recontado em Python, dos
arquivos de dado, por caminho diferente do que o PHP usa, e comparado com o HTML servido:

| página | caixa | no ar | terceira conta |
|---|---|---|---|
| `/sobre/` | veículos no banco | **17** | 17 |
| `/contato/` | anúncios lidos um por um | **40** | 40 |
| `/divulgacao-de-afiliados/` | itens com link de loja | **5** | 5 |
| `/privacidade/` | páginas no ar | **9** | 9 |

A conta de `/privacidade/` é a mais interessante das quatro porque as duas metades leem **fontes
diferentes de verdade**: o PHP conta o **mapa de páginas da casca** e o portão conta o
**`wp-sitemap.xml` servido**. Quando elas discordarem, a divergência é informação e não ruído — URL no
sitemap que o mapa não conhece é página órfã da árvore da 16, e página no mapa que o sitemap não lista
não é indexável.

### 5. TRÊS PORTÕES REPROVARAM A PÁGINA **CERTA** EM DOIS DIAS, E A TERCEIRA VEZ FOI HOJE

Esta é a lição de método do bloco, e ela tem nome no contrato: *"portão que reprova página certa é o
caminho mais curto para alguém passar a ignorá-lo"* (20.5 e 32.5-b, com as mesmas palavras).

1. **30/10, bloco 5c:** `gerar-f2.py --conferir` reprovava a F2 por causa do selo `gerado_em`.
2. **30/10, hoje, `teste-institucional.py`:** a régua que proíbe a folha desta família de redecorar o
   que é da casca procurava a palavra `h1` no texto da folha — e achou **o comentário que explica por
   que ela não mexe em h1**. Consertada para medir **seletor**, com as duas metades provadas no
   autoteste: o comentário que cita `h2` não reprova, e `.rdm-inst-secao h2{}` reprova.
3. **30/10, hoje, `conferir-institucional-no-ar.py`:** disse que dois itens do bloco de recusa de
   `/sobre/` *"não estão no ar"*. Estavam, inteiros e corretos: `esc_html()` transforma a aspa reta em
   `&quot;` e a comparação era contra o texto declarado, com aspa. Consertado com `html.unescape`.

Nas três, a tentação era mexer na página. Nas três, o defeito era da régua.

### 6. E UM PORTÃO NÃO ESTAVA REPROVANDO O QUE DEVIA: A **HOME** ESTAVA FORA DA 32.5 DESDE QUE NASCEU

Achado escrevendo este bloco, e é a **32.5-c** outra vez — *família nova entra no molde pelo seletor,
nunca pela intenção*. `conferir-32-5-no-navegador.mjs` decidia "está no molde" por
`!!(bloco_de_compra || formulario)`. Página com **caixa de resposta e sem nada para vender** caía em
`fora do molde`: a caixa era medida, **impressa** e **nunca julgada** contra os 700 px. A 32.5 diz o
contrário com todas as letras — *"o formulário (ou a caixa de resposta, em ficha) começa antes de 700
px"*: ter caixa já é estar no molde.

**E não era hipotético: a HOME desta ilha é HUB, não tem bloco de compra e não tem formulário.** Ela
estava fora do veredito desde 29/10. Medida agora, passa com folga — mas passar por medição e passar
por omissão são coisas diferentes, e só a primeira avisa quando mudar. As quatro páginas de hoje
entrariam pela mesma porta: seriam **quatro** páginas de molde que o portão abria e deixava passar.

O teto de **compra** passou a ser julgado só onde há o que comprar, e onde não há o portão **imprime**
"não se aplica (a página não vende nada)" em vez de pular calado — com a outra metade cobrada: página
que serve link patrocinado **fora** de um bloco de compra é **reprovada**, porque sem o componente o
teto não teria o que medir. Sem isso a isenção viraria a porta dos fundos dos 1.400 px.

### 7. MEDIDO NO AR — os números, e nenhum deles é a conta de antes do desembarque

**32.5, a 390 px num Chromium de verdade, com quebra de cache** (`conferir-32-5-no-navegador.mjs`,
descobrindo as URLs no sitemap): **8 de 8 páginas do molde aprovadas**, de 3 antes do conserto.

| página | caixa de resposta | compra | altura |
|---|---|---|---|
| `/sobre/` | **211 px** | não se aplica | 3.769 px |
| `/contato/` | **244 px** | não se aplica | 3.372 px |
| `/divulgacao-de-afiliados/` | **244 px** | não se aplica | 3.946 px |
| `/privacidade/` | **244 px** | não se aplica | 5.092 px |

Teto da caixa: 700 px. Pior caixa da ilha inteira: 331 px (a home). `/veiculos/` segue **fora do
molde**, e agora com o motivo exato impresso: não tem componente de molde nenhum.

**O piso de 1.500 caracteres da seção 8, MEDIDO NO AR** e não pela conta feita antes de desembarcar —
que é o erro que a mãe `/veiculos/` quase pagou em 29/10, quando a conta de antes dava 1.253 e a página
no ar passou: `/sobre/` **4.449** · `/contato/` **3.674** · `/divulgacao-de-afiliados/` **4.786** ·
`/privacidade/` **5.899**.

**Bancada com rede: 17 portões, 0 falha, APROVADO.** `conferir-no-ar.py` 445 afirmações / 0 falha nas
**9** URLs; `conferir-institucional-no-ar.py` **210** afirmações / 0 falha;
`conferir-32-5-no-navegador.mjs` 8 de 8. Sem rede: 14 portões, 0 falha, com os **19 casos de autoteste**
do portão novo, que **fabricam** o mundo de cada regra em vez de esperar que o dado o produza — dígito
plantado na prosa, molde órfão, promessa escondida dentro do bloco de recusa, negação no meio da frase,
número literal na caixa, página fina.

### 8. O QUE ESTE BLOCO NÃO FEZ, dito em vez de deixar implícito

- **A `/contato/` não tem canal**, e isso é do Raphael. Está no despacho, agora com quatro ilhas.
- **A ilha segue com `piso: abaixo`:** 9 URLs contra as 40 da 21.1. As quatro de hoje **não contam para
  o piso de malha** — a 21.7 as tira do teto justamente porque nenhuma responde a uma busca.
- **O teto de levas da 21.4 não foi gasto:** pela 21.7 estas quatro não são leva.
- **O soft 404 da borda do hospedeiro** segue sendo despacho ALTA e não se conserta daqui.

**PRÓXIMO PASSO DESBLOQUEADO.** A fila não tem mais nada que seja ao mesmo tempo grande e livre: a
**F1** depende do `gov.br` (despacho ALTA), a **F3** depende de `carga_max_kg` em registro com oferta,
as duas consultas que sobraram da cauda dependem de uma sessão de Chrome (despacho de 30/10, no topo do
`PROMPT.md`), e `scooter`/`moto elétrica` dependem das etiquetas do Mercado Livre. O que **não**
depende de ninguém é o **bloco 4**: a **F3** como REGRA, sem página — o mesmo desenho que a ohmetria
usou para a F1 dela com o banco vazio, e que esta ilha já usou na F2. Ela nasce medindo quantos
registros têm carga máxima declarada e dizendo na própria tela o que falta, em vez de esperar o dado.

## 2026-10-30 10h1xZ–10h4xZ — **BLOCO 5c: A CAUDA DESTE NICHO É TERRITÓRIO DE FAZENDA** — três das cinco consultas fecharam sem precisar do Chrome, e no caminho a bancada acusou um portão que reprovava a página CERTA

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi antes as duas exceções que furam o foco:
(a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas — lido no topo dos três `PROMPT.md`,
com data e hora de fecho em cada um (aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria
21/10 16h1xZ); (b) nenhum despacho **ALTA** é de ilha *"no ar e quebrada"*. `executando_desde` estava
`null`, que pela **1.1** já significa que não havia bloco da Fundação vivo — reserva escrita às
**10h17Z** (commit `392bece`), push aceito de primeira, reescrita às **10h25Z**. O `main` vinha de um
**forced update** (`b793f79` → `3c952f0`); o branch `claude/dreamy-mccarthy-lbibd5` estava **idêntico**
ao `origin/main` (zero commits de diferença nos dois sentidos) e **nenhum PR aberto** — nada a mergear.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 nas mesmas três, e o `/wp-json/rodametria/v1/status` em 200 na **revisão 16**
— a mesma que o 5b deixou, com **todas** as linhas da revisão corrente dizendo `ok` no log (20.4).

---

### 1. O QUE O BLOCO MEDIU, E ELE CORRIGE A PREMISSA DO PRÓPRIO BLOCO

O 5c estava escrito dizendo que *"o caminho mais curto é a cauda medida do corpus"*. Medi as **cinco**
caudas do eixo D com o único instrumento desta nuvem — busca — e colhi **102 ocupantes com URL**.
O placar, contado do próprio arquivo e não digitado:

| consulta | buscas/mês | veredito | por quê |
|---|---|---|---|
| `patinete elétrico adulto` | 49.500 | **tomada** | 6 fazendas com página dedicada (`melhor-patinete-eletrico-adulto`) + categoria dedicada da Casas Bahia |
| `melhor patinete elétrico` | não medido | **tomada** | **12** fazendas com página dedicada, mais o blog da Shopee. A medição mais limpa das cinco |
| `moto elétrica 1000w` | 14.800 | **tomada** | 5 páginas brasileiras dedicadas (4 de fazenda + `consultadeplaca.net`), com o MENOR vazamento das três de potência |
| `patinete elétrico 1000w` | não medido | **nao-medida** | **17 dos 21 ocupantes fora do Brasil**; nenhum dos 4 brasileiros é página dedicada |
| `scooter elétrica 1000w` | 33.100 | **nao-medida** | 13 de 19 fora do Brasil, e o instrumento **derivou** para `autopropelido` |

**O ACHADO, e é de fila e não de página: a cauda deste nicho é território de FAZENDA.** O dossiê
registrou, nas seis cabeças vistas no Chrome do Raphael, que *"nenhuma fazenda da lista apareceu"*. Na
cauda ela aparece em **quatro das cinco**, com **26** páginas dedicadas de fazenda entre os 102
ocupantes — e no formato *"melhor X"* / *"Top 10"* que o `VOZ.md` desta ilha **proíbe nominalmente**.
**A proibição da voz e a medição da SERP coincidem**, e isso não é coincidência: a ilha foi desenhada
para o eixo paramétrico, e a cauda de produto é o campo do concorrente que ela não quer ser. O
`ACHADO D` do corpus de 28/10 já tinha visto a fazenda nas caudas; o que faltava era tirar dele a
conclusão de fila. **A cauda não é o caminho curto desta ilha: é onde ela perderia.**

**ZERO PÁGINA NOVA, E É A 30.8 FUNCIONANDO.** `tomada` fecha a consulta — barato e final, e três
fecharam sem gastar um minuto do Raphael. `nao-medida` não autoriza nada. Vale a frase da seção:
*"errar para o lado de não publicar é barato; errar para o lado de publicar é a leva inteira"*.

**E A 30.4 ESTAVA CUMPRIDA SEM NINGUÉM PLANEJAR.** `/veiculos/patinete-eletrico/` serve a palavra
`adulto` **53 vezes** no HTML no ar (contado às 10h2xZ, com quebra de cache), porque `patinete eletrico
adulto` é o **degrau 1** da escada de chaves daquela página. A intenção da cauda de 49,5 mil já está
atendida por uma URL que existe — abrir uma segunda seria canibalizar a própria mãe. **Não refiz nada
por isso**: o reforço que a 30.4 manda já estava no ar.

**O que foi escrito:** `dados/consultas-de-produto.json` (a fonte: 11 consultas, 6 cabeças + 5 caudas,
com `forma` agora **explícito** em toda linha) e `dados/consultas-de-produto.md` (a vista legível,
**gerada do JSON na mesma passada** para não haver erro de transcrição). O despacho da 30.8 está no
topo do `PROMPT.md`: duas SERPs e um volume, numa sessão de Chrome.

**DOIS RÓTULOS MEUS MENTIRAM E FORAM CONSERTADOS ANTES DE FECHAR**, e registro porque é a família do
número de tela digitado: o placar nasceu com `com_pagina_no_ar: 4`, contando **slug declarado** —
e `veiculos/moto-eletrica` e `veiculos/scooter-eletrica` têm endereço reservado desde o 5b e **não
existem no ar**. O número do ar é **2**, e agora o arquivo traz os dois campos separados com a causa
da diferença escrita. O segundo: `ocupantes_registrados_com_url` somava um total com **duas
procedências diferentes dentro** (as cabeças vêm do dossiê, por domínio e sem URL por ocupante) —
virou `ocupantes_com_url_das_CAUDAS_medidos_em_30_10`, que diz de quem a conta é.

---

### 2. O DEFEITO QUE A BANCADA ACUSOU ANTES DE EU CONSTRUIR (18.5), E ELE É UM PORTÃO REPROVANDO A PÁGINA CERTA

Rodei `ferramentas/bancada.py --no-ar` antes de escrever uma linha, como a 18.5 manda. Ela reprovou:
`gerar-f2.py --conferir` dizia que `dados/f2-respostas.json` estava diferente do que a referência
produz. **A única diferença, medida campo por campo, era o selo `gerado_em`: `2026-10-29` →
`2026-10-30`.**

**A causa:** o gerador escrevia esse campo com o **relógio da execução**
(`datetime.utcnow()`), num arquivo **derivado** cujo conteúdo não depende de data para nada que a F2
calcula. Logo o portão era **irreprodutível por construção** e passava a reprovar **todo dia seguinte**
ao que a F2 fosse gerada. É exatamente o perigo que a **20.5** e a **32.5-b** nomeiam: *"portão que
reprova página certa é o caminho mais curto para alguém passar a ignorá-lo"* — e o perigo maior é
concluir que o portão mente e passar a ignorá-lo de vez.

**A irmã já fazia certo, e a lição não havia viajado — a 32.5-c outra vez.**
`gerar-vitrine-de-produto.py` escreve `'gerado_em': anuncios['gerado_em']`, **herdado do dado**, e por
isso é reprodutível. Os `coletar-*` usam a data de hoje e **estão certos**: ali a data é a da
**medição**, que é procedência e tem de entrar na comparação.

**O conserto:** o selo saiu da comparação — e **só ele** —, com o motivo, a data e a medição escritos
no código, ao lado do que o portão continua cobrando. **As duas metades do veredito foram provadas em
cinco casos**, porque portão que só aprova é inerte:

| caso | esperado | palavra impressa | código de saída |
|---|---|---|---|
| mundo real, selo de ontem | aprovar | APROVADO | 0 |
| só o selo trocado por `1999-01-01` | aprovar | APROVADO | 0 |
| um **número** da tela mexido (`exemplo.tensao_v`) | reprovar | REPROVADO | 1 |
| uma **frase** da tela mexida (`nota`) | reprovar | REPROVADO | 1 |
| arquivo corrompido, não-JSON | reprovar sem explodir | REPROVADO, com o erro nomeado | 1 |

**NÃO REGEREI O ARQUIVO para "consertar" o selo**, e isso é decisão: regerar mudaria `gerado_em` para
30/10 e empurraria uma **revisão nova do Sync sem uma letra de mudança na tela**. O arquivo no ar e o
do repositório seguem com `2026-10-29`, que é a data em que a F2 foi de fato gerada, e é o que a página
diz a quem lê (*"Esta página foi gerada a partir do nosso banco em 29/10/2026"*). Nenhum desembarque
nesta execução, de propósito.

**POR QUE ISTO NÃO VIROU SEÇÃO DO `ARQUIPELAGO.md`, e conferi antes de decidir.** A 20.4 manda a regra
subir ao contrato quando *"o Sync é o mesmo código nas três"*. Aqui o código **não** é compartilhado:
cada ilha tem os geradores dela. Varri as outras cinco e o defeito **não existe lá** — e duas já fazem
certo por caminhos diferentes: `atualizar-manifest.py` da aquametria e da robometria só grava
`atualizado_em` **quando algo mudou de verdade** (`if mudados or titulos or alvo is not None`), e
`medir-palavras-chave.py` da robometria sela a data da **medição**. Pela **31.2** (*"pode acontecer não
basta"*) não há defeito medido fora desta ilha, e a seção **0** do contrato reclama do crescimento dele.
O princípio geral já está escrito na **20.5** e na **32.5-b**. **Se o Raphael discordar, a regra cabe
em três linhas e o lugar é a família da 20.5.**

**O MANIFEST SUBIU PARA A REVISÃO 17, E ISSO NÃO É DESEMBARQUE.** O portão
`atualizar-manifest.py --conferir` reprovou — corretamente — porque `dados/consultas-de-produto.json`
mudou nesta passada; rodei o atualizador e o sha e a revisão acompanharam. **Nada no site muda por
isso:** aquele arquivo é `publicar: false`, e os cinco itens publicáveis seguem com o conteúdo de
29/10. O Sync aplicou a revisão 17 com a mesma tela da 16.

**CONFERIDO NO AR PELA 20.4:** revisão **17** no `/status` às **10h39:48Z**, com as **quatro** linhas
da revisão corrente dizendo `ok`, e `ferramentas/bancada.py --no-ar` aprovando **15 de 15** depois
dela — `conferir-no-ar.py` incluído, que havia reprovado **corretamente** enquanto o manifest local
estava à frente do `/status`.

**E UMA MEDIÇÃO QUE CORRIGE A MINHA PRÓPRIA PREVISÃO, e ela é sobre o cron da 20.6.** Eu escrevi, às
10h39Z, que a tarefa desta ilha venceria *"~10h47"*, somando 30 minutos sobre a passada anterior
(10h17:15). **Ela rodou às 10h39:48 — 22 minutos e 33 segundos depois**, logo após os três GET na
home. Então a leitura de 29/10 (*"o relógio dele não se adianta por GET"*) **não é a história
inteira**: os GET daquela passada não adiantaram nada porque a tarefa ainda não estava vencida; os
desta, sim. **O que está medido, e é só isto:** o intervalo entre duas passadas consecutivas desta
ilha foi de **22,5 minutos**, não 30 — então "30 minutos" é o **nome** do cron (`rodametria_30min`),
não o período medido dele. Quem for prever a hora de um desembarque aqui **visita e confere**, em vez
de somar 30 sobre a última linha do log; a régua da **20.5** continua sendo a certa para decidir se
revisão atrasada é cache ou defeito.

**E ACHEI UM CAMPO MORTO NO CAMINHO, que fica registrado em vez de consertado.** O `manifest.json`
desta ilha traz `atualizado_em: 2026-10-29` e agora diz `revisao: 17` — ou seja, o campo ficou para
trás. Conferi: **nesta ilha ninguém escreve e ninguém lê esse campo** (`grep` em `ferramentas/` e nos
três snippets não acha uma referência); ele veio copiado de ilha irmã no nascimento, e lá ele é escrito
pelo atualizador. É a seção **4** em miniatura — *resumo velho lido como fato* —, e o risco é alguém o
ler um dia como a data da última mudança. **Não mexi na ferramenta de propósito:** a **31.3** proíbe
ampliar portão que já existe enquanto a ilha tiver item de conteúdo aberto na fila, e o 5d está aberto.
Quem pegar o 5d pode resolver em uma linha: ou o atualizador passa a escrever o campo quando bumpa a
revisão (como as irmãs), ou o campo sai do manifest. **As duas são certas; o que não é certo é ele
continuar ali parecendo conferido.**

---

### 3. O PRÓXIMO PASSO DESBLOQUEADO — O BLOCO 5d, E ELE NÃO ESPERA NINGUÉM

Medindo o `wp-sitemap.xml` no ar achei a dívida mais barata e mais atrasada desta ilha: as **5** URLs
publicadas são `/`, `/autonomia-patinete-eletrico/`, `/veiculos/` e as duas filhas. **Não existe
`/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` nem `/privacidade/`**, e a **16.1** nomeia essas
cinco por nome. **A ilha publica link de afiliado da Shopee desde 29/10** — na F2 e nas duas páginas de
produto — sem a página de divulgação que o programa e o leitor pedem.

Ele é o próximo por três razões independentes: **não depende de despacho nenhum** (nem do `gov.br`, nem
do Chrome, nem das etiquetas do ML); pela **21.7** essas páginas **ficam fora do teto** da 21.4, então
não gastam leva de malha; e é **dívida de confiança no ar**. A 21.7 nasceu exatamente deste caso na
aquametria, com a privacidade parada em "aberto" *"com a etiqueta do GA4 no ar e link de afiliado
publicado desde 12/09"*. O "pronto quando" está escrito na fila do `PROMPT.md`.

**A conta da 31.1 desta execução, dita sem maquiar:** ela **não** entregou página nova no ar. Entregou
a lista que fecha três consultas, o despacho que destrava as outras duas, e o conserto de um portão que
reprovava página certa todo dia. **Zero página no ar era o resultado correto aqui** — a 30.8 proíbe
`alvo` desta nuvem —, mas isso não a torna uma entrega da 31.1, e quem contar a proporção conta como
ela é. **O 5d existe para que a execução seguinte não tenha essa conversa:** ele é quatro páginas no
ar sem depender de ninguém.

---

## 2026-10-29 19h1xZ–20h1xZ — **BLOCO 5b: A CONSULTA DO GOOGLE E A CHAVE DA LOJA NÃO SÃO A MESMA PALAVRA** — das seis cabeças do dossiê só **duas** abrem o portão da 30.2, e a causa das outras quatro está medida

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar:
(a) o **despacho do molde da 32.6** segue `FECHADO` nas três ilhas, lido no topo dos três `PROMPT.md`;
(b) nenhum despacho **ALTA** aberto é de ilha *"no ar e quebrada"* — os ALTA de `dados/despachos.md` são
o egresso do `gov.br` (endereçado ao Raphael, não é trabalho da Fundação), o chamado da HostGator da
clubedomosaico (pela **19.4(b)** o próximo passo é chamado, não reparo) e o portão de desembarque que
falta nas outras duas ilhas, que é risco guardado e não página servindo erro. `executando_desde` estava
`null`, que pela **1.1** já significa que não havia bloco da Fundação vivo — reserva escrita às **19h18Z**
(commit `642ac19`), push aceito de primeira, **renovada às 19h37Z e às 19h48Z**. Nenhum branch `claude/*`
à frente do `main` e nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` e o `/status` em **200 nas três passadas**,
com `aquametria.com.br` em 200 nas mesmas três.

---

### O ACHADO, E ELE REORDENA O QUE SOBRA DA FILA

O bloco pedia *"páginas pelo nome do produto (seção 30) para as seis cabeças"*. Antes de escrever uma
linha de página, medi na loja o que cada cabeça devolve — **20 ofertas por chave, nas seis, pela Open
API**. O resultado:

| chave | o que ela devolve nas 20 primeiras |
|---|---|
| `patinete eletrico` | **ZERO** patinete de adulto. Serve `Patinete Elétrico Infantil 150W Rodas 6 Polegadas UNITOYS` e `Moto Elétrica Infantil 6V` |
| `moto eletrica` | **20 de 20** entre brinquedo infantil e peça de caminhão (soquete de painel, relé de pisca) |
| `scooter eletrica` | brinquedo infantil e acessório |
| `bicicleta eletrica` / `bike eletrica` | câmara de ar, pneu, compressor, moto infantil |
| `motos eletricas para adultos` | 18 de capacete e capa de chuva, 2 veículos de adulto com zero venda |

**Com o qualificador `adulto`, a MESMA família devolve produto de verdade:** `patinete eletrico adulto`
→ **16** patinetes de adulto entre **R$ 1.297,13 e R$ 3.399,00**; `bicicleta eletrica adulto` → **5**
e-bikes, três delas com **74, 28 e 25 vendas**.

**A palavra que a pessoa digita no Google e a palavra que acha o produto na loja não são a mesma, e
neste nicho elas divergem por um qualificador.** Por isso cada consulta passou a declarar uma **escada
de chaves**, do degrau mais específico para o mais largo, a escada **para no primeiro degrau que alcança
o piso de três**, e o degrau que casou fica **gravado em cada anúncio** — o mesmo desenho que a
`coletar-piso-de-compra.py` desta ilha já usa pela **25.6(a)**, agora um andar acima. E a exigência da
família é **POSITIVA** (`adulto` declarado no título), nunca negativa.

**DUAS DAS SEIS NASCERAM. AS OUTRAS QUATRO NÃO, COM A CAUSA MEDIDA:**

- `moto eletrica` e `scooter eletrica`: a SERP **autoriza** (alvo, vista com os olhos do Raphael em
  27/10), e o que falta é **produto**. Três anúncios de adulto, **zero venda** nos três, preços variando
  **R$ 6.500** para a mesma classe. O `PROMPT.md` desta ilha já escrevia a regra antes desta medição e
  ela vale: *"na Shopee, scooter e moto elétrica aparecem com 0 vendas e preços incoerentes — não entram
  como recomendação"*. Página que nasce **no piso** com três anúncios sem uma venda sai do ar na primeira
  coleta que perder um. O caminho delas é o Mercado Livre, onde o dossiê mediu 8 de 10 com link
  rastreável — e lá a geração exige clique humano (25.6), o que faz disso **despacho, nunca bloco**.
- `bike eletrica` e `motos eletricas para adultos`: pela **30.4**, mesma intenção de outras duas. O
  sinônimo vive no corpo da página irmã, com a âncora apontando para ela.

As quatro causas estão escritas em `dados/consultas-de-produto.json` e, **em voz de leitor**, no cartão
mudo da mãe — que não é link, pela **16.5**.

### O QUE FOI AO AR

`/veiculos/` (seção de nível 1 da **16.1**, com o nome que o `VOZ.md` já declarava no menu),
`/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/`, filhas diretas dela pela **30.1**.
Ordem da **32.2** de cima para baixo: trilha e H1 · caixa de resposta com o preço mediano em Mono ·
bloco de compra com `id="comprar"` logo abaixo · a tabela-resumo **visível** com **todos** os anúncios
(a **seção 7** manda nomear todo item uma vez) · a prestação de contas de quem não entrou, com a causa
contada · a malha da **16.4** também visível, porque é alvo de link e nem todo navegador abre um
`<details>` fechado ao pular para dentro dele · o resto nas dobras da casca · a barra fixa do telefone.

**NENHUM DADO TÉCNICO FOI PUBLICADO, E ISSO É O PRODUTO DA PÁGINA.** Potência nominal, velocidade
máxima, acelerador e carga máxima têm piso de **nível 5** no `niveis_minimos_por_campo` do esquema desta
ilha, e título de anúncio é **nível 6**. Então a coluna diz o que o anúncio **declara** — e a frase que
conta isso é **contada no gerador, em cinco formas**, nunca escrita na prosa: de **16** anúncios do
patinete, **15 declaram um watt** e **1** diz qual watt é aquele. É a tese do `VOZ.md` virando coluna.

### AS TRÊS COISAS QUE QUEBRARAM, E AS TRÊS SÃO DO MESMO TIPO

**1. A RÉGUA RECUSOU QUATRO PRODUTOS CERTOS NA PRIMEIRA PASSADA COM REDE.** O grupo `acessorio`
barrou `Patinete Elétrico 800W Pico 1000W ... Pneu 10" Off-Road` por **`pneu`**, `Patinete Elétrico
Dobrável Adulto com Assento` por **`assento`** e `VYRON Patinete Elétrico Adulto ... Amortecedor` por
**`amortecedor`**. **O título de um veículo nomeia as peças DELE.** E o absurdo que fechou a conta:
`Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo` **passou**, porque `pneus` no plural não casa com
`pneu` entre bordas — duas páginas certas, uma recusada e uma aprovada **pela letra `s`**. O conserto é a
**regra da posição**: `acessorio` só recusa quando a palavra vem **antes** do substantivo do produto, e o
substantivo é um **campo declarado**, não a primeira posição de uma lista — regra que depende da ordem de
uma lista se desliga em silêncio no dia em que alguém a reordena por estética.

**2. A RECUSA POR PEDAÇO DE PALAVRA.** A primeira versão recusou `Patinete Elétrico Adulto 350W **36V**`
com a causa `infantil`, porque a lista do brinquedo tem `6v` (a bateria do brinquedo) e **`36V` termina
em `6v`**. Mesma família do `grep` que atravessa YAML quebrado: o instrumento responde, e a resposta é
errada. Hoje a busca é por palavra inteira, com os prefixos **declarados um por um** (`eletric`,
`adulto`, `bicicleta`, `patinete`) — e `moto` **não** é prefixo, porque casaria com `motocicleta`,
`motorizado` e `motoca`, três palavras que aparecem em título de acessório e de brinquedo desta coleta.

**3. A MUTAÇÃO `São 2 famílias com página hoje` SOBREVIVEU.** A trava que proíbe número digitado na prosa
declarada cobrava **dois dígitos ou mais**, e a contagem que esta ilha de fato tem é de **um** dígito.
Ela passou a cobrar **qualquer** dígito, com a lista de permitidos nomeando o que escapa (o número da
Resolução Contran é nome próprio de documento, não número de tela) e o resto escrito por extenso. Na
mesma rodada, a trava do número digitado só lia string e lista de string, e as **perguntas frequentes
são lista de dicionário** — ela passava por cima de toda pergunta e resposta sem dizer que não as leu,
que é a cara do portão que aprova em silêncio o que não mediu (**32.5-b**).

**4. DOIS "DEGRAUS" DIFERENTES MORAVAM NO MESMO CAMPO.** Achado relendo o próprio diff, antes de medir
no ar. `degrau_da_escada` do anúncio é o degrau da escada de **chaves** (que palavra achou o produto na
loja); o `degrau` que o cartão da casca lê é o da escada de **compra** da 25.1, e é ele que decide o
rótulo do botão — ficha diz "Ver na Shopee", busca diz "Ver ofertas na Shopee". A vitrine passava o
primeiro no lugar do segundo: **dava o rótulo certo por coincidência** (1 e 1), e daria o errado no dia
em que uma consulta descesse para o degrau 2 da escada de chaves. Agora o degrau de compra vai
**declarado**, e a tabela parou de digitar o rótulo: ele sai de
`rodametria_casca_rotulo_da_loja()`, que é onde ele mora.

**5. A MÃE `/veiculos/` NASCERIA PÁGINA FINA.** Contado antes de medir no ar, com a mesma régua do
`conferir-no-ar.py`: **1.253 caracteres** de corpo contra o piso de **1.500** da seção 8. E o conserto
não foi texto a mais — foram **os três números** que decidem a compra de um elétrico (potência nominal
mais velocidade máxima, watt-hora da bateria, carga máxima declarada), que são o produto desta casa e
estavam faltando justamente na página onde a pessoa escolhe qual família olhar, mais a dobra "Como
sabemos". Corpo em **2.923** caracteres.

### E A BANCADA DENUNCIOU A RÉGUA NOVA NA PRIMEIRA PASSADA, COM RAZÃO

Ela nasceu `relevancia-do-anuncio.py`, que não casa com convenção de nome nenhuma, e a `bancada.py`
escreveu a frase certa: *"ou ele é portão e precisa do prefixo, ou não é e precisa estar fora de
`ferramentas/` — silêncio aqui é portão que nunca roda"*. Virou `teste-relevancia-do-anuncio.py` e roda
a bateria quando chamada sem argumento. **A ilha nasceu com a bancada e foi ela que pegou isto**, não
alguém se lembrando.

### OS PORTÕES

- `bancada.py`: **13 portões** sem rede, **0 falha** (eram 9 antes deste bloco).
- `teste-relevancia-do-anuncio.py`: **25 casos**, 0 falha, todos com título **real** desta coleta, mais
  um **kit fabricado** para a trava `kit_multiplo` poder falhar — nenhuma das 180 ofertas medidas era um
  kit de dois veículos da mesma família, e trava que nunca viu o mundo dela nasce errada sem poder falhar.
- `coletar-por-consulta.py --conferir`: **190 afirmações**, 0 falha, sem rede. Ele reaplica a régua sobre
  os títulos gravados, refaz o número próprio e a contagem de rótulo, e cobra que a chave gravada esteja
  **na escada declarada** e que todo anúncio tenha sido achado por ela.
- `gerar-vitrine-de-produto.py --conferir`: **150 afirmações**, 0 falha.
- `mutacoes-produto.py`: **26 mutações, 26 reprovadas, 0 sobrevivente, 0 inerte**, com trava de alvo
  exato em todas e **três mundos fabricados** que o banco de hoje não produz (foto sem dimensão, página
  abaixo do piso de três, carrossel acima do teto de cinco). Ela roda o mundo **limpo** primeiro: portão
  que reprova tudo não mede nada.
- As **21 fotos** têm largura e altura **lidas no cabeçalho do arquivo na CDN** (1024 × 1024), nunca
  digitadas, e a leitura vem de `coletar-oferta.py` — fato externo se lê de **um lugar só** (seção 8).

### OS NÚMEROS NO AR, MEDIDOS DEPOIS DA REVISÃO 16

- `conferir-no-ar.py`: **APROVADO, 281 afirmações, 0 falha.** Corpo das cinco URLs: **2.586 · 11.246 ·
  3.488 · 9.408 · 6.377** caracteres, todas acima do piso de 1.500.
- `conferir-32-5-no-navegador.mjs` (390 px, Chromium de verdade, quebra de cache): **APROVADO, 3 de 3
  páginas do molde.** Caixa de resposta a **211 px** nas duas páginas novas (teto 700); primeiro botão
  de compra a **1.129 px** no patinete e **1.084 px** na bicicleta (teto 1.400); a F2 segue em 329 e
  1.380 px. Rolagem horizontal **0** e **0** erro de JavaScript nas três.
- Na página do patinete: **21** links `sponsored`, **ItemList com 16 itens**, **FAQPage com 4
  perguntas**, **BreadcrumbList de três níveis** (`Início › Veículos › Patinete elétrico`), 4
  `<details>` e 5 imagens com `width`/`height`.
- **O portão de pixel lista `/veiculos/` e a home como FORA DO MOLDE**, e isso é registro e não
  aprovação em silêncio: as duas não têm formulário nem bloco de compra. Para a home é decisão
  registrada (nasceu HUB); para a mãe é porque a **32 não nomeia uma família de página de LISTAGEM** —
  ela tem FERRAMENTA (32.1) e FICHA/RESPOSTA (32.2) e mais nada. Duas ilhas já têm página de listagem
  (`/materiais/` da clubedomosaico e esta). **Fica anotado para a leitura semanal; não inventei regra.**

### A LEITURA SEM QUEBRA DE CACHE, E O QUE ELA ACHOU NÃO É DESTA ILHA

As três URLs novas em **200 nas duas leituras**. E a sonda **virgem** — caminho carimbado com o relógio,
que nunca existiu — devolveu **404 · 200 · 200 · 200**, com o corpo do 404 servido em HTTP **200** e o
`<title>Página não encontrada – Rodametria</title>`. **É o mesmo soft 404 na borda que a clubedomosaico
registra há oito medições**, agora medido numa **segunda conta do mesmo hospedeiro** — e isso é o dado
que faltava ao chamado: até hoje ele só havia sido medido num domínio, o que deixava aberta a leitura de
que fosse configuração daquela conta. Esta ilha tem **dois dias de vida** e nunca recebeu uma linha de
configuração de cache. Linha acrescentada ao despacho **ALTA** de `dados/despachos.md`, afirmando **só
sobre a ilha que esta execução reservou**, como a lição de 14/09 daquele arquivo manda. **Não se
conserta daqui.**

### O DEFEITO QUE A ENTREGA ACHOU NO AR, E ELE É A SEÇÃO 4 EM FORMA DE INSTALADOR

A **revisão 13** subiu os arquivos e **não criou as três páginas**. A instalação da casca rodava uma vez
por **versão da casca**, e a revisão 13 subiu casca nova **e** o snippet da página nova na **mesma
passada do Sync**: quando o `init` chamou a instalação, o snippet novo ainda **não estava carregado**
naquela requisição — então o filtro `rodametria_instalar` dele não existia, as três páginas não nasceram,
e a casca gravou `instalado: 1.3.0`. **Com a versão já marcada, a instalação nunca mais rodaria.**

**E o sintoma era verde em todo lugar:** `/status` em **13**, as **cinco** linhas do log da revisão
dizendo `ok`, e `/wp-json/rodametria/v1/casca` já listando `veiculos`, `patinete-eletrico` e
`bicicleta-eletrica` no mapa de páginas — **com `url` vazia nos três** — e `wp-sitemap.xml` com **duas**
URLs. O relato gravado tinha duas linhas, `home` e `f2`, e **nenhuma vermelha**. Quem lesse o log do
desembarque pela 20.4 e parasse ali teria escrito "entregue".

A casca subiu para **1.4.0**: a instalação roda de novo quando a **assinatura do mapa** muda — os slugs
do mapa, em ordem, num texto só — e não só quando a versão da casca muda. Com isso **página nova nasce
no dia em que o snippet dela entra, sem ninguém tocar na versão da casca**, que é o que o comentário do
mapa promete desde a revisão 3: *"a casca não é editada quando a ilha cresce"*.

A casca também subiu de 1.2.1 para 1.3.0 por **duas razões de árvore**, as duas da **16**:
`garantir_pagina()` passou a aceitar **pai** (16.2: página sem pai é defeito e não publica), e
`url_do_slug()` passou a achar a página pela meta `_rodametria_id` **em vez de por caminho** —
`get_page_by_path()` casa o caminho **inteiro**, e no dia em que a árvore ganhou um nível ele devolveria
nulo para a filha, com `casca_link()` transformando link vazio em texto **sem reclamar**: página no ar,
órfã, com a mãe apontando para texto morto e nenhum portão vermelho.

---

## 2026-10-29 16h2xZ–16h4xZ — **BLOCO 3e: A PREMISSA DELE ESTAVA ERRADA**, e a coleta que não deu em campo técnico nenhum achou um defeito **no ar** — o bloco de compra dizia a mesma coisa **três vezes** e a página de autonomia estava **calada sobre autonomia**

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar:
(a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas — aquametria 21/10 18h2xZ,
clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ, lidos no topo dos três `PROMPT.md`; (b) o único
despacho marcado **ALTA** aberto no arquipélago é o **ITEM 1 da ronda de 28/10 da clubedomosaico** (58
links de afiliado sem piso), e ele **não fura o foco**: a 1.2 exige ilha *"no ar e quebrada — página
servindo erro, ferramenta devolvendo número errado, site fora do ar"*, e a régua técnica daquela ronda
**passou inteira** (32 de 32 em HTTP 200, console limpo, as duas ferramentas com a conta refeita na mão).
É defeito grave de banco, não de página servida. `executando_desde` estava `null`, que pela **1.1** já
significa que não havia bloco da Fundação vivo. Reserva escrita às **16h25Z**, commit `fb97851`, push
aceito de primeira, e **renovada às 16h37Z**. Nenhum branch `claude/*` à frente do `main` e nenhum PR
aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` e `robometria.com.br` em 200 nas mesmas três.

---

### A PREMISSA DO BLOCO ESTAVA ERRADA, E CORRIGI-LA FOI A ENTREGA MAIOR

A fila pedia *"coleta em ficha de fabricante — o nível 4 da escada, hoje vazio"*. **Ele não está vazio
por falta de tentativa: pode ser vazio por estrutura.** Remedido pela **20.3** às 16h2xZ, três passadas
cada, com controle verde e a causa lida no `__agentproxy/status` em vez de suposta (`connect_rejected`,
403 de política no CONNECT): `honeywhale.com`, `maxshot.com.br`, `kenda.com.br`, `sousabike.com.br` e
`evoo.com.br` em `000`. **Mas o egresso não é a causa raiz** — e é isso que muda o plano de quem ler
isto. As duas marcas principais do banco **não têm site de fabricante achável**: a Honeywhale vende por
vitrine de marketplace e varejo mexicano, a MAXSHOT só aparece em varejista brasileiro. **Abrir os cinco
domínios não encheria este nível.** São marcas *de* marketplace, não fabricantes com página própria no
Brasil.

**E O GARGALO TEM NOME, UM SÓ, E ELE NÃO É DESTA ILHA: o nível 5 está atrás do egresso.**
`www.casasbahia.com.br`, `www.extra.com.br` e `www.magazineluiza.com.br` em `000` nas três passadas;
`www.mercadolivre.com.br` em `403` do próprio anti-robô, com o CONNECT passando (egresso aberto e caminho
fechado são coisas diferentes). A leitura por **BUSCA** — a única porta aberta — alcança os níveis **6, 7
e 8**, que são **exatamente** os que `niveis_minimos_por_campo` recusa nos quatro campos do nível 5.
**Consequência escrita sem maquiar: `potencia_nominal_w`, `velocidade_max_kmh`, `acelerador` e
`carga_max_kg` não são colhíveis desta nuvem por caminho nenhum.** A F1 e a F3 não vão ao ar por coleta —
vão por **abertura**. O despacho ALTA de `dados/despachos.md` deixou de ser "seria bom" e passou a ser o
único caminho.

**O QUE A BUSCA ACHOU E FOI RECUSADO**, escrito no esquema (versão 4) registro a registro, para a próxima
execução não gastar a mesma busca — porque o que foi procurado e não achado é dado:

| achado | fonte | nível | por que não entrou |
|---|---|---|---|
| variante de **350 W** do M2 MAX | loja estrangeira de catálogo | 8 | nível 8 não sustenta campo **nenhum**. E a informação é boa: existe variante de potência com o MESMO nome de modelo |
| **36 V** de bateria | publicador editorial | 7 | nunca sustenta campo técnico — e é do **MAX-B**, justamente o aparelho que as travas do casamento barraram por ser outro |
| **25 km/h** e **120 kg** | guia de compra | 8 | os dois campos exigem nível 5. A oferta casada diz 32 km/h (nível 6): **a divergência é ela mesma a prova de que aceitar uma seria sorteio** |
| **bico** da câmara Kenda 16x3.0 | — | — | **não publicado em porta nenhuma alcançável**. A busca devolveu Schrader para 16x1.5/2.25 e 16x1.75/2.125, que são linhas de bicicleta: herdar o bico de outra largura é especificação herdada, proibida |

**O ÚNICO CAMPO QUE SOBROU COLHÍVEL FOI COLHIDO:** `autonomia_declarada_km` = **22 km** no
`honeywhale-m2-max`, lido no título da **própria oferta casada** (20299836765) e não de oferta vizinha.
A oferta foi **remedida na Open API às 16h3xZ**: viva, R$ 2.299, 3 vendas, título literalmente idêntico ao
colhido às 13h3xZ. Nível 6, que a escada aceita neste campo com a razão escrita (o erro caro aqui é uma
faixa de km larga, não uma pessoa na rua sem habilitação). **E a medição tem uma metade negativa que vale
tanto quanto: dos 10 títulos que a resposta devolveu, ZERO declara tensão ou amperagem.** Não é que a
leitura falhou — é que a bateria não está publicada nesta porta.

---

### O DEFEITO NO AR QUE A COLETA ACHOU: TRÊS CÓPIAS DE UM FATO, E ZERO DO FATO QUE A PÁGINA RESPONDE

Medido às 16h3xZ em `/autonomia-patinete-eletrico/`, com quebra de cache. O bloco de compra dizia **a
mesma coisa três vezes na mesma tela**:

1. o parágrafo de abertura: *"Nenhum destes entrou pela conta de Wh: a ficha deles não declara tensão nem
   amperagem"*;
2. a linha `bateria não declarada` dentro de cada cartão (4 ocorrências, uma por cartão);
3. o rótulo do grupo do cartão: `a ficha não declara a bateria`.

**E o cartão da página de AUTONOMIA não dizia uma palavra sobre autonomia** — enquanto a oferta que o
botão dele abre declara, no próprio título, **22 km**. Três cópias de um fato, e zero do número que a
página existe para responder, gastando a primeira tela que a 32.5 mede em pixel.

**Consertado nas três pontas:**

- **a autonomia entra no cartão PRIMEIRO**, com a atribuição ao lado — e a atribuição **não é digitada**:
  `quem_declara()` a alcança pelo caminho que o próprio banco grava (o campo diz qual `fonte` o sustenta,
  a fonte diz o `nível`, e o nível diz `na_tela.quem_declara` na escada do esquema). O dia em que a escada
  mudar a palavra, o cartão muda com ela. Número de nível 6 na tela **sem dono** é promessa da ilha;
- **a linha duplicada saiu.** O cartão serve `V × Ah` quando existe e **cala** quando não existe, porque
  o rótulo do grupo logo abaixo já é literalmente aquela frase;
- **a frase de abertura deixou de ser string digitada no PHP** e passou a ser derivada da contagem da
  vitrine, em `gerar-f2.py`.

**ESSA ÚLTIMA É A 32.5-d OUTRA VEZ, EM OUTRO MATERIAL, E É A LIÇÃO DO DIA.** *"Nenhum destes entrou pela
conta de Wh"* era uma **afirmação sobre o estado do banco** escrita à mão dentro do snippet, que nenhum
portão conferia. Ela é verdadeira hoje **por falta de dado que a contradiga**: no dia em que um registro
declarasse V e Ah com oferta aberta, o cartão entraria em `cabem_no_wh` e o parágrafo acima dele
continuaria dizendo que nenhum entrou — mentindo calado, com cara de conferido. É a mesma família do
comentário de CSS que declarava economizar 52 px e nunca economizou um, e do número de tela digitado.
**Prosa que afirma o estado do banco é número digitado em outro traje.** As **cinco** frases da função
nova são conferidas sobre mundos **fabricados** dentro do próprio gerador — vitrine de 1 e de 4, com 0
cabendo no Wh, com todos e com parte —, não só a que o banco de hoje acende. Singular e plural inclusive:
*"O único com oferta aberta hoje"* contra *"Nenhum dos 4"*.

**NENHUM PORTÃO NOVO NASCEU, e é decisão e não esquecimento:** a **31.3** proíbe ampliar portão enquanto a
ilha tiver item de conteúdo ou de página pelo nome do produto aberto na fila, e os blocos 4, 5, 5b e 6
estão abertos. Os mundos fabricados moram dentro do gerador que já existia e não custaram arquivo novo.

---

### CONFERIDO NO AR (18.4), REVISÃO 12

- `/status` em **12**, igual ao `manifest.json`, com as **duas** linhas da revisão 12 dizendo `ok`, lidas
  uma por uma (**20.4**). Registro, não aprovação: a janela do log tem 15 linhas e está **cheia**, então
  item que rolou para fora dela não foi conferido.
- `conferir-no-ar.py`: **138 afirmações, 0 falha**.
- **32.5 no navegador, a 390 px reais, com o portão descobrindo as páginas no `wp-sitemap.xml`:**
  formulário **329 px** (teto 700) e primeiro botão de compra **1.380 px** (teto 1.400). A home segue
  **fora do molde** com o motivo impresso (não tem bloco de compra), caixa de resposta a 331 px.
- **E o botão SUBIU 5 px com uma linha A MAIS no cartão** (era 1.385). A causa é aritmética de texto: a
  frase de abertura derivada tem 145 caracteres contra 175 da digitada, e devolveu uma linha acima dos
  cartões. Tirar a repetição pagou a linha que a autonomia custou, com 5 px de troco.
- Texto servido, contado com quebra de cache: `22 km declarados pelo vendedor` **1**,
  `bateria não declarada` **0** (eram 4), `Nenhum destes entrou pela conta de Wh` **0** (era 1),
  `Nenhum dos 4 com oferta aberta hoje` **1**.
- **Bancada: 9 portões sem rede, 0 falha.** Snippet F2 **1.2.0 → 1.3.0**.

**E O PIXEL FOI PREVISTO ANTES DE IR AO AR, por um método que vale guardar.** A **32.5-d** manda conferir
no navegador quem acrescenta dado novo ao cartão, e com 15 px de folga sobre o teto eu não queria descobrir
isso *depois* do desembarque — nesta ilha cada revisão custa uma espera de Sync. Baixei o HTML servido,
troquei **as duas frases** num espelho local e medi o espelho a 390 px. **O método se valida contra o
número que o portão já mediu na origem:** o espelho *antes* deu **1.385 px**, idêntico ao que o portão
havia medido, e o espelho *depois* previu **1.380 px** — que foi exatamente o que o portão mediu no ar
depois da revisão 12. Espelho não substitui portão (o portão mede a **origem**, com o CSS e a fonte que o
site serve); ele diz, de graça, se vale gastar uma revisão.

---

### O ACHADO DE MÉTODO, E ELE MUDA O CUSTO DE TODA EXECUÇÃO NESTA ILHA

**O CRON DO SYNC NÃO RODA POR RELÓGIO: RODA POR VISITA.** O `ESTADO.md` e o `PROMPT.md` desta ilha dizem
que o Sync tem *"cron próprio de 30 minutos"* e que a Fundação, sem o token, **"empurra e espera"** — a
execução da manhã registrou que isso custou **nove esperas de cron** entre 10h44Z e 12h10Z.

**Medido às 16h3xZ:** o log do `/status` trazia disparos às 11h39, 12h09, 13h56 e 14h09 — e depois **nada
por 2h29**. E 14h12Z é exatamente o minuto em que a execução anterior fechou e **parou de abrir o site**.
É WP-Cron: ele é acionado por **requisição**, não por um relógio no servidor; sem visita, a ilha não
desembarca, por mais que a agenda diga 30 minutos. Três GETs na home às 16h38Z e o `wp-cron.php`
respondendo **409** (já havia cron em andamento) — a revisão 12 entrou em **um minuto**.

**A regra, e ela cabe numa frase: a Fundação não espera o cron nesta ilha — ela o aciona, abrindo a
própria página, e não precisa do token para isso.** Nove esperas de cron eram evitáveis, e a frase
"empurra e espera" estava certa sobre o token e **errada sobre o relógio**.

---

### O QUE FICA ABERTO

1. **A bateria do M2 MAX não está publicada em porta nenhuma alcançável** (0 de 10 títulos da Open API).
   Enquanto nenhum registro com oferta aberta declarar V e Ah, `cabem_no_wh` fica vazio e o bloco de
   compra continua dizendo o que os cartões **são** em vez do que a conta escolheu. Está na tela, com a
   causa. **Não é defeito.**
2. **A leitura sem quebra de cache** (como o Google lê) segue não feita — terceira execução seguida.
   Toda URL desta passada foi pedida com `?v=<agora>`, então as afirmações são sobre a **origem**. O
   portão que mede a borda existe na clubedomosaico (`leitura-do-visitante.py`) e não aqui, e a **31.3**
   proíbe abri-lo enquanto houver item de conteúdo e de página pelo nome do produto na fila.
3. **O despacho ALTA do egresso** (gov.br para a F1; casasbahia, extra e magazineluiza para o nível 5)
   está remedido hoje e **continua recusado**. Ele é agora o único caminho para a F1 e a F3.

**PRÓXIMO PASSO: o bloco 5b — página pelo nome do produto (seção 30).** Ele é o próximo por **eliminação
medida**, não por ordem de lista: o 3e provou que coleta não destrava mais nenhuma ferramenta desta ilha;
o bloco 4 pede ferramenta nova e as duas que faltam estão travadas por dado que não se colhe daqui; o 5
pede artigo-âncora **pareado** com ferramenta, e só há uma no ar. O 5b não depende de nenhum dos três — as
seis cabeças estão medidas, a SERP delas está medida e **não tomada**, e a ilha tem 4 registros publicáveis
com piso e 1 com ficha. A ilha tem **2 URLs** contra as 40 do piso da 21.1. Primeiro passo: ler a seção 30
inteira e a 21.4 (teto de leva por semana) **antes** de escolher quantas páginas, e escolher a primeira
cabeça pela intersecção entre volume e o que o banco sustenta — hoje `patinete eletrico`, a única das seis
com registro de ficha aberta nesta ilha.

---

## 2026-10-29 13h3xZ–14hxxZ — **BLOCO 3d: A ILHA TEM A PRIMEIRA FICHA DE PRODUTO DA HISTÓRIA DELA**, com foto medida e preço de hoje na tela. E o bloco mediu o que vale mais que a ficha: **13 dos 17 registros não têm com o que pedir uma** — e isso não se conserta com trava mais frouxa

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar:
(a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas — li o topo dos três `PROMPT.md`
(aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ); (b) **nenhum despacho
marcado ALTO** existe em ilha no ar e quebrada — procurei o rótulo nos três arquivos e não há. O despacho
da Sentinela de 28/10 nesta ilha foi **reescrito pela 18.3** na execução da manhã e o único item que
sobrou é a **conta da 31.1**, cujo `pronto quando` é a leitura semanal recontar — ele diz, com todas as
letras, que *"o caminho é a fila andar, não uma correção"*. `executando_desde` estava `null`, que pela
**1.1** já significa que não havia bloco da Fundação vivo; o último commit da ilha era de **12h13Z**, 82
minutos antes. Reserva escrita às **13h36Z**, commit `f9e138d`, push aceito de primeira, e **renovada às
13h59Z** pela 1.1. Nenhum branch `claude/*` à frente do `main` e nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` e `www.rodametria.com.br` em **200 nas três
passadas**, com `aquametria.com.br` em 200 nas mesmas três. E a fonte que este bloco precisava foi medida
antes de qualquer regra exigi-la, pela **20.3**: `open-api.affiliate.shopee.com.br` em **200 nas três**, e
`cf.shopee.com.br` — a CDN de onde a dimensão da foto sai — em 200.

**A CREDENCIAL.** `SHOPEE_APP_ID` e `SHOPEE_SECRET` conferidos **por presença e nunca por valor**, e os
dois **estavam no ambiente do processo** desta execução. Não foi preciso passar valor nenhum em linha de
comando, e não se deve: linha de comando fica visível na lista de processos da máquina. `git grep` pelo
NOME dos dois campos antes de empurrar: zero ocorrência no que foi commitado.

---

### 1. O QUE FOI AO AR, E É A METADE VISÍVEL DO BLOCO

`honeywhale-m2-max` **casou no DEGRAU 1 da 25.1** e o primeiro cartão do bloco de compra da F2 passou a
servir, em `/autonomia-patinete-eletrico/`:

- a **foto de verdade** (`cf.shopee.com.br/...`, 1024×1024), no lugar do espaço reservado;
- o **link da ficha** como botão, com o rótulo mudando de *"Ver ofertas na Shopee"* (degrau 4) para
  *"Ver na Shopee"* — a casca já fazia essa distinção e nunca tinha tido um registro para exercê-la;
- a linha discreta **"Veja todos disponíveis aqui"** logo abaixo do botão, que é a 25.2 ao pé da letra:
  *"quando existir e estiver viva, ela vira o botão e a busca desce para a linha discreta"*. A busca
  **não sai** — ficha apodrece e busca não;
- o **preço de hoje**: R$ 2.299, lido pela Open API em 29/10, com a data ao lado. Era de 27/10, do painel.

O componente da linha discreta mora na **CASCA** e não no snippet, pela **32.6-b**. O `conferir-no-ar.py`
passou a ler `bloco de compra: 4 cartão(ões), degrau(s) [1, 4]` — antes era só `[4]`.

---

### 2. AS TRAVAS DA 25.7 TRABALHARAM, E O NÚMERO ESTÁ GRAVADO NO BANCO

**10 ofertas julgadas, 6 barradas.** Quatro eram **`M2 MAX-B`**, que é outro patinete (armadilha 4 — *"o
sufixo faz outro aparelho"*), e duas enumeravam **`M2 Pro,M2 MAX,M2 MAX-B modelos da série`** (armadilha
5 — *"no máximo um está certo, e não há como dizer qual, então os dois caem"*). Os seis motivos estão em
`afiliado.candidatos_barrados`, em português, dentro do registro.

**E AQUI ESTÁ A PROVA DE QUE A RÉGUA NÃO ESCOLHE PELO NÚMERO BONITO:** a oferta de **maior venda** da
resposta inteira — 12 vendas, nota 4,9, na `HONEYWHALE BRASIL` — **foi barrada**, porque é o MAX-B. A
escolhida tem **3 vendas**. Dar o primeiro lugar da vitrine ao anúncio mais vendido teria sido recomendar
um produto que a página não descreve, e é o que a 25.4-b.1 chama de pior que casamento nenhum: *"parece
dado"*.

**O casamento foi conferido COM OS OLHOS antes de gravar**, como a 25.3 manda: oferta `20299836765`,
título *"HONEYWHALE M2 MAX Patinete Elétrico Adulto, 500W Scooter Eletrica, 32KM/H Velocidade, 22KM
Autonomia"*, loja `HONEYWHALE BRASIL`, preço **único** (2299/2299). O registro declara Honeywhale M2 MAX,
500 W, 32 km/h. Bate campo a campo.

**A FOTO É MEDIDA, NUNCA SUPOSTA (25.7):** 1024×1024 lidos do **cabeçalho do arquivo** na CDN, nos
primeiros 32.768 bytes, e o registro grava `como_a_dimensao_foi_medida`. Dimensão digitada é da família do
número de tela digitado — parece conferida.

---

### 3. O ACHADO QUE VALE MAIS QUE A FICHA: **13 DOS 17 REGISTROS NÃO TÊM IDENTIDADE PARA PEDIR UMA**

As três causas de "não casou" saem **separadas**, pela **25.4-b.4**, e a **25.9** mediu o que custa
contá-las juntas: na Aquametria o número `12` foi lido como mercado **quatro vezes seguidas**, e a quinta
medição — item por item, degrau por degrau — achou `9 de mercado + 2 barrados com razão + 1 defeito nosso`.

| causa | quantos | o que a resolve |
|---|---|---|
| **casou** | 1 | — |
| **mercado_nao_anuncia** | 3 | só o mercado mudar |
| **candidato_barrado** | 0 | dado melhor no registro, nunca trava mais frouxa |
| **sem_identidade_minima** | 13 | **colher o campo que falta** |

**`mercado_nao_anuncia` foi medido até o fim, e não presumido.** `MAXSHOT V1`, `MAXSHOT V1SPRO` e
`Honeywhale H3` devolveram **zero em todos os degraus da escada**, e — porque a 25.9 exige que a recusa
seja separada da ausência — medi também as **variantes do nome**: `MAXSHOT V1S`, `MAXSHOT V1S Pro`,
`MAXSHOT patinete eletrico`, `Honeywhale H3 patinete`. Zero em todas. E a chave **`MAXSHOT` sozinha**
devolveu película de Zenfone Max Shot e suplemento Action Max; **`Honeywhale` sozinha** devolveu bolsa
frontal e pneus de *outros* modelos da marca (M2 Pro, M1 Lite). É a armadilha 3 da 25.7 remedida nesta
ilha: *"código de modelo é curto e o mundo é grande"*. **O H3 tem casa, e ela está fora do alcance desta
máquina:** o `titulo_colhido` dele diz *"anúncio Mercado Livre"*, e o degrau 2 — a página `/p/MLB...` —
depende do gerador do ML, que tem reCAPTCHA (25.5). Pela 25.2 isso nunca trava página: é oportunidade.

**E os 13 sem identidade são o retrato do mercado desta ilha.** Dez veículos não declaram `modelo` (ou
`marca`): `Sousa Bike`, `Siena`, `PLAYBIK`, `Verdevento`, `Evoo`, `Haixia`, `LS Sport` têm marca e nenhum
modelo; `L40 Plus` e `X13` têm modelo e nenhuma marca; `scooter-chopper-1000w-48v` não tem nenhum dos
dois. **É a mesma medição do bloco 3c por outro ângulo:** *"o que nomeia marca e modelo é achável na loja
e não publica ficha; o que publica `60 V 20 Ah` empacota três nomes no título e não é achável por nome
nenhum"*. O 3c viu isso no eixo do PISO; o 3d vê no eixo da FICHA, e a conclusão é a mesma — **o que falta
nesta ilha é coleta em ficha de fabricante (nível 4 da escada, hoje vazio)**, não link.

**A CÂMARA KENDA É A 25.9 EM FORMA NOVA, e é o achado mais fino do bloco.** A medida `16 x 3.0` casa com
**dez ofertas**, e o mercado as separa pelo **BICO** — `bico torto curvo`, `bico curvo`, `bico grosso
33mm`. São produtos que **não se substituem na roda de ninguém**, e o registro **não declara bico**.
Escolher uma ficha ali afirmaria uma válvula que o banco nunca leu, e mandaria a pessoa comprar a peça
errada. **Aqui a BUSCA é literalmente melhor que a ficha**: ela mostra as três e deixa a pessoa escolher,
que é para isso que o piso existe. O registro fica no degrau 4 com o motivo escrito, e a dívida tem nome e
é de DADO: `bico`. A 25.9(1) já diz a regra — *"o conserto é do DADO, nunca da trava"*. O esquema passou a
declarar, por tipo de peça, **qual atributo o mercado usa para distinguir** (`camara` e `pneu` → `bico`;
os outros `null`, e `null` ali é declaração e não ausência).

---

### 4. O QUE A BANCADA PEGOU DE MIM, ANTES DO AR

**`validar-banco.py` reprovou a primeira versão deste bloco**, com a frase exata: *"veiculo
honeywhale-m2-max: cotacao aponta a fonte 'open-api-afiliados', que nao esta em fontes{}"*. Eu gravei uma
cotação citando uma fonte que não declarei. **A regra que o bloco 3 escreveu pegou um defeito do bloco
3d** — e é exatamente o que um portão de dado existe para fazer. A régua passou a **declarar a própria
fonte** antes de qualquer campo citá-la, no **nível 6**, e a escada do esquema diz por que: *"o nível é o
do ELO MAIS FRACO entre autoria, custódia e leitura"*. A leitura aqui é **melhor** que a do
`painel-shopee` — é mecânica, sem ninguém transcrevendo número à mão —, mas a **autoria continua sendo o
vendedor do anúncio**. Logo 6: sustenta preço, disponibilidade e o nome comercial, e **não** sustenta
campo técnico que a F1 leia.

**E um veredito certo com a frase errada, que eu só vi porque leio o que a régua escreve.** O anúncio que
enumera a série era barrado pela trava do sufixo, dizendo *"o modelo vem seguido de `m2`, que é sufixo de
modelo"* — e `m2` ali **não é sufixo**: é o começo do modelo **seguinte** da lista. A recusa estava certa e
a explicação estava errada, e a explicação é o que a execução seguinte lê **dentro do banco**: ela mandava
consertar a coisa errada. A enumeração ganhou **trava própria** (`trava_enumeracao_da_serie`), que recusa
pelo motivo verdadeiro — o modelo aparecendo mais de uma vez no título. É a mesma família do motivo que
envelhece calado da 25.4-b.3.

---

### 5. E O DEFEITO QUE SÓ A PRIMEIRA FOTO DA ILHA PODIA REVELAR — 32.5-c, POR ESPECIFICIDADE

**A revisão 10 subiu e o portão de pixel REPROVOU:** o primeiro botão de compra foi de **1.385 para 1.471
px**, 71 acima do teto de 1.400 da 32.5. Medi no navegador a 390 px em vez de deduzir, e os números são:
**espaço reservado 96 px, foto 182 px**.

**A causa não era a foto ser grande: era de SELETOR.** `body.rdm img{max-width:100%;height:auto}` vale
**(0,1,2)** e vence `.rdm-molde-cartao-foto`, que vale **(0,1,0)** — então o `height:auto` daquela linha
mandava na foto e a altura do molde era simplesmente ignorada. **É a família que a 32.5-c nomeou** (*"a
folha do snippet redecorava a caixa do molde, vencendo-a por ordem de carga"*), aqui por especificidade. E
foi invisível por um motivo que vale guardar: **enquanto nenhum registro da ilha tinha foto, a regra da
foto nunca rodou contra uma foto de verdade.** O espaço reservado escondeu o defeito justamente porque
**não é um `<img>`** — a regra que o vencia não o alcançava. Conserto por especificidade (`body.rdm` no
seletor da foto), **sem `!important`**: `!important` esconderia a disputa em vez de resolvê-la.

**E no caminho, um número que o arquivo afirmava e a página não servia.** A linha
`.rdm-molde-cartao-sem-foto{height:44px}` estava **MORTA**: a regra de 96 px vem depois dela no mesmo bloco
de telefone, com a mesma especificidade, e vencia. O comentário dela — escrito há **três horas**, na
execução da manhã — dizia *"44 px em vez de 96, porque no telefone esses 52 px são do espaço mais caro da
página"*. **Os 52 px nunca foram economizados, e a medição de 1.385 px daquela manhã foi feita com 96.**
Afirmação em comentário não é medição: é da família do número de tela digitado, e parece conferida. A
linha saiu e a medição ficou escrita no lugar dela.

---

### 6. OS PORTÕES, E O QUE ELES NÃO PROMETEM

- **Bancada sem rede: 9 portões, 0 falha** (`mutacoes-banco`, `mutacoes-piso`, `teste-f2`,
  `validar-banco`, `atualizar-manifest --conferir`, `coletar-oferta --conferir`,
  `coletar-piso-de-compra --conferir`, `derivar-banco --conferir`, `gerar-f2 --conferir`).
  `coletar-oferta.py --conferir` nasceu com **82 afirmações sobre o que está escrito** e entrou na bancada
  pela convenção de nome, sem ninguém o listar.
- **`conferir-no-ar.py`: 138 afirmações, 0 falha** (eram 134), medido na **revisão 10**.
- **O portão de pixel da 32.5 na revisão 11: APROVADO, medido às 14h1xZ depois do cron.** Formulário a
  **329 px** (teto 700) e primeiro botão de compra a **1.385 px** (teto 1.400) — **exatamente o número de
  antes da foto existir, agora COM a foto na tela**. E a prova do conserto é a altura medida no navegador:
  **foto 96 px, reservado 96, 96 e 96** — os quatro cartões com 343 px cada. A afirmação que o esquema faz
  (*"o reservado tem a MESMA altura da foto, então foto que entra não muda a altura do cartão"*) era falsa
  quando eu a escrevi e passou a ser verdadeira por construção. Rolagem horizontal 0, zero erro de JS.
- **E `conferir-no-ar.py` rodou de novo na revisão 11: 138 afirmações, 0 falha**, com a linha do log da
  revisão corrente dizendo `ok` (20.4).
- A **home** segue `fora do molde` com o motivo impresso, como no parágrafo acima: é o estado dela, não
  uma reprovação desta entrega.
- **20.4, o log lido linha por linha:** as três linhas da revisão corrente dizem `ok`. Os **4 aguardando
  desembarque** são os itens de `publicar: false` (constantes, veículos, peças, esquema) — estado de
  propósito, conferido no `manifest.json`, não entrega que falhou. E a janela do log tem **15 linhas e está
  CHEIA**: item que rolou para fora dela **não foi conferido**, e isso é registro, não aprovação.
- **O que NÃO foi medido, e segue não sendo:** a leitura **sem quebra de cache** (como o Google lê). Toda
  URL desta execução foi pedida com `?v=<agora>`, então as afirmações são sobre a **origem**. A
  clubedomosaico tem o portão que mede a borda (`leitura-do-visitante.py`); esta ilha não.
- **A HOME continua FORA DO MOLDE**, pelo mesmo motivo de ontem e com o motivo impresso pelo portão: não
  tem bloco de compra (a caixa de resposta dela está a 331 px, dentro do teto). Ela ganha isso no dia em
  que a F1 puder nascer nela.

---

### 7. O PRÓXIMO PASSO DESBLOQUEADO

**Não é mais o 3d, e não é mais link: é COLETA DE FICHA DE FABRICANTE — o nível 4 da escada, hoje vazio.**
Os dois eixos do banco (3c pelo piso, 3d pela ficha) convergiram no mesmo lugar: o que falta aos 13
registros é **`marca` + `modelo` lidos numa ficha**, e isso não sai de anúncio de marketplace, que é o
nível 6 de onde o banco inteiro vive. **E o primeiro passo dele é a 20.3 outra vez** — medir o egresso
contra os domínios dos fabricantes **antes** de escrever regra que os exija. Nenhum domínio de fabricante
foi tentado nesta ilha até hoje.

**O alvo apertado, com nome:** `MAXSHOT` (V1 e V1SPRO) e `Honeywhale` (H3) têm marca e modelo e o mercado
da Shopee não os anuncia — ficha de fabricante resolveria o campo técnico mesmo sem oferta. E os dez sem
`modelo`/`marca` precisam do nome antes de qualquer outra coisa.

**E O PRIMEIRO PASSO DO 3e FOI DADO NESTA EXECUÇÃO, porque é um comando — e ele INVERTEU o plano do
bloco.** A 20.3 manda medir o egresso antes de escrever regra que exija a fonte, e a medição desmentiu a
suposição de que o que falta é ficha de **fabricante**:

- **Nenhuma das duas marcas principais tem site de fabricante achável.** A Honeywhale é vendida por loja
  de marketplace — a própria *"loja oficial"* dela é uma vitrine do Mercado Livre — e por varejo mexicano;
  a MAXSHOT aparece **só** em varejista brasileiro. **Para este nicho o nível 4 da escada pode ser
  estruturalmente VAZIO:** são marcas de marketplace, não fabricantes com página própria no Brasil. Isso
  não é um bloqueio a remover, é uma **premissa a corrigir**.
- `honeywhale.com`, `maxshot.com.br`, `kenda.com.br`, `sousabike.com.br` e `evoo.com.br`: **`000` nas três
  passadas**, `connect_rejected` — *policy denial* lido no status do proxy, não suposto.
- **O que vale pedir são TRÊS domínios de VAREJO GRANDE**, porque eles são textualmente o **nível 5** da
  escada desta ilha e o nível 5 *"sustenta campo técnico atribuído à LOJA"*: `www.casasbahia.com.br`,
  `www.extra.com.br` e `www.magazineluiza.com.br`, os três `connect_rejected`. A ficha da Casas Bahia
  declara, para o `V1SPRO`, **500 W, carga máxima de 120 kg e certificação UL 2272** — e `carga_max_kg` é
  a **entrada da F3**, que hoje não vai ao ar por falta exatamente desse campo em registro com oferta.
- `www.mercadolivre.com.br` devolveu **403**, e ele **não** está na lista de falhas do proxy: o CONNECT
  passou e o 403 é do **anti-robô do ML**. Egresso aberto, caminho fechado — são coisas diferentes e só o
  status do proxy as separa.
- **E a prova de que o pedido funciona é nova:** os cinco domínios de fabricante que o despacho de
  **17/09/2026** pediu para a robometria **estão abertos hoje** — `mais.conteudo.wap.ind.br` em **200** e
  `www.electrolux.com.br` em **301**, nas mesmas três passadas. A lista deixou de ter *"os domínios das
  ilhas e mais nada"*. Despacho aberto em `dados/despachos.md` com os três domínios, a causa e esta prova.
- **O que NÃO está bloqueado:** a leitura por **BUSCA** funciona, e foi por ela que tudo acima foi medido —
  o degrau que a jornadafly nomeou em 27/10 (*"o egresso não trava a coleta inteira; o que ele trava é a
  leitura direta, que é a PREFERIDA"*). O 3e **pode andar** por busca; os três domínios destravam a leitura
  **direta**, que é a que o nível 5 exige para atribuir campo técnico à loja.

**E duas dívidas pequenas, ditas para ninguém as descobrir de novo:**
1. **A `camara-kenda-16x3-0` espera UM campo: `bico`.** Com ele declarado, ela passa a ter identidade
   mínima e o casamento dela roda sem mudar uma linha de régua — o esquema já a espera.
2. **A bateria de mutações do casamento não virou arquivo.** Pela **31.2** eu não abri `mutacoes-*.py`
   novo sem defeito no ar que o justificasse, e as travas foram exercidas por dado real (10 ofertas, 6
   barradas, os motivos conferidos um a um). **O defeito que justificaria o arquivo já está escrito acima**
   — a trava da enumeração que recusava pelo motivo errado — e quando o casamento ganhar o próximo bloco, a
   bateria vira arquivo.

---

## 2026-10-29 10h1xZ–11hxxZ — **A ILHA ESTÁ NO AR.** A casca e a F2 desembarcaram, e a revisão do manifest saiu de 1 (que não publicava nada de propósito) para 5 — **a primeira execução desta ilha que entrega um byte que um visitante vê**

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar
isso: (a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas (aquametria 21/10 18h2xZ,
clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ) — li o topo dos três `PROMPT.md`; (b) o item
**ALTA** da ronda da clubedomosaico de 28/10 **não fura o foco**, porque a 1.2 só admite despacho ALTO em
ilha *"no ar e quebrada"* e a régua técnica daquela ronda passou inteira, **32 de 32 URLs em 200**. O item
dela é dado de banco, não página servindo erro. `executando_desde` estava `null`, que pela **1.1** já
significa que não havia bloco da Fundação vivo. Reserva escrita às **10h18Z**, commit `2addfbd`, push
aceito de primeira, e **renovada às 10h43Z** pela 1.1 — este bloco passou de 40 minutos sozinho. Nenhum
branch `claude/*` à frente do `main` e nenhum PR aberto.

---

### 1. A REDE ABRIU — E A ATRIBUIÇÃO DISSO É MAIS HONESTA DO QUE EU ESCREVI NO PRIMEIRO COMMIT

**O que está medido, às 10h2xZ, nas três passadas que a 20.2 manda:** `rodametria.com.br` e
`www.rodametria.com.br` em **200 nas três**, com `aquametria.com.br` e `robometria.com.br` em 200 nas
**mesmas** três. Seis medições de verde contra seis controles verdes, zero intermitência.

**O que eu escrevi no commit da revisão 2 e está ERRADO como afirmação:** *"o passo 20.1 foi dado pelo
Raphael"*. Eu não medi gesto nenhum dele — medi um `curl`. E o registro desta própria ilha desmente a
inferência: **a entrada de 28/10 às 19h1xZ, logo acima desta, escreve que `rodametria.com.br` e
`www.rodametria.com.br` estavam em 200**, e o cabeçalho do `ESTADO.md` escrito pela leitura semanal
**às 19h5xZ do mesmo dia** diz `000` com *"403 do proxy, medido duas vezes"*. **Trinta e poucos minutos
separam as duas, e elas se contradizem.**

**A leitura certa, e ela já está escrita no contrato:** a correção de 11/09/2026 no topo da seção 20 é
exatamente este caso — *"o mesmo comando, repetido minutos depois, devolveu 200 (…) era intermitência do
túnel lida como bloqueio, e o diagnóstico se propagou porque cada execução leu o `ESTADO.md` da anterior
como fato"*. Então o que esta execução pode afirmar é: **o egresso desta ilha responde 200 hoje, em três
passadas com controle**, e o despacho que dependia disso está cumprido. O que ela **não** pode afirmar é
quem o abriu, nem que ele estivesse fechado ininterruptamente desde 27/10. O campo `rede:` do `ESTADO.md`
foi escrito com essa diferença dentro.

**E a mesma passada remediu o que NÃO abriu** (20.3, porque é a execução que escreve a regra que exige a
fonte): os cinco domínios oficiais da Resolução Contran (`gov.br`, `in.gov.br`, `planalto.gov.br`,
`contran.gov.br`, `lex.com.br`), os quatro de prefeitura da camada municipal, os dois periódicos que
publicam o consumo de patinete e o repositório da tese da UPS — **todos em `000`**, com
`rodametria.com.br` e `aquametria.com.br` em 200 na mesma passada. Os três despachos abertos em
`dados/despachos.md` ganharam a nota de remedição; nenhum deles ficou mais barato.

---

### 2. O QUE FOI AO AR, E POR QUE A F2 E NÃO A F1

**A casca** (`snippets/rodametria-casca.php`, 1.1.1): tokens do `DESIGN.md`, símbolo **V9 completo** no
cabeçalho e em negativo no rodapé, favicon próprio em SVG (a seção 6 chama ícone padrão do WordPress na
aba de **bloco reprovado**), menu hambúrguer com `aria-expanded`/`aria-controls` e links `<a href>` de
verdade no HTML servido, trilha + `BreadcrumbList`, `WebSite` JSON-LD na home, e `<title>` e
`description` saindo de **um** mapa de páginas — nunca de dois lugares.

**E os COMPONENTES DO MOLDE da seção 32 moram nela, não em cada snippet**, porque a **32.6-b** manda:
*"o que se repete entre páginas (…) vira componente da CASCA"*. São seis: a caixa de resultado, a dobra
`<details>`, o cartão de compra (com **espaço reservado** para quem não tem foto — nenhum registro desta
ilha tem, e a seção 6 diz que perder a recomendação certa por falta de foto é trocar o certo pelo bonito),
o carrossel com `scroll-snap` em CSS puro, a barra fixa do telefone, e o rótulo do botão de loja **por
degrau** da escada da 25.1 — numa função só, porque a seção 8 registra **sete** réguas que quebraram por
procurar o rótulo de um degrau. A **32.5-c** foi obedecida na origem: as regras de telefone do molde
miram a classe `rdm-molde-*`, e as **duas** famílias de página desta ilha (ferramenta e hub) já existem
no primeiro dia, então nenhuma delas nasceu fora do alcance delas.

**A F2** (`snippets/rodametria-f2.php`, 1.0.0), em `/autonomia-patinete-eletrico/`, na ordem da **32.1**
— e a ordem é **conferida por afirmação no fonte**, não lida de olho.

**A F1 NÃO FOI, e isso é decisão registrada.** O limiar legal dela é `pendente` e os cinco domínios
oficiais seguem recusados, remedidos nesta execução. A especificação do bloco 2 já dizia, com todas as
letras: *"A F1 segue sem poder ir ao ar. A F2 e a F3 podem ir ao ar"*. **A F3 também não foi**, e a causa
é de dado: três registros declaram `carga_max_kg` e **nenhum dos três tem oferta aberta** — a conta não
teria o que comparar nem o que vender.

**Daí a home nascer HUB, divergindo do `VOZ.md`, que manda a F1 ser a home.** Home que faz a pergunta do
título e não a responde é pior que home nenhuma. A divergência está escrita **dentro da própria casca**,
no lugar onde quem for mexer a lê, com a saída: no dia em que a resolução for lida, a F1 toma a primeira
tela e os cartões descem — **nenhuma URL muda**, que é o que a 32.3 protege.

---

### 3. A DECISÃO DE ENGENHARIA DO BLOCO: NENHUM NÚMERO E NENHUMA FRASE DE RESPOSTA MORA NO PHP OU NO JS

O caminho é `dados/constantes.json` → `regras/f2.py` (o cérebro) → `ferramentas/gerar-f2.py` →
`dados/f2-respostas.json` → a option que o Sync grava → o PHP → o JS. **O PHP é tradutor e o JS é
preenchedor de molde.** Isso tem um motivo medido e não é elegância: a página responde em **dois** lugares
— o HTML pré-renderizado e a recomputação no navegador — e se cada um escrevesse a própria frase, a página
diria duas coisas diferentes para a mesma entrada **e nenhum portão veria**. É a cicatriz da seção 8 (*"as
duas metades nunca se falavam"*) com um andar a mais: aqui as duas metades são **a mesma página**.

A fronteira da seção 8 foi aplicada nome por nome: o **molde de frase** é fato externo às duas metades e
mora num lugar só; a **decisão** de qual molde vale em cada mundo está escrita duas vezes de propósito
(Python e JS), porque é ali que a divergência ensina algo. E `ferramentas/teste-f2.py` **reescreve a
aritmética à mão em `Fraction`** e lê as constantes do arquivo de constantes — nunca do arquivo que o
gerador escreveu, nem do gerador: quem confere escreve a própria régua.

**A terceira conta que a seção 8 pede** está lá: a razão `97,74 ÷ 41,29` é refeita do zero e comparada
com o fator publicado, e o fator de `misto` é conferido **pelo quadrado** (meio-caminho geométrico), sem
precisar de ponto flutuante.

---

### 4. A BATERIA DE MUTAÇÕES ACHOU UM DEFEITO REAL E TRÊS TRAVAS INERTES — ANTES DO PUSH

**O defeito real foi achado pela mutação que PRODUZ O MUNDO**, e é a regra da seção 8 em estado puro:
*"todo caso que o ESQUEMA permite e o banco ainda não tem é um caso que a régua precisa tratar hoje"*. A
vitrine lia **só** o grupo `nao_declaram_v_ou_ah`, que é o único que o banco de hoje enche. Fabriquei um
registro declarando V, Ah **e** oferta aberta — o mundo que a interseção vazia de 28/10 torna impossível
— e o item caiu em `de_outro_wh` e **desapareceu do bloco de compra**: publicável, com piso, fora da
vitrine. É o **avesso da 25.2**, e ele nunca poderia falhar enquanto o mundo não existisse. A vitrine
passou a varrer os três grupos na **ordem da seção 7** (quem passa em todas as condições antes de quem
falha numa), cada cartão carrega o rótulo do grupo dele, e a bancada ganhou a afirmação de ordem.

**As três travas inertes, as três da mesma família — régua que mede prosa por vizinhança:**
1. A régua da **32.4** (bastidor da fábrica na tela) só olhava linhas com `<p>` literal, e a promessa da
   F2 é `<p class="rdm-promessa">`. A mutação enfiou *"O egresso da nuvem"* na primeira linha da página e
   **passou**. Agora a régua olha `<p` e `<h`.
2. A trava do JS só conferia que os moldes **citados** existiam. Trocar `D.moldes.km_recusa` por um
   literal passava. Agora ela proíbe **prosa** dentro do bloco `<script>` — e a primeira versão dela
   reprovou markup legítimo, que é o erro que a 20.5 nomeia (*"portão que reprova página certa é o
   caminho mais curto para alguém passar a ignorá-lo"*), então ela deixa passar literal com `<` ou `>`.
3. **E ela achou um defeito meu no caminho:** o JS escrevia `'O que esperar no seu trajeto'` e o PHP
   escrevia **a mesma frase** — dois lugares para o mesmo rótulo, no arquivo cujo propósito declarado é
   não ter nenhum. Os dois rótulos viraram molde.

Mais a mutação cujo **alvo exato** não existia: a primeira versão mirava `faixas.plano.degenerada` da
primeira linha da tabela, que é um registro **sem autonomia declarada** — faixa vazia, campo que não
existe. Ela passou medindo nada. A segunda versão **procura** a linha com autonomia declarada em vez de
indexar, e a trava de alvo exato recusa operar se o texto não estiver lá. **8 de 8 mordem.**

---

### 5. OS DOIS DEFEITOS QUE SÓ O AR MOSTROU, E OS DOIS SÃO DA FAMÍLIA DO "VERDE QUE NÃO É ENTREGA"

**(a) A CASCA LIA A OPTION COM O NOME ERRADO.** O Sync grava `rodametria_dados_` +
`sanitize_key(id do manifest)`, e `sanitize_key` **preserva hífen**: a chave é
`rodametria_dados_f2-respostas`. A casca pedia `f2_respostas`, com sublinhado. **O desembarque da revisão
2 ACONTECEU** — três linhas no log do `/status`, as três dizendo `ok`, snippets #6 e #7 criados, option
gravada — e a página caía no estado degradado honesto. **Não havia linha vermelha em lugar nenhum:** nem
erro de PHP, nem falha no log, nem nada no console. É a **20.4** um andar abaixo: ali o Sync não aplica e
diz; aqui ele aplica, diz `ok`, e o que falha é a **leitura** do que foi aplicado. O conserto não foi
trocar a letra: o nome virou constante declarada e a bancada ganhou a afirmação que a confere contra os
ids do manifest, **nas duas direções**, mais a trava que proíbe voltar a digitar o nome na chamada.

**(b) O SITEMAP ERA INVENTÁRIO.** Ele publicava **seis** URLs e **quatro** eram lixo de fábrica do
WordPress — `/2026/10/27/hello-world/`, `/sample-page/`, `/category/uncategorized/` e
`/author/rodametria_gestor/` — contra as duas páginas de verdade, num domínio de **dois dias**. A 14.1 é
literal: *"cada URL fraca gasta orçamento que uma página boa precisaria (…) o sitemap é curadoria, não
inventário"*. A casca 1.1.0 manda as duas páginas de exemplo para a **lixeira** (nunca apaga, casando por
slug **e** por título nas duas línguas, pulando a home e tudo que ela mesma criou — mesmo método da casca
da Robometria) e **remove os provedores de sitemap de autor e de taxonomia**. Quando esta ilha tiver
artigo, quem volta é o provedor de **post**, nunca o de autor.

**(c) E DOIS `<h1>` POR PÁGINA.** O tema de blocos imprime o `post_title` como `<h1>` e o shortcode
imprime o H1 da página. Saiu o do tema, porque o da página é o que a 32.1 põe na ordem certa e o que a
32.3 protege. **H1 duplicado não dá erro em lugar nenhum** — só uma afirmação que **conta** o vê, e é por
isso que o portão de ar conta em vez de procurar.

---

### 5-b. E DEPOIS O PORTÃO DE AR ACHOU OUTROS TRÊS — DOIS DELES CHEGAVAM À TELA **POR DADO**, NÃO POR CÓDIGO

Rodado contra a revisão 6, o `conferir-no-ar.py` reprovou com dois itens, e os dois estavam no **mesmo
campo**: o `fonte` das constantes, que a dobra *"As réguas que a conta usa"* imprime.

**(d) A 32.4 FOI FERIDA POR DADO.** A palavra **"egresso"** — que a 32.4 lista **por nome** entre as
proibidas na página pública — apareceu no texto servido da F2. **Não veio do PHP:** a régua de fonte do
`teste-f2.py` varre o snippet e estava verde. Veio do `fonte` da constante
`energia-wh-tensao-vezes-amperagem`, que diz *"Nao depende de fonte nem de egresso"* — frase **certa** no
arquivo de constantes, que é registro interno, e **proibida na tela**. É a família do número de tela
digitado **com o sinal invertido**: ali o defeito era texto escrito à mão numa metade que não fala com o
banco; aqui é texto do banco indo para a tela **sem ninguém o ler como texto de tela**.

**(e) E NO MESMO CAMPO, O ACENTO.** A seção 8 manda que texto de tela saia acentuado, e os arquivos de
dado desta ilha são **ASCII**. Duas constantes publicavam *"Decisao desta ilha, nao medicao"* na dobra.
Nenhuma régua de PHP veria, pelo mesmo motivo do item (d).

**O conserto é no ponto em que o dado vira texto de tela, não no ponto em que o texto é impresso:** o
gerador passou a ter a **frase de leitor** de cada constante publicada, declarada e acentuada, com o
texto interno preservado no arquivo de constantes — e **recusa publicar** qualquer frase que carregue
palavra de bastidor ou forma portuguesa sem acento. Ele **falha em vez de publicar**. A régua de acento
tem a **lista** das formas que esta ilha produz, e não heurística: heurística sobre acento reprovaria o
título em espanhol da tese de Quito, que é fonte legítima. **4 mutações, 4 mordem.**

**(f) E A PRIMEIRA VERSÃO DA RÉGUA DA 20.4 REPROVAVA ENTREGA CERTA.** Ela lia a **janela inteira** do log
do `/status`, e as quatro linhas `FALHA manifest: HTTP 404` são de **28/10** — de antes de o manifest
existir no repositório, ou seja a história de um defeito já consertado. A 20.4 é literal: *"as linhas da
**revisão corrente**"*. O log é append-only e **sempre** vai carregar o passado. Agora a régua corta na
linha de fecho da revisão corrente, **cobra que essa linha exista** (janela que rolou é entrega não
conferida) e **registra** as falhas antigas como passado, sem reprovar. Régua que reprova entrega certa é
o caminho mais curto para alguém passar a ignorá-la — a lição da 20.5, aqui no sentido oposto ao dela.

---

### 5-c. A 32.5 FOI MEDIDA EM PIXEL, REPROVOU, E PRIMEIRO FOI PRECISO FAZER O PORTÃO EXISTIR NESTA NUVEM

**O portão de navegador não começava, e a causa é a do despacho aberto de `dados/despachos.md`** — *"21
dos 26 portões de navegador do Arquipélago estão inertes nesta nuvem, pela mesma linha de `import`"*.
Medido aqui, numa ilha que não existia quando aquele despacho foi escrito:
`node ferramentas/conferir-32-5-no-navegador.mjs` morria em `ERR_MODULE_NOT_FOUND: Cannot find package
'playwright'`, enquanto `node -e "require('playwright')"` resolvia em
`/opt/node-tools/node_modules/playwright/index.js` **na mesma máquina**. A causa cabe numa frase: **o
playwright desta nuvem é alcançado por `NODE_PATH`, e o resolvedor de ESM não lê `NODE_PATH`** — só o de
CommonJS lê. `createRequire(import.meta.url)` resolve, nenhum `--loader` conserta, e **quem copiar o
portão copia essas três linhas junto**. A nota ficou escrita no despacho, com o que esta execução **não**
fez de propósito: os 21 arquivos das outras duas ilhas, porque `foco.md` nomeia a rodametria e o próprio
despacho diz que o conserto é *"no commit da passada que reservar cada ilha"*.

**COM O PORTÃO VIVO, ELE REPROVOU:** o primeiro botão de compra da F2 estava a **1.730 px** num telefone
de 390 px, contra o teto de **1.400** da 32.5. O formulário passava com folga — **416 px** contra o teto
de 700 —, e é por isso que a 32.5-b insiste em não trocar as duas réguas: medir a caixa de resultado ali
reprovaria uma página certa.

**E A MEDIÇÃO, BLOCO POR BLOCO, DISSE ONDE ESTAVAM OS PIXELS — QUE NÃO ERA ONDE A INTUIÇÃO PUNHA:**

| onde | custo |
|---|---|
| respiro do **tema** entre cabeçalho e trilha | 84 px |
| a frase de promessa, em **quatro** linhas | 144 px |
| o formulário, cinco campos de ~100 px | 521 px |
| a frase de escopo do bloco de compra, em **quatro** linhas | 144 px |
| o espaço reservado da foto, por cartão, **antes** do botão | 96 px |
| a especificação do cartão, em **três** linhas | 77 px |

O corte foi nesses seis lugares e **em nenhum outro**. **Nenhuma palavra saiu da página** (32.3), nenhum
bloco mudou de ordem (32.1) e nenhuma afirmação da bancada mudou — o que mudou foi **densidade no
telefone**. As duas frases encurtadas dizem a mesma coisa com menos linha, e a de escopo mantém o que a
seção 7 exige dela: **a causa de nenhum dos cartões ter entrado pela conta**. O espaço reservado da foto
**continua existindo**, como a seção 6 manda, com 44 px em vez de 96 — porque no telefone esses 52 px são
do espaço mais caro da página.

**E A HOME FICOU FORA DO MOLDE, DITO E NÃO ESCONDIDO.** Ela é HUB: tem caixa de resposta (396 px, dentro
do teto) e **não** tem bloco de compra nem formulário, porque a ferramenta que o `VOZ.md` põe nela é a F1.
Julgá-la pela régua do molde a reprovaria por não ter botão de compra antes de 1.400 px — e a 32.5-b é
explícita em que portão que reprova página certa é o caminho mais curto para alguém passar a ignorá-lo.
Então `tem_molde` passou a ser o **contrato de conversão** (bloco de compra ou formulário de ferramenta), e
a home é **listada fora do molde com o motivo impresso**, que é o que a 32.5-b manda. **Isto é item para o
bloco seguinte, não estado final:** a 32.2 quer produto e ação na primeira tela de página de resposta, e a
home ganha isso no dia em que a F1 puder nascer nela — ou antes, se alguém decidir que o hub também
vende.

---

### 6. OS DOIS PORTÕES NOVOS, E POR QUE ELES NÃO FEREM A 31.2

A **31.2** proíbe portão novo sem defeito medido no ar que ele teria pegado, e a **31.3** proíbe trabalho
de bancada com item de conteúdo aberto. Os dois nasceram aqui **porque a seção 8 os exige por escrito
para publicar**, e os dois pagaram o próprio custo na mesma execução:

- `ferramentas/conferir-no-ar.py` é a lista literal da seção 8 (*"depois de publicar, busque a URL no ar
  e confira com número medido"*) mais a porta de entrada da **29.2**, o log do `/status` **linha por
  linha** da 20.4 com a leitura de cache da **20.5**, e a curadoria do sitemap da 14.1. **Ele achou os
  três defeitos do item 5 acima**, nenhum dos quais aparecia em lugar nenhum.
- `ferramentas/conferir-32-5-no-navegador.mjs` é **cópia do modelo da clubedomosaico**, como a **32.5-b**
  manda com todas as letras (*"quem copiar troca o domínio e os nomes de classe da ilha"*). Trocaram o
  domínio, o prefixo das classes e o seletor do formulário; o cabeçalho conta a história **desta** ilha,
  porque cópia que mantém o motivo da origem envelhece contando o defeito de outro site.

**E a referência saiu de `ferramentas/` para `regras/`** porque a `bancada.py` desta ilha a **denunciou no
dia em que nasceu**: *"ou ele é portão e precisa do prefixo, ou não é e precisa estar fora de
`ferramentas/`"*. Ela não é portão — portão que confere a própria produção é o teste que mede a si mesmo.
`regras/LEIA.md` registra a decisão e o que garante que aquele código roda: o gerador o importa, e a
bancada roda o gerador com `--conferir` em toda passada.

---

### 7. A CONTA DA 31.1 SAIU DE 0 DE 5 PARA 1 DE 6, e o despacho de 28/10 foi reescrito pela 18.3

Os itens **2, 3 e 4** daquele despacho estão fechados — o `pronto quando` do item 3 era **literalmente**
o `curl` que esta execução rodou. Ficou só a conta da 31.1, com o novo número. O piso é 7 em 10, e agora
o caminho para ele é a fila andar: com o canal provado e a casca no ar, **cada bloco da fila pode
terminar em página**, o que não era verdade em nenhuma das cinco execuções anteriores.

---

### O QUE ESTE BLOCO DEIXA PARA O SEGUINTE — e o primeiro item mudou de lugar na fila

**O 3d (o casamento do registro com a oferta) continua sendo o próximo**, e agora com uma razão a mais
que é visível na tela: a F2 no ar diz, com a prestação de contas da seção 7, que **nenhum** dos 17
registros entra pela conta de Wh, e que os quatro da vitrine estão lá com o rótulo *"a ficha não declara a
bateria"*. Isso é honesto e é pouco. O 3d resolve `url_produto` (e com ele o teste de vida da 25.4-b
passa a existir aqui), a **foto** que o cartão do molde pede — hoje os quatro cartões servem espaço
reservado — e o caminho para a ficha onde o campo técnico mora. Leia a **25.7** e a **25.9** antes de
escrever uma linha.

**E duas coisas que esta execução deixou medidas e não fechou, ditas para ninguém as descobrir de novo:**
1. **A 32.5 não foi medida em pixel nesta passada.** O portão existe e está no repositório, mas a
   medição a 390 px num navegador de verdade ficou para a passada seguinte ou para a ronda — e o
   `conferir-no-ar.py` **diz isso como registro** em vez de aprovar em silêncio, que é o que a 32.5-b
   proíbe. Rodá-lo é um comando.
2. **A bateria de mutações da F2 não virou arquivo.** As 8 mutações rodaram nesta execução, de dentro de
   uma passada avulsa, e provaram as travas hoje. Pela 31.2 eu não abri `mutacoes-f2.py` sem defeito no
   ar que o justificasse — mas a seção 8 é clara em que *"mutação que não roda não é trava"*, e mutação
   que rodou uma vez não roda amanhã. **Quando a F2 ganhar o próximo bloco, a bateria vira arquivo**, e o
   defeito medido que a justifica já está escrito no item 4 acima.

---

## 2026-10-28 19h1xZ–19h3xZ — **O PISO DE COMPRA EXISTE: 5 REGISTROS PUBLICÁVEIS, DE ZERO.** E o bloco mediu a coisa que ninguém tinha medido: **o piso e o dado técnico caíram em registros DIFERENTES, e a interseção é VAZIA** — o que destrava a casca não é link, é casamento

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10), e pela 1.2 não há escolha a fazer. A exceção do molde de conversão (32.6) segue **fechada nas três
ilhas**, e nenhuma ilha no ar está quebrada. `executando_desde` da rodametria estava `null` — que pela 1.1
já significa que não havia bloco da Fundação vivo, sem reserva vencida para o git desempatar; o último
commit na pasta da ilha era de **16h41Z**, 2h35 antes. Reserva escrita às **19h16Z**, commit `e34d578`,
push aceito de primeira. Nenhum branch `claude/*` e nenhum PR com commit fora do `main` (o
`claude/dreamy-mccarthy-c0c92n` estava idêntico ao `origin/main`, 0 à frente e 0 atrás).

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA:** `rodametria.com.br` e `www.rodametria.com.br` em **200**, com
`aquametria.com.br` e `robometria.com.br` em 200 na mesma passada. Pela **20.3**, porque este bloco escreve
a regra que exige a fonte: `open-api.affiliate.shopee.com.br` em **200**, `shopee.com.br` em **200**,
`s.shopee.com.br` em **307**. **O egresso da Shopee está aberto para esta ilha** — e isso não estava medido
em execução nenhuma dela.

**CANAL DE DESEMBARQUE SÃO (20.5), embora nada tenha ido ao ar:** `/status` em **revisão 1**, igual ao
`manifest.json`, `ultimo` às **18:40:29** (o cron de 30 minutos está vivo) e **zero linha de FALHA depois
das 13h40**.

---

### POR QUE ESTE BLOCO E NÃO A CASCA — a divergência está escrita porque ela é uma decisão, não um esquecimento

O `bloco_atual` que o bloco 3 deixou dizia *"PRÓXIMO PASSO: a coleta em ficha de FABRICANTE, antes da
casca"*, e a fila do `PROMPT.md` tem o **3b (casca)** como próximo. **Peguei o piso de compra, e a razão é
de contrato, em três passos que se encadeiam:**

1. A **25.2** manda, com todas as letras: *"Todo item ganha `url_busca` ANTES de qualquer outra coisa. Item
   sem `url_busca` é defeito da 19.1, sempre, em qualquer degrau. Não existe item publicável sem piso."*
   Os 24 registros do banco tinham a **mesma** frase em `motivo_do_status`, e ela nomeia esta causa única.
2. A **32.1**, item 5, põe o **BLOCO DE COMPRA imediatamente abaixo do resultado** na página de ferramenta,
   e a **32.5** reprova a página cujo primeiro botão de compra não aparece antes de 1.400 px. Ilha nova
   **nasce** no molde (32.6). Com zero registro publicável, a casca não teria o que pôr ali — o bloco 3b
   não estava apenas em segundo lugar, estava **impossível**.
3. A **18.5** desempata na mesma direção: *"na dúvida entre fechar um despacho e começar um bloco novo,
   fecha o despacho"*, e a 14 põe a indexação como prioridade máxima da ilha nova — o que vale dizer que o
   caminho mais curto para a primeira página no ar passava por aqui.

A coleta em ficha de fabricante **continua sendo o passo caro e necessário**, e este bloco mediu por que
ela ficou ainda mais necessária. Está escrita abaixo, com o alvo apertado.

---

### O QUE ENTROU

**`dados/esquema-banco.json` — versão 2, com a `escada_de_compra`.** A regra da palavra-chave mora no
**esquema**, nunca dentro da régua, pelo mesmo motivo que a lista de níveis mora lá: lista dentro da régua
envelhece calada, e tipo novo entraria sem termo nenhum com o banco verde. O que a seção declara:

- **`termo_de_contexto`** — a palavra que diz *o que o produto é*, na língua do vendedor de marketplace,
  por `tipo_comercial` (VEÍCULO) e por `tipo` (PEÇA). Valor que não está lá **mata a régua**, e há quatro
  mutações que provam isso.
- **A escada de palavra-chave**, do degrau mais específico ao menos: VEÍCULO `marca_modelo_termo` →
  `marca_modelo` → `modelo_termo` → `marca_termo`; PEÇA `marca_termo_medida` → `marca_termo` →
  `termo_medida`. **A peça não leva código de modelo** — lição da Robometria herdada pronta: código de peça
  é SKU interno e o vendedor não o digita no título; o que a peça leva é a **medida de encaixe**, que é como
  ela é vendida.
- **O que nunca compõe:** o termo sozinho (daria a vários registros a MESMA URL), a marca sozinha (a
  armadilha da 25.3), o modelo sozinho, e o `titulo_colhido` inteiro (a 25.6(a) mediu que chave longa
  devolve zero).
- **`sub_id_2` é `null` no piso de REGISTRO, e está escrito por quê:** um registro aparece em mais de uma
  ferramenta — o mesmo patinete responde à F2 e à F3 — e um link carrega **um** `sub_id_2`. Quem o decide é
  a **página**, não o registro; gravar um aqui atribuiria a uma ferramenta o clique que veio de outra, que é
  pior que não atribuir. O piso nasce com `sub_id_1` só, **como o da Robometria**, e o link por ferramenta é
  refinamento da casca.

**`ferramentas/coletar-piso-de-compra.py`** — mede, encurta e grava, com `--gravar` e `--conferir`.
**`ferramentas/mutacoes-piso.py`** — 18 casos (3 mundos que passam, 11 quebras, **4 mortes do esquema**),
mais 10 afirmações sobre a forma da chave e o autoteste da própria bateria. **`ferramentas/validar-banco.py`**
ganhou duas contagens e um aviso novo (o do parágrafo abaixo); ele **já cobrava** a 25.2 e a 25.2-b e não
precisou de uma linha para isso — o portão do bloco 3 estava certo e esperando dado.

---

### A CHAVE É MEDIDA, NUNCA SUPOSTA — e é isso que separa esta régua de um gerador de texto

A 25.6(a) mediu em 16/09 que palavra-chave longa devolve zero e que **zero não é erro**. A busca permite
uma coisa que a ficha não permite: o degrau útil não é o que casa com o registro, é o **em que a loja tem o
que vender**. Então cada degrau desta escada é consultado na Open API (`productOfferV2`) antes de virar
piso, e o número volta gravado em `ofertas_na_medicao` com `medido_em`. **Chave com zero oferta não vira
piso e a escada desce** — um botão que leva a uma página de busca vazia é o beco sem saída que o piso
existe para impedir.

**RESULTADO, 17 registros não excluídos medidos um por um:** **5 com piso** (4 veículos + 1 peça), **12
sem**. E os 12 se separam em duas causas, nenhuma delas "falta coletar":

- **7 não compõem chave nenhuma**, porque o banco não tem os dois identificadores que a escada combina. O
  caso é o do anúncio que empacota três nomes no título (`Bike/Scooter/Moto elétrica`): `tipo_comercial`
  ficou honestamente em `nao_declarado` e com isso **o termo é `null`** — e sem marca **e** modelo não há o
  que compor. **É a 25.9 outra vez, num campo novo:** campo que empacota dois identificadores recusa o
  anúncio certo para sempre. Aqui o anúncio que empacota dois nomes **não dá nem o nome pelo qual ele se
  busca.**
- **5 percorreram a escada inteira e a loja devolveu ZERO em todos os degraus** — `MAXSHOT V1`, `MAXSHOT
  V1SPRO`, `PLAYBIK patinete eletrico`, `Honeywhale H3`, `Haixia scooter eletrica`. Os degraus medidos
  ficaram gravados um por um no `motivo_sem_url_busca`, no formato CAUSA || ÚLTIMA TENTATIVA da 25.4-b.3,
  para a próxima execução não repetir a mesma pergunta às cegas.

**O `sub_id` saiu certo POR CONSTRUÇÃO, e a prova não gastou um clique desta ilha.** A 25.8 é explícita: o
salto do encurtador é onde a Shopee conta o clique, e conferir os links de uma ilha por esse caminho grava
um clique com a etiqueta dela justo na semana em que a leitura semanal procura o **primeiro clique
orgânico**. Então os cinco links desta ilha **não foram abertos**. O mecanismo foi provado uma vez, com
`ferramentas/conferir-sub-id.py` e sub-id de **bancada**: 301, `utm_content` = `bancada-t0---`, campo 1 na
primeira casa. Os links da ilha saem da **mesma** função `encurtar()`.

---

### O ACHADO DO BLOCO, E ELE VALE MAIS QUE OS CINCO LINKS

**O PISO E O DADO TÉCNICO CAÍRAM EM REGISTROS DIFERENTES, E A INTERSEÇÃO É VAZIA.** Dos **4** veículos
publicáveis, **zero** declara tensão + amperagem (a entrada da F2) e **zero** declara carga máxima (a
entrada da F3) — enquanto os **2** registros com Wh derivado e os **3** com carga máxima estão, todos,
entre os 12 **sem** saída de compra.

Não é coincidência, e é por isso que virou **aviso do validador** em vez de frase de registro: o anúncio
que nomeia **marca e modelo** é achável na loja e não publica ficha técnica; o que publica **60 V 20 Ah** ou
**120 kg** empacota três nomes no título e não é achável por nome nenhum. **São duas populações de anúncio,
e o banco herdou as duas.**

**A consequência, escrita para quem for construir a casca:** o bloco de compra da 32.1 pede o produto **que
a ferramenta escolheu**, e hoje **nenhuma das três escolhe um publicável**. Mais piso não conserta isso.
**O que destrava é o CASAMENTO do registro com a oferta** — os degraus 1 a 3 da 25.1 —, porque é ele que
traz a ficha e, com a ficha, o campo técnico. E ele é justamente o casamento das cinco armadilhas da 25.7,
que esta execução **não** fez de propósito: é bloco próprio.

---

### OS DOIS DEFEITOS QUE ESTA PASSADA ACHOU EM SI MESMA, e os dois foram pegos por portão e não por leitura

**(1) O DEGRAU COM NOME MENTIROSO.** A primeira versão de `_juntar()` filtrava as partes vazias e devolvia
o que sobrasse. Com isso o degrau `marca_modelo_termo` de um registro **sem modelo** compunha, na verdade,
`marca_termo` — e era **gravado com o nome errado**. A primeira passada medida imprimiu `playbik` e
`honeywhale-h3` com `marca_modelo_termo`, os dois sem modelo um deles sem termo. **Procedência que mente é
pior que procedência ausente**, porque `degrau_da_palavra_chave` existe exatamente para a execução seguinte
saber por que aquela chave é aquela. Agora o degrau só nasce quando **todas** as partes que o nomeiam
existem, e três afirmações da bateria mordem isso.

**(2) A COLETA PULAVA O REGISTRO EXCLUÍDO E A CONFERÊNCIA NÃO.** `coletar-piso-de-compra.py --conferir`
reprovou o banco em três registros `excluido_do_banco`, cobrando deles o motivo de hoje. Os dois lados
estavam defensáveis e **discordavam**: a coleta os pula porque registro recusado fica gravado para a
próxima execução não o recolher, e a conferência os varria como qualquer outro. O portão reprovou **banco
certo** — que a 32.5-b já nomeou como o caminho mais curto para alguém passar a ignorar um portão. A
conferência passou a pular pela mesma regra, e há um **mundo que tem de passar** na bateria guardando isso.

---

### BANCADA, 0 FALHA — 5 portões, e dois deles nasceram hoje

`validar-banco.py` **APROVADO** com 0 falha e 4 avisos; `mutacoes-banco.py` **APROVADO** com os 66 casos de
ontem intactos (o esquema subiu para a versão 2 e nenhuma morte do esquema mudou de comportamento);
`mutacoes-piso.py` **APROVADO** com 18 casos + composição + autoteste; `coletar-piso-de-compra.py
--conferir` **APROVADO** sem rede; `derivar-banco.py --conferir` **APROVADO**. A bancada **descobriu** os
dois portões novos pela convenção de nome, sem ninguém os listar — que é a razão pela qual esta ilha nasceu
com ela.

---

### A SEÇÃO 31 LIDA EM VOZ ALTA, porque ela desaprova parte do que entrou aqui e isso não se esconde

A **31.1** pede que 7 de cada 10 execuções de uma ilha entreguem algo **no ar que o visitante vê**, e a
**31.2** diz que portão, régua ou mutação nova *"só nasce quando existe defeito medido no ar que ela teria
pegado"*. **Esta execução não entregou nada no ar e escreveu uma bateria nova.** Os dois fatos ficam
registrados, e com eles o que penso deles:

- **Nenhuma execução desta ilha pode satisfazer a 31.1 hoje**, porque a ilha tem **zero** URL. A 31 nasceu
  em 21/10 de um problema oposto e nomeado: a aquametria, **com 52 URLs no ar e 586 impressões na semana**,
  gastando execução em bancada. A proporção da 31.1 passa a ser mensurável nesta ilha no dia em que a casca
  subir — e a 31.6 manda a leitura semanal contá-la, com o `REGISTRO.md` na mão.
- **A bateria nova não é trabalho de bancada sobre portão existente** (o que a 31.3 proíbe): é a bateria de
  uma régua que nasceu nesta mesma execução, e o `PROMPT.md` desta ilha já declarava a prática, com a causa
  — *"Esta ilha nasceu com a bancada, em vez de ganhá-la depois de perder uma régua"*. **E ela mordeu na
  própria passada:** os dois defeitos da seção acima foram achados por portão, não por leitura, e um deles
  (o degrau com nome mentiroso) teria ido para o `main` gravado em cinco registros.

---

### NADA FOI AO AR, E NADA PODIA

O `manifest.json` segue na **revisão 1** com os três grupos vazios: esta ilha não tem página nenhuma, e a
primeira revisão que publica algo continua sendo a da **casca (bloco 3b)**. `publicar` segue `false` nos
arquivos de dados — eles alimentam ferramenta, não são página.

**PRÓXIMO PASSO DESBLOQUEADO: o CASAMENTO do registro com a oferta da Shopee (degraus 1 a 3 da 25.1).** É
ele que resolve as duas pontas de uma vez — dá `url_produto` (e com ela o teste de vida da 25.4-b passa a
existir nesta ilha), dá a foto que a 32.1 pede no cartão, e dá o caminho para a ficha onde o campo técnico
mora. **E ele é o casamento das cinco armadilhas da 25.7**, que precisam ser lidas antes de uma linha ser
escrita. O alvo apertado, saindo da medição de hoje e não de impressão: os **7** registros que não compõem
chave e os **5** que a loja não respondeu — e os **12** sem saída de compra que incluem todo o dado técnico
que o banco tem.

## 2026-10-28 16h4xZ — **BLOCO 3 ENTREGUE: O MODELO DO BANCO.** O esquema, 24 registros, três portões e a bancada — e o número que o bloco mediu vale mais que o esquema: **zero veículo com potência nominal declarada, contra 14 com um watt sem rótulo**

**A ESCOLHA DA ILHA, dita antes de qualquer coisa.** `foco.md` nomeia a **rodametria** (foco total e
absoluto, decisão do Raphael de 27/10), e pela 1.2 não há escolha a fazer. Conferi as duas exceções que
furariam o foco: o **despacho do molde de conversão** (32.6) está **FECHADO nas três ilhas** — aquametria
em 21/10 às 18h2xZ, clubedomosaico em 21/10 às 19h1xZ, robometria em 21/10 às 16h1xZ —, e o **item 1
(ALTA) do despacho da Sentinela de 28/10 na clubedomosaico** não fura: a 1.2 exige ilha no ar **E
QUEBRADA** (página servindo erro, ferramenta devolvendo número errado, site fora do ar), e a própria ronda
registra, com todas as letras, *"A RÉGUA TÉCNICA PASSOU INTEIRA"* — 32 de 32 em 200, as duas ferramentas
conferidas com entrada inédita e a conta refeita na mão. O que o item 1 descreve é dívida de receita, não
ilha quebrada. **`executando_desde` da rodametria estava `null`, que pela 1.1 já significa que não havia
bloco da Fundação vivo** — não houve reserva vencida para o git desempatar. Reserva escrita às **16h19Z**,
commit `4a14f00`, push aceito de primeira. Nenhum branch `claude/*` e nenhum PR aberto (`list_pull_requests`
em aberto devolveu vazio), e o `main` local estava idêntico ao `origin/main`.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA:** `https://rodametria.com.br/` e `/wp-sitemap.xml` os dois em
**200 nas três passadas**.

---

### O QUE ENTROU

`dados/esquema-banco.json` — o contrato, **versão 1**, com três entidades, a escada de fontes de oito
níveis, a regra de divergência por campo, a lista de campos que exigem procedência de leitura e os grupos
de prestação de contas das três ferramentas. `dados/veiculos.json` (**17** registros), `dados/pecas.json`
(**3**), `dados/municipios.json` (**4**). Os portões: `ferramentas/validar-banco.py`,
`ferramentas/derivar-banco.py` (quem **escreve** `energia_wh`, separado de quem o **confere**, de propósito
— a segunda metade existe para discordar da primeira) e `ferramentas/mutacoes-banco.py`. Mais
`ferramentas/bancada.py`, que descobre os portões em vez de os listar.

**OS 24 REGISTROS SAÍRAM SÓ DO QUE JÁ ESTAVA COLHIDO NO REPOSITÓRIO** — `dados/corpus-buscas.md` (bloco 1),
a tabela 1.6 de `dados/especificacao-calculadoras.md` (bloco 2) e a seção (c) de
`bussola/dossies/rodametria/DOSSIE.md` (Bússola, 27/10). **Nenhuma rede foi tocada para montá-los e nenhum
número foi digitado de cabeça.** Modelo de banco sem registro nenhum é hipótese: o que prova um esquema é
ele aplicado a dado real, e foi a aplicação que achou tudo o que está abaixo.

**NENHUM REGISTRO É `publicavel`, e a causa é UMA SÓ:** ninguém tem saída de compra, e a 25.2 não admite
item publicável sem piso. Está em cada `motivo_do_status`, com a mesma frase. **Nada foi ao ar e nada
podia:** o `manifest.json` segue na **revisão 1** com os três grupos vazios. Conferi o canal de qualquer
jeito, porque ele nasceu hoje e vinha falhando: `/status` em **revisão 1**, igual ao `manifest.json`,
`ultimo` em **16:13:31** e **zero linha de FALHA** depois das 13h40 — o cron de 30 minutos está vivo e o
canal está são. Pela 20.5, revisão igual com log de agora é o estado certo, não cache.

### BANCADA, 0 FALHA

`bancada.py` rodou os três portões sem rede: `validar-banco.py` **APROVADO**,
`derivar-banco.py --conferir` **APROVADO** (todo `energia_wh` do banco bate com V × Ah),
`mutacoes-banco.py` **APROVADO** com **66 casos** — **4 mundos que têm de passar** (o banco de hoje, o
banco **vazio**, um registro publicável completo no degrau 3 com par colhido, e um no degrau 4 com `url`
vazia) e **62 quebras**, cada uma declarando no próprio caso o **pedaço da frase** que espera ouvir de
volta. Mutação que aceita qualquer reprovação passa quando o portão reprova pelo motivo errado, e duas
delas reprovaram assim na primeira rodada — as duas eram expectativa minha escrita com desleixo, e a
bateria as pegou. **Mais o autoteste da bateria:** um validador de mentira, que aprova tudo, tem de fazer
a bateria reprovar. Sem isso, bateria quebrada diz `0 falha(s)` e ninguém sabe.

**Sete das 62 são MORTES DO ESQUEMA (26.2), e elas não estragam registro nenhum:** apagam uma chave **do
esquema** e exigem que o portão **MORRA**, nunca que aprove em silêncio. Régua que lê a própria lista de um
arquivo de dados aprova tudo, calada, no dia em que o arquivo perder a chave. A mais instrutiva é a da
sentinela: apagando `valor_sentinela_de_ausencia` do esquema, **o banco de HOJE passa a reprovar** — o que
prova que aquela linha do esquema sustenta peso, e não é decoração.

**E a bancada tem régua própria, medida no dia em que nasceu:** com um portão inerte de mentira (imprime
`REPROVADO` e sai 0) e um arquivo sem convenção de nome, ela denunciou os dois e fechou **REPROVADO**.
Removidos depois.

---

### O ACHADO DO BLOCO, E ELE É UM NÚMERO: **`veiculos_com_nominal_declarado` = 0, CONTRA 14 COM UM WATT SEM RÓTULO**

O `PROMPT.md` desta ilha já dizia a regra: *"anúncio que só diz '1000W' no título não alimenta a F1 sem a
ficha dizer qual dos dois é"*. Era uma regra. **Aplicada aos 17 registros, virou uma medição**, e a medição
é mais dura do que a regra soava: **das 17 fontes colhidas, nenhuma declara se o watt é nominal ou de pico.**
Nem a ficha do Extra, nem a das Casas Bahia, nem o painel da Shopee, nem o do Mercado Livre.

**O que isso muda no plano, e muda de verdade:** a F1 **não tem candidato nenhum na vitrine nem no dia em
que os limiares da Contran chegarem**. O despacho ALTA de 28/10 destrava a *fórmula*; ele não destrava a
*entrada*. O que falta além da resolução é a **ficha que diz qual dos dois watts é o nominal** — nível 4 da
escada (`ficha-do-fabricante-lida`), hoje **vazio**, porque nenhum domínio de fabricante desta ilha foi
tentado por execução nenhuma. **Isto é trabalho de coleta, não de ferramenta**, e é o próximo passo
desbloqueado mais caro da ilha.

**E A TABELA 1.6 DA ESPECIFICAÇÃO TEM UMA COLUNA QUE PROMETE MAIS DO QUE AS FONTES DERAM — ERRATA.** Ela
tabula sete veículos sob o cabeçalho **"W nominal"**. Nenhuma das sete fontes usa a palavra *nominal*: o que
cada uma publica é um watt só, sem rótulo. A coluna não está errada nos números; está errada no **nome**, e
o nome é justamente a distinção que esta ilha vende. No banco, os mesmos números moram em
`potencia_declarada_sem_rotulo_w`, e `potencia_nominal_w` está null com motivo nos 17. **A errata fica aqui
e não reescreve a especificação:** a tabela é registro do que o bloco 2 leu, e o banco é o contrato do que
a ferramenta pode usar — quem construir a F1 lê o banco.

### AS TRÊS COISAS QUE O ESQUEMA ACRESCENTOU À LISTA DO `PROMPT.md`, e as três nasceram de aplicar a lista a dado real

**(1) A ENTIDADE `MUNICIPIO`.** A lista do bloco 3 pede VEÍCULO e PEÇA, e é **anterior** à especificação do
bloco 2 — que deu à F1 **quatro** entradas e fez a quarta ter **três** estados de saída, sendo o do meio
*"município preenchido e conhecido pelo banco"*. Esse estado precisa de um banco de municípios que ninguém
havia mandado existir; sem ele, a F1 cairia na ressalva genérica fingindo que essa é a única resposta
possível. A camada 2 da F1 é **dado**, não prosa de rodapé.

**(2) `potencia_declarada_sem_rotulo_w`.** Ver o achado acima. O esquema nasceu com dois campos de potência
e a montagem dos registros mostrou que o mundo tem **três** estados, não dois.

**(3) `cotacoes[]` como SÉRIE**, no lugar de "preço com data" como campo. Leitura nova não substitui leitura
velha: substituir apaga a série, que é a única coisa capaz de mostrar que o anúncio de R$ 2.299 de 27/10
virou outro número. É a lição que a Robometria escreveu no esquema dela, aqui como array dentro do registro
em vez de entidade separada — com 24 registros, o custo de um arquivo a mais não se paga ainda.

### A DECISÃO DE ENGENHARIA DO BLOCO: **SEVERIDADE DE FONTE É POR CAMPO, PELA ASSIMETRIA DE CUSTO — NÃO UMA LINHA SÓ PARA O REGISTRO INTEIRO**

A primeira versão da escada dizia, como a da Robometria, que os níveis 6, 7 e 8 **não sustentam campo
técnico nenhum**. Aplicada ao banco, ela **reprovava campo certo**: o Wh da F2 é `V × Ah`, identidade
matemática, e o anúncio que escreve *"60 V 20 Ah"* no título está **declarando a bateria**, não prometendo
desempenho. Errar ali custa uma faixa de km mais larga; errar na categoria legal manda alguém para a rua
sem habilitação. **São erros de preço diferente, e a seção 10 manda a direção sair da assimetria de custo.**

Então o esquema ganhou `niveis_minimos_por_campo`: **nível 5 ou melhor** (ficha de varejo grande) em
`potencia_nominal_w`, `velocidade_max_kmh`, `acelerador` e `carga_max_kg` — os três primeiros são as
entradas da F1, e o quarto é a 3.5 da especificação (*"não estima carga máxima de veículo que não a
declara"*); **nível 6 aceito** em `tensao_v`, `amperagem_ah`, `autonomia_declarada_km`, `aro`, `peso_kg` e
nos dois campos de potência que não classificam; **nível 8 não sustenta nada**, em nenhum campo.

**O resultado prático:** a F2 e a F3 têm candidato real no dia um (2 veículos com Wh derivado de V e Ah
declarados, 3 com carga máxima de ficha), e a F1 tem zero — **cada um pelo seu motivo, escrito.** Portão
que reprova campo certo é o caminho mais curto para alguém passar a ignorá-lo, e é a mesma lição que a
20.5 nomeou quando o "REPROVADO" era cache.

### O SEGUNDO ACHADO, E ELE VEIO DA PRIMEIRA RODADA DO PRÓPRIO VALIDADOR: **O PIVÔ DA F1 QUEBRA A INVARIANTE DE PROCEDÊNCIA, E QUEBRA COM RAZÃO**

Todo campo deste banco obedece a "valor presente ⇒ procedência presente": com valor, exige-se `fonte`,
`declarado_como` (o texto **literal** da fonte) e, nos dois campos da 26.1, `declarada_por`. O `acelerador`
é um enum de **três** valores em que o terceiro, `nao_declarado`, **tem como conteúdo a própria ausência de
declaração** — cobrar dele o texto literal é cobrar o literal de uma frase que não existe. A primeira
rodada reprovou **40 vezes** por isso, em registro certo.

**A regra que nasceu:** o esquema declara `valor_sentinela_de_ausencia` no campo, e a sentinela **exige
`fonte`** (onde se olhou) e **`motivo`** (por que não se achou) e **dispensa** `declarado_como` e
`declarada_por`. O nome da sentinela mora **no esquema**, não dentro do validador: o dia em que outro campo
ganhar sentinela, ele a declara numa linha e a trava passa a tratá-la sem código novo (26.2). E a sentinela
nunca dispensa o registro de nada mais — ela é um valor, conta nos grupos de prestação de contas, e **nunca
cai no lado "só pedal assistido" por omissão**.

**E a mesma rodada achou um defeito de verdade no dado**, não na régua: **dois registros nasceram com o
pivô da F1 em `null`** (`patinete-adulto-com-banco-shopee` e `playbik`), porque o construtor caiu no padrão
de "campo não colhido" num campo que **não aceita nulo**. Os dois foram consertados para a sentinela, com
`fonte` e `motivo`. Foi o portão pegando o autor do portão na mesma passada — que é exatamente para isso
que ele existe.

### A MEDIÇÃO DA 20.3, QUE É DEVER DE QUEM ESCREVE A REGRA: **OS QUATRO DOMÍNIOS DE PREFEITURA ESTÃO RECUSADOS**

Escrevi no esquema que o nível 3 exige **o ato lido no domínio `.gov.br` do município** — então pela 20.3 a
medição é minha. Às 16h3xZ, nas três passadas da 20.2: `www.campinas.sp.gov.br`, `www.rio.rj.gov.br`,
`www.joinville.sc.gov.br` e `www.sjc.sp.gov.br` em **000 nas três**, com `rodametria.com.br` e
`aquametria.com.br` em **200 nas mesmas três**. **12 medições de bloqueio contra 6 de controle verde, zero
intermitência**, com o egresso respondendo `connect_rejected` — recusa de política, não queda de host. **É
a mesma parede do despacho ALTA de hoje:** o que esta ilha não alcança não é um site, é o domínio
`.gov.br`.

Os quatro municípios são `pendente`, e a consequência está escrita sem maquiar no próprio arquivo: **hoje a
camada 2 da F1 tem DUAS saídas em vez de três, e as duas imprimem a mesma frase genérica.** A diferença
entre isso e um buraco é que isso está contado, com a causa e com o nome dos quatro domínios. **Despacho
NORMAL novo** em `dados/despachos.md`, com o pedido nas duas formas — e a forma (a) dele é uma linha só,
`*.gov.br`, que fecha **os dois despachos de hoje** de uma vez.

E a nota de método, porque ela se repetiu dentro da mesma execução: a primeira versão do `municipios.json`
dizia *"os quatro domínios que ninguém tentou"*. **Essa frase ficou velha na execução que a escreveu**, e a
nova é pior: não é que ninguém tentou — é que não dá. É a família do bloqueio herdado do `ESTADO.md` lido
como fato (20.2), com três horas de vida em vez de três dias.

### O QUE MAIS O ESQUEMA DECIDIU, em uma linha cada

- **`tipo_comercial` e `categoria` são enums DISJUNTOS**, e o validador reprova se passarem a compartilhar
  um valor. "Scooter" não é categoria da resolução, e o esquema faz com que não exista **como** gravá-la.
- **`categoria` é null nos 17, por força da constante**, e o validador lê o **status da constante** em
  `constantes.json` — não uma lista escrita dentro dele. Com o limiar `pendente`, categoria preenchida é
  reprovação com a frase *"o anúncio escrevendo a regra"*.
- **A divergência resolve para o lado RESTRITIVO** nesta ilha — oposto da Aquametria (que resolve pelo
  maior) e mesma direção da Robometria (que resolve pelo mais estreito). O erro caro aqui é o permissivo.
- **Três registros nasceram `excluido_do_banco` com a causa escrita** — dois títulos de anúncio sem marca e
  sem modelo, e um item cuja única fonte é nível 8. Recusa que não se escreve é recusa que a próxima coleta
  repete.
- **A prestação de contas da seção 7 é conferida como invariante**, não como intenção: o validador avalia
  os grupos das três ferramentas sobre **todo** registro e reprova se algum cair em zero ou em dois grupos.
  Com zero publicáveis ela é **verdadeira por vacuidade**, e o validador diz isso como **AVISO** — registro,
  nunca aprovação, na mesma família da janela de 15 linhas da 20.4.

### PRÓXIMO PASSO DESBLOQUEADO

**O bloco 3b (casca) depende do WordPress e ele está no ar**; o que o bloco 3 deixa pronto para ele é o
banco de onde a vitrine sai e a dívida da 26.3 nomeada (a frase da tela que lê `declarada_por` e escolhe a
atribuição — ela é da casca, não do banco). **Mas o passo que vale mais não é a casca: é a COLETA EM FICHA
DE FABRICANTE**, pelos dois números que este bloco mediu — 0 de 17 com potência nominal declarada e nível 4
da escada vazio. Sem ele a F1 fica sem entrada mesmo com a resolução na mão, e a F1 é a home desta ilha. O
primeiro passo dessa coleta é de um comando e é a 20.3 outra vez: **medir o egresso contra os domínios dos
fabricantes antes de escrever regra que os exija.**

---

## 2026-10-28 13h5xZ — **ADENDO À MESMA EXECUÇÃO: O SYNC DA ILHA NASCEU HOJE E ESTAVA FALHANDO EM SILÊNCIO.** A seção 4 **ao contrário** — não foi o site que ficou para trás, foi o repositório

**Achado fora do bloco, na conferência de fecho.** Às 10h17Z desta mesma manhã a execução
do bloco 1 mediu `/wp-json/rodametria/v1/status` em **404** e escreveu no `PROMPT.md` que *"o
snippet de Sync não existe ainda"*. Às **13h2xZ** o mesmo endereço devolve **200**, com
`versao_sync: 1.1.5`. **O passo 8 da seção 11 foi feito pelo Raphael entre as duas
medições**, e nem o `ESTADO.md`, nem o `PROMPT.md`, nem o despacho sabiam.

**E o canal não estava só desconhecido: estava FALHANDO, de 30 em 30 minutos.** O que o
`/status` trazia:

```
revisao: -1
2026-10-28 13:10 FALHA manifest: HTTP 404 em manifest.json
2026-10-28 12:48 FALHA manifest: HTTP 404 em manifest.json
2026-10-28 12:30 FALHA manifest: HTTP 404 em manifest.json
2026-10-28 11:48 FALHA manifest: HTTP 404 em manifest.json
```

O cron próprio da ilha (`rodametria_30min`) vinha pedindo
`raw.githubusercontent.com/rmnatal/arquipelago/main/ilhas/rodametria/manifest.json` **desde
as 11h48Z**, e o arquivo não existia no repositório. **É a seção 4 virada do avesso:** o
contrato existe para o caso de o site andar e o cabeçalho ficar para trás; aqui o **canal de
desembarque** estava de pé, batendo na porta, e o lado do repositório estava mudo.

**O QUE FOI FEITO, e por que não publica nada.** Nasceu
`ilhas/rodametria/manifest.json` na **revisão 1**, com os **três grupos vazios**
(`snippets`, `conteudo`, `dados`). **Verificado contra o código do Sync** antes de escrever —
`ilhas/robometria/snippets/robometria-sync.php`, que é o mesmo código nas ilhas: o Sync exige
`revisao` e um array, pula grupo vazio sem erro, e o portão de publicação é o `publicar:
true` de **cada item** (`desembarque.aprovado` ele **não lê** — é documentação para gente).
Com zero item, ele aplica zero, pula zero e grava a revisão.

**As duas coisas que isso compra, as duas baratas:**
1. **O log do `/status` para de encher de FALHA** — e ele é uma **janela de 15 linhas** (20.4).
   No dia do primeiro desembarque de verdade, a janela estaria cheia de ruído, e *"item que
   rolou para fora da janela não foi conferido"*.
2. **O caminho fica provado ponta a ponta com NADA em jogo:** `raw.githubusercontent.com` →
   `wp_remote_get` do Sync → `json_decode` → revisão gravada → `/status` público. Se a
   constante `RODAMETRIA_SYNC_BASE`, o caminho ou o cron estiverem errados, **descobre-se
   hoje, com zero página no ar**, e não no dia em que a F1 for ao ar. É a mesma família do
   passo 20.1: *"casca no ar que não pode ser verificada é pior que casca inexistente"*.

**VERIFICADO NO AR PELA 18.4 E PELA 20.4, e o critério de pronto era declarado antes.** O
cron da ilha rodou às **13h40:03Z** e o `/status` virou:

```
revisao: 1   ultimo: 2026-10-28 13:40:03
2026-10-28 13:40 revisão 1: 0 aplicado(s), 0 aguardando desembarque
2026-10-28 13:10 FALHA manifest: HTTP 404 em manifest.json     <- a última falha
```

**É exatamente o previsto, item por item:** zero aplicado (não havia o que publicar), zero
aguardando desembarque (não havia item com `publicar: false`), e a linha da revisão corrente
**não é FALHA** — que é o que a 20.4 manda conferir. As quatro falhas pararam. **O canal de
desembarque da rodametria está provado ponta a ponta**, e a primeira revisão que publicar
algo vai encontrar um log limpo em vez de uma janela cheia de ruído.

Entre o push e o `/status` subir passaram **~4 minutos**, com `raw.githubusercontent.com` já
servindo a revisão 1 desde o primeiro minuto — a **20.5** em estado puro, e aqui ela não era
cache e sim o cron esperando a hora dele (o evento de 30 minutos venceu às 13h40, depois do
de 13h10). Quem vier depois: `wp-cron.php` chamado à mão **não antecipa** evento que ainda
não venceu, e devolve **409** quando o cron já está travado.

**E os endpoints do `PROMPT.md` deixaram de ser placeholder.** Eles estavam em
`<preencher quando o snippet Rodametria Sync existir>` **com o snippet no ar**, e o passo 8
da seção 11 diz, com todas as letras, que **sem eles a seção 4 não é executável**. Agora
trazem o `/status`, o `/sync`, o gatilho por query, a base do `raw` e a ressalva da **20.5**
(revisão atrasada logo depois do push é cache do GitHub, não defeito). **O token não está no
repositório e não deve estar** — e a Fundação não precisa dele: o cron de 30 minutos é o que
desembarca.

## 2026-10-28 13h19Z–13h4xZ — **O BLOCO 2, E A DECISÃO DE ENGENHARIA QUE TIRA A ILHA DA ESPERA.** As três ferramentas especificadas inteiras, 9 constantes com procedência — e o limiar legal que a F1 não tem **isolado num objeto JSON**, para a chegada da fonte ser a edição de um arquivo e não um bloco

**O que saiu:** `dados/especificacao-calculadoras.md` (470 linhas) e
`dados/constantes.json` (**9 constantes**: 6 publicáveis, 2 `pendente` com a consequência
declarada, 1 observação de mercado). Para cada uma das três ferramentas: entradas com tipo
e exemplo pré-preenchido, saída, fórmula degrau por degrau, **o que ela se recusa a
responder**, tabela pré-renderizada, bloco de compra com o critério de entrada do produto,
e a prestação de contas da seção 7 com os grupos de recusa separados por causa.
`publicar: false` nos dois, como todo bloco de dado.

**A DECISÃO DO BLOCO, e ela é o que fica depois de hoje.** A ilha estava numa armadilha
simples: a F1 **é** a home, o produto dela **é** a categoria legal, e o texto que decide a
categoria é negado pelo egresso há duas execuções. A saída não foi esperar nem improvisar
um número — foi **separar o que depende da fonte do que não depende**. Os quatro limiares
(`LIMIAR_BIKE_W`, `LIMIAR_BIKE_KMH`, `LIMIAR_AUTOPROP_W`, `LIMIAR_AUTOPROP_KMH`) viraram
**uma constante só**, referenciada **por nome** na árvore de decisão, com **literal
numérico proibido** no código da F1. A árvore inteira, as duas ressalvas obrigatórias, a
camada municipal, o bloco de compra e o esquema do banco estão escritos e podem ser
construídos. **Quando o texto oficial chegar, a F1 destrava editando um objeto JSON** —
preencher `valor`, trocar `status`, gravar `url` e `verificado_em`. Nenhuma linha de lógica
muda. *É por isso que este bloco não esperou a fonte: o que a fonte decide é um objeto, e o
que ela não decide é tudo o mais.*

**O QUE CONTINUA TRAVADO, remedido e não herdado do campo.** Às 13h2xZ, em duas passadas:
`gov.br`, `in.gov.br`, `planalto.gov.br`, `contran.gov.br` e `lex.com.br` — **os cinco** em
`CONNECT tunnel failed, response 403`, com `rodametria.com.br` em **200** na mesma janela.
Três horas e meia depois do despacho ALTA do bloco 1, o pedido segue aberto. **A F1 não vai
ao ar**, e não vai com número de portal, não vai com o número que mais apareceu e não vai
"com ressalva" — a seção 10 proíbe constante `pendente` dentro de fórmula publicada, e aqui
a fórmula publicada é o produto da ilha. **A F2 e a F3 podem ir ao ar.**

**A ERRATA DO BLOCO 1, e ela é a razão de um despacho novo existir.** O corpus entregou à F2
*"a régua do relevo com número: 41,29 Wh/km em plano × 97,74 Wh/km a 12%"* e calculou com
ela sobre **1.200 Wh**, uma bateria de patinete. A coleta limpa de hoje achou o registro do
estudo: *"Análisis de la eficiencia energética de la batería de ion litio en una **moto
eléctrica** para el uso de micro movilidad"* — Rodrigo David Limaico Quinteros, Maestría en
Ingeniería Automotriz, UPS sede Quito, **2025**, bateria de **60 V e 30 Ah (1.800 Wh)**,
rota de **25,8 km**. **Wh/km absoluto de uma moto de 1.800 Wh não é o de um patinete de 500
Wh.** O que virou constante foi a **razão** — `97,74 ÷ 41,29 = 2,37` —, medida na mesma
rota, com o mesmo veículo e a mesma bateria, que é a única forma de um número atravessar
classe de veículo. A errata está escrita **nos dois lugares do corpus** que carregavam a
frase, com o original riscado e preservado.

**E a mesma tese deu de graça o número que faltava:** **29,8 km medidos em condição mista
contra 60 km declarados na ficha — 49,7%**. O corpus registrava *"60% a 80% do valor
anunciado"* como leitura agregada sem fonte única, e dizia ele mesmo que não servia de
constante. **A medição nomeada cai abaixo do piso daquela faixa**, e é a direção que
importa: a faixa agregada era otimista. Entra como **linha de calibração** da tabela da F2,
com autor e instituição dentro da frase, e **não** multiplica nada.

**A TERCEIRA COISA QUE A COLETA LIMPA FEZ FOI REBAIXAR UM NÚMERO DA PRÓPRIA ILHA.** O bloco
1 anotou que *"uma fonte estrangeira colhida sugere margem de pelo menos 10% acima do peso
do condutor"*, e a F3 ia nascer com essa margem atribuída a terceiro. A busca limpa — sem o
número dentro da pergunta — percorreu 13 publicadores e **não achou percentual publicado em
nenhum**. O que existe publicado é **qualitativo e convergente** em três deles, um
brasileiro: perto do teto declarado, a velocidade e a aceleração máximas não são
alcançadas. **Então a margem de 10% virou `decisao_da_ilha`, com o motivo escrito** — a
direção do erro caro aponta para a folga —, e a página nunca a atribui a ninguém. *Atribuir
a terceiro uma régua que terceiro não publicou é pior que não ter régua.* E o número não é
cosmético: 10% sobre o teto de mercado de 120 kg exclui quem passa de **109 kg**, que é
exatamente a pessoa do `VOZ.md`.

**O que a F2 deixou de poder fazer, e fica dito em vez de disfarçado:** sem régua de consumo
por km de **patinete**, ela não devolve km absoluto a partir de V e Ah. Devolve `Wh = V × Ah`
(identidade, não precisa de fonte nenhuma), a faixa degradando a autonomia **declarada** pelo
fator de relevo, e — quando a pessoa não informa a declarada — **diz que não estima km,
nomeando o que falta**. A única medição de patinete que existe (≈ 20 Wh/km, 4.000 km rodados,
70 ciclos) está em dois hosts que não resolvem nesta nuvem. Os outros três candidatos foram
reprovados **com o motivo escrito um por um** em `constantes.json`: um é de bicicleta e de
fabricante de kit, um é circular (divide a autonomia declarada pela energia, assumindo
justamente o número que a F2 existe para não assumir), e um é de moto.

**Despacho novo, prioridade NORMAL** (`dados/despachos.md`): três domínios —
`stdjet.scienceandtechnology.com.vn`, `et.vnuhcmjournal.com.vn` e `dspace.ups.edu.ec` — ou a
leitura no Chrome. **É NORMAL e não ALTA de propósito: ele melhora a F2, não a libera.** O
terceiro domínio é o mais barato dos três: ele sobe de "leitura por busca" para leitura
direta as **duas constantes publicáveis** que esta execução já gravou.

**Próximo passo desbloqueado — bloco 3, modelo do banco, e ele não depende de site NEM de
fonte bloqueada.** A seção 5 da especificação já entrega o contrato: os campos que as três
ferramentas leem, `potencia_nominal_w` e `potencia_pico_w` **separados** (a F1 só lê o
nominal), **`acelerador` como enum de TRÊS valores** — `nao_declarado` é o terceiro, com
frase própria, e **nunca** cai em "só pedal assistido" por omissão, porque é o pivô da
classificação —, `energia_wh` **derivado** de V × Ah e nunca copiado de anúncio, e
**`categoria` como campo DERIVADO da F1, nunca de entrada do catálogo**: gravar categoria à
mão é deixar o anúncio escrever a regra.

## 2026-10-28 10h17Z–10h25Z — **O BLOCO 1, E AS DUAS COISAS QUE ELE ACHOU SEM PROCURAR.** Primeira execução da Fundação nesta ilha. O corpus de buscas saiu inteiro, a **S_par deixou de ser "não medida"** — e no caminho a passada descobriu que **o site já está no ar** e que **a fonte que decide a F1 é negada pelo egresso**

**O que saiu:** `dados/corpus-buscas.md` — quatro eixos (CNH e placa · autonomia ·
carga e tamanho · produto pelo nome), **19 consultas** com procedência medida consulta a
consulta pela busca da nuvem em 28/10, seis achados nomeados, a contagem do vazamento da
busca **por eixo** e a seção 6 com o que o bloco 2 herda pronto. `publicar: false`, como
todo bloco de dado.

**A S_par ESTAVA NO DOSSIÊ COMO "NÃO MEDIDA" E ERA A PRIMEIRA TAREFA DE LEITURA DO
NASCIMENTO. Está medida, e o resultado é mais útil que "aberta" ou "fechada":** o eixo da
CNH está **tomado**, mas por **portal de trânsito e notícia** — `portaldotransito`,
`olhardigital`, `canaltech`, `motonline`, `consultadeplaca`, `doutormultas`, `gringo`,
`zuldigital`, mais folheto de duas prefeituras e PDF de duas entidades. **Nenhum varejo
grande, nenhuma loja, e em sete consultas independentes NENHUMA ferramenta** que receba
potência e velocidade e devolva a categoria. A vaga da F1 não é "ninguém fala disso": é
**"todos falam, ninguém calcula"**.

**E O MOTIVO PELO QUAL A PROSA NÃO RESOLVE É O ACHADO QUE SUSTENTA A ILHA: AS FONTES SE
CONTRADIZEM NO NÚMERO.** Três limites diferentes para a mesma pergunta, todos em fontes
que se apresentam como quem sabe — **350 W / 25 km/h** (que é regra **do Rio**, apresentada
como nacional), **1.000 W / 32 km/h** (nacional) e **4 kW / 50 km/h** (ciclomotor, sem
citar o de 1.000 W) — e uma fonte de primeira página afirmando **CNH categoria A** para
bicicleta elétrica, o contrário de todas as outras. O desacordo não é de tom: é de número,
e é o número que decide se a pessoa sai de casa habilitada.

**Os três achados que amarram a ilha, e os dois primeiros estão em título de loja grande:**
- *"**Bicicleta elétrica** aro 24 Sousa Bike **350W** freio a disco **com acelerador**"* —
  o título diz, ele mesmo, as duas coisas que a regra não deixa coexistir. Pelo que o eixo
  A mediu (as fontes convergem exatamente aqui), **acelerador manual tira o veículo da
  definição de bicicleta elétrica, mesmo abaixo do limite de potência**.
- *"**Bicicleta elétrica** Siena **1000W** adulto **sem CNH** **scooter**"* — quatro termos
  que a resolução separa, num anúncio só.
- O guia que elege **"o melhor patinete elétrico de 2026 para adultos"** descreve o
  vencedor com **dois motores de 1.000 W e 72 km/h**. Pelos limites colhidos, 72 km/h **não
  é autopropelido em nenhuma leitura**. **A página que mais aparece para "melhor patinete
  adulto" recomenda, sem dizer, um ciclomotor** — e é a frase da ilha inteira numa linha:
  *o número grande do anúncio não é o número que a regra lê.*

**O que isto muda no bloco 2, e está escrito na seção 6 do corpus:** a F1 tem **quatro**
entradas, não três — o **acelerador é pivô, não detalhe** (sem ele nenhuma potência
classifica) —, e a saída tem **duas camadas**, porque a resposta é nacional **e** municipal
(Campinas regulamenta 20 km/h; o Rio tem os 350 W/25 km/h próprios). A F1 que responder
"autopropelido, dispensa CNH" sem dizer que a rua é municipal estaria certa na categoria e
incompleta na vida. Para a F2, o eixo B entregou a régua do relevo **com número**: 41,29
Wh/km em plano contra **97,74 Wh/km a 12% de inclinação** — a reler na fonte e datar. Para
a F3, o teto de mercado está medido em **120 kg**, com a régua de margem de 10% que exclui
quem passa de 109 — e a pessoa de 110 kg do `VOZ.md` cai exatamente ali.

### O SITE JÁ ESTAVA NO AR, E O `ESTADO.md` DIZIA "PENDENTE" — a seção 4 em ação, no primeiro dia da ilha

A conferência de rede da **20.2** era para ser barata e de rotina. Devolveu **200 em três
tentativas**, com `<title>Rodametria - Mobilidade elétrica</title>` e `last-modified` de
**27/10 às 22h17Z** — ou seja, o WordPress subiu **cinco horas depois** de a ilha nascer, e
o cabeçalho que esta execução leu ainda dizia *"WordPress: pendente"*, *"nameservers
pendente"*, *"hospedagem pendente"* e *"lista de domínios permitidos pendente"*. **Nenhum
dos quatro estava pendente.** É a seção 4 no estado puro, e no dia 1: o site anda e o
cabeçalho fica para trás em silêncio.

**O que de fato falta, medido e não herdado:** tema de blocos cru, **zero página
publicada**, `/wp-sitemap.xml` sem URL nenhuma, e `/wp-json/rodametria/v1/status` em **404**
— o snippet de Sync não existe. O que está **são**: `/wp-json/` em 200 e
`/nao-existe-xyz/` devolvendo **404 de verdade**, então a porta de entrada da seção 29 passa
nesta primeira leitura (vale reconferir quando houver página, que é quando o `.htaccess`
costuma cair).

### A FONTE QUE DECIDE O PRODUTO DESTA ILHA É NEGADA PELO EGRESSO (20.3)

O `PROMPT.md` desta ilha é explícito: a constante central da F1 *"só vira `publicavel`
depois de lida no texto oficial do gov.br, com data"*. Medido às 10h4xZ: `www.gov.br` e
`lex.com.br` em **`000` com `connect_rejected`**, e a busca de página falha na própria
resolução de nome (`ENOTFOUND www.gov.br`). **Não é intermitência de túnel** — a 20.2 manda
repetir antes de chamar de bloqueio, e aqui a repetição não muda nada, porque o erro
nomeado pelo egresso é recusa. É a **20.3** em estado puro: a regra que exige a fonte foi
escrita em 27/10 e a fonte nunca foi conferida.

**A consequência, dita sem maquiagem:** o bloco 2 pode ser escrito inteiro daqui, e
`constantes.json` pode nascer com a constante da F1 marcada `publicavel: false` e a dívida
nomeada. **O que não pode é a F1 ir ao ar classificando veículo com número de portal de
notícia** — numa ilha onde errar manda a pessoa para a rua sem habilitação. Virou despacho
**ALTA** em `dados/despachos.md`, com os dois gestos que o resolvem (liberar `gov.br` na
lista de rede, **ou** colar as três definições literais com URL e data). **E a ilha NÃO
recebeu `bloqueada_por`** (seção 11, passo 4): travou uma fonte, não a ilha.

### A 30.8 MEDIDA NUMA ILHA NOVA, COM A CONTAGEM QUE FALTAVA: O VAZAMENTO NÃO É PARELHO ENTRE EIXOS

| eixo | ocupantes de fora do Brasil |
|---|---|
| **CNH e placa** (regra brasileira) | **zero** em 7 consultas |
| produto pelo nome | 3 de ~18 |
| carga e tamanho | 6 de ~17 |
| **autonomia** | **~40 de ~50**, e uma consulta com **zero** ocupante brasileiro |
| **peças** (câmara, pneu, carregador) | **18 de 20** em `pccomponentes.pt` |

**A leitura vale para as outras cinco ilhas, e é por isso que está escrita e não só
sentida:** pergunta de **regra brasileira** não tem equivalente em Portugal ou na Espanha,
então a busca da nuvem não tem para onde vazar e a procedência é confiável; pergunta de
**produto e consumível** tem catálogo europeu idêntico, e aí a busca entrega Portugal. **O
vazamento é mínimo exatamente onde esta ilha nasce** — o que é sorte, não desenho, e vale
dito para a próxima Bússola saber que eixo de regra é o mais barato de medir da nuvem. E,
pela assimetria da 30.8, **nada disso autoriza `alvo`**: nenhuma linha do corpus diz `alvo`,
nem no eixo A. A SERP dos eixos de autonomia, carga e peças virou despacho NORMAL.

### Nada foi ao ar, e não podia

A ilha tem WordPress e não tem casca, snippet de Sync, `/status` nem URL própria. Acionar
Sync e conferir no ar era impossível, e dizer que conferi seria inventar. Este bloco é
dado: `publicar: false`, zero URL, zero revisão. A **31.1** não se move por ele.

**Próximo passo desbloqueado:** **bloco 2 — especificação das ferramentas**
(`dados/especificacao-calculadoras.md` + `dados/constantes.json`), na ordem obrigatória F1,
F2, F3. Ele pode ser escrito inteiro desta nuvem e **herda da seção 6 do corpus** as quatro
entradas da F1, as duas camadas de saída, a régua do relevo da F2 e o teto de 120 kg da F3.
**A constante legal da F1 nasce `publicavel: false`** até o despacho ALTA de 28/10 ser
atendido — e quem fechar o bloco 2 lê a seção 4 do corpus antes, para não ler a tabela do
eixo A como se fosse a resolução.
