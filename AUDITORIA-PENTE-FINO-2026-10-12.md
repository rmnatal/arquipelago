# AUDITORIA PENTE FINO — 12/10/2026

Varredura do estado real do `main` em `57d6759` (09/10/2026 20h47Z). Branch `pente-fino`.

**114 arquivos abertos** — **42 de regra e prosa**: `ARQUIPELAGO.md` (1.057 linhas), `bussola/BUSSOLA.md`,
`bussola/fila.md`, `bussola/despacho-viagem.md`, `foco.md`, `README.md`, `.gitignore`, `dados/PAINEL.md`,
`dados/consertos.md`, `bussola/rodadas/004.md` e `005.md`, os dois `DOSSIE.md` + `VOZ.md` dos dossiês, os
`PROMPT.md`/`ESTADO.md`/`VOZ.md`/`DESIGN.md`/`ARVORE.md` das cinco ilhas, o `PROMPT.md` e o `ESTADO.md` do `_modelo`,
`ilhas/clubedomosaico/dados/cruzamento-14-9.md` e o relatório de Pente Fino de 05/10/2026 — mais **4** relatórios anteriores
consultados por busca. E **72 JSON de `ilhas/*/dados/`** passados por parser (72 parseiam, 0 falham), os **6** `ESTADO.md`
passados pelo portão da §2, e **todos os 501 arquivos versionados** varridos por quatro padrões de segredo.

**Resultado: 1 GRAVE · 13 MÉDIO corrigidos em 11 arquivos · 7 MÉDIO registrados · 5 BAIXO corrigidos · 11 itens herdados ainda
pendurados.**

**O achado da semana não é uma contradição nova: é a MESMA de 13/09/2026.** A frase que põe a Amazon de volta no Arquipélago —
o arquétipo que criou esta auditoria — estava **de pé em duas ilhas**, com a condição que ela cria (*"quando houver tráfego"*)
**já disparada**. Não é régua velha dormindo: é permissão que acorda sozinha.

---

## GRAVE — PRECISA DO RAPHAEL (1)

**1. O foco não trocou na data que ele mesmo escreveu: a janela da aquametria abriu em 10/10 e hoje é 12/10.**
`foco.md:3` traz `ilha: clubedomosaico`, `desde: 2026-09-24`. `foco.md:7`, escrita por ele em 09/10/2026, diz:
*"(1) clubedomosaico fecha em 09/10/2026 e entra em MODO DE MEDIÇÃO. (2) **aquametria em foco de 10/10/2026 a 16/10/2026** (…)
(3) jornadafly em foco a partir de 17/10/2026"*. O arquivo avisa que a linha da fila *"NÃO troca o foco sozinha: quem troca é a
linha `ilha:`, editada na data"* — e ninguém a editou. **Por que é GRAVE e não MÉDIO:** a decisão de ADIAR já foi tomada em cima
dessa janela. O `dados/PAINEL.md:41` estaciona a dívida da 25.4-b da aquametria (aberta há 26 dias) em *"Entra em foco em
10/10"*, e o despacho de 07/10 no `PROMPT.md` dela marca prazo **14/10** para o veredito das Propostas 1 e 2 — trabalho que, pela
1.2, nenhuma execução pode fazer enquanto a ilha estiver fora do foco. **O que ainda não aconteceu:** nenhuma execução rodou
desde 09/10 20h47Z (`git log --since` em 12/10: zero commits), então nenhum bloco foi construído na ilha errada. A próxima é que
vai. **Não troquei a linha:** o Pente Fino não reserva ilha e não muda a ordem da fila — e três dias de atraso podem ser decisão
dele, não esquecimento. Três linhas e está resolvido: `ilha: aquametria`, `desde: 2026-10-10`, e o histórico da clubedomosaico.

---

## MÉDIO — CORRIGIDO (13 consertos, 11 arquivos)

### A família da semana: a frase da Amazon, de pé em duas ilhas, com a condição já disparada

**2. `ilhas/aquametria/ESTADO.md:45` — "Amazon Associados SÓ quando houver tráfego (regra 3 vendas/180 dias). Ticket típico
R$380, comissão ~R$42." CORRIGIDO por ponteiro.**
A §7 mantém a **Amazon FORA de todas as ilhas** e proíbe, duas linhas abaixo, **criar conta** em plataforma nenhuma. Esta linha
não é só velha: ela escreve uma **condição**, e a condição **já fechou** — a leitura semanal de 07/10/2026 mediu 371 impressões
e 3 cliques nesta ilha. Régua velha dorme; permissão condicional acorda. O `~R$42` sobre R$380 é 11%, nível de tabela da Amazon;
a âncora que vale é o piso publicado da Shopee, **3%**, que dá **R$ 11,40** — e a `bussola/fila.md` trocou essa âncora em
14/09/2026 exatamente por este motivo. Medido hoje por `git grep`: **nenhum link da Amazon existe no banco desta ilha**; o que
estava de pé era a autorização — no `main` desde **06/09/2026** (`f86baf4`), 36 dias.

**3. `ilhas/robometria/PROMPT.md:1190` — "Amazon paga 8% em Eletrodomésticos, mas a conta não deve ser aberta até haver
tráfego". CORRIGIDO por ponteiro.**
Segunda cópia da mesma frase, na outra ilha nascida antes de 14/09. **E a prova de que o conserto é o certo está no próprio
repositório:** as duas ilhas nascidas em 14/09/2026 trazem a formulação correta, palavra por palavra, em
`ohmetria/PROMPT.md:67` e `jornadafly/PROMPT.md:75` — *"Amazon está fora de tudo (seção 7): não é âncora de comissão, não é
evidência de cobertura, não é categoria de referência"*. As duas ilhas **velhas** ficaram com o mundo anterior. Foi o nascimento
que aprendeu, não o contrato que falhou. Esta cópia está no `main` desde **09/09/2026** (`ae48c69`), 33 dias.

### O portão da §2 reprovou a ilha EM FOCO, e a quebra tinha dois dias e meio

**4. `ilhas/clubedomosaico/ESTADO.md` — o cabeçalho YAML perdeu o `---` de fechamento e NÃO PARSEIA. CORRIGIDO.**
O comando que a §2 manda rodar **antes de todo commit, em toda ilha** (`yaml.safe_load(...split('---')[1])`) morre neste arquivo
com `ScannerError: while scanning an alias`. **Causa, achada por `git show`:** o commit `57d6759` (09/10 20h47Z, o último do
`main`) substituiu o `bloco_atual` e **apagou o `---` que vinha depois dele** — a versão anterior, `dd06686`, tinha o
delimitador na linha 44. Sem ele, `split('---')[1]` engole a prosa de "O QUE FALTA PARA ESTA ILHA ESTAR COMPLETA" e o parser
quebra na primeira linha em negrito. **Medido: os 20 commits anteriores deste arquivo parseiam; só o último não.** Nenhuma
decisão foi contaminada porque a ilha está em foco e a §1.2 dispensa comparar cabeçalhos — mas a §2 escreve o custo com todas as
letras: *"a primeira ferramenta que parsear o cabeçalho de verdade decide errado ou morre"*. O conserto é uma linha: o `---` de
volta entre o fim do `bloco_atual` e o `##` da prosa. Os seis `ESTADO.md` voltaram a passar o portão (a ohmetria segue sem dois
campos — achado 21).

### O mapa de leitura: a seção que decide não estava na linha de quem decide — pela quinta vez

**5. `ARQUIPELAGO.md` §0 — a §25 não estava na linha de papel NENHUM, e a §7 manda ela mandar. CORRIGIDO.**
A §7 está na linha da Fundação e na da Bússola, e termina dizendo: *"Onde esta seção e a 25 divergirem, **manda a 25**"* —
apontando para a única seção do contrato que **nenhum papel** era mandado ler. É a 25 que põe o piso de `url_busca` em todo item
publicável (25.2), que proíbe registro publicável sem encurtamento tentado (25.2-b), que exige `url_produto` para o teste de
vida existir (25.4-b) e que proíbe gerar link de afiliado à mão (25.8) — **tudo trabalho da Fundação dentro do banco**. E é a
25.4 que manda a **ronda diária** conferir os links dos itens publicados e tratar link morto como defeito da 19.1. Linha da
Fundação e da ronda diária passam a incluir **25**.

**6. `ARQUIPELAGO.md` §0 — a §30, nascida em 09/10 dizendo "vale para toda ilha", não entrou em linha nenhuma. CORRIGIDO.**
Decisão do Raphael de 09/10/2026, estendida por ele no mesmo dia a todas as ilhas, e invisível para todos os papéis pela letra
do mapa. Quem cria as páginas que ela manda criar é a Fundação; **30** entra na linha dela. É a quinta vez que este mesmo defeito
é consertado (1.2 em 16/09, 1.2-b em 21/09, as três seções da Bússola em 05/10) — e isso está na seção "O PADRÃO".

**7. `ARQUIPELAGO.md:1047` §30.2 — cita "a regra das duas camadas de procedência", que não existe como seção deste contrato.
CORRIGIDO por ponteiro.**
`git grep` em 12/10: a expressão aparece no `ARQUIPELAGO.md` **só nessa linha**, e no resto do repositório só em
`ilhas/aquametria/ESTADO.md:165` e `REGISTRO.md:6108`, onde é a formulação de uma passada **daquela ilha**. É a §3 ao contrário
(*"regra nova do Arquipélago se escreve AQUI, uma vez — nunca copiada para dentro dos prompts das ilhas"*): aqui o contrato citou,
como lei comum, um nome que só existia dentro de uma ilha. As duas camadas estão declaradas na própria 30.2, nas duas frases
seguintes; o ponteiro diz isso, para ninguém sair procurando uma seção que falta nem inventá-la.

### As pontas velhas que davam ordem errada para a semana que vem

**8. `ilhas/aquametria/ARVORE.md:121` — "As cinco calculadoras no ar não têm impressão registrada, então a seção 12.1 ainda
permite mover o slug delas". CORRIGIDO por ponteiro.**
É a correção mais cara desta auditoria, porque é **permissão escrita para mover cinco URLs monetizadas** no arquivo que a próxima
leva de malha abre para decidir endereço (a linha 5 dele: *"breadcrumb, cluster de interlinkagem e leva de malha saem daqui,
nunca da cabeça de quem executa"*) — e a aquametria é a próxima ilha da fila do Raphael. A frase é de 12/09/2026, quando a ilha
tinha 13 URLs e zero impressão, e era verdadeira. A leitura semanal de **07/10/2026** mediu as **mesmas cinco** com **116
impressões na banda 4 a 10**, com as cinco consultas e posições nomeadas uma a uma (litragem 27/9,1 · iluminação 26/5,5 · mídia
23/5,9 · aquecedor 21/7,1 · vazão 19), e o mesmo despacho escreve: *"**Não é para mexer nas URLs** (12.1 proíbe mover URL
posicionada)"*. Hoje a 12.1 **proíbe** o que esta linha autorizava. No `main` desde **11/09/2026** (`2857656`), 31 dias.

**9. `ilhas/aquametria/PROMPT.md:326` — "(e) Produto novo entra sem `afiliado.url`; quem gera o link é a Sentinela estratégica".
CORRIGIDO por ponteiro.**
A alínea é de 09/09/2026 e a alínea **(f), uma linha abaixo**, a desmente desde 23/09: a Open API da Shopee chegou nesta ilha e
os **78 de 78** itens passaram a servir `url_busca` encurtada. A §25.6 aposentou a espera e a §7 fechou a regra: *"produto de
plataforma com API entra no banco já com o link"*. **O que sobra de verdadeiro na (e) é só o Mercado Livre**, e lá quem aperta
"Gerar" é o Raphael, não a Sentinela — o ponteiro guarda essa metade em vez de apagar a alínea.

**10. `ilhas/robometria/PROMPT.md:1315` — "rode os OITO testes de bancada", e a linha 40 do mesmo arquivo proíbe exatamente
isso. CORRIGIDO por ponteiro.**
A linha 40 diz: *"**Não enumere bancada de cabeça neste arquivo nem no `REGISTRO.md`**"*, porque `bancada.py` (18/09/2026) varre
`ferramentas/` e classifica pela convenção de nome. A lista de oito é de 13/09 — ela própria cita *"em 13/09/2026 eram 902 no
total"* — e afirma ser *"a única verificação da seção 8 que roda sem depender do site"*. **Contado hoje: 42 portões sem rede**
(12 `teste-*`, 28 `mutacoes-*`, 2 `validar-*`) **e 48 com `--no-ar`** (mais 6 `conferir-*`). Quem obedecesse rodaria **8 de 42** e
declararia a §8 verificada, e os quatro que a lista omite por nome (`teste-malha.php`, `teste-purga-cache.php`,
`teste-escada-compra.py`, `teste-navegador-arvore.mjs`) são justamente os da leva de malha e da escada de compra. **Agrava, e é a
assinatura do padrão:** o Pente Fino de 28/09 colou ponteiro na linha **1314** e não olhou a **1315**.

**11. `ilhas/robometria/PROMPT.md:35-36` — "38 portões, sem rede" / "44". CORRIGIDO com a contagem de hoje ao lado da de 18/09.**
A seção existe para que portão que desapareça apareça; com o número vencido, ela não vê. O próprio arquivo mediu 40/46 em 21/09
(linha 833) e o `ESTADO.md:20` registra 41. Contados hoje: 42 e 48. O conserto deixa as duas datas visíveis e diz que
`bancada.py --lista` é a única fonte que não envelhece.

**12. `ilhas/robometria/PROMPT.md:1008` — "O EGRESSO DIRETO A ESSES DOMÍNIOS SEGUE FECHADO", medido em 11/09. CORRIGIDO por
ponteiro.**
É a 25.4-b.3 em ação — *motivo velho manda não tentar* — e no arquivo onde essa regra nasceu. O despacho do Raphael de
**17/09/2026**, neste mesmo arquivo (linhas 527-536), mediu `mais.conteudo.wap.ind.br` em **200 aberto** e `www.mi.com` em **301
aberto**, e fechou com *"OS CINCO CAMINHOS ESTAO ABERTOS"*. E a §4 já avisa que **o endereço que vale está no banco, não na frase
que descreve o bloqueio** — lição aprendida nesta ilha, porque os sete registros da marca apontam para `www.mi.com/br` e não para
os nomes da frase. O ponteiro de 28/09 escreveu *"ESSE DIA CHEGOU"* para o item (c) e parou no parágrafo vizinho.

**13. `ilhas/robometria/ESTADO.md:221` — "Falta reenviar o sitemap no Search Console, e isso exige o navegador do Raphael".
CORRIGIDO por ponteiro em linha NOVA.**
Quarta cópia da mesma frase; as três primeiras já tinham ponteiro. O item 4 da DEFINIÇÃO DE PRONTA (`PROMPT.md:806`) registra
*"FECHADO em 16/09/2026: processado, última leitura 15/09, 9 páginas encontradas"*, e `dados/indexacao.md` traz a linha de 23/09
com o reenvio feito. O Pente Fino de 28/09 colou ponteiro nas linhas 304 e 551 deste arquivo e **não chegou a esta** — a da
seção Infraestrutura, que é a que alguém abre para saber o que ainda é do Raphael. **O ponteiro entrou como linha nova, de
propósito:** a linha 221 carrega o valor do `google-site-verification` em texto puro, e reescrevê-la jogaria esse valor para
dentro de um commit novo.

**14. `ilhas/clubedomosaico/ARVORE.md` §5 — o mapa "onde mora cada página que existe HOJE" tem 19 páginas e a ilha tem 29.
CORRIGIDO por ponteiro.**
As **oito** URLs de consulta de produto que nasceram em 09/10 pela §30 (`torques-`, `alicate-`, `cortador-de-vidro-`,
`pastilhas-`, `pastilha-de-vidro-`, `base-de-mdf-`, `espelho-` e `rejunte-para-mosaico`, declaradas em
`dados/consultas-de-produto.json`) não estão na tabela, e o arquivo inteiro para em 07/10. **Escrever as oito linhas é bloco da
Fundação, não conserto de documento** — o Pente Fino não inventa a trilha que a casca serve —, então o ponteiro diz que esta
tabela não é o inventário da ilha e aponta o arquivo que é.

---

## MÉDIO — PRECISA DO RAPHAEL (7 novos)

**15. `ilhas/aquametria/ESTADO.md:5` — `piso: abaixo`, e o próprio cabeçalho já mandou trocar.**
A linha 21 do mesmo arquivo diz *"A rampa DOBRA; `piso` deve passar a `atingido` no primeiro bloco"*, e o `PROMPT.md:60` é mais
direto: *"`piso: abaixo` não é mais verdade"*. **As duas condições da 21.1 estão medidas no próprio cabeçalho:**
`urls_publicadas: 52` (pede 40) e `primeira_indexacao: 2026-09-09` (21 dias fecharam em 30/09). O `congelamento` ainda descreve
48 URLs e "continua ABAIXO DO PISO", texto de 12/09. **Não virei o campo:** a 21.6 dá a escrita dele à leitura semanal, e o campo
é o que a 21.8 faz decidir o tamanho da leva — virar `piso` muda o que a Fundação pode publicar na semana que começa. É decisão,
não conserto.

**16. `ARQUIPELAGO.md` §22.7 manda a Sentinela consertar na hora cinco coisas que a §19.2 e a §12 proíbem.**
A 22.7 põe *"na lista mecânica da seção 19.1, que ela conserta na hora"*: imagem sem `width`/`height`, link interno que não é
`<a href>`, texto que só aparece com JS, cor ou fonte fora do `DESIGN.md`, imagem acima da dobra marcada como `lazy`. **As cinco
só se consertam dentro de snippet** — e a 19.2 diz *"qualquer código de snippet ou lógica de ferramenta"*, declarando-se "lista
fechada, e ela vale mais que a de cima", enquanto a regra 3 da §12 fecha: *"Se a correção exigir tocar em snippet, ela para e
despacha. **Sem exceção**, mesmo que a mudança pareça de uma linha"*. A 22 é mais nova (12/09) que a 19 (11/09), o que daria a
vitória à 22.7; a 19.2 se declara prevalente, o que daria a vitória a ela. **As duas leituras são defensáveis** e o que está em
jogo é a independência da verificação — a razão pela qual a Sentinela existe. Não é conserto de ponta velha: é escolher.

**17. `ilhas/clubedomosaico/PROMPT.md:339` × `ARVORE.md:38` — dois endereços escritos como a futura mãe do `alicate`, e um deles
já está no ar.**
O `PROMPT.md` diz que `/materiais/alicate-para-mosaico/` — publicada em 09/10 — *"quando ganhar 3 filhas, vira mãe sem trocar de
URL"*; o `ARVORE.md:38` e o `VOZ.md:38` registram `/materiais/alicates-e-corte/` como o nível 2 daquela camada, e o
`PROMPT.md:2506` manda **não** publicar essa mãe ainda. A 12.1 proíbe mover URL publicada, então as duas não podem valer juntas.
O slug `alicates-e-corte` foi escolhido em 30/09 *"porque nenhuma das duas páginas existe"* (`ARVORE.md:105`) — premissa que caiu
em 09/10. **É a família do M9** (dois desenhos de URL para a mesma camada da Loja, aberto há 3 semanas), agora na camada do Guia
e com URL no ar. Escolher o desenho é dele.

**18. `ilhas/clubedomosaico/PROMPT.md:2158` × `:337` — a 16.6 proibiria as oito páginas que a §30 acabou de autorizar.**
A linha 2158, escrita em 07/10 e usada como motivo de duas execuções sem URL nova, diz que *"filha sozinha pendurada em
`/materiais/` é o cluster ralo que a 16.6 proíbe"*. A §30.1 isenta a página de consulta de produto da **16.5** e **nada a isenta
da 16.6** — e as oito nasceram em 09/10 exatamente assim, filhas diretas de `/materiais/`. Hoje a frase desqualificaria uma nona
consulta legítima. As duas leituras se sustentam; o que falta é a linha que diz qual vale.

**19. `ilhas/jornadafly/VOZ.md:39` manda, pela §22.2, um lockup e uma cor que foram descartados — e os quatro lockups já estão
em curvas.**
O `VOZ.md` prescreve *"`JORNADA` em 700 + `fly` em 400, coladas"* e *"o índigo da marca"*; o `DESIGN.md:34` manda peso e cor
**iguais** em caixa alta, e o `:44` dá `#378AD0` como a cor da marca. O `PROMPT.md:28` (05/10/2026) declara o índigo `#2F3E9E`
descartado. **A §22.2 dá a vitória ao `VOZ.md`** — e o `VOZ.md` é a ponta velha nas duas, enquanto a §22.6 diz que token só nasce
no `DESIGN.md`. Mexer aqui é mexer em identidade visual aprovada, com os lockups já convertidos em curvas: é dele.

**20. `dados/PAINEL.md` escreve narrativa, histórico, opinião e projeção, que a §23.3 proíbe — e foi a projeção que produziu o
achado 1.**
A §23.3 é taxativa: *"Narrativa, histórico, opinião, projeção e elogio"* ficam fora. O painel de 09/10 projeta datas de foco
futuras (linha 7), narra *"segunda ronda seguida"* (27), opina *"É a terceira vez que a demora tem a mesma causa"* (48) e traz
sete parágrafos de histórico de reconferência (69). **Não é ponta velha — é a regra desobedecida na escrita, no mesmo dia.** E a
linha 7 é a que fez a janela de foco parecer trocada sem que a linha `ilha:` fosse editada. Quem escreve o painel é a Sentinela
(23.1) e **ninguém mais**; o Pente Fino não reescreve painel.

**21. `ilhas/ohmetria/ESTADO.md` continua sem `ultima_ronda` e sem `bloqueada_por` — 26 dias, e o dono designado não chega.**
Confirmado hoje por parser: é a única das seis que falha o portão da §2. O `PAINEL.md` nomeia o dono — *"é da próxima execução que
reservar aquela ilha"* — e essa execução **estruturalmente não chega**, porque a ohmetria está fora do foco e ilha fora do foco
não recebe bloco. Registrado como defeito em 16/09, 21/09, 28/09 e 05/10. **Dívida com dono impossível fica aberta para sempre**,
e sair desse laço é decisão: ou o campo entra por quem não precisa reservar a ilha, ou a §2 diz quem conserta cabeçalho de ilha
parada.

---

## BAIXO — CORRIGIDO (5)

Cinco contagens que o próprio parágrafo desmente na linha seguinte. Três são herdadas e não foram consertadas quando reportadas.

**22. `bussola/rodadas/004.md` — "Cobertura 10 de 10, cinco com preço confirmado" e o parêntese lista SETE.** Corrigido para
sete, aqui e na cópia que já tinha vazado para `bussola/fila.md`.

**23. `bussola/rodadas/004.md:172` — "de doze programas consultados" e a tabela logo abaixo tem TREZE.** Corrigido. *(A cópia em
`viagem-experiencia-icone/DOSSIE.md` **não** foi tocada: lá o "doze" está dentro de uma citação do texto antigo, já marcada como
superada — corrigir citação é falsificar o registro.)*

**24. `bussola/rodadas/005.md:4` — "Seis das sete pendências da 004 estão fechadas"; a tabela marca P1 "NÃO DETERMINADO" e P7
"em aberto": são cinco.** Corrigido. *(Registrado em 05/10 e não consertado então.)*

**25. `bussola/rodadas/004.md:41` — "10 candidatos pontuados" e a 2.4 declara-se "não pontuado": são 9.** Corrigido.
*(Registrado em 05/10.)*

**26. `bussola/fila.md` — a coluna `#` saltava de 16 para 18, e "a melhor Facilidade da fila inteira (4,40)" é falso.**
Renumeradas as duas últimas linhas (17 e 18) com nota, e a posição alinhada em `rodadas/005.md`; nenhum índice, nota ou ordem
tocados. A afirmação foi corrigida recalculando as 18 linhas: a melhor Facilidade é o **som automotivo, 4,64**, e o pior Retorno
é o **drone, 1,73**. *(Herdado de 14/09 e 21/09 — 4 e 3 semanas.)*

---

## O QUE VERIFIQUEI E NÃO É ACHADO

Fica escrito porque a próxima auditoria vai tropeçar nos mesmos, e porque **não achar é resultado**.

- **`ilhas/clubedomosaico/ESTADO.md:63`, "as três mães do Guia estão a 1 (`alicate`), 2 (`pastilha`) e 1 (`rejunte`) filha".**
  Parece não fechar com `PROMPT.md:2414` ("rejunte 1, alicate 2"). **Fecha:** a frase conta quanto **falta**, e
  `dados/cruzamento-14-9.md` — o arquivo GERADO que ela cita — dá exatamente `faltam`: alicate **1**, pastilha **2**, rejunte
  **1**. A linha do `PROMPT.md` é de 02/10 e usa a contagem por RECORTE, que a régua por CONSULTA de 07/10 substituiu. O bloco de
  09/10 foi escolhido pela conta certa.
- **`ilhas/aquametria/PROMPT.md:176`, o critério de pronto que exige `dados/links-afiliado-pendentes.md`.** Parece violar a
  25.6, que aposentou a fila. **Não viola:** a §7 mantém a fila viva *"onde não tem API e o gerador tem reCAPTCHA — Mercado
  Livre"*, e os 12 itens são justamente as marcas que a Shopee não vende. A linha ainda fecha dizendo que os dois campos entram
  juntos, da mesma oferta, "nunca grampeados (25.4-b.1)".
- **Os 12 produtos da aquametria com `afiliado.degrau: null`.** Todos têm a chave presente, `intestavel: true` e
  `motivo_sem_url_produto` escrito: são os 12 intestáveis conhecidos. Dívida administrada, não buraco silencioso.
- **Os literais de 32 caracteres hexadecimais em `robometria/dados/fotos-do-fabricante-*.md`.** São nomes de arquivo da CDN
  `appmifile.com`, não segredo. **E `dados/PAINEL.md:50` e `clubedomosaico/dados/consertos.md:13` citam `?<ilha>_sync=` com
  `...` no lugar do valor** — placeholder, não vazamento.
- **A ordem da `fila.md` com o nº 2 em 3,92 e o nº 3 em 3,94.** Continua sem critério de desempate escrito (herdado, 4 semanas),
  mas as 18 linhas foram recalculadas hoje e **todas** conferem: os 18 S pela fórmula do cabeçalho, os 18 M por
  `M = 2,2 × log10(R$/venda) − 0,07`, os 17 R$/venda por ticket × 3% (o JornadaFly por Civitatis 8%, exceção declarada) e os 18
  índices pela média harmônica. Zero divergência acima de 0,01.

---

## MEDIÇÃO DOS DADOS (classe 5) — contado, não presumido

**72 JSON de `ilhas/*/dados/` passados por parser: 72 parseiam, 0 falham.** Nos bancos primários, contados hoje com o campo de
publicação de cada ilha (e não com um palpite — a primeira passada desta auditoria errou por ler `lista_de_compras` em vez de
`registros`, e o número errado foi descartado antes de entrar aqui):

| ilha | registros | publicáveis | sem `url_busca` | sem `url_produto` | sem motivo escrito | `url` sem `degrau` |
|---|---|---|---|---|---|---|
| robometria `pecas` | 57 | **54** | **0** | 40 | **0** | 0 |
| robometria `modelos-robo` | 50 | **45** | **0** | 30 | **0** | 0 |
| aquametria (4 bancos de produto) | 78 | 78 | **0** | 43 | **0** | 0 |
| clubedomosaico (5 bancos de material) | 41 | 41 | **0** | 17 | **0** | 0 |

- **O piso da 25.2 está íntegro em 100% dos publicáveis das três ilhas no ar** — 99 na robometria (54 peças + 45 modelos), 78 na
  aquametria e 41 na clubedomosaico: **218 itens, zero sem `url_busca`**.
- **Nenhum buraco silencioso de `url_produto` nos 11 bancos acima:** os **130** que faltam têm **todos** um campo de motivo
  escrito (`motivo_sem_url_produto` ou `motivo_sem_ficha`) — medido com a definição estrita, sem contar `observacao` nem
  `intestavel` como motivo. **Isto não é comparável com os "43 buracos silenciosos" de 05/10:** aquele recorte foi de 12 bancos
  e 230 registros, e incluía bancos sem campo de afiliado (espécies, peças da artesã). Quem for comparar as duas semanas
  compara o recorte primeiro.
- **A contagem declarada dentro do JSON bate com a recontada**, nas duas que se pode recontar: `pecas.json` declara
  `total: 57 / publicavel: 54 / excluido_do_banco: 3` e é o que o parser conta; `modelos-robo.json` declara `50 / 45` e idem.
- **Zero `degrau` fora da escada 1–4.** A armadilha que o relatório anterior deixou avisada continua de pé e continua não sendo
  defeito: `robometria/palavras-chave-medidas.json` usa uma escada própria de 0 a 5, declarada no arquivo.
- **Correção de uma linha do relatório de 05/10:** ele registrou que `jornadafly/esquema-banco.json` *"não declara `url_busca`,
  `degrau` nem `conferido_em`"*. Medido hoje pelos caminhos de chave do esquema: `url_produto` **existe**
  (`/entidades/AFILIADO/campos/url_produto`) e `degrau` existe, mas só dentro de `/piso_de_compra/degraus[]/degrau`, que é a
  descrição da escada e não campo de registro. **`url_busca` e `conferido_em` seguem sem existir como chave** — a dívida é real
  e menor do que estava escrita. Continua sendo bloco de dados da Fundação.

---

## SEGREDO (classe 7) — medido, nunca transcrito

Varredura de **todos** os arquivos versionados por quatro padrões (literal de alta entropia atribuído a nome de segredo,
`google-site-verification=`, segredo em query string, chave privada PEM). **Nenhum valor aparece neste relatório nem em nenhuma
linha do commit** — confirmado rodando a varredura contra o próprio diff: zero.

- **Token do Sync em texto puro, em 3 das 5 ilhas, 4 arquivos, 12 linhas:** `ilhas/aquametria/PROMPT.md` (1),
  `ilhas/aquametria/REGISTRO.md` (9: linhas 4166, 4328, 4552, 4744, 4958, 5141, 5271, 5388, 5522),
  `ilhas/clubedomosaico/PROMPT.md` (2: 162 e 164) e `ilhas/robometria/PROMPT.md` (1). Tipo: token de disparo do Sync, 32
  caracteres. **Rotação é o único conserto real**, porque os valores estão na história do git — e rotação é dele.
- **`google-site-verification` em texto puro:** `ilhas/clubedomosaico/ESTADO.md:161`, `ilhas/robometria/ESTADO.md:183` e `:221`.
- **A causa sistêmica continua aberta, e ela é a única parte consertável sem tocar em segredo:** `ilhas/_modelo/PROMPT.md` tem
  **zero** menções a "segredo", "token" ou "credencial" — contado hoje —, então toda ilha nova reproduz o padrão; e o
  `.gitignore` tem **5 linhas** (`node_modules/`, `package.json`, `package-lock.json`, `__pycache__/`, `*.pyc`) e **nenhuma**
  cobre `.env`, `*.pem`, `*.key` ou JSON de conta de serviço. Não consertei nem isto: a regra desta auditoria é registrar quando
  envolve segredo, e os dois são rede de proteção para o próximo vazamento, não remédio para estes. **São duas linhas de arquivo
  e um parágrafo no molde** — é a dívida mais barata de fechar da lista inteira.

---

## HERDADOS — abertos, com o tempo na mesa (sem reabrir discussão)

| item | 1ª aparição | pendurado |
|---|---|---|
| Token do Sync em texto puro (hoje medido em **3** ilhas, 12 linhas) | 14/09 | **4 semanas** |
| E-mail pessoal da artesã em arquivo versionado | 14/09 | **4 semanas** |
| `fila.md` sem critério de desempate: o nº 2 traz 3,92 e o nº 3 traz 3,94 | 14/09 | **4 semanas** |
| `fila.md` "Ilhas nascidas" lista 3 e o Ranking marca 5 como `ilha` — ponteiro colado hoje, decisão aberta | 14/09 | **4 semanas** |
| `aquametria/ARVORE.md` atribui à 16.1 a permanência de `/metodologia/` na raiz; a 21.7 diz o oposto | 14/09 | **4 semanas** |
| Dossiê do som automotivo: "Os 40 candidatos" são **41** (estoura o teto de 30–40 do §5) e "sem DNS (38 de 40)" são 39 | 14/09 | **4 semanas** |
| As **cinco** regras de processo propostas pelas auditorias e nunca inseridas (10.x, 10.y, 8.z, 10.z, 10.w) | 14/09 | **4 semanas** |
| `ohmetria/ESTADO.md` sem `ultima_ronda` e `bloqueada_por`, com dono que não chega (achado 21) | 16/09 | **26 dias** |
| Clube do Mosaico com dois desenhos de URL para a mesma camada (M9) — e agora também na camada do Guia (achado 17) | 21/09 | **3 semanas** |
| Altura do cabeçalho do Clube do Mosaico, 84 ou 96 px (M10) | 14/09 | **4 semanas** |
| `rodadas/005.md:40` "todo índice cai entre 0,20 e 0,35 ponto" falha em três linhas (0,18 · 0,18 · 0,10) | 05/10 | **1 semana** |
| A regra das 48 h da `BUSSOLA.md:112` que o dono designado não tem mãos para cumprir | 05/10 | **1 semana** |
| Menu da Robometria: `VOZ.md`/`DESIGN.md` pedem "Guias" e `/guias/` não existe | 05/10 | **1 semana** |
| Robometria `ESTADO.md:110-113`: 95 − 28 ≠ 71 — **não verificado**, recontar é bloco | 05/10 | **1 semana** |
| P7 fechada no `ohmetria/DESIGN.md:48` e viva na `fila.md` e na `rodadas/005.md` | 05/10 | **1 semana** |
| `BUSSOLA.md` §3.0-b fixa um corte de 50% na linha 61 e nega tê-lo fixado na 63 | 05/10 | **1 semana** |
| `jornadafly/esquema-banco.json` sem `url_busca` nem `conferido_em` como chave (medido hoje, menor do que estava escrito) | 05/10 | **1 semana** |

**Não verificados que ninguém verificou:** `lotus-512.png` com 9.095 bytes contra os 8.770 que três documentos declaram;
`aquametria/ARVORE.md:90`, *"falsa em 14 dos 36 registros"*; qual `sub_id` os 58 links de `malha-pecas.json` carregam (a §25.8
proíbe o único caminho que diria); `casca-fatos.json` `total_de_fontes: 141`, não recontável a partir do arquivo.

**Observação de processo, repetida porque o número só cresce:** a lista "Precisa do Raphael" do `PAINEL.md` de 09/10 tem 12
linhas e **não contém um único item desta tabela**. As pendências mais antigas do Pente Fino não estão no painel que ele lê — e
é por isso que "4 semanas" aparece sete vezes acima.

---

## O PADRÃO

Treze consertos, uma forma só, e ela é a de sempre: **a decisão estava certa e a cópia ficou.** Mas esta semana a forma mostrou
uma variante que as quatro auditorias anteriores não nomearam, e é a mais perigosa das duas.

**Régua velha dorme. Permissão velha acorda.** Uma régua vencida fica vermelha sobre página certa e alguém a conserta no mesmo
dia. Uma **permissão condicional** vencida — *"Amazon quando houver tráfego"*, *"pode mover o slug porque não tem impressão"* —
não reprova nada, não aparece em portão nenhum, e **espera a condição fechar para passar a autorizar o proibido**. As duas
condições fecharam: a aquametria tem 371 impressões, e as cinco calculadoras que a `ARVORE.md` liberava para mudar de endereço
estão na primeira página do Google. Nenhuma das duas frases foi obedecida — e as duas estavam prontas.

E a prova de que vigilância não resolve continua se acumulando no mesmo lugar: em 28/09 o Pente Fino colou ponteiro na linha
**1314** do `PROMPT.md` da robometria e não viu a **1315**; colou nas linhas 304 e 551 do `ESTADO.md` dela e não chegou à 221. É
o terceiro relatório seguido em que o auditor erra o vizinho da linha que estava corrigindo. **Quem corrige um ponto olha o
ponto; a cópia está fora do campo de visão por construção.**

Das **cinco** regras de processo que as auditorias já propuseram, **uma** entrou no contrato — e entrou porque era um comando.
A de 05/10 (a 10.w, varredura da frase revogada no mesmo commit) segue não inserida. **Esta semana não propõe uma sexta.** O que
ela acrescenta é um recorte da 10.w, porque é o que a medição desta rodada sustenta, e cabe numa linha:

> **Acrescentar à 10.w proposta em 05/10/2026, como terceira alínea:** a varredura da frase revogada procura, **além** da frase,
> toda **permissão condicional** sobre o assunto decidido — "quando houver X", "enquanto não Y", "ainda permite Z". Frase
> declarativa vencida fica vermelha e alguém a conserta; **permissão condicional vencida não reprova nada e passa a autorizar o
> proibido no dia em que a condição fechar.** As três que esta auditoria achou estavam no `main` desde 06/09, 09/09 e 11/09/2026
> — **36, 33 e 31 dias**, datados por `git log` —, as três com a condição já cumprida, e nenhum portão do Arquipélago podia
> vê-las: elas não decidem nada, elas permitem.

Não inserido: regra nova de política é decisão do Raphael.
