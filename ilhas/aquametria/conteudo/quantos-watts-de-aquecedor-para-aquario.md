---
id: quantos-watts-de-aquecedor-para-aquario
tipo: artigo
titulo: "Quantos watts de aquecedor o seu aquário precisa (e por que \"1 W por litro\" erra sempre para o mesmo lado)"
slug: quantos-watts-de-aquecedor-para-aquario
meta_descricao: "O 1 W por litro não veio de um cálculo: veio da prateleira. Este texto mostra de onde a regra saiu, em que casos ela funciona por acidente, onde ela falha, e o que muda quando a conta pergunta o frio do seu cômodo."
cluster: C5
artigo_ancora_de: c5-aquecedor-delta
fontes:
  - "wl-delta-ate-10, 1,0 a 1,5 W/L para até 10 °C — ReefFlow (divergente-fontes-br)"
  - "wl-sul, até 2,0 W/L na região Sul — Casa da Ada (divergente-fontes-br)"
  - "wl-generico, 1,0 W/L — sem autoria única na web BR (divergente-fontes-br)"
  - "wl-ehow, 1,3 W/L — eHow (divergente-fontes-br)"
  - "eheim-jager-linha-comercial: 9 tamanhos, 25 a 300 W, volume declarado por potência (transcrita-varejo, 08/09/2026)"
  - "linha Roxin HT-1300/Q3: volume declarado e faixa de ajuste em conflito entre fichas de varejo BR (dados/produtos-aquecedor.json)"
  - "u-vidro-aquario: PENDENTE — bloqueia o cálculo físico e é dito no texto"
verificado_em: 2026-09-08
publicar: true
---

[aquametria_artigo_resposta]

Existe um número que todo mundo no aquarismo brasileiro sabe de cor: **um watt por litro**. Aquário de 60 litros, aquecedor de 60 W. Aquário de 200, aquecedor de 200. É simples, é fácil de repetir e é o tipo de regra que sobrevive por décadas justamente porque ninguém precisa entender para usar.

O problema não é a regra ser grosseira. Regras de bolso boas são grosseiras de propósito. O problema é que essa aqui **não diz para qual situação vale**, e por isso erra sempre na mesma direção — contra quem mora onde faz frio.

Se você quer ir direto ao número do seu caso, a **[calculadora de potência do aquecedor](https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/)** faz a conta perguntando a mínima do cômodo onde o aquário fica. Este texto é o porquê.

## De onde saiu o "1 W por litro"

A resposta mais provável não é lisonjeira para a regra: **ela veio da prateleira, não de um cálculo.**

Levantamos a linha de aquecedores Eheim Jäger inteira em 08/09/2026 — nove tamanhos, de 25 a 300 W. O que o fabricante declara, modelo a modelo, é isto:

| Modelo | Volume declarado pelo fabricante | Watts por litro no teto |
| --- | --- | --- |
| 25 W | 20 a 25 L | 1,00 |
| 50 W | 25 a 50 L | 1,00 |
| 75 W | 50 a 75 L | 1,00 |
| 100 W | 75 a 100 L | 1,00 |
| 125 W | 100 a 125 L | 1,00 |
| 150 W | 125 a 150 L | 1,00 |
| 200 W | 300 a 400 L | 0,50 |

Fonte: catálogo Eheim e tabelas de varejo europeu e norte-americano, transcritas em 08/09/2026. Status `transcrita-varejo` — as páginas não foram lidas diretamente e o dado deve ser reconferido no manual.

Olhe a coluna da direita. **Um vírgula zero, seis vezes seguidas.** O catálogo não deriva de um modelo térmico: ele nomeia cada aparelho pelo volume que dá exatamente 1 W/L. A regra de bolso brasileira não descobriu nada sobre física de aquário — ela leu a caixa e transformou o rótulo em lei.

Isso explica por que a regra é tão consistente entre fontes que não se citam. Todas leram a mesma prateleira.

## Onde a régua se quebra

Agora repare na última linha da tabela. O 200 W é declarado para 300 a 400 litros: **0,5 W por litro**, metade do resto da própria linha. E o mesmo fabricante, no catálogo geral, declara esse mesmo 200 W para **30 a 400 litros** — uma faixa de treze vezes, dentro da qual cabem 6,7 W/L num extremo e 0,5 W/L no outro.

Não é caso isolado de uma marca. A linha popular brasileira, a Roxin HT-1300/Q3, tem a mesma incoerência:

| Modelo Roxin | Volume declarado | W/L no teto | W/L no piso |
| --- | --- | --- | --- |
| 25 W | 20 a 35 L | 0,71 | 1,25 |
| 50 W | 40 a 60 L | 0,83 | 1,25 |
| 100 W | 50 a 150 L | 0,67 | 2,00 |
| 200 W | até 200 L | 1,00 | — |
| 300 W | 250 a 350 L | 0,86 | 1,20 |

Fichas de varejo brasileiro especializado, coletadas em 07 e 08/09/2026. A série não fecha: há buraco entre 35 e 40 litros e entre 200 e 250 litros, e sobreposição de três modelos entre 50 e 150 litros — um aquário de 60 L cabe, pela própria declaração do fabricante, no 50 W, no 100 W e no 200 W ao mesmo tempo. A razão watts por litro varia de 0,67 a 2,0 **dentro de uma única linha de produtos**.

E há o caso que mais incomoda: o Eheim Jäger de 150 W aparece declarado para **125 a 150 litros** numa tabela e para **200 a 300 litros** numa ficha de varejo brasileiro. O mesmo aparelho, o dobro de diferença, as duas fontes do mesmo nível de confiança. Nenhuma vence. No nosso banco as duas ficam publicadas lado a lado, e o cartão do produto mostra a divergência em vez de escolher uma calada.

A conclusão prática é curta: **o volume que vem na caixa serve para escolher entre dois modelos parecidos, e não serve para dimensionar.**

## A pergunta que falta

Um aquecedor de aquário faz uma coisa só: repõe o calor que a água perde para o ar. Quanto calor a água perde depende, principalmente, de três coisas — quanta superfície ela tem em contato com o ambiente, o que separa uma coisa da outra, e **quantos graus de diferença há entre as duas**.

O volume do aquário não está nessa lista. Ele entra por tabela, porque aquário maior costuma ter mais superfície — mas a relação não é proporcional, e é por isso que aquário alto e estreito perde menos que aquário baixo e comprido de mesmo volume.

O que está fora da regra de bolso e é decisivo é a diferença de temperatura. Compare dois casos reais:

- **Aquário de 100 L em Belém.** Alvo de 26 °C, mínima do quarto na madrugada mais fria: 23 °C. Diferença: 3 °C.
- **Aquário de 100 L em Curitiba.** Alvo de 26 °C, mínima do quarto numa noite de julho: 11 °C. Diferença: 15 °C.

São **cinco vezes** mais diferença de temperatura para vencer no segundo caso. O "1 W por litro" responde 100 W para os dois.

No primeiro caso, 100 W é folga confortável. No segundo, é um aquecedor que vai passar a madrugada inteira ligado e ainda assim pode não segurar. E a consequência não é simétrica: aquecedor sobrando com um termostato que funcione apenas liga menos vezes; aquecedor faltando é a temperatura caindo com peixe dentro.

**É por isso que a regra erra sempre para o mesmo lado.** Ela foi calibrada num clima que não é o do Brasil inteiro.

## O que as fontes brasileiras dizem, e o que elas não dizem

Nosso levantamento de setembro de 2026 encontrou quatro afirmações circulando:

| Constante | Valor | Condição declarada pelo autor | Fonte |
| --- | --- | --- | --- |
| `wl-delta-ate-10` | 1,0 a 1,5 W/L | até 10 °C de diferença | ReefFlow |
| `wl-sul` | até 2,0 W/L | região Sul | Casa da Ada |
| `wl-generico` | 1,0 W/L | nenhuma | sem autoria única |
| `wl-ehow` | 1,3 W/L | nenhuma | eHow |

Duas coisas saltam.

A primeira: **uma única fonte, a ReefFlow, amarra o número a uma diferença de temperatura**. É a única do corpus que responde à pergunta certa, e o que ela diz é que a faixa de 1,0 a 1,5 W/L vale para até 10 °C. Acima disso ela não afirma nada. Nós também não: esticar o número dela para 15 °C seria inventar uma constante e pendurar o nome de outra pessoa nela.

A segunda: **a Casa da Ada reconhece que o Brasil tem mais de um clima** e sobe para 2,0 W/L no Sul. É a fonte mais próxima do raciocínio certo — mas ela troca "quanto frio faz aí" por "em que estado você mora", que é uma aproximação grossa. Aquário em quarto interno de apartamento em Porto Alegre pode esfriar menos que aquário em varanda envidraçada em São Paulo.

E as duas genéricas discordam entre si em 30 %, para a mesma pergunta, sem nenhuma condição que explique a diferença. Essa discordância não é ruído: é a prova de que ninguém está calculando nada.

## O que ainda não conseguimos publicar

A resposta honesta para "quantos watts" não é uma regra de bolso melhor. É a conta:

```
P = U · A · ΔT
```

Potência igual ao coeficiente global de troca térmica, vezes a área que troca calor com o ambiente, vezes a diferença de temperatura. Essa fórmula sabe distinguir aquário alto de aquário baixo, vidro de 6 mm de vidro de 10 mm, tampado de aberto. É o que a Aquametria quer publicar.

Falta uma peça, e é uma peça difícil: o `U` do aquário. Não o `U` tabelado de janela de vidro, que é o que se acha fácil em catálogo de vidraçaria — aquele descreve ar de um lado e ar do outro. No aquário há água de um lado, ar do outro, convecção natural nas duas faces, e a lâmina livre por cima, onde a **evaporação** costuma responder pela maior parte da perda. Sem fonte para isso, a via física não sai, e a nossa constante `u-vidro-aquario` continua marcada como pendente.

Enquanto ela não sai, a calculadora faz a coisa intermediária e honesta: usa as regras de bolso que existem, **mas só as que se aplicam ao seu caso**, cada uma com o nome de quem a publicou, e diz na cara quando nenhuma delas cobre você.

## O que fazer com isso na prática

Se você quer o número, [a calculadora faz a conta](https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/) e ainda filtra os aquecedores pela voltagem da sua tomada e pela temperatura que o termostato alcança. Se você quer só o resumo do raciocínio:

1. **Meça o frio, não a cidade.** Deixe um termômetro no cômodo onde o aquário fica e olhe de manhã, na semana mais fria. Esse número vale mais que qualquer normal climatológica.
2. **Calcule sobre a água real**, não sobre o rótulo do aquário. Vidro, borda livre e rochas tiram uma parte — a [calculadora de litragem](https://aquametria.com.br/calculadora-de-litragem/) devolve esse número.
3. **Na dúvida entre dois degraus, suba.** As consequências não são simétricas: sobrando, o termostato liga menos; faltando, a temperatura cai.
4. **Acima de 150 W, considere dois aquecedores de metade da potência.** O argumento é modo de falha, não economia — travado ligado, um aparelho menor faz menos estrago; travado desligado, o outro segura alguma coisa. Isso é raciocínio nosso, não regra publicada por ninguém, e está declarado como tal.
5. **Confira a voltagem antes de comprar.** A mesma potência é vendida em 110 V e em 220 V, e o anúncio nem sempre deixa claro qual. Aquecedor na voltagem errada queima ou esquenta demais.
6. **Tenha um termômetro independente do aquecedor.** O botão do aparelho é uma indicação, não uma medição — e a precisão declarada, quando existe, é de meio grau nos modelos bons.

## O que conversa com este texto

- **[Calculadora de potência do aquecedor (C5)](https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/)** — o número do seu caso, com a faixa atribuída fonte por fonte e os aquecedores que atendem.
- **[Calculadora de litragem (C1)](https://aquametria.com.br/calculadora-de-litragem/)** — o volume real de água, que é sobre o que se dimensiona.
- **[Vazão do filtro (C3)](https://aquametria.com.br/calculadora-de-vazao-do-filtro/)** — a mesma história, no outro equipamento: fabricante e web brasileira divergindo em até 5,7 vezes.
- **[Como a Aquametria calcula](https://aquametria.com.br/metodologia/)** — a escada de fontes e a diferença entre constante com origem e convenção declarada.
