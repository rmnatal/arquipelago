---
id: calculadora-de-midia-filtrante
tipo: pagina
titulo: "Quanta mídia biológica cabe no seu filtro?"
slug: calculadora-de-midia-filtrante
meta_descricao: "Quanta mídia filtrante o seu aquário pede, em mililitros? Quatro fabricantes declaram dosagens que variam dez vezes; aqui estão as quatro."
cluster: C12
calculadora: c12-midia-filtrante
fontes:
  - "seachem-matrix-dosagem, 1,25 e 2,64 mL/L — Seachem, página do Matrix (status fabricante-via-busca). Duas leituras da MESMA copy, que discordam por 2,1 vezes"
  - "jbl-micromec-dosagem, 5,00 mL/L — JBL, ficha do MicroMec: 650 g (= 1 L) para 200 L (status fabricante-via-busca), coletada em 08/09/2026"
  - "ocean-tech-bio-glass-dosagem, 12,50 mL/L — Ocean Tech, ficha do Bio Glass: 1 L para cada 80 L (status fabricante-via-busca), coletada em 08/09/2026. Única dosagem por litro publicada por marca brasileira"
  - "eheim-classic-250-2213, 3,0 L de mídia para até 250 L = 12,0 mL/L de mídia TOTAL — Eheim (status fabricante-via-busca)"
  - "seachem-tidal-55, 1,2 L de mídia para até 200 L = 6,0 mL/L de mídia TOTAL — Seachem (status fabricante-via-busca), coletado em 08/09/2026"
  - "carvao-ativado, 1 a 2 g/L e troca em 15 a 30 dias — Aquarismo Paulista (status divergente-fontes-br)"
  - "perlon-troca, semanal a quinzenal — Aquarismo Paulista (status divergente-fontes-br)"
  - "ceramica-regeneracao, substituição PARCIAL a cada 6 a 12 meses — Aquarismo Paulista (status divergente-fontes-br)"
  - "ordem-midias-canister, cerâmica → perlon → carvão → perlon → cerâmica → perlon — AquaPeixes (status divergente-fontes-br)"
  - "tpa-percentual e tpa-diferenca-termica — Escola de Aquário e Aquário Vivo (status divergente-fontes-br)"
  - "nitrato-limites, > 40 ppm urgente, ≤ 20 ppm sensíveis, 5 a 10 ppm plantado — corpus do Bloco 1 (status divergente-fontes-br)"
  - "proporção entre as camadas do cesto: NÃO PUBLICADA, sem fonte no corpus"
  - "densidade aparente do carvão ativado: PENDENTE, e é o que impede comparar a regra em gramas com a declaração em mililitros"
  - "fichas das mídias sugeridas: dados/produtos-midia.json, fonte e data por campo"
verificado_em: 2026-09-08
publicar: true
---

Num aquário de 100 litros, a mídia biológica que o seu filtro pede vai de **125 mililitros a 1,25 litro** — dez vezes de diferença, conforme a marca que você abrir. Não é erro de leitura: as dosagens que existem discordam nessa ordem de grandeza, e ninguém as coloca lado a lado.

Aqui elas ficam lado a lado, convertidas para os litros do seu aquário, com o teto do cesto do seu filtro junto — para você não comprar mídia que não cabe.

[aquametria_calculadora_midia]

## O que ela faz de diferente

Ela não escolhe um número. Ela mostra os quatro que existem, com o nome de quem publicou cada um, e calcula o que cada um significa nos litros do seu aquário.

| Quem declara | Dosagem declarada | Em 100 L de água |
|---|---|---|
| Seachem Matrix — leitura "250 mL para 200 L" | 1,25 mL/L | 125 mL |
| Seachem Matrix — leitura "1 L para 100 galões" | 2,64 mL/L | 264 mL |
| JBL MicroMec — "650 g para 200 L" | 5,00 mL/L | 500 mL |
| Ocean Tech Bio Glass — "1 L para cada 80 L" | 12,50 mL/L | 1.250 mL |

Verificado em 08/09/2026. As duas primeiras linhas são a **mesma comunicação do mesmo fabricante**, lida de duas formas: o Matrix declara "250 mL tratam 200 L" num lugar e "1 litro trata 100 galões" em outro, e os dois números não batem entre si por 2,1 vezes. As duas ficam publicadas porque quem discorda aqui é o fabricante consigo mesmo — nós não temos como desempatar, e fingir que temos seria pior.

Do primeiro ao último número da tabela vai um fator de dez. Não é imprecisão da conta: é a distância real entre o que quatro empresas afirmam sobre a mesma função técnica.

## A segunda família de números: quem vende filtro

Existe uma segunda declaração que ninguém cruza com a primeira. O fabricante de filtro publica duas coisas: quanto de mídia cabe no aparelho e para que aquário ele serve. Dividir uma pela outra dá **mídia por litro de água** — só que mídia total, com a mecânica e a química dentro.

| Filtro | Mídia declarada | Aquário declarado | Mídia total por litro |
|---|---|---|---|
| Seachem Tidal 55 | 1,2 L | até 200 L | 6,0 mL/L |
| Eheim classic 250 (2213) | 3,0 L | até 250 L | 12,0 mL/L |
| Atman AT-3338 | 1,6 L ou 4,8 L (ficha ambígua) | até 450 L | 3,6 a 10,7 mL/L |
| Atman AT-3338S | 3,5 L ou 10,5 L (ficha ambígua) | 150 a 400 L | 8,8 a 26,3 mL/L |

Verificado em 08/09/2026. Fontes por campo em `dados/produtos-filtro.json`.

Essas duas famílias de números respondem perguntas diferentes e por isso não se comparam de igual para igual — mas elas se cruzam num ponto que decide a compra, e é aí que a calculadora chega.

## O número que ninguém publica: cabe no seu filtro?

A dosagem só vale se a mídia couber. É uma conta trivial — dosagem vezes volume, dividido pelo volume útil do cesto — e não a encontramos publicada em lugar nenhum, em português.

Escolha o seu filtro na calculadora e ela mostra, para cada dosagem declarada, quanto do cesto a camada biológica ocuparia. Num Eheim classic 250 com um aquário de 110 litros, a dosagem da Seachem ocupa 5 % do cesto e a da Ocean Tech ocupa 46 %. Nos dois casos cabe, e sobra espaço para a mecânica e a química. Já um aquário de 600 litros num Tidal 55 estoura o cesto na segunda dosagem em diante: nesse caso o problema não é a mídia, é o filtro — e comprar mais mídia não resolve.

## As fichas ambíguas do Atman, publicadas como ambíguas

Duas linhas da tabela acima trazem dois números. O motivo é honesto e vale explicar.

A ficha que o varejo brasileiro replica do Atman AT-3338 diz: "3 cestos para mídia filtrante com dimensões de 17x17x6 e capacidade de 1,6 litros de mídia". Essa frase pode significar 1,6 L **em cada cesto** (4,8 L no total) ou 1,6 L **no conjunto**. A geometria declarada apoia a leitura por cesto — 17 × 17 × 6 cm dá 1,73 L brutos, e 1,6 L úteis cabem ali dentro — mas apoiar não é declarar, e não achamos ficha de fabricante que resolvesse.

No modelo irmão, a mesma frase puxa para o outro lado: o AT-3338S declara cestos de 21 × 21 × 7 cm com "capacidade de 3,5 litros". Um cesto dessas medidas tem 3,09 L brutos e **não comporta** 3,5 L — ou seja, aqui só a leitura do conjunto é coerente com as dimensões que o próprio anúncio publica.

A mesma frase, dois modelos, duas leituras opostas. Publicamos as duas, com a razão de cada uma, e deixamos a decisão com quem tem o filtro na mão e pode medir o cesto.

## O que esta calculadora se recusa a fazer

**Não reparte o cesto em porcentagens.** Quanto do volume é mecânica, quanto é biológica e quanto é química é a pergunta seguinte, e nenhuma fonte do nosso corpus a responde. Chutar "50 % biológica" seria inventar exatamente o tipo de número que este site existe para não publicar. Publicamos a ordem das camadas, que tem fonte, e o teto físico, que é do fabricante do filtro.

**Não converte grama em mililitro.** A regra brasileira mede carvão ativado em gramas por litro de água — 1 a 2 g/L, trocado a cada 15 a 30 dias. O fabricante do carvão mede em mililitros de mídia por litro de água: a Seachem declara 250 mL de MatrixCarbon para 400 L, durando "vários meses". Para dizer qual das duas pede mais carvão seria preciso a densidade aparente do carvão ativado, e não temos essa constante com fonte. As duas saem lado a lado, cada uma na sua unidade. A distância entre elas é grande e está na tela — o que não está na tela é um número nosso fingindo resolver.

**Não compara área de superfície entre marcas.** A JBL declara 1.500 m² por litro para o MicroMec. A Ocean Tech declara 1.500 m² por litro para o Bio Glass. A Seachem declara mais de 700 m²/L para o Matrix, e a Eheim, 450 m²/L para o Substrat pro. Nenhuma das quatro publica o método de medição. Números medidos por métodos desconhecidos e possivelmente diferentes não formam um ranking, e nós não montamos um.

**Não estima quando a mídia biológica "vence".** A colônia de bactérias não tem prazo de validade; o que envelhece é a porosidade entupida, e ninguém no corpus mede isso. Publicamos a substituição **parcial** de 6 a 12 meses, que tem fonte, e explicamos por que ela é parcial.

**Não dimensiona mídia cujo fabricante não declara dosagem.** O Eheim Substrat pro aparece na lista com a ficha completa e sem número de compra, dizendo isso com todas as letras. O silêncio dele é parte do assunto.

## O aviso que vale mais que qualquer número desta página

Nunca lave toda a mídia biológica de uma vez, e nunca em água de torneira.

O que faz a filtragem biológica funcionar não é a pedra: é a colônia de bactérias nitrificantes que mora nos poros dela, e que leva semanas para se estabelecer. A água tratada da rede leva cloro ou cloramina justamente para matar bactéria — é para isso que ela existe. Lavar a mídia inteira na torneira mata a colônia de uma vez, e o aquário volta ao começo do ciclo, com pico de amônia e de nitrito na água onde os peixes estão vivendo.

É por isso que a substituição da cerâmica é parcial: troca-se uma parte, e a colônia da parte que ficou recoloniza a nova. Para tirar a sujeira grossa, use a água que saiu do próprio aquário na troca parcial — já não tem cloro e está na mesma temperatura.

## De onde vieram os números

Todas as dosagens desta página vêm da comunicação dos fabricantes, colhida em 07 e 08 de setembro de 2026. Duas ressalvas de procedência, que ficam registradas na própria tela:

O servidor onde este site é mantido não alcança `seachem.com`, `jbl.de` nem as lojas brasileiras diretamente — os números foram colhidos por resultado de busca e reconfirmados em varejo especializado que replica a mesma ficha. Estão marcados como **fabricante via busca**, e não como leitura direta da página do fabricante. Confira na embalagem antes de comprar.

E as constantes de manutenção — carvão, perlon, cerâmica, ordem das camadas, troca parcial de água, nitrato — vêm do corpus brasileiro do nosso levantamento, com o nome de cada publicação ao lado. São fontes que discordam entre si, e a tela mostra a discordância em vez de escondê-la atrás de uma média.

## Continue por aqui

- [Quanta mídia biológica o aquário realmente precisa](https://aquametria.com.br/2026/09/08/quanta-midia-biologica-o-aquario-precisa/) — o artigo que destrincha por que os quatro fabricantes discordam por dez vezes, e o que muda quando se segue cada um.
- [Quantos litros tem o seu aquário](https://aquametria.com.br/calculadora-de-litragem/) — o volume real de água, que é a entrada de tudo aqui.
- [Qual filtro dá conta do seu aquário](https://aquametria.com.br/calculadora-de-vazao-do-filtro/) — a água precisa passar, e precisa passar por alguma coisa: vazão e mídia são as duas metades da mesma decisão.
- [Quantos watts de aquecedor você precisa](https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/) — a colônia nitrificante também depende de temperatura.
- [Como a Aquametria calcula](https://aquametria.com.br/metodologia/) — por que uma faixa com fontes que discordam vale mais que um número redondo sem origem.
- [Como a Aquametria ganha dinheiro](https://aquametria.com.br/divulgacao-de-afiliados/) — o que é link de afiliado e o que ele não muda.
