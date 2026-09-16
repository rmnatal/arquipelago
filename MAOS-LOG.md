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
