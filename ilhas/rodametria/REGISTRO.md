# Registro de execuções — Rodametria

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-10-30 19h17Z–19:44Z — **A ESCADA DA 25.2 CHEGA À TELA NAS DUAS PONTAS**, e o ramo que ela conserta não existe no dado publicado — é por isso que ninguém o via

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** e pela **1.2** não há escolha a fazer. **As duas
exceções que furam o foco foram conferidas e NENHUMA furou.** (a) A **robometria** segue *"no ar e
quebrada"* com despacho **ALTA**, o que pela 1.2 e pela 18.1 teria precedência — mas o conserto **não é
do repositório**, e remedi antes de respeitar o herdado (seção 4): `robometria.com.br/` em **200** e
`/robots.txt`, `/wp-sitemap.xml` e `/wp-json/robometria/v1/status` os três em **404**, com
`rodametria.com.br` e `aquametria.com.br` em 200 na mesma passada. O gesto é de cPanel e é do Raphael.
(b) Os **três despachos do molde** da 32.6 (aquametria, clubedomosaico, robometria) estão **FECHADOS** —
conferido no topo dos três `PROMPT.md`. `executando_desde` estava `null`, que pela **1.1** já significa
que não há bloco da Fundação vivo. Reserva às **19h17Z**, push aceito **de primeira**, campo **reescrito
às 19h29Z** pela mesma execução. Nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br/`, `/wp-sitemap.xml` e
`/wp-json/rodametria/v1/status` os três em **200**, com `aquametria.com.br` em 200 na mesma passada.

**O BRANCH `claude/*` E O `main` SÃO O MESMO COMMIT, e o `git log` desta nuvem veio RASO** — `.git/shallow`
existe, 50 commits. Pela correção de 27/10 no topo da seção 1.1 **não contei nada de história** nesta
execução, e por isso nenhum número daqui é de contagem de `main`.

**POR QUE ESTE BLOCO: ele estava PRÉ-REGISTRADO pelo fecho das 18h13Z**, textual — *"na vitrine, a escada
da casca ESCONDE o cartão quando `url` está vazia, em vez de cair na busca como a F2 faz (…) A tabela de
16 linhas também serve só a ficha, sem a linha discreta da busca. Os dois são BLOCO, não conserto."*

### O DEFEITO, E ELE NUNCA APARECEU NUMA PÁGINA

A **25.2** é literal nas duas pontas: a ficha de produto é **bônus**, e *"quando não existir, ou quando a
ronda marcar como morta, **a busca sobe e vira o botão** — sem esperar decisão humana, sem página ficar
com 'link de loja em breve'"*. **Só a primeira ponta estava na tela.**
`rodametria_casca_cartao_de_compra()` devolvia **string vazia** quando a `url` chegava vazia, e a segunda
ponta vivia no **CHAMADOR** da F2, que resolvia a escada antes de montar o item.

**A F2 nunca teve o defeito. A VITRINE de produto tinha TRÊS lugares lendo a `url` crua**, e os três
quebravam juntos no dia em que uma ficha morresse:

1. o **CARTÃO** sumia da página — com o piso gravado no mesmo registro, ao lado, sem ninguém para o promover;
2. a célula **"Comprar"** da tabela servia `href=""` — e `href=""` **não é botão morto**: é um botão que
   **recarrega a própria página**, com o rótulo "Ver na Shopee" do lado. **Pior que o cartão**, que ao
   menos sumia;
3. a **`Offer` do JSON-LD** saía com `"url": ""` — dado estruturado inválido que olho humano não vê.

**POR QUE NADA VIU, e é a 32.5-d inteira:** os 21 anúncios da vitrine têm ficha, **21 de 21**. O ramo
**não existe** no dado publicado, e régua que lê o dado publicado aprova o mundo que existe. A saída é a
que a ohmetria escreveu: **só a mutação que PRODUZ o mundo o enxerga.**

### O CONSERTO É MECANISMO, NÃO INTENÇÃO

A escada virou **uma função da casca** — `rodametria_casca_escada_de_compra()` — e **todo chamador entrega
os dois links crus**. A F2 **parou de escolher**, então a regra deixou de existir em dois lugares onde
podia divergir: a **32.5-c** desta fábrica nasceu exatamente da metade que não viajou.

**E O DEGRAU SOBE COM A BUSCA**, que é a metade que mente se ficar para trás: o rótulo sai de
`rodametria_casca_rotulo_da_loja()`, e botão que abre **página de busca** dizendo "Ver na Shopee" promete
uma ficha que não existe mais. Medido no ar depois do desembarque: o bloco de compra da F2 serve
**degraus [1, 4]** — os itens do mundo B passam pela escada nova **em produção**.

**A TABELA GANHOU A LINHA DISCRETA DO PISO** que devia desde que nasceu, e ela sai **UMA VEZ** embaixo da
tabela, **não por linha**: o piso é da **CONSULTA** e não do anúncio — medido, **uma `url_busca` distinta
por página** nas duas —, e repeti-la seria o mesmo link **dezesseis vezes**. Com duas buscas distintas a
linha **não sai**, porque "a primeira" é arbitrária, e o portão reprova esse caso em vez de o maquiar.

**NO JSON-LD, `availability: InStock` deixa de sair quando o piso sobe:** afirmar estoque sobre um
**resultado de busca** é afirmar o que ninguém mediu.

### O PORTÃO, E ELE É PHP PORQUE A ESCOLHA É DECIDIDA EM PHP

`ferramentas/teste-escada-de-compra.php`, **138 afirmações e 0 falha**. Ele **CHAMA** a função em vez de
ler o arquivo — régua em Python sobre o texto do PHP conferiria a FORMA. Ele **FABRICA** os mundos que o
dado não tem (ficha morta com piso, ficha sem piso, nenhum dos dois, chave **ausente**, `url` **nula**,
ficha **só de espaço**), e **prova que morde** reproduzindo a escada velha dentro da própria bateria.

**E ELE COBRA A PROMESSA QUE EU ESCREVI NO COMENTÁRIO DA F2**, porque afirmação em comentário é número
digitado em outro traje (32.5-d): a regra velha do chamador é reproduzida e comparada item a item com a
escada, no dado publicado — **10 itens da F2, 4 deles já no mundo B, idênticos**. A F2 é o único lugar
desta ilha onde o mundo B **já existe**.

**TRÊS MUTAÇÕES NO CÓDIGO DE VERDADE, as três reprovadas:** a busca que não sobe (**13 falhas**), o degrau
que fica para trás (**6**), a linha do piso por linha (**2**).

### E AS PÁGINAS DE VITRINE NÃO TINHAM PORTÃO DE AR NENHUM — E É NELAS QUE EU MEXI

`conferir-no-ar.py` confere a casca e a F2; `conferir-institucional-no-ar.py` confere as quatro do 5d.
`/veiculos/` e as filhas **não tinham ninguém lendo o HTML servido** desde que nasceram em 29/10: o que as
media era o portão de **pixel** da 32.5 e o `mutacoes-produto.py`, que roda **sem rede** sobre o gerador.
**Entre os dois faltava quem lesse a página.**

`ferramentas/conferir-produto-no-ar.py`, **191 afirmações**, descobrindo as URLs no `wp-sitemap.xml` lido
no ar (32.5-b: *"régua que não varre todas certifica a página que o autor abriu"*). **Rodado contra a
revisão 23, a que estava no ar: 2 falhas, e as duas eram exatamente a linha do piso que estava subindo.**
O portão **reprovou o mundo de antes do desembarque** — e é o que o faz valer depois.

**E ELE ACHOU TRÊS COISAS, as três do lado da RÉGUA, as três pagas antes de aprovar nada:**

1. **A linha do piso se conta pela CLASSE, nunca pela frase.** A **mesma** frase é a linha discreta de cada
   cartão do carrossel (25.2), **5× numa página sã**. Contar a frase é medir duas coisas com a mesma régua.
2. **`&quot;`** — um título tem `10"`, e sem `unescape` a régua reprova a página **certa**. Mesma pedra em
   que o portão institucional bateu.
3. **O WORDPRESS TEXTURIZA O HÍFEN, e isto vale registro.** O `wptexturize` do `the_content` troca hífen
   **cercado de espaços** por **EN DASH** no retorno do shortcode: o dado diz `550W - 40km/h` e o corpo
   serve `550W &#8211; 40km/h`. O **JSON-LD sai no `wp_head`**, não passa por aquele filtro, e serve o
   hífen cru — **o mesmo nome em duas formas na mesma página**. Não é defeito a consertar: é tipografia do
   WordPress, e brigar com ela custa mais do que vale. É a cicatriz que esta ilha já tem escrita no topo da
   casca (*"o WordPress troca `&&` por `&#038;&#038;` no retorno do shortcode"*) **num traje novo** — e
   quem não a souber escreve uma régua que reprova a página certa. Agora está na régua, com a medição.
   (Espaço duplo também: dois títulos da vitrine o trazem da loja, e normalizar **um lado só** reprova a
   página certa. As três normalizações moram numa função, com a cicatriz de cada uma ao lado.)

### O ACHADO FORA DO ESCOPO, CORRIGIDO COMO PROSA E NÃO COMO MECANISMO

O comentário da vitrine afirmava que *"`atualizar-manifest.py` casa esta constante com o campo `versao` do
manifest"*. **Não casa, e nunca casou:** a palavra `versao` **não aparece uma vez** naquela ferramenta
(ela espelha `sha256` e sobe a revisão, e só) e os itens de `snippets` do `manifest.json` **não têm o
campo** — conferido nos quatro. **`RODAMETRIA_PRODUTO_VERSAO` e `RODAMETRIA_F2_VERSAO` são lidas por
NINGUÉM**; só a da casca é viva, porque é o gatilho de reinstalação dela.

É a família do `height:44px` morto que a 32.5-d registra: **comentário que declara um mecanismo parece
conferido e não mede nada.** O que saiu foi a frase que prometia um portão inexistente. **Não mexi no
esquema do `manifest.json` na mesma passada que desembarca**, e a razão é de risco e não de preguiça:
aquele arquivo é o contrato do Sync, e o Sync é o **único** canal de desembarque desta ilha. Fazer o campo
existir é bloco, e está pré-registrado abaixo.

### O DESEMBARQUE, E A 20.6 OUTRA VEZ

Push às 19h29Z, **revisão 27**. O `/status` respondeu **23** com `ultimo: 19:17:02` — **recente e anterior
ao push**, que pela régua de leitura escrita ontem na 20.6 é **turno de cron**, nem defeito nem cache.
`raw.githubusercontent.com` já servia 27 na mesma passada. Mantive as visitas de pé (o cron desta ilha roda
por **visita**) e a revisão entrou às **19h41:02Z**, no turno seguinte. **As 7 linhas da revisão 27 no log
dizem `ok`, lidas uma por uma** (20.4): os quatro itens de dados e os três snippets.

### MEDIDO NO AR (18.4)

- **`conferir-produto-no-ar.py`: 191 afirmações, 0 falha.** De `piso da tabela 0x` (revisão 23) para
  **`1x`** nas duas páginas, `0 href vazio`, 21 de 21 anúncios nomeados e com saída, 21 `Offer`s com url e
  `availability` em 21 — que é o número certo, porque **21 de 21 têm ficha hoje**.
- **`conferir-no-ar.py` (casca + F2): APROVADO.** Bloco de compra da F2 com **degraus [1, 4]**.
- **`conferir-institucional-no-ar.py`: 210 afirmações, 0 falha.**
- **32.5 a 390 px num navegador de verdade: 8 de 8 APROVADAS, e o primeiro botão de compra é IDÊNTICO ao de
  antes** — `/veiculos/bicicleta-eletrica/` **1084 px**, `/veiculos/patinete-eletrico/` **1129 px**,
  `/autonomia-patinete-eletrico/` **1380 px**. A altura das duas vitrines subiu **39 px** (3774→3813 e
  6383→6422): é a linha do piso, embaixo da tabela, longe da primeira tela. **A altura da F2 não mudou um
  pixel** (5196 px), que é a prova independente de que ela não mudou um byte.
- **Bancada: 21 portões com rede, 0 falha** (eram 20 — ela **descobriu** o portão novo sozinha).

### O PRÓXIMO PASSO DESBLOQUEADO, e são três, em ordem de valor

1. **`/veiculos/` ESTÁ FORA DO MOLDE, e o portão de pixel o diz com essas palavras** — *"sem componente de
   molde nenhum"*, nas duas passadas de hoje. A mãe serve `<p class="rdm-promessa">` onde o molde pede a
   **caixa de resposta**, então os **700 px da 32.5 nunca a julgaram**. É **exatamente** a lacuna que o
   bloco 5d fechou na home (a home era HUB e caía em "fora do molde"), uma página depois — a **32.5-c** em
   estado puro: família nova entra no molde **pelo seletor**, nunca pela intenção. É bloco, não conserto:
   a página não está quebrada, ela é **não medida**.
2. **O CAMPO `versao` NO `manifest.json`**, que faria a constante de versão de cada snippet ser **espelhada
   e impressa** como o `sha256` já é — fechando o buraco de duas constantes que ninguém lê. Mexe no
   contrato do Sync, então é bloco com desembarque próprio, nunca carona.
3. **A FILA NORMAL** segue no bloco **4** (ferramentas) com a **F1 e a F3 travadas por ABERTURA e não por
   coleta** — o `gov.br` para o limiar legal da F1 e o nível 5 (`casasbahia`, `extra`, `magazineluiza`)
   para `carga_max_kg` da F3, os dois despacho **ALTA** em `dados/despachos.md`, remedidos em 29/10.

**E A ROBOMETRIA SEGUE FORA DO AR**, remedida nesta passada: home em 200, os três endpoints em 404. Não é
consertável do repositório.

## 2026-10-30 16h38Z–18h1xZ — **O DESPACHO DA RONDA SAIU INTEIRO (18.2): OS CINCO ITENS ACIONÁVEIS**, e os dois defeitos que apareceram no caminho são da mesma família do item 1 — a página se desdizendo

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. **A exceção que fura o foco foi conferida e NÃO furou:** a
**robometria** está com despacho **ALTA** e está *"no ar e quebrada"*, o que pela 1.2 e pela 18.1 teria
precedência — mas o próprio despacho dela diz, com todas as letras, que o conserto **não é do
repositório**: a reescrita do `.htaccess` da raiz é painel do WordPress ou Gerenciador de Arquivos do
cPanel, e o gesto está na lista do Raphael. **Remedi antes de respeitar o herdado (seção 4):** três
passadas com quebra de cache, `robometria.com.br/` em **200** nas três e `/robots.txt`,
`/wp-sitemap.xml` e `/qual-peca-serve-no-meu-robo-aspirador/` em **404** nas três, com
`rodametria.com.br` e `aquametria.com.br` em 200 nas **mesmas** três. Segue caída, segue não
consertável daqui. `executando_desde` estava `null`, que pela **1.1** já significa que não havia bloco
da Fundação vivo — o último commit na pasta era da **ronda** das 15h10Z, e commit de ronda **não
reserva nada** (1.1). Reserva escrita às **16h38Z**, push aceito **de primeira**, campo **reescrito às
16h58Z** pela mesma execução. Branch `claude/*` e `main` idênticos nos dois sentidos, nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 nas mesmas três.

**POR QUE O DESPACHO E NÃO UM BLOCO: a 18.5 é textual** — *"na dúvida entre fechar um despacho e começar
um bloco novo, fecha o despacho. Ilha com defeito no ar não recebe página nova."*

### ITEM 1 — A FRASE DA F2 NEGAVA O NÚMERO QUE ELA MESMA ACABAVA DE SERVIR

O molde `km_degradado` dizia *"conte com {piso} a {teto} km, e não os {teto} km do anúncio"* — e `{teto}`
**é** a autonomia declarada. Com `60/26/110/ladeira/80` a caixa servia "34 a 80 km" e, logo abaixo, "não
os 80 km do anúncio": o topo da faixa que ela mesma publicou.

**A RONDA OFERECEU DUAS SAÍDAS DEFENSÁVEIS E A ESCOLHIDA FOI A SEGUNDA**, com o motivo: mexer no **topo
da faixa** exigiria um número que **ninguém mediu**. A `faixa_de_km()` deriva o piso de `declarada /
fator` — o fator vem do estudo de Quito, que é fonte — e **não existe fonte para um teto que não seja a
própria declarada**. Inventar o topo para salvar a frase seria a seção 10 ao contrário. Então a frase
passou a dizer do número do anúncio **o mesmo que o `km_plano` já dizia dele**: que ele é **teto**, o
melhor caso. E a frase aponta a ponta da faixa que a pessoa deve esperar, que é o que ela veio saber.

### ITEM 2 — O CAMPO "SEU PESO" NÃO MUDAVA NADA, E A ILHA PROMETIA QUE MUDAVA

**ESTE ITEM FOI FECHADO DUAS VEZES, E A PRIMEIRA ESTAVA ERRADA — a correção dela está nesta mesma
execução, e o que a desmentiu foi um número.** A ronda deu duas saídas defensáveis; comecei pela
**primeira** (a caixa de resultado passar a dizer algo sobre o peso informado), e ela foi ao ar na
**revisão 20**. As frases `peso`, `peso_ladeira` e `peso_acima_do_teto` **já existiam** na regra, já
eram acentuadas e **já diferenciavam 50 de 150** — o tradutor as servia abaixo do bloco de compra —,
então subir uma versão curta delas para a caixa parecia o conserto mais barato.

**NÃO CABE. MEDIDO EM NAVEGADOR DE VERDADE, A 390 PX, URL NO AR:**

| o que está na caixa | primeiro botão de compra | teto da 32.5 |
|---|---|---|
| revisão 19 (como a ronda encontrou) | **1.380 px** | 1.400 |
| revisão 20 (a primeira saída, como foi ao ar) | **1.504 px** | 1.400 |
| idem, com as frases enxutas | 1.477 px | 1.400 |
| + a frase de promessa encurtada | 1.454 px | 1.400 |
| + a frase de abertura do bloco de compra encurtada | 1.434 px | 1.400 |
| a frase do peso **dentro** do parágrafo do km | 1.411 px | 1.400 |

**Nenhuma combinação cabe**, e a causa é que **o custo não é de linha, é de BLOCO**: a frase de 46
caracteres e a de 81 deram **o mesmo número** (97 px de acréscimo), porque o que pesa é o parágrafo.
A página já estava a **98,6% do teto** antes de o despacho existir — e o portão da ordem da 32.1, em
`teste-f2.py`, **já registrava** que "a caixa com as cinco frases longas" empurrava o botão para baixo
do teto. Uma passada anterior já tinha pagado essa conta; eu paguei de novo, e de novo só o navegador
disse. **A simulação previu 1.504 px e o portão da 32.5, rodado contra a revisão 20 no ar, leu
1.504 px** — mesmo número, o que é a prova de que a medição por injeção no DOM serve para decidir
ANTES de empurrar.

**ENTÃO O ITEM FECHA PELA SEGUNDA SAÍDA: O PESO SAI DA PROMESSA.** E ela não é consolo — é a mais
honesta das duas. A F2 deriva o piso de `declarada / fator`, e `fator` é **relevo**: nenhum quilo de
quem pilota entra em fórmula, porque `consumo-absoluto-wh-por-km-patinete` está `pendente` e a seção
10 proíbe. A ilha prometia o peso em cinco lugares e passou a prometer o **relevo**, que ela desconta
de verdade, com a fonte do fator citada na própria página:

- a pergunta da home: *"Faz quantos km de verdade com o seu peso?"* → **"na sua ladeira?"**
- o cartão da F2 na home: o mesmo — e **o corpo dele já dizia a verdade** ("com o relevo do seu
  trajeto descontando o que tem de descontar"); só o título prometia o peso
- as duas meta descriptions (que são também o item 5)
- **três textos das páginas de produto** que diziam que a calculadora *"faz essa conta"* com o peso
- o `VOZ.md`, com a data e o motivo escritos ao lado da pergunta trocada, porque ele é o documento
  que descreve a voz aprovada e mudar a tela sem mudá-lo deixaria os dois discordando

**O PESO CONTINUA EM DOIS LUGARES, e nos dois ele é legítimo.** A **terceira** pergunta da home —
*"Aguenta você e a mochila?"* — é a **F3**, onde peso é **carga** e se compara contra o `carga_max_kg`
de cada veículo: ali ele entra de verdade. E a **ressalva abaixo do bloco de compra**, que nomeia o
peso informado e diferencia 50 de 150 — é ela que faz o campo "Seu peso" **não ser enfeite**, e o
portão novo cobra exatamente isso. O FAQ segue explicando, com todas as letras, que a Rodametria não
converte peso em km.

### ITEM 3 — O PREÇO ERA DE UMA LOJA E O BOTÃO IA PARA OUTRA

**Não é a escolha da loja que estava errada.** A regra de dinheiro desta ilha manda preferir o link da
Shopee, e a cotação do Mercado Livre é a **única com procedência e data** que o `x13-chopper-1000w` e o
`ls-sport-scooter-1000w` têm — confirmado no banco. Era a **frase**: o leitor recebia um preço com
procedência e um botão que não serve aquele preço.

Agora, quando as duas lojas divergem, a nota diz **onde o preço foi lido** e **para onde o botão vai**;
quando são a mesma, ela é a de sempre. O nome da loja saiu de dentro do rótulo do botão para
`rodametria_casca_nome_da_loja()`, porque a partir de hoje **dois** lugares o perguntam — mapeamento
escrito duas vezes é mapeamento que envelhece pela metade no dia em que entrar o terceiro programa.
**A nota continua curta de propósito:** ela nasce ACIMA do botão dentro do cartão.

### ITEM 4 — AS 21 OFERTAS DA VITRINE ERAM INTESTÁVEIS E SEM PISO

**Os três campos do par da 25.4-b não foram colhidos nesta passada: eles já estavam no repositório.**
`dados/anuncios-por-consulta.json` guarda `url_produto`, `shop_id` e `item_id` de **40 de 40** anúncios,
colhidos **na mesma chamada da API** que devolveu `url_afiliado` — então a 25.4-b.1 está atendida sem
remendo, porque os dois lados do par são da mesma oferta, da mesma leitura. Eles só não chegavam até a
tela, e foi por isso que a ronda conseguiu testar 9 das 21 lendo o par no arquivo de anúncios.

**O piso da 25.2 foi a única parte que precisou de rede**, e ele é **um por consulta**, com o motivo
escrito: a chave que achou **todos** os anúncios de uma página é uma só (`chave_escolhida`), e é ela que
a 25.2 pode oferecer como saída honesta. Título de marketplace não é marca mais modelo, e busca por
título inteiro devolve menos que a chave medida. Nasceu `coletar-piso-da-vitrine.py` — **fora** do
gerador de propósito, porque `gerar-vitrine-de-produto.py` roda na bancada **sem rede** e gerador que
depende de rede não se reconfere. Os dois encurtados foram medidos **VIVOS** (301 no encurtador).

**21 de 21 itens servidos com os quatro campos**, e o piso já é **servido** nos cartões sem tocar no
snippet: a escada da casca imprime a linha discreta "Veja todos disponíveis aqui" quando `url_busca`
existe — o mecanismo da 25.2 funcionando como foi desenhado.

### ITEM 5 — DUAS META DESCRIPTIONS PASSAVAM DE 160, E O PORTÃO TOLERAVA 200

161 → **147** na home e 193 → **155** na F2, contados. **E o defeito de fundo era o portão:** ele
aprovava até 200, então as duas passaram com ele verde, e a ronda as achou a olho. Teto em **160** nele
e no espelho offline (`teste-institucional.py`, cujo texto de falha já dizia ser espelho do de ar).
**E as entidades HTML passam a ser desfeitas ANTES de contar:** o atributo vem escapado do `esc_attr`,
então um apóstrofo chegaria como `&#039;` e contaria **6** caracteres no lugar de 1 — a família do
`&#038;` que a própria seção 12 cobra dentro de `<script>`.

### E DOIS DEFEITOS QUE NÃO ESTAVAM NO DESPACHO, achados ao escrever os itens acima

1. **`peso_ladeira` mandava "esperar o PISO da faixa" também quando a caixa havia RECUSADO o km.** Com
   ladeira e sem autonomia declarada, a caixa dizia *"não dá para dizer quantos km esta bateria faz"* e a
   ressalva, logo abaixo, mandava esperar o piso **de uma faixa que a página acabara de se recusar a
   dar**. É a **mesma família do item 1**, um andar abaixo. Agora ela só nasce onde existe faixa com duas
   pontas, e a guarda está escrita nas duas metades (regra e navegador).
2. **A frase de peso acima do teto dizia "veja se o modelo AGUARDA o seu peso".** Texto de tela, e a
   palavra desta ilha — a do `VOZ.md` — é **aguenta**. Ela não está na página de exemplo (o exemplo tem
   110 kg e o teto é 120), mas viaja no arquivo publicado e o navegador a imprime.

### OS PORTÕES QUE NASCERAM COM O FECHO — e os três MORDEM, provado por mutação

- **`teste-f2.py`** ganhou as réguas dos itens 1 e 2, e **as duas se provam antes de julgar**: o
  primeiro caso de cada uma exige que ela **REPROVE o texto que estava no ar**, senão é portão
  **inerte** — a cicatriz que a bancada desta família já nomeia com essa palavra. A do item 2 **mudou
  de alvo** junto com a decisão: ela cobra a **ausência da promessa**, não a presença da frase, mais a
  ressalva **nomeando o peso informado**. **E ela nasceu com um defeito que a própria bateria achou:**
  a primeira versão varria TODO literal dos dois snippets e reprovou **três textos do FAQ** —
  inclusive a resposta que diz *"a Rodametria não converte peso em km"*, que é exatamente o que a ilha
  deve ao leitor depois de tirar o peso da promessa. **Explicação não é promessa.** Agora ela julga
  **21** textos nos slots que prometem (`description`, `titulo`, `<h1>`, a frase de promessa e os
  títulos dos cartões) e **exige um piso de 8 textos julgados**, para não aprovar por cegueira.
  Mutações, todas reprovando: a pergunta da home voltando a prometer o peso; a description voltando; a
  ressalva parando de nomear o peso; o molde do item 1 voltando a negar o topo. **E o portão pegou,
  sozinho, um erro meu que nenhuma leitura pegaria:** ao desfazer a primeira saída eu removi o molde
  `peso_caixa` do arquivo publicado e **deixei o JS citando-o** — a página teria impresso `{piso}` na
  cara de quem lê.
- **`teste-nota-de-preco.php`** — **PHP porque a frase é decidida em PHP**. Uma régua em Python sobre o
  texto do arquivo conferiria a FORMA; esta **chama a função** e lê o que o leitor recebe. Julga quatro
  mundos (loja igual, o defeito, o **espelho** do defeito, e cartão sem botão) **mais os cartões reais do
  arquivo publicado**. Mutação: a nota voltando à forma antiga → **4 reprovações**, duas delas nomeando
  o X13 e o LS Sport. E a bateria achou um furo na **minha** régua: cartão sem botão não tem destino para
  prometer, e ele nem chega à tela — o ramo nasceu com o caso que o provou.
- **`validar-banco.py` passa a CONTAR A VITRINE**, que é o buraco que o despacho nomeia. A régua não
  mudou; mudou o que ela alcança. Mutação: a vitrine de volta ao estado de ontem → **21 intestáveis, 0
  com piso**, com uma falha por item. Era o estado em que o portão podia escrever "intestáveis: ZERO"
  com verdade sobre o banco que lia e falso sobre um terço dos links que a ilha servia.

**O ITEM 6 NÃO FOI TOCADO, e está certo assim:** ele não é conserto. É a receita do anti-robô da Shopee
(teto de chamadas na janela, não intervalo) e mora onde a próxima ronda vai procurá-la.

### O QUE FICA PARA QUEM VIER, e nada disto é deste despacho

1. **A ressalva do peso termina apontando para frente, e no caso `misto` não há nada depois dela.** O
   molde diz *"Eles entram aqui, no que esperar da faixa"* — e com `ladeira` a frase seguinte entrega
   (*"espere o PISO da faixa, não o meio dela"*), mas com `misto` ou `plano` a ressalva fica sozinha
   prometendo um "aqui" que não vem. É a mesma família do item 2, uma oitava abaixo, e é **anterior a
   esta execução**. Não mexi: o item 2 foi fechado e verificado, e alargar despacho é o que a 18.2
   proíbe. Fica nomeado para a ronda decidir.
2. **Na vitrine, a escada da casca ESCONDE o cartão quando `url` está vazia**, em vez de cair na busca
   como a `rodametria_f2_itens_da_vitrine()` faz. Hoje os 21 têm ficha, então o ramo não existe; no dia
   em que uma morrer, o piso está no dado e a tela não o promove sozinha. **A tabela de 16 linhas
   também serve só a ficha**, sem a linha discreta da busca. Os dois são **bloco, não conserto**.
3. **A robometria segue FORA DO AR com despacho ALTA**, remedida nesta passada em três leituras com
   quebra de cache. Não é consertável do repositório: a reescrita do `.htaccess` da raiz é cPanel, e o
   gesto é do Raphael.

### O FECHO, CONFERIDO NO AR PELA 18.4

**Revisão 23**, com as linhas da revisão corrente do log dizendo `ok` (20.4, lidas uma por uma).

- **32.5: APROVADO em 1.380 px**, que é exatamente onde a ronda encontrou o botão — 8 de 8 páginas do
  molde dentro, pior caixa em 331 px contra o teto de 700.
- **`conferir-no-ar.py`: APROVADO**, e com o teto novo: as **nove** URLs com description entre **131 e
  159** caracteres, contra as de 161 e 193 que a ronda achou.
- **`conferir-institucional-no-ar.py`: 210 afirmações, 0 falha.**
- **Bancada com rede: 19 portões, 0 falha** (eram 17 antes desta execução).
- **Item 1 no ar:** a caixa serve *"os 60 do anúncio são o teto"*, e a oração proibida tem **zero**
  ocorrências na página.
- **Item 2 no ar:** **zero** ocorrências de "com o seu peso" na home e na F2, e a ressalva abaixo do
  bloco de compra segue nomeando os 90 kg da entrada.
- **Item 3 no ar:** os cartões do X13 e do LS Sport servem *"lido na Mercado Livre em 27/10/2026 — o
  botão abre a Shopee"*; os dois de loja igual seguem com a nota de sempre.
- **Item 4 no ar:** **5 de 5** cartões em cada página de produto servem a linha discreta do piso, e cada
  página serve a busca da **sua** consulta.

**TRÊS TURNOS DE CRON, e é a causa do bloco longo — não foi trabalho.** O Sync desta ilha roda por
visita (20.6), mas **visita não antecipa evento que ainda não venceu**: cada revisão esperou o seu turno
de 30 minutos (20 às 17h10, 22 às 17h39, 23 às 18h10), e cada conferência da 18.4 precisa da revisão
**pousada**. A reserva foi renovada três vezes pela 1.1.


## 2026-10-30 13h5xZ–14h4xZ — **BLOCO 5d: AS QUATRO PÁGINAS QUE O SITE DEVIA A QUEM LÊ** — e a de privacidade não promete nada: tudo o que ela afirma foi **medido na página servida**, inclusive o que era mais fácil de esconder

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi antes as duas exceções que furam o foco: (a) o
**despacho do molde da 32.6** está `FECHADO` nas três ilhas que a 32.6 nomeia — lido no topo dos três
`PROMPT.md`, com hora de fecho em cada um; (b) nenhum despacho **ALTA** é de ilha *"no ar e quebrada"*.
`executando_desde` estava `null`, que pela **1.1** já significa que não havia bloco da Fundação vivo —
reserva escrita às **13h54Z** (commit `a860712`), push aceito **de primeira**, campo **reescrito às
14h11Z** pela mesma execução. `git log` entre `origin/main` e `origin/claude/dreamy-mccarthy-4smb5m`
veio **vazio nos dois sentidos** e a listagem de PRs devolveu **zero aberto** — nada a mergear.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 nas mesmas três, e o `/status` em 200 na **revisão 17**, a que o 5c deixou.

**POR QUE O 5d.** O próprio `PROMPT.md` já o declarava *"o próximo bloco, e ele não espera ninguém"*,
com as três razões escritas: não depende de despacho nenhum, fica fora do teto da 21.4 pela **21.7**, e
é dívida de confiança no ar. A dívida estava medida desde a contagem de sitemap de 30/10 às 10h3xZ: **a
ilha serve link de afiliado da Shopee desde 29/10** e não tinha `/divulgacao-de-afiliados/` nem
`/privacidade/`.

---

### 1. O QUE FOI AO AR

**Quatro URLs, e a casca não foi tocada.** `/sobre/` (#21), `/contato/` (#22),
`/divulgacao-de-afiliados/` (#23) e `/privacidade/` (#24), pelo snippet `rodametria-institucional`
**1.0.0** (#9 no Code Snippets). Elas entraram pelos filtros `rodametria_paginas` e
`rodametria_instalar`, de dentro do próprio snippet delas — que é a promessa que a casca faz desde a
revisão 3 dela, *"a casca não é editada quando a ilha cresce"* —, e a instalação rodou porque a
**assinatura do mapa** mudou, que é exatamente o que a casca **1.4.0** nasceu para fazer em 29/10.
Zero linha de casca neste bloco, e portanto zero risco no arquivo que pinta todas as páginas.

**A instalação aconteceu na requisição SEGUINTE à do Sync, e isso é o mecanismo funcionando.** O log
diz `snippets/rodametria-institucional: ok (snippet #9 criado)` às 14h40, e o relato de instalação da
casca é de **14h41:38** — porque quando o `init` chamou a instalação às 14h40 o snippet ainda não
estava carregado naquela requisição. Era exatamente o defeito de 29/10 que custou as três páginas do
5b; com a assinatura no lugar da versão, a passada seguinte criou as quatro sem ninguém tocar em nada.

`pai` **nulo** nas quatro, pela **16.1** ao pé da letra (*"sem página solta na raiz além de home,
sobre, contato, divulgação de afiliados e privacidade"*) — e `garantir_pagina()` aceita pai zero
exatamente por elas. `no_menu` **true**: o `VOZ.md` manda um menu curto de assunto, e página
institucional no menu de cima rouba o lugar do que a pessoa veio procurar. Elas aparecem no **rodapé**,
que a casca monta do mapa inteiro e serve em toda página — e isso fechou a **16.4(f)** com folga:
medido no ar, cada uma das quatro **recebe link de 9 das 9 páginas no ar**, contra as 2 que a regra pede.

### 2. O DESEMBARQUE, PELA 20.4 E PELA 20.6

Revisão **19** no `/status`, com as **cinco** linhas da revisão corrente lidas **uma por uma** e todas
dizendo `ok`. O portão de ar também as leu e registrou: *"15 linha(s) na janela, 1 da revisão 19, 0
linha de falha nesta entrega"*.

**E a 20.6 foi medida de novo, com um achado que ela não tinha.** A 20.6 diz que o cron roda **por
visita** e não por relógio, e isso continua verdadeiro — mas ela não diz o que acontece quando o evento
**não está vencido**. Empurrei a revisão 18 às 14h11Z e o `/status` ficou em 17 por meia hora, com
`ultimo: 14:10:04` — ou seja: o Sync **havia rodado** às 14h10, um minuto antes do meu push, e o
`rodametria_30min` só vencia às ~14h40. Visitar a home e bater no `wp-cron.php` (que respondeu **409**,
prova de cron em andamento) **não antecipou nada**, e não devia: o WP-Cron dispara evento **vencido**,
não evento futuro. A revisão entrou às **14h40:39**, pontualmente no turno.

**A régua que isto acrescenta, e ela é de leitura e não de conserto:** o campo `ultimo` do `/status`
separa os três mundos que a 20.5 junta em dois. `ultimo` **antigo** = o Sync não rodou (defeito).
`ultimo` **de agora** com revisão atrasada = cache do GitHub (reacione). `ultimo` **recente mas
anterior ao push** = nem defeito nem cache: é **turno de cron**, e o que resolve é esperar o próximo
mantendo as visitas de pé para ele disparar. Gastei uma rodada de reação achando que era cache, até ler
o `ultimo` e ver que ele era mais velho que o meu próprio push.

### 3. A PÁGINA DE PRIVACIDADE FOI **MEDIDA** ANTES DE ESCRITA, E É ISSO QUE ELA TEM DE DIFERENTE

Não escrevi uma política de privacidade: medi o que o site faz e escrevi o que medi. As quatro
medições, feitas do lado de fora, como o navegador recebe:

| o que | medido | consequência na página |
|---|---|---|
| `Set-Cookie` | **zero**, nas URLs no ar | a página afirma que o site não escreve cookie nenhum |
| medidor de audiência e pixel | **zero** ocorrência de doze famílias procuradas | a página afirma que não há medidor — e não há GA4 nesta ilha |
| endereços de fora que **carregam** | **dois**: Google (`fonts.googleapis.com` e `fonts.gstatic.com`, em toda página) e Shopee (`cf.shopee.com.br`, onde há foto) | a página **nomeia os dois**, com o que cada um serve |
| endereços que são **só link** | `s.shopee.com.br` e `dspace.ups.edu.ec` | a página diz que link não faz nada até o clique |

**E A MEDIÇÃO ACHOU O QUE ERA MAIS FÁCIL DE ESCONDER, que é a parte de que mais me orgulho neste
bloco.** A primeira versão da página dizia, como toda página de privacidade de calculadora diz, que *"a
conta é feita no seu navegador e o que você digita não sai dele"*. O formulário da F2 é
**`method="get"`** com `action` para a própria URL: se a pessoa aperta o botão, **os números vão para o
endereço da página** e passam pelo servidor junto com o pedido, e ficam no registro de acesso do
hospedeiro. A frase bonita era **falsa na metade que importa**. O que foi ao ar diz as duas coisas
separadas — mexer nos campos não envia um byte; apertar o botão põe os valores na barra do navegador,
de propósito, para o resultado poder ser guardado ou mandado para alguém — e nomeia quais são os
quatro números. **Dizer "nada sai" seria mentir em quatro palavras.**

**A `/contato/` NÃO INVENTOU UM CANAL.** Esta ilha não tem caixa de e-mail, e o despacho de 13/09 em
`dados/despachos.md` — *"o que NÃO se faz enquanto isso: publicar um endereço que ninguém lê"* — é
explícito. A página diz que o canal não existe, diz por que, e entrega no lugar o que de fato serve:
toda afirmação daqui carrega fonte e data, e a seção do fim de cada página nomeia a loja, o anúncio e o
dia da leitura, para conferir **sem intermediário**. O despacho foi reescrito hoje: ele dizia "nenhuma
das **três**" e agora são **quatro**, com o custo novo escrito (uma página chamada "Contato" sem
contato) e com a linha que a Fundação troca no dia em que a caixa existir — **uma linha**, no JSON
declarado, sem tocar em código.

### 4. NENHUM NÚMERO É DIGITADO: 16 MOLDES CONTADOS NA HORA DE SERVIR

A prosa mora em `dados/paginas-institucionais.json` e traz molde no lugar de todo número;
`rdm_inst_numeros()` os conta ao servir, das options que o Sync grava e do mapa de páginas da casca.
Isto não é preciosismo: esta é a família de página que **fala de si mesma** (*"quantos itens têm link",
"quantas páginas no ar"*), que é justamente o caso em que a seção 8 diz que o número digitado passa a
mentir calado.

**As quatro caixas no ar, cada número conferido por uma TERCEIRA CONTA** — recontado em Python, dos
arquivos de dado, por caminho diferente do que o PHP usa, e comparado com o HTML servido:

| página | caixa | no ar | terceira conta |
|---|---|---|---|
| `/sobre/` | veículos no banco | **17** | 17 |
| `/contato/` | anúncios lidos um por um | **40** | 40 |
| `/divulgacao-de-afiliados/` | itens com link de loja | **5** | 5 |
| `/privacidade/` | páginas no ar | **9** | 9 |

A conta de `/privacidade/` é a mais interessante das quatro porque as duas metades leem **fontes
diferentes de verdade**: o PHP conta o **mapa de páginas da casca** e o portão conta o
**`wp-sitemap.xml` servido**. Quando elas discordarem, a divergência é informação e não ruído — URL no
sitemap que o mapa não conhece é página órfã da árvore da 16, e página no mapa que o sitemap não lista
não é indexável.

### 5. TRÊS PORTÕES REPROVARAM A PÁGINA **CERTA** EM DOIS DIAS, E A TERCEIRA VEZ FOI HOJE

Esta é a lição de método do bloco, e ela tem nome no contrato: *"portão que reprova página certa é o
caminho mais curto para alguém passar a ignorá-lo"* (20.5 e 32.5-b, com as mesmas palavras).

1. **30/10, bloco 5c:** `gerar-f2.py --conferir` reprovava a F2 por causa do selo `gerado_em`.
2. **30/10, hoje, `teste-institucional.py`:** a régua que proíbe a folha desta família de redecorar o
   que é da casca procurava a palavra `h1` no texto da folha — e achou **o comentário que explica por
   que ela não mexe em h1**. Consertada para medir **seletor**, com as duas metades provadas no
   autoteste: o comentário que cita `h2` não reprova, e `.rdm-inst-secao h2{}` reprova.
3. **30/10, hoje, `conferir-institucional-no-ar.py`:** disse que dois itens do bloco de recusa de
   `/sobre/` *"não estão no ar"*. Estavam, inteiros e corretos: `esc_html()` transforma a aspa reta em
   `&quot;` e a comparação era contra o texto declarado, com aspa. Consertado com `html.unescape`.

Nas três, a tentação era mexer na página. Nas três, o defeito era da régua.

### 6. E UM PORTÃO NÃO ESTAVA REPROVANDO O QUE DEVIA: A **HOME** ESTAVA FORA DA 32.5 DESDE QUE NASCEU

Achado escrevendo este bloco, e é a **32.5-c** outra vez — *família nova entra no molde pelo seletor,
nunca pela intenção*. `conferir-32-5-no-navegador.mjs` decidia "está no molde" por
`!!(bloco_de_compra || formulario)`. Página com **caixa de resposta e sem nada para vender** caía em
`fora do molde`: a caixa era medida, **impressa** e **nunca julgada** contra os 700 px. A 32.5 diz o
contrário com todas as letras — *"o formulário (ou a caixa de resposta, em ficha) começa antes de 700
px"*: ter caixa já é estar no molde.

**E não era hipotético: a HOME desta ilha é HUB, não tem bloco de compra e não tem formulário.** Ela
estava fora do veredito desde 29/10. Medida agora, passa com folga — mas passar por medição e passar
por omissão são coisas diferentes, e só a primeira avisa quando mudar. As quatro páginas de hoje
entrariam pela mesma porta: seriam **quatro** páginas de molde que o portão abria e deixava passar.

O teto de **compra** passou a ser julgado só onde há o que comprar, e onde não há o portão **imprime**
"não se aplica (a página não vende nada)" em vez de pular calado — com a outra metade cobrada: página
que serve link patrocinado **fora** de um bloco de compra é **reprovada**, porque sem o componente o
teto não teria o que medir. Sem isso a isenção viraria a porta dos fundos dos 1.400 px.

### 7. MEDIDO NO AR — os números, e nenhum deles é a conta de antes do desembarque

**32.5, a 390 px num Chromium de verdade, com quebra de cache** (`conferir-32-5-no-navegador.mjs`,
descobrindo as URLs no sitemap): **8 de 8 páginas do molde aprovadas**, de 3 antes do conserto.

| página | caixa de resposta | compra | altura |
|---|---|---|---|
| `/sobre/` | **211 px** | não se aplica | 3.769 px |
| `/contato/` | **244 px** | não se aplica | 3.372 px |
| `/divulgacao-de-afiliados/` | **244 px** | não se aplica | 3.946 px |
| `/privacidade/` | **244 px** | não se aplica | 5.092 px |

Teto da caixa: 700 px. Pior caixa da ilha inteira: 331 px (a home). `/veiculos/` segue **fora do
molde**, e agora com o motivo exato impresso: não tem componente de molde nenhum.

**O piso de 1.500 caracteres da seção 8, MEDIDO NO AR** e não pela conta feita antes de desembarcar —
que é o erro que a mãe `/veiculos/` quase pagou em 29/10, quando a conta de antes dava 1.253 e a página
no ar passou: `/sobre/` **4.449** · `/contato/` **3.674** · `/divulgacao-de-afiliados/` **4.786** ·
`/privacidade/` **5.899**.

**Bancada com rede: 17 portões, 0 falha, APROVADO.** `conferir-no-ar.py` 445 afirmações / 0 falha nas
**9** URLs; `conferir-institucional-no-ar.py` **210** afirmações / 0 falha;
`conferir-32-5-no-navegador.mjs` 8 de 8. Sem rede: 14 portões, 0 falha, com os **19 casos de autoteste**
do portão novo, que **fabricam** o mundo de cada regra em vez de esperar que o dado o produza — dígito
plantado na prosa, molde órfão, promessa escondida dentro do bloco de recusa, negação no meio da frase,
número literal na caixa, página fina.

### 8. O QUE ESTE BLOCO NÃO FEZ, dito em vez de deixar implícito

- **A `/contato/` não tem canal**, e isso é do Raphael. Está no despacho, agora com quatro ilhas.
- **A ilha segue com `piso: abaixo`:** 9 URLs contra as 40 da 21.1. As quatro de hoje **não contam para
  o piso de malha** — a 21.7 as tira do teto justamente porque nenhuma responde a uma busca.
- **O teto de levas da 21.4 não foi gasto:** pela 21.7 estas quatro não são leva.
- **O soft 404 da borda do hospedeiro** segue sendo despacho ALTA e não se conserta daqui.

**PRÓXIMO PASSO DESBLOQUEADO.** A fila não tem mais nada que seja ao mesmo tempo grande e livre: a
**F1** depende do `gov.br` (despacho ALTA), a **F3** depende de `carga_max_kg` em registro com oferta,
as duas consultas que sobraram da cauda dependem de uma sessão de Chrome (despacho de 30/10, no topo do
`PROMPT.md`), e `scooter`/`moto elétrica` dependem das etiquetas do Mercado Livre. O que **não**
depende de ninguém é o **bloco 4**: a **F3** como REGRA, sem página — o mesmo desenho que a ohmetria
usou para a F1 dela com o banco vazio, e que esta ilha já usou na F2. Ela nasce medindo quantos
registros têm carga máxima declarada e dizendo na própria tela o que falta, em vez de esperar o dado.

## 2026-10-30 10h1xZ–10h4xZ — **BLOCO 5c: A CAUDA DESTE NICHO É TERRITÓRIO DE FAZENDA** — três das cinco consultas fecharam sem precisar do Chrome, e no caminho a bancada acusou um portão que reprovava a página CERTA

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi antes as duas exceções que furam o foco:
(a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas — lido no topo dos três `PROMPT.md`,
com data e hora de fecho em cada um (aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria
21/10 16h1xZ); (b) nenhum despacho **ALTA** é de ilha *"no ar e quebrada"*. `executando_desde` estava
`null`, que pela **1.1** já significa que não havia bloco da Fundação vivo — reserva escrita às
**10h17Z** (commit `392bece`), push aceito de primeira, reescrita às **10h25Z**. O `main` vinha de um
**forced update** (`b793f79` → `3c952f0`); o branch `claude/dreamy-mccarthy-lbibd5` estava **idêntico**
ao `origin/main` (zero commits de diferença nos dois sentidos) e **nenhum PR aberto** — nada a mergear.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 nas mesmas três, e o `/wp-json/rodametria/v1/status` em 200 na **revisão 16**
— a mesma que o 5b deixou, com **todas** as linhas da revisão corrente dizendo `ok` no log (20.4).

---

### 1. O QUE O BLOCO MEDIU, E ELE CORRIGE A PREMISSA DO PRÓPRIO BLOCO

O 5c estava escrito dizendo que *"o caminho mais curto é a cauda medida do corpus"*. Medi as **cinco**
caudas do eixo D com o único instrumento desta nuvem — busca — e colhi **102 ocupantes com URL**.
O placar, contado do próprio arquivo e não digitado:

| consulta | buscas/mês | veredito | por quê |
|---|---|---|---|
| `patinete elétrico adulto` | 49.500 | **tomada** | 6 fazendas com página dedicada (`melhor-patinete-eletrico-adulto`) + categoria dedicada da Casas Bahia |
| `melhor patinete elétrico` | não medido | **tomada** | **12** fazendas com página dedicada, mais o blog da Shopee. A medição mais limpa das cinco |
| `moto elétrica 1000w` | 14.800 | **tomada** | 5 páginas brasileiras dedicadas (4 de fazenda + `consultadeplaca.net`), com o MENOR vazamento das três de potência |
| `patinete elétrico 1000w` | não medido | **nao-medida** | **17 dos 21 ocupantes fora do Brasil**; nenhum dos 4 brasileiros é página dedicada |
| `scooter elétrica 1000w` | 33.100 | **nao-medida** | 13 de 19 fora do Brasil, e o instrumento **derivou** para `autopropelido` |

**O ACHADO, e é de fila e não de página: a cauda deste nicho é território de FAZENDA.** O dossiê
registrou, nas seis cabeças vistas no Chrome do Raphael, que *"nenhuma fazenda da lista apareceu"*. Na
cauda ela aparece em **quatro das cinco**, com **26** páginas dedicadas de fazenda entre os 102
ocupantes — e no formato *"melhor X"* / *"Top 10"* que o `VOZ.md` desta ilha **proíbe nominalmente**.
**A proibição da voz e a medição da SERP coincidem**, e isso não é coincidência: a ilha foi desenhada
para o eixo paramétrico, e a cauda de produto é o campo do concorrente que ela não quer ser. O
`ACHADO D` do corpus de 28/10 já tinha visto a fazenda nas caudas; o que faltava era tirar dele a
conclusão de fila. **A cauda não é o caminho curto desta ilha: é onde ela perderia.**

**ZERO PÁGINA NOVA, E É A 30.8 FUNCIONANDO.** `tomada` fecha a consulta — barato e final, e três
fecharam sem gastar um minuto do Raphael. `nao-medida` não autoriza nada. Vale a frase da seção:
*"errar para o lado de não publicar é barato; errar para o lado de publicar é a leva inteira"*.

**E A 30.4 ESTAVA CUMPRIDA SEM NINGUÉM PLANEJAR.** `/veiculos/patinete-eletrico/` serve a palavra
`adulto` **53 vezes** no HTML no ar (contado às 10h2xZ, com quebra de cache), porque `patinete eletrico
adulto` é o **degrau 1** da escada de chaves daquela página. A intenção da cauda de 49,5 mil já está
atendida por uma URL que existe — abrir uma segunda seria canibalizar a própria mãe. **Não refiz nada
por isso**: o reforço que a 30.4 manda já estava no ar.

**O que foi escrito:** `dados/consultas-de-produto.json` (a fonte: 11 consultas, 6 cabeças + 5 caudas,
com `forma` agora **explícito** em toda linha) e `dados/consultas-de-produto.md` (a vista legível,
**gerada do JSON na mesma passada** para não haver erro de transcrição). O despacho da 30.8 está no
topo do `PROMPT.md`: duas SERPs e um volume, numa sessão de Chrome.

**DOIS RÓTULOS MEUS MENTIRAM E FORAM CONSERTADOS ANTES DE FECHAR**, e registro porque é a família do
número de tela digitado: o placar nasceu com `com_pagina_no_ar: 4`, contando **slug declarado** —
e `veiculos/moto-eletrica` e `veiculos/scooter-eletrica` têm endereço reservado desde o 5b e **não
existem no ar**. O número do ar é **2**, e agora o arquivo traz os dois campos separados com a causa
da diferença escrita. O segundo: `ocupantes_registrados_com_url` somava um total com **duas
procedências diferentes dentro** (as cabeças vêm do dossiê, por domínio e sem URL por ocupante) —
virou `ocupantes_com_url_das_CAUDAS_medidos_em_30_10`, que diz de quem a conta é.

---

### 2. O DEFEITO QUE A BANCADA ACUSOU ANTES DE EU CONSTRUIR (18.5), E ELE É UM PORTÃO REPROVANDO A PÁGINA CERTA

Rodei `ferramentas/bancada.py --no-ar` antes de escrever uma linha, como a 18.5 manda. Ela reprovou:
`gerar-f2.py --conferir` dizia que `dados/f2-respostas.json` estava diferente do que a referência
produz. **A única diferença, medida campo por campo, era o selo `gerado_em`: `2026-10-29` →
`2026-10-30`.**

**A causa:** o gerador escrevia esse campo com o **relógio da execução**
(`datetime.utcnow()`), num arquivo **derivado** cujo conteúdo não depende de data para nada que a F2
calcula. Logo o portão era **irreprodutível por construção** e passava a reprovar **todo dia seguinte**
ao que a F2 fosse gerada. É exatamente o perigo que a **20.5** e a **32.5-b** nomeiam: *"portão que
reprova página certa é o caminho mais curto para alguém passar a ignorá-lo"* — e o perigo maior é
concluir que o portão mente e passar a ignorá-lo de vez.

**A irmã já fazia certo, e a lição não havia viajado — a 32.5-c outra vez.**
`gerar-vitrine-de-produto.py` escreve `'gerado_em': anuncios['gerado_em']`, **herdado do dado**, e por
isso é reprodutível. Os `coletar-*` usam a data de hoje e **estão certos**: ali a data é a da
**medição**, que é procedência e tem de entrar na comparação.

**O conserto:** o selo saiu da comparação — e **só ele** —, com o motivo, a data e a medição escritos
no código, ao lado do que o portão continua cobrando. **As duas metades do veredito foram provadas em
cinco casos**, porque portão que só aprova é inerte:

| caso | esperado | palavra impressa | código de saída |
|---|---|---|---|
| mundo real, selo de ontem | aprovar | APROVADO | 0 |
| só o selo trocado por `1999-01-01` | aprovar | APROVADO | 0 |
| um **número** da tela mexido (`exemplo.tensao_v`) | reprovar | REPROVADO | 1 |
| uma **frase** da tela mexida (`nota`) | reprovar | REPROVADO | 1 |
| arquivo corrompido, não-JSON | reprovar sem explodir | REPROVADO, com o erro nomeado | 1 |

**NÃO REGEREI O ARQUIVO para "consertar" o selo**, e isso é decisão: regerar mudaria `gerado_em` para
30/10 e empurraria uma **revisão nova do Sync sem uma letra de mudança na tela**. O arquivo no ar e o
do repositório seguem com `2026-10-29`, que é a data em que a F2 foi de fato gerada, e é o que a página
diz a quem lê (*"Esta página foi gerada a partir do nosso banco em 29/10/2026"*). Nenhum desembarque
nesta execução, de propósito.

**POR QUE ISTO NÃO VIROU SEÇÃO DO `ARQUIPELAGO.md`, e conferi antes de decidir.** A 20.4 manda a regra
subir ao contrato quando *"o Sync é o mesmo código nas três"*. Aqui o código **não** é compartilhado:
cada ilha tem os geradores dela. Varri as outras cinco e o defeito **não existe lá** — e duas já fazem
certo por caminhos diferentes: `atualizar-manifest.py` da aquametria e da robometria só grava
`atualizado_em` **quando algo mudou de verdade** (`if mudados or titulos or alvo is not None`), e
`medir-palavras-chave.py` da robometria sela a data da **medição**. Pela **31.2** (*"pode acontecer não
basta"*) não há defeito medido fora desta ilha, e a seção **0** do contrato reclama do crescimento dele.
O princípio geral já está escrito na **20.5** e na **32.5-b**. **Se o Raphael discordar, a regra cabe
em três linhas e o lugar é a família da 20.5.**

**O MANIFEST SUBIU PARA A REVISÃO 17, E ISSO NÃO É DESEMBARQUE.** O portão
`atualizar-manifest.py --conferir` reprovou — corretamente — porque `dados/consultas-de-produto.json`
mudou nesta passada; rodei o atualizador e o sha e a revisão acompanharam. **Nada no site muda por
isso:** aquele arquivo é `publicar: false`, e os cinco itens publicáveis seguem com o conteúdo de
29/10. O Sync aplicou a revisão 17 com a mesma tela da 16.

**CONFERIDO NO AR PELA 20.4:** revisão **17** no `/status` às **10h39:48Z**, com as **quatro** linhas
da revisão corrente dizendo `ok`, e `ferramentas/bancada.py --no-ar` aprovando **15 de 15** depois
dela — `conferir-no-ar.py` incluído, que havia reprovado **corretamente** enquanto o manifest local
estava à frente do `/status`.

**E UMA MEDIÇÃO QUE CORRIGE A MINHA PRÓPRIA PREVISÃO, e ela é sobre o cron da 20.6.** Eu escrevi, às
10h39Z, que a tarefa desta ilha venceria *"~10h47"*, somando 30 minutos sobre a passada anterior
(10h17:15). **Ela rodou às 10h39:48 — 22 minutos e 33 segundos depois**, logo após os três GET na
home. Então a leitura de 29/10 (*"o relógio dele não se adianta por GET"*) **não é a história
inteira**: os GET daquela passada não adiantaram nada porque a tarefa ainda não estava vencida; os
desta, sim. **O que está medido, e é só isto:** o intervalo entre duas passadas consecutivas desta
ilha foi de **22,5 minutos**, não 30 — então "30 minutos" é o **nome** do cron (`rodametria_30min`),
não o período medido dele. Quem for prever a hora de um desembarque aqui **visita e confere**, em vez
de somar 30 sobre a última linha do log; a régua da **20.5** continua sendo a certa para decidir se
revisão atrasada é cache ou defeito.

**E ACHEI UM CAMPO MORTO NO CAMINHO, que fica registrado em vez de consertado.** O `manifest.json`
desta ilha traz `atualizado_em: 2026-10-29` e agora diz `revisao: 17` — ou seja, o campo ficou para
trás. Conferi: **nesta ilha ninguém escreve e ninguém lê esse campo** (`grep` em `ferramentas/` e nos
três snippets não acha uma referência); ele veio copiado de ilha irmã no nascimento, e lá ele é escrito
pelo atualizador. É a seção **4** em miniatura — *resumo velho lido como fato* —, e o risco é alguém o
ler um dia como a data da última mudança. **Não mexi na ferramenta de propósito:** a **31.3** proíbe
ampliar portão que já existe enquanto a ilha tiver item de conteúdo aberto na fila, e o 5d está aberto.
Quem pegar o 5d pode resolver em uma linha: ou o atualizador passa a escrever o campo quando bumpa a
revisão (como as irmãs), ou o campo sai do manifest. **As duas são certas; o que não é certo é ele
continuar ali parecendo conferido.**

---

### 3. O PRÓXIMO PASSO DESBLOQUEADO — O BLOCO 5d, E ELE NÃO ESPERA NINGUÉM

Medindo o `wp-sitemap.xml` no ar achei a dívida mais barata e mais atrasada desta ilha: as **5** URLs
publicadas são `/`, `/autonomia-patinete-eletrico/`, `/veiculos/` e as duas filhas. **Não existe
`/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` nem `/privacidade/`**, e a **16.1** nomeia essas
cinco por nome. **A ilha publica link de afiliado da Shopee desde 29/10** — na F2 e nas duas páginas de
produto — sem a página de divulgação que o programa e o leitor pedem.

Ele é o próximo por três razões independentes: **não depende de despacho nenhum** (nem do `gov.br`, nem
do Chrome, nem das etiquetas do ML); pela **21.7** essas páginas **ficam fora do teto** da 21.4, então
não gastam leva de malha; e é **dívida de confiança no ar**. A 21.7 nasceu exatamente deste caso na
aquametria, com a privacidade parada em "aberto" *"com a etiqueta do GA4 no ar e link de afiliado
publicado desde 12/09"*. O "pronto quando" está escrito na fila do `PROMPT.md`.

**A conta da 31.1 desta execução, dita sem maquiar:** ela **não** entregou página nova no ar. Entregou
a lista que fecha três consultas, o despacho que destrava as outras duas, e o conserto de um portão que
reprovava página certa todo dia. **Zero página no ar era o resultado correto aqui** — a 30.8 proíbe
`alvo` desta nuvem —, mas isso não a torna uma entrega da 31.1, e quem contar a proporção conta como
ela é. **O 5d existe para que a execução seguinte não tenha essa conversa:** ele é quatro páginas no
ar sem depender de ninguém.

---

## 2026-10-29 19h1xZ–20h1xZ — **BLOCO 5b: A CONSULTA DO GOOGLE E A CHAVE DA LOJA NÃO SÃO A MESMA PALAVRA** — das seis cabeças do dossiê só **duas** abrem o portão da 30.2, e a causa das outras quatro está medida

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar:
(a) o **despacho do molde da 32.6** segue `FECHADO` nas três ilhas, lido no topo dos três `PROMPT.md`;
(b) nenhum despacho **ALTA** aberto é de ilha *"no ar e quebrada"* — os ALTA de `dados/despachos.md` são
o egresso do `gov.br` (endereçado ao Raphael, não é trabalho da Fundação), o chamado da HostGator da
clubedomosaico (pela **19.4(b)** o próximo passo é chamado, não reparo) e o portão de desembarque que
falta nas outras duas ilhas, que é risco guardado e não página servindo erro. `executando_desde` estava
`null`, que pela **1.1** já significa que não havia bloco da Fundação vivo — reserva escrita às **19h18Z**
(commit `642ac19`), push aceito de primeira, **renovada às 19h37Z e às 19h48Z**. Nenhum branch `claude/*`
à frente do `main` e nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` e o `/status` em **200 nas três passadas**,
com `aquametria.com.br` em 200 nas mesmas três.

---

### O ACHADO, E ELE REORDENA O QUE SOBRA DA FILA

O bloco pedia *"páginas pelo nome do produto (seção 30) para as seis cabeças"*. Antes de escrever uma
linha de página, medi na loja o que cada cabeça devolve — **20 ofertas por chave, nas seis, pela Open
API**. O resultado:

| chave | o que ela devolve nas 20 primeiras |
|---|---|
| `patinete eletrico` | **ZERO** patinete de adulto. Serve `Patinete Elétrico Infantil 150W Rodas 6 Polegadas UNITOYS` e `Moto Elétrica Infantil 6V` |
| `moto eletrica` | **20 de 20** entre brinquedo infantil e peça de caminhão (soquete de painel, relé de pisca) |
| `scooter eletrica` | brinquedo infantil e acessório |
| `bicicleta eletrica` / `bike eletrica` | câmara de ar, pneu, compressor, moto infantil |
| `motos eletricas para adultos` | 18 de capacete e capa de chuva, 2 veículos de adulto com zero venda |

**Com o qualificador `adulto`, a MESMA família devolve produto de verdade:** `patinete eletrico adulto`
→ **16** patinetes de adulto entre **R$ 1.297,13 e R$ 3.399,00**; `bicicleta eletrica adulto` → **5**
e-bikes, três delas com **74, 28 e 25 vendas**.

**A palavra que a pessoa digita no Google e a palavra que acha o produto na loja não são a mesma, e
neste nicho elas divergem por um qualificador.** Por isso cada consulta passou a declarar uma **escada
de chaves**, do degrau mais específico para o mais largo, a escada **para no primeiro degrau que alcança
o piso de três**, e o degrau que casou fica **gravado em cada anúncio** — o mesmo desenho que a
`coletar-piso-de-compra.py` desta ilha já usa pela **25.6(a)**, agora um andar acima. E a exigência da
família é **POSITIVA** (`adulto` declarado no título), nunca negativa.

**DUAS DAS SEIS NASCERAM. AS OUTRAS QUATRO NÃO, COM A CAUSA MEDIDA:**

- `moto eletrica` e `scooter eletrica`: a SERP **autoriza** (alvo, vista com os olhos do Raphael em
  27/10), e o que falta é **produto**. Três anúncios de adulto, **zero venda** nos três, preços variando
  **R$ 6.500** para a mesma classe. O `PROMPT.md` desta ilha já escrevia a regra antes desta medição e
  ela vale: *"na Shopee, scooter e moto elétrica aparecem com 0 vendas e preços incoerentes — não entram
  como recomendação"*. Página que nasce **no piso** com três anúncios sem uma venda sai do ar na primeira
  coleta que perder um. O caminho delas é o Mercado Livre, onde o dossiê mediu 8 de 10 com link
  rastreável — e lá a geração exige clique humano (25.6), o que faz disso **despacho, nunca bloco**.
- `bike eletrica` e `motos eletricas para adultos`: pela **30.4**, mesma intenção de outras duas. O
  sinônimo vive no corpo da página irmã, com a âncora apontando para ela.

As quatro causas estão escritas em `dados/consultas-de-produto.json` e, **em voz de leitor**, no cartão
mudo da mãe — que não é link, pela **16.5**.

### O QUE FOI AO AR

`/veiculos/` (seção de nível 1 da **16.1**, com o nome que o `VOZ.md` já declarava no menu),
`/veiculos/patinete-eletrico/` e `/veiculos/bicicleta-eletrica/`, filhas diretas dela pela **30.1**.
Ordem da **32.2** de cima para baixo: trilha e H1 · caixa de resposta com o preço mediano em Mono ·
bloco de compra com `id="comprar"` logo abaixo · a tabela-resumo **visível** com **todos** os anúncios
(a **seção 7** manda nomear todo item uma vez) · a prestação de contas de quem não entrou, com a causa
contada · a malha da **16.4** também visível, porque é alvo de link e nem todo navegador abre um
`<details>` fechado ao pular para dentro dele · o resto nas dobras da casca · a barra fixa do telefone.

**NENHUM DADO TÉCNICO FOI PUBLICADO, E ISSO É O PRODUTO DA PÁGINA.** Potência nominal, velocidade
máxima, acelerador e carga máxima têm piso de **nível 5** no `niveis_minimos_por_campo` do esquema desta
ilha, e título de anúncio é **nível 6**. Então a coluna diz o que o anúncio **declara** — e a frase que
conta isso é **contada no gerador, em cinco formas**, nunca escrita na prosa: de **16** anúncios do
patinete, **15 declaram um watt** e **1** diz qual watt é aquele. É a tese do `VOZ.md` virando coluna.

### AS TRÊS COISAS QUE QUEBRARAM, E AS TRÊS SÃO DO MESMO TIPO

**1. A RÉGUA RECUSOU QUATRO PRODUTOS CERTOS NA PRIMEIRA PASSADA COM REDE.** O grupo `acessorio`
barrou `Patinete Elétrico 800W Pico 1000W ... Pneu 10" Off-Road` por **`pneu`**, `Patinete Elétrico
Dobrável Adulto com Assento` por **`assento`** e `VYRON Patinete Elétrico Adulto ... Amortecedor` por
**`amortecedor`**. **O título de um veículo nomeia as peças DELE.** E o absurdo que fechou a conta:
`Bicicleta Elétrica Dobrável Adulto com Pneus A Vácuo` **passou**, porque `pneus` no plural não casa com
`pneu` entre bordas — duas páginas certas, uma recusada e uma aprovada **pela letra `s`**. O conserto é a
**regra da posição**: `acessorio` só recusa quando a palavra vem **antes** do substantivo do produto, e o
substantivo é um **campo declarado**, não a primeira posição de uma lista — regra que depende da ordem de
uma lista se desliga em silêncio no dia em que alguém a reordena por estética.

**2. A RECUSA POR PEDAÇO DE PALAVRA.** A primeira versão recusou `Patinete Elétrico Adulto 350W **36V**`
com a causa `infantil`, porque a lista do brinquedo tem `6v` (a bateria do brinquedo) e **`36V` termina
em `6v`**. Mesma família do `grep` que atravessa YAML quebrado: o instrumento responde, e a resposta é
errada. Hoje a busca é por palavra inteira, com os prefixos **declarados um por um** (`eletric`,
`adulto`, `bicicleta`, `patinete`) — e `moto` **não** é prefixo, porque casaria com `motocicleta`,
`motorizado` e `motoca`, três palavras que aparecem em título de acessório e de brinquedo desta coleta.

**3. A MUTAÇÃO `São 2 famílias com página hoje` SOBREVIVEU.** A trava que proíbe número digitado na prosa
declarada cobrava **dois dígitos ou mais**, e a contagem que esta ilha de fato tem é de **um** dígito.
Ela passou a cobrar **qualquer** dígito, com a lista de permitidos nomeando o que escapa (o número da
Resolução Contran é nome próprio de documento, não número de tela) e o resto escrito por extenso. Na
mesma rodada, a trava do número digitado só lia string e lista de string, e as **perguntas frequentes
são lista de dicionário** — ela passava por cima de toda pergunta e resposta sem dizer que não as leu,
que é a cara do portão que aprova em silêncio o que não mediu (**32.5-b**).

**4. DOIS "DEGRAUS" DIFERENTES MORAVAM NO MESMO CAMPO.** Achado relendo o próprio diff, antes de medir
no ar. `degrau_da_escada` do anúncio é o degrau da escada de **chaves** (que palavra achou o produto na
loja); o `degrau` que o cartão da casca lê é o da escada de **compra** da 25.1, e é ele que decide o
rótulo do botão — ficha diz "Ver na Shopee", busca diz "Ver ofertas na Shopee". A vitrine passava o
primeiro no lugar do segundo: **dava o rótulo certo por coincidência** (1 e 1), e daria o errado no dia
em que uma consulta descesse para o degrau 2 da escada de chaves. Agora o degrau de compra vai
**declarado**, e a tabela parou de digitar o rótulo: ele sai de
`rodametria_casca_rotulo_da_loja()`, que é onde ele mora.

**5. A MÃE `/veiculos/` NASCERIA PÁGINA FINA.** Contado antes de medir no ar, com a mesma régua do
`conferir-no-ar.py`: **1.253 caracteres** de corpo contra o piso de **1.500** da seção 8. E o conserto
não foi texto a mais — foram **os três números** que decidem a compra de um elétrico (potência nominal
mais velocidade máxima, watt-hora da bateria, carga máxima declarada), que são o produto desta casa e
estavam faltando justamente na página onde a pessoa escolhe qual família olhar, mais a dobra "Como
sabemos". Corpo em **2.923** caracteres.

### E A BANCADA DENUNCIOU A RÉGUA NOVA NA PRIMEIRA PASSADA, COM RAZÃO

Ela nasceu `relevancia-do-anuncio.py`, que não casa com convenção de nome nenhuma, e a `bancada.py`
escreveu a frase certa: *"ou ele é portão e precisa do prefixo, ou não é e precisa estar fora de
`ferramentas/` — silêncio aqui é portão que nunca roda"*. Virou `teste-relevancia-do-anuncio.py` e roda
a bateria quando chamada sem argumento. **A ilha nasceu com a bancada e foi ela que pegou isto**, não
alguém se lembrando.

### OS PORTÕES

- `bancada.py`: **13 portões** sem rede, **0 falha** (eram 9 antes deste bloco).
- `teste-relevancia-do-anuncio.py`: **25 casos**, 0 falha, todos com título **real** desta coleta, mais
  um **kit fabricado** para a trava `kit_multiplo` poder falhar — nenhuma das 180 ofertas medidas era um
  kit de dois veículos da mesma família, e trava que nunca viu o mundo dela nasce errada sem poder falhar.
- `coletar-por-consulta.py --conferir`: **190 afirmações**, 0 falha, sem rede. Ele reaplica a régua sobre
  os títulos gravados, refaz o número próprio e a contagem de rótulo, e cobra que a chave gravada esteja
  **na escada declarada** e que todo anúncio tenha sido achado por ela.
- `gerar-vitrine-de-produto.py --conferir`: **150 afirmações**, 0 falha.
- `mutacoes-produto.py`: **26 mutações, 26 reprovadas, 0 sobrevivente, 0 inerte**, com trava de alvo
  exato em todas e **três mundos fabricados** que o banco de hoje não produz (foto sem dimensão, página
  abaixo do piso de três, carrossel acima do teto de cinco). Ela roda o mundo **limpo** primeiro: portão
  que reprova tudo não mede nada.
- As **21 fotos** têm largura e altura **lidas no cabeçalho do arquivo na CDN** (1024 × 1024), nunca
  digitadas, e a leitura vem de `coletar-oferta.py` — fato externo se lê de **um lugar só** (seção 8).

### OS NÚMEROS NO AR, MEDIDOS DEPOIS DA REVISÃO 16

- `conferir-no-ar.py`: **APROVADO, 281 afirmações, 0 falha.** Corpo das cinco URLs: **2.586 · 11.246 ·
  3.488 · 9.408 · 6.377** caracteres, todas acima do piso de 1.500.
- `conferir-32-5-no-navegador.mjs` (390 px, Chromium de verdade, quebra de cache): **APROVADO, 3 de 3
  páginas do molde.** Caixa de resposta a **211 px** nas duas páginas novas (teto 700); primeiro botão
  de compra a **1.129 px** no patinete e **1.084 px** na bicicleta (teto 1.400); a F2 segue em 329 e
  1.380 px. Rolagem horizontal **0** e **0** erro de JavaScript nas três.
- Na página do patinete: **21** links `sponsored`, **ItemList com 16 itens**, **FAQPage com 4
  perguntas**, **BreadcrumbList de três níveis** (`Início › Veículos › Patinete elétrico`), 4
  `<details>` e 5 imagens com `width`/`height`.
- **O portão de pixel lista `/veiculos/` e a home como FORA DO MOLDE**, e isso é registro e não
  aprovação em silêncio: as duas não têm formulário nem bloco de compra. Para a home é decisão
  registrada (nasceu HUB); para a mãe é porque a **32 não nomeia uma família de página de LISTAGEM** —
  ela tem FERRAMENTA (32.1) e FICHA/RESPOSTA (32.2) e mais nada. Duas ilhas já têm página de listagem
  (`/materiais/` da clubedomosaico e esta). **Fica anotado para a leitura semanal; não inventei regra.**

### A LEITURA SEM QUEBRA DE CACHE, E O QUE ELA ACHOU NÃO É DESTA ILHA

As três URLs novas em **200 nas duas leituras**. E a sonda **virgem** — caminho carimbado com o relógio,
que nunca existiu — devolveu **404 · 200 · 200 · 200**, com o corpo do 404 servido em HTTP **200** e o
`<title>Página não encontrada – Rodametria</title>`. **É o mesmo soft 404 na borda que a clubedomosaico
registra há oito medições**, agora medido numa **segunda conta do mesmo hospedeiro** — e isso é o dado
que faltava ao chamado: até hoje ele só havia sido medido num domínio, o que deixava aberta a leitura de
que fosse configuração daquela conta. Esta ilha tem **dois dias de vida** e nunca recebeu uma linha de
configuração de cache. Linha acrescentada ao despacho **ALTA** de `dados/despachos.md`, afirmando **só
sobre a ilha que esta execução reservou**, como a lição de 14/09 daquele arquivo manda. **Não se
conserta daqui.**

### O DEFEITO QUE A ENTREGA ACHOU NO AR, E ELE É A SEÇÃO 4 EM FORMA DE INSTALADOR

A **revisão 13** subiu os arquivos e **não criou as três páginas**. A instalação da casca rodava uma vez
por **versão da casca**, e a revisão 13 subiu casca nova **e** o snippet da página nova na **mesma
passada do Sync**: quando o `init` chamou a instalação, o snippet novo ainda **não estava carregado**
naquela requisição — então o filtro `rodametria_instalar` dele não existia, as três páginas não nasceram,
e a casca gravou `instalado: 1.3.0`. **Com a versão já marcada, a instalação nunca mais rodaria.**

**E o sintoma era verde em todo lugar:** `/status` em **13**, as **cinco** linhas do log da revisão
dizendo `ok`, e `/wp-json/rodametria/v1/casca` já listando `veiculos`, `patinete-eletrico` e
`bicicleta-eletrica` no mapa de páginas — **com `url` vazia nos três** — e `wp-sitemap.xml` com **duas**
URLs. O relato gravado tinha duas linhas, `home` e `f2`, e **nenhuma vermelha**. Quem lesse o log do
desembarque pela 20.4 e parasse ali teria escrito "entregue".

A casca subiu para **1.4.0**: a instalação roda de novo quando a **assinatura do mapa** muda — os slugs
do mapa, em ordem, num texto só — e não só quando a versão da casca muda. Com isso **página nova nasce
no dia em que o snippet dela entra, sem ninguém tocar na versão da casca**, que é o que o comentário do
mapa promete desde a revisão 3: *"a casca não é editada quando a ilha cresce"*.

A casca também subiu de 1.2.1 para 1.3.0 por **duas razões de árvore**, as duas da **16**:
`garantir_pagina()` passou a aceitar **pai** (16.2: página sem pai é defeito e não publica), e
`url_do_slug()` passou a achar a página pela meta `_rodametria_id` **em vez de por caminho** —
`get_page_by_path()` casa o caminho **inteiro**, e no dia em que a árvore ganhou um nível ele devolveria
nulo para a filha, com `casca_link()` transformando link vazio em texto **sem reclamar**: página no ar,
órfã, com a mãe apontando para texto morto e nenhum portão vermelho.

---

## 2026-10-29 16h2xZ–16h4xZ — **BLOCO 3e: A PREMISSA DELE ESTAVA ERRADA**, e a coleta que não deu em campo técnico nenhum achou um defeito **no ar** — o bloco de compra dizia a mesma coisa **três vezes** e a página de autonomia estava **calada sobre autonomia**

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar:
(a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas — aquametria 21/10 18h2xZ,
clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ, lidos no topo dos três `PROMPT.md`; (b) o único
despacho marcado **ALTA** aberto no arquipélago é o **ITEM 1 da ronda de 28/10 da clubedomosaico** (58
links de afiliado sem piso), e ele **não fura o foco**: a 1.2 exige ilha *"no ar e quebrada — página
servindo erro, ferramenta devolvendo número errado, site fora do ar"*, e a régua técnica daquela ronda
**passou inteira** (32 de 32 em HTTP 200, console limpo, as duas ferramentas com a conta refeita na mão).
É defeito grave de banco, não de página servida. `executando_desde` estava `null`, que pela **1.1** já
significa que não havia bloco da Fundação vivo. Reserva escrita às **16h25Z**, commit `fb97851`, push
aceito de primeira, e **renovada às 16h37Z**. Nenhum branch `claude/*` à frente do `main` e nenhum PR
aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` em **200 nas três passadas**, com
`aquametria.com.br` e `robometria.com.br` em 200 nas mesmas três.

---

### A PREMISSA DO BLOCO ESTAVA ERRADA, E CORRIGI-LA FOI A ENTREGA MAIOR

A fila pedia *"coleta em ficha de fabricante — o nível 4 da escada, hoje vazio"*. **Ele não está vazio
por falta de tentativa: pode ser vazio por estrutura.** Remedido pela **20.3** às 16h2xZ, três passadas
cada, com controle verde e a causa lida no `__agentproxy/status` em vez de suposta (`connect_rejected`,
403 de política no CONNECT): `honeywhale.com`, `maxshot.com.br`, `kenda.com.br`, `sousabike.com.br` e
`evoo.com.br` em `000`. **Mas o egresso não é a causa raiz** — e é isso que muda o plano de quem ler
isto. As duas marcas principais do banco **não têm site de fabricante achável**: a Honeywhale vende por
vitrine de marketplace e varejo mexicano, a MAXSHOT só aparece em varejista brasileiro. **Abrir os cinco
domínios não encheria este nível.** São marcas *de* marketplace, não fabricantes com página própria no
Brasil.

**E O GARGALO TEM NOME, UM SÓ, E ELE NÃO É DESTA ILHA: o nível 5 está atrás do egresso.**
`www.casasbahia.com.br`, `www.extra.com.br` e `www.magazineluiza.com.br` em `000` nas três passadas;
`www.mercadolivre.com.br` em `403` do próprio anti-robô, com o CONNECT passando (egresso aberto e caminho
fechado são coisas diferentes). A leitura por **BUSCA** — a única porta aberta — alcança os níveis **6, 7
e 8**, que são **exatamente** os que `niveis_minimos_por_campo` recusa nos quatro campos do nível 5.
**Consequência escrita sem maquiar: `potencia_nominal_w`, `velocidade_max_kmh`, `acelerador` e
`carga_max_kg` não são colhíveis desta nuvem por caminho nenhum.** A F1 e a F3 não vão ao ar por coleta —
vão por **abertura**. O despacho ALTA de `dados/despachos.md` deixou de ser "seria bom" e passou a ser o
único caminho.

**O QUE A BUSCA ACHOU E FOI RECUSADO**, escrito no esquema (versão 4) registro a registro, para a próxima
execução não gastar a mesma busca — porque o que foi procurado e não achado é dado:

| achado | fonte | nível | por que não entrou |
|---|---|---|---|
| variante de **350 W** do M2 MAX | loja estrangeira de catálogo | 8 | nível 8 não sustenta campo **nenhum**. E a informação é boa: existe variante de potência com o MESMO nome de modelo |
| **36 V** de bateria | publicador editorial | 7 | nunca sustenta campo técnico — e é do **MAX-B**, justamente o aparelho que as travas do casamento barraram por ser outro |
| **25 km/h** e **120 kg** | guia de compra | 8 | os dois campos exigem nível 5. A oferta casada diz 32 km/h (nível 6): **a divergência é ela mesma a prova de que aceitar uma seria sorteio** |
| **bico** da câmara Kenda 16x3.0 | — | — | **não publicado em porta nenhuma alcançável**. A busca devolveu Schrader para 16x1.5/2.25 e 16x1.75/2.125, que são linhas de bicicleta: herdar o bico de outra largura é especificação herdada, proibida |

**O ÚNICO CAMPO QUE SOBROU COLHÍVEL FOI COLHIDO:** `autonomia_declarada_km` = **22 km** no
`honeywhale-m2-max`, lido no título da **própria oferta casada** (20299836765) e não de oferta vizinha.
A oferta foi **remedida na Open API às 16h3xZ**: viva, R$ 2.299, 3 vendas, título literalmente idêntico ao
colhido às 13h3xZ. Nível 6, que a escada aceita neste campo com a razão escrita (o erro caro aqui é uma
faixa de km larga, não uma pessoa na rua sem habilitação). **E a medição tem uma metade negativa que vale
tanto quanto: dos 10 títulos que a resposta devolveu, ZERO declara tensão ou amperagem.** Não é que a
leitura falhou — é que a bateria não está publicada nesta porta.

---

### O DEFEITO NO AR QUE A COLETA ACHOU: TRÊS CÓPIAS DE UM FATO, E ZERO DO FATO QUE A PÁGINA RESPONDE

Medido às 16h3xZ em `/autonomia-patinete-eletrico/`, com quebra de cache. O bloco de compra dizia **a
mesma coisa três vezes na mesma tela**:

1. o parágrafo de abertura: *"Nenhum destes entrou pela conta de Wh: a ficha deles não declara tensão nem
   amperagem"*;
2. a linha `bateria não declarada` dentro de cada cartão (4 ocorrências, uma por cartão);
3. o rótulo do grupo do cartão: `a ficha não declara a bateria`.

**E o cartão da página de AUTONOMIA não dizia uma palavra sobre autonomia** — enquanto a oferta que o
botão dele abre declara, no próprio título, **22 km**. Três cópias de um fato, e zero do número que a
página existe para responder, gastando a primeira tela que a 32.5 mede em pixel.

**Consertado nas três pontas:**

- **a autonomia entra no cartão PRIMEIRO**, com a atribuição ao lado — e a atribuição **não é digitada**:
  `quem_declara()` a alcança pelo caminho que o próprio banco grava (o campo diz qual `fonte` o sustenta,
  a fonte diz o `nível`, e o nível diz `na_tela.quem_declara` na escada do esquema). O dia em que a escada
  mudar a palavra, o cartão muda com ela. Número de nível 6 na tela **sem dono** é promessa da ilha;
- **a linha duplicada saiu.** O cartão serve `V × Ah` quando existe e **cala** quando não existe, porque
  o rótulo do grupo logo abaixo já é literalmente aquela frase;
- **a frase de abertura deixou de ser string digitada no PHP** e passou a ser derivada da contagem da
  vitrine, em `gerar-f2.py`.

**ESSA ÚLTIMA É A 32.5-d OUTRA VEZ, EM OUTRO MATERIAL, E É A LIÇÃO DO DIA.** *"Nenhum destes entrou pela
conta de Wh"* era uma **afirmação sobre o estado do banco** escrita à mão dentro do snippet, que nenhum
portão conferia. Ela é verdadeira hoje **por falta de dado que a contradiga**: no dia em que um registro
declarasse V e Ah com oferta aberta, o cartão entraria em `cabem_no_wh` e o parágrafo acima dele
continuaria dizendo que nenhum entrou — mentindo calado, com cara de conferido. É a mesma família do
comentário de CSS que declarava economizar 52 px e nunca economizou um, e do número de tela digitado.
**Prosa que afirma o estado do banco é número digitado em outro traje.** As **cinco** frases da função
nova são conferidas sobre mundos **fabricados** dentro do próprio gerador — vitrine de 1 e de 4, com 0
cabendo no Wh, com todos e com parte —, não só a que o banco de hoje acende. Singular e plural inclusive:
*"O único com oferta aberta hoje"* contra *"Nenhum dos 4"*.

**NENHUM PORTÃO NOVO NASCEU, e é decisão e não esquecimento:** a **31.3** proíbe ampliar portão enquanto a
ilha tiver item de conteúdo ou de página pelo nome do produto aberto na fila, e os blocos 4, 5, 5b e 6
estão abertos. Os mundos fabricados moram dentro do gerador que já existia e não custaram arquivo novo.

---

### CONFERIDO NO AR (18.4), REVISÃO 12

- `/status` em **12**, igual ao `manifest.json`, com as **duas** linhas da revisão 12 dizendo `ok`, lidas
  uma por uma (**20.4**). Registro, não aprovação: a janela do log tem 15 linhas e está **cheia**, então
  item que rolou para fora dela não foi conferido.
- `conferir-no-ar.py`: **138 afirmações, 0 falha**.
- **32.5 no navegador, a 390 px reais, com o portão descobrindo as páginas no `wp-sitemap.xml`:**
  formulário **329 px** (teto 700) e primeiro botão de compra **1.380 px** (teto 1.400). A home segue
  **fora do molde** com o motivo impresso (não tem bloco de compra), caixa de resposta a 331 px.
- **E o botão SUBIU 5 px com uma linha A MAIS no cartão** (era 1.385). A causa é aritmética de texto: a
  frase de abertura derivada tem 145 caracteres contra 175 da digitada, e devolveu uma linha acima dos
  cartões. Tirar a repetição pagou a linha que a autonomia custou, com 5 px de troco.
- Texto servido, contado com quebra de cache: `22 km declarados pelo vendedor` **1**,
  `bateria não declarada` **0** (eram 4), `Nenhum destes entrou pela conta de Wh` **0** (era 1),
  `Nenhum dos 4 com oferta aberta hoje` **1**.
- **Bancada: 9 portões sem rede, 0 falha.** Snippet F2 **1.2.0 → 1.3.0**.

**E O PIXEL FOI PREVISTO ANTES DE IR AO AR, por um método que vale guardar.** A **32.5-d** manda conferir
no navegador quem acrescenta dado novo ao cartão, e com 15 px de folga sobre o teto eu não queria descobrir
isso *depois* do desembarque — nesta ilha cada revisão custa uma espera de Sync. Baixei o HTML servido,
troquei **as duas frases** num espelho local e medi o espelho a 390 px. **O método se valida contra o
número que o portão já mediu na origem:** o espelho *antes* deu **1.385 px**, idêntico ao que o portão
havia medido, e o espelho *depois* previu **1.380 px** — que foi exatamente o que o portão mediu no ar
depois da revisão 12. Espelho não substitui portão (o portão mede a **origem**, com o CSS e a fonte que o
site serve); ele diz, de graça, se vale gastar uma revisão.

---

### O ACHADO DE MÉTODO, E ELE MUDA O CUSTO DE TODA EXECUÇÃO NESTA ILHA

**O CRON DO SYNC NÃO RODA POR RELÓGIO: RODA POR VISITA.** O `ESTADO.md` e o `PROMPT.md` desta ilha dizem
que o Sync tem *"cron próprio de 30 minutos"* e que a Fundação, sem o token, **"empurra e espera"** — a
execução da manhã registrou que isso custou **nove esperas de cron** entre 10h44Z e 12h10Z.

**Medido às 16h3xZ:** o log do `/status` trazia disparos às 11h39, 12h09, 13h56 e 14h09 — e depois **nada
por 2h29**. E 14h12Z é exatamente o minuto em que a execução anterior fechou e **parou de abrir o site**.
É WP-Cron: ele é acionado por **requisição**, não por um relógio no servidor; sem visita, a ilha não
desembarca, por mais que a agenda diga 30 minutos. Três GETs na home às 16h38Z e o `wp-cron.php`
respondendo **409** (já havia cron em andamento) — a revisão 12 entrou em **um minuto**.

**A regra, e ela cabe numa frase: a Fundação não espera o cron nesta ilha — ela o aciona, abrindo a
própria página, e não precisa do token para isso.** Nove esperas de cron eram evitáveis, e a frase
"empurra e espera" estava certa sobre o token e **errada sobre o relógio**.

---

### O QUE FICA ABERTO

1. **A bateria do M2 MAX não está publicada em porta nenhuma alcançável** (0 de 10 títulos da Open API).
   Enquanto nenhum registro com oferta aberta declarar V e Ah, `cabem_no_wh` fica vazio e o bloco de
   compra continua dizendo o que os cartões **são** em vez do que a conta escolheu. Está na tela, com a
   causa. **Não é defeito.**
2. **A leitura sem quebra de cache** (como o Google lê) segue não feita — terceira execução seguida.
   Toda URL desta passada foi pedida com `?v=<agora>`, então as afirmações são sobre a **origem**. O
   portão que mede a borda existe na clubedomosaico (`leitura-do-visitante.py`) e não aqui, e a **31.3**
   proíbe abri-lo enquanto houver item de conteúdo e de página pelo nome do produto na fila.
3. **O despacho ALTA do egresso** (gov.br para a F1; casasbahia, extra e magazineluiza para o nível 5)
   está remedido hoje e **continua recusado**. Ele é agora o único caminho para a F1 e a F3.

**PRÓXIMO PASSO: o bloco 5b — página pelo nome do produto (seção 30).** Ele é o próximo por **eliminação
medida**, não por ordem de lista: o 3e provou que coleta não destrava mais nenhuma ferramenta desta ilha;
o bloco 4 pede ferramenta nova e as duas que faltam estão travadas por dado que não se colhe daqui; o 5
pede artigo-âncora **pareado** com ferramenta, e só há uma no ar. O 5b não depende de nenhum dos três — as
seis cabeças estão medidas, a SERP delas está medida e **não tomada**, e a ilha tem 4 registros publicáveis
com piso e 1 com ficha. A ilha tem **2 URLs** contra as 40 do piso da 21.1. Primeiro passo: ler a seção 30
inteira e a 21.4 (teto de leva por semana) **antes** de escolher quantas páginas, e escolher a primeira
cabeça pela intersecção entre volume e o que o banco sustenta — hoje `patinete eletrico`, a única das seis
com registro de ficha aberta nesta ilha.

---

## 2026-10-29 13h3xZ–14hxxZ — **BLOCO 3d: A ILHA TEM A PRIMEIRA FICHA DE PRODUTO DA HISTÓRIA DELA**, com foto medida e preço de hoje na tela. E o bloco mediu o que vale mais que a ficha: **13 dos 17 registros não têm com o que pedir uma** — e isso não se conserta com trava mais frouxa

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar:
(a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas — li o topo dos três `PROMPT.md`
(aquametria 21/10 18h2xZ, clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ); (b) **nenhum despacho
marcado ALTO** existe em ilha no ar e quebrada — procurei o rótulo nos três arquivos e não há. O despacho
da Sentinela de 28/10 nesta ilha foi **reescrito pela 18.3** na execução da manhã e o único item que
sobrou é a **conta da 31.1**, cujo `pronto quando` é a leitura semanal recontar — ele diz, com todas as
letras, que *"o caminho é a fila andar, não uma correção"*. `executando_desde` estava `null`, que pela
**1.1** já significa que não havia bloco da Fundação vivo; o último commit da ilha era de **12h13Z**, 82
minutos antes. Reserva escrita às **13h36Z**, commit `f9e138d`, push aceito de primeira, e **renovada às
13h59Z** pela 1.1. Nenhum branch `claude/*` à frente do `main` e nenhum PR aberto.

**A REDE, MEDIDA E NÃO HERDADA (20.2).** `rodametria.com.br` e `www.rodametria.com.br` em **200 nas três
passadas**, com `aquametria.com.br` em 200 nas mesmas três. E a fonte que este bloco precisava foi medida
antes de qualquer regra exigi-la, pela **20.3**: `open-api.affiliate.shopee.com.br` em **200 nas três**, e
`cf.shopee.com.br` — a CDN de onde a dimensão da foto sai — em 200.

**A CREDENCIAL.** `SHOPEE_APP_ID` e `SHOPEE_SECRET` conferidos **por presença e nunca por valor**, e os
dois **estavam no ambiente do processo** desta execução. Não foi preciso passar valor nenhum em linha de
comando, e não se deve: linha de comando fica visível na lista de processos da máquina. `git grep` pelo
NOME dos dois campos antes de empurrar: zero ocorrência no que foi commitado.

---

### 1. O QUE FOI AO AR, E É A METADE VISÍVEL DO BLOCO

`honeywhale-m2-max` **casou no DEGRAU 1 da 25.1** e o primeiro cartão do bloco de compra da F2 passou a
servir, em `/autonomia-patinete-eletrico/`:

- a **foto de verdade** (`cf.shopee.com.br/...`, 1024×1024), no lugar do espaço reservado;
- o **link da ficha** como botão, com o rótulo mudando de *"Ver ofertas na Shopee"* (degrau 4) para
  *"Ver na Shopee"* — a casca já fazia essa distinção e nunca tinha tido um registro para exercê-la;
- a linha discreta **"Veja todos disponíveis aqui"** logo abaixo do botão, que é a 25.2 ao pé da letra:
  *"quando existir e estiver viva, ela vira o botão e a busca desce para a linha discreta"*. A busca
  **não sai** — ficha apodrece e busca não;
- o **preço de hoje**: R$ 2.299, lido pela Open API em 29/10, com a data ao lado. Era de 27/10, do painel.

O componente da linha discreta mora na **CASCA** e não no snippet, pela **32.6-b**. O `conferir-no-ar.py`
passou a ler `bloco de compra: 4 cartão(ões), degrau(s) [1, 4]` — antes era só `[4]`.

---

### 2. AS TRAVAS DA 25.7 TRABALHARAM, E O NÚMERO ESTÁ GRAVADO NO BANCO

**10 ofertas julgadas, 6 barradas.** Quatro eram **`M2 MAX-B`**, que é outro patinete (armadilha 4 — *"o
sufixo faz outro aparelho"*), e duas enumeravam **`M2 Pro,M2 MAX,M2 MAX-B modelos da série`** (armadilha
5 — *"no máximo um está certo, e não há como dizer qual, então os dois caem"*). Os seis motivos estão em
`afiliado.candidatos_barrados`, em português, dentro do registro.

**E AQUI ESTÁ A PROVA DE QUE A RÉGUA NÃO ESCOLHE PELO NÚMERO BONITO:** a oferta de **maior venda** da
resposta inteira — 12 vendas, nota 4,9, na `HONEYWHALE BRASIL` — **foi barrada**, porque é o MAX-B. A
escolhida tem **3 vendas**. Dar o primeiro lugar da vitrine ao anúncio mais vendido teria sido recomendar
um produto que a página não descreve, e é o que a 25.4-b.1 chama de pior que casamento nenhum: *"parece
dado"*.

**O casamento foi conferido COM OS OLHOS antes de gravar**, como a 25.3 manda: oferta `20299836765`,
título *"HONEYWHALE M2 MAX Patinete Elétrico Adulto, 500W Scooter Eletrica, 32KM/H Velocidade, 22KM
Autonomia"*, loja `HONEYWHALE BRASIL`, preço **único** (2299/2299). O registro declara Honeywhale M2 MAX,
500 W, 32 km/h. Bate campo a campo.

**A FOTO É MEDIDA, NUNCA SUPOSTA (25.7):** 1024×1024 lidos do **cabeçalho do arquivo** na CDN, nos
primeiros 32.768 bytes, e o registro grava `como_a_dimensao_foi_medida`. Dimensão digitada é da família do
número de tela digitado — parece conferida.

---

### 3. O ACHADO QUE VALE MAIS QUE A FICHA: **13 DOS 17 REGISTROS NÃO TÊM IDENTIDADE PARA PEDIR UMA**

As três causas de "não casou" saem **separadas**, pela **25.4-b.4**, e a **25.9** mediu o que custa
contá-las juntas: na Aquametria o número `12` foi lido como mercado **quatro vezes seguidas**, e a quinta
medição — item por item, degrau por degrau — achou `9 de mercado + 2 barrados com razão + 1 defeito nosso`.

| causa | quantos | o que a resolve |
|---|---|---|
| **casou** | 1 | — |
| **mercado_nao_anuncia** | 3 | só o mercado mudar |
| **candidato_barrado** | 0 | dado melhor no registro, nunca trava mais frouxa |
| **sem_identidade_minima** | 13 | **colher o campo que falta** |

**`mercado_nao_anuncia` foi medido até o fim, e não presumido.** `MAXSHOT V1`, `MAXSHOT V1SPRO` e
`Honeywhale H3` devolveram **zero em todos os degraus da escada**, e — porque a 25.9 exige que a recusa
seja separada da ausência — medi também as **variantes do nome**: `MAXSHOT V1S`, `MAXSHOT V1S Pro`,
`MAXSHOT patinete eletrico`, `Honeywhale H3 patinete`. Zero em todas. E a chave **`MAXSHOT` sozinha**
devolveu película de Zenfone Max Shot e suplemento Action Max; **`Honeywhale` sozinha** devolveu bolsa
frontal e pneus de *outros* modelos da marca (M2 Pro, M1 Lite). É a armadilha 3 da 25.7 remedida nesta
ilha: *"código de modelo é curto e o mundo é grande"*. **O H3 tem casa, e ela está fora do alcance desta
máquina:** o `titulo_colhido` dele diz *"anúncio Mercado Livre"*, e o degrau 2 — a página `/p/MLB...` —
depende do gerador do ML, que tem reCAPTCHA (25.5). Pela 25.2 isso nunca trava página: é oportunidade.

**E os 13 sem identidade são o retrato do mercado desta ilha.** Dez veículos não declaram `modelo` (ou
`marca`): `Sousa Bike`, `Siena`, `PLAYBIK`, `Verdevento`, `Evoo`, `Haixia`, `LS Sport` têm marca e nenhum
modelo; `L40 Plus` e `X13` têm modelo e nenhuma marca; `scooter-chopper-1000w-48v` não tem nenhum dos
dois. **É a mesma medição do bloco 3c por outro ângulo:** *"o que nomeia marca e modelo é achável na loja
e não publica ficha; o que publica `60 V 20 Ah` empacota três nomes no título e não é achável por nome
nenhum"*. O 3c viu isso no eixo do PISO; o 3d vê no eixo da FICHA, e a conclusão é a mesma — **o que falta
nesta ilha é coleta em ficha de fabricante (nível 4 da escada, hoje vazio)**, não link.

**A CÂMARA KENDA É A 25.9 EM FORMA NOVA, e é o achado mais fino do bloco.** A medida `16 x 3.0` casa com
**dez ofertas**, e o mercado as separa pelo **BICO** — `bico torto curvo`, `bico curvo`, `bico grosso
33mm`. São produtos que **não se substituem na roda de ninguém**, e o registro **não declara bico**.
Escolher uma ficha ali afirmaria uma válvula que o banco nunca leu, e mandaria a pessoa comprar a peça
errada. **Aqui a BUSCA é literalmente melhor que a ficha**: ela mostra as três e deixa a pessoa escolher,
que é para isso que o piso existe. O registro fica no degrau 4 com o motivo escrito, e a dívida tem nome e
é de DADO: `bico`. A 25.9(1) já diz a regra — *"o conserto é do DADO, nunca da trava"*. O esquema passou a
declarar, por tipo de peça, **qual atributo o mercado usa para distinguir** (`camara` e `pneu` → `bico`;
os outros `null`, e `null` ali é declaração e não ausência).

---

### 4. O QUE A BANCADA PEGOU DE MIM, ANTES DO AR

**`validar-banco.py` reprovou a primeira versão deste bloco**, com a frase exata: *"veiculo
honeywhale-m2-max: cotacao aponta a fonte 'open-api-afiliados', que nao esta em fontes{}"*. Eu gravei uma
cotação citando uma fonte que não declarei. **A regra que o bloco 3 escreveu pegou um defeito do bloco
3d** — e é exatamente o que um portão de dado existe para fazer. A régua passou a **declarar a própria
fonte** antes de qualquer campo citá-la, no **nível 6**, e a escada do esquema diz por que: *"o nível é o
do ELO MAIS FRACO entre autoria, custódia e leitura"*. A leitura aqui é **melhor** que a do
`painel-shopee` — é mecânica, sem ninguém transcrevendo número à mão —, mas a **autoria continua sendo o
vendedor do anúncio**. Logo 6: sustenta preço, disponibilidade e o nome comercial, e **não** sustenta
campo técnico que a F1 leia.

**E um veredito certo com a frase errada, que eu só vi porque leio o que a régua escreve.** O anúncio que
enumera a série era barrado pela trava do sufixo, dizendo *"o modelo vem seguido de `m2`, que é sufixo de
modelo"* — e `m2` ali **não é sufixo**: é o começo do modelo **seguinte** da lista. A recusa estava certa e
a explicação estava errada, e a explicação é o que a execução seguinte lê **dentro do banco**: ela mandava
consertar a coisa errada. A enumeração ganhou **trava própria** (`trava_enumeracao_da_serie`), que recusa
pelo motivo verdadeiro — o modelo aparecendo mais de uma vez no título. É a mesma família do motivo que
envelhece calado da 25.4-b.3.

---

### 5. E O DEFEITO QUE SÓ A PRIMEIRA FOTO DA ILHA PODIA REVELAR — 32.5-c, POR ESPECIFICIDADE

**A revisão 10 subiu e o portão de pixel REPROVOU:** o primeiro botão de compra foi de **1.385 para 1.471
px**, 71 acima do teto de 1.400 da 32.5. Medi no navegador a 390 px em vez de deduzir, e os números são:
**espaço reservado 96 px, foto 182 px**.

**A causa não era a foto ser grande: era de SELETOR.** `body.rdm img{max-width:100%;height:auto}` vale
**(0,1,2)** e vence `.rdm-molde-cartao-foto`, que vale **(0,1,0)** — então o `height:auto` daquela linha
mandava na foto e a altura do molde era simplesmente ignorada. **É a família que a 32.5-c nomeou** (*"a
folha do snippet redecorava a caixa do molde, vencendo-a por ordem de carga"*), aqui por especificidade. E
foi invisível por um motivo que vale guardar: **enquanto nenhum registro da ilha tinha foto, a regra da
foto nunca rodou contra uma foto de verdade.** O espaço reservado escondeu o defeito justamente porque
**não é um `<img>`** — a regra que o vencia não o alcançava. Conserto por especificidade (`body.rdm` no
seletor da foto), **sem `!important`**: `!important` esconderia a disputa em vez de resolvê-la.

**E no caminho, um número que o arquivo afirmava e a página não servia.** A linha
`.rdm-molde-cartao-sem-foto{height:44px}` estava **MORTA**: a regra de 96 px vem depois dela no mesmo bloco
de telefone, com a mesma especificidade, e vencia. O comentário dela — escrito há **três horas**, na
execução da manhã — dizia *"44 px em vez de 96, porque no telefone esses 52 px são do espaço mais caro da
página"*. **Os 52 px nunca foram economizados, e a medição de 1.385 px daquela manhã foi feita com 96.**
Afirmação em comentário não é medição: é da família do número de tela digitado, e parece conferida. A
linha saiu e a medição ficou escrita no lugar dela.

---

### 6. OS PORTÕES, E O QUE ELES NÃO PROMETEM

- **Bancada sem rede: 9 portões, 0 falha** (`mutacoes-banco`, `mutacoes-piso`, `teste-f2`,
  `validar-banco`, `atualizar-manifest --conferir`, `coletar-oferta --conferir`,
  `coletar-piso-de-compra --conferir`, `derivar-banco --conferir`, `gerar-f2 --conferir`).
  `coletar-oferta.py --conferir` nasceu com **82 afirmações sobre o que está escrito** e entrou na bancada
  pela convenção de nome, sem ninguém o listar.
- **`conferir-no-ar.py`: 138 afirmações, 0 falha** (eram 134), medido na **revisão 10**.
- **O portão de pixel da 32.5 na revisão 11: APROVADO, medido às 14h1xZ depois do cron.** Formulário a
  **329 px** (teto 700) e primeiro botão de compra a **1.385 px** (teto 1.400) — **exatamente o número de
  antes da foto existir, agora COM a foto na tela**. E a prova do conserto é a altura medida no navegador:
  **foto 96 px, reservado 96, 96 e 96** — os quatro cartões com 343 px cada. A afirmação que o esquema faz
  (*"o reservado tem a MESMA altura da foto, então foto que entra não muda a altura do cartão"*) era falsa
  quando eu a escrevi e passou a ser verdadeira por construção. Rolagem horizontal 0, zero erro de JS.
- **E `conferir-no-ar.py` rodou de novo na revisão 11: 138 afirmações, 0 falha**, com a linha do log da
  revisão corrente dizendo `ok` (20.4).
- A **home** segue `fora do molde` com o motivo impresso, como no parágrafo acima: é o estado dela, não
  uma reprovação desta entrega.
- **20.4, o log lido linha por linha:** as três linhas da revisão corrente dizem `ok`. Os **4 aguardando
  desembarque** são os itens de `publicar: false` (constantes, veículos, peças, esquema) — estado de
  propósito, conferido no `manifest.json`, não entrega que falhou. E a janela do log tem **15 linhas e está
  CHEIA**: item que rolou para fora dela **não foi conferido**, e isso é registro, não aprovação.
- **O que NÃO foi medido, e segue não sendo:** a leitura **sem quebra de cache** (como o Google lê). Toda
  URL desta execução foi pedida com `?v=<agora>`, então as afirmações são sobre a **origem**. A
  clubedomosaico tem o portão que mede a borda (`leitura-do-visitante.py`); esta ilha não.
- **A HOME continua FORA DO MOLDE**, pelo mesmo motivo de ontem e com o motivo impresso pelo portão: não
  tem bloco de compra (a caixa de resposta dela está a 331 px, dentro do teto). Ela ganha isso no dia em
  que a F1 puder nascer nela.

---

### 7. O PRÓXIMO PASSO DESBLOQUEADO

**Não é mais o 3d, e não é mais link: é COLETA DE FICHA DE FABRICANTE — o nível 4 da escada, hoje vazio.**
Os dois eixos do banco (3c pelo piso, 3d pela ficha) convergiram no mesmo lugar: o que falta aos 13
registros é **`marca` + `modelo` lidos numa ficha**, e isso não sai de anúncio de marketplace, que é o
nível 6 de onde o banco inteiro vive. **E o primeiro passo dele é a 20.3 outra vez** — medir o egresso
contra os domínios dos fabricantes **antes** de escrever regra que os exija. Nenhum domínio de fabricante
foi tentado nesta ilha até hoje.

**O alvo apertado, com nome:** `MAXSHOT` (V1 e V1SPRO) e `Honeywhale` (H3) têm marca e modelo e o mercado
da Shopee não os anuncia — ficha de fabricante resolveria o campo técnico mesmo sem oferta. E os dez sem
`modelo`/`marca` precisam do nome antes de qualquer outra coisa.

**E O PRIMEIRO PASSO DO 3e FOI DADO NESTA EXECUÇÃO, porque é um comando — e ele INVERTEU o plano do
bloco.** A 20.3 manda medir o egresso antes de escrever regra que exija a fonte, e a medição desmentiu a
suposição de que o que falta é ficha de **fabricante**:

- **Nenhuma das duas marcas principais tem site de fabricante achável.** A Honeywhale é vendida por loja
  de marketplace — a própria *"loja oficial"* dela é uma vitrine do Mercado Livre — e por varejo mexicano;
  a MAXSHOT aparece **só** em varejista brasileiro. **Para este nicho o nível 4 da escada pode ser
  estruturalmente VAZIO:** são marcas de marketplace, não fabricantes com página própria no Brasil. Isso
  não é um bloqueio a remover, é uma **premissa a corrigir**.
- `honeywhale.com`, `maxshot.com.br`, `kenda.com.br`, `sousabike.com.br` e `evoo.com.br`: **`000` nas três
  passadas**, `connect_rejected` — *policy denial* lido no status do proxy, não suposto.
- **O que vale pedir são TRÊS domínios de VAREJO GRANDE**, porque eles são textualmente o **nível 5** da
  escada desta ilha e o nível 5 *"sustenta campo técnico atribuído à LOJA"*: `www.casasbahia.com.br`,
  `www.extra.com.br` e `www.magazineluiza.com.br`, os três `connect_rejected`. A ficha da Casas Bahia
  declara, para o `V1SPRO`, **500 W, carga máxima de 120 kg e certificação UL 2272** — e `carga_max_kg` é
  a **entrada da F3**, que hoje não vai ao ar por falta exatamente desse campo em registro com oferta.
- `www.mercadolivre.com.br` devolveu **403**, e ele **não** está na lista de falhas do proxy: o CONNECT
  passou e o 403 é do **anti-robô do ML**. Egresso aberto, caminho fechado — são coisas diferentes e só o
  status do proxy as separa.
- **E a prova de que o pedido funciona é nova:** os cinco domínios de fabricante que o despacho de
  **17/09/2026** pediu para a robometria **estão abertos hoje** — `mais.conteudo.wap.ind.br` em **200** e
  `www.electrolux.com.br` em **301**, nas mesmas três passadas. A lista deixou de ter *"os domínios das
  ilhas e mais nada"*. Despacho aberto em `dados/despachos.md` com os três domínios, a causa e esta prova.
- **O que NÃO está bloqueado:** a leitura por **BUSCA** funciona, e foi por ela que tudo acima foi medido —
  o degrau que a jornadafly nomeou em 27/10 (*"o egresso não trava a coleta inteira; o que ele trava é a
  leitura direta, que é a PREFERIDA"*). O 3e **pode andar** por busca; os três domínios destravam a leitura
  **direta**, que é a que o nível 5 exige para atribuir campo técnico à loja.

**E duas dívidas pequenas, ditas para ninguém as descobrir de novo:**
1. **A `camara-kenda-16x3-0` espera UM campo: `bico`.** Com ele declarado, ela passa a ter identidade
   mínima e o casamento dela roda sem mudar uma linha de régua — o esquema já a espera.
2. **A bateria de mutações do casamento não virou arquivo.** Pela **31.2** eu não abri `mutacoes-*.py`
   novo sem defeito no ar que o justificasse, e as travas foram exercidas por dado real (10 ofertas, 6
   barradas, os motivos conferidos um a um). **O defeito que justificaria o arquivo já está escrito acima**
   — a trava da enumeração que recusava pelo motivo errado — e quando o casamento ganhar o próximo bloco, a
   bateria vira arquivo.

---

## 2026-10-29 10h1xZ–11hxxZ — **A ILHA ESTÁ NO AR.** A casca e a F2 desembarcaram, e a revisão do manifest saiu de 1 (que não publicava nada de propósito) para 5 — **a primeira execução desta ilha que entrega um byte que um visitante vê**

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10) e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam o foco antes de aceitar
isso: (a) o **despacho do molde da 32.6** está `FECHADO` nas três ilhas (aquametria 21/10 18h2xZ,
clubedomosaico 21/10 19h1xZ, robometria 21/10 16h1xZ) — li o topo dos três `PROMPT.md`; (b) o item
**ALTA** da ronda da clubedomosaico de 28/10 **não fura o foco**, porque a 1.2 só admite despacho ALTO em
ilha *"no ar e quebrada"* e a régua técnica daquela ronda passou inteira, **32 de 32 URLs em 200**. O item
dela é dado de banco, não página servindo erro. `executando_desde` estava `null`, que pela **1.1** já
significa que não havia bloco da Fundação vivo. Reserva escrita às **10h18Z**, commit `2addfbd`, push
aceito de primeira, e **renovada às 10h43Z** pela 1.1 — este bloco passou de 40 minutos sozinho. Nenhum
branch `claude/*` à frente do `main` e nenhum PR aberto.

---

### 1. A REDE ABRIU — E A ATRIBUIÇÃO DISSO É MAIS HONESTA DO QUE EU ESCREVI NO PRIMEIRO COMMIT

**O que está medido, às 10h2xZ, nas três passadas que a 20.2 manda:** `rodametria.com.br` e
`www.rodametria.com.br` em **200 nas três**, com `aquametria.com.br` e `robometria.com.br` em 200 nas
**mesmas** três. Seis medições de verde contra seis controles verdes, zero intermitência.

**O que eu escrevi no commit da revisão 2 e está ERRADO como afirmação:** *"o passo 20.1 foi dado pelo
Raphael"*. Eu não medi gesto nenhum dele — medi um `curl`. E o registro desta própria ilha desmente a
inferência: **a entrada de 28/10 às 19h1xZ, logo acima desta, escreve que `rodametria.com.br` e
`www.rodametria.com.br` estavam em 200**, e o cabeçalho do `ESTADO.md` escrito pela leitura semanal
**às 19h5xZ do mesmo dia** diz `000` com *"403 do proxy, medido duas vezes"*. **Trinta e poucos minutos
separam as duas, e elas se contradizem.**

**A leitura certa, e ela já está escrita no contrato:** a correção de 11/09/2026 no topo da seção 20 é
exatamente este caso — *"o mesmo comando, repetido minutos depois, devolveu 200 (…) era intermitência do
túnel lida como bloqueio, e o diagnóstico se propagou porque cada execução leu o `ESTADO.md` da anterior
como fato"*. Então o que esta execução pode afirmar é: **o egresso desta ilha responde 200 hoje, em três
passadas com controle**, e o despacho que dependia disso está cumprido. O que ela **não** pode afirmar é
quem o abriu, nem que ele estivesse fechado ininterruptamente desde 27/10. O campo `rede:` do `ESTADO.md`
foi escrito com essa diferença dentro.

**E a mesma passada remediu o que NÃO abriu** (20.3, porque é a execução que escreve a regra que exige a
fonte): os cinco domínios oficiais da Resolução Contran (`gov.br`, `in.gov.br`, `planalto.gov.br`,
`contran.gov.br`, `lex.com.br`), os quatro de prefeitura da camada municipal, os dois periódicos que
publicam o consumo de patinete e o repositório da tese da UPS — **todos em `000`**, com
`rodametria.com.br` e `aquametria.com.br` em 200 na mesma passada. Os três despachos abertos em
`dados/despachos.md` ganharam a nota de remedição; nenhum deles ficou mais barato.

---

### 2. O QUE FOI AO AR, E POR QUE A F2 E NÃO A F1

**A casca** (`snippets/rodametria-casca.php`, 1.1.1): tokens do `DESIGN.md`, símbolo **V9 completo** no
cabeçalho e em negativo no rodapé, favicon próprio em SVG (a seção 6 chama ícone padrão do WordPress na
aba de **bloco reprovado**), menu hambúrguer com `aria-expanded`/`aria-controls` e links `<a href>` de
verdade no HTML servido, trilha + `BreadcrumbList`, `WebSite` JSON-LD na home, e `<title>` e
`description` saindo de **um** mapa de páginas — nunca de dois lugares.

**E os COMPONENTES DO MOLDE da seção 32 moram nela, não em cada snippet**, porque a **32.6-b** manda:
*"o que se repete entre páginas (…) vira componente da CASCA"*. São seis: a caixa de resultado, a dobra
`<details>`, o cartão de compra (com **espaço reservado** para quem não tem foto — nenhum registro desta
ilha tem, e a seção 6 diz que perder a recomendação certa por falta de foto é trocar o certo pelo bonito),
o carrossel com `scroll-snap` em CSS puro, a barra fixa do telefone, e o rótulo do botão de loja **por
degrau** da escada da 25.1 — numa função só, porque a seção 8 registra **sete** réguas que quebraram por
procurar o rótulo de um degrau. A **32.5-c** foi obedecida na origem: as regras de telefone do molde
miram a classe `rdm-molde-*`, e as **duas** famílias de página desta ilha (ferramenta e hub) já existem
no primeiro dia, então nenhuma delas nasceu fora do alcance delas.

**A F2** (`snippets/rodametria-f2.php`, 1.0.0), em `/autonomia-patinete-eletrico/`, na ordem da **32.1**
— e a ordem é **conferida por afirmação no fonte**, não lida de olho.

**A F1 NÃO FOI, e isso é decisão registrada.** O limiar legal dela é `pendente` e os cinco domínios
oficiais seguem recusados, remedidos nesta execução. A especificação do bloco 2 já dizia, com todas as
letras: *"A F1 segue sem poder ir ao ar. A F2 e a F3 podem ir ao ar"*. **A F3 também não foi**, e a causa
é de dado: três registros declaram `carga_max_kg` e **nenhum dos três tem oferta aberta** — a conta não
teria o que comparar nem o que vender.

**Daí a home nascer HUB, divergindo do `VOZ.md`, que manda a F1 ser a home.** Home que faz a pergunta do
título e não a responde é pior que home nenhuma. A divergência está escrita **dentro da própria casca**,
no lugar onde quem for mexer a lê, com a saída: no dia em que a resolução for lida, a F1 toma a primeira
tela e os cartões descem — **nenhuma URL muda**, que é o que a 32.3 protege.

---

### 3. A DECISÃO DE ENGENHARIA DO BLOCO: NENHUM NÚMERO E NENHUMA FRASE DE RESPOSTA MORA NO PHP OU NO JS

O caminho é `dados/constantes.json` → `regras/f2.py` (o cérebro) → `ferramentas/gerar-f2.py` →
`dados/f2-respostas.json` → a option que o Sync grava → o PHP → o JS. **O PHP é tradutor e o JS é
preenchedor de molde.** Isso tem um motivo medido e não é elegância: a página responde em **dois** lugares
— o HTML pré-renderizado e a recomputação no navegador — e se cada um escrevesse a própria frase, a página
diria duas coisas diferentes para a mesma entrada **e nenhum portão veria**. É a cicatriz da seção 8 (*"as
duas metades nunca se falavam"*) com um andar a mais: aqui as duas metades são **a mesma página**.

A fronteira da seção 8 foi aplicada nome por nome: o **molde de frase** é fato externo às duas metades e
mora num lugar só; a **decisão** de qual molde vale em cada mundo está escrita duas vezes de propósito
(Python e JS), porque é ali que a divergência ensina algo. E `ferramentas/teste-f2.py` **reescreve a
aritmética à mão em `Fraction`** e lê as constantes do arquivo de constantes — nunca do arquivo que o
gerador escreveu, nem do gerador: quem confere escreve a própria régua.

**A terceira conta que a seção 8 pede** está lá: a razão `97,74 ÷ 41,29` é refeita do zero e comparada
com o fator publicado, e o fator de `misto` é conferido **pelo quadrado** (meio-caminho geométrico), sem
precisar de ponto flutuante.

---

### 4. A BATERIA DE MUTAÇÕES ACHOU UM DEFEITO REAL E TRÊS TRAVAS INERTES — ANTES DO PUSH

**O defeito real foi achado pela mutação que PRODUZ O MUNDO**, e é a regra da seção 8 em estado puro:
*"todo caso que o ESQUEMA permite e o banco ainda não tem é um caso que a régua precisa tratar hoje"*. A
vitrine lia **só** o grupo `nao_declaram_v_ou_ah`, que é o único que o banco de hoje enche. Fabriquei um
registro declarando V, Ah **e** oferta aberta — o mundo que a interseção vazia de 28/10 torna impossível
— e o item caiu em `de_outro_wh` e **desapareceu do bloco de compra**: publicável, com piso, fora da
vitrine. É o **avesso da 25.2**, e ele nunca poderia falhar enquanto o mundo não existisse. A vitrine
passou a varrer os três grupos na **ordem da seção 7** (quem passa em todas as condições antes de quem
falha numa), cada cartão carrega o rótulo do grupo dele, e a bancada ganhou a afirmação de ordem.

**As três travas inertes, as três da mesma família — régua que mede prosa por vizinhança:**
1. A régua da **32.4** (bastidor da fábrica na tela) só olhava linhas com `<p>` literal, e a promessa da
   F2 é `<p class="rdm-promessa">`. A mutação enfiou *"O egresso da nuvem"* na primeira linha da página e
   **passou**. Agora a régua olha `<p` e `<h`.
2. A trava do JS só conferia que os moldes **citados** existiam. Trocar `D.moldes.km_recusa` por um
   literal passava. Agora ela proíbe **prosa** dentro do bloco `<script>` — e a primeira versão dela
   reprovou markup legítimo, que é o erro que a 20.5 nomeia (*"portão que reprova página certa é o
   caminho mais curto para alguém passar a ignorá-lo"*), então ela deixa passar literal com `<` ou `>`.
3. **E ela achou um defeito meu no caminho:** o JS escrevia `'O que esperar no seu trajeto'` e o PHP
   escrevia **a mesma frase** — dois lugares para o mesmo rótulo, no arquivo cujo propósito declarado é
   não ter nenhum. Os dois rótulos viraram molde.

Mais a mutação cujo **alvo exato** não existia: a primeira versão mirava `faixas.plano.degenerada` da
primeira linha da tabela, que é um registro **sem autonomia declarada** — faixa vazia, campo que não
existe. Ela passou medindo nada. A segunda versão **procura** a linha com autonomia declarada em vez de
indexar, e a trava de alvo exato recusa operar se o texto não estiver lá. **8 de 8 mordem.**

---

### 5. OS DOIS DEFEITOS QUE SÓ O AR MOSTROU, E OS DOIS SÃO DA FAMÍLIA DO "VERDE QUE NÃO É ENTREGA"

**(a) A CASCA LIA A OPTION COM O NOME ERRADO.** O Sync grava `rodametria_dados_` +
`sanitize_key(id do manifest)`, e `sanitize_key` **preserva hífen**: a chave é
`rodametria_dados_f2-respostas`. A casca pedia `f2_respostas`, com sublinhado. **O desembarque da revisão
2 ACONTECEU** — três linhas no log do `/status`, as três dizendo `ok`, snippets #6 e #7 criados, option
gravada — e a página caía no estado degradado honesto. **Não havia linha vermelha em lugar nenhum:** nem
erro de PHP, nem falha no log, nem nada no console. É a **20.4** um andar abaixo: ali o Sync não aplica e
diz; aqui ele aplica, diz `ok`, e o que falha é a **leitura** do que foi aplicado. O conserto não foi
trocar a letra: o nome virou constante declarada e a bancada ganhou a afirmação que a confere contra os
ids do manifest, **nas duas direções**, mais a trava que proíbe voltar a digitar o nome na chamada.

**(b) O SITEMAP ERA INVENTÁRIO.** Ele publicava **seis** URLs e **quatro** eram lixo de fábrica do
WordPress — `/2026/10/27/hello-world/`, `/sample-page/`, `/category/uncategorized/` e
`/author/rodametria_gestor/` — contra as duas páginas de verdade, num domínio de **dois dias**. A 14.1 é
literal: *"cada URL fraca gasta orçamento que uma página boa precisaria (…) o sitemap é curadoria, não
inventário"*. A casca 1.1.0 manda as duas páginas de exemplo para a **lixeira** (nunca apaga, casando por
slug **e** por título nas duas línguas, pulando a home e tudo que ela mesma criou — mesmo método da casca
da Robometria) e **remove os provedores de sitemap de autor e de taxonomia**. Quando esta ilha tiver
artigo, quem volta é o provedor de **post**, nunca o de autor.

**(c) E DOIS `<h1>` POR PÁGINA.** O tema de blocos imprime o `post_title` como `<h1>` e o shortcode
imprime o H1 da página. Saiu o do tema, porque o da página é o que a 32.1 põe na ordem certa e o que a
32.3 protege. **H1 duplicado não dá erro em lugar nenhum** — só uma afirmação que **conta** o vê, e é por
isso que o portão de ar conta em vez de procurar.

---

### 5-b. E DEPOIS O PORTÃO DE AR ACHOU OUTROS TRÊS — DOIS DELES CHEGAVAM À TELA **POR DADO**, NÃO POR CÓDIGO

Rodado contra a revisão 6, o `conferir-no-ar.py` reprovou com dois itens, e os dois estavam no **mesmo
campo**: o `fonte` das constantes, que a dobra *"As réguas que a conta usa"* imprime.

**(d) A 32.4 FOI FERIDA POR DADO.** A palavra **"egresso"** — que a 32.4 lista **por nome** entre as
proibidas na página pública — apareceu no texto servido da F2. **Não veio do PHP:** a régua de fonte do
`teste-f2.py` varre o snippet e estava verde. Veio do `fonte` da constante
`energia-wh-tensao-vezes-amperagem`, que diz *"Nao depende de fonte nem de egresso"* — frase **certa** no
arquivo de constantes, que é registro interno, e **proibida na tela**. É a família do número de tela
digitado **com o sinal invertido**: ali o defeito era texto escrito à mão numa metade que não fala com o
banco; aqui é texto do banco indo para a tela **sem ninguém o ler como texto de tela**.

**(e) E NO MESMO CAMPO, O ACENTO.** A seção 8 manda que texto de tela saia acentuado, e os arquivos de
dado desta ilha são **ASCII**. Duas constantes publicavam *"Decisao desta ilha, nao medicao"* na dobra.
Nenhuma régua de PHP veria, pelo mesmo motivo do item (d).

**O conserto é no ponto em que o dado vira texto de tela, não no ponto em que o texto é impresso:** o
gerador passou a ter a **frase de leitor** de cada constante publicada, declarada e acentuada, com o
texto interno preservado no arquivo de constantes — e **recusa publicar** qualquer frase que carregue
palavra de bastidor ou forma portuguesa sem acento. Ele **falha em vez de publicar**. A régua de acento
tem a **lista** das formas que esta ilha produz, e não heurística: heurística sobre acento reprovaria o
título em espanhol da tese de Quito, que é fonte legítima. **4 mutações, 4 mordem.**

**(f) E A PRIMEIRA VERSÃO DA RÉGUA DA 20.4 REPROVAVA ENTREGA CERTA.** Ela lia a **janela inteira** do log
do `/status`, e as quatro linhas `FALHA manifest: HTTP 404` são de **28/10** — de antes de o manifest
existir no repositório, ou seja a história de um defeito já consertado. A 20.4 é literal: *"as linhas da
**revisão corrente**"*. O log é append-only e **sempre** vai carregar o passado. Agora a régua corta na
linha de fecho da revisão corrente, **cobra que essa linha exista** (janela que rolou é entrega não
conferida) e **registra** as falhas antigas como passado, sem reprovar. Régua que reprova entrega certa é
o caminho mais curto para alguém passar a ignorá-la — a lição da 20.5, aqui no sentido oposto ao dela.

---

### 5-c. A 32.5 FOI MEDIDA EM PIXEL, REPROVOU, E PRIMEIRO FOI PRECISO FAZER O PORTÃO EXISTIR NESTA NUVEM

**O portão de navegador não começava, e a causa é a do despacho aberto de `dados/despachos.md`** — *"21
dos 26 portões de navegador do Arquipélago estão inertes nesta nuvem, pela mesma linha de `import`"*.
Medido aqui, numa ilha que não existia quando aquele despacho foi escrito:
`node ferramentas/conferir-32-5-no-navegador.mjs` morria em `ERR_MODULE_NOT_FOUND: Cannot find package
'playwright'`, enquanto `node -e "require('playwright')"` resolvia em
`/opt/node-tools/node_modules/playwright/index.js` **na mesma máquina**. A causa cabe numa frase: **o
playwright desta nuvem é alcançado por `NODE_PATH`, e o resolvedor de ESM não lê `NODE_PATH`** — só o de
CommonJS lê. `createRequire(import.meta.url)` resolve, nenhum `--loader` conserta, e **quem copiar o
portão copia essas três linhas junto**. A nota ficou escrita no despacho, com o que esta execução **não**
fez de propósito: os 21 arquivos das outras duas ilhas, porque `foco.md` nomeia a rodametria e o próprio
despacho diz que o conserto é *"no commit da passada que reservar cada ilha"*.

**COM O PORTÃO VIVO, ELE REPROVOU:** o primeiro botão de compra da F2 estava a **1.730 px** num telefone
de 390 px, contra o teto de **1.400** da 32.5. O formulário passava com folga — **416 px** contra o teto
de 700 —, e é por isso que a 32.5-b insiste em não trocar as duas réguas: medir a caixa de resultado ali
reprovaria uma página certa.

**E A MEDIÇÃO, BLOCO POR BLOCO, DISSE ONDE ESTAVAM OS PIXELS — QUE NÃO ERA ONDE A INTUIÇÃO PUNHA:**

| onde | custo |
|---|---|
| respiro do **tema** entre cabeçalho e trilha | 84 px |
| a frase de promessa, em **quatro** linhas | 144 px |
| o formulário, cinco campos de ~100 px | 521 px |
| a frase de escopo do bloco de compra, em **quatro** linhas | 144 px |
| o espaço reservado da foto, por cartão, **antes** do botão | 96 px |
| a especificação do cartão, em **três** linhas | 77 px |

O corte foi nesses seis lugares e **em nenhum outro**. **Nenhuma palavra saiu da página** (32.3), nenhum
bloco mudou de ordem (32.1) e nenhuma afirmação da bancada mudou — o que mudou foi **densidade no
telefone**. As duas frases encurtadas dizem a mesma coisa com menos linha, e a de escopo mantém o que a
seção 7 exige dela: **a causa de nenhum dos cartões ter entrado pela conta**. O espaço reservado da foto
**continua existindo**, como a seção 6 manda, com 44 px em vez de 96 — porque no telefone esses 52 px são
do espaço mais caro da página.

**E A HOME FICOU FORA DO MOLDE, DITO E NÃO ESCONDIDO.** Ela é HUB: tem caixa de resposta (396 px, dentro
do teto) e **não** tem bloco de compra nem formulário, porque a ferramenta que o `VOZ.md` põe nela é a F1.
Julgá-la pela régua do molde a reprovaria por não ter botão de compra antes de 1.400 px — e a 32.5-b é
explícita em que portão que reprova página certa é o caminho mais curto para alguém passar a ignorá-lo.
Então `tem_molde` passou a ser o **contrato de conversão** (bloco de compra ou formulário de ferramenta), e
a home é **listada fora do molde com o motivo impresso**, que é o que a 32.5-b manda. **Isto é item para o
bloco seguinte, não estado final:** a 32.2 quer produto e ação na primeira tela de página de resposta, e a
home ganha isso no dia em que a F1 puder nascer nela — ou antes, se alguém decidir que o hub também
vende.

---

### 6. OS DOIS PORTÕES NOVOS, E POR QUE ELES NÃO FEREM A 31.2

A **31.2** proíbe portão novo sem defeito medido no ar que ele teria pegado, e a **31.3** proíbe trabalho
de bancada com item de conteúdo aberto. Os dois nasceram aqui **porque a seção 8 os exige por escrito
para publicar**, e os dois pagaram o próprio custo na mesma execução:

- `ferramentas/conferir-no-ar.py` é a lista literal da seção 8 (*"depois de publicar, busque a URL no ar
  e confira com número medido"*) mais a porta de entrada da **29.2**, o log do `/status` **linha por
  linha** da 20.4 com a leitura de cache da **20.5**, e a curadoria do sitemap da 14.1. **Ele achou os
  três defeitos do item 5 acima**, nenhum dos quais aparecia em lugar nenhum.
- `ferramentas/conferir-32-5-no-navegador.mjs` é **cópia do modelo da clubedomosaico**, como a **32.5-b**
  manda com todas as letras (*"quem copiar troca o domínio e os nomes de classe da ilha"*). Trocaram o
  domínio, o prefixo das classes e o seletor do formulário; o cabeçalho conta a história **desta** ilha,
  porque cópia que mantém o motivo da origem envelhece contando o defeito de outro site.

**E a referência saiu de `ferramentas/` para `regras/`** porque a `bancada.py` desta ilha a **denunciou no
dia em que nasceu**: *"ou ele é portão e precisa do prefixo, ou não é e precisa estar fora de
`ferramentas/`"*. Ela não é portão — portão que confere a própria produção é o teste que mede a si mesmo.
`regras/LEIA.md` registra a decisão e o que garante que aquele código roda: o gerador o importa, e a
bancada roda o gerador com `--conferir` em toda passada.

---

### 7. A CONTA DA 31.1 SAIU DE 0 DE 5 PARA 1 DE 6, e o despacho de 28/10 foi reescrito pela 18.3

Os itens **2, 3 e 4** daquele despacho estão fechados — o `pronto quando` do item 3 era **literalmente**
o `curl` que esta execução rodou. Ficou só a conta da 31.1, com o novo número. O piso é 7 em 10, e agora
o caminho para ele é a fila andar: com o canal provado e a casca no ar, **cada bloco da fila pode
terminar em página**, o que não era verdade em nenhuma das cinco execuções anteriores.

---

### O QUE ESTE BLOCO DEIXA PARA O SEGUINTE — e o primeiro item mudou de lugar na fila

**O 3d (o casamento do registro com a oferta) continua sendo o próximo**, e agora com uma razão a mais
que é visível na tela: a F2 no ar diz, com a prestação de contas da seção 7, que **nenhum** dos 17
registros entra pela conta de Wh, e que os quatro da vitrine estão lá com o rótulo *"a ficha não declara a
bateria"*. Isso é honesto e é pouco. O 3d resolve `url_produto` (e com ele o teste de vida da 25.4-b
passa a existir aqui), a **foto** que o cartão do molde pede — hoje os quatro cartões servem espaço
reservado — e o caminho para a ficha onde o campo técnico mora. Leia a **25.7** e a **25.9** antes de
escrever uma linha.

**E duas coisas que esta execução deixou medidas e não fechou, ditas para ninguém as descobrir de novo:**
1. **A 32.5 não foi medida em pixel nesta passada.** O portão existe e está no repositório, mas a
   medição a 390 px num navegador de verdade ficou para a passada seguinte ou para a ronda — e o
   `conferir-no-ar.py` **diz isso como registro** em vez de aprovar em silêncio, que é o que a 32.5-b
   proíbe. Rodá-lo é um comando.
2. **A bateria de mutações da F2 não virou arquivo.** As 8 mutações rodaram nesta execução, de dentro de
   uma passada avulsa, e provaram as travas hoje. Pela 31.2 eu não abri `mutacoes-f2.py` sem defeito no
   ar que o justificasse — mas a seção 8 é clara em que *"mutação que não roda não é trava"*, e mutação
   que rodou uma vez não roda amanhã. **Quando a F2 ganhar o próximo bloco, a bateria vira arquivo**, e o
   defeito medido que a justifica já está escrito no item 4 acima.

---

## 2026-10-28 19h1xZ–19h3xZ — **O PISO DE COMPRA EXISTE: 5 REGISTROS PUBLICÁVEIS, DE ZERO.** E o bloco mediu a coisa que ninguém tinha medido: **o piso e o dado técnico caíram em registros DIFERENTES, e a interseção é VAZIA** — o que destrava a casca não é link, é casamento

**A ESCOLHA DA ILHA.** `foco.md` nomeia a **rodametria** (foco total e absoluto, decisão do Raphael de
27/10), e pela 1.2 não há escolha a fazer. A exceção do molde de conversão (32.6) segue **fechada nas três
ilhas**, e nenhuma ilha no ar está quebrada. `executando_desde` da rodametria estava `null` — que pela 1.1
já significa que não havia bloco da Fundação vivo, sem reserva vencida para o git desempatar; o último
commit na pasta da ilha era de **16h41Z**, 2h35 antes. Reserva escrita às **19h16Z**, commit `e34d578`,
push aceito de primeira. Nenhum branch `claude/*` e nenhum PR com commit fora do `main` (o
`claude/dreamy-mccarthy-c0c92n` estava idêntico ao `origin/main`, 0 à frente e 0 atrás).

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA:** `rodametria.com.br` e `www.rodametria.com.br` em **200**, com
`aquametria.com.br` e `robometria.com.br` em 200 na mesma passada. Pela **20.3**, porque este bloco escreve
a regra que exige a fonte: `open-api.affiliate.shopee.com.br` em **200**, `shopee.com.br` em **200**,
`s.shopee.com.br` em **307**. **O egresso da Shopee está aberto para esta ilha** — e isso não estava medido
em execução nenhuma dela.

**CANAL DE DESEMBARQUE SÃO (20.5), embora nada tenha ido ao ar:** `/status` em **revisão 1**, igual ao
`manifest.json`, `ultimo` às **18:40:29** (o cron de 30 minutos está vivo) e **zero linha de FALHA depois
das 13h40**.

---

### POR QUE ESTE BLOCO E NÃO A CASCA — a divergência está escrita porque ela é uma decisão, não um esquecimento

O `bloco_atual` que o bloco 3 deixou dizia *"PRÓXIMO PASSO: a coleta em ficha de FABRICANTE, antes da
casca"*, e a fila do `PROMPT.md` tem o **3b (casca)** como próximo. **Peguei o piso de compra, e a razão é
de contrato, em três passos que se encadeiam:**

1. A **25.2** manda, com todas as letras: *"Todo item ganha `url_busca` ANTES de qualquer outra coisa. Item
   sem `url_busca` é defeito da 19.1, sempre, em qualquer degrau. Não existe item publicável sem piso."*
   Os 24 registros do banco tinham a **mesma** frase em `motivo_do_status`, e ela nomeia esta causa única.
2. A **32.1**, item 5, põe o **BLOCO DE COMPRA imediatamente abaixo do resultado** na página de ferramenta,
   e a **32.5** reprova a página cujo primeiro botão de compra não aparece antes de 1.400 px. Ilha nova
   **nasce** no molde (32.6). Com zero registro publicável, a casca não teria o que pôr ali — o bloco 3b
   não estava apenas em segundo lugar, estava **impossível**.
3. A **18.5** desempata na mesma direção: *"na dúvida entre fechar um despacho e começar um bloco novo,
   fecha o despacho"*, e a 14 põe a indexação como prioridade máxima da ilha nova — o que vale dizer que o
   caminho mais curto para a primeira página no ar passava por aqui.

A coleta em ficha de fabricante **continua sendo o passo caro e necessário**, e este bloco mediu por que
ela ficou ainda mais necessária. Está escrita abaixo, com o alvo apertado.

---

### O QUE ENTROU

**`dados/esquema-banco.json` — versão 2, com a `escada_de_compra`.** A regra da palavra-chave mora no
**esquema**, nunca dentro da régua, pelo mesmo motivo que a lista de níveis mora lá: lista dentro da régua
envelhece calada, e tipo novo entraria sem termo nenhum com o banco verde. O que a seção declara:

- **`termo_de_contexto`** — a palavra que diz *o que o produto é*, na língua do vendedor de marketplace,
  por `tipo_comercial` (VEÍCULO) e por `tipo` (PEÇA). Valor que não está lá **mata a régua**, e há quatro
  mutações que provam isso.
- **A escada de palavra-chave**, do degrau mais específico ao menos: VEÍCULO `marca_modelo_termo` →
  `marca_modelo` → `modelo_termo` → `marca_termo`; PEÇA `marca_termo_medida` → `marca_termo` →
  `termo_medida`. **A peça não leva código de modelo** — lição da Robometria herdada pronta: código de peça
  é SKU interno e o vendedor não o digita no título; o que a peça leva é a **medida de encaixe**, que é como
  ela é vendida.
- **O que nunca compõe:** o termo sozinho (daria a vários registros a MESMA URL), a marca sozinha (a
  armadilha da 25.3), o modelo sozinho, e o `titulo_colhido` inteiro (a 25.6(a) mediu que chave longa
  devolve zero).
- **`sub_id_2` é `null` no piso de REGISTRO, e está escrito por quê:** um registro aparece em mais de uma
  ferramenta — o mesmo patinete responde à F2 e à F3 — e um link carrega **um** `sub_id_2`. Quem o decide é
  a **página**, não o registro; gravar um aqui atribuiria a uma ferramenta o clique que veio de outra, que é
  pior que não atribuir. O piso nasce com `sub_id_1` só, **como o da Robometria**, e o link por ferramenta é
  refinamento da casca.

**`ferramentas/coletar-piso-de-compra.py`** — mede, encurta e grava, com `--gravar` e `--conferir`.
**`ferramentas/mutacoes-piso.py`** — 18 casos (3 mundos que passam, 11 quebras, **4 mortes do esquema**),
mais 10 afirmações sobre a forma da chave e o autoteste da própria bateria. **`ferramentas/validar-banco.py`**
ganhou duas contagens e um aviso novo (o do parágrafo abaixo); ele **já cobrava** a 25.2 e a 25.2-b e não
precisou de uma linha para isso — o portão do bloco 3 estava certo e esperando dado.

---

### A CHAVE É MEDIDA, NUNCA SUPOSTA — e é isso que separa esta régua de um gerador de texto

A 25.6(a) mediu em 16/09 que palavra-chave longa devolve zero e que **zero não é erro**. A busca permite
uma coisa que a ficha não permite: o degrau útil não é o que casa com o registro, é o **em que a loja tem o
que vender**. Então cada degrau desta escada é consultado na Open API (`productOfferV2`) antes de virar
piso, e o número volta gravado em `ofertas_na_medicao` com `medido_em`. **Chave com zero oferta não vira
piso e a escada desce** — um botão que leva a uma página de busca vazia é o beco sem saída que o piso
existe para impedir.

**RESULTADO, 17 registros não excluídos medidos um por um:** **5 com piso** (4 veículos + 1 peça), **12
sem**. E os 12 se separam em duas causas, nenhuma delas "falta coletar":

- **7 não compõem chave nenhuma**, porque o banco não tem os dois identificadores que a escada combina. O
  caso é o do anúncio que empacota três nomes no título (`Bike/Scooter/Moto elétrica`): `tipo_comercial`
  ficou honestamente em `nao_declarado` e com isso **o termo é `null`** — e sem marca **e** modelo não há o
  que compor. **É a 25.9 outra vez, num campo novo:** campo que empacota dois identificadores recusa o
  anúncio certo para sempre. Aqui o anúncio que empacota dois nomes **não dá nem o nome pelo qual ele se
  busca.**
- **5 percorreram a escada inteira e a loja devolveu ZERO em todos os degraus** — `MAXSHOT V1`, `MAXSHOT
  V1SPRO`, `PLAYBIK patinete eletrico`, `Honeywhale H3`, `Haixia scooter eletrica`. Os degraus medidos
  ficaram gravados um por um no `motivo_sem_url_busca`, no formato CAUSA || ÚLTIMA TENTATIVA da 25.4-b.3,
  para a próxima execução não repetir a mesma pergunta às cegas.

**O `sub_id` saiu certo POR CONSTRUÇÃO, e a prova não gastou um clique desta ilha.** A 25.8 é explícita: o
salto do encurtador é onde a Shopee conta o clique, e conferir os links de uma ilha por esse caminho grava
um clique com a etiqueta dela justo na semana em que a leitura semanal procura o **primeiro clique
orgânico**. Então os cinco links desta ilha **não foram abertos**. O mecanismo foi provado uma vez, com
`ferramentas/conferir-sub-id.py` e sub-id de **bancada**: 301, `utm_content` = `bancada-t0---`, campo 1 na
primeira casa. Os links da ilha saem da **mesma** função `encurtar()`.

---

### O ACHADO DO BLOCO, E ELE VALE MAIS QUE OS CINCO LINKS

**O PISO E O DADO TÉCNICO CAÍRAM EM REGISTROS DIFERENTES, E A INTERSEÇÃO É VAZIA.** Dos **4** veículos
publicáveis, **zero** declara tensão + amperagem (a entrada da F2) e **zero** declara carga máxima (a
entrada da F3) — enquanto os **2** registros com Wh derivado e os **3** com carga máxima estão, todos,
entre os 12 **sem** saída de compra.

Não é coincidência, e é por isso que virou **aviso do validador** em vez de frase de registro: o anúncio
que nomeia **marca e modelo** é achável na loja e não publica ficha técnica; o que publica **60 V 20 Ah** ou
**120 kg** empacota três nomes no título e não é achável por nome nenhum. **São duas populações de anúncio,
e o banco herdou as duas.**

**A consequência, escrita para quem for construir a casca:** o bloco de compra da 32.1 pede o produto **que
a ferramenta escolheu**, e hoje **nenhuma das três escolhe um publicável**. Mais piso não conserta isso.
**O que destrava é o CASAMENTO do registro com a oferta** — os degraus 1 a 3 da 25.1 —, porque é ele que
traz a ficha e, com a ficha, o campo técnico. E ele é justamente o casamento das cinco armadilhas da 25.7,
que esta execução **não** fez de propósito: é bloco próprio.

---

### OS DOIS DEFEITOS QUE ESTA PASSADA ACHOU EM SI MESMA, e os dois foram pegos por portão e não por leitura

**(1) O DEGRAU COM NOME MENTIROSO.** A primeira versão de `_juntar()` filtrava as partes vazias e devolvia
o que sobrasse. Com isso o degrau `marca_modelo_termo` de um registro **sem modelo** compunha, na verdade,
`marca_termo` — e era **gravado com o nome errado**. A primeira passada medida imprimiu `playbik` e
`honeywhale-h3` com `marca_modelo_termo`, os dois sem modelo um deles sem termo. **Procedência que mente é
pior que procedência ausente**, porque `degrau_da_palavra_chave` existe exatamente para a execução seguinte
saber por que aquela chave é aquela. Agora o degrau só nasce quando **todas** as partes que o nomeiam
existem, e três afirmações da bateria mordem isso.

**(2) A COLETA PULAVA O REGISTRO EXCLUÍDO E A CONFERÊNCIA NÃO.** `coletar-piso-de-compra.py --conferir`
reprovou o banco em três registros `excluido_do_banco`, cobrando deles o motivo de hoje. Os dois lados
estavam defensáveis e **discordavam**: a coleta os pula porque registro recusado fica gravado para a
próxima execução não o recolher, e a conferência os varria como qualquer outro. O portão reprovou **banco
certo** — que a 32.5-b já nomeou como o caminho mais curto para alguém passar a ignorar um portão. A
conferência passou a pular pela mesma regra, e há um **mundo que tem de passar** na bateria guardando isso.

---

### BANCADA, 0 FALHA — 5 portões, e dois deles nasceram hoje

`validar-banco.py` **APROVADO** com 0 falha e 4 avisos; `mutacoes-banco.py` **APROVADO** com os 66 casos de
ontem intactos (o esquema subiu para a versão 2 e nenhuma morte do esquema mudou de comportamento);
`mutacoes-piso.py` **APROVADO** com 18 casos + composição + autoteste; `coletar-piso-de-compra.py
--conferir` **APROVADO** sem rede; `derivar-banco.py --conferir` **APROVADO**. A bancada **descobriu** os
dois portões novos pela convenção de nome, sem ninguém os listar — que é a razão pela qual esta ilha nasceu
com ela.

---

### A SEÇÃO 31 LIDA EM VOZ ALTA, porque ela desaprova parte do que entrou aqui e isso não se esconde

A **31.1** pede que 7 de cada 10 execuções de uma ilha entreguem algo **no ar que o visitante vê**, e a
**31.2** diz que portão, régua ou mutação nova *"só nasce quando existe defeito medido no ar que ela teria
pegado"*. **Esta execução não entregou nada no ar e escreveu uma bateria nova.** Os dois fatos ficam
registrados, e com eles o que penso deles:

- **Nenhuma execução desta ilha pode satisfazer a 31.1 hoje**, porque a ilha tem **zero** URL. A 31 nasceu
  em 21/10 de um problema oposto e nomeado: a aquametria, **com 52 URLs no ar e 586 impressões na semana**,
  gastando execução em bancada. A proporção da 31.1 passa a ser mensurável nesta ilha no dia em que a casca
  subir — e a 31.6 manda a leitura semanal contá-la, com o `REGISTRO.md` na mão.
- **A bateria nova não é trabalho de bancada sobre portão existente** (o que a 31.3 proíbe): é a bateria de
  uma régua que nasceu nesta mesma execução, e o `PROMPT.md` desta ilha já declarava a prática, com a causa
  — *"Esta ilha nasceu com a bancada, em vez de ganhá-la depois de perder uma régua"*. **E ela mordeu na
  própria passada:** os dois defeitos da seção acima foram achados por portão, não por leitura, e um deles
  (o degrau com nome mentiroso) teria ido para o `main` gravado em cinco registros.

---

### NADA FOI AO AR, E NADA PODIA

O `manifest.json` segue na **revisão 1** com os três grupos vazios: esta ilha não tem página nenhuma, e a
primeira revisão que publica algo continua sendo a da **casca (bloco 3b)**. `publicar` segue `false` nos
arquivos de dados — eles alimentam ferramenta, não são página.

**PRÓXIMO PASSO DESBLOQUEADO: o CASAMENTO do registro com a oferta da Shopee (degraus 1 a 3 da 25.1).** É
ele que resolve as duas pontas de uma vez — dá `url_produto` (e com ela o teste de vida da 25.4-b passa a
existir nesta ilha), dá a foto que a 32.1 pede no cartão, e dá o caminho para a ficha onde o campo técnico
mora. **E ele é o casamento das cinco armadilhas da 25.7**, que precisam ser lidas antes de uma linha ser
escrita. O alvo apertado, saindo da medição de hoje e não de impressão: os **7** registros que não compõem
chave e os **5** que a loja não respondeu — e os **12** sem saída de compra que incluem todo o dado técnico
que o banco tem.

## 2026-10-28 16h4xZ — **BLOCO 3 ENTREGUE: O MODELO DO BANCO.** O esquema, 24 registros, três portões e a bancada — e o número que o bloco mediu vale mais que o esquema: **zero veículo com potência nominal declarada, contra 14 com um watt sem rótulo**

**A ESCOLHA DA ILHA, dita antes de qualquer coisa.** `foco.md` nomeia a **rodametria** (foco total e
absoluto, decisão do Raphael de 27/10), e pela 1.2 não há escolha a fazer. Conferi as duas exceções que
furariam o foco: o **despacho do molde de conversão** (32.6) está **FECHADO nas três ilhas** — aquametria
em 21/10 às 18h2xZ, clubedomosaico em 21/10 às 19h1xZ, robometria em 21/10 às 16h1xZ —, e o **item 1
(ALTA) do despacho da Sentinela de 28/10 na clubedomosaico** não fura: a 1.2 exige ilha no ar **E
QUEBRADA** (página servindo erro, ferramenta devolvendo número errado, site fora do ar), e a própria ronda
registra, com todas as letras, *"A RÉGUA TÉCNICA PASSOU INTEIRA"* — 32 de 32 em 200, as duas ferramentas
conferidas com entrada inédita e a conta refeita na mão. O que o item 1 descreve é dívida de receita, não
ilha quebrada. **`executando_desde` da rodametria estava `null`, que pela 1.1 já significa que não havia
bloco da Fundação vivo** — não houve reserva vencida para o git desempatar. Reserva escrita às **16h19Z**,
commit `4a14f00`, push aceito de primeira. Nenhum branch `claude/*` e nenhum PR aberto (`list_pull_requests`
em aberto devolveu vazio), e o `main` local estava idêntico ao `origin/main`.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA:** `https://rodametria.com.br/` e `/wp-sitemap.xml` os dois em
**200 nas três passadas**.

---

### O QUE ENTROU

`dados/esquema-banco.json` — o contrato, **versão 1**, com três entidades, a escada de fontes de oito
níveis, a regra de divergência por campo, a lista de campos que exigem procedência de leitura e os grupos
de prestação de contas das três ferramentas. `dados/veiculos.json` (**17** registros), `dados/pecas.json`
(**3**), `dados/municipios.json` (**4**). Os portões: `ferramentas/validar-banco.py`,
`ferramentas/derivar-banco.py` (quem **escreve** `energia_wh`, separado de quem o **confere**, de propósito
— a segunda metade existe para discordar da primeira) e `ferramentas/mutacoes-banco.py`. Mais
`ferramentas/bancada.py`, que descobre os portões em vez de os listar.

**OS 24 REGISTROS SAÍRAM SÓ DO QUE JÁ ESTAVA COLHIDO NO REPOSITÓRIO** — `dados/corpus-buscas.md` (bloco 1),
a tabela 1.6 de `dados/especificacao-calculadoras.md` (bloco 2) e a seção (c) de
`bussola/dossies/rodametria/DOSSIE.md` (Bússola, 27/10). **Nenhuma rede foi tocada para montá-los e nenhum
número foi digitado de cabeça.** Modelo de banco sem registro nenhum é hipótese: o que prova um esquema é
ele aplicado a dado real, e foi a aplicação que achou tudo o que está abaixo.

**NENHUM REGISTRO É `publicavel`, e a causa é UMA SÓ:** ninguém tem saída de compra, e a 25.2 não admite
item publicável sem piso. Está em cada `motivo_do_status`, com a mesma frase. **Nada foi ao ar e nada
podia:** o `manifest.json` segue na **revisão 1** com os três grupos vazios. Conferi o canal de qualquer
jeito, porque ele nasceu hoje e vinha falhando: `/status` em **revisão 1**, igual ao `manifest.json`,
`ultimo` em **16:13:31** e **zero linha de FALHA** depois das 13h40 — o cron de 30 minutos está vivo e o
canal está são. Pela 20.5, revisão igual com log de agora é o estado certo, não cache.

### BANCADA, 0 FALHA

`bancada.py` rodou os três portões sem rede: `validar-banco.py` **APROVADO**,
`derivar-banco.py --conferir` **APROVADO** (todo `energia_wh` do banco bate com V × Ah),
`mutacoes-banco.py` **APROVADO** com **66 casos** — **4 mundos que têm de passar** (o banco de hoje, o
banco **vazio**, um registro publicável completo no degrau 3 com par colhido, e um no degrau 4 com `url`
vazia) e **62 quebras**, cada uma declarando no próprio caso o **pedaço da frase** que espera ouvir de
volta. Mutação que aceita qualquer reprovação passa quando o portão reprova pelo motivo errado, e duas
delas reprovaram assim na primeira rodada — as duas eram expectativa minha escrita com desleixo, e a
bateria as pegou. **Mais o autoteste da bateria:** um validador de mentira, que aprova tudo, tem de fazer
a bateria reprovar. Sem isso, bateria quebrada diz `0 falha(s)` e ninguém sabe.

**Sete das 62 são MORTES DO ESQUEMA (26.2), e elas não estragam registro nenhum:** apagam uma chave **do
esquema** e exigem que o portão **MORRA**, nunca que aprove em silêncio. Régua que lê a própria lista de um
arquivo de dados aprova tudo, calada, no dia em que o arquivo perder a chave. A mais instrutiva é a da
sentinela: apagando `valor_sentinela_de_ausencia` do esquema, **o banco de HOJE passa a reprovar** — o que
prova que aquela linha do esquema sustenta peso, e não é decoração.

**E a bancada tem régua própria, medida no dia em que nasceu:** com um portão inerte de mentira (imprime
`REPROVADO` e sai 0) e um arquivo sem convenção de nome, ela denunciou os dois e fechou **REPROVADO**.
Removidos depois.

---

### O ACHADO DO BLOCO, E ELE É UM NÚMERO: **`veiculos_com_nominal_declarado` = 0, CONTRA 14 COM UM WATT SEM RÓTULO**

O `PROMPT.md` desta ilha já dizia a regra: *"anúncio que só diz '1000W' no título não alimenta a F1 sem a
ficha dizer qual dos dois é"*. Era uma regra. **Aplicada aos 17 registros, virou uma medição**, e a medição
é mais dura do que a regra soava: **das 17 fontes colhidas, nenhuma declara se o watt é nominal ou de pico.**
Nem a ficha do Extra, nem a das Casas Bahia, nem o painel da Shopee, nem o do Mercado Livre.

**O que isso muda no plano, e muda de verdade:** a F1 **não tem candidato nenhum na vitrine nem no dia em
que os limiares da Contran chegarem**. O despacho ALTA de 28/10 destrava a *fórmula*; ele não destrava a
*entrada*. O que falta além da resolução é a **ficha que diz qual dos dois watts é o nominal** — nível 4 da
escada (`ficha-do-fabricante-lida`), hoje **vazio**, porque nenhum domínio de fabricante desta ilha foi
tentado por execução nenhuma. **Isto é trabalho de coleta, não de ferramenta**, e é o próximo passo
desbloqueado mais caro da ilha.

**E A TABELA 1.6 DA ESPECIFICAÇÃO TEM UMA COLUNA QUE PROMETE MAIS DO QUE AS FONTES DERAM — ERRATA.** Ela
tabula sete veículos sob o cabeçalho **"W nominal"**. Nenhuma das sete fontes usa a palavra *nominal*: o que
cada uma publica é um watt só, sem rótulo. A coluna não está errada nos números; está errada no **nome**, e
o nome é justamente a distinção que esta ilha vende. No banco, os mesmos números moram em
`potencia_declarada_sem_rotulo_w`, e `potencia_nominal_w` está null com motivo nos 17. **A errata fica aqui
e não reescreve a especificação:** a tabela é registro do que o bloco 2 leu, e o banco é o contrato do que
a ferramenta pode usar — quem construir a F1 lê o banco.

### AS TRÊS COISAS QUE O ESQUEMA ACRESCENTOU À LISTA DO `PROMPT.md`, e as três nasceram de aplicar a lista a dado real

**(1) A ENTIDADE `MUNICIPIO`.** A lista do bloco 3 pede VEÍCULO e PEÇA, e é **anterior** à especificação do
bloco 2 — que deu à F1 **quatro** entradas e fez a quarta ter **três** estados de saída, sendo o do meio
*"município preenchido e conhecido pelo banco"*. Esse estado precisa de um banco de municípios que ninguém
havia mandado existir; sem ele, a F1 cairia na ressalva genérica fingindo que essa é a única resposta
possível. A camada 2 da F1 é **dado**, não prosa de rodapé.

**(2) `potencia_declarada_sem_rotulo_w`.** Ver o achado acima. O esquema nasceu com dois campos de potência
e a montagem dos registros mostrou que o mundo tem **três** estados, não dois.

**(3) `cotacoes[]` como SÉRIE**, no lugar de "preço com data" como campo. Leitura nova não substitui leitura
velha: substituir apaga a série, que é a única coisa capaz de mostrar que o anúncio de R$ 2.299 de 27/10
virou outro número. É a lição que a Robometria escreveu no esquema dela, aqui como array dentro do registro
em vez de entidade separada — com 24 registros, o custo de um arquivo a mais não se paga ainda.

### A DECISÃO DE ENGENHARIA DO BLOCO: **SEVERIDADE DE FONTE É POR CAMPO, PELA ASSIMETRIA DE CUSTO — NÃO UMA LINHA SÓ PARA O REGISTRO INTEIRO**

A primeira versão da escada dizia, como a da Robometria, que os níveis 6, 7 e 8 **não sustentam campo
técnico nenhum**. Aplicada ao banco, ela **reprovava campo certo**: o Wh da F2 é `V × Ah`, identidade
matemática, e o anúncio que escreve *"60 V 20 Ah"* no título está **declarando a bateria**, não prometendo
desempenho. Errar ali custa uma faixa de km mais larga; errar na categoria legal manda alguém para a rua
sem habilitação. **São erros de preço diferente, e a seção 10 manda a direção sair da assimetria de custo.**

Então o esquema ganhou `niveis_minimos_por_campo`: **nível 5 ou melhor** (ficha de varejo grande) em
`potencia_nominal_w`, `velocidade_max_kmh`, `acelerador` e `carga_max_kg` — os três primeiros são as
entradas da F1, e o quarto é a 3.5 da especificação (*"não estima carga máxima de veículo que não a
declara"*); **nível 6 aceito** em `tensao_v`, `amperagem_ah`, `autonomia_declarada_km`, `aro`, `peso_kg` e
nos dois campos de potência que não classificam; **nível 8 não sustenta nada**, em nenhum campo.

**O resultado prático:** a F2 e a F3 têm candidato real no dia um (2 veículos com Wh derivado de V e Ah
declarados, 3 com carga máxima de ficha), e a F1 tem zero — **cada um pelo seu motivo, escrito.** Portão
que reprova campo certo é o caminho mais curto para alguém passar a ignorá-lo, e é a mesma lição que a
20.5 nomeou quando o "REPROVADO" era cache.

### O SEGUNDO ACHADO, E ELE VEIO DA PRIMEIRA RODADA DO PRÓPRIO VALIDADOR: **O PIVÔ DA F1 QUEBRA A INVARIANTE DE PROCEDÊNCIA, E QUEBRA COM RAZÃO**

Todo campo deste banco obedece a "valor presente ⇒ procedência presente": com valor, exige-se `fonte`,
`declarado_como` (o texto **literal** da fonte) e, nos dois campos da 26.1, `declarada_por`. O `acelerador`
é um enum de **três** valores em que o terceiro, `nao_declarado`, **tem como conteúdo a própria ausência de
declaração** — cobrar dele o texto literal é cobrar o literal de uma frase que não existe. A primeira
rodada reprovou **40 vezes** por isso, em registro certo.

**A regra que nasceu:** o esquema declara `valor_sentinela_de_ausencia` no campo, e a sentinela **exige
`fonte`** (onde se olhou) e **`motivo`** (por que não se achou) e **dispensa** `declarado_como` e
`declarada_por`. O nome da sentinela mora **no esquema**, não dentro do validador: o dia em que outro campo
ganhar sentinela, ele a declara numa linha e a trava passa a tratá-la sem código novo (26.2). E a sentinela
nunca dispensa o registro de nada mais — ela é um valor, conta nos grupos de prestação de contas, e **nunca
cai no lado "só pedal assistido" por omissão**.

**E a mesma rodada achou um defeito de verdade no dado**, não na régua: **dois registros nasceram com o
pivô da F1 em `null`** (`patinete-adulto-com-banco-shopee` e `playbik`), porque o construtor caiu no padrão
de "campo não colhido" num campo que **não aceita nulo**. Os dois foram consertados para a sentinela, com
`fonte` e `motivo`. Foi o portão pegando o autor do portão na mesma passada — que é exatamente para isso
que ele existe.

### A MEDIÇÃO DA 20.3, QUE É DEVER DE QUEM ESCREVE A REGRA: **OS QUATRO DOMÍNIOS DE PREFEITURA ESTÃO RECUSADOS**

Escrevi no esquema que o nível 3 exige **o ato lido no domínio `.gov.br` do município** — então pela 20.3 a
medição é minha. Às 16h3xZ, nas três passadas da 20.2: `www.campinas.sp.gov.br`, `www.rio.rj.gov.br`,
`www.joinville.sc.gov.br` e `www.sjc.sp.gov.br` em **000 nas três**, com `rodametria.com.br` e
`aquametria.com.br` em **200 nas mesmas três**. **12 medições de bloqueio contra 6 de controle verde, zero
intermitência**, com o egresso respondendo `connect_rejected` — recusa de política, não queda de host. **É
a mesma parede do despacho ALTA de hoje:** o que esta ilha não alcança não é um site, é o domínio
`.gov.br`.

Os quatro municípios são `pendente`, e a consequência está escrita sem maquiar no próprio arquivo: **hoje a
camada 2 da F1 tem DUAS saídas em vez de três, e as duas imprimem a mesma frase genérica.** A diferença
entre isso e um buraco é que isso está contado, com a causa e com o nome dos quatro domínios. **Despacho
NORMAL novo** em `dados/despachos.md`, com o pedido nas duas formas — e a forma (a) dele é uma linha só,
`*.gov.br`, que fecha **os dois despachos de hoje** de uma vez.

E a nota de método, porque ela se repetiu dentro da mesma execução: a primeira versão do `municipios.json`
dizia *"os quatro domínios que ninguém tentou"*. **Essa frase ficou velha na execução que a escreveu**, e a
nova é pior: não é que ninguém tentou — é que não dá. É a família do bloqueio herdado do `ESTADO.md` lido
como fato (20.2), com três horas de vida em vez de três dias.

### O QUE MAIS O ESQUEMA DECIDIU, em uma linha cada

- **`tipo_comercial` e `categoria` são enums DISJUNTOS**, e o validador reprova se passarem a compartilhar
  um valor. "Scooter" não é categoria da resolução, e o esquema faz com que não exista **como** gravá-la.
- **`categoria` é null nos 17, por força da constante**, e o validador lê o **status da constante** em
  `constantes.json` — não uma lista escrita dentro dele. Com o limiar `pendente`, categoria preenchida é
  reprovação com a frase *"o anúncio escrevendo a regra"*.
- **A divergência resolve para o lado RESTRITIVO** nesta ilha — oposto da Aquametria (que resolve pelo
  maior) e mesma direção da Robometria (que resolve pelo mais estreito). O erro caro aqui é o permissivo.
- **Três registros nasceram `excluido_do_banco` com a causa escrita** — dois títulos de anúncio sem marca e
  sem modelo, e um item cuja única fonte é nível 8. Recusa que não se escreve é recusa que a próxima coleta
  repete.
- **A prestação de contas da seção 7 é conferida como invariante**, não como intenção: o validador avalia
  os grupos das três ferramentas sobre **todo** registro e reprova se algum cair em zero ou em dois grupos.
  Com zero publicáveis ela é **verdadeira por vacuidade**, e o validador diz isso como **AVISO** — registro,
  nunca aprovação, na mesma família da janela de 15 linhas da 20.4.

### PRÓXIMO PASSO DESBLOQUEADO

**O bloco 3b (casca) depende do WordPress e ele está no ar**; o que o bloco 3 deixa pronto para ele é o
banco de onde a vitrine sai e a dívida da 26.3 nomeada (a frase da tela que lê `declarada_por` e escolhe a
atribuição — ela é da casca, não do banco). **Mas o passo que vale mais não é a casca: é a COLETA EM FICHA
DE FABRICANTE**, pelos dois números que este bloco mediu — 0 de 17 com potência nominal declarada e nível 4
da escada vazio. Sem ele a F1 fica sem entrada mesmo com a resolução na mão, e a F1 é a home desta ilha. O
primeiro passo dessa coleta é de um comando e é a 20.3 outra vez: **medir o egresso contra os domínios dos
fabricantes antes de escrever regra que os exija.**

---

## 2026-10-28 13h5xZ — **ADENDO À MESMA EXECUÇÃO: O SYNC DA ILHA NASCEU HOJE E ESTAVA FALHANDO EM SILÊNCIO.** A seção 4 **ao contrário** — não foi o site que ficou para trás, foi o repositório

**Achado fora do bloco, na conferência de fecho.** Às 10h17Z desta mesma manhã a execução
do bloco 1 mediu `/wp-json/rodametria/v1/status` em **404** e escreveu no `PROMPT.md` que *"o
snippet de Sync não existe ainda"*. Às **13h2xZ** o mesmo endereço devolve **200**, com
`versao_sync: 1.1.5`. **O passo 8 da seção 11 foi feito pelo Raphael entre as duas
medições**, e nem o `ESTADO.md`, nem o `PROMPT.md`, nem o despacho sabiam.

**E o canal não estava só desconhecido: estava FALHANDO, de 30 em 30 minutos.** O que o
`/status` trazia:

```
revisao: -1
2026-10-28 13:10 FALHA manifest: HTTP 404 em manifest.json
2026-10-28 12:48 FALHA manifest: HTTP 404 em manifest.json
2026-10-28 12:30 FALHA manifest: HTTP 404 em manifest.json
2026-10-28 11:48 FALHA manifest: HTTP 404 em manifest.json
```

O cron próprio da ilha (`rodametria_30min`) vinha pedindo
`raw.githubusercontent.com/rmnatal/arquipelago/main/ilhas/rodametria/manifest.json` **desde
as 11h48Z**, e o arquivo não existia no repositório. **É a seção 4 virada do avesso:** o
contrato existe para o caso de o site andar e o cabeçalho ficar para trás; aqui o **canal de
desembarque** estava de pé, batendo na porta, e o lado do repositório estava mudo.

**O QUE FOI FEITO, e por que não publica nada.** Nasceu
`ilhas/rodametria/manifest.json` na **revisão 1**, com os **três grupos vazios**
(`snippets`, `conteudo`, `dados`). **Verificado contra o código do Sync** antes de escrever —
`ilhas/robometria/snippets/robometria-sync.php`, que é o mesmo código nas ilhas: o Sync exige
`revisao` e um array, pula grupo vazio sem erro, e o portão de publicação é o `publicar:
true` de **cada item** (`desembarque.aprovado` ele **não lê** — é documentação para gente).
Com zero item, ele aplica zero, pula zero e grava a revisão.

**As duas coisas que isso compra, as duas baratas:**
1. **O log do `/status` para de encher de FALHA** — e ele é uma **janela de 15 linhas** (20.4).
   No dia do primeiro desembarque de verdade, a janela estaria cheia de ruído, e *"item que
   rolou para fora da janela não foi conferido"*.
2. **O caminho fica provado ponta a ponta com NADA em jogo:** `raw.githubusercontent.com` →
   `wp_remote_get` do Sync → `json_decode` → revisão gravada → `/status` público. Se a
   constante `RODAMETRIA_SYNC_BASE`, o caminho ou o cron estiverem errados, **descobre-se
   hoje, com zero página no ar**, e não no dia em que a F1 for ao ar. É a mesma família do
   passo 20.1: *"casca no ar que não pode ser verificada é pior que casca inexistente"*.

**VERIFICADO NO AR PELA 18.4 E PELA 20.4, e o critério de pronto era declarado antes.** O
cron da ilha rodou às **13h40:03Z** e o `/status` virou:

```
revisao: 1   ultimo: 2026-10-28 13:40:03
2026-10-28 13:40 revisão 1: 0 aplicado(s), 0 aguardando desembarque
2026-10-28 13:10 FALHA manifest: HTTP 404 em manifest.json     <- a última falha
```

**É exatamente o previsto, item por item:** zero aplicado (não havia o que publicar), zero
aguardando desembarque (não havia item com `publicar: false`), e a linha da revisão corrente
**não é FALHA** — que é o que a 20.4 manda conferir. As quatro falhas pararam. **O canal de
desembarque da rodametria está provado ponta a ponta**, e a primeira revisão que publicar
algo vai encontrar um log limpo em vez de uma janela cheia de ruído.

Entre o push e o `/status` subir passaram **~4 minutos**, com `raw.githubusercontent.com` já
servindo a revisão 1 desde o primeiro minuto — a **20.5** em estado puro, e aqui ela não era
cache e sim o cron esperando a hora dele (o evento de 30 minutos venceu às 13h40, depois do
de 13h10). Quem vier depois: `wp-cron.php` chamado à mão **não antecipa** evento que ainda
não venceu, e devolve **409** quando o cron já está travado.

**E os endpoints do `PROMPT.md` deixaram de ser placeholder.** Eles estavam em
`<preencher quando o snippet Rodametria Sync existir>` **com o snippet no ar**, e o passo 8
da seção 11 diz, com todas as letras, que **sem eles a seção 4 não é executável**. Agora
trazem o `/status`, o `/sync`, o gatilho por query, a base do `raw` e a ressalva da **20.5**
(revisão atrasada logo depois do push é cache do GitHub, não defeito). **O token não está no
repositório e não deve estar** — e a Fundação não precisa dele: o cron de 30 minutos é o que
desembarca.

## 2026-10-28 13h19Z–13h4xZ — **O BLOCO 2, E A DECISÃO DE ENGENHARIA QUE TIRA A ILHA DA ESPERA.** As três ferramentas especificadas inteiras, 9 constantes com procedência — e o limiar legal que a F1 não tem **isolado num objeto JSON**, para a chegada da fonte ser a edição de um arquivo e não um bloco

**O que saiu:** `dados/especificacao-calculadoras.md` (470 linhas) e
`dados/constantes.json` (**9 constantes**: 6 publicáveis, 2 `pendente` com a consequência
declarada, 1 observação de mercado). Para cada uma das três ferramentas: entradas com tipo
e exemplo pré-preenchido, saída, fórmula degrau por degrau, **o que ela se recusa a
responder**, tabela pré-renderizada, bloco de compra com o critério de entrada do produto,
e a prestação de contas da seção 7 com os grupos de recusa separados por causa.
`publicar: false` nos dois, como todo bloco de dado.

**A DECISÃO DO BLOCO, e ela é o que fica depois de hoje.** A ilha estava numa armadilha
simples: a F1 **é** a home, o produto dela **é** a categoria legal, e o texto que decide a
categoria é negado pelo egresso há duas execuções. A saída não foi esperar nem improvisar
um número — foi **separar o que depende da fonte do que não depende**. Os quatro limiares
(`LIMIAR_BIKE_W`, `LIMIAR_BIKE_KMH`, `LIMIAR_AUTOPROP_W`, `LIMIAR_AUTOPROP_KMH`) viraram
**uma constante só**, referenciada **por nome** na árvore de decisão, com **literal
numérico proibido** no código da F1. A árvore inteira, as duas ressalvas obrigatórias, a
camada municipal, o bloco de compra e o esquema do banco estão escritos e podem ser
construídos. **Quando o texto oficial chegar, a F1 destrava editando um objeto JSON** —
preencher `valor`, trocar `status`, gravar `url` e `verificado_em`. Nenhuma linha de lógica
muda. *É por isso que este bloco não esperou a fonte: o que a fonte decide é um objeto, e o
que ela não decide é tudo o mais.*

**O QUE CONTINUA TRAVADO, remedido e não herdado do campo.** Às 13h2xZ, em duas passadas:
`gov.br`, `in.gov.br`, `planalto.gov.br`, `contran.gov.br` e `lex.com.br` — **os cinco** em
`CONNECT tunnel failed, response 403`, com `rodametria.com.br` em **200** na mesma janela.
Três horas e meia depois do despacho ALTA do bloco 1, o pedido segue aberto. **A F1 não vai
ao ar**, e não vai com número de portal, não vai com o número que mais apareceu e não vai
"com ressalva" — a seção 10 proíbe constante `pendente` dentro de fórmula publicada, e aqui
a fórmula publicada é o produto da ilha. **A F2 e a F3 podem ir ao ar.**

**A ERRATA DO BLOCO 1, e ela é a razão de um despacho novo existir.** O corpus entregou à F2
*"a régua do relevo com número: 41,29 Wh/km em plano × 97,74 Wh/km a 12%"* e calculou com
ela sobre **1.200 Wh**, uma bateria de patinete. A coleta limpa de hoje achou o registro do
estudo: *"Análisis de la eficiencia energética de la batería de ion litio en una **moto
eléctrica** para el uso de micro movilidad"* — Rodrigo David Limaico Quinteros, Maestría en
Ingeniería Automotriz, UPS sede Quito, **2025**, bateria de **60 V e 30 Ah (1.800 Wh)**,
rota de **25,8 km**. **Wh/km absoluto de uma moto de 1.800 Wh não é o de um patinete de 500
Wh.** O que virou constante foi a **razão** — `97,74 ÷ 41,29 = 2,37` —, medida na mesma
rota, com o mesmo veículo e a mesma bateria, que é a única forma de um número atravessar
classe de veículo. A errata está escrita **nos dois lugares do corpus** que carregavam a
frase, com o original riscado e preservado.

**E a mesma tese deu de graça o número que faltava:** **29,8 km medidos em condição mista
contra 60 km declarados na ficha — 49,7%**. O corpus registrava *"60% a 80% do valor
anunciado"* como leitura agregada sem fonte única, e dizia ele mesmo que não servia de
constante. **A medição nomeada cai abaixo do piso daquela faixa**, e é a direção que
importa: a faixa agregada era otimista. Entra como **linha de calibração** da tabela da F2,
com autor e instituição dentro da frase, e **não** multiplica nada.

**A TERCEIRA COISA QUE A COLETA LIMPA FEZ FOI REBAIXAR UM NÚMERO DA PRÓPRIA ILHA.** O bloco
1 anotou que *"uma fonte estrangeira colhida sugere margem de pelo menos 10% acima do peso
do condutor"*, e a F3 ia nascer com essa margem atribuída a terceiro. A busca limpa — sem o
número dentro da pergunta — percorreu 13 publicadores e **não achou percentual publicado em
nenhum**. O que existe publicado é **qualitativo e convergente** em três deles, um
brasileiro: perto do teto declarado, a velocidade e a aceleração máximas não são
alcançadas. **Então a margem de 10% virou `decisao_da_ilha`, com o motivo escrito** — a
direção do erro caro aponta para a folga —, e a página nunca a atribui a ninguém. *Atribuir
a terceiro uma régua que terceiro não publicou é pior que não ter régua.* E o número não é
cosmético: 10% sobre o teto de mercado de 120 kg exclui quem passa de **109 kg**, que é
exatamente a pessoa do `VOZ.md`.

**O que a F2 deixou de poder fazer, e fica dito em vez de disfarçado:** sem régua de consumo
por km de **patinete**, ela não devolve km absoluto a partir de V e Ah. Devolve `Wh = V × Ah`
(identidade, não precisa de fonte nenhuma), a faixa degradando a autonomia **declarada** pelo
fator de relevo, e — quando a pessoa não informa a declarada — **diz que não estima km,
nomeando o que falta**. A única medição de patinete que existe (≈ 20 Wh/km, 4.000 km rodados,
70 ciclos) está em dois hosts que não resolvem nesta nuvem. Os outros três candidatos foram
reprovados **com o motivo escrito um por um** em `constantes.json`: um é de bicicleta e de
fabricante de kit, um é circular (divide a autonomia declarada pela energia, assumindo
justamente o número que a F2 existe para não assumir), e um é de moto.

**Despacho novo, prioridade NORMAL** (`dados/despachos.md`): três domínios —
`stdjet.scienceandtechnology.com.vn`, `et.vnuhcmjournal.com.vn` e `dspace.ups.edu.ec` — ou a
leitura no Chrome. **É NORMAL e não ALTA de propósito: ele melhora a F2, não a libera.** O
terceiro domínio é o mais barato dos três: ele sobe de "leitura por busca" para leitura
direta as **duas constantes publicáveis** que esta execução já gravou.

**Próximo passo desbloqueado — bloco 3, modelo do banco, e ele não depende de site NEM de
fonte bloqueada.** A seção 5 da especificação já entrega o contrato: os campos que as três
ferramentas leem, `potencia_nominal_w` e `potencia_pico_w` **separados** (a F1 só lê o
nominal), **`acelerador` como enum de TRÊS valores** — `nao_declarado` é o terceiro, com
frase própria, e **nunca** cai em "só pedal assistido" por omissão, porque é o pivô da
classificação —, `energia_wh` **derivado** de V × Ah e nunca copiado de anúncio, e
**`categoria` como campo DERIVADO da F1, nunca de entrada do catálogo**: gravar categoria à
mão é deixar o anúncio escrever a regra.

## 2026-10-28 10h17Z–10h25Z — **O BLOCO 1, E AS DUAS COISAS QUE ELE ACHOU SEM PROCURAR.** Primeira execução da Fundação nesta ilha. O corpus de buscas saiu inteiro, a **S_par deixou de ser "não medida"** — e no caminho a passada descobriu que **o site já está no ar** e que **a fonte que decide a F1 é negada pelo egresso**

**O que saiu:** `dados/corpus-buscas.md` — quatro eixos (CNH e placa · autonomia ·
carga e tamanho · produto pelo nome), **19 consultas** com procedência medida consulta a
consulta pela busca da nuvem em 28/10, seis achados nomeados, a contagem do vazamento da
busca **por eixo** e a seção 6 com o que o bloco 2 herda pronto. `publicar: false`, como
todo bloco de dado.

**A S_par ESTAVA NO DOSSIÊ COMO "NÃO MEDIDA" E ERA A PRIMEIRA TAREFA DE LEITURA DO
NASCIMENTO. Está medida, e o resultado é mais útil que "aberta" ou "fechada":** o eixo da
CNH está **tomado**, mas por **portal de trânsito e notícia** — `portaldotransito`,
`olhardigital`, `canaltech`, `motonline`, `consultadeplaca`, `doutormultas`, `gringo`,
`zuldigital`, mais folheto de duas prefeituras e PDF de duas entidades. **Nenhum varejo
grande, nenhuma loja, e em sete consultas independentes NENHUMA ferramenta** que receba
potência e velocidade e devolva a categoria. A vaga da F1 não é "ninguém fala disso": é
**"todos falam, ninguém calcula"**.

**E O MOTIVO PELO QUAL A PROSA NÃO RESOLVE É O ACHADO QUE SUSTENTA A ILHA: AS FONTES SE
CONTRADIZEM NO NÚMERO.** Três limites diferentes para a mesma pergunta, todos em fontes
que se apresentam como quem sabe — **350 W / 25 km/h** (que é regra **do Rio**, apresentada
como nacional), **1.000 W / 32 km/h** (nacional) e **4 kW / 50 km/h** (ciclomotor, sem
citar o de 1.000 W) — e uma fonte de primeira página afirmando **CNH categoria A** para
bicicleta elétrica, o contrário de todas as outras. O desacordo não é de tom: é de número,
e é o número que decide se a pessoa sai de casa habilitada.

**Os três achados que amarram a ilha, e os dois primeiros estão em título de loja grande:**
- *"**Bicicleta elétrica** aro 24 Sousa Bike **350W** freio a disco **com acelerador**"* —
  o título diz, ele mesmo, as duas coisas que a regra não deixa coexistir. Pelo que o eixo
  A mediu (as fontes convergem exatamente aqui), **acelerador manual tira o veículo da
  definição de bicicleta elétrica, mesmo abaixo do limite de potência**.
- *"**Bicicleta elétrica** Siena **1000W** adulto **sem CNH** **scooter**"* — quatro termos
  que a resolução separa, num anúncio só.
- O guia que elege **"o melhor patinete elétrico de 2026 para adultos"** descreve o
  vencedor com **dois motores de 1.000 W e 72 km/h**. Pelos limites colhidos, 72 km/h **não
  é autopropelido em nenhuma leitura**. **A página que mais aparece para "melhor patinete
  adulto" recomenda, sem dizer, um ciclomotor** — e é a frase da ilha inteira numa linha:
  *o número grande do anúncio não é o número que a regra lê.*

**O que isto muda no bloco 2, e está escrito na seção 6 do corpus:** a F1 tem **quatro**
entradas, não três — o **acelerador é pivô, não detalhe** (sem ele nenhuma potência
classifica) —, e a saída tem **duas camadas**, porque a resposta é nacional **e** municipal
(Campinas regulamenta 20 km/h; o Rio tem os 350 W/25 km/h próprios). A F1 que responder
"autopropelido, dispensa CNH" sem dizer que a rua é municipal estaria certa na categoria e
incompleta na vida. Para a F2, o eixo B entregou a régua do relevo **com número**: 41,29
Wh/km em plano contra **97,74 Wh/km a 12% de inclinação** — a reler na fonte e datar. Para
a F3, o teto de mercado está medido em **120 kg**, com a régua de margem de 10% que exclui
quem passa de 109 — e a pessoa de 110 kg do `VOZ.md` cai exatamente ali.

### O SITE JÁ ESTAVA NO AR, E O `ESTADO.md` DIZIA "PENDENTE" — a seção 4 em ação, no primeiro dia da ilha

A conferência de rede da **20.2** era para ser barata e de rotina. Devolveu **200 em três
tentativas**, com `<title>Rodametria - Mobilidade elétrica</title>` e `last-modified` de
**27/10 às 22h17Z** — ou seja, o WordPress subiu **cinco horas depois** de a ilha nascer, e
o cabeçalho que esta execução leu ainda dizia *"WordPress: pendente"*, *"nameservers
pendente"*, *"hospedagem pendente"* e *"lista de domínios permitidos pendente"*. **Nenhum
dos quatro estava pendente.** É a seção 4 no estado puro, e no dia 1: o site anda e o
cabeçalho fica para trás em silêncio.

**O que de fato falta, medido e não herdado:** tema de blocos cru, **zero página
publicada**, `/wp-sitemap.xml` sem URL nenhuma, e `/wp-json/rodametria/v1/status` em **404**
— o snippet de Sync não existe. O que está **são**: `/wp-json/` em 200 e
`/nao-existe-xyz/` devolvendo **404 de verdade**, então a porta de entrada da seção 29 passa
nesta primeira leitura (vale reconferir quando houver página, que é quando o `.htaccess`
costuma cair).

### A FONTE QUE DECIDE O PRODUTO DESTA ILHA É NEGADA PELO EGRESSO (20.3)

O `PROMPT.md` desta ilha é explícito: a constante central da F1 *"só vira `publicavel`
depois de lida no texto oficial do gov.br, com data"*. Medido às 10h4xZ: `www.gov.br` e
`lex.com.br` em **`000` com `connect_rejected`**, e a busca de página falha na própria
resolução de nome (`ENOTFOUND www.gov.br`). **Não é intermitência de túnel** — a 20.2 manda
repetir antes de chamar de bloqueio, e aqui a repetição não muda nada, porque o erro
nomeado pelo egresso é recusa. É a **20.3** em estado puro: a regra que exige a fonte foi
escrita em 27/10 e a fonte nunca foi conferida.

**A consequência, dita sem maquiagem:** o bloco 2 pode ser escrito inteiro daqui, e
`constantes.json` pode nascer com a constante da F1 marcada `publicavel: false` e a dívida
nomeada. **O que não pode é a F1 ir ao ar classificando veículo com número de portal de
notícia** — numa ilha onde errar manda a pessoa para a rua sem habilitação. Virou despacho
**ALTA** em `dados/despachos.md`, com os dois gestos que o resolvem (liberar `gov.br` na
lista de rede, **ou** colar as três definições literais com URL e data). **E a ilha NÃO
recebeu `bloqueada_por`** (seção 11, passo 4): travou uma fonte, não a ilha.

### A 30.8 MEDIDA NUMA ILHA NOVA, COM A CONTAGEM QUE FALTAVA: O VAZAMENTO NÃO É PARELHO ENTRE EIXOS

| eixo | ocupantes de fora do Brasil |
|---|---|
| **CNH e placa** (regra brasileira) | **zero** em 7 consultas |
| produto pelo nome | 3 de ~18 |
| carga e tamanho | 6 de ~17 |
| **autonomia** | **~40 de ~50**, e uma consulta com **zero** ocupante brasileiro |
| **peças** (câmara, pneu, carregador) | **18 de 20** em `pccomponentes.pt` |

**A leitura vale para as outras cinco ilhas, e é por isso que está escrita e não só
sentida:** pergunta de **regra brasileira** não tem equivalente em Portugal ou na Espanha,
então a busca da nuvem não tem para onde vazar e a procedência é confiável; pergunta de
**produto e consumível** tem catálogo europeu idêntico, e aí a busca entrega Portugal. **O
vazamento é mínimo exatamente onde esta ilha nasce** — o que é sorte, não desenho, e vale
dito para a próxima Bússola saber que eixo de regra é o mais barato de medir da nuvem. E,
pela assimetria da 30.8, **nada disso autoriza `alvo`**: nenhuma linha do corpus diz `alvo`,
nem no eixo A. A SERP dos eixos de autonomia, carga e peças virou despacho NORMAL.

### Nada foi ao ar, e não podia

A ilha tem WordPress e não tem casca, snippet de Sync, `/status` nem URL própria. Acionar
Sync e conferir no ar era impossível, e dizer que conferi seria inventar. Este bloco é
dado: `publicar: false`, zero URL, zero revisão. A **31.1** não se move por ele.

**Próximo passo desbloqueado:** **bloco 2 — especificação das ferramentas**
(`dados/especificacao-calculadoras.md` + `dados/constantes.json`), na ordem obrigatória F1,
F2, F3. Ele pode ser escrito inteiro desta nuvem e **herda da seção 6 do corpus** as quatro
entradas da F1, as duas camadas de saída, a régua do relevo da F2 e o teto de 120 kg da F3.
**A constante legal da F1 nasce `publicavel: false`** até o despacho ALTA de 28/10 ser
atendido — e quem fechar o bloco 2 lê a seção 4 do corpus antes, para não ler a tabela do
eixo A como se fosse a resolução.
