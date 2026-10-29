# Registro de execuções — Rodametria

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

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
