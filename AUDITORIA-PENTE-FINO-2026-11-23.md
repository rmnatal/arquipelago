# AUDITORIA PENTE FINO — 2026-11-23

Varredura de coerência do corpo de regras do `rmnatal/arquipelago`, rodada na segunda de manhã **antes da
Bússola**, do estado real do `main` (`a56ca24`, 20/11/2026 16h32 de Brasília — 19h32Z).

**Clone COMPLETO, não raso** (`.git/shallow` não existe; medido antes de contar, pela régua da **1.1**). Contei
sobre os **1.633** commits do `main`. A janela desde a auditoria anterior (16/11, `dbc8b21`) tem **103 commits**.

---

## O QUE FOI LIDO, E COMO

**Lidos inteiros, linha por linha (12):** `ARQUIPELAGO.md` (1.726 linhas na leitura) · `bussola/BUSSOLA.md` (412) ·
`bussola/cacados.md` (203) · `bussola/despacho-viagem.md` (67) · `foco.md` · `README.md` ·
`AUDITORIA-PENTE-FINO-2026-11-16.md` (301) · `dados/PAINEL.md` (50) · `ilhas/_modelo/PROMPT.md` ·
`ilhas/_modelo/ESTADO.md` · `bussola/dossies/rodametria/VOZ.md` · `ilhas/rodametria/VOZ.md`.

**Lidos em parte, nos trechos nomeados (9):** `bussola/fila.md` (cabeçalho, mapa de seções, "Ilhas nascidas",
"Dívida desta fila", "Dossiês prontos" e o fim) · `bussola/oportunidades/rodametria.md` ·
`ilhas/ohmetria/PROMPT.md` · `ilhas/rodametria/ESTADO.md` e `PROMPT.md` · `ilhas/jornadafly/VOZ.md` e `DESIGN.md` ·
`ilhas/robometria/ARVORE.md` · `dados/despachos.md`.

**Medidos por régua ou varredura, sem leitura integral:** os **7** `ilhas/*/ESTADO.md` pela régua de presença da
**§2** mais os dois campos da **21.6**, antes e depois das minhas edições · os **96** `ilhas/*/dados/*.json` por
`json.load` e pela varredura do piso da **25.2/25.4-b**, registro por registro, com `publicar`, `gerado_por` e
`status` lidos · os **4** `manifest.json` pela régua do item 1 da **20.7** · os **34** snippets e as **4** cascas
pela presença do `gtag`, do filtro de versões da 20.7(2), da seção da cura da 29.4 e dos campos da 29.4-b/29.4-c ·
os **26** arquivos de lei de ilha (`PROMPT.md`/`ESTADO.md`/`VOZ.md`/`DESIGN.md`) por varredura de token, endereço,
mandato e causa-de-impossibilidade herdada · os **15** arquivos de `bussola/dossies/` por **diff contra a cópia
viva da ilha** e por varredura de âncora de M · os **70** caminhos de arquivo citados no `ARQUIPELAGO.md`,
conferidos um a um contra o disco · as referências de subseção do contrato, conferidas contra os **119**
cabeçalhos declarados · e os **771** arquivos versionados por varredura de segredo (token, e-mail, chave).

**Não verificado, e dito como tal:** os `PROMPT.md` da **aquametria, clubedomosaico, robometria e rodametria**
não foram lidos inteiros — **8.256 linhas somadas** —, foram varridos por régua. Os `REGISTRO.md` e o
`MAOS-LOG.md` não entram nesta varredura por desenho: são append-only e histórico. **Nada foi medido no ar:**
esta passada não abriu página de ilha nenhuma, e por isso toda afirmação abaixo sobre o que uma página serve é
citação do que a ilha mediu, nunca medição minha.

---

## GRAVE — decisão tomada com base errada (0)

**Nenhum.** E o lugar onde eu esperava achar um foi medido e está são:

- **A tabela "Ilhas nascidas" da `fila.md` está incompleta (achado 1) e isso NÃO contaminou caça nenhuma.**
  Medido antes de graduar o achado: `bussola/cacados.md` traz, em **19/11/2026**, a linha *"triciclo elétrico ·
  **já é nicho da Rodametria** (mobilidade elétrica) · 246 mil/mês"* — a caça reconheceu o nicho como tomado sem
  precisar da tabela, do mesmo jeito que fez com *"aquário (cabeça de produto) · já é ilha (Aquametria)"* em
  27/10. **Nenhuma rodada gastou candidato por causa do buraco.**
- **A régua de dinheiro da Bússola continua longe da Amazon.** Revarrido: as menções em `ARQUIPELAGO.md`,
  `BUSSOLA.md`, `fila.md`, nos 5 dossiês e nos `PROMPT.md` estão **todas** marcadas como a régua derrubada ou
  como a proibição da §7. O defeito que criou este auditor segue fechado nas duas pontas.
- **O corpo da lei da Bússola não mudou desde 16/11**: o único diff em `BUSSOLA.md` e `fila.md` na janela são os
  **ponteiros que a auditoria anterior escreveu**. A ordem "Pente Fino antes da Bússola" está sendo cumprida, e a
  régua que ela vai ler hoje é a de 27/10 com os cinco ponteiros de 16/11 em cima.

---

## MÉDIO — regra inconsistente, sem decisão contaminada (5)

### 1. `bussola/fila.md` — a tabela "Ilhas nascidas" tem CINCO linhas e o Arquipélago tem SEIS ilhas: falta a rodametria, que é a ilha em foco total — **CORRIGIDO (ponteiro)**

**O trecho.** `## Ilhas nascidas`, cinco linhas (robometria, aquametria, ohmetria, jornadafly, clubedomosaico), e
a nota do Pente Fino de 12/10/2026 logo abaixo fechando com *"Agora a página conta cinco nos dois lugares."*

**A contradição.** `ilhas/` tem **seis** pastas de ilha (contadas em 23/11/2026). A **rodametria** foi aprovada
por ele em **27/10/2026 às 14h29** — e isso está escrito **nesta mesma página**, quatro parágrafos antes do fim
(*"RODAMETRIA REAPROVADA pelo Raphael, pela regra nova da 0.9"*) —, tem dossiê, ficha, domínio pago, site no ar e
`foco.md` a nomeia desde 27/10. **A página registra a sexta ilha na prosa do fim e conta cinco na tabela.**

**A evidência de que é operacional.** A **seção 4** desta lei manda *"refazer a busca paramétrica dos 5 primeiros
da fila **sem ilha nascida**"*, e é esta tabela que diz quais nichos já têm ilha. E há uma segunda metade, da
ohmetria: a tabela a lista como ilha nascida em som automotivo e **não diz que o `cacados.md` desta mesma pasta
fechou aquele nicho em 22/10/2026** — o ponteiro que a auditoria de 16/11 escreveu sobre isso foi para
`ilhas/ohmetria/`, não para cá, e quem lê a Bússola lê daqui.

**O que fiz.** Ponteiro datado **antes** da tabela, com as duas metades, a evidência e a medição que descarta a
contaminação. **Não acrescentei linha nem nota à tabela:** a **0.3** diz que esta página é registro de medição e a
coluna `Nota` carrega índice e régua, que são medição da Bússola — preencher medição que eu não fiz seria a **3.1**
ao contrário. A linha é da próxima rodada; o buraco fica nomeado para ela.

### 2. `bussola/dossies/rodametria/VOZ.md` e `bussola/oportunidades/rodametria.md` — as duas cópias da Bússola ainda servem as frases sobre HABILITAÇÃO que a ilha proibiu por FONTE em 06/11 — **CORRIGIDO (dois ponteiros)**

**O trecho.** `bussola/dossies/rodametria/VOZ.md`, linha 15 (vocabulário de veredito) e linha 19 (exemplo
aprovado): `"dispensa CNH"`, `"dispensa CNH e placa"`, `"aí precisa de habilitação"`. E
`bussola/oportunidades/rodametria.md`, linha 4: *"a potência que **dispensa CNH e placa**"*.

**A contradição.** Em **05/11/2026** a Resolução Contran nº 996/2023 foi lida no texto oficial, no Chrome dele, e
**ela não tem artigo nenhum sobre CNH** — decide categoria, placa, registro, licenciamento e capacete; quem decide
habilitação é o Código de Trânsito, que esta fábrica ainda não leu na fonte. Em **06/11 às 19h3xZ** o
`ilhas/rodametria/VOZ.md` riscou as duas frases e preservou as originais. **A cópia do dossiê nunca foi relida:**
medido por `diff`, os dois arquivos divergem em **30 linhas**, e a divergência é exatamente esta.

**A evidência, e ela é de três lugares executáveis.** `ilhas/rodametria/dados/constantes.json` declara, na camada
do banco, *"a frase `dispensa CNH` e a frase `precisa de habilitacao` ficam PROIBIDAS na tela"*;
`ferramentas/teste-afirmacao-de-tela.py` e `ferramentas/teste-f1.py` **reprovam** as duas em texto de tela; e o
cabeçalho de `snippets/rodametria-f1.php` as nomeia. **Por que não é cosmético:** o `PROMPT.md` da ilha escreve
que *"errar 'dispensa CNH' num veículo que é ciclomotor manda a pessoa para a rua sem habilitação"*; a **15.1**
manda a Fundação ler o `VOZ.md` **antes de escrever qualquer título, parágrafo ou rótulo**; a linha 4 do
`PROMPT.md` da ilha manda a primeira execução ler o dossiê; e essa mesma linha diz que **"a ficha manda sobre o
dossiê"** — então a cópia de maior autoridade das três é justamente a ficha, que também carrega a frase.

**Por que MÉDIO e não GRAVE, e eu procurei antes de graduar:** as páginas no ar **não** servem as frases — a
própria ilha mediu isso em 06/11 e os três portões as reprovam. Nenhuma decisão foi tomada sobre a base errada.
É o MÉDIO mais caro da semana, não um GRAVE.

**O que fiz.** Ponteiro datado no topo do `VOZ.md` do dossiê e um ponteiro de parágrafo na linha da ficha, os dois
nomeando a fonte, a data, os três portões e qual é o arquivo vivo. **Não apaguei nem reescrevi uma linha:** o
texto de 27/10 é a cópia de nascimento que a **5(g)** manda o dossiê entregar e é o registro de onde a voz veio —
jogá-lo fora apagaria a causa (**28.4**). E não consertei a cópia para igualá-la: a **32.4-c** diz, com todas as
letras, que *"o conserto de uma frase duplicada não é consertar as duas: é a segunda deixar de existir"* — o que
este ponteiro faz é a segunda parar de se apresentar como a voz de hoje.

**A linha do arquivo vivo que isto desmente, e vale guardar:** ele afirma, sobre as duas expressões, *"só este
arquivo ainda as servia"*. **Era falso quando foi escrito**, porque esta cópia existia desde 27/10. É a **20.7**
ao pé da letra: *"duas declarações do mesmo fato começam iguais e só uma sobe"*.

### 3. `ARQUIPELAGO.md` seção 0 — as seções **27** e **28** não estavam na linha de papel NENHUM, e a 28 é a que mantém outro projeto fora deste repositório — **CORRIGIDO**

**O trecho.** O mapa de leitura, lido linha por linha: Fundação `1 a 11, 13 a 18, 20, 21, 22, 24, 25, 26, 29, 30,
31, 32, 33`; as duas Sentinelas; Bússola; Pauta; e `Sempre, para todo papel: 1.2, 2, 3, 4, 10, 18`.

**A contradição.** **27** e **28** não aparecem em nenhuma dessas listas, e as duas são universais no próprio
texto: a **27.3** diz *"NINGUÉM declara feito sem contar no `main`"*, que é o passo de fecho de todo papel; a
**27.2** governa quem toca `dados/*.json`, que é trabalho da Fundação; e a **28.1** diz que *"tudo que envolve o
Arquipélago tem de ser deliberadamente criado dentro do Arquipélago"* — a regra que mantém Real 21, Atlas e o
resto fora deste repositório, e que vale para quem escreve nele, não para um cargo.

**A evidência.** É o **sexto** caso do defeito que esta própria seção já registra cinco vezes (a 1.2 em 16/09, a
1.2-b em 21/09, as três seções da Bússola em 05/10, a 25 e a 30 em 12/10, a 30 na linha da Bússola em 16/11):
*a seção que decide não está na linha de quem decide.*

**O que fiz.** **27** e **28** acrescentadas à linha *"Sempre, para todo papel"*, com a nota datada. A linha das
**Mãos** continua dizendo "nenhuma" **de propósito**: a trava da 28.2 mora no prompt delas, não aqui. O desempate
é o da própria seção: *"errar por ler a mais é barato"*.

### 4. `ARQUIPELAGO.md` 32.9 item 5 — cita a **32.4** para uma régua que mora na **32.8**, e quem a procurar na 32.4 não a acha — **CORRIGIDO (ponteiro)**

**O trecho.** 32.9, item 5 (escrito em 20/11/2026): *"A camada da máquina do estado degradado nasce do MESMO par
que a tela imprime **(32.4)**, e o construtor dela é UM para os dois caminhos."*

**A contradição.** A **32.4** é *"Texto de bastidor da fábrica é proibido na página pública"* — ela não diz uma
palavra sobre montar as duas camadas do mesmo campo. A régua citada é a da **32.8**, cujo título é literalmente
*"A REGRA DE MONTAR A CAMADA DA IA DO MESMO CAMPO QUE A VISÍVEL ESTÁ CERTA E TEM ESTE CUSTO"*, e a do fecho da
**32.4-c**. A 32.8 foi renumerada de 32.6 pelo Pente Fino em **16/11**, quatro dias antes de a 32.9 ser escrita.

**A evidência.** Conferidas as referências de subseção do contrato contra os **119** cabeçalhos declarados: esta é
a única citação do contrato que aponta para uma seção que existe e **não contém a regra citada** — a classe do
ponteiro de 12/10 na 30.2, sobre *"a regra das duas camadas de procedência"*, que também não existia onde era
citada.

**O que fiz.** `(32.4)` → `(32.8, e o fecho da 32.4-c)`, com a nota datada dizendo o que a 32.4 é e por que não é
ela. Nenhuma palavra da régua foi tocada.

### 5. `dados/PAINEL.md` — o painel de 20/11 traz `ultima_ronda` de **13/11** para duas ilhas, contra **18/11** no cabeçalho de cada uma: a 23.4 ao pé da letra — **NÃO CORRIGIDO, a 23.1 proíbe (vai para a próxima ronda)**

**O trecho.** A tabela de ilhas do painel escrito em 20/11/2026 às 15h01Z: aquametria `2026-11-13T15:12Z` e
clubedomosaico `2026-11-13T15:12Z`, na mesma coluna em que a rodametria aparece com `2026-11-18T20:01Z`.

**A contradição.** A leitura semanal de **18/11** gravou `ultima_ronda: 2026-11-18T20:01Z` nos **quatro**
cabeçalhos, no commit `6f6cf76` de 18/11 às 20h10Z — **dois dias antes** do painel. Conferido na árvore do próprio
commit do painel (`696b74d`): as duas ilhas já traziam 18/11 no `ESTADO.md`. A **23.4** é literal — *"todo número
do painel sai de arquivo do repositório ou de medição da própria ronda (…) nunca repete o número velho com cara
de novo"* — e a mesma coluna da mesma tabela foi preenchida do repositório para uma ilha e de uma cópia vencida
para duas.

**O custo, e ele é da §12.** A régua de dívida manda rondar *"a ilha de `ultima_ronda` mais antiga"*. Quem a
aplicar lendo o painel vê duas ilhas com sete dias de atraso onde o repositório diz dois. **Não achei decisão
contaminada:** a ronda de 20/11 foi funda na robometria, e com os valores certos as três irmãs empatariam em
18/11 — a escolha não mudaria.

**Por que não corrigi.** A **23.1** é categórica: *"A Sentinela, ao fim de toda ronda diária (…) **Ninguém mais
escreve nesse arquivo.** A Fundação não escreve, o boletim não escreve."* Eu também não. Fica registrado para a
próxima ronda, que é quem reescreve o painel.

---

## MÉDIO — PRECISA DO RAPHAEL, novos (0)

**Nenhum novo.** Os dois de 16/11 (achados 7 e 8) continuam abertos e estão na lista de herdados.

---

## BAIXO (4)

### 6. `README.md` — "Ilhas atuais" listava cinco e não trazia a rodametria, que é a ilha em foco — **CORRIGIDO**

A lista era a contagem de **16/09/2026** e a rodametria nasceu em 27/10. É a porta de entrada do repositório, e
quem a lia não sabia que a ilha que recebe todas as execuções existe. Corrigido com a contagem de hoje (seis
pastas) e com a ressalva que separa "pasta de ilha" de `estado: viva` (três e três, medidos no mesmo dia) —
porque são contagens diferentes e o texto antigo trocava uma pela outra.

### 7. `ilhas/_modelo/` — o molde que toda ilha nova herda ainda conta **cinco** ilhas; são seis, e este número já foi corrigido de quatro para cinco pelo Pente Fino em 05/10 — **CORRIGIDO**

Duas ocorrências: `PROMPT.md` (*"Use os das cinco ilhas vivas como formato"*) e o comentário de
`primeira_indexacao` no `ESTADO.md` (*"há cinco pastas de ilha em `ilhas/` fora deste molde"*). A segunda carrega,
no próprio texto, o registro de ter sido corrigida de **quatro** para **cinco** em 05/10/2026 — e envelheceu de
novo em 27/10. Recontado e datado, com a ressalva de que a propriedade que a nota afirma (as pastas têm os dois
campos) continua verdadeira para as seis. Reconferi os sete cabeçalhos no parser depois da edição: **7 de 7
parseiam.**

### 8. `ARQUIPELAGO.md` §11 passo 7 — *"que hoje nenhuma ilha mede"* (GA4), e o `gtag` está no fonte de 3 das 4 cascas com Sync — **CORRIGIDO (ponteiro)**

O "hoje" da frase é **11/09/2026**. Contado no repositório: o `gtag` está na casca da aquametria, da
clubedomosaico e da robometria; falta na rodametria. Ponteiro datado, e ele diz o que **não** afirma — que a tag
está no HTML servido —, porque esta passada não mediu o ar e a própria §5 avisa que *"enquanto o `gtag` não
estiver no HTML servido, o zero mede a ausência da tag"*. O que está medido é o fonte, e "nenhuma" é falso no
fonte.

### 9. `ilhas/rodametria/ESTADO.md` — o comentário do campo `piso` diz "10 URLs publicadas" e o campo `urls_publicadas` do mesmo cabeçalho diz **11** — **NÃO CORRIGIDO (§3: ilha em foco, não reservada por mim)**

Dois números para o mesmo fato no mesmo cabeçalho, com um deles vencido desde 16/11 — e o próprio comentário já
carrega o registro de ter sido corrigido de 5 para 10 pela mesma causa, chamando-a pelo nome (*"número velho lido
como fato, o defeito que a seção 4 nomeia"*). O **valor** do campo (`abaixo`) está certo nas duas contagens, 10 e
11 estão longe das 40 da 21.1, então não há decisão em risco. Não corrigi porque a **§3** manda tocar só na pasta
da ilha reservada e esta é a ilha em foco, em construção ativa; e porque a 21.6 dá o campo à leitura semanal.

---

## HERDADOS QUE CONTINUAM ABERTOS — PRECISA DO RAPHAEL (16 de 16)

Sem reabrir a discussão. Nenhum saiu da lista esta semana; dois entraram, vindos dos MÉDIO de 16/11.

| # | o que é | herdado de | semanas | medido hoje |
|---|---|---|---|---|
| 51 | **o desfecho da `ohmetria`** — a Bússola fechou o nicho em 22/10 e a 1.2-b.4 pede um critério pré-registrado com três desfechos que esta ilha nunca recebeu | 16/11 | **1** | os ponteiros de 16/11 seguem no `PROMPT.md` e no `ESTADO.md` dela; a ilha segue com a `ultima_execucao` mais antiga do arquipélago (15/09), `estado: nascendo` e `prioridade: 1` — no dia em que `foco.md` disser `nenhuma`, o passo 4 da §1 aponta para cá primeiro. **E agora a tabela da `fila.md` também ficou nomeada** (achado 1) |
| 52 | **a regra de processo da 3.x proposta em 16/11** — "regra nova fecha a velha no mesmo commit, e fechar é deixar ponteiro onde a velha é EXECUTADA" | 16/11 | **1** | **não inserida**, como manda a regra de regra nova de política. O texto está no fim da auditoria de 16/11 |
| 7 | a 0.8 fecha o portão 4 para nicho de SERVIÇO e a seção 2 e a seção 3 da mesma lei o mantêm aberto | 16/11 | **1** | sem mudança. E `bussola/despacho-viagem.md`, lido inteiro hoje, **reforça a tensão**: a exigência 1 dele diz, com todas as letras, *"a prova de cobertura usa a regra nova (programa acessível com link rastreável), **não Shopee/ML**"* |
| 8 | a 0.6 diz que a SERP vista pela rotina no Chrome dele satisfaz a 30.8; a 30.8 exige olhos | 16/11 | **1** | sem mudança; os dois `alvo` da rodada 008 seguem `provisório` na `fila.md` |
| 36 | `jornadafly/VOZ.md` manda um lockup e uma cor que o `DESIGN.md` declarou descartados, e a §22.2 dá o desempate ao arquivo velho | 12/10 | **6** | `VOZ.md:39` segue com *"`JORNADA` em 700 + `fly` em 400, coladas"*; o `DESIGN.md` segue com o monograma em "J", `#378AD0`, os quatro lockups oficiais e a linha *"ninguém redigita a marca com `<text>` e webfont"* |
| 37 | o `alicate` da clubedomosaico tem três endereços escritos para a mesma camada, e um está no ar | 21/09 | **9** | os três seguem: `/materiais/alicate-para-mosaico/` (13 arquivos), `/materiais/alicates-e-corte/` (6) e `/materiais/alicates/` (3) |
| 38 | a 16.6 escrita no `PROMPT.md` da clubedomosaico proibiria as páginas que a §30 autorizou | 12/10 | **6** | sem mudança |
| 39 | M9 — a camada de coleção da Loja tem três desenhos de URL escritos e um publicado; mexe em peça da mãe dele | 21/09 | **9** | sem mudança |
| 40 | `/metodologia/` na raiz: duas ilhas atribuem a permanência à §16.1, e a §21.7 diz o oposto com ela nomeada | 14/09 | **10** | `robometria/ARVORE.md:64` segue com o veredito próprio (*"fica na raiz"*), e a lista de cinco da §16.1 segue sem ela |
| 41 | §20.4, §20.7, §20.9, §22.8, §29.4, §29.4-b, §29.4-c e §32.5-b mandam toda ilha ganhar um portão que a §31.2 proíbe criar — **e o conflito CRESCEU outra vez** | 26/10 | **4** | eram **4** mandatos em 16/11, são **8**. Medido hoje: `conferir-desembarque.py` (20.4) em **2 de 4** ilhas com Sync · casca servindo versão por filtro + portão comparando (20.7, itens 2 e 3) em **1 de 4** (só rodametria; o item 1, o campo `versao` no manifest, está em **4 de 4**) · `veredito_da_revisao_atrasada` (20.9) em **1 de 4** · cura da porta na casca + `teste-cura-da-porta` (29.4) em **3 de 6** (falta aquametria) · `tem_bloco_wordpress`/`cura_liberada_em_s` (29.4-b) em **2 das 3 que têm a cura** (falta clubedomosaico) · `episodios_vistos` (29.4-c) em **2 de 3** (falta clubedomosaico) · `conferir-32-5-no-navegador.mjs` (32.5-b) em **3 de 6** · `teste-desenho.mjs` (22.8, de 12/09) em **0 de 6** |
| 42 | a §31.6 manda item de prioridade alta abaixo de 7 em 10, e o despacho de 21/10 declarou que não é | 26/10 | **4** | sem mudança |
| 43 | o `esquema-banco.json` da jornadafly não exige o piso que a §25.2 declara inegociável | 05/10 | **7** | **estável**: segue com **6 de 6** registros de `experiencias.json` sem `url_busca`/`degrau`, e o arquivo os conta em `itens_com_piso_nao_rastreavel: 6`. As duas leituras defensáveis continuam: emendar a §25 para nicho de serviço, ou emendar o esquema |
| 44 | o `esquema-banco.json` da ohmetria declara `url_busca.obrigatorio: false` | 26/10 | **4** | lido inteiro hoje: a nota segue, **e o esquema cobra o piso pelo outro campo** — `url_busca_produto.obrigatorio: true` com *"item sem `url_busca_produto`: erro duro, em qualquer degrau"*. O banco segue com **0** registros. Continuam as duas leituras: ou a URL crua é o piso e o encurtamento é bônus (25.2-b), ou o piso é o `url_busca` da 25.2 |
| 45 | **SEGREDO** — token do Sync em texto puro | 14/09 | **10** | **estabilizou pela segunda quinzena: 16 linhas em 4 arquivos, 3 ilhas** (aquametria `REGISTRO.md` 12 e `PROMPT.md` 1, clubedomosaico `PROMPT.md` 2, robometria `PROMPT.md` 1) — o mesmo que em 26/10 e em 16/11. Rotação continua sendo o único conserto real. **Nenhum valor escrito aqui nem em commit.** E as duas coisas baratas continuam não feitas: o `.gitignore` tem **5 linhas** e nenhuma menção a `.env`, `*.pem`, `*.key` ou JSON de conta de serviço; o `ilhas/_modelo/PROMPT.md` segue com **0** menções a segredo, token ou credencial. *(Varredura de hoje: 8 outras ocorrências de padrão de token nas `ferramentas/` foram abertas uma a uma e **as 8 são falso positivo** — `filter_input`, variável de teste, valor de propósito errado num autoteste, e leitura de variável de ambiente.)* |
| 46 | **SEGREDO** — o e-mail pessoal da artesã em arquivo versionado, inclusive em snippet de produção | 14/09 | **10** | **não cresceu.** Medido com a mesma régua nos dois commits: **30 ocorrências em 10 arquivos** em `dbc8b21` (16/11) **e** em `a56ca24` (hoje) — idêntico. A auditoria de 16/11 escreveu "25 em 9" com uma régua mais estreita; **o número de hoje vem com a régua ao lado e não deve ser lido como crescimento** (23.4). Entre os arquivos seguem `snippets/clubedomosaico-leads.php` e `snippets/clubedomosaico-atelie.php`. Envolve dado pessoal de terceiro: registro, não conserto |
| 48 | `ilhas/ohmetria/ESTADO.md` sem `ultima_ronda` e sem `bloqueada_por` | 16/09 | **10** | **é a única dos sete** que falha na régua de presença da §2, e falha nos dois — medido antes e depois das minhas edições. A regra da §2 é clara: quem **reservar** a ohmetria acrescenta os dois no mesmo commit, e eu não a reservei. *(Na mesma medição: `clubedomosaico` segue com `primeira_indexacao: 'desconhecida'`, que não é "data ou null" como a 21.6 pede)* |
| 49 | a régua de presença da §2 não cobre os dois campos que a §21.6 exige | 26/10 | **4** | a régua segue conferindo os **oito** da §1; medido hoje, os sete cabeçalhos **têm** `piso` e `primeira_indexacao`, então ampliá-la não reprovaria ninguém — mas ampliar o que um portão cobra continua sendo escolha |
| 50 | `dados/PAINEL.md` escreve narrativa, histórico e opinião, que a §23.3 proíbe | 12/10 | **6** | o painel de 20/11 tem parágrafos inteiros de prosa (*"A PORTA DE ENTRADA DA SEÇÃO 29, MEDIDA NESTA RONDA"*, *"FECHADO HOJE, E NÃO POR ESTA RONDA"*, o bloco de "Consertos" explicando a causa em cinco linhas). A prosa é boa; a §23.3 é literal. **E agora há um achado de número no mesmo arquivo** (achado 5) |

---

## O QUE VERIFIQUEI E NÃO É ACHADO

Dito porque zero achado é resultado, e porque **seis suspeitas minhas morreram na medição**:

- **O piso da 25.2-c já está de pé na página que o pagou.** A regra é de 19/11 e manda o piso viajar *"no dado
  publicado que a página degradada lê — nunca dentro do bloco opcional, e nunca num arquivo com `publicar:
  false`"*. Medido: o `piso_da_busca` da rodametria vive em `dados/anuncios-por-consulta.json` e em
  `dados/vitrine-de-produto.json`, sob a chave **`nao_nasceram[0]`** — a página sem vitrine carregando o próprio
  piso. Nenhum dos dois tem `publicar: false`, e **os dois estão no grupo `dados` do `manifest.json`**, logo são
  option no ar. Era onde eu mais esperava um achado de dado contra regra nova, e está certo.
- **"o Sync é o mesmo código nas quatro ilhas" é verdade sobre quantas ilhas rodam Sync, e eu fui conferir se era
  afirmação sem procedência.** Medido: três snippets de Sync no repositório (aquametria, clubedomosaico,
  robometria) e a rodametria com o Sync **nascido no site, pela mão dele** — o que a própria 29.4 registra. Então
  quatro ilhas rodam Sync e uma delas não tem o código versionado. **Não promovi isso a achado:** a 29.4 já
  nomeia a exceção com todas as letras, e a 20.9 cita as linhas 473/516/530 declarando que as releu **na fonte do
  repositório**, não na do site. A afirmação está no lugar certo com a ressalva no lugar certo.
- **"não havia navegador" na `PROMPT.md` da rodametria é o registro que a §33 descreve, não uma reincidência.**
  A linha é do commit de **09/11 às 15h05Z** e a §33 foi escrita no mesmo dia, entre 19h1xZ e 19h5xZ — ela nomeia
  aquela ronda como a causa. Precede a regra em quatro horas.
- **As duas filas `links-afiliado-pendentes.md` que existem não violam a 25.6.** A da rodametria abre dizendo
  *"na Shopee o link sai pela Open API na própria coleta e esta fila NÃO é criada"* e lista só catálogo
  `/p/MLB` do Mercado Livre; a da clubedomosaico é o registro datado da dívida do degrau 4, com a causa medida
  item por item. Fila para o que exige clique humano é exatamente o que a regra manda.
- **Os 96 `ilhas/*/dados/*.json` parseiam, 0 falham.** E os registros sem piso que a varredura acusou **não são
  publicáveis**: `excluido_do_banco`, `nao_publicavel`, `rascunho`, ou dentro de arquivo com `publicar: false` ou
  com `gerado_por` (esquema, resposta gerada, malha). A única exceção é a jornadafly, que é o herdado 43.
- **As cópias de `VOZ.md` e `DESIGN.md` nos dossiês da ohmetria e da jornadafly são idênticas às das ilhas**, e o
  `DESIGN.md` do dossiê da rodametria é idêntico ao da ilha. Suspeitei do padrão do achado 2 nas outras e ele não
  existe: **a rodametria é a única divergência, e só no `VOZ.md`.**
- **Os 70 caminhos de arquivo citados no contrato existem.** Os que o teste acusou como ausentes são formas
  genéricas (`ESTADO.md`, `conferir-no-ar.py`, `dados/indexacao.md`) que o contrato usa como padrão de
  `ilhas/<ilha>/`; os qualificados, inclusive `ferramentas/shopee-api.py` e `ferramentas/conferir-sub-id.py` na
  raiz, estão todos no disco.

---

## O PADRÃO

1. **Os nove achados não são "regra nova não fechou a velha" — esse era o padrão de 16/11. Cinco dos nove são
   REGISTROS QUE CONTAM O MUNDO e ficaram velhos quando o mundo cresceu:** a tabela de ilhas nascidas da Bússola,
   a lista de ilhas do README, a contagem do molde, o "nenhuma ilha mede" do nascimento, e a coluna de
   `ultima_ronda` do painel. Nenhum deles é uma régua errada; todos são um **inventário** certo na data em que
   foi contado.
2. **E três deles já tinham sido corrigidos por um Pente Fino anterior, e envelheceram de novo.** A contagem do
   molde foi de quatro para cinco em 05/10; a tabela da `fila.md` foi fechada em 12/10 com a frase *"agora a
   página conta cinco nos dois lugares"*; a lista do README foi contada em 16/09. **Corrigir um inventário não o
   dá um dono** — e sem dono ele volta a envelhecer no primeiro crescimento.
3. **O gatilho é sempre o mesmo e tem nome e data: a sexta ilha, 27/10/2026.** Quatro dos cinco inventários
   quebraram naquele dia, porque a rodametria nasceu e nada obriga um nascimento a visitar os lugares que contam
   ilhas. É a 29.5 outra vez — *"regra nova não roda sozinha"* — aplicada a um número em vez de a uma régua.
4. **O achado mais caro da semana (o 2) é a mesma doença com outro traje:** o dossiê e a ficha são a **cópia de
   nascimento** de uma ilha, e nada obriga uma correção na ilha a visitar a cópia que a pariu. A 20.7 já tinha
   escrito a frase inteira — *"duas declarações do mesmo fato começam iguais e só uma sobe"* — e aqui a que subiu
   chegou a afirmar, por escrito, que era a única que existia.

**A regra de processo que evitaria a próxima** — cabe na §3 do `ARQUIPELAGO.md`, ao lado da 3.x que a auditoria de
16/11 propôs e que continua esperando. **NÃO INSERIDA**, porque é regra nova de política:

> **3.y TODO NÚMERO QUE CONTA O ARQUIPÉLAGO NASCE COM A DATA DA CONTAGEM E COM UM DONO, E NASCIMENTO DE ILHA
> FECHA A LISTA DE INVENTÁRIOS.** Nenhum documento desta fábrica escreve quantas ilhas, quantas URLs, quantas
> ferramentas ou quantas ilhas medem algo **sem a data em que aquilo foi contado ao lado** — a 23.4 já exige isso
> do painel, e esta linha o estende ao contrato, ao README, ao molde e à `fila.md`. E a execução que faz **nascer
> ou morrer uma ilha** fecha, no mesmo commit, a lista fixa de inventários que contam ilhas: `README.md`, o mapa
> de `foco.md`, a tabela "Ilhas nascidas" da `fila.md`, o comentário de contagem de `ilhas/_modelo/`, e os
> números de "quantas ilhas" do `ARQUIPELAGO.md`; ela diz no commit quantos achou e quantos fechou, e zero
> fechados com mais de zero achados é commit incompleto. **E a cópia de nascimento de uma ilha — dossiê e ficha —
> é inventário também:** correção de fonte no `VOZ.md`, no `DESIGN.md` ou no dado de uma ilha escreve o ponteiro
> datado na cópia da Bússola na mesma passada, porque é dela que a próxima execução lê o tom. Inventário sem data
> é número de tela digitado (seção 8); inventário sem dono é o número de ontem com cara de hoje (seção 4).

---

*Auditoria rodada em 23/11/2026, 05h20 de Brasília (08h20Z). 5 achados MÉDIO (4 corrigidos no ponto operacional,
1 reservado à ronda pela 23.1), 0 MÉDIO novo que precise dele, 4 BAIXO (3 corrigidos), 16 herdados ainda abertos,
nenhum herdado resolvido. Nenhum GRAVE, e a medição que o descarta está escrita. Nenhum valor de segredo escrito
neste arquivo nem em commit.*
