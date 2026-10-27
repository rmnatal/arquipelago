---
titulo: Especificação das ferramentas — JornadaFly
bloco: 2
gerado_em: 2026-09-14
publicar: false
---

# Especificação das ferramentas — JornadaFly

Bloco 2 da fila. Define **o que cada ferramenta responde, com que entrada, com que
saída, com que fonte, e o que ela se recusa a responder**. Nenhuma linha de PHP
nasce antes deste arquivo; nenhum número entra aqui sem fonte e data.

Três ferramentas, na ordem que o corpus do bloco 1 confirmou — e ela não é
negociável, porque as duas últimas entram contra quem já ocupa a vaga:

| Código | Ferramenta | Eixo do corpus | Momento do funil | Sub_id 2 |
|---|---|---|---|---|
| **F1** | Quanto custa a experiência para o SEU grupo | A — custo de experiência | fim (cartão na mão) | `F1` |
| **F2** | Quanto custa N dias em `<cidade>` | B — custo de estadia | início (sonhando) | `F2` |
| **F3** | O passe da cidade vale a pena para você | C — passe × avulso | fim | `F3` |

Sub_id 1 é sempre `jornadafly` (seção 7 do `ARQUIPELAGO.md`).

---

## 0. Como esta coleta foi feita, e o que isso limita

Três canais foram tentados nesta execução, e **dois estão fechados**:

| Canal | Resultado, medido em 14/09/2026 entre 17h25Z e 17h40Z |
|---|---|
| `curl` direto às fontes | **fechado.** `economia.awesomeapi.com.br`, `open.er-api.com` e `api.bcb.gov.br` devolveram `000`, com o proxy declarando `connect_rejected` por política da organização |
| leitura direta de página de fonte primária | **fechado.** `www.comune.venezia.it` devolveu `EGRESS_BLOCKED` |
| busca web em pt-BR | **aberto.** É o canal de tudo que está escrito abaixo |

**A consequência fica escrita e não escondida:** toda constante deste bloco saiu de
**busca web**, e o canal está declarado item a item em `constantes.json`. Pela regra do
elo mais fraco (seção 10 do `ARQUIPELAGO.md`), **nenhuma delas é "leitura direta da
fonte primária"**, mesmo quando o documento citado é oficial — o elo da leitura é
fraco, e é ele que dá o nível. A reconfirmação na fonte primária é trabalho do bloco 3,
e depende da mesma abertura de rede que o despacho do bloco 1 já pede.

### 0.1 Uma armadilha de coleta em que esta execução caiu, e o conserto

A seção 8 do `ARQUIPELAGO.md` proíbe, com todas as letras, pôr na consulta o valor que
se quer confirmar: *"pergunte qual é o valor, não se o valor é X"*. **Duas das consultas
desta execução violaram isso**, e fica escrito porque esconder seria pior que o erro:

| Consulta com o número plantado | O que ela devolveu |
|---|---|
| "IOF … alíquota 2026 **3,5%**" | 3,5% — confirmando o que a própria pergunta dizia |
| "tariffa … gondola Venezia comune **90 euro 110 notturno**" | €90 e €110 — idem |

**As duas foram refeitas com pergunta limpa**, sem número dentro, antes de qualquer
coisa ser gravada:

- *"qual a alíquota do IOF para compras internacionais no cartão de crédito
  atualmente"* → **3,5%**, chegando por outros publicadores (Nubank, Wise, Afinz,
  Mercado Pago, Rádio Câmara) e com a história da alíquota (3,38% em janeiro de 2025,
  depois 3,5%), que a pergunta plantada não tinha trazido.
- *"quanto costa un giro in gondola a Venezia tariffa ufficiale del comune quante
  persone"* → **€90 diurno (30 min) e €110 noturno (35 min), máximo 5 pessoas**, e
  agora **com o ato que as sustenta**: *Delibera della Giunta Comunale n. 89 del
  20/04/2023*. A pergunta limpa trouxe a procedência que a plantada não trouxe.

**As duas passaram**, então os dois números ficam publicáveis — mas o que os torna
publicáveis é a **segunda** passada, não a primeira, e é a segunda que está citada em
`constantes.json`. A lição é a que o contrato já tinha: pergunta que carrega a resposta
não é coleta, e o custo de refazer é de dois minutos.

**Uma correção de método ao bloco 1, e ela enfraquece uma frase daquele arquivo.** O
corpus diz "a coleta é SERP brasileira em pt-BR". O que a ferramenta desta nuvem
garante é a **língua** da consulta, não a **geografia** de quem busca: a busca sai dos
Estados Unidos. Onde este arquivo e o corpus dizem "SERP em pt-BR", leia **"SERP
devolvida para consulta em português"**. Nada do que os dois arquivos concluem depende
da geografia — as conclusões são sobre quem escreve em português e sobre o que as
páginas dizem —, mas a frase estava larga demais e fica corrigida aqui.

---

## 1. A PERGUNTA ABERTA DO BLOCO 1, MEDIDA E **NEGADA**

O bloco 1 deixou uma hipótese escrita como pergunta e proibiu de supô-la: *"o muro do
portal veterano brasileiro é forte onde existe um portal brasileiro que cobre aquele
destino, e fraco onde não existe"*. Se fosse verdade, mudaria a ordem das cidades do
banco. **Foram medidas seis consultas novas em 14/09/2026, e a hipótese não se
sustenta.**

| Consulta medida | Destino tem portal veterano brasileiro? | Plataforma no resultado? | Quem de fato ocupa |
|---|---|---|---|
| "quanto custa ingresso Petra Jordânia preço" | não dedicado | **não** | blogs br (`dicasdeviagem`, `escolhaviajar`, `buenasdicas`, `abraceomundo`, `fuigosteicontei`) e dois portugueses (`deferias.pt`, `destinosvividos`) |
| "quanto custa ingresso Angkor Wat Camboja preço" | **sim** (`melhoresdestinos`, `queroviajarmais` estão lá) | **não** | os dois portais veteranos + blogs + agregadores de notícia |
| "quanto custa passeio de barco na Baía de Ha Long Vietnã preço" | não dedicado | **sim** (`booking.com/boats`) | `umviajante`, `guiaviagemfacil`, `prepareamochila` e o Booking |
| "quanto custa passeio de quadriciclo no deserto em Dubai preço" | não dedicado | **sim** (`hellotickets`, e a **Civitatis com página de produto** `civitatis.com/br/dubai/oferta-dubai-safari/`) | `quantocustaviajar` em 1º, `travel.com.br`, blogs |
| "quanto custa city tour em Buenos Aires passeio preço" | **sim** | **não** — mas o lugar delas está tomado por **receptivos vendendo direto** (`denomades`, `nomades`, `fulltour`, `ciatrip`, `aguiarbuenosaires`) | receptivos + `buenasdicas`, `voltologo` |
| "quanto custa passeio de gôndola em Veneza para 4 pessoas preço" | **sim** (`eurodicas` está lá) | **sim**, mas só o **blog** (`civitatis.com/blog/pt-br/gondolas-veneza/`) | `maladeaventuras`, `eurodicas`, `viajandoparaitalia`, `viveromundo`, `turismoemfamilia` |

**Veredito: a hipótese está NEGADA, e por contraexemplo dos dois lados.** Petra não tem
portal veterano dedicado **e** não tem plataforma; Angkor tem dois portais veteranos
**e** também não tem plataforma. A presença do portal brasileiro não prediz a ausência
da plataforma. **Nenhuma cidade do banco muda de ordem por causa disto**, que era a
única decisão que a pergunta poderia ter mudado.

**O que aparece no lugar dela é mais estreito e fica escrito como leitura, não como
critério** (é hipótese nova, com uma medição a favor e uma contra): a plataforma entra
em português onde o item é **atividade vendida por operador** (safári de Dubai, cruzeiro
de Ha Long, passeio de gôndola) e não entra onde o item é **ingresso de sítio público
com bilheteria oficial** (Petra, Angkor, Coliseu, Torre Eiffel). O contraexemplo que
impede isso de virar regra é o balão da Capadócia, medido no bloco 1: atividade de
operador privado, **zero plataforma**, e dois operadores turcos com página em português
no lugar. **O que derrubaria essa leitura:** encontrar plataforma em consulta de
ingresso de sítio público, ou medir três atividades de operador sem nenhuma plataforma.
Enquanto não for medido, não decide nada.

### 1.1 E o que as OITO consultas dos dois blocos têm em comum — isto sim decide

Uma coisa apareceu em **100% das consultas medidas nos dois blocos**, e é ela que
sustenta a ilha inteira:

1. **Ninguém data o preço.** Nenhuma das seis páginas de topo medidas hoje diz quando
   leu o número que publica. O corpus já tinha achado um `<title>` com `[2024]` e uma
   conversão em real sem câmbio e sem data; hoje isso se repetiu em seis destinos
   novos, em três continentes.
2. **A unidade do preço troca dentro da mesma resposta, sem aviso.** Foi o achado mais
   forte desta execução e é o que especifica a F1:

| Experiência medida hoje | Unidade real do preço | Como as páginas publicam |
|---|---|---|
| Gôndola, Veneza | **por gôndola** (veículo), até 5 pessoas | "€80 para até 4", "€90 dia / €110 noite", "€30 a €90 por pessoa", "€16/pessoa com lotação completa", "a partir de €34 por pessoa" — **cinco leituras, três unidades** |
| Cruzeiro, Ha Long | **por cabine** em parte dos casos | "a partir de US$ 50", "US$ 120 a 200 por pessoa", "US$ 714 (quarto para duas pessoas)" — a última é por cabine e está na mesma lista das outras |
| Safári, Dubai | por pessoa, com pacote variável | "US$ 30 a 44", "cerca de US$ 85", "US$ 59 a 160 (R$ 320 a 870)" — o real convertido **sem câmbio e sem data** |
| Petra | por pessoa, **em escada de dias** | "US$ 70 (1 dia), 75 (2), 80 (3)", com a condição "para quem pernoita na Jordânia" fora da frase do preço |
| Angkor | por pessoa, em escada de dias | "US$ 37 (1 dia), 62 (3), 72 (7)" |
| City tour, Buenos Aires | por pessoa, com preço de criança | "US$ 33 adulto / US$ 17 criança (2 a 7)" — **o único caso medido hoje que declara a regra de criança** |

**É esta a vaga, e agora ela está medida em seis destinos além dos sete do bloco 1: o
dado bruto circula, a unidade não é declarada, e a conta para o grupo de quem lê não
é feita por ninguém.** A F1 não inventa categoria: ela **declara a unidade, fecha a
conta e data o preço**.

---

## 2. FERRAMENTA F1 — Quanto custa a experiência para o SEU grupo

### 2.1 A pergunta e o alvo de busca

**Consulta principal:** `quanto custa <experiência> para <N> pessoas` e as irmãs
`vale a pena <experiência>`, `<experiência> preço`, `o que está incluso no <experiência>`
(clusters A1, A2 e A3 do corpus).

**Classificação da SERP, exigida pela seção 14.9, feita em 14/09/2026 na consulta real
"quanto custa passeio de gôndola em Veneza para 4 pessoas preço":**

| Quem ocupa | O que entrega |
|---|---|
| `maladeaventuras.com` ("Preços 2026") | faixa de preço, sem data de leitura, sem dizer a unidade |
| `turismo.eurodicas.com.br` | portal veterano; "quanto custa e como funciona", preço por gôndola citado como €80 até 4 pessoas |
| `civitatis.com/blog/pt-br` | a plataforma, **com blog e não com produto** nesta consulta |
| `viajandoparaitalia.com.br`, `viveromundo.org`, `turismoemfamilia.com.br` | blog de viagem, relato e faixa |
| `viagemitalia.com` | reserva de passeio, vende |

**Veredito: é ALVO, e por um motivo mais forte do que "a SERP é fraca".** A SERP é
cheia e é de gente que escreve bem. O que nenhum dos sete entrega é a resposta ao
parâmetro: **quatro dos sete publicam números que se contradizem sobre uma tarifa
tabelada por prefeitura, e nenhum declara quando leu.** A consulta tem "para 4 pessoas"
escrito nela e a resposta que está no ar é uma faixa por pessoa sobre um preço que é
por veículo.

**Por que a F1 chega às 10 primeiras:** ela serve, em HTML, a conta fechada para o
tamanho do grupo, com a unidade declarada, o nome de quem publicou cada número
divergente, e a data de leitura ao lado de cada preço. Intenção de compra: alta e
imediata — quem escreve "para 4 pessoas" já decidiu ir e está dividindo a conta.

### 2.2 O caso que especifica a ferramenta: a gôndola de Veneza

Medido em 14/09/2026. Cinco leituras do mesmo preço, na mesma página de resultados:

| Quem publica | O que diz | Unidade |
|---|---|---|
| duas páginas de topo em pt | **€80** para até 4 pessoas | por gôndola |
| outras páginas de topo em pt | **€90** (dia) e **€110** (noite) | por gôndola |
| a mesma família de páginas | **€30 a €90** por pessoa (gôndola compartilhada) | por pessoa |
| idem | **€16** por pessoa com lotação completa de 5 | por pessoa |
| plataforma (GetYourGuide, citada por terceiros) | **a partir de €34** por pessoa | por pessoa |

**A fonte que decide, e ela é poder público:** o *Servizio Gondola* do **Comune di
Venezia** publica a tarifa oficial, aprovada pela **Delibera della Giunta Comunale n. 89
de 20/04/2023** — **€90 por 30 minutos das 9h às 19h**, **€110 por 35 minutos das 19h às
4h**, **máximo de 5 passageiros por gôndola**, e cerca de **€40 (dia) ou €50 (noite) a
cada 20 minutos adicionais**. A fonte diz a unidade com todas as letras: *"não se paga
por pessoa, e sim pelo aluguel da embarcação inteira"*. Lido por busca web em
14/09/2026, com pergunta limpa (ver 0.1); **a leitura direta da página foi tentada e
recusada pelo egresso** (`EGRESS_BLOCKED`), então o nível desta fonte é o do elo da
leitura, não o da autoria (seção 10).

**E note o que isso faz com a lista de divergentes acima:** as duas páginas de topo que
publicam "€80 para até 4 pessoas" não estão arredondando — **estão três anos
desatualizadas**, porque a tarifa vigente é de abril de 2023. O defeito que a ilha
existe para corrigir não é imprecisão; é preço sem data envelhecendo em silêncio numa
página que continua no topo.

**O que isso faz com a conta, e é o produto da ilha em uma linha:** para **4 pessoas**,
de dia, o passeio custa **€90 no total — €22,50 por pessoa**, e não "€80" nem "€34 por
pessoa". Quem chegar com a conta de €34 por pessoa leva **€136** para um passeio de
**€90**; quem chegar com a de €80 vai pagar €90. **As duas direções do erro existem, e
não custam a mesma coisa** — ver 2.5.

**A regra de resolução de divergência desta ilha, escrita como a seção 10 exige (com o
erro caro nomeado antes da direção):**

1. **Quando existe tarifa de poder público, ela ganha de qualquer número de blog**, e a
   página publica as duas declarações com quem as publicou. Foi o caso aqui.
2. **Quando não existe autoridade e duas fontes divergem, a ilha resolve para o valor
   MAIOR.** O erro caro é o de **subestimar**: o leitor que chega com dinheiro a menos
   perde a experiência na porta; o que chega com dinheiro a mais volta com troco. A
   assimetria é a mesma da Aquametria (errar para cima dá ao peixe mais espaço do que
   precisa) e o oposto da Robometria (peça que não encaixa) — e a direção sai do custo,
   nunca do gosto.
3. **Média é proibida** (seção 10). A divergência é o produto: ela aparece na tela, com
   nome e data de cada declaração.

### 2.3 Entradas

| Campo | Tipo | Obrigatório | Observação |
|---|---|---|---|
| `experiencia` | seleção | sim | lista fechada, vinda do banco do bloco 3. Nunca texto livre |
| `pessoas` | número inteiro | sim | 1 a 12. Acima de 12 a ferramenta recusa e diz por quê (ver 2.6) |
| `versao` | seleção dependente | sim | **as versões que o operador realmente vende** (diurno/noturno, padrão/deluxe, 1 dia/3 dias). Nunca uma escada inventada pela ilha |
| `momento_do_dia` | seleção dependente | condicional | só existe quando o banco declara preço diferente por horário — a gôndola é o caso |

**O seletor de versão só oferece o que o banco consegue responder**, pela mesma regra
que a Robometria aprendeu com o reservatório: valor que está no vocabulário do esquema
e tem zero itens no banco **não aparece na tela**. A varredura que prova isso é portão
do bloco 3c, não deste.

> **CORRIGIDO EM 22/10/2026, NO BLOCO 4: `momento_do_dia` NÃO É UMA QUARTA ENTRADA —
> ele é campo da VERSÃO, e oferecê-lo à parte deixaria a pessoa escolher uma
> combinação que não existe.** A tabela acima o lista como "seleção dependente,
> condicional", e no banco a gôndola resolve isso de outro jeito: as duas versões
> vendidas **são** o diurno e o noturno, cada uma com `momento_do_dia`, duração,
> janela horária e preço próprios. Ou seja, escolher a versão **já é** escolher o
> horário, e um seletor de horário separado permitiria pedir "noturno" sobre a versão
> diurna — um estado que o operador não vende. O estado da F1 é, portanto,
> **(experiência, versão, pessoas)**, e o horário sai da versão escolhida, para a tela
> e para o JSON-LD. Se um dia um operador vender a MESMA versão em dois horários com
> preços diferentes, o campo volta a ser entrada — e aí ele nasce como dimensão do
> banco antes de nascer como campo de formulário.

### 2.4 Saídas, na ordem em que aparecem na página

A ordem obedece à 15.2 (voz em cima, prova embaixo), à 14.5 (resposta antes da
explicação) e à 7 (bloco de compra antes da procedência):

1. **A frase-resposta**, na voz do `VOZ.md`, autossuficiente fora de contexto (seção 5):
   > "Passeio de gôndola em Veneza para 4 pessoas, de dia: **€90 no total, €22,50 por
   > pessoa**. O preço é **por gôndola**, não por pessoa, e cabem até 5. Tarifa oficial
   > da prefeitura de Veneza, lida em 14/09/2026."
2. **A linha do bolso brasileiro** (ver 2.5), que é o que nenhum concorrente medido tem.
3. **O que está incluso e o que não está**, as duas listas do banco, nomeadas. Lista
   vazia não some: ela diz "o operador não declara o que está incluso", que é um fato
   sobre o operador e é informação.
   > **E A FRASE É ESCRITA PELA FERRAMENTA, NUNCA COPIADA DO `motivo_*` DO BANCO
   > (medido em 22/10/2026, no bloco 4).** Os campos `motivo_sem_*` e
   > `*_motivo_lista_vazia` são escritos para a **próxima execução**: eles citam nome
   > de campo entre acentos graves, data de migração e número de seção do contrato. A
   > primeira versão da F1 os repassava para a tela, e o resultado era a página
   > dizendo ao visitante que *"o esquema PROÍBE faixa etária onde a unidade não é
   > `por_pessoa`"* — texto de bastidor da fábrica numa página pública, que a **32.4**
   > proíbe com todas as letras. É a mesma cicatriz que a ohmetria pagou publicando
   > `dados/modulos.json` na tela. O motivo continua no banco, onde serve; a tela
   > recebe a frase que responde ao visitante. Quem achou foi a régua de acento do
   > portão, e o defeito embaixo era maior que o acento.
4. **O bloco de saída de compra** (ver 2.9), antes da prova.
5. **A prestação de contas das versões** (ver 2.7).
6. **A camada de prova**: operador, URL de origem, unidade de preço declarada, data de
   leitura, e — quando houver — as declarações divergentes com o nome de quem publicou
   cada uma.

### 2.5 As três contas, e a quarta que é o diferencial

**Conta 1 — normalizar a unidade.** O banco declara `unidade_de_preco` ∈
`{por_pessoa, por_veiculo, por_cabine, por_grupo}` e `capacidade_maxima`. A F1 traduz
tudo para **total do grupo**:

- `por_pessoa` → `total = preco × pessoas`
- `por_veiculo` / `por_cabine` / `por_grupo` → `total = preco × teto(pessoas ÷ capacidade_maxima)`

O segundo caso é o que produz o degrau que nenhuma página medida mostra: **6 pessoas na
gôndola são duas gôndolas, €180**, não "€90 dividido por 6".

**Conta 2 — por pessoa.** `por_pessoa = total ÷ pessoas`, sempre exibido ao lado do
total, porque é assim que o grupo divide.

**Conta 3 — a escada de dias/versões**, quando o banco declara mais de uma: a F1 mostra
a versão escolhida **e** a linha "a partir de qual número de dias/atrações a versão mais
cara passa a valer", que é a mesma aritmética da F3 aplicada dentro de um item só.
Petra e Angkor são os casos medidos.

> **ATUALIZADO EM 22/10/2026, NO BLOCO 4, E A ATUALIZAÇÃO É UMA CONDIÇÃO QUE NÃO
> ESTAVA ESCRITA: a Conta 3 só existe quando as versões se SUBSTITUEM em quantidade,
> e isso é declarado, nunca deduzido do rótulo.** Escrever a F1 como regra mostrou que
> esta conta não era calculável sobre o banco versão 4 — e que calculá-la onde ela não
> cabe é pior que não a calcular. As duas metades:
>
> 1. **A EXPERIÊNCIA declara `eixo_das_versoes`** ∈ `{por_quantidade, por_escopo,
>    por_momento}`. A conta roda **só** em `por_quantidade`. Nos outros dois a F1 diz,
>    na tela, por que não há ponto de equilíbrio — e isso é uma resposta, não um
>    silêncio. **O erro caro, nomeado antes da direção, como a seção 10 manda:**
>    comprar dois ingressos de 24 horas do Coliseu **não** dá a área restrita da
>    Experiência Completa, e comprar dois passeios diurnos de gôndola **não** dá um
>    passeio noturno. Um ponto de equilíbrio entre bilhetes que não se substituem é
>    aritmética correta sobre uma pergunta sem sentido — a forma mais eficiente de
>    publicar uma mentira com cara de conta.
> 2. **A VERSÃO declara `dias_de_uso`**, com `dias_de_uso_transcrito_de` dizendo de qual
>    frase da fonte o número saiu. O número **tem de aparecer no `declarado_como`** da
>    própria versão, em dígito ou por extenso, e a régua confere isso — é a terceira
>    conta da seção 8: sem ela o campo seria um inteiro digitado por quem migrou, com
>    cara de transcrito. Os três números do Angkor (1, 3 e 7) já estavam escritos na
>    declaração da fonte desde 14/09/2026, em **prosa**; a migração os transformou em
>    campo e não leu nada de novo. É a mesma troca que a `faixa_etaria` fez no dia
>    anterior, um andar acima.
>
> **O eixo não se deduz do rótulo**, e essa é a parte que não se adivinha: "1 dia" e
> "3 dias, usáveis dentro de uma semana" têm a quantidade escrita dentro do texto, e
> ler o texto como se fosse campo é exatamente o que a migração de 22/10 desfez. Ler o
> rótulo também acertaria no Angkor e **erraria no Coliseu**, cujos rótulos não falam
> de quantidade nenhuma — e erro que acerta no caso que se tem na mão é o mais caro de
> todos, porque ele passa.
>
> **O ponto de equilíbrio é uma FUNÇÃO PURA** sobre a relação já calculada
> (`[(id, rótulo, preço, dias_de_uso)]` + o eixo), e não uma varredura do banco. É a
> regra da seção 8 nascida no Clube do Mosaico em 08/10/2026: recusa que depende de uma
> relação entre os dados — empate, ausência, borda — só é testável no dia em que o banco
> produzir o caso, e é esse o dia em que ela vai estar errada. Com a função pura, a
> bancada fabrica o empate de preço, a versão única e o preço ausente sem fabricar um
> banco falso.
>
> **A conta, para o Angkor, medida:** a base é o bilhete de menor quantidade (1 dia,
> US$ 37) e o equilíbrio é o menor número de dias `D` em que `teto(D ÷ dias_da_base) ×
> preço_da_base ≥ preço_da_versão`. Dá **2 dias** para o passe de 3 (US$ 62: dois de um
> dia já custam US$ 74) e **2 dias** para o de 7 (US$ 72). Quem fica 1 dia compra o de
> 1 dia; a partir do segundo, qualquer um dos dois passes já paga.

**Conta 4 — o que o cartão brasileiro acrescenta, e ela funciona HOJE sem taxa de
câmbio.** Sobre compra internacional com cartão de crédito ou débito de pessoa física
incide **IOF de 3,5%** (Decreto nº 12.499/2025; ver `constantes.json`). Como é
percentual, ela se aplica **na moeda do operador** e não precisa de conversão:

> "No cartão brasileiro, o IOF de 3,5% entra por cima: **€93,15 no total**, ou **€23,29
> por pessoa**."

**Nenhuma das seis páginas medidas hoje menciona IOF**, e três delas convertem para real
sem declarar câmbio nem data — que é exatamente o defeito inverso. Esta linha é o
diferencial mais barato e mais defensável que a ilha tem, e ela não depende de nada que
esteja bloqueado.

**O que a F1 NÃO publica hoje:** o valor em reais. As constantes `cambio-eur-brl` e
`cambio-usd-brl` estão com status `pendente` — não há canal aberto para lê-las (ver
seção 0) — e **constante pendente é proibida dentro de fórmula publicada** (seção 10 do
`ARQUIPELAGO.md`). A página diz isso ao leitor em vez de esconder, e diz na voz dela:
*"o valor em real depende do câmbio do dia do seu cartão; a conta acima está na moeda
que o operador cobra, que é a que não muda."* No dia em que houver fonte de câmbio
datada, **nenhuma linha de estrutura muda**: nasce uma linha a mais, com a taxa e a data
ao lado.

### 2.6 O que a F1 se RECUSA a responder, e o que ela diz no lugar

Recusa que nomeia a causa medida, nunca hipótese (seção 7):

- **Preço em real como número atual.** Sem câmbio datado, não há número. Ver 2.5.
- **Desconto de criança**, enquanto o banco não tiver `faixa_etaria` preenchida para
  **aquela VERSÃO**. *(Atualizado em 22/10/2026: `faixa_etaria` desceu de EXPERIÊNCIA
  para VERSÃO, porque o preço de uma faixa depende do bilhete — na Torre Eiffel a
  criança de 4 a 11 anos paga 3,80€ pela escada até o segundo piso e 9,20€ pelo
  elevador até o topo. **A F1 lê a faixa da versão que a pessoa escolheu, nunca da
  experiência**, e essa é a diferença entre responder o preço do grupo e responder o
  preço de um grupo que compra outro bilhete.)* O city tour de Buenos Aires foi o único
  caso medido no bloco 2 que declara a regra (US$ 33 adulto / US$ 17 criança de 2 a 7
  anos) — então a regra existe no mundo e a ausência dela no banco é falta de dado, que
  a página declara como falta de dado daquele operador.
- **Faixa que a fonte declara e a leitura não transcreveu.** Caso novo de 22/10/2026, e
  ele NÃO é o mesmo que o de cima: duas das quatro versões da Torre Eiffel não trazem a
  criança nem o jovem porque a leitura de 15/09 transcreveu só o piso e o teto da grade.
  A ausência está **contada** em
  `faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu`, com quatro entradas, e a F1
  diz *"o operador cobra uma tarifa de criança neste bilhete e nós ainda não a lemos"* —
  que é uma frase diferente de *"o operador não declara tarifa de criança"*. Confundir
  as duas é cobrar do leitor o preço cheio de quem tinha desconto.
- **O número que a frase da fonte cita, quando ele é de outra versão.** No Angkor a
  fonte escreve que a criança sem passaporte paga US$ 37, e US$ 37 é o passe de **um
  dia**: nos passes de 3 e de 7 dias a faixa traz
  `numero_da_frase_e_de_outra_versao`, e a F1 **cita a frase dizendo de qual bilhete ela
  fala**, em vez de usar 37 como se fosse daquele passe.
- **Alta e baixa temporada**, sem o campo `temporada`. As fontes do bloco 1 dizem que a
  diária de carro na Islândia varia **até três vezes** entre inverno e verão; chutar
  isso seria inventar o dado mais caro da página.
- **Grupo acima de 12 pessoas.** Acima disso a compra vira negociação com o operador, e
  a página diz isso em vez de multiplicar.
- **Gorjeta de free tour somada como se fosse preço.** As fontes divergem
  (`constantes.json`) e a gorjeta não é cobrada: ela entra como **faixa, com o nome de
  quem recomenda cada número**, nunca dentro do total. É o caso em que somar seria
  transformar recomendação editorial em preço.

### 2.7 Prestação de contas (seção 7) — cada versão nomeada uma vez

A seção 7 manda que todo item da categoria consultada apareça **exatamente uma vez** na
prosa da resposta: ou na frase que o recomenda, ou numa linha que diz por que não está.
Aqui a "categoria consultada" é o conjunto das **versões vendidas daquela experiência**
que o banco conhece. Portanto:

- Toda versão do banco daquela experiência aparece na resposta — a escolhida com o
  preço, as outras numa linha com o motivo ("noturno: €110, 35 min, fora do horário que
  você escolheu").
- **Nenhuma versão entra no bloco de compra sem que a prosa a nomeie.**
- **A soma dos nomeados fecha o banco, e isso se mede varrendo a entrada inteira contra
  o tamanho CONTADO do banco, nunca contra um número digitado.** É a cicatriz da F2 do
  Clube do Mosaico, e a régua nasce junto com a ferramenta, não depois.
- Vale igual para a **tabela pré-renderizada** (2.8), que é a metade que um modelo de
  linguagem lê sem preencher formulário — foi lá que três das nove linhas do Clube do
  Mosaico não fechavam.

### 2.8 Tabela pré-renderizada (seções 5 e 14.5)

Obrigatória no HTML servido, cobrindo a faixa real de uso: cada experiência do banco
× **1, 2, 4 e 6 pessoas**, com colunas `total`, `por pessoa`, `unidade do preço`,
`com IOF`, `lido em`. O 6 é obrigatório na tabela porque é onde o degrau de capacidade
aparece — uma tabela que para em 4 esconde exatamente o que a ferramenta tem de
diferente.

### 2.9 A saída de compra, e por que a escada da seção 25 não serve como está

A 25.1 é uma escada de **marketplace** (loja oficial na Shopee → catálogo `/p/` do
Mercado Livre → anúncio de vendedor → link de busca). **Nenhum dos quatro degraus
existe no nicho de experiência**, e fingir que existem seria copiar a forma da regra
perdendo o que ela protege.

**O princípio da 25.2, esse vale inteiro e é o que manda: o piso nunca depende de
ninguém, todo item nasce com ele, e "link de loja em breve" está proibido (seção 7).**
A escada desta ilha, então, é a tradução do princípio para o nicho:

1. **Página da experiência na plataforma**, em português: `civitatis.com/br/<cidade>/<slug>/`.
   Medida hoje em dois destinos independentes — `civitatis.com/br/veneza/passeio-gondola-veneza/`
   e `civitatis.com/br/dubai/oferta-dubai-safari/`. É o equivalente ao degrau 1: quem
   opera é a plataforma, não um vendedor avulso.
2. **Página de cidade da plataforma**: `civitatis.com/br/<cidade>/`. **É o PISO desta
   ilha.** Não esgota, não sai do ar quando uma atividade encerra, e é **fabricável
   sozinha a partir do campo `cidade` do banco**, sem clique de ninguém — que é
   exatamente o que a 25.2 exige do piso.
3. **Página de reserva do próprio operador**, quando existir e a plataforma não cobrir.
   Converte, mas não paga comissão enquanto não houver programa; entra como saída de
   compra honesta, nunca como se fosse afiliado.

**O estado de hoje, dito ao leitor e não escondido:** **nenhum programa de afiliado
está cadastrado** (a Civitatis não aceita quem só tem rede social, e pela ordem do
`PROMPT.md` o cadastro vem **depois** de haver conteúdo real no ar). Portanto, quando a
F1 nascer, o link do bloco de compra será **cru** — e, pela decisão que a Aquametria e a
Robometria já registraram, **link cru sai sem `rel="sponsored"`**: `sponsored` é a
declaração de relação **paga**, e ninguém está pagando por aquele clique. Ele sai com
`rel="nofollow noopener"` e `target="_blank"`, e a página de divulgação de afiliados diz
qual link rende comissão e qual não rende. **No dia do cadastro, nenhuma linha de
estrutura muda** — só o gerador que monta a URL.

**Campo obrigatório no banco (bloco 3), com o nome que o contrato já usa:** todo item
nasce com `afiliado.url_busca_produto` preenchida (a URL do degrau 2, crua), e
`afiliado.url` nasce presente e vazia. Item sem piso é defeito da 19.1, sempre.

### 2.11 A F1 COMO REGRA — o que o bloco 4 entregou, e onde ela mora (22/10/2026)

A F1 existe hoje como **regra** e ainda não como **página**, e isso é decisão
registrada e não atraso. Esta ilha não tem WordPress, não tem Sync e não tem
`/status`, e `jornadafly.com.br` não está na lista de Domínios permitidos deste
ambiente (remedido em 22/10/2026: `CONNECT tunnel failed, response 403`, seis
medições, com as duas ilhas de controle em 200). Sem casca, um snippet PHP só poderia
ser medido por um render de bancada que serve **menos** do que o site serve — a
cicatriz que a seção 8 do `ARQUIPELAGO.md` mais cobra. Então a regra nasceu onde pode
ser conferida hoje, e **o PHP, quando nascer, é tradutor desta referência, frase a
frase** — o mesmo desenho que a ohmetria usou na F1 dela e que a robometria usa entre
`cobertura-r1.py` e `robometria-r1.php`.

| Arquivo | O que é |
|---|---|
| `ferramentas/f1-referencia.py` | o cérebro: estado → resposta inteira, já em frase acentuada |
| `ferramentas/gerar-f1.py` | grava o domínio de resposta e a tabela pré-renderizada |
| `dados/f1-respostas.json` | as **154** respostas (11 versões × 12 tamanhos de grupo + as 2 bordas) e as **44** linhas da tabela. `publicar: false` |
| `ferramentas/teste-f1.py` | o portão: refaz a aritmética à mão, em `Fraction`, e mede acento e texto de bastidor em toda frase de todo estado |
| `ferramentas/mutacoes-f1.py` | quebra a referência de propósito e exige que o portão veja |

**As bordas entram no domínio de propósito:** 0 e 13 pessoas são as duas recusas
duras, e um arquivo que trouxesse só 1 a 12 deixaria a metade que **recusa** sem
nenhum caso gravado. Grade que não pisa na borda é amostra com nome de grade.

**O que o bloco mediu e vale guardar:** existe **exatamente um** estado neste banco
em que arredondar meio-para-cima difere de arredondar meio-para-par — a gôndola
noturna para 2 pessoas, €56,925 por pessoa com IOF, que é €56,93 e não €56,92. Uma
grade por amostragem teria 1 chance em 154 de o encontrar, e a mutação que troca o
arredondamento voltaria **verde**. É a seção 8 sobre varrer a entrada inteira, com o
número do custo de não a varrer.

### 2.10 JSON-LD

`WebApplication` na ferramenta; `FAQPage` com as perguntas que a própria ferramenta
responde ("o preço da gôndola é por pessoa?"); `BreadcrumbList` com a árvore da seção 16.
**A ficha de experiência do bloco 5b usa `TouristTrip` com `offers`, nunca `Product`** —
a ilha não vende a experiência, e declarar `Product` com `Offer` de um preço que é de
terceiro é afirmar uma relação comercial que não existe.

---

## 3. FERRAMENTA F2 — Quanto custa N dias em `<cidade>`

**Entra depois da F1**, e o bloco 1 reforçou o motivo em vez de enfraquecê-lo: o
`quantocustaviajar.com` apareceu em **1º** em duas consultas de tipos diferentes, e hoje
apareceu em **1º numa terceira** ("quanto custa passeio de quadriciclo no deserto em
Dubai"). **Três consultas independentes, três primeiros lugares** — é o concorrente mais
forte medido nos dois blocos.

**Entradas:** `cidade` (fechada, do banco), `dias` (1 a 21), `pessoas` (1 a 12),
`padrao` (mochileiro · econômico · mediano — as três faixas que as próprias páginas de
topo publicam).

**Saídas:** uma linha por categoria — hospedagem, alimentação, transporte local,
experiências marcadas — **cada uma com fonte e data**, mais o total do grupo e o por
pessoa por dia.

**O diferencial, e é o único que justifica entrar contra quem já está em 1º:** a linha
de **experiências** não é média de blog — é a **soma das experiências do banco da F1**,
com preço colhido na fonte e data de leitura. As outras três linhas são faixa publicada
por terceiros, e a página **diz qual linha é qual**. Misturar as duas procedências numa
tabela só, sem dizer, seria o defeito que esta ilha existe para não cometer.

**Recusa declarada:** a F2 não publica número de hospedagem e alimentação como se fosse
colhido por nós. O corpus mediu duas frases na mesma SERP — "média de R$ 203,87 nos
últimos 30 dias" e "a diária mais baixa encontrada foi R$ 396,84" — **que não podem ser
as duas verdadeiras do jeito que estão escritas**. A F2 publica faixa com quem
publicou, ou não publica.

### 3.1 A F2 COMO REGRA — o que este bloco entregou, e as duas procedências (22/10/2026)

Mesma decisão da 2.11, e pelo mesmo motivo: a F2 existe como **regra** e ainda não como
**página**. O que mudou de ferramenta para ferramenta não é o desenho, é **de onde vêm os
números**.

| Arquivo | O que é |
|---|---|
| `ferramentas/f2-referencia.py` | o cérebro: (cidade, dias, pessoas, padrão) → resposta inteira, já em frase acentuada |
| `ferramentas/gerar-f2.py` | grava a grade da tabela mais as bordas, e conta o domínio inteiro |
| `dados/f2-respostas.json` | os **144** casos da tabela e as **53** bordas, com o domínio de **3.077** estados contado no cabeçalho. `publicar: false` |
| `ferramentas/teste-f2.py` | o portão: varre os 3.077 estados, refaz a aritmética à mão em `Fraction`, e chama as funções puras com os mundos que o banco não tem |
| `ferramentas/mutacoes-f2.py` | quebra a referência de propósito e exige que o portão veja |

**A F2 importa a F1 em vez de reescrever as contas dela.** A normalização de unidade, o
degrau de capacidade, a escrita do dinheiro e a data em português são as mesmas regras, e
**quarto é unidade de capacidade como gôndola**: seis pessoas numa diária de quarto duplo
são TRÊS quartos, exatamente como seis pessoas numa gôndola de cinco lugares são DUAS
gôndolas. `quartos_necessarios()` chama `unidades_necessarias()` da F1 — duas funções para
o mesmo fato é como as duas metades de um repositório param de se falar.

**AS QUATRO LINHAS NÃO TÊM A MESMA PROCEDÊNCIA, e é isso que a entidade nova garante.**
A linha de **experiências** é nossa: preço colhido no site de quem opera, com data de
leitura. **Hospedagem, alimentação e transporte local são de terceiros**, e desde hoje
moram na entidade `FAIXA_DIARIA` do esquema (versão 6), separada da `EXPERIENCIA`. A
separação é **estrutural e não editorial**: a referência nunca tem como juntar as duas
numa linha, e o portão reprova a resposta em que uma linha carregue as duas formas.

**A troca que esta migração fez, e ela é a mesma da versão 5 um andar acima.** Lá a
quantidade de uso de cada bilhete saiu da prosa do `rotulo` para `dias_de_uso`; aqui o que
saiu da prosa é **o que o número significa**. O bloco 1 mediu, em 14/09/2026, duas frases
na **mesma página de resultados** — *"média de R$ 203,87 nos últimos 30 dias"* e *"a
diária mais baixa encontrada foi R$ 396,84"* —, que não podem ser as duas verdadeiras do
jeito que estão escritas. A distinção entre elas morou numa ressalva de leitura humana por
38 dias. Agora é `o_que_o_numero_e`, que é enum, e a regra passou a ser **computável**:

> **A F2 nunca soma faixas cujo `o_que_o_numero_e` difere.** Somar uma média com um
> mínimo produz um intervalo que **ninguém publicou**. Quando a categoria tem naturezas
> diferentes, as duas vão para a tela lado a lado, com o nome de quem publicou e a frase
> com que ele disse o que o número é, e a F2 **recusa o intervalo único**.

**E a base também é declarada, nunca deduzida.** `base` diz se o número é por pessoa, por
quarto ou pelo grupo, e `base_transcrita_de` guarda a frase de onde isso saiu. Quando a
base é de quarto, `pessoas_por_quarto` é obrigatório e o número tem de **aparecer** na
frase da fonte — a régua cobra isso como cobra `dias_de_uso`. Faixa de quarto sem ocupação
**não escala**, e a linha é recusada pelo nome: dividir a diária pelo tamanho do grupo
seria escolher a ocupação no lugar de quem publicou o preço, e o resultado continuaria
parecendo dinheiro, que é por que esse erro não se vê.

**AS QUATRO RECUSAS DECLARADAS DA F2, e três delas estão ativas hoje:**

1. **Sem faixa publicada, sem linha.** É a recusa declarada desta seção, aplicada
   **categoria por categoria** em vez de à ferramenta inteira: a F2 publica a linha que
   tem e nomeia as que faltam.
2. **Sem as quatro linhas, sem total.** Um total somado só com o que a ilha tem seria um
   número **menor que a viagem** apresentado como se fosse ela inteira.
3. **A linha de experiências não cresce com os dias.** Quantas experiências cabem em N
   dias **não está no banco**, e a F2 declara isso em vez de supor. A linha é o custo de
   fazer uma vez cada experiência que a ilha leu na cidade.
4. **A F2 não escolhe a versão da experiência.** Escolher entre os quatro bilhetes da
   Torre Eiffel seria decisão editorial com cara de conta, então a linha é uma **faixa**:
   o piso é a versão mais barata de cada experiência, o teto é a mais cara, e a tela diz
   quais são.

**O QUE O BANCO AINDA NÃO TEM, e por que a falta não é descuido.** `faixas_diarias` tem
**zero** registros, então hoje a F2 publica **uma linha de quatro** em todo estado. Carregar
exige `publicado_por`, `url` e `data_leitura`, e as duas únicas frases de diária que esta
ilha mediu foram registradas **sem nenhum dos três**: o corpus guardou os números e não
guardou de quem eram. Carregar hoje exigiria **inventar o dono do número**, e o dono do
número é o produto desta ilha. A coleta também não é trabalho desta nuvem — o egresso
recusa `numbeo.com`, `booking.com` e `civitatis.com.br`, medido em 22/10/2026.

**O que o portão achou na própria ferramenta, antes do commit, e os dois são de
honestidade e não de aritmética:**

- **A faixa de largura zero.** Com as duas versões da gôndola pelo mesmo preço, as duas
  pontas vinham de versões **diferentes** com o mesmo número, e a tela publicava *"de «De
  dia» a «À noite»"* para um intervalo que não é intervalo. As duas pontas passaram a
  desempatar para o mesmo lado, e a tela diz que as versões custam o mesmo.
- **A frase que mentia sobre Siem Reap.** A primeira versão descartava a experiência que
  não fosse `publicavel`, e a página dizia *"esta ilha ainda não leu o preço de nenhuma
  experiência em Siem Reap"* — falso: o preço do passe de Angkor está lido e gravado,
  apenas não reconferido. Pior que a frase: **o mesmo item aparece na F1 com ressalva e
  desaparecia aqui**, de modo que quem viesse de uma página para a outra veria a
  experiência sumir. Agora `pendente_de_releitura` **entra na conta com a ressalva**, como
  na F1; só `excluido_do_banco` fica fora.

**E o arquivo gravado não traz os 3.077 estados, e isso é decisão com o número na mesa:**
gravá-los deu **13 MB**, contra 858 KB do arquivo da F1, e seria regravado inteiro a cada
mudança de regra ou de banco. O arquivo leva o que a página lê — a tabela pré-renderizada
e as bordas, **679 KB** —, e a prova da grade inteira mora no portão, que a varre em cada
passada. Prova em arquivo que ninguém recomputa é peso; prova em portão é prova.

---

## 4. FERRAMENTA F3 — O passe da cidade vale a pena para você

**Última, e agora por motivo medido.** O 1º colocado de "Roma Pass vale a pena" promete
**"fiz as contas pra você"** no próprio título: o formato "soma dos avulsos × preço do
passe, com ponto de equilíbrio" **já está entregue por quem ocupa o topo**. Não há vaga
de formato.

**A vaga que existe é estreita e é de atualidade**, e o bloco 1 a nomeou: a fonte de
topo do Roma Pass menciona que **novas regras de reserva obrigatória mudaram a conta em
2026**. Passe cuja regra muda é passe cujo artigo envelhece — e a F3 ganha, se ganhar,
por ser a única com **data de leitura em cada preço avulso da soma**, e com a regra de
reserva declarada ao lado do preço.

**Entradas:** `cidade`, `atracoes_pretendidas` (múltipla escolha do banco), `dias`,
`pessoas`.
**Saídas:** soma dos avulsos (cada um com data), preço do passe (com data), **o ponto de
equilíbrio em número de atrações**, e a frase de veredito na voz da ilha ("para 2 dias e
3 atrações, o passe não paga").

**Recusa declarada:** a F3 não responde por cidade cujo passe mudou de regra depois da
data de leitura registrada. Ela diz a data e diz que a regra pode ter mudado — que é o
defeito exato que ela existe para não repetir.

### 4.1 A F3 COMO REGRA — o que este bloco entregou, e o que a conta **é sobre** (22/10/2026)

Mesma decisão da 2.11 e da 3.1, e pelo mesmo motivo: a F3 existe como **regra** e ainda
não como **página**. O que mudou de ferramenta para ferramenta não é o desenho — é a
pergunta que a régua tem de responder antes da aritmética.

| Arquivo | O que é |
|---|---|
| `ferramentas/f3-referencia.py` | o cérebro: (cidade, atrações, dias, pessoas) → resposta inteira, já em frase acentuada |
| `ferramentas/gerar-f3.py` | grava a tabela mais as bordas, e conta o domínio inteiro |
| `dados/f3-respostas.json` | as **48** linhas da tabela e as **30** bordas, com o domínio de **1.038** estados contado no cabeçalho. `publicar: false` |
| `ferramentas/teste-f3.py` | o portão: varre os 1.038 estados, refaz a aritmética à mão em `Fraction`, e chama as funções puras com os mundos que o banco não tem |
| `ferramentas/mutacoes-f3.py` | quebra a referência de propósito e exige que o portão veja |

**A F3 IMPORTA A F2, QUE IMPORTA A F1**, e a cadeia é deliberada. A faixa de preço de
uma atração entre as versões dela — com o desempate das duas pontas para o mesmo lado,
que é conserto medido na F2 — mora em `f2.faixa_de_experiencias`; a normalização de
unidade e o degrau de capacidade moram na F1. **Três cópias da mesma conta seriam três
regras que divergem no dia em que uma delas mudar.** O portão prova a cadeia por um
caminho que a referência não usa: ele exige que **a soma das faixas por atração seja a
faixa do conjunto** (aditividade), o que é o que permite à tela publicar o detalhe por
atração ao lado do total sem que os dois discordem.

**A CONTA NÃO ERA A PARTE DIFÍCIL, e descobrir isso é o achado do bloco.** O 1º colocado
de «Roma Pass vale a pena» já publica «soma dos avulsos × preço do passe, com ponto de
equilíbrio» — a seção 4 acima diz, desde 14/09/2026, que **não há vaga de formato**. O
que ninguém publica é **sobre o que** aquele ponto de equilíbrio foi calculado. Daí as
três regras que agora moram no esquema (`regra_da_cobertura_do_passe`) e que a
ferramenta publica:

1. **NÃO LIDA NÃO É NÃO COBERTA.** Atração pretendida sem `COBERTURA_DO_PASSE` fica fora
   do valor entregue **e é nomeada na tela**. Tratá-la como não coberta publica um «não
   paga» que a ilha não mediu; tratá-la como coberta publica o contrário. As duas são
   erradas, e a única frase honesta é que ninguém leu.
2. **O EQUILÍBRIO É SOBRE O QUE A ILHA LEU, NUNCA SOBRE O PASSE.** `atracoes_declaradas_pelo_passe`
   (o número da fonte) e a contagem das coberturas lidas vão para a tela **lado a lado**,
   e a frase do equilíbrio diz sobre quantas atrações ele saiu. Passe que declara 50
   atrações com 3 lidas **não tem equilíbrio publicável como equilíbrio dele**.
3. **DESCONTO COM TETO É FAIXA.** «Até 50%» entrega de **zero** à metade do avulso, e as
   duas pontas vão para a tela. É a mesma troca do `o_que_o_numero_e` da `FAIXA_DIARIA`
   um bloco atrás: o que sai da prosa para o campo não é o número, é **o que o número é**.

**O VEREDITO TEM TRÊS DESFECHOS, NÃO DOIS**, e o terceiro é o que esta ferramenta tem de
diferente. `paga` quando o passe se paga **até na ponta de baixo** da faixa; `nao_paga`
quando não se paga **nem na de cima**; e `depende_da_versao` quando a faixa **atravessa**
o preço do passe — ali existe bilhete em que ele paga e bilhete em que não paga, e as
duas coisas são verdade. Escolher uma seria a ilha escolhendo a versão no lugar de quem
viaja, que é a mesma recusa da 3.1 item 4. É também a lição que a ohmetria pagou no mesmo
dia um andar acima: **quem separa as duas causas no código separa as duas no texto.**

**O PONTO DE EQUILÍBRIO SAI DAS MAIS CARAS PARA AS MAIS BARATAS, e a ordem é declarada.**
É a ordem em que o passe rende mais, portanto a que dá o **menor** número de atrações — e
dizer «a partir de 3 atrações o passe paga» sem dizer **quais 3** seria um número sem
dono. A função devolve a ordem que usou e a tela nomeia as atrações. Ele é calculado nas
**duas pontas** da faixa: na de baixo o passe precisa de mais atrações, na de cima de
menos, e a diferença entre os dois números é exatamente «qual bilhete você compraria».

**AS SETE RECUSAS DURAS**, e três delas são novas nesta ferramenta porque a entrada é
nova: dias fora de 1–21, grupo fora de 1–12, cidade desconhecida, **escolha vazia** (sem
atração não há o primeiro lado da comparação), **atração repetida** (somaria o ingresso
duas vezes e o passe pareceria valer mais do que vale), **atração desconhecida** e
**o passe escolhido como atração** (ele é o outro lado da conta, não um item dela).

**O TETO DE 8 ATRAÇÕES NÃO É LIMITE DE BANCO, É LIMITE DE ESCOLHA**, e ele existe por
aritmética: o domínio desta ferramenta cresce em **2^n − 1** com o número de atrações
lidas numa cidade. Hoje são 4 cidades com 1 atração cada e **1.038** estados; com 8
atrações numa cidade só seriam 255 subconjuntos × 252 combinações de dias e pessoas,
nela sozinha. O número está escrito no portão **a partir desta seção**, não lido da
ferramenta — régua que toma o limite da coisa que ela mede não mede o limite.

**O QUE O BANCO AINDA NÃO TEM, e por que a falta não é descuido.** `coberturas_de_passe`
tem **zero** registros e **nenhuma** das cinco experiências é `passe_de_cidade` — o
valor está no vocabulário desde 14/09/2026 sem um registro que o use, e o aviso
`vocabulario_sem_lastro` o conta em toda passada. Carregar exige **ler o preço e a
cobertura na fonte de quem vende o passe**, e o egresso desta nuvem recusa os cinco
domínios que o corpus mediu: `romapass.it`, `turismoroma.it`, `lisboacard.org`,
`visitlisboa.com` e `civitatis.com.br`, todos em `000` em 22/10/2026, com
`raw.githubusercontent.com` em 301 na mesma passada. Carregar de cabeça exigiria inventar
**três** coisas — o preço do passe, a lista de atrações que ele cobre e a regra de reserva
de cada uma — e a terceira é justamente a que o bloco 1 mediu como a que envelhece
primeiro. **O Angkor Pass não foi recategorizado:** ele é `ingresso_de_sitio_publico`
desde 14/09/2026, cobre **um sítio** e não uma cidade, e trocar a categoria dele para dar
lastro ao vocabulário seria mover o dado para caber na ferramenta.

**O QUE ISSO FAZ A F3 PUBLICAR HOJE:** em todos os **1.008** estados válidos ela publica a
soma dos avulsos — que é **metade** da pergunta — e fecha com `sem_passe_lido`, dizendo
que a outra metade não foi lida. A recusa nunca diz que a cidade **não tem** passe: o
vocabulário da cobertura nasceu sem lastro, e a `regra_de_crescimento_de_vocabulario` do
esquema proíbe frase de inexistência enquanto for assim. **O portão cobra essa distinção
em cada estado** — é a primeira vez nesta ilha que aquela regra do esquema é conferida por
código em vez de obedecida de boa vontade.

**O QUE O PORTÃO ACHOU, antes do commit, e os quatro são de honestidade e não de
aritmética:**

- **A F2 SOMAVA O PASSE COM O INGRESSO QUE O PASSE INCLUI.** Medido no mundo de bancada do
  passe: a linha de experiências de Roma publicava **«€100 a €148»** para 2 pessoas — o
  ingresso (€36 a €44) **mais** o passe que inclui o ingresso (€64 a €104) —, e a tela
  nomeava os dois lado a lado como se fossem dois programas. **Pagar a mesma visita duas
  vezes.** A F2 passou a descartar `passe_de_cidade` da linha e a **nomear** a recusa,
  mandando quem pergunta para a F3 — e a metade mais traiçoeira era a segunda: a **fonte**
  do passe continuava na prestação de contas de um número que a página não publica.
- **AS RECUSAS DURAS PUBLICAVAM ID DE REGISTRO NA TELA.** Duas delas ecoavam o id da
  atração entre aspas, que é texto de bastidor da fábrica pela 32.4 — a mesma cicatriz do
  `unidade_de_preco` da F1 e do caminho de arquivo da ohmetria. **A causa de ninguém ver
  era estrutural:** a varredura do portão dava `continue` na borda, então as sete frases de
  recusa dura nunca passavam pela régua de acento, de frase proibida nem de bastidor.
  Agora passam.
- **O EIXO `null` NÃO CONFERIA `dias_de_uso`.** As duas direções da regra no validador
  cobravam `por_quantidade` e proibiam os outros eixos, e o `null` — a experiência de
  **uma** versão, que é exatamente o que um passe de validade única é — não caía em
  nenhuma das duas e passava calado. A conferência virou função chamada dos dois lugares.
- **A CONCORDÂNCIA, pela terceira vez nesta pasta.** A primeira versão publicou «1 atração
  em Veneza **custam** €90» e «dentro **das 1** atração». Não se vê lendo o código; se vê
  lendo a frase, e é por isso que o portão lê a frase.

**E uma régua que nasceu porque as duas metades não se falavam:** a validade do preço
(`validade_do_preco` do esquema) era **aviso de bancada** dentro do validador, e a F3 é a
primeira ferramenta que a leva para a **tela** — «este preço foi lido há 38 dias e esta
ilha considera 60 o prazo». Em vez de uma segunda cópia da regra, ela virou
`f1.preco_vencido`, e o portão da F3 **compara os dois vereditos versão por versão do
banco**: eles discordarem quer dizer que uma das duas está errada e nenhuma das duas sabe.

---

## 5. A FRONTEIRA ENTRE `constantes.json` E O BANCO — e por que ela importa aqui mais que nas outras ilhas

`constantes.json` guarda **parâmetro que atravessa ferramenta e experiência**: imposto,
câmbio, faixa de gorjeta, regra de validade de preço. **Preço de experiência NÃO entra
aqui** — ele é banco, nasce no bloco 3 com `data_leitura`, e é o produto desta ilha.

**A tarifa da gôndola é o caso-limite e fica de fora de propósito.** Ela é preço de
experiência (banco), mesmo sendo tabelada por poder público; aparece neste arquivo como
**exemplo trabalhado**, com a fonte citada, e **não é copiada para `constantes.json`**.
Duas cópias da mesma decisão em dois arquivos é exatamente o defeito que a Robometria
pagou em 14/09 com a tabela de artigos de publicador, e que a Aquametria pagou no mesmo
dia com um campo batizado duas vezes. **Quem for escrever o bloco 3 lê a 2.2 e grava o
número no banco, uma vez.**

---

## 6. O QUE ESTE BLOCO DEIXA ABERTO, com o que cada coisa trava

| Aberto | Trava o quê | De quem depende |
|---|---|---|
| **Câmbio sem canal** (`cambio-eur-brl`, `cambio-usd-brl` pendentes) | a linha em real da F1 e da F2 — **não trava as ferramentas**, que publicam na moeda do operador | abertura de rede para uma fonte de câmbio datada. **Somar ao despacho de rede do bloco 1**, que já está aberto para o domínio da ilha |
| **Leitura direta de fonte primária fechada** | o nível de fonte de tudo que foi colhido (elo mais fraco, seção 10) | a mesma abertura de rede |
| **Seção pendente do `VOZ.md`** — as 10 a 15 legendas reais do @jornadafly | **a primeira página**, pelo `PROMPT.md` desta ilha | o Raphael |
| **Identidade visual** não aprovada | o bloco 3b | o Raphael |
| **Nenhum programa de afiliado cadastrado** | a comissão, **não a página**: o piso da 2.9 é link cru e não espera ninguém | o Raphael, e só **depois** de conteúdo no ar |
| **Rede da ilha bloqueada** | 3b em diante | o Raphael (despacho ALTO, bloco 1) |

**O bloco 3 ESTÁ FEITO** — banco carregado em 14 e 15/09/2026 e migrado em 22/10/2026 —
e este arquivo é quem obrigou o esquema a ter `unidade_de_preco`, `capacidade_maxima`,
`versoes[]`, `temporada`, `faixa_etaria`, `data_leitura` e
`afiliado.url_busca_produto`. *(A linha anterior dizia "próximo bloco desbloqueado: o 3"
e estava velha desde 14/09/2026; corrigida em 22/10/2026 pela execução que migrou a
faixa etária. `faixa_etaria` agora é campo da **VERSÃO** — ver 2.6.)*

**AS TRÊS FERRAMENTAS ESTÃO ENTREGUES COMO REGRA** — F1 e F2 em 22/10/2026 (2.11 e 3.1)
e a F3 no mesmo dia (4.1) —, e **nenhuma** delas é página: sem casca não há snippet, e um
render de bancada que serve menos do que o site serve é a cicatriz que a seção 8 do
`ARQUIPELAGO.md` mais cobra. O PHP das três, quando nascer, é **tradutor** da referência,
frase a frase. *(A linha anterior dizia "próximo bloco desbloqueado: o 4 — a F1 como
REGRA" e estava velha desde 22/10/2026 de manhã; corrigida no fim do mesmo dia pela
execução que entregou a F3.)*

**Próximo bloco desbloqueado: o que o Raphael destravar.** As três ferramentas que esta
ilha podia escrever sem site estão escritas, e **as três publicam menos do que sabem
calcular, por falta de DADO que esta nuvem não alcança**:

| Ferramenta | O que falta | Quem destrava |
|---|---|---|
| **F1** | nada de regra. Falta a **página** | o Raphael: passos 2 a 8 da seção 11 |
| **F2** | `faixas_diarias` com zero registros — hospedagem, alimentação e transporte local | abertura de `numbeo.com`, `booking.com` e `civitatis.com.br` no egresso |
| **F3** | `coberturas_de_passe` e os passes com zero registros | abertura de `romapass.it`, `turismoroma.it`, `lisboacard.org`, `visitlisboa.com` e `civitatis.com.br` |

**Os dois itens de trabalho de arquivo que sobram, e os dois são pequenos:** o **bloco 5**
(artigos-âncora pareados com cada ferramenta) e o **bloco 6** (lista de prospecção do
widget, `publicar: false`). O **5b** (malha) e o **5c** (cluster free tour) dependem da
casca. Depois deles, esta ilha não tem mais bloco que não precise do Raphael — e isso
está escrito aqui para a próxima execução não gastar a vez descobrindo.

> **O BLOCO 5 SAIU EM 23/10/2026 — ver a seção 7 acima.** Quatro artigos escritos como
> regra e dois pré-registrados, estes esperando dado de coleta e não trabalho de escrita.
> **Sobra o bloco 6, e ele é o último item de arquivo desta ilha.** Depois dele não há
> bloco que não precise do Raphael: a casca (3b), os passos 2 a 8 da seção 11, a liberação
> do domínio no egresso e as fontes de diária e de passe — todas de navegador, todas dele.

---

## 7. OS ARTIGOS-ÂNCORA — o bloco 5, e por que eles não são texto digitado (23/10/2026)

A fila desta ilha pede, no bloco 5, **artigos-âncora pareados com cada ferramenta, na
mesma execução**. Este bloco entregou **quatro escritos** e **dois pré-registrados**, e a
decisão que mais importa aqui é de **forma**, não de conteúdo.

### 7.1 O artigo é MONTADO do banco, nunca redigido

Artigo escrito à mão carrega número digitado, e **número digitado envelhece calado**: no
dia em que o banco for recarregado, a ferramenta publica o preço novo e o artigo continua
publicando o velho, com a mesma cara de verdade. Nesta ilha isso não é um detalhe de
manutenção — **o preço datado É o produto**, e preço cravado como atual sem a data da
coleta é o defeito que o `VOZ.md` chama de "o mais grave possível nesta ilha".

Então a regra mora em `ferramentas/artigos-referencia.py`, o arquivo sai de
`ferramentas/gerar-artigos.py` para `dados/artigos-ancora.json`, e **toda frase de preço é
devolvida pela `f1-referencia.py`** — a mesma regra que a bancada mede. O que o arquivo da
referência guarda é o que **nenhuma ferramenta sabe**: qual consulta o artigo ataca, quem
ocupava a SERP dela no dia da medição, qual é a mãe na árvore, quais são as irmãs e para
onde vai o link de compra.

É o mesmo desenho das três ferramentas: a regra em Python, o PHP como **tradutor** dela
quando a casca nascer, nunca uma segunda regra.

### 7.2 A árvore, e por que os quatro moram na mesma mãe

Nível 1 `/guias/` · nível 2 **`/guias/quanto-custa/`** · nível 3 a pergunta, com as
palavras que a pessoa digita. "Quanto custa" é, literalmente, um dos três itens do menu que
o `VOZ.md` define, e é a palavra da pessoa.

**Agrupar por cidade teria sido o erro barato:** cada cidade do banco tem **uma**
experiência hoje, e categoria nasce com no mínimo três filhas — uma filha por categoria é
cluster ralo, que não passa autoridade nenhuma. Com os quatro na mesma mãe, a categoria
nasce com quatro filhas e **cada página recebe três irmãs apontando para ela**.

**A janela de irmãs ROTACIONA:** cada página leva as até-quatro irmãs que vêm **depois**
dela na ordem do mapa, dando a volta no fim. O grafo que sai é circulante, então o grau de
**entrada** de toda filha é igual ao de **saída**, hoje com quatro e no dia em que a
categoria tiver dez. Janela fixa é trava que depende de a categoria ser pequena, e o portão
mede a conta **na direção de quem aponta** — contar só o que sai fica verde nos dois
mundos.

### 7.3 Dois campos para a mesma pergunta, e a diferença é uma regra

| Campo | O que é | Vai para a tela? |
|---|---|---|
| `consulta_alvo` | a consulta como foi **medida**, do jeito que a pessoa digita — e gente digita sem acento | **não** |
| `titulo_na_tela` | a mesma pergunta em português correto | **sim**: `<title>`, H1, trilha e âncora das irmãs |

Publicar a consulta crua na tela seria publicar português sem acento, que é a cicatriz da
Robometria. Esconder a consulta crua seria perder a correspondência exata que faz a página
ser achada. O portão cobra que o título **não perca nenhuma palavra** da consulta e que só
possa **ganhar palavra de ligação** (artigo e preposição): ele acentua e capitaliza a
pergunta da pessoa, não a reescreve.

### 7.4 A fronteira com a calculadora, para a ilha não disputar consigo

**A consulta paramétrica é da ferramenta; a consulta crua é do guia.** O guia responde
"quanto custa X" e a ferramenta responde "quanto custa X **para N pessoas**" — e o portão
reprova título de guia que traga "para N pessoas" ou "para o seu grupo". Cada guia linka a
calculadora no corpo e no botão **Calcular**, com o parâmetro da própria página já na URL;
a calculadora linka o guia que a explica. Duas páginas na mesma consulta é a ilha
competindo contra si mesma, e o portão também reprova duas páginas com a mesma
`consulta_alvo`.

### 7.5 O molde: caixa de resposta, compra, tabela, dobras

Na ordem, de cima para baixo: **caixa de resposta** (o número e a condição em uma frase,
com a data da leitura dentro dela) → **"Monte / Compre o que esta resposta pede"**, de 2 a
4 itens, cada um com os dois botões (**Calcular**, que leva à ferramenta com o parâmetro, e
**Ver na plataforma**, que leva à saída de compra) → **tabela de casos resolvidos**,
visível e nunca recolhida, cobrindo 1, 2, 4 e 6 pessoas por versão → o resto em dobras:
como chegamos no número, o que está incluso e o que não está, a escada de versões, crianças
e jovens, cada versão vendida pelo operador uma por uma, o que a página não responde, e
"Como sabemos".

**Nenhuma palavra sai da página**: o que vai para a dobra continua no HTML servido. E
**nenhum item vivo tem link de compra** — nenhuma das cinco experiências desta pasta é um
ser vivo, e isso fica dito em vez de suposto.

### 7.6 O valor de terceiro tem dono, e é o diferencial medido

O número com que a ilha **discorda** também vai para a tela. Na gôndola, quatro dos sete
ocupantes da SERP publicam valores que se contradizem sobre uma tarifa de ato oficial e
**nenhum diz em que dia leu** — dizer quem publicou o quê, com a data, é a única coisa que
nenhum deles faz. Então o portão deixa passar um valor que o banco **não** autoriza
**somente** dentro de uma frase que nomeia quem o publicou e quando foi lido. Sem o nome, é
número sem dono, e reprova. *(Foi a primeira coisa que este portão pegou, e ele pegou contra
mim: a regra escrita sem essa exceção reprovava a prestação de contas da gôndola, que é
justamente o diferencial da ilha.)*

### 7.7 O que o portão mede, e a régua que foi tentada três vezes e NÃO existe

`python3 ferramentas/artigos-referencia.py` monta e confere; `mutacoes-artigos.py` quebra e
exige que ele veja — **43 quebras, 43 reprovadas, zero morte e zero inerte** em
23/10/2026, 39 por artigo e 4 pelo conjunto.

**E uma régua não existe, por medição e não por esquecimento.** A acentuação correta foi
tentada em três formas no mesmo dia, e as três reprovaram texto impecável:

1. *"todo título tem de ter um acento"* — reprovou três páginas certas; "quanto custa subir
   na torre eiffel" não tem uma letra acentuada e está escrito corretamente;
2. *"palavra acentuada num lugar não aparece crua noutro"* — **25 reprovações** em texto
   impecável, porque em português o par sem acento costuma ser **outra palavra**: "e" e "é",
   "esta" e "está", "da" e "dá";
3. *"parágrafo com 12 palavras ou mais tem de ter um acento"* — reprovou "A partir de
   quantos dias de visita o Angkor Pass de 3 dias paga?" e a frase de divergência da
   GetYourGuide. Catorze palavras, nenhum acento, as duas corretas. Subir o corte reduz o
   falso positivo e não o elimina.

**O que isso decide:** acentuação correta **não é verificável localmente** — é julgamento
sobre cada palavra, e **portão que reprova texto certo é pior que portão nenhum, porque
ensina a ignorar o vermelho**. O que sobra e é verificável está no portão: mojibake, que é
mecânico e inequívoco, e a procedência de todo valor da tela. A acentuação das frases é
garantida **na fonte**, pelas três referências, que nascem com a regra.

### 7.8 Os dois artigos que NÃO foram escritos, e o que destrava cada um

A fila pede um artigo por ferramenta. **Dois não foram escritos, e não por falta de tempo:
a ferramenta pareada não tem resposta para publicar.** Artigo cujo título promete um número
que a página não entrega é exatamente o defeito que o bloco 1 mediu nos concorrentes.

| Pareado com | Consulta | Por que não foi escrito | Destrava quando |
|---|---|---|---|
| **F2** | `quanto custa um dia em veneza para 2 pessoas` | a F2 soma quatro linhas e hoje publica **uma**: `faixas_diarias` tem **zero** registros. O artigo prometeria o dia inteiro e entregaria o passeio | houver faixa de diária para Veneza nas três naturezas, cada uma com publicador nomeado, URL e data de leitura |
| **F3** | `roma pass vale a pena` | **zero** passes e **zero** coberturas no banco: o veredito que o título promete não existe. E Roma tem **uma** experiência — julgamento de passe sobre uma atração só não é julgamento de passe | houver o Roma Pass com preço e data próprios **mais** a cobertura par por par com cada atração de Roma, cada par com fonte e data próprias |

Os dois esperam **coleta de navegador**, e as fontes estão recusadas no egresso desta
nuvem. A regra dos dois está inteira: no dia em que o dado entrar, o artigo é **montagem**,
não pesquisa.

### 7.9 Nada foi ao ar, e não podia

Esta ilha não tem WordPress, não tem Sync e não tem `/status`, e `jornadafly.com.br` não
está na lista de Domínios permitidos deste ambiente — remedido em 23/10/2026 às 10h16Z:
**000 em quatro medições**, com `aquametria.com.br` e `robometria.com.br` em **200 nas
quatro de controle**. `publicar` sai `false` em todo artigo, com o motivo dentro dele.

---

## 8. A LISTA DE PROSPECÇÃO DO WIDGET — o bloco 6, e a régua que o banco escreve (23/10/2026)

A seção **14.7** do `ARQUIPELAGO.md` diz, com todas as letras, que a prospecção do widget em
lojas é a **única alavanca de link do projeto**, e que ela **vale mais no começo do que no
fim: backlink é o que faz o robô voltar**. Este bloco é essa lista nesta ilha. Mora em
`dados/prospeccao-widget.json` (o banco, `publicar: false`), com o arquivo de leitura
`dados/prospeccao-widget.md` **gerado** e quatro portões: `prospeccao-referencia.py` (a
régua), `gerar-prospeccao.py`, `validar-prospeccao.py` e `mutacoes-prospeccao.py`.

### 8.1 A lista não começou do zero — ela já estava medida e ninguém a tinha lido assim

O bloco 1 mediu **69 domínios** de SERP em pt-BR e os registrou como **procedência**, isto é,
como *concorrência*. Entre eles há operador com site próprio, concessionária de bem público e
plataforma, cada um **rotulado pelo próprio corpus**. Ler a mesma medição na outra direção é
o que este bloco faz: `bondinho.com.br` não entrou nesta lista por busca nova, entrou porque
o corpus já o tinha escrito como *«operador, e três URLs dele»* em 14/09/2026.

**É a mesma família de defeito que esta ilha e a ohmetria já pagaram: duas metades contando a
mesma coisa sem nunca se falarem.** Aqui as duas metades são o corpus de buscas e a lista de
prospecção, e o portão as faz conversar por regra — toda consulta citada no banco tem de
existir em `dados/corpus-buscas.md`, e todo domínio que diz vir do corpus tem de aparecer lá.

### 8.2 O BARRAMENTO, e ele sai de uma decisão que a ilha já tinha tomado

Dos seis clusters que o bloco 1 mediu, a ilha declarou que **não disputa um**: o **A2**,
*«quanto custa <experiência>»*, porque *«disputar 'quanto custa o ingresso X' contra o
operador é perder, e não é preciso»*. Daí a régua, e ela é curta:

> **Quem ocupa consulta de cluster que esta ilha DISPUTA não hospeda a ferramenta que a
> disputa.** É BARRADO, com a consulta nomeada.

O caso que prova o valor disso é o `northbound.is`: operador islandês com site próprio, que
ocupa *«vale a pena alugar carro na islândia»* — a consulta que o próprio bloco 1 chama de
**«o melhor encaixe entre recorte e monetização que este levantamento encontrou»**. O
operador que hospedaria a ferramenta é o mesmo que ocupa a página que a ilha mais quer
escrever. E o `romapravoce.com` mostra por que a régua é **escada** e não soma de pontos: ele
é operador **e** concorrente ao mesmo tempo, e tratar os dois lados como pesos somáveis o
deixaria passar. O barramento vem primeiro.

### 8.3 A RÉGUA DA OFERTA LÊ O BANCO, NÃO A LISTA

Nenhuma ferramenta é oferecida a ninguém se a ilha não souber servi-la **hoje**, e quem
decide isso é `dados/experiencias.json`, contado em toda passada:

| Ferramenta | Só é ofertável se | Nunca é ofertável a |
|---|---|---|
| **F1** | o candidato atende experiência **que o banco tem** e vende **a mesma versão** que o banco preça | quem vende versão que **inclui** a do banco — a F1 serviria, ao visitante dele, o preço da versão barata que o produto dele embute |
| **F2** | o banco tiver ao menos uma `FAIXA_DIARIA` | — |
| **F3** | o banco tiver passe **e** cobertura | **quem vende passe de cidade**: o veredito dela pode ser «não vale», e esse é o produto do anfitrião |

**A linha da F1 é a decisão deste bloco.** Nas outras ilhas o widget *ajuda* o anfitrião a
vender: a calculadora dimensiona o equipamento que a loja tem no catálogo. Aqui a ferramenta
responde *«vale a pena?»* e *«quanto custa para o seu grupo»* — e pode servir um número que
**mina** quem a hospeda. É o que acontece com o `viagemitalia.com`, único candidato
brasileiro que atende experiência do banco: ele vende o tour guiado do Coliseu a €75 por
pessoa **com o ingresso dentro**, e o banco preça o ingresso avulso. Ferramenta que mina o
anfitrião não se oferece ao anfitrião. É a mesma família da **ATENÇÃO DE ESCOPO** que a lista
da aquametria escreveu para a loja de marinho, um andar acima: lá o número ficava fora do
escopo declarado, aqui ele **compete com quem hospeda**.

### 8.4 O que este bloco achou, e é uma cadeia de cinco elos com uma causa só

**A lista existe, a régua existe, e NENHUM dos 25 candidatos tem ferramenta ofertável hoje.**
A causa é **uma**, já registrada três vezes nesta ilha sem nunca ter sido ligada à alavanca de
link:

1. o egresso desta nuvem recusa o domínio da ilha e as fontes de preço (15/09, 18/09, 22/10 e
   hoje);
2. com a rede fechada, o bloco 3 registrou que `ingresso_de_sitio_publico` era *«o único tipo
   reproduzível enquanto o egresso estiver fechado»* — e o banco nasceu com **quatro**
   experiências de tarifa pública;
3. **três dos quatro operadores do banco são poder público** (gondoleiros com tarifa da
   prefeitura de Veneza, Angkor Enterprise, Parco archeologico del Colosseo) e o quarto é
   concessionária francesa. Poder público não instala widget de afiliado;
4. logo a F1 — a única das três com dado para servir — não tem a quem ser oferecida;
5. e o **critério de entrada do bloco 1** dizia justamente o contrário do que o banco
   carregou: *«prefira experiência de operador privado, com versões vendidas diferentes entre
   si e sem tabela pública»*.

**O que isso muda na leitura do bloqueio de rede:** ele não atrasa só coleta de preço. Ele
**decidiu a composição do banco**, e a composição do banco **parou a única alavanca de link do
projeto** nesta ilha. Esse custo nunca esteve escrito num lugar só.

**E o que destrava é barato e está nomeado:** UMA experiência de operador privado brasileiro
no banco abre a linha de prioridade 1 desta lista. O candidato está medido — o **Parque
Bondinho Pão de Açúcar** vende direto, pelo próprio site, mais de uma versão da mesma
experiência (bonde exclusivo, tour ecológico com café, bonde + aula de caipirinha). Carregá-lo
exige ler a página de tarifa dele na fonte, e `bondinho.com.br` devolveu **000** às 13h28:28Z
de hoje.

### 8.5 O que os portões cobram, e o que eles acharam no próprio texto

- **Presença, nunca ausência.** Campo de fato aceita `true` ou `null`; `false` é **recusado**.
  É a regra que o `ARQUIPELAGO.md` já carrega, vinda da `regua-prospeccao.py` da aquametria.
- **Toda afirmação tem evidência que a NOMEIA.** `afirma` é uma **lista** de campos: uma
  medição sustenta vários fatos de uma vez, e dizer **quais** é o que separa evidência de
  impressão. A primeira versão deste banco afirmava 68 fatos sem evidência nomeada, e **foi o
  portão que os achou** — o conserto não foi afrouxar a regra, foi afirmar menos: oito campos
  viraram `null` (entre eles `tipo` do `ingressomachupicchu.com`, que o nome do domínio
  *parecia* provar, e a venda de passe dos três revendedores de Lisboa e Roma).
- **Nada de derivado gravado.** `prioridade` e `ferramentas_ofertaveis` não existem no banco:
  prioridade escrita à mão é opinião com cara de dado, e envelhece calada.
- **A régua de acento retira o que está entre craseadas antes de olhar.** A primeira versão
  dela reprovou `dados/experiencias.json` e `prospeccao-referencia.py`, que são **texto
  legítimo**. A saída não foi uma heurística melhor, foi estrutura — a quarta trava da mesma
  família que o `ARQUIPELAGO.md` já ensina: *quando o texto legítimo e o proibido são a mesma
  palavra, quem decide é a estrutura, nunca a vizinhança*.
- **A BANCADA LÊ A PROSA DESTA SEÇÃO E DO ACHADO, e conferiu contra o dado.** É a terceira
  conta que a seção 8 do contrato pede, e ela **pegou um erro meu**: o texto dizia que o
  corpus mediu **64** domínios. São **69** — a contagem de cabeça usou uma lista de
  terminações que deixava `.is`, `.fr`, `.pt`, `.paris`, `.kh` e `.cz` de fora. O conserto não
  foi trocar o número: foi a bancada passar a conferi-lo em toda passada.
- **A regra da F3 sobre vendedor de passe não tem nenhum caso neste banco hoje**, porque a
  venda de passe não foi medida em ninguém. A regra existe e é a **bateria de mutações** que
  prova que ela morde, não uma linha da lista. Portão que nunca reprovou nada é decoração.

### 8.6 O próximo passo desta lista não é da Fundação

Nenhum dos 25 candidatos é alcançável desta nuvem — medido nesta execução e não herdado: às
13h28:28Z de 23/10/2026, `bondinho.com.br`, `www.toureiffel.paris`, `viagemitalia.com`,
`www.panrotas.com.br` e `www.civitatis.com` devolveram **000**, com `aquametria.com.br` em
**200** na mesma passada. É a 20.3 exercida antes de escrever a regra que exige a fonte. Por
isso `contato` e `plataforma_do_site` estão `null` em todas as linhas, e a bancada **proíbe**
que sejam preenchidos. Abrir cada domínio, confirmar canal de contato e plataforma, e só então
escrever a abordagem é trabalho de navegador.

### 8.7 E há um achado de método, que vale para quem continuar esta lista

Três buscas desta execução foram dirigidas a *«receptivo/agência brasileiro com site
próprio»* em Roma, Paris e Veneza. **As três devolveram portal de conteúdo e plataforma** —
`eurodicas`, `maladeaventuras`, `grupodicas`, `dicasdaitalia`, `tiqets`, `civitatis` —, isto
é, devolveram **a concorrência**, não os candidatos. Os únicos receptivos que apareceram **por
nome** vieram da **imprensa de trade** (`panrotas.com.br`, `mercadoeeventos.com.br`): Hola
Tour em Paris, a representação da Carrani para o mercado brasileiro, e a confirmação de que
`bondinho.com.br` é o canal de venda do próprio operador.

**A razão é estrutural e não é azar de consulta: operador e receptivo não disputam a SERP de
«quanto custa» — logo não são achados por ela.** Quem continuar esta lista busca em trade, e
não em SERP de consumidor. É por isso que os dois veículos estão no banco como
`imprensa_de_trade`, prioridade 3: não são alvo de widget, são o instrumento que acha o alvo.


## 9. A ELEGIBILIDADE — o preço de quem prova o que não é idade (27/10/2026)

Nasceu na carga do **Parque Bondinho Pão de Açúcar**, a quinta experiência do banco e a
primeira brasileira. Nasceu de um dado, não de uma previsão, e o dado é este: **o mesmo
Bilhete Bondinho custa R$ 205, R$ 160 e R$ 89**, e o que muda não é quantidade, nem
escopo, nem momento — é **quem compra**.

| O que o operador vende | Preço | O que se prova |
|---|---|---|
| Bilhete Bondinho | R$ 205 | nada: é a tarifa cheia |
| Promocional para Brasileiros | R$ 160 | ter nascido **e** morar no Brasil |
| Promocional Estado RJ | R$ 89 | ter nascido **ou** residir no estado do Rio |
| Bilhete Criança | R$ 102 | idade de 3 a 12 anos → é `faixa_etaria` |
| Bilhete maiores de 60 anos | R$ 102 | idade acima de 60 → é `faixa_etaria` |

### 9.1 Por que não cabia em nada que já existia

O esquema tinha **três** eixos de versão — `por_quantidade`, `por_escopo`, `por_momento` —
e nenhum descreve residência. `faixa_etaria` também não serve: o próprio esquema diz que o
campo `se_nao_cumprir` dela é *"o que o operador cobra de quem não prova a **IDADE**"*.
Residência não é idade, e as duas **coexistem na mesma versão** do Bondinho.

Sem a entidade, a carga tinha duas saídas e as duas eram erradas:

1. **Gravar os cinco preços como versões irmãs** — inventando um eixo que o operador não
   vende, e fazendo o seletor da F1 oferecer "versões" que são a mesma coisa.
2. **Gravar só o R$ 205** — publicando, numa ilha escrita em português do Brasil, o preço
   de estrangeiro quando o operador cobra **28% menos** do próprio leitor.

### 9.2 A conta NÃO muda, e isso é regra

O total continua saindo da **tarifa cheia**. Duas razões, as duas já escritas:
`regra_de_divergencia.sem_autoridade` resolve para o **maior** e `erro_caro` é
*subestimar* — quem chega à bilheteria sem o comprovante paga o cheio. O que a tela ganha
é a **escada de quem compra**, com a condição, a frase da fonte e o que se paga sem provar.

### 9.3 A soma não se presume, e isso tem número

`acumula_com_faixa_etaria` é campo **obrigatório**, e nasceu obrigatório por uma medição.
A leitura devolveu, na página do operador, que a meia-entrada vale para o Bilhete Bondinho,
o Acesso Rápido e a Visita Guiada e **não vale para as tarifas promocionais**. E a imprensa
dos 114 anos declarou o preço composto: **R$ 89 para adulto e R$ 44 para criança de 3 a 12
anos** no bilhete de morador do Rio.

**Metade de R$ 89 é R$ 44,50. O operador cobra R$ 44.** Se a F1 tivesse autorizado somar a
faixa etária à elegibilidade, ela publicaria cinquenta centavos inventados na página do
dinheiro, numa conta que pareceria certa — a aritmética estaria correta; só a pergunta é
que não existia. É por isso que `acumula` nunca é `null` numa versão que tem faixa, e que
`acumula: true` exige a frase da fonte que **autoriza** somar: silêncio não autoriza soma.

### 9.4 Os dois sentidos da troca, e o que a régua mede

A troca entre faixa etária e elegibilidade é **silenciosa**: os dois campos guardam um
preço menor com uma condição escrita ao lado, e lidos de longe parecem a mesma coisa. A
régua reprova nos **dois** sentidos, e a bateria mede os dois:

- **idade em elegibilidade** → `condicao` ou `rotulo` com padrão de faixa de idade reprova;
- **residência em faixa etária** → `condicao` ou `rotulo` com morador, residente, nascido,
  brasileiro, estrangeiro ou nacionalidade reprova. **É este o sentido que a ilha ia
  errar**: os cinco preços vieram na mesma leitura, e a saída barata era chamar os cinco de
  faixa.

### 9.5 A MEIA-ENTRADA BRASILEIRA NÃO É NENHUM DOS DOIS, e por isso não entrou

Os bilhetes de Trilheiros declaram `Meia-entrada: R$ 70` e `R$ 32` ao lado do adulto, e os
dois números **não foram gravados**. Não é lacuna por descuido: a meia-entrada brasileira
**empacota idade, vínculo e deficiência numa só palavra**, e cada uma das três se prova de
um jeito diferente. Gravá-la em `faixa_etaria` diria que o operador cobra por idade o que
ele cobra por condição; gravá-la em `elegibilidade` afirmaria uma prova que a fonte não
fez. A página do próprio operador que a define — «Outras opções de meia-entrada», em
`sac.bondinho.com.br` — **voltou por nome na busca e não foi lida**, porque o egresso
recusa o domínio. Está contado como dívida, com o endereço de releitura escrito.

### 9.6 TRÊS DEFEITOS DA MESMA FAMÍLIA, achados na mesma carga

Nenhum deles é da elegibilidade: os três são **réguas escritas num mundo sem real**, as
três corretas enquanto o mundo não mudou, e as três erradas no dia em que ele mudou. O
Bondinho é a primeira experiência deste banco que cobra em `BRL_do_operador` — valor que
estava no vocabulário desde 14/09/2026 **sem um registro que o usasse**.

| Onde | O que fazia | Por que passava |
|---|---|---|
| `validar-banco.py` | o contador `experiencias_com_preco_em_brl` era incrementado **dentro do ramo de ERRO** da conferência de moeda: contava versão cuja moeda *discorda* da cidade | publicava `0`, e `0` era a verdade **por acidente** — nenhuma experiência cobrava em real |
| `teste-f1.py` | afirmava que **`R$` nunca aparece** na tela | todo `R$` só poderia ser conversão com o câmbio pendente. **288 frases de tela** passaram a carregar `R$` legitimamente, e ele reprovava todas — número refeito depois do conserto, varrendo as respostas da F1 de 1 a 12 pessoas |
| `f1-referencia.py` | somava **IOF de 3,5%** em toda versão | IOF é imposto de **compra internacional**; publicou `R$ 144,90` num bilhete de R$ 140 |

**O terceiro é o pior, e por uma assimetria:** os dois primeiros erram alto — um reprova o
certo, o outro publica um número redondo que ninguém confere. O da F1 **cobrava do leitor
um imposto que ele não paga**, na página do dinheiro, com a aritmética certa.

O conserto dos três é o mesmo movimento: **perguntar a moeda**. O contador conta versão em
real; o portão do câmbio passou a proibir **conversão** e não o símbolo (por *contenção*: o
símbolo na tela tem de caber no conjunto de moedas que os registros daquela experiência
declaram, o que permite **citar** a plataforma em dólar e continua proibindo converter); e
o IOF só entra quando `moeda != BRL_do_operador` — com a linha do cartão dizendo, em compra
em real, **por que** não há IOF, porque linha que não se aplica não some calada da tela.

### 9.7 O que esta carga achou e NÃO consertou

- **`eixo_das_versoes` é singular e esta experiência tem três eixos ao mesmo tempo**
  (escopo entre bilhetes, momento na tarifa de sexta e sábado, quem compra nas
  promocionais). Hoje isso se acomoda: o escopo fica no eixo, o momento mora em
  `acrescimos`, que já existia, e quem compra é a entidade nova. Nada foi construído para
  isso, e fica nomeado.
- **A `resolucao` é de UMA versão por experiência** (`versao_resolvida` é campo único). O
  Acesso Rápido tem o próprio operador publicando **R$ 285 numa página e R$ 295 no blog**,
  e não há onde gravar a segunda resolução — então o preço dele ficou `null`, com a causa
  escrita. Preço errado por R$ 10 na página do dinheiro custa mais que preço ausente com a
  causa escrita.
- **A escada de fontes não previu a fonte que discorda DE SI MESMA.** Ela resolve conflito
  *entre* níveis e diz, sobre o empate, apenas que *"dentro do mesmo nível, ninguém
  vence"*. O site do operador discorda de si em **quatro** números (205/185, 89/80,
  160/150, 285/295), e foi preciso quebrá-lo em **duas fontes** para que a divergência
  pudesse sequer ser gravada: declaração aponta para uma `fonte`, e uma fonte não pode
  divergir de si.
- **`declaração` não pode discordar de uma ELEGIBILIDADE**, só de uma VERSÃO. Três das sete
  declarações desta carga discordam de elegibilidades e ficaram com `versao: null`, o que
  pelo esquema as tira da resolução e as manda para a tela como conteúdo.
