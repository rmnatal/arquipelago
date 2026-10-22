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

**Próximo bloco desbloqueado: o 4 — a F1 como REGRA**, no desenho que a ohmetria usou na
F1 dela: a referência em Python (entrada → resposta inteira, já em frase acentuada),
a tabela pré-renderizada e os portões, sem PHP enquanto não houver casca. Não depende de
site, de domínio, nem da rede bloqueada — e o PHP, quando nascer, é **tradutor** da
referência, frase a frase.
