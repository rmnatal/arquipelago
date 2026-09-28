# AUDITORIA PENTE FINO — 28/09/2026

Rodada de segunda de manhã, **antes da Bússola**. Auditei do `main` real, `82c1ff7` (25/09/2026 10h37Z), por
`git fetch origin main && git checkout -B pente-fino origin/main`.

## O que foi lido

**42 documentos de lei, inteiros:** `ARQUIPELAGO.md` (1.012 linhas), `README.md`, `foco.md` e o relatório do
Pente Fino de 21/09; `bussola/BUSSOLA.md`, `bussola/fila.md`, `bussola/despacho-viagem.md`,
`bussola/rodadas/004.md` e `005.md`, `bussola/medicoes/volume-absoluto-2026-09-18.md` e os **4** arquivos dos
dois dossiês; `dados/PAINEL.md`, `dados/despachos.md`, `dados/consertos.md`; e os **25** arquivos de ilha — os
**6** `PROMPT.md` (cinco ilhas mais `_modelo`), os **6** `ESTADO.md`, os **5** `VOZ.md`, os **5** `DESIGN.md` e
os **3** `ARVORE.md`. Mais trechos do `MAOS-LOG.md` e dos relatórios de 14 e 16/09, por busca dirigida.

**Honestidade sobre quem leu o quê.** Li eu mesmo, inteiros, o contrato, os dois arquivos da Bússola, o painel,
os despachos, os consertos, o `PROMPT.md` e o `ESTADO.md` da **clubedomosaico** (a ilha em foco), o molde e o
relatório anterior. Os arquivos das quatro ilhas fora do foco, os dossiês e as rodadas foram lidos por duas
varreduras auxiliares, instruídas com regra dura de não inventar achado — **e nenhum achado delas entrou aqui
sem eu abrir o arquivo, reler o trecho na fonte e, onde cabia, datar a linha com `git blame`.** Descartei seis
achados delas depois de conferir: (i) a nota de 21/09 no `aquametria/PROMPT.md` que diz "a ilha está fora do
foco" é hoje **verdadeira** de novo, não contradição; (ii) o `T2 CONCLUÍDO × não conta como entregue` da
aquametria é dívida declarada com motivo escrito no próprio item; (iii) as duas medições de egresso da
robometria de 17/09 às 12h35Z e 13h20Z não listam os mesmos hosts, então não se contradizem — só a metade do
`mais.conteudo.wap.ind.br` se contradiz, e essa entrou (M6); (iv) os 14 × 12 itens `intestavel` da aquametria
o próprio arquivo corrige por baixo; (v) o símbolo do `ohmetria/PROMPT.md` contra o `DESIGN.md` está
declarado como resolvido no mesmo parágrafo; (vi) o item 2 da DEFINIÇÃO DE PRONTA da robometria tem motivo
escrito e dono nomeado.

**Medição, não leitura.** Os **6** cabeçalhos `ESTADO.md` passados por `yaml.safe_load` e conferidos chave a
chave contra a seção 2; os **62** arquivos `ilhas/*/dados/*.json` varridos campo a campo atrás de `url_busca`,
`url_produto`, `degrau` e `conferido_em`; os **9** validadores de banco das cinco ilhas **rodados**
(`validar-banco` × 4, `validar-produtos`, `validar-especies`, `validar-prospeccao`, `validar-pastilhas`,
`validar-derivados`); os valores de `sub_id_1` e `sub_id_2` **contados** nos bancos das três ilhas no ar; as
**17** linhas da `fila.md` recalculadas em Python contra as quatro fórmulas declaradas no cabeçalho dela; e
todas as referências a arquivo dentro do `ARQUIPELAGO.md` e da `BUSSOLA.md` conferidas contra a árvore real.
`git log --since="7 days ago" --name-only` e `git blame` para começar pelo que mudou e para datar cada ponta.

**Achados: 18** — **0 GRAVE** · 12 MÉDIO · 6 BAIXO. **12 correções aplicadas** em 7 arquivos; **6 registrados**
(2 deles PRECISA DO RAPHAEL). Mais **5 pendências herdadas**, a mais antiga aberta há **14 dias**.

> **A resposta curta, antes do detalhe:** nenhuma decisão desta semana foi tomada com base errada — **não há
> GRAVE**, e isso é o resultado saudável. O que há é um padrão só, repetido cinco vezes: a execução de 24/09
> corrigiu o aviso de foco do `PROMPT.md` da ilha que entrou em foco e **não releu o das outras quatro**.
> Resultado medido hoje: **cinco de cinco** `PROMPT.md` de ilha contradiziam o `foco.md` — a robometria ainda
> dizia "esta ilha é a única em foco, então recebe todas as execuções da Fundação", e a própria ilha em foco
> abria o despacho aberto dela dizendo "despacho NORMAL de ilha fora do foco espera" (M1). Os cinco foram
> corrigidos com ponteiro datado, sem apagar uma linha de história.

---

## GRAVE — decisão foi tomada com base errada

**Nenhum.** Varri as sete classes e não achei, nesta semana, uma decisão tomada sobre uma ponta velha. Os dois
candidatos que cheguei a abrir e descartei estão nomeados: o aviso de foco (M1) **não** desviou execução — as
passadas de 25/09 trabalharam o despacho do Raphael de 24/09, que é o certo pela 18.1 —, e o `sub_id_2` da
robometria (M2c) não sustentou decisão nenhuma, só uma afirmação que ninguém mediu.

---

## MÉDIO — regra inconsistente, sem decisão contaminada

### M1. Cinco de cinco `PROMPT.md` de ilha contradiziam o `foco.md` — **CORRIGIDO nos cinco**

`foco.md` nomeia a **clubedomosaico desde 24/09/2026**, e ele mesmo registra o histórico: aquametria de 21/09 a
24/09, robometria de 16/09 a 21/09. Contra isso, medido arquivo por arquivo com `git blame`:

| arquivo | o que dizia | data da linha |
|---|---|---|
| `ilhas/robometria/PROMPT.md` | *"Esta ilha é a única em foco (`foco.md`), então recebe **todas** as execuções da Fundação e o teto semanal inteiro de geração de link"* | 16/09 |
| `ilhas/aquametria/PROMPT.md` | *"O FOCO VOLTOU PARA CÁ EM 21/09/2026"*, como cabeçalho da FILA DE BLOCOS | 22/09 |
| `ilhas/ohmetria/PROMPT.md` | *"`foco.md` na raiz nomeia a **robometria**"* | 16/09 |
| `ilhas/jornadafly/PROMPT.md` | idem, texto idêntico | 16/09 |
| `ilhas/clubedomosaico/PROMPT.md` | *"**A ilha está FORA DO FOCO** (`foco.md` nomeia a aquametria desde 21/09) … **despacho NORMAL de ilha fora do foco espera**"* — na abertura do despacho **aberto** da ilha que hoje recebe todas as execuções | 23/09 |

A ponta da robometria é a mais cara das cinco: lida ao pé da letra ela manda entregar a uma ilha em **modo de
medição** todas as execuções e o teto inteiro de link, o contrário do que o despacho do Raphael de 21/09 — no
mesmo arquivo, 260 linhas acima — decidiu. A da clubedomosaico é a mais próxima de virar defeito: manda adiar
o despacho aberto da ilha em foco.

- **O que eu fiz: CORRIGIDO.** Ponteiro datado em cada um dos cinco, dizendo qual é a data da ponta velha, o
  que vale hoje e onde está a decisão que manda. **Nenhuma linha de história foi apagada** — a 1.2 continua
  legível do jeito que foi escrita, e o `foco.md` continua sendo a fonte.

### M2. O `sub_id` com hífen: a Shopee recusa, e o hífen está em três lugares

A **25.7** do `ARQUIPELAGO.md` mediu em 16/09/2026, com chamada real: `robometria`, `aquametria`,
`clubedomosaico` e `rbmR1` são aceitos; `controle-de-bancada` e `teste_bancada` devolvem
`[11001] Params Error : invalid sub id`. **Hífen e sublinhado estão fora.** Contei os valores de `sub_id_2`
nos bancos das três ilhas no ar:

- **(a) `ilhas/clubedomosaico/PROMPT.md`, "Específico desta ilha"** mandava usar `G-PASTILHAS`, `G-ALICATES`,
  `G-COLAS` e `T-VASO` como `Sub_id 2`. Quatro códigos com hífen, prescritos para a ilha que **acabou de
  regerar 31 links pela Open API** no BLOCO 0 de 25/09. E a mesma linha já tinha sido corrigida uma vez, pelo
  Pente Fino em 14/09, **só na metade do Mercado Livre** — a metade da Shopee ficou de pé.
  **O que eu fiz: CORRIGIDO** — os quatro sem hífen, mais o `GUIA` que o banco desta ilha já usa em 13
  registros de alicate, com o ponteiro citando a 25.7.
- **(b) `ilhas/clubedomosaico/dados/esquema-banco.json`** repete a lista velha na observação do campo:
  *"Codigo da pagina de origem: F1, F2, G-COLAS, G-PASTILHAS, T-VASO."*
  **O que eu fiz: REGISTRADO, não corrigido.** Este arquivo está no `manifest.json` com `sha256`; editá-lo sem
  incrementar a revisão faria o Sync recusar o desembarque inteiro com "sha256 divergente" (seção 4). É uma
  linha de bloco da Fundação, não de auditoria.
- **(c) `ilhas/robometria/dados/malha-pecas.json`: **58 registros** com `sub_id_2: "M-PECAS"`, carimbado por
  `ferramentas/gerar-malha-pecas.py:183`, escrito em **21/09** — cinco dias **depois** de a 25.7 medir que o
  hífen é recusado. E há uma segunda metade: os `url`/`url_busca` desses 58 registros são links **já
  encurtados**, herdados de `pecas.json`, então o campo afirma um `sub_id_2` que **ninguém mediu** no link. É a
  moral da 25.8 em pessoa — *"o banco é o resumo e o link é o fato"*.
  **O que eu fiz: REGISTRADO, e a outra metade fica NÃO VERIFICADA.** Só o `utm_content` do 301 diria qual
  `sub_id` o link carrega, e a 25.8 proíbe conferir link **de ilha** por esse caminho, porque o salto do
  encurtador é onde a plataforma conta o clique — e a robometria ainda espera o primeiro clique orgânico.
  Corrigir exige regerar link e mexer em derivado com `sha256`: é bloco, não conserto.

### M3. A 29.6 responde a pergunta que o ponteiro da 1.2 deixou aberta para o Raphael — **PRECISA DO RAPHAEL**

- O ponteiro do Pente Fino de **21/09**, dentro da **1.2**, diz textualmente: *"O que este ponteiro NÃO decide,
  porque as duas leituras são defensáveis e a escolha é do Raphael: se a **ronda diária TÉCNICA** … também
  volta a rodar nas quatro ilhas fora do foco … Enquanto ele não disser, a leitura semanal mede todas e a ronda
  técnica segue a letra da 1.2."* A mesma pendência está escrita em "Precisa do Raphael" no `PAINEL.md`.
- A **29.6**, escrita em **24/09** por uma execução da Fundação, diz: *"A 1.2-b.1 manda a medição continuar em
  toda ilha justamente por isso, e **a medição de uma ilha fora do foco custa um `conferir-no-ar.py`** — que é
  um comando, não um bloco."* Isso **é** a ronda técnica, e é exatamente a metade que o ponteiro deixou em
  aberto.
- As duas não podem valer juntas: ou as quatro ilhas fora do foco recebem `conferir-no-ar.py`, ou não recebem.
- **O que eu fiz: PRECISA DO RAPHAEL.** É regra de política e as duas leituras continuam defensáveis — a 29.6
  tem a melhor causa (a ilha caiu nove dias sem ninguém ver), e a 1.2 tem a decisão escrita dele. Não toquei
  em nenhuma das duas.

### M4. A 29.2 manda medir três URLs em **toda ilha**, e duas das três ilhas no ar não medem nenhuma — e uma nem tem o arquivo

A 29.2 diz: *"O `conferir-no-ar.py` de **toda ilha** mede, além do que já mede, as três URLs que o Google usa"*
— `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`, mais o 404 que tem de ser 404. Medido hoje:

- `ilhas/clubedomosaico/ferramentas/conferir-no-ar.py` — mede as três e o 404. **Cumpre.**
- `ilhas/robometria/ferramentas/conferir-no-ar.py` — **zero** ocorrência das três.
- `ilhas/aquametria/` — **não tem** `conferir-no-ar.py`: a ilha tem onze conferidores por assunto
  (`conferir-robots-no-ar.py`, `conferir-peixes-no-ar.py`, …). A regra nomeia um arquivo que essa ilha não tem.

Isso é a classe 4 do meu próprio trabalho: **regra escrita a partir do caso que quebrou**, e não da regra. Ela
descreve a ilha da cicatriz e desqualifica, por acidente, um desenho legítimo da ilha vizinha.

- **O que eu fiz: REGISTRADO.** Escrever o portão nas duas ilhas é bloco, e reescrever a 29.2 para falar de
  "a conferência no ar da ilha" em vez de um nome de arquivo é regra nova de política — proponho e paro
  (ver **O PADRÃO**).

### M5. Quatro pontas da robometria travavam a leva 5b num sitemap aceito há doze dias — **CORRIGIDO nas quatro**

`ilhas/robometria/PROMPT.md` (duas pontas, escritas em 11/09) e `ilhas/robometria/ESTADO.md` (duas, mesma data)
dizem, em tempo presente, *"esta ilha não publica leva de malha enquanto o sitemap não for reenviado"* e
*"**A leva de malha (5b) continua travada**"*. Contra, nos mesmos dois arquivos: item 4 da DEFINIÇÃO DE PRONTA
— *"**FECHADO em 16/09/2026**: processado, última leitura 15/09, 9 páginas encontradas"* — e
*"**A PRIMEIRA LEVA SAIU EM 21/09/2026, 19h54Z — CINCO URLs NO AR, CONFERIDAS**"*, que é o que o `bloco_atual`
do cabeçalho do `ESTADO.md` também registra.

- **O que eu fiz: CORRIGIDO** com ponteiro datado nas quatro, dizendo o que trava a ilha hoje: o despacho do
  Raphael de 21/09 (modo de medição), não o Search Console. O `ARVORE.md` da mesma ilha já tinha achado este
  defeito em 21/09 e corrigido **só a si mesmo**; as quatro pontas ficaram.

### M6. O alvo (c) da robometria diz `EGRESS_BLOCKED` num domínio que a própria ilha mediu aberto — **CORRIGIDO**

A linha é de **09/09** (`git blame`): *"Hoje o domínio devolve `EGRESS_BLOCKED`; no dia em que abrir…"*, sobre
`mais.conteudo.wap.ind.br`. A medição de **17/09 às 12h35Z**, no mesmo arquivo, lista
`mais.conteudo.wap.ind.br  200  aberto` e conclui *"OS CINCO CAMINHOS ESTAO ABERTOS"*. É a **25.4-b.3**: motivo
velho manda não tentar.

- **O que eu fiz: CORRIGIDO** com ponteiro datado, dizendo que "hoje" ali é 09/09 e que esse dia chegou.

### M7. Um bloco sob `## FECHADOS` sem a linha de fechamento que o próprio arquivo exige — **CORRIGIDO**

`dados/despachos.md` abre mandando: *"**Nunca apagar despacho fechado**: fecha-se escrevendo a data e a
justificativa embaixo dele."* O último bloco do arquivo está sob `## FECHADOS` e **nunca recebeu essa linha** —
termina afirmando, em tempo presente, *"**Enquanto isso não acontecer, nenhuma execução da Fundação move o
item 2**"*, sobre cinco domínios que o Raphael liberou em 17/09 e um item que a robometria fechou em 20/09.

- **O que eu fiz: CORRIGIDO** — escrevi a linha de fechamento que o arquivo pede, com as duas evidências que já
  estavam no repositório (a medição de 17/09 no `PROMPT.md` e o `estado: viva # PRONTA em 20/09` do cabeçalho
  do `ESTADO.md`), e registrei de passagem que dois dos cinco nomes da lista — `www.mi.com.br` e
  `loja.positivotecnologia.com.br` — **não existem em DNS**, que é a lição da 20.3 e não o fato.

### M8. Um item ABERTO diz que falta uma credencial que o repositório prova existir — **PRECISA DO RAPHAEL (a outra metade)**

`dados/despachos.md`, seção `## ABERTOS`, item 2: *"A credencial da conta de serviço do Google no ambiente
(`GOOGLE_SA_B64`…). A conta de serviço **já é Leitor** … então **falta a variável**, não a permissão."* Contra:
o `MAOS-LOG.md` do disparo de **23/09 19h51Z** registra que *"só foi verificada a **presença da variável**"* —
e aquela mesma passada rodou `ferramentas/search-console.py` **pela nuvem** e commitou saída real em
`ilhas/robometria/dados/search-console-2026-09-23.md`. O `ferramentas/ga4.py` declara no cabeçalho usar
*"a MESMA da Search Console — `GOOGLE_SA_B64`"*.

- **O que eu fiz: REGISTRADO, sem fechar.** O "Pronto quando" desse item é um **E** de duas condições, e a
  outra — `curl` a `www.googletagmanager.com` devolvendo 200 de dentro de uma rotina — **não verifiquei**, e
  ela continua sendo passo do Raphael. Mas a **afirmação** "falta a variável" está desmentida, e ela é do tipo
  que manda a execução seguinte nem tentar.

### M9. Um item de despacho cumprido há quatro dias continuava sem a linha que os dois irmãos ganharam — **CORRIGIDO**

`ilhas/clubedomosaico/PROMPT.md`, item **3** do despacho da Sentinela de 23/09: *"Pronto quando: o cabeçalho do
`ESTADO.md` trouxer `urls_publicadas: 17`…"*. O cabeçalho traz `urls_publicadas: 17` desde 24/09, e o **BLOCO
D** do despacho do Raphael, no mesmo arquivo, registra a contagem refeita no sitemap no ar. Os itens 1 e 2
receberam nota de estado; o 3 não.

- **O que eu fiz: CORRIGIDO** pela 18.4 — nota de cumprimento com as duas evidências, sem apagar o item.

### M10. O único despacho ABERTO do Raphael nesta ilha estava aninhado dentro de um despacho CUMPRIDO — **CORRIGIDO**

`## DESPACHO DO RAPHAEL — 24/09/2026` estava escrito como `###`, isto é, como **subseção** do
`## DESPACHO DA SENTINELA — 12/09/2026`, que está cumprido e termina com *"Nada mais nesta ronda."* Pela
**18.1**, despacho do Raphael vem antes do da Sentinela.

- **O que eu fiz: CORRIGIDO** — só o nível do título subiu de `###` para `##`. **Nada foi movido nem
  reordenado**: mover o bloco mudaria a ordem de leitura da fila, e isso não é meu.

### M11. A leitura semanal da aquametria conta 48 URLs 49 minutos depois de a ilha ir para 52 — **REGISTRADO**

- `ilhas/aquametria/PROMPT.md`, leitura semanal de **23/09 20h05Z**: *"`piso: abaixo` — **48 URLs** (passa das
  40)"*.
- A leva 9 saiu às **19h16Z do mesmo dia**, *"a ilha de 48 para 52"* (`ESTADO.md`, `congelamento`, e a linha da
  leva no `PROMPT.md`). O cabeçalho traz `urls_publicadas: 52` e a conferência de 24/09 mediu *"as **52** URLs
  do sitemap"*.
- O que isso carrega: o "Pronto quando" da Proposta 2 dessa mesma leitura congela o denominador — *"registrar
  **47 ou mais indexadas de 48**"* — e ele será lido na leitura de 30/09 contra um site de 52.
- **O que eu fiz: REGISTRADO, e de propósito não mexi.** A **1.2-b.4** diz que critério reescrito depois do
  dado é critério dobrado para caber no dado; trocar o denominador de um critério pré-registrado é decisão de
  quem o escreveu, não minha.

### M12. Dois cabeçalhos de estado seguem incompletos — **herdado, aberto há 12 dias**

Passados os seis `ESTADO.md` por `yaml.safe_load` e conferidos chave a chave contra a seção 2:
`ilhas/ohmetria/ESTADO.md` não tem **`ultima_ronda`** nem **`bloqueada_por`**; `ilhas/clubedomosaico/ESTADO.md`
não tem **`bloqueada_por`**. A seção 2 chama o cabeçalho de obrigatório e lista os dois campos. É o M12 de
21/09 e o M10 de 16/09, **e encolheu pela metade**: a clubedomosaico ganhou `ultima_ronda` na ronda de
23/09 e só lhe falta o `bloqueada_por`; a ohmetria continua sem os dois. Não consertei porque escrever
campo em cabeçalho de ilha é fecho de bloco de quem a reservar, e os dois valores corretos dependem de quem
rondou a ilha — que é justamente o que a M3 deixa em aberto.

---

## BAIXO — ruído

### B1. A 22.8 nomeia `ferramentas/teste-desenho.mjs`, que não existe em nenhuma das cinco ilhas — registrado
*"Cada ilha ganha `ferramentas/teste-desenho.mjs`. Ele abre as páginas com JavaScript desligado e reprova se
faltar…"*. O arquivo não existe em ilha nenhuma. **O portão existe e é cumprido** — medido: a clubedomosaico o
mede em `teste-navegador-atelie.mjs` e `conferir-atelie-no-ar.py` com `javaScriptEnabled: false`, e a
aquametria em `teste-escada-compra.py` por `fetch` + `DOMParser`, as duas citando "portão 22.8" no código. O
que está errado é o contrato nomear um arquivo em vez do portão.

### B2. A seção 11, passo 7, cita `dados/redirecionamentos.json`, que não existe em ilha nenhuma — registrado
*"Redirecionamento 301 — `dados/redirecionamentos.json` no repositório, lido pela casca."* Nenhuma das cinco
ilhas tem o arquivo. Hoje sem consequência: a 16.8 registra que nenhuma URL mudou em ilha nenhuma, então não há
301 a guardar. Vira defeito no primeiro dia em que uma URL se mover.

### B3. "Quem fechar o bloco risca os dois itens" — e os dois itens não estão mais no arquivo — registrado
`ilhas/aquametria/PROMPT.md`, leitura semanal de 23/09: *"**Esta leitura NÃO apagou esses dois itens do
despacho da ronda**, de propósito … **Quem fechar o bloco risca os dois itens.**"* A seção da ronda diária de
23/09, no mesmo arquivo, tem só o `### 3.` e o item 5 riscado de 13/09 — **não há item 1 nem item 2**. A
instrução é inexecutável e a afirmação "NÃO apagou" é falsa contra o próprio arquivo. Não corrigi porque
apagar ou reescrever verificação dentro de despacho aberto é de quem o escreveu.

### B4. O dossiê do JornadaFly não traz V por ferramenta, que a 3.1 passou a exigir na 005 — registrado
`BUSSOLA.md` 3.1: *"**V é por ferramenta, não por nicho** … No dossiê, escreva V ferramenta por ferramenta"*, e
a seção diz valer "da 005 em diante". O `dossies/viagem-experiencia-icone/DOSSIE.md` é da 005, nomeia F1, F2 e
F3, e traz **`V 4`** como nota de nicho. O dossiê irmão da mesma rodada cumpre a regra com tabela por
ferramenta e cita a 3.1 pelo número. Decisão já tomada — a ilha nasceu —, então é registro, não reabertura.

### B5. `primeira_indexacao: desconhecida` é um terceiro valor que a 21.6 não prevê — registrado
A 21.6 manda `primeira_indexacao: <data ou null>`. `ilhas/clubedomosaico/ESTADO.md` traz `desconhecida`. É
honesto — o domínio teve vida anterior e a data real não se sabe — e é justamente por ser honesto que merece
uma linha na 21.6 em vez de um valor fora do vocabulário. Regra nova de política: proponho e paro.

### B6. Quatro ruídos da `fila.md` seguem abertos desde 21/09 — herdados, **7 dias**
Os quatro do B2 e do B3 daquele relatório, reconferidos hoje e idênticos: *"a melhor Facilidade da fila inteira
(4,40)"* é falso pela própria fila (som automotivo dá 4,64); o ranking não está ordenado pelo índice no 2º e no
3º (3,92 acima de 3,94); a coluna `#` pula do 16 para o 18; e "Ilhas nascidas" lista **3** ilhas enquanto a
coluna Estado da mesma tabela marca **5** como `ilha` e o `README.md` nomeia as cinco. **A aritmética, essa,
está limpa:** recalculei as 17 linhas contra as quatro fórmulas declaradas e **zero** divergência acima de
0,05.

---

## Segredo em lugar errado — registro, nunca conserto

**O token do Sync continua em texto puro no repositório público.** Tipo: **token de autenticação do endpoint de
Sync, embutido em query string**. *(O valor não está transcrito aqui nem no commit.)*

| arquivo | onde | tipo |
|---|---|---|
| `ilhas/robometria/PROMPT.md` | linha 21 | token do Sync em query string |
| `ilhas/aquametria/PROMPT.md` | linha 14 | token do Sync em query string |
| `ilhas/clubedomosaico/PROMPT.md` | linhas 45 e 47 | o mesmo token, no Sync e no parâmetro `token=` da rota de cópia das peças (§24) |
| `ilhas/clubedomosaico/PROMPT.md` | linha 14, aviso da §29 | a rota `v1/rotas` de reparo da porta de entrada, que usa o mesmo token |
| `ilhas/aquametria/REGISTRO.md` | ~13 linhas | o endpoint completo, em histórico append-only |
| `ilhas/robometria/REGISTRO.md` | histórico | idem |

**Aberto há 14 dias**, desde o G4 da rodada de 14/09, e **ganhou um lugar novo nesta semana**: a seção 29,
escrita em 24/09, criou a rota `?rest_route=/<ilha>/v1/rotas&token=<token do Sync>`, que **repara o `.htaccess`
com `&reparar=1`** — o mesmo token passou a abrir a porta de entrada do site, não só o Sync. O conserto
continua tendo duas metades e as duas são dele: gerar token novo em cada ilha e passar a lê-lo do documento
`arquipelago-credenciais` do Drive, como a 25.6 já manda. O contrato registra a própria dívida na 25.6.

**Também registrado, e não é credencial:** o e-mail pessoal da artesã segue em arquivo versionado
(`ilhas/clubedomosaico/PROMPT.md`, 5 linhas, e `ESTADO.md`, 2). Mesma pendência de 14/09, **aberta há 14 dias**,
e é dado de uma pessoa de verdade — decisão dele, não minha.

---

## Pendências do Pente Fino anterior (21/09/2026)

| # | o que é | estado hoje | há quanto tempo |
|---|---|---|---|
| **G1** | `cobertura-r1.json` afirmando 15 com o comando devolvendo 11 | **FECHADO** — `validar-derivados.py` rodado hoje: 9 derivados reconstruídos e idênticos ao commitado | — |
| **G2** | o `foco.md` nomeando uma ilha PRONTA e proibida de receber investimento | **FECHADO** — o Raphael trocou o foco em 24/09 e escreveu o motivo | — |
| **G3** | a 1.2-b × a 1.2 sobre quem mede ilha fora do foco | **ABERTO, e agora com uma terceira ponta** (M3: a 29.6) | **7 dias** |
| **M9/M10/M11** | URL e token do Clube do Mosaico, altura do cabeçalho, "FLY" azul no JornadaFly | **ABERTOS** — os três são PRECISA DO RAPHAEL e nenhum mudou | **7 dias** |
| **M12** | `ultima_ronda` e `bloqueada_por` ausentes nas mesmas duas ilhas | **ABERTO, e menor:** a clubedomosaico ganhou `ultima_ronda` na ronda de 23/09 e só falta `bloqueada_por`; a ohmetria segue sem os dois — M12 | **12 dias** |
| **G4 (de 14/09)** | token do Sync em texto puro | **ABERTO e pior** — ganhou a rota de reparo da §29 | **14 dias** |
| **B14 (de 21/09) / B3 (de 14/09)** | o `PAINEL.md` atrasado | **ABERTO e pior:** escrito em 23/09 15h00Z, ele nomeia a **aquametria** como ilha em foco, dá 13 URLs à clubedomosaico (são 17) e 48 à aquametria (são 52). **Não é meu para consertar: a 23.1 diz que ninguém além da ronda escreve nesse arquivo** | **14 dias** |
| **B2/B3 (de 21/09)** | os quatro ruídos da `fila.md` | **ABERTOS**, idênticos — B6 | **7 dias** |
| — | `aquametria/ARVORE.md` "37" × banco de 39 · `clubedomosaico/ARVORE.md` "11 URLs" × três números | **ABERTOS**, não remedidos nesta rodada — **não verificado** | **7 dias** |

---

## O PADRÃO

1. **O defeito não viaja mais entre pessoas nem entre dias: ele viaja entre IRMÃOS, no mesmo commit.** Em 24/09
   uma execução corrigiu o aviso de foco de **uma** ilha e escreveu isso na mensagem de commit com todas as
   letras — *"o aviso era de 16/09 e nomeava a robometria, três mundos atrás. Corrigido."* As outras quatro
   ilhas tinham o mesmo aviso, escrito pelo mesmo molde, e nenhuma foi aberta (M1). É a terceira repetição
   literal do achado nº 3 de 21/09: **a correção não viaja com a cópia.**
2. **A ponta velha quase nunca está longe: ela está no mesmo arquivo.** Das doze correções de hoje, **seis**
   tinham as duas pontas dentro do mesmo documento — a robometria dizendo-se em foco 260 linhas abaixo do
   despacho que a tirou do foco; a clubedomosaico abrindo um despacho com "está fora do foco" 60 linhas abaixo
   do aviso que diz "está em foco"; o item cumprido e o BLOCO D que o cumpriu; o alvo bloqueado e a medição que
   o abriu. **Ninguém precisou de um segundo arquivo para se contradizer.**
3. **Regra nova nasce descrevendo a ilha que quebrou.** A 29.2 nomeia `conferir-no-ar.py` porque foi esse o
   arquivo da clubedomosaico; a aquametria, que divide a conferência em onze arquivos por assunto, fica fora
   da regra sem ter feito nada de errado (M4). É a classe 4 acontecendo dentro do contrato.
4. **O portão que faltou continua sendo sobre o LINK, não sobre o banco.** O hífen no `sub_id` está medido
   desde 16/09 e entrou em três lugares depois disso (M2). Nenhum deles é código: são prosa e um campo de
   esquema, e nenhum portão lê prosa.
5. **O que envelhece pior continua sendo o motivo escrito com número.** `EGRESS_BLOCKED`, "falta a variável",
   "o sitemap precisa ser reenviado": três frases verdadeiras no dia em que foram escritas e que, enquanto
   estiveram de pé, mandavam a execução seguinte **nem tentar** (M5, M6, M8). A 25.4-b.3 já nomeou isso e
   ainda não virou hábito fora da ilha onde nasceu.

**A regra de processo que evitaria a próxima.** A ponta velha mora no arquivo irmão, e o que os irmãos têm em
comum é uma **frase copiada**. Proponho para o `ARQUIPELAGO.md`, como **10.z** — escrita aqui e **NÃO
inserida**:

> **10.z — FRASE QUE EXISTE EM MAIS DE UM ARQUIVO SE CORRIGE EM TODOS, NA MESMA PASSADA (28/09/2026).** Quem
> corrigir uma frase por estar desatualizada roda, antes do commit, um `grep` pelo pedaço estável dela no
> repositório inteiro — e corrige **todas** as ocorrências no mesmo commit, ou escreve na mensagem quantas
> deixou e por quê. Vale em especial para o que é copiado de molde entre ilhas: aviso de foco, aviso de rede,
> nome de campo, código de `sub_id`. **Medido em 28/09/2026:** o aviso de foco da clubedomosaico foi corrigido
> em 24/09 e as outras quatro ilhas ficaram com a versão de 16/09, uma delas mandando dar a uma ilha em modo de
> medição todas as execuções da Fundação. O custo do `grep` é de segundos; o custo de não fazê-lo já foi medido
> três rodadas seguidas. **E o avesso, que é o que faz esta regra ser barata de obedecer:** quando a frase
> repetida for lei, ela não devia estar copiada — devia estar no `ARQUIPELAGO.md` uma vez, com os arquivos de
> ilha apontando para ela.
