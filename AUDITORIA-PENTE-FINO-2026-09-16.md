# AUDITORIA PENTE FINO — 16/09/2026

Rodada 4, **fora de horário**, pedida pelo Raphael na conversa. O disparo veio com foco declarado: o contrato mudou
**quatro vezes hoje de manhã** (commits `be4b3a1` 11h33Z, `c3a7f3b` 11h39Z e `15b3f83` 11h42Z) e ninguém releu o
conjunto depois. Auditei do `main` real, `15b3f83`.

## O que foi lido

**33 documentos de lei, inteiros:** `ARQUIPELAGO.md` (835 linhas), `foco.md`, `README.md`, `bussola/BUSSOLA.md`,
`bussola/fila.md`, `bussola/despacho-viagem.md`, `dados/PAINEL.md`, `dados/despachos.md` (527), `dados/consertos.md`,
os **6** `PROMPT.md` (cinco ilhas + `_modelo`), os **5** `VOZ.md`, os **5** `DESIGN.md`, os **3** `ARVORE.md`
(aquametria, clubedomosaico, robometria), os 4 arquivos dos dois dossiês, e o relatório do Pente Fino de 14/09.
**Mais os 6 `ESTADO.md`: 39 arquivos.** Cabeçalho passado por `yaml.safe_load` (os seis parseiam) e conferido campo
a campo contra a seção 2; o corpo dos dois mais longos (aquametria 523 linhas, robometria 504) lido inteiro.

**Honestidade sobre quem leu o quê:** li eu mesmo, inteiros, o contrato, os dois arquivos da Bússola, o painel, os
despachos, o `PROMPT.md` e o `ESTADO.md` da robometria, o molde e o relatório anterior. Os 13 arquivos das quatro
ilhas fora do foco e os 4 dos dossiês foram lidos inteiros por duas varreduras auxiliares que instruí com regra
dura de não inventar achado — **e nenhum achado delas entrou neste relatório sem eu abrir o arquivo e reler o
trecho na fonte.** Os dois desencontros que elas trouxeram e eu não pude confirmar como defeito vivo ficaram de
fora, de propósito.

**Medição, não leitura:** os **68 registros publicáveis** de `ilhas/robometria/dados/pecas.json` (35) e
`modelos-robo.json` (33), campo de afiliado a campo de afiliado; as duas varreduras de cobertura da ilha rodadas
(`cobertura-r1.py`, `cobertura-r2.py`); e as **9 URLs do sitemap da robometria abertas no ar**, com
`Accept-Encoding: identity` e quebra de cache, medindo `meta description`, `og:`, `rel="sponsored"` e a frase
"em breve". `git log --since="7 days ago" --name-only` para começar pelo que mudou.

**Achados: 19** — 3 GRAVE · 10 MÉDIO · 6 BAIXO. **11 corrigidos**, **8 registrados** (6 deles PRECISA DO RAPHAEL).
Mais **4 pendências herdadas** da rodada de 14/09, abertas há 2 dias.

> **Resposta curta às seis perguntas do disparo, antes do detalhe:** a 1.2 **contradiz** a 18.1 e o pórtico da
> seção 1 — a ponta velha é a 18.1 (11/09), e corrigi com ponteiro sem mexer na ordem dela (M1). A 1.2 **não**
> deixa a Fundação sem saber o que fazer no passo 4: a suspensão está explícita. Sim, **quatro `PROMPT.md` de ilha
> descreviam o mundo sem foco** e um deles manda "modo mutirão, entregue quantos blocos couberem" (M2, corrigido).
> A **definição de pronta contradiz sim** o despacho do Raphael de 14/09 no mesmo arquivo (G2) e traz dois itens
> que a Fundação não consegue fechar sozinha (G3). **Dos cinco itens, um já está atendido** (item 5, medido no ar
> hoje) e outro tinha a linha de base de três dias atrás (item 2). E a medição que você pediu: **68 de 68
> publicáveis seguem sem `url_busca` e sem `url_produto`** — os links de afiliado que o disparo diz terem sido
> gravados hoje **não estão no `main`** (G1).
>
> **E o padrão aconteceu de novo AO VIVO, como em 14/09:** às 12h13Z, no meio desta auditoria, o commit `f370a2f`
> fechou o item 4 da definição de pronta **medindo** — o sitemap estava processado desde 15/09 e ninguém precisava
> reenviar nada. Seis dias de "metade humana" que eram espera. Ver G3.

---

## GRAVE — decisão foi ou está sendo tomada com base errada

### G1. Os links de afiliado que o disparo dá como gravados hoje NÃO estão no `main`, e o campo continua vazio em 68 de 68

- **Arquivos:** `ilhas/robometria/dados/pecas.json` e `ilhas/robometria/dados/modelos-robo.json`.
- **O que o disparo diz:** *"nesta manhã foram gravados links de afiliado em `pecas.json` e `modelos-robo.json`,
  no campo `afiliado.url_busca`"*.
- **A medição, contada e não presumida** (`status: publicavel`, os dois bancos):

  | banco | publicáveis | sem `url_busca` | sem `url_produto` | sem `degrau` | sem `conferido_em` |
  |---|---|---|---|---|---|
  | `pecas.json` | 35 | **35** | **35** | 0 | 0 |
  | `modelos-robo.json` | 33 | **33** | **33** | 0 | 0 |
  | **total** | **68** | **68** | **68** | **0** | **0** |

  `afiliado.url_busca` é **string vazia** nos 68; `afiliado.url` também. O que está preenchido nos 68 é
  `afiliado.url_busca_produto` — a busca **crua**, que não rastreia e não paga comissão — com
  `motivo_sem_url_busca` dizendo, item a item, que *"falta o ENCURTAMENTO, não a escolha"*.
- **A prova de que não é leitura minha:** o último commit que tocou qualquer um dos dois arquivos é **`0a02bd1`,
  de 14/09/2026 23h31Z**. Nenhum commit de hoje toca a pasta `ilhas/robometria/dados/`.
- **Por que é GRAVE:** o item 1 da DEFINIÇÃO DE PRONTA, com prazo de 23/09, é exatamente esse campo. Se alguém
  acredita que ele foi preenchido hoje, o placar da ilha nasce errado e a dívida some da mesa sem ter sido paga.
- **O que eu fiz: PRECISA DO RAPHAEL.** Não inventei explicação. As possibilidades que os dados admitem são duas
  e nenhuma é minha para escolher: ou o trabalho foi feito e **não foi empurrado** (branch, execução que morreu
  antes do push, ou `main` reescrito — o `git fetch` desta execução veio com *"forced update"*), ou ele não
  aconteceu. **A checagem é de um minuto e é dele:** se havia uma execução gerando link no painel da Shopee hoje,
  ela não chegou ao repositório.

### G2. A DEFINIÇÃO DE PRONTA exige `afiliado.url` e `rel="sponsored"` em todo item — as duas coisas que o contrato e o despacho do Raphael de 14/09 decidiram, com medição, que NÃO valem aqui

- **Arquivo:** `ilhas/robometria/PROMPT.md`, "DEFINIÇÃO DE PRONTA — PRAZO 23/09/2026", item 1.
- **O trecho:** *"Todo item publicável com `afiliado.url` preenchido, `rel="sponsored"` no link e o aviso de
  comissão visível na página."*
- **As duas pontas que ele derruba, as duas datadas e as duas acima dele no mesmo arquivo ou no contrato:**
  - `ARQUIPELAGO.md` §25.2 — *"**A ficha de produto (`url`) é BÔNUS, não requisito.** … Quando não existir …
    **a busca sobe e vira o botão** — sem esperar decisão humana"*. A §25.2 diz de si mesma que *"manda na seção
    inteira e desempata todo conflito"*, por decisão textual do Raphael de 13/09.
  - `ilhas/robometria/PROMPT.md`, DESPACHO DO RAPHAEL — 14/09/2026, item 4, marcado **CUMPRIDO E CONFERIDO NO AR**:
    *"**A busca crua sai SEM `rel="sponsored"`**: ninguém paga por aquele clique"*, e a `/divulgacao-de-afiliados/`
    foi reescrita para dizer ao leitor qual link rende comissão e qual não rende.
- **A evidência medida hoje no ar, nas 9 URLs do sitemap:** **zero** ocorrências de `rel="sponsored"` e **zero**
  ocorrências de "em breve". Ou seja: a ilha, hoje, está obedecendo à ponta que a definição de pronta contradiz —
  e cumprir o item 1 ao pé da letra significaria **carimbar de patrocinado 68 links que ninguém paga**, que é
  afirmação falsa ao Google e ao leitor.
- **O "pronto quando" do próprio item 1 não cobra nada disso:** ele pede só que a varredura não ache "em breve"
  nem item publicável sem link — e isso **já está satisfeito** (65 → hoje 68 de 68 com saída pelo piso).
- **O que eu fiz: PRECISA DO RAPHAEL.** Não corrigi: mexe no que a ilha publica e no que conta como PRONTA.
- **Texto proposto para o item 1, se ele concordar** (não inserido):
  > 1. **PORTA DE COMPRA EM TODO ITEM PUBLICÁVEL.** Nenhum cartão com "Link de loja em breve". Todo item
  > publicável com saída de compra pela escada da 25.1, parando no primeiro degrau que servir, e o aviso de
  > comissão visível na página. `rel="sponsored"` **só** no link que rende comissão (ficha ou busca encurtada);
  > a busca crua sai sem ele, e o cartão diz qual é qual. **Pronto quando:** uma varredura das páginas no ar não
  > encontra a frase "em breve", não encontra item publicável sem saída, e a página de divulgação declara as duas
  > contas — quantos itens têm saída e quantos rendem comissão. *(A meta de receita — os 68 com `url_busca`
  > encurtada — continua existindo, mas como **dívida do elo da Shopee**, não como critério de PRONTA, porque ela
  > não depende da Fundação.)*

### G3. Dois dos cinco itens do prazo de 23/09 não podiam ser fechados pela Fundação — e um deles se resolveu DURANTE esta auditoria, medindo

> **ATUALIZAÇÃO, 12h13Z, escrita antes do meu push:** enquanto eu redigia isto, o commit `f370a2f` fechou o
> **item 4**. E fechou do jeito certo, que é a parte útil: **ninguém reenviou nada** — alguém foi ao Search
> Console e MEDIU. O sitemap estava *processado desde 15/09, com 9 páginas encontradas*. O "Não foi possível
> buscar" de 10/09 era espera de domínio novo e se resolveu sozinho, enquanto seis dias de "metade humana"
> ficaram registrados como pendência do Raphael. **Isso não enfraquece este achado: é a prova dele.** Um item de
> pronto que nunca foi remedido travou a rampa da seção 14 por seis dias sem motivo. O que segue aberto é o
> item 3 — e a lição de medir antes de despachar entrou no próprio arquivo, por quem mediu.

- **Arquivo:** `ilhas/robometria/PROMPT.md`, DEFINIÇÃO DE PRONTA, itens 3 e 4.
- **Item 4 — SITEMAP ACEITO NO SEARCH CONSOLE — fechado às 12h13Z de hoje (ver a atualização acima).** Quando eu
  o li, o próprio item admitia *"É metade humana e está no despacho de 10/09"*. O despacho de 10/09, no mesmo arquivo, é literal: *"**FALTA A METADE HUMANA, e ela não é da Fundação:**
  reenviar o sitemap no Search Console … **Exige o navegador do Raphael ou credencial de conta de serviço que
  este ambiente ainda não tem**"*. E a §11, passo 9, confirma: sem a credencial, a leitura é no navegador dele.
- **Item 3 — ZERO DEFEITO ABERTO DE RONDA**, com o critério *"as seções de despacho não tiverem item sem
  'CUMPRIDO E CONFERIDO NO AR'"*. Contados os itens que sobram nas seções de despacho deste arquivo: **três**, e
  os três se declaram do Raphael — o item 4 do despacho da Sentinela de 14/09 (*"Continua sendo linha de 'Precisa
  do Raphael'"*, o encurtamento da Shopee), o item 5 do mesmo (*"essa linha é do Raphael, não da Fundação"*) e a
  metade humana do sitemap, que é o item 4 acima contado duas vezes.
- **Por que continua GRAVE e não MÉDIO, mesmo com o item 4 fechado:** o prazo de 23/09 foi dado como "nossa parte", e a própria seção escreve
  *"cumprir os cinco itens até 23/09 é a nossa parte, e é a única parte que depende de nós"*. **Um dos cinco não depende de nós, e um segundo passou seis dias
  parecendo não depender sem ninguém remedir.** A Fundação vai rodar 4 vezes por dia útil contra uma lista em que 40% é dele, e o placar
  obrigatório de toda execução vai mostrar dois itens vermelhos que nenhuma execução consegue apagar.
- **O que eu fiz: PRECISA DO RAPHAEL.** A saída barata é uma linha, não uma reescrita: marcar o item 3 (e todo
  item futuro nessa condição) como **[RAPHAEL]**, do jeito que a §11 já marca o passo 1, e deixar o placar dizer "esperando o Raphael" em vez de
  "faltando". **O prazo continua de pé; o que muda é de quem é cada item.**

---

## MÉDIO — regra inconsistente, sem decisão contaminada

### M1. A 1.2 nasceu suspendendo a rotação e a 18.1 continuou mandando o contrário — **CORRIGIDO (ponteiro, sem mexer na ordem)**

- **Arquivos:** `ARQUIPELAGO.md` §1 (pórtico) e §18.1 × §1.2.
- **A contradição:** a 18.1 (11/09) diz *"Prioridade de ilha (substitui a rotação da seção 1 quando houver
  conflito) … (1ª) ilha com DESPACHO aberto no topo do `PROMPT.md`"*, e a 1.2 (16/09) diz *"Despacho NORMAL de
  ilha fora do foco **espera**, por mais antigo que seja"*. As duas falam de prioridade e a 1.2 não nomeou a 18.1.
  **A ponta velha é a 18.1**, por data e porque a 1.2 é decisão do Raphael de hoje. Agrava: pelo mapa da seção 0,
  a **18 está na leitura obrigatória de TODO papel** e a 1.2 não estava na de ninguém (ver M3).
- **O que eu fiz: CORRIGIDO.** A 18.1 ganhou o ponteiro no começo e a frase "com o foco em `nenhuma`, a ordem é";
  **a ordem dela não foi alterada** e volta inteira quando o foco sair. O pórtico da seção 1 idem.

### M2. Os quatro `PROMPT.md` de ilha fora do foco mandavam trabalhar normalmente, e um deles manda MUTIRÃO — **CORRIGIDO**

- **Arquivos:** `ilhas/aquametria/PROMPT.md`, `ilhas/clubedomosaico/PROMPT.md`, `ilhas/ohmetria/PROMPT.md`,
  `ilhas/jornadafly/PROMPT.md`. Nenhum dos quatro mencionava `foco.md` nem a 1.2.
- **Os trechos que mais doem, todos no presente do indicativo:** aquametria — *"**MODO MUTIRÃO, ligado em
  09/09/2026 a pedido do Raphael:** … Entregue quantos blocos couberem na sessão"* e *"**Sentinela técnica**, todo
  dia 11h30 BRT … Disparo dela com defeito descrito **tem prioridade sobre a fila**"*; ohmetria — *"Os blocos 1, 2,
  3 e 3c NÃO dependem de domínio nem de site. **Comece por eles hoje**"*; jornadafly — *"**casca + 1 ferramenta +
  sitemap no ar em até 48 h** … O relógio do Google já corre"*.
- **Por que é a família mais cara:** é **ordem velha**, não prosa velha. Uma execução que abra um desses arquivos
  obedece, e obedecer aqui custa a execução inteira da ilha em foco.
- **O que eu fiz: CORRIGIDO.** Cada um dos quatro ganhou, no topo, um aviso de cinco linhas dizendo que a ilha não
  está em foco, que nada ali é executado enquanto isso valer, e **como desligar o aviso** (`foco.md` em `nenhuma`).
  Nenhuma linha de conteúdo foi apagada.

### M3. A regra que manda nas duas Sentinelas morava numa seção que o mapa de leitura proíbe as duas de ler — **CORRIGIDO**

- **Arquivo:** `ARQUIPELAGO.md` §0, tabela de papéis.
- **A contradição:** a linha "Sentinela — ronda diária" listava `2, 3, 4, 10, 12, 15, 16, 18, 19, 21, 22, 23, 24`
  e a "leitura semanal", `2, 3, 4, 10, 12, 12.1, 14, 18, 21`. **A seção 1 não está em nenhuma das duas** — e o
  mapa abre dizendo *"Cada papel abre as seções da sua linha e para. Ler seção de outro papel não é zelo"*. A 1.2,
  escrita hoje, diz no próprio texto que *"mora na seção 1 por acidente de lugar, não de alcance"* e que vale para
  as duas Sentinelas. Escrita e invisível para quem ela governa.
- **O que eu fiz: CORRIGIDO.** A **1.2** entrou nas duas linhas de Sentinela e na lista "Sempre, para todo papel",
  com a causa escrita.

### M4. A seção 12 ainda mandava a ronda diária varrer por dívida, entre todas as ilhas — **CORRIGIDO (ponteiro)**

`ARQUIPELAGO.md` §12: *"**VERIFICAR POR DÍVIDA** … depois a ilha de `ultima_ronda` mais antiga"*, contra a 1.2:
*"Ronda diária: trabalha só na ilha em foco. Não abre, não mede e não relata nenhuma outra ilha."* É a seção que
as duas Sentinelas de fato leem. **CORRIGIDO** com a linha de suspensão datada; a regra de dívida fica escrita e
volta a valer quando o foco sair.

### M5. Dentro da própria 1.2, o parágrafo do custo descrevia o mundo de nove minutos antes — **CORRIGIDO**

- **Arquivo:** `ARQUIPELAGO.md` §1.2.
- **A contradição, medida no `git log`:** o parágrafo *"O que isto custa"* (commit `be4b3a1`, **11h33Z**) dizia
  *"**A Sentinela continua rondando todas** e continua escrevendo despacho"*. O parágrafo imediatamente seguinte
  (commit `15b3f83`, **11h42Z**) diz *"**Não abre, não mede e não relata nenhuma outra ilha.** Decisão do Raphael
  em 16/09/2026: foco é foco"*. Dois parágrafos colados, nove minutos de distância, afirmando o oposto.
- **Isto é o padrão da Amazon em escala de minutos** — e o commit do meio (`c3a7f3b`, 11h39Z) tinha criado um
  CHECK DE VIDA para as ilhas fora do foco que o commit das 11h42Z apagou inteiro, sem tocar no parágrafo acima.
- **O que eu fiz: CORRIGIDO** para a decisão mais nova, com as duas datas e os dois horários escritos na linha.

### M6. A seção 12 dizia que a nuvem não alcança os sites — de novo, dois dias depois de a mesma frase ser consertada na seção 10 — **CORRIGIDO**

- **Arquivo:** `ARQUIPELAGO.md` §12: *"A nuvem agendada não alcança os sites: **o proxy bloqueia** e o WebFetch
  exige aprovação humana por URL."*
- **A contradição:** §4 (*"A NUVEM ALCANÇA O SITE desde 10/09/2026"*), §10 (corrigida pelo Pente Fino em 14/09
  por esta mesma frase) e §20.2. **Remedido por mim agora:** as 9 URLs do sitemap da robometria responderam
  **200 da nuvem**, numa passada.
- **O que eu fiz: CORRIGIDO.** A metade verdadeira ficou e ganhou a causa certa (o WebFetch e o fato de a
  Sentinela não commitar); a metade falsa saiu, nomeada. **É o item 6 do padrão da auditoria anterior acontecendo
  outra vez: o defeito viaja em cópia, e quem conserta uma cópia não varre as outras.**

### M7. A decisão 5 do bloco 4 da robometria mandava toda ferramenta nova nascer com a frase proibida — **CORRIGIDO**

`ilhas/robometria/PROMPT.md`, bloco 4, decisão 5: *"o bloco **nasce mesmo sem link**, reservando o lugar com
'Link de loja em breve'"*, com *"a R2 nasce com isso, não com retrofit"* logo abaixo. A frase foi **proibida pela
§7 em 14/09** e retirada de cinco lugares desta ilha no mesmo dia (casca 1.6.0, R1 1.7.0, R2 1.5.0); medido no ar
hoje: **zero ocorrências nas 9 URLs**. **CORRIGIDO**: a decisão passa a mandar descer a escada da 25.1, com a
intenção original preservada e a data do que a derrubou.

### M8. Um despacho ALTA fechado há um dia continuava na lista dos ABERTOS — e ALTO é a única coisa que fura o foco — **CORRIGIDO**

`dados/despachos.md`: o despacho *"prioridade ALTA — o cache do hospedeiro pode estar segurando bloco de OUTRA
ilha"* traz, na primeira linha, *"**FECHADO em 15/09/2026, 11h36Z, com a AQUAMETRIA**"* — e estava sob `## ABERTOS`,
enquanto o arquivo tem `## FECHADOS` e move para lá todos os outros. Com a 1.2 valendo, um ALTA falso na lista dos
abertos é exatamente o que tira a Fundação da ilha em foco por nada. **CORRIGIDO**: bloco movido **sem uma palavra
alterada**, com a nota do porquê. O outro ALTA (rede das duas ilhas novas, para o Raphael) continua aberto e é
legítimo — e não fura o foco, porque nenhuma das duas está no ar.

### M9. A `BUSSOLA.md` continua mandando nascer duas ilhas por semana, e a pausa da Bússola não existe no repositório — **PRECISA DO RAPHAEL**

- **Arquivos:** `bussola/BUSSOLA.md` §5 × `ARQUIPELAGO.md` §1.2 e `foco.md`.
- **Os trechos:** BUSSOLA §5 — *"A Bússola roda **uma vez por semana** (segunda de manhã). O Arquipélago nasce
  **duas ilhas por semana** enquanto a meta for ~10 ilhas"* e *"Toda rodada garante que existam **dois dossiês
  prontos**"*. `foco.md` — *"o corte de crédito de 15/09 deixou a Fundação com ~20 execuções por semana para 5
  ilhas. Dividir por cinco não termina nenhuma."*
- **A contradição:** nascer ilha consome a Fundação (§11), e a 1.2 dá a Fundação inteira para uma ilha só. As duas
  regras não podem ser obedecidas ao mesmo tempo. E o disparo desta execução informa que **a Bússola está PAUSADA
  desde hoje** — `[stated]`, dito na conversa: **não existe uma linha sobre isso em arquivo nenhum do repositório**,
  nem em `BUSSOLA.md`, nem em `foco.md`, nem em `dados/despachos.md`. A própria `BUSSOLA.md` §6 diz que ela *"não
  escreve na memória como canal de decisão (o canal é o repositório, pelas Mãos — seção 12.2)"*.
- **O que eu fiz: PRECISA DO RAPHAEL.** Não escrevi a pausa: ela é decisão de política e eu só a conheço pelo
  disparo. **Texto proposto para o topo da `BUSSOLA.md`** (não inserido):
  > **PAUSADA desde 16/09/2026, por decisão do Raphael, enquanto `foco.md` na raiz nomear uma ilha.** A cadência
  > da seção 5 — uma rodada por semana, duas ilhas por semana, dois dossiês prontos — fica **suspensa**: a seção
  > 1.2 do `ARQUIPELAGO.md` dá todas as execuções da Fundação à ilha em foco, e ilha nova nasceria para ficar
  > parada. A fila e os dossiês existentes continuam válidos e não são remedidos. A Bússola volta no dia em que
  > `foco.md` disser `ilha: nenhuma`.

### M10. Duas ilhas estão com o cabeçalho de estado incompleto, e o molde nascia sem o campo — **CORRIGIDO no molde, registrado nas duas**

Passados os seis `ESTADO.md` pelo parser: os seis parseiam, **mas** `ilhas/clubedomosaico/ESTADO.md` e
`ilhas/ohmetria/ESTADO.md` não têm `ultima_ronda` **nem** `bloqueada_por`, obrigatórios pela §2 e usados pela §12
e pela §23.2 — e `ilhas/_modelo/ESTADO.md`, o molde de toda ilha futura, **também não tinha `ultima_ronda`**.
É o M6 da auditoria anterior de novo: o portão da §2 mede se o cabeçalho **parseia**, nunca se ele tem os campos.
**CORRIGIDO só o molde** (`ultima_ronda: null`, com a causa na linha). **Nas duas ilhas, registrado e não
corrigido:** `ultima_ronda` é campo da Sentinela e o valor teria de ser escolhido, e na ohmetria o `bloqueada_por`
é justamente a pergunta aberta (ela tem `rede: bloqueada em 2026-09-15`, que é dependência externa e portanto
candidata legítima a bloqueio — decidir isso a tiraria da rotação, e não é minha decisão). **Continua valendo a
proposta de 14/09, ainda não adotada:** o portão da §2 deveria cobrar as oito chaves, não só o parse.

---

## BAIXO — ruído

### B1. Três ilhas estão com reserva vencida de ontem — registrado, não corrigido

`ilhas/robometria/ESTADO.md` (`executando_desde: 2026-09-15T13:20Z`), `clubedomosaico` (13h22Z) e `ohmetria`
(13h19Z), as três com `ultima_execucao` **anterior** à própria reserva — ou seja, três execuções do dia 15 nunca
fizeram o passo 7 da seção 1 (limpar a reserva ao fechar). **Não limpei, pelo mesmo motivo da auditoria anterior:**
limpar reserva é passo da Fundação. **Não bloqueia nada** — a 1.1 resolve com o git (nenhum commit nessas pastas
nas últimas 40 h), e a 1.2 item 3 só manda parar se a reserva for de menos de 40 minutos.

### B2. A linha de base do item 2 da definição de pronta era de três dias atrás — **CORRIGIDO**

O item dizia *"das **28** entradas publicáveis, só **3** são atendidas pelas DUAS ferramentas"*. Rodando a própria
`cobertura-r1.py` hoje: **33 modelos publicáveis e 8 atendidos pelas duas** (os dois números mudaram com a leva do
Xiaomi S10, de 14/09 23h31Z). **CORRIGIDO por transcrição da medição, com os oito `id` nomeados; a meta de 15
ficou intacta**, porque é número absoluto e mudá-la seria decidir.

### B3. O item 5 da definição de pronta já está atendido — **CORRIGIDO**

*"TODA PÁGINA COM `<meta name="description">` E TAGS `og:` — defeito levantado na ronda de 11/09"*. O mesmo arquivo
registra esse defeito **cumprido em 11/09/2026** (item 1 daquela ronda). Medido no ar hoje: **9 de 9 URLs com
`meta description` e com cinco propriedades `og:`**. **CORRIGIDO** com a medição datada; não apaguei o item, para
o placar continuar tendo cinco linhas.

### B4. O despacho do Raphael de 14/09 diz "65 publicáveis"; hoje são 68 — registrado, não corrigido

35 peças + 33 modelos. O 65 (32 + 33) era exato às 15h17Z de 14/09 e envelheceu na leva das 23h31Z do mesmo dia.
**Não reescrevi:** é medição datada dentro de um despacho fechado, e o conserto certo é a linha nova — que este
relatório é.

### B5. A `fila.md` lista três ilhas nascidas e o arquipélago tem cinco — registrado

`bussola/fila.md`, tabela "Ilhas nascidas": robometria, aquametria e clubedomosaico. Faltam **ohmetria** e
**jornadafly**, que a **mesma tabela de ranking** marca com estado `ilha` e com *"nasce como ilha nº4"* / *"nº5"*,
e que têm pasta e `ESTADO.md` no repositório. Não corrigi: a `fila.md` é arquivo da Bússola e a coluna "Nota"
pediria um número que não é meu para escolher.

### B6. Contradições de contagem em ilha fora do foco — registradas, não corrigidas

Achadas na varredura e **sem nenhuma decisão em cima delas**, por isso BAIXO e por isso não gastei correção numa
ilha que hoje não recebe bloco: `aquametria/ARVORE.md` diz "37 registros" numa linha e "14 dos 36 registros" em
outra (já registrado em 14/09, segue aberto); `aquametria/PROMPT.md` tira C2/C7/C8 da fila enquanto o `ARVORE.md`
põe a C7 como item 1 da ordem das levas; `clubedomosaico/ARVORE.md` diz "11 URLs publicadas" e a tabela do mesmo
arquivo lista 14 linhas; `aquametria/PROMPT.md` chama de "duas regras independentes" uma trava cuja segunda metade
está declarada **SUSPENSA** no mesmo arquivo.

---

## Segredo em lugar errado — registro, nunca conserto

**O token do Sync continua em texto puro em três `PROMPT.md`**, que é o arquivo que toda execução abre. Tipo:
**token de autenticação do endpoint de Sync, embutido em query string**. *(O valor não está transcrito aqui nem no
commit.)*

| arquivo | linha | tipo |
|---|---|---|
| `ilhas/robometria/PROMPT.md` | 21 | token do Sync em query string |
| `ilhas/aquametria/PROMPT.md` | 21 | token do Sync em query string |
| `ilhas/clubedomosaico/PROMPT.md` | 41 | token do Sync em query string |
| `ilhas/clubedomosaico/PROMPT.md` | 43 | **o mesmo token**, repetido como `token=` na rota de cópia das peças (§24) |
| `ilhas/aquametria/REGISTRO.md` | 12 linhas | o endpoint completo, em histórico append-only |

*(Os números de linha são os do `main` DEPOIS deste commit: o aviso de foco que inseri empurrou as linhas da
aquametria e da clubedomosaico sete para baixo. Em 14/09 elas eram 14, 34 e 36.)*
**Aberto há 2 dias**, desde o G4 da rodada de 14/09. O conserto continua tendo duas metades e as duas são dele:
gerar token novo em cada ilha e passar a lê-lo de variável de ambiente, como `ferramentas/ga4.py` já faz.

**Também registrado, e não é credencial:** o e-mail pessoal da artesã segue em arquivo versionado
(`ilhas/clubedomosaico/PROMPT.md`, 6 linhas, e mais 8 arquivos da mesma ilha). É a mesma pendência de 14/09,
**aberta há 2 dias**, e é dado de uma pessoa de verdade — decisão dele, não minha.

---

## Pendências do Pente Fino anterior (14/09/2026)

| # | o que é | estado hoje | há quanto tempo |
|---|---|---|---|
| **G1** | §7 mandava "link de loja em breve" e a 25.2 proibia | **FECHADO** — a §7 foi reescrita e hoje diz *"a frase está proibida"* e *"onde esta seção e a 25 divergirem, manda a 25"*. As duas últimas cópias vivas da ordem velha eu corrigi hoje (M7 e a linha do `aquametria/ESTADO.md`) | — |
| **G2** | o piso da 25.2 não existe em ilha nenhuma; a 25.6 diz que é automático | **ABERTO** — medido hoje na robometria: 68 de 68 sem `url_busca`. A §25.6 continua dizendo *"Automático, sem humano, hoje … Responde a clique de script"* e os 68 `motivo_sem_url_busca` continuam dizendo que exige a sessão logada. **É o mesmo desacordo, com número novo** | **2 dias** |
| **G4** | token do Sync em texto puro em três ilhas | **ABERTO** (acima) | **2 dias** |
| **B3** | o `PAINEL.md` está com um dia e uma régua de atraso | **PIOR** — continua datado de **14/09 14h32Z**, cita *"`bussola/dossies/` continua vazia"* (há dois dossiês) e *"energia solar off-grid (4,20), nobreak (4,19)"*, índices que não existem em régua nenhuma em uso. Lista 3 ilhas de 5 e 4 despachos abertos que já foram cumpridos. **Não corrigi de propósito: a §23.1 diz "ninguém mais escreve nesse arquivo"** — e agora há um agravante, porque pela 1.2 a ronda diária só olha a robometria, então **ninguém tem mandato para atualizar as outras linhas do painel** | **2 dias** |
| — | logo do Clube do Mosaico: 52 px no código e no `VOZ.md`, 64 px no `DESIGN.md` | **ABERTO**, idêntico | **2 dias** |
| — | `executando_desde` preenchido depois do bloco fechar (aquametria) | **FECHADO** na aquametria; **reapareceu em três outras ilhas** (B1) | — |

---

## O PADRÃO

1. **A distância entre as duas pontas encolheu de novo, e agora se mede em MINUTOS.** Em 14/09 o recorde era
   "mesmo commit". Hoje é **nove minutos**: o parágrafo do custo da 1.2 (11h33Z) e o parágrafo seguinte (11h42Z)
   dizem o contrário um do outro, no mesmo arquivo, colados.
2. **Quem escreve a regra nova quase nunca varre quem ela contradiz.** A 1.2 nasceu declarando, no próprio texto,
   que vale "para o arquipélago inteiro" — e não tocou no mapa de leitura que a esconde das Sentinelas (M3), nem
   na 18.1 (M1), nem na 12 (M4), nem em quatro `PROMPT.md` de ilha (M2), nem na `BUSSOLA.md` (M9). **Seis lugares,
   todos alcançáveis por um `git grep` de duas palavras.**
3. **O defeito viaja em cópia, e consertar uma cópia não é consertar o fato.** "A nuvem não alcança os sites" foi
   corrigida na §10 em 14/09 e continuou de pé na §12 até hoje (M6). É o item 6 do padrão anterior, repetido.
4. **Lista nova nasce descrevendo o mundo de três dias atrás.** Dos cinco itens da DEFINIÇÃO DE PRONTA, **um já
   estava cumprido** (B3), **outro trazia números de 13/09** (B2), **um exige o que o contrato proíbe** (G2) e
   **dois são do Raphael** (G3). Nenhum dos cinco foi medido no dia em que foi escrito — e todos eram mensuráveis
   com ferramentas que a própria ilha já tem.
5. **Definição de pronta é a peça mais perigosa deste repositório**, porque é a única que manda sobre a fila e
   carrega prazo. Ela merece o portão mais duro, não o mais frouxo.
6. **A ordem velha é executada; a prosa velha só confunde.** Todas as correções de hoje que eu classificaria como
   urgentes são frases no imperativo: "entregue quantos blocos couberem", "comece por eles hoje", "reservando o
   lugar com 'Link de loja em breve'", "a ilha de `ultima_ronda` mais antiga".

**A regra de processo que evitaria a próxima.** A proposta de 14/09 (10.x — toda regra nova paga o pedágio da
busca) continua **não inserida** e teria pego cinco dos dez achados MÉDIO de hoje. Em vez de repeti-la, proponho a
metade que falta nela e que hoje custou caro — **também PROPOSTA, NÃO INSERIDA**, porque é regra nova de política:

> ### 10.y CRITÉRIO DE PRONTO NASCE MEDIDO, E DIZ DE QUEM É CADA ITEM
>
> Quem escreve uma lista de "pronto quando" — definição de pronta, despacho com critério, portão de bloco — faz
> duas coisas **antes de fechar o commit**, e a lista não vale sem elas:
>
> 1. **Mede cada item no dia em que o escreve**, com a ferramenta que já existe, e escreve o número ao lado.
>    Item cuja medição não couber na execução nasce com "não verificado", nunca com um número de memória. Critério
>    escrito sem medir é a versão com prazo do "número de tela digitado": ele parece conferido, e a primeira
>    execução que o ler vai gastar bloco atrás de coisa já feita — ou atrás de coisa impossível.
> 2. **Marca cada item com quem consegue fechá-lo:** `[FUNDAÇÃO]` ou `[RAPHAEL]`. Item que depende de sessão
>    logada, de navegador, de painel de terceiro ou de credencial que o ambiente não tem é **dele**, e dizer isso
>    não é desculpa — é a diferença entre um prazo que a fábrica pode cumprir e um prazo que ela não pode.
>    **Prazo com item de outra pessoa dentro não é meta: é uma dívida escondida com data.**
