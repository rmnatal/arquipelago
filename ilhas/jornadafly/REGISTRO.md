# Registro de execuções — JornadaFly

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-09-15 11h25Z — Coliseu e Torre Eiffel entram, a pergunta da moeda é respondida com uma regra, e `existe_hoje` deixa de ser prosa

**O que saiu:** o **Coliseu de Roma** e a **Torre Eiffel** entram no banco, com Roma e
Paris como terceira e quarta cidades. O banco foi de 2 para 4 experiências, de 5 para
11 versões, de 2 para 4 cidades e de 5 para 7 fontes; esquema e banco passam à versão 3.
Nasceram no esquema a `regra_de_crescimento_de_vocabulario` e o valor
`concessionaria_de_bem_publico`, e `existe_hoje` da escada virou campo **derivado**, com
régua. **Nada foi ao ar: esta ilha não tem site, Sync nem `/status`, e dizer que
verifiquei no ar seria inventar.**

**A ESCOLHA DA ILHA: SEGUNDA TENTADA, uma perdida na corrida do push.** Os cinco
`ESTADO.md` do `main` real parseiam em `yaml.safe_load` e os cinco estavam com
`executando_desde: null`, que pela 1.1 já significa que nenhum bloco da Fundação está
vivo — não houve reserva vencida para o git desempatar. Pela **18.1** li o topo dos
cinco `PROMPT.md` antes da rotação e **nenhuma ilha tem despacho com item acionável pela
Fundação**: o da robometria tem os itens 1, 2 e 3 **cumpridos**, o 4 dependendo da sessão
logada da Shopee (25.6) e o 5 sendo achado de método endereçado ao Raphael; os da
ohmetria e da jornadafly são de **nascimento**, que carregam a fila inteira e não cabem
na 18.2; os da aquametria e da clubedomosaico estão fechados. Os despachos de
`dados/despachos.md` que estão abertos são todos para o **Raphael**, não para a Fundação.
Sobrou a rotação da seção 1: pedi a **ohmetria**, a mais antiga (21h20Z), e o push foi
**RECUSADO** — duas outras execuções tinham reservado a aquametria às 11h16Z e a
ohmetria às 11h17Z. Voltei ao passo 2 sem force push. Sobraram três, com **jornadafly e
robometria empatadas em 23h35Z** e as duas de prioridade 1; o desempate alfabético da
seção 1 dá a jornadafly. Reserva aceita às **11h25Z**. Nenhum PR aberto, e as branches
`claude/*` do repositório ou já estão mescladas no `main` ou são anteriores a uma
reescrita de história dele — nenhuma carrega trabalho a mesclar.

**REDE PELA 20.2, RETESTADA E NÃO HERDADA:** três passadas, `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas três, com `aquametria.com.br` e `robometria.com.br`
em `200` nas mesmas três. Seis medições de bloqueio contra seis de controle verde, igual
às três execuções anteriores. Segue bloqueada, e `bloqueada_por` segue `null` de
propósito: o que a rede trava é o 3b em diante, não o bloco de arquivo.

### A pergunta da moeda tinha duas saídas postas, e a resposta não era nenhuma das duas

A carga de 14/09 fechou mandando quem gravasse a próxima cidade decidir primeiro: **ou o
vocabulário de `moeda` cresce com as moedas que os operadores realmente cobram, ou o
banco fica restrito a três moedas e a ilha diz por quê.** As duas saídas tratam o
vocabulário como uma lista a dimensionar. Ele não é: é uma promessa.

Nasceu a **`regra_de_crescimento_de_vocabulario`**: valor de vocabulário controlado
nasce **junto com o primeiro registro que o usa**, nunca antes dele. Então JOD, AED, ARS
e VND **não entram hoje**, e o motivo fica escrito — nenhum registro do banco cobra
nelas. Entram no commit de Petra, Dubai, Buenos Aires ou Ha Long. É a cicatriz que a
ohmetria pagou em 14/09: vocabulário sem lastro faz o gerador oferecer um valor que
nenhum registro sustenta, e toda frase de inexistência da tela fica sem como ser
conferida.

**E a regra foi exercida no mesmo commit, por outro vocabulário.** `tipo_de_operador`
ganhou `concessionaria_de_bem_publico` porque a Torre Eiffel precisa dele: a SETE opera o
monumento **sob concessão da cidade de Paris**, e não é o poder público declarando tarifa
nem uma empresa privada qualquer. Chamar de um dos dois seria pôr o número na boca de
quem não o publicou. O valor nasce com o registro que o carrega, que é a regra se
cumprindo na mesma passada em que foi escrita.

### O Coliseu é o primeiro registro publicável por PÁGINA DE TARIFA, e não por ato

A `regra_do_documento_nomeado` nasceu em 14/09 dizendo que se sai dela "nomeando o
documento — o ato, a **tabela** ou a **página de tarifa** da própria autoridade". Até
hoje **só o ato tinha sido exercido**, pela gôndola e a sua Delibera 89/2023; o Angkor
não saiu porque a autoridade dele só devolveu uma página de perguntas frequentes, e por
isso segue `pendente_de_releitura`.

O Coliseu sai pelo terceiro caminho. A passada em inglês devolveu, por endereço, a
página de horários e bilhetes do próprio órgão (`colosseo.it/en/opening-times-and-tickets/`)
e a página de categorias de bilhete do sistema oficial de venda
(`ticketing.colosseo.it/en/categorie/singoli-1-8-persone/`), e a passada em português já
tinha devolvido `ticketing.colosseo.it` por nome como o canal oficial. **Duas versões,
convergentes nas duas passadas:** €18 no ingresso comum de 24 horas, que inclui Coliseu
nos níveis 1 e 2 mais uma entrada no Fórum Romano e no Palatino, e €22 na Experiência
Completa, que acrescenta uma área restrita. `url` continua `null` nas duas fontes desta
carga, e o motivo é o de sempre: **endereço visto em resultado de busca não é página
lida** — `colosseo.it`, `www.coopculture.it`, `www.toureiffel.paris` e `civitatis.com`
deram `000` às 11h31Z, com o proxy declarando CONNECT recusado por política. É isso que
mantém a fonte no nível 3 e não no 1.

### A Torre Eiffel é o primeiro registro de NÍVEL 4 deste banco

O degrau do **operador lido por busca** estava marcado no esquema como `existe_hoje:
false`. Ele passou a existir, e a diferença não é de grau: o que a busca devolveu não é
alguém falando da tarifa, são **as páginas de tarifa do próprio operador, uma por
bilhete, com o preço no título de cada uma** — 14,80€ pela escada até o segundo piso,
23,50€ pelo elevador até o segundo, 28,00€ no combinado escada mais elevador até o topo e
36,70€ pelo elevador até o topo. A segunda passada, em inglês, devolveu a grade inteira
por faixa etária e bate nas pontas com a primeira (3,80€ e 18,40€ para criança e jovem).

**Quatro versões, e nenhuma delas é escada de dias** — é escada de *acesso*, que o banco
não tinha. E a fonte declara a duração pelo avesso: "o seu ingresso só tem horário para
entrar, a saída é livre". Gravar minutos ali inventaria um limite que o operador diz não
ter, e é o contrário do Coliseu, que declara validade de 24 horas. **Das duas formas quem
declara é a fonte**, e é por isso que `duracao_minutos` é `null` nas seis versões desta
carga, cada uma com o seu motivo escrito.

### O achado de modelo, e os dois registros são a prova

**`faixa_etaria` é da VERSÃO e o esquema a põe na EXPERIÊNCIA.** Na Torre Eiffel a
criança de 4 a 11 anos paga **3,80€ pela escada e 9,20€ pelo elevador até o topo** — a
mesma faixa, quatro preços; o jovem de 12 a 24 vai de 7,40€ a 18,40€ pelo mesmo caminho.
`faixa_etaria` guarda **um** preço por faixa, então gravar essas três publicaria o número
errado para três das quatro versões. Só a gratuidade dos menores de 4 anos, que vale
igual nos quatro bilhetes, cabe no campo como ele é hoje — e é só ela que está gravada.

**Não apareceu antes porque o mundo não se movia:** a gôndola não tem faixa etária e a do
Angkor vale igual nas três versões do passe. Campo que só erra quando o mundo se move
parece certo até o mundo se mover — a mesma forma que esta ilha já pagou no resumo e no
piso.

### A divergência mais cara que esta ilha já mediu, e ela ficou FORA de `declaracoes`

As duas passadas do Coliseu **discordam sobre quem não paga**, e discordam exatamente
onde o leitor brasileiro tem mais a perder:

| | Passada em português | Passada em inglês |
|---|---|---|
| gratuidade até 18 anos | só para cidadão de Estado-membro da UE | «free to citizens of **EU and non-EU** countries» |
| gratuidade universal | menores de 6 anos | menores de 18, de qualquer nacionalidade |
| reduzida de 18 a 25 (UE) | €4 | cerca de €2 |
| 18 a 25 de fora da UE | não diz | paga a tarifa cheia |

Nenhuma das duas é autoridade — as duas são **publicador editorial, nível 6** —, e a
regra de divergência **sem autoridade** desta ilha resolve para o valor **maior**, porque
o erro caro é subestimar. Resolvido pelo maior, **o adolescente brasileiro paga os €18 do
adulto**, e é isso que a página vai dizer: que a gratuidade está em disputa entre as
fontes, com o nome de quem publicou cada versão, e que a conta do grupo é feita pelo
cheio até a autoridade declarar.

**E ela não entrou em `declaracoes`, de propósito.** Declaração, neste esquema, discorda
de uma **VERSÃO** — e faixa etária não é versão. Gravar ali diria que essas fontes
discordam do preço do bilhete, e elas não discordam: os €18 e os €22 voltaram idênticos
nas duas passadas. É a mesma raiz do achado acima, e está nomeada no esquema em
`faixa_etaria_e_da_VERSAO_e_o_esquema_a_poe_na_EXPERIENCIA`.

### `existe_hoje` era a prosa mais silenciosa do esquema

Cada degrau da escada declara `existe_hoje`, e **nenhuma régua recomputava isso**. É a
família do número de tela digitado, na sua forma mais quieta: um `existe_hoje: false`
velho faz a ilha **negar um degrau que ela já alcançou**, e nada no banco contradiz a
frase. Esta carga é justamente a ocasião em que um campo desses envelhece — o nível 4
passou de `false` a `true`.

O validador passou a **derivar `existe_hoje` das fontes do banco** e a reprovar o gravado
que discordar, **nas duas direções**: degrau negado que o banco pisa, e degrau prometido
que nenhuma fonte pisa. E a régua nova achou uma interação **no mesmo dia em que
nasceu**: ela reprovou um MUNDO que passava havia uma carga — o `mundo_sem_divergencia`,
que apaga as declarações e, com elas, as fontes editoriais, e portanto tem de apagar o
degrau 6 junto. **Régua que só mede o banco real é régua com metade do mundo desligada**,
e foi o mundo produzido que mostrou isso.

### A bancada passou a cobrar a FRASE, e não só o veredito

Mutação ganhou um quinto elemento opcional: a frase que a quebra tem de ouvir de volta.
**Reprovar não é a mesma coisa que reprovar pelo motivo certo** — sem isso, uma mutação
pode disparar outra trava, voltar verde e nunca ter medido a sua, que é a forma de
mutação inerte mais difícil de ver, porque o relatório fica todo `ok`. É a régua que a
ohmetria escreveu em 14/09, trazida para cá.

### Verificação, 0 falha

- `python3 ferramentas/validar-banco.py` — verde sobre o banco real, com as duas réguas
  novas.
- `python3 ferramentas/mutacoes-banco.py` — **53 mutações** (eram 49): **6 mundos que têm
  de PASSAR** e **47 quebras que têm de REPROVAR**, todas decidindo certo nos dois lados
  da fronteira, **3 delas cobradas pela frase**.
- **Nenhuma mutação nova é inerte, e as duas foram provadas uma a uma.** Trocando a frase
  esperada de uma quebra por outra trava real, a bancada acusa e sai com código 1. E
  tirando do mundo do degrau novo o ajuste do esquema, ele **reprova** — ou seja, ele não
  passava de graça.
- **A régua pegou o que existe para pegar:** as cinco contagens do `resumo` ficaram para
  trás quando os dois registros entraram, e o validador reprovou as cinco antes do
  commit. Número que a ilha publica sobre si mesma nasce contado.
- Os três JSON passam por `json.load` e o cabeçalho do `ESTADO.md` por `yaml.safe_load`.
  Conferida também a acentuação nas duas direções: **zero** id, slug ou valor de
  vocabulário acentuado, e os nomes de tela acentuados.
- **`vocabulario_sem_lastro` passou a ser publicado a cada passada**, que é a outra
  metade da regra de crescimento: hoje **4 de 6** em `categoria`, **3 de 5** em
  `tipo_de_operador`, **2 de 4** em `unidade_de_preco`, **1 de 3** em `moeda` e **1 de 3**
  em `status_do_registro`; `momento_do_dia` é o único com lastro inteiro. É **aviso e não
  erro**, de propósito: os valores que o bloco 3 já trazia são anteriores à regra e não
  viram defeito retroativo. O que fica proibido enquanto a lista não for vazia é a ilha
  publicar **frase de inexistência**.

### Uma diferença que ninguém tinha medido, e ela é sobre o piso

Os resultados de hoje trazem o host da plataforma com `www.`
(`www.civitatis.com/br/roma/`), e o molde do esquema foi escrito no bloco 2 com o host
**sem** `www`, do jeito que ele foi visto lá. As duas formas apareceram em dias
diferentes e nenhuma das duas páginas foi aberta. O piso continua sendo **derivado do
molde**, e é assim que fica: piso derivado que envelhece junto é melhor que piso digitado
que envelhece calado. Está escrito na `nota_do_slug` das duas cidades novas.

### Achado de higiene, e ele não é desta carga

Os commits de **00h20Z, 00h32Z e 00h45Z de 15/09** fizeram o símbolo, a fonte da marca e
os quatro lockups desta ilha e **não fecharam a execução**: não há entrada neste
`REGISTRO.md`, o cabeçalho do `ESTADO.md` nunca foi tocado e nenhuma reserva foi escrita.
Os arquivos estão no `main` e o `DESIGN.md` os documenta — **o que falta é o rastro**.
Fica dito aqui para a próxima execução não procurar o registro que não existe, e para o
`ultima_execucao` de 23h35Z não ser lido como se nada tivesse acontecido depois dele.

### Aberto e nomeado

(a) a **rede** da ilha, despacho ALTO, que trava 3b em diante — remedida hoje, não
herdada; (b) o **câmbio**, no mesmo despacho, que custa uma linha e não trava bloco;
(c) a **seção pendente do `VOZ.md`** — as 10 a 15 legendas reais do @jornadafly, que o
`PROMPT.md` exige antes da primeira página; (d) a **identidade visual**, que precisa da
aprovação do Raphael antes do 3b (o símbolo e os lockups existem desde 15/09, e é a
aprovação que falta); (e) **nenhum programa de afiliado cadastrado**; (f) **não existe
`manifest.json`**, e criá-lo vazio seria inventar infraestrutura antes do WordPress.

### Próximo passo desbloqueado

**Mover `faixa_etaria` de EXPERIENCIA para VERSAO**, com a régua e as mutações junto, e
migrar os registros da gôndola e do Angkor na mesma passada. Esta carga mediu que o campo
está no lugar errado e deixou os dois registros novos pagando o preço disso: a Torre
Eiffel publica **uma** das quatro faixas que a fonte declara, e o Coliseu publica
**nenhuma**. É a mudança que destrava a divergência do Coliseu sair do motivo e virar
dado — e ela **não depende de site, de domínio nem da rede bloqueada**.

**A carga continua disponível pelo mesmo canal e pela mesma lista:** dos três nomes que a
carga de 14/09 deixou, **dois saíram hoje** e sobra **Petra**, que trai a moeda (JOD) e
agora tem regra dizendo o que fazer com isso — o valor nasce no commit do registro.

## 2026-09-14 23h18Z — A CARGA DO BANCO, e o achado é sobre o CANAL: a busca devolve faixa onde o preço é de operador e devolve número onde há tabela pública

**O que saiu:** o **Angkor Pass** entra no banco com as três versões da escada de dias
(1, 3 e 7 dias), preço por pessoa, faixa etária preenchida e cidade nova (Siem Reap).
Nasceu no esquema a **`regra_do_documento_nomeado`**, com régua e três mutações. O banco
foi de 1 para 2 experiências, de 2 para 5 versões, de 1 para 2 cidades e de 4 para 5
fontes. **Nada foi ao ar: esta ilha não tem site, Sync nem `/status`, e dizer que
verifiquei no ar seria inventar.**

**A ESCOLHA DA ILHA: SEGUNDA TENTADA, uma perdida na corrida do push.** Os cinco
`ESTADO.md` do `main` real parseiam em `yaml.safe_load` e os cinco estavam com
`executando_desde: null`, que pela 1.1 já significa que nenhum bloco da Fundação está
vivo — não houve reserva vencida para o git desempatar. Pela **18.1** li o topo dos
cinco `PROMPT.md` antes da rotação e **nenhuma ilha tem despacho corretivo com item
acionável em aberto**: o da robometria, da Sentinela de 14/09, tem os itens 1, 2 e 3
**CUMPRIDOS** e o item 4 dependendo da sessão logada do painel da Shopee, que é do
Raphael pela 25.6; os da ohmetria e da jornadafly são despachos de **nascimento**, que
carregam a fila inteira e por isso não cabem na 18.2; o da aquametria deixou aberto o
item 5, que diz de si mesmo que a ordem não muda, e o 6, suspenso pela seção 21. Sobrou
a rotação da seção 1. A **robometria** era a mais antiga (19h17Z) e meu push de reserva
foi **RECUSADO** — outra execução a reservou às 23h16Z, cerca de um minuto antes. Voltei
ao passo 2 sem force push, e a próxima da ordem era a jornadafly (19h31Z). Reserva
aceita às 23h18Z. Nenhum branch `claude/*` e nenhum PR aberto para mesclar.

**REDE PELA 20.2, RETESTADA E NÃO HERDADA:** três passadas, `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas três, com `aquametria.com.br` e `robometria.com.br`
em `200` nas mesmas três. Seis medições de bloqueio contra seis de controle verde, igual
às duas execuções anteriores. Segue bloqueada, e `bloqueada_por` segue `null` de
propósito: o que a rede trava é o 3b em diante, não o bloco de arquivo.

### O achado, e ele não estava na lista de coisas a procurar

O próximo passo escrito pelo bloco 3 era ler, na fonte de quem opera, as seis
experiências que o bloco 2 mediu. **Três foram tentadas e três recusaram entrar, pelo
mesmo motivo, e é o motivo que interessa.**

| Experiência | Passadas | O que voltou |
|---|---|---|
| Balão da Capadócia | 2 (pt e en) | US$ 150; "em média a partir de €190"; €90 a €160; €130 a €150; €130/€180/€300/€800; €150 a €450; €70; €60 a €250 |
| Cruzeiro de Ha Long | 2 (pt e en) | US$ 180 a 480 **por cabine**; US$ 90 **por pessoa**; "a partir de" US$ 292; e a segunda passada em **VND por pessoa** |
| Quadriciclo no deserto de Dubai | 1 | US$ 30 a 44; ≈ AED 110 a 160; US$ 85; R$ 300 a 800 |
| **Angkor Pass** | 2 (pt e en) | **US$ 37, US$ 62 e US$ 72** nas duas, atribuídos por nome ao vendedor oficial |

**A busca web devolve FAIXA onde o preço é de operador privado e devolve NÚMERO onde há
tabela pública.** Nenhuma das sete leituras de faixa tinha as três coisas que esta ilha
exige de um preço: dono, data e unidade. A de Ha Long é a mais dura, porque as duas
passadas **discordam da unidade e da moeda da mesma experiência** — que é, literalmente,
o defeito que a ilha existe para corrigir, aparecendo dentro do canal com que ela
pretendia se abastecer.

**A consequência não é sobre estas três experiências, é sobre o plano:** o critério de
entrada do esquema **prefere operador privado sem tabela pública**, e o único canal
aberto hoje serve exatamente o tipo que ele **não** prefere. Enquanto o egresso estiver
fechado, o banco só cresce pela exceção. Isso virou acréscimo ao despacho ALTO de rede
em `dados/despachos.md`, às 23h35Z: o que muda lá não é o pedido — é o que está em jogo,
que antes era "trava o 3b" e agora é "trava o 3b **e** a carga pelo tipo que sustenta a
tese da ilha".

**O canal foi remedido nesta execução, não herdado da prosa** (seção 4): `curl` devolveu
`000` em `visitpetra.jo`, `angkorenterprise.gov.kh`, `civitatis.com`,
`www.getyourguide.com.br`, `www.viator.com` e `api.bcb.gov.br`, e o **WebFetch** de
`www.angkorenterprise.gov.kh` devolveu `EGRESS_BLOCKED` às 23h30Z. As duas portas,
medidas hoje.

### A regra que nasceu, e ela é sobre o QUARTO elo

O Angkor entrou, e entrar levantou uma pergunta que o esquema não sabia responder.
A escada de fontes cobra o **elo mais fraco** entre autoria, custódia e leitura — e
tanto a tarifa da gôndola quanto a do Angkor são "autoridade lida por busca", nível 3,
o mesmo degrau. **Só que elas não valem o mesmo.** A da gôndola voltou com o ato que a
sustenta (Delibera 89 de 20/04/2023): o número tem endereço dentro da autoridade. A do
Angkor voltou duas vezes, em duas línguas, atribuída por nome ao vendedor oficial, e
**nenhuma das duas passadas trouxe ato, deliberação, tabela ou página de tarifa** — ela
tem procedência falada. O endereço da autoridade apareceu nos resultados
(`angkorenterprise.gov.kh/en` e `/en/faqs`) e **não foi lido**, porque o egresso recusou.

Nasceu no esquema a `regra_do_documento_nomeado`: **fonte de nível de autoridade que não
nomeia documento não deixa o registro `publicavel` — ele entra como
`pendente_de_releitura`.** O registro entra, e entra a reconferir. É o quarto elo, ao
lado de autoria, custódia e leitura.

A régua lê a regra **do esquema** e nunca de dentro de si (26.2), e a lista de níveis de
autoridade mora lá. Três mutações medem os dois lados: a que marca o Angkor como
`publicavel` reprova; **a que apaga o ato da gôndola reprova igual**, e é ela que prova
que a trava lê a escada e não um `id`; e a que apaga a chave do **esquema** reprova pela
mensagem do próprio esquema. E há um **mundo que tem de passar**: o mesmo registro com o
documento nomeado vira `publicavel` — sem ele a regra estaria só dizendo não, e o dia em
que a busca devolver a tabela de tarifa é esse mundo que vira o banco real.

### Duas decisões de dado que não são óbvias e ficam escritas

1. **A moeda de Siem Reap é `USD`, não a moeda do Camboja.** O campo `moeda_local`
   pergunta em que moeda o operador daquela cidade **cobra**, e o Angkor Pass é vendido
   em dólar. Gravar o riel seria descrever a bandeira e não o caixa.
2. **A unidade "por pessoa" foi DECLARADA pelo contraste, e a fonte nunca escreve "por
   pessoa".** Ela escreve que a criança sem passaporte paga **US$ 37 — o mesmo valor do
   adulto, por cabeça**. Preço que se cobra de cada criança é preço por pessoa, e quem
   classificou foi a ilha. É o exemplo mais limpo de `no_contraste_da_propria_fonte` que
   o banco tem, e a frase da tela terá de dizer quem classificou (26.3).

**E uma terceira, sobre a monetização:** este item **não tem página de produto em
plataforma nenhuma**, e a causa não é falta de coleta. O passe é vendido pela própria
Angkor Enterprise; o que a Civitatis vende em Siem Reap são passeios guiados — as duas
páginas vistas hoje, `/br/siem-reap/excursao-koh-ker/` e
`/br/siem-reap/tour-tres-dias-angkor/`, são **produto diferente do ingresso**. Apontar
uma delas como se fosse o passe seria vender uma coisa no lugar de outra, que é pior do
que não ter link. O **piso da 25.2 continua de pé** e é derivado da cidade:
`https://civitatis.com/br/siem-reap/`. Itens sem saída de compra: **0**. Piso não
rastreável: **2**, que é dívida de comissão e não defeito de página.

### A lista vazia que é uma afirmação, e ela é o contrário da gôndola

`declaracoes` do Angkor é **vazia**, e o registro diz o que isso significa: **não é que
ninguém mais publicou número — é que ninguém publicou número DIFERENTE.** Duas passadas,
duas línguas, publicadores brasileiros, portugueses e de língua inglesa, os mesmos três
valores. Declaração, pelo esquema, é número que **discorda** do resolvido; sem
discordância não há o que registrar, e por isso `resolucao` é `null` com o motivo
escrito — resolução sem divergência seria a ilha encenando uma dúvida que não mediu.
É o contraste que vale: a gôndola é tarifa igualmente tabelada e tem **quatro leituras
em três unidades**. Tabela pública não garante convergência; onde ela converge, converge
inteira.

### Verificação, 0 falha

- `python3 ferramentas/validar-banco.py` — verde sobre o banco real, com a régua nova.
- `python3 ferramentas/mutacoes-banco.py` — **49 mutações** (eram 45): **5 mundos que
  têm de PASSAR** e **44 quebras que têm de REPROVAR**, todas decidindo certo nos dois
  lados da fronteira. As três quebras novas foram lidas **uma a uma pela mensagem que
  devolvem**, não só pelo veredito: nenhuma é inerte, nenhuma reprova por outra trava.
- A régua pegou o que existe para pegar: as cinco contagens do `resumo` ficaram para
  trás quando o registro entrou, e o validador reprovou as cinco antes do commit.
  Número que a ilha publica sobre si mesma nasce contado.
- Os três JSON passam por `json.load`; o cabeçalho do `ESTADO.md` passa por
  `yaml.safe_load`.

### Próximo passo desbloqueado

**Continuar a carga pelo que o canal aberto alcança, e é uma lista curta e nomeada:**
ingresso de sítio público com bilheteria oficial — Petra, Coliseu, Torre Eiffel —, que
é o tipo que a medição de hoje mostrou ser o único reproduzível por busca. **Petra tem
uma trava a mais e ela é de esquema:** a Jordânia cobra em dinar, e `JOD` não está no
vocabulário de `moeda`, que hoje é `EUR`, `USD` e `BRL_do_operador`. O mesmo vale para
Dubai (AED), Buenos Aires (ARS) e Ha Long (VND). **Quem for gravar a próxima cidade
decide isso primeiro**, e a decisão mora no esquema, nunca dentro da régua: ou o
vocabulário cresce com as moedas que os operadores realmente cobram, ou o banco fica
restrito a três moedas e a ilha diz por quê. **Não depende de site, de domínio nem da
rede bloqueada.**

## 2026-09-14 19h19Z — Bloco 3: o modelo do banco, e uma régua que só podia errar num mundo que o banco não tem

**A ESCOLHA DA ILHA: SEGUNDA TENTADA, uma perdida na corrida do push.** Li os cinco
`ESTADO.md` do `main` real. A **ohmetria** já estava reservada às 19h16Z por outra
execução e saiu pelo passo 3 da seção 1. Pela **18.1**, sobrava **uma** ilha com
despacho aberto do Raphael — a jornadafly, com o "ESTA ILHA NASCE AGORA" de 14/09.
(A aquametria e a robometria tiveram o despacho do piso de busca **cumprido e
conferido no ar** mais cedo hoje; a clubedomosaico não tem despacho aberto, e o que
sobrou do dela está declarado no próprio despacho como bloco de malha.) Meu primeiro
push de reserva foi **recusado** — e não porque alguém tivesse pegado a jornadafly:
outra execução acabara de reservar a robometria e o `main` andou. Voltei ao passo 2
sem force push, confirmei `executando_desde: null` na jornadafly e a reserva foi
aceita às **19h19Z**. Nenhum branch `claude/*` e nenhum PR aberto para mesclar.

**REDE PELA 20.2, RETESTADA E NÃO HERDADA.** Três passadas: `jornadafly.com.br` e
`www.jornadafly.com.br` em **000** nas três, `aquametria.com.br` em **200** nas mesmas
três. Seis medições de bloqueio contra três de controle verde — é rede, não túnel. O
despacho ALTO para o Raphael segue aberto. O bloco 3 é arquivo no repositório: não
aciona Sync, não abre URL e não afirma nada sobre o ar.

### O que foi entregue

- **`dados/esquema-banco.json`** — o contrato. Entidades **CIDADE**, **EXPERIENCIA**,
  **VERSAO**, **DECLARACAO**, **FONTE** e **AFILIADO**, campo a campo, com escada de
  fontes de seis níveis, regra de divergência, vocabulários controlados, molde do piso
  de compra e a lista de `campos_que_exigem_declaracao_de_origem`.
- **`dados/experiencias.json`** — o banco, com **um** registro: o passeio de gôndola de
  Veneza, duas versões (diurno €90/30 min, noturno €110/35 min), quatro declarações
  divergentes e a resolução pela autoridade.
- **`ferramentas/validar-banco.py`** — a régua, 0 falha sobre o banco real.
- **`ferramentas/mutacoes-banco.py`** — **45 mutações**, todas decidindo certo.

### Por que o banco nasce com UM registro, e por que isso não é atraso

Duas frases do repositório pareciam brigar. O corpus do bloco 1 fecha dizendo *"o banco
começa vazio no bloco 3 e se enche por leitura na fonte de quem opera"*; a seção 5 da
especificação do bloco 2 manda o contrário para um caso: *"quem for escrever o bloco 3
lê a 2.2 e grava o número no banco, uma vez"*. **As duas falam de coisas diferentes e as
duas valem:** nenhum preço do **corpus** entra no banco, e a tarifa da gôndola — colhida
no bloco 2 **com o ato que a sustenta**, a *Delibera della Giunta Comunale n. 89 de
20/04/2023* — entra uma vez.

**Nenhuma coleta nova foi feita nesta execução.** Gravar Petra, Angkor, Ha Long, Dubai
ou Buenos Aires exigiria ler a fonte de quem opera com `data_leitura` própria, e isso é
bloco de **carga**, não de **modelo**. Escrever aqui os números que o bloco 2 anotou
como *leitura de SERP* seria transformar medição de desacordo em dado de produto — o
defeito que o `VOZ.md` desta ilha nomeia como o mais grave possível.

### O ACHADO, e ele é de régua: a divergência é sobre a VERSÃO, nunca sobre a EXPERIÊNCIA

A regra da ilha diz que, sem autoridade, a divergência resolve para o **maior** — o erro
caro é subestimar. Escrevi isso varrendo todas as versões de mesma unidade da
experiência. **Verde sobre o banco real, e errado.**

Quem mostrou foi a mutação que **produz o mundo** que o banco não tem: Petra, com escada
de dias (1, 2 e 3 dias por US$ 70, 75 e 80) e uma declaração de US$ 65 discordando do
preço de **um** dia. A régua comparou 65 com **80** — o preço de outro produto — e
reprovou uma resolução correta. **Enquanto a experiência tem uma versão só, as duas
contas dão o mesmo número e ninguém vê.** É a mesma forma dos dois `63` da R1 da
Robometria: duas grandezas diferentes que coincidem por acidente do banco.

Conserto na raiz, não no sintoma: **DECLARACAO ganhou o campo `versao`**; declaração sem
versão atribuída **não participa da resolução** (é conteúdo na tela, não voto na conta);
e a conta passou a varrer só a versão resolvida. Quatro mutações novas guardam isso.

**E o conserto acendeu uma dívida real do próprio banco:** as **quatro** declarações da
gôndola estão com `versao: null`, porque nenhuma das fontes diz se fala do passeio
diurno ou do noturno. A ilha tem quatro divergências e **zero votos na conta** — quem
resolve hoje é a autoridade, sozinha. Está contado no resumo como
`declaracoes_sem_versao`, não escondido.

**A segunda dívida é de coleta e já estava no bloco 2:** duas das quatro declarações
**não têm publicador nomeado**. O bloco 2 anotou o que o *conjunto* de páginas de topo
publica, sem separar quem disse qual número. Pela regra desta ilha, declaração sem nome
não vai para a tela — *"algumas páginas dizem €30 a €90"* é exatamente a frase sem dono
que a ilha existe para não escrever. As duas ficam no banco como evidência de coleta,
com `publicavel_na_tela` **derivado** e conferido pelo validador.

### A seção 26 aplicada ao campo que dói nesta ilha

Na Robometria o fabricante batiza a peça pela **posição** e o banco classifica pela
**função**. Aqui o publicador escreve um **número** e **ninguém declara a unidade** — foi
o achado central do bloco 2, com a gôndola publicada em três unidades diferentes na mesma
página de resultados. Então `unidade_de_preco` e `capacidade_maxima` nascem com
`declarada_por` ∈ {`no_ato_oficial`, `no_texto_da_fonte`, `no_contraste_da_propria_fonte`},
e **sem uma das três o registro não nasce**. A lista dos campos mora no **esquema**, nunca
dentro da régua (26.2) — e a mutação que **apaga a chave do esquema** reprova, que é a
metade que a 26.2 exige e que uma régua ingênua deixaria passar em silêncio.

**Dívida nomeada pela 26.3:** a frase de tela que lê `declarada_por` e escolhe a
atribuição ("o operador declarou" × "a ilha classificou") **não existe** — não há página.
Fica escrita no `ESTADO.md` como dívida, nunca como detalhe.

### As outras três coisas que a régua faz e que não são "conferir campo obrigatório"

1. **A proibição de média virada em código.** Média não se reconhece pelo nome: reconhece-se
   por **cair entre o mínimo e o máximo sem ser nenhum dos dois**. A mutação que prova isso
   precisou de **duas** declarações sobre a mesma versão — com uma só, o preço da versão é
   sempre um extremo e nenhuma média é construível. Descobrir isso foi metade do trabalho.
2. **O piso da 25.2 é DERIVADO.** `url_busca_produto` é fabricada a partir do molde do
   esquema com o `slug_plataforma` da cidade e comparada com o que está gravado. URL de piso
   digitada à mão envelhece calada no dia em que o molde mudar. **Itens sem saída de compra:
   0**, erro duro. **Piso não rastreável: 1** — dívida de comissão, não defeito de página.
3. **O resumo nasce contado.** As doze contagens do `resumo` são recomputadas e comparadas
   uma a uma, nas **duas** direções: número gravado que não bate reprova, e número no resumo
   que ninguém sabe refazer também reprova.

### Verificação, 0 falha

- `python3 ferramentas/validar-banco.py` — verde sobre o banco real.
- `python3 ferramentas/mutacoes-banco.py` — **45 mutações**: **4 MUNDOS que têm de PASSAR**
  (preço por pessoa com escada de dias, preço de criança e temporada; preço por cabine; item
  com link rastreado e `intestavel`; experiência sem divergência nenhuma) e **41 QUEBRAS que
  têm de REPROVAR**. Todas decidiram certo, **nos dois lados da fronteira**. Três das quebras
  atacam o **esquema** e não o dado.
- Os três JSON da pasta passam por `json.load`; o cabeçalho do `ESTADO.md` passa por
  `yaml.safe_load`.
- **Nada foi ao ar, e não havia o que pôr no ar:** esta ilha não tem site, Sync nem
  `/status`. Dizer que verifiquei no ar seria inventar.

### Próximo passo desbloqueado

**A CARGA do banco** — ler na fonte de quem opera as experiências que o bloco 2 mediu
(Petra, Angkor, Ha Long, Dubai, Buenos Aires, balão da Capadócia), com `data_leitura` e
unidade declarada, até haver banco suficiente para o portão de dado da seção 9 (3 itens
reais por página). Não depende de site nem da rede da ilha; depende de busca web, que
está aberta. **A F1 (bloco 4) depende dela, e não o contrário** — ferramenta sobre banco
vazio é a promessa que a seção 9 proíbe.

## 2026-09-14 15h19Z — Bloco 1: corpus de buscas paramétricas

**A ESCOLHA DA ILHA: TERCEIRA TENTADA, duas perdidas na corrida do push.** Pela
18.1, ilha com despacho aberto vem antes da rotação — e **duas** tinham o mesmo
despacho do Raphael de 14/09 sobre o piso de busca, escritas no **mesmo commit**
(`29099ba`, 14h59Z), então o critério "entre dois despachos do Raphael, o mais
antigo" empatou e a rotação da seção 1 desempatou. Reservei a **robometria**
(`ultima_execucao` 13h54Z, a mais antiga das duas): push **recusado**, outra
execução a reservou às 15h17Z. Voltei ao passo 2 sem force push e reservei a
**aquametria** (14h34Z): push **recusado de novo**, reservada às 15h18Z. Das
três que sobraram, a clubedomosaico não tem despacho aberto (os quatro achados
da artesã saíram inteiros às 11h18Z) e tem `ultima_execucao` de 13h21Z;
**jornadafly e ohmetria têm `ultima_execucao: null`, que pela rotação conta como
a mais antiga de todas**; empate em `prioridade: 1` desfeito em ordem
alfabética. Reserva da jornadafly aceita às 15h19Z. **Primeiro bloco da vida
desta ilha.**

**REDE PELA 20.2, ANTES DE TRABALHAR — E ELA ESTÁ BLOQUEADA.** `jornadafly.com.br`
e `www.jornadafly.com.br` devolveram **000** (o proxy recusou o CONNECT por
política da organização), quatro tentativas, enquanto `aquametria.com.br` e
`robometria.com.br` devolveram **200 na mesma passada**. Falha em dois endereços
com dois controles verdes ao lado é rede, não túnel. **A causa tem nome e está
no contrato:** a 20.1 manda pôr o domínio na lista de "Domínios permitidos" no
dia da compra; o domínio está pago desde 13/09 e o passo não foi feito. Virou
despacho de prioridade ALTA para o Raphael em `dados/despachos.md`, cobrindo
também a ohmetria, que cai no mesmo buraco no dia em que registrar o domínio
dela. Gravado `rede: bloqueada em 2026-09-14` no `ESTADO.md`.

**POR QUE O BLOCO SAIU MESMO ASSIM, dito como é e não escondido.** A 20.1 diz
"enquanto isso não estiver feito, a ilha não recebe bloco", e a razão que ela
mesma dá é *"casca no ar que não pode ser verificada é pior que casca
inexistente"*. O bloco 1 **não põe nada no ar**: é arquivo no repositório, o
`PROMPT.md` desta ilha declara que ele não depende de site, e a ilha não tem
WordPress nem endpoint de Sync (os dois campos de "Endpoints desta ilha" estão
literalmente com `<preencher quando o WordPress existir>`). **O que a 20.1
protege está intacto, e o que ela bloqueia de verdade — 3b em diante — está
declarado como bloqueado no despacho.** Se a leitura correta for a mais estrita,
o conserto é uma linha no contrato e quem a escreve é o Raphael; parar a única
ilha do arquipélago com 0 URL e o relógio do Google já correndo, por uma regra
cuja justificativa não alcança este bloco, custava mais.

**O BLOCO.** `dados/corpus-buscas.md` — **15 consultas novas medidas em pt-BR**
em 14/09/2026 entre 15h25Z e 15h40Z, nos três eixos que o `PROMPT.md` manda
(custo de experiência, custo de estadia, passe × avulso) mais o cluster FREE
TOUR do 5c, cada linha com os domínios que de fato responderam. **Nenhum número
de volume de busca**, porque não houve acesso a ferramenta de volume — mesma
disciplina do corpus da Robometria. **Nenhum preço deste arquivo entra no
banco**, e isso está escrito duas vezes lá dentro: o banco desta ilha só aceita
preço colhido na fonte de quem opera, com `data_leitura`.

**O ACHADO QUE SUSTENTA A ILHA, medido e não suposto: o topo da SERP discorda de
si mesmo sobre o mesmo preço, e ninguém data.** Três casos, na mesma página de
resultados cada um: (1) **gôndola de Veneza** — uma fonte dá tabela oficial de
€80, outra dá €90 de dia e €110 de noite, **sobre um preço que é tabelado por
prefeitura**, e o mesmo conjunto de páginas diz que o valor é por gôndola, com
até 6 lugares, o que faz o "por pessoa" ir de €13 a €110 sem que nenhuma resolva
isso para o grupo de quem lê; (2) **Coliseu** — "a partir de €25" convivendo com
"a partir de 18€ ou R$ 104", o segundo com conversão em real cravada sem câmbio
e sem data; (3) **Capadócia** — US$ 164–256, a escada em euro €130/180/300/800 e
€160 num operador nomeado, **três moedas e três recortes de "padrão"**. É a
mesma família do que a Aquametria achou nas réguas de lotação.

**DUAS CORREÇÕES AO QUE O `PROMPT.md` SUPUNHA, as duas para melhor.** (a) Ele diz
que a consulta de Veneza para 2 pessoas não tem quem responda; é verdade nos
títulos, **mas as páginas têm a faixa por pessoa por dia** e o que falta é a
multiplicação e a data — ou seja, a F1 não precisa inventar categoria nova,
precisa **fechar a conta e datar o preço**. (b) O muro do pt-BR **não é
uniforme**: a consulta da Blue Lagoon devolveu SERP quase toda em inglês e **com
plataforma dentro** (`trip.com`, `expedia.com`), o oposto do que foi medido em
Coliseu, Torre Eiffel e Pão de Açúcar. Ficou escrito como **pergunta aberta do
bloco 2, não como critério** — a hipótese de que o muro é forte onde existe
portal veterano brasileiro cobrindo aquele destino **não está provada**.

**UM CRITÉRIO DE BANCO NASCEU DO CONTRAEXEMPLO, e ele é o mais acionável do
levantamento.** Em **Fernando de Noronha** as páginas **já** multiplicam por 2 e
**já** datam o reajuste (TPA com alta de 4,4% em 2026; ICMBio com dois valores e
validade declarada). **Onde a taxa é pública, oficial e datada, o mercado
brasileiro faz a conta direito e a ilha não acrescenta nada.** Portanto:
*prefira a experiência de operador privado, com versões vendidas diferentes
entre si e sem tabela pública.*

**O ÂNGULO "VALE A PENA" JÁ TEM DONO, e isso CONFIRMA a tese em vez de
derrubá-la.** `maladeaventuras.com` apareceu com título de julgamento em quatro
consultas independentes (Capadócia, Torre Eiffel, Roma Pass, gôndola), e o 1º de
"Roma Pass vale a pena" promete **"fiz as contas pra você"** no próprio título.
O diferencial desta ilha não é o ângulo — é o **formato**: preço datado, colhido
na fonte, conta fechada para o grupo.

**O PEDÁGIO DO FREE TOUR, que o plano não previa.** A Civitatis **já está** em
pt-BR neste cluster, citada por nome por terceiros — e **o GuruWalk é citado no
mesmo fôlego e com o mesmo peso** nas duas páginas de topo medidas. O €1 fixo
por pessoa só existe se a reserva sair pela Civitatis, então **página que
recomenda "free tour" sem escolher o operador doa a conversão**. Não muda o
plano; muda a redação, e fica escrito para o 5c não redescobrir. E o cluster tem
um desacordo de fato que dá página inteira: as fontes convergem em €10–15 de
gorjeta por pessoa **e ao mesmo tempo** o topo diz que "free tour não é
verdadeiramente gratuito" — uma família de quatro está olhando para €40–60, e
**essa conta não apareceu em nenhuma página medida**.

**UMA LINHA NOVA NO MAPA DE MONETIZAÇÃO, e ela é o melhor encaixe do
levantamento.** "Vale a pena alugar carro na Islândia" é consulta de
**julgamento** (o recorte da ilha) cujo objeto **é** o produto de **início de
funil** — e as fontes medidas dizem que a diária varia **até três vezes** entre
inverno e verão, o que a torna paramétrica de verdade. É a única página em que o
cookie de 365 dias do aluguel de carro é **a resposta**, não um enxerto. O
`quantocustaviajar.com`, que o `PROMPT.md` registrava como dono de uma consulta,
apareceu **em 1º nesta também** — o que reforça a ordem F1 → F2 → F3 em vez de
enfraquecê-la.

**VERIFICAÇÃO.** Não há site, não há Sync, não há `/status` e não há URL para
abrir: **esta ilha não tem o que verificar no ar, e dizer o contrário seria
inventar**. O que foi medido de verdade nesta execução: os quatro códigos HTTP
da 20.2 (dois 000 e dois 200 de controle), o cabeçalho do `ESTADO.md` passando
por `yaml.safe_load`, e as 15 SERPs, cada uma com os domínios anotados na linha
da consulta.

**ABERTO E NOMEADO:** (a) a **rede** da ilha, despacho de prioridade ALTA para o
Raphael, que trava 3b em diante; (b) a **seção pendente do `VOZ.md`** — as 10 a
15 legendas reais do @jornadafly, que o `PROMPT.md` exige **antes da primeira
página** e que nada neste bloco supre; (c) a **identidade visual** precisa de
aprovação do Raphael antes do 3b; (d) **não existe `manifest.json`** nesta ilha
— nada é publicável ainda, e criá-lo vazio seria inventar infraestrutura antes
do WordPress; (e) nenhum programa de afiliado cadastrado, e pela ordem do
`PROMPT.md` a Civitatis só entra **depois** de haver conteúdo real no ar.

**PRÓXIMO PASSO DESBLOQUEADO: bloco 2 — especificação das ferramentas**
(`dados/especificacao-calculadoras.md` + `dados/constantes.json`), começando
pela **F1**, com o recorte que este corpus estreitou: não "quanto custa a
experiência" (o operador responde melhor e ganha a SERP), e sim **quanto custa
para o SEU grupo, com data de leitura e com o que está fora**. O caso da gôndola
sozinho especifica a ferramenta — preço por veículo e não por pessoa,
capacidade variável, e duas fontes de topo declarando tabelas oficiais
diferentes. **Não depende de site, de domínio nem da rede bloqueada.** E leva
junto a pergunta aberta a medir, nunca a supor: se a fronteira do idioma cede em
destino sem portal veterano brasileiro.

---

## 2026-09-14 17h45Z — Bloco 2: especificação das três ferramentas

**A ESCOLHA DA ILHA: SEGUNDA TENTADA.** Os cinco `ESTADO.md` estavam com
`executando_desde: null`, que pela 1.1 já significa que não há bloco da Fundação
vivo — o git só é consultado para desempatar reserva **vencida**, e não havia
nenhuma. Pela 18.1, as duas ilhas nascidas em 14/09 (ohmetria e jornadafly)
carregam o mesmo despacho do Raphael, escrito no mesmo commit; empate de
destinatário e de data, então valeu a rotação da seção 1, e a **ohmetria**
(`ultima_execucao: null`) vinha antes. **Meu push de reserva dela foi recusado
por cerca de um minuto** — outra execução a reservou às 17h17Z. Voltei ao passo 2
como o passo 5 manda, **sem force push**, e a jornadafly era a seguinte com
despacho aberto. Reserva aceita às 17h20Z, e o rebase daquela volta ainda
atropelou uma terceira reserva (clubedomosaico, 17h18Z), resolvida por rebase e
não por força. Nenhum branch `claude/*` e nenhum PR aberto para mesclar.

**REDE PELA 20.2 — RETESTADA, NÃO HERDADA.** O `ESTADO.md` já trazia
`rede: bloqueada em 2026-09-14`, e a seção 4 é explícita: **bloqueio herdado do
`ESTADO.md` é retestado antes de ser respeitado, nunca lido como fato.** Foram
duas passadas: `jornadafly.com.br` e `www.jornadafly.com.br` em **000** nas duas,
`aquametria.com.br` em **200 na mesma passada**. O bloqueio é real e continua. O
bloco 2 não põe nada no ar.

### O que foi entregue

`dados/especificacao-calculadoras.md` (476 linhas) e `dados/constantes.json`
(6 constantes). As três ferramentas com pergunta-alvo, classificação de SERP pela
14.9, entradas, saídas na ordem da 15.2, régua de divergência, prestação de
contas da seção 7, tabela pré-renderizada, JSON-LD e **recusa declarada**.

### A pergunta aberta do bloco 1 foi medida, e está NEGADA

O bloco 1 proibiu de supô-la: *"o muro do português é forte onde existe portal
veterano brasileiro cobrindo o destino, e fraco onde não existe"*. Se fosse
verdade, mudaria a ordem das cidades do banco. **Seis consultas novas, em três
continentes, e o contraexemplo vem dos dois lados:** Petra não tem portal
veterano dedicado **e** não tem plataforma; Angkor tem **dois** portais veteranos
(`melhoresdestinos`, `queroviajarmais`) **e** também não tem plataforma. Ha Long
trouxe o Booking, Dubai trouxe Hellotickets e uma **página de produto** da
Civitatis em português, Buenos Aires não trouxe plataforma nenhuma — o lugar
delas está tomado por **receptivos brasileiros vendendo direto**.

**Nenhuma cidade do banco muda de ordem**, que era a única decisão que a pergunta
podia mudar. A leitura que aparece no lugar (plataforma entra em atividade de
operador, não em ingresso de sítio público) ficou escrita **com o contraexemplo
ao lado** — o balão da Capadócia, que é atividade de operador privado e deu zero
plataforma — e com o que a derrubaria. Não é critério e não decide nada.

### O que apareceu em 100% das oito consultas dos dois blocos

Ninguém data o preço, e **a unidade do preço troca dentro da mesma resposta**:
gôndola é **por veículo**, o cruzeiro de Ha Long aparece **por cabine** na mesma
lista dos por pessoa, Petra e Angkor são por pessoa **em escada de dias**. Foi
isso que especificou a F1, e não uma ideia: declarar a unidade, fechar a conta do
grupo, datar o preço. A tabela pré-renderizada nasce obrigada a ir até **6
pessoas**, porque é aí que o degrau de capacidade aparece — tabela que para em 4
esconde justamente o que a ferramenta tem de diferente.

### A gôndola, resolvida na fonte que tabela o preço

Cinco leituras divergentes do mesmo preço nas páginas de topo (€80 até 4; €90
dia / €110 noite; €30–90 por pessoa; €16 por pessoa com 5; €34 por pessoa na
plataforma). O **Comune di Venezia** publica €90 de dia (30 min, 9h–19h) e €110 à
noite (35 min), **máximo 5 passageiros**, pela **Delibera della Giunta Comunale
n. 89 de 20/04/2023**, e diz a unidade com todas as letras: não se paga por
pessoa, e sim pelo aluguel da embarcação inteira. **As duas páginas de topo que
dizem "€80 para até 4" não estão arredondando: estão três anos desatualizadas.**
Para 4 pessoas, de dia, a conta é **€90 no total e €22,50 por pessoa**.

**A régua de divergência desta ilha ficou escrita com o erro caro nomeado antes
da direção**, como a seção 10 exige: havendo tarifa de poder público, ela ganha;
não havendo autoridade, resolve-se para o valor **maior**, porque quem chega com
dinheiro a menos perde a experiência na porta e quem chega com a mais volta com
troco. Média continua proibida.

### O diferencial que não depende de nada bloqueado

**IOF de 3,5%** sobre compra internacional no cartão de pessoa física (Decreto
12.499/2025). Por ser percentual, ele entra na conta **na moeda do operador**, sem
precisar de câmbio: *"no cartão brasileiro são €93,15 no total, €23,29 por
pessoa"*. **Nenhuma das seis páginas medidas hoje menciona IOF**, e três
convertem para real sem declarar câmbio nem data — o defeito exatamente inverso.

### O que cai da página, e está dito em vez de escondido

`cambio-eur-brl` e `cambio-usd-brl` nasceram **pendentes**: nenhuma fonte de
cotação é alcançável desta nuvem (`economia.awesomeapi.com.br`,
`open.er-api.com` e `api.bcb.gov.br` em **000**, com o proxy declarando
`connect_rejected`). Constante pendente é **proibida em fórmula publicada**
(seção 10), então a F1 publica na moeda que o operador cobra — que é a que não
muda — e diz o porquê ao leitor. Pesa mais do que parece: **quatro das seis
experiências medidas hoje publicam em dólar**. Virou acréscimo ao despacho de
rede que já estava aberto, pedindo `api.bcb.gov.br` na mesma lista, e **não trava
ferramenta nenhuma**: custa uma linha por resultado.

### A escada da seção 25 não serve como está, e isso foi resolvido sem copiar a forma

Os quatro degraus da 25.1 são de **marketplace** (Shopee, Mercado Livre) e
**nenhum existe no nicho de experiência**. O **princípio** da 25.2 vale inteiro —
o piso nunca depende de ninguém —, então a escada desta ilha é a tradução dele:
página da experiência na plataforma → **página de cidade da Civitatis
(`civitatis.com/br/<cidade>/`), que é o PISO** → página de reserva do operador. O
piso foi medido em **dois destinos independentes** (`/br/veneza/`, `/br/dubai/`) e
é fabricável sozinho a partir do campo `cidade` do banco. Sem programa cadastrado,
o link nasce **cru e sem `rel="sponsored"`**, porque `sponsored` declara relação
**paga** e ninguém paga por aquele clique — a mesma decisão que a Aquametria e a
Robometria já registraram. "Link de loja em breve" não aparece em lugar nenhum.

### A armadilha em que esta execução caiu, e fica escrita

**Duas das minhas consultas carregavam o número que eu queria confirmar**
("IOF … 3,5%", "gondola … 90 euro 110 notturno"), que é exatamente o que a seção
8 proíbe: *pergunte qual é o valor, não se o valor é X*. As duas foram
**descartadas como fonte e refeitas com pergunta limpa antes de qualquer
gravação**. As duas confirmaram por outros publicadores — e a limpa da gôndola
ainda trouxe **o ato que sustenta a tarifa** (Delibera 89/2023), que a plantada
não tinha trazido. **O que sustenta os dois números é a segunda passada**, e é ela
que está citada no `constantes.json`.

### Verificação

**Não há site, não há Sync, não há `/status` e não há URL para abrir: esta ilha
não tem o que verificar no ar, e dizer o contrário seria inventar.** O que foi
medido de verdade: os quatro códigos HTTP da 20.2 (dois `000` e dois `200` de
controle), os três códigos das fontes de câmbio (`000`, com a causa declarada
pelo proxy), o `EGRESS_BLOCKED` na tentativa de leitura direta do
`comune.venezia.it`, o cabeçalho do `ESTADO.md` passando por `yaml.safe_load`, o
`constantes.json` passando por `json.load`, e uma afirmação que compara o
`resumo` do JSON com a lista **contada** — nunca com número digitado, que é a
cicatriz do número de tela — e cobra que **nenhuma constante pendente esteja em
uso**.

### Aberto e nomeado

(a) a **rede** da ilha, despacho ALTO, que trava 3b em diante; (b) o **câmbio**,
acrescentado ao mesmo despacho, que custa uma linha e não trava bloco; (c) a
**seção pendente do `VOZ.md`** — as 10 a 15 legendas reais do @jornadafly, que o
`PROMPT.md` exige **antes da primeira página**; (d) a **identidade visual**, que
precisa da aprovação do Raphael antes do 3b; (e) **nenhum programa de afiliado
cadastrado**, e pela ordem do `PROMPT.md` a Civitatis só entra depois de haver
conteúdo real no ar; (f) **não existe `manifest.json`**, e criá-lo vazio seria
inventar infraestrutura antes do WordPress.

**PRÓXIMO PASSO DESBLOQUEADO: bloco 3 — modelo do banco.** Este bloco já o obriga
a ter `unidade_de_preco` ∈ {por_pessoa, por_veiculo, por_cabine, por_grupo},
`capacidade_maxima`, `versoes[]`, `temporada`, `faixa_etaria`, `data_leitura`
(obrigatória **e visível na página**) e `afiliado.url_busca_produto` preenchida
desde o nascimento. **Não depende de site, de domínio nem da rede bloqueada.**
