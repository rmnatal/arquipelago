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

### prioridade NORMAL — duas linhas de configuração que destravam a medição inteira

12/09/2026 — RAPHAEL — Nada aqui é código, e nenhuma das duas bloqueia bloco: as duas ampliam o que a nuvem consegue **verificar sozinha**, em toda ilha presente e futura.

1. **`www.googletagmanager.com` e `*.google-analytics.com` na rede Personalizada** dos ambientes das rotinas ("Arquipélago — Fundação" e "Arquipélago — Mãos no repositório", em claude.ai/code → seletor de ambiente → engrenagem), junto com os domínios das ilhas que já estão lá. Sem isso, a Fundação prova que a tag **está** na página e nunca que a visita **chega** na propriedade — e essas duas coisas falham por motivos diferentes. A ferramenta que fecha isso já existe e está commitada: `ilhas/clubedomosaico/ferramentas/conferir-tag-no-navegador.mjs`, escrita em 12/09 e **nunca vista aprovando**, exatamente por causa deste 403.
2. **A credencial da conta de serviço do Google no ambiente** (`GOOGLE_SA_B64`, o JSON em base64 numa linha só). A conta de serviço **já é Leitor** na conta `Arquipélago` (`407777291`), então falta a variável, não a permissão. Com ela, `python3 ferramentas/ga4.py <ilha>` passa a alimentar a série `ilhas/<ilha>/dados/audiencia.md` na ronda, e a seção 5 vira número em vez de intenção.

**Pronto quando:** de dentro de uma rotina, `curl -s -o /dev/null -w "%{http_code}" https://www.googletagmanager.com/gtag/js?id=G-0K5PY39HV7` devolver 200, e `python3 ferramentas/ga4.py clubedomosaico --dias 7` devolver uma leitura em vez da linha "Sem credencial".

**O que NÃO se faz enquanto isso, escrito aqui para valer para toda ilha:** mandar evento pelo Measurement Protocol para "confirmar" que a medição funciona. Seria inventar a visita que se queria comprovar e sujar a série com uma sessão que nunca existiu. Zero medido é dado; zero fabricado é mentira.

---

## FECHADOS

**Despacho fechado nunca é apagado** — ele fica aqui inteiro, com a linha de fechamento
dentro dele. Esta seção nasceu em 12/09/2026, junto com o primeiro fechamento: o arquivo
prometia "abertos e fechados" desde a primeira linha e só tinha a metade de cima, e um
despacho cumprido embaixo do título **ABERTOS** é exatamente a armadilha que o próprio
despacho do GA4 registra ter caído — resumo velho lido como fato.

### prioridade ALTA — GA4 na casca das três ilhas

12/09/2026 — FUNDAÇÃO — As três ilhas agora têm propriedade GA4 e nenhuma tem a tag no ar. Sem isso a seção 5 (visibilidade em IA) não é mensurável: as referências de `chatgpt.com`, `perplexity.ai` e `gemini.google.com` só aparecem no GA4. Na Real 21, medido em 12/09/2026, o canal "AI Assistant" já é 264 sessões em 7 dias e o terceiro maior da casa — é por isso que isto fura a fila.

**ESTADO EM 12/09/2026 17h50Z — AS TRÊS CUMPRIDAS; o despacho está FECHADO (ver a linha de fechamento no fim deste bloco).** Robometria às 17h23Z (casca 1.5.0, manifest revisão 21, `conferir-no-ar.py` com 138 afirmações, 0 falha, nas nove URLs), **Aquametria** às 17h39Z (casca 1.6.0, manifest revisão 54, 168 afirmações nas 13 URLs) e **Clube do Mosaico** às 17h37Z (casca 1.7.0, manifest revisão 13, 334 afirmações nas 11 URLs). Quem atualizar esta linha: ela é resumo, e **a verdade está nas três linhas de ID mais abaixo** — foi lida como fato por uma execução enquanto já estava velha.

**A TERCEIRA, ACHADA NA AQUAMETRIA, E ELA CORRIGE A PRIMEIRA FRASE DESTE DESPACHO — "nenhuma tem a tag no ar" era FALSO para a Aquametria.** Antes de escrever uma linha de código, o medidor novo foi rodado contra o site como ele estava, para provar que sabia distinguir (77 falhas, como devia) — e no meio delas apareceu que as **treze páginas já serviam** um `gtag/js?id=GT-PL9DD7KW`, posto pelo plugin **Google Site Kit**, que é legítimo na ilha (seção 11.7 o deixa opcional, e o Raphael fez a conexão). Três coisas saem daí, e a terceira é para quem pegar o Clube do Mosaico:

   (a) **MEÇA O QUE JÁ ESTÁ NO AR ANTES DE ACRESCENTAR TAG.** Um `curl` na home, procurando `googletagmanager`, custa segundos e responde se a ilha já mede — e a resposta muda o bloco.

   (b) **O PORTÃO NÃO PODE LOCALIZAR A TAG PELA PALAVRA "googletagmanager": localiza pelo ID DA ILHA.** Na primeira versão do medidor, três afirmações de ordem deram **verde com a nossa tag ausente**, porque a posição que elas leram era a da tag do Site Kit. É a cicatriz da seção 8 na escolha do localizador: quando o texto legítimo e o que se quer medir são a mesma palavra, quem decide é o identificador, nunca a vizinhança.

   (c) **PRECISA DE RESPOSTA DO RAPHAEL, porque muda número e ninguém na nuvem pode ler.** `GT-PL9DD7KW` é um Google Tag, e para onde ele roteia só se lê logado (`www.googletagmanager.com` responde `000` por política de egresso, remedido duas vezes). **Se ele rotear para a propriedade 553860444 da Aquametria, a página vista chega DUAS vezes e a série da seção 5 nasce dobrada** — e número medido errado é pior que número digitado errado, porque parece conferido. A tag do Site Kit **não foi tocada** por esta execução, de propósito: desligar medição que o Raphael montou, sem saber o que ela alimenta, não é conserto de bloco. Até a resposta chegar, a primeira leitura de `dados/audiencia.md` da Aquametria sai com essa ressalva escrita ao lado. A Robometria e o Clube do Mosaico **não têm** o Site Kit servindo tag, então isto é só da Aquametria.

**Duas coisas aprendidas na Robometria que valem para as duas que faltam, e que não estavam escritas aqui:**
1. **O portão mede ORDEM, não presença.** "A tag está na página" é a afirmação fácil e é a que não protege nada: um JSON-LD novo numa prioridade acima da tag quebra a regra deste despacho sem tirar a tag do lugar. Meça a posição da tag contra o **último** bloco `application/ld+json` servido, nunca contra uma lista do que a casca acha que imprime.
2. **O ID da ilha vai ESCRITO na régua do teste, nunca lido da constante.** Comparar a constante com o que a casca serviu é compará-la consigo mesma — e o único erro que isso nunca pegaria é o que vai acontecer de verdade, porque cada casca é copiada da anterior: o ID esquecido vai **ao ar funcionando**, sem uma linha de defeito visível, gravando sessão na propriedade da ilha vizinha por meses.

**O que fazer, em cada ilha, dentro da CASCA (nunca por plugin — seção 11.7):** imprimir no `wp_head`, o mais cedo possível, a tag do Google com o ID de medição da ilha:
- ~~aquametria → `G-8Y26XFZF39`~~ **CUMPRIDO em 12/09/2026 17h39Z** (casca 1.6.0, manifest revisão 54, `/status` conferido em um disparo; `ferramentas/teste-ga4.py` com 216 afirmações e `ferramentas/mutacoes-ga4.py` com 13 de 13 reprovadas; `ferramentas/conferir-ga4-no-ar.py` com 168 afirmações no HTML servido das 13 URLs, 0 falha)
- ~~robometria → `G-RM7KS75QP2`~~ **CUMPRIDO em 12/09/2026 17h23Z** (prioridade 23 do `wp_head`, `ferramentas/mutacoes-ga4.py` com 9 de 9 reprovadas)
- ~~clubedomosaico → `G-0K5PY39HV7`~~ **CUMPRIDO em 12/09/2026 17h37Z** (casca 1.7.0, prioridade 8 do `wp_head`, manifest revisão 13, `/status` conferido em um disparo; `teste-casca.php` de 409 para 539 afirmações e `ferramentas/mutacoes-ga4.py` com 14 de 14 reprovadas; `conferir-no-ar.py` de 231 para 334 afirmações no HTML servido das 11 URLs, 0 falha. A página de Privacidade mudou junto, porque ela prometia por escrito ser atualizada ANTES de a medição ser ligada)

**Regras, porque esta tag entra numa página que a seção 22 governa:**
- O script de `googletagmanager.com` vai com `async`. Ele é o ÚNICO script de terceiro permitido na página pública.
- O ID **não é digitado no meio do código**: vira constante no topo do arquivo da casca, com o nome da ilha ao lado, do mesmo jeito que as outras constantes dela.
- A tag **não pode** atrasar o LCP nem entrar antes do `<title>`, da meta descrição ou do JSON-LD.
- **Nada de banner de consentimento bloqueante.** A seção 22.4 proíbe o que empurra a resposta para baixo da dobra. A página de privacidade da ilha passa a dizer, em uma frase, que o site usa GA4 para medir audiência.
- Versão da casca sobe, `sha256` do manifest é atualizado, Sync é acionado e o `/status` tem de bater com a revisão do manifest antes de dar por entregue (seção 4).

**Pronto quando:** nas três ilhas, o HTML servido da home contiver o `gtag` com o ID certo da ilha, o `/status` bater com o manifest, e o Tempo Real do GA4 registrar a própria visita de verificação. Escreva no `REGISTRO.md` de cada ilha a data em que a medição começou — é o marco zero da série, e a seção 21 vai precisar dele.

**FECHADO EM 12/09/2026 17h50Z — as três ilhas estão medindo.** As três execuções paralelas da Fundação cobriram uma ilha cada, e o `gtag` com o **ID certo de cada uma** foi medido no HTML servido, agora, numa passada só: aquametria `G-8Y26XFZF39`, robometria `G-RM7KS75QP2`, clubedomosaico `G-0K5PY39HV7`. O `/status` batendo com o manifest está registrado no `REGISTRO.md` de cada ilha, por quem a executou. O marco zero de cada série também.

**A METADE DO "PRONTO QUANDO" QUE A NUVEM NÃO ALCANÇA, medida em 12/09/2026:** o ambiente das rotinas **não tem** a credencial da conta de serviço do Google (`python3 ferramentas/ga4.py <ilha>` responde *"Sem credencial: defina GOOGLE_SA_B64 (base64), GOOGLE_SA_JSON (conteúdo) ou GOOGLE_SA_FILE (caminho)"*). Então a confirmação no Tempo Real **não é da Fundação** enquanto essa variável não existir no ambiente: é do navegador do Raphael, ou de quem puser a credencial lá. O que a Fundação mede, e que é a metade que estava quebrada, é a tag certa no lugar certo no HTML servido. Nenhuma ilha fica com o item aberto por causa disto — ele é humano, como o reenvio do sitemap.

**E EXISTE UMA SEGUNDA CAUSA, INDEPENDENTE DA CREDENCIAL, que a execução da Aquametria não tinha como ver — medida no Clube do Mosaico em 12/09/2026 17h41Z:** `www.googletagmanager.com` está **fora da lista de egresso** do ambiente das rotinas. O gateway responde **403 ao CONNECT**, cinco vezes seguidas, com `clubedomosaico.com.br` respondendo 200 na mesma passada — é **política**, e não a intermitência de túnel da seção 20.2 (que foi retestada, como ela manda). A consequência é maior que o item do despacho, e por isso ela sobe para cá em vez de ficar no `ESTADO.md` de uma ilha: **enquanto esse host estiver barrado, nenhuma verificação de tag por navegador a partir da nuvem pode funcionar em ilha nenhuma**, porque o navegador não baixaria o `gtag.js`. Some-se que o Chromium não atravessa este túnel nem para o domínio liberado (`ERR_CONNECTION_RESET` em 3 tentativas, `ws_closed_mid_exchange` no proxy, `curl` em 200 no mesmo minuto). Ou seja: a Fundação mede a tag no HTML servido, e **só isso**, por dois motivos somados e não por um.

---
