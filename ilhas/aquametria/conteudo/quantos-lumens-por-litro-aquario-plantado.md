---
id: quantos-lumens-por-litro-aquario-plantado
tipo: artigo
titulo: "Quantos lúmens por litro o aquário plantado precisa (e por que o lúmen é a unidade errada para medir luz de planta)"
slug: quantos-lumens-por-litro-aquario-plantado
meta_descricao: "Três fontes brasileiras chamam a mesma faixa de iluminação pelo mesmo nome com o dobro do número. Fomos atrás de onde vem a regra de lúmens por litro, por que ela penaliza justamente a luminária feita para planta e por que ninguém no Brasil publica a medida certa."
cluster: C15
calculadora: c15-iluminacao
fontes:
  - "iluminacao-lumen-por-litro — peixeseaquarismo, aquarioturbinado e aquariosplantados, corpus de 04/09/2026 (status divergente-fontes-br)"
  - "fotoperiodo — quatro regimes do mesmo corpus (status divergente-fontes-br)"
  - "co2-concentracao — CO2Art pelo corpus (status divergente-fontes-br), com os dois limites se sobrepondo"
  - "ppfd-por-litragem — PENDENTE. Fórum de suporte da Chihiros: não existe teste de PAR oficial da linha WRGB II Pro, coletado em 08/09/2026"
  - "fichas de luminária de dados/produtos-iluminacao.json: Ista I-401 45 e IL-401 60, Chihiros WRGB II Pro 60, SunSun ADE-400c, WFish WF-H600 e o LED 60 cm dos Aquários do Rio, todas com fonte e data por campo"
  - "definição fotométrica do lúmen (curva de visibilidade fotópica, pico no verde) e faixas de absorção da clorofila: conhecimento de definição, não constante colhida — e o artigo diz isso"
verificado_em: 2026-09-08
publicar: true
---

Um aquarista brasileiro que queira dimensionar a luz do aquário plantado encontra, nas três primeiras páginas de resultado, a mesma tabela três vezes. Três autores, três colunas, os mesmos rótulos: baixa, média, alta. E números que não batem.

| Nível | peixeseaquarismo | aquarioturbinado | aquariosplantados |
|---|---|---|---|
| Baixa | 20 lm/L | 10 a 20 lm/L | 15 lm/L |
| Média | 30 a 40 lm/L | 20 a 40 lm/L | 30 lm/L |
| Alta | 60 lm/L | acima de 40 lm/L | 60 lm/L |

Para um aquário de 100 litros, "iluminação baixa" significa 1 000 lúmens numa fonte e 2 000 na outra. É o dobro, para a mesma palavra. Nenhuma das três diz de onde tirou o número, nenhuma cita as outras duas, e nenhuma menciona a diferença.

Se você só quer o número no seu volume, com as três leituras lado a lado e a lista de luminárias que atendem, ele está na [calculadora de iluminação e fotoperíodo](https://aquametria.com.br/calculadora-de-iluminacao/). Este texto é sobre o que está por trás dele: de onde essa régua veio, por que ela é estruturalmente frágil e o que o varejo brasileiro deixa de declarar.

## O lúmen é uma unidade de olho humano

Essa é a fragilidade de fundo, e ela não é opinião: é a definição da unidade.

O lúmen mede fluxo luminoso ponderado pela sensibilidade do olho humano. A ponderação não é neutra entre as cores: ela dá peso máximo ao verde, perto de 555 nanômetros, e desconta fortemente o azul profundo e o vermelho profundo. É assim que a unidade foi construída, e faz todo o sentido para iluminar uma sala — quem vai enxergar a sala é uma pessoa.

Só que quem "enxerga" a luz do aquário plantado é a clorofila, e a clorofila trabalha principalmente **no azul e no vermelho** — justamente as duas pontas que o lúmen desconta.

A consequência é desconfortável para a regra de lm/L: **duas luminárias com o mesmo número de lúmens e espectros diferentes não entregam a mesma fotossíntese.** Pior: uma luminária projetada para planta, com muito vermelho e muito azul, tende a marcar **menos** lúmens do que uma luminária branca comum de mesmo consumo — e a régua de lúmens por litro vai considerá-la pior. A régua penaliza exatamente o produto feito para a tarefa.

O nosso próprio banco mostra o padrão, e vale registrar com o cuidado que ele merece: a Chihiros WRGB II Pro 60, que é uma luminária WRGB de aquário plantado, declara 74 W para 6 630 lm — **89,6 lm/W**. A Ista IL-401 60, uma calha branca de aquário, declara 35 W para 3 717 lm — **106 lm/W**. Dois produtos não provam nada sozinhos; são coerentes com o que a definição da unidade prevê, e é assim que este texto os apresenta: como indício, não como demonstração.

A medida que resolveria isso existe e tem nome: **PPFD**, o fluxo de fótons fotossinteticamente ativos, medido em µmol/m²/s — os fótons que a planta pode usar, contados na profundidade em que ela está. É o que a literatura de plantio usa. É o que deveria estar nesta página.

## Por que ninguém publica PPFD — e onde a trilha termina

A resposta preguiçosa seria "porque a web brasileira copia mal". Fomos atrás e a trilha termina bem antes do Brasil.

Procurando a tabela de PAR da linha WRGB II Pro para o nosso banco, chegamos ao fórum de suporte da **própria Chihiros** — uma marca cujo argumento de venda é justamente intensidade de PAR. A resposta oficial, publicada lá, é que **não existe teste de PAR oficial** desses modelos e que o usuário procure medições feitas por terceiros no YouTube.

Isto é, o fabricante de uma luminária de 6 630 lúmens não publica a grandeza que dimensiona o produto dele. A fonte brasileira que copiaria essa informação não tem de onde copiar. E o número que circula por aí — "PAR 50 a 60 no substrato" — costuma vir sem a distância em centímetros, o que o torna inútil: PPFD sem distância declarada não diz nada, porque a intensidade cai com o caminho percorrido. É por isso que o nosso banco recusa gravar PPFD desacompanhado de distância, e por isso a constante `ppfd-por-litragem` continua marcada como pendente, e proibida em fórmula publicada.

Enquanto isso, o lúmen fica como a única grandeza que ainda aparece nas fichas. Nem sempre.

## O que o varejo brasileiro declara: centímetros

Montando o banco de iluminação, o padrão apareceu rápido. De seis luminárias vendidas no Brasil com ficha catalogada:

- **duas não declaram lúmen nenhum** em fonte alguma — nem a ficha do varejo especializado, nem os anúncios de marketplace (SunSun ADE-400c e WFish WF-H600);
- **uma não declarava voltagem** em nenhuma fonte que encontramos — a Chihiros de 6 630 lm, a mais cara do banco. Essa saiu do buraco em 09/09/2026, quando catalogamos a família WRGB II inteira e o varejo brasileiro especializado anunciou dois membros da linha como bivolt; a lacuna era da nossa coleta, não do mercado;
- **todas as seis declaram centímetros**.

O banco cresceu bastante depois desse retrato — 26 luminárias em 09/09/2026 — e a proporção não melhorou: onze delas continuam barradas por não declarar lúmen, e oito dessas onze são a linha Soma WRGB inteira, que cobre de 20 a 130 cm de aquário e é vendida em nove lojas brasileiras. Nenhuma das nove publica o número.

Faz sentido comercial: o cliente chega na loja com a fita métrica do aquário na cabeça, não com o cálculo de lúmens. O problema é que centímetro não dimensiona luz. Uma peça de 60 cm pode ser de 24 W ou de 74 W — três vezes de diferença — e as duas cabem no mesmo aquário.

E tem uma segunda armadilha, que a coleta revelou por acaso: **o número no nome nem sempre é o tamanho da peça.**

| O que o nome promete | Quanto a peça mede | Que aquário a ficha diz cobrir |
|---|---|---|
| Ista IL-401 "60 cm" | 56 cm | 56 a 66 cm |
| WFish WF-H600 | 56,7 cm | 60 a 65 cm |
| SunSun ADE-400C | 41 cm | 48 a 65 cm |
| Chihiros WRGB II Pro 60 | 60 cm | 60 a 80 cm |
| LED 60 cm (Aquários do Rio) | 60 cm | 55 a 75 cm |

A primeira linha é o caso mais direto: a mesma página de varejo que chama o produto de "60 cm" no título declara, na ficha de dimensões, 56 × 12 × 4,6 cm. Quem compra pelo nome acha que está levando 60 cm de luminária e leva 56. Registramos isso no banco como conflito entre o nome comercial e a ficha, com a ficha vencendo — e a calculadora mostra os dois números no cartão do produto, em vez de escolher em silêncio.

A terceira linha mostra o outro extremo: uma peça de 41 cm que o fabricante declara cobrir até 65 cm de aquário, porque acompanha hastes reguláveis. Entre 1,17 e 1,59 vez o próprio comprimento.

É por isso que a Aquametria **não converte comprimento de peça em cobertura de aquário**. A razão entre os dois números varia demais entre produtos para virar constante, e inventar uma média serviria para uma coisa só: recomendar luminária que deixa as pontas do aquário na sombra.

## Onde as três fontes concordam

Elas concordam em mais do que parece, e é justo dizer isso.

Concordam na **ordem**: mais planta exigente, mais luz. Concordam na **ordem de grandeza**: a régua inteira vive entre 10 e 60 lm/L, não entre 1 e 600. E concordam, sem escrever com essas palavras, em algo que a calculadora transformou em aviso: os números altos — 40, 60 lm/L — aparecem sempre acompanhados de CO2 injetado. Ninguém publica "60 lm/L, e não precisa de carbono".

A discordância está nas **fronteiras**, e é exatamente onde uma pessoa comprando luminária precisa de precisão. "Baixa" é 10 ou 20 lm/L? Para um aquário de 100 litros, essa dúvida separa uma luminária de 1 000 lm de uma de 2 000 lm, que provavelmente é o dobro do preço.

Nossa posição: publicar a faixa que as três sustentam juntas e mostrar as três leituras com nome e sobrenome. Média, aqui, seria fabricar consenso.

## Mais horas não compensam menos lúmens

O erro que aparece depois da luminária subdimensionada é sempre o mesmo: a planta não cresce, e a pessoa aumenta o fotoperíodo.

Não funciona, e a razão é simples: a planta responde à intensidade que recebe enquanto a luz está acesa. Abaixo de um certo patamar, hora a mais não vira crescimento — vira tempo a mais de nutriente disponível na água com planta parada, que é a condição em que a alga leva vantagem. Por isso o regime de 5 a 6 horas aparece nas fontes brasileiras como **combate a alga**: é uma medida de contenção, não de dimensionamento.

Os quatro regimes que o levantamento trouxe — low tech 6 a 8 h, high tech 8 a 10 h, combate a alga 5 a 6 h, ciclagem 4 a 6 h — são faixas repetidas sem medição publicada por trás. Estão na calculadora com esse rótulo, e é assim que devem ser lidos.

## O que a régua não vê: profundidade

Dois aquários de 100 litros. Um tem 80 cm de frente por 30 de fundo e 40 cm de lâmina; o outro tem 40 × 40 e 62 cm de lâmina. Mesmo volume, mesma resposta em lúmens por litro — e uma diferença enorme na luz que chega ao substrato do segundo.

A água absorve e espalha luz ao longo do caminho, e nada em "lúmens por litro" carrega informação sobre esse caminho. Um aquário alto pede mais luz na superfície para entregar a mesma coisa lá embaixo, e a régua não sabe disso.

Poderíamos publicar um fator de correção por profundidade. Não vamos: seria um número inventado, e no formato mais perigoso possível — o formato que parece preciso. O que a calculadora faz é avisar, acima de 45 cm de lâmina, que ali a fórmula começa a mentir. Enquanto não houver PPFD por profundidade com fonte, esse aviso é a resposta honesta.

## Seis recomendações práticas

1. **Comece pelo lúmen declarado, não pelo watt.** Watt é consumo, não luz — e a eficácia dos LEDs vendidos aqui varia de 89 a 107 lm/W dentro do nosso próprio banco. Se a ficha não traz lúmen, você não tem como dimensionar a peça; considere isso na hora de comparar preços.
2. **Confira a cobertura declarada, não o nome do produto.** "60 cm" pode ser uma peça de 56 cm. O número que interessa é o comprimento de aquário que o fabricante afirma cobrir.
3. **Confira a voltagem antes de comprar.** É o campo que mais falta nas fichas brasileiras de luminária, e o erro nele queima o aparelho na primeira tomada.
4. **Se for de alta exigência, monte o CO2 junto.** Luz alta sem carbono é a receita clássica de alga, e todas as fontes que publicam os números altos os publicam com CO2 injetado.
5. **Não aumente o fotoperíodo para compensar luz fraca.** Se falta luz, falta lúmen. Hora a mais alimenta alga antes de alimentar planta.
6. **Em aquário fundo, superdimensione com consciência.** Acima de 45 cm de lâmina, o número da régua descreve mal o que chega ao substrato — e regulagem de intensidade (dimmer ou app) vale mais do que parece, porque deixa você corrigir para baixo depois de observar as plantas.

## O que ainda falta coletar

Três coisas, e a primeira delas é a que fecharia a pergunta:

**PPFD declarado com a distância em centímetros**, de luminárias vendidas no Brasil. Enquanto isso não existir, lm/L é o que dá para publicar com honestidade.

**Lúmen das duas luminárias barradas do banco** (SunSun ADE-400c e WFish WF-H600) e **voltagem da Chihiros WRGB II Pro 60**. São três campos que, se aparecerem numa embalagem fotografada, tiram três produtos da lista de barrados.

**Um protocolo de medição própria.** Existe um caminho tentador — medir lux com o celular e converter para PPFD — e ele tem um problema conhecido: o fator de conversão de lux para PPFD depende do espectro da luminária, e é diferente para uma calha branca e para uma WRGB. Sem o fator com fonte, a conversão vira exatamente o tipo de número inventado que esta ilha não publica. Fica registrado como coleta, não como método.

## Continue por aqui

- [Calculadora de iluminação e fotoperíodo](https://aquametria.com.br/calculadora-de-iluminacao/) — o número no seu volume, com as três leituras lado a lado e as luminárias que atendem à faixa no seu comprimento.
- [Calculadora de litragem](https://aquametria.com.br/calculadora-de-litragem/) — o volume real de água, que é a entrada de tudo aqui.
- [Calculadora de mídia filtrante](https://aquametria.com.br/calculadora-de-midia-filtrante/) — luz forte e CO2 aceleram o crescimento das plantas e a carga do filtro junto.
- [Calculadora de vazão do filtro](https://aquametria.com.br/calculadora-de-vazao-do-filtro/) — aquário plantado pede corrente mais lenta, e a faixa de lá muda por causa disso.
- [Como a Aquametria calcula](https://aquametria.com.br/metodologia/) — por que publicamos a divergência entre fontes em vez da média delas.
