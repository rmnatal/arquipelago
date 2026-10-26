# AUDITORIA PENTE FINO — 26/10/2026

**41 arquivos de regra e prosa lidos inteiros:** `ARQUIPELAGO.md` (1.195 linhas), `bussola/BUSSOLA.md`,
`bussola/fila.md`, `bussola/despacho-viagem.md`, `foco.md`, `README.md`, `dados/PAINEL.md`, `dados/consertos.md`,
`AUDITORIA-PENTE-FINO-2026-10-12.md`, os dois `bussola/dossies/*/DOSSIE.md` e os dois `bussola/dossies/*/VOZ.md`,
`ilhas/_modelo/{PROMPT,ESTADO}.md`, e das cinco ilhas os cinco `PROMPT.md`, os cinco `ESTADO.md`, os cinco
`VOZ.md`, os cinco `DESIGN.md`, os três `ARVORE.md` e os três `dados/consertos.md`.

**Medido, não lido:** os **80** JSON de `ilhas/*/dados/` passados por `json.load` (80 parseiam, 0 falham); os seis
`esquema-*.json` conferidos campo por campo contra a §25; os **620** arquivos versionados (`git ls-files`) varridos
por oito famílias de padrão de segredo; e **os próprios portões das ilhas rodados** em vez de acreditar na prosa —
`validar-especies.py`, `bancada.py --lista` nos três modos, e recontagem em Python de `produtos-*.json`,
`pecas.json`, `modelos-robo.json`, `materiais-*.json`, `experiencias.json`, `ensaio-shopee-2026-10-21.json` e
`consultas-de-produto.json`.

**Resultado: 1 GRAVE · 20 MÉDIO corrigidos em 11 arquivos · 7 BAIXO corrigidos · 14 MÉDIO registrados · 17 itens
herdados ainda abertos.**

**UMA NOTA DE CADÊNCIA, antes de tudo:** o relatório anterior é de **12/10/2026**. **Não houve Pente Fino em
19/10** — `git log -- 'AUDITORIA-PENTE-FINO-*'` não tem nada entre 12/10 e hoje. Esta rodada cobre **duas
semanas**, e é por isso que os herdados abaixo saltam de "1 semana" para "3 semanas" de uma vez. Nesse intervalo o
contrato ganhou quatro seções novas (31, 32, 32.5-b e 32.5-c), a Bússola ganhou duas (3.0-c e 3.0-d) e a `fila.md`
teve a régua de dinheiro inteira remedida. **Foi a semana de maior mudança de lei do projeto, e foi a semana em
que o auditor não rodou** — 14 dos 28 consertos de hoje são de pontas que ficaram para trás justamente nela.

---

## GRAVE — CORRIGIDO (1)

**1. `ilhas/clubedomosaico/PROMPT.md:5` — o aviso de topo dizia "ESTA ILHA ESTÁ EM FOCO", e ela saiu do foco há
12 dias. CORRIGIDO.**

> *"**ESTA ILHA ESTÁ EM FOCO desde 24/09/2026.** `foco.md` na raiz nomeia a **clubedomosaico**, e pela seção
> **1.2** do `ARQUIPELAGO.md` a Fundação trabalha **só nela**. Este arquivo vale inteiro."*

**A contradição:** `foco.md` nomeia a **jornadafly** desde **22/10/2026**, e antes dela a aquametria, de 14/10 a
22/10 — o próprio `foco.md` registra as duas no `historico`. A ponta nova sempre esteve **neste mesmo arquivo**,
260 linhas abaixo: *"A ilha está FORA DO FOCO, em modo de medição pela 1.2-b.1"* (23/10), e o `ESTADO.md` e o
`dados/PAINEL.md` concordam com ela.

**A evidência:** `git log -L 5,8:ilhas/clubedomosaico/PROMPT.md` → `2c25302`, **24/09/2026**. A linha ficou de pé
**32 dias**, nas quatro primeiras linhas do arquivo que toda execução da Fundação lê depois do contrato.

**Por que é GRAVE e não MÉDIO:** não é número velho, é **permissão**. O aviso autoriza por escrito o bloco de
construção que a 1.2 proíbe em ilha fora do foco, e autoriza na posição em que ninguém duvida — o topo. É a
distinção que a auditoria de 12/10 nomeou em "O PADRÃO": *"régua velha dorme; permissão velha acorda"*. Esta
acordou: entre 14/10 e hoje, a ilha recebeu seis commits de ronda e correção e **nenhum** de construção, o que
quer dizer que o aviso ainda não foi obedecido — e não que ele fosse inofensivo.

**E a parte que dói:** o próprio parêntese do aviso dizia que o aviso **anterior** a ele tinha sobrevivido a *"três
mundos atrás"*. Sobreviveu a dois. **A nota sobre o defeito foi escrita dentro do defeito que a repetiu.**

**O conserto:** o bloco passa a declarar a ilha fora do foco, em modo de medição pela 1.2-b.1, nomeia a jornadafly
como a ilha em foco, diz o que **pode** rodar aqui (ronda técnica pela decisão de 28/09, correção da lista fechada
19.1) e manda trocar a linha no mesmo commit em que o foco mudar. O contraste está na mesma pasta de ilhas e vale
como modelo: o `PROMPT.md` da **ohmetria** carrega um aviso de 16/09 que já sobreviveu a três trocas de foco e
**não errou nenhuma vez**, porque ele não afirma qual ilha está em foco — ele afirma *"esta ilha NÃO está"* e
manda conferir `foco.md`, *"que é a fonte, nunca este parágrafo"*. **Aviso que aponta para a fonte não envelhece;
aviso que copia a fonte envelhece sempre.**

---

## MÉDIO — CORRIGIDO (20 consertos, 11 arquivos)

### A família da semana: a régua de dinheiro foi remedida em 22/10 e a `fila.md` não foi relida

As quatro gravações de **22/10/2026** (`7d61d7a`, `df7ad29`, `7404e8a`, `3428190`) mediram comissão **e** ticket no
painel de afiliado, produto por produto, em **dez nichos e 200 produtos**, e acharam que o piso real é **8%** e não
os 3% em que a página inteira estava ancorada. `git show` de cada uma mostra que elas tocaram as linhas **83+**,
**179+** e **228+** do arquivo. **Nenhuma tocou o quadro de abertura, que governa a leitura de tudo.** É o
arquétipo de 13/09/2026 outra vez, no arquivo que a Bússola abre primeiro.

**2. `bussola/fila.md`, quadro de abertura, motivo (a) — "os 3% de 14/09 continuam sendo o melhor número que a
Bússola tem, e por isso estão preservados em cada linha abaixo". CORRIGIDO por ponteiro.**
As duas metades são falsas desde 22/10: o número melhor existe (8%, com ferragem em 13% e peça de robô em 12%) e
**não** está preservado como 3% em cada linha abaixo — a tabela do M remedido está na mesma página.
`git log -L 9,34:bussola/fila.md` → `de723ad`, **21/10**, rodada 006. **O ponteiro diz, com todas as letras, o que
ele NÃO muda:** o ranking continua vazio, porque o motivo **(b)** — nenhum nicho com tráfego medido — é
independente e continua inteiro. Conserto que ressuscitasse o ranking seria decisão, não conserto.

**3. `bussola/fila.md`, "O que destrava" — pedia fechar a P4b inteira. CORRIGIDO por ponteiro:** a metade **Shopee**
fechou em 22/10; o que resta é a tabela do Mercado Livre e os doze nichos que ainda não foram ao painel.

**4. `bussola/fila.md`, dívida 1-B — "M fica não calculado na 008 exatamente como ficou na 006 e na 007".
CORRIGIDO por ponteiro, e este é o conserto com custo de rodada.** Lida ao pé da letra, a linha manda a rodada 008
esperar que o Raphael libere `help.shopee.com.br` — parado há três rodadas — quando em 22/10 o M de dez nichos foi
calculado **sem** esse host, pelo painel. E a própria página, oito seções acima, diz que o resto são *"oito buscas
de minutos, no mesmo painel"*. **A ordem certa é painel primeiro, tabela canônica depois**, e era o contrário que
estava escrito.

**5. `bussola/fila.md`, dívida 2 (P4b) — "Sem ela não há M, e sem M não há índice", apontando a resistência de
chuveiro como o caso que ela decidiria. CORRIGIDO por ponteiro:** a resistência **já tem** o número que a linha
esperava — 8% sobre R$ 32, **M 0,83** —, medido em 22/10. `git log -L 444,458` → `a7f77c0`, **21/10**.

**6. `bussola/fila.md:229` — "a melhor facilidade da página inteira", e a correção que a declara falsa está DOZE
LINHAS ABAIXO, escrita pelo MESMO COMMIT. CORRIGIDO.**
O `git show 3428190` mostra a coisa inteira num diff: a gravação de 22/10 riscou a frase *"Acima de toda linha
desta página"*, escreveu *"**Erro 2** — 'a melhor facilidade da página' é falso (…) a facilidade da ferragem é
**4,40**, a **segunda** melhor; a melhor é a do som automotivo, **4,64**"* — e **deixou a frase de pé nas linhas de
contexto do próprio hunk.** Recalculado por mim pelas fórmulas do cabeçalho da página: ferragem S 4,00 × 0,60 +
P 5 × 0,40 = **4,40**; som automotivo S 4,40 × 0,60 + P 5 × 0,40 = **4,64**. **É a quarta vez que esta frase é
consertada** — 14/09, 05/10, 12/10 e hoje —, e a terceira em que quem a conserta não a vê.

**7. `bussola/fila.md`, fila de medição, resistência de chuveiro — "a 3% é a faixa que matou irrigação e ferragem.
Só fecha se a P4b mostrar comissão extra alta". CORRIGIDO por ponteiro.** Medido em 22/10: resistência dá 8% sobre
R$ 32 (**M 0,83**), e **a ferragem não morreu, ressuscitou** a 13% e M 1,84. A célula é de 21/10.

**8. `bussola/fila.md`, fila de medição, enxoval de cama — "a faixa em reais não foi verificada". CORRIGIDO:**
verificada em 22/10, 8% sobre ticket mediano de **R$ 82**, **M 1,73**, o segundo melhor dos dez remedidos.

**9. `bussola/dossies/som-automotivo/DOSSIE.md` — o M do dossiê é o de 3%, e tem uma ironia que explica por que
ninguém o releu. CORRIGIDO por ponteiro.**
As notas trazem **M 1,65** (R$ 202 × 3%) e a linha 71 carrega a correção *"Dizia M 2,59 e índice 4,23, a régua da
Amazon"*. A medição de 22/10 devolveu **exatamente 2,59** — por um motivo inteiramente diferente e correto: 8%
reais da Shopee, não os 7–8% da Amazon que a §7 proíbe. Conferido na fórmula da própria página: R$ 202 × 8% =
R$ 16,16 → 2,2 × log10(16,16) − 0,07 = **2,59**. **Quem bate o olho na correção antiga lê "2,59 já foi descartado"
e passa adiante o número certo.** O ponteiro diz também o que não faz: não recalcula nota e não mexe em ordem de
fila — as duas linhas remedidas seguem fora do ranking até passarem no piso da 3.0-d.

### O molde da seção 32 fechou em 21 e 23/10, e três arquivos continuaram pedindo o trabalho

**10. `ARQUIPELAGO.md` §2 — o molde canônico do cabeçalho de estado não tem os dois campos que a §21.6 exige há 45
dias. CORRIGIDO.**
A **21.6** (11/09/2026) manda: *"O cabeçalho do `ESTADO.md` de cada ilha ganha `piso: abaixo|atingido` e
`primeira_indexacao: <data ou null>`"*. O bloco YAML de exemplo da §2 listava oito campos e **nenhum dos dois**. O
`ilhas/_modelo/ESTADO.md` recebeu os dois em **21/09/2026**, pelo Pente Fino, com a nota *"obrigatorio pela secao
21.6"* — **e a seção que o molde diz obedecer nunca foi relida.** Medido hoje: os **seis** `ESTADO.md` (o `_modelo`
incluído) carregam os dois campos. Só o exemplo do contrato não tinha. **O molde certo apontando para o exemplo
velho** é a forma mais barata deste defeito, e ela estava dentro da seção que o descreve.

**11. `ilhas/aquametria/ESTADO.md`, seção "Blocos" — "Faltam as quatro outras calculadoras e as fichas de peixe",
fechado quatro horas depois. CORRIGIDO por ponteiro.**
Escrito às **14h09Z de 21/10** (`895072b`); as cinco calculadoras saíram às 18h0xZ e **as 29 fichas de peixe às
18h2xZ do mesmo dia**, conferidas pela 18.4 — está no `PROMPT.md` desta ilha. **Três execuções passaram por este
arquivo depois dela e nenhuma a releu.** E o `foco.md` fecha a conta pelo lado do contrato: *"AS TRES ILHAS ESTAO
COM O MOLDE NO AR E CONFERIDO"*, medido em 23/10 — ou seja **o despacho do molde não fura mais o foco** (exceção
da 1.2 de 21/10).

**12. `ilhas/clubedomosaico/PROMPT.md:348` — "20 de 20 passam" na 32.5. CORRIGIDO por ponteiro.**
É o ato datado de 21/10, e a **§32.5-b do contrato nasceu em 23/10 justamente para dizer que ele certificava a
página que o autor abriu**: a ronda independente achou **19 de 20**, e as páginas do molde no ar eram **22**. A
régua que varre todas fechou às 19h4xZ de 23/10 com **22 de 22 dentro da 32.5**. A correção morava 100 linhas
acima; o ponteiro foi para a linha que alguém encontra primeiro ao procurar o número.

### A contagem de URL da clubedomosaico envelheceu em quatro lugares do mesmo arquivo

**13. `ilhas/clubedomosaico/ESTADO.md` — "A ilha tem 31 URLs. Faltam 9 para o piso de 40". CORRIGIDO para 32 e 8.**
As duas gravações são do **mesmo dia**: `55b57d4` às 13h18Z escreveu 31 aqui, `508399c` às 16h20Z escreveu
`urls_publicadas: 32` no cabeçalho e *"8 URLs para o piso da 21.1"* na tabela — **e não releu esta linha, três
telas acima, dentro da mesma seção.** Conferido no ar em 23/10: **32 de 32 URLs em HTTP 200**.

**14. `ilhas/clubedomosaico/ESTADO.md` — "`piso: abaixo`, 29 de 40 URLs" e "quando as 11 URLs nascerem". CORRIGIDO
para 32 de 40 e 8 URLs.**

**15. `ilhas/clubedomosaico/ESTADO.md` — "conferir-no-ar.py fecha APROVADO com 524 afirmações, 29 de 29 URLs em
200". CORRIGIDO para 530 e 32 de 32**, que é o que o mesmo arquivo publica na entrada de 23/10. Os três números
eram de 09/10.

**16. `ilhas/clubedomosaico/ESTADO.md` — "20 dos 41 itens desta ilha estão com a saúde do link NÃO MEDIDA".
CORRIGIDO por ponteiro, e o custo escrito no item foi desmentido duas vezes.**
A ronda de **23/10** fechou **24 de 24 testáveis VIVOS** — 20 da Shopee em `item_status` normal e os 4 de catálogo
do Mercado Livre na página renderizada —, zero morto, zero esgotado, zero clique de afiliado gasto. **E o "41"
nunca foi o banco:** recontados hoje os cinco `dados/materiais-*.json`, são **43** (acabamento 10 · alicates 6 ·
colas 9 · pastilhas 13 · rejuntes 5), que é o número que `dados/consertos.md` publica em *"43 de 43"*. O pedido ao
Raphael continua legítimo; o custo que o justificava, não.

**17. `ilhas/clubedomosaico/ESTADO.md` — item "Precisa do Raphael": "Trocar a linha `ilha:` do `foco.md`".
CORRIGIDO: a condição fechou há 12 dias.** A linha foi para `aquametria` em 14/10 e para `jornadafly` em 22/10.
O que o item dizia estar parado — a aquametria esperando foco — destravou no mesmo dia.

**18. `ilhas/clubedomosaico/ESTADO.md` — "M10 do Pente Fino: a altura do cabeçalho, 84 ou 96 px — o `DESIGN.md`
diz 96 e está sozinho contra três documentos". CORRIGIDO: estava fechado quatro dias antes de o item ser escrito.**
O `DESIGN.md` foi corrigido em **05/10/2026** e hoje diz ~84 px de barra e 52 px de logo, com o desempate da §22.2
no próprio parágrafo. O item é de **09/10** e descreve o `DESIGN.md` de antes da correção. Medido no código: a
casca serve `min-height:5.25rem` (84 px) e `height:52px`, e `conferir-no-ar.py` **reprova** se o CSS não mandar 52.
**Nenhuma ponta diz 96.** O M10 passou duas semanas na lista de decisões do Raphael sem haver decisão a tomar.

**19. `ilhas/clubedomosaico/PROMPT.md:2741` — item de bancada aberto, pago no mesmo dia, e hoje proibido pela 31.3.
CORRIGIDO por ponteiro.**
Escrito às 11h38Z de 09/10 (*"treze das catorze baterias ainda não têm `restaura_em_sinal()`"*) e fechado às
**20h47Z do mesmo dia** — o aviso de topo do próprio arquivo diz *"O CONSERTO DE CÓDIGO ESTÁ NAS CATORZE DESDE
09/10/2026 às 20h4xZ, e ele é UM MÓDULO e não catorze cópias"*, e o `ESTADO.md` confirma com *"**PAGO** (…) e eram
CATORZE e não treze"*. A execução que o fechou não releu a linha 2.600 linhas abaixo. **E mesmo aberto não seria
trabalho de hoje:** a **31.3** (21/10) proíbe *"ampliar, refatorar, deduplicar ou testar portão que já existe"*
enquanto a ilha tiver item de conteúdo ou de CTR aberto — e ela tem.

**20. `ilhas/clubedomosaico/ARVORE.md` §5 — o ponteiro do Pente Fino de 12/10 envelheceu no mesmo dia em que foi
escrito. CORRIGIDO por recontagem.**
Ele dizia *"um site de **29** URLs olhando **19**"*; saiu às **09h01Z de 12/10** e **três linhas novas entraram na
tabela depois dele**, às 10h48Z, 13h45Z e 16h47Z, sem que ninguém o relesse. Contado hoje: a tabela tem **22
linhas de página** (20 são URL de sitemap) e a ilha tem **32 URLs**. **Faltam 12 linhas, não 8:** as oito páginas
de consulta de produto da §30 e **quatro das cinco peças** de `/loja/` — a tabela traz só a
`quadro-flores-do-campo`, e `dados/pecas.json` tem `total: 5`. Escrever as doze continua sendo bloco da Fundação, e
por isso não foi feito aqui. **Terceiro relatório seguido em que o auditor erra o vizinho da linha que corrige —
e o primeiro em que o vizinho errado é um ponteiro do próprio auditor.**

**21. `ilhas/clubedomosaico/ARVORE.md` §3b — "peça publicada pela artesã, que hoje são 1 (`total: 1`)". CORRIGIDO
para 5.** A ponta nova está **neste mesmo arquivo**, na seção 7b: *"hoje são cinco peças na cópia e as cinco são
medidas"*, escrita em 28/09 sem que ninguém voltasse à seção 3b. Contado hoje em `dados/pecas.json`: `total: 5`.
*(A conclusão que o número sustentava — "faltam duas para o mínimo de três do 16.5, então nenhuma coleção nasce
hoje" — caiu com ele, e **quem a reescreve não é o Pente Fino**: ver o item do M9 em "Precisa do Raphael".)*

### As duas pontas que diziam coisas opostas sobre o mesmo arquivo e o mesmo portão

**22. `ilhas/aquametria/PROMPT.md` — o mesmo item diz que o ensaio EXISTE no `main` e que ele NÃO EXISTE.
CORRIGIDO por ponteiro.**
Ponta nova, **21h50Z de 21/10** (`f1fa9a1`): *"O ENSAIO EXISTE NO `main`: `dados/ensaio-shopee-2026-10-21.json`, com
78 itens"*. Ponta velha, **20h18Z do mesmo dia** (`a163b1f`), uma tela abaixo: *"`dados/ensaio-shopee-2026-10-21.json`
**não existe**, e nenhum arquivo foi criado"*. **Medido hoje rodando o parser:** o arquivo está no `main` com
70.501 bytes, **78 itens**, **37** com `degrau_que_casou`, **41** com `motivo_sem_ficha`, **0** sem nenhum dos
dois. Uma hora e meia entre as duas, no mesmo item. **O ponteiro preserva a metade que vale:** o achado de
arquitetura — a credencial da Shopee existe no ambiente da **Fundação** e não no das **MÃOS**, logo a Sentinela não
gera link em ilha nenhuma — continua inteiro, e é ele que faz o PASSO 4 da leitura semanal produzir despacho e
nunca link.

**23. `ilhas/robometria/PROMPT.md` — instrução aberta para escrever portão novo, justificada com exatamente a frase
que a §31.2 proibiu cinco dias depois. CORRIGIDO por ponteiro de suspensão.**
A instrução diz: *"Vale a pena escrever um portão sem rede que reprove registro `publicavel` com `url_busca` vazia
ou ausente — **hoje ele ficaria verde, e é justamente por isso que é a hora de escrevê-lo**"* (16/10). A **31.2**
(21/10) responde: *"Portão, régua, mutação, bancada ou ferramenta de teste NOVA só nasce quando existe **defeito
medido no ar** que ela teria pegado (…) **'Pode acontecer' não basta**"*. **Medido hoje, e é o que fecha a questão:**
os dois bancos da ilha dão **99 de 99 publicáveis com `url_busca` e `url_busca_produto`, zero intestável** — o
portão sairia verde, como o próprio texto previa. A errata do parágrafo acima já havia **anulado por medição** o
defeito que originou o item. **Nada de trabalho feito se perde: o item nunca foi executado**, e o gatilho fica
escrito — no dia em que um registro publicável entrar sem piso, existe o defeito com URL e data, e a 31.2
autoriza o portão.

### Números de banco que o próprio portão da ilha desmente

**24. `ilhas/aquametria/ARVORE.md` — "34 de 40 no portão do catálogo e 34 de 40 no portão de página, com os mesmos
6 barrados". CORRIGIDO para 35 e 5, rodando a régua da própria ilha.**
`python3 ferramentas/validar-especies.py` imprime hoje `catalogo-de-especies 35 apto(s), 5 barrado(s)` e
`pagina-especie 35 apto(s), 5 barrado(s)`. O registro que entrou foi o **guppy**, em 21/10 às 12h3xZ, quando o
`aviso [E15]` saiu da linha de base — está escrito no `PROMPT.md` desta ilha (*"entrou no catálogo (34 → 35)"*).
**Este arquivo não foi tocado desde 12/10 e a mudança é de 21/10.** Corrigido nos três lugares em que o número
aparecia.

**25. `ilhas/aquametria/ARVORE.md` — "Os dois vivíparos MAIS vendidos do Brasil são (…) barrados pelo portão (…)
o guppy tem duas urls de um corpo só (E15)". CORRIGIDO por ponteiro: desde 21/10 é UM.**
Medido: os cinco barrados são `danio-margaritatus`, `ancistrus-cirrhosus`, `poecilia-sphenops`,
`trichopodus-leerii` e `trichopodus-trichopterus` — **o guppy não está entre eles** —, e os quatro avisos
restantes são E21, E25, E27 e E21, **nenhum E15**. Sobrou o molly. A célula fica como ato datado de 14/09; o que
mudou foi o mundo.

**26. `ilhas/aquametria/PROMPT.md` — critério de pronto que nomeia 12 itens quando o banco tem 11, e é a terceira
contagem que o mesmo critério carrega. CORRIGIDO para 11.**
Medido varrendo os cinco `produtos-*.json`: `afiliado.intestavel: true` em **11** registros, nomeados um a um no
ponteiro. O décimo segundo era o `eheim-classic-250-2213`, consertado em **14/10 às 19h16Z** pelo campo
`codigo_catalogo` da §25.9 — e `dados/divida-25-4-b-2026-10-14.md` já manda, na própria abertura: *"Onde este
documento disser 12, 35 ou 'falta um', some este parágrafo"*. A linha acima, na mesma seção, ainda diz **14**.
**Três números para um conjunto só, e o parêntese de 05/10 já havia escrito a lição: parar de escrever a
contagem.**

**27. `ilhas/aquametria/PROMPT.md` — "os 30 portões que rodam sem rede / mais os seis / mais os dezesseis". OS TRÊS
NÚMEROS SAÍRAM, e o erro do primeiro era de 2,4×.**
Medido rodando o próprio comando: `bancada.py --lista` imprime **73** portões sem rede, `--no-ar` sobe para **84**
(mais **11**) e `--navegador` para **91** (mais **18**). **A causa está na frase imediatamente abaixo deles**, que
é a razão de ser da ferramenta: ela varre a pasta, e *"portão novo entra na bancada no dia em que é escrito, sem
ninguém se lembrar dele"*. **Contagem digitada ao lado de um contador automático envelhece a cada portão novo.** A
robometria escreve o mesmo bloco com a data ao lado (*"eram 38 em 18/09; contados 42 em 12/10"*), que é o jeito
certo quando o número tem de aparecer — aqui ele não tem: quem quiser roda `--lista`.

---

## BAIXO — CORRIGIDO (7)

**28. `bussola/fila.md:3` — "Última rodada que mexeu aqui: 007 (21/10/2026, noite)".** Corrigido: `git log` mostra
**quatro** commits de 22/10 depois daquela linha.

**29. `ilhas/aquametria/PROMPT.md` — "78 itens, uma linha por registro".** Corrigido para *"um objeto por
registro"*: o arquivo é JSON indentado e tem **1.817 linhas** para 78 registros, ~23 por item. A intenção —
nenhum registro agrupado — está cumprida; a forma descrita não era a do arquivo. **É a família do precedente dos
"2,8 milhões de produtos" que eram 100.000 registros**, em escala pequena e no mesmo lugar: linha contada como
registro.

**30. `ilhas/clubedomosaico/ARVORE.md` — "`/materiais/alicates/` precisa de 3 filhas".** Corrigido para
`/materiais/alicates-e-corte/`: a seção 2 do mesmo arquivo registra que *"`materiais/alicates` virou
`materiais/alicates-e-corte`"*. Com o nome velho, a ilha tinha **três** endereços escritos para a mesma camada em
vez de dois.

**31. `ilhas/clubedomosaico/DESIGN.md` — duas citações por NÚMERO DE LINHA que já apontavam para outro assunto.**
Corrigido para citação pela frase. `PROMPT.md:356` hoje é uma linha sobre a âncora da 30.4; `ESTADO.md:301` é uma
linha sobre a sessão logada do Shopee Afiliados. **Esta ilha já tinha escrito a regra contra isso em 14/09/2026** —
*"número de linha envelhece a cada edição do arquivo, então a referência passa a ser pela frase"* — e este arquivo,
escrito em 05/10, repetiu o padrão que aquela correção proibiu.

**32–33. `bussola/dossies/som-automotivo/DOSSIE.md` — "Os 40 candidatos" são 41, e "Sem DNS (38 de 40)" são 39 de
41.** Corrigidos os dois. Recontado: 7 + 10 + 8 + 7 + 9 = **41** nomes nas cinco famílias, dois com DNS. O item
estava na lista de herdados **desde 14/09** — **seis semanas** —, e é contagem, não decisão. **Consequência que
vale registrar:** 41 estoura o teto de "30 a 40 candidatos" da §5(d) da `BUSSOLA.md`, sem efeito sobre a escolha,
que foi `ohmetria` e está paga.

**34. `ilhas/clubedomosaico/ESTADO.md`** — o cluster de contagens de URL recebeu, junto, a nota de que é a terceira
vez que os parágrafos de 09/10 envelhecem atrás de um cabeçalho alargado em 12/10.

---

## MÉDIO — PRECISA DO RAPHAEL (14)

**35. A `fila.md` do Raphael acabou no item (3), e o foco não tem item (4).** `foco.md` diz, com todas as letras:
*"A fila do Raphael acaba aqui: **NÃO há item (4)**, então a próxima troca de foco precisa de decisão nova dele"*.
A jornadafly está em foco desde 22/10 e **a fila de arquivo dela esgotou em 23/10** — o próprio `foco.md` registra
que *"a execução seguinte que encontrar esta ilha em foco, com `rede: BLOQUEADA` e sem WordPress, **não tem bloco
para abrir**"*. **São três dias de Fundação sem destino escrito, e nenhuma régua do Arquipélago resolve isso:** a
1.2 proíbe pegar outra ilha, o molde da 32 já não fura o foco (as três estão conferidas desde 23/10) e a ilha em
foco não tem trabalho que a Fundação alcance. **É a decisão mais urgente desta auditoria** e é só dele: ou os
passos 2 a 8 da seção 11 na jornadafly, ou `ilha: nenhuma`, ou um item (4).

**36. `ilhas/jornadafly/VOZ.md` e `bussola/dossies/viagem-experiencia-icone/VOZ.md` mandam, pela §22.2, um lockup e
uma cor que o `DESIGN.md` declarou descartados — e os dois arquivos são idênticos.** O `VOZ.md` prescreve o logo
como *"`JORNADA` em 700 + `fly` em 400, coladas"* e *"o índigo da marca aparece uma vez por tela"*; o `DESIGN.md`
diz que a marca oficial, trazida pelo Raphael em 14/09, é o **monograma em "J" com traço ascendente azul**, com
sinal **`#378AD0`**, e que o desenho do dossiê *"está descartado (…) para ninguém 'restaurar' achando que corrige
um desvio"*. **E a §22.2 entrega o desempate ao arquivo velho:** *"Quando os dois discordarem, é o `VOZ.md` que
decide"* — regra que o próprio `DESIGN.md` repete. Herdado de 12/10; **2 semanas**. Muda identidade: §22.6.

**37. O `alicate` da clubedomosaico tem três endereços escritos para a mesma camada, e um deles está no ar.**
`PROMPT.md` (09/10) manda a página de consulta de produto nascer *"filha direta de `/materiais/` (nível 2),
página-folha (…) a 16.5 não se aplica a ela"*, e `/materiais/alicate-para-mosaico/` está no ar desde 09/10;
`ARVORE.md`, `VOZ.md` e o registro da casca dizem `/materiais/alicates-e-corte/`. A 12.1 proíbe mover URL
publicada, então as duas leituras não podem valer juntas. Herdado de 21/09; **5 semanas**. §19.2: estrutura de URL
não se conserta sem decisão. *(O terceiro endereço saiu hoje — achado 30.)*

**38. A 16.6 escrita no `PROMPT.md` da clubedomosaico proibiria as oito páginas que a §30 do contrato autorizou.**
A ilha escreve que *"filha sozinha pendurada em `/materiais/` é o cluster ralo que a 16.6 proíbe"* (07/10) e, duas
seções adiante, que a página de consulta de produto nasce exatamente assim (09/10). Medido no contrato: a §30.1
isenta essa página **só da 16.5**; **nada a isenta da 16.6**. Lida ao pé da letra, a frase da ilha desqualifica uma
nona consulta legítima — classe 4, critério escrito a partir dos casos existentes. Herdado de 12/10; **2 semanas**.

**39. M9 — a camada de coleção da Loja tem três desenhos de URL escritos e um publicado, e agora a primeira
coleção tem as três filhas que a 16.5 pede.** Contado hoje em `dados/pecas.json`: **quatro das cinco peças estão na
coleção `parede`**. O número que faltava chegou; o desenho continua por escolher entre `/loja/colecao/<termo>/`,
`/loja/<termo>/` e `/loja/<uso>/` — e os termos reais que a artesã gravou (`parede`, `presentes`) não são nenhum
dos três conjuntos de nomes escritos. **Mexe em peça da mãe dele e em estrutura de URL.** Herdado de 21/09;
**5 semanas**.

**40. `/metodologia/` na raiz: duas ilhas decidiram por escrito que a §16.1 a cobre, e a §21.7 diz o oposto, com
ela nomeada.** `aquametria/ARVORE.md` (13/09 19h35) atribui a permanência à §16.1; a §21.7, escrita **12 minutos
depois** no mesmo dia, diz *"**O que a exceção NÃO cobre** (…) qualquer outra página da raiz, **`/metodologia/`
incluída**"*, e a §16.1 lista cinco nomes que não a incluem. `robometria/ARVORE.md` repete a mesma atribuição e
**cita a própria lista de cinco que a exclui**. Consertar exige emendar a §16.1 ou mover URL publicada (§12.1
proíbe). Herdado de 14/09; **6 semanas**.

**41. §20.4 e §22.8 mandam toda ilha ganhar um portão que a §31.2 proíbe criar.** A §20.4 (12/10): *"Toda ilha com
Sync copia esse portão"* (`conferir-desembarque.py`) — a robometria registra em 23/10 que **não o tem**, e que leu
o log à mão com **13 de 13 `ok`**, que é a prova de que não há defeito no ar. A §22.8: *"Cada ilha ganha
`ferramentas/teste-desenho.mjs`"* — medido: **não existe em nenhuma das três**. A §31.2 (21/10): portão novo só
nasce com defeito medido no ar. **É o contrato contra o contrato, e nenhuma edição de ilha resolve.**

**42. A §31.6 manda item de prioridade alta abaixo de 7 em 10, e o despacho de 21/10 declarou que não é.** A
§31.6: *"Abaixo de 7 em 10, vira item de despacho com prioridade alta"*, sem condição. O despacho da aquametria,
escrito **7 horas depois** da §31, mediu **7 de 24 (29%)** e escreveu *"este item **não é conserto, é vigilância**
(…) hoje não é, porque o número já virou"*. Recontei do `REGISTRO.md` e a aritmética está certa (24 execuções na
janela 14→21/10, 2+5=7 entregas no ar). O corte pela data de nascimento da regra é defensável — aplicá-la a uma
janela que começou antes dela é retroativo —, mas **quem dá essa ressalva à §31.6 é ele, e a decisão muda a fila**.

**43. O `esquema-banco.json` da jornadafly não exige o piso que a §25.2 declara inegociável, e três itens
publicáveis estão sem ele.** Medido: a chave `afiliado.url_busca` **não existe** em 4 de 4 registros de
`dados/experiencias.json` (3 publicáveis), e `afiliado.degrau` falta nos mesmos 3. A entidade AFILIADO do esquema
exige seis campos e **nenhum deles é `url_busca`, `degrau` ou `conferido_em`** — o esquema é o portão, e o portão
não pergunta pelo piso. Contra a §25.2: *"Item sem `url_busca` é defeito da 19.1, sempre, em qualquer degrau. **Não
existe item publicável sem piso**"*. **Mas o esquema declara, por escrito, por que a escada da 25.1 não serve a um
nicho de serviço** (`por_que_a_escada_da_25_1_nao_serve`), e troca-a por uma própria de três degraus — e os quatro
itens têm `url_busca_produto` e saída de compra, só não rastreável; o arquivo conta isso em
`itens_com_piso_nao_rastreavel: 4`, que eu recontei e confere. **Duas leituras defensáveis, e a escolha é entre
emendar a §25 para nichos de serviço ou emendar o esquema.** Herdado de 05/10; **3 semanas**.

**44. O `esquema-banco.json` da ohmetria declara `url_busca.obrigatorio: false`, com uma nota que contradiz a §25.2
em uma linha.** A nota: *"quando falta, o item tem saída de compra e não tem comissão — é **dívida de comissão,
nunca defeito de página**"*. A §25.2 diz o contrário com todas as letras. Hoje custa zero (o banco tem **0**
registros, medido), e é exatamente por isso que custa: **a trava está escrita para o dia em que o banco encher.**

**45. SEGREDO — o token do Sync em texto puro CRESCEU, e o crescimento é estrutural.** Dívida conhecida desde
14/09. Medido hoje: **3 tokens distintos, 3 ilhas, 4 arquivos, 16 linhas**, contra **12 linhas** em 12/10. **+4
linhas, todas em `ilhas/aquametria/REGISTRO.md`**, que é append-only por desenho — cada ronda que cola a URL
completa do Sync acrescenta uma cópia. **A dívida não está parada: ela cresce ~4 linhas por quinzena sozinha.** A
§25.6 já nomeia o conserto (*"esse mesmo documento é a casa dos tokens do Sync, que hoje estão em texto puro no
repositório público e **precisam ser rotacionados**"*) e ele é dele: rotacionar nos três Code Snippets e ler do
documento `arquipelago-credenciais` no Drive. **Rotação é o único conserto real — os valores já estão na história
do git.** Nenhum valor foi escrito aqui, em commit nenhum, nem no relatório. **E duas coisas baratas continuam não
feitas:** o `.gitignore` tem 5 linhas e nenhuma menção a `.env`, `*.pem`, `*.key` ou JSON de conta de serviço; e o
`ilhas/_modelo/PROMPT.md` tem **zero** menções a segredo, token ou credencial — **toda ilha nova nasce repetindo o
padrão, e o `PROMPT.md` é o arquivo que toda execução abre.** Herdado de 14/09; **6 semanas**.

**46. SEGREDO — o e-mail pessoal da artesã está em 9 arquivos versionados, e dois são snippet de produção.**
Registrado em 14/09 como **um** arquivo (`PROMPT.md`). Medido hoje: **25 ocorrências em 9 arquivos**, entre eles
`snippets/clubedomosaico-atelie.php` e `snippets/clubedomosaico-leads.php` — **código que vai ao ar** — e
`dados/despachos.md`. Os próprios testes da ilha já têm a convenção `@exemplo.com` em outras linhas, que é o que
deveria substituí-lo nos fixtures. **Envolve dado pessoal de terceiro: registro, não conserto.** Herdado de 14/09;
**6 semanas**. *(De passagem, e menor: o e-mail do próprio Raphael em 5 linhas, uma delas em snippet de produção.)*

**47. A `BUSSOLA.md` §5 declara a Bússola PAUSADA desde 16/09, e ela rodou duas rodadas e recebeu duas leis novas
em 21 e 22/10.** O texto: *"**BÚSSOLA PAUSADA EM 16/09/2026** (…) a rotina semanal está desligada (…) o gatilho
combinado é **uma ilha terminada e dando dinheiro**"*. Desde então: rodada 006 e rodada 007 (21/10), a §3.0-c
(21/10) e a §3.0-d (22/10), as duas decisões nomeadas dele. A `fila.md` ainda cita a pausa como razão de não haver
urgência (*"a Bússola está pausada desde 16/09/2026 e nenhuma ilha ia nascer hoje"*). **Nenhuma ilha terminou e
nenhuma deu dinheiro**, então o gatilho escrito não disparou — e a rotina rodou. **Ou a pausa acabou e a linha tem
de sair, ou ela vale e as rodadas foram exceção: as duas leituras são defensáveis e a §5 é lei dele.**

**48. `ilhas/ohmetria/ESTADO.md` continua sem `ultima_ronda` e sem `bloqueada_por`.** Medido com a régua de
presença da §2: é a **única** dos seis cabeçalhos que falha, e falha nos dois campos. A própria §2 registra a
dívida desde **30/09** e explica por que não a consertei: *"Quem fecha bloco conserta o cabeçalho da ilha que
reservou, **e só dela**"* — a ilha não recebe execução desde 15/09. **Dono designado que não chega.** Herdado de
16/09; **6 semanas**. *(Na mesma medição: `clubedomosaico` traz `primeira_indexacao: 'desconhecida'`, que não é
"data ou null" como a 21.6 pede — e o `PAINEL.md` já publica isso como "sem registro".)*

**49. A régua de presença de campo da §2 não cobre os dois campos que a §21.6 exige.** Corrigi hoje o **molde**
(achado 10), e não a régua: a linha de uma linha confere os oito campos que a **§1** lê para escolher a ilha, e
ampliá-la para dez muda o que um portão reprova. **Ou se amplia, ou se escreve na §2 que ela não cobre a 21.6** —
e isso é escolha.

**50. O `dados/PAINEL.md` continua escrevendo narrativa, histórico e opinião, que a §23.3 proíbe.** Medido: o
painel de 23/10 tem seis parágrafos de prosa explicativa — *"POR QUE DUAS ILHAS, e a escolha está escrita porque a
primeira metade dela estava errada"*, *"O QUE A MEDIÇÃO DE QUEM CONSTRUIU NÃO PODIA ACHAR"* — e a §23.3 é literal:
*"Narrativa, histórico, opinião, projeção e elogio (…) Se uma linha do painel só faz sentido com um parágrafo de
explicação, ela não é do painel"*. Herdado de 12/10; **2 semanas**. *(A prosa é boa; o lugar dela é o
`REGISTRO.md`. Decidir se a §23.3 continua valendo assim é dele.)*

---

## O QUE VERIFIQUEI E NÃO É ACHADO

**Dito porque zero achado é resultado, e porque três suspeitas minhas morreram na medição:**

- **`robometria/ESTADO.md` — "95 − 28 ≠ 71" era FALSO POSITIVO, e a prova é contável.** As duas frases vizinhas
  usam réguas diferentes e as duas estão certas: medi os 28 ids de `chaves-do-navegador-2026-09-20.json` (28
  exatos, 22 peças e 6 modelos, como o texto diz) contra os dois bancos — **4 têm ficha e 24 não**. Logo 95 − 28 =
  **67 com link curto** e 95 − 24 = **71 que rendem comissão** (ficha OU busca encurtada), e o `PROMPT.md` fecha o
  círculo com *"'saída crua, sem rastreio' foi de 24 para 0 em 95 publicáveis"*. **Nada a consertar.** Estava na
  lista de herdados como "não verificado" desde 05/10; sai dela hoje, verificado.
- **O menu "Guias" da robometria está RECONCILIADO em quatro lugares, não é defeito.** `ARVORE.md` escreve a
  condição e o motivo: *"O `VOZ.md` descreve Peças · Modelos · Guias. **Hoje ele é Peças · Sucção · Como
  conferimos**, porque esses três são onde a pessoa resolve o problema (…) Quando `/pecas/` e `/succao/`
  nascerem, `/guias/` entra"*, e o `PROMPT.md` e o comentário da casca repetem. `/succao/` não existe, então o
  estado atual **obedece** ao que está escrito. Sai da lista de herdados.
- **`aquametria/ESTADO.md:5` — `piso: abaixo` RESOLVIDO.** Hoje lê `piso: atingido`, e **está correto**: 52 URLs
  (≥ 40) e `primeira_indexacao: 2026-09-09` + 21 dias, vencido em 30/09. Sai da lista.
- **Os 80 JSON de `ilhas/*/dados/` parseiam, 0 falham.** E o defeito do precedente — contagem inflada por quebra
  de linha dentro de campo de descrição — **procurei onde ele cabia e não existe**: `clubedomosaico/pecas.json`
  tem `\r\n` dentro de `descricao` nas cinco peças e o `total: 5` bate com `len(pecas)`; nenhum contador do
  repositório deriva de `splitlines()` sobre campo de dado.
- **O piso da §25.2 está inteiro nas três ilhas no ar**, recontado: aquametria **78 de 78** com `url_busca`,
  robometria **99 de 99** (54 peças + 45 modelos, zero intestável), clubedomosaico **43 de 43**. Os **133**
  publicáveis sem `url_produto` do arquipélago inteiro **têm, todos os 133, o motivo escrito** — é dívida
  declarada e contada, exatamente como a 25.4-b.1 manda, nunca violação silenciosa.
- **O `MAOS-LOG.md` (365 KB) está limpo de valor de segredo.** Os 12 acertos de palavra-chave são prosa sobre
  higiene de segredo; os 32-hex são SHA de git e md5 de arquivo. E as `ferramentas/*.py` leem toda credencial do
  ambiente, nunca de literal.
- **O despacho do molde da §32 está FECHADO nas três ilhas e nenhuma alega furar o foco.** Conferido por `grep`
  nos três `PROMPT.md`: o único acerto vivo de "fura o foco" é na robometria e o motivo declarado lá é o caso
  **ALTO** da 1.2, não o molde.
- **O `PROMPT.md` da jornadafly é o contraexemplo saudável, e vale copiar o mecanismo.** Ele mantém uma lista de
  portões escrita à mão e, ao lado dela, o aviso *"quem acrescentar o sétimo e não o escrever aqui cria exatamente
  o defeito que esta ilha acabou de pagar num andar abaixo"*. **O aviso foi cobrado duas vezes e funcionou as
  duas** — de seis para oito em 22/10 e de oito para dez em 23/10, com os novos escritos na mesma passada, e o
  título corrigido de "oito" para "treze" pelo próprio autor. É o único lugar do repositório onde uma contagem à
  mão **não** envelheceu, e a razão é que o gatilho de aposentá-la está escrito junto dela.

---

## HERDADOS — abertos, com o tempo na mesa (sem reabrir discussão)

| item | 1ª aparição | pendurado |
|---|---|---|
| Token do Sync em texto puro — hoje **16 linhas**, contra 12 em 12/10 (achado 45) | 14/09 | **6 semanas** |
| E-mail pessoal da artesã — hoje **9 arquivos**, dois de produção (achado 46) | 14/09 | **6 semanas** |
| `fila.md` sem critério de desempate: o nº 2 traz 3,92 e o nº 3 traz 3,94 | 14/09 | **6 semanas** |
| `/metodologia/` na raiz: §16.1 × §21.7, duas ilhas do lado velho (achado 40) | 14/09 | **6 semanas** |
| As **cinco** regras de processo propostas pelas auditorias e nunca inseridas (10.x, 10.y, 8.z, 10.z, 10.w) | 14/09 | **6 semanas** |
| `ohmetria/ESTADO.md` sem `ultima_ronda` e `bloqueada_por` (achado 48) | 16/09 | **6 semanas** |
| Altura do cabeçalho do Clube do Mosaico (M10) — **FECHADO HOJE**, achado 18 | 14/09 | *encerrado* |
| Dossiê do som automotivo: "40 candidatos" são 41 — **CORRIGIDO HOJE**, achados 32–33 | 14/09 | *encerrado* |
| Clube do Mosaico com dois (três) desenhos de URL para a mesma camada — M9 (achado 39) | 21/09 | **5 semanas** |
| `alicate`: duas mães escritas, uma no ar (achado 37) | 21/09 | **5 semanas** |
| A regra das 48 h da `BUSSOLA.md` §5 que o dono designado não tem mãos para cumprir | 05/10 | **3 semanas** |
| `jornadafly/esquema-banco.json` sem `url_busca` nem `degrau` como chave (achado 43) | 05/10 | **3 semanas** |
| `rodadas/005.md:40` "todo índice cai entre 0,20 e 0,35 ponto" falha em três linhas | 05/10 | **3 semanas** |
| P7 fechada no `ohmetria/DESIGN.md` e viva na `fila.md` e na `rodadas/005.md` | 05/10 | **3 semanas** |
| `BUSSOLA.md` §3.0-b fixa um corte de 50% numa linha e nega tê-lo fixado na seguinte | 05/10 | **3 semanas** |
| `robometria/ESTADO.md` "95 − 28 ≠ 71" — **VERIFICADO HOJE, falso positivo** | 05/10 | *encerrado* |
| Menu da Robometria pedindo `/guias/` — **VERIFICADO HOJE, reconciliado por escrito** | 05/10 | *encerrado* |
| `aquametria/ESTADO.md` `piso: abaixo` — **VERIFICADO HOJE, resolvido e correto** | 12/10 | *encerrado* |
| §22.7 manda a Sentinela consertar na hora cinco coisas que a §19.2 e a §12 proíbem | 12/10 | **2 semanas** |
| `clubedomosaico/PROMPT.md` 16.6 × as oito páginas da §30 (achado 38) | 12/10 | **2 semanas** |
| `jornadafly/VOZ.md`: lockup e cor descartados, e a §22.2 dá o desempate ao velho (achado 36) | 12/10 | **2 semanas** |
| `dados/PAINEL.md` escreve narrativa, que a §23.3 proíbe (achado 50) | 12/10 | **2 semanas** |

**Não verificados que ninguém verificou:** `lotus-512.png` com 9.095 bytes contra os 8.770 que três documentos
declaram; `aquametria/ARVORE.md`, *"falsa em 14 dos 36 registros"*; qual `sub_id` os 58 links de
`malha-pecas.json` carregam (a §25.8 proíbe o único caminho que diria); `casca-fatos.json`
`total_de_fontes: 141` — hoje reproduzi **134** dos 141 (nível 3 = 91 e nível 4 = 43, exatos nos dois bancos) e
**não** os 7 do nível 7, porque a regra que mapeia tipo→nível não está no arquivo; as 29 fichas no ar da
aquametria contra os 40 registros do banco (é contagem de página, não de registro — exige o site).

**Observação de processo, repetida porque o número só cresce:** a lista "Precisa do Raphael" do `ESTADO.md` da
clubedomosaico tinha, hoje, **dois** itens cuja condição já havia fechado — o `foco.md` e o M10 — e os dois saíram
nesta passada. A lista dele continua sem conter **um único** item desta tabela de herdados. **As pendências mais
antigas do Pente Fino não estão em nenhum lugar que ele leia**, e é por isso que "6 semanas" aparece cinco vezes
acima.

---

## O PADRÃO

Vinte e oito consertos, uma forma só, e esta rodada mediu **onde** ela mora com uma precisão que as anteriores não
tinham: **quem corrige um ponto não vê o vizinho — e "vizinho" não é distância no arquivo, é distância na
atenção.** Os três consertos mais puros de hoje provam isso em três escalas. A `fila.md:229` ficou errada a **doze
linhas** da correção que a declara falsa, escrita **pelo mesmo commit**, nas linhas de contexto do próprio hunk. A
clubedomosaico escreveu `urls_publicadas: 32` no cabeçalho e deixou "31 URLs" **três telas abaixo, na mesma
seção**, no mesmo dia. A §2 do contrato ficou sem os dois campos que a §21.6 exige porque o `_modelo` foi
consertado e **a seção que o molde diz obedecer** não foi aberta. Perto, longe, e em outro arquivo: a mesma falha.

**O que esta rodada acrescenta, e é a parte que nenhuma régua do projeto cobre hoje: a correção é o momento de
maior risco do documento, não o de menor.** Quatro dos achados de hoje foram criados *por* uma correção —
a gravação de 22/10 que remediu o M e não releu o quadro que o governa; a de 12/10 que inseriu um ponteiro e foi
atropelada por três linhas novas **no mesmo dia**; a de 09/10 que fechou um item e deixou a cópia dele 2.600
linhas abaixo; e a 32.5-b, que nasceu no contrato porque uma régua certificou **as páginas que o autor abriu**.
Quem conserta chega com a atenção toda no ponto, e é exatamente nesse estado que o resto do documento fica
invisível. **Vigilância não resolve, e já são quatro relatórios dizendo isso.** O que resolve é a régua que mede
sem ler.

E há um achado de método que vale mais que qualquer um dos 28: **as contagens que não envelheceram são as que têm
um contador ao lado.** Os três números de bancada da aquametria estavam errados por 2,4× ao lado de uma ferramenta
que os imprime com um `--lista`; o "34 de 40" do `ARVORE.md` caiu rodando a `validar-especies.py` da própria ilha;
o "20 dos 41 itens" morreu contando cinco arquivos JSON. **Nenhum dos três exigiu julgamento — exigiu rodar o que
já estava escrito.** E o único lugar do repositório onde uma lista à mão **não** envelheceu, o `PROMPT.md` da
jornadafly, é o único que carrega, junto dela, o gatilho escrito de quando aposentá-la.

> **Proposta de regra, para o `ARQUIPELAGO.md`, seção 10 — e ela é um recorte da 10.w de 05/10, não uma sexta
> proposta:**
>
> **10.w-b — NÚMERO QUE UMA FERRAMENTA DO REPOSITÓRIO SABE CONTAR NÃO SE ESCREVE EM PROSA; E QUANDO TIVER DE SER
> ESCRITO, NASCE COM A DATA E COM O COMANDO QUE O RECONTA.** Toda afirmação numérica sobre o próprio repositório —
> quantos portões, quantos registros, quantas URLs, quantos passam numa régua — ou sai de um comando na hora da
> leitura, ou carrega, na mesma frase, a data da medição e o comando que a refaz. **Contagem digitada ao lado de um
> contador automático é a forma mais paciente de defeito que esta fábrica produz: ela não reprova nada, não
> aparece em portão nenhum, e envelhece sozinha a cada commit que alguém faz do outro lado do arquivo.** Medido em
> 26/10/2026: dos 28 consertos daquele dia, **nove** eram exatamente isso, e os nove foram desfeitos rodando uma
> ferramenta que já existia na pasta da própria ilha.

Não inserido: regra nova de política é decisão do Raphael.
