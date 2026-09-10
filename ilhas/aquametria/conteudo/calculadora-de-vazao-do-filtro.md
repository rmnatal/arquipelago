---
id: calculadora-de-vazao-do-filtro
tipo: pagina
titulo: "Calculadora de vazão do filtro: quantos L/h o seu aquário pede"
slug: calculadora-de-vazao-do-filtro
meta_descricao: "Qual a vazão de filtro para o seu aquário, em L/h? A faixa vai de 1,76 a 10 renovações por hora, e cada extremo aparece com a fonte dele."
cluster: C3
calculadora: c3-vazao-filtro
fontes:
  - "eheim-classic-250-2213: 440 L/h declarados para até 250 L, ou 1,76 renovações por hora (dados/constantes-calculadoras.json, status fabricante-via-busca)"
  - "turnover-comunitario-br, 5 a 10 x/h — Aquarismo Paulista e AquaOnline (status divergente-fontes-br)"
  - "turnover-comunitario-mybest, 4 a 5 x/h — my-best BR (status divergente-fontes-br)"
  - "turnover-plantado, 3 a 5 x/h — AquaPeixes (status divergente-fontes-br)"
  - "sump-proporcao-minima, 20 % do volume — AquaOnline (status divergente-fontes-br)"
  - "fator de perda de carga e turnover marinho: PENDENTES, recusados em fórmula"
  - "fichas dos filtros sugeridos: dados/produtos-filtro.json, fonte e data por campo"
verificado_em: 2026-09-08
publicar: true
---

Pergunte na internet brasileira qual filtro serve para um aquário de 100 litros e a resposta virá pronta: "de 5 a 10 vezes o volume por hora", ou seja, de 500 a 1000 L/h. Vá agora ao site da Eheim e olhe o classic 250, o velho 2213: **440 litros por hora, declarados pelo fabricante para aquários de até 250 litros**. São 1,76 renovações por hora.

Uma das duas afirmações está muito errada, ou as duas medem coisas diferentes. Nenhuma fonte brasileira do nosso levantamento confronta as duas — todas repetem uma delas como se a outra não existisse. Esta calculadora existe para publicar a divergência inteira, com a atribuição de cada extremo.

[aquametria_calculadora_vazao]

## Por que a resposta é uma faixa larga, e não um número

O piso da faixa é o dimensionamento de quem fabrica o filtro. O teto é a regra de bolso que circula no aquarismo brasileiro. Entre um e outro há uma diferença de até 5,7 vezes, e cada lado tem um argumento que se sustenta:

**O fabricante mede o próprio equipamento.** A vazão declarada sai de bancada, com a bomba nova, sem mídia dentro do cesto e com a saída na altura da água. O volume atendido que ele publica pressupõe o filtro montado como o manual manda, com a mídia que vem de fábrica, em um aquário de povoamento normal.

**A regra de bolso compensa o que o fabricante não controla.** No aquário real o cesto está cheio, a mídia está suja, a mangueira sobe até o móvel e há mais peixe do que o manual imaginou. Pedir mais vazão nominal é o jeito de comprar folga sem precisar medir nada.

O que nenhum dos dois lados publica é o tamanho dessa folga. Por isso a Aquametria não escolhe um lado: mostra os dois extremos com o nome de quem os defende, e diz que a decisão — mais folga ou menos — é sua.

## O que a calculadora não faz, e por quê

**Não aplica fator de perda de carga.** Seria fácil escrever "considere 30 % a menos com mídia" e a página ficaria mais confortável. Só que nenhuma fonte do nosso levantamento publica esse número, e o fabricante só declara a coluna máxima, que é outra coisa. Constante sem origem é proibida aqui, mesmo quando o palpite é razoável.

No lugar do fator, a página entrega uma medição que você mesmo faz. Com o filtro ligado, aponte a saída para um recipiente de volume conhecido e cronometre:

> vazão real (L/h) = volume do recipiente (L) ÷ tempo (h)
>
> 10 litros em 45 segundos = 10 ÷ 0,0125 = **800 L/h**

Esse número vale mais que qualquer catálogo, inclusive o nosso: é o seu filtro, com a sua mídia, no seu móvel, hoje. Repita depois de uma limpeza e você vê a perda com os próprios olhos.

**Não publica turnover para aquário marinho.** O levantamento não trouxe nenhuma fonte brasileira com esse número. Quem marca "tenho sump" recebe o volume mínimo do sump — 20 % do volume do aquário, repetido pela AquaOnline —, e nada além disso. Um perfil marinho no formulário sugeriria que temos a resposta.

## Coluna máxima: o campo que decide se o canister funciona no seu móvel

Canister fica embaixo do aquário e precisa empurrar a água para cima. Todo fabricante sério declara até que altura a bomba vence — o Eheim 2213 declara 1,5 m. Se o seu filtro fica no chão e a superfície da água está a 1,6 m, esse modelo está fora, por mais que a vazão feche a conta.

A calculadora aplica esse corte e diz qual modelo saiu por causa dele. Filtro hang-on não entra nessa conta: ele fica pendurado na borda do aquário e não tem coluna a vencer — o campo simplesmente não se aplica, e o banco registra isso em vez de deixar um número faltando.

## Os filtros que aparecem no resultado, e como eles foram escolhidos

O bloco de produto só aparece quando existe filtro no nosso banco cuja vazão declarada cai **dentro da faixa que o seu aquário pediu**. Se não existe, não aparece nada — resposta sem produto é melhor que produto que não atende o seu número.

Três regras que valem sempre:

1. **A ordem é técnica.** Os modelos são ordenados pela proximidade do meio da faixa calculada, e cada cartão mostra quantas renovações por hora aquele filtro entrega **no seu volume**, não no volume genérico do catálogo.
2. **Comissão não ordena nada.** Modelo sem link de loja aparece do mesmo jeito, na mesma ordem que a adequação técnica manda. Isso está escrito como regra no esquema do nosso banco de dados, não é promessa de página.
3. **A ficha vem do fabricante ou do varejo especializado, com data.** O anúncio da loja nunca é a fonte técnica. Cada cartão traz o endereço da fonte, a data em que foi conferida e o nível dela — "fabricante via busca" quer dizer que a página do fabricante não foi lida direto e que o dado precisa de reconferência no manual.

**O preço que aparece nos cartões não é preço de hoje: é a cotação que lemos naquele anúncio, com a data ao lado.** Preço de aquarismo muda toda semana, e um número cravado como atual numa página que fica meses no ar envelheceria em dias — por isso ele sai datado ou não sai. Trate o nosso valor como ordem de grandeza e confira no anúncio antes de comprar. Quando um botão for link de afiliado, ele está marcado como patrocinado e o aviso de comissão está no próprio bloco — os detalhes estão em [como a Aquametria ganha dinheiro](https://aquametria.com.br/divulgacao-de-afiliados/).

O banco hoje é pequeno de propósito: são poucos filtros com ficha completa, porque completar uma ficha exige achar fonte para cada campo. Ele cresce a cada coleta, e a lista da sua faixa cresce junto.

## De onde vem o volume que esta página usa

Do seu navegador, se você já usou a [calculadora de litragem](https://aquametria.com.br/calculadora-de-litragem/). É ela que transforma as medidas em centímetros nos três volumes que importam e guarda o volume real — sem conta, sem login, sem envio para servidor nenhum.

Vale insistir num ponto: o volume que dimensiona filtro é a **água que está lá dentro**, não o número da etiqueta. Um "aquário de 128 litros" costuma ter menos de 110 litros de água depois do vidro, da borda livre e das rochas. Usar o número da loja aqui infla a vazão pedida em mais de 15 %.

A calculadora de litragem ainda não desconta o substrato, e isso está declarado lá: o volume real sai superestimado. Para filtro, o erro é **seguro** — você acaba pedindo vazão de sobra, não de menos.

## Onde este resultado vai ser usado

A faixa de vazão e o perfil do aquário ficam guardados no navegador junto com o volume. As próximas calculadoras leem de lá:

- **Mídia filtrante (C12)** — quantos mililitros de mídia biológica o cesto precisa carregar, com as duas âncoras de fabricante que discordam entre si.
- **Consumo elétrico (C7)** — o filtro é o equipamento que fica ligado 24 horas por dia; é ele que aparece na conta de luz.

As duas entram no ar uma por vez, cada uma só quando a fonte de cada constante estiver conferida. A lista completa está em [todas as calculadoras](https://aquametria.com.br/calculadoras/), e o critério que aceita ou recusa cada número está em [como a Aquametria calcula](https://aquametria.com.br/metodologia/).

**Verificado em 08/09/2026.** Calculadora versão 1.0.0.
