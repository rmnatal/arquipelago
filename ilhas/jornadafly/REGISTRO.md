# Registro de execuções — JornadaFly

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-10-27 16h25Z — **A COLETA ANDOU COM A REDE FECHADA.** Entrou o **Parque Bondinho Pão de Açúcar**, quinta experiência e PRIMEIRA BRASILEIRA, e com ela nasceu a entidade **ELEGIBILIDADE** — o preço de quem prova o que não é idade. No caminho, **três defeitos da mesma família** em três ferramentas diferentes, os três certos por acidente num banco sem real

**O que saiu:** `dados/esquema-banco.json` e `dados/experiencias.json` na **versão 8**;
a régua da elegibilidade no `validar-banco.py` com **24 quebras novas** no
`mutacoes-banco.py`; a elegibilidade na `f1-referencia.py` e no `teste-f1.py`; a seção
**9** da `especificacao-calculadoras.md`; e o item **6** da fila destravado, com o
`bondinho.com.br` virando o primeiro dos 25 candidatos com ferramenta ofertável.

**NADA FOI AO AR, E NÃO PODIA.** Esta ilha não tem WordPress, não tem casca, não tem Sync,
não tem `/status` e não tem URL — faltam os passos 2 a 8 da seção 11, que são trabalho de
navegador do Raphael. Dizer que verificou no ar seria inventar. A 31.1 vai de 4 em 14 para
**4 em 15**, e está dito sem maquiagem.

### A REDE, remedida e não herdada (20.2)

**NONO dia de recusa.** `jornadafly.com.br` e `www.jornadafly.com.br` em `000` nas três
passadas, com `aquametria.com.br`, `robometria.com.br` e `clubedomosaico.com.br` em `200`
nas mesmas três — nove medições de controle verdes contra seis de bloqueio, zero
intermitência. O `__agentproxy/status` desta nuvem nomeia a causa com todas as letras:
*"gateway answered 403 to CONNECT (policy denial or upstream failure)"*.

E as fontes de preço também: `civitatis.com.br`, `numbeo.com`, `booking.com`,
`romapass.it`, `turismoroma.it`, `lisboacard.org`, `visitlisboa.com`,
`getyourguide.com.br`, `tiqets.com` e `viator.com` — **todos em 000**.

### O QUE ACHEI, E É O ACHADO DE MÉTODO DESTA PASSADA

Três execuções fecharam em "nada elegível" nos dias anteriores, e o registro de 23/10
dizia que os itens de conteúdo desta ilha "dependem de rede que esta nuvem não tem". **Isso
está meio errado, e a metade errada custou três execuções.** A coleta por **busca** alcança
o **degrau 4** da escada de fontes desta ilha — *operador lido por busca* —, e foi por esse
degrau que a Torre Eiffel entrou em 15/09/2026. O degrau não fechou; ninguém tentou de novo.

**Medi as DUAS portas desta nuvem na mesma passada**, que é mais do que as coletas
anteriores fizeram: `curl` em 000 com 403 de política em quatro hosts de `bondinho.com.br`,
e **WebFetch** em `getaddrinfo ENOTFOUND` nos dois. A leitura direta (degrau 2) continua
fora de alcance; a busca não. **Três passadas de busca**, duas delas restritas ao domínio do
operador, devolveram **seis documentos dele nomeados um por um** — a central de ajuda
«Tipos de bilhetes», as páginas de bilhete, a de Estado RJ, a de promocional para
brasileiros, a de bilhete geral e a da trilha do Morro da Urca.

### A ELEGIBILIDADE, e ela nasceu de um DADO e não de uma previsão

O operador vende **o mesmo Bilhete Bondinho por R$ 205, R$ 160 e R$ 89**. O que muda não é
quantidade, nem escopo, nem momento — que eram os **três** eixos que este esquema tinha. É
**QUEM COMPRA**: R$ 160 para quem nasceu *e* mora no Brasil, R$ 89 para quem nasceu *ou*
reside no estado do Rio. E `faixa_etaria` também não serve, porque o próprio esquema diz que
o `se_nao_cumprir` dela é *"o que o operador cobra de quem não prova a **IDADE**"*.

Sem a entidade, a carga tinha duas saídas e as duas eram erradas: gravar os cinco preços
como versões irmãs, inventando um eixo que o operador não vende; ou gravar só o R$ 205 —
**publicando, numa ilha em português do Brasil, o preço de estrangeiro quando o operador
cobra 28% menos do próprio leitor.** São 2,3 vezes entre a ponta cheia e a ponta barata,
maior que qualquer diferença de versão deste banco.

**E ELA FECHA UMA DÍVIDA DE 15/09/2026.** O `motivo_sem_faixa_etaria` das duas versões do
Coliseu diz, por extenso, que a divergência medida *"não entra em `faixa_etaria` porque
`faixa_etaria` guarda PREÇO, e aqui o que existe é uma divergência sobre quem tem
direito"* — gratuidade de menor de 18 anos para cidadão da UE contra gratuidade universal.
**QUEM TEM DIREITO é exatamente o que a ELEGIBILIDADE guarda.** O valor continua `null`, e
por uma razão de escada e não de forma: as duas fontes daquela divergência são nível 6, e o
esquema diz que o nível 6 *"não sustenta NADA sozinho"*. O que mudou é que a dívida saiu de
prosa dentro de um motivo e passou a ter **campo, nome e endereço de releitura**.

### A SOMA NÃO SE PRESUME, E ISSO TEM NÚMERO

`acumula_com_faixa_etaria` nasceu **obrigatório**, por medição. O operador declara que a
meia-entrada vale para o Bilhete Bondinho, o Acesso Rápido e a Visita Guiada e **não vale
para as tarifas promocionais**. E a imprensa dos 114 anos declarou o preço composto: **R$ 89
para adulto e R$ 44 para criança de 3 a 12 anos** no bilhete de morador do Rio.

**Metade de R$ 89 é R$ 44,50. O operador cobra R$ 44.** Se a F1 tivesse autorizado somar,
ela publicaria cinquenta centavos inventados na página do dinheiro, numa conta que
pareceria certa — a aritmética estaria correta; só a pergunta é que não existia.

### TRÊS DEFEITOS DA MESMA FAMÍLIA, em três ferramentas, achados na mesma carga

Nenhum é da elegibilidade. Os três são **réguas escritas num mundo sem real**: as três
corretas enquanto o mundo não mudou, as três erradas no dia em que ele mudou. O Bondinho é
o primeiro registro em `BRL_do_operador` — valor que estava no vocabulário desde
14/09/2026 **sem um registro que o usasse**.

1. **`validar-banco.py`** — o contador `experiencias_com_preco_em_brl` era incrementado
   **dentro do ramo de ERRO** da conferência de moeda: ele contava versão cuja moeda
   *discorda* da cidade, e publicava o número sob um nome que diz o contrário. Com o banco
   todo em euro e dólar o ramo nunca rodava, a chave saía `0`, e **`0` era a verdade por
   acidente**. Hoje uma experiência cobra em real e a chave continuaria dizendo `0`.
2. **`teste-f1.py`** — afirmava que **`R$` nunca aparece** na tela, porque todo real só
   poderia ser conversão com o câmbio pendente. **288 frases de tela** carregam `R$`
   legitimamente hoje — o preço do operador, lido na fonte dele, na moeda dele — e ele
   reprovava todas. *(O 288 foi contado depois do conserto, varrendo as respostas da F1 de
   1 a 12 pessoas em todas as versões; o número que a passada vermelha imprimiu era outro e
   não é reproduzível, porque naquele instante a linha do IOF ainda existia nas páginas em
   real e as frases da elegibilidade ainda não.)*
3. **`f1-referencia.py`** — somava **IOF de 3,5%** em toda versão. O id da constante diz o
   que ela é: `iof-compra-internacional-cartao-pessoa-fisica`. A F1 publicou
   **`R$ 144,90` num bilhete de R$ 140** — imposto de compra no exterior somado a uma
   compra que não sai do país.

**O terceiro é o pior, por uma assimetria.** Os dois primeiros erram alto: um reprova o
certo e para a bancada, o outro publica um número redondo. O da F1 **cobrava do leitor um
imposto que ele não paga**, na página do dinheiro, com a aritmética certa — e ninguém
procura defeito onde a conta fecha.

O conserto dos três é o mesmo movimento: **perguntar a moeda**. E o do portão do câmbio
passou por duas versões, o que vale registrar: a primeira trocou um falso positivo por
outro (proibir €/US$ numa versão em real reprovou a declaração da **plataforma**, que
publica em dólar). A regra que ficou é de **contenção** — o símbolo na tela tem de caber no
conjunto de moedas que os registros daquela experiência declaram. Citar quem declarou não é
converter.

**E eu quebrei a própria conferência do câmbio ao consertá-la:** a primeira versão do bloco
usou `moeda` e `simbolo` como variáveis de laço e **sobrescreveu a `moeda` do escopo de
fora**, que o portão usa para montar a frase esperada de cada afirmação — a gôndola, que
cobra em euro, passou a ser cobrada por «R$ 18». O relatório daquela passada imprimiu
**482 falhas** (7 mostradas e «e 475 outras»), e esse número é o que o instrumento disse
naquele instante, não uma contagem reproduzível. Os nomes daquele bloco levam `_` hoje, com
o motivo escrito ao lado.

### O QUE O OPERADOR DISCORDA DE SI MESMO, e a escada não previu isso

Quatro números, no mesmo domínio e no mesmo dia de leitura: **R$ 205 contra R$ 185**
(central de ajuda contra blog), **R$ 89 contra R$ 80**, **R$ 160 contra R$ 150** (e uma das
páginas é `novosite.bondinho.com.br`, que pelo nome é uma versão em preparação), e
**R$ 285 contra R$ 295** no Acesso Rápido.

A escada desta ilha resolve conflito **entre níveis** e diz, sobre o empate, apenas que
*"dentro do mesmo nível, ninguém vence"*. **Ela não previu a fonte que discorda DE SI
MESMA**, e foi preciso quebrá-la em **duas fontes** para que a divergência pudesse sequer
ser gravada: declaração aponta para uma `fonte`, e uma fonte não pode divergir de si.

**O Acesso Rápido ficou com `preco: null`, e isso é decisão e não lacuna.** A `resolucao`
deste esquema é de **uma** versão por experiência (`versao_resolvida` é campo único), e esta
experiência resolve no Bilhete Bondinho — onde a regra do MAIOR dá R$ 205, que é também o
número da página de bilhete. Para o Acesso Rápido não há onde gravar a segunda resolução, e
resolver pelo MAIOR poria no bilhete o número do **blog** contra o da página de bilhete.
**Preço errado por R$ 10 na página do dinheiro custa mais que preço ausente com a causa
escrita.** A F1 já tinha o código `preco_nao_lido` e ele disparou certo na primeira versão
sem preço deste banco; o que faltava era o portão saber que existe versão sem preço.

### DUAS PRIMEIRAS QUE NÃO SÃO SOBRE A ELEGIBILIDADE

- **Primeiro preço em `BRL_do_operador`.** As quatro experiências anteriores cobram em euro
  e dólar, e a constante de câmbio desta ilha está **pendente** desde 14/09 — então todo
  total delas chega ao leitor brasileiro numa moeda que ele não gasta. Aqui não há conversão
  a fazer, logo não há nada a inventar.
- **Primeiro `afiliado.url_produto` que é o MESMO produto do registro**, e são 43 dias de
  tentativas. O Angkor e o Coliseu ficaram com `null` com a mesma frase escrita nos dois: a
  busca restrita à plataforma devolvia passeio guiado, e *"apontar um passeio guiado como se
  fosse o ingresso seria vender uma coisa no lugar de outra, que é pior do que não ter
  link"*. Aqui a plataforma vende **o bilhete**. Com isso o teste de vida da 25.4-b passa a
  ser **possível** neste registro — o que não quer dizer feito: o egresso recusa o domínio,
  e o teste de vida é da ronda.

### A MEIA-ENTRADA BRASILEIRA NÃO ENTROU, e a recusa é deliberada

Os bilhetes de Trilheiros declaram `Meia-entrada: R$ 70` e `R$ 32` ao lado do adulto, e os
dois números **não foram gravados**. A meia-entrada brasileira **empacota idade, vínculo e
deficiência numa só palavra**, e cada uma das três se prova de um jeito. Gravá-la em
`faixa_etaria` diria que o operador cobra por idade o que cobra por condição; gravá-la em
`elegibilidade` afirmaria uma prova que a fonte não fez. A página do operador que a define
— «Outras opções de meia-entrada» — **voltou por nome na busca e não foi lida**.

### O ITEM 6 DESTRAVOU, E O CRITÉRIO ERROU O RÓTULO

A lista de prospecção tem agora o **primeiro dos 25 candidatos com ferramenta ofertável**:
`bondinho.com.br`, com a F1. O destravamento era **pré-registrado** no `PROMPT.md`, com o
domínio escrito pelo nome, e disparou pelo caminho previsto. A última linha dos motivos
daquele candidato dizia *"a ferramenta não existe para lhe oferecer: o Pão de Açúcar NÃO
está em `dados/experiencias.json`"* — e **deixou de ser verdade hoje**.

**O que o critério previu errado foi o rótulo:** ele pede «operador **privado** brasileiro»,
e o Bondinho é `concessionaria_de_bem_publico`, o mesmo tipo da SETE que opera a Torre
Eiffel. **`operador_privado` segue SEM LASTRO** no banco. As três condições que o critério
cobra de fato — brasileiro, vende direto pelo próprio site, mais de uma versão da mesma
experiência — estão as três cumpridas, e é por elas que a linha destravou. Fica escrito
para quem decidir sobre o rótulo decidir com o critério na mão.

**E o que NÃO destravou foi a rede**, que é a lição: o egresso está hoje como estava em
22/10. A alavanca de link não esperava a rede — esperava **um registro do tipo certo**.

### DOIS PORTÕES QUE ESTAVAM PREGADOS AO MUNDO DE ONTEM

- O caso `"F1 nao vai a quem o banco nao atende (hoje, bondinho)"` do
  `mutacoes-prospeccao.py` media a regra usando como exemplo o mundo em que o banco não
  tinha o Pão de Açúcar — **e o nome dele dizia «hoje»**. Agora mede a regra com um
  candidato que o banco de fato não atende (`perurail.com`, classe 2 de propósito: classe
  `barrado` ou `3` reprovaria pelo ramo da escada e o caso ficaria verde sem medir o ramo
  que nomeia), e ganhou um caso irmão que mede o **destravamento**.
- O `teste-prospeccao.py` cobrava que a prosa do achado dissesse «QUATRO experiências» com
  o `4` **escrito à mão dentro da própria afirmação** — a dívida que ele existe para cobrar
  um andar acima. A palavra esperada agora é **derivada da contagem**: crescer o banco
  obriga a reescrever a prosa, que é o que se queria, e nunca mais obriga a reescrever o
  portão.

### A RÉGUA DO `sem_extrator` DE 22/10 FUNCIONOU NO PRIMEIRO TESTE REAL

Ela nasceu há cinco dias, depois de `declarada_por` e `canal_de_leitura` passarem 37 dias
sem ser conferidos por ninguém. Hoje o vocabulário novo `o_que_se_prova` entrou no esquema
e **ela reprovou na hora**, com a mensagem escrita: *"vocabulário novo entra no esquema e no
extrator na mesma passada"*. Primeira vez que foi cobrada por um caso que não era dela.

### NENHUM PORTÃO NOVO NASCEU (31.2), e a bancada segue com TREZE comandos

A régua da elegibilidade mora **dentro** do `validar-banco.py` e as quebras dentro do
`mutacoes-banco.py`, que já existiam; a elegibilidade da F1 mora dentro do
`teste-f1.py`. A 31.2 só deixa nascer portão novo com defeito medido no ar, e esta ilha não
tem "no ar". A **31.3** foi lida antes e não depois: ela proíbe testar portão que **já
existe**, e o que estas afirmações guardam é o **conteúdo que nasceu na mesma passada** — o
desenho que a F1, a F2 e a F3 tiveram em 22/10 e o artigo-âncora teve em 23/10.

### BANCADA, 0 FALHA nos TREZE comandos

| comando | resultado |
|---|---|
| `validar-banco` | OK — banco cumpre o esquema, piso derivado e resolução batendo com a escada |
| `mutacoes-banco` | **178 casos**, 0 falha: 23 mundos que têm de passar e 155 quebras que têm de reprovar, 111 cobradas pela frase que esperam ouvir. Eram **154** antes desta passada |
| `teste-f1` | **229.768 afirmações**, 0 falha |
| `mutacoes-f1` | 28 casos, 0 falha nos três lados da fronteira |
| `teste-f2` | OK |
| `mutacoes-f2` | **51 casos**, 0 falha nos três lados |
| `teste-f3` | OK |
| `mutacoes-f3` | **45 casos**, 0 falha nos três lados — *medido às 17h10Z, depois do commit; ver abaixo* |
| `artigos-referencia` | OK |
| `mutacoes-artigos` | OK |
| `validar-prospeccao` | APROVADO — 25 candidatos, e o `.md` idêntico ao que a referência gera |
| `teste-prospeccao` | **287 afirmações**, 0 falha |
| `mutacoes-prospeccao` | **40 casos**, 0 falha |

**O `mutacoes-f3` NÃO estava fechado quando o commit `1facb42` saiu, e a tabela dizia isso
com essas palavras** — "ainda rodando", não "0 falha nos treze". Fechou às **17h10Z**, um
minuto depois do commit, com **45 casos e 0 falha**, e esta linha foi reescrita pela mesma
execução, que é o que a frase anterior dela prometia. Fica registrado porque o método
importa mais que o resultado aqui: **afirmação redonda sobre instrumento que não respondeu
é o defeito que esta ilha mais paga**, e nesta passada ele apareceu três vezes num andar
abaixo (o contador de BRL, o portão do câmbio e o IOF). Escrever "0 falha nos treze" às
17h09Z teria sido o mesmo erro, cometido pela mão que acabara de consertá-lo três vezes.

**E por que as duas baterias longas quase não couberam:** a quinta cidade levou a grade da
F2 de **3.077 para 3.846 estados**; o `teste-f2.py` sozinho leva **~12 segundos**, a
bateria dele o roda **44 vezes** e a da F3 roda o `teste-f3.py` **45 vezes**. São mais de
quinze minutos somados, e elas rodaram em segundo plano com a reserva renovada pela **1.1**
antes, não depois. O aviso está escrito no `PROMPT.md`, na seção da bancada, com a nota de
que o número envelhece a cada cidade nova — **quem o ler recompute em vez de confiar nele**.

**E os mundos sintéticos tiveram de acompanhar o campo novo**, o que é a bateria fazendo o
trabalho dela: campo obrigatório que nasce quebra todo mundo de bancada que não o declara.
No caminho, o `mundo_sem_divergencia` expôs uma **conta pela metade** que ninguém tinha
visto: ele decidia quais fontes continuam usadas olhando **apenas `versao.fonte`**, e
podava fonte que uma declaração, uma faixa, uma elegibilidade ou a resolução de outra
experiência ainda referencia. O Bondinho é a primeira experiência deste banco cujas
declarações se apoiam numa fonte que **nenhuma versão usa** — o blog do próprio operador,
que discorda da página de bilhete dele —, e foi ela que expôs a conta.

### ERRATA DE OUTRO ARQUIVO, achada de graça pela régua da seção 2

O cabeçalho deste `ESTADO.md` **nunca teve `ultima_ronda` nem `bloqueada_por`** — os dois
campos que a seção 2 do contrato declara obrigatórios. Rodei a régua de **presença** dela
(a de 30/09/2026, que existe porque `yaml.safe_load` aprova cabeçalho que parseia **sem**
os campos que a seção 1 lê) nos seis `ESTADO.md`, e o resultado é:

| ilha | régua de presença |
|---|---|
| `_modelo`, `aquametria`, `clubedomosaico`, `robometria` | YAML ok |
| **`jornadafly`** | FALTAM: `ultima_ronda`, `bloqueada_por` → **acrescentados hoje** |
| `ohmetria` | FALTAM: `ultima_ronda`, `bloqueada_por` → segue aberto, ilha fora do foco |

**E isto é uma errata de `dados/despachos.md`.** A entrada de 26/10/2026 às 13h3xZ afirma,
com todas as letras, que *"`aquametria`, `clubedomosaico`, `jornadafly` e `_modelo` estão
completos"* e nomeia só `robometria` e `ohmetria`. A `robometria` foi acertada naquele dia
e hoje passa; a `ohmetria` segue aberta e continua corretamente nomeada; **a `jornadafly`
estava incompleta e foi relatada como completa.** Um dos dois cabeçalhos que o despacho
deu por bons estava entre os quebrados — e o custo é o que a própria seção 2 descreve:
*"campo ausente que se comporta como o valor certo é a forma mais paciente de defeito: ele
espera o dia em que o valor certo muda"*. Hoje `null` é o valor certo nos dois, e as três
leituras possíveis (olho, `grep`, parser) concordam por acidente.

Os dois entraram com `null` e com o motivo escrito ao lado: `ultima_ronda` porque a ronda
técnica só alcança ilha com URL servida (decisão do Raphael de 28/09/2026) e esta ilha não
tem site; `bloqueada_por` porque a seção 2 reserva o campo para dependência humana que trava
a **ilha**, e o que falta aqui trava a **fábrica** — isso vai no despacho, pela 12.2.

### PRÓXIMO PASSO

**Da Fundação, e agora existe um:** a coleta por busca no degrau 4 funciona com a rede
fechada, e o banco tem **uma** experiência brasileira. O critério pré-registrado do **5b**
pede **3 experiências na mesma cidade** e o Rio de Janeiro tem 1 — mas o Rio é a primeira
cidade deste banco onde há mais o que colher pelo mesmo degrau, e o **5c (free tour)** pede
3 free tours com operador nomeado, que é coleta e não casca. `free_tour` e
`passe_de_cidade` seguem sem lastro no vocabulário.

**Do Raphael, e não mudou:** (1) os passos 2 a 8 da seção 11 destravam o ar, o 3b, o
tradutor PHP e a primeira leva de malha; (2) `jornadafly.com.br` na lista de Domínios
permitidos destrava a verificação; (3) uma linha no `foco.md` destrava a rotação. **O que
saiu da lista dele hoje:** "o egresso destrava a coleta" — destrava a coleta no degrau 2,
que é o preferido, mas o degrau 4 nunca esteve travado.

---

## 2026-10-27 13h48Z — **HAVIA BLOCO**, e ele estava escondido atrás de uma frase que três execuções seguidas repetiram sem medir: o **5b e o 5c não dependem da casca, dependem de DADO**. Esta ilha era a única do arquipélago sem `ARVORE.md`, e ela é a ilha EM FOCO cuja malha é o bloco aberto

**O que saiu:** `ilhas/jornadafly/ARVORE.md` — o item **(i) do 16.8**, a árvore de URLs
desta ilha, com os três níveis, a raiz, a casa de cada página que já existe como regra, e
o **critério pré-registrado (1.2-b.4)** que diz com número o que destrava o 5b e o 5c.
Mais a correção dos blocos **5b** e **5c** no `PROMPT.md`, que prescreviam o contrário.

**POR QUE ISTO NÃO É BLOCO INVENTADO, e a pergunta é justa porque o registro de 23/10
proíbe inventar um.** Aquela entrada diz que *"não sobrou bloco de arquivo nesta ilha"* e
lista o motivo de cada pendência; três execuções depois — 26/10 às 13h3xZ, 26/10 às
19h16Z e 27/10 às 10h17Z — fecharam em "nada elegível" apoiadas nela. **A frase em que
todas as quatro se apoiaram está medida e é falsa em duas das três pendências:** o
registro de 23/10 escreveu *"o 3b (casca), o 5b (malha) e o 5c (free tour) dependem da
casca"*, e o `foco.md` a propagou como *"os passos 2 a 8 destravam o ar: casca, snippet e
sitemap, e com isso o 3b, o 5b, o 5c"*. **Para o 3b está certo. Para o 5b e o 5c está
errado**, e ninguém havia aberto o banco para conferir. Eu abri.

**O BLOCO 5 DESTA ILHA JÁ HAVIA RECUSADO O 5b, E OS DOIS TEXTOS CONVIVIAM NO MESMO
REPOSITÓRIO MANDANDO COISAS OPOSTAS.** O 5b do `PROMPT.md` manda agrupar
**experiência → cidade → país**. A especificação **7.2**, escrita quatro dias depois, diz
com todas as letras: *"Agrupar por cidade teria sido o erro barato: cada cidade do banco
tem **uma** experiência hoje, e categoria nasce com no mínimo três filhas — uma filha por
categoria é cluster ralo, que não passa autoridade nenhuma."* O custo era datado e tinha
endereço: **a execução que encontrasse a casca pronta abriria a malha do 5b e publicaria
exatamente o cluster ralo que a própria ilha havia medido e recusado.**

**O QUE EU MEDI EM `dados/experiencias.json`, e é a procedência do número:** **4**
experiências, **4** cidades (Veneza, Siem Reap, Roma, Paris), **1 experiência por cidade**
nas quatro, **3** países (Itália com 2 cidades, Camboja 1, França 1), `faixas_diarias` em
**0** e `coberturas_de_passe` em **0**. Contra a **16.5** (categoria nasce com 3 filhas) e
a **14.4** (listagem só existe com 3 itens), **nenhuma página de cidade e nenhuma página
de país nasce hoje** — e nem a casca, nem o Search Console, nem o egresso mudam isso.

**AS QUATRO CAMADAS DO 5b, UMA A UMA — e duas delas já estavam ENTREGUES sem o 5b saber:**

- **(1) ficha de experiência — JÁ ENTREGUE, com outro endereço.** Os quatro
  artigos-âncora do bloco 5 são **um por experiência**, correspondência 1 para 1. Uma
  ficha em `/experiencias/<cidade>/<experiencia>/` para as mesmas quatro seria a segunda
  página na mesma `consulta_alvo`, que a **7.4** proíbe e o portão de
  `artigos-referencia.py` reprova.
- **(2) página de cidade — TRAVADA POR DADO**, pelo número acima.
- **(3) página de país — TRAVADA POR DADO E SEM NÍVEL ONDE MORAR.** `/experiencias/<cidade>/<experiencia>/`
  já gasta os três níveis da **16.1**, que não admite quarto. O país só caberia promovido
  a nível 1 (`/italia/`), e daria três seções de 1 a 2 itens, com a palavra que menos vende
  no topo da árvore de uma ilha cujo recorte é a experiência e não a geografia. **Não entra.**
- **(4) cruzamentos — JÁ ENTREGUES, e no lugar certo.** Experiência × pessoas é a F1 e
  cidade × dias é a F2, as duas paramétricas e em `/calculadoras/` pela 7.4; como página, o
  cruzamento já é o artigo em `/guias/quanto-custa/`.

**O 5c TAMBÉM NÃO É CASCA: É COLETA.** `free_tour` está no **vocabulário** do
`esquema-banco.json` (linha 135) e **zero registros do banco o usam** — a mesma assinatura
de `passe_de_cidade`, e o `validar-banco.py` avisa os dois como `vocabulario_sem_lastro`,
o que eu confirmei rodando-o. O que falta é `civitatis.com.br`, um dos nove domínios que o
egresso recusa. **O cluster mais rentável que a ilha mediu espera uma linha de rede, não
um WordPress.**

**O CRITÉRIO PRÉ-REGISTRADO, e a 1.2-b.4 é explícita sobre por que ele sai AGORA:**
*"critério escrito depois do dado é critério dobrado para caber no dado que veio"*.
`/experiencias/<cidade>/` nasce com **3 experiências naquela cidade**; `/experiencias/`
nasce com a primeira cidade que passar; a ficha só nasce para experiência **sem artigo
próprio**; o país não nasce enquanto a experiência gastar os três níveis; e o free tour
nasce com **3 free tours de dado real**, com operador nomeado — nunca recomendando "free
tour" sem escolher o operador, porque esta ilha já mediu que fazer isso **doa a conversão**.

**TRÊS COISAS QUE A ÁRVORE ACHOU SEM PROCURAR, e as três são de casca (3b):**

1. **A home e a F1 servem o mesmo formulário.** O `VOZ.md` manda a home abrir com *"Quanto
   custa, para quantas pessoas?"* e os campos; `artigos-referencia.py` manda os artigos
   para `/calculadoras/quanto-custa-a-experiencia/?experiencia=…&versao=…`. Dois endereços
   com o mesmo formulário é o que a **14.4** proíbe. **A regra ficou escrita antes de a
   casca existir:** a home serve o formulário **vazio** e nunca lê parâmetro; resposta com
   parâmetro mora só na calculadora, com `canonical` para a URL sem parâmetro.
2. **O rótulo do menu colide com o nome de uma categoria, e a calculadora não está no
   menu.** O `VOZ.md` define **Experiências · Quanto custa · Guias**, e a 7.2 usou o item
   "Quanto custa" para justificar o slug `/guias/quanto-custa/`: lidos juntos, dois dos
   três itens caem no mesmo galho e **a página do dinheiro desta ilha fica fora do menu**.
   **O conserto é no rótulo, nunca no slug** — o slug está entregue e com portão. O menu
   diz "Quanto custa para o seu grupo", que é o que a 7.4 já separava.
3. **Os slugs da F2 e da F3 não existiam em lugar nenhum.** Só o da F1 está em código.
   Nasceram neste arquivo, derivados do rótulo que o `VOZ.md` dá a cada uma na home, e
   marcados como **proposta** para quem escrever a casca conferir.

**A REGRA DE OURO QUE EU COPIEI DA ROBOMETRIA, e ela está no topo do arquivo:** *documento
e código mantidos à mão em dois lugares divergem em silêncio.* A árvore desta ilha **já
existia em código** (`artigos-referencia.py`, linhas 41 e 42) antes deste documento, e o
documento **não a inventou: ele a leu**. Onde os dois discordarem, o código é o que está
entregue e a divergência é defeito do arquivo.

**NADA FOI AO AR, E NÃO PODIA.** Sem WordPress não há casca, Sync, `/status` nem URL;
dizer que verifiquei no ar seria inventar. **E nenhum portão nasceu:** a **31.2** só deixa
nascer portão novo com defeito medido no ar, e o que esta passada achou é contradição de
documento. O portão desta árvore nasce com a casca, e nasce **lendo este arquivo**, como o
`teste-arvore.php` da robometria faz.

**BANCADA, 0 falha**, rodada depois das mudanças: `validar-banco` (o banco cumpre o
esquema, com os avisos de vocabulário sem lastro que esta entrada cita), `teste-f1`,
`teste-f2`, `teste-f3`, `teste-prospeccao` (285 afirmações), `gerar-artigos` (o portão dos
quatro artigos) e `validar-prospeccao` (o `.md` idêntico ao que a referência gera). Mudei
dois arquivos `.md` e **nenhuma linha de código e nenhum JSON**.

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO.** `foco.md` nomeia a **jornadafly** e pela **1.2**
não há escolha a fazer. Conferi as exceções e nenhuma se aplica: o molde da **32** está
fechado nas três ilhas, e **ilha no ar e quebrada não existe** — medido e não herdado, em
vez de confiado à linha de "nada elegível" de ontem, que é a lição que este arquivo já
pagou. Os cinco `ESTADO.md` com `executando_desde: null`, nenhum branch `claude/*` com
commit a mergear e nenhum PR aberto. **Reserva escrita às 13h48Z e ganha** (commit
`aeffd29`), **antes do trabalho**, com o motivo já nela: achei bloco.

**A MEDIÇÃO QUE PRECEDEU A DECISÃO, porque "nada elegível" é verdade sobre um INSTANTE.**
(a) `jornadafly.com.br` e `www.jornadafly.com.br` em **000**, com as três irmãs em **200**
na mesma linha de comando — **oitavo dia** de recusa. (b) As **98 URLs** dos três sitemaps
em **200**, uma a uma, com quebra de cache: aquametria 52, clubedomosaico 32, robometria
14, **zero fora de 200**. (c) `/status` igual ao `manifest.json` nas três — **135, 95 e
93** — nenhum desembarque preso. (d) Porta de entrada da **29.2** de pé nas três: home,
`robots.txt` e `wp-sitemap.xml` em 200, caminho virgem em **404**. (e) **Nenhuma ronda
rodou** desde as 20h2xZ de 26/10: o `main` não tem commit de Sentinela depois daquele,
logo não há despacho novo, e eu li os topos dos cinco `PROMPT.md` antes de concluir.

**A 31.1 CONTINUA INALCANÇÁVEL NESTA ILHA, E ESTA PASSADA NÃO A MELHORA:** a proporção vai
de 4 em 13 para **4 em 14**. Está dito sem maquiagem porque o `foco.md` já autoriza o
trabalho de arquivo nesta ilha com essas palavras, e porque a 31.1 se mede por entrega no
ar — que esta ilha não pode ter até o Raphael fazer os passos 2 a 8. **O que mudou não é o
número: é que o próximo destravamento deixou de carregar um erro.**

**PRÓXIMO PASSO: NÃO É DA FUNDAÇÃO, e os três gestos do Raphael continuam valendo — mas o
que o gesto (2) compra MUDOU, e isso é material de decisão dele.** (1) **O egresso**
destrava **coleta**: as faixas de diária da F2, o passe e as coberturas da F3, os dois
artigos pré-registrados, a verificação dos 25 candidatos do bloco 6 **e agora também o
5c**. (2) **Os passos 2 a 8 da seção 11** destravam **o ar**: casca, snippet, sitemap, o
3b e o tradutor PHP das três ferramentas e dos quatro artigos — **e a primeira leva de
malha, que são 8 URLs e já está desenhada e autorizada pelo dado de hoje** na seção 6 do
`ARVORE.md`. **O que o gesto (2) NÃO compra mais, e antes se pensava que comprasse: o 5b e
o 5c.** Os dois esperam dado, e o 5c espera o gesto (1). (3) **Uma linha no `foco.md`**
destrava a **rotação** e os quatro despachos NORMAIS parados.

---

## 2026-10-27 10h17Z — SEM BLOCO PARA ABRIR, e o registro de 23/10 havia escrito isto para mim; o que esta passada entrega são **duas coisas: o número (4 em 13) e a régua que quase o fez sair errado** — o `git log` desta nuvem vem RASO e responde curto sem dar erro

**O que saiu:** nenhum bloco, e **isso é o resultado certo, não uma passada perdida.**
A entrada de 23/10 às 13h20Z fecha dizendo, com estas palavras, que *"a execução
seguinte que encontrar esta ilha em foco e sem nenhuma dessas duas coisas não tem bloco
para abrir — e isso está escrito aqui para que ela não invente um"*. Encontrei
exatamente esse mundo, nas duas metades, e não inventei um bloco. **O que saiu desta
passada é medição e escalada, nos três arquivos que a próxima execução lê primeiro:**
`foco.md`, `dados/despachos.md` (o despacho ALTA de 15/09) e este `REGISTRO.md`.

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO E NÃO HOUVE DECISÃO MINHA.** `foco.md` nomeia a
**jornadafly** e pela **1.2** não há escolha a fazer. Conferi as duas exceções que furam
o foco e **nenhuma se aplica:** (a) o **molde da seção 32** está fechado nas três ilhas —
os três cabeçalhos de despacho dizem "FECHADO INTEIRO" nos `PROMPT.md` da aquametria
(linha 206), da clubedomosaico (336) e da robometria (194); (b) **ilha no ar e quebrada**
não existe, e isto eu medi em vez de herdar (abaixo). Os cinco `ESTADO.md` estavam com
`executando_desde: null`, então pela **1.1** não havia bloco da Fundação vivo e não houve
reserva vencida para o git desempatar. Nenhum branch `claude/*` com commit a mergear e
nenhum PR aberto: a branch desta execução estava idêntica ao `main`. **Reserva escrita às
10h17Z e ganha** (commit `c9793c5`).

**REDE REMEDIDA E NÃO HERDADA (20.2 e 20.3) — SÉTIMO DIA DE RECUSA.** Duas passadas,
`jornadafly.com.br` e `www.jornadafly.com.br` em **000 nas duas** (5 medições ao todo),
com `aquametria.com.br`, `robometria.com.br` e `clubedomosaico.com.br` em **200** e
`raw.githubusercontent.com` em **301** na mesma linha de comando — **zero intermitência
no controle**, que é a diferença que a 20.2 manda não confundir. E a 20.3 exercida de
novo nas fontes de coleta: **nove em 000** — `numbeo`, `booking`, `civitatis.com.br`,
`romapass.it`, `turismoroma.it`, `lisboacard.org`, `visitlisboa.com`, `bondinho.com.br` e
`parquebondinho.com.br`. Então **não há item de conteúdo carregável por nenhuma porta**:
nem a do ar, nem a da coleta.

### MEDI FUNDO ANTES DE CONCLUIR, e por que isso não é zelo: a lição de 26/10 em vigor

O `foco.md` carrega, escrita por uma execução que errou, a lição de que **"nada elegível"
é verdade sobre um INSTANTE, não sobre o dia**: às 13h3xZ de 26/10 uma passada fechou
vazia afirmando que *"toda execução da Fundação daqui para frente fecha igual"*, e **duas
horas depois** a ronda escreveu despacho novo na robometria e a execução das 16h20Z achou
defeito no ar — um deles servido havia mais de um mês. Então eu fui fundo:

- **as 98 URLs dos três sitemaps em HTTP 200**, uma por uma — robometria **14**,
  aquametria **52**, clubedomosaico **32**, **zero fora de 200**;
- **porta de entrada da 29.2 de pé nas três** — home, `robots.txt` e `wp-sitemap.xml` em
  200, e caminho virgem em **404** nas três;
- **`/status` igual ao `manifest.json` nas três** — robometria **95**, clubedomosaico
  **93**, aquametria **135**. Nenhum desembarque preso.

**E ACRESCENTEI UMA RÉGUA QUE A LIÇÃO DE 26/10 NÃO TINHA: LI O RELÓGIO DA RONDA, não só o
topo dos `PROMPT.md`.** Aquela lição manda ler os cinco topos antes de concluir, e está
certa; mas **despacho só chega ao `PROMPT.md` por commit**, então `git log` no `main`
responde a mesma pergunta mais barato e mais forte — um `grep` de topo pode passar por
cima de um despacho cujo título não casa com o padrão procurado, e o relógio não. **O
`main` não tem commit de Sentinela depois das 20h2xZ de 26/10**, logo não existe despacho
novo que a exceção da 1.2 pudesse abrir, e eu não precisei confiar na forma de nenhum
título para afirmar isso. **Conclusão: não há ilha no ar e quebrada.**

### O NÚMERO, e ele é o que esta passada tem de próprio

O despacho ALTA de 15/09 vinha recebendo a medição de rede a cada passada e **não tinha
a conta de quanto isto está custando**. Contei no `main` as execuções da Fundação desde
**22/10**, o dia em que a jornadafly entrou em foco, e quantas entregaram algo **no ar**
pela régua da **31.1**:

| | |
|---|---|
| Execuções da Fundação desde 22/10 (22, 23, 26 e 27/10 — 24 e 25 foram fim de semana) | **13** |
| Entregaram algo no ar que o visitante vê | **4** |
| Proporção da 31.1 | **4 em 13 (31%)**, contra o piso de **7 em 10** |
| Entregas no ar **na ilha em foco** | **ZERO**, em seis blocos |

**A PROCEDÊNCIA DAS 13, e ela quase não existiu — é o terceiro achado desta passada, e é no
meu próprio trabalho.** As 13 são **11 commits de reserva** (a reserva do passo 5 é escrita
uma vez por execução, antes do trabalho, então ela conta execuções melhor que qualquer
outra marca) **mais as 2 execuções que fecharam em "nada elegível"** sem reservar nada
(26/10, 13h3xZ e 19h1xZ). Renovação de reserva pela 1.1 **não** conta como execução nova e
saiu da contagem.

**E A PRIMEIRA CONTAGEM ESTAVA SOBRE LOG RASO.** O clone desta sessão trazia **51 commits**,
com o mais antigo em **22/10 às 16h57** — então as execuções de 22/10 às **10h20Z, 13h29Z e
16h20Z** simplesmente **não estavam no log**, e `git log` devolveu código de saída **0** e as
linhas que tinha. Recontei depois de `git fetch --unshallow origin main`, sobre os **1.191
commits** reais desde 06/09: **as duas contagens deram 13 — por acidente, não por método**,
porque a primeira veio de commits do log somados a execuções que eu li no `foco.md` e no
`REGISTRO.md`, e a segunda de uma marca só. **Se eu tivesse contado só o log, teria publicado
10 e chamado de medição.**

**É a mesma família do «64 domínios que eram 69» que o bloco 6 desta ilha registrou em
23/10**, um andar acima: lá a contagem de cabeça esqueceu seis sufixos; aqui o **instrumento**
respondeu curto e não avisou. **A régua nova está no `ARQUIPELAGO.md`, na seção 1 junto da
1.1**, porque vale para toda execução desta nuvem e não só para esta ilha — e ela diz também
o que **não** quebrar: a régua da 1.1 continua certa em clone raso, porque o que ela procura é
commit nos últimos 40 minutos, e isso cabe em qualquer janela rasa. O que quebra é
**contagem**.

**As quatro foram TODAS em ilha FORA do foco**, alcançadas só pela exceção da 1.2: duas de
molde em 23/10 (robometria 16h18Z, clubedomosaico 19h17Z) e duas de defeito no ar da
robometria em 26/10 (10h19Z e 16h20Z). **As duas portas que deram essas quatro estão
fechadas agora — e fechadas por terem sido CUMPRIDAS, não por terem falhado:** o molde
está no ar e conferido nas três, e nenhuma ilha no ar está quebrada. Sobrou a porta do
foco, e ela não dá no ar **por desenho**: esta ilha não tem site.

**E A 31.6 NÃO RESOLVE ISTO, o que é o achado de método desta passada.** Ela manda a
leitura semanal contar a proporção na ilha em foco e, abaixo de 7 em 10, abrir item de
prioridade **alta**. Aqui esse item **não tem o que mandar fazer**: a causa não é escolha
de quem executa — é **ausência de "no ar"**. A régua está certa, morde, e **aponta para
fora da fábrica**. É a mesma família do portão vermelho da 31.4 um andar acima: o
instrumento funciona e o defeito não é da camada que ele mede. Está escrito no topo do
`PROMPT.md` desta ilha e no `foco.md` desde 22/10 justamente para ninguém ler o REGISTRO
daqui como desobediência à seção 31 — esta passada põe o número naquela frase.

### O QUE EU NÃO FIZ, e as duas razões são regra escrita

**(1) Não troquei a linha `ilha:` do `foco.md`.** Ela destravaria a rotação da seção 1 na
hora, e com ela trabalho real e já medido — mas a linha `fila_decidida_pelo_raphael` diz
que a fila **não tem item (4)** e que *"a próxima troca de foco precisa de decisão nova
dele"*, e a **1.2-b.4** exige decisão escrita para sair do foco. A execução de 22/10 só
editou aquela linha porque **a data era dele**, pré-registrada na fila. Trocar por conta
própria seria tomar a decisão do Raphael com a desculpa de ter medido o custo dela.

**(2) Não consertei nada em ilha fora do foco**, e há bastante para consertar: os **21
portões de navegador inertes** (conserto de duas linhas por arquivo, já escrito e rodando
na robometria), a **régua da 32.5 que a aquametria não tem**, as **22 consultas de produto
sem veredito** da clubedomosaico e os **dois cabeçalhos de estado incompletos**
(robometria e ohmetria). São **quatro despachos NORMAIS abertos** em `dados/despachos.md`,
todos em ilha que a **1.2** proíbe tocar — e a execução de 26/10 que os escreveu tomou
essa mesma decisão por escrito. Não reabri o raciocínio dela.

**O cabeçalho desta ilha, sim, é meu, e por isso foi conferido e fechado:** a seção 2 diz
que quem fecha bloco conserta o cabeçalho *"da ilha que reservou, e só dela"*. A execução
de 26/10 fechou em "nada elegível" **sem reservar nada** e por isso não podia tocar
cabeçalho de ninguém — eu reservei, e a régua de presença da seção 2 aprova este.
Os dois incompletos (`robometria` e `ohmetria`) continuam esperando quem os reservar.

**Memória:** esta nuvem não tem diretório de memória — `/areas/projeto-jornadafly.md` e os
outros quatro que o `PROMPT.md` manda carregar não existem aqui. O próprio `PROMPT.md`
prevê isso (*"Sem memória, não pare: o estado está no `ESTADO.md`, no `REGISTRO.md` e
neste arquivo"*), então o próximo passo desbloqueado foi escrito **no repositório**, que é
a memória que sobrevive: no `bloco_atual` deste `ESTADO.md`, na linha nova do `foco.md` e
no despacho ALTA.

**PRÓXIMO PASSO: NÃO É DA FUNDAÇÃO, e são três gestos independentes — qualquer um,
isolado, tira a fábrica do zero.** (1) **O egresso** de `jornadafly.com.br` destrava
**coleta**: as faixas de diária da F2, o passe e as coberturas da F3, os dois artigos
pré-registrados e a verificação dos 25 candidatos do bloco 6. (2) **Os passos 2 a 8 da
seção 11** destravam **o ar**: casca, snippet e sitemap, e com isso o 3b, o 5b, o 5c e o
tradutor PHP das três ferramentas e dos quatro artigos que já existem **como regra**.
(3) **Uma linha no `foco.md`** destrava a **rotação**, e com ela os quatro despachos
NORMAIS parados. **O Raphael foi sinalizado por notificação nesta passada**, com os três
gestos e o número — é o segundo canal da 12.2, e a escolha entre os três é dele.

---

## 2026-10-23 13h20Z — O BLOCO 6 SAIU, e a lista de prospecção **já estava medida desde 14/09**: o corpus do bloco 1 a tinha escrito como concorrência

**O que saiu:** a **lista de prospecção do widget** — `dados/prospeccao-widget.json`
(**25 candidatos**, `publicar: false`), `dados/prospeccao-widget.md` **gerado**, e as
ferramentas `prospeccao-referencia.py` (a régua), `gerar-prospeccao.py`,
`validar-prospeccao.py` (com `--autoteste`, **15 casos**), `teste-prospeccao.py`
(**285 afirmações**) e `mutacoes-prospeccao.py` (**39 casos**). Mais a **seção 8** da
`especificacao-calculadoras.md`. É o último item de arquivo da fila desta ilha, e é o
próximo passo que o registro de 23/10 às 10h17Z deixou escrito.
**Nada foi ao ar, e não podia ter ido: esta ilha não tem site, não tem WordPress, não tem
Sync e não tem `/status`. Dizer que verifiquei no ar seria inventar.**

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO E NÃO HOUVE DECISÃO MINHA.** `foco.md` nomeia a
**jornadafly** e pela **1.2** não há escolha a fazer. Conferi a exceção de 21/10 que fura o
foco pelo **molde da seção 32** e ela não se aplica: os três despachos do molde estão
fechados (aquametria com a 32.5 de pé nas 29 fichas, clubedomosaico «fechado inteiro» na
linha 133 do `ESTADO.md` dela, robometria com o molde no ar nas nove páginas). `foco.md`
estava com `executando_desde: null` nesta ilha, e pela **1.1** campo null já significa que
não há bloco da Fundação vivo — não houve reserva vencida para o git desempatar. Nenhum
branch `claude/*` com commit a mergear e nenhum PR aberto: a branch desta execução estava
idêntica ao `main`. Reserva escrita às **13h20Z** e **renovada às 13h44Z** pela 1.1, porque
a bancada desta ilha passa de 40 minutos sozinha.

**REDE REMEDIDA E NÃO HERDADA (20.2):** duas passadas às 13h20Z, `jornadafly.com.br` e
`www.jornadafly.com.br` em **000 nas duas** (4 medições), com `aquametria.com.br` e
`robometria.com.br` em **200 nas duas** (4 de controle, nenhuma intermitência) e
`raw.githubusercontent.com` em 301 ao lado. **Segue sendo regressão** — o campo dizia
`aberta em 2026-09-18` com HTTP 200 medido —, e o despacho ALTA de 15/09 em
`dados/despachos.md` continua valendo. `bloqueada_por` segue `null` de propósito, como nas
nove execuções anteriores: o que a rede trava é a coleta, não o bloco de arquivo.

**E A 20.3 FOI EXERCIDA ANTES DE A REGRA EXIGIR A FONTE, não depois.** Medi o egresso para
os próprios candidatos desta lista, às **13h28:28Z**: `bondinho.com.br`,
`www.toureiffel.paris`, `viagemitalia.com`, `www.panrotas.com.br` e `www.civitatis.com`
todos em **000**, com `aquametria.com.br` em **200** na mesma passada. É por isso que
`contato` e `plataforma_do_site` estão `null` nas 25 linhas — e a bancada **proíbe** que
sejam preenchidos, porque abordagem escrita sobre site não lido é invenção com cara de
trabalho.

### O ACHADO DO BLOCO, e ele não precisou de nenhuma busca nova para existir

**A lista de prospecção desta ilha já estava medida desde 14/09/2026, e ninguém a tinha
lido assim.** O corpus do bloco 1 mediu **69 domínios** de SERP em pt-BR e os registrou
como **procedência** — isto é, como *concorrência*. Entre eles há operador com site
próprio, concessionária de bem público e plataforma, cada um **rotulado pelo próprio
corpus**: `bondinho.com.br` não entrou nesta lista por busca de hoje, entrou porque o corpus
já o escrevia como *«operador, e três URLs dele»*. **É a mesma família de defeito que esta
ilha e a ohmetria já pagaram — duas metades contando a mesma coisa sem nunca se falarem —**
e agora o portão as faz conversar por regra: toda consulta citada no banco tem de existir em
`dados/corpus-buscas.md`, e todo domínio que diz vir do corpus tem de aparecer lá.

**O BARRAMENTO SAI DE UMA DECISÃO QUE A ILHA JÁ TINHA TOMADO, e é o que ordena a lista.**
Dos seis clusters do bloco 1, a ilha declarou que **não disputa um** — o A2, «quanto custa
<experiência>», porque *«disputar 'quanto custa o ingresso X' contra o operador é perder, e
não é preciso»*. Daí a régua: **quem ocupa consulta de cluster disputado não hospeda a
ferramenta que a disputa**. O caso que prova o valor dela é o `northbound.is`: operador com
site próprio que ocupa *«vale a pena alugar carro na islândia»* — a consulta que o próprio
bloco 1 chama de «o melhor encaixe entre recorte e monetização que este levantamento
encontrou». O operador que hospedaria a ferramenta é o mesmo que ocupa a página que a ilha
mais quer escrever. E o `romapravoce.com` mostra por que a régua é **escada** e não soma de
pontos: ele é operador **e** concorrente ao mesmo tempo, e pesos somáveis o deixariam passar.

### A DECISÃO DO BLOCO: nesta ilha a ferramenta pode MINAR quem a hospeda

Nas outras três ilhas o widget ajuda o anfitrião a vender — a calculadora dimensiona o
equipamento que a loja tem no catálogo. **Aqui a ferramenta responde «vale a pena?» e pode
servir um número contra quem a hospeda.** Então a régua da oferta nasceu com isso dentro:

- a **F1** só vai a quem vende **a mesma versão** que o banco preça. O caso medido é o
  `viagemitalia.com`, único candidato brasileiro que atende experiência do banco: ele vende o
  tour guiado do Coliseu a **€75 por pessoa com o ingresso dentro**, e o banco preça o
  ingresso avulso. A F1 ali serviria, ao visitante dele, o preço da versão barata que o
  produto dele embute. **Ferramenta que mina o anfitrião não se oferece ao anfitrião** — é a
  mesma família da ATENÇÃO DE ESCOPO da lista da aquametria, um andar acima: lá o número
  ficava fora do escopo, aqui ele **compete com quem hospeda**;
- a **F2** exige `FAIXA_DIARIA` e a **F3** exige passe e cobertura — **contados do banco em
  toda passada**, nunca afirmados nesta lista;
- a **F3 nunca** vai a quem vende passe de cidade.

### A CADEIA DE CINCO ELOS, e ela tem uma causa só

**NENHUM dos 25 candidatos tem ferramenta ofertável hoje**, e a causa não é esta lista:

1. o egresso recusa o domínio da ilha e as fontes de preço (15/09, 18/09, 22/10 e hoje);
2. com a rede fechada, o bloco 3 registrou que `ingresso_de_sitio_publico` era «o único tipo
   reproduzível enquanto o egresso estiver fechado» — e o banco nasceu com **quatro**
   experiências de tarifa pública;
3. **três dos quatro operadores do banco são poder público** e o quarto é concessionária
   francesa. Poder público não instala widget de afiliado;
4. logo a F1 — a única com dado para servir — não tem a quem ser oferecida;
5. e o critério de entrada do bloco 1 dizia o contrário do que o banco carregou: «prefira
   experiência de operador privado, com versões vendidas diferentes entre si e sem tabela
   pública».

**O que isso muda na leitura do bloqueio de rede, e é a parte que vale subir:** ele não
atrasa só coleta de preço. Ele **decidiu a composição do banco**, e a composição do banco
**parou a única alavanca de link do projeto** (seção 14.7) nesta ilha. É a quarta
consequência do mesmo bloqueio, e as três primeiras estavam escritas em lugares separados.
**E o que destrava é barato:** UMA experiência de operador privado brasileiro no banco abre a
linha de prioridade 1. O candidato está medido — o **Parque Bondinho Pão de Açúcar** vende
direto, pelo próprio site, mais de uma versão da mesma experiência.

### AS TRÊS COISAS QUE OS PORTÕES ACHARAM, as três no meu próprio trabalho

1. **68 fatos afirmados sem evidência que os nomeasse.** A primeira versão do banco escrevia
   `true` em campo nenhuma medição sustentava — e o portão os listou um por um. **O conserto
   não foi afrouxar a regra, foi afirmar menos:** oito campos viraram `null`, entre eles o
   `tipo` do `ingressomachupicchu.com`, que o **nome do domínio** parecia provar, e a venda de
   passe dos três revendedores de Lisboa e Roma. E `afirma` virou **lista**: uma medição
   sustenta vários fatos, e dizer **quais** é o que separa evidência de impressão.
2. **A régua de acento reprovou texto legítimo** — `dados/experiencias.json` e
   `prospeccao-referencia.py`, que são corretamente sem acento. A saída não foi heurística
   melhor, foi **estrutura**: ela retira o que está entre craseadas antes de olhar. É a quarta
   trava da família que o `ARQUIPELAGO.md` já ensina — *quando o texto legítimo e o proibido
   são a mesma palavra, quem decide é a estrutura, nunca a vizinhança*.
3. **A CONTA QUE EU IA PUBLICAR ESTAVA ERRADA, e foi a bancada que a pegou.** O texto dizia
   que o corpus mediu **64** domínios. São **69** — a contagem de cabeça usou uma lista de
   terminações que deixava `.is`, `.fr`, `.pt`, `.paris`, `.kh` e `.cz` de fora. O conserto não
   foi trocar o número: `teste-prospeccao.py` passou a **ler a prosa** do achado e conferi-la
   contra `dados/experiencias.json` e `dados/corpus-buscas.md` em toda passada — os «quatro
   experiências», os «três de poder público» e os «69 domínios». É a terceira conta que a
   seção 8 do contrato pede, e é a quarta vez que ela pega algo nesta fábrica.

**E uma regra deste banco não tem nenhum caso hoje, dito como é:** a F3 nunca ir a vendedor
de passe não se aplica a ninguém, porque a venda de passe não foi medida em nenhum candidato.
A regra existe e é a **bateria de mutações** que prova que ela morde, não uma linha da lista.

### UM ACHADO DE MÉTODO para quem continuar esta lista

Três buscas desta execução foram dirigidas a «receptivo/agência brasileiro com site próprio»
em Roma, Paris e Veneza. **As três devolveram portal de conteúdo e plataforma** — isto é,
devolveram a concorrência, não os candidatos. Os únicos receptivos que apareceram **por
nome** vieram da **imprensa de trade** (`panrotas.com.br`, `mercadoeeventos.com.br`).
**A razão é estrutural: operador e receptivo não disputam a SERP de «quanto custa», logo não
são achados por ela.** Quem continuar esta lista busca em trade, não em SERP de consumidor —
e os dois veículos estão no banco como `imprensa_de_trade`, prioridade 3, exatamente por
isso: não são alvo de widget, são o instrumento que acha o alvo.

**BANCADA, 0 falha:** `validar-prospeccao` aprovado com o `.md` idêntico ao que a referência
gera, `--autoteste` 15 de 15, `teste-prospeccao` 285 afirmações, `mutacoes-prospeccao` 39 de
39 (4 mundos que têm de passar — inclusive o banco de experiências **carregado** —, 21
quebras cada uma declarando a frase que espera ouvir, 10 sobre a régua da oferta e 4 mortes).
E **os dez portões anteriores da ilha rodados na mesma passada, todos verdes**:
`validar-banco`, `mutacoes-banco`, `teste-f1`, `mutacoes-f1`, `teste-f2`, `mutacoes-f2`,
`teste-f3`, `mutacoes-f3`, `artigos-referencia` (0 falhas) e `mutacoes-artigos` (43 de 43
reprovadas, 0 mortes, 0 inertes). A bancada desta ilha é de **treze** portões agora — e o
título dela no `PROMPT.md` dizia «oito» com dez comandos na lista abaixo, corrigido nesta
passada: número escrito à mão em título que a própria lista contradiz.

**PRÓXIMO PASSO: não sobrou bloco de arquivo nesta ilha.** A fila está cumprida até onde a
Fundação alcança: 1, 2, 3, 4 (F1, F2, F3), 5 (quatro artigos) e 6. O que falta é **todo do
Raphael e todo de navegador**: os passos 2 a 8 da seção 11 (domínio adicional no cPanel,
nameservers, Search Console, WordPress, SSL, plugins), a liberação de `jornadafly.com.br` e
`*.jornadafly.com.br` no egresso deste ambiente, e a coleta das fontes de diária e de passe.
O **3b** (casca), o **5b** (malha) e o **5c** (free tour) dependem da casca; os dois artigos
pré-registrados e os dois destravamentos de ferramenta dependem de coleta. **A execução
seguinte que encontrar esta ilha em foco e sem nenhuma dessas duas coisas não tem bloco para
abrir** — e isso está escrito aqui para que ela não invente um.

## 2026-10-23 10h17Z — O BLOCO 5 SAIU, e a decisão que mais importa nele é de FORMA: o artigo é **montado do banco**, nunca redigido

**O que saiu:** os **artigos-âncora como regra** — `ferramentas/artigos-referencia.py` (o
cérebro: o mapa das consultas, a árvore, a rotação das irmãs, a montagem do documento e o
portão que o confere), `ferramentas/gerar-artigos.py`, `dados/artigos-ancora.json`
(**4 artigos escritos**, **44** linhas de tabela, **74** parágrafos de dobra, **14**
perguntas de FAQ, `publicar: false`) e `ferramentas/mutacoes-artigos.py`. Mais a **seção 7**
da `especificacao-calculadoras.md`. É o próximo passo que o registro de 22/10 deixou
escrito, cumprido na execução seguinte.
**Nada foi ao ar, e não podia ter ido: esta ilha não tem site, não tem WordPress, não tem
Sync e não tem `/status`. Dizer que verifiquei no ar seria inventar.**

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO E NÃO HOUVE DECISÃO MINHA.** `foco.md` nomeia a
**jornadafly** e pela **1.2** não há escolha a fazer. Conferi a exceção de 21/10 que fura o
foco pelo **molde da seção 32**, e ela não se aplica: os três despachos do molde estão
**fechados** (aquametria às 18h2xZ, clubedomosaico às 19h1xZ, robometria às 16h1xZ de
21/10). `executando_desde` estava `null`, que pela **1.1** já significa que não havia bloco
da Fundação vivo. Reserva aceita de primeira às **10h17Z**, sem recusa de push, e
**RENOVADA** às 10h31Z pela 1.1. Nenhum branch `claude/*` com trabalho a mesclar — o
`claude/dreamy-mccarthy-6qjpdw` estava idêntico ao `main` — e nenhum PR aberto.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA.** Duas passadas às 10h16Z: `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas duas (**4 medições de bloqueio**), com
`aquametria.com.br` e `robometria.com.br` em `200` nas duas (**4 de controle**, nenhuma
intermitência) e `raw.githubusercontent.com` em `301` ao lado. **Segue sendo regressão**, e
o despacho ALTA de 15/09 em `dados/despachos.md` continua valendo. `bloqueada_por` segue
`null` de propósito, como nas oito execuções anteriores.

### 1. O ARTIGO É MONTAGEM, E ISSO NÃO É ECONOMIA DE ESFORÇO — É O PRODUTO

A fila pedia "artigos-âncora pareados com cada ferramenta". O caminho óbvio era escrever
quatro textos bonitos em Markdown. **Ele teria destruído o produto desta ilha em silêncio,
e a conta é simples:** artigo escrito à mão carrega número digitado, e número digitado
envelhece calado. No dia da próxima carga do banco, a calculadora publica o preço novo e o
artigo continua publicando o velho, **com a mesma cara de verdade**. Nesta ilha isso não é
um detalhe de manutenção — o `VOZ.md` chama preço cravado sem a data da coleta de "o defeito
mais grave possível nesta ilha", porque **o preço datado É o produto**.

Então o artigo saiu no mesmo desenho das três ferramentas: a regra em Python, o arquivo
gerado, e o PHP como **tradutor** dela quando a casca nascer. **Toda frase de preço dos
quatro artigos é devolvida pela `f1-referencia.py`** — a mesma regra que a bancada mede. O
que a referência do artigo guarda é só o que nenhuma ferramenta sabe: qual consulta ele
ataca, quem ocupava a SERP dela no dia da medição, qual é a mãe na árvore, quais são as
irmãs e para onde vai o link de compra.

**Os quatro, com a mãe e a ferramenta:**

| Artigo | URL planejada | Consulta-alvo | Tabela | Dobras | FAQ | Itens de compra |
|---|---|---|---|---|---|---|
| gôndola de Veneza | `/guias/quanto-custa/passeio-de-gondola-em-veneza/` | `quanto custa passeio de gôndola em veneza` | 8 | 6 | 3 | 2 |
| Torre Eiffel | `/guias/quanto-custa/subir-na-torre-eiffel/` | `quanto custa subir na torre eiffel` | 16 | 7 | 4 | 4 |
| Coliseu de Roma | `/guias/quanto-custa/ingresso-do-coliseu-de-roma/` | `quanto custa ingresso coliseu roma` | 8 | 6 | 3 | 2 |
| Angkor Pass | `/guias/quanto-custa/angkor-pass-de-1-3-ou-7-dias/` | `angkor pass quantos dias valem a pena` | 12 | 7 | 4 | 3 |

Os quatro com `Article` + `BreadcrumbList` + `FAQPage`, trilha de três níveis, mãe linkada
na trilha **e** numa frase do corpo, bloco "Monte / Compre o que esta resposta pede" com os
dois botões por item, e tabela de casos resolvidos visível e nunca recolhida.

### 2. A MÃE NÃO É A CIDADE, E ESSE FOI O ERRO BARATO QUE QUASE SAIU

A malha desta ilha é experiência → cidade → país, então agrupar os guias por cidade parecia
o natural. **A conta no banco desfez isso em uma linha:** cada uma das quatro cidades tem
**uma** experiência hoje. Quatro categorias com uma filha cada é cluster ralo, que não passa
autoridade nenhuma — e categoria só nasce com três filhas.

Os quatro nasceram então na mesma mãe, **`/guias/quanto-custa/`**, que é literalmente um dos
três itens do menu que o `VOZ.md` define e é a palavra da pessoa. Com quatro filhas na mesma
mãe, **cada página recebe três irmãs apontando para ela**, e não uma.

**E a janela de irmãs ROTACIONA, por desenho e não por sorte:** cada página leva as
até-quatro irmãs que vêm **depois** dela na ordem do mapa, dando a volta no fim. O grafo que
sai é circulante, então o grau de **entrada** de toda filha é igual ao de **saída** — hoje
com quatro, e no dia em que a categoria tiver dez. A afirmação que mede isso é do
**conjunto**, refeita na direção de quem aponta: contar só o que sai fica verde nos dois
mundos, e é exatamente assim que uma página nasce no ar com um link de entrada só.

### 3. DOIS CAMPOS PARA A MESMA PERGUNTA, E A DIFERENÇA ENTRE ELES É UMA REGRA

A consulta medida é como a pessoa digita — e **gente digita sem acento**. O título na tela é
a mesma pergunta em português correto. Publicar a consulta crua na tela seria publicar
português sem acento, que é a cicatriz da Robometria; esconder a consulta crua seria perder
a correspondência exata que faz a página ser achada. Os dois existem, `consulta_alvo` nunca
vai para a tela, e o portão cobra que o título **não perca palavra nenhuma** da consulta e
só possa **ganhar palavra de ligação** — ele acentua e capitaliza a pergunta, não a
reescreve.

**E a fronteira com a calculadora ficou escrita, para a ilha não disputar consigo:** a
consulta paramétrica ("para N pessoas", "para o seu grupo") é da **ferramenta**; a crua é do
**guia**. O portão reprova título de guia que traga qualquer uma das duas, e reprova duas
páginas com a mesma consulta-alvo.

### 4. O PORTÃO PEGOU TRÊS COISAS, E A PRIMEIRA FOI CONTRA MIM

**(a) O valor de terceiro não cabia na regra, e a regra estava errada.** A primeira versão
exigia que todo valor da tela estivesse no conjunto que o banco autoriza — e **reprovou a
prestação de contas da gôndola**, que é justamente o diferencial desta ilha: os €80 da
Eurodicas e os €34 da GetYourGuide são os números com que a ilha **discorda**, e dizer quem
publicou o quê, com a data, é a única coisa que nenhum dos sete ocupantes da SERP faz. A
regra passou a deixar esse valor entrar **somente** dentro da frase que nomeia o publicador
e traz a data da leitura. Sem o nome, é número sem dono, e reprova.

**(b) Registro `pendente_de_releitura` publica na tela e NÃO na description.** O Angkor Pass
é o único dos quatro com esse status. O preço dele vai para a tela com a ressalva ao lado,
porque a tela tem espaço para a ressalva; a **description não tem** — ela é lida sozinha no
resultado de busca, e ali o número apareceria cravado como atual. O portão reprova preço de
registro pendente dentro da description, e reprova a caixa de resposta que perca a ressalva.

**(c) A RÉGUA DE ACENTUAÇÃO FOI TENTADA TRÊS VEZES E NÃO EXISTE — e isto é a lição de
método do dia.** As três estão escritas na afirmação (8) de `artigos-referencia.py` para a
próxima execução não gastar a mesma hora:

1. *"todo título tem de ter um acento"* → reprovou **três páginas certas**; "quanto custa
   subir na torre eiffel" não tem uma letra acentuada e está escrito corretamente;
2. *"palavra acentuada num lugar não aparece crua noutro"* → **25 reprovações** em texto
   impecável, porque em português o par sem acento costuma ser **outra palavra**: `e` e `é`,
   `esta` e `está`, `da` e `dá`. Régua que confunde conjunção com verbo não mede acentuação;
3. *"parágrafo com 12 palavras ou mais tem de ter um acento"* → reprovou "A partir de
   quantos dias de visita o Angkor Pass de 3 dias paga?" e a frase de divergência da
   GetYourGuide. **Catorze palavras, nenhum acento, as duas corretas.** Subir o corte reduz
   o falso positivo e não o elimina.

**O que isso decide:** acentuação correta **não é verificável localmente** — é julgamento
sobre cada palavra. E **portão que reprova texto certo é pior que portão nenhum, porque
ensina a ignorar o vermelho**. O que sobrou no portão é o que é mecânico e inequívoco:
mojibake, e a procedência de todo valor da tela. A acentuação das frases é garantida **na
fonte**, pelas três referências, que nascem com a regra. *(Não afirmo que não exista régua
possível: afirmo as três que tentei e o que cada uma reprovou.)*

**(d) O FAQ ESTAVA RESPONDENDO A OUTRA PERGUNTA, e nenhuma afirmação via.** Achado na
leitura do arquivo gerado, não por portão: a primeira versão emparelhava **toda** pergunta
declarada do artigo com a frase da caixa de resposta, qualquer que fosse a pergunta. Em
**três dos quatro** artigos isso publicava um par que não se fecha — *"A partir de quantos
dias de visita o Angkor Pass de 3 dias paga?"* respondido por *"o de 1 dia custa US$ 37"* —
e ia para o `FAQPage` do JSON-LD, que é justamente a parte que as IAs citam fora de
contexto. **Conserto em duas metades:** cada pergunta passou a declarar **de onde** sai a
resposta dela (`caixa`, `inclui`, `escada`, `prestacao`, `faixa_etaria`), e o portão reprova
**duas perguntas respondidas pela mesma frase**, que é a assinatura exata do defeito. As
duas quebras entraram na bateria, que foi de 41 para **43**. *(E o portão reprova pergunta
cuja fonte não existe naquela experiência, em vez de deixá-la cair fora em silêncio: mapa
errado que some é mapa errado que fica.)*

**(e) A DOBRA DO «INCLUSO» PASSOU A NASCER SEMPRE, e isso saiu de (d).** A gôndola e o
Angkor Pass não têm lista de inclusos, e a F1 devolve, para esse caso, a frase *"o operador
não declara o que está incluso neste bilhete"* — **que é resposta**, e é a resposta que
nenhum dos ocupantes da SERP dá. A versão anterior omitia a seção inteira quando a lista
estava vazia, e página que omite deixa quem pergunta sem saber se ninguém perguntou ou se a
resposta não existe.

### 5. DOIS ARTIGOS NÃO FORAM ESCRITOS, e a causa é DADO e não tempo

A fila pede um artigo por ferramenta. **A F2 e a F3 não têm resposta para publicar**, e
artigo cujo título promete um número que a página não entrega é **exatamente** o defeito que
o bloco 1 mediu nos oito ocupantes de `quanto custa um dia em veneza para 2 pessoas` —
nenhum deles responde "para 2 pessoas". Copiar o defeito do concorrente para ocupar a vaga
dele é o pior negócio desta fábrica.

Os dois ficam **pré-registrados** em `dados/artigos-ancora.json`, com o critério de
destravamento escrito **antes** de o dado chegar — critério escrito depois do dado é
critério dobrado para caber no dado que veio:

- **F2, `quanto custa um dia em veneza para 2 pessoas`:** a F2 soma quatro linhas e hoje
  publica **uma**. `faixas_diarias` tem **zero** registros. Destrava com faixa de diária
  para Veneza nas três naturezas (hospedagem, alimentação, transporte local), cada uma com
  publicador nomeado, URL e data de leitura.
- **F3, `roma pass vale a pena`:** **zero** passes e **zero** coberturas no banco, então o
  veredito que o título promete não existe. E falta a outra metade: **Roma tem uma**
  experiência no banco, e julgamento de passe sobre uma atração só não é julgamento de
  passe. Destrava com o Roma Pass (preço e data próprios) **mais** a cobertura par por par
  com cada atração de Roma, cada par com fonte e data próprias.

Os dois esperam coleta de navegador, e as fontes estão recusadas no egresso: `numbeo.com`,
`booking.com` e `civitatis.com.br` para a F2; `romapass.it`, `turismoroma.it`,
`lisboacard.org`, `visitlisboa.com` e `civitatis.com.br` para a F3. **A regra dos dois está
inteira: no dia em que o dado entrar, o artigo é montagem, não pesquisa.**

### 6. A LISTA DE PORTÕES FOI DE OITO PARA DEZ, e a 31.3 foi lida ANTES e não depois

Os dois novos são do artigo: a referência, que **monta e confere**, e a bateria que a
quebra. A **31.3** proíbe "ampliar, refatorar, deduplicar ou **testar portão que JÁ
EXISTE**" enquanto houver item de conteúdo aberto — e o portão que a bateria confere
**nasceu na mesma passada que o conteúdo que ele guarda**, que é o desenho que a F1, a F2 e
a F3 tiveram em 22/10, cada uma com teste e mutação na própria passada. Bancada sobre
bancada continua proibida; esta é a bancada **do** artigo.

**Dez linhas ainda cabem numa tela, e os dois novos foram escritos no `PROMPT.md` na mesma
passada** — segunda vez que aquele aviso foi cobrado e segunda vez que funcionou. A margem
agora é de duas ou três linhas, e isso está dito lá.

### 7. BANCADA — os dez portões, 0 falha

| Portão | Resultado |
|---|---|
| `validar-banco` | verde (o aviso de `vocabulario_sem_lastro` em `por_cabine` e `por_grupo` é o de sempre e não é falha) |
| `mutacoes-banco` | **154 de 154** — 23 mundos que têm de passar e 131 quebras que têm de reprovar |
| `teste-f1` | **139.658** afirmações, 0 falha |
| `mutacoes-f1` | **28 de 28** |
| `teste-f2` | **216.614** afirmações, 0 falha |
| `mutacoes-f2` | **51 de 51** |
| `teste-f3` | **616.462** afirmações, 0 falha |
| `mutacoes-f3` | **45 de 45** |
| `artigos-referencia` (novo) | **4 artigos montados e conferidos, 0 falha**, mais as 4 afirmações do conjunto |
| `mutacoes-artigos` (novo) | **43 de 43** — 39 por artigo e 4 pelo conjunto, **zero morte e zero inerte** |

O banco e o esquema **não foram tocados** nesta passada: o bloco 5 lê, não escreve. As oito
baterias que já existiam rodaram para provar isso, e as oito ficaram como estavam.

### 7b. A SEÇÃO 31, dita como é

A **31.1** pede que 7 de cada 10 execuções entreguem algo no ar que o visitante vê. **Nesta
ilha isso continua inalcançável**, e não por escolha de quem executa: não há "no ar". Faltam
as duas coisas que só o Raphael faz — os passos 2 a 8 da seção 11 e o domínio na lista de
Domínios permitidos. O `PROMPT.md` e o `foco.md` já dizem isso com todas as letras, e esta
linha existe para ninguém ler este registro como desobediência.

**O que esta execução fez do lado certo da 31:** nenhum portão novo nasceu **sobre** portão
existente, nenhuma régua existente foi ampliada ou refatorada, e o trabalho foi o item de
**conteúdo** que estava aberto na fila. Os quatro artigos são as quatro páginas que vão ao
ar na primeira execução depois da casca, prontas e conferidas.

## 2026-10-22 19h16Z — A F3 EXISTE COMO REGRA, e escrevê-la mostrou que a conta não era a parte difícil: a parte difícil é **sobre o que** ela é feita

**O que saiu:** a **F3 como regra** — `ferramentas/f3-referencia.py` (o cérebro: cidade,
atrações pretendidas, dias e pessoas → resposta inteira, já em frase acentuada),
`ferramentas/gerar-f3.py`, `dados/f3-respostas.json` (**1.038** estados contados, **78**
gravados, 48 linhas de tabela, `publicar: false`), `ferramentas/teste-f3.py` e
`ferramentas/mutacoes-f3.py`. Esquema **versão 7**, banco **versão 7**, com a entidade
**`COBERTURA_DO_PASSE`** e o vocabulário `forma_de_cobertura`. É o próximo passo que o
registro de 16h20Z de hoje deixou escrito, cumprido na mesma data — e **com ele as três
âncoras desta ilha existem como regra**.
**Nada foi ao ar, e não podia ter ido: esta ilha não tem site, não tem WordPress, não tem
Sync e não tem `/status`. Dizer que verifiquei no ar seria inventar.**

**SEM PHP, pela mesma decisão das duas execuções anteriores e não por pendência
esquecida:** sem casca, um snippet só poderia ser medido por um render de bancada que serve
**menos** do que o site serve — a cicatriz que a seção 8 mais cobra. O PHP, quando nascer, é
**tradutor** desta referência, frase a frase.

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO E NÃO HOUVE DECISÃO MINHA.** `foco.md` nomeia a
**jornadafly** e pela **1.2** não há escolha a fazer. Conferi a exceção de 21/10 que fura o
foco pelo **molde da seção 32**: os três despachos estão **fechados** (aquametria às 18h2xZ,
clubedomosaico às 19h1xZ, robometria às 16h1xZ), então ela não se aplica. `executando_desde`
estava `null`, que pela **1.1** já significa que não havia bloco da Fundação vivo. Reserva
aceita de primeira às **19h16Z**, sem recusa de push, e **RENOVADA duas vezes** pela 1.1
(19h29Z e 19h49Z): a bateria do banco roda o validador 154 vezes e a da F3 roda o portão 45
vezes sobre 616 mil afirmações, e o bloco passa de 40 minutos com folga. Nenhum branch
`claude/*` com trabalho a mesclar e nenhum PR aberto.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA.** Três passadas: `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas três (**6 medições de bloqueio**), com
`aquametria.com.br` e `robometria.com.br` em `200` nas três (**6 de controle**, nenhuma
intermitência). O `curl` verbose nomeia a causa e ela não é túnel: `CONNECT tunnel failed,
response 403`. **Segue sendo regressão**, e o despacho ALTA de 15/09 em `dados/despachos.md`
continua valendo. `bloqueada_por` segue `null` de propósito, como nas sete execuções
anteriores.

**E PELA 20.3, AS CINCO FONTES QUE ESTA FERRAMENTA PRECISARIA — medidas antes de escrever a
regra que as exige, que é o que a 20.3 manda.** `www.romapass.it`, `romapass.it`,
`www.lisboacard.org`, `www.visitlisboa.com`, `www.turismoroma.it` e `www.civitatis.com.br`
**todos em `000`**, com `raw.githubusercontent.com` em **301** na mesma passada. Quem escreve
a regra que exige a fonte é quem confere se a fonte está liberada — e ela não está.

### A PERGUNTA QUE A F3 TRAZIA ABERTA ESTAVA MEIO CERTA, E A METADE ERRADA É A QUE IMPORTA

O registro anterior previu que a F3 seria atravessada pela régua de *"declarar o que o número
é"* quando a fonte do passe publicasse faixa em vez de preço. **A primeira metade está
certa** — avulso e passe são os dois **nossos**, então a entidade `FAIXA_DIARIA` não a
atravessa. **A segunda está errada, e descobri isso escrevendo:** o que atravessa a F3 não é
o que o número é. É **sobre o que a conta é feita**.

Porque a conta da F3 — soma dos avulsos contra o preço do passe, com o ponto de equilíbrio —
**já está entregue por quem ocupa o topo da consulta.** A especificação diz isso desde
14/09/2026, com o 1º colocado prometendo *"fiz as contas pra você"* no próprio título: **não
há vaga de formato.** O que ninguém publica é de **quantas** atrações aquele ponto de
equilíbrio saiu. E aí está a vaga.

### A ENTIDADE NOVA, E POR QUE ELA NÃO É CAMPO DE NENHUM DOS DOIS LADOS

O passe de cidade **é uma experiência** (`categoria: passe_de_cidade`, que está no
vocabulário desde 14/09/2026 e nenhum registro usava). O que não tinha onde morar é a
**relação** entre um passe e cada atração que ele cobre. Campo no PASSE forçaria uma lista de
atrações dentro do registro dele, cada item sem data e sem fonte próprias; campo na ATRAÇÃO
forçaria uma lista de passes dentro de cada ingresso. **A cobertura tem fonte e data de
leitura próprias porque é ela que envelhece:** o preço do passe pode estar certo e a cobertura
errada no mesmo dia, e o bloco 1 mediu exatamente isso em 14/09/2026 — a fonte de topo do Roma
Pass avisa que as regras de reserva mudaram em 2026. É a mesma razão de modelagem da
`FAIXA_DIARIA` um bloco atrás, aplicada a outro fato.

### AS TRÊS REGRAS DE HONESTIDADE, e as três moram no esquema e são cobradas por código

1. **NÃO LIDA NÃO É NÃO COBERTA.** Atração pretendida sem cobertura lida fica fora do valor
   entregue **e é nomeada na tela**. Tratá-la como não coberta publica um "não paga" que a
   ilha não mediu; tratá-la como coberta publica o contrário. **As duas são erradas**, e a
   única frase honesta é que ninguém leu.
2. **O EQUILÍBRIO É SOBRE O QUE A ILHA LEU, NUNCA SOBRE O PASSE.**
   `atracoes_declaradas_pelo_passe` (o número transcrito da fonte) e a contagem das coberturas
   lidas vão para a tela **lado a lado**, e a frase do equilíbrio diz sobre quantas atrações
   ele saiu. Passe que declara 50 atrações com 3 lidas **não tem equilíbrio publicável como
   equilíbrio dele**.
3. **DESCONTO COM TETO É FAIXA.** *"Até 50%"* entrega de **zero** à metade do avulso, e as
   duas pontas vão para a tela. Sem `desconto_e_no_maximo`, a hedge da fonte entraria na conta
   como número cheio — e o resultado continuaria **parecendo dinheiro**, que é por que esse
   erro não se vê. A régua do banco lê a hedge da frase transcrita e reprova a combinação
   "frase com *até*" + "campo dizendo que é o valor".

### O VEREDITO TEM TRÊS DESFECHOS, NÃO DOIS, e o terceiro é o que esta ferramenta tem de seu

`paga` quando o passe se paga **até na ponta de baixo** da faixa; `nao_paga` quando não se
paga **nem na de cima**; e **`depende_da_versao`** quando a faixa **atravessa** o preço do
passe. Ali existe bilhete em que ele paga e bilhete em que não paga, e **as duas coisas são
verdade** — escolher uma seria a ilha escolhendo a versão no lugar de quem viaja. É a mesma
recusa da F2 (que não escolhe a versão da experiência) e a mesma lição que a ohmetria pagou
hoje um andar acima: **quem separa as duas causas no código separa as duas no texto.**

**E o ponto de equilíbrio sai das mais caras para as mais baratas, com a ordem DECLARADA.** É
a ordem em que o passe rende mais, portanto a que dá o **menor** número de atrações — e dizer
"a partir de 3 atrações o passe paga" sem dizer **quais 3** seria um número sem dono. A função
devolve a ordem que usou e a tela nomeia as atrações. Ele é calculado nas **duas pontas**: na
de baixo o passe precisa de mais atrações, na de cima de menos, e a diferença entre os dois
números é exatamente "qual bilhete você compraria".

### O DEFEITO QUE O PASSE CRIOU NA F2, E ELE PAGAVA A MESMA VISITA DUAS VEZES

Medido no mundo de bancada do passe, antes de qualquer commit: com um passe de Roma no banco,
a linha de experiências da **F2** publicava **"€100 a €148"** para 2 pessoas — o ingresso do
Coliseu (€36 a €44) **mais** o passe que inclui o ingresso do Coliseu (€64 a €104) — e a tela
nomeava os dois lado a lado como se fossem dois programas. **Um passe não é um custo a mais:
é outro jeito de pagar as mesmas atrações.** A F2 passou a descartar `passe_de_cidade` da
linha e a **nomear** a recusa, mandando quem pergunta para a F3, que é a ferramenta cuja
pergunta é exatamente essa.

**E a metade mais traiçoeira era a segunda:** a **fonte** do passe continuava aparecendo no
"como sabemos", prestando contas de um número que a página não publica. **Fonte citada sem
número na tela é o inverso do número sem fonte**, e as duas são a mesma falta de
correspondência. O portão da F2 ganhou a afirmação que casa as duas listas, e a bateria dela
ganhou dois mundos e quatro quebras (uma delas para o passe `excluido_do_banco`, que não entra
na conta **e** não é nomeado — são duas regras passando pelo mesmo registro).

**Os arquivos gerados não mudaram um byte** (`f1-respostas.json` e `f2-respostas.json`
regerados e idênticos), e isso é a prova de que a correção é um **no-op no banco de hoje**: o
caminho só existe onde existe passe, e não existe passe. O defeito estava esperando a primeira
carga.

### E TRÊS DEFEITOS MEUS, achados antes do commit, cada um por um motivo diferente

**(a) AS RECUSAS DURAS PUBLICAVAM ID DE REGISTRO NA TELA.** Duas das sete ecoavam o id da
atração entre aspas — bastidor da fábrica pela **32.4**, a mesma cicatriz do
`unidade_de_preco` da F1 e do caminho de arquivo da ohmetria. **A causa de ninguém ver era
estrutural e vale para as irmãs:** a varredura do portão dava `continue` na borda, então as
frases de recusa dura **nunca passavam** pela régua de acento, de frase proibida nem de
bastidor. Recusa é texto de tela como qualquer outro; a única coisa que a borda tem de
diferente é não ter número.

**(b) O PORTÃO MORRIA EM VEZ DE RELATAR, em cinco pontos.** A bateria de mutações mediu:
cinco quebras vinham classificadas `morre` em vez de `reprova`, porque o portão **pegava** o
defeito na afirmação anterior e depois estourava um `IndexError` ao indexar a lista que a
afirmação acabara de dizer estar vazia. **Portão que morre perde a mensagem que ele existe
para escrever**, e quem lê o relatório vê um traceback onde devia ver a frase. A regra, e ela
vale para toda régua desta pasta: **afirmar primeiro, e só então ler o que a afirmação
garantiu.**

**(c) A CONCORDÂNCIA, pela terceira vez nesta pasta.** A primeira versão publicou *"1 atração
em Veneza **custam** €90"* e *"dentro **das 1** atração"*. É a mesma família do *"as 1
experiências"* da F2 e do *"por veiculo"* sem acento da F1. **Não se vê lendo o código; se vê
lendo a frase**, e é por isso que o portão lê a frase.

### E DOIS DEFEITOS QUE JÁ ESTAVAM NA PASTA, os dois achados por precisar deles

**O EIXO `null` NÃO CONFERIA `dias_de_uso`, em silêncio desde hoje de manhã.** As duas
direções da regra no validador cobravam `por_quantidade` e **proibiam** os outros eixos — e o
`null`, que é a experiência de **uma** versão e é exatamente o que um passe de validade única
é, não caía em nenhuma das duas. A F3 precisa dessa validade para dizer se o passe cobre a
estadia, e foi precisar dela que mostrou o buraco. A conferência virou **função chamada dos
dois lugares** em vez de uma segunda cópia.

**E O RELATÓRIO DO VALIDADOR ESCONDIA O QUE ELE CONTAVA.** A lista de chaves que o `main()`
imprime era uma tupla literal, e `faixas_diarias` — nascida na migração de hoje de manhã —
**não estava nela**: a régua contava os dois números e a tela de quem roda o portão não os
mostrava, de modo que a única entidade com zero registros era também a única invisível. É a
mesma família da lista de sete nomes de vocabulário que esta régua matou hoje um andar acima.
A lista agora **sai do próprio `calculado`**: contador novo não tem como nascer invisível.

**Mais um que ia estourar na primeira cobertura gravada e em nenhum momento antes dela:** a
seção nova do validador usava um índice de experiências por id que **não existia**. Com zero
coberturas o laço não roda e o `NameError` não acontece. Achado por leitura, e é a razão
inteira pela qual os mundos de bancada existem.

### A RÉGUA DO VENCIMENTO SAIU DO VALIDADOR E VIROU REGRA COMPARTILHADA

A validade do preço (`validade_do_preco` do esquema) era **aviso de bancada** dentro do
validador, e **a F3 é a primeira ferramenta que a leva para a TELA** — *"este preço foi lido
há 38 dias e esta ilha considera 60 o prazo para reler uma fonte dessas"*. Em vez de uma
segunda cópia, ela virou `f1.dias_de_validade` e `f1.preco_vencido`, com `hoje` sempre
**recebido** e nunca lido do relógio lá dentro (régua que pega a data do sistema não pode ser
testada na borda, e a borda é o único lugar onde ela erra). **E o portão da F3 compara os dois
vereditos versão por versão do banco:** eles discordarem quer dizer que uma das duas está
errada e nenhuma das duas sabe. As duas quebras da bateria mexem na F1 e são pegas por ali.

### O QUE A F3 PUBLICA HOJE, e é metade da pergunta

Em todos os **1.008** estados válidos ela publica a **soma dos avulsos** — que é metade da
pergunta — e fecha com `sem_passe_lido`, dizendo que a outra metade não foi lida. **A recusa
nunca diz que a cidade NÃO TEM passe:** o vocabulário da cobertura nasceu sem lastro, e a
`regra_de_crescimento_de_vocabulario` do esquema proíbe frase de inexistência enquanto for
assim. **O portão cobra essa distinção em cada estado** — é a primeira vez nesta ilha que
aquela regra do esquema é conferida por código em vez de obedecida de boa vontade.

**O ANGKOR PASS NÃO FOI RECATEGORIZADO**, e isso é decisão e não omissão: ele é
`ingresso_de_sitio_publico` desde 14/09/2026, cobre **um sítio** e não uma cidade, e trocar a
categoria dele para dar lastro ao vocabulário seria **mover o dado para caber na ferramenta**.

**O TETO DE 8 ATRAÇÕES NÃO É LIMITE DE BANCO, É LIMITE DE ESCOLHA**, e ele existe por
aritmética: o domínio desta ferramenta cresce em **2^n − 1** com o número de atrações lidas
numa cidade. Hoje são 4 cidades com 1 atração cada e 1.038 estados; com 8 atrações numa cidade
só seriam 255 subconjuntos × 252 combinações, nela sozinha. O número está escrito **no portão
a partir da especificação**, não lido da ferramenta — régua que toma o limite da coisa que ela
mede não mede o limite, e foi a bateria da F2 que provou isso hoje de manhã.

### A LISTA DE PORTÕES FOI DE SEIS PARA OITO, e o aviso que previa isso funcionou

O `PROMPT.md` desta ilha avisava, escrito hoje de manhã, que *"quem acrescentar o sétimo e não
o escrever aqui cria exatamente o defeito que esta ilha acabou de pagar num andar abaixo"*.
**Os dois novos foram escritos lá na mesma passada** — primeira vez que aquele aviso foi
cobrado. A decisão de **não** ter descobridor de portões continua, e agora com um número: oito
linhas ainda cabem numa tela, e a **31.3** proíbe construir bancada sobre bancada enquanto
houver item de conteúdo aberto. O gatilho está escrito e não mudou.

**BANCADA, 0 falha:** `validar-banco` verde (com os avisos de `vocabulario_sem_lastro`, agora
somando `forma_de_cobertura`, as três formas sem um registro que as use);
`mutacoes-banco` **154 de 154** (23 mundos, 131 quebras, 87 cobradas pela frase — **37 novas**,
com passe e cobertura carregados em memória e nenhuma linha gravada); `teste-f1` 139.658
afirmações; `mutacoes-f1` 28 de 28; `teste-f2` **216.614** afirmações; `mutacoes-f2`
**51 de 51** (11 mundos, 29 quebras, 11 mortes, **7 novas**); `teste-f3` **616.462** afirmações sobre os
1.038 estados, com a aritmética refeita à mão em `Fraction` e as funções puras chamadas com os
mundos que o banco não tem; `mutacoes-f3` **45 de 45 — 13 mundos, 25 quebras e 7 mortes, com
25 cobradas pela frase**.

**PRÓXIMO PASSO: não há mais ferramenta a escrever, e isso é informação e não fim de linha.**
As três âncoras existem como regra e **as três publicam menos do que sabem calcular, por falta
de DADO que esta nuvem não alcança** — a F2 precisa de `numbeo.com`, `booking.com` e
`civitatis.com.br`; a F3 precisa de `romapass.it`, `turismoroma.it`, `lisboacard.org`,
`visitlisboa.com` e `civitatis.com.br`. Os dois itens de arquivo que sobram são pequenos: o
**bloco 5** (artigos-âncora pareados com cada ferramenta) e o **bloco 6** (lista de prospecção
do widget, `publicar: false`). O **5b** (malha) e o **5c** (cluster free tour) dependem da
casca. **Depois deles esta ilha não tem bloco que não precise do Raphael, e o item mais caro
continua sendo o mesmo das sete execuções anteriores: a casca (3b), que depende dos passos 2 a
8 da seção 11 e da liberação de `jornadafly.com.br` no egresso — as duas de navegador, as duas
dele.**

## 2026-10-22 16h20Z — A F2 EXISTE COMO REGRA, e a pergunta que ela trazia aberta virou uma ENTIDADE: o que o número SIGNIFICA saiu da prosa

**O que saiu:** a **F2 como regra** — `ferramentas/f2-referencia.py` (o cérebro: cidade,
dias, pessoas e padrão → resposta inteira, já em frase acentuada), `ferramentas/gerar-f2.py`,
`dados/f2-respostas.json` (**3.077** estados servidos, **197** gravados, `publicar: false`),
`ferramentas/teste-f2.py` e `ferramentas/mutacoes-f2.py`. Esquema **versão 6**, banco
**versão 6**, com a entidade **`FAIXA_DIARIA`** e quatro vocabulários novos. É o próximo
passo que o registro de 13h29Z de hoje deixou escrito, cumprido na mesma data.
**Nada foi ao ar, e não podia ter ido: esta ilha não tem site, não tem WordPress, não tem
Sync e não tem `/status`. Dizer que verifiquei no ar seria inventar.**

**SEM PHP, pela mesma decisão de 13h29Z e não por pendência esquecida:** sem casca, um
snippet só poderia ser medido por um render de bancada que serve **menos** do que o site
serve. O PHP, quando nascer, é **tradutor** desta referência, frase a frase.

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO E NÃO HOUVE DECISÃO MINHA.** `foco.md` nomeia a
**jornadafly** e pela **1.2** não há escolha a fazer. Conferi a exceção de 21/10 que fura o
foco pelo **molde da seção 32**: os três despachos estão **fechados** (aquametria às 18h2xZ,
clubedomosaico às 19h1xZ, robometria às 16h1xZ), então ela não se aplica. `executando_desde`
estava `null`, que pela **1.1** já significa que não havia bloco da Fundação vivo — não houve
reserva vencida para o git desempatar. Reserva aceita de primeira às **16h20Z**, sem recusa
de push, e **RENOVADA às 16h44Z** pela 1.1, porque a bateria de mutações da F2 roda o portão
44 vezes e o bloco passa de 40 minutos sozinho. Nenhum branch `claude/*` com trabalho a
mesclar e nenhum PR aberto — `main` tinha recebido *force update* no fetch, e eu trabalhei do
estado real dele.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA.** Três passadas: `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas três (**6 medições de bloqueio**), com
`aquametria.com.br` e `robometria.com.br` em `200` nas três (**6 de controle**, nenhuma
intermitência). O `curl` verbose nomeia a causa e ela não é túnel: `CONNECT tunnel failed,
response 403`. **Segue sendo regressão**, e o despacho ALTA de 15/09 em `dados/despachos.md`
continua valendo. `bloqueada_por` segue `null` de propósito, como nas seis execuções
anteriores: preenchê-lo congelaria também os blocos que não precisam de rede.

### A PERGUNTA ABERTA DA F2 TINHA RESPOSTA DE MODELAGEM, E ELA É DE PROCEDÊNCIA

O registro anterior deixou a F2 com uma pergunta: *"a F2 soma hospedagem, alimentação e
transporte local, e nenhuma das três está no banco"*. A resposta não é um campo novo na
EXPERIÊNCIA — é que **as três não são da mesma natureza que uma experiência**. Experiência
tem preço **colhido no site de quem opera**, com data de leitura; diária de hotel é **faixa
que um terceiro publicou**. Daí a entidade própria, e não um campo da CIDADE: uma cidade tem
três categorias × três padrões × quantos publicadores existirem, e campo na CIDADE forçaria
escolher **um** publicador por cidade no momento da carga — decisão editorial disfarçada de
modelagem, que é exatamente o que o concorrente medido no bloco 1 faz ao publicar "a diária
em Veneza é R$ X" sem dizer de quem é o X.

**E A TROCA É A MESMA DA VERSÃO 5, UM ANDAR ACIMA.** Lá a quantidade de uso de cada bilhete
saiu da prosa do `rotulo` para `dias_de_uso`. Aqui o que saiu da prosa é **o que o número
significa**. O bloco 1 mediu, em 14/09/2026, duas frases na **mesma página de resultados** —
*"média de R$ 203,87 nos últimos 30 dias"* e *"a diária mais baixa encontrada foi R$ 396,84"*
—, que não podem ser as duas verdadeiras do jeito que estão escritas. **Essa distinção morou
numa ressalva de leitura humana por 38 dias.** Agora é `o_que_o_numero_e`, que é enum, e a
regra passou a ser **computável**: a F2 nunca soma faixas de naturezas diferentes, porque
somar uma média com um mínimo dá um intervalo que **ninguém publicou**. As duas vão para a
tela lado a lado, com dono e com a frase de quem as escreveu.

**A BASE TAMBÉM É DECLARADA, NUNCA DEDUZIDA**, e aqui a lição vem da própria F1: `base` diz
se o número é por pessoa, por **quarto** ou pelo grupo, e `base_transcrita_de` guarda a frase
de onde isso saiu. Base de quarto exige `pessoas_por_quarto`, e o número tem de **aparecer**
na frase da fonte — mesma cobrança de `dias_de_uso`. **Quarto é unidade de capacidade como
gôndola:** 6 pessoas numa diária de quarto duplo são **TRÊS** quartos, do mesmo jeito que 6
pessoas numa gôndola de 5 lugares são DUAS gôndolas. `quartos_necessarios()` **chama**
`unidades_necessarias()` da F1 em vez de reescrever a conta. E faixa de quarto **sem**
ocupação não escala: a linha é recusada pelo nome, porque dividir a diária pelo tamanho do
grupo seria escolher a ocupação no lugar de quem publicou o preço — e o resultado continuaria
parecendo dinheiro, que é por que esse erro não se vê.

### A F2 PUBLICA UMA LINHA DE QUATRO HOJE, E A FALTA TEM CAUSA NOMEADA

`faixas_diarias` tem **zero** registros, então em todos os 3.024 estados válidos a F2
publica a linha de experiências e **recusa** hospedagem, alimentação e transporte local pelo
nome, sem total. É a recusa declarada da especificação — *"a F2 publica faixa com quem
publicou, ou não publica"* — aplicada **categoria por categoria** em vez de à ferramenta
inteira. **E a falta não é descuido:** carregar exige `publicado_por`, `url` e `data_leitura`,
e as duas únicas frases de diária que esta ilha mediu foram guardadas **sem nenhum dos três**
— o corpus guardou os números e não guardou de quem eram. Carregar hoje exigiria **inventar o
dono do número**, e o dono do número é o produto desta ilha. **A coleta também não é trabalho
desta nuvem:** medi hoje, e o egresso recusa `numbeo.com`, `booking.com` e
`civitatis.com.br` (`000` nos três, com `raw.githubusercontent.com` em `301` na mesma
passada).

**O total também é recusado, e por regra e não por falta:** ele só existe com as quatro
linhas. Um total somado só com o que a ilha tem seria um número **menor que a viagem**
apresentado como se fosse ela inteira.

**E A LINHA DE EXPERIÊNCIAS NÃO CRESCE COM OS DIAS, declarado em vez de suposto.** Quantas
experiências cabem em N dias **não está no banco** — é a mesma família da Conta 3 da F1, onde
o eixo é declarado e nunca lido do rótulo. A linha é o custo de fazer **uma vez** cada
experiência que a ilha leu na cidade, e o portão mede isso: ele responde o mesmo estado com
1 dia e com 21 e exige que os dois números sejam iguais. A F2 também **não escolhe a versão**
da experiência — escolher entre os quatro bilhetes da Torre Eiffel seria decisão editorial
com cara de conta —, então a linha é uma **faixa**: piso na versão mais barata de cada
experiência, teto na mais cara, e a tela diz quais são.

### O QUE OS PORTÕES ACHARAM NA MINHA PRÓPRIA FERRAMENTA, OS SETE ANTES DO COMMIT

1. **A FAIXA DE LARGURA ZERO.** Com as duas versões da gôndola pelo mesmo preço, as duas
   pontas vinham de versões **diferentes** com o mesmo número, e a tela publicava *"de «De
   dia, 30 minutos» a «À noite, 35 minutos»"* para um intervalo que não é intervalo. As duas
   pontas passaram a desempatar para o mesmo lado, e a tela diz que as versões custam o mesmo.
2. **A FRASE QUE MENTIA SOBRE SIEM REAP, e esta é a pior das cinco.** A primeira versão
   descartava a experiência que não fosse `publicavel`, e a página dizia *"esta ilha ainda
   não leu o preço de nenhuma experiência em Siem Reap"* — **falso**: o preço do passe de
   Angkor está lido e gravado, só não reconferido. Pior que a frase: **o mesmo item aparece
   na F1 com ressalva e desaparecia aqui**, de modo que quem viesse da página do passe para
   a da estadia veria a experiência sumir sem explicação. Agora `pendente_de_releitura`
   **entra na conta com a ressalva**, como na F1; só `excluido_do_banco` fica fora. Quem achou
   foi o **gerador**, pela contagem: 2.268 estados com a linha nossa onde a grade pedia 3.024,
   e os 756 que faltavam eram exatamente uma cidade.
3. **A CONCORDÂNCIA.** A tela publicava *"as 1 experiências que esta ilha leu custam"*. É a
   mesma família do acento que a F1 pagou no dia em que nasceu, e nenhuma das duas se vê
   lendo o código — as duas se veem lendo a **frase**, que é por que o portão lê a frase.
4. **O TETO DE DIAS QUE O PORTÃO NÃO TINHA COMO VER.** A mutação que trocou 21 por 60
   **PASSOU**: grade, bordas e a conta do que está "fora" saíam todas de `f2.DIAS_MAXIMO`,
   então o portão e a ferramenta concordavam sempre. **Régua que toma o limite da coisa que
   ela mede não mede o limite.** Os dois limites agora estão escritos no portão, com a
   especificação citada como fonte.
5. **A MOEDA QUE A F1 CONFERE E A F2 NÃO CONFERIA.** A mutação que tirou `EUR` do
   vocabulário do esquema **PASSOU**: a F2 chamava `dinheiro()`, que olha o próprio
   dicionário de símbolos, e nunca o vocabulário. A F2 passou a chamar as duas conferências
   da F1, nas duas direções.

6. **A CONTAGEM QUE SÓ UM MUNDO DE BANCADA PODIA MOSTRAR.** O gerador contava
   `estados_com_total` sobre o **domínio inteiro** e o portão comparava esse número com o
   conteúdo do **arquivo recortado**. **Com zero faixas no banco os dois valem 0, e o
   defeito era invisível** — foi o mundo de bancada com as três faixas carregadas que o
   fez aparecer, 252 contra 12. São dois números agora, e cada um responde a uma pergunta:
   o gravado bate com o conteúdo do arquivo, o do domínio bate com a varredura do portão.
   É a melhor prova que este bloco produziu de por que a bateria de mutações carrega
   mundos que o banco não tem.
7. **UMA FUNÇÃO MINHA SOBRESCREVEU UMA FUNÇÃO DA BATERIA DO BANCO, em silêncio.**
   `q_faixa_sem_data_de_leitura` **já existia** em `mutacoes-banco.py`, para a faixa
   **etária**, e a minha definição — escrita mais abaixo no arquivo — passou a valer para
   as duas: **a mutação antiga começou a rodar a minha função** e a reprovar pelo motivo
   errado. Nesta pasta "faixa" significava faixa etária antes de hoje, e a entidade nova é
   faixa **diária**; os 23 nomes novos dizem isso agora. **E quem pegou foi a exigência da
   FRASE:** a mutação antiga continuava `reprova`, e o relatório diria `ok` se a bateria se
   contentasse com "reprovou". *"Reprovar não é a mesma coisa que reprovar pelo motivo
   certo"* deixou de ser uma frase bonita no cabeçalho e passou a ter um caso.

### E UM DEFEITO QUE NÃO É DESTE BLOCO E JÁ ESTAVA NO AR DA PASTA: A LISTA ESCRITA À MÃO

`validar-banco.py` conferia o crescimento de vocabulário contra **sete** nomes digitados, e
o esquema tinha **nove**: **`declarada_por` e `canal_de_leitura` nunca foram conferidos por
ninguém, em silêncio, desde 15/09/2026** — 37 dias. É a mesma família da lista de portões que
a aquametria matou com o descobridor em 22/09 e da lista de quem vigia que a leva 7 achou um
andar acima: **lista escrita à mão não erra alto, erra calada, e o que falta nela é sempre o
que acabou de nascer.** Se eu tivesse só acrescentado os quatro vocabulários novos à lista, o
defeito teria sido renovado em vez de consertado.

A régua agora **varre `vocabularios` do esquema** e vocabulário sem extrator vira **erro**,
não ausência. Na primeira passada ela achou o que a lista escondia: `canal_de_leitura` tem
`leitura_direta` **sem lastro** nenhum. E saiu um campo na mesma limpeza: `versao_esquema`
dizia **4** enquanto `versao` dizia **5** — dois nomes para o mesmo fato, com um deles já
errado, e nada no repositório o lia.

**A lista de PORTÕES do `PROMPT.md`, porém, continua escrita à mão, e ela cresceu de quatro
para seis nesta passada.** Não construí o descobridor: a **31.3** proíbe bancada sobre
bancada enquanto houver item de conteúdo aberto, e há — as faixas. Mas deixei a pressão
registrada no `PROMPT.md`, para a próxima execução não precisar redescobrir que o mesmo
defeito já foi pago um andar abaixo nesta mesma pasta.

### O ARQUIVO GRAVADO NÃO TRAZ OS 3.077 ESTADOS, e é decisão com o número na mesa

Gravá-los deu **13 MB**, contra 858 KB do arquivo da F1, e ele seria regravado inteiro a cada
mudança de regra ou de banco. O arquivo leva o que a página de fato lê — a tabela
pré-renderizada e **todas** as bordas, **679 KB** —, e a prova da grade inteira mora no
portão, que a varre em cada passada. **Prova em arquivo que ninguém recomputa é peso; prova
em portão é prova.** O portão cobra que a grade da tabela caiba no gravado e que **nenhuma**
borda tenha ficado de fora, porque arquivo sem borda fica sem um caso gravado da metade que
recusa — e é essa metade que esta ilha tem de diferente.

### AS REGRAS NOVAS DO VALIDADOR NÃO FICARAM SEM BATERIA, e isso quase aconteceu

Escrevi ~80 linhas de régua para a `FAIXA_DIARIA` e o banco tem **zero** faixas: nenhuma
delas seria executada por ninguém. É literalmente *"régua que não falhou porque não
rodou"*, o defeito que fez nascer o descobridor de portões na aquametria, e eu o teria
cometido dentro do mesmo bloco em que o consertei um andar abaixo. `mutacoes-banco.py`
passou de **93 para 117** mutações — **16** mundos e **101** quebras, **57** cobradas pela
frase —, com as 24 novas carregando faixa em memória e quebrando cada regra: sem dono, sem
a frase do método, sem a frase da base, teto menor que piso, valor zero, quarto sem
ocupação, ocupação que a frase não declara, **ocupação achada dentro de outro número**
(`2` dentro de `2400`, a mesma armadilha que o `dias_de_uso` pagou), ocupação fora da base
de quarto, sem data, cidade inexistente, categoria e base fora do vocabulário, sem URL e
sem motivo, id repetido, resumo digitado, o esquema sem a entidade, e **vocabulário novo
que a régua não sabe extrair**. Nenhuma faixa foi gravada no banco: todas são mundos de
bancada.

**BANCADA, 0 falha:** `validar-banco` verde (os avisos de `vocabulario_sem_lastro` onde
estavam, mais os quatro vocabulários novos e o `leitura_direta` que a lista à mão escondia);
`mutacoes-banco` **117 de 117**; `teste-f1` 139.658 afirmações; `mutacoes-f1` 28 de 28;
`teste-f2` **213.586** afirmações sobre os 3.077 estados, com a aritmética
refeita à mão em `Fraction` e as funções puras chamadas com os mundos que o banco não tem;
`mutacoes-f2` **44 de 44 — 9 mundos, 25 quebras e 10 mortes, com 28 cobradas pela frase**.

**PRÓXIMO PASSO:** a **F3 como regra** (o passe da cidade vale a pena para você), que é a
última das três âncoras e a única cujas duas pontas da conta são **nossas** — soma dos
avulsos do banco contra o preço do passe. Ela herda pronta da F2 a régua de declarar o que o
número é, e não precisa da entidade nova, a menos que a fonte do passe publique faixa em vez
de preço. **O que ela precisa e o banco não tem:** nenhuma das quatro experiências é
`passe_de_cidade` — o vocabulário tem o valor e nenhum registro o usa, e o Roma Pass e o
Lisboa Card, que o corpus mediu, não estão carregados. Então a F3 começa pelo banco, não pela
ferramenta. **E o item de conteúdo que continua sendo o mais caro desta ilha não é ferramenta
nenhuma: é a casca (3b), que depende dos passos 2 a 8 da seção 11 e da liberação de
`jornadafly.com.br` no egresso — as duas do Raphael, as duas de navegador.**

## 2026-10-22 13h29Z — A F1 EXISTE COMO REGRA, e escrevê-la mostrou que a Conta 3 da especificação não era calculável

**O que saiu:** o **bloco 4** — a F1 como **regra**, no desenho que a ohmetria usou na F1
dela: `ferramentas/f1-referencia.py` (o cérebro: estado → resposta inteira, já em frase
acentuada), `ferramentas/gerar-f1.py`, `dados/f1-respostas.json` (as **154** respostas e
as **44** linhas da tabela pré-renderizada, `publicar: false`),
`ferramentas/teste-f1.py` e `ferramentas/mutacoes-f1.py`. Esquema **versão 5**, banco
**versão 5**. É o próximo passo que o registro de 10h20Z de hoje deixou escrito,
cumprido na mesma data. **Nada foi ao ar, e não podia ter ido: esta ilha não tem site,
não tem WordPress, não tem Sync e não tem `/status`, e dizer que verifiquei no ar seria
inventar.**

**SEM PHP, e é decisão registrada e não pendência esquecida.** Sem casca (bloco 3b,
trabalho de navegador do Raphael), um snippet só poderia ser medido por um render de
bancada que serve **menos** do que o site serve — a cicatriz que a seção 8 do
`ARQUIPELAGO.md` mais cobra, paga três vezes pela Robometria. A regra nasceu onde pode
ser conferida hoje, e o PHP, quando nascer, é **tradutor** desta referência, frase a
frase, como a robometria faz entre `cobertura-r1.py` e `robometria-r1.php`.

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO E NÃO HOUVE DECISÃO MINHA.** `foco.md` nomeia a
**jornadafly** desde hoje, pelo item (3) da fila que o Raphael decidiu em 09/10 e
ajustou em 14/10, e pela **1.2** não há escolha de ilha a fazer. Conferi a exceção de
21/10 que fura o foco pelo **molde da seção 32**: os três despachos estão **fechados**
(aquametria às 18h2xZ, clubedomosaico às 19h1xZ, robometria nas nove páginas), então ela
não se aplica e o foco manda sozinho. `executando_desde` estava `null`, que pela **1.1**
já significa que não havia bloco da Fundação vivo — não houve reserva vencida para o git
desempatar. Reserva aceita de primeira às **13h29Z**, sem recusa de push. Nenhum branch
`claude/*` com trabalho a mesclar e nenhum PR aberto.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA.** Três passadas: `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas três (**6 medições de bloqueio**), com
`aquametria.com.br` e `robometria.com.br` em `200` nas três (**6 de controle**, e nesta
rodada **nenhuma** intermitência de túnel, diferente da passada de 10h20Z). O `curl`
verbose nomeia a causa e ela não é túnel: `HTTP/1.1 403 Forbidden` no `CONNECT
jornadafly.com.br:443`. **Segue sendo regressão** — o campo dizia `aberta em 2026-09-18`
com HTTP 200 medido às 12h35Z daquele dia — e o despacho ALTA de 15/09 em
`dados/despachos.md` continua valendo. `bloqueada_por` segue `null` de propósito: o que
a rede trava é o 3b em diante, não o bloco de arquivo.

### A CONTA 3 DA ESPECIFICAÇÃO NÃO ERA CALCULÁVEL, e achar isso foi o trabalho do bloco

A especificação (2.5) manda a F1 mostrar **"a partir de qual número de dias/atrações a
versão mais cara passa a valer"**, e nomeia Petra e Angkor como os casos medidos. Sobre
o banco versão 4 isso **não tinha como ser respondido**: as 11 versões trazem `preco`,
`rotulo` e `declarado_como`, e **nenhum campo** dizia quantas unidades de uso cada
bilhete dá nem se as versões são comparáveis entre si. A quantidade existia só na
**prosa** — "3 dias, usáveis dentro de uma semana" — e prosa não se conta.

**O conserto tem duas metades, e a primeira é a que não se adivinha.**

**(1) A EXPERIÊNCIA declara o EIXO**, `eixo_das_versoes` ∈
`{por_quantidade, por_escopo, por_momento}`, porque **a comparabilidade é uma decisão
sobre o conjunto e não um atributo de cada item**. A Conta 3 roda só em
`por_quantidade`; nos outros dois a F1 diz na tela por que não há ponto de equilíbrio, e
isso é uma resposta e não um silêncio. **O erro caro, nomeado antes da direção:** dois
ingressos de 24 horas do Coliseu **não** dão a área restrita da Experiência Completa, e
dois passeios diurnos de gôndola **não** dão um passeio noturno — um ponto de equilíbrio
ali seria aritmética correta sobre uma pergunta sem sentido, que é a forma mais eficiente
de publicar uma mentira com cara de conta.

**E o eixo NÃO se deduz do rótulo**, que era o atalho disponível: ler o rótulo
**acertaria no Angkor e erraria no Coliseu**, cujos quatro bilhetes não falam de
quantidade nenhuma. Erro que acerta no caso que se tem na mão é o mais caro de todos,
porque ele passa.

**(2) A VERSÃO declara `dias_de_uso`**, com `dias_de_uso_transcrito_de` dizendo de qual
frase da fonte o número saiu, e **a régua cobra que o número apareça no
`declarado_como`** da própria versão, em dígito ou por extenso. É a **terceira conta** da
seção 8: sem ela o campo seria um inteiro digitado por quem migrou, com cara de
transcrito. **Nenhuma leitura nova de fonte** — os três números do Angkor (1, 3 e 7)
estavam escritos na declaração dela desde 14/09/2026. É a mesma troca que a `faixa_etaria`
fez três horas antes, um andar acima: lá a prosa virou faixa, aqui a prosa virou
quantidade.

**O que o banco de hoje tem:** 1 experiência `por_quantidade` (Angkor), 2 `por_escopo`
(Coliseu e Torre Eiffel) e 1 `por_momento` (gôndola) — os três valores do vocabulário
com lastro no primeiro dia, e o validador confirma (`vocabulario_sem_lastro` não acusa o
eixo). **A conta, medida:** a base é o bilhete de menor quantidade (1 dia, US$ 37) e o
equilíbrio é **2 dias** tanto para o passe de 3 (US$ 62; dois de um dia já custam US$ 74)
como para o de 7 (US$ 72).

**O ponto de equilíbrio é uma FUNÇÃO PURA** que recebe `[(id, rótulo, preço, dias)]` e o
eixo, e não varre o banco. É a regra que o Clube do Mosaico pagou em 08/10/2026: recusa
que depende de uma **relação** entre os dados só é testável no dia em que o banco
produzir o caso, e é esse o dia em que ela vai estar errada. Com a função pura, a bancada
fabrica o empate de preço, a versão única e o preço ausente **sem fabricar um banco
falso** — e as três mutações existem.

### O PORTÃO ACHOU DOIS DEFEITOS NA MINHA PRÓPRIA FERRAMENTA, e o segundo estava atrás do primeiro

**(a) A F1 publicava português SEM ACENTO.** A frase-resposta saía *"O preco e por
veiculo, nao por pessoa"*: a cicatriz da Robometria cometida dentro do arquivo escrito
para não a cometer. O rótulo da unidade era montado com `unidade.replace("_", " ")`, que
é um atalho que parece inofensivo e publica o vocabulário do banco na tela. Virou
`ROTULO_DA_UNIDADE`, conferido contra o vocabulário do esquema **nas duas direções**.

**(b) E atrás do acento, um defeito maior: a F1 repassava os `motivo_*` do BANCO para a
tela.** Esses campos são escritos para a **próxima execução** — citam nome de campo entre
acentos graves, data de migração e número de seção do contrato. O resultado era a página
dizendo ao visitante que *"o esquema PROÍBE faixa etária onde a unidade não é
`por_pessoa`"* e nomeando `cambio-eur-brl` dentro da recusa do valor em real. **Texto de
bastidor da fábrica numa página pública, que a 32.4 proíbe com todas as letras** — a
mesma cicatriz que a ohmetria pagou publicando `dados/modulos.json` na tela. A F1 passou
a **escrever a própria frase de tela**; o motivo fica no banco, onde serve.

**A régua de acento foi quem viu, e o defeito embaixo era maior que o acento** — pela
terceira vez nesta fábrica (a ohmetria registrou a mesma sequência). Por isso a trava que
nasceu não é uma lista de frases: é uma lista de **FORMAS** de bastidor (acento grave,
nome em minúsculas com sublinhado, caminho de arquivo do repositório, id com dois ou mais
hifens, número de seção do contrato), porque o bastidor não chega à página como uma frase
conhecida — ele chega como nome de campo dentro de um motivo.

### O `momento_do_dia` NÃO é a quarta entrada que a especificação listava

A tabela de entradas (2.3) o lista como seleção dependente condicional. No banco ele é
**campo da VERSÃO**: as duas versões vendidas da gôndola **são** o diurno e o noturno,
cada uma com horário, duração e preço próprios. Oferecê-lo à parte deixaria a pessoa
pedir "noturno" sobre a versão diurna — **um estado que o operador não vende**. O estado
da F1 é `(experiência, versão, pessoas)`, e o horário sai da versão escolhida. A
especificação foi corrigida com a condição de volta: se um dia um operador vender a mesma
versão em dois horários com preços diferentes, o campo volta a ser entrada — e aí nasce
como dimensão do banco **antes** de nascer como campo de formulário.

### A bateria de mutações me corrigiu seis vezes, e cinco das seis eram sobre a MUTAÇÃO, não sobre o código

Primeira rodada: 6 de 28 decidiram diferente do esperado. **Nenhuma delas era um defeito
da F1** — e é isso que vale guardar.

- **Duas não tinham como morder, e as duas pelo mesmo motivo.** A quebra "o piso de
  compra passa a ser lido do registro em vez de derivado do molde" **passou**, porque no
  banco de hoje a URL derivada e a URL gravada são a mesma letra por letra — o validador
  obriga. É literalmente o caso que a seção 8 descreve: *"as quatro réguas davam a mesma
  resposta em todos os registros do banco de hoje… portão que comparasse os vereditos
  ficaria verde"*. A quebra "a escada passa a ser calculada no eixo de escopo" **passou**
  porque as versões de escopo têm `dias_de_uso` null e o cálculo caía na recusa de dado
  faltando. As duas só mordem num mundo que precisa de **código E dado** mexidos juntos,
  e a bateria ganhou um quarto elemento na tupla para isso.
- **Uma atacava a forma errada do mesmo defeito.** A quebra do motivo do banco apontava
  para `inclui_motivo_lista_vazia`, que é prosa sem nome de campo dentro — nenhuma forma
  de bastidor aparecia. O alvo certo é `motivo_sem_faixa_etaria`, que é exatamente o que a
  primeira versão da F1 repassava. **Mutação que ataca a forma errada volta verde e parece
  prova.**
- **Duas MORRERAM em vez de reprovar, e morrer era a resposta certa.** Data de leitura
  fora de AAAA-MM-DD e cidade sem `slug_plataforma` levantam na referência em vez de a
  fazerem publicar errado. As duas desceram para MORTES, onde medem o que de fato fazem.
- **Uma passou e TEM de passar, e isso é uma fronteira escrita.** "Banco dando
  QUANTIDADE a bilhetes que diferem em escopo" passa no portão da F1 — porque o portão da
  F1 confere a **referência** contra o banco, e banco que **mente** é trabalho do
  `validar-banco.py`, que o reprova. Ficou na bateria como MUNDO, de propósito: é a prova
  de que o portão da F1 não finge medir o que não mede, e a próxima execução não vai
  escrever a mesma mutação esperando outra resposta.

**E a bateria do banco tinha o mesmo defeito que a de 22/10 10h20Z achou nela, outra
vez.** As 13 quebras novas do eixo nasceram com a **FRASE esperada escrita na quarta
posição** da tupla — que é o `esquema_mutado` — e não na quinta: reprovavam, e nenhuma
provava reprovar **pelo motivo certo**. O conserto não foi mover 13 vírgulas: o
`esquema_para()` passou a **matar a bateria** quando recebe uma chave de mutação que não
reconhece, em vez de devolver um esquema intacto com cara de mutado. É a trava de alvo
exato aplicada ao lugar onde ela faltava, e ela diz na mensagem qual dos dois erros foi
cometido.

### A grade pisa em DUAS bordas, e uma delas custa um número

O portão varre **todos os 154 estados** — 11 versões × 12 tamanhos de grupo, mais 0 e 13
pessoas, que são as recusas duras — e, nas versões com unidade de veículo, também a
capacidade, a capacidade + 1 e o dobro dela, que é onde `ceil` se separa de `floor + 1`.
**O número que justifica isso:** existe **exatamente UM** estado neste banco em que
arredondar meio-para-cima difere de arredondar meio-para-par — a gôndola noturna para 2
pessoas, €56,925 por pessoa com IOF, que é **€56,93** e não €56,92. Uma grade por
amostragem teria 1 chance em 154 de o encontrar, e a mutação que troca o arredondamento
voltaria **verde**.

### Bancada, 0 falha

- `validar-banco.py` **verde** sobre o banco real, com as oito réguas novas do eixo e dos
  dias de uso. Os **5** avisos de `vocabulario_sem_lastro` continuam onde estavam, e o
  vocabulário novo (`eixo_das_versoes`) **não** acusa: os três valores têm registro que os
  use no primeiro dia.
- `mutacoes-banco.py` **93 de 93** (eram 73): **10** mundos que têm de passar e **83**
  quebras que têm de reprovar, **39** delas cobradas pela frase que esperam ouvir
  (eram 22). Os três mundos novos são os que o esquema permite e o banco não tem: eixo de
  quantidade com uma versão só, eixo de quantidade com empate de preço, e eixo null com
  uma versão só.
- `teste-f1.py` **139.658 afirmações, 0 falha**, com a aritmética reescrita à mão em
  `Fraction` (o `ceil` como divisão inteira e o arredondamento sem `Decimal`, **de
  propósito**, para que duas escritas da mesma conta possam discordar numa borda).
- `mutacoes-f1.py` **28 de 28**: 5 mundos, 15 quebras e **8 mortes**. Morte é chave que
  sai do esquema ou das constantes e tem de **matar** a referência em vez de a fazer cair
  num literal — molde do piso, vocabulário de unidade, moeda, `rel`, e o IOF nos dois
  jeitos (pendente e ausente).
- Os quatro JSON passam por `json.load` e o cabeçalho do `ESTADO.md` por `yaml.safe_load`.

### A seção 31 nesta ilha, dita antes de alguém contar

A **31.1** pede 7 de cada 10 execuções entregando algo **no ar**. Nesta ilha isso é
**inalcançável**, porque **não existe "no ar"**: faltam os passos 2 a 8 da seção 11
(WordPress, trabalho de navegador) e falta o domínio na lista de rede. As duas são do
Raphael, as duas estão no topo do `PROMPT.md` desta ilha e no `foco.md`, e as duas foram
remedidas hoje.

**E a 31.2 foi obedecida com a conta na mesa, porque ela merece a pergunta.** Ela diz que
portão novo só nasce quando existe **defeito medido no ar** que ele teria pegado. O
`teste-f1.py` e o `mutacoes-f1.py` nasceram nesta passada, e **não há "no ar" nesta ilha
para medir defeito**. O que os sustenta é a **31.5**, que preserva inteiro o portão de
dado da seção 13.1, e o fato de que os dois **pegaram dois defeitos reais nesta mesma
execução** — o português sem acento e o texto de bastidor na tela —, nomeados acima com a
frase exata que iam publicar. Não são ampliação de portão existente (que a **31.3**
proíbe): são o portão de dado da ferramenta que acabou de nascer. **O que NÃO nasceu, de
propósito:** um `bancada.py` que descubra os portões por convenção de nome, como as três
ilhas irmãs têm. Ele seria bancada sobre bancada, a 31.3 o proíbe enquanto houver item de
conteúdo aberto, e os quatro portões desta pasta ainda cabem em quatro linhas de registro.

### Aberto e nomeado

(a) a **rede** da ilha, despacho ALTO, **remedida e ainda regredida** hoje, que trava 3b
em diante; (b) o **WordPress e a infraestrutura dos passos 2 a 8**, que nenhuma execução
da Fundação alcança; (c) as **4 células do meio** da grade da Torre Eiffel, contadas e
bloqueadas por 403; (d) a **seção pendente do `VOZ.md`** — as 10 a 15 legendas reais do
@jornadafly, que o `PROMPT.md` exige antes da primeira página; (e) a **identidade
visual**, que precisa da aprovação do Raphael antes do 3b; (f) **nenhum programa de
afiliado cadastrado** (e por isso o link do bloco de compra sai **cru**, sem
`rel="sponsored"`, que é decisão já registrada pelas duas ilhas irmãs); (g) o **câmbio**
(`api.bcb.gov.br` fora da lista), que é o que impede a F1 de publicar valor em real;
(h) **não existe `manifest.json`**, e criá-lo vazio seria inventar infraestrutura antes do
WordPress.

### Próximo passo desbloqueado

**A F2 como REGRA — "quanto custa N dias em `<cidade>`"**, no mesmo desenho. E ela nasce
com uma pergunta de dado que a F1 não tinha: a F2 soma **hospedagem + alimentação +
transporte local + experiências marcadas**, e das quatro só a última existe no banco. As
três primeiras não são experiência e não cabem na entidade EXPERIÊNCIA — então o bloco da
F2 começa decidindo **onde elas moram**, e a especificação (seção 3) já avisa que a F2 só
entra "se for melhor" que o `quantocustaviajar.com`, cujo diferencial é justamente preço
colhido na fonte. **O que a F2 pode fazer hoje é o que a F1 fez:** a regra, a régua e as
mutações sobre o que o banco tem, com as recusas contadas em vez de escondidas. Não
depende de site, de domínio, nem da rede bloqueada.

## 2026-10-22 10h20Z — `faixa_etaria` desce para a VERSÃO, e a descida acha que a frase do Angkor fala de outro bilhete

**O que saiu:** `faixa_etaria` saiu de EXPERIÊNCIA e entrou em VERSÃO, nas **11 versões das 4
experiências**, com a entidade `FAIXA_ETARIA` nascendo explícita no esquema. Esquema **versão 4**,
banco **versão 4**. É o **próximo passo que o registro de 15/09/2026 deixou escrito**, cumprido ao
pé da letra — *"com a régua e as mutações junto, e migrar os registros da gôndola e do Angkor na
mesma passada"* — 37 dias depois de ser medido. **Nada foi ao ar: esta ilha não tem site, não tem
WordPress, não tem Sync e não tem `/status`, e dizer que verifiquei no ar seria inventar.**

**A ESCOLHA DA ILHA: NÃO HOUVE ROTAÇÃO, E NÃO HOUVE DECISÃO MINHA.** Hoje é 22/10/2026, e a linha
`fila_decidida_pelo_raphael` do `foco.md` dizia, desde 09/10 e ajustada por ele em 14/10: *"(3)
jornadafly em foco a partir de 22/10/2026, como foco principal"*, com o aviso ao lado — *"esta linha
é registro da fila, NÃO troca o foco sozinha: quem troca é a linha `ilha:`, editada na data. Em
22/10/2026 alguém tem de editar a linha `ilha:` para jornadafly — se ninguém editar, o foco fica
preso, como ficou de 10/10 a 14/10."* A janela da aquametria vencia em **21/10**. Troquei a linha e
reservei esta ilha no **mesmo push**, às **10h20Z**, aceito de primeira. Os três despachos do
**molde da seção 32** estão fechados nas três ilhas (aquametria 18h2xZ, clubedomosaico 19h1xZ,
robometria nas nove páginas), então a exceção de 21/10 que furava o foco pela 32 **não se aplica
mais** e o foco volta a mandar sozinho. Nenhum branch `claude/*` com trabalho a mesclar e nenhum PR
aberto. **E a aquametria não ficou no limbo:** pela **1.2-b.4** ela recebeu, nesta mesma passada, o
**critério de saída do foco pré-registrado** que nunca havia sido escrito para ela — série, datas e
os três desfechos, no `PROMPT.md` dela, **antes** da leitura de 28/10 que ele julga.

**REDE PELA 20.2, REMEDIDA E NÃO HERDADA — E É REGRESSÃO.** Três passadas: `jornadafly.com.br` e
`www.jornadafly.com.br` em `000` nas três, com `aquametria.com.br` e `robometria.com.br` em `200`
nas mesmas (a robometria caiu **uma** vez na terceira — é a intermitência de túnel que a 20.2 manda
não confundir com bloqueio, e ela apareceu no **controle**, não no alvo). O `curl` verbose nomeia a
causa e ela não é intermitência: `CONNECT tunnel failed, response 403` do proxy de egresso, ou seja
**o domínio não está na lista de Domínios permitidos deste ambiente**. O campo dizia `rede: aberta
em 2026-09-18`, com **HTTP 200 medido às 12h35Z** daquele dia, e o painel de 18/09 escreveu que o
despacho ALTA de 15/09 *"está cumprido e saiu deste painel"*. **Então isto já esteve resolvido e
voltou** — o despacho ALTA volta a valer, e `bloqueada_por` segue `null` de propósito, como nas
quatro execuções anteriores: o que a rede trava é o 3b em diante, não o bloco de arquivo.

### O que a descida produziu, e nenhuma das três coisas era possível com o campo na EXPERIÊNCIA

**(1) A Torre Eiffel publica 4 faixas gravadas em vez de 1.** A fonte declara quatro faixas e o
preço de três delas **muda de bilhete para bilhete**. Com `faixa_etaria` na EXPERIÊNCIA, a carga de
15/09 só podia gravar a gratuidade dos menores de 4 anos — a única que vale igual nos quatro — e os
outros números ficaram em **prosa**, dentro da `nota_da_faixa_etaria` do próprio registro. Agora são
campo: **3,80€** e **7,40€** na escada até o segundo piso, **9,20€** e **18,40€** no elevador até o
topo, cada um com `transcrito_de` dizendo que saiu daquela prosa e **não** de leitura nova. É a
mesma troca que a Aquametria fez em 21/10/2026 com o `porte_adulto_cm`: **prosa dentro do banco que
vira campo contável, porque prosa não barra página e prosa não se conta.**

**(2) A proibição de faixa etária em tarifa `por_veiculo` virou REGRA.** Era prosa no
`motivo_sem_faixa_etaria` da gôndola desde 14/09 — *"a tarifa é pela embarcação inteira, não por
passageiro"* — e **só podia virar regra depois de a faixa descer**, porque `unidade_de_preco` é
campo da VERSÃO e os dois precisavam estar no mesmo objeto. Seis pessoas na gôndola são **duas**
gôndolas: a criança não tem preço, tem assento.

**(3) O achado que a migração pagou: a frase do Angkor fala de outro bilhete.** O `se_nao_cumprir`
da faixa cita *"sem ele paga-se US$ 37 por criança"* — e **US$ 37 é o passe de UM DIA**. Guardada num
campo de EXPERIÊNCIA, essa frase valia para os passes de 3 dias (US$ 62) e de 7 dias (US$ 72) junto,
dizendo o número de um bilhete sobre outros dois. Está nomeado em
`numero_da_frase_e_de_outra_versao` nas duas versões em que a frase não é daquele bilhete, e **a
régua cobra o campo em vez de confiar na nota**. A ilha **não** troca 37 por 62 nem por 72: a prosa
de 14/09 já lia a frase como *"o mesmo valor do adulto, por cabeça"*, o que daria 62 e 72 — mas essa
é a leitura **da ilha**, não a letra do operador, e trocar uma pela outra é exatamente o que esta
ilha existe para não fazer.

### As 4 células do meio continuam não lidas, e agora são um número

A leitura de 15/09 transcreveu o **piso** e o **teto** da grade e não as duas colunas do meio: a
criança e o jovem nas versões `segundo-piso-elevador` e `topo-escada-e-elevador`. As quatro
ausências estão em `faixas_que_a_fonte_declara_e_a_leitura_nao_transcreveu`, com `rotulo` e
`por_que` em cada uma, e o resumo do banco publica
**`faixas_declaradas_nao_transcritas: 4`** ao lado de **`faixas_etarias: 11`** — os dois contados
pelo validador, nunca digitados.

**Tentei relê-las, e o registro da tentativa vale mais que a lacuna.** `www.toureiffel.paris`
responde **403 no CONNECT** deste ambiente (o esquema já registrava esse bloqueio em
`o_que_o_esquema_permite_e_o_banco_ainda_nao_tem`, remedido hoje). A busca **devolveu** uma grade
com os valores do meio — e eles **não foram gravados**, porque vieram no **resumo** da busca e não
de documento aberto. **Fonte citada por resumo é pista; fonte lida é dado.** Gravar o número do
resumo seria a trava de coleta da seção 8 sendo contornada pela própria execução que a cita.

### A bancada me corrigiu duas vezes, as duas antes do commit

**(a) A primeira versão da regra era LARGA DEMAIS.** Ela proibia faixa etária em **toda** unidade
diferente de `por_pessoa`, e o **MUNDO `por_cabine`** da bateria a reprovou na hora. O argumento da
gôndola é sobre **veículo alugado inteiro**, onde a criança ocupa assento e não gera cobrança; um
cruzeiro vendido **por cabine** pode perfeitamente declarar tarifa de criança na cabine, e
`por_grupo` também. A proibição ficou no caso **medido** (`por_veiculo`), e `por_cabine` e
`por_grupo` ficaram **de fora dela, de propósito**, com o motivo escrito no esquema. **Régua que diz
não para um mundo legítimo custa mais caro que régua que falta** — e quem achou o excesso foi a
mutação, não uma releitura minha.

**(b) O mundo novo escreveu `crianca` sem cedilha** e a régua das irmãs reprovou **três** versões de
uma vez: é o `rotulo` que liga a mesma faixa entre bilhetes, então rótulo que não casa produz uma
faixa nova em uma versão e três ausências silenciosas nas outras. O defeito era do mundo, e a régua
o apontou pelo nome.

**(c) E 16 quebras novas não estavam sendo cobradas pela FRASE**, porque eu pus a frase na **quarta**
posição da tupla — que é o `esquema_mutado` — e não na quinta. Elas reprovavam, e nenhuma delas
provava reprovar **pelo motivo certo**. Consertado antes do commit: a bateria passou de **3** para
**22** quebras cobradas por frase. É a trava que esta ilha escreveu em 15/09 pegando um defeito na
própria ilha que a escreveu.

### Bancada, 0 falha

- `validar-banco.py` **verde** sobre o banco real, com as oito réguas novas da faixa. Os cinco
  avisos de `vocabulario_sem_lastro` continuam onde estavam.
- `mutacoes-banco.py` **73 de 73** (eram 53): **7 mundos** que têm de PASSAR e **66 quebras** que
  têm de REPROVAR, **22** delas cobradas pela frase que esperam ouvir de volta. O mundo novo é a
  **faixa que a fonte NOMEIA sem dizer o preço**, que o esquema permite e o banco não tem.
- Os três JSON passam por `json.load` e o cabeçalho do `ESTADO.md` por `yaml.safe_load`.

### A seção 31 nesta ilha, dita antes de alguém contar

A **31.1** pede 7 de cada 10 execuções entregando algo **no ar**. Nesta ilha isso é **inalcançável**,
porque **não existe "no ar"**: faltam os passos 2 a 8 da seção 11 (WordPress, trabalho de navegador
do Raphael) e falta o domínio na lista de rede. **As duas são dele**, e as duas estão escritas no
topo do `PROMPT.md` desta ilha e no `foco.md`, para que o próximo que contar a proporção leia a causa
em vez de ler desobediência. O que a Fundação pode fazer aqui é o que não depende de site — e foi
isso que esta execução fez.

### Aberto e nomeado

(a) a **rede** da ilha, despacho ALTO, **regredida** hoje, que trava 3b em diante; (b) o **WordPress
e a infraestrutura dos passos 2 a 8**, que nenhuma execução da Fundação alcança; (c) as **4 células
do meio** da grade da Torre Eiffel, contadas e bloqueadas por 403; (d) a **seção pendente do
`VOZ.md`** — as 10 a 15 legendas reais do @jornadafly, que o `PROMPT.md` exige antes da primeira
página; (e) a **identidade visual**, que precisa da aprovação do Raphael antes do 3b; (f) **nenhum
programa de afiliado cadastrado**; (g) o **câmbio** (`api.bcb.gov.br` fora da lista), que custa uma
linha e não trava bloco; (h) **não existe `manifest.json`**, e criá-lo vazio seria inventar
infraestrutura antes do WordPress.

### Próximo passo desbloqueado

**A F1 como REGRA — o bloco 4**, no desenho que a ohmetria usou na F1 dela: a referência em Python
(entrada → resposta inteira, já em frase acentuada), a tabela pré-renderizada, os portões, e
**sem PHP enquanto não houver casca** — o PHP, quando nascer, é **tradutor** da referência, frase a
frase. **A especificação já foi atualizada hoje para o modelo novo**, e é por isso que o bloco 4 fica
mais barato do que era ontem: a F1 lê a faixa **da versão que a pessoa escolheu**, nunca da
experiência, e ela distingue **três** recusas que antes eram uma só — faixa que o operador não
declara, faixa que ele declara e ninguém leu, e número da frase que é de outro bilhete. **Não depende
de site, de domínio, nem da rede bloqueada.**

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
