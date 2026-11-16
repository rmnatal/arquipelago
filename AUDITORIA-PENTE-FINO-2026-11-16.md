# AUDITORIA PENTE FINO — 2026-11-16

Varredura de coerência do corpo de regras do `rmnatal/arquipelago`, rodada antes da Bússola, do estado real do
`main` (`dbc8b21`, 13/11/2026 19h48Z).

**Esta é a primeira auditoria em três semanas.** A anterior é de **26/10/2026**; não houve Pente Fino em 02/11
nem em 09/11. A janela auditada tem **367 commits** e **186 arquivos tocados** — e **clone COMPLETO, não raso**
(`.git/shallow` não existe; medido antes de contar, pela régua da **1.1**). Contei sobre os **1.530** commits do
`main`.

---

## O QUE FOI LIDO, E COMO

**Lidos inteiros, linha por linha (6):** `ARQUIPELAGO.md` (1.625 linhas) · `bussola/BUSSOLA.md` (405) ·
`bussola/cacados.md` (163) · `foco.md` · `ilhas/rodametria/VOZ.md` · `ilhas/rodametria/DESIGN.md`.

**Lidos em parte, nos trechos nomeados (12):** `bussola/fila.md` · `bussola/despacho-viagem.md` ·
`bussola/oportunidades/rodametria.md` · `dados/PAINEL.md` · `AUDITORIA-PENTE-FINO-2026-10-26.md` ·
`ilhas/ohmetria/ESTADO.md` (inteiro) e `PROMPT.md` · `ilhas/rodametria/ESTADO.md` e `PROMPT.md` ·
`ilhas/clubedomosaico/VOZ.md` e `DESIGN.md` · `ilhas/jornadafly/VOZ.md` e `DESIGN.md`.

**Medidos por régua ou varredura, sem leitura integral:** os **96** `ilhas/*/dados/*.json` (passados por
`json.load` e pela varredura do piso da 25.2/25.4-b, registro por registro) · os **7** `ilhas/*/ESTADO.md` pela
régua de presença da **§2** mais os dois campos da **21.6** · os **26** arquivos de lei de ilha
(`PROMPT.md`/`ESTADO.md`/`VOZ.md`/`DESIGN.md`) por varredura de token, endereço e mandato · os **15** arquivos de
`bussola/dossies/` por varredura de âncora de M e de veredito de SERP · e os **750** arquivos versionados por
varredura de segredo (e-mail, token, chave) e de mandato "toda ilha copia portão".

**Não verificado, e dito como tal:** os `ilhas/*/PROMPT.md` da aquametria, clubedomosaico, robometria e
jornadafly **não foram lidos inteiros** (8.206 linhas somadas) — foram varridos por régua. Os `REGISTRO.md` (43
mil linhas) não entram nesta varredura por desenho: são append-only e histórico.

---

## GRAVE — decisão tomada com base errada (0)

**Nenhum.** E os dois lugares onde eu esperava achar um foram medidos e estão sãos:

- **A régua de dinheiro da Bússola não está mais apontada para a Amazon.** A §3 da `BUSSOLA.md` hoje diz, com
  todas as letras, *"a Amazon NÃO é âncora de nada"*, e nos 5 dossiês as 7 menções à Amazon estão todas marcadas
  como a régua **derrubada**, com ponteiro para a seção que a derrubou. O defeito que criou este auditor está
  fechado nas duas pontas.
- **As caçadas de 09 e 12/11 aplicaram a régua NOVA, não a velha.** Apesar de o portão 3 da 0.2 ainda estar
  escrito com o piso de 1.000 visitas/dia (achado 2), as **25 linhas** de `cacados.md` daqueles dois dias
  reprovam pela conta da **0.9** (*"exigiria ≈ R$ X por venda em top-3"*), e a última nomeia o portão:
  `0.9 (comissão conservadora)`. A ficha que fez nascer a rodametria também cita a 0.9 e fecha em
  **R$ 20 mil/mês** no conservador, acima do piso de R$ 10 mil. **Nenhuma decisão foi contaminada.**

---

## MÉDIO — regra inconsistente, sem decisão contaminada (6)

### 1. `ilhas/ohmetria/` — a Bússola fechou o nicho desta ilha em 22/10/2026, e nenhum arquivo da pasta dizia isso. É a próxima da rotação. — **CORRIGIDO (ponteiro) + PRECISA DO RAPHAEL (desfecho)**

**O trecho.** `ilhas/ohmetria/PROMPT.md:1` é *"# ILHA: OHMETRIA — som automotivo"*, e a linha 4 manda ler o
dossiê que a aprovou. `bussola/cacados.md:11` registra:
`| 22/10/2026 | som automotivo | SERP de compra tomada por carrossel | 230 buscas/mês nas consultas de compra exatas |`.

**A contradição.** O dossiê aprovou o nicho na rodada 004; a reavaliação da **§4 da `BUSSOLA.md`** — *"toda
rodada reavalia o topo (SERP aberta fecha) (…) nicho aprovado que fechou tem que ser desmarcado antes de alguém
pagar domínio"* — o fechou em 22/10. **O domínio já estava pago** (14/09/2026, até 14/09/2028), então a régua da
§4 chegou tarde e nada diz o que se faz depois. Medido: **zero** ocorrências de reprovação, `cacados` ou 22/10
em qualquer arquivo de `ilhas/ohmetria/`, e **zero** menções a `ohmetria` na linha da caçada.

**A evidência de que isto não é histórico.** Medido hoje nos seis cabeçalhos de `ilhas/*/ESTADO.md`: ohmetria tem
a `ultima_execucao` **mais antiga do arquipélago** — 15/09/2026, cinco semanas à frente da segunda (aquametria,
21/10) —, `estado: nascendo` (que o passo 3 da §1 **não** descarta), `executando_desde: null` e `prioridade: 1`.
**No dia em que `foco.md` disser `ilha: nenhuma`, o passo 4 da §1 aponta para cá primeiro.** E a mesma ilha é a
única cujo cabeçalho não tem o campo `bloqueada_por` (achado herdado 48), então quem ler o passo 3 com `.get()`
trata a ausência como `null` sem nunca dizer que o campo não existe — a armadilha que a própria §2 nomeia:
*"campo ausente que se comporta como o valor certo espera o dia em que o valor certo muda"*.

**O que fiz.** Escrevi o ponteiro datado no topo do `PROMPT.md` (o arquivo que o passo 6 da §1 manda abrir) e uma
linha em "O que está travando" do `ESTADO.md`, nomeando a linha 11 de `cacados.md` e a medição da ordem da
rotação. **O ponteiro não decide nada.**

**O que sobra para ele.** O **desfecho** da ilha. A **1.2-b.4** pede um critério **pré-registrado** com três
desfechos (volta ao foco · manutenção · arquivada, com o aprendizado indo para a `BUSSOLA.md`), e esta ilha
nunca o recebeu. Escolher muda a ordem da fila e joga fora quatro blocos entregues (8.262 afirmações na bancada
da F1, 144 estados de resposta, 18 constantes) mais um domínio pago até 2028. **PRECISA DO RAPHAEL.**

### 2. `bussola/BUSSOLA.md` — o portão 3 do ciclo de caça ainda é o piso que a 0.9 substituiu, e a 0.1 declara inteiros dois portões que a 0.8 e a 0.9 mudaram — **CORRIGIDO (5 ponteiros)**

**O trecho.** 0.2, portão 3: *"A conta da 3.0-d com a 3.0-e, no cenário conservador. **Menos de 1.000
visitas/dia → próximo**."* E 0.1: *"Os portões (seções 2, 3, 3.0-c, 3.0-d, 3.0-e, 3.1) continuam valendo
**inteiros**"*.

**A contradição.** A **0.9** nomeia a 0.2 com todas as letras — *"**o portão 3 da 0.2 muda.** Em vez de 'menos de
1.000 visitas/dia no conservador → próximo', vale: comissão projetada no cenário conservador, só com produtos da
Shopee, de pelo menos R$ 10.000/mês"* — e diz que *"a 3.0-c.1 e a 3.0-d.1 (1.000 visitas/dia) **deixam de ser
eliminatórias**"*. A **0.8** passa a medir a cobertura da **seção 2** só na Shopee. As três são de **27/10/2026**
e estão na mesma seção 0: a 0.1 é a ponta velha. Junto, seguiam escritas como trava eliminatória, sem ponteiro, a
**3.0-c.1** (*"A trava, eliminatória"*, e o próprio título da 3.0-c, *"ou a ilha não nasce"*), a **3.0-d.1**
(*"A TRAVA, eliminatória"*) e a **3.0-d.5** (*"nicho que reprova aqui não vira ilha"*).

**A evidência.** A 0.2 não é prosa: é a lista que a Bússola **executa** em toda execução. É o arquétipo exato
desta auditoria — seção corrigida, seção vizinha descrevendo o mundo antigo. **Nenhuma decisão foi contaminada**
(ver GRAVE, acima): a prática já segue a 0.9.

**O que fiz.** Ponteiro datado na 0.1, no portão 3 da 0.2, na 3.0-c.1, na 3.0-d.1 e na 3.0-d.5. Nenhum número e
nenhuma régua de **como** se faz a conta de visitas foi tocado — a 3.0-c.2, a 3.0-d.2, a 3.0-d.3 e a 3.0-e.3
continuam inteiras e são o que alimenta a conta da 0.9.

### 3. `ARQUIPELAGO.md` — o número de seção **32.6** está usado duas vezes, e toda citação de "32.6" no repositório ficou ambígua — **CORRIGIDO (renumerada para 32.8)**

**O trecho.** Linha 1582: `**32.6 Ordem de aplicação:**` (21/10/2026). Linha 1590 (antes 1588):
`### 32.6 CAMPO QUE É PEDAÇO DE ORAÇÃO CONCORDA COM QUEM O USA` (11/11/2026).

**A contradição.** A primeira é a seção que a **32.6-b** estende, que a **32.5-c** cita (*"a 32.6-b já manda o
que se repete entre páginas virar componente da casca"*) e que os documentos das ilhas chamam de *"o despacho do
molde da 32.6"* em **mais de dez linhas** do `REGISTRO.md` e do `PROMPT.md` da rodametria. A segunda reusou o
número para outra regra.

**A evidência que autorizou o conserto.** Medido antes de renumerar: **nenhum arquivo do repositório citava a
regra de 11/11 por número** (`grep` de concordância, "pedaço de oração" e `ARTIGO_DA_CATEGORIA` devolve só prosa
e código, nunca uma citação numérica). Logo trocar o número **não deixa referência órfã**, e deixá-lo tornava
ambígua toda citação de "32.6". **32.7** era o último número usado da seção.

**O que fiz.** `### 32.6` → `### 32.8`, com a nota datada explicando a troca. Só o número mudou; o texto da regra
está byte por byte igual. Conferido depois: a seção 32 vai de 32.1 a 32.7 e depois 32.8, sem repetição.

### 4. `ARQUIPELAGO.md` 25.1 — o degrau 1 da escada manda procurar num lugar que o próprio contrato aposentou, e a 25.10 já nomeou o buraco sem fechá-lo — **CORRIGIDO (ponteiro)**

**O trecho.** 25.1: *"1. Loja oficial do fabricante na Shopee. **Achada no feed de afiliado** (ver 25.3)."*

**A contradição.** A **25.6** aposentou o feed em **16/09/2026**. A **25.10 (29/10/2026)** nomeia isso com todas
as letras — *"desde esse dia o degrau mais durável da escada **não tem como ser achado**: a regra diz onde
procurar, e o lugar não existe mais"* — e escreve a régua nova (o nome da loja carregar a marca do registro, com
**como** foi medido escrito no próprio registro; e `shopType` **não** é essa régua, porque é o programa de
vendedor da plataforma). **A 25.1 nunca recebeu o ponteiro**, e é ela que a Fundação lê ao escolher o degrau.

**O que fiz.** Risquei a referência ao feed e pus o ponteiro datado para a 25.10 dentro do degrau 1. Classe
"regra que cita ferramenta que o próprio contrato aposentou" — conserto inequívoco e sem perda.

### 5. `bussola/fila.md` — declara **aberta** uma contradição que o contrato fechou em 27/10/2026 — **CORRIGIDO (ponteiro)**

**O trecho.** O bloco *"A CONTRADIÇÃO QUE A RODADA 008 MEDIU E NÃO RESOLVEU — 3.0-d × 30.5"* fecha com *"Três
saídas, e nenhuma é da Bússola: (a) … (b) … (c) … **Nada foi aplicado: as contas desta página seguem a letra em
vigor**"*. Mais acima: *"o portão eliminatório da 3.0-d.1 segue fechado para todo nicho desta página"*.

**A contradição.** A **3.0-e** da `BUSSOLA.md` diz, datada de 27/10/2026 — **um dia depois desta página** —, *"o
Raphael escolheu a **saída (b)** da rodada 008"*, e a **3.0-e.3** aplica também a **saída (a)**, com os descontos
de carrossel (× 0,5), de resposta de IA (× 0,7) e de resposta que cabe no snippet (× 0,5). No mesmo dia a **0.9**
tirou o caráter eliminatório da 3.0-d.1. Quem abrir a `fila.md` hoje conclui que a decisão está pendente.

**O que fiz.** Ponteiro datado no topo do bloco. **Não reescrevi nada**: a **0.3** diz que esta página é registro
de medição e só recebe linha quando houver ficha. O que mudou é que ela deixou de declarar aberta uma decisão já
tomada.

### 6. `ARQUIPELAGO.md` seção 0 — a linha da Bússola no mapa de leitura não tinha a seção 30, e a `BUSSOLA.md` manda a Bússola decidir por ela — **CORRIGIDO**

**O trecho.** Mapa de leitura: *"| **Bússola** | **7**, 10, 11, **12.2**, 14, **15**, 20, 21 |"*.

**A contradição.** O portão 1 do ciclo de caça (0.2) manda classificar a SERP *"(seção 3 e **seção 30.5** do
`ARQUIPELAGO.md`)"*, e a 0.6 afirma que o Chrome dela *"satisfaz a **30.8** do `ARQUIPELAGO.md` para `alvo`"*.
Duas seções que a linha dela mandava, ao pé da letra, **não ler**. A nota de 12/10 do próprio mapa escreveu que a
30 *"não entrou em linha nenhuma"* e a pôs só na da Fundação, porque ali quem cria a página é a Fundação — e isso
mudou em 27/10, quando a seção 0 da `BUSSOLA.md` nasceu.

**A evidência.** É a mesma falha que este mapa já registrou **quatro** vezes (a 1.2 em 16/09, a 1.2-b em 21/09,
as três seções da Bússola em 05/10, a 25 e a 30 em 12/10): *a seção que decide não está na linha de quem decide*.

**O que fiz.** `30` acrescentada à linha da Bússola, com a nota datada. O desempate é o da própria seção: *"errar
por ler a mais é barato; errar por não saber a regra custa uma leva inteira"*.

---

## MÉDIO — PRECISA DO RAPHAEL, novos (2)

### 7. A 0.8 da `BUSSOLA.md` fecha o portão 4 para nicho de SERVIÇO, e a seção 2 e a seção 3 da mesma lei o mantêm aberto

A **0.8 (27/10/2026)**: *"no portão 4 da 0.2 a cobertura da seção 2 se mede **SÓ na Shopee**: 7 de 10 produtos
que a ferramenta indicaria precisam estar na Shopee (…) nicho que só passa contando Mercado Livre reprova no
portão 4"*. A **seção 2**, ampliada por decisão dele em 13/09/2026, admite *"serviço com preço e condição
publicados por quem opera — passeio, ingresso, seguro, plano"* e diz que *"marketplace não é requisito"*. A
**seção 3** ancora o M *"no programa próprio do operador quando a ilha for de serviço"*. **Nenhum passeio,
ingresso ou seguro está na Shopee** — então, lido ao pé da letra, nicho de serviço reprova no portão 4 **por
definição**, e a porta que a seção 2 abriu em 13/09 fechou sem ninguém dizer. O caso tem nome e está no
repositório: `bussola/despacho-viagem.md`, o nicho que ele aprovou em 13/09 e que virou a ilha `jornadafly`.
**Duas leituras defensáveis:** ou a 0.8 é só sobre marketplace e a seção 2 fica, ou a porta de serviço fechou e a
seção 2 e a seção 3 precisam dizer isso. **É decisão dele.**

### 8. A 0.6 diz que a SERP vista pela rotina no Chrome dele satisfaz a 30.8; a 30.8 exige olhos

A **0.6 (27/10/2026)**: *"A SERP vista nesse Chrome satisfaz a 30.8 do `ARQUIPELAGO.md` para `alvo`; **não existe
mais `provisório` por falta de olhos**"*. A **30.8 (14/10/2026)**: *"`alvo` exige a SERP **aberta com os olhos**
(…) A linha da lista registra **quem** viu e **quando**; ausência de um dos dois é reprovação, não omissão
tolerada"*. A própria `fila.md` da rodada 008 escolheu a leitura conservadora e deixou **dois** `alvo` em
`provisório`, justamente porque *"o instrumento novo não é o Chrome dele e não teve olhos humanos"*. O que isto
decide é se o veredito `alvo` de uma rotina autoriza **gastar orçamento de rastreamento** — a assimetria que a
30.8 existe inteira para proteger (*"errar para o lado de publicar é a leva inteira"*). **É decisão dele.**

---

## BAIXO (1)

### 9. `ARQUIPELAGO.md` §2, último parágrafo — a ordem está meio cumprida

O parágrafo de 26/10/2026 fecha com *"quem reservar a `robometria` ou a `ohmetria` acrescenta os dois campos no
mesmo commit em que fechar o bloco"*. Medido hoje com a própria régua de presença da §2: a **robometria tem os
oito campos** e **só a `ohmetria`** falha, nos dois. A medição datada do parágrafo continua certa sobre 26/10; é
a ordem que envelheceu pela metade. **Não corrigido** — o texto é registro datado, e quem fecha bloco conserta o
cabeçalho da ilha que reservou, nunca o de outra.

---

## HERDADOS QUE CONTINUAM ABERTOS — PRECISA DO RAPHAEL (14 de 16)

Sem reabrir a discussão. Dois saíram da lista hoje, **resolvidos**:

- **#35 (foco sem item 4) — RESOLVIDO.** `foco.md` nomeia a **rodametria** desde 27/10/2026, com a decisão escrita
  dele (*"Foco total nesse projeto agora. Total e absoluto"*) e `fila_decidida_pelo_raphael` preenchida.
- **#47 (a Bússola declarada pausada enquanto rodava) — RESOLVIDO.** A §5 da `BUSSOLA.md` traz a pausa **riscada**
  e marcada *"REVOGADA EM 27/10/2026 pela seção 0 — a Bússola está ligada, em modo caçador"*.

| # | o que é | herdado de | semanas | medido hoje |
|---|---|---|---|---|
| 36 | `jornadafly/VOZ.md` manda um lockup e uma cor que o `DESIGN.md` declarou descartados, e a §22.2 dá o desempate ao arquivo velho | 12/10 | **5** | o `VOZ.md:39` segue com *"`JORNADA` em 700 + `fly` em 400, coladas"*; o `DESIGN.md` segue com o monograma em "J", `#378AD0`, e os quatro lockups oficiais |
| 37 | o `alicate` da clubedomosaico tem três endereços escritos para a mesma camada, e um está no ar | 21/09 | **8** | os três seguem: `/materiais/alicate-para-mosaico/` (3 ocorrências), `/materiais/alicates-e-corte/` (5) e `/materiais/alicates/` (1) |
| 38 | a 16.6 escrita no `PROMPT.md` da clubedomosaico proibiria as páginas que a §30 autorizou | 12/10 | **5** | sem mudança |
| 39 | M9 — a camada de coleção da Loja tem três desenhos de URL escritos e um publicado; mexe em peça da mãe dele | 21/09 | **8** | sem mudança |
| 40 | `/metodologia/` na raiz: duas ilhas atribuem a permanência à §16.1, e a §21.7 diz o oposto com ela nomeada | 14/09 | **9** | `robometria/ARVORE.md:64` segue com o veredito, e a lista de cinco da §16.1 segue sem ela |
| 41 | §20.4, §20.9, §22.8 e §29.4 mandam toda ilha ganhar um portão que a §31.2 proíbe criar — **e o conflito CRESCEU** | 26/10 | **3** | eram 2 mandatos, são **4**. Medido: `conferir-desembarque.py` (§20.4) em **2 de 6** ilhas (falta na robometria e na rodametria); `veredito_da_revisao_atrasada` (§20.9) em **1 de 6**, só na rodametria; `teste-cura-da-porta` + a seção da cura na casca (§29.4) em **2 de 6**, faltando na aquametria e na **robometria, cuja porta caiu em 30/10 e 11/11**; `teste-desenho.mjs` (§22.8, de 12/09) em **0 de 6** |
| 42 | a §31.6 manda item de prioridade alta abaixo de 7 em 10, e o despacho de 21/10 declarou que não é | 26/10 | **3** | sem mudança |
| 43 | o `esquema-banco.json` da jornadafly não exige o piso que a §25.2 declara inegociável — **e a dívida CRESCEU** | 05/10 | **6** | eram **4** registros sem `url_busca`/`degrau`/`conferido_em`; são **6 de 6**, e o próprio arquivo os conta em `itens_com_piso_nao_rastreavel: 6` (recontei, confere). As duas leituras defensáveis continuam: emendar a §25 para nicho de serviço, ou emendar o esquema |
| 44 | o `esquema-banco.json` da ohmetria declara `url_busca.obrigatorio: false` com uma nota que contradiz a §25.2 | 26/10 | **3** | a nota segue literal (*"é dívida de comissão, nunca defeito de página"*), e o banco segue com **0** registros — a trava continua escrita para o dia em que ele encher |
| 45 | **SEGREDO** — token do Sync em texto puro | 14/09 | **9** | **estabilizou**: **16 linhas em 4 arquivos, 3 ilhas** (aquametria `REGISTRO.md` 12, `PROMPT.md` 1, clubedomosaico `PROMPT.md` 2, robometria `PROMPT.md` 1) — o mesmo que em 26/10, depois de ter crescido 4 linhas na quinzena anterior. Rotação continua sendo o único conserto real. **Nenhum valor escrito aqui nem em commit.** E as duas coisas baratas continuam não feitas: o `.gitignore` tem **5 linhas** e nenhuma menção a `.env`, `*.pem`, `*.key` ou JSON de conta de serviço; o `ilhas/_modelo/PROMPT.md` tem **0** menções a segredo, token ou credencial |
| 46 | **SEGREDO** — o e-mail pessoal da artesã em arquivo versionado, inclusive em snippet de produção | 14/09 | **9** | **estabilizou em 25 ocorrências, 9 arquivos**, entre eles `snippets/clubedomosaico-leads.php` e `snippets/clubedomosaico-atelie.php`. Envolve dado pessoal de terceiro: registro, não conserto |
| 48 | `ilhas/ohmetria/ESTADO.md` sem `ultima_ronda` e sem `bloqueada_por` | 16/09 | **9** | **é a única dos sete** que falha na régua de presença da §2, e falha nos dois — e agora é a ilha do achado 1, a próxima da rotação. A robometria foi acertada. *(Na mesma medição: `clubedomosaico` segue com `primeira_indexacao: 'desconhecida'`, que não é "data ou null" como a 21.6 pede)* |
| 49 | a régua de presença da §2 não cobre os dois campos que a §21.6 exige | 26/10 | **3** | a régua segue conferindo os **oito** da §1; medido hoje, os sete cabeçalhos **têm** `piso` e `primeira_indexacao`, então ampliá-la não reprovaria ninguém — mas ampliar o que um portão cobra continua sendo escolha |
| 50 | `dados/PAINEL.md` escreve narrativa, histórico e opinião, que a §23.3 proíbe | 12/10 | **5** | o painel de 13/11 tem seções inteiras de prosa (*"Ilha da ronda funda de hoje"*, *"AS DUAS ILHAS QUE CAÍRAM EM 11/11"*, *"O que a rodametria mediu hoje"*). A prosa é boa; a §23.3 é literal |

---

## O QUE VERIFIQUEI E NÃO É ACHADO

Dito porque zero achado é resultado, e porque **cinco suspeitas minhas morreram na medição**:

- **O piso da 25.2 está INTEIRO em todas as ilhas no ar — e os 11 registros sem `url_busca` que a varredura
  acusou não são publicáveis.** Medido registro por registro: robometria `pecas.json` 3 sem piso, **os 3 com
  `status: excluido_do_banco`** (54 publicáveis, 54 com piso); `modelos-robo.json` 5 sem piso, **4
  `excluido_do_banco` e 1 `nao_publicavel`** (45 publicáveis, 45 com piso); rodametria `pecas.json` e
  `veiculos.json` com `publicar: false` no topo e os itens em `rascunho`, **cada um com a CAUSA escrita no
  formato da 25.4-b.3**. Nada a consertar. A única exceção é a jornadafly, que é o herdado 43.
- **Os 96 `ilhas/*/dados/*.json` parseiam, 0 falham.** E os 7 cabeçalhos de `ESTADO.md` parseiam em
  `yaml.safe_load` — inclusive depois das minhas duas edições na ohmetria, que reconferi.
- **Os números do `PAINEL.md` batem com os arquivos, pela 23.4.** `urls_publicadas` conferido um a um: rodametria
  10, aquametria 52, robometria 14, clubedomosaico 44, ohmetria 0, jornadafly 0 — iguais aos seis cabeçalhos.
- **A Amazon não ancora nada em lugar nenhum.** Varrido o contrato, a `BUSSOLA.md`, a `fila.md` e os 5 dossiês: as
  7 menções que existem estão **todas** marcadas como a régua derrubada, com ponteiro. O arquétipo desta auditoria
  está fechado.
- **`clubedomosaico/VOZ.md` carrega 5 cores em hexadecimal, e as 5 são idênticas às do `DESIGN.md`.** Suspeitei do
  padrão do herdado 36 numa segunda ilha e ele não existe: `#FFFFFF`, `#E9DCD7`, `#1F1715`, `#FC483B` e `#69030C`
  estão nos dois arquivos com o mesmo valor. Token no arquivo errado pela §22.6, não contradição.
- **Os dois despachos não riscados da rodametria não contradizem o `ESTADO.md`.** Ele declara *"nenhum despacho
  aberto para a Fundação"*, e os dois abertos (11/11 e 04/11, leituras semanais) dizem, cada um no próprio
  cabeçalho, *"o que sobra não é da Fundação"* e *"nenhum dos dois é da Fundação"*. É a 18.3 sendo cumprida, não
  burlada.
- **A exceção do símbolo da rodametria está registrada do jeito certo.** O `DESIGN.md` dela contraria a §5(e) da
  `BUSSOLA.md` (*"o símbolo não desenha o produto"*) e **declara a exceção, nomeia quem decidiu, datou e limitou o
  alcance**: *"Decisão dele, vale só para a Rodametria"*, com o registro das recusas para ninguém restaurar. É o
  contraexemplo saudável desta auditoria.
- **Os dossiês de `camametria` e `pneumetria` existirem sem ficha não é defeito.** A 0.7 revogou a *obrigação* de
  manter dois dossiês prontos; não mandou apagar os que existem, e apagá-los seria jogar fora trabalho feito.

---

## O PADRÃO

1. **Os seis achados são a mesma falha, e ela não é esquecimento: é que a decisão nova nasce em lugar NOVO.** A
   0.9 nasceu como seção 0.9 em vez de reescrever o portão 3 da 0.2; a 25.10 nasceu como 25.10 em vez de emendar o
   degrau 1 da 25.1; a 3.0-e nasceu em vez de fechar o bloco da `fila.md` que a pedia. Escrever em lugar novo é
   **certo** — preserva a causa, que é o que a 28.4 protege. O que falta é o passo de volta.
2. **A ponta velha é sempre a OPERACIONAL, e é por isso que custa.** Em cinco dos seis, o texto que ficou velho é
   o que alguém **executa**: a lista do ciclo de caça, o degrau que se grava no banco, a linha do mapa de leitura,
   o `PROMPT.md` que a rotação abre. A regra nova fica na prosa e a velha fica no procedimento.
3. **Quatro dos seis estão a UMA LINHA de distância da regra que os conserta** — a 0.9 já diz "o portão 3 da 0.2
   muda", a 25.10 já diz que o degrau 1 ficou sem régua, a 3.0-e já diz que escolheu a saída (b). **O defeito não
   é não saber: é a regra nova não ter ido escrever o ponteiro na régua velha.**
4. **E o pior deles é o que não tinha ponteiro nenhum** (achado 1): a Bússola fechou um nicho num arquivo e a ilha
   daquele nicho, em outra pasta, nunca soube. Entre dois cérebros, ninguém era dono do passo de volta.

**A regra de processo que evitaria a próxima** — cabe na §3 do `ARQUIPELAGO.md`, ao lado de *"regra nova do
Arquipélago se escreve AQUI, uma vez"*. **NÃO INSERIDA**, porque é regra nova de política:

> **3.x REGRA NOVA FECHA A VELHA NO MESMO COMMIT, E "FECHAR" É DEIXAR PONTEIRO NO LUGAR ONDE A VELHA É
> EXECUTADA.** Toda seção, decisão ou medição que **substitui**, **afrouxa** ou **estreita** uma régua existente
> nasce com duas escritas no mesmo commit: a dela, e um **ponteiro datado no trecho velho** — e o trecho velho é
> o **operacional**, não o explicativo: a lista de passos que alguém executa, o campo que alguém grava, a linha do
> mapa de leitura de quem decide, o `PROMPT.md` da ilha afetada. Quem escreve a regra nova roda `git grep` do
> número e do nome da régua que ela muda e **diz no commit quantos lugares achou e quantos fechou**; zero fechados
> com mais de zero achados é commit incompleto. **E a regra atravessa cérebro:** decisão de um (Bússola, Sentinela,
> Fundação) que muda o chão de outro escreve o ponteiro **na pasta do outro**, porque ninguém lê o arquivo de quem
> não é. Ponteiro é barato; a frase velha executada é a leva inteira.

---

*Auditoria rodada em 16/11/2026. 6 achados MÉDIO (6 corrigidos no ponto operacional, 1 deles com o desfecho
reservado a ele), 2 MÉDIO que precisam dele, 1 BAIXO, 14 herdados ainda abertos, 2 herdados resolvidos. Nenhum
GRAVE. Nenhum valor de segredo escrito neste arquivo nem em commit.*
