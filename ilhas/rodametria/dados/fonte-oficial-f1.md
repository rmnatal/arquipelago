# A FONTE OFICIAL DA F1 — todas as portas tentadas, com data, e o lugar pronto para a leitura aterrissar

`publicar: false`. Arquivo de bancada: nenhuma linha daqui vai para a tela.

**Para que serve.** A F1 (*"esse elétrico precisa de CNH?"*) é a home desta ilha e a razão
pela qual ela nasceu.

> **ESTE PARÁGRAFO ESTAVA VENCIDO E FOI REESCRITO EM 25/11/2026, E ELE CONTRADIZIA A PRÓPRIA
> SEÇÃO 5 DESTE ARQUIVO.** Ele dizia: *"Ela está travada desde 28/10/2026 por uma coisa: os quatro
> limiares legais da Resolução Contran nº 996/2023 não podem ser lidos no texto oficial desta
> nuvem. Enquanto isso, a constante `limiares-categoria-contran-996-2023` de
> `dados/constantes.json` fica `pendente` e a ferramenta não desembarca."* A **seção 5** abaixo, no
> mesmo arquivo, escreve com todas as letras que a leitura foi feita pelo Raphael em **05/11/2026**
> e que **a F1 foi ao ar na revisão 46 em 06/11/2026** — e é a seção 5 que está certa. **A frase
> ficou de pé 19 dias**, no arquivo cuja razão de existir é ser lido pela próxima passada **para ela
> não remedir porta já medida**: lida ao pé da letra, ela mandava a próxima execução tratar como
> travado o que está no ar. Achada em 25/11/2026 pela mesma varredura que achou os três
> `limiares-categoria-contran-996-2023` mortos em `veiculos.json` e em `esquema-banco.json`.

**O ESTADO DE HOJE, 25/11/2026, e cada metade com o seu dono.** Dos limiares para baixo a F1 está
**no ar e completa**: a constante dos limiares (`limiares-categoria-contran-996-2023`, hoje
`publicavel`) classifica as três categorias da resolução, com os artigos lidos no PDF oficial.
O que **segue atrás da parede de egresso** são outras duas coisas, e nenhuma delas é o limiar:

- **a habilitação (CNH)**, porque a resolução **não fala de CNH** — quem decide é o Código de
  Trânsito, e a constante `exigencia-de-habilitacao-por-categoria-ctb` (seção 6 deste arquivo)
  nasceu `pendente` por isso. A F1 **cala** sobre CNH e nomeia a causa na tela, em vez de não
  existir;
- **a camada municipal**, porque os quatro atos de prefeitura exigem leitura no `.gov.br` do
  município e os quatro domínios respondem `000` do egresso.

A tabela de portas abaixo continua valendo para essas duas, e é por isso que ela não se apaga.

Este arquivo existe por dois motivos, e os dois são para baratear a próxima passada:

1. **Nenhuma execução remede uma porta já medida.** A tabela abaixo diz qual porta foi
   tentada, quando, e o que ela respondeu. Porta com data é porta que não se tenta de novo
   por hábito — e a 20.2 continua mandando retestar bloqueio **herdado**, que é diferente de
   retestar o que esta passada mediu.
2. **A leitura tem um lugar pronto para aterrissar.** A seção final tem os campos rotulados,
   um por um. Quem tiver o texto oficial na frente preenche os campos e a constante vira
   `publicavel` **editando um objeto JSON** — nenhuma linha de lógica muda, porque a 1.3 da
   especificação proibiu literal numérico no código.

---

## 1. AS PORTAS, UMA POR UMA

| porta | o que é | medido em | resposta |
|---|---|---|---|
| `www.gov.br`, `gov.br` | o texto oficial, fonte primária | 28/10 10h4xZ · 28/10 13h2xZ · 29/10 11hxxZ · 05/11 19h1xZ · 13/11 13h3xZ · **24/11 10h2xZ** | `000`, `connect_rejected` (403 de política no CONNECT) |
| `in.gov.br` (Imprensa Nacional / DOU) | a publicação de 22/06/2023 | 28/10 · 29/10 · 05/11 19h1xZ · 13/11 · **24/11 10h2xZ** | `000`, mesma recusa |
| `www.planalto.gov.br` | compilação de atos | 28/10 · 29/10 · 05/11 19h1xZ · 13/11 · **24/11 10h2xZ** | `000`, mesma recusa |
| `www.contran.gov.br` | o órgão que editou | 28/10 · 29/10 · 13/11 · **24/11 10h2xZ** | `000`, mesma recusa |
| `www.lex.com.br` | reprodução comercial do ato | 28/10 · 29/10 · 05/11 19h1xZ · 13/11 · **24/11 10h2xZ** | `000`, mesma recusa |
| **busca de página (`WebFetch`)** no `gov.br` | a outra porta da nuvem | 28/10 · **05/11 19h1xZ** | `getaddrinfo ENOTFOUND www.gov.br` — falha na resolução de nome, não no HTTP |
| **`araras.sp.gov.br`** — PDF da resolução | **porta NOVA, achada em 05/11** | **05/11 19h1xZ** | `000`, mesma recusa — é `.gov.br`, cai na mesma parede |
| **busca da nuvem (`WebSearch`)** | a única porta que ATRAVESSA | **05/11 19h1xZ** | **responde, e NÃO serve** — ver a seção 2 |
| **`www2.camara.leg.br`** — o CTB na Câmara dos Deputados | **porta NOVA, tentada pela PRIMEIRA vez em 16/11** | **16/11 13h2xZ** | `000`, `connect_rejected`, **403 no CONNECT lido com `curl -v`** |
| **`legis.senado.leg.br`** — o CTB no Senado | **porta NOVA, tentada pela PRIMEIRA vez em 16/11** | **16/11 13h2xZ** | `000`, mesma recusa |
| **`normas.leg.br`** (LexML/LEG) | **porta NOVA, tentada pela PRIMEIRA vez em 16/11** | **16/11 13h2xZ** | `000`, mesma recusa |
| **leitor de página (`WebFetch`) no `www2.camara.leg.br`** | a outra porta da nuvem, no `.leg.br` | **16/11 13h2xZ** | `getaddrinfo ENOTFOUND www2.camara.leg.br` — **a mesma assinatura que o `www.gov.br`** |
| **o NAVEGADOR desta nuvem (Chromium do Playwright)** no `planalto.gov.br`, `gov.br/transportes` e `lex.com.br` | **porta NOVA, tentada pela PRIMEIRA vez em 24/11** — em 27 dias de despacho aberto a parede só havia sido medida por `curl` e por `WebFetch` | **24/11 10h2xZ** | **`net::ERR_TUNNEL_CONNECTION_FAILED`** nos três, com `rodametria.com.br` em **HTTP 200** e `<title>` de verdade na MESMA passada e no MESMO navegador — é o egresso e não o site, logo **não falta sessão nem há anti-robô a contornar** (a regra geral está na **33**) |
| **`www.mdpi.com`** — agregador acadêmico aberto | **porta NOVA, tentada pela PRIMEIRA vez em 18/11**, como canal alternativo para o estudo de patinete da F2 | **18/11 19h2xZ** | `000`, `connect_rejected` lido no status |
| **`doaj.org`** — diretório de periódicos abertos | **porta NOVA, tentada pela PRIMEIRA vez em 18/11**, mesmo alvo | **18/11 19h2xZ** | `000`, `connect_rejected` lido no status |
| `stdjet.scienceandtechnology.com.vn`, `et.vnuhcmjournal.com.vn` | os dois periódicos que publicam o consumo por km de PATINETE (constante da F2) | 28/10 · 29/10 · **18/11 19h2xZ** | `000` nas três passadas de hoje, `connect_rejected` lido no status |

> **REMEDIDO EM 18/11/2026 às 19h2xZ, E A PAREDE É A MESMA — com DUAS portas novas e as DUAS fechadas.**
> A passada que mediu isto encontrou a **fila de blocos da ilha acabada** e foi medir, em vez de supor, por que
> nenhum eixo anda. **20 portas, 3 passadas cada: 60 medições de recusa e 20 controles em 200** em
> `rodametria.com.br`, na mesma passada, zero intermitência. Dezenove em `000`; só
> `www.mercadolivre.com.br` respondeu — **403 nas três**, que é o anti-robô da loja com o CONNECT passando.
>
> **O que é NOVO e vale a linha:** `www.mdpi.com` e `doaj.org` foram tentados pela primeira vez como canal
> alternativo para a medição de patinete da F2 — a ideia era que um agregador acadêmico aberto pudesse
> servir o que os dois periódicos vietnamitas servem. **Os dois estão fechados pela mesma parede**, e por
> isso continuam **fora** do pedido: o alvo não é um agregador, são os dois periódicos nomeados, e pedido
> curto é pedido que acontece. **Estão aqui para nenhuma execução os remedir por hábito**, que é a razão de
> ser desta seção.
>
> **E a honestidade do instrumento vai dita, porque ele é uma JANELA:** o `__agentproxy/status` guarda as
> últimas entradas, e quando foi lido só **7** dos 20 hosts ainda estavam nela. Os outros 13 estão
> classificados pela assinatura idêntica mais as leituras datadas desta tabela — **não por uma leitura de
> status que não existe**. É a família da 20.4: janela que rolou não aprova com cara de completo.
>
> **O pedido inteiro passou a existir numa lista só**, em `dados/despachos.md`, no topo dos ABERTOS: as seis
> fatias que seis despachos pediam separadas, reunidas, porque montar a lista era o trabalho que não estava
> sendo feito. Nenhum dos seis foi fechado.

**O controle é o que torna isto medição e não palpite.** Nas mesmas passadas de 05/11 às
19h1xZ, `aquametria.com.br` respondeu **200** três vezes e `rodametria.com.br`,
`robometria.com.br` e `aquametria.com.br` responderam **200** na passada da porta de entrada.
São **4 controles verdes** contra **6 recusas**, com o egresso nomeando a causa em cada uma:
`gateway answered 403 to CONNECT (policy denial or upstream failure)`. **Recusa de política,
não queda de host** — e por isso repetir não muda nada, como a 20.2 prevê.

> **CORREÇÃO MEDIDA EM 16/11/2026 às 13h2xZ, E ELA É DO DIAGNÓSTICO E NÃO DO FATO — A PAREDE NÃO É
> O `.gov.br`: É A LISTA DE PERMITIDOS, E O `.leg.br` CAI COM ELA.** O parágrafo abaixo é de 05/11 e
> conclui, das seis recusas daquele dia, que *"o que esta ilha não alcança não é um site, é o domínio
> `.gov.br` inteiro"*. **A conclusão é mais estreita que a parede, e lida ao pé da letra ela promete
> uma porta que não existe:** quem a ler acredita que uma reprodução oficial fora do `.gov.br` é
> alcançável — e o CTB tem exatamente isso, na custódia de quem o promulgou.
>
> **MEDIDO HOJE, três passadas cada, com dois controles verdes nas MESMAS três passadas:**
> `www2.camara.leg.br`, `legis.senado.leg.br` e `normas.leg.br` devolveram **`000` nas três** — 9
> medições de recusa —, com `rodametria.com.br` e `aquametria.com.br` em **200 nas mesmas três** (6
> controles verdes, zero intermitência). `www.planalto.gov.br` foi medido na mesma passada como
> controle da parede conhecida e deu **`000`**. A classificação foi **lida** no
> `__agentproxy/status` e não suposta — `connect_rejected`, *"gateway answered 403 to CONNECT
> (policy denial or other refusal)"*, `host: www2.camara.leg.br:443` —, e o **403 no CONNECT** foi
> lido direto no `curl -v`. O leitor de página devolveu `getaddrinfo ENOTFOUND www2.camara.leg.br`,
> **a mesma assinatura que a seção 1 registra para o `www.gov.br`**: fora da lista, um domínio que
> existe não se distingue de um que não existe.
>
> **O QUE ISTO MUDA, e é o motivo de a correção valer uma passada:** a parede é a **lista de
> permitidos** da seção 20.1, e `.gov.br` era só o primeiro domínio a bater nela. O `*.gov.br` do
> GESTO A **continua certo e continua necessário** — é por ele que vêm a resolução, o CTB compilado
> no `planalto` e os quatro folhetos municipais. O que ele **não** faz é abrir a via da Câmara e do
> Senado, que é a via da **publicação original** do CTB contra a **compilação** do `planalto`, e por
> isso o pedido ganhou uma segunda linha na seção 4. **É a seção 4 do contrato acontecendo dentro de
> um arquivo de bancada:** o diagnóstico ficou para trás em silêncio e cada execução o leu como
> fato, que é a mesma doença que a própria seção 20 corrigiu em 11/09 — *"era intermitência do túnel
> lida como bloqueio, e o diagnóstico se propagou porque cada execução leu o `ESTADO.md` da anterior
> como fato"*.

**O que esta passada acrescentou à parede, e é o achado de maior alcance:** o que esta ilha
não alcança **não é um site, é o domínio `.gov.br` inteiro**. O PDF da resolução hospedado num
município (`araras.sp.gov.br`) é um host completamente diferente dos cinco federais e **cai na
mesma recusa**. Isso une este despacho ao despacho NORMAL da camada municipal — que já pedia
`*.gov.br` — e o pedido dos dois passa a ser **uma linha só**. Ver a seção 4.

---

## 2. A PORTA DA BUSCA ATRAVESSA, E MEDIMOS POR QUE ELA NÃO SERVE

A busca da nuvem roda **fora** do egresso deste contêiner, então ela alcança o que o `curl` não
alcança. Foi tentada em 05/11 às 19h1xZ, duas consultas, e **devolveu texto que se apresenta
como citação do DOU de 22/06/2023**. Mesmo assim ela **não pode ser a fonte de registro desta
constante**, e a razão é medida, não purista:

1. **Ela própria se recusou a confirmar uma das três definições.** Nas duas consultas, o
   ciclomotor voltou com o trecho **cortado antes dos limites**, e a busca disse com todas as
   letras que não conseguiu confirmar os números no texto oficial. **Três definições são
   pedidas; duas voltaram.**
2. **O único número que ela ofereceu para o ciclomotor é exatamente o número contaminado.**
   Ela trouxe *"até 4.000 W e 50 km/h"* a partir de sites secundários — e **4.000 W é o número
   que esta ilha já mediu como o lado errado de uma contradição dentro de um único
   publicador**: a `eletricz.com.br` afirma 1.000 W numa página e 4.000 W noutra, citando a
   mesma resolução (medido no bloco 6, em 02/11). **A busca reproduz a contradição que esta
   ilha diagnosticou; ela não a desfaz.**
3. **Ela mistura primária com comercial no mesmo parágrafo, sem separar.** O que volta é um
   resumo em que a citação do DOU e a prosa de loja chegam coladas. Para **toda** outra
   constante desta ilha isso seria aproveitável com rótulo de segunda mão; para **esta**, não:
   o `PROMPT.md` exige o texto oficial *"com data"*, e o "Específico desta ilha" diz por quê —
   **errar "dispensa CNH" num veículo que é ciclomotor manda a pessoa para a rua sem
   habilitação.**

**A conclusão, dita para fechar a pergunta em vez de deixá-la implícita:** a porta da busca
está **medida e descartada como fonte de registro**, e descartada **com motivo**, não por
regra de estilo. A próxima execução não precisa tentá-la de novo esperando outro resultado.
O que ela serve é para o que já serviu aqui: **achar portas** (foi ela que achou o PDF do
município) e **medir o estado do mercado**, que é segunda mão declarada.

---

## 3. A PREMISSA DA "FASE NOVA DE VIGÊNCIA" FOI CONFERIDA, E ELA PARECE SER OUTRA COISA

O despacho de 28/10 e o campo `fonte_exigida` da constante dizem que a resolução *"ganhou
**fase nova de vigência** em 1º/01/2026"*, colhido em `canalve.com.br` e
`paraibabusiness.com.br` — segunda mão, e os dois arquivos dizem isso de si mesmos. **Essa
frase foi lida como "existe um texto novo para ler", e isso encarece o pedido**: manda procurar
uma redação alterada antes de ler a original.

**Conferido em 05/11/2026 às 19h1xZ, por busca dirigida a alteração e revogação:** não apareceu
**nenhuma** alteração nem revogação da 996/2023. O que apareceu foi outra leitura da mesma
data: a resolução **entrou em vigor em 03/07/2023**, o **prazo de adequação** terminou em
**31/12/2025**, e **1º/01/2026 é o dia em que ela passou a valer integralmente** — mesmo texto,
fim de carência, não redação nova.

**E o tamanho honesto deste achado, porque ele é menor do que parece.** É um achado
**negativo** ("não encontrei alteração") colhido na **mesma** camada de segunda mão que gerou a
frase que ele corrige, numa **única** rodada de busca. Ele **não** é prova de que não houve
alteração, e **não** vira constante. O que ele faz é mudar o **pedido**: quem for ler o texto
oficial lê **a 996/2023 como publicada em 22/06/2023** e, na mesma sessão, confere no portal se
há ato posterior — em vez de sair atrás de uma "fase nova" que, pelo que se mediu, talvez não
exista como texto. **Enquanto a leitura oficial não chegar, o campo `fonte_exigida` continua
pedindo que a leitura diga QUAL fase está lendo**, porque pedir isso é barato e desfazer um erro
de fase depois é caro.

---

## 4. O PEDIDO, E ELE VIROU UMA LINHA

Os dois gestos do despacho ALTA de 28/10 continuam valendo e **qualquer um dos dois destrava**.
O que mudou em 05/11 é que o primeiro ficou **mais barato e mais abrangente**:

**GESTO A — DUAS linhas na lista de "Domínios permitidos"** dos ambientes de nuvem
(`claude.ai/code` → seletor de ambiente → Nuvem → engrenagem):

```
*.gov.br
*.leg.br
```

> **A SEGUNDA LINHA NASCEU EM 16/11/2026, MEDIDA, e até hoje este gesto pedia só a primeira.** O
> `*.gov.br` traz a resolução, o CTB **compilado** no `planalto` e os quatro folhetos municipais. O
> `*.leg.br` traz o CTB na custódia de **quem o promulgou** — `www2.camara.leg.br` (publicação
> original de 23/09/1997) e `legis.senado.leg.br` —, e os três hosts `.leg.br` foram medidos hoje em
> **`000` nas três passadas**, com `connect_rejected` lido no status do proxy. **Por que as duas e
> não só a primeira:** o que o `planalto` serve é texto **compilado**, e a seção 5 deste arquivo já
> pagou o preço de não saber qual redação estava lendo — o campo *"qual fase/redação está sendo
> lida"* existe por isso. Ter a publicação original ao lado da compilação é a diferença entre ler o
> CTB e ler **uma** versão dele. Pedir as duas custa o mesmo gesto; descobrir depois que faltava uma
> custa a passada de quem for ler.

**Por que o curinga e não os dois nomes do despacho original:** a passada de 05/11 mediu que a
parede não eram os hosts. `*.gov.br` fecha, de uma vez:

- o **despacho ALTA de 28/10** (`www.gov.br`, `gov.br`, `in.gov.br`, `planalto.gov.br`,
  `contran.gov.br`) — a fonte primária da F1;
- o **despacho NORMAL da camada municipal** (`campinas.sp.gov.br`, `rio.rj.gov.br`,
  `joinville.sc.gov.br`, `sjc.sp.gov.br`), que já pedia o curinga — a camada 2 da F1, que hoje
  tem duas saídas iguais em vez de três;
- a porta **nova** desta passada, o PDF da resolução em `araras.sp.gov.br`, que ninguém havia
  contado porque ninguém sabia que existia.

`lex.com.br` fica de fora dos dois curingas e **não faz falta**: é reprodução comercial, e com o
`.gov.br` e o `.leg.br` abertos a fonte primária está na mão — em duas custódias independentes,
que é o que permite conferir uma contra a outra em vez de confiar numa só.

**GESTO B — dois minutos de navegador, e vale a passada do mesmo jeito se o A demorar.** Abrir o
texto oficial da **Resolução Contran nº 996, de 15/06/2023** e preencher a seção 5 abaixo. Os
campos estão rotulados um por um justamente para isto: não é preciso saber como a ilha guarda a
constante, só copiar número por número.

---

## 5. O LUGAR DA LEITURA — PREENCHIDA EM 05/11/2026, E JÁ COPIADA PARA A CONSTANTE

> **ESTA SEÇÃO FOI CUMPRIDA E CONSUMIDA.** Preenchida pelo Raphael em **05/11/2026, ~23h3x de
> Brasília**, com o PDF oficial do Ministério dos Transportes aberto no Chrome dele. Em
> **06/11/2026 às ~10h3xZ** a execução seguinte da Fundação copiou os valores para a constante
> `limiares-categoria-contran-996-2023` de `dados/constantes.json` (`tipo: oficial`, `status:
> publicavel`, com `url`, `verificado_em` e os artigos lidos), e **a F1 foi ao ar na revisão 46 — ela
> é a home da ilha.** Nenhuma linha de lógica mudou, exatamente como a 1.3 da especificação prometia.
>
> **O QUE A LEITURA MUDOU NA ESPECIFICAÇÃO está escrito como ERRATA dentro da seção 1 de
> `dados/especificacao-calculadoras.md`** — três coisas, e a mais importante é que **a resolução não
> fala de CNH**. Veja a seção 6 abaixo, que é o lugar pronto para essa outra leitura.
>
> **O texto do preenchimento fica abaixo, intacto, porque ele é a procedência.** Não o apague: é
> contra ele que qualquer releitura futura se compara, e é dele que a `url` e o `verificado_em` da
> constante saíram.

## 5. O LUGAR DA LEITURA — preencher e nada mais

> **Quem preencher esta seção destrava a F1.** Depois de preenchida, a execução seguinte copia
> os valores para `dados/constantes.json` (constante `limiares-categoria-contran-996-2023`),
> troca `status` e `tipo` para `publicavel`, e a F1 passa a poder ir ao ar. **Nenhuma linha de
> lógica muda.**
>
> **Se um campo não estiver no texto, escreva `NÃO CONSTA` em vez de deixar em branco ou
> estimar.** Campo vazio não se distingue de campo esquecido, e número estimado aqui é
> exatamente o defeito que este arquivo existe para impedir.

```
URL lida: https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucoes/Resolucao9962023.pdf/@@download/file
  (PDF oficial do Ministério dos Transportes, "Criado em 22/06/2023 11:36", 118.177 bytes, servido em 200 application/pdf no Chrome do Raphael)
data da leitura: 2026-11-05, ~23h3x de Brasília (2026-11-06 ~02h3xZ)
qual fase/redação está sendo lida (e se há ato posterior à 996/2023):
  Texto ORIGINAL: Resolução CONTRAN nº 996, de 15/06/2023, DOU de 22/06/2023 (Ed. 117, Seção 1, p. 327).
  Vigência pelo art. 22: 3 de julho de 2023. Prazo do art. 14 §1º I (RENAVAM de ciclomotor sem CAT):
  1º/11/2023 a 31/12/2025 — confirma que 1º/01/2026 é FIM DE PRAZO e não redação nova.
  Ato posterior: NÃO CONFERIDO no portal nesta leitura (a busca de 05/11 19h1xZ não achou alteração).
COMO FOI LIDO (declarado, para a próxima execução pesar): o PDF foi aberto pelo leitor de página
  (WebFetch) da sessão do chat de 05/11, não por pdftotext. Os números abaixo vêm entre aspas quando o
  leitor os devolveu literais; os do ciclomotor vieram parafraseados pelo leitor, com os números.
  A "frase inteira" das definições NÃO foi transcrita (o leitor limita citação longa) — só as alíneas.
artigo(s) e/ou anexo de onde cada número abaixo saiu: art. 2º, incisos II (autopropelido), III (bicicleta
  elétrica) e IV (ciclomotor); §§ 4º, 5º, 6º e 7º do art. 2º; arts. 12, 13, 14, 19, 21 e 22.

--- BICICLETA ELÉTRICA ---
definição literal (copiar a frase inteira): NÃO TRANSCRITA INTEIRA. Alíneas do inciso III do art. 2º:
  a) motor auxiliar "até 1000 W (mil watts)", duas rodas; b) "provido de sistema que garanta o
  funcionamento do motor somente quando o condutor pedalar"; c) "não dispor de acelerador";
  d) velocidade do motor auxiliar "não superior a 32 km/h"
potência nominal máxima (W): 1000
velocidade máxima do motor auxiliar (km/h): 32
tem acelerador, ou só pedal assistido: SÓ PEDAL ASSISTIDO (alínea c proíbe acelerador). § 4º permite modo
  de assistência a pé, sem pedalar, até 6 km/h.

--- EQUIPAMENTO DE MOBILIDADE INDIVIDUAL AUTOPROPELIDO ---
definição literal (copiar a frase inteira): NÃO TRANSCRITA INTEIRA. Alíneas do inciso II do art. 2º:
  c) "provido de motor de propulsão com potência nominal máxima de até 1000 W (mil watts)";
  d) "velocidade máxima de fabricação não superior a 32 km/h (trinta e dois quilômetros por hora)";
  e) "largura não superior a 70 cm (setenta centímetros) e distância entre eixos de até 130 cm"
potência nominal máxima (W): 1000
velocidade máxima de fabricação (km/h): 32
largura máxima: 70 cm (700 mm)
distância entre eixos máxima: 130 cm (1300 mm)
  (§ 5º trata de passageiro em autopropelido "que se assemelha a bicicleta com acelerador" — a bike COM
  acelerador cai em autopropelido, não em bicicleta elétrica)

--- CICLOMOTOR ---
definição literal (copiar a frase inteira): NÃO TRANSCRITA. Inciso IV do art. 2º, sem alíneas, parafraseado
  pelo leitor: veículo de 2 ou 3 rodas, motor a combustão até 50 cm³ ou elétrico até 4 kW, velocidade
  máxima de fabricação 50 km/h.
potência máxima (W), se o texto declarar: 4000 (4 kW, motor elétrico)
cilindrada máxima, se o texto declarar: 50 cm³ (combustão)
velocidade máxima (km/h), se o texto declarar: 50
  >>> A CONTRADIÇÃO DO BLOCO 6 SE DESFAZ: 1.000 W é o teto de AUTOPROPELIDO e de BICICLETA ELÉTRICA;
  4.000 W é o teto de CICLOMOTOR. Os dois números são da mesma resolução, para categorias diferentes.

--- A REGRA DE TRANSBORDO ---
o que o texto diz que acontece quando o equipamento passa dos limites do autopropelido: §§ 6º e 7º do
  art. 2º — passa a ser classificado como "ciclomotor, motocicleta, motoneta ou triciclo, conforme o caso."

--- EXIGÊNCIAS, se o texto as declarar ---
habilitação exigida por categoria: NÃO CONSTA na 996/2023 (nenhum artigo sobre CNH/ACC; vem do CTB)
registro/placa exigido por categoria: art. 12 — autopropelido e bicicleta elétrica "não são sujeitos ao
  registro, ao licenciamento e ao emplacamento para circulação nas vias"; art. 13 — ciclomotor É
  registrado e licenciado (CAT + nota fiscal); art. 19 III e IV — sanção por falta de placa/registro.
capacete exigido por categoria: só CICLOMOTOR (art. 19 V, remete ao art. 244 do CTB); NÃO CONSTA para
  bicicleta elétrica e autopropelido
idade mínima por categoria: NÃO CONSTA na 996/2023
```

---

## 6. O QUE NÃO ESTÁ TRAVADO POR ISTO

Dito para ninguém parar a ilha errada. **Não** dependem desta leitura: a árvore de decisão da
F1 (escrita, com os limiares referenciados **por nome**), as duas ressalvas da 1.4, a camada
municipal, o bloco de compra, a prestação de contas da seção 7, o bloco 3 inteiro, o esquema do
banco, a F2 (no ar desde 29/10) e a F3. **E a ilha não recebe `bloqueada_por` por causa disto**
(seção 11, passo 4): o que travou é uma **fonte**, não a ilha.

O portão da F1, quando nascer, usa limiar **fictício** declarado como fictício no próprio caso
(ex. `LIMIAR_AUTOPROP_W = 777`) e afirma a **árvore**, nunca os números do mundo. Portão que
afirma 1.000 W antes de o texto oficial chegar é o número de tela digitado com outra roupa.

---

## 6. O LUGAR DA PRÓXIMA LEITURA — O CTB, E A F1 ESTÁ NO AR SEM ELE

> **POR QUE ESTA SEÇÃO EXISTE, e ela nasceu da leitura da seção 5 e não de um palpite:** a Resolução
> Contran nº 996/2023 **não tem artigo nenhum sobre habilitação**. Isso está medido no próprio
> preenchimento acima — *"habilitação exigida por categoria: NÃO CONSTA na 996/2023 (nenhum artigo
> sobre CNH/ACC; vem do CTB)"*. Ela decide a **categoria** e decide **registro, licenciamento e
> emplacamento** (arts. 12 e 13) e **capacete** (art. 19 V).
>
> **A consequência é dura e está no ar:** a F1 responde a categoria, responde a placa com o artigo, e
> **cala sobre CNH**, com uma frase própria dizendo que a resolução não decide isso e que a gente não
> leu o Código de Trânsito na fonte. A constante `exigencia-de-habilitacao-por-categoria-ctb` nasceu
> `pendente` para esse silêncio ter nome, e o portão `ferramentas/teste-f1.py` **proíbe** as frases
> "dispensa CNH" e "exige habilitação" em todo texto de tela. **AS DUAS NÃO TÊM O MESMO REGIME, e
> isso foi separado em 25/11/2026 — até aquela data esta linha terminava em "enquanto ela for
> pendente", e era essa condição que desligava a trava sozinha no dia em que esta seção fosse
> preenchida:** "dispensa CNH" (e "dispensa habilitação") é proibida **sempre**, porque é afirmação
> permissiva e categórica e o CTB não exime por veículo; "exige habilitação" é proibida **só**
> enquanto a constante for `pendente`, e no dia em que ela virar `publicavel` o portão **troca de
> cobrança** — passa a exigir `url`, `verificado_em` e `tipo: oficial` da constante — em vez de
> parar de olhar. Quem preencher esta seção vai ver o portão reprovar por procedência até os três
> campos estarem escritos, e isso é o desenho.
>
> **Quem preencher esta seção faz a F1 responder a pergunta do título dela.** Depois de preenchida, a
> execução seguinte copia os valores para a constante, troca `status` e `tipo` para `publicavel`, e a
> ferramenta passa a responder CNH **sem uma linha de lógica mudar** — é o mesmo mecanismo que
> destravou o limiar em 06/11/2026, e ele já foi exercitado uma vez.
>
> **Se um campo não estiver no texto, escreva `NÃO CONSTA`** em vez de deixar em branco ou estimar.
> Campo vazio não se distingue de campo esquecido, e número estimado aqui é exatamente o defeito que
> este arquivo existe para impedir. **E a direção do erro importa mais aqui do que em qualquer outro
> campo desta ilha:** dizer que dispensa habilitação quem precisa dela manda alguém para a rua sem o
> documento.

**A PAREDE, E ELA FICOU MAIOR DO QUE SE PENSAVA — REMEDIDA EM 16/11/2026 às 13h2xZ pela 20.3.**
`www.planalto.gov.br` é um dos cinco domínios medidos em 403 de CONNECT em 28/10, 29/10 e 05/11/2026,
e em 05/11 a parede foi **diagnosticada** como sendo o domínio `.gov.br` inteiro. **Esse diagnóstico
está corrigido na seção 1:** a parede é a **lista de permitidos** (20.1), e o `.leg.br` cai com ela.

**O QUE ISTO FAZ COM ESTA SEÇÃO, e é a razão de a remedição ter valido a passada.** O CTB **não é**
uma resolução de órgão: é a **Lei 9.503/1997**, e lei tem reprodução oficial fora do Executivo — a
**Câmara dos Deputados** e o **Senado** guardam o texto de quem o promulgou. Era a via que esta
tabela nunca havia contado, e era a candidata natural a furar uma parede de `.gov.br`. **Foi tentada
hoje, pela primeira vez, e está fechada:** `www2.camara.leg.br`, `legis.senado.leg.br` e
`normas.leg.br` em `000` nas três passadas, com dois controles em 200 nas mesmas três, e o leitor de
página devolvendo `ENOTFOUND` — a mesma assinatura do `www.gov.br`.

**Então esta seção não tem porta aberta nenhuma, e isso agora está medido em vez de suposto.** O
pedido que a destrava são as **duas** linhas da seção 4 (`*.gov.br` e `*.leg.br`) do despacho ALTA de
`dados/despachos.md` — a segunda nasceu desta medição. A tabela de todas as portas tentadas, com
data, está na seção 1 deste arquivo; **nenhuma execução precisa remedir o `.leg.br` por hábito**, e a
20.2 continua mandando retestar bloqueio **herdado**, que é outra coisa.

```
URL lida:
data da leitura:
qual redação está sendo lida (e se há ato posterior alterando os artigos de habilitação):
COMO FOI LIDO (declarado, para a próxima execução pesar — leitor de página, PDF, texto consolidado):
artigo(s) de onde cada linha abaixo saiu:

--- BICICLETA ELÉTRICA ---
exige habilitação (sim / não / NÃO CONSTA), com o artigo:
idade mínima, se o texto declarar:

--- EQUIPAMENTO DE MOBILIDADE INDIVIDUAL AUTOPROPELIDO ---
exige habilitação (sim / não / NÃO CONSTA), com o artigo:
idade mínima, se o texto declarar:

--- CICLOMOTOR ---
exige habilitação (sim / não / NÃO CONSTA), com o artigo:
qual categoria ou autorização (ACC, categoria A, outra), com o artigo:
idade mínima, se o texto declarar:

--- MOTOCICLETA, MOTONETA E TRICICLO (o que a 996/2023 chama de "acima do ciclomotor") ---
exige habilitação (sim / não / NÃO CONSTA), com o artigo:
qual categoria, com o artigo:

--- A DEFINIÇÃO QUE AMARRA TUDO ---
como o CTB define "veículo automotor", literal, com o artigo (é ela que decide se autopropelido e
bicicleta elétrica estão dentro ou fora da exigência de habilitação):
```
