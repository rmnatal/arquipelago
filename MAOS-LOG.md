# MAOS-LOG

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
