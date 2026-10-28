---
titulo: Especificação das ferramentas — Rodametria
bloco: 2
gerado_em: 2026-10-28
publicar: false
---

# Especificação das ferramentas — Rodametria

Bloco 2 da fila. Define **o que cada ferramenta responde, com que entrada, com que
saída, com que fonte, e o que ela se recusa a responder**. Nenhuma linha de PHP nasce
antes deste arquivo; nenhum número entra aqui sem fonte e data.

As três ferramentas, na ordem obrigatória do `PROMPT.md`:

| Código | Pergunta na língua de quem pilota | Eixo do corpus | Etiqueta ML | Sub_id 2 (Shopee) |
|---|---|---|---|---|
| **F1** | Esse elétrico precisa de CNH? | A — CNH e placa | `rodametriaf1` | `F1` |
| **F2** | Quantos km ele faz de verdade? | B — autonomia | `rodametriaf2` | `F2` |
| **F3** | Aguenta o meu peso? | C — carga e tamanho | `rodametriaf3` | `F3` |

`Sub_id 1` é sempre `rodametria` (seção 7 do `ARQUIPELAGO.md`). As três etiquetas do
Mercado Livre **ainda não existem** — criar etiqueta funciona por script, gerar link
não (seção 7).

---

## 0. O CANAL DESTA COLETA, E O QUE ELE PROÍBE

Coleta de 28/10/2026 entre 13h20Z e 13h40Z, pela execução que reservou a ilha às
13h19Z. Dois canais foram tentados e **só um está aberto**:

| Canal | Resultado medido em 28/10/2026 |
|---|---|
| leitura direta da fonte (`curl`, WebFetch) | **fechado para toda fonte de fora da ilha.** `www.gov.br`, `www.in.gov.br`, `www.planalto.gov.br`, `www.contran.gov.br` e `www.lex.com.br` devolveram `000` com `CONNECT tunnel failed, response 403`; `dspace.ups.edu.ec` e `stdjet.scienceandtechnology.com.vn` falharam em `getaddrinfo ENOTFOUND`. Controle verde na mesma janela: `rodametria.com.br` em 200 |
| busca web | **aberto.** É o canal de tudo que está escrito abaixo |

**A consequência fica escrita e não escondida.** Pela regra do elo mais fraco (seção 10
do `ARQUIPELAGO.md`), **nenhuma constante deste bloco é leitura direta de fonte
primária**, mesmo quando o documento citado é oficial: o elo da leitura é fraco e é ele
que dá o nível. Cada constante declara o canal em `constantes.json`.

**A repetição que a 20.2 manda foi feita e não mudou o veredito**: duas passadas no
`gov.br`, as duas com 403 de política do egresso, com o domínio da ilha em 200 na mesma
janela. Erro nomeado pelo egresso é recusa, não queda — a 20.2 pede repetição contra
intermitência, e intermitência não é o que está medido aqui.

### 0.1 O QUE ESTE BLOCO **NÃO** PODE FECHAR, E POR QUÊ ISSO NÃO É DESCULPA

O `PROMPT.md` desta ilha é explícito: a constante central da F1 (os limites de potência,
velocidade e dimensão que separam bicicleta elétrica, autopropelido e ciclomotor) *"só
vira `publicavel` depois de lida no texto oficial do gov.br, com data"*. **Ela não foi
lida, e segue `pendente`.** O despacho ALTA de 28/10 em `dados/despachos.md` pede os dois
gestos que a destravam, e **nenhum deles é bloco**.

O que esta especificação faz com isso é a única coisa honesta disponível: **separa o que
depende da constante do que não depende**, e desenha a F1 de modo que a chegada do texto
oficial seja a edição de **um arquivo só**. Está na seção 1.3 — e é decisão de engenharia,
não consolo.

### 0.2 ERRATA AO BLOCO 1 — O ESTUDO DOS 41,29 Wh/km É DE **MOTOCICLETA**, NÃO DE BICICLETA

A seção 6, item 3, do `dados/corpus-buscas.md` entrega à F2 *"a régua do relevo com
número: 41,29 Wh/km em plano × 97,74 Wh/km a 12% de inclinação (`dspace.ups.edu.ec`)"*,
e logo acima calcula com ela *"com 1.200 Wh, os dois extremos dão ≈ 29 km e ≈ 12 km"* —
ou seja, aplica o número a uma bateria de patinete. **O bloco 1 não disse a classe do
veículo medido, e ela muda a leitura.** A coleta limpa de hoje achou o registro:

> **"Análisis de la eficiencia energética de la batería de ion litio en una moto
> eléctrica para el uso de micro movilidad"** — Rodrigo David Limaico Quinteros (autor),
> Carlos Alberto Carranco Quiñonez (tutor), Maestría en Ingeniería Automotriz, sede
> Quito, Universidad Politécnica Salesiana, **2025**. Bateria de **60 V e 30 Ah** (1.800
> Wh nominais) numa **moto elétrica**, em rota predefinida de **25,8 km** com subida,
> descida e trecho plano.

**O que isso corrige:** o valor **absoluto** de Wh/km de uma moto de 1.800 Wh não é o de
um patinete de 500 Wh — massa, área frontal e velocidade de cruzeiro são outras. O que
**atravessa** a classe de veículo é a **razão entre relevo e plano** medida na mesma
rota, com o mesmo veículo e a mesma bateria: **97,74 ÷ 41,29 = 2,37**. A F2 usa a razão,
nunca o absoluto — e isso está escrito como constante com esse nome em
`constantes.json`.

**O que o estudo entrega de novo, e o bloco 1 não tinha:** a mesma tese mede **29,8 km
de autonomia em condição mista contra 60 km declarados na ficha técnica** — **49,7% do
declarado**. O corpus registrou uma *"faixa de 60% a 80% do valor anunciado em uso
urbano"* como *"leitura agregada, sem fonte única"*, e dizia, ele mesmo, que não servia
como constante. **A medição nomeada cai ABAIXO do piso daquela faixa**, o que é a
direção que importa: a faixa agregada era otimista.

---

## 1. F1 — "ESSE ELÉTRICO PRECISA DE CNH?"

A home da ilha (`DESIGN.md`, `VOZ.md`). É a ferramenta que o bloco 1 mediu como vaga
real: em sete consultas independentes do eixo A, **nenhuma ferramenta** que receba
potência e velocidade e devolva categoria. *"Todos falam, ninguém calcula."*

### 1.1 Entradas — QUATRO, e a terceira é pivô

| # | Campo | Tipo | Obrigatório | Exemplo pré-preenchido na casca |
|---|---|---|---|---|
| 1 | `potencia_nominal_w` | inteiro, W | sim | `500` |
| 2 | `velocidade_max_kmh` | inteiro, km/h | sim | `32` |
| 3 | `acelerador` | **binário**: `manual` · `so_pedal_assistido` | sim | `manual` |
| 4 | `municipio` | texto, opcional | **não** | vazio |

**O campo 3 não é caixinha opcional no fim do formulário** — é a conclusão A2 do bloco 1,
e ela é a única coisa em que as fontes do eixo A não divergem: **acelerador manual tira o
veículo da definição de bicicleta elétrica mesmo com potência abaixo do limite**, e o
autopropelido, ao contrário, **pode** ter acelerador. Sem o campo 3, nenhuma potência
classifica. Na tela ele é um par de botões de rádio no mesmo nível visual dos dois
números, nunca um `checkbox` abaixo do botão de calcular.

**O campo 4 é opcional por desenho, e a sua ausência não cala a camada municipal** — ver
1.5. Município em branco imprime a ressalva genérica; município preenchido e **conhecido
pelo banco** imprime o limite daquele município; município preenchido e **desconhecido**
imprime a ressalva genérica dizendo que aquele município não está no banco. Três estados,
três frases, nenhuma delas silenciosa (seção 7: *"causa que o código separa, o texto
separa"*).

### 1.2 Saída — DUAS camadas, e elas nunca se misturam numa frase

**Camada 1 — categoria nacional.** Uma das três, mais o que ela implica:

| Categoria | O que a saída diz |
|---|---|
| `bicicleta_eletrica` | dispensa CNH e dispensa placa |
| `autopropelido` | dispensa CNH e dispensa placa |
| `ciclomotor` | **exige** habilitação e **exige** emplacamento |

**Camada 2 — a rua é municipal.** Uma linha, sempre impressa, mesmo quando a categoria
dispensa tudo: a categoria é nacional, **o limite de circulação é local**. O bloco 1 mediu
o motivo: Campinas aparece com **20 km/h** regulamentado, o Rio com **350 W / 25 km/h**
próprios, e duas prefeituras publicam folheto (`joinville.sc.gov.br`, `sjc.sp.gov.br`).
**A F1 que responde "autopropelido, dispensa CNH" sem essa linha está certa na categoria
e incompleta na rua.**

As duas camadas saem em **blocos separados com título próprio**. Fundi-las numa frase é o
defeito que a seção 7 nomeia como inventar uma das causas.

### 1.3 A DECISÃO DE ENGENHARIA QUE ESTE BLOCO TOMA: LIMIAR NUMÉRICO MORA **SÓ** EM `constantes.json`

A lógica de classificação da F1 **não depende** do texto oficial. O que depende são os
**números dos limiares**. Então a F1 nasce com a árvore inteira escrita e os limiares
referenciados **por nome**, nunca por literal no código:

```
se acelerador == so_pedal_assistido
   e potencia_nominal_w <= LIMIAR_BIKE_W
   e velocidade_max_kmh <= LIMIAR_BIKE_KMH        -> bicicleta_eletrica
senao se potencia_nominal_w <= LIMIAR_AUTOPROP_W
   e velocidade_max_kmh <= LIMIAR_AUTOPROP_KMH    -> autopropelido
senao                                             -> ciclomotor
```

Os quatro `LIMIAR_*` são **uma constante só** em `constantes.json`
(`limiares-categoria-contran-996-2023`), hoje com `valor: null` e `status: pendente`.
**Consequência declarada, e ela é dura: enquanto o status for `pendente`, a F1 não vai ao
ar.** Não vai ao ar com número de portal, não vai ao ar com o número que mais apareceu, e
não vai ao ar "com ressalva". A seção 10 do `ARQUIPELAGO.md` proíbe constante `pendente`
dentro de fórmula publicada, e aqui a fórmula publicada **é o produto da ilha**.

**O que isso compra:** quando o texto oficial chegar — pelo egresso liberado ou pelo
Chrome do Raphael, os dois caminhos do despacho ALTA —, a F1 inteira destrava **editando
um arquivo**: preencher os quatro valores, trocar `status` para `publicavel`, gravar
`url`, `verificado_em` e o artigo lido. Nenhuma linha de lógica muda. **É por isso que
este bloco não esperou a fonte: o que a fonte decide é um objeto JSON, e o que ela não
decide é tudo o mais.**

**O que isso NÃO permite:** nem a árvore acima nem a tabela pré-renderizada da 1.6 podem
nascer com número plantado "para testar". Caso de teste leva limiar **fictício e
declarado como fictício** no próprio caso (ver 1.6), e o portão da ferramenta compara
contra o fictício, nunca contra 1.000 ou 32.

### 1.4 AS DUAS RESSALVAS OBRIGATÓRIAS DA F1, as duas com caso medido

Não são rodapé: são parte da resposta, e cada uma nasce de um achado do bloco 1.

**(a) Potência de PICO não classifica.** O `PROMPT.md` já exigia, e o bloco 1 achou o caso
no título de loja grande: *"Bicicleta elétrica Siena **1000W** adulto sem CNH scooter"*
(`extra.com.br`) — quatro termos que a regra separa, num anúncio só. A F1 pergunta
**potência nominal** e diz, na mesma tela, que o número grande do anúncio costuma ser o
pico e que o que a regra lê está na ficha. Entrada de pico **não** vira classificação: se a
pessoa não sabe qual dos dois tem, a F1 diz que não sabe classificar, e diz onde olhar.

**(b) Veículo alterado depois da compra sai da categoria.** O caso é medido e tem fonte:
scooter **adulterada** flagrada a **73 km/h** com velocidade de fábrica declarada de **32
km/h** (`folhavitoria.com.br`, colhido em 28/10/2026). A categoria sai da **ficha de
fábrica**, não do velocímetro nem do destaque do anúncio. E a frase de vendedor *"não
exige CNH nem emplacamento, conforme legislação vigente"*, colhida num anúncio, é
afirmação de quem vende — a F1 nunca a repete.

### 1.5 O QUE A F1 SE RECUSA A RESPONDER

- **Não afirma além da resolução.** Nada sobre multa, apreensão, idade mínima, uso de
  capacete, calçada, ciclovia ou seguro — o `VOZ.md` proíbe *"qualquer frase que afirme o
  que a resolução não diz"*, e o produto desta ilha é a categoria, não o manual do
  trânsito.
- **Não classifica sem o campo 3.** Formulário enviado sem o pivô não devolve categoria:
  devolve o pedido do campo que falta, explicando em uma linha por que ele decide.
- **Não classifica por nome comercial.** "Scooter" não é categoria da resolução — o bloco 1
  mediu isso em título de varejo. A F1 recebe números e devolve categoria; marca e nome
  do anúncio entram na resposta só como o que a página contradiz, nunca como entrada.
- **Não diz "pode andar à vontade".** Frase proibida nominalmente no `VOZ.md`.

### 1.6 TABELA PRÉ-RENDERIZADA — a metade que a IA lê sem preencher formulário

Obrigatória pela seção 5 (visibilidade em IA) e pela 32.1 item 6: visível, **nunca
recolhida**. Linhas = combinações reais colhidas no bloco 1, não grade sintética:

| Veículo colhido | W nominal | km/h | acelerador | fonte do dado |
|---|---|---|---|---|
| Honeywhale M2 MAX | 500 | 32 | manual | painel Shopee, dossiê 27/10/2026 |
| MAXSHOT V1 | 350 | — | manual | ficha `extra.com.br`, 28/10/2026 |
| MAXSHOT V1SPRO | 500 | — | manual | ficha `extra.com.br`, 28/10/2026 |
| Sousa Bike aro 24 | 350 | — | **manual** (diz no título) | ficha `extra.com.br`, 28/10/2026 |
| Siena "1000W adulto sem CNH" | 1.000 | — | não declarado | ficha `extra.com.br`, 28/10/2026 |
| Honeywhale H3 | 1.000 | 55 | manual | anúncio ML, 28/10/2026 |
| modelo "melhor de 2026" do guia | 2 × 1.000 | 72 | manual | `guiadosperifericos.com.br`, 28/10/2026 |

**A coluna "categoria" desta tabela está VAZIA neste bloco, e isso é proposital.** Ela só
pode ser preenchida pelos limiares da 1.3, e eles são `pendente`. A tabela nasce no bloco
de construção da F1 com a coluna preenchida, ou não nasce.

**Para o caso de teste do portão da ferramenta:** o portão usa limiares **fictícios**,
declarados como fictícios no próprio caso (por exemplo `LIMIAR_AUTOPROP_W = 777`), e
afirma a **árvore**, não os números do mundo. Portão que afirma 1.000 W antes de o texto
oficial chegar é o número de tela digitado com outra roupa.

### 1.7 O BLOCO DE COMPRA DA F1 — a parte que não depende da resolução

Pela 32.1 item 5, o bloco de compra vem **imediatamente abaixo do resultado** e antes de
qualquer procedência (seção 7). Na F1 o critério de entrada do produto é **a categoria
que a pessoa acabou de receber**: os modelos do banco que caem naquela categoria, com a
especificação que fez cada um entrar (W nominal e km/h declarados) impressa no cartão.

**Prestação de contas (seção 7), e ela vale na tabela também:** **todo** veículo do banco
na categoria consultada aparece **exatamente uma vez** na prosa da resposta — na frase que
o recomenda, e aí ele está na vitrine, ou numa linha que diz **por que** não está. A soma
dos nomeados fecha o banco, contado, nunca digitado. Grupos por causa, com nome próprio e
nunca fundidos:

1. **Cabem na categoria** — vitrine.
2. **De outra categoria** — nomeados, com a categoria deles.
3. **Não declaram potência nominal** (só o número do título) — nomeados, e é a ressalva
   1.4(a) com produto na mão.
4. **Sem link de compra ainda** — nomeados, e **nenhum fica sem saída**: o piso é o link
   de busca da seção 25.2. A frase "link de loja em breve" é proibida.

---

## 2. F2 — "QUANTOS KM ELE FAZ DE VERDADE?"

### 2.1 Entradas

| # | Campo | Tipo | Obrigatório | Exemplo pré-preenchido |
|---|---|---|---|---|
| 1 | `tensao_v` | inteiro, V | sim | `48` |
| 2 | `amperagem_ah` | decimal, Ah | sim | `20` |
| 3 | `peso_piloto_kg` | inteiro, kg | sim | `90` |
| 4 | `relevo` | `plano` · `misto` · `ladeira` | sim | `misto` |
| 5 | `autonomia_declarada_km` | inteiro, km, opcional | não | `60` |

### 2.2 A CONTA, em três degraus de força de prova diferente — e eles ficam separados

**Degrau 1 — a energia. `Wh = V × Ah`.** É **identidade**, não fonte: 48 V × 20 Ah = 960
Wh; 60 V × 20 Ah = 1.200 Wh. Publicável sem depender de egresso nenhum, e é por si só
metade do valor da F2 — o bloco 1 mediu que **a autonomia anunciada sobe com a potência do
motor** nas fichas (350 W → 20 km; 1.000 W → 70/75 km; 2.000 W → 100 km), *"que não é a
grandeza que armazena energia"*. **Pôr Wh ao lado do número declarado é a ferramenta
inteira funcionando, e não precisa de mais nada.**

**Degrau 2 — o relevo, pela RAZÃO e nunca pelo absoluto.** Da tese da UPS Quito de 2025
(0.2): na mesma rota, mesmo veículo, mesma bateria, **97,74 ÷ 41,29 = 2,37**. É o fator de
`ladeira` contra `plano`; `misto` fica no meio-caminho geométrico (≈ 1,54 = √2,37) **como
decisão da ilha declarada, não como medição** — o estudo mediu os extremos e o misto,
mas o misto dele é a rota dele, com a proporção de subida dele.

**Degrau 3 — o consumo absoluto por km. `pendente` para patinete.** A única medição de
patinete achada hoje (≈ 20 Wh/km, com 18,1 a 20,1 Wh/km em mais de 4.000 km rodados e 70
ciclos) está em periódico vietnamita cujo host **não resolve nesta nuvem**, sem autoria
confirmada na busca. **Não é constante publicável.** O valor de ≈ 10 Wh/km da
`ozo-electric.com` é de **bicicleta** e de **fabricante de kit** — interesse comercial
declarado, e classe de veículo errada.

**Portanto a F2 nasce sem o degrau 3**, e o que ela publica é:

```
Wh = V × Ah                                    (identidade)
piso_km  = autonomia_declarada_km / FATOR_RELEVO   quando a pessoa informou a declarada
faixa_km = [piso_km , autonomia_declarada_km]
```

— ou seja, **a F2 não inventa um km absoluto: ela degrada o número que o fabricante
declarou, pela razão de relevo medida, e mostra o Wh ao lado.** Sem a declarada, a F2
devolve o Wh e **diz que não estima km**, nomeando o que falta (ver 2.4). É a seção 7 em
ação: recusa que nomeia a causa que a página mediu.

### 2.3 A CALIBRAÇÃO QUE A TESE DÁ DE GRAÇA, e ela é a frase mais vendável da ilha

A mesma tese mede **29,8 km em condição mista contra 60 km declarados na ficha** —
**49,7%**. Isso **não entra como fator de cálculo** (uma medição, um veículo, uma rota),
mas entra como **linha de calibração da tabela pré-renderizada**, com autor, instituição e
ano na própria frase (seção 5, item 4). O corpus registrava *"60% a 80% do declarado"*
como leitura agregada sem fonte única; a medição nomeada fica **abaixo** desse piso, e a
página diz as duas coisas com o nome de quem publicou cada uma.

### 2.4 O QUE A F2 SE RECUSA A RESPONDER

- **Não devolve km sem autonomia declarada** enquanto o degrau 3 for `pendente`. Devolve
  Wh, a comparação com veículos do banco de Wh parecido, e a linha dizendo que o km
  absoluto depende de uma régua de consumo que a ilha ainda não leu em fonte que alcança.
- **Não contesta o número do fabricante.** Põe Wh ao lado dele e a faixa degradada; quem
  conclui é quem lê. O `PROMPT.md` diz isso com todas as letras.
- **Não converte peso do piloto em km** — nenhuma régua de Wh/km por kg de condutor foi
  achada em fonte alcançável. O campo 3 entra na **escolha do grupo de relevo** e na
  ressalva, não numa fórmula: peso alto com `ladeira` imprime o aviso de que a faixa fica
  no piso dela. Campo que não alimenta conta e alimenta ressalva **fica declarado assim**,
  nunca disfarçado de entrada de cálculo.
- **Não promete autonomia de bateria usada nem fala de degradação por ciclo** — sem fonte.

### 2.5 Tabela pré-renderizada da F2

Linhas = combinações de V × Ah colhidas em ficha real, com Wh calculado (identidade),
autonomia declarada quando existe, e a faixa degradada pelos três relevos. Mais a linha de
calibração da 2.3, marcada como medição de terceiro e não como cálculo da página.

### 2.6 Bloco de compra da F2

Critério de entrada: **Wh do veículo**, que é a grandeza que a ferramenta acabou de
calcular — e a especificação impressa no cartão é `V × Ah = Wh`, nunca "autonomia de até".
Peça entra onde a resposta a pede: **bateria por V/Ah** e **carregador pela tensão** são as
duas peças que a F2 nomeia (bloco 3 do `PROMPT.md`). A prestação de contas da 1.7 vale
igual, com os grupos por causa: cabem no Wh pedido · de outro Wh · **não declaram V ou Ah**
(a classe de defeito mais comum nas fichas colhidas) · sem link ainda.

---

## 3. F3 — "AGUENTA O MEU PESO?"

### 3.1 Entradas

| # | Campo | Tipo | Obrigatório | Exemplo pré-preenchido |
|---|---|---|---|---|
| 1 | `peso_piloto_kg` | inteiro, kg | sim | `110` |
| 2 | `carga_kg` | inteiro, kg | não (vale 0) | `8` |

O exemplo pré-preenchido é a pessoa do `VOZ.md`: *"O patinete aguenta 100 kg. Você e a
mochila dão 108."* O caso de exemplo da casca é um caso **que dá 'no limite'**, não um que
passa folgado — é a 32.1 item 4 servindo a pergunta real da ilha.

### 3.2 Saída — TRÊS grupos, e o do meio é a razão de a ferramenta existir

`peso_total = peso_piloto_kg + carga_kg`

| Grupo | Critério | O que a saída diz |
|---|---|---|
| **Aguenta com folga** | `carga_max_kg >= peso_total × (1 + MARGEM)` | vitrine, em primeiro lugar |
| **Passa, mas no limite** | `peso_total <= carga_max_kg` **e** abaixo da margem | nomeados, com o aviso da 3.4 |
| **Não aguenta** | `peso_total > carga_max_kg` | nomeados, com os kg que faltam |

Os três grupos saem **em blocos separados, com título próprio**, e o grupo "no limite"
**nunca aparece em primeiro lugar** — seção 7: *"quem passa na principal e falha em outra
vai para seção separada, abaixo, rotulada"*, e *"recomendar em primeiro lugar um produto
que a própria página diz não servir é defeito GRAVE"*.

### 3.3 A MARGEM É **DECISÃO DA ILHA**, E ISSO FICA ESCRITO — a coleta limpa negou a fonte

O bloco 1 escreveu que *"uma fonte estrangeira colhida sugere margem de pelo menos 10%
acima do peso do condutor"*. **A coleta limpa de hoje procurou essa régua e não a achou
publicada em nenhum número.** O que as fontes trazem é **qualitativo e convergente** (3.4).
Uma loja espanhola sugere escolher capacidade de 100 a 120 kg — recomendação comercial de
catálogo, não régua, e ainda por cima de outro mercado.

**Portanto `MARGEM` nasce como `decisao_da_ilha`, em 10%, com o motivo escrito** e não como
dado de terceiro. A direção da escolha sai do erro caro, como manda a família de regras do
arquipélago: **quem compra um patinete que não aguenta o peso perde o veículo e pode se
machucar; quem compra um com folga paga um pouco mais.** O erro assimétrico aponta para a
folga. E 10% sobre o teto de mercado de **120 kg** exclui quem passa de **109 kg** — que é
exatamente a pessoa do `VOZ.md`, e é por isso que o número não é cosmético.

**A página nunca atribui a margem a ninguém.** Ela diz que é critério da Rodametria, com o
motivo, numa linha. Atribuir a terceiro uma régua que terceiro não publicou é o defeito que
esta seção existe para não cometer.

### 3.4 A RESSALVA SOURCED DA F3 — perto do limite, o veículo não entrega o que anuncia

Esta, sim, tem fonte, e ela é convergente em três publicadores colhidos em 28/10/2026:
quem está **perto do peso máximo anunciado** pode **não obter a velocidade e a aceleração
máximas declaradas pelo fabricante** (`race.es`), *"o peso não deve exceder a recomendação,
pois o desempenho pode ser afetado"* (`milar.es`), e o limite extra *"evita sobrecarga no
motor e mantém a velocidade e a segurança, mesmo com peso adicional"* (`br.my-best.com`,
publicador brasileiro). **É a frase do grupo "no limite", e ela amarra a F3 à F2:** peso
perto do teto não derruba só a carga — derruba a velocidade e a autonomia. A F3 linka para
a F2 com o peso já passado na URL (32.2).

### 3.5 O QUE A F3 SE RECUSA A RESPONDER

- **Não estima carga máxima de veículo que não a declara.** Sem `carga_max_kg` na ficha, o
  veículo vai para um quarto grupo nomeado — *"não declara carga máxima"* — e **não** entra
  na vitrine. Estimar por aro, por potência ou por "parece reforçado" é inventar dado.
- **Não fala de peso de bagageiro, garupa ou carona** — o bloco 1 não mediu nada disso, e o
  autopropelido é monoposto na prosa colhida, o que é afirmação de terceiro e não da
  resolução lida.
- **Não devolve "nenhum modelo serve" em silêncio.** Este é o eixo com a maior chance de
  devolver lista vazia (corpus, seção 6, item 4): o teto de mercado medido é 120 kg, com um
  modelo de 115 kg e dois patinetes de 120/140 kg no painel da Shopee. Lista vazia imprime
  **a causa que a página mediu** — "o maior teto do nosso banco é X kg, e você pediu Y" —,
  com o número do banco contado, nunca uma hipótese sobre por que ninguém serve.

---

## 4. O QUE VALE PARA AS TRÊS, e não se repete em cada uma

**Molde da seção 32 (ferramenta).** Trilha e H1 · uma frase de promessa · formulário já
preenchido com o caso de exemplo · caixa de resultado **pré-renderizada no HTML** com esse
caso · bloco de compra imediatamente abaixo · tabela de casos resolvidos visível e nunca
recolhida · o resto em `<details>`. No celular, barra fixa com o resultado e o botão para o
bloco de compra. Pronto quando: formulário antes de 700 px, primeiro botão de compra antes
de 1.400 px, HTML servido com JS desligado contendo o texto inteiro, console limpo (32.5),
conferido por portão que **lê o `wp-sitemap.xml` no ar** e varre todas as páginas de molde
(32.5-b), nunca por lista.

**Visibilidade em IA (seção 5).** `WebApplication` em cada ferramenta, `FAQPage` onde
couber, `Dataset` no banco, `Organization` com `sameAs`. Resposta antes da explicação, em
frase autossuficiente que sobrevive a ser citada fora de contexto. Procedência **dentro da
frase**: *"segundo <fonte>, <afirmação> (lido em DD/MM/AAAA)"*.

**Monetização (seções 7 e 25).** Bloco de compra **antes** da procedência; procedência
discreta, texto "fonte", `rel="nofollow noopener"`, nunca botão. Afiliado com
`rel="sponsored"` + `target="_blank" rel="noopener"`, aviso de comissão visível, preço
**sempre com data da coleta**. Shopee primeiro quando o produto existe nos dois; Mercado
Livre só onde a Shopee não tem; Amazon fora. Nenhum item publicável sem saída de compra —
piso é o link de busca da 25.2.

**Voz (`VOZ.md`).** Veredito na primeira linha. Nunca no título nem no primeiro parágrafo:
"regulamentação vigente", "consulte um especialista", "conforme a legislação aplicável",
"consulta paramétrica", "procedência". Nada de "melhor patinete" em título — o bloco 1 mediu
que essa família é ocupada por fazenda (`guiadosperifericos`, `cupomonline`,
`guiarecomenda`) e o `VOZ.md` já a proibia. **E nada de texto de bastidor da fábrica na
página pública (32.4):** "egresso", "SERP", "snippet", nome de seção do contrato, nome de
rotina.

**O que atravessa as três e é a frase da ilha:** *o número grande do anúncio não é o número
que a regra lê.* Na F1 é o pico contra o nominal; na F2 é o watt do motor contra o Wh da
bateria; na F3 é o teto declarado contra o peso real com a mochila.

---

## 5. O QUE ESTE BLOCO DEIXA PRONTO PARA O BLOCO 3 (modelo do banco)

1. **Os campos que as três ferramentas LEEM, e eles são o contrato do banco:**
   `potencia_nominal_w`, `potencia_pico_w` (separados, e a F1 só lê o nominal),
   `velocidade_max_kmh`, `acelerador` (**enum de dois valores**, não booleano com nome
   ambíguo), `tensao_v`, `amperagem_ah`, `energia_wh` (derivado, nunca digitado),
   `autonomia_declarada_km`, `carga_max_kg`, `categoria` (**derivada da F1, nunca campo de
   entrada do catálogo** — gravar categoria à mão é o anúncio escrevendo a regra).
2. **Quatro grupos de recusa por ferramenta**, cada um com nome próprio, porque a seção 7
   exige que a causa que o código separa o texto separe. O banco tem de distinguir
   *"declara e falha"* de *"não declara"* — são grupos diferentes na página, logo são
   estados diferentes no registro.
3. **O enum de `acelerador` é pivô da F1**, então ele **não aceita nulo silencioso**: ficha
   sem a informação grava `nao_declarado`, que é um terceiro valor com frase própria, e
   **nunca** cai no lado "só pedal assistido" por omissão.
4. **`energia_wh` é derivado de V × Ah**, nunca copiado de anúncio. Anúncio que declara Wh
   em desacordo com V × Ah é divergência a registrar, não a média.
5. **O que o bloco 3 NÃO resolve e não se resolve daqui:** os limiares da 1.3 (despacho ALTA
   de 28/10) e a régua de consumo por km do degrau 3 da 2.2. Os dois são despacho, não
   bloco — e o segundo nasceu nesta execução, porque a fonte dele foi medida como inalcançável
   hoje.
