---
id: calculadora-de-litragem
tipo: pagina
titulo: "Calculadora de litragem: quantos litros tem o seu aquário"
slug: calculadora-de-litragem
meta_descricao: "Medidas em centímetros para litros, com os três volumes que importam: o bruto que a loja anuncia, o interno depois do vidro e o volume real de água. Com a fonte de cada número."
cluster: C1
calculadora: c1-litragem
fontes:
  - "Geometria (definição de litro em centímetro cúbico) — não é constante de terceiro"
  - "borda-livre-padrao, 3 cm, convenção editorial da Aquametria (dados/constantes-calculadoras.json)"
  - "substrato-densidade e substrato-porosidade: constantes PENDENTES, recusadas em fórmula (dados/constantes-calculadoras.json)"
verificado_em: 2026-09-08
publicar: true
---

Um aquário de 80 × 40 × 40 cm é vendido como "aquário de 128 litros". Ele nunca tem 128 litros de água. O vidro ocupa espaço, a lâmina d'água para antes da borda, e o substrato e as rochas tomam mais um pedaço. Com vidro de 8 mm e a lâmina no valor inicial, sobram **109 litros** — 15 % a menos que a etiqueta —, e é esse número menor que define o filtro, o aquecedor, a mídia e quantos peixes cabem.

Esta calculadora devolve os três volumes separados, e diz de onde cada um vem.

[aquametria_calculadora_litragem]

## Os três volumes, e para que serve cada um

**Volume bruto** é comprimento × largura × altura ÷ 1000, com as medidas por fora. É o número que a loja anuncia, o que vem no anúncio e o que a busca pergunta. Serve para conversar sobre o aquário — não serve para dimensionar nada.

**Volume interno** desconta o vidro. A conta é geométrica: cada parede lateral entra duas vezes no comprimento e duas vezes na largura, e a base entra uma vez na altura. Um vidro de 8 mm em um aquário de 80 × 40 × 40 cm tira quase 10 litros. Sem a espessura informada, este número não existe, e a calculadora diz isso em vez de inventar uma espessura provável.

**Volume real de referência** é a lâmina d'água sobre a área interna, menos as rochas e a decoração que você informar. É o único volume que as outras calculadoras da Aquametria leem. Ele fica guardado no seu próprio navegador — sem conta, sem login, sem envio para servidor nenhum — e é reaproveitado quando você abrir a calculadora de vazão do filtro ou a de aquecedor.

## A borda livre é convenção nossa, e está declarado

O campo da lâmina d'água começa preenchido com a altura interna menos 3 cm. Esses 3 cm são uma **convenção editorial da Aquametria**, registrada como constante `borda-livre-padrao` com esse status — não são dado de fabricante nem norma. Existem porque quase ninguém enche o aquário até a borda, e porque um valor inicial razoável é melhor que um campo vazio.

Ajuste para a sua borda. Em um aquário de 40 cm de altura, a diferença entre 2 cm e 5 cm de borda livre é de cerca de 7 % do volume — mais do que a diferença entre dois modelos de filtro.

## Por que o substrato não é descontado

Esta é a recusa que define a página. Descontar substrato parece trivial e não é: o que importa não é o volume aparente do leito, e sim a **porosidade** dele, ou seja, quanta água fica entre os grãos. Um leito de cascalho grosso pode guardar quase metade do próprio volume em água.

Duas coisas impedem o desconto hoje:

- **Densidade**: as fontes brasileiras do nosso levantamento divergem em 100 % — uma publica "1 a 2 kg por litro", outra publica "1 kg ≈ 1 litro". Divergência desse tamanho não vira média.
- **Porosidade**: nenhuma fonte brasileira publica o valor, para nenhum tipo de grão.

As duas constantes estão registradas como `pendente`, e constante pendente é proibida em fórmula publicada aqui. Então a calculadora informa a altura do substrato, avisa que ele reduz o volume, e **não** desconta.

Isso tem uma consequência que precisa estar na tela: o volume real sai **superestimado**. A direção do erro importa mais que o tamanho dele.

| Onde o volume é usado | Efeito de superestimar | Direção |
|---|---|---|
| Vazão do filtro | pede vazão maior | segura |
| Potência do aquecedor | pede potência maior | segura |
| Volume de mídia filtrante | pede mais mídia | segura |
| Custo mensal de energia | custo estimado maior | conservadora |
| Lotação de peixes | permitiria mais peixe | **insegura** |
| Dosagem de produto | overdose | **insegura** |

Por isso a calculadora de lotação, quando entrar no ar, vai usar o pior caso — a lâmina menos a camada inteira de substrato — e por isso a calculadora de dosagem ficou de fora do lote inicial. Errar para cima em filtro custa dinheiro; errar para cima em dosagem mata peixe.

## Como o desconto vai ser liberado

Com medição própria, porque não existe fonte para citar. O protocolo já está desenhado: recipiente graduado, substrato seco até uma marca conhecida, água adicionada até cobrir os grãos; a porosidade é a água adicionada dividida pelo volume ocupado pelo leito. Três repetições para cada tipo de grão — areia grossa, cascalho fino e substrato fértil — com registro fotográfico de cada medição.

Quando essa medição existir, ela vira constante com fonte própria, a Aquametria passa a descontar o substrato e a página passa a mostrar de quanto foi o desconto e como ele foi medido. Até lá, o número que falta continua declarado como faltando.

## O caminho inverso

Quem já sabe quantos litros quer costuma estar escolhendo o móvel ou o espaço da parede. A segunda ferramenta da página resolve isso: informe o volume desejado e duas das três medidas, e ela devolve a terceira. O resultado é no volume **bruto** — a água que cabe é sempre menos, e a própria resposta mostra quanto seria com a borda livre padrão.

## Onde este resultado é usado

O volume real fica guardado no navegador e alimenta as próximas calculadoras. A primeira delas já está no ar: a [calculadora de vazão do filtro](https://aquametria.com.br/calculadora-de-vazao-do-filtro/) pega o volume real desta página e devolve a faixa de L/h que o seu aquário pede — do 1,76 renovações por hora que o fabricante do filtro dimensiona ao 10 x/h que a web brasileira repete. As outras entram no ar uma por vez: potência do aquecedor por delta térmico, mídia filtrante, consumo elétrico e lotação. A lista completa, com o estado de cada uma, está em [todas as calculadoras](https://aquametria.com.br/calculadoras/).

Antes de usar qualquer número desta página em uma compra, vale ler [como a Aquametria calcula](https://aquametria.com.br/metodologia/): toda constante tem fonte nomeada, endereço e data, e o que não tem fonte aceitável fica de fora da fórmula, com o motivo escrito.

**Verificado em 08/09/2026.** Calculadora versão 1.0.1.
