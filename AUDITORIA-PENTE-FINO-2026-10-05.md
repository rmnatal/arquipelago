# AUDITORIA PENTE FINO — 05/10/2026

Varredura do estado real do `main` em `55cca0c` (02/10/2026 19h57Z). Branch `pente-fino`.

**102 arquivos lidos** — 32 de regra e prosa (`ARQUIPELAGO.md` 1025 linhas, `bussola/BUSSOLA.md`, `bussola/fila.md`,
`bussola/despacho-viagem.md`, `foco.md`, `dados/PAINEL.md`, os `PROMPT.md`/`ESTADO.md`/`VOZ.md`/`DESIGN.md` das cinco ilhas e do
`_modelo`, os dois `DOSSIE.md` + `VOZ.md` dos dossiês, `rodadas/004.md` e `005.md`), **4** relatórios de Pente Fino anteriores e
**66** JSON de `ilhas/*/dados/` (todos parseiam; 0 falha de parse). Mais **470 arquivos varridos** por grep na busca de segredo e
**4 `logo.svg`** comparados por md5.

**Resultado: 0 GRAVE · 19 correções MÉDIO aplicadas em 11 arquivos · 6 MÉDIO registrados · 4 BAIXO · 11 itens herdados ainda pendurados.**

**NENHUMA decisão desta semana foi tomada com base errada — e isso é dito com a medição na mão, não por boa vontade.** O candidato
óbvio a GRAVE era a seção 12 (achado 1): ela manda a ronda diária trabalhar só na ilha em foco, o que a decisão do Raphael de
28/09 revogou. Mas as rondas de **30/09** (`8c5c5a9`, "3 ilhas medidas no ar") e **02/10** (`36ee243`, três ilhas) obedeceram à
regra NOVA, e o `dados/PAINEL.md` de 02/10 abre declarando-a corretamente. A ponta velha estava de pé e **ninguém a executou**.
Os 19 consertos abaixo são, portanto, armadilhas desarmadas antes de cobrarem — não estragos a reparar.

---

## MÉDIO — CORRIGIDO (19 consertos, 11 arquivos)

### A FAMÍLIA DA SEMANA: a decisão de 28/09 deixou QUATRO pontas velhas, e uma delas foi escrita pelo próprio Pente Fino

Em 28/09/2026 o Raphael decidiu que a **ronda diária técnica roda em toda ilha que está no ar, em foco ou fora**, revogando a
metade da 1.2 que dizia que a ronda "não mede e não relata nenhuma outra ilha". A causa tinha nome e preço: o Clube do Mosaico
passou **nove dias fora do ar**, 16 das 17 URLs em 404, e ninguém viu porque a ilha estava fora do foco. O commit `4393e6f`
escreveu a decisão na §1.2 com todo o cuidado — e **não varreu as cópias**.

**1. `ARQUIPELAGO.md` §12 — a seção que as DUAS Sentinelas leem continuava dizendo que a escolha é pendente. CORRIGIDO.**
Trecho: *"Para a **ronda diária técnica**, a 1.2-b não separou as duas Sentinelas e a escolha está registrada como pendente do
Raphael no ponteiro da 1.2 — **até lá vale a letra desta linha**."* E a letra dessa linha é *"a ronda diária e a leitura semanal
trabalham só na ilha em foco e não abrem nenhuma outra"*. **A contradição:** a §1.2 diz, desde 28/09, *"O ponteiro de 21/09 deixou
esta metade em aberto e ela **está fechada**"*; a §12 diz que continua aberta e manda obedecer à versão velha. **A evidência que
decide:** a decisão é datada, nomeada e posterior; e o mapa de leitura da §0 põe **a §12 na linha dos dois papéis de Sentinela** —
ou seja, a ponta velha estava justamente no arquivo que quem ronda abre. Reescrita apontando para a decisão de 28/09, separando a
metade que MEDE (todas as ilhas no ar) da que CONSTRÓI (só a ilha em foco).

**2. `ARQUIPELAGO.md` §29.6 — "a 1.2 **diz**, com todas as letras, que ninguém ronda ilha fora do foco". CORRIGIDO.**
Presente do indicativo sobre uma frase revogada, e na seção que está nas **três** linhas do mapa de leitura. Trocado por "dizia",
com o ponteiro. É a mesma decisão, o mesmo arquivo, nove seções de distância.

**3 e 4. `ilhas/jornadafly/PROMPT.md` e `ilhas/ohmetria/PROMPT.md` — e aqui o Pente Fino repetiu o defeito que ele existe para
caçar. CORRIGIDO nas duas.** O aviso de foco das duas ilhas afirma que *"pela seção **1.2** do `ARQUIPELAGO.md` nenhuma outra ilha
recebe bloco da Fundação e **nenhuma outra ilha é rondada**"*. Logo acima dele há um **ponteiro do Pente Fino datado 28/09/2026** —
o mesmo dia da decisão — que conserta o nome da ilha em foco e conclui: *"**A conclusão deste aviso continua certa**; a ilha que ele
nomeia, não."* **A conclusão não continuava certa:** metade dela foi cortada naquele mesmo dia. O auditor abriu os dois arquivos,
corrigiu o detalhe que viu e **ratificou por escrito a frase que a decisão do dia tinha revogado**, em duas cópias. Mitigação
registrada: nenhuma das duas ilhas está no ar, e a própria §1.2 diz que ilha fora do ar não tem o que rondar — o efeito prático
hoje é **nulo**. A frase passa a ser falsa no dia em que qualquer uma subir, que é exatamente o dia em que ela custaria os nove dias
de novo.

### As outras treze

**5. `ARQUIPELAGO.md` §0 — a Bússola é mandada aplicar três seções que o mapa de leitura manda ela NÃO ler. CORRIGIDO.**
A linha dela era `10, 11, 14, 20, 21`. Mas a `BUSSOLA.md`, que é a lei dela, exige: no item (g) do §5, *"o `VOZ.md` da ilha, pronto,
no formato dos três existentes (…) (**seção 15** do `ARQUIPELAGO.md`)"*; no §3, que a âncora do **M** não seja a Amazon *"porque a
**seção 7** do `ARQUIPELAGO.md` a mantém fora de todas as ilhas"*; e no §6, que o canal de decisão é o repositório *"pelas Mãos —
**seção 12.2**"*. **Três seções que governam a saída da Bússola, e nenhuma na linha dela.** É a terceira vez que este exato defeito
é consertado: o Pente Fino acrescentou a **1.2** à linha da Sentinela em 16/09 e a **1.2-b** em 21/09, pela mesma razão. O desempate
está escrito na própria §0: *"errar por ler a mais é barato; errar por não saber a regra custa uma leva inteira"*. Linha agora
`7, 10, 11, 12.2, 14, 15, 20, 21`.

**6. `ARQUIPELAGO.md` §7 — pendência da Robometria cumprida em 20/09, afirmada no presente. CORRIGIDO com número.**
*"A Robometria corrige isto no próximo bloco publicável (ver despacho no PROMPT.md dela)."* **Medido por mim hoje:** `0 de 54` peças
publicáveis e `0 de 45` modelos publicáveis sem `afiliado.url_busca`. O piso da 25.2 está de pé desde 20/09; nenhum item publicável
fica sem saída de compra. Linha de fechamento escrita com a contagem; a regra do parágrafo continua valendo para toda ilha.

**7. `ilhas/clubedomosaico/DESIGN.md` — 64 px e ~96 px contra CINCO pontas que dizem 52 px e ~84 px. CORRIGIDO.**
Aberto desde **14/09** e deixado três vezes como "precisa do Raphael" — e não precisava: **a §22.2 nomeia o desempate** e nenhum
relatório a aplicou aqui. Ela é literal: *"o `DESIGN.md` manda na forma, o `VOZ.md` manda na palavra. **Quando os dois discordarem,
é o `VOZ.md` que decide**"*. O `VOZ.md:33` diz 52 px e ~84 px, e com ele concordam `PROMPT.md:356-357`, `ESTADO.md:301-302`, o
**código no ar** (`clubedomosaico-casca.php:969`, `height:52px`) e o **portão** (`conferir-no-ar.py:103-104`, que **reprova** se a
folha não mandar 52 px). A data fecha: o 52 px entrou no `VOZ.md` em **11/09** por decisão nomeada (`71a16c6`) e este arquivo nasceu
em **12/09** já trazendo 64 px, sem reler o vizinho do dia anterior. Obedecer ao número antigo deixava a bancada vermelha — classe 3.
**Nada no ar muda:** o site já serve 52 px. Se o Raphael quiser 64 px de verdade, a mudança é um bloco só, nos cinco lugares de uma vez.

**8. `ilhas/clubedomosaico/ARVORE.md:246` — "Esta ilha tem **11 URLs publicadas**". CORRIGIDO para 21, com procedência.**
Herdado de 16/09 e marcado "não verificado" em 28/09; agora **é** verificável: `ESTADO.md` traz `urls_publicadas: 21` (02/10 19h51Z,
depois do BLOCO 4c) e a ronda das 14h51Z mediu **17 no ar** antes dele. O argumento que a linha sustenta não muda — 21 continua
abaixo do piso de 40 —, e por isso o conserto é sem perda.

**9. `ilhas/jornadafly/PROMPT.md:20` — a fonte do corpo estava na lista de descarte e é obrigatória. CORRIGIDO.**
A lista dizia descartada *"a tipografia Fraunces/**Source Sans 3**"*, e o `DESIGN.md:69` manda *"Texto corrido: **Source Sans 3**
400/600"*, carregando-a no `:72`. Quem obedecesse à lista ficaria sem fonte de corpo. A troca real foi só no título (Fraunces →
Montserrat), e o desempate já estava na mesma linha: *"vale o `DESIGN.md`"*. Descarte estreitado ao Fraunces.

**10. `bussola/despacho-viagem.md:3` — duas ilhas não podem ser a nº 4. CORRIGIDO por ponteiro.**
O despacho chama a viagem de *"ilha nº 4"*; a nº 4 é a **ohmetria** (`ohmetria/PROMPT.md:19`, domínio pago em 14/09 às 15h00Z) e a
viagem é a **nº 5** (`jornadafly/PROMPT.md:19` e `fila.md`). Era a expectativa de 13/09, quando havia três ilhas e um candidato. O
arquivo é lido na primeira execução da ilha por ordem do `PROMPT.md:4` dela.

**11. `ilhas/_modelo/ESTADO.md:6` — o molde conta quatro ilhas vivas; o `PROMPT.md` do mesmo molde conta cinco. CORRIGIDO.**
São cinco pastas de ilha desde 15/09, e as cinco têm os dois campos. Errado no total e na contagem de quem os tinha.

**12 e 13. Os dois dossiês entregam identidade RECUSADA, sem um ponteiro. CORRIGIDO por ponteiro nos dois — e os dois casos não
são iguais.**
No **som automotivo**, a prosa descreve *"dois arcos espelhados (…) a silhueta de uma ferradura fechada"*, e o
`ilhas/ohmetria/DESIGN.md:12` registra a recusa com data e causa: *"a primeira proposta (dois arcos em ferradura, do dossiê) **foi
recusada por ele** (…) Fica escrito para ninguém 'restaurar' o desenho antigo"*. Aqui o arquivo **foi** atualizado e só a prosa
envelheceu: `dossies/som-automotivo/logo.svg` é **byte-idêntico** a `ilhas/ohmetria/logo.svg` (md5 `f147548d…`). Na **viagem** é pior,
e é o ponteiro mais necessário dos dois: além da prosa, **o `logo.svg` da pasta do dossiê continua sendo o desenho descartado** e
NÃO bate com `ilhas/jornadafly/logo.svg` — e o `jornadafly/PROMPT.md:4` manda a primeira execução ler o dossiê inteiro. Sem o
ponteiro, essa execução desenha a marca errada a partir de um arquivo que parece oficial. Junto vão a paleta de sete valores (o
`--sinal` oficial é `#378AD0`, não o índigo `#2F3E9E`) e o título Fraunces.

**14, 15 e 16. `ilhas/aquametria/PROMPT.md` — três ORDENS velhas na fila de blocos. CORRIGIDAS.**
(a) *"o banco não mediu as imagens e a ilha **não grava dimensão que não mediu**"* — contra a §22.4 (*"Toda imagem com `width` e
`height` no HTML"*), contra as **41 de 41** fotos fechadas no mutirão de 24/09 e contra a ronda de 02/10 (*"zero imagem sem
width/height"*). A condição que a própria linha previa já aconteceu. (b) A manchete *"O MUTIRÃO CONTINUA DESLIGADO"* (22/09) convive
com o despacho de **24/09** que o REABRIU mandando *"entregue quantos blocos couberem"* — ordens opostas no mesmo arquivo. Ponteiro
escrito: a janela **morreu sozinha em 30/09** pelo prazo do `foco.md`, então a manchete volta a ser verdadeira hoje por um caminho
que ela não descreve. (c) Um *"Pronto quando"* que cobra **14** itens nomeados quando são **12** desde 24/09 — critério escrito
sobre o caso que existia e que tinha virado impossível de cumprir, porque nomear os 14 incluiria dois registros que já não são
intestáveis.

**17, 18 e 19. `ilhas/robometria/ESTADO.md` — a cauda que o ponteiro de 28/09 não alcançou. CORRIGIDAS.**
O ponteiro do Pente Fino de 28/09 chegou às linhas 548 e 574 **e parou ali**. Atrás dele: (a) a linha de infraestrutura que manda
procurar *"paleta, tipografia e a geometria do símbolo (…) no `PROMPT.md` desta pasta"* — exatamente o arquivo que a §22.6 (12/09),
o `PROMPT.md:8` e o `DESIGN.md:3` declaram **não ser mais o dono**; quem a lesse editaria token no lugar errado. (b) Dois "achados
que valem para a próxima" que pedem bloco de dados à Fundação e estão **fechados desde 11/09** (121 strings de acentuação
restauradas, com portão novo; e a regra do nível 2 decidida — manual de terceiro colhido por busca é nível 3). (c) Um parágrafo que
declara **44 itens esperando link de afiliado**, o site na **revisão 6** e o trabalho como sendo *"no navegador do Raphael"* —
quando a ilha fechou **95 de 95 publicáveis rendendo comissão** em 20/09, o `/status` está na **revisão 81**, e a §7 decidiu em
**22/09** que *"o portal de afiliado da Shopee aberto no Chrome do Raphael não é mais pré-requisito de nenhuma rotina"*. Esse último
põe na conta dele um trabalho que é da Fundação e que nesta ilha já está feito.

---

## MÉDIO — PRECISA DO RAPHAEL (6 novos)

**20. Segredo: o token do Sync está em texto puro em TRÊS ilhas, não em uma — e a dívida registrada só conhecia uma.**
A dívida conhecida era a do Clube do Mosaico. Medido hoje: `ilhas/clubedomosaico/PROMPT.md` **linhas 53 e 55** (o mesmo token
também abre a rota que copia o dado das peças da artesã), `ilhas/aquametria/PROMPT.md` **linha 14** mais **12 repetições** no
`REGISTRO.md` dela (linhas 4166, 4328, 4552, 4744, 4958, 5141, 5142, 5271, 5272, 5388, 5390, 5522), e
`ilhas/robometria/PROMPT.md` **linha 21**. Tipo: token de disparo do Sync, 32 caracteres. **Nenhum valor é transcrito aqui, nem foi
para o commit.** Três das cinco ilhas. Rotação é o único conserto real, porque os valores estão no histórico do git — e rotação é
dele. **A causa sistêmica, que é consertável sem ele:** `ilhas/_modelo/PROMPT.md` não tem **uma linha** sobre segredo, então toda
ilha nova reproduz o padrão. Junto: dois `google-site-verification` em `clubedomosaico/ESTADO.md:90` e `robometria/ESTADO.md:221`; e
o `.gitignore` tem 5 linhas e **nenhuma** cobre `.env`, `*.pem`, `*.key` ou JSON de conta de serviço — rede de proteção para o
próximo vazamento, não remédio para estes. Não consertei nada disto: a regra é registrar, não mexer em segredo sozinho.

**21. `bussola/BUSSOLA.md` §3.0-b fixa um corte de 50% na linha 61 e nega ter fixado corte na 63.**
Linha 61: *"**Nicho em que a maioria das consultas paramétricas volta `—` não vira ilha**, por melhor que seja o índice"* — que é um
corte eliminatório em 50%. Linha 63: *"**Dois pontos não definem um corte numérico**, e por isso esta seção **não fixa um percentual
mínimo ainda**."* **O corte morde com os dois pontos que existem:** Robometria 18% com volume (82% `—`, reprovaria) e Aquametria 51%
(49% `—`, passaria raspando). Qual das duas frases vale é decisão de política — não conserto.

**22. O menu da Robometria: as duas pontas são inobedecíveis hoje.** `VOZ.md:31` e `DESIGN.md:40` mandam *"Peças · Modelos ·
Guias"*; `PROMPT.md:558` registra que o menu no ar é *"Peças · Sucção · Como conferimos"* e que os rótulos do `VOZ.md` *"só entram
quando as seções existirem como página"*. A §22.2 dá a vitória ao `VOZ.md` — e o rótulo "Guias" que ele exige aponta para
`/guias/`, que **não existe** (`PROMPT.md:569`). Obedecer ao contrato exigiria publicar endereço inventado; obedecer ao `PROMPT.md`
mantém a casca contra os dois donos da forma. Precisa de despacho, não de edição.

**23. Robometria: 95 − 28 ≠ 71, e nenhum arquivo diz qual número foi medido — NÃO VERIFICADO.** No mesmo bullet do
`ESTADO.md:110-113`: *"95 de 95 publicáveis rendem comissão (era **71** de 95)"* e *"o encurtamento das **28** chaves saiu (…) com os
**67** links que já estavam certos reaproveitados"*. 67 + 28 = 95 fecha; 95 − 24 = 71 fecha. Nenhum dos dois arquivos nomeia os 4 de
diferença, e o `PROMPT.md:149` repete o 71 como *"derivado do banco, não digitado"* — as duas contagens têm a mesma pretensão de
medida. As duas leituras são defensáveis; recontar é bloco.

**24. A regra das 48 h não pode ser obedecida por quem foi encarregado dela (classe 3).** `BUSSOLA.md:112` promete *"casca + 1
ferramenta + sitemap no ar em até 48h"* da aprovação. Mas `jornadafly/PROMPT.md:60` diz que *"a infraestrutura dos passos 2 a 8 da
seção 11 é trabalho de NAVEGADOR e está com o Raphael (…) não é sua"*, e o aviso de foco proíbe executar o arquivo. **22 dias depois
da aprovação de 14/09, as duas ilhas têm 0 URL e nenhum WordPress.** O prazo não é adiável por quem não tem as mãos; ou ele muda de
dono, ou muda de redação.

**25. A pendência P7 está fechada num arquivo e aberta em dois.** `ilhas/ohmetria/DESIGN.md:48` diz *"**fecha a pendência P7 da
rodada 004**"* (14/09); `bussola/fila.md:75` a carrega como dívida viva e `rodadas/005.md:16` a marca *"em aberto — segue para a
006"*. Para a outra ilha com dossiê a tarefa também caducou, porque a identidade veio pronta do Raphael. As duas leituras da ordem
dos fatos em 14/09 são defensáveis; o que não se sustenta é a `fila.md`, que se declara "ranking vivo", seguir cobrando o que o dono
dos tokens declara cumprido.

---

## BAIXO (4)

**26. `ohmetria/ESTADO.md` afirma o valor de dois campos que não existem, e o dono designado não pode chegar.** Faltam
`ultima_ronda` e `bloqueada_por` (confirmado hoje por parser; é a única das seis ilhas que falha o portão da §2), e a prosa da
linha 14 diz *"`bloqueada_por` segue null de proposito"*. Registrado como MÉDIO em 16/09, 21/09 e 28/09 — **19 dias**. Não
consertei porque o `PAINEL.md` nomeia o dono: *"é da próxima execução que reservar aquela ilha"*. **A observação que vale mais que o
defeito:** essa execução **estruturalmente não chega**, porque a ohmetria está fora do foco e ilha fora do foco não recebe bloco.
Dívida com dono impossível fica aberta para sempre.

**27. `rodadas/005.md:4` diz "seis das sete pendências da 004 estão fechadas"; a tabela logo abaixo marca duas abertas (P1, P7) — são cinco.**

**28. `rodadas/005.md:40` — "todo índice cai entre 0,20 e 0,35 ponto" falha em três linhas.** Recalculado: nobreak 3,80→3,63 =
**0,18**; coifa 3,79→3,61 = **0,18**; airfryer 2,96→2,86 = **0,10**. A ΔM é de fato constante (0,937), mas a harmônica amortece mais
quando o Retorno supera a Facilidade — exatamente esses três.

**29. `rodadas/004.md:41` anuncia "10 candidatos pontuados" e a 2.4 declara-se "não pontuado, verificação inacabada" — são 9.**

---

## HERDADOS — abertos, com o tempo na mesa (sem reabrir discussão)

| item | 1ª aparição | pendurado |
|---|---|---|
| Token do Sync em texto puro (hoje medido em **3** ilhas — ver achado 20) | 14/09 | **3 semanas** |
| E-mail pessoal da artesã em arquivo versionado — 29 linhas em 10 arquivos | 14/09 | **3 semanas** |
| `fila.md` sem critério de desempate: o 2º traz 3,92 e o 3º traz 3,94 | 14/09 | **3 semanas** |
| `fila.md`: "a melhor Facilidade da fila inteira (4,40)" é falso (som automotivo = **4,64**; pior Retorno é o drone, 1,73) · a coluna `#` salta de 16 para 18 · "Ilhas nascidas" lista 3 e são 5 | 14/09 e 21/09 | **3 e 2 semanas** |
| Altura do cabeçalho do Clube do Mosaico, 84 × ~96 — **resolvido hoje junto com o logo, achado 7** | 14/09 | fechado |
| `aquametria/ARVORE.md` atribui à 16.1 a permanência de `/metodologia/` na raiz; a 21.7 diz o oposto | 14/09 | **3 semanas** |
| Dossiê do som automotivo: "Os 40 candidatos" são **41** (estoura o teto de 30–40 do §5) e "sem DNS (38 de 40)" são 39 | 14/09 | **3 semanas** |
| Clube do Mosaico com dois desenhos de URL e dois eixos de categoria para a mesma camada | 21/09 | **2 semanas** |
| `jornadafly/DESIGN.md` proíbe (linha 34) e manda (linha 44) pintar "FLY" de azul | 21/09 | **2 semanas** |
| `despachos.md:193` afirma que "falta a variável" `GOOGLE_SA_B64` e o repositório prova que ela existe | 28/09 | **1 semana** |
| As **quatro** regras de processo propostas pelas quatro auditorias e nunca inseridas (10.x, 10.y, 8.z, 10.z) | 14/09 | **3 semanas** |

**Não verificados que ninguém verificou:** `lotus-512.png` com **9.095** bytes contra os 8.770 que três documentos declaram (e
`favicon-512.png`/`favicon-180.png` não existem na pasta); `aquametria/ARVORE.md:90`, *"falsa em 14 dos 36 registros"*; qual `sub_id`
os **58** links de `malha-pecas.json` carregam (a §25.8 proíbe o único caminho que diria).

**Observação de processo, e ela é a razão de o número 3 semanas se repetir:** a lista "Precisa do Raphael" do `PAINEL.md` de 02/10
tem 12 linhas e **não contém um único item desta tabela**. As pendências mais antigas do Pente Fino não estão no painel que ele lê.

---

## MEDIÇÃO DOS DADOS (classe 5) — contado, não presumido

230 registros nos 12 bancos primários. **141 (61,3%) sem `url_produto` utilizável** e **107 (46,5%) sem data de conferência** — mas
a leitura honesta exige separar três coisas que um grep cru junta:

- **Buraco com motivo declarado** é dívida administrada, não defeito: 13 pastilhas (`motivo_sem_ficha`), 40 de 43 peças e 30 de 35
  modelos da robometria (`motivo_sem_url_produto`).
- **Buraco silencioso, sem campo de motivo — 43 registros:** aquametria **31**, robometria **8**, clubedomosaico **4**.
- **Divergência de NOME entre ilhas, não ausência de dado:** a aquametria não tem `conferido_em`; ela usa
  `afiliado.piso_conferido_em` e `verificado_em`, preenchidos em **78 de 78**. Os "78 ausentes" são os mesmos 78 presentes com outro
  nome. **Se o par da aquametria satisfaz a 25.4 é decisão de regra — NÃO VERIFICADO aqui, e registrado como tal.**
- **Piso da 25.2 íntegro onde importa:** `url_busca` em 100% dos publicáveis de robometria (54 peças, 45 modelos) e aquametria (78).
- **Defeito de esquema, não de dado — `jornadafly/esquema-banco.json`:** ele **não declara** `url_busca`, `degrau` nem
  `conferido_em`. As 4 experiências conformam ao esquema da ilha e violam a 25.1/25.2/25.4 **por omissão do próprio esquema**. É
  bloco de dados da Fundação, não conserto de documento — registrado, não consertado.
- **Zero `degrau` fora da escada 1–4.** Armadilha para a próxima auditoria: `robometria/palavras-chave-medidas.json` usa uma escada
  **própria de 0 a 5**, declarada no arquivo. Quem a comparar com a 25.1 marca 22 registros como fora de domínio e **nenhum** está.
- **Nenhum número declarado dentro de JSON divergiu do contado**, nas 11 contagens conferíveis. `casca-fatos.json`
  `total_de_fontes: 141` não é recontável a partir do arquivo — **não verificado**.

---

## O PADRÃO

Os 19 consertos desta semana têm **uma** forma, e nenhum deles é erro de quem decidiu: a decisão estava certa e escrita com
cuidado. O que falhou foi sempre o **segundo passo** — varrer quem repetia a frase revogada. A decisão de 28/09 foi escrita num
parágrafo impecável e deixou quatro cópias de pé, uma delas na seção que as Sentinelas abrem para rondar.

E a prova de que o hábito não se resolve com boa intenção é o achado 3: **em 28/09 o próprio Pente Fino abriu os dois `PROMPT.md`,
consertou o nome da ilha em foco e escreveu "a conclusão deste aviso continua certa" sobre a frase que a decisão daquele mesmo dia
revogava.** O auditor cometeu, no mesmo commit, o defeito que ele existe para caçar. Isso desqualifica a vigilância como remédio:
quem corrige um ponto está olhando o ponto, e a cópia fica fora do campo de visão por construção, não por descuido.

Daí o que faltava e continua faltando: **a decisão não tem critério de pronto.** Ninguém mede o fechamento de uma decisão; mede-se o
parágrafo novo. Quatro auditorias propuseram quatro regras de processo e **uma** entrou no contrato (o portão das oito chaves, 30/09)
— e ela entrou justamente porque era um **comando**, não uma recomendação.

Proposta de texto para o `ARQUIPELAGO.md` — **NÃO inserido, porque regra nova de política é decisão do Raphael**:

> ### 10.w DECISÃO QUE REVOGA UMA FRASE SÓ ESTÁ FECHADA QUANDO A FRASE NÃO EXISTE MAIS EM LUGAR NENHUM
> Quem escreve no repositório uma decisão que revoga uma regra faz, **no mesmo commit**, três coisas, e a terceira é a que falta hoje:
> (1) escreve a decisão onde a regra morava; (2) roda `git grep` da **frase revogada** — não do assunto, da frase — e trata **cada**
> ocorrência, consertando ou colando ponteiro; (3) escreve na mensagem do commit **quantos arquivos a varredura achou e quantos
> tratou**. Decisão cujo commit não traz esses dois números não está fechada, está só anunciada. E a varredura é obrigatória mesmo
> para quem está apenas colando um ponteiro de auditoria: foi exatamente aí, em 28/09/2026, que o Pente Fino ratificou por escrito
> a metade de uma frase que a decisão do mesmo dia tinha cortado.
