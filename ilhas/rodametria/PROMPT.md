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
- **A CASCA E A F2 ESTÃO NO AR DESDE 29/10/2026.** `/` (home, molde da 32.2) e
  `/autonomia-patinete-eletrico/` (F2, molde de FERRAMENTA da 32.1). A casca publica
  `https://rodametria.com.br/wp-json/rodametria/v1/casca` (GET público), que devolve a versão
  da casca, o relato da instalação e o mapa de páginas com a URL de cada uma — é por ele que
  `ferramentas/conferir-no-ar.py` confere que link interno não aponta para 404.
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

## DESPACHO DA FUNDAÇÃO PARA O RAPHAEL — 30/10/2026 — DUAS SERPs E UM VOLUME, NUMA SESSÃO DE CHROME

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

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de mobilidade elétrica com site próprio, `publicar: false`.

## A BANCADA DESTA ILHA É UM COMANDO SÓ, E ELA DESCOBRE OS PORTÕES (28/10/2026)

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
