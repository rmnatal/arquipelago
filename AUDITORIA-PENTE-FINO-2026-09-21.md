# AUDITORIA PENTE FINO — 21/09/2026

Rodada de segunda de manhã, **antes da Bússola**. Auditei do `main` real, `4c6ff67` (20/09/2026 15h47Z), por
`git fetch origin main && git checkout -B pente-fino origin/main`.

## O que foi lido

**43 documentos de lei, inteiros:** `ARQUIPELAGO.md` (948 linhas), `README.md`, `foco.md`, o relatório do Pente Fino
de 16/09; `bussola/BUSSOLA.md`, `bussola/fila.md`, `bussola/despacho-viagem.md`, `bussola/rodadas/004.md` e `005.md`,
`bussola/medicoes/volume-absoluto-2026-09-18.md`, os **4** arquivos dos dois dossiês; `dados/PAINEL.md`,
`dados/despachos.md`, `dados/consertos.md`; e os **25** arquivos de ilha — os **6** `PROMPT.md` (cinco ilhas mais
`_modelo`), os **6** `ESTADO.md`, os **5** `VOZ.md`, os **5** `DESIGN.md` e os **3** `ARVORE.md`.

**Honestidade sobre quem leu o quê.** Li eu mesmo, inteiros, o contrato, os dois arquivos da Bússola, o painel, os
despachos, os consertos, o `PROMPT.md` e o `ESTADO.md` da robometria (a ilha em foco), o molde e o relatório
anterior. Os arquivos das quatro ilhas fora do foco, os dossiês e as rodadas foram lidos por duas varreduras
auxiliares, instruídas com regra dura de não inventar achado — **e nenhum achado delas entrou neste relatório sem
eu abrir o arquivo e reler o trecho na fonte.** Três achados que elas trouxeram eu **descartei** depois de conferir:
(i) a 1.2-b.3 dizer que a Aquametria é "a única com demanda medida" **não** é erro — ela fala das quatro fora do
foco, e a Robometria, medida no mesmo dia, é a que está em foco; (ii) a cobertura de afiliado do JornadaFly abaixo
de 7/10 já está **declarada no próprio dossiê** e a ilha nasceu com isso na mesa, então é decisão tomada, não
achado; (iii) o tamanho do `lotus-512.png` (8.770 × 9.095 bytes) eu não consegui separar entre medida de bloco e
recommit — fica **não verificado**.

**Medição, não leitura.** Os **103 registros** de `ilhas/robometria/dados/pecas.json` (53) e `modelos-robo.json`
(50), campo a campo; `cobertura-r1.py`, `validar-banco.py` e `bancada.py --lista` **rodados**; os **6** cabeçalhos
`ESTADO.md` passados por `yaml.safe_load` e conferidos chave a chave contra a seção 2; as **39** espécies de
`aquametria/dados/especies-agua-doce.json` contadas; os campos de afiliado de `ohmetria/dados/*.json` e
`jornadafly/dados/experiencias.json`; e as **18 linhas** da `fila.md` recalculadas em Python contra as quatro
fórmulas declaradas. `git log --since="7 days ago" --name-only` para começar pelo que mudou.

**Achados: 29** — 3 GRAVE · 12 MÉDIO · 14 BAIXO. **13 corrigidos**, **16 registrados** (8 deles PRECISA DO RAPHAEL).
Mais **4 pendências herdadas** da rodada de 16/09, abertas há 5 dias, e **1** aberta há 7.

> **A resposta curta, antes do detalhe:** a Robometria foi declarada PRONTA às 13h45Z de 20/09 e, **às 15h39Z do
> mesmo dia**, um portão escrito pela mesma execução derrubou o número do item 2 de **15 para 11** — o commit de
> fecho remediu o item 1 e não releu o vizinho (G1). A ilha está PRONTA, proibida de receber investimento novo por
> decisão escrita do Raphael, e o `foco.md` continua nomeando **ela** — então a próxima execução da Fundação não
> tem trabalho elegível em ilha nenhuma (G2). E a 1.2-b, escrita em 18/09, devolveu as ilhas fora do foco ao modo
> de medição sem tocar na 1.2, que manda o contrário: duas horas depois, a ronda de 18/09 obedeceu à ponta velha e
> registrou no painel que não olhou nenhuma delas (G3).

---

## GRAVE — decisão foi tomada com base errada

### G1. A Robometria foi declarada PRONTA às 13h45Z de 20/09 com o item 2 em **15**; às 15h39Z do mesmo dia a própria execução o levou a **11**, e ninguém releu

- **Arquivos:** `ilhas/robometria/PROMPT.md` (DEFINIÇÃO DE PRONTA, item 2, e a tabela "OS CINCO ITENS ESTÃO
  FECHADOS"), `ilhas/robometria/ESTADO.md` (`estado: viva`), `ilhas/robometria/dados/cobertura-r1.json`.
- **A régua do item:** *"Pronto quando `cobertura-r1.py --gravar` mostrar pelo menos **15** modelos publicáveis
  atendidos pelas duas ferramentas."* Fechado em 18/09 às 10h32Z com exatamente 15.
- **A medição de hoje, rodada e não lembrada** — `python3 ferramentas/cobertura-r1.py`:

  | | 18/09 (gravado) | 21/09 (rodado hoje) |
  |---|---|---|
  | atendidos pelas DUAS | **15** | **11** |
  | `recomendaveis_pela_r2` (o teto da meta) | 17 | **13** |

  Os 11 são `positivo-pra2000`, `positivo-pra800`, `roborock-saros-z70` e os oito Xiaomi.
- **A causa está no mesmo arquivo, duas seções abaixo, e é do mesmo dia.** O portão novo do canal brasileiro
  (`ferramentas/medir-canal-brasileiro-no-ar.py`, commit `174e0f1`, **20/09 15h39Z**) anulou **7 canais** — 5
  Roborock e 2 Multi — porque as páginas estavam servindo **404 no ar como prova**. Quatro dos cinco Roborock
  anulados eram quatro dos 15 da interseção: `roborock-q8-max`, `roborock-qrevo-curv`, `roborock-qrevo-master`,
  `roborock-s8-maxv-ultra`. **15 − 4 = 11.** O portão fez o que existe para fazer; o que não aconteceu foi a
  releitura.
- **A ordem do relógio, que é o que faz disto um achado:** PRONTA às **13h45Z**, portão às **15h39Z**, commit de
  fecho às **15h47Z**. Esse último commit **remediu o item 1** (95 de 95 rendendo comissão, conferido no ar) e
  **não tocou no item 2**, que a mesma execução tinha acabado de mover.
- **E o número errado está commitado como DADO, não só como prosa:** `dados/cobertura-r1.json` ainda afirma *"das
  45 entradas publicáveis, apenas **15** são atendidas pelas DUAS"*.
- **Por que nenhum portão viu, e esta é a metade que vale para as outras ilhas:** `bancada.py` classifica o prefixo
  `cobertura-` como *"ferramenta de PRODUÇÃO … que NÃO afirma nada"*, então `cobertura-r1.py` **não roda em nenhuma
  das 44 passadas** — enquanto o arquivo que ela grava é a única afirmação da ilha sobre a emenda do funil.
  `validar-banco.py` roda e **APROVA**, porque não olha esse arquivo. Régua que não cobre o que o bloco mudou
  certifica a página de ontem (seção 4).
- **O que eu fiz: PRECISA DO RAPHAEL, com a medição transcrita.** Escrevi a remedição datada no topo da tabela dos
  cinco itens, com a causa e a aritmética. **Não rodei `--gravar`, não mexi no `estado: viva` e não reabri o
  item:** gravar 11 por cima de 15 reabre o item 2, desfaz a PRONTA, muda a fila e joga fora trabalho declarado.
  As três saídas que os dados admitem estão escritas lá — (a) a PRONTA vale e a queda vira dívida nova; (b) a meta
  de 15 é remedida contra o teto de 13, como já foi em 17/09; (c) o assunto inteiro entra na decisão de outubro.
  **Em todas elas o primeiro passo é o mesmo e custa um comando:** `cobertura-r1.py --gravar`, para o dado parar de
  afirmar 15.

### G2. O `foco.md` nomeia uma ilha PRONTA que está proibida de receber investimento — e a 1.2 impede a Fundação de pegar qualquer outra

- **Arquivos:** `foco.md` × `ARQUIPELAGO.md` §1.2 e §1.2-b.3 × `ilhas/robometria/PROMPT.md` (despacho do Raphael de
  18/09) e `ESTADO.md`.
- **As quatro pontas, todas datadas:**
  - `foco.md`: `ilha: robometria`, desde **16/09**, e o arquivo diz como sair — *"troque a linha `ilha:` por
    `ilha: nenhuma`"*.
  - §1.2: *"a Fundação trabalha **só nela**. A rotação da seção 1 fica suspensa"*, e o item 3 manda **parar** em vez
    de pegar outra ilha.
  - Despacho do Raphael de 18/09, decisão 2: *"Depois de pronta, ela **NÃO** recebe investimento novo … Nenhuma
    execução da Fundação deve propor expansão de malha, leva nova de modelos ou bloco de conteúdo nesta ilha sem
    que a série mostre impressão em dois dígitos"* — e a série só é lida em 23/09, 30/09, 07/10 e 14/10.
  - §1.2-b.4: *"Ilha que **termina o foco** não fica no limbo"* — a seção pressupõe a saída, e a ilha terminou em
    20/09.
- **O efeito, em uma frase:** a única ilha que a Fundação pode tocar é a única em que ela está proibida de
  construir. O `ESTADO.md` da robometria já registra isso, duas execuções seguidas: *"NÃO SEGUI PARA BLOCO DA FILA,
  e pelo mesmo motivo da execução anterior: a ilha está PRONTA e no regime do CRITÉRIO PRÉ-REGISTRADO."*
- **Medido, para não exagerar:** **nenhuma execução foi desperdiçada ainda** — não há um commit no `main` desde
  20/09 15h47Z. O custo é da próxima em diante, e são ~20 por semana (`foco.md`).
- **A resposta já está escrita no contrato, e é por isso que eu não a executo.** A §1.2-b.3 diz qual é a próxima:
  *"Em 18/09/2026 a Aquametria vem antes das outras três **porque é a única com demanda medida**"*.
- **O que eu fiz: PRECISA DO RAPHAEL.** Trocar a linha do `foco.md` muda a ordem da fila e é decisão de política.
  **Texto proposto, NÃO inserido:**
  > ```
  > ilha: aquametria
  > desde: <data>
  > decidido_por: <Raphael>
  > motivo: a Robometria ficou PRONTA em 20/09/2026 e entrou no regime de experimento medido (decisão de 18/09):
  >   a Sentinela continua medindo a série, a Fundação não investe, e outubro decide. A ordem sai da medição
  >   (1.2-b.3) e a Aquametria é a única das quatro com demanda medida.
  > ```
  > *(Se ele preferir `ilha: nenhuma`, a rotação da seção 1 e a 18.1 voltam inteiras — também resolve o travamento,
  > e é a opção que não escolhe ilha por ele.)*

### G3. A 1.2-b devolveu as ilhas fora do foco ao modo de medição em 18/09 e não tocou na 1.2 — duas horas depois, a ronda obedeceu à ponta velha

- **Arquivos:** `ARQUIPELAGO.md` §1.2 × §1.2-b.1, §12, e `dados/PAINEL.md`.
- **As duas pontas, coladas no mesmo arquivo:**
  - §1.2 (**16/09**): *"**Ninguém ronda as ilhas fora do foco**"* e *"**Ronda diária:** … Não abre, não mede e não
    relata nenhuma outra ilha"*; e para a leitura semanal, *"toda a leitura — indexação, vigilância de loja, lacuna
    de conteúdo, tráfego, posição — é dela e de mais nenhuma"*.
  - §1.2-b.1 (**18/09**, commit `ee530f2` às 12h41Z): *"**Medição**: todas as outras. Na medição a Sentinela
    continua rodando, a série de `dados/indexacao.md` e `dados/posicoes.md` continua crescendo"*, com a frase do
    Raphael — *"sempre mensurando os anteriores"* — e a causa na 1.2-b.2: cada ilha medida barateia a seguinte.
- **`dados/indexacao.md` e `dados/posicoes.md` são artefatos da LEITURA SEMANAL** (§12.1 e §11, passo 9), então
  para ela a contradição é frontal e a 1.2-b vence por data e por ser decisão nomeada.
- **A decisão contaminada, e ela tem hora:** a ronda de **18/09 às 14h52Z** (commit `8795ef2`), **duas horas e
  onze minutos depois** de a 1.2-b entrar no `main`, fechou escrevendo em `dados/PAINEL.md`: *"As outras quatro
  ilhas não foram olhadas nesta ronda, por força do foco da 1.2"*, e as linhas delas saíram do cabeçalho do
  `ESTADO.md`, **não medidas no ar**. Desde então não houve outra ronda: a série de quatro ilhas está parada há
  três dias por uma regra que foi revogada pela metade.
- **O que eu fiz: CORRIGIDO com ponteiro, e a metade ambígua REGISTRADA.** Pus na §1.2 e na §12 o ponteiro datado
  dizendo que a 1.2-b é a ponta nova para a **leitura semanal**, com as duas citações e a hora do painel. **Não
  decidi** se a **ronda diária técnica** (HTTP 200, `/status`, console, `&#038;`, tom) também volta às quatro
  ilhas: a 1.2-b diz "a Sentinela continua rodando" sem separar as duas Sentinelas, as duas leituras são
  defensáveis, e isso muda quanto trabalho a ronda faz. **Essa metade é do Raphael**, e está escrita como pendência
  dentro do próprio ponteiro.

---

## MÉDIO — regra inconsistente, sem decisão contaminada

### M1. Duas ilhas mandam gravar um campo que não existe no contrato, e uma delas ainda nem carregou o banco — **CORRIGIDO**

`ilhas/ohmetria/PROMPT.md` e `ilhas/jornadafly/PROMPT.md`, a mesma linha nos dois: *"Nenhum item entra no banco sem
`afiliado.url_busca_bruta`."* Também em `ilhas/ohmetria/dados/especificacao-calculadoras.md`. **`url_busca_bruta`
não existe em lugar nenhum do `ARQUIPELAGO.md`:** a §25.4-b batizou a URL crua da busca de
`afiliado.url_busca_produto` em 13/09/2026. **A Aquametria e a Robometria já corrigiram exatamente esta frase nos
próprios `PROMPT.md`** — *"onde o despacho diz `url_busca_bruta`, leia `url_busca_produto`"* —, e a correção não
viajou para as duas ilhas novas. É o defeito que viaja em cópia, quarta ocorrência registrada.
**Por que é MÉDIO e não BAIXO:** os dois bancos da ohmetria (`modulos.json`, `alto-falantes.json`) têm **zero
registros** — a próxima carga criaria o campo com o nome errado. O `experiencias.json` da jornadafly já grava
`url_busca_produto` (4 ocorrências), ou seja, **o banco já desobedece à letra do próprio `PROMPT.md`**, e
acertadamente. **CORRIGIDO** nos três arquivos, com o nome certo, a data e a causa.

### M2. O mapa de leitura não dá a 1.2-b às Sentinelas — e a 1.2-b.1 é a regra que decide o que elas fazem — **CORRIGIDO**

`ARQUIPELAGO.md` §0. As duas linhas de Sentinela listavam `1.2` e não `1.2-b`, e o mapa abre dizendo *"cada papel
abre as seções da sua linha e para"*. **É o M3 da auditoria de 16/09 acontecendo de novo, com a seção seguinte.**
**CORRIGIDO:** `1.2-b` entrou nas duas linhas, com a causa escrita ao lado da nota gêmea de cinco dias atrás.

### M3. O molde nasce sem `piso` e sem `primeira_indexacao`, que a 21.6 tornou obrigatórios — **CORRIGIDO**

`ilhas/_modelo/ESTADO.md`. As **quatro** ilhas vivas têm os dois campos; o molde não tinha nenhum, então toda ilha
nova nasceria sem os campos que a Fundação lê antes de decidir o tamanho da leva (21.6: *"a Fundação lê esse campo
antes de decidir o tamanho da leva — não recalcula de cabeça"*). **É o mesmo defeito que o `ultima_ronda` do
mesmo arquivo, corrigido em 16/09** — e cinco dias depois o molde ainda estava incompleto por outros dois campos,
porque o conserto de 16/09 foi do campo, não do gabarito. **CORRIGIDO**, com a causa na linha.

### M4. O molde faz o `PROMPT.md` dono da paleta, que a 22.6 proíbe, e não traz `DESIGN.md` nem `VOZ.md` — **CORRIGIDO no ponteiro, o resto é bloco**

`ilhas/_modelo/PROMPT.md` lista *"Paleta, 7 valores e nada além"* e a tipografia como conteúdo dele, contra a §22.6
(12/09/2026): *"o `PROMPT.md` **deixa de ser dono da paleta**: onde ele hoje lista cor e fonte, passa a apontar
para o `DESIGN.md`"*. E a pasta `_modelo/` tem **só** `ESTADO.md` e `PROMPT.md` — pela §15.1, *"ilha sem `VOZ.md`
não recebe bloco novo até ele existir"*, então **ilha copiada do molde nasce impedida de receber bloco**.
**CORRIGIDO** com o ponteiro no topo da Identidade, nomeando as duas seções. **Criar os dois moldes é bloco da
Fundação, não conserto de auditor** — fica registrado.

### M5. Um despacho de prioridade ALTA cumprido pela metade continua em ABERTOS, com o título afirmando um fato falso — **CORRIGIDO com nota, sem mover**

`dados/despachos.md`, *"prioridade ALTA — as DUAS ilhas nascidas em 14/09 não estão na lista de rede"*. O "pronto
quando" do título está atendido: `ilhas/jornadafly/ESTADO.md` e `ilhas/ohmetria/ESTADO.md` trazem
`rede: aberta em 2026-09-18`, medido às 12h35Z com **HTTP 200**, e o `PAINEL.md` de 18/09 escreve que *"o despacho
ALTA de 15/09 sobre a lista de domínios está cumprido e saiu deste painel"*. **É a segunda vez que um ALTA
cumprido fica na lista dos abertos** — a primeira foi o M8 de 16/09, no bloco de FECHADOS logo abaixo.
**O que sobra dele é real e não é ALTA pela própria descrição:** `api.bcb.gov.br` (câmbio, e o texto diz *"nada
trava por causa disso"*), `sac.taramps.com.br` (trava a F3 da ohmetria e 8 constantes) e os domínios de operador da
jornadafly. **CORRIGIDO** com nota datada no topo do bloco, separando as duas metades. **Não movi e não rebaixei a
prioridade:** reescrever despacho pela 18.3 é da Fundação. *(Atenuante medido: este ALTA **não** fura o foco, porque
a 1.2 só é furada por ilha no ar e quebrada, e nenhuma das duas está no ar.)*

### M6. O corpo de dois `ESTADO.md` declara a rede BLOQUEADA contra o cabeçalho do próprio arquivo — **CORRIGIDO**

`ilhas/ohmetria/ESTADO.md` (*"**Rede da nuvem: BLOQUEADA** … Despacho de prioridade ALTA"*, e *"sem registro A —
não resolve para endereço nenhum"*) e `ilhas/jornadafly/ESTADO.md` (seção "O que está travando": *"devolvem **000**
… **O que trava:** o **3b em diante**"*). **Os dois cabeçalhos, no mesmo arquivo, dizem `rede: aberta em
2026-09-18`, com HTTP 200 medido.** É o "resumo velho lido como fato" da seção 4 dentro do arquivo cuja primeira
linha é o resumo novo. **CORRIGIDO** com ponteiro datado nos dois, sem apagar o que foi medido em 14/09.

### M7. A Aquametria manda, em dois arquivos, recusar uma leva que está no ar desde 14/09 — **CORRIGIDO**

`ilhas/aquametria/ARVORE.md`: *"`/peixes/ciclideos-anoes/` | — | em breve — **1 elegível** (ramirezi)"*. E
`ilhas/aquametria/PROMPT.md`, na fila: *"**Próxima leva deste eixo: nenhuma está pronta** … `/peixes/ciclideos-anoes/`
tem 1 elegível"*. **O `REGISTRO.md` da mesma ilha, em 2026-09-14 22h11Z:** *"LEVA 6: A QUINTA CATEGORIA … QUATRO
URLs novas — `/peixes/ciclideos-anoes/` e as fichas do ramirezi, do apistogramma agassizi e do papilocromis"*,
manifest revisão 87, `/status` conferido na 87. **Ordem velha é executada:** quem ler ou recusa trabalho já feito ou
republica o que está publicado. **CORRIGIDO** nos dois, com a fonte e a data. **Qual é a próxima leva eu não
decidi** — é banco e é bloco.

### M8. Três números para um banco só, e o certo não é nenhum dos dois escritos — **CORRIGIDO na contagem**

`ilhas/aquametria/ARVORE.md` diz *"`especies-agua-doce.json`, **37 registros**"* numa linha e *"falsa em **14 dos
36 registros**"* em outra. **Contado no arquivo hoje: 39 espécies** (mais 3 em `especies_recusadas`). O `ESTADO.md`
corrobora (`validar-especies 39 registros`) e o `REGISTRO.md` anota a passagem de 37 para 39. O 37 × 36 já estava
aberto desde 14/09; o dado novo é que **nenhum dos dois é o banco**. **CORRIGIDO** o número contado, com nota.
**Os derivados — "29 dos 37 passam", "14 dos 36" — ficam marcados como não verificados**: recontar régua é bloco, e
a ilha está fora do foco.

### M9. O Clube do Mosaico tem dois desenhos de URL e dois eixos de categoria para a mesma camada — **PRECISA DO RAPHAEL**

`PROMPT.md`: *"coleções `/loja/colecao/<termo>/`"* e *"Coleções **por uso** (/loja/centro-de-mesa, /loja/presentes,
/loja/jardim)"*. `ARVORE.md`: *"Nível 2 **pelo tipo de peça**: `/loja/vasos/`, `/loja/colares/`, `/loja/quadros/`…"*,
sem o segmento `colecao`. `VOZ.md`: *"na loja: `vasos`, `colares`, `quadros`"*. **Dois esquemas de endereço e dois
eixos de categorização**, e a §16 é estrutural. O bloco que publicar a primeira coleção escolhe no escuro — e a
§19.2 põe *"estrutura de URL, pai ou molde de casca"* na lista fechada do que **não** se conserta sem decisão.
Registrado.

### M10. A altura do cabeçalho do Clube do Mosaico: o dono do token diz 96 px, três documentos dizem 84 — **PRECISA DO RAPHAEL**

`DESIGN.md`: *"altura **~96 px**"*. `VOZ.md`: *"~84 px"*. `PROMPT.md`: *"a barra subiu para **84 px**"*.
`ESTADO.md`: *"barra de **84 px**"*. Pela §22.6 o `DESIGN.md` é o dono da medida, e **é ele que está sozinho**.
É irmão do defeito do logo (52 × 64 px) já aberto desde 14/09, e não é o mesmo. Registrado: escolher entre 84 e 96
é mudar token, e a 22.6 manda mudar o `DESIGN.md` primeiro, com o motivo.

### M11. O `DESIGN.md` do JornadaFly proíbe e manda pintar "FLY" de azul, no mesmo arquivo — **PRECISA DO RAPHAEL**

`ilhas/jornadafly/DESIGN.md`: *"**Ninguém pinta FLY de azul**: o azul da marca é do rasgo do símbolo e de mais
nada"* — e, na tabela de cor, a linha `--sinal` (`#378AD0`) lista como uso *"traço do monograma, **\"FLY\"**,
preenchimento, barra do resultado"*. Junto vem a segunda metade: o `PROMPT.md` declara **lei nesta ilha** que *"a
assinatura tipográfica dá peso a JORNADA e recua fly"* (700 caixa alta + 400 caixa baixa), o `VOZ.md` repete, e o
`DESIGN.md` diz que *"JORNADA e FLY têm o MESMO peso e a MESMA cor"* — que é o que a arte oficial entregue pelo
Raphael faz. Pela §22.2, **quando os dois discordam vence o `VOZ.md`**, ou seja, a regra em vigor hoje é a que
contradiz a marca. Registrado: identidade é dele.

### M12. Duas ilhas continuam com o cabeçalho de estado incompleto — **herdado, aberto há 5 dias**

`ilhas/clubedomosaico/ESTADO.md` e `ilhas/ohmetria/ESTADO.md` não têm `ultima_ronda` **nem** `bloqueada_por`,
obrigatórios pela §2 e lidos pela §1 (passo 3), pela §12 e pela §23.2. Os seis parseiam em `yaml.safe_load`;
o portão da §2 mede se o cabeçalho **parseia**, nunca se ele tem as chaves. **Agravante novo:** o próprio
`bloco_atual` da ohmetria escreve *"`bloqueada_por` segue null de propósito"* — sobre um campo que não está no
arquivo. Não corrigi pelo mesmo motivo de 16/09: `ultima_ronda` é campo da Sentinela e o `bloqueada_por` da
ohmetria é justamente a pergunta aberta. **Continua valendo a proposta de 14/09, ainda não adotada:** o portão da
§2 deveria cobrar as oito chaves, não só o parse.

---

## BAIXO — ruído

### B1. `fila.md`, linha 8: S digitado 2,60 onde a fórmula dá 2,70 — **CORRIGIDO**

Bicicleta e patinete: S_par 3 · S_com 1 → S = 3×0,85 + 1×0,15 = **2,70**, e a célula dizia 2,60. **A prova de que
era digitação e não conta é o índice publicado:** com 2,70 a Facilidade é 3,22 e o índice 3,57, que é o número da
tabela; com 2,60 seria 3,54. Só a célula foi trocada. **Foi a única divergência acima de 0,05 nas 18 linhas** — os
18 M conferem com M = 2,2×log10(R$/venda) − 0,07 e com ticket × 3%, e todos os índices conferem com a média
harmônica.

### B2. "A melhor Facilidade da fila inteira (4,40)" é falso pela própria fila — registrado

`fila.md` (ferragem de marcenaria) e `rodadas/005.md`. Pela fórmula declarada, ferragem = 4,40, mas **som
automotivo = 4,64** (S 4,40 · P 5) — número que o dossiê dele imprime com todas as letras (*"Facilidade 4,64"*).
Não corrigi: dá para ler "a melhor entre os que ainda não nasceram", e as duas leituras são defensáveis.

### B3. O ranking não está ordenado pelo índice, e falta o nº 17 — registrado

`fila.md`: o nº 2 (viagem) traz **3,92** e o nº 3 (solar) **3,94**. A tabela se declara "ranking vivo" ordenado por
índice. A `rodadas/005.md` assume o desencontro (*"praticamente empatado com a energia solar"*) e o nº 2 já é ilha
nascida. Na mesma tabela, **o nº 17 não existe** — salta de 16 para 18. Não corrigi: renumerar quebra as
referências das rodadas, e é arquivo da Bússola.

### B4. Um `ESTADO.md` cita o próprio cabeçalho com números que o cabeçalho não tem — registrado

`ilhas/aquametria/ESTADO.md`: *"o próprio cabeçalho deste arquivo registra, hoje, 'home em 200 e `/status` na
**revisão 77**, em **UMA** passada'"*. O cabeçalho diz **revisão 87, em TRÊS passadas**. Citação literal de um
texto que não existe no arquivo citado.

### B5. A `ARVORE.md` da Aquametria cita 36 páginas "pelo `urls_publicadas` do `ESTADO.md`", que diz 40 — registrado

E a nota ao lado do número já avisava, em 14/09, que ele *"vai envelhecer de novo"*. Envelheceu em oito dias.

### B6. O `DESIGN.md` do JornadaFly citava a seção 15 para o teto de fontes, que é da 22.4 — **CORRIGIDO**

A seção 15 é a da voz; o teto de famílias é a 22.4. O próprio arquivo já a cita certo dois parágrafos abaixo.

### B7. No dossiê do som automotivo, V é medido por ferramenta numa seção e volta a ser nota de nicho na vizinha — registrado

`dossies/som-automotivo/DOSSIE.md`: *"**V MEDIDO POR FERRAMENTA**, como a seção 3.1 do `BUSSOLA.md` passou a
exigir"*, com **F2 = 4**; e, na linha de notas do mesmo arquivo (e na `fila.md`), **V 5** como nota do nicho — que
é exatamente a forma que a §3.1 proíbe (*"V é por ferramenta, não por nicho"*). **Não contamina índice:** V não
entra em Facilidade nem em Retorno, só desqualifica abaixo de 2.

### B8. Dois arquivos citam uma regra de símbolo que a `BUSSOLA.md` não tem — registrado

`bussola/despacho-viagem.md` e `dossies/viagem-experiencia-icone/DOSSIE.md`: *"a regra de símbolo da seção 5 do
`BUSSOLA.md` proíbe avião, mala, globo e passaporte"*. A §5(e) diz outra coisa: o símbolo *"nasce do GESTO TÉCNICO
do nicho … nunca de animal, produto ou mascote"*. A paráfrase é fiel ao espírito e a ilha já nasceu com o logo —
por isso BAIXO e não corrigido.

### B9. O Clube do Mosaico nomeia dois arquivos de favicon que não existem, e uma regra que depende de um arquivo quebrado — registrado

`PROMPT.md`: *"os PNGs de `identidade/logo/` (**favicon-512/180/32**)"*; `ESTADO.md`: *"ficam **os favicons**"*. A
pasta tem `LEIA-ME.md`, `favicon-32.png` e `lotus-512.png` — **`favicon-512.png` e `favicon-180.png` não
existem**. E o `DESIGN.md` manda *"o logo no rodapé é a **lótus sozinha**"*, sendo que o único arquivo de lótus é
declarado truncado e ilegível pelo próprio `PROMPT.md` e pelo `ESTADO.md`. **Não verificado:** o `ESTADO.md` diz
"8.770" bytes e o arquivo tem 9.095 — não consegui separar medida de bloco de recommit.

### B10. "7 valores e nada além" seguido do oitavo, na linha de baixo — registrado

`ilhas/ohmetria/PROMPT.md`: *"Paleta, 7 valores e nada além: … alerta `#B3261E`."* e, na linha seguinte, *"use
`#8A5200`"*. O `DESIGN.md` da ilha traz 8 tokens de cor. Pela §22.6 quem manda é o `DESIGN.md`, então o que está
errado é a contagem da frase — e mudar a frase é mexer em token, que a 22.6 manda fazer com motivo escrito.

### B11. Uma razão de contraste apresentada como medida está errada — registrado

`dossies/viagem-experiencia-icone/DOSSIE.md`, `--traco #E3DCD1`: declarado **1,27:1** sobre branco; o cálculo WCAG
dá **1,362:1**. Foi a única das 21 razões de contraste dos dois dossiês que não bateu — as outras 20 conferem à
segunda casa. Decorativo, sem exigência de 4,5:1, por isso BAIXO.

### B12. Uma nota "conservadora" que ninguém mediu segue virando índice — registrado

`rodadas/004.md`, airsoft: *"S_com não foi medível (a busca devolveu SERP 100% em inglês); **usei 1 conservador**"*.
A §3.1 da `BUSSOLA.md`, válida "da 005 em diante", diz *"valor neutro é invenção … se falta componente, **não
calcule o índice**"*. A 005 recalculou o airsoft mexendo só em A, sem remedir S_com, e ele segue em 14º com S_com
1. Não corrigi: remedir SERP é rodada da Bússola, que está **pausada**.

### B13. O Clube do Mosaico diz, na seção de referência, que o `pecas.json` ainda vai nascer — registrado

`PROMPT.md`, "Endpoints desta ilha": *"a artesã ainda não cadastrou peça … o arquivo `dados/pecas.json` **nasce no
dia em que houver a primeira**"*. Mais abaixo, no mesmo arquivo: *"**`dados/pecas.json` nasceu** com a peça de
verdade dentro"*, e o `ESTADO.md` registra a peça publicada em 13/09.

### B14. O `PAINEL.md` está com três dias e uma decisão de atraso — herdado, e pior que em 16/09

Datado de **18/09 14h45Z**. Diz `robometria | nascendo` (o `ESTADO.md` diz `viva` desde 20/09), lista quatro
despachos que foram cumpridos em 19 e 20/09, e pede na "Precisa do Raphael" coisas já pagas (a credencial da Open
API estava no ambiente em 20/09; a decisão da foto do fabricante saiu em 19/09). **Não corrigi de propósito: a
§23.1 diz "ninguém mais escreve nesse arquivo".** O agravante de 16/09 continua — pela 1.2 a ronda só olha a
robometria, então **ninguém tem mandato para atualizar as outras quatro linhas** (ver G3).

---

## Segredo em lugar errado — registro, nunca conserto

**O token do Sync continua em texto puro**, que é o arquivo que toda execução abre. Tipo: **token de autenticação
do endpoint de Sync, embutido em query string**. *(O valor não está transcrito aqui nem no commit.)*

| arquivo | onde | tipo |
|---|---|---|
| `ilhas/robometria/PROMPT.md` | linha 21 | token do Sync em query string |
| `ilhas/aquametria/PROMPT.md` | linha 21 | token do Sync em query string |
| `ilhas/clubedomosaico/PROMPT.md` | linhas 41 e 43 | o mesmo token, reaproveitado no parâmetro `token=` da rota de cópia das peças (§24) |
| `ilhas/aquametria/REGISTRO.md` | ~13 linhas | o endpoint completo, em histórico append-only |
| `ilhas/robometria/REGISTRO.md` | histórico | idem |

**Aberto há 7 dias**, desde o G4 da rodada de 14/09. O conserto continua tendo duas metades e as duas são dele:
gerar token novo em cada ilha e passar a lê-lo do documento `arquipelago-credenciais` do Drive, como a §25.6 já
manda e como as credenciais da Shopee já fazem. **O contrato registra a própria dívida** na §25.6: *"esse mesmo
documento é a casa dos tokens do Sync, que hoje estão em texto puro no repositório público e precisam ser
rotacionados"*.

**Também registrado, e não é credencial:** o e-mail pessoal da artesã segue em arquivo versionado
(`ilhas/clubedomosaico/PROMPT.md`, 5 linhas, e `ESTADO.md`, 2). Mesma pendência de 14/09, **aberta há 7 dias**, e é
dado de uma pessoa de verdade — decisão dele, não minha.

---

## Pendências do Pente Fino anterior (16/09/2026)

| # | o que é | estado hoje | há quanto tempo |
|---|---|---|---|
| **G1** | links de afiliado que o disparo dava como gravados não estavam no `main` | **FECHADO** — medido hoje: **95 de 95** publicáveis com `url_busca`, `url_busca_produto`, `degrau` e `conferido_em`, zero vazios. A dívida do elo morreu em 20/09 15h30Z | — |
| **G2** | a DEFINIÇÃO DE PRONTA exigia `afiliado.url` e `rel="sponsored"` em todo item | **FECHADO** — o item 1 foi reescrito com o texto proposto e fechado em 16/09, remedido em 20/09 | — |
| **G3** | dois dos cinco itens do prazo não podiam ser fechados pela Fundação | **FECHADO** — o item 3 deixou de ser `[RAPHAEL]` em 20/09, com a causa escrita | — |
| **G2 (de 14/09)** | o piso da 25.2 não existia em ilha nenhuma | **FECHADO** na robometria: 95 de 95 com piso rastreável | — |
| **G4 (de 14/09)** | token do Sync em texto puro | **ABERTO** (acima) | **7 dias** |
| **M10** | `ultima_ronda` e `bloqueada_por` ausentes em duas ilhas | **ABERTO** (M12) | **5 dias** |
| **B3 (de 14/09)** | o `PAINEL.md` atrasado | **ABERTO e pior** (B14) | **7 dias** |
| — | logo do Clube do Mosaico: 52 px × 64 px | **ABERTO**, idêntico, e agora com um irmão (M10) | **7 dias** |
| — | `aquametria/ARVORE.md` "37" × "36 registros" | **ABERTO e pior:** o banco tem **39** (M8) | **7 dias** |
| — | `clubedomosaico/ARVORE.md` "11 URLs" × tabela de 14 linhas | **ABERTO**, e agora são **três** números: o `ESTADO.md` diz 13 | **5 dias** |
| — | `fila.md` lista 3 ilhas nascidas e existem 5 | **ABERTO** | **5 dias** |
| — | a pausa da Bússola não existia no repositório | **FECHADO** — a nota de pausa está na §5 da `BUSSOLA.md` e é coerente com o `foco.md` e o `README.md` | — |
| — | reservas vencidas em três ilhas | **FECHADO** — os seis `ESTADO.md` estão com `executando_desde: null`, e a 1.2-b.5 passou a mandar a próxima execução limpar | — |

---

## O PADRÃO

1. **A distância entre as duas pontas encolheu de novo: agora é UMA EXECUÇÃO.** Em 14/09 o recorde era "mesmo
   commit"; em 16/09, nove minutos. Hoje é a mesma execução da Fundação **derrubando um número às 15h39Z e fechando
   o placar às 15h47Z sem reler a linha que ela mesma moveu** (G1). O padrão deixou de viajar entre pessoas e passou
   a caber dentro de um trabalhador só.
2. **Quem escreve a regra nova continua não varrendo quem ela contradiz.** A 1.2-b nasceu em 18/09 declarando o
   modo de medição e não tocou na 1.2, nem na 12, nem no mapa de leitura (G3, M2) — os mesmos três lugares que a
   1.2 não tocou dois dias antes. **É a segunda repetição literal do mesmo achado.**
3. **O defeito viaja em cópia, e a correção não viaja junto.** `url_busca_bruta` foi corrigido na Aquametria e na
   Robometria em 14/09 e continuou de pé nas duas ilhas novas (M1). O molde foi corrigido por um campo em 16/09 e
   continuou faltando outros dois (M3).
4. **O que envelhece pior não é a prosa: é a MEDIÇÃO GRAVADA COMO DADO.** O `cobertura-r1.json` afirma 15 e o
   comando devolve 11; o `ARVORE.md` afirma 37 e o banco tem 39; o `ESTADO.md` cita a revisão 77 do próprio
   cabeçalho, que diz 87. Número commitado parece conferido.
5. **Régua que não cobre o que o bloco mudou certifica a página de ontem — e aqui ela nem rodava.** O portão que
   mede a emenda do funil está **fora da bancada por classificação**: `bancada.py` chama `cobertura-` de
   "ferramenta de produção que não afirma nada", e o arquivo que ela grava é a única afirmação da ilha sobre o
   item 2 da PRONTA.

**A regra de processo que evitaria a próxima.** As duas propostas anteriores (10.x, o pedágio da busca, e 10.y,
critério de pronto nasce medido e diz de quem é cada item) **continuam não inseridas** e teriam pego seis dos doze
achados MÉDIO de hoje. Em vez de repeti-las pela terceira vez, proponho a que falta e que hoje custou o achado mais
caro — **PROPOSTA, NÃO INSERIDA**, porque é regra nova de política:

> ### 8.z QUEM MOVE UM NÚMERO RELÊ TODA AFIRMAÇÃO QUE DEPENDE DELE, NA MESMA EXECUÇÃO
>
> Toda execução que mudar um número do banco — anular um campo, entrar com uma leva, mudar uma régua de
> elegibilidade — faz duas coisas **antes de escrever o placar**, e o placar não vale sem elas:
>
> 1. **Roda de novo TODA ferramenta que deriva daquele número, não só a bancada.** A bancada é a lista das réguas
>    que *afirmam*; a conta que decide um critério de pronto pode estar numa ferramenta classificada como "de
>    produção", e é exatamente onde ela fica invisível. **Ferramenta cujo arquivo de saída é citado por um
>    critério de pronto, por um despacho ou por uma página é PORTÃO**, seja qual for o prefixo do nome dela — e
>    entra na bancada, mesmo que rodá-la custe mais que as outras juntas.
> 2. **Relê o placar inteiro, item a item, com o número novo na mão** — não só o item que o bloco estava fechando.
>    Um portão que nasce para proteger a página **subtrai** do banco por desenho, e o item que ele derruba quase
>    nunca é o item em que se estava trabalhando. **Declarar pronto sem reler o vizinho é a versão com prazo do
>    "consertar um ponto e não reler o resto do documento", que é o defeito que o Pente Fino existe para caçar.**
