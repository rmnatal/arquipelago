# AUDITORIA PENTE FINO — 14/09/2026

Rodada 3. As rodadas 1 e 2 falharam por falta de repositório e entregaram vazio; esta leu o `main` real
(`8a58a63`, Bússola rodada 005, 14/09 14h10Z) e auditou dele.

## O que foi lido

**26 documentos de lei, inteiros:** `ARQUIPELAGO.md` (795 linhas), `README.md`, `bussola/BUSSOLA.md`,
`bussola/fila.md`, `bussola/despacho-viagem.md`, `bussola/rodadas/005.md`, `dados/PAINEL.md`,
`dados/consertos.md`, os 4 `PROMPT.md` (três ilhas + `_modelo`), os 3 `VOZ.md`, os 3 `DESIGN.md`,
os 4 arquivos dos dois dossiês (`som-automotivo/` e `viagem-experiencia-icone/`, DOSSIE + VOZ).

**Os 3 `ESTADO.md` e os 3 `ARVORE.md`, inteiros:** cabeçalho YAML passado por `yaml.safe_load` (os três
parseiam) e conferido campo a campo contra a seção 2, e o corpo lido linha a linha numa segunda varredura —
519 + 511 + 377 linhas de `ESTADO.md` e 135 + 119 + 171 de `ARVORE.md`. Os `ARVORE.md` não estavam na lista
de leitura da rotina e **deviam estar**: sozinhos deram 9 achados, e são lei de ilha como o `DESIGN.md`.

**24 arquivos `ilhas/*/dados/*.json`** varridos por estrutura, e **10 bancos de produto medidos item a item**
(133 registros) para os campos que a seção 25 exige. **Os 296 arquivos versionados** varridos por padrão de
segredo. `git log --since="7 days ago"` usado para começar pelo que mudou na semana.

**Achados: 30 no total** — 14 na primeira varredura (4 GRAVE · 7 MÉDIO · 3 BAIXO) e **16 na segunda**, que leu
o corpo inteiro dos `ESTADO.md` e os três `ARVORE.md`. **16 corrigidos**, **1 resolvido pela própria Bússola
durante a auditoria** (M7) e **13 registrados** — os quatro GRAVE, a metade de G3 que é o dossiê de viagem, e
os sete da segunda varredura em que corrigir seria decidir. Um único item ficou com **"não verificado"**, e
está nomeado como tal.

> **Nota de ordem, e ela é achado por si só:** este Pente Fino deveria rodar **antes** da Bússola. Hoje não
> rodou: a rodada 005 fechou às 14h10Z e uma segunda execução dela entrou às **14h22Z**, no meio desta
> varredura. Duas consequências reais estão registradas em M7 e G3 — uma correção duplicada que tive de
> retirar, e um dossiê que ficou se contradizendo em cinco lugares por uma hora. A régua da semana seguinte
> continua correndo o risco que a rodada 004 pagou.

---

## GRAVE — decisão foi ou pode ser tomada com base errada

### G1. A seção 7 manda publicar "link de loja em breve"; a 25.2 proíbe essa frase com todas as letras — e as três ilhas estão no ar obedecendo à perdedora

- **Arquivo:** `ARQUIPELAGO.md`, seção 7 (regra da PROCEDÊNCIA, item 3) × seção 25.2.
- **Os dois trechos:** §7 — *"ferramenta que recomenda peça ou produto não vai ao ar sem o bloco de afiliado
  junto, mesmo com `afiliado.url` ainda vazio: a página reserva o lugar, mostra **"link de loja em breve"** e a
  ilha reporta quantos itens esperam link"*. §25.2 — *"a busca sobe e vira o botão — sem esperar decisão humana,
  **sem página ficar com "link de loja em breve"**"*, e antes disso: *"Todo item ganha `url_busca` ANTES de
  qualquer outra coisa. Item sem `url_busca` é defeito da 19.1, sempre, em qualquer degrau."*
- **A contradição:** as duas regras não podem ser obedecidas ao mesmo tempo. A §7 é a cicatriz de 10/09; a §25.2
  é decisão textual do Raphael de 13/09 (*"deve ser 100% automático sem eu tocar"*) e diz de si mesma que
  "manda na seção inteira". **As duas foram escritas no mesmo commit (`395a0e8`, 13/09)** — ou seja, quem
  escreveu a 25 tinha a 7 na mesa e não a releu. É o padrão da Amazon, de novo, três dias depois.
- **A evidência de que não é teórico, medida agora:**
  - `ilhas/robometria/PROMPT.md`: *"a ilha está no ar com quatro páginas de conteúdo e **nenhum link de loja em
    nenhum cartão** — todo cartão diz 'Link de loja em breve' … Ilha viva sem porta de compra."*
  - A frase está **em código no ar**: `robometria-r1.php`, `robometria-r2.php`, `robometria-a1.php`,
    `robometria-a2.php`, `robometria-casca.php` (duas vezes, uma delas numa seção pública inteira intitulada
    *"O que quer dizer 'link de loja em breve'"*), `aquametria-calculadora-vazao.php` (PHP e JS).
  - Está **cobrada por portão**: `teste-r2.php` linha 626 e `teste-a2.php` linha 407 **reprovam** se a frase
    sumir. Hoje, cumprir a 25.2 faz a bancada da robometria ficar vermelha.
  - Está **na lei das ilhas**: `ilhas/robometria/DESIGN.md` linha 34 e `ilhas/aquametria/DESIGN.md` linha 33.
  - E as três filas de bloco ainda mandam o contrário da 25.2: `aquametria/PROMPT.md` T3(e) — *"Produto novo
    entra **sem** `afiliado.url`; quem gera o link é a Sentinela estratégica"*; `robometria/PROMPT.md` 3c —
    *"Produto novo entra com `afiliado.url` presente e vazio"*; `clubedomosaico/PROMPT.md` bloco 3 —
    *"`afiliado.programa`/`afiliado.url` vazios **até a Sentinela preencher**"*. Nenhuma das três menciona
    `url_busca`, que a 25.2 exige **antes de qualquer outra coisa**.
- **O que eu fiz:** **PRECISA DO RAPHAEL.** Não corrigi. As duas pontas têm a mesma data, e há uma terceira
  leitura defensável (a 25.2 tornaria o galho da §7 inalcançável em vez de contraditório). Decidir aqui muda o
  que três ilhas vivas publicam e derruba dois portões verdes — é bloco, não conserto de coerência.
- **O texto proposto para a §7, item 3, se ele decidir pela 25.2** (não inserido):
  > (3) **ferramenta que recomenda peça ou produto não vai ao ar sem o bloco de afiliado junto.** O bloco nunca
  > nasce vazio: pela 25.2 todo item tem `url_busca`, e é ela que vira o botão enquanto não houver ficha viva.
  > "Link de loja em breve" **deixou de ser resposta** em 13/09/2026 — página sem porta de compra é defeito, não
  > espera. A ilha reporta em todo bloco quantos itens têm ficha e quantos estão no piso da busca.

### G2. O piso da 25.2 não existe em nenhuma ilha, e a própria 25.6 diz que ele é automático

- **Arquivos:** `ARQUIPELAGO.md` §25.2 e §25.6 × os 10 bancos de produto.
- **A regra:** §25.2 — "Item sem `url_busca` é defeito da 19.1, sempre". §25.6 — "**Automático, sem humano,
  hoje:** gerar link de afiliado da Shopee (produto, **busca**, loja ou categoria), com Sub_id … **Responde a
  clique de script**."
- **A medição (contada, não presumida):** itens sem `afiliado.url_busca` —
  | banco | itens | sem `url_busca` | sem `url_produto` | sem `degrau` |
  |---|---|---|---|---|
  | aquametria/produtos-aquecedor | 27 | 27 | 27 | 27 |
  | aquametria/produtos-filtro | 19 | 19 | 19 | 19 |
  | aquametria/produtos-iluminacao | 26 | 26 | 26 | 26 |
  | aquametria/produtos-midia | 6 | 6 | 6 | 6 |
  | clubedomosaico/materiais-colas | 7 | 2 | 2 | 2 |
  | clubedomosaico/materiais-rejuntes | 5 | 0 | 0 | 0 |
  | clubedomosaico/materiais-pastilhas | 13 | 13 | 13 | 13 |
  | robometria/pecas | 35 | 35 | 35 | 35 |
  | **total** | **138** | **128** | **128** | **128** |
- **A contradição:** o próprio banco da aquametria carrega, em `motivo_sem_url_busca`, a medição que derruba a
  25.6: o gerador da Shopee responde 200 e serve casca de JavaScript **sem sessão logada**, medido desta nuvem
  em 13/09, duas passadas. Os três `ESTADO.md` de hoje dizem o mesmo, cada um por sua conta: *"os 32 `url_busca`
  dependem de UMA sessão do painel da Shopee"* (robometria), *"os 15 `url_busca` dependem da sessão da Shopee"*
  (clubedomosaico), *"a escada de compra na tela, no minuto em que houver `url_busca`"* (aquametria).
- **Por que é GRAVE e não MÉDIO:** a 25.2 foi escrita **contra** a espera pelo Raphael ("Nada, nunca, fica na
  fila esperando o Raphael"), e hoje 128 de 138 itens estão exatamente nessa fila. A lei diz que o piso está
  de pé; a medição diz que ele nunca foi levantado. Toda a arquitetura de monetização do Arquipélago está
  escrita em cima de um automatismo que não existe.
- **O que eu fiz:** **PRECISA DO RAPHAEL.** Envolve sessão de conta dele e desempata o G1. Ou a 25.6 perde a
  linha "automático, sem humano, hoje" para a busca, ou uma sessão da Shopee destrava os 128 de uma vez.

### G3. O dossiê do som automotivo — o que o Raphael assina — carregava a régua da Amazon em cinco lugares — **CORRIGIDO, e o padrão aconteceu AO VIVO durante esta auditoria**

- **Arquivo:** `bussola/dossies/som-automotivo/DOSSIE.md`.
- **O que eu encontrei ao varrer, às ~14h15Z:** o dossiê inteiro sobre a âncora da Amazon — *"M **2,59**
  (R$ 16/venda, ticket R$ 202) … Retorno 3,89 · **Índice 4,23**"*. R$ 16 sobre R$ 202 é ~7,9%, **a taxa da
  Amazon**, que a seção 7 do contrato proíbe em todas as ilhas e que a rodada 005 declarou como o defeito
  central da régua.
- **O que aconteceu enquanto eu escrevia:** às **14h22Z** entrou o commit `09cd6c6` ("Bússola 005 — dossiês
  atualizados"). Ele **corrigiu o cabeçalho** do dossiê para índice 4,00 e **acrescentou uma seção 4 nova**
  explicando a queda de 4,23 para 4,00 com o número certo (R$ 202 × 3% = R$ 6,06 → M 1,65). **E não releu o
  resto do arquivo.** Um minuto antes do meu push, o mesmo documento passou a dizer as duas coisas:
  | onde | o que dizia |
  |---|---|
  | linha 3 (cabeçalho, novo) | índice **4,00** |
  | seção 4 (nova) | M **1,65** · R$ 6,06 por venda |
  | item 9 | "M = **2,59** … o índice **4,23** já é líquido disso" |
  | bloco **Notas** (a linha do scorecard) | "M **2,59** (R$ 16/venda) → Retorno 3,89 · **Índice 4,23**" |
  | seção de cesta | "O M de **2,59** é o número sem favor" |
  | "O que o Raphael precisa saber antes de dizer sim", item 2 | "R$ 202 típico, M **2,59**" |
  - **E o mesmo com o domínio:** a seção 1 (nova) traz *"O DOMÍNIO ESTÁ LIVRE, confirmado na fonte"* com o
    JSON literal do `registro.br` (`status: 0`); as linhas 164-166 e o item 1 do bloco de aprovação continuavam
    dizendo *"o domínio **não foi confirmado** … confirmar `status: 0` **antes de pagar**"*.
- **Por que é GRAVE:** `BUSSOLA.md` §5 — *"Dossiê é o que o Raphael aprova com um 'sim'; sem dossiê não há
  decisão."* O bloco que ele lê antes de dizer sim chama-se literalmente **"O que o Raphael precisa saber
  antes de dizer sim"**, e era exatamente ali que estavam o índice inflado em 5,7% e uma ordem para não pagar
  um domínio que já foi confirmado livre.
- **O que eu fiz: CORRIGIDO**, e agora era inequívoco — depois do `09cd6c6` os números certos passaram a estar
  **escritos no próprio arquivo**, então não houve recálculo nenhum: as cinco pontas velhas foram alinhadas à
  seção 1 e à seção 4 do mesmo dossiê, com a frase antiga nomeada em cada lugar. Conferi a aritmética por fora
  antes de copiar (Facilidade 4,64 · Retorno 3,51 · Índice 4,00, que é o que a `fila.md` também traz).
- **E ACONTECEU UMA TERCEIRA VEZ, com o dossiê de viagem, meia hora depois.** Quando varri, ele abria com
  *"índice não calculado — ver o portão aberto abaixo"*; registrei como PRECISA DO RAPHAEL porque os números
  certos não estavam no arquivo. Às **14h27Z** entrou o commit `e1cd745` ("JornadaFly: portão de monetização
  fechado, índice 3,92"), que corrigiu o cabeçalho para **índice 3,92** e escreveu uma seção nova de
  monetização com M 3,77 — **e deixou o bloco "Notas medidas" dizendo `D alta, não quantificada · A não
  verificado · M não calculável → índice não calculado`.** O mesmo movimento do dossiê do som automotivo,
  uma hora antes, no dossiê irmão.
  - **O que eu fiz: CORRIGIDO**, pelo mesmo motivo de antes — depois do `e1cd745` os números passaram a estar
    escritos no próprio arquivo (cabeçalho, tabela de cenários e a linha "ÍNDICE: 3,92"), então foi
    transcrição, não recálculo. Conferi a aritmética por fora: S 3,10 · Facilidade 3,86 · Retorno 3,98 ·
    Índice **3,921**. Bate com a `fila.md`.
  - **O que NÃO toquei, e é honestidade da própria Bússola:** a tabela de programas da seção (c) continua com
    "não verificado na fonte" em dez linhas, e isso está **certo** — a seção nova declara explicitamente que
    *"a lista de programas da seção (c) continua válida e é completada aqui pelos percentuais"*. Registro
    datado que diz o que substitui não é contradição; é o hábito que falta em todo o resto.

### G4. O token do Sync está em texto puro no `PROMPT.md` das TRÊS ilhas, não só no Clube do Mosaico

- **Arquivos e linhas** (tipo: token de autenticação do Sync em query string; **o valor não é transcrito aqui,
  nem no commit**):
  - `ilhas/aquametria/PROMPT.md` linha 14
  - `ilhas/robometria/PROMPT.md` linha 21
  - `ilhas/clubedomosaico/PROMPT.md` linha 34 — e **linha 36**, onde o mesmo token aparece uma segunda vez
    como parâmetro `token=` do endpoint de peças da seção 24
  - `ilhas/aquametria/REGISTRO.md`: 12 linhas com o endpoint completo (histórico append-only)
- **Por que importa:** a dívida registrada no meu próprio prompt nomeia só o Clube do Mosaico. **São três
  ilhas.** O `ESTADO.md` de cada uma diz "Nunca guarde credencial aqui" e a seção 2 do contrato repete — a
  regra existe, só não alcança o `PROMPT.md`, que é o arquivo que toda execução abre. E a seção 25.6 já
  decidiu onde credencial mora: *"variáveis de ambiente da rotina … **nunca** em arquivo do repositório"*.
- **O que eu fiz:** **PRECISA DO RAPHAEL.** Registrado, não consertado — girar token é operação em conta e no
  Code Snippets de três sites, e o Pente Fino não toca em credencial. O conserto tem duas metades: gerar token
  novo em cada ilha e passar a lê-lo de variável de ambiente, como `ferramentas/ga4.py` já faz.

---

## MÉDIO — regra inconsistente, sem decisão contaminada

### M1. A seção 10 dizia "a nuvem não alcança os sites; para checar, WebFetch, nunca curl" — **CORRIGIDO**

- **Arquivo:** `ARQUIPELAGO.md` seção 10, primeira linha.
- **A contradição:** a seção 4 declara, com data, *"**A NUVEM ALCANÇA O SITE desde 10/09/2026** — a Fundação
  aciona o Sync ela mesma … roda `curl -s`"*, e a 20.2 manda `curl` na conferência de rede. As três ilhas
  medem com `curl` todo dia; o `ESTADO.md` de cada uma de hoje registra "rede pela 20.2 … home em 200".
- **Por que é da seção 10 e não da 4:** a 10 é "regras que valem sempre" e está no cabeçalho de leitura
  obrigatória de **todo** papel (mapa da seção 0). Era a linha mais lida do contrato dizendo o contrário do
  que a fábrica faz.
- **O que eu fiz: CORRIGIDO.** A linha passa a dizer que o desenho é PULL, que a nuvem alcança desde
  10/09/2026, e aponta para a 4 e a 20.2. O papel do WebFetch (aprovação humana por URL, inviável em rotina,
  seção 12) ficou escrito.

### M2. O `PROMPT.md` da robometria mandava dar o bloco 3c inteiro por bloqueado testando o endereço errado — **CORRIGIDO**

- **Arquivo:** `ilhas/robometria/PROMPT.md`, bloco 3c.
- **O trecho:** *"TODA a coleta acima depende de rede que hoje NÃO existe … `mi.com.br`, `xiaomi.com.br` …
  **Antes de escolher um alvo do 3c, teste a rede com `curl`. Se ela continuar fechada, o 3c inteiro está
  bloqueado**."*
- **A contradição:** este é **o texto que a seção 4 do contrato cita como a cicatriz**, com nome e data —
  *"O ENDEREÇO QUE VOCÊ TESTA SAI DA PROSA; O ENDEREÇO QUE VALE ESTÁ NO BANCO (Robometria, 13/09/2026)"* —
  e o mesmo arquivo já registra a correção 200 linhas abaixo: *"a causa dos três dias parados **não era a
  rede**: o `PROMPT.md` e o `ESTADO.md` mandavam testar `mi.com.br` … e o banco sempre citou `www.mi.com/br`"*.
  A lição subiu para o contrato e a instrução que a causou continuou de pé, mandando o contrário.
- **O que eu fiz: CORRIGIDO.** A medição de 11/09 fica como registro; a instrução passa a mandar copiar o
  endereço do campo `url` do registro que se quer melhorar, testar **os dois canais** (egresso direto e busca,
  que a própria ilha já separou em 12/09) e só dar por bloqueado o alvo, nunca o 3c inteiro.

### M3. O `PROMPT.md` da robometria dizia, na mesma página, que a nuvem alcança e que não alcança — **CORRIGIDO**

- **Arquivo:** `ilhas/robometria/PROMPT.md`. Linha 25: *"Quem aciona o Sync é a própria Fundação, por `curl`
  … a nuvem alcança o site desde 10/09/2026"*. Bloco 3b, linha 153: *"(a nuvem não alcança robometria.com.br)"*
  — com o próprio bloco 3b registrando, sete linhas acima, *"Sync acionado pela nuvem: `/status` responde
  revisão 7"*.
- **O que eu fiz: CORRIGIDO.** O parêntese falso saiu; a frase passa a dizer o que é verdade e útil — que o
  `teste-casca.php` é a verificação da seção 8 que roda **sem tocar o site**.

### M4. O `PROMPT.md` do Clube do Mosaico mandava cabeçalho preto — **CORRIGIDO**

- **Arquivo:** `ilhas/clubedomosaico/PROMPT.md`, bloco 3b: *"Cabeçalho e rodapé pretos, miolo branco"*.
- **A contradição:** três documentos dizem o contrário, e um deles é o mesmo arquivo. Linha 14: *"O cabeçalho
  é CLARO"*; linha 20: *"**o cabeçalho é claro — o logo NUNCA vai sobre preto, porque o wordmark vinho
  some**"*; `DESIGN.md`: *"O preto nunca vai no topo"*; `VOZ.md`: *"Header claro (papel #FFFFFF)"*.
- **A evidência de que custou:** o próprio `DESIGN.md` registra *"foi isso que sumiu com o logo em 11/09"*.
- **O que eu fiz: CORRIGIDO.** Cabeçalho claro `#FFFFFF`, rodapé escuro, com a causa escrita.

### M5. A etiqueta do Mercado Livre do Clube do Mosaico estava no formato que o painel recusa — **CORRIGIDO**

- **Arquivo:** `ilhas/clubedomosaico/PROMPT.md`, "Específico desta ilha": *"Mercado Livre (etiqueta
  `clubedomosaico-<código>`)"*.
- **A contradição:** `ARQUIPELAGO.md` seção 7, **medido no painel em 13/09/2026, não suposto** — a etiqueta
  *"só aceita letras minúsculas e números, **sem hífen**, sem espaço, sem maiúscula"*, e a própria seção manda:
  *"Onde texto antigo do contrato disser `aquametria-C3` ou `clubedomosaico-F1`, leia a forma sem hífen."*
  O dossiê do som automotivo já nasceu certo (`ohmetriaf1`); só a ilha viva ficou para trás.
- **O que eu fiz: CORRIGIDO** para `clubedomosaicof1` / `clubedomosaicof2`, citando a seção 7.

### M6. Os campos `ultima_ronda` e `bloqueada_por` caíram do cabeçalho da aquametria HOJE — **CORRIGIDO**

- **Arquivo:** `ilhas/aquametria/ESTADO.md`, cabeçalho YAML.
- **A contradição:** a seção 2 declara os dois obrigatórios; a seção 12 usa `ultima_ronda` para distribuir a
  ronda por dívida; a 23.2 publica os dois no painel. Os dois **existiam** e sumiram no commit `9e9f7d0`
  (LEVA 5, 14/09) — conferido em `9e9f7d0^`. O YAML continuou parseando, que é exatamente por que ninguém viu:
  o portão da seção 2 mede se o cabeçalho **parseia**, não se ele tem os campos.
- **O que eu fiz: CORRIGIDO por restauração**, sem recalcular nada: `ultima_ronda: 2026-09-13T14:47Z` (o valor
  literal de `9e9f7d0^`, que bate com o `PAINEL.md` e com o despacho da Sentinela no `PROMPT.md`) e
  `bloqueada_por: null`. Os três `ESTADO.md` voltam a ter os oito campos e os três parseiam.
- **Fica proposto, não inserido** — o portão da seção 2 deveria cobrar as chaves, não só o parse:
  ```
  python3 -c "import io,yaml;d=yaml.safe_load(io.open('ilhas/<ilha>/ESTADO.md',encoding='utf-8').read().split('---')[1]);f=[k for k in ('ilha','estado','prioridade','ultima_execucao','executando_desde','bloco_atual','ultima_ronda','bloqueada_por') if k not in d];print('YAML ok' if not f else 'FALTAM: '+', '.join(f))"
  ```

### M7. A rodada 005 declarou 23 fazendas novas "entram na lista do `BUSSOLA.md` nesta rodada" e elas não estavam lá — **RESOLVIDO PELA PRÓPRIA BÚSSOLA, minha cópia retirada**

- **Arquivos:** `bussola/rodadas/005.md` seção 2.7 × `bussola/BUSSOLA.md` seção 3.
- **O trecho:** a 005 mediu que *"a lista nomeada de 12 fazendas pegou **4 ocorrências**"* em 12 consultas,
  enquanto 23 fazendas fora da lista *"dominaram duas SERPs comerciais inteiras"*, e conclui: *"**Se a régua só
  olha os 12 nomes antigos, ela dá S_com alto para SERP que está fechada.** Os nomes acima entram na lista do
  `BUSSOLA.md` nesta rodada."* Quando varri, o `BUSSOLA.md` continuava com as 12.
- **O que aconteceu:** eu transcrevi os 23 nomes; sete minutos depois o commit `09cd6c6` da própria Bússola
  fez a mesma coisa, num parágrafo próprio e **melhor que o meu** — ele acrescenta a régua de FORMA ("qualquer
  domínio cujo título siga o molde 'As N Melhores X de 2026' conta como fazenda, esteja nomeado aqui ou não;
  a lista é atalho de reconhecimento, nunca a definição"). **Retirei a minha cópia e mantive a da Bússola**,
  restaurando a linha original das 12. Conferido: `techminuto` aparece **uma vez** no arquivo.
- **Registro honesto:** este achado era real quando foi feito e deixou de ser durante a auditoria. Fica no
  relatório porque duas execuções corrigirem a mesma coisa em sete minutos é informação sobre o processo — a
  ordem "Pente Fino antes da Bússola" não foi respeitada nesta segunda-feira.

---

## BAIXO — ruído

### B1. A fila põe o 2º lugar acima de um índice maior

`bussola/fila.md`: JornadaFly em **2º com 3,92**, energia solar em **3º com 3,94**. Recomputei as duas contas
pela fórmula da seção 3 e os dois números estão certos (3,921 e 3,944) — o que não fecha é a ordem. A rodada
005 escreve a escolha com todas as letras (*"Isso o põe em 2º, praticamente empatado com a energia solar"*),
então não é descuido de digitação; o que falta é o critério de desempate estar escrito na fila, já que a
tabela se declara ordenada por índice. **PRECISA DO RAPHAEL** — mexe na ordem da fila, que não é minha.

### B2. O dossiê do som automotivo diz "40 candidatos" e lista 41

`bussola/dossies/som-automotivo/DOSSIE.md`, linhas 115-124. As cinco famílias somam 7+10+8+7+9 = **41**; o
título diz "Os 40 candidatos" e o resultado, "Sem DNS (**38 de 40**)" — com 2 ocupados seriam 39 de 41. A
seção 5(d) do `BUSSOLA.md` pede "30 a 40 candidatos". Nada decidiu nada em cima disso (o nome escolhido foi
confirmado livre no registro.br pela 005), e por isso é BAIXO. **PRECISA DO RAPHAEL** junto com G3, na
reemissão do dossiê.

### B3. O `PAINEL.md` está com um dia e uma régua de atraso

`dados/PAINEL.md` está datado de 13/09 14h47Z e diz *"`bussola/dossies/` está **vazia** e o topo da fila é
energia solar off-grid (**4,20**), seguido de nobreak (**4,19**)"*. Hoje há **dois dossiês**, o topo é som
automotivo (4,00) e os índices citados não existem em régua nenhuma em uso — são anteriores à rodada 004.
**Não corrigi, de propósito:** a seção 23.1 diz *"**Ninguém mais escreve nesse arquivo**"* além da ronda da
Sentinela. Fica para a próxima ronda diária. Vale a pena a Sentinela reparar que o painel cita número de
Bússola: enquanto ele copiar índice de fila, ele envelhece toda segunda de manhã.

---

## SEGUNDA VARREDURA — o corpo dos `ESTADO.md` e os três `ARVORE.md`

A primeira passada leu os `ESTADO.md` só pelo cabeçalho. Uma segunda varredura leu o **corpo inteiro** dos
três (519 + 511 + 377 linhas) e os três `ARVORE.md` (135 + 119 + 171), que não estavam na lista original e
são lei de ilha do mesmo jeito. **Mais 16 achados; 9 corrigidos, 7 registrados.** Todos conferidos por mim
na fonte antes de qualquer edição.

### Corrigidos nesta segunda passada

| # | onde | o que dizia | por que caiu |
|---|---|---|---|
| S1 | `aquametria/ESTADO.md`, "Stack e infra" | *"o container da nuvem **NÃO alcança o site** por HTTP — só GitHub"* | Mesma família de M1/M3. Falso desde 10/09, e contradito **pelo próprio cabeçalho deste arquivo, escrito hoje**: *"Rede pela 20.2 antes de trabalhar: home em 200 e `/status` na revisão 77, em UMA passada"*. Mantive o que continua verdadeiro: o egresso a **domínio de fabricante** segue fechado, que é outra coisa |
| S2 | `aquametria/ESTADO.md` | *"Produto sem link **não entra** no bloco de produto — a regra **V15** do validador executa isso"* | Duas coisas erradas numa frase. `dados/esquema-produtos.json` **já tinha reescrito essa mesma frase em 13/09** — *"isso era falso desde a V16 … o que falta a ele não é presença, é PISO (25.2)"* — e a cópia no ESTADO ficou de pé. E a régua citada é a errada: a V15 confere se o campo `afiliado` está bem formado; quem manda é a **V16**, uma linha abaixo no próprio arquivo |
| S3 | `aquametria/ARVORE.md` | *"o rodapé, que a linka **das 28 páginas** do site"* | A ilha tem **36** (`urls_publicadas`, e a própria árvore soma 36). Contado antes das levas 4 e 5 |
| S4 | `clubedomosaico/ESTADO.md` | *"Cabeçalho e rodapé **pretos** com miolo branco"* | M4 de novo, em outro arquivo. E a cicatriz está escrita **140 linhas abaixo, no mesmo arquivo**: *"o logo sumiu em 1.1.0 porque o **cabeçalho era preto** e o wordmark dentro do arquivo é vinho `#69030C`"* |
| S5 | `clubedomosaico/ESTADO.md` | *"a **linha 178** do `PROMPT.md` manda tratar queda em spam como bloqueio da ilha"* | A linha 178 trata de outro assunto; a regra do spam está na 205. **Número de linha envelhece a cada edição** — a referência passa a ser pela frase |
| S6 | `clubedomosaico/ARVORE.md` (3 lugares) | *"peça publicada pela artesã, que hoje são **zero**"*, *"porque hoje **não há peça**"*, *"hoje **não existe peça nenhuma** — a artesã ainda não publicou a primeira"* | **Existe uma desde hoje:** "Quadro flores do campo", `dados/pecas.json` com `total: 1`, e o `ESTADO.md` registra *"A ILHA TEM A PRIMEIRA PEÇA DE VERDADE"*. Corrigi a premissa e **deixei a decisão aberta**: a escolha entre as duas saídas de URL continua de quem tiver o número, e acrescentar a linha da peça à tabela é do próximo bloco, porque o portão da casca cobra que toda linha dela exista no código |
| S7 | `clubedomosaico/ARVORE.md`, tabela do Guia | "Colas **5 itens**" · "Pastilhas **0**" | Contados: **7** colas e **13** pastilhas. Tabela digitada, e vai envelhecer de novo — é o "número de tela nasce contado" da seção 8 aplicado a documento |
| S8 | `clubedomosaico/ARVORE.md` | *"As **cinco** categorias do vocabulário sem um único item (`pastilha`, `alicate`, …)"* | São **quatro**; o `ESTADO.md` já dizia *"caíram de 5 para 4"* |
| S9 | `clubedomosaico/ARVORE.md` | *"Fora da árvore ficam **só** a home, `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/`"* | A seção 3c do **mesmo arquivo** chama `/atelie/` de *"a segunda exceção"* e o põe fora da árvore pela camada `privada`. Cai o "só" |

### Registrados, não corrigidos

- **`executando_desde` da aquametria ficou preenchido depois do bloco fechar** — MÉDIO, **PRECISA DA
  FUNDAÇÃO**. O cabeçalho diz `executando_desde: 2026-09-14T14:03Z` **e** `ultima_execucao: 14:05Z`, o que a
  seção 1 passo 7 proíbe (ao terminar, limpe a reserva). O commit que fechou o bloco (`c088dde`, "LEVA 5 NO
  AR — revisão 80 aplicada", 14h15Z) **não tocou o cabeçalho**. **Não limpei de propósito:** limpar reserva é
  o passo 7 da Fundação, e se eu estiver errado sobre a execução ter terminado eu entrego ilha viva a uma
  segunda execução — exatamente o dano que a 1.1 existe para impedir. É uma linha para a próxima execução.
  *(Não verificado: se há execução realmente em curso.)*
- **`aquametria/ARVORE.md` atribui à 16.1 a permanência de `/metodologia/` na raiz** — BAIXO, **PRECISA DO
  RAPHAEL**. O trecho diz *"o 16.1 lista essa família por nome"*, e `/metodologia/` **não está** nessa lista
  (home, sobre, contato, divulgação, privacidade) — a 21.7 diz o oposto com todas as letras: *"o que a
  exceção NÃO cobre … qualquer outra página da raiz, `/metodologia/` **incluída**"*. A mesma lista troca
  `/contato/` por `/metodologia/` e ainda chama a privacidade de "a quinta". **A colocação pode estar certa**
  — a robometria resolveu o mesmo caso como **veredito da ilha**, não como lista da 16.1, e escreveu isso —;
  o que não fecha é a atribuição. Corrigir a atribuição é escolher qual regra licencia a página, e isso é
  decisão, não coerência.
- **Logo do Clube do Mosaico: 52 px no `ESTADO.md`, no `VOZ.md` e no código; 64 px no `DESIGN.md`** (e barra
  de 84 px contra ~96 px) — MÉDIO, **PRECISA DO RAPHAEL**. A contradição é inequívoca, **o lado a corrigir
  não é**: pela 22.6 o `DESIGN.md` é o dono dos tokens e a casca deveria renderizar dele, mas quem está
  sozinho é justamente ele. Ou o código sobe para 64/96, ou o `DESIGN.md` desce para 52/84 — e o próprio
  registro de 11/09 já anotou que "52 px é pequeno para ler" e que subir para ~64 px **não é decisão da
  Fundação**. É a mesma pergunta, ainda aberta.
- **`robometria/ESTADO.md`: "o tipo `reservatório` tem zero peças no banco inteiro"** — BAIXO. O banco tem
  **3**, e o `ARVORE.md` registra a terceira entrando em 13/09. É seção datada de 10/09 sem linha de
  correção. Não corrigi: seção datada é registro histórico, e o conserto certo é a linha de atualização que
  o `ARVORE.md` escreveu e o `ESTADO.md` não.
- **`robometria/ESTADO.md` ainda lista como pendência aberta *"uma fonte está no nível 2 e a escada diz que o
  nível 2 não existe … é bloco de dados para a Fundação"*** — BAIXO. O **mesmo arquivo**, com data posterior
  (11/09), já responde: *"A regra do nível 2, **decidida**: não é nível 2, é nível 3"*. Mesma família do
  anterior: falta a linha que fecha o item.
- **`aquametria/ARVORE.md`: "37 registros" numa linha e "14 dos 36 registros" noutra** — BAIXO. O arquivo tem
  37; o 36 é medição de 12/09. Não é erro, é **número sem data ao lado** — a 23.4 já decidiu como se escreve
  isso, e vale para documento também.
- **`aquametria/ARVORE.md`: "a Pauta entra na fila desta ilha antes de qualquer leva de malha nova"** —
  BAIXO. As levas 4 e 5 saíram hoje sem pauta, `pauta.md` não existe em ilha nenhuma, e pela 17.1 quem a
  escreve é uma rotina **no computador do Raphael** — a Fundação não pode produzi-la. O `PROMPT.md` põe a
  Pauta antes **dos guias**, não da malha. Lido ao pé da letra, este trecho congela a malha da ilha à espera
  de um arquivo que a nuvem não pode criar — é a família da 21 (regra boa lida ao pé da letra travando a
  ilha). Provavelmente quis dizer "leva de `/guias/`", e por isso é proposta, não conserto.

**Não houve achado em `robometria/ARVORE.md`** — as contagens fecham (4 + 14 = 18 URLs novas, 9 páginas) e o
"de 2 a 4 irmãs" bate com o 16.4(c). É o único dos seis limpo, e vale dizer por quê: é o que mais escreve
linha de correção datada em cima do próprio texto, em vez de deixar a frase velha de pé.

---

## Pendências do Pente Fino anterior

**Não há relatório de Pente Fino anterior no repositório.** As rodadas 1 e 2 não tinham o repositório
montado e entregaram vazio; este é o primeiro. Nada a herdar, nada a cobrar por semana pendurada.

---

## Dado da artesã em arquivo versionado — registro, não conserto

O e-mail pessoal da mãe do Raphael aparece em **9 arquivos versionados**: `ilhas/clubedomosaico/PROMPT.md`
(5 linhas), `ESTADO.md` (2), `REGISTRO.md` (2), `manifest.json` (1), `snippets/clubedomosaico-atelie.php`,
`snippets/clubedomosaico-leads.php`, `ferramentas/teste-atelie.php` (9), `ferramentas/teste-leads.php` (5),
`ferramentas/mutacoes-leads.py`, `ferramentas/render-para-teste.php`, e `dados/despachos.md`.

A seção 24.2 decidiu, para os leads, que *"nome e WhatsApp de pessoa não entram em arquivo versionado"* — e
o e-mail da artesã, que é a mesma classe de dado, entrou. Não é contradição de letra (a regra foi escrita
sobre `lead_peca`), e por isso não a promovi a defeito. **PRECISA DO RAPHAEL:** é dado de uma pessoa de
verdade, num repositório que o `ESTADO.md` da aquametria diz que "pode virar público", e a decisão é dele.
O caminho barato seria o e-mail virar option do site (`cdm_email_leads` já existe) e sair dos arquivos.

---

## O PADRÃO

1. **O defeito não está em decidir errado. Está em decidir certo num lugar e não reler o vizinho.** Seis dos
   doze achados são o mesmo movimento: alguém corrigiu um ponto, escreveu a data, e deixou de pé a frase ao
   lado que descreve o mundo anterior.
2. **A distância entre as duas pontas encolheu, e isso é o mais alarmante.** No caso Amazon foram semanas.
   Em G1, as duas regras contraditórias nasceram **no mesmo commit**. Em M6, o campo caiu do cabeçalho **hoje
   de manhã**. Em G3 o padrão aconteceu **durante esta auditoria**: às 14h22Z uma execução da Bússola corrigiu
   o cabeçalho de um dossiê e a seção nova, e deixou o bloco de notas, o item 9, a seção de cesta e o próprio
   bloco "o que o Raphael precisa saber antes de dizer sim" dizendo o contrário — quatro pontas velhas, um
   minuto antes do meu push. **E de novo às 14h27Z, no dossiê irmão**, com o mesmo formato: cabeçalho e seção
   nova certos, bloco de notas dizendo "índice não calculado". **Três vezes em quarenta minutos, sempre a
   mesma forma: o topo do documento é corrigido e o bloco de números lá embaixo não.** A fábrica está
   escrevendo lei mais rápido do que a relê, e uma auditoria semanal não alcança isso.
3. **Toda ponta velha que sobrou era uma FRASE OPERACIONAL — uma ordem, não uma explicação.** "Teste com
   curl", "cabeçalho preto", "etiqueta com hífen", "a nuvem não alcança". Prosa velha é inofensiva; **ordem
   velha é executada.**
4. **Quem escreve a lição quase nunca é quem apaga a causa.** A cicatriz sobe para o `ARQUIPELAGO.md` com
   nome e data, e o arquivo que a causou fica intacto (M2 é o caso puro: a seção 4 cita o texto, o texto
   continua lá).
5. **O portão que existe mede a forma, não o conteúdo** (M6: o YAML parseia sem os campos obrigatórios).
6. **A segunda varredura confirmou os cinco pontos e acrescentou um sexto: o defeito viaja em CÓPIA.** A
   mesma frase falsa mora em dois arquivos, alguém corrige um, e o outro continua servindo a versão velha —
   S2 é o caso puro (o `esquema-produtos.json` reescreveu a frase em 13/09 nomeando que era falsa; a cópia no
   `ESTADO.md` ficou intacta), e S4 e S1 são o mesmo movimento. **O contrato já proíbe isso para regra**
   ("regra nova se escreve AQUI, uma vez — nunca copiada para dentro dos prompts das ilhas") e não proíbe
   para **fato medido**, que é o que mais se copia.
7. **Quem escreve linha de correção datada em cima do próprio texto não acumula dívida.** O
   `robometria/ARVORE.md` é o único dos seis arquivos da segunda varredura sem nenhum achado, e é
   justamente o que mais faz isso. Não é sorte: é o hábito.

**A regra de processo que evitaria a próxima**, escrita para caber no `ARQUIPELAGO.md`. **Proposta, NÃO
inserida** — é regra nova de política e a decisão é do Raphael:

> ### 10.x TODA REGRA NOVA PAGA O PEDÁGIO DA BUSCA — quem escreve a lei varre quem a contradiz
>
> Quando uma execução escreve, muda ou data uma regra — no `ARQUIPELAGO.md`, no `BUSSOLA.md` ou num
> `PROMPT.md` —, ela faz, **no mesmo commit**, duas coisas e não fecha sem elas:
>
> 1. **Busca pela palavra que a regra proíbe ou substitui**, em todo o repositório, e não só no arquivo que
>    ela abriu: `git grep -n "<a frase antiga>"`. Frase que a regra nova torna falsa é corrigida agora ou
>    ganha uma linha nomeando onde ficou e por quê. Regra nova sem essa varredura não é regra: é uma segunda
>    opinião convivendo com a primeira.
> 2. **Nomeia a regra que ela substitui**, por seção e por data, dentro do próprio texto novo. Regra que não
>    diz o que ela derruba deixa a anterior de pé, e quem ler primeiro a antiga obedece à antiga.
>
> **A busca é pela ORDEM, não pela ideia.** Prosa velha custa uma leitura confusa; **instrução velha é
> executada por quem chegar depois** — foi assim que três dias de coleta da Robometria se perderam testando
> um domínio que o banco nunca citou. Por isso a varredura procura o imperativo: o comando, o hexadecimal, o
> formato de campo, o endereço, a frase que vai para a tela.
>
> **E há um lugar que a varredura visita SEMPRE, porque é onde o defeito caiu três vezes em quarenta minutos
> no dia em que esta regra foi escrita: o BLOCO DE NÚMEROS do próprio documento que você acabou de corrigir.**
> Nota, índice, contagem, tabela de resumo, "o que o leitor precisa saber" — é o trecho que ninguém relê
> porque parece derivado, e é justamente o que o leitor lê primeiro. Documento cujo cabeçalho e cujo bloco de
> notas discordam não está meio corrigido: está pior do que estava, porque agora tem uma versão certa dando
> crédito à errada.
