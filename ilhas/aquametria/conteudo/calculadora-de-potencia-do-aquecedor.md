---
id: calculadora-de-potencia-do-aquecedor
tipo: pagina
titulo: "Calculadora de potência do aquecedor: quantos watts, pelo frio que faz aí"
slug: calculadora-de-potencia-do-aquecedor
meta_descricao: "Quantos watts de aquecedor o seu aquário pede? A conta parte da mínima do seu cômodo, não do genérico 1 W por litro, e filtra pela sua voltagem."
cluster: C5
calculadora: c5-aquecedor-delta
fontes:
  - "wl-delta-ate-10, 1,0 a 1,5 W/L para até 10 °C de diferença — ReefFlow (status divergente-fontes-br). A ÚNICA fonte do corpus que amarra W/L a um delta declarado"
  - "wl-sul, até 2,0 W/L na região Sul — Casa da Ada (status divergente-fontes-br)"
  - "wl-generico, 1,0 W/L — repetida sem autoria única na web BR (status divergente-fontes-br)"
  - "wl-ehow, 1,3 W/L — eHow (status divergente-fontes-br)"
  - "eheim-jager-linha-comercial, 9 tamanhos de 25 a 300 W — Eheim e tabelas de varejo (status transcrita-varejo), completada em 08/09/2026"
  - "especies-parametros-iniciais, 8 espécies — Petz e Aquarismo Paulista (status transcrita-varejo)"
  - "u-vidro-aquario e temperatura-minima-por-cidade: PENDENTES, recusadas em fórmula"
  - "fichas dos aquecedores sugeridos: dados/produtos-aquecedor.json, fonte e data por campo"
verificado_em: 2026-09-08
publicar: true
---

Pergunte na internet brasileira quantos watts de aquecedor um aquário de 100 litros precisa e a resposta virá pronta: **100 watts**. Um watt por litro. O número aparece em loja, em blog, em vídeo e em grupo, sempre com a mesma segurança e nunca com uma pergunta que deveria vir antes: um watt por litro **para aquecer de quanto para quanto**?

Um aquário a 26 °C num apartamento em Belém, onde a mínima da madrugada é 23 °C, tem três graus para vencer. O mesmo aquário a 26 °C numa casa em Curitiba, onde o quarto chega a 11 °C numa noite de julho, tem quinze. É a mesma água, o mesmo vidro e o mesmo volume — e não é, de jeito nenhum, o mesmo problema de aquecimento. A regra de bolso brasileira responde igual para os dois.

Esta calculadora pergunta o que falta.

[aquametria_calculadora_aquecedor]

## O que ela faz de diferente

Ela pede **a temperatura mínima do cômodo onde o aquário fica** — não a média da cidade, não a mínima histórica do estado: quanto o ar daquele quarto marca na noite mais fria do ano. Dessa entrada sai a diferença de temperatura, o ΔT, que é o que um aquecedor de verdade tem de vencer.

Com o ΔT na mão, a calculadora faz uma coisa que nenhuma das fontes faz: **separa as regras que se aplicam ao seu caso das que não se aplicam**, e mostra as duas listas. Se a sua diferença é de 6 °C, a regra do ReefFlow entra, porque o autor dela declarou que vale para até 10 °C. Se a sua diferença é de 14 °C, essa mesma regra sai da conta e a tela diz, com essas palavras, que nenhuma fonte do nosso levantamento cobre o seu caso.

Saber qual regra **não** vale para você é parte da resposta. É, aliás, a parte que ninguém publica.

## De onde vem cada extremo da faixa

O nosso levantamento de setembro de 2026 encontrou quatro afirmações sobre watts por litro circulando no aquarismo brasileiro. Elas discordam entre si, e apenas uma delas diz em que condição vale.

| Constante | Valor | Condição que o próprio autor declarou | Fonte |
| --- | --- | --- | --- |
| `wl-delta-ate-10` | 1,0 a 1,5 W/L | diferença de até 10 °C entre ambiente e água | ReefFlow |
| `wl-sul` | até 2,0 W/L | região Sul | Casa da Ada |
| `wl-generico` | 1,0 W/L | nenhuma | repetida sem autoria única |
| `wl-ehow` | 1,3 W/L | nenhuma | eHow |

Verificado em 08/09/2026. Três das quatro não dizem para qual clima valem, e as duas genéricas discordam entre si em 30 % — para a mesma pergunta, sem condição nenhuma que explique a diferença.

A faixa que a calculadora devolve vai do menor watt por litro aplicável ao maior. Não é uma média: média entre fontes que discordam produz um número que ninguém publicou e que não tem de onde ser conferido. Cada extremo da nossa faixa carrega o nome de quem o afirmou.

## Por que a caixa do aquecedor não resolve

A saída fácil seria olhar o volume que o fabricante estampa na embalagem. Ela não resolve, e o próprio catálogo dos fabricantes mostra por quê.

A Eheim declara o modelo Jäger de **200 W para aquários de 30 a 400 litros**. É uma faixa de treze vezes. Dentro dela cabem 6,7 W por litro num extremo e 0,5 W por litro no outro — o mesmo aparelho, o mesmo texto, a mesma caixa.

Não é um deslize isolado. Ao levantar a linha inteira em 08/09/2026, apareceu o padrão:

| Modelo | Volume declarado | W/L no teto da faixa |
| --- | --- | --- |
| Jäger 25 W | 20 a 25 L | 1,00 |
| Jäger 50 W | 25 a 50 L | 1,00 |
| Jäger 75 W | 50 a 75 L | 1,00 |
| Jäger 100 W | 75 a 100 L | 1,00 |
| Jäger 150 W | 125 a 150 L | 1,00 |
| Jäger 200 W | 300 a 400 L | 0,50 |

Fonte: catálogo Eheim e tabelas de varejo europeu e norte-americano, transcritas em 08/09/2026 (status `transcrita-varejo`; as páginas não foram lidas diretamente e devem ser reconferidas no manual).

Dois achados de uma vez. O primeiro: **o catálogo do fabricante é construído sobre a mesma regra de 1 W por litro** que a web brasileira repete sem citar ninguém — ela não veio de lugar nenhum, ela veio da prateleira. O segundo: a própria linha quebra a regra no 200 W, e ninguém explica.

Há ainda um terceiro caso, e ele é o mais desconfortável: uma ficha de varejo brasileiro declara o **mesmo Jäger de 150 W para 200 a 300 litros**, contra os 125 a 150 litros da tabela acima. O mesmo aparelho, duas fichas, o dobro de diferença. As duas fontes são varejo, ou seja, do mesmo nível de confiança, e por isso nenhuma vence: o nosso banco publica as duas lado a lado, e o cartão do produto mostra a divergência em vez de escondê-la.

O volume da caixa serve para você escolher entre dois modelos parecidos. Ele não sabe quanto frio faz no seu quarto.

## O que esta calculadora não faz, e por quê

**Não calcula pela física.** O caminho certo seria `P = U · A · ΔT`: potência igual ao coeficiente de troca térmica, vezes a área que troca calor, vezes a diferença de temperatura. Isso corrigiria por formato do aquário, por espessura do vidro, por tampa. Falta a constante `u-vidro-aquario`, que está **pendente** no nosso banco: o coeficiente global do vidro com convecção natural nas duas faces, mais a perda por evaporação na lâmina livre — que costuma ser a maior parcela e é a mais difícil de achar com fonte. Sem essa constante, a via física não sai. Quando sair, esta página deixa de depender de regra de bolso, e é a entrega que torna a Aquametria a única referência do nicho no Brasil com física atrás do número.

**Não corrige por aquário tampado ou destampado.** O campo existe no formulário e muda o *texto* da resposta, nunca o número. Dizer "some 20 % se for aberto" seria inventar uma constante, e é exatamente a parcela que a `u-vidro-aquario` cobriria. O que a tela faz é honesto e útil: avisa que, com o aquário aberto, a faixa deve ser lida como piso.

**Não usa temperatura mínima por cidade.** A constante `temperatura-minima-por-cidade` também está pendente; a coleta prevista é a Normal Climatológica do INMET, 1991-2020, mínima média do mês mais frio por estação. Enquanto ela não existir, a mínima é entrada sua — e, sinceramente, isso é melhor: a mínima do seu quarto não é a mínima da sua cidade. Aquário em quarto interno de apartamento, com a porta fechada, esfria muito menos que aquário em sala com pé-direito alto e janela grande. Você sabe qual é o seu caso; um banco de dados climático não saberia.

**Não extrapola a regra de bolso.** Se a sua diferença passa de 10 °C, a única fonte que amarrou watts por litro a um delta já não fala do seu caso. A tela diz isso e entrega a faixa das regras genéricas como **piso**, avisando que pode ser insuficiente. Esticar o número da fonte para além do que ela afirmou seria a mesma coisa que inventá-lo.

## O que aqui é critério nosso

Duas escolhas desta página são convenção editorial da Aquametria, não constante com fonte, e por isso aparecem declaradas na própria tela do resultado:

> **Mirar no degrau comercial que cobre o topo da faixa.** Aquecedor não se vende em qualquer potência: a linha comercial tem degraus (25, 50, 75, 100, 125, 150, 200, 250 e 300 W). Entre dois degraus, indicamos o que cobre o topo. O motivo é assimetria de consequência — aquecedor subdimensionado trabalha ligado o tempo todo e, na noite mais fria, ainda assim não segura a temperatura; superdimensionado com termostato que funcione apenas liga menos vezes.

> **Dois aquecedores de metade da potência, acima de 150 W.** O argumento é modo de falha, não eficiência: termostato que trava ligado num aparelho de metade da potência aquece menos o aquário, e termostato que trava desligado deixa o outro segurando alguma coisa. Nenhuma fonte do nosso levantamento publica isso como regra — é raciocínio nosso, e está identificado como tal.

Quando a espécie preenche a temperatura-alvo, usamos o **meio** da faixa que a ficha publica. A faixa tem fonte; mirar no meio dela é convenção, e a tela diz isso também.

## As duas barreiras de segurança antes de qualquer produto

O bloco de aquecedores que aparece dentro do resultado é montado por adequação técnica, e só por ela. Mas duas condições vêm antes da adequação, porque são de segurança:

1. **A voltagem da sua tomada.** Aquecedor na voltagem errada queima — ou, pior, esquenta demais. Só entra na lista modelo que as nossas fichas trazem existindo em 110 V ou em 220 V, conforme você marcar. Este foi, aliás, o campo que durante dias barrou o banco inteiro de aquecedores: nenhum registro tinha voltagem com fonte, e sem ela nenhum produto podia ser sugerido. A coleta de 08/09/2026 resolveu isso para as duas linhas do banco.
2. **O termostato alcançar a sua temperatura-alvo.** Não adianta a potência bater se o botão não chega lá. Aquecedor que não alcança o alvo sai da lista, e o motivo aparece escrito na tela.

Sobre esse segundo ponto há uma decisão nova, e vale explicá-la.

### A faixa conservadora: o que fazer quando duas fichas discordam

A linha Roxin HT-1300/Q3 é o aquecedor popular brasileiro, e a faixa de ajuste dele aparece publicada de dois jeitos no varejo: **22 a 34 °C** numas fichas, **16 a 32 °C** noutras. As duas são varejo, ou seja, do mesmo nível de confiança. Nenhuma vence, e tirar a média seria inventar um número que ninguém publicou.

Até 08/09/2026 o nosso banco fazia o óbvio nesse caso: zerava o campo. Só que zerar o campo tirava a linha inteira das sugestões — o aquecedor mais vendido do Brasil ficava de fora por excesso de escrúpulo, e quem visitasse a página não veria nada.

A saída foi escrever uma regra nova no esquema do banco, a **V17**:

> Quando duas fontes do mesmo nível discordam sobre um intervalo, publica-se a **interseção** delas: o maior dos mínimos e o menor dos máximos. No caso do Roxin, 22 a 32 °C. Não é média nem escolha de fonte — é a única faixa que as duas fontes concordam que o aparelho cobre. Fora dela, o aparelho pode alcançar ou não, e a Aquametria não afirma que alcança.

Na prática: quem quer 30 °C para acará-disco vê o Roxin na lista, porque as duas fichas concordam que ele chega lá. Quem quer 33 °C não vê, e lê na tela que o termostato vai só até 32 °C pela faixa conservadora. Quem quer 20 °C para kinguio também não vê, porque a faixa conservadora começa em 22 °C. É menos do que o aparelho talvez faça, e é exatamente tudo o que as fontes sustentam.

A ficha de cada produto mostra o selo **faixa conservadora** e a frase que explica de onde o número saiu. Onde há uma fonte de fabricante, como na linha Eheim, a faixa declarada é usada direto e não há selo nenhum.

## O caminho inverso

A calculadora também responde à pergunta que a maioria das pessoas realmente tem: *o aquecedor de 100 W que eu já comprei serve?* Informe a potência e ela devolve até quantos litros ele cobre por cada regra, e quantos watts por litro ele entrega no seu aquário. Continua sem perguntar o frio — por isso o cálculo principal, lá em cima, é o que vale.

## O que conversa com esta página

- **[Calculadora de litragem (C1)](https://aquametria.com.br/calculadora-de-litragem/)** — de onde vem o volume real de água que esta página usa. Aquecedor se dimensiona sobre a água que existe, não sobre o número da etiqueta do aquário.
- **[Vazão do filtro (C3)](https://aquametria.com.br/calculadora-de-vazao-do-filtro/)** — o outro aparelho que o mesmo volume dimensiona, e a mesma história de fontes que discordam.
- **[Quantos watts de aquecedor o seu aquário precisa](https://aquametria.com.br/2026/09/08/quantos-watts-de-aquecedor-para-aquario/)** — o texto longo: de onde veio o "1 W por litro", por que ele erra sempre para o mesmo lado e o que muda quando se pergunta o frio.
- **[Como a Aquametria calcula](https://aquametria.com.br/metodologia/)** — a escada de fontes, o que é constante e o que é convenção declarada.
- **[Como a Aquametria ganha dinheiro](https://aquametria.com.br/divulgacao-de-afiliados/)** — link de afiliado, o que ele muda (nada na ordem) e o que não publicamos.
