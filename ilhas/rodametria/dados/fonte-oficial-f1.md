# A FONTE OFICIAL DA F1 — todas as portas tentadas, com data, e o lugar pronto para a leitura aterrissar

`publicar: false`. Arquivo de bancada: nenhuma linha daqui vai para a tela.

**Para que serve.** A F1 (*"esse elétrico precisa de CNH?"*) é a home desta ilha e a razão
pela qual ela nasceu. Ela está travada desde **28/10/2026** por **uma** coisa: os quatro
limiares legais da Resolução Contran nº 996/2023 não podem ser lidos no texto oficial desta
nuvem. Enquanto isso, a constante `limiares-categoria-contran-996-2023` de
`dados/constantes.json` fica `pendente` e a ferramenta não desembarca.

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
| `www.gov.br`, `gov.br` | o texto oficial, fonte primária | 28/10 10h4xZ · 28/10 13h2xZ · 29/10 11hxxZ · **05/11 19h1xZ** | `000`, `connect_rejected` (403 de política no CONNECT) |
| `in.gov.br` (Imprensa Nacional / DOU) | a publicação de 22/06/2023 | 28/10 · 29/10 · **05/11 19h1xZ** | `000`, mesma recusa |
| `www.planalto.gov.br` | compilação de atos | 28/10 · 29/10 · **05/11 19h1xZ** | `000`, mesma recusa |
| `www.contran.gov.br` | o órgão que editou | 28/10 · 29/10 | `000`, mesma recusa |
| `www.lex.com.br` | reprodução comercial do ato | 28/10 · 29/10 · **05/11 19h1xZ** | `000`, mesma recusa |
| **busca de página (`WebFetch`)** no `gov.br` | a outra porta da nuvem | 28/10 · **05/11 19h1xZ** | `getaddrinfo ENOTFOUND www.gov.br` — falha na resolução de nome, não no HTTP |
| **`araras.sp.gov.br`** — PDF da resolução | **porta NOVA, achada em 05/11** | **05/11 19h1xZ** | `000`, mesma recusa — é `.gov.br`, cai na mesma parede |
| **busca da nuvem (`WebSearch`)** | a única porta que ATRAVESSA | **05/11 19h1xZ** | **responde, e NÃO serve** — ver a seção 2 |

**O controle é o que torna isto medição e não palpite.** Nas mesmas passadas de 05/11 às
19h1xZ, `aquametria.com.br` respondeu **200** três vezes e `rodametria.com.br`,
`robometria.com.br` e `aquametria.com.br` responderam **200** na passada da porta de entrada.
São **4 controles verdes** contra **6 recusas**, com o egresso nomeando a causa em cada uma:
`gateway answered 403 to CONNECT (policy denial or upstream failure)`. **Recusa de política,
não queda de host** — e por isso repetir não muda nada, como a 20.2 prevê.

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

**GESTO A — uma linha na lista de "Domínios permitidos"** dos ambientes de nuvem
(`claude.ai/code` → seletor de ambiente → Nuvem → engrenagem):

```
*.gov.br
```

**Por que o curinga e não os dois nomes do despacho original:** esta passada mediu que a parede
é o **domínio**, não os hosts. `*.gov.br` fecha, de uma vez:

- o **despacho ALTA de 28/10** (`www.gov.br`, `gov.br`, `in.gov.br`, `planalto.gov.br`,
  `contran.gov.br`) — a fonte primária da F1;
- o **despacho NORMAL da camada municipal** (`campinas.sp.gov.br`, `rio.rj.gov.br`,
  `joinville.sc.gov.br`, `sjc.sp.gov.br`), que já pedia o curinga — a camada 2 da F1, que hoje
  tem duas saídas iguais em vez de três;
- a porta **nova** desta passada, o PDF da resolução em `araras.sp.gov.br`, que ninguém havia
  contado porque ninguém sabia que existia.

`lex.com.br` fica de fora do curinga e **não faz falta**: é reprodução comercial, e com o
`.gov.br` aberto a fonte primária está na mão.

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
> "dispensa CNH" e "exige habilitação" em todo texto de tela enquanto ela for pendente.
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

**A PAREDE, e ela é a mesma de sempre:** `www.planalto.gov.br` é um dos cinco domínios medidos em 403
de CONNECT em 28/10, 29/10 e 05/11/2026, e em 05/11 a parede foi medida como sendo o **domínio
`.gov.br` inteiro**, não os hosts. O pedido que destrava esta seção é o **mesmo** de uma linha
(`*.gov.br`) do despacho ALTA de `dados/despachos.md`. A tabela de todas as portas tentadas está na
seção 2 deste arquivo.

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
