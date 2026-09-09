# arquipelago
Projeto Arquipelago - codigo e conteudo das ilhas (Aquametria etc.), puxados pelo snippet Sync de cada site

## Estrutura do repositorio (desde 09/09/2026)

O Arquipelago passou a ter **uma unica Fundacao com despachante**, no lugar de
uma rotina por ilha. A estrutura que sustenta isso:

- **`ARQUIPELAGO.md`** na raiz e o **contrato comum**: as regras que valem para
  toda ilha (despachante, publicacao, visibilidade em IA, interface,
  monetizacao, verificacao, malha). Regra nova do Arquipelago se escreve la,
  uma vez so — nunca copiada para dentro do prompt de uma ilha.
- **Cada ilha tem o seu `ilhas/<ilha>/PROMPT.md`**, com apenas o que e daquela
  ilha: identidade, endpoints, memoria a carregar e fila de blocos.
- **O cabecalho YAML do `ilhas/<ilha>/ESTADO.md`** e o que o despachante le para
  escolher a ilha de cada execucao (`estado`, `prioridade`, `ultima_execucao`,
  `executando_desde`, `bloco_atual`, `bloqueada_por`). O formato esta na secao 2
  do `ARQUIPELAGO.md`. A reserva da ilha e feita por commit, entao varias
  execucoes podem rodar ao mesmo tempo sem se atropelar.
- **Ilha nova se cria copiando `ilhas/_modelo/`** e preenchendo o que estiver
  entre `< >`. Nenhuma rotina muda quando uma ilha nasce.

Ilhas atuais: `ilhas/aquametria/` (aquarismo, no ar) e `ilhas/robometria/`
(robo aspirador, nascendo).
