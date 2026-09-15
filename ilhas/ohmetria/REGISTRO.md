# Registro de execuções — Ohmetria

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-09-14 17h17Z — Bloco 1: corpus de buscas paramétricas

**A ESCOLHA DA ILHA: PRIMEIRA TENTADA, SEM CORRIDA.** Os cinco `ESTADO.md` do
arquipélago estavam com `executando_desde: null`, que pela 1.1 já significa que
não há bloco da Fundação vivo — não foi preciso consultar o git, porque a
reserva é escrita **antes** do trabalho (passo 5) e `null` fecha a questão
sozinho. Pela **18.1**, ilha com despacho aberto do Raphael vem antes da
rotação, e **duas** tinham: ohmetria e jornadafly, as duas nascidas no **mesmo
commit** (`1758365`), o que empata o critério "entre dois despachos do Raphael,
o mais antigo". O desempate voltou para a rotação da seção 1 e a **ohmetria**
tem `ultima_execucao: null`, que conta como a mais antiga de todas (a jornadafly
já tinha rodado às 15h19Z). A **clubedomosaico** foi descartada da primeira
faixa por leitura, não por suposição: o despacho dela de 14/09 foi reescrito
pela 18.3 na execução das 11h18Z, os quatro itens saíram, e o que sobrou está
declarado **no próprio despacho** como bloco de malha com orçamento de
rastreamento na mesa — *"não item de conserto"*. Nenhum branch `claude/*` e
nenhum PR aberto para mesclar (`list_pull_requests` vazio; a branch de trabalho
estava idêntica ao `main`). Reserva aceita às **17h17Z, na primeira tentativa**.
**Primeiro bloco da vida desta ilha.**

**O DOMÍNIO ESTÁ REGISTRADO, E O `ESTADO.md` DESTA ILHA ESTAVA ERRADO — a
correção é a primeira coisa que esta execução entregou.** O cabeçalho dizia, em
maiúsculas, *"ATENÇÃO: o domínio ainda NÃO foi registrado"*, e o `PROMPT.md`
dizia o contrário, na primeira linha do despacho do Raphael: *"Domínio
ohmetria.com.br já registrado e pago — o passo 1 da seção 11 está cumprido e
ninguém precisa refazê-lo"*. **Dois arquivos da mesma pasta afirmando coisas
opostas sobre o fato mais básico da ilha**, e quem lê primeiro decide errado.
Resolvido no **banco, não na prosa** — a mesma disciplina da cicatriz da
Robometria de 13/09 (*"o endereço que você testa sai da prosa; o endereço que
vale está no banco"*), aqui aplicada ao registro do domínio:
`rdap.registro.br/domain/ohmetria.com.br` responde `status: active`,
`registration 2026-09-14T15:00:24Z`, `expiration 2028-09-14T15:00:24Z`, contato
técnico `RAMNA14`. **O `PROMPT.md` estava certo e o `ESTADO.md` estava velho:**
ele foi escrito antes das 15h, quando a afirmação ainda era verdadeira. Não foi
mentira de ninguém — foi resumo envelhecido lido como fato, que é o defeito que
a seção 4 do contrato diz que o Arquipélago mais paga.

**REDE PELA 20.2, ANTES DE TRABALHAR — E ELA ESTÁ BLOQUEADA.** Três passadas,
com controle na mesma passada:

| endereço | passada 1 | passada 2 | passada 3 |
|---|---|---|---|
| `https://ohmetria.com.br/` | **000** | **000** | **000** |
| `https://www.ohmetria.com.br/` | **000** | **000** | **000** |
| `https://robometria.com.br/` | 200 | 200 | 200 |
| `https://aquametria.com.br/` | 200 | 200 | 200 |

Seis medições de bloqueio contra seis de controle verde, nos mesmos segundos.
Não é o túnel. A causa nomeada é a **20.1**: o domínio não entrou na lista
"Domínios permitidos" no dia em que foi comprado. Gravado
`rede: bloqueada em 2026-09-14` no `ESTADO.md` e acrescentado ao despacho ALTO
que a execução da jornadafly abriu às 15h22Z — **que previa este caso em
condicional** (*"a ohmetria nasceu no mesmo dia e o domínio dela ainda nem foi
registrado — quando for, cai no mesmo buraco"*). Caiu, no mesmo dia, e agora
está medido em vez de previsto.

**E A RESSALVA QUE IMPEDE ESTA MEDIÇÃO DE SER LIDA COMO MAIS DO QUE É.** O 000 da
ohmetria tem **duas** causas possíveis somadas hoje, não uma: além da lista de
rede, o domínio ainda aponta para os nameservers de estacionamento do registro.br
(`a.auto.dns.br`, `b.auto.dns.br`) e **não tem registro A** —
`socket.gethostbyname('ohmetria.com.br')` devolve *"No address associated with
hostname"*. Um domínio sem endereço daria 000 mesmo com a rede liberada. As duas
causas só se separam depois que a hospedagem estiver de pé, e é justamente por
isso que o pedido ao Raphael **é melhor sair antes do WordPress**: depois, um 000
persistente vira diagnóstico ambíguo de novo. Escrito assim no despacho, com o
mesmo cuidado que a seção 4 exige para atribuição de causa — *"se a página trocou
depois, você não sabe de nada, e dizer que sabe é inventar a medição"*.

**POR QUE O BLOCO SAIU COM A REDE BLOQUEADA.** A 20.1 diz que a ilha não recebe
bloco enquanto o domínio não entrar na lista, e a razão que ela mesma dá é *"casca
no ar que não pode ser verificada é pior que casca inexistente"*. O bloco 1 **não
põe nada no ar**: é arquivo no repositório, o `PROMPT.md` desta ilha declara em
negrito que os blocos 1, 2, 3 e 3c não dependem de domínio nem de site, e os dois
campos de "Endpoints desta ilha" estão literalmente com
`<preencher quando o WordPress existir>`. O que a 20.1 protege está intacto; o
que ela bloqueia de verdade está declarado como bloqueado. Mesmo raciocínio, e
mesma redação, do bloco 1 da jornadafly de duas horas antes.

**UM TERCEIRO BLOQUEIO APARECEU, E ELE NÃO É DE ILHA NENHUMA — é do egresso, e
muda o método deste bloco.** Ao tentar abrir
`www.lojadesomautomotivo.com.br/comprar/qual-modulo-usar/woofer.html` para
enumerar a família de URLs do concorrente, a nuvem devolveu `EGRESS_BLOCKED`: a
rede Personalizada libera os domínios das ilhas, `*.googleapis.com` e
`github.com`, **e nada mais**. A busca web funciona (ela não sai por este proxy),
então o bloco saiu inteiro por ela — mas a consequência está declarada dentro do
corpus, em "Método", e é a regra da **20.3** cumprida: **toda URL citada no
arquivo é URL que apareceu em resultado de busca, com o título que a busca
devolveu; nenhuma foi aberta.** Isso importa para o bloco 3, que depende de
**ler PDF de fabricante** (Bomber, JBL/Selenium, Eros, Pioneer, e agora Zetta), e
hoje isso está fora do alcance da nuvem. Registrado no despacho como o que falta,
**e não como pedido fechado**, porque a Fundação ainda não tentou o bloco 3 e
pode ser que a busca resolva parte dele. Inventar o bloqueio antes de tentar
seria o mesmo erro que a seção 4 do contrato descreve de trás para frente.

### O que o bloco entregou

`ilhas/ohmetria/dados/corpus-buscas.md`, `publicar: false`, os três eixos que o
`PROMPT.md` manda não misturar, coletado entre **17h20Z e 17h45Z de 14/09/2026**.
**Zero número de volume de busca**, porque não houve acesso a ferramenta de
volume — mesma disciplina do corpus da Robometria e do da JornadaFly. **Zero
valor deste arquivo entra em banco ou em constante de calculadora**, e isso está
escrito duas vezes lá dentro: o que ele mede é o **desacordo da SERP**, não a
física.

**Nenhuma consulta que o dossiê da rodada 004 já mediu foi remedida.** O arquivo
ataca o que ele deixou em aberto, a começar pela única que ele marcou
explicitamente como não medida.

### Os seis achados, e por que cada um muda um bloco futuro

**1. A CONSULTA QUE O DOSSIÊ DEIXOU POR MEDIR ESTÁ MEDIDA, e a hipótese dele
cresceu.** Ele tinha **um** exemplo de URL por faixa de RMS
(`/qual-modulo-usar/subwoofer/400-rms.html`) e a leitura de que ninguém constrói
isso sem busca própria em cada variação. A família foi mapeada e tem **dois**
eixos: `{woofer, subwoofer} × faixa de RMS`, com **sete URLs vistas** (woofer
200, 400, 600 e 1200; subwoofer 400, 1000 e 2000) mais as duas páginas-mãe, e um
concorrente (`somautomotivobr`) cobrindo **cinco tipos** num endereço só. **É
planta de malha para o bloco 5b, medida e não suposta.**

**2. A VAGA DA F1 É UM DESACORDO, NÃO UM VAZIO — e é a mesma forma dos achados
da Aquametria e da JornadaFly.** Para a **mesma** pergunta sobre um falante de
200 W RMS, a SERP publica três regras incompatíveis: *até 100%*
(`lojadesomautomotivo`), *o dobro* (`somautomotivobr`, no próprio `<title>`) e
*150 a 250 W* (`mundomax`). De 150 a 400 W — **2,7 vezes** — e **nenhuma das três
diz de onde a regra sai**. O mesmo `mundomax` muda o próprio multiplicador de
`0,75–1,25×` para `0,6–1,2×` entre dois exemplos da mesma página. **Consequência
para o bloco 2:** a F1 declara o critério **com fonte de fabricante**, senão ela
vira a quarta opinião de uma briga de três.

**3. EXISTE UM VEREDITO QUE NINGUÉM PUBLICA, E ELE É "NÃO FECHA".** Dois
subwoofers de bobina dupla 2+2 Ω alcançam, em ligação simétrica, **0,5 Ω, 2 Ω e
8 Ω** — **1 Ω não está no conjunto**. Conferido por script nesta execução, cinco
configurações, e o mesmo script mostra que **um** sub 2+2 sozinho **chega** a
1 Ω, que é de onde vem a confusão. Quem digita a consulta-âncora com esse par e
um módulo de 1 Ω está pedindo o que não existe, e as páginas medidas respondem
com a fórmula *"impedância ÷ número de alto-falantes"*, que sozinha produz 0,5 Ω
e não avisa nada. **Dizer "não fecha, e o mais perto que fecha é 2 Ω" na primeira
linha é exatamente o que o `VOZ.md` manda e o que ninguém faz.** Vira obrigação
do bloco 2.

**4. A CALCULADORA JÁ EXISTE NO BRASIL — e isto CORRIGE o dossiê.** Ele escreveu
*"uma única calculadora em toda a varredura: `infinitysom.com.br`"*. São pelo
menos **quatro** para impedância (`nexxobox` com duas, `amantesdeamplificadores`,
`sombox` com duas URLs) e **três** para caixa e duto (`audioclassico`,
`speakerboxlite`, `omnicalculator/pt`). **A afirmação do dossiê é verdadeira para
as consultas que ele mediu e falsa para o nicho** — e a distinção entre as duas
coisas é o que esta correção existe para fixar. **Por que ela CONFIRMA a tese em
vez de derrubar:** essas ferramentas fazem a **aritmética** e nenhuma faz a
**decisão**, que é cruzar o resultado contra um banco de módulos que estabilizam
naquela impedância com RMS compatível; e **nenhuma delas apareceu no top 10 da
consulta-âncora** que o dossiê mediu. A ferramenta existe e **não ocupa a
pergunta que a pessoa digita** — a mesma forma do achado da JornadaFly sobre o
ângulo "vale a pena" já ter dono. **E existe uma pergunta sem resposta nenhuma:**
não há, em pt-BR, **lista de módulos filtrável por impedância estável**; a busca
devolve categoria de loja organizada por **número de canais**, vídeo de
comparação de marca e uma das fazendas nomeadas no dossiê.

**5. A F2 TEM UMA TRAVA DE UNIDADE QUE PODE QUEBRAR A VALIDAÇÃO DO PRÓPRIO
`PROMPT.md`.** "Litros" é três grandezas com nomes que não batem: a Zetta publica
*"volume bruto 49 L, volume livre 42 L, sintonia 41 Hz"*; a **Hinor — que está na
lista de carga do bloco 3** — publica que *"40 litros brutos, com o duto e o
subwoofer dentro, dão 32 a 35"*. A razão entre líquido e bruto fica entre **0,80
e 0,88**. A **trava 3** do `PROMPT.md` manda validar a fórmula da F2 contra a
litragem recomendada pelo fabricante — e **se a fórmula devolver líquido e a
recomendação for bruta, a validação acusa 12 a 20% de erro que não é erro de
fórmula, é erro de unidade**, com os dois números plausíveis e nenhum parecendo
absurdo. É mais perigoso que o `Vas 672,3 cm³` que o `PROMPT.md` já nomeava,
justamente porque não salta aos olhos. **Consequência para o bloco 3:**
`litragem_tipo` (`bruto | liquido | nao_declarado`) nasce ao lado de
`litragem_l`, e a F2 diz na tela qual dos dois está devolvendo.

**6. O DESACORDO MAIS CARO ESTÁ NO EIXO C, porque dele saem o fusível E o
cabo.** Para um módulo de 2000 W RMS a SERP publica **três divisores**: `÷12`
(167 A), `÷12,6` (159 A) e `÷20`, o "consumo musical" (100 A). **67% de
diferença**, e o fusível recomendado a 125–150% da corrente vai de **125 A a
250 A** conforme a página que a pessoa abriu primeiro. **Nenhuma das três declara
o rendimento do módulo**, que é o que faria a conta fechar. E a consulta escrita
**com a distância** (1000 W, 4 metros, queda de tensão) devolveu **cinco fóruns**
— um deles de energia solar — e **a calculadora da InfinitySom não apareceu
nela**. A vaga da F3 fica medida com precisão: não é "calcular bitola", é
**calcular bitola para a distância de ida e volta, com o fusível junto e o
rendimento declarado**, que é onde o `PROMPT.md` diz que a do concorrente para.
*(De quebra, o capacitor: 1 farad por 1000 W na regra de bolso contra o rótulo da
própria Taramps, "Mega Capacitor 0,3 Farad 1000w rms" — 3,3× na mesma página de
resultados. Não vira ferramenta agora; é matéria de artigo-âncora do bloco 5.)*

### Verificação

Nada foi ao ar e nada podia ir: esta ilha não tem site, não tem `manifest.json` e
não tem endpoint de Sync. O que foi verificado nesta execução:

- **Cabeçalho do `ESTADO.md` por parser**, como manda a seção 2 —
  `yaml.safe_load` aprovando, `bloco_atual` com 13 linhas e sem aspas duplas
  dentro de escalar de aspas duplas.
- **A aritmética do achado 3 por script**, cinco configurações de ligação, em vez
  de confiada à cabeça — inclusive o contraexemplo (um sub sozinho **chega** a
  1 Ω) que explica de onde vem a confusão do nicho.
- **O registro do domínio pelo RDAP oficial**, não pela prosa dos dois arquivos
  que discordavam.
- **A rede em três passadas com controle na mesma passada**, como a 20.2 manda,
  mais a resolução de DNS que revelou a segunda causa possível do 000.

### Próximo passo desbloqueado

**BLOCO 2 — especificação das calculadoras** (`dados/especificacao-calculadoras.md`
e `dados/constantes.json`). Não depende de site, não depende da lista de rede, e
já nasce com três obrigações que saíram do bloco 1 e estão escritas no fim do
corpus: o critério de casamento de RMS **com fonte**, o veredito **"não fecha"**
com a impedância mais próxima que fecha, e o **rendimento suposto + distância de
ida e volta** declarados na tela da F3.

---

## 2026-09-14 19h16Z — Bloco 2: especificação das três ferramentas e `constantes.json`

**A ESCOLHA DA ILHA: PRIMEIRA TENTADA, RESERVA ACEITA SEM CORRIDA.** Os cinco
`ESTADO.md` do arquipélago passaram por `yaml.safe_load` (seção 2) e os cinco
estavam com `executando_desde: null` — pela 1.1 isso já basta, porque a reserva é
escrita **antes** do trabalho (passo 5), então não havia reserva vencida para o
git desempatar. Pela **18.1**, **três** ilhas tinham despacho aberto do Raphael
datado de 14/09 (ohmetria, jornadafly e o item que sobrou na clubedomosaico),
empate de destinatário e de data; o desempate voltou para a rotação da seção 1 e
a **ohmetria** tinha a `ultima_execucao` mais antiga das três (17h17Z, contra
17h45Z e 18h45Z). Nenhuma branch `claude/*` e nenhum PR aberto para mesclar — a
branch desta execução estava idêntica ao `main`. Reserva commitada e empurrada
às 19h16Z, aceita na primeira tentativa.

**A REDE FOI RETESTADA, NÃO HERDADA** (20.2, e o `ESTADO.md` já trazia
`rede: bloqueada`): `ohmetria.com.br` e `www.ohmetria.com.br` em **000 nas três
passadas**, com `aquametria.com.br` e `robometria.com.br` em **200 nas mesmas
três**. Seis medições de bloqueio contra seis de controle verde, igual à
execução anterior. `bloqueada_por` segue `null` de propósito: o que a rede trava
é o 3b em diante, não bloco de arquivo.

**E O EGRESSO DE TERCEIRO FOI MEDIDO PELA SEGUNDA PORTA.** No bloco 1 quem
recusou foi o `curl`, em outro domínio. Aqui foi o **WebFetch em
`sac.taramps.com.br`**, `EGRESS_BLOCKED` às 19h30Z. As duas portas estão medidas
e as duas estão fechadas: **nenhum documento de fabricante foi lido**. A busca
web funciona, e foi só dela que saiu tudo que segue.

### O achado principal, e ele muda as três ferramentas

O bloco 1 mediu, no eixo A, **três regras incompatíveis** para a mesma pergunta
(100%, o dobro, 0,75–1,25×), amplitude de **2,7 vezes**, e escreveu que nenhuma
delas diz de onde sai. **Esta execução achou de onde sai, e não são três
opiniões: são duas declarações do mesmo fabricante, lidas em unidades
diferentes.** A Taramps publica em artigo dedicado, **um por linha de produto**
(DS, HD, TS, Amplayer), o critério de casamento — *a potência RMS do
alto-falante tem de ser igual ou superior à do amplificador*, teto de **100%** —
e publica em artigo próprio que **potência musical é cerca de 2× o RMS**. A
regra "use o DOBRO" que ocupa a SERP tem o mesmo 2 da razão musical/RMS, e esse
2 é a relação entre duas maneiras de medir o **mesmo** equipamento, não licença
para dobrar a potência do amplificador. A fonte que o achado A1-b disse não
existir **existe**, e ela aponta para 100%.

**O mesmo aconteceu no eixo C, e vira o achado C1 do avesso.** O divisor 20
("consumo musical") que o corpus atribuiu a um blog é, aparentemente, a conta do
**próprio fabricante** — a Taramps declara o 20 como aproximação dos técnicos
dela. Dos três divisores medidos, o de 20 é o único com autoria de fabricante;
os outros dois são `W ÷ V`, que ignora o rendimento do módulo. E apareceu um
segundo número que o corpus não tinha: **fusível a cerca de 10% acima do consumo
musical**, contra os **125 a 150%** que os guias publicam — de **110 A a 250 A**
para o mesmo módulo de 2000 W RMS, **2,3 vezes**, e o número do **fabricante é o
mais BAIXO**, o contrário do que a intuição diz.

### E tudo isso entrou como `pendente` — essa é a parte que importa

Pela regra do **elo mais fraco** (seção 10), autoria forte com leitura por busca
continua sendo leitura por busca. Há um segundo motivo, e é medição: **os
exemplos que vieram junto com o divisor não fecham entre si.** Uma resposta deu
*"3.000 W ÷ 20 = 135 A"*, e 3.000 ÷ 20 é **150**; outra deu *"TS400x4 consome
16,5 A"*, enquanto 400 ÷ 20 é 20. A **regra** veio idêntica em duas consultas
independentes, os **exemplos** não — sinal de paráfrase por cima do documento.
Regra forte, exemplos fracos: nenhuma dessas quatro constantes de fabricante
entra em fórmula publicada antes de alguém abrir a página.

As consultas foram feitas com **pergunta limpa**, como a seção 8 manda: da forma
*"qual é a conta que o fabricante publica"*, nunca *"o divisor é 20?"*. O 20
apareceu sem ter sido plantado, e apareceu duas vezes.

`dados/constantes.json` termina com **`pendencias_de_leitura`**: os quatro
documentos que promovem cada constante, em ordem de quanto desbloqueiam, com **o
que transcrever de cada um**. Promover é uma linha por constante, não um bloco.

### A F1 não depende de nenhuma delas para a metade que importa

`ferramentas/impedancias.py` enumera o domínio de saída inteiro e grava
`dados/impedancias-alcancaveis.json` com **24 casos contados**. O modelo: K
bobinas iguais de Z ohms partidas em **g grupos iguais** em série, os grupos em
paralelo → **Z × K / g²**, com g dividindo K. É aritmética, publica hoje, e prova
que **"não fecha" é calculável em vez de opinado**: dois subs 2+2 Ω alcançam
**0,5, 2 e 8 Ω**, e **1 Ω não está no conjunto**.

**A régua reprovou o próprio gerador, e o conserto virou regra da ilha.** A
primeira versão respondia, para dois subs 2+2 pedindo módulo de 1 Ω, que o mais
perto era **0,5 Ω** — por menor distância em ohms. Essa é a resposta que
**queima** o módulo: menos ohm é mais corrente. Pela assimetria de custo da
seção 10, errar para baixo custa hardware e errar para cima custa volume, então o
critério passou a ser o **menor alcançável ≥ o pedido**, e a alternativa errada
ficou **afirmada de propósito** na régua, para que trocar o critério volte a
reprovar.

**E a enumeração devolveu um veredito que este bloco não foi procurar: TRÊS
alto-falantes iguais não fecham em impedância de módulo NENHUMA.** Nas **seis**
montagens de três — uma por tipo de bobina — não existe ligação simétrica que
caia em 0,5, 1, 2, 4 ou 8 Ω; três subs 2+2 dão **12 · 3 · 1,333 · 0,333 Ω**. Não
é "ímpar nunca fecha": **um** falante de 2 Ω fecha em módulo de 2 Ω, e a régua
guarda esse contraexemplo para a afirmação não se generalizar sozinha.

### A F2 e a F3

**F2** ganhou fórmula e dois portões: `Vb = Vas / ((Qtc/Qts)² − 1)`, alinhamento
selado clássico, com status **`aguarda_validacao`** porque a trava 3 do
`PROMPT.md` manda bater com a litragem que o fabricante recomenda e o banco do
bloco 3 não existe. A **faixa de Qtc (0,7–1,1) é quem decide o tamanho da
caixa** e não tem fonte de fabricante nem leitura direta → `pendente`. E
enquanto a razão líquido/bruto estiver `pendente`, **a F2 não converte unidade**:
compara só o que já estiver na mesma.

**F3** está honestamente travada, e isso coincide com a ordem obrigatória do
`PROMPT.md`. Quatro das oito pendentes são dela, inclusive
`queda-de-tensao-maxima-aceitavel`, que foi **procurada e não encontrada em fonte
nenhuma**. Mas **duas coisas dela publicam hoje**: a **distância de ida e volta**,
que é derivação e é metade da vaga do achado C2; e a **direção do erro** — cabo
pela corrente **maior**, fusível pela **menor**, fusível nunca acima do que o
cabo aguenta, porque quem protege o cabo é o fusível e os dois erros baratos
apontam para lados **opostos** da mesma divergência. Nenhuma página medida faz
essa separação: todas escolhem um divisor e propagam para as duas saídas.

### Verificação

Nada foi ao ar e nada podia ir: esta ilha não tem site, não tem `manifest.json` e
não tem endpoint de Sync. O que foi medido nesta execução:

- **Cabeçalho do `ESTADO.md` por parser** (seção 2), `yaml.safe_load` aprovando
  antes de cada commit; citação em aspas simples dentro do `bloco_atual`.
- **O portão da F1: 73 afirmações, 0 falha**, com régua **própria** — as contas
  da conferência estão escritas à mão, com os números por extenso, e não chamam
  nenhuma função do gerador. Reproduzir com
  `python3 ferramentas/impedancias.py --conferir`.
- **Seis mutações deliberadas, seis reprovadas**: voltar ao critério de distância
  absoluta (duas maneiras), aceitar ligação assimétrica, errar o expoente do
  paralelo, encolher o teto de quantidade, e inventar um módulo de 1/3 ohm para
  ver a afirmação sobre as montagens de três cair. Régua que não pode falhar é
  teste verde com outro nome (seção 8).
- **A rede em três passadas com controle na mesma passada** (20.2), e o egresso
  de terceiro pela segunda porta (WebFetch).
- **Os números da especificação conferidos contra o JSON gerado**, não contra a
  memória de quem escreveu: 24 casos, o conjunto do par 2+2, as seis montagens
  de três e o caso de 0,125 Ω sem módulo no mercado.
- **A estrutura do `constantes.json` por script**, cobrando que nenhuma constante
  de tipo `fabricante` ou `recomendacao_editorial` esteja `publicavel`, e que
  todo item traga `fonte`, `canal_de_coleta`, `leitura`, `verificado_em` e
  `usada_em`. Zero violações.

### Próximo passo desbloqueado

**BLOCO 3 — modelo do banco**: esquema das entidades **MÓDULO** (`impedancias_estaveis[]`,
`rms_por_impedancia{}`, canais), **ALTO-FALANTE/SUBWOOFER** (`impedancia_bobinas`,
`rms`, `vas_l`, `qts`, `fs_hz`, `xmax_mm`, `sd_cm2`), **CAIXA**, **CABO** e
**CAPACITOR**. Não depende de site nem de rede. Já nasce com três obrigações
escritas: `litragem_tipo` (`bruto | liquido | nao_declarado`) ao lado de
`litragem_l`; a `faixa-de-validacao-thiele-small` como portão de **entrada**, que
**recusa** valor fora de faixa em vez de corrigir; e
`afiliado.url_busca_bruta` obrigatório em **todo** item antes de qualquer outra
coisa (25.2), com `afiliado.url_produto` em todo item que tenha ficha (25.4-b).

**Um achado de canal para esse bloco, e ele NÃO foi conferido:** a busca devolveu,
no SAC da Taramps, páginas de **descrições técnicas em HTML por modelo de
módulo** (TS 400X4, TL1500, MD1200.1, TS 1200X4 foram vistas em resultado). Se o
egresso abrir, a carga do lado **MÓDULO** pode não precisar de PDF nenhum — o que
mudaria a trava 1 do bloco 3 de "extração de PDF" para "leitura de página" na
metade que sustenta a F1. A página não foi aberta; está escrito como hipótese.

---

## 2026-09-14, 21h20Z–22h05Z — BLOCO 3: o modelo do banco, e a frase que a F1 ia publicar sobre o mercado

**Entregue:** `dados/esquema-banco.json`, `dados/modulos.json`, `dados/alto-falantes.json`,
`ferramentas/validar-banco.py`, `ferramentas/mutacoes-banco.py`. Corrigidos:
`ferramentas/impedancias.py`, `dados/impedancias-alcancaveis.json` e a seção 1.3 de
`dados/especificacao-calculadoras.md` (mais uma seção 6 nova nela).
**Nada foi ao ar, e não havia como ir:** esta ilha não tem site, não tem Sync e não tem
`/status`. Dizer que verificou no ar seria inventar a medição.

### A escolha da ilha, e a corrida que eu perdi

Os cinco `ESTADO.md` do `main` real passam em `yaml.safe_load` e os cinco estavam com
`executando_desde: null` — o que, pela 1.1, **já significa** que não há bloco da Fundação
vivo, porque a reserva é escrita ANTES do trabalho. Não houve reserva vencida para o git
desempatar. Pela 18.1, **três** ilhas tinham despacho aberto do Raphael de 14/09, e como a
regra manda pegar o mais antigo entre dois dele, o desempate foi por **hora de abertura**:
clubedomosaico (antes das 14h03Z), ohmetria (14h46Z), jornadafly (14h49Z). Meu push da
reserva da clubedomosaico foi **recusado por cerca de um minuto** — outra execução a
reservou às 21h17Z, e uma terceira reservou a aquametria às 21h18Z. Voltei ao passo 2 sem
force push, e a ohmetria foi aceita às 21h20Z. Nenhum branch `claude/*` e nenhum PR aberto
para mesclar.

**Rede pela 20.2, retestada e não herdada:** três passadas, `ohmetria.com.br` e
`www.ohmetria.com.br` em `000` nas três, com `aquametria.com.br` e `robometria.com.br` em
`200` nas mesmas três. Seis medições de bloqueio contra seis de controle verde — igual às
duas execuções anteriores. Segue bloqueada, e `bloqueada_por` segue `null` de propósito: o
que a rede trava é o 3b em diante, não bloco de arquivo.

### O banco nasce com ZERO registros, e isso é a regra desta ilha sendo cumprida

O egresso HTTP continua fechado para todo domínio de terceiro, medido pelas duas portas nos
blocos 1 e 2. A **escada de fontes** que este esquema escreve diz que número de fabricante
colhido por **busca** nasce `publicavel: false`, por mais forte que seja a autoria — é a
mesma regra do elo mais fraco que fez 8 das 18 constantes do bloco 2 nascerem pendentes.
Carregar o banco hoje produziria registros que nenhuma ferramenta pode usar e que teriam de
ser recolhidos depois.

**E há um segundo motivo, que é mais específico e mais duro:** os valores de Thiele-Small
que o dossiê desta ilha cita — Bomber Bicho Papão, JBL Bass 10SW17A, Eros E-12 MB 2.2K,
Ultravox Ultra 700+, Hinor 12 EVO 550, Triton AK 6.1, Pioneer TS-W3090BR — estão no
repositório **sem a URL do documento de onde saíram**. Gravá-los criaria registro sem
`fonte.url`, que o próprio esquema recusa; e inventar a URL seria pior que a lacuna. Lacuna
com causa nomeada é dado.

### O achado do bloco, e ele estava numa frase que a F1 ia publicar

`ferramentas/impedancias.py` afirmava sobre o **mercado** a partir de uma lista de cinco
impedâncias **digitada dentro dele**. O comentário dizia, com todas as letras, que aquilo
era *"o conjunto de valores que o mercado de módulos oferece"*; o campo que ela alimentava
no JSON se chamava `alcancavel_mas_sem_modulo_no_mercado`; e a saída 2 da F1, na
especificação, dizia *"0,125 Ω é alcançável e não existe módulo para isso"*.

**Nenhum registro de banco podia contradizer isso, porque não havia banco.** É a família da
seção 8: número de tela nasce **contado**, nunca digitado, e régua escrita para um mundo que
nunca aconteceu nasce sem poder falhar — ela passaria por todos os blocos parecendo saudável
até o dia em que alguém gravasse um módulo de 16 Ω e a página continuasse dizendo que ele
não existe.

O conserto tem quatro partes e nenhuma delas é encurtar a prosa:

1. **A lista mudou de casa.** `vocabularios.impedancia_de_modulo` e
   `vocabularios.impedancia_de_bobina` moram agora em `dados/esquema-banco.json`, e o
   gerador as lê de lá (seção 26.2: a lista mora no esquema, nunca dentro da régua). Se a
   chave sumir, **o gerador morre** em vez de cair num literal — medido nesta execução:
   apagando a chave, ele sai com código 1 e diz por quê.
2. **O campo mudou de nome**, para `alcancavel_e_fora_do_vocabulario_de_modulo`, e o JSON
   carrega, ao lado, a frase que a F1 **pode** e a que ela **não pode** dizer.
3. **O validador cobra os dois sentidos.** Módulo do banco fora do vocabulário é **erro duro
   do ESQUEMA**, não do módulo — a lista cresce numa linha e o módulo entra; sumir com o
   módulo seria o banco escondendo o que mediu. E entrada do vocabulário sem módulo por trás
   é **dívida contada**, em `vocabulario_sem_lastro`, hoje **5 de 5**.
4. **A frase da tela virou "nenhum módulo do nosso banco"**, e a especificação ficou com a
   proibição escrita: enquanto `vocabulario_sem_lastro` não for vazio, nenhuma frase de
   inexistência de mercado é publicável.

### As três decisões do esquema que vão para a tela, não só para o disco

- **Módulo não tem "um RMS": tem `rms_por_impedancia`.** Não existe campo `rms` escalar de
  módulo neste esquema, de propósito — um número de watt solto é exatamente o defeito que o
  bloco 1 mediu na SERP.
- **`potencia.unidade_declarada` nasce com `unidade_declarada_por`** (seção 26 do contrato,
  aplicada ao campo que dói nesta ilha). Lá o fabricante batiza a peça pela posição e o banco
  classifica pela função; aqui ele estampa um **número** e ninguém declara a **unidade**. É o
  que separa *"a Taramps declara 3.000 W RMS"* de *"a página estampa 3.000 W e nós lemos como
  RMS"*.
- **A monotonia, que é o portão mais barato desta ilha.** Módulo entrega **mais** watt quando
  a impedância **cai**. Tabela que cresce com a impedância é transcrição errada ou dois
  números de unidades diferentes na mesma tabela — o achado 0.1 do bloco 2 aparecendo dentro
  de **um único registro**, em vez de entre duas páginas da SERP.

### O portão, e a conferência que ele ganhou porque "reprovou" não bastava

`ferramentas/mutacoes-banco.py`: **39 mutações, 39 decidiram certo**, nos dois lados da
fronteira — **6 mundos que têm de PASSAR** (o banco vazio de hoje; um módulo e um alto-falante
corretos, que o banco não tem; o registro que entra sem ser publicável, com o motivo escrito)
e **33 quebras que têm de REPROVAR**, uma por linha de
`o_que_o_esquema_permite_e_o_banco_ainda_nao_tem`.

Os registros de bancada são **ficção**, moram no arquivo de mutações e nunca em `dados/`:
fixture dentro do arquivo de dados seria a ilha inventando produto.

**E cada quebra declara a FRASE que espera ouvir de volta.** "Reprovou" não é a mesma coisa
que "reprovou pelo motivo certo": uma mutação pode quebrar o registro de um jeito que dispara
**outra** trava e voltar verde sem nunca ter medido a sua — é a cicatriz da mutação inerte que
a Robometria pagou em 14/09. Quebra sem linha em `ESPERA_OUVIR` é erro da própria bancada, e
ela reprova por isso. **Provado que essa conferência morde:** trocando uma frase esperada por
outra trava real do validador, a bancada acusa a linha e sai com código 1.

### Próximo passo desbloqueado

**Bloco 4 — a F1**, parcialmente travada por banco vazio. A metade aritmética publica hoje
(24 montagens, veredito, a impedância mais perto que fecha); a lista de módulos que
estabilizam precisa de pelo menos um registro em `dados/modulos.json`, e isso é o **3c**, que
espera o canal, não a decisão. A seção 14 do contrato (indexação é prioridade máxima de ilha
nova) puxa para construir a F1 com a lista vazia **declarada na tela**. A seção 6 nova da
especificação diz onde cada coisa está, para quem pegar o bloco 4 não ter de reler dois
arquivos inteiros.

---

## 2026-09-15, 11h17Z–11h45Z — BLOCO 4: a F1 existe como regra, e ainda não como página

**Entregue:** `ferramentas/f1-referencia.py` (o cérebro da F1: entrada → resposta
inteira, já em frase acentuada), `ferramentas/gerar-f1.py`, `dados/f1-respostas.json`
(os **144 estados** varridos, mais a tabela pré-renderizada de 24 linhas,
`publicar: false`), `ferramentas/teste-f1.py` (**8.262 afirmações, 0 falha**) e
`ferramentas/mutacoes-f1.py` (**41 mutações, 41 decidiram certo**). Mais a seção 7 de
`dados/especificacao-calculadoras.md`, que é onde quem pegar o 3b encontra a regra
pronta. **Nada foi ao ar**: esta ilha não tem site, não tem Sync e não tem `/status`,
e dizer que verificou no ar seria inventar.

### A escolha da ilha, e a corrida

Os cinco `ESTADO.md` parseiam em `yaml.safe_load` e os cinco estavam com
`executando_desde: null` — que pela **1.1** já significa que não há bloco da Fundação
vivo, sem precisar do git para desempatar reserva vencida. Pela **18.1** li o topo dos
cinco `PROMPT.md` antes de aplicar a rotação, e **nenhuma ilha tem despacho corretivo
com item acionável aberto**: o do Raphael de 14/09 na aquametria está *cumprido e
conferido no ar*; o de 14/09 na clubedomosaico foi *fechado às 21h17Z* daquele dia,
com os quatro itens da artesã verificados; o de 14/09 na robometria idem; e os desta
ilha e o da jornadafly são despachos de **nascimento**, que carregam a fila inteira e
por isso não cabem na 18.2. Sobrou a rotação da seção 1, e a ohmetria tinha a
`ultima_execucao` mais antiga por quase uma hora (21h20Z de 14/09, contra 22h16Z,
23h35Z, 23h35Z e 00h01Z).

**O push da reserva foi recusado na primeira tentativa** — outra execução tinha
reservado a **aquametria** às 11h17Z, citando um despacho ALTA da Fundação em
`dados/despachos.md`. O `main` tinha andado; `fetch` + `rebase`, **sem force push**, e
a reserva da ohmetria entrou às 11h19Z. Nenhum branch `claude/*` e nenhum PR aberto.

**Rede pela 20.2, retestada e não herdada:** três passadas, `ohmetria.com.br` e
`www.ohmetria.com.br` em `000` nas três, com `aquametria.com.br` e `robometria.com.br`
em `200` nas mesmas passadas. Seis medições de bloqueio contra seis de controle verde,
igual às três execuções anteriores. Segue bloqueada, e `bloqueada_por` segue `null` de
propósito: o que a rede trava é o 3b em diante, não bloco de arquivo.

### Por que a F1 não tem PHP, e isso é decisão registrada

A seção 8 do `ARQUIPELAGO.md` cobra três vezes, todas pagas pela Robometria, a mesma
coisa: **render de bancada que serve menos do que o site serve mede a página errada e
não acusa**. Sem casca — e a casca é o 3b, trabalho de navegador que está com o
Raphael — um snippet PHP desta ilha só poderia ser medido assim. Então a regra nasceu
onde ela pode ser conferida hoje, em Python, e o PHP, quando nascer, é **tradutor**
desta referência, frase a frase, com a bancada comparando as duas. É o mesmo desenho
que a Robometria usa entre `cobertura-r1.py` e `robometria-r1.php`.

### O achado do bloco, e ele estava num campo que o bloco 2 já tinha gerado

`dados/impedancias-alcancaveis.json` devolve, para todo pedido que não fecha, um campo
`mais_perto_que_fecha`. **Servir esse campo sempre do mesmo jeito publicaria, em 17 dos
144 estados, a resposta que queima o módulo.** Porque `abaixo_do_pedido: true` quer
dizer que **nada** na montagem alcança o mínimo que aquele módulo estabiliza, e o valor
devolvido é o menos ruim de um conjunto que é todo ruim. Concretamente: quatro falantes
de 1 Ω pedindo módulo de 8 Ω alcançam 0,25, 1 e 4 Ω — o campo devolve 4, e 4 Ω num
módulo que só estabiliza até 8 Ω é menos ohm do que ele aguenta.

A especificação previa **dois** vereditos e a tela passou a ter **três**:

- **NÃO FECHA, SOBE** (36 estados) — existe valor alcançável ≥ o pedido. A página o
  nomeia, diz com que ligação, e diz o que se perde: *"em 2 ohms o módulo entrega menos
  watt e roda frio, e esse é o lado seguro de errar"*.
- **NÃO FECHA, SÓ ABAIXO** (17 estados) — não existe. A página **não oferece valor**:
  *"Não ligue assim… abaixo do mínimo é o que queima."* E o bloco de compra fica sem
  piso, de propósito.
- **NÃO FECHA EM NENHUMA** (30 estados) — as seis montagens de três alto-falantes.

É a assimetria de custo da seção 10 aplicada a um campo que já existia, e é a mesma
regra que o Clube do Mosaico escreveu em 12/09: **causa que o código separa, o texto
separa.** Misturar as duas numa frase é inventar uma delas.

### O piso de compra quando o banco tem zero itens

A **25.2** dá o piso por item — marca + modelo viram a palavra-chave — e com zero
módulos não existe item. A saída honesta não é inventar produto: é derivar a busca da
**própria resposta**, pela impedância em que o módulo precisa estabilizar. É a mesma
manobra que a jornadafly registrou em 14/09 ao derivar o piso da cidade. O molde vem de
`esquema-banco.json → piso_de_compra.moldes.shopee` e nunca é digitado na ferramenta; a
bancada refabrica cada URL do molde e compara. Sai **sem** `rel=sponsored`, porque
busca crua não rende comissão e carimbá-la de patrocinada mentiria para o leitor.

**91 estados com piso, 53 sem** — e os 53 dizem por quê. Mandar quem não tem montagem
válida para uma busca de módulo seria vender uma coisa no lugar de outra, que é pior do
que não ter link.

### A conta que eu ia publicar estava errada, e o conserto não foi trocar o número

A primeira versão da seção 7 da especificação dizia **47** estados sem piso: somei 30 e
17 de cabeça e esqueci os **6 estados SEM PEDIDO das montagens de três**, que também não
têm o que oferecer. São 53. O número saiu errado pelo motivo que a seção 8 mais repete
— foi somado, não contado.

Trocar o 47 por 53 devolveria o verde e deixaria o defeito de pé. Então **a bancada
passou a ler a prosa**: ela extrai da seção 7 os cinco números da distribuição de
vereditos e as duas contas do piso, e compara com a varredura. Quatro mutações provam
que morde — contagem trocada, conta de piso trocada, a linha sumindo, e o texto de
verdade tendo de passar. É a **terceira conta** que a seção 8 pede quando duas metades
contam a mesma coisa, e o defeito que ela impede é o mais barato de cometer.

### As duas coisas que as mutações acharam, as duas fechadas antes do commit

1. **A bancada não conferia a lista de módulos por ligação.** Com o banco vazio, a
   afirmação passava sobre lista vazia; com um módulo dentro, a linha da ligação podia
   continuar dizendo que não havia nenhum e a bancada aprovava. É exatamente o mundo que
   o **esquema permite e o banco ainda não tem**, e só a mutação que *produz* o mundo o
   enxerga — verde sobre um banco de zero elementos é ausência de contraexemplo
   confundida com prova.
2. **A referência não conferia o banco de casos contra o vocabulário do esquema.**
   Apagando `impedancia_de_bobina` do esquema, a F1 continuava respondendo, feliz, a
   partir do banco de casos de ontem. Duas metades contando a mesma coisa sem nunca se
   falarem. Agora ela **para**, e a mutação mede os dois sentidos: esquema sem a chave, e
   esquema intacto com o banco de casos velho — que é o caso que acontece de verdade,
   quando alguém acrescenta bobina ao vocabulário e esquece de rodar
   `ferramentas/impedancias.py`.

### E a régua de acento pegou um defeito que não era de acento

A frase da prestação de contas citava `dados/modulos.json` **na tela**. Caminho de
arquivo do repositório numa página é a ilha falando com o visitante no vocabulário de
quem a escreveu, e a regra da fase 4b sobre texto acentuado foi o único portão que o
viu. A frase passou a dizer, na língua da pessoa, que a ilha ainda não conferiu nenhum
módulo com a ficha do fabricante na mão e por isso não recomenda nenhum.

### O que a F1 está proibida de dizer, e quem vigia

1. **Qualquer afirmação sobre o MERCADO**, enquanto `vocabulario_sem_lastro` não for
   vazio (hoje 5 de 5). A única frase verdadeira é *"nenhum módulo do nosso banco"*.
2. **Qualquer teto de RMS**, enquanto `criterio-rms-modulo-nao-passa-do-falante`
   estiver `pendente`. A página imprime o RMS do falante e diz **o que ainda não pode
   dizer**, em vez de calar.
3. **As cinco expressões proibidas pelo `VOZ.md`** no veredito.

As três são varridas nos 144 estados, no **corpo** — `texto_de_tela()` junta o que o
visitante lê e deixa de fora `id`, URL e palavra-chave de busca, que são ASCII por
desenho e não são frase.

### Verificação

`teste-f1.py` **8.262 afirmações, 0 falha**, com a aritmética de associação reescrita à
mão dentro dele (`Fraction` e divisores) para poder discordar do gerador.
`impedancias.py --conferir` 73, `validar-banco.py` sem erro com o aviso de
`vocabulario_sem_lastro` 5 de 5, `mutacoes-banco.py` 39 de 39. **`mutacoes-f1.py`: 41
de 41** — 4 mundos que têm de passar, 28 quebras cada uma declarando a frase que espera
ouvir, 4 mortes, 4 sobre a prosa da especificação, e o autoteste da própria bateria,
que troca a frase esperada de uma quebra pela de outra trava real e exige que a bateria
acuse. `validar-banco.py` ganhou `f1-respostas.json` na lista do que **não é banco de
produto**: cobrá-lo como banco seria medir a coisa errada com a régua certa.

**NADA FOI AO AR.** Sem WordPress não há manifest, não há Sync e não há `/status`.

### Próximo passo desbloqueado

**A F2 como regra**, pelo mesmo desenho da F1 — e com uma diferença que muda tudo:
`formula-volume-caixa-selada` está `aguarda_validacao` e `faixa-qtc-alvo` está
`pendente`, então **a F2 não pode publicar litragem** enquanto a leitura não abrir. O
que ela pode fazer hoje é o que a F1 fez com o banco vazio: o domínio de entrada, as
recusas declaradas, o que ela se recusa a afirmar e por quê, e a trava de faixa de
Thiele-Small, que é constante `publicavel`. O 3b e o 3c continuam esperando,
respectivamente, o WordPress e o egresso.
