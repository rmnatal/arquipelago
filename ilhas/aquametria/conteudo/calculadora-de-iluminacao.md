---
id: calculadora-de-iluminacao
tipo: pagina
titulo: "Quanta luz o seu aquário precisa?"
slug: calculadora-de-iluminacao
meta_descricao: "Quantos lúmens o seu aquário plantado precisa? A faixa pelas três leituras brasileiras que discordam, mais fotoperíodo, Kelvin e consumo por mês."
cluster: C15
calculadora: c15-iluminacao
fontes:
  - "iluminacao-lumen-por-litro — três leituras BR do corpus de 04/09/2026 (peixeseaquarismo, aquarioturbinado, aquariosplantados), status divergente-fontes-br. Discordam por até 2 vezes sobre o mesmo rótulo"
  - "fotoperiodo — low tech 6 a 8 h, high tech 8 a 10 h, combate a alga 5 a 6 h, ciclagem 4 a 6 h (status divergente-fontes-br)"
  - "temperatura-de-cor, 6500 a 8000 K para aquário plantado (status divergente-fontes-br)"
  - "co2-concentracao, 15 a 35 mg/L úteis e risco acima de 30 a 35 mg/L — CO2Art pelo corpus (status divergente-fontes-br). Os dois extremos se sobrepõem"
  - "cobertura-luminaria-declarada — convenção editorial da Aquametria de 08/09/2026, derivada dos cinco registros do banco que declaram peça E cobertura (status convencao-editorial)"
  - "ppfd-por-litragem — PENDENTE, recusada em fórmula. O fórum de suporte da própria Chihiros declara que não existe teste de PAR oficial da linha WRGB II Pro"
  - "fichas das luminárias sugeridas: dados/produtos-iluminacao.json, fonte e data por campo"
verificado_em: 2026-09-08
publicar: true
---

Quanta luz o seu aquário plantado pede depende de quão exigentes são as suas plantas — e, num aquário de 100 litros, **iluminação baixa** pode querer dizer 1.000 lúmens ou 2.000, conforme a régua que você abrir. As três que circulam no aquarismo brasileiro chamam a mesma faixa pelo mesmo nome com o dobro do número.

Esta página não escolhe uma delas. Mostra as três nos litros do seu aquário, lado a lado, e diz quantas horas deixar aceso.

[aquametria_calculadora_iluminacao]

## O que ela faz de diferente

Três coisas que as tabelas copiadas não fazem.

**Publica a divergência em vez de escondê-la numa média.** A faixa consolidada — baixa 10 a 20, média 20 a 40, alta 40 a 60+ lm/L — é o que as três fontes, juntas, sustentam. A média delas seria um número mais bonito e mais falso: inventaria um consenso que não existe.

| Nível | peixeseaquarismo | aquarioturbinado | aquariosplantados |
|---|---|---|---|
| Baixa exigência | 20 lm/L | 10 a 20 lm/L | 15 lm/L |
| Exigência média | 30 a 40 lm/L | 20 a 40 lm/L | 30 lm/L |
| Alta exigência | 60 lm/L | acima de 40 lm/L | 60 lm/L |

Repare na última linha: uma das fontes escreve "acima de 40 lm/L" e para por aí. É por isso que a resposta do nível alto sai com um sinal de mais em vez de um teto — não existe teto declarado para inventar.

**Confere se a luminária cobre o seu vidro.** Luminária que não cobre o comprimento do aquário ilumina o meio e deixa as pontas na sombra, e nenhum varejo avisa disso. Por isso o comprimento do aquário é entrada da calculadora, e por isso só entra na lista de produtos a luminária cujo fabricante ou lojista **declara** o comprimento de aquário que ela cobre.

**Mostra o custo da luz acesa.** Potência vezes horas é física, sem divergência de fonte: o painel de consumo devolve kWh por mês do fotoperíodo que você escolheu. Em reais só sai com a sua tarifa, digitada por você — não publicamos tarifa de energia, porque ela muda por distribuidora, por bandeira e por faixa de consumo.

## O que ela não faz, e por quê

**Não publica PPFD (ou PAR).** É a medida correta, e sabemos disso: o lúmen conta a luz que o olho humano enxerga, na superfície da água; o PPFD conta os fótons que a planta pode usar, na profundidade em que ela está. Nenhuma fonte brasileira do nosso levantamento publica PPFD por litragem — e, em setembro de 2026, encontramos a razão a montante: no fórum de suporte da **própria Chihiros**, cujo argumento de venda é PAR, a resposta oficial sobre a tabela de PAR da linha WRGB II Pro é que **não existe teste oficial** e que o usuário procure medições no YouTube. Se o fabricante da luminária de 6 630 lúmens não publica, a fonte brasileira que copiaria dele também não tem. A constante `ppfd-por-litragem` continua pendente, e constante pendente é proibida em fórmula publicada aqui.

**Não converte o comprimento da peça em cobertura de aquário.** Seria cômodo: quase todo anúncio brasileiro traz o tamanho da peça, e quase nenhum traz o aquário que ela atende. Mas os registros do nosso banco que declaram **os dois números** mostram que não há razão constante a extrair:

| Luminária | Peça | Aquário coberto (declarado) | Cobertura ÷ peça |
|---|---|---|---|
| SunSun ADE-400c | 41 cm | 48 a 65 cm | 1,17 a 1,59 |
| WFish WF-H600 | 56,7 cm | 60 a 65 cm | 1,06 a 1,15 |
| Ista IL-401 60 | 56 cm | 56 a 66 cm | 1,00 a 1,18 |
| Chihiros WRGB II Pro 60 | 60 cm | 60 a 80 cm | 1,00 a 1,33 |
| LED 60 cm (Aquários do Rio) | 60 cm | 55 a 75 cm | 0,92 a 1,25 |

O teto declarado vai de 1,15 a 1,59 vez o comprimento da peça — uma peça de 41 cm que a loja diz cobrir 65 cm, outra de 60 cm que cobre 66. Fabricar uma razão média para essa tabela seria inventar número. A regra ficou registrada como convenção editorial (`cobertura-luminaria-declarada`), e o efeito prático dela é só barrar sugestão: nunca criar valor.

**Não publica número para aquário marinho nem para coral.** O levantamento não trouxe PAR nem lm/L de recife com fonte brasileira, e aqui não se extrapola água doce para coral.

**Não publica preço de hoje.** Desde 11/09/2026 a vitrine mostra a **cotação** que lemos no anúncio, com a data em que a lemos ao lado — que é outra coisa. Preço muda toda semana, e um número velho passando por atual seria pior que nenhum; um número velho que diz quando foi lido é informação honesta. Confira no anúncio antes de comprar: o valor da loja é o que vale.

## Como a lista de luminárias é montada

Três regras, iguais às das outras calculadoras:

1. **Adequação técnica ordena, comissão não.** A ordem é pela proximidade do meio da faixa que o seu aquário pede. Modelo sem link de loja aparece do mesmo jeito.
2. **Ficha com fonte e data em cada cartão.** A especificação vem do fabricante ou do varejo especializado, com endereço e data ao lado. O anúncio da loja nunca é a nossa fonte técnica — ele sustenta que o produto existe e é vendido, nada além.
3. **Sem produto adequado, não aparece produto nenhum.** Resposta sem sugestão é melhor que sugestão errada.

Um exemplo do que essas regras custam, e do que custa desfazê-las. Entre 08 e 09/09/2026 a Chihiros WRGB II Pro 60, de 6 630 lm, era a luminária mais cara do nosso banco, **tinha link de afiliado e não era sugerida**: nenhuma fonte que tínhamos declarava a voltagem dela, e voltagem errada queima o aparelho. A mais barata, uma Ista de 810 lm, era sugerida. Em 09/09/2026 a barreira caiu — e não porque afrouxamos a régua. Ao catalogar a família WRGB II inteira para cobrir os aquários acima de 80 cm, apareceu a declaração que faltava: o varejo brasileiro especializado anuncia dois membros diferentes da linha como **bivolt**, e a ficha da série descreve a alimentação como entrada de 100 a 240 V por fonte externa de 12 V. Um campo colhido para outros produtos destravou este. É assim que a lista cresce aqui: por dado que apareceu, nunca por exceção aberta para um produto que rende comissão. A calculadora publica a lista dos barrados e o motivo de cada um, embaixo da lista dos sugeridos — e hoje são onze, com a linha Soma inteira entre eles, todas com link e todas barradas pelo lúmen que ninguém publica.

## Fotoperíodo não compensa falta de lúmen

É o erro mais comum depois da luminária subdimensionada: deixar a luz acesa mais tempo porque a planta não cresce. A planta responde à intensidade que recebe; hora a mais com intensidade insuficiente alimenta alga antes de alimentar planta. Se falta luz, o que falta é lúmen, não hora.

Os quatro regimes que o levantamento trouxe — low tech 6 a 8 h, high tech 8 a 10 h, combate a alga 5 a 6 h e ciclagem 4 a 6 h — são faixas repetidas por fontes brasileiras que não publicam a medição por trás dos limites. Estão na tela com esse rótulo.

## CO2: os dois limites publicados se sobrepõem

A mesma fonte que dá 15 a 35 mg/L como faixa útil diz que acima de 30 a 35 mg/L há risco de toxicidade para os peixes. Os dois extremos se encavalam: 35 mg/L é ao mesmo tempo o teto do que é útil e o começo do que é perigoso.

Não escolhemos um lado dessa sobreposição, porque a fonte não escolheu — e porque, entre errar para mais e errar para menos, errar para mais mata peixe. O que resolve isso não é conta, é medição: o drop checker mostra **azul** para CO2 baixo, **verde** para dentro da faixa e **amarelo** para excesso, com atraso de uma a duas horas em relação ao que está acontecendo na água.

E vale a recíproca, que é o motivo de a calculadora avisar: luz alta **sem** CO2 é a receita clássica de alga. As fontes que publicam 40 a 60 lm/L publicam esse número junto de carbono injetado.

## Profundidade: onde a régua de lúmens por litro quebra

Dois aquários de 100 litros, um com 40 cm de lâmina e outro com 60 cm, recebem exatamente a mesma resposta em lúmens por litro — e não recebem a mesma luz no substrato. A água absorve e espalha luz ao longo do caminho, e lúmen por litro não tem dentro de si nenhuma informação sobre esse caminho.

A calculadora avisa quando a sua lâmina passa de 45 cm, que é o limite a partir do qual essa cegueira da fórmula começa a importar de verdade. Não corrigimos o número, porque corrigir exigiria justamente o PPFD por profundidade que ninguém publica. Dizer o que a própria conta não enxerga é o que separa esta página das tabelas copiadas.

## Continue por aqui

- [Quantos lúmens por litro o aquário plantado precisa](https://aquametria.com.br/2026/09/08/quantos-lumens-por-litro-aquario-plantado/) — o artigo pareado com esta calculadora: de onde saiu a regra, por que o lúmen é a unidade errada para planta e o que o varejo brasileiro não declara.
- [Quantos litros tem o seu aquário](https://aquametria.com.br/calculadora-de-litragem/) — o volume real, o comprimento e a lâmina que esta página usa saem de lá.
- [Qual filtro dá conta do seu aquário](https://aquametria.com.br/calculadora-de-vazao-do-filtro/) — o mesmo aquário visto pela filtragem; plantado pede corrente mais lenta.
- [Quantos watts de aquecedor você precisa](https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/) — o aparelho que mais pesa na conta de luz, e o único que pergunta quanto frio faz no seu cômodo.
- [Quanta mídia biológica cabe no seu filtro](https://aquametria.com.br/calculadora-de-midia-filtrante/) — luz forte com CO2 acelera o crescimento das plantas e a carga do filtro junto.
- [Como a Aquametria calcula](https://aquametria.com.br/metodologia/) — por que uma faixa com três fontes que discordam vale mais que um número redondo sem origem.
- [Como a Aquametria ganha dinheiro](https://aquametria.com.br/divulgacao-de-afiliados/) — o que é link de afiliado e o que ele não muda.
