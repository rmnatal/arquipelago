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
