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
