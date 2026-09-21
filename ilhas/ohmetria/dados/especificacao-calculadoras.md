---
titulo: Especificação das ferramentas — Ohmetria
bloco: 2
gerado_em: 2026-09-14
publicar: false
---

# Especificação das ferramentas — Ohmetria

Bloco 2 da fila. Define **o que cada ferramenta responde, com que entrada, com que
saída, com que fonte, e o que ela se RECUSA a responder**. Nenhuma linha de PHP nasce
antes deste arquivo; nenhum número entra aqui sem fonte e data.

Três ferramentas, uma por eixo do corpus (`dados/corpus-buscas.md`), e elas **não se
fundem**: casar carga é aritmética contra catálogo, dimensionar caixa é acústica,
dimensionar cabo é elétrica. A ordem é obrigatória e está no `PROMPT.md`.

| Código | Ferramenta | Eixo | Sub_id 2 | Etiqueta ML |
|---|---|---|---|---|
| **F1** | Casa o módulo com o seu alto-falante | A — casamento de carga | `F1` | `ohmetriaf1` |
| **F2** | Litragem da caixa para o seu subwoofer | B — dimensionamento de caixa | `F2` | `ohmetriaf2` |
| **F3** | Bitola do cabo de alimentação | C — instalação elétrica | `F3` | `ohmetriaf3` |

`Sub_id 1` é sempre `ohmetria` (seção 7 do `ARQUIPELAGO.md`). As três etiquetas do
Mercado Livre **ainda não existem** na conta RMNATAL.

---

## 0. Como esta coleta foi feita, e o que ela limita

O egresso HTTP direto desta nuvem está **fechado para todo domínio de terceiro**:
`sac.taramps.com.br` devolveu `EGRESS_BLOCKED` pelo WebFetch nesta execução (19h30Z de
14/09/2026), como `www.lojadesomautomotivo.com.br` já havia devolvido no bloco 1.
**Nenhum documento de fabricante foi lido.** A coleta abaixo saiu de **busca web**,
restrita ao domínio da fonte quando a atribuição precisava ser exata, e o canal está
declarado constante a constante em `dados/constantes.json`.

Consequência escrita, não escondida: pela regra do elo mais fraco (seção 10), autoria
forte com **leitura por busca continua sendo leitura por busca**. Por isso toda
constante de fabricante deste bloco nasce com status `pendente`, mesmo quando a busca
devolveu a URL do documento. `dados/constantes.json` traz, no fim,
**`pendencias_de_leitura`**: a lista fechada dos quatro documentos que promovem essas
constantes, em ordem de quanto cada um desbloqueia.

**Nenhuma consulta desta execução carregou o valor que queria confirmar** (seção 8): as
perguntas foram da forma *"qual é a conta que o fabricante publica"*, nunca *"o divisor
é 20?"*. Isso importa para o achado principal deste bloco, abaixo — o número apareceu
sem ter sido plantado, e apareceu duas vezes, em consultas independentes.

---

## 0.1 O achado que muda as três ferramentas: o desacordo da SERP é UMA confusão de unidade, não três opiniões

O bloco 1 mediu que o topo da busca publica **três regras incompatíveis** para "quantos
RMS de módulo para um falante de N RMS" — 100%, o dobro, e 0,75–1,25× — com amplitude
de **2,7 vezes**, e escreveu que **nenhuma das três diz de onde a regra sai**. Esta
execução achou de onde sai, e são **duas** declarações do mesmo fabricante:

1. **O critério de casamento**, que a Taramps publica em artigo dedicado, um por linha
   de produto (DS, HD, TS, Amplayer): *a potência RMS do alto-falante tem de ser igual
   ou superior à do amplificador*. O teto é **100%**.
2. **A razão entre potência musical e RMS**, que a mesma base de conhecimento publica em
   artigo próprio: musical é **cerca de 2×** o RMS, porque considera pico e não regime.

Os dois juntos explicam o desacordo inteiro: **a regra "use o DOBRO" tem o mesmo 2 da
razão musical/RMS** — e esse 2 é a relação entre duas maneiras de medir **o mesmo
equipamento**, não uma licença para dobrar a potência do amplificador. O mercado está
trocando uma unidade pela outra e publicando o resultado como conselho.

**Isto é a tese da ilha em uma frase, e nenhuma das páginas medidas a diz.** Vale igual
no eixo C: dos três divisores de corrente, o `÷ 20` que o corpus atribuiu a um blog é,
aparentemente, **a conta do próprio fabricante** — declarada pela Taramps como
aproximação dos técnicos dela para o *consumo musical* —, e os outros dois (`÷ 12` e
`÷ 12,6`) são `W ÷ V`, que ignora o rendimento do módulo. O desacordo de 67% do achado
C1 não é "três contas"; é **uma conta com premissa e duas sem**.

**O que ainda não está provado, e por isso nada disso vai à tela hoje:** nenhum dos dois
documentos foi aberto, e os exemplos numéricos que vieram junto com o divisor **não
fecham entre si** — uma resposta deu *"3.000 W ÷ 20 = 135 A"*, e 3.000 ÷ 20 é 150. A
regra veio idêntica nas duas consultas e os exemplos não, o que é sinal de paráfrase por
cima do documento. **Regra forte, exemplos fracos** → `pendente`, e a leitura é a
prioridade 1 da lista de pendências.

---

## 1. FERRAMENTA F1 — Casa o módulo com o seu alto-falante

É a **home**, sem introdução (`VOZ.md`, molde FERRAMENTA). A primeira da ordem porque é
a única das três cuja metade central **não depende de fonte nenhuma**.

### 1.1 A pergunta e a classificação da SERP (exigência da seção 14.9)

**Consulta principal:** `qual modulo para 2 subwoofer de 2 ohms` (a consulta-âncora da
ilha, medida no dossiê em 14/09/2026). Irmãs medidas no bloco 1:
`como ligar 2 subwoofer 2+2 ohms em 1 ohm associação paralelo`,
`qual módulo estabiliza em 1 ohm`, e a família
`qual módulo usar para {woofer, subwoofer} de N rms`.

| Quem ocupa o top 10 | O que entrega |
|---|---|
| `corsaclube.com.br`, `autoforum.com.br`, `forum.monzeiros.com` | **três fóruns**, um deles em #1 — resposta de pessoa para pessoa, sem tabela |
| `lojadesomautomotivo.com.br` (três URLs na mesma página de resultados) | guia de loja em prosa, com a regra dos 100% e sem dizer de onde ela sai |
| `somautomotivobr.com.br`, `blog.mundomax.com.br` | guia em prosa, com a regra do dobro e com a faixa de 0,75–1,25×, respectivamente |
| `poweraltofalantes.webnode.page` | prosa de como ligar |

**Veredito: é ALVO, e com folga.** Nenhuma calcula — todas explicam. Não há fazenda de
conteúdo estacionada nesta consulta (as quatro fazendas nomeadas no dossiê aparecem na
**comercial**, `melhor módulo amplificador 2026`, que a ilha não disputa na largada).

**E o achado que estreita o recorte, do bloco 1:** a calculadora de impedância **já
existe** no Brasil — pelo menos quatro (`nexxobox`, `amantesdeamplificadores`, `sombox`
com duas URLs). **Nenhuma delas apareceu no top 10 da consulta-âncora.** Elas fazem a
**aritmética** e nenhuma faz a **decisão**. Portanto a vaga da F1 não é "existir uma
calculadora": é **ocupar a pergunta que a pessoa digita, com veredito e com o módulo que
fecha**.

**Por que a F1 chega às 10 primeiras:** ela serve, em HTML, (a) o veredito "fecha" ou
"não fecha" na primeira linha, (b) **todas** as impedâncias que aquela montagem alcança,
com a ligação de cada uma, e (c) a lista de módulos do banco que estabilizam naquela
impedância, cada um com o RMS que o fabricante declara **naquela** impedância e o
endereço da declaração. As três coisas faltam em todos os nove resultados acima.

### 1.2 Entradas

| Campo | Domínio aceito | Por quê |
|---|---|---|
| quantidade de alto-falantes | 1, 2, 3, 4 | acima de 4 a instalação vira projeto e não cabe em resposta de duas linhas. **Teto declarado na tela**, nunca omitido |
| impedância da bobina | `1`, `2`, `4`, `1+1`, `2+2`, `4+4` Ω | é o que os fabricantes do nicho publicam. `N+N` é bobina dupla |
| RMS do alto-falante | número, W | um valor; a F1 supõe falantes **iguais** e diz isso |
| impedância que o módulo estabiliza | `0,5`, `1`, `2`, `4`, `8` Ω — **opcional** | quando vem preenchida, a F1 responde "fecha" ou "não fecha". Vazia, ela lista tudo que a montagem alcança |

### 1.3 Saídas, em ordem de tela

1. **O veredito, primeira linha, na língua do nicho.** "Fecha: os dois subs em paralelo
   dão 0,5 Ω." Ou: **"Não fecha. Esse par não alcança 1 Ω de jeito nenhum — o mais perto
   que fecha é 2 Ω."**
2. **Todas as impedâncias alcançáveis**, com a ligação escrita de cada uma, e marcando
   as que **o banco atende** e as que **o banco não atende** ("0,125 Ω é alcançável e
   **nenhum módulo do nosso banco** estabiliza aí").
   **CORRIGIDO NO BLOCO 3, e a diferença é a única que importa nesta linha:** até
   14/09/2026 esta frase era *"0,125 Ω é alcançável e não existe módulo para isso"*, que
   é uma afirmação sobre o **mercado** — e a única coisa que a sustentava era uma lista
   de cinco impedâncias digitada à mão dentro de `ferramentas/impedancias.py`, com o
   comentário dizendo, com todas as letras, que ela era "o conjunto de valores que o
   mercado de módulos oferece". Nenhum registro de banco podia contradizê-la, porque não
   havia banco. É a família da seção 8 do contrato: número de tela nasce **contado**,
   nunca digitado, e régua escrita para um mundo que nunca aconteceu nasce sem poder
   falhar. A lista mudou de casa (`esquema-banco.json` → `vocabularios.impedancia_de_modulo`,
   pela 26.2), o campo do JSON mudou de nome
   (`alcancavel_e_fora_do_vocabulario_de_modulo`) e `ferramentas/validar-banco.py` passou
   a cobrar os dois sentidos entre a lista e o banco. **Enquanto `vocabulario_sem_lastro`
   não for vazio — hoje ele é 5 de 5, porque o banco está vazio — a F1 não pode publicar
   nenhuma frase sobre o que existe ou não existe no mercado.**
3. **Os módulos do banco** que estabilizam na impedância escolhida, com o RMS declarado
   naquela impedância.
4. **Bloco de compra**, com link de afiliado, **antes** da prova de procedência (seção 7
   e `DESIGN.md`).
5. **"Como sabemos"**: a fonte de cada módulo, com `data_leitura`, e o desacordo da SERP.

### 1.4 A metade que é aritmética, e ela publica hoje

`ferramentas/impedancias.py` enumera o domínio de saída inteiro e grava
`dados/impedancias-alcancaveis.json` (**24 casos**, contados e não digitados). O modelo:
K bobinas iguais de Z ohms, partidas em **g grupos iguais** de K/g em série, os grupos em
paralelo → **Z × K / g², com g dividindo K**. `g=1` é tudo em série, `g=K` é tudo em
paralelo, os divisores do meio são as série-paralelo.

**Por que isto importa mais do que parece:** o conjunto alcançável é **discreto**, e é
por isso que existe pedido que não fecha. Dois subs 2+2 Ω alcançam **0,5, 2 e 8 Ω** — e
**1 Ω não está no conjunto**. A fórmula que a SERP publica (*impedância ÷ número de
alto-falantes*) é o caso `g=K` visto de longe: ela produz 0,5, some com os outros dois e
**nunca avisa** que 1 Ω não existe ali.

**E a enumeração devolveu um veredito que este bloco não foi procurar, e que nenhuma
página medida publica: TRÊS alto-falantes iguais não fecham em impedância de módulo
nenhuma.** Nas **seis** montagens de três — uma por tipo de bobina — não existe uma única
ligação simétrica que caia em 0,5, 1, 2, 4 ou 8 Ω. Para três subs 2+2 Ω, por exemplo, as
seis bobinas de 2 Ω dão **12 · 3 · 1,333 · 0,333 Ω**, e nenhum desses quatro é impedância
de módulo. Quem monta três falantes iguais **precisa** de ligação assimétrica ou de dois
canais — e a F1 é o único lugar que vai dizer isso antes da compra. (Não é "ímpar nunca
fecha": **um** falante de 2 Ω fecha em módulo de 2 Ω. A afirmação é sobre três, e a régua
guarda o contraexemplo para que ela não se generalize sozinha.)

**A regra de decisão quando não fecha, e ela é da ilha, não de fabricante nenhum:** a
resposta é o **menor valor alcançável que seja ≥ o pedido**, nunca o de menor distância
em ohms. A assimetria de custo decide (seção 10): descer abaixo da impedância mínima que
o módulo estabiliza é o que **queima** o módulo; subir perde potência e roda frio. Para
o par 2+2 pedindo 1 Ω, **0,5 Ω está mais perto em ohms e é a resposta que queima**.

Isto não é retórica: a primeira versão do gerador respondeu 0,5 Ω, e **a régua própria
reprovou o gerador**. O portão ficou escrito com a alternativa errada afirmada de
propósito, para que trocar o critério por distância absoluta volte a reprovar.

**Recusa declarada:** ligação **assimétrica** (três bobinas em paralelo mais uma, por
exemplo) fecha valores intermediários e faz bobinas idênticas receberem potência
diferente. A F1 **não recomenda** e **diz na tela que não recomenda** — em vez de omitir.

### 1.5 A metade que espera, e o que ela espera

| O que | Espera | Enquanto isso |
|---|---|---|
| filtrar módulos por impedância estável | **banco de MÓDULOS (bloco 3)**: `impedancias_estaveis[]`, `rms_por_impedancia{}` | a F1 não nasce antes do bloco 3. É o achado A2-c: não existe em pt-BR lista de módulo filtrável por impedância estável, e é a metade que nenhum concorrente tem |
| afirmar teto de RMS ("esse módulo é demais para o seu falante") | `criterio-rms-modulo-nao-passa-do-falante`, hoje **`pendente`** | a F1 **imprime os dois números** (RMS do módulo naquela impedância, RMS do falante) e a relação entre eles, **sem asserir limiar**. A linha de veredito sobre potência só aparece quando a constante for promovida |

**É isto que faz a F1 caber no bloco 4 sem constante publicada:** a metade central é
aritmética, e o que depende de fonte fica visível como número do fabricante lado a lado,
não como conselho da ilha.

### 1.6 Portão da seção 7, desde o primeiro dia

**Todo módulo do banco é nomeado uma vez em cada resposta** — ou na frase que o
recomenda, ou numa linha que diz por que ficou fora (*"o MD 1200.1 de 4 Ω não estabiliza
em 1 Ω"*). Nenhum módulo entra no bloco de compra sem que a frase o nomeie. A soma dos
nomeados fecha o banco, e isso se mede **varrendo a entrada inteira** (as 24 montagens ×
as impedâncias de módulo) contra o tamanho **contado** do banco — nunca contra número
digitado. Vale igual para a **tabela pré-renderizada**, que é a metade que um modelo de
linguagem lê sem preencher formulário: foi ali que a F2 do Clube do Mosaico falhou em
três de nove linhas.

### 1.7 O que a F1 se RECUSA a responder

- **Qual é o "melhor" módulo.** Ela responde qual **fecha**. Ranking sem medição é o que
  as quatro fazendas fazem na consulta comercial.
- **Ligação assimétrica** (1.4).
- **Mais de 4 alto-falantes** e **falantes diferentes entre si** — diz que não responde e
  por quê, em vez de supor igualdade em silêncio.
- **Quanto de potência o falante "aguenta de verdade"** acima do que o fabricante
  declara. Essa é a pergunta que os fóruns respondem e ela não tem fonte.

---

## 2. FERRAMENTA F2 — Litragem da caixa para o seu subwoofer

### 2.1 A pergunta e a classificação da SERP

**Consulta principal:** `qual litragem de caixa selada para subwoofer 12 polegadas`
(medida no dossiê). Irmãs medidas no bloco 1:
`quantos litros caixa dutada subwoofer 12 polegadas sintonia duto`,
`volume bruto ou volume livre litragem caixa som automotivo`.

| Quem ocupa o top 10 | O que entrega |
|---|---|
| **`tudosobresom.blogspot.com` (2009)** e **`extremepreparacoes.blogspot.com` (2010)** | posts com 16 e 17 anos, ainda posicionados |
| `nandinsound`, `wellbagagitos` | **anúncio de caixa pronta**, não resposta |
| `carrostech.com.br`, `somautomotivobr.com.br` | prosa "selada, dutada e litros" |
| `autoforum.com.br` | **fórum** com projeto de caixa |

**Veredito: é ALVO, e o vácuo é mais fundo do que o dossiê mediu** — somando as três
consultas do eixo, **cinco blogspots** de 2009 e 2012 aparecem em top 10 de consultas
diferentes. Não é uma página velha sobrevivendo: é a camada de explicação do eixo
**parada há mais de uma década**.

**O que estreita o recorte:** `speakerboxlite`, `omnicalculator.com/pt` e
`audioclassico.com` calculam caixa e duto — e **nenhuma apareceu na consulta em
linguagem de pessoa**. Elas ocupam a consulta de quem **já sabe** que precisa de Vas e
Qts. **Por que a F2 chega às 10 primeiras:** ela aceita **o modelo do sub** como entrada
e busca os parâmetros no banco, o que nenhuma delas faz — e é aí que o banco de
Thiele-Small do bloco 3 vira a barreira que a fórmula sozinha não é.

### 2.2 Entradas

- **Modelo do subwoofer** (busca no banco) **ou** `Vas` (L), `Qts`, `Fs` (Hz) à mão.
- **Tipo de caixa:** selada ou dutada.
- **Quantidade de subs** na mesma caixa (o volume multiplica; câmaras separadas).

### 2.3 Saídas

1. **O volume, em faixa e com o tipo dito**: *"Sub de 12 com esses parâmetros pede caixa
   selada de 32 a 36 litros"* — e a faixa é a varredura do Qtc, não uma margem inventada.
2. **Qual volume é esse**: bruto ou líquido. **Na primeira linha, não no rodapé.**
3. **Na dutada:** comprimento e diâmetro do duto para a frequência de sintonia.
4. **A comparação com o que o fabricante recomenda** para aquele modelo, quando existir
   (Bomber e Pioneer publicam), **só quando as duas estiverem na mesma unidade**.
5. Bloco de compra → prova → "como sabemos".

### 2.4 A fórmula, e o portão que a promove

```
Vb = Vas / ((Qtc / Qts)^2 - 1)
```

Alinhamento selado clássico de Thiele-Small; a derivação está em `constantes.json`. A
fórmula **só tem solução com Qtc > Qts**: falante de Qts alto **não cabe** em caixa
selada pequena, e a F2 tem de dizer isso em vez de devolver número negativo — é um caso
que o esquema permite e que a régua trata **hoje**, não no dia em que aparecer (seção 8).

**Status: `aguarda_validacao`.** A trava 3 do `PROMPT.md` manda a fórmula bater com a
litragem que o fabricante recomenda, e a validação **ainda não rodou** porque o banco não
existe. Conjunto de validação já identificado: Bomber (Bicho Papão 12", projetos de 37 a
66 L) e Pioneer (TS-W3090BR, selada 35 L). **Até bater, a F2 não publica número.**

### 2.5 As duas travas que podem quebrar a F2, e como cada uma é contida

**Trava de unidade (achado B2), e é a perigosa:** "litros" são três grandezas com nomes
que não batem. A `zettaaudio` publica *bruto 49 L, livre 42 L*; a **Hinor**, fabricante
da lista de carga, publica que *40 L brutos, com duto e sub dentro, dão 32 a 35 L*. A
razão fica entre **0,80 e 0,88**. Se a fórmula devolver líquido e a recomendação for
bruta, a validação acusa **12 a 20% de erro que é erro de unidade, não de fórmula** — e
os dois números são plausíveis, nenhum parece absurdo.

Contenção, em três partes: (a) `litragem_tipo` (`bruto | liquido | nao_declarado`) nasce
no banco ao lado de `litragem_l`; (b) a F2 **declara na tela** qual dos dois devolve;
(c) **enquanto `razao-volume-liquido-sobre-bruto` estiver `pendente`, a F2 NÃO
converte** — ela compara só o que estiver na mesma unidade e cala sobre o resto.

**Trava do Qtc:** é o Qtc que decide o tamanho da caixa, e a faixa 0,7–1,1 encontrada
**não tem fonte de fabricante nem leitura direta** → `pendente`. Publicar faixa de
litragem sem declarar de onde saiu o Qtc seria entregar número exato com cara de
especificação: o defeito que o `VOZ.md` nomeia como o pior possível nesta ilha.

**Faixa de validação de entrada (trava 2 do `PROMPT.md`), essa sim publicável:**
`Fs 20–90 Hz`, `Vas 10–250 L`, `Qts 0,2–0,9`. Valor fora da faixa é **recusado**, nunca
corrigido — o `PROMPT.md` registra `Fs 4 Hz` num manual Hinor e `Vas 672,3 cm³` num JBL.
Recusar um valor bom custa um modelo a menos; aceitar um errado faz a ferramenta cuspir
litragem absurda com cara de número exato.

### 2.6 O que a F2 se RECUSA a responder

- **Caixa para modelo sem Thiele-Small lido.** Ela diz que não tem os parâmetros daquele
  modelo e oferece a litragem **que o fabricante recomendou**, se houver, marcada como
  recomendação do fabricante e não como cálculo.
- **Qual caixa "bate mais forte".** Gíria de fórum não é marca da casa (`VOZ.md`).
- **Sintonia "ideal"** sem o uso declarado: a F2 pede a sintonia ou usa uma faixa com o
  critério escrito, nunca um número mágico.

---

## 3. FERRAMENTA F3 — Bitola do cabo de alimentação

**A última da ordem, de propósito.** É a única que entra contra um concorrente que **já
tem a ferramenta pronta** (`infinitysom.com.br`), e só entra se for melhor.

### 3.1 A pergunta e a classificação da SERP

**Consulta principal:** `que bitola de cabo para modulo 1000w som automotivo`.

| Quem ocupa o top 10 | O que entrega |
|---|---|
| **`sac.taramps.com.br`** — tabela técnica de bitola por amplificador | **é a nossa FONTE, não concorrente** |
| **`infinitysom.com.br`** — Calculadora de Bitola de Cabos | **o concorrente com ferramenta**; loja de nicho pequena |
| `corsaclube`, `autoforum` | **fóruns** |
| `somautomotivobr` (três URLs), `mdmax`, `discabos` | guias em prosa — e o artigo da `discabos` que ranqueia aqui é, lido de perto, **residencial** |

**Veredito: é alvo CONDICIONAL.** Existe ferramenta, existe fonte oficial e existe
fazenda (`guiaomelhor` apareceu na consulta com distância). Entrar exige ser melhor.

**E a vaga está medida com precisão (achado C2):** a consulta escrita com os três
parâmetros que decidem — 1000 W RMS, **4 metros**, queda de tensão — devolveu **cinco
fóruns** (um deles de energia solar), um guia de loja e uma fazenda. As páginas dizem que
*"o comprimento influencia a queda"* e **nenhuma fecha a conta para um comprimento
dado**. **A calculadora da InfinitySom não apareceu nessa consulta.** Logo a vaga não é
"calcular bitola": é **calcular bitola para a distância, de ida e volta, com o fusível
junto** — exatamente onde o `PROMPT.md` diz que a do concorrente para.

### 3.2 Entradas

RMS total do sistema (soma dos módulos) · tensão do sistema (12 V ou 14,4 V) ·
**distância bateria → módulo**, em metros, **um trecho só** (a F3 dobra; ver 3.4).

### 3.3 Saídas

1. **mm² mínimo**, com a premissa da corrente **dita na mesma frase**.
2. **Fusível**, em ampere, junto — nunca em outra página.
3. **Queda de tensão** para a bitola escolhida, no comprimento de ida e volta.
4. A **premissa** declarada na tela: qual divisor, de quem é, e que o rendimento do
   módulo é o que nenhuma das páginas medidas declara.
5. Bloco de compra (cabo, fusível, porta-fusível) → prova → "como sabemos".

### 3.4 As duas coisas que a F3 publica hoje sem depender de leitura

**A distância é de ida e volta.** A corrente vai pelo positivo e volta pelo retorno; a
queda é o produto da corrente pela resistência do caminho **inteiro**. É derivação, não
afirmação sobre produto — e é metade da vaga do achado C2.

**A direção do erro, quando as fontes discordam da corrente — e esta é a decisão mais
interessante das três ferramentas.** As fontes dão de 100 A a 167 A para o mesmo módulo
de 2000 W RMS. A ilha **não escolhe um divisor só**:

> **o cabo se dimensiona pela corrente MAIOR, o fusível pela MENOR, e o fusível nunca
> passa do que o cabo aguenta.**

Por quê: quem protege o cabo é o fusível, então **fusível grande demais deixa o cabo
esquentar antes de abrir** — e cabo esquentando dentro do carro queima mais que o módulo.
Fusível pequeno demais abre em uso normal: chateia e não machuca ninguém. Cabo grosso
demais custa dinheiro; cabo fino demais derruba tensão e esquenta. **Os dois erros
baratos apontam para lados opostos da mesma divergência**, então usar os dois extremos,
cada um do lado em que ele é conservador, é mais seguro que qualquer média — e média é a
única saída proibida (seção 10). **Nenhuma das páginas medidas faz essa separação:** todas
escolhem um divisor e propagam para as duas saídas.

E o desacordo que isso resolve na tela, com os dois nomes e os dois números: **fusível de
110 A a 250 A** para o mesmo módulo, **2,3 vezes** — e o número do **fabricante é o mais
BAIXO** dos dois, o contrário do que a intuição diz.

### 3.5 O que a F3 espera, e por que ela é a terceira

| O que | Constante | Por que trava |
|---|---|---|
| a corrente | `divisor-consumo-musical-taramps` — **`pendente`** | é a entrada de tudo. A regra veio em duas consultas independentes; os exemplos não fecham (3.000 ÷ 20 = 150, e a resposta disse 135) |
| o fusível | `fusivel-acima-do-consumo-fabricante` — **`pendente`** | documento citado, não aberto |
| a bitola | `tabela-bitola-taramps` — **`pendente`** | a busca devolveu bitolas soltas (2,5 · 4 · 16 mm²) **sem dizer a que modelo e a que distância** cada uma pertence. Bitola sem modelo e sem distância não é dado, e transcrever assim seria inventar a tabela |
| o veredito da queda | `queda-de-tensao-maxima-aceitavel` — **`pendente`, sem fonte encontrada** | nenhuma página medida declara o limite; dizem que o comprimento influencia e param. **Dar veredito sem critério publicado é exatamente o que a ilha acusa nos concorrentes** |

**A F3 não nasce antes da prioridade 1 e da 3 da lista de pendências de leitura.** Isso
não é bloqueio da ilha: é a ordem obrigatória do `PROMPT.md` coincidindo com o que a
medição mostrou.

### 3.6 O que a F3 se RECUSA a responder

- **Quantos farad de capacitor.** O achado C3 mediu desacordo de **3,3×** — a regra de
  bolso diz 1 F por 1000 W e a ficha do próprio fabricante se chama *"Mega Capacitor 0,3
  Farad 1000w rms"*. Capacitor é **entidade do banco** e **matéria de artigo-âncora**, não
  ferramenta: a conta certa não é por potência, é por quanto tempo o pico dura, e essa
  conta precisa de um dado que ninguém publica.
- **Bitola de cabo de alto-falante.** Outra pergunta, outra consulta, e é por onde o
  artigo residencial da `discabos` vaza para cá.
- **Dimensionamento de bateria e alternador.** A Taramps publica artigos próprios sobre
  isso; é cluster de guia, não saída de ferramenta.

---

## 4. O que vale para as três — e se mede, não se promete

**Visibilidade em IA (seção 5), em toda ferramenta desde o primeiro dia:**
tabela de exemplos **pré-renderizada no HTML**, cobrindo a faixa real de uso e **as
bordas** (a F1 tem as 24 montagens de `impedancias-alcancaveis.json` — e o caso que não
fecha entra na tabela, porque é a resposta que só ela dá) · **resposta antes da
explicação**, em frase autossuficiente que sobrevive a ser citada fora de contexto ·
**JSON-LD** `WebApplication` na ferramenta, `Product` na ficha, `Dataset` no banco,
`FAQPage` onde couber · **procedência na própria frase** · `robots.txt` liberado para
GPTBot, ClaudeBot, PerplexityBot e Google-Extended · página **Sobre** com método.

**Link de compra (seção 25.2):** **todo item ganha `afiliado.url_busca_produto` ANTES de
qualquer outra coisa** *(dizia `url_busca_bruta`, nome que não existe no contrato; a 25.4-b
batiza a URL crua da busca de `url_busca_produto` desde 13/09/2026 — corrigido pelo Pente
Fino em 21/09/2026, antes de o banco desta ilha ter um registro sequer)* — o piso é a busca e o piso não espera ninguém. `url_produto`
(URL crua) é obrigatória em todo item que tenha ficha, senão o teste de vida é impossível
(25.4-b). Ficha viva vira botão e a busca desce para a linha discreta; ficha morta ou
inexistente, **a busca sobe e vira o botão**. A frase **"link de loja em breve" é
proibida**. Amazon está fora de tudo.

**Quando o produto existe nos dois programas, o link é o da Shopee.**

**Bloco de compra ANTES da prova de procedência**, com o "fonte" discreto em
`rel="nofollow noopener"`, nunca botão (cicatriz da Robometria). O âmbar da marca aparece
**uma vez por tela** — no veredito ou no botão, nunca nos dois (`DESIGN.md`). Onde for
texto, o âmbar é `#8A5200`: `#B86E00` dá 3,99:1 e reprova.

**Voz (seção 15 e `VOZ.md`):** veredito na primeira linha, na língua da pessoa —
"fecha", "não fecha", "estabiliza", "vai clipar". **Nunca no título nem no primeiro
parágrafo:** "associação de impedâncias", "especificação verificável", "conforme a ficha
técnica do fabricante", "consulta paramétrica", "procedência". A ficha e a
`data_leitura` ficam na tabela e no "como sabemos".

**Portão de medição que cada ferramenta tem de trazer no bloco dela**, e ele é a lição da
seção 8: **quem confere escreve a própria régua**, nunca chama a de quem produziu o dado
· a grade **pisa na borda** · afirmação sobre o que a página diz se mede **no CORPO**,
nunca no HTML completo · **varrer a entrada inteira**, não o caso-âncora — para a F1 são
as 24 montagens × as impedâncias de módulo, **um processo por estado** · e toda régua
prova que **pode falhar**, por mutação que **produz o mundo** que o banco ainda não tem.
`ferramentas/impedancias.py --conferir` é o primeiro desses portões e já está de pé: **73
afirmações, 0 falha, seis mutações deliberadas e seis reprovadas** — e ele reprovou o
próprio gerador na primeira passada, no critério de "mais perto que fecha".

**Número de tela nasce contado, nunca digitado.** Vale para quantos módulos o banco tem,
quantas montagens a tabela cobre e quantos itens esperam link — e a ilha **reporta em todo
bloco quantos itens esperam link** (seção 7, cicatriz da Robometria).

---

## 5. As três obrigações que o bloco 1 deixou para este bloco — e onde cada uma está

| Obrigação (fim de `dados/corpus-buscas.md`) | Onde foi cumprida |
|---|---|
| (a) a F1 declara o critério de casamento de RMS **com fonte** | §0.1 e §1.5: a fonte **foi achada** (quatro artigos do SAC da Taramps, um por linha de produto) e entrou como `pendente` por não ter sido lida. Até a leitura, a F1 imprime os dois números e **não asserta limiar** |
| (b) a F1 sabe dizer **"não fecha"** e qual é a impedância mais próxima que fecha | §1.4, e virou **código com régua própria** em vez de frase: `dados/impedancias-alcancaveis.json`, 24 casos. O critério de "mais perto" foi **corrigido** pela régua — é o menor ≥ o pedido, nunca a menor distância |
| (c) a F3 declara **o rendimento suposto e a distância de ida e volta** na tela | §3.3 e §3.4: a distância de ida e volta é derivação e publica hoje; a premissa da corrente tem agora **autoria de fabricante** e está `pendente` até a leitura. O rendimento **continua sem ninguém que o declare**, e isso é o que a F3 diz na tela |

**E uma quarta, que este bloco acrescenta:** o bloco 3 herda de `constantes.json` a
`faixa-de-validacao-thiele-small` como portão de entrada do banco, `litragem_tipo` ao
lado de `litragem_l`, e **um achado de canal**: a busca devolveu, no SAC da Taramps,
páginas de **descrições técnicas em HTML por modelo de módulo** (TS 400X4, TL1500,
MD1200.1, TS 1200X4 foram vistas). Se o egresso abrir, a carga do lado **MÓDULO** pode
não precisar de PDF nenhum — o que muda a trava 1 do bloco 3 de "extração de PDF" para
"leitura de página" **na metade que sustenta a F1**. Não conferido: a página não foi
aberta.

---

## 6. O QUE O BLOCO 3 ENTREGOU, E ONDE A F1 VAI BUSCAR CADA COISA (14/09/2026)

Esta seção foi acrescentada pelo **bloco 3**, que é o modelo do banco. Ela existe para
que quem escrever a F1 no bloco 4 não precise reler os dois arquivos inteiros.

| O que a F1 precisa | Onde está |
|---|---|
| domínio de saída enumerado (24 montagens) | `dados/impedancias-alcancaveis.json`, gerado por `ferramentas/impedancias.py` |
| o contrato do banco, campo a campo | `dados/esquema-banco.json` |
| os módulos que estabilizam em cada impedância | `dados/modulos.json` — **hoje com 0 registros** |
| os alto-falantes | `dados/alto-falantes.json` — **hoje com 0 registros** |
| o portão que decide se um registro pode entrar | `ferramentas/validar-banco.py` |
| a prova de que esse portão pode falhar | `ferramentas/mutacoes-banco.py` |

**As três coisas do esquema que mudam o que a F1 escreve na tela, e não só o que ela lê:**

1. **Módulo não tem "um RMS": tem `rms_por_impedancia`.** Não existe campo `rms` escalar
   de módulo neste esquema, de propósito. A F1 imprime o RMS **naquela** impedância, que
   é a metade que nenhum dos nove resultados medidos na SERP entrega.
2. **`potencia.unidade_declarada` vem sempre com `unidade_declarada_por`** (seção 26 do
   contrato). É o que separa *"a Taramps declara 3.000 W RMS"* de *"a página do produto
   estampa 3.000 W e nós lemos como RMS"*. A primeira frase é permitida quando a origem
   for `no_titulo_ou_na_prosa_do_fabricante`; a segunda é a única honesta quando a origem
   for `na_tabela_de_potencia_por_impedancia`.
3. **A F1 fala do BANCO, nunca do mercado** (ver a correção na seção 1.3). O validador
   publica `vocabulario_sem_lastro` a cada passada, e enquanto ele não for vazio, toda
   frase de inexistência está proibida.

**E a trava de potência que a F1 herda pronta, sem ter de pensar nela:** o validador
recusa `rms_por_impedancia` que **cresça** quando a impedância sobe. Módulo entrega mais
watt quando a impedância cai — é física, não convenção — então a tabela invertida é
sinal de transcrição errada ou de dois números de unidades diferentes na mesma tabela,
que é o achado 0.1 deste arquivo aparecendo dentro de um único registro.

---

## 7. O QUE O BLOCO 4 ENTREGOU — a F1 existe, e ainda não é uma página (15/09/2026)

Esta seção foi acrescentada pelo **bloco 4**. Ela substitui a seção 6 como primeiro
lugar a abrir: quem for escrever o snippet PHP da F1 (bloco 3b em diante) encontra
aqui a regra pronta e não precisa reler a seção 1.

| O que a F1 é hoje | Onde |
|---|---|
| o cérebro: entrada → resposta inteira, já em frase acentuada | `ferramentas/f1-referencia.py` |
| as 144 respostas gravadas, com a tabela pré-renderizada | `dados/f1-respostas.json` (`publicar: false`) |
| a bancada, régua própria, varrendo a entrada inteira | `ferramentas/teste-f1.py` |
| a prova de que a bancada reprova | `ferramentas/mutacoes-f1.py` |

**A F1 NÃO tem snippet PHP, e isso é decisão e não pendência esquecida.** A ilha não
tem WordPress: o passo 3b é trabalho de navegador e está com o Raphael. Sem casca, um
snippet só poderia ser medido por um render de bancada que serve **menos** do que o
site serve — a cicatriz da seção 8 do `ARQUIPELAGO.md`, paga três vezes pela
Robometria. Então a regra nasceu onde ela pode ser conferida hoje, e o PHP, quando
nascer, é **tradutor** desta referência, frase a frase, do jeito que a Robometria faz
entre `cobertura-r1.py` e `robometria-r1.php`.

### 7.1 O domínio de resposta é 144, e ele é contado

24 montagens × (as 5 impedâncias de módulo do vocabulário + o pedido vazio). Os
vereditos se distribuem assim, e os cinco números saem da varredura, nunca digitados:
**FECHA 37 · NÃO FECHA, SOBE 36 · NÃO FECHA, SÓ ABAIXO 17 · NÃO FECHA EM NENHUMA 30 ·
SEM PEDIDO 24.**

### 7.2 A distinção que a seção 1 não tinha, e que é o coração da ferramenta

A seção 1.3 previa dois vereditos — "fecha" e "não fecha" — e o gerador do bloco 2
devolvia, para todo pedido que não fechasse, um campo `mais_perto_que_fecha`. **Servir
esse campo sempre da mesma maneira seria publicar, em 17 dos 144 estados, a resposta
que queima o módulo.** Porque `abaixo_do_pedido: true` quer dizer que **nada** na
montagem alcança o mínimo que aquele módulo estabiliza, e o valor devolvido é o menos
ruim de um conjunto que é todo ruim. São coisas diferentes e a tela as separa:

- **NÃO FECHA, SOBE** (36 estados) — existe valor alcançável ≥ o pedido. A página o
  nomeia, diz com que ligação, e diz o que se perde: *"em 2 ohms o módulo entrega menos
  watt e roda frio, e esse é o lado seguro de errar"*.
- **NÃO FECHA, SÓ ABAIXO** (17 estados) — não existe. A página **não oferece valor**:
  *"Não ligue assim… abaixo do mínimo é o que queima. Troque o módulo ou mude a
  quantidade de alto-falantes."* E o bloco de compra fica sem piso, de propósito.
- **NÃO FECHA EM NENHUMA** (30 estados) — a montagem não cai em impedância de módulo
  alguma. São as seis montagens de três alto-falantes, e só elas.

É a regra da assimetria de custo da seção 10 do `ARQUIPELAGO.md` aplicada a um campo
que já existia: **quem separa as duas causas no código separa as duas no texto.**

### 7.3 O piso de compra quando o banco tem zero itens

A seção 25.2 do contrato dá o piso por **item**: marca + modelo viram a palavra-chave.
Com zero módulos não existe item, e a saída honesta não é inventar produto: é derivar a
busca da **própria resposta** — a impedância em que o módulo precisa estabilizar. É a
mesma manobra que a jornadafly registrou em 14/09/2026 ao derivar o piso da cidade.

O molde vem de `esquema-banco.json → piso_de_compra.moldes.shopee` e **nunca** é
digitado na ferramenta; a bancada refabrica cada URL do molde e compara. O link sai
**sem** `rel=sponsored`, porque busca crua não rende comissão e carimbá-la de
patrocinada seria mentir para o leitor sobre a única coisa que ele tem o direito de
saber sobre nós. **Itens sem saída de compra: 0. Piso não rastreável: todos** — as
etiquetas de afiliado desta ilha ainda não existem, e isso é dívida de comissão, não
defeito de página.

**E onde o bloco fica sem piso, ele fala.** São **53** estados, contra 91 com piso, e a
conta vale a pena ser escrita por extenso porque a primeira versão desta frase dizia
**47** — eu somei os 30 de NÃO FECHA EM NENHUMA com os 17 de SÓ ABAIXO e esqueci os
**6 estados SEM PEDIDO das montagens de três**, que também não têm o que oferecer. O
número saiu errado pelo motivo que a seção 8 do contrato mais repete: ele foi somado de
cabeça em vez de contado da varredura. Nos 53, o bloco não lista e **diz por quê** — que
é o que a seção 7 manda fazer em vez de deixar silêncio com cara de defeito. Mandar quem
não tem montagem válida para uma busca de módulo seria vender uma coisa no lugar de
outra, e isso é pior do que não ter link.

### 7.4 As três frases que a F1 está proibida de dizer, e quem as vigia

1. **Qualquer afirmação sobre o MERCADO**, enquanto `vocabulario_sem_lastro` não for
   vazio (hoje é 5 de 5). A única frase verdadeira é *"nenhum módulo do nosso banco"*.
2. **Qualquer teto de RMS**, enquanto `criterio-rms-modulo-nao-passa-do-falante`
   estiver `pendente`. A página imprime o RMS do falante e **diz o que ainda não pode
   dizer**, em vez de calar.
3. **As cinco expressões proibidas pelo `VOZ.md`** no veredito.

As três são varridas em todos os 144 estados, no **corpo** — o que o visitante lê —, e
cada uma tem mutação própria. A vigilância não é opcional porque ela já pegou coisa:
a régua de acento reprovou uma frase que citava `dados/modulos.json` **na tela**. O
defeito não era o acento; era a página falando com o visitante no vocabulário de quem
a escreveu.

### 7.5 O que a bancada mede, e as duas coisas que ela achou

**8.262 afirmações, 0 falha.** A régua é própria: a aritmética de associação está
reescrita dentro de `teste-f1.py` com `Fraction` e divisores, e pode discordar do
gerador. **41 mutações decidiram certo**, em cinco famílias — quatro **mundos que têm de
passar** (banco vazio, com 1, com 2 e com um módulo que estabiliza em todas as cinco
impedâncias), 28 **quebras que têm de reprovar**, cada uma declarando a frase que espera
ouvir, quatro **mortes** (chave que some da fonte tem de matar a referência, nunca virar
literal), quatro sobre a **prosa desta seção** (os números publicados aqui em cima são
conferidos contra a varredura, porque número em prosa envelhece calado) e o **autoteste
da própria bateria**, que troca a frase esperada de uma quebra pela de outra trava real
e exige que a bateria acuse.

As duas coisas que as mutações acharam, e as duas já estão fechadas:

- **A bancada não conferia a lista de módulos por ligação.** Com o banco vazio, a
  afirmação passava sobre lista vazia; com um módulo dentro, a linha da ligação podia
  continuar dizendo que não havia nenhum e a bancada aprovava. É exatamente o mundo que
  o esquema permite e o banco ainda não tem.
- **A referência não conferia o banco de casos contra o vocabulário do esquema.**
  Apagando `impedancia_de_bobina` do esquema, a F1 continuava respondendo a partir do
  banco de casos de ontem. Duas metades contando a mesma coisa sem nunca se falarem.
