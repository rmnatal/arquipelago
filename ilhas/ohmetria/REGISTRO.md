# Registro de execuções — Ohmetria

Log append-only da Fundação. Cada execução escreve aqui o bloco entregue e o
próximo passo desbloqueado.

## 2026-09-14 17h17Z — Bloco 1: corpus de buscas paramétricas

**A ESCOLHA DA ILHA: PRIMEIRA TENTADA, SEM CORRIDA.** Os cinco `ESTADO.md` do
arquipélago estavam com `executando_desde: null`, que pela 1.1 já significa que
não há bloco da Fundação vivo — não foi preciso consultar o git, porque a
reserva é escrita **antes** do trabalho (passo 5) e `null` fecha a questão
sozinho. Pela **18.1**, ilha com despacho aberto do Raphael vem antes da
rotação, e **duas** tinham: ohmetria e jornadafly, as duas nascidas no **mesmo
commit** (`1758365`), o que empata o critério "entre dois despachos do Raphael,
o mais antigo". O desempate voltou para a rotação da seção 1 e a **ohmetria**
tem `ultima_execucao: null`, que conta como a mais antiga de todas (a jornadafly
já tinha rodado às 15h19Z). A **clubedomosaico** foi descartada da primeira
faixa por leitura, não por suposição: o despacho dela de 14/09 foi reescrito
pela 18.3 na execução das 11h18Z, os quatro itens saíram, e o que sobrou está
declarado **no próprio despacho** como bloco de malha com orçamento de
rastreamento na mesa — *"não item de conserto"*. Nenhum branch `claude/*` e
nenhum PR aberto para mesclar (`list_pull_requests` vazio; a branch de trabalho
estava idêntica ao `main`). Reserva aceita às **17h17Z, na primeira tentativa**.
**Primeiro bloco da vida desta ilha.**

**O DOMÍNIO ESTÁ REGISTRADO, E O `ESTADO.md` DESTA ILHA ESTAVA ERRADO — a
correção é a primeira coisa que esta execução entregou.** O cabeçalho dizia, em
maiúsculas, *"ATENÇÃO: o domínio ainda NÃO foi registrado"*, e o `PROMPT.md`
dizia o contrário, na primeira linha do despacho do Raphael: *"Domínio
ohmetria.com.br já registrado e pago — o passo 1 da seção 11 está cumprido e
ninguém precisa refazê-lo"*. **Dois arquivos da mesma pasta afirmando coisas
opostas sobre o fato mais básico da ilha**, e quem lê primeiro decide errado.
Resolvido no **banco, não na prosa** — a mesma disciplina da cicatriz da
Robometria de 13/09 (*"o endereço que você testa sai da prosa; o endereço que
vale está no banco"*), aqui aplicada ao registro do domínio:
`rdap.registro.br/domain/ohmetria.com.br` responde `status: active`,
`registration 2026-09-14T15:00:24Z`, `expiration 2028-09-14T15:00:24Z`, contato
técnico `RAMNA14`. **O `PROMPT.md` estava certo e o `ESTADO.md` estava velho:**
ele foi escrito antes das 15h, quando a afirmação ainda era verdadeira. Não foi
mentira de ninguém — foi resumo envelhecido lido como fato, que é o defeito que
a seção 4 do contrato diz que o Arquipélago mais paga.

**REDE PELA 20.2, ANTES DE TRABALHAR — E ELA ESTÁ BLOQUEADA.** Três passadas,
com controle na mesma passada:

| endereço | passada 1 | passada 2 | passada 3 |
|---|---|---|---|
| `https://ohmetria.com.br/` | **000** | **000** | **000** |
| `https://www.ohmetria.com.br/` | **000** | **000** | **000** |
| `https://robometria.com.br/` | 200 | 200 | 200 |
| `https://aquametria.com.br/` | 200 | 200 | 200 |

Seis medições de bloqueio contra seis de controle verde, nos mesmos segundos.
Não é o túnel. A causa nomeada é a **20.1**: o domínio não entrou na lista
"Domínios permitidos" no dia em que foi comprado. Gravado
`rede: bloqueada em 2026-09-14` no `ESTADO.md` e acrescentado ao despacho ALTO
que a execução da jornadafly abriu às 15h22Z — **que previa este caso em
condicional** (*"a ohmetria nasceu no mesmo dia e o domínio dela ainda nem foi
registrado — quando for, cai no mesmo buraco"*). Caiu, no mesmo dia, e agora
está medido em vez de previsto.

**E A RESSALVA QUE IMPEDE ESTA MEDIÇÃO DE SER LIDA COMO MAIS DO QUE É.** O 000 da
ohmetria tem **duas** causas possíveis somadas hoje, não uma: além da lista de
rede, o domínio ainda aponta para os nameservers de estacionamento do registro.br
(`a.auto.dns.br`, `b.auto.dns.br`) e **não tem registro A** —
`socket.gethostbyname('ohmetria.com.br')` devolve *"No address associated with
hostname"*. Um domínio sem endereço daria 000 mesmo com a rede liberada. As duas
causas só se separam depois que a hospedagem estiver de pé, e é justamente por
isso que o pedido ao Raphael **é melhor sair antes do WordPress**: depois, um 000
persistente vira diagnóstico ambíguo de novo. Escrito assim no despacho, com o
mesmo cuidado que a seção 4 exige para atribuição de causa — *"se a página trocou
depois, você não sabe de nada, e dizer que sabe é inventar a medição"*.

**POR QUE O BLOCO SAIU COM A REDE BLOQUEADA.** A 20.1 diz que a ilha não recebe
bloco enquanto o domínio não entrar na lista, e a razão que ela mesma dá é *"casca
no ar que não pode ser verificada é pior que casca inexistente"*. O bloco 1 **não
põe nada no ar**: é arquivo no repositório, o `PROMPT.md` desta ilha declara em
negrito que os blocos 1, 2, 3 e 3c não dependem de domínio nem de site, e os dois
campos de "Endpoints desta ilha" estão literalmente com
`<preencher quando o WordPress existir>`. O que a 20.1 protege está intacto; o
que ela bloqueia de verdade está declarado como bloqueado. Mesmo raciocínio, e
mesma redação, do bloco 1 da jornadafly de duas horas antes.

**UM TERCEIRO BLOQUEIO APARECEU, E ELE NÃO É DE ILHA NENHUMA — é do egresso, e
muda o método deste bloco.** Ao tentar abrir
`www.lojadesomautomotivo.com.br/comprar/qual-modulo-usar/woofer.html` para
enumerar a família de URLs do concorrente, a nuvem devolveu `EGRESS_BLOCKED`: a
rede Personalizada libera os domínios das ilhas, `*.googleapis.com` e
`github.com`, **e nada mais**. A busca web funciona (ela não sai por este proxy),
então o bloco saiu inteiro por ela — mas a consequência está declarada dentro do
corpus, em "Método", e é a regra da **20.3** cumprida: **toda URL citada no
arquivo é URL que apareceu em resultado de busca, com o título que a busca
devolveu; nenhuma foi aberta.** Isso importa para o bloco 3, que depende de
**ler PDF de fabricante** (Bomber, JBL/Selenium, Eros, Pioneer, e agora Zetta), e
hoje isso está fora do alcance da nuvem. Registrado no despacho como o que falta,
**e não como pedido fechado**, porque a Fundação ainda não tentou o bloco 3 e
pode ser que a busca resolva parte dele. Inventar o bloqueio antes de tentar
seria o mesmo erro que a seção 4 do contrato descreve de trás para frente.

### O que o bloco entregou

`ilhas/ohmetria/dados/corpus-buscas.md`, `publicar: false`, os três eixos que o
`PROMPT.md` manda não misturar, coletado entre **17h20Z e 17h45Z de 14/09/2026**.
**Zero número de volume de busca**, porque não houve acesso a ferramenta de
volume — mesma disciplina do corpus da Robometria e do da JornadaFly. **Zero
valor deste arquivo entra em banco ou em constante de calculadora**, e isso está
escrito duas vezes lá dentro: o que ele mede é o **desacordo da SERP**, não a
física.

**Nenhuma consulta que o dossiê da rodada 004 já mediu foi remedida.** O arquivo
ataca o que ele deixou em aberto, a começar pela única que ele marcou
explicitamente como não medida.

### Os seis achados, e por que cada um muda um bloco futuro

**1. A CONSULTA QUE O DOSSIÊ DEIXOU POR MEDIR ESTÁ MEDIDA, e a hipótese dele
cresceu.** Ele tinha **um** exemplo de URL por faixa de RMS
(`/qual-modulo-usar/subwoofer/400-rms.html`) e a leitura de que ninguém constrói
isso sem busca própria em cada variação. A família foi mapeada e tem **dois**
eixos: `{woofer, subwoofer} × faixa de RMS`, com **sete URLs vistas** (woofer
200, 400, 600 e 1200; subwoofer 400, 1000 e 2000) mais as duas páginas-mãe, e um
concorrente (`somautomotivobr`) cobrindo **cinco tipos** num endereço só. **É
planta de malha para o bloco 5b, medida e não suposta.**

**2. A VAGA DA F1 É UM DESACORDO, NÃO UM VAZIO — e é a mesma forma dos achados
da Aquametria e da JornadaFly.** Para a **mesma** pergunta sobre um falante de
200 W RMS, a SERP publica três regras incompatíveis: *até 100%*
(`lojadesomautomotivo`), *o dobro* (`somautomotivobr`, no próprio `<title>`) e
*150 a 250 W* (`mundomax`). De 150 a 400 W — **2,7 vezes** — e **nenhuma das três
diz de onde a regra sai**. O mesmo `mundomax` muda o próprio multiplicador de
`0,75–1,25×` para `0,6–1,2×` entre dois exemplos da mesma página. **Consequência
para o bloco 2:** a F1 declara o critério **com fonte de fabricante**, senão ela
vira a quarta opinião de uma briga de três.

**3. EXISTE UM VEREDITO QUE NINGUÉM PUBLICA, E ELE É "NÃO FECHA".** Dois
subwoofers de bobina dupla 2+2 Ω alcançam, em ligação simétrica, **0,5 Ω, 2 Ω e
8 Ω** — **1 Ω não está no conjunto**. Conferido por script nesta execução, cinco
configurações, e o mesmo script mostra que **um** sub 2+2 sozinho **chega** a
1 Ω, que é de onde vem a confusão. Quem digita a consulta-âncora com esse par e
um módulo de 1 Ω está pedindo o que não existe, e as páginas medidas respondem
com a fórmula *"impedância ÷ número de alto-falantes"*, que sozinha produz 0,5 Ω
e não avisa nada. **Dizer "não fecha, e o mais perto que fecha é 2 Ω" na primeira
linha é exatamente o que o `VOZ.md` manda e o que ninguém faz.** Vira obrigação
do bloco 2.

**4. A CALCULADORA JÁ EXISTE NO BRASIL — e isto CORRIGE o dossiê.** Ele escreveu
*"uma única calculadora em toda a varredura: `infinitysom.com.br`"*. São pelo
menos **quatro** para impedância (`nexxobox` com duas, `amantesdeamplificadores`,
`sombox` com duas URLs) e **três** para caixa e duto (`audioclassico`,
`speakerboxlite`, `omnicalculator/pt`). **A afirmação do dossiê é verdadeira para
as consultas que ele mediu e falsa para o nicho** — e a distinção entre as duas
coisas é o que esta correção existe para fixar. **Por que ela CONFIRMA a tese em
vez de derrubar:** essas ferramentas fazem a **aritmética** e nenhuma faz a
**decisão**, que é cruzar o resultado contra um banco de módulos que estabilizam
naquela impedância com RMS compatível; e **nenhuma delas apareceu no top 10 da
consulta-âncora** que o dossiê mediu. A ferramenta existe e **não ocupa a
pergunta que a pessoa digita** — a mesma forma do achado da JornadaFly sobre o
ângulo "vale a pena" já ter dono. **E existe uma pergunta sem resposta nenhuma:**
não há, em pt-BR, **lista de módulos filtrável por impedância estável**; a busca
devolve categoria de loja organizada por **número de canais**, vídeo de
comparação de marca e uma das fazendas nomeadas no dossiê.

**5. A F2 TEM UMA TRAVA DE UNIDADE QUE PODE QUEBRAR A VALIDAÇÃO DO PRÓPRIO
`PROMPT.md`.** "Litros" é três grandezas com nomes que não batem: a Zetta publica
*"volume bruto 49 L, volume livre 42 L, sintonia 41 Hz"*; a **Hinor — que está na
lista de carga do bloco 3** — publica que *"40 litros brutos, com o duto e o
subwoofer dentro, dão 32 a 35"*. A razão entre líquido e bruto fica entre **0,80
e 0,88**. A **trava 3** do `PROMPT.md` manda validar a fórmula da F2 contra a
litragem recomendada pelo fabricante — e **se a fórmula devolver líquido e a
recomendação for bruta, a validação acusa 12 a 20% de erro que não é erro de
fórmula, é erro de unidade**, com os dois números plausíveis e nenhum parecendo
absurdo. É mais perigoso que o `Vas 672,3 cm³` que o `PROMPT.md` já nomeava,
justamente porque não salta aos olhos. **Consequência para o bloco 3:**
`litragem_tipo` (`bruto | liquido | nao_declarado`) nasce ao lado de
`litragem_l`, e a F2 diz na tela qual dos dois está devolvendo.

**6. O DESACORDO MAIS CARO ESTÁ NO EIXO C, porque dele saem o fusível E o
cabo.** Para um módulo de 2000 W RMS a SERP publica **três divisores**: `÷12`
(167 A), `÷12,6` (159 A) e `÷20`, o "consumo musical" (100 A). **67% de
diferença**, e o fusível recomendado a 125–150% da corrente vai de **125 A a
250 A** conforme a página que a pessoa abriu primeiro. **Nenhuma das três declara
o rendimento do módulo**, que é o que faria a conta fechar. E a consulta escrita
**com a distância** (1000 W, 4 metros, queda de tensão) devolveu **cinco fóruns**
— um deles de energia solar — e **a calculadora da InfinitySom não apareceu
nela**. A vaga da F3 fica medida com precisão: não é "calcular bitola", é
**calcular bitola para a distância de ida e volta, com o fusível junto e o
rendimento declarado**, que é onde o `PROMPT.md` diz que a do concorrente para.
*(De quebra, o capacitor: 1 farad por 1000 W na regra de bolso contra o rótulo da
própria Taramps, "Mega Capacitor 0,3 Farad 1000w rms" — 3,3× na mesma página de
resultados. Não vira ferramenta agora; é matéria de artigo-âncora do bloco 5.)*

### Verificação

Nada foi ao ar e nada podia ir: esta ilha não tem site, não tem `manifest.json` e
não tem endpoint de Sync. O que foi verificado nesta execução:

- **Cabeçalho do `ESTADO.md` por parser**, como manda a seção 2 —
  `yaml.safe_load` aprovando, `bloco_atual` com 13 linhas e sem aspas duplas
  dentro de escalar de aspas duplas.
- **A aritmética do achado 3 por script**, cinco configurações de ligação, em vez
  de confiada à cabeça — inclusive o contraexemplo (um sub sozinho **chega** a
  1 Ω) que explica de onde vem a confusão do nicho.
- **O registro do domínio pelo RDAP oficial**, não pela prosa dos dois arquivos
  que discordavam.
- **A rede em três passadas com controle na mesma passada**, como a 20.2 manda,
  mais a resolução de DNS que revelou a segunda causa possível do 000.

### Próximo passo desbloqueado

**BLOCO 2 — especificação das calculadoras** (`dados/especificacao-calculadoras.md`
e `dados/constantes.json`). Não depende de site, não depende da lista de rede, e
já nasce com três obrigações que saíram do bloco 1 e estão escritas no fim do
corpus: o critério de casamento de RMS **com fonte**, o veredito **"não fecha"**
com a impedância mais próxima que fecha, e o **rendimento suposto + distância de
ida e volta** declarados na tela da F3.
