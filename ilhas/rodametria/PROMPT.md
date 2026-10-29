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

**3d. O CASAMENTO DO REGISTRO COM A OFERTA (degraus 1 a 3 da 25.1) — é o próximo bloco, e ele vem ANTES do
3b.** Leia a **25.7** (as cinco armadilhas de casamento) e a **25.9** antes de escrever uma linha. Ele
resolve três coisas de uma vez: `url_produto` (e com ela o teste de vida da 25.4-b passa a existir nesta
ilha), a **foto** que o cartão da 32.1 pede, e o caminho para a ficha onde o campo técnico mora. Alvo
apertado, saindo da medição de 28/10: os **7** registros que não compõem chave nenhuma e os **5** que a loja
não respondeu em nenhum degrau. **A coleta em ficha de FABRICANTE (nível 4 da escada, hoje vazio) continua
necessária e ficou mais urgente**, e o primeiro passo dela é a 20.3 outra vez — medir o egresso contra os
domínios dos fabricantes antes de escrever regra que os exija.

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

**5b. PÁGINAS PELO NOME DO PRODUTO** (seção 30) para as seis cabeças, e depois a malha.

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
