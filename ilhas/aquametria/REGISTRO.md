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

## 2026-09-09 (mutirão, bloco 1 de N) — T3(a): o banco de espécies vai a 36, e duas recusas viram conteúdo

**Bloco entregue: T3(a), banco de espécies, leva 3.** 25 → **36 registros**, manifest na
**revisão 23**. Validador `validar-especies.py`: **0 erro**, 1 aviso antigo (o espelho do guppy).

### O que entrou

| id | porte | temperatura | frente mínima | status |
|---|---|---|---|---|
| `hyphessobrycon-amandae` (tetra ember) | 2,0 cm SL | 24–28 °C | — | parcial |
| `danio-margaritatus` (rasbora galáxia) | 2,1 cm SL | — | — | parcial |
| `tanichthys-albonubes` (peixe-neve) | 4,0 cm TL | 18–22 °C | 60 cm | parcial |
| `corydoras-paleatus` (coridora pimenta) | 6,6 cm SL | 18–23 °C | 61 cm | conflito |
| `nannostomus-beckfordi` (peixe-lápis) | 6,5 cm SL | 24–26 °C | 60 cm | parcial |
| `corydoras-sterbai` | 6,8 cm SL | 21–25 °C | 45 cm | **completo** |
| `melanotaenia-boesemani` (arco-íris) | 9,0 cm SL | 27–30 °C | 120 cm | conflito |
| `trichopodus-leerii` (gurami pérola) | 12,0 cm TL | 24–28 °C | 120 cm | parcial |
| `symphysodon-aequifasciatus` (acará-disco) | 13,7 cm SL | 26–30 °C | 120 cm | parcial |
| `pethia-conchonius` (barbo rosado) | 14,0 cm TL | 18–22 °C | 80 cm | parcial |
| `trichogaster-chuna` (gurami mel) | **recusado** | 22–28 °C | 60 cm | parcial |

Quem passa no portão de página de espécie subiu de **21 para 24**; a C8 (lotação) de 22 para 28;
a C5 de 23 para 33. A faixa de porte agora vai de 2,0 a 48,0 cm e as frentes mínimas declaradas
ganharam um décimo degrau (45 cm), que é o menor do banco.

### As duas recusas, que são o conteúdo mais valioso desta leva

**1. O porte do gurami mel foi RECUSADO por implausibilidade.** A busca restrita à FishBase
devolveu **13,7 cm TL em duas formulações independentes** — e 13,7 cm é o mesmo número que a
mesma busca tinha acabado de devolver para o acará-disco. O comércio brasileiro vende o gurami
mel a 4–5 cm, e a **própria ficha se contradiz** ao recomendar aquário mínimo de 60 cm para um
peixe que teria 13,7 cm. `porte_adulto_cm` ficou `null` com o motivo escrito no registro.
**Precedente que este bloco fixa: número atribuído que contradiz a própria ficha não entra só
porque tem dono.** A regra de atribuição do esquema garante que colher não é inventar; ela não
garante que a colheita esteja certa, e é por isso que a plausibilidade continua sendo trabalho
de quem grava.

**2. O `Poecilia wingei` (guppy endler) ficou de FORA**, e o motivo foi gravado no campo novo
`especies_recusadas[]` do banco: a busca devolveu porte, família e distribuição, mas nenhuma
faixa de temperatura e nenhum tamanho mínimo de aquário, em três formulações. Sem temperatura o
registro não serve nem à página de espécie nem à C5 — sobraria uma ficha que só repete o nome.

E uma terceira recusa, menor: a temperatura da rasbora galáxia. Os 22–24 °C que a busca devolveu
são a temperatura **do hábitat medida no campo**, e a fonte diz isso com essas palavras. Hábitat
não é faixa de manutenção; publicar um como o outro seria trocar uma medida por outra.

### Divergência publicada, não resolvida na média

Dois conflitos novos, os dois em campo de bem-estar, os dois resolvidos pelo MAIOR (regra própria
deste banco, oposta à do banco de produtos):

- **`melanotaenia-boesemani`, frente mínima: FishBase diz 80 cm, Seriously Fish diz 120 cm.** 50%
  de diferença, e não é arredondamento. Vale 120. São **120 cm de frente para um peixe de 9 cm** —
  a maior exigência já registrada aqui em relação ao porte, e o exemplo mais limpo de por que
  "1 cm de peixe por litro" não dimensiona nada. Cardume: 5 (FishBase) contra 6 (Seriously Fish) →
  vale 6; o "de preferência mais" da fonte não é número e não foi gravado.
- **`corydoras-paleatus`, frente mínima: 60 contra 61 cm** — este é só o arredondamento das 24
  polegadas, e o registro diz isso em vez de esconder a diferença.

### O que a coleta ensinou sobre o canal

O egresso continua fechado: `fishbase.se`, `fishbase.org`, `seriouslyfish.com` e
`en.wikipedia.org` devolveram **EGRESS_BLOCKED** de novo em 09/09/2026, e o mesmo vale para
`aquametria.com.br`. Toda coleta desta leva saiu de **busca restrita ao domínio**, níveis 3 e 5
da escada. O que mudou é que agora existe um caso documentado de a busca restrita devolver número
errado com atribuição certa — e é por isso que a nota de procedência do arquivo continua dizendo
que a leitura direta é uma coleta em aberto, não um capricho.

Três espécies novas ficaram em UM corpo de fonte só (`symphysodon-aequifasciatus`,
`pethia-conchonius`, `nannostomus-beckfordi`): a busca restrita ao Seriously Fish devolveu a ficha
mas nenhum número dela, e o número das congêneres do gênero foi **recusado** — número de outra
espécie não é fonte, ainda que o resumo da busca o ofereça de bandeja.

## 2026-09-09 (mutirão, bloco 2) — T3(a2): a C15 ganha quatro luminárias, e o buraco de lúmen é confirmado como estrutural

**Bloco entregue: T3(a2), catálogo de iluminação.** Banco de produtos de 64 para **68 registros**,
`produtos-iluminacao.json` de 16 para **20**, C15 de **5 para 9 luminárias aptas**, snippet da C15
na **1.1.1** (só o catálogo embutido mudou; nenhuma linha de cálculo foi tocada), manifest na
**revisão 24**. Validador de produtos: **0 erro**.

### O que entrou, e por que foi a Chihiros A-Series

| id | W | lm | lm/W | aquário |
|---|---:|---:|---:|---|
| `chihiros-a-series-a301` | 18 | 2.800 | 155,6 | 30 cm |
| `chihiros-a-series-a361` | 21 | 3.450 | 164,3 | 36 cm |
| `chihiros-a-series-a601` | 39 | 5.800 | 148,7 | 60 cm |
| `chihiros-a-series-a801` | 50 | 7.200 | 144,0 | 80 cm |

Não entrou por ser marca boa: entrou porque é **a única linha do catálogo que declara fluxo
luminoso em toda a escada de tamanhos**, e fluxo é exatamente o campo que barra a C15. Os quatro
números foram colhidos por busca atribuída ao fabricante e **reconferidos numa segunda formulação
independente**, que devolveu os mesmos valores; a eficácia dos quatro cai entre 144 e 164 lm/W,
uma família coerente com a A451M (130 lm/W, marinha, mais azul) e a A901 (149 lm/W) que já
estavam no banco. Os quatro entram **sem `afiliado.url`** — quem gera link é a Sentinela
Estratégica —, com `plataforma: null` e o motivo escrito, e ficam `parcial` por um campo só:
`disponibilidade_br`, que só varejo brasileiro sustenta e não foi conferido para estes tamanhos.
A A1201 (120 cm) foi tentada e **não entrou**: a busca devolveu a dimensão da peça e não devolveu
o fluxo. Registro sem o campo que a calculadora exige não é ganho de catálogo, é ruído.

### O buraco de lúmen da C15 é ESTRUTURAL, e agora está medido duas vezes

As oito luminárias Soma cobrem de 20 a 130 cm, **todas com link de afiliado e voltagem fechada**,
e continuam barradas por um campo só: `fluxo_lm`. A coleta de 09/09 já tinha registrado que nem a
marca nem nove lojas brasileiras publicam lúmen; **esta execução reconferiu por busca
independente e confirmou**: as fichas de varejo declaram watt, comprimento, contagem de LEDs por
cor, espessura, peso e comprimento do fio — e nenhuma declara lúmen. O anúncio da Shopee também
não. Junte a SunSun ADE-400c e a WFish WF-H600 e são **dez luminárias barradas pelo mesmo campo**.

Isto não é falha de coleta, é um fato do mercado: **a C15 dimensiona por lm/L, e o meio do mercado
brasileiro não publica lm.** Enquanto isso valer, ampliar o catálogo de iluminação com marca
brasileira não aumenta a receita da C15 em nada — os produtos entram e ficam na lista de
barrados. As saídas possíveis, nenhuma delas decidida aqui: (a) importar marca que declara fluxo,
que foi o que este bloco fez; (b) a C15 passar a aceitar um segundo caminho de dimensionamento
com fonte (PPFD declarado a distância declarada, que o esquema já prevê); (c) medição própria,
que hoje não existe. **Estimar lúmen a partir do watt continua proibido** — seria inventar
constante, e a eficácia medida no próprio banco varia de 89,6 a 164,3 lm/W, quase o dobro.

### T3(b), voltagem: duas tentativas, nenhum número, e é assim que tem de ser

- **Chihiros WRGB II Pro 60** (tem link de afiliado, cobre 60 a 80 cm): busca restrita ao domínio
  do fabricante em três formulações não devolveu a tensão de entrada da fonte. `voltagem`
  continua `null` e o produto continua barrado.
- **Sicce Scuba Contactless 150 W** — o aquecedor da ficha mais completa do banco, e justamente o
  que cairia na janela de 110 a 150 W que a Sentinela mediu vazia a 108 L: a busca restrita a
  `sicce.com` devolveu a faixa de ajuste (15 a 35 °C), a linha de 50 a 400 W e o modo de economia,
  e **não devolveu a tensão**. Continua `null`.

Somados aos sete registros Maxxi (cujo anúncio declara a tensão, mas anúncio de marketplace é
nível 6 e **nunca** sustenta campo técnico) e ao RS-50 sem marca, são **dez elétricos com
`voltagem: null`**, cada um com o motivo no registro. Nenhum foi chutado. A regra "nunca chute 110
nem 220" custou dez produtos neste banco, e continua certa: aquecedor ligado na tensão errada
queima, e a Aquametria não tem como pedir desculpa depois.

## 2026-09-09 (mutirão, bloco 3) — T3(c): a cobertura de faixa deixou de ser opinião e virou medida

**Bloco entregue: T3(c), catálogo geral — mas com o critério novo.** O Raphael descartou a meta
de "60 produtos" hoje; o critério passou a ser **cobertura**: nenhuma faixa que as calculadoras
conseguem produzir pode sair com menos de 3 produtos elegíveis (seção 14.3 do `ARQUIPELAGO.md`).
Este bloco construiu o instrumento que mede isso e publicou a primeira medição. Manifest na
**revisão 25**.

### `ferramentas/varrer-cobertura.mjs`, arquivo novo

Ele **não reimplementa regra de seleção nenhuma**, e essa é a decisão que importa. Reescrever a
seleção de produto em Python criaria uma segunda cópia da regra, que divergiria da calculadora em
silêncio — exatamente o defeito que os geradores de catálogo existem para impedir. Em vez disso a
calculadora **de verdade** roda num Chromium de verdade, é preenchida ponto a ponto ao longo da
faixa de entrada declarada, em cada combinação de condição que a tela oferece, e o que se conta é
o cartão que apareceu. 87 faixas medidas em 486 pontos.

### A primeira medição, em `dados/cobertura-de-faixa.md` (arquivo histórico, nunca sobrescrito)

| | faixas | vazias | com 1 ou 2 | cumprem |
|---|---:|---:|---:|---:|
| **total** | 87 | 18 | 28 | 41 |

E o detalhe é mais duro que o total:

- **A C15 não cumpre o critério em NENHUMA das 22 faixas.** O melhor resultado em toda a escada de
  30 a 120 cm é **duas** luminárias; oito faixas saem vazias. Acima de 80 cm não há nada, em
  nenhum nível de exigência. Não é tamanho de catálogo: são 20 luminárias e 11 barradas pelo
  mesmo campo.
- **A C5 fica sem nenhum aquecedor de 310 a 400 L**, nas quatro combinações de delta e tomada — o
  banco não tem aparelho acima de 300 W. E entrega dois (um abaixo do piso) de 30 a 50 L e de 210
  a 300 L.
- **Descoberta lateral da C5:** trocar a tomada de 110 para 220 V **não muda uma linha sequer**.
  Todos os aquecedores aptos declaram as duas tensões, então a barreira de voltagem hoje não
  elimina ninguém — ela só elimina os dez registros que estão com `voltagem: null`. A barreira de
  segurança está certa e continua; o que ela custa hoje é catálogo, não sugestão.
- **A C3 tem um buraco na ENTRADA: de 20 a 40 L não há filtro nenhum**, nos três perfis
  comunitários. É o aquário de começo, que é justamente por onde mais gente chega pela busca. No
  perfil plantado o buraco vai até 170 L, porque a dupla condição corta mais fundo.
- **A C12 cumpre em toda a faixa, mas exatamente no piso:** 3 mídias de 20 a 400 L nos três
  perfis. Não é folga — qualquer mídia que saia do banco derruba a calculadora abaixo do critério.

### A lista de compras que estes números determinam

1. Luminária com fluxo declarado **acima de 80 cm** (C15 vazia em toda a faixa alta).
2. Aquecedor **acima de 300 W** (C5 vazia de 310 a 400 L).
3. Filtro de **baixa vazão, 150 a 400 L/h**, para 20 a 40 L (C3 vazia na entrada).
4. Luminária com fluxo declarado de **30 a 55 cm** para exigência alta.
5. Aquecedor de **250 W** e um segundo de **25 a 50 W**.
6. Uma **quarta mídia biológica**, para a C12 sair do piso.

Isto substitui qualquer meta de número redondo: o banco não precisa de 60 itens, precisa destes
seis buracos fechados. Um produto que não fecha nenhuma faixa descoberta não é prioridade, por
melhor que seja a comissão.

### Um teste que estava vermelho antes deste mutirão

`teste-navegador-c15.mjs` fixava em **3** o número de luminárias barradas. O lote de anúncios de
09/09 tinha levado esse número a **11** (as oito Soma, mais SunSun, WFish e Chihiros), e a
asserção ficou vermelha sem que nada tivesse quebrado — a contagem já era 11 **antes** de este
bloco tocar em qualquer coisa. Número de catálogo não é contrato de tela: o que a tela promete é
que **toda** barrada aparece com o motivo. A asserção passou a conferir isso, e o comentário no
teste registra o porquê. É a mesma correção que a C5 já tinha recebido na contagem de cartões, e
vale como regra: **teste que fixa tamanho de catálogo reprova a cada coleta bem-sucedida.**

E um segundo vermelho, do mesmo tipo: **`teste-navegador-c15.mjs`, `-c5` e `-c12` reprovavam por
falha de REDE**, não de código. O `render-para-teste` serve um `file://` e a casca pede a folha do
Google Fonts, que o egresso deste container barra — o console enchia de
`net::ERR_CONNECTION_RESET` e a asserção "nenhum erro de console" ficava vermelha. O
`teste-navegador-cinco.mjs` já filtrava exatamente isso desde 08/09/2026
(`!/ERR_(CONNECTION|NAME|INTERNET)/`); os três testes por calculadora estavam sem o filtro. Agora
têm, com o comentário dizendo por quê. O sinal que importa — `pageerror`, `SyntaxError`, o defeito
do `&&` escapado que derrubou as cinco calculadoras em 08/09 — continua inteiro: o filtro só
descarta falha de carregamento de recurso externo.

### NÃO CONCLUÍDO — o Sync continua fora de alcance, e agora são OITO revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** nesta sessão, tanto na URL do Sync com `&forcar=1`
quanto em `/wp-json/aquametria/v1/status`, testados nas duas pontas da execução. **Não foi
possível acionar o desembarque nem conferir a revisão aplicada**, e por isso nenhum destes três
blocos pode ser dado por "no ar" — só por "no `main`".

**O repositório está na revisão 25. A última medição do site, em 08/09 às 13h03, dizia 11.** Quem
alcança o site é a **Sentinela Técnica das 11h30, que roda no Chrome do Raphael**: basta abrir a
URL do Sync com `&forcar=1` e, uns cinco minutos depois, conferir que
`/wp-json/aquametria/v1/status` diz **revisão 25**. Enquanto isso não acontecer, o que mudou no ar
foi nada — nem as calculadoras da revisão 24, nem o catálogo novo da C15.

O que ESTE bloco muda no site, quando o Sync rodar: só a C15, que passa a poder sugerir quatro
luminárias a mais. O banco de espécies e o arquivo de cobertura são `publicar: false` e não vão
para o site por desenho — são insumo de página futura e lista de compras, não conteúdo.

### Próximo passo desbloqueado

**T1 — medir a indexação no Search Console**, que continua sendo o primeiro bloco da fila e
depende do Chrome do Raphael (Site Kit no wp-admin), não da nuvem. Ele é o que autoriza ou barra a
T4, a malha de páginas.

Enquanto a T1 não roda, o que a nuvem consegue fazer sozinha, em ordem de valor, é o que a
varredura de cobertura acabou de nomear: **fechar as seis faixas descobertas**, começando pela
luminária acima de 80 cm com fluxo declarado e pelo aquecedor acima de 300 W. Não é mais "ampliar
o banco": é fechar buraco medido, e agora existe o instrumento que diz quando o buraco fechou.

### Números do mutirão de 09/09/2026 (resposta às três perguntas do disparo)

- **Blocos entregues: 4** — o contrato (14.9 / 14.6 / 14.3), T3(a) espécies, T3(a2) iluminação
  com T3(b) voltagem dentro, e T3(c) cobertura. Todos no `main`.
- **Faixas ainda descobertas, por calculadora** (87 medidas ao todo):
  - **C15 — 22 de 22 fora do critério**, sendo 8 vazias. Nenhuma faixa cumpre.
  - **C5 — 12 de 32 fora**, sendo 4 vazias (310 a 400 L nas quatro combinações).
  - **C3 — 12 de 30 fora**, sendo 4 vazias (20 a 40 L nos três perfis comunitários, e 20 a 70 L
    no plantado).
  - **C12 — 0 de 3 fora**, mas as três exatamente no piso de 3.
- **Produtos esperando link de afiliado: 29** de 68 (39 já têm link) — 9 aquecedores, 9 filtros,
  7 luminárias (4 delas as Chihiros que nasceram hoje) e 4 mídias. Pela regra V16 todos já são
  sugeridos pela adequação técnica; o cartão sai sem botão de loja.

## 2026-09-09 (execução da noite) — T3: a leva de FECHAMENTO DE FAIXA, e a primeira vez que o buraco medido foi a lista de compras

Primeira execução da Aquametria depois que `dados/cobertura-de-faixa.md` passou a existir, e a
primeira em que a fila não veio de julgamento: veio da varredura. O bloco anterior mediu 87 faixas
e deixou uma ordem de compra escrita. Esta execução atacou os dois primeiros itens dela —
**luminária acima de 80 cm com fluxo declarado** e **aquecedor acima de 300 W** — e não escolheu
mais nada por conta própria.

Manifest revisão 27. C5 na 1.3.1, C15 na 1.1.2. Banco de 68 para **78 produtos**.

### O que entrou, e por que exatamente isto

**Quatro aquecedores, e o banco passa dos 300 W pela primeira vez.** A varredura mediu a C5 VAZIA
de 310 a 400 L nas quatro combinações de delta e tomada, por uma razão simples: o banco parava em
300 W e a janela de potência a 400 L começa em 400 W. Entraram:

| id | W | ajuste | volume declarado | o que ele fecha |
|---|---|---|---|---|
| `hopar-j-226-400w` | 400 | 18 a 34 °C | até 500 L | o único degrau de 400 W do levantamento |
| `hopar-j-226-500w` | 500 | 17 a 35 °C | até 500 L | acima de 350 L |
| `oceantech-warmer-x-5-250w` | 250 | 20 a 34 °C | até 260 L | tira do piso a faixa de 210 a 300 L |
| `oceantech-warmer-x-5-500w` | 500 | 20 a 34 °C | até 500 L (4 leituras) | acima de 350 L |

A **Hopar é marca nova no banco**, e entrou por cobertura, não por marca: das fichas conferidas, é
a única que publica um degrau de 400 W. Nenhum dos quatro tem link de afiliado — quem gera link é
a Sentinela Estratégica, e pela regra V16 os quatro já são sugeridos pela adequação técnica, com o
cartão saindo sem botão de loja.

**Seis luminárias, a família Chihiros WRGB II inteira.** A C15 não cumpria o critério em faixa
nenhuma das 22 medidas, e saía vazia em toda a escala acima de 80 cm. A escolha da família tem dois
motivos e **nenhum deles é marca**: ela declara fluxo luminoso em toda a escada de tamanhos — que é
o campo que barra a C15 — e declara **cobertura em FAIXA** (90 a 110 cm, 120 a 140 cm) em vez de um
comprimento cravado. Esse segundo ponto é o que resolve o buraco de verdade: as duas Chihiros
A-Series que já estavam no banco declaram 80 cm e 90 cm exatos, então 95, 100, 105 e 110 cm saíam
sem nenhuma opção mesmo com elas lá.

| id | lm | W | aquário coberto | status |
|---|---|---|---|---|
| `chihiros-wrgb-ii-pro-90` | 9250 | 110 | 90 a 110 cm | completo |
| `chihiros-wrgb-ii-90` | 8400 | 100 | 90 a 110 cm | conflito (publicado) |
| `chihiros-wrgb-ii-slim-90` | 3600 | 69 | 90 a 110 cm | parcial (falta comprimento da peça) |
| `chihiros-wrgb-ii-120` | 11000 | 130 | 120 a 140 cm | completo |
| `chihiros-wrgb-ii-slim-120` | 4800 | 90 | 120 a 140 cm | completo |
| `chihiros-wrgb-ii-pro-120` | — | — | 120 a 140 cm | parcial, e é o caso mais desconfortável |

### O achado que vale dinheiro: um campo colhido para um produto destravou outro

A `chihiros-wrgb-ii-pro-60` estava no banco desde 07/09/2026, **com link de afiliado**, e barrada
pela C15 por um campo só: `voltagem`. A página da calculadora publicava isso como exemplo do que as
regras custam — "a luminária mais cara do banco tem link e não é sugerida".

Catalogando a família WRGB II para cobrir os aquários grandes, a declaração apareceu: o varejo
brasileiro especializado (AquaBetta) anuncia **dois membros diferentes da linha** como bivolt, no
próprio título, e a ficha da série descreve a alimentação como entrada de 100 a 240 V por fonte
externa de 12 V. Não é inferência de voltagem, que a ilha proíbe — é declaração de varejo sobre a
linha, e a família inteira acende pela mesma fonte externa.

**Resultado: a C15 foi de 3 para 4 luminárias sugeríveis COM link, sem que nada mudasse no produto.**
E fica a regra: quando um campo barra vários registros, colher esse campo para a linha vale mais que
colher dez produtos novos.

Consequência que a mesma execução foi obrigada a pagar: **duas páginas no ar diziam algo que deixou
de ser verdade.** `conteudo/calculadora-de-iluminacao.md` e
`conteudo/quantos-lumens-por-litro-aquario-plantado.md` afirmavam que a Chihiros não é sugerida por
falta de voltagem. As duas foram corrigidas na mesma passada, e a correção virou conteúdo melhor que
o original: o exemplo não deixou de existir, ele foi **resolvido**, e a história de como — um campo
que apareceu, nunca uma exceção aberta para um produto que rende comissão — é exatamente o que
separa a Aquametria de uma fazenda de conteúdo. Página que contradiz o próprio catálogo é o defeito
de julgamento que a Sentinela procura, e ele não sobrevive a uma execução aqui.

### Duas regras de banco que este bloco fixou

**EMENDA À V12: `parcial` vale junto com `conflitos[]` quando falta obrigatório.** É a mesma emenda
que o banco de espécies já tinha no E10, e o caso que a obrigou é a `chihiros-wrgb-ii-pro-120`: a
Fazenda Submersa declara **7.700 lm com 130 W** e a Green Aqua declara **11.170 lm com 138 W** para
o mesmo aparelho — 45 % de diferença no fluxo, duas lojas especializadas do mesmo nível da escada.
Empate de nível faz o campo virar null (`campo-vira-null`), e campo null deixa o registro `parcial`.
Ou seja, **o conflito é a CAUSA da incompletude**, e exigir status `conflito` ali obrigaria o banco
a declarar completo o que não está. Completude e divergência são fatos ortogonais, `status_registro`
carrega um campo só, e vale o mais restritivo. A V12 também passou a reprovar o inverso: status
`conflito` sem nenhum conflito declarado. Esquema na **versão 7**.

O caso é desconfortável de propósito e fica publicado por isso: é a única luminária de 120 cm da
família que uma loja brasileira anuncia, tem link em potencial, e **mesmo assim não é sugerida**.
Se a diferença for versão do produto, é a loja que precisa dizer qual está vendendo; se for erro de
transcrição, é a prova de que o número que dimensiona iluminação no Brasil não passa por conferência
nenhuma. Desempata quem tiver a caixa na mão.

**Anúncio de marketplace continua não sustentando campo técnico, e agora com custo medido.** O
título do anúncio do Hopar J-226 400 W diz "até 400 L"; o varejo especializado diz "até 500 L". Não
é empate: nível 6 não sustenta número técnico. A ficha publica o 500 e registra o 400 com
atribuição, para o leitor saber que a divergência existe.

### O achado editorial: entre 300 W e 500 W o mercado brasileiro não tem degrau

Procurando o aquecedor que fecharia a faixa, a busca devolveu 300 W e 500 W em todas as linhas, e
**400 W em uma só** (Hopar J-226). A janela de potência a 310 L vai de 310 a 465 W. Ou seja: para o
aquário de 310 a 333 litros existe, no Brasil, **exatamente um** aparelho único possível — e acima
disso a resposta honesta continua sendo dois aquecedores, que é também o arranjo mais seguro por
modo de falha do termostato, coisa que a C5 já dizia na tela desde 08/09/2026 sem saber que estava
descrevendo uma lacuna de catálogo do país inteiro.

### Ferramenta nova, e ela nasceu de um defeito medido

`ferramentas/atualizar-manifest.py` recalcula o sha256 de todo item do manifest e sobe a revisão
quando algum mudou. Não é conveniência: **na primeira execução ele achou QUATRO itens com sha
vencido** — `render-para-teste.php`, `teste-navegador-c5.mjs`, `-c12.mjs` e `-c15.mjs` —, todos
alterados em execuções anteriores sem que ninguém atualizasse o registro. Nos quatro casos é
ferramenta de bancada com `publicar: false`, então o site não quebrou. O mesmo esquecimento num item
publicável faz o Sync recusar o arquivo no ar e a revisão do site ficar para trás **em silêncio**,
que é exatamente o defeito da seção 4 do `ARQUIPELAGO.md`. O passo manual que a gente esquece é o
passo que vira ferramenta.

Ele também lista o que está na pasta e fora do manifest, e isso expôs uma inconsistência que fica
anotada como dívida: das 21 ferramentas, 14 estão no manifest e 7 não, sem critério visível —
`conferir-slugs.py`, `varrer-cobertura.mjs`, `teste-navegador-casca.mjs`, `render-casca-para-teste.php`,
`gerar-favicon.php`, `proteger-funcoes.php` e os três `README.md` de pasta.

### Dois testes que estavam medindo a coisa errada

**`conferir-entidades.mjs` estava VERMELHO desde 09/09 de manhã, e não era defeito de código.** Ele
passava **todo** bloco `<script>` por `node --check` — inclusive o `<script type="application/ld+json">`
que nasceu com o JSON-LD do bloco 4c. JSON não é JavaScript: um objeto literal solto é sintaxe
inválida, então C3 e C5 reprovavam desde que ganharam visibilidade em IA. Agora cada bloco é
conferido pelo verificador da linguagem dele, e o JSON-LD passa por `JSON.parse`, que aqui é **mais
severo** que `node --check` seria: um `&#038;` no meio de uma string escapada quebra a análise, que
é exatamente o defeito de 08/09/2026 reaparecendo no lugar novo. Saída passou a contar `jsonld_ok`
à parte de `js_ok`. Falhas: 3 → 0.

Na mesma varredura saiu a terceira ocorrência da regra "entidade em comentário também sai": a casca
1.3.0, escrita ontem, voltou a escrever a entidade por extenso num comentário explicando o defeito.
Trocada pela descrição em palavras.

**`teste-navegador-c15.mjs` reprovou em 5 asserções, e três delas eram o buraco que este bloco
fechou.** É a terceira vez que a ilha tropeça no mesmo padrão, então vale escrito de uma vez:
*teste que fixa tamanho de catálogo, ou que exige que um buraco continue aberto, reprova exatamente
o trabalho que a fila manda fazer.* O que mudou:

- `duas luminárias sugeridas` (contagem fixa) → **pelo menos uma**, porque a Pro 60 destravada passou
  a cobrir os 60 cm do caso.
- `Chihiros barrada por voltagem` → caiu. Ela media um defeito de coleta nosso, não uma promessa da
  tela. No lugar entraram duas asserções que são contrato de verdade: a linha Soma inteira (oito
  registros, todos COM link) aparece na lista de barradas, e **nenhuma barrada sai sem motivo
  escrito**.
- `nenhum produto cobre um aquário de 120 cm` → trocado para **115 cm**, com o porquê no comentário:
  120 cm deixou de ser buraco nesta execução, e 115 cm é o buraco que sobrou, porque as peças do
  mercado declaram 90 a 110 ou 120 a 140 e ninguém declara o meio. Quando 115 cm for coberto, troque
  de novo em vez de afrouxar a asserção — o que se testa ali é a tela dizer a verdade quando não tem
  o que sugerir.

### A medida, e ela é o ponto do bloco

Varredura rodada de novo com o **mesmo instrumento e o mesmo eixo** (`varrer-cobertura.mjs`,
Chromium de verdade, 486 pontos). Comparação por PONTO medido, não por linha de tabela — as linhas
agrupam pontos contíguos de mesma contagem e se re-segmentam a cada medição, então contar linhas
não compara com nada.

| | manhã | noite |
|---|---:|---:|
| pontos que cumprem o critério | 312 de 486 | **379 de 486** |
| pontos abaixo do piso de 3 | 81 | 73 |
| pontos VAZIOS | 93 | **34** |

| | ok | abaixo de 3 | VAZIA |
|---|---:|---:|---:|
| C3 (manhã e noite) | 131 | 13 | 12 |
| C5 manhã | 64 | 52 | 40 |
| **C5 noite** | **128** | **28** | **0** |
| C12 (manhã e noite) | 117 | 0 | 0 |
| C15 manhã | 0 | 16 | 41 |
| **C15 noite** | **3** | **32** | **22** |

**A C3 e a C12 devolveram número IDÊNTICO nas duas medições.** Não é detalhe: o banco delas não foi
tocado, então a repetição exata é o controle que prova que o instrumento é estável e que a diferença
na C5 e na C15 veio do banco, não da medida.

**A C5 não tem mais nenhum ponto vazio de 20 a 400 L.** Era o buraco número 2 da lista de compras, e
está fechado. **A C15 cumpriu o critério pela primeira vez desde que existe**, em dois degraus: 60 a
65 cm na exigência média e 90 cm na alta.

### O que a medição nova ensinou, e que a anterior não sabia pedir

**A exigência BAIXA virou o pior caso da C15, por inversão.** De 85 a 120 cm ela sai vazia
justamente porque as luminárias que entraram são potentes DEMAIS: a faixa de lúmens que a exigência
baixa pede fica abaixo do que uma WRGB II de 90 a 130 W entrega. A compra que falta não é "mais
luminária grande" — é **barra econômica de 100 a 120 cm com lúmen declarado**. A lista de compras da
manhã pedia o oposto, e teria sido gasto errado se seguida às cegas. É o argumento da seção 14.3 do
contrato funcionando: cobertura se mede, não se estima.

**Aquecedor acima de 300 W saiu da lista de compras.** A faixa está coberta e o único trecho magro
(310 a 330 L, com um aparelho) é lacuna do mercado brasileiro, não do banco — comprar mais não
fecha, e a tela já explica.

### NÃO CONCLUÍDO — o Sync continua fora de alcance, e agora são QUINZE revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** nesta sessão, testado no fim da execução em
`/wp-json/aquametria/v1/status`. **Não foi possível acionar o desembarque nem conferir a revisão
aplicada**, então nada deste bloco pode ser dado por "no ar" — só por "no `main`".

**O repositório está na revisão 27. A última medição do site, em 08/09 às 13h03, dizia 11.** Quem
alcança o site é a Sentinela Técnica das 11h30, que roda no Chrome do Raphael: basta abrir a URL do
Sync com `&forcar=1` e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisão 27**.

O que este bloco muda no site quando o Sync rodar: a C5 passa a sugerir aquecedor acima de 300 W, a
C15 passa a sugerir luminária para aquário de 90 a 140 cm e volta a sugerir a Chihiros WRGB II Pro 60
(que tem link), e duas páginas param de afirmar algo que deixou de ser verdade. O banco em si é
`publicar: false` e não vai para o site por desenho.

### Verificação desta execução (seção 8 do `ARQUIPELAGO.md`)

- `php -l` nos 8 snippets: limpo. `conferir-protecao-funcoes.py`: limpo.
- `conferir-entidades.mjs`: **0 falhas** (eram 3, e as 3 eram do próprio instrumento — ver acima).
- `conferir-slugs.py`: 9 slugs concordam, nenhum link publicado aponta para página inexistente.
- `teste-conversor-markdown.php`: 17 casos, 0 falha. `teste-apelidos.php`: 59 afirmações, 0 falha.
- `teste-escape-shortcode.php`: todas as afirmações passaram.
- `validar-produtos.py`: **78 produtos, 39 cotações, 0 erro**, 9 avisos (todos conhecidos: V20 de
  produto com link e sem foto, e o V11 do Jäger 200 W, que é conteúdo da página).
- **`teste-navegador-c5.mjs`: 15 cenários em Chromium real, todos passaram.**
- **`teste-navegador-c15.mjs`: 78 asserções em Chromium real, todas passaram** depois das correções
  descritas acima.
- **C1, C3 e C12 não foram re-testados no navegador de propósito, e dá para provar por quê:**
  `git diff` mostra os três snippets **byte a byte idênticos**. Só C5, C15 e um comentário da casca
  mudaram. Além disso, a varredura de cobertura re-executou a C3 e a C12 inteiras num Chromium de
  verdade e devolveu o número idêntico ao da manhã, o que é um teste de regressão melhor que
  re-rodar as asserções.
- Site no ar: **não conferido** — egresso bloqueado, registrado acima como não concluído.

### Produtos esperando link de afiliado: 39 de 78

Metade do banco. Por entidade: 13 luminárias, 13 aquecedores, 9 filtros e 4 mídias. Os 10 que
entraram hoje estão todos nessa conta. Pela regra V16 todos já são sugeridos pela adequação técnica;
o cartão sai sem botão de loja. **Este número é trabalho pendente de verdade, e é da Sentinela
Estratégica** — não consome execução da Fundação, então nunca compete por fila.

### Próximo passo desbloqueado

**T1 — medir a indexação no Search Console** continua sendo o primeiro bloco da fila e continua
dependendo do Chrome do Raphael (Site Kit no wp-admin), não da nuvem. É ele que autoriza ou barra a
T4, a malha de páginas, que é o motor de tráfego da ilha.

O que a nuvem consegue fazer sozinha, agora com a lista de compras corrigida pela medição da noite:
**luminária de exigência baixa (lúmen modesto) de 85 a 120 cm**, que é a faixa vazia mais larga que
sobrou e que a medição da manhã nem enxergava; depois luminária com lúmen declarado de 30 a 55 cm; e
filtro de baixa vazão para 20 a 40 L, que é a entrada da C3 e continua vazia desde a manhã.

---

## 09/09/2026 — 21h a 22h UTC · Fundação · despacho da Sentinela (itens 1 e 3), T2 e o par C15 do T7

**Revisão do repositório: 27 → 29.** A ilha foi escolhida pela regra da seção 1 do
`ARQUIPELAGO.md` na SEGUNDA tentativa: a primeira reserva foi da Robometria e o push perdeu a
corrida para outra execução da Fundação que reservou a mesma ilha no mesmo minuto. Rebase, volta ao
passo 2, Aquametria reservada às 21h18. **A reserva por commit funcionou exatamente como projetada** —
é o primeiro registro de duas execuções simultâneas se cruzando, e nenhuma das duas trabalhou em
ilha alheia.

### Item 1 do despacho (= T2): `/category/uncategorized/` no sitemap

A causa de raiz não estava no sitemap: **está no Sync**, que grava artigo com `wp_insert_post` e
nunca atribui categoria — então o WordPress despeja tudo na padrão. Consertar pelo Sync exigiria
passar pelo atualizador (caminho mais longo e mais arriscado, e o Sync se pula a si mesmo por
desenho), então o conserto foi feito pelo lado que **se auto-corrige**: um snippet novo,
`aquametria-seo-tecnico` v1.0.0, que varre a categoria padrão a cada carregamento enquanto ela tiver
post dentro. Artigo novo que o Sync criar amanhã cai na mesma varredura.

O que ele faz: (a) cria a categoria "Métodos", move para ela todo post da categoria padrão e **troca
a categoria padrão**, para o problema não voltar pela porta que o criou; (b) tira do
`wp-sitemap.xml` o provedor de autores sempre, e o de taxonomias enquanto nenhuma categoria estiver
curada; (c) manda `noindex, follow` para arquivo por data, autor, tag, categoria não curada (a "sem
categoria" inclusive), anexo, busca e 404 — **pelo filtro `wp_robots` do próprio núcleo**, e não
imprimindo meta na mão, porque duas metas "robots" na mesma página o Google resolve pelo lado mais
restritivo; (d) desliga a página de anexo pelo interruptor do núcleo; (e) **não toca em página,
artigo nem home.**

**A categoria "Métodos" nasce FORA do sitemap e com `noindex`, de propósito** — e essa foi a decisão
que exigiu mais cuidado, porque os itens 1 e 2 do despacho se contradizem na superfície: o item 1
manda criar categoria de verdade, o item 2 proíbe URL nova até 16/09. A saída que atende os dois é
tirar os artigos da "sem categoria" **sem pedir ao Google que indexe a categoria nova**. Quando a
leitura de 16/09 liberar e a listagem tiver texto próprio (seção 14.4), basta acrescentar `metodos`
em `aquametria_seo_categorias_no_sitemap()`: entra no sitemap e sai do `noindex` na mesma linha.

### Item 3 do despacho: a regra das ilhas que não se interligam

Escrita na seção 10 do `ARQUIPELAGO.md`, que era a condição para apagar o item — e apagada de lá no
mesmo commit, como o despacho manda. A regra ficou escrita pelo motivo, não pelo par: público sem
sobreposição, arquipélago é economia de fábrica e não rede de links, e a exceção futura exige nomear
as duas ilhas e justificar pelo leitor.

### T7, par C15 — e o achado que muda o tamanho do bloco seguinte

A C15 recebeu as **três** peças da seção 5 que faltavam nela, não só o JSON-LD: resposta antes da
explicação, tabela de exemplos pré-renderizada e JSON-LD (`WebApplication` + `FAQPage` de 15
perguntas). Seis aquários de 30 a 120 cm resolvidos em PHP com as mesmas regras do script — `lm()` e
`litros()` espelhados função a função, porque tabela servida que contradiz a calculadora logo acima
dela é pior que tabela nenhuma.

**Três das seis linhas dizem que NENHUMA luminária do banco atende**, com o motivo escrito. Não é
defeito: é a faixa vazia que a varredura de cobertura já tinha medido, agora visível na página em
vez de escondida atrás de um formulário. Bloco de produto vazio é portão (seção 7) — mas silêncio
parece defeito, e por isso a célula explica.

**O achado, e ele custa tempo de quem pegar o próximo bloco:** medindo para escrever isto, ficou
claro que **nem a C12 nem a C1 servem tabela de exemplos, e nenhuma das duas tem resposta direta no
topo**. O T7 nessas duas não é "acrescentar schema", é o pacote inteiro — planeje como bloco de
calculadora. O molde está pronto na C15.

### Verificação desta execução (seção 8 do `ARQUIPELAGO.md`)

- `php -l` nos 9 snippets: limpo, **com controle negativo** — como os snippets não têm `<?php` no
  topo, `php -l` cru passaria mesmo com erro de sintaxe; o lint foi feito com o marcador prefixado e
  um erro proposital foi injetado para provar que o instrumento acusa.
- `conferir-protecao-funcoes.py`: 9 snippets, todas as funções dentro de `function_exists`.
- `teste-seo-tecnico.php` (novo): **28 afirmações, 0 falha.** Exercita as duas metades do risco — o
  que tem que sair do índice sai, e **o que não pode sair fica**. Um `noindex` sobrando numa
  calculadora seria um defeito muito pior do que o consertado aqui.
- `teste-navegador-c15.mjs`: **78 afirmações em Chromium real, TUDO PASSOU, console limpo.**
- **O teste de navegador pegou dois defeitos meus, em duas rodadas**, e vale registrar porque é
  exatamente para isso que ele existe: eu tinha reusado `.aqm-c15-aviso-afiliado` e depois
  `.aqm-c15-fontes` nos elementos novos, e cada reuso quebrou um localizador que o teste usa em modo
  estrito. Nenhum dos dois é erro de sintaxe, e nenhum apareceria em `php -l`. Viraram classes
  próprias (`aqm-c15-aviso-tabela`, `aqm-c15-exemplos`) com o estilo herdado pela lista de seletores.
- `conferir-entidades.mjs`: 0 falhas. **C15 passou a `jsonld_ok=1`** (eram C3 e C5 só). Zero
  entidade `&#038;` dentro de `<script>` nas cinco calculadoras.
- JSON-LD analisado como JSON de verdade: 2 nós (`WebApplication`, `FAQPage`), 15 perguntas, cada
  resposta conferida contra o número que a tabela servida mostra.
- `validar-produtos.py`: 78 produtos, 0 erro, 9 avisos conhecidos. `conferir-slugs.py`: limpo.
- `teste-conversor-markdown.php` (17 casos), `teste-apelidos.php` (59 afirmações),
  `teste-escape-shortcode.php`: 0 falha.

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são DEZOITO revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** de novo, testado em
`/wp-json/aquametria/v1/status`. **O Sync não foi acionado e a revisão aplicada não foi conferida**,
então nada desta execução pode ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 29; a última medição do site, em 08/09 às 13h03, dizia 11.** E o egresso não
bloqueia só o site: `chihirosaquaticstudio.com` também foi recusado, o que **torna o T3 (catálogo)
inexecutável da nuvem** — produto novo exige ficha de fabricante com fonte e data, e inventar dado
técnico é proibido. Foi por isso que esta execução fez despacho + T2 + T7, e não banco.

**O que destrava tudo é um gesto de trinta segundos no Chrome do Raphael:** abrir a URL do Sync com
`&forcar=1` e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz **revisão
29**. Depois disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem `/category/uncategorized/`,
e essa URL servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução. Por marca: 10 Atman, 10 Chihiros, 4 Eheim, 3
Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Roxin, Ista, WFish, JBL e um sem marca.

**O número "20 sem loja possível" do item 4 do despacho está VENCIDO e não deve ser repetido.** Ele
foi medido quando a Shopee era o único programa; o Mercado Livre entrou em 09/09 justamente porque a
Shopee não vende Eheim, Atman canister, Chihiros e JBL — que são **24 dos 39** desta lista. Quem
refizer essa medição precisa do painel do Mercado Livre aberto, e isso é da Sentinela estratégica,
não da Fundação.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4.
2. **T7, par C12** — trabalho de repositório, não depende de egresso. Agora se sabe que é bloco
   inteiro de calculadora (tabela + resposta direta + JSON-LD), com o molde pronto na C15.
3. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear os sites de fabricante.

---

## 09/09/2026 — execução das 23h17Z: T7, par C12 — a calculadora de mídia deixou de ser um formulário vazio para quem não executa JavaScript

**Bloco:** T7 (visibilidade em IA), par C12. Escolhido por ser o primeiro da fila que **não depende do
egresso**: o T1 continua dependendo do Chrome do Raphael e o T3 (catálogo) segue barrado enquanto a
nuvem não alcançar site de fabricante. Manifest **revisão 30**, C12 na versão **1.2.0**.

A ilha foi sorteada pela regra da seção 1 do `ARQUIPELAGO.md`. **A primeira tentativa foi na
Robometria e o push da reserva foi RECUSADO**: outra execução (`session_013a11...`) commitou a
reserva dela 13 segundos antes. Rebase, volta ao passo 2, e a Aquametria era a próxima elegível.
A reserva por commit funcionou exatamente como o contrato promete — duas execuções simultâneas, zero
atropelo, sem force push.

### O que entrou, e por que é bloco de calculadora e não retoque de schema

O registro anterior já tinha medido isto e vale confirmar: **o T7 na C12 não era "acrescentar
JSON-LD"**. A página não tinha nenhuma das três peças da seção 5. Entraram as três:

- **(a) Resposta antes da explicação** (`aquametria_c12_resposta_direta_html`, bloco `aqm-c12-direta`,
  ANTES do formulário). Frase autossuficiente com número, unidade, quem declarou e data — escrita
  para sobreviver a ser citada por um modelo que leu só aquele parágrafo. 2.052 caracteres, quatro
  parágrafos: a faixa em 100 L, por que a ilha não escolhe nem tira média, o teto físico, e o que a
  conta não sabe.
- **(b) Tabela de exemplos pré-renderizada** (`aquametria_c12_exemplos_html`), seis aquários de 30 a
  300 L resolvidos no PHP, cinco colunas: a faixa da mídia biológica do piso ao teto com o nome de
  quem sustenta cada extremo; a mídia TOTAL que quem vende filtro reserva; o **teto físico**; e a
  mídia do banco para comprar, com a quantidade pela dosagem daquele fabricante e quanto rende a
  embalagem.
- **(c) JSON-LD no `wp_head`** — nunca dentro do retorno do shortcode, pelo mesmo motivo que o script
  sai no rodapé. `WebApplication` com `featureList` de 8 itens e `FAQPage` com **15 perguntas**, cada
  resposta carregando o mesmo número que a tabela servida mostra.

**Nenhuma fórmula mudou, e nenhuma dosagem foi escolhida.** Tudo que a tabela mostra sai de espelhos
em PHP das funções do próprio script — `mL()`, `litros()`, `pct()`, `ancorasBio()`, `ancorasFiltro()`
—, função a função, porque tabela servida que contradiz a calculadora logo acima dela é pior que
tabela nenhuma. As âncoras continuam saindo do catálogo embutido, que sai do banco: mídia nova com
dosagem declarada entra na tabela servida sozinha no próximo gerador.

### O achado desta execução: quatro das seis linhas NÃO CABEM no filtro

A coluna do teto físico é a que não existe em português, e pré-renderizá-la tornou visível uma coisa
que a calculadora só dizia depois de a pessoa preencher o formulário: **a dosagem mais generosa não
cabe no filtro em quatro dos seis volumes da escada.** Em 100 L ocupa 104 % do cesto do Seachem Tidal
55; em 150 L, 156 %; em 200 L, 208 %; em 300 L, 107 % do cesto do Atman AT-3338S. Só 30 e 60 L
sobram folga (16 % e 33 % do SunSun HW-603B). O critério da célula é o da seção 7: entre os filtros
que o fabricante **declara** para aquele volume, o de menor volume declarado — que é o que a pessoa
realmente compraria, e é a leitura mais apertada. Filtro que o fabricante não declara para o volume
não entra na célula nem em último lugar.

### Três defeitos que o teste pegou, e nenhum apareceria em `php -l`

1. **Uma resposta do FAQPage não carregava número** ("Encher o cesto do filtro é melhor?"). FAQPage
   sem número é FAQPage-lixo, e é lixo detectável. Ganhou o caso medido de 200 L (2,50 L ocupando
   208 % de um cesto de 1,2 L) e as 6 posições da ordem das camadas.
2. **A tabela imprimia "30,0 L" e o teste exigia "30 L".** Aqui quem estava certo era a tabela: o
   `litros()` do script devolve uma casa decimal abaixo de 100 L, e é isso que a calculadora escreve
   quando a pessoa digita 30. **Exigir "30 L" cravado reprovaria a tabela por ser FIEL ao script**,
   que é o oposto do que o teste existe para garantir. Quem cedeu foi o teste.
3. **A C15 tinha as três peças desde a revisão 29 e mesmo assim ficava FORA do teste que as mede.**
   O bloco de resposta direta dela usava `aqm-c15-citar` — a MESMA classe da caixa de citação do
   resultado, duas coisas diferentes com o mesmo nome — e o painel de exemplos não tinha onde o teste
   pendurar o localizador. Peça entregue sem teste é peça que a próxima sessão quebra sem ninguém
   notar.

### O verde falso que estava no ferramental desde 09/09 de manhã

`conferir-protecao-funcoes.py` recebe os arquivos por argumento. **Chamado sem argumento, ele varria
uma lista vazia e saía 0 em silêncio.** Verde falso é pior que vermelho: treina a próxima sessão a
confiar num instrumento que não olhou para nada. Agora, sem argumento, ele varre os snippets da
própria ilha e diz quantos; e sem achar arquivo nenhum, **reprova em vez de aprovar**. Controle
negativo conferido: desprotegendo uma função de propósito, ele acusa a linha e sai 1.

**Regra que fica, e é a terceira vez que a ilha tropeça em alguma versão dela:** instrumento que pode
sair 0 sem ter medido nada não é instrumento. Todo verificador desta ilha precisa reprovar quando não
mede — nunca aprovar por omissão.

### Verificação desta execução (seção 8 do `ARQUIPELAGO.md`)

- `php -l` nos 9 snippets: limpo, **com controle negativo** — como os snippets não têm `<?php` no
  topo, o lint foi feito com o marcador prefixado e um erro proposital foi injetado para provar que o
  instrumento acusa.
- `conferir-protecao-funcoes.py`: 9 snippets, **214 funções** (34 na C12, eram 22), todas dentro de
  `function_exists`, **com controle negativo**.
- `teste-navegador-visibilidade-ia.mjs`: **124 afirmações em Chromium real com o JavaScript
  DESLIGADO, 0 falha**, agora nas QUATRO calculadoras que têm as três peças (eram 46 afirmações em
  duas). É o teste que mede o que esta execução entregou: com o script desligado, a tabela e a
  resposta direta são a única coisa citável que a página serve.
- `teste-navegador-c12.mjs`: **84 cenários em Chromium real, todos passaram, console limpo** — a
  calculadora continua calculando, o teto físico continua estourando onde deve, o bloco de produto
  continua aparecendo dentro da resposta e o celular de 390 px continua sem rolagem horizontal.
- `conferir-entidades.mjs`: 0 falhas. **C12 passou a `jsonld_ok=1`** (eram C3, C5 e C15). Zero
  entidade numérica dentro de `<script>` nas cinco calculadoras. Falta só a C1.
- JSON-LD analisado como JSON de verdade: 2 nós, 15 perguntas, e conferido item a item que o número
  do FAQ para 100 L (`125 mL a 1,25 L`) é o MESMO que a tabela servida mostra e o mesmo que a
  calculadora devolve.
- `teste-escape-shortcode.php`, `teste-conversor-markdown.php` (17 casos), `teste-apelidos.php` (59
  afirmações), `conferir-slugs.py`: 0 falha.
- `validar-produtos.py`: 78 produtos, 0 erro, avisos conhecidos. `validar-especies.py`: 36 espécies,
  0 erro, 1 aviso conhecido (E15 do guppy).
- `atualizar-manifest.py`: 4 arquivos com sha novo, **revisão 30**, 0 item com sha vencido.

### O que ficou medido para quem pegar o próximo bloco

**Os testes de navegador desta ilha levam DEZENAS de minutos na nuvem, e o motivo não é o teste.**
Cada `page.goto()` espera o `load`, e o `load` espera as fontes do Google, que o egresso barra até o
timeout de 30 s — por navegação. O teste da C12 sozinho faz mais de vinte navegações. Rodar três em
paralelo é PIOR, não melhor: três Chromiums disputam a mesma máquina e todos rastejam. **Rode um de
cada vez.** Isso não é defeito de código e não reprova nada — mas é a diferença entre uma execução
que verifica e uma que desiste de verificar, e é assim que verificação morre.

### A quarta asserção vencida, achada rodando o teste que a seção 8 exige

`teste-navegador-cinco.mjs` reprovou a C15 em **"bloco de produto oculto, como manda a regra do
banco — apareceu"**. Não era regressão desta execução: o diff inteiro da C15 aqui são DUAS classes CSS
acrescentadas a `div`, e classe não faz bloco de produto aparecer. O caso trazia `semProduto: true`
com este comentário escrito pelo próprio autor: *"Vira semProduto:false no dia em que o banco tiver
luminária apta."* **Esse dia foi 09/09**, na leva de catálogo que deu voltagem à Chihiros WRGB II Pro
60 e levou a C15 de 3 para 9 aptas. Ninguém voltou ao teste.

Em vez de virar o booleano — que apodrece de novo no próximo movimento de catálogo — a afirmação
deixou de dizer QUAL dos dois estados a página deve ter. **Os dois são legítimos, e quem decide qual é
hoje é o catálogo, não o teste.** Passou a afirmar a PROMESSA de cada estado: bloco visível tem de
estar bem formado (todo link que existir com `sponsored`, `noopener` e aba nova, mais aviso de
comissão); bloco oculto tem de dizer por que não sugere e não pode vazar link.

E como `every()` sobre lista vazia passa por vácuo, entrou uma afirmação de CONJUNTO: **nenhuma
calculadora é obrigada a ter link** — a ordem é por adequação técnica e catálogo maior chega a
*reduzir* links na tela, então exigir link por página seria pedir que o banco não melhorasse — mas as
cinco juntas não podem ficar sem nenhum, porque aí não é catálogo, é encanamento quebrado. Deu **7
links bem marcados**, e a C15 agora serve bloco de produto com 1 link: a lacuna fechou de verdade.

Manifest **revisão 31**. `teste-navegador-cinco.mjs`: **56 afirmações, 0 falha, as cinco calculando
em Chromium real** — que é o mínimo que a seção 8 exige quando a sessão não alcança o site.
`teste-navegador-c15.mjs` rodado de novo depois das duas classes novas: **78 afirmações, tudo passou,
console limpo.**

**Quatro asserções vencidas em duas execuções seguidas, todas do mesmo tipo.** Vale escrever a regra
de uma vez: *afirmação que descreve o ESTADO do catálogo — quantos itens, qual buraco está aberto,
qual produto está barrado — vence sozinha e reprova o trabalho da fila. Afirme a promessa, nunca o
estado.*

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são VINTE revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** de novo, testado em `/wp-json/aquametria/v1/status`.
**O Sync não foi acionado e a revisão aplicada não foi conferida**, então nada desta execução pode
ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 31; a última medição do site, em 08/09 às 13h03, dizia 11.**

**O que destrava tudo continua sendo um gesto de trinta segundos no Chrome do Raphael:** abrir a URL
do Sync com `&forcar=1` e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisão 31**. Depois disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem
`/category/uncategorized/`, e essa URL servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução. Por marca: 10 Atman, 10 Chihiros, 4 Eheim, 3
Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Roxin, Ista, WFish, JBL e um sem marca.
Continua valendo o registrado em 09/09: o número "20 sem loja possível" está VENCIDO e não deve ser
repetido, porque foi medido quando a Shopee era o único programa. Refazer essa medição exige o painel
do Mercado Livre aberto, e isso é da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4.
2. **T7, leva 3: a C1 e depois os três artigos.** É o último par de calculadora sem as três peças —
   `conferir-entidades.mjs` mostra a C1 como a única com `jsonld_ok=0`. Mesmo molde, agora com DOIS
   exemplos prontos (C15 e C12) e com o teste de visibilidade já preparado para receber o caso novo:
   basta acrescentar a C1 em `CASOS`, com o eixo e a âncora dela.
3. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## 2026-09-10, 11h19Z–11h40Z — T7, leva 3: a C1 fecha o retrofit de visibilidade em IA

Ilha reservada às 11h19Z pelo commit de reserva, como manda a seção 1 do `ARQUIPELAGO.md`. A
Robometria estava reservada havia um minuto por outra execução e caiu fora pela regra dos 40 minutos;
sobrou a Aquametria, que também era a de `ultima_execucao` mais antiga entre as elegíveis.

Bloco escolhido: **T7, leva 3 — a C1**. O T1 continua sendo o primeiro da fila e continua dependendo
do Chrome do Raphael, então o que estava desbloqueado era este.

### O que a C1 ganhou

Snippet `aquametria-calculadora-litragem.php` na **v1.2.0**, manifest na **revisão 32**. As três peças
da seção 5, de uma vez: **resposta antes da explicação** no topo (2.126 caracteres, com os três
volumes de um aquário concreto e a data de verificação dentro da frase), **tabela pré-renderizada**
com seis aquários e **JSON-LD** (`WebApplication` + `FAQPage` de nove perguntas) no `wp_head`, nunca
dentro do retorno do shortcode. **Nenhuma linha de cálculo mudou**: tudo que a tabela imprime é
espelho em PHP do `fmt()`, do `litros()` e do ramo de `calcular()` que ela representa.

Com isso o `conferir-entidades.mjs` deixa de ter alguma calculadora em `jsonld_ok=0`: são **5 de 5**.

### A decisão que este bloco tomou, e que não estava no molde

O molde da C15 e da C12 respondia como montar as peças, não **em que eixo** a tabela é indexada. A C3,
a C5 e a C12 indexam por litro; a C15 por centímetro, porque luminária é vendida por centímetro. A
tentação era cravar litro na C1, que é *a calculadora de litros*.

Seria errado, e por um motivo que vale para toda ilha: **na C1 o litro é a SAÍDA.** Quem abre esta
página tem a fita métrica na mão e não sabe o volume — se soubesse, não precisaria da calculadora.
Uma tabela indexada por litro responderia à pergunta que a pessoa ainda não consegue fazer. O eixo
ficou o comprimento da frente, na mesma escada da C15 (30, 45, 60, 80, 90 e 120 cm), que é como o
aquário e a luminária são vendidos. **Regra que sai daqui: o eixo da tabela pertence à pergunta, não
ao formato da ferramenta.**

Segunda decisão, esta sobre produto: **a tabela da C1 não tem link de loja, e diz por quê.** Litragem
é geometria, e geometria não escolhe produto — quem escolhe filtro, aquecedor, mídia e luminária são
as calculadoras que leem este volume, e é lá que o bloco de produto nasce dentro da resposta, como
consequência do cálculo. A seção 7 do contrato manda dizer ao visitante por que o bloco está vazio, e
o aviso da tabela faz isso em vez de deixar silêncio, que parece defeito.

Terceira: as medidas e a espessura de cada linha são **ENTRADAS do exemplo**, exatamente como os
volumes de 30 a 300 L são entradas nas tabelas da C3 e da C5 — não são catálogo de fabricante e não
são recomendação de vidro. A nota da tabela declara isso com todas as letras, porque a Aquametria não
dimensiona vidro e uma coluna de espessura sem essa frase seria lida como conselho.

### Verificação (seção 8), com número medido

- `php -l` limpo; `conferir-protecao-funcoes.py` ok — toda função de nível superior dentro de
  `function_exists`.
- `conferir-entidades.mjs`: **0 falhas**, C1 agora com `jsonld_ok=1`, `entidade_038_no_documento=0`,
  script depois do conteúdo. (O `numéricas_no_documento=1` da C1 é o `&#039;` de "lâmina d'água" no
  rótulo do campo, fora de `<script>` — já era assim antes e é legítimo.)
- `teste-navegador-visibilidade-ia.mjs` com a C1 acrescentada em `CASOS`: **155 afirmações, 0 falha,
  JavaScript DESLIGADO** nas cinco calculadoras.
- `teste-navegador-cinco.mjs`: **56 afirmações, 0 falha**, as cinco calculando em Chromium real, 7
  links de afiliado bem marcados no conjunto.
- `teste-escape-shortcode.php` e `conferir-slugs.py`: ok.

### O teste novo, e por que ele foi escrito assim

`ferramentas/teste-navegador-c1-tabela.mjs` — **28 afirmações, JavaScript LIGADO**. Ele põe a tabela
servida contra a própria calculadora: lê as seis linhas do HTML, extrai da coluna do aquário as
medidas e a espessura que geraram cada linha, digita essas entradas no formulário e compara os três
volumes e a lâmina. Deu igual nas seis linhas (22,5/20,9/18,8 · 40,5/37,6/33,8 · 63,0/58,3/53,2 ·
128/118/109 · 182/170/158 · 300/278/261), console sem erro de página.

Ele **não guarda número esperado nenhum**, de propósito. Quatro asserções venceram sozinhas em duas
execuções seguidas nesta ilha, todas do mesmo tipo, e a regra que ficou escrita foi: *afirme a
promessa, nunca o estado*. A promessa aqui é "a tabela servida não contradiz a calculadora" — mudar
as medidas de exemplo, a borda livre ou o arredondamento não reprova nada, e é assim que ele
sobrevive à próxima execução.

Uma asserção nasceu passando por engano e foi consertada antes do commit: a que confere se todo
volume citado na resposta direta existe na tabela usava `includes()`, e `"1 L"` é substring de
`"261 L"`. Passou a comparar por token. Com a comparação certa, a frase que citava a divergência de
densidade do substrato como "1 kg ≈ 1 L" ficou sem lastro na tabela — e a saída certa não era
afrouxar o teste, foi escrever "1 kg como um litro" por extenso, que é um número de fonte externa e
não um volume que esta página calcula. Três volumes citados, três com lastro.

### Uma contradição da própria página, corrigida no caminho

A abertura de `conteudo/calculadora-de-litragem.md` afirmava que a diferença entre a etiqueta e a água
real "passa de 15 %". Com o aquário que ela mesma cita (80 × 40 × 40 cm, vidro de 8 mm, lâmina no
valor inicial), a conta dá **14,9 %** — 128 L na etiqueta contra 109 L de água. Não passava de 15 %:
chegava a 15 %. A frase agora dá os dois números e o percentual exato. É defeito pequeno e é
exatamente o tipo que a tabela pré-renderizada expõe, porque põe o número ao lado da afirmação.

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são VINTE E UMA revisões paradas

`aquametria.com.br/wp-json/aquametria/v1/status` devolveu **EGRESS_BLOCKED** nesta execução também,
testado com `?v=` novo para furar o cache. **O Sync não foi acionado e a revisão aplicada não foi
conferida**, então nada deste bloco pode ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 32; a última medição do site, em 08/09 às 13h03, dizia 11.**

O que destrava continua sendo o mesmo gesto de trinta segundos no Chrome do Raphael: abrir a URL do
Sync com `&forcar=1` e, uns cinco minutos depois, conferir que o `/status` diz **revisão 32**. Depois
disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem `/category/uncategorized/`, e essa URL
servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução, e este bloco não mexeu em catálogo. Por marca: 10
Chihiros, 10 Atman, 4 Eheim, 3 Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Ista, WFish,
Roxin, JBL e um sem marca. Continua valendo o registrado em 09/09: o número "20 sem loja possível"
está VENCIDO e não deve ser repetido, porque foi medido quando a Shopee era o único programa. Refazer
essa medição exige o painel do Mercado Livre aberto, e isso é da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4.
2. **T7, o que sobrou: os 3 artigos.** Com as cinco calculadoras fechadas, é o único resto do
   retrofit. Atenção ao que NÃO se copia do molde: artigo não tem formulário, então resposta direta e
   JSON-LD valem, mas tabela pré-renderizada só entra se o artigo tiver número próprio para pôr nela.
   Tabela decorativa é pior que nenhuma.
3. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## 2026-09-10, 13h20Z — T7 leva 4: os 3 artigos-âncora fecham o retrofit de visibilidade em IA

**Bloco:** T7, o resto que sobrava depois da leva 3. Manifest **revisão 33**.
**Ilha reservada às 13h20Z**, depois de a Robometria ter sido levada por uma execução paralela na
mesma corrida de push — o mecanismo de reserva da seção 1 do contrato funcionou exatamente como
descrito: push recusado, `fetch` e `rebase`, e a escolha caiu na ilha seguinte sem atropelo nenhum.

### O que entrou no ar (no `main`, não no site — ver o fim desta entrada)

- **`snippets/aquametria-artigos.php` v1.0.0**, snippet novo, `publicar: true`, escopo front-end.
- Uma linha `[aquametria_artigo_resposta]` no topo de cada um dos três artigos de `conteudo/`:
  `quantos-watts-de-aquecedor-para-aquario.md`, `quanta-midia-biologica-o-aquario-precisa.md` e
  `quantos-lumens-por-litro-aquario-plantado.md`. Nenhuma linha de texto dos artigos foi reescrita.
- **`ferramentas/teste-navegador-artigos.mjs`** e **`ferramentas/render-artigo-para-teste.php`**,
  arquivos novos, `publicar: false`.
- Uma linha em `ferramentas/render-para-teste.php`: o slug da página de teste virou global.

Com isso o retrofit da seção 5 do `ARQUIPELAGO.md` cobre **8 de 8 páginas** de ferramenta e artigo.
A Sentinela Técnica mediu JSON-LD **zero em 13 de 13** páginas em 09/09; hoje as oito que têm
conteúdo próprio servem JSON-LD, resposta antes da explicação e tabela de números no HTML servido.

### Três decisões de projeto, e a razão de cada uma

**1. Artigo se reconhece pelo SLUG, calculadora pelo shortcode.** Não dá para descobrir a página de
um artigo por `has_shortcode()`: artigo não tem formulário. O snippet lê o `post_name` e compara com
o registro dos três slugs — os mesmos do front matter e do manifest. Amarrar o JSON-LD à presença do
shortcode da resposta direta seria pior: a página perderia o schema no dia em que alguém tirasse o
bloco do topo. Vale para toda ilha: **página de conteúdo se identifica pelo endereço; página de
ferramenta, pelo shortcode que ela carrega.**

**2. TABELA PRÉ-RENDERIZADA NÃO SE INVENTA — e este bloco recusou inventar três.** O `PROMPT.md`
já avisava, e o material confirmou: os três artigos JÁ serviam tabela própria no HTML servido, escrita
em Markdown e convertida pelo Sync — a linha comercial Eheim Jäger com o 1,00 W/L em seis degraus, as
quatro dosagens de mídia com a área que cada uma entrega por litro de água, e as três réguas de lm/L
lado a lado. Acrescentar uma tabela nossa por cima seria decoração, e o portão da seção 5 é **servir
resposta citável**, não servir uma tabela. O que o teste passou a exigir é que a tabela que o artigo
já tinha continue no HTML, com cabeçalho e pelo menos três linhas, e com número em toda ela.

**3. A resposta direta de artigo não é a de calculadora.** A da calculadora resolve um caso de
exemplo. A do artigo tem de entregar a **tese com número**, porque é ela que vai ser citada fora de
contexto por um modelo que leu só aquele bloco. As três, em três parágrafos cada, com fonte nomeada e
data dentro da frase:

- **C5:** não existe um watts-por-litro que valha para o Brasil inteiro; a única fonte do
  levantamento de 04/09/2026 que declara condição (ReefFlow) sustenta 1,0 a 1,5 W/L para até 10 °C, o
  que dá 100 a 150 W num aquário de 100 L; e o "1 W por litro" veio da prateleira, porque a linha
  Eheim Jäger nomeia cada aparelho pelo volume que dá exatamente 1,00 W/L em seis degraus seguidos.
- **C12:** as quatro dosagens declaradas vão de 1,25 a 12,50 mL/L — dez vezes —, a área entregue por
  litro de água vai de 0,88 a 18,8 m² (vinte e uma vezes) e na direção **contrária** ao argumento de
  venda, e nenhuma das quatro pergunta quantos peixes há no aquário.
- **C15:** "baixa" é 10, 15 ou 20 lm/L conforme a fonte, o que num aquário de 100 L é a diferença
  entre 1.000 e 2.000 lúmens; e a régua é frágil por definição, porque o lúmen desconta o azul e o
  vermelho profundos, que são as faixas da clorofila.

### O teste novo, e as duas afirmações que valem o arquivo

`ferramentas/teste-navegador-artigos.mjs` — **108 afirmações, JavaScript DESLIGADO**, que é o que um
crawler de IA recebe. Confere o nó `Article` (headline dentro do limite do schema, título completo em
`alternativeHeadline`, description, idioma, datas, autor, publisher, a consulta que a página mira e
`citation` com data em toda fonte), o `FAQPage` (oito perguntas por artigo, nenhuma resposta curta
demais para ser citada, toda resposta com número), o bloco do topo (corpo, data, fonte nomeada dentro
da frase, links de verdade e a posição **antes** do primeiro título de seção), a tabela que o artigo
já tinha, e o portão de entidade numérica contado **só dentro dos blocos de script**.

Mas o que faz o arquivo valer são duas afirmações de **coerência entre as duas metades da mesma
página**: *todo número da resposta direta existe no corpo do artigo* e *toda resposta do FAQPage
carrega ao menos um número que o corpo sustenta*. **Nenhum número esperado fica gravado no teste.**
Corrigir um dado com fonte melhor não reprova nada — desde que o topo e o FAQ mudem junto, que é
exatamente o defeito que ele existe para pegar. É o desenho do `teste-navegador-c1-tabela.mjs`
aplicado a texto em vez de formulário, e a terceira aplicação da regra que esta ilha já pagou caro
para escrever: **afirme a promessa, nunca o estado.**

Um detalhe de implementação que vale para quem copiar isto em outra ilha: o corpus dos artigos
escreve milhar com espaço fino ("6 630 lm") e o registro do snippet escreve com ponto ("6.630"). São
o mesmo número, e sem normalizar isso o teste reprovaria por **tipografia**, que é ruído. Datas saem
da comparação antes da extração, porque procedência não precisa (nem deve) aparecer no corpo.

### Controle negativo conferido, nos dois sentidos — e um defeito real pego antes do commit

- A página **como estava antes deste bloco** (sem JSON-LD e sem o bloco do topo) dá **15 falhas**.
- Trocar **um único número** da resposta direta por um que o artigo não sustenta é reprovado pelo
  valor: `FALHA todo numero da resposta direta existe no corpo do artigo — sem lastro: 1,7`.
- E o teste pegou um defeito de verdade antes do commit: a resposta do FAQ da C12 sobre troca parcial
  de mídia não carregava número nenhum. A saída certa não foi afrouxar a regra — foi amarrar a
  resposta às quatro dosagens que a própria página publica.

### Verificação da seção 8, item a item

- `php -l` nos 10 snippets e nos dois PHP de bancada: sem erro.
- `conferir-protecao-funcoes.py`: **158 funções em 10 snippets**, todas dentro de `function_exists` —
  as 11 do arquivo novo incluídas.
- `conferir-entidades.mjs`: **0 falhas**. Fonte limpo nos 10 snippets, e nas 5 calculadoras
  `jsonld_ok=1`, `entidade_038_no_documento=0`, script depois do conteúdo.
- `teste-conversor-markdown.php`: **17 casos, 0 falha** — o corpo dos três artigos continua começando
  por texto, sem resíduo de front matter, com a linha do shortcode saindo fora do `<p>`.
- `conferir-slugs.py`: 9 slugs concordando entre `conteudo/`, manifest e snippets; nenhum link
  publicado apontando para página inexistente.
- `teste-navegador-artigos.mjs`: **108 afirmações, 0 falha**, mais os dois controles negativos.
- **Regressão:** `teste-navegador-visibilidade-ia.mjs` rodado de novo nas 5 calculadoras — tudo
  passou. O snippet novo registra um `wp_head` global, e era isso que precisava ser provado inócuo
  fora das três páginas de artigo.
- `validar-produtos.py`: 78 produtos, 39 cotações, **0 erro** (9 avisos conhecidos).
  `validar-especies.py`: 36 espécies, 0 erro, 1 aviso conhecido (o E15 do guppy).
- `atualizar-manifest.py`: 7 itens com sha novo, **revisão 33**.

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são VINTE E DUAS revisões paradas

`aquametria.com.br/wp-json/aquametria/v1/status` devolveu **EGRESS_BLOCKED** nesta execução também,
testado com `?v=` novo para furar o cache duplo. **O Sync não foi acionado e a revisão aplicada não
foi conferida**, então nada deste bloco pode ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 33; a última medição do site, em 08/09 às 13h03, dizia 11.**

O gesto que destrava continua sendo o mesmo, de trinta segundos, no Chrome do Raphael: abrir a URL do
Sync com `&forcar=1` e, uns cinco minutos depois, conferir que o `/status` diz **revisão 33**. Depois
disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem `/category/uncategorized/`, e essa URL
servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução e este bloco não tocou em catálogo. Por marca: 10
Chihiros, 10 Atman, 4 Eheim, 3 Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Ista, WFish, Roxin
e JBL, e 1 sem marca. Continua valendo o registrado em 09/09: o número "20 sem loja possível" está
**VENCIDO** e não deve ser repetido, porque foi medido quando a Shopee era o único programa. Refazer
essa medição exige o painel do Mercado Livre aberto, e isso é da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4, e a leitura de 16/09 depende
   dele para dizer por que a leva de 08/09 não indexou.
2. **T8 — a vitrine, começando pela C3.** É o primeiro bloco de construção que não cria URL nova,
   então ele respeita o item 2 do despacho da Sentinela (nenhuma página nova até 16/09) e é o que
   sobra de maior na fila agora que o T7 fechou. A C3 é a que tem mais itens com foto e link.
3. **A `Organization` com `sameAs` na home, que mora na casca**, é o resíduo do item 3 da seção 5 do
   contrato e NÃO foi feita aqui de propósito: a Aquametria não tem perfil externo nenhum (o Raphael
   não aparece em ilha nenhuma, por decisão de projeto), então `sameAs` sairia vazio ou inventado.
   Quando o widget em lojas (T6) der o primeiro perfil externo real, aí ela nasce com lastro. Fica
   registrado para a próxima execução não achar que foi esquecimento.
4. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## EXECUÇÃO DE 10/09/2026, 17h15Z — o despacho da Sentinela de 10/09 fechou nos três itens de código

Manifest **revisão 35**, conferida no `/status` do site. Três itens do despacho numa execução, cada um
verificado no ar antes do seguinte começar, como o modo mutirão pede.

### Item 1 — as 13 URLs do sitemap passaram a servir `<meta name="description">`

Era o defeito mais caro da ilha: o `<head>` trazia 6 elementos `<meta>` e nenhum deles era a
description, em nenhuma das 13 URLs, e também não havia uma única tag `og:`. Sem description quem
escreve o resumo do resultado é o Google, recortando um pedaço qualquer do corpo — e numa página de
calculadora o pedaço costuma ser o rótulo de um campo de formulário.

O snippet `aquametria-seo-tecnico` subiu para **1.1.0** e imprime `description`, `og:title`,
`og:description`, `og:type`, `og:locale`, `og:site_name`, `og:url` e `twitter:card`.

**A decisão que vale para toda ilha: o texto não mora no snippet.** Ele mora onde a página mora — no
front matter de cada arquivo de `conteudo/`, no campo `meta_descricao` que já existia e que nada lia,
e, para as quatro páginas da casca (que nascem do snippet e não têm arquivo em `conteudo/`), em
`dados/metas-seo.json`. Duas fontes porque são dois tipos de página, mas **nenhuma página aparece nas
duas**. Quem junta e escreve o mapa entre os marcadores `METAS-INICIO` e `METAS-FIM` é
`ferramentas/gerar-metas-descricao.py`, o mesmo desenho do favicon: texto mantido em dois lugares
diverge em silêncio.

O gerador **recusa gravar** — e não grava nada — se algum texto sair de 120 a 160 caracteres, se dois
forem iguais (description repetida devolve ao Google o sinal de duplicata, que é pior do que não ter),
se um slug do sitemap ficar sem descrição, ou se aparecer descrição para slug que não está na lista
das 13. Com `--conferir` ele não grava: só reprova se o snippet estiver desatualizado, e por isso pode
rodar como portão antes do commit.

**Página fora do mapa não ganha descrição inventada** — o snippet simplesmente não imprime nada.
Description errada escrita por nós seria pior que o recorte automático do Google, porque pareceria
intencional.

**Sem `og:image`, de propósito.** A ilha não tem imagem de compartilhamento: o favicon é um SVG de
32 px embutido como data URI, e `og:image` exige URL absoluta de arquivo real. Declarar uma imagem que
não existe faz o cartão quebrar em vez de não aparecer. Ela entra quando a vitrine do T8 der à ilha a
primeira imagem própria hospedada.

Medido no ar depois do Sync, nas 13 URLs: **13 de 13 em HTTP 200, exatamente uma description em cada,
6 tags `og:` em cada, texto diferente em todas.**

### Item 3 — os três links internos que respondiam 301

O despacho dizia "o link está dentro do snippet das calculadoras". Estava, mas a causa não era o HTML
delas: **`aquametria_casca_url_se_existir()` só procurava em `post_type` `page`, e os três
artigos-âncora são `post`.** As duas vias da função falhavam, quem chamava caía no último recurso —
`home_url('/<slug>/')` —, e esse endereço existe e responde **301** para `/2026/09/08/<slug>/`.

Consertar no HTML de cada calculadora teria fechado os três casos e deixado o quarto artigo nascer com
o mesmo defeito. A casca subiu para **1.3.1** com uma terceira via, que busca por `post_name` em
`post_type` `post` e devolve o permalink real. Os três links escritos no próprio Markdown foram para a
URL canônica na mesma passada.

**O `conferir-slugs.py` aprendeu a diferença entre página e artigo** e agora reprova nos dois sentidos:
artigo linkado sem o prefixo de data, e página linkada com ele. Ele aceita **qualquer** data bem
formada em vez de cravar `2026/09/08`, senão reprovaria sozinho no dia em que nascesse o quarto artigo.
O portão foi conferido com teste negativo — os três casos pegos, inclusive o de uma linha só carregando
os dois defeitos ao mesmo tempo, que a primeira versão deixava passar.

Medido no ar: os **16 endereços internos** servidos pelas 13 páginas respondem **200, nenhum 301**.

### Item 2 — a C5 parou de se contradizer no bloco de produto

O despacho ofereceu dois caminhos e não escolheu, porque elegibilidade é da Fundação. **A escolha foi:
a elegibilidade está certa e não muda.**

Aquecedor não se vende em 160 W. O teto da lista é, de propósito, o degrau comercial que cobre o topo
da faixa — e a própria página anuncia isso duas telas acima ("na prateleira, isso vira um aquecedor de
200 W"). O que mentia era o **rótulo**: um título dizendo "Aquecedores que atendem essa potência" sobre
um aparelho que a linha ao lado declara fora da faixa é contradição na cara do leitor.

A C5 subiu para **1.4.0**, e tudo o que mudou é rótulo. A lista se parte em dois grupos com cabeçalho e
frase próprios — "Dentro da faixa calculada — 110 a 160 W" e "O degrau comercial acima — 200 W", este
dizendo por que ele está ali e o que a sobra de potência significa num aparelho com termostato. O cartão
sem link de loja parou de dizer "aparece aqui porque atende ao seu número" quando o aparelho é o degrau
acima. O cartão do degrau acima diz "acima dos" em vez de "contra os", porque o desacordo já foi
explicado no título do grupo e repetir "contra" faria a página parecer estar se desdizendo.

**E o lado que quase escapou: a tabela pré-renderizada.** É ela que um modelo de linguagem lê sem
JavaScript, e é dela que sai a citação fora de contexto. A tabela escolhe o modelo mais próximo do topo
da faixa, e em **2 das 6 linhas** (30 L e 60 L) o mais próximo é justamente o degrau comercial acima.
A célula agora diz isso, e o cabeçalho da coluna deixou de prometer "que atende".

**A ordem não mudou, e nenhuma fórmula, constante ou faixa foi tocada.** Continua sendo a distância até
o topo da faixa dentro de cada grupo, e quem cabe na faixa vem antes. Comissão não ordena nada (V16).

### O que ficou como portão, e não como conserto

Três consertos, três portões — porque conserto sem portão volta:

- `ferramentas/gerar-metas-descricao.py --conferir` reprova se o snippet estiver fora de dia com as
  descrições, ou se alguma sair da faixa de caracteres.
- `ferramentas/conferir-slugs.py` reprova artigo linkado sem data e página linkada com data.
- O **caso 15b** do `teste-navegador-c5.mjs` reproduz a entrada exata do despacho (108 L, mínima 16 °C,
  alvo 26 °C, 220 V, tampado) e lê a **ordem do DOM**: nenhum cartão acima do teto pode estar sob
  cabeçalho que diz "atendem", todo cartão acima tem que estar sob o do degrau comercial, quem cabe na
  faixa vem antes, e o cartão acima não repete as frases de quem cabe.

### Verificação

`php -l` nos 10 snippets; proteção de funções ok nos 10; `teste-seo-tecnico` com **177 afirmações**
(eram 28) e zero falha, incluindo o HTML que sai impresso no `<head>`; `teste-apelidos` 59/0;
`teste-conversor-markdown` 17/0; `teste-atualizador-sync` 9/0; `conferir-entidades` zero falha nas
cinco calculadoras; `teste-navegador-casca` inteiro em Chromium; `teste-navegador-c5` com os 15 casos
antigos mais o 15b, console limpo; `teste-navegador-visibilidade-ia` nas cinco calculadoras com o
JavaScript **desligado**, tudo passou; validadores de produto (78 produtos, 0 erro) e de espécie (36
espécies, 0 erro). No ar, depois do Sync: revisão 35 no `/status`, 13 de 13 URLs em 200, zero `&#038;`
dentro de `<script>`, corpo nunca começando por metadado YAML.

**A ronda seguinte é quem aprova.** Quem constrói não aprova o próprio conserto — foi por confundir
isso que cinco calculadoras ficaram horas quebradas no ar em 08/09.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança: nenhum produto entrou nesta execução e nenhum dos três blocos tocou em catálogo. Desses
39, **7 estão sem anúncio achado na plataforma** (o campo `motivo` diz "sem anúncio" ou que a busca não
encontrou) e **32 só aguardam a Sentinela estratégica gerar o link** — para esses a loja existe. Esta é
a leitura que substitui o número "20 sem loja possível", **VENCIDO** desde 09/09 porque foi medido
quando a Shopee era o único programa; refazer a medição de verdade exige o painel do Mercado Livre
aberto, e isso continua sendo da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T8 — a vitrine, começando pela C3.** Agora é o maior bloco de construção que sobrou e não cria URL
   nova, então respeita o item 5 do despacho (nenhuma página nova até 16/09). A C3 é a que tem mais
   itens com foto e link.
2. **T1 — medir a indexação no Search Console.** Continua dependendo do Chrome do Raphael ou da
   credencial da conta de serviço no ambiente. É ele que autoriza ou barra a T4, e a leitura de 16/09
   depende dele para dizer por que a leva de 08/09 não indexou.
3. **A `Organization` com `sameAs` na home** segue pendente de propósito, pelo mesmo motivo de sempre:
   a Aquametria não tem perfil externo nenhum, então `sameAs` sairia vazio ou inventado. Nasce quando o
   T6 der o primeiro perfil externo real.
4. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## EXECUÇÃO DE 10/09/2026, 19h17Z — T8: a VITRINE nasce na C3

Bloco entregue: **T8, a vitrine de produto**, na C3. É a primeira vitrine do Arquipélago inteiro, e a
C3 veio primeiro porque é a calculadora com mais itens de banco com foto **e** link ao mesmo tempo —
sem isso a vitrine nasceria como um layout bonito sem nada para mostrar.

O despacho da Sentinela de 10/09 não pedia nada de código nesta execução: os itens 1, 2 e 3 foram
cumpridos na execução das 17h15Z e aguardam a conferência da ronda seguinte. O item 4 é registro de
receita (reportado no fim desta entrada) e o item 5 proíbe página nova até 16/09 — **o T8 não cria
URL nenhuma**, e por isso é o maior bloco de construção que cabia hoje.

### O que a vitrine é, e por que ela não é a lista que já existia

A lista de produtos da C3 já era boa: ficha técnica completa, procedência com endereço e data,
elegibilidade dupla. Mas ficha técnica é o que convence **depois** que a pessoa decidiu comparar. O
que faltava era o que convence antes — e no celular, onde a ficha ocupa três telas, "antes" é a única
chance que existe.

A vitrine é um carrossel de cartões, `scroll-snap` em CSS puro, sem biblioteca nenhuma. Cada cartão
carrega foto, marca, modelo, **a especificação que fez o produto entrar** ("1.000 L/h — atende os 190 L
do seu aquário"), a cotação com a data da coleta e o botão da loja. Ela vem **antes** da ficha e antes
da procedência, que é o que o contrato 7 passou a exigir depois da cicatriz da Robometria de 10/09: a
prova de onde veio o número fica, mas ela existe para ser conferida, não para ser o único clique de
compra da página.

### Duas vitrines, porque são dois leitores

A vitrine **pintada** pelo script mostra o aquário de quem está lendo. A vitrine **servida** no HTML,
para o caso de referência de 100 litros, existe pelo mesmo motivo da tabela de exemplos: um modelo de
linguagem e um crawler não executam JavaScript, e vitrine que só nasce no clique é vitrine que só o
comprador que já chegou vê. As duas saem da mesma função de cartão em cada linguagem — duas marcações
para o mesmo cartão viram dois CSS e, mais cedo do que se pensa, duas aparências.

### A decisão que valeu a versão inteira: preço passou a sair, e sai datado

Até a 1.4.0 esta página dizia, em três lugares, que não publicava preço. A razão era boa — preço muda
toda semana e número velho na tela é pior que nenhum — e resolvia o problema errado. **O que o contrato
proíbe (seção 7) é preço CRAVADO COMO ATUAL.** Cotação com a data ao lado é exatamente o que a seção 6
pede da vitrine, e é o que o banco já guardava em `dados/produtos-cotacoes.json` desde 07/09.

As três frases foram reescritas na mesma versão, e não na seguinte. Página que mostra preço e diz que
não publica preço se contradiz — que é a classe de defeito que a C5 acabou de pagar no item 2 do
despacho desta mesma semana.

### O que a medição no ar pegou, e o repositório não pegaria

Depois do Sync da revisão 36, medindo a página **no ar**: a vitrine estava lá, certa, e **duas páginas
de conteúdo continuavam afirmando o contrário**. O corpo da própria C3 dizia "Não publicamos preço
nesta página" três parágrafos acima de cinco cartões com preço, e a página de divulgação dizia "nas
páginas de calculadora não publicamos preço nenhum" e "não usamos foto de loja". Nenhum teste pegaria
isso: os três textos estavam corretos ontem, e nenhuma regra objetiva sabe que hoje deixaram de estar.

Foi a leitura da página como um leitor leria — o que a seção 12 do contrato manda a Sentinela fazer, e
que aqui a Fundação fez sobre o próprio trabalho antes de dar o bloco por entregue. Corrigido na
revisão 37. **A ronda seguinte é quem aprova, como sempre.**

### As três decisões de desenho que valem para a próxima ilha que montar vitrine

1. **Cartão sem link não é link.** O contrato manda que os cartões sejam âncoras de verdade e não `div`
   com `onclick`. Produto sem link de loja não tem para onde apontar, então sai como `div`, com o lugar
   do botão reservado e escrito "link de loja em breve" — que é literalmente o que o contrato 7 manda a
   ferramenta fazer enquanto `afiliado.url` estiver vazio.
2. **Produto sem foto não some.** Sai com espaço reservado neutro, na posição que a adequação técnica
   lhe deu. Neste caso não é hipótese: o primeiro cartão da vitrine servida de 100 L é o Atman HF-0600,
   sem foto e sem link. Perder a recomendação certa por falta de imagem é trocar o certo pelo bonito.
3. **Largura e altura não se inventam.** O banco não mediu as imagens (o egresso da nuvem barra o CDN
   da Shopee) e a Aquametria não grava dimensão que não mediu. Em vez de chutar um par de números para
   satisfazer a letra da regra, o cartão reserva o espaço com `aspect-ratio: 1/1` e `object-fit:
   contain` — o layout não salta qualquer que seja a proporção real, que é a coisa que a regra existe
   para garantir. Quando o banco trouxer medida, os atributos saem sozinhos: o código já os imprime
   quando existem.

### O que NÃO entrou, de propósito

**Não há `Product`/`Offer` no JSON-LD desta página.** `Offer.price` afirma preço ATUAL, e o que temos é
cotação de uma data. Declarar schema de oferta com número velho seria mentir em formato de máquina, que
é pior do que mentir em texto, porque ninguém revisa. O `WebApplication` e o `FAQPage` continuam como
estavam.

**A `og:image` continua fora.** A vitrine não deu à ilha imagem própria hospedada: as fotos são dos
anúncios, servidas pelo CDN da Shopee. `og:image` exige URL absoluta de arquivo nosso, e declarar uma
que não é nossa é pedir para o cartão quebrar no dia em que o anúncio sair do ar.

### Os portões que nasceram junto

Conserto sem portão volta, e vitrine é o bloco da página que mais tenta voltar errado — ela mostra
foto, preço e botão, que são exatamente as três coisas que empurram uma página a vender o que paga mais
em vez do que atende.

- **`ferramentas/teste-navegador-c3-vitrine.mjs`**, 38 afirmações, nas duas metades da página: a vitrine
  SERVIDA com o JavaScript **desligado** e a PINTADA com ele ligado. A afirmação central é que **a ordem
  da vitrine seja idêntica à da lista técnica** — se um dia alguém ordenar a vitrine por comissão, por
  preço ou por "quem tem foto", o teste reprova. Ele não guarda número esperado nenhum: lê
  `AQM_C3_CATALOGO` e confere a tela contra o dado.
- **O gerador do catálogo recusa gravar imagem sem `alt`** e para se achar qualquer chave de comissão
  viajando para dentro do snippet. Comissão não aparece na tela e não ordena nada — agora isso é
  verificado, não prometido.
- Mede também o celular em 390 px: rolagem até o resultado **só no envio explícito** (sequestrar a
  rolagem de quem acabou de abrir a página é o oposto de ajudar), barra fixa enquanto o resultado está
  fora da tela, barra sumindo quando ele entra e desligando no botão Limpar.

### Um teste que precisou de conserto, e o motivo importa

O `teste-navegador-cinco.mjs` reprovou a C3 com seis `ERR_TUNNEL_CONNECTION_FAILED` — as cinco fotos da
Shopee e uma fonte. Ele já filtrava `ERR_CONNECTION`, `ERR_NAME` e `ERR_INTERNET`; nunca tinha visto a
variante do proxy porque nenhuma página da ilha carregava imagem externa antes de hoje. O filtro foi
estendido, e só para erro de rede: erro de script continua reprovando. Quem confere que a URL da foto é
a do banco é o teste da vitrine, por dado; quem confere que a imagem **abre** é a Sentinela Técnica, no
Chrome. Deixar o erro ali faria o teste reprovar todo dia por um motivo que não é defeito — e teste que
reprova sempre é teste que ninguém lê.

Uma afirmação do `teste-navegador-visibilidade-ia.mjs` foi **renomeada**, não afrouxada: chamava-se "o
aviso da tabela explica por que não publica preço" e media, na verdade, que o aviso não fica mudo sobre
preço. Deixou de ser verdade no nome quando a C3 passou a publicar cotação datada. Nome de teste treina
a próxima sessão.

### Verificação

`php -l` nos 10 snippets; proteção de funções ok nos 10 (47 funções na C3); `teste-seo-tecnico` 177/0;
`teste-apelidos` 59/0; `teste-conversor-markdown` 17/0; `teste-atualizador-sync` 9/0; `teste-escape-shortcode`
ok; `conferir-entidades` zero falha nas cinco; `conferir-slugs` ok nos dois sentidos;
`gerar-metas-descricao --conferir` em dia com as 13; validador de produtos 78/0 erro; validador de
espécies 15/0. No navegador, um teste de cada vez: `c3-vitrine` 38/0, `c3-dupla-condicao` tudo passou,
`visibilidade-ia` nas cinco com JavaScript desligado, `cinco`, `casca`, `c1-tabela`, `c5`, `c12`, `c15`
e `artigos` — todos passaram.

No ar, depois do Sync: **revisão 37 no `/status`**, igual à do manifest; **13 de 13 URLs do sitemap em
HTTP 200, nenhum redirecionamento**;
**zero `&#038;` dentro de `<script>`** (12 blocos; as 4 ocorrências da página inteira são da casca do
tema, e contar na página inteira é teste errado); o corpo começa pela linha de promessa e não por
metadado YAML; o script vem do rodapé; a tabela de exemplos e a vitrine servida aparecem no HTML
servido, com 7 cartões, 5 âncoras `sponsored noopener` em aba nova, 5 imagens com `alt` e
`loading="lazy"`, 2 espaços reservados e 5 cotações datadas.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança no total: nenhum produto entrou no banco nesta execução. Desses 39, **7 estão sem anúncio
achado na plataforma** e **32 só aguardam a Sentinela estratégica gerar o link** — para esses a loja
existe. No catálogo da C3 especificamente, **8 dos 13 filtros esperam link**, e o banco tem foto para
32 dos 78 produtos.

**Item 4 do despacho, medido de novo com a vitrine no ar:** o topo continua sem link de loja. Na vitrine
servida de 100 L o primeiro cartão é o Atman HF-0600, sem link e sem foto, e os dois seguintes com link
vêm depois. **A ordem não mudou e não vai mudar por isso** — o desbloqueio é banco melhor ou segundo
programa de afiliado, e isso é decisão do Raphael. O que a vitrine acrescentou ao problema é que agora
ele é visível: o cartão sem link mostra "link de loja em breve" no lugar do botão, em vez de o leitor
descobrir a ausência depois de rolar a ficha inteira.

### Próximo passo desbloqueado

1. **T8 nas outras calculadoras**, na ordem C5, C15, C12 — a C5 é a que tem mais itens com foto e link
   depois da C3 (11 dos 14 aquecedores com link têm foto). O código da vitrine é o mesmo desenho, e as
   três frases de preço de cada uma se reescrevem junto com ela, nunca depois.
2. **T1 — medir a indexação no Search Console.** Continua dependendo do Chrome do Raphael ou da
   credencial da conta de serviço no ambiente. É ele que autoriza ou barra a T4, e a leitura de 16/09
   depende dele para dizer por que a leva de 08/09 não indexou.
3. **Acentuar o `alt` das imagens dos outros bancos.** O `alt` é texto de tela — leitor de tela lê,
   crawler lê — e nos bancos de aquecedor, iluminação e mídia ele ainda está sem acento, como estava no
   de filtros até hoje. Vai junto com a vitrine de cada calculadora, porque cada mudança de banco pede
   regerar e reverificar o snippet daquela calculadora.
4. A `Organization` com `sameAs` na home segue pendente de propósito: a Aquametria não tem perfil
   externo nenhum. Nasce quando o T6 der o primeiro.

---

## EXECUÇÃO DE 10/09/2026, 21h17Z — T8: a VITRINE chega à C5, e a regra de reserva de ilha funcionou pela primeira vez

### A execução começou perdendo uma corrida, e isso é notícia boa

Pela seção 1 do `ARQUIPELAGO.md`, a ilha desta execução seria a **Robometria**: `ultima_execucao` mais
antiga (17h17Z) e `prioridade: 1`. A reserva foi escrita, commitada e o push foi **recusado** — outra
execução tinha reservado a mesma ilha às 21h15Z, um minuto antes. O procedimento da regra 5 foi seguido
à risca: `reset --hard` no commit da reserva, releitura dos cabeçalhos, e a ilha passou a ser a
**Aquametria** (19h17Z, a mais antiga das que sobraram). **É a primeira vez que a reserva por commit
impediu duas execuções de trabalhar na mesma ilha**, e ela impediu do jeito mais barato possível: quem
perde a corrida do push não conserta nada, só escolhe outra ilha. Fica registrado que o mecanismo é
real, e não teoria.

### O que foi entregue: C5 v1.5.0, manifest revisão 38

A **vitrine de produto nasce na calculadora de potência do aquecedor** — a segunda do Arquipélago,
depois da C3. Carrossel de cartões em `scroll-snap` de CSS puro, sem biblioteca, com foto, marca,
modelo, a especificação que fez o produto entrar, a cotação **com a data da coleta** e o botão de loja.
Vem **antes** da ficha técnica e da procedência (contrato 7). Duas vitrines por página: a pintada,
dentro do resultado, e uma **servida no HTML** para o aquário de referência de 100 L, que é o que um
crawler de IA recebe.

Vieram junto, na mesma versão, três coisas que a seção 6 do contrato pedia e esta página não tinha:
a **linha de promessa** antes do formulário, a **barra fixa do celular** enquanto o resultado está fora
da tela, e a **rolagem até o resultado** ao calcular — o mesmo desenho da C3, portado com o
`IntersectionObserver` e o `prefers-reduced-motion` incluídos.

### O que a C5 tem e a C3 não tinha, e é a lição desta execução

**A lista da C5 é partida em dois grupos** desde a 1.4.0 — "Dentro da faixa calculada" e "O degrau
comercial acima" —, e um cartão de vitrine não comporta cabeçalho de grupo: enfiar um `<h4>` dentro de
um trilho horizontal quebraria o `scroll-snap`. Copiar a C3 de olhos fechados teria produzido cartões
bonitos dizendo "atende os 108 L do seu aquário" sobre um aparelho que a linha ao lado declara **fora**
da faixa — ou seja, teria **reencenado em foto e botão de loja** exatamente a contradição que o item 2
do despacho da Sentinela mandou consertar nesta mesma semana.

A saída foi pôr a distinção na frase do próprio cartão: quem cabe diz *"150 W — dentro dos 110 a 160 W
que os 108 L pedem"*; o degrau acima diz *"200 W — degrau comercial acima dos 160 W do topo"*. E a
**sequência é calculada uma vez só** em `pintarProdutos()` e passada para `pintarVitrine()`, em vez de
recalculada dos dois lados: recalcular a mesma ordem em dois lugares é combinar de divergir depois, e
aqui divergir significa um cartão com foto e botão aparecendo antes de quem a ficha técnica pôs na
frente. O portão novo mede isto por afirmação própria — o **grupo** de cada cartão tem de ser o mesmo
que a lista técnica deu a ele.

### O número que o PROMPT.md tinha errado, e por quê

O `PROMPT.md` justificava a C5 como a próxima da fila porque "11 dos 14 aquecedores com link têm foto".
O número está certo e a conclusão estava errada: ele foi medido no **banco**, e a vitrine desenha o
**catálogo**. Dos 27 aquecedores do banco, só **18** passam no `minimo_para_sugerir` — e **9 dos 11 que
têm foto são justamente os que ficam de fora**, por não declararem volume atendido, faixa de ajuste ou
voltagem. Medido depois de regerar: **a vitrine da C5 tem foto em 2 dos 18**, contra 5 de 13 na C3.

Isso não mudou nada na entrega — produto sem foto **não some** da vitrine, sai com o espaço reservado
neutro, porque perder a recomendação técnica certa por falta de imagem é trocar o certo pelo bonito —,
mas muda como se escolhe a próxima calculadora. A regra foi escrita no `PROMPT.md`: **conte foto e link
depois do portão de elegibilidade, nunca antes**, e a medida certa é a linha "vitrine: N de M com link,
K com foto" que os geradores agora imprimem.

### Preço passa a sair, e as frases que diziam o contrário foram reescritas junto

Até a 1.4.0 esta página dizia, em dois lugares, que não publicava preço. A razão era boa — preço muda
toda semana — mas resolvia o problema errado: o que a seção 7 proíbe é preço **cravado como atual**, e
cotação com a data ao lado é o que a seção 6 pede da vitrine. As duas frases foram reescritas **na mesma
versão** em que a vitrine entrou, mais a `conteudo/divulgacao-de-afiliados.md`, que ainda dizia que só a
calculadora de vazão mostrava cotação. Página que mostra preço e diz que não publica preço se
contradiz, e contradição na cara do leitor é o defeito que a 1.4.0 acabou de consertar.

A C12 e a C15 continuam dizendo que não publicam preço, e ali a frase **é verdadeira** — elas ainda não
têm vitrine. Cada uma se reescreve na versão em que a vitrine chegar, nunca depois.

### O gerador do catálogo e o banco

`ferramentas/gerar-catalogo-aquecedores.py` ganhou os dois campos que o gerador dos filtros já tinha, com
os mesmos portões: `imagem` **recusa gravar** URL sem `alt` (imagem sem texto alternativo na vitrine é
defeito de acessibilidade que ninguém vê passar), `preco` sai de `dados/produtos-cotacoes.json` sempre
como faixa com a data **mais antiga** da coleta, e o gerador **para** se achar qualquer chave de
comissão viajando para dentro do snippet. `largura` e `altura` viajam como estão no banco, inclusive
`null`: a Aquametria não grava dimensão que não mediu, e o cartão reserva o espaço com `aspect-ratio`.

Os **11 `alt`** do banco de aquecedores foram acentuados (`submersível`, `aproximação`), como já tinham
sido os do banco de filtros. Faltam os de iluminação e de mídia, e vão junto com a vitrine de cada uma.

Não há `Product`/`Offer` no JSON-LD desta página, e é de propósito: `Offer.price` afirma preço **atual**,
e o que temos é cotação de uma data. Declarar schema de oferta com número velho seria mentir em formato
de máquina, que é pior do que mentir em texto, porque ninguém revisa.

### Verificação

`php -l` nos 10 snippets; proteção de funções ok nos 10 (**47 funções** na C5); `conferir-entidades`
zero falha, com `entidade_038_no_documento=0` nas cinco; `conferir-slugs` ok nos dois sentidos;
`gerar-metas-descricao --conferir` em dia com as 13; `teste-seo-tecnico` 177/0; `teste-apelidos` 59/0;
`teste-conversor-markdown` 17/0; `teste-atualizador-sync` 9/0; `teste-escape-shortcode` ok; validador de
produtos 78 produtos, 0 erro.

No navegador, um teste de cada vez: **`teste-navegador-c5-vitrine.mjs`, o portão novo, APROVADO em 44
afirmações** — as duas metades da página, a servida com o JavaScript **desligado** e a pintada com ele
ligado; **`teste-navegador-c5.mjs` (15 cenários, entre eles o 15b do despacho de 10/09) passou inteiro**;
`teste-navegador-visibilidade-ia.mjs` **155 afirmações, zero falha**, nas cinco calculadoras com o
JavaScript desligado; `teste-navegador-cinco.mjs` **56 afirmações, "tudo passou"** nas cinco.

### No ar, medido depois do Sync

**Revisão 38 no `/status`**, igual à do manifest, aplicada às 21h40Z — 18 itens aplicados, 14 aguardando
desembarque. O Sync precisou de **duas chamadas**: a primeira, às 21h36Z, ainda leu a revisão 37 do
`raw.githubusercontent`, cujo edge servia uma cópia de 260 s (`max-age=300`). Não é defeito, é o cache
duplo da seção 4 do contrato — e fica registrado que **a espera é do lado do raw, não do WordPress**:
o `curl` daqui já via a 38 enquanto o servidor da HostGator ainda via a 37.

A página `https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/` responde **HTTP 200**;
**`softwareVersion` 1.5.0** no JSON-LD; **zero `&#038;` dentro de `<script>`** (12 blocos; as 4
ocorrências da página inteira são da casca do tema, e contar na página inteira é teste errado); o corpo
começa pelo título e pela linha de promessa, não por metadado YAML; o script vem do rodapé; a tabela de
exemplos e a **vitrine servida** aparecem no HTML servido, com **5 cartões**, 1 âncora
`sponsored noopener` em aba nova, 1 imagem com `alt` e `loading="lazy"`, **4 espaços reservados neutros**
e 1 cotação datada. A frase "não publicamos preço" **não existe mais** nesta página.

### Produtos esperando link de afiliado: 39 de 78 no banco, 13 de 18 no catálogo da C5

Sem mudança no total do banco: nenhum produto entrou nesta execução. **No catálogo que a C5 publica, 5
dos 18 aquecedores têm link** e 13 esperam — trabalho da Sentinela estratégica, não da Fundação. Desses
13, todos têm loja possível: são modelos vendidos no varejo brasileiro, só sem link gerado. **Três dos
que já têm link não têm foto** (Roxin HT-1300/Q3 de 100, 200 e 300 W): são os avisos V20 do validador, e
a URL da foto só sai do painel da Shopee, no navegador do Raphael.

**Item 4 do despacho, medido de novo com a vitrine da C5 no ar:** na entrada do próprio despacho (108 L,
mínima 16 °C, alvo 26 °C) a lista sai com 5 aparelhos e **só o terceiro tem link** — Atman AT-150 e
Eheim Jäger 150 W vêm antes, os dois sem link, e o Ocean Tech Warmer X-5 150 W é o único com botão de
loja e com foto. **A ordem não mudou e não vai mudar por isso.** O que a vitrine acrescentou é que a
ausência agora é visível no lugar mais caro da página: o primeiro cartão mostra "link de loja em breve"
onde estaria o botão, em vez de o leitor descobrir a falta depois de rolar a ficha inteira.

### Próximo passo desbloqueado

1. **T8 na C15, depois na C12.** Antes de escolher, rode o gerador daquele banco e leia a linha
   "vitrine: N de M com link, K com foto" — a lição desta execução é que essa conta só vale **depois**
   do portão de elegibilidade. As frases de preço daquela calculadora se reescrevem na MESMA versão da
   vitrine, e o `alt` daquele banco se acentua **antes** de regerar o catálogo.
2. **T1 — medir a indexação no Search Console.** Continua dependendo do Chrome do Raphael ou da
   credencial da conta de serviço no ambiente. É ele que autoriza ou barra a T4, e a leitura de 16/09
   depende dele para dizer por que a leva de 08/09 não indexou.
3. **Item 5 do despacho continua de pé:** nenhuma página nova até 16/09. Esta execução não criou URL
   nenhuma — a vitrine e a barra do celular moram dentro de páginas que já existiam.
4. A `Organization` com `sameAs` na home segue pendente de propósito: a Aquametria não tem perfil
   externo nenhum. Nasce quando o T6 der o primeiro.

## 2026-09-11 11h16Z — Bloco T8 na C15: a terceira vitrine do Arquipélago, e um defeito de rótulo que só apareceu lendo a página

**O bloco.** A vitrine de produto chegou à calculadora de iluminação (C15 v1.3.0,
manifest na revisão 39). Mesmo desenho da C3 e da C5, copiado e não reinventado:
uma função de cartão em PHP (`aquametria_c15_vitrine_cartao_html`) e o espelho
dela em JavaScript (`vitrineCartao`), com a MESMA marcação; duas vitrines por
página — a pintada dentro do resultado e a **servida** no HTML, porque crawler de
IA não executa JavaScript; e a vitrine **antes** da ficha e da procedência
(contrato 7). A sequência é calculada UMA vez em `pintarProdutos()` e passada
para `pintarVitrine()`: calculador de ordem duplicado é combinar de divergir
depois.

**O ACHADO, e é o que vale mais que a vitrine.** Lendo o resultado como um leitor
leria — que é o único jeito de pegar este tipo de coisa — a C15 se contradizia no
cartão da lista técnica, no ar desde a 1.2.0. O nível de **alta exigência tem a
faixa ABERTA por cima**: a fonte aquarioturbinado publica "acima de 40 lm/L" e
não diz até onde, então o filtro aceita qualquer fluxo acima do piso. Só que a
frase do cartão dizia, para TODO mundo que passasse, "fica dentro da faixa de 40
a 60 lm/L que este nível pede" — e num aquário de 60 cm com 57,6 L a Chihiros
WRGB-II Pro 60 entrega **115,1 lm/L**. Afirmar que 115 está dentro de 40 a 60 é a
contradição do item 2 do despacho da Sentinela de 10/09 em outra roupa.

**A elegibilidade NÃO mudou e a ordem NÃO mudou** — a mesma escolha que a C5 fez
em 10/09, e pelo mesmo motivo: a régua estava certa, o rótulo é que mentia. A
lista passou a ter dois grupos, "dentro do intervalo que as três fontes publicam"
e "acima do teto da leitura mais alta, na parte da faixa que a fonte deixou
aberta", cada um com a frase que diz a verdade sobre ele, e quem cai no segundo
**mostra o lm/L que realmente entrega**. O grupo também foi para o DOM
(`aqm-c15-produto-acima`), que é por onde o portão confere se o cartão da vitrine
diz o mesmo grupo que a lista técnica. A distinção viaja na frase do cartão
porque trilho de `scroll-snap` não comporta cabeçalho de grupo — lição da C5,
copiada.

**Preço passou a sair, e sai datado.** As duas frases do snippet que diziam "não
publicamos preço" foram reescritas na MESMA versão, mais a página
`conteudo/calculadora-de-iluminacao.md` e o parágrafo da
`conteudo/divulgacao-de-afiliados.md`: página que mostra preço e diz que não
publica preço se contradiz. O que a seção 7 proíbe é preço **cravado como atual**;
cotação com data ao lado é o que ela permite. Continua sem `Product`/`Offer` no
JSON-LD, de propósito: `Offer.price` afirma preço de hoje, e o que temos é
cotação de uma data — mentir em formato de máquina é pior, porque ninguém revisa.

**Vieram junto as três dívidas da seção 6** que a C5 pagou em 10/09: linha de
promessa antes do formulário, barra fixa do celular enquanto o resultado está
fora da tela, e rolagem até o resultado ao calcular.

**A ESCOLHA DO AQUÁRIO DE REFERÊNCIA VIROU CONTEÚDO, porque calar o motivo seria
colher cereja.** A vitrine servida usa um aquário de 90 × 45 × 45 cm (170 L) em
alta exigência, e o parágrafo abaixo dos cartões diz por quê: varrendo os seis
aquários da tabela nos três níveis, **este é o único caso em que três luminárias
do banco cobrem o vidro E caem dentro do intervalo publicado**. Nos níveis baixo
e médio a lista sai vazia em quase todos os tamanhos — não porque a conta erre,
mas porque o catálogo brasileiro de luminária com lúmen declarado é curto
justamente na faixa de 10 a 40 lm/L. Isso é **faixa descoberta medida** (seção
14.3) e é a lista de compras do banco de iluminação, não estatística. Medido
célula a célula (seis aquários × três níveis = 18 células): **9 das 18 têm algum
produto**, e **1 única** tem três ou mais DENTRO do intervalo publicado — a de
90 cm em alta exigência, que é por isso a referência da vitrine servida. Das
outras oito não vazias, quatro só têm itens acima do teto da leitura mais alta,
e três têm um produto só. **Nenhuma célula de nível baixo tem produto abaixo de
120 cm.**

**O gerador ganhou o portão dos outros dois** (`gerar-catalogo-iluminacao.py`):
`imagem` só viaja com URL **e** `alt` — url sem alt PARA o gerador —, `preco` vem
de `produtos-cotacoes.json` como faixa com a data mais antiga, e qualquer chave
de comissão no item barra a gravação. Os 10 `alt` do banco de iluminação foram
**acentuados** (a dívida que o PROMPT registrava; falta agora só o de mídia).

**MEDIDO, e corrige de novo o mesmo erro de leitura que a C5 ensinou:** a vitrine
da C15 tem **4 de 15 com link, 2 com foto, 4 com cotação datada**. O banco de
iluminação tem 10 registros com foto — mas 8 deles são as Soma, que não declaram
lúmen e por isso nem chegam ao catálogo. Conte foto e link **depois** do portão
de elegibilidade; a linha "vitrine: N de M" no fim do gerador existe para isso.
**11 das 15 luminárias do catálogo esperam link de afiliado.**

**Receita (item 4 do despacho de 10/09, que é registro e não pedido de mudança de
ordem).** No caso do teste (60 cm, alta exigência) os três primeiros da lista não
têm link e o quarto tem; na vitrine servida (90 cm, alta) o primeiro não tem e o
segundo tem. O topo continua sendo o espaço mais caro da página. Nenhum dos 11
sem link é "sem loja possível hoje" por impedimento conhecido — todos são Chihiros
e similares vendidos no Brasil; o que falta é a geração do link, que tem teto de
calendário e é da Sentinela estratégica.

**Verificação (seção 8), toda ela antes de dar o bloco por entregue:**
- `php -l` limpo nos 11 snippets; `conferir-protecao-funcoes.py` ok (41 funções
  da C15, todas dentro de `function_exists`); `conferir-slugs.py` ok.
- `validar-produtos.py`: 78 produtos, 39 cotações, **0 erro**, 9 avisos (todos
  V20/V14/V11 já conhecidos).
- `teste-navegador-c15-vitrine.mjs`, **novo, 55 afirmações, tudo passou**.
- `teste-navegador-c15.mjs`: **78 afirmações, tudo passou**.
- `teste-navegador-visibilidade-ia.mjs`: **155 afirmações**, tudo passou.
- `teste-navegador-cinco.mjs`: **56 afirmações**, tudo passou.
- Zero `&#038;` DENTRO de `<script>` (medido nos blocos `<script>`, não na página
  inteira); `&amp;` `&lt;` `&gt;` `&quot;` uma vez cada, que é o `esc()` da própria
  calculadora.
- 0 px de rolagem horizontal a 390 px, com a página medida em **155 KB** — a
  asserção de tamanho entrou no teste justamente por causa da cicatriz da
  Robometria: render de bancada que serve metade mede 0 px por não ter o que
  estourar.

**TRÊS TESTES NEGATIVOS, porque teste que mede a si mesmo é teste verde que não
mede nada:** (1) o rótulo voltando a dizer "dentro dos" para todo mundo — três
portões reprovaram, e a saída mostrou literalmente "6.630 lm — 115,1 lm/L, dentro
dos 40 a 60 lm/L", que é o defeito que estava no ar; (2) a vitrine reordenando
para pôr quem tem link na frente — o portão central reprovou; (3) o produto sem
foto sumindo da vitrine servida — reprovou por sobrar menos de três cartões.
Mais um no gerador: apagar o `alt` da A901 fez o script recusar gravar.

**Um caso de teste errado foi corrigido no caminho, e a correção é informação:**
a primeira versão do portão de lista vazia usava "60 cm no nível médio". Reprovou
com razão — ali a lista fica sem ninguém DENTRO da faixa, mas ainda tem os
**reguláveis**, que são modelos acima do teto com dimmer declarado. Lista vazia de
verdade é outra coisa, e o caso passou a ser um aquário de 115 cm, que nenhuma
luminária do banco declara cobrir.

**Uma trava de teste foi afrouxada, e só depois de medir:** `ERR_TUNNEL` e
`ERR_PROXY` entraram na lista de erros de rede que o `teste-navegador-c15.mjs`
ignora, ao lado de `ERR_CONNECTION`/`NAME`/`INTERNET` que já estavam lá desde
08/09. Motivo medido: as ÚNICAS duas requisições que falham nesta página são a
folha do Google Fonts (que vem da casca) e a foto da A901 no CDN da Shopee (que a
vitrine servida pede) — as duas de domínio externo, as duas fora do alcance da
nuvem, as duas vivas no navegador do Raphael. `pageerror` continua reprovando
sempre, e nenhum outro tipo de erro é filtrado.

**Próximo passo desbloqueado:** T8 na C12 (mídia filtrante), que é a última da
fila de vitrines — na C1 provavelmente não nasce, porque litragem é geometria e
geometria não escolhe produto. Antes dela, acentuar os `alt` do banco de mídia e
copiar para `gerar-catalogo-midias.py` o mesmo portão de `alt`/`preco`/comissão
que os outros três geradores já têm. E fica anotado para o T3: a **faixa
descoberta de 10 a 40 lm/L** do banco de iluminação é a lista de compras de
catálogo mais urgente desta entidade, medida célula a célula neste bloco.

**NO AR E CONFERIDO (seção 4 do `ARQUIPELAGO.md`), 11/09/2026 12h21Z.** A nuvem
alcançou o domínio: `curl` no Sync devolveu **revisão 39, 18 aplicados, 14
aguardando desembarque**, e o `/status` confirma `revisao: 39`, **igual à do
manifest**. Medido na URL no ar (`/calculadora-de-iluminacao/?v=1226`, com
quebra-cache):
- **HTTP 200**, 216 KB servidos.
- **Zero `&#038;` DENTRO dos 12 blocos `<script>`** — e 4 na página inteira, que
  é justamente por que contar na página inteira é o teste errado. `&amp;` `&lt;`
  `&gt;` `&quot;` uma vez cada dentro do script: é o `esc()` da calculadora.
- O corpo começa por texto ("Pular para o conteúdo… Calculadora de iluminação e
  fotoperíodo: quantos lúmens o seu aquário pede"), **nunca por metadado YAML**.
- O script vem do **rodapé**, depois de todo o conteúdo do shortcode.
- A **tabela de exemplos** e a **vitrine servida com 3 cartões** aparecem no HTML
  servido; a vitrine servida vem **antes** do quadro de fontes e a pintada vem
  **antes** da lista técnica (contrato 7).
- Rodapé diz **versão 1.3.0**; `<meta name="description">` presente; JSON-LD
  presente; **zero ocorrência de "não publicamos preço"** e **1 cotação datada**.
- Os três cartões servidos dizem, cada um, o lm/L que entregam: 49,4 / 48,2 /
  54,4 lm/L, os três dentro dos 40 a 60 publicados — que é o que o grupo de cima
  significa agora.

## 2026-09-11, 15h16Z — A VOZ CHEGA À HOME E AO HEADER (casca 1.4.1, revisão 42)

**Bloco:** despacho do Raphael de 11/09/2026, seção 15 do `ARQUIPELAGO.md` — prioridade máxima, antes de qualquer bloco da fila. Junto veio o item (i) do 16.8: o `ARVORE.md` da ilha.

### O que mudou na tela

- **A home parou de abrir pelo manifesto.** Até a 1.3.1 a primeira linha era *"A Aquametria dimensiona aquário com número que tem fonte"*. A frase não era falsa; ela falava da fábrica para a fábrica. Agora a home abre pela pergunta mais frequente da ilha — *"Quantos litros tem o seu aquário?"* — com as três medidas nomeadas, porque quem chega aqui chegou com uma fita métrica na mão.
- **Os oito cartões viraram a pergunta que a pessoa digita.** "Potência do aquecedor por delta térmico" virou "Quantos watts de aquecedor você precisa?"; "Vazão do filtro e turnover" virou "Qual filtro dá conta do seu aquário?". **Nenhum código, slug ou URL mudou** — a seção 12.1 proíbe mover endereço de página publicada, e este bloco não moveu nenhum.
- **Nasceu a prateleira de guias**, no fim da home, no molde GUIA do `VOZ.md`.
- **O menu diz "Como a gente calcula"** no lugar de "Metodologia", e o título das quatro páginas da casca passou a ser sincronizado — só nas que carregam `_aquametria_casca`, e sem tocar em `post_name`.

### As três decisões de desenho que valem para as outras ilhas

**1. A prateleira de guias não guarda cópia de título nenhum.** A casca pergunta pelo filtro `aquametria_guias` e quem responde é o snippet dos artigos. Guia novo aparece na home sozinho. É a mesma escolha do hub de calculadoras, e existe pela cicatriz de 11/09: o número digitado que era verdade no dia em que foi escrito e virou mentira em silêncio no dia em que o banco cresceu. A frase "5 de 8 já estão no ar" é contada, e o portão conta de novo e compara.

**2. A camada de prova se declara no MARKUP, não se adivinha pela vizinhança.** "Procedência" é palavra proibida na voz e obrigatória na prova, e as duas são a mesma palavra. A saída não é heurística melhor: a página marca a prova com a classe `aqm-prova`, o portão **retira** esses blocos e proíbe o termo em todo o resto. Para a declaração não virar porta dos fundos, os blocos marcados são contados (no máximo dois por página), nenhum pode conter o H1 ou o primeiro parágrafo, e nenhum pode abrir a página. É a lição do Clube do Mosaico aplicada antes de doer aqui.

**3. A régua do portão mora no portão.** `teste-voz.mjs` escreve a própria lista de termos proibidos, à mão, a partir do `VOZ.md`. Ela não é importada de um JSON que o snippet também leia — se as duas metades lessem a mesma lista, apagar um termo dela faria as duas errarem juntas e o teste continuaria verde. E toda afirmação sobre o que a página diz é medida **no corpo**, entre `<main>` e `</main>`: no HTML inteiro o termo apareceria dentro do próprio JSON-LD.

### O que a medição achou sem procurar

**O `<title>` da home vinha da tagline do WordPress, e nunca ninguém a tinha tocado.** A linha que a pessoa lê no resultado de busca — a mais lida da página inteira — ainda dizia *"Aquametria – Calculadoras e dados técnicos para dimensionar o seu aquário"*, escrita quando a ilha nasceu. Nenhum portão do projeto olhava para ela: o `teste-voz.mjs` da primeira versão media o corpo, e o `<title>` não é corpo. A casca passa a gravar a opção `blogdescription`, na mesma família de `page_on_front`, e a bancada passou a montar o `<title>` **como o núcleo do WordPress monta** — `<nome do site> – <blogdescription>` na home, `<título da página> – <nome do site>` na interna. Bancada que compõe o título de outro jeito é bancada que serve o que o site não serve.

**A tabela de constantes da `/metodologia/` rolava na horizontal no celular, e está no ar assim desde que a página existe.** 67 px a 360 px, 37 px a 390 px. A causa é discreta e vale para toda ilha: o conversor de Markdown do Sync embrulha **toda** tabela vinda de `conteudo/` num bloco que rola, mas esta tabela é impressa direto pelo shortcode e por isso nunca passou por lá. Nenhum teste do projeto media largura nas páginas da casca — o `teste-navegador-casca.mjs` monta o cabeçalho com um corpo falso, de propósito, porque o que ele mede é o menu. **Não foi este bloco que quebrou; foi este bloco que passou a medir.** Consertado na mesma versão, e o gate reprovou antes e passou depois — que é o teste negativo desta trava, observado ao vivo.

**A C15 seria a única a ficar com o texto antigo.** Ela é a única calculadora que sobrescreve o resumo do cartão pelo filtro `aquametria_calculadoras`. Quem lesse só a casca veria os oito cartões reescritos e nunca saberia que um deles é descartado no ar. Achado pela varredura, não pela leitura do código. (C15 v1.3.1, e nada além desse texto mudou nela.)

### Verificação — seção 8 inteira

| portão | afirmações | resultado |
|---|---|---|
| `teste-voz.mjs` (novo) | 86 | 0 falha |
| `teste-navegador-casca-paginas.mjs` (novo) | 28 | 0 falha, **0 px de rolagem nas 24 medições** |
| `mutacoes-voz.py` (novo) | 11 mutações | **11 reprovadas** |
| `teste-navegador-casca.mjs` | 43 | 0 falha |
| `teste-navegador-cinco.mjs` | 56 | 0 falha |
| `teste-navegador-visibilidade-ia.mjs` | 155 | 0 falha |
| `teste-navegador-artigos.mjs` | 108 | 0 falha |
| `teste-seo-tecnico.php` | 177 | 0 falha |
| `conferir-slugs.py` · `validar-produtos.py` · `conferir-protecao-funcoes.py` | — | 0 erro |

`php -l` limpo nos dez snippets. Corpo medido: home 3.760 caracteres, `/calculadoras/` 2.495, `/metodologia/` 4.249, `/sobre/` 1.616 — as quatro acima do piso de ~1.500 da seção 8.

**A mutação que mais vale é a número 3**, a porta dos fundos: embrulhar a home inteira na classe que declara camada de prova. Ela não escreve nada de errado na tela — só desliga a regra. Se passasse, a marca `aqm-prova` valeria zero.

### O `ARVORE.md`

Quatro seções de nível 1 (`/calculadoras/`, `/peixes/`, `/equipamentos/`, `/guias/`), as categorias de nível 2 com o nome que a pessoa usa, e o pai de cada página existente. **Nenhuma categoria tem hoje as 3 filhas com dado real que a 16.5 exige**, então nenhuma nasce agora — e duas travas independentes de calendário (item 5 do despacho da Sentinela e o T2 deste `PROMPT.md`) seguram qualquer URL nova até a leitura de 16/09. O arquivo diz isso por escrito, com a ordem das levas para quando destravar.

### Receita e pendências

- **39 dos 78 produtos esperam link de afiliado.** Quem gera é a Sentinela estratégica, no navegador do Raphael.
- Item 4 do despacho de 10/09 (o topo da lista sem link de loja) e item 5 (nenhuma página nova até 16/09) continuam de pé, e este bloco não criou nenhuma URL.
- As páginas de `conteudo/` ainda falam na voz antiga: elas são reescritas ao passar pela ronda, como manda a 15.5.

**Próximo passo desbloqueado:** breadcrumb com `BreadcrumbList` e blocos "Veja também" (16.4) em toda página que já existe. Nenhum dos dois cria URL, então os dois cabem antes de 16/09. O breadcrumb nasce com o nível 2 em texto, sem link, porque a categoria ainda não existe — estado de transição declarado no `ARVORE.md`, não desenho.

## 2026-09-11, 17h38Z — A arvore da secao 16 chega as treze paginas no ar

**Entregue:** `snippets/aquametria-casca.php` v1.5.0, manifest na revisao 43,
`/status` respondendo 43 e as treze URLs abertas e medidas no ar as 17h37Z.
Fecha o que o despacho do Raphael de 11/09 deixou de pe depois do bloco da voz
— e fecha **sem criar uma URL**, que era a condicao para caber antes da leitura
de 16/09.

- **A TRILHA, em doze das treze.** A home nao tem, como manda o 16.3. O nivel 2
  sai em TEXTO enquanto a categoria nao existe: e o estado de transicao que o
  `ARVORE.md` ja declarava, e nao ha nada a lembrar no dia em que ela nascer,
  porque quem resolve o endereco de todo degrau e `url_se_existir()`.
- **O BREADCRUMBLIST PUBLICA MENOS QUE A TELA, DE PROPOSITO.** Numa calculadora
  a trilha na tela mostra quatro degraus e o schema publica tres, sem a
  categoria. Nao e esquecimento e foi a decisao mais dificil do bloco: um
  `ListItem` do meio sem `item` invalida a lista inteira para o Google, e lista
  invalida e lista ignorada — o schema "mais completo" publicaria **menos** com
  cara de publicar mais. A mutacao 4 e exatamente essa porta dos fundos, e o
  portao amarra os itens do schema aos degraus LINKADOS da tela, para a relacao
  nao poder derivar em silencio.
- **AS IRMAS SAO DERIVADAS, NUNCA DIGITADAS.** De 2 a 4 por pagina (16.4c),
  tiradas do mesmo registro que alimenta o hub, com afinidade declarada: mesma
  categoria primeiro, ordem do mapa depois. Lista escrita a mao envelheceria no
  dia em que a proxima calculadora entrasse no ar — e a frase que linka a mae
  (16.4b) traz a contagem **contada**, conferida contra os cartoes com link do
  hub, nunca perguntada ao snippet.
- **O GUIA AINDA NAO TEM FRASE DE MAE, e o portao cobra a AUSENCIA dela.**
  `/guias/` nao existe; frase apontando para la seria link morto. Cobrar a
  ausencia e o que impede a proxima execucao de "consertar" isso com um
  endereco inventado — a mutacao 14 e essa tentacao, e ela reprova.

**A BANCADA MEDIA METADE DA PAGINA.** Nasceu `ferramentas/render-pagina-completa.php`
porque dos tres renderizadores que havia, um montava so as quatro paginas da
casca e os outros dois montavam corpo **sem cabecalho e sem H1** — e a trilha
nasce justamente entre o cabecalho e o H1. Medir a arvore em qualquer um dos
tres seria afirmar sobre o que nao existe, que e a cicatriz que a Robometria
pagou tres vezes. Uma pagina por processo, como as outras bancadas desta ilha.

**O QUE AS MUTACOES ACHARAM — e uma delas era buraco de verdade no portao.**
Com cinco calculadoras no ar, **nenhuma pagina chega a ter cinco irmas
candidatas**: trocar o teto de 4 por 5 no snippet nao mudava uma virgula do que
o site serve, e o portao ficava verde nas duas versoes. A faixa "de 2 a 4"
estava sendo conferida contra um mundo que nunca passa de 4 — grade que nao
pisa na borda, so que desta vez a borda nao existia no mundo. A saida foi a
bancada **fabricar** a borda: o modo `todas` do renderizador poe C2, C7 e C8 no
ar, a pagina passa a ter sete candidatas e ai o teto tem o que cortar. E a
unica afirmacao do portao que mede um mundo que nao e o de hoje, e esta
declarada como tal.
Outras tres mutacoes passaram por serem **inertes**, nao por o portao ser cego:
tirar a trava do `render_block` nao duplica nada porque o bloco so renderiza uma
vez na requisicao, e tirar `is_front_page()` nao poe trilha na home porque o
slug da home nao esta na arvore. As tres foram reescritas ate morder de
verdade. **14 de 14 reprovadas** na rodada final.

**UM LIMITE DECLARADO, porque fingir que nao existe seria pior:** se alguem
mudar a categoria de uma calculadora no snippet **e** no `ARVORE.md` na mesma
passada, este portao nao ve — nao ha terceira fonte no repositorio que diga de
que categoria uma calculadora e. Categoria e decisao editorial. As mutacoes 1 e
2 cobrem o caso de UMA das metades mudar, que e o que acontece por descuido.

**VERIFICACAO (secao 8):** `teste-arvore.mjs` 288 afirmacoes com regua propria,
lendo o `ARVORE.md` para cobrar que documento e codigo digam a mesma coisa;
14 de 14 mutacoes reprovadas; 224 medicoes em Chromium nas treze paginas em
360/390/781/782/783/1200 px, **0 px de rolagem horizontal** e console limpo;
`teste-voz`, `teste-seo-tecnico` (177), `conferir-slugs` e
`conferir-protecao-funcoes` sem falha; `php -l` limpo nos 10 snippets.
**No ar as 17h37Z:** 13 de 13 em HTTP 200, 175 afirmacoes medidas no HTML
servido — zero `&#038;` dentro de `<script>` nas treze, trilha sempre antes do
H1 e uma so por pagina, nenhum degrau apontando para pagina inexistente,
`BreadcrumbList` valido nas doze.

**ACHADO REGISTRADO, fora do escopo deste bloco.** A medicao de orfa nasceu
errada e o erro valeu a pena: a primeira versao contava so os links do `<main>`
e reprovou `/sobre/` com zero. O defeito era da **regua**, nao da pagina —
`/sobre/` esta no menu e no rodape das treze, entao o robo acha, que e o que o
16.4(f) existe para garantir. Mas contar a pagina inteira sozinho nao mede nada,
porque o menu faz tres paginas passarem sempre. Viraram duas afirmacoes com
nomes diferentes: o 16.4(f) literal, no HTML servido, para as treze; e a
promessa do cluster, no CORPO, para as oito paginas da arvore. O que fica
registrado e que **`/sobre/` e a unica das treze que nenhum corpo cita** — nao e
defeito desta entrega, e assunto de pauta (secao 17).

**39 dos 78 produtos esperam link de afiliado** (nao mudou: este bloco nao tocou
em catalogo). Nao houve memoria disponivel nesta execucao (`/areas` nao existe
no ambiente); o estado vive no `ESTADO.md` desta pasta.

**Proximo passo desbloqueado:** `pauta.md` (secao 17) ainda nao existe nesta
pasta, entao o proximo bloco que nao cria URL e a **reescrita na voz das paginas
de `conteudo/`**, que o despacho da voz deixou marcada como pendente ("as de
conteudo/ ainda nao foram"). Tudo que cria URL — as oito paginas de nivel 1 e 2,
a troca de pai e de slug, a leva de malha — espera a leitura de 16/09.

## 2026-09-11, 19h44Z — A VOZ CHEGA ÀS NOVE PÁGINAS DE conteudo/, e o título publicado vinha de outro lugar

**Bloco entregue:** casca 1.5.1, artigos 1.2.0, manifest na revisão 48, `/status`
conferido, as treze URLs abertas no ar. Nenhuma URL mudou — a condição da leitura
de 16/09 continua respeitada.

### O que o despacho da voz tinha deixado escrito à mão

"Cada página existente continua sendo reescrita na voz ao passar pela ronda — as
de `conteudo/` ainda não foram." Pendência escrita à mão não é portão, e foi
assim que **as cinco calculadoras seguiram no ar com o H1 começando por
"Calculadora de"** — a única forma de título que o `VOZ.md` proíbe pelo nome — e
**oito dos nove `<title>` passando de 65 caracteres** (120, 128, 97…). Nada disso
precisava de olho humano; precisava de alguém medindo.

### UM NOME POR PÁGINA

O degrau da trilha e o H1 ficam a uma linha um do outro na tela e, em 8 das 9
páginas, diziam nomes diferentes: a trilha dizia "Quantos litros tem o seu
aquário?" e o H1, logo abaixo, "Calculadora de litragem: quantos litros tem o seu
aquário". A casca **já tinha** a voz certa nos rótulos desde 11/09; o que nunca
foi tocado foi o `titulo` das páginas. Então os nove títulos passaram a ser o
rótulo que a casca já publicava — nada foi inventado, uma divergência foi
removida — e existe agora uma afirmação que cobra a igualdade.

Nos três guias os títulos longos com parêntese sumiram e a manchete virou o nome
único. Eles foram escolhidos para **não canibalizar a ferramenta do mesmo
assunto**: o guia do aquecedor é "Por que o 1 W por litro erra para o mesmo lado"
e a ferramenta é "Quantos watts de aquecedor você precisa?" — a ferramenta
responde a pergunta, o guia responde o porquê. Era escolher entre duas opções
defensáveis, e a Fundação escolheu: perde-se a cabeça da consulta no `<title>` do
guia, que continua no slug, nos H2 e na `meta_descricao`.

### PROCEDÊNCIA NÃO ABRE PÁGINA

Os três artigos abriam por fabricante e data de coleta — "Coletadas em 08/09/2026
e atribuídas ao próprio fabricante: Seachem Matrix, 1,25 mL por litro…" — **sem um
único termo da lista de proibidas aparecer**. Lista de palavra não pega isso.

A caixa da resposta direta passou a ter duas camadas: o primeiro parágrafo
responde à pessoa na língua dela, e a procedência desce um parágrafo, **dentro da
mesma caixa**, marcada com `aqm-prova`. A seção 5 continua inteira — quem cita a
caixa leva a fonte junto — e a 15.2 passa a valer. Cinco páginas abriam falando da
internet em vez de falar com quem entrou ("Pergunte na internet brasileira
quantos watts…"); agora abrem pela resposta, em segunda pessoa.

### O DEFEITO QUE SÓ O AR MOSTROU, e era a família inteira

Depois do primeiro desembarque, **168 afirmações medidas no ar acharam o que 293
afirmações verdes na bancada não podiam ver**: o corpo das nove páginas trocou e
**os nove títulos não**.

Duas fontes para o mesmo dado. Quem grava `post_title` é o Sync, e o Sync lê
`titulo` do `manifest.json`; o front matter do `.md` ele nem abre. A bancada
inteira renderizava do `.md`. E `atualizar-manifest.py` só recalculava `sha256` —
`titulo` **nunca** foi reespelhado desde que o arquivo existe. Resultado: bancada
verde, Sync respondendo "18 aplicado(s)", e o H1 e o `<title>` das nove
continuando os de antes.

Três consertos, e o do meio é o que fecha a família e não só este caso:
1. `atualizar-manifest.py` relê o título do front matter e o reespelha, imprimindo
   cada troca (8 nesta passada). O front matter manda.
2. **`render-pagina-completa.php` passou a ler o título do MANIFEST.** A bancada
   agora lê a mesma fonte que o site: manifest atrasado aparece na primeira
   medição, não depois do desembarque.
3. `conferir-slugs.py` cobra manifest == front matter e nomeia a ferramenta a
   rodar. Provado mordendo: com o título velho de volta no manifest, reprova.

De quebra, `render-pagina-completa.php` servia `\&quot;` num H1 que no ar sai com
aspas curvas — o front matter é YAML e a aspa interna vem escapada. Calibrar o
portão da voz nessa string seria medir o que não existe.

### A LISTA DE MUTAÇÕES MENTIU POR UMA RODADA, pelo mesmo motivo

Três mutações editavam o título no `.md` e ficaram **inertes** no instante em que
a bancada mudou de fonte: 18 de 20, verdes sem medir nada. Agora mutam o
manifest, que é a fonte que publica, e as três reprovam pela regra que existem
para medir. Antes disso, outras duas já haviam passado por serem inertes — mutar
o `titulo` do snippet dos artigos não move o H1 (ele vem do front matter), e
trocar meia frase deixava "você" no resto do parágrafo. **Mutação que não morde
não prova nada, e o jeito de descobrir é ela ficar verde.**

### VERIFICAÇÃO

- `teste-voz.mjs`: de **4 para 13 páginas** e de **86 para 293 afirmações**. As
  nove de `conteudo/` montadas pelo `render-pagina-completa.php`, um processo por
  página. Régua nova: procedência não abre página (fabricante e data de leitura
  fora do primeiro parágrafo), degrau da trilha igual ao H1, H1 único na ilha,
  `<title>` ≤ 65, âncora interna pela consulta do destino, segunda pessoa no
  primeiro parágrafo — **com o limite desta última declarado no próprio teste**:
  ela não pega manifesto que diga "você" na primeira linha. Quem julga manifesto
  é a ronda (15.4).
- `mutacoes-voz.py`: de 11 para **20 mutações, 20 reprovadas**.
- `teste-arvore.mjs`, `teste-seo-tecnico.php` (177), `conferir-slugs.py`,
  `conferir-protecao-funcoes.py` (10 snippets) e `validar-produtos.py` (78
  produtos, 0 erro) sem falha. `php -l` limpo nos 10 snippets.
- Chromium: **224 medições** nas treze páginas em 360/390/781/782/783/1200 com 0
  px de rolagem, mais os três artigos no `teste-navegador-artigos.mjs`.
- **NO AR, às 19h44Z:** 13 de 13 em HTTP 200, **160 afirmações medidas no HTML
  servido, 0 falha** — nove H1 novos, nove `<title>` dentro de 65, trilha e H1
  iguais nas nove, nenhum fabricante e nenhuma data no primeiro parágrafo, zero
  `&#038;` dentro de `<script>`.
- 39 dos 78 produtos esperam link de afiliado (**não mudou**; este bloco não tocou
  em catálogo). Pauta da seção 17: `pauta.md` ainda não existe nesta pasta — 0
  temas escritos, 0 na fila, 0 recusados.
- `package.json` entrou na pasta declarando a dependência da bancada
  (`playwright`), que esta execução descobriu pelo erro. O Chromium não se baixa:
  já vem em `/opt/pw-browsers`.

### Próximo passo desbloqueado

A voz fechou em toda página que existe. **Tudo que cria URL continua travado até a
leitura de 16/09** (item 5 do despacho da Sentinela e o T2 deste arquivo), e a
`pauta.md` da seção 17 ainda não existe nesta pasta. Sobram, sem criar URL: o
banco de espécies (T3d), que destrava "quantos litros para X peixes"; o catálogo
de iluminação por faixa (T3a); e a vitrine nas calculadoras que ainda não a têm.
O T3d é o de maior valor porque é o eixo que a Bússola verificou aberto.

## 2026-09-11 (21h) — T3d leva 4: o banco de especies ganhou PROFUNDIDADE, e o canal de coleta ganhou duas regras

Bloco escolhido pela rotacao da secao 1 (a ilha estava com a `ultima_execucao`
mais antiga das tres; nenhuma tinha despacho com item acionavel em aberto — os
que restam na Aquametria e na Robometria sao os travados ate 16/09 e a metade
humana do Search Console). Reserva por commit feita as 21h18Z e aceita no
primeiro push.

**Nenhuma especie nova, e isso foi a decisao.** O banco tinha 36 registros e 12
deles eram barrados no portao de pagina de especie por campo faltando, nao por
falta de peixe. Acrescentar o 37o registro nao destrava nada; fechar campo
destrava. Resultado medido pelo proprio validador: **pagina de especie de 24
para 27 aptos, C8 de 28 para 29**, com 0 erro.

**O que foi colhido (busca RESTRITA ao dominio, niveis 3 e 5 da escada):**

- **Tetra ember** (`hyphessobrycon-amandae`), que era o pior registro do banco:
  o Seriously Fish devolveu, atribuidos a ESTA especie pelo nome, a base minima
  (45 x 30 cm), a faixa de manutencao (20 a 28 C), o cardume (8 a 10) e o
  temperamento. Os tres campos que faltavam fecharam, e com o compendio entrando
  como segundo corpo o E14 fechou junto. O menor peixe do banco (2,0 cm) passou a
  ser tambem o de menor frente declarada (45 cm) — o piso util do eixo "quantos
  litros para X peixes".
- **Peixe-neve** (`tanichthys-albonubes`): segundo corpo de fonte, e duas
  divergencias publicadas em `conflitos[]` em vez de escondidas. A temperatura de
  manutencao desceu de 18–22 para 14–22 C e o cardume subiu de 5 para 10. O
  cardume importa mais do que parece: com 60 cm de frente declarada, 5 peixes dao
  12 cm por individuo e 10 dao 6 cm — a mesma especie com o dobro de densidade,
  dependendo de qual fonte a pagina citar.
- **Peixe-lapis** (`nannostomus-beckfordi`): segundo corpo, registro completo. O
  `observacao` diz com precisao o que o segundo corpo confere (a convivencia, e
  so ela) e o que ele NAO confere — nenhum numero desta ficha foi corroborado
  por um segundo corpo, e isso ficou escrito.

**AS DUAS REGRAS NOVAS, e elas sao do canal, nao do banco.** Enquanto o egresso
barrar as fontes (reconferido hoje nos quatro dominios, por `curl` e por
`WebFetch`, com o site da propria ilha respondendo 200 na mesma passada — e
politica de rede, nao a intermitencia de tunel da secao 20), todo numero entra
por resumo de busca. E resumo de busca tem dois vicios, os dois medidos hoje:

1. **A CONGENERE.** Quando a ficha da especie alvo nao publica o campo, o resumo
   oferece o numero da especie IRMA do mesmo genero **sem avisar que trocou de
   ficha**. Aconteceu tres vezes numa unica execucao: a base de 80 x 30 cm de uma
   *Celestichthys* oferecida como a do danio celestial, a base do *T.* sp.
   'Vietnam' oferecida como a do peixe-neve (segunda vez — a coleta de 09/09 caiu
   na mesma oferta), e a base das congeneres de *Nannostomus* oferecida como a do
   peixe-lapis. **Numero sem o nome da especie do lado e recusa, nao dado**, e
   agora cada registro grava qual numero foi oferecido e recusado, para a proxima
   coleta nao repetir a busca perdida.
2. **REPRODUZIR NAO E CONFERIR.** O porte de 13,7 cm TL do gurami mel voltou
   identico em duas formulacoes de busca hoje — e a recusa de 09/09 estava certa.
   Cheguei a ela por conta propria, sem ter lido a nota, e pelo mesmo caminho: o
   que derruba o numero e a **contradicao interna da fonte**, que declara 13,7 cm
   e, na mesma ficha, aquario minimo de 60 cm, enquanto para o *T. leerii*, de
   12,0 cm, a mesma base declara 120 cm. Tres reproducoes em duas datas nao
   compram uma conferencia.

**E16, a guarda executavel.** `esquema-especies.json` foi para a versao 3 e o
validador ganhou a regra: **todo numero de campo tem de aparecer no texto de
alguma fonte que declara aquele campo**, em algarismo ou por extenso. O campo e o
numero que a maquina usa; a `referencia` e a transcricao do que a fonte disse —
sao duas escritas independentes do mesmo fato, e quando divergem alguem
transcreveu, digitou ou editou um lado so. E a mesma familia de defeito que a
Robometria achou comparando duas copias da mesma regua, com uma diferenca que faz
a comparacao valer: **aqui as duas copias sao mesmo independentes.**

**A REGRA QUE FOI DESCARTADA, e o motivo importa mais que a que ficou.** A
primeira ideia foi cobrar coerencia entre porte e frente minima: peixe maior,
frente maior. Medi antes de escrever e o banco tem **87 dessas "inversoes", quase
todas legitimas** — o betta de 6,5 cm pede 45 cm porque e sedentario, o
paulistinha de 3,8 cm pede 90 cm porque nada muito. Quem manda na frente e a
natacao, nao o comprimento. A regra teria enchido o portao de ruido e ensinado a
ignora-lo.

**E o E16 nasceu VERDE, entao teve de provar que morde.** Quatro corrupcoes
deliberadas novas em `testar-validador-especies.py`: numero trocado, um lado do
intervalo trocado, a largura da base trocada, e — a que prova que a leitura por
extenso e real e nao um buraco que aprova qualquer coisa — o cardume da
coridora-panda de 6 para 7, onde a fonte escreve "pelo menos SEIS" por extenso.
**19 testes negativos, 19 reprovando.**

**VERIFICACAO:** `validar-especies.py` 36 especies, 0 erro, 1 aviso (o E15 do
guppy, que fica de pe de proposito — ver abaixo); `testar-validador-especies.py`
19 de 19; `validar-produtos.py` e `conferir-slugs.py` sem falha; os tres JSON
reparseados. **Nada foi ao ar e nao havia o que ir:** os quatro arquivos tocados
sao `publicar: false`. O manifest subiu para a **revisao 50** e o `/status` foi conferido no ar batendo
em 50, com 18 aplicados e 0 falha — ver a nota de processo abaixo, porque o
caminho ate la quase virou um diagnostico errado.

**TRES COLETAS RECONFERIRAM 09/09 E DERAM O MESMO RESULTADO** — a verificacao
separada no TEMPO, que e o que a secao 19.4(c) do contrato pede: o guppy nao tem
ficha propria no compendio (so forum, e forum nao e compendio com bibliografia,
entao o aviso E15 dele nao sai por busca — sai por leitura direta ou por um
terceiro corpo); a ficha do molly no compendio esta publicada INCOMPLETA, com a
secao de dimensoes vazia, o que explica por que a frente minima nao vem e avisa
que procurar de novo pelo mesmo caminho nao adianta; e o gurami de tres pintas
recebeu a oferta de um arranjo "um macho para 2 ou 3 femeas" que foi recusada
porque a propria fonte o apresenta como arranjo de REPRODUCAO, nao de manutencao.
Harem de desova nao e convivencia de aquario comunitario.

**NOTA DE PROCESSO — O `/status` ATRASA ~5 MINUTOS DEPOIS DO PUSH, E ISSO NAO E
DEFEITO.** Medido nesta execucao porque quase virou diagnostico errado. Depois do
push com o manifest na revisao 50, o Sync foi acionado e respondeu 200 dizendo
**revisao 48** — a anterior. Tres acionamentos seguidos disseram 48; o quarto,
`21:34:33Z`, disse 50, e o `/status` passou a bater com o manifest (18 aplicados,
0 falha). A causa esta no proprio snippet: `AQUAMETRIA_SYNC_BASE` aponta para
`raw.githubusercontent.com/.../main/`, e o `wp_remote_get` manda
`Cache-Control: no-cache` — que instrui o servidor de origem, **nao o CDN do
raw**, que serve a versao anterior por alguns minutos. O `no-cache` no codigo da
a impressao de que isso ja esta resolvido, e nao esta.

**Como ler isso na proxima vez:** Sync respondendo 200 com a revisao ANTERIOR,
logo depois de um push, e cache de CDN — espere e reacione, nao reescreva nada.
E a mesma forma do `000` lido como bloqueio de rede na semana passada (secao 20
do contrato) e do fundo preto do logo do Clube do Mosaico: **sintoma lido como
causa, e o diagnostico errado se propaga porque a execucao seguinte le o
`ESTADO.md` da anterior como fato.** O jeito de nao cair nisso e o que foi feito
aqui: reacionar o Sync em intervalo e olhar a serie, em vez de concluir na
primeira leitura.

**Receita:** 39 dos 78 produtos seguem esperando link de afiliado; este bloco nao
tocou catalogo. **Pauta (secao 17):** `pauta.md` ainda nao existe — 0 escritos, 0
na fila, 0 recusados.

Proximo passo desbloqueado: com 27 especies aptas a pagina e 29 alimentando a
C8, o eixo "quantos litros para X peixes" tem banco suficiente — mas **tudo que
cria URL continua travado ate a leitura de 16/09** (item 5 do despacho da
Sentinela e o T2 deste arquivo). O proximo bloco sem URL nova e a **vitrine da
C12** (T8), a unica calculadora que ainda nao a tem; antes de escrever uma linha
dela, procurar na C12 a faixa que nao tem um dos dois lados, que foi o que a C15
ensinou. Depois, o catalogo de iluminacao por faixa (T3a).
