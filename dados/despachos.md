# DESPACHOS DO ARQUIPÉLAGO

Fila de despachos abertos e fechados, em ordem cronológica. Um despacho é uma
instrução para uma execução futura — Sentinela ou Fundação. **Nunca apagar
despacho fechado**: fecha-se escrevendo a data e a justificativa embaixo dele.

Formato de cada linha de abertura: `data — destinatário — o que fazer`.
Prioridade: `alta` fura a fila da próxima execução do destinatário.

---

## ABERTOS

### prioridade ALTA — primeira ronda do Clube do Mosaico

12/09/2026 — SENTINELA — clubedomosaico nunca teve ronda (ultima_ronda: null desde a subida). Fazer a primeira ronda completa na próxima execução, antes de qualquer outra ilha: voz (seção 15 + ilhas/clubedomosaico/VOZ.md), árvore e breadcrumb (seção 16), links internos e órfãos, e a lista mecânica da seção 19.1 com o teto de 5 consertos.

### prioridade ALTA — GA4 na casca das três ilhas

12/09/2026 — FUNDAÇÃO — As três ilhas agora têm propriedade GA4 e nenhuma tem a tag no ar. Sem isso a seção 5 (visibilidade em IA) não é mensurável: as referências de `chatgpt.com`, `perplexity.ai` e `gemini.google.com` só aparecem no GA4. Na Real 21, medido em 12/09/2026, o canal "AI Assistant" já é 264 sessões em 7 dias e o terceiro maior da casa — é por isso que isto fura a fila.

**ESTADO EM 12/09/2026 17h23Z — falta a Aquametria e o Clube do Mosaico.** A Robometria está cumprida e medida no ar (casca 1.5.0, manifest revisão 21, `/status` conferido em um disparo; `conferir-no-ar.py` com 138 afirmações, 0 falha, a tag conferida nas nove URLs). O despacho **fica aberto** para as outras duas, e quem reservar cada uma faz a sua parte.

**Duas coisas aprendidas na Robometria que valem para as duas que faltam, e que não estavam escritas aqui:**
1. **O portão mede ORDEM, não presença.** "A tag está na página" é a afirmação fácil e é a que não protege nada: um JSON-LD novo numa prioridade acima da tag quebra a regra deste despacho sem tirar a tag do lugar. Meça a posição da tag contra o **último** bloco `application/ld+json` servido, nunca contra uma lista do que a casca acha que imprime.
2. **O ID da ilha vai ESCRITO na régua do teste, nunca lido da constante.** Comparar a constante com o que a casca serviu é compará-la consigo mesma — e o único erro que isso nunca pegaria é o que vai acontecer de verdade, porque cada casca é copiada da anterior: o ID esquecido vai **ao ar funcionando**, sem uma linha de defeito visível, gravando sessão na propriedade da ilha vizinha por meses.

**O que fazer, em cada ilha, dentro da CASCA (nunca por plugin — seção 11.7):** imprimir no `wp_head`, o mais cedo possível, a tag do Google com o ID de medição da ilha:
- aquametria → `G-8Y26XFZF39`
- ~~robometria → `G-RM7KS75QP2`~~ **CUMPRIDO em 12/09/2026 17h23Z** (prioridade 23 do `wp_head`, `ferramentas/mutacoes-ga4.py` com 9 de 9 reprovadas)
- clubedomosaico → `G-0K5PY39HV7`

**Regras, porque esta tag entra numa página que a seção 22 governa:**
- O script de `googletagmanager.com` vai com `async`. Ele é o ÚNICO script de terceiro permitido na página pública.
- O ID **não é digitado no meio do código**: vira constante no topo do arquivo da casca, com o nome da ilha ao lado, do mesmo jeito que as outras constantes dela.
- A tag **não pode** atrasar o LCP nem entrar antes do `<title>`, da meta descrição ou do JSON-LD.
- **Nada de banner de consentimento bloqueante.** A seção 22.4 proíbe o que empurra a resposta para baixo da dobra. A página de privacidade da ilha passa a dizer, em uma frase, que o site usa GA4 para medir audiência.
- Versão da casca sobe, `sha256` do manifest é atualizado, Sync é acionado e o `/status` tem de bater com a revisão do manifest antes de dar por entregue (seção 4).

**Pronto quando:** nas três ilhas, o HTML servido da home contiver o `gtag` com o ID certo da ilha, o `/status` bater com o manifest, e o Tempo Real do GA4 registrar a própria visita de verificação. Escreva no `REGISTRO.md` de cada ilha a data em que a medição começou — é o marco zero da série, e a seção 21 vai precisar dele.

**A METADE DO "PRONTO QUANDO" QUE A NUVEM NÃO ALCANÇA, medida em 12/09/2026:** o ambiente das rotinas **não tem** a credencial da conta de serviço do Google (`python3 ferramentas/ga4.py <ilha>` responde *"Sem credencial: defina GOOGLE_SA_B64 (base64), GOOGLE_SA_JSON (conteúdo) ou GOOGLE_SA_FILE (caminho)"*). Então a confirmação no Tempo Real **não é da Fundação** enquanto essa variável não existir no ambiente: é do navegador do Raphael, ou de quem puser a credencial lá. O que a Fundação mede, e que é a metade que estava quebrada, é a tag certa no lugar certo no HTML servido. Nenhuma ilha fica com o item aberto por causa disto — ele é humano, como o reenvio do sitemap.
