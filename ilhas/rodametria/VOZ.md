# VOZ — Rodametria

Este arquivo manda no tom de toda página desta ilha. Número, fonte e data continuam obrigatórios, mas moram na camada de prova, nunca na voz (seção 15 do `ARQUIPELAGO.md`).

## Quem entra aqui
Quem decidiu largar o ônibus, o carro ou a moto a gasolina no trajeto curto e está com três anúncios abertos sem saber qual serve. É o entregador que quer rodar o dia inteiro sem recarregar; quem mora a 8 km do trabalho e não quer tirar CNH; o pai que vai dar um patinete para o filho de 17 anos; quem pesa 110 kg e desconfia que o patinete de 100 kg não aguenta. Chega por "moto elétrica", "scooter elétrica 1000w", "bicicleta elétrica precisa de cnh", "patinete elétrico adulto", "autonomia patinete elétrico".

## O momento
Aba do marketplace aberta, anúncio prometendo "sem CNH, 60 km de autonomia", preço de um salário e meio. A pessoa quer saber três coisas e nenhum anúncio responde direito: **precisa ou não precisa de CNH e placa**, **quantos km faz de verdade com o peso dela** e **se aguenta**.

## Quem fala
Quem roda e mexe com elétrico há anos: já abriu bateria inchada, já viu anúncio chamar de "1000 W" o pico do motor, sabe a diferença entre autonomia declarada e a de quem pesa 90 kg numa cidade com ladeira. Não é vendedor e não é despachante. Fala na segunda pessoa ("o seu trajeto", "a sua bateria"), diz o número que a pessoa precisa ouvir mesmo quando ele desanima, e cita a regra pelo nome quando o assunto é trânsito.

## Como a gente fala
Veredito na primeira linha, na língua de quem pilota: watt, km/h, volt, amper-hora, Wh, km, kg, aro, "precisa de placa", "faz uns X km", "aguenta", "não aguenta", "no limite". *(A expressão `"dispensa CNH"` estava nesta lista desde 27/10 e **saiu em 06/11/2026**, pelo mesmo motivo escrito na seção "Com a nossa cara": a resolução que esta ilha lê não fala de habilitação, e o portão de afirmação de tela reprova a frase. O vocabulário da PESSOA continua sendo `CNH` — ela digita isso, e a página responde nomeando o que falta para responder.)* As palavras que a pessoa digita: moto elétrica, scooter, patinete, bike elétrica, autopropelido, CNH, placa, autonomia, bateria, carregador.
Nunca no título nem no primeiro parágrafo: "regulamentação vigente", "consulte um especialista", "conforme a legislação aplicável", "consulta paramétrica", "procedência". A Resolução Contran nº 996/2023, a ficha do fabricante e a data de leitura ficam na tabela e no bloco "como sabemos", no fim da página.

## Com a nossa cara

> **CORRIGIDO EM 06/11/2026 às 19h3xZ, E A CORREÇÃO É DE FONTE E NÃO DE TOM.** Os exemplos aprovados em 27/10
> eram de antes de alguém ler a Resolução Contran nº 996/2023 no texto oficial — o que aconteceu em 05/11, no
> Chrome do Raphael. **A resolução não tem artigo nenhum sobre CNH:** ela decide a categoria, a placa, o
> registro, o licenciamento e o capacete. Quem decide habilitação é o Código de Trânsito, que esta fábrica
> ainda não leu na fonte. Então as frases `dispensa CNH e placa` e `aí precisa de habilitação` **não podem ser
> exemplo de nada**: elas afirmam o que a fonte não diz, que é a única coisa que o "Específico desta ilha" do
> `PROMPT.md` chama de risco de mandar alguém para a rua sem habilitação. O portão
> `ferramentas/teste-afirmacao-de-tela.py` as **reprova** desde 06/11, e as páginas no ar não as servem — **só
> este arquivo ainda as servia, e ele é o que a próxima execução lê para escrever o tom.** O mesmo vale para o
> `costuma` do quarto exemplo, que é a classe do quantificador por extenso que esta ilha paga desde 03/11: a
> página já serve a contagem no lugar da hesitação. Os quatro exemplos abaixo são os de hoje, e o original
> fica preservado no fim desta seção.

- "Até 1.000 W e 32 km/h é autopropelido, e a resolução diz que ele não é sujeito a registro, licenciamento nem emplacamento. Esse aqui anuncia 2.000 W — é ciclomotor, e aí a resolução manda registrar e licenciar. Sobre habilitação esta página não responde: quem decide isso é o Código de Trânsito, e a gente ainda não o leu na fonte oficial."
- "60 V × 20 Ah são 1.200 Wh. Com 90 kg e um pouco de subida, conte com 35 a 40 km, não os 60 do anúncio."
- "O patinete aguenta 100 kg. Você e a mochila dão 108. Não é para arriscar: olhe os de 120 kg logo abaixo."
- "O número grande do anúncio não é o que a regra lê: ela lê a potência NOMINAL, que fica na ficha. Dos {colhidos} anúncios que a gente colheu, {sem_rotulo} declaram um watt sem dizer se é nominal ou de pico, e NENHUM declara o nominal." — **este exemplo está com as chaves de propósito.** É o molde que a página serve, e os três números dele são CONTADOS do banco pelo gerador, nunca digitados. A primeira versão desta linha, escrita minutos antes nesta mesma passada, trazia os números à mão e **errou um dos dois** (disse 14 onde o banco conta 13) — o defeito que este arquivo acabara de corrigir em outra frase, cometido ao corrigi-la. Exemplo de tom não carrega número de banco.

### Os quatro exemplos de 27/10/2026, preservados

Eles ficam aqui porque **a diferença entre eles e os de cima é a leitura da fonte**, e quem for escrever tom
nesta ilha precisa ver as duas versões lado a lado. O primeiro e o quarto são os que mudaram:

- ~~"Até 1.000 W e 32 km/h é autopropelido: **dispensa CNH e placa**. Esse aqui anuncia 2.000 W — é ciclomotor, e aí **precisa de habilitação** e emplacamento."~~
- ~~"O número grande no anúncio **às vezes** é o pico do motor. O que conta para a regra é a potência nominal — e ela **costuma** estar na ficha, não no título."~~

## Proibidas
- "Consulte sempre a legislação vigente e um profissional habilitado."
- "Recomendação com procedência verificável e data de leitura."
- "Pode andar à vontade, ninguém fiscaliza" — e qualquer frase que afirme o que a resolução não diz.
- Prometer "a melhor moto elétrica" ou "a scooter certa" em título: vocabulário das fazendas.
- Contagem regressiva, "mais vendido", selo de avaliação que a ilha não mediu, e qualquer comparação de comissão entre lojas (seção 7).

## Home
A ferramenta principal em cima, sem introdução: **"Esse elétrico precisa de CNH?"** com os campos de potência (W), velocidade máxima e "tem acelerador?", e o botão. O resultado abre no mesmo lugar, com o veredito na primeira linha e o bloco de compra logo abaixo — os modelos que cabem na categoria. As outras ferramentas entram como cartões com a pergunta na linguagem da pessoa ("Quantos km ele faz no seu relevo?", "Aguenta você e a mochila?") — a primeira dizia "com o seu peso" até 30/10/2026, e **mudou pelo item 2 do despacho da ronda daquele dia**: a F2 não faz conta com o peso de quem pilota (a constante de consumo por quilo está `pendente` e pela seção 10 não pode entrar em fórmula), e prometer o peso ali era prometer o que a ferramenta não entrega. O relevo entra de verdade. **O peso continua na terceira pergunta**, que é a F3, onde ele é carga máxima e é comparado contra a ficha de cada veículo. Guias embaixo. **Sem manifesto, sem "bem-vindo", sem parágrafo explicando o que é o site.**

## Molde de casca: FERRAMENTA
Header claro, logo à esquerda, menu curto (Ferramentas · Veículos · Peças · Guias). A ferramenta é a home. Resultado sempre acima da dobra; **bloco de compra com link de afiliado antes da prova de procedência**; explicação, tabela pré-renderizada e "como sabemos" depois. O verde `#0A6B4C` aparece uma vez por tela — no veredito ou no botão, nunca nos dois; o âmbar `#8F4A00` só no aviso de "precisa de CNH" ou "não aguenta". Todo número e toda unidade saem em monoespaçada.
