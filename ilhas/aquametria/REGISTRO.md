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
