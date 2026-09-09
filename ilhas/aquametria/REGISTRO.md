# Registro de execucoes — Aquametria

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e
o proximo passo desbloqueado, e espelha o mesmo resumo em
`/areas/projeto-aquametria.md` na memoria.

## 2026-09-06 — Estrutura inicial do repositorio

- Criada a pasta `ilhas/aquametria/` com `snippets/`, `conteudo/`, `dados/`
  e `manifest.json` (revisao 0, nada marcado para publicar).
- Fixada a regra: codigo e conteudo do site vivem neste repositorio; o
  WordPress e so o destino, alimentado pelo snippet Sync via manifest.
- A tarefa agendada "Fundacao — Aquametria" foi recriada como
  `trig_01Jg2qeDDsWDJdU9khHVswqd`, dias uteis 11h BRT (cron `0 14 * * 1-5`,
  UTC), sessao nova a cada disparo, com o prompt antigo acrescido do
  "Passo 0 — o repositorio e o lugar do trabalho" e da regra permanente de
  que codigo e conteudo do site nunca vao direto para o WordPress.
- A versao antiga, `trig_01XhxsiuQBX68oUBcJ7LR6pv`, foi desativada e
  renomeada para "[ANTIGA — desativada] ... (sem repo)".

Pendente do Raphael (bloqueia a tarefa): a API de rotinas nao permite anexar
um repositorio, e foi verificado que a sessao disparada sobe sem repo. E
preciso abrir Rotinas no claude.ai, na tarefa "Arquipelago - Fundacao —
Aquametria", e selecionar `rmnatal/arquipelago`. Enquanto isso nao for feito,
a Fundacao roda sem o repositorio e nao consegue commitar.

Tambem pendente do Raphael: dominio com HTTPS e Application Password do
WordPress.

Nao registrado na memoria: esta sessao nao expoe a ferramenta de memoria,
entao `/areas/projeto-aquametria.md` NAO foi atualizado. O conteudo desta
entrada precisa ser copiado para la.

Proximo passo desbloqueado: Bloco 2 do playbook — especificacao das
calculadoras (5 a 8 ferramentas, cada uma com entradas, formula, faixas de
saida, fonte tecnica de cada constante e produtos sugeridos), a partir dos
15 clusters ja levantados no Bloco 1.

## 2026-09-07 — BLOCO 2 entregue: especificacao das calculadoras

Sessao SEM ferramenta de memoria (o estado foi lido de `ESTADO.md`). Sem a
Application Password, o site nao foi tocado: trabalho 100 % no repositorio.
Egresso HTTP: `WebSearch` funciona, `WebFetch` e bloqueado por dominio (a
tentativa em `seachem.com` voltou `EGRESS_BLOCKED`) — por isso todo numero de
fabricante colhido hoje entrou com status `fabricante-via-busca`, a
reconfirmar.

Entregue:
- `dados/especificacao-calculadoras.md` — 8 calculadoras especificadas: C1
  litragem (nucleo), C2 peso e carga no piso, C3 vazao/turnover, C5 aquecedor
  por delta termico, C7 consumo e custo, C8 lotacao, C12 midia filtrante, C15
  iluminacao. Cada uma com entradas, formula, faixa de saida com criterio E
  fonte em cada extremo, produtos sugeridos (com os campos que o Bloco 3 tem
  de entregar) e as recusas explicitas. Inclui o contrato de resposta comum e
  o objeto `aquario` compartilhado (C1 alimenta as outras 7).
- `dados/constantes-calculadoras.json` — 42 registros: toda constante usada ou
  recusada, com fonte, url, data e status. Vocabulario de status criado
  (`fisica`, `verificada-fabricante`, `fabricante-via-busca`,
  `norma-via-secundaria`, `transcrita-varejo`, `divergente-fontes-br`,
  `convencao-editorial`, `pendente`). Regra fixada: constante `pendente` e
  proibida em formula publicada.
- `manifest.json` revisao 1, com os dois arquivos registrados
  (`publicar: false`, sha256 conferivel). O esquema de `dados` ganhou
  `formato: md`, `publicar`, `sha256` e `descricao`.

Dois achados novos, de fabricante, que nenhuma fonte BR do corpus confronta:
1. **Turnover.** Eheim classic 250 (2213) declara 440 L/h para ate 250 L =
   **1,8 renovacoes/h**, contra as 5 a 10 x/h das regras de bolso brasileiras.
   Divergencia de 3 a 6 vezes. Virou o eixo da C3.
2. **Aquecedor.** A propria Eheim declara o Jager de 200 W para **30 a 400 L**
   — faixa de 13 vezes. Serve para escolher potencia comercial, nao para
   dimensionar. Reforca o vacuo n. 2 (potencia por delta termico).
3. Bonus para o vacuo n. 1 (midia): duas ancoras de fabricante, Seachem Matrix
   (1,25 ou 2,6 mL/L — as duas leituras da propria copy conflitam por 2x) e
   Eheim 2213 (3,0 L de filtragem para 250 L = 12 mL/L de cesto). E a primeira
   publicacao BR de mL de midia por litro com fonte de fabricante.

Verificado hoje (novo, fora do corpus do Bloco 1): densidade do vidro float
2500 kg/m3 = 2,5 kg/m2 por mm (Cebrace / Saint-Gobain Sekurit); carga
acidental de piso residencial 1,5 kN/m2 (~153 kgf/m2) dormitorio e sala, 2,0
area de servico, 3,0 corredor publico — ABNT NBR 6120:2019 via fontes
secundarias (norma paga, nao lida direto).

Retido de proposito, por falta de fonte (esta documentado no proprio arquivo,
com o criterio que libera cada item):
- **Espessura de vidro** (C2): sem tensao admissivel e coeficiente de
  seguranca citaveis. Errar aqui alaga casa.
- **Veredito "a laje aguenta"** (C2): a calculadora da a carga, nunca a
  autorizacao. Quem decide e engenheiro.
- **Calculo fisico do aquecedor** `P = U.A.deltaT` (C5): falta o coeficiente U
  do vidro do aquario. Sem ele, a C5 publica a sintese atribuida das regras de
  bolso e diz que ninguem no BR cobre delta > 10 C.
- **Desconto de substrato** (C1): densidade conflita 100 % entre as fontes e
  ninguem publica porosidade. `V_real` fica superestimado; a direcao do erro
  esta tabelada por calculadora (segura para filtro/aquecedor/midia, insegura
  para lotacao e para dosagem). C8 usa o pior caso.
- **"Regra dos 10 %"** (C8): a fonte nao define a base de calculo.
- **C13 dosagem**: nao existe no lote inicial. Risco letal, so 2 dosagens
  verificadas no fabricante, e o volume superestimado da C1 erra para
  overdose. Abre com >= 6 rotulos verificados + marca/concentracao como
  entrada obrigatoria + porosidade resolvida.
- **PPFD** (C15): lm/L ignora profundidade e espectro; nenhuma fonte BR
  publica PPFD por litragem.
- **Tarifa de energia** (C7) e **minima por cidade** (C5): entram como entrada
  do usuario; a coleta (ANEEL e INMET) fica para depois.

C10 confirmado como banco de fichas, nao calculadora. C14 absorvida pela C12
como painel de manutencao. C4, C6, C9 e C11 ficaram fora com criterio de
entrada registrado.

Nao registrado na memoria: esta sessao nao expoe a ferramenta de memoria,
entao `/areas/projeto-aquametria.md` NAO foi atualizado. Copiar esta entrada
para la (e o estado novo em `ESTADO.md`).

Proximo passo desbloqueado: **Bloco 3 — modelo do banco de produtos**. A
especificacao ja lista, calculadora por calculadora, os campos exigidos de
`filtro`, `aquecedor`, `iluminacao` e `midia`, e a secao 12 traz as 8 coletas
abertas em ordem de prioridade (a primeira e o coeficiente U do vidro, que
libera a C5 fisica e a C6).

## 2026-09-07 (2o disparo) — BLOCO 3 entregue: modelo do banco de produtos

Sessao SEM ferramenta de memoria (estado lido de `ESTADO.md`). Sem Application
Password, o site nao foi tocado: trabalho 100 % no repositorio. `WebSearch`
funciona; `WebFetch` continua bloqueado por dominio (`sicce.com` devolveu
`EGRESS_BLOCKED` hoje, como `seachem.com` no disparo anterior).

Primeiro, o pendente: o Bloco 2 estava na branch `claude/lucid-carson-w52jma`,
fora do `main`. Foi levado ao `main` por push direto (fast-forward
3399f1b..bbc52c1) e o PR #2 fechou como merged. Nao ha mais trabalho fora do
`main` de execucoes anteriores.

Entregue:
- `dados/modelo-banco-produtos.md` — o modelo: 6 principios, identidade do
  produto, campos comuns, as 4 entidades campo a campo (tipo, unidade,
  obrigatoriedade, origem esperada), a escada de 6 niveis de fonte, o
  tratamento de conflito, preco como serie temporal, as 14 regras, os 6
  achados da semente, as limitacoes conhecidas do esquema v1 e a fila de
  coletas.
- `dados/esquema-produtos.json` — o contrato formal (campos, vocabularios,
  derivados, `minimo_para_sugerir` por calculadora, regras V1 a V14).
- `dados/produtos-filtro.json` (5), `produtos-aquecedor.json` (4),
  `produtos-iluminacao.json` (4), `produtos-midia.json` (2) — 15 registros de
  semente, cada campo amarrado a uma entrada de `fontes[]` com url e data.
- `dados/produtos-cotacoes.json` — modelado e VAZIO de proposito.
- `ferramentas/validar-produtos.py` — as regras rodando de verdade. Primeira
  execucao apontou 12 erros nas proprias sementes (campo sem fonte, voltagem
  gravada sem origem, status incoerente); todos corrigidos. Estado final:
  15 produtos, 0 erros, 3 avisos.
- `manifest.json` revisao 2 (7 itens novos em `dados`, todos `publicar: false`
  e com sha256; o esquema de `dados` ganhou as entidades `cotacao` e `esquema`,
  e o manifest ganhou a lista `ferramentas`). `README.md` da ilha documenta a
  pasta `ferramentas/` e o comando de validacao.

Decisoes de modelo que o dado real forcou:
1. **Variante e registro proprio.** Atman AT-3338 x AT-3338S: uma letra muda
   vazao (1200/1500 L/h), potencia (35/18 W), coluna (1,8/1,5 m) e volume
   (ate 450 / 150 a 400 L).
2. **Procedencia por campo, nao por registro** — cada `fontes[]` declara quais
   campos sustenta; o validador reprova campo preenchido sem fonte (V2).
3. **Preco sai do produto** e vira serie temporal com loja e data. Nenhum dos
   precos vistos hoje entrou: sem data de leitura seriam numero inventado.
4. **Voltagem vira requisito de sugestao** (C3, C5, C15), nao da ficha.
5. **Comprimento da luminaria nao e comprimento do aquario** (SunSun ADE-400c:
   peca de 41 cm para aquario de 48 a 65 cm). Ficou pendencia de criterio: a
   C15 so sugere por comprimento de peca depois que a convencao de cobertura
   virar constante `convencao-editorial`.
6. **`posicao_no_fluxo` e o unico campo de origem editorial** do banco e por
   isso nao exige fonte de terceiro.

Achados da semente (todos com fonte nos registros):
- Turnover implicito DECLARADO pelos proprios fabricantes: Eheim 2213 1,76 x/h,
  Atman AT-3338 2,67, SunSun HW-303B 4,00, Seachem Tidal 55 5,00, Atman
  AT-3338S 3,75 a 10,0. Os fabricantes divergem ENTRE SI por 5,7 vezes, alem de
  divergirem das regras de bolso brasileiras. Material pronto para a C3.
- Eficiencia de filtro: 34,3 a 166,7 L/h por W — 4,9x entre modelos que
  "servem" ao mesmo aquario. Base da comparacao de conta de luz da C7.
- A linha Roxin nao segue regra propria: 0,67, 1,0 e 0,86 W/L nos tres
  tamanhos, com um vao sem modelo declarado entre 200 e 250 L.
- Voltagem e o gargalo: 9 dos 13 equipamentos eletricos nao a declaram em
  nenhuma fonte. Hoje a C5 e a C15 sugeririam ZERO produtos, e a C3, dois.
- Iluminacao: 3 das 4 luminarias declaram lumen (83 a 106 lm/W, plausiveis) —
  melhor do que o Bloco 1 previa; o que falta e voltagem, comprimento e ate
  marca (uma e vendida com o nome da loja).
- Midia: 700 (Seachem Matrix) contra 450 m2/L (Eheim SUBSTRAT pro), nenhum dos
  dois publicando o metodo de medicao. A C12 cita os dois e nao ranqueia.

Nao registrado na memoria: esta sessao nao expoe a ferramenta de memoria,
entao `/areas/projeto-aquametria.md` NAO foi atualizado. Copiar esta entrada
para la (e o estado novo em `ESTADO.md`).

Proximo passo desbloqueado: **Bloco 4 — rascunhos dos artigos-ancora** (12 a 15
textos que sustentam as calculadoras; cada tabela tecnica cita o manual do
fabricante e leva data de verificacao). A tabela de turnover implicito por
fabricante e a serie W/L da Roxin ja sao dois artigos com dado proprio.
Coletas baratas que podem ser feitas junto: voltagem dos 9 equipamentos,
`coluna_maxima_m` do HW-303B e do Tidal 55, `volume_filtragem_L` dos canisters
e a `faixa_ajuste_C` da Roxin na embalagem.

## 2026-09-07 (3o disparo, extra) — BLOCO 3b entregue: CASCA DO SITE, e o desembarque virou automatico

Sessao SEM ferramenta de memoria (estado lido de `ESTADO.md`). Disparo manual
pedido pelo Raphael as 11h52 BRT: rodar o 3b hoje, com `publicar: true`.

Pendencias de execucoes anteriores: NENHUMA. O `main` ja estava em `44ec496`
(Bloco 3), e as branches `claude/lucid-carson-w52jma` e `-sbd8tp` nao tinham
commit fora do `main`. A branch desta sessao nasceu de `origin/main`.

Entregue:
- `snippets/aquametria-casca.php` (616 linhas) — nome no Code Snippets
  "Aquametria Casca — identidade e estrutura do site", escopo global, ativo.
  Faz as seis coisas do briefing, sozinho, sem tema filho e sem construtor:
  (a) carrega Chivo, IBM Plex Sans e IBM Plex Mono do Google Fonts e injeta a
      paleta no `wp_head` (prioridade 20, depois do tema): papel de fundo,
      tinta no texto, lamina em link e botao, Chivo nos titulos, Plex Mono em
      numero e unidade. Alem das regras proprias, redefine as variaveis de
      preset do tema de blocos (`--wp--preset--color--base/contrast/primary/
      secondary` e as duas de fonte), que e o que realmente recolore um tema
      de blocos sem editar o tema;
  (b) `render_block` troca `core/site-title` e `core/site-logo` pelo logotipo
      inline em SVG — recipiente graduado, linha de enchimento em lamina,
      marcacoes escuras acima da agua e claras abaixo, sem peixe, sem bolha,
      sem mascote — seguido do wordmark "Aquametria" em Chivo 900. Trava
      estatica: se o tema imprimir os dois blocos, o segundo sai vazio em vez
      de duplicar a marca;
  (c) `render_block` troca `core/navigation` pelo menu proprio
      Calculadoras · Metodologia · Sobre;
  (d) cria, casando pelo slug, `inicio`, `calculadoras`, `metodologia` e
      `sobre`, e fixa `show_on_front=page` com `page_on_front=inicio`;
  (e) manda "Hello world!" e "Sample Page" para a LIXEIRA (`wp_trash_post`,
      nunca apagar), casando por slug E por titulo, nas duas linguas (o site e
      pt-BR, entao `ola-mundo` e `pagina-exemplo` tambem entram na lista), com
      guarda para nunca mandar a pagina inicial para a lixeira;
  (f) rodape proprio no `wp_footer` com a tagline "Calculadoras e dados
      tecnicos para dimensionar o seu aquario" e a nota de fontes.
- O texto das quatro paginas NAO ficou no banco do WordPress: cada pagina
  nasce com um shortcode (`[aquametria_home]`, `[aquametria_calculadoras]`,
  `[aquametria_metodologia]`, `[aquametria_sobre]`) e o conteudo mora no
  proprio snippet. Consequencia pratica: atualizar o snippet atualiza as
  paginas, e o conteudo continua versionado no repositorio, como manda a regra
  de ouro. A home explica o site em tres linhas e lista as 8 calculadoras.
- A pagina `metodologia` publica o quadro dos 8 status de constante com a
  contagem (42 constantes: 24 divergente-fontes-br, 8 pendente, 3
  fabricante-via-busca, 3 transcrita-varejo, 1 fisica, 1 verificada-fabricante,
  1 norma-via-secundaria, 1 convencao-editorial) e a lista dos 7 numeros que a
  Aquametria se recusa a publicar, com o motivo de cada um. Se um dia o banco
  de constantes for publicado como `dados`, a pagina conta ao vivo pela option
  `aquametria_dados_constantes-calculadoras` em vez do instantaneo.
- `manifest.json` revisao 3: o snippet entra com **`publicar: true`** e sha256
  `20e197fc…`, e **`desembarque.aprovado` virou `true`**, com a data e a
  observacao da decisao (so conteudo programatico em escala continua preso).
- `README.md` da ilha, `snippets/README.md` e `conteudo/README.md` atualizados:
  a nova regra de desembarque e a obrigacao de toda calculadora publicada
  aparecer no hub.

Verificacao feita antes de marcar `publicar: true`:
- `php -l` de verdade (PHP 8.4): sem erro de sintaxe.
- Teste de fumaca com o WordPress simulado por stubs: os 4 shortcodes rendem
  (4053, 3442, 5249 e 1987 bytes), `wp_head` sai com 5292 bytes, `wp_footer`
  com 658, `render_block` troca os tres blocos e devolve `core/paragraph`
  intacto, a estrutura cria 4 paginas com 1 unico `flush_rewrite_rules`, manda
  os dois posts padrao para a lixeira e nao toca no rascunho de politica de
  privacidade. **Segunda passada: 0 insercoes** — idempotencia confirmada.
- Render visual em Chromium (Playwright), 1100 px e retina: cabecalho, home,
  cards, metodologia e rodape conferidos; o logotipo le como recipiente
  graduado no tamanho real de cabecalho.

Duas decisoes que valem para os proximos blocos:
1. **O hub e obrigatorio.** A lista das 8 calculadoras vive em
   `aquametria_casca_calculadoras()` com `estado` em `em-construcao` ou
   `publicada`, e passa pelo filtro `aquametria_calculadoras`. Publicar a C1
   sem virar o estado dela na casca deixa a calculadora orfa: o bloco 4 tem
   que mexer nos dois arquivos.
2. **Conteudo institucional mora em shortcode do snippet**, nao em Markdown de
   `conteudo/`. `conteudo/` continua sendo o lugar dos artigos-ancora e das
   paginas de calculadora, que sao texto longo com fonte citada.

Nao registrado na memoria: esta sessao nao expoe a ferramenta de memoria,
entao `/areas/projeto-aquametria.md` NAO foi atualizado. Copiar esta entrada
para la (e o estado novo em `ESTADO.md`).

Proximo passo desbloqueado: **Bloco 4 — C1, a calculadora de litragem**, que e
o nucleo e o estado compartilhado (`localStorage`, chave `aquametria.aquario`).
Ao publica-la, virar o `estado` da C1 para `publicada` na casca e bumpar
`AQUAMETRIA_CASCA_VERSAO`.

### Desembarque desta execucao (07/09/2026, ~15h20 BRT)

Push direto em `main` funcionou (`44ec496..c9e8999`), sem PR. Cinco minutos
depois, `raw.githubusercontent.com` ja servia a revisao 3 com
`aquametria-casca` em `publicar: true` (conferido por WebFetch).

**Sync NAO acionado pela nuvem:** o WebFetch em
`aquametria.com.br/?aquametria_sync=...&forcar=1` voltou `EGRESS_BLOCKED`,
como o ESTADO.md ja previa para o dominio do site. O WP-Cron do proprio site
aplica sozinho em ate 30 minutos, sem intervencao. Nada a fazer alem de
esperar.

URLs para o Raphael conferir depois que o WP-Cron rodar:
- `https://aquametria.com.br/` — home: logotipo, menu, as tres linhas e os 8 cards
- `https://aquametria.com.br/calculadoras/` — hub
- `https://aquametria.com.br/metodologia/` — quadro de status e as 7 recusas
- `https://aquametria.com.br/sobre/`
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — log do Sync (deve
  mostrar `snippets/aquametria-casca: ok` e `revisao 3`)

"Hello world!" e "Sample Page" vao para a LIXEIRA, nao para o apagador: se
alguma coisa der errado, e so restaurar. Se a estrutura precisar ser refeita a
mao, um administrador logado abre `https://aquametria.com.br/?aquametria_casca=refazer`.

---

## 2026-09-07 (4o disparo, correcao) — Sync v1.1.0 e casca v1.0.1

**Nao e bloco novo.** Disparo extra de correcao urgente: o site puxou a revisao
3 e caiu com "Ha um erro critico no seu site". O bloco 4 (C1, litragem)
continua sendo o proximo passo e NAO foi executado aqui.

### Diagnostico (feito fora desta sessao, confirmado no site)
A causa foi o proprio `snippets/aquametria-sync.php` (v1.0.0), que falava a API
antiga do Code Snippets. Na versao instalada (3.10.2):

1. a classe do modelo e `Code_Snippets\Model\Snippet` — `new \Code_Snippets\Snippet()` e fatal;
2. `\Code_Snippets\save_snippet()` devolve o OBJETO Snippet, nao o id — `$id = save_snippet(...)` vira 0/erro;
3. `save_snippet()` de um snippet marcado ativo roda `test_snippet_code()`, que da `eval` no codigo na mesma requisicao;
4. o validador (`Code_Snippets\Utils\Validator`) recusa com "Cannot redeclare function X" quando o snippet ja esta carregado naquela requisicao.

Consequencia que vale para SEMPRE (ja escrita na fase 4b do `ESTADO.md`):
**toda funcao de nivel superior de qualquer snippet da ilha precisa estar dentro
de `if ( ! function_exists( 'nome' ) ) { ... }`** — sem isso, atualizar um
snippet ativo falha ou o deixa inativo em silencio. Vale para a casca e para
todas as calculadoras futuras.

### O que foi entregue

**`snippets/aquametria-sync.php` → v1.1.0** (edicoes cirurgicas, arquivo nao reescrito):
- cabecalho e `AQUAMETRIA_SYNC_VERSAO` em `1.1.0`;
- `aquametria_sync_aplicar_snippet()` detecta a classe do modelo com
  `class_exists()` (`Model\Snippet`, com queda para a antiga) e instancia
  `new $classe()`; se nenhuma existir, devolve erro em vez de fatal;
- grava **inativo** e so entao chama `activate_snippet()`, porque gravar ativo
  faz o plugin dar `eval` no codigo na mesma requisicao; le o retorno como
  objeto (`$ret->id`) com queda para inteiro; releu e confere `active` depois
  de ativar, e **relata** ("gravado (#id) mas NAO ativado: ...") em vez de
  fingir sucesso;
- `aquametria_sync_executar()` envolve o despacho dos tres aplicadores em
  `try/catch ( \Throwable )` — um item quebrado vira linha de log, nao derruba
  o sync inteiro.

**`ferramentas/proteger-funcoes.php`** (nova; ferramenta de bancada, **nao entra
no manifest**): le um snippet e envolve cada funcao de nivel superior em
`if ( ! function_exists( ... ) )`, pulando closures. Uso:
`php ferramentas/proteger-funcoes.php entrada.php saida.php`.

> Ponto em aberto para a proxima execucao: a instrucao deste disparo foi
> explicita — "NAO vai para o manifest" — e foi seguida a risca. Mas o manifest
> tem uma lista `ferramentas` (que o Sync **nao** consome; ele so le `snippets`,
> `conteudo` e `dados`) onde a ferramenta irma `validar-produtos.py` esta
> registrada. Registrar `proteger-funcoes.php` la seria inofensivo e mais
> consistente; fica para o Raphael decidir.

Rodada nos dois snippets: **10 funcoes protegidas no sync** e **14 na casca**,
exatamente o esperado. Conferido que, fora os involucros, nenhuma linha de
codigo mudou. A casca virou **v1.0.1** (so a protecao das funcoes; nenhuma
mudanca de comportamento).

### Verificacao
- `php -l` **de verdade** (com `<?php` prefixado antes de lintar, porque o
  arquivo comeca em `/**` e o lint passaria trivialmente sem isso) nos dois
  snippets: limpo.
- `sha256` recalculado do arquivo final commitado, nao herdado.

| arquivo | sha256 |
| --- | --- |
| `snippets/aquametria-sync.php` | `b72a007c022f60127a36dff34cfbfb552a8b2ba7086041901b8f567b3856e931` |
| `snippets/aquametria-casca.php` | `387e16d5abe5775311eeafec5fc5bcb65567f87c2eea3291e43df4d9655e7980` |

### Manifest
`revisao` = **4**, `atualizado_em` = `2026-09-07`. `aquametria-casca` continua
`publicar: true`. **`aquametria-sync` passou a `publicar: true`** (mantendo
`ativo: true`): a partir da v1.1.0 o Sync pode se atualizar sozinho, e como ele
se pula pelo nome (`AQUAMETRIA_SYNC_NOME_PROPRIO`), isso e inofensivo e deixa o
arquivo rastreado. A `descricao` dele, que ainda dizia "publicar=false e so
registro de procedencia", foi corrigida.

### Sync do site
**Nao acionado nesta execucao, de proposito** — quem aciona e o Cowork, que ja
esta com o navegador aberto. O container da nuvem tambem nao alcanca o dominio
(`EGRESS_BLOCKED`).

Proximo passo desbloqueado (inalterado): **Bloco 4 — C1, a calculadora de
litragem**, o nucleo e o estado compartilhado (`localStorage`, chave
`aquametria.aquario`). Ao publica-la, virar o `estado` da C1 para `publicada`
na casca e bumpar `AQUAMETRIA_CASCA_VERSAO`.

Sem ferramenta de memoria nesta sessao: `/areas/projeto-aquametria.md` NAO foi
atualizado; esta entrada e o `ESTADO.md` sao o registro.

## 2026-09-07 (5o disparo, correcao visual) — rodape duplicado

Nao foi bloco novo: disparo extra para corrigir o que o Raphael viu no site
depois de a casca entrar no ar (revisao 4 aplicada as 16h36). **Ficaram dois
rodapes empilhados**: primeiro o do tema Twenty Twenty-Five, com o credito
"Twenty Twenty-Five · Criado com WordPress", e logo abaixo o rodape escuro da
Aquametria.

### Causa
`aquametria-casca.php` v1.0.1 imprimia o rodape proprio no hook `wp_footer`
(prioridade 20) e nao removia o do tema. Em tema de blocos o rodape e a
template part `footer` (`core/template-part` com `attrs['slug'] === 'footer'`),
renderizada DENTRO do fluxo do conteudo — por isso ela sai acima de qualquer
coisa impressa em `wp_footer`.

### Correcao — casca v1.0.2
- O rodape virou funcao: `aquametria_casca_rodape_html()` (protegida com
  `function_exists`, como todas as outras), acompanhada de
  `aquametria_casca_rodape_impresso()`, que guarda em `static` se o rodape ja
  saiu nesta requisicao.
- **Caminho principal:** o filtro `render_block` que ja existia passou a tratar
  `core/template-part` com slug `footer` (ou `rodape`) e devolve
  `aquametria_casca_rodape_html()` no lugar do rodape do tema — substituicao,
  nao empilhamento.
- O `add_action( 'wp_footer', ... )` que imprimia o rodape foi trocado por uma
  **rede de seguranca**: so imprime se `aquametria_casca_rodape_impresso()` for
  falso (tema sem template part de rodape, ou filtro que nao pegou).
- **Cinto de seguranca em CSS**, para o caso de o filtro nao pegar:
  `.wp-site-blocks > footer.wp-block-template-part .wp-block-group:has(a[href*="wordpress.org"]){display:none;}`
  esconde o credito do WordPress, e
  `body:has(.aqm-rodape) .wp-site-blocks > footer.wp-block-template-part:not(:has(.aqm-rodape)){display:none;}`
  esconde a template part de rodape que nao seja a nossa, quando a nossa ja
  esta na pagina.
- **Residuo extra corrigido na mesma passada:** `core/site-tagline` agora e
  substituido por vazio no `render_block` — era por onde a tagline padrao do
  WordPress ("Just another WordPress site") podia aparecer. Nao ha titulo
  duplicado nem menu do tema sobrando: `core/site-title`, `core/site-logo` e
  `core/navigation` ja eram substituidos desde a v1.0.0, e as quatro paginas
  institucionais nao imprimem `<h1>` proprio (o titulo vem do tema).

O rodape da Aquametria continua com a tagline, o paragrafo de procedencia e a
linha "Metodologia · Sobre · Aquametria 2026". Nenhum credito de tema.
`AQUAMETRIA_CASCA_VERSAO` foi de `1.0.0` (a constante estava atrasada em relacao
ao cabecalho) para `1.0.2`, o que faz a casca remontar a estrutura uma vez —
idempotente, sem duplicar nada.

### Verificacao
- `ferramentas/proteger-funcoes.php` rodado no arquivo final: saida IDENTICA ao
  arquivo (nenhuma funcao desprotegida), 16 funcoes conferidas uma a uma.
- `php -l` de verdade (com `<?php` prefixado, porque o arquivo comeca em `/**`):
  limpo.
- `sha256` recalculado do arquivo final commitado:
  `f8f3d1a06e325b458ff48ec01079e099bf2049e435ba9c27bbeb791a7e896479`.

### Manifest
`revisao` = **5**, `atualizado_em` = `2026-09-07`, `aquametria-casca` continua
`publicar: true` e `ativo: true`; a `descricao` passou a dizer que a casca
substitui o rodape do tema.

Sync **nao acionado** por esta sessao, conforme a instrucao do disparo — quem
aciona e o Cowork.

Proximo passo desbloqueado (inalterado): **Bloco 4 — C1, a calculadora de
litragem**, o nucleo e o estado compartilhado (`localStorage`, chave
`aquametria.aquario`). Ao publica-la, virar o `estado` da C1 para `publicada` na
casca e bumpar `AQUAMETRIA_CASCA_VERSAO`.

Sem ferramenta de memoria nesta sessao: `/areas/projeto-aquametria.md` NAO foi
atualizado; esta entrada e o `ESTADO.md` sao o registro.

## 2026-09-07 (6º disparo, tarefa extraordinária) — links de afiliado da Shopee no banco

Não foi bloco novo da fila: tarefa extraordinária pedida no disparo, que desbloqueia
a monetização. Os links foram gerados pelo Raphael no painel Shopee Afiliados em
07/09/2026, com `Sub_id 1 = aquametria` e `Sub_id 2` = o código da calculadora.

### O que entrou no banco

Campo novo `afiliado` em **todos os 16 produtos** — 10 com link, 6 com o motivo de
não terem. Ele fica logo antes de `fontes[]` em cada registro:

| Calculadora | Produtos com link |
|---|---|
| C3 filtro | Eheim classic 250 (2213), Seachem Tidal 55 |
| C5 aquecedor | Roxin HT-1300 Q3 100 W (anúncio 127 V), 200 W (110 V), 300 W (220 V) |
| C12 mídia | Seachem Matrix 1 L, Eheim SUBSTRAT pro 1 L |
| C15 iluminação | Ista I-401 45 cm, Chihiros WRGB II Pro 60, SunSun ADE-400c |

**Sem anúncio do produto na Shopee em 07/09/2026** (só peças de reposição e
lâmpadas UV), gravados com `"plataforma": null` e o motivo: SunSun HW-303B,
Atman AT-3338, Atman AT-3338S e Eheim Jäger 200 W. Enquanto não houver link, eles
não entram no bloco de produto de nenhuma calculadora.

### Três decisões que mudaram o pedido

1. **Preço não foi para o arquivo de produto.** O pedido dizia guardar
   `preco_referencia` no produto; o esquema do Bloco 3 proíbe (regra V7: nenhum
   campo de preço dentro de `produtos-*.json`, porque preço é série temporal e
   apodrece em semanas), e o validador reprovaria. Os 10 valores viraram **10
   cotações datadas** em `dados/produtos-cotacoes.json`, cada uma com loja, data,
   condição, disponibilidade, voltagem do anúncio, título do anúncio, comissão
   quando informada e o campo `origem_leitura`, que diz que a leitura foi do
   painel pelo operador — não da página pela Aquametria (o egresso da nuvem barra
   `shopee.com.br`). É a mesma informação, no lugar onde ela pode ser auditada.
2. **O link da Ista não foi colado no registro que existia.** O anúncio é da
   luminária de **45 cm** (7,6 W, 810 lm); o registro do banco era a de **60 cm**
   (35 W, 3717 lm). São produtos diferentes: colar o link ali faria a C15 prometer
   3717 lm e entregar 810. Entrou o registro `ista-i-401-45`, com ficha própria
   (Aquarius Hobby, nível varejo, lida por busca porque o domínio dá
   EGRESS_BLOCKED), e o de 60 cm ficou sem link, com o motivo escrito.
3. **O LED genérico "Newpet Slim 30–60 cm" não virou produto.** É outro produto,
   de outro revendedor, e a busca de 07/09 não achou ficha com potência e lúmen
   de fabricante ou varejo especializado — só anúncio de marketplace, que pelo
   esquema (nível 6) não sustenta número técnico. O link ficou em
   `dados/afiliados-sem-produto.json`, com o que o desbloqueia. Link sem
   especificação verificada não pode ser sugerido por calculadora.

### Troca de registro na iluminação

`aquario-projetado-x1-fr-60w` **saiu** do banco (pedido do disparo: não tem anúncio
real na Shopee). Entrou no lugar `chihiros-wrgb-ii-pro-60`, com as specs refeitas
por duas fontes de varejo especializado que concordam entre si — Green Aqua
(74 W, 6630 lm, aquários de 60 a 80 cm, 60 LEDs WRGB, IP43, controle por app
Bluetooth) e Aquasabi (600 × 140 × 18 mm) — ambas lidas por resultado de busca,
porque `chihiros.eu` devolveu EGRESS_BLOCKED. O PAR de 50–60 citado pelo varejo
vem "no substrato", sem distância em cm: sem distância o PPFD é inútil e a regra
V5 o rejeita, então não foi gravado. A voltagem não é declarada por nenhuma das
fontes — e voltagem é requisito para SUGERIR — então ele entra como ficha, não
como sugestão.

O registro removido, transcrito para o caso de voltar (também está no histórico do
git, commit `08d84dc`):

```json
{
  "id": "aquario-projetado-x1-fr-60w", "entidade": "iluminacao",
  "marca": null, "linha": "X1-FR", "modelo": "X1-FR 60 W Wi-Fi", "variante": "60 W",
  "nomes_alternativos": ["Luminaria X1-FR 60W 5000 lumens"],
  "gtin": null, "disponibilidade_br": "vendido", "voltagem": null,
  "tipo": "led-pendente", "potencia_w": 60, "fluxo_lm": 5000,
  "temperatura_cor_k": null, "espectro": null,
  "ppfd_declarado": null, "ppfd_distancia_cm": null,
  "comprimento_luminaria_cm": null, "comprimento_aquario_cm": null,
  "regulagem": "app", "volume_atendido_declarado_L": null,
  "fontes": [{ "origem": "varejo", "status": "transcrita-varejo",
    "referencia": "Aquario Projetado (varejo BR especializado), ficha da luminaria X1-FR 60 W com 5000 lumens e controle Wi-Fi",
    "url": "https://www.aquarioprojetado.com/luminaria-x1-fr-60w-5000-lumens-wi-fi-luminaria-para-aquario-plantado",
    "verificado_em": "2026-09-07",
    "campos": ["potencia_w", "fluxo_lm", "regulagem", "tipo"],
    "observacao": "Ficha de varejo. Confira a embalagem." }],
  "conflitos": [], "verificado_em": "2026-09-07", "status_registro": "parcial",
  "observacao": "Tem lumen, nao tem comprimento: cai na validacao V13 e nao pode ser sugerido. 83 lm/W."
}
```

### Regra nova: V15, e o relatório que ela abriu

O esquema virou **v2**: o campo `afiliado` está documentado (`plataforma`, `url`,
`sub_id_1`, `sub_id_2`, `rel`, `verificado_em`, `anuncio_shopee`,
`voltagem_anuncio`, `motivo`), com as regras de renderização (`rel="sponsored"`,
`target="_blank" rel="noopener"`, aviso visível de comissão, preço sempre com data)
e a proibição de link apontando para outra variante. `ferramentas/validar-produtos.py`
ganhou a regra **V15**: todo produto tem `afiliado`; com plataforma preenchida
exige URL https, os dois `sub_id`, o título do anúncio e `rel: "sponsored"`, e
proíbe qualquer campo de preço lá dentro; com plataforma `null` exige o motivo.

O relatório do validador passou a separar, por calculadora, **apto com link** de
**apto sem link**. O que ele mostra hoje é o trabalho que sobra:

```
c12-midia-filtrante    3 com link, 0 apto(s) sem link, 4 barrado(s)
c15-iluminacao         1 com link, 0 apto(s) sem link, 4 barrado(s)
c3-vazao-filtro        0 com link, 2 apto(s) sem link, 3 barrado(s)
c5-aquecedor-delta     0 com link, 0 apto(s) sem link, 4 barrado(s)
c7-consumo-custo       7 com link, 6 apto(s) sem link, 1 barrado(s)
16 produtos, 10 cotacoes, 0 erro(s), 2 aviso(s)
```

**Ter link não basta.** A C15 hoje só consegue sugerir UM produto (a Ista de
45 cm) e a C5, ZERO. A C5 continua em zero porque os três Roxin
não declaram `faixa_ajuste_C` nem voltagem — e voltagem de anúncio não conta, que
é exatamente por que ela foi para `voltagem_anuncio` e não para o campo `voltagem`:
anúncio de marketplace é nível 6 e não sustenta número técnico. A C3 tem dois
produtos aptos (Atman) que não têm link, e dois com link (Eheim 2213, Tidal 55)
barrados por voltagem e coluna máxima. **A coleta que destrava dinheiro agora é
voltagem e `faixa_ajuste_C` de fabricante, não mais link.**

### Verificação
- `python3 ferramentas/validar-produtos.py`: **16 produtos, 10 cotações, 0 erros,
  2 avisos** (os dois avisos são antigos: eficiência implausível do Tidal 55 e
  faixa de 13,3× do Eheim Jäger).
- Todo JSON reaberto com `json.load` depois de gravado.
- `sha256` de todos os arquivos alterados recalculado do arquivo final commitado.

### Manifest
`revisao` = **6**, `atualizado_em` = `2026-09-07`. Hashes atualizados de
`produtos-filtro`, `produtos-aquecedor`, `produtos-iluminacao`, `produtos-midia`,
`produtos-cotacoes` (agora 10 registros), `esquema-produtos` e
`modelo-banco-produtos`; entrada nova `afiliados-sem-produto`. Tudo continua
`publicar: false` — é dado interno, não vai para o site sozinho.

Próximo passo desbloqueado (inalterado): **Bloco 4 — C1, a calculadora de
litragem**, o núcleo e o estado compartilhado (`localStorage`, chave
`aquametria.aquario`). Ao publicá-la, virar o `estado` da C1 para `publicada` na
casca e bumpar `AQUAMETRIA_CASCA_VERSAO`. A C1 não tem bloco de produto (litragem
não vende equipamento); o primeiro bloco de produto com link será o da C3.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-07 (6º disparo, bloco do dia) — BLOCO 4 começa: C1, a calculadora de litragem

Primeira calculadora no ar. Snippet, página e itens de manifest com `publicar: true`.

### O que foi entregue
- `snippets/aquametria-calculadora-litragem.php` — snippet **Aquametria
  Calculadora de Litragem**, escopo front-end, v1.0.0, shortcode
  `[aquametria_calculadora_litragem]`.
- `conteudo/calculadora-de-litragem.md` — a página, com front matter, o
  shortcode no corpo e a explicação metodológica.
- `manifest.json` revisão **7**, os dois itens com `publicar: true` e sha256
  conferido do arquivo final.

### Decisões que a construção fixou (valem para C3, C5, C12, C15…)

1. **Todo o cálculo é JavaScript no navegador.** O site está atrás do cache de
   página da hospedagem: HTML que dependesse da query string seria servido
   errado para o visitante seguinte. Como consequência, a página é estática e o
   permalink é lido e escrito pelo próprio JS (`history.replaceState`).
2. **A calculadora se anuncia no hub, em vez de a casca listá-la.** O snippet
   registra `add_filter( 'aquametria_calculadoras', ... )` e vira o `estado` da
   C1 para `publicada`. Ganho: nenhuma edição da casca, nenhum bump de
   `AQUAMETRIA_CASCA_VERSAO`, e desativar o snippet devolve o cartão para "em
   construção" sozinho. **É este o caminho para as próximas** — a casca já
   previa o filtro, ninguém tinha usado.
3. **A chave do estado compartilhado é `aquametria.aquario`** (com ponto), como
   manda a tarefa. A especificação do Bloco 2 dizia `aquametria_aquario`; ela
   foi corrigida para a chave publicada, que é a que vale.
4. **Vírgula decimal é entrada válida.** Ninguém digita "80.5" no Brasil. Os
   campos são `text` com `inputmode="decimal"` e a leitura troca vírgula por
   ponto.
5. **Litro sai inteiro a partir de 100 L**, com uma casa abaixo disso. Precisão
   falsa (109,47 L) mente sobre a incerteza de um volume que nem desconta
   substrato.

### O que a página recusa, e diz por quê
Não desconta substrato. `substrato-densidade` (1 a 2 kg/L contra 1 kg ≈ 1 L, 100 %
de diferença) e `substrato-porosidade` (nenhuma fonte publica) estão `pendente`,
e constante pendente é proibida em fórmula. A tela declara a consequência — o
volume real fica **superestimado** — e publica a tabela de direção do erro:
seguro para filtro, aquecedor e mídia; **inseguro** para lotação e dosagem. Fica
registrado o protocolo de medição própria que libera o desconto.

### Dois defeitos do Sync que a primeira página em Markdown expôs (v1.1.1)
- **O front matter era impresso na página.** `aquametria_sync_md()` não o
  descartava; a página teria começado com "titulo:", "slug:", "publicar: true".
  Agora o bloco `---…---` do topo é cortado antes da conversão.
- **O shortcode saía dentro de `<p>`.** `<div>` dentro de `<p>` é HTML inválido:
  o navegador fecha o parágrafo no meio e a página fica remendada. Linha que só
  tem shortcode agora sai como bloco próprio.
- De quebra, **toda tabela vinda de Markdown agora sai dentro de um bloco que
  rola** — uma tabela de três colunas empurrava a página inteira para o lado no
  celular.

### Verificação (o que foi realmente rodado)
- `php -l` de verdade nos dois snippets (com `<?php` prefixado, porque o arquivo
  começa em `/**`): limpo.
- `ferramentas/proteger-funcoes.php` nos dois: saída **idêntica** ao arquivo —
  nenhuma função de nível superior desprotegida.
- **Teste de fumaça em PHP com stubs de WordPress**: o filtro do hub vira só a
  C1 para `publicada` e deixa a C3 em construção; o shortcode devolve 28 KB de
  HTML na primeira chamada e string vazia na segunda (uma instância por página);
  nenhum id duplicado; 26 `<div>` abertas e 26 fechadas; acentos preservados.
- **Teste em navegador de verdade** (Chromium via Playwright), 9 casos: cálculo
  com vidro (80 × 40 × 40, 8 mm → 128 L brutos, 118 L internos, 109 L reais);
  vírgula decimal e desconto de rochas; sem espessura (diz "sem número" e avisa
  que a lâmina saiu superestimada); medidas internas (bruto = interno); erro de
  unidade (800 cm barrado, saída escondida); lâmina maior que a altura interna
  (limitada ao máximo físico, com aviso); caminho inverso (100 L com 80 × 40 →
  31,3 cm de altura, e a água que caberia); permalink reabrindo com as entradas;
  estado retomado do `localStorage` em nova visita. **Zero erro de console.**
- **Conversão do Markdown pelo próprio Sync**: front matter removido, shortcode
  fora do `<p>`, tabela convertida, 6 `<h2>`, 2 links internos.
- **Página final montada (conteúdo + shortcode) em 390 px de largura**: sem
  rolagem horizontal do documento depois da correção da tabela.

### Desembarque
Automático, como decidido em 07/09/2026. Depois do push em `main`, o Sync precisa
ser acionado (WebFetch da nuvem costuma cair no bloqueio de egresso; se cair,
fica para o WP-Cron, que roda a cada 30 minutos). URLs a conferir:
`https://aquametria.com.br/calculadora-de-litragem/` e o hub
`https://aquametria.com.br/calculadoras/`, onde o cartão da C1 deve passar de
"Em construção" para "Abrir calculadora".

Próximo passo desbloqueado: **C3 — vazão do filtro e turnover**, que é a primeira
com bloco de produto (e a primeira a usar os links de afiliado gravados hoje).
Ela lê `aquametria.aquario` do navegador. Atenção ao que o validador já mostra:
dos filtros com link, o Eheim 2213 e o Tidal 55 estão barrados por falta de
voltagem e coluna máxima — sem coletar isso, o bloco de produto da C3 nasce vazio.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como nas execuções anteriores — o container da nuvem não
alcança o site, só o GitHub. O `raw.githubusercontent.com` **já serve a revisão
7** (conferido nesta sessão), então o WP-Cron do próprio site, que roda a cada 30
minutos, aplica sozinho. Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

Depois disso, conferir:
- `https://aquametria.com.br/calculadora-de-litragem/` — a calculadora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C1 deve ter virado
  "Abrir calculadora";
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

---

## 08/09/2026 — Bloco 4: C3, a calculadora de vazão do filtro, no ar (com o primeiro bloco de produto)

**Disparo extra**, autorizado pelo Raphael, pedindo a C1. A C1 já estava no `main`
(commits `0989345` e `4cf5a8f`, execução das 20h47 UTC de 07/09) — a referência
local é que estava velha. Como o bloco pedido estava entregue, esta execução fez
**o próximo passo desbloqueado: a C3**, que é a primeira calculadora com bloco de
produto e a primeira a usar os links de afiliado gravados ontem.

### O problema que precisou ser resolvido antes da calculadora

O validador dizia, no início da sessão: `c3-vazao-filtro — 0 com link`. Os dois
únicos filtros com link de afiliado estavam barrados por campo faltante, e sem
eles o bloco de produto da C3 nasceria vazio. Foi resolvido com **coleta, não com
afrouxamento de regra**:

- **Eheim classic 250 (2213)**: ganhou `voltagem: ["110"]`, com fonte de varejo BR
  (Pró-Aquarista e Bixo da Água anunciam a versão 110 V). Nenhum anúncio brasileiro
  visto declara a versão 220 V, então o campo registra só o que tem fonte — e o
  cartão de produto obriga o aviso de conferir a voltagem no anúncio, porque o
  anúncio de afiliado não a declara.
- **Seachem Tidal 55**: ganhou `voltagem: ["110","220"]` (Biotopos 110 V,
  Amazon.com.br 220 V) e saiu de `revalidar` para `completo`.
- **A correção de modelo que isso revelou**: `coluna_maxima_m` estava marcada como
  obrigatória para todo filtro, mas **hang-on não tem recalque a vencer** — ele fica
  pendurado na borda. Exigir o campo dele era defeito do esquema, não dado faltando.
  Entrou `coluna_maxima_nao_se_aplica`, e a obrigatoriedade virou condicional ao tipo
  (`obrigatorio_se_tipo: [canister, sump]`), legível pelo validador.
- **A regra V10** (eficiência acima de 120 L/h por W é implausível) ficou restrita a
  canister e sump: o Tidal 55 declara 1000 L/h com 6 W — 167 L/h por W — porque
  hang-on trabalha a coluna quase zero. O limite tinha sido calibrado para canister.

Resultado: a C3 passou de 0 para **4 filtros sugeríveis** (Eheim 2213, Tidal 55,
Atman AT-3338 e AT-3338S), 2 deles com link. O SunSun HW-303B segue barrado por
não ter coluna máxima publicada por nenhuma fonte.

### A decisão editorial desta execução (regra V16)

A execução anterior tinha deixado implícito que produto sem link de afiliado não
entra no bloco. Isso é ordenar por comissão pelo caminho inverso, e contraria a
regra do projeto ("a ordem é por adequação técnica ao resultado, jamais por
comissão"). Ficou escrito como regra de validação:

> **V16.** Link de afiliado NÃO entra em critério de sugestão. A lista de produtos
> de uma calculadora é montada e ordenada só por adequação técnica ao resultado;
> produto tecnicamente apto é mostrado tenha ou não link, e quem tem link ganha o
> botão de loja, marcado como patrocinado.

Na prática: os dois Atman aparecem na lista, no lugar que a adequação técnica manda,
com a frase "ainda não temos link de loja para este modelo".

### O que foi entregue

**`snippets/aquametria-calculadora-vazao.php`** (novo, v1.0.0) — shortcode
`[aquametria_calculadora_vazao]`. Lê o volume real que a C1 guardou em
`localStorage`, devolve a faixa em L/h com o critério e a fonte de cada extremo,
os cartões por banda (piso do fabricante · leitura conservadora BR · regra de bolso
BR, ou plantado), o volume mínimo do sump quando marcado, o caminho inverso, o
veredito do filtro que a pessoa já tem, o quadro de fontes e o permalink citável.
Anuncia-se sozinho no hub pelo filtro `aquametria_calculadoras`.

**O bloco de produto**, que é a novidade estrutural: nasce dentro da resposta, como
consequência do cálculo. Cada cartão mostra a placa da marca com a vazão, **o
turnover que aquele filtro entrega naquele aquário** (não no volume genérico do
catálogo), a ficha com a fonte e a data, e o botão da loja com
`rel="sponsored noopener" target="_blank"` quando existe link. O aviso de comissão
é obrigatório e visível dentro do bloco. Sem filtro que atenda a faixa, o bloco
não aparece e a tela diz quantos filtros o banco tem e por que nenhum serviu.
**Preço não entra**: snippet é código que fica meses no ar e preço envelheceria na
tela; a política está escrita na página de divulgação.

**`conteudo/calculadora-de-vazao-do-filtro.md`** — a metodologia: por que a resposta
é faixa e não número, o argumento dos dois lados, o que a calculadora não faz (fator
de perda de carga e turnover marinho, ambos pendentes por falta de fonte), o
protocolo do balde no lugar do fator inventado, a coluna máxima como corte, e as
três regras do bloco de produto.

**`conteudo/divulgacao-de-afiliados.md`** (página nova) — exigida pelo primeiro
bloco de produto e pela autorregulamentação publicitária brasileira. Declara o link
de afiliado, transcreve a V16 na íntegra, mostra a escada de fontes e admite o
tamanho atual do programa.

**Ligações, para nenhuma página nascer órfã:** a casca (v1.0.3) passou a linkar a
divulgação no rodapé de todo o site; a C1 (v1.0.1, snippet e página) passou a
**linkar** a C3, que antes só citava; a C3 aponta de volta para a C1, o hub, a
metodologia e a divulgação. O hub já mostra C1 e C3 como publicadas.

**`ferramentas/gerar-catalogo-filtros.py`** (nova) — o site não lê o repositório em
tempo de execução, então o banco de filtros viaja dentro do PHP. Este gerador
reescreve o trecho entre `CATALOGO-INICIO` e `CATALOGO-FIM` a partir de
`dados/produtos-filtro.json`, aplicando o `minimo_para_sugerir` do esquema. É o que
impede as duas cópias de divergirem.

**Sync v1.1.2** — o conversor de Markdown não entendia citação em bloco e imprimia
o `>` escapado no meio do parágrafo. As duas páginas novas usam citação (a fórmula
do protocolo do balde e a regra V16), então o conversor foi corrigido, com estilo
próprio na casca.

### Verificação (o que foi realmente rodado)
- **`php -l` de verdade** nos quatro snippets (com `<?php` prefixado): limpo.
- **`ferramentas/proteger-funcoes.php`** nos quatro: saída idêntica ao arquivo —
  nenhuma função de nível superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 16 produtos, **0 erro**, 1 aviso conhecido
  (a faixa de 13,3x do Eheim Jager, que é conteúdo da C5, não defeito).
- **Teste de fumaça em PHP com stubs de WordPress**: o hub vira C1 e C3 para
  `publicada` e deixa as outras seis em construção; o shortcode devolve 42 KB na
  primeira chamada e string vazia na segunda; nenhum id duplicado; 21 `<div>`
  abertas e 21 fechadas, 5 `<ul>` e 5 fechadas; acentos preservados; catálogo com
  4 filtros; aviso de comissão e link da divulgação presentes.
- **Teste em navegador de verdade** (Chromium via Playwright), 12 casos: caso base
  (110 L comunitário → 190 a 1.100 L/h, Eheim e Tidal na lista, Eheim entregando
  4,0 x/h); **atributos do link de afiliado** (`sponsored noopener` + `_blank` em
  todos, aviso de comissão visível); perfil plantado mudando o teto para 550 L/h;
  coluna de 1,6 m barrando o Eheim de 1,5 m com o motivo na tela; filtro por tipo;
  **estado vindo da C1** (volume 109,5 preenchido, cálculo automático, e a mescla
  preservando medidas e apelido da C1 enquanto a C3 acrescenta o dela); permalink
  por query string; caminho inverso; **aquário de 15 L sem produto que atenda** (o
  bloco não aparece e a tela explica); sump; erro de unidade escondendo a saída;
  convite para a C1 quando não há estado; 390 px sem rolagem horizontal.
  **Zero erro de console.**
- **Conversão do Markdown pelo próprio Sync** nas três páginas: front matter
  removido, shortcode fora do `<p>`, tabela em bloco que rola, citação em bloco
  correta, 6/5/6 `<h2>`, links internos presentes.
- **sha256 do manifest conferido contra os arquivos finais commitados**: todos batem.

### Desembarque
Automático. Manifest na revisão 8. Depois do push em `main`, o Sync precisa ser
acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-vazao-do-filtro/` — a calculadora nova;
- `https://aquametria.com.br/divulgacao-de-afiliados/` — a página de afiliados;
- `https://aquametria.com.br/calculadoras/` — o cartão da C3 deve ter virado
  "Abrir calculadora";
- `https://aquametria.com.br/calculadora-de-litragem/` — deve ter ganhado o link
  para a C3;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

Próximo passo desbloqueado: **C5 — potência do aquecedor por delta térmico**. Atenção
ao que o validador já mostra: os quatro aquecedores do banco estão barrados
(`voltagem` nos quatro, `faixa_ajuste_C` nos três Roxin, que está em conflito
varejo-contra-varejo). Sem essa coleta, o bloco de produto da C5 nasce vazio — e o
caminho é o mesmo desta execução: coletar com fonte antes de escrever a calculadora.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 8** (conferido nesta
sessão, sem atraso de cache), então o WP-Cron do próprio site, que roda a cada 30
minutos, aplica sozinho. Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

## 2026-09-08 (8º disparo) — BLOCO 4: C5, a potência do aquecedor, no ar com o artigo-âncora pareado

Sessão SEM ferramenta de memória (estado lido de `ESTADO.md` e deste registro).
Sem Application Password, o site não foi tocado: trabalho 100 % no repositório.
Egresso: `WebSearch` funciona; `WebFetch` cai em `EGRESS_BLOCKED` em qualquer
domínio que não seja o GitHub — inclusive Cobasi, tentado hoje. Por isso toda
ficha coletada nesta execução entrou como `transcrita-varejo` ou
`fabricante-via-busca`, com a observação de reconferir.

### O bloqueio real não era a calculadora, era o banco

A execução anterior deixou o aviso: os quatro aquecedores do banco estavam
barrados pelo validador. Faltava `voltagem` nos quatro e `faixa_ajuste_C` nos
três Roxin, esta última em conflito varejo-contra-varejo. Escrever a C5 sem
resolver isso entregaria uma calculadora com bloco de produto sempre vazio.

Então a coleta veio primeiro, e mudou o tamanho do banco:

**Voltagem, o campo que barrava tudo.** As duas linhas são vendidas no Brasil
em 110 V e em 220 V, na mesma potência — Cobasi publica duas fichas do Roxin
HT-1300, uma por tomada; Tudo de Bicho, WorldFish, AquaMaeda, Aquarioz e
Peixinho e Cia repetem; a Pró-Aquarista publica Thermocontrol 100 W 110 V,
250 W 110 V e 300 W 220 V. O campo virou `["110","220"]` nas duas linhas, com a
ressalva escrita na própria fonte: **o que ela sustenta é que EXISTE versão para
as duas tomadas**, não que um anúncio específico seja de uma delas. Daí o cartão
de produto obrigar o aviso de conferir a voltagem, dizendo qual versão o anúncio
que conferimos abria.

**O banco foi de 4 para 9 aquecedores**: Eheim Jäger 50, 100, 150 e 200 W e
Roxin HT-1300/Q3 25, 50, 100, 200 e 300 W. Cobre de 25 a 300 W, que é a faixa
onde mora o aquarismo brasileiro doméstico. O validador saiu de **0 de 4 aptos
para 9 de 9** na `c5-aquecedor-delta` (3 com link de afiliado, 6 sem — e, pela
V16, os seis sem link aparecem do mesmo jeito, só sem botão de loja).

### A regra V17, que é a decisão editorial desta execução

A faixa de ajuste da linha Roxin aparece publicada de dois jeitos no varejo:
22 a 34 °C numas fichas, 16 a 32 °C noutras. As duas são varejo, ou seja, do
mesmo nível. A regra antiga mandava zerar o campo — e zerar o campo tirava das
sugestões o aquecedor mais vendido do Brasil, por excesso de escrúpulo.

Ficou escrita a regra V17 no esquema (versão 3):

> Quando duas fontes do MESMO nível discordam sobre um intervalo, publica-se a
> **interseção** delas: o maior dos mínimos e o menor dos máximos. Não é média
> nem escolha de fonte — é a única faixa que todas as fontes concordam que o
> aparelho cobre. Exige `valor_conservador` e `derivacao` no conflito, e a
> calculadora que usar esse valor **tem de dizer na tela** que a faixa é a
> conservadora e por quê. Interseção vazia continua sendo `campo-vira-null`.

No caso do Roxin: 22 a 32 °C. Na prática, quem quer 30 °C para acará-disco vê o
Roxin na lista; quem quer 33 °C não vê, e lê o motivo; quem quer 20 °C para
kinguio também não vê, porque a faixa conservadora começa em 22 °C. É menos do
que o aparelho talvez faça, e é exatamente tudo o que as fontes sustentam.

Junto veio a **V18**: aquecedor sugerido tem de alcançar a temperatura-alvo
dentro da faixa que o registro sustenta. No bloco de produto da C5, duas
barreiras de segurança vêm ANTES da adequação técnica — a voltagem da tomada e o
termostato chegar ao alvo. O validador aprendeu a conferir a interseção de
verdade (se o `valor_conservador` não for a interseção dos valores em conflito,
é erro) e o `minimo_para_sugerir` aceita a alternativa `conflito:campo`.

### O achado, que virou o artigo

Ao levantar a linha Eheim Jäger inteira para completar a constante
`eheim-jager-linha-comercial`, apareceu o volume declarado potência a potência:

| Modelo | Volume declarado | W/L no teto |
|---|---|---|
| 25 W | 20 a 25 L | 1,00 |
| 50 W | 25 a 50 L | 1,00 |
| 75 W | 50 a 75 L | 1,00 |
| 100 W | 75 a 100 L | 1,00 |
| 125 W | 100 a 125 L | 1,00 |
| 150 W | 125 a 150 L | 1,00 |
| 200 W | 300 a 400 L | 0,50 |

Um vírgula zero, seis vezes seguidas. **O "1 W por litro" que a web brasileira
repete sem citar ninguém não veio de física: veio da prateleira.** O catálogo do
fabricante nomeia cada aparelho pelo volume que dá exatamente 1 W/L, e a regra
de bolso leu a caixa e transformou o rótulo em lei. Isso explica por que fontes
que não se citam repetem o mesmo número.

E a régua quebra em três lugares, todos registrados como conflito no banco:
o 200 W sai da série (0,50 W/L); o catálogo Eheim declara esse mesmo 200 W para
30 a 400 L (treze vezes); e o Jäger de 150 W aparece declarado para 125-150 L
numa ficha e para 200-300 L noutra, as duas de varejo, o dobro de diferença.

De quebra, a constante ficou completa: faltavam as potências de **125 W e
250 W**, que eram justamente os dois dos "9 tamanhos" que a coleta do Bloco 2
não tinha achado.

### O que foi entregue

**`snippets/aquametria-calculadora-aquecedor.php`** (novo, v1.0.0) — shortcode
`[aquametria_calculadora_aquecedor]`. Pede o volume real (herdado da C1) e **a
temperatura mínima do cômodo onde o aquário fica**, que é a entrada que nenhuma
outra calculadora brasileira pede. Devolve a faixa de potência com o nome do
autor em cada extremo e faz uma coisa que nenhuma fonte faz: **separa as regras
que se aplicam ao caso das que não se aplicam, e mostra as duas listas** — saber
qual regra não vale para você é parte da resposta. Traz o degrau da linha
comercial, o confronto com o volume da caixa, o caminho inverso, o quadro de
fontes e o permalink citável. Anuncia-se sozinha no hub pelo filtro
`aquametria_calculadoras`.

**O que ela se recusa a fazer, escrito na página:** não publica a via física
`P = U · A · ΔT` (falta `u-vidro-aquario`, pendente); não corrige por tampa — o
campo existe e muda o TEXTO, nunca o número, porque quantificar a perda pela
lâmina livre é exatamente a constante que falta; não usa mínima por cidade
(`temperatura-minima-por-cidade`, pendente); e **não extrapola a regra de bolso
acima de 10 °C de ΔT**, que é o limite que a única fonte com delta declarado
afirmou — acima disso a tela diz com essas palavras que nenhuma fonte cobre o
caso e entrega a faixa genérica como PISO. Com ΔT ≤ 0 não devolve número nenhum
e explica por quê.

**`conteudo/calculadora-de-potencia-do-aquecedor.md`** — a metodologia: a tabela
das quatro constantes com a condição que cada autor declarou, por que a caixa do
aquecedor não dimensiona, o que a calculadora não faz e por quê, o que é
critério editorial declarado (mirar no degrau que cobre o topo; dois aquecedores
acima de 150 W, que é argumento de modo de falha e não de eficiência) e a
explicação da faixa conservadora.

**`conteudo/quantos-watts-de-aquecedor-para-aquario.md`** — o artigo-âncora
pareado, o primeiro do projeto. Não repete a calculadora: mostra de onde o
"1 W por litro" veio, onde a régua quebra, o caso Belém contra Curitiba (cinco
vezes mais ΔT para a mesma resposta da regra), o que as quatro fontes brasileiras
dizem e não dizem, a fórmula que ainda não podemos publicar e por quê, e seis
recomendações práticas. Linka a calculadora no primeiro terço; a calculadora
linka de volta.

**Correção na C1 (v1.0.2), dívida que a C5 tornaria pior:** `guardar()`
SUBSTITUÍA o estado compartilhado em vez de mesclar — voltar à C1 para corrigir
uma medida zerava a vazão que a C3 tinha calculado e o clima que a C5 tinha
perguntado. Agora mescla, e `recuperar()` aceita estado sem `medidas`, que é
como a C3 e a C5 gravam.

**Sync v1.1.3** — duas coisas. O conversor passou a entender bloco de código
cercado por crases triplas (a fórmula do artigo sairia com as crases impressas).
E passou a converter **link relativo à raiz**: antes só link `https` virava
`<a>`, e link relativo saía com os colchetes no meio do texto — defeito
silencioso, porque não é erro de sintaxe nenhum e só aparece lendo a página no
ar. Foi pego pelo teste de conversão, não por leitura.

**Ligações, para nenhuma página nascer órfã:** a C1 (v1.0.2) e a C3 (v1.0.1)
passaram a LINKAR a C5, no snippet; a C5 aponta de volta para a C1, a C3, o hub,
a metodologia, a divulgação de afiliados e o artigo pareado; o artigo aponta para
as três calculadoras e para a metodologia. O hub já mostra C1, C3 e C5 como
publicadas, sozinho.

**Ferramentas novas:** `gerar-catalogo-aquecedores.py` (mantém sincronizadas as
duas cópias do banco, já que o site não lê o repositório em tempo de execução, e
carrega a faixa conservadora do V17 quando o campo ficou null);
`render-para-teste.php` (monta qualquer shortcode numa página HTML solta com
WordPress falso, carregando todos os snippets menos o Sync — também é teste de
convivência entre calculadoras); `teste-navegador-c5.mjs` (os 15 cenários).

### Verificação (o que foi realmente rodado)
- **`php -l` de verdade** nos cinco snippets (com `<?php` prefixado): limpo.
- **`ferramentas/proteger-funcoes.php`** nos cinco: saída idêntica ao arquivo —
  nenhuma função de nível superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 21 produtos, **0 erro**, 1 aviso
  conhecido (o V11 do Jäger 200 W, que é conteúdo da página, não defeito).
  `c5-aquecedor-delta`: 9 aptos, 0 barrados.
- **Teste de fumaça em PHP com stubs de WordPress**: o hub vira C1, C3 e C5 para
  `publicada`; o shortcode devolve 62 KB na primeira chamada e string vazia na
  segunda; 38 ids, nenhum duplicado; div, ul, form, table, li e p balanceados;
  acentos preservados; catálogo com 9 aquecedores, todos com voltagem e faixa de
  ajuste; aviso de comissão e link da divulgação presentes; nenhuma superglobal
  de servidor.
- **Teste em navegador de verdade** (Chromium via Playwright), 15 casos: caso
  base (110 L, alvo 26 °C, mínima 20 °C → 110 a 165 W, degrau comercial de
  200 W, 3 produtos); **atributos do link de afiliado** (`sponsored noopener` +
  `_blank` + https, aviso de comissão visível, aviso de voltagem em todo cartão
  com link); voltagem 220 V filtrando a lista e avisando que o anúncio conferido
  era de 110 V; **alvo de 33 °C barrando o Roxin pelo teto conservador de 32 °C**
  com o motivo na tela; **alvo de 20 °C barrando pelo piso conservador de 22 °C**;
  ΔT de 14 °C dizendo que nenhuma fonte cobre e marcando a regra do delta como
  não aplicável; região Sul entrando na conta (teto vai a 220 W); ΔT ≤ 0 sem
  número nenhum; espécie preenchendo o alvo pelo meio da faixa com a fonte
  citada; aquário de 900 L sem produto que atenda (o bloco some e a tela
  explica); **mescla do `localStorage`** preservando as medidas da C1 e a vazão
  da C3 enquanto a C5 acrescenta clima, voltagem e potência-alvo; permalink;
  caminho inverso; erros de campo obrigatório e de unidade; 390 px sem rolagem
  horizontal. **Zero erro de console.**
- **Conversão do Markdown pelo próprio Sync** nas cinco páginas: front matter
  removido, shortcode fora do `<p>`, tabelas em bloco que rola, citação em bloco,
  bloco de código, nenhuma crase solta, links convertidos, tags balanceadas.
- **sha256 do manifest conferido contra os arquivos finais commitados**: 25 itens,
  0 divergências.

### Desembarque
Automático. Manifest na revisão 9. Depois do push em `main`, o Sync precisa ser
acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/` — a calculadora nova;
- `https://aquametria.com.br/quantos-watts-de-aquecedor-para-aquario/` — o artigo-âncora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C5 deve ter virado "Abrir calculadora";
- `https://aquametria.com.br/calculadora-de-litragem/` e
  `https://aquametria.com.br/calculadora-de-vazao-do-filtro/` — devem ter ganhado o link para a C5;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

Próximo passo desbloqueado: **C12 — mídia filtrante**, pareada com o artigo dela.
Atenção ao que o validador já mostra: três filtros (Atman AT-3338, AT-3338S e
Seachem Tidal 55) estão sem `volume_filtragem_L` e por isso barrados na C12, e o
banco de mídia tem só dois registros. O caminho é o mesmo das duas últimas
execuções: **coletar com fonte antes de escrever a calculadora** — é a coleta que
decide se o bloco de produto nasce cheio ou vazio. A C12 é o vácuo de conteúdo
nº 1 do levantamento e já tem duas âncoras de fabricante que conflitam por duas
vezes (Seachem Matrix, 1,25 mL/L numa leitura da copy e 2,6 mL/L noutra) mais os
12 mL/L de cesto do Eheim 2213.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 9** (conferido nesta
sessão, sem atraso de cache: 5 snippets e 5 páginas com `publicar: true`), então
o WP-Cron do próprio site, que roda a cada 30 minutos, aplica sozinho. Para
acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

---

## 2026-09-08 (9º disparo) — BLOCO 4: C12, a mídia filtrante, no ar com o artigo-âncora pareado

Bloco entregue: **C12 — mídia filtrante**, quarta calculadora do lote, pareada
com o artigo `quanta-midia-biologica-o-aquario-precisa`. É o **vácuo de conteúdo
nº 1** do levantamento do Bloco 1 — e era o vazio que a própria página "Sobre"
do site cita como um dos motivos de a Aquametria existir.

### A coleta veio antes da calculadora, de novo, e foi ela que decidiu tudo

A execução anterior deixou o diagnóstico certo: o banco tinha **duas** âncoras
de dosagem, as duas da Seachem, e três filtros barrados por falta de
`volume_filtragem_L`. Uma calculadora com duas leituras da mesma marca não é
comparação, é um duelo interno. A primeira hora foi coleta.

**Quatro dosagens declaradas por fabricante, onde havia duas** (todas colhidas
por busca — o egresso continua bloqueado para `seachem.com`, `jbl.de` e as lojas
brasileiras — e reconfirmadas em varejo especializado que replica a mesma ficha):

| Constante nova | Valor | Fonte |
|---|---|---|
| `jbl-micromec-dosagem` | 5,00 mL/L | JBL: 650 g para 200 L, e a mesma embalagem é vendida como 1 L |
| `ocean-tech-bio-glass-dosagem` | 12,50 mL/L | Ocean Tech: 1 L para cada 80 L |
| `seachem-matrixcarbon-dosagem` | 0,625 mL/L | Seachem: 250 mL para 400 L, "vários meses" |
| `seachem-purigen-dosagem` | 0,25 mL/L | Seachem: 100 mL para 400 L, até 6 meses |

Mais `seachem-tidal-55-midia` (1,2 L de mídia para 200 L = 6,0 mL/L de mídia
TOTAL), que dá o par do `eheim-classic-250-2213` na segunda família de âncoras.

**O achado que virou o artigo.** A Ocean Tech é a **única marca brasileira** que
publica mL de mídia por litro de água — e ela pede **dez vezes** o que a Seachem
pede para a mesma função. A hipótese óbvia (mídias diferentes, áreas diferentes)
morre na aritmética: área declarada × dosagem declarada = área entregue por litro
de **água**, e ela vai de 0,88 m² (Seachem) a 7,5 (JBL) a 18,8 (Ocean Tech) —
**21 vezes**. Pior: a marca que declara MAIS área por litro de mídia (Ocean Tech,
1.500 m²/L) é a que pede DEZ VEZES mais mídia que a que declara menos (Seachem,
>700 m²/L). Se a área fosse o critério, a relação seria a inversa. Nenhuma das
quatro publica método de medição. É o eixo do artigo e é original: não achamos
ninguém, em português, cruzando essas duas colunas.

**O segundo achado, de brinde:** a Seachem discorda de si mesma em dois níveis.
Como fabricante de mídia diz que 1,25 mL/L de Matrix bastam; como fabricante de
filtro põe 6,0 mL/L de espaço de mídia no Tidal 55. E, dentro da mesma copy do
Matrix, "250 mL para 200 L" (1,25 mL/L) contra "1 L para 100 galões" (2,64 mL/L).

**Volume útil de mídia dos filtros** (`volume_filtragem_L`, que destravava a C12):
Tidal 55 com 1,2 L do próprio fabricante; Atman AT-3338 e AT-3338S com ficha de
varejo **ambígua**, e a ambiguidade virou conteúdo. A frase "3 cestos de 17x17x6
com capacidade de 1,6 litros de mídia" pode ser 1,6 L no total ou por cesto
(4,8 L) — e a geometria (1,73 L brutos por cesto) apoia a leitura por cesto. No
modelo irmão a mesma frase dá 3,5 L em cestos de 21×21×7 cm, que têm 3,09 L
brutos e **não comportam** 3,5 L: aqui só a leitura do conjunto fecha. A mesma
frase, dois modelos, leituras opostas apoiadas pela própria geometria declarada.
Registrado como `conflitos[]` com `publicar-os-dois`, e a tela mostra as duas.
O SunSun HW-303B continua barrado: nenhuma fonte publica a capacidade dos cestos.

### O que foi entregue

**`snippets/aquametria-calculadora-midia.php` (v1.0.0, 1.675 linhas)** — o
shortcode `[aquametria_calculadora_midia]`. As âncoras **não são digitadas no
JavaScript**: saem do catálogo embutido, que sai do banco de produtos. Mídia nova
com dosagem declarada entra na tabela sozinha no próximo gerador — não há como as
duas cópias divergirem em silêncio.

O que ela entrega: a faixa de mídia biológica (para 110 L, de 140 mL a 1,38 L)
dizendo com todas as letras que **a faixa é 10 vezes larga porque os fabricantes
discordam 10 vezes, não porque a conta seja imprecisa**; as duas tabelas de
âncoras, separadas porque respondem perguntas diferentes; e **o teto físico** —
quanto do cesto do filtro escolhido cada dosagem ocuparia, com barra e
porcentagem, avisando quando a camada biológica sozinha estoura ("o problema não
é a mídia, é o filtro"). Essa conta é trivial e não a encontramos publicada em
português. Mais: ordem das camadas, camada química nas duas unidades que não
conversam, calendário de trocas com datas calculadas a partir da última
manutenção, TPA, gatilhos de nitrato, e o caminho inverso.

**O que ela se recusa a fazer, escrito na tela:** não escolhe uma dosagem; não
reparte o cesto em porcentagens (`proporcao-entre-camadas-do-cesto`, pendente —
publica a ORDEM, que tem fonte); não converte grama em mililitro no carvão
(`densidade-aparente-carvao-ativado`, pendente — mas a FREQUÊNCIA compara sem
conversão: a regra BR manda trocar de 4 a 10 vezes mais que o fabricante do
carvão); não compara marcas por área de superfície; não dimensiona mídia sem
dosagem declarada (o Eheim Substrat pro sai no cartão sem número de compra,
dizendo por quê); e não estima validade de mídia biológica.

**`conteudo/calculadora-de-midia-filtrante.md`** — a metodologia: as duas tabelas
com atribuição, o teto físico, as fichas ambíguas do Atman destrinchadas, a lista
de recusas e o aviso obrigatório sobre lavar mídia biológica publicado como
**mecanismo explicado** (cloro existe para matar bactéria; a colônia leva semanas;
por isso a substituição é parcial; para a sujeira grossa, use a água da TPA).

**`conteudo/quanta-midia-biologica-o-aquario-precisa.md`** — o artigo-âncora, o
segundo do projeto. Não repete a calculadora: desenvolve o paradoxo da área, a
Seachem contra si mesma, o caso do carvão, e a **crítica de fundo** — todas as
quatro dosagens são por litro de ÁGUA, mas o trabalho da mídia depende da amônia
que entra, ou seja, da carga de peixes, que nenhuma declaração pergunta. Fechar
isso exigiria `taxa-de-nitrificacao-por-area` (pendente, registrada). Linka a
calculadora no primeiro terço; a calculadora linka de volta.

**Constantes:** 42 → 50. Cinco novas com fonte e três **pendências declaradas**
(proporção entre camadas, densidade do carvão, taxa de nitrificação), que existem
no registro justamente para dizer o que a C12 não publica e por quê.

**Banco:** 21 → 25 produtos. Mídias de 2 para 6 (JBL MicroMec, Ocean Tech Bio
Glass, Seachem MatrixCarbon, Seachem Purigen — todas sem link de afiliado, porque
a geração do link curto é manual no painel Shopee e fica fora desta sessão; pela
regra V16 elas saem no cartão do mesmo jeito, sem botão de loja). Três filtros
ganharam `volume_filtragem_L`.

**Ligações, para nenhuma página nascer órfã:** a C1 (v1.0.3), a C3 (v1.0.2) e a
C5 (v1.0.1) passaram a LINKAR a C12 nos painéis de ligação; a casca (v1.0.4) teve
o resumo da C12 no hub reescrito de "duas âncoras" para as quatro reais; a C12
aponta de volta para C1, C3, C5, hub, metodologia, divulgação de afiliados e o
artigo pareado.

**Ferramentas novas:** `gerar-catalogo-midias.py` (escreve DOIS blocos no mesmo
snippet, porque a C12 consome os dois bancos, e carrega a segunda leitura dos
campos em conflito para a tela publicar as duas) e `teste-navegador-c12.mjs`
(19 cenários).

### Verificação (o que foi realmente rodado)
- **`php -l` de verdade** nos seis snippets (com `<?php` prefixado): limpo.
- **`ferramentas/proteger-funcoes.php`** nos quatro snippets tocados: saída
  idêntica ao arquivo — nenhuma função de nível superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 25 produtos, **0 erro**, 1 aviso
  conhecido (o V11 do Jäger 200 W, que é conteúdo da página, não defeito).
  `c12-midia-filtrante`: 4 aptos com link, 6 sem link, 1 barrado (o SunSun, por
  falta de `volume_filtragem_L` — e a tela diz isso).
- **Teste de fumaça estrutural**: 45 ids, nenhum duplicado; div, ul, li, form,
  table, p, tbody, span e a todos balanceados; acentos preservados; nenhuma
  superglobal de servidor no HTML; aviso de comissão e link da divulgação
  presentes; `rel="sponsored noopener"` no JS; nenhum preço cravado.
- **Teste em navegador de verdade** (Chromium via Playwright), **19 cenários, todos
  passando**: caso base; as quatro âncoras com atribuição e link de fonte; a
  segunda família de âncoras; teto físico num Eheim classic 250 (Seachem 5 %,
  Ocean Tech 46 %); **teto estourado** (600 L num Tidal 55, com "Não cabe" e "o
  problema é o filtro"); as duas leituras da ficha do Atman na tela; volume de
  mídia digitado à mão, com o critério editorial declarando que a medida é da
  pessoa; ordem das camadas com a recusa da proporção; camada química com as duas
  unidades e a recusa da conversão; calendário de trocas com datas calculadas
  (perlon 08–16/09, carvão 16/09–01/10, cerâmica 01/03–01/09 de 2027); TPA e
  nitrato; **o aviso obrigatório** sobre lavar mídia; bloco de produto com 4
  mídias (6 com química marcada); **atributos do link de afiliado** (`sponsored
  noopener` + `_blank` + https nos dois links); **mescla do `localStorage`**
  preservando medidas da C1, clima da C5 e vazão da C3; permalink; caminho
  inverso; erros de entrada; 390 px sem rolagem horizontal. **Zero erro de
  console.**
- **Teste da C5 rodado de novo** depois de tocar o snippet dela: todos os 15
  cenários continuam passando (sem regressão pela ligação nova).
- **Conversão do Markdown pelo próprio Sync** nas sete páginas: front matter
  removido, shortcode fora do `<p>`, tabelas dentro do bloco que rola, nenhuma
  crase solta, nenhum link markdown por converter, tags balanceadas.
- **sha256 do manifest conferido contra os arquivos finais commitados**: 30 itens,
  0 divergências.

### Desembarque
Automático. Manifest na **revisão 10**. Depois do push em `main`, o Sync precisa
ser acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-midia-filtrante/` — a calculadora nova;
- `https://aquametria.com.br/quanta-midia-biologica-o-aquario-precisa/` — o artigo-âncora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C12 deve ter virado "Abrir calculadora", com o resumo novo;
- `https://aquametria.com.br/calculadora-de-litragem/`, `/calculadora-de-vazao-do-filtro/` e
  `/calculadora-de-potencia-do-aquecedor/` — devem ter ganhado o link para a C12;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

**Próximo passo desbloqueado: C15 — iluminação e fotoperíodo**, pareada com o
artigo dela. Atenção ao que o validador já mostra: dos 5 registros de iluminação,
**4 estão barrados** — três por falta de `voltagem` (Aquários do Rio LED 60 cm,
Chihiros WRGB II Pro 60, ISTA IL-401-60) e um por falta de `fluxo_lm` (SunSun
ADE-400C). O caminho é o mesmo das três últimas execuções: **coletar com fonte
antes de escrever a calculadora**, porque é a coleta que decide se o bloco de
produto nasce cheio ou vazio. E há uma armadilha própria da C15 registrada na
especificação: `ppfd-por-litragem` está **pendente**, e a regra V5 exige que
`ppfd_declarado` e `ppfd_distancia_cm` andem juntos — PPFD sem distância declarada
não entra. A constante `iluminacao-lumen-por-litro` tem três fontes que chamam as
mesmas faixas pelos mesmos nomes com números diferentes, que é exatamente o
padrão que a C12 acabou de aprender a publicar em tabela com atribuição.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 10** (conferido
nesta sessão, sem atraso de cache: 6 snippets e 7 páginas com `publicar: true`),
então o WP-Cron do próprio site, que roda a cada 30 minutos, aplica sozinho.
Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

**Uma coisa depende do Raphael, e não bloqueia nada.** As quatro mídias novas
(JBL MicroMec, Ocean Tech Bio Glass, Seachem MatrixCarbon e Seachem Purigen)
entraram no banco **sem link de afiliado**, porque a geração do link curto é
feita à mão no painel Shopee Afiliados, fora desta sessão. Pela regra V16 elas
já aparecem no bloco de produto, com a quantidade calculada e a ficha completa,
só sem botão de loja — a página está correta e completa do jeito que está. Mas
são quatro cartões monetizáveis parados: hoje só o Seachem Matrix e o Eheim
Substrat pro têm link na C12. Gerar os quatro links (Sub_id_2 = `C12`) e colar
em `dados/produtos-midia.json` é trabalho de cinco minutos no painel, e a
próxima execução pega sozinha. O mesmo vale para os 6 aquecedores e as 2
luminárias que já estão aptos e sem link desde as execuções anteriores.

---

## 2026-09-08 (10º disparo) — BLOCO 4: C15, a iluminação e o fotoperíodo, no ar com o artigo-âncora pareado

Bloco entregue: **C15 — iluminação e fotoperíodo**, quinta calculadora do lote,
pareada com o artigo `quantos-lumens-por-litro-aquario-plantado`. É o maior
cluster empatado do levantamento do Bloco 1 (83 consultas, junto com o C10).

### De novo, a coleta veio antes da calculadora — e de novo era o bloqueio real

A execução anterior deixou o diagnóstico: dos 5 registros de iluminação, **4
estavam barrados** — três por `voltagem`, um por `fluxo_lm`. Com 1 luminária
sugerível, o bloco de produto nasceria vazio. A primeira hora foi coleta, toda
por resultado de busca (o egresso da nuvem continua barrando `proaquarista.com.br`,
`aquariosdorio.com.br` e as demais lojas brasileiras — o WebFetch devolve
`EGRESS_BLOCKED`, e as fichas entram marcadas como `transcrita-varejo` lida por
busca, com o pedido de conferir a embalagem).

O que a coleta trouxe:

| Registro | O que faltava | O que a ficha declarou em 08/09 |
|---|---|---|
| `ista-il-401-60` | voltagem | bivolt (110/220 V), cobre aquário de 56 a 66 cm, peça de 56 × 12 × 4,6 cm, IRC > 95 % |
| `aquarios-do-rio-led-60cm` | voltagem | bivolt, cobre 55 a 75 cm com suportes reguláveis, timer com até 3 fotoperíodos e nascer/pôr do sol |
| `wfish-wf-h600-wrgb` (novo) | — | 36 W, bivolt, WRGB, peça de 56,7 × 8 cm, cobre 60 a 65 cm; **sem lúmen em fonte alguma** |
| `chihiros-wrgb-ii-pro-60` | voltagem | **nada**: nenhuma fonte declara. Continua barrada, e tem link de afiliado |
| `sunsun-ade-400c` | lúmen | **nada**: nenhuma loja publica. Continua barrada, e tem link de afiliado |

Resultado: **3 aptas de 6** (contra 1 de 5), 1 delas com link. Duas luminárias
que TÊM link de afiliado seguem barradas — e isso virou conteúdo de tela, não
constrangimento escondido: a lista dos barrados é publicada na página, com o
motivo de cada um e a frase "link não promove produto barrado".

### O achado que virou o artigo: a régua usa a unidade errada

O lúmen é ponderado pela sensibilidade do olho humano, que pesa o verde e
desconta azul e vermelho profundos — que são exatamente as duas faixas em que a
clorofila trabalha. Consequência incômoda para a regra de lm/L: **a luminária
projetada para planta tende a marcar MENOS lúmens que uma calha branca de mesmo
consumo, e a régua a considera pior.** O nosso banco é coerente com isso — a
Chihiros WRGB II Pro 60 dá 89,6 lm/W e a calha branca Ista IL-401 dá 106 lm/W —
e o artigo apresenta os dois números como **indício, não demonstração**, porque
dois produtos não provam padrão nenhum.

**E a trilha do PPFD termina antes do Brasil.** Procurando a tabela de PAR da
linha WRGB II Pro para o banco, chegamos ao fórum de suporte da própria
Chihiros — marca cujo argumento de venda é PAR: a resposta oficial é que **não
existe teste de PAR oficial** e que o usuário procure medições no YouTube. Ou
seja, a ausência brasileira não é preguiça de blogueiro: o fabricante não
publica. `ppfd-por-litragem` continua `pendente`, agora com URL e data, e a
página publica esse motivo em vez de só dizer "não temos fonte".

### O segundo achado: o nome não é o tamanho da peça

O varejo brasileiro nomeia luminária por centímetro, e o centímetro do nome nem
sempre é o da peça. A Ista vendida como "IL-401 60 cm" mede **56 cm** na ficha
de dimensões da mesma página. Registrado como `conflitos[]` (nome comercial,
origem `marketplace-anuncio`, contra ficha de varejo — `nivel-mais-alto-vence`),
e a calculadora mostra os dois números no cartão.

Disso saiu a **decisão editorial desta execução**, que fecha uma pendência
aberta desde o Bloco 3 (`pendencia_de_criterio` da entidade iluminação):

> **A Aquametria NÃO converte comprimento de peça em cobertura de aquário.**
> Nos 5 registros que declaram os dois números, o teto declarado vai de **1,15 a
> 1,59 vez** o comprimento da peça (41 cm cobrindo 65; 60 cm cobrindo 66) e o
> piso de 0,92 a 1,17. Não há razão constante a extrair, e fabricar uma média
> serviria para recomendar luminária que deixa as pontas na sombra.

Virou a constante `cobertura-luminaria-declarada` (status `convencao-editorial`,
com a `derivacao` escrita), o `minimo_para_sugerir` da `c15-iluminacao` passou a
exigir `comprimento_aquario_cm` **declarado**, e o esquema foi para a versão 4.
O efeito da convenção é só barrar sugestão: ela nunca cria número.

### O que foi entregue

**`snippets/aquametria-calculadora-iluminacao.php` (v1.0.0)** — o shortcode
`[aquametria_calculadora_iluminacao]`, escopo global, anunciado no hub pelo
filtro `aquametria_calculadoras`. O que ele põe na tela:

- **A faixa de lúmens** no volume da pessoa, pela faixa consolidada do nível
  escolhido (baixa 10–20, média 20–40, alta 40–60+ lm/L) — e, ao lado, **a
  tabela das três leituras brasileiras**, com o nome de quem publicou cada uma.
  A divergência é calculada e dita: 2,0 vezes sobre o rótulo "baixa".
- **Faixa aberta no nível alto**: uma das fontes escreve "acima de 40 lm/L" e
  para aí. A resposta sai com "+" em vez de um teto inventado.
- **Os quatro regimes de fotoperíodo**, com o da pessoa marcado, e a frase que
  falta em toda tabela copiada: hora a mais não compensa lúmen a menos.
- **O bloco de CO2 com os dois limites que se sobrepõem** (útil 15–35 mg/L,
  risco acima de 30–35) publicados como sobreposição, mais o drop checker; e o
  aviso obrigatório quando o nível alto é escolhido **sem** CO2.
- **Aviso de lâmina acima de 45 cm**, que é onde lm/L começa a mentir por não
  saber a profundidade.
- **Painel de consumo**: kWh/mês do fotoperíodo escolhido (física pura) e reais
  **só com a tarifa que o visitante digita** — tarifa de energia não é publicada
  aqui, e a tela diz por quê.
- **Bloco de produto** com a cobertura de comprimento como barreira, a lista
  publicada dos barrados, e um caso que mostra o preço das regras: a luminária
  mais cara do banco tem link de afiliado e **não** é sugerida.
- **Caminho inverso** (tenho X lúmens, que aquário isso cobre em cada nível).

**`conteudo/calculadora-de-iluminacao.md`** — página-âncora com o shortcode, a
tabela das três leituras, as três coisas que a calculadora faz de diferente, as
quatro que ela recusa fazer com o motivo de cada uma (com a tabela de peça ×
cobertura), as regras do bloco de produto e as seções de fotoperíodo, CO2 e
profundidade.

**`conteudo/quantos-lumens-por-litro-aquario-plantado.md`** — o artigo pareado,
com o eixo da unidade errada, a trilha do PPFD que termina na própria Chihiros,
o que o varejo declara no lugar (centímetros), a armadilha do nome, onde as três
fontes **concordam**, seis recomendações práticas e as três coletas que faltam
— incluindo a recusa de publicar fator de conversão de lux para PPFD, que
depende do espectro e não tem fonte.

**Banco e ferramentas:** `dados/produtos-iluminacao.json` (6 registros, 0 erro
no validador), `dados/constantes-calculadoras.json` (51 constantes),
`dados/esquema-produtos.json` v4, `ferramentas/gerar-catalogo-iluminacao.py`
(escreve DOIS blocos no snippet: os aptos e os barrados com motivo) e
`ferramentas/teste-navegador-c15.mjs` (21 cenários).

**Nenhuma página nasce órfã:** C1 (v1.0.4), C3 (v1.0.3), C5 (v1.0.2) e C12
(v1.0.1) passaram a linkar a C15 no painel de ligações, cada uma com o motivo
técnico da ligação. A casca não precisou ser tocada: a C15 vira "publicada" no
hub pelo próprio filtro, e o resumo do cartão é reescrito pelo snippet.

**Uma decisão de arquitetura pequena e que vale para as próximas:** o banco de
produtos é escrito **sem acento** (convenção do repositório) e a tela sai
**acentuada**. Então o gerador manda a **estrutura** do conflito (campo, valor,
origem) e quem escreve a frase é o JavaScript do snippet. Texto de banco não vai
para a tela.

### Verificação (o que foi realmente rodado)

- **`php -l` de verdade** nos 7 snippets, e `ferramentas/proteger-funcoes.php`
  devolvendo saída idêntica ao arquivo em todos — nenhuma função de nível
  superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 26 produtos, **0 erro**, 1 aviso
  conhecido (o V11 do Jäger 200 W, que é conteúdo da página). `c15-iluminacao`:
  1 apto com link, 2 aptos sem link, 3 barrados.
- **Teste em navegador de verdade** (Chromium via Playwright), **21 cenários e
  mais de 60 verificações, todos passando**: caso base; as 9 linhas da tabela de
  leituras com as três fontes nomeadas; a divergência de 2,0 vezes no rótulo
  "baixa"; a faixa aberta do nível alto com "+"; o aviso de luz alta sem CO2; a
  sobreposição dos limites de CO2 e o drop checker; os quatro regimes; o aviso
  de lâmina de 55 cm; a recusa de listar produto sem o comprimento do aquário; o
  bloco de produto (dois cartões, ordenados pela proximidade do meio da faixa, o
  conflito nome-contra-ficha publicado no cartão, o modelo de 810 lm barrado
  pela cobertura com o motivo na tela); a lista dos três barrados; os atributos
  do link de afiliado (`sponsored noopener`, `_blank`, https); o aviso de
  comissão e o link da divulgação; o caso sem nenhuma luminária que cubra 120 cm;
  o consumo (5,0 kWh/mês e R$ 4,79 com tarifa de R$ 0,95) e a recusa de publicar
  tarifa padrão; o caminho inverso; a **mescla do `localStorage`** preservando
  medidas da C1, vazão da C3 e clima da C5; o permalink e a reconstrução por
  query string; os erros de entrada; 390 px sem rolagem horizontal.
  **Zero erro de console.**
- **Testes da C5 e da C12 rodados de novo** depois de tocar os dois snippets:
  todos os cenários continuam passando (sem regressão pelas ligações novas).
- **Conversão do Markdown pelo próprio Sync** nas duas páginas novas: front
  matter removido, shortcode fora do `<p>`, as duas tabelas de cada página
  dentro do bloco que rola, nenhuma crase solta, nenhum link markdown por
  converter, tags balanceadas, acentos preservados.
- **sha256 do manifest conferido contra os arquivos finais commitados**: todos
  os itens, 0 divergências.

### Desembarque

Automático. Manifest na **revisão 11**. Depois do push em `main`, o Sync precisa
ser acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-iluminacao/` — a calculadora nova;
- `https://aquametria.com.br/quantos-lumens-por-litro-aquario-plantado/` — o artigo-âncora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C15 deve ter virado "Abrir calculadora";
- `/calculadora-de-litragem/`, `/calculadora-de-vazao-do-filtro/`,
  `/calculadora-de-potencia-do-aquecedor/` e `/calculadora-de-midia-filtrante/`
  — devem ter ganhado o link para a C15;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

**Próximo passo desbloqueado: C2 — peso do aquário cheio e carga no piso**,
pareada com o artigo dela. É a próxima da ordem depois da C15. Duas travessas
já conhecidas, registradas na especificação: (a) a C2 **não publica espessura de
vidro** nem veredito de "a laje aguenta" — falta tensão admissível e coeficiente
de segurança citáveis; (b) a carga de projeto da NBR 6120 está no corpus como
`norma-via-secundaria` (norma paga, não lida direto), e a tela precisa dizer isso
com essas palavras. O que a C2 tem de sólido é a aritmética: volume × densidade
+ vidro + substrato + rochas, e a carga por metro quadrado comparada com a de
projeto. O padrão das quatro últimas execuções continua valendo: **a coleta vem
antes da calculadora**.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 11** (conferido
nesta sessão, sem atraso de cache: 7 snippets e 9 páginas com `publicar: true`,
incluindo `calculadora-de-iluminacao` e `quantos-lumens-por-litro-aquario-plantado`),
então o WP-Cron do próprio site, que roda a cada 30 minutos, aplica sozinho.
Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

**O que depende do Raphael, e não bloqueia nada.** A dívida de links de afiliado
cresceu e agora tem um caso que dói: das 3 luminárias que a C15 consegue sugerir,
só a Ista I-401 45 cm tem link — o LED 60 cm dos Aquários do Rio e a Ista IL-401
60 cm entram no cartão sem botão de loja, e a IL-401 é justamente a que mais
aparece, porque cobre a faixa de aquário mais comum (56 a 66 cm). Somando com o
que já estava parado: 4 mídias, 6 aquecedores e agora 2 luminárias aptas e sem
link. Gerar os links no painel Shopee Afiliados (Sub_id_2 = `C15` para as
luminárias) e colar em `dados/produtos-*.json` é trabalho de minutos, e a
próxima execução pega sozinha.

E o inverso também está registrado: **duas luminárias que TÊM link continuam
barradas** — a Chihiros WRGB II Pro 60 (nenhuma fonte declara voltagem) e a
SunSun ADE-400c (nenhuma loja publica lúmen). Elas não são sugeridas, e a página
diz isso na cara, com o motivo. Uma foto da embalagem de qualquer uma das duas
resolveria o campo que falta.

---

## 2026-09-08 (11º disparo, correção urgente) — o Sync não se atualiza sozinho: nasceu o atualizador

**Fila normal interrompida a pedido do Raphael.** A C2 (peso e carga no piso) fica
para a próxima execução. Esta rodada resolveu um defeito visível no site e, mais
importante, o gargalo estrutural que o produziu.

### O defeito

O Raphael abriu `https://aquametria.com.br/calculadora-de-litragem/` e viu o front
matter YAML do arquivo Markdown impresso **dentro do corpo da página**:
"— id: calculadora-de-litragem tipo: pagina titulo: … publicar: true —", com a lista
de fontes virando lista com marcadores. Os `---` viraram travessão porque o
`wptexturize` do WordPress converte três hifens em em-dash.

### A causa, confirmada nesta sessão

O repositório estava **certo**. O que roda no site é que estava velho.

- `ilhas/aquametria/snippets/aquametria-sync.php` está na v1.1.3 desde 08/09 e corta
  o front matter em `aquametria_sync_md()` desde a **v1.1.1** (07/09).
- O snippet "Aquametria Sync" **ativo no site** é a **v1.1.0**, colada à mão pelo
  Raphael em 07/09.
- Rodei o conversor da v1.1.3 sobre os 9 arquivos reais de `conteudo/`: **nenhum
  resíduo de YAML em nenhum deles**. O lado do repositório nunca produziu o defeito.

E o motivo de a correção nunca ter chegado ao site é estrutural, não um esquecimento:

> **O Sync se pula a si mesmo de propósito.** Em `aquametria_sync_aplicar_snippet()`,
> a checagem `$nome === AQUAMETRIA_SYNC_NOME_PROPRIO` devolve "pulado". Isso protege o
> site — o Sync não se reescreve no meio da própria execução — e, como efeito colateral
> permanente, **nenhuma correção no próprio Sync chega ao site sozinha**.

Quatro versões do conversor de Markdown (1.1.1, 1.1.2, 1.1.3 e agora a 1.1.4) ficaram
só no repositório sem ninguém notar, porque o log do Sync dizia "aplicado com sucesso"
— e dizia a verdade. As páginas *foram* aplicadas. Pelo conversor velho.

### 1. Sync v1.1.4 — o corte do front matter ficou tolerante

A regex antiga (`/\A---\n.*?\n---\n?/s`) exigia o arquivo perfeito. Três variações que
**não aparecem no editor** a derrotavam em silêncio, e uma delas produz exatamente a
tela que o Raphael viu:

| Variação | O que acontecia antes |
| --- | --- |
| BOM no começo do arquivo | o BOM fica antes do `---` e o corte não casa |
| quebra de linha antiga, só `\r` | o arquivo inteiro vira uma linha só |
| espaço ou tabulação à direita do `---` | o corte não casa e o YAML sai como parágrafo |

Agora o conversor tira o BOM, normaliza `\r\n` **e** `\r` sozinho, e aceita espaço ou
tabulação à direita dos dois delimitadores. O `---` legítimo no meio do texto continua
intocado (é caso de teste).

**`ferramentas/teste-conversor-markdown.php`** (novo) roda o conversor do próprio
snippet Sync sobre todos os arquivos de `conteudo/` e recusa qualquer resíduo de
metadado no HTML — chaves como `publicar:`, `verificado_em:`, `slug:`, HTML que comece
por separador, primeiro bloco que não seja texto — mais as oito variações de front
matter acima. **17 casos, 0 falhas.**

### 2. O ATUALIZADOR — a entrega estrutural

**`snippets/aquametria-atualizador-sync.php`**, nome no Code Snippets
**"Aquametria Sync — atualizador do Sync"**, escopo global, ativo, `publicar: true`.

Como o **nome é diferente** do nome do Sync, a v1.1.0 que está no site vai instalá-lo e
ativá-lo pelo caminho que já funciona. E a única coisa que ele faz é reescrever o Sync
a partir do repositório. Cada trava existe por um motivo:

- **sha256 contra o manifest, antes de qualquer coisa.** Divergiu, aborta e registra —
  nunca grava código não verificado.
- **Coerência de versão:** o arquivo tem de declarar a mesma versão que o manifest
  anuncia. Manifest desatualizado não vira gravação.
- **Sintaxe de verdade, sem executar o código:** `token_get_all( $codigo, TOKEN_PARSE )`
  faz o parse completo e levanta `ParseError` em código quebrado. É o mais perto de um
  `php -l` que dá para fazer dentro do WordPress sem `eval` — e `eval` aqui seria
  justamente o erro que derrubou o site em 07/09.
- **Backup, e a releitura que prova que ele existe:** grava o código atual em
  `aquametria_sync_backup_codigo` (com versão, id do snippet, sha e data) e **relê a
  option** comparando o tamanho. Sem backup confirmado, não prossegue.
- **Gravação pelo caminho que a v1.1.0 já usa e que sabidamente funciona:**
  `Code_Snippets\Model\Snippet`, `save_snippet()` lido como **objeto**, gravação
  **INATIVA** primeiro e `activate_snippet()` depois, tudo em `try/catch`. Nunca
  `new \Code_Snippets\Snippet()`.
- **A verificação é uma REQUISIÇÃO NOVA.** Nesta requisição o código velho continua
  carregado na memória do PHP, então perguntar à constante não prova nada. Ele busca
  `/wp-json/aquametria/v1/status` e confere `versao_sync`. Não bateu, ou o endpoint
  devolveu erro, **restaura o backup automaticamente**. Loopback mudo (o site fechado
  para si mesmo) conta como **inconclusivo** e mantém o código novo: derrubar a versão
  nova por falta de prova seria pior que mantê-la, e fica escrito no log.
- **No máximo uma vez por hora**, por WP-Cron, e só quando a versão do manifest difere
  da que está rodando. A marca de tentativa é gravada **antes** de tentar, para que uma
  falha no meio não vire laço.
- **Log legível** em `GET /wp-json/aquametria/v1/atualizador` (público, só o log).
  Gatilho manual: `/?aquametria_atualizar_sync=TOKEN&forcar=1`, com o mesmo token do Sync.

**`ferramentas/teste-atualizador-sync.php`** (novo) exercita tudo isso com WordPress e
Code Snippets falsos, **um processo por cenário** — a versão instalada é uma constante,
e constante não muda dentro do mesmo processo. **9 cenários, 0 falhas:**

| Cenário | O que tem de acontecer |
| --- | --- |
| feliz | grava inativo, ativa, verifica, marca o conteúdo, registra o sha aplicado |
| sha divergente | aborta sem gravar e sem sequer criar backup |
| sintaxe quebrada | aborta sem gravar |
| versão mentirosa | manifest anuncia 9.9.9, arquivo declara outra: aborta |
| verificação falha | **restaura o backup** e o site volta à 1.1.0 |
| loopback mudo | mantém o código novo e diz que a verificação foi inconclusiva |
| já atualizado | não reescreve nada |
| janela de 1 h | nem chega a baixar o manifest |
| Sync ausente | aborta — reescreve, não instala do zero |

### 3. Reaplicação das páginas que estão no ar com o YAML sujo

Feita **pelo próprio atualizador**, porque este container não alcança o site. Depois de
atualizar o Sync com sucesso, ele apaga o `sha256` registrado de cada item `conteudo:*`
em `aquametria_sync_estado` e zera a revisão — é isso que obriga a reaplicação, já que o
Sync pula arquivo cujo sha já foi aplicado — e agenda um evento avulso do sync para 60
segundos depois. Ele **não** roda o sync na mesma requisição: ali quem está carregado é
o conversor velho, que reescreveria o mesmo defeito. O teste confere que só os itens de
conteúdo perdem o sha (o de snippet fica) e que nada disso acontece quando houve
reversão.

### 4. Regra permanente (gravada em ESTADO.md, seção da fase 4b)

> **O snippet Sync não se atualiza sozinho, por desenho.** Toda correção no próprio Sync
> chega ao site pelo snippet atualizador, nunca por colagem manual do Raphael. Mexeu em
> `snippets/aquametria-sync.php`? Suba a versão no cabeçalho **e** o campo `versao` do
> item `aquametria-sync` no manifest — sem isso o atualizador não vê motivo para agir.

> **Depois de publicar qualquer página vinda de `conteudo/`, buscar a URL no ar e
> conferir que o corpo começa pelo TEXTO, não por metadado.** Nunca confie no "aplicado
> com sucesso" do log: em 08/09 o log estava certo e a página estava errada, e quem viu
> o defeito foi o Raphael, não a rotina.

O campo `versao` entrou no `esquema.snippets` do manifest, documentado.

### Verificação (o que foi realmente rodado)

- **`php -l` de verdade** nos 8 snippets, e `ferramentas/proteger-funcoes.php` devolvendo
  saída idêntica ao arquivo em todos — nenhuma função de nível superior desprotegida.
- **`teste-conversor-markdown.php`**: 17 casos, 0 falhas. As 9 páginas reais saem sem
  nenhum resíduo de YAML, e as 8 variações de front matter são cortadas.
- **`teste-atualizador-sync.php`**: 9 cenários, 0 falhas (tabela acima).
- **Simulação do Sync DO SITE aplicando a revisão 12**, com Code Snippets falso: ele se
  pula pelo nome, **cria o "Aquametria Sync — atualizador do Sync"** e o ativa, aplica os
  outros 6 snippets e as 9 páginas, e **todas as 9 páginas começam por `<p>` com texto de
  verdade**. É a prova de que o caminho de entrega funciona com a v1.1.0 que está no ar.
- **sha256 do manifest recalculado e conferido** contra os arquivos finais commitados:
  todos os itens, 0 divergências.

### Desembarque

Manifest na **revisão 12**. `WebFetch` em `aquametria.com.br` continua devolvendo
`EGRESS_BLOCKED` — este container só alcança o GitHub —, então **não consegui confirmar
a página no ar nesta sessão**. A sequência que o site executa sozinho, sem ninguém tocar
em nada:

1. o WP-Cron do Sync (a cada 30 min) vê a revisão 12 e **instala o atualizador**;
2. o cron do atualizador (de hora em hora, primeira volta ~3 min depois de ativado) vê
   a v1.1.4 no manifest contra a v1.1.0 instalada, grava, ativa, verifica e marca as
   páginas para reaplicação;
3. o evento avulso do Sync, 60 s depois, reaplica as 9 páginas **com o conversor novo**.

Para acionar na hora, na ordem:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ `https://aquametria.com.br/?aquametria_atualizar_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ o mesmo `?aquametria_sync=…&forcar=1` de novo.

**A CONFERIR (fica para a próxima execução, e é a primeira coisa a fazer):**
`https://aquametria.com.br/wp-json/aquametria/v1/status` tem de responder
`"versao_sync":"1.1.4"`; `https://aquametria.com.br/wp-json/aquametria/v1/atualizador`
mostra o log do atualizador; e o corpo de `/calculadora-de-litragem/`,
`/calculadora-de-vazao-do-filtro/`, `/calculadora-de-potencia-do-aquecedor/`,
`/calculadora-de-midia-filtrante/`, `/calculadora-de-iluminacao/` e
`/quantos-lumens-por-litro-aquario-plantado/` tem de começar pelo texto, não por
metadado.

**Próximo passo desbloqueado: C2 — peso do aquário cheio e carga no piso**, pareada com
o artigo dela, depois de conferir as URLs acima. As duas travessas continuam as mesmas:
a C2 não publica espessura de vidro nem veredito de "a laje aguenta" (falta tensão
admissível e coeficiente de segurança citáveis), e a carga de projeto da NBR 6120 está
no corpus como `norma-via-secundaria`, o que a tela precisa dizer com essas palavras.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-08 (3ª execução do dia) — CORREÇÃO CRÍTICA: as cinco calculadoras não calculavam

Fila normal de blocos interrompida. O Raphael abriu as páginas no navegador, com o
console aberto, e viu o que nenhum teste desta ilha via: **nenhuma das cinco
calculadoras publicadas funcionava**. A C2 fica para a próxima execução.

### Defeito 1 (o grave) — o WordPress escapava os `&&` e matava o script inteiro

Confirmado no repositório antes de mexer em qualquer coisa: os cinco snippets
montavam o `<style>` e o `<script>` **dentro** do valor que o shortcode devolve
(`$h .= '<script id="aquametria-c3-script">' . $js . '</script>';`). Tudo que volta
do shortcode ainda atravessa os filtros de texto do conteúdo, que trocam cada `&`
por `&#038;`. O primeiro `&&` do script virava `&#038;&#038;`, o navegador parava
com `SyntaxError` e a calculadora inteira morria: o formulário nunca calculava, os
contêineres `aqm-cN-saida` e `aqm-cN-produtos` ficavam com a classe `-oculto` — eles
nascem ocultos no HTML, quem os revela é o script — e **o bloco de produto com os
links de afiliado nunca aparecia**. Clicar em "Calcular" só fazia submit nativo do
formulário. A casca escapou porque já imprimia o CSS dela no `wp_head`.

**Correção, que passa a ser o padrão de toda calculadora futura:** o shortcode
devolve só o HTML. O estilo sai no `wp_head` (sem piscar sem estilo, com
`has_shortcode()` decidindo se a página usa) e o comportamento sai no `wp_footer`,
registrado pelo próprio shortcode quando ele roda. Ambos fora dos filtros de
conteúdo. Nenhuma linha de cálculo mudou — mudou o lugar de onde o script sai.
As cinco foram para a v1.1.0.

### Defeito 2 — slug que o hub publicava e que dava 404

`aquametria_casca_calculadoras()` trazia `'slug' => 'calculadora-de-aquecedor'` para
a C5, cuja página é `/calculadora-de-potencia-do-aquecedor/`. O slug certo só chegava
ao hub pelo filtro da própria C5; bastava ela não carregar para o hub publicar 404.
Corrigido o valor **e** a estrutura: a casca (v1.1.0) resolve o endereço de cada
página pelo `_aquametria_id` que o Sync grava — identidade canônica, que sobrevive
ao WordPress ter trocado o slug — e **só vira link se a página existir publicada**.
Sem página, sai o selo "Em construção" ou o rótulo sem link, nunca um 404.

Descoberta na mesma trilha: `wp_insert_post()` **renomeia `post_name` em silêncio**
quando o endereço já está ocupado (acrescenta `-2`), e o Sync respondia "ok" do
mesmo jeito — o log dizia uma coisa e o site tinha outra. Sync v1.1.5: cada página
aplicada devolve o permalink real, o slug divergente sai com ATENÇÃO no log e o
estado guarda `slug_ok:false`, que o endpoint de status publica.

### Defeito 3 — front matter

Do lado do repositório está resolvido e conferido: `teste-conversor-markdown.php`,
17 casos, 0 falhas, e as 9 páginas reais saem sem resíduo de YAML.
`teste-atualizador-sync.php`, 9 cenários, 0 falhas. **Não foi possível confirmar no
ar**: o `WebFetch` para `aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessão,
como nas anteriores. Fica como primeira conferência da próxima execução que
alcançar o site.

### Por que nenhum teste tinha pego isso — e o que mudou

`ferramentas/render-para-teste.php` mentia. Tratava `add_action` como no-op e não
aplicava o escape de `&`, então o script saía inline no HTML de teste e tudo passava
enquanto o site estava quebrado. Agora ele monta a página como o WordPress monta:
`wp_head`, conteúdo **já passado pelo escape de `&`**, `wp_footer`.

Três redes novas, todas com **controle negativo conferido** — reprovam o código
defeituoso e aprovam o corrigido:

- `ferramentas/teste-escape-shortcode.php` — 45 afirmações, 5 calculadoras. Com o
  `<script>` de volta dentro do retorno do shortcode, ele acusa **26 ocorrências de
  `&#038;`** na C1 e reprova.
- `ferramentas/teste-navegador-cinco.mjs` — executa o cálculo das cinco num Chromium
  de verdade: clica em Calcular, confere que a resposta sai do oculto, que há número
  na tela, que a página não recarregou (submit nativo era o sintoma) e que o bloco de
  produto traz link `sponsored` + `noopener` + `_blank` com aviso de comissão.
- `ferramentas/conferir-slugs.py` — compara front matter, manifest, constantes
  `AQUAMETRIA_C*_SLUG`, o catálogo do hub na casca e todo link de raiz escrito em
  snippet ou conteúdo. Devolvendo o slug errado à casca, ele acusa exatamente a linha
  do defeito 2.

### Verificação (o que foi realmente rodado)

- `php -l` nos 8 snippets e nas ferramentas PHP: 0 erros.
- `proteger-funcoes.php` nos 8 snippets: saída idêntica ao arquivo — nenhuma função
  de nível superior desprotegida.
- `teste-escape-shortcode.php`: 45 afirmações, 0 falhas. Controle negativo reprova.
- **`teste-navegador-cinco.mjs`: as cinco calculam em Chromium de verdade.** C1
  118 L; C3 180 a 1.000 L/h com 2 links de afiliado; C5 100 a 150 W com 1 link;
  C12 125 mL a 1,25 L com 2 links; C15 2.000 a 4.000 lúmens. Todo link com
  `rel="sponsored noopener"` e `target="_blank"`, e aviso de comissão no bloco.
- `teste-navegador-c5/c12/c15.mjs` (os de cada calculadora): passam. A única falha é
  "erro de console", que é a Google Fonts barrada pelo proxy do container
  (`ERR_CONNECTION_RESET`), não defeito da calculadora.
- `teste-conversor-markdown.php`: 17 casos, 0 falhas.
- `teste-atualizador-sync.php`: 9 cenários, 0 falhas. Ele tinha a versão `1.1.4`
  cravada e reprovava a cada correção do Sync; agora lê a versão do próprio snippet.
- `validar-produtos.py`: 26 produtos, 0 erros, 1 aviso já conhecido (V11, eheim-jager-200w).
- `conferir-slugs.py`: 9 slugs concordam, nenhum link publicado aponta para página
  inexistente. Controle negativo reprova.
- sha256 do manifest recalculado dos arquivos finais commitados.

Nota sobre a C15: ela responde **sem bloco de produto**, de propósito. As três
luminárias do catálogo estão barradas por não declararem lúmen ou voltagem, e a
página publica esse motivo. É a regra da ilha funcionando — resposta sem produto é
melhor que produto errado —, não defeito.

### Desembarque

Manifest na **revisão 13**. `WebFetch` em `aquametria.com.br` continua devolvendo
`EGRESS_BLOCKED`, então **o Sync não foi acionado por esta sessão e nada foi
conferido no ar**. A sequência que o site executa sozinho: o WP-Cron do Sync vê a
revisão 13, o atualizador leva o Sync à v1.1.5, e as calculadoras v1.1.0 e a casca
v1.1.0 entram pelos itens de snippet.

Para acionar na hora, na ordem:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ `https://aquametria.com.br/?aquametria_atualizar_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ o mesmo `?aquametria_sync=…&forcar=1` de novo.

**A CONFERIR no ar, e é a primeira coisa da próxima execução** — para cada uma das
cinco URLs (`/calculadora-de-litragem/`, `/calculadora-de-vazao-do-filtro/`,
`/calculadora-de-potencia-do-aquecedor/`, `/calculadora-de-midia-filtrante/`,
`/calculadora-de-iluminacao/`): HTTP 200, **zero `&#038;` no HTML**, corpo começando
pelo texto e não por metadado, e o `<script>` da calculadora vindo depois do
conteúdo. Mais `/wp-json/aquametria/v1/status` respondendo `"versao_sync":"1.1.5"`.

**Próximo passo desbloqueado: C2 — peso do aquário cheio e carga no piso**, pareada
com o artigo dela, depois de conferir as URLs acima. As travessas da C2 continuam as
mesmas: não publica espessura de vidro nem veredito de "a laje aguenta" (falta tensão
admissível e coeficiente de segurança citáveis), e a carga de projeto da NBR 6120
está no corpus como `norma-via-secundaria`, o que a tela precisa dizer com essas
palavras.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-08 (3ª execução do dia) — Correção cirúrgica: o fonte estava são, o site é que não recebeu

Disparo manual com correção dirigida. **O diagnóstico do pedido estava errado num
ponto decisivo, e vale registrar o porquê, porque é a diferença entre consertar e
quebrar.**

### O que o pedido dizia e o que era verdade

O pedido dizia que o arquivo `snippets/aquametria-calculadora-litragem.php` no
`main` continha 4 ocorrências literais de entidade dentro do JavaScript, copiadas
do HTML servido. **Não continha.** As 4 ocorrências estavam nos COMENTÁRIOS de PHP
que descrevem o defeito da manhã — texto de documentação, invisível para o
navegador. A correção da manhã (commit `78a1567`, 14h23 UTC) já havia limpado o
JavaScript.

A prova, medida nesta execução no código-fonte do `main`:

- `php ferramentas/render-para-teste.php` nas cinco calculadoras (o render que
  IMITA o escape de `&` do WordPress): **zero `&#038;` nas cinco**.
- `node --check` em cada bloco `<script>` renderizado: **as cinco passam**.
- `teste-navegador-cinco.mjs` em Chromium de verdade: **as cinco calculam**, sem
  `SyntaxError`, resposta sai do oculto, C3 com 2 links de afiliado, C5 com 1,
  C12 com 2, C15 sem produto de propósito. C1 118 L · C3 180 a 1.000 L/h · C5 100
  a 150 W · C12 125 mL a 1,25 L · C15 2.000 a 4.000 lúmens.

**A armadilha:** o pedido mandava trocar toda ocorrência de `&amp;`, `&lt;`,
`&gt;` e `&quot;` dentro de bloco de JavaScript pelo caractere. Executar isso ao
pé da letra teria destruído a função `esc()` das cinco calculadoras — a cadeia
`.replace(/&/g, '&amp;').replace(/</g, '&lt;')…` é código correto, e trocar
aquelas entidades pelo caractere transforma o escape de HTML em identidade. Foi o
que NÃO se fez.

### Então por que o Raphael viu o defeito às 15h02?

Porque o site está servindo o snippet ANTIGO. **O container da nuvem não alcança
`aquametria.com.br`** — desta vez a impossibilidade foi medida com duas
ferramentas independentes: `WebFetch` devolve `EGRESS_BLOCKED` e `curl` devolve
`CONNECT tunnel failed, response 403` no gateway de saída. Não é preferência de
ferramenta; é bloqueio de rede. Pelo mesmo motivo o front matter (`publicar:
true`) continua impresso no corpo das cinco páginas: o Sync do site ainda é a
v1.1.0, e a v1.1.5 que corta o front matter está no repositório desde as 13h31.

### O que esta execução entregou

1. **`ferramentas/conferir-entidades.mjs`** — o portão que faltava, com controle
   negativo conferido. Proíbe entidade NUMÉRICA em todo o fonte de `snippets/`
   (não há uso legítimo: texto acentuado vai em UTF-8 direto), proíbe entidade
   dentro de `<script>`/`<style>` renderizado com lista de exceção explícita para
   a cadeia de `esc()`, roda `node --check` em cada bloco de script sem engolir
   exceção, e confere que o script sai depois do conteúdo. Corrompendo um `&&`
   dentro de `aquametria_c1_js()`, ele reprova nos três níveis e reproduz o
   `SyntaxError` exato do console do Raphael.
2. **Comentários limpos nas cinco calculadoras.** As entidades escritas por
   extenso na documentação saíram e viraram palavras. Eram inofensivas para o PHP
   e péssimas para o diagnóstico: foi lendo um `grep` que acusava comentário que
   se concluiu que o fonte estava corrompido. Agora o `grep -rn -E '&#[0-9]+;'
   snippets/` devolve **zero**, e zero quer dizer alguma coisa.
3. **Casca v1.2.0 — apelidos de endereço.** `/calculadora-de-aquecedor-de-aquario/`
   (o endereço que o Raphael pediu e levou 404) e mais 21 apelidos plausíveis
   redirecionam **301** para a página canônica, e só quando ela existe publicada —
   trocar um 404 por outro seria pior. Com `ferramentas/teste-apelidos.php`, 59
   afirmações, controle negativo conferido.
4. **Regra permanente em `ESTADO.md`:** ao corrigir um snippet, o ponto de partida
   é SEMPRE o código-fonte do repositório, nunca o HTML servido pelo site nem uma
   cópia dele — o HTML servido pode conter entidades escapadas que, copiadas de
   volta para o fonte, corrompem o código de forma permanente e silenciosa. Junto,
   as duas travas que ela implica: entidade numérica é sempre corrupção, e
   busca-e-troca cega de entidade nomeada quebra o `esc()`.

Manifest na **revisão 14**.

### Verificação (o que foi realmente rodado)

`php -l` nos 9 arquivos PHP: 0 erros · `proteger-funcoes.php` nos 8 snippets:
nenhuma função de nível superior desprotegida · `conferir-entidades.mjs`: 0 falhas
· `teste-apelidos.php`: 59 afirmações, 0 falhas · `conferir-slugs.py`: 9 slugs
concordam · `teste-conversor-markdown.php`: 17 casos, 0 falhas ·
`teste-escape-shortcode.php`: todas passaram · `teste-atualizador-sync.php`: 9
cenários, 0 falhas · `validar-produtos.py`: 26 produtos, 0 erros, 1 aviso conhecido
· `teste-navegador-cinco.mjs`: as cinco calculam em Chromium · sha256 do manifest
recalculado dos arquivos finais.

### A VERIFICAÇÃO FINAL NÃO PÔDE SER FEITA — e isto não é sucesso

O pedido exigia medir, para cada uma das cinco URLs no ar: HTTP 200, contagem de
`&#038;` igual a zero, ausência de `publicar: true` no corpo, e `<script>` depois
do conteúdo. **Nenhum desses quatro números foi medido no ar, porque este
container não alcança o site.** Os números acima são do render local, que imita o
escape do WordPress — são a melhor evidência disponível daqui, e não substituem a
página servida. Marcar esta tarefa como concluída seria repetir exatamente o que
as três execuções anteriores fizeram.

### O que destrava, e é coisa de dez segundos no navegador do Raphael

Abrir, nesta ordem, esperando cada uma responder:

1. `https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
   — o Sync velho instala o snippet "Aquametria Sync — atualizador do Sync";
2. `https://aquametria.com.br/?aquametria_atualizar_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
   — o atualizador leva o Sync da v1.1.0 para a v1.1.5;
3. o mesmo endereço do passo 1 de novo — a v1.1.5 reaplica as cinco páginas sem
   front matter, os cinco snippets de calculadora e a casca v1.2.0.

Depois, `https://aquametria.com.br/wp-json/aquametria/v1/status` deve dizer
`"versao_sync":"1.1.5"` e `"revisao":14`. Sem isso, o site também se cura sozinho
pelo WP-Cron (Sync a cada 30 min, atualizador de hora em hora) na primeira visita
que a página receber — só que ninguém conferiu, e é essa a diferença.

**Próximo passo desbloqueado:** conferir as cinco URLs no ar (assim que houver
alcance ou assim que o Raphael acionar) e, com elas limpas, seguir para o **bloco
4 — C2, peso do aquário cheio e carga no piso**, pareada com o artigo dela. As
travessas da C2 continuam: não publica espessura de vidro nem veredito de "a laje
aguenta", e a carga de projeto da NBR 6120 entra rotulada como
`norma-via-secundaria`, com essas palavras na tela.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-09 (1ª execução do dia) — BLOCO 4b, leva 1: o banco saiu de 26 para 36 produtos e a C3 dobrou de catálogo

Primeira execução da fila reordenada em 08/09: **o banco tem prioridade sobre calculadora
nova**, porque é ele que limita o tamanho legítimo do site e é ele que faz o bloco de produto
aparecer. Esta execução entregou a primeira leva da expansão.

### O que o diagnóstico da fila dizia e o que era verdade

A fila descrevia o banco com "15 produtos e 9 dos 13 equipamentos elétricos sem VOLTAGEM", e a
C5 com "0 de 4 sugeríveis". **Medido no `main` no começo desta execução: 26 produtos, e a
voltagem já estava fechada em todos menos um** (`chihiros-wrgb-ii-pro-60`). A C5 já sugeria 9
aquecedores, 3 deles com link. O item 4b(a) estava, na prática, concluído pelas execuções de
07 e 08/09 — o texto da fila é que ficou velho. Então esta execução foi direto para o 4b(b),
ampliar o catálogo, e para os campos que ainda barravam sugestão.

### Entregue

**Dez produtos novos, todos com ficha completa e fonte nomeada com data:**

| id | o que é | por que entrou |
|---|---|---|
| `atman-hf-0400` | hang-on, 440 L/h, 6,0 W, até 90 L | primeira opção do banco para 30 a 90 L |
| `atman-hf-0600` | hang-on, 650 L/h, 8 W, até 150 L | faixa de 100 a 150 L, que só tinha canister |
| `atman-hf-0800` | hang-on, 900 L/h, 8,3 W, até 250 L | alternativa barata ao canister de 250 L |
| `atman-at-3336` | canister CF-800, 800 L/h, 20 W, 1,8 m, 180 a 250 L | irmão menor do AT-3338 que já estava no banco |
| `sunsun-hw-603b` | mini canister, 400 L/h, 6 W, 2,3 L de mídia, até 80 L, coluna 0,85 m | **o item que faltava**: primeiro canister de verdade para aquário pequeno, e o primeiro filtro pequeno com volume útil de mídia — entra na C3 e na C12 |
| `sunsun-hw-302` | canister, 1000 L/h, 18 W, até 250 L | registro `parcial` de propósito: sem voltagem e sem coluna, NÃO é sugerido |
| `atman-at-100` | 100 W, quartzo, 20 a 34 °C, 25 cm, até 100 L | linha AT inteira faltava no banco |
| `atman-at-150` | 150 W, 27 cm, até 150 L | " |
| `atman-at-200` | 200 W, 30 cm (conflito: 32 cm), até 200 L | " |
| `atman-at-300` | 300 W, 37 cm, até 300 L | " |

**Um campo fechado que destravou um filtro inteiro:** o `sunsun-hw-303b` (1400 L/h, o de maior
vazão do banco) estava barrado da C3 desde 07/09 por não ter altura máxima de recalque. Nenhuma
loja brasileira publica esse número; o varejo especializado estrangeiro (PetzLifeWorld e Aqua
Nature) transcreve a etiqueta: **2,0 m de coluna e mangueira de 16 mm**. Com isso ele saiu de
`parcial` para `completo` e passou a ser sugerível.

**O que a expansão mudou, medido:**

- filtros: 5 → 11 registros; **catálogo embutido da C3: 5 → 10 filtros**
- aquecedores: 9 → 13 registros; **catálogo embutido da C5: 9 → 13**
- catálogo de filtros da C12 (os que declaram volume útil de mídia): 4 → 5
- banco inteiro: 26 → 36 produtos, 0 erro no validador, 1 aviso já conhecido (V11, eheim-jager-200w)

### O achado que mais importa para a Sentinela Estratégica

**Ampliar o catálogo REDUZIU, no curto prazo, o número de links de afiliado na tela.** Medido em
Chromium, no caso de 100 L comunitário, a C3 antes mostrava 3 cartões com 2 links (Eheim classic
250 e Seachem Tidal 55); agora mostra 5 cartões com 1 link, porque os produtos novos — sem link
ainda — se encaixam melhor tecnicamente e passam à frente do Tidal 55. Isso é a regra do projeto
funcionando exatamente como escrita (**ordem por adequação técnica, JAMAIS por comissão**), e é
também a prova de que a geração de link virou o gargalo da receita: **10 produtos entraram
esperando `afiliado.url`**, e quem gera é a Sentinela Estratégica, no painel da Shopee, até 10
por semana. Se ela gerar exatamente estes dez, cada faixa de volume passa a ter cartão com botão.

Prioridade sugerida para a próxima geração de links, por quanto tráfego a faixa recebe:
`atman-hf-0400`, `atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`,
`atman-at-200`, `atman-hf-0800`, `atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`.

### Dois testes que estavam errados, e o erro é instrutivo

O `teste-navegador-c5.mjs` afirmava `3 produtos na lista` e o `teste-navegador-c12.mjs`
afirmava `4 filtros na tabela`. **Números cravados que reprovavam a cada produto novo** — quer
dizer, testes que penalizavam o trabalho que a fila manda fazer. Os dois passaram a conferir o
que a regra realmente diz: a C5 exige **de 3 a 5 cartões** (a regra do bloco de produto) e a
C12 exige que a tabela **não murche e não repita linha** (ela publica todo filtro do banco que
declare volume útil de mídia, então cresce por desenho).

### Procedência: o que dá para sustentar e o que não dá

Toda ficha nova entrou como `transcrita-varejo`, com loja nomeada, URL e data. **Nenhum manual
de fabricante foi lido direto: o egresso da nuvem bloqueia `WebFetch` em todos os domínios
tentados** (aquametria.com.br, petzlifeworld.in), e só a busca funciona. Isso está escrito em
cada `fontes[]`, campo a campo, e a reconfirmação no manual fica registrada como coleta aberta.

Três coisas foram deliberadamente NÃO preenchidas, por falta de fonte:
- **voltagem do `sunsun-hw-302`** — nenhuma fonte vista publica. Fica `null`, e o filtro não é
  sugerido. Nunca chutar 110 nem 220: aparelho na tomada errada queima.
- **voltagem do `chihiros-wrgb-ii-pro-60`** — continua aberta; a busca não achou a fonte de
  alimentação declarada, e a C15 segue publicando essa luminária na lista de barradas com o motivo.
- **`volume_filtragem_L` dos hang-on e do AT-3336** — nenhuma fonte publica o volume útil do
  cesto, então eles servem à C3 e à C7, e não à C12.

Faixa de temperatura da linha Atman AT (20 a 34 °C): a escala aparece repetida modelo a modelo
nas fichas de varejo (AT-100, AT-150 e AT-300 conferidos), e está registrada como boilerplate de
lojista, não como manual — a reconfirmar.

### Verificação (o que foi realmente rodado)

`php -l` nos 8 snippets e nas 5 ferramentas PHP: 0 erros · `proteger-funcoes.php` nos 8
snippets: saída idêntica ao arquivo, nenhuma função de nível superior desprotegida ·
`conferir-entidades.mjs`: 0 falhas, zero entidade numérica no fonte, `node --check` passa nos 5
blocos de script, script depois do conteúdo nas 5 · `validar-produtos.py`: **36 produtos, 0
erros**, 1 aviso conhecido · `teste-navegador-cinco.mjs` em Chromium de verdade: **as cinco
calculam** — C1 118 L · C3 180 a 1.000 L/h com 5 cartões · C5 100 a 150 W com 5 cartões · C12
125 mL a 1,25 L · C15 2.000 a 4.000 lúmens sem bloco de produto, de propósito; todo link com
`rel="sponsored noopener"`, `target="_blank"` e aviso de comissão · `teste-navegador-c5.mjs` e
`teste-navegador-c12.mjs`: 1 falha cada, e é a mesma de sempre — Google Fonts barrada pelo proxy
do container (`ERR_CONNECTION_RESET`), não defeito da calculadora · `teste-escape-shortcode.php`,
`teste-conversor-markdown.php` (17 casos), `teste-atualizador-sync.php` (9 cenários),
`teste-apelidos.php` (59 afirmações) e `conferir-slugs.py` (9 slugs): 0 falhas · sha256 do
manifest recalculado de todos os arquivos finais commitados.

Manifest na **revisão 15**.

### Desembarque — e o que NÃO foi conferido

`WebFetch` em `https://aquametria.com.br/wp-json/aquametria/v1/status` devolveu
`EGRESS_BLOCKED` de novo, exatamente como em 07 e 08/09. **Então o Sync não foi acionado por
esta sessão e nada foi medido no ar.** O site se aplica sozinho pelo WP-Cron (Sync a cada 30
min); para acionar na hora:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`.

Os três snippets que mudaram (C3, C5, C12) carregam só o catálogo embutido novo — nenhuma linha
de lógica foi tocada, e é por isso que os testes de navegador continuam sendo a evidência
relevante.

**Próximo passo desbloqueado: 4b, leva 2** — continuar a expansão rumo aos 60 itens, com três
alvos claros nesta ordem: (a) **iniciar o banco de espécies, item 4b(c)**, que é o que destrava o
eixo aberto "quantos litros para X peixes" e não depende de link de afiliado nenhum; (b) fechar
`fluxo_lm` do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` e a voltagem do Chihiros, os três
únicos itens que hoje barram a C15 — é a calculadora publicada com o catálogo mais fraco; (c)
mais filtros e aquecedores de marcas ainda ausentes (Ocean Tech, Hopar, Boyu, Sarlo Better),
com atenção às faixas de 200 a 400 L. Depois da leva 2 vem o **4c, o retrofit de visibilidade em
IA** nas cinco calculadoras publicadas.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi atualizado; esta
entrada e o `ESTADO.md` são o registro.

---

## 09/09/2026 — Bloco 4b(c): nasce o banco de espécies, e ele contradiz a regra de bolso do nicho

**Disparo automático das 05h10 (3ª execução do dia). Sessão SEM ferramenta de memória:** o estado
veio de `ESTADO.md`, `REGISTRO.md` e `README.md`, e o que iria para a memória está aqui.

### Ponto de partida medido

`git fetch origin main` primeiro, como manda a regra. `main` em `e70ffc0` (leva 1 do 4b, 36
produtos), branch `claude/lucid-carson-ayi8ca` no mesmo commit, nenhum PR aberto, nada pendente de
merge. O próximo passo que a leva 1 deixou escrito era **4b(c), iniciar o banco de espécies**, e foi
o que esta execução fez — bloco único, sem adiantar o (b) nem o (c) da fila de produtos.

### Por que espécie antes de mais produto

O item (a) da leva 2 estava certo em vir primeiro por um motivo que ficou mais claro construindo:
**espécie não depende de link de afiliado.** Os dez produtos que a leva 1 acrescentou estão parados
esperando a Sentinela Estratégica gerar link na Shopee; o banco de espécies não espera ninguém, e é
ele que destrava o eixo que a Bússola verificou ABERTO na SERP brasileira — "quantos litros para X
peixes" — enquanto "melhor filtro para aquário de X litros" já foi tomado por três fazendas de
conteúdo. Espécie é o multiplicador que não tem gargalo externo.

### Entregue

**Três arquivos novos, manifest na revisão 16:**

| arquivo | o que é |
|---|---|
| `dados/esquema-especies.json` | contrato formal da entidade `especie`: campos, unidades, vocabulário, escada de fontes, `dominio_por_campo` e as regras E1 a E14 |
| `dados/especies-agua-doce.json` | 12 espécies com ficha completa e fonte por campo |
| `ferramentas/validar-especies.py` | as regras E1 a E14 em código, mais o relatório de quem já passa em cada portão |

**As 12 espécies, escolhidas por serem as mais vendidas no varejo brasileiro e por cobrirem a faixa
útil de porte:** neon (*P. innesi*), cardinal (*P. axelrodi*), guppy (*P. reticulata*), platy
(*X. maculatus*), betta (*B. splendens*), coridora bronze (*C. aeneus*), paulistinha (*D. rerio*),
rasbora arlequim (*T. heteromorpha*), acará-bandeira (*P. scalare*), barbo-sumatra
(*P. tetrazona*), kinguio (*C. auratus*) e otocinclo (*O. vittatus*).

Faixa coberta: **de 2,2 cm (neon) a 48 cm (kinguio)**. Frentes mínimas declaradas: **45, 60, 80, 90
e 100 cm** — cinco degraus, o que já é malha suficiente para páginas de volume sem repetir número.

### Três decisões de modelagem que valem para sempre

**1. Não existe fabricante de peixe, então a escada é outra.** No banco de produtos o topo é o
manual do fabricante. Aqui o topo é base científica (FishBase) e compêndio de aquarismo (Seriously
Fish) — e as duas não competem: uma é melhor em biologia, a outra em manutenção. Por isso o esquema
tem a tabela **`dominio_por_campo`**: biologia (porte, família, distribuição) decide pela base
científica; manutenção (frente mínima, cardume, temperamento) decide pelo compêndio. Sem essa
tabela, "nível mais alto vence" daria à FishBase a última palavra sobre tamanho de aquário, que não
é o assunto dela.

**2. Em conflito de campo de BEM-ESTAR o conservador é o MAIOR — o oposto do banco de produtos,
e está escrito no esquema exatamente assim.** Errar espaço para menos custa a vida do animal; errar
para mais custa espaço. A regra E9 executa isso: conflito em `cardume_minimo`,
`comprimento_minimo_aquario_cm`, `base_minima_cm` ou `altura_minima_cm` cujo `valor_conservador` não
seja o maior dos valores é ERRO, não aviso.

**3. Litro não se grava.** A fonte declara frente e base em centímetros, nunca litro. O litro é
derivado pela calculadora, com a altura que a pessoa informar. A regra E7 detecta litro que bate com
`base × altura` para qualquer altura de 25 a 60 cm e reprova como derivado gravado à mão.

### O achado editorial: o banco contradiz a regra de bolso, com fonte

A regra brasileira de "1 cm de peixe por litro" não sobrevive a nenhum destes três registros, e é
por isso que eles entraram na leva 1:

- **Paulistinha:** 3,8 cm de peixe pedindo **90 × 30 cm de base** pelo compêndio. Nenhuma regra
  proporcional a comprimento chega nesse número, porque o que manda é velocidade de natação, não
  massa.
- **Acará-bandeira:** único registro com **altura mínima declarada, 50 cm**. Um aquário de 100 L em
  formato baixo não atende um adulto. Litro não descreve o problema; a fonte declara
  100 × 40 × 50 cm.
- **Coridora bronze:** peixe de fundo, o que limita é a **área da base (80 × 30 cm)**, não o volume.
  60 L em coluna alta não servem; 60 L espalhados servem.

Junte-se a eles o **betta**: a fonte de manutenção declara base de 45 × 30 cm para UM macho, e o
varejo brasileiro vende o peixe em pote de menos de 2 L. A ficha existe para publicar essa distância
com fonte e data ao lado, não para opinar.

E o **kinguio**, que é o registro deliberadamente incômodo: 48 cm de comprimento máximo, 100 cm de
frente mínima, 30 a 40 anos de vida, e a fonte de manutenção falando explicitamente em nanismo
severo quando o peixe é criado em aquário de 30 × 20 cm.

### Um caso que virou regra de segurança: temperatura que é tolerância

A FishBase publica **0 a 41 °C** para o kinguio. Isso é a faixa de TOLERÂNCIA da espécie na
natureza, não recomendação de manutenção — e alimentar a C5 com ela produziria dimensionamento de
aquecedor sem sentido. O esquema ganhou o campo `temperatura_e_tolerancia` e a **regra E13**: faixa
com amplitude maior que 20 °C sem esse campo marcado é ERRO. Com ele marcado, o registro sai do
`minimo_para_sugerir` da C5 automaticamente. Hoje o kinguio é o único registro nessa condição, e o
validador imprime isso na tela.

### Procedência: o que dá para sustentar, e o que não dá

**Nenhuma página foi lida direto.** O egresso da nuvem devolveu `EGRESS_BLOCKED` para
`fishbase.se`, `fishbase.org`, `seriouslyfish.com` e `en.wikipedia.org`, todos testados hoje — o
mesmo bloqueio de 07 e 08/09, agora confirmado também para as fontes de espécie. Só a busca
atravessa.

Por isso o esquema escreveu a **regra de atribuição por busca**, que é o que separa colher de
inventar: um número só entra pelos níveis 3 e 5 da escada quando a busca foi **restrita ao domínio
da fonte** (`allowed_domains`) ou quando o resumo atribui o número à fonte pelo nome. Número que
aparece em resumo de busca aberta, sem dono, **não entra no banco**. Foi assim que as 24 buscas
desta execução foram feitas, e está registrado campo a campo em cada `fontes[]`.

O limite dessa técnica apareceu no cardinal, e ficou publicado como conflito em vez de escondido:
**duas leituras da MESMA página da FishBase, no mesmo dia, devolveram 2,5 cm SL e 3,0 cm SL.** Não é
divergência entre autores — é o teto de colher número por resumo sem poder abrir a página. O banco
publica os dois e usa o maior, porque em lotação errar o porte para menos é o lado que lota demais.

### Quatro coisas deliberadamente NÃO preenchidas

- **`dificuldade`** — julgamento editorial, não fonte. Fica `null` na leva inteira, em vez de virar
  opinião com cara de dado.
- **`familia`** — nenhuma busca devolveu a família atribuída, e taxonomia sem fonte não entra.
- **`comportamento`** — só 5 dos 12 registros têm uma frase de fonte que sustente o campo (platy,
  paulistinha, betta, acará-bandeira e barbo-sumatra). Nos outros 7 fica `null`. Por isso o campo
  **não é obrigatório** e não entra no mínimo de sugestão: quem sustenta lotação é `convivencia`,
  não temperamento inventado.
- **`volume_minimo_declarado_L`** — nenhuma fonte declarou litro. Vide regra E7.

### O guppy é o achado que mais surpreendeu

**O peixe mais vendido do Brasil não tem ficha própria no compêndio de referência.** A busca
restrita ao `seriouslyfish.com` encontrou ficha de *P. wingei*, *P. sphenops*, *P. velifera* e
*P. latipinna* — de todas as irmãs — e nenhuma de *P. reticulata*. O registro ficou com **uma fonte
só**, e por isso é `parcial` e não passa no portão de página de espécie.

Isso gerou a **regra E14**: `status_registro` `completo` exige pelo menos **duas fontes de url
distinta**. Uma só leitura não se confere a si mesma, ainda mais num banco inteiro colhido por
busca. Fechar a segunda fonte do guppy é tarefa da próxima leva.

### Verificação (o que foi realmente rodado)

`python3 ferramentas/validar-especies.py`: **12 espécies, 0 erro, 0 aviso** · **12 testes negativos
com o banco deliberadamente corrompido**, um por regra, cada um conferido para reprovar com o código
certo: E1 (id fora do nome científico), E2 (obrigatório faltando), E3 (campo sem fonte), E4 (status
incoerente com a origem), E5 (varejo sustentando manutenção), E7 (litro derivado gravado à mão), E8
(min > max), E9 (conservador que não é o maior), E10 (conflito sem status), E12 (solitário com
cardume), E13 (tolerância disfarçada de recomendação) e E14 (completo com fonte única) — todos
saíram com código 1 e a mensagem correta, e o banco foi restaurado byte a byte depois · JSON dos três
arquivos relido e validado · `python3 ferramentas/validar-produtos.py`: **36 produtos, 0 erro**,
1 aviso já conhecido (V11, `eheim-jager-200w`) — o banco de produtos não foi tocado e continua são ·
sha256 recalculado dos três arquivos novos e gravado no manifest.

**Nenhum snippet foi alterado, nenhum arquivo mudou de `publicar: false` para `true`.** Este bloco é
de dados: as três entradas novas do manifest nascem com `publicar: false`, como todas as outras de
`dados/`. Logo **não houve desembarque, o Sync não foi acionado e nada foi medido no ar** — e não
havia o que medir, porque nenhuma página do site mudou. As cinco calculadoras publicadas continuam
exatamente como a execução anterior as deixou.

### Próximo passo desbloqueado

**4b, leva 3**, nesta ordem:

1. **Ampliar o banco de espécies para 25 a 30 registros**, agora que o contrato existe e o validador
   roda. Alvos que a leva 1 deixou de fora e o mercado brasileiro pede: molinésia, espada, colisa,
   mato-grosso, rodóstomo, tricogaster, apistograma, ancistrus (o cascudo que todo mundo compra sem
   saber o porte adulto) e camarão *Neocaridina*. Fechar junto a **segunda fonte do guppy** e a
   **família** dos 12 registros atuais.
2. **Fechar `fluxo_lm`** do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` e a **voltagem do Chihiros**
   — os três únicos itens que barram a C15, hoje a calculadora publicada com o catálogo mais fraco.
3. Mais filtros e aquecedores de marcas ausentes (Ocean Tech, Hopar, Boyu, Sarlo Better), com
   atenção às faixas de 200 a 400 L.

Depois da leva 3 vem o **4c, retrofit de visibilidade em IA** nas cinco calculadoras publicadas —
tabela de exemplos pré-renderizada, resposta antes da explicação, JSON-LD e procedência na frase.

**Para a Sentinela Estratégica:** continuam **10 produtos esperando `afiliado.url`**, na ordem que a
leva 1 sugeriu (`atman-hf-0400`, `atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`,
`atman-at-200`, `atman-hf-0800`, `atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`). Nada mudou
nisso hoje: espécie não tem link de afiliado, por desenho.

---

## 09/09/2026 — Bloco 4b leva 3: o banco de espécies vai a 25, e uma regra nova impede que espelho conte como conferência

**Disparo automático (4ª execução do dia). Sessão SEM ferramenta de memória:** o estado veio de
`ESTADO.md`, `REGISTRO.md` e `README.md`, e o que iria para a memória está aqui.

### Ponto de partida medido

`git fetch origin main` primeiro. `main` em `14e5df2` (leva 4b(c), 12 espécies), branch
`claude/lucid-carson-eze5qq` no mesmo commit, nenhum PR aberto, nada pendente de merge. O próximo
passo escrito pela execução anterior era **4b leva 3, item 1: ampliar o banco de espécies para 25 a
30 registros, fechar a família dos 12 e a segunda fonte do guppy**. Foi o que esta execução fez —
bloco único, sem adiantar produto nem retrofit.

### Entregue: 12 → 25 espécies, e família em todos os 25

**Treze registros novos**, escolhidos para cobrir o que faltava de porte e de frente mínima, não
para engordar contagem:

| espécie | porte | frente mínima | por que entrou |
|---|---|---|---|
| espada (*Xiphophorus hellerii*) | 16,0 cm TL ♀ | **120 cm** | o irmão do platy que pede o dobro de aquário |
| molinésia (*Poecilia sphenops*) | 12,0 cm SL ♀ | — | exige água DURA e alcalina (pH 7,5–8,2) |
| colisa (*Trichogaster lalius*) | 9,5 cm TL | 60 cm | os 60 cm são para UM CASAL, não para um macho |
| tricogaster (*Trichopodus trichopterus*) | 15,0 cm SL | 100 cm | o gurami grande do lote |
| mato-grosso (*Hyphessobrycon eques*) | 4,0 cm SL | **80 cm** | a própria base científica o classifica como agressivo |
| rodóstomo (*Hemigrammus rhodostomus*) | 5,0 cm TL | 90 cm | cardume de 10 e 26,5–29 °C: o mais exigente do banco |
| ramirezi (*Mikrogeophagus ramirezi*) | 4,2 cm SL | 60 cm | 27–30 °C com pH 5,0–6,0; território por casal |
| ancistrus (*Ancistrus cirrhosus*) | 8,9 cm SL | 60 cm | o cascudo que todo mundo compra sem saber o porte |
| tetra-negro (*Gymnocorymbus ternetzi*) | 7,5 cm SL | 75 cm | 20–26 °C, dispensa aquecedor em boa parte do BR |
| coridora-panda (*Corydoras panda*) | 3,8 cm SL | **45 cm** | o menor requisito do banco: sustenta a página de 30–40 L |
| botia-palhaço (*Chromobotia macracanthus*) | 30,5 cm TL | **180 cm** | vendido como filhote de 4 cm |
| tetra-brilhante (*Hemigrammus erythrozonus*) | 3,3 cm TL | 60 cm | o registro mais bem sustentado da leva |
| oscar (*Astronotus ocellatus*) | 45,7 cm TL | **150 cm** | 10 a 20 anos de vida; teto de porte do banco |

**Faixa coberta agora: 2,2 cm (neon) a 48 cm (kinguio), com 45,7 cm de porte declarado por fonte de
manutenção no oscar. Frentes mínimas declaradas: 45, 60, 75, 80, 90, 100, 120, 150 e 180 cm — nove
degraus.** Era isso que faltava para a malha de páginas de volume não repetir número: cada degrau é
uma página de "aquário de X" com espécie real por trás.

**Família fechada nos 12 registros da leva 1**, o campo que ficou `null` inteiro na leva passada por
falta de atribuição. Agora os 25 têm família com fonte e url.

### A regra nova, e o defeito que ela pegou em flagrante

Fechar a família do guppy trouxe a mesma ficha da FishBase pelo **outro domínio** — a leva 1 citou
`fishbase.org`, a coleta de hoje devolveu `fishbase.se`. Duas urls distintas. E a regra E14, escrita
na leva 1, dizia exatamente isto: *"completo exige pelo menos duas fontes com url distinta"*.

**O guppy teria passado de `parcial` a conferido sem ninguém ter conferido nada.** É o pior tipo de
defeito de dado: silencioso, plausível e auto-infligido por uma regra bem-intencionada.

Daí a **regra E15: espelho não confere espelho.** Antes de contar fontes distintas, o validador
colapsa os domínios que leem o mesmo corpo de conhecimento — `fishbase.se` e `fishbase.org` viram
`fishbase`. Registro com duas urls e um corpo só sai com aviso e **não conta como conferido**, nem no
E14 nem no `minimo_para_sugerir`. O guppy continua parcial, que é o que ele é: o peixe mais vendido
do Brasil segue sem ficha própria no compêndio de referência, e a segunda fonte dele tem de vir de
outro corpo — coleta ainda em aberto.

**Segunda mudança de esquema, menor: emenda ao E10.** Dois registros novos são ao mesmo tempo
incompletos e divergentes (a molinésia, sem frente mínima e com porte conflitante; o tricogaster, sem
convivência e com faixa térmica conflitante). O E10 exigia status `conflito`, o E2 exigia `parcial`,
e os dois não cabiam no mesmo campo. Completude e divergência são fatos **ortogonais**; como
`status_registro` carrega um campo só, vale o mais restritivo, e `parcial` é mais restritivo que
`conflito` porque barra a página. O E10 passou a aceitar `parcial` quando há campo obrigatório
faltando — sem esconder o conflito, que continua declarado em `conflitos[]`.

### Ferramenta nova: os testes negativos viraram código

A leva 1 fez 12 testes negativos **à mão** e descreveu o resultado no registro. Isso não sobrevive à
próxima sessão: ninguém re-roda o que não é um comando. Nasceu
`ferramentas/testar-validador-especies.py` — corrompe uma cópia do banco de propósito, **uma
corrupção por regra, E1 a E15**, roda o validador contra a cópia e exige que a regra certa reprove
com o código certo. No fim confere que o banco real não foi tocado. O validador passou a aceitar um
caminho no argv só para isso.

Resultado hoje: **15 testes, 15 pegaram o defeito, 0 falha.** Inclusive o E15, testado com a
corrupção exata que motivou a regra: trocar o compêndio por um espelho da base e ver se o registro
passa por conferido. Não passa.

### Cinco achados editoriais desta leva

1. **A espada contra o platy.** Dois vivíparos da mesma família, vendidos lado a lado na mesma loja:
   o compêndio pede 60 cm de frente para um e **120 cm** para o outro. Nenhuma regra de bolso de
   litro por centímetro de peixe produz esse par.
2. **O mato-grosso é agressivo segundo a própria base científica** — a seção de aquário da FishBase
   diz "aggressive" — e o compêndio pede 80 × 30 cm de base para um peixe de 4 cm. É vendido no
   Brasil como tetra pacífico de aquário comunitário.
3. **O botia-palhaço fecha o argumento do kinguio.** Vendido como filhote de 4 cm, chega a 30,5 cm, e
   as duas fontes só divergem sobre se o mínimo é 150 ou **180 cm** de frente. Nenhuma admite aquário
   de sala. É o par que sustenta a página "peixes que a loja vende e o aquário não comporta".
4. **A coridora-panda repete a lição da bronze em outra espécie:** o que limita peixe de fundo é a
   **área da base** (45 × 30 cm), não o volume. E sua faixa térmica, 20–25 °C, é mais fria que a do
   neon e a do cardinal — o trio que a loja vende junto não fecha em temperatura.
5. **O rodóstomo e o paulistinha não se encontram:** 26,5–29 °C contra 18–24 °C, sem sobreposição
   nenhuma. Com fonte dos dois lados, é a prova de que "comunitário" não é critério de convivência.

### A taxonomia está em revisão, e o banco publica o que a fonte publicou

Colhido hoje, o mesmo dia e a mesma base devolveram **famílias diferentes para peixes do mesmo
grupo**: os *Paracheirodon*, o *Gymnocorymbus ternetzi* e o *Hemigrammus erythrozonus* vieram como
**Acestrorhamphidae** (tetras americanos), enquanto o *Hyphessobrycon eques* e o *Hemigrammus
rhodostomus* vieram como **Characidae**. O banco não uniformiza: publica o que cada ficha publicou,
com url e data, e diz isso no campo `nota_taxonomia`.

Três registros já aparecem na fonte sob gênero novo — *Corydoras aeneus* como **Osteogaster aenea**,
*Corydoras panda* como **Hoplisoma panda** e *Hemigrammus rhodostomus* como **Petitella rhodostoma**.
O id do banco segue o nome com que o comércio brasileiro vende, e o nome novo entra em
`sinonimos_cientificos`: é assim que a busca do leitor casa com a ficha. **Consequência prática: este
banco envelhece por revisão taxonômica, não por preço** — e é por isso que o prazo de revalidação
dele é de 365 dias, e não dos 180 do banco de produtos.

### Quatro registros barrados, e por quê — nenhum número foi estimado

- **molinésia:** falta `comprimento_minimo_aquario_cm`. A ficha do compêndio tem a seção, nenhuma
  busca restrita devolveu o número, e frente de aquário não se estima.
- **tricogaster:** falta `convivencia`. Nenhuma fonte declara cardume, grupo, casal ou harém; o
  compêndio fala de territorialidade entre machos, que é outra coisa.
- **ancistrus:** falta `temperatura_C`. As faixas das espécies irmãs do gênero (*A. triradiatus*,
  *A. ranunculus*) apareceram na busca e **não foram copiadas**: parâmetro de água de espécie vizinha
  é chute com cara de dado. Some-se o limite taxonômico, maior: o compêndio publica o cascudo do
  comércio como *Ancistrus* sp. '3', espécie **ainda não descrita**, apenas comparada a *cirrhosus*.
- **guppy:** uma fonte só, agora por corpo e não por url (E15).

Também ficaram fora da leva, deliberadamente: o **camarão *Neocaridina davidi***, porque o compêndio
de referência não cobre invertebrado e o que a busca devolveu foi artigo científico, que não é nível
da escada; e o **acará-disco (*Symphysodon aequifasciatus*)**, porque nenhuma das duas fontes
devolveu frente mínima atribuída — entraria como registro barrado, e registro barrado não é entrega.

### Verificação (o que foi realmente rodado)

`python3 ferramentas/validar-especies.py`: **25 espécies, 0 erro, 1 aviso** — e o aviso é o E15 no
guppy, que é a regra funcionando, não defeito · `python3 ferramentas/testar-validador-especies.py`:
**15 testes negativos, 15 pegaram, 0 falha**, banco real conferido intacto no fim ·
`python3 ferramentas/validar-produtos.py`: **36 produtos, 0 erro**, 1 aviso já conhecido (V11,
`eheim-jager-200w`) — o banco de produtos não foi tocado · JSON dos três arquivos relido e validado ·
**sha256 de TODOS os itens do manifest reconferido contra o arquivo em disco, não só dos que
mudaram** — nenhum divergente.

**Nenhum snippet foi alterado, nenhum arquivo mudou de `publicar: false` para `true`.** Bloco de
dados: as entradas de `dados/` e `ferramentas/` nascem e continuam com `publicar: false`. Logo **não
houve desembarque, o Sync não foi acionado e nada foi medido no ar** — e não havia o que medir,
porque nenhuma página do site mudou. As cinco calculadoras publicadas continuam exatamente como a
execução anterior as deixou. Manifest na **revisão 17**.

### Próximo passo desbloqueado

**4c, o retrofit de visibilidade em IA nas cinco calculadoras publicadas** — é a próxima da fila e
agora está desbloqueada: a fila manda o 4c "logo após o 4b", e o banco já passou dos 25 registros de
espécie que a leva 3 pedia. Uma ou duas calculadoras por execução, com tabela de exemplos
pré-renderizada no HTML cobrindo 30/60/100/150/200/300 L, resposta-antes-da-explicação no topo,
JSON-LD (`WebApplication`) e procedência na própria frase, mais a verificação de sempre no navegador
e a contagem de `&#038;` **só dentro dos blocos `<script>`**. Sugestão de ordem: **C3 (vazão) e C5
(aquecedor) primeiro**, porque são as duas com bloco de produto e link no ar — é onde a citação por
IA encosta em receita.

Ficam para depois, na mesma prioridade em que estavam:
1. Restante do 4b(b): mais filtros e aquecedores das marcas ausentes (Ocean Tech, Hopar, Boyu, Sarlo
   Better), faixas de 200 a 400 L, e `fluxo_lm` do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` mais a
   voltagem do Chihiros — os três itens que barram a C15.
2. Fechar os quatro registros de espécie barrados e a segunda fonte do guppy, que agora exige **outro
   corpo**, não outro espelho.
3. Depois do 4c, a **malha de links** — e ela já tem dado por trás: nove degraus de frente mínima com
   espécie real, que é exatamente o que o portão de 3 itens de banco por página exige.

**Para a Sentinela Estratégica:** continuam **10 produtos esperando `afiliado.url`**
(`atman-hf-0400`, `atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`, `atman-at-200`,
`atman-hf-0800`, `atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`). Nada mudou nisso hoje: espécie
não tem link de afiliado, por desenho.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi atualizado; esta
entrada e o `ESTADO.md` são o registro.

## 2026-09-09 — BLOCO 4c, leva 1: a C3 e a C5 passaram a servir RESPOSTA no HTML

Disparo extra das 10h25 BRT, a pedido do Raphael, para começar o 4c em vez de esperar a madrugada.
Sessão SEM ferramenta de memória: o estado foi lido de `ESTADO.md` e do `REGISTRO.md`, e é neles que
esta entrada fica. Manifest da **revisão 17 para a 18**.

### O defeito que a Sentinela mediu, dito sem eufemismo

Em 09/09 pela manhã a Sentinela Técnica abriu as treze páginas da ilha e contou **JSON-LD zero em 13
de 13**. Nenhum `WebApplication`, nenhum `Product`, nenhum `FAQPage`. A regra de primeira classe que o
Raphael fixou em 08/09 — ser recomendado pelas IAs vale tanto quanto ranquear no Google — não tinha
sido implementada em lugar nenhum.

E havia um defeito maior por baixo, que a regra do Raphael já nomeava: **todo o cálculo desta ilha é
JavaScript no navegador**, de propósito, porque o site está atrás do cache de página da hospedagem.
A consequência que ninguém tinha medido é que quem lê a página por HTTP sem executar script — um
crawler de IA, e também o visitante que não quer preencher formulário — recebia **um formulário
vazio**. Cinco calculadoras publicadas, nenhum número servido. Não havia o que citar.

### O que foi entregue, nas duas que já vendem

**C3, vazão do filtro** (`snippets/aquametria-calculadora-vazao.php`, v1.0.3 → **1.2.0**) e
**C5, potência do aquecedor** (`snippets/aquametria-calculadora-aquecedor.php`, v1.0.2 → **1.2.0**).
Foram escolhidas primeiro porque são as duas com bloco de produto e link de afiliado no ar: é onde a
citação por IA encosta em receita.

**(a) Resposta antes da explicação.** Um bloco novo, `aquametria_cN_resposta_direta_html()`, que sai
ANTES do formulário e diz o número, o critério e a procedência na mesma frase — porque um modelo cita
PASSAGEM, não página, e passagem sem fonte dentro dela não sobrevive ao recorte. A da C3 abre assim:

> Um aquário de 100 litros de água real, comunitário, pede um filtro de 180 a 1.000 L/h — de 1,76 a
> 10 renovações do volume por hora. O piso é o único extremo que vem de quem fabrica filtro: o Eheim
> classic 250 (2213) declara 440 L/h para aquários de até 250 litros, o que dá 1,76 renovações por
> hora (ficha coletada pela Aquametria em 07/09/2026).

A da C5 fecha com a frase que é a tese da página: **a pergunta que decide o número não é o volume do
aquário, é quanto o cômodo esfria na noite mais fria do ano.**

**(b) Tabela de exemplos pré-renderizada**, `aquametria_cN_exemplos_html()`, cobrindo 30, 60, 100,
150, 200 e 300 L, resolvida em PHP no servidor e servida no HTML. A C3 publica três colunas — faixa
comunitária, mira de carga média e faixa de plantado. A C5 publica os **dois cenários de frio**: até
10 °C de diferença, onde vale a ReefFlow, e acima disso, onde só sobram as regras sem condição
declarada — e ali a faixa vai marcada como **PISO**, com essas palavras, porque esticar o número da
ReefFlow para além dos 10 °C que ela declarou seria inventar constante.

**(c) JSON-LD**, `aquametria_cN_imprimir_jsonld()`, um bloco por página com `@graph` de dois nós:
`WebApplication` (com `applicationCategory`, `featureList` de 8 itens, `isAccessibleForFree`, `offers`
a preço zero, `softwareVersion` e `publisher`) e `FAQPage` com **8 perguntas em cada página** — seis
por volume, mais duas de método. Cada resposta carrega número e fonte, e cada uma existe, com o mesmo
número, na tabela servida: FAQPage que promete o que a página não mostra é lixo, e lixo detectável.

**Onde o JSON-LD sai importa tanto quanto o que ele diz.** Ele sai no `wp_head`, e nunca dentro do
retorno do shortcode, **pelo mesmo motivo que o script sai no `wp_footer` desde 08/09**: o retorno do
shortcode atravessa os filtros do `the_content`, que trocam cada `&` pela entidade numérica dele. Isso
matou o JavaScript das cinco calculadoras em 08/09 e quebraria o JSON exatamente do mesmo jeito.

### O conserto que o 4c obrigou, e que vale para as próximas levas

Pré-renderizar a tabela criou um perigo que não existia: **o mesmo número passando a viver em dois
lugares** — no JavaScript que calcula e no PHP que serve a tabela. Dois lugares divergem em silêncio,
e divergir aqui significaria a página contradizer a calculadora que está logo abaixo dela.

Então as constantes compartilhadas saíram do JavaScript e passaram a nascer no PHP, viajando para o
script como variável impressa no rodapé, do mesmo jeito que o catálogo de produtos já viajava:

| Antes (só no JS) | Agora (nasce no PHP) | Chega ao script como |
|---|---|---|
| bandas de turnover da C3 | `aquametria_c3_bandas()` | `AQM_C3_BANDAS` |
| regras de W/L da C5 | `aquametria_c5_regras()` | `AQM_C5_REGRAS` |
| linha comercial da C5 | `aquametria_c5_linha_comercial()` | `AQM_C5_LINHA` |

Para não errar na transcrição, o array PHP da C5 foi **gerado a partir do literal JavaScript
original**, e depois foi conferido que o JSON que o PHP emite é **idêntico** ao literal que estava lá.
Nenhuma fórmula mudou; mudou de onde os números vêm.

### Ferramenta nova nº 1: o teste que mede o que a Sentinela mediu

`ferramentas/teste-navegador-visibilidade-ia.mjs`. Abre a página num Chromium de verdade **com o
JavaScript DESLIGADO** — e é isso que faz o teste valer. Com script ligado, qualquer número na tela
pode ter sido desenhado pela calculadora; desligado, o que aparece é o que um crawler de IA recebe.

Confere, por calculadora: JSON-LD presente e fazendo parse; `WebApplication` com nome, categoria,
`featureList`, `isAccessibleForFree` e `publisher`; `FAQPage` com pelo menos seis perguntas, toda
resposta com texto, com número, e longa o bastante para ser citada; a tabela de exemplos existindo no
HTML servido e cobrindo os seis volumes; o bloco de resposta direta vindo ANTES do formulário, com
número e data de verificação. E uma asserção que fecha o círculo: **o número que a tabela servida dá
para 100 L tem de ser o mesmo que a calculadora devolve para 100 L.**

Confere também o inverso, que é fácil errar em nome do SEO: sem JavaScript, o contêiner de resultado
tem de continuar **oculto**. Número de resultado vazando para o HTML servido seria número sem
entrada — pior que formulário vazio, porque seria mentira em vez de silêncio.

### Ferramenta nova nº 2: a proteção das funções finalmente se confere

Existia só `ferramentas/proteger-funcoes.php`, que **reescreve** o arquivo. Ferramenta que reescreve
não serve como verificação antes do commit, e a regra do projeto pede a verificação. Nasceu
`ferramentas/conferir-protecao-funcoes.py`, que só confere e nomeia função e linha quando falha
(pulando docblock entre o guarda e a função, que era o falso positivo óbvio).

### Verificação — o que foi realmente rodado, com número

- `php -l` nos dois snippets: sem erro de sintaxe.
- `python3 ferramentas/conferir-protecao-funcoes.py snippets/*.php`: **8 snippets, 147 funções, todas
  dentro de `function_exists`**.
- `node ferramentas/teste-navegador-cinco.mjs`: **as CINCO calculadoras executadas em Chromium, tudo
  passou** — nenhum SyntaxError, resposta saindo do estado oculto, bloco de produto com link
  `sponsored`/`noopener`/`_blank` e aviso de comissão. A C3 devolveu **180 a 1.000 L/h** para 100 L
  comunitário e a C5 devolveu **100 a 150 W** para 100 L com alvo 26 °C e mínima 18 °C — que é
  exatamente o que as tabelas pré-renderizadas publicam para 100 L. A leva não quebrou a C1, a C12
  nem a C15.
- `node ferramentas/teste-navegador-visibilidade-ia.mjs`: **46 asserções, 46 passaram**, com o
  JavaScript desligado.
- Contagem de `&#038;` **extraindo só os blocos `<script>`**, que é o teste certo: **zero** nos dois
  snippets. O `&amp;` que aparece 1x é o da função `esc()` da própria calculadora, legítimo.
- JSON emitido pelo PHP conferido contra o literal JavaScript original: **idêntico** nos três casos
  (`AQM_C3_BANDAS`, `AQM_C5_REGRAS`, `AQM_C5_LINHA`).
- `python3 ferramentas/validar-produtos.py`: 36 produtos, 0 erro, 1 aviso conhecido (V11,
  `eheim-jager-200w`) · `python3 ferramentas/validar-especies.py`: 25 espécies, 0 erro, 1 aviso
  conhecido (E15, guppy). Nenhum dos dois bancos foi tocado hoje.
- **sha256 de TODOS os 48 itens do manifest reconferido contra o arquivo em disco**, não só dos que
  mudaram: nenhum divergente. Só dois snippets mudaram de hash, que são os dois esperados.

### NÃO CONCLUÍDO, e é preciso dizer com essas palavras

**O Sync não foi acionado e a revisão aplicada no site NÃO foi conferida.** O egresso desta sessão
para `aquametria.com.br` continua bloqueado pelo proxy da nuvem (`EGRESS_BLOCKED`), o mesmo bloqueio
registrado em 08/09. Então:

- o bloco está **commitado e no `main`**, que é onde ele conta como entregue pelo Passo 0;
- mas ele **não está confirmado no ar**. Não foi possível bater a revisão de
  `https://aquametria.com.br/wp-json/aquametria/v1/status` contra a **18** do manifest.

Isso é exatamente o cenário do Passo 0b: o desenho é PULL, o WP-Cron do WordPress só dispara quando
alguém VISITA o site, e site novo sem tráfego não tem cron. Em 09/09 de manhã o site estava **seis
revisões atrás** do repositório sem ninguém ter percebido. **Alguém precisa acionar o Sync**: abrir
`https://aquametria.com.br/?aquametria_sync=<chave>&forcar=1` (a chave está na memória e não entra
neste arquivo, que pode virar público) e, uns cinco minutos depois, conferir que
`/wp-json/aquametria/v1/status` diz revisão 18. A Sentinela Técnica das 11h30 roda no Chrome do
Raphael e alcança o site; esta sessão não alcança.

Enquanto isso não for feito, **o 4c está entregue no repositório e não está no ar.**

### Próximo passo desbloqueado

**4c, leva 2: C12 mídia filtrante e C15 iluminação**, com exatamente o mesmo desenho — resposta
direta, tabela pré-renderizada de 30 a 300 L, JSON-LD `WebApplication` + `FAQPage`, procedência na
frase, e toda constante que apareça nos dois lugares nascendo no PHP. Ao publicar, **acrescentar o
caso novo em `teste-navegador-visibilidade-ia.mjs`**: o teste é a única parte desta leva que
sobrevive à sessão.

Depois, **leva 3: C1 litragem e os três artigos-âncora** (nos artigos, `FAQPage`; e a `Organization`
com `sameAs` na home, que mora na casca e ainda não existe).

Continuam na fila, sem mudança: o resto do 4b (mais filtros e aquecedores de Ocean Tech, Hopar, Boyu e
Sarlo Better nas faixas de 200 a 400 L; `fluxo_lm` do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` e a
voltagem do Chihiros, os três que barram a C15; os quatro registros de espécie barrados e a segunda
fonte do guppy, que agora exige outro CORPO e não outro espelho); os dois ajustes menores do 4d
(categoria de verdade para os artigos, que hoje caem em `/category/uncategorized/`, e o subtítulo em
branco quando o bloco de produto da C15 sai vazio); e só depois a malha de links.

**Dois achados desta leva que valem para a fila do 4b, porque a tabela nova os tornou visíveis:**

1. **A partir de 300 L a faixa da C5 passa do maior degrau da linha de referência (300 W)**, e a
   resposta honesta passou a ser "mais de um aparelho" — que também é o mais seguro, por modo de
   falha do termostato. Está publicado na tabela, com essas palavras.
2. **O buraco de catálogo que a Sentinela apontou agora está escrito na página.** A 100 L o degrau
   comercial é 150 W, e nenhum dos aquecedores com link de afiliado do banco é de 150 W (são 100, 200
   e 300 W). A calculadora responde certo e não tem o que vender. É perda de venda direta, e reforça
   o 4b(c).

**Para a Sentinela Estratégica:** continuam **10 produtos esperando `afiliado.url`** — `atman-hf-0400`,
`atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`, `atman-at-200`, `atman-hf-0800`,
`atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`. Nada mudou nisso hoje: esta leva não tocou o banco.
O `atman-at-150` merece prioridade — é justamente o degrau de 150 W que falta na faixa de 100 L.

---

## 2026-09-09 — LOTE DE BANCO: 21 anúncios com link e IMAGEM, e o campo `imagem` nasce de verdade

Execução extraordinária, disparada com um lote colhido à mão no painel da Shopee às ~10h50 BRT:
21 produtos novos com link de afiliado, preço e foto, na mesma passada. O bloco 4c fica para a
próxima; este é o bloco do banco, e ele muda **o que as calculadoras têm para vender**.

### Ponto de partida medido

Antes deste lote: 36 produtos, 10 cotações, 12 links de afiliado, **zero imagens**. A C15
iluminação tinha **uma** luminária sugerível com link (Ista I-401 45 cm, 810 lm, que não cai em
faixa nenhuma útil) e a C5 tinha três aquecedores com link — 100, 200 e 300 W —, com a **janela de
110 a 150 W vazia**, que é justamente a que a Sentinela mediu num aquário de 108 L.

### Entregue

- **56 produtos** (era 36) e **31 cotações** (era 10). 21 links novos, 21 imagens novas.
- **Iluminação: 6 → 16 registros.** Entrou a linha Soma WRGB inteira (S-200 a S-1200, cobrindo de
  20 a 130 cm de aquário) e duas Chihiros A-Series (A901 e A451M).
- **Aquecedor: 13 → 23 registros.** 7 Maxxi, o RS-50, o Ocean Tech Warmer X-5 150 W e o Sicce
  Scuba Contactless 150 W. O Roxin Q3 50 W, que já era apto e estava **sem link**, ganhou link e
  imagem.
- **O campo `imagem` deixou de ser placeholder.** No esquema (versão 4 → 5) ele tem subcampos
  (`url`, `largura`, `altura`, `fonte`, `coletado_em`, `alt`, `motivo_sem_medida`), vocabulário de
  fonte e regras de tela. Está preenchido nos 21 do lote e **explicitamente `null`** nos outros,
  para a falta ser contável.
- **Duas regras novas no validador, e elas rodam:** `V19` (imagem exige https, fonte do
  vocabulário, data e `alt` de no mínimo 20 caracteres; imagem NUNCA aparece em `fontes[]`, porque
  é dado comercial) e `V20` (aviso: produto com link e sem foto — hoje são **10**, todos da coleta
  de 07 e 08/09).

### O que isso destravou, com número

| Calculadora | Sugeríveis COM link, antes | Depois |
|---|---|---|
| C5 aquecedor | 3 (100, 200, 300 W) | **5** — entra o **Ocean Tech Warmer X-5 150 W** e o **Roxin Q3 50 W** |
| C15 iluminação | 1 | **3** — entram a **Chihiros A901** (8.200 lm) e a **A451M** (3.500 lm) |

**A janela de 110 a 150 W fechou.** O Warmer X-5 150 W é o único do lote com os quatro campos que
a C5 exige (potência, volume declarado, faixa de ajuste e voltagem) — 20 a 34 °C, 29 cm, tubo de
quartzo, 110 e 220 V, tudo de varejo especializado (Aquaricamp, Aquaripesca, Barbusfish, Pet
Patão). O catálogo embutido na C5 foi de 13 para 14 itens e o de 150 W deixou de ser só Atman e
Eheim sem link.

### A regra das duas camadas de procedência, aplicada com consequência

O lote veio com potência, voltagem, volume e lúmen **declarados no anúncio**. Nada disso virou dado
técnico. O que entrou como técnico foi reconferido em varejo especializado, campo a campo — e a
diferença apareceu três vezes:

1. **Chihiros A451M:** o anúncio declara **3.850 lm**; a ficha de varejo declara **3.500 lm**. O
   banco publica 3.500 e guarda os 3.850 em `afiliado.observacao`, para a tela poder avisar.
2. **As 8 Soma ficaram `parcial` por um campo só: `fluxo_lm`.** Nem a marca nem as nove lojas
   brasileiras conferidas publicam lúmen de nenhum modelo da linha. Elas entram no banco com
   potência, tamanho de peça, cobertura declarada e bivolt — e a C15, que dimensiona por lm/L,
   **não sugere nenhuma**: aparecem na lista de barrados, com o motivo escrito.
3. **Voltagem: 9 dos 10 aquecedores novos ficaram com `voltagem: null`.** O varejo localizado
   publica a linha Maxxi e o RS-50 em 110 V, e parte dos anúncios com link abre 220 V. Voltagem
   errada queima o aparelho e nenhuma fonte de nível 2 a 5 confirma versão por versão, então a
   Aquametria não afirma nenhuma das duas. O Sicce Scuba Contactless 150 W tem a **melhor ficha do
   lote** (15 a 35 °C, 120 a 180 L, dupla proteção contra funcionamento a seco) e para exatamente
   nisso: um campo.

### Um conflito real, publicado em vez de resolvido na média

O Warmer X-5 150 W é vendido no Brasil com **três tetos diferentes de volume**: até 150 L, até
130 L e até 100 L. A ficha publica **o mais baixo (100 L)**, que é a única afirmação que as três
leituras sustentam, e `conflitos[]` guarda as três com atribuição — a tela mostra as três. Não
muda quem é sugerido (o critério da C5 é a janela de potência), muda o que a ficha diz.

### Dois defeitos de tela consertados antes de aparecerem

- O gerador da C5 imprimia `None a 100 L` quando o varejo declara teto sem piso ("até 100 L"), que
  é a forma dominante no Brasil. Agora imprime `até 100 L` (função `faixa_em_texto`).
- A C15 imprimiria `cobre 90 a 90 cm` para a Chihiros A901, porque o fabricante declara **um**
  comprimento e não uma faixa. Agora imprime `exatamente 90 cm` (função `cobertura`). Transformar
  peça de 90 cm em faixa mais larga seria inventar cobertura, então a A901 só é sugerida para
  aquário de 90 cm mesmo — e a A451M só para 45 cm.

### Verificação (o que foi realmente rodado)

- `python3 ferramentas/validar-produtos.py` → **56 produtos, 31 cotações, 0 erro, 12 avisos**
  (10 são o V20 novo — link sem foto; 1 é o V11 do Eheim 200 W, antigo; 1 era o V14 do Sicce, e o
  status foi corrigido para `completo`).
- `python3 ferramentas/gerar-catalogo-aquecedores.py` → 14 itens embutidos, 5 com link.
- `python3 ferramentas/gerar-catalogo-iluminacao.py` → 5 itens embutidos, 3 com link, 11 barrados
  com motivo.
- `php -l` nos dois snippets tocados → sem erro.
- `python3 ferramentas/conferir-protecao-funcoes.py` e `conferir-slugs.py` → ok.
- **Imagem NÃO pôde ser conferida por esta sessão:** `down-bs-br.img.susercontent.com` devolve
  `EGRESS_BLOCKED`, como todo domínio de loja. Por isso `largura` e `altura` estão `null` com
  motivo, e o cartão vai reservar o espaço por CSS (`aspect-ratio: 1/1` + `object-fit: contain`),
  que não salta o layout qualquer que seja a proporção real. **Quem consegue conferir se as 21
  fotos carregam é a Sentinela Técnica, que roda no Chrome.**

### Próximo passo desbloqueado

**Bloco 4e — a vitrine.** O banco agora tem foto, e é o que faltava para o cartão de produto
parecer comércio: rolagem horizontal com `scroll-snap`, cartão que é link de verdade, promessa
acima da dobra e barra fixa no celular. As 21 imagens só chegam ao visitante nesse bloco.

Depois dele, o **4c leva 2** (JSON-LD e tabela pré-renderizada na C12 e na C15), que era o próximo
antes deste lote.

**Para a Sentinela Estratégica**, em ordem de retorno:

1. **Lúmen da linha Soma** — 8 produtos com link e foto, todos barrados por um número que nenhuma
   loja brasileira publica. Se a Soma responder por e-mail ou se alguém fotografar a caixa,
   destravam 8 vendas de uma vez, cobrindo de 20 a 130 cm.
2. **Voltagem confirmada em ficha** dos 7 Maxxi, do RS-50 e do Sicce — 9 links parados por um
   campo.
3. **Imagem dos 10 antigos** (`eheim-classic-250-2213`, `seachem-tidal-55`, `roxin-ht-1300-q3-100w`,
   `-200w`, `-300w`, `chihiros-wrgb-ii-pro-60`, `ista-i-401-45`, `sunsun-ade-400c`,
   `seachem-matrix-1l`, `eheim-substrat-pro-1l`): já vendem, e vão para a vitrine sem foto.
4. Continuam **10 produtos esperando `afiliado.url`** — a lista da leva anterior não mudou.

### NÃO CONCLUÍDO — o Sync não foi acionado, e agora são DUAS revisões paradas

Esta sessão **não alcança o site**: `aquametria.com.br` devolve `EGRESS_BLOCKED` no proxy de saída,
tanto na URL do Sync quanto em `/wp-json/aquametria/v1/status`. Não foi possível acionar o
desembarque nem conferir a revisão aplicada, então **este bloco está entregue no `main` e não está
no ar** — exatamente como a revisão 18 da leva anterior.

**O repositório está na revisão 19. O site está pelo menos oito revisões atrás.** Alguém com
navegador precisa abrir a URL do Sync com `&forcar=1` (a chave está na memória e não entra neste
arquivo, que pode virar público) e, uns cinco minutos depois, conferir que
`/wp-json/aquametria/v1/status` diz **revisão 19**. A Sentinela Técnica das 11h30 roda no Chrome do
Raphael e alcança o site; esta sessão, não.

Enquanto isso não for feito, o que está no ar continua sem as 21 fotos, sem os 20 produtos novos,
sem o aquecedor de 150 W que fecha a janela da C5 e sem as duas Chihiros da C15.

## 2026-09-09 — Bloco 4c, leva 1b: a tabela pre-renderizada passou a dizer QUAL produto atende

Disparo encadeado, autorizado pelo Raphael para antecipar a entrega em um dia. O pedido do
disparo era executar o 4c na C3 e na C5. **Ao ler o `main` antes de trabalhar, o 4c dessas duas
ja estava entregue** na revisao 18 — JSON-LD, tabela pre-renderizada de 30 a 300 L, resposta antes
da explicacao e procedencia dentro da frase, tudo conferido em Chromium com o JavaScript
desligado. Refazer seria trabalho perdido.

O que NAO estava entregue era justamente o item novo do pedido: **a coluna com o produto que
atende cada faixa**. Foi esse o bloco desta execucao, e ele e a metade do 4e-B que cabe dentro do
4c — a pessoa passa a saber que sai dali com produto ANTES de preencher qualquer campo.

### O defeito que a coluna corrige, dito sem eufemismo

A tabela servida respondia ao leitor e **nao respondia ao comprador**. Quem chegava com "que
filtro comprar para 100 litros" via a faixa de L/h e nada mais: a recomendacao de produto so
existia depois de preencher o formulario inteiro e rolar ate o fim do resultado. No celular isso
e pior, porque o formulario ocupa a tela toda. E, para um modelo de linguagem, a pagina inteira
nao continha uma unica indicacao de compra citavel.

### Entregue, nas duas calculadoras

- **Uma coluna nova na tabela**, uma celula por volume. Cada celula traz o modelo, a
  especificacao QUE FEZ ELE ENTRAR ("650 L/h — 6,5 renovacoes/h nos 100 L"; "150 W — 110 ou
  220 V"), a procedencia e a data na mesma frase, e o link de loja quando existe
  (`rel="sponsored noopener"`, `target="_blank"`).
- **O criterio e o MESMO do script**, e isso e verificavel: a funcao `escolher()` do JavaScript
  ganhou espelho em PHP (`aquametria_c3_produtos_exemplo`, `aquametria_c5_produtos_exemplo`) —
  vazao dentro da faixa e ordem pela distancia ate o meio dela na C3; potencia dentro da faixa,
  com teto no degrau comercial, e ordem pela distancia ate o topo na C5. **Comissao nao ordena
  nada** (regra V16).
- **A linha do comprável, rotulada como o que e.** O modelo que atende melhor quase sempre e um
  que o banco ainda nao conseguiu link — hoje, 4 das 6 linhas da C3 e 5 das 6 da C5. Sem isso a
  tabela mostrava seis nomes que ninguem sabe onde comprar. Entao, quando o primeiro nao tem
  link, sai embaixo, escrito "Com link hoje, na mesma faixa", **o primeiro da mesma ordem** que
  tem. A ordem nao muda; muda o que a tela conta.
- **Bloco vazio nunca sai mudo.** A faixa de 30 L da C3 nao tem filtro nenhum no banco (o menor
  e de 400 L/h, e a faixa vai ate 300 L/h), e a celula escreve isso com os dois numeros. Silencio
  parece defeito.
- **Aviso de publicidade proprio, junto da tabela** — nao basta o do bloco de resultado, que so
  aparece depois do calculo e nao existe sem JavaScript. Diz a palavra comissao, diz que a ordem
  e por adequacao tecnica, diz por que nao publicamos preco e linka a pagina de divulgacao.
- **FAQPage ganhou as perguntas de COMPRA**, uma por volume: C3 de 8 para 13 perguntas, C5 de 8
  para 14. Cada resposta nomeia o mesmo modelo e o mesmo numero que a tabela serve — FAQPage que
  promete o que a pagina nao mostra e lixo detectavel.

### Tres ressalvas que a coluna obrigou a escrever, e que sao o conteudo

1. **A C5 nao filtra por voltagem nem por temperatura-alvo na tabela**, porque a tabela nao
   conhece nenhum dos dois — e sao exatamente as duas barreiras de seguranca do formulario
   (V18). Aquecedor na voltagem errada queima. Entao a celula publica a voltagem que a ficha
   declara, ou a frase de que ela nao esta confirmada, e o aviso abaixo da tabela diz em negrito
   para conferir a voltagem antes de comprar. Nao se chuta 110 nem 220.
2. **A linha de 300 L da C5 avisa que a faixa passa do maior degrau da linha de referencia** e
   que ali a resposta e mais de um aparelho — senao a ultima coluna contradiria a coluna ao lado,
   que ja dizia isso.
3. **Quando o volume declarado pelo fabricante e menor que o do exemplo, a celula diz.** Acontece
   hoje uma vez: o Seachem Tidal 55 e o unico filtro com link na faixa de 300 L, e a ficha dele
   declara ate 200 L. Ele entra pela vazao; a declaracao de volume nao cobre o caso, e quem le
   precisa saber disso antes de clicar.

### A correcao do campo `imagem` — dado bom que quase foi jogado fora

O disparo trouxe uma correcao, e ela estava certa: **nao conseguir BUSCAR um arquivo nao e
evidencia de que a URL esteja errada.** As 21 URLs de foto foram colhidas do painel de afiliados
da Shopee, no navegador do Raphael, em 09/09/2026. O que esta bloqueado e o egresso da nuvem, que
barra `down-bs-br.img.susercontent.com` como barra todo dominio de loja.

Conferido no `main`: **nenhuma imagem tinha sido anulada** — as 21 estao la, com `url`, `fonte`,
`coletado_em` e `alt`. O que faltava era o lugar de registrar a falta de conferencia sem mexer no
dado. Foi criado:

- `imagem.verificado_em` (null hoje) e `imagem.motivo_sem_verificacao`, no esquema (versao 5 → 6)
  e nos 21 registros, com o motivo escrito por extenso e nomeando quem consegue conferir: **a
  Sentinela Tecnica, que roda no Chrome.**
- **Regra V21 do validador**, para isto nao depender de ninguem lembrar: imagem sem
  `verificado_em` tem de dizer por que. Testada nos dois sentidos — com o motivo, 0 erro; sem o
  motivo, erro apontando o produto.
- A regra escrita no esquema, em uma frase, para a proxima sessao: **jogar fora dado bom por
  falta de meio de conferencia e a pior troca possivel.**

### Verificacao (o que foi realmente rodado, com numero)

- `php -l` nos dois snippets → sem erro. `conferir-protecao-funcoes.py` → 8 snippets, todas as
  funcoes dentro de `function_exists`. `conferir-slugs.py` → ok.
- `validar-produtos.py` → **56 produtos, 31 cotacoes, 0 erro, 11 avisos** (os mesmos 10 do V20,
  link sem foto, mais o V11 antigo do Eheim 200 W).
- `teste-navegador-visibilidade-ia.mjs`, em Chromium **com JavaScript DESLIGADO** → **tudo
  passou**, nos dois arquivos. O teste ganhou os casos deste bloco: uma celula de produto por
  volume, **nenhuma muda** (celula com menos de 20 caracteres reprova), todo link da tabela
  `sponsored` + `noopener` + aba nova e **com texto** (teclado e leitor de tela), e o aviso de
  comissao presente junto da tabela.
- `teste-navegador-cinco.mjs` (JavaScript LIGADO, as cinco calculadoras) → tudo passou, incluindo
  **zero `&#038;` no HTML servido** e os links de afiliado do bloco de resultado.
- `teste-navegador-c5.mjs` → **15 casos, todos passaram**, incluindo as duas barreiras de
  seguranca e o celular de 390 px **sem rolagem horizontal** com a tabela mais larga (ela rola
  dentro do proprio `-rolagem`, nao empurra a pagina).
- Dois consertos no proprio ferramental, para os testes nao mentirem:
  - o `teste-navegador-c5.mjs` procurava `.aqm-c5-aviso-afiliado` sem escopo e passou a achar
    DOIS elementos — quebrava por ambiguidade, nao por defeito. Agora confere os dois avisos, um
    por um, e diz qual e qual;
  - o caso "console limpo" reprovava por **13 falhas de rede**: o egresso da nuvem barra
    `fonts.googleapis.com` e `fonts.gstatic.com`, que a casca carrega de verdade e que carregam
    no navegador do Raphael. Falha de rede agora sai contada e nomeada a parte, e o caso mede o
    que ele existe para medir: **erro de script**. Um teste que reprova sempre treina a proxima
    sessao a ignorar o resultado dele, que e o pior estrago possivel.

### NAO CONCLUIDO — o Sync continua fora de alcance, e agora sao TRES revisoes paradas

`aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessao, tanto na URL do Sync quanto em
`/wp-json/aquametria/v1/status`. **Nao foi possivel acionar o desembarque nem conferir a revisao
aplicada.** Este bloco esta entregue no `main` e **nao esta no ar**, como as revisoes 18 e 19.

**O repositorio esta na revisao 20. O site estava na 11 na ultima medicao (08/09, 13h03).** Nove
revisoes de diferenca. O que esta no ar hoje nao tem: as 21 fotos, os 20 produtos novos, o
aquecedor de 150 W que fecha a janela da C5, as duas Chihiros da C15, o JSON-LD, a tabela
pre-renderizada e agora a coluna de produto.

Quem alcanca o site e a **Sentinela Tecnica das 11h30, que roda no Chrome do Raphael**. Basta
abrir a URL do Sync com `&forcar=1` (a chave esta na memoria e nao entra neste arquivo, que pode
virar publico) e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisao 20**.

### Proximo passo desbloqueado

**Bloco 4e — a vitrine**, agora com a metade B ja meio-caminho andada: a promessa antes do
formulario existe em forma de tabela com produto, e falta o resto — cartao com FOTO em rolagem
horizontal com `scroll-snap`, linha de promessa no topo, barra fixa no celular, e rolagem
automatica ate o resultado. As 21 imagens do banco so chegam ao visitante nesse bloco.

Depois dele, o **4c leva 2** (JSON-LD e tabela pre-renderizada na C12 e na C15) e o 4c leva 3
(C1 e os tres artigos).

**Para a Sentinela Estratégica**, sem mudanca desde a leva anterior: lumen da linha Soma (8
produtos com link e foto barrados por um numero), voltagem confirmada dos 7 Maxxi, do RS-50 e do
Sicce (9 links parados por um campo), imagem dos 10 antigos que ja vendem, e 10 produtos
esperando `afiliado.url`.

## 2026-09-09 (terceira execucao do dia) — A DUPLA CONDICAO: a C3 para de recomendar filtro que ela mesma diz que nao serve

Disparo manual do Raphael, com tres itens vistos por ele na C3 NO AR (aquario de 189,6 L,
plantado, carga media). Os tres foram feitos nesta execucao, antes da fila normal.

### Item 1 — o defeito grave, e ele era de credibilidade e nao de calculo

O primeiro produto recomendado era o **Atman HF-0600**, e o cartao dele escrevia, logo abaixo do
nome: "O fabricante declara que ele atende ate 150 L — o seu volume passa disso, e a declaracao do
fabricante nao cobre o seu caso." A pagina recomendava em PRIMEIRO lugar um filtro que ela mesma
dizia nao servir.

A causa era a que o Raphael suspeitou: a elegibilidade olhava so a VAZAO (650 L/h caem na faixa
334-948 L/h daquele aquario) e ignorava o volume atendido declarado pelo fabricante.

A regra nova esta escrita no esquema do banco como **V22** e implementada nos DOIS lados da C3, o
PHP que serve a tabela e o JavaScript que calcula na tela:

- entra nos recomendados so quem passa nas **duas** condicoes — vazao dentro da faixa **E** volume
  do visitante dentro do volume declarado pelo fabricante (o corte vale nas duas pontas: modelo
  declarado "a partir de 180 L" tambem nao cobre um aquario de 100 L);
- fabricante que **nao declara** volume entra, com a ressalva escrita no cartao;
- fabricante que declara e nao cobre **sai dos recomendados** e vai para uma secao SEPARADA,
  abaixo, rotulada "Atendem a vazao, mas o fabricante nao cobre esse volume". Nunca misturado,
  nunca em primeiro lugar. Some quando nao ha ninguem nela.

A funcao `aquametria_c3_volume_ressalva` mudou de assunto junto: como recomendado nao fura mais o
volume, o que sobra para ressalvar e o outro caso, o fabricante que nao declara volume nenhum.

### Item 2 — o topo da lista

A ordem passou a ter **tres degraus**: (1) elegibilidade tecnica dupla; (2) adequacao tecnica entre
os elegiveis, que e a distancia ate o meio da faixa; (3) so como DESEMPATE entre itens
**tecnicamente equivalentes**, quem tem link de loja aparece antes.

"Tecnicamente equivalente" precisava de um numero, senao o desempate come a ordem tecnica: dois
filtros sao equivalentes quando as distancias deles ate o meio da faixa caem no **mesmo decimo da
largura da faixa**. E convencao editorial da Aquametria, declarada na tela e no codigo, nao
constante de fabricante. A regra V16 do esquema foi reescrita para dizer exatamente isso e para
repetir o que continua proibido: taxa de comissao nao e comparada em lugar nenhum, produto pior
nunca sobe por pagar mais, e "produto sem link de loja aparece do mesmo jeito" continua valendo —
muda a POSICAO de quem ja era equivalente, nao a presenca de ninguem.

**Numero medido, e ele importa:** no caso exato do Raphael (189,6 L, PLANTADO) a faixa e estreita
(334 a 948 L/h, decimo de 61 L/h) e nenhum par de filtros cai no mesmo degrau — o desempate nao
dispara, e o topo continua sendo o Atman AT-3336, que ainda nao tem link. Isso nao e o desempate
falhando: e ele fazendo o que foi mandado fazer, que e nao passar na frente da adequacao tecnica.
O que resolve esse caso e link para o AT-3336, e isso e trabalho da Sentinela Estrategica. No mesmo
volume em perfil COMUNITARIO, onde a faixa vai a 1.896 L/h e cinco modelos caem no mesmo decimo, o
desempate dispara e o topo virou quatro itens com link (Eheim 2217 nas duas voltagens, Seachem
Tidal 55, SunSun HW-702B), com o Atman AT-3338 sem link caindo para quinto.

### Item 3 — o lote de filtro e midia colhido a mao no painel da Shopee

Entraram **8 filtros novos** com link e imagem, mais a imagem de 3 registros que ja vendiam
(Eheim classic 250, Seachem Tidal 55, Seachem Matrix 1 L) e **8 cotacoes** novas.

O que o lote virou depois de conferido contra a escada de fontes — e aqui esta a parte que importa,
porque as specs vieram do ANUNCIO e anuncio de marketplace (nivel 6) sustenta so existencia,
nomenclatura e preco, **nunca numero tecnico**. Cada numero abaixo foi reconferido em varejo BR
especializado por resultado de busca (nivel 5), que e o que o egresso da nuvem permite:

- **Eheim classic 600 (2217), 127 V e 220 V** — registros SEPARADOS, porque voltagem e chave de
  compatibilidade e cada anuncio vende uma versao so. 1000 L/h, 20 W, coluna de 2,25 m, ate 600 L,
  repetidos por AquaMaeda, Pro-Aquarista, Fazenda Submersa e AquaBetta; a voltagem de cada versao
  sai do titulo da loja BR que a vende. **Os dois entraram no catalogo da C3 como completos, com
  link E foto.** Sao os primeiros do banco a fechar a faixa acima de 200 L vendendo.
- **SunSun HW-702B 220 V** — 1000 L/h para ate 200 L (Pet Hobby), coluna de 1,4 m (Wiltec), UV de
  9 W (Pet Hobby e Aqua Mais), 220 V (Aqua Mais). **Entrou no catalogo da C3, com link e foto.**
- **Ocean Tech CT-1000-3** — 1000 L/h, 15 W, ate 200 L confirmados por quatro lojas BR. Ficou
  `parcial`: falta coluna maxima (o "1,4 m" das fichas e COMPRIMENTO DE CABO, nao recalque) e falta
  voltagem — o varejo vende o mesmo modelo em 110/127 V e em 220 V e nenhuma fonte diz qual versao
  este anuncio abre.
- **SunSun HW-702A** — mesma ficha do B, sem UV. `parcial` por UM campo: voltagem. O anuncio abre
  110 V, e isso ficou em `afiliado.voltagem_anuncio`, que e onde voltagem de anuncio mora.
- **SunSun XBL-600** — 500 L/h, 7 W, ate 150 L (Pet Hobby). `parcial` por UM campo: voltagem. As
  fichas dizem que sai em 110 V **ou** em 220 V e que NAO e bivolt, sem dizer qual e a deste
  anuncio. Chutar 110 ou 220 e proibido aqui, e queima aparelho.
- **Maxxi Pro MP-600** e **Aquaverso APK-600** — `parcial` com NENHUM numero tecnico. A busca nao
  achou ficha de fabricante nem de varejo especializado para nenhum dos dois; o que aparece com
  600 L/h na linha Maxxi e o hang-on HF-800, que e outro modelo, e a loja oficial da Aquaverso
  (lojaaquaverso.com.br) devolve EGRESS_BLOCKED. Os 600 L/h do titulo do anuncio ficaram onde
  valem, que e no anuncio. O campo `tipo` tambem ficou null nos dois: "mini canister de pendurar" e
  nomenclatura de anuncio, e `tipo` e campo tecnico aqui porque e ele que decide se a C3 cobra
  altura de coluna do modelo.

**Placar do lote: 3 de 8 ja vendem dentro do resultado da C3; 5 esperam UM ou DOIS campos** — 4
esperam so voltagem, 2 esperam vazao. Todos os 8 tem foto e link no banco.

Uma coisa que a lista de nomes tornou necessaria: com o Eheim 2217 no banco duas vezes, a tela
mostrava dois itens de nome identico. O nome de tela passa a carregar a voltagem quando o registro
declara uma so — "Eheim classic 600 (2217) (127 V)" —, no cartao, na tabela servida e no FAQ.

### Verificacao (o que foi realmente rodado, com numero)

- `php -l` no snippet da C3 → sem erro. `conferir-protecao-funcoes.py` → sai 0, todas as funcoes
  novas (`aquametria_c3_cobre_volume`, `_degrau_adequacao`, `_ordenar`, `_produtos_fora_do_volume`,
  `_fora_do_volume_frase`, `_nome_produto`) dentro de `function_exists`. `conferir-slugs.py` → ok.
- `validar-produtos.py` → **64 produtos, 39 cotacoes, 0 erro, 9 avisos**. Os erros que apareceram na
  primeira passada foram consertados no dado, nao afrouxando a regra: o HW-702B saiu de `completo`
  para `parcial` (potencia_w e obrigatorio da entidade e ficou null porque a unica ficha que a
  publica diz 24 W no titulo e 15 W na descricao, e somar 15 W de bomba com 9 W de UV para chegar
  aos 24 seria derivacao nossa), e o MP-600 e o APK-600 perderam o `tipo`, que nenhuma fonte
  acima de anuncio sustentava. O aviso V14 do XBL-600 fica de proposito: falta voltagem, que nao
  esta na lista de obrigatorios da entidade mas esta no minimo da C3, e a observacao do registro
  diz isso com essas palavras.
- `gerar-catalogo-filtros.py` → **13 filtros no catalogo da C3** (eram 10), 6 com link (eram 3).
- **`teste-navegador-c3-dupla-condicao.mjs`, arquivo NOVO** → 16 casos, todos passaram, em Chromium
  de verdade, executando o caso do Raphael. Ele confere o que este bloco promete: nenhum recomendado
  com volume declarado que nao cubra o aquario, o HF-0600 fora dos recomendados e dentro da secao
  separada, a secao rotulada e ABAIXO no HTML, o desempate por link so entre itens do mesmo degrau,
  e todo botao de loja `sponsored` + `noopener` + aba nova com texto. Duas decisoes de desenho do
  teste, e as duas existem para ele nao mentir: (a) ele roda um SEGUNDO caso, o mesmo volume em
  perfil comunitario, porque no plantado a faixa e estreita demais para dois filtros cairem no mesmo
  degrau e o desempate nunca dispararia — teste que nao exercita a regra nao prova a regra; (b) ele
  casa cada linha da tela com a ficha do catalogo embutido e **reprova quando nao acha**, em vez de
  filtrar os orfaos e passar em silencio (foi exatamente o que quase aconteceu quando o nome de tela
  ganhou a voltagem).
- `teste-navegador-visibilidade-ia.mjs`, em Chromium **com JavaScript DESLIGADO** → tudo passou nos
  dois arquivos, incluindo as 6 celulas de produto da tabela servida e os 6 links `sponsored`.
- `teste-navegador-cinco.mjs` (JavaScript ligado, as cinco calculadoras) → tudo passou.

### NAO CONCLUIDO — o Sync continua fora de alcance, e agora sao QUATRO revisoes paradas

`aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessao, tanto na URL do Sync com `&forcar=1`
quanto em `/wp-json/aquametria/v1/status`. **Nao foi possivel acionar o desembarque nem conferir a
revisao aplicada.** Este bloco esta entregue no `main` e **nao esta no ar**, como as revisoes 18,
19 e 20.

**O repositorio esta na revisao 21. O site estava na 11 na ultima medicao (08/09, 13h03).** Dez
revisoes de diferenca. O que esta no ar hoje NAO tem: a dupla condicao (ou seja, **a C3 no ar
continua recomendando em primeiro lugar o Atman HF-0600 para o aquario de 189,6 L do Raphael**),
o desempate por link, as 24 fotos, os 28 produtos novos, o aquecedor de 150 W que fecha a janela
da C5, as duas Chihiros da C15, o JSON-LD e a tabela pre-renderizada.

Quem alcanca o site e a **Sentinela Tecnica das 11h30, que roda no Chrome do Raphael**. Basta abrir
a URL do Sync com `&forcar=1` (a chave esta na memoria e nao entra neste arquivo, que pode virar
publico) e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisao 21**.

### Proximo passo desbloqueado

O Raphael disse "nao adiante o proximo bloco — eu disparo em seguida". O que estava na fila
continua sendo o **4e, a vitrine**: cartao com FOTO em rolagem horizontal com `scroll-snap`, linha
de promessa no topo, barra fixa no celular e rolagem automatica ate o resultado. As 24 imagens do
banco (21 da leva anterior mais 3 desta) so chegam ao visitante nesse bloco — hoje elas existem no
dado e nao aparecem na tela.

**Para a Sentinela Estrategica**, a fila de link cresceu e mudou de forma. O que trava venda hoje,
em ordem de dano: (1) **voltagem** de 4 registros novos que ja tem link E foto e nao podem ser
sugeridos por causa de um campo — HW-702A, XBL-600 e CT-1000-3 (que tambem precisa da coluna) —,
mais os 9 antigos na mesma situacao; (2) **link para o Atman AT-3336**, que e o primeiro
recomendado do caso real do Raphael e nao tem onde comprar; (3) vazao com fonte para o MP-600 e o
APK-600; (4) lumen da linha Soma, imagem dos que vendem sem foto.

---

## 2026-09-09 (redisparo das 12h) — BLOCO 4d: a casca no celular ganha menu, e o site ganha ícone próprio

**Antes de mais nada, sobre a execução que falhou.** O disparo das 12h20 (sessão
`cse_01R1msCiPtLH1iFvqdgmUfLT`) morreu às 12h26 sem empurrar nada, e esta execução
**não achou rastro do que a matou**: não há branch `claude/*` divergente, não há PR
aberto e o `main` estava intacto na revisão 21 — ou seja, ela morreu antes de commitar
qualquer coisa, e não deixou trabalho pela metade para recuperar. Não sei a causa e não
vou inventar uma. O que ficou de aprendizado prático desta execução, e que pode ser a
causa: o bloco 4e inteiro (vitrine em quatro calculadoras + promessa + barra fixa +
rolagem) é grande demais para uma execução; o payload do redisparo mandou entregar em
partes, e foi o que foi feito.

**Entregue: os dois itens de casca do bloco 4d, no mesmo snippet, como pedido.**
Manifest revisão **22**, casca na versão **1.3.0**.

### (1) Menu hambúrguer no celular

Abaixo de 782 px — a mesma quebra que o próprio WordPress usa para decidir que a tela
virou celular — o menu vira sanfona atrás de um botão. Acima disso nada muda: é a mesma
fileira de links de sempre.

**A decisão que governa o resto, e que é de indexação, não de layout:** os três links
saem **sempre** no HTML servido, dentro de `<nav>`, e o botão não gera link nenhum — ele
só mostra e esconde o que já está lá. Quem esconde a lista no celular é o seletor
`.aqm-nav-caixa[data-aqm-menu]`, e esse atributo quem põe é o JavaScript do rodapé.
**Sem JavaScript o atributo não existe, a regra de CSS não casa e o menu não some**:
volta a ser a lista visível que o site tinha antes desta versão. Esconder por padrão e
contar com o script para revelar teria trocado um defeito de celular por um defeito de
visibilidade em IA — que é regra de primeira classe do projeto desde 08/09.

O que o botão carrega: `aria-expanded` que muda de verdade, `aria-controls` apontando
para o id do `<nav>` (id **contado**, porque o filtro `render_block` pode trocar mais de
um bloco `core/navigation` na mesma página e `aria-controls` para id repetido não
controla nada), fecho no **Escape** com o foco devolvido ao botão, fecho no clique fora,
e reset ao alargar a janela — sem esse último o `aria-expanded` continuaria dizendo
"aberto" para o leitor de tela depois de o menu já ter virado fileira.

O script sai no **`wp_footer`**, nunca dentro do retorno de shortcode. É a regra que
nasceu do defeito de 08/09/2026, e ela vale para a casca do mesmo jeito que vale para
calculadora.

### (2) Ícone próprio do site

`remove_action( 'wp_head', 'wp_site_icon', 99 )` tira o ícone que o WordPress imprime
sozinho — sem isso o site sairia com dois e o navegador escolheria o errado. No lugar
entram três, todos como data URI dentro do snippet, **nada sobe para a biblioteca de
mídia**: o SVG da aba (`rel="icon" type="image/svg+xml"`, 464 bytes), um PNG de 32 px
como `alternate icon` para quem não desenha SVG na aba (186 bytes), e o
`apple-touch-icon` de 180 px para o iOS (3.238 bytes), mais `theme-color` na tinta da
marca.

O desenho é o mesmo do logotipo: o recipiente graduado com a linha de enchimento, em
tinta #0D1B22 e lâmina #0E7C8C. Sem peixe, sem bolha, sem wordmark — a 16 px o wordmark
vira borrão e o que sobrevive é o recipiente.

Duas decisões de desenho, cada uma com motivo: **o SVG da aba tem canto arredondado e o
PNG do iOS não tem**, porque o iOS aplica a própria máscara e canto arredondado por baixo
de máscara vira borda dupla; e o PNG passa por redução de paleta para 64 cores, o que o
levou de 9.124 para 3.238 bytes sem mudar nada do que se vê — o desenho tem três cores, e
o PNG truecolor estava carregando milhares de tons de borda que viravam 12 KB de base64
dentro do snippet.

**`ferramentas/gerar-favicon.php`, arquivo novo:** o desenho não se edita à mão no
snippet. Ele é gerado entre os marcadores `FAVICON-INICIO` e `FAVICON-FIM`, pelo mesmo
motivo que o catálogo de produtos é gerado dentro das calculadoras — desenho mantido em
dois lugares diverge em silêncio.

### O ferramental que este bloco obrigou a criar

Nenhum teste do projeto olhava para o **cabeçalho**: o `render-para-teste.php` monta
página de calculadora, cujo corpo é o retorno de um shortcode, e o cabeçalho da
Aquametria não vem de shortcode nenhum — vem do filtro `render_block`. Então nasceram:

- **`ferramentas/render-casca-para-teste.php`**, que monta a página como o tema de blocos
  monta: `wp_head`, o cabeçalho vindo do filtro, o conteúdo (esse sim passando pelo
  escape de `&` dos filtros de conteúdo) e `wp_footer`.
- **`ferramentas/teste-navegador-casca.mjs`**, **31 asserções, todas passaram** em
  Chromium de verdade: HTML servido (três `<a href>` dentro do `<nav>`, `aria-controls`,
  zero `&#038;` dentro de `<script>`), desktop a 1100 px (botão escondido, três links
  visíveis), celular a 390 px (abre, fecha no Escape com foco devolvido, abre no Enter,
  Tab chega ao primeiro link **com endereço de verdade**, clique fora fecha, alargar
  reseta o `aria-expanded`), **celular com o JavaScript DESLIGADO** (os três links
  continuam visíveis e o botão não aparece) e os ícones medidos por `naturalWidth`: SVG
  desenha, PNG do iOS tem 180×180, alternativo tem 32×32, e o ícone do WordPress sumiu do
  `wp_head`.
- Três acréscimos ao `render-para-teste.php`, todos compatíveis com o que já existia:
  `apply_filters` passou a repassar argumentos extras (o `render_block` recebe dois),
  `get_posts` passou a consultar um mapa `__paginas` (vazio por padrão — sem ele a casca
  serve `<span>` em vez de `<a>`, de propósito, e o teste estaria conferindo o caso
  errado), e nasceram `remove_action` de verdade mais um `wp_site_icon` de mentira
  registrado no `wp_head` na prioridade do core: é ele que permite **provar** que a casca
  tirou o ícone do WordPress de lá.

### Verificação (o que foi realmente rodado)

- `php -l` nos três arquivos novos/alterados → sem erro.
- `conferir-protecao-funcoes.py` nos 8 snippets → **sai 0**, 22 funções da casca dentro
  de `function_exists`.
- `teste-navegador-casca.mjs` → **31 de 31**.
- `teste-navegador-cinco.mjs` (as cinco calculadoras, JavaScript ligado) → tudo passou.
- `teste-navegador-visibilidade-ia.mjs` (JavaScript desligado) → tudo passou.
- `teste-apelidos.php` → 59 afirmações, 0 falha. `conferir-slugs.py` → ok.
- sha256 do manifest conferido contra os arquivos: **0 divergentes**.
- Inspeção visual em Chromium a 390 px e a 1100 px: o menu aberto e o cabeçalho de
  desktop foram fotografados e olhados, não só medidos.

### NÃO CONCLUÍDO — o Sync continua fora de alcance, e agora são CINCO revisões paradas

`aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessão, tanto na URL do Sync com
`&forcar=1` quanto em `/wp-json/aquametria/v1/status`. **Não foi possível acionar o
desembarque nem conferir a revisão aplicada.** Este bloco está entregue no `main` e
**não está no ar**, como as revisões 18, 19, 20 e 21.

**O repositório está na revisão 22. O site estava na 11 na última medição (08/09,
13h03).** Quem alcança o site é a **Sentinela Técnica das 11h30, que roda no Chrome do
Raphael**: basta abrir a URL do Sync com `&forcar=1` e, uns cinco minutos depois,
conferir que `/wp-json/aquametria/v1/status` diz **revisão 22**.

### Próximo passo desbloqueado

**BLOCO 4e — A VITRINE**, inteiro, e ele é grande: cartão de produto com foto em rolagem
horizontal com `scroll-snap` (sem biblioteca, cartão que é `<a>` de verdade), linha de
promessa acima do formulário, barra fixa no rodapé do celular enquanto o resultado está
fora da tela, e rolagem automática até o resultado com `scroll-margin-top`. As 24 imagens
do banco só chegam ao visitante nesse bloco. **Se não couber numa execução, entregar por
calculadora** — começando pela C3, que é a que tem mais itens com foto e link (6 de 13).

## 2026-09-09 — Reorganizacao do Arquipelago aplicada (execucao excepcional, sem bloco da fila)

- Disparo excepcional: a fila de blocos da Aquametria ficou parada de proposito.
  Nenhum snippet foi tocado, nada foi publicado e o Sync **nao** foi acionado.
- O Arquipelago deixou de ter uma Fundacao por ilha e passou a ter **uma
  Fundacao com despachante**, que escolhe a ilha mais atrasada a cada execucao:
  - criado o `ARQUIPELAGO.md` na raiz, contrato comum a todas as ilhas;
  - criado o `ilhas/aquametria/PROMPT.md`, com o que e so desta ilha
    (identidade, endpoints, quem verifica, memoria e fila de blocos);
  - acrescentado ao topo do `ESTADO.md` desta ilha o cabecalho YAML que o
    despachante le (`estado: viva`, `prioridade: 2`,
    `ultima_execucao: 2026-09-09T16:00Z`, `bloco_atual: "4c"`), sem tirar
    nenhuma linha do que ja existia;
  - criada a segunda ilha, `ilhas/robometria/`, com pastas, `manifest.json` na
    revisao 0, `README.md`, `PROMPT.md`, `ESTADO.md` e `REGISTRO.md`;
  - criado o modelo de ilha nova em `ilhas/_modelo/`;
  - o `README.md` da raiz ganhou a secao que explica a estrutura nova.
- **Proximo passo da Aquametria: sem mudanca — continua o bloco 4c**, retrofit
  de visibilidade em IA, na ordem C3 e C5, depois C12 e C15, depois C1 e os
  artigos. A partir de agora a fila desta ilha mora em
  `ilhas/aquametria/PROMPT.md`, e as regras comuns no `ARQUIPELAGO.md` da raiz.

## 2026-09-09 — Fila reordenada pela meta de trafego organico (execucao excepcional, sem bloco da fila)

- Decisao do Raphael em 09/09/2026: a Aquametria so conta como completa quando
  estiver **entrando trafego organico** — pagina indexada, aparecendo em busca e
  recebendo visita. Nao e numero de calculadora publicada e nao e a primeira venda.
- A fila de `ilhas/aquametria/PROMPT.md` foi reescrita por essa meta: T1 medir a
  indexacao, T2 limpar o que atrapalha a indexacao, T3 banco de dados (especies
  primeiro), T4 malha de paginas, T5 artigos-ancora, T6 prospeccao do widget,
  T7 schema e visibilidade em IA, T8 vitrine de produto. C2, C7 e C8 saem da fila
  por ora — ferramenta nova nao traz trafego enquanto as que existem nao estiverem
  indexadas.
- Execucao excepcional: nenhum snippet foi tocado, nada foi publicado, o Sync
  **nao** foi acionado e nenhum arquivo da Robometria ou o `ARQUIPELAGO.md` foi
  alterado. O cabecalho do `PROMPT.md` (identidade, endpoints, quem verifica,
  memoria) ficou intacto.
- **Proximo passo: bloco T1** — medir a indexacao no Search Console e gravar a
  primeira secao de `dados/indexacao.md`.
