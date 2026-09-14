# DESPACHOS DO ARQUIPÉLAGO

Fila de despachos abertos e fechados, em ordem cronológica. Um despacho é uma
instrução para uma execução futura — Sentinela ou Fundação. **Nunca apagar
despacho fechado**: fecha-se escrevendo a data e a justificativa embaixo dele.

Formato de cada linha de abertura: `data — destinatário — o que fazer`.
Prioridade: `alta` fura a fila da próxima execução do destinatário.

---

## ABERTOS

### prioridade NORMAL — duas linhas de configuração que destravam a medição inteira

12/09/2026 — RAPHAEL — Nada aqui é código, e nenhuma das duas bloqueia bloco: as duas ampliam o que a nuvem consegue **verificar sozinha**, em toda ilha presente e futura.

1. **`www.googletagmanager.com` e `*.google-analytics.com` na rede Personalizada** dos ambientes das rotinas ("Arquipélago — Fundação" e "Arquipélago — Mãos no repositório", em claude.ai/code → seletor de ambiente → engrenagem), junto com os domínios das ilhas que já estão lá. Sem isso, a Fundação prova que a tag **está** na página e nunca que a visita **chega** na propriedade — e essas duas coisas falham por motivos diferentes. A ferramenta que fecha isso já existe e está commitada: `ilhas/clubedomosaico/ferramentas/conferir-tag-no-navegador.mjs`, escrita em 12/09 e **nunca vista aprovando**, exatamente por causa deste 403.
2. **A credencial da conta de serviço do Google no ambiente** (`GOOGLE_SA_B64`, o JSON em base64 numa linha só). A conta de serviço **já é Leitor** na conta `Arquipélago` (`407777291`), então falta a variável, não a permissão. Com ela, `python3 ferramentas/ga4.py <ilha>` passa a alimentar a série `ilhas/<ilha>/dados/audiencia.md` na ronda, e a seção 5 vira número em vez de intenção.

**Pronto quando:** de dentro de uma rotina, `curl -s -o /dev/null -w "%{http_code}" https://www.googletagmanager.com/gtag/js?id=G-0K5PY39HV7` devolver 200, e `python3 ferramentas/ga4.py clubedomosaico --dias 7` devolver uma leitura em vez da linha "Sem credencial".

**O que NÃO se faz enquanto isso, escrito aqui para valer para toda ilha:** mandar evento pelo Measurement Protocol para "confirmar" que a medição funciona. Seria inventar a visita que se queria comprovar e sujar a série com uma sessão que nunca existiu. Zero medido é dado; zero fabricado é mentira.

### prioridade NORMAL — a Fundação já roda mais vezes do que há ilha para construir

12/09/2026 — RAPHAEL — Medido às 23h17Z: **três ilhas no arquipélago e quatro execuções da Fundação vivas na mesma janela de três minutos** — clubedomosaico reservada às 22h25Z e trabalhando (Sync na revisão 16 às 23h13m30Z), robometria às 23h18Z, aquametria às 23h19Z, e a quarta é a que escreve este despacho. Ela reservou a robometria, **perdeu a corrida do push por cerca de um minuto**, voltou ao passo 2 da seção 1 como manda o contrato e **não havia ilha para pegar**. Fechou em "nada elegível" sem construir nada.

**Não é defeito e não bloqueia ilha nenhuma.** A reserva por commit funcionou exatamente como foi desenhada: ninguém se atropelou, nenhum trabalho foi perdido, nenhuma ilha ficou com duas execuções dentro. É **aritmética**: a rotação da seção 1 supõe que sobra ilha para quem perde a corrida, e com três ilhas a quarta execução da janela não tem o que fazer. Quanto mais frequente o disparo, maior a fração de execuções que fecha vazia.

**Duas saídas, e as duas são suas — a Fundação não mexe em nenhuma:**
1. **A Bússola entrega a ilha 4** (e a 5). A fila já está pontuada em `bussola/fila.md` e o topo disponível é **energia solar off-grid / estação portátil** (índice 4,20, paramétrica aberta), seguido de **nobreak e estabilizador** (4,19) — nenhum dos dois tem dossiê escrito ainda, e `bussola/dossies/` está vazia. Ilha nova é pasta nova: nenhuma rotina muda.
2. **Espaçar os disparos da rotina "Arquipélago — Fundação"** para no máximo um por janela de ~40 minutos, que é a ordem de grandeza de um bloco. Configuração da sua conta, em claude.ai/code.

A primeira é a que faz a fábrica crescer; a segunda só para de gastar execução. Dá para fazer as duas.

**Pronto quando:** o número de ilhas não bloqueadas for maior ou igual ao número de execuções da Fundação que disparam na mesma janela de 40 minutos — ou seja, quando toda execução que acorda tiver ilha elegível para reservar.

**MEDIÇÃO DE 13/09/2026, 11h19Z, por uma execução que ACHOU ilha — e por isso ela vale:** três execuções da Fundação reservaram nos minutos 11h18, 11h19 e 11h19, uma para cada ilha do arquipélago, e **todas as três acharam trabalho**. A folga é exatamente ZERO: a que escreve esta linha perdeu a robometria por cerca de um minuto, perdeu a clubedomosaico por outro, e pegou a aquametria, que era a última. A quarta execução daquela janela teria fechado em "nada elegível", como aconteceu ontem às 23h17Z. A reserva por commit segue funcionando como desenhada — ninguém se atropelou, nenhuma ilha ficou com duas execuções dentro. O que falta continua sendo ilha, não mecanismo.

**A metade que a Fundação já fez sozinha:** a seção **1.1** do `ARQUIPELAGO.md` nasceu desta mesma execução e conserta o lado que era da máquina — a reserva vencida que esconde execução viva. Sem ela, esta execução teria pegado a clubedomosaico pela letra do passo 3 e mandado um **segundo** e-mail de acesso para a sua mãe, invalidando o link do primeiro na véspera do domingo.

### prioridade NORMAL — dois domínios de fonte que a Aquametria já perdeu campo por não alcançar

13/09/2026 — RAPHAEL — Nada aqui é código e isto **não bloqueia bloco nenhum**: a Aquametria constrói normalmente e o banco dela cresce. O que trava é uma família específica de campo, e ela já custou quatro passadas medidas.

**O pedido, e é da mesma família do despacho de 12/09:** acrescentar `www.fishbase.se`, `www.fishbase.org` e `www.seriouslyfish.com` à lista "Domínios permitidos" dos ambientes das rotinas (claude.ai/code → seletor de ambiente → engrenagem), junto com os domínios das ilhas que já estão lá.

**O que está acontecendo hoje.** Os três respondem `connect_rejected` ao CONNECT, por POLÍTICA de egresso — não é intermitência de túnel, e foi reconferido com `curl` em 13/09/2026 como a 20.2 manda testar antes de declarar. **Todo o banco de espécies desta ilha foi colhido por BUSCA RESTRITA ao domínio**, com "a confirmar na ficha" escrito em cada fonte. A busca funciona e sustenta a maior parte dos campos; o que ela não alcança é a ficha inteira.

**O custo medido, e ele não é hipotético:**
- **Molly** (`Poecilia sphenops`), campo `comprimento_minimo_aquario_cm`: a busca devolveu `90 × 30 × 30 cm` em UMA passada e em nenhuma das outras três que não carregavam o número na consulta. Uma passada não é confirmação, então o campo ficou nulo. **Ele sozinho levaria `/peixes/vivaparos/` de 2 para 3 espécies elegíveis, que é o mínimo exato do 16.5** — ou seja, uma categoria inteira de malha esperando um número que está publicado numa página que a nuvem não abre.
- **Guppy** (`Poecilia reticulata`): três tentativas (09/09, 11/09, 13/09) de achar um segundo corpo de fonte. O peixe mais vendido do Brasil é um dos poucos sem ficha própria no compêndio, e o aviso E15 do validador fica de pé de propósito.
- **Cascudo** (`Ancistrus cirrhosus`), campo `temperatura_C`: duas tentativas (09/09, 13/09). Nenhum dos dois corpos declara faixa térmica para a espécie por busca.

**Em todas essas passadas a busca ofereceu SOZINHA o número da espécie congênere** — 60 cm de *P. velifera* para o molly, pH 6,0–6,5 de "espécies aparentadas" para o cascudo — e em todas foi recusado. A regra da congênere é da ilha e continua valendo com ou sem este despacho: **parâmetro de água de espécie vizinha é chute com cara de dado.** O que o acesso direto muda não é a regra, é poder ler a ficha certa.

**Pronto quando:** de dentro de uma rotina, `curl -s -o /dev/null -w "%{http_code}" https://www.seriouslyfish.com/species/poecilia-sphenops/` devolver 200.

**O que NÃO se faz enquanto isso, e vale para toda ilha:** completar campo com o valor da espécie vizinha, ou gravar um número que voltou UMA vez como se tivesse sido confirmado. Campo nulo com o motivo escrito é dado; campo preenchido por vizinhança é mentira com cara de medição.

**QUARTA E QUINTA MEDIÇÕES DE CUSTO, 13/09/2026 às 21h21Z, e a quarta MUDA o que este despacho destrava.** A Aquametria voltou a este par de domínios num bloco de banco, e o que ela mediu não é mais custo do mesmo tipo:

- **Molly (`Poecilia sphenops`), campo `comprimento_minimo_aquario_cm` — os DOIS corpos já foram perguntados.** Até hoje o que se sabia era que o compêndio publica a seção de dimensões dele **vazia**, e a saída óbvia era perguntar à base científica, que tem seção de aquário e é quem sustenta esse mesmo campo para o platy (60 cm) e para o plati variatus (60 cm). **Foi perguntado, em duas passadas limpas, e a base também não entrega:** devolveu nas duas o número da espécie **vizinha**, uma citando este peixe e a outra citando a *P. velifera* — o que é impressão digital de vazamento e não uma leitura. Antes era "a fonte da vez tem buraco, tente a outra"; agora é "as duas foram perguntadas e nenhuma entregou". **Este campo só sai da leitura direta**, e ele sozinho leva `/peixes/vivaparos/` de 3 para 4 espécies, que é a diferença entre categoria no mínimo exato e categoria com folga.
- **Plati variatus (`Xiphophorus variatus`), o registro novo:** a ficha do compêndio desta espécie **tem** seção de dimensões de aquário, e três formulações de busca restrita não alcançaram os valores dela. Aqui o buraco é da **nossa leitura**, não da fonte — e como o `dominio_por_campo` põe o compêndio na frente em campo de manutenção, a frente mínima gravada veio da base científica e é a **primeira a reconferir** no dia em que o acesso abrir.
- **Duas espécies recusadas na mesma passada por esta mesma parede:** *P. latipinna* e *P. velifera*, as duas por falta de frente mínima declarada, as duas com o motivo escrito em `especies_recusadas`.

**O que continua NÃO mudando:** nenhuma dessas recusas foi convertida em número. A regra da congênere vale com ou sem este despacho, e foi ela que recusou os cinco valores que a busca ofereceu sozinha nesta passada.

### prioridade NORMAL — as ilhas não têm caixa de e-mail, e é o único elo que falta na página de privacidade

13/09/2026 — RAPHAEL — Atravessa ilha, e por isso está aqui e não no `PROMPT.md` de nenhuma: **nenhuma das três tem um endereço de e-mail próprio.** A clubedomosaico já registrava isso como pendência (`contato@clubedomosaico.com.br` não existe como caixa) e a aquametria acabou de esbarrar no mesmo buraco por outro caminho.

**O que aconteceu:** a `/politica-de-privacidade/` da Aquametria nasceu em 13/09/2026, no ar e conferida. Tudo o que ela afirma foi medido — e a única coisa que ela **não** consegue oferecer é um canal para pedido formal de titular, porque não existe endereço para onde mandar. A página diz isso com todas as letras, numa seção chamada "O que falta nesta página, dito aqui em vez de escondido", porque omitir seria pior. **Na prática o caso do leitor não fica travado** (não há dado dele no site para consultar, corrigir ou apagar — não há cadastro, não há formulário, e o servidor não grava cookie nenhum), mas o canal precisa existir.

**Por que é seu e não da Fundação:** criar caixa de e-mail é criar conta em plataforma, e a seção 7 do contrato proíbe a Fundação de fazer isso, sempre, sem exceção. O endereço pessoal do Raphael também não entra em página pública por decisão de quem manda nele.

**Pronto quando:** existir uma caixa por ilha (`contato@aquametria.com.br`, `contato@robometria.com.br`, `contato@clubedomosaico.com.br` — ou uma só, se preferir) e o endereço estiver escrito no `PROMPT.md` da ilha. A partir daí a Fundação troca a seção "o que falta" pela linha do canal, num conserto de uma linha por ilha, e a `/contato/` da clubedomosaico deixa de esperar.

**O que NÃO se faz enquanto isso:** publicar um endereço que ninguém lê. Canal que não responde é pior que canal declarado ausente — o primeiro promete e falha, o segundo diz a verdade e envergonha quem tem de resolver, que é o efeito certo.

### prioridade NORMAL — O CABEÇALHO DE ESTADO DE UMA ILHA PODE NÃO SER YAML VÁLIDO, E NADA MEDE ISSO

13/09/2026 — FUNDAÇÃO (quem reservar a aquametria) — Medido às 19h58Z por uma execução da
clubedomosaico, ao validar o próprio cabeçalho antes de fechar o bloco.

**O achado.** A seção 2 do `ARQUIPELAGO.md` manda o cabeçalho de todo `ESTADO.md` ser um bloco
**YAML**, e mostra o bloco. O `bloco_atual` cresceu de "4c" para prosa de milhares de
caracteres entre aspas duplas — e **aspas duplas dentro de um escalar de aspas duplas quebram o
YAML**. Passando os três pela `yaml.safe_load`:

- `clubedomosaico` — era **inválido** nesta execução e foi consertado no mesmo commit: as aspas
  internas viraram simples e uma barra invertida dentro de uma regex citada saiu da prosa
  (`\d` é sequência de escape desconhecida em YAML de aspas duplas, e ela sozinha derruba o
  arquivo).
- `aquametria` — **INVÁLIDO hoje.** O erro é na linha do `bloco_atual`, coluna 1910: a prosa
  cita a etiqueta do Google entre **aspas duplas**. Essa é a metade que este despacho pede.
- `robometria` — válido.

**Por que ninguém viu.** Hoje quem lê o cabeçalho é a Fundação, com `grep` e com o olho, e as
duas coisas atravessam YAML quebrado sem reclamar. O defeito só aparece no dia em que alguma
ferramenta parsear o cabeçalho de verdade — e a seção 1 é feita de decisões tomadas a partir
dele: `estado`, `bloqueada_por`, `executando_desde`, `ultima_execucao`. **Cabeçalho que só o
olho lê é cabeçalho sem portão**, e é a mesma família do número de tela digitado: parece
conferido.

**A quem cabe, e por quê.** A seção 3 proíbe editar arquivo de ilha que não se reservou, e a
aquametria estava reservada por outra execução às 19h18Z. Então **quem reservar a aquametria
conserta o `bloco_atual` dela** — as aspas internas viram simples, como as entradas antigas
desta fábrica já fazem — e não precisa de mais nada.

**A metade que vale para TODA ilha JÁ ESTÁ ESCRITA, e não é deste despacho:** a regra de passar
o cabeçalho por um parser antes do commit entrou na **seção 2 do `ARQUIPELAGO.md`** nesta mesma
execução, com o comando de uma linha e a convenção de usar aspas simples dentro do
`bloco_atual`. Regra nova se escreve no contrato uma vez e vale para toda ilha, inclusive as que
ainda não nasceram — este despacho existe só para a metade que a seção 3 não me deixa consertar.

**Pronto quando:** o cabeçalho da aquametria passar por essa linha sem exceção. Os outros dois já
passam.

**MEDIDO EM 14/09/2026 às 00h05Z, por uma execução da clubedomosaico, e o "pronto quando" está
SATISFEITO:** os **três** `ESTADO.md` do arquipélago passam por `yaml.safe_load` sem exceção — a
execução das 21h21Z da aquametria consertou a metade que faltava, e o commit dela diz isso na
mensagem ("o cabeçalho do ESTADO.md volta a ser YAML válido"). Quem escreve esta linha **não
reservou a aquametria** e portanto não tocou em arquivo nenhum daquela ilha (seção 3); o que dá
para fazer daqui é registrar a medição onde ela evita que a próxima execução gaste o bloco
procurando um defeito que já não existe. **A regra que sobrou deste despacho é a da seção 2 do
`ARQUIPELAGO.md`** — passar o cabeçalho por um parser antes do commit —, e ela vale para toda
ilha, inclusive as que ainda não nasceram.

**O que NÃO se faz:** trocar a prosa do `bloco_atual` por texto curto para o YAML fechar. A
prosa longa é o que faz a próxima execução saber o que aconteceu sem abrir o `REGISTRO.md`
inteiro; o que está errado é a citação, não o tamanho.

---

## FECHADOS

### prioridade MÁXIMA — o ateliê da artesã tem de estar de pé no domingo 13/09

12/09/2026 — FUNDAÇÃO — O Raphael vai à casa dos pais no domingo e quer ensinar a mãe a entrar no site e cadastrar as peças dela. O escopo cortado está no fim de `ilhas/clubedomosaico/PROMPT.md`, no "DESPACHO DO RAPHAEL — 12/09/2026, 18h20 BRT". A clubedomosaico está com `prioridade: 1`. Enquanto este despacho estiver aberto, toda execução da Fundação vai para ela.

**FECHADO em 12/09/2026 23h20Z, e o critério de pronto que ele mesmo escreveu foi cumprido pela metade que a nuvem alcança — a outra metade está nomeada, não escondida.**

Os cinco itens do corte saíram, nesta ordem, e cada um só depois do anterior estar de pé: CPT `peca` e o papel `artesa` com o bloqueio duplo do wp-admin; a usuária e **o e-mail de acesso, enviado às 23h13m23s Z** para mina196@hotmail.com; `/atelie/` com login e tela inicial; o formulário de peça em uma tela, no celular; e a ficha pública da peça com `Product`+`Offer`, com a `/loja/` listando. Manifest na revisão 17, `/status` conferido, snippets #9 (loja) e #10 (ateliê) criados pelo Sync.

**O PORTÃO DESTE DESPACHO NÃO PODE SER CUMPRIDO INTEIRO PELA FUNDAÇÃO, e isso não é desculpa — é a consequência de uma decisão que o próprio despacho de 10/09 tomou.** Ele manda "entre em /atelie/ como `artesa`, numa janela de 360 px, cadastre uma peça de teste com 3 fotos, publique, abra a página pública, volte, pause e apague". A senha da artesã **não existe** em lugar nenhum a que a nuvem tenha acesso: o snippet gera uma senha aleatória e a descarta sem imprimir em log, e-mail ou option, e o que chega a ela é um link na caixa dela. Gravar a senha ou criar um segundo acesso "só para testar" quebraria a única coisa que protege a conta de uma pessoa de verdade — e a pessoa aqui é a mãe do Raphael.

O portão foi então partido em duas metades **declaradas**, e as duas estão escritas no cabeçalho de `ilhas/clubedomosaico/ferramentas/teste-atelie.php`:

- **A metade que a máquina mediu, e mediu inteira:** todo o caminho de dentro do painel, com uma pessoa logada de mentira que tem as capacidades que o **snippet** criou — as telas, o formulário, salvar, publicar, pausar, apagar, as fotos, o nonce, o bloqueio do wp-admin e cada recusa com a frase que ela lê (209 afirmações). Mais a **janela de 360 px**, que é a medida escrita dentro do próprio portão, num Chromium de verdade: 91 medições em 6 páginas × 5 larguras, rolagem lateral zero, todo alvo de toque com 44 px ou mais, todo campo com 16 px ou mais (abaixo disso o iPhone dá zoom sozinho e a tela pula), nenhum par de campos lado a lado, e o painel inteiro num contexto com o JavaScript **desligado**. Foi esse medidor que achou os três botões de foto com 38 px — invisíveis em leitura de código e no HTML servido.
- **A metade que só um humano faz, e que fica aberta:** confirmar que o e-mail **chegou** na caixa da Hotmail (o `wp_mail` devolveu true, o que diz que o servidor **aceitou** a mensagem, não que ela passou do filtro de spam), e o dedo dela na tela.

**A frase que o despacho pede que o Raphael possa ler no domingo de manhã:** *o ateliê está de pé e ele pode ensinar a mãe hoje — abra o e-mail dela antes de sair de casa, e se a mensagem não estiver na caixa de entrada, procure no spam; se ela estiver lá, o link funciona igual, e é o único passo que a nuvem não conseguiu conferir.* O endereço é `https://clubedomosaico.com.br/atelie/`.

**Uma coisa que ele vai querer fazer em um minuto, e que é de uma linha:** a option `cdm_whatsapp` está vazia, então a ficha da peça serve, no lugar do botão, a frase de que o contato ainda não foi publicado — em vez de um número inventado. Com o número lá, o botão "Falar com a artesã sobre esta peça" nasce funcionando.

### prioridade ALTA — primeira ronda do Clube do Mosaico

12/09/2026 — SENTINELA — clubedomosaico nunca teve ronda (ultima_ronda: null desde a subida). Fazer a primeira ronda completa na próxima execução, antes de qualquer outra ilha: voz (seção 15 + ilhas/clubedomosaico/VOZ.md), árvore e breadcrumb (seção 16), links internos e órfãos, e a lista mecânica da seção 19.1 com o teto de 5 consertos.

**FECHADO em 12/09/2026, e quem fechou não foi quem escreveu:** a ronda aconteceu às 14h43Z do mesmo dia — `ultima_ronda: 2026-09-12T14:43Z` no cabeçalho do `ESTADO.md` da ilha, e o `DESPACHO DA SENTINELA — 12/09/2026` no `PROMPT.md` dela conta o que foi medido: as 11 URLs e os 50 links internos em 200, nenhuma página órfã, os 12 exemplos da F1 recalculados à mão, e os dois itens de coerência da recomendação já cumpridos. **Este bloco continuou aqui embaixo de ABERTOS por horas depois de cumprido**, com prioridade ALTA, mandando a próxima Sentinela refazer uma ronda que já existia — que é exatamente a armadilha que o despacho do GA4 registra ter caído: resumo velho lido como fato. Fechado pela Fundação na execução das 19h20Z, ao ler a fila antes de escolher a ilha.


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

- **CUMPRIDO 13/09/2026** — o link de afiliado da cimentcola AC-II do Clube do Mosaico, gerado pelo Raphael no Mercado Livre e escrito no banco. Com ele, os 10 materiais da ilha (5 colas, 5 rejuntes) estão com link vivo; sobram as 10 pastilhas, que estão fora por decisão e não por pendência.

### clubedomosaico — a Loja e as fichas precisam mostrar o "Veja todos disponíveis aqui"

Aberto em 13/09/2026 pela seção 25. O banco já tem `afiliado.url_busca` e `afiliado.degrau` nos dez materiais, e `afiliado.imagem.url` em três deles (Cascorez, silicone acético e rejunte acrílico, vindos do feed da Shopee). Falta a casca e as fichas **usarem**: o botão de compra aponta para `url`, e logo abaixo, em texto discreto com `rel="sponsored nofollow noopener"`, a linha "Veja todos disponíveis aqui" apontando para `url_busca`. Onde houver `imagem.url`, mostre a foto com `width` e `height` (regra 22.4) e o `alt` que está no banco. **Item de `degrau` 3 sem `url_busca` não pode ir ao ar** — portão novo para o `teste-casca.php`.

### aquametria — piso de busca em todos os 78 itens, e os 39 links velhos sob suspeita

Reescrito em 13/09/2026 pela decisão de 25.2 ("100% automático, sem tocar").

**Passo único e inteiramente de máquina: gere `url_busca` para os 78 itens do banco**, pelo gerador da Shopee, que aceita clique de script — 5 URLs por lote, Sub_id 1 = `aquametria`, Sub_id 2 = o código da ferramenta de origem. A partir daí **nenhum item da ilha fica sem porta de compra**, e a ilha para de depender de qualquer pessoa.

Os 39 links antigos ficam onde estão **e sob suspeita declarada**: nasceram do degrau 3, são velhos, e o banco não guarda `url_produto`, então não há como conferi-los (25.4-b). Não os apague — com a 25.2 no ar, a página tem piso mesmo se algum estiver morto. Quando qualquer um for reescolhido, o novo sai com `url_produto`, `degrau` e `conferido_em`.

**Não espere feed. Não espere clique.** O feed oficial foi medido e não cobre aquarismo (25.3); o Mercado Livre daria links melhores mas exige o clique dele, e por 25.2 isso é oportunidade, não plano. Se sobrar folga numa execução, monte a lista de candidatos `/p/` do Mercado Livre e deixe pronta em `dados/links-afiliado-pendentes.md` — ele gera quando quiser, sem que nada dependa disso.

### robometria — a ilha recomenda peça e não tem UMA porta de compra. Piso de busca agora.

Reescrito em 13/09/2026 pela decisão de 25.2. **Prioridade alta: esta é a única ilha no ar com ZERO link**, e é a cicatriz da seção 8 aberta na ilha que a gerou — ela faz o trabalho caro da compatibilidade e entrega o clique de graça.

**Passo único e de máquina: `url_busca` nas 44 respostas** (`r1-respostas.json` 33, `r2-respostas.json` 11), pelo gerador da Shopee. A chave de busca é o nome da peça mais o modelo do robô, que é exatamente como a pessoa procura. Sub_id 1 = `robometria`, Sub_id 2 = R1 ou R2 conforme a ferramenta.

Três itens do `dados/feed-shopee-oficial.json` são peça de verdade (controle remoto Electrolux, pano mop Dreame, bateria WAP K21) — esses podem virar ficha de produto no degrau 1, com `url_produto` e foto. O resto fica no piso. **O recorte do feed já provou que loja oficial não vende reposição; não gaste execução procurando mais lá.**

---

## 13/09/2026 — FUNDAÇÃO — QUEM MEXE NO BANCO DE UMA ILHA TEM DE MEXER NO MANIFEST DELA, E DUAS EXECUÇÕES MEXERAM NA MESMA ILHA NA MESMA HORA

**Medido no Clube do Mosaico em 13/09/2026, duas vezes na mesma execução.** Os
commits `4e69738` (a escada do link de compra) e `35412c1` (o `url_produto` do
teste de vida) editaram `ilhas/clubedomosaico/dados/materiais-colas.json` e
`materiais-rejuntes.json` e **não tocaram no `manifest.json`**. A consequência
não é teórica e foi lida no `/status`: o Sync baixou os dois arquivos, comparou
com o `sha256` que o manifest ainda declarava e recusou aplicar —
`"materiais-colas: sha256 divergente — não aplicado"` — nas revisões 19, 20 **e**
21. **Os dez links novos, o `url_produto` e as três fotos ficaram no repositório
e fora do ar**, que é a seção 4 na forma mais pura. A trava fez o que devia; o
que faltou foi a metade de quem escreve.

**A regra, e ela já está na seção 3 — o que falta é ela valer para quem edita só
dado:** *todo arquivo publicável que muda tem o `sha256` recalculado e a
`revisao` incrementada no mesmo commit.* São dois comandos:
`python3 ferramentas/atualizar-manifest.py . --gravar` e subir a revisão. Sem
isso, editar o banco é escrever num arquivo que o site nunca vai ler. **E o
validador roda antes:** o `4e69738` também deixou 11 erros de esquema
(`mercado_livre` onde o vocabulário diz `mercadolivre`, `imagem` sem
`largura`/`altura`, contadores de cabeçalho desatualizados) — nenhum deles teria
sobrevivido a um `python3 ferramentas/validar-banco.py .`, que leva segundos.

**E A OUTRA METADE, que é do Raphael e não tem conserto do lado da Fundação:
duas execuções estavam trabalhando na MESMA ilha ao mesmo tempo.** A reserva por
commit da seção 1 funcionou como escrito — esta execução reservou a
clubedomosaico às 13h19Z depois de perder a robometria e a aquametria para outras
duas —, e mesmo assim uma terceira sessão editou o banco desta ilha às 13h36Z e
de novo depois. **A reserva protege contra quem a lê; não existe para quem entra
pela porta do dado.** O custo hoje foi barato (dois rebases e uma revisão a mais);
o custo caro é o do próprio 1.1: dois trabalhos concorrentes na ilha da artesã, no
dia em que ela ia aprender a usar o painel. Isto é decisão do Raphael, como a
aritmética de "três ilhas e quatro execuções" de 12/09: ou a camada de links de
afiliado passa a reservar a ilha como a Fundação reserva, ou ela deixa de tocar em
`ilhas/<ilha>/dados/` e vira despacho para quem tem a ilha na mão.

### clubedomosaico — o `PROMPT.md` dela não documenta o parâmetro de autenticação do endpoint de peças

Aberto em 13/09/2026 pela ronda da Sentinela na **aquametria**, que não tinha
outro canal, e movido para cá pela execução da Fundação das 15h16Z — o achado é
de outra ilha, e a seção 3 proíbe editar arquivo de ilha que não se reservou.

A seção 24.2 manda a ronda diária buscar o endpoint de leitura da clubedomosaico
e commitar `ilhas/clubedomosaico/dados/pecas.json`. O endpoint **existe** —
`https://clubedomosaico.com.br/wp-json/clubedomosaico/v1/pecas` responde **401** —
mas o `PROMPT.md` daquela ilha não documenta, em "Endpoints desta ilha", **o nome
do parâmetro de autenticação**. Sem isso a ronda não tem como montar a URL, e a
cópia da 24 não aconteceu naquela passada nem vai acontecer na próxima.

**Quem fecha:** a próxima execução da Fundação que reservar a clubedomosaico.
Escreva a URL COMPLETA e literal na seção "Endpoints desta ilha", do mesmo jeito
que o Sync e o `/status` já estão escritos lá.

### bússola — pontuar o nicho de viagem na rodada 004 (segunda, 14/09)

Aberto em 13/09/2026 pelo Raphael. O enquadramento, a medição de quatro SERPs e o levantamento de monetização já estão em `bussola/despacho-viagem.md` — a rodada não recomeça do zero. Os critérios eliminatórios da seção 2 do `BUSSOLA.md` foram ampliados no mesmo dia para permitir nicho de serviço; sem essa mudança, viagem reprovava nos quatro. Entrega esperada: dossiê completo, com as duas adaptações que o despacho exige.

### precisa do Raphael — conferir se a credencial da Open API já apareceu no painel

Aberto em 13/09/2026. A Shopee **aprovou** o acesso à Open API no mesmo dia do pedido (protocolo 2099140709749702724) e disse que a liberação sai **em até 5 dias úteis, direto no portal do afiliado**. A credencial aparece **sem aviso nenhum**, em `affiliate.shopee.com.br/open_api`, nos campos `AppID` e `Senha` que hoje mostram `--`.

**Nenhuma rotina alcança essa tela.** Então o passo é dele: abrir a página a partir de **18/09** e ver se os dois campos saíram do `--`. Quando saírem, ele passa os valores **no chat**, e eles viram variável de ambiente da rotina — nunca arquivo do repositório (regra em 25.6).

**O boletim de sexta 18/09 tem de carregar este lembrete em destaque.** É o único mecanismo que a gente tem contra o cenário provável: credencial liberada, ninguém olha, e ela fica parada por semanas.

**O que a Fundação constrói no dia em que a credencial chegar** — para não se descobrir o plano naquele dia:

1. `ferramentas/shopee.py`, irmão de `ga4.py`: mesmo `_bootstrap_venv()`, credencial só de ambiente, GraphQL por POST simples.
2. **Primeiro uso, e é o que paga a conta:** buscar produto por palavra-chave **com estoque**, para alimentar o degrau 1 da escada sem depender do feed que só ele baixa.
3. **Segundo uso:** conferir, todo dia na ronda, se os produtos já ligados continuam vivos — o que hoje exige abrir página no navegador e ler o texto (25.4).
4. A Shopee **não dá suporte**; a documentação está na Central do Afiliado, e é de lá que sai o esquema das consultas. Leia antes de escrever.
