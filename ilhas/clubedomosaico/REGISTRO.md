# Registro de execucoes — Clube do Mosaico

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e o
proximo passo desbloqueado.

02/10/2026 19h16Z — O BLOCO 4c: A PRIMEIRA CATEGORIA DO GUIA NASCEU, E NASCEU COM AS TRÊS FILHAS

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **19h16Z** e push da reserva aceito na
primeira tentativa (`e52777e`). `executando_desde` estava `null` e o último commit da ilha era de
16h56Z, duas horas e vinte antes — pela 1.1, ilha livre sem desempate.

**Quatro URLs novas**, a ilha vai de **17 para 21**. Casca na **1.19.0** sem mudança; snippet novo
`Clube do Mosaico Guia` **1.0.0**; manifest na **revisão 56**.

## A PORTA DE ENTRADA, ANTES DO BLOCO (seção 20.2)

`https://clubedomosaico.com.br/` em **200** na primeira tentativa. A ronda técnica da Sentinela
tinha fechado às 14h51Z com 17 de 17 URLs em 200 e zero defeito novo; este bloco não remediu o que
ela mediu há quatro horas.

## O BLOCO: `acabamento`, a mãe e as três filhas

**Quem escolheu a categoria não foi esta execução — foi o `cruzamento-14-9.py`**, escrito às 16h2xZ
de hoje. `acabamento` é o único recorte desta ilha em que os **dois** portões da 14.9 abriram ao
mesmo tempo, na mãe **e** nas três filhas:

| recorte | dado (seção 9) | SERP (14.9) | veredito |
|---|---|---|---|
| `acabamento` | passa, 10 itens | ABERTA | **pode_nascer** |
| `acabamento/selador` | passa, 3 itens | ABERTA | **pode_nascer** |
| `acabamento/verniz` | passa, 4 itens | ABERTA | **pode_nascer** |
| `acabamento/impermeabilizante` | passa, 3 itens | ABERTA | **pode_nascer** |

As quatro saem numa leva só porque é o que a **16.6** manda — *"primeiro a mãe e suas 3 primeiras
filhas"*, nunca uma filha de cada categoria espalhada —, e porque a **16.5** só deixa a mãe nascer
com três filhas. A `alicate/cortador_de_azulejo`, que também está em `pode_nascer`, **ficou de
fora**: a mãe dela está em `espera_serp` e uma filha sozinha pendurada em `/materiais/` seria
cluster ralo, que é exatamente o que a 16.6 proíbe.

**A ÁRVORE DESTA ILHA SERVE TRÊS SEGMENTOS PELA PRIMEIRA VEZ.** As quatro páginas de nível 3 que
existiam antes — as duas ferramentas e as duas técnicas — vivem em dois segmentos por estado de
transição declarado: a categoria delas não existia quando nasceram, e a 12.1 proíbe mover URL
publicada. Este é o primeiro bloco em que a **categoria nasce antes da filha**, e por isso o
primeiro que não precisa do estado de transição. Endereços:

- `/materiais/acabamento/` — nível 2, mãe `/materiais/`
- `/materiais/acabamento/selar-a-base-antes-de-fazer-mosaico/`
- `/materiais/acabamento/verniz-para-peca-de-mosaico/`
- `/materiais/acabamento/impermeabilizar-peca-de-mosaico/`

## O NÚMERO CALCULADO DA SEÇÃO 9, E ELE NÃO FOI ESCOLHIDO PARA PREENCHER O PORTÃO

É a **cobertura declarada**: das **15 superfícies** que o vocabulário do esquema nomeia (9 bases e 6
caquinhos), quantas a frase do próprio fabricante de cada produto alcança — e, portanto, quantas ele
não alcança. Contado, por página, do banco:

| página | produtos | combinações | nomeadas | superfícies alcançadas |
|---|---|---|---|---|
| `acabamento` (mãe) | 10 | 150 | **13** | 4 de 15 |
| `selador` | 3 | 45 | **4** | 3 de 15 |
| `verniz` | 4 | 60 | **2** | 1 de 15 |
| `impermeabilizante` | 3 | 45 | **7** | 3 de 15 |

**Este número é literalmente o que a medição de SERP de hoje chamou de "o número que a SERP não
publica".** Os dez resultados que ocupam a consulta de impermeabilizante dizem *emulsão de
silicone*, *tinta betuminosa duas ou mais demãos* e *silicone ou verniz*: tipo de produto, sem
marca, sem produto e sem número. Nenhum deles diz **sobre o quê** o fabricante escreveu que o
produto pode ir. A ausência medida é o produto desta ilha.

**O SEGUNDO NÚMERO É O RELÓGIO**, aritmética desta ilha sobre três declarações, no mesmo desenho dos
gramas de rejunte da F1: `(demãos − 1) × intervalo entre demãos + secagem final`. Ele fecha em
**2 dos 10** produtos e **só neles** — o Selador Acrílico da Coral (1 demão, 5 h) e a Resina Acrílica
da Coral (3 demãos, 4 h entre elas, 12 h final: **20 horas**). Nos outros oito falta uma das
parcelas e a página **diz que o fabricante não declara**, em vez de emprestar o número do vizinho de
prateleira — que é o erro escrito dentro do próprio `quartzolit-fundo-selador`, no registro dele.

## O QUE ESTAS PÁGINAS SE RECUSAM A FAZER, E A RECUSA É CONTADA

Nenhuma linha deste snippet **escolhe produto para uma base**. Não é omissão: é o esquema.
`regras_da_categoria_acabamento` diz, desde 25/09, que acabamento não entra na matriz base ×
ambiente, porque *"acabamento não adere duas coisas uma na outra e não se escolhe por ambiente
declarado"* — e por isso todo registro da categoria nasce com as seis listas de `declaracoes`
vazias, o que é portão no `validar-banco.py`. Montar uma régua de "qual verniz para qual peça" em
cima de declarações que não falam de peça de mosaico seria inventar a recomendação.

E a lacuna é **derivada**, não escrita: o vidro, a pastilha de vidro e o rejunte entram na frase
porque a conta diz que faltam. No dia em que um fabricante nomear vidro, a frase do vidro some
sozinha — e **a bateria de mutações fabrica esse dia e exige que ela suma**.

## A DÍVIDA QUE ESTE BLOCO ACHOU NO CAMINHO, E ELA NÃO ERA DESTA CATEGORIA

**O banco de `acabamento` nunca tinha sido lido por uma página, e por isso estava sem acento.**
`ferramentas/restaurar-acentos.py` existe desde 11/09 exatamente para isto, e o cabeçalho dele diz
com estas palavras: *"o banco nasceu sem acento porque foi digitado a partir de busca, e até aqui
ele só era lido por ferramenta; no dia em que uma PÁGINA passou a servi-lo, o defeito virou texto no
ar"*. Hoje foi esse dia. `CAMPOS_DE_TELA` via `marca`, `fabricante` e `nome_comercial`, e a
declaração do fabricante de `acabamento` mora em `protecao.literal_do_fabricante` — campo que
nenhuma outra categoria tem, criado em 25/09.

- O alcance cresceu para `protecao.literal_do_fabricante`, `protecao.trecho_que_declara_o_momento` e
  `propriedades.*.valor`. O `declarado_como` e o `motivo` **ficaram de fora de propósito**: a página
  publica o **número**, não a frase de onde ele saiu, e acentuar o que ninguém lê é alargar a
  superfície sem ganho.
- **41 palavras** entraram no mapa, uma a uma, só aquelas cuja forma acentuada é a única leitura
  possível; **164** foram para `_CONHECIDAS` porque não precisam de acento. **21 trocas gravadas**,
  e o `--provar` aprovou: reduzidas a sem-diacrítico, as 21 são byte a byte iguais às de antes.
- Duas das trocas são de **outros bancos** (`flexível` na pastilhart, `manutenção` na cortag): elas
  não chegam à tela hoje, mas o campo passou a ser de tela e a categoria delas nasce depois — foi a
  ordem inversa que criou aquela ferramenta.
- O aviso de palavras fora do mapa fecha hoje em **zero**, pela primeira vez.

## DOIS PORTÕES DA ILHA ESTAVAM CRAVADOS NO "HOJE", E OS DOIS FORAM DERIVADOS

Os dois reprovaram a casca por ela estar **certa** — e os dois reprovariam qualquer bloco que fizesse
a ilha crescer:

1. **`nenhum cartao de categoria e link hoje (16.5)`**, cravado em `0 === $viraram_link`. A 16.5 não
   diz "nenhum cartão abre"; ela diz que cartão **sem página** não vira link. Agora o esperado é a
   contagem de categorias que têm página declarada, e ela cresce sozinha.
2. **`os blocos de recusa sao poucos e contados`**, com teto **4**, que era o retrato de uma ilha de
   nove páginas. Ele teria reprovado esta leva por existir — quatro páginas novas, uma recusa cada,
   todas legítimas. Virou **no máximo um bloco de recusa por página**, medido por página.

**E UMA MUTAÇÃO ESTAVA INERTE DESDE 28/09, achada de passagem:** `noindex na pagina errada`, em
`mutacoes-voz-e-cabeca.py`, casava a entrada da página `materiais` escrita em **uma linha só**; na
casca 1.16.0, de 28/09, aquela entrada ganhou o campo `descricao` e virou várias linhas. É a mesma
família — e o mesmo dia — do que o bloco de 28/09 achou em `mutacoes-arvore.py`. O conserto é não
casar mais a linha inteira.

## AS DUAS BANCADAS NOVAS, E O QUE A SEGUNDA ACHOU NA PRIMEIRA

- **`ferramentas/teste-guia.php`** — **106 afirmações, 0 falha**. O portão da 14.9 **nos dois
  sentidos** (nenhuma página sem autorização **e** nenhum recorte autorizado sem página, que é a
  metade que impede a família de parar calada); a cobertura e o relógio recontados do JSON cru por um
  caminho que não chama uma linha do snippet, conferidos contra o número **na tela**; a prestação de
  contas da seção 7; a 16.4(a) com a consulta-alvo como texto-âncora e a 16.4(b) com a mãe linkada no
  **corpo**, fora dos `<nav>`; o `rel` de cada link derivado do que o link **é**; a frase da lacuna.
- **`ferramentas/mutacoes-guia.py`** — **14 mutações, 14 decididas certo**. Onze reprovam, uma fica
  honesta (banco fora do ar), uma degrada (F2 fora do ar) e uma **passa** (um fabricante nomeia vidro
  e a lacuna some sozinha).
- **E a bateria achou TRÊS buracos na bancada recém-escrita, na primeira passada**, que é o motivo de
  ela existir: (a) a frase da lacuna podia virar lista escrita à mão e passar; (b) a busca **crua**
  podia se declarar `sponsored` e passar — a régua media "tem rel", não "tem o rel certo"; (c) a
  própria mutação do vidro media o corpo inteiro em vez da frase. Os três viraram portão.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Nenhuma das quatro declara promessa no `<title>`.** A alavanca da 12.1 é para a banda de posição
  4 a 10: título que promete número numa página que já está na primeira página e não é clicada. Estas
  nascem hoje, sem impressão e sem posição — não há CTR a consertar. O portão que cobra a lista
  inteira de páginas com promessa, nas duas direções, foi quem apontou isso.
- **A faixa de volume das consultas continua `null`.** O Planejador é do Raphael e o pedido está em
  `dados/despachos.md`. Ela não decide se a página nasce; decide a ordem da leva (1.2-b.3) — e a
  execução das 16h2xZ já tinha escrito que quem publicasse o 4c podia publicar sem ela e **não podia
  estimá-la**.
- **Nenhuma URL antiga se moveu**, nenhum 301, nenhum `<title>` e nenhuma `description` existente
  foram tocados: a janela de comparação do BLOCO A, que fecha em **08/10**, continua limpa.

## O DESEMBARQUE E A VERIFICAÇÃO NO AR (seção 8 e 18.4)

Sync acionado por `curl` às **19h52Z**: *revisão 56, 15 aplicados*, `snippets/guia: ok (snippet #13
criado)`. `/status` na **revisão 56**, igual à do `manifest.json`. As quatro URLs novas em **200**,
com quebra de cache. `conferir-no-ar.py` **APROVADO: 524 afirmações medidas no HTML servido, 0
falha** — agora sobre **21** URLs do sitemap, com as quatro novas dentro da faixa de 120–160 na
`description`, no teto de 65 no `<title>`, com JSON-LD, `BreadcrumbList` e sem `&#038;` dentro de
`<script>`. O soft 404 na borda **continua** e segue com o Raphael desde 29/09: registro, não portão.

**E um rótulo do próprio `conferir-no-ar.py` estava cravado**, achado na saída desta verificação:
quatro linhas diziam *"as 17 URLs"* com a medida ao lado dizendo **21**, na mesma linha. O portão
sempre varreu `_urls_sitemap` inteiro e estava **certo** — só o texto envelheceu. Mas rótulo que
discorda da medida ao lado é o que faz alguém ler "17" e não contar. Passou a sair do `len()`.

As cinco baterias de mutação que este bloco podia ter quebrado foram rodadas e as cinco fecham
verdes: `mutacoes-arvore` 29/29, `mutacoes-voz-e-cabeca` **24/24 depois do conserto das três
inertes**, `mutacoes-promessa-do-titulo` 19/19, `mutacoes-acabamento` 14/14 e `mutacoes-guia` 14/14.

## PRÓXIMO PASSO DESBLOQUEADO

**Medir a SERP das três mães em `espera_serp` — `alicate`, `pastilha` e `rejunte`.** É o estado que
parece passe livre (dado verde, SERP nunca olhada) e é o trabalho mais barato que sobrou nesta fila:
é **busca, não coleta**. Com a SERP de `alicate` medida, a `alicate/cortador_de_azulejo` — que já
está em `pode_nascer` — ganha mãe e a segunda categoria do Guia pode sair com a mesma leva de
quatro. O caminho agora é um comando: `python3 ferramentas/cruzamento-14-9.py` depois de escrever a
medição em `dados/serp-das-filhas.json`, e o veredito sai calculado.

02/10/2026 16h17Z — O PORTÃO DE SERP DEIXOU DE SER PROSA, E O 4c DE `acabamento` ESTÁ LIBERADO PELOS DOIS PORTÕES

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **16h17Z** e push da reserva aceito na
primeira tentativa (`2d16710`). Manifest e `/status` seguem na **revisão 55**: este bloco **não
mudou nada que o Sync publique** — nenhuma URL nova (a ilha segue em **17**), nenhum endereço,
nenhum `<title>` e nenhuma `description`. A janela de comparação do BLOCO A continua limpa e o
veredito dele segue de **08/10**. Por isso não houve acionamento do Sync: não havia o que
desembarcar.

## A PORTA DE ENTRADA, ANTES DO BLOCO (seção 29.2)

`conferir-no-ar.py` **APROVADO: 524 afirmações, 0 falha**, antes de qualquer mudança. As 17 URLs do
sitemap em 200, as 17 descriptions na faixa de 120–160, os títulos no teto de 65, `/status` igual ao
`manifest.json`. O soft 404 na borda **continua** — registro e não portão, com dono escrito desde
29/09.

## O BLOCO: O CRUZAMENTO DA 14.9 VIROU PORTÃO, E ELE ABRIU O 4c NUMA CATEGORIA

**O que a execução das 13h17Z deixou escrito, palavra por palavra:** *"o portão de DADO abriu, o de
SERP é outro. (...) Quem publicar o 4c cruza os dois, como a 14.9 manda."* Este bloco cruzou — e
descobriu que **cruzar era o problema**, não o resultado.

**O DIAGNÓSTICO, e ele é de arquitetura:** as duas metades da 14.9 existiam desde 30/09 e nunca se
encontraram num veredito. O portão de **dado** da seção 9 era número derivado do banco
(`dados/filhas-do-guia.json`). O portão de **SERP** era **prosa**, numa seção de
`dados/filhas-do-guia.md` que o gerador preserva **sem ler** — e o próprio cabeçalho daquele gerador
diz, de si mesmo, que *"não classifica SERP"*. **Prosa não cruza com número.** O custo é datado: a
pergunta "o 4c pode nascer?" exigia abrir dois arquivos e fazer a conta na cabeça, e o `ESTADO.md`
das 13h17Z teve de escrever **à mão** o aviso para a execução seguinte não ler passe livre. Aviso à
mão é o que um portão substitui.

**A MEDIÇÃO QUE FALTAVA — duas filhas que nunca tiveram SERP olhada, e a mãe também não.** Quatro
consultas novas, com os três limites do canal respeitados (frase inequivocamente portuguesa, nenhuma
marca dentro da consulta, e sem afirmar posição de ninguém, porque este canal não dá ordem):

| recorte | consulta | quem ocupa | classe |
|---|---|---|---|
| `acabamento` (a mãe) | *acabamento para peça de mosaico artesanal qual produto passar depois do rejunte* | Catraca Livre, Benjoino (2010), NeuralWord, **mosaico.arq.br (4, e é obra)**, Artesanato Passo a Passo, Portal das Maravilhas, Artesanato Local (2010) | **ABERTA** |
| `acabamento/selador` | *precisa passar selador na base antes de colar mosaico em MDF ou cerâmica* | 9 dos 10 são **pintura de parede** | **ABERTA, SEM INTENÇÃO NA SERP** |
| `acabamento/selador` | *selar vaso de cerâmica antes de fazer mosaico artesanato precisa selador* | Cenário Tocantins, Viva Decora, Sua Decoração, umComo, Terra, Limpeza.com, Wikipedia | **ABERTA** |
| `acabamento/impermeabilizante` | *como impermeabilizar peça de mosaico para ficar no jardim na chuva* | forumdacasa.com PT (2), Benjoino (2010), FazFácil (2), Casas Jardim, Redelease, soudal.pt | **ABERTA** |

**Zero marketplace nas quatro.** E a classe da segunda linha **é nova**, e nasceu da medição em vez
de ter sido escolhida: `ABERTA_SEM_INTENCAO_NA_SERP` diz que ninguém ocupa **porque nenhum resultado
do top 10 fala da pergunta desta ilha** — a SERP respondeu o nicho vizinho da pintura de parede.
Chance alta e intenção **não provada**, que é literalmente a metade *"chance alta sem intenção"* que
a 14.9 nomeia e que a legenda de três classes do corpus não sabia descrever. Ela entrou na legenda.

**O QUE FOI CONSTRUÍDO, e é o que fica depois do veredito de hoje:**

- **`dados/serp-das-filhas.json`** — a metade **coletada**, agora em dado: dez medições, com quem
  ocupa escrito pelo nome, data **por medição**, os três limites do canal declarados, as cinco
  classificações e o número que a SERP não publica. **As seis medições de 30/09 foram movidas para
  cá sem uma palavra alterada.**
- **`ferramentas/cruzamento-14-9.py`** — o portão. Lê as duas metades de arquivos diferentes e
  devolve **um** veredito por recorte, dos seis que **calcula e nunca escreve**: `pode_nascer`,
  `pode_nascer_sem_demanda_medida`, `espera_autoridade`, `espera_dado`, `espera_serp`, `nunca`.
  Bancada: **`--autoteste` com 32 casos fabricados, 0 falha**, e `--conferir` que regera e compara.
- **`dados/cruzamento-14-9.md`** — a saída, derivada e não digitada.
- **A segunda verdade foi apagada:** a tabela de SERP em prosa saiu de `dados/filhas-do-guia.md` e o
  que ficou ali é um ponteiro para os dois arquivos novos, com o motivo. **Uma fonte por campo.**

## O VEREDITO: `acabamento` É A PRIMEIRA CATEGORIA DO GUIA A PASSAR OS DOIS PORTÕES

| recorte | dado | SERP | veredito |
|---|---|---|---|
| `acabamento` (a mãe, que é o 4c) | `passa`, 10 itens | ABERTA | **`pode_nascer`** |
| `acabamento/verniz` | `passa`, 4 itens | ABERTA | **`pode_nascer`** |
| `acabamento/selador` | `passa`, 3 itens | ABERTA | **`pode_nascer`** |
| `acabamento/impermeabilizante` | `passa`, 3 itens | ABERTA | **`pode_nascer`** |
| `alicate/cortador_de_azulejo` | `passa`, 3 itens | ABERTA | **`pode_nascer`** |
| `pastilha/vidro` | `passa`, 13 itens | TOMADA | `espera_autoridade` |

Dos 42 recortes: **5 `pode_nascer`**, 1 `espera_autoridade`, 3 `espera_serp`, 33
`sem_nenhum_dos_dois`. **A ordem da 7b — banco, depois as filhas de nível 3, só então a mãe de nível
2 — foi percorrida inteira numa categoria pela primeira vez desde 12/09.**

## O ACHADO QUE VALE MAIS QUE O VEREDITO: A 16.5 CONTA FILHA, E FILHA NÃO É FILHA NO DADO

A 16.5 exige 3 filhas de nível 3 para a mãe nascer, e até hoje "filha" era lida na contagem do
**dado**. O cruzamento põe as duas contagens lado a lado e elas **discordam**:

| categoria | filhas que o DADO autoriza | filhas que o CRUZAMENTO autoriza |
|---|---|---|
| `acabamento` | 3 | **3** → a mãe pode nascer |
| `pastilha` | 1 | **0** |

**A `pastilha` é a de mais banco da ilha** — 13 itens, três números em 12 deles — e a filha dela que
passa no dado é justamente a que a SERP recusa. Pela contagem do dado ela estava a **duas** filhas da
mãe; pelo cruzamento, a **três**. Nenhum dos dois arquivos de entrada mostra isso sozinho, e o caso
tem autoteste próprio na bateria (`3 filhas verdes no dado e 2 no cruzamento`, mais o caso da **mãe
TOMADA com 3 filhas abertas**, que sem o portão faria a mãe nascer para uma SERP de marketplace).

**E três recortes ficaram com `espera_serp` — `alicate`, `pastilha` e `rejunte`, as três mães: dado
verde e SERP nunca olhada.** Esse veredito existe por nome próprio porque é **o estado que parece
passe livre**. Medir as três é busca, não coleta de banco: é o trabalho mais barato que sobrou nesta
fila.

## O DEFEITO QUE A PRÓPRIA EXECUÇÃO ACHOU, ANTES DE QUALQUER COMMIT

A primeira versão do `cruzamento-14-9.py` cravava, no veredito `sem_nenhum_dos_dois`, a frase *"os
dois: nem 3 itens de banco, nem SERP medida"* — e ela era **FALSA** em `alicate/torques` e
`rejunte/cimenticio`, que **têm** 3 itens e param por lastro e por número comum, não por contagem.
Achado lendo o documento gerado, não por portão. Corrigido extraindo `falta_no_dado()`, que **deriva**
a frase da distância que o portão de dado já mediu, e agora as duas saem certas: *"2 itens com fonte
que sustente recomendação primária"* e *"um número que a página calcule sobre 3 itens do mesmo
recorte (a propriedade mais perto é `liberacao_area_molhada_h`)"*. **A lição é a de sempre nesta
ilha: frase cravada envelhece calada; frase derivada não.**

## O PEDIDO AO RAPHAEL É DERIVADO, E A FAIXA NÃO FOI ESTIMADA

Nenhuma das **seis** consultas abertas tem faixa de volume. O Planejador está na conta dele, a nuvem
não abre painel autenticado, e o campo ficou **`null` nos dez registros** em vez de preenchido por
palpite — que é o que o cabeçalho do `corpus-buscas.md` já proibia para o CPC desde 10/09. O pedido
entrou em `dados/despachos.md` com a lista **derivada pela ferramenta**, consulta por consulta, com o
recorte que a exige; e só consulta ABERTA entra, porque faixa de consulta que não vai nascer é número
que ninguém usa. O portão confere sozinho: `Pedido de faixa ao Raphael: N` encolhe quando o número
chega, **não quando alguém edita a lista**.

**E está escrito que não é bloqueio:** a faixa **não decide se a página nasce** — decide a **ORDEM da
leva**, que é o que a 1.2-b.3 manda sair da medição e não da rotação. Quem pegar o 4c de `acabamento`
pode publicar sem ela.

## O RÓTULO VELHO QUE O CRUZAMENTO DERRUBOU NO CORPUS

A medição de 30/09 deixou escrito que o corpus classificava `pastilhas de vidro para mosaico` como
**ABERTA** com a **mesma evidência** que a régua da 14.9 lê como **TOMADA**, e mandava: *"quem for
mexer no corpus lê este parágrafo primeiro"*. **Mexido hoje:** o rótulo daquela linha virou
`~~ABERTA~~ → TOMADA`, com a evidência **intacta** e a diferença entre as duas réguas escrita na
própria linha — o corpus chamou de aberta porque ninguém responde a pergunta técnica, e a 14.9 manda
classificar **quem ocupa**, que é o galho do *"a página NÃO nasce agora"*. **O achado do bloco de
10/09 continua inteiro; o que ele nunca foi é autorização para a página nascer.** E as cinco consultas
de `acabamento` entraram na seção 1E, com a SERP **citada** daqui e a fonte no JSON novo.

## BANCADA

`conferir-no-ar.py` **524 afirmações, 0 falha** (antes do bloco) · `validar-banco.py` verde, 41
materiais · `validar-pastilhas.py` 189 afirmações, 0 falha · `cobertura.py --conferir` OK ·
`filhas-do-guia.py --conferir` aprovado nas três pernas e `--autoteste` 27 casos 0 falha ·
`cruzamento-14-9.py --conferir` aprovado e **`--autoteste` 32 casos 0 falha** · mutações:
acabamento 14, base 20, apoio 24, degrau 8, motivo-degrau-4 10, batismo 14, casamento 5, árvore 29,
pastilhas 14, cobertura 14 — **todas reprovaram, nenhuma passou** · `atualizar-manifest.py --gravar`
com os 5 sha impressos, e ele **acusou a ferramenta nova fora do manifest** antes de eu a registrar,
que é o portão dele funcionando.

O soft 404 na borda **continua** e segue com o Raphael desde 29/09 — vermelho esperado, com dono.

---

02/10/2026 13h17Z — A PRIMEIRA CATEGORIA DO GUIA A ALCANÇAR AS 3 FILHAS DA 16.5, E QUATRO FERRAMENTAS QUE MEDIAM MENOS DO QUE PROMETIAM

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h17Z** e push aceito na primeira
tentativa. Manifest e `/status` na **revisão 55**. **NENHUMA URL NOVA** — a ilha segue em 17 —, e
**nenhum `<title>` e nenhuma `description` foram tocados**: a janela de comparação do BLOCO A
continua limpa e o veredito dele segue de **08/10**.

## A PORTA DE ENTRADA, ANTES DE QUALQUER BLOCO (seção 29.2)

Rede pela **20.2**, antes de trabalhar: `clubedomosaico.com.br` em **200**; o `/status` da rota REST
em **200** na revisão 54, igual à do manifest daquele momento. `conferir-no-ar.py`: **524 afirmações,
0 falha** na origem. `leitura-do-visitante.py` segue **REPROVADO pelo soft 404 da borda** — 404 na 1ª
leitura, 200 na 2ª com `x-proxy-cache HIT` e `max-age=7200` —, que é **vermelho esperado, com dono
escrito** desde 29/09 e fora do alcance de qualquer snippet daqui. **Nenhum defeito novo.**

## O BLOCO: O PRÓXIMO PASSO QUE O REGISTRO DE 30/09 DEIXOU ESCRITO, E ELE SAIU INTEIRO

O registro de 30/09 às 13h17Z fechou nomeando o passo: *"coletar **1 impermeabilizante e 2
seladores** fecha as **3 filhas de `acabamento`**, que é a categoria mais barata do Guia, e é o que
abre a primeira mãe de nível 2 desta ilha — o **4c**, parado desde 12/09"*. Saiu, e saiu inteiro.

**Entraram três registros**, por busca restrita ao domínio do fabricante, **duas passadas por SKU,
escritas de forma diferente e nenhuma delas carregando um valor** — as consultas pediram os
**rótulos** da ficha ("indicado para", "demãos", "rendimento", "secagem", "diluição", "composição",
"não indicado para"), que é o método que a categoria usou em 25/09:

| registro | tipo | o que a frase do fabricante nomeia |
|---|---|---|
| `suvinil-seladora-para-madeira` | selador | **`mdf_madeira`** — "superfícies internas não molháveis de madeira" |
| `coral-selador-acrilico` | selador | `alvenaria_tijolo` — "as mais diversas superfícies de alvenaria" |
| `coral-resina-acrilica` | impermeabilizante | `cimento_concreto`, `alvenaria_tijolo` e a tessela **`pedra`** |

**O NÚMERO QUE MOVEU, e ele é o portão e não a contagem:** `acabamento/selador` saiu de **1 para 3**
itens e `acabamento/impermeabilizante` de **2 para 3**, os dois **com lastro** (fonte de nível ≤ 3) e
os dois **com número calculável sobre o recorte inteiro** — `tempo_de_secagem_h` nos três seladores
(6 h, 2 h e 5 h) e `base_quimica` nos três impermeabilizantes (duas resinas acrílicas e um
silano-siloxano). Com `acabamento/verniz`, que já passava, **são 3 filhas de 3**, e
`dados/filhas-do-guia.json` registra `acabamento` como a **única categoria do Guia que alcança as 3
da 16.5**. Recortes que podem nascer hoje: de 7 para **9**.

**E os três NASCERAM NO DEGRAU 3, não no 4.** `coletar-shopee.py --ensaio` casou anúncio para os três
na primeira tentativa, e `--gravar` deu `url`, `url_produto` e **foto medida** a cada um — o caminho
normal de registro novo que o item 5 da fila já tinha deixado pronto, sem uma linha de código nova.
Banco em **41 materiais**, escada **1:1 · 2:5 · 3:18 · 4:17**, e o `motivo_sem_ficha` do degrau 4
segue em **17 de 17** porque nenhum dos três entrou lá.

## A DECISÃO DE ESQUEMA SAIU ANTES DA COLETA, QUE É O QUE A 1.2-b.4 EXIGE

A passada de 30/09 deixou a pergunta escrita como **pré-requisito**: *"quem coletar decide antes se
selador de alvenaria cabe em `regras_da_categoria_acabamento`, que é decisão de esquema e não de
coleta"*. **Decidido, e por escrito antes dos três registros entrarem — esquema na versão 10.** Cabe,
e o motivo não é tolerância: a seção define selador pelo **MOMENTO** ("na base ANTES de colar"), nunca
pelo substrato, e `alvenaria_tijolo` e `cimento_concreto` são **dois dos nove** valores de
`vocabularios.base` desta ilha. Recusar selador de alvenaria deixaria essas duas bases sem preparo
declarado **por decisão de esquema, não por falta de fonte**. O que não muda é
`o_que_esta_categoria_NAO_pode_sustentar`, e a trava disso não é a decisão: é a lista
`bases_do_vocabulario_que_a_frase_NAO_nomeia`, que cobre o vocabulário inteiro e não deixa o silêncio
passar. **Critério escrito depois do dado é critério dobrado para caber no dado que veio.**

## DOIS ACHADOS DE DECLARAÇÃO, E ELES VALEM MAIS QUE A CONTAGEM QUE FECHARAM

- **O selador deixou de ser um item que não serve MDF.** A observação de 25/09 estava escrita no
  dado: *"a categoria `selador` entra no banco com UM item, e ele não serve a base que a ilha mais
  usa"*. O `suvinil-seladora-para-madeira` é o **primeiro acabamento deste banco a nomear
  `mdf_madeira`** — a base mais comum da peça do ateliê. A faixa descoberta da categoria passou a ter
  dono.
- **A primeira frase de acabamento a nomear uma TESSELA, e ela vem com uma EXCLUSÃO.** A Resina
  Acrílica da Coral nomeia **`pedra`** ("pedras naturais"), e nenhum dos sete anteriores nomeava
  tessela nenhuma. No mesmo parágrafo o fabricante escreve que **não se recomenda o uso em superfícies
  horizontais** — e **tampo de mesa e centro de mesa são duas das coleções de uso da Loja desta
  ilha**. Nenhuma frase publicada pode indicar esse produto para peça horizontal, e o motivo é
  declaração do fabricante, não cautela nossa. É o lado que esta ilha quase nunca consegue citar.

**O QUE CONTINUA ABERTO, e agora está medido em dez em vez de sete:** das **dez** frases de
fabricante desta categoria, **zero nomeiam `vidro`** e **zero nomeiam rejunte** — as duas superfícies
que a peça de mosaico pronta expõe. A pendência `acabamento-nenhum-nomeia-vidro-nem-rejunte` fica
aberta, com uma tessela a menos de buraco.

## QUATRO DEFEITOS ACHADOS DE PASSAGEM, OS QUATRO DE ALCANCE, OS QUATRO NO MESMO COMMIT

Nenhum deles foi procurado; os quatro apareceram porque o bloco de hoje passou por eles. E os quatro
são da mesma família: **ferramenta que mede menos do que promete, e fecha verde.**

1. **`gerar-links-afiliado.py` datava os links com uma constante de 25/09.** A linha era
   `HOJE = '2026-09-25'`, digitada no dia em que a ferramenta nasceu, e é ela que vira
   `url_busca_gerada_em`. **Os três links encurtados de hoje nasceram datados de sete dias antes de
   existirem.** Não é cosmético: a 25.4-b manda reconferir palavra-chave que envelhece, e quem
   reconfere escolhe **pela data**. A data agora sai do relógio, em UTC.
2. **`restaurar-acentos.py` varria DOIS dos cinco bancos.** A tupla `ARQUIVOS` trazia só
   `materiais-colas` e `materiais-rejuntes`, os dois que existiam quando ela nasceu; **pastilhas,
   alicates e acabamento nunca foram varridos**, e nada acusava, porque ela sempre fechava "0 trocas"
   nos arquivos que ela via. Com os cinco: **47 trocas GRAVADAS**, e entre elas texto que estava **no
   ar** — `Verniz Acrilico Brilhante`, `Cortador de ceramicas e azulejos manual`,
   `Saint-Gobain ... Construcao Ltda.`. É a mesma família da mutação inerte de 28/09: **régua que não
   alcança aprova em silêncio.** Dez palavras entraram no mapa (as únicas, de 118 acusadas, cuja forma
   acentuada é a única leitura possível) e as outras 108 foram para `_CONHECIDAS` uma a uma, porque
   aviso que grita 118 palavras não é aviso.
3. **O `--provar` dessa mesma ferramenta estava prometido no cabeçalho e NÃO EXISTIA no código.** O
   cabeçalho diz desde 11/09 *"A OPERAÇÃO É PROVADAMENTE DIACRÍTICO-ONLY, e é o `--provar` que
   garante"*, e `sys.argv` era lido **só** para `--gravar`: `--provar` passava direto, ignorado em
   silêncio, imprimindo o mesmo relatório e dando a impressão de ter provado. **E é justamente essa
   prova que torna a ampliação do item 2 segura**, porque o que ela impede é "restaurar acento" virar
   reescrita de declaração de fabricante. Implementado — e **conferido que ele REPROVA de verdade**,
   adulterando o mapa numa cópia em `/tmp` e vendo a única violação ser acusada pelo nome. Portão que
   nunca reprovou nada não é portão.
4. **`mutacoes-base.py` e `mutacoes-apoio.py` estavam VERMELHAS no `main`, pela segunda vez em dois
   dias e pela mesma causa.** O comentário dentro delas conta a primeira: o aperto do degrau, em
   29/09, reprovava o **mundo fabricado** antes de qualquer mutação. A leva de 30/09 que subiu o
   esquema para a **versão 9** tornou `motivo_sem_ficha` obrigatório, com forma, para todo item no
   degrau 4 sem ficha — e as duas voltaram a cair, **dois dias**, sem ninguém as vendo. O que elas
   deixam sem medição não é pouco: **`base` e `apoio` são as duas únicas categorias sem SKU**, portanto
   as únicas cujos portões não têm banco real que os exercite. **Medido vermelho no `main` limpo**
   (`git stash`) antes de qualquer mudança desta execução, para não chamar de meu o que era de antes.
   Consertadas **derivando** o campo do estado fabricado em vez de cravá-lo, que é o que impede a
   terceira morte: **20 de 20** e **24 de 24**.

## E O PORTÃO CORRIGIU O DOCUMENTO, NÃO A MÃO

`filhas-do-guia.py --conferir` **reprovou** a tabela da seção 2 do `ARVORE.md`: ela dizia
`7 itens | 1 de 3` para `/materiais/acabamento/` e a derivação dizia `10 | 3 de 3`. As duas direções
foram medidas. O documento foi para 10 e 3 de 3, e a seção 7b-ter ganhou a atualização que diz, com
todas as letras, que **o parágrafo "o 4c continua fechado" é de 25/09 e deixou de descrever o mundo**
— e também que o selador já não é mais o item que não serve MDF. A régua fabricada da bancada
(`tabela()`, escrita à mão de propósito, para não chamar a função que ela mede) foi atualizada no
mesmo movimento, com a linha dizendo o preço disso: quem mudar o banco e vir aquele caso falhar não
tem defeito para procurar, tem dois números para reescrever.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Não criou nenhuma URL, e o portão de dado abrir não autoriza criar.** A **14.9** exige o
  cruzamento de intenção de compra com chance real de primeira página, e a medição de SERP de 30/09
  (em `dados/filhas-do-guia.md`) diz que as filhas publicáveis desta ilha hoje têm forma de
  **pergunta** e não de tipo: `verniz para peça de mosaico artesanal` está **ABERTA** e `pastilhas de
  vidro para mosaico` está **TOMADA**. Além disso **`verniz` não existe em `dados/corpus-buscas.md`**
  — sem faixa de volume medida. **Dois vereditos saem juntos ou nenhum dos dois serve.**
- **Não tocou em `<title>` nem em `description`** de nenhuma das 17 URLs. O BLOCO A espera a leitura
  da janela 23→30/09 por ordem escrita do Raphael, e a janela segue limpa.
- **Não inventou nome comercial.** Os três têm a caixa do **título** da página de produto (nível 3), e
  por `batismo_do_fabricante.origens_que_batizam` **só PDF batiza** — então os três ficam **fora do
  escopo da trava, com o motivo escrito em `motivo_do_batismo_pela_pagina`** em vez de aprovados em
  silêncio. `batismos conferidos` segue em 7.
- **Não escreveu `fabricante` de cabeça.** O da Suvinil ficou **null com motivo**: a marca trocou de
  dono e as duas passadas devolveram marca, não razão social. O da Coral é **AkzoNobel**, lido no
  próprio domínio do fabricante (`coral.com.br/content/dam/akzonobel-flourish/coral/`), com a razão
  social da entidade brasileira registrada como não obtida.
- **Não converteu rendimento em consumo** em nenhum dos três. Os fabricantes declaram m²/L e o campo
  pede mL/m²; converter é aritmética desta ilha, e o esquema proíbe a conversão nesse campo com essas
  palavras. Ficaram null **com motivo**, que é pergunta feita e respondida.
- **Não mexeu no egresso.** Reteste da **20.2** nesta execução: `loja.suvinil.com.br`,
  `suvinil.com.br`, `coral.com.br`, `vedacit.com.br`, `sayerlack.com.br` e `montanaquimica.com.br`
  em **000** por `curl` e **EGRESS_BLOCKED** por fetch; `www.quartzolit.weber` em **403**. Todo campo
  dos três carrega `conferir_no_pdf: true`, como os sete de 25/09.

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` verde: **41 materiais**, escada **1:1 · 2:5 · 3:18 · 4:17** (soma 41), degrau 4
com motivo **17 de 17**, itens sem saída de compra **0**, piso não rastreável **0**, casamentos
reconferidos **14**. `filhas-do-guia.py --autoteste` **27 casos fabricados, 0 falha** e `--conferir`
**aprovado**, nas duas direções. `cobertura.py` regerado e `--conferir` **OK**, com `mutacoes-cobertura` verde. `mutacoes-promessa-do-titulo` **19 de 19**. Mutações:
acabamento **14**, batismo **14**, casamento **17** (12 na regra + 5 no banco), degrau **8**, motivo-degrau-4 **10**, pastilhas
**14**, árvore **29 de 29**, **base 20 de 20** e **apoio 24 de 24** (as duas que estavam vermelhas).
`teste-batismo` **62**, `teste-casamento` **42**, `validar-pastilhas` verde. PHP: casca **601**, F2
**127**, técnicas **137**, F1 24 estados com processo próprio, Loja, Ateliê, Leads e Prestação
**aprovados** — **zero falha**. `restaurar-acentos --provar` **aprovada**, 47 trocas diacrítico-only.

## DESEMBARQUE E VERIFICAÇÃO NO AR

Push aceito na **primeira tentativa** (`1e2c211..50fc063`). Sync acionado **depois** do push, que é a
ordem certa porque ele lê o `manifest.json` do `main` pelo `raw.githubusercontent`.

**E a primeira leva de Sync NÃO entregou, por um motivo que vale escrever:** o Sync leu o manifest na
revisão **54** — a anterior — e devolveu **`sha256 divergente — não aplicado`** justamente nos três
bancos que este bloco mudou (`materiais-acabamento`, `materiais-alicates`, `materiais-pastilhas`). Não
era defeito do bloco nem do Sync: é o **cache do `raw.githubusercontent`**, que serviu o manifest
velho enquanto os arquivos de dado já vinham novos. Seis disparos ao longo de **cerca de quatro
minutos** e meio, e o sexto leu **55**. A lição operacional, para a próxima execução não diagnosticar
isto como sha errado: **`sha256 divergente` logo depois do push é cache de manifest até prova em
contrário — o reteste é um disparo, e a 20.2 já manda repetir antes de chamar de bloqueio.** Nesse
intervalo o ar ficou coerente, e não meio aplicado: o Sync recusa o par que não fecha, então os três
bancos continuaram servindo o estado anterior até o manifest novo chegar.

**Sync na revisão 55** às **14h13:46**, **14 aplicados** e 11 aguardando desembarque, com
`dados/materiais-acabamento`, `materiais-alicates`, `materiais-pastilhas` e `dados/esquema-banco`
todos em `ok`. `/status` devolvendo **55**, igual à do manifest.

**E no ar depois do desembarque: `conferir-no-ar.py` com 524 afirmações e 0 falha**, medido antes e
depois. O único vermelho da borda continua sendo o **soft 404 do hospedeiro**, com dono escrito desde
29/09.

**A correção de acento foi CONFERIDA NA TELA, não só no dado**, porque era disso que ela se tratava:
`/materiais/quantas-pastilhas-para-mosaico/` serve agora **`catálogo`** e **zero** ocorrências de
`catalogo` — antes deste bloco ela servia a palavra sem acento, e serviu assim por 21 dias sem que a
ferramenta que existe para isso olhasse aquele banco.

**A memória da ilha não foi atualizada porque ela não existe neste ambiente:** `/areas/` não está
montado, conferido nesta execução com `find`. O `PROMPT.md` desta ilha já prevê isto — *"Sem memória,
não pare: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta"* — e é onde o próximo
passo ficou escrito.

- **Próximo passo desbloqueado, e ele é uma ESCOLHA e não mais uma espera:** o 4c tem o portão de
  **dado** aberto em `acabamento` (3 de 3), e o que falta para publicar é o portão de **SERP** da
  14.9. As duas pontas estão medidas e discordam da fila: a filha de mais banco (`pastilha/vidro`,
  13 itens, três números) está **TOMADA** por marketplace, e a de SERP mais aberta
  (`verniz para peça de mosaico artesanal`) **não tem faixa de volume** em
  `dados/corpus-buscas.md`. Então o próximo bloco é um dos dois, e os dois são da Fundação: **(a)**
  medir `verniz` e os termos de acabamento no corpus, acrescentando-os a `dados/corpus-buscas.md`
  com faixa, concorrência e classificação de SERP — é o que falta para a 14.9 poder ser cruzada e
  não depende de ninguém; ou **(b)** levar a mesma régua de 3 itens a um recorte em forma de
  **pergunta** em vez de tipo, que é o que o próprio `filhas-do-guia.md` diz ser a forma que esta
  ilha publica (a F1 e a F2 são assim) — a régua já está na ferramenta para ser chamada em vez de
  reescrita. **(a) vem antes de (b)**, porque (b) sem faixa de volume publicaria escolhendo pelo
  dado que temos e não pela demanda, e foi por isso que a 14.9 existe.
- **O que continua fora do alcance daqui, e os dois seguem com o Raphael:** a leitura da janela
  23→30/09 (acesso do `sentinela@` a `sc-domain:clubedomosaico.com.br`, ou `GOOGLE_SA_B64` no
  ambiente), que é o veredito do BLOCO A e segue marcado para **08/10**; e o **curinga** de egresso
  dos domínios de fabricante, que trava o primeiro SKU de `base` e de `apoio` — a lista derivada,
  domínio por domínio, está em `dados/egresso-de-fontes.md`. O soft 404 da borda é o terceiro, aberto
  desde 29/09. **Nenhum dos três é pré-requisito do passo acima.**

02/10/2026 11:5xZ — A MARCA CEDEU O LUGAR AO NÚMERO NAS TRÊS QUE O GOOGLE JÁ MOSTRA

Manifest e `/status` na **revisão 54**, conferidos no ar. **Nenhuma URL nova** (a ilha segue
em 17), nenhum endereço mudou, nenhuma linha de corpo mudou. O que mudou é a etiqueta onde o
clique se decide: o `<title>` de **três** páginas e a `description` de **quatro**.
`conferir-no-ar.py`: **524 afirmações, 0 falha.** Bancada: teste-casca 601, teste-f1 210,
teste-f2 127, teste-tecnicas 137, teste-loja e teste-leads aprovados, 0 falha.

**O BLOCO desta execução é o BLOCO A do despacho do Raphael de 24/09**, que pela 18.1 vem
antes de tudo nesta ilha e que esperava uma coisa só: a janela de medição de **30/09**.
Hoje é 02/10 e ela fechou. No mesmo movimento saiu o **item 4 (metade)** do despacho da
Sentinela de 28/09 — a `description` é a outra metade da mesma promessa de SERP, e separar
as duas é exatamente o que o BLOCO A existia para impedir. Com isso **os despachos de 24/09
e de 28/09 estão fechados inteiros.**

## O QUE ESTÁ NO AR, E O QUE NÃO MUDOU

| página | `<title>` servido | nº | `description` | nº |
|---|---|---|---|---|
| qual-cola | …e qual rejunte **– 7 colas para 9 bases** | 64 | …7 colas em 270 casos…, e os 68 que a gente ainda não responde | 143 |
| quantas-pastilhas | …rejunte comprar **– 12 peças calculadas** | 64 | …12 peças já calculadas, de 23 a 960 pastilhas… | 139 |
| picassiete | …e como colar **– 7 colas em 45 casos** | 62 | …7 colas em 45 casos, pela declaração do fabricante | 150 |
| trencadís | …colar o caco – Clube do Mosaico (**INTOCADO**) | 62 | …o caco de azulejo ou de louça em cada superfície | 139 |

**O NOME DA PÁGINA NÃO FOI TOCADO EM NENHUMA DAS QUATRO**, e isso é a parte que mais importa:
o que cede o lugar é a **marca**, 16 caracteres de carimbo no fim de um título que está na
primeira página e não é clicado — numa ilha com **zero clique orgânico medido**, ninguém a
procura pelo nome. O `<h1>` servido continua `Qual cola usar no mosaico, e qual rejunte`, e a
promessa aparece **uma vez** no HTML inteiro: dentro do `<title>`. É a regra "UM NOME POR
PÁGINA" que esta ilha herdou da cicatriz que a Aquametria pagou em 11/09, e o caminho é o
precedente da Robometria de 17/09, portado: a casca **1.19.0** monta o título uma vez e quem
tem promessa a **declara** pelo filtro `cdm_promessa` — o mesmo contrato de camadas que a
`description` tem desde 28/09 e a etiqueta de robô desde 25/09.

## O TRENCADÍS FICOU PARADO, E A AUSÊNCIA DELE É A DECISÃO

O despacho de 23/09 manda, com estas palavras, *"deixe uma página parada para a próxima
leitura ter com o que comparar"*. Ele não declara promessa, e o portão mede isso nas **duas
direções** — promessa onde tem de haver, marca onde tem de ficar. Só a `description` dele
mudou, de 189 para 139, que era o que o item 4 cobrava. **Trocar as quatro de uma vez não é
zelo: é tornar a próxima medição ilegível**, e é o mesmo argumento que a Robometria escreveu
ao dar promessa a três cabeças e a nenhuma outra.

## NENHUM NÚMERO É DIGITADO, E A VARREDURA É A MESMA DA TELA

Os três números da `qual-cola` saem de `cdm_f2_cobertura()` — e ela **não é nova por
capricho**: a varredura de base × lugar × caquinho já existia dentro da seção "o que a gente
ainda não responde", contando ali e em lugar nenhum mais. Agora ela é contada **uma vez e
lida por três** (a seção da tela, a promessa do título e a `description`). Contar a mesma
coisa em três lugares é a família de defeito que esta ilha mais pagou: duas metades contando
a mesma coisa sem nunca se falarem. No dia em que o banco mudar, a promessa do resultado da
busca e a confissão do fim da página mudam **juntas**.

## TRÊS TRAVAS, E DUAS SÃO SILENCIOSAS POR DESENHO

1. Promessa que estoura o teto de **65** devolve a marca — promessa cortada no meio pelo
   Google é pior que promessa nenhuma.
2. Número que não chegou, ou **zero**, recusa o molde **inteiro**. Zero entra na recusa
   porque "0 colas" é uma frase verdadeira que não serve, e no resultado da busca ela custa
   o clique que o bloco existe para ganhar.
3. A bancada reprova quem **declara** promessa e serve título sem dígito.

As duas primeiras **não falham**: elas devolvem a marca e a página continua válida. Trava
silenciosa sem quem a conte é como a promessa desaparece do ar sem ninguém ver — então a
bancada ganhou o mundo **`sem_banco=1`**, que apaga as options de material e faz a trava 2
disparar **na página**, não só na função pura. Bateria nova
`ferramentas/mutacoes-promessa-do-titulo.py`: **19 mutações, 19 reprovadas, 0 passaram.**

## O ACHADO DE BANCADA, E ELE É O MAIOR DESTA EXECUÇÃO

**A bancada servia um `<title>` que nenhuma afirmação media.** Até hoje o
`render-para-teste.php` punha `<title>Clube do Mosaico — teste</title>` em **toda** página —
um rótulo fixo, igual nas dezessete. O bloco de hoje mexe exatamente nessa etiqueta, e régua
que não alcança o que o bloco muda é régua que nasce cega (seção 8). Agora a bancada monta o
título pelo caminho do WordPress: partes, filtro `document_title_parts`, separador. **O
separador não é escolha nossa:** o núcleo junta com `" - "` e o `wptexturize` dele troca o
hífen cercado de espaço por travessão — `&#8211;`, medido no ar hoje. A conta do teto é em
caracteres **decodificados**, a mesma régua da `description`: `&#8211;` conta 1, não 7.

## E A RÉGUA NOVA NASCEU REPROVANDO PÁGINA CERTA

O portão de `<title>` do `conferir-no-ar.py` cobrou o teto de 65 nas **17** e reprovou
**quatro títulos de peça da Loja**, entre 71 e 79 caracteres
(`/loja/quadro-nossa-senhora-aparecida/`, 79, é o maior). Não é defeito: o formato é o que o
despacho do Raphael de **10/09** escreveu, e a primeira observação do despacho de **28/09** já
tinha decidido que *"a régua de 64 é da aquametria e não do contrato"* — recomendação, não
defeito. A régua foi consertada antes de o despacho fechar: o teto é portão nas páginas cujo
título a **casca** monta, e na peça o número é **medido e impresso, nunca reprovado**, no
mesmo desenho do soft 404 de borda. É a quinta vez que esta família aparece no Arquipélago, e
a lição não muda: **portão que não sabe sobre o que decide acusa a coisa errada.**

## O QUE ESTA EXECUÇÃO NÃO PODE FECHAR, E POR QUE ISSO É INFORMAÇÃO

**A leitura semanal de 30/09 não aconteceu.** A ronda diária técnica daquele dia rodou
(14h53Z, nas três ilhas no ar) e fechou sem defeito de página aqui; a estratégica não foi
disparada, e em 01/10 não houve execução nenhuma. A série de `dados/posicoes.md` tem **uma
linha**, a de 23/09.

**E isso não impediu a troca de hoje, por uma razão medida e não conveniente:** a janela
23→30/09 está **fechada e congelada** no Search Console, e nada servido em 02/10 reescreve
aquela semana. A ordem do BLOCO A era não misturar duas causas **dentro** daquela janela.
Fora dela, esperar não protege nada — protelaria a única alavanca medida desta ilha por uma
leitura que a Fundação **não tem como fazer**: a conta `sentinela@` não tem acesso a
`sc-domain:clubedomosaico.com.br`, e o pedido está aberto desde 23/09.

**Então duas coisas foram para `dados/despachos.md`, na lista de ABERTOS:** o acesso da conta
`sentinela@` (que vivia só dentro deste `PROMPT.md` desde 23/09) e o pedido de **ler a janela
de 7 dias que termina em 30/09** — a última semana inteira com o título antigo, e por isso a
única base de comparação limpa que vai existir. A semana 30/09→07/10 já nasce misturada: dois
dias de título velho e cinco de novo. **O veredito continua de 08/10**, como o BLOCO A manda,
e nada aqui declara vitória nem derrota.

## O QUE SOBRA ABERTO NESTA ILHA, em uma linha cada

- **Soft 404 na borda** (item 2 do despacho de 30/09): do hospedeiro, com o Raphael desde
  29/09, medido também na robometria. `leitura-do-visitante.py` fecha REPROVADO por esse
  **único** defeito — vermelho esperado, com dono escrito.
- **A decisão do `tipo_de_casamento: "equivalente"`** para as 13 pastilhas: do Raphael, em
  `dados/despachos.md`, com a medição de 30/09 atrás dela.
- **Os quatro itens que dependem da leitura semanal**: a linha de `/author/` sair de
  `posicoes.md`, o formato `clubedomosaico-f2---` no Relatório de cliques, o CTR da
  `qual-cola` e o primeiro clique orgânico. Nenhum é trabalho de máquina.

## PRÓXIMO PASSO DESBLOQUEADO

Com os despachos de 24/09 e 28/09 fechados e o de 30/09 sem item de Fundação, **a fila volta
a ser fila**: o próximo bloco é de construção, sob o teto da 21.4 (10 URLs por leva, 3 levas
por semana) e com `piso: abaixo` (17 de 40 URLs). A semana está com **zero leva gasta** — a
última URL nova desta ilha é de 14/09. E a 18.5 não bloqueia mais nada: não há defeito de
página no ar.

---

30/09/2026 16:3xZ — OS DOZE DIZIAM COMO A CHAVE FOI MONTADA E CALAVAM O QUE A ESCADA RESPONDEU

Manifest e `/status` na **revisão 53**, conferidos no ar. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudaram: o **BLOCO A** do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09 segue
limpa — o veredito dele é de 08/10 e a troca de título espera a leitura semanal, que
ainda não aconteceu hoje. `conferir-no-ar.py`: **519 afirmações, 0 falha.**

**O bloco desta execução é o item 1 do DESPACHO DA SENTINELA de 30/09**, e pela 18.1
ele é o único item da ilha que não depende da leitura semanal: o BLOCO A espera 30/09,
o item 4 (metade) do despacho de 28/09 espera o BLOCO A, e os quatro itens do despacho
de 23/09 esperam a leitura. **Nada foi construído, por 18.5: verificação antes de
construção.**

## O QUE O DESPACHO PEDIA, E POR QUE NÃO ERA ZELO DE ARQUIVO

Dos 38 registros do banco, **17 estão no degrau 4** — servem a página de busca, que é
o piso da 25.2. Cinco escreviam por que pararam ali; **doze traziam só
`motivo_da_chave`**, texto como `"familia: medida"`, que conta como a chave foi
MONTADA e não o que a escada de palavra-chave devolveu. Os dois estados eram a mesma
tela, e a 25.4-b.4 diz o preço disso: "não casou" tem causas que parecem uma — produto
que ninguém anuncia (só o mercado resolve) ou candidato barrado por trava (resolve-se
com trava melhor ou com um registro de variante que falta) — e **contadas juntas viram
um número que não diz o que fazer.**

## O QUE FOI MEDIDO, E A FERRAMENTA QUE NÃO PODIA SER O COLETOR

`ferramentas/medir-degrau-4.py` desceu a escada **inteira** pela Open API (25.6) para
os dezessete, com a regra de casamento de `casar-anuncio.py` **importada, nunca
copiada**. Ela não para no primeiro degrau que casa, ao contrário do coletor: quem mede
quer a escada toda, senão o motivo fala de um degrau e cala os outros três.

**Ela não grava `url` em nenhuma hipótese, e é isso que a deixa medir as 13 pastilhas.**
O `coletar-shopee.py` as exclui por `FORA = ('dados/materiais-pastilhas.json',)`, e com
razão: subir o degrau delas dependeria de `afiliado.tipo_de_casamento: "equivalente"`,
que é decisão do Raphael. **Mas medir não é agir** — e foi por confundir os dois que
elas ficaram de 13/09 a 30/09 carregando a frase *"elas nem foram tentadas"*, que é
exatamente a família de defeito que a 25.4-b.3 nomeia: motivo que diz "nem tentamos"
manda a execução seguinte não tentar, e fica assim por quanto tempo ninguém olhar.
**Dezessete dias, aqui.**

## A REPARTIÇÃO, QUE É O QUE O DESPACHO PEDIA — E ELA NÃO É A DA 25.4-b.4

| causa medida | quantos | de quem é a dívida |
|---|---|---|
| `marca-nao-anunciada` | **13** | do Raphael. Nenhuma oferta da escada traz a marca: degraus 1 e 2 (marca + código, marca + nome comercial) devolvem **zero** e os largos devolvem catálogo de outras marcas. Pede a decisão do casamento por atributo, não trava melhor |
| `candidato-barrado-nome` | **2** | nossa. `quartzolit-protetor-para-fachadas` e `cortag-torques-azulejista-corte-curvo` |
| `candidato-barrado-variante` | **2** | nossa. `quartzolit-fundo-selador` e `cascola-pl500-adesivo-de-montagem` |

**A 25.4-b.4 previa duas causas e a medição achou três**, e a terceira é a que mais
importa: `marca-nao-anunciada` não é "produto não anunciado" (a Shopee **tem** o
produto Glass Mosaic, anunciado como CG10/CG21/CG33) nem "candidato barrado por trava
que se pode melhorar" — é **pedido de decisão**. Somada a qualquer das outras duas, o
pedido ao Raphael desaparece dentro de uma dívida técnica que não é dele. Por isso o
relatório do validador imprime a repartição, e não só o total.

**E a medição confirmou, por máquina, o diagnóstico que estava escrito à mão em 29/09**
em `dados/links-afiliado-pendentes.md` — os três da Quartzolit e o da Cortag caíram como
dívida de nome ou de variante, nenhum como produto inexistente. Aquela tabela tinha sido
escrita lendo ensaio com o olho; hoje a classificação saiu do laudo da regra, sem
ninguém olhar, e caiu nos mesmos lugares.

## O ERRO DESTA EXECUÇÃO, ESCRITO PORQUE VALE MAIS QUE O ITEM

A **primeira versão do classificador** decidia a causa pela trava que barrou o
candidato, e o ensaio das 17 devolveu **17 de 17 na mesma classe** — precisamente o
número que não diz nada de que o despacho reclamava. A causa do erro: em
`casar.compativel` as cinco travas correm **em ordem** e a primeira que falha encerra o
julgamento, e a trava 5b (o título tem de trazer o `nome_comercial` inteiro) quase
sempre falha antes de qualquer trava de irmão ser avaliada. **"Nenhuma trava de irmão
foi acionada" media a ordem do código, não o mundo.**

O conserto foi trocar a pergunta: o que separa as causas é a **trava 1** — algum
anúncio da escada traz a marca deste registro? Zero oferta em toda a escada é
`nao-anunciado`; oferta sem a marca é `marca-nao-anunciada`; oferta **com** a marca é
dívida nossa, e aí a trava que barrou diz se é de nome ou de variante. **Régua que mede
a ordem em que o portão pergunta nunca reprova o portão.**

E uma segunda honestidade, na hora de batizar as classes: a primeira versão chamava uma
delas de `candidato-barrado-batismo`, afirmando que o nosso `nome_comercial` é que
estava errado. Para a Quartzolit é verdade (seção 26), para o torques da Cortag **não**
— lá o `nome_comercial` está certo e os anúncios são de corte RETO. A trava 5b não
distingue as duas leituras, então o rótulo passou a ser `candidato-barrado-nome` e o
campo diz, com todas as letras, que quem consertar tem de abrir o anúncio.

## O PORTÃO, E ELE COBRA A FORMA E NUNCA O TEXTO

`validar-banco.py` reprova registro no degrau 4 sem ficha cujo `motivo_sem_ficha` não
esteja na forma da 25.4-b.3: `CAUSA (<classe>): ... || ULTIMA TENTATIVA <AAAA-MM-DD>:
...`. A causa não se reescreve; a tentativa, sim, a cada passada. O relatório passou a
imprimir **`degrau 4 com motivo escrito: 17 de 17`** — que é o critério de pronto que o
despacho declarou — e a repartição por classe abaixo dele.

**Bateria nova:** `ferramentas/mutacoes-motivo-degrau-4.py`, **10 mutações, 10
reprovadas, as 10 só pelo portão novo** (desligado por
`CDM_SEM_PORTAO_MOTIVO_DEGRAU_4=1`). Atacam uma metade da forma por vez: o campo
ausente, a prosa de uma metade só que era a forma de 29/09 e passava, a causa sem
classe, a classe escrita em prosa com maiúscula (duas grafias da mesma causa viram duas
causas e a repartição soma errado **sem reprovar**), a tentativa sem data, a data em
formato brasileiro — legível e não ordenável — e a causa vazia dentro da forma certa.
Duas **produzem o mundo** que o banco não tem: ficha achada com link não encurtado, e
item que **cai** do degrau 3 de volta para o 4 quando o anúncio sai do ar. As duas
recontam `itens_esperando_link` do cabeçalho, porque sem isso era o portão do CABEÇALHO
que as pegava — e **mutação pega pelo portão errado não prova portão nenhum**: era
assim que as duas apareciam como "outro portão já pegava" na primeira rodada.

`dados/esquema-banco.json` foi para a **v9**, declarando a forma, as quatro classes,
quem escreve e quem cobra.

## BANCADAS, TODAS VERDES

`validar-banco` · `validar-pastilhas` · `mutacoes-degrau` 8/8 · `mutacoes-casamento`
17/17 · `teste-casamento` 42 · `mutacoes-pastilhas` 14/14 · `teste-casca` 591 ·
`teste-f1` 24 estados · `teste-f2` 119 · `teste-loja` · `teste-atelie` · `teste-leads` ·
`teste-tecnicas` 123 · `conferir-cobertura` 353 · `conferir-no-ar` **519 afirmações, 0
falha**. `leitura-do-visitante` continua **REPROVADO pelo soft 404 da borda**, que é do
hospedeiro, está com o Raphael desde 29/09 e hoje também foi medido na robometria.

## O PRÓXIMO PASSO DESBLOQUEADO

**Nada da Fundação, até a leitura semanal de 30/09 acontecer.** Os quatro itens que
restam nesta ilha dependem todos dela, e é uma dependência escrita, não uma escolha:

1. **BLOCO A** (Raphael, 24/09) — título e meta das três páginas de primeira página.
   Espera a leitura de 30/09 por ordem do próprio despacho; o retrato "antes" já está
   gravado em `dados/posicoes.md` desde 29/09.
2. **Item 4 (metade) do despacho de 28/09** — a faixa de 120 a 160 nas quatro
   `description` acima de 160. Espera o BLOCO A, porque é a outra metade da mesma
   promessa de SERP.
3. **Itens 1 e 2 e Propostas 1 e 3 do despacho de 23/09** — os quatro só fecham com
   número da leitura semanal: a saída de `/author/` de `dados/posicoes.md`, o formato
   `clubedomosaico-f2---` no Relatório de cliques, o CTR de `qual-cola` e o primeiro
   clique orgânico.
4. **Item 2 do despacho de 30/09** — o soft 404 da borda. É do hospedeiro e não se
   conserta daqui.

**E um pedido novo ao Raphael, que esta execução não inventou e sim mediu:** a decisão
do `tipo_de_casamento: "equivalente"` para as 13 pastilhas deixou de ser uma frase
antiga e passou a ser uma linha de banco com medição de hoje atrás dela. São 13 dos 17
itens do degrau 4 — a maior fatia da dívida de conversão desta ilha — e o caminho pelo
código está **medido como fechado**, não apenas inexplorado.


29/09/2026 19:16Z — O BATISMO DO FABRICANTE JÁ ESTAVA NO REPOSITÓRIO, E O EGRESSO NÃO ERA O QUE TRAVAVA

Manifest e `/status` na **revisão 50**, conferidos no ar. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudaram: o BLOCO A do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09 segue
limpa. O que mudou foi o **banco** — e, desta vez, um campo do banco que ninguém
tinha lido.

**A escada da 25.1 saiu de `1:1 · 2:5 · 3:14 · 4:18` para `1:1 · 2:5 · 3:15 · 4:17`**,
e a página de divulgação passou de *"Em 20 o botão é a ficha do produto e em 18 é a
busca"* para **21 e 17**, sem ninguém digitar número: ela conta dos registros.

## ESTE BLOCO CONTRADIZ O QUE A EXECUÇÃO ANTERIOR ESCREVEU, E A CORREÇÃO VALE MAIS QUE O ITEM

O `REGISTRO.md` das 16h17Z de hoje fechou dizendo, sobre os três registros da
Quartzolit presos no degrau 4:

> *"TRÊS são da Quartzolit e o defeito NÃO é do link: é do BANCO. (...) Consertar é
> COLETA, na página do fabricante, e esbarra no mesmo egresso do item 3 acima:
> `quartzolit.weber` em 403, na lista do Raphael."*

**Não esbarra.** O batismo do fabricante estava dentro do próprio registro desde
25/09, em `fontes[].url`: o endereço do boletim técnico, cujo **nome de arquivo** é o
fabricante escrevendo o nome do produto.

```
BT_Borracha Líquida Elástica Quartzolit_REV110624.pdf
```

O registro chamava-se *"impermeabilizante borracha liquida elastica quartzolit"*. A
palavra `impermeabilizante` **não está no boletim**: ela veio do **caminho** da página
de produto — `/impermeabilizantes-quartzolit/impermeabilizantes-para-paredes-externas-e-fachadas/`
—, que é a **prateleira** do fabricante, não o nome do produto. A ilha colou a
classificação dentro do batismo, que é a seção 26 exatamente ao contrário.

**O egresso continua fechado e continua travando `base` e `apoio`.** Este item não era
dele, e quatro execuções seguidas anotaram "esbarra no egresso" sem abrir a fonte que
já estava em casa. Vale como aviso mais do que como conserto: *bloqueio herdado de um
documento é retestado antes de ser respeitado* (seção 20.2) — e isso vale para o
bloqueio herdado do `REGISTRO.md` tanto quanto para o do `ESTADO.md`.

## A REGRA JÁ ERA DO BANCO; O QUE FALTAVA ERA ALGUÉM APLICÁ-LA A ESTE CAMPO

`escada_de_fontes`, do `dados/esquema-banco.json`, diz desde o bloco 3: *"em conflito,
o nível mais alto vence e o outro fica registrado em `divergencias[]`"*. O registro
citava **duas** fontes do mesmo fabricante — boletim técnico (nível 2) e página de
produto (nível 3) — e elas **discordam sobre o nome**. O banco já mandava o nível 2
vencer. Nenhum portão media isso para `nome_comercial`, porque até hoje de manhã nada
comparava esse campo com um texto de fora: `casar-anuncio.py` foi o primeiro, e o que
ele achou foi um campo do próprio banco escrito no papel errado.

A divergência ficou **gravada** no registro, com as duas declarações, os dois níveis e
a resolução escrita — não foi corrigida em silêncio.

## DUAS RÉGUAS MAIS LARGAS FORAM MEDIDAS E DESCARTADAS ANTES DESTA

Isto é o que evita que a trava nasça grande e morra ignorada:

1. *"o batismo tem de caber na URL da melhor fonte"* — reprova **20 dos 38**, e quase
   todos são honestos: página de produto de fabricante tem endereço genérico, e
   `Verniz Acrilico Brilhante` não está no dele.
2. *"o batismo não começa com a palavra que a ilha usa para classificar"* — reprova
   **20 dos 38**, entre eles `Verniz Acrilico Brilhante` (tipo `verniz`) e
   `Rejunte Cerâmicas Quartzolit` (categoria `rejunte`). O fabricante batiza pelo tipo
   o tempo todo.

A terceira, a que ficou, mede **7 registros** — os que citam PDF de fabricante — e
reprova **1**, com **zero falso positivo**. Trava larga que a próxima execução aprende
a ignorar não é trava.

## A COMPARAÇÃO TEM DE SABER QUE O SERVIDOR DO FABRICANTE MUTILA O NOME DO ARQUIVO

Duas mutilações, as duas medidas neste banco: ele **apaga a letra acentuada inteira**
(`Boletim_Tcnico` por "Técnico", `rejunte_epxi_quartzolit.pdf` por "Rejunte Epóxi") e
**cola as palavras** (`RejuntePorcelanatoseCeramicas`). Uma comparação ingênua
reprovaria `Rejunte Epóxi Quartzolit` e `Rejunte Porcelanatos e Cerâmicas Quartzolit`,
que são batismos **certos**. E a **marca** fica fora da cobrança: ela mora no campo
dela, e o fabricante nem sempre a repete no nome do arquivo.

## A BATERIA OBRIGOU A BANCADA A FABRICAR DUAS BORDAS — DE NOVO, E PELO MESMO MOTIVO

A primeira rodada deu **7 de 10** na regra: duas mutações passaram com a bancada verde,
e as duas atacavam travas que **nenhum registro de hoje exercita**.

- **A palavra vazia.** Cobrar `de` num batismo cujo arquivo não o traz reprovaria um
  nome certo — mas o `para` de *"Verniz Protetor para Pisos"* está escrito no próprio
  arquivo, então a trava nunca era exercitada. A bancada passou a fabricar o par.
- **O separador.** O fabricante pode partir no arquivo o que o batismo escreve junto
  (`AC2` virando `AC_2`); nenhum arquivo deste banco faz isso hoje.

**Bancada que só mede o banco de hoje envelhece junto com ele** — a mesma frase do
bloco das 16h17Z, e a segunda vez em um dia que a bateria a cobra.

## O QUE MEDE ISSO

- `ferramentas/batismo-do-fabricante.py` — a regra sozinha, sem rede e sem gravação,
  pelo mesmo motivo de `casar-anuncio.py`: quem a usa e quem a ataca precisam da mesma
  função.
- `ferramentas/teste-batismo.py` — **59 afirmações, 0 falha**, sobre os registros reais
  em **cópia** (bancada que escreve no banco para se provar estraga o que mede).
- `ferramentas/mutacoes-batismo.py` — **14 de 14 reprovadas**: 10 na regra (duas delas
  **apertando** a régua, porque folga deliberada que ninguém mede alguém aperta por
  zelo na leitura seguinte) e 4 no esquema/banco, entre elas a que a **26.2** exige por
  escrito — apagar a chave da lista.
- `validar-banco.py` ganhou a linha `batismos conferidos .... 7`.
- Esquema na **versão 8**, com `batismo_do_fabricante`. A lista de quais fontes batizam
  mora **no esquema**, nunca dentro da régua (26.2).

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

**`quartzolit-fundo-selador` e `quartzolit-protetor-para-fachadas` continuam em
minúsculas**, e agora com o motivo escrito no registro: a única fonte deles é a página
de produto, e o batismo chega pelo **slug** do endereço, que soletra as palavras e
**perde a tipografia**. Capitalizar dali seria palpite sobre como o fabricante escreve
— palpite com cara de declaração do fabricante é o que a seção 26 existe para impedir.
Os dois ficam fora do escopo da trava, com o motivo no laudo, não aprovados em silêncio.

**E os outros três do degrau 4 continuam onde estavam**, cada um com o dono que a
execução anterior já tinha nomeado certo: as **treze pastilhas** dependem de
`tipo_de_casamento: "equivalente"` e são do Raphael; a **torquês de corte curvo da
Cortag** foi remedida com quatro chaves novas nesta execução e **a Shopee não anuncia
esse produto** — as chaves de "corte curvo" devolvem a torquês de **mosaico**, que já é
outro registro do banco, e casar as duas seria a armadilha 5 da 25.7; o **Cascola
PL500** continua caindo na trava do nome comercial inteiro, e afrouxá-la para ele
passar é critério dobrado para caber no dado (1.2-b.4).

## O QUE APARECE NA TELA, E O QUE NÃO APARECE

A prova servida é a frase da página de divulgação: **21 e 17**. O nome corrigido em si
**não aparece em página nenhuma hoje** — os sete materiais de acabamento estão no
banco e `/materiais/` lista a categoria como *"Em breve"*, porque a ficha de categoria
é o bloco **4c** e ele não nasceu. Dizer que o conserto "foi ao ar" sem essa ressalva
seria contar meia verdade.

## NO AR, E UMA FALHA QUE NÃO ERA DA ILHA

`conferir-no-ar.py` **519 afirmações, 0 falha**; `conferir-tecnica-no-ar.py` **54 e 0**;
`conferir-atelie-no-ar.py` **197 e 0**. O soft 404 da borda continua reprovando a leitura
do visitante por **1** defeito — é do hospedeiro, está pendente com o Raphael e não mudou.
O desembarque aplicou **na primeira chamada** (revisão 50, 14 aplicados).

O ateliê chegou a fechar vermelho, e o vermelho era meu: **`conferir-atelie-no-ar.py` toma
o TOKEN como primeiro argumento**, e todas as outras ferramentas desta ilha tomam a raiz
(`conferir-no-ar.py .`). Chamei com `.` por hábito, o ponto foi para a rota protegida, e o
401 que voltou era a rota **recusando corretamente** uma palavra errada. Custou uma
passada de diagnóstico. Virou trava em vez de nota: a ferramenta agora **recusa um
argumento que seja caminho** em vez de transformá-lo em credencial, e diz como se chama.
Nada do site foi tocado.

- **Próximo passo desbloqueado:** continua sendo a leitura de **30/09**, que libera o
  **BLOCO A** (CTR das três páginas de primeira página, veredito em 08/10) e, com ele, a
  metade que falta do item 4 da Sentinela de 28/09. O que **não** depende dela: (a) o
  egresso de fabricante, que trava `base` e `apoio` e está na lista do Raphael — e que
  este bloco confirma ser o travamento **de verdade** daquelas duas, não uma herança de
  documento; (b) a decisão de `tipo_de_casamento: "equivalente"` das treze pastilhas,
  que é do Raphael; (c) **a ficha de categoria de acabamento (bloco 4c)**, que é o que
  daria página ao que este bloco corrigiu — e que, pela 21.4, é leva de malha e deve
  esperar a leitura de 30/09 fechar a janela de medição.

---

29/09/2026 16:17Z — DEZ MATERIAIS SAEM DO PISO DA 25.2 E GANHAM FICHA DE PRODUTO, COM A PROVA DO CASAMENTO GRAVADA E RECONFERIDA POR PORTÃO

Manifest e `/status` na **revisão 49**, conferidos no ar. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudaram: o BLOCO A do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09 segue
limpa. O que mudou foi o **banco**, e o que o banco mudou apareceu na tela.

**A escada da 25.1 saiu de `1:1 · 2:5 · 3:4 · 4:28` para `1:1 · 2:5 · 3:14 · 4:18`.**
Vinte dos trinta e oito materiais servem agora a FICHA do produto; dezoito servem o
piso da 25.2, a página de busca. E a página de divulgação, que conta isso ao leitor,
passou de *"Em 10 o botão é a ficha do produto e em 28 é a busca"* para **20 e 18**,
sem ninguém digitar número nenhum — ela conta dos registros.

## POR QUE ISTO NÃO TINHA SIDO FEITO ANTES, E A RESPOSTA ESTAVA ESCRITA NO PRÓPRIO BANCO

O cabeçalho de `materiais-acabamento.json` dizia, desde 25/09, com todas as letras:
*"Nenhum tem ficha de produto (`url` vazio): ficha exige casamento de item, que a
25.7 proíbe sem prova de que o anúncio é daquele SKU."* O de `materiais-alicates.json`
dizia o mesmo em outras palavras. **Não era preguiça nem esquecimento: era uma
recusa correta.** A 25.7 é explícita — *casamento errado no banco é pior que
casamento nenhum, porque parece dado* — e escolher um anúncio pelo olho, item a
item, é exatamente a mão humana sem portão que fez os dezesseis `sub_id` nascerem
deslocados em 13/09.

**O que faltava não era trabalho: era o portão.** Este bloco construiu o portão, e
só então usou.

## A REGRA, E ELA MORA SOZINHA NUM ARQUIVO PARA PODER SER ATACADA

`ferramentas/casar-anuncio.py` não fala com a rede e não grava nada. É só a regra —
separada de propósito, porque quem a **usa** (`coletar-shopee.py`) e quem a **ataca**
(`mutacoes-casamento.py`) precisam da mesma função. Regra copiada em dois lugares é
regra que a bateria mede num lugar e o banco usa no outro.

São **seis travas mais a unicidade**, e todas as sete têm de passar:

1. **A marca aparece no título.** Sem ela, `verniz acrílico brilhante` é o catálogo
   de meio Brasil.
2. **A cabeça do título é o produto** — as quatro primeiras palavras trazem algo do
   nome comercial. É a armadilha 1 da 25.7 traduzida para este nicho: *"Kit 3
   Pincéis para aplicar Verniz Acrilex Brilhante"* tem o verniz no meio e um pincel
   na cabeça, e quem compra leva pincel.
3. **O título separa o registro de cada irmão** (outro registro da mesma marca).
4. **O título NÃO traz o que é do irmão**, quando o irmão é do mesmo tipo.
5. **Nenhuma palavra de armadilha** — `kit`, `combo`, `usado`, `apostila`. A lista
   **não** tem `manual`, e isso é medição e não esquecimento: três registros deste
   banco são *"Cortador de cerâmicas e azulejos MANUAL"*.
6. **O título traz o nome comercial inteiro.**

E por cima delas, a **unicidade**: o anúncio casa quando UM registro passa. Dois
passando é a armadilha 5 da 25.7 — no máximo um está certo e não há como dizer
qual, então os dois caem.

## A TRAVA 6 NASCEU NO ENSAIO, E ELA É A QUE VALE A LEITURA

O primeiro ensaio casou **13 de 15** e um dos treze estava **errado**:
`quartzolit-fundo-selador` casou com *"Selador PU30 Cinza Quartzolit 600g"*, que é
um selante de poliuretano e não o fundo selador acrílico de parede.

As cinco travas não viram nada, e o motivo é mecânico: elas comparam o registro com
os **irmãos**, e nenhum irmão da Quartzolit disputa a palavra `selador`. **Token que
nenhum irmão tem nunca era exigido de ninguém** — a palavra `fundo`, que é o produto
inteiro, era a única coisa que separava o certo do errado e era exatamente a que
ninguém cobrava. O buraco não era do irmão: era de não cobrar do título o nome que o
fabricante deu ao produto.

A trava 6 custou **três casamentos** — caiu de 13 para 10. É o lado certo de errar, e
está escrito para poder ser discordado.

## O QUE O ENSAIO MEDIU, COPIADO DA SHOPEE E NÃO IMAGINADO

A chave `verniz acrilico brilhante acrilex` devolveu oito anúncios. **Dois**
identificam um registro só. Os outros seis são o catálogo da armadilha 5:

    Verniz para Couro Acrilex 100ml Fosco Semibrilho Brilhante     <- fosco E brilhante
    Verniz Acrilico Acrilex 100ml / 250ml / 500ml (Fosco ou Brilhante)
    Verniz Acrilex Acrilfix Fosco, SemiBrilho ou Brilhante Spray
    Verniz Vitral Acrilex 100ml Incolor Brilhante Madreperola     <- outro produto

O terceiro é o que obrigou a trava 4 a existir na forma que tem. Ele traz `acrilfix`
e `brilhante`, e o banco **não tem** um `acrilfix fosco` para disputá-lo — então uma
regra que só exigisse os tokens do registro o aprovaria. **Quem escreve "Fosco,
SemiBrilho ou Brilhante" está vendendo a escolha, e a escolha não é um SKU.** Por
isso a regra proíbe o título de trazer o que é do irmão, e não só exige o que é dele.

## OS CINCO QUE NÃO SUBIRAM, E O ACHADO QUE VALE MAIS QUE OS DEZ LINKS

| registro | o que segurou |
|---|---|
| `quartzolit-borracha-liquida-elastica` | o `nome_comercial` é uma descrição, não o batismo do fabricante |
| `quartzolit-protetor-para-fachadas` | idem |
| `quartzolit-fundo-selador` | idem — e aqui a trava 6 **evitou** o casamento errado |
| `cortag-torques-azulejista-corte-curvo` | as chaves devolvem o anúncio de corte **reto**; sem a palavra `curvo` o título não separa os dois irmãos |
| `cascola-pl500-adesivo-de-montagem` | uma letra de gênero: o anúncio é *"Cola **Adesiva** Montagem Cascola Monta E Fixa Interior Pl500"* e o registro diz *"**Adesivo** de Montagem"* |

**Três dos cinco são da Quartzolit e têm o mesmo defeito, e ele não é da regra: é do
banco.** `impermeabilizante borracha liquida elastica quartzolit`, `protetor para
fachadas`, `fundo selador quartzolit` — minúsculas, com a marca repetida dentro, e
uma frase que **nós** escrevemos para descrever o produto. A seção 26 do contrato diz
que *o vocabulário da ilha classifica pela função e o fabricante batiza pela posição*,
e `nome_comercial` é o lado do FABRICANTE.

Nenhum portão via isso porque, até hoje, **nada comparava esse campo com um texto de
fora**. A regra de casamento foi a primeira a comparar — e o que ela achou não foi um
anúncio: foi um campo do próprio banco escrito no papel errado. Consertar os três é
coleta na página do fabricante, e o egresso a `quartzolit.weber` continua em 403.

**E o Cascola não foi consertado de propósito.** Afrouxar a trava para aceitar
`adesiva` onde o registro diz `adesivo` faria a régua passar por causa deste item, que
é critério dobrado para caber no dado que veio — a 1.2-b.4 nomeia isso. Fica o motivo
escrito em `afiliado.motivo_sem_ficha`, com as chaves tentadas e quantas ofertas cada
uma devolveu, para a próxima execução saber se vale retentar.

**As treze pastilhas não foram tentadas.** Elas dependem da decisão de
`afiliado.tipo_de_casamento: "equivalente"` descrita em `dados/links-afiliado-pendentes.md`,
e ela é do Raphael. A regra não as alcança e não deveria: a Shopee não anuncia a
codificação da Glass Mosaic.

## A ESCADA DE PALAVRA-CHAVE DESTA ILHA NÃO É A DA 25.6 AO PÉ DA LETRA, E ISSO ESTÁ ESCRITO

A 25.6 nasceu na Robometria, onde o degrau 1 é *"o código do fabricante sozinho"* —
e lá funciona porque `ERB10` é digitado no título pelo vendedor de reposição. Aqui os
códigos são `61341`, `68.51.050.000`, `REV110624`, `BRSA005`: **SKU interno de
catálogo industrial**, que nenhum vendedor de Shopee escreve. Código sozinho aqui casa
com o mundo, que é a armadilha 3 da 25.7. A escada desta ilha é marca + código, depois
marca + nome comercial, depois a chave de hoje, depois marca + os dois primeiros
tokens. **O degrau em que cada um casou fica gravado**, porque casar pelo código e
casar pela chave larga não valem o mesmo — e um deles casou pelo código: a torquês de
mosaico da Cortag, com `61341` no título do anúncio.

## O DEGRAU DA 25.1 NUNCA FOI CHUTADO PARA CIMA

Todos os dez entraram no **degrau 3**, anúncio de vendedor comum. Nenhum virou degrau
1, e a régua é dupla: o nome da loja tem de trazer a marca do fabricante **e** uma
palavra de loja oficial. `arteciaoficial` tem "oficial" e **não** é a Acrilex —
revendedor que se chama oficial é revendedor. Errar para baixo custa uma ressalva mais
dura na tela; errar para cima faz a metodologia declarar um rigor que a ilha não tem.

## DEZ FOTOS, E É A PRIMEIRA VEZ QUE ESTE BANCO GANHA IMAGEM SEM O FABRICANTE

O egresso a `acrilex.com.br`, `cortag.com`, `vonder.com.br` e `quartzolit.weber`
continua fechado, e continua na lista do Raphael. O que mudou é que agora existe um
anúncio **provadamente** daquele produto, e a foto dele é legítima. Largura e altura
saíram dos primeiros bytes do arquivo servido, por `ferramentas/medir-imagens.py`, que
já existia e **não foi reescrito** — a API não devolve dimensão, e caixa de foto sem
medida é o salto de layout da 22.4. Foto que não pôde ser medida não entra. Itens sem
imagem caíram de 35 para 25.

## O PORTÃO DO OUTRO LADO: A PROVA SE RECONFERE, NÃO SE ACREDITA

A prova ficou gravada em `afiliado.casamento`, com o título do anúncio que a produziu.
**Título gravado que ninguém reconfere é decoração, não procedência.** Então
`validar-banco.py` ganhou um portão que não lê o campo: ele passa o título gravado pela
regra **viva** de `casar-anuncio.py`, contra o banco inteiro, e reprova quando ela deixa
de identificar aquele registro. No dia em que alguém afrouxar a regra, renomear um
registro ou acrescentar um irmão que o título também descreve, o casamento para de valer
e o validador acusa. É a seção 4 do contrato aplicada ao banco: o resumo não pode
sobreviver ao fato.

O esquema foi para a **versão 7**, com `casamento` e `motivo_sem_ficha` escritos — e a
ausência de `casamento` nos cinco registros de 13/09 é declarada como **história, não
defeito**: a ficha deles veio por outro caminho, antes de a regra existir.

## AS DUAS BORDAS QUE A BATERIA OBRIGOU A BANCADA A FABRICAR

A primeira rodada de `mutacoes-casamento.py` deu **10 de 12**: duas mutações passaram
com a bancada verde, e as duas são travas que **nenhum registro do banco de hoje
exercita**.

- **A metade positiva da trava 3** só é a única a salvar quando o nome comercial de um
  registro cabe inteiro no do irmão e o único separador dos dois é o código. Isso não
  existe neste banco; existe no dia em que um fabricante lançar a versão "Spray" do que
  já vende. A bancada passou a fabricar esse par, e a mutação reprova.
- **A unicidade** só morde no **lote**: um anúncio que vende dois produtos de marcas
  diferentes não são irmãos um do outro, então as travas 3 e 4 não se olham. E o lote
  tem de começar pela palavra que os dois dividem, senão nem chega lá — a primeira
  versão desse título juntava a torquês da Cortag com o cortador da Vonder, e a **trava
  2 sozinha** já derrubava a Vonder, porque a cabeça do título era a torquês. Dois
  **vernizes** de marcas diferentes é o caso real.

**Bateria que só mede o banco de hoje envelhece junto com ele.**

## BANCADA E BATERIA

`ferramentas/teste-casamento.py`: **42 afirmações**, todas sobre títulos **reais**
devolvidos pela Open API em 29/09/2026, copiados byte a byte — com acento, com caixa
errada, com espaço duplo e com uma quebra de linha no meio de um deles, que é como o
vendedor escreveu. Título inventado mede a regra contra a imaginação de quem a escreveu.

`ferramentas/mutacoes-casamento.py`: **17 mutações em duas metades, 17 de 17
reprovadas**. Doze atacam a regra — cada trava cai uma vez, e **uma delas APERTA em vez
de afrouxar**, pondo `manual` nas armadilhas, porque régua que reprova o certo custa
tanto quanto régua que aprova o errado. Cinco atacam o **banco** e medem o portão novo
do validador: o título vira o do irmão, fica vazio, a ficha some, um campo de
procedência some, e — a que mais importa — **o banco muda e a prova caduca sem ninguém
tocar no campo**. As cinco reprovaram pelo portão do casamento, nenhuma por outro.

## O QUE NÃO FOI CLICADO, E POR QUÊ

Nenhum link desta ilha foi aberto. A 25.8 é explícita: o salto do encurtador é onde a
Shopee **conta** o clique, e autoclique com a etiqueta `clubedomosaico` apaga
justamente o primeiro clique orgânico que a leitura de 30/09 vai procurar. A prova de
vida de cada anúncio é a API tê-lo devolvido nesta passada, e está escrita assim, com
essas palavras, dentro de cada `casamento`.

## DE PASSAGEM, UM ALARME FALSO QUE VALE SER REGISTRADO

`conferir-atelie-no-ar.py` fechou com **1 falha** numa passada — *"com token a rota
responde 401"* — e a falha era da chamada, não do site: a ferramenta lê `argv[1]` como
**token**, e ela foi chamada com `.`, que é o argumento que quase todas as outras desta
ilha recebem como caminho. Chamada sem argumento ela fecha em **184 afirmações, 0 falha,
3 puladas**, exatamente como em 28/09. Fica escrito porque um 401 lido como defeito faria
a execução seguinte caçar um bug que não existe.

## BANCADAS E O AR

Casca **591**, F2 119, F1 200, Loja 208, Técnicas 123, Ateliê 289, Leads 211, Prestação
5 — zero falha. Validador do banco verde, com a linha nova **casamentos reconferidos:
10**. `validar-pastilhas.py` verde. `teste-casamento.py` 42 e 0.
**No ar: `conferir-no-ar.py` com 519 afirmações e 0 falha**, `conferir-tecnica-no-ar.py`
com 54 e 0, `conferir-atelie-no-ar.py` com 184 e 0. O soft 404 da borda continua
REPROVANDO a leitura do visitante por **1** defeito — é do hospedeiro, está pendente com
o Raphael e não mudou.

**O desembarque levou duas tentativas e isso é registro, não defeito:** a primeira
chamada do Sync leu a **revisão 48** com o `raw` do GitHub já servindo a **49** — cache
de borda do próprio GitHub, não do WordPress, que anexa `?v=time()` em toda leitura. A
segunda, dois minutos depois, aplicou. **Commit sem Sync não é entrega, e Sync que
responde não é entrega: o que é entrega é o número na tela.** Quem provou foi a página
de divulgação dizendo 20 e 18.

- **Próximo passo desbloqueado:** continua sendo a leitura de **30/09**, que libera o
  **BLOCO A** (CTR das três páginas de primeira página, veredito em 08/10) e, com ele, a
  metade que falta do item 4 da Sentinela de 28/09 — as duas são a mesma promessa de SERP
  nas mesmas páginas. O que **não** depende dela: (a) o egresso de fabricante, que trava
  `base` e `apoio` e está na lista do Raphael; (b) a decisão de
  `tipo_de_casamento: "equivalente"` das **treze pastilhas**, que é a maior fatia dos 18
  que restam no degrau 4 e é dele; (c) **os três `nome_comercial` da Quartzolit escritos
  como descrição em vez do batismo do fabricante** — item novo, achado por este bloco, que
  é coleta e não decisão, e que hoje esbarra no mesmo egresso de (a).

---

29/09/2026 13:17Z — A PÁGINA DE DIVULGAÇÃO DIZIA AO LEITOR QUE 28 BOTÕES NÃO RENDIAM COMISSÃO, E OS 28 SAEM COM `rel="sponsored"`

Casca **1.18.0**, manifest e `/status` na **revisão 48**. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudou — o BLOCO A do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09
segue limpa. O que mudou é o TEXTO de uma página que não rankeia e cujo produto
inteiro é dizer a verdade sobre dinheiro.

## O DEFEITO, E ELE ESTAVA NO AR HÁ QUATRO DIAS

`/divulgacao-de-afiliados/` servia, hoje de manhã, esta frase:

> *"Quando ainda não existe [link de afiliado para o produto], o botão leva você
> para a **busca daquele produto na loja**, e essa busca **não é link de
> afiliado**: ninguém nos paga por aquele clique."*

**É falso para 28 dos 38 materiais do banco.** O `url_busca` desses 28 é um
encurtador `s.shopee.com.br/...` com `sub_id_1 = clubedomosaico` — link de
afiliado, que rende comissão. O validador mede `piso nao rastreavel = 0` desde
25/09, e `conferir-no-ar.py` contou hoje **29 encurtadores servidos** nas 17
URLs, **todos com `rel="sponsored"`**.

**A DIREÇÃO DO ERRO É O QUE O TORNA GRAVE, e ela é a rara.** O defeito comum de
site de afiliado é esconder do buscador a relação paga. Aqui era o contrário: a
ilha **declarava** a relação paga ao Google, no atributo, e a **negava** a quem
lê, no texto — na única página do site cujo produto inteiro é a divulgação.

## NINGUÉM MENTIU: A FRASE ENVELHECEU SOZINHA, E ISSO TEM DATA

- **14/09/2026** — a busca CRUA subiu para o botão (f2 1.5.0, degrau 4 da 25.1).
  A frase nasceu nesse dia e **era verdadeira**: busca crua leva à mesma loja e
  não paga nada. Escrevê-la foi zelo, não descuido.
- **16/09/2026** — a Open API de afiliados entrou (25.6 do contrato). Encurtar
  deixou de exigir o painel do Raphael e virou uma chamada de rede.
- **25/09/2026** — o BLOCO 0 regerou os links pela API e **os 38 itens ganharam
  busca encurtada**. A frase ficou falsa nesse instante, e ninguém a tocou.

É a seção 4 do contrato na forma mais pura — o texto fica para trás em silêncio
—, com o agravante de que o texto era uma **afirmação sobre dinheiro**.

## E A CONTA EMBAIXO TINHA DUAS PARCELAS DE TRÊS

A mesma página publicava: *"os **38** materiais do banco têm, todos, um caminho
de compra. Em **10** deles esse caminho é um link de afiliado (…); em **0** ele é
a busca na loja, que não rende nada."*

**10 + 0 = 10, de 38.** Os 28 do meio — a busca encurtada — não apareciam em
parcela nenhuma, e **nenhum dígito estava visivelmente errado**. É assim que uma
classificação inteira some de uma página sem nenhum número parecer falso: a
conta tinha duas parcelas porque o mundo tinha dois estados em 14/09, e ganhou o
terceiro sem ninguém recontar as parcelas.

## POR QUE NENHUM PORTÃO VIA, E É ESTRUTURAL

O texto mora na **casca** e o `rel` mora na **F2**. Nenhuma régua comparava os
dois — e o docbloco da própria `cdm_f2_compra_html()` já dizia, desde 14/09, que
*"a busca ENCURTADA (…) é link de afiliado e rende comissão"*. **O código sabia
e a página não.** Duas verdades em dois snippets, sem nada entre elas.

## O QUE FOI CONSTRUÍDO

**A página** passa a nomear os **três** estados do botão, dizendo quais dois são
afiliado: ficha do produto (afiliado), busca daquele produto (afiliado, e a
palavra "também" está lá de propósito) e busca sem rastreio (não afiliado, e é o
único botão do site sem a marca de patrocinado). A conta passa a ter **três
parcelas que fecham no total**.

**E ela só sai pela via viva.** O instantâneo de `cdm_casca_numeros()` é de 14/09
e ainda declara `piso_nao_rastreavel => 15` num banco que tem zero; publicá-lo
hoje repetiria o defeito que esta versão conserta. Quando os cinco bancos não
chegaram, a seção fica com a **regra** — que é o que o leitor tem direito de
saber — e sem a contagem. **Estatística velha envelhece; disclosure velho mente**,
e essa é a distinção que justificou não seguir a convenção de "não mexer no
instantâneo" com um `if` em vez de um dígito.

**O portão (teste-casca, seção 15c) não guarda a resposta: ele pergunta ao
código.** Para cada um dos três estados, monta o `afiliado` à mão, chama
`cdm_f2_compra_html()`, lê se o `rel` emitido é `sponsored`, acha o `<li>`
correspondente na página pelo marcador do próprio texto e exige que as duas
classificações **batam**. No dia em que a escada mudar de novo, quem falha é o
par — não o lado que alguém lembrou de atualizar.

**A régua no ar** (`conferir-no-ar.py`) mede a mesma coisa no HTML servido: a
frase aposentada ausente, as três parcelas com os números **recontados dos
registros** (nunca dos cabeçalhos que a tela lê), e o `rel` de **cada** link de
loja das 17 URLs — 29 encurtadores, 29 patrocinados, 0 busca crua se dizendo
patrocinada.

## A MUTAÇÃO QUE PASSOU, E ELA VALE MAIS QUE AS SETE QUE REPROVARAM

`ferramentas/mutacoes-divulgacao.py`, oito mutações. Na primeira rodada **uma
passou**: *"a parcela da busca troca de fonte"* — trocar
`esperando_link - piso_nao_rastreavel` por `esperando_link` sozinho. Com
`piso_nao_rastreavel` em **0** os dois dão o mesmo número, e a trava **nasceu
inerte**: ela mediria o acaso de hoje, não a regra. O defeito que essa mutação
escreve só aparece no dia em que um item perder o rastreio — que é exatamente o
dia em que a página voltaria a contar como pago um clique que não paga.

A bancada passou a **fabricar esse dia** (regra 2 da seção 8: a grade inclui a
borda): um item de alicate perde a busca encurtada, e a conta tem de sair
10 · 27 · 1. Com a borda, **8 de 8 reprovaram**.

## DE PASSAGEM, UM MARCADOR DE PURGA QUE O PRÓPRIO BLOCO INVALIDOU

O portão de cache da seção 12 compara origem e canônico por **marcadores** de
texto, e o marcador de `/divulgacao-de-afiliados/` era o título antigo da seção.
Trocar o título derrubou o portão na primeira passada — e ele reprovou **como
devia**: marcador é o texto que só existe depois da revisão nova, então ele muda
junto com o bloco ou para de medir purga. Atualizado no mesmo commit.

## BANCADAS E O AR

Casca **591** afirmações (eram 587; as novas são o portão do par, as três
parcelas e a borda), F2 119, Técnicas 123, F1, Loja, Ateliê, Leads e Prestação
verdes, validador do banco verde. `mutacoes-divulgacao.py` 8 de 8 reprovadas.
**No ar: `conferir-no-ar.py` com 519 afirmações e 0 falha** (eram 508).
`leitura-do-visitante.py` continua REPROVADO por **1** defeito, o mesmo de hoje
de manhã — o soft 404 da borda, que é do hospedeiro e está pendente com o
Raphael. A borda já serve o texto novo: lida **sem** quebra de cache, a página
traz o título novo e as três parcelas.

- **Próximo passo desbloqueado:** continua sendo a leitura de **30/09**, que
  libera o **BLOCO A** (CTR das três páginas de primeira página, veredito em
  08/10) e, com ele, a metade que falta do item 4 da Sentinela de 28/09 — as duas
  são a mesma promessa de SERP nas mesmas páginas. O que **não** depende dela
  continua sendo o egresso de fabricante, que trava `base` e `apoio` e está na
  lista do Raphael. **E entra um item novo de valor comercial, que não depende
  de nenhum dos dois:** 28 dos 38 materiais estão no degrau 4 da 25.1 (busca, que
  converte pior que ficha) — entre eles as **13 pastilhas**, que são a vitrine da
  F1. Subir degrau é trabalho de API da Shopee, que esta nuvem alcança; o que
  falta nas pastilhas é a decisão de `afiliado.tipo_de_casamento: "equivalente"`
  descrita em `dados/links-afiliado-pendentes.md`, e ela é do Raphael.

---

29/09/2026 11:12Z — A LEITURA DO VISITANTE, E ELA ACHOU UM DEFEITO NO AR NA PRIMEIRA VEZ QUE OLHOU

Bloco de instrumento, escolhido por eliminação e com a eliminação escrita: hoje é
**29/09**, véspera da leitura, e o BLOCO A do despacho do Raphael de 24/09 proíbe
mexer na promessa de SERP das páginas que rankeiam até 30/09. A metade aberta do
item 4 da Sentinela de 28/09 espera o BLOCO A pela 18.1; os itens 1 e 2 de 23/09
têm a última condição na leitura de amanhã; e `base` e `apoio` esperam **canal**,
não decisão — o que foi **remedido** nesta execução, e continua fechado: o egresso a
`quartzolit.weber`, `tekbond`, `loctite`, `cascola` e `pastilhart` devolve **403 ao
CONNECT** (política de egresso), cinco domínios, cinco tentativas, com o domínio da
ilha em 200 na mesma passada. **Quarto bloco seguido parando nessa porta**, e agora
com o pedido escrito, que é o que faltava (ver "O que depende do Raphael").

**NENHUM ARQUIVO PUBLICÁVEL MUDOU, e por isso não houve Sync.** Manifest e `/status`
seguem na **revisão 47**. Nenhuma URL nova, nenhum endereço mudou, nenhum `<title>`,
nenhuma `description` e nenhum texto de página mudou. O ar está exatamente como
estava — que é a condição que o despacho do Raphael impõe a esta véspera.

## O ACHADO, E ELE NÃO ESTAVA ESCONDIDO: ESTAVA ESCRITO AQUI HÁ QUATRO DIAS

O BLOCO C, em 25/09, mediu e escreveu, com todas as letras:

> *"`conferir-no-ar.py` gruda `?v=<agora>` em toda URL — e está certo, porque nasceu
> para provar que o Sync aplicou a revisão nova. O preço é que **ele nunca vê o que o
> visitante vê**. Cache servindo página velha para gente de verdade passa por baixo
> das 488 afirmações dele sem encostar em nenhuma."*

Ficou **quatro dias sem instrumento**. Esta execução construiu o instrumento e, na
primeira passada, ele achou um defeito que está no ar agora.

## O DEFEITO, MEDIDO E REPETIDO ANTES DE VIRAR AFIRMAÇÃO (20.2)

**Toda URL que não existe nesta ilha responde 404 na primeira leitura e 200 na
segunda**, por duas horas.

| leitura | resposta |
|---|---|
| 1ª (cache sem a entrada) | **404**, `cache-control: no-cache, must-revalidate, max-age=0, no-store, private` — a **origem**, e ela está **certa** |
| 2ª em diante, por 2h | **200**, `x-proxy-cache: HIT`, `x-server-cache: true`, `max-age=7200`, corpo = a página de **404 desta ilha** |

**Como foi provado que é mecanismo e não coincidência:** uma URL **virgem**, com o
relógio no nome, nunca lida por ninguém — 1ª **404**, 2ª **200**, 3ª **200**. E as
três URLs inexistentes lidas uma vez minutos antes, todas 404 na primeira, davam
**200** na segunda. Mais cinco leituras seguidas de uma delas: 200, 200, 200, 200,
200. Com quebra de cache, na mesma janela: 404, 404, 404.

**É SOFT 404.** 200 com corpo de erro faz o Google contar a URL como existente. Quem
lê uma URL duas vezes é exatamente o Googlebot, e o orçamento de rastreamento é o
recurso escasso da 14.1 — esta ilha tem **15 URLs ainda não indexadas**. É a mesma
família, e a mesma causa, do outro achado do BLOCO C: *"o rastreador nunca recebe
redirecionamento"*. A camada de cache responde antes do WordPress.

**POR QUE NENHUM PORTÃO DAQUI VIA.** As 504 afirmações do `conferir-no-ar.py` passam
por `buscar()`, e `buscar()` gruda a quebra de cache. **Todas mediam a origem.** A
afirmação `[rota] caminho inexistente responde 404` passa, e está **certa**: a origem
responde 404. O defeito mora na camada da frente, e até hoje nada daqui a lia.

## O QUE FOI CONSTRUÍDO

`ferramentas/leitura-do-visitante.py` — lê as **17 URLs do sitemap sem quebra de
cache**, que é a leitura que se parece com a do Google, e termina na sonda de 404
pela borda.

- **A régua é função pura** e tem `--autoteste` com **11 casos fabricados, um por
  ramo** (11 de 11, zero falha). A varredura fechou em 17 esperado e zero defeito nas
  URLs, e esta ilha já escreveu em 25/09 que *"passada limpa em portão que nunca
  acusou nada não prova nada"*.
- **A sonda leva sufixo novo a cada passada**, e isso não é detalhe: com URL fixa ela
  mediria a entrada de cache que a **passada anterior** criou, e acusaria a si mesma
  para sempre.
- **O visitante é lido PRIMEIRO**, antes da origem: a quebra de cache aquece a borda,
  e medi-la depois de aquecer mediria o instrumento, não o site.
- O `conferir-no-ar.py` **importa** essa régua em vez de copiá-la — uma terceira
  reimplementação de "o visitante recebeu a ilha" não acrescentaria independência, só
  uma cópia para envelhecer calada (é o mesmo motivo escrito em `cobertura.py`). Foi
  de **504 para 508 afirmações, 0 falha**.

## AS DUAS POLÍTICAS, E NENHUMA DELAS É NOVA

**A ferramenta REPROVA** — fecha em `REPROVADO: 18 URL(s) lidas, 1 defeito(s)`, e é
para ficar vermelha até a pendência fechar. **O portão de entrega REGISTRA**, com o
número, a data e o dono na linha. A jurisprudência é desta ilha, de 14/09, e está
escrita no próprio `conferir-no-ar.py`: portão vermelho que nenhuma execução consegue
fechar *"se aprende a ignorar, que é pior do que não ter portão"*. **No dia em que o
Raphael fechar, a linha vira portão** trocando `ok(True` por `ok(_borda_404_ok` — e
isso está escrito no arquivo, ao lado da linha, não só aqui.

**O que impediu a outra saída fácil, e vale registrar:** a primeira tentação era fazer
a afirmação reprovar de qualquer jeito, "para não deixar passar". Isso travaria toda
execução futura desta ilha num vermelho que nenhuma delas pode consertar — o cache é
do hospedeiro, roda antes do PHP, e a origem já manda `no-store`, que ele ignora.

## O RETRATO "ANTES" DO BLOCO A, QUE ERA O ÚNICO PEDAÇO DELE QUE NÃO ESPERAVA

O BLOCO A manda, textualmente: *"Gravar em `dados/posicoes.md` o título e a meta ANTES
da troca, na mesma linha da série, para haver com o que comparar depois."* Estava por
fazer, e **depois da troca não teria como ser remontado** — o HTML servido não guarda
o que servia ontem. Gravado, **medido pela borda** (a leitura do Google), com contagem
em caracteres decodificados:

| URL | `<title>` | nº | `description` | nº |
|---|---|---|---|---|
| `/materiais/qual-cola-usar-no-mosaico/` | Qual cola usar no mosaico, e qual rejunte – Clube do Mosaico | 60 | … pela declaração do próprio fabricante … | 183 |
| `/materiais/quantas-pastilhas-para-mosaico/` | Quantas pastilhas e quanto rejunte comprar – Clube do Mosaico | 61 | … a conta da pastilha pequena e não a do azulejo de obra | 165 |
| `/como-fazer/o-que-e-mosaico-picassiete/` | O que é mosaico Picassiete, e como colar – Clube do Mosaico | 59 | … com o que colar o caquinho em cada superfície … | 192 |
| `/como-fazer/o-que-e-trencadis/` | O que é trencadís, e com o que colar o caco – Clube do Mosaico | 62 | … de onde vem o nome ligado a Gaudí … | 189 |

**O que o retrato já diz para quem escrever o BLOCO A depois de 30/09:** nenhum dos
quatro `<title>` promete um número, e nenhuma das quatro `description` promete a
faixa — as duas alavancas que a 12.1 nomeia para a banda de 4 a 10 estão **inteiras
por usar**. E os quatro títulos cabem em 64 com folga de **2 a 5 caracteres**: quem
for enfiar um número ali vai ter de tirar palavra, e a candidata é a marca no fim,
que foi o caminho do precedente da robometria.

## MEDIDO NESTA EXECUÇÃO

- `conferir-no-ar.py`: **508 afirmações, 0 falha** (eram 504).
- `leitura-do-visitante.py --autoteste`: **11 de 11**, 0 falha.
- `leitura-do-visitante.py`: 17 URLs esperado, **0 janela de cache aberta**, **1
  defeito** — a sonda de 404.
- `teste-casca.php` **569**, `teste-loja.php` **208**, `validar-banco.py` OK,
  `varrer-canonicas.py --autoteste` **11 de 11**. Zero falha.
- Cabeçalho do `ESTADO.md` em `yaml.safe_load`: **ok**.
- Rede da ilha pela 20.2 no começo da execução: `/` **200**, `wp-sitemap.xml` **200**,
  `/wp-json/clubedomosaico/v1/status` **revisão 47**.

## O QUE DEPENDE DO RAPHAEL — três coisas, e duas já estavam abertas

1. **NOVA: o soft 404 da borda.** No cPanel da HostGator, cache de página que não
   guarde resposta 404. Está no `ESTADO.md` e em `dados/consertos.md`, com o comando
   que reconfere.
2. **O egresso aos domínios de fabricante** (20.1 e 20.3), e é o que destrava o
   primeiro SKU de `base` e de `apoio` — **quarto bloco seguido parando aqui**.
   `quartzolit.weber`, `tekbond.com.br`, `loctite.com.br`, `cascola.com.br` e
   `pastilhart.com.br` respondem **403 ao CONNECT**. O caminho está na 20.1:
   `claude.ai/code` → seletor de ambiente → Nuvem → engrenagem → Domínios permitidos.
   **Sem PDF de fabricante não sai FISPQ de epóxi nem `dureza_shore_a`**, e as duas
   categorias já têm regra, portão e bateria verde esperando só a frase.
3. **O acesso da conta `sentinela@` ao Search Console** desta propriedade, que
   continua aberto desde o BLOCO C e é o que tira a nota de rodapé da leitura de
   30/09.

## PRÓXIMO PASSO

**A leitura de 30/09 é amanhã**, e ela destrava de uma vez o BLOCO A (agora com o
retrato "antes" já gravado, que era pré-requisito dele), a faixa de `description` das
quatro travadas, a terceira condição do item 1 de 23/09 e a segunda metade do item 2.
O que sobra antes disso continua sendo **canal**, não decisão.

**Memória:** `/areas` e `/topics` não existem neste ambiente — conferido, como em
execuções anteriores. O estado está no `ESTADO.md`, neste registro e no `PROMPT.md`.

28/09/2026 19:42Z — A LINHA DA PEÇA ENTRA NA ÁRVORE, E O QUE FALTAVA NÃO ERA A LINHA: ERA A CHAVE

Item 4 da lista de desbloqueados do `PROMPT.md` ("a linha da peça na tabela do
`ARVORE.md` — é conserto de TESTE, não de documento"). Casca **1.17.0**, Loja
**1.4.0**, manifest na revisão **47**.

**Por que este item e não outro:** hoje é 28/09 e **todo** o resto da fila desta
ilha espera 30/09. O BLOCO A do despacho do Raphael de 24/09 espera a leitura de
30/09 por ordem escrita dele; a metade aberta do item 4 do despacho da Sentinela
de 28/09 (a faixa de 120 a 160 nas quatro páginas que já tinham `description`)
espera o BLOCO A pela 18.1; os itens 1 e 2 do despacho de 23/09 têm a última
condição na leitura de 30/09; e as duas categorias vazias que sobram (`base` e
`apoio`) já têm decisão de campo e portão — o que falta nelas é **canal**, não
decisão: frase literal de fabricante que esta nuvem consiga citar, e o egresso
de PDF continua fechado. Este item não toca em nenhuma das páginas que estão na
primeira página do Google, não cria URL nova e não mexe em `<title>` nem em
`description` de nada — então é o único que podia sair hoje sem misturar causa
na janela de medição que o Raphael mandou preservar.

**A DECISÃO QUE O `ARVORE.md` DEIXOU ESCRITA PARA A FUNDAÇÃO (19.2), E QUAL FOI.**
A seção 5 daquele arquivo tinha duas opções defensáveis: ou o filtro da Loja
passa a chavear por `CDM_LOJA_BASE . '/' . $slug`, ou a tabela declara a exceção
e o portão passa a admiti-la. **Escolhida a primeira**, e o que decidiu não foi
gosto: foi um **segundo defeito** que só existe com o slug nu e que a segunda
opção não consertaria.

**O SEGUNDO DEFEITO, MEDIDO NA BANCADA ANTES DE QUALQUER CONSERTO:** peça cujo
slug bate com o de uma página da raiz servia a trilha **daquela página**. Peça
chamada `sobre` saía com `Início › Sobre` — sem o nome da peça na trilha — e o
`BreadcrumbList` levava a URL de `/sobre/`. O mesmo com `privacidade` e
`contato`. A causa é a ordem: `cdm_casca_slug_atual()` remonta o caminho pela
definição de PÁGINAS, casando por último nível, e a peça é tipo próprio. Com o
caminho inteiro a colisão deixa de existir **por construção** — `loja/sobre` não
é `sobre`. Uma exceção documentada continuaria sendo uma exceção no código.

**O CONSERTO, E ELE TEM DUAS PONTAS E UMA FUNÇÃO SÓ.** `cdm_loja_caminho_da_peca()`
monta o caminho, e dela saem as duas declarações: a chave do filtro `cdm_arvore`
(onde a peça mora) e a resposta do filtro novo `cdm_caminho_atual` da casca (qual
página está sendo servida). As duas pontas montando a própria string são a
**origem** do defeito, não o conserto dele: se uma mudasse de formato e a outra
não, a trilha da peça sumiria da tela sem cor nenhuma. O `teste-loja.php` cobra
que só **um** lugar do snippet monte o caminho, e que as duas declarações passem
pela função.

**A PRIMEIRA ESCRITA DO CONSERTO ERROU, E O ERRO ESTÁ AQUI PORQUE A MUTAÇÃO DELE
FICOU:** o filtro nasceu **depois** do laço da definição de páginas. O caso comum
ficou verde na hora — `loja/vaso-azul-com-flores` — e a colisão continuou de pé
inteira, porque o laço casava `sobre` e retornava antes de o filtro ser chamado.
Medido, não deduzido: a régua de colisão reprovou. O filtro passou a falar
**antes**, e a mutação `o filtro do caminho fala DEPOIS do laco das paginas`
existe para ninguém reverter isso sem ver.

**O PORTÃO TEM TRÊS PERNAS, E NENHUMA SOBRA** (item 21 do `teste-casca.php`):

| perna | o que cobra | o que ela impede |
|---|---|---|
| documento → código | a linha da tabela existe no mapa, **com a peça servida** | a divergência silenciosa de sempre |
| documento → realidade | o slug da linha está em `dados/pecas.json` | portão vazio: a bancada fabrica a peça com o slug que a tabela pedir, então linha inventada passaria |
| realidade → código | **todas** as 5 peças da cópia pousam em `loja/<slug>`, nível 2, mãe `loja` | a tabela com uma linha virar álibi para as outras quatro |

**O número de peças não foi digitado no documento**, e isso é decisão: quem
publica peça é a artesã, no dia que ela quiser, e tabela escrita pela Fundação
que precise de commit a cada peça nova nasce velha. A tabela nomeia a **âncora**
(`/loja/quadro-flores-do-campo/`, a primeira que ela publicou, em 14/09) e o
portão conta o resto contra a cópia da seção 24. Hoje são cinco, e as cinco são
medidas.

**E a decisão declarada no filtro continua de pé, com portão próprio:** fora de
uma requisição de peça, `/loja/` **não** tem filha no mapa. Sem essa afirmação o
conserto preguiçoso — declarar todas as peças sempre — passaria, e encheria a
lista de irmãs de `/loja/` de peça, que é outra decisão e não é a de hoje.

**UMA MUTAÇÃO PRÉ-EXISTENTE ESTAVA INERTE, E O ACHADO É DO MESMO DIA.**
`dois slugs com o mesmo ultimo nivel` casava com a entrada `'sobre'` escrita em
UMA linha da definição de páginas; a casca **1.16.0**, de algumas horas antes
nesta mesma quarta, quebrou a entrada em várias linhas quando a `description`
ganhou dono. A mutação parou de achar o alvo e passou a se declarar INVÁLIDA — e
a bancada conta inválida como "passou", então a trava dos slugs repetidos ficou
**sem ninguém a vendo**, justamente a trava que sustenta a premissa do caminho
remontado. Conferido que já estava inerte **antes** deste bloco. O alvo agora é a
**abertura** da entrada, que não depende de quantos campos ela tem. É a mesma
cicatriz que `m_pagina_de_prova_deixa_de_ser_citada` registra em comentário desde
12/09, e ela voltou.

**As baterias.** `ferramentas/mutacoes-arvore.py` foi de 21 para **29 mutações,
29 reprovadas, 0 passaram** — as oito novas: o slug nu de volta, uma ponta só
mudando de formato, o filtro falando depois do laço, a tabela nomeando peça que
não existe, mãe divergente na linha da peça, a linha sumindo da tabela, toda peça
entrando servida ou não, e só a peça da tabela sendo atendida.

**Bancadas:** `teste-casca` 569 (eram 563), `teste-loja` 208 (eram 196), e
`leads`, `atelie`, `f1`, `f2`, `tecnicas`, `prestacao-rejunte` sem falha.

**O DESEMBARQUE, e a régua que ele exigiu.** Revisão **47** no ar às 19h48Z, 14 aplicados; `/status`
na 47 e a rota pública da loja servindo `versao_loja: 1.4.0`. **E o `conferir-no-ar.py` não media a
trilha — nenhuma linha dele falava dela**, o que para este bloco seria conferir tudo menos o que
mudou. Entraram três afirmações, medidas no HTML servido das 5 peças: a trilha existe (a chave nova
não a apagou), ela é `Início › Loja › <nome da peça>` com o degrau atual sem link e com
`aria-current`, e o `BreadcrumbList` sobe por `/loja/` com a numeração sem buraco. **5 de 5 nas
três.** O total foi de 501 para **504 afirmações, 0 falha**.

*(O Sync leu a revisão 46 em três disparos seguidos antes de pegar a 47: é o cache de borda do
`raw.githubusercontent.com`, que serviu 47 para esta nuvem e 46 para o servidor do site por alguns
minutos. Repetido até passar, como a 20.2 manda — não é bloqueio, e fica registrado porque a próxima
execução que vir "revisão anterior" logo depois de empurrar vai querer saber que isso é esperado.)*

**Uma afirmação que escrevi e apaguei no mesmo bloco, registrada porque o erro é
da família que esta ilha mais paga:** a primeira versão da régua de colisão do
`teste-loja.php` terminava em `|| true`. Ela passava sempre e não media nada —
portão que nunca pode reprovar. Foi trocada pela medição real: a página `/sobre/`
de verdade continua respondendo `sobre`, que é o outro lado da borda e o que
impede o conserto de ter mandado toda página singular para baixo de `/loja/`.

- **Nenhuma URL nova, nenhuma URL mudou de endereço, nenhum texto de página
  mudou.** O que muda no ar é a chave interna do mapa e a trilha das peças em
  caso de colisão de slug — que hoje não acontece em nenhuma das cinco.
- Próximo passo: **a leitura de 30/09** destrava, de uma vez, o BLOCO A do
  despacho do Raphael de 24/09, a faixa de `description` das quatro páginas
  travadas, a terceira condição do item 1 de 23/09 (`/author/` sair de
  `dados/posicoes.md`) e a segunda metade do item 2 (o formato
  `clubedomosaico-f2---` no Relatório de cliques). Antes disso, o que sobra na
  fila é **canal**, não decisão: `base` e `apoio` esperam frase literal de
  fabricante, e é o terceiro bloco seguido parando na mesma porta (PDF).

10/09/2026 — pasta da ilha criada pelas mãos, a pedido da sessão de conversa

- Criada a pasta `ilhas/clubedomosaico/` com `snippets/`, `conteudo/`,
  `dados/`, `identidade/logo/`, `manifest.json` (revisao 0, nenhum item, nada
  marcado para publicar), `README.md`, `PROMPT.md`, `ESTADO.md` e este
  registro.
- `snippets/clubedomosaico-sync.php` gerado a partir de
  `ilhas/robometria/snippets/robometria-sync.php`, sem outra alteracao alem da
  troca de nome da ilha. Passou em `php -l`.
  sha256: `0b893702fd4614928adeddabdf51465f7214304798640041c6a277f2fcfd0649`
- Proximo passo: bloco 1 — corpus de buscas em `dados/corpus-buscas.md`. Nao
  depende de site nem de WordPress.

10/09/2026 15:21Z — BLOCO 1 ENTREGUE: corpus de buscas

- `dados/corpus-buscas.md` criado com os tres clusters da ilha
  (materiais/ferramentas, pecas prontas, aprender), a SERP classificada
  consulta a consulta em aberta/tomada/armadilha pela regra da secao 14.9, e a
  ordem da fila derivada do cruzamento intencao de compra x chance de primeira
  pagina. Manifest na revisao 1; `publicar: false`, entao **nao houve Sync
  nesta execucao** — a secao 4 do contrato so exige acionar o Sync em bloco que
  mexe em conteudo publicavel, e este nao mexeu.
  sha256: `5580e5fa9084b4c06da3bb26e8e2088936b9cffbb65ca60f1b4de243f14db695`
- Procedencia separada em duas coletas, e assim escrita no arquivo: a faixa de
  volume veio do Planejador na conta do Raphael (10/09, via `PROMPT.md`, nao
  refeita aqui); a SERP foi coletada nesta execucao por busca web da nuvem, com
  os ocupantes do top 10 nomeados. **CPC nao foi coletado e esta declarado como
  ausente, nunca estimado** — a fila do bloco 1 pedia CPC e ele nao existe sem
  o painel autenticado.
- Tres achados medidos que mudam o desenho das ferramentas:
  (1) toda a SERP de rejunte responde a pergunta de OBRA (0,2-0,4 kg/m2, azulejo
  grande) e portanto esta ERRADA para peca de artesanato com pastilha de 1x1 cm
  — a F1 nao compete com essas paginas, responde outra coisa;
  (2) a regra cola x base ja circula em blog, mas sem fabricante, codigo, data
  nem separacao interno/externo/molhado — abre a F2 e ao mesmo tempo proibe usar
  a SERP como fonte dela;
  (3) as lojas vendem pastilha em tres unidades diferentes (100 pecas, 100 g,
  placa 30x30 com 225), entao converter peca <-> grama <-> placa e numero
  proprio da ilha.
- Tomadas, e por isso FORA da fila: `curso de mosaico` (top 10 sao escolas reais
  com professora e turma; a ilha nao vende curso), `presente artesanal` (Elo7) e
  `vaso centro de mesa` (Leroy). `mosaico bizantino` entrou como alvo: faixa
  1k-100k com a primeira pagina em portugues ocupada por resultado em espanhol.
- Concorrente nomeado para a leitura semanal acompanhar: `mosaico.arq.br`, que
  vende peca artesanal e curso — o mais parecido com esta ilha inteira.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente).
  O estado vive no `ESTADO.md` desta pasta, como manda o `PROMPT.md`.
- Proximo passo desbloqueado: **bloco 2** — `dados/especificacao-calculadoras.md`
  e `dados/constantes.json`, comecando pela F2 (seletor de cola e rejunte), que
  o corpus mostrou ser a de maior intencao e menor concorrencia. Constante so
  com fonte de fabricante e data (Quartzolit, Tekbond, Loctite, Cascola); sem
  fonte, `pendente` e fora de formula publicada. Nao depende de site.

10/09/2026 19:30Z — BLOCO 2 ENTREGUE: especificacao das duas ferramentas + constantes

- `dados/constantes.json` (11 constantes de fabricante, 6 pendencias nomeadas) e
  `dados/especificacao-calculadoras.md` (contrato de construcao da F1 e da F2). Manifest na
  revisao 2; os dois com `publicar: false`, entao **nao houve Sync nesta execucao** — a
  secao 4 do contrato so exige Sync em bloco que mexe em conteudo publicavel.
  sha256 constantes: `99c6c5cb7130fc0428bb15312226c74ced0b51fa79cc95c3ca4de7f45dca1e39`
  sha256 especificacao: `1189ad6f0fc3e21ed046acc7d2215e0c947f267b1557b07b1c87a05edb58fa7a`
- **Procedencia, e o limite dela, declarados item a item.** A coleta foi por busca web
  restrita ao dominio de cada fabricante (quartzolit.weber, tekbond.com.br, cascola.com.br,
  henkel.com.br). `curl` e `WebFetch` para esses dominios voltaram `EGRESS_BLOCKED` /
  `connect_rejected` — a rede das rotinas libera os dominios das ilhas, `*.googleapis.com` e
  `github.com` —, entao os PDFs de boletim tecnico **nao foram abertos linha a linha**. Cada
  constante diz isso em `fonte_tipo` e marca `conferir_no_pdf`. **Nada de blog, loja ou
  agregador entrou**: o bloco 1 tinha medido que a regra cola x base circula na SERP sem
  fabricante, codigo nem data, e a fila proibiu usar a SERP como fonte da F2.
- **O achado que decide a F2:** a ficha BRSA004 do Silicone Acetico Construcao Tekbond
  (revisada em 10/2025) lista espelho, concreto, cimento, tijolo, calcario, superficie
  alcalina, superficie pintada ou porosa, acrilico, aquario, metal corrosivel e imersao
  continua entre as superficies em que o produto NAO deve ser usado — que sao exatamente os
  casos em que o mosaico artesanal brasileiro usa silicone acetico por indicacao de blog.
  Isso torna a elegibilidade da secao 7 **mecanica**: basta uma restricao bater com a entrada
  para o produto sair dos recomendados e ir para a secao rotulada, com a frase do fabricante
  e a data. E o par acetico/neutro sendo do mesmo fabricante, a F2 diz "nao use A, use B" sem
  sair de uma fonte so.
- **O achado que decide a F1:** aplicando a formula publicada pela propria Quartzolit
  (`((A+B) x E x L x CR)/(A x B)`, CR 1,75 no exemplo do fabricante) ao tamanho real da
  pastilha de artesanato, pastilha de 1x1 cm com 4 mm de espessura e junta de 2 mm consome
  **2,80 kg/m2** de rejunte — 7 a 14 vezes os 0,2-0,4 kg/m2 que a primeira pagina do Google
  publica com azulejo de obra. A tabela pre-renderizada de 12 pecas tipicas ja esta calculada
  no arquivo. Segundo numero proprio: a placa 30x30 com 225 pastilhas tem passo 30/raiz(225)
  = 2,00 cm, ou seja, **nao e pastilha de 1x1 cm** — e o erro de quem compara preco entre
  loja que vende por peca e loja que vende por placa.
- **O que NAO foi publicado, de proposito.** A espessura da pastilha virou campo de entrada,
  nao constante, porque nenhum fabricante de pastilha de artesanato a padroniza. A coluna de
  gramas de cola da F1 nasce vazia com explicacao na tela: falta o consumo em kg/m2 da
  cimentcola e o rendimento do silicone por area (o fabricante declara por cordao), e as duas
  estao em `pendentes`. A F2 declara duas faixas DESCOBERTAS — peca em contato permanente com
  agua e base de plastico — em vez de preencher no chute. A conversao grama <-> peca fica
  pendente por SKU, para o banco MATERIAL do bloco 3 coletar com data.
- A especificacao ja carrega o bloco de compra obrigatorio ANTES da prova de procedencia,
  pela cicatriz da Robometria de 10/09: nenhuma das duas ferramentas vai ao ar sem ele, mesmo
  com `afiliado.url` vazio, e a ilha reporta quantos itens esperam link.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como no
  bloco 1. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 3** — modelo do banco (MATERIAL, PECA, TECNICA). A
  especificacao ja nomeou os campos que as duas ferramentas exigem de MATERIAL: categoria
  cola (com a lista de restricoes declaradas por produto), rejunte (com faixa de junta) e
  pastilha (com lado, espessura e unidade de venda). Nao depende de site. Depois dele, o
  bloco 4 fica dependendo so do WordPress existir.

10/09/2026 23:16Z — BLOCO 3 ENTREGUE: modelo do banco + categoria COLA + verificador

- `dados/esquema-banco.json` (modelo das entidades MATERIAL, PECA, TECNICA e da serie
  temporal COTACAO), `dados/materiais-colas.json` (5 registros da categoria cola) e
  `ferramentas/validar-banco.py`. Manifest na revisao 3; tudo com `publicar: false`, entao
  **nao houve Sync nesta execucao** — a secao 4 do contrato so exige Sync em bloco que mexe
  em conteudo publicavel, e a ilha ainda nao tem WordPress.
  sha256 esquema: `862f84b64ed9005ab00dc2c97335e470c1c44d63b63d025e51e93be77e50ed33`
  sha256 colas:   `0df9a40da7343f2a96675aaf4c9b0bc8506fed008fc6781afa6f37b9d62a090d`
  sha256 validador: `ac3f1f6001ea405f26303b3ecf6a82092329926701070ee686eb61909db27f3a`
- **NENHUM dado novo foi coletado, e isso e proposital.** Os 5 registros de cola sao a
  transposicao campo a campo do que o bloco 2 ja tinha colhido em `dados/constantes.json`,
  com a mesma fonte, o mesmo tipo de documento e a mesma data. O que o bloco acrescenta e
  ESTRUTURA: a lista literal do fabricante virou campo COM PESO — indicado, proibido, nao
  recomendado, delimita ambiente, resiste a ambiente — e por isso a matriz da F2 passou a ser
  RECOMPUTADA em vez de lida.
- **O verificador nao e enfeite.** Ele recomputou as 18 celulas base x ambiente pelas cinco
  regras de elegibilidade e bateu com a tabela publicada no esquema. Tres mutacoes provaram
  que ele falha quando deve: apagar `espelhos` da lista de restricoes da ficha BRSA004
  (2 erros, o acetico deixa de ser eliminado no espelho), promover o press release do
  Durepoxi de nivel 4 para 3 (20 erros, ele invade os recomendados de 8 celulas) e criar
  `dados/pecas.json` (1 erro: PECA nao vive no repositorio).
- **QUATRO ACHADOS que corrigem a matriz que o bloco 2 tinha escrito a mao**, e por isso a
  secao 1.3 da especificacao ganhou uma nota dizendo que quem manda agora e o esquema:
  (1) **a cimentcola AC-II nao tem declaracao de SUBSTRATO** — a especificacao a recomendava
  para base de cimento citando que ela e declarada para "area interna e externa", que e
  AMBIENTE; as unicas superficies nomeadas na coleta ("ceramicas e placas de pedra natural de
  ate 120 x 120 cm") sao a PECA ASSENTADA. Ela sai dos recomendados de todas as celulas, e
  quem responde base de cimento e o silicone neutro, que declara concreto e alvenaria com
  todas as letras;
  (2) **ceramica e vidro em ambiente comum sao EMPATE** entre acetico e neutro — o mesmo
  fabricante declara ceramica para os dois e nenhum declara o ambiente —, entao a pagina
  lista os dois em vez de fingir uma preferencia que a fonte nao sustenta;
  (3) **em sol e chuva o acetico nao fica "em segundo lugar", fica FORA**: ambiente de
  exposicao continuada exige declaracao explicita, e so o neutro declara chuva e raios UV;
  (4) **MDF molhado e externo TEM resposta** — o neutro declara madeira entre os substratos
  que veda —, ao contrario do "a ilha nao recomenda" da especificacao, que so tinha olhado
  PVA e acetico. O PVA sai desses ambientes por DELIMITACAO do proprio fabricante
  ("ambientes internos"), nunca por proibicao inventada.
- **O que o esquema tem de proprio desta ilha**, e que nao foi copiado de Aquametria nem de
  Robometria: o campo que decide a recomendacao e NEGATIVO (a lista de restricoes vale mais
  que a de indicacoes); existem TRES estados de declaracao e nao dois, porque silencio nao e
  proibicao e foi o Cascorez que obrigou isso; a escada de fontes tem um nivel 4 criado para
  material de imprensa, que e o que mantem a peca submersa como faixa DESCOBERTA mesmo com o
  Durepoxi declarando secar debaixo d'agua; e PECA e a unica entidade do Arquipelago que NAO
  e arquivo do repositorio — o validador falha de proposito se alguem criar `dados/pecas.json`.
- **Uma correcao de entrada para o bloco 4:** a secao 1.2 da especificacao tem so "vidro",
  mas a matriz distingue vidro comum de vidro LAMINADO — e a distincao decide o produto
  (o acetico e proibido no laminado). O formulario precisa da pergunta, escrita em portugues
  de gente: "o vidro tem uma pelicula entre duas camadas?".
- 5 itens esperando link de afiliado e 5 sem imagem — os cinco da categoria cola. Geracao de
  link e da Sentinela estrategica, no navegador, e nunca da Fundacao.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos
  blocos 1 e 2. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **as categorias REJUNTE e PASTILHA do banco**, que nao dependem
  de site e que o esquema ja deixou com os campos nomeados (rejunte com faixa de junta;
  pastilha com lado anunciado, passo de fabrica, espessura e unidade de venda). O bloco 3b
  (casca) e o bloco 4 (ferramentas) continuam dependendo so de o WordPress existir.

11/09/2026 — sessão de conversa: decisões do Raphael gravadas — artesã aparece com nome/foto/redes; botão Verificar disponibilidade + leads por e-mail; acesso do painel vai direto para a artesã.

11/09/2026 11:49Z — BLOCO 3b ENTREGUE: a casca da ilha (commitada e verificada; NAO esta no ar)

- `snippets/clubedomosaico-casca.php` v1.0.0, manifest na revisao 4 com `publicar: true` e
  `ativo: true`. Oito paginas criadas e mantidas por shortcode: inicio, loja, materiais,
  como-fazer, sobre, contato, divulgacao-de-afiliados e privacidade. Cabecalho e rodape pretos
  com o miolo branco, menu sanfona com aria-expanded/aria-controls, favicon proprio no lugar do
  icone do WordPress, JSON-LD Organization + WebSite em toda pagina, apelidos com 301 e a trava
  do sitemap 404.
  sha256 casca: `9b678bcffd00fc75261a6769d64777c2b6d1be1e3fb56e02398bd9d627753001`
- Ferramentas de bancada que nasceram junto, nenhuma publicada no site:
  `ferramentas/gerar-favicon.php`, `ferramentas/render-para-teste.php`,
  `ferramentas/teste-casca.php` e `ferramentas/teste-navegador-casca.mjs`.

- **O QUE ESTA CASCA TEM DE PROPRIO**, e que nao foi copiado de Aquametria nem de Robometria:
  (1) **a marca e uma imagem ENTREGUE, nao um desenho do snippet.** As duas primeiras ilhas
  desenham o simbolo em SVG dentro do codigo; aqui o logo foi feito por gente e o `PROMPT.md`
  proibe redesenhar, vetorizar ou escrever o nome ao lado do arquivo, que ja traz o wordmark. O
  teste reprova se aparecer um `<svg>` de logotipo ou se o nome for repetido em texto dentro do
  bloco da marca.
  (2) **tres motores, tres catalogos.** Loja, Guia e Escola nao cabem num catalogo de
  "ferramentas": a casca tem `cdm_casca_ferramentas()`, `cdm_casca_categorias_do_guia()` e
  `cdm_casca_tutoriais()`, e o cartao de categoria do Guia diz **quantos itens ela tem no banco**
  em vez de um "em breve" generico — e esse numero que separa promessa de trabalho feito.
  (3) **a Loja tem estado vazio honesto, e ele e testado nos DOIS estados.** O catalogo de pecas
  vive no CPT que a artesa alimenta (bloco 4d) e nunca no repositorio, entao hoje a Loja mostra
  "em breve, e sem peca de mentira ate la". O teste simula o CPT com duas pecas e exige que a
  vitrine apareca e o estado vazio suma — sem isso, uma vitrine que nunca mostra peca nenhuma
  passaria despercebida.
  (4) A casca nasce com a **trava do sitemap 404** que a Robometria so descobriu depois de
  publicar: ilha sem post publicado faz o `wp-sitemap.xml` sair com o XML certo e status 404.

- **VERIFICACAO** (secao 8): `php -l` limpo; `teste-casca.php` com **127 afirmacoes** e
  `teste-navegador-casca.mjs` com **33 medicoes** num Chromium de verdade — rolagem horizontal
  **0 px** em 360/390/781/782/783/1200 px nas oito paginas, o botao do menu aparecendo e sumindo
  na borda exata dos 782 px, contraste 21:1 no cabecalho e no rodape e 17,6:1 no corpo (formula da
  WCAG escrita dentro do proprio teste), e a **mesma pagina com o JavaScript DESLIGADO** servindo
  os quatro links do menu visiveis e o corpo inteiro, que e o que o crawler de IA recebe.

- **QUINZE MUTACOES DELIBERADAS, e o que elas custaram.** Treze reprovaram de primeira. **Duas
  passaram**, as duas na mesma trava — a de escassez inventada —, e reescreve-la duas vezes foi o
  trabalho mais util do bloco:
  1. A 1a versao procurava o termo no corpo inteiro com excecao para algumas negacoes escritas a
     mao. Reprovou a pagina Sobre, que diz com todas as letras que **nao** publica selo de mais
     vendido. Regua que reprova a frase certa.
  2. A 2a versao separava o corpo em frases e perdoava a frase com qualquer negacao. A mutacao
     "a ficha tecnica do silicone acetico mais vendido do Brasil lista ... entre as superficies em
     que o produto **nao** deve ser usado" **passou**: o "nao" da frase negava outra coisa.
     Perdoar por presenca de palavra e adivinhar.
  3. A 3a versao, que ficou: a pagina **declara no markup** qual bloco e recusa
     (`class="cdm-nao-fazemos"`), o teste retira esses blocos e proibe o termo em todo o resto. E
     para a declaracao nao virar porta dos fundos, exige que **todo bloco marcado ABRA negando** —
     porque a mutacao seguinte enfiou "Peca mais vendido, ultimas unidades!" dentro do bloco de
     recusa e passou enquanto a regra so pedia negacao em algum lugar dele.
- **A 2a versao, antes de ser reprovada, achou um defeito de verdade escrito pela propria
  Fundacao**: a home chamava o produto de "o silicone acetico **mais vendido** para construcao" —
  numero de venda que esta ilha nunca mediu e nao pode afirmar (secao 7). Corrigido para o nome do
  produto. E a trava de "a pagina medida tem tamanho de pagina" reprovou duas paginas finas demais
  para o indice de um dominio novo (como-fazer com 971 e contato com 1194 caracteres de corpo); as
  duas ganharam conteudo real, tirado do banco e nao de enchimento, e hoje tem 2.716 e 1.813.

- **O DESEMBARQUE NAO ACONTECEU, e isso nao e detalhe.** `curl` para
  `https://clubedomosaico.com.br/...` devolveu **000**, e o `$HTTPS_PROXY/__agentproxy/status`
  registrou `connect_rejected: gateway answered 403 to CONNECT` para
  `clubedomosaico.com.br:443` as 11h19Z. A secao 4 do contrato manda testar antes de presumir
  bloqueio — foi testado, duas vezes, e falhou. Entao **a casca esta no `main` e nao esta no ar**:
  o site continua servindo o tema padrao do WordPress. O item fica aberto e e de uma linha: acionar
  o Sync da ilha e conferir no `/status` que a revisao aplicada e a **4**. Quem tiver o dominio na
  rede Personalizada do ambiente faz isso em um minuto. "Aplicado com sucesso" nao foi dito aqui
  porque nao foi medido.

- 5 itens do banco esperando link de afiliado e 5 sem imagem — os mesmos cinco da categoria cola,
  inalterados: este bloco nao coletou dado nenhum, e nao devia.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos blocos
  1, 2 e 3. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 4 — a ferramenta F2** (seletor de cola e rejunte), que o
  esquema do bloco 3 ja deixou especificado com as 18 celulas recomputadas e as regras de
  elegibilidade executaveis. Ela agora tem casca para viver dentro, catalogo que a lista e pagina
  de divulgacao de afiliados ja publicada, que era o que faltava. Alternativa que nao depende de
  nada: as categorias REJUNTE e PASTILHA do banco.

11/09/2026 13:47Z — BLOCO 3c ENTREGUE: a categoria REJUNTE do banco, e os tres defeitos
que ela revelou (commitado e verificado; a ilha continua NAO estando no ar)

- `dados/materiais-rejuntes.json` com **5 rejuntes Quartzolit** — ceramicas, porcelanatos e
  ceramicas (BT 2024), acrilico, epoxi e piscinas —, mais a regua propria deles no esquema
  (`versao_esquema` 2) e `ferramentas/mutacoes-rejunte.py`. Manifest na revisao 5; a casca
  subiu para 1.1.0.
  sha256 rejuntes:  `ver manifest.json` (recalculado nesta execucao junto com esquema,
  constantes, especificacao, validador, teste-casca e casca)
- **Por que este bloco e nao a F2, que o registro anterior indicava.** A F2 se chama
  "seletor de cola E REJUNTE" e o banco tinha **zero** rejuntes: metade da resposta dela
  sairia cravada na prosa do snippet em vez de recomputada da declaracao, que e exatamente o
  que o esquema do bloco 3 existe para impedir. E o desembarque esta bloqueado por rede, entao
  um bloco publicavel nasceria sem poder ser conferido no ar (secao 8: nao se marca sucesso
  sem medir). O REGISTRO do 3b ja nomeava esta alternativa.

- **O QUE A CATEGORIA DESCOBRIU SOBRE O PROPRIO BANCO: rejunte nao e cola.** Na cola, a lista
  do fabricante nomeia a **base** — a superficie sobre a qual se cola. No rejunte, a mesma
  lista nomeia a **tessela** e o **ambiente**: "ceramicas, pastilhas de porcelana e de vidro"
  e o que vai ser rejuntado, nunca o vaso de cimento embaixo. Rejunte nao toca a base. Por
  isso a categoria ganhou `mapa_de_termos_do_rejunte` (que traduz para ambiente e tessela,
  nunca para base), `regras_de_elegibilidade_do_rejunte`, `perfis_esperados_do_rejunte` e
  `matriz_esperada_do_rejunte` — e a variavel que decide passou a ser a LARGURA DA JUNTA.
  Uma diferenca de regra que vale ser lida antes de discordar: o rejunte tem **tres** ambientes
  criticos e a cola tem dois, e o que entra e `interno_molhado`. Nao e inconsistencia, e
  geometria: a cola fica escondida atras da tessela e a agua chega nela por ultimo; o rejunte e
  a superficie exposta, a agua fica parada em cima dele e e nele que o mofo cresce.

- **DEFEITO 1 — latente, e medido antes de consertado.** `computar_celula()` varria TODOS os
  materiais do banco sem olhar categoria. As 18 celulas da F2 passavam so porque o banco so
  tinha cola: o primeiro rejunte gravado fez **as 18 falharem de uma vez**, cada uma acusando
  os cinco rejuntes como "eliminados por silencio" — frase sem sentido para um produto que
  nunca foi candidato a colar nada. O conserto tentador seria colar os cinco ids nas 18
  celulas do esquema: a matriz voltaria ao verde dizendo uma bobagem. O conserto certo foi
  declarar `categoria_considerada: cola` na matriz e conferir isso em codigo, com trava de
  regressao que reprova rejunte em qualquer lista da matriz da F2.

- **DEFEITO 2 — um numero FALSO que ja estava NO AR.** O cartao "Rejuntes" do Guia trazia
  `'no_banco' => 0` digitado a mao, no mesmo dia em que a categoria ganhou cinco produtos. O
  `teste-casca` nao viu porque conferia so a categoria **cola**, a unica que existia quando ele
  foi escrito — a mesma familia da cicatriz da secao 8 do contrato: regua que so mede a metade
  que ja existia. Casca **1.1.0**: `cdm_casca_numeros()` passa a contar o banco por categoria,
  e os totais de "esperando link" e "sem imagem" da ilha so assumem a via viva do Sync quando
  TODOS os bancos chegaram (somar metade das categorias daria um total menor e com cara de
  verdadeiro). O teste passa a cobrar as **seis** categorias e nos dois sentidos: categoria do
  Guia sem arquivo de banco mapeado reprova, e arquivo de banco sem cartao no Guia tambem —
  dado colhido que a tela nunca mostra e trabalho jogado fora.

- **DEFEITO 3 — de metodo, e apanhado no proprio ato.** Uma busca feita com o numero `1,55`
  escrito DENTRO da consulta devolveu `1,55` como se fosse declaracao do fabricante. Foi
  descartada: pergunta que carrega a resposta nao mede nada. Uma segunda, com pergunta limpa,
  generalizou o 1,75 do cimenticio sem citar documento do epoxi, e ainda inventou uma
  justificativa para o numero — tambem descartada. A pendencia `rejunte-CR-por-tipo` continua
  aberta e **virou limite declarado da ferramenta**, nao um "seria bom ter": dos cinco produtos,
  o acrilico e monocomponente pronto uso em pote de 1 kg e o epoxi e bicomponente fracionado, e
  o CR 1,75 sai de um exemplo de **po**. A coluna de rejunte da F1 passa a dizer na tela que
  vale para rejunte CIMENTICIO.

- **O ACHADO DE MAIOR VALOR E TAMBEM O QUE ELE NAO RESOLVE.** O *rejunte piscinas quartzolit*
  e o unico material do banco inteiro cujo fabricante nomeia **"pastilhas de porcelana e de
  vidro"** em uso submerso — a tessela do mosaico no ambiente mais critico do vocabulario. E
  mesmo assim ele NAO e recomendado em celula nenhuma, por dois motivos que a pagina diz com
  todas as letras: (1) a faixa de junta dele nao foi obtida — a unica mencao e de PROCEDIMENTO,
  "juntas com ate 3 mm devem ser molhadas antes", e ler 3 mm como maximo inverteria a frase do
  fabricante —, entao a regra 1 o mantem fora; e (2) o que ele declara e **agua TRATADA
  quimicamente**, que e piscina, e nao a agua parada de uma fonte ou de um vaso de jardim.
  O lado do rejunte ganhou resposta de verdade (o epoxi: junta de 1 a 5 mm, liberacao em 7
  dias, boletim 2018-01, nivel 2), mas **peca submersa precisa de cola tambem**, e a unica
  declaracao de colagem submersa da ilha continua sendo o press release do Durepoxi, nivel 4.
  A faixa fica declarada como descoberta. Meia resposta escrita como meia resposta ainda e a
  resposta mais util da pagina; meia resposta escrita como resposta inteira e o defeito.

- **VERIFICACAO** (secao 8): `php -l` limpo; `validar-banco.py` com 18 celulas de cola + 9 de
  rejunte + 5 perfis, todos conferidos contra o que esta escrito **A MAO** no esquema, escrito
  antes de rodar o validador; `teste-casca.php` com **137** afirmacoes (eram 127); 33 medicoes
  em Chromium de verdade, 0 px de rolagem em 360/390/781/782/783/1200 px nas oito paginas, com
  a trava 0 confirmando que as paginas medidas tem tamanho de pagina (corpo de 1.557 a 5.915
  caracteres).
- **QUATORZE MUTACOES DELIBERADAS, todas reprovadas.** Doze em `mutacoes-rejunte.py` (junta com
  1 mm a mais, faixa pela metade, faixa invertida, faixa inventada para o rejunte piscinas,
  epoxi perdendo a piscina, ambiente generico cobrindo sol e chuva, grade deixando de pisar na
  borda de 4 mm, rejunte voltando a entrar na matriz da cola, fonte de blog sustentando
  recomendacao, rejunte sem perfil escrito, cabecalho mentindo sobre itens esperando link) mais
  duas na casca (o zero cravado de volta no cartao, e categoria do Guia sem arquivo mapeado).
  **A que mais vale e a decima segunda:** ela tira a declaracao do banco E ajusta o perfil
  esperado no esquema junto, que e como um editor de verdade mexeria nas duas metades — as duas
  passam a errar juntas e a conferencia de perfil deixa de ver. Quem viu foi a **matriz**, que
  continuava esperando o epoxi no topo da celula de 3 mm submersa. E a prova de que a matriz
  nao e enfeite da conferencia de perfil, e a resposta local a cicatriz da secao 8.
- A grade da matriz do rejunte pisa **exatamente** em 1, 2, 4, 5 e 10 mm — os extremos
  declarados pelos cinco produtos — e em 6 e 11, logo depois do ultimo. Grade de passo fixo nao
  separaria "ate 4" de "ate 5", e o validador reprova se alguem tirar uma borda da grade.

- **10 itens esperando link de afiliado e 10 sem imagem**: os 5 de cola, inalterados, mais os 5
  de rejunte. Geracao de link e da Sentinela estrategica, no navegador, nunca da Fundacao.
- **O DESEMBARQUE CONTINUA NAO ACONTECENDO, e agora sao DUAS revisoes presas (4 e 5).** `curl`
  para o Sync e para o `/status` devolveu **000** as 13h46Z, e o `$HTTPS_PROXY/__agentproxy/status`
  registrou `connect_rejected: gateway answered 403 to CONNECT` para `clubedomosaico.com.br:443`.
  **A medicao que aponta a causa, e que nao existia no registro de 11h49Z:** na mesma execucao,
  `aquametria.com.br` e `robometria.com.br` responderam **200**. Nao e a nuvem que nao alcanca
  site nenhum — e o dominio da ilha 3 que nunca entrou na lista Personalizada do ambiente, que
  foi montada quando so existiam duas ilhas. E conserto de um minuto, do Raphael, no seletor de
  ambiente. Nao foi marcado em `bloqueada_por` de proposito: a ilha tem trabalho de sobra que
  nao depende do site, e marca-la bloqueada a tiraria da fila.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos blocos
  1, 2, 3 e 3b. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 4 — a ferramenta F2**, que agora tem as DUAS metades no
  banco e ganhou uma entrada nova, escrita no esquema e na especificacao: a **largura da junta em
  milimetros** ("quanto espaco voce deixa entre uma pastilha e outra?"), sem a qual nao ha como
  escolher rejunte. Alternativa que nao depende de rede nem de site: as categorias **PASTILHA** e
  **ALICATE** — mas atencao, a PASTILHA e de outra natureza, porque os campos que ela exige (passo
  de fabrica, espessura, peso unitario, unidade de venda) nao existem em boletim de fabricante e
  sim em anuncio de loja, nivel 5 e 6 da escada, e nenhum desses dominios foi testado ainda.

11/09/2026 17:55Z — DESPACHO DO RAPHAEL CUMPRIDO E CONFERIDO NO AR: cabeçalho claro, a voz da ilha, e a home que deixou de ser manifesto (casca 1.2.0, manifest na revisão 6, `/status` conferido)

- **A reclamação era uma coisa só, não duas.** *"Muito ruim o fundo preto no
  header, o logo sumiu, queria algo mais clean."* O logo sumia porque o arquivo
  entregue tem **fundo preto** com wordmark vinho — e o cabeçalho era preto
  porque era a única cor em que aquele arquivo aparecia. Trocar só o fundo
  faria o logo virar um retângulo escuro em cima do branco; trocar só o logo
  deixaria o bloco preto que ele reprovou. Os dois saem juntos ou nenhum sai.
- **O cabeçalho:** papel `#FFFFFF` com linha de 1 px em `#E9DCD7` (a linha da
  seção 6 do contrato, no lugar de sombra), menu em `#1F1715` peso 500 com
  passagem em coral, painel do menu sanfona também claro, `theme-color` branco.
  Medido **no navegador**, não no texto do CSS: `rgb(255, 255, 255)` de fundo e
  `rgb(31, 23, 21)` no menu, nas nove páginas. A paleta **não** ganhou cor nova:
  o despacho sugeria `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A`, e os quatro são
  vizinhos de um a quatro passos dos tokens já aprovados em 10/09. Um segundo
  coral a quatro unidades do primeiro é defeito, não identidade — então valeram
  papel, traço, tinta e coral da ilha. Se o Raphael quiser exatamente aqueles
  hexadecimais, é uma linha.
- **A marca virou o wordmark "clube do mosaico" em TEXTO**, na tipografia da
  identidade (Outfit 600, vinho, minúsculas de verdade e não `text-transform`,
  para quem usa leitor de tela ouvir o nome como ele é escrito). Contraste
  medido no navegador: 17,62:1 do menu e 12,97:1 do wordmark sobre o cabeçalho.
- **O ACHADO QUE NÃO ESTAVA SENDO PROCURADO, e que muda o desenho:**
  `identidade/logo/lotus-512.png` — o símbolo transparente que o despacho manda
  usar no cabeçalho claro — está **TRUNCADO no repositório**. O chunk `IDAT`
  declara 11.638 bytes num arquivo que tem 8.770, com um `IEND` colado no fim.
  Não é imagem cortada pela metade: tentei recuperar o pedaço que existisse e o
  `zlib` recusa o **primeiro** bloco ("invalid code lengths set"), então não sai
  um único pixel. Publicá-lo teria trocado o logo sumido por um ícone de imagem
  quebrada, que é pior porque parece descuido em vez de obra em andamento. A
  metade que existe do par foi ao ar; a lótus fica pendente com o Raphael.
  `ferramentas/gerar-marca.php` nasceu para embuti-la e **recusa** arquivo que
  não abre — confere chunk a chunk, cobra canal alfa e cantos transparentes, e
  sai com código 1 sem tocar no snippet. Rodada hoje: recusou, com o número de
  bytes que faltam na mensagem.
- **A HOME (molde LOJA do `VOZ.md`, seção 15 do contrato).** Abria com três
  parágrafos de método, e o terceiro era a ficha técnica de um silicone com
  código de documento e lista de superfícies proibidas. **Duas dessas frases
  estão literalmente na lista de "Proibidas" do `VOZ.md`** — não é coincidência:
  a lista foi escrita para proibir aquele texto. Agora a home abre por "Mosaico
  feito à mão, uma peça por vez", segue com a vitrine (estado vazio honesto,
  reescrito curto), o bloco "Vai fazer o seu? A gente ajuda a escolher o
  material" e a artesã fechando a página. O número e a fonte **não sumiram do
  site**: mudaram de lugar.
- **A home deixou de se chamar "Início"** — e o defeito por trás disso é que
  valia mais: `garantir_paginas()` nunca sincronizava título, então a página
  nascia com o título da definição e ficava com ele para sempre. Era assim que
  "Início" sobrevivia às versões da casca. Agora sincroniza, **sem tocar em
  `post_name`** (seção 12.1: URL publicada não se move). De quebra, a casca
  passou a gravar `blogname` e `blogdescription` como já gravava
  `page_on_front`: o `<title>` da home no resultado de busca agora diz "Clube do
  Mosaico – Mosaico feito à mão, uma peça por vez", que é a mesma frase da
  página e do rodapé. É a lição da Aquametria de 11/09 aplicada antes de doer.
- **O GUIA perdeu sete seções de bastidor**, que não foram jogadas fora: mudaram
  para **`/materiais/como-sabemos/`**, primeira página de nível 2 desta ilha
  (seção 16), com mãe declarada, `noindex` e fora do sitemap. Ela ficou com
  4.340 caracteres de corpo — não é página fina. No Guia ficaram as seis
  prateleiras, com os resumos reescritos na voz, e o único achado que muda a mão
  de quem faz: silicone acético não serve em espelho nem em cimento, e o neutro
  do mesmo fabricante serve.
- **"Hoje 10 dos 5 itens esperam link" SAIU DO AR.** Os dois números estavam
  certos sozinhos — 10 itens esperando link no banco inteiro, 5 adesivos na
  categoria cola — e a frase que os juntou era impossível. Foi exatamente por
  isso que nenhum teste viu: cada metade era conferida separada. O denominador
  passou a ser `itens_no_banco`, somado das categorias, e a página de
  divulgação parou de **afirmar por escrito** que não há link nenhum: agora é a
  subtração entre o que existe e o que espera.

**VERIFICAÇÃO — 198 afirmações na bancada (eram 137), 54 medições em Chromium, 19 mutações, e a conferência no ar.**

- **A bancada estava medindo oito das nove páginas pela metade, e ninguém
  sabia.** A trava nova de "página inteira" reprovou de primeira: o rodapé saía
  só na primeira página. A causa é um `static` legítimo em
  `cdm_casca_rodape_impresso()` (e outro em `cdm_casca_marca_html()`), que
  existe para o rodapé não sair duas vezes na MESMA página — no site um processo
  é uma requisição e ele está certo. Numa varredura de nove páginas em
  sequência, ele faz o rodapé aparecer na primeira e sumir nas oito seguintes,
  **sem erro nenhum**. É a terceira vez que o Arquipélago paga por isso, e a
  regra do contrato já estava escrita: varredura de muitos estados roda **um
  processo por estado**. O teste passou a fazer isso. E a conferência de "página
  inteira" deixou de ser um número redondo de bytes (que eu não consigo calibrar
  sem o site no ar, e número redondo não é critério) e virou a lista do que uma
  página desta ilha obrigatoriamente carrega: folha, JSON-LD, menu, comando do
  menu, favicon, rodapé e H1.
- **19 mutações deliberadas em `ferramentas/mutacoes-voz-e-cabeca.py`, 19
  reprovadas — mas DUAS passaram na primeira rodada**, e são o resultado do
  teste:
  1. *"o título para de sincronizar"* passou porque a bancada monta o H1 a
     partir da **definição**, e a definição está certa. O defeito mora no outro
     lado, no caminho que atualiza a página que já existe — e medir o H1 servido
     nunca poderia vê-lo. Trava nova: o teste simula o site real de hoje (as
     páginas existem, com os títulos velhos) e afirma sobre o que a casca **manda
     gravar**, inclusive que nenhuma gravação toca `post_name` e que página que
     não é da casca não tem o título reescrito.
  2. *"noindex na página errada"* passou porque o teste conferia que a etiqueta
     sai nas páginas **declaradas** — o que é verdade mesmo quando alguém declara
     a página errada. Conferir a declaração contra ela mesma é a mesma forma do
     teste que mede a si mesmo. Régua nova, vinda de fora: só a página de camada
     de prova pode sair do índice, e nenhuma página do menu pode.
- **As duas mutações que mais valem são as portas dos fundos do portão de voz**,
  e as duas reprovam: embrulhar o Guia inteiro na classe que declara camada de
  prova, e declarar uma **segunda** página como página de prova. Sem contar os
  blocos, medir onde eles começam e exigir que a página de prova seja uma só, o
  portão se desligaria com uma linha e nenhuma palavra mudaria na tela — que é
  exatamente a porta que a Aquametria achou ao tentar quebrar o próprio portão.
- **NO AR às 17h55Z:** `/status` com revisão 6, igual à do manifest. 9 de 9 URLs
  em 200, a nova inclusive. Zero `&#038;` dentro de `<script>` nas nove
  (contado só dentro dos blocos de script). Um rodapé por página. O `H1` da home
  é a frase da voz e nenhuma das três frases proibidas aparece no corpo dela. O
  Guia diz "10 itens de fabricante" e não diz "10 dos 5". `/materiais/como-sabemos/`
  serve `noindex` e **está fora** do `wp-sitemap-posts-page-1.xml`, enquanto
  `/materiais/` continua dentro — as duas direções medidas.
- **A REDE ALCANÇA ESTA ILHA, e o bloqueio anterior era diagnóstico não
  reconferido.** O `ESTADO.md` dizia "403 ao CONNECT para clubedomosaico.com.br,
  segunda execução seguida" e duas revisões presas. Nesta execução o primeiro
  `curl` à home devolveu `000` — e **o mesmo comando, repetido minutos depois,
  devolveu 200**, assim como o Sync, o `/status`, as nove páginas e o sitemap. A
  falha era intermitente, não bloqueio. A lição fica escrita: bloqueio que não é
  reconferido a cada execução vira permanente sozinho, e prendeu duas revisões
  desta ilha por duas execuções.

**10 dos 10 itens do banco ainda esperam link de afiliado; 10 sem imagem.** Este
bloco não tocou catálogo.

**Próximo passo:** a árvore da seção 16 inteira — `ARVORE.md` da ilha, mãe para
toda página existente, breadcrumb com `BreadcrumbList` e blocos "Veja também"
(16.4). `/materiais/como-sabemos/` já nasceu dentro dela e serve de primeiro
caso. Nenhuma categoria de nível 2 do Guia tem as 3 filhas que a 16.5 exige,
então nenhuma nasce agora. Depois disso, o bloco 4 (a ferramenta F2).

---

## 11/09/2026 19h40Z — A ÁRVORE DA SEÇÃO 16, e nenhuma URL se moveu

Casca **1.3.0**, manifest na **revisão 7**. Bloco nomeado como próximo passo pela
execução das 17h55Z e pelo despacho do Raphael de 11/09, cuja última linha dizia
que a árvore era o bloco seguinte.

**O que foi entregue**

- **`ARVORE.md`** (item i do 16.8): os três níveis com slug, onde mora cada uma
  das nove páginas que existem, o que está travado e por quê. É o mapa que os
  blocos seguintes seguem — e o teste lê este arquivo para cobrar que documento e
  código digam a mesma coisa, porque duas metades mantidas à mão em lugares
  diferentes divergem em silêncio.
- **Trilha (16.3)** em oito das nove páginas; a home não tem, que é o que a regra
  manda. Ela nasce entre o cabeçalho e o H1, pelo filtro do bloco
  `core/post-title`, com cinto de segurança no `the_content` para o caso de a
  página não ter aquele bloco.
- **`BreadcrumbList`** em JSON-LD nas mesmas oito.
- **Cluster "Veja também" (16.4c)** nas três seções de nível 1, cada uma listando
  as outras duas: é o ciclo LOJA → GUIA → ESCOLA, que é a razão de esta ilha ter
  três motores num domínio só.

**ESTA ILHA NASCEU COM A ÁRVORE CERTA E NÃO SABIA.** Nenhuma página mudou de
endereço neste bloco, e nenhuma precisou: as três seções já eram nível 1, a única
página de nível 2 já nascera com mãe em 1.2.0, e as quatro da raiz são exatamente
as que a 16.1 admite ali. Por isso **não há um 301 sequer e o sitemap não muda** —
o que faltava era a árvore ficar **visível** (trilha, schema, cluster), que é o
que a 16.3 e a 16.4 pedem. Nas outras duas ilhas o nível 1 ainda é página
inexistente e a trilha sai com degrau em texto; aqui os três degraus de topo são
link de verdade desde o primeiro dia.

**AS DUAS COISAS ERRADAS QUE ESTE BLOCO ACHOU SEM PROCURAR**

1. **O registro do Guia e o `VOZ.md` discordavam nos slugs de duas categorias**
   desde que a casca nasceu: o código dizia `materiais/colas` e `materiais/alicates`,
   o `VOZ.md` dizia `colas-e-adesivos` e `alicates-e-corte`. Nada no repositório
   cobrava os dois juntos, e a divergência só apareceria no dia em que a página
   nascesse — quando já seria URL publicada, que não se move. **O dia de acertar
   é o dia ANTES de a página existir.** Corrigido para o nome do `VOZ.md`, que é
   quem manda no nome do nível (seção 15.1), e agora há trava: todo slug de
   categoria do Guia tem que ser um nome escrito no `VOZ.md`.
2. **O cartão da categoria que ainda não abre publicava contagem de banco** —
   "5 no banco, ficha em construção". O número era certo e era contado do arquivo;
   o problema é outro, e a 16.5 o nomeia: cartão que não é link diz "em breve",
   **sem contagem**. É promessa com número colada num lugar que não se pode
   visitar. O número não sumiu do site: continua na camada de prova do Guia e na
   página Como sabemos (15.2), contado, que é onde quem quer conferir confere.
   O campo `no_banco` continua existindo e continua sendo cobrado contra o
   arquivo — o que mudou foi ele deixar de ir para a TELA daquele cartão.

**O SCHEMA PUBLICA MENOS DO QUE A TRILHA MOSTRA, de propósito.** Um `ListItem`
intermediário sem `item` invalida o `BreadcrumbList` inteiro para o Google, e
lista inválida é lista ignorada — então o schema "mais completo", que levaria
também o degrau sem página, publicaria MENOS com cara de publicar mais. Hoje isso
não corta nada nesta ilha, porque os três degraus de nível 1 existem: a via foi
escrita para o dia em que a primeira ficha de material nascer antes da categoria
dela, que é o estado normal das outras duas ilhas.

**A BANCADA ESTAVA MEDINDO FORA DE ORDEM, e a própria trava pegou.** A primeira
versão do render rodava `the_content` **antes** do bloco de título. No site a
ordem é a inversa — o `core/post-title` renderiza primeiro —, e por isso a trilha
nasce acima do H1. Na bancada invertida o cinto de segurança de prioridade 9
disparava, a trilha caía dentro do corpo, e **oito páginas foram reprovadas por
um defeito que só existia na bancada**. Quarta vez que o Arquipélago paga por
render que serve diferente do site; desta vez a conta veio em minutos porque a
trava media a POSIÇÃO da trilha, não a presença dela.

**AS DUAS MUTAÇÕES QUE PASSARAM, E POR QUE ELAS VALIAM MAIS QUE AS DEZESSETE QUE
REPROVARAM.** `ferramentas/mutacoes-arvore.py` quebra a árvore de propósito, uma
mutação por vez. Na primeira rodada, 17 de 19 reprovaram — e as duas que passaram
não passaram por a trava ser fraca: passaram por serem **inertes**.

- *"degrau de trilha vira link morto"* trocava o `<span>` do degrau sem página por
  um `<a>`. Só que **nenhuma página desta ilha tem degrau sem página hoje**, então
  o ramo nunca é executado e o site servido é byte a byte o mesmo.
- *"cluster publicado com uma irmã só"* baixava o piso de 2 para 1 irmã. Só que
  nenhuma página desta ilha tem **exatamente uma** irmã no ar — elas têm zero ou
  duas.

É a cicatriz da grade que não pisa na borda, com a borda faltando no **mundo** e
não no teste. A saída foi a mesma do modo `todas` do render: **a bancada fabrica
a borda**, aqui pelo filtro `cdm_arvore`, que é o mesmo por onde uma página nova
entrará no mapa de verdade. As duas situações fabricadas são as duas que esta
ilha vai ter — a ficha nascendo antes da categoria, e uma categoria com uma irmã
só. Com elas, as 19 de 19 reprovam.

**VERIFICAÇÃO em bancada:** `teste-casca.php` com **327 afirmações** (eram 198),
um processo por página; `php -l` limpo nos dois snippets; `validar-banco.py`
aprovado; `mutacoes-arvore.py` 19 de 19 reprovadas; `mutacoes-voz-e-cabeca.py`
19 de 19 e `mutacoes-rejunte.py` 12 de 12 continuam reprovando (nada deste bloco
afrouxou trava anterior).

**NO AR às 19h40Z:** Sync acionado por `curl`, `/status` com **revisão 7**, igual
à do manifest. **9 de 9 URLs em 200** e **117 afirmações medidas no HTML
SERVIDO**, sem uma falha:

- zero `&#038;` dentro de `<script>` nas nove (contado só dentro dos blocos de
  script, 7 na home e 8 nas outras);
- trilha em 8 de 9, sempre **antes do H1** e **uma só por página**; a home não
  tem, e também não publica `BreadcrumbList`;
- nenhum degrau aponta para página inexistente; a trilha de
  `/materiais/como-sabemos/` tem os três degraus e o do meio **linka** a mãe;
- `BreadcrumbList` nas oito, todo `ListItem` com `item`, posições de 1 a n sem
  buraco, e a relação que importa conferida uma a uma: **os itens do schema são
  os degraus linkados da trilha mais a página atual**;
- "Veja também" em 3 de 9 — exatamente as três seções, com 2 irmãs cada, nenhuma
  irmã morta e nenhuma página se listando como irmã de si mesma;
- os **6 cartões** de categoria do Guia servem "Em breve", **sem um dígito** e
  **sem serem link** (16.5), enquanto a camada de prova continua publicando 5
  colas e 5 rejuntes contados do banco;
- o `wp-sitemap-posts-page-1.xml` continua com as mesmas 8 URLs, e
  `/materiais/como-sabemos/` continua fora dele.

**10 dos 10 itens do banco ainda esperam link de afiliado; 10 sem imagem.** Este
bloco não tocou catálogo. Da pauta da seção 17: **nenhum tema escrito, nenhum na
fila, nenhum recusado** — `pauta.md` ainda não existe nesta pasta.

**Próximo passo:** o **bloco 4 — a ferramenta F2** ("qual cola e qual rejunte
para a sua peça"), que é a primeira página de nível 3 desta ilha e o primeiro
caso real do degrau de trilha sem página, já coberto pela borda fabricada na
bancada. Ela nasce com o bloco de compra da seção 7 junto, mesmo com
`afiliado.url` vazio, e com a mãe `/materiais/` declarada no `ARVORE.md`. Só
depois dela uma categoria de nível 2 chega perto das 3 filhas que a 16.5 exige.

---

## 11/09/2026, 20h35Z — O LOGO DELE, INTEIRO, NO CABEÇALHO (despacho do Raphael de 11/09 (2), cumprido inteiro)

**Casca 1.4.0, manifest na revisão 8, `/status` com revisão 8.** Despacho de
prioridade máxima, e a seção 18.2 manda ele sair inteiro: os **cinco itens**
saíram nesta execução, não um por passada.

**O que o cabeçalho serve agora:** `logo-clube-do-mosaico.png` em `<img>` de
52 px de altura, com link para a home e **nenhuma letra ao lado**. O nome está
desenhado dentro da imagem; escrevê-lo de novo seria a marca em dobro na tela e
anunciada duas vezes por leitor de tela. Por isso não existe `<span>` nenhum ali
e quem carrega o nome para quem não vê a imagem é o `alt`. A barra do cabeçalho
subiu de 72 para 84 px, e abaixo de 600 px o logo desce para 44 px — com 52, ele
e o botão do menu não cabem na mesma linha a 360 px.

### A afirmação que sustentava a versão anterior estava errada

Estava escrita em **três lugares do snippet e um do `VOZ.md`** desde 1.2.0: *"o
arquivo entregue tem fundo preto"*. **Não tem** — é transparente, e o Raphael
conferiu na biblioteca de mídia. O logo sumiu em 1.1.0 porque o **cabeçalho** era
preto e o wordmark dentro do arquivo é vinho `#69030C`: defeito de **onde o logo
foi posto**, nunca do arquivo. A 1.2.0 consertou a causa — clareou o cabeçalho —
e, pela leitura errada do sintoma, tirou junto o logo, que era a parte certa.

Fica escrito porque a forma se repete: **sintoma não é causa, e um diagnóstico
escrito com ar de fato se propaga por versões**. É o mesmo desenho do `000` lido
como bloqueio de rede na semana passada, que prendeu duas revisões desta ilha por
dois dias até alguém repetir o comando.

### 1,26 MB num espaço de 78 px — e por que isso não é "processar o logo"

O arquivo dele é o original de 1536×1024 e a marca ocupa 78×52 px na tela.
Servi-lo cru seria 1,26 MB em toda página de um domínio recém-nascido, e
orçamento de rastreamento é a primeira coisa que o Google mede num domínio assim.
**Não se redesenha nem se gera nada** — o `PROMPT.md` proíbe, e tem razão: o
`src` continua sendo a URL exata que o despacho mandou usar, e o `srcset` oferece
as reduções que o **próprio WordPress** gerou do upload dele (`-300x200` com
41 KB, `-768x512` com 175 KB), com `sizes="78px"`. Mesma imagem, mesmo recorte,
mesma origem; quem ignorar o `srcset` baixa o original e vê a mesma coisa. Medido
no navegador: a escolhida foi a de 41 KB.

### As mutações, que é onde o teste vira teste

Seis novas, e a antiga **"logo de fundo preto volta ao cabeçalho claro" foi
aposentada**: ela media o mundo ao contrário — lá o defeito era o logo *entrar*,
aqui é ele *sair*. Mutação que edita a regra antiga vira **inerte** quando a
regra muda de lado, e inerte é verde sem medir nada.

**Duas passaram na primeira rodada, pelo mesmo motivo de sempre:** não acharam o
alvo, porque as linhas do `<img>` foram escritas na mutação sem as duas
tabulações que o arquivo tem. Mutação que não consegue ser escrita é verde que
não mediu nada. Reescritas, as duas morderam: `0x0` de medida declarada e `alt`
vazio.

**A que mais vale da leva é a porta dos fundos do `srcset`:** o `src` fica certo
no código e outra imagem entra no lugar do logo por um atributo que ninguém lê. O
portão passou a cobrar que **todo candidato seja o mesmo arquivo com sufixo de
tamanho**.

### Verificação

Bancada: `teste-casca.php` de **327 para 347 afirmações**, um processo por página
— o `static` de `cdm_casca_marca_html()` é exatamente o mecanismo que faria o logo
sair na home e sumir nas outras oito numa bancada de um processo só, e agora há
uma afirmação por página cobrando isso. `mutacoes-voz-e-cabeca.py` de 19 para
**24 mutações, 24 reprovadas**; `mutacoes-arvore.py` 19/19 e `mutacoes-rejunte.py`
12/12 seguem reprovando; `validar-banco.py` aprovado; `php -l` limpo. **63
medições em Chromium** nas nove páginas em 360/390/781/782/783/1200 com 0 px de
rolagem, incluindo a caixa de **78×52 px desenhada pelo motor de layout** — que é
a diferença entre "a regra de 52 px está escrita no CSS" e "o logo tem 52 px na
tela".

**No ar, às 20h35Z: 9 de 9 URLs em 200 e 102 afirmações medidas no HTML
SERVIDO**, nenhuma falha, por `ferramentas/conferir-no-ar.py`, que nasceu nesta
execução. Ele tem **régua própria**: a URL do logo e a medida 78×52 estão
literais dentro dele, copiadas do despacho, não lidas da constante da casca —
senão as duas metades errariam juntas. Mediu, em cada uma das nove: o `src` é o
arquivo dele, zero texto dentro da marca, `alt` com o nome, medida declarada, o
logo uma vez só, o wordmark em texto de 1.2.0 fora da página, zero `&#038;`
dentro de `<script>`, a folha servida mandando 52 px e o cabeçalho ainda claro.
As três URLs da imagem respondem PNG.

**O critério de pronto que ele escreveu era de olho, e foi conferido de olho:** a
home **servida** foi desenhada em Chromium com os bytes reais da imagem, e o logo
foi ampliado pixel a pixel. A lótus e o nome "clube do mosaico" embaixo, nítidos
sobre o branco, sem texto duplicado ao lado.

### Duas coisas registradas para ele poder discordar

1. **A 52 px o wordmark dentro do logo fica com ~8 px por linha.** Lê-se como
   logotipo, mas é pequeno — o arquivo é um lockup empilhado e 52 px é o número
   do próprio despacho. Os dois caminhos (subir para ~64 px, ou uma versão
   horizontal do lockup) são escolha dele, não da Fundação.
2. **Os hexadecimais sugeridos no despacho continuam fora**, como em 11/09:
   `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A` são vizinhos de um a quatro passos
   dos tokens que ele aprovou em 10/09. Um segundo branco a quatro unidades do
   primeiro é defeito, não identidade. Se ele quiser exatamente aqueles valores,
   é uma linha.

**10 dos 10 itens do banco seguem esperando link de afiliado; 10 sem imagem.**
Este bloco não tocou catálogo. Da pauta da seção 17: **nenhum tema escrito,
nenhum na fila, nenhum recusado** — `pauta.md` ainda não existe nesta pasta.

**Próximo passo:** o **bloco 4 — a ferramenta F2**, primeira página de nível 3
desta ilha e o primeiro caso real do degrau de trilha sem página, já coberto pela
borda fabricada na bancada. Nasce com o bloco de compra da seção 7 junto, mesmo
com `afiliado.url` vazio, e com a mãe `/materiais/` declarada no `ARVORE.md`.

## 11/09/2026, 22h05Z — BLOCO 4: A F2 NO AR, a primeira ferramenta da ilha

**Entregue:** `/materiais/qual-cola-usar-no-mosaico/` — snippet
`clubedomosaico-f2.php` v1.0.0, casca 1.5.0, manifest na revisão 9,
`/status` com revisão 9. Primeira ferramenta do Clube do Mosaico e
primeira página de **nível 3** da ilha.

### A decisão que decide todas as outras: a resposta é servida pelo SERVIDOR

O formulário é um `GET` para a própria página e o PHP monta a resposta.
**Não existe uma linha de decisão em JavaScript** — o script do rodapé só
evita o recarregamento quando a pessoa troca uma opção, e a página funciona
inteira sem ele. Duas coisas saem de graça dessa escolha, e as duas são
cicatriz do Arquipélago:

1. **Todo estado da entrada é HTML servido de verdade.** A seção 5 do contrato
   diz que ferramenta que calcula no navegador mostra a um modelo de linguagem
   um formulário vazio; aqui qualquer uma das 45 combinações de base × ambiente
   é uma página com a resposta escrita nela.
2. **Não há régua duplicada entre PHP e JS para as duas se separarem em
   silêncio.** Era o caminho mais curto para o defeito clássico de duas metades
   que erram juntas — ou pior, separado.

O preço é URL com parâmetro, e ele é pago na mesma linha: estado com parâmetro
sai com `noindex, follow` e `canonical` para o endereço limpo. Quem entra no
índice é a página-âncora, uma só, e ela carrega as duas tabelas inteiras
(seções 14.1 e 14.4).

### A elegibilidade é recomputada, nunca digitada

As cinco regras da cola e as quatro do rejunte estão em
`dados/esquema-banco.json` e agora têm **duas implementações independentes**:
`ferramentas/validar-banco.py` em Python e o snippet em PHP. As duas são
conferidas contra as matrizes escritas **à mão** no bloco 3 — 18 células de
base × ambiente e 9 de folga × ambiente. A categoria continua sendo parte da
pergunta: a régua da cola decide sobre **base**, a do rejunte sobre **largura
de junta**, e rejunte não toca a base.

### O QUE O RENDER MOSTROU NO PRIMEIRO SEGUNDO, e que nenhum teste procurava

A primeira página montada na bancada dizia **"Silicone Acetico Construcao"** e
**"o fabricante declara ceramica e azulejo"**. O banco inteiro estava sem
acento — 122 strings de tela, escritas assim desde o bloco 2, porque foram
digitadas a partir de busca e porque **até aqui nenhuma página as servia**. No
dia em que uma página passou a servi-las, o defeito virou texto no ar. É a
mesma coisa que a Robometria pagou em 11/09/2026, com 121 strings.

`ferramentas/restaurar-acentos.py` devolveu os acentos em **68 trocas**, e a
operação é **provada diacrítico-only**: reduzidos a sem-diacrítico, os dois
arquivos do banco depois dela são byte a byte iguais aos de antes — com cinco
exceções **declaradas e conferidas uma a uma**, que são os `nome_comercial` dos
rejuntes, escritos em caixa baixa ("rejunte acrilico quartzolit") e promovidos
a nome próprio. A ferramenta imprime cada troca que faz: espelho que não
imprime o que trocou envelhece calado.

De quebra, a tela dizia **"Quartzolit Rejunte Cerâmicas Quartzolit"** — os
cinco rejuntes têm a marca dentro do nome comercial e as cinco colas não.

### A VARREDURA ACHOU UM ESTADO QUE A FERRAMENTA NÃO ACEITAVA

A grade conferida do rejunte pisa em **11 mm** de propósito: é o primeiro valor
depois do maior extremo que algum fabricante declara. O campo do formulário
parava em 10, então quem tem folga de 11 caía **calado** no padrão de 2 mm e
recebia uma resposta que não era a dele. O campo foi para 12 mm e o estado
passou a responder a verdade: nenhum rejunte do banco cobre essa folga.

### As quatro mutações que passaram, e os três buracos que elas abriram

`ferramentas/mutacoes-f2.py` nasceu com 20 mutações e, na primeira rodada,
**quatro passaram**. Nenhuma passou por a trava ser frouxa — as quatro passaram
por a trava medir o lugar errado:

1. **A lista do silêncio nunca era conferida.** A mutação que fazia a matriz da
   cola varrer o banco inteiro punha os cinco rejuntes na decisão de *colagem*
   como "eliminados por silêncio" — frase sem sentido — e o teste só olhava o
   topo e os proibidos. Agora a lista é cobrada **nos dois sentidos**: o que
   falta e o que sobra.
2. **O rejunte só era medido na FRASE, e a frase só nomeia o topo.** Duas
   mutações de faixa de junta punham o produto indevido como elegível *abaixo*
   do topo, onde ele aparece no cartão e não na frase. Recomendar em segundo
   lugar o que o fabricante não declara é recomendar.
3. **Marca em dobro não aparece em teste de conter.** "Rejunte Cerâmicas
   Quartzolit" está *dentro* de "Quartzolit Rejunte Cerâmicas Quartzolit", então
   procurar por conter aprova o nome errado que engloba o certo. A régua passou
   a ser de igualdade, e direta: para todo produto cujo nome já carrega a marca,
   a composição "&lt;marca&gt; &lt;nome&gt;" não pode existir em lugar nenhum do corpo.

E uma quinta, que é a lição mais fina do bloco: **a mutação da faixa pela
metade era INERTE**, e não por não achar o alvo. Ela trocava um `||` por `&&` e
completava as pontas que faltavam — só que o único produto sem faixa tem as
**duas** pontas nulas, então a guarda trocada continuava pegando nele e nada
mudava na tela. Mutação que acha o alvo e mesmo assim não muda o que o site
serve é verde sem medir nada, e é mais difícil de ver que a mutação que não
acha o alvo. Reescrita, ela morde.

### Dois defeitos de régua na bancada que existia

- **`[a-z_]+` não casa com `cdm_f2`.** O `teste-casca.php` mapeava shortcode →
  caminho com essa expressão, e o dígito fazia falta: a página da primeira
  ferramenta da ilha entrava na tabela com caminho **vazio**, e a trilha dela, o
  `BreadcrumbList` dela e o cluster dela passavam a ser medidos contra o nada.
  Régua estreita demais não é régua frouxa: é régua que mede outra coisa.
- **O portão da 16.5 media o cartão errado.** "Cartão de categoria não vira link
  enquanto a categoria não existir" contava TODO cartão do corpo, e no dia em
  que a primeira ferramenta virou link ele reprovou a home e o Guia por um
  cartão que está certo. As duas listagens ganharam classe própria.

### O que a página diz que não sabe

Duas faixas continuam **declaradas** como descobertas, em vez de preenchidas no
chute: **base de plástico** e **peça em contato permanente com água**. E a
página passou a separar uma coisa que não é a mesma: *declaração vaga não é
silêncio*. Dizer "o fabricante não fala" de um produto cujo fabricante escreveu
"certos tipos de plástico" seria falso — ele falou, e falou de um jeito que não
decide. As duas saem em parágrafos diferentes, com a frase dele.

O tempo de espera do PVA também virou texto: o campo existe no banco com o
motivo escrito, e a página diz que não publica o número em vez de simplesmente
não ter a seção. Ausência de seção é indistinguível de "não importa".

### Duas mudanças pequenas na casca, e nenhuma a mais (1.5.0)

1. `cdm_casca_definicao_paginas()` ganhou o filtro **`cdm_paginas`**. Era o
   único registro da casca sem filtro; sem ele, toda ferramenta nova obrigaria a
   editar a casca — e casca editada por bloco de ferramenta é casca que sai do
   ar por defeito de ferramenta.
2. **`/materiais/` passou a listar as ferramentas** (16.4a). Ela é a mãe das
   duas e não as listava; enquanto nenhuma existia isso não aparecia, e no dia
   em que a primeira nasce a falta vira página órfã. **E a listagem vem ANTES
   das seis prateleiras**: as seis são cartão "em breve" e nenhuma abre, então
   deixá-las no topo punha seis cartões mortos na frente do único caminho vivo
   da página — que é justamente o que termina numa recomendação de compra.

### VERIFICAÇÃO

- `ferramentas/teste-f2.php`: **72 afirmações**, régua própria, **um processo
  por estado** — os **45** estados de cola e os **60** de rejunte, mais a
  âncora e os estados com parâmetro. Zero falha.
- `ferramentas/mutacoes-f2.py`: **20 mutações, 20 reprovadas**.
- `ferramentas/teste-casca.php`: **367 verificações**, nenhuma falha, agora
  incluindo a página nova nos portões de voz, prova, escassez, trilha, árvore,
  página fina e entidade dentro de `<script>`.
- `ferramentas/validar-banco.py`: aprovado, com a matriz batendo com as
  declarações depois da restauração dos acentos.
- `php -l` limpo nos três snippets.
- Chromium em 360/390/781/782/783/1200 px nas doze páginas (as nove da casca,
  a âncora da F2 e dois estados dela com parâmetro): **78 medições, 0 px de
  rolagem horizontal**.
- **NO AR, às 22h05Z:** o Sync aplicou os 5 itens (snippet `f2` criado como #7,
  casca atualizada e os três arquivos do banco virando option pela primeira
  vez), o `/status` devolve **revisão 9**, e `ferramentas/conferir-no-ar.py`
  mediu **145 afirmações no HTML SERVIDO, zero falha** — as 10 URLs em 200, a
  tabela pré-renderizada servida, o JSON-LD servido, e os quatro casos de
  coerência (espelho, cimento em sol e chuva, MDF e vidro laminado) com o
  silicone acético **na seção do que não usar** e nunca na recomendação.
  O sitemap passou de 8 para **9 URLs**, a F2 recebe **dois links internos** (a
  home e a mãe) e a trilha serve os três degraus com endereço de verdade.

  **O Sync precisou de três disparos, e a razão vale registrar:** os dois
  primeiros leram do `raw.githubusercontent` um `manifest.json` ainda na revisão
  8 enquanto já baixavam a casca nova — "sha256 divergente, não aplicado", que é
  a trava funcionando. Cache de borda por caminho, não por commit: o arquivo
  novo e o índice velho chegam em momentos diferentes. Esperar e repetir
  resolve; o que não se pode é ler o primeiro "0 aplicados" como entrega.

### Números da ilha, contados

**10 dos 10 itens do banco esperam link de afiliado; 10 estão sem imagem** —
este bloco não tocou catálogo, e nenhum dos dez tem loja possível hoje. Da
pauta da seção 17: **nenhum tema escrito, nenhum na fila, nenhum recusado** —
`pauta.md` ainda não existe nesta pasta.

**Próximo passo:** a **F1**, em `/materiais/quantas-pastilhas-para-mosaico/`,
com a mesma mãe. A especificação está pronta desde o bloco 2, com a correção do
bloco 3c: a coluna de rejunte vale só para rejunte **cimentício** e a de gramas
de cola sai **vazia com explicação**, porque faltam o consumo por área da
cimentcola e o rendimento por área do silicone. Ela reaproveita da F2 o registro
de página pelo filtro, o desenho de resposta servida pelo servidor com `noindex`
no estado com parâmetro, o cartão de compra e o padrão de teste com varredura
da entrada inteira.

## 12/09/2026, 00h05Z — BLOCO 4, SEGUNDA PARTE: A F1 NO AR — e a casca que não deixava a página nascer

**Entregue:** `/materiais/quantas-pastilhas-para-mosaico/`, a segunda ferramenta
da ilha (`snippets/clubedomosaico-f1.php` 1.0.0, casca **1.6.0**, manifest na
revisão **11**, `/status` com revisão 11 às 00h05Z). Nível 3, mãe `/materiais/`,
a mesma escolha da F2 e pelo mesmo motivo.

### Por que esta página ganha, e é a única que responde isto

O bloco 1 mediu que a primeira página inteira de "rejunte para mosaico" responde
à pergunta da **obra** — 0,2 a 0,4 kg/m², "1 kg faz 3 m²" —, e esses números
foram calculados com azulejo grande. A **mesma fórmula do fabricante**, aplicada
à pastilha de 1×1 cm com folga de 2 mm, dá **2,8 kg/m²**: 3,8 vezes o azulejo de
10 cm e 2 vezes o piso de 20. A página não disputa aquelas — ela responde outra
pergunta, e serve as duas contas **lado a lado, na mesma tabela**, para a
diferença ficar verificável em vez de afirmada.

### As cinco decisões, e a cicatriz que cada uma evita

1. **A conta é do servidor**, como na F2: o formulário é um GET para a própria
   página, não existe uma linha de decisão em JavaScript, e todo estado é HTML
   servido de verdade. O preço é URL com parâmetro, pago na mesma linha —
   `noindex, follow` no estado com parâmetro, e quem entra no índice é a âncora.
2. **A geometria é nossa; o consumo é do fabricante.** Área por forma (o cone
   pela **geratriz**, nunca pela altura — num vaso bojudo a diferença passa de
   10% e sempre para menos) e contagem pelo passo são aritmética e não dependem
   de banco nenhum. Os gramas saem da fórmula publicada pela Quartzolit com o
   coeficiente **lido do registro do rejunte cerâmicas**, nunca digitado.
3. **A correção do bloco 3c está na tela.** O 1,75 vem de um exemplo de rejunte
   cimentício **em pó**; o acrílico é pronto uso em pote e o epóxi é
   bicomponente. A ferramenta recusa calcular para os dois e nomeia o que falta.
   E recusa também **se o banco trouxer dois coeficientes diferentes**: escolher
   um deles calado é a mesma invenção com outra roupa.
4. **A régua do rejunte tem dono.** `cdm_f2_celula_rejunte()` é chamada daqui em
   vez de reescrita; a F1 só filtra pelo tipo escolhido. Duas implementações da
   mesma decisão no mesmo site é o defeito que a Robometria pagou comparando
   duas cópias da mesma régua.
5. **A sobra vai na pastilha e não no rejunte**, e arredonda para cima. Lote
   novo de pastilha muda de cor: faltar dez peças no fim é pior que sobrar dez.
   O saco de rejunte não tem esse problema.

### O QUE QUASE PASSOU: a página respondeu 404 com o Sync dizendo revisão 10

O Sync aplicou seis itens, criou o snippet #8, escreveu revisão 10 no `/status`
— e `conferir-no-ar.py` devolveu **37 falhas**, todas a mesma: a URL da F1 não
existia. **Commit sem verificação no ar não é entrega**, e foi a régua que disse
isso, não a leitura do log.

A causa é da casca, e é fina: `cdm_casca_montar()` voltava na primeira linha
quando `get_option('cdm_casca_estrutura')` era igual a `CDM_CASCA_VERSAO`. A
1.5.0 tinha acabado de criar o filtro `cdm_paginas` **exatamente** para que uma
ferramenta nova registrasse a própria página sem ninguém editar a casca — e a
guarda deixava esse mecanismo inerte: página nova entrava na definição, a versão
da casca continuava a mesma, a montagem não rodava, a página nunca nascia. **A
F2 escapou porque nasceu junto com a 1.5.0** e foi de carona na troca de versão.
Mecanismo que só é exercitado de verdade na segunda vez que alguém o usa.

**Casca 1.6.0:** a chave passa a ser a versão **mais um resumo do mapa de
páginas** (slug, título, mãe e shortcode de cada uma). Página nova, título
trocado ou mãe trocada mudam a impressão e a estrutura se remonta sozinha no
primeiro carregamento depois do Sync — sem humano logado, sem `?cdm_casca=refazer`
e sem tocar na casca. Remontar é barato e seguro porque `garantir_paginas()` só
cria o que falta. O portão 21b do `teste-casca.php` **mede o mecanismo, nunca a
versão**: um teste que olhasse `CDM_CASCA_VERSAO` teria ficado verde com o
defeito no ar, que foi o que aconteceu por um bloco inteiro.

### O cluster mudou de estado sozinho — e duas mutações antigas pararam de morder

Com a terceira filha de `/materiais/` no ar, a F2 e a `/materiais/como-sabemos/`
passaram a ter **duas irmãs** e as três publicam "Veja também". Ninguém editou
nada: as irmãs são derivadas do mapa, e a regra da seção 6 do `ARVORE.md`
funcionou pela primeira vez no sentido inverso — antes ela **proibia** o bloco,
agora ela o **exige**.

O efeito colateral foi o achado do dia, e são dois casos diferentes:

- **"irmã escolhida fora da mãe" passou** porque o portão do cluster contava
  quantas irmãs saíam e se estavam no ar, **nunca de onde elas vinham**. A
  mutação morria por efeito colateral — estourava a contagem — e o efeito sumiu
  quando havia mais páginas no ar. **Trava frouxa de verdade**, e agora toda
  irmã listada tem a mãe recomputada do mapa. Trava que reprova por efeito
  colateral é trava que um dia para de reprovar.
- **"a página fora do sitemap perde a citação" passou** porque o cluster novo
  liga a camada de prova sozinho. Aqui a trava **não** afrouxou: ela mudou de
  dono. E o que mudou de dono ganhou trava própria — a citação **no texto**,
  medida com o cluster e a trilha fora da conta, porque o que se mede ali é
  escolha editorial, não geração automática.

### O que a página diz que não sabe

A linha de **gramas de cola** nasce vazia com o motivo escrito (o fabricante do
silicone declara rendimento por cordão, não por área, e o consumo por área da
cimentcola não foi obtido). A **pastilha não tem banco**: o cartão de compra tem
o lugar reservado dizendo que está vazio, em vez de sumir. E **sem o banco a
página continua respondendo área e pastilhas** e diz que não publica os gramas —
a bancada mede esse estado de propósito, porque página degradada é uma página
válida, com cabeçalho, rodapé e prosa, e foi assim que a Robometria mediu três
páginas pela metade sem ninguém acusar.

### Verificação

- `ferramentas/teste-f1.php`: **67 afirmações**, régua aritmética escrita fora do
  snippet, um processo por estado. Varre 24 combinações de forma × caquinho, 36
  de folga × tipo de rejunte, as cinco sobras, quatro espessuras, cinco lugares,
  e as bordas fabricadas: vão maior que a moldura, folga que nenhum fabricante
  cobre, caquinho irregular, banco ausente e **banco com outro coeficiente**.
- `ferramentas/mutacoes-f1.py`: **27 de 27 reprovadas.** Duas passaram na
  primeira rodada e as duas viraram afirmação nova — o CR digitado dentro do
  snippet **com o valor certo** (invisível para qualquer teste sobre a tela de
  hoje; só troca de banco o revela) e a vitrine ignorando o tipo escolhido
  (continua sendo subconjunto do que a F2 aprova, então a trava de subconjunto
  não a via).
- `teste-casca.php` de **367 para 409** com a página nova nos portões de voz,
  prova, trilha, árvore e página fina; `mutacoes-arvore.py` **20 de 20**;
  `teste-f2.php` 72 e `validar-banco.py` sem regressão; `php -l` limpo nos
  quatro snippets; os três JSON reparseados.
- Chromium em 360/390/781/782/783/1200 nas **14 páginas** — três delas estados
  da F1, incluindo o da medida que não fecha —, **88 medições, 0 px de rolagem**.
  **A medição foi feita com a casca 1.5.0**, antes do conserto da remontagem, e
  fica dito assim de propósito: o que a prova valer tem que ser o que foi
  medido. O que sustenta ela continuar valendo é uma segunda medida, não uma
  suposição — o HTML servido das 14 páginas é **byte a byte idêntico** entre a
  1.5.0 e a 1.6.0, porque a 1.6.0 só troca a chave que decide *quando* a
  estrutura é remontada e não imprime uma linha na tela (a constante de versão
  nem aparece no HTML). Uma terceira rodada do navegador foi tentada e morreu no
  túnel de rede, que estava derrubando as conexões de fonte.
- **No ar, às 00h05Z:** `conferir-no-ar.py` com **194 afirmações medidas no HTML
  servido, zero falha**. As 11 URLs em 200, as três tabelas pré-renderizadas
  servidas, JSON-LD `WebApplication` + `FAQPage`, canonical na âncora e
  `noindex` em todo estado com parâmetro, e **quatro contas conferidas contra o
  que foi calculado à mão** (vaso 942 cm²/720/264 g, tampo 2.827/588/594 g,
  esfera 1.257/960/352 g, moldura 900/188/189 g). O sitemap passou de 9 para
  **10 URLs**.
- **Defeito de etiqueta consertado de quebra:** o manifest dizia casca 1.4.0
  enquanto o arquivo definia 1.5.0. O sha estava certo — o Sync aplicou os bytes
  certos e o site nunca esteve errado —, envelheceu a **etiqueta**, que é por
  onde qualquer relatório lê o que está no ar. Nenhum portão lia essa metade;
  agora `atualizar-manifest.py` compara a versão do manifest com a constante do
  snippet e **recusa gravar** quando os dois se separam. Foi ele que acusou a
  1.6.0 antes deste commit.

### Números da ilha, contados

**10 dos 10 itens do banco esperam link de afiliado; 10 estão sem imagem** —
este bloco não tocou catálogo, e nenhum dos dez tem loja possível hoje. Da pauta
da seção 17: **nenhum tema escrito, nenhum na fila, nenhum recusado** —
`pauta.md` ainda não existe nesta pasta.

**Próximo passo:** as **fichas de categoria de material** (bloco 4c). A 16.5
continua valendo — categoria só nasce com três filhas de dado real —, e hoje
Colas e Rejuntes têm banco de cinco itens cada e **uma** filha cada (as duas
ferramentas). O caminho mais curto para destravar `/materiais/colas-e-adesivos/`
e `/materiais/rejuntes/` é a leva de fichas de produto, que são nível 3 com dado
real: cinco colas e cinco rejuntes já cadastrados, cada ficha com a declaração
do fabricante, a faixa, a fonte e o cartão de compra. A ilha está **abaixo do
piso** da seção 21 (10 URLs, 21 dias não passaram), então a leva sai no ritmo
normal, de 5 a 10 URLs, sem esperar medição.

12/09/2026 15h55Z — DESPACHO DA SENTINELA DE 12/09 CUMPRIDO INTEIRO (itens 1 e 2)

- **Os dois itens eram o mesmo defeito com duas roupas**, e foi por isso que o
  conserto virou UMA regra em vez de dois remendos: a página falava de menos
  produtos do que listava, ou nomeava a causa errada por quem ficou de fora. A
  regra subiu para o `ARQUIPELAGO.md` seção 7, porque vale para toda ilha:
  **todo item do banco é nomeado exatamente uma vez em cada resposta** — na
  frase que o recomenda, e aí ele está na vitrine, ou numa linha que diz por que
  ele não está — e **o bloco de compra serve exatamente o que a frase nomeia**.
  Junto com ela foi a metade complementar: **a recusa nomeia a causa que a
  página mediu, nunca oferece hipótese**, e **afirmação em bloco tem o escopo
  do que foi medido**.

- **ITEM 2 (F2, `clubedomosaico-f2.php` 1.0.0 → 1.1.0).** A frase dizia "o
  rejunte é Rejunte Acrílico Quartzolit", singular e definitiva, e a vitrine
  logo abaixo servia QUATRO cartões. Agora a frase tem duas linhas — a
  recomendação e os que também servem, com o que os separa escrito (o fabricante
  não nomeia o lugar; a régua do rejunte só transforma silêncio em exclusão nos
  ambientes críticos) — e a vitrine serve exatamente esses. Os que ficaram de
  fora ganharam uma linha cada: fora pela folga (com a faixa publicada), fora
  pelo lugar, fonte de imprensa e **faixa não obtida**.
  **Dois achados dentro do item**, e nenhum dos dois estava no despacho:
  (a) o grupo `mencionados_com_ressalva` não era impresso em lugar nenhum —
  vazio com o banco de hoje, invisível para sempre no dia em que enchesse;
  (b) "faixa não obtida" estava sendo contada como "a folga não cabe", que é
  afirmar sobre uma declaração que ninguém leu — o rejunte piscinas não publica
  faixa, e a página dizia que ele não cobria 2 mm. Esse mesmo defeito tinha
  tornado INALCANÇÁVEL um ramo da frase de recusa que eu mesma acabara de
  escrever ("só o lugar exclui"): com o piscinas eternamente no balde da folga,
  aquele caso nunca acontece. Ramo morto saiu; quem diz a causa são as linhas.

- **ITEM 1 (F1, `clubedomosaico-f1.php` 1.0.0 → 1.1.0).** A recusa culpava
  SEMPRE a folga, inclusive quando a folga cabia e quem excluía era o lugar — e
  com a linha de "outro tipo" logo abaixo dizendo "dentro dessa folga", a página
  negava e afirmava o mesmo fato em duas frases seguidas. Agora são três causas
  com nome próprio, produtos nomeados e a faixa que o fabricante publica; e
  quando a causa é o lugar a página diz "é o LUGAR, não a folga", o que não é
  suposição: quem cai pelo lugar passou pela trava da folga antes.
  **A outra metade do defeito não estava no despacho e só a tela mostrava:**
  `strtok( $rotulo, ' —' )` cortava no primeiro espaço e devolvia só "Rejunte",
  então a frase afirmava sobre o banco INTEIRO ("Nenhum rejunte do nosso
  banco…") o que valia no máximo para o tipo escolhido.

- **O PORTÃO ACHOU UM BURACO NO PRÓPRIO CONSERTO, antes do desembarque.** A
  primeira versão da F1 só prestava contas quando a lista voltava vazia: em 27
  estados ela listava dois cimentícios e não dizia uma palavra sobre o terceiro.
  É o item 2 um andar acima — produto do banco que some da tela sem que nada
  diga por quê. A prestação de contas passou a sair sempre.

- **PORTÃO NOVO: `ferramentas/teste-prestacao-rejunte.php`.** Régua própria,
  recomputada aqui a partir dos `perfis_esperados_do_rejunte` escritos à mão e
  das regras 1 a 4 do esquema — nada nele chama `cdm_f2_celula_rejunte()`,
  `cdm_f2_avaliar_rejunte()` nem `cdm_f2_perfil_rejunte()`. Varre **540 estados
  da F2** (9 bases × 5 lugares × 12 folgas), **180 da F1** (3 tipos × 5 lugares
  × 12 folgas) e as **9 linhas da tabela pré-renderizada**, um processo por
  estado, com as folgas indo de 1 a 12 para pisar nas bordas (1 e 11 estão fora
  de todo extremo declarado; 2, 4, 5 e 10 são extremos exatos). 5 afirmações, 0
  falha.

- **`ferramentas/mutacoes-prestacao.py`: 11 mutações, 11 reprovadas.** As duas
  primeiras são os dois defeitos do despacho escritos de volta. **Quatro delas
  não morderam na primeira rodada, e as quatro ensinaram coisa diferente:**
  (1) a que condicionava a linha de `fora_lugar` mirava um estado que o banco de
  hoje não produz — os dois cimentícios têm faixa e declarações iguais, então ou
  os dois servem ou os dois caem; o estado que existe é o de `sem_faixa`;
  (2) a do grupo de ressalva não mudava um byte enquanto o banco não tivesse
  fonte fraca, e precisou **produzir o mundo** nas DUAS metades (o nível nas
  `fontes` do banco, que o snippet lê, e o nível no perfil escrito à mão, que a
  régua lê) — rebaixar só uma faria o teste reprovar pelo motivo errado;
  (3) a da tabela mirava o grupo de ressalva, vazio, e teve de mirar o de faixa
  não obtida, que está fora em todas as nove linhas;
  (4) a da promoção silenciosa **passou por erro de alvo**: a linha do score é
  idêntica byte a byte em `cdm_f2_avaliar_cola()` e em `cdm_f2_avaliar_rejunte()`,
  e a substituição pegou a primeira — mutou a cola, que este portão não mede, e
  o verde foi honesto. O alvo agora carrega a linha anterior, que é a única
  diferença entre as duas funções naquele ponto.

- **DOIS DEFEITOS MECÂNICOS CONSERTADOS NA MESMA PASSADA (seção 19).** O
  manifest declara `sha256` no grupo `ferramentas` desde que nasceu e **nenhuma
  linha o recalculava**: `render-para-teste` e `teste-casca` estavam com a
  etiqueta de uma versão que não existe mais, de blocos anteriores. E a lista
  conhecia **9 das 18 ferramentas** do disco — entre as ausentes, `teste-f1.php`
  e `teste-f2.php`, que são os dois portões principais da ilha. Bancada não vai
  para o site, então nada disso quebraria uma página; quebrava a capacidade de
  qualquer relatório dizer com o que esta ilha se verifica.
  `atualizar-manifest.py` passou a espelhar o grupo e a cobrar as duas direções
  (ferramenta no disco fora do manifest agora reprova). 16 sha recalculados.

- **VERIFICAÇÃO.** `php -l` limpo nos três snippets; `teste-prestacao-rejunte`
  5 afirmações 0 falha em 729 estados; `teste-f1` 67; `teste-f2` 72;
  `teste-casca` 409; `validar-banco` sem regressão; mutações antigas intactas
  (f1 27/27, f2 20/20, rejunte 12/12, árvore 20/20 — nenhuma virou inerte);
  Chromium em 360/390/781/782/783/1200 nas **16 páginas** renderizadas (as 11 da
  casca mais os 5 estados de ferramenta que este bloco mudou), **98 medições, 0
  px de rolagem lateral**.
  **UMA AFIRMAÇÃO ANTIGA FOI REESCRITA, e isso é parte da entrega:** o
  `teste-f1.php` cobrava a string `'do nosso banco declara folga'` para os 11 e
  12 mm — que é a frase DO DEFEITO. Afirmação que fixa o texto de hoje vira
  trava contra o conserto de amanhã; ela passou a cobrar a intenção (a página
  diz que nenhum serve E diz que a causa é a folga).

- **NO AR às 15h51Z: revisão 12 no `/status`, igual à do manifest, 6 aplicados,
  UM disparo** — sem o atraso de CDN dos blocos anteriores. `conferir-no-ar.py`
  mediu **231 afirmações no HTML servido, 0 falha**, e ele ganhou as afirmações
  do despacho escritas nas palavras do próprio despacho: as 6 combinações do
  item 1 (externo_exposto e contato_permanente_agua × 2, 4 e 10 mm) sem a frase
  antiga, dizendo que a exclusão é do lugar e nomeando o lugar; os 5 rejuntes do
  banco contados um a um em 3 respostas do item 2; e as 9 linhas da tabela
  somando 5.

- **Receita:** 10 dos 10 itens do banco continuam esperando link de afiliado e
  10 seguem sem imagem; este bloco não tocou catálogo, e nenhum dos dez tem loja
  possível hoje. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0
  na fila, 0 recusados.

- **PRÓXIMO PASSO:** o bloco **4c**, fichas de categoria de material
  (`/materiais/pastilhas/`, `/alicates/`, `/colas/`, `/rejuntes/`, `/bases/`,
  `/acabamento/`). A regra nova da seção 7 nasce com ele em vez de ser
  descoberta depois: ficha de categoria é, por definição, uma página que fala de
  TODOS os itens de uma categoria do banco, então a prestação de contas dela é a
  própria página — e o portão desta execução já sabe medir isso. A ilha está
  ABAIXO DO PISO da seção 21 (11 URLs, 21 dias não passaram), então a leva sai
  no ritmo normal, de 5 a 10 URLs, sem esperar medição.

---

## 12/09/2026 17h37Z — A TAG DO GA4 NO AR: a ilha começa a ser medida

**Despacho ALTA de 12/09/2026 para a FUNDAÇÃO** (`dados/despachos.md`), na parte
desta ilha. Casca **1.7.0**, manifest na **revisão 13**, `/status` com revisão 13
às 17h37Z, em **UM disparo**.

- **O MARCO ZERO DESTA ILHA É 12/09/2026 17h37Z.** Antes disso não existe dado de
  audiência, e isso é a metade que faltava para a seção 5 ser executável: a ilha
  nasceu em 10/09 e serviu nove, depois onze URLs **sem tag nenhuma**. Qualquer
  leitura feita até hoje devolveria zero, e aquele zero media **a ausência da
  tag** — nunca a ausência de visita. A seção 5 manda o relatório dizer qual dos
  dois é; até hoje a resposta desta ilha era sempre o primeiro.

- **A prioridade 8 no `wp_head` não é gosto, é o único número que cabe.** O
  despacho pede a tag o mais cedo possível **e** proíbe que ela passe na frente
  do `<title>`, da meta descrição e do JSON-LD. As duas metades juntas dão
  exatamente 8: depois do robots (4), do ícone (5), do `Organization` (6) e da
  trilha (7), e **antes da folha de fontes (20)**, que é o único recurso
  bloqueante desta casca. O `async` faz o resto — o LCP desta ilha é texto.

- **O ID é constante no topo e é conferido antes de ser impresso.** ID de medição
  digitado no meio do código é ID que alguém copia junto com a casca para a ilha
  4 e só descobre trocado quando o relatório do mês vier somando duas ilhas.
  `cdm_casca_ga4_html()` só devolve markup se o ID casar com `G-` + maiúsculas e
  dígitos: meia tag no ar não mede nada **e** ainda faz o console falar.

- **A página de Privacidade mudou na mesma versão, e isso não foi zelo.** Ela
  prometia, com todas as letras, que "se um dia houver medição de audiência, esta
  página será atualizada *antes* de ela ser ligada, com a data da mudança".
  Ligar a medição e deixar a promessa de pé seria publicar uma frase falsa na
  página que existe justamente para não ter nenhuma. Sem banner de consentimento
  (22.4).

- **ACHADO QUE NÃO É DESTE BLOCO, E É PARA O RAPHAEL: o Site Kit by Google
  1.187.0 está instalado e ativo nesta ilha e não mede nada.** Medido no HTML
  servido **antes** de mudar qualquer coisa: zero ocorrência de `gtag(` e zero do
  ID da ilha; o que ele deixa na página é uma meta `generator` e um
  `dns-prefetch`. Plugin desconectado ocupando uma linha de `<head>`. O risco não
  é hoje: no dia em que alguém o conectar pelo wp-admin, a propriedade ganha um
  **segundo dono de tag** e toda sessão passa a ser contada duas vezes **sem uma
  coisa mudar na tela**. Quem acusa isso é uma afirmação nova do
  `conferir-no-ar.py`, que conta os inicializadores de `gtag` no HTML servido.

- **DEFEITO MECÂNICO CONSERTADO NA MESMA PASSADA (seção 19), e ele mordeu esta
  execução.** `atualizar-manifest.py` parava no **primeiro** achado, e o `return`
  do descasamento de versão escondeu a conferência de ferramenta órfã: o
  `mutacoes-ga4.py` recém-escrito ficou fora do manifest **sem uma linha de
  aviso**, numa execução em que a versão do snippet acabara de subir — que é
  exatamente quando ferramenta nova nasce. O portão existia, estava certo e era
  **inalcançável**: a conferência que roda primeiro escondia a que interessava.
  As quatro conferências agora acumulam e a lista sai inteira.

- **VERIFICAÇÃO.** `teste-casca.php` de **409 para 539 afirmações**, 0 falha, com
  a **ordem** medida e não só a presença — portão que só pergunta "existe gtag na
  página?" fica verde com a tag no lugar errado, que é o único jeito de esta
  mudança fazer mal. `mutacoes-ga4.py` novo: **14 de 14 reprovadas**, em três
  famílias (a tag some ou sai pela metade; a tag fica e está errada — ID de outra
  ilha, ID digitado ao lado da constante, `config` discordando do `src`, tag
  dobrada, que é o caso Site Kit; e a tag certa no lugar errado — sem `async`,
  antes do JSON-LD, depois das fontes). **Uma mutação reprovou pelo portão errado
  na primeira rodada e foi reescrita:** ela trocava a frase nova da privacidade
  *pela* velha, então morria na trava da frase nova e deixava sem medida a trava
  que interessa — a que mede a **ausência** da promessa antiga. Agora ela
  acrescenta o parágrafo velho sem tirar o novo, que é como isso acontece de
  verdade. Regressões sem uma falha: f1 67, f2 72, prestação 5 em 729 estados,
  `validar-banco`, e as mutações antigas (f1 27/27, f2 20/20, rejunte 12/12,
  árvore 20/20, voz 24/24, prestação 11/11) — nenhuma virou inerte. `php -l` limpo.

- **NO AR às 17h37Z:** `conferir-no-ar.py` de **231 para 334 afirmações** no HTML
  **servido**, 0 falha. As onze URLs com a tag uma vez só dentro do `<head>`, o
  ID desta ilha, o `async`, o `config` batendo com o `src`, a ordem conferida no
  que o **servidor** serve, o `gtag` como **único** script de terceiro, **um**
  inicializador e não dois, e a página de Privacidade com a frase nova, a data, e
  a promessa antiga **medida como ausente**.

- **O TERCEIRO CRITÉRIO DO DESPACHO FICOU ABERTO, e não por falta de tentativa.**
  O Tempo Real do GA4 não foi confirmado. Duas causas independentes, as duas
  medidas e **repetidas na mesma execução**, como a seção 20.2 exige:
  1. **Sem credencial.** `ferramentas/ga4.py` pede `GOOGLE_SA_B64`,
     `GOOGLE_SA_JSON` ou `GOOGLE_SA_FILE`, e o ambiente desta rotina não tem
     nenhuma das três (zero variável `GOOGLE*`). A conta de serviço já é Leitor
     na conta `Arquipélago`: falta a **variável**, não a permissão.
  2. **`www.googletagmanager.com` está fora da lista de egresso.** 403 ao
     CONNECT, cinco vezes, com `clubedomosaico.com.br` em 200 na mesma passada —
     é **política**, e não a intermitência de túnel da seção 20.2, e a regra é
     nomear o host barrado em vez de insistir. A consequência é maior que o item:
     **nenhuma verificação de tag por navegador a partir da nuvem pode funcionar**
     enquanto esse host estiver barrado, porque o navegador não baixaria o
     `gtag.js`. De quebra, o Chromium não atravessa este túnel nem para o domínio
     liberado (`ERR_CONNECTION_RESET` em 3 tentativas, `ws_closed_mid_exchange` no
     proxy, `curl` em 200 no mesmo minuto).

- **Nasceu mesmo assim `ferramentas/conferir-tag-no-navegador.mjs`**, que abre a
  ilha num navegador e mede o **disparo saindo** (o `tid`, o código que o Google
  devolve, **um** `page_view`, o console limpo). O `conferir-no-ar.py` usa `curl`
  e `curl` não executa uma linha de JavaScript: ele prova que a tag **está** na
  página e nunca que a visita **chega** na propriedade. O arquivo diz no próprio
  cabeçalho que **nunca foi visto aprovando**, porque ferramenta que ninguém viu
  rodar é promessa.

- **O que fecha o item é configuração, não código:** `www.googletagmanager.com` e
  `*.google-analytics.com` na rede Personalizada do ambiente das rotinas, junto
  com os domínios das ilhas que já estão lá, e a credencial da conta de serviço
  na variável de ambiente. Até lá, quem confirma o Tempo Real é o Raphael, no
  Chrome dele. **E o que NÃO se fez, escrito para ninguém ter a ideia:** mandar
  um evento pelo Measurement Protocol para "confirmar" a medição seria inventar a
  visita que se queria comprovar e sujar a série com uma sessão que nunca
  existiu. Zero medido é dado; zero fabricado é mentira.

- **`dados/audiencia.md` nasceu** com o marco zero e com esta não-medição escrita
  como linha da série — que é o que a seção 5 manda quando não se conseguiu medir.

- **Receita:** 10 dos 10 itens do banco seguem esperando link de afiliado e 10
  sem imagem; este bloco não tocou catálogo. Pauta da seção 17: `pauta.md` ainda
  não existe — 0 escritos, 0 na fila, 0 recusados.

- **PRÓXIMO PASSO:** o bloco **4c**, fichas de categoria de material, que já era
  o próximo antes deste despacho furar a fila e continua sendo. A ilha está
  ABAIXO DO PISO da seção 21 (11 URLs), então a leva sai no ritmo normal, de 5 a
  10 URLs, sem esperar medição — e agora, pela primeira vez, com a série de
  audiência correndo por baixo dela.

12/09/2026 19:21Z — A VARREDURA DA SEÇÃO 14.3: o 4c não estava esperando ser escrito, estava esperando banco — e agora isso é um número

- **O bloco começou como 4c e virou a medição que o 4c pedia.** O `ESTADO.md`
  vinha dizendo, execução após execução, que o próximo passo eram as **seis
  fichas de categoria de material** (`/materiais/pastilhas`, `/alicates`,
  `/colas`, `/rejuntes`, `/bases`, `/acabamento`). O `ARVORE.md` já dizia, desde
  11/09, que nenhuma delas podia nascer pela **16.5** — categoria só nasce com 3
  filhas de dado real, e Colas e Rejuntes têm **uma** cada. As duas frases
  conviviam porque nenhuma era falsa. O que faltava era o segundo portão, que
  ninguém tinha medido: **a seção 14.3**, que proíbe faixa de ferramenta sair com
  menos de 3 produtos elegíveis. Sem esse número, a próxima execução escolheria
  entre escrever seis páginas magras e adiar de novo, sem critério.

- **O QUE A VARREDURA MEDIU, de ponta a ponta e pela primeira vez.** Dos **45**
  estados de cola que a F2 serve, **ZERO** chegam aos 3 elegíveis que a 14.3
  exige; o teto é **2** e **13** não servem nenhum produto. Dos **60** estados de
  rejunte, **12** chegam, **48** não, e **25** não servem nenhum. E **5 das 7
  categorias do vocabulário não têm um único item no banco**: `pastilha`,
  `alicate`, `base`, `acabamento`, `apoio`. A consequência é mais dura do que a
  16.5 sozinha: com o banco de hoje **nem as filhas de nível 3 de cola podem
  nascer**, porque nenhum recorte da categoria reúne os 3 itens que o portão de
  dado da seção 9 cobra. Não é falta de texto — é falta de produto.

- **TRÊS FONTES, E NENHUM NÚMERO DIGITADO.** (1) A **faixa** vem de
  `ferramentas/faixa-da-f2.php`, que a mede **provocando o próprio snippet**: põe
  cada valor de um superconjunto deliberadamente maior em `$_GET`, chama
  `cdm_f2_entrada()` — a mesma função que saneia a consulta de quem visita — e
  fica com o que sobreviveu. Faixa digitada mediria a faixa que alguém lembrou e
  ficaria verde no dia em que o campo da junta mudasse de teto. O medidor
  **recusa medir** quando o superconjunto não passa por cima nem por baixo da
  faixa (teto medido igual ao teto da régua não é teto, é o fim da régua) e
  quando o saneamento aceita um valor inventado. (2) A **régua** é a de
  `validar-banco.py`, importada: ela recompõe a elegibilidade das **declarações**
  pelas regras do esquema e foi escrita no bloco 3 **antes** de existir uma linha
  do snippet PHP. Reimplementá-la aqui uma terceira vez não acrescentaria
  independência nenhuma — acrescentaria uma cópia para envelhecer calada. (3) O
  que o **site serve** é conferido por `ferramentas/conferir-cobertura.php`, que
  anda os mesmos estados chamando o snippet, **um processo por estado**.

- **O CRUZAMENTO PASSOU DE 27 PARA 105 ESTADOS, e esse é o ganho estrutural do
  bloco.** A régua Python e a régua PHP são duas implementações da mesma regra, e
  até hoje elas só se encontravam nas **27** células escritas à mão do esquema —
  18 de cola e 9 de rejunte — de **105** que as ferramentas servem. Os outros
  **78** nunca tinham sido comparados com nada: se as duas metades divergissem
  ali, o censo diria um número e a página serviria outro, e nenhum portão veria.
  Hoje as duas concordam nos 105. `conferir-cobertura.php`: **128 afirmações, 0
  falha**.

- **MUTAÇÕES: 14 escritas, 14 reprovadas, e 9 delas NENHUM portão antigo pegou.**
  O script roda, para cada mutação, também `validar-banco.py` e `teste-f2.php`, e
  marca as que só a varredura viu — mutação que qualquer portão antigo pega já
  estava coberta e não justificaria arquivo novo. A que melhor mostra o buraco:
  **a faixa de junta afrouxa só em 7, 8 e 9 mm**. A grade escrita à mão do
  esquema pisa em 1, 2, 3, 4, 5, 6, 10 e 11 mm, escolhidos para encostar nas
  bordas declaradas — é uma grade boa, e é exatamente por isso que 7, 8 e 9 caem
  num vão onde nenhum extremo mora. Com esse afrouxamento o site passa a
  recomendar rejunte que o fabricante não cobre, e os 27 cruzamentos antigos
  continuam verdes.

- **DUAS MUTAÇÕES FORAM REESCRITAS DEPOIS DE PASSAR, e as duas ensinaram algo.**
  (a) A que derrubava a **regra 3 do rejunte** (quem delimita ambiente fica
  fechado nele) passou — e não por buraco no portão: **com o banco de hoje essa
  regra é código morto.** Das cinco fichas, só o acrílico declara ambiente
  (`áreas internas e externas`), e nos estados em que a regra 3 o cortaria a
  regra 2 já o tinha cortado antes, porque `contato_permanente_agua` é crítico e
  as resistências dele param em `áreas molhadas`. A regra **fica no snippet** — é
  ela que vai decidir no dia em que entrar um rejunte que delimite ambiente — mas
  a mutação saiu, porque mutação inerte é teste verde com outro nome. (b) A do
  **gerador contando errado** reprovava pelo portão errado: ela mutava
  `cobertura.py` sem regenerar o JSON, então caía em "arquivo velho" em vez de na
  recontagem. O caso real é alguém mexer no gerador, rodar e commitar as duas
  coisas juntas — aí a regeneração bate consigo mesma e só a recontagem do lado
  PHP vê. Reescrita assim, ela passou a cair em `cola: "com o mínimo" bate com a
  contagem`, que é o portão que ela existe para medir.

- **REDE, reconferida como a seção 20.2 manda.** Os domínios de fabricante estão
  **fora da lista de egresso**: `colormix.com.br`, `vidrotil.com.br` e
  `quartzolit.weber` responderam `000` por `curl` em **duas passadas da mesma
  execução**, com `clubedomosaico.com.br` em **200** nas duas. É política, não a
  intermitência de túnel. **Mas isso NÃO bloqueia a coleta de banco:** o canal de
  busca alcança os mesmos fabricantes, foi assim que o bloco 3c colheu os cinco
  rejuntes, e foi reconfirmado nesta execução. Escrever "coleta bloqueada por
  rede" aqui seria repetir o diagnóstico que custou dois dias a esta ilha em
  11/09.

- **NADA FOI AO AR, e isso é desenho, não pendência.** Nenhum arquivo publicável
  mudou: os três snippets estão byte a byte como estavam, nenhuma URL nasceu e
  nenhuma mudou. `dados/cobertura.json` entra com `publicar: false` — o site não
  precisa dele, e publicá-lo criaria uma segunda fonte do mesmo número dentro do
  site. Portanto **não houve Sync nesta execução**, pela mesma leitura da seção 4
  que valeu no bloco 1. Manifest na **revisão 14**, com as quatro ferramentas
  novas e o censo inventariados — o portão de ferramenta órfã de
  `atualizar-manifest.py` acusou as quatro antes de qualquer commit, que é para
  isso que ele foi consertado ontem.

- **REGRESSÃO SEM UMA FALHA:** `php -l` em todos os snippets e ferramentas,
  `validar-banco` (10 materiais, 18 + 9 células recomputadas), `teste-casca`
  (539), `teste-f1` (67, 24 estados um processo cada), `teste-f2` (72),
  `teste-prestacao-rejunte` (5 afirmações sobre 540 estados da F2 e 180 da F1).
  O `teste-casca` importa em especial porque ele **lê o `ARVORE.md`** para cobrar
  que documento e código digam a mesma coisa, e este bloco escreveu uma seção
  nova lá. As sete baterias de mutação antigas foram rodadas inteiras para provar
  que **nenhuma virou inerte**: árvore 20/20, F1 27/27, F2 20/20, GA4 14/14,
  prestação 11/11, rejunte 12/12, voz e cabeça 24/24 — **128 mutações, 128
  reprovadas**.

- **Receita:** 10 dos 10 itens do banco seguem esperando link de afiliado e 10
  sem imagem; este bloco não tocou catálogo. Pauta da seção 17: `pauta.md` ainda
  não existe — 0 escritos, 0 na fila, 0 recusados.

- **PRÓXIMO PASSO, e agora ele tem ordem e motivo.** **Banco antes de página.** A
  categoria `pastilha` é a primeira, e não por gosto: a F1 responde "quantas
  pastilhas comprar" e a ilha não tem **uma** pastilha no banco, então a
  ferramenta de maior intenção de compra da ilha calcula uma quantidade e não tem
  o que vender — é a faixa descoberta mais cara da seção 14.3 e o buraco que
  nenhuma coleta de cola ou de rejunte fecha. Depois dela, cola, onde o teto de 2
  elegíveis por estado diz que faltam produtos. **Só então** as filhas de nível 3
  por cluster (16.6), e **só então** a mãe de nível 2, que é o 4c. A coleta vai
  pelo canal de busca, com as travas da seção 8: nunca pôr na consulta o valor
  que se quer confirmar, e fonte que não cita o documento é paráfrase.

12/09/2026 21:19Z — BLOCO 3d ENTREGUE: a categoria PASTILHA nasce no banco, e com ela o número que os fabricantes não publicam

- **Por que este bloco e não o 4c.** O `ESTADO.md` da execução anterior deixou a
  ordem escrita e o motivo junto: **banco antes de página**, e `pastilha` é a
  primeira das cinco categorias que a varredura da seção 14.3 achou com ZERO
  itens — a F1 responde "quantas pastilhas comprar" e a ilha não tinha **uma**
  pastilha para vender. Nenhuma URL nasceu ou mudou.

- **O QUE ENTROU:** `dados/materiais-pastilhas.json`, 10 SKUs de dois lugares
  distintos da escada de fontes. Nove da **Glass Mosaic** (fabricante, nível 3):
  linha Cristal 2,5 cm (K2501, K2502, MIX2510) e 3 cm (K117, K77, K66), linha
  Fosca 2 cm (A11, A61) e linha Strip 1,2 cm (ST5102). Um da **Pastilhart**
  (AF1500, 1,5 cm) — e ele entra em **nível 5**, não 3, porque a empresa se
  declara "importadora e distribuidora" na própria página institucional. É o
  único item do arquivo que declara ambiente, inclusive piscina, justamente o
  campo que mais pesaria numa recomendação: ter o dado e **não poder recomendar
  com ele** é o resultado certo da escada, não um defeito da coleta.

- **A COLETA, e as travas da seção 8.** Busca restrita ao domínio, como nos
  blocos 2, 3 e 3c. `curl` e `WebFetch` para glassmosaic.com.br,
  pastilhart.com.br, vidrotil.com.br, colormix.com.br e jatoba.ind.br devolveram
  `000`/`EGRESS_BLOCKED` em **duas passadas** da mesma execução, com
  clubedomosaico.com.br em **200 nas duas** — é política de egresso e não a
  intermitência de túnel que custou dois dias a esta ilha em 11/09 (seção 20.2).
  **Nenhuma consulta plantou o valor que se queria confirmar:** as buscas
  pediram os RÓTULOS da ficha ("tamanho, espessura, tamanho placa, placas caixa,
  peso caixa"), nunca um número.

- **TRÊS CAMPOS NASCEM NULL, E É O QUE ESTE ARQUIVO TEM DE MAIS ÚTIL.**
  - **Peças por placa — nenhum fabricante declara**, e é exatamente o número de
    que a F1 precisa para converter placa em peça. A SERP inteira preenche o
    buraco dividindo o lado da placa pelo lado da pastilha. **A divisão não
    fecha:** 29,2 / 3,0 = 9,73 e 32,3 / 2,0 = 16,15 não são inteiros — em 6 dos
    10 itens. E onde ela fecha, fecha errado por outro motivo: 30,0 / 2,5 = 12
    exige **junta zero** na placa telada, e placa sem junta é placa que não se
    rejunta. As duas leituras possíveis do número anunciado — lado da PEÇA e
    passo do MÓDULO — não podem valer ao mesmo tempo no catálogo de um mesmo
    fabricante. Então `pastilhas_por_placa` e `passo_de_fabrica_cm` ficam null,
    com o motivo escrito, e a régua **reprova** quem os preencher.
  - **Peso unitário — e aqui o próprio catálogo se entrega.** Dividindo peso da
    caixa pela metragem sai um kg/m², que se compara com o teto físico do vidro
    maciço (espessura × densidade). A linha Cristal de 4 mm dá 8,9 e 9,4 kg/m²
    contra teto de 10,0: cabe, e a folga é a junta. A linha Strip de 6 mm dá
    **16,9 contra teto de 15,0 — passa do teto**, o que só pode ser embalagem,
    tela e papel contados junto. Portanto **peso de caixa não vira peso de
    produto em tela nenhuma**, e o item fica no banco com `divergencias` e
    `resolucao` escritas em vez de ser descartado: descartar o caso que não
    fecha é apagar a prova.

- **O DEFEITO QUE ESTE BLOCO ENCONTROU NA PRÓPRIA RÉGUA, e que só podia aparecer
  agora.** O `validar-banco.py` checava o passo de fábrica com
  `lado_anunciado_cm / raiz(N)` — o lado da **pastilha** no lugar do lado da
  **placa**. Com o exemplo do próprio `especificacao-calculadoras.md` (placa
  30×30 com 225 pastilhas → passo 2,00 cm) a conta certa é 30/raiz(225); a que
  estava escrita dava 1/15 = 0,07 cm. **Nunca disparou porque a categoria
  pastilha tinha zero itens** — função de portão que nunca rodou é função morta,
  a mesma família que a Robometria nomeou em 11/09. Consertado, e a geometria do
  `esquema-banco.json` ganhou os campos que a fórmula precisava
  (`placa_lado_a_cm`, `placa_lado_b_cm`, `formato`), mais a recusa de aplicar
  L/raiz(N) em placa que não é quadrada — o caso da linha Strip, 28,6 × 31,2.

- **A CASCA 1.8.0, e por que o banco foi publicado nesta passada.** Option que
  nenhuma página lê é caminho morto, e caminho morto envelhece calado. Então
  `materiais-pastilhas` entra em `cdm_casca_numeros()` junto de colas e rejuntes
  **na mesma revisão**: o cartão "Pastilhas e tesselas" do Guia deixa de servir
  um zero digitado, a tabela do "Como sabemos" ganha a linha e a frase passa a
  nomear as **três** categorias — item que a soma conta e a frase não nomeia é a
  prestação de contas pela metade que o despacho da Sentinela de 12/09 fechou nas
  ferramentas. **Nenhuma URL nova:** `/materiais/pastilhas/` continua sem página
  (16.5 pede 3 filhas de nível 3), e o cartão só vira link quando a página
  existir — quem decide isso é `cdm_casca_url_se_existir()`, não a lista.

- **VERIFICAÇÃO.** `ferramentas/validar-pastilhas.py`, **139 afirmações, 0
  falha**, um processo por item, com a régua escrita à mão no próprio arquivo e
  nunca lida do banco que ela mede. Ela fez duas descobertas que a leitura não
  faria: (a) **o catálogo não tem uma regra única de arredondamento** — a caixa
  da Fosca cobre 2,086583 m² e sai "2,086" num SKU (corte) e "2,09" no irmão
  (arredondamento); uma régua que exigisse uma das duas reprovaria metade da
  linha sem haver erro de dado, e uma que aceitasse tolerância frouxa não mediria
  nada, então ela aceita **exatamente** as duas operações e **diz qual foi usada
  em cada item**; (b) a aritmética das fichas fecha na terceira casa em todos os
  10, o que é o que sustenta que os três números de cada ficha são do mesmo
  produto. `ferramentas/mutacoes-pastilhas.py`: **12 escritas, 12 reprovadas**, e
  **6 delas nenhum portão antigo viu** — entre elas a mutação que "produz o
  mundo", promovendo o distribuidor a fabricante, que sem tocar em mais nada faz
  1,5 cm passar de zero para um elegível.

- **A COBERTURA POR TAMANHO, que é o eixo pelo qual a F1 escolhe pastilha**, e é
  o número que este bloco deixa para o próximo: dos quatro tamanhos que a
  ferramenta oferece, só **um** chega aos 3 elegíveis da seção 14.3 — 2,5×2,5 com
  3; 2×2 com 2; **1×1 com ZERO** e irregular com zero. E 1×1 é o tamanho de **7
  das 12 linhas** da tabela pré-renderizada da F1: ele não aparece em catálogo de
  fabricante nenhum, só em armarinho e marketplace, vendido **a peso** ("100
  gramas") ou por contagem solta — nível 6, que sustenta preço e nada mais. É a
  mesma pendência da conversão grama↔peça vista pelo outro lado.

- **Receita:** 20 dos 20 itens do banco esperam link de afiliado e 20 estão sem
  imagem (eram 10 e 10; os 10 novos entram todos assim, e nenhuma foto foi
  colhida porque o egresso não alcança os domínios). Pauta da seção 17:
  `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

- **NO AR, 21h58Z, em UM disparo do Sync:** `/status` na revisão 15, igual à do
  manifest; 7 itens aplicados. `ferramentas/conferir-no-ar.py` passou de 334 para
  **339 afirmações, 0 falha**, porque ganhou a seção que este bloco tornou
  necessária: **a prestação de contas do banco medida no HTML servido.** A frase
  do Guia publica um total e a repartição dele, e agora tem TRÊS parcelas em vez
  de duas — no ar ela diz "20 itens de fabricante, sendo 5 colas, 5 rejuntes e 10
  pastilhas, e 20 deles ainda esperam link". A régua não lê a frase do snippet:
  lê os **arquivos de banco do repositório**, um a um, e cobra quatro coisas
  distintas — o total servido bate com a soma dos arquivos; as parcelas somam o
  total que **a própria frase** publica (defeito diferente do primeiro: uma frase
  pode estar internamente certa e desatualizada, e foi o outro caso que pôs no ar
  "hoje 10 dos 5 itens"); **toda categoria com arquivo de banco é nomeada** na
  frase, que é o que impede a próxima categoria de entrar na soma e ficar fora do
  texto; e o número de itens esperando link bate com os cabeçalhos. Testada por
  negação antes de ser dada por boa: com o banco adulterado para 9 pastilhas, as
  três afirmações que deviam cair caíram.

12/09/2026 23:20Z — BLOCO 4d, O CORTE DO DESPACHO: A ILHA TEM UM ATELIÊ

- **Por que este bloco e não a ordem de banco que o estado anterior deixou.** O
  despacho do Raphael de 12/09, 18h20 BRT, tem prioridade MÁXIMA e prazo, e o prazo
  é amanhã: ele vai à casa dos pais no domingo 13/09 ensinar a própria mãe a
  cadastrar as peças dela. É a primeira vez que alguém de fora da máquina vai usar o
  que esta fábrica constrói, e é a mãe dele. A seção 18.1 diz que despacho aberto do
  Raphael vence qualquer rotação; a execução das 21h26Z tinha subido a prioridade da
  ilha para 1 sem escrever despacho, mas o despacho estava em `dados/despachos.md`,
  aberto, com prioridade máxima.

- **Dois snippets novos, e a separação não é organização — é o Sync desembarcando um
  sem o outro.** Se o painel tiver defeito, a loja no ar não cai com ele; se a loja
  mudar, ela não perde o acesso.
  - `snippets/clubedomosaico-loja.php` **1.0.0** = snippet **#9** (criado pelo Sync):
    CPT `peca`, taxonomias `colecao` e `tecnica`, a ficha pública em `/loja/<slug>/`,
    a vitrine com foto e o endpoint de cópia da seção 24.
    sha256: `769be91f7e43...`
  - `snippets/clubedomosaico-atelie.php` **1.0.1** = snippet **#10**: papel `artesa`,
    a usuária e o e-mail de acesso, `/atelie/` com login, lista e formulário.
  - `snippets/clubedomosaico-casca.php` **1.9.0**: UMA linha de mudança, o filtro
    `cdm_vitrine_de_pecas`.
  Manifest na revisão **17**; `/status` conferido às 23h13Z (revisão 16) e de novo
  depois do conserto de 1.0.1.

- **OS CINCO ITENS DO CORTE SAÍRAM.** (1) CPT `peca` com `show_ui` FALSE — ela nunca
  vê o wp-admin, e isso é requisito escrito dele — mais o papel `artesa` com sete
  capacidades e o bloqueio duplo; (2) a usuária criada e **o e-mail de acesso enviado
  às 23h13m23s Z**; (3) `/atelie/` com login e tela inicial; (4) o formulário de peça
  em uma tela, no celular; (5) a ficha pública com `Product`+`Offer` e a `/loja/`
  listando. **Uma URL nova**, `/atelie/`, que é `noindex`: a ilha vai de 11 para 12
  páginas publicadas e continua com 11 no índice.

- **O que ficou FORA, por escrito no próprio despacho:** o formulário "Verificar
  disponibilidade" e o CPT `lead_peca` (adendo 3 de 11/09), a aba Interessados, a
  exportação CSV, "Meus dados", o feed do Merchant Center e as páginas de técnica e
  de coleção.

- **A METADE DO PORTÃO QUE A FUNDAÇÃO NÃO CUMPRE, e por que fabricar um jeito seria
  pior que não cumprir.** O despacho manda entrar em `/atelie/` como `artesa` e
  cadastrar uma peça de teste. A senha dela **não existe** em lugar nenhum a que a
  nuvem tenha acesso: o snippet gera uma senha aleatória e a descarta sem imprimir em
  log, e-mail ou option, e o que chega a ela é um link na caixa dela. Gravar a senha
  ou criar um segundo acesso para "poder testar" quebraria a única coisa que protege
  a conta de uma pessoa de verdade. O portão foi partido em duas metades
  **declaradas** no cabeçalho do `teste-atelie.php`, e a metade da LARGUra — os 360
  px que o despacho escreve dentro do portão — foi cumprida num Chromium de verdade,
  porque essa uma máquina mede melhor que um humano.

- **A senha é criada em `/atelie/` e não no `wp-login.php`** — único desvio
  consciente da especificação de 10/09, e a favor dela: o fluxo nativo manda o link
  para uma tela com a marca do WordPress e um medidor de força de senha, que é a
  definição literal do que o portão reprova. A CHAVE continua nativa
  (`check_password_reset_key` e `reset_password`); a TELA é a nossa, com o logo dela,
  e ao terminar ela já entra logada.

- **Reordenar foto é botão ◀ ▶ e não arrastar-e-soltar**, contra o que a
  especificação pedia, por duas razões que valem mais que a especificação: arrastar
  depende de JavaScript (portão 22.8) e de precisão de dedo, e ela vai cadastrar de
  um celular.

- **O QUE OS PORTÕES ACHARAM, e nenhum foi achado lendo código:**
  1. **O `teste-casca` reprovou o painel, e estava certo.** Ele cobrava que a ÚNICA
     página fora do índice fosse a camada de prova. O painel sai do índice por outro
     motivo, e as duas razões exigem tratamentos OPOSTOS — a de prova TEM de ser
     citada por outra página, esta NÃO pode ser citada por nenhuma. Nasceu a camada
     `privada`, declarada no markup e cobrada nas duas direções. A exceção pelo nome
     do slug foi recusada: seria a heurística por vizinhança que a seção 8 proíbe.
  2. **Dois filtros que eu escrevi e ninguém aplicava**, achados antes de rodar uma
     linha: um em `cdm_vitrine_de_pecas` que a casca não aplicava, e um em
     `clubedomosaico_status` que o Sync não aplica porque **ele se pula a si mesmo por
     desenho**. Portão que nunca roda é função morta. O primeiro virou filtro de
     verdade na casca (a única mudança da 1.9.0), o segundo virou rota pública.
  3. **A direção da foto num campo escondido.** Campo `hidden` é enviado seja qual
     for o botão apertado, então o botão "para frente" mandava "para trás" junto e a
     foto andava para o lado errado. Virou `value` do próprio botão, e a mutação 22 é
     esse defeito escrito de volta.
  4. **Os botões de foto tinham 38 px** — achado pelo medidor de navegador a 360 px,
     e invisível em leitura de código e no HTML servido, porque só o motor de layout
     sabe o tamanho que o botão ficou tendo. São os menores do painel e os que ela
     mais vai apertar com o dedo. Viraram 44, na versão **1.0.1**, depois de a 1.0.0
     já estar no ar.
  5. **O canonical da BANCADA** dizia `/vaso-azul/` e o site diz
     `/loja/vaso-azul/` — defeito da bancada, mesma família de "a bancada e o site
     lendo fontes diferentes para o mesmo campo".
  6. **A description abria cinco frases em minúscula depois de ponto**, visto ao
     renderizar a primeira ficha, não em revisão de código.
  7. **O piso de tamanho de página do `teste-loja` estava cravado em 40 KB**,
     calibrado na F2 que carrega uma ferramenta inteira, e REPROVAVA fichas corretas
     de 26 KB. Passou a ser DERIVADO de `/contato/` na mesma bancada: piso inventado
     reprova o certo.
  8. **Código morto que a mutação expôs:** um `str_replace` de `%0D%0A` que nunca
     podia disparar, porque `rawurlencode` de `\n` já devolve `%0A`. Saiu do snippet,
     e a mutação saiu com ele.
  9. **NO AR, e este foi o mais humilhante:** o conferidor contou 6 cartões de peça
     numa Loja com ZERO peça publicada, e os 6 eram os seletores da própria folha de
     estilo. É literalmente o erro que a seção 8 nomeia — medir no HTML inteiro em vez
     de no CORPO — cometido por quem tinha acabado de escrever uma bancada que faz
     isso certo. A bancada media no corpo, o conferidor no ar não, e **nada obrigava
     os dois a concordarem**.
  10. **Três réguas minhas erradas no medidor de navegador:** o piso de 200
     caracteres de corpo, emprestado da regra de página fina que existe para página
     de ÍNDICE, reprovava a tela de entrar, a lista e a de criar senha — as três
     estão certas, porque tela de ação boa tem pouco texto; e duas réguas do painel
     aplicadas na FICHA da peça, que não tem formulário (o botão dela é um link
     `wa.me`) e que mostra foto grande e título na primeira tela, exatamente o que o
     `DESIGN.md` manda. **Apertar o portão errado reprova o desenho certo** — é a
     mesma lição que a Aquametria escreveu em 12/09 sobre catálogo e ficha.
  11. **O `/loja/<peça>/` na tabela do `ARVORE.md`** foi reprovado pelo portão da
     casca, com razão: ele cobra que toda linha daquela tabela exista no código, e
     molde não é página. Foi para a prosa da seção 3b.

- **VERIFICAÇÃO, 0 falha.** `teste-casca` 546 (era 539); `teste-loja` **140, novo**,
  com 72 estados da ficha em processo próprio; `teste-atelie` **209, novo**, com 9
  telas em processo próprio; `teste-navegador-atelie.mjs` **91 medições, novo**, em 6
  páginas × 5 larguras num Chromium de verdade, com um contexto de
  `javaScriptEnabled: false` para medir a 22.8 de verdade; `teste-f1` 67, `teste-f2`
  72, `teste-prestacao-rejunte` 5 sobre 720 estados, `conferir-cobertura` 128,
  `validar-banco` e `validar-pastilhas` aprovados, `php -l` em tudo (com `<?php`
  prefixado, porque o snippet desta ilha nasce sem a tag).

- **MUTAÇÕES.** `mutacoes-loja` **23 de 23** reprovadas, **22 que só o portão novo
  pega**; `mutacoes-atelie` **26 de 26**, **23 que só o novo pega**. E **quatro
  passaram na primeira passada**, as quatro lacunas reais do meu portão: duas porque
  ele media TELAS e nunca DISPARAVA os ganchos (`admin_init` e o filtro da barra não
  aparecem em HTML nenhum), uma porque a varredura da senha NOMEAVA dois lugares onde
  procurar e a mutação gravou num terceiro, e uma porque eu conferia a função de
  mascarar o e-mail sem conferir se a rota a CHAMAVA. As nove baterias antigas
  rodadas inteiras, nenhuma inerte: árvore 20, cobertura 14, f1 27, f2 20, ga4 14,
  pastilhas 12, prestação 11, rejunte 12, voz-e-cabeça 24.

- **NO AR.** `/status` na revisão 16 igual à do manifest às 23h13Z, em UM disparo, 9
  itens aplicados, snippets #9 e #10 criados pelo Sync; e a revisão 17 depois do
  conserto de 1.0.1. `conferir-atelie-no-ar.py` **novo, 33 afirmações, 0 falha, 1
  pulada**: `/atelie/` em 200 servindo a tela de entrar, com `noindex`, FORA do
  sitemap (varrido pelo índice e pelos sub-mapas), ZERO links para ela nas oito
  páginas públicas, e o corpo sem dizer "WordPress", "wp-admin" ou "wp-login" uma
  vez; a rota RECUSANDO sem token (401) **antes** de ser usada com token; as sete
  capacidades presentes e NENHUMA das oito proibidas; o e-mail MASCARADO na resposta.
  A pulada é a ficha da peça, porque não há peça publicada — e esse é o estado certo
  hoje. `conferir-no-ar.py` também rodado: 339 afirmações, 0 falha.

- **O QUE FALTA, E SÓ UM HUMANO FAZ:** confirmar que o e-mail **chegou** na caixa de
  mina196@hotmail.com. `wp_mail` devolveu true, o que diz que o servidor **aceitou** a
  mensagem, não que ela passou do filtro de spam da Hotmail — e a linha 178 do
  `PROMPT.md` manda tratar queda em spam como **bloqueio da ilha**. E o dedo dela na
  tela.

- **A option `cdm_whatsapp` continua VAZIA**, e por isso a ficha da peça serve, no
  lugar do botão, a frase de que o contato ainda não foi publicado — em vez de um
  número inventado. É o primeiro item da fila e é de UMA linha.

- **Próximo passo, com ordem e motivo:** (a) a option `cdm_whatsapp`, que é o que
  transforma a ficha da peça em venda e não depende de bloco nenhum; (b) o adendo 3
  inteiro (`lead_peca`, notificação por e-mail, aba Interessados, CSV), que era o
  corte de hoje e volta à fila agora que o painel está de pé; (c) a ordem de BANCO
  que o estado anterior deixou e que continua valendo — fechar 2×2 na categoria
  pastilha, que está a UM item dos 3 da 14.3, depois a vitrine de pastilha da F1,
  depois a categoria cola.

- **ESTA EXECUÇÃO FOI O CASO QUE PRODUZIU A SEÇÃO 1.1 DO CONTRATO**, escrita por OUTRA
  execução enquanto esta trabalhava, e o registro dela é útil aqui porque ela nos
  salvou: o bloco durou 65 minutos, a reserva de 22h25Z venceu a janela de 40 minutos
  do passo 3, e uma quarta execução da Fundação teria pegado esta ilha por estar
  "livre" pela letra da regra. Se tivesse pegado, teria rodado o item 2 do despacho e
  mandado um **segundo e-mail de acesso para a mãe do Raphael** — e o segundo
  invalida o link do primeiro, na véspera do dia marcado. Ela não pegou porque
  escreveu a regra antes de agir: reserva vencida se reconfere no git, e commit na
  pasta da ilha nos últimos 40 minutos significa ilha VIVA.
  **A 1.1 também manda quem passa de 40 minutos reescrever `executando_desde` no
  próximo commit, e esta execução NÃO fez isso** — a regra não existia quando ela
  começou, e o commit intermediário das 23h13Z manteve o relógio de 22h25Z. Fica
  escrito para a próxima: renovar é uma linha, e é o que faz a execução seguinte não
  precisar do git para saber.

- **Segundo desembarque, e o que ele provou de quebra:** a revisão 17 subiu às 23h28Z
  com a casca do painel em 1.0.1, e o `/atelie/` no ar serve `min-height:2.75rem` nos
  botões de foto. E a rota de conferência mostrou `tentativas: 1` com a MESMA hora de
  envio — ou seja, **o segundo Sync não reenviou o e-mail de acesso**. A guarda por
  option funcionou exatamente onde precisava funcionar: e-mail repetido para a Hotmail
  é o caminho mais curto para a caixa de spam, e caixa de spam aqui é uma pessoa
  esperando na frente do filho sem conseguir entrar.

13/09/2026 11:56Z — ADENDO 3 ENTREGUE: os leads da Loja, e tres defeitos herdados que sairam junto

**O BLOCO.** O adendo 3 de 11/09/2026 — o formulario "Verificar disponibilidade",
o CPT `lead_peca`, a notificacao por e-mail, a aba Interessados e a exportacao
CSV — ficou FORA do corte do despacho de 12/09 **por escrito**, e voltou a fila
agora que o painel esta de pe. Saiu inteiro. Snippet novo
`clubedomosaico-leads.php` 1.0.0 (snippet #11, criado pelo Sync), `loja` 1.1.0,
`atelie` 1.1.0, manifest na revisao 18, `/status` conferido as 11h56Z **em UM
disparo**, 10 itens aplicados.

**O QUE MUDOU NA FICHA DA PECA.** O botao principal deixou de ser um `wa.me`
direto e passou a ser "Verificar disponibilidade": um `<details>` que abre um
formulario de **dois campos** — nome e WhatsApp, e nada mais, como o adendo
manda ("Sem e-mail, sem CEP") — com o texto de consentimento e o link para
`/privacidade/`. Envia, grava o lead, manda o aviso para
`mina196@hotmail.com` com um botao que abre a conversa **com o cliente**,
mensagem ja escrita, e volta para a peca dizendo "Pronto, {nome}!".

**AS SETE DECISOES, e a cicatriz que cada uma evita** (estao inteiras no
cabecalho do snippet; aqui o resumo):

1. **Terceiro snippet, nao um pedaco da Loja.** O Sync desembarca um sem o
   outro — e este e o primeiro arquivo desta ilha que guarda DADO DE PESSOA.
2. **A Loja aplica `cdm_peca_acao`, e ele e aplicado de verdade.** A cicatriz e
   de 12/09, aqui mesmo: dois `add_filter` sem ninguem do outro lado. Por isso
   os portoes medem os DOIS lados — que a Loja CHAMA, e que o que volta aparece
   no corpo servido. Sem o snippet de Leads no ar, a ficha volta ao que servia
   ontem, e nao quebra.
3. **Funciona com o JavaScript desligado** (22.8). O unico script e a mascara do
   telefone, e ela e enfeite: quem canoniza e o PHP.
4. **O nome da pessoa nao viaja na URL.** O POST guarda a confirmacao num
   transient de 10 minutos e redireciona com uma CHAVE aleatoria — o nome nao
   entra no historico, no Referer nem no log de acesso, e quem nao enviou nada
   nao consegue fabricar a tela de "enviado".
5. **O estado com parametro sai `noindex`**, pela mesma razao da F2.
6. **O lead NAO vai para o repositorio.** A copia da secao 24 para a PECA e o
   endpoint `/v1/pecas`; para o LEAD e o CSV dentro do painel, na mao dela. Nao
   ha rota REST de lead — e o portao mede a AUSENCIA, no banco e no ar.
7. **A aba nao cria capacidade nova.** As mesmas sete de ontem: quem pode editar
   as pecas pode ver quem perguntou por elas.

**O DEFEITO QUE O PORTAO PEGOU ANTES DO AR, e a forma dele vale mais que o
conserto.** `cdm_leads_nome_da_artesa()` nasceu lendo o `first_name` da usuaria e
descartando o valor quando ele fosse a palavra "artesa" — uma **lista de palavras
proibidas**, exatamente a heuristica por vizinhanca que a secao 8 do contrato
proibe. Falhou na primeira medicao pelo motivo mais previsivel: o que o snippet
do Atelie grava ali e `Artesã`, com til e cedilha, e nenhuma lista de palavras
acerta a grafia de um texto de espera que ela nao escreveu. A mensagem teria dito
**"Aqui é Artesã"** para uma cliente de verdade. A saida nao foi uma lista melhor:
o nome publico passou a ser **DECLARADO** na option `cdm_artesa_nome`, que nasce
vazia — e vazia significa uma coisa so, que a identidade de `identidade/artesa/`
ainda nao chegou, que e o mesmo estado que o `PROMPT.md` ja manda a pagina Sobre
respeitar.

**O QUE O NAVEGADOR ACHOU, e nenhum apareceria em leitura de codigo.** (a) O
botao "Quero esta peca" saia com **43 px** — um pixel abaixo do alvo de toque,
o mesmo defeito dos botoes de foto do painel em 12/09 e do mesmo jeito, porque so
o motor de layout sabe a altura que o botao ficou tendo. (b) O `select` de estado
da aba saia com 34 px e fonte de 15 px — abaixo de 16 px o iPhone da zoom sozinho
ao tocar no campo e a tela pula. (c) **A aba Interessados vazia nao tinha uma
unica acao**: uma tela sem saida, e o portao a chamou de beco. Ganhou "+ Nova
peca" e "Ver minhas pecas".

**TRES REGUAS DO NAVEGADOR MEDIAM A COISA ERRADA, e as tres teriam reprovado
codigo certo.** (1) `getBoundingClientRect()` de um elemento dentro de um
`<details>` FECHADO **nao devolve zero** neste Chromium — o conteudo e escondido
por `content-visibility`, que pula a pintura e preserva a caixa; medindo altura,
"antes" e "depois" davam o mesmo numero. Quem decide e `details.open`, e ele e a
prova da 22.8 porque o clique acontece num contexto com o JavaScript
**desligado**. (2) O alvo de toque era medido no proprio campo, e o alvo de um
checkbox e o **rotulo** que o liga; e um honeypot, que esta fora da vista, fora do
teclado e fora do leitor de tela, tem caixa de layout e era cobrado. As duas
exclusoes sao ESTRUTURAIS, declaradas no markup — nunca pelo nome do campo. (3)
"existe formulario E todo formulario POSTa" era uma afirmacao so, e reprovou a aba
vazia, que legitimamente nao tem formulario nenhum. Virou duas: todo formulario
PRESENTE POSTa, e a tela tem pelo menos um lugar onde agir.

**OS TRES DEFEITOS HERDADOS, achados ao rodar os portoes ANTES de construir
(secao 18.5).** A execucao das 02h33Z de 13/09 gravou os links de afiliado e nao
rodou portao nenhum:

- **DOIS BANCOS ESTAVAM COMMITADOS FORA DO MANIFEST.** `materiais-colas.json` e
  `materiais-rejuntes.json` divergiam do `sha256` do manifest desde 12/09 — os
  **dez links de afiliado estavam no repositorio e nao estavam no ar**. E a secao
  4 na forma mais pura: o site fica para tras em silencio. O manifest deste bloco
  os levou junto, e o `/status` na revisao 18 e a prova.
- **O PROGRAMA DO MERCADO LIVRE ESTAVA GRAVADO COMO `mercado_livre`** e o
  esquema declara `mercadolivre`. O `validar-banco.py` reprovava; ele nao tinha
  sido rodado. Corrigido no banco, que e o lado errado — o esquema e a
  declaracao.
- **AS REGUAS DA F1 E DA F2 MEDIAM UM MUNDO COM ZERO LINK.** Elas cobravam a
  frase "Link de loja em breve" no corpo da ancora, e isso era verdade so
  enquanto NENHUM item tivesse link. Na noite em que as dez colas e rejuntes
  ganharam link, as duas reprovaram **sem defeito nenhum embaixo** — a ilha tinha
  melhorado e a regua chamou isso de erro. E a familia que a Aquametria nomeou em
  12/09: **regua que depende de um caso raro do banco morre no dia em que o banco
  melhora.** As tres (bancada da F1, bancada da F2 e a conferencia no ar) passaram
  a medir o COMPORTAMENTO nos dois lados — item sem link reserva o lugar, item com
  link serve o botao patrocinado —, e a bancada ganhou um mundo produzido de
  proposito (`sem_links=1`) para poder medir o lado que o banco de hoje nao tem.

**VERIFICACAO NA BANCADA, 0 falha:** teste-leads **175 NOVO** (8 estados de
pagina, um processo cada), teste-loja 147 (era 140), teste-atelie 209,
teste-casca 546, teste-f1 70 (era 67), teste-f2 74 (era 72),
teste-prestacao-rejunte 5 sobre 720 estados, conferir-cobertura 128,
validar-banco aprovado, validar-pastilhas aprovado, `php -l` em tudo.
**NAVEGADOR:** teste-navegador-atelie **124 medicoes** em 7 paginas x 5 larguras,
0 falha, 0 px de rolagem lateral em todas.
**MUTACOES:** mutacoes-leads **36 de 36 reprovadas, 34 que so o portao novo
pega**. Sete delas sao de PRIVACIDADE — o nome na URL, o IP em texto puro, o nome
no titulo do registro, o tipo publico, o tipo na REST, o tipo na busca, a copia
para o Raphael sem option — porque trava de privacidade que ninguem quebra de
proposito e trava que ninguem sabe se funciona. **QUATRO PASSARAM NA PRIMEIRA
PASSADA, e eram quatro buracos reais do meu portao:** o IP guardado em texto puro
(o portao media que o limite funcionava e nao COM O QUE ele o fazia), o e-mail que
falha apagando o lead (o stub da bancada esquecia de apagar, entao a contagem nao
mudava), a acao da aba sem conferir capacidade (o portao media a TELA e nunca as
ACOES) e o despacho de um estado que ninguem registrou como aba (so mensuravel
PRODUZINDO um atendente intrometido).

**NO AR as 11h56Z, em UM disparo:** `/status` na revisao 18, igual a do manifest,
10 itens aplicados, snippet #11 criado. `conferir-no-ar.py` 339 afirmacoes, 0
falha, as 11 URLs intactas. `conferir-atelie-no-ar.py` 37 afirmacoes (era 33), 0
falha, 2 puladas — e as sete capacidades do papel `artesa` continuam sendo
exatamente sete, com nenhuma das oito proibidas, que era a razao da decisao 7.
Medido no ar tambem: a folha do snippet de Leads sai no `/atelie/` (ele esta
ATIVO) e `/v1/leads`, `/v1/lead_peca` e `/v1/interessados` respondem **404** —
lead nao sai por endpoint.

**O QUE NAO FOI MEDIDO NO AR, e e pulada declarada, nao aprovada:** o formulario
so existe em pagina de peca e **nao ha peca publicada**. Ele esta medido na
bancada, em 8 estados, e no navegador a 360 px; no ar, so quando a artesa
publicar a primeira peca. Esta escrito assim no proprio `conferir-atelie-no-ar.py`.

**UMA CONSEQUENCIA QUE VALE DIZER:** a option `cdm_whatsapp` **deixou de decidir
se a peca tem como ser pedida**. Ela estava vazia e por isso a ficha servia a
frase de que o contato nao foi publicado; agora o caminho de venda e o
formulario, que nao depende de numero nenhum. O item "a option de uma linha"
sai da lista do que trava a venda — continua util para um botao direto no
futuro, mas nao bloqueia mais nada.

**PROXIMO, com ordem e motivo:** (a) **"Meus dados"** dentro do painel, que e o
que torna a option `cdm_email_leads` editavel por ela e fecha o unico pedaco do
adendo 3 que ficou em codigo — a option existe e funciona, mas so por
`update_option`; (b) a ordem de BANCO que o estado anterior ja deixava: fechar
2x2 na categoria pastilha, que esta a UM item dos 3 da 14.3, depois a vitrine de
pastilha da F1, depois a categoria cola; (c) o feed do Merchant Center, que
**depende de haver peca publicada** e por isso nao e escolha de fila e sim de
espera. E um item que so um humano fecha, o mesmo de ontem: confirmar que o
e-mail de acesso CHEGOU na caixa da Hotmail.

**A REVISÃO 19, no ar às 12h16Z, e por que houve um segundo desembarque.** Foram **dois disparos**: o primeiro leu do `raw` um manifest ainda na revisão 18 (o cache é por caminho, seção 4), e o segundo, um minuto depois, aplicou os 10 itens. `/status` na 19, `conferir-no-ar.py` 339 afirmações e `conferir-atelie-no-ar.py` 37, zero falha nos dois. Três coisas só
apareceram depois de o primeiro estar no ar:

- **O CSV podia ser EXECUTADO pela planilha dela.** O campo `nome` é digitado por
  qualquer pessoa que abra a ficha de uma peça na internet, e planilha trata
  célula que começa por `=`, `+`, `-` ou `@` como **fórmula** — um nome escrito
  como `=HYPERLINK(...)` vira um link clicável dentro do arquivo que a artesã
  abre. As aspas do CSV protegem a **coluna**, não a leitura; o que protege é um
  apóstrofo na frente. Duas mutações novas medem os dois erros possíveis: não
  escapar, e escapar tudo (que devolve o verde e quebra a leitura).
- **O `From: contato@` que o adendo pede aponta para uma caixa que não existe.**
  A mesma linha do adendo diz que a casca "precisa criar a conta `contato@` no
  cPanel OU garantir SPF/DKIM", e isso é do Raphael e não foi feito. Muita
  hospedagem recusa enviar com remetente que não é caixa local, e aí o lead fica
  gravado e a artesã não fica sabendo dele até abrir o painel. Agora, se a
  primeira tentativa falhar, vai uma **segunda com o remetente padrão do
  WordPress** — o mesmo que entregou o e-mail de acesso dela em 12/09 — e o
  caminho usado fica **gravado no lead**, para a ronda ver que o `contato@` não
  está de pé em vez de descobrir pela ausência.
- **Não deu para conferir SPF/DKIM daqui.** `dns.google` e `cloudflare-dns.com`
  respondem **403 ao CONNECT por política de egresso**, em duas passadas cada,
  como a 20.2 manda testar antes de declarar. Não é intermitência de túnel: é a
  lista Personalizada da rede das rotinas, que tem os domínios das ilhas,
  `googleapis` e `github`, e nenhum resolvedor de DNS. Fica declarado, não
  presumido.

**Números finais, com as duas revisões dentro.** Bancada: teste-leads **184**,
teste-loja 147, teste-atelie 209, teste-casca 546, teste-f1 70, teste-f2 74,
teste-prestacao-rejunte 5 sobre 720 estados, conferir-cobertura 128 — 0 falha em
todas. Navegador: 124 medições em 7 páginas × 5 larguras, 0 falha. Mutações:
**mutacoes-leads 40 de 40 reprovadas, 38 que só o portão novo pega, 0 inertes**.
**As onze baterias antigas rodadas inteiras, para provar que nenhuma virou
inerte: árvore 20, ateliê 26, cobertura 14, F1 27, F2 20, GA4 14, loja 23,
pastilhas 12, prestação 11, rejunte 12 e voz-e-cabeça 24 — 203 mutações, 203
reprovadas, 0 passaram, 0 inertes.**

## 13/09/2026 — "MEUS DADOS": a aba onde ela manda no que só existia em código

Ateliê **1.2.0**, Leads **1.1.0**, manifest na **revisão 20**. **Nenhuma URL
nova.** Fecha o último pedaço do adendo 3 que tinha ficado por fazer — a option
`cdm_email_leads` existia, funcionava, e só a Fundação podia mexer nela — e
cumpre a linha do `PROMPT.md` que promete desde 10/09 que "ela troca a senha em
Meus dados dentro do painel".

**A ABA TEM TRÊS SEÇÕES, e a divisão entre elas é a decisão do bloco.** "Seu
acesso" mostra o e-mail da conta **como texto**; "Sua senha" troca a senha; e
"Avisos de interessados" — que **não é deste arquivo** — traz o endereço para
onde vai o aviso e o nome que assina a mensagem do WhatsApp.

- **A TROCA DE SENHA NÃO PEDE A SENHA ATUAL, e isso é escolha e não esquecimento.**
  O WordPress não pede na tela de perfil dele, e aqui a razão é mais forte que a
  dele: **ela entrou na conta por um link de e-mail** e pode legitimamente não
  saber a senha que quer trocar. Pedi-la trancaria a porta justamente para quem
  tem a chave. O que protege a ação é sessão autenticada + nonce, e o custo de
  errar para este lado é conhecido e menor — quem já está dentro da sessão dela
  já podia publicar, apagar e exportar os interessados. Se um dia houver mais de
  uma pessoa no ateliê, a linha se reabre; está escrita no cabeçalho do snippet.

- **O E-MAIL DA CONTA APARECE E NÃO SE EDITA.** É o endereço para onde vai o link
  de recuperar a senha; um dedo errado num teclado de celular a deixaria de fora
  da própria conta, sem ninguém do outro lado para socorrer no domingo. Aparecer
  responde a única pergunta que ela vai fazer sobre esse endereço ("para onde vai
  o link?"); virar campo é risco sem ganho. O portão mede as duas metades: que o
  endereço **aparece** e que **não existe `<input>` com ele**.

- **QUEM LÊ A OPTION É QUEM A ESCREVE — e por isso nasceu um terceiro ponto de
  extensão.** `cdm_email_leads` e `cdm_artesa_nome` são lidas **só** pelo snippet
  de Leads, então os campos delas nascem lá e chegam à tela pelo filtro
  `cdm_atelie_meus_dados`, do mesmo jeito e pela mesma razão que a aba
  "Interessados" chega pelo `cdm_atelie_abas`: **o Sync desembarca um snippet sem
  o outro**, e uma tela que promete um campo cujo dono não está no ar é a
  divergência silenciosa que esta ilha já pagou duas vezes. **Cada seção é um
  formulário próprio**, com nonce e gravação próprios — nada de um caminho de
  salvar compartilhado onde o campo de um dono sobrescreve o do outro por
  descuido. E a borda do cartão não é enfeite: é o que diz onde um formulário
  acaba e o outro começa, para ela não apertar "Trocar a senha" achando que
  salvou os dois.

- **O VAZIO CONTINUA SIGNIFICANDO O QUE SIGNIFICAVA, e agora a tela DIZ isso.**
  E-mail em branco é "avise no endereço padrão"; nome em branco é "a identidade
  da artesã ainda não chegou", e a mensagem assina "do Clube do Mosaico". Os dois
  campos escrevem embaixo o que o branco faz e **qual é o estado de hoje**, em
  vez de deixar ela adivinhar se esqueceram de preencher ou se é assim mesmo. E
  branco **grava** branco em vez de ser ignorado: sem isso ela não teria como
  desfazer um endereço digitado por engano.

- **E-MAIL INVÁLIDO NÃO DERRUBA O QUE FUNCIONAVA.** O antigo fica de pé e a tela
  diz que não deu. A direção sai da assimetria de custo, como manda a seção 10:
  trocar um endereço que recebe por um que não existe é o aviso do interessado
  sumindo sem ninguém perceber.

**A GUARDA DE `defined()` NO SNIPPET DE LEADS não é paranoia, é a ordem do
desembarque:** este arquivo pode chegar ao ar minutos antes do Ateliê 1.2.0, que
é quem declara `CDM_ATELIE_ABA_DADOS`. Sem ela, um POST daquela ação levaria erro
fatal do PHP no lugar da tela. Com ela, a ação simplesmente não existe enquanto o
outro lado não chega — que é o mesmo que já acontece com a seção, porque o filtro
não é aplicado.

**O QUE A BANCADA GANHOU, e ela é a metade que dá sentido ao filtro:** o
`render-para-teste.php` passou a **produzir o mundo em que um snippet não
desembarcou** (`sem_leads=1`), na mesma família do `sem_links` de 13/09. "A tela
não promete o que o dono ausente não entrega" é uma afirmação que **só pode ser
medida com o dono ausente**, e não há como produzir essa ausência lendo código —
só deixando de carregar o arquivo. O portão mede os dois lados: com o Leads no
ar a seção aparece; sem ele, ela some **e a troca de senha continua inteira**.

**DUAS MUTAÇÕES PASSARAM NA PRIMEIRA PASSADA, e as duas eram buraco de portão —
não de código.** É o resultado do teste, não um detalhe:

1. **`34 quem não está logada troca a senha dela`.** Todas as afirmações da aba
   rodavam **com a artesã logada**, e por isso nenhuma delas via a guarda de
   sessão cair. A mutação removeu `is_user_logged_in()` e `current_user_can()` da
   ação e ficou verde. **Um portão que só mede o caminho feliz da recusa mede a
   recusa errada.** O conserto foi medir a ação deslogada e logada-sem-capacidade
   — o nonce da bancada é determinístico, e é isso que torna a medição possível:
   quem está de fora consegue calculá-lo, que é exatamente o mundo contra o qual
   a capacidade protege.
2. **`48 a tela para de dizer para onde os avisos vão hoje`.** A régua cobrava o
   endereço na tela **com a option vazia** — e aí "hoje" e "o padrão" são o mesmo
   texto, então a frase "deixe em branco para usar mina196@..." satisfazia a
   régua sem a tela dizer nada sobre o estado atual. **Régua que só distingue
   quando os dois valores diferem tem de ser medida onde eles diferem:** a
   afirmação mudou de lugar e passou a rodar depois de gravar um endereço
   diferente do padrão.

**E UMA MUTAÇÃO ANTIGA TINHA VIRADO INERTE nesta mesma passada** — a `24 o script
volta para dentro do shortcode`. O alvo dela era "o `</form></div>` que vem antes
do `add_shortcode`", e o Ateliê 1.2.0 pôs duas funções entre um e outro. **Alvo
de mutação que depende da vizinhança morre no dia em que o vizinho se muda**, e
mutação inerte não mede nada — ela conta como "passou". Reescrita com âncora no
próprio fim do formulário da peça.

**UM DEFEITO MENOR CONSERTADO DE PASSAGEM:** o piso de 8 caracteres da senha
estava escrito três vezes na tela de criar senha (o `strlen`, dois `minlength` e
a frase de ajuda). Virou `CDM_ATELIE_SENHA_MINIMA`, uma vez, para as duas telas
não poderem divergir.

**VERIFICAÇÃO NA BANCADA, 0 falha:** `teste-atelie` **251** (era 209),
`teste-leads` **210** (era 184), `teste-casca` 546, `teste-loja` 147, `teste-f1`
70, `teste-f2` 74, `teste-prestacao-rejunte` 5 sobre 720 estados,
`conferir-cobertura` 128, `validar-banco` aprovado, `validar-pastilhas` aprovado,
`php -l` em tudo. **NAVEGADOR:** `teste-navegador-atelie` **128 medições em 8
páginas × 5 larguras**, 0 falha, 0 px de rolagem — a tela nova passou de primeira
no alvo de toque e na fonte de 16 px, porque reusa `.cdm-at-campo` e
`.cdm-at-botao` em vez de inventar botão.

**MUTAÇÕES: 262 em 12 baterias, 262 reprovadas, 0 passaram, 0 inertes.**
`mutacoes-atelie` de 26 para **37** e `mutacoes-leads` de 40 para **48** — as 19
novas atacam a aba pelas duas famílias de sempre: as que **abrem porta** (o nonce
que some, a capacidade que some, o piso da senha que cai, o segundo campo que
deixa de ser conferido) e as que **vazam segredo** (a senha no endereço de volta,
o e-mail da conta virando campo). As dez baterias antigas rodadas inteiras:
árvore 20, cobertura 14, F1 27, F2 20, GA4 14, loja 23, pastilhas 12, prestação
11, rejunte 12 e voz-e-cabeça 24.

**NO AR às 14h04Z, e foram TRÊS revisões e quatro disparos, por um motivo que não
era o cache.** `/status` na **revisão 22** igual à do manifest, 10 aplicados,
`conferir-no-ar.py` **339** afirmações e `conferir-atelie-no-ar.py` **45** (era
37), 0 falha nos dois, as 11 URLs intactas, e as sete capacidades do papel
`artesa` continuam sendo exatamente sete. A marca do código novo foi medida **no
corpo servido**, não no log do Sync: `.cdm-at-secao` só existe no Ateliê 1.2.0, e
a folha do painel sai no `/atelie/` mesmo deslogada — é a diferença entre "o
manifest diz que subiu" e "o site está servindo". Medido também que
`?estado=meus-dados` deslogada cai na tela de entrar, sai `noindex`, e **não
serve** `trocar_senha`, `cdm_email_leads`, `cdm_artesa_nome` nem o e-mail dela.

**PULADA DECLARADA, não aprovada:** a aba só existe para quem entrou, e a
Fundação não entra — a senha da artesã não existe para a nuvem, por desenho. O
que está medido no ar é a versão servida e a ausência do que não pode vazar; o
dedo dela na tela de 360 px continua sendo a metade do domingo.

### O QUE ESTA EXECUÇÃO ENCONTROU E NÃO ERA DELA — dois commits mexeram no banco desta ilha enquanto ela estava reservada

**Isto é o achado mais caro do bloco, e não é sobre "Meus dados".** Os commits
`4e69738` (a escada do link de compra, seção 25 nova do contrato) e `35412c1` (o
`url_produto` do teste de vida) chegaram ao `main` às 13h36Z e depois, editaram
`dados/materiais-colas.json` e `dados/materiais-rejuntes.json` e **não tocaram no
`manifest.json`**. Lido no `/status`, três vezes seguidas: `"materiais-colas:
sha256 divergente — não aplicado"`. **Os dez links novos, o `url_produto` e as
três fotos estavam no repositório e fora do ar** — a seção 4 na forma mais pura, e
a segunda vez no mesmo dia (a execução das 11h56Z tinha achado exatamente isto).

O `4e69738` também deixou **11 erros de esquema**, nenhum dos quais sobreviveria a
um `validar-banco.py` de segundos: `mercado_livre` em três itens onde o
vocabulário declara `mercadolivre` (**o mesmo defeito de 12/09, de volta**),
`imagem` sem `largura`/`altura`, e os contadores de cabeçalho dizendo "nenhuma
foto foi coletada" com três fotos coletadas.

**A LARGURA E A ALTURA DA FOTO: havia dois caminhos, e o cômodo era o errado.** O
feed de afiliado da Shopee — que a seção 25.3 nomeia como a fonte legítima da foto
— **não declara dimensão**. O caminho cômodo era afrouxar o esquema para aceitar
os dois campos ausentes; e ele estaria errado, porque os dois campos existem para
a página **reservar a caixa da foto antes de ela chegar**, e caixa sem medida é o
salto de layout que a seção 22.4 chama de defeito de desempenho. O outro caminho
era **medir**: `cf.shopee.com.br` responde 200 em duas passadas (medido, não
presumido), e nasceu `ferramentas/medir-imagens.py`, que lê a dimensão do
cabeçalho do arquivo servido — JPEG, PNG e WebP, sem biblioteca, porque instalar
Pillow para ler dois inteiros seria trocar uma linha de código por um risco de
ambiente. **1024×1024, 1024×1024 e 768×768, lidas.** `800x800` digitado porque
"foto de e-commerce costuma ser quadrada" passaria no validador exatamente igual —
e seria chute com cara de dado, que é o defeito mais caro que esta fábrica tem.
Download que falha vira `FALHOU` e o item **continua reprovando**: rede fechada
nunca vira número.

**E a metade que não tem conserto do lado da Fundação está em `dados/despachos.md`:**
a reserva por commit da seção 1 funcionou como escrito — esta execução perdeu a
robometria e a aquametria e pegou a clubedomosaico às 13h19Z —, e **uma terceira
sessão editou o banco desta ilha assim mesmo**. A reserva protege contra quem a
lê; não existe para quem entra pela porta do dado. Hoje custou dois rebases e duas
revisões a mais; o custo caro é o do próprio 1.1, dois trabalhos concorrentes na
ilha da artesã no dia em que ela ia aprender a usar o painel. É decisão do
Raphael.

**PRÓXIMO, com ordem e motivo:** (a) a ordem de BANCO que o estado anterior já
deixava — fechar 2×2 na categoria pastilha, que está a UM item dos 3 da 14.3,
depois a vitrine de pastilha da F1, depois a categoria cola; (b) o `url_busca` do
degrau 3 e o segundo link discreto que a seção 25.2 manda pôr embaixo do botão —
os campos chegaram ao banco e **a página ainda não os serve**, então hoje a escada
existe no dado e não na tela; (c) o feed do Merchant Center, que depende de haver
peça publicada e por isso não é escolha de fila e sim de espera. O que só um
humano fecha continua o mesmo: confirmar que o e-mail de acesso CHEGOU na caixa da
Hotmail, e o `contato@clubedomosaico.com.br` que ainda não existe como caixa.

---

## 13/09/2026, 15h18–15h45Z — A ESCADA DA SEÇÃO 25 CHEGA À TELA (f2 1.2.0, manifest revisão 23)

**Terceira ilha tentada nesta execução, e isso é a seção 1 funcionando.** A aquametria foi
reservada às 15h16Z e a robometria às 15h17Z por outras duas execuções; o push da minha
reserva da aquametria foi recusado por cerca de um minuto. O passo 5 manda voltar ao passo 2
e escolher outra ilha, e foi o que aconteceu — sem force push, sem atropelo.

**O bloco é o item (b) que a execução anterior deixou escrito**, palavra por palavra: *"o
`url_busca` do degrau 3 e o segundo link discreto que a seção 25.2 manda pôr embaixo do
botão — os campos chegaram ao banco e a página ainda não os serve, então hoje a escada
existe no dado e não na tela."* Ele venceu a ordem de BANCO que vinha antes na fila porque a
25.2 não é preferência de fila: ela diz que **não existe item publicável sem piso** e que a
página com piso no banco **nunca** diz "em breve". Dez itens estavam nesse estado.

### O que mudou na tela

Nasce `cdm_f2_compra_html()`, dona dos três estados do bloco de compra. **A F1 reusa o mesmo
cartão**, então os dois lugares que servem produto nesta ilha desceram a escada de uma vez:

1. **Com ficha** — a ficha é o botão ("Ver na loja") e a busca desce para a linha discreta
   "Veja todos disponíveis aqui", palavra por palavra como a 25.2 a escreve. As duas convivem
   de propósito: ficha converte melhor, e a busca é a saída de quem chegou num anúncio
   esgotado. O degrau 3 é justamente o que quebrou quatro links em doze horas em 13/09.
2. **Só com busca** — a busca **sobe e vira o botão**, com texto próprio: "Ver as opções na
   loja". O texto muda junto com o papel, e não por estilo: o botão abre uma **lista**, e
   prometer "Ver na loja" ali seria o leitor clicar esperando a ficha do que a página acabou
   de recomendar.
3. **Sem nada** — sobra "Link de loja em breve", e ele deixa de ser estado de espera para ser
   **defeito contado**.

**Por que é função própria e não um `if` dentro do cartão:** a escada é regra do Arquipélago
e o cartão é desenho da ilha. Quem for servir a vitrine de pastilha da F1, a ficha do Guia ou
a página da peça **chama a função** em vez de reescrever quatro degraus que discordariam em
silêncio. O portão mede isso contando a **classe emitida** nos snippets — e não a frase
legível, porque a primeira versão dessa régua contou a frase e reprovou o próprio comentário
que a explica.

### Os três mundos produzidos, e por que `sem_links=1` mudou de significado

O banco de hoje só produz o estado 1, então medir os outros dois no banco de hoje seria medir
o caminho que nenhum cartão percorre — verde com a função quebrada, e o dia em que importasse
seria o dia em que um link morresse.

`sem_links=1` **apaga a ficha e deixa o piso de pé**, que é exatamente o estado 2. Até a
1.1.0 esse mundo produzia "em breve"; depois da 1.2.0, produzir "em breve" nele **é o
defeito**. A afirmação antiga reprovou na primeira rodada, e essa reprovação é a mudança
funcionando. Nasceu `sem_piso=1` para o vazio de verdade.

**A ordem das três réguas importa, e é o que as torna três:** (a) sozinha passaria numa
função que ignora a ficha e serve só a busca; (b) sozinha passaria numa que serve a busca por
cima da ficha; e (c) pega o erro mais provável de quem escreve isto com pressa — deixar o "em
breve" no lugar do piso —, **o único que (a) e (b) aprovariam juntas.**

### O banco aprende o que a seção 25 criou

O esquema não conhecia `url_produto`, `url_busca`, `url_busca_produto`, `degrau` nem
`conferido_em`, e a observação dele ainda mandava a página dizer "em breve" e declarava que
gerar link *"é da Sentinela estratégica, no navegador, e nunca da Fundação"*. As duas frases
são **anteriores à 25.2** e foram **reescritas, não acrescentadas**: deixadas ali, o esquema
contradiria o campo vizinho, e contradição no dado é pior que lacuna porque tem cara de
decisão. O `validar-banco.py` passa a exigir `url_produto` de quem tem link (25.4-b: link
cuja saúde ninguém consegue conferir), a cobrar o degrau, e a **contar** os itens sem piso num
campo novo de cabeçalho, `itens_sem_piso`, reconferido contra o arquivo.

**Os dez sem piso são as pastilhas, e o motivo é medido e não suposto.** Gerar o link de busca
exige a **sessão logada** do painel de afiliado da Shopee, que mora no navegador do Raphael.
Desta nuvem o `custom_link` responde **200 em duas passadas** e serve uma casca de JavaScript
**sem o formulário** — zero ocorrência de `custom_link` e de `sub_id` no HTML servido. **Não é
bloqueio de rede** (a seção 4 manda testar duas vezes antes de chamar de bloqueio, e o teste
foi feito): é falta de sessão, e criar conta ou tocar na conta dele está fora do que esta
camada faz. **Não virou erro duro do validador de propósito** — portão vermelho que ninguém
consegue fechar é portão que se aprende a ignorar; contado e declarado, ele é o número que a
ilha reporta em todo bloco, que foi exatamente o desenho que fez os dez links nascerem em
13/09. **No dia em que os dez `url_busca` forem colados, nenhuma linha de código muda.**

### Uma mutação antiga tinha virado inerte em cada bateria, e inerte conta como passou

O alvo das duas era a linha que **abria** o `<span>` do bloco de compra dentro do cartão, e a
refatoração mudou o vizinho: a abertura desceu para a função nova. As duas acharam zero
ocorrência e foram contadas como PASSOU. É a mesma família da mutação 24 desta ilha em 12/09
— **alvo que depende da vizinhança morre quando o vizinho se muda.** As duas apontam agora
para a **chamada** da função, que é o que governa a ordem hoje.

### Um achado de outra ilha, fechado

A ronda da Aquametria de 13/09 escreveu, por não haver outro canal, que o endpoint de cópia da
seção 24 desta ilha **existia** e devolvia 401, mas que o nome do parâmetro de autenticação
não estava documentado em lugar nenhum — então a cópia da 24 não acontecia e não ia acontecer.
O parâmetro é `token` e o valor é **o mesmo token do Sync**. A URL completa e literal entrou em
"Endpoints desta ilha", conferida desta nuvem: HTTP 200, `{"total":0,"pecas":[]}`. **Zero peça
é resposta, não falha** — o `dados/pecas.json` nasce no dia em que a artesã cadastrar a
primeira.

### A regra nova que subiu para o contrato (seção 1.1)

A 1.1 manda descartar a ilha com commit na pasta nos últimos 40 minutos e **não diz commit de
quem**. Lida ao pé da letra, ela manda a Fundação ignorar por 40 minutos exatamente a ilha que
a **Sentinela** acabou de tocar — que é a ilha com despacho novo, a primeira da 18.1. As duas
regras se contradiziam. O que a 1.1 mede é **execução da Fundação viva**, e `executando_desde:
null` já prova que não há bloco em andamento, **porque a reserva é escrita antes do trabalho**.

### Verificação

**Bancada, 0 falha:** `teste-f2` 87 afirmações (era 74), `teste-f1` 72 (era 70), `teste-casca`
546, `teste-loja` 147, `teste-leads` 211, `teste-atelie`, `teste-prestacao-rejunte` 5 sobre
720 estados, `conferir-cobertura` 128, `validar-banco` APROVADO, `php -l` em tudo.
**Mutações:** f2 **26 de 26** reprovadas, f1 **27 de 27**, **0 inertes** nas duas depois do
conserto dos dois alvos. **Navegador:** 63 medições em 9 páginas × 6 larguras, 0 px de
rolagem, console limpo — e entre as nove está o **mundo produzido em que a busca é o botão**,
porque alvo de toque de botão novo não se mede no mundo onde ele não aparece.

**No ar às 15h40Z, em UM disparo:** `/status` na revisão **23**, igual à do `manifest.json`, 10
aplicados; `conferir-no-ar` **351 afirmações, 0 falha**, com a escada medida **cartão a cartão
no HTML servido** (6 cartões na F2 e 2 na F1, todos com as duas portas) e a marca do código
novo — a classe `cdm-f2-busca` — no corpo servido, que é a diferença entre "o manifest diz que
subiu" e "o site está servindo".

**A primeira versão dessa régua no ar reprovou a página certa**, e vale registrar: ela comparou
as linhas discretas da tela com o número de itens do **banco**, e a âncora serve 6 cartões de
um banco de 10 porque publica um **caso de referência**, não o catálogo. Régua de página medida
com régua de banco. O banco continua na medição, mas no papel certo: dizer o que a tela **não
pode** ter.

**PRÓXIMO, com ordem e motivo:** (1) a ordem de BANCO que já estava escrita e **agora não tem
mais nada na frente** — fechar 2×2 na categoria pastilha, que está a UM item dos 3 da 14.3,
depois a vitrine de pastilha da F1, que já nasce com a escada pronta, depois a categoria cola;
(2) os dez `url_busca` das pastilhas, no minuto em que houver sessão — é copiar e colar no
banco, sem uma linha de código; (3) o feed do Merchant Center, que é espera e não escolha de
fila. O que só um humano fecha continua o mesmo: confirmar que o e-mail de acesso chegou na
caixa da Hotmail, e o `contato@clubedomosaico.com.br` que ainda não existe como caixa.

13/09/2026 17:50Z — O 2×2 FECHA O MÍNIMO DA 14.3, E A FAIXA SOBRE A QUAL A COBERTURA ERA PUBLICADA ESTAVA FALTANDO UM TAMANHO

- **Por que este bloco.** Era a ordem de banco que o estado anterior deixou escrita
  e que não tinha mais nada na frente: fechar 2×2 na categoria pastilha, que estava
  a UM item dos 3 da seção 14.3. Nenhum despacho aberto nesta ilha, nenhum defeito
  da 19.1 registrado pela ronda. **Nenhuma URL nova, nenhum snippet reescrito,
  nenhuma página criada** — manifest na revisão **24**.

- **As três fichas que o bloco 3d deixou pela metade entraram inteiras**, e a
  pendência `pastilha-fichas-colhidas-pela-metade` está FECHADA: **A37** (2×2,
  placa 32,3, 3 mm, 20 placas, 2,086 m², 13 kg), **102** (2,5×2,5, placa 31,7,
  4 mm, 20 placas, 2,01 m², 18 kg) e **IC02** (2,3×2,3, placa 30,0, 8 mm, 10
  placas, 0,9 m², 16 kg). O banco vai de 10 para **13** itens, e **a A37 é o
  terceiro elegível de 2×2**: o tamanho passa de 2 para 3 e cumpre o mínimo da
  14.3. Era o único buraco de cobertura desta ilha que dependia de coleta e não
  de decisão.

- **Coleta.** Busca restrita ao domínio, **duas passadas por SKU** com consultas
  escritas de forma diferente e **nenhuma delas carregando um valor** — as duas
  pediram os rótulos da ficha. As três voltaram idênticas nas duas. O egresso foi
  remedido antes, como a 20.2 manda: `glassmosaic.com.br` e `www.pastilhart.com.br`
  em 000 por `connect_rejected` (política) em duas passadas, com
  `clubedomosaico.com.br` em 200 nas mesmas duas. Por isso `conferir_no_pdf: true`
  nos três, como nos dez anteriores.

- **O ACHADO DO BLOCO NÃO É DO DADO — É DO PRÓPRIO PORTÃO, e ele muda o que a ilha
  vinha publicando sobre si mesma.** O `validar-pastilhas.py` carregava os tamanhos
  da F1 numa constante de **quatro** linhas, com o comentário "os tamanhos que a F1
  oferece". **A F1 oferece cinco:** `cdm_f1_pastilhas_disponiveis()` serve 1×1,
  **1,5×1,5**, 2×2, 2,5×2,5 e o caquinho irregular. A cópia nasceu certa e
  envelheceu calada.

  **O custo não era cosmético.** A seção 14.3 manda varrer "a faixa de entrada de
  cada ferramenta de ponta a ponta", e a cobertura saía publicada sobre quatro
  linhas de uma faixa de cinco: **um tamanho que a ferramenta serve nunca apareceu
  no relatório do buraco.** E logo esse — 1,5 cm é o lado do `pastilhart-af1500`, o
  único item do banco sustentado por distribuidor (nível 5). A **mutação 07** desta
  bateria diz, com todas as letras, que promover o distribuidor "faz 1,5 cm passar
  de zero para um elegível": uma afirmação sobre uma linha que o relatório não
  tinha. Ela reprovava pelo nível na régua por item, e a outra metade nunca foi
  medida.

- **Nasce `ferramentas/tamanhos-da-f1.php`**, irmão do `faixa-da-f2.php`. Ele **não
  lê o código: provoca a ferramenta.** As chaves saem de
  `cdm_f1_pastilhas_disponiveis()`, que é a declaração da própria F1, e cada uma
  passa por `cdm_f1_entrada()` — a MESMA função que saneia a consulta de quem
  visita — para provar que sobrevive ao saneamento. As duas metades falham por
  motivos diferentes: tamanho que a tela lista e o saneamento derruba é tamanho que
  a ferramenta não aceita. **8 afirmações, com a borda dentro delas:** uma chave
  inventada tem de ser recusada, e o padrão do saneamento tem de ser um tamanho que
  a tela lista. É a mesma família do "número de tela nasce contado, nunca digitado"
  da seção 8 e da lista de tipos que a Robometria tirou de dentro da régua hoje de
  manhã pela seção 26: **lista dentro da régua envelhece calada, e o sintoma é o
  portão verde.**

- **As duas primeiras mutações de CÓDIGO desta bateria (13 e 14)** nasceram junto, e
  existem porque a bateria só sabia mexer no banco — portão que só mede o dado não
  vê o defeito que mora na régua. A 13 faz o padrão do saneamento cair num tamanho
  que a tela não lista; a 14 faz o saneamento aceitar qualquer chave. As duas
  **produzem um mundo que o banco não tem como produzir**, que é o que a seção 8
  exige de quem escreve régua nova, e as duas reprovaram.

- **O que os três itens ensinaram sobre o catálogo.** (1) O **102** tem a mesma
  pastilha anunciada de 2,5 cm dos três K e placa de **31,7** contra 30,0 — prova,
  dentro do catálogo de um fabricante só, de que **o lado da placa não se deduz do
  lado da pastilha**; quem completasse um campo pelo vizinho de mesmo tamanho
  erraria 1,7 cm por placa. O próprio endereço o classifica em `uncategorized`,
  então o nome comercial não carrega linha: inventar uma seria atribuir ao
  fabricante uma classificação que ele não publicou. (2) O **IC02** é o único item
  do banco cuja aritmética de ficha fecha **exata** (10 × 30 × 30 = 0,90 m², sem
  corte nem arredondamento), e o lado dele, 2,3 cm, não é nenhum dos cinco do
  seletor — como já acontecia com 3,0, 1,5 e 1,2. Virou pendência nova,
  `pastilha-tamanho-fora-do-seletor-da-f1`: **6 dos 13 itens** têm lado que a F1 não
  oferece, e o que eles medem não é defeito de coleta, é o quanto o seletor é mais
  pobre que o mercado. (3) A **A37** fecha a metragem por CORTE (2,086) e a irmã A61
  por ARREDONDAMENTO (2,09) na mesma caixa — a régua já aceitava exatamente as duas
  operações e diz qual foi usada em cada item, então a A37 entrou sem uma linha nova
  de tolerância.

- **Receita, e o número PIOROU de propósito.** `itens_sem_piso` sobe de 10 para
  **13**, contado do arquivo pelo validador e nunca digitado. Os três novos entram
  sem `url_busca` pelo mesmo motivo medido ontem e hoje: gerar o link de busca exige
  a **sessão logada** do painel de afiliado da Shopee, que mora no navegador do
  Raphael, e isso não é bloqueio de rede. **Inventar um endereço para o contador não
  subir seria trocar defeito contado por defeito escondido.** No dia em que os treze
  forem colados, nenhuma linha de código muda — a escada de ontem já serve os três
  estados.

- **VERIFICAÇÃO NA BANCADA, 0 falha:** `validar-pastilhas` **189 afirmações** (era
  139) em 13 itens, um processo cada, 8 delas vindas da faixa medida na F1;
  `validar-banco` APROVADO com 23 materiais; `cobertura` 128; `teste-casca` 546;
  `teste-f2` 87; `teste-f1` 72; `teste-loja`, `teste-leads` e `teste-atelie`
  aprovados; `prestacao-rejunte` 5 sobre 720 estados; `php -l` em tudo.
  **MUTAÇÕES:** pastilhas **14 de 14** (12 no banco e as 2 novas no código), 0
  inertes; cobertura **14 de 14**, 9 que só a varredura vê; f1 **27 de 27** e f2
  **26 de 26**, 0 inertes nas duas — as antigas rodadas inteiras para provar que
  nenhuma morreu com o banco maior. **NAVEGADOR:** 63 medições em 9 páginas × 6
  larguras, 0 px de rolagem, console limpo, e a passada com o JavaScript
  **desligado** (portão 22.8) inteira.

- **As baterias que esta execução NÃO rodou, ditas pelo nome:** prestação, árvore,
  loja, leads, ateliê, rejunte, voz-e-cabeça e ga4. Elas medem superfícies que este
  bloco não tocou, e a de prestação sozinha passa de vinte minutos (720 estados por
  mutação). Ficam para quem mexer naquelas superfícies. Dizer quais é o mínimo:
  "rodei as mutações" sem a lista é a mesma promessa vazia que o número digitado.

- **NO AR às 17h47Z, em DOIS disparos**, e o primeiro é o caso que a seção 4
  documenta: às 17h42Z o Sync leu um manifest ainda na revisão 23 **enquanto já
  baixava o banco novo** e recusou com `"materiais-pastilhas: sha256 divergente —
  não aplicado"`. A trava fez o que devia; o segundo disparo aplicou. `/status` na
  **revisão 24**, igual à do manifest. `conferir-no-ar` **351 afirmações, 0 falha**,
  com a prestação de contas do banco medida no HTML SERVIDO: a página do Guia serve
  **"23 itens de fabricante, sendo 5 colas, 5 rejuntes e 13 pastilhas, e 13 deles
  ainda esperam link"** — total batendo com a soma dos arquivos do repositório,
  parcelas somando o total que a própria frase publica, e toda categoria com arquivo
  de banco nomeada.

- **ABERTO E NOMEADO:** (a) os 13 `url_busca` das pastilhas, que dependem da sessão
  do painel da Shopee; (b) `url_busca_produto` em 10 de 10 itens com busca (25.4-b)
  — a URL crua se perdeu e não se recupera sem clicar; (c) **1×1 continua com ZERO**
  e é o tamanho de 7 das 12 linhas da tabela pré-renderizada da F1 — não existe em
  catálogo de fabricante, só em armarinho e marketplace vendido a peso, e é a
  pendência mais cara da categoria; (d) **1,5×1,5 aparece pela primeira vez no
  relatório e sai com ZERO**, porque o único item daquele lado é de nível 5; (e)
  peças por placa segue null nos 13, agora com 9 de 13 sem divisão inteira; (f) a
  ilha não tem peça publicada, então ficha, formulário no ar e feed do Merchant
  Center continuam esperando a artesã; (g) `contato@clubedomosaico.com.br` ainda não
  existe como caixa. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0
  na fila, 0 recusados.

- **PRÓXIMO, com ordem e motivo:** (1) **a vitrine de pastilha da F1**, que agora não
  tem mais nada na frente e ficou mais barata do que estava —
  `cdm_f1_pastilha_sem_banco_html()` ainda diz "ainda não temos as pastilhas no
  nosso banco", o 2×2 e o 2,5×2,5 têm os 3 elegíveis da 14.3 para servir, a escada
  de compra já está pronta, e a faixa por onde ela vai filtrar agora é **medida** em
  vez de digitada; falta decidir o que a tela diz nos três tamanhos que continuam em
  zero e nos 6 itens cujo lado o seletor não oferece, que é a pendência nova; (2) a
  categoria **cola**, que é a faixa mais descoberta da ilha (45 estados varridos, 0
  com o mínimo, teto de 2 elegíveis); (3) os 13 `url_busca`, no minuto em que houver
  sessão — é copiar e colar no banco, sem uma linha de código.

---

## 13/09/2026, 19h17–20hZ — A VITRINE DE PASTILHA DA F1 (f1 1.2.0, manifest revisão 25)

**Terceira ilha tentada nesta execução, de novo, e de novo é a seção 1 funcionando.** A
aquametria foi reservada às 19h18Z e a robometria às 19h16Z por outras duas execuções — o meu
push da reserva da aquametria foi recusado por cerca de um minuto, e o da robometria também.
O passo 5 manda voltar ao passo 2 e escolher a próxima da ordem; sem force push, sem atropelo.
Antes de escolher, conferi os três `PROMPT.md`: **nenhuma ilha tem despacho aberto para a
Fundação** (a 18.1 não se aplicou), então valeu a rotação normal da seção 1.

**O bloco é o item (1) que a execução anterior desta ilha deixou escrito**, e ele não tinha
mais nada na frente: *"a vitrine de pastilha da F1 — `cdm_f1_pastilha_sem_banco_html()` ainda
diz 'ainda não temos as pastilhas no nosso banco'"*.

### O defeito era de OMISSÃO, e ele tinha data

A frase nasceu verdadeira em 11/09/2026. Em **12/09** o bloco 3d gravou dez pastilhas; em
**13/09** entraram outras três. O arquivo está com `publicar: true` desde 12/09, a casca lê
ele em `cdm_casca_numeros()` e o cartão do Guia publica a contagem — e **nenhuma linha de
código da F1 abria o banco**. Dado no banco e tela sem leitor é o mesmo defeito que a F2
tinha com o `url_busca` até 13/09 de manhã; aqui era mais caro, porque esta é a ferramenta
cuja pergunta **é** "quantas pastilhas comprar", e ela respondia sem ter o que vender.

### O que decide uma pastilha não é o que decide uma cola

Primeira coisa que o código novo declara, e é a cicatriz da "categoria nova herda a régua da
antiga em silêncio" (seção 8), que esta ilha já pagou quando o primeiro rejunte fez as 18
células da cola falharem de uma vez. A cola se escolhe por base × ambiente; o rejunte, pela
folga. **A pastilha entrou no banco pela GEOMETRIA** — o próprio arquivo diz isso e diz por
quê: o fabricante não nomeia substrato nem ambiente na ficha dela. Então a elegibilidade tem
três travas, **nesta ordem**, e a ordem é o que faz cada frase de recusa poder ser verdadeira:

1. **o LADO** (o que a pessoa escolheu, ou digitou no caquinho irregular);
2. **o FORMATO** — o seletor oferece pastilha quadrada e o banco tem um strip retangular de
   1,2 cm. Quem cai aqui já passou pelo lado, então "o lado é o mesmo" não é suposição;
3. **a FONTE** — nível <= 3 pela escada do esquema. É por isso que **1,5 cm sai com ZERO
   tendo um item**: a causa é a fonte (distribuidor), não o tamanho, e a tela diz qual das duas.

**Prestação de contas (seção 7):** as quatro listas são disjuntas e somam o banco inteiro,
contado do arquivo. Todo item aparece **uma vez** — no cartão que o recomenda ou numa linha
que diz por que ele não está. Uma frase por causa, cada uma nomeando quem caiu por ela.

### A PENDÊNCIA DO SELETOR FECHOU POR UM TERCEIRO CAMINHO — e o número dela estava errado

O banco abriu em 13/09 a pendência `pastilha-tamanho-fora-do-seletor-da-f1` dizendo **6 dos
13**. São **5**. Ela listava o AF1500 de 1,5 cm entre os lados que o seletor não tem, porque
foi escrita a partir da frase "a F1 oferece quatro tamanhos — 1x1, 2x2, 2,5x2,5 e a tessela
irregular". **A F1 oferece cinco, e o quinto é justamente 1,5 cm** — foi esse o defeito que
`ferramentas/tamanhos-da-f1.php` achou na régua de manhã, e **a prosa da pendência herdou a
mesma lista vencida no mesmo dia**. Lista digitada envelhece calada em qualquer arquivo,
inclusive num que descreve o problema. Os cinco são os três K de 3,0 cm, o ST5102 de 1,2 cm e
o IC02 de 2,3 cm, contados do cruzamento do banco com `cdm_f1_pastilhas_disponiveis()`.

A pendência propunha duas saídas e **nenhuma das duas foi tomada**: opção nova no seletor
prometeria cobertura da 14.3 que não existe, e servir tamanho aproximado seria recomendar 3,0
a quem pediu 2,5 com a conta de 2,5. Havia um terceiro caminho, e ele **já estava construído**:
o campo do **caquinho irregular** aceita qualquer lado de 0,3 a 10 cm e é o único da
ferramenta em que o lado é digitado. A vitrine casa pelo lado em milímetros, então quem digita
3 recebe os três K de 3,0 cm com a conta do próprio lado dele. A tela nomeia os lados que o
seletor não lista e manda a pessoa para lá.

### O CARTÃO FALA EM PLACA, E ISSO É ESCOLHA DECLARADA

Converter "N pastilhas" em "M placas" exigiria quantas pastilhas vêm na placa, e **nenhum dos
treze fabricantes publica**: a divisão ingênua não fecha em 9 dos 13 e, nos outros 4, fecha
exigindo folga zero — placa que não se rejunta. Área, sim, se converte sem supor nada: a
placa cobre o próprio tamanho, seja qual for o arranjo das peças dentro dela. Então o cartão
diz quantas **placas** a peça pede, com a sobra escolhida dentro e arredondando para cima
pelo mesmo motivo da contagem de peças — e a página diz, na cara, que a peça ela não converte.

### A ESCADA DA SEÇÃO 25 FOI CHAMADA, NÃO COPIADA

`cdm_f2_compra_html()` nasceu em 13/09 dizendo, no próprio comentário, que a vitrine de
pastilha da F1 a chamaria em vez de reescrevê-la. Foi o que aconteceu. Hoje os treze caem no
**terceiro** degrau — sem ficha e sem piso —, e isso é defeito declarado da 19.1, não estado
de espera: o cartão reserva o lugar, e o número está contado no banco (`itens_sem_piso: 13`).

### A TABELA PRÉ-RENDERIZADA EXISTE POR UM MOTIVO ARITMÉTICO

O estado-âncora desta página é caquinho de **1 cm**, e 1 cm tem **zero** elegível. Sem a
tabela do banco inteiro, a única URL indexada desta ferramenta — a sem parâmetro, a que o
Google e as IAs leem — **não citaria um único produto do nosso catálogo de pastilha**. A
vitrine responde a quem escolheu um lado; a tabela responde a quem só chegou. Treze linhas,
cada item uma vez, com uma coluna "está no formulário?" que publica a cobertura da 14.3 item
por item, em vez de a deixar só na bancada.

E a frase que explica o zero de 1 cm — "não aparece em catálogo de fabricante nenhum; quem
vende é armarinho e marketplace, a peso ou por peça solta" — **só sai no lado de 1 cm e só
quando ele está vazio**. Ela é verdadeira hoje, e é isso que a tornava perigosa.

### A BANCADA, E O QUE ELA ACHOU NELA MESMA

`teste-f1.php` foi de **72 para 182 afirmações**, 0 falha. A régua da classificação é escrita
**neste arquivo**, em PHP, lendo `dados/materiais-pastilhas.json` do disco — não chama nenhuma
função do snippet. A grade varre os cinco tamanhos do seletor, os três lados que só o caquinho
irregular alcança e um lado que não existe em ninguém, um processo por estado.

`mutacoes-f1.py` foi de 27 para **40 mutações, 40 reprovadas, 0 inertes**. A primeira rodada
teve **três que passaram, e as três eram resultado**:

1. **"vão maior que a moldura passa e a área fica negativa"** reprovava desde 12/09 e passou a
   escapar **por causa deste bloco**: a afirmação procurava "não fecha" no corpo INTEIRO, e a
   camada de prova nova passou a dizer que a divisão do lado da placa "não fecha" em quase
   todos os itens. A agulha foi encontrada numa seção que nada tem a ver com a recusa — o mesmo
   defeito que a seção 8 registra como "a conferência achava o texto dentro do próprio
   JSON-LD". Ela passou a medir **no bloco da resposta**. E a afirmação vizinha tinha um furo
   mais antigo: `-\d+ cm²` nunca casaria com **"-1.100 cm²"**, que é exatamente o que a página
   serve quando a guarda cai. Só pegava área negativa de três dígitos.
2. **"as placas esquecem a sobra"** passou porque a grade não pisava na borda: no vaso de
   15 × 20 a sobra de 10% não muda o número de placas, e o `ceil` engole a diferença. Nasceu a
   seção **4c**, com uma peça de 44,5 × 40 cm escolhida para a sobra atravessar o degrau (2 / 2
   / 3 placas em 0 / 10 / 20%) — e uma afirmação que cobra que os degraus sejam **diferentes**,
   senão a peça escolhida não mediria a sobra.
3. **"a frase do 1 cm passa a sair sempre"** passou porque nada media o ESCOPO dela. Ela é
   verdadeira no lado de 1 cm e seria uma afirmação sobre um mercado que ninguém olhou em
   qualquer outro lado. Agora a régua cobra que ela saia **se e somente se** o lado pedido é
   10 mm e ele está vazio.

**TRÊS MUNDOS NOVOS no `render-para-teste.php`**, e cada um existe porque o banco de hoje não
consegue produzir o caso — "todo caso que o ESQUEMA permite e o banco ainda não tem é um caso
que a régua precisa tratar hoje" (seção 8):

- **`com_piso=1`** escreve `url_busca` em quem não tem. Sem ele, a mutação que faz o cartão de
  pastilha **reimplementar** a escada em vez de chamar `cdm_f2_compra_html()` produz uma tela
  **idêntica byte a byte** — os treze estão sem piso, então os dois caminhos caem no terceiro
  degrau. A cópia só mentiria no dia em que o Raphael colasse os links, com um portão verde ao
  lado. Essa mutação reprova **só** neste mundo.
- **`strip_fraco=1`** rebaixa a fonte do único item não quadrado para nível 5, fazendo-o cair
  pelas DUAS travas. É o único jeito de provar a ORDEM declarada: com um item por balde,
  qualquer ordem produz a mesma tela.
- **`um_de_1cm=1`** clona um item para o lado de 1 cm e exige que a frase do mercado
  desapareça.

**Navegador:** 83 medições em 13 páginas × 6 larguras (360, 390, 781, 782, 783, 1200), **0 px
de rolagem lateral** nos três estados novos da F1, console limpo, contraste de 12,97:1 a
21:1, e a passada com o **JavaScript desligado** inteira (portão 22.8) — a vitrine é servida
pelo servidor e não tem uma linha de decisão em JavaScript.

**Outras baterias rodadas inteiras, 0 falha:** casca 546, f2 87, loja 147, leads 211, atelie
aprovado, cobertura 128, validar-pastilhas 189, validar-banco aprovado, `php -l` em tudo. As
que NÃO rodaram, e vale dizer quais: prestação de rejunte (720 estados, passa de vinte
minutos), árvore, rejunte, voz-e-cabeça, ga4 e as mutações de pastilhas, cobertura, f2, loja,
atelie e leads — elas medem superfícies que este bloco não tocou.

**NO AR às 19h54Z, em UM disparo.** `/status` na revisão **25**, igual à do manifest, 10
aplicados. `conferir-no-ar.py` foi de 351 para **365 afirmações, 0 falha**, medidas no HTML
SERVIDO depois do Sync — a tabela do banco com 13 linhas e os treze códigos, o estado-âncora
dizendo que não tem 1 cm com a causa, o estado de 2 cm com três cartões nomeados e o lugar do
link reservado nos três, e o caquinho irregular de 3 cm alcançando os três K que o seletor não
lista. A régua dele também é própria: os treze códigos estão escritos literais no arquivo.

**Um detalhe do próprio commit, para não parecer descuido:** o nome da pendência entre acentos
graves foi comido pelo shell na mensagem de commit, e a linha saiu "fecha a pendencia  —".
Não há force push nesta fábrica (seção 3), então a mensagem fica como está; o nome é
`pastilha-tamanho-fora-do-seletor-da-f1` e a história inteira está acima.

**ABERTO E NOMEADO, ao fim deste bloco:** (a) os **13** `url_busca` das pastilhas, que dependem
da sessão logada do painel de afiliado da Shopee — no dia em que forem colados, **nenhuma linha
de código muda**, e o `com_piso=1` já prova que a tela sabe subir o degrau; (b) `url_busca_produto`
em 10 de 10 itens com busca (25.4-b); (c) **1x1 continua com ZERO elegível** e é o tamanho de 7
das 12 linhas da tabela pré-renderizada da F1 — agora a página diz isso na cara, mas o buraco
é o mesmo e é o mais caro da categoria; (d) 1,5x1,5 sai com zero por FONTE, não por tamanho;
(e) peças por placa segue null nos 13, e é a pendência que faz o cartão falar em placa; (f) a
ilha não tem peça publicada, então ficha, formulário no ar e feed do Merchant Center continuam
esperando a artesã; (g) contato@clubedomosaico.com.br ainda não existe como caixa.

**Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

**PRÓXIMO, com ordem e motivo:** (1) **a categoria COLA**, que é a faixa mais descoberta da
ilha — 45 estados varridos, **0 com o mínimo** da 14.3, teto de 2 elegíveis; é a única
categoria em que a ferramenta responde e o banco não tem o que vender, e agora não tem mais
nada na frente. (2) **A ORDEM DAS DUAS VITRINES na F1**: hoje "Qual rejunte cabe nessa folga"
vem antes de "E onde comprar a pastilha", ordem herdada de quando o bloco da pastilha era uma
frase de espera. O H1 da página nomeia a pastilha primeiro e a resposta também; mover é
decisão de desenho e merece bloco próprio, não um `swap` no meio de outro. (3) **1x1 de
fabricante**, que é a pendência mais cara da categoria pastilha — a busca alcança os domínios,
o egresso é que não. (4) os 13 `url_busca`, no minuto em que houver sessão: é copiar e colar.

### O ACHADO QUE NÃO ERA DESTE BLOCO: o cabeçalho de estado não é YAML válido

Ao validar o próprio cabeçalho antes de fechar (porque ele ficou grande e eu quis ter certeza),
descobri que **a seção 2 do contrato manda o cabeçalho ser YAML e nada nunca conferiu que ele
PARSEIA**. Passando os três `ESTADO.md` do arquipélago por `yaml.safe_load` às 19h58Z:
**dois dos três estavam quebrados**. A causa é a mesma e nasceu do crescimento saudável do
arquivo — o `bloco_atual` passou de `"4c"` para prosa de milhares de caracteres entre aspas
duplas, e aspas duplas dentro de um escalar de aspas duplas derrubam o documento; uma barra
invertida solta também, porque `\d` é escape desconhecido em YAML de aspas duplas.

- **clubedomosaico**: estava inválido e foi consertado no mesmo commit (aspas internas viraram
  simples, e a regex citada saiu por extenso).
- **aquametria**: inválido, na coluna 1910 do `bloco_atual`. Reservada por outra execução às
  19h18Z, e a seção 3 proíbe editar ilha que não se reservou → virou **despacho** em
  `dados/despachos.md`.
- **robometria**: válido.

Ninguém tinha visto porque quem lê o cabeçalho hoje é a Fundação, com `grep` e com o olho, e as
duas coisas atravessam YAML quebrado sem reclamar. **Cabeçalho que só o olho lê é cabeçalho sem
portão.** A metade que vale para toda ilha foi escrita onde regra nova mora, uma vez: a
**seção 2 do `ARQUIPELAGO.md`**, com o comando de uma linha e a convenção de aspas simples.

13/09/2026 21:19Z — BLOCO 3e ENTREGUE: A CATEGORIA COLA GANHA OS DOIS PRODUTOS DAS FAIXAS DE ZERO, E A F2 APRENDE A CONDIÇÃO DE SUPERFÍCIE (regra 6)

**A ilha desta execução foi a terceira tentativa.** A robometria foi reservada às
21h16Z por outra execução — o push da minha reserva foi recusado por cerca de um
minuto, o passo 5 da seção 1 manda voltar ao passo 2, e nenhum force push
aconteceu. Antes de escolher, os três `PROMPT.md` foram lidos: **nenhuma ilha
tinha despacho aberto para a Fundação**, então a 18.1 não se aplicou e valeu a
rotação da seção 1. A clubedomosaico era a de `ultima_execucao` mais antiga entre
as livres (19h17Z), com prioridade 1.

**O QUE ESTE BLOCO FOI BUSCAR, e estava escrito no `ESTADO.md` desde as 19h17Z:**
a categoria COLA era a faixa mais descoberta da ilha. O censo da seção 14.3 media
**45 estados, 0 com o mínimo de 3 elegíveis, teto de 2**. Era a única categoria em
que a ferramenta responde e o banco não tinha o que vender.

## A rede, medida antes de trabalhar (seção 20.2)

`clubedomosaico.com.br` e o `/status` em 200. O egresso a fabricante segue
fechado e foi **remedido em duas passadas** antes de ser respeitado, como manda a
seção 4: `quartzolit.weber`, `tekbond.com.br`, `cascola.com.br`, `henkel.com.br`,
`bra.sika.com` e `brascola.com.br` responderam `000` nas duas, com o domínio da
ilha em 200 como controle na mesma janela. O WebFetch devolveu `EGRESS_BLOCKED`
para o mesmo domínio. **O canal que sobrou é exatamente o que a escada de fontes
do esquema chama de nível 2 e 3: busca restrita ao domínio do fabricante, sem
abrir o PDF** — e foi por ele que os dois produtos entraram.

## Os dois produtos, e por que cada um fecha uma faixa

**Tekbond Silicone Acético Maxx (BRSA005)** — o primeiro produto do banco que
pode ser **recomendado em contato permanente com água**. Até hoje essa faixa
tinha zero elegíveis nas nove bases, e a única declaração de colagem submersa da
ilha era press release de 2018 (`loctite-durepoxi`, nível 4, abaixo do mínimo de
3). A declaração de aquário e piscina está na página de produto do fabricante,
nível 3, e cumpre a regra 4 (ambiente crítico exige declaração explícita).

**Cascola Adesivo de Montagem PL500 Interior** — o primeiro indicado **sobre
plástico**. O único que falava de plástico dizia "certos tipos de plástico", que
não nomeia tipo nenhum e por isso nunca virou indicação; aqui o fabricante lista
"plásticos" sem qualificador.

**O QUE FOI RECUSADO DE PROPÓSITO, nos dois:**

- No Maxx, **vidro NÃO entrou**. É um silicone de aquário e aquário é de vidro, e
  a tentação de traduzir "fabricação e reparo de aquários" em base VIDRO é a
  heurística por vizinhança que a seção 8 proíbe. "Aquários" é aplicação e entra
  como AMBIENTE, que é o que ela mede. As outras oito bases seguem descobertas
  dentro da água, e a página diz isso.
- No PL500, a frase *"ideal para adesão de rodapés, peças decorativas, azulejos,
  ladrilhos, molduras, canaletas, cantoneiras, maquetes, mosaicos"* **não entrou
  em `indicado_para`**, embora contenha "azulejos", que o mapa traduz como BASE.
  É a lista do que se COLA, nunca a do que se cola SOBRE — o mesmo erro que este
  banco já pegou na cimentcola AC-II. **"Mosaicos" está escrito lá pelo próprio
  fabricante e mesmo assim não virou declaração de substrato: virou citação.**

## A regra 6, e por que ela precisou existir

O PL500 declara **"ao menos uma das superfícies deve ser porosa, já que o produto
seca por evaporação da água"**. Isso não é base e não é ambiente: é o **PAR de
superfícies coladas**. Sem tratá-la, a página mandaria colar pastilha de vidro em
vaso de plástico com um adesivo que não teria por onde curar — recomendar em
primeiro lugar um produto que a própria página diz não servir, que a seção 7
chama de defeito GRAVE.

Nasce a **regra 6 do esquema (versão 3)**: a primeira régua de cola que olha o
CAQUINHO. A entrada existia desde a F2 1.0.0 e nenhuma régua de cola a lia — o
mesmo defeito que a F1 tinha com o banco de pastilhas e a F2 com o `url_busca`.

**TRÊS DECISÕES DECLARADAS NO CÓDIGO:**

1. **A ordem.** A condição roda DEPOIS das cinco e ANTES da ordenação por score.
   Rodar depois da ordenação deixaria célula sem topo com elegíveis na mão: em
   `vidro` + `caquinho de espelho` o produto com condição é o PRIMEIRO colocado,
   e quem sobe no lugar dele são os dois silicones que estavam abaixo. É uma das
   cinco âncoras escritas à mão no esquema.
2. **A causa tem grupo próprio.** Quem cai pela condição não vai para o balde do
   silêncio. Não é proibição (o fabricante não proíbe) e não é silêncio (ele
   falou, e falou desta superfície). Misturar seria a mistura de causas que a
   seção 7 proíbe desde 12/09/2026, escrita nesta mesma ilha.
3. **A atribuição sai dividida ao meio (seção 26.3).** A **condição** é do
   fabricante; a classificação de **quais superfícies são porosas** é da ilha. A
   página escreve as duas metades em orações separadas — *"a Henkel escreve ao
   menos uma das superfícies deve ser porosa; quem diz que pastilha de cerâmica é
   a superfície porosa deste caso somos nós, não ela"* — e o portão mede a
   separação.

**A lista mora no esquema, nunca na régua (seção 26.2)**, com as duas direções
cobradas: a união de porosas e não porosas tem de ser IGUAL ao vocabulário, e as
duas listas disjuntas. A direção da dúvida está escrita: **na dúvida, NÃO
porosa** — cerâmica esmaltada entra como não porosa mesmo sabendo que o biscoito
por baixo do esmalte é poroso, porque quem escolhe "cerâmica ou porcelana" na F2
está colando sobre a face esmaltada.

## O ACHADO QUE QUASE FOI COMMITADO, e foi um portão que o pegou

A ficha técnica BRSA005 foi **localizada e não lida** (o PDF não abre desta
nuvem). Ela tinha sido gravada dentro de `fontes`, "para a próxima execução saber
onde ir", com o nível 2 dela. **O nível de um material é o MELHOR dos níveis das
fontes**, então aquela linha promoveu o produto inteiro de 3 para 2 sem que uma
declaração dele viesse da ficha — e a linha de prova da tela passou a atribuir a
declaração a um documento que ninguém abriu. Quem viu foi o portão de acentuação
da F2, que reprovou a palavra `tecnica` chegando à tela vinda do campo `tipo`
daquela fonte.

Seção 10 do contrato: **o nível é o do elo MAIS FRACO, e inflar o próprio nível
de fonte é o defeito mais caro numa fábrica que vende procedência.** O endereço
ficou, em campo próprio — `fonte_localizada_nao_lida` —, e nasceu a trava:
`fontes` é o que SUSTENTA o registro, e fonte que declara não sustentar campo
nenhum é recusada pelo validador com o motivo escrito.

## O OUTRO ACHADO, de carona, e ele estava numa régua

O validador cobrava etiqueta do Mercado Livre no formato `clubedomosaico-<código>`
— **uma etiqueta IMPOSSÍVEL de criar**. A seção 7 do `ARQUIPELAGO.md` foi
corrigida em 13/09/2026 MEDINDO o painel: só minúsculas e números, sem hífen, no
máximo 30 caracteres. A régua ficou para trás e aprovava os **23 registros** do
banco que carregavam a forma com hífen. Portão verde sobre um valor que não
existe do outro lado. Os 23 registros e a régua foram corrigidos no mesmo commit.

## O DEFEITO QUE ESTE BLOCO CRIOU E CONSERTOU NO AR: prosa que envelhece calada

A seção "Duas coisas que a gente ainda não responde" era **duas frases escritas à
mão**, e as duas eram exatas no dia em que nasceram. Os dois produtos as fizeram
mentir no mesmo dia — **no ar, em voz de confissão**, que é pior, porque frase de
honestidade é a última de que alguém desconfia. O conserto não foi reescrever a
prosa: a seção passou a ser **CONTADA a cada requisição**, varrendo a entrada
inteira (base × lugar × caquinho) e publicando *"esta página responde 270
combinações; em 68 delas a gente ainda não tem cola para indicar"*.

**Mais três listas digitadas caíram no mesmo bloco**, e a quarta foi pega pelo
portão que eu mesmo tinha acabado de escrever: a resposta do FAQ e a frase
*"trocando por X, ele voltaria a servir"* traziam os nomes dos caquinhos porosos
escritos à mão. Essa última é a única frase da página que diz à pessoa **o que
fazer para a peça não descolar**, e digitada ela erraria do jeito caro. As duas
passaram a sair das mesmas listas que a régua usa.

**A tabela pré-renderizada ganhou a coluna da condição.** Sem ela, a linha
"plástico, dentro de casa: use Cascola PL500" sairia servida no HTML como se
valesse sempre — e ela só vale com caquinho poroso. É a metade que um modelo de
linguagem lê sem preencher formulário, e é onde a afirmação sem escopo custa mais.

**Na casca, três números entraram na via viva**: `celulas_matriz`,
`celulas_com_saida` e `celulas_sem_saida` eram os únicos do instantâneo que
nenhuma linha recontava, e a página de metodologia — cujo único produto é o rigor
— passou a publicar que a ilha tinha duas combinações sem saída num dia em que
ela não tinha nenhuma. A frase também ganhou o ESCOPO do que ela mediu, e aponta
para a ferramenta, que tem a conta com as três dimensões.

## A verificação, em números

**Banco:** `validar-banco.py` APROVADO — 25 materiais, 18 células da F2
recomputadas, 9 do rejunte, **54 pares da regra 6 com 5 âncoras ponta a ponta**.
As 18 células da matriz foram **derivadas à mão** das declarações dos dois
produtos ANTES de o validador rodar; as 32 divergências que ele acusou bateram
uma a uma com a derivação.

**Bancada, 0 falha:** teste-f2 de 87 para **102 afirmações**, com varredura da
entrada INTEIRA — 270 estados, um processo cada —, incluindo a **prestação de
contas da cola** que a ilha nunca teve: 1.890 nomeações (7 colas contadas do
arquivo × 270 respostas), cada item em exatamente UM lado. teste-casca 546,
teste-f1 182, teste-loja 147, teste-leads 211, teste-atelie, validar-pastilhas,
prestação de rejunte (540 estados da F2 e 180 da F1), `php -l` em tudo.
`conferir-cobertura.php` **353 afirmações, 0 falha**: a régua do censo e a do
snippet dão o mesmo elegível nos 270 estados de cola e nos 60 de rejunte.

**Censo da 14.3, o número deste bloco:** a cola sai de **45 estados varridos, 0
com o mínimo, teto 2** para **270 varridos, 28 com o mínimo de 3, teto 4**. Os
com zero elegíveis são 68, e é esse o número que a página publica.

**Navegador:** a bateria rodou sobre os quatro estados novos da F2, com a passada
de JavaScript desligado inteira.

**Mutações:** a bateria rodou inteira **três vezes**, e as três passadas
produziram achado. **Quatro resultados**, e os quatro valem mais que o verde:
- Uma mutação antiga **virou INERTE** quando a assinatura de `cdm_f2_fora_html()`
  ganhou a tessela. Mutação que não morde é teste verde com outro nome; foi
  reapontada.
- Uma **PASSOU**, e o motivo era meu: eu declarei o portão errado. Ela edita o
  snippet e eu mandei o validador do banco julgá-la, e o validador não lê uma
  linha de PHP. Ganhou o portão certo, e ganhou uma **gêmea do lado do Python**,
  porque duas implementações da mesma regra precisam das duas mutações.
- A trava que ela deveria ter acionado **não existia**. A afirmação que faltava —
  *"produto proibido sai no bloco da proibição, nunca no da condição"* — nasceu e
  descobriu-se **verde sem poder falhar**: o banco tem um produto com condição e
  ele não é proibido em base nenhuma. Nasceu com ela a mutação que **produz o
  mundo**, criando o par proibido-com-condição que o banco de hoje não tem.
- Na passada seguinte, **uma segunda PASSOU**: apagar a coluna da condição da
  tabela pré-renderizada deixava o portão inteiro verde. O defeito era real e o
  `conferir-no-ar.py` o pegava — **mas defeito pego pela regra VIZINHA prova que
  ALGUMA trava existe, nunca que ESTA existe**, e é por isso que cada mutação
  deste bloco declara qual portão tem de reprová-la. Enquanto a bancada não
  medisse, a tabela podia perder a coluna e só o desembarque diria. A afirmação
  nasceu, com régua própria (o literal do fabricante lido do banco em disco), e
  a mutação foi reaplicada sozinha para ver a trava reprová-la antes da passada
  final: **6 linhas da tabela indicam produto com condição, e as 6 publicam a
  condição literal.**

**Resultado final, medido depois do fechamento e corrigido aqui: 44 mutações, 44 reprovadas,
0 passaram, 0 inertes.** A entrada acima foi escrita quando a terceira passada estava em 31 de
44, e era isso que ela dizia — o número menor, que era o medido naquele minuto. A bateria
terminou em seguida, no mesmo container, e este parágrafo é a correção. **Escrever o número
menor e corrigi-lo custa um commit; escrever 44 antes de vê-lo seria a única coisa que esta
fábrica não perdoa.**

## Receita e dívida, contadas do arquivo

7 colas no banco (eram 5). **Os dois novos nascem SEM PISO**, e isso é dívida
contada, não estado de espera: a palavra-chave de busca dos dois está escrita em
`afiliado.url_busca_produto`, e o que falta é o encurtamento, que exige a sessão
logada do painel de afiliado — medido nesta execução às 21h (o
`affiliate.shopee.com.br` serve casca de JavaScript sem sessão). **No dia da
sessão são duas colagens e nenhuma linha de código muda.** A ilha vai a 25 itens
de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem.

## Aberto e nomeado

- (a) **A matriz escrita à mão cobre 18 das 45 células de base × lugar.** As
  outras 27 são verificadas só pela varredura das páginas servidas, que mede a
  agregação e NÃO é régua independente de elegibilidade. Está dito dentro do
  próprio portão, em vez de escondido. O conserto é a matriz chegar a 45 — nunca
  o portão fingir que já mede o que não mede.
- (b) Os 15 `url_busca` dependem de uma sessão do painel da Shopee.
- (c) O egresso a fabricante segue fechado; a ficha BRSA005 está localizada e não
  lida, com o endereço guardado.
- (d) `1x1` de fabricante continua com zero elegível, e é o tamanho de 7 das 12
  linhas da tabela da F1.
- (e) A ilha não tem peça publicada, então ficha, formulário no ar e feed do
  Merchant Center esperam a artesã.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.

## UM DETALHE DO COMMIT, e desta vez ele virou regra do Arquipélago

A mensagem do commit deste bloco perdeu a palavra `fontes`: ela estava entre
crases dentro de aspas duplas, e o shell executou o que havia ali e colou a saída
vazia no lugar. A linha foi ao ar como *"saiu de \n depois que"*. **É a segunda
vez no mesmo dia e na mesma ilha** — às 19h17Z sumiu o nome de uma pendência,
pelo mesmo motivo, e a execução de então registrou o fato só aqui, no `REGISTRO`
da ilha. Registrado só aqui, o defeito repetiu.

A seção 3 proíbe force push, então as duas mensagens ficam como estão. O que
mudou é onde a lição foi escrita: **a regra nova está na seção 3 do
`ARQUIPELAGO.md`**, que é onde regra do Arquipélago mora e é lida por toda
execução de toda ilha — *crase não entra em mensagem de commit*, e a mesma
armadilha vale para `$` e `!` dentro de aspas duplas.

**PRÓXIMO, com ordem e motivo:** (1) **a matriz esperada da F2 de 18 para 45
células**, que é a independência que falta ao número que a página publica, e é o
único item aberto que este bloco criou; (2) a ordem das duas vitrines na F1, hoje
herdada de quando o bloco da pastilha era uma frase de espera; (3) `1x1` de
fabricante, a pendência mais cara da categoria pastilha; (4) os 15 `url_busca`,
no minuto em que houver sessão — e é copiar e colar.

---

# 13/09/2026, 23h18Z — A MATRIZ ESCRITA À MÃO VAI DE 18 PARA 45 CÉLULAS, E A PRIMEIRA COISA QUE ELA VÊ É UM DEFEITO NO AR

**F2 1.4.0 · esquema versão 3 · manifest revisão 27 · nenhuma URL nova, nenhuma
página criada.** Era o item (1) do PRÓXIMO da execução das 22h30Z, e o único item
aberto que aquele bloco tinha criado.

## A escolha da ilha, e ela foi a terceira tentada

Rotação da seção 1, sem despacho aberto para a Fundação em nenhum dos três
`PROMPT.md` (os três foram lidos antes de escolher, como a 18.1 manda). A
robometria era a de `ultima_execucao` mais antiga (21h16Z) e **meu push de reserva
foi recusado por cerca de um minuto** — outra execução a reservou às 23h18Z; a
aquametria caiu às 23h19Z pelo mesmo motivo. O passo 5 manda voltar ao passo 2, e
**nenhum force push aconteceu**. Sobrou a clubedomosaico, com `executando_desde:
null`, que pela **1.1** já significa que não há bloco da Fundação vivo — o git não
precisou desempatar, embora a ilha tivesse fechado bloco 6 minutos antes.

`dados/despachos.md` tem um despacho para a **FUNDAÇÃO (quem reservar a
aquametria)**: consertar o cabeçalho YAML dela. **Medido nesta execução, os três
`ESTADO.md` passam por `yaml.safe_load`** — a execução das 21h21Z da aquametria já
o cumpriu. Não é minha ilha para tocar, mas o "pronto quando" dele está satisfeito
e isso ficou escrito no despacho, com quem mediu.

## O que a dívida era, dita com o tamanho que ela tinha

A matriz `matriz_esperada_da_F2` é a **régua independente** da ferramenta: ela é
escrita à mão a partir das declarações dos fabricantes e nunca chama uma linha do
snippet, então as duas metades não erram juntas. Ela cobria **18 das 45 células**
de base × lugar. As outras 27 passavam só pela varredura das páginas servidas —
que mede a **agregação** e lê a MESMA implementação de elegibilidade dos dois
lados. Portão verde que não é régua.

**As 27 novas foram DERIVADAS À MÃO das declarações ANTES de o validador rodar uma
vez**, e a derivação ficou gravada antes da inserção. Resultado, dito com o número
que ele tem: **zero divergência** nas cinco listas das 27 — recomendados no topo,
elegíveis abaixo, proibidos, silêncio e menção com ressalva bateram produto a
produto com a recomputação. O que o validador cobrou foram **9 observações que
faltavam**, e ele estava certo: célula sem recomendação tem de dizer POR QUE, e
essa regra existia antes deste bloco.

## O ACHADO, e ele é o motivo de esta régua valer o que custa

**As 18 células antigas TODAS tinham recomendação.** Nenhuma delas era faixa
descoberta — ou seja, **a régua independente desta ilha nunca havia pisado numa
célula sem resposta**, que é justamente a metade em que a página vende honestidade
em vez de produto. Com as 45, **11 células são descobertas**, e o ramo do código
que as escreve deixou de ser código morto para o portão.

Ele estava errado, e **estava no ar**. Em quatro estados — **vidro, madeira,
alvenaria e metal em contato permanente com água** — a página servia:

> "Não temos cola para indicar em metal dentro da água. **Nenhum dos adesivos do
> nosso banco é declarado pelo próprio fabricante para esse caso** — e a gente
> prefere dizer isso a chutar o de sempre."

e, **duas seções abaixo, na mesma página**:

> "Existe menção a **Loctite Durepoxi**, mas o que sustenta isso é material de
> imprensa do fabricante, não documento de produto."

A primeira frase é **falsa**. A Henkel declara metal, alumínio, ferro, cobre e
latão E declara secar em condição submersa — as duas metades, no mesmo produto. O
que segura a recomendação é a **procedência da fonte**, que é régua NOSSA (regra
5), não o silêncio do fabricante, que seria fato dele. Trocar uma causa pela outra
é a mistura que a seção 7 do contrato proíbe — e ela é pior aqui do que em
qualquer outro lugar da página, porque está dentro da frase que o leitor recebe
como confissão de honestidade. É a mesma família do defeito que esta ilha já
consertou em 12/09 na prosa que envelhece calada, e da correção que a regra 6
obrigou em 13/09 ("o motivo não é falta de declaração").

**O conserto saiu inteiro, nas duas metades.** A frase-resposta ganhou um terceiro
ramo, e a **vitrine vazia** ganhou o dela — sem a segunda, a página consertaria a
resposta e repetiria a frase errada uma seção abaixo, em "nenhum produto do nosso
banco passa no que o fabricante declara". Defeito pego pela régua vizinha prova
que ALGUMA trava existe, nunca que ESTA existe, então cada metade tem mutação
própria.

**AS TRÊS CAUSAS DE UMA FAIXA DESCOBERTA, agora nomeadas uma a uma na tela:**
**silêncio** (ninguém declara a base — 7 células), **procedência** (alguém declara
as duas metades e a fonte é nível 4 — 4 células) e **ambiente delimitado** (o
fabricante declarou a base e delimitou o uso a outro ambiente — é o caso do
plástico fora do interno seco). O tipo do documento sai **lido do banco em disco**,
nunca digitado na frase: digitar "material de imprensa" ali mediria a frase contra
ela mesma.

## A PROVA DE QUE AS 27 CÉLULAS COMPRARAM ALGUMA COISA, medida nos dois mundos

Régua nova que só fica verde não provou nada. Nasceu a mutação **"o mapa perde a
pedra do epóxi"**, e ela é cirúrgica de propósito: tira do mapa de termos os dois
literais que o Durepoxi usa para alvenaria (*pedra* e *marmore*) e **não** os que o
Silicone Neutro usa (*pedras*, *alvenaria*). Assim o neutro continua respondendo e
o único efeito visível é o Durepoxi cair de menção com ressalva para silêncio nas
quatro células de alvenaria — **as quatro nascidas neste bloco**.

- **Com a matriz de 45:** o validador acusa **8 erros**, um par por célula.
- **Com as 18 de ontem, a mesma mutação:** validador **OK**, e `teste-f2` fecha em
  **107 afirmações, 0 falha**. O defeito passava inteiro, deixando só um AVISO de
  termo sem tradução — e aviso não reprova nada.

É a aritmética da cobertura dita sem eufemismo: **régua com buraco fica verde
exatamente dentro do buraco.**

## O que mudou na tela, além da frase

A **tabela pré-renderizada da cola foi de 18 para 45 linhas** — ela é montada a
partir da mesma matriz, e é a metade que um modelo de linguagem lê sem preencher
formulário. Cada linha continua **recomputada das declarações**, nunca lida do
campo escrito à mão ao lado dela: se o banco e a matriz se separarem, quem acusa é
o validador, e a tela nunca finge concordância copiando o esperado. Nenhuma URL
nova nasceu e nenhuma página foi criada.

## Três frases que envelheceram e foram reescritas em vez de ficarem

Prosa que descreve um problema também envelhece calada, e três arquivos diziam o
tamanho velho do buraco: o comentário do `teste-f2.php` que declarava a dívida
("cobre 18 das 45"), a docstring do `cobertura.py` que chamava a matriz de amostra,
e a da mutação do ambiente crítico ("16 das 18 células continuam certas"). As três
foram reescritas com o que se mede hoje — e a do `cobertura.py` **não** virou
"agora é dispensável": a matriz decide sobre base × ambiente e não olha o caquinho,
então a entrada da ferramenta continua tendo 270 estados e a pergunta daquela
varredura continua sendo uma contagem sobre os 270.

## A conferência no ar precisou nascer, e os 390 verdes mostram por quê

Depois do Sync, `conferir-no-ar.py` passou com **390 afirmações, 0 falha** —
**sem tocar uma linha do que mudou**. Nenhum dos casos que ela media era uma
célula SEM recomendação, então ela nunca tinha lido a frase que este bloco
consertou. É a cicatriz da robometria de 13/09 acontecendo aqui: verde que não
morde.

Nasceram **26 afirmações novas no ar**, em quatro estados e com régua escrita
literal no próprio arquivo (o nome do produto e o tipo do documento copiados da
fonte, nunca lidos do banco que monta a página): os **três** estados que
respondem por procedência (vidro, metal e alvenaria dentro da água) e o estado
**negativo**, sem o qual os outros três têm porta dos fundos — em espelho dentro
da água ninguém declarou nada, e ali a página TEM de dizer que ninguém declarou.
Sem ele, uma página que servisse a frase da procedência em toda faixa descoberta
passaria nos três primeiros. Mais a linha que conta as **45** da tabela servida,
com o 45 saindo do produto dos dois vocabulários, nunca digitado.

## A verificação, em números

- **`validar-banco`**: APROVADO — 25 materiais, **45 células da F2** (eram 18), 9
  do rejunte, 54 pares da regra 6 com 5 âncoras ponta a ponta.
- **Bancada, 0 falha:** `teste-casca` 546 · `teste-f2` **107** (eram 102, e agora
  varrendo 45 células em vez de 18) · `teste-f1` 182 · `teste-loja` 147 (72
  estados) · `teste-leads` 211 · `teste-atelie` aprovado · `teste-prestacao-rejunte`
  5 afirmações sobre 540 estados da F2 e 180 da F1 · `conferir-cobertura` 353 ·
  `validar-pastilhas` aprovado · `php -l` limpo em ferramentas e snippets.
- **Mutações:** `mutacoes-f2` de 44 para **47, com 47 reprovadas, 0 passaram e 0
  inertes** — a bateria inteira, rodada do zero sobre o estado final. As três
  novas são as deste bloco: a faixa descoberta voltando a negar a declaração, a
  vitrine vazia fazendo o mesmo uma seção abaixo, e a que só as 27 células novas
  pegam.
- **UMA PASSADA DA BATERIA FOI DESCARTADA E REFEITA, e o motivo fica escrito:**
  a primeira rodada aconteceu enquanto um `git stash` reverteu a árvore de
  trabalho por alguns segundos, para o commit de renovação da reserva. A bateria
  copia a pasta da ilha **a cada mutação**, então qualquer cópia feita naquela
  janela leu a ilha de ontem. Nenhum resultado dela foi aproveitado. Número que
  saiu de uma árvore que mudou no meio não é número medido.
- **No ar, depois do Sync:** `/status` na **revisão 27**, igual à do
  `manifest.json`, em UM disparo com 10 aplicados. `conferir-no-ar` de 390 para
  **416 afirmações, 0 falha**.

## Receita e dívida, contadas do arquivo

Nada mudou de receita neste bloco, e isso é a informação: **7 colas no banco, 25
itens de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem**. Os 15
`url_busca` continuam dependendo de uma sessão do painel da Shopee — a
palavra-chave já está escrita em `afiliado.url_busca_produto` nos 15, e no dia da
sessão são 15 colagens e nenhuma linha de código. Pauta da seção 17: `pauta.md`
ainda não existe — 0 escritos, 0 na fila, 0 recusados.

## Aberto e nomeado

- (a) **A dívida que este bloco fecha era a única que o bloco anterior tinha
  criado**, e ele não criou nenhuma no lugar dela. O que sobra da família é a
  metade do **rejunte**: `matriz_esperada_do_rejunte` tem 9 células de junta ×
  ambiente e continua sendo **amostra de borda**, escolhida para pisar nas faixas
  declaradas. É amostra de propósito e não é o mesmo caso da cola — lá a grade
  inteira é finita e pequena (45), aqui a junta é contínua.
- (b) Os 15 `url_busca` dependem de uma sessão do painel da Shopee.
- (c) O egresso a fabricante segue fechado; a ficha BRSA005 segue localizada e não
  lida, com o endereço guardado em `fonte_localizada_nao_lida`.
- (d) `1x1` de fabricante segue com zero elegível, e é o tamanho de 7 das 12
  linhas da tabela da F1.
- (e) A ilha não tem peça publicada, então ficha, formulário no ar e feed do
  Merchant Center esperam a artesã.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.

**PRÓXIMO, com ordem e motivo:** (1) **a ordem das duas vitrines na F1**, hoje
herdada de quando o bloco da pastilha era uma frase de espera — é o item mais
antigo da fila e o único que mexe em como a página apresenta produto; (2) **`1x1`
de fabricante**, a pendência mais cara da categoria pastilha, e a que sozinha
muda 7 das 12 linhas da tabela da F1; (3) **a matriz do rejunte de amostra para
grade**, se e quando a junta virar um vocabulário fechado — hoje ela é contínua e
a amostra de borda é a escolha certa, então isto é pergunta antes de bloco; (4)
os 15 `url_busca`, no minuto em que houver sessão — e é copiar e colar.

---

# 14/09/2026, 11h18Z — O 404 DEPOIS DE PUBLICAR NÃO ERA REGRA DE REESCRITA: ERA UM NOME QUE JÁ TINHA DONO

**Despacho do Raphael de 14/09, os quatro itens, e é o primeiro despacho desta
fábrica escrito a partir do que uma PESSOA encontrou usando o que ela construiu.**
A mãe dele recebeu o e-mail, criou a senha, entrou e cadastrou a primeira peça do
Arquipélago — "Quadro flores do campo", quatro fotos, R$ 500, pronta entrega. O que
vem abaixo é o que ela encontrou no caminho.

**Ilha escolhida pela 18.1, não pela rotação.** A clubedomosaico tinha o despacho do
Raphael mais recente e aberto no topo do `PROMPT.md`; a aquametria e a robometria
foram lidas antes de escolher e não tinham despacho aberto para a Fundação (o item
1 do de 10/09 da robometria é metade humana, no Search Console, e não é nossa). As
outras duas execuções da mesma janela registraram nos próprios commits que
perderam a corrida por esta ilha; nenhum force push aconteceu, dos dois lados.

## ITEM 1 — a causa não era a que o despacho supôs, e ele mandava confirmar

O despacho escreveu a hipótese e a marcou como hipótese: regras de reescrita do
CPT `peca` não descarregadas. **Medido antes de uma linha mudar, às 11h19Z:**
`/loja/quadro-flores-do-campo/` — a peça que ela publicou — responde **200**. A
regra de reescrita está de pé e nasce sozinha desde a Loja 1.0.0.

O que estava errado era **o nome de um parâmetro**. O painel carregava o id da peça
na URL como `peca`, e `peca` é o nome do TIPO DE CONTEÚDO, registrado com
`query_var` true — ou seja, uma variável PÚBLICA do WordPress. Para o núcleo,
`/atelie/?peca=24` não é "o painel com a peça 24": é "me dê a peça de slug 24", que
não existe, e o tema serve o 404 dele. As quatro medições, no ar, antes do
conserto:

| endereço | resposta |
|---|---|
| `/atelie/` | 200 |
| `/atelie/?aviso=publicada` | 200 |
| `/atelie/?peca=24` | **404** |
| `/atelie/?estado=editar&peca=24` | **404** |
| `/atelie/?estado=editar&cdm_peca=24` | 200 |

E a confirmação que fecha a frase dele: o corpo daquele 404 serve
`themes/twentytwentyfive/assets/images/404-image.webp`, com `alt="Pequena árvore
totara no topo acima de Long Point"`. **É a foto em preto e branco que ele viu.**

**Isto atingia mais que o publicar, e o despacho não sabia.** Seis voltas do painel
carregam o id — publicou, salvou rascunho, pausou, faltou um campo, atualizou fotos
— mais o link "Editar" da lista. **As sete caíam no mesmo 404.** Publicar era só o
caminho em que ela chegou primeiro.

**O conserto é o nome:** o parâmetro passou a ser `cdm_peca`, o mesmo prefixo que os
campos do POST deste painel já usam. Nenhum filtro tirando variável do núcleo no meio
do caminho — a colisão se resolve não colidindo. E como isso é uma regra que ninguém
enxerga lendo a linha (`'peca' => $id` parece certo), ela virou **portão**:
`teste-atelie.php` varre o snippet, extrai toda chave literal passada a
`cdm_atelie_url()`, resolve a constante do parâmetro de peça, e compara a lista
inteira com as variáveis públicas do WordPress — escritas à mão no teste, copiadas
de `WP::$public_query_vars`, mais o tipo e as duas taxonomias desta ilha. Quem
escrever uma chamada nova amanhã cai no portão sem precisar lembrar dele.

**A segunda metade do item 1**, que é o que ela devia ver no lugar do 404: a volta
para `/atelie/` já era PRG desde a 1.0.0 e continua sendo, agora com **faixa de
"Peça publicada!"**, botão **"Ver no site"** e botão **"Cadastrar outra peça"**. O
"Ver no site" **não é incondicional**: só nasce se a peça existe, é dela, está
PUBLICADA de verdade e tem endereço — a trava do núcleo devolve ao rascunho a peça
que não cumpre a regra de qualidade, então "publiquei" e "está no ar" são duas
coisas, e um botão que promete o site e cai num 404 seria o mesmo defeito, dentro
da tela que o conserta.

## ITEM 2 — "o que seria 'escolha'? Não tem nada"

Duas coisas erradas na mesma linha, e são independentes. **A palavra:** "Escolha"
nomeia uma opção que não existe; lida por quem não sabe o que é uma lista, é um item
como os outros. **O estado:** era `value=""` selecionável e inicial, então dava para
voltar a ela. Agora a primeira linha de toda lista de escolha do painel é
`<option value="" disabled hidden selected>Selecione…</option>` — instrução, não
item —, escrita por **uma função só**, porque foi exatamente dois lugares
escrevendo a mesma linha à mão que deixou "Escolha" sobreviver nos dois.

**A trava.** As duas listas que ligam a peça ao site — coleção e técnica — ganharam
`required`, e o botão **"Salvar e terminar depois" ganhou `formnovalidate`**: sem
essa palavra, o `required` transformaria guardar rascunho em refém de uma lista e
ela perderia o texto que já tinha escrito (decisão 5 do snippet). A frase que
aparece é do painel e não do navegador — "Escolha a técnica que você usou nesta
peça." —, trocada por `setCustomValidity`; com o JavaScript desligado sobra a do
navegador, que é seca mas trava do mesmo jeito, e travar é o que protege a peça
órfã. No servidor a régua já existia e não foi duplicada:
`cdm_loja_peca_publicavel()` recusa publicar sem coleção e sem técnica desde 12/09.

## ITEM 3 — Picassiete, e a prova de que o campo obrigava a mentir

A peça que ela cadastrou tem **"Picassiette" escrito na descrição por ela mesma** e
**"Trencadís" marcado no campo** — porque Picassiete não existia para marcar. É o
caso literal do campo que obriga a pessoa a responder o que não é.

A técnica entrou. **E a versão da Loja subiu com ela, que é a metade que faltava:**
`cdm_loja_termos_iniciais()` só é percorrida quando `CDM_LOJA_VERSAO` difere da
option `cdm_loja_termos` — termo novo sem versão nova é linha no repositório que
nunca vira linha na lista dela. Medido: antes deste bloco a rota pública `/v1/loja`
dizia `tecnica: 4`; depois do Sync diz **5**.

A distinção que o despacho mandou escrever está na **ajuda do campo**, que é onde ela
decide: *"Trincadís é caquinho de azulejo ou cerâmica, sem dar para reconhecer de
onde veio; Picassiete é caco de louça em que dá para reconhecer a peça original —
alça, bico, estampa. Também chamada pique-assiette."* O trincadís **fica**, como o
esclarecimento do mesmo dia manda.

**O slug gravado é `picassiette`, e isto é escolha registrada, não descuido.** O
despacho pediu `Picassiete`; o esclarecimento do mesmo dia diz que "entrou como
`picassiette`" e não o desfaz. As duas taxonomias desta ilha são registradas com
`rewrite` false, então o slug do TERMO não decide endereço nenhum hoje: no dia em
que houver página de técnica, `/tecnicas/Picassiete/` continua inteiramente
disponível, e quem decide o endereço é a malha, não este campo. Na tela, onde ela
lê, o nome é **"Picassiete"** — o `VOZ.md` manda na palavra.

## ITEM 4 — o comportamento do Real 21, com código nosso

O Raphael deu a referência e **mudou a instrução na mesma frase**: a galeria do
Real 21 é Elementor + Swiper, medido por ele em 14/09, e isso é construtor de página
mais biblioteca JavaScript — o que a 22.3 proíbe na página pública e a 11.7 proíbe
instalar. Copiar aquilo trocaria ranqueamento por beleza.

O que nasceu, todo ele sobre o HTML que já estava servido:

- **Foto grande em proporção fixa 4:5** com `object-fit: cover`. Era metade do "está
  muito feio": foto de celular vem em pé e deitada, e sem proporção fixa a página
  saltava de altura entre uma peça e outra.
- **Tira de miniaturas quadradas de verdade** — `aspect-ratio: 1/1` mais
  `object-fit: cover`, o quadrado é do CSS e o arquivo nunca é cortado. **Cada
  miniatura é um link para a âncora da foto**, então ela funciona com o JavaScript
  desligado: `#cdm-foto-3` rola o contêiner de `scroll-snap` sem uma linha de
  script. O `alt` delas é vazio de propósito — a foto grande já descreve a peça, e
  repetir faria o leitor de tela ler a peça inteira duas vezes.
- **Setas de 44 px**, botões de verdade com `aria-label` e `aria-controls`, que só
  rolam o contêiner. Aparecem no ponteiro e somem no toque, onde o dedo já arrasta.
- **Ampliar com `<dialog>` nativo**, X grande, `Esc` (que é do navegador) e clique
  fora. **Zoom** na ampliada com `transform: scale(2)` e origem no ponto tocado.
- **O endereço da foto grande viaja no HTML**, em `data-cdm-grande`: o zoom não é a
  foto pequena esticada, e o script **não busca nada** — que é o outro lado da 22.3.
- Tokens do `DESIGN.md` desta ilha, que ganhou a entrada "Galeria da ficha da peça"
  ANTES do código, como a 22.6 manda.

## O DEFEITO QUE SÓ O AR TINHA, E QUE EU PUBLIQUEI ANTES DE VER

Esta é a parte que vale mais que as quatro acima, porque ela é sobre o portão e não
sobre a tela.

A ficha é montada por `the_content`, e **o retorno desse filtro passa pelo
`wpautop`** — que usa as etiquetas de BLOCO como fronteira de parágrafo, embrulha
cada pedaço em `<p>…</p>`, e depois tira o `<p>` que encosta num bloco e o `</p>`
que vem logo depois de um. **`button`, `dialog`, `span`, `a` e `img` não são blocos
para ele.** A bancada desta ilha não tem WordPress: ela mede o HTML que a função
devolve, e o `wpautop` só existe no site.

Eu previ metade disso e errei a outra. A `<dialog>` foi para o `wp_footer` antes de
qualquer medição, e isso estava certo. As duas setas eu deixei soltas logo depois da
abertura do palco, achando que bastava não vir depois de um `</div>`. **Fui olhar o
HTML servido e ele trazia:**

```
<div class="cdm-gal-palco"><button …>‹</button><button …>›</button></p>
```

Um `</p>` órfão colado no `</button>`: a abertura do parágrafo foi removida por
encostar num `<div>` e o fechamento ficou, porque encostava num `</button>`. Nada
quebra na tela. O navegador engole. **E o portão tinha passado verde**, porque a
régua que eu tinha escrito olhava só um lado — etiqueta de linha DEPOIS de um
fechamento de bloco — e o defeito era do outro, ANTES de uma abertura.

A regra que sobra, e ela vale para tudo que esta ficha imprimir daqui para a frente:
**etiqueta que não é bloco nunca encosta numa fronteira de bloco, de nenhum dos dois
lados.** As setas passaram a morar dentro de um `<div class="cdm-gal-setas">` — uma
camada absoluta que cobre o palco, deixa o dedo passar e ancora as duas. A régua do
`teste-loja.php` passou a medir os dois lados e **nomeia qual** apareceu; a mutação
37 devolve exatamente o HTML que foi ao ar e a régua reprova dizendo
`antes de bloco: </button>`. E o `conferir-atelie-no-ar.py` passou a procurar as
cinco marcas do estrago — `<p><button`, `</button></p>`, `<p><dialog`,
`</dialog></p>`, `<p></dialog>` — **no HTML servido**, porque é lá que o `wpautop`
existe.

## A OUTRA COISA QUE O AR ENSINOU: a ficha é servida de cache por duas horas

Conferindo o conserto, a primeira leitura de `/loja/quadro-flores-do-campo/` veio
com `last-modified` de **13/09 17h01** e `cache-control: max-age=7200`, servindo a
ficha ANTERIOR — com a revisão 28 já aplicada e a rota `/v1/loja` já dizendo
`versao_loja: 1.2.0`. É a família da seção 4 do contrato com uma cara nova: o site
não ficou para trás, a CÓPIA que o visitante recebe ficou. O `conferir-atelie-no-ar.py`
já se protegia disso — o `buscar()` dele anexa `?v=<timestamp>` a toda URL, escrito
lá desde 12/09 — e foi o `curl` a mão desta execução que caiu no cache. Fica
registrado para a próxima passada: **`curl` a mão nesta ilha mede o cache, não o
site.**

## A verificação, em números

- **Bancada, 0 falha:** `teste-casca` **549** (eram 546), `teste-loja` **178** (eram 148),
  `teste-atelie` **288** (eram 251), `teste-leads` 211, `teste-f1` 182, `teste-f2`
  107, `teste-prestacao-rejunte` 5 sobre 540 e 180 estados, `conferir-cobertura` 353,
  `validar-banco` aprovado com 25 materiais e 45 células, `validar-pastilhas`
  aprovado, `php -l` limpo nos três snippets tocados.
- **Mutações:** `mutacoes-atelie` de 37 para **48**, com **48 reprovadas**, 0
  passaram, 0 inertes. `mutacoes-loja` de 23 para **36**, com **36 reprovadas**, 0
  passaram, 0 inertes. `mutacoes-arvore` de 20 para **21**, com **21 reprovadas**.
- **Duas mutações antigas foram consertadas, e as duas por causa deste bloco:** a 26
  do ateliê ficou INERTE porque o alvo dela citava `'peca' => $id`, que o conserto
  renomeou; a 33 da loja ficou INERTE porque a lupa saiu do retorno da ficha.
  Mutação inerte é teste verde com outro nome.
- **Uma afirmação foi endurecida depois de a mutação 25 passar limpa:** a régua da
  proporção fixa procurava `aspect-ratio:4/5` no documento inteiro, e o cartão da
  vitrine também tem essa linha — tirar a proporção da foto grande passava verde.
  Agora ela lê a declaração `.cdm-carrossel img{…}` isolada e imprime o conteúdo
  dela na medida. **Régua que procura no documento inteiro mede a existência da
  palavra, não a do comportamento.**
- **No ar:** `conferir-atelie-no-ar.py` **79 afirmações** (eram 65), 0 falha, 0
  pulada, com a seção 4d nova — o parâmetro, a faixa, a contagem de técnicas — e a
  galeria medida na ficha servida. `conferir-no-ar.py` **416 afirmações, 0 falha**,
  sem tocar uma linha do que mudou.
- **A própria afirmação de ar nasceu errada uma vez, e vale escrever:** a primeira
  versão procurava a FORMA `</button></p>` no HTML servido e reprovou a peça — só
  que essa forma tem versão legítima aqui, no formulário de lead
  (`<p class="cdm-lead-enviar"><button …></button></p>`), com a abertura escrita por
  nós. **O que separa o certo do errado não é a forma, é o BALANÇO.** A afirmação
  passou a contar `<p` e `</p>` dentro da região da galeria, onde a única abertura
  que existe é a da contagem de fotos: 1 abre, 1 fecha. Procurar a forma teria
  reprovado a página certa e, num dia com o formulário desligado, aprovado a errada.
- **A régua do `teste-loja` mudou de forma numa linha, e ela ENDURECEU:** até 13/09
  a afirmação era "a Loja não serve JavaScript nenhum", e ela media a coisa certa
  pelo motivo errado — o que a 22.8 protege não é a ausência de JavaScript, é a
  página FUNCIONAR sem ele. O que ela cobra agora: UM script, no rodapé, depois do
  conteúdo, e **nenhuma** ocorrência de `fetch(`, `XMLHttpRequest`, `import(`,
  `document.write`, `cdn.`, `swiper` ou `elementor` dentro dele.

## E UM TERCEIRO DEFEITO, ACHADO NA CONFERÊNCIA, QUE NINGUÉM ESCREVEU

Contando as URLs do `wp-sitemap.xml` para fechar o bloco, apareceu uma que não é
página desta ilha: **`/author/artesa/`**. Ela não foi escrita por ninguém e nenhuma
linha de código mudou para ela existir — **o provedor `users` do núcleo só lista
autor que TEM conteúdo publicado**, e até 13/09 esta ilha não tinha peça nenhuma.
No minuto em que a artesã publicou a primeira, o arquivo de autor dela entrou no
sitemap: **uma de doze URLs de um domínio de quatro dias.**

Duas razões para tirar, e cada uma bastaria. **É página fina e repetida** — o
arquivo do autor lista as peças publicadas, que é o que `/loja/` já faz com texto
editorial em volta, e orçamento de rastreamento é o recurso escasso da seção 14.1.
E **ele confirma o login dela**: o endereço carrega o `user_nicename`, que nesta
ilha é o mesmo `artesa` com que ela entra; este snippet e o do ateliê gastam
trabalho para a conta de uma pessoa de verdade não ficar exposta, e publicar o nome
de usuário num arquivo XML desfaz metade disso de graça.

Casca **1.9.2**: o provedor `users` sai, pelo mesmo mecanismo que a Aquametria já
media desde 10/09 — aqui ele só não existia porque não havia autor com conteúdo. A
régua entrou no `teste-casca.php` escrita à mão (o nome do provedor e a resposta
esperada estão na linha, não lidos do snippet) e cobra os dois lados: `users` sai,
`posts` e `taxonomies` ficam, para a remoção não vazar. Mutação nova na bateria da
árvore, **21 de 21 reprovadas**. **No ar: o sitemap foi de 12 para 11 URLs, e
nenhum arquivo de autor pede rastreamento.**

**E o `atualizar-manifest.py` fez o trabalho dele nesta passada**, o que é raro o
bastante para ficar escrito: ele **recusou gravar** a revisão 30 porque a versão da
casca no manifest (1.9.1) não batia com a constante do snippet (1.9.2). A recusa
veio antes do commit da revisão, não depois.

## A cópia da seção 24 nasceu, com peça de verdade dentro

`dados/pecas.json` existe desde hoje, com a peça que ela cadastrou: título, slug,
estado, descrição, campos, coleção, técnica e as quatro URLs de foto. Até 13/09 a
rota devolvia `total: 0`, e zero peça é resposta, não falha.

**Uma decisão de formato, e ela é o que faz a regra 24.2 funcionar:** o campo
`gerado_em` da rota **não entra na cópia**. Com ele dentro, toda passada da ronda
seria um commit, e a 24.2 manda commitar só quando o JSON MUDOU. Quando a cópia foi
tirada é o git que sabe — é para isso que ele serve. `publicar: false`, porque este
arquivo é cópia do site e nunca fonte dele; desembarcá-lo devolveria ao WordPress o
que veio de lá.

## Receita, contada do arquivo (nada mudou neste bloco)

7 colas, 25 itens de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem. Os
15 `url_busca` seguem dependendo de UMA sessão do painel da Shopee. Pauta da seção
17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.
**A loja tem 1 peça publicada e 0 rascunhos**, e é a primeira linha de receita
própria do Arquipélago inteiro.

## Aberto e nomeado

- **(a) A página `/tecnicas/Picassiete/` NÃO nasceu, e o item 3 pedia.** Não é
  esquecimento e não é conserto: **nenhuma** técnica desta ilha tem página. As duas
  taxonomias são registradas `public => false` por decisão medida de orçamento de
  rastreamento (decisão 4 do snippet da Loja, 12/09) — taxonomia pública nasce com
  arquivo e põe de sete a doze URLs finas no sitemap de um domínio de quatro dias.
  Criar a página do Picassiete sozinha seria criar a família inteira por uma porta
  lateral. **Isto é bloco de malha, não item de despacho**, e ficou reescrito no
  `PROMPT.md` como o que falta.
- **(b) A metade humana do item 4 continua aberta:** o dedo dela na galeria, num
  telefone. A Fundação mediu o HTML servido, as marcas do `wpautop`, os
  `aria-label` e a proporção; **ninguém tocou a tela**. Isso fica como o que falta,
  nunca como conferido.
- (c) Os 15 `url_busca` dependem da sessão da Shopee.
- (d) O egresso a fabricante segue fechado e a ficha BRSA005 segue localizada e não
  lida.
- (e) `1x1` de fabricante segue com zero elegível, e é o tamanho de 7 das 12 linhas
  da tabela da F1.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.
- (g) A dívida de modelagem que o esclarecimento do Raphael registrou e mandou NÃO
  mexer agora: o campo "técnica" mistura MÉTODO (direto, indireto) com ESTILO
  (bizantino, trincadís, Picassiete), e ela pode marcar um achando que marcou o
  outro.

**PRÓXIMO, com ordem e motivo:** (1) **a família `/tecnicas/<slug>/`**, que é o que
sobrou do item 3 e agora tem peça publicada para linkar — e é decisão de malha, com
o orçamento de rastreamento na mesa; (2) **a ordem das duas vitrines na F1**, o item
mais antigo da fila e o único que mexe em como a página apresenta produto; (3) `1x1`
de fabricante, a pendência mais cara da categoria pastilha; (4) os 15 `url_busca`,
no minuto em que houver sessão.

---

# 14/09/2026, 13h21Z — A ORDEM DAS DUAS VITRINES DA F1: A PASTILHA VEM PRIMEIRO, E O TÍTULO DEIXA DE DEPENDER DE ESTAR EM SEGUNDO LUGAR

**F1 1.3.0, manifest revisão 31, `/status` conferido. NENHUMA URL nova, NENHUMA
página criada, NENHUM produto entrou ou saiu do banco.** Este é o item mais antigo
da fila desta ilha — o único que mexe em como a página apresenta produto — e foi o
`PRÓXIMO (2)` do fecho anterior depois que o `(1)`, a família `/tecnicas/`, ficou
nomeado como bloco de malha e não de conserto.

**A ESCOLHA DA ILHA: TERCEIRA TENTADA.** Nenhuma ilha tinha despacho aberto para a
Fundação no topo do `PROMPT.md` (os quatro achados da artesã de 14/09 saíram inteiros
na execução das 11h18Z e o que restou é bloco de malha; a aquametria e a robometria
não tinham despacho para a Fundação), então valeu a rotação da seção 1. A aquametria
tinha a `ultima_execucao` mais antiga (11h25Z) e meu push de reserva foi recusado —
outra execução a tomou às 13h19Z. A robometria (11h44Z) caiu do mesmo jeito,
reservada às 13h20Z. A clubedomosaico estava com `executando_desde: null`, que pela
1.1 já significa que não há bloco da Fundação vivo. Nenhum force push, e nada de
execução anterior para mesclar: local e remoto batiam com o `main`. Rede pela 20.2
antes de trabalhar: home em 200 e `/status` na revisão 30, igual à do manifest, em
UMA passada.

## O QUE ERA A ORDEM ERRADA, e por que ninguém a via
Até a 1.2.0 o bloco de compra do **rejunte** vinha antes do da **pastilha**. Não era
decisão: era herança. Quando a vitrine do rejunte nasceu, o lugar da pastilha era uma
frase de espera (`"ainda não temos as pastilhas no nosso banco"`), então o rejunte
era o único bloco de compra que a página tinha. A 1.2.0 encheu aquele lugar com treze
produtos e **manteve a sequência de chamada** — que é como uma ordem provisória
sobrevive a quem a tornou errada. Não havia régua nenhuma sobre ordem, e ordem que
ninguém mede não pode nem ser corrigida com confiança.

A pastilha vem primeiro porque as **três superfícies** que abrem a página falam dela:
o `<title>`, o H1 e a primeira frase da resposta (`"leva cerca de N pastilhas de X
cm"`, com o rejunte entrando como o segundo número). A seção 22.1 põe ranqueamento
antes de conversão antes de beleza; aqui as três apontam para o mesmo lado, porque
quem chega por "quantas pastilhas para mosaico" veio comprar pastilha, e o `VOZ.md`
desta ilha diz "produto primeiro". **Nada da 22.2 se moveu:** a resposta continua
antes da explicação, os DOIS blocos de compra continuam ANTES da camada de prova
(seção 7), e nenhuma URL, trilha, âncora ou JSON-LD mudou.

## O QUE A TROCA REVELOU, e é o que fez disto um bloco e não um swap
O título do bloco da pastilha era **"E onde comprar a pastilha"**. Aquele "E" é
conector: ele só faz sentido depois de outro bloco de compra, e é um título que
**mente quando a ordem muda**. Pior, a seção 5 pede frase autossuficiente, que
sobreviva a ser citada fora de contexto — e o título é justamente a frase que um
modelo de linguagem cita sozinho. Os dois títulos passaram a ser autossuficientes:
**"Onde comprar a pastilha"** e **"Qual rejunte cabe nessa folga"**, nenhum
dependendo da posição em que foi servido. Uma mutação escreve o "E" de volta, e ela é
o defeito de verdade: invisível para qualquer régua de ordem, porque a sequência fica
certa e só o título passa a prometer um bloco anterior que não existe mais.

## A FRONTEIRA DOS DOIS BLOCOS GANHOU NOME (cicatriz da Robometria de 13/09/2026)
A bancada e a conferência no ar extraíam cada vitrine pelo **texto do H2** — régua que
morre calada no dia em que o título muda, e que no estado degradado do rejunte (sem a
F2 no ar, o título é `"Onde comprar o rejunte"`) **nunca conseguiu extrair nada**.
Cada seção passou a declarar o que ela é na própria classe (`cdm-f1-vitrine-pastilha`
e `cdm-f1-vitrine-rejunte`), em **todas** as saídas, inclusive as degradadas.
Fronteira de teste é marcador escrito, nunca "a primeira coisa parecida com". As três
réguas que extraíam pelo título — `teste-f1.php`, `teste-prestacao-rejunte.php` e
`conferir-no-ar.py` — passaram a ler o marcador.

## O MUNDO SEM A F2 FOI PRODUZIDO PELA PRIMEIRA VEZ
A F1 chama a régua do rejunte da F2 em vez de escrever uma segunda (decisão 4 do
cabeçalho dela), e por isso tem DUAS saídas degradadas escritas de propósito — uma em
cada vitrine — que dizem "a lista está fora do ar" e mantêm a conta de pé. Elas
existiam desde 12/09/2026 **sem uma única afirmação encostando nelas**, e a do rejunte
serve um H2 diferente do normal, que era o que fazia a extração por título não achar
nada ali. Régua escrita para um mundo que nunca acontece nasce errada sem poder
falhar (seção 8). O render ganhou `sem_f2=1`, e a bancada agora mede esse mundo: a
conta continua, as duas vitrines dizem que a lista está fora do ar (uma cada), e
nenhum cartão de produto nem recusa é improvisado sem a régua que decide quem entra.

## O PORTÃO VERMELHO QUE JÁ ESTAVA NO main — a cópia da seção 24
Ao rodar a bancada inteira antes de fechar, `validar-banco.py` reprovava o
`dados/pecas.json` que a execução das 11h18Z criou (a cópia da primeira peça de
verdade, "Quadro flores do campo"). A régua era de 12/09 e dizia uma frase só: **o
arquivo não pode existir** — verdadeira enquanto o único jeito de ele aparecer fosse
alguém inventar o catálogo da artesã. Depois disso a **seção 24** entrou no contrato e
virou a mesa: dado que uma pessoa digita no WordPress nasce com cópia no repositório,
e o bloco não fecha sem ela. A proibição envelhecida passou a reprovar o repositório
por cumprir o contrato. A régua foi trocada: o que ela protege não é a ausência do
arquivo, é que ele seja **cópia e nunca fonte**. Três afirmações, e a do meio é a de
verdade: (1) o manifest o declara `publicar: false`; (2) **nenhum snippet o lê** —
medido no código que vai ao ar, com o comentário descartado —, porque peça inventada
só chega à tela se alguém servir o arquivo; (3) o arquivo tem a **forma da resposta do
endpoint** (id de post, URL no domínio da ilha, `total` que bate com a lista, e sem o
carimbo `gerado_em`, que a 24.2 mantém fora da cópia para a ronda não commitar a cada
passada). Quatro mutações novas na bateria do rejunte escrevem os quatro defeitos de
volta — cópia publicada, snippet lendo a cópia, total digitado, peça sem id.

## A VERIFICAÇÃO, EM NÚMEROS (bancada, 0 falha)
- **`teste-f1.php`**: nasceu a seção **4d** (ordem das duas vitrines) com 15 estados,
  um processo cada — marcador único, pastilha antes do rejunte, resposta antes das
  duas, as duas antes da prova, e nenhum título abrindo com conector, medido em 6
  títulos. Mais o mundo sem a F2 produzido. O arquivo foi de 190 para **211
  afirmações**.
- **`mutacoes-f1.py`**: de 40 para **46 mutações, 46 reprovadas, 0 passaram** — as
  seis novas: ordem invertida, o "E" de volta no título, a vitrine descendo para
  depois da prova (uma versão que reprova pela ordem, outra que preserva a ordem e só
  inverte compra x procedência), o marcador da pastilha sumindo, e o do rejunte
  sumindo SÓ na saída degradada.
- **`teste-prestacao-rejunte.php`**: 5 afirmações, 540 estados da F2 e 180 da F1, a
  extração do bloco do rejunte da F1 agora pelo marcador.
- **`validar-banco.py`**: OK, 25 materiais, 45 células da F2; a régua nova da cópia da
  seção 24 no ar.
- **`mutacoes-rejunte.py`**: de 12 para **16 mutações, 16 reprovadas** (as quatro
  novas da cópia da seção 24).
- **`validar-pastilhas.py`** 189, **`mutacoes-prestacao.py`** 11 de 11,
  **`mutacoes-cobertura.py`** 11 de 11, **`teste-casca.php`** 549, **`teste-f2.php`**
  107, **`teste-loja.php`** 178, **`teste-atelie.php`** aprovado, **`teste-leads.php`**
  211, **`conferir-cobertura.php`** 353, **`php -l`** limpo em tudo.

## NO AR (o desembarque)
Sync disparado UMA vez, revisao 31 com 10 aplicados; `/status` na revisao 31, igual
a do manifest. A F1 serve, no HTML servido, a vitrine da **pastilha antes** da do
rejunte, com os marcadores `cdm-f1-vitrine-pastilha` e `cdm-f1-vitrine-rejunte` e os
titulos **"Onde comprar a pastilha"** e **"Qual rejunte cabe nessa folga"** — nenhum
abrindo com conector. `conferir-no-ar.py`: **437 afirmacoes** (eram 416), 0 falha,
incluindo a ordem das duas vitrines medida em tres estados servidos.

## PROXIMO, com ordem e motivo
1. **A familia `/tecnicas/<slug>/`**, decisao de malha com o orcamento de rastreamento
   na mesa, e agora com peca publicada para linkar.
2. **`1x1` de fabricante**, a pendencia mais cara da categoria pastilha — sozinha muda
   7 das 12 linhas da tabela da F1.
3. **A categoria COLA**, 45 estados varridos e 0 com o minimo da 14.3.
4. Os 15 `url_busca`, no minuto em que houver sessao da Shopee.

14/09/2026 17:35Z — A FAMÍLIA DAS TÉCNICAS: o endereço é decidido, o banco da entidade TECNICA nasce, e a família NÃO nasce hoje

- **A escolha da ilha: SEGUNDA tentada.** Os cinco `ESTADO.md` estavam com
  `executando_desde: null`, que pela 1.1 já significa que não há bloco da
  Fundação vivo. Pela 18.1, ilha com despacho aberto do Raphael vem primeiro: a
  **ohmetria** tinha o despacho de nascimento de 14/09 e `ultima_execucao: null`,
  que é a mais antiga de todas. Reservei-a às 17h16Z e o push foi **RECUSADO**
  por segundos — outra execução gravou a reserva dela às 17h17Z (commit
  `a92f759`). Voltei ao passo 2 sem force push, como o passo 5 manda. Das que
  sobraram, nenhuma tinha despacho ABERTO para a Fundação: os de 14/09 da
  aquametria e da robometria estão marcados CUMPRIDOS e conferidos no ar, e o
  único item aberto do despacho da clubedomosaico é declarado pelo próprio texto
  como bloco de malha e não conserto. Valeu a rotação da seção 1 e a
  clubedomosaico tinha a `ultima_execucao` mais antiga (13h21Z). Reservada às
  17h18Z, push aceito.
- **Rede pela 20.2, antes de trabalhar:** home em 200 e `/status` na revisão 31,
  igual à do manifest, em UMA passada.
- **O BLOCO.** Era o item 1 da fila desta ilha desde 14/09 de manhã: a família
  `/tecnicas/<slug>/`, que o despacho do Raphael pediu pelo nome
  (`/tecnicas/Picassiete/`) e que a execução das 11h18Z classificou, com razão,
  como decisão de malha com o orçamento de rastreamento na mesa. **Decidido em
  `ARVORE.md`, seção 4b.**
- **O ENDEREÇO NÃO É A RAIZ, e essa metade é do contrato.** O
  `dados/corpus-buscas.md`, de 10/09/2026, escreveu o item 5 da fila como
  `/tecnicas/bizantino`. A seção 16.1 entrou em 11/09 e proíbe página solta na
  raiz além das cinco que ela nomeia. **O corpus estava certo no dia em que foi
  escrito e passou a contradizer o contrato no dia seguinte**, e ninguém viu
  porque a página nunca foi criada — é a mesma família do slug de categoria que
  o `VOZ.md` e a casca escreviam diferente até 11/09. Corrigido no corpus, com a
  nota de por quê. Nenhuma URL se moveu porque nenhuma existia.
- **A MÃE É `/como-fazer/`, e a técnica nasce filha DIRETA dela** — terceira
  aplicação de uma regra que este arquivo já tinha escrito duas vezes: *a mãe de
  hoje é a mãe que já tem endereço* (as duas ferramentas em `/materiais/`, a peça
  em `/loja/`). A categoria `/como-fazer/tecnicas/` fica registrada como
  candidata para o dia das três filhas (16.5).
- **POR QUE ELA NÃO NASCE HOJE — três portões, e os três medidos, nenhum
  opinião:** (1) seção 9, três itens de banco reais por página: **0 para 5 de 5
  técnicas**; (2) 16.5, três filhas: não há nenhuma; (3) 14.6 e 14.8, a rampa só
  é autorizada por número — e `dados/indexacao.md` tem **uma linha só**, de
  10/09/2026, escrita quando o WordPress ainda não existia (zero URL, zero
  impressão). **Nenhum número autoriza leva nova nesta ilha hoje**, de nenhuma
  família.
- **O ACHADO, e ele é mais estreito do que "falta banco":** as duas únicas
  técnicas cujo lado do material tem fonte (trencadís e picassiete) apontam para
  `caco_azulejo` e `caco_louca` — **caco de prato e de azulejo não têm
  fabricante**, e `caco_louca` nem sequer é valor possível de `tipo` para a
  categoria pastilha no vocabulário do esquema. Os 13 itens do banco de pastilhas
  são todos `pastilha_vidro`. A distância entre a técnica e o banco desta ilha é
  a distância entre o caco e o produto — e o caminho mais curto não é catalogar
  caco: é ligar a técnica à cola e ao rejunte, onde há 12 itens e uma ferramenta
  que já decide.
- **O QUE FOI ENTREGUE NO LUGAR DA PÁGINA: `dados/tecnicas.json`**, o banco da
  entidade TECNICA que o esquema previu em 12/09 e que nunca tinha nascido. Cinco
  técnicas, as mesmas cinco que a artesã pode marcar no ateliê, cada uma com
  definição sustentada por fonte de enciclopédia, museu ou instituição de ensino
  (Museo Nacional de Cerámica, Sagrada Família, Wikipedia, SPACES Archives,
  FASBAM, Câmara dos Deputados, repositório da Universidade Nova de Lisboa),
  consulta-alvo, SERP lida em 14/09/2026 com os domínios nomeados um a um, e
  `revisao_tecnica: pendente` — **porque nesta ilha a revisora existe e é a
  artesã**, e página que finge revisão que não houve é a única mentira que esta
  ilha pode contar sobre uma pessoa de verdade.
- **AS 10 FONTES FORAM COLHIDAS POR BUSCA E NENHUMA FOI ABERTA**, e isso está
  escrito em cada uma no campo `leitura`: `pt.wikipedia.org`, `britannica.com` e
  `google.com` devolveram `connect_rejected` às 17h30Z. É a regra do elo mais
  fraco da seção 10 aplicada à única entidade da ilha que não tem fabricante — e
  é o mesmo buraco de egresso que a escada de fontes já registrava do lado dos
  fabricantes, agora medido do lado das técnicas.
- **NADA FOI INVENTADO, e os campos vazios dizem por quê.** `junta_tipica_mm`
  nasce `null` em 5 de 5 porque nenhuma fonte declara folga em milímetro — e esse
  é justamente o campo que alimentaria o valor sugerido da F1. As três técnicas
  `opus_*` do vocabulário ficaram de fora com motivo: nenhuma é oferecida à
  artesã, então nenhuma peça poderia ser marcada com elas.
- **O PORTÃO QUE MEDE ISSO ESTAVA ESCRITO DESDE 12/09 E NUNCA TINHA RODADO.** A
  régua de TECNICA do `validar-banco.py` vivia imprimindo "tecnicas.json ainda
  não existe" — verde por ausência, que é função morta com outro nome. No dia em
  que o arquivo nasceu ela passou de primeira, e passar de primeira não é elogio:
  ela cobrava o que qualquer arquivo bem digitado teria. Passou a cobrar o que o
  esquema diz que esta entidade tem de especial: fonte obrigatória apontando para
  fonte que **existe**; origem dentro dos três níveis que o esquema aceita, lidos
  DO esquema e não recopiados; campo vazio exigindo o motivo ao lado; número só
  com fonte; e **o portão da família** — técnica não declara página com menos de
  3 itens de banco. A contagem por técnica passou a sair em toda execução.
- **`ferramentas/mutacoes-tecnicas.py`: 14 mutações, 14 decididas certo.** A
  bateria tem **os dois lados da fronteira** de propósito: 13 precisam reprovar e
  **uma precisa PASSAR** — a mesma página de técnica, com o lado do material
  resolvido, tem de abrir o portão. Sem ela ninguém saberia se o portão mede a
  contagem ou se apenas odeia o campo, e uma régua que reprova tudo nunca deixa a
  família nascer.
- **UM DESPACHO DO ARQUIPÉLAGO FECHADO SEM TRABALHO, e vale registrar por quê:**
  `dados/despachos.md` pedia que a próxima execução que reservasse esta ilha
  documentasse o parâmetro de autenticação do endpoint de peças. Ele **já estava
  documentado** no `PROMPT.md` desta ilha desde 13/09, com URL completa, nome do
  parâmetro e conferência no ar. Despacho fechado no destino não se apaga sozinho
  na origem; marcado como fechado lá.
- **UM DESVIO ENCONTRADO NO MAIN, de outra execução:** o commit `29099ba` das
  14h59Z — o que corrigiu a seção 7 do contrato — editou
  `ilhas/clubedomosaico/dados/especificacao-calculadoras.md`, arquivo de uma ilha
  que aquela execução **não tinha reservado** (seção 3: toque apenas na pasta da
  ilha que você reservou), e deixou o `sha256` do manifest desatualizado. O
  conteúdo da edição está certo e ficou; o sha foi recalculado aqui. É a mesma
  família da "outra metade que é do Raphael" já registrada em `despachos.md`: a
  reserva protege contra quem a lê.
- **VERIFICAÇÃO, 0 falha:** `validar-banco.py` aprovado com 25 materiais e a
  contagem nova por técnica (direto 0, indireto 0, bizantino 0, trencadis 0,
  picassiette 0); `mutacoes-tecnicas.py` 14 de 14; `mutacoes-rejunte.py` 16 de 16;
  `validar-pastilhas.py` 189; `teste-casca.php` 549 — incluindo o portão que
  cobra que documento e código digam a mesma coisa sobre a árvore, que a seção 4b
  nova não moveu.
- **NÃO HOUVE SYNC, e não é esquecimento:** nenhum arquivo `publicar: true` mudou
  neste bloco. `dados/tecnicas.json` nasce `publicar: false` porque nenhum snippet
  o lê — dado publicado que ninguém lê é a porta por onde uma cópia vira fonte sem
  ninguém decidir. A seção 4 só exige acionar o Sync em bloco que mexe em conteúdo
  publicável.
- **Próximo passo, e ele mudou de dono nesta execução:** a frase "link de loja em
  breve", que a seção 7 passou a proibir em 14/09/2026, **ainda está no ar nesta
  ilha** — `cdm_f2_compra_html()` a serve para todo item sem `url` e sem
  `url_busca`, e são **15 de 25** (13 pastilhas e 2 colas). É defeito no ar, e
  pela 18.5 vem antes de construção.

14/09/2026 18:45Z — A FRASE PROIBIDA SAI DA ILHA, e o desembarque parava numa camada que a purga não alcançava no primeiro Sync

- **Segundo bloco da mesma execução** (mutirão da seção 13: cada um passou pela
  verificação inteira antes do seguinte). O primeiro está na entrada anterior.
- **POR QUE ELE VEIO ANTES DE QUALQUER CONSTRUÇÃO NOVA (18.5):** fechando o bloco
  da família das técnicas, o `grep` de rotina achou `Link de loja em breve` sendo
  servido por `cdm_f2_compra_html()` — a frase que a **seção 7 do contrato passou
  a proibir em 14/09/2026**, no mesmo dia, e que a aquametria (39 itens) e a
  robometria (65 itens) tinham acabado de tirar das delas. Aqui eram **15 de 25**
  itens: 13 pastilhas e 2 colas, nos cartões da F2 e na vitrine de pastilha da F1,
  que chama a mesma função. Defeito no ar na ilha que eu tinha reservado.
- **O QUE FALTAVA NÃO ERA DECISÃO, ERA A TELA LER O CAMPO.** Dois dos 15 já tinham
  a palavra-chave da busca escrita em `afiliado.url_busca_produto` **desde 13/09**,
  e nenhuma linha de código a lia. É a mesma distância entre repositório e ar que a
  seção 4 do contrato paga mais caro, uma camada abaixo — e é literalmente o mesmo
  defeito que a aquametria nomeou hoje de manhã, na ilha ao lado.
- **A ESCADA DA SEÇÃO 25 GANHOU O DEGRAU 4** (f2 **1.5.0**): sem ficha e sem busca
  encurtada, a busca **crua** vira o botão. Ela sai `rel="nofollow noopener"` e
  **nunca** `sponsored`, e a decisão está registrada no código: `sponsored` é a
  declaração de uma relação **paga**, e ninguém paga por aquele clique. Chamar de
  patrocinado um link que não rende seria mentir ao leitor sobre a única coisa que
  ele tem o direito de saber sobre nós. O quinto estado — sem nenhuma das três —
  deixou de imprimir promessa: o bloco sai **vazio**, e quem impede esse item de
  chegar ao ar é o validador, com falha dura.
- **UMA PALAVRA-CHAVE ESTAVA ERRADA E MANDAVA PARA OUTRA ILHA.** O Silicone Acético
  Maxx buscava `silicone maxx tekbond **aquario**` — o nicho da Aquametria, copiado
  de lá junto com o padrão do campo. Quem faz mosaico chegaria na prateleira de
  aquário. Trocada por `silicone acetico maxx tekbond`. As 13 palavras-chave novas
  das pastilhas saíram de marca, código e o nome que a pessoa usa.
- **`itens_sem_piso` MORREU, e ele media a coisa errada.** Contava quem não tinha a
  busca **encurtada** e chamava isso de "sem piso" — duas perguntas coladas numa só,
  que davam o mesmo número **enquanto nenhum item tinha saída crua**: (1) o leitor
  tem para onde ir? e (2) esse clique rende comissão? Viraram duas contas:
  `itens_sem_saida_de_compra`, que agora é **erro duro** do validador e está em
  **0**, e `itens_com_piso_nao_rastreavel`, que é dívida de comissão e está em
  **15**. O campo velho é **recusado** pela régua: deixar o nome antigo conviver com
  o significado novo seria o pior dos mundos — o número continuaria batendo e
  diria outra coisa.
- **A PÁGINA DE DIVULGAÇÃO PASSOU A DIZER QUAL LINK PAGA E QUAL NÃO PAGA** (casca
  1.10.0), com seção própria e o "Estado de hoje" em duas contas. A frase "os links
  daqui são de afiliado" virou meia verdade no minuto em que a busca crua subiu
  para o botão.
- **O DESEMBARQUE E O CACHE: A PURGA SÓ VALE A PARTIR DO SEGUNDO SYNC.** Isto fecha
  o despacho de prioridade ALTA aberto na robometria, e o achado é maior que o
  despacho. A casca que **contém** a purga faz parte da carga que está sendo
  entregue: no Sync que a instala, o PHP já carregado é o **anterior**, então
  nenhuma purga roda. Medido minuto a minuto: às **17h40Z**, antes do bloco, as 11
  URLs serviam a assinatura do Endurance e o canônico **concordava** com a quebra
  de cache — não havia divergência, havia a janela. Às **18h29** o Sync da revisão
  32 aplicou com a casca 1.9.2 na memória, e aí o canônico ficou para trás: as duas
  páginas do bloco com entrada de 17h36Z e **a home com uma entrada de 13h53Z, do
  bloco anterior, velha havia cinco horas sem ninguém ver**. Às **18h34** um segundo
  Sync, já com a 1.10.0 carregada; poucos minutos depois o canônico servia o bloco
  novo nas onze URLs. São **duas camadas** e os cabeçalhos as nomeiam:
  `x-server-cache: true` e `x-proxy-cache` (nginx), com `max-age=7200`.
- **A AFIRMAÇÃO DO CACHE REPROVA PELA ORIGEM E RELATA O CANÔNICO**, e a escolha é
  deliberada: fazer o canônico reprovar transformaria toda entrega em duas horas de
  portão vermelho que ninguém consegue fechar, e portão assim se aprende a ignorar —
  que é pior do que não ter portão. Defeito de verdade é a **origem** não servir o
  bloco; canônico velho é janela, relatada com a hora da entrada e a da expiração.
- **DUAS RÉGUAS TINHAM PARADO DE MEDIR SEM FICAR VERMELHAS, e as duas foram
  consertadas:** (1) a mutação "cartão sem nenhum degrau some" procurava a classe da
  etiqueta proibida, que deixou de ser emitida — ela editava o snippet, o `if` nunca
  era verdadeiro, **nada sumia e a bateria ficava verde**; é a mutação inerte que a
  robometria nomeou hoje de manhã, aqui por outro caminho. (2) A soma dos degraus
  emitidos por um snippet só sobreviveu à mudança **dando o mesmo número por outra
  composição**: era 1 etiqueta + 1 botão de busca + 1 linha discreta = 3, virou 0 +
  2 + 1 = 3. Um degrau inteiro sumiu e outro nasceu com o portão verde ao lado.
  Agora cada degrau é contado pelo próprio marcador.
- **E TRÊS AFIRMAÇÕES QUE REPROVARAM UMA PÁGINA CERTA** foram reescritas por
  **escopo**, não afrouxadas: elas diziam da página inteira o que valia do cartão
  com ficha. É a mesma família da "afirmação em bloco com escopo maior do que o que
  foi medido" que a seção 7 do contrato nomeia.
- **VERIFICAÇÃO, 0 falha.** BANCADA: `teste-casca` 549, `teste-f2` 111 (eram 107),
  `teste-f1` 195, `teste-loja` 178, `teste-atelie`, `teste-leads` 211,
  `teste-prestacao-rejunte` 5 sobre 540 e 180 estados, `conferir-cobertura` 353,
  `validar-banco` aprovado, `validar-pastilhas` 189, `php -l` limpo.
  MUTAÇÕES: f1 46/46, **f2 50/50** (três novas: a busca crua declarando sponsored,
  a tela voltando a não ler o campo, e a crua passando na frente da ficha),
  rejunte 16/16, técnicas 14/14, pastilhas 14/14, cobertura 14/14, prestação 11/11.
- **NO AR:** revisão **33** no `/status`, igual à do manifest. `conferir-no-ar.py`
  com **450 afirmações** (eram 437), 0 falha. As 11 URLs em 200 e **zero**
  ocorrência da frase proibida; a vitrine de pastilha serve 3 botões de busca crua
  para os 3 elegíveis de 2 cm; a página de divulgação serve as duas contas.
- **Próximo passo, com ordem e motivo:** (1) o lado do material da família das
  técnicas — ligar técnica a cola e rejunte, que é onde esta ilha tem banco e
  ferramenta; (2) `1x1` de fabricante, que sozinho muda 7 das 12 linhas da tabela da
  F1; (3) a categoria COLA, 45 estados varridos e 0 com o mínimo da 14.3; (4) os 15
  `url_busca` encurtados, no minuto em que houver sessão do painel da Shopee — o
  piso já está na tela sem eles.

---

## 14/09/2026, 21h17Z — A PÁGINA DO PICASSIETE NASCE, e o que a impedia eram TRÊS RÉGUAS MAL LIDAS

**Ilha escolhida pela 18.1, segunda tentada.** Os cinco `ESTADO.md` parseavam em
`yaml.safe_load` e os cinco tinham `executando_desde: null`, que pela 1.1 já
significa que não há bloco da Fundação vivo — não houve reserva vencida para o
git desempatar. Três ilhas tinham despacho aberto do Raphael de 14/09
(clubedomosaico, ohmetria e jornadafly), empate de data, e a rotação da seção 1
desempatou: clubedomosaico com `ultima_execucao` 18h45Z, a mais antiga das três.
O primeiro push da reserva foi **recusado**, e não porque alguém pegou esta ilha:
outra execução reservou a aquametria às 21h18Z e o `main` andou. Voltei ao passo
2 sem force push, confirmei que a clubedomosaico seguia livre, e a reserva
passou. Rede pela 20.2, retestada e não herdada: home 200 e `/status` na revisão
33 — igual à do manifest — em três passadas.

### BLOCO A — o portão contava uma categoria que a página não recomenda

O despacho do Raphael de 14/09 tinha um item aberto: a página do Picassiete. Duas
execuções daquele dia responderam que ela não podia nascer, e a segunda delas
escreveu **três portões medidos** na `ARVORE.md` seção 4b. Os três decidiam
errado, e nenhum dos três erros era de dado — eram de leitura de régua:

**1. O portão de 3 itens de banco da seção 9 contava só TESSELA.** Ele perguntava
quantos produtos da categoria `pastilha` o banco tem com o tipo que a técnica
cita. As duas únicas técnicas com material declarado por fonte — trencadís e
Picassiete — apontam para `caco_azulejo` e `caco_louca`, e **caco de prato e de
azulejo não têm fabricante e nunca terão ficha de produto nesta ilha**. O portão
lia zero, e leria zero para sempre, por mais coleta que acontecesse.

Só que **a página de uma técnica não recomenda caquinho**. Ela responde *o que
comprar para colar aquele caquinho*, que é o eixo desta ilha escrito no
`PROMPT.md` — e isso é produto com fabricante, declaração datada e link de
afiliado. O item 6 da mesma seção 4b já dizia isso com todas as letras ("o
caminho mais curto não é catalogar caco: é ligar a técnica à cola e ao rejunte"),
enquanto o item 3 contava caco. **As duas metades da mesma seção discordavam, e
quem decidia era a que tinha número.**

É a mesma família da V24 da Aquametria, consertada poucas horas antes no mesmo
dia: uma régua que amarra o portão a um campo que o caso certo nunca preenche
reprova o mundo inteiro e **parece rigor**.

A conta passou a ser, escrita uma vez só, em `itens_de_banco_da_tecnica()` do
`validar-banco.py`: as pastilhas do banco cujo tipo é a tessela que a técnica
declara, **mais** as colas que o fabricante declara elegíveis para aquela tessela
em algum par base × ambiente do vocabulário. Resultado medido: trencadís **5**,
Picassiete **5**, e direto, indireto e bizantino seguem em **zero**, cada um com
o `motivo_sem_materiais` escrito dizendo por que não declara material. **Régua que
abre para todo mundo não mede nada** — é por isso que três das cinco continuam
fechadas, e é isso que separa conserto de porta dos fundos.

Três coisas ficaram deliberadamente fora da conta, e estão escritas no código:
menção com ressalva (fonte fraca demais para virar recomendação), o rejunte (a
régua dele decide por junta em milímetro e não olha a tessela; as cinco técnicas
têm `junta_tipica_mm` null) e qualquer comparação por texto.

**O que nasceu:** `ferramentas/tecnica-x-material.py`, que deriva
`dados/tecnica-x-material.json` **importando** a conta do validador em vez de
reescrevê-la — uma conta, dois leitores —, e
`ferramentas/mutacoes-tecnica-x-material.py`, com 9 mutações. Ela afirma o
**número**, não o veredito, e a razão é a mutação mais perigosa desta família: a
que **infla** a conta, faz o portão abrir mais cedo e continua verde porque
"abriu". Duas mutações inflam de propósito (contar ressalva; varrer todas as
tesselas em vez das declaradas) e são pegas pelo número.

**Uma expectativa minha estava errada e a bancada me corrigiu.** Na mutação que
encolhe a varredura para uma base só, previ que a união de colas ficaria em 5 e
os estados com o mínimo cairiam para 2 e 1; a medição devolveu 4, 6 e 3, e ela
estava certa. Ficou registrada dentro do arquivo, porque é o próprio argumento a
favor de afirmar número em vez de veredito: uma bateria que só perguntasse
"abriu ou fechou" teria passado nas duas contas, a minha e a certa.

**2. A 16.5 não se aplica.** Ela pede três filhas antes de a categoria nascer — e
a técnica de hoje nasce **filha direta** de `/como-fazer/`, não dentro de uma
categoria. A própria tabela do item 2 daquela seção já dizia isso.

**3. "Nenhum número autoriza leva nova" é o oposto do que a seção 21 manda.** A
21.1 é literal: abaixo do piso — 40 URLs publicadas e 21 dias desde a primeira
indexada —, zero impressão **não é informação** e **nunca** trava leva nenhuma.
Esta ilha tem 11 URLs e `piso: abaixo` escrito no cabeçalho, que é o campo que a
21.6 manda ler em vez de recalcular de cabeça. A armadilha é fina e por isso se
repete: quem lê a 14.8 ("é essa série que autoriza dobrar, manter ou parar") e
olha uma série de uma linha conclui corretamente que ela não autoriza nada — só
que **"não autoriza" e "proíbe" não são a mesma frase**. A Aquametria pagou isto
em 12/09 e a Clube do Mosaico em 14/09: duas ilhas, três dias. Virou a **21.8**
do `ARQUIPELAGO.md`, com a régua em duas perguntas na ordem.

### BLOCO B — a página, e ela não decide nada

`/como-fazer/o-que-e-mosaico-picassiete/`, nível 3 com a mãe de nível 1 direto —
o mesmo estado de transição em que a F2 e a F1 vivem desde o bloco 4. **Não é
`/tecnicas/Picassiete/`**, que foi o endereço que o despacho pediu: a 16.1 proíbe
página solta na raiz desde 11/09, e o slug é a consulta-alvo do banco.

**Nenhuma linha do snippet escolhe cola.** Quem escolhe é `cdm_f2_celula_cola()`,
a régua da F2 que está no ar desde 11/09, chamada aqui para o caquinho de louça.
A grade tem 45 células — 9 superfícies × 5 lugares —, é servida no HTML e é
recalculada a cada requisição. É a tabela pré-renderizada da seção 5 do contrato:
um modelo de linguagem lê os 45 casos sem preencher formulário nenhum. O texto, a
definição e as fontes saem de `dados/tecnicas.json`, que passou a `publicar: true`
porque agora existe snippet que o lê.

**A prestação de contas da seção 7 fecha com o banco:** das 7 colas, 5 entram na
vitrine e as 2 que ficam de fora são nomeadas em linha própria. **E isso virou
conserto dentro do próprio bloco:** a primeira versão escrevia só o balde de maior
contagem, e o Durepoxi cai por silêncio em 25 células **e** entra com ressalva em
20 — dizer só o silêncio faria a página afirmar que o fabricante nunca nomeia uma
daquelas superfícies, o que é falso em 20 delas. A seção 7 é explícita desde
12/09: causa que o código separa, o texto separa. Agora o código separa quatro
baldes e o texto separa quatro.

**A recusa:** a página não responde o rejunte, e diz por quê — ele se decide pela
largura da junta em milímetro, e nenhuma fonte colhida sobre Picassiete declara
essa folga. Onze das 45 células dizem, com todas as letras, que não há cola que o
fabricante sustente.

**A casca subiu para 1.11.0 por um motivo de malha, não de vitrine.** Com um link
só, vindo da mãe, a página nasceria **órfã** pela 16.4(f), e o portão do
`teste-casca` pegou isso na hora. A Escola e a home passaram a listar as técnicas
em **bloco próprio**, separado dos tutoriais: técnica é "o que é isso", tutorial é
"como se faz", e juntá-las faria a Escola prometer um passo a passo que a página
de técnica não entrega.

**Duas dívidas de texto do banco viraram defeito no ar e foram pagas aqui.** O
`dados/tecnicas.json` nasceu sem acento — "louca", "xicara", "monumento historico"
— porque até hoje só era lido por ferramenta; no dia em que uma **página** passou
a servi-lo, virou português errado na tela, que é exatamente a cicatriz que o
`restaurar-acentos.py` desta ilha existe para lembrar. Vieram junto as aspas
tipográficas: aspa reta vira `&#039;` no `esc_html` e o filtro de conteúdo do
WordPress escapa o `&` de novo, servindo a entidade crua ao leitor. A troca dos
acentos tem **prova**: reduzido a sem-diacrítico, o arquivo é idêntico ao de
antes, fora de 10 frases do campo `leitura` reescritas de propósito e declaradas
uma a uma.

### Verificação

**Bancada, 0 falha:** `teste-tecnicas.php` com **52** afirmações — e o esperado
das 45 células **não vem do snippet**: vem de `dados/cobertura.json`, gerado pela
régua em Python, que é implementação independente em outra linguagem, escrita no
bloco 3 antes de existir uma linha do PHP. Ele começa rodando
`cobertura.py --conferir`, porque régua velha aprova a página de ontem. Mais:
`teste-casca` 549, `teste-f2` 111, `teste-f1`, `teste-loja`, `teste-atelie`,
`teste-leads`, `teste-prestacao-rejunte`, `validar-banco`, `validar-pastilhas`,
`tecnica-x-material --conferir`, `php -l` limpo nos sete snippets.

**Mutações:** 9 da página, 9 da conta e as 14 do banco de técnicas — 32 no total,
todas decididas certo. A nona da página **não reprova por reprovar**: com o banco
fora do ar ela exige a página **honesta**, dizendo que não mediu e sem servir a
grade.

**Uma seção do teste foi apagada pelo próprio autor.** A primeira versão do
`teste-tecnicas.php` tinha uma seção 8 que imprimia `ok` sem medir nada — o
caminho sem banco não cabe num teste cuja bancada carrega as options na entrada do
processo. Ela virou aquela nona mutação, e o motivo de ter saído ficou escrito no
cabeçalho do arquivo: afirmação que não pode falhar é pior que afirmação ausente.

**No ar:** `ferramentas/conferir-tecnica-no-ar.py`, **23 afirmações sobre o HTML
que o site serve**. Ele reconta as 45 células contra o banco commitado, refaz a
prestação de contas na tela, confere a escada de compra e o `rel` de cada link, os
dois links internos que tiram a página da condição de órfã, o sitemap e o JSON-LD
servido. A seção 4 dele compara o **endereço canônico** com o mesmo endereço com
quebra de cache, por marcador e nunca por bytes — é a trava do cache do
hospedeiro, que o `/status` não enxerga. Sync da revisão 34 às 21h51Z, 12
aplicados em **um** disparo; canônico e versão sem cache iguais nos cinco
marcadores deste bloco.

### Próximo passo desbloqueado

**A segunda página de técnica: o trencadís.** Não sobrou portão — ela reúne os
mesmos 5 itens de banco, a SERP dela está classificada como ABERTA, e a máquina
inteira já existe. **Uma diferença que o Picassiete não tinha:** o trencadís
declara **duas** tesselas (`caco_azulejo` e `caco_louca`), e a página de hoje
resolve a primeira da lista — quem escrever decide se serve duas grades ou uma, e
diz qual na tela. O teto da 21.4 está longe: esta leva teve **uma** URL.

Depois dela, na ordem: a coleta das quatro categorias vazias do vocabulário
(`alicate`, `base`, `acabamento`, `apoio`), que é o que destrava o bloco 4c e que
nenhuma coleta de cola ou rejunte fecha; e a linha da peça na tabela da seção 5 do
`ARVORE.md`, que é conserto de **teste** e não de documento — o que falta está
escrito lá.

14/09/2026 23h19Z — A FAMILIA DAS TECNICAS VIRA FAMILIA: nasce a pagina do trencadis, e a grade passa a ser medida POR CAQUINHO (tecnicas 1.1.0, manifest revisao 35)

UMA URL nova: `/como-fazer/o-que-e-trencadis/`, a segunda filha da Escola e a
segunda e ultima que o portao da secao 4b do `ARVORE.md` autoriza hoje. Nenhuma
peca entrou ou saiu; nenhuma URL mudou de endereco.

- **A ESCOLHA DA ILHA: TERCEIRA TENTADA, DUAS PERDIDAS NA CORRIDA DO PUSH.** Os
  cinco `ESTADO.md` do `main` real tinham `executando_desde: null`, que pela 1.1
  ja significa que nao ha bloco da Fundacao vivo. Pela 18.1 li o topo dos cinco
  `PROMPT.md` antes da rotacao e **nenhuma ilha tem despacho aberto para a
  Fundacao**: os quatro itens do despacho da Sentinela de 14/09 na robometria
  estao CUMPRIDOS e o quinto e um achado de metodo endereçado ao Raphael (uma
  linha da 25.4 do contrato); os da ohmetria e da jornadafly sao despachos de
  NASCIMENTO, que carregam a fila inteira e nao cabem na 18.2; os desta ilha
  morreram conferidos no ar as 21h17Z. Sobrou a rotacao da secao 1. Pedi a
  robometria (19h17Z, a mais antiga) e o push foi recusado — outra execucao a
  reservou as 23h16Z e uma terceira reservou a jornadafly as 23h18Z. Voltei ao
  passo 2 sem force push e a clubedomosaico, que era a proxima da ordem (21h17Z),
  foi aceita as 23h19Z. Nenhum branch `claude/*` e nenhum PR aberto para mesclar.
- **REDE PELA 20.2, antes de trabalhar:** home em 200 e `/status` na revisao 34,
  igual a do manifest, em TRES passadas.

**O QUE O BLOCO ENTREGOU, e a parte que vale para as proximas paginas nao e a
pagina.** O `PROMPT.md` deixava uma escolha escrita para quem publicasse: *"o
trencadis declara DUAS tesselas e a pagina de hoje resolve a primeira — quem
escrever decide se serve duas grades ou uma, e diz qual na tela"*. **Ela nao foi
escolhida, foi medida.** O snippet passou a calcular **uma grade por caquinho** e
a **agrupar as que saem identicas**, celula a celula; as duas do trencadis saem
iguais nas 45, entao a pagina serve **uma** tabela e diz na tela que **comparou as
90** e por que elas empatam.

**A CAUSA, e ela e de uma linha da regua da F2:** o caquinho entra na decisao num
lugar so — `cdm_f2_condicao_cumprida()`, a condicao de superficie porosa que o
Cascola PL500 declara — e o esquema classifica `caco_azulejo` e `caco_louca` como
POROSOS os dois. Medido sobre `dados/cobertura.json`, que e a metade
independente: dos seis caquinhos do vocabulario, os **quatro porosos**
(`pastilha_ceramica`, `caco_azulejo`, `caco_louca`, `pedra`) tem as 45 celulas
**identicas entre si**, e os **dois que nao absorvem** (`pastilha_vidro`,
`caco_espelho`) divergem deles em **4 celulas**, sempre as mesmas quatro. **A
grade nao depende do caquinho: depende da CLASSE de porosidade dele.** Isso nao
virou frase escrita na pagina — a comparacao e recalculada a cada carregamento,
porque frase que resume uma medicao e a primeira coisa a envelhecer sozinha.

**O RAMO DAS DUAS TABELAS EXISTE E E MEDIDO, embora o banco de hoje nao o pise.**
`mutacoes-tecnicas-pagina.py` fabrica o mundo em que o trencadis declara
`caco_louca` e `caco_espelho` — um poroso e um nao —, exige **duas** tabelas e
exige que o teste **APROVE**; e a mutacao seguinte quebra o agrupamento no mesmo
mundo e exige que ele **REPROVE**. E a disciplina da borda fabricada: grade que
so pisa no caso que o banco tem hoje nao e grade.

**O SNIPPET DEIXOU DE SER UMA PAGINA (tecnicas 1.0.0 -> 1.1.0).** Id, slug e
titulo eram tres constantes; agora moram em `cdm_tecnicas_registro()` e cada
pagina tem **shortcode proprio** (`[cdm_tecnica_<id>]`). A razao nao e asseio: a
bancada descobre QUE pagina esta medindo casando o shortcode com a definicao de
paginas (`cdm_teste_caminho_da_pagina`), entao duas paginas com o mesmo shortcode
seriam medidas como uma so — a primeira duas vezes, a segunda nenhuma — e o verde
continuaria la. Esta medido pela mutacao `as duas paginas voltam a servir o MESMO
shortcode`. O `[cdm_tecnica]` da 1.0.0 continua registrado como atalho que resolve
pelo endereco servido, para o caso de a reescrita do conteudo da pagina nao pegar
no Sync.

**E `cdm_teste_paginas_no_ar()` PAROU DE LISTAR PAGINA DE TECNICA A MAO.** A
primeira entrou escrita; a segunda mostrou o custo na hora — a mae deixou de
listar a filha e as duas afirmacoes da 16.4(a) reprovaram num arquivo de bancada
que nada tem a ver com a pagina. A lista passou a sair do registro do snippet.

**DUAS REGUAS INERTES, ACHADAS DE PASSAGEM E CONSERTADAS NA MESMA EXECUCAO** — e
as duas sao da mesma familia, a de regua amarrada a um numero que o banco move:
- `dados/tecnicas.json` dizia de si mesmo `publicacao.publicar: false`, com o
  motivo *"nenhum snippet le este arquivo"*, escrito antes de existir pagina de
  tecnica — enquanto o manifest ja gravava a option que a pagina do Picassiete le
  desde 14/09. As duas metades estavam certas no dia em que foram escritas, que e
  sempre como esta divergencia nasce. Agora o `teste-tecnicas.php` exige que as
  duas digam a mesma coisa.
- A mutacao `slug de categoria foge do VOZ.md`, em `mutacoes-arvore.py`, estava
  amarrada a linha inteira da tabela do `ARVORE.md` com **"5 itens"** dentro. O
  banco de colas cresceu para 7, a mutacao parou de achar o alvo e essa trava
  ficou **inerte** — sem reprovar nada e sem acusar nada. O alvo passou a ser so
  o endereco: a bateria voltou de 20 para **21 mutacoes decididas**.

**O QUE A PAGINA DO TRENCADIS ENTREGA, e nao e o mesmo que a irma.** A definicao
e a origem catala vem do Museo Nacional de Ceramica (exposicao "Gaudi &
trencadis"); a resposta de com o que colar sai das 45 combinacoes de superficie e
lugar, 11 delas dizendo com todas as letras que nao ha adesivo que o fabricante
sustente. E ela tem uma **segunda recusa** que a do Picassiete nao tem: **o caco
de vidro comum**. As fontes citam vidro entre os cacos de Gaudi e o vocabulario
`material_tessela` desta ilha nao tem valor para caco de vidro de garrafa — tem
`caco_espelho`, que e vidro com prata atras e cai do outro lado da conta que
decide a cola. Responder pelo mais parecido seria trocar um material por outro no
meio de uma recomendacao, entao a pagina diz que nao responde e por que. Fica
como **divida de vocabulario**, nao como defeito de pagina.

**BANCADA, 0 falha:** teste-tecnicas **123** afirmacoes (era 52, e agora varre as
DUAS paginas), teste-casca 549, teste-f2 111, teste-f1 195,
teste-prestacao-rejunte 5 (540 estados da F2 e 180 da F1, um processo cada),
teste-loja, teste-atelie e teste-leads aprovados, validar-banco e
validar-pastilhas OK, `php -l` limpo. **MUTACOES:** mutacoes-tecnicas-pagina **14
de 14** (eram 9), mutacoes-tecnicas 14 de 14, mutacoes-tecnica-x-material 9 de 9,
mutacoes-arvore **21 de 21** (era 20 medindo e uma inerte). A bateria inteira da ilha foi rodada, nao so a do bloco: mutacoes-cobertura 14 de 14, mutacoes-voz-e-cabeca 24 de 24, mutacoes-pastilhas 14 de 14, mutacoes-rejunte 16 de 16, mutacoes-prestacao 11 de 11 — todas decidindo certo.

**NO AR:** Sync as 23h42Z, `/status` na revisao **35**, igual a do manifest, em UM
disparo com 12 aplicados. `conferir-tecnica-no-ar.py` **54 afirmacoes, 0 falha**,
agora varrendo as duas paginas e comparando uma com a outra — titulo, description
e primeiro paragrafo tem de ser diferentes, porque duas paginas geradas pelo mesmo
codigo sao o jeito mais facil de uma ilha publicar malha fina sem que nenhuma
medicao acuse. `conferir-no-ar.py` **450 afirmacoes, 0 falha**. O endereco
canonico ja servia o conteudo novo na primeira medicao, batendo com a versao com
quebra de cache nos cinco marcadores deste bloco.

**PROXIMO PASSO DESBLOQUEADO:** o eixo das tecnicas **ficou sem proxima pagina** —
as duas que o portao autoriza nasceram. As tres que seguem em ZERO (direto,
indireto, bizantino) sao trabalho de **FONTE**, nao de texto: nenhuma declara
material, e o bizantino e o de maior valor de indexacao da ilha. O que destrava
mais coisa continua sendo a **coleta das quatro categorias vazias do
vocabulario** (`alicate`, `base`, `acabamento`, `apoio`), que e o que abre o bloco
4c — e o canal de busca alcanca, o egresso direto aos dominios de fabricante nao.
A semana da 21.4 esta em **2 de 3 levas**, uma URL cada.

---

## 24/09/2026, 19h40Z — A ILHA ESTAVA FORA DO AR. A execução inteira foi levantá-la

**Primeira execução da Fundação depois de a ilha entrar em foco, e ela não criou
uma URL sequer.** O despacho do Raphael de 24/09 manda **medir antes de
construir**, e foi a medição de rede da seção 20.2 — o `curl` barato do começo de
execução — que achou o que nove dias de silêncio esconderam.

### O QUE FOI MEDIDO, às 19h20Z

**16 das 17 URLs do sitemap serviam a página de estacionamento da HostGator, com
404.** `/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`, `/loja/`,
`/materiais/quantas-pastilhas-para-mosaico/`, `/como-fazer/o-que-e-trencadis/`,
`/como-fazer/o-que-e-mosaico-picassiete/`, as cinco peças da Loja, mais
`/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`. **Só a home respondia.** As três
páginas que a leitura semanal de 23/09 mediu na primeira página do Google —
posições 7,8 · 9,1 · 7,0 — estavam entre as mortas.

**O WordPress estava inteiro, e é isso que nomeia a causa.** A busca interna
(`/?s=picassiete`) renderizava, achava a página do picassiete e listava as URLs
de todas as outras; o Sync aplicava a revisão 35 sem erro; o `/status` respondia.
Tudo que é **arquivo de verdade** (`/`, `/index.php`, `/wp-login.php`) ou **query
na raiz** (`/?s=`, `/?rest_route=`) passava. **Todo caminho bonito morria ANTES de
chegar no PHP.**

Medido oito vezes por URL, determinístico. A irmã `aquametria`, no **mesmo IP**
(108.179.253.218), servia sitemap, robots e wp-json em 200 — então não era o
plano, não era o túnel e não era a rede desta nuvem.

### UMA MEDIÇÃO QUE ATRAPALHOU, e fica escrita porque atrapalharia de novo

Às 19h16 a `/materiais/qual-cola-usar-no-mosaico/` ainda respondia 200. Às 19h21,
depois de eu disparar o Sync, ela virou 404 como as outras. **Não foi o Sync que
quebrou a ilha** — ela já estava quebrada quando a medição começou. O que aquela
URL tinha era um HTML cacheado em disco, que é **arquivo de verdade** e por isso
passava pela porta fechada; a purga do Sync o apagou. Aquele cache expirava
sozinho às 20h09 (`max-age=7200` a partir de 18h09). Fica registrado para
ninguém ler a sequência como causa.

### A CAUSA, medida de dentro do servidor

A casca ganhou a **seção 6** e a rota
`?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>`, que devolve o
retrato do roteamento por dentro. Ela respondeu:

```
permalink_structure : /%year%/%monthnum%/%day%/%postname%/
regras_no_banco     : 115
mod_rewrite         : true
raiz_gravavel       : true
htaccess            : /home3/rapha921/clubedomosaico.com.br/.htaccess
                      existe, legivel, gravavel, 1057 bytes
blocos              : ["NFD EPC"]
tem_wordpress       : false
```

**O `.htaccess` tinha um bloco só — `NFD EPC`, o do Endurance Page Cache do
hospedeiro — e não tinha o `# BEGIN WordPress`.** Sem esse bloco o Apache não
manda para o `index.php` nada que não seja arquivo existente, e o WordPress
deixa de receber todo caminho bonito. Um arquivo, sete linhas ausentes, a ilha
inteira fora do índice.

### O REPARO, com o antes e o depois na mesma resposta

`&reparar=1` roda `flush_rewrite_rules( true )` — o mesmo que salvar
Configurações > Links permanentes, que é o conserto que a documentação do
WordPress manda fazer para este defeito:

```
antes   1057 bytes   blocos NFD EPC             tem_wordpress false   rewrite  8
depois  1580 bytes   blocos NFD EPC,WordPress   tem_wordpress true    rewrite 15
```

**As 17 URLs voltaram a 200 no minuto seguinte**, junto com `wp-sitemap.xml`,
`robots.txt`, `wp-json` e `/author/mosaico_gestor/`. A **F2 voltou a responder
consulta**: `?cdm_base=vidro&cdm_tessela=pastilha_vidro&cdm_ambiente=externo`
saiu de 404 com 2.361 bytes de página do hospedeiro para 200 com 121.077 bytes
da ferramenta. Enquanto a porta esteve fechada, quem chegasse pela busca em
"cola para mosaico", na posição 7,8, e preenchesse o formulário **recebia a
página de estacionamento da HostGator** — as duas ferramentas desta ilha são GET
para a própria página.

### E O CONSERTO DURA — medido, não suposto

A suspeita óbvia era `cdm_casca_purgar_cache()`, que apaga arquivo e roda a cada
Sync desde 14/09. **Não foi ela**, por dois argumentos e o segundo é mais forte
que o primeiro: (1) ela só esvazia `wp-content/endurance-page-cache/`, com
`realpath` conferido a cada nível da recursão, e nunca encosta na raiz; (2)
**depois do reparo, um Sync novo reescreveu o `.htaccess` (mtime novo, 1579
bytes) e MANTEVE o bloco do WordPress** — o EPC preserva o que encontra. As
quatro URLs reconferidas depois dessa purga continuaram em 200.

**A causa de origem continua sem nome, e fica escrito assim.** O que tem nome é o
sintoma, o portão que o pega e o reparo que o desfaz. Causa inventada seria a
próxima execução consertando a coisa errada.

### O PORTÃO QUE FALTAVA, e por que ele faltava

`conferir-no-ar.py` media 450 afirmações e **teria** acusado este defeito — ele
gruda quebra de cache em toda URL, então toda leitura dele já era uma URL com
query, que era exatamente a forma que morria. **O que faltou não foi
sensibilidade, foi alguém rodar:** a ilha passou de 15/09 a 24/09 sem bloco.

O que ele **não** cobria são as três URLs que o Google usa e que **nenhuma página
desta ilha linka** — e é por não serem linkadas que nunca entraram na lista de
nenhum portão. Entraram agora:

- `/wp-sitemap.xml` em 200 com `content-type` de XML, **e trazendo XML de sitemap
  de verdade** em vez da página do hospedeiro;
- `/robots.txt` em 200 e `text/plain`;
- `/wp-json/` em 200 e `application/json`;
- **o 404 que tem de ser 404**: caminho inexistente responde 404 **na página desta
  ilha**, não na do hospedeiro. Portão que só cobra 200 aprova um servidor que
  responde 200 para tudo.

**456 afirmações, 0 falha**, medidas no HTML servido, a ilha inteira.

### A REGRA SUBIU PARA O CONTRATO — seção 29 do `ARQUIPELAGO.md`

Porque o motivo vale para toda ilha, não só para esta: **todo portão desta
fábrica entra pela porta que continuou aberta.** O Sync é `/?<ilha>_sync=`, uma
query na raiz; o `/status` é rota REST; a bancada roda sem site e sem rede, por
desenho. O `/status` respondeu a revisão certa o tempo inteiro e a bancada fechou
verde — as duas coisas eram verdade e irrelevantes. Entrou nas **três linhas** do
mapa de leitura, porque regra que ninguém lê é regra morta.

### A CÓPIA DA SEÇÃO 24 ESTAVA TRÊS PEÇAS ATRASADA

A Loja tinha **1 peça no repositório e 5 no ar**. A artesã cadastrou quatro entre
15 e 16/09 — Quadro Divino Espírito Santo (15/09), Vaso com flores em cerâmica,
Quadro Nossa Senhora Aparecida e Bandeja em madeira (16/09) — e **nenhuma
execução passou aqui desde então para buscá-las**. É o dado que a 24 chama de
único que não se reconstrói a partir do repositório, e é o trabalho da mãe do
Raphael. Gravado em `dados/pecas.json`, **formatado e não numa linha só**: cópia
sem diff legível não é histórico, e histórico é o ganho que a 24.4 nomeia.

### O DESPACHO DO RAPHAEL DE 24/09, pela 18.3

**Saiu:** o **BLOCO D**. `urls_publicadas` passou de 13 para **17**, contado no
sitemap no ar às 19h33Z — 12 em `wp-sitemap-posts-page-1.xml` (`/`, `/loja/`,
`/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`,
`/divulgacao-de-afiliados/`, `/privacidade/`, `/materiais/qual-cola-usar-no-mosaico/`,
`/materiais/quantas-pastilhas-para-mosaico/`, `/como-fazer/o-que-e-mosaico-picassiete/`,
`/como-fazer/o-que-e-trencadis/`) e 5 em `wp-sitemap-posts-peca-1.xml`.
`primeira_indexacao` continua `desconhecida`, como o bloco manda.

**Ficou, reescrito no `PROMPT.md` com o motivo em uma linha:** o **BLOCO 0** (o
`sub_id` deslocado uma casa) e os **BLOCOS A, B e C**. A ilha estava fora do ar,
e a 18.5 manda verificação antes de construção.

**E uma coisa que o próximo bloco precisa saber:** o BLOCO A é sobre **CTR de três
páginas na primeira página do Google**, e essas três páginas passaram pelo menos
um dia servindo 404 ao Google. **A série de `dados/posicoes.md` tem um buraco que
não é de CTR.** Trocar título agora mistura duas causas na mesma janela de
medição — quem fizer o BLOCO A decide isso com o número de 30/09 na mão e escreve
qual leitura está usando.

**PRÓXIMO PASSO DESBLOQUEADO:** o **BLOCO 0** do despacho do Raphael — o `sub_id`
da Shopee gravado como `-clubedomosaico-F2--`, deslocado uma casa, com
`sub_id_1` vazio. É o primeiro da fila, não divide passada com nada, e agora tem
uma ilha de pé embaixo dele. Nenhuma página nova nesta passada; a semana da 21.4
continua em **2 de 3 levas**.

---

## 2026-09-25, 10h16Z → 10h45Z — BLOCO 0 DO DESPACHO DO RAPHAEL DE 24/09: OS 31 LINKS DE SHOPEE RENASCEM COM O `sub_id` NA CASA CERTA

**Ilha em foco** (`foco.md`, desde 24/09). Reserva às 10h16Z, commit `105746f`. Rede conferida antes de
trabalhar (20.2): home, `/materiais/`, `/wp-sitemap.xml`, `/como-fazer/`, `/loja/` e `/sobre/` em 200 — a
porta de entrada consertada ontem continua de pé, que é o que `dados/consertos.md` mandava reconferir.

### O DEFEITO, E POR QUE ONZE DIAS NÃO BASTARAM PARA ALGUÉM VER

O único clique desta ilha na janela 16→22/09 chegou ao Relatório da Shopee como `-clubedomosaico-F2--`:
cinco campos, o **primeiro vazio**, tudo deslocado uma casa. A seção 7 manda `sub_id_1` = nome da ilha e
`sub_id_2` = código da ferramenta, e sem o campo 1 o painel não responde *"qual ilha vendeu"*.

**O banco estava certo o tempo todo.** `sub_id_1: "clubedomosaico"` e `sub_id_2: "F1"/"F2"` estavam
gravados em todos os 25 registros desde 13/09, e o `validar-banco.py` cobrava isso num portão próprio.
O que ninguém media era o **link** — e os 16 links nasceram no painel `offer/custom_link`, com os cinco
campos preenchidos **à mão**. **Mão humana em cinco caixas de texto não tem portão; chamada de API tem.**
É a seção 4 de novo, com outro nome: o banco é o resumo e o link é o fato.

### O QUE FOI FEITO — 31 LINKS, PELA OPEN API

| o quê | quantos | de onde saiu |
|---|---|---|
| ficha de produto regerada | 6 | do `url_produto` já gravado, que é da Shopee — os dois campos vêm da mesma URL crua conhecida, e o par continua demonstrável (25.4-b.1) |
| busca encurtada regerada | 10 | palavra-chave **reescolhida inteira**, nunca grampeada ao link velho |
| busca encurtada NOVA | 15 | esperavam sessão do painel desde 13/09 |
| Mercado Livre | 4 | **não tocados** — outro programa, com `etiqueta_ml` própria e reCAPTCHA no gerador (25.6) |

**Os 15 que esperavam sessão são a 25.4-b.3 em ação.** O `motivo_sem_url_busca` deles dizia, desde 13/09,
que o encurtamento *"exige a sessão logada"*. Era verdade naquele dia e deixou de ser **três dias depois**,
quando a Open API entrou — e, enquanto esteve escrito, mandava toda execução seguinte **nem tentar**.

**Os 10 que tinham link e não tinham busca crua são a 25.4-b.1.** A tentação era buscar uma palavra-chave
nova e grampeá-la ao lado do link antigo: o campo ficaria preenchido e a dívida iria a zero. Seria fabricar
a aparência de um par que ninguém mediu. Os dois campos saíram da mesma passada, e o link velho foi
descartado, não remendado.

### O ACHADO QUE NÃO ESTAVA EM NENHUM BLOCO: AS TREZE CHAVES DAS PASTILHAS DEVOLVIAM ZERO

Conferindo as palavras-chave contra a API **antes** de gerar link — que é o que a 25.4-b manda, porque
*"busca não esgota, mas muda de nome"* — as **treze** das pastilhas devolveram **zero oferta**:
`Glass Mosaic <código> pastilha de vidro <medida>`. A marca não é anunciada por nome na Shopee e código de
catálogo não aparece em título de anúncio. **O piso levava a uma busca vazia**, que é exatamente o beco sem
saída que o degrau 4 da 25.1 existe para impedir — e estava assim desde 13/09, com o botão na tela, sem
que nada acusasse.

A descida da escada de palavra-chave da 25.6 parou na **família** (medida e acabamento), com o degrau
escrito em `motivo_da_chave` de cada registro: `pastilha de vidro cristal 2,5`, `pastilha de vidro 3x3`,
`pastilha de vidro 2x2`, `pastilha de vidro 2,3`, `pastilha de vidro 1,5x1,5` e, para o strip de 1,2 cm,
`pastilha de vidro placa 30x30`. **Dois degraus ficaram barrados e o motivo é da 25.7:** código sozinho
(`K2501` devolve grade traseira de aspirador **Karcher**) e `pastilha de vidro` pelado (devolve pastilha de
**freio**). O que sustenta a busca é a **medida** junto do substantivo.

**O que se perde na descida, dito sem maquiar:** a busca deixou de prometer *aquele código* e passou a
prometer a família. **É o que um piso é** — "ver outras ofertas", nunca "este produto". Nenhuma ficha,
nenhum preço e nenhuma foto saiu daí; casamento de item continua proibido pela 25.7.

Uma chave das dez reescritas também caiu: `argamassa cimentcola externo ac-ii quartzolit` devolveu zero —
a Shopee anuncia **AC-2/AC-3** e quase nunca escreve a numeração romana. Virou
`argamassa cimentcola externo quartzolit`. **As 25 palavras-chave do banco devolvem oferta hoje**, medido.

### OS PORTÕES, QUE SÃO O QUE IMPEDE ISSO DE VOLTAR

1. **`ferramentas/conferir-sub-id.py`** (raiz do repositório, vale para todas as ilhas). Gera um link de
   **bancada** e lê o `utm_content` do **301** do encurtador, **sem seguir o redirecionamento**:
   `bancada-t0---`. Esse é, letra por letra, o formato do Relatório de cliques.
   **E o link é de bancada de propósito:** o salto do encurtador é onde a Shopee conta o clique. Conferir
   os 31 links da ilha por esse caminho gravaria 31 cliques com a etiqueta `clubedomosaico`, justo na
   semana em que a leitura semanal procura o **primeiro clique orgânico** (proposta 3 de 23/09). O
   mecanismo se prova **uma vez**; os links da ilha saem certos **por construção**, pela mesma função.
2. **`conferir-no-ar.py` ganhou a seção "O link de afiliado servido"**: varre as URLs do sitemap e reprova
   se aparecer encurtador de Shopee que o banco não conhece — mais uma afirmação de que ela **encontra
   algum**, senão o portão aprovaria por vacuidade. Pega link velho sobrevivendo na tela depois de uma
   regeração, que é defeito **mudo**: o link antigo continua vivo na Shopee, nada dá 404, e a ilha só perde
   a atribuição.
3. **`validar-banco.py`: `piso não rastreável` e `busca sem endereço cru` deixaram de ser aviso e viraram
   ERRO DURO.** O próprio comentário do arquivo prometia isso *"no dia em que o número chegar a zero"*.
   Chegou. `ausente` continua diferente de `tentado-e-falhou` (25.2-b): registro com `motivo_sem_url_busca`
   escrito passa; o que não passa é o silêncio. **As duas mutações reprovaram.**
4. A regra subiu ao contrato como **seção 25.8**.

**A régua de 14/09 que media a dívida teve de mudar de objeto, e ficou com a história junto.** A afirmação
`[F1 2 cm]` contava **botões de busca CRUA**, um por elegível — e hoje reprovava, porque a vitrine passou a
servir o botão **encurtado** com `rel="sponsored"`. É a terceira vez que essa linha troca de objeto contando
o mesmo número: etiqueta "em breve" (até 14/09), busca crua (14/09→25/09), busca encurtada (desde hoje).
Ela agora cobra as duas metades — a encurtada apareceu **e** a crua sumiu — porque enquanto as duas puderem
conviver na mesma tela, um item sem piso rastreável passa escondido atrás do vizinho que tem.

### O QUE FOI MEDIDO NO AR (18.4)

- Sync forçado: **revisão 37**, 12 aplicados.
- `conferir-no-ar.py`: **459 afirmações, 0 falha**.
- Varredura das **17 URLs do sitemap** mais dois estados de ferramenta: **14 encurtadores servidos, 0
  desconhecido** — nenhum link deslocado sobrou na tela.
- `validar-banco.py`: 25 materiais, **itens SEM SAÍDA de compra 0**, **piso NÃO rastreável 0** (era 15),
  **busca sem endereço cru 0** (era 10).
- `validar-pastilhas.py` 189 afirmações · `mutacoes-pastilhas.py` 14/14 · `mutacoes-rejunte.py` 16/16.

### DE PASSAGEM

`dados/pecas.json` carregava `gerado_em`, trazido do endpoint pela execução de ontem: era o **único erro
vermelho** do `validar-banco.py`, e portão vermelho que ninguém fecha é portão que se aprende a ignorar.
Removido — o carimbo de hora fica fora da cópia pela 24.2, senão toda passada da ronda vira commit.

### O QUE **NÃO** FOI FEITO, E POR QUÊ

Nenhuma página nova, nenhuma URL nova: continuam **17**, e a semana da 21.4 continua em 2 de 3 levas.
Os **BLOCOS A, B e C** do despacho de 24/09 não foram tocados e estão reescritos no `PROMPT.md` pela 18.3 —
o BLOCO 0 dizia, com todas as letras, que **não divide passada com nada**. O BLOCO A depende do número de
30/09; o BLOCO B (filtro `wp_robots` para `/author/`) é o único que não espera dado nenhum.

**PRÓXIMO PASSO DESBLOQUEADO:** o **BLOCO B** — `/author/mosaico_gestor/` está indexada e tomou impressão na
posição 1,0. O caminho é o **filtro** `wp_robots` no snippet da casca, nunca uma segunda meta em paralelo
(lição trazida da Aquametria, escrita no próprio bloco), mais a saída do sitemap. Não depende de nenhum
número que ainda não chegou.

25/09/2026 14:10Z — BLOCOS B E C DO DESPACHO DE 24/09 ENTREGUES: a etiqueta de robô era quatro em paralelo, e o rastreador nunca recebe redirecionamento

- **A ILHA DESTA EXECUÇÃO NÃO FOI ESCOLHIDA, FOI IMPOSTA PELO FOCO.** `foco.md`
  nomeia a **clubedomosaico** desde 24/09, então pela 1.2 a rotação da seção 1
  está suspensa e não houve o que comparar. `executando_desde` estava `null`, que
  pela 1.1 já significa que nenhum bloco da Fundação estava vivo — não houve
  reserva vencida para o git desempatar. Nenhum PR aberto e a branch `claude/*`
  do repositório está mesclada (zero commits à frente do `main`). Reserva aceita
  às 13h17Z, no primeiro push.
- **REDE PELA 20.2, RETESTADA E NÃO HERDADA:** três passadas,
  `clubedomosaico.com.br` em **200** nas três, com `aquametria.com.br` em 200 nas
  mesmas três.
- **A ORDEM VEIO DO PRÓPRIO DESPACHO**, que já a tinha escrito: o BLOCO B não
  depende de dado que não chegou, o C é varredura e relatório, e **o A espera
  30/09** — trocar título antes do número de 30/09 misturaria duas causas na
  mesma janela, e o veredito dele é de 08/10. Pela 18.3 o despacho foi reescrito
  deixando só o A, com o motivo em uma linha.

**BLOCO B — E ELE ACHOU UM DEFEITO MAIOR DO QUE O QUE VEIO CONSERTAR.**

- O pedido era `/author/mosaico_gestor/`: 200, sem etiqueta, fora do sitemap, sem
  link de nenhuma página daqui — e mesmo assim indexado e servido na **posição
  1,0** na janela 15→21/09, disputando orçamento de rastreamento com 15 páginas
  NÃO indexadas desta mesma propriedade.
- **O que a primeira medição achou, antes de escrever uma linha de código:**
  `/materiais/como-sabemos/` já servia **DUAS** `<meta name="robots">` — a do
  núcleo (`max-image-preview:large`, aspas simples) e a da casca (`noindex,
  follow`, aspas duplas), injetada num `wp_head` paralelo. **Era exatamente a
  armadilha que o BLOCO B nomeia como lição da Aquametria**, e ela já estava no ar.
- **E não eram duas, eram quatro.** A F1, a F2 e o Leads faziam o mesmo, cada um
  para tirar do índice o estado COM PARÂMETRO da própria página. Medido no ar em
  `/materiais/qual-cola-usar-no-mosaico/?base=espelho&onde=interno_seco`, que é um
  estado da **melhor página desta ilha** (17 impressões na posição 7,8).
- **POR QUE NENHUM PORTÃO VIA:** todos mediam **SE** a frase `noindex` aparecia;
  **nenhum media QUANTAS etiquetas apareciam.** O idioma de contar já existia
  nesta ilha desde que o `teste-f2.php` nasceu — mas só para o `<link
  rel="canonical">` ("a ancora serve UM canonical"). Para o robô, nunca.
- **A IRONIA ESTAVA ESCRITA NO PRÓPRIO F2**, três linhas acima do `echo` que ele
  fazia: ele explica, com todas as letras, por que NÃO imprime o canonical —
  *"serviria DOIS canonicals (...) sujo numa página cujo propósito inteiro é ter
  UM endereço no índice"* — e fazia exatamente isso com a etiqueta de robô.
- **O CONSERTO, e é o caminho que o bloco manda:** a casca 1.13.0 declara a
  etiqueta pelo filtro `wp_robots` (prioridade 20, depois do núcleo) em vez de
  imprimi-la, e abriu `cdm_fora_do_indice` para quem quiser sair do índice
  **declarar a condição**. Quem imprime é a casca, uma vez, a partir de um vetor
  só. `max-image-preview` é retirada quando a página sai do índice, para o texto
  servido não depender da ordem dos filtros: sai exatamente `noindex, follow`.
- **TRÊS CONTEXTOS SAEM DO ÍNDICE**, e dois são os que a Sentinela mediu em 23/09:
  as páginas declaradas na definição, o **arquivo de autor** e a **busca interna**
  (`/?s=`), que respondia 200 sem etiqueta nas três ilhas. `follow` fica nos três —
  a página sai do índice e a malha não se corta.
- **CINCO RÉGUAS DESTA ILHA MEDIAM A ASPA DE QUEM ESCREVEU, NÃO A DIRETIVA**, e
  as duas famílias apareceram no mesmo dia. `teste-f1`, `teste-f2`, `teste-atelie`
  e duas afirmações do `conferir-no-ar` procuravam a frase literal com **aspas
  duplas**, que eram as do `echo` dos snippets. O `wp_robots()` do núcleo usa
  **aspas simples**. Resultado: três reprovaram código CERTO no dia do conserto, e
  **duas passavam A VAZIO** — `'name="robots"' not in html` é verdade em toda
  página de aspas simples, inclusive numa que saísse com `noindex` por engano. As
  cinco passaram a medir a DIRETIVA e a CONTAR as etiquetas.
- **A BANCADA PASSOU A EMULAR `wp_robots()`**, com o
  `wp_robots_max_image_preview()` do núcleo na prioridade 10 e as aspas simples do
  original. Sem isso ela reprovaria o conserto por não saber produzir o mecanismo
  novo — e a saída fácil seria afrouxar o teste.
- **CONFERIDO NO AR**, casca 1.13.0 / f1 1.3.1 / f2 1.5.1 / leads 1.1.1, manifest
  39 e `/status` na 39: `/author/`, `/materiais/como-sabemos/`, `/?s=mosaico`,
  `/atelie/` e os estados com parâmetro da F1 e da F2 servem **UMA** etiqueta com
  `noindex, follow`; a home, as 17 URLs do sitemap e as duas âncoras que rankeiam
  servem UMA e continuam **no** índice.

**BLOCO C — O RASTREADOR NUNCA RECEBE REDIRECIONAMENTO, E ISSO SÓ APARECEU PORQUE DUAS LEITURAS DISCORDARAM.**

- `ferramentas/varrer-canonicas.py` (nova) lê a canônica e a cadeia de
  redirecionamento de cada URL e classifica nas duas listas que o bloco pede, em
  `dados/indexacao.md`. **71 URLs: 71 em "esperado, nenhuma ação", 0 defeito.**
  Nenhuma correção aplicada, como o bloco manda.
- **A LISTA NÃO É DIGITADA:** as 17 vêm do `wp-sitemap.xml` no ar, mais `/author/`
  e as variações de cada uma (`http`, `www`, sem barra final) — os dois motivos do
  e-mail nascem de DUAS URLs para a mesma coisa, e varrer só a versão boa mediria
  o lado que nunca dá problema.
- **O ACHADO, e ele quase não foi feito:** a primeira conferência abriu
  `https://www.clubedomosaico.com.br/loja/` no `curl` e leu **200**; a varredura,
  que gruda `?v=<agora>`, leu **301** na mesma URL no mesmo minuto. Não é
  intermitência: são **dois respondedores**. Com a quebra de cache a pergunta
  chega ao WordPress, que redireciona certo; sem ela quem responde é o **cache de
  página**, que não sabe redirecionar. **O Googlebot não manda quebra de cache.**
  Medido em três passadas por URL e por leitura, porque uma leitura só não
  distingue cache frio de regra — a primeira leitura da home deu 301 cru, antes de
  a entrada esquentar, e as três seguintes deram 200.
- **Em 36 das 71 URLs as duas leituras discordam**, e a coluna nova da tabela as
  marca uma a uma.
- **ISSO EXPLICA UM MOTIVO E NÃO EXPLICA O OUTRO.** "Página alternativa com tag
  canônica adequada": explicado, e o despacho está certo em chamá-lo de
  comportamento esperado — o rastreador recebe 200 em cada variação e a canônica
  aponta para a versão boa. "Página com redirecionamento": **não explicado pelo
  que a ilha serve hoje**, o oposto do que esta execução esperava achar. A fonte
  provável é a vida anterior do domínio (há um `sitemap.xml` de 2019 na
  propriedade), e **a lista só existe dentro do Search Console**.
- **O PEDIDO AO RAPHAEL CONTINUA DE PÉ, e é o que destrava de verdade:** dar
  acesso de leitura à conta `sentinela@` em `sc-domain:clubedomosaico.com.br`.
  Sem ele, indexação e posição desta ilha só se leem no navegador dele.
- **O QUE ISSO CUSTA A QUEM MEDIR ESTA ILHA, e é maior que o BLOCO C:**
  `conferir-no-ar.py` gruda `?v=<agora>` em toda URL — e está **certo** em fazer
  isso, porque nasceu para provar que o Sync aplicou a revisão nova (seção 4). O
  preço é que **ele nunca vê o que o visitante vê**, e nenhuma linha dizia isso.
  Cache servindo página velha para gente de verdade passa por baixo das 488
  afirmações dele sem encostar em nenhuma. Mesma família da seção 29.
- **A FERRAMENTA TEM `--autoteste`**, 11 casos fabricados, um por ramo da régua:
  a varredura fechou em 71 esperado e ZERO defeito, e portão que nunca acusou nada
  é indistinguível de portão quebrado. Os sete ramos de defeito acusam; os quatro
  de "esperado" não. **E o autoteste já pagou:** a primeira passada chamou de
  DEFEITO a ausência de canônica em `/author/`, que é o comportamento padrão do
  núcleo em arquivo (só página singular recebe `rel_canonical()`) — trabalho
  inventado, que é o que a abertura do BLOCO C manda evitar.

**DE PASSAGEM, UMA BANCADA VERMELHA QUE NÃO ERA DESTE DESPACHO — E QUE TRAVAVA DUAS BATERIAS.**

- `teste-f1` (2 falhas) e `teste-f2` (1) estavam vermelhos no `main` **desde as
  10h40Z desta mesma data**, e com eles `mutacoes-f1` e `mutacoes-f2` se recusavam
  a rodar: *"a F1 de verdade já está reprovada — conserte antes de mutar"*.
  Confirmado como anterior rodando as duas em `82ced82`: 2 e 1 falhas, idênticas.
- **A CAUSA ERA A PRÓPRIA MELHORA DAQUELA EXECUÇÃO.** Os treze itens de pastilha
  subiram do degrau 4 (busca crua, `rel=nofollow`, que não rende nada) para o
  degrau 3 (`url_busca`, link de afiliado com `rel=sponsored`). As réguas cobravam,
  com número fixo, que os treze estivessem no degrau 4 — **e o comentário três
  linhas acima da própria afirmação já tinha escrito, em 14/09, que "uma régua
  presa a isso ficaria verde para sempre".** Prendeu-se assim mesmo, e ficou
  vermelha quando a ilha melhorou.
- **CONSERTADO SEM AFROUXAR:** o degrau de cada item passa a ser **derivado do
  banco**, e a régua cobra que o cartão sirva o botão do degrau em que o item
  está, um por recomendado, nos **três** degraus em vez de num só. O invariante
  que nunca mudou — nenhum item sem saída de compra, nenhuma promessa de "em
  breve" — continua cobrado igual.
- **E O DEGRAU 4 PASSOU A SER PRODUZIDO, NÃO ESPERADO:** nasceu o mundo
  `so_crua=1` no `render-para-teste.php`, que apaga a ficha e a busca encurtada e
  deixa a crua de pé. É onde o `rel=nofollow` da busca crua é conferido agora — o
  irmão `sem_piso` já tinha escrito essa mesma cicatriz sobre si mesmo em 14/09.
- **Os dois voltaram a verde e as duas baterias voltaram a rodar.**

**TRÊS MUTAÇÕES FICARAM INERTES NO CONSERTO, E AS TRÊS FORAM RETARGETADAS.**
`mutacoes-leads` 29, `mutacoes-f1` e `mutacoes-f2` apagavam o `echo` que deixou de
existir. Mutação inerte é o pior dos dois estados: a bateria continua verde
dizendo que mediu. O alvo novo é a declaração do `cdm_fora_do_indice`, e apagá-la
devolve o estado com parâmetro ao índice do mesmo jeito.

**MEDIDO NESTA EXECUÇÃO.** Bancada: `teste-casca` 555 (eram 549), `teste-f1` 196,
`teste-f2` 114, `teste-atelie`, `teste-leads`, `teste-loja`, `teste-tecnicas` e
`teste-prestacao-rejunte` — **todos 0 falha**. Mutações: `mutacoes-atelie` 48/48,
`mutacoes-leads` 48/48 e **0 inertes** (era 1), `mutacoes-voz-e-cabeca` 24/24,
`mutacoes-arvore` 21/21, `mutacoes-f1` 46/46 e `mutacoes-f2` 50/50 — **as duas
últimas voltaram a rodar nesta execução**, depois de se recusarem desde as 10h40Z. No ar: `conferir-no-ar.py` **488
afirmações, 0 falha** (eram 459). As afirmações novas da casca foram provadas não
inertes uma a uma, com quatro quebras: `max-image-preview` colada no `noindex`,
autor de volta ao índice, casca devolvendo markup em vez de diretiva, e tudo
saindo do índice — as quatro reprovam.

**PRÓXIMO PASSO DESBLOQUEADO:** o **BLOCO A** (CTR das três páginas de primeira
página), que **espera o número de 30/09** por ordem do próprio despacho. Até lá
esta ilha não tem item da Fundação aberto que não dependa de dado que ainda não
chegou. **O que depende do Raphael:** o acesso do `sentinela@` ao Search Console,
e a proposta de 301 de `http` para `https` em todo caminho, escrita em
`dados/indexacao.md` e **não aplicada**.

25/09/2026 16:16Z — BLOCO ENTREGUE: a categoria ALICATE sai de zero, e o teto de corte da ilha e 5 mm

- **O que este bloco e, e por que ele e este.** O despacho do Raphael de 24/09 esta fechado menos pelo
  BLOCO A, que **espera 30/09 por ordem do proprio despacho** — trocar titulo antes do numero de 30/09
  misturaria duas causas na mesma janela. Com isso a fila normal volta, e o que o `ESTADO.md` e o
  `ARVORE.md` vinham apontando ha treze dias como "o que destrava mais coisa" e a **coleta das quatro
  categorias vazias do vocabulario**. Comecei pela `alicate` por um motivo escrito, nao por gosto: o
  proprio `esquema-banco.json` diz, desde 11/09, que "as categorias rejunte, pastilha e alicate podem ser
  enchidas em qualquer execucao, **sem decisao nova** — o esquema ja diz que campo cada uma exige". As
  outras tres nao tem essa linha.
- **`dados/materiais-alicates.json`, seis SKUs.** Tres torqueses Cortag (mosaico com roldanas de metal
  duro, azulejista corte reto, azulejista corte curvo) e tres cortadores manuais Vonder (VDEC 51, 75 e
  90). `dados/cobertura.json` recontado pela propria `ferramentas/cobertura.py`: a lista
  `categorias_do_vocabulario_sem_nenhum_item` **cai de quatro para tres** — restam `base`, `acabamento`
  e `apoio`.
- **O ACHADO NAO ERA DESTE BLOCO, E CRUZA COM O BANCO QUE JA EXISTIA.** O torques de mosaico da Cortag e
  a **unica** ferramenta do arquivo cuja declaracao nomeia **vidro**, e ela para em **5 mm**. Os tres
  cortadores de bancada declaram *"pisos ceramicos e porcelanatos ate 10 mm"* e **nao nomeiam vidro em
  lugar nenhum** — nem na indicacao, nem no rodel de carboneto de tungstenio. Medido contra
  `materiais-pastilhas.json`: das **13** pastilhas do banco, todas de vidro, **10** cabem no teto e
  **tres nao** — `st5102` (6 mm), `af1500` (8 mm) e `ic02` (8 mm). **Para tres dos treze produtos cuja
  quantidade a F1 ja calcula, o banco de ferramentas nao tem uma declaracao de fabricante que sustente o
  corte.** Nao e falta de coleta: os quatro fabricantes alcancados publicam o teto deles. E faixa
  DESCOBERTA no sentido da 14.3, escrita na secao **7b-bis** do `ARVORE.md`.
- **A outra metade vale para as duas paginas de tecnica que ja estao no ar.** A frase do torques nomeia
  **pastilha** de vidro e de ceramica e **nao nomeia** caco de azulejo, caco de louca, caco de espelho
  nem pedra — e caco de louca e o material do **picassiete** e caco de azulejo o do **trencadis**. Pelo
  principio dos tres estados, para esses quatro o estado e `nao_declarado`: nem recomendar, nem proibir,
  e dizer que ninguem declarou.
- **A SECAO 8 PEGOU UMA CONSULTA MINHA CONTAMINADA, e ela ficou registrada no dado em vez de apagada.**
  Uma passada escrita com o prefixo `68.51` devolveu `68.51.075.000` e `68.51.090.000` — exatamente o que
  ela plantou. A passada limpa seguinte, sem numero nenhum, **nao devolveu referencia**. Os dois codigos
  ficaram **NULL** com o motivo escrito no registro. O do VDEC 51 (`68.51.050.000`) ficou porque veio de
  consulta que nao o carregava, e depois foi corroborado por canal independente: o titulo de um anuncio
  lido pela Open API, *"... VDEC 51, VONDER 6851050000"*. Duas passadas por SKU, escritas de forma
  diferente, pedindo sempre os ROTULOS da ficha e nunca um numero.
- **O PORTAO DESMENTIU A MINHA SUPOSICAO, e esse e o melhor pedaco da execucao.** O arquivo nasceu
  `publicar: false` com o motivo "option que nenhuma pagina le e caminho morto". Quem desmentiu foi o
  `teste-casca.php`: *"o cartao 'Alicates e corte' mostra o que o banco tem — tela 0 / banco 6"*. O
  cartao **G-ALICATES existe no Guia desde que a casca nasceu**, e o mapa `G-ALICATES =>
  materiais-alicates` ja estava escrito **dentro do proprio teste**, esperando o arquivo. O leitor
  existia; a suposicao e que estava errada. Casca **1.14.0** liga os dois.
- **E de passagem, a frase de prova do Guia ia publicar uma soma impossivel.** Ela anunciava o total do
  banco e enumerava **so tres** categorias: com a quarta entrando, teria ido ao ar *"o banco tem 31
  itens, sendo 7 colas, 5 rejuntes e 13 pastilhas"*. E a familia do *"hoje 10 dos 5 itens esperam link"*
  que esta ilha ja pagou uma vez. A frase passou a nomear a quarta, e a tabela da metodologia ganhou a
  linha.
- **E O SEGUNDO PORTAO REPROVOU A MINHA REDACAO, no ar.** `conferir-no-ar.py`: *"toda categoria com
  arquivo de banco e NOMEADA na frase — faltou: alicate"*. Eu tinha escrito "6 ferramentas de corte":
  total certo, parcelas somando certo, e **errado assim mesmo**, porque o cartao se chama "Alicates e
  corte" e numero que nao usa a palavra do cartao e numero que o leitor nao liga a lugar nenhum. Casca
  **1.14.1**: "6 alicates e cortadores".
- **TRAVA NOVA NO `gerar-links-afiliado.py`, escrita pela execucao que caiu nela.** Rodar `--escrever`
  para gravar **seis** registros novos regerou os **vinte e cinco** que ja estavam certos: URL encurtada
  nova para a mesma busca, sem um unico ganho. O custo so aparece depois — o banco passa a conhecer um
  encurtador que a pagina no ar ainda nao serve, e o `conferir-no-ar.py` reprova exatamente isso, entao a
  ilha ficaria vermelha ate o Sync publicar o banco novo, por causa de uma passada que nao pediu nada
  disso. Foi desfeito com `git checkout --`, **e mao nao e portao**. Agora registro cuja busca crua ja e
  a da tabela e cujo encurtador ja existe e **pulado**; `--regerar-tudo` continua existindo para o caso
  em que a chave mudou, que e o das treze pastilhas.
- **As seis chaves foram medidas na API ANTES de qualquer link nascer** — a licao das treze pastilhas, de
  25/09 de manha, aplicada ao contrario do que a causou. As **31** chaves do banco devolvem oferta, e os
  titulos batem com o produto. Uma desceu um degrau na hora: `torques azulejista corte curvo cortag`
  devolveu **ZERO** e desceu para a FAMILIA, com o degrau escrito em `motivo_da_chave`.
- **Tres pendencias nomeadas**, e a primeira e a que mais importa: nao da para saber, desta nuvem, se o
  torques de corte curvo e o de mosaico com roldanas sao **dois produtos ou duas entradas de catalogo do
  mesmo** — as URLs sao distintas mas a frase de 5 mm e a mesma palavra por palavra, e a busca por SKU do
  curvo devolve zero oferta enquanto a do outro devolve tres. O registro do curvo nasceu sem **nenhuma**
  propriedade tecnica, entao se a resposta for "e o mesmo", ele vira `descartado` com motivo e a
  categoria cai de 6 para 5 **sem perder um so campo verificado**.
- **O que este bloco NAO destravou:** o **4c continua fechado**, e por um motivo diferente do de 12/09.
  Nao e mais "a categoria alicate nao tem um unico item"; e a **16.5** — `/materiais/alicates/` precisa
  de 3 filhas de nivel 3 e nenhuma filha de alicate existe. E a contagem esconde uma distincao: dos tres
  registros de `tipo: torques`, **um so** carrega declaracao tecnica propria, entao por elegibilidade
  `cortador_de_azulejo` esta em 3 e `torques` esta em **1**.
- **Nenhuma URL nova.** As 17 continuam 17, e a semana da 21.4 continua onde estava.
- MEDIDO: `teste-casca` **555** e 0 falha (eram **4** quando o arquivo entrou sem leitor), `teste-f1` 196,
  `teste-f2` 114, `teste-loja` 178, `teste-leads` 211, `teste-tecnicas` 123, `teste-atelie` e
  `teste-prestacao-rejunte` aprovados, todos 0 falha; `validar-banco` **31 materiais**, 0 sem saida de
  compra, 0 piso nao rastreavel, 0 busca sem endereco cru; `cobertura` recontada; `mutacoes-f1` 46/46.
  Sync na revisao **41** e depois **42**, `conferir-no-ar` **488 afirmacoes**.
- Proximo passo: **as tres categorias que sobraram** (`base`, `acabamento`, `apoio`) — e elas **nao** tem
  a linha do esquema que a `alicate` tinha, entao cada uma comeca por decidir que campo exige. A de menor
  atrito e `acabamento` (verniz, impermeabilizante, selador), porque e quimico de fabricante com ficha
  tecnica publicada, que e o mesmo terreno das colas e dos rejuntes; `base` e `apoio` sao genericas e
  provavelmente sem fabricante que declare. E o **BLOCO A espera 30/09**, por ordem do despacho.


---

## 2026-09-25, 19h16Z → 20h58Z — A CATEGORIA ACABAMENTO SAI DE ZERO, E ELA FOI A PRIMEIRA QUE PRECISOU DECIDIR O CAMPO ANTES DE COLETAR

**Ilha em foco** (`foco.md`, desde 24/09). Reserva às 19h16Z, commit `2de100b` — `executando_desde` estava
`null` e o último commit da ilha era de 17h29Z, 106 minutos atrás, então não havia reserva vencida para o git
desempatar (1.1). Rede conferida antes de trabalhar (20.2): `clubedomosaico.com.br` em **200 nas três
passadas**.

**O DESPACHO ABERTO NÃO TINHA ITEM PARA HOJE, e isso foi verificado antes de escolher bloco.** O despacho do
Raphael de 24/09 está em **BLOCO A e mais nada**, e o próprio despacho manda o A **esperar 30/09** ("trocar
título antes do número de 30/09 misturaria duas causas na mesma janela"). Do despacho da Sentinela de 23/09,
o item 1 e o item 2 esperam a leitura de 30/09 e o item 3 está cumprido. Pela **18.5** a verificação vem antes
da construção; não havia o que verificar, e a fila assumiu.

**UMA PROPOSTA ESTAVA MARCADA COMO ABERTA COM A CONDIÇÃO DE FECHAMENTO JÁ CUMPRIDA.** A PROPOSTA 2 de 23/09
pedia que o Raphael respondesse sobre a ordem do foco, *"ou mantendo a aquametria com o motivo escrito em
`foco.md`, ou trocando"*. Ele trocou — em **24/09**, com o motivo escrito. A proposta ficou um dia inteiro
parecendo pendente. É a seção 4 do contrato outra vez, agora dentro do próprio `PROMPT.md`: resumo velho lido
como fato. Fechada nesta execução.

### O QUE FOI FEITO — SETE PRODUTOS, DE DOIS FABRICANTES, E NENHUM DELES NOMEIA O QUE A PEÇA EXPÕE

`dados/materiais-acabamento.json`: quatro vernizes (três da Acrilex, um boletim de piso da Quartzolit), dois
impermeabilizantes e um selador. A lista `categorias_do_vocabulario_sem_nenhum_item` de `dados/cobertura.json`,
recontada pela própria `cobertura.py`, **cai de três para DUAS** — restam `base` e `apoio`.

**O ACHADO, e ele é o motivo de o arquivo existir:** a peça de mosaico pronta expõe **duas** superfícies — a
**pastilha** (as 13 do banco são todas de vidro) e o **rejunte**. **Nenhuma das sete frases de fabricante
nomeia vidro. Nenhuma nomeia rejunte.** Os três vernizes de artesanato da Acrilex listam tela, madeira, papel,
cortiça, cerâmica, gesso e isopor; o verniz da Quartzolit é de **piso**, com liberação de tráfego de carro e
máquina; a borracha líquida é de fachada, telha e laje sem trânsito; o protetor para fachadas é hidrofugante
de revestimento mineral, churrasqueira de tijolo e pedra natural. Pelo princípio dos três estados, para vidro
e para rejunte o estado é `nao_declarado` nos sete: nem recomendar, nem proibir, e dizer que ninguém declarou.
É a faixa **DESCOBERTA** da 14.3 encontrada pela **superfície**, irmã da que a categoria alicate encontrou
pela **espessura** às 16h43Z do mesmo dia — e as duas apontam para o mesmo lugar: **fabricante de obra não
escreve sobre peça de artesanato, e fabricante de artesanato não escreve sobre mosaico.**

**A SEGUNDA METADE É SOBRE A BASE:** o único selador alcançado (`fundo selador quartzolit`) nomeia concreto,
emboço, reboco, pintura PVA ou acrílica e construção a seco, e **não nomeia MDF** — que é a base mais comum
da peça do ateliê e um dos cinco valores de `tipo_por_categoria.base`. A categoria `selador` nasce com um item
que não serve a base que a ilha mais usa, e isso está escrito no dado.

### A DECISÃO DE ESQUEMA, QUE É O QUE ESTE BLOCO TEVE DE DIFERENTE

A `alicate` de 16h43Z era nomeada pela linha do `esquema-banco.json` que autoriza encher uma categoria *"sem
decisão nova — o esquema já diz que campo cada uma exige"*. As três que sobravam **não são nomeadas nessa
linha**, e o `ESTADO.md` das 17h29Z registrou isso com todas as letras: *"cada uma começa por decidir que campo
exige"*. Esta execução tomou a decisão da `acabamento` e a escreveu em `regras_da_categoria_acabamento`
(esquema **versão 4**), em três partes:

1. **A matriz `base × ambiente` fica VAZIA.** Ela é o eixo pelo qual a F2 escolhe **cola** e **rejunte**;
   acabamento não adere nada e não se escolhe por ambiente declarado. Verniz dentro dela viraria candidato a
   colar peça.
2. **O que o fabricante declara mora no objeto `protecao`**, irmão do `corte` do alicate: a frase literal, a
   fonte, e as listas do que a frase **nomeia** e do que ela **NÃO nomeia** — cobrindo o vocabulário inteiro,
   porque o que não entra em nenhuma das duas é silêncio **não lido**, e é assim que faixa descoberta fica
   invisível. Mais `nomeia_rejunte`, que existe porque rejunte não é valor de `base` nem de `material_tessela`
   e mesmo assim é metade da superfície exposta.
3. **As propriedades têm NOME FIXO.** Nome livre é o que faz a segunda execução gravar `secagem_horas` onde a
   primeira gravou `tempo_de_secagem_h`, e aí nenhuma régua compara dois registros. `contato_com_alimento` é
   **obrigatório mesmo quando null**: centro de mesa e tampo são duas coleções desta loja, e campo ausente é
   pergunta que ninguém faz. Nos sete ele é null — ninguém declarou.

### AS DUAS MUTAÇÕES QUE ACHARAM BURACO ANTES DO COMMIT, E É O MELHOR PEDAÇO

`ferramentas/mutacoes-acabamento.py` nasceu junto com o portão, e duas das catorze **passaram** na primeira
rodada:

- **A 05 — momento de uso deduzido do mecanismo do produto.** O portão cobrava motivo no **silêncio**
  (`nao_declarado` sem `motivo_do_momento`) e não cobrava **nada na afirmação**: gravar
  `momento_de_uso: depois_de_rejuntar` num hidrofugante, porque "obviamente" é assim que se usa, passava com
  cara de declaração. Agora momento declarado exige `trecho_que_declara_o_momento`, **e o trecho tem de ser
  pedaço literal da frase do fabricante** — não uma segunda frase escrita por quem preencheu.
- **A 13 — a matriz `base × ambiente` preenchida num verniz.** A regra estava escrita desde que nasceu, em
  prosa, e **nenhuma régua a media**. Agora o `validar-banco` reprova acabamento com qualquer lista de
  `declaracoes` preenchida, e reprova lista vazia sem `motivo_declaracoes_vazias`.

A **07** é a que PRODUZ O MUNDO: faz um verniz **nomear vidro**, que é o estado que nenhum dos sete tem hoje e
do qual o achado central deste arquivo depende. Portão que só funciona enquanto a lista de "nomeia" estiver
vazia não mede a regra, mede o acaso.

**Segunda rodada: 14 de 14 reprovadas, 13 delas só o portão novo viu.**

### DOIS NÚMEROS QUE ESTA EXECUÇÃO SE RECUSOU A PUBLICAR

- **O rendimento da borracha líquida.** A frase colhida por busca diz *"18 kg rende no mínimo 70 m²/L"* —
  mistura a embalagem com a unidade e não fecha em nenhuma das duas leituras. Ficou `valor: null` com o motivo
  escrito, e virou a **mutação 12**.
- **As demãos e o consumo do fundo selador.** A mesma página de resultados devolve "duas demãos" (que é do
  **protetor para fachadas**, outro produto) e "350 mL/m² em duas demãos" (que é do **weber.floor selador de
  base**, produto de piso industrial). Emprestar número de um produto a outro é exatamente o que a regra das
  duas passadas existe para pegar.

### AS DUAS PALAVRAS-CHAVE QUE DESCERAM UM DEGRAU, MEDIDAS ANTES DE VIRAR LINK

As sete chaves foram conferidas na Open API (`--conferir-chaves`) **antes** de qualquer link nascer, que é a
lição das treze pastilhas aplicada ao contrário do que a causou. Duas devolveram **ZERO**: `fundo selador
quartzolit` (a palavra "fundo" não aparece em título de anúncio) e `protetor para fachadas quartzolit` (o
produto é de canal de obra e não é anunciado por esse nome). As duas desceram para a **família** —
`selador quartzolit` e `impermeabilizante fachada quartzolit`, três ofertas cada — com o degrau escrito no
`motivo_da_chave` de cada registro. **Sete links novos, 31 intocados**: a trava escrita às 16h43Z pela execução
que caiu nela segurou.

### A CASCA, E O PORTÃO QUE DESMENTIU A EXECUÇÃO PELA SEGUNDA VEZ NO MESMO DIA

O cartão "Acabamento" do Guia mostrava **0 com o banco em 7**, e a frase de prova anunciava o total do banco
enumerando só quatro categorias — com a quinta entrando, ela teria posto no ar *"o banco tem 38 itens, sendo 7
colas, 5 rejuntes, 13 pastilhas e 6 alicates"*, soma que não fecha. É a mesma família do *"hoje 10 dos 5 itens
esperam link"* que esta ilha já pôs no ar uma vez, e foi o `teste-casca.php` que a pegou, exatamente como
pegou a `alicate` três horas antes. **Casca 1.15.0**, manifest **43**.

### O QUE ESTE BLOCO NÃO É

- **Não é o BLOCO A** do despacho de 24/09, que espera 30/09 por ordem do próprio despacho.
- **Não publica página nenhuma.** A 16.5 exige 3 filhas de nível 3 por categoria e `/materiais/acabamento/`
  continua sem página. **As 17 URLs continuam 17** e a semana da 21.4 continua onde estava.
- **Não abriu o domínio de ninguém.** `acrilex.com.br`, `www.acrilex.com.br`, `corfix.com.br`,
  `www.quartzolit.weber`, `suvinil.com.br` e `vedacit.com.br` em **000 nas três passadas**, com o domínio da
  ilha em 200 nas três. Todo campo carrega `conferir_no_pdf: true`.
- **Não usou a loja da marca como fonte técnica.** A Suvinil publica um selador acrílico e uma seladora para
  madeira — que seriam os dois únicos registros a nomear MDF —, e as duas páginas que a busca devolveu são de
  `loja.suvinil.com.br`, **nível 5** na escada desta ilha, que não sustenta recomendação primária. Nenhuma das
  duas virou registro, e o motivo está escrito em `pendencias_desta_categoria`.

### MEDIDO

**Bancada, tudo sem rede:** `teste-casca` 555 (eram 4 falhas quando o arquivo entrou sem leitor), `teste-f1`
196, `teste-f2` 114, `teste-loja` 178, `teste-leads` 211, `teste-tecnicas` 123, `teste-atelie` e
`teste-prestacao-rejunte` aprovados — todos 0 falha. `validar-banco` com **38 materiais**, 0 sem saída de
compra, 0 piso não rastreável, 0 busca sem endereço cru; `validar-pastilhas` 189 afirmações, 0 item com falha.

**AS SETE BATERIAS DE MUTAÇÃO RODARAM INTEIRAS E NENHUMA MUTAÇÃO PASSOU:** `f1` 46/46, `f2` 50/50,
`pastilhas` 14/14, `cobertura` 14/14, `voz-e-cabeca` 24/24, `arvore` 21/21 e a nova **`acabamento` 14/14**,
com 13 das 14 vistas só pelo portão novo.

**No ar:** Sync forçado, `/status` na revisão **43**, `conferir-no-ar.py` com **488 afirmações e 0 falha**.
A frase servida em `/materiais/` foi lida à mão além do portão: *"Hoje o banco tem 38 itens de fabricante,
sendo 7 colas, 5 rejuntes, 13 pastilhas, 6 alicates e cortadores e 7 produtos de acabamento, e 28 deles ainda
esperam link de loja"* — as parcelas somam o total e as cinco categorias com arquivo de banco estão nomeadas.

*(A revisão ficou em 42 no primeiro Sync: o `--revisao 43` foi passado na passada do `atualizar-manifest.py`
que parou no descasamento de versão da casca, e a passada seguinte não o repetiu. O Sync aplicou os 14 itens
assim mesmo — ele compara sha, não número —, mas `/status` mostrando 42 depois de um bloco é a seção 4 outra
vez. Corrigido em commit próprio, e o número de verdade levou ~4 minutos para chegar por causa do cache do
raw do GitHub.)*

### O QUE DEPENDE DO RAPHAEL — três coisas, e nenhuma é da Fundação

1. **Acesso de leitura da conta `sentinela@`** em `sc-domain:clubedomosaico.com.br` no Search Console. É o que
   destrava a medição desta ilha, e está aberto desde 23/09.
2. **Autorizar, ou não, o 301 de `http` para `https` em todo caminho** — hoje só a home redireciona. A
   proposta está escrita em `dados/indexacao.md` e **não foi aplicada**, porque o BLOCO C proíbe aplicar sem
   autorização item por item.
3. **Acrescentar domínio de fabricante à rede Personalizada do ambiente** (20.1). Hoje `acrilex.com.br`,
   `quartzolit.weber`, `suvinil.com.br`, `corfix.com.br` e `vedacit.com.br` respondem `000`, e **todo o banco
   desta ilha é nível 2 ou 3 por causa disso**. Com os domínios abertos, o banco inteiro sobe para nível 1 e
   as tabelas de substrato dos boletins — que é exatamente onde a resposta sobre vidro e rejunte moraria —
   passam a ser legíveis.

### PRÓXIMO PASSO

As **duas** categorias que sobraram: `base` e `apoio`. As duas herdam o molde de
`regras_da_categoria_acabamento` sem herdar a decisão — cada uma ainda começa por decidir que campo exige. A
`base` é a de maior valor para esta ilha (ela é a primeira pergunta da F2 e de todo tutorial) e a de maior
risco: base de artesanato é genérica e provavelmente sem fabricante que declare, ao contrário do químico. E o
**BLOCO A** do despacho de 24/09 **espera 30/09**, por ordem do próprio despacho.

28/09/2026 10:16Z — BLOCO ENTREGUE: a categoria BASE decide o campo, e a decisão descobre que o vocabulário desta ilha não tem onde pousar TRÊS dos cinco tipos dela

- **A ilha em foco continua sendo esta** (`foco.md`, desde 24/09). Rede reconferida antes de trabalhar como manda
  a 20.2: home em **200**, `/status` em **200** na revisão **43**, e `ferramentas/conferir-no-ar.py .` com
  **488 afirmações e 0 falha** no HTML servido — a porta de entrada da seção 29 conferida antes de qualquer
  outra coisa, e ela estava de pé.
- **O bloco é o item 3 da fila** ("a coleta das categorias vazias"), na categoria `base`, e ele **não coletou
  SKU nenhum**. A metade que saiu é a que o próprio `ESTADO.md` de 25/09 dizia que vinha primeiro: *"cada uma
  ainda começa por decidir que campo exige"*. O motivo de a outra metade não ter saído está medido abaixo e
  está escrito no esquema, não só aqui.

## O ACHADO, E ELE NÃO ESTÁ NA FRASE DO FABRICANTE: ESTÁ DO NOSSO LADO DO BALCÃO

`vocabularios.tipo_por_categoria.base` declara **cinco** tipos — `mdf_cru`, `ceramica_crua`, `cimento`,
`isopor_estrutural`, `moldura`. `vocabularios.base`, que é o eixo pelo qual a **F2 decide cola e rejunte** e a
primeira pergunta que ela faz a quem chega, tem **nove** valores. Cruzando os dois, pela primeira vez:

- `mdf_cru` → **pousa** em `mdf_madeira`.
- `cimento` → **pousa** em `cimento_concreto`.
- `ceramica_crua` → **não tem valor**. O único valor de cerâmica no eixo é `ceramica_esmaltada_porcelana`, que é
  a cerâmica **vidrada**. Vaso de barro cru é o contrário: absorve água e absorve cola. A distinção já estava
  escrita à mão nesta ilha, em 25/09, na `observacao` do registro `acrilex-verniz-acrilico-brilhante` —
  *"Cerâmica crua e cerâmica esmaltada absorvem de maneira oposta, e o fabricante não separa as duas"*.
- `isopor_estrutural` → **não tem valor**, e este é o pior dos três, porque **a regra do que fazer já estava
  escrita no mesmo arquivo**. A linha `poliestireno expandido` de `termos_que_nao_traduzem` diz, com todas as
  letras: *"se virar base (isopor estrutural), entra no vocabulário primeiro"* — e `isopor_estrutural` **já era**
  um dos cinco tipos de `tipo_por_categoria.base`. A condição estava cumprida no próprio arquivo que a escreveu,
  e nada conferia as duas linhas juntas.
- `moldura` → **não é material**. A mesma moldura existe em madeira, MDF, metal e plástico, que são quatro
  valores do eixo. Tipo de base que pousa em quatro lugares ao mesmo tempo não descreve substrato: descreve
  **geometria**, e geometria nesta ilha é a **F1** (`area_moldura = L × A − l × a`), não a F2.

**O preço disso já estava pago no banco, antes desta seção existir.** Dois vernizes da Acrilex carregam `isopor`
e `gesso` **dentro da frase literal do fabricante** — e as duas palavras não existem em `vocabularios.base`.
Então a declaração foi lida, classificada e **descartada em silêncio**. A ilha já sabia ler SILÊNCIO de
fabricante (é o terceiro estado do esquema, e a alicate achou uma faixa pela ESPESSURA e a acabamento pela
SUPERFÍCIE). O que ela não sabia ler era **declaração de fabricante jogada fora por falta de vocabulário
nosso** — a mesma família, do nosso lado. É a terceira faixa descoberta desta ilha e a primeira encontrada pelo
VOCABULÁRIO.

## O QUE FOI ESCRITO, E COMO CADA PEDAÇO É MEDIDO

- **`ponte_do_tipo_para_o_vocabulario_base`** no `dados/esquema-banco.json` (esquema na **versão 5**): os cinco
  tipos, cada um em um de três estados — `pousa`, `sem_valor_no_vocabulario` (com `valor_proposto` e
  `o_que_falta`) ou `nao_e_material` (com `onde_ele_e`). Nenhum fica calado, e isso é portão.
- **`condicionais_do_mapa_de_termos`**, dentro da ponte: toda linha de `termos_que_nao_traduzem` que recusa o
  termo **sob condição** ("entra no vocabulário primeiro") aparece aqui com a condição **medida** e o `por_onde`.
  Duas linhas: `poliestireno expandido` (condição **cumprida**) e `gesso` (condição **não cumprida** — gesso não
  está em `tipo_por_categoria.base` nem no corpus como base de peça; a palavra aparece no banco do outro lado do
  balcão, como substrato de PINTURA na frase do fabricante). Condição escrita e nunca conferida é promessa, e
  uma delas já estava cumprida sem ninguém ver.
- **`regras_da_categoria_base`**: o campo novo é o objeto **`substrato`**, irmão do `corte` da alicate e da
  `protecao` do acabamento — frase literal, fonte, `valor_do_vocabulario_base` (UM valor, nunca lista, porque
  base é feita de um material só), `trecho_que_declara_o_material` obrigatório (herdado inteiro da mutação 05 do
  acabamento: *"disco MDF 20 cm" é nome comercial, e nome comercial não é declaração técnica*), as duas listas
  de **ambiente** cobrindo o vocabulário inteiro (a base é a única categoria cujo produto decide onde a peça
  pronta pode **viver**) e `preparo_declarado`, que é o selador do banco de acabamento visto do outro lado.
- **Propriedades de nome fixo**, e aqui elas são MEDIDA: `forma` (num vocabulário novo, `forma_da_base`, que é a
  lista das seis formas que a F1 calcula), diâmetros, lados, vãos da moldura, espessura, peso, densidade,
  `acabamento_de_fabrica` e **`absorcao_declarada` obrigatória mesmo null** — é a pergunta que decide a regra 6
  da F2 e a que separa barro cru de cerâmica esmaltada.
- **A regra que protege a F1 de si mesma:** a base é a única categoria cujo produto declara exatamente o que a
  F1 pergunta (forma e medidas), e medida colhida em anúncio de marketplace é **nível 6**, que sustenta preço,
  unidade e imagem. Medida de anúncio **nunca** entra em fórmula publicada nem na tabela pré-renderizada.

## O PORTÃO NASCEU ANTES DO DADO, E FOI A BATERIA QUE PROVOU QUE ELE MORDE

`ferramentas/mutacoes-base.py` é a primeira bateria desta ilha que **fabrica o próprio mundo**: ela escreve um
`dados/materiais-base.json` com cinco registros (um por tipo, cobrindo os três estados da ponte), confere que o
mundo certo **passa**, muta vinte vezes — treze no registro e **sete no esquema**, porque a ponte é um documento
que mede outro documento —, restaura tudo e **apaga o arquivo fabricado no fim**. Os textos de fabricante lá
dentro são inventados e marcados como tal; nenhum vai para o repositório.

**A mutação 05 PASSOU na primeira rodada, e ela é o defeito mais caro desta categoria:** o vaso de barro cru
gravado como `ceramica_esmaltada_porcelana`. O portão só consultava a ponte quando o **registro** declarava
`sem_valor_no_vocabulario` — e o caminho caro é o contrário, o registro gravando um valor de verdade num tipo
que a ponte diz que **não pousa**. Esse defeito **não deixa rastro**: some a faixa descoberta e nasce, no lugar
dela, uma recomendação de cola sobre uma superfície que absorve ao contrário da que foi respondida; o registro
fica verde, a ponte continua dizendo a verdade, e as duas nunca se encontram. Agora a ponte manda nas **duas
direções**. **Segunda rodada: 20 de 20 reprovadas, 19 só os portões novos viram.**

A mutação **14** é a que PRODUZ O MUNDO: ela **executa** a ponte (acrescenta `isopor_eps` a
`vocabularios.base`) e mede se o esquema acusa que a ponte envelheceu no mesmo commit em que o vocabulário
cresceu. Sem ela, a ponte viraria, ela própria, o *resumo velho lido como fato* da seção 4 do contrato.

## POR QUE NENHUM SKU FOI COLETADO, E ISSO ESTÁ NO ESQUEMA E NÃO SÓ AQUI

Egresso medido nesta execução, em três passadas, com `clubedomosaico.com.br` em **200** nas mesmas passadas
(seção 20.2 — é isso que separa bloqueio de rede de intermitência de túnel): **000** em `dexco.com.br`,
`duratex.com.br`, `guararapes.com.br`, `arauco.com.br`, `berneck.com.br`, `eternit.com.br`, `brasilit.com.br`,
`termotecnica.ind.br`, `isoeste.com.br` e `leroymerlin.com.br`.

**E a diferença em relação à acabamento, que correu com o mesmo bloqueio, é o CANAL e não a rede:** a acabamento
se sustentou na busca restrita ao domínio, que devolve a frase do fabricante sem abrir a página (nível 3). Nesta
execução o canal de busca disponível devolveu **resumo e tradução** das páginas de painel de MDF, não a frase do
fabricante. `literal_do_fabricante` é a viga de todo este esquema, e gravar paráfrase de resumo naquele campo é
a família do número de tela digitado: **parece conferido**. Então a decisão de campo saiu inteira, com portão e
bateria, e o primeiro SKU nasce na execução em que a frase do fabricante puder ser citada. Está escrito em
`regras_da_categoria_base.o_que_falta_para_coletar_o_primeiro_SKU`, não só neste registro.

## O QUE ESTE BLOCO DELIBERADAMENTE **NÃO** FEZ, E O MOTIVO É A JANELA DE MEDIÇÃO

Ele **não** acrescentou `ceramica_crua_barro` nem `isopor_eps` a `vocabularios.base`. Não é dúvida — é a 12.1 e
o BLOCO A do despacho de 24/09. Acrescentar valor ao eixo muda o que
`/materiais/qual-cola-usar-no-mosaico/` **serve**: a lista suspensa ganha duas opções, a contagem de
`cdm_f2_faixas_descobertas_html()` sai de 9 × 5 × 6 = **270** para 11 × 5 × 6 = **330** combinações, e as duas
bases novas entram na frase que a página já sabe dizer sozinha — *"Não indicamos cola nenhuma, em lugar nenhum,
para: …"* —, porque nenhum fabricante do banco as nomeia. Essa é a página de **posição 7,8**, a melhor do
Arquipélago inteiro, e o BLOCO A espera 30/09 exatamente para não misturar duas causas na mesma janela. Mexer no
corpo dela hoje misturaria três. **A máquina para dizer a verdade já existe na página; falta a decisão, e ela
está escrita, medida e pronta para sair inteira.**

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` verde (38 materiais, 0 sem saída de compra, 0 piso não rastreável), `cobertura.py` recontada
e **sem mudança** — continuam **duas** categorias sem nenhum item (`base`, `apoio`) —, `teste-casca.php` 555
verificações, `teste-f2.php` 114 afirmações, `teste-f1.php` 24 estados com processo próprio,
`teste-prestacao-rejunte.php` 5 afirmações sobre 540 estados da F2 e 180 da F1, `teste-tecnicas.php` 123
verificações. **E as baterias de mutação inteiras, porque a mudança foi no ESQUEMA e o esquema é lido por
quase todas:** `mutacoes-base.py` 20 de 20, `mutacoes-f2.py` 50 de 50, `mutacoes-arvore.py` 21 de 21,
`mutacoes-rejunte.py` 16 de 16, `mutacoes-cobertura.py` 14 de 14, `mutacoes-acabamento.py` 14 de 14,
`mutacoes-pastilhas.py` 14 de 14 e `mutacoes-tecnica-x-material.py` 9 de 9 — **158 mutações, nenhuma passando**.
E `conferir-no-ar.py` refeito no fecho: **488 afirmações, 0 falha**, o mesmo número da abertura, que é a prova de
que o site não foi tocado. **Nenhuma URL nova: as 17 continuam 17**, a semana da 21.4 continua
onde estava, e **não houve Sync** — nada do que este bloco mexeu é conteúdo publicável (seção 4).

## DE PASSAGEM, UMA MEDIÇÃO QUE DESMENTE UMA INSTRUÇÃO DO PRÓPRIO REPOSITÓRIO (item 4 da fila)

O item 4 da fila diz que a linha da peça no `ARVORE.md` é *"conserto de TESTE, não de documento"*, e a seção 5
daquele arquivo explica por quê: o mapa é por requisição e a peça só entra nele quando está sendo servida.
**Medido com a bancada nesta execução, servindo a peça de verdade: a explicação está certa e a conclusão está
incompleta.** O mapa ganha a chave **`quadro-flores-do-campo`** — slug nu, nível 2, mãe `loja` —, e **não**
`loja/quadro-flores-do-campo`. Toda outra entrada de nível 2 ou 3 é chaveada pelo **caminho inteiro**; a peça é a
única chaveada pelo slug nu, porque o filtro `cdm_arvore` da Loja escreve `$mapa[ $peca->post_name ]`. Na tela
funciona, e é por isso que ninguém viu: quem pede a trilha da peça passa o `post_name`. O que não funciona é
escrever a peça numa tabela que é **lida por caminho**.

**Isso deixa de ser conserto e vira decisão** — ou o filtro passa a chavear pelo caminho (e é código de snippet
que serve `/loja/quadro-flores-do-campo/`, página **no ar**, com peça publicada por uma pessoa de verdade), ou a
tabela declara a exceção e o portão passa a admiti-la. Escolher entre duas opções defensáveis não é da bancada
(19.2), e as duas mexem em coisa que está servindo. **Não foi executado nesta passada**, e está escrito na seção
5 do `ARVORE.md` para a próxima execução não redescobrir. `teste-casca.php` continua em 555 verificações e
`mutacoes-arvore.py` em 21 de 21 depois da nota.

- **Próximo passo desbloqueado:** a categoria **`apoio`**, que é a última das cinco e a única que ainda não tem
  decisão de campo nenhuma — e ela é a de menor risco de egresso, porque espátula, óculos e luva são EPI e
  ferramenta com ficha de fabricante do mesmo terreno da alicate, que já saiu de zero por busca. A `base`
  espera duas coisas, nesta ordem: (1) a decisão do Raphael sobre os dois valores novos do vocabulário, que só
  pode sair **depois** da leitura de 30/09; (2) o egresso de fabricante, que é o item 3 do "o que depende do
  Raphael" e resolve o banco inteiro junto. E o **BLOCO A** do despacho de 24/09 continua esperando 30/09, por
  ordem do próprio despacho.

---

# 28/09/2026 14h55Z — A CATEGORIA `APOIO` RECEBE A DECISÃO DE CAMPO, E COM ELA NENHUMA DAS SETE FICA SEM A SUA

Esquema na **versão 6**, casca **1.15.0 intocada**, manifest **44**, `conferir-no-ar.py` com **488
afirmações e 0 falha** no ar — o mesmo número da abertura, que é a prova de que o site não foi tocado.
**Nenhuma URL nova: as 17 continuam 17**, a semana da 21.4 continua onde estava.

## A ESCOLHA DA ILHA, E O QUE A FILA DEIXOU DE LADO

`foco.md` nomeia a **clubedomosaico** desde 24/09, então pela **1.2** não há escolha de ilha a fazer.
Reserva por commit às **13h20Z**, aceita na primeira tentativa. Nenhum PR aberto; a branch
`claude/dreamy-mccarthy-kf0p74` não tem commit além do `main`. Rede pela **20.2**, medida e não herdada:
três passadas, `clubedomosaico.com.br` em **200** nas três e `/wp-json/clubedomosaico/v1/status` em **200**
nas três.

Pela **18.1** li o topo do `PROMPT.md` antes de pegar bloco, e **os dois despachos abertos desta ilha não
têm item acionável hoje** — não por falta de fôlego, e sim por ordem escrita: o **BLOCO A** do despacho do
Raphael de 24/09 espera 30/09 pelo próprio texto dele; os itens **1** e **2** do despacho da Sentinela de
23/09 já fecharam a metade de máquina e têm a terceira condição de pronto na **leitura de 30/09**; o item
**3** foi fechado pelo Pente Fino nesta manhã. Então a fila normal, e nela o próximo passo estava escrito
com todas as letras pela execução das 10h16Z: **a categoria `apoio`**, a última das sete sem decisão de
campo.

## A FORQUILHA QUE DECIDE A CATEGORIA INTEIRA, E ELA NÃO É ARRUMAÇÃO

`apoio` é a única categoria desta ilha cujos tipos se dividem em dois ramos que **não se comparam entre
si**, e a divisão muda **o que o erro custa**. Espátula, desempenadeira, pinça e marcador agem sobre o
**material** — errar neles estraga a **peça**. Óculos e luva agem sobre a **pessoa** — errar neles machuca
**quem monta**. Uma lista só poria luva ao lado de desempenadeira como se a escolha fosse do mesmo tipo, e
não é: desempenadeira se escolhe pelo que ela toca, luva se escolhe pelo que ela impede de tocar em você.
É a assimetria de custo da seção 10 aplicada a um vocabulário que já existia e que ninguém tinha cruzado.

Vocabulário novo `ramo_do_apoio` e ponte `ponte_do_tipo_de_apoio_para_o_ramo`, irmã da ponte da `base`
escrita seis horas antes e pelo mesmo motivo. **Seis tipos, quatro na ferramenta e dois no EPI**, nenhum
calado, e o portão reprova registro cujo `servico.ramo` discorde da ponte — nas **duas** direções, que é a
trava que a mutação 05 da base ensinou.

## O PREÇO JÁ ESTAVA PAGO NO BANCO, PELA SEGUNDA VEZ NO MESMO DIA

**CINCO frases de fabricante, em QUATRO registros de TRÊS categorias diferentes, nomeiam um apoio — e
nenhuma tinha campo para onde ir.** Foram lidas, classificadas e descartadas em silêncio, exatamente como
`isopor` e `gesso` na manhã de hoje.

- **`pastilhart-af1500`** (pastilha), em `propriedades.assentamento_recomendado.declarado_como` e em
  `preparo`: *"desempenadeira de **borracha** para não riscar"*.
- **`cascola-cascorez-extra`** (cola), em `preparo`: *"Aplicação com **pincel** ou **rolo**"*.
- **`quartzolit-verniz-protetor-para-pisos`** (acabamento), em `protecao.literal_do_fabricante`:
  *"aplicar com **rolo de espuma de poliéster** limpo e seco"*.

**A primeira delas é a que desenhou o campo novo.** O fabricante da PASTILHA não nomeia só a ferramenta:
ele nomeia o **material dela**, e diz por quê. As 13 pastilhas do banco são todas de vidro. O que decide se
a peça sai riscada não é "desempenadeira", é "de borracha" — então o objeto `servico` tem
`material_de_contato` com vocabulário próprio, e o valor exige o **trecho literal** da frase que o declara.
Gravar só a ferramenta perderia exatamente a metade da declaração que importa.

## É A PRIMEIRA CATEGORIA CUJA DECLARAÇÃO VEM DO OUTRO LADO DO BALCÃO

Quem diz qual desempenadeira usar **não é o fabricante da desempenadeira**. Isso é novo nesta ilha e não
tinha onde ser guardado. Por isso o portão mais forte deste bloco **não olha registro de apoio nenhum**:
`exigencias_de_apoio_ja_declaradas_no_banco` varre as **outras** categorias, só nos campos que carregam
frase de fabricante (a nossa `observacao` fica de fora de propósito — varrer o registro inteiro leria o
nosso julgamento como declaração), e anda nas **duas direções**: ocorrência encontrada tem de estar
listada, e ocorrência listada tem de ser encontrada. Sem a segunda metade, uma linha sobreviveria à saída
do registro que a sustentava, e a seção viraria o *resumo velho lido como fato* da seção 4.

## O VOCABULÁRIO E A FRASE DOS FABRICANTES APONTAM PARA LADOS OPOSTOS

Dos **seis** tipos que `tipo_por_categoria.apoio` declara, **UM** aparece no banco (desempenadeira). Dos
**dois** termos que mais aparecem no banco (`pincel`, `rolo`), **ZERO** estão no vocabulário. E há uma
terceira metade que ninguém tinha cruzado: a propriedade `forma_de_aplicacao` da categoria acabamento
declara *"aerossol, rolo, pincel, trincha"* — e a **interseção dela com `tipo_por_categoria.apoio` é
VAZIA**. Duas metades contando a mesma coisa sem nunca se falarem, que é a família de defeito que esta ilha
mais nomeia.

`pincel` e `rolo` ficam como `sem_valor_no_vocabulario`, com `valor_proposto` e `o_que_falta` escritos, e
**não** entram hoje. E o motivo é diferente do que trava o vocabulário da `base`: nenhuma página lê
`tipo_por_categoria`, e a categoria tem zero itens, então isto **não** é a espera da leitura de 30/09 — é a
regra de crescimento, e só. Valor de vocabulário controlado nasce junto com o primeiro registro que o usa.

## O SILÊNCIO QUE ESTE BLOCO TRANSFORMOU EM NÚMERO

**38 registros, cinco ocorrências, TODAS no ramo `ferramenta_de_aplicacao`. O ramo
`equipamento_de_protecao_individual` tem ZERO:** nenhuma frase de fabricante no banco inteiro nomeia luva,
óculos ou qualquer proteção de quem monta.

Isso importa nesta ilha e não em qualquer uma, porque **a F2 recomenda os dois produtos em que a proteção
deixa de ser opcional**: `loctite-durepoxi` e `quartzolit-rejunte-epoxi` estão no banco e são servidos pela
ferramenta. A ilha recomenda epóxi a uma pessoa em casa e não tem **uma** declaração de fabricante sobre
proteção para pôr ao lado disso.

**O que o bloco NÃO fez, de propósito:** não escreveu recomendação de EPI nenhuma. Deduzir "epóxi pede
luva" do mecanismo do produto é afirmar pelo fabricante, que a seção 8 proíbe, e é o mesmo defeito que a
mutação 05 do acabamento pegou no `momento_de_uso`. O que ele fez foi tornar `risco_declarado`
**obrigatório mesmo null**, para que a primeira coleta responda *"ninguém declarou"* em vez de a pergunta
não ser feita. O que destrava é a FISPQ do epóxi — nível 1, em PDF no domínio do fabricante, o mesmo
egresso fechado que segura o primeiro SKU da `base`. **É o terceiro bloco seguido desta ilha a parar na
mesma porta.**

## UM VOCABULÁRIO QUE NÃO FOI REUSADO, E O MOTIVO É MEDIÇÃO E NÃO GOSTO

`momento_de_uso` já existia (`antes_de_colar`, `depois_de_rejuntar`, `ambos`, `nao_declarado`) e seria o
candidato óbvio para a etapa do apoio. **Ele não tem valor para o ato de COLAR** — porque nasceu para o
acabamento, que por definição nunca cola. E a Cascola declara o pincel e o rolo exatamente para colar.
Reusá-lo obrigaria todo aplicador de cola a responder a uma pergunta que não é a dele, e a resposta menos
errada seria falsa. Nasceu `etapa_da_montagem`, com o motivo escrito no campo, em vez de um valor torcido
para caber.

## AS DUAS COISAS QUE A BATERIA ACHOU ANTES DO COMMIT, E AS DUAS NO PORTÃO NOVO

`ferramentas/mutacoes-apoio.py` é a **segunda** bateria desta ilha que **fabrica o próprio mundo** — e a
primeira que também muta o **banco de verdade**, porque a declaração que importa mora nas outras
categorias. 24 mutações: 14 no mundo fabricado, **6 na AF1500, na Cascorez e no verniz de pisos**
(restaurados byte a byte no fim) e 4 no esquema.

- **A mutação 15** passou na primeira rodada. A varredura comparava os dois lados por `(registro, termo)`,
  e a AF1500 nomeia a desempenadeira em **dois campos** — então apagar **uma** das duas linhas passava
  verde: a outra cobria a que sumiu. **O texto da própria seção já dizia, com essas palavras, "a varredura
  mede CAMPO, não registro".** A prosa estava certa e o código não a cumpria, que é pior que prosa errada,
  porque quem lê acredita. A chave passou a ser `(registro, campo, termo)`.
- **A mutação 20** passou também. Trocar o estado de `aerossol` de `nao_e_ferramenta` para
  `sem_valor_no_vocabulario` satisfazia todos os campos que aquele estado exige — e a próxima execução
  criaria um tipo de apoio chamado `aerossol`, que é **embalagem**. O que separa `aerossol` de `pincel` e
  `rolo` é medível: **onde o termo aparece.** Os dois últimos aparecem em `preparo` e em
  `literal_do_fabricante`, que é prosa de fabricante; `aerossol` aparece uma vez só, em
  `propriedades.forma_de_aplicacao.valor`, que é um **slot do nosso próprio esquema**. Propor crescimento de
  vocabulário a partir de um campo que nós mesmos criamos não é ler declaração nenhuma. Agora o crescimento
  do vocabulário também se apoia em `literal_do_fabricante`, que é a viga deste esquema inteiro.

Segunda rodada: **24 de 24 reprovadas, e as 24 só o portão novo viu.**

## DE PASSAGEM, UMA FERRAMENTA NO DISCO FORA DO MANIFEST — E QUEM A ACHOU FOI O PRÓPRIO PORTÃO

`ferramentas/mutacoes-base.py` nasceu nesta manhã, às 10h16Z, e **não entrou no manifest**. O
`atualizar-manifest.py --gravar` **se recusou a gravar** enquanto a linha não existisse: *"FERRAMENTA NO
DISCO FORA DO MANIFEST"*. Entrou com descrição própria, e a linha dela diz que entrou tarde e por quem.

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` verde (38 materiais, 0 sem saída de compra, 0 piso não rastreável), `cobertura.py`
recontada e **sem mudança** — continuam **duas** categorias sem nenhum item (`base`, `apoio`), porque
decisão de campo não é SKU —, `validar-pastilhas.py` 189 afirmações, `tecnica-x-material.py` reescrito sem
mudança, `teste-casca.php` 555 verificações, `teste-f2.php` 114 afirmações, `teste-f1.php` 196 sobre 24
estados com processo próprio, `teste-prestacao-rejunte.php` 5 afirmações sobre 540 estados da F2 e 180 da
F1, `teste-tecnicas.php` 123, `teste-loja.php` 178 sobre 72 estados e `teste-leads.php` 211 sobre 8.

**E as baterias de mutação inteiras, porque a mudança foi no ESQUEMA e o esquema é lido por quase todas:**
`mutacoes-apoio` 24/24, `mutacoes-base` 20/20, `mutacoes-f2` 50/50, `mutacoes-f1` 46/46, `mutacoes-arvore`
21/21, `mutacoes-rejunte` 16/16, `mutacoes-cobertura` 14/14, `mutacoes-acabamento` 14/14,
`mutacoes-pastilhas` 14/14 e `mutacoes-tecnica-x-material` 9/9 — **228 mutações, nenhuma passando**.

## DESEMBARQUE E VERIFICAÇÃO NO AR

O `dados/esquema-banco.json` é item **`publicar: true`** do manifest — a casca e a F2 leem a *option*
`clubedomosaico_dados_esquema-banco` em tempo de requisição. Então este bloco **é publicável**, e o Sync
foi acionado: **revisão 44 aplicada às 14h57Z, `/status` batendo com o manifest, um disparo só.**
*(A execução das 10h16Z escreveu a versão 5 do esquema sem subir a revisão e registrou "não houve Sync";
o site ficou na 43 desde 25/09. A subida para 44 desembarcou as duas de uma vez.)*

**A prova de que o desembarque NÃO mexeu na página da posição 7,8**, que é o que o BLOCO A exige até
30/09: `/materiais/qual-cola-usar-no-mosaico/` continua servindo **270 combinações** e **45** linhas na
tabela — `9 × 5 × 6`, os mesmos números de antes —, medido no endereço **canônico** e no mesmo endereço
**com quebra de cache**, que devolveram o mesmo número. As três chaves que a F2 lê do esquema
(`vocabularios.base`, `.ambiente`, `.material_tessela`, o `mapa_de_termos_do_fabricante` e as
`regras_de_elegibilidade`) **não foram tocadas**: a versão 6 só acrescenta chaves novas, e nenhuma página
percorre `vocabularios` de forma genérica. E `conferir-no-ar.py` refeito depois do Sync: **488 afirmações,
0 falha**, o mesmo número da abertura.

- **Próximo passo desbloqueado:** o que sobra das duas categorias vazias **não é mais decisão de campo, é
  CANAL**. `base` e `apoio` têm regra escrita, portão de pé e bateria verde, e as duas esperam a mesma
  coisa: uma frase de fabricante que esta nuvem consiga **citar literalmente** — o egresso direto está em
  000 e o canal de busca devolveu resumo e tradução nas duas tentativas de hoje. O item que resolve as
  duas junto é o **egresso de fabricante**, que já está na lista do que depende do Raphael. Enquanto isso,
  a fila útil desta ilha é a leitura de **30/09**: ela é a terceira condição de pronto dos itens 1 e 2 do
  despacho da Sentinela de 23/09, é o que libera o **BLOCO A** (CTR das três páginas de primeira página) e
  é o que autoriza a decisão do Raphael sobre os dois valores novos de `vocabularios.base`.

28/09/2026 16:17Z — DESPACHO DA SENTINELA DE 28/09 ENTREGUE, quatro itens inteiros e meio: cinco camadas, e DUAS contagens da ronda corrigidas pela medição

Revisão **46** no ar. *(A 45 levou o bloco; a 46 e a decisão da 25.2-b, escrita no `esquema-banco.json` depois de o manifest da 45 estar fechado — sha velho no manifest é commit sem entrega com um passo de silêncio a mais.)* Casca **1.16.0**, Loja **1.3.0**, F1 **1.4.0**, F2 **1.6.0**, Ateliê **1.4.0**,
Tecnicas **1.2.0**. Foi a primeira ronda diária técnica que esta ilha recebeu, e o despacho dela tinha
cinco itens; pela 18.2 correção sai inteira, e pela 18.3 o que sobrou está reescrito no `PROMPT.md` com o
motivo. A ilha estava livre (`executando_desde: null`), a rede respondeu 200 nas duas tentativas da 20.2, e
o despacho do Raphael de 24/09 não furou a fila porque o único bloco aberto dele (o **BLOCO A**) espera
30/09 por ordem do próprio despacho.

**O ACHADO QUE MUDA O QUE O ITEM 2 ERA.** A ronda escreveu que os estados com parâmetro de
`/materiais/qual-cola-usar-no-mosaico/` não saíam do índice e que a reconferência do conserto de 25/09
tinha falhado nessa metade. Falhou mesmo — mas a causa não é a que o nome do defeito sugere, e ela só
aparece lendo as **duas** ferramentas lado a lado: **elas liam a MESMA pergunta de dois jeitos opostos.**

- O `escolheu` da F1 pergunta `isset( $_GET['forma'] )` — **a presença** do parâmetro.
- O `escolheu` da F2 pergunta `isset( $rot['base'][ $base ] )` — **a validade do valor**.

As três URLs que a ronda mediu (`?base=ceramica&onde=externo`, `?base=mdf`,
`?base=ceramica&caco=louca&junta=fina&onde=interno`) têm os quatro **nomes de parâmetro reais** e **nenhum
valor que exista** no vocabulário — as chaves são `ceramica_esmaltada_porcelana`, `externo_exposto`,
`mdf_madeira`, `caco_louca`, e `junta` é número. Então a F2 respondia "não escolheu nada" e a página entrava
no índice com três endereços a mais. **E a F1 passou pelo motivo oposto e igualmente por acidente:** a régua
de 25/09 a mediu com `?forma=vaso&caquinho=medio`, em que `forma` foi enviado. Com `?caquinho=medio`
sozinho ela teria falhado igual. **Duas irmãs, cada uma acertando o portão da outra por sorte.**

O conserto separa as duas perguntas, e a separação é a parte que vale:

- **`escolheu` manda na TELA** e continua medindo o **valor**, nas duas. Valor fora do vocabulário volta ao
  padrão em silêncio e a página que sai é a âncora; dizer "você escolheu" sobre uma escolha que a página não
  honrou seria trocar um defeito de índice por um defeito de texto.
- **`cdm_fX_tem_parametro()` manda no `noindex`** e mede a **presença**. Para essa pergunta o valor não
  importa: `?base=lixo` é um endereço diferente servindo o MESMO HTML, que é a definição de duplicata — e o
  conjunto dos valores inválidos é **infinito**, enquanto o das escolhas válidas é finito.
- Só os parâmetros **da própria ferramenta**, nunca "qualquer query": `noindex` em toda URL com `?`
  alcançaria a paginação e a busca do núcleo, e tirar do índice página que rankeia é o lado caro da borda —
  esta ilha tem TRÊS páginas na primeira página do Google.

**E um buraco medido de brinde:** a lista de parâmetros da F1 estava escrita à mão dentro do `escolheu` e
nomeava `d`, `h`, `l` e `a` — **esquecendo o `d2`**, o diâmetro do fundo do cone, que existe desde que a
forma cônica existe. `cdm_f1_parametros()` agora deriva os campos de `cdm_f1_formas()`, e a bancada afirma
que toda medida de toda forma está na lista. `?d2=12` sai com `noindex` no ar.

**A SEGUNDA CONTAGEM CORRIGIDA — O ITEM 3 ERA 27 E SÃO 5.** A ronda contou 27 imagens com `alt=""` nas
cinco páginas de peça e pediu que "todas" ficassem com alt não vazio. Contadas de novo aqui, imagem por
imagem no HTML servido, elas se separam em duas famílias e a separação muda o conserto:

- **5 são a foto de DESTAQUE** (`attachment-post-thumbnail`, do bloco do núcleo, que lê
  `_wp_attachment_image_alt` da biblioteca de mídia). Nenhuma foto da artesã tem esse campo. É a foto
  **principal** de cada peça, a que `Product.image` aponta, e nesta ilha a foto **é** o produto — a própria
  `/loja/` diz "a foto é a da peça que você vai receber". **Este é o defeito.**
- **22 são as miniaturas da tira do carrossel**, e o `alt=""` delas é **deliberado**, com o motivo escrito em
  `cdm_loja_miniaturas_html()` desde que a tira nasceu: a miniatura repete a foto que já tem `alt`
  descritivo logo acima, e o nome do controle está no `<a>`, num `<span class="cdm-gal-so-leitor">`. Imagem
  decorativa que repete conteúdo vizinho leva `alt=""` — é a regra, não a exceção. **Preenchê-las para o
  número chegar a zero faria o leitor de tela ler a peça inteira duas vezes.** Régua que não sabe distinguir
  decorativo de descritivo cobra a piora, então a régua nova deixa a tira de fora **por nome**.

**O ALT AGORA SAI DE UMA FUNÇÃO SÓ.** Eram três lugares: o molde do carrossel escrevia
`<título>, mosaico em <base>, foto N`, o cartão da vitrine escrevia a mesma frase de novo, e o núcleo não
escrevia nada na foto de destaque. Agora os três chamam `cdm_loja_alt_da_foto()`, no formato que o despacho
recomenda — **técnica na frente da base**, porque quem olha a foto vê louça quebrada, não vê MDF. No ar:
`Vaso com flores em cerâmica — pica-sete (louça quebrada), foto 1`. Com uma foto só o "foto 1" não entra:
seria ruído lido em toda peça da vitrine. E o `alt` da artesã **sempre vence** — o filtro só entra quando o
campo está vazio.

**O ITEM 1 FOI CONSERTADO DOS DOIS LADOS, e o despacho tinha razão em exigir os dois.** O campo
`_cdm_medidas` de quatro peças trazia a unidade dentro do valor (`46x36cm`, `35cm de diâmetro`) e o molde
acrescentava ` cm` depois, nos **três** lugares que servem medida — a frase da ficha (que vira o
`description` do `Product`), o `additionalProperty` do JSON-LD e a linha do cartão. Consertar só o molde
deixaria o banco com quatro formatos; consertar só o dado deixaria o molde pronto para dobrar o próximo
valor que chegasse por outro caminho. Entraram: `cdm_loja_medida_normalizada()` (o que se grava),
`cdm_loja_medida_na_tela()` (o que se serve), a normalização no `/atelie/` na hora de salvar, e uma migração
idempotente presa a uma chave de option para as peças que já existiam. **No ar:** `40×28 cm`,
`35cm de diâmetro`, `46×36 cm`, `46cm de diâmetro`, `46×37 cm`.

**E O QUE ELAS NÃO FAZEM:** reescrever a frase da artesã. `35cm de diâmetro` é texto dela, tem **uma**
unidade, e sai como ela escreveu — o que se tira é a unidade REDUNDANTE, a do fim do valor, no lugar exato
onde o molde ia pôr a dele. Valor com uma unidade por dimensão (`12 cm x 5 cm`) fica **intocado**: tirar a
última daria `12 cm × 5`, que é pior que o defeito.

**O ITEM 4 É O QUE O PRÓPRIO DESPACHO DISSE QUE ERA:** *"não é o texto de uma página: é qual camada emite a
etiqueta e para quais tipos de página"*. E é o **mesmo desenho** que fez a etiqueta de robô sair dobrada em
25/09, com o sintoma **invertido** — lá o excesso, aqui a falta, e falta não tem cor na tela. Quem tinha
snippet próprio imprimia a sua num `wp_head` paralelo (as duas ferramentas, os dois tutoriais, as cinco
peças pela Loja) e as **oito páginas da casca não tinham quem imprimisse**. Agora **quem tem `description`
DECLARA pelo filtro `cdm_descricao`; quem imprime é a casca, uma vez.** As oito nasceram entre **121 e 143**
caracteres, nenhuma repetida, e a home é tratada à parte porque `cdm_casca_slug_atual()` devolve vazio na
frente do site — sem essa linha o conserto pularia justamente a URL mais visitada da ilha.

**O ITEM 5 e o portão que estava medindo a pergunta errada.** Os 13 itens (7 de acabamento, 6 de alicate)
estavam com `afiliado.degrau` em `null` servindo degrau 4 na tela, e o validador aprovava porque cobrava o
degrau de quem tinha `afiliado.url` — a ficha de produto. **Item que serve BUSCA não tem `url`**, então a
regra velha nunca alcançava o degrau 4, e o esquema dizia o mesmo em `obrigatorio_quando`. Agora o degrau é
cobrado de quem **serve** link, a escada é contada no relatório — **1:1 · 2:5 · 3:4 · 4:28, soma 38** — e
`ferramentas/mutacoes-degrau.py` (8 mutações nos **cinco** bancos, porque o buraco era do portão e não do
arquivo) reprova 8 de 8, **4 delas só pelo portão novo**. A regra antiga fica guardada no esquema em
`obrigatorio_quando_ate_28_09_2026`, porque ela explica um número do histórico.

**A SEGUNDA OBSERVAÇÃO DO DESPACHO FOI DECIDIDA**, como ela pedia: a **25.2-b nomeia um CONCEITO, não um
campo**. Nesta ilha o conceito tem **dois** campos e não um — `url_busca_gerada_em` declara o sucesso e
`motivo_sem_url_busca` declara o fracasso —, e o par cobre os dois desfechos que a regra nomeia. Um campo
`encurtamento_tentado_em` sozinho cobriria só o carimbo e diria "tentei" sem dizer o que aconteceu. Está
escrito em `dados/esquema-banco.json`, em `e_o_campo_de_tentativa_da_25_2_b`.

**O QUE NÃO SAIU, E O MOTIVO É DESPACHO DE PRIORIDADE MAIOR.** A **faixa** de 120 a 160 nas quatro páginas
que já tinham `description` — `qual-cola` (183), `quantas-pastilhas` (165), `picassiete` (192), `trencadis`
(189). **Três delas estão na primeira página do Google** e o **BLOCO A do despacho do Raphael de 24/09**,
que pela 18.1 vem antes deste, diz com todas as letras que espera **30/09**, porque *"trocar título antes do
número de 30/09 misturaria duas causas na mesma janela"*. A `description` é a outra metade da mesma promessa
de SERP. **E é por isso que o pedido de cumprir a Proposta 1 no mesmo movimento não foi obedecido:** fazer só
a `description` agora seria a pior das três opções — mexeria na janela de medição sem entregar a alavanca
inteira. A régua no ar **já mede as quatro** e **imprime o número delas** para não ser esquecido; fechar isto
depois de 30/09 é tirá-las da lista `TRAVADAS_ATE_30_09`.

**BANCADAS.** Casca 563, Loja 196, F1 200, F2 119, Tecnicas 123, Ateliê 289, Leads 211, Prestação 5 — zero
falha. Validador do banco verde. **E no ar: `conferir-no-ar.py` com 501 afirmações e 0 falha** (eram 488 na abertura; as 13 novas são as réguas dos quatro itens). **E cada régua nova foi provada contra o defeito que a fez nascer, não
contra o conserto:** revertida a condição da F2, a bancada reprova servindo
`<meta name='robots' content='max-image-preview:large' />` nas três URLs — o texto exato que a ronda mediu
no ar; revertida a da F1, ela reprova no `d2`. **A régua da unidade dobrada foi escrita ERRADA na primeira
tentativa e o próprio teste pegou:** com `\b` antes da unidade ela **não reconhecia** `46x36cm cm`, porque
entre o `6` e o `c` não há fronteira de palavra. É a família da régua de robô que media a **aspa** em vez da
diretiva, que esta ilha pagou em 25/09 — régua que não reconhece o defeito que a fez nascer aprova o
desastre calada. Agora ela exige o número na frente, e a bancada afirma as duas direções.

**E as mutações de `noindex` da F1 e da F2 estavam a caminho de virar INERTE**, que é o pior dos dois
estados: a bateria continuaria verde dizendo que mediu. Foram retargetadas para a condição nova e ganharam
uma **mutação nova** que escreve de volta a regressão exata de 28/09 — o `noindex` voltando a depender do
valor. **Rodadas no código final: F2 51 de 51 reprovadas, F1 47 de 47, Loja com as 37 pegas, degrau 8 de 8 —
zero passou, zero inerte, zero sem compilar.**

**E UMA BANCADA VERMELHA ACHADA DE PASSAGEM, QUE NÃO ERA DESTE DESPACHO.** `conferir-atelie-no-ar.py`
estava com **2 falhas** e as duas eram da régua, não do site: ela procurava a frase literal
`content="noindex, follow"` com **aspas duplas** — as do `echo` que o snippet do Ateliê fazia num `wp_head`
próprio — e quem imprime a etiqueta desde a casca **1.13.0** (25/09) é o `wp_robots()` do **núcleo**, com
aspas **simples**. O painel sai do índice corretamente e a régua o reprovava. **É exatamente a cicatriz que
`conferir-no-ar.py` pagou em 25/09** — *"a etiqueta de robô se mede pela diretiva e pela contagem, nunca
pela aspa"* — e o conserto daquele dia **passou ao lado desta bancada**, que ficou vermelha três dias sem
ninguém olhar. Pior que reprovar o certo: a mesma régua **passaria a vazio** num painel que saísse do índice
por engano, porque a frase com aspa dupla é falsa nos dois mundos. Agora ela mede a **diretiva** e **conta**
as etiquetas, como a irmã. **184 afirmações, 0 falha, 3 puladas** (as três dependem do token, e o token não
foi usado nesta execução).

- **Próximo passo desbloqueado:** a leitura de **30/09**. Ela continua sendo o que libera o **BLOCO A** (CTR
  das três páginas de primeira página, com o veredito em 08/10), e agora ela libera também a **metade que
  falta do item 4** — as duas são a mesma promessa de SERP nas mesmas páginas e saem no mesmo movimento, que
  é exatamente por isso que nenhuma das duas saiu hoje. O que **não** depende dela continua sendo o egresso
  de fabricante, que trava as duas categorias vazias (`base` e `apoio`) e está na lista do Raphael.

# 30/09/2026, 10h16Z — A PORTA DO EGRESSO NÃO ESTAVA FECHADA: ESTAVA PELA METADE, E QUATRO EXECUÇÕES A CHAMARAM DE FECHADA

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h16Z** com `executando_desde` e push
aceito na primeira tentativa. **NENHUMA URL NOVA** — a ilha segue em 17 —, **nenhum título e
nenhuma `description` mudaram**: o BLOCO A do despacho do Raphael de 24/09 continua intocado e a
janela de medição de 30/09 segue limpa. Manifest e `/status` na revisão **51**.

## A PORTA DE ENTRADA, ANTES DE QUALQUER BLOCO (seção 29.2)

`conferir-no-ar.py`: **519 afirmações, 0 falha** na origem. `leitura-do-visitante.py`:
**REPROVADO com 1 defeito, e é o esperado** — o soft 404 do hospedeiro (404 na 1ª leitura, 200 na
2ª, `x-proxy-cache: HIT`, `max-age=7200`), aberto em 29/09, com dono escrito e fora do alcance de
qualquer snippet daqui. **Nenhum defeito novo.** Rede pela 20.2: três passadas em
`clubedomosaico.com.br`, 200 nas três, com `aquametria.com.br` em 200 nas mesmas.

## O QUE ESTE BLOCO É, E POR QUE NÃO É O BLOCO A

O passo que o registro de 29/09 deixou nomeado como desbloqueado era **a leitura de 30/09** — é
hoje. **Ela não pode ser feita daqui, e agora isso está medido por dois lados independentes:** a
conta de serviço `sentinela@` não tem acesso a `sc-domain:clubedomosaico.com.br` (escrito em
`dados/search-console-2026-09-23.md` desde 23/09) **e a credencial não está neste ambiente** —
`GOOGLE_SA_B64`, `GOOGLE_SA_JSON` e `GOOGLE_SA_FILE` estão as três ausentes, conferido nesta
execução. Sem uma das duas, o BLOCO A e a metade que falta do item 4 do despacho de 28/09 (a faixa
de 120 a 160 nas quatro `description`) continuam travados, e **o veredito de 08/10 escorrega**.
Está no aviso ao Raphael.

**O que sobrava sem depender dela era o egresso de fabricante.** A 20.2 manda retestar bloqueio
herdado antes de respeitá-lo, e a lição da Quartzolit de 29/09 estendeu isso a bloqueio herdado de
**documento**. Foi o que esta execução fez — e a resposta não era nenhuma das duas que estavam
postas.

## O ACHADO: O APEX RESPONDE, O `www.` NÃO, E NENHUMA FONTE MORA NO APEX

Medido às **10h22Z**, e o que separa este relato de um palpite é o cabeçalho. Os apex
`quartzolit.weber`, `tekbond.com.br`, `cascola.com.br` e `loctite.com.br` devolvem
`HTTP/1.1 200 Connection Established` — **o CONNECT passa** — e em seguida o servidor **de
verdade** responde **301**, com `server: Apache` e `server: CloudFront`, data, `content-length` e
`location`. Os quatro domínios **entraram na lista de rede** entre 29/09 e hoje.

**E o ganho é zero.** Os quatro redirecionam tudo para o host `www.` (a Loctite para
`next.henkel-adhesives.com`), e esse host responde `connect_rejected` — política de egresso — nas
três passadas. As **36 URLs de boletim técnico** que os bancos desta ilha citam nesses domínios
estão **todas** em `www.`, incluindo os sete PDFs da Quartzolit e os dois da Tekbond.
`pastilhart.com.br` não entrou nem no apex.

**A frase que o repositório afirmava em quatro lugares — "403 ao CONNECT" — é FALSA hoje**, e a
frase oposta seria igualmente falsa. Os dois vereditos têm de sair juntos:

- Um portão que medisse só o CONNECT diria **"liberado"** e mandaria a próxima execução coletar o
  que não há como ler.
- Um que medisse só o código final diria **"bloqueado"** e esconderia que falta **uma linha**, não
  uma decisão.

**A 20.1 sempre mandou os dois**, `<domínio>` **e** `*.<domínio>`. O pedido de 29/09 foi atendido
só na primeira metade, e nenhuma das quatro execuções anteriores tinha o veredito
`liberado_mas_sem_entrega` para escrever.

## A FERRAMENTA, E AS QUATRO TRAVAS QUE SÃO CICATRIZ DESTA ILHA

`ferramentas/medir-egresso.py`, com saída em `dados/egresso-de-fontes.md` e `.json` (gerados, não
editáveis à mão). **`--autoteste`: 29 casos fabricados, 29 ok** — passada limpa em portão que nunca
acusou nada não prova nada, e o **caso 6** é exatamente o mundo de hoje.

1. **A lista não é digitada.** Os hosts saem de `dados/*.json`. Lista escrita à mão envelhece
   calada — foi assim que `urls_publicadas` ficou quatro dias defasado.
2. **Três passadas, nunca uma** (20.2). Host que responde em duas de três sai como
   **intermitente**, que é veredito e não erro: foi um `000` lido como bloqueio que prendeu esta
   ilha dois dias em 11/09.
3. **Controle obrigatório.** Se `clubedomosaico.com.br` não responder nas três, a medição é
   **VOID** e nada é gravado. Sem isso, queda de túnel escreveria "tudo bloqueado" com cara de
   fato.
4. **A entrega é calculada, nunca escrita.** Apex que só redireciona para host recusado sai como
   `liberado_mas_sem_entrega`, com o host que falta nomeado.

## TRÊS DEFEITOS DA PRÓPRIA FERRAMENTA, OS TRÊS ACHADOS POR ELA RODANDO E OS TRÊS ANTES DO COMMIT

**(1) A primeira versão não viu o achado do dia.** Ela media só os hosts que os bancos citam — e os
bancos citam `www.quartzolit.weber`, nunca o apex. Resultado: imprimiu `bloqueado` para os quatro
fabricantes e **o único fato novo do dia ficou invisível**. Portão que mede só o que o banco cita vê
só o lado que o banco já conhece. Corrigido medindo o **irmão** de cada host — o apex e o `www.` do
mesmo domínio registrável —, o que exigiu `dominio_registravel()` com sufixos de dois rótulos
(`com.br`, `leg.br`, `gob.es`), porque `www2.camara.leg.br` pelo "penúltimo rótulo" daria `leg.br`
e o pedido sairia errado. **Doze casos de autoteste só para isso.**

**(2) Ela lia a própria saída e se citava como fonte.** `egresso-de-fontes.json` nasce em
`dados/` e na passada seguinte apareceu em "citado em: egresso-de-fontes.json". É circular: o
portão passaria a se sustentar no que ele mesmo escreveu ontem, que é a seção 4 do contrato com
outra roupa.

**(3) `loctite.com.br` — o quarto domínio meio-aberto — ficou fora da medição de 36 hosts**, porque
`loctite` aparece nos bancos como **marca** e nunca como URL: nenhum SKU dele foi coletado. A 20.3
manda que quem escreve a regra que exige a fonte confira se a fonte está liberada, então a fonte
exigida em prosa teve de virar **dado**: `dados/fontes-pedidas.json`, onde cada linha aponta **quem
a exige** e a ferramenta **recusa** linha sem `exigido_por` — senão viraria lista de desejo. E o
gatilho teve de aprender a ler esse arquivo: na passada seguinte `loctite.com.br` saiu listado em
"bloqueado e **não pedido**", que é o absurdo de um portão não ler o arquivo escrito para ele ler.

**Um segundo extrator nasceu no caminho**, e a fonte que mais trava esta ilha só existe por causa
dele: os **dez** fabricantes de painel de MDF que `regras_da_categoria_base` nomeia estão em
**prosa**, num campo chamado `dominios_em_000`, e nenhum é URL. Campo cujo **nome** fala de domínio
passou a ser lido como lista de domínio — com trava, porque na primeira tentativa ele pediu rede
para **`validar-banco.py`** (dois rótulos, TLD de duas letras: tem a forma de um host e não é um).

## O PEDIDO, AGORA DERIVADO E COM DONO POR LINHA

**21 domínios, 42 linhas**, cada um com o arquivo que o exige, em `dados/egresso-de-fontes.md`. E o
que **não** se pede está escrito junto, com o motivo: marketplace (o link nasce pela Open API da
25.6, não por leitura de página) e as **16 referências de conteúdo já lidas e já citadas** —
Wikipédia, `camara.leg.br`, teses, museus. Elas também não chegam, e não se pedem: nenhum trabalho
pendente depende delas, e **pedido longo é pedido que não se atende**.

## A `base` NÃO É ALCANÇADA POR ESSA CORREÇÃO, E O NÚMERO DIZ POR QUÊ

Os dez fabricantes de painel — `dexco`, `duratex`, `guararapes`, `arauco`, `berneck`, `eternit`,
`brasilit`, `termotecnica`, `isoeste`, `leroymerlin` — estão em **000 no apex E no `www.`**, três
passadas, com o controle em 200. **Nenhum entrou na lista.** O primeiro SKU de `base` continua
esperando frase de fabricante que esta nuvem possa citar literalmente, e a correção de hoje não o
alcança. Para a `apoio` é o contrário: a FISPQ do epóxi mora justamente em `www.`, então **o curinga
a destrava**.

## DUAS BATERIAS VERMELHAS NO `main`, HAVIA UM DIA, E NINGUÉM AS ESTAVA VENDO

Achado de passagem, e **medido vermelho no `main` limpo antes de qualquer mudança desta execução**:
`mutacoes-base.py` e `mutacoes-apoio.py` fechavam com *"o mundo FABRICADO já está reprovado antes de
qualquer mutação. Portão que reprova o mundo certo não mede nada."*

**A causa é a melhora de ontem.** As duas nasceram em 28/09 com `"degrau": None` no mundo
fabricado, e isso era válido naquele dia. A leva de 29/09 às 16h17Z tornou o degrau **obrigatório**
para todo item que serve link de compra — e a partir dali as duas baterias passaram a se recusar a
rodar. **Não é vermelho inofensivo:** bateria que não roda deixa os portões novos das duas
categorias, 20 e 24 mutações, **sem ninguém medindo** — e foi por isso que o vermelho passou um dia
inteiro sem ser visto. É a mesma família do `conferir-atelie-no-ar.py`, que ficou três dias
vermelho por medir a aspa em vez da diretiva.

**O conserto não foi cravar `4`: foi calcular.** O mundo fabricado não tem `url_produto` e tem
`url_busca`, e a 25.1 diz que item que serve só busca é degrau 4 — então o degrau sai dos campos,
por duas constantes que são as mesmas que o mundo usa. Cravar o número deixaria a bateria à espera
do próximo aperto de regra para apagar-se outra vez. **De volta ao verde: `mutacoes-base` 20 de 20
reprovadas, `mutacoes-apoio` 24 de 24** — os números que o registro de 28/09 declarava.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Não coletou nenhum SKU.** A porta continua sem entregar; coletar hoje seria escrever paráfrase
  de resumo em `literal_do_fabricante`, que é a viga do esquema.
- **Não tocou em `<title>` nem em `description`** de nenhuma das 17 URLs. O BLOCO A espera o número
  de 30/09 por ordem escrita do Raphael, e a janela segue limpa.
- **Não afrouxou nenhuma régua** para o mundo fabricado passar. O degrau passou a ser derivado, não
  tolerado.

## DESEMBARQUE E VERIFICAÇÃO NO AR

Push aceito na primeira tentativa. Sync acionado **depois** do push, porque ele lê o
`manifest.json` do `main` pelo `raw.githubusercontent` — o disparo anterior ao push leu a revisão
**50** e foi descartado, que é a forma de "commit sem Sync não é entrega" da seção 20 com a ordem
invertida. Sync na **revisão 51**, 14 aplicados, e `/status` devolvendo **51**, igual à do manifest.

**BANCADA DESTA EXECUÇÃO.** Casca 591, Loja 208, F1 200, F2 119, Técnicas 123, Ateliê 289, Leads
211, Prestação 5 — **zero falha**. `validar-banco.py` verde (38 materiais, 0 sem saída de compra, 0
piso não rastreável, escada **1:1 · 2:5 · 3:15 · 4:17**, soma 38). `cobertura.py` recontada **sem
mudança** — seguem duas categorias em zero (`base`, `apoio`). Baterias: `mutacoes-degrau` 8 de 8,
`mutacoes-batismo` 14 de 14, `mutacoes-casamento` 5 de 5 no banco, `mutacoes-acabamento` 14 de 14,
`mutacoes-base` **20 de 20** e `mutacoes-apoio` **24 de 24** (as duas de volta ao verde nesta
execução). `medir-egresso.py --autoteste` **29 de 29**. **E no ar: `conferir-no-ar.py` com 519
afirmações e 0 falha**, medido antes e depois do desembarque.

**E A BATERIA MAIS LENTA DA ILHA FECHOU VERDE, depois do push:** `mutacoes-cobertura.py` roda
**dois portões inteiros por mutação** (`validar-banco.py` e `teste-f2.php`, este varrendo 105
estados), levou perto de uma hora e fechou em **14 mutações, 14 reprovadas, 0 passaram** — com o
mundo intacto saindo **APROVADO** antes de começar, que é exatamente a afirmação que estava falhando
em `mutacoes-base` e `mutacoes-apoio`. **Nove das 14 nenhum portão antigo pegou**, entre elas *"o
GERADOR conta errado e regenera coerente com o próprio defeito"* e *"o resumo do censo é digitado em
vez de contado"*. Ela não foi tocada por este bloco, e a árvore ficou limpa depois dela: os 14
bancos seguem parseando.

*(Esta frase substitui, no mesmo lugar, a que esta execução escreveu antes do push dizendo que a
bateria **não** terminara — e a substituição é o ponto, não um detalhe: naquele momento a frase
honesta era "não afirmo verde nem vermelho no que não vi fechar", e é ela que este parágrafo pôde
trocar por um número. Bancada que ainda roda se declara em aberto; nunca se arredonda para verde.)*

**E a reprodutibilidade do artefato foi conferida, não presumida:** re-derivados os hosts depois de
todas as edições do esquema, são **76**, os mesmos 76 que `dados/egresso-de-fontes.json` gravou,
sem nenhum a mais nem a menos. Arquivo gerado que não fecha com a própria derivação é o começo de
um número que ninguém sabe de onde veio.

- **Próximo passo desbloqueado: continua sendo a leitura de 30/09, e agora ela tem DOIS donos
  possíveis escritos** — o acesso da conta `sentinela@` a `sc-domain:clubedomosaico.com.br`, ou a
  credencial `GOOGLE_SA_B64` no ambiente das rotinas. Qualquer uma das duas serve; **nenhuma existe
  hoje**, e sem ela o BLOCO A e a faixa de `description` das quatro páginas ficam onde estão. O
  segundo item do Raphael é o **curinga** dos quatro domínios de adesivo mais o par de
  `pastilhart.com.br`, e esse destrava a `apoio` — a lista inteira, derivada, está em
  `dados/egresso-de-fontes.md`. **O que NÃO depende de ninguém:** nada na fila desta ilha. As três
  técnicas em zero esperam fonte, `base` espera dez domínios que não entraram, os 13 itens de
  pastilha no degrau 4 são decisão do Raphael (`tipo_de_casamento: "equivalente"`) e os dois da
  Quartzolit não têm anúncio único na Shopee. **É por isso que esta execução mediu em vez de
  construir, e não por falta de fôlego.**

# 30/09/2026, 13h17Z — O SEGUNDO DEGRAU DA 7b NUNCA TINHA SIDO CONTADO, E "NADA NA FILA" ERA UMA FRASE QUE NINGUÉM MEDIU

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h17Z** com `executando_desde` e push
aceito na primeira tentativa. **NENHUMA URL NOVA** — a ilha segue em 17 —, **nenhum título e
nenhuma `description` mudaram**: o BLOCO A do despacho do Raphael de 24/09 continua intocado e a
janela de medição de 30/09 segue limpa. Manifest e `/status` na revisão **52**.

## A PORTA DE ENTRADA, ANTES DE QUALQUER BLOCO (seção 29.2)

`conferir-no-ar.py`: **519 afirmações, 0 falha** na origem. `leitura-do-visitante.py`:
**REPROVADO com 1 defeito, e é o esperado** — o soft 404 do hospedeiro (404 na 1ª leitura, 200 na
2ª), aberto em 29/09, com dono escrito e fora do alcance de qualquer snippet daqui. **Nenhum defeito
novo.** Rede pela 20.2: três passadas em `clubedomosaico.com.br`, 200 nas três, com
`aquametria.com.br` em 200 nas mesmas.

## O QUE ESTE BLOCO É, E POR QUE ELE CONTRADIZ AS DUAS EXECUÇÕES ANTERIORES

O registro das 10h16Z de hoje fechou dizendo, com todas as letras: *"O que NÃO depende de ninguém:
**nada na fila desta ilha**."* O de 29/09 dissera o equivalente. **Esta execução derrubou a frase**,
e o caminho foi o que a própria ilha já tinha escrito duas vezes como lição: a **20.2** manda
retestar bloqueio herdado antes de respeitá-lo, e a 7b-ter de 25/09 estendeu isso a bloqueio herdado
de **documento** — *"quatro execuções anotaram 'esbarra no egresso' sem abrir a fonte que estava em
casa"*.

**Primeiro, o que era bloqueio de verdade e continua sendo, conferido e não herdado:** a leitura de
30/09 não sai desta nuvem. `GOOGLE_SA_B64`, `GOOGLE_SA_JSON`, `GOOGLE_SA_FILE` e
`GOOGLE_APPLICATION_CREDENTIALS` estão **as quatro ausentes** (a execução anterior mediu três; a
quarta também não existe), e o acesso do `sentinela@` a `sc-domain:clubedomosaico.com.br` segue
pendente com o Raphael. Então o **BLOCO A** e a metade que falta do item 4 do despacho de 28/09
seguem travados, e **o veredito de 08/10 escorrega**. Nada disso mudou.

**Segundo, o que não era bloqueio:** a ordem da seção 7b do `ARVORE.md` — *"Banco. (...) Só então as
filhas de nível 3, por cluster. Só então a mãe de nível 2, que é o 4c."* — está escrita desde
12/09/2026, e o **segundo degrau nunca foi MEDIDO**. O que existia era *"nenhuma filha de alicate
existe"*, que diz o que falta e **não diz o que já dá**. Entre "o 4c está fechado" e "quais páginas
podem nascer amanhã" há uma **contagem**, e ela nunca tinha sido feita. Fazê-la não dependia de
ninguém: nem de rede, nem de credencial, nem de decisão do Raphael.

## A FERRAMENTA, E O QUE ELA MEDE QUE NENHUMA OUTRA MEDIA

`ferramentas/filhas-do-guia.py` aplica o portão **inteiro** da seção 9 — *"pelo menos 3 itens de
banco reais **e** um número calculado próprio por página"* — a cada recorte que o vocabulário do
esquema admite no Guia. **A segunda metade nunca tinha sido contada nesta ilha.** O `cobertura.py`
conta itens elegíveis por **faixa das ferramentas**, que é outra pergunta; contar se existe um número
que a página consegue calcular **sobre 3 itens do mesmo recorte** é o que decide se a página compara
três produtos ou mostra um número e duas lacunas.

**Nada é digitado.** Os 42 recortes saem de `vocabularios.tipo_por_categoria` (categoria inteira mais
cada tipo), o teto de nível de fonte sai de
`escada_de_fontes.nivel_minimo_para_recomendacao_primaria`, e os itens saem dos
`dados/materiais-*.json`. Recorte digitado mediria os recortes que alguém lembrou, e ficaria verde no
dia em que o vocabulário crescesse — que é justamente o que acontece aqui, onde a regra de
crescimento faz valor novo nascer junto com o primeiro registro que o usa.

**TRÊS VEREDITOS, NUNCA UM BOOLEANO,** e a razão é a lição que o `medir-egresso.py` desta mesma ilha
pagou às 10h22Z de hoje: *"os dois vereditos saem juntos ou nenhum dos dois serve."* Um portão que
olhasse só a **contagem** diria que `alicate/torques` passa (três registros) e mandaria escrever uma
página que compara um produto com dois silêncios; um que olhasse só a **declaração** esconderia que
falta uma frase de fabricante, não um produto. Então: `passa`, `passa_na_contagem_sem_lastro`,
`nao_passa`.

**E a régua reproduziu, sem ser mandada, o exemplo que o próprio esquema nomeia:** o
`loctite-durepoxi` sai da contagem de lastro porque sua única declaração tem fonte de **nível 4**
(press release) — que é textualmente o caso que a `regra 5` do esquema escreveu para explicar a
própria regra. Régua que reencontra sozinha o exemplo da regra é régua que está lendo a regra, e não
a lembrança dela.

## O NÚMERO: 7 PASSAM, 3 PASSAM SÓ NA CONTAGEM, 32 NÃO PASSAM — E NENHUMA CATEGORIA ALCANÇA A 16.5

Passam: `acabamento`, `acabamento/verniz`, `alicate`, `alicate/cortador_de_azulejo`, `pastilha`,
`pastilha/vidro`, `rejunte`. Os de nível de **tipo** — que são os que podem ser filha — são **três**,
e são **um por categoria**: `acabamento/verniz`, `alicate/cortador_de_azulejo`, `pastilha/vidro`.

**Por isso nenhuma categoria do Guia alcança as 3 filhas da 16.5**, nem somando todos os tipos que o
vocabulário lhe dá. A mãe de nível 2 continua fechada — e agora por um **número**, não por uma frase.
O achado por trás do número: **o banco desta ilha é largo entre categorias e fino dentro de cada
uma**, então o 16.5 não se abre coletando em qualquer lugar; ele se abre coletando **dentro de uma**.

## A LISTA DE COMPRAS, QUE É O QUE SEPARA "NÃO PASSA" DE "NÃO SE SABE O QUE FALTA"

A lição é do `cobertura.py` desta ilha: *"O que falta nessa varredura é a lista de compras do banco —
e o número final aparece sozinho."* Por categoria, itens a coletar para ter as três filhas:
**`acabamento` 3** (1 impermeabilizante + 2 seladores) · `rejunte` 5 · `alicate` 5 · `cola` 6 ·
`pastilha` 6 · `base` 9 · `apoio` 9.

**A distância conta o MAIOR buraco, nunca a soma** — um item novo com número declarado fecha os três
de uma vez, e somar faria a lista pedir o triplo.

**E ela separa SKU novo de campo vazio,** que não custam a mesma coisa: `rejunte/cimenticio` está a
**um campo** de um registro que **já mora no banco** — `liberacao_area_molhada_h` no
`quartzolit-rejunte-piscinas` —, não a um produto novo.

## A CLASSIFICAÇÃO DE SERP DA 14.9 INVERTEU A ORDEM QUE A FILA SUPUNHA

A 14.9 manda olhar a SERP **antes** de criar a página. Feita nesta passada, consulta a consulta, em
`dados/filhas-do-guia.md`, abaixo de uma fronteira que o gerador **preserva** (busca não é derivação,
e regenerar o arquivo não pode apagar o que custou busca).

**As duas ABERTAS são PERGUNTA; as duas TOMADAS são PRODUTO.**

- `como cortar pastilha de vidro para mosaico qual ferramenta` → **8 de 10** são blog e resposta
  genérica sem número: Vila do Artesão, Obramax, FazFácil (2), Além da Rua Atelier (**2012**),
  Artesanato Benjoino (**2010**), O Portal das Maravilhas (2). **ABERTA**, e é o galho da 14.9 escrito
  ao pé da letra.
- `verniz para peça de mosaico artesanal qual usar` → Portal de Artesanato, três blogspots de
  **2010**, Revista Oeste, em.com.br, Viva Decora, Como Fazer Artesanatos. **ABERTA**.
- `pastilhas de vidro para mosaico` → **9 de 9** marketplace e loja: Mercado Livre, Buscapé, Elo7 (2),
  Bazar Horizonte, Vetro Designer, Mosaico & Cia, Mosaico em Casa, Pastilhart. **TOMADA.**
- `quantas pastilhas vem na caixa placa telada mosaico vidro medida` → **10 de 10** loja e obra,
  Leroy Merlin PT e Telhanorte inclusive. **TOMADA, e é a ARMADILHA do revestimento** que o corpus de
  10/09 já tinha nomeado — agora com evidência nova.

**A leitura, e ela não é sobre categoria:** quem vende produto **já ocupa** a consulta de produto, e
**ninguém ocupa** a consulta de método. Consequência dura para a fila: a filha de mais banco da ilha
— `pastilha/vidro`, 13 itens, três números em 12 deles — **passa no dado e a SERP recusa.** E a
ferramenta já dizia, na própria nota de alcance, que mede recorte de **tipo** e é um **piso**; a SERP
acabou de dizer que o piso mede a forma errada, e que as filhas publicáveis são **perguntas**, cuja
régua de contagem é a mesma.

## O QUE CADA ABERTA TEM DE NÚMERO QUE A SERP NÃO PUBLICA

- **Cortar pastilha de vidro:** nenhum dos oito resultados editoriais dá **espessura máxima de corte
  em mm**. O banco dá, em 4 dos 6 itens de `alicate`, com fonte de nível 2 ou 3. E a página nasce com
  a faixa descoberta que a 7b-bis mediu em 25/09: o torquês de mosaico para em **5 mm** e **3 das 13**
  pastilhas do banco não cabem (6, 8 e 8 mm) — três dos treze produtos cuja quantidade a F1 já calcula
  não têm ferramenta declarada que os corte.
- **Verniz:** nenhum dos nove dá demãos, consumo em ml/m² nem secagem. O banco dá. **E dá a ausência,
  que vale mais:** a 7b-ter mediu que **nenhuma** das sete frases de fabricante de `acabamento` nomeia
  **vidro** e **nenhuma** nomeia **rejunte** — as duas superfícies que a peça pronta expõe.

## DOIS DEFEITOS DO MEU PRÓPRIO INSTRUMENTO, E OS DOIS ESTÃO NO ARQUIVO EM VEZ DE ESCONDIDOS

1. **O canal de busca desta nuvem é dos EUA**, declarado pela própria ferramenta. Uma consulta
   (`cortador de azulejo manual para mosaico`) voltou com SERP **espanhola** — Amazon MX, Leroy ES,
   Bricodepot ES, Home Depot MX. Está marcada **NÃO MEDIDA**, não "consulta sem concorrente
   brasileiro". E daí sai o limite do arquivo inteiro: ele classifica **quem ocupa**, que é o que a
   14.9 pede com essas palavras, e **não afirma posição de ninguém** — posição, nesta ilha, vem do
   Search Console, cujo acesso está pendente.
2. **Eu pus `Vonder` e `Cortag` dentro da consulta**, e ela voltou cheia de página de fabricante. Era
   previsível e o defeito é meu: é a trava de coleta da seção 8 — *"nunca pôr na consulta o valor que
   se quer confirmar"* — aplicada à SERP em vez de ao dado. Também **NÃO MEDIDA**, com o motivo, e
   refeita sem marca. Foi a passada sem marca que achou a consulta aberta.

## E CONTRADIZ O CORPUS DE 10/09 COM TODAS AS LETRAS, EM VEZ DE EM SILÊNCIO

O corpus classificou `pastilhas de vidro para mosaico` como **ABERTA**, com a **mesma** evidência que
esta passada leu como **tomada** (anúncio da Shopee, Bazar Horizonte, Art Glass). A diferença não é de
dado, é de **régua**: o corpus chamou de aberta porque *ninguém responde a pergunta técnica*, e a 14.9
manda classificar **quem ocupa** — e quem ocupa é marketplace, que é o primeiro galho dela, o do "a
página NÃO nasce agora". As duas leituras cabem na mesma SERP, e **a 14.9 é a que decide se a página
nasce**. Está escrito no arquivo, com a instrução de quem for mexer no corpus ler aquele parágrafo
primeiro: o que está velho lá é o **rótulo** daquela linha, não a evidência.

## A TABELA DO `ARVORE.md` DIZIA ZERO EM DUAS CATEGORIAS QUE SAÍRAM DE ZERO HÁ CINCO DIAS

A seção 2 do `ARVORE.md` trazia `0` em `Alicates e corte` e em `Acabamento`. As duas saíram de zero em
**25/09** — 6 e 7 itens —, e **as próprias seções 7b-bis e 7b-ter do mesmo arquivo registram isso três
telas abaixo**. É a seção 4 do contrato dentro de um documento que já tinha a correção escrita: em
prosa, e não na tabela que se lê primeiro.

Corrigida, com coluna nova (`tipos que passam o portão da 9`) para a tabela parar de responder a
pergunta errada — **banco não é filha**, e era o número do banco que ela mostrava ao lado de uma coluna
chamada "existe".

**E aqui eu cometi, e consertei, o defeito que esta ilha mais nomeia:** escrevi que as colunas eram
*"derivadas de `dados/filhas-do-guia.json`"* **tendo digitado os números à mão** — número de tela que
parece conferido. Agora `--conferir` confere a tabela contra a derivação, **nas duas direções**: cada
linha tem de bater no número de banco e na forma `N de M`, e **toda categoria do vocabulário com nível
2 tem de ter linha**. Slug fora da ponte é ignorado de propósito, porque a tabela tem linhas que não
são categoria de banco (`/materiais/como-sabemos/`) e reprovar por elas faria o portão brigar com o
documento certo.

## TRÊS DEFEITOS DA PRÓPRIA FERRAMENTA, OS TRÊS ACHADOS POR ELA RODANDO E OS TRÊS ANTES DO COMMIT

1. **Um `motivo` contava a lista errada:** dizia *"os 7 itens sustentam recomendação"* para a `cola`,
   onde **3** sustentam — ele imprimia o total do banco no lugar da contagem de lastro. Frase de
   diagnóstico com o número errado é pior que frase ausente: ela é o que a próxima execução cita.
2. **"Pode fechar completando registro existente" prometia uma coleta e eram seis.** Para a `cola`,
   dizia que faltava `tempo_de_ajuste` em **6 registros que já moram no banco** — verdade literal que
   se lê como um campo a preencher, quando a propriedade era declarada por **um** item só. Número que
   existe num registro só não está *perto* de ser número da página: ele ainda tem de ser
   **construído**, e construir não é completar. A promessa passou a valer só a **um** registro de
   distância, e sobrou exatamente um caso no banco real — o do Rejunte Piscinas.
3. **O gerador não era idempotente.** O trecho preservado chegava com a quebra de linha que o separava
   da fronteira, e `A("")` punha outra: o arquivo ganhava **uma linha vazia por passada** e
   `--conferir` reprovava o arquivo que a passada anterior havia escrito. Achado porque eu rodei
   `--conferir` depois de gerar, e não porque eu o li. **Gerador que não é idempotente é gerador que
   não fecha com a própria derivação** — e o caso 18 do autoteste agora gera três vezes e compara.

## UM CAMPO OBRIGATÓRIO FALTAVA NO CABEÇALHO DESTA ILHA, E A SEÇÃO 1 LÊ ESSE CAMPO

Ao fechar o cabeçalho, `bloqueada_por` **não existia** nele — e a seção 2 do contrato o exige desde que
ela existe. Conferido que já faltava antes desta execução (`git show HEAD`), e medido nos **seis**
`ESTADO.md` do repositório, o `_modelo` incluído: **os seis parseiam** em `yaml.safe_load` e **dois
estavam incompletos** — esta ilha sem `bloqueada_por`, a `ohmetria` sem `bloqueada_por` **e** sem
`ultima_ronda`. O molde está certo desde 21/09; as ilhas nascidas antes dele não foram acertadas.

**Por que isso é a seção 1 lendo a si mesma errada:** o passo 3 manda descartar ilha *"com
`bloqueada_por` preenchido"*. Com o campo **ausente**, `grep` e olho concluem "não está preenchido" e
acertam por acidente; um parser com `d["bloqueada_por"]` **morre**; e `d.get()` trata ausência como
`null` sem nunca dizer que o campo não existe. As três leituras concordam **hoje** porque o valor certo
é mesmo `null`, e discordam no primeiro dia em que uma ilha for bloqueada de verdade. **Campo ausente
que se comporta como o valor certo é a forma mais paciente de defeito: ele espera o dia em que o valor
certo muda.**

Consertado **nesta ilha** e escrito no contrato: a régua da seção 2, que desde 13/09 conferia se o
cabeçalho **parseia**, passa a conferir **presença** na mesma linha. **Não toquei na `ohmetria`** —
reserva é por ilha, e consertar cabeçalho de ilha que não se reservou é a colisão que a seção 1 existe
para impedir. O defeito dela está nomeado no contrato para a próxima execução que a reservar não
precisar redescobri-lo.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Não criou nenhuma URL, e não podia:** a 16.5 exige 3 filhas por categoria e nenhuma categoria tem
  3. Duas filhas abertas não são três.
- **Não coletou nenhum SKU.** A coleta das 3 de `acabamento` é o bloco seguinte, e a seção 13 proíbe
  empilhar dois blocos numa passada sem a verificação inteira de cada um.
- **Não tocou em `<title>` nem em `description`** de nenhuma das 17 URLs. O BLOCO A espera o número de
  30/09 por ordem escrita do Raphael, e a janela segue limpa.
- **Não escreveu volume de busca que não mediu:** `verniz` **não existe** em `dados/corpus-buscas.md`,
  então a filha de SERP mais aberta da ilha é a que **não tem faixa de volume**. A 14.9 exige o
  cruzamento de intenção com chance; a intenção é clara (é produto que a artesã compra) e o volume está
  escrito como **desconhecido**, nunca estimado.
- **Não afrouxou nenhuma régua** para o banco de hoje passar. Onde a régua mordeu, o conserto foi na
  régua ou na frase — nunca no limiar.

## BANCADA DESTA EXECUÇÃO

`filhas-do-guia.py --autoteste`: **27 casos fabricados, 0 falha** — 19 sobre a medição (entre eles o
teto lido do esquema nas duas direções, fonte órfã, valor nulo, registro inativo, e a distância que
conta o maior buraco e não a soma), **5 jeitos diferentes de reprovar uma tabela de `ARVORE.md`
fabricada** mais os 2 que ela tem de aprovar, e a idempotência em três passadas. `--conferir`:
**aprovado**, e roda duas vezes seguidas sem reprovar o próprio arquivo.

`validar-banco.py` verde (38 materiais, escada **1:1 · 2:5 · 3:15 · 4:17**, soma 38).
`cobertura.py --conferir` OK. `mutacoes-arvore.py` **29 de 29 reprovadas**. Casca **591**, Loja
**208**, F1 **200**, F2 **119**, Técnicas **123**, Ateliê, Leads e Prestação aprovados — **zero
falha**. `conferir-no-ar.py` **519 afirmações, 0 falha**, antes e depois do desembarque.

## DESEMBARQUE E VERIFICAÇÃO NO AR

Push aceito na **primeira tentativa** (`307dcd1..b2e39c0`). Sync acionado **depois** do push, porque
ele lê o `manifest.json` do `main` pelo `raw.githubusercontent` e disparo anterior ao push leria a
revisão 51 — é a forma de "commit sem Sync não é entrega" da seção 20 com a ordem invertida. **Sync na
revisão 52** às 13h43:41, 14 aplicados e 11 aguardando desembarque, e `/status` devolvendo **52**,
igual à do manifest. Os dois arquivos novos de `dados/` nascem com `publicar: false` e por isso estão
entre os que aguardam — eles são medição, não conteúdo de página.

**E no ar depois do desembarque: `conferir-no-ar.py` com 519 afirmações e 0 falha**, medido antes e
depois. O único vermelho da borda continua sendo o soft 404 do hospedeiro, com dono escrito.

**A memória da ilha não foi atualizada porque ela não existe neste ambiente:** `/areas/` não está
montado, conferido nesta execução. O `PROMPT.md` desta ilha já prevê isto com estas palavras — *"Sem
memória, não pare: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta"* — e é onde
o próximo passo ficou escrito.

- **Próximo passo desbloqueado, e desta vez ele é da FUNDAÇÃO e não de ninguém de fora:** coletar **1
  impermeabilizante e 2 seladores** fecha as **3 filhas de `acabamento`**, que é a categoria mais
  barata do Guia, e é o que abre a primeira mãe de nível 2 desta ilha — o **4c**, parado desde 12/09.
  **Confirmado alcançável nesta passada**, e não presumido: selador com rendimento em m²/demão, número
  de demãos e tempo de secagem declarados existe em página de fabricante. **E o resultado reproduziu o
  achado da 7b-ter antes de eu coletar nada:** o selador do Coral nomeia reboco, bloco, concreto, gesso
  e fibrocimento e **não nomeia MDF** — a base mais comum da peça do ateliê. Quem coletar decide antes
  se selador de alvenaria cabe em `regras_da_categoria_acabamento`, que é decisão de esquema e não de
  coleta. **O que continua fora do alcance daqui:** a leitura de 30/09 (acesso do `sentinela@` ou
  `GOOGLE_SA_B64`), que trava o BLOCO A e a faixa de `description` das quatro páginas, e o **curinga**
  de egresso, que trava `base` e `apoio`. Os dois estão na lista do Raphael e nenhum dos dois é
  pré-requisito do passo acima.
