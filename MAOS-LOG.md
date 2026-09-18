# MAOS-LOG — serie historica dos disparos das MAOS

**ESTE ARQUIVO E APPEND-ONLY.** Cada disparo das MAOS acrescenta uma secao NOVA no FIM do arquivo, com data e hora UTC no titulo. Nenhum disparo apaga, reescreve ou resume a secao de um disparo anterior — do mesmo jeito que `dados/indexacao.md` e `dados/audiencia.md` de cada ilha. Um log que se sobrescreve nao serve para nada: ele existe justamente para o caso em que um disparo diz SUCCEEDED e nao chega nada no `main`, e nesse caso o que importa e comparar com os disparos de antes.

O que toda secao tem de conter, sem excecao: a saida de `git status --porcelain`, a de `git diff --stat`, o hash do commit que foi ao `main`, e a contagem do que mudou (quantos registros, quantas linhas, o que foi conferido relendo o arquivo depois de gravar). Se algum passo falhou, a mensagem de erro completa entra aqui tambem — disparo que falhou e o que mais precisa de rastro.

---

## 16/09/2026 — disparo das 13h38 UTC — 68 links de afiliado Shopee na Robometria

## Passo 4 — saida do script (rodado da raiz da copia de trabalho, sobre `origin/main` em `fb9197e`)

```
pecas.json | registros=38 | alterados=35 | com_url_busca_apos_gravar=35 | faltaram=[] | lixo_removido_no_fim=1 chars
modelos-robo.json | registros=43 | alterados=33 | com_url_busca_apos_gravar=33 | faltaram=[] | lixo_removido_no_fim=1 chars
```

## resumo.txt

```
pecas.json | registros=38 | alterados=35 | com_url_busca_apos_gravar=35 | faltaram=[] | lixo_removido_no_fim=1 chars
modelos-robo.json | registros=43 | alterados=33 | com_url_busca_apos_gravar=33 | faltaram=[] | lixo_removido_no_fim=1 chars
```

## Passo 5 — provas

### `git status --porcelain`

```
 M ilhas/robometria/dados/modelos-robo.json
```

`pecas.json` nao aparece porque o `main` atual (`fb9197e`) ja traz os 35 links exatamente
como o mapa manda: o script reescreveu o arquivo e o resultado saiu byte a byte igual ao
que ja estava versionado. Os 35 links estao la, conferidos pelo `grep` abaixo.

### `git diff --stat`

```
 ilhas/robometria/dados/modelos-robo.json | 330 +++++++++++++++----------------
 1 file changed, 165 insertions(+), 165 deletions(-)
```

### `git check-ignore -v ilhas/robometria/dados/pecas.json ; echo "check-ignore saiu com $?"`

```
check-ignore saiu com 1
```

(nenhuma saida antes do `echo`, e codigo 1: o arquivo NAO esta ignorado pelo `.gitignore`)

### `grep -c "s.shopee.com.br" ilhas/robometria/dados/pecas.json`

```
35
```

### `grep -c "s.shopee.com.br" ilhas/robometria/dados/modelos-robo.json`

```
33
```

## Observacoes de execucao

- **Copia de trabalho:** `/home/user/arquipelago`, clone ja existente na maquina com
  `origin = https://github.com/rmnatal/arquipelago`. Onde a instrucao diz `/tmp/arq`, leia
  esse caminho.
- **`/tmp` bloqueado:** o ambiente barrou escrita direta em `/tmp`, entao `mapa.json`,
  `aplicar.py` e `resumo.txt` foram para o diretorio de scratchpad da sessao. Os tres
  caminhos `/tmp/...` do script apontam para lá; conteudo e logica identicos.
- **Primeira tentativa de push recusada:** o commit foi feito sobre `4d24dbe` e, no
  intervalo, `fb9197e` entrou no `main` (canal brasileiro na R2 + reparo do banco). O push
  voltou `403 / fetch first`, o `git pull --rebase origin main` conflitou em
  `modelos-robo.json`, e o trabalho foi refeito do zero sobre o `main` novo — nenhum
  commit de outra sessao foi sobrescrito e nunca houve `--force`.
- **`pecas.json` ja estava pronto no `main` novo:** `fb9197e` corrigiu a duplicacao do
  arquivo (ele tinha DOIS documentos JSON concatenados, o segundo uma copia desatualizada
  sem `url_busca`) e preservou os 35 links. Rodar o script sobre ele nao mudou um byte.
- **Unico desvio do script da instrucao:** a instrucao gravava `modelos-robo.json` com
  `indent=2`, que era o formato do arquivo quando ela foi escrita. O `fb9197e` regravou o
  arquivo com `indent=1` (o mesmo de `pecas.json`). Manter o `indent=2` reindentaria o
  arquivo inteiro — 4947 linhas de diff — desfazendo a formatacao que o `main` acabou de
  adotar. Gravei com `indent=1`, e o diff ficou so nos 33 blocos `afiliado` (165+/165-).
  Os dados escritos sao exatamente os do mapa.
- **`modelos-robo.json` tem 43 registros agora** (eram 38): `fb9197e` acrescentou cinco
  codigos Xiaomi sem canal brasileiro. Nenhum deles esta no mapa, e nenhum foi tocado.

---

## 16/09/2026 — disparo das 14h50 UTC — ronda da Sentinela na robometria: 4 operacoes, 1 commit no `main`

Instrucao recebida no disparo: quatro operacoes no `rmnatal/arquipelago`, branch `main`, num commit so.
Base: `git fetch origin main && git checkout -B trabalho origin/main` — partiu de `7578db7`.
As quatro ancoras da instrucao foram conferidas ANTES de qualquer escrita e as quatro bateram, cada uma
uma unica vez no arquivo. Nada foi adivinhado, nada foi reformatado, nenhuma linha fora da instrucao.

### `git status --porcelain` (antes do commit)

```
 M dados/PAINEL.md
 M ilhas/robometria/ESTADO.md
 M ilhas/robometria/PROMPT.md
 M ilhas/robometria/dados/consertos.md
```

Depois do commit, `git status --porcelain` voltou vazio (so o `MAOS-LOG.md` deste registro ficou pendente,
e vai no commit seguinte).

### `git diff --stat`

```
 dados/PAINEL.md                     | 51 +++++++++++---------
 ilhas/robometria/ESTADO.md          |  2 +-
 ilhas/robometria/PROMPT.md          | 96 +++++++++++++++++++++++++++----------
 ilhas/robometria/dados/consertos.md |  1 +
 4 files changed, 101 insertions(+), 49 deletions(-)
```

### Hash do commit que foi ao `main`

```
07be6b115e2a11d6be08b9775fc1d5c41b977b71
ronda da Sentinela 16/09: despacho novo na robometria (4 itens), ultima_ronda, consertos.md e PAINEL.md
```

Push aceito de primeira: `git push origin HEAD:main` devolveu `7578db7..07be6b1  HEAD -> main`.
Sem rebase, sem force, sem PR. Conferido depois com `git fetch origin main && git log -1 origin/main`:

```
07be6b115e2a11d6be08b9775fc1d5c41b977b71 ronda da Sentinela 16/09: despacho novo na robometria (4 itens), ultima_ronda, consertos.md e PAINEL.md
```

### Contagem do que mudou — relida DOS ARQUIVOS DEPOIS DE GRAVAR

- **OP1 `ilhas/robometria/PROMPT.md`:** o trecho das linhas 95 a 146 (52 linhas, do titulo
  `## DESPACHO DA SENTINELA — 14/09/2026 ...` ate a linha em branco anterior ao
  `### 4. O PISO DA 25.2 — **a conta mudou em 14/09/2026...`) foi apagado e no lugar entraram
  **96 linhas** do bloco novo. Arquivo: **779 -> 823 linhas**. Relendo: `## DESPACHO DA SENTINELA — 16/09/2026`
  aparece **1** vez, `## DESPACHO DA SENTINELA — 14/09/2026` aparece **0** vezes, e os quatro itens do
  despacho novo estao nas linhas 109, 134, 154 e 179. A linha `### 4. O PISO DA 25.2 — **a conta mudou
  em 14/09/2026...` continua no arquivo, agora na linha 191, e tudo dali para baixo ficou intacto —
  por isso o arquivo tem hoje dois cabecalhos comecando por `### 4.`, que e o resultado correto da instrucao.
- **OP2 `ilhas/robometria/ESTADO.md`:** **1 linha** trocada. Relendo, a linha 23 e
  `ultima_ronda: 2026-09-16T14:50Z`; `2026-09-14T14:32Z` nao aparece mais. O bloco multilinha
  `bloco_atual: |` nao foi tocado. Validacao pedida pela instrucao:

```
$ python3 -c "import io,yaml;yaml.safe_load(io.open('ilhas/robometria/ESTADO.md',encoding='utf-8').read().split('---')[1]);print('YAML ok')"
YAML ok
```

- **OP3 `ilhas/robometria/dados/consertos.md`:** **1 linha acrescentada**, na linha 9, logo abaixo da
  linha `| 2026-09-14 | — | **Nenhum conserto.** ...`. Arquivo: **12 -> 13 linhas**; a tabela tem agora
  **2** linhas de dados (`2026-09-14` e `2026-09-16`). Nenhuma linha anterior foi tocada.
- **OP4 `dados/PAINEL.md`:** arquivo inteiro substituido. **47 -> 54 linhas**, 7974 bytes.
  Relendo, a linha 5 e `**Escrito em:** 16/09/2026 14h50Z, pela ronda diária da **robometria**.`
  A tabela de despachos abertos tem 6 linhas, as 4 primeiras desta ronda.

### Passos que falharam

Nenhum. As quatro ancoras bateram, o YAML validou, o push foi aceito na primeira tentativa e o commit
aparece em `origin/main`.

---

## Disparo de 16/09/2026 15h05Z — correcao curta da Sentinela na robometria

**Instrucao recebida:** uma unica operacao, um unico arquivo — `ilhas/robometria/PROMPT.md`.
INSERIR (nada apagado) um bloco com o cabecalho `## DESPACHO DA SENTINELA — 14/09/2026 — O QUE RESTOU,
E E TUDO DO RAPHAEL` imediatamente antes da linha `### 4. O PISO DA 25.2 — **a conta mudou em
14/09/2026, e a divida agora tem outro nome**`, para que os itens 4 e 5 do despacho de 14/09 deixem de
ficar orfaos debaixo do despacho de 16/09.

**Ancora:** a linha do `### 4. O PISO DA 25.2` e unica no arquivo (conferido em codigo antes de
escrever). A outra linha que comeca com `### 4.` (`dateModified` DOS DOIS ARTIGOS...) foi deixada
intacta, como a instrucao mandou.

### git status --porcelain (depois do commit)

```
(vazio — arvore limpa)
```

### git diff --stat (HEAD~1..HEAD)

```
 ilhas/robometria/PROMPT.md | 6 ++++++
 1 file changed, 6 insertions(+)
```

### Commit que foi ao main

```
d4c3a9ba8a68ac9d7f11ddd6bf357fe158b723be ronda da Sentinela 16/09: devolve o cabecalho aos itens 4 e 5 do despacho de 14/09
```

Push direto: `git push origin HEAD:main` aceito na primeira tentativa (`7d90179..d4c3a9b`). Sem rebase,
sem force, sem PR. Conferido com `git fetch origin main && git log -1 origin/main`: o hash acima e o
topo de `origin/main`.

### Contagem, relida do arquivo DEPOIS de gravar

```
$ grep -n '^## DESPACHO\|^### [0-9]\.' ilhas/robometria/PROMPT.md
33:## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz
95:## DESPACHO DA SENTINELA — 16/09/2026 (ronda diária, 14h50Z, no Chrome do Raphael)
109:### 1. QUATRO ITENS APONTAM O BOTÃO DE COMPRA PARA UMA BUSCA QUE DEVOLVE ZERO RESULTADO
134:### 2. A R1 PUBLICA "71 PARES" E "38 MODELOS" NA MESMA FRASE, E OS DOIS NÚMEROS VÊM DE UNIVERSOS DIFERENTES
154:### 3. O PISO DA 25.2 ESTÁ DE PÉ E O TOPO DELE MANDA O LEITOR PARA OUTRO PRODUTO
179:### 4. `dateModified` DOS DOIS ARTIGOS DIZ 13/09 E A PÁGINA MUDOU EM 16/09
193:## DESPACHO DA SENTINELA — 14/09/2026 — O QUE RESTOU, E É TUDO DO RAPHAEL
197:### 4. O PISO DA 25.2 — **a conta mudou em 14/09/2026, e a dívida agora tem outro nome**
213:### 5. ACHADO DE MÉTODO: o teste de vida da 25.4, do jeito que está escrito, NÃO É EXECUTÁVEL hoje — e existe um caminho que funciona
230:## DESPACHO DA SENTINELA — 11/09/2026 (ronda diária, medida no navegador do Raphael)
258:## DESPACHO DA SENTINELA — 10/09/2026 (medição pela nuvem)
271:## DESPACHO DO RAPHAEL — 14/09/2026 — O PISO DE BUSCA — **CUMPRIDO E CONFERIDO NO AR EM 14/09/2026, 15h**
```

Numeros: 6 linhas inseridas, 0 apagadas, 1 arquivo tocado alem deste log. O `### 4. O PISO DA 25.2`
(linha 197) esta agora abaixo do cabecalho `## DESPACHO DA SENTINELA — 14/09/2026 — O QUE RESTOU`
(linha 193), e nao mais abaixo do despacho de 16/09 (linha 95). O item 5 (linha 213) segue no mesmo
bloco. As duas secoes `### 4.` continuam existindo, mas cada uma sob o seu proprio despacho, que era o
ponto da correcao.

### Passos que falharam

Nenhum. A ancora era unica, o diff saiu como insercao pura (6 `+`, 0 `-`), o push foi aceito de
primeira e o commit aparece em `origin/main`. Sync nao foi acionado e nenhum PR foi aberto, conforme a
instrucao.

---

## Disparo de 16/09/2026 15h17Z — insercao do despacho do Raphael sobre o espaco vazio da foto (robometria)

Instrucao do disparo: tarefa unica, um arquivo, uma insercao literal — inserir um bloco novo em
`ilhas/robometria/PROMPT.md` imediatamente ANTES da linha 33 (`## DESPACHO DO RAPHAEL — 11/09/2026 —
a ilha ganha voz`), com uma linha em branco entre o fim do bloco e essa linha. Nada de snippet, nada
de `manifest.json`, nada de `ESTADO.md`. As MAOS nao executaram nenhuma das edicoes descritas DENTRO
do bloco (EDICAO 1 e EDICAO 2 em `robometria-casca.php`, `robometria-r2.php` e `robometria-a2.php`,
subir `revisao`/`sha256` do manifest, acionar Sync): isso e texto do despacho, trabalho da Fundacao,
e a instrucao proibia tocar em arquivo nao nomeado.

### Ponto de partida

```
$ git fetch origin main && git checkout -B trabalho origin/main
 * branch            main       -> FETCH_HEAD
 + e7b1889...d5e9332 main       -> origin/main  (forced update)
Switched to a new branch 'trabalho'
d5e9332 MAOS-LOG: secao do disparo de 16/09 15h05Z (cabecalho dos itens 4 e 5 do despacho de 14/09)
```

### git status --porcelain (antes do commit do trabalho)

```
 M ilhas/robometria/PROMPT.md
```

### git diff --stat

```
 ilhas/robometria/PROMPT.md | 25 +++++++++++++++++++++++++
 1 file changed, 25 insertions(+)
```

`git diff --numstat` confirma insercao pura: `25	0	ilhas/robometria/PROMPT.md`. Nenhuma linha
apagada, nenhum despacho existente reescrito ou reordenado.

### Commit que foi ao main

```
82b7b891e381e7907d211923678872bad402ad81 robometria: despacho — o lugar vazio da foto esta desenhado como spinner e le como site quebrado
```

Push direto: `git push origin HEAD:main` aceito na primeira tentativa (`d5e9332..82b7b89`). Sem rebase,
sem force, sem PR. Conferido com `git fetch origin main && git log -1 origin/main`: o hash acima e o
topo de `origin/main`.

### Contagem, relida do arquivo DEPOIS de gravar

```
$ grep -n '^## DESPACHO' ilhas/robometria/PROMPT.md
33:## DESPACHO DO RAPHAEL — 16/09/2026 — o espaco reservado da foto esta desenhado como uma roda de carregamento
58:## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz
120:## DESPACHO DA SENTINELA — 16/09/2026 (ronda diária, 14h50Z, no Chrome do Raphael)
218:## DESPACHO DA SENTINELA — 14/09/2026 — O QUE RESTOU, E É TUDO DO RAPHAEL
255:## DESPACHO DA SENTINELA — 11/09/2026 (ronda diária, medida no navegador do Raphael)
283:## DESPACHO DA SENTINELA — 10/09/2026 (medição pela nuvem)
296:## DESPACHO DO RAPHAEL — 14/09/2026 — O PISO DE BUSCA — **CUMPRIDO E CONFERIDO NO AR EM 14/09/2026, 15h**

$ wc -l ilhas/robometria/PROMPT.md
854 ilhas/robometria/PROMPT.md

$ sed -n '56,58p' ilhas/robometria/PROMPT.md | cat -A   (so as pontas de cada linha)
**COMO SE SABE QUE FICOU PRONTO:** ... secao 18.$
$
## DESPACHO DO RAPHAEL M-bM-^@M-^T 11/09/2026 M-bM-^@M-^T a ilha ganha voz$
```

Numeros: 25 linhas inseridas, 0 apagadas, 1 arquivo tocado alem deste log. O arquivo foi de 829 para
854 linhas. O bloco novo comeca na linha 33 — exatamente onde ficava o cabecalho de 11/09, que desceu
intacto para a linha 58 — e termina na 56; a linha 57 esta em branco, como a instrucao pediu. Os
outros 5 despachos seguem na mesma ordem relativa de antes, apenas 25 linhas mais abaixo. O texto do
bloco foi conferido contra a instrucao: 7 paragrafos, 3 trechos indentados como bloco de codigo
(a regra CSS antiga, as duas regras novas, a linha de `$html .=`), nenhuma palavra acrescentada.

### Passos que falharam

Nenhum. A ancora da linha 33 era exata e foi validada por assercao antes da gravacao, o diff saiu como
insercao pura, o push foi aceito de primeira e o commit aparece em `origin/main`. Sync nao foi
acionado, nenhum PR foi aberto e nenhum outro arquivo foi tocado, conforme a instrucao.

---

## Disparo de 16/09/2026 16h01Z — insercao do despacho do Raphael sobre a API de Afiliados da Shopee (robometria)

Instrucao do disparo: tarefa unica, um arquivo, uma insercao literal — inserir um bloco novo em
`ilhas/robometria/PROMPT.md` imediatamente ANTES da linha `## DESPACHO DO RAPHAEL — 16/09/2026 — o
espaco reservado da foto esta desenhado como uma roda de carregamento` (linha 33 antes da edicao),
com uma linha em branco entre o fim do bloco e essa linha, sem apagar nem reordenar nada. As MAOS
NAO executaram nenhum dos trabalhos descritos DENTRO do bloco (criar `ferramentas/shopee-api.py`,
mexer em `dados/esquema-banco.json`, `validar-banco.py`, `dados/pecas.json`,
`dados/modelos-robo.json` ou na vitrine; ler documento no Google Drive; tocar em credencial de
qualquer especie): isso e texto do despacho, trabalho da Fundacao, e a instrucao proibia tocar em
arquivo nao nomeado. Nenhuma credencial foi lida, gravada, impressa ou passada adiante neste
disparo — o bloco inserido cita apenas NOMES de campo, nunca valores.

### Ponto de partida

```
$ git fetch origin main && git checkout -B trabalho origin/main
 * branch            main       -> FETCH_HEAD
 + e7b1889...22e59b1 main       -> origin/main  (forced update)
Switched to a new branch 'trabalho'
22e59b1 MAOS-LOG: secao do disparo de 16/09 15h17Z (despacho do espaco vazio da foto na robometria)
```

### git status --porcelain (antes do commit do trabalho)

```
 M ilhas/robometria/PROMPT.md
```

### git diff --stat

```
 ilhas/robometria/PROMPT.md | 27 +++++++++++++++++++++++++++
 1 file changed, 27 insertions(+)
```

Insercao pura, conferida: `git diff -U0 | grep -c '^-[^-]'` devolveu `0` (nenhuma linha apagada).

### Commit que foi ao main

```
8769bbb397ea7b4ad14b81525f2f13f0886a41f8 robometria: despacho — a API da Shopee abriu e fecha foto, encurtamento, ficha de produto e o portao do canal brasileiro
```

Push direto: `git push origin HEAD:main` aceito na primeira tentativa (`22e59b1..8769bbb`). Sem
rebase, sem force, sem PR. Conferido com `git fetch origin main && git log -1 origin/main`: o hash
acima e o topo de `origin/main`.

### Contagem, relida do arquivo DEPOIS de gravar

```
$ grep -n '^## DESPACHO' ilhas/robometria/PROMPT.md
33:## DESPACHO DO RAPHAEL — 16/09/2026 — A API DA SHOPEE FOI LIBERADA, E ELA FECHA QUATRO BURACOS DESTA ILHA DE UMA VEZ
60:## DESPACHO DO RAPHAEL — 16/09/2026 — o espaco reservado da foto esta desenhado como uma roda de carregamento
85:## DESPACHO DO RAPHAEL — 11/09/2026 — a ilha ganha voz
147:## DESPACHO DA SENTINELA — 16/09/2026 (ronda diária, 14h50Z, no Chrome do Raphael)
245:## DESPACHO DA SENTINELA — 14/09/2026 — O QUE RESTOU, E É TUDO DO RAPHAEL
282:## DESPACHO DA SENTINELA — 11/09/2026 (ronda diária, medida no navegador do Raphael)
310:## DESPACHO DA SENTINELA — 10/09/2026 (medição pela nuvem)
323:## DESPACHO DO RAPHAEL — 14/09/2026 — O PISO DE BUSCA — **CUMPRIDO E CONFERIDO NO AR EM 14/09/2026, 15h**

$ wc -l ilhas/robometria/PROMPT.md
881 ilhas/robometria/PROMPT.md

$ sed -n '57,60p' ilhas/robometria/PROMPT.md | cat -A   (so as pontas de cada linha)
$
**COMO SE SABE QUE FICOU PRONTO:** ... nunca imprimindo valor.$
$
## DESPACHO DO RAPHAEL M-bM-^@M-^T 16/09/2026 M-bM-^@M-^T o espaco reservado da foto ...$
```

Numeros: 27 linhas inseridas, 0 apagadas, 1 arquivo tocado alem deste log. O arquivo foi de 854 para
881 linhas. O bloco novo comeca na linha 33 — exatamente onde ficava o cabecalho da roda de
carregamento, que desceu intacto para a linha 60 — e termina na 58; a linha 59 esta em branco, como
a instrucao pediu. Os outros 7 despachos seguem na mesma ordem relativa de antes, apenas 27 linhas
mais abaixo. O texto do bloco foi conferido contra a instrucao: cabecalho, 3 paragrafos de abertura,
a lista numerada de 4 buracos, o paragrafo das credenciais, a linha `**O QUE CONSTRUIR, nesta
ordem:**`, os 4 itens (a) a (d) e o paragrafo de pronta — 26 linhas de bloco mais a linha em branco
de separacao. Nenhuma palavra acrescentada, nenhuma corrigida: o `afiltado.url` do item (c) veio
assim na instrucao e foi gravado assim.

### Passos que falharam

Nenhum. A ancora era exata e foi conferida por `grep -n` antes da gravacao, o diff saiu como
insercao pura, o push foi aceito de primeira e o commit aparece em `origin/main`. Sync nao foi
acionado, nenhum PR foi aberto, nenhuma ilha foi reservada e nenhum outro arquivo foi tocado,
conforme a instrucao.

## Disparo de 16/09/2026 16h10Z — adendo ao despacho da API da Shopee (robometria): escada de palavra-chave e sub-id

Instrucao recebida: uma tarefa unica, um arquivo, uma insercao literal. Arquivo `ilhas/robometria/PROMPT.md`.
O bloco do adendo de 16h07Z entrou imediatamente antes da linha `**COMO SE SABE QUE FICOU PRONTO:**` do
despacho da API da Shopee (a que fala do `git grep` pelo AppID e pela Senha), com uma linha em branco entre
o fim do bloco e essa linha. Nada foi apagado, nada foi reformatado.

Partida: `git fetch origin main && git checkout -B trabalho origin/main`, a partir de `773e55f`.

### `git status --porcelain` (depois do commit do trabalho, antes deste log)

```
(vazio — arvore limpa)
```

### `git diff --stat` (do commit que foi ao `main`)

```
 ilhas/robometria/PROMPT.md | 6 ++++++
 1 file changed, 6 insertions(+)
```

### Commit que foi ao `main`

```
d0b4049760471345dae2ba2a1a6840ccfe79b73c
robometria: adendo ao despacho da API — escada de palavra-chave e sub-id obrigatorio no link gerado
```

Push: `git push origin HEAD:main` aceito de primeira (`773e55f..d0b4049  HEAD -> main`). Nenhum rebase foi
preciso, nenhum force push foi dado, nenhum PR foi aberto. Conferido com `git fetch origin main &&
git log -1 origin/main`: `origin/main` esta em `d0b4049`, que e o commit acima.

### Contagem, conferida relendo o arquivo depois de gravar

```
$ git show HEAD~1:ilhas/robometria/PROMPT.md | wc -l
881
$ wc -l < ilhas/robometria/PROMPT.md
887
$ grep -n "ADENDO DE 16/09/2026, 16h07Z" ilhas/robometria/PROMPT.md
58:**ADENDO DE 16/09/2026, 16h07Z — A CHAMADA FOI FEITA DE VERDADE, ...
$ grep -n "COMO SE SABE QUE FICOU PRONTO" ilhas/robometria/PROMPT.md
64:**COMO SE SABE QUE FICOU PRONTO:** `ferramentas/shopee-api.py` roda e devolve JSON ...
89:**COMO SE SABE QUE FICOU PRONTO:** no HTML servido de uma pagina de cada ferramenta, ...
```

Numeros: 6 linhas inseridas, 0 apagadas, 1 arquivo tocado alem deste log. O arquivo foi de 881 para 887
linhas. O bloco novo ocupa as linhas 58 a 62 — cabecalho do adendo na 58, branco na 59, o item 1 (escada de
palavra-chave) na 60, branco na 61, o item 2 (`offerLink` sem `subId`) na 62 —, a linha 63 esta em branco e
a linha 64 e a ancora `**COMO SE SABE QUE FICOU PRONTO:**` do despacho da API, intacta, que antes estava na
58. A segunda ancora de mesmo nome, a da roda de carregamento, desceu de 83 para 89: as mesmas 6 linhas de
diferenca, nada mais se mexeu. O texto foi conferido palavra por palavra contra a instrucao: cabecalho,
os dois itens numerados, os grifos e as crases estao como vieram. Nenhuma palavra acrescentada, nenhuma
corrigida.

### Passos que falharam

Nenhum. A ancora era exata e foi localizada por `grep -n` antes da gravacao, o diff saiu como insercao pura
de 6 linhas, o push foi aceito de primeira e o commit aparece em `origin/main`. Sync nao foi acionado,
nenhuma ilha foi reservada, nenhum bloco de fila foi executado e nenhum outro arquivo foi tocado, conforme
a instrucao.

---

## Disparo de 16/09/2026 16h19Z — contrato na raiz: a API da Shopee aposenta a fila de links pendentes e a credencial muda de casa

**Instrucao recebida:** tarefa unica, documental, na raiz. Arquivo `ARQUIPELAGO.md`, tres substituicoes
literais. Nenhuma ilha tocada, nenhum outro arquivo tocado alem deste log.

**O que mudou, nas palavras da instrucao:**

1. Dentro da linha longa do cano de links de afiliado (secao das regras de raiz), o trecho entre parenteses
   que mandava a Sentinela montar `dados/links-afiliado-pendentes.md` foi trocado pela regra nova: a fila
   so existe onde o gerador exige clique humano; onde ha API de afiliado (Shopee, desde 16/09/2026, secao
   25.6) o arquivo **nao e criado**; onde nao ha e o gerador tem reCAPTCHA (Mercado Livre) a fila continua
   valendo como antes.
2. Na secao 25.6, o item `Open API da Shopee — APROVADA em 13/09/2026` (cinco linhas: o cabecalho mais as
   quatro recuadas da pegadinha de processo, do aviso de que a Shopee nao da suporte, de onde a credencial
   mora e do que a API mudaria) foi apagado inteiro e substituido pelo item novo de sete linhas
   `Open API da Shopee — LIBERADA E MEDIDA EM 16/09/2026`: endpoint e cabecalho de assinatura, o egresso e
   a lista de dominios permitidos da conta, a correcao da regra anterior sobre onde a credencial mora (sai
   da variavel de ambiente da rotina e vai para o documento privado do Drive), o que a chamada real de
   16h07Z devolveu, as duas descobertas viradas regra (escada de palavra-chave, `offerLink` sem sub-id), o
   que a API aposenta e o que nao aposenta, e o alcance de contrato valendo para o arquipelago inteiro com
   implementacao so na ilha em foco.
3. A linha `A aposta e o piso sao coisas diferentes` virou `A aposta virou chao em 16/09/2026, e o piso
   continua sendo o piso`.

### git status --porcelain

```
$ git status --porcelain
(vazio — arvore limpa; o commit do trabalho ja estava gravado e empurrado quando este log foi escrito)
```

### git diff --stat

```
$ git show --stat --format='' c862832
 ARQUIPELAGO.md | 18 ++++++++++--------
 1 file changed, 10 insertions(+), 8 deletions(-)
```

### Hash do commit que foi ao main

```
$ git fetch origin main && git log -1 origin/main --format='%H %s'
c86283222a2203b805459956abee537a83729d61 contrato: a API da Shopee aposenta a fila de links pendentes, e a
credencial sai da variavel de ambiente para o Drive privado
```

O push para `main` foi recusado na primeira tentativa (`fetch first` — o `main` tinha andado para a211e2a
enquanto o trabalho era feito). Um `git fetch origin main && git rebase origin/main` resolveu, sem
conflito, e o segundo `git push origin HEAD:main` foi aceito (`a211e2a..c862832  HEAD -> main`). Nenhum
force push.

### Contagem, conferida relendo o arquivo depois de gravar

```
$ git show c862832^:ARQUIPELAGO.md | wc -l
850
$ wc -l < ARQUIPELAGO.md
852
$ grep -n "O CANO DE LINKS DE AFILIADO ENCHE EM PARALELO" ARQUIPELAGO.md
233:- **O CANO DE LINKS DE AFILIADO ENCHE EM PARALELO, SEMPRE — ...
$ grep -n "### 25.6" ARQUIPELAGO.md
793:### 25.6 O QUE E AUTOMATICO HOJE, E O QUE SO SERIA COM CREDENCIAL
$ grep -n "Open API da Shopee" ARQUIPELAGO.md
804:- **Open API da Shopee — LIBERADA E MEDIDA EM 16/09/2026. Deixou de ser aposta.** ...
$ grep -n "A aposta virou chao" ARQUIPELAGO.md
812:**A aposta virou chao em 16/09/2026, e o piso continua sendo o piso.** ...
$ grep -c "A aposta e o piso sao coisas diferentes" ARQUIPELAGO.md
0
$ grep -c "APROVADA em 13/09/2026" ARQUIPELAGO.md
0
```

Numeros: um unico arquivo tocado alem deste log. O arquivo foi de 850 para 852 linhas — saldo de duas
linhas, que e exatamente o item da 25.6 saindo com cinco linhas e entrando com sete. As tres substituicoes
foram aplicadas por casamento literal do texto exato, com a contagem de ocorrencias conferida antes de
gravar: cada trecho procurado aparecia **uma unica vez** no arquivo, e o programa abortaria se fosse
diferente. O `git diff -U0` mostra somente as tres regioes: a linha 233, o bloco de 804 a 810 e a linha
812; a linha em branco entre o item da 25.6 e a linha da aposta aparece no diff porque as duas regioes sao
vizinhas e o git juntou o trecho, mas o conteudo dela e identico ao de antes. Os dois textos antigos
sumiram do arquivo (`grep -c` devolve 0 para ambos), o que confirma que a troca foi substituicao e nao
duplicacao. Nenhuma linha foi reformatada, nenhum acento ou crase mexido, nada acrescentado alem do que a
instrucao trouxe.

### Passos que falharam

A recusa do primeiro push, descrita acima, resolvida por rebase — nada mais. Nenhuma ilha foi reservada,
nenhum `executando_desde` foi escrito, nenhum bloco de fila foi executado, o Sync nao foi acionado, nada
foi publicado e nenhum arquivo alem de `ARQUIPELAGO.md` e deste log foi tocado.

---

## 16/09/2026 — disparo das 20h23 UTC — leitura semanal da Sentinela na Robometria (4 passos de arquivo)

Instrucao recebida no disparo: acrescentar uma linha em `ilhas/robometria/dados/indexacao.md`, criar
`ilhas/robometria/dados/posicoes.md`, inserir uma secao de despacho no topo da fila do
`ilhas/robometria/PROMPT.md` e trocar dois campos do cabecalho do `ilhas/robometria/ESTADO.md`. Partida em
`origin/main` = `d188d71`, branch de trabalho criada com `git checkout -B trabalho origin/main`. Editor web do
GitHub nao foi usado (27.2): tudo por copia de trabalho local.

### `git status --porcelain` (antes do commit)

```
 M ilhas/robometria/ESTADO.md
 M ilhas/robometria/PROMPT.md
 M ilhas/robometria/dados/indexacao.md
?? ilhas/robometria/dados/posicoes.md
```

### `git diff --stat` (antes do commit, so os rastreados; `posicoes.md` ainda era `??`)

```
 ilhas/robometria/ESTADO.md          |  4 ++--
 ilhas/robometria/PROMPT.md          | 38 +++++++++++++++++++++++++++++++++++++
 ilhas/robometria/dados/indexacao.md |  1 +
 3 files changed, 41 insertions(+), 2 deletions(-)
```

### `git show --stat` do commit ja em `origin/main` (com o arquivo novo dentro)

```
 ilhas/robometria/ESTADO.md          |  4 ++--
 ilhas/robometria/PROMPT.md          | 38 +++++++++++++++++++++++++++++++++++++
 ilhas/robometria/dados/indexacao.md |  1 +
 ilhas/robometria/dados/posicoes.md  | 18 ++++++++++++++++++
 4 files changed, 59 insertions(+), 2 deletions(-)
```

### Hash do commit que foi ao `main`

```
0deaaf5416108a3d4fc57a572f1b48d305f36165
robometria: leitura semanal da Sentinela de 16/09 — primeira medição com sinal, série de posições nasce
```

Empurrado com `git push origin HEAD:main` de primeira, sem recusa e sem rebase: `d188d71..0deaaf5  HEAD -> main`.
Conferido depois com `git fetch origin main && git log -1 origin/main`, que devolve este mesmo hash — o push
esta em `origin/main`, nao so na copia local.

### Contagem do que mudou, conferida RELENDO os arquivos depois de gravar

```
$ test -f ilhas/robometria/dados/posicoes.md && echo SIM
SIM
$ grep -c '^| 2026-' ilhas/robometria/dados/posicoes.md
5
$ wc -l < ilhas/robometria/dados/posicoes.md
18
$ grep -c '^| 2026-' ilhas/robometria/dados/indexacao.md
2
$ grep -o '^| 2026-[0-9-]*' ilhas/robometria/dados/indexacao.md
| 2026-09-10
| 2026-09-16
$ grep -n '^## DESPACHO' ilhas/robometria/PROMPT.md | head -2
33:## DESPACHO DA SENTINELA — 16/09/2026 (leitura semanal, 19h40Z) — a primeira medicao com sinal...
71:## DESPACHO DO RAPHAEL — 16/09/2026 — a API da Shopee ~~fecha quatro buracos desta ilha~~ ...
$ grep -c '^## DESPACHO' ilhas/robometria/PROMPT.md
9
$ grep -n '^primeira_indexacao:\|^ultima_ronda:' ilhas/robometria/ESTADO.md
7:primeira_indexacao: 2026-09-11
21:ultima_ronda: 2026-09-16T19:40Z
```

Os dois numeros que o passo 6 mandou conferir batem: `dados/posicoes.md` existe e tem **5 linhas de dados**
(mais cabecalho, tabela e as 4 notas da primeira medicao, 18 linhas no total), e `dados/indexacao.md` tem
**2 linhas de dados** — a de 10/09, que ja estava la e nao foi tocada, mais a de 16/09 que entrou agora como
ultima linha. O `PROMPT.md` foi de 8 para 9 secoes `## DESPACHO` e a nova ficou na linha 33, imediatamente
antes da que era a primeira da fila (a da API da Shopee, agora na 71) — **nada foi apagado**, as 38 linhas
do diff sao todas insercao. O `ESTADO.md` mudou exatamente 2 linhas: `primeira_indexacao` de
`desconhecida` para `2026-09-11` e `ultima_ronda` de `2026-09-16T14:50Z` para `2026-09-16T19:40Z`.

As tres edicoes em arquivo existente foram feitas por casamento literal do texto exato, com a contagem de
ocorrencias conferida ANTES de gravar e o programa abortando se fosse diferente de 1: a ancora
`## DESPACHO DO RAPHAEL — 16/09/2026 — a API da Shopee` aparecia uma unica vez, e cada um dos dois campos
do `ESTADO.md` tambem. A linha do `indexacao.md` foi acrescentada depois de confirmar que o arquivo
terminava em `\n` e que a linha ainda nao existia. A mensagem de commit foi passada por arquivo com `-F`,
nunca com `-m`, para nao perder as crases. Nada foi reformatado, nenhum acento ou crase mexido, nenhuma
linha acrescentada alem das que a instrucao trouxe.

### Passos que falharam

Nenhum. Push aceito na primeira tentativa, sem rebase e sem force. Nenhuma ilha foi reservada, nenhum
`executando_desde` foi escrito, nenhum bloco de fila foi executado, o Sync nao foi acionado, nada foi
publicado, nenhuma conta foi criada e nenhum arquivo alem dos quatro nomeados pela instrucao e deste log
foi tocado.

---

## 17/09/2026 — disparo das 23h13 UTC — insercao do despacho do Raphael de 17/09 na Robometria (a rede abriu para os fabricantes)

Tarefa unica: um arquivo, uma insercao literal. `ilhas/robometria/PROMPT.md`, bloco novo imediatamente antes
do despacho do Raphael de 16/09 sobre a API da Shopee. O `REGISTRO.md` nao foi tocado. Nenhum outro arquivo
alem deste log.

### A ancora da instrucao NAO existia com o texto que a instrucao deu — e o que foi feito

A instrucao mandou localizar a linha exata:

```
## DESPACHO DO RAPHAEL — 16/09/2026 — A API DA SHOPEE FOI LIBERADA, E ELA FECHA QUATRO BURACOS DESTA ILHA DE UMA VEZ
```

Essa linha nao existe mais no `main`. `grep` no arquivo devolveu zero ocorrencia. O que existe, e e a MESMA
secao, e:

```
## DESPACHO DO RAPHAEL — 16/09/2026 — a API da Shopee ~~fecha quatro buracos desta ilha~~ — **CUMPRIDO E CONFERIDO NO AR EM 16/09/2026, 17h05Z**
```

A confirmacao nao foi por semelhanca, foi pelo historico: `git log -S` sobre o texto antigo mostra que a linha
nasceu em `8769bbb` com o titulo que a instrucao cita e foi reescrita em `aae66e5`
("robometria: fecha os dois despachos do Raphael de 16/09 e sobe as regras ao contrato"), que a marcou como
cumprida e baixou a caixa alta. Mesma data, mesmo assunto, mesma secao — so o titulo mudou depois que o
despacho foi fechado. A insercao foi feita ali, com a ancora conferida uma unica ocorrencia ANTES de gravar e
o programa abortando se fosse diferente de 1.

### Passo 1 — ponto de partida

```
$ git fetch origin main && git checkout -B trabalho origin/main
00309c8 robometria: fecha a execucao das 19h16Z — e uma data de regua que estava verde por coincidencia da coleta
```

### Passo 2 — `git status --porcelain` e `git diff --stat` antes do commit

```
$ git status --porcelain
 M ilhas/robometria/PROMPT.md

$ git diff --stat
 ilhas/robometria/PROMPT.md | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)

$ git diff --numstat
20	0	ilhas/robometria/PROMPT.md
```

20 insercoes, **0 remocoes**. Nada foi apagado, nada reformatado.

### Passo 3 — hash do commit que foi ao `main`

```
2ae99089d120cd3677f2e0d8402266e5f93e0a8b
robometria: a rede abriu para os cinco fabricantes, e dois dos enderecos registrados nunca existiram
```

### Passo 4 — push e confirmacao em `origin/main`

```
$ git push origin HEAD:main
   00309c8..2ae9908  HEAD -> main

$ git fetch origin main && git log -1 --format='%H %s' origin/main
2ae99089d120cd3677f2e0d8402266e5f93e0a8b robometria: a rede abriu para os cinco fabricantes, e dois dos enderecos registrados nunca existiram
```

Push aceito na primeira tentativa. Sem rebase, sem force, sem PR.

### Passo 5 — contagem conferida RELENDO o arquivo depois de gravar

```
$ grep -c '' ilhas/robometria/PROMPT.md
891
$ git show 00309c8:ilhas/robometria/PROMPT.md | grep -c ''
871
$ git show 00309c8:ilhas/robometria/PROMPT.md | grep -c '^## DESPACHO'
9
$ grep -c '^## DESPACHO' ilhas/robometria/PROMPT.md
10
$ grep -n '^## DESPACHO' ilhas/robometria/PROMPT.md | head -3
33:## DESPACHO DA SENTINELA — 16/09/2026 (leitura semanal, 19h40Z) — a primeira medição com sinal, e o alvo é um só
100:## DESPACHO DO RAPHAEL — 17/09/2026 — A REDE ABRIU PARA OS FABRICANTES, E DOIS DOS CINCO ENDERECOS NUNCA EXISTIRAM
120:## DESPACHO DO RAPHAEL — 16/09/2026 — a API da Shopee ~~fecha quatro buracos desta ilha~~ — **CUMPRIDO E CONFERIDO NO AR EM 16/09/2026, 17h05Z**
$ grep -c '^## DESPACHO DO RAPHAEL — 17/09/2026 — A REDE ABRIU PARA OS FABRICANTES' ilhas/robometria/PROMPT.md
1
```

O arquivo foi de **871 para 891 linhas** (20 a mais, exatamente o tamanho do bloco mais a linha em branco que
o separa da ancora) e de **9 para 10** secoes `## DESPACHO`. O bloco novo comeca na linha 100 e a ancora, que
estava na 100, passou para a 120 — intacta, com uma unica linha em branco entre o fim do bloco e ela. O bloco
aparece uma unica vez. A linha 99 ja era em branco antes da insercao, entao a separacao de cima tambem ficou
correta sem acrescentar nada.

O bloco foi gravado por arquivo, com heredoc de delimitador entre aspas, para as tres crases da tabela de
dominios e as crases simples dos hostnames passarem sem interpretacao do shell. A mensagem de commit foi
passada com `-F -`, nunca com `-m`, pelo mesmo motivo. O texto entrou byte a byte como veio, sem acento
acrescentado, sem hostname corrigido, sem uma linha a mais.

### Passos que falharam

Nenhum passo de git falhou. A unica divergencia do disparo esta registrada na secao "A ancora da instrucao
NAO existia" acima: o titulo da linha-ancora mudou no `main` desde que a instrucao foi escrita, e a insercao
foi feita na secao correspondente, identificada pelo historico do arquivo e nao por palpite.

Nenhuma ilha foi reservada, nenhum `executando_desde` foi escrito, nenhum bloco de fila foi executado, o Sync
nao foi acionado, nada foi publicado, nenhuma conta foi criada, o `REGISTRO.md` nao foi tocado e nenhum
arquivo alem de `ilhas/robometria/PROMPT.md` e deste log foi alterado.

---

## DISPARO DE 17/09/2026, 23h39Z — o teste de vida da Shopee vira teste de navegador, e o item 3 da robometria passa a contar defeito

Instrucao: DOIS arquivos, TRES edicoes literais, UM commit so.

- `ARQUIPELAGO.md` — insercao de um bloco novo logo depois da linha da ronda diaria, dentro da 25.4.
- `ilhas/robometria/PROMPT.md` — EDICAO A: troca do item 3 da DEFINICAO DE PRONTA por duas linhas.
- `ilhas/robometria/PROMPT.md` — EDICAO B: troca do marcador dos "65 de 65 saem por link que NAO rastreia",
  no despacho de 14/09, por uma linha com o texto original riscado mais o texto novo.

As tres ancoras foram encontradas no `main` byte a byte como vieram na instrucao, cada uma uma unica vez.
Nenhuma divergencia. Nada foi reformatado, nada foi "melhorado", nenhuma linha foi acrescentada alem das
que a instrucao trouxe.

### Passo 1 — partida do main real

```
$ git fetch origin main && git checkout -B trabalho origin/main
Switched to a new branch 'trabalho'
$ git log -1 --oneline
1b7a455 maos-log: secao do disparo de 17/09 23h13Z — insercao do despacho de 17/09 na robometria
```

### Passo 3 — commit

Hash que foi ao `main`: **`347010eed005ad02a29f4fbe3d3b41eb8f359606`** (`347010e`).

Mensagem, exatamente a que a instrucao deu:

```
contrato: o teste de vida da Shopee e de navegador, nao de nuvem — e o item 3 da robometria passa a contar defeito, nao vigilancia
```

### Passo 4 — push

```
$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   1b7a455..347010e  HEAD -> main
```

Aceito de primeira. Nenhuma recusa, nenhum rebase, nenhum force push, nenhum PR.

### Passo 5 — confirmacao em origin/main

```
$ git fetch origin main && git log -1 origin/main --format='%H %s'
347010eed005ad02a29f4fbe3d3b41eb8f359606 contrato: o teste de vida da Shopee e de navegador, nao de nuvem — e o item 3 da robometria passa a contar defeito, nao vigilancia
```

### Estado da arvore e diff do commit

```
$ git status --porcelain
(vazio — arvore limpa)
$ git diff --stat HEAD~1 HEAD
 ARQUIPELAGO.md             | 14 ++++++++++++++
 ilhas/robometria/PROMPT.md |  5 +++--
 2 files changed, 17 insertions(+), 2 deletions(-)
```

Sao 14 insercoes e 0 remocoes no `ARQUIPELAGO.md`, e 3 insercoes com 2 remocoes no
`ilhas/robometria/PROMPT.md` — as duas trocas literais.

### Contagem conferida RELENDO os arquivos depois de gravar

```
$ grep -c '' ARQUIPELAGO.md
890
$ git show 1b7a455:ARQUIPELAGO.md | grep -c ''
876
$ grep -c '' ilhas/robometria/PROMPT.md
892
$ git show 1b7a455:ilhas/robometria/PROMPT.md | grep -c ''
891
$ grep -c 'O MODO CERTO DE FAZER ESSE TESTE NA SHOPEE' ARQUIPELAGO.md
1
$ grep -n 'O MODO CERTO DE FAZER ESSE TESTE NA SHOPEE' ARQUIPELAGO.md | cut -d: -f1
778
$ grep -c 'O QUE CONTA E O QUE NÃO CONTA, corrigido em 17/09/2026' ilhas/robometria/PROMPT.md
1
$ grep -c 'ESTA DÍVIDA MORREU EM 16/09/2026' ilhas/robometria/PROMPT.md
1
$ grep -c 'Nenhum item pendente nos despachos' ilhas/robometria/PROMPT.md
0
```

O `ARQUIPELAGO.md` foi de **876 para 890 linhas** (14 a mais, exatamente o tamanho do bloco mais a linha em
branco que o separa da ancora). O bloco novo comeca na linha 778; a ancora da 25.4 ficou na 776, intacta, com
uma unica linha em branco entre ela e o bloco. A linha 791 (a que ja era em branco antes da insercao, entre a
ancora e o `### 25.4-b`) serviu de separacao de baixo, entao nenhuma linha em branco extra foi criada. O bloco
aparece uma unica vez.

O `ilhas/robometria/PROMPT.md` foi de **891 para 892 linhas** (+1 liquido: a EDICAO A trocou 1 linha por 2 e a
EDICAO B trocou 1 linha por 1). Os dois textos novos aparecem uma vez cada. A regua antiga do item 3 —
"Nenhum item pendente nos despachos" — nao existe mais no arquivo: zero ocorrencias, que e a prova de que a
troca foi feita e nao duplicada.

Os textos foram gravados por arquivo, com os acentos escritos como escapes `\u` num script Python, para que
nem o shell nem nenhuma etapa intermediaria tocasse em cedilha, til ou travessao. As tres crases do bloco da
API da Shopee e as chaves do corpo JSON do erro 403 passaram inteiras. A mensagem de commit foi passada com
`-F -`, nunca com `-m`, pelo mesmo motivo — ela tem um travessao.

### Passos que falharam

Nenhum. As tres ancoras existiam, as tres edicoes entraram, o commit foi aceito no `main` de primeira e a
confirmacao em `origin/main` mostra o hash certo.

Nenhuma ilha foi reservada, nenhum `executando_desde` foi escrito, nenhum bloco de fila foi executado, o Sync
nao foi acionado, nada foi publicado, nenhuma conta foi criada, o `REGISTRO.md` nao foi tocado, o
`ARQUIPELAGO.md` nao foi lido para decidir nada — so para achar a ancora — e nenhum arquivo alem dos dois que
a instrucao nomeou e deste log foi alterado.

---

## DISPARO DE 18/09/2026, 01h31Z — a primeira medicao de volume absoluto (arquivo novo na Bussola) e as duas insercoes que ela obriga

Um arquivo novo e duas insercoes literais, num commit so, como a instrucao pediu. Nenhum arquivo alem dos tres
que a instrucao nomeou (mais este log) foi tocado.

### Passo 1 — ponto de partida

Parti do `main` real, nao da branch da sessao:

```
$ git fetch origin main && git checkout -B trabalho origin/main
 + e7b1889...dbde3d3 main       -> origin/main  (forced update)
Switched to a new branch 'trabalho'
```

O `origin/main` de partida era `dbde3d3` (`maos-log: secao do disparo de 17/09 23h39Z`). Vale o registro de que
o fetch veio com **forced update**: o `main` remoto tinha sido reescrito desde o clone desta maquina
(`e7b1889` -> `dbde3d3`). Nada foi forcado por mim — quem forcou foi um disparo anterior; eu so peguei o estado
novo.

### Passo 2 — as ancoras, conferidas antes de escrever

As duas ancoras literais existiam e eram **unicas**, cada uma uma unica vez no seu arquivo:

```
$ grep -c '^## 3.1 Nota que não foi medida não vira índice' bussola/BUSSOLA.md
1
$ grep -n 'DESPACHO DO RAPHAEL — 17/09/2026 — A REDE ABRIU' ilhas/robometria/PROMPT.md
100:## DESPACHO DO RAPHAEL — 17/09/2026 — A REDE ABRIU PARA OS FABRICANTES, E DOIS DOS CINCO ENDERECOS NUNCA EXISTIRAM
```

Nos dois casos a linha imediatamente anterior a ancora ja era uma linha em branco, entao ela serviu de separacao
de cima e eu acrescentei so a de baixo. Nenhuma linha em branco extra foi criada.

### Passo 3 — `git status --porcelain` e `git diff --stat`

```
$ git status --porcelain
M  bussola/BUSSOLA.md
A  bussola/medicoes/volume-absoluto-2026-09-18.md
M  ilhas/robometria/PROMPT.md
```

```
$ git diff --cached --stat
 bussola/BUSSOLA.md                             | 10 ++++
 bussola/medicoes/volume-absoluto-2026-09-18.md | 79 ++++++++++++++++++++++++++
 ilhas/robometria/PROMPT.md                     | 13 +++++
 3 files changed, 102 insertions(+)
```

**102 insercoes, zero remocoes.** Nenhuma linha existente foi apagada ou reescrita em nenhum dos dois arquivos
editados — as duas edicoes sao insercao pura.

### Passo 4 — o commit que foi ao `main`

```
ab8f69fce324a474ef9c2450054b9ffc4aca4f65
bussola: a primeira medicao de volume absoluto do Arquipelago, e o piso que faltava na regua
```

```
$ git push origin HEAD:main
   dbde3d3..ab8f69f  HEAD -> main
```

Aceito de primeira, sem rebase e sem force. Confirmado no remoto, nao no que eu acho que empurrei:

```
$ git fetch origin main && git log -1 origin/main
ab8f69fce324a474ef9c2450054b9ffc4aca4f65
bussola: a primeira medicao de volume absoluto do Arquipelago, e o piso que faltava na regua
2026-09-18 01:31:35 +0000
$ git diff --stat HEAD origin/main
(vazio — a arvore local e a do origin/main sao identicas)
```

### Passo 5 — a contagem, conferida relendo os arquivos DEPOIS de gravar

```
$ wc -l bussola/BUSSOLA.md ilhas/robometria/PROMPT.md bussola/medicoes/volume-absoluto-2026-09-18.md
   118 bussola/BUSSOLA.md
   905 ilhas/robometria/PROMPT.md
    79 bussola/medicoes/volume-absoluto-2026-09-18.md
```

- **`bussola/medicoes/volume-absoluto-2026-09-18.md`** — arquivo NOVO, e a pasta `bussola/medicoes/` tambem nao
  existia (`ls: cannot access 'bussola/medicoes': No such file or directory` antes do `mkdir -p`). **79 linhas**,
  com o cabecalho YAML em `publicar: false`.
- **`bussola/BUSSOLA.md`** — de **108 para 118 linhas** (+10: as 9 linhas do bloco mais a linha em branco que o
  separa da ancora). O bloco novo comeca na linha 55; a ancora `## 3.1 Nota que não foi medida não vira índice`
  desceu para a linha 65, intacta. `grep -c '3.0-b PISO DE DEMANDA'` devolve **1** — o bloco aparece uma unica vez.
- **`ilhas/robometria/PROMPT.md`** — de **892 para 905 linhas** (+13: as 12 linhas do bloco mais a linha em
  branco). O despacho novo de 18/09 comeca na linha 100 e o despacho de 17/09 que era a ancora desceu para a
  linha 113, intacto. `grep -c '18/09/2026 — A ILHA TERMINA'` devolve **1**.

Os tres textos foram gravados por heredoc com delimitador entre aspas simples e as duas insercoes foram feitas
por um script Python que le e escreve em UTF-8 explicito, para que nem o shell nem nenhuma etapa intermediaria
tocasse em cedilha, til, travessao (`—`), traco de faixa (`–`), sinal de multiplicacao (`×`) ou no travessao
solto que marca "abaixo do limiar" nos blocos de codigo. As ancoras foram casadas por igualdade de linha
inteira, com os acentos escritos como escapes `\u` dentro do script, e o script aborta se a ancora aparecer
zero ou mais de uma vez. A mensagem de commit foi passada por `-F -`, nunca por `-m`, pelo mesmo motivo.

### Passos que falharam

Nenhum. A pasta foi criada, as duas ancoras existiam e eram unicas, as tres gravacoes entraram, o commit foi
aceito no `main` de primeira e a confirmacao em `origin/main` mostra o hash certo.

Nenhuma ilha foi reservada, nenhum `executando_desde` foi escrito, nenhum bloco de fila foi executado, o Sync
nao foi acionado, nada foi publicado (o arquivo novo nasceu com `publicar: false`, como a instrucao mandou),
nenhuma conta foi criada, o `REGISTRO.md` nao foi tocado, o `ARQUIPELAGO.md` nao foi lido nem aberto, e nenhum
arquivo alem dos tres que a instrucao nomeou e deste log foi alterado.

---

## DISPARO DE 18/09/2026, 13h02Z — a segunda ordem do dia da robometria (fotos + decisao de outubro) inserida antes do despacho de congelamento

Uma insercao literal num arquivo so, como a instrucao pediu. Nenhum arquivo alem do que a instrucao nomeou
(`ilhas/robometria/PROMPT.md`) e deste log foi tocado.

### Passo 1 — ponto de partida

Parti do `main` real, nao da branch da sessao:

```
$ git fetch origin main && git checkout -B trabalho origin/main
 + e7b1889...af70d53 main       -> origin/main  (forced update)
Switched to a new branch 'trabalho'
```

O `origin/main` de partida era `af70d53` (`robometria: fecho da execucao de 18/09 10h32Z — item 2 da DEFINICAO DE
PRONTA marcado FECHADO`). O fetch veio de novo com **forced update**: o `main` remoto foi reescrito desde o clone
desta maquina (`e7b1889` -> `af70d53`). Nada foi forcado por mim.

### Passo 2 — a ancora, conferida antes de escrever

A ancora literal existia e era **unica** no arquivo:

```
$ grep -n 'DESPACHO DO RAPHAEL — 18/09/2026 — A ILHA TERMINA' ilhas/robometria/PROMPT.md
100:## DESPACHO DO RAPHAEL — 18/09/2026 — A ILHA TERMINA, MAS MUDA DE ESTADO: DE APOSTA PARA EXPERIMENTO MEDIDO
```

A linha 99, imediatamente anterior a ancora, ja era uma linha em branco: ela serviu de separacao de cima, e eu
acrescentei a de baixo (a linha em branco entre o fim do bloco e a ancora, como a instrucao mandou). Nenhuma
linha em branco extra foi criada, nada foi apagado.

### Passo 3 — `git status --porcelain` e `git diff --stat`

```
$ git status --porcelain
 M ilhas/robometria/PROMPT.md
```

```
$ git diff --stat
 ilhas/robometria/PROMPT.md | 31 +++++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)
```

31 linhas inseridas: as 30 linhas do bloco mais a linha em branco de separacao. Zero remocoes.

### Passo 4 — o commit que foi ao `main`

```
$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   af70d53..0db853e  HEAD -> main
```

```
$ git fetch origin main && git log -1 origin/main --format="%H%n%s"
0db853eb9c369c5f9441913b2277438fa871e5d4
robometria: segunda passada de fotos sobre os 76 sem imagem, e a decisao de outubro pre-registrada
```

Hash no `main`: **`0db853eb9c369c5f9441913b2277438fa871e5d4`**. Push aceito de primeira, sem rebase, sem force,
sem PR.

### Passo 5 — contagem conferida relendo o arquivo DEPOIS de gravar

```
$ grep -c "" ilhas/robometria/PROMPT.md
941
```

O arquivo tinha 910 linhas antes e tem 941 depois: +31, o mesmo numero do `diff --stat`. O bloco novo comeca na
linha 100 e a ancora, que era a linha 100, passou a ser a linha 131.

```
$ grep -n '^## DESPACHO DO RAPHAEL — 18/09/2026' ilhas/robometria/PROMPT.md
100:## DESPACHO DO RAPHAEL — 18/09/2026 (segunda ordem do dia) — TERMINAR AS FOTOS, E DEIXAR A DECISAO DE OUTUBRO PRE-REGISTRADA
131:## DESPACHO DO RAPHAEL — 18/09/2026 — A ILHA TERMINA, MAS MUDA DE ESTADO: DE APOSTA PARA EXPERIMENTO MEDIDO
```

Nenhum passo falhou; nao ha mensagem de erro para registrar.

### O que NAO foi feito

Nenhuma ilha foi reservada, nenhum `executando_desde` foi escrito, nenhum bloco de fila foi executado, o Sync nao
foi acionado, nada foi publicado, nenhuma conta foi criada, nenhuma coleta de imagem foi rodada (o bloco inserido
e uma ordem para a ilha, nao para as maos), o `ARQUIPELAGO.md` nao foi lido nem aberto, e nenhum arquivo alem do
que a instrucao nomeou e deste log foi alterado. O log foi num commit proprio, logo apos o commit do trabalho.

## DISPARO DE 18/09/2026, 12h41Z — quatro edicoes literais em quatro arquivos, um commit so: dois cabecalhos de estado limpos, duas linhas de rede abertas e a secao 1.2-b inserida no contrato

Instrucao do disparo: quatro edicoes literais, um commit unico. EDICAO 1 em `ilhas/ohmetria/ESTADO.md`
(`executando_desde` para `null` com o comentario de reserva orfa limpa, e a linha `rede:` trocada de bloqueada
em 2026-09-15 para aberta em 2026-09-18). EDICAO 2 em `ilhas/jornadafly/ESTADO.md` (so a linha `rede:`).
EDICAO 3 em `ilhas/clubedomosaico/ESTADO.md` (so o `executando_desde`). EDICAO 4 em `ARQUIPELAGO.md` (bloco da
secao 1.2-b inserido imediatamente antes da linha da secao 1.1, com uma linha em branco antes e depois). As duas
primeiras mexem em cabecalho de estado, e a instrucao mandou explicitamente.

Partida do `main` real: `git fetch origin main && git checkout -B trabalho origin/main`, a partir de
`7b81221` (`maos-log: secao do disparo de 18/09 13h02Z`).

### Passo 2 — `git status --porcelain` e `git diff --stat` ANTES do commit

```
$ git status --porcelain
 M ARQUIPELAGO.md
 M ilhas/clubedomosaico/ESTADO.md
 M ilhas/jornadafly/ESTADO.md
 M ilhas/ohmetria/ESTADO.md
```

```
$ git diff --stat
 ARQUIPELAGO.md                 | 16 ++++++++++++++++
 ilhas/clubedomosaico/ESTADO.md |  2 +-
 ilhas/jornadafly/ESTADO.md     |  2 +-
 ilhas/ohmetria/ESTADO.md       |  4 ++--
 4 files changed, 20 insertions(+), 4 deletions(-)
```

Depois do commit a arvore ficou limpa — `git status --porcelain` e `git diff --stat` voltaram VAZIOS os dois,
e por isso o que esta gravado acima e a captura de antes do commit, com o `--stat` do proprio commit repetido
abaixo.

### Passo 3 e 4 — commit e push

```
$ git show --stat --format= ee530f2
 ARQUIPELAGO.md                 | 16 ++++++++++++++++
 ilhas/clubedomosaico/ESTADO.md |  2 +-
 ilhas/jornadafly/ESTADO.md     |  2 +-
 ilhas/ohmetria/ESTADO.md       |  4 ++--
 4 files changed, 20 insertions(+), 4 deletions(-)
```

```
$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   7b81221..ee530f2  HEAD -> main
```

```
$ git fetch origin main && git log -1 origin/main --format="%H%n%s"
ee530f2d243bd59d25d7e0864e3240bac1001b97
contrato: fora do foco e modo de medicao, a ordem do foco sai da medicao, e reserva orfa vira lixo que a proxima execucao limpa
```

Hash no `main`: **`ee530f2d243bd59d25d7e0864e3240bac1001b97`**. Push aceito de primeira, sem rebase, sem force,
sem PR.

### Passo 5 — contagem conferida relendo os arquivos DEPOIS de gravar

```
$ grep -c "" ARQUIPELAGO.md   # antes: 890
906
```

O `ARQUIPELAGO.md` tinha 890 linhas antes e tem 906 depois: +16, o mesmo numero do `diff --stat`. Sao as 15
linhas do bloco mais a linha em branco que o separa da ancora; a linha em branco de cima ja existia.

```
$ grep -n '^### 1\.2-b FORA DO FOCO\|^### 1\.1 A RESERVA' ARQUIPELAGO.md
71:### 1.2-b FORA DO FOCO NÃO É PARADA: É MODO DE MEDIÇÃO — e a ordem do foco sai da medição (18/09/2026)
87:### 1.1 A RESERVA ENVELHECE ENQUANTO A EXECUÇÃO ESTÁ VIVA — quem decide é o último commit da ilha (12/09/2026)
```

A ancora, que era a linha 71, passou a ser a 87, e o bloco novo ocupa da 71 a 85 com a 86 em branco. Os tres
cabecalhos de ESTADO.md foram relidos com `yaml.safe_load` depois de gravados e os tres parseiam:

```
ilhas/ohmetria/ESTADO.md        executando_desde=None   rede='aberta em 2026-09-18'
ilhas/jornadafly/ESTADO.md      executando_desde=None   rede='aberta em 2026-09-18'
ilhas/clubedomosaico/ESTADO.md  executando_desde=None   rede=None (esta ilha nao tem campo rede)
```

Uma linha trocada em cada um dos tres, mais a segunda linha trocada na ohmetria: 4 linhas de cabecalho ao todo,
que sao as 4 substituicoes contadas no `--stat` (2+2 na ohmetria, 1+1 na jornadafly, 1+1 na clubedomosaico).

Nenhum passo falhou; nao ha mensagem de erro para registrar.

### O que NAO foi feito

Nenhuma ilha foi reservada — os dois `executando_desde` foram LIMPOS, nao escritos, e a instrucao mandou
explicitamente. Nenhum bloco de fila foi executado, o Sync nao foi acionado, nada foi publicado, nenhum site foi
verificado, nenhuma conta foi criada. O `ARQUIPELAGO.md` foi aberto so para achar a linha ancora e conferir a
insercao, nunca para decidir o que fazer. Nenhum arquivo alem dos quatro que a instrucao nomeou e deste log foi
alterado. O log vai num commit proprio, logo apos o commit do trabalho.

---

## DISPARO DE 18/09/2026, 14h52Z — ronda da Sentinela de 18/09 na robometria: quatro arquivos, um commit so

Instrucao recebida: SENTINELA, ronda diaria de 18/09/2026 14h45Z, ilha robometria. Quatro arquivos, nenhum
deles snippet, nenhum codigo, num commit so. Partiu do `main` real (`9d3a360`), nao da branch da sessao.

### Passo 2 — a mudanca aplicada, byte a byte

1. `ilhas/robometria/ESTADO.md` — a linha `ultima_ronda: 2026-09-16T19:40Z` trocada por
   `ultima_ronda: 2026-09-18T14:45Z`. Uma ocorrencia, conferida antes de trocar. Nada mais no arquivo.
2. `ilhas/robometria/PROMPT.md` — o bloco `## DESPACHO DA SENTINELA — 18/09/2026 (ronda diaria, 14h45Z)`
   inserido inteiro imediatamente ANTES da linha 33, que comecava com
   `## DESPACHO DA SENTINELA — 16/09/2026 (leitura semanal, 19h40Z)`. Nada apagado.
3. `ilhas/robometria/dados/consertos.md` — a linha `| 2026-09-18 | — | ... | — |` acrescentada
   imediatamente depois da linha 9, que comeca com `| 2026-09-16 | — |`. Nada mais no arquivo.
4. `dados/PAINEL.md` (raiz) — conteudo apagado inteiro e regravado com o texto da instrucao, do comeco ao fim.

Todos os quatro trechos-ancora foram achados exatamente como a instrucao escreveu. Nenhum reformatado,
nenhuma linha acrescentada alem do que a instrucao trouxe.

### Passo 3 e 4 — commit e push

```
$ git status --porcelain
 M dados/PAINEL.md
 M ilhas/robometria/ESTADO.md
 M ilhas/robometria/PROMPT.md
 M ilhas/robometria/dados/consertos.md
```

```
$ git diff --stat
 dados/PAINEL.md                     | 41 ++++++++++---------
 ilhas/robometria/ESTADO.md          |  2 +-
 ilhas/robometria/PROMPT.md          | 78 +++++++++++++++++++++++++++++++++++++
 ilhas/robometria/dados/consertos.md |  1 +
 4 files changed, 100 insertions(+), 22 deletions(-)
```

```
$ git show --numstat --format='' HEAD
20	21	dados/PAINEL.md
1	1	ilhas/robometria/ESTADO.md
78	0	ilhas/robometria/PROMPT.md
1	0	ilhas/robometria/dados/consertos.md
```

Mensagem de commit, a da instrucao, sem uma palavra a mais:
`ronda da sentinela 18/09 na robometria: despacho de 4 defeitos, ultima_ronda e painel`

```
$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   9d3a360..8795ef2  HEAD -> main
```

Push aceito de primeira, sem rebase, sem force, sem PR.

### Passo 5 — confirmado no `origin/main`

```
$ git fetch origin main && git log -1 origin/main --format="%H%n%s"
8795ef2c66f50237568588dad2a641a5b23f0102
ronda da sentinela 18/09 na robometria: despacho de 4 defeitos, ultima_ronda e painel
```

Hash no `main`: **`8795ef2c66f50237568588dad2a641a5b23f0102`**. Arquivos alterados: os quatro acima, e so eles.

### Passo 6 — contagem conferida relendo os arquivos DEPOIS de gravar

Contagem de linhas de cada arquivo, antes (em `9d3a360`) e depois:

```
ilhas/robometria/ESTADO.md            antes=501   depois=501    (1 linha trocada, 0 de saldo)
ilhas/robometria/PROMPT.md            antes=980   depois=1058   (+78)
ilhas/robometria/dados/consertos.md   antes=13    depois=14     (+1)
dados/PAINEL.md                       antes=54    depois=53     (-1: 20 gravadas, 21 apagadas)
```

Os saldos batem com o `--numstat` linha a linha. As 78 do `PROMPT.md` sao as 77 do bloco da instrucao mais a
linha em branco que o separa da ancora.

Releitura dos quatro arquivos ja gravados:

```
$ grep -n "^ultima_ronda:" ilhas/robometria/ESTADO.md
19:ultima_ronda: 2026-09-18T14:45Z

$ grep -n "^## DESPACHO DA SENTINELA" ilhas/robometria/PROMPT.md | head -3
33:## DESPACHO DA SENTINELA — 18/09/2026 (ronda diária, 14h45Z) — quatro defeitos...
111:## DESPACHO DA SENTINELA — 16/09/2026 (leitura semanal, 19h40Z) — a primeira medição com sinal...
363:## DESPACHO DA SENTINELA — 16/09/2026 (ronda diária, 14h50Z) — ~~quatro itens~~ — CUMPRIDO...

$ grep -c "^| 2026-09-18 | — |" ilhas/robometria/dados/consertos.md
1

$ sed -n "5p" dados/PAINEL.md
**Escrito em:** 18/09/2026 14h45Z, pela ronda diária da **robometria**.

$ grep -c "18/09/2026 (0 dia)" dados/PAINEL.md
4
```

O despacho novo e o PRIMEIRO do `PROMPT.md` (linha 33), como a instrucao mandou; o de 16/09 da leitura semanal
desceu intacto para a 111 e o de 16/09 da ronda diaria, ja CUMPRIDO, para a 363 — nenhum dos dois tocado. A
linha de 18/09 do `consertos.md` existe uma unica vez. O `PAINEL.md` traz as quatro linhas de despacho aberto
com `18/09/2026 (0 dia)`.

Nenhum passo falhou; nao ha mensagem de erro para registrar.

### O que NAO foi feito

Nenhuma ilha reservada, nenhum `executando_desde` escrito, nenhum cabecalho de estado tocado alem da unica
linha `ultima_ronda` que a instrucao nomeou. Nenhum bloco de fila executado. Nenhum snippet aberto para
conserto — o defeito 3 aponta `snippets/robometria-r1.php` linhas 934-939 e o arquivo NAO foi tocado, porque e
19.2. Nada publicado, `publicar: true` nao mexido, Sync nao acionado, site nao verificado, nenhuma conta
criada. O `ARQUIPELAGO.md` nao foi aberto. Nenhum arquivo alem dos quatro nomeados e deste log foi alterado.
O log vai num commit proprio, logo apos o commit do trabalho, porque o hash so existe depois do commit.

---

## Disparo de 18/09/2026, 15h26Z — duas insercoes literais no `ARQUIPELAGO.md` (25.2-b e a segunda fonte de imagem)

Instrucao recebida no disparo: duas insercoes literais no `ARQUIPELAGO.md` da raiz, num commit so, sem tocar em
nenhum outro arquivo. Bloco 1 imediatamente depois da linha `**O que isso custa, dito sem maquiar:** ...` no fim da
25.2; bloco 2 imediatamente depois da linha `**A foto do produto sai do feed** (image_link), ...` na 25.3. Ambos com
uma linha em branco antes e depois. Nada mais foi pedido e nada mais foi feito.

Hash do commit que foi ao `main`: **`00bc2ef6582c91ad5bcd3b5975655dd43ce2bb95`**

```
$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   e46dfe6..00bc2ef  HEAD -> main

$ git fetch origin main && git log -1 origin/main --format='%H %s'
00bc2ef6582c91ad5bcd3b5975655dd43ce2bb95 contrato: link sem comissao deixa de ser padrao e nunca fica acima de link que rende, e a imagem do fabricante vira segunda fonte
```

```
$ git status --porcelain
(vazio — arvore limpa depois do commit)
```

```
$ git diff --stat HEAD~1 HEAD
 ARQUIPELAGO.md | 27 +++++++++++++++++++++++++++
 1 file changed, 27 insertions(+)

$ git diff --numstat HEAD~1 HEAD
27	0	ARQUIPELAGO.md
```

### Contagem, conferida relendo o arquivo DEPOIS de gravar

```
$ wc -l ARQUIPELAGO.md
933 ARQUIPELAGO.md

$ grep -n "^\*\*25\.2-b" ARQUIPELAGO.md
765:**25.2-b — O LINK QUE NÃO RENDE COMISSÃO DEIXOU DE SER ACEITÁVEL COMO PADRÃO (18/09/2026). Vale para TODAS as ilhas.**

$ grep -n "^\*\*A SEGUNDA FONTE DE IMAGEM" ARQUIPELAGO.md
798:**A SEGUNDA FONTE DE IMAGEM — AUTORIZADA PELO RAPHAEL EM 18/09/2026, e vale para TODAS as ilhas.** ...

$ grep -n "### 25.3\|### 25.4 " ARQUIPELAGO.md
779:### 25.3 Os dois feeds da Shopee, e o que cada um é
811:### 25.4 O teste de vida, que agora existe
```

O arquivo saiu de **906** para **933** linhas: **+27**, exatamente o que o `--numstat` diz. O saldo bate linha a
linha: bloco 1 sao 13 linhas mais a linha em branco que o separa da ancora (14), bloco 2 sao 12 linhas mais a sua
linha em branco (13); 14 + 13 = 27. Nenhuma linha removida, nenhuma linha existente alterada — o diff e `27 0`.

O bloco 1 ficou na 765, logo apos a ancora da 25.2 (linha 763) e antes do cabecalho `### 25.3` (linha 779), com uma
linha em branco de cada lado. O bloco 2 ficou na 798, logo apos a ancora da 25.3 (linha 796) e antes do cabecalho
`### 25.4` (linha 811), tambem com uma linha em branco de cada lado. A ancora de cada insercao aparecia **uma unica
vez** no arquivo — conferido antes de gravar — entao nao houve risco de inserir no lugar errado.

Nenhum passo falhou; nao ha mensagem de erro para registrar. O push foi aceito de primeira, sem rebase e sem
retentativa, e o `git log -1 origin/main` acima mostra o commit das MAOS no topo do `main`.

### O que NAO foi feito

Nenhum arquivo alem do `ARQUIPELAGO.md` e deste log foi tocado. O texto entrou byte a byte como veio na instrucao:
nada reformatado, nada "melhorado", nenhuma linha acrescentada por conta propria. Nenhuma ilha reservada, nenhum
`executando_desde` escrito, nenhum cabecalho de estado tocado. Nenhum bloco de fila executado. Nada publicado,
`publicar: true` nao mexido, Sync nao acionado, site nao verificado, nenhuma conta criada. O `ARQUIPELAGO.md` foi
aberto apenas para localizar as duas ancoras nomeadas pela instrucao, nunca para decidir o que fazer. O log vai num
commit proprio, logo apos o commit do trabalho, porque o hash so existe depois do commit — e porque a instrucao
mandou um commit so para o trabalho.

---

## 18/09/2026 — disparo das 17h06 UTC — registro da prospeccao de imprensa (Gazeta enviada, Circe Bonatelli respondeu)

A instrucao mandou atualizar `claude/prospeccao/registro.md` antes das 15h30 de Brasilia: corrigir a linha da Gazeta
de "a enviar" para "enviado" e acrescentar a linha da Circe Bonatelli / Estadao com status "respondeu".

**O arquivo nao existia no repositorio.** Conferido antes de escrever, tanto na copia de trabalho quanto no `main`
remoto:

```
$ git ls-files | grep -i prospec
(nenhuma saida)

$ git ls-tree -r --name-only origin/main | grep -i -E "prospec|imprensa|claude/"
(nenhuma saida)
```

O diretorio `claude/` inteiro nao existia. A instrucao previa esse caso e mandou cria-lo no caminho esperado com o
cabecalho e o formato pedidos — uma linha por contato com data, veiculo, jornalista, recorte oferecido, status
(a enviar / enviado / respondeu / sem resposta) e a data do follow-up. Foi o que se fez. Como o arquivo nasceu
neste disparo, nao havia conteudo anterior a preservar: as duas linhas entraram juntas, a da Gazeta ja com o
status corrigido.

O arquivo de execucao do dia, `claude/prospeccao/2026-09-18-execucao.md`, **tambem nao existe** — e a instrucao foi
explicita em nao cria-lo nesse caso. Nada foi escrito la. O `2026-09-11-execucao.md`, citado como onde esta o texto
da mensagem da Gazeta, igualmente nao existe neste repositorio; o registro cita o caminho como a instrucao o citou,
sem inventar o texto da mensagem.

### `git status --porcelain` antes do commit

```
A  claude/prospeccao/registro.md
```

### `git diff --stat`

```
 claude/prospeccao/registro.md | 30 ++++++++++++++++++++++++++++++
 1 file changed, 30 insertions(+)
```

### Hash do commit que foi ao `main`

```
578a565c129ceddb094dfcef8682366f18e7dd01

$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   e45e016..578a565  HEAD -> main

$ git fetch origin main && git log -1 origin/main --format='%H%n%s'
578a565c129ceddb094dfcef8682366f18e7dd01
prospeccao: registro de imprensa — Gazeta enviada (WhatsApp, envio manual do Raphael) e Circe Bonatelli/Estadao respondeu
```

Push aceito de primeira, sem rebase, sem retentativa e sem force push.

### Caminho do registro

`claude/prospeccao/registro.md`

### Contagem da rampa — conferida relendo o arquivo DEPOIS do push

O numero que a rampa usa e a quantidade de linhas de contato com status **enviado** ou **respondeu**: **2**.
Conferido lendo o arquivo de volta do `origin/main`, nao pelo que se acha que foi escrito:

```
$ git show origin/main:claude/prospeccao/registro.md | grep -n -E "Gazeta|Bonatelli|Contagem"
10:| 11/09/2026 (mensagem redigida) — envio confirmado pelo Raphael ate 18/09/2026 | Gazeta | nao registrado | texto preservado em `claude/prospeccao/2026-09-11-execucao.md` | **enviado** | a definir |
11:| 17/09/2026 | Estadao | Circe Bonatelli (mercado imobiliario) | "Circe, sua materia de 5/2 sobre o Secovi mostrou estoque de 85,2 mil unidades. Tenho o m2 de lancamento de SP aberto por 98 bairros e 81 estacoes do metro. Reproducao com credito liberada. Mando?" | **respondeu** | enviar o material por e-mail (Raphael) — sem data definida |
28:## Contagem da rampa

$ git show origin/main:claude/prospeccao/registro.md | grep -c -E '^\| .*\*\*(enviado|respondeu)\*\* \|'
2
```

As duas linhas estao no `main`: a da Gazeta com status **enviado**, canal WhatsApp e a observacao de que foi envio
manual do Raphael; a da Circe com status **respondeu** e o pendente registrado como "enviar o material por e-mail
(Raphael) — sem data definida", mais a linha explicita de que a rotina NAO deve recontata-la nem conta-la como alvo
novo, porque o contato esta aberto e a bola esta com o Raphael.

### Uma coisa que NAO entrou no arquivo, e por que

O repositorio e **publico** (`visibility: public`, conferido pela API do GitHub). A instrucao passou, como contexto,
o e-mail direto e o telefone celular com WhatsApp da jornalista. Esses dois campos **nao foram escritos no
registro**: o formato pedido pela propria instrucao tem seis campos (data, veiculo, jornalista, recorte, status,
follow-up) e nenhum deles e contato, e commit em repositorio publico e permanente e indexavel. O registro diz que
ela passou os contatos diretos e que eles ficam com o Raphael, fora do repositorio — que e o que a rotina precisa
saber para nao recontata-la. Nada mais foi omitido: as datas, os horarios, os dois textos literais e o status
entraram como vieram.

### O que NAO foi feito

Nenhum passo falhou; nao ha mensagem de erro para registrar. Nenhum arquivo alem do `claude/prospeccao/registro.md`
e deste log foi tocado — nada de dados de ilhas, nada de credenciais em lugar nenhum. Nenhuma ilha reservada,
nenhum `executando_desde` escrito, nenhum cabecalho de estado tocado, nenhum bloco de fila executado. Nada
publicado, `publicar: true` nao mexido, Sync nao acionado, site nao verificado, nenhuma conta criada. O
`ARQUIPELAGO.md` nao foi aberto para decidir nada. O log vai em commit proprio, logo apos o commit do trabalho,
porque o hash so existe depois do commit.

---

## 18/09/2026 — disparo das 17h10 UTC — REVERSAO: o registro da prospeccao de imprensa da Real 21 sai do `main` deste repositorio

O disparo anterior (17h06Z, secao acima) criou `claude/prospeccao/registro.md` aqui por **erro de enderecamento de
quem disparou**: o assunto e da Real 21 e nao pertence ao `rmnatal/arquipelago`. Este disparo desfaz isso no estado
atual do `main`, sem reescrever historico.

### Passo 2 — estado antes de mexer

```
$ git log --oneline -3 origin/main
b5d83dd maos-log: disparo de 18/09 17h06Z — registro da prospeccao de imprensa criado, commit 578a565
578a565 prospeccao: registro de imprensa — Gazeta enviada (WhatsApp, envio manual do Raphael) e Circe Bonatelli/Estadao respondeu
e45e016 robometria: fecho da execucao de 18/09 16h16Z — itens 2 e 3 conferidos no ar na revisao 67, e o despacho reescrito pela 18.3

$ git ls-files | grep -i prospec
claude/prospeccao/registro.md
```

### Passo 4 — o que o commit errado trouxe

```
$ git show --stat 578a565
commit 578a565c129ceddb094dfcef8682366f18e7dd01
Author: Claude <noreply@anthropic.com>
Date:   Fri Sep 18 17:06:36 2026 +0000

    prospeccao: registro de imprensa — Gazeta enviada (WhatsApp, envio manual do Raphael) e Circe Bonatelli/Estadao respondeu

 claude/prospeccao/registro.md | 30 ++++++++++++++++++++++++++++++
 1 file changed, 30 insertions(+)
```

Um arquivo so. Nenhum outro arquivo de assunto Real 21 foi criado por aquele commit, e nao sobrou nada sob
`claude/` alem dele (`git ls-files claude/` devolvia exatamente `claude/prospeccao/registro.md`). Com o `git rm`, a
pasta `claude/prospeccao/` — e a `claude/` inteira — desapareceu sozinha: nao foi criado `.gitkeep`, nem README, nem
nada no lugar.

### `git status --porcelain` antes do commit

```
D  claude/prospeccao/registro.md
```

### `git diff --stat` da reversao

```
 claude/prospeccao/registro.md | 30 ------------------------------
 1 file changed, 30 deletions(-)
```

### Hash do commit de reversao que foi ao `main`

```
5dff20646cc79d84279dee0e508691c1e671f10c

$ git push origin HEAD:main
To https://github.com/rmnatal/arquipelago
   b5d83dd..5dff206  HEAD -> main
```

Push aceito de primeira: sem rebase, sem retentativa e **sem force push**. O historico nao foi reescrito — os
commits `578a565` e `b5d83dd` continuam existindo e alcancaveis; o que saiu foi o arquivo do estado atual do `main`.

### Passo 7 — prova relida do remoto, nao do local

```
$ git fetch origin main && git ls-tree -r origin/main --name-only | grep -i prospec
(nenhuma linha; grep saiu com codigo 1 = nada encontrado)

$ git log -1 origin/main --format='%H %s'
5dff20646cc79d84279dee0e508691c1e671f10c reverte 578a565: registro da prospeccao de imprensa da Real 21 foi criado aqui por erro de enderecamento — assunto nao pertence a este repositorio
```

Zero arquivos com `prospec` no nome no `main`. Contagem do que mudou, conferida relendo do remoto e nao pelo que se
acha que foi escrito: **1 arquivo removido, 30 linhas deletadas, 0 arquivos criados**.

### A causa, sem rodeio

Foram **dois disparos errados seguidos para este repositorio no mesmo dia, ambos de assunto Real 21, e a causa foi
de quem disparou, nao da execucao** — as maos fizeram ao pe da letra o que veio, em endereco errado. O rastro dos
dois esta no `main`: `578a565` (17h06Z, o arquivo) e `b5d83dd` (17h07Z, a secao de log obrigatoria daquele disparo).

### O que NAO foi feito

Nenhum passo falhou; nao ha mensagem de erro para registrar. As secoes anteriores deste log **nao foram apagadas,
editadas nem resumidas** — inclusive as dos disparos errados: o rastro do erro fica, e o arquivo segue append-only.
Nada de `rebase -i`, `filter-branch` ou force push. Nenhum arquivo alem do `claude/prospeccao/registro.md` (removido)
e deste log foi tocado. Nenhuma ilha reservada, nenhum `executando_desde` escrito, nenhum cabecalho de estado
tocado, nenhum bloco de fila executado. Nada publicado, `publicar: true` nao mexido, Sync nao acionado, site nao
verificado, nenhuma conta criada. O `ARQUIPELAGO.md` nao foi aberto para decidir nada. O log vai em commit proprio,
logo apos o commit da reversao, porque o hash so existe depois do commit.
