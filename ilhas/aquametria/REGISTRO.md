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
