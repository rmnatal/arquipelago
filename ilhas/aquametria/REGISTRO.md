# Registro de execucoes — Aquametria

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e
o proximo passo desbloqueado, e espelha o mesmo resumo em
`/areas/projeto-aquametria.md` na memoria.


> **ANOMALIA DE ORDEM DESTE ARQUIVO, anotada em 14/09/2026 e NÃO consertada aqui.**
> As entradas deste log estão em ordem do mais novo para o mais velho, do topo
> para baixo — menos uma: a das **15h18Z–15h52Z de 14/09** foi escrita no FIM do
> arquivo, abaixo das entradas de 06 e 07/09. Nada foi movido nesta execução
> (mexer em entrada de outra execução num log append-only custa mais do que a
> desordem), mas quem procurar a execução do piso de busca a encontra no rodapé e
> não no topo.


## 2026-09-24 13h18Z–14h45Z — O MUTIRÃO DO DESPACHO DO RAPHAEL: AS 24 FOTOS SEM DIMENSÃO FECHARAM (41 de 41), E O PARÊNTESE QUE CUSTOU TRÊS FICHAS ERA UMA REGRA APLICADA DE UM LADO SÓ. Intestáveis de 14 para 12; NENHUMA URL nova

**A ESCOLHA DA ILHA: FOCO, RESERVA NA PRIMEIRA.** `foco.md` nomeia a aquametria
desde 21/09 (1.2), então não houve rotação. O cabeçalho trazia
`executando_desde: null` — pela **1.1** isso já significa que não há bloco da
Fundação vivo, e não houve reserva vencida para o git desempatar. O último commit
na pasta da ilha era de 14 minutos antes, mas era o **despacho do Raphael** escrito
pelas Mãos no repositório, e a 1.1 diz com todas as letras que o que torna a ilha
VIVA é commit de **bloco da Fundação**. Reserva aceita às 13h18Z, commit `5a9b027`.
Nenhum PR aberto; a branch `claude/*` estava em sincronia com o `main`.

**O DESPACHO QUE MANDOU (24/09, 10h05 BRT):** mutirão reaberto **só** para dívida
que não cria URL — as 24 imagens sem largura e a coleta de ficha. Dentro da
exceção, quantos blocos couberem; fora dela, a seção 1 inteira. **Nenhuma URL
nasceu, mudou de endereço ou saiu**, e a cota da 21.4 segue gasta em 3 de 3.

**Rede pela 20.2, retestada e não herdada:** três passadas, home **200** e
`/status` **200** nas três, revisão 111 igual à do `manifest.json`.

---

### 1. AS 24 FOTOS SEM DIMENSÃO: O ARQUIVO RESPONDIA EM OUTRO ENDEREÇO, E NINGUÉM TINHA PERGUNTADO

A causa estava medida e certa desde 09/09: o egresso desta nuvem barra
`down-bs-br.img.susercontent.com`, e quem não alcança o arquivo não lê o
cabeçalho. **Reconferido hoje pela 20.3, não herdado:** `000` em três passadas,
contra `cf.shopee.com.br` em **200** nas mesmas três.

**O que ninguém tinha perguntado é se o MESMO arquivo respondia em outro host.**
O identificador (`sg-11134201-8259h-…`) é o mesmo nos dois, e
`cf.shopee.com.br/file/<id>.webp` serve aquele arquivo.

**E A PROVA NÃO É ESSE RACIOCÍNIO — É UM GRUPO DE CONTROLE QUE JÁ ESTAVA NO
BANCO.** "Mesmo id, logo mesmo arquivo" é hipótese sobre infraestrutura de outra
empresa, e hipótese sobre infra alheia envelhece calada. Só que esta ilha tinha
guardado, sem saber para quê, **oito fotos hospedadas no host BLOQUEADO cuja
dimensão já estava medida — e medida por OUTRO INSTRUMENTO**, `naturalWidth` ×
`naturalHeight` lidos no Chrome do Raphael pela ronda da Sentinela de 13/09, do
outro lado do bloqueio.

Medidas pelo espelho: **8 de 8 batem.** E batem em **265, 692, 726 e 1001** —
justamente os números que um redimensionamento não sobreviveria. Espelho que
servisse miniatura padronizada devolveria 800×800 ou 1024×1024 para todas, e as
tortas ficariam vermelhas na primeira passada.

**Resultado: as 24 mediram. O banco foi de 17 para 41 fotos com dimensão, de 41
com foto — a fila zerou.**

**O QUE A RÉGUA NÃO FAZ, e cada recusa tem um motivo diferente:**
- **Não troca `imagem.url` para o espelho.** As 8 do controle provam que o host
  bloqueado entrega o arquivo a quem tem navegador — ele funciona para o
  visitante; quem não o alcança é esta nuvem. Trocar o que o visitante recebe
  para contornar um limite da máquina que constrói o site seria o rabo abanando
  o cachorro.
- **Não preenche `verificado_em`.** Ninguém abriu a URL servida e viu a imagem
  carregar. Três datas, três vidas: `coletado_em`, `verificado_em` e `medida_em`
  são atos diferentes, e só o terceiro aconteceu aqui.
- **Não toca `alt` nem `alt_origem`.** Quem lê bytes não vê imagem.

**Nascem** `regua-cdn-shopee.py` (compartilhada, importada pelos dois portões, e
por isso escapa da denúncia do `bancada.py`), `teste-cdn-shopee.py` (66
afirmações, sem rede) e `conferir-espelho-cdn.py` (no ar, 36 afirmações), que
**remede o grupo de controle a cada passada** — a premissa é sobre um CDN que não
é nosso e pode mudar sem aviso, e quando mudar quem descobre é o controle ficando
vermelho, não um cartão com a caixa errada na tela de alguém. Ele também **reprova
se o grupo de controle sumir**, em vez de imprimir "0 de 0, tudo certo".

**O PORTÃO DE BANCADA NASCEU VERDE, QUE NÃO PROVA NADA — e as mutações acharam
três buracos reais:**
1. **A máscara de 14 bits do WebP VP8.** Todas as dimensões que eu tinha escolhido
   cabem em 14 bits com os dois bits altos em zero, então apagar a máscara não
   mudava resultado nenhum. Arquivo real com escala é raro, e é por isso que só a
   mutação o acha: o defeito dormiria até a primeira foto que o tivesse.
2. **O espelho do espelho.** Eu afirmava a identidade com `/file/<id>`, que é a
   forma canônica — e remontar a canônica dá a canônica. O caso que separa os dois
   é a URL com parâmetro de consulta.
3. **As três tentativas da 20.2.** Nenhuma das 54 afirmações tocava a única função
   com rede. Medidas agora com um `urlopen` de mentira que falha duas vezes e
   acerta na terceira — sem rede, como a bancada exige.

`mutacoes-cdn-shopee.py`: **11 de 11 reprovadas.**

---

### 2. O PARÊNTESE NÃO ERA SEPARADOR, E A REGRA VALIA DE UM LADO SÓ DA COMPARAÇÃO

O ensaio da coleta mostrou **três registros recusando o anúncio CERTO**, que
aparecia na primeira página da busca:

    "Filtro Canister Eheim Classic 600 (2217) 1000l/h 20w 220v"
        recusado por "o titulo nao traz o codigo (classic 600 2217)"

**A causa:** `codigo_base()` troca `(` e `)` por espaço **no modelo** desde que
nasceu, então o código chegava como `classic 600 2217`; a classe de separadores
do `token_no_titulo()` nunca teve parêntese, então o **título** chegava com ele no
meio. Régua que devolve zero para sempre, por mais certo que esteja o anúncio.
**É a mesma família do falso positivo do `noindex` de aspa simples, medido nesta
mesma ilha quatro horas antes** — régua boa que atravessa a fronteira onde a outra
metade da comparação tem outro autor.

**O afrouxamento aceita PONTUAÇÃO, nunca PALAVRA.** `"Classic 250 440lh Eheim -
2213"` continua reprovado: entre `250` e `2213` há duas palavras, e código
espalhado pelo título identificaria também o anúncio de kit que cita dois filtros
da linha. O preço de ser conservador aqui é ficar sem ficha; o de ser folgado é a
C5 prometer uma coisa e entregar outra na casa de quem leu.

**DUAS FICHAS NOVAS, conferidas com os olhos antes de gravar (25.3):**

| registro | anúncio | degrau |
|---|---|---|
| `eheim-classic-600-2217-220v` | Eheim Classic 600 (2217) 1000l/h 20w **220v** | 1 |
| `eheim-classic-600-2217-127v` | Eheim Classic 600 (2217) 1000l/h 20w **127v** | 1 |

As duas casaram com a voltagem certa, em lojas e URLs diferentes. **E a foto que a
API devolveu tem o mesmo identificador de arquivo da que já estava no banco**,
colhida à mão em 09/09 — a API achou o mesmo anúncio que a pessoa tinha achado,
por outro caminho. É a confirmação mais forte que esta coleta já produziu, e ela
também confirma, de terceiro lado, a premissa do espelho do item 1.

**`intestavel` foi de 14 para 12**; `url_produto` de 33 para 35.

**E A BANCADA REPROVOU UMA AFIRMAÇÃO MINHA.** Eu tinha escrito que partes
**grudadas** não deveriam casar (`"Classic 6002217"`). Elas casam, de propósito, e
é o mesmo mecanismo que faz `"HT1300"` casar com `HT-1300` — que é como metade do
varejo escreve — e `"A301"` com `a 301`. Não dá para exigir separador entre duas
partes sem perder as duas colagens legítimas. **Fica afirmado como é, não como eu
gostaria**, para que uma mudança futura apareça ali em vez de passar calada.

Bancada de **159 para 177** afirmações; mutações de **20 para 22**, e as duas novas
medem as **duas** direções — o separador apertado demais e o afrouxado até engolir
palavra. Sem as duas, a classe teria uma direção medida só, que é como régua boa
vira folgada numa passada distraída.

---

### 3. O NÚMERO "45" JUNTAVA DUAS COISAS DIFERENTES, E A LEITURA SEMANAL TIROU A CONCLUSÃO ERRADA DELE

O despacho fala em **45 itens sem ficha**, e 45 é a contagem de
`afiliado.url_produto` vazio. Mas `url_produto` é a **URL crua**, não a ficha.
Contando o que chega à tela: **47 itens com botão de ficha**, **31 sem link de
ficha nenhum**, **14 com ficha e sem a URL crua** (`intestavel: true`).

**A leitura semanal de 23/09 escreveu que os 14 intestáveis são "exatamente as
marcas que a seção 7 diz que a Shopee não vende" e que são "o caso de manual do
degrau 2 (catálogo `/p/MLB…` do Mercado Livre)".** Os 14 têm `plataforma: shopee`
e o título do anúncio guardado em `afiliado.anuncio_shopee` — a Shopee **vendia**
os 14 em 07–09/09, e cada um tem link de afiliado no ar hoje. Caçar catálogo no
Mercado Livre para eles seria trabalho gasto em produtos que já têm link — e é
justamente a parte da Proposta 3 que depende de um egresso que continua fechado.
**O que eles precisam é da URL crua do mesmo anúncio**, para o par ficar
demonstrável (25.4-b.1). Dois fecharam hoje.

**O RESÍDUO FOI ESCRITO INTEIRO**, como o despacho pede, em
`dados/fichas-pendentes.md`: **43 itens em quatro causas.**

| causa | itens | é portão severo? |
|---|---|---|
| **A** — a busca não devolve nada | 27 | não: não há o que julgar |
| **B** — só resultado de outra categoria (código curto: `AT-100`, `A301`) | 12 | não: recusa correta |
| **C** — quase, a linha certa apareceu | 3 | **não: nos três o portão está certo** |
| **D** — o registro não declara marca (`rs-50-50w`) | 1 | não: falta dado, não sobra rigor |

**A leitura que importa: A e B somam 39 dos 43, e nas duas o gargalo é oferta e
palavra-chave, não código.** Escrever mais portão não move nenhuma delas. Sobram
quatro itens em que um par de olhos num navegador vale mais do que qualquer coisa
que esta nuvem consiga fazer.

---

### ACHADO DE DADO QUE NÃO É DESTA FILA, e não dá para consertar de olhos fechados

Medindo as 24 apareceu que **dois registros compartilham a mesma foto**:
`maxxi-m-050-anuncio-220v` e `maxxi-m-200-anuncio-220v`, mesma URL. Os dois `alt`
foram escritos por quem viu a foto e descrevem **potências diferentes** (50 W e
200 W) — a mesma imagem não mostra os dois, então **no máximo um está certo**.
Qual corrigir depende de **olhar a foto**, e quem lê os bytes não a vê. Fica para
a Sentinela Técnica, junto com os 33 `alt_origem: 'banco'` que já a esperavam.

### E UM DEFEITO MEU, PEGO ANTES DO AR

A primeira versão do `coletar-dimensao-imagens.py` gravou o banco com `indent=1`
e **reformatou 2.542 linhas para mudar 24 campos**. Diff que ninguém revisa é a
maneira mais eficiente de esconder uma mudança real no meio de ruído. Corrigido
para `indent=2`, que é o formato deste banco e o que o `coletar-shopee.py` usa; o
diff foi de 2.542 para **78** linhas. Fica escrito no próprio código, não só aqui.

E as **duas primeiras renovações de reserva saíram no FUTURO** (13h55Z e 14h05Z
escritas às 13h38Z e 13h44Z), porque eu somava folga de cabeça em vez de ler o
relógio. Reserva adiantada faz a ilha parecer ocupada mais tempo do que está, que
é o contrário do que a 1.1 quer. A terceira foi lida do `date -u`.

**VERIFICAÇÃO.**

**O `bancada.py` FOI MORTO PELO TIMEOUT e isso fica escrito, porque "rodei a bancada" sem esta linha seria falso.** Ele saiu em `exit=124` dentro de `mutacoes-peixes.py`, com **11 dos 38 portões medidos**. Os outros 27 foram rodados **um a um**, à mão, e o número da bancada abaixo é a soma dessas passadas — não a saída de um comando só. *(Causa medida, e ela não era o portão: duas execuções do `bancada.py` estavam vivas ao mesmo tempo, disputando CPU — a segunda ficou com metade da máquina. A primeira, que media uma árvore já desatualizada, foi encerrada; mesmo sozinho, `mutacoes-peixes` leva mais que os 1700 s do timeout.)*

**BANCADA — 38 de 38 portões, 0 falha.** `teste-peixes` **4299** afirmações · `teste-ga4` 825 · `teste-escada-compra` 703 · `teste-seo-tecnico` 555 · **`teste-coleta-shopee` 177 (eram 159)** · `teste-titulos-das-duas-fontes` 160 · `teste-datas-schema` 102 · **`teste-cdn-shopee` 66 (novo)** · `teste-apelidos` 59 · `teste-dimensao-imagem` 42 · `testar-validador-especies` 41 · `teste-site-jsonld` 22 · `teste-robots` 21 · `teste-purga-cache` 21 · `teste-conversor-markdown` 18 · `teste-atualizador-sync` 9 · `teste-escape-shortcode`, `teste-arvore`, `teste-voz`, `conferir-entidades`, `conferir-indice-de-levas`, `conferir-protecao-funcoes`, `conferir-slugs` limpos. `validar-produtos` **78 produtos, 0 erro, 8 avisos** (os V20 conhecidos, de item com link e sem foto); `validar-especies` **40 espécies, 0 erro, 3 avisos** (o E15 do guppy e os dois E21 conhecidos).

**MUTAÇÕES — 0 sobreviventes em todas.** `mutacoes-peixes` **100 de 100** · `mutacoes-escada` 26 · **`mutacoes-coleta-shopee` 22 (eram 20)** · `mutacoes-arvore` 14 · `mutacoes-dimensao` 14 · `mutacoes-site-jsonld` 14 · `mutacoes-ga4` 13 · `mutacoes-datas` 12 · **`mutacoes-cdn-shopee` 11 (novo)** · `mutacoes-titulos` 6 · `mutacoes-privacidade` 23 afirmações · `mutacoes-purga-cache` 8 baterias, zero inertes.

**NO AR, depois do Sync (revisão 113, conferida no `/status`, aplicada na PRIMEIRA chamada — sem a armadilha de cache de CDN da 27.3).** `conferir-peixes-no-ar` **1012** afirmações, 0 falha (eram 1012 na malha de 52 URLs) · `conferir-datas-e-voz-no-ar` **407**, 0 · `conferir-escada-no-ar` **130**, 0 · **`conferir-espelho-cdn` 92, 0 (novo)** · `conferir-cache-do-host` 55, 0 · `conferir-privacidade-no-ar` 21, 0 · `conferir-site-jsonld-no-ar` 16, 0 · `conferir-robots-no-ar` 12, 0 · `conferir-ga4-no-ar` 0 falha.

**E O PORTÃO NOVO REPROVOU NO PRIMEIRO USO NO AR — o meu.** Ver o item 4 abaixo: ele imprimiu um grupo de controle de **32** fotos "medidas por outro instrumento", e 24 daquelas 32 eu tinha medido naquela mesma hora, pelo próprio espelho que elas deveriam estar conferindo. Consertado antes de a execução fechar: **8 controles e 24 regressões**, com os rótulos separados e a procedência exigida em campo.

### 4. O PORTÃO DO ESPELHO ESTAVA DILUINDO A PRÓPRIA PROVA COM AS PRÓPRIAS CONCLUSÕES

A primeira versão definia controle como *"está em host bloqueado e tem dimensão"*. Aquilo estava **certo enquanto as únicas fotos assim eram as 8 que a Sentinela mediu no Chrome** — e deixou de estar certo no minuto seguinte, quando o `coletar-dimensao-imagens.py` mediu 24 do mesmo host pelo espelho. As 24 entraram no controle por construção, e o portão passou a afirmar **quatro vezes mais evidência do que tem**.

**Não era um número errado: era uma prova contaminada.** O portão continuaria ficando vermelho se o CDN mudasse — as 8 verdadeiras reprovariam —, mas evidência inflada é como se para de desconfiar de uma premissa.

**A regra agora:** só é controle quem foi medido por **outro** instrumento, e quem responde isso é o campo `medida_como`. As 24 continuam sendo remedidas, com o rótulo certo: **teste de regressão do CDN**, nunca prova da premissa.

**E a porta dos fundos dessa definição foi fechada junto.** "Controle" está definido por **negação** (não menciona o espelho), então foto com `medida_como` **vazio** cairia no controle por omissão e diluiria a prova do mesmo jeito, sem ninguém ver. Cada membro do controle agora tem de **dizer em campo** de onde veio o número. Provado num banco copiado com a procedência apagada: o portão reprova, nomeando cada uma.

### O QUE FICA DESBLOQUEADO PARA A PRÓXIMA EXECUÇÃO

- **O mutirão do Raphael continua aberto até 30/09** e **não é para apagar**: é exceção com prazo próprio, e morre sozinha na leitura semanal daquele dia.
- **A fila de dívida que não cria URL está vazia do lado da máquina.** As 24 fotos fecharam; o resíduo das fichas está medido e escrito, e em **39 dos 43** o gargalo é oferta e palavra-chave, não código.
- **O que sobrou pede olho humano, não execução da Fundação:** os 33 `alt_origem: 'banco'`, a foto que dois registros Maxxi compartilham com `alt` de potências diferentes, e os quatro itens dos grupos C e D de `dados/fichas-pendentes.md`.
- **Item 2 do despacho da Sentinela (diagnóstico da 21.5) continua aberto de propósito:** o critério exige arquivo escrito **depois** da leitura semanal de 30/09. Hoje é 24.

---

## 2026-09-24 10h16Z–11h00Z — O ITEM 1 DO DESPACHO ERA FALSO POSITIVO, E A CAUSA É A RÉGUA: A DIRETIVA QUE DECIDE O ÍNDICE FICOU 14 DIAS SEM PORTÃO NO AR. Mais a Proposta 1 no ar (peixes 1.16.0, manifest revisão 111, `/status` conferido na 111; NENHUMA URL nova)

**A ESCOLHA DA ILHA: FOCO, E A RESERVA PASSOU NA PRIMEIRA.** `foco.md` nomeia a
aquametria desde 21/09 (1.2), então não houve rotação a aplicar. O cabeçalho
trazia `executando_desde: null`, que pela **1.1** já significa que não há bloco da
Fundação vivo — não houve reserva vencida para o git desempatar. Reserva aceita às
10h16Z, commit `6ea6b13`. Nenhum PR aberto e a branch `claude/*` do repositório
estava em sincronia com o `main`, nada a mesclar. **Rede pela 20.2, retestada e não
herdada:** três passadas, home em **200** e `/status` em **200** nas três, revisão
110 igual à do `manifest.json`.

**O TETO DA 21.4 ESTAVA GASTO ANTES DE EU COMEÇAR, e isso não travou nada:** a
leva 9, de 23/09, foi a **terceira** da semana que começou em 21/09. Como o
despacho fura a fila pela **18.5** ("verificação antes de construção, sempre") e
correção não consome vez de bloco (**18.2**), esta execução é toda de despacho e
de portão — **zero URL nova**, que é o que o teto proíbe.

### 1. O ITEM 1 NÃO EXISTIA. A PÁGINA ESTAVA CERTA DESDE 10/09, E QUEM ERROU FOI O INSTRUMENTO

O item dizia que `https://aquametria.com.br/author/aquametria_gestor/` respondia
**200 sem `<meta name="robots">`**. Medido às 10h2xZ com quebra de cache e
`Accept-Encoding: identity`, a página serve:

    <meta name='robots' content='noindex, follow' />

**Aspa simples.** Nesta ilha quem imprime a meta é o **núcleo do WordPress**, pelo
filtro `wp_robots` — e o núcleo usa aspa simples. O critério de pronto do item
pedia `grep -c 'name="robots"[^>]*noindex'`, de aspa **dupla**, que devolve **zero
para sempre** nesta ilha por mais correta que a página esteja.

**A régua não veio do nada, e é isso que a torna perigosa:** nas irmãs
**robometria** (`robometria-r1.php`, `-r2.php`) e **clubedomosaico**
(`clubedomosaico-f1/f2/leads/casca.php`) quem imprime a meta é o **snippet**, com
`echo '<meta name="robots" content="noindex,follow">'` — **aspa dupla**, e lá o
mesmo `grep` está exatamente certo. Foi uma régua boa **atravessando a fronteira
de uma ilha onde a tag tem outro autor**. E a aquametria escolheu o filtro do
núcleo **de propósito**, com o motivo escrito no próprio snippet desde 10/09:
imprimir a meta na mão arrisca servir **duas** metas `robots`.

**MEDIDO NOS QUATRO CONTEXTOS DE ARQUIVO, não só no que o item nomeou:**

| URL | HTTP | meta `robots` |
|---|---|---|
| `/author/aquametria_gestor/` | 200 | `noindex, follow` — uma só |
| `/?s=aquario` | 200 | `noindex, follow` — uma só |
| `/2026/09/` | 200 | `noindex, follow` — uma só |
| `/category/metodos/` | 200 | `noindex, follow` — uma só |
| `/` (home, controle) | 200 | `max-image-preview:large` — **sem** noindex, que é o certo |

### 2. O CONSERTO QUE O ITEM PEDIA É QUE SERIA O DEFEITO

O item mandava **acrescentar** `noindex`. Cumprido ao pé da letra por quem
confiasse na medição, o conserto imprimiria a **segunda** meta `robots` ao lado da
que o núcleo já imprime — e **o Google resolve meta duplicada pelo lado mais
restritivo**, numa ilha com 52 URLs que precisam ser indexadas. **O falso positivo
custaria mais caro que o defeito imaginado**, e a direção do estrago seria a de
apagar página do índice. É por isso que isto virou arquivo e despacho, e não uma
linha dizendo "não era nada".

### 3. O QUE O ITEM ACHOU DE VERDADE VALE MAIS QUE O DEFEITO QUE ELE DESCREVEU

**Nada nesta ilha media, no ar, a diretiva que decide o que entra no índice do
Google.** A regra existia e estava certa — `aquametria_seo_deve_noindex()`, função
pura, desde 10/09 — e `ferramentas/teste-seo-tecnico.php` a media **fora do
WordPress**. Ou seja: a régua vivia na bancada e a tela não era medida por
ninguém. É a distância exata que a **seção 4** do contrato paga mais caro, e ela
ficou **14 dias** aberta. O único instrumento que já tinha apontado para lá era um
`grep` digitado numa ronda, e ele estava errado.

Nasceram três arquivos, e a divisão entre eles é o ponto:

- **`ferramentas/regua-robots.py`** — a régua, **compartilhada**. Não é portão: não
  afirma nada sozinha. Mora num arquivo só porque régua escrita duas vezes erra de
  um lado, e o lado errado fica verde. Ela (a) **ignora aspa** — simples, dupla ou
  nenhuma, nos dois atributos; (b) exige que o `noindex` seja **diretiva** no
  `content` de uma meta cujo `name` é `robots`, não a palavra solta na mesma linha,
  que era o que o `grep` aceitava; (c) **conta** as metas, porque **duas é defeito
  tanto quanto zero** e a medição que só pergunta "tem?" nunca vê a segunda.
- **`ferramentas/teste-robots.py`** — 21 afirmações de bancada, sem rede, em HTML
  escrito à mão, **nas duas direções**. A metade de cima são páginas que mandam não
  indexar (aspa simples, dupla, sem aspa, ordem trocada, caixa alta, diretiva no
  meio da lista, meta duplicada); a de baixo são páginas que **não** mandam (a home
  desta ilha, sem meta nenhuma, a palavra no corpo, dentro de `<script>`, meta de
  outro nome, `content` vazio, `noindexar`, tag comentada). **O caso 1 é o falso
  positivo de 23/09 em pessoa:** se a régua voltar a ler só aspa dupla, ele fica
  vermelho na bancada em um segundo, e não num despacho.
- **`ferramentas/conferir-robots-no-ar.py`** — 12 afirmações no ar, **as duas
  direções que o próprio item declarou** ("acrescentar `noindex` demais é o defeito
  oposto e igualmente grave"): os 4 contextos de arquivo mandam `noindex`; as **52**
  URLs do sitemap **não** mandam; e **cada uma serve exatamente uma** meta `robots`
  — esta última existe porque a maneira plausível de fechar o item era imprimir a
  segunda tag na mão, e este portão reprovaria esse conserto. A lista de URLs sai do
  **sitemap no ar**, nunca digitada: a leva seguinte publica página e a régua cresce
  sozinha.

**Verde no ar em 24/09/2026:** 12 afirmações, 0 falha.

### 4. A RÉGUA NOVA ESTAVA ERRADA NA PRIMEIRA PASSADA, E QUEM DISSE FOI O PORTÃO

Na primeira execução de `teste-robots.py`, **duas afirmações ficaram vermelhas** —
o caso 15 e o da contagem: a régua contava uma tag **citada dentro de um
comentário HTML** como diretiva servida. Comentário e corpo de `<script>`/`<style>`
passaram a sair **antes** da varredura de tags, e dois casos novos entraram para
provar (a tag inteira como texto dentro de `<script>`, e dentro de comentário
dentro de `<script>`). **Tag comentada valendo como diretiva é o falso positivo de
23/09 de novo, do outro lado.** Portão que nasce verde no primeiro uso não provou
nada; este nasceu vermelho e apontou para quem o escreveu.

### 5. PROPOSTA 1 NO AR: O TÍTULO PASSA A DIZER A CONSULTA, E ELA JÁ ESTAVA DECLARADA NO REGISTRO HAVIA DEZ DIAS

A Sentinela mediu quatro grafias da mesma busca no Search Console de 23/09:
`ciclídeos anões` **6,0**, `ciclídeo anão` **11,0**, `ciclideo anao` **13,0**,
`ciclideos anoes` **35,0** — uma impressão cada. As duas **singulares** são as que
caem na banda de 11 a 20, que é a banda em que a **12.1** nomeia título e meta
description como a alavanca. A página é a **única desta ilha já na disputa**.

**O QUE NINGUÉM TINHA MEDIDO, e é o motivo de a linha ter nascido errada:** o
registro desta página declara `'consulta' => 'quantos litros para ciclídeo anão'`
**desde a leva 6, em 14/09/2026** — e o `titulo` **não continha essa frase**. Dez
dias de uma página perseguindo uma consulta que o próprio registro nomeia e que o
título não dizia.

Servido no ar às 10h5xZ, revisão 111, medido depois de decodificar as entidades:

- `<title>`: `Ciclídeos anões: quantos litros para ciclídeo anão – Aquametria` —
  **63 caracteres** (teto 65 do `teste-voz.mjs`: 50 no campo + os 13 de
  ` – Aquametria`), com a forma **singular**, a **plural**, e a consulta declarada
  **inteira, palavra por palavra**.
- `<meta name="description">`: **148 caracteres**, abrindo pela consulta singular,
  com as duas formas.
- `<h1>` e `og:title` mudaram junto. **As quatro superfícies dizem o mesmo nome no
  ar.**

**O RÓTULO PLURAL CONTINUA ABRINDO O TÍTULO, e isso é escolha e não descuido:** é
a grafia de **melhor** posição das quatro (6,0). Trocá-la pela singular para
consertar a pior seria **mudar o defeito de lado**. O molde `<rótulo>: <pergunta>`
é o mesmo das oito irmãs do eixo. Nenhuma URL nasceu, mudou de endereço ou saiu, e
as 3 fichas filhas não foram tocadas — a 12.1 proíbe trocar URL, e a proposta
dizia isso com todas as letras.

### 6. O TÍTULO MORA EM DOIS ARQUIVOS, AS 38 PÁGINAS CONCORDAVAM, E NADA MEDIA ISSO

- `snippets/aquametria-peixes.php`, no `aquametria_peixes_registro()` → `post_title`,
  logo o `<h1>` e a primeira metade do `<title>`.
- `dados/metas-seo.json`, em `paginas_do_eixo_peixes` → `og:title` e `twitter:title`.

**Contado antes de escrever o portão, não suposto: 38 e 38, zero divergência.** O
portão nasce **no dia da primeira mudança de título do eixo** porque é exatamente
esse o momento em que a segunda cópia fica para trás — quem muda o título para
consertar posição de busca está pensando no `<title>`, e o `og:title` mora noutro
arquivo, noutra pasta, sem nada que avise. **É a terceira vez que esta ilha paga a
mesma doença,** e as duas primeiras já tinham portão: o favicon mantido em dois
lugares (casca, seção 2b) e a meta description, que por isso é **gerada** e não
escrita.

- **`ferramentas/teste-titulos-das-duas-fontes.py`** — 160 afirmações, sem rede: as
  duas direções da concordância, o título igual nas duas, o **teto de 65 cobrado na
  bancada** (antes só existia no `teste-voz.mjs`, que precisa de Chromium e de site
  no ar), e o critério da Proposta 1 cobrado **por nome**, para ele não voltar a ser
  esquecido. O registro é lido **em texto**, não perguntando à função do snippet —
  a mesma escolha que `teste-peixes.py` declara, pelo mesmo motivo: a afirmação é
  que os dois **arquivos** concordam.
- **`ferramentas/mutacoes-titulos.py`** — **6 mutações, 6 reprovadas.** As 1 e 2
  mudam o título em **só uma** das duas fontes: o site continua 200, o `<h1>`
  continua certo, e só o `og:title` mente — defeito que nenhuma ronda de HTTP e
  nenhum olho na tela encontra. A 3 estoura o teto por **um** caractere nas duas
  juntas. A 4 é o conserto **pela metade** da Proposta 1. A **5 é a porta dos
  fundos**: a leitura em texto deixa de casar e os dois lados ficam **vazios**,
  portanto **concordes** — as três primeiras afirmações do portão existem só para
  que ela fique vermelha. A 6 tira uma página do JSON sem divergir título nenhum.

### 7. A BANCADA APRENDEU UMA CONVENÇÃO, E ELA TEM DENTE

`regua-robots.py` não casava com nenhuma convenção e o `bancada.py` **a denunciou**
na primeira passada — que é o comportamento certo dele. Régua compartilhada não é
portão (não afirma nada sozinha) e não é produção. A convenção nova: **`regua-*.py`
escapa da denúncia SÓ se algum portão da pasta a importar pelo nome.** A pergunta é
feita aos **arquivos**, nunca a uma lista dentro do `bancada.py` — pelo mesmo
motivo que o resto daquele arquivo não tem lista. **Provado:** uma `regua-orfa.py`
num repositório copiado foi denunciada.

### 8. O QUE ESTA EXECUÇÃO NÃO FEZ, COM O MOTIVO DE CADA UM (18.3)

- **Item 2 do despacho (diagnóstico da 21.5).** O critério de pronto dele exige um
  arquivo escrito **depois** da leitura semanal de **30/09**; hoje é 24/09.
  Escrevê-lo agora seria escrever o diagnóstico **antes** do dado que ele julga —
  a **1.2-b.4** de cabeça para baixo. A hipótese **(a) indexação** segue
  respondida, e ganhou meia medição nova: **52 de 52** URLs do sitemap servindo a
  meta `robots` **sem** `noindex`.
- **Proposta 2 (`/peixes/tetras/` em "Discovered — currently not indexed").** A
  própria proposta diz "nada de código" e "o valor desta proposta é ela não virar
  bloco". O portão novo fechou uma hipótese de graça: a página serve `robots`
  **sem** `noindex`, então **não é a ilha pedindo para não ser indexada**.
- **Proposta 3 (degrau 2, catálogo `/p/MLB…`).** **Retestada, não herdada
  (20.2/20.3):** `www.mercadolivre.com.br` em **403 nas três passadas** —
  `connect_rejected`, política do proxy, não intermitência — contra
  `shopee.com.br` em **200 nas mesmas três**. O critério exige URL de catálogo
  **colhida com os olhos**, e da nuvem não há olhos nem rede.

### 9. O QUE ATRAVESSA ILHA FOI PARA O CANAL DA RAIZ

`dados/despachos.md` ganhou despacho **NORMAL** endereçado à **Sentinela** (e à
Fundação de quem reservar a clubedomosaico): a régua de `noindex` erra ao
atravessar a fronteira entre as ilhas, com a tabela de quem imprime a meta em cada
uma. **Não foi para o `PROMPT.md` de outra ilha porque a seção 3 proíbe editar
arquivo de ilha que não se reservou.**

**E o que ele deliberadamente NÃO decide:** a leitura semanal registrou que na
**clubedomosaico** a página de autor **já está indexada e tomou uma impressão na
posição 1,0**. Esse dado é do Search Console e **não foi desmentido** pelo que se
mediu aqui — lá quem imprime a meta é o snippet, não o núcleo, e a página pode ter
entrado no índice antes de qualquer `noindex`. **Ninguém mediu aquela ilha com a
régua nova**, e é de quem a reservar.

### 10. O QUE MUDOU SEM SER PEDIDO, E POR QUÊ

- **Três entradas do mapa de metas voltaram para a ordem alfabética.** O
  `gerar-metas-descricao.py` ordena por `ordem()`, e as três da categoria `barbos`
  tinham sido inseridas **à mão** no bloco gerado, na leva 9, junto com um
  comentário `/* LEVA 9 ... */` que morava **dentro** da região gerada. Regerar
  alinhou o arquivo ao seu gerador e apagou o comentário. **O conteúdo dos 52 pares
  título/descrição foi comparado antes e depois: só `ciclideos-anoes` mudou.**
  Comentário dentro de bloco gerado é comentário condenado.
- **Uma imprecisão minha, corrigida e anotada:** ao renovar `executando_desde` pela
  **1.1** eu gravei `11:15Z` quando eram ~10h47Z — relógio **à frente**, não atrás.
  Reserva com horário futuro faria a execução seguinte achá-la mais fresca do que
  era. O campo está `null` desde o fecho, então não sobrou efeito; fica escrito
  porque a 1.1 existe justamente para que ninguém confie em campo de relógio sem
  perguntar ao git.

### A BANCADA DESTA EXECUÇÃO

`php -l` nos **11** snippets, sem erro. `teste-seo-tecnico.php` **555** afirmações,
0 falha. `teste-peixes.py` **4.299**, 0 falha. `teste-voz.mjs` TUDO OK (é ele que
cobra que o `<title>` **comece pelo H1** e caiba em 65 — as duas superfícies saem
do mesmo campo, então a mudança as moveu juntas). `teste-arvore.mjs` 0 falha.
`conferir-slugs.py` e `conferir-indice-de-levas.py` verdes. **Os portões novos:**
`teste-robots.py` **21**/0, `teste-titulos-das-duas-fontes.py` **160**/0,
`mutacoes-titulos.py` **6 de 6** reprovadas. **No ar, depois do desembarque:**
`conferir-robots-no-ar.py` **12**/0, `conferir-peixes-no-ar.py` **1.012**/0,
`conferir-datas-e-voz-no-ar.py` **407**/0, `conferir-site-jsonld-no-ar.py` **16**/0.

**A PASSADA COMPLETA DO `bancada.py` NÃO CHEGOU AO FIM, e o motivo não é defeito:**
ela foi iniciada duas vezes. A **primeira** começou antes de eu terminar de editar
os arquivos e eu a **encerrei** de propósito, em vez de deixá-la medir um
repositório que mudava embaixo dela — as mutações copiam a pasta inteira e um alvo
movido no meio dá falha que não é da ilha. A **segunda** rodou com os arquivos já
parados e **tudo o que ela mediu ficou verde**, mas ela não terminou dentro desta
execução: com 36 portões, e as mutações copiando um repositório grande uma vez por
mutação, a passada é de muitas dezenas de minutos. **Encerrei a execução em vez de
segurar a reserva**, porque `foco.md` nomeia esta ilha e, pela 1.2 passo 3, outra
execução que a encontre reservada **para e não pega outra** — segurar a reserva
para assistir a portões verdes é bloquear o arquipélago.

**O que a segunda passada mediu antes de eu fechar, tudo verde:** a régua do
veredito (17 afirmações), `php -l` nos 11 snippets, `conferir-entidades.mjs`,
`conferir-indice-de-levas.py`, `conferir-protecao-funcoes.py`,
`conferir-slugs.py`, `mutacoes-arvore.py` (14/14), `mutacoes-coleta-shopee.py`
(20/20), `mutacoes-datas.py` (12/12), `mutacoes-dimensao.py` (14/14),
`mutacoes-escada.py` (26/26), `mutacoes-ga4.py` (13/13). **Não chegaram a rodar
nela** os `mutacoes-peixes/privacidade/purga-cache/site-jsonld/voz`, os
`teste-*.php` de família alheia a esta mudança, `teste-coleta-shopee.py`,
`teste-datas-schema.py`, `teste-dimensao-imagem.py`, `teste-escada-compra.py`,
`teste-ga4.py`, os `validar-*` — **e os de Chromium** (`--navegador`), que são
dezenas de minutos por desenho. Os portões que **esta** mudança toca foram todos
rodados à mão e estão na lista acima.

### A MEMÓRIA NÃO ESTAVA ALCANÇÁVEL, E ISSO NÃO PAROU A EXECUÇÃO

O `PROMPT.md` manda carregar `/areas/projeto-aquametria.md` e outros quatro
arquivos de memória, e o cabeçalho deste log manda espelhar o resumo lá. **Neste
ambiente não existe diretório de memória** — procurado, não suposto. O próprio
`PROMPT.md` prevê o caso com todas as letras: *"Sem memória, não pare: o estado
está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta."* Foi o que se fez, e
o espelho da memória fica **devendo** para a próxima execução que tiver acesso a
ela — dito aqui em vez de omitido, porque resumo que ninguém escreveu e ninguém
registra como não escrito é a família do "resumo velho lido como fato" da seção 4.

### O PRÓXIMO PASSO DESBLOQUEADO

1. **Uma passada limpa de `python3 ferramentas/bancada.py --no-ar`**, com os
   arquivos parados, para fechar o que esta execução deixou medido pela metade.
2. **A semana da 21.4 virou em 28/09** (a de 21/09 fechou em 3 de 3 com a leva 9).
   Até lá, **nenhuma URL de malha nova** — o que cabe é portão, correção e as cinco
   páginas institucionais da 21.7, se faltar alguma.
3. **30/09/2026 é a data que manda nesta ilha:** a ilha atinge o piso da **21.1**
   (52 URLs, passa das 40; e 21 dias desde a primeira indexação de 09/09), e a
   **21.5** passa a cobrar o diagnóstico escrito das hipóteses **(b) consulta** e
   **(c) SERP** — a **(a)** está respondida. O item 2 do despacho é esse
   compromisso, e o critério dele exige que o arquivo nasça **depois** da leitura
   semanal daquele dia.
4. **A comparação da Proposta 1** (as quatro grafias contra 6,0 / 11,0 / 13,0 /
   35,0) é da leitura semanal de 30/09, em `dados/posicoes.md`. **Amostra fina:**
   uma impressão por linha.
5. **A régua de `noindex` é portável** — três arquivos, trocando a lista de
   contextos e o domínio. A clubedomosaico é a que tem sintoma medido do outro
   lado, e o despacho da raiz espera quem a reservar.


## 2026-09-23 19h16Z–20h32Z — LEVA 9: A NONA CATEGORIA, E O CAMPO QUE FAZ A FONTE RECUSAR COMPANHEIRO EM VEZ DE A PROSA PEDIR (peixes 1.15.0, esquema de espécies versão 6, manifest revisão 110, `/status` conferido na 110; QUATRO URLs novas — `/peixes/barbos/` e as fichas do barbo sumatra, do barbo rosado e do barbo cereja; a ilha vai de 48 para 52 URLs)

**A ESCOLHA DA ILHA: FOCO, E A RESERVA PASSOU NA PRIMEIRA.** `foco.md` nomeia a
aquametria desde 21/09 (1.2), então não houve rotação a aplicar: os cinco
`ESTADO.md` parseiam em `yaml.safe_load`, o da ilha em foco estava com
`executando_desde: null` — que pela 1.1 já significa que não há bloco da Fundação
vivo — e a reserva das 19h16Z entrou no primeiro push. Nenhum branch `claude/*`
pendente e nenhum PR aberto. **Rede pela 20.2, retestada e não herdada:** três
passadas, home em 200 nas três e `/status` na revisão **108**, igual à do
`manifest.json`, nas três.

**O DESPACHO DA SENTINELA DE 23/09 NÃO TINHA ITEM PARA A FUNDAÇÃO**, e isso foi
conferido antes da fila (18.1): os itens 1 e 2 saíram inteiros na execução das
16h16Z de hoje e o item 3 é registro para a ronda seguinte — a chave da Shopee que
caiu no CAPTCHA —, endereçado a quem mede link, não a bloco. **Os dois itens
cumpridos foram APAGADOS do `PROMPT.md` nesta execução, pela 18.4**: ficaram lá,
riscados, por uma execução, e o lugar do detalhe é este arquivo.

### 1. O CRITÉRIO É O NOME, E ELE VOLTA CONTADO EM VEZ DE LEMBRADO

A leva 7 separou os danios e as rasboras pelo NOME que a pessoa digita, e fechou
dizendo que era um critério verificável dentro do banco. A leva 8 teve de
abandoná-lo: quatro registros trazem "acará" e o quarto já era filha de outra
categoria. **Aqui ele volta, e volta com a medição ao lado:** `barbo` casa em
**exatamente três** registros de `nomes_populares_br` no banco de 40 — barbo
sumatra, barbo rosado e barbo cereja.

**O que ele não suporta é ser encurtado, e a distância é de uma letra.** `barb` —
a raiz do gênero antigo, que este banco guarda em `sinonimos_cientificos`
(*Barbus tetrazona*, *Barbus titteya*), e o nome em inglês do cereja — casa em
**quatro**. O quarto é o `cascudo-barbudo`, que é o `ancistrus-cirrhosus`,
declarado em `/peixes/plecos-e-limpa-vidros/` e barrado pelo portão por falta de
`temperatura_C`. Ele não tem nada a ver com esta prateleira, e um critério de
subcadeia o traria para cá.

**Nem a família nem o gênero servem, e as duas contas estão feitas:** Cyprinidae
tem **quatro** elegíveis neste banco e o quarto é o kinguio, de 48,0 cm, que
ninguém vende como barbo — o mesmo erro de trazer peixe demais pela família que a
`ciclideos-anoes` já registrou; e o gênero são três gêneros para três peixes
(Puntigrus, Pethia, Puntius).

**AS QUATRO CONTAGENS QUE O CRITÉRIO PUBLICA SÃO RECOMPUTADAS DO BANCO** pelo
`teste-peixes.py` (item 7 de `medir_categoria_preparada`): os três do nome
inteiro, os quatro da raiz encurtada, os 40 registros do banco e os quatro
Cyprinidae elegíveis, com a afirmação de que o registro que a raiz traz a mais
NÃO está na categoria. Número de banco dentro de frase publicada é o defeito que
esta ilha mais paga; a régua da raiz é a que guarda o motivo de o critério não
poder ser encurtado, e no dia em que outro registro trouxer `barb` no nome popular
a frase é reescrita em vez de envelhecer calada.

### 2. A LINHA MESTRA É DE TEMPERATURA PELA SEGUNDA LEVA SEGUIDA, E NÃO É REPETIÇÃO

Na `acaras` a coluna da temperatura separava **dois** peixes que não se tocavam, e
o terceiro não tinha nada a ver com a conta. Aqui os **três** formam uma escada:
18 a 22 °C no rosado, 20 a 26 °C no sumatra, 23 a 27 °C no cereja. Os dois
extremos não se cruzam em um grau e o do meio alcança os dois — é a primeira
categoria do eixo em que a coluna **ordena** as três linhas em vez de separar
duas.

**E o que a linha mestra NÃO diz é a escolha oposta à da `acaras`.** Lá o porte
ficou fora porque metade dele estava em outra régua (13,7 cm SL contra 45,7 cm
TL). Aqui os três estão na MESMA régua — 5,0 · 7,0 · 14,0 cm TL — e o maior é
quase três vezes o menor, então o porte **poderia** entrar na frase. Ficou fora
por outro motivo: a tabela já o explica sozinha, e **a linha mestra paga o que
falta na tela do concorrente**. Nenhuma das nove páginas da SERP desta consulta
publica temperatura como critério de companhia.

### 3. O DEFEITO QUE ESTA LEVA ACHOU ESTAVA NO AR HAVIA NOVE DIAS, E É PIOR QUE O DO CHÃO DECLARADO

A ficha do **papilocromis**, no ar desde 14/09 pela leva 6, servia **treze**
companheiros de aquário na tabela de "quem divide a mesma faixa de temperatura".
O compêndio daquele registro diz, com todas as letras, que a espécie *"não é
recomendado para o aquário comunitário geral, porque exige água de qualidade
impecável e é mau competidor"*.

**A diferença em relação ao caso do chão declarado, e ela é para pior:** lá a
proibição morava no `observacao` do registro, escrita por quem colheu. Aqui ela
morava na **transcrição da fonte que a própria página cita** — o mesmo texto que
alimenta a tabela "o que as fontes declaram sobre o papilocromis". A página
contradizia, duas seções abaixo, o corpo que ela nomeia como prova.

**Por que nenhum portão viu:** a tabela tem três filtros — interseção das faixas
declaradas, o aquário mínimo do companheiro caber na frente desta ficha, e o banco
não declarar o companheiro **agressivo** — e nenhum dos três alcança uma restrição
escrita em palavras. E o ramo que existia para isso, o da espécie agressiva, olha
o `comportamento` do peixe da própria ficha, que no papilocromis é nulo de
propósito (o compêndio diz "mais agressivos EM ESPAÇO CONFINADO", que é
temperamento condicionado à manutenção).

**A SEGUNDA OCORRÊNCIA IA NASCER NESTA MESMA LEVA**, e é o que torna o campo
inevitável em vez de conveniente: a base científica do barbo sumatra manda **não o
manter com peixe de nadadeira longa**, e este banco **não tem campo para formato
de nadadeira**. A tabela não tem como peneirar isso — então o honesto é **dizer
que não peneira**, e não peneirar calado.

**O CAMPO:** `restricoes_de_companhia` (esquema de espécies **versão 6**, regra
**E23**), com as duas metades do desenho do `chao_declarado_para`: `tipo` de
vocabulário fechado (`nadadeiras-longas`, `comunitario-geral`), porque a tradução
para a língua do leitor mora num mapa só do PHP; e `frase`, a cláusula da fonte
copiada ao pé da letra e conferida como **trecho literal** da referência de uma
fonte que declare o campo em `campos`. O tipo tem de ser sustentado pela cláusula
**por palavra** — `nadadeiras-longas` pede "nadadeira", `comunitario-geral` pede
"comunitario" —, senão qualquer cláusula literal sustentaria qualquer tipo e a
tela falaria de uma coisa que a fonte nunca disse.

**O QUE A PÁGINA PASSOU A FAZER:** publica a recusa **antes** da tabela, com o
nome de quem a declarou e a data, e diz o que a tabela **não** peneira. Antes e
não depois porque a leva 1 já aprendeu, com o mato-grosso, que *"nota não desfaz
tabela — quem lê vê a lista, não a ressalva"*: restrição que chega depois da lista
é a mesma nota com outro nome.

**O CAMPO É OPCIONAL E A AUSÊNCIA NÃO É BURACO:** 24 dos 26 registros com ficha
não têm nenhuma restrição declarada, e restrição que a fonte não declarou não se
inventa. Lista presente e **vazia** é erro, porque lista vazia afirma que a fonte
foi lida e não recusou ninguém, e isso se escreve deixando o campo fora.

### 4. O TETO DE BLOCOS DE PROVA DEIXOU DE SER CONSTANTE, E ISSO É O CONTRÁRIO DE AFROUXAR

A ficha tinha **dois** blocos `aqm-prova` — a atribuição da base e a ressalva das
réguas de lotação — e o teto de dois foi escrito quando dois era tudo o que ela
podia ter. A recusa com dono é o terceiro, e ela **tem** de ser prova: sem a
marca, o nome "FishBase" cairia na camada de voz e o portão dos termos proibidos
reprovaria — corretamente, por um defeito que não existe.

**Subir a constante para três afrouxaria o teto em TODA página.** Ele virou **dois
mais um por restrição declarada NO BANCO**, nos dois portões — `teste-peixes.py` e
`teste-voz.mjs`, que passou a ler o banco de espécies para isso. E o número vem do
**banco**, nunca da página: página que se concede um bloco a mais é justamente o
que o teto existe para pegar. A outra direção — cada restrição do banco na tela e
nenhuma inventada — é cobrada pelo `teste-peixes.py`.

### 5. A CLASSIFICAÇÃO DE SERP DAS QUATRO CONSULTAS, ANTES DE UMA LINHA DE PÁGINA (14.9)

Medida nesta execução, **antes** de a categoria e as três fichas serem escritas, e
escrita inteira em `dados/indexacao.md`. As quatro são **ALVO**. O resumo:

- **`quantos litros para barbo`** (a mãe): top 9 de dois artigos do mesmo blog de
  nicho, quatro páginas de produto de loja, um portal de bicho de estimação, um
  blog e uma loja estrangeira. **O defeito é o SUJEITO trocado, o mesmo da leva 8
  em dose maior:** as nove respostas falam de barbos DIFERENTES — ouro, tinfoil,
  nigrofasciatus, titéia — e devolvem 30 L, 80 L, 96 L e 300 L sem dizer de qual
  peixe é cada número. O tinfoil pede dez vezes o do cereja e os dois saem na
  mesma tela como "barbo".
- **`quantos litros para barbo sumatra`**: 60 L a 100 L sem atribuição, e o
  cardume mínimo como 5 e como 8 a 10 na mesma tela — o mesmo par das nossas duas
  fontes, sem dizer de quem é cada um. Ninguém publica a base de 80 × 30 cm. A
  prova de que a pergunta existe está no próprio top 9, em forma de fórum.
- **`quantos litros para barbo rosado`**: de 75 L para quatro exemplares a 150 L,
  grupo mínimo como 4 e como 6 — **abaixo dos 8 do compêndio**. Ninguém diz que
  este é o barbo de faixa subtropical nem publica a base de 100 × 30 cm. **É a
  SERP em que o sujeito troca DENTRO de um resultado:** um dos nove serve o título
  do barbo rosado num endereço de barbo cereja.
- **`quantos litros para barbo cereja`**: 30 L a 50 L sem atribuição, duas das
  nove de outro mercado, e o pior não é o litro — uma das páginas manda manter
  **"ao menos três indivíduos"**, metade dos 6 a 10 que o compêndio declara.

**Uma coisa que a SERP ensinou e que NÃO virou página:** duas lojas do top
organizam a prateleira como **"barbos e danios"** no próprio endereço. O varejo
junta o que este eixo separa em duas categorias, e as duas continuam separadas
porque o critério de cada uma é verificável no banco e nenhuma espécie cai nas
duas — nenhum dos três barbos traz `danio`, `rasbora` ou `paulistinha` entre os
nomes populares. Fica registrado porque a próxima categoria deste eixo vai
encontrar isso de novo.

### 7. A VERIFICAÇÃO, COM OS NÚMEROS E COM O QUE FICOU DE FORA

**BANCADA SEM REDE, RODADA INTEIRA CONTRA O CÓDIGO QUE FOI PUBLICADO: 33 portões,
0 falha.** Os números que esta leva moveu: `teste-peixes.py` **4.299** afirmações
(eram 4.248 antes de as quatro páginas entrarem); `mutacoes-peixes.py` **100 de
100** reprovadas (eram 95 — as cinco novas são as do campo de recusa);
`testar-validador-especies.py` **41** testes, com os **cinco do E23** pegando o que
prometem; `mutacoes-voz.py` 30 de 30; `teste-voz.mjs` varrendo as **52** páginas
que a ilha publica; `validar-especies.py` 40 registros, 0 erro e os 3 avisos
conhecidos; `conferir-indice-de-levas.py` TUDO OK com a linha da leva 9 na tabela.

**NO AR, NA REVISÃO 110, e a bancada `--no-ar` rodada SOZINHA** — sem nenhum outro
`curl` contra o domínio, que é o que a execução anterior deixou anotado depois de
dois portões caírem por `Connection reset` disputando a rede com ela:
`conferir-peixes-no-ar.py` **1.012** afirmações, 0 falha (eram 904);
`conferir-datas-e-voz-no-ar.py` **407**, 0 falha (eram 368);
`conferir-escada-no-ar.py` 130, 0 falha; `conferir-cache-do-host.py` 55, 0 falha;
`conferir-site-jsonld-no-ar.py` 16, 0 falha; `conferir-privacidade-no-ar.py` 21,
0 falha; `conferir-ga4-no-ar.py` medindo as **52** páginas. As quatro URLs novas
respondem **200** e o `/status` está na **110**, igual à do `manifest.json`.

**O QUE FICOU DE FORA, dito com todas as letras:** a passada `--no-ar` foi
**interrompida** depois dos sete portões do ar, porque os 33 restantes dela são a
bateria offline que já havia rodado inteira, minutos antes, contra este mesmo
código — repeti-la custaria mais meia hora e mediria duas vezes a mesma coisa. E os
**18 portões de Chromium** (`--navegador`) seguem sem rodar por falta do pacote
`playwright` neste ambiente, como nas execuções anteriores.

**O SYNC:** disparado com `forcar=1` às 20h23Z, aplicou a revisão 110 com 20 itens
e 14 aguardando desembarque (os que têm `publicar: false`).

### 8. PRÓXIMA LEVA: NENHUMA DÉCIMA CATEGORIA É POSSÍVEL, E AGORA O EIXO TAMBÉM ESTÁ SEM FICHA ESPERANDO

Varrido por `ferramentas/varrer-categorias-possiveis.py` **depois** da leva: 40
registros, 34 elegíveis, **29 com ficha própria**, **5 sem categoria nenhuma** —
kinguio, botia-palhaço, arco-íris boesemani, peixe-lápis e otocinclo. **Nenhuma
família chega a três** (cinco famílias de um registro cada) e o único agrupamento
por nome que alcança três é `peixe`, que não é prateleira nenhuma — a própria
ferramenta o chama de PISTA.

**E a novidade em relação à leva 8: nenhuma categoria no ar tem elegível sem
ficha.** Os 5 sem ficha são exatamente os 5 sem categoria. O eixo `/peixes/` só
cresce com **coleta** — e o teto da 21.4 desta semana está **gasto, 3 de 3** (as
levas 7 e 8 em 22/09 e esta em 23/09).

## 2026-09-23 16h16Z–17h12Z — O DESPACHO DA SENTINELA DE 23/09 SAI INTEIRO: A HOME GANHA O NÓ `WebSite`, E A DÍVIDA DOS 39 LINKS SEM FICHA CAI PARA 14 (casca 1.11.0, manifest revisão 108, `/status` conferido na 108; NENHUMA URL nova — seguem 48 — e NENHUMA leva do teto da 21.4 gasta)

**Não houve escolha de ilha:** o foco é a Aquametria desde 21/09 (`foco.md`), e a 1.2 suspende a rotação inteira. Houve escolha de *bloco*, e ela também estava feita: a 18.5 diz que na dúvida entre fechar despacho e começar bloco novo, fecha o despacho — e havia um aberto, escrito pela ronda de hoje às 14h52Z. Pela 18.2 ele sai inteiro, não um item por execução.

**Reserva pela seção 1, passo 5:** os cinco `ESTADO.md` parseiam em `yaml.safe_load` e os cinco estavam com `executando_desde: null`, que pela 1.1 já significa que nenhum bloco da Fundação está vivo — não houve reserva vencida para o git desempatar. O último commit na pasta desta ilha era das 14h53Z, da **Sentinela**, e commit de ronda não reserva nada (1.1, correção de 13/09). Reserva escrita às 16h16Z e aceita no primeiro push. Nenhum branch `claude/*` pendente e nenhum PR aberto. **Rede pela 20.2, retestada e não herdada:** `aquametria.com.br` em 200 nas três passadas, `www` em 301 nas três.

### 1. ITEM 1 — A HOME ERA A ÚNICA PÁGINA DA ILHA SEM DADO ESTRUTURADO NENHUM

A ronda mediu **zero** ocorrência de `application/ld+json` e **zero** de `schema.org` na home, contra as outras 47 URLs. A causa que ela nomeou está certa e é a parte que importa: **não era a trilha faltar** — a 16.3 manda mesmo não haver breadcrumb na home — e sim **não existir nenhum outro tipo de JSON-LD na ilha**. Os oito emissores do repositório são `BreadcrumbList`, `WebApplication`, `Article`, `FAQPage` e `CollectionPage`, e os cinco dependem de uma página interna. A página mais linkada da ilha, e a porta dela para superfície generativa (seção 5, regra de primeira classe), não tinha o que dizer sobre si mesma.

Nasce `aquametria_casca_site_jsonld()`: `WebSite` com `name`, `url`, `inLanguage`, `description` e `publisher` `Organization`, no `wp_head` na prioridade 22.

**SÓ NA HOME, e isso é regra e não economia.** `WebSite` e `Organization` são os nós de **identidade** do site inteiro; repetidos em 48 páginas não acrescentam informação e passam a falar por cima do nó da página. O portão mede as duas direções, e a segunda não é preciosismo: `is_front_page()` é a única coisa que separa os dois mundos, e uma guarda que sempre responde `true` passa despercebida por qualquer teste que só olhe a home.

**SEM `potentialAction`/`SearchAction`, e é decisão registrada.** Esse nó promete que o site tem caixa de busca própria e que a URL declarada devolve resultados. Esta ilha não serve busca ao visitante. Declará-lo seria publicar uma promessa que a página não cumpre — a família de defeito que a seção 8 mais cobra. Uma das 14 mutações o acrescenta, e o portão reprova.

**A DESCRIÇÃO É A CONSTANTE QUE JÁ EXISTIA**, a mesma `TAGLINE_CURTA` com que o núcleo monta o `<title>` da home. Uma terceira descrição da ilha, escrita só para o robô ler, é a família do "parece dado": ninguém a lê na tela e ninguém a mantém.

#### A bateria de mutações achou dois buracos no portão recém-nascido, no dia em que os dois nasceram

Isto é o achado de método desta execução, e ele vale mais que o conserto. `teste-site-jsonld.php` passou verde de primeira, com 22 afirmações. Aí a bateria rodou, e **2 das 14 mutações sobreviveram**:

- **A afirmação "o conteúdo do nó não muda com o contexto da página" era verdadeira por construção.** Ela lia `$a` sem montar mundo nenhum — e o mundo que sobrava do render anterior já era o de página interna —, então `$a` e `$b` saíam do **mesmo** mundo. Uma afirmação que compara uma coisa com ela mesma fica verde para sempre. Os dois mundos passaram a ser montados, um para cada lado.
- **A mutação do "conserto pelo caminho errado" estava INERTE.** Ela mexia num contador da trilha que, para a home, não produzia breadcrumb nenhum — então provava zero. Reescrita para o defeito plausível de verdade: alguém "fecha" o item 1 fazendo a home emitir um `BreadcrumbList` de um degrau só. É o conserto tentador, porque a medição crua do despacho ("a home serve `ld+json`") ficaria verde na hora, publicando trilha na única página que não tem degrau nenhum. **A afirmação que pega isso não é a presença do nó novo: é a AUSÊNCIA do nó velho, no mesmo render.**

14 de 14 depois dos dois consertos.

#### E o portão do ar reprovou o mundo de hoje ANTES do conserto

`conferir-site-jsonld-no-ar.py` escreve o critério que o **próprio despacho** declarou, com `Accept-Encoding: identity` e quebra de cache. Rodado contra o site antes do desembarque: **4 falhas de 11** — reproduziu o defeito que a ronda relatou, medido por outra pessoa e por outro caminho. Depois da revisão 108: **16 afirmações, 0 falha**, com a terceira direção (o nó de identidade é da home e de mais ninguém) conferida numa amostra de seis internas, que servem `BreadcrumbList` e não servem `WebSite`.

### 2. ITEM 2 — A TRAVA QUE IMPEDIA O CONSERTO ERA A PRÓPRIA FERRAMENTA DE COLETA

A contagem que o critério de pronto pede saiu de **39 para 14**. Mas o caminho até ela é o que esta entrada precisa registrar, porque o despacho não tinha como saber onde o obstáculo estava.

`coletar-shopee.py` recusava gravar ficha em registro que já tivesse `afiliado.url`, com um argumento bom e escrito em prosa no próprio código: trocar o link apagaria a atribuição do `sub_id_2` daqueles links feitos à mão, que é a única coisa que o painel da Shopee sabe dizer sobre qual calculadora vende. **O argumento é falso justamente nos 39**, e a prova está no banco: eles são `intestavel: true`. Pela 25.4-b, não é um link conferido que se preserva — é um link cuja saúde é **desconhecida e permanecerá desconhecida**. A trava de atribuição tinha virado trava de conserto.

**A pergunta certa não é se existe link; é se o par é DEMONSTRÁVEL.** Com `url` e `url_produto` o registro afirma para onde o link vai e alguém consegue conferir. Sem o segundo campo ele não afirma nada.

**E O PAR TEM DE TROCAR JUNTO — esta é a metade que passa despercebida.** Gravar o `url_produto` da oferta que a escada casou ao lado do `url` velho seria afirmar que os dois apontam para o mesmo produto, e **ninguém mediu isso**: de um `s.shopee.com.br/XXXX` não se chega à ficha sem clicar, e a 25.4 proíbe clicar. Seria fabricar a aparência de um par conferido, **que é pior que o buraco de hoje — o buraco está escrito, a aparência não**. E o que se perde na troca é zero: o `sub_id_2` novo sai da MESMA tabela de onde os antigos saíram.

**O que custou:** 33 fichas casaram (18 no degrau 1, 15 no degrau 2), 8 delas em registros que já tinham o par e por isso foram preservadas, 25 nos registros que o despacho nomeou. A amostra foi lida com os olhos antes de gravar, como a 25.3 manda — os 25 casamentos contra marca, modelo e variante, com atenção aos quatro pares 110/220 da Maxxi, que são o caso em que o título do vizinho passa por certo. Os quatro pares trouxeram a voltagem no título e bateram.

**OS 14 QUE SOBRARAM SÃO DUAS DÍVIDAS OPOSTAS, e só o motivo escrito as separa: 10 devolveram ZERO RESULTADO em todos os degraus da escada** — não estão anunciados, nenhuma trava foi acionada, e isso só muda quando o mercado mudar — **e 4 tiveram candidatos BARRADOS** pelas travas da 25.7 e da variante, que pode mudar com uma trava melhor ou com o registro de variante que falta no banco. Contadas juntas viram um número que não diz o que fazer. Os cinco Roxin HT-1300 estão entre os 10: a escada inteira devolveu zero.

**E O MOTIVO VELHO MANDAVA NÃO TENTAR.** Os 39 carregavam, desde 13/09, uma prosa dizendo que a recuperação pelo título fora *"TENTADA E RECUSADA"* porque a busca da Shopee serve casca de JavaScript. Era verdade naquele dia e deixou de ser três dias depois, quando a Open API entrou. O campo passou a guardar **duas** coisas com vidas diferentes, separadas por um marcador: a **causa** (por que a URL crua se perdeu — não muda nunca) e a **última tentativa** (a escada de hoje, degrau a degrau, com a recusa de cada um). Sem a separação, ou a prosa cresce sem fim, ou a causa é apagada pela tentativa de hoje.

### 3. A SEGUNDA METADE DO ITEM 2 NÃO SAIU AO PÉ DA LETRA, E ESTÁ ESCRITO POR QUÊ

O despacho manda `afiliado.conferido_em` sair de todo registro que continuar `intestavel: true`, com o argumento — **correto para o nome que o campo tinha** — de que item que não pode ser conferido não tem data de conferência.

Fui ao `dados/esquema-produtos.json` antes de apagar, e o campo **nunca foi a data da ficha**: *"A data em que o PISO deste item foi escrito ou reconferido"*. O piso é o `url_busca`, ele é conferível nos 78 e estava conferido nos 78. Apagá-lo teria **destruído dado verdadeiro** e, pior, teria **quebrado a idempotência** de `gerar-busca-de-produto.py`, que reescreve o campo com a data de HOJE quando ele falta: o piso de 39 itens se moveria sem ninguém decidir. Não é hipótese — é a mutação 26 de `mutacoes-escada.py`, que existe exatamente para reprovar isso e que eu vi reprovar nesta passada.

O despacho deixou a saída escrita: *"se for útil guardar a data da última tentativa, ela se chama outra coisa"*. **Ela é útil e agora se chama outra coisa:** `piso_conferido_em`, nos 78 registros, no esquema e no gerador. Nenhuma ferramenta pode mais contá-lo como ficha conferida — que era a preocupação do item — e nenhum dado verdadeiro morreu. **O defeito real era o nome**, e o nome é o que a 26.1 chama de campo que não declara de onde veio: `afiliado.conferido_em`, sentado ao lado de `afiliado.url`, não tinha como ser lido de outro jeito.

### 4. O DEFEITO QUE A BANCADA ACHOU EM MIM: DUAS FONTES PARA O MESMO DADO

A coleta reescreveu 25 links no banco, e os catálogos que a C3, a C5 e a C15 **embutem** nos snippets continuaram servindo os links velhos. `mutacoes-escada.py` reprovou com **16 falhas**, dizendo que quatro cartões apontavam para uma URL *"que não é ficha nem piso de nenhum item do banco"*.

Isto não é novidade nesta fábrica — é a cicatriz que o próprio `atualizar-manifest.py` documenta sobre os títulos do front matter, com outra roupa. O site não lê o repositório em tempo de execução, então o banco viaja **dentro** do snippet, e os `gerar-catalogo-*.py` existem para impedir as duas cópias de divergirem. Os três foram regerados e a bateria voltou a **26 de 26**. **O que faltou foi um portão que ligasse as duas coisas**: quem mexe no banco tem de regerar os catálogos, e hoje isso é memória de quem executa, não trava. Fica nomeado como dívida.

### 5. E A REGRA NOVA ESTAVA INALCANÇÁVEL POR PORTÃO

A escolha entre preservar a ficha do banco e reescolher o par é a decisão mais cara do coletor, e ela nasceu como um `if` dentro do `main()` — onde afirmação nenhuma chega. A bancada media o **casamento** e não media isto. Virou `preserva_ficha_existente(af)`, com 4 afirmações em `teste-coleta-shopee.py` (159 no total) e **duas** mutações, uma por direção: a que faz a pergunta voltar a ser *"existe link"* — reproduzindo o mundo em que a dívida dos 39 era imortal — e a que faz a preservação parar de acontecer, jogando fora a atribuição de um link que estava bom. **Sem as duas, uma afirmação só ficaria verde numa função que nunca preserva nada.** 20 de 20.

### 6. O QUE SUBIU PARA O CONTRATO

A 25.4-b dizia, desde 13/09, que a saída para estes 39 era *"reescolher pelo feed"* — e o feed foi aposentado pela própria 25.6 em 16/09. A ponta velha foi corrigida e o que esta passada aprendeu virou quatro regras para toda ilha: **25.4-b.1** par perdido se reescolhe inteiro, nunca remendado; **25.4-b.2** "já tem link" não preserva, "já tem par" preserva; **25.4-b.3** motivo envelhece calado, e motivo velho manda não tentar; **25.4-b.4** "não casou" tem duas causas que parecem uma.

### 7. VERIFICAÇÃO

Bancada sem rede: **33 portões, 0 falha**. `validar-produtos`: 78 produtos, 39 cotações, **0 erro**, 8 avisos (os conhecidos). `mutacoes-site-jsonld` 14 de 14, `mutacoes-coleta-shopee` 20 de 20, `mutacoes-escada` 26 de 26, `teste-coleta-shopee` 159 afirmações 0 falha, `teste-site-jsonld` 22 afirmações 0 falha. **No ar, na revisão 108:** bancada `--no-ar`, **40 portões**. `conferir-site-jsonld-no-ar` 16/0, `conferir-escada-no-ar` 130/0, `conferir-cache-do-host` 51/0, `conferir-datas-e-voz-no-ar` 368/0, `conferir-peixes-no-ar` 904/0, `conferir-privacidade-no-ar` e `conferir-ga4-no-ar` aprovados.

**E DOIS PORTÕES REPROVARAM POR REDE ANTES DE PASSAREM, o que vale anotar porque a causa não era o site.** `conferir-datas-e-voz-no-ar` e `conferir-peixes-no-ar` caíram com `Connection reset by peer` — e são exatamente os dois que abrem mais URLs (368 e 904 afirmações sobre as 48 páginas). Eles rodaram enquanto eu disparava outros `curl` contra o mesmo domínio: o host cortou a conexão por concorrência, não por defeito. Rodados **sozinhos**, na mesma revisão e minutos depois, os dois passaram com zero falha. É a 20.2 ao pé da letra — falha de rede só vira bloqueio depois de repetir —, e a leitura que fica para a próxima execução é mais estreita: **não rode outra coisa contra o site enquanto a bancada `--no-ar` estiver aberta**, senão os dois portões mais caros da ilha reprovam por uma causa que não é a que eles medem. O `/status` conferido na 108, igual à do `manifest.json` — e o Sync leu 107 nas duas primeiras chamadas porque a cópia dele vem de cache de CDN, que é a armadilha que a 27.3 nomeia; a terceira, três minutos depois, aplicou a 108.

### 8. PRÓXIMO PASSO DESBLOQUEADO

**A leva 9 continua sendo o próximo bloco de malha** — a categoria de barbos mais três fichas, 4 URLs, a terceira e última leva desta semana pela 21.4 —, e ela está destravada desde a preparação de 13h17Z: são 3 barbos elegíveis, o mínimo exato do 16.5. Nada do que esta execução fez a atrasa: correção não consome a vez de um bloco de construção (18.2), e nenhuma URL nasceu aqui.

**Aberto:** os 14 itens sem ficha, cada um com a escada de hoje escrita; a falta de um portão que cobre a regeração dos catálogos embutidos quando o banco muda; os 18 portões de Chromium sem rodar por falta do pacote `playwright`; e T6 (prospecção do widget) parada pelo egresso.


## 2026-09-23 13h17Z–14h05Z — PREPARAÇÃO DA LEVA 9: OS BARBOS GANHAM BANCO, E A CONTA QUE DECIDE SE A MALHA PODE CRESCER DEIXA DE SER FEITA DE CABEÇA (banco de espécies de 39 para 40 registros, catálogo embutido de 32 para 34, peixes 1.14.0, manifest revisão 104, `/status` conferido na 104; NENHUMA URL NOVA — seguem 48 — e NENHUMA leva do teto da 21.4 gasta)

**O BLOCO ERA O ÚNICO QUE A FILA DESTE EIXO AINDA TINHA, e quem o nomeou foi a
leva 8 na véspera.** Ela fechou medindo que nenhuma nona categoria era possível e
escreveu o caminho mais curto com dois passos contados: *"o barbo sumatra é
elegível, o **barbo rosado** (`pethia-conchonius`) está a UM campo — `duas fontes
distintas` —, e **não existe um terceiro barbo no banco**"*. Os dois passos
fecharam nesta execução.

### 1. POR QUE ESTE BLOCO E NÃO OUTRO, com as quatro portas conferidas antes

O foco é esta ilha (`foco.md`, desde 21/09), então não houve escolha de ilha.
Houve escolha de bloco, e as outras portas da fila estavam fechadas por motivo
que não é meu para abrir:

- **`/peixes/` (T4):** sem coleta, nenhuma nona categoria — medido pela leva 8 e
  reconferido aqui **por ferramenta** (adiante).
- **`/guias/` (T5 e a pauta da seção 17):** o `ARVORE.md` seção 5 diz que é a
  `pauta.md` que enche as três categorias de guia e que ela *"entra na fila desta
  ilha antes de qualquer leva de malha nova"* — e a **17.1 dá a pauta à rotina
  Pauta das ilhas, não à Fundação**: *"a rotina Pauta das ilhas (terças, no
  computador do Raphael) descobre e ranqueia temas e grava `ilhas/<ilha>/pauta.md`
  pelas mãos. A Fundação escreve os artigos"*. Não existe `pauta.md` nesta pasta,
  então não há artigo para escrever. **Isto não é despacho e não é defeito: é uma
  camada da fila que depende de uma rotina que ainda não rodou nesta ilha.**
- **`/equipamentos/`:** o `ARVORE.md` seção 7 item 4 a trava até o cluster de
  aquecimento estar **indexado**.
- **`/calculadoras/aquecimento-e-luz/`:** exige MOVER duas URLs publicadas, que a
  12.1 e a seção 6 do `ARVORE.md` proíbem.

Rede conferida antes de trabalhar (20.2): `https://aquametria.com.br/` em **200**
em duas passadas.

### 2. A COLETA, e ela é de DOIS TIPOS diferentes no mesmo bloco

**`Puntius titteya` (barbo cereja) entrou NOVO, com dois corpos de fonte e ZERO
conflito** — e o zero é o achado, não a ausência dele. As duas fontes **não se
cruzam em campo nenhum**: a base científica declara porte, faixa térmica, pH e
dureza e diz, com todas as letras, que a seção de aquário dela **não** traz número
de grupo nem tamanho mínimo; o compêndio declara a base (60 × 30 cm) e o grupo (6
a 10). Registro sem conflito neste banco costuma ser registro com fonte fraca;
aqui é o contrário, e a transcrição de cada fonte diz por quê.

**`pethia-conchonius` (barbo rosado) saiu de UM corpo de fonte para DOIS**, e com
isso saiu de `parcial` — que **barra** a ficha pelo `minimo_para_sugerir` — para
`conflito`, que não barra. Os dois conflitos que nasceram estão declarados:

- **`comprimento_minimo_aquario_cm`: 80 (base científica) contra 100 (compêndio).**
  As duas fontes medem coisas diferentes com o mesmo número: uma declara só a
  frente, a outra declara a base inteira. Conservador **100**, pela E9.
- **`cardume_minimo`: 5 contra 8.** É o **mesmo par de números, nas mesmas duas
  fontes**, que o barbo sumatra já carrega desde 09/09 — a terceira vez que este
  banco encontra essa divergência, e a primeira em que ela aparece **duas vezes
  dentro da mesma categoria**. Conservador **8**.

### 3. O QUE NÃO VIROU CONFLITO, E É A DECISÃO MAIS IMPORTANTE DESTA COLETA

A base científica publica **14,0 cm TL** como máximo do barbo rosado; o compêndio
publica que *"algumas formas chegam a 90 a 100 mm, mas a maioria está adulta com
65 a 75 mm"*. É tentador chamar isso de conflito de porte — e seria **errado**,
porque o compêndio **não diz se mede SL ou TL**, e comparar comprimento sem a
cauda com comprimento com ela é exatamente o que a leva 7 proibiu (*"número de
medidas diferentes não se compara"*). Então os dois números convivem no registro
em lugares diferentes: o campo carrega o 14,0 cm **com a medida dele**, e a
`observacao` carrega a frase do compêndio e a ordem para a ficha — **publicar o
número da fonte com a medida E dizer que porte máximo registrado não é porte
esperado em cativeiro**, senão a C8 dimensiona para um peixe que ninguém tem.

### 4. O QUE A COLETA DESTRAVOU, contado: A NONA CATEGORIA É POSSÍVEL

São **3 barbos elegíveis** — sumatra, rosado e cereja —, o **mínimo exato do
16.5**, pela terceira leva seguida deste eixo. O que a leva 9 ainda tem de fazer é
o que as levas 7 e 8 fizeram na mesma execução da leva: `criterio` e
`linha_mestra` escritos **contra a tabela que a página serve** e a SERP das quatro
consultas classificada pela 14.9 **antes** de escrever uma linha. **Este bloco não
escreveu nenhum dos dois de propósito** — a regra que a leva 5 deixou é que texto
de categoria escrito antes da leva é afirmação que ninguém mediu.

**O critério desta categoria NÃO pode ser a família, e agora isso está contado em
vez de suposto:** Cyprinidae tem **quatro** elegíveis sem categoria, e o quarto é
o **kinguio**, que nenhuma loja vende como barbo. É o mesmo erro que a
`ciclideos-anoes` registrou de trazer peixe demais pela família.

**E a tabela já tem uma linha mestra esperando quem a medir:** as três faixas
térmicas são 18 a 22 °C (rosado), 20 a 26 °C (sumatra) e 23 a 27 °C (cereja) — **a
do rosado termina antes de a do cereja começar**, e o sumatra é o único que encosta
nas duas. Segunda categoria seguida em que a coluna que decide é a temperatura, e
aqui ela é uma **escada de três degraus** em vez do par que a `acaras` achou. E, ao
contrário dos acarás, os três portes estão **na mesma régua** (5,0 · 7,0 · 14,0 cm
TL), então comparar porte aqui é legítimo.

### 5. A QUARTA LISTA ESCRITA À MÃO DESTA FAMÍLIA MORREU — e a nova régua foi conferida contra o passado

As levas 7 e 8 escreveram, cada uma no seu fecho, **a mesma varredura à mão com
números diferentes**: 31/23/8 na leva 7, 32/26/6 na leva 8. É a conta que decide
se este eixo pode crescer, e ela era feita de cabeça, sem deixar como refazer.
Agora é `python3 ferramentas/varrer-categorias-possiveis.py . --gravar`, com série
em `dados/cobertura-de-categorias.md`.

**A prova de que ela mede o mundo e não a si mesma:** rodada contra o banco do
commit **anterior** a esta execução, ela devolve **32 elegíveis, 26 com ficha, 6
sem categoria, Cyprinidae faltando 1** — a conta da leva 8, número por número.
Rodada contra o banco de hoje: **34 elegíveis, 26 com ficha, 8 sem categoria, e o
grupo `barbo` alcançando o mínimo do 16.5**.

**Ela CONTA e não decide, e o primeiro dia dela já mostrou por que isso importa.**
Ela agrupa por família (a conta das duas levas) e por nome popular compartilhado
(o critério que a `danios-e-rasboras` usou), e chama as duas de **PISTA**. O
agrupamento por nome devolve `peixe` com três elegíveis — kinguio, arco-íris
boesemani e peixe-lápis —, que não é prateleira nenhuma. **Uma ferramenta que
escolhesse o critério estaria inventando a afirmação central da página**, e por
isso o cabeçalho dela diz, com o nome das oito categorias, que nenhuma usa o
critério da anterior.

A régua de elegibilidade está escrita **dentro** dela e o esquema é lido só para
conferir que as duas listas dizem a mesma coisa — a mesma decisão do
`gerar-catalogo-especies.py`, e pelo mesmo motivo: se ela importasse a lista,
apagar um campo no esquema faria as duas metades errarem juntas.

### 6. O QUE MUDOU NA TELA SEM NASCER URL NENHUMA

O catálogo que viaja dentro do snippet foi de **32 para 34 espécies** (o banco não
é lido em tempo de requisição), então a contagem que a seção `/peixes/` publica
sobre o próprio banco mudou, e os dois barbos passaram a poder aparecer na lista de
quem divide a mesma água das fichas vizinhas. **Nenhuma URL nova, nenhuma leva
gasta:** o teto da 21.4 segue em **2 de 3** nesta semana, que zera em 28/09.

### 7. `teste-peixes` FOI DE 3719 PARA 3715 AFIRMAÇÕES, e a causa foi medida em vez de suposta

Régua que mede MENOS depois de uma mudança é exatamente o defeito que esta ilha
mais paga, então as duas saídas foram diferenciadas linha por linha. As quatro
afirmações que sumiram são **as quatro que falavam do `pethia-conchonius` como
BARRADO** — o motivo gravado, a tradução dele para língua de gente, a ordem da
lista de barrados e o nome científico dele viajando junto. Ele deixou de ser
barrado porque entrou no catálogo. **Nada parou de ser medido; o sujeito saiu do
conjunto.**

### VERIFICAÇÃO

**Sem rede, num comando só:** `python3 ferramentas/bancada.py` → **APROVADO: 31
portões, 0 falha**, com a régua do próprio veredito medida antes (17 afirmações) e
`php -l` nos 11 snippets. Um a um, do que importa a este bloco:
`validar-especies` **40 espécies, 0 erro, 3 avisos** — os três conhecidos (o E15 do
guppy e os dois E21 do disco e do apistogramma), e os três foram medidos **iguais
no banco do commit anterior**, o que prova que este bloco não acrescentou aviso
nenhum; `testar-validador-especies` **36 testes, 0 falha**; `teste-peixes`
**3715/0** (eram 3719 — a causa está na seção 7 acima); `mutacoes-peixes` **95 de
95 reprovadas**; `teste-escada-compra` **703/0**; `mutacoes-escada` 26 de 26;
`teste-ga4` **760/0**; `teste-voz` nas 48 páginas; `teste-arvore`,
`teste-datas-schema` 102/0, `teste-dimensao-imagem` 42/0, `teste-seo-tecnico`
519/0, `teste-apelidos` 59/0, `teste-coleta-shopee` 153/0, `mutacoes-coleta-shopee`
18 de 18, `mutacoes-voz` 30 de 30, `conferir-entidades`, `conferir-slugs`,
`conferir-protecao-funcoes` e `conferir-indice-de-levas` limpos; `validar-produtos`
com o aviso V20 conhecido.

**NO AR, depois do Sync (revisão 104, conferida no `/status`):**
`conferir-peixes-no-ar` **904 afirmações, 0 falha** (eram 906);
`conferir-datas-e-voz-no-ar` **368/0**; `conferir-escada-no-ar` **130/0** — 19
cartões, 12 pela ficha, 7 pelo piso, 0 sem saída; `conferir-privacidade-no-ar`
**21/0**; `conferir-cache-do-host` **51/0**, com atraso de 0 s até o canônico
concordar (orçamento de 360 s); `conferir-ga4-no-ar` limpo, com a nota conhecida do
`google-site-kit` nas 48 páginas.

**As duas afirmações que o ar perdeu são as mesmas quatro da bancada, vistas de
fora**, e foram lidas no HTML servido em vez de supostas: o bloco "as espécies que
o banco tem e esta seção não publica" foi de **7 para 6 nomes**, e o barbo rosado
saiu dele. Cada barrado vale duas afirmações naquele portão — o nome uma vez só e a
causa em língua de gente.

**E a contagem nova foi lida na própria página, não no código:** `/peixes/` serve
*"São 34 espécies de água doce com o mínimo declarado por fonte com nome e data"* e
*"O banco desta ilha guarda 40 registros de espécie, e 34 deles têm o mínimo
declarado que as tabelas acima exigem"*.

**O que ficou medido e NÃO foi consertado (18.3):** a dívida das ferramentas fora
do `manifest.json` **cresceu em dois** com este bloco —
`ferramentas/varrer-categorias-possiveis.py` e `dados/cobertura-de-categorias.md`,
os dois nomeados pelo `atualizar-manifest.py` em toda passada. Fica nomeada aqui em
vez de virar promessa, como o fecho de 22/09 fez. E os **18 portões de Chromium**
seguem sem rodar nesta nuvem desde 14/09/2026, por falta do pacote `playwright`.

### ITENS ESPERANDO LINK DE AFILIADO (item 5 do despacho da Sentinela de 13/09)

**Este bloco não tocou em produto nenhum.** Seguem os números do fecho anterior:
zero itens sem `url_busca` encurtada, zero sem saída de compra, 47 de 78 com ficha
e 41 de 78 com foto.

### PRÓXIMO PASSO DESBLOQUEADO

**A leva 9 pode nascer, e ela é a primeira em duas passadas que não depende de
coleta:** `/peixes/barbos/` mais as fichas do barbo sumatra, do barbo rosado e do
barbo cereja — quatro URLs, dentro do teto de 10 por leva, e ela é a **terceira e
última leva desta semana** pela 21.4. Quem a escrever decide o `criterio` (e o
kinguio fica fora, contado), escreve a `linha_mestra` contra a tabela e classifica
a SERP das quatro consultas antes de escrever uma linha.

**Sem coleta e sem gastar leva:** `T6` (prospecção do widget) segue sendo a única
alavanca de link do projeto e segue parada — e o egresso desta nuvem devolve
`000` para domínio de loja, medido nesta execução, então uma lista de prospecção
feita daqui não consegue conferir no ar o site de nenhuma das lojas. Quem a fizer
declara esse limite em vez de o esconder.

**A camada `/guias/` continua esperando quem ela espera:** a `pauta.md` da seção
17, que é da rotina Pauta das ilhas e não da Fundação. Enquanto ela não existir,
as três categorias de guia ficam com uma filha cada — abaixo das três que o 16.5
exige — e nenhuma leva de guia pode nascer.

## 2026-09-23 10h17Z–12hZ — T3(f): A OPEN API DA SHOPEE CHEGA À ILHA, E OS 78 ITENS PASSAM A RENDER COMISSÃO (esquema de produtos versão 12, C3 1.7.0, C5 1.7.0, C12 1.5.0, C15 1.6.0, manifest revisão 100; NENHUMA URL NOVA — seguem 48 — e NENHUMA leva gasta do teto da 21.4)

**O BLOCO ERA O MAIOR PARADO DA FILA, e quem o nomeou foi a leva 8 na véspera**,
ao conferir a seção 25 do contrato antes de fechar. A 25.6 mediu em 16/09, com
chamada real, que o `productOfferV2` devolve o `offerLink` já encurtado; a
25.2-b (18/09) declarou que link que não rende comissão *"deixou de ser
aceitável como padrão"*. **Esta ilha esteve fora do foco de 16 a 21/09 e herdou
as duas regras sem nunca aplicar nenhuma.** O foco voltou em 21/09 e este é o
primeiro bloco que paga essa dívida.

### 1. O QUE A LEVA 8 MANDOU CONFERIR ANTES DE COLETAR

`open-api.affiliate.shopee.com.br` **está** na lista de domínios permitidos
deste ambiente: `200` em quatro passadas. Não virou despacho para o Raphael — a
25.6 avisa que essa lista é passo dele e que nenhuma rotina a alcança, e por
isso a conferência vinha antes de qualquer coleta.

A credencial saiu do documento privado `arquipelago-credenciais` do Drive,
entrou no processo **só como variável de ambiente** e não existe em arquivo, em
log, em commit nem neste registro. `git diff --cached` varrido por `AppID` e por
`Senha` antes de cada um dos três pushes: zero ocorrência.

### 2. DUAS CAMADAS DE RISCO MUITO DIFERENTE, E É O QUE A PRÓXIMA ILHA COPIA

**Camada 1 — o piso encurtado.** Não tem casamento nenhum: a busca já estava
escolhida e conferida desde 13/09 em `url_busca_produto`, e encurtá-la é uma
chamada de rede sobre uma URL que ninguém precisa identificar. **78 de 78, zero
falha**, com `sub_id_1=aquametria` e o `sub_id_2` da calculadora. É ela que
fecha a 25.2-b, e ela vale para os 78 sem exceção e sem julgamento.

**Camada 2 — a ficha e a foto.** Aqui mora o risco, e ela ficou em **33 de 78**,
com **9 fotos novas**, todas com largura e altura lidas nos **bytes do arquivo**
(cabeçalho JPEG, PNG ou WebP), nunca supostas. 45 sem ficha é **medição honesta
e não falha**: casamento errado no banco é pior que casamento nenhum, porque
parece dado.

**NENHUMA LINHA DE SNIPPET MUDOU**, exatamente como o despacho do Raphael de
14/09 previu. Os catálogos regerados trazem `busca_afiliada: true`, e a casca
sozinha vira o `rel` de `nofollow` para `sponsored` e o selo do cartão de
"busca na Shopee, sem comissão" para "busca patrocinada".

### 3. A ARMADILHA DESTA ILHA NÃO É NENHUMA DAS CINCO DA 25.7

As cinco foram medidas na Robometria, que vende **peça**. Esta ilha vende o
**aparelho**, e o aparelho vem em linha: o Roxin HT-1300/Q3 existe em 25, 50,
100, 200 e 300 W. O título do anúncio traz a marca certa, a linha certa e a
potência **do vizinho**.

Não é hipótese: a ilha já pagou por isso no ar. O `ESTADO.md` registra, em
07/09, que `ista-i-401-45` entrou porque *"o anúncio da Shopee é da luminária de
45 cm, não a de 60 do banco — colar o link no registro errado faria a C15
prometer 3717 lm e entregar 810"*. E o esquema já proibia, **em prosa**, na
lista `afiliado.regras`. **Prosa não conta e prosa não barra anúncio** — mesma
família do `afiliado.intestavel` (14/09) e do `chao_declarado_para` (22/09).

**O PORTÃO SAI DO BANCO, NÃO DE LISTA ESCRITA À MÃO**, e são três regras:
- a medida **conflitante** barra sempre (título que diz 300 W para o registro de
  25 W não está calado: está dizendo outra coisa);
- a medida **ausente** barra só onde ela discrimina — onde irmãos dividem o
  mesmo código base. Onde o código já é único, como no SunSun HW-303B, não: o
  varejo anuncia canister pela **vazão** e nunca pelo consumo, e cobrar watt ali
  reprovaria o anúncio certo;
- e as palavras que, depois do código, nomeiam **outro produto do banco** saem
  da comparação entre irmãos. A Chihiros tem WRGB II, WRGB II Pro e WRGB II
  Slim, e a WRGB II 90 e a Pro 90 são **as duas de 90 cm** — ali nem a medida
  separa, só o sufixo.

Irmão novo entrando no banco liga esses portões sozinho. Lista dentro da régua
envelhece calada.

### 4. O PORTÃO PEGOU QUATRO DEFEITOS EM MIM ANTES DE QUALQUER COLETA

Os quatro estão comentados no lugar onde mora a regra que os conserta:
1. **o título achatado**, que tirava a fronteira das palavras: com o título sem
   espaços, "Roxin" deixa de ter borda e o portão reprovava o anúncio certo
   dizendo que faltava a marca;
2. **a medida cobrada de quem não precisa dela** (o canister);
3. **o código base comendo o `2213`** do Eheim classic 250, que é o código do
   filtro e não o tamanho dele — uma regra que jogasse fora todo número final
   comeria justamente o que identifica o produto;
4. **a `linha` valendo como identidade**: "HW" está no título do HW-303, do
   HW-603B e do HW-702A. Linha é sobrenome, não identifica produto.

### 5. E AS DOZE MUTAÇÕES PASSARAM VERDES MENTINDO NA PRIMEIRA RODADA

Isto é o achado de método do bloco. A cópia ia para `<tmp>/ilha`, e dali o
caminho relativo de `coletar-shopee.py` apontava para `/tmp/ferramentas/shopee-api.py`,
que não existe: **o portão morria de `FileNotFoundError` antes de medir coisa
alguma**, e o `returncode != 0` era lido como "mutação reprovada". As doze
saíram verdes sem que uma única regra tivesse sido exercida — o defeito que
aquele arquivo existe para impedir nos outros.

Pego porque o **controle positivo rodava na árvore real** enquanto as mutações
rodavam na cópia quebrada. O conserto tem duas partes: a cópia reproduz o layout
do repositório, e **cada cópia tem de APROVAR antes de ser mutada**. Com isso
três mutações se revelaram vivas e viraram regra — entre elas a dos sufixos que
vêm do banco.

### 6. O ENSAIO ACHOU SEIS DEFEITOS QUE NENHUM TESTE ESCRITO DE CABEÇA PEGARIA

É por isso que a 25.3 manda conferir a amostra **com os olhos** antes de gravar,
e é por isso que `--ensaio` não grava nada. Todos os seis são títulos reais:
- **a VOLTAGEM do anúncio é medida.** Sete registros Maxxi existem separados por
  ela — o M-200 aparece duas vezes, uma por anúncio —, e os gêmeos casaram com o
  **mesmo** anúncio de 110 V. O campo `afiliado.voltagem_anuncio` guardava esse
  número desde 07/09 e **ninguém o lia**. Agora cada gêmeo casa com o anúncio da
  sua tomada. 110 e 127 são a mesma tomada, e o varejo usa os dois nomes.
- **a lâmpada UV do canister** casou com o canister;
- **o balde de reposição** do Atman casou com o filtro — e a palavra que o
  denuncia vinha no **fim** do título, fora dos 40 caracteres que o portão olhava;
- **o refil de um filtro é peça** (o de uma mídia é o produto);
- **"Carvão Ativado Matrix Carbon" casou com o Seachem Matrix.** São dois
  produtos do mesmo banco que nem fazem a mesma coisa: um é colônia de bactéria,
  o outro adsorve;
- **a medida cobrada passou a ser a que DISCRIMINA**, não qualquer uma: os dois
  M-200 têm a mesma potência, então o "200W" do título satisfazia os dois.

### 7. E O VALIDADOR PEGOU O ÚLTIMO, QUE TAMBÉM ERA MEU

As 33 imagens nasceram com `fonte: "shopee-api"` — nome de **ferramenta** num
campo cujo vocabulário diz de onde veio o **arquivo** — e sem as três datas
obrigatórias. **45 erros de uma vez.** A foto da API é a foto do anúncio, então
ela é `anuncio-shopee`, igual às oito que já estavam no banco.

O conserto ensinou junto: a primeira regra de reescrita perguntava pelo
`medida_como` para saber se a imagem era desta ferramenta — e as 33 malformadas
**não tinham `medida_como` nenhum**, porque era justamente um dos campos que
faltavam. **Regra de conserto que depende do campo quebrado não conserta nada.**

### 7-b. E O PISO PASSAR A PAGAR QUEBROU UMA RÉGUA QUE MEDIA CERTO — SEIS MUTAÇÕES MORTAS DE UMA VEZ

**Este é o achado mais caro do bloco, e ele não estava em lugar nenhum da
fila.** `teste-escada-compra.py` reprovou **sete cartões que estavam certos**,
cobrando *"a linha discreta do piso embaixo"* de cartões cujo botão **já é o
piso**. A causa está escrita no docblock da própria régua, de 14/09: *"a FICHA
paga comissão e a busca CRUA não"*. **Era verdade por acidente** — o único link
que pagava era a ficha, porque encurtar a busca exigia o Raphael abrir o painel.
A Open API desfez a coincidência: a busca passou a pagar e continuou sendo a
busca.

São **dois eixos independentes**, e a régua os tratava como um:
- **o que o link É** — ficha ou busca. Só a ficha leva a linha do piso embaixo,
  porque só ela pode apodrecer (a cicatriz de 13/09: quatro de nove links do
  Clube do Mosaico morreram em doze horas).
- **se o link PAGA** — `sponsored` contra `nofollow`. Decide a marcação e o
  selo, e nada mais.

É a mesma família das duas réguas que a leva 8 consertou na véspera: **regra que
só funciona porque duas coisas andam juntas para de medir no dia em que elas se
separam.**

**E O ESTRAGO ERA MAIOR DO QUE OS SETE CARTÕES.** Rodada `mutacoes-escada.py`,
**seis das 23 mutações que passavam verdes em 22/09 tinham morrido** — todas
minhas, e todas pelo mesmo motivo: a coleta apagou do banco o mundo em que elas
aconteciam. Rodar o arquivo no commit anterior deu 23 de 23, que é como se sabe
que a dívida é desta execução e não herdada.

- **quatro eram `.replace()` cru dentro de um lambda**, e `.replace()` de alvo
  que sumiu **não falha: devolve o texto igual**. Os links curtos substituíram
  as URLs cruas que aqueles alvos citavam literalmente. Agora existe
  `troca_em()`, que morre alto — a mesma lição que o `mutacoes-coleta-shopee.py`
  aprendeu no mesmo dia por outro caminho.
- **uma sorteava o alvo**: `'busca' => 'https://...'` casa com vários itens, e
  `.replace(..., 1)` pega o primeiro, que era um registro que nem aparece na
  tela medida. Agora existe `troca_no_item()`, que procura dentro do bloco
  daquele `id`.
- **duas precisavam PRODUZIR o mundo**, porque depois da coleta **não existe
  mais busca crua neste banco**: a mutação devolve um item ao mundo antigo e só
  então mente sobre ele. É a receita que o `mutacoes-dimensao.py` já usava.

**E DUAS FALHAS DE COBERTURA APARECERAM NO MEIO DISSO, as duas de verdade:**
1. **A tabela pré-renderizada não era medida.** A régua olhava só os cartões da
   vitrine, e a tabela — que é o que chega a quem não tem JavaScript (portão
   22.8) e ao robô de busca — sai da **mesma** `aquametria_cN_compra()` e não
   era conferida por ninguém. O buraco só apareceu quando a coleta deu ficha aos
   itens do topo: a mutação da URL inventada deixou de acertar um cartão, passou
   a acertar só a tabela, e a bateria **ficou verde com uma URL inventada
   servida na página**.
2. **A linha discreta do piso tinha o endereço não conferido.** A régua
   perguntava se ela existia e nunca para onde levava.

**E a afirmação do `rel` virou igualdade em vez de dois ramos.** Escrita como
`if paga: exige sponsored / elif cru: exige nofollow`, ela **deixa de medir o
cartão que não cai em ramo nenhum** — foi assim que a mutação "o piso encurtado
deixa de exigir sponsored" sobreviveu. Com `==`, tirar um termo não cala a
régua: faz a régua discordar da tela.

`teste-escada-compra.py` foi de 644 para **703 afirmações**;
`mutacoes-escada.py` de 23 para **26, todas reprovadas**.

### 7-c. E O IRMÃO NO AR TINHA O MESMO DEFEITO, COM UM ESTRAGO PIOR

`conferir-escada-no-ar.py` é o irmão de `teste-escada-compra.py` e carregava a
mesma conflação, palavra por palavra. **Ali ele não reprovou nada — e isso é
pior.** Depois do Sync da revisão 101 ele imprimiu, aprovando:

> *"19 cartões: 19 pela ficha, 0 pelo piso da 25.2, 0 sem saída"*

**Sete daqueles cartões saem pelo piso.** Como todo piso passou a pagar
comissão, a régua os contou como ficha e o relatório virou um **número errado
com cara de medido** — e é esse número que vai para o `REGISTRO.md` de toda
execução. A régua estava verde e a linha estava mentindo.

Corrigido do mesmo jeito (três conjuntos, `rel` por igualdade), mais uma
afirmação nova que impede a classe inteira de defeito: **a conta do relatório
tem de fechar** — cartão servido que não cai em nenhuma categoria agora reprova,
em vez de sumir da soma. No ar, depois do conserto: **19 cartões, 12 pela ficha,
7 pelo piso, 0 sem saída**, 130 afirmações (eram 107), 0 falha.

### 7-d. E A PÁGINA DE PRIVACIDADE FICOU ERRADA NAS DUAS DIREÇÕES — pego pela régua, no ar, depois do Sync

`conferir-privacidade-no-ar.py` reprovou com **duas** falhas, e as duas são
consequência direta deste bloco. A régua tem três regras, e o bloco furou duas:

1. **`cf.shopee.com.br` passou a carregar sozinho e a página não o nomeava.**
   As 9 fotos novas são servidas pelo CDN que a API devolve, que é um endereço
   diferente do CDN do painel (`down-bs-br.img.susercontent.com`). São **3 das
   48 páginas** fazendo requisição a um terceiro que o leitor não tinha como
   saber que existia. Não é detalhe de forma: é a única página do site que
   promete listar **todos** os endereços que o navegador contata.
2. **`shopee.com.br`, que a página nomeava, deixou de existir no ar.** Toda
   busca por extenso virou link curto nesta execução, então a frase que a
   descrevia envelheceu no mesmo commit que a tornou falsa.

**A segunda falha é a mais interessante, porque ela é a régua funcionando ao
contrário do costume:** quase todo portão cobra que a página não *esconda* algo;
este cobra também que a página não *invente* — endereço nomeado que o site não
serve mais é promessa velha lida como fato. Foi a tentação do conserto, aliás: a
primeira reescrita explicava o desaparecimento **citando o endereço**, e teria
reprovado de novo pela mesma regra. O endereço saiu da tabela e o que ficou foi
a explicação **sem** ele — descrever a ausência não exige repetir o nome.

Números recontados no ar, não estimados: **48 páginas** (a tabela dizia 44),
`www.googletagmanager.com`, `fonts.googleapis.com` e `fonts.gstatic.com` em 48
de 48; `down-bs-br.img.susercontent.com` em 5; `cf.shopee.com.br` em 3;
`s.shopee.com.br` em 5, só como destino de clique. Busca por extenso servida em
**zero** páginas.

### 8. O ESQUEMA FOI À VERSÃO 12, COM DOIS CAMPOS

- **`afiliado.encurtamento_tentado_em`** — a trava que a 25.2-b exige com todas
  as letras: *"ausente é diferente de tentado-e-falhou, e essa distinção é a
  regra inteira"*. Data e não booleano: tentativa de um mês atrás não é a mesma
  coisa que tentativa de hoje. **78 de 78.**
- **`imagem.alt_origem`** — porque quem lê os bytes do arquivo **não vê a
  imagem**, e descrever o que ela mostra seria inventar. As 9 fotos novas nascem
  com `'banco'`, e quem as substitui por `'vista'` é a Sentinela, que roda no
  Chrome. Campo e não prosa, pelo mesmo motivo do `intestavel`: a Sentinela
  precisa de uma LISTA do que falta descrever, não de um texto para ler.

`ferramentas/shopee-api.py`, que é da raiz e vale para todas as ilhas, ganhou
`sub_id_2` **opcional** — sem mudar o comportamento de quem não o passa. Ele
existe porque esta ilha já gravava esse campo desde 07/09 com o código da
calculadora, e link novo nascido sem ele entraria cego no painel.

### 9. AS 25 FICHAS QUE JÁ EXISTIAM NÃO FORAM SOBRESCRITAS

25 dos 33 casamentos caem em registros que **já têm `url`** — links feitos à mão
em 07 e 09/09, cada um com o `sub_id_2` da calculadora que o gerou. Trocá-los
por link novo apagaria a medição de **qual ferramenta vende**, que é a única
coisa que o painel da Shopee sabe dizer sobre o assunto, e trocaria um link já
conferido por outro sem história. Só **8** registros ganharam ficha nova. A
foto, essa, entra do mesmo jeito: ela não disputa com nada.

### 10. O QUE ESTE BLOCO DEIXA ABERTO, contado e não estimado

- **45 itens sem ficha.** Medição honesta, e o motivo de cada recusa fica
  escrito na passada.
- **24 imagens antigas seguem sem largura e altura**, e a causa foi **medida
  hoje**: `down-bs-br.img.susercontent.com` (o CDN do painel) devolve **403 de
  proxy** desta nuvem, enquanto `cf.shopee.com.br` (o CDN da API) responde 200.
  Quem tem foto da API tem dimensão; quem tem foto do painel não tem. Quem mede
  as 24 é a Sentinela, no Chrome.
- **Trocar a foto velha sem medida pela foto da API do mesmo anúncio** acabaria
  com o salto de leiaute nessas 24 — e arriscaria descasar o `alt` que alguém
  escreveu **vendo** a imagem. São duas opções defensáveis, então é **bloco e
  não conserto** (19.2).
- **A bancada ficou mais lenta**, e não por minha causa: `mutacoes-peixes.py`
  (95 mutações × 3719 afirmações) é o portão longo desta ilha.

### VERIFICAÇÃO

**Sem rede:** `bancada.py` **APROVADO em 31 portões, 0 falha** (régua do veredito
17 afirmações, `php -l` em 11 snippets). `teste-coleta-shopee` **153/0** (novo);
`mutacoes-coleta-shopee` **18 de 18** (novo); `teste-escada-compra` **703/0**
(eram 644); `mutacoes-escada` **26 de 26** (eram 23); `validar-produtos` 78
produtos, **0 erro**, 8 avisos (eram 9 — a `sunsun-ade-400c` ganhou foto);
`teste-peixes`, `mutacoes-peixes` 95 de 95, `teste-voz` nas 48 páginas,
`mutacoes-voz`, `teste-arvore`, `teste-ga4`, `teste-datas-schema`,
`teste-dimensao-imagem`, `teste-purga-cache`, `teste-seo-tecnico`,
`teste-apelidos`, `validar-especies`, `conferir-slugs`,
`conferir-protecao-funcoes`, `conferir-entidades` e `conferir-indice-de-levas`
todos limpos.

**NO AR, depois do Sync (revisão 103, conferida no `/status`):**
`conferir-escada-no-ar` **130 afirmações, 0 falha** (eram 107) — 19 cartões, **12
pela ficha, 7 pelo piso, 0 sem saída de compra**; `conferir-peixes-no-ar`
**906/0**; `conferir-datas-e-voz-no-ar` **368/0**; `conferir-privacidade-no-ar`
**21/0** (reprovava com 2 antes do conserto desta execução);
`conferir-cache-do-host` **51/0**.

**A sequência de revisões desta execução, porque ela conta a história:** 100 (a
coleta), 101 (as duas réguas separadas), 102 (o irmão no ar), 103 (a página de
privacidade). As falhas de 101 e 102 foram achadas **pelos próprios portões,
depois do Sync** — nenhuma delas apareceu antes de o código estar no ar, e é
exatamente para isso que a seção 8 manda verificar abrindo a URL.

### ITENS ESPERANDO LINK DE AFILIADO (item 5 do despacho da Sentinela de 13/09)

**ZERO itens sem `url_busca` encurtada** — eram 78 desde 13/09. E **zero** sem
saída de compra. **47 de 78 com ficha** (eram 39) e **41 de 78 com foto** (eram
32). O relatório que este item pede muda de forma a partir de hoje: o número que
importava era "quantos esperam link", e ninguém mais espera link.

## 2026-09-22 19h16Z — LEVA 8: A OITAVA CATEGORIA, E A PRIMEIRA EM QUE O CRITÉRIO DA LEVA ANTERIOR FALHARIA (peixes 1.13.0, manifest revisão 99, `/status` conferido na 99; QUATRO URLs novas — `/peixes/acaras/` e as fichas do acará-bandeira, do oscar e do acará-disco; a ilha vai de 44 para 48 URLs)

**O BLOCO ERA O QUE A FILA DIZIA, e pela primeira vez em duas passadas ele saiu
inteiro sem virar outra coisa.** A execução das 13h20Z de hoje gastou a passada
numa coleta recusada por escopo; a das 17h25Z virou correção na primeira
varredura e escreveu o campo que destravou esta. O banco já estava fechado
quando esta execução abriu: `/peixes/acaras/` tinha as três fichas do mínimo do
16.5 desde as 17h25Z. O que faltava era o que a própria fila listou — classificar
a SERP das quatro consultas (14.9) e escrever a linha mestra e o critério da
categoria.

### 1. O CRITÉRIO DA LEVA ANTERIOR FALHARIA AQUI, E ISSO SE MEDE

A leva 7 fechou comemorando um critério que era **verificável dentro do banco**
em vez de depender da leitura de quem escreve: separar pelo NOME que a pessoa
digita, conferindo `nomes_populares_br`. Era um avanço real e continua sendo.

Nesta categoria ele falha, e falha pelo lado caro. Varrendo `nomes_populares_br`
do banco inteiro, **quatro** registros trazem "acará": o acará-bandeira, o
acará-disco, o **acará-açu** (que é o oscar) e o **acará-borboleta** — que é o
`mikrogeophagus-ramirezi`, e que é filha de `/peixes/ciclideos-anoes/` desde a
leva 6. Um critério de nome **tiraria uma filha da mãe dela**.

**Critério bom não é o que funcionou na última vez: é o que sobrevive à varredura
desta vez.** São três categorias seguidas em que o critério da anterior não
serve — a `ciclideos-anoes` separou por prateleira, a `danios-e-rasboras` por
nome, e esta por porte.

**O que serve aqui é o porte declarado, e ele é número e não leitura:** os três
desta categoria começam em 13,7 cm de adulto e os três ciclídeos anões terminam
em 5,6 cm. Entre 5,6 e 13,7 cm **não existe um único Cichlidae neste banco** — o
corte atravessa um vão vazio de oito centímetros, então não é uma linha escolhida
para caber no dado. A prateleira brasileira concorda com ele, e é a mesma prova
que a `ciclideos-anoes` levantou do outro lado.

Com esta leva a família **Cichlidae fica inteira publicada**, repartida em duas
categorias. É a primeira família do banco em que isso acontece, e é por isso que
a `barradas` desta categoria nasce **vazia sendo afirmação e não descuido**: os
seis Cichlidae do banco passam no portão e não existe um sétimo, nem passando nem
barrado.

### 2. A LINHA MESTRA MUDOU DE COLUNA, E É A PRIMEIRA VEZ NO EIXO

As sete categorias anteriores tinham, todas, faixas térmicas que se cruzavam: a
temperatura era dado de ficha e nenhuma linha mestra teve o que dizer sobre ela.

Aqui as faixas do **oscar (22 a 25 °C)** e do **acará-disco (26 a 30 °C) não se
tocam**, e as duas vêm da MESMA base científica — o que torna a comparação
legítima pela regra que a leva 7 escreveu, porque aqui não há duas réguas, há uma
só. Um grau de distância entre o teto de um e o piso do outro separa dois peixes
que a loja põe na mesma prateleira e que a SERP responde na mesma página de
resultados.

A frase publicada **nomeia os dois peixes e não imprime os dois números**, e as
duas metades são deliberadas. Nomear, porque a linha mestra é a resposta CITÁVEL
da página (seção 5) e afirmação citada fora de contexto sem sujeito não afirma
nada — a primeira escrita dizia "dois deles", que só existe para quem está com a
tabela na tela. Não imprimir, porque o número vive na tabela, que sai do banco, e
número digitado em frase é o defeito que esta ilha mais paga.

**E o que a linha mestra não diz é tão deliberado quanto:** nada sobre porte
comparado. Esta é a categoria de MAIOR distância de porte do eixo — 13,7 a
45,7 cm — e mesmo assim o número fica fora da frase, porque o acará-disco declara
SL e os outros dois declaram TL. A regra da leva 7 vale contra a frase mais forte
que esta página poderia publicar, que é justamente quando ela custa alguma coisa.

### 3. A SERP DAS QUATRO, E UM DEFEITO DE SERP QUE ESTE EIXO NÃO TINHA VISTO

Classificadas nesta execução, pela 14.9, **antes** de uma linha da categoria ser
escrita. As quatro são **ALVO**, e a leitura inteira está em `dados/indexacao.md`.

Duas coisas ficam ditas porque são novas:

**(a) É a primeira SERP do eixo com fabricante E domínio forte ao mesmo tempo.**
Aparecem dois fabricantes de ração (Alcon, Grupo Sarlo) e um varejista de pet de
domínio forte (Petz). A 14.9 só manda a página não nascer quando eles ocupam
**quase tudo**, e não é o caso — são três posições de nove ou dez, e nenhuma
responde à pergunta com número atribuído a fonte nomeada. **O que eles ocupam é a
atenção, não a resposta.** Fica escrito porque a próxima leva de qualquer ilha vai
encontrar esse caso e a 14.9 não o resolve sozinha.

**(b) O defeito da consulta da categoria não é o número errado: é o SUJEITO
trocado.** Nas outras sete consultas de categoria o top respondia mal a pergunta
certa; aqui ele responde a **outra pergunta**. "Acará" é nome de prateleira, não
de espécie, e a mesma página de resultados mistura acará-bandeira, acará comum
(*Geophagus brasiliensis*), acará severo, acará do congo e acará-disco, devolvendo
de 60 a 300 L sem que dê para saber de qual peixe cada número fala. É a
justificativa mais forte de página de categoria que este eixo já mediu: uma linha
por espécie, com o arranjo ao lado do espaço.

E a contradição interna mais cara é a do disco: 200 L para três, 250 L para cinco
ou seis e 300 L para quatro ou cinco. **Três dessas não podem ser verdade juntas**
— 200 L para três é mais por peixe do que 300 L para cinco.

### 4. O TERCEIRO ESTADO DA AUSÊNCIA DE FUNDO GANHOU O SEGUNDO CASO, E O PRIMEIRO QUE NASCE SABENDO

A 1.12.0, quatro horas antes, escreveu esse ramo **consertando** um defeito que
esteve oito dias no ar. A ficha do acará-disco **nasce nele**: o chão de
120 × 45 cm foi declarado para juvenis ou um casal, o registro publica cardume de
cinco, e a página diz a largura, diz para quem ela foi declarada e não abre as
duas tabelas que dependem do fundo. Lido no ar, o parágrafo sai inteiro e sem
buraco.

E os **três escopos de chão vivem na mesma categoria**, o que nenhuma outra tem:
`nao-declarado` no acará-bandeira, `um-exemplar` no oscar e `juvenis`+`casal` no
acará-disco. O oscar é também a **primeira ficha do eixo com `convivencia:
solitario` cujo chão declarado COBRE o arranjo publicado** — o betta também vive
sozinho, e nele a fonte não diz para quem a base foi dada. Eram dois ramos da
mesma função com um exemplar só.

**A pergunta aberta do oscar foi respondida e não virou bloco.** A fila dizia que
quem publicasse a leva 8 decidiria se escreve a ficha dele com a ressalva do
`convivencia: solitario` na tela. A medição diz que não há o que ressalvar: o chão
declarado cobre o arranjo, a ficha abre com "e é um por aquário, não dois" — que é
o que a fonte declara — e a `observacao` do registro continua explicando o resto
para quem abrir o banco. O que sobra segue sendo bloco de esquema: `convivencia`
carrega, ali, o ESCOPO do chão e não a sociabilidade da espécie.

### 5. DUAS RÉGUAS CONSERTADAS, E AS DUAS PELO MESMO MOTIVO — ELAS TINHAM PARADO DE MEDIR

**(a) A régua do "cardume" reprovou uma página CERTA.** A afirmação "a palavra
cardume não aparece no corpo" é da leva 4, escrita quando o betta era o único
peixe de arranjo fixo da ilha, e procurava a palavra SOLTA no corpo inteiro. Ficou
verde oito dias porque nenhuma vizinha do betta tinha "cardume" no título.

As três ocorrências no corpo da ficha do oscar eram, **todas**, o título de OUTRA
página dentro de um link: o degrau da trilha e a frase de mãe apontando para
`Acarás: quantos litros, do solitário ao cardume`, e o bloco "Veja também"
apontando para `Quantos litros para um cardume de acará-disco?`. Nenhuma das três
diz uma palavra sobre o oscar, e apagar a palavra dos títulos seria mentir sobre a
categoria e sobre o disco, que vive em cardume mesmo.

O conserto é do contrato, e a frase já estava escrita lá para outro caso: **"a
régua que mede isso mede o LUGAR, nunca a palavra solta"** (16.5). `prosa_propria()`
tira do corpo exatamente os links cuja âncora é o título de uma página do eixo —
nada mais —, e a segunda metade impede o afrouxamento de virar buraco: **toda
ocorrência que sobra no corpo tem de ser, uma a uma, o título de outra página do
eixo.** Sem ela bastaria envolver a frase num `<a>` para escapar, e é exatamente
isso que a mutação nova faz.

**(b) O PORTÃO DE VERSÃO DO MANIFEST ESTAVA CEGO, E CEGO EM SILÊNCIO.**
`versao_do_snippet()` lia `f.read(20000)` — os primeiros 20 000 caracteres do
arquivo. O docblock de `aquametria-peixes.php` passou dessa marca na 1.12.0, a
busca deixou de encontrar a constante, devolveu `None`, e a guarda de divergência
logo abaixo — que **existe** para não deixar a etiqueta envelhecer calada — parou
de disparar sem dizer nada.

O resultado estava no repositório para quem olhasse: **o manifest anunciava
`versao: 1.11.0` para um snippet que estava em 1.12.0 desde as 17h25Z de hoje**, e
teria anunciado 1.11.0 para a 1.13.0. A janela era uma otimização contra um custo
que não existe — o script já calcula o `sha256` do arquivo inteiro duas linhas
acima, em toda passada — e comprava um portão que **se apaga sozinho quando o
arquivo cresce**, que é a única direção em que todo arquivo desta ilha anda.

Consertadas as duas metades: a leitura passou a ser do arquivo inteiro, e
**ausência de constante deixou de ser caso neutro** — item que declara `versao` no
manifest e cujo arquivo não define constante nenhuma agora PARA o script, com
mensagem própria. Era essa metade que teria pegado isto no primeiro dia.

**E o próximo a cair já estava medido:** `aquametria-casca.php` define a constante
no caractere 17 410, a 2 590 do mesmo penhasco.

### 6. A DÍVIDA DAS DEZOITO FERRAMENTAS FORA DO MANIFEST FOI FECHADA

O `ESTADO.md` da execução anterior a nomeou como item (a) do que ficou medido e
não consertado: *"DEZOITO ferramentas seguem fora do `manifest.json` … quarta
lista escrita à mão da mesma família, avisada em toda passada do
`atualizar-manifest.py`, lida e não atendida, hoje inclusive"*. As dezoito
entraram, com `publicar: false` e descrição própria — entre elas o `teste-voz.mjs`,
o `teste-arvore.mjs` e o `mutacoes-voz.py`, que são portões e estavam invisíveis
para o inventário da ilha.

**Sobraram cinco órfãos, e eles são de outra família:** os três `README.md` de
`snippets/`, `conteudo/` e `dados/`, e os dois arquivos de série que a Sentinela
escreve (`dados/consertos.md` e `dados/indexacao.md`). Os dois últimos precisam do
esquema mais rico da seção `dados` (`formato`, `entidade`, `fonte`), e inventá-lo
sem decidir de quem é a fonte seria trocar um aviso por um campo errado. Ficam
nomeados aqui.

### 7. O QUE ESTA LEVA NÃO FEZ, E O QUE ELA DEIXA PARA A PRÓXIMA

**Nenhuma coleta.** É a segunda leva seguida sem coleta nova — e o estoque
acabou. Varridos o catálogo e as listas declaradas das oito categorias:
**32 espécies elegíveis, 26 com ficha própria, 6 sem categoria nenhuma** (kinguio,
botia-palhaço, arco-íris boesemani, peixe-lápis, otocinclo e barbo sumatra).
**Nenhuma família entre as seis chega a três**, que é o mínimo do 16.5: são 2
Cyprinidae e mais quatro famílias de um registro cada.

O caminho mais curto continua sendo "barbos" e **custa dois passos**: o barbo
sumatra é elegível, o barbo rosado está a UM campo (`duas fontes distintas`) e não
existe um terceiro barbo no banco. O kinguio é Cyprinidae e **não** é barbo —
contá-lo seria o erro que a `ciclideos-anoes` já registrou, de trazer peixe demais
pela família. O segundo caminho, `/peixes/plecos-e-limpa-vidros/`, continua com 1
elegível e a parede dela não mudou.

### 8. E UMA COISA QUE NÃO É DESTA LEVA, MEDIDA AO CONFERIR A SEÇÃO 25 ANTES DE FECHAR

**A Open API da Shopee nunca chegou nesta ilha, e é o maior bloco parado da fila.**

Este arquivo, o `congelamento` do `ESTADO.md`, o item (e) do T3 e o item 5 do
despacho da Sentinela de 13/09 descrevem, os quatro, o mesmo mundo: *"quem
encurta é a Sentinela estratégica no navegador do Raphael, em lotes de 5"*.
**Esse mundo acabou em 16/09/2026.** A seção 25.6 do contrato mediu, com chamada
real às 16h07Z daquele dia, que o `productOfferV2` devolve numa chamada só o
`offerLink` **já encurtado**, mais a foto, a ficha canônica e o preço — sem
navegador, sem portal aberto e sem teto de calendário.

**Esta ilha esteve fora do foco de 16 a 21/09 e herdou a regra sem nunca a
aplicar.** Não é defeito de ninguém: é exatamente o custo que a 1.2 escreveu na
mesa quando o foco saiu daqui. Mas fica nomeado agora que o foco voltou.

**O que isso custa, contado:** os 78 itens servem `url_busca` **crua** — link que
dá saída de compra e **não rende comissão** —, e a **25.2-b** (18/09/2026, vale
para todas as ilhas) diz com todas as letras que isso *"deixou de ser aceitável
como padrão"*. A frase que esta ilha vem repetindo em todo fecho, *"o piso da 25.2
cobre os 78"*, era verdadeira em 13/09 e **a 25.2-b a superou**: o piso deixou de
ser destino e voltou a ser piso. Continuei reportando o número, como o despacho
manda, mas com a moldura certa.

O bloco está escrito inteiro no `PROMPT.md` como **T3(f)**, com as três partes na
ordem e com o que conferir **antes** de coletar: se `open-api.affiliate.shopee.com.br`
está na lista de domínios permitidos deste ambiente — que é passo do Raphael, e
**nenhuma rotina consegue mexer nessa lista**. Não toquei em credencial, em conta
nem em configuração: só li o contrato e escrevi o que ele diz.

**ITENS ESPERANDO LINK DE AFILIADO** (item 5 do despacho da Sentinela de 13/09):
**78** itens seguem sem `url_busca` encurtada, e **zero** deles está sem saída de
compra. Esta execução não tocou em produto nenhum.

**VERIFICAÇÃO.** bancada.py --no-ar APROVADO em 35 portoes, 0 falha (regua do veredito 17 afirmacoes, php -l em 11 snippets). teste-peixes 3719/0 (eram 3206); mutacoes-peixes 95 de 95 (eram 94 — a nova e a porta dos fundos da regua estreitada); teste-voz TUDO OK nas 48 paginas (eram 44); mutacoes-voz 30 de 30; teste-arvore 0; validar-especies 39 registros 0 erro (3 avisos: o E15 conhecido do guppy e DOIS E21, que sao a regra funcionando — a agassizii e agora o disco); testar-validador-especies 36 testes 0 falha; teste-escada-compra 644; teste-ga4 760; teste-datas-schema 102; teste-dimensao-imagem 36; teste-purga-cache 21; teste-seo-tecnico 519; teste-apelidos 59; conferir-slugs, conferir-protecao-funcoes, conferir-entidades e conferir-indice-de-levas limpos. NO AR, depois do Sync (revisao 99, conferida no /status): conferir-peixes-no-ar 906/0 (eram 805), conferir-datas-e-voz-no-ar 365/0 (eram 326), conferir-escada-no-ar 107/0, conferir-privacidade-no-ar 21/0, conferir-cache-do-host 51/0. As quatro URLs novas abertas uma a uma: 200 nas quatro, as quatro no wp-sitemap, que fechou em 48 (3 posts + 45 pages). E UMA REGRESSAO MINHA FOI PEGA PELO PORTAO ANTES DO AR: ao refinar a linha mestra para nomear os dois peixes, a primeira escrita citou a fonte na abertura (procedencia nao abre pagina, 15.2) e trocou 'o SEU aquario' por 'o mesmo aquario', perdendo a segunda pessoa. O teste-voz.mjs reprovou as duas na mesma passada.

## 2026-09-22 17h25Z — O CHÃO DECLARADO GANHOU DONO: DOIS DEFEITOS QUE ESTAVAM NO AR SAÍRAM, E O CAMPO QUE OS BARRA NASCEU (esquema de espécies versão 5, peixes 1.12.0, manifest revisão 94, `/status` conferido na 94; NENHUMA URL NOVA — seguem 44 — e NENHUMA leva gasta do teto da 21.4)

**O BLOCO ERA OUTRO QUANDO A EXECUÇÃO COMEÇOU.** A fila apontava o caminho (b) que
a leva 7 nomeou — *"um campo de ESCOPO no esquema, que deixe a base declarada
viajar com o arranjo a que ela se refere"* —, e o que justificava o bloco era
destravar `/peixes/acaras/`. A varredura que o bloco pedia antes de escrever uma
linha achou outra coisa: **a ficha do apistogramma agassizi estava no ar, desde
14/09, prometendo ao harém um chão que a fonte declarou para um casal.** A partir
daí isto deixou de ser construção e virou correção (seção 18 do contrato), e a
seção 18.5 decide a ordem: ilha com defeito no ar não recebe página nova.

### 1. O defeito, e onde ele estava escrito

A página servia, na primeira frase:

> *"Para um harém de apistogramma agassizi — e harém quer dizer mais fêmeas do que
> machos, nunca um casal —, o seu aquário precisa de 60 cm de frente por 30 cm de
> fundo."*

Os 30 cm de fundo são do Seriously Fish, que os declarou **para UM CASAL** (*"base
de 60 x 30 cm ou mais é aceitável para UM casal, com o grupo exigindo espaço
maior"*). A base científica, que declara o harém, publica a **frente** de 60 cm e
não diz uma palavra sobre o fundo.

**A proibição já existia — e não valia nada.** Estava no campo `observacao` do
próprio registro, em maiúsculas, escrita pela execução que publicou a ficha:

> *"O QUE A FICHA NÃO PODE FAZER, e fica escrito para quem a escrever: prometer que
> 60 x 30 cm serve ao harém. Serve ao casal por declaração do compêndio; para o
> harém, os 60 cm de FRENTE são o que a base declara, e o fundo não está declarado
> para esse arranjo."*

Quem escreveu a frase tinha entendido o problema inteiro. **Prosa não conta e prosa
não barra página** — é a mesma família do `afiliado.intestavel` (14/09) e do
`coletas_recusadas` (ontem), e desta vez o custo foi tela: oito dias, uma tabela de
litros por altura e uma tabela de "quantos cabem no aquário mínimo", as duas
multiplicando um fundo que é de outros peixes.

### 2. O segundo defeito, que ninguém tinha visto: a base atribuída à fonte errada

Medido com `curl` nas fichas no ar: **quatro** diziam *"Quem declara essa base é o
FishBase"* — tetra neon, tetra-brilhante, rasbora arlequim e apistogramma agassizi
— e nas quatro os **dois lados do chão são do Seriously Fish**. A causa é de uma
linha: a frase perguntava sempre por `comprimento_minimo_aquario_cm` e só caía na
base quando não havia comprimento declarado, então nomeava o corpo que declarou
**a frente** enquanto a palavra na tela era **base**.

Atribuir número à fonte errada é o defeito mais caro desta ilha, porque a
procedência é o que ela vende. A frase passa a perguntar pelo campo que ela vai
nomear.

### 3. O campo: `chao_declarado_para` (esquema versão 5)

`base_minima_cm` sempre foi um número sobre uma **população**, e o esquema não
tinha onde dizer qual. O campo tem duas metades:

- **`arranjos`** — termos de vocabulário fechado, **ordenados por população**:
  `juvenis` < `um-exemplar` < `casal` < `grupo`. Chão declarado para um nível serve
  a tudo nele ou abaixo (aquário que abriga um grupo abriga um casal; o contrário
  não vale). `harem` e `cardume` mapeiam os dois em `grupo` — e é exatamente por
  isso que a base do casal não serve nenhum dos dois.
- **`frase`** — a cláusula da transcrição da fonte em que o chão foi declarado,
  copiada ao pé da letra.

**`nao-declarado` é o caso mais comum e não é um buraco:** é a fonte que publica a
base como o mínimo da espécie sem nomear população (*"base recomendada de 61 x 38
cm"*). **Foi escolha, e o custo está escrito no esquema:** cobrar população nomeada
onde a fonte não nomeou tiraria o fundo de doze fichas por causa do silêncio da
fonte, e silêncio ali quer dizer "este é o aquário mínimo da espécie". Por isso ele
nunca aparece ao lado de outro termo, e o E22 reprova se a própria cláusula nomear
alguma população — **o termo permissivo é justamente o que devolve o fundo a uma
ficha que não pode publicá-lo, e por isso ele é conferido pelo avesso.**

**Preenchido nos 23 registros** com base de dois lados, com a cláusula conferida
como trecho **literal** da referência antes de gravar. Resultado da varredura: **um
único** desacordo entre o chão declarado e o arranjo publicado — a agassizii. As
outras 22 estão cobertas, e seis delas por fonte que nomeia "grupo pequeno" ou
"cardume" explicitamente.

### 4. As três regras, e onde os dentes ficaram

- **E20** — base de dois lados **exige** o campo, e registro sem base de dois lados
  não pode tê-lo. `nao-declarado` não se mistura.
- **E21** — **aviso, não erro.** O dado está certo: a fonte declarou o que
  declarou. Quem tem de obedecer é a **página**, e por isso os dentes ficaram em
  `teste-peixes.py`, contra o HTML servido.
- **E22** — a `frase` tem de ser trecho **literal** da referência que sustenta a
  base, e os termos têm de estar sustentados por ela, palavra a palavra.

`testar-validador-especies.py` foi de **28 para 36 testes**, 0 falha, com oito
corrupções novas. Uma delas conserta um teste que tinha envelhecido: o do E19 corrompia
o banco **preenchendo** a base do disco, e a base entrou hoje de direito — a
corrupção agora é apagar a superação e deixar o campo preenchido, que é a metade
que a regra existe para pegar.

### 5. A metade da tela, e a terceira ausência

`aquametria_peixes_fundo()` é agora a **única** leitura do fundo publicável — a
ficha e o JSON-LD liam `base_largura` cada um por si, e duas leituras do mesmo
campo são duas respostas no dia em que uma ganhar condição.

E a ausência virou **três estados**, não dois, porque são diferentes para quem lê:

1. ninguém declarou largura (o rodóstomo);
2. **a largura declarada não é sobre estes peixes** (novo);
3. a base serve e sai inteira.

O estado 2 **não cala o número**: a página diz a largura, diz **para quem** ela foi
declarada, diz que as duas tabelas do fundo não saem e por quê, e mantém de pé a
frente — essa sim declarada para o arranjo publicado. Calar seria repetir, do outro
lado, o erro de publicar sem escopo.

E a abertura da ficha ganhou o **terceiro ramo** na mesma execução, depois de a
primeira versão subir e ser lida no ar: ela dizia *"o fundo fica em aberto"* e
publicava a largura declarada dois parágrafos abaixo — **duas coisas diferentes a
uma tela de distância**, e a primeira lida como "ninguém sabe". Agora diz *"o fundo
fica de fora: a largura declarada é para outra quantidade de peixe"*, sem nomear
corpo nenhum, que é o que a 15.2 pede do primeiro parágrafo.

`teste-peixes.py` foi de **3147 para 3206 afirmações**, com a segunda lista escrita à
mão do arquivo (`FUNDO_DE_OUTRO_ARRANJO`) posta frente a frente com o banco — pelo
mesmo motivo da primeira: perguntar ao banco quem está fora de escopo seria medir o
banco contra ele mesmo. `mutacoes-peixes.py` foi de **90 para 94**, e as quatro novas
são as quatro portas dos fundos: o portão sumindo, o harém virando casal, a ordem
dos termos invertendo e a atribuição voltando a perguntar pelo comprimento.

### 6. E o que o bloco tinha ido fazer: `/peixes/acaras/` DESTRAVOU

O acará-disco passou treze dias em **um corpo de fonte só**, e a coleta das 13h20Z de hoje
foi recusada por escopo. Com o campo, ela entrou **sem uma busca nova**: os 120 × 45 ×
45 cm e os 255 L do Seriously Fish estão gravados com `arranjos: [juvenis, casal]`,
o registro foi a **completo**, e a entrada em `coletas_recusadas` ganhou
`superada_em` e `superada_por` em vez de ser apagada — é a **primeira recusa
superada** desta ilha, e a série é o que ensina.

**A categoria tem as três fichas do mínimo do 16.5:** acará-bandeira, oscar e disco.
O catálogo foi de **31 para 32** espécies.

**E a ficha do disco já nasce sabendo o que não pode dizer:** o chão dela é a
**frente** de 120 cm, que a FishBase declara para grupos de cinco ou mais. O fundo
sai na tela com o nome da população para quem foi declarado, e as duas tabelas que
dependem dele não saem.

### 7. O que ficou medido e NÃO consertado (18.3)

- **DEZOITO ferramentas seguem fora do `manifest.json`**, entre elas `teste-voz.mjs`,
  `teste-arvore.mjs` e `mutacoes-voz.py`. É a quarta lista escrita à mão da mesma
  família, o aviso sai em toda passada do `atualizar-manifest.py` e vem sendo lido e
  não atendido — hoje inclusive.
- **O `convivencia` do oscar continua carregando duas coisas.** A fila supunha que o
  oscar tinha o mesmo defeito do disco resolvido em prosa; **a medição diz que não**.
  A base de 150 × 60 cm dele foi declarada para UM adulto e ele publica `solitario`,
  que o esquema define como "um por aquário" — o chão **cobre** o arranjo, e o campo
  novo registra isso sem nada a consertar. O que sobra é outra coisa, e fica nomeada:
  `convivencia: solitario` está dizendo, no oscar, o **escopo do chão** e não a
  sociabilidade da espécie, e a própria `observacao` diz isso. Trocar o valor tiraria
  o oscar do portão de página e com ele a categoria inteira, então isto é bloco de
  esquema, não conserto de passada.
- **78 itens seguem sem `url_busca` encurtada**, e **zero** sem saída de compra — o
  piso da 25.2 cobre os 78. Esta execução não tocou em produto nenhum.

### PRÓXIMO PASSO DESBLOQUEADO

**LEVA 8 — `/peixes/acaras/`**, a oitava categoria do eixo: a mãe e as fichas do
acará-bandeira, do oscar e do acará-disco. Banco fechado em três elegíveis nesta
execução. Falta, antes de publicar: classificar a SERP das quatro consultas (14.9) e
escrever a linha mestra da categoria — e a leva 5 deixou a regra de como escrevê-la
(*"texto de categoria escrito antes da leva é afirmação que ninguém mediu"*). O teto
da 21.4 segue em **1 de 3** nesta semana.


## 2026-09-14 22h11Z — LEVA 6: A QUINTA CATEGORIA, E A PRIMEIRA EM QUE AS TRÊS FILHAS VIVEM DE TRÊS JEITOS DIFERENTES (peixes 1.10.0, manifest revisão 87, `/status` conferido na 87 em UM disparo; QUATRO URLs novas — `/peixes/ciclideos-anoes/` e as fichas do ramirezi, do apistogramma agassizi e do papilocromis)

**MESMA EXECUÇÃO DAS 21h18Z**, seguindo no **modo mutirão** que esta ilha tem
ligado desde 09/09 a pedido do Raphael ("entregue quantos blocos couberem na
sessão, em sequência, na ordem da fila, verificando cada um pela seção 8 antes de
começar o próximo"). O bloco anterior — a preparação — foi verificado no ar antes
deste começar: `/status` na revisão 86, seção `/peixes/` servindo 31/39/8 e
`/peixes/ciclideos-anoes/` respondendo **404**, que era o critério de pronto dele.
O que o mutirão não cobre é "publicar a malha em massa", e uma leva de quatro
URLs é a unidade normal da rampa, não massa.

**A ILHA CHEGOU A 40 URLs, e é metade do piso da seção 21 — não o piso.** O
`wp-sitemap` conta **40** (3 posts + 37 pages). A 21.1 pede **40 URLs E 21 dias
desde a primeira URL indexada**, e `primeira_indexacao` é 09/09/2026: são **5
dias**. A ilha segue **abaixo do piso**, e o campo `piso` do cabeçalho segue
`abaixo` porque quem escreve esse campo é a leitura semanal da Sentinela (21.6) —
a Fundação lê e não recalcula de cabeça. A metade do tempo fecha em **30/09/2026**.

### 1. Três arranjos numa categoria só, pela primeira vez

As quatro categorias anteriores tinham no máximo **dois** arranjos, e a
`vivaparos` tinha **um** (as três em harém). Esta tem os três: o **ramirezi**
vive em casal, a **apistogramma agassizi** em harém e o **papilocromis** em grupo
de 6 a 8. É a primeira página desta ilha em que os três ramos da abertura da
ficha aparecem lado a lado, na mesma tabela, e por isso a primeira em que trocar
um ramo pelo outro mudaria a tela de uma categoria inteira.

### 2. A frente mínima do papilocromis é a primeira do eixo que é CONDICIONAL

O compêndio não publica "aquário mínimo" solto para ele. Publica *"grupo misto de
6 a 8 ou mais **desde que** o aquário seja espaçoso, de 120 cm de comprimento ou
maior"* — os três números na **mesma frase**. Separá-los daria uma frente mínima
que a fonte nunca declarou sozinha, e é a mesma família do **BASE contra FRENTE**
que a leva 2 consertou: número certo, escopo errado.

A ficha dele também exercita o ramo do **comprimento sem fundo**: nenhuma das
duas fontes declara a largura, então a página **não serve** a tabela de litros por
altura nem a de quantos cabem — e diz por quê, com a frase que a leva 2 escreveu
("elas sairiam de um fundo que a gente teria inventado"), em vez de encolher
calada.

### 3. O que a categoria prova, e nenhuma outra deste eixo pode provar

O ramirezi e a apistogramma agassizi têm **exatamente o mesmo porte declarado** —
4,2 cm SL, os dois na mesma base científica — e pedem os **mesmos 60 cm**. O
papilocromis tem 5,6 cm, **1,4 cm a mais**, e pede **120**. A abertura da página
sai contada na hora: *"São 3 ciclídeos anões com aquário mínimo declarado por
fonte com nome e data, e o mínimo vai de 60 a 120 cm de frente."*

### Verificação

**Bancada, 0 falha:** `teste-peixes` **2683 afirmações** (eram 2255);
`mutacoes-peixes` **90 de 90 reprovadas**; `mutacoes-arvore` 14 de 14;
`teste-arvore` PASSOU; `teste-seo-tecnico` **447** (eram 411);
`teste-datas-schema` 102; `conferir-slugs`; `conferir-protecao-funcoes`;
`php -l` limpo nos dois snippets tocados. As quatro metas de descrição entre
**140 e 147** caracteres, todas distintas.

**A régua da bancada cresceu junto, e em quatro lugares escritos à mão** — é o
desenho deste teste, que nunca pergunta ao snippet o que o snippet deveria
provar: `FICHAS` (mais três), `CATEGORIAS` (a quinta, com `barradas` **vazia** e
isso é afirmação: não existe um quarto ciclídeo anão no banco, nem passando nem
barrado), `SEM_FUNDO_DECLARADO` (ramirezi e papilocromis) e o mapa de páginas do
`render-pagina-completa.php`.

**No ar:** Sync às 22h11Z, `/status` na **revisão 87**, igual à do manifest, em
**um** disparo com 20 aplicados. As quatro URLs novas em **200**, as quatro no
`wp-sitemap`, **40 URLs no total**. `conferir-peixes-no-ar` com **707
afirmações, 0 falha** (eram 614) e `conferir-datas-e-voz-no-ar` com **287
afirmações, 0 falha**. A categoria serve `CollectionPage + ItemList +
BreadcrumbList`; as fichas servem `Article + FAQPage + BreadcrumbList`.

### Próximo passo

1. **NENHUMA LEVA DE MALHA ATÉ 15/09.** O teto da 21.4 fechou em **3 de 3** nesta
   semana: leva 4 às 11h25Z, leva 5 às 13h19Z e leva 6 às 22h11Z, as três em
   14/09. Não é bloqueio — é calendário, e ele zera em 21/09/2026.
2. **BANCO**, que é o que destrava as próximas levas: a `vivaparos` de 3 para 5
   fichas segue presa ao despacho de egresso do Raphael (molly e guppy) e é o
   maior salto disponível do eixo; a `plecos-e-limpa-vidros` não nasce sem coleta
   que hoje não existe, porque o ancistrus do comércio brasileiro é espécie não
   descrita; e a `Apistogramma cacatuoides` fica como coleta em aberto, com a
   causa nomeada acima.
3. **T5, artigos-âncora**, e **T6, prospecção do widget** — os dois cabem sem
   gastar leva, e o T6 é a única alavanca de backlink do projeto.
4. **A pauta da seção 17** ainda não existe nesta ilha: `pauta.md` com 0 escritos,
   0 na fila, 0 recusados.

## 2026-09-14 21h18Z — PREPARAÇÃO DA LEVA 6: A QUINTA CATEGORIA GANHA BANCO, CRITÉRIO E LINHA MESTRA, E NENHUMA URL NASCE (peixes 1.9.0, banco de espécies de 37 para 39 registros, manifest revisão 86; ZERO URL nova, ZERO leva do teto da 21.4 gasta)

**A ESCOLHA DA ILHA: primeira tentada, e sem corrida.** Os cinco `ESTADO.md` do
arquipélago estavam com `executando_desde: null`, que pela **1.1** já significa que
não há bloco da Fundação vivo — o git não precisou desempatar nada. Pela **18.1**
li o topo dos cinco `PROMPT.md` antes de aplicar a rotação: **nenhuma ilha tem
despacho corretivo aberto**. Os da aquametria (Raphael de 11/09, Sentinela de
13/09 e Raphael de 14/09) estão fechados — o que sobra do de 13/09 são os itens 5
(registro de receita, que diz de si mesmo "a ordem NÃO muda") e 6 (suspenso pela
seção 21); o da clubedomosaico foi reescrito pela 18.3 em 14/09 e o que ele deixou
aberto ele mesmo classifica como **bloco de malha, não item de conserto**; e os da
ohmetria e da jornadafly são despachos de NASCIMENTO, que carregam a fila de
blocos inteira dentro deles e por isso não cabem na 18.2 ("despacho sai inteiro
numa execução só"). Sobrou a rotação da seção 1, e a aquametria tinha a
`ultima_execucao` mais antiga por quase três horas: **15h52Z**, contra 18h45Z da
clubedomosaico, 19h16Z da ohmetria, 19h17Z da robometria e 19h31Z da jornadafly.
Reserva empurrada às 21h18Z e **aceita de primeira**. Nenhum branch `claude/*`
com o que mesclar e nenhum PR aberto. **Rede pela 20.2, antes de trabalhar:** home
em **200** e `/status` na **revisão 84**, igual à do manifest, em **uma** passada.

**POR QUE ESTE BLOCO.** O item (1) do PRÓXIMO da execução das 13h19Z e o item (2)
da lista das 15h52Z nomeavam a mesma coisa: *"a próxima categoria do eixo, e ela é
decisão de banco antes de ser de leva"*. O item (2) daquela última lista ("a lista
dos barrados na tela") **já estava entregue** — a leva 5 escreveu, no seu próprio
PRÓXIMO, que *"a lista dos barrados na tela da categoria já existe"*, e ela foi ao
ar em 13/09 às 23h19Z. Era item copiado de uma lista anterior sem reconferência, e
esta execução o fecha como cumprido em vez de refazê-lo. O item (1) da mesma lista
(a `vivaparos` de 3 para 5 fichas) segue preso ao despacho de egresso do Raphael, e
o (3) segue preso à Sentinela estratégica. O que sobrava sem bloqueio era o banco —
e banco é trabalho, não bloqueio (seção 2).

### 1. As duas categorias vazias tinham UM elegível cada, e a escolha entre elas foi medida

`/peixes/ciclideos-anoes/` tinha o **ramirezi** e `/peixes/plecos-e-limpa-vidros/`
tinha o **otocinclo** — as duas a duas espécies do mínimo de três do **16.5**. A
escolha foi pelos plecos serem um beco: o segundo candidato natural, o
`ancistrus-cirrhosus`, está **barrado por `temperatura_C`** desde 09/09 e o motivo
escrito no registro dele não é falta de busca, é que **o cascudo do comércio
brasileiro é *Ancistrus* sp. '3', espécie não descrita** — as faixas que aparecem
na busca são das espécies irmãs e foram recusadas na coleta original. Coletar de
novo devolveria a mesma recusa. Os ciclídeos anões não têm esse problema: o
recorte é comercial, tem prateleira com endereço próprio nas lojas brasileiras, e
os candidatos têm ficha nos dois corpos de fonte que este banco usa.

### 2. Duas espécies novas, e cada número voltou em duas passadas independentes

**`apistogramma-agassizii`** — porte **4,2 cm SL** macho/não sexado, **26 a 29 °C**,
pH 5,0 a 7,0, dH 0 a 12, frente mínima **60 cm**, `convivencia: harem`. A base
científica declara a seção de aquário como *"várias fêmeas para um macho, aquário
mínimo de 60 cm"*; o compêndio declara *"base de 60 × 30 cm ou mais é aceitável
para UM casal, com o grupo exigindo espaço maior"*.

**`mikrogeophagus-altispinosus`** — porte **5,6 cm SL**, **22 a 26 °C**, frente
mínima **120 cm**, `convivencia: grupo`, `cardume_minimo: 6`,
`cardume_recomendado_ate: 8`. O compêndio publica os três números numa frase só:
*"grupo misto de 6 a 8 ou mais, desde que o aquário seja espaçoso, de 120 cm de
comprimento ou maior"*.

**Banco: 39 registros, 0 erro, 1 aviso** — o mesmo aviso E15 do guppy, que já
existia. O catálogo foi de **29 para 31** e o portão de página de 29 para 31.

### 3. O VAZAMENTO QUE FOI RECUSADO, e ele custou uma espécie inteira

A candidata mais óbvia da categoria não era nenhuma das duas: era a
**`Apistogramma cacatuoides`**, que é o apistograma mais vendido do Brasil. Ela
**ficou de fora**, e o motivo é o que esta ilha persegue desde a leva 1. A base
científica publica dela o porte (5,0 cm SL), o pH, a dureza e a faixa de 24 a 25 °C
— os quatro voltaram iguais em duas passadas —, e **não publica tamanho de
aquário**. O que a busca ofereceu no lugar foi a frente da **congênere**, com a
frase *"a espécie relacionada A. agassizii menciona aquário mínimo de 60 cm, o que
pode servir de referência para espécies semelhantes de Apistogramma"*. É
literalmente o atalho que a leva 2 proibiu: **parâmetro de espécie vizinha é chute
com cara de dado**.

E a segunda passada, no compêndio, deu o sinal mais forte ainda: o bloco de
compatibilidade devolvido para a `cacatuoides` era **idêntico palavra por palavra**
ao devolvido para a `agassizii` na passada anterior, e junto veio uma frase de
cálculo de aquecedor que nenhuma ficha daquele compêndio publica. Duas fichas
diferentes não devolvem o mesmo parágrafo; **resumo que repete parágrafo é resumo
costurando páginas, não lendo uma**. A espécie fica como coleta em aberto para o
dia em que a leitura direta abrir.

**O sentido inverso do mesmo vazamento é o que autorizou a `agassizii`:** a
passada que devolveu a frente dela **não estava perguntando por ela** — perguntava
pela `cacatuoides`, e citou a `agassizii` como a que TEM o número. Foi confirmada
depois por uma passada que perguntava pela `agassizii` e devolveu a mesma seção,
com a mesma frase da proporção entre os sexos.

### 4. Os dois corpos declaram o MESMO 60 cm para arranjos DIFERENTES, e a ficha vai ter de dizer isso

Na `agassizii`, a base atribui os 60 cm a *várias fêmeas para um macho* (harém) e o
compêndio atribui a base de 60 × 30 cm a *um casal*, dizendo que o grupo exige
espaço maior **sem dar o número desse espaço**. O número é o mesmo nos dois lados,
então **não é conflito** pelo vocabulário desta ilha — conflito é valor diferente
para o mesmo campo. Mas também não é uma afirmação só, e o registro diz o que a
ficha não pode fazer: **prometer que 60 × 30 cm serve ao harém**. Serve ao casal por
declaração do compêndio; para o harém, o que está declarado são os 60 cm de
FRENTE, e o fundo não está declarado para esse arranjo.

### 5. A categoria ganha critério e linha mestra, e é a primeira em que nem a família nem o gênero servem

Nos tetras a família não servia e o gênero resolvia; nas coridoras o gênero não
servia e a subfamília resolvia; nas bettas e nos vivíparos a família serviu. **Aqui
nenhum dos dois serve.** Cichlidae é a família do **oscar (45,7 cm)**, do
**acará-disco (13,7 cm)** e do **acará-bandeira (15,0 cm)**, os três neste mesmo
banco e nenhum deles anão; e o gênero também não, porque o **ramirezi** e o
**papilocromis** são os dois `Mikrogeophagus` e ocupam as **duas pontas** da tabela,
enquanto a `agassizii`, que é `Apistogramma`, cai exatamente em cima do ramirezi.

Quem separa é a **prateleira brasileira**, e ela é verificável em vez de opinativa:
"ciclídeos anões" é categoria de loja com endereço próprio na Kauar, na RSDiscus e
na Fazenda Submersa, e as três põem estes três lá dentro e nenhuma põe o oscar, o
disco ou a bandeira. O porte declarado explica a prateleira sem régua nova: **os
três ficam abaixo de 6 cm e o menor dos outros Cichlidae do banco tem 13,7 cm.**

**A linha mestra sai da tabela e de mais nada, e é o caso mais limpo do eixo
inteiro:** o ramirezi e a agassizii têm **exatamente o mesmo porte declarado** —
4,2 cm SL, os dois na mesma base — e pedem os mesmos 60 cm; o papilocromis tem
5,6 cm, **1,4 cm a mais**, e pede **120**. Nenhuma outra categoria deste eixo tem
dois peixes de porte IDÊNTICO para provar que não é o porte que decide. O que
dobra o aquário é o arranjo: casal, harém e grupo de 6 a 8.

### 6. O PORTÃO REPROVOU ESTA EXECUÇÃO, e é o motivo de ele existir

A lista `especies` da categoria foi preenchida com os três, e o
`teste-peixes.py` reprovou na hora: **"a lista de espécies é da LEVA, não da
preparação"** — preenchê-la antes faria a mãe publicar a contagem de uma categoria
que o 16.5 ainda não deixou nascer. A lista voltou a `array()` com o motivo escrito
ao lado e com os três ids nomeados no comentário, para a leva 6 não precisar
refazer a medição. **Régua que pode falhar falhou na bancada em vez de no ar**, que
é o oposto da régua escrita para um mundo que nunca aconteceu.

### 7. SERP das QUATRO consultas classificada em 14/09/2026, todas ALVO

Pela **14.9**, e prontas para a leva 6 copiar para `aquametria_peixes_registro()`
com `serp_em => '14/09/2026'`:

- **`quantos litros para ciclídeo anão`** (a mãe, nível 2). Top 10 com um portal
  europeu (zooplus.pt), um fórum português, dois blogs de pet shop, um Blogspot de
  2012, uma loja, três blogs de aquarismo e **uma ficha de OUTRA espécie**
  (*A. gephyra*). Os números se contradizem na mesma página de resultados: 54 L,
  30 L para casal e 50 L para comunitário, 75 L, 100 L. Nenhum domínio forte,
  nenhuma atribuição — e **o próprio resumo da busca termina mandando o leitor
  pesquisar espécie por espécie**, que é exatamente a tabela que esta página é. É
  a mesma assinatura da mãe dos vivíparos. **ALVO.**
- **`quantos litros para ramirezi`** (ficha). Top 9 com **seis lojas**, uma ficha de
  portal de aquarismo, um portal de conteúdo e um blog. Números: 30 L para casal e
  50 L para comunitário, 40 L, 60 L, 50 L, mais a regra de bolso "um ramirezi para
  cada 20 litros" — que é a conta per capita que esta ilha recusa desde a leva 1.
  Nenhum publica a base em centímetros nem atribui o número. **ALVO.**
- **`quantos litros para apistogramma agassizi`** (ficha). Top 9 com **oito páginas
  de PRODUTO** (rsdiscus, myaquarium, proaquarista, fazendasubmersa, solaqua com
  três anúncios, mais uma loja portuguesa) e uma ficha de portal. Elas vendem o
  peixe e não respondem a pergunta: 30 L / 50 L, 50 L, 60 × 30 × 30 cm (54 L),
  60 L. É a SERP mais frouxa das quatro. **ALVO.**
- **`quantos litros para papilocromis`** (ficha). Top 8 e **só dois resultados
  falam da espécie**: duas lojas. O resto é página genérica de "quantos peixes
  cabem" (duas), ficha de kinguio fora do assunto, Blogspot de 2013, Blogspot de
  2011 e um fórum. Números: 60 L para casal, 100 L para harém, 70 L para casal — e
  **ninguém publica os 120 cm de frente que o compêndio declara para o grupo de 6 a
  8**, que é o arranjo que a própria fonte recomenda. **ALVO, e é a consulta de
  maior distância entre o que a SERP responde e o que a fonte declara.**

### 8. A CONFERÊNCIA NO AR REPROVOU, E O DEFEITO ERA DELA: `in` não sabe onde o número começa

`conferir-peixes-no-ar.py` acusou, na ficha do peixe-espada, *"a prestação de
contas nunca diz '1 estão'"*. **A página estava certa.** Ela serve *"21 estão na
tabela acima"* — e `"1 estão na tabela" not in t` é um teste de SUBSTRING, que
casa dentro do 21. As duas espécies novas levaram a tabela de vizinhos de
temperatura daquela ficha de 20 para **21**, e a régua acusou um defeito que não
existia.

**É a mesma família do número de tela digitado que esta ilha persegue nas
páginas, do lado do portão** — com a diferença de que aqui o custo é o inverso:
**régua que falha ERRADO custa tanto quanto régua que não falha.** A primeira
manda consertar o que está certo; a segunda deixa passar o que está errado. As
duas roubam a única coisa que o portão existe para dar, que é saber em qual das
duas situações a ilha está.

O conserto é `(?<![\d.,])` nas duas linhas — só casa o `1` que **começa** o
número —, e a intenção não mudou: continuar pegando a concordância agramatical
com UM, que foi o que a leva 5 consertou nas fichas. **Provado nos dois
sentidos**, com oito casos: `"1 ficaram fora"` e `"1 estão na tabela"` continuam
sendo pegos; `11`, `21`, `31` e `1,1` deixam de ser. Depois do conserto:
`conferir-peixes-no-ar` com **614 afirmações, 0 falha**.

A bancada não tinha esse defeito, e a diferença entre as duas diz por quê: no
`teste-peixes.py` a frase inteira é **recomputada do banco** e comparada por
igualdade; no ar ela tinha virado um atalho de substring. **Atalho de portão é
portão com uma régua a menos.**

### Verificação

**Bancada:** `validar-especies` 39 registros, 0 erro, 1 aviso (o E15 do guppy, que
já existia); `testar-validador-especies` 24 testes, 0 falha; `teste-peixes`
**2255 afirmações, 0 falha**; **`mutacoes-peixes` 90 de 90 reprovadas**; `conferir-slugs`;
`conferir-protecao-funcoes` (46 funções do snippet, todas dentro de
`function_exists`); `teste-seo-tecnico` 411; `teste-escada-compra` 644;
`teste-datas-schema` 102; `teste-apelidos` 59; `validar-produtos` 78 produtos,
0 erro; `php -l` limpo.

**No ar:** Sync disparado às 21h45Z, `/status` na **revisão 86**, igual à do
manifest, em **um** disparo com 20 aplicados. A seção `/peixes/` passou a servir
**31 espécies no catálogo, 39 no banco, 8 fora** (era 29/37/8), e a checagem
precisou de quebra-cache: o endereço limpo continuou servindo 29/37/8 depois do
Sync, porque o corpo dessas páginas é um **shortcode** — mudança que vem do
snippet não move `post_modified`, não invalida nada, e a hospedagem responde
`cache-control: max-age=7200`. Não é defeito novo e não é surpresa: é o cache
duplo que a seção 4 do contrato nomeia, e é por isso que o
`conferir-peixes-no-ar.py` manda `?v=<hora e minuto>` em toda requisição desde
que nasceu. **O que está no ar é o que a origem serve**; a cópia em cache vence
sozinha (expirava às 23h51Z do mesmo dia). **`/peixes/ciclideos-anoes/` responde 404**,
que é o critério de pronto desta preparação: a categoria tem critério, linha
mestra e banco, e NÃO tem URL. `conferir-peixes-no-ar` com **614 afirmações, 0
falha** depois do conserto do item 8.

### Receita, contada (item 5 do despacho da Sentinela de 13/09)

Nada mudou nesta execução, e a contagem é a mesma das 15h52Z: **78 de 78** itens
com piso escolhido; **39** com ficha de afiliado, os 39 marcados `intestavel`;
**0 de 78** com `url_busca` encurtada, que segue sendo trabalho da Sentinela
estratégica no navegador do Raphael e que pela 25.2 **nunca** bloqueia página.
**Espécie não é produto e não tem link de afiliado** — os dois registros novos
nascem sem campo de afiliado, como os outros 37.

### Próximo passo

1. **LEVA 6 = `/peixes/ciclideos-anoes/`** com as três fichas, e ela está pronta
   para nascer: banco fechado em três elegíveis, critério e linha mestra escritos,
   SERP das quatro consultas classificada. Falta escrever as quatro entradas em
   `aquametria_peixes_registro()`, preencher a lista `especies` da categoria e as
   metas de descrição. **O teto da 21.4 está em 2 de 3 nesta semana**, então a leva
   cabe hoje.
2. **A `vivaparos` de 3 para 5 fichas** continua sendo o maior salto disponível do
   eixo e continua presa ao despacho de egresso do Raphael (molly e guppy).
3. **A `plecos-e-limpa-vidros`** só nasce com coleta que hoje não existe: o
   ancistrus do comércio é espécie não descrita, e o segundo elegível teria de vir
   de outra família da prateleira.
4. **A `cacatuoides`** fica como coleta em aberto, com a causa nomeada: a base não
   publica o aquário dela e a busca ofereceu o da congênere.

## 2026-09-14 13h19Z — LEVA 5: A QUARTA CATEGORIA, E A PRIMEIRA EM QUE NENHUMA FILHA TEM NÚMERO DECLARADO (peixes 1.8.0, manifest revisão 82, `/status` conferido na 82; QUATRO URLs novas — `/peixes/vivaparos/` e as fichas do platy, do peixe-espada e do plati variatus)

**A ESCOLHA DA ILHA: primeira tentada, e sem corrida.** Os três `ESTADO.md` estavam com `executando_desde: null`, que pela 1.1 já significa que não há bloco da Fundação vivo — o git não precisou desempatar nada. Pela 18.1 procurei despacho aberto antes da rotação: os três `PROMPT.md` foram lidos e nenhum tem despacho para a Fundação de pé (o da clubedomosaico, de 14/09, foi fechado inteiro na execução das 11h18Z e já está em FECHADOS; `dados/despachos.md` tem quatro abertos e os quatro são do RAPHAEL, nenhum bloqueando bloco). Sobrou a rotação da seção 1, e a aquametria tinha a `ultima_execucao` mais antiga: 11h25Z, contra 11h44Z da robometria e 12h45Z da clubedomosaico. Nenhum branch `claude/*` com o que mesclar e nenhum PR aberto. **Rede pela 20.2, antes de trabalhar:** home em 200 e `/status` na revisão 77, igual à do manifest, em UMA passada.

**POR QUE ESTE BLOCO:** era o item (1) do PRÓXIMO da execução das 11h25Z, e o teto da 21.4 estava em 1 de 3 nesta semana. A categoria estava preparada desde 13/09 às 21h21Z — banco fechado em três elegíveis, critério e linha mestra escritos, SERP das três fichas classificada. Faltava a leva.

### 1. O TERCEIRO MUNDO DA ESCADA DE LOTAÇÃO ERA UM RAMO DE RESGATE, E RAMO DE RESGATE É RÉGUA QUE NÃO PODE FALHAR

A leva 4 escreveu, em 14/09 de manhã, os **três** mundos da tabela de lotação: arranjo que FIXA o número (solitário, casal), número declarado (cardume, grupo) e **arranjo sem número** (harém). Publicou os dois primeiros. O terceiro ficou escrito e sem nenhuma página que o alcançasse — o banco não tinha ficha de harém e o mapa do arranjo trazia `abertura` vazia para ele.

**Ele estava errado, e do jeito exato que a seção 8 do contrato descreve.** Sem abertura própria, a ficha caía no ramo de resgate, que abre pela tradução do `aquametria_peixes_como_vive()` — e essa tradução carrega a oração do temperamento. A primeira frase da ficha do platy sairia assim, e foi assim que ela saiu na primeira renderização de bancada desta execução:

> Para o platy, que vive em harém, um macho para várias fêmeas, **e a fonte o declara pacífico**, o seu aquário precisa de 60 cm de frente…

Procedência abrindo a página é exatamente o que o **item 4 do despacho da Sentinela de 13/09/2026** tirou das onze fichas antigas (15.2). Ele voltaria pela porta de trás, na primeira ficha de harém, e nenhum portão podia ver: as 14 fichas no ar não passam por ali.

O conserto não foi dar uma abertura ao harém e parar: **o ramo de resgate deixou de existir**. `aquametria_peixes_pode_virar_ficha()` passa a exigir que o termo esteja no vocabulário fechado — que é o que o cabeçalho da 1.7.0 já afirmava ("termo fora dele devolve null e a espécie não vira ficha") e o código **não fazia**: bastava `cardume_minimo` preenchido para uma `convivencia` qualquer virar página, e a ficha abriria chamando de "cardume mínimo" um peixe que ninguém declarou de cardume. Com o portão fechado dos dois lados — o esquema enumera os cinco valores, o validador reprova o sexto, o mapa tem os mesmos cinco — os três ramos da abertura cobrem o mundo inteiro e nenhum deles é inalcançável.

A abertura do harém é a tradução do próprio termo, do mesmo jeito que "e é um por aquário, não dois" traduz `solitario`: **"e harém quer dizer mais fêmeas do que machos, nunca um casal"**. Ela não traz número porque os três registros têm a mesma sentença de fonte por trás — mais fêmeas por macho, para dissipar o assédio — e **nenhum deles declara quantas**.

### 2. DOIS DEFEITOS DE CONCORDÂNCIA QUE JÁ ESTAVAM NO AR, os dois medidos no HTML servido

Os dois nasceram com a frase no plural, e os dois só erram quando a contagem é UM — por isso passaram por 14 fichas sem ninguém ver.

1. **"1 ficaram fora porque o banco os declara agressivos: mato-grosso."** Lido com `curl` em `/peixes/corydoras/quantos-litros-para-coridora-sterbai/` em 14/09/2026. O banco tem **um** peixe agressivo, e até esta leva ele ou aparecia junto com o betta (dois, e a frase fica certa) ou não encostava na faixa de temperatura da ficha (zero, e a frase nem sai). A coridora sterbai já servia a versão errada desde 12/09. Nasceu `aquametria_peixes_concorda()`, e ela vale para as três contagens da prestação de contas.

2. **"cabem 1 coridora sterbai pelo critério apertado e 6 pelo folgado. A diferença entre os dois é de 4 vezes."** Mesma página, mesmo `curl`, e são **duas** coisas numa frase só. O verbo — e o número: o "4 vezes" saía das CONSTANTES da ilha (4 L/cm contra 1 cm/L), e a razão entre as réguas só é a razão entre os NÚMEROS DA TELA enquanto o arredondamento para baixo não morde. **Ele mordia em dez das quatorze fichas no ar** — 4,2 no cardinal e no mato-grosso, 4,6 no tetra ember e no tetra-brilhante, 5 no tetra-negro, 5,5 no gurami mel e na coridora bronze, 6 na sterbai — e morde mais no peixe-espada, que com 16 cm é o maior peixe com ficha desta ilha: a linha do meio dá 7 e 1, que é **sete** vezes, com a frase anunciando quatro a uma linha de distância dos dois números que a desmentem.

É o **escopo de afirmação** da seção 8, na forma mais silenciosa dele: a frase estava certa sobre as duas réguas e falsa sobre os dois números que ela mesma acabara de imprimir. A razão agora é derivada dos dois números impressos. E o caso em que o critério apertado não põe **nem um** ganhou frase própria, porque "cabem 0" no aquário que a própria fonte declara como mínimo seria publicar uma contradição sem nome — nenhum peixe do banco chega lá hoje, e quem mede esse ramo é a mutação que PRODUZ o mundo.

### 3. A LINHA MESTRA E O CRITÉRIO DA CATEGORIA FORAM REESCRITOS NA LEVA QUE OS PUBLICOU

Mesma família do que a `bettas` teve de fazer em 14/09 de manhã: **texto de categoria escrito antes da leva promete o que a tabela não paga.** A linha mestra de 13/09 dizia que o número que decide o aquário "não é quantos você comprou, é quantos vão existir daqui a três meses, e o macho é quem manda nessa conta" — e nenhuma fonte deste banco declara taxa de reprodução, ninhada ou prazo. Pior que isso: ela dizia que manda o **macho** e o critério, duas telas abaixo, dizia que manda "o tamanho adulto da **fêmea**". Duas afirmações contrárias na mesma página, nenhuma medida.

E a do critério era falsa por mais um motivo, que o próprio banco registra: dos três, **dois declaram o porte da fêmea e o do plati variatus não declara sexo nenhum** (a base publica 7,0 cm TL para macho/não sexado). A página não mostra o sexo em lugar nenhum, então a frase afirmava sobre um dado que ela não serve.

As duas dizem agora o que a tabela paga linha a linha: o **arranjo sem número** (a coluna "Como vive" repete "em harém, número não declarado" três vezes — é a única categoria do eixo assim) e a **frente que varia em duas vezes dentro de um gênero só**. E a primeira escrita da nova linha mestra **reprovou no portão da voz**, por duas coisas ao mesmo tempo: abria por "as fontes destes três declaram", que é procedência na primeira frase, e falava do banco em vez de falar com quem lê.

### 4. A SERP DA MÃE, CLASSIFICADA NESTA EXECUÇÃO — e é a única do eixo em que o top não fala do assunto

As três fichas mantêm `serp_em` **13/09/2026**, que é quando foram medidas. A mãe declara **14/09/2026**, porque a consulta dela não existia classificada e herdar o padrão seria mentira.

**"quantos litros para peixes vivíparos"**, medida em 14/09/2026: nenhuma das sete primeiras respostas fala de vivíparo. A consulta devolve as páginas genéricas de "quantos peixes cabem no meu aquário" — dois blogs de pet shop (Terra Zoo, Agrosete), uma ficha de aquarismo (peixeseaquarismo), uma loja portuguesa (Kiwoko), um fórum (Brasil Reef), a MyAquarium e um Blogspot de 2013 —, e o que elas publicam é a regra por centímetro de peixe **em três versões que discordam entre si na mesma página de resultados** (1 L por cm até 2 cm, 1,5 L por cm de 2 a 5 cm, 2 L por cm de 5 a 10 cm). Na busca vizinha, com os nomes dos peixes, aparece ainda o "10 litros vagos + 5 litros por peixe" — a conta per capita que esta ilha recusa desde a leva 1, publicada ali como se fosse regra. Nenhum domínio forte, nenhuma atribuição, e o próprio resumo da busca termina mandando o leitor pesquisar espécie por espécie, **que é exatamente a tabela que esta página é**. ALVO, e do tipo mais limpo do eixo: aqui a ilha não disputa um número com ninguém, ela ocupa um lugar vazio.

### 5. A CATEGORIA DECLARA AS CINCO POECIIDAE, e aqui os dois barrados não são vizinhança

São o **guppy** e o **molly**, os dois vivíparos mais vendidos do Brasil, cada um a UM campo de entrar — o guppy tem duas urls de um corpo só (aviso E15, espelho não confere espelho) e o molly não tem `comprimento_minimo_aquario_cm`. Sem declará-los, a frase de lista fechada desta página diria que todo vivíparo que o banco sustenta já tem página, e o banco sustenta os dois registros. Declarados, eles saem da tabela e entram na lista de fora, com nome e causa.

**A parede do molly não mudou nesta execução e continua sendo a mesma:** os dois corpos já foram perguntados em 13/09 — o compêndio publica a seção de dimensões vazia e a base científica, em duas passadas limpas, devolveu o número da espécie vizinha. O desbloqueio depende da leitura direta, que é o **despacho de egresso aberto para o Raphael** em `dados/despachos.md`. Nada foi tentado de novo aqui, e nada foi completado por vizinhança.

### 6. UM TERCEIRO DEFEITO NO AR, ACHADO LENDO A FICHA NOVA COMO UM LEITOR LERIA — e ele era total

A linha **"De onde vem"** da tabela de fontes da ficha do plati variatus servia *"bacias que drenam para o Golfo do **Mexico**, do sul de Tamaulipas ao norte de Veracruz (**Mexico**)"*. Medido no banco inteiro: **15 de 15** registros que declaram `origem_geografica` estavam sem **um** acento — "America do Sul: bacia do rio Parana", "Asia: Paquistao, India e Bangladesh", "Sudeste asiatico: Malasia, Singapura e Indonesia". Está no ar desde 12/09/2026, em onze fichas, e foi conferido com `curl` na página do tetra ember antes de qualquer conserto.

É a **mesma cicatriz de 12/09**, no campo vizinho. Aquela correção acentuou `nomes_populares_br`, criou a tabela declarada de forma-errada → forma-certa no esquema e a regra **E17** no validador. O que ela não fez foi perguntar **quais outros campos vão inteiros para a tela** — e `origem_geografica` vai, na linha "De onde vem" de toda ficha. Regra que nomeia um campo não protege o campo vizinho, e o vizinho aqui nasceu do mesmo arrasto: o resto do arquivo é nota interna e por isso é escrito sem acento.

Os 15 foram acentuados e **a régua foi ampliada em vez de repetida**: a lista de campos de tela passou a morar no esquema, ao lado da tabela, e a E17 varre os dois. Os 21 topônimos entraram na tabela declarada — que continua sendo declarada e nunca adivinhada por vizinhança, como o próprio esquema diz. A régua foi exercitada desacentuando um registro de propósito: reprova com os dois tokens nomeados.

### 7. UMA TROCA DE TELA NO BANCO, declarada

Os nomes populares do `xiphophorus-hellerii` foram reordenados para pôr **"peixe-espada"** na frente de "espada". É o precedente da colisa-anão, de 14/09 de manhã, aplicado pelo mesmo motivo: `aquametria_peixes_nome()` lê o PRIMEIRO do campo e é ele que vai para o título, para o corpo e para a tabela da categoria; a consulta classificada é "quantos litros para peixe espada", e "espada" sozinho é ambíguo fora do aquarismo. Nenhum número mudou, e a troca está escrita na observação do registro.

### Verificação

**Bancada, 0 falha:** `teste-peixes` **2256** afirmações (eram 1775), `teste-voz` TUDO OK com as quatro páginas novas dentro, `teste-arvore`, `teste-datas-schema` 102 (eram 90), `teste-seo-tecnico` 411, `teste-ga4` 568, `teste-apelidos` 59, `teste-escada-compra` 522, `conferir-entidades`, `conferir-slugs`, `conferir-protecao-funcoes`, `validar-especies` 37 registros com o mesmo aviso E15 do guppy (e a E17 agora varrendo os dois campos de tela), `testar-validador-especies` 24 casos, `validar-produtos`, `php -l` limpo em tudo. **Mutações:** a bateria foi de 81 para **90**, com **90 de 90 reprovadas e 0 inertes**. **Navegador:** 658 medições em 35 páginas × 6 larguras, 0 px de rolagem horizontal, console limpo.

**No ar, em UM disparo do Sync:** `/status` na revisão **82**, igual à do manifest; as quatro URLs novas em HTTP 200; zero `&#038;` dentro de `<script>` nelas; o `wp-sitemap` publica **36** URLs (33 páginas + 3 posts), as quatro novas incluídas; `conferir-peixes-no-ar` **614** afirmações (eram 470) e `conferir-datas-e-voz-no-ar` **248**, as duas com 0 falha. As duas frases consertadas foram lidas no HTML servido: *"1 ficou fora porque o banco o declara agressivo"* e *"cabe 1 coridora sterbai pelo critério apertado e 6 pelo critério folgado. A diferença entre os dois é de 6 vezes"* — onde até hoje iam ao ar o plural e o quatro.

**Receita, sem mudança:** espécie não é produto e nenhum produto entrou ou saiu do banco. Seguem 39 dos 78 com ficha de loja, **0 com piso**, 78 sem piso; dos 39 sem ficha, 9 não têm loja possível hoje. **Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

### As três mutações que passaram, e por que cada uma era uma trava que faltava

A bateria subiu de 81 para 90 mutações e, na penúltima rodada, **três passaram**. Nenhuma delas era ruído:

1. **Duas não eram mutação nenhuma — eram cobertura com nome de trava.** Elas mudavam o porte do peixe-espada no banco **e** no catálogo do snippet, para produzir o mundo em que o critério conservador não põe nem um exemplar. Só que a régua do teste **recomputa o esperado a partir do banco**: as duas metades andaram juntas e a página continuou certa. É o "as duas metades erram juntas" da seção 8, do lado benigno — **mundo novo em que as duas metades concordam prova que o ramo roda, nunca que existe trava.** As duas foram reescritas para produzir o mundo **e** quebrar alguma coisa: numa, a frase do zero volta a dizer que o apertado põe um; na outra, o número do critério folgado sai do lugar errado.
2. **A terceira tirava a guarda do vocabulário fechado e não quebrava nada**, porque nenhuma espécie do banco tem termo desconhecido — tirar código que o mundo de hoje não alcança não muda uma afirmação. Ela passou a produzir o mundo: uma espécie com `convivencia` fora dos cinco valores do esquema **e** com cardume preenchido, que é o caso exato que a guarda existe para barrar.

E ela achou uma afirmação faltando, que é o achado de processo deste bloco: **as duas afirmações que eu tinha escrito sobre a abertura eram negativas**, e negativa é verde sobre a frase errada. Com a guarda removida e o termo desconhecido no banco, a página abria *"Para um  de 5 tetra-negro"*, com o rótulo **vazio** no meio da frase — não é a forma do número (o rótulo não está lá) nem a do arranjo (não há travessão), e as duas réguas ficavam verdes. Nasceu a afirmação **positiva**: a abertura é uma das duas formas declaradas, e as duas são montadas aqui, à mão, a partir do banco.

Sobrou ainda uma lição de ferramenta: com o termo desconhecido, este arquivo **morria de `KeyError`** antes de terminar a medição. **Verificador que estoura não diz o que estava errado, só que algo estava** — as três buscas no vocabulário passaram a devolver sentinela nomeado, e a cadeia de ramos do teste passou a espelhar a do snippet (quem decide é o rótulo do arranjo, não a presença do número).

### O contador de fichas de uma ferramenta de conferência estava digitado

`conferir-datas-e-voz-no-ar.py` afirmava **"achei as onze fichas de peixe no sitemap"**, com o 11 escrito à mão em 13/09. A leva 4 pôs catorze no ar e não tocou nele; a afirmação só reprovou **aqui**, na leva 5, com dezessete — uma leva inteira depois de virar falsa, e só porque a ferramenta não foi rodada no fecho da leva 4. É o **"número de tela digitado"** que esta ilha persegue nas páginas, dentro da própria ferramenta de conferência. O número passa a sair do registro do eixo, e cresce sozinho com a próxima leva.

### Próximo passo

1. **A LISTA DOS BARRADOS NA TELA DA CATEGORIA já existe** — esta leva a viu funcionar pela primeira vez com barrados que importam. O que continua aberto é o **molly** e o **guppy**, e os dois dependem do despacho de egresso do Raphael. `/peixes/vivaparos/` iria de 3 para 5 fichas no dia em que ele abrir, e é a categoria com o maior salto disponível do eixo.
2. **A PRÓXIMA CATEGORIA DO EIXO**, e ela é decisão de banco antes de ser de leva: `/peixes/ciclideos-anoes/` tem **1** elegível (ramirezi) e `/peixes/plecos-e-limpa-vidros/` tem **1** (otocinclo). As duas estão longe do mínimo de três do 16.5, e nenhuma nasce sem coleta nova.
3. **A escada de compra na tela**, no minuto em que houver `url_busca` — bloco inteiro nas quatro calculadoras de uma vez.
4. **A leitura de 16/09** continua tendo o que responder sobre a leva de 08/09 e continua não travando leva nenhuma: 36 URLs, abaixo do piso de 40.

## 2026-09-14 11h25Z — LEVA 4: A TERCEIRA CATEGORIA DO EIXO, E O EIXO APRENDE QUE PEIXE NEM SEMPRE VIVE EM CARDUME (peixes 1.7.0, esquema de espécies versão 4, manifest revisão 77, `/status` conferido às 12h09Z; QUATRO URLs novas, a primeira leva desde 12/09)

**A ESCOLHA DA ILHA: segunda tentada.** A clubedomosaico era a primeira pela 18.1 — tem despacho ABERTO do Raphael de 14/09, os quatro achados da artesã usando o ateliê — e o meu push de reserva foi recusado: outra execução a reservou às 11h18Z pelo mesmo motivo. O passo 5 da seção 1 manda voltar ao passo 2, e nenhum force push aconteceu. Das duas que sobraram, a aquametria tinha a `ultima_execucao` mais antiga (23h19Z contra 23h47Z da robometria), e as duas estavam com `executando_desde: null` — que pela 1.1 já significa que não há bloco da Fundação vivo, então o git não precisou desempatar. Os três `PROMPT.md` foram lidos antes de escolher. **Rede pela 20.2, antes de trabalhar:** home em 200 e `/status` na revisão 76, igual à do manifest, em UMA passada.

**POR QUE ESTE BLOCO:** era o item (1) do PRÓXIMO da execução das 23h19Z, e o que o travava era calendário, não trabalho. O teto da 21.4 estava em 3 de 3 levas gastas na semana que terminou no domingo 13/09; a semana virou em 14/09 e a leva 4 nasceu com 0 de 3. A SERP das quatro consultas já estava classificada desde 13/09 e o critério da categoria já estava escrito.

**O DESPACHO DE RAIZ QUE ERA MEU, FECHADO.** `dados/despachos.md` tinha um despacho endereçado a "FUNDAÇÃO (quem reservar a aquametria)": o `bloco_atual` do `ESTADO.md` desta ilha não era YAML válido. Reservei a ilha, então ele é meu pela letra dele. Passei os três `ESTADO.md` por `yaml.safe_load` **depois** de escrever a reserva no cabeçalho — que é o commit mais provável de quebrar o bloco, porque mexe numa linha dele — e os três passam. Fechado e movido para FECHADOS, com a medição escrita. A regra que sobrevive a ele é a da seção 2 do contrato, e ela não era dele.

### 1. O QUE A CATEGORIA CUSTOU, E NÃO ERA PREENCHER A LISTA

Preencher `especies` da `bettas` é uma linha. O que esta leva pagou é outra coisa: **até 13/09 as ONZE fichas no ar eram `convivencia: cardume`, sem exceção**, e por isso a palavra "cardume" estava DIGITADA em sete lugares do corpo da ficha — a abertura, a legenda da tabela de lotação, o contraexemplo do cubo, a chamada do filtro, o bloco da espécie agressiva, a linha da tabela de fontes e o rabicho do JSON-LD. Era verdade em toda página publicada e é **falsa em três das quatro** desta leva: o betta vive sozinho, a colisa-anão vive em casal e o gurami mel vive em grupo — e a fonte dele escreve, com todas as letras, que a espécie **não** é gregária no sentido dos peixes de cardume.

É a cicatriz da seção 8 do contrato no lado que ela chama de **régua escrita para um mundo que nunca aconteceu**: o esquema desta ilha permite `solitario`, `casal`, `harem` e `grupo` desde o primeiro dia — `aquametria_peixes_pode_virar_ficha()` cita os três primeiros **pelo nome** — e o banco nunca tinha produzido um. Nenhum portão podia falhar, e nenhum falhou.

O vocabulário agora é **fechado** e mora num mapa só, `aquametria_peixes_arranjo()`. Termo fora dele devolve `null` e a espécie não vira ficha.

### 2. DUAS RECUSAS QUE A LEVA ESCREVEU, E A SEGUNDA ESTAVA LATENTE NO AR

1. **A escada de lotação só sobe onde a fonte deixa.** No betta a fonte declara um por aquário; a tabela pré-renderizada de "N exemplares" subiria até 20, oferecendo com cara de tabela exatamente o número que a fonte recusa — e a tabela é a metade que um modelo de linguagem lê. Onde o arranjo FIXA o número (solitário 1, casal 2) a escada tem um degrau e a página diz por quê; onde a fonte declara um número de grupo, começa nele; onde declara o arranjo e não o número (harém, que é o mundo inteiro da próxima leva), a escada é a de leitura e NENHUMA linha se chama mínima.
2. **O conselho do bloco da espécie agressiva se inverte com o arranjo.** "Quanto maior o cardume, menos a agressão se concentra num alvo só" é certo para o mato-grosso e é o CONTRÁRIO do que a fonte diz do betta, que é agressivo **e** solitário: ali ela manda um por aquário. E a frase antiga ainda iria ao ar **quebrada**, porque `$card` é nulo nessa espécie — "cardume mínimo de  e não de dois".

### 3. O DEFEITO QUE JÁ ESTAVA NO AR, medido no HTML servido

`/peixes/corydoras/` servia **"fechada quer dizer que todo TETRA que o banco desta ilha sustenta já tem a página dele"**. Medido com `curl` em 14/09/2026, na página das coridoras. É a mesma cicatriz do "São 4 tetras" que a leva 3 pegou ANTES de publicar, escondida um nível mais fundo: ela mora num ramo que só é alcançado quando a categoria **fecha**, e até 12/09 só os tetras tinham fechado. **Ramo novo herda o texto do mundo antigo**, e nenhuma contagem estava errada — só a palavra.

O sujeito passa a vir declarado por categoria, como o `plural`. Na mesma família e na mesma passada: o exemplo da pergunta do nível 2, que era **"quantos litros para dez neons" digitado em toda categoria**, passa a ser a consulta da própria página.

### 4. A FAIXA DO GRUPO, E ELA CUSTOU UM CAMPO DE ESQUEMA (versão 4)

O compêndio recomenda, do gurami mel, **"não menos que 4 a 6 exemplares"**. O piso morava em `cardume_minimo` desde 13/09 e o teto não tinha onde morar — a ficha publicaria metade da recomendação, e completá-la de cabeça seria inventar a metade que falta. Nasceu `cardume_recomendado_ate`; **o número sai da MESMA sentença já transcrita em `fontes[]`**, sem passada nova de coleta, colhida em duas passadas independentes em 13/09. O validador ganhou a regra **E18** (teto sem piso não é faixa; teto menor ou igual ao piso é faixa invertida), com dois casos no auto-teste.

**E a lista de regras do esquema parava em E16 enquanto o código já cobrava E17** (acentuação de nome de tela, implementada em 12/09). Foi por pouco que a regra de hoje não nasceu com o mesmo id. A E17 entrou na lista, com a nota de que ela já existia.

### 5. A CATEGORIA DECLARA AS CINCO OSPHRONEMIDAE, E NÃO SÓ AS TRÊS QUE PASSAM

Primeiro mundo REAL do ramo de barrados que a 1.6.0 escreveu em 13/09 sem ter caso no banco para exercitá-lo: os dois guramis grandes têm duas fontes cada e o portão os barra por `convivencia`, então saem na página com nome e causa. **Sem declará-los, a frase de lista fechada diria que todo betta e todo gurami que o banco sustenta já tem página — e o banco sustenta os dois.** As quatro mutações que PRODUZIAM aquele mundo continuam, porque agora elas provam o ramo VAZIO da mesma régua.

### 6. UMA TROCA DE TELA NO BANCO, declarada

Os nomes populares da colisa foram reordenados para pôr **"colisa-anão"** na frente. `aquametria_peixes_nome()` é documentada como "o nome que a pessoa digita" e lê o PRIMEIRO do campo — e a classificação de SERP de 13/09 mediu que a consulta brasileira é "quantos litros para colisa anão". Com "colisa" na frente, o título da ficha e o corpo dela serviriam nomes diferentes a uma linha de distância, que é o defeito que o item 4 do despacho da Sentinela de 13/09 já pagou nas nove páginas de conteúdo. Nenhum nome saiu da lista e nenhum campo de biologia foi tocado.

### 7. TRÊS DEFEITOS QUE A PRÓPRIA BANCADA ACHOU ANTES DE QUALQUER URL NASCER

Estes não estavam no ar e não chegaram lá — e valem mais escritos que escondidos, porque os três têm a mesma forma: **frase que nasce certa na primeira página em que é escrita e vai errada para a do lado.**

1. **A comparação com a base era frase pronta.** O ramo do arranjo fixo dizia que "as duas réguas ficam bem abaixo da base que a fonte declara". Verdade no betta — 6,5 a 26 litros contra 47,3 da base —, **falsa na colisa-anão**, onde o critério conservador pede 76 litros e a base dá 63. Pior: ia também dentro do JSON-LD, onde um modelo de linguagem a cita sem ter como conferir. Agora a comparação é **derivada**, resolvida num lugar só (`aquametria_peixes_lotacao_contra_base()`), e as duas superfícies que a publicam leem dali — não podem discordar.
2. **Duas `Question` de mesmo nome no mesmo `FAQPage`.** A pergunta do ramo do arranjo fixo repetia o `titulo` da página palavra por palavra. Nenhuma das onze fichas antigas podia produzir isso, e por isso ninguém tinha medido. A pergunta virou a que só esta página responde: se a régua de 1 cm por litro serve para um peixe cujo número a fonte fixa.
3. **A tabela de "quantos cabem" respondia à pergunta errada em silêncio.** No aquário mínimo do betta ela dizia "cabem 7" — duas telas depois de a página declarar um por aquário. A régua de lotação conta centímetro de peixe e não sabe de comportamento; agora a página diz isso na mesma tela, e o limite da fonte aparece ao lado.

**E o portão da voz reprovou a primeira escrita da abertura do arranjo fixo**, que dizia "que é o que a fonte declara por aquário": procedência não abre página (15.2), que é a régua que o item 4 do despacho da Sentinela de 13/09 cobrou nas onze fichas. A frase de cada arranjo passou a vir declarada no mapa, sem a palavra fonte.

### VERIFICAÇÃO, 0 falha

**Bancada:** `teste-peixes` **1775** afirmações (eram 1302); `teste-voz` TUDO OK, com as quatro páginas novas e as três fichas na régua da ficha de peixe; `teste-arvore`; `teste-datas-schema` 90; `teste-seo-tecnico` 375; `teste-escada-compra` 522; `teste-ga4` 504; `teste-apelidos` 59; `conferir-entidades`; `conferir-slugs`; `conferir-protecao-funcoes` (44 funções no snippet dos peixes, todas dentro de `function_exists`); `validar-especies` 37 registros, 0 erro e o mesmo aviso E15 do guppy; `testar-validador-especies` 24 casos; `validar-produtos` 78 produtos, 0 erro; `php -l` limpo.

**MUTAÇÕES: **81 de 81 reprovadas, 0 INERTES**, rodadas do zero sobre a árvore final. A bateria foi de 56 para 81 mutações, e o valor delas não é o placar: **duas passaram na penúltima rodada, e cada uma era uma trava que faltava.** (1) *O rótulo da tabela de fontes volta a ser digitado* passou porque a régua da palavra "cardume" era minúscula e a LINHA da tabela escreve "Grupo mínimo" com maiúscula — a página do gurami mel chamava o peixe de cardume numa superfície e não na outra, e o portão só olhava uma. (2) *O teto sai da escada* passou porque o teto do gurami mel é 6 e o 6 já está na escada de leitura por conta própria: a mutação media a coincidência do banco de hoje, não a regra — e o comentário do próprio código tinha previsto isso. Ela virou **mundo produzido**, que fabrica a faixa ímpar de 4 a 7 nos dois lados antes de tirar o teto da escada..** 

**Navegador:** **578 medições** em 31 páginas × 6 larguras, 0 px de rolagem horizontal, console limpo, em duas passadas — a segunda depois do conserto da comparação com a base.

**AS TRÊS PÁGINAS JÁ NO AR QUE MUDAM, e só elas**, medido por diff do corpo servido contra o render local, frase a frase: `/peixes/corydoras/` (o substantivo digitado, o exemplo da pergunta, a cláusula que supunha cardume e a irmã nova no cluster), `/peixes/tetras/` (as três últimas) e `/peixes/` (a categoria `bettas` vira link com a contagem própria, e o total de fichas vai de 11 para 14, contado na hora). Nenhuma outra frase de nenhuma outra página se move.

**NO AR:** `/status` na revisão **77**, igual à do manifest, em UM disparo com 20 aplicados. As quatro URLs novas em **200**, zero `&#038;` dentro de `<script>` nas quatro, e o sitemap publica **32** URLs (29 páginas + 3 posts), que é o número que o cabeçalho do `ESTADO.md` passa a declarar. `conferir-peixes-no-ar.py` **470** afirmações (eram 380), 0 falha — as 90 novas medem as quatro páginas no HTML SERVIDO, inclusive a frase de lista fechada das coridoras, que era o defeito. E a prova de que o conserto chegou: `/peixes/corydoras/` agora serve "fechada quer dizer que **toda coridora** que o banco desta ilha sustenta", lido com `curl`.

## 2026-09-13 23h19Z — A PRESTAÇÃO DE CONTAS DA SEÇÃO 7 ALCANÇA QUEM NÃO ESTÁ NA TABELA (peixes 1.6.0, manifest revisão 76, `/status` conferido às 23h38Z em UM disparo com 20 aplicados; NENHUMA URL nova, NENHUMA página criada, NENHUMA leva consumida)

**POR QUE ESTE BLOCO, com a leva 4 escrita como próximo passo.** A leva 4 (`/peixes/bettas/`) espera o CALENDÁRIO e não trabalho: o teto da 21.4 segue em 3 de 3 levas gastas nesta semana e 13/09 é domingo — esta execução rodou às 23h19Z de domingo, então a leva 4 continua nascendo só a partir de 14/09, exatamente como a execução das 21h21Z já tinha medido. O item (2) da lista é a leva seguinte, e vale o mesmo. O (4), a escada na tela, segue provadamente dormente com `url_busca` null nos 78 produtos. Sobrou o **item (3)**, que a execução anterior nomeou como dívida NOVA no `ESTADO.md` e deixou marcada como "merece bloco próprio". É este.

**A ESCOLHA DA ILHA.** Segunda ilha tentada: a robometria foi reservada às 23h18Z por outra execução e o push de reserva desta foi recusado por cerca de um minuto; o passo 5 manda voltar ao passo 2 e nenhum force push aconteceu. A clubedomosaico foi reservada às 23h18Z por uma terceira. Antes de escolher, os três `PROMPT.md` foram lidos: **nenhuma ilha tinha despacho aberto para a Fundação** — o da Sentinela de 13/09 desta ilha está com os itens 1 a 4 cumpridos, o 5 é registro e o 6 está suspenso pela seção 21 —, então a 18.1 não se aplicou e valeu a rotação da seção 1, com a aquametria de `ultima_execucao` mais antiga entre as que sobraram. Rede conferida pela 20.2 antes de trabalhar: home em 200 e `/status` na revisão 74, em uma passada.

### O BURACO ERA ESTRUTURAL, E NÃO DE TEXTO

A seção `/peixes/` servia **"São 29 espécies"** e não tinha como dizer que o banco tem **37**, nem por que os outros 8 não estão ali. Não era descuido de redação: o catálogo embutido — o bloco que o `gerar-catalogo-especies.py` escreve dentro do snippet — carregava **só quem PASSA no portão**, então os barrados simplesmente não existiam do lado de cá. A regra da seção 7 do `ARQUIPELAGO.md` ("cada item da categoria consultada aparece exatamente uma vez na prosa da resposta — ou na frase que o recomenda, ou numa linha que diz por que ele não está") estava cumprida para quem está na tabela e para mais ninguém.

O custo disso é específico desta ilha: **ausência sem nome, numa página que fala do próprio banco, é indistinguível de espécie que a ilha nunca procurou.** O molly e o guppy são os dois vivíparos mais vendidos do Brasil, estão no banco, foram perguntados a dois corpos de fonte cada um, e quem abrisse `/peixes/` concluiria que a ilha nem sabe que eles existem.

### O QUE PASSOU A EXISTIR

O gerador escreve um **segundo bloco** no snippet, `aquametria_peixes_barrados()`, com o registro barrado, a família e o que falta em cada um. A seção publica os três números **contados na hora** — 37 no banco, 29 na contagem, 8 fora — e a lista dos ausentes; a página de categoria faz o mesmo com quem **ela declara** e a tabela não mostra.

**O MOTIVO VIAJA COMO CÓDIGO, E A TRADUÇÃO MORA NUM MAPA SÓ DO PHP.** Se o gerador escrevesse a frase pronta, mudar a redação de um motivo reescreveria o catálogo inteiro e moveria o `sha256` do manifest por causa de uma vírgula. O vocabulário de códigos é **fechado nos dois lados** e o gerador RECUSA gravar código fora dele — o portão produz motivo de duas formas, o nome seco do campo e uma frase de diagnóstico com URL dentro (`conflito em pH sem nome de corpo: https://...`), e a segunda **nunca pode chegar à tela**. Cortar a URL por heurística seria adivinhar por vizinhança, então o corte é por prefixo declarado e o que não casar PARA o script. Regra nova de portão que chegasse à tela como `comprimento_minimo_aquario_cm` seria vocabulário de dentro da fábrica na cara de quem lê.

**UM ITEM POR ESPÉCIE, E NÃO UM GRUPO POR MOTIVO** — a decisão é entre duas regras da seção 7 que se cruzam aqui. Ela manda que cada item apareça **exatamente uma vez** na prosa e também que **causa que o código separa, o texto separa**. O `danio-margaritatus` está a QUATRO campos de distância; agrupado por motivo ele apareceria em quatro lugares, quebrando a primeira regra, e fundido numa razão genérica quebraria a segunda. A saída é a espécie aparecer uma vez com cada causa em oração própria. A primeira versão repetia "falta" quatro vezes na mesma linha e ficou ilegível justamente na espécie que mais precisa ser lida; a enumeração com "e" antes da última resolveu sem juntar causa nenhuma.

**A ORDEM É DERIVADA, de quem está mais perto de entrar para quem está mais longe.** Ordem de arquivo é ordem de digitação, e quem lê esta lista quer saber quem está a um campo de distância — que é, aliás, a mesma frase que o critério dos vivíparos já publica.

### O DEFEITO LATENTE QUE SAIU JUNTO, E ELE É FILHO DA MESMA MUDANÇA

O cartão de categoria da seção virava link quando a categoria **DECLARAVA** espécie. Enquanto o snippet só conhecia quem passa, declarar e entrar na tabela eram a mesma coisa; com os barrados aqui dentro deixaram de ser, e **uma categoria que declarasse só barradas viraria link para uma página de tabela vazia** — a página fina que o 16.5 existe para não deixar entrar no índice de domínio novo. Quem decide o link passou a ser a contagem de quem está no catálogo. Pela mesma raiz, a frase **"esta lista está fechada"** ganhou a forma que faltava: com uma barrada declarada na categoria ela ficaria falsa sem mudar uma letra, que é a forma mais silenciosa do número de tela que envelhece.

### QUATRO MUTAÇÕES PRODUZEM O MUNDO, PORQUE O RAMO DA CATEGORIA NÃO EXISTE HOJE

Nenhuma das duas categorias no ar declara espécie barrada — `tetras` e `corydoras` estão com o conjunto vazio. Régua escrita para um mundo que nunca aconteceu nasce errada sem poder falhar (seção 8), então as quatro criam a declaração e só depois quebram: a categoria declara uma barrada e a bancada não percebe; declara, a bancada sabe, e a página cala; declara e a lista continua se dizendo fechada; e declara um id que o banco não tem, que é o erro de digitação capaz de encolher a tabela em silêncio.

### VERIFICAÇÃO

**BANCADA, 0 falha:** `teste-peixes.py` de **1246 para 1302** afirmações — com régua própria que recomputa o portão E os motivos do banco do zero, sem importar nada do gerador, e que lê o bloco do snippet em texto para cobrar as duas direções —, `teste-arvore.mjs`, `teste-voz.mjs`, `teste-datas-schema.py` 78, `teste-seo-tecnico.php` 339, `teste-escada-compra.py` 522, `validar-especies.py` (37 registros, 0 erro, 1 aviso conhecido — o E15 do guppy), `conferir-slugs.py`, `validar-produtos.py`, `conferir-protecao-funcoes.py` e `php -l` limpo.

**MUTAÇÕES:** `mutacoes-peixes.py` de **46 para 56**, **56 reprovadas, 0 INERTES**, cópia limpa passando em 1302. `mutacoes-arvore.py` 14 de 14. Nasceram dois auxiliares: `varias()`, para a mutação que toca snippet e bancada como UMA mudança, e `inverter_ordem_dos_barrados()`, que mexe só na ordem e em mais nada — afirmação de ordem só se mede mexendo na ordem, porque trocar um campo junto mediria o campo.

**NAVEGADOR:** 480 medições em 27 páginas × 6 larguras (360 a 1200 px), 0 falha, console sem mensagem. A lista nova é um `<ul>` e entra no caso que a seção 6 mede a 360 px.

**NO AR, DEPOIS DO SYNC:** `/status` na revisão **76**, igual à do manifest, em um disparo às 23h38Z. `conferir-peixes-no-ar.py` foi de **358 para 380** afirmações, 0 falha, medindo o HTML que o servidor devolve. A conferência da prestação de contas mora ali e não só na bancada por um motivo desta ilha: **o corpo da seção é um shortcode**, então mudança que vem só do snippet não move `post_modified` e não aparece em log de desembarque nenhum — o Sync pode dizer "0 aplicado(s)" e a tela ter mudado. A única prova é ler o que o servidor devolve, e é a mesma cicatriz dos nove títulos de 11/09.

### DUAS COISAS DE PROCESSO, DITAS EM VEZ DE ESCONDIDAS

1. **O `manifest.json` volta ao recuo de dois espaços** que o próprio `atualizar-manifest.py` grava. A execução anterior o deixou com um espaço, e é por isso que o arquivo inteiro aparece no diff desta — nenhuma linha de conteúdo mudou além do `sha256`, da `versao` e da `descricao` do snippet dos peixes.
2. **A bancada de navegador precisou de `npm install`** nesta nuvem: o `playwright` não vinha instalado e o `package.json` já existia justamente para isso. O Chromium não foi baixado — ele já está em `/opt/pw-browsers`, como o próprio `package.json` diz.

### RECEITA, sem mudança

39 dos 78 com ficha de loja, **0 COM PISO**, 78 sem piso; dos 39 sem ficha, 9 não têm loja possível hoje. Nenhum produto entrou ou saiu do banco — espécie não é produto, e este bloco não tocou produto nenhum. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

### ABERTO E NOMEADO

(a) o piso de 78 itens depende de uma sessão do painel; (b) a saúde dos 39 links no ar segue desconhecida; (c) a escada não está na tela, provadamente dormente com `url_busca` null nos 78; (d) a dimensão de 24 imagens segue nula, por `connect_rejected` no CDN da Shopee; (e) 18 arquivos seguem fora do manifest — este bloco **não criou arquivo nenhum**, então a dívida não cresceu; (f) a ilha não tem canal para pedido formal de titular, despacho do Raphael; (g) `GT-PL9DD7KW` e o Tempo Real do GA4 seguem como estavam; (h) **a dívida (h) do estado anterior está PAGA** — era exatamente esta.

### PRÓXIMO, com ordem e motivo

1. **LEVA 4 = `/peixes/bettas/`** com as três fichas, a partir de 14/09, quando o teto da 21.4 zera. A categoria está preparada desde 13/09 às 13h17Z e a preparação tem régua desde as 21h21Z.
2. **A LEVA SEGUINTE = `/peixes/vivaparos/`** com platy, espada e plati variatus, pronta pelo mesmo padrão: banco fechado, critério escrito, SERP classificada. **E agora ela nasce com a prestação de contas de fábrica** — as duas `Poecilia` que ficaram de fora já têm nome e causa escritos, e a página de categoria vai servi-los sozinha no dia em que a lista declarar as duas.
3. **A escada na tela**, no minuto em que houver `url_busca`, em bloco inteiro nas quatro calculadoras de uma vez.

## 2026-09-13 19h35Z — A ILHA GANHA A PÁGINA QUE FALTAVA DESDE QUE PASSOU A MEDIR, e a lista de terceiros dela nasce contada (casca 1.9.0, manifest revisão 72, `/status` conferido às 19h36Z na revisão 71 em UM disparo com 20 aplicados e a page #121 criada, e reconferido na 72 depois do conserto do portão dos peixes; a ilha vai de 27 para 28 URLs)

**POR QUE ESTE BLOCO, E NÃO OS TRÊS QUE O ESTADO ANTERIOR LISTOU À FRENTE.** Os três estavam medidos e travados, cada um por um motivo próprio, e nenhum deles cedia hoje:

1. **LEVA 4 (`/peixes/bettas/`)** espera o CALENDÁRIO, não trabalho: o teto da 21.4 estava em 3 de 3 levas gastas nesta semana, e 13/09 é domingo — ela nasce a partir de 14/09 sem nada pendente antes.
2. **A ESCADA NA TELA** continua provadamente dormente: `url_busca` é null nos 78 produtos, então o estado 2 da 25.2 nunca acontece e a linha discreta do estado 1 não tem para onde apontar.
3. **OS DOIS VIVÍPARA** seguem recusados, com o despacho de egresso aberto em `dados/despachos.md`.

O que sobrou da lista de "aberto" era o item **(d)**, e ele não dependia de nada: **a ilha não tinha página de privacidade.** Está escrito no `ESTADO.md` desde 12/09/2026 — o dia em que a etiqueta do GA4 entrou no ar — e a execução daquele dia o deixou nomeado com a justificativa certa para aquele momento: criar página nova teria alargado um despacho que pediu uma frase. Desde então a ilha passou três dias medindo audiência e publicando link de afiliado sem nenhuma página que dissesse isso a quem lê.

**A REGRA QUE PRECISOU SER DECIDIDA ANTES DE ESCREVER UMA LINHA, e ela subiu para o contrato.** O teto da 21.4 (3 levas por semana) estava gasto, e lido ao pé da letra ele congelava por uma semana exatamente a página que o site devia ao leitor. O motivo declarado da 21.4 diz o contrário do que a letra dela fazia: ela existe contra "despejar centenas de páginas", que é **padrão de fazenda** — e página de privacidade é o oposto disso. Então nasceu a **21.7** no `ARQUIPELAGO.md`: o teto conta **página de malha**, e as cinco que a 16.1 nomeia por nome (home, sobre, contato, divulgação de afiliados, privacidade) ficam fora dele, porque são família fechada, no máximo uma de cada por ilha, e nenhuma responde a uma busca. A fronteira está escrita dura de propósito — `/metodologia/` **não** entra na exceção, e nada que mire consulta entra —, e a exceção afrouxa só a CONTAGEM: o portão de dado, a SERP, a verificação no ar, a voz e a árvore continuam inteiros.

### O QUE ENTROU NO AR

`/politica-de-privacidade/` (`conteudo/politica-de-privacidade.md`, page #121), quinta e última página da família institucional desta ilha. Fica na raiz pelo mesmo veredito que pôs `/metodologia/` lá. **Não tem mãe e não tem irmã**, então nenhum cluster a alcança — o que a tira de órfã pelo 16.4(f) é o **rodapé**, que a linka das 28 páginas, e isso virou afirmação medida em vez de suposição.

A casca foi a **1.9.0** pelas duas superfícies que são dela: o degrau da trilha em `aquametria_casca_lugar()` (com o mesmo nome do H1, como já acontece com a divulgação de afiliados) e o link no rodapé, onde o rótulo é o reconhecível, "Privacidade".

### O ACHADO DO BLOCO NÃO É DA PÁGINA NOVA, É DE UMA FRASE QUE JÁ ESTAVA NO AR

A `/divulgacao-de-afiliados/` dizia, desde 12/09, que a etiqueta do Google era **"o único script de terceiro que carrega em qualquer página desta ilha"**. A medição desmentiu: além da etiqueta — que na verdade são **duas** tags, a `G-8Y26XFZF39` da casca e a `GT-PL9DD7KW` do Site Kit —, toda página pede a folha e os arquivos das fontes ao Google, e as quatro páginas com vitrine pedem a foto do anúncio à Shopee. A frase sobrevivia à letra ("script") e mentia ao leitor, que concluiria que nada mais sai dali. **É a mesma família do "afirmação em bloco tem o escopo do que foi medido"**: ela falava do site inteiro valendo só para uma categoria de arquivo. Saiu, e no lugar ficou o ponteiro para a lista completa.

### A LISTA DE TERCEIROS NÃO PODIA SER DIGITADA, E ESSE É O MIOLO DO BLOCO

Uma lista de terceiros escrita à mão numa página de privacidade **nasce certa e envelhece calada** no dia em que alguém acrescentar um plugin — e o leitor nunca descobre, porque a página continua com cara de conferida. É o "número de tela nasce contado, nunca digitado" (Clube do Mosaico, 11/09) e o "afirmação da página sobre o próprio banco se conta" (Robometria, 12/09), agora sobre o AR em vez do banco.

Nasce `ferramentas/conferir-privacidade-no-ar.py` (**19 afirmações, 0 falha**), e ele **não guarda a lista**: recolhe os endereços do HTML SERVIDO de cada URL do sitemap e cobra as **duas direções** — todo endereço do ar nomeado na página, e todo endereço nomeado ainda existindo no ar. A segunda direção é a que quase sempre falta, e sem ela a primeira tem porta dos fundos: bastaria a página listar meia internet para nunca mais reprovar.

**MEDIDO NAS 28 URLs, 13/09/2026:** nenhuma devolve `Set-Cookie`; quatro endereços carregam sozinhos (`www.googletagmanager.com`, `fonts.googleapis.com` e `fonts.gstatic.com` nas 28; `down-bs-br.img.susercontent.com` em 4) e um quinto só é contatado no clique (`s.shopee.com.br`, em 4). A separação é por **TAG**, que é estrutura: o que decide se o navegador liga sozinho é o elemento em que o endereço está, não a palavra em volta dele — e a página afirma coisas diferentes sobre os dois, então misturá-los seria publicar que a ilha entrega o IP de quem lê a um endereço que ela só linka.

### AS MUTAÇÕES PRECISARAM PRODUZIR O MUNDO, PORQUE O AR NÃO SE EDITA DAQUI

`ferramentas/mutacoes-privacidade.py`, **23 de 23**. Uma bateria que só quebrasse arquivo do repositório deixaria esta régua exatamente como a seção 8 descreve desde hoje de manhã: **verde desde sempre e sem nunca ter podido falhar.** O juízo do portão não mora na rede, mora em quatro funções puras, e cada mutação monta uma página que o site **não serve** e cobra a decisão certa: iframe de terceiro (esta ilha nunca teve um), endereço sem esquema (`//host`), e o **sósia do domínio da casa** — `naoeaquametria.com.br`, que uma comparação por "termina com" sem o ponto deixaria passar por família.

**Três portas dos fundos fechadas, e as três produzem página vazia passando:** o endereço citado **dentro de um `<script>`** (o próprio script do Google carrega o nome do Google dentro dele — se o extrator lesse o HTML inteiro, uma página que não nomeia ninguém passaria); o endereço citado **só no `<head>`** (canonical, `og:` e JSON-LD não são o que a página diz ao leitor); e a **página que não nomeia nada**, que passaria em todas as outras regras por vacuidade.

### UM NÚMERO DIGITADO CAIU DE CARONA, E ELE ESTAVA NUM PORTÃO

`conferir-peixes-no-ar.py` reprovou depois do desembarque, dizendo "o sitemap publica as 27 URLs da ilha". Estava certo em reprovar e **errado no que afirmava**: o total vinha de `URLS_ANTES_DO_EIXO = 13` somado ao eixo derivado. A leva 2 já tinha consertado metade desse mesmo defeito neste mesmo arquivo; a outra metade ficou. Trocar 13 por 14 só reagendaria o problema para a próxima página institucional, que é o que a seção 8 proíbe fazer com literal. Agora as páginas fora do eixo são **derivadas das duas fontes que criam página nesta ilha**: o `$base` de `aquametria_casca_definicao_paginas()` e os itens de `conteudo/` com `publicar=true` no manifest — e uma afirmação nova reprova se qualquer uma das duas leituras vier zerada, que é a trava do 26.2 (régua que lê a própria lista de um arquivo aprova tudo em silêncio no dia em que o arquivo perde a chave).

### O QUE ESTE BLOCO NÃO PÔDE FAZER, COM NOME E MOTIVO

**A página não oferece canal para pedido formal de titular, porque a ilha não tem caixa de e-mail.** Isso está escrito NA PRÓPRIA PÁGINA, numa seção chamada "O que falta nesta página, dito aqui em vez de escondido" — omitir seria pior. Na prática o caso do leitor não fica travado: não há dado dele no site para consultar, corrigir ou apagar, e a página explica que o que existe sobre a visita está com o Google e se resolve do lado dele. Criar caixa de e-mail é criar conta em plataforma, e a seção 7 proíbe a Fundação de fazer isso sempre. Virou despacho aberto em `dados/despachos.md`, e ele atravessa ilha: a clubedomosaico já registrava a mesma falta.

### VERIFICAÇÃO

**BANCADA, 0 falha:** `teste-voz` 782 afirmações em 25 páginas (era 24 páginas); `teste-arvore`; `teste-seo-tecnico` 339 (era 330); `teste-peixes` 1222; `conferir-slugs`; `conferir-entidades`; `conferir-protecao-funcoes`; `php -l` em tudo.
**MUTAÇÕES:** privacidade 23 de 23 (nova); voz 27 de 27; árvore 14 de 14; peixes 39 de 39 — as antigas rodadas inteiras para provar que nenhuma virou inerte com a casca nova, **0 inertes**.
**NAVEGADOR:** 70 medições em 10 páginas x 6 larguras, 0 px de rolagem, console limpo. A página de privacidade entrou nessa bateria de propósito: ela publica uma **tabela** cuja célula é um endereço longo e sem espaço (`down-bs-br.img.susercontent.com`), que é o caso em que a tabela não tem por onde quebrar — 0 px a 360 px.
**NO AR às 19h36Z, em UM disparo:** `/status` na revisão 71, igual à do manifest, 20 aplicados, page #121 criada. Rodados DEPOIS do Sync: `conferir-privacidade-no-ar` 19, `conferir-datas-e-voz-no-ar` 170, `conferir-peixes-no-ar` 358, `conferir-ga4-no-ar` 363 — **0 falha nas quatro**.
**REDE (20.2)** medida no começo: home e `/status` em 200. A medição em Chromium contra o site VIVO não foi possível e isso fica dito em vez de suposto — o Chromium do container não atravessa o proxy de egresso (`ERR_CONNECTION_RESET` em duas passadas, com e sem `proxy:` configurado), que é por que toda bancada `.mjs` desta ilha renderiza local. Consequência prática: **os nomes dos cookies que a etiqueta do Google grava não foram medidos, e por isso não foram publicados.** A página descreve o que o identificador faz, não como ele se chama.

### RECEITA, sem mudança

39 dos 78 com ficha de loja, **0 com piso**, 78 sem piso; dos 39 sem ficha, 9 não têm loja possível hoje. Nenhum produto entrou ou saiu do banco neste bloco.

Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

### PRÓXIMO, com ordem e motivo

1. **LEVA 4 = `/peixes/bettas/` com as três fichas — DESTRAVADA AGORA**, porque a semana virou em 14/09 e nada mais está na frente dela. O teto da 21.4 volta a 0 de 3, e a 21.7 deixa claro que a página de privacidade não gastou leva.
2. **A ESCADA NA TELA**, quando houver `url_busca` para ela servir, em bloco inteiro nas quatro calculadoras de uma vez, com o portão medindo a CLASSE EMITIDA e nunca a frase legível.
3. **Vivípara**, quando o egresso abrir ou aparecer um terceiro corpo.

## 2026-09-13 17h20Z — A ESCADA DA SEÇÃO 25 NASCE NA ILHA QUE A SEÇÃO 25 CITA PELO NOME: o piso deixa de ser prosa e vira número contado (esquema 10, manifest revisão 68, nenhuma URL nova, nenhum snippet reescrito)

**POR QUE ESTE BLOCO, E NÃO OS DOIS QUE O ESTADO ANTERIOR LISTOU À FRENTE.** O
"PRÓXIMO" da execução das 15h16Z tinha três itens, e os dois primeiros foram
medidos e estão travados hoje, cada um por um motivo diferente:

1. **A leva 4 (`/peixes/bettas/`) espera o calendário, não trabalho.** O teto da
   21.4 é de três levas por semana e a semana gastou as três. Hoje é domingo,
   13/09; a leva nasce a partir de 14/09 e não falta nada antes de escrevê-la.
2. **O banco dos vivíparos foi TENTADO nesta execução e os dois continuam
   recusados** — e uma das recusas ficou mais forte do que estava. Está abaixo.
3. Sobrou o que o próprio `ESTADO.md` chamava de espera do Raphael e que **o
   contrato chama de defeito**: a ilha não implementava a seção 25, escrita em
   13/09/2026 e que **cita esta ilha pelo nome** na 25.4-b. A 18.5 é explícita:
   verificação antes de construção, e ilha com defeito no ar não recebe página
   nova. Era este o bloco.

**O QUE FOI MEDIDO ANTES DE ESCOLHER, porque escolher bloco por suposição custa a
execução inteira.** `url_busca`, `url_produto` e `degrau` **não existiam em
nenhum arquivo desta ilha** — nem no esquema, nem no banco, nem nos snippets.
Não era dívida parcial: a seção 25 inteira estava fora.

**A FRASE DO PRÓPRIO ESTADO QUE CONTRADIZIA O CONTRATO.** O cabeçalho dizia que
os 30 produtos com anúncio "esperam a geração manual do link curto no painel, que
é a metade do Raphael". A 25.2 decide o contrário, com a palavra do dono citada
literalmente: *"deve ser 100% automático sem eu tocar"* — e a consequência
escrita logo abaixo, **"nada, nunca, fica na fila esperando o Raphael"**. O que
estava na fila não era a escolha: era o encurtamento. Este bloco separa as duas
coisas, e só a segunda depende de alguém.

### O que a nuvem alcança, e o que ela não alcança — remedido hoje, duas passadas

- `affiliate.shopee.com.br/offer/custom_link` responde **HTTP 200** e serve uma
  **casca de JavaScript**: zero ocorrência de `custom_link`, zero de `sub_id`,
  **zero de `input`**. Não é bloqueio de rede, é falta de sessão — e criar conta
  ou tocar na conta do Raphael está fora do que esta camada faz. É a mesma parede
  que o Clube do Mosaico mediu hoje mais cedo, agora medida também daqui.
- **A recuperação da url crua pelo título do anúncio foi tentada e recusada.** A
  25.4-b declara a dívida dos 39 links desta ilha como irrecuperável "sem
  clicar", mas o banco guarda `afiliado.anuncio_shopee`, o título exato — o que
  abriria um caminho sem clique: buscar o título e reencontrar a página. Não
  abre: `shopee.com.br/search` responde 200 e serve casca de JavaScript com
  **zero ocorrência de `shopee.com.br/` no HTML servido**. A dívida fica, agora
  com a saída fechada *medida* em vez de suposta.
- `mercadolivre.com.br` responde **403** desta nuvem, o que fecha também o degrau 2.
- Egresso de fonte técnica remedido e igual ao de sempre: `fishbase.se`,
  `fishbase.org`, `seriouslyfish.com` e `en.wikipedia.org` em **000**.
- A ilha em **200** na home e no `/status`, nas duas passadas.

### O que entrou

**O esquema aprendeu a escada (versão 10).** `afiliado` ganhou seis campos —
`degrau`, `url_produto`, `motivo_sem_url_produto`, `url_busca`,
`url_busca_produto`, `motivo_sem_url_busca` — e um bloco `escada_de_compra` com
os **quatro degraus da 25.1 nomeados**, a base da busca e o **termo de contexto
por entidade**. Os quatro degraus ficam declarados mesmo com o banco de hoje
usando um só, porque a escada é do contrato e não do banco.

**DUAS FRASES DO ESQUEMA FORAM REESCRITAS, NÃO ACRESCENTADAS, PORQUE JÁ ERAM
FALSAS.** As duas diziam que produto sem link não aparece no bloco de produto —
uma na observação de `plataforma`, outra na terceira linha de `afiliado.regras`.
A **V16**, escrita no mesmo arquivo, decide o oposto, e é a V16 que está no ar: o
cartão sai sem botão, com o selo "entrou pela ficha técnica, não pelo link". As
duas frases eram anteriores à V16 e sobreviveram a ela caladas. O que falta a
produto sem link não é presença: é **piso**.

**O DEGRAU DOS 39 LINKS VIVOS É NULL, E ISSO NÃO É PREGUIÇA — É A ÚNICA COISA
HONESTA A ESCREVER.** Seria fácil carimbar `degrau: 3` nos 39 e ficar verde. Mas
o degrau se lê da **url crua**, e ela se perdeu: `s.shopee.com.br` encurta a loja
oficial (degrau 1) e o anúncio de vendedor (degrau 3) com a mesma cara, e os dois
apodrecem de forma oposta. Daí sai a regra, e ela é **causal e não conveniente**:
o degrau e a saúde do link morrem **pela mesma causa**, então um único motivo
cobre os dois, e a V24 aceita degrau ausente **só** quando
`motivo_sem_url_produto` declara aquela causa. Uma das mutações é exatamente
tirar o motivo e deixar o degrau vazio.

**O PISO TEM DOIS ELOS, E SÓ UM DEPENDE DE ALGUÉM.** Nasce
`ferramentas/gerar-busca-de-produto.py`, que escreve `url_busca_produto` nos
**78** produtos compondo `marca + modelo + termo de contexto da entidade`. A
escolha da palavra-chave é da máquina, do começo ao fim, e já está feita: **no
dia em que houver sessão, é colar — nenhuma linha de código muda.** O que ficou
para o encurtamento está declarado item a item em `motivo_sem_url_busca`, com a
medição de hoje dentro.

**O TERMO DE CONTEXTO MORA NO ESQUEMA E NÃO DENTRO DO GERADOR**, pelo mesmo
motivo que a Robometria tirou a lista de tipos de dentro da régua hoje mais cedo:
lista dentro da régua envelhece calada, e **entidade nova entraria sem termo
nenhum com o banco inteiro verde**. A 25.3 diz o que isso traz para o cartão — a
JBL de caixa de som e a "Aquário" de roteador. É a mutação 10, e é a que mais
importa: ela não estraga registro nenhum, tira a lista do esquema, e sem a trava
o banco de hoje continuaria passando.

### A régua reprovou dois registros CERTOS, e a correção é da régua

A primeira versão cobrava a marca na busca de **todo** produto. Ela reprovou
`rs-50-50w` e `aquarios-do-rio-led-60cm`, que estão **certos**: os dois declaram
`marca: null` porque são produto sem marca. A 25.3 proíbe buscar **só por
marca**; quem não tem marca nenhuma não cai nessa armadilha. A regra passou a
cobrar a marca **de quem tem marca** e o contexto **de todos**, mais uma
afirmação nova — fora o contexto, a busca tem de identificar alguma coisa —, para
a correção não abrir a porta que ela fechou. É a mesma família do que aconteceu
com a régua de voz hoje mais cedo, quando "conforme" e "segundo" reprovaram três
primeiros parágrafos corretos.

### A dívida deixou de ser prosa e virou número contado

O `validar-produtos.py` passou a imprimir a escada, **recomputada do arquivo**:

```
com ficha (url)          39 de 78
com piso (url_busca)      0 de 78
itens_sem_piso           78 de 78
links_sem_degrau         39 de 39
links sem url crua       39 de 39
```

Enquanto isso era prosa no `ESTADO.md`, a dívida não tinha tamanho: o cabeçalho
dizia "39 esperam link" e **não dizia que 78 estavam sem piso**, que é outra
coisa e é a que a 25.2 chama de defeito. Uma das mutações troca a contagem por um
`78` digitado no lugar certo, e o portão pega.

### No ar às 17h38Z, em UM disparo

`/status` na **revisão 68**, igual à do `manifest.json`, 19 aplicados. E a
conferência que só o ar faz, rodada **depois** do Sync: `conferir-peixes-no-ar`
**356** afirmações e `conferir-datas-e-voz-no-ar` **170**, 0 falha nas duas, com
a home em 200. Este bloco não mudou uma linha do que o site serve, e é
exatamente por isso que as duas baterias no ar valem aqui: elas provam que a
revisão andou **sem** a tela andar junto, que era o desenho.

### Verificação na bancada, 0 falha

`teste-escada-compra.py` **522** afirmações (novo) · `mutacoes-escada.py`
**14 de 14, cada uma reprovada pela REGRA QUE A NOMEIA** — exigência um nível
mais dura que a das outras baterias desta ilha, porque defeito pego pela regra
vizinha prova que alguma trava existe, não que **esta** existe · `validar-produtos`
78 produtos, 0 erro, 9 avisos (os mesmos de antes) · `validar-especies` 36, 0
erro, o mesmo aviso E15 do guppy · `testar-validador-especies` 22 ·
`teste-peixes` 1222 · `teste-ga4` 440 · `teste-seo-tecnico` 330 ·
`teste-apelidos` 59 · `teste-voz` · `teste-arvore` · `conferir-entidades` ·
`conferir-slugs` · `conferir-protecao-funcoes` · `php -l` em tudo.

**Baterias antigas rodadas inteiras, para provar que nenhuma virou inerte com o
banco novo:** `mutacoes-dimensao` **14 de 14**, `mutacoes-peixes` **39 de 39**,
`mutacoes-voz` **27 de 27**. Nenhuma inerte — o que importa aqui porque este
bloco reordenou os campos de `afiliado` nos quatro arquivos de produto.

**OS QUATRO GERADORES DE CATÁLOGO FORAM RODADOS E NÃO MOVERAM UM BYTE DOS
SNIPPETS.** Era a medição que decidia se este bloco toca o ar: os catálogos
embutidos leem `afiliado.url` e `afiliado.plataforma`, e nenhum dos dois mudou.
**Nenhuma página servida mudou, nenhuma URL nasceu, nenhum snippet foi
reescrito** — o que subiu foi esquema, banco e bancada.

### O que este bloco NÃO fez, com o nome e o motivo

**A escada não chegou à TELA, e isso é escolha declarada, não esquecimento.** Os
três estados da 25.2 (ficha + busca discreta / busca vira botão / nem uma nem
outra) vivem em **quatro calculadoras × PHP e JavaScript**, com o cartão da
vitrine, a lista técnica, o desempate de ordem e o texto de FAQ em cada uma — da
ordem de quarenta pontos de decisão, cada um com portão de navegador próprio.
Dois motivos para não começar isso na cauda deste bloco:

1. **Renderizaria exatamente o que já está no ar.** Com `url_busca` null nos 78,
   o estado 2 nunca acontece e a linha discreta do estado 1 não tem para onde
   apontar. Seria refatoração grande e **provadamente dormente**.
2. **Meia refatoração em quatro calculadoras que discordam em silêncio é pior do
   que nenhuma.** O Clube do Mosaico levou a escada à tela hoje em duas
   superfícies e achou duas mutações inertes no caminho; aqui são oito.

A diferença para o caso dele importa e está dita: lá **o dado existia e o código
faltava**, e o leitor perdia monetização real. Aqui o dado do piso **não pode ser
completado desta nuvem**, e o código esperaria por ele de qualquer jeito.

### Os dois vivíparos, tentados hoje e recusados — e um deles com mecanismo novo

- **Molly (`poecilia-sphenops`), `comprimento_minimo_aquario_cm`: recusado, e
  agora se sabe POR QUÊ.** Três passadas de busca restrita ao compêndio hoje, com
  três formulações. Nenhuma atribui o número à espécie. E a terceira trouxe o
  achado: **`90 × 30 cm` é medida-padrão que aquele compêndio repete em fichas de
  espécies sem parentesco** (o headstander pintado, o panda garra). Ou seja, o
  `90 × 30 × 30 cm` que a coleta de 13/09 viu numa passada só não era uma
  confirmação fraca — era a **medida-padrão do corpo**, oferecida com cara de
  resposta. É a `regra_da_congenere` numa forma nova: não a ficha da irmã, e sim
  **o número de prateleira da casa**. Quem derruba o número passa a ser o
  mecanismo, não a contagem de passadas.
  **O que uma das passadas trouxe e NÃO entrou:** `21 a 28 °C`, pH `7,5 a 8,5` e
  dureza `10-25 mg/l` atribuídos ao compêndio, que discordam do que o banco tem
  pela base científica. Não entram na cauda de um bloco que não é de coleta:
  seriam conflito declarado em três campos, com tratamento pela V17, e isso é
  bloco.
- **Guppy (`poecilia-reticulata`), o segundo corpo: recusado.** A busca restrita
  ao Catalog of Fishes **não devolveu nada daquele domínio** — os resultados
  vieram de NCBI, bioRxiv e até de patente. Pela `regra_de_atribuicao_por_busca`,
  número sem dono não entra. **E fica dito, para a próxima coleta não gastar a
  passada:** existe um atalho que passaria no portão e que foi **recusado de
  propósito** — juntar um corpo taxonômico só para a contagem de "duas fontes"
  fechar. Ele confirmaria a família e deixaria todos os números de manutenção
  ainda sustentados por um corpo só. É o mesmo movimento que a regra E15 existe
  para impedir, de roupa nova.

**Resultado:** `/peixes/vivaparos/` continua com **2 elegíveis**. O `ARVORE.md`
não muda, porque o que ele já dizia continua verdadeiro.

### Aberto e nomeado

- **(a) O PISO DE 78 ITENS depende de UMA sessão.** `url_busca_produto` está
  escrito nos 78; falta o encurtamento. Não é código e não é decisão: é a sessão
  do painel de afiliado, e no dia em que ela existir são 78 colagens e **nenhuma
  linha de código**.
- **(b) A SAÚDE DOS 39 LINKS NO AR É DESCONHECIDA E VAI CONTINUAR.** A 25.4 manda
  a ronda conferir link publicado; sem `url_produto` ela não consegue, e hoje
  ficou medido que nem o título do anúncio reabre o caminho. A saída é
  **reescolher** os 39, e reescolher exige o feed ou a sessão. É a dívida que a
  própria 25.4-b registrou com o nome desta ilha.
- **(c) A escada não está na tela** — item nomeado acima, com os dois motivos.
- **(d)** A ilha **não tem página de privacidade**, com GA4 no ar e link de
  afiliado publicado. Continua sendo dívida de verdade.
- **(e)** `atualizar-manifest.py` avisa "fora do manifest" e segue; **os três
  portões novos deste bloco ENTRARAM**, então a dívida não cresceu com ele.
- **(f)** A dimensão de 24 imagens do banco segue nula com motivo declarado; só o
  Chrome da Sentinela alcança aquele CDN.
- **(g)** GT-PL9DD7KW e o Tempo Real do GA4 (falta `GOOGLE_SA_B64`) seguem como
  estavam.

**RECEITA:** 39 dos 78 produtos com ficha de loja, **0 com piso**, 78 sem piso.
Dos 39 sem ficha, 9 não têm loja possível hoje (7 sem anúncio, 1 cujo único
anúncio é outro produto, 1 cujo único anúncio é outra variante). **Pauta da seção
17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

**PRÓXIMO, com ordem e motivo:**
1. **LEVA 4 = `/peixes/bettas/`** com as três fichas (betta, colisa-anão, gurami
   mel). **Destravada a partir de 14/09**, quando a semana vira. Não falta nada
   antes de escrever, e as quatro páginas nascem declarando `serp_em` =>
   `13/09/2026`.
2. **A ESCADA NA TELA**, quando houver `url_busca` para ela servir — ou antes, se
   o dono preferir o código pronto esperando o dado. É bloco inteiro, nas quatro
   calculadoras de uma vez, e o portão tem de medir a **classe emitida**, nunca a
   frase legível.
3. **Vivíparos**, quando o egresso abrir ou aparecer um terceiro corpo: é a
   categoria mais barata do banco e vai de 2 para 4 com dois campos.

## 2026-09-13 15h16Z — O DESPACHO DA SENTINELA DE 13/09 SAI INTEIRO: as datas do schema passam a sair de onde já são verdade, e a ficha de peixe para de abrir pela prova (casca 1.8.0, artigos 1.3.0, peixes 1.4.0, os quatro catálogos regerados, manifest revisão 66, `/status` conferido às 15h50Z em UM disparo)

**Nenhuma URL nova. Nada na fila de construção foi tocado:** a 18.5 manda fechar
despacho antes de começar bloco, a 18.2 manda o despacho sair INTEIRO, e ele
tinha quatro itens. Os quatro estão cumpridos e **verificados no ar**, que é o que
a 18.4 exige para um item morrer. Os itens 1 e 2 eram o mesmo defeito visto de dois
lados; o 3 era falta de DADO, não de código; o 4 era voz. Nenhum deles é opinião:
os quatro eram medições da ronda.

### 1 e 2. A DATA SAI DE `post_modified_gmt`, E NÃO DE UM LITERAL

O snippet dos artigos declarava `'dateModified' => '2026-09-10'`, escrito à mão, e
o `wp-sitemap-posts-post-1.xml` declarava `2026-09-13T13:38:10+00:00` para as
MESMAS três URLs. **Duas datas da mesma página**, e a do schema envelhecia sozinha
a cada Sync — trocar o literal por um literal novo só reagendaria o defeito para a
semana seguinte.

**Onde o conserto mora, e por que não em cada snippet:** nasceu
`aquametria_casca_data_da_pagina()`, na casca 1.8.0. A data de modificação não é
propriedade do artigo nem da ficha de peixe: é propriedade da **página**, e a
casca é a única camada que toda página tem. Dois snippets com a mesma função
copiada divergiriam no dia em que um fosse corrigido — a forma de defeito que este
contrato paga mais caro. Os dois chamadores guardam `function_exists()`, porque o
Sync aplica um arquivo por vez e o snippet pode chegar minutos antes da casca.

A função lê `post_modified_gmt` (ou `post_date_gmt`) do post servido e formata em
W3C no fuso UTC — **a mesma leitura que o sitemap do núcleo faz**. As duas datas
não podem discordar, e não porque alguém as comparou: são a mesma leitura.

**AS DUAS GUARDAS DA FUNÇÃO SÃO CARREGADAS, e isso foi medido e não suposto.**
`strtotime(' UTC')` devolve **AGORA** e `strtotime('0000-00-00 00:00:00 UTC')`
devolve o **ano zero**. Sem a guarda de vazio, uma página que o WordPress diz não
saber quando mudou passaria a jurar que mudou hoje — data inventada em nó de
schema, que é a mentira que a seção 10 proíbe. Data ausente devolve `''` e quem
chama **omite o campo**: não existe data de reserva.

**A ASSIMETRIA DOS ARTIGOS FICOU, E AGORA ESTÁ DECLARADA NO PORTÃO.** O
`datePublished` dos três continua sendo a data editorial do registro
(`2026-09-08`, que o próprio endereço carrega) e **não** a do post. Consertar isso
"por simetria" moveria a data de publicação de três URLs indexadas, então o portão
reprova quem tentar, nomeando o motivo.

O item 2 é o mesmo conserto na página que mais dependia dele: o `Article` das onze
fichas trazia `headline`, `about`, `inLanguage`, `isAccessibleForFree` e
`mainEntityOfPage`, **e nada mais** — enquanto o `Article` dos três artigos já
declarava os quatro campos. Agora as onze declaram `datePublished`,
`dateModified`, `author` e `publisher`, com a **mesma** editora, e o
`datePublished` vem de `post_date_gmt` porque nenhuma das onze declara data de
publicação em lugar nenhum do repositório: o post é a única coisa que sabe.
Escrever a data da leva à mão seria a constante do item 1 renascendo na página
vizinha.

**O QUE SOBROU DISSO, e não é dívida: é uma coisa que ninguém tinha percebido.**
Para as onze fichas, `post_modified` só se move quando o **conteúdo da página**
muda — e o corpo delas é um shortcode. Este bloco reescreveu a abertura das onze,
a tela mudou, e as onze continuam declarando `2026-09-13T02:37:08+00:00`, que é
quando a casca criou as páginas. **O critério do item 1 está cumprido** — schema e
sitemap declaram a mesma coisa, url por url, e foi isso que a Sentinela pediu —,
mas quem decidir um dia fazer o Sync tocar as páginas cujo snippet mudou decide
junto o que dizer ao Google. É bloco, não conserto, e está nomeado no `ESTADO.md`.

Para os três artigos o critério foi medido nas duas metades: o sitemap dizia
`13:38:10` no começo desta execução, e depois do Sync **as duas** dizem
`15:50:1x`. **Um Sync novo moveu as duas juntas**, que era a segunda metade do
"pronto quando".

### 3. AS OITO FOTOS GANHAM `width` E `height` — e o que faltava era DADO

O renderizador já estava certo: ele só emite o par quando o registro tem os dois
campos. Os oito registros não tinham. A Sentinela mediu as oito no Chrome
(`naturalWidth` × `naturalHeight`) e deixou os números no despacho; a nuvem **não
alcança** `down-bs-br.img.susercontent.com` (`connect_rejected` por política,
reconferido por `curl` em duas passadas hoje, com a ilha em 200 na mesma passada),
então a medida vem de quem tem navegador. Os oito entraram no banco com
`verificado_em: 2026-09-13` — a ronda abriu a URL e viu a imagem carregar, que é
exatamente o que aquele campo significa — e os quatro catálogos embutidos foram
regerados.

**UMA CORREÇÃO DE PREMISSA, e ela diminui o tamanho do defeito sem diminuir o
conserto:** o despacho dizia que as oito "reservam zero espaço no layout". Não
reservavam **pelo atributo**, mas a caixa da foto é reservada pelo CSS
(`aspect-ratio:1/1;width:100%`), então não havia salto de layout. O defeito da
22.7 é real e foi consertado; o custo dele era menor do que o escrito. Este portão
passou a **medir a regra de CSS no que é servido**, para essa afirmação não
envelhecer calada.

**A DECISÃO QUE O DESPACHO MANDOU TOMAR — o que acontece quando o campo falta.** A
foto **continua** sendo servida, sem o par. Deixar de servi-la seria perder a
recomendação técnica certa por falta de uma medida, com a caixa já reservada do
mesmo jeito. O que fica proibido é o **silêncio**: registro com imagem sem
dimensão declara `motivo_sem_medida`, e registro com dimensão declara `medida_em` e
`medida_como` — campos novos no esquema. **Número sem data de leitura é chute com
cara de dado**, e `800x800` digitado porque foto de e-commerce costuma ser
quadrada passaria por qualquer regra que olhasse só o valor.

**UM BURACO ANTIGO FECHADO DE PASSAGEM:** a V19 do validador olhava só a
`largura`. Um registro com largura e sem altura passava, e o cartão serviria
`width` sozinho — que dá ao navegador uma **proporção errada** em vez de nenhuma, e
é pior que omitir as duas. Agora é o par inteiro ou nenhum.

### 4. A FICHA DE PEIXE PARA DE ABRIR PELA CAMADA DE PROVA

As onze começavam por *"Para os N \<peixe\> que **a fonte declara** como cardume
mínimo ... e **a fonte declara** a BASE, não o litro"* — duas menções à fonte na
primeira frase, contra a 15.2 e contra a régua que o bloco de 11/09 fixou,
"procedência não abre página". A prova não foi apagada: ela já estava duas telas
abaixo, na tabela "O que as fontes declaram", com o corpo e a data de cada linha.

Agora: *"Para um cardume mínimo de 5 tetra neon, o seu aquário precisa de 60 cm de
frente por 30 cm de fundo. O que manda é a BASE do aquário, não o litro."*

**A DISTINÇÃO QUE A REESCRITA TINHA DE PRESERVAR era a decisão 7 do snippet, e ela
custou uma leva inteira:** 14 dos 36 registros declaram COMPRIMENTO e não BASE.
Enquanto a abertura citava a fonte, era a palavra "fonte" que carregava a
diferença. Agora ela viaja na **estrutura** da frase, em dois lugares ao mesmo
tempo: o trecho "por Y cm de fundo" só existe quando há fundo declarado, e a
palavra final é BASE ou COMPRIMENTO. Quem tem só o comprimento diz que o fundo
**fica em aberto** — o que um aquarista diria, e não um buraco escondido. E porque
a diferença deixou de morar numa palavra, ela ganhou régua: **exatamente um** dos
dois formatos, cobrado nas onze.

**A RÉGUA QUE O DESPACHO PEDIU REPROVAVA TRÊS PÁGINAS CERTAS, e isto é medição.**
Ele nomeava quatro termos — "a fonte declara", "declarado por", "conforme" e
"segundo" — para reprovar no `<title>`, no `h1` e no primeiro parágrafo. Escritos
como estão e medidos nas 27 páginas, "conforme" e "segundo" reprovaram **três
primeiros parágrafos corretos**: *"iluminação baixa pode querer dizer 1.000 lúmens
ou 2.000, **conforme** a régua que você abrir"*, *"vai de 125 mililitros a 1,25
litro, **conforme** a marca que você abrir"*. Ali "conforme" é **dependendo de**, e
é justamente a frase que publica a divergência entre fontes — a tese da ilha. Uma
lista literal teria silenciado a tese para proibir a atribuição.

A saída não é heurística de vizinhança: a seção 8 já pagou por isso duas vezes, e
na segunda a heurística **aprovou** a frase errada. A saída é que **atribuição
precisa de um atribuído**: "conforme" e "segundo" só contam quando o que vem depois
**nomeia** alguém — uma marca da lista de fontes da ilha, ou "a fonte", "o
fabricante", "o compêndio", "o manual". `marca` e `régua` de propósito **não** são
atribuídos: "conforme a marca que você abrir" fala de uma marca qualquer, não
daquela marca. E a régua mede a si mesma em duas frases produzidas, para quem um
dia achar mais simples pôr "conforme" de volta na lista literal reprovar **ali**,
antes de reprovar dez páginas.

O `teste-voz.mjs` já media as onze fichas, ao contrário do que o despacho supunha
("hoje ele mede 13 páginas e nenhuma delas é ficha de peixe" era verdade em 11/09;
as levas 1 a 3 as acrescentaram em 12/09). O que faltava era a régua, não o
alcance: 27 páginas, 752 afirmações.

### VERIFICAÇÃO

**Portões novos:** `ferramentas/teste-datas-schema.py` (78 afirmações) e
`ferramentas/mutacoes-datas.py` (**12 de 12** reprovadas);
`ferramentas/teste-dimensao-imagem.py` (36) e `ferramentas/mutacoes-dimensao.py`
(**14 de 14**, cada uma pelo portão que ela **nomeia** — defeito de dado pego por
sorte pelo portão do HTML não prova que a regra do banco existe).

**OS DOIS PORTÕES PRODUZEM MUNDO, e um deles só ficou honesto na segunda
tentativa.** A primeira rodada de mutações das datas teve **uma que PASSOU**: "sem
data, a casca devolve a data de HOJE". O ramo existia, e as duas guardas de cima
interceptavam os dois mundos que o portão produzia — o ramo **nunca rodava**. Ramo
defensivo não medido é ramo que pode mentir à vontade, então nasceu o terceiro
mundo, o campo com texto que não se lê como data: o esquema permite (o campo é uma
string), o WordPress nunca grava, e a régua trata hoje.

**Bancada, 0 falha:** `teste-peixes.py` **1222**, `teste-voz.mjs` **752** (era
749), `teste-dimensao-imagem.py` 36, `teste-datas-schema.py` 78,
`teste-seo-tecnico.php` 330, `teste-ga4.py` 440, `teste-apelidos.php` 59,
`validar-especies.py` 36 registros com o mesmo aviso E15 do guppy,
`testar-validador-especies.py` 22, `validar-produtos.py` 78 produtos 0 erro,
`teste-arvore.mjs`, `conferir-entidades.mjs`, `conferir-slugs.py`,
`conferir-protecao-funcoes.py`, conversor 17, escape, atualizador 9, `php -l` em
tudo. **Navegador:** `teste-navegador-arvore.mjs` com **498 medições** em 27
páginas × 6 larguras, 0 px de rolagem, console limpo. **Mutações antigas rodadas
inteiras:** peixes **39 de 39** e voz **27 de 27** (era 20) — e uma das antigas
tinha virado **INERTE** com a reescrita da abertura; o próprio mutador avisou,
porque ele conta as ocorrências em vez de substituir em silêncio, e o alvo foi
reapontado.

**NO AR às 15h50Z, em UM disparo.** `/status` na **revisão 66**, igual à do
`manifest.json`, 19 aplicados. E a conferência que **só o ar pode fazer**, porque
o critério de pronto compara com o sitemap: `conferir-datas-e-voz-no-ar.py`, **170
afirmações, 0 falha** às 16h11Z — as 14 URLs com `dateModified` do schema **igual**
ao `lastmod` do sitemap, as 11 fichas com os quatro campos e a editora igual à dos
artigos, as 8 fotos com o par do banco, e as 33 superfícies de abertura das onze
sem atribuição.

**REDE (20.2):** a ilha em 200 na home e no `/status`.
`down-bs-br.img.susercontent.com` em `connect_rejected` por política, duas
passadas, com a ilha em 200 na mesma passada — é o que manda a medida da imagem
vir do Chrome da Sentinela.

**RECEITA (item 5 do despacho, que fica aberto por desenho):** **39 dos 78**
produtos esperam link de afiliado, e destes **9 não têm loja possível hoje** — 7
sem anúncio na plataforma, 1 cujo único anúncio é outro produto
(`aquarios-do-rio-led-60cm`) e 1 cujo único anúncio é outra variante
(`ista-il-401-60`). Os outros **30** têm anúncio e esperam a geração manual do
link curto no painel, que é a metade do Raphael. Este bloco não tocou catálogo de
produto. **Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na
fila, 0 recusados.

**O ACHADO QUE NÃO ERA DESTA ILHA foi para o canal certo:** a ronda escreveu no
`PROMPT.md` daqui, "porque não há outro canal", que o `PROMPT.md` da
clubedomosaico não documenta o parâmetro de autenticação do endpoint de peças da
24.2. A seção 3 proíbe editar arquivo de ilha que não se reservou, então ele foi
copiado para `dados/despachos.md` na raiz, endereçado a quem reservar aquela ilha.

**PRÓXIMO, com ordem e motivo:** (1) **LEVA 4** = `/peixes/bettas/` com as três
fichas (betta, colisa-anão, gurami mel), que **já pode nascer na semana que começa
em 14/09**, quando o teto da 21.4 virar — nada falta antes de escrever, e as
quatro páginas nascem declarando `'serp_em' => '13/09/2026'`; (2) **BANCO**:
`/peixes/vivaparos/` está a DOIS campos de ter 4 fichas (guppy e molly) e a UM de
ter 3, e os dois dependem de leitura direta da ficha ou de um terceiro corpo; (3)
a leitura de 16/09 continua tendo o que responder sobre a leva de 08/09 e continua
**não** travando leva nenhuma — 27 URLs, abaixo do piso de 40 da seção 21.

## 2026-09-13 13h17Z — A DATA DA SERP VIRA CAMPO E A BETTAS GANHA CRITERIO: a leva 4 fica pronta para nascer (snippet aquametria-peixes 1.3.0, manifest revisao 65, /status conferido as 13h38Z em UM disparo)

**Nenhuma URL nova, e isso e regra e nao escolha:** o teto da 21.4 e de tres levas
de URL por semana e a semana ja gastou as tres (levas 1, 2 e 3, todas em 12/09).
O que o `ESTADO.md` anterior nomeava como "o que falta antes de escrever uma
linha" da leva 4 eram duas coisas — a classificacao de SERP da 14.9 e o criterio
da categoria — e este bloco entrega as duas, mais a consequencia de codigo que a
primeira delas criou.

### 1. A CLASSIFICACAO DE SERP DAS QUATRO CONSULTAS: as quatro sao ALVO

A leitura inteira, com quem ocupa cada top e que numero cada um publica, esta em
`dados/indexacao.md`. Aqui fica o que ela tem de diferente das tres anteriores.

**A medicao que vale mais nao e sobre uma consulta: e sobre duas.** O
*Trichogaster lalius* — a colisa-anao, UMA especie — aparece com **56 L** numa
consulta e com **70 L** na outra, no mesmo dia, alem do **40** e do **36** que ja
discordavam entre si. Quatro numeros para o mesmo peixe, nenhum atribuido a fonte
nomeada, dois deles na primeira pagina. E a tese desta ilha medida **por fora**
dela: nas levas 1 a 3 a discordancia foi medida entre paginas diferentes sobre
especies diferentes; aqui ela e a mesma especie se contradizendo em duas buscas.

**O que a ilha tem A MAIS nesta categoria, e e o que justifica a categoria
existir em vez de tres fichas soltas:** o arranjo social. Sob o mesmo rotulo
estao um peixe que vive SOZINHO (betta), um que vive EM CASAL (colisa-anao) e um
que vive EM GRUPO COM HIERARQUIA (gurami mel, cardume de 4 a 6), e nenhuma das
quatro SERPs distingue isso. Quem responde "quantos litros para gourami" com um
numero so esta respondendo a pergunta errada.

**O limite do metodo fica declarado, nao escondido:** a classificacao sai da
ferramenta de busca desta nuvem, que nao e o Google brasileiro visto de um IP
brasileiro. Ela mede QUEM publica e QUE numero publica — que e o que a 14.9 pede
para decidir — e nao a ordem exata do top 10 no Brasil. E o mesmo metodo das
levas 1 a 3; a diferenca e que agora esta escrito.

### 2. A CONSEQUENCIA QUE O PROPRIO CODIGO TINHA PREVISTO, e o dia chegou

O comentario da constante `AQUAMETRIA_PEIXES_SERP_EM`, escrito na leva 2, dizia:
*"se uma leva futura sair em outro dia, esta constante deixa de servir para todas
e vira campo do registro"*. **O dia chegou antes da leva** — estas quatro
consultas foram classificadas em 13/09 e as doze paginas no ar continuam em
12/09.

Nasceu o campo `serp_em` no registro e a funcao `aquametria_peixes_serp_em()`. A
constante **continua existindo, e nao por compatibilidade**: doze paginas
declarando a mesma data doze vezes seria a mesma data escrita doze vezes, que e
exatamente o defeito que a constante nasceu para impedir. Ela e o PADRAO; quem
tem data propria declara. **Nenhuma pagina imprime a constante direto** — se
imprimisse, a pagina com data propria continuaria servindo a data das outras e o
defeito seria invisivel justamente na pagina que ele afeta.

### 3. A REGUA DA DATA ERA UMA DATA DIGITADA, E TERIA REPROVADO UMA PAGINA CERTA

O portao afirmava a presenca do texto "12/09/2026" no corpo. **A afirmacao
dependia de TODAS as paginas terem a mesma data**, que e um caso do banco de hoje
e nao uma propriedade do codigo — e no dia da leva 4 ela reprovaria quatro
paginas corretas por servirem a data certa. E a mesma familia da regua que morreu
quando o banco melhorou na clubedomosaico em 12/09, numa forma mais discreta:
la a regua dependia de o banco NAO ter link nenhum; aqui dependia de o eixo ter
uma data so.

O teste agora recomputa a data esperada pela propria regra — le o `serp_em` do
registro **em texto** e cai no padrao quando nao ha — e **nao chama**
`aquametria_peixes_serp_em()`. Se chamasse, um erro na funcao faria as duas
metades errarem juntas e o portao ficaria verde, que e a decisao 1 do cabecalho
daquele arquivo.

### 4. O CAMINHO NOVO SO E MENSURAVEL NUM MUNDO PRODUZIDO

Nenhuma das doze paginas declara `serp_em`: as doze herdam o padrao. Uma
afirmacao sobre o caminho da data propria, medida no banco de hoje, mediria o
caminho do PADRAO e ficaria verde com a funcao quebrada — e o dia em que ela
importasse seria o da leva 4. Entao o portao **produz o mundo**: copia a ilha,
injeta o campo numa ficha e mede tres coisas, que sao uma ideia partida em tres
porque cada uma pega um defeito diferente:

- **(a)** a pagina com data propria serve a data DELA — pega a funcao que ignora
  o campo;
- **(b)** essa mesma pagina NAO serve mais o padrao — pega a funcao que imprime
  os dois, que passaria em (a) sem consertar nada;
- **(c)** a VIZINHA, que nao declara nada, continua no padrao — pega a funcao que
  devolve a data declarada para todo mundo, **o erro mais provavel de quem
  escreve isto com pressa e o unico que (a) e (b) aprovariam juntas**.

As tres mutacoes correspondentes reprovam, cada uma na sua afirmacao.

### 5. O CRITERIO DA `bettas`, escrito com a lista de especies ainda VAZIA

E a primeira categoria deste eixo em que **o posto taxonomico SERVE de criterio**.
Nos tetras a familia nao servia (a revisao dos caracideos deixou tetra em duas
familias, e Characidae carrega peixe que ninguem vende como tetra); nas coridoras
o genero nao servia (a revisao da subfamilia tirou as quatro do genero Corydoras
na propria fonte). Aqui as cinco especies do banco sao Osphronemidae e as cinco
sao vendidas como betta, colisa ou gurami: a familia nao traz uma sexta de brinde
nem deixa nenhuma de fora. **E o criterio diz tambem o que a familia NAO decide**
— o arranjo social —, porque e ele que muda a resposta.

**A regra nova do portao cobra o criterio de quem TEM especie, e nao de quem esta
registrada como pagina.** A diferenca e a que importa: cobrar so das registradas
deixaria a leva seguinte encher a lista e publicar a categoria com o campo vazio,
e o defeito entraria no ar **uma leva depois de ser cometido**. A primeira versao
da regua cobrava so das registradas e ainda mediu o pedaco errado do arquivo (o
registro das paginas usa a MESMA forma `'slug' => array(` e vem antes), reprovando
duas categorias que declaram o criterio ha tres blocos — regua que le o pedaco
errado do arquivo reprova codigo certo.

### COLETA DE BANCO: tres alvos, tres RECUSAS, nenhum campo gravado

Os tres alvos mais baratos que o estado anterior nomeava. **Nenhum entrou, e os
tres motivos sao diferentes:**

1. **Molly (`comprimento_minimo_aquario_cm`), o mais caro de perder** — ele
   sozinho levaria a `/peixes/vivaparos/` de 2 para 3, que e o minimo exato do
   16.5. O compendio devolveu **90 × 30 × 30 cm** em UMA passada e em nenhuma das
   outras tres que nao carregavam o numero na consulta. **Reproduzir uma vez nao
   e confirmar**, e a regua e a mesma que sustentou o porte do gurami mel ontem:
   o numero volta IGUAL em duas passadas independentes. Aqui nao voltou. Isto
   **nao** e uma contradicao da fonte — e ausencia de confirmacao, e o campo fica
   nulo ate a leitura direta da ficha.
2. **Cascudo (`temperatura_C`)** — segunda tentativa, mesma parede de 09/09: nem
   o compendio nem a base cientifica declaram faixa termica para esta especie.
3. **Guppy (segunda fonte)** — terceira tentativa, mesma parede. A saida dele
   continua sendo a que o proprio registro ja dizia: leitura direta da ficha
   quando o egresso abrir, ou um terceiro corpo.

**NAS TRES A BUSCA OFERECEU SOZINHA O NUMERO DA CONGENERE**, e nas tres foi
recusado: 60 cm de *P. velifera* e de *P. reticulata* para o molly; pH 6,0–6,5 e
75–80 °F de "especies aparentadas do genero" para o cascudo; temperatura de
*P. latipinna* para o molly. A busca inclusive DIZ que o numero e da vizinha — a
tentacao vem rotulada, como veio no gurami perola em 12/09.

**O que a coleta CONFIRMOU, e e o unico ganho dela:** a base de **60 × 30 cm** do
cascudo voltou igual a que o banco guarda desde 09/09, por uma passada que nao a
carregava na consulta. Reconferencia independente de campo antigo, nao campo
novo.

**REDE (20.2):** a ilha em **200** na home e no `/status`. `fishbase.se` e
`seriouslyfish.com` em `connect_rejected` por POLITICA de egresso, reconferido
hoje com `curl` — e por isso esta coleta, como todo o banco desta ilha, sai por
busca restrita ao dominio, com "a confirmar na ficha" escrito em cada fonte.

### VERIFICACAO, 0 falha

**Bancada:** `teste-peixes` **1222** afirmacoes (era 1206); `mutacoes-peixes`
**39 de 39 reprovadas** (era 35 de 35 — as 35 antigas rodadas inteiras, nenhuma
virou inerte); `validar-especies` 36 registros, 0 erro e o mesmo aviso E15 do
guppy; `testar-validador` 22; `teste-arvore`; `teste-voz`; `teste-seo-tecnico`
330; `teste-ga4` 440; `teste-apelidos` 59; `conferir-entidades`;
`conferir-slugs`; `conferir-protecao-funcoes` (39 funcoes, todas dentro de
`function_exists`); `php -l` limpo nos snippets.

**Navegador:** `teste-navegador-arvore` **498 medicoes** em 27 paginas x 6
larguras, 0 px de rolagem, console limpo.

**A PROVA QUE VALE MAIS QUE TODAS, e ela e desta familia de mudanca:** as
QUATORZE paginas do eixo servem **HTML byte a byte identico** ao do HEAD
anterior, medido pagina a pagina contra uma copia do commit de antes. Refatoracao
que promete nao mudar a tela tem como PROVAR isso, e o `cmp` e a prova.

**No ar as 13h38Z, em UM disparo:** `/status` na revisao **65** igual a do
manifest, 19 aplicados. `conferir-peixes-no-ar.py` **356** afirmacoes, 0 falha.
E as duas medicoes que so este bloco tinha para fazer, no HTML SERVIDO: (1) as
paginas do eixo continuam servindo **12/09/2026** e **nenhuma** serve 13/09/2026
— o caminho do padrao funciona em producao, e nao so na bancada; (2)
`/peixes/` serve a categoria **"Bettas e gouramis" com "Em breve", sem `<a>`**, e
a palavra "Osphronemidae" **nao aparece** na tela: o criterio e preparo, nao
publicacao.

### PROXIMO, com ordem e motivo

1. **LEVA 4 = `/peixes/bettas/` com as tres fichas**, e ela ja pode nascer **na
   semana que comeca em 14/09**, quando o teto da 21.4 virar. **Nao falta mais
   nada antes de escrever**: a SERP esta classificada e o criterio esta escrito.
   As quatro paginas nascem declarando `'serp_em' => '13/09/2026'` — quem nao
   declarar herda 12/09/2026, que seria mentira nestas quatro. A ficha da
   colisa-anao tem um paragrafo obrigatorio: os quatro numeros que a SERP publica
   para ela.
2. **BANCO, a categoria mais barata:** `/peixes/vivaparos/` esta a DOIS campos de
   ter 4 fichas (guppy e molly), e a UM de ter 3. Os dois dependem de leitura
   direta da ficha ou de um terceiro corpo — busca restrita ja foi tentada tres
   vezes no guppy e quatro no molly. **Isto e o que mais destrava malha por
   campo colhido em toda a ilha.**
3. A leitura de 16/09 continua tendo o que responder sobre a leva de 08/09 e
   continua **nao travando leva nenhuma**: 27 URLs, abaixo do piso de 40 da
   secao 21.

**ABERTO E NOMEADO, o mesmo de antes e nada novo:** (a) para onde `GT-PL9DD7KW`
roteia, humano; (b) o Tempo Real do GA4, que este ambiente nao le por falta de
`GOOGLE_SA_B64`; (c) a ilha **NAO TEM PAGINA DE PRIVACIDADE**, e com a tag do GA4
no ar e link de afiliado publicado isso e divida de verdade; (d) o
`atualizar-manifest.py` avisa "fora do manifest" e SEGUE, e sobram 22 arquivos
fora. **RECEITA (item 4 do despacho da Sentinela de 10/09):** este bloco nao
tocou catalogo de produto — seguem **39 dos 78** produtos esperando link de
afiliado. **Pauta da secao 17:** `pauta.md` ainda nao existe — 0 escritos, 0 na
fila, 0 recusados.


## 2026-09-12 20h15Z — T4, LEVA 1: A MALHA DO EIXO /peixes/ NASCE (casca 1.7.2, snippet aquametria-peixes 1.0.0, manifest revisao 59)

Cinco URLs novas, e a ilha vai de 13 para 18. Nivel 1 `/peixes/`, nivel 2
`/peixes/tetras/` e tres fichas de especie — tetra neon, neon cardinal e
mato-grosso —, na ordem do 16.6: a mae e as tres primeiras filhas de maior
intencao, nunca uma filha de cada categoria espalhada.

**Sao as primeiras paginas desta ilha que nascem com MAE.** A URL passa a mostrar
os tres niveis da 16.1 e o `BreadcrumbList` passa a ter quatro degraus, todos com
endereco. Ate hoje o degrau de nivel 2 desta ilha nunca tinha sido link — e
afirmacao sobre o caso que nao existe nao mede nada, o que ficou provado da pior
maneira (ver os dois defeitos abaixo).

**Por que este cluster e nao o de aquecimento**, que e o item 1 da ordem do
`ARVORE.md`: a secao 21 suspendeu a trava de pagina nova, mas **nao** a de mover
URL publicada. `/calculadoras/aquecimento-e-luz/` exigiria pendurar C5 e C15 sob
uma categoria nova — duas URLs movidas — alem de a C7 nao existir, e a 16.5 pedir
3 filhas. `/peixes/tetras/` e o unico cluster do mapa que nasce inteiro sem mover
endereco nenhum.

### A tese da camada, e ela e o que a proxima leva copia

**AS FONTES DECLARAM A BASE DO AQUARIO, NAO O LITRO.** As sete primeiras
respostas da SERP brasileira, medidas em 12/09 **antes** de a pagina ser escrita,
dao litro sem fonte e discordam entre si: 40 L para 8 a 10 neons contra 20 L para
6 a 8; cardume de 3 contra cardume de 6 no mato-grosso; porte de 3 cm contra 5 cm
na mesma pagina de resultados. Cada ficha serve a base declarada — com o nome do
corpo de fonte e a data — ao lado das duas reguas brasileiras de lotacao, que
discordam em **quatro vezes**, com a atribuicao de cada extremo. Nenhuma das sete
publica as duas coisas juntas, e e nisso que a pagina ganha.

### Duas recusas que ficam valendo para toda ficha de especie

1. **O DERIVADO PER CAPITA NAO SE MULTIPLICA.** O esquema do banco declara
   `frente_por_individuo_cm` (frente minima / cardume minimo) e ele sai na tela
   como leitura, **nunca** extrapolado: para o neon daria 120 cm para dez peixes,
   o que contradiz todas as fontes e seria regra de bolso nossa com cara de dado.
   Quem responde "e para dez?" sao os criterios de lotacao, que existem para
   isso. A pagina diz isso por escrito e o portao cobra a frase — e cobra tambem
   que a tabela de lotacao **nao tenha coluna de frente**, porque e assim que a
   multiplicacao voltaria sem ninguem perceber.
2. **ESPECIE QUE O BANCO DECLARA AGRESSIVA NAO GANHA LISTA DE COMPANHEIRO.** Na
   primeira versao o mato-grosso — que a FishBase declara agressivo — servia
   tetra ember e tetra neon na tabela de quem divide a agua, com uma nota dizendo
   que aquilo nao era veredito de convivencia. **Nota nao desfaz tabela:** quem
   le ve a lista, nao a ressalva. E a saida honesta nao era uma lista menor, era
   nao publicar lista — o esquema recusa compatibilidade como campo justamente
   porque ela depende de volume, layout e ordem de introducao, e para peixe
   agressivo e ai que a resposta mora. Agora a ficha conta quantas especies
   dividem a faixa (18 das 27) e diz por que nao recomenda nenhuma.

### Os dois defeitos que a bancada nao podia ver — e e por isso que a conferencia no ar existe

Os dois foram achados **depois do desembarque**, por `conferir-peixes-no-ar.py`,
com a bancada verde nas duas vezes.

- **(a) O degrau do meio nao resolvia.** `aquametria_casca_url_se_existir()` pedia
  a pagina pelo **slug solto**, e `get_page_by_path()` casa o **caminho inteiro**
  em tipo hierarquico — entao `tetras` nunca achava `/peixes/tetras/`. A bancada
  dava quatro degraus linkados; o site servia tres, com o do meio em texto e o
  `BreadcrumbList` com um item a menos. A causa de as duas metades discordarem e
  a licao: no ar a primeira via (`_aquametria_id`) so responde por pagina que veio
  do **Sync**, e as cinco do eixo sao criadas pela **casca** — e a bancada
  respondia essa via para qualquer slug do mapa. Casca 1.7.1, e
  `render-para-teste.php` passou a imitar as tres vias do site, **inclusive as que
  falham**: `get_page_by_path` casa caminho inteiro, `get_permalink` devolve URL
  aninhada, e a via da meta so responde para quem tem arquivo em `conteudo/`.
- **(b) Tres fichas duplicadas, publicadas e no sitemap.** Na primeira remontagem
  depois da leva, a busca da pagina existente usava mae + slug concatenados
  (`tetras/quantos-litros-para-tetra-neon`) para uma pagina que mora em
  `peixes/tetras/quantos-litros-para-tetra-neon`. A busca falhava e
  `wp_insert_post` **criava de novo**, com `-2` no fim. Tres paginas finas e
  duplicadas entraram no sitemap de um dominio recem-nascido — o que gasta o
  recurso escasso da secao 14.1 — e **nao houve uma linha de erro**: o log do Sync
  disse "19 aplicado(s)". Casca 1.7.2: a busca passa a usar o caminho do mapa (o
  mesmo helper da 1.7.1: um lugar so sabe montar caminho) e nasce
  `recolher_duplicatas()`, que manda para a **lixeira** toda `page` marcada
  `_aquametria_casca` que o mapa nao reconhece. Tres limites, e sao eles que
  tornam isso seguro: so pagina que a casca criou e marcou; lixeira e nunca
  exclusao; e nada e recolhido se o mapa vier vazio ou pela metade, porque
  limpeza automatica sobre mapa quebrado nao se conserta depois. As tres
  duplicatas foram recolhidas e devolvem 404.

### Verificacao

- **`ferramentas/teste-peixes.py` (novo): 295 afirmacoes, 0 falha**, um processo
  `php` por pagina, com toda a aritmetica recomputada do
  `dados/especies-agua-doce.json` e o mapa pagina->especie **escrito no teste** —
  ler o mapa do snippet seria perguntar ao snippet qual e a resposta certa, e a
  proxima leva vai copiar este registro.
  **A licao dele, e ela e nova nesta fabrica: COMPARE CELULA, NAO PAGINA.** Duas
  mutacoes deliberadas **passaram** enquanto o portao procurava o numero no texto
  da pagina, porque o numero errado que elas produziam existia em **outra
  tabela**: trocar `floor` por `ceil` devolvia 29 onde cabem 28, e o teste achou o
  "28" dentro de "20 a 28 C". E o mesmo defeito de contar `&#038;` na pagina
  inteira em vez de dentro do `<script>`.
  **E o localizador do corpo era `<body>`**, que casa na bancada e devolve vazio
  no ar, onde o WordPress serve `<body class="wp-singular page-child ...">` —
  corpo vazio faz toda afirmacao sobre texto reprovar de uma vez.
- **`ferramentas/mutacoes-peixes.py` (novo): 24 deliberadas, 24 reprovadas**, em
  tres familias — o numero muda; o numero fica e a ESTRUTURA quebra (a especie
  agressiva ganha lista, o per capita volta a ser multiplicado, categoria vazia
  registrada como pagina, `Product` no JSON-LD); e a regua perde o chao (o
  catalogo do snippet envelhece em relacao ao banco, a colisao de slug volta).
- **`ferramentas/teste-voz.mjs` foi de 13 para 18 paginas** (293 para 422
  afirmacoes) e **tres aberturas reprovaram de uma vez**: nenhuma das tres falava
  na segunda pessoa, e a da categoria abria com "o banco desta ilha", que e
  vocabulario de dentro da fabrica. Nenhum olho tinha visto; a regua viu.
- **Colisao de slug consertada antes de existir:** `aquametria_casca_categorias()`
  chamava de `peixes` a categoria de calculadora do C8, o mesmo slug da secao de
  nivel 1 desta leva. Como `url_se_existir()` acha a pagina pelo `post_name`, com
  as duas no ar o hub linkaria uma ao acaso. A pagina do C8 nao existe, entao a
  troca para `lotacao` nao moveu URL nenhuma — e `teste-peixes.py` tem a
  afirmacao que impede a colisao de voltar.
- **Regressao sem uma falha:** `teste-arvore` (com o `ARVORE.md` atualizado),
  `teste-seo-tecnico` (177), `teste-ga4` (291), `mutacoes-ga4` 13/13,
  `mutacoes-voz` 20/20, `mutacoes-arvore` 14/14, `mutacoes-c15-regulagem` 13/13, `mutacoes-c12-vitrine` 11/11,
  `teste-apelidos` (59), `teste-conversor-markdown` (17),
  `teste-escape-shortcode`, `teste-atualizador-sync` (9), `validar-especies` (36,
  0 erro), `validar-produtos` (78, 0 erro, os mesmos 9 avisos), `conferir-slugs`,
  `php -l` em tudo e `conferir-protecao-funcoes`; `teste-navegador-visibilidade-ia`
  nas cinco calculadoras com o JavaScript **desligado**; e as **nove** paginas da
  casca e do eixo medidas em Chromium a 360/390/781/782/783/1200 px, **0 px de
  rolagem horizontal** nas seis larguras e console limpo.
- **No ar as 20h13Z: `ferramentas/conferir-peixes-no-ar.py` (novo), 103
  afirmacoes, 0 falha.** A lista de URLs vem do **indice** do sitemap (os dois
  provedores, `page` e `post`), nunca digitada; a aritmetica e conferida celula
  por celula no que o **servidor** devolve; cada degrau do `BreadcrumbList`
  responde 200; a tag do GA4 sobreviveu a troca de versao da casca; e as 18
  paginas foram varridas para provar que nenhuma das cinco e orfa (16.4f),
  descontando menu e trilha, que estao em todas.

### O que este bloco NAO fez, escrito para ninguem procurar

- **Nao tocou no catalogo de produto.** 39 dos 78 produtos seguem esperando link
  de afiliado. Especie nao e produto, e a ficha **diz** por que nao tem link de
  loja em vez de calar: peixe vivo nao se compra por link de afiliado, e o
  equipamento sai pelas calculadoras, onde a vitrine ja existe.
- **Nao moveu URL nenhuma.** Os tres artigos seguem em `/2026/09/08/<slug>/` e as
  cinco calculadoras seguem na raiz, porque a trava do T2 continua de pe ate a
  leitura de 16/09.
- **Nao criou `pauta.md`** (secao 17): 0 escritos, 0 na fila, 0 recusados.

### Fecho de fila

- **Despacho vencido fechado:** a ronda do Clube do Mosaico estava aberta em
  `dados/despachos.md` com prioridade ALTA depois de ja ter acontecido (14h43Z de
  12/09, com `ultima_ronda` gravada e o despacho dela escrito). Movido para
  FECHADOS ao ler a fila — despacho cumprido embaixo de ABERTOS manda a proxima
  execucao refazer trabalho feito, e e a armadilha que o proprio arquivo registra.

**PROXIMO: a leitura de 16/09 manda agora, e ela ganhou uma pergunta nova.** As
cinco URLs de hoje sao as primeiras desta ilha com tres niveis, mae publicada e
`BreadcrumbList` de quatro degraus. Se elas indexarem e a leva de 08/09 continuar
fora, a hierarquia vira hipotese; se nenhuma das duas indexar, a causa e do
dominio e nao da pagina. So depois disso sai a leva 2: as quatro fichas de tetra
que faltam (ember, brilhante, rodostomo, negro), que fecham a categoria, e depois
`/peixes/corydoras/`, com 4 especies do banco passando no portao.


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

## 2026-09-07 (2o disparo) — BLOCO 3 entregue: modelo do banco de produtos

Sessao SEM ferramenta de memoria (estado lido de `ESTADO.md`). Sem Application
Password, o site nao foi tocado: trabalho 100 % no repositorio. `WebSearch`
funciona; `WebFetch` continua bloqueado por dominio (`sicce.com` devolveu
`EGRESS_BLOCKED` hoje, como `seachem.com` no disparo anterior).

Primeiro, o pendente: o Bloco 2 estava na branch `claude/lucid-carson-w52jma`,
fora do `main`. Foi levado ao `main` por push direto (fast-forward
3399f1b..bbc52c1) e o PR #2 fechou como merged. Nao ha mais trabalho fora do
`main` de execucoes anteriores.

Entregue:
- `dados/modelo-banco-produtos.md` — o modelo: 6 principios, identidade do
  produto, campos comuns, as 4 entidades campo a campo (tipo, unidade,
  obrigatoriedade, origem esperada), a escada de 6 niveis de fonte, o
  tratamento de conflito, preco como serie temporal, as 14 regras, os 6
  achados da semente, as limitacoes conhecidas do esquema v1 e a fila de
  coletas.
- `dados/esquema-produtos.json` — o contrato formal (campos, vocabularios,
  derivados, `minimo_para_sugerir` por calculadora, regras V1 a V14).
- `dados/produtos-filtro.json` (5), `produtos-aquecedor.json` (4),
  `produtos-iluminacao.json` (4), `produtos-midia.json` (2) — 15 registros de
  semente, cada campo amarrado a uma entrada de `fontes[]` com url e data.
- `dados/produtos-cotacoes.json` — modelado e VAZIO de proposito.
- `ferramentas/validar-produtos.py` — as regras rodando de verdade. Primeira
  execucao apontou 12 erros nas proprias sementes (campo sem fonte, voltagem
  gravada sem origem, status incoerente); todos corrigidos. Estado final:
  15 produtos, 0 erros, 3 avisos.
- `manifest.json` revisao 2 (7 itens novos em `dados`, todos `publicar: false`
  e com sha256; o esquema de `dados` ganhou as entidades `cotacao` e `esquema`,
  e o manifest ganhou a lista `ferramentas`). `README.md` da ilha documenta a
  pasta `ferramentas/` e o comando de validacao.

Decisoes de modelo que o dado real forcou:
1. **Variante e registro proprio.** Atman AT-3338 x AT-3338S: uma letra muda
   vazao (1200/1500 L/h), potencia (35/18 W), coluna (1,8/1,5 m) e volume
   (ate 450 / 150 a 400 L).
2. **Procedencia por campo, nao por registro** — cada `fontes[]` declara quais
   campos sustenta; o validador reprova campo preenchido sem fonte (V2).
3. **Preco sai do produto** e vira serie temporal com loja e data. Nenhum dos
   precos vistos hoje entrou: sem data de leitura seriam numero inventado.
4. **Voltagem vira requisito de sugestao** (C3, C5, C15), nao da ficha.
5. **Comprimento da luminaria nao e comprimento do aquario** (SunSun ADE-400c:
   peca de 41 cm para aquario de 48 a 65 cm). Ficou pendencia de criterio: a
   C15 so sugere por comprimento de peca depois que a convencao de cobertura
   virar constante `convencao-editorial`.
6. **`posicao_no_fluxo` e o unico campo de origem editorial** do banco e por
   isso nao exige fonte de terceiro.

Achados da semente (todos com fonte nos registros):
- Turnover implicito DECLARADO pelos proprios fabricantes: Eheim 2213 1,76 x/h,
  Atman AT-3338 2,67, SunSun HW-303B 4,00, Seachem Tidal 55 5,00, Atman
  AT-3338S 3,75 a 10,0. Os fabricantes divergem ENTRE SI por 5,7 vezes, alem de
  divergirem das regras de bolso brasileiras. Material pronto para a C3.
- Eficiencia de filtro: 34,3 a 166,7 L/h por W — 4,9x entre modelos que
  "servem" ao mesmo aquario. Base da comparacao de conta de luz da C7.
- A linha Roxin nao segue regra propria: 0,67, 1,0 e 0,86 W/L nos tres
  tamanhos, com um vao sem modelo declarado entre 200 e 250 L.
- Voltagem e o gargalo: 9 dos 13 equipamentos eletricos nao a declaram em
  nenhuma fonte. Hoje a C5 e a C15 sugeririam ZERO produtos, e a C3, dois.
- Iluminacao: 3 das 4 luminarias declaram lumen (83 a 106 lm/W, plausiveis) —
  melhor do que o Bloco 1 previa; o que falta e voltagem, comprimento e ate
  marca (uma e vendida com o nome da loja).
- Midia: 700 (Seachem Matrix) contra 450 m2/L (Eheim SUBSTRAT pro), nenhum dos
  dois publicando o metodo de medicao. A C12 cita os dois e nao ranqueia.

Nao registrado na memoria: esta sessao nao expoe a ferramenta de memoria,
entao `/areas/projeto-aquametria.md` NAO foi atualizado. Copiar esta entrada
para la (e o estado novo em `ESTADO.md`).

Proximo passo desbloqueado: **Bloco 4 — rascunhos dos artigos-ancora** (12 a 15
textos que sustentam as calculadoras; cada tabela tecnica cita o manual do
fabricante e leva data de verificacao). A tabela de turnover implicito por
fabricante e a serie W/L da Roxin ja sao dois artigos com dado proprio.
Coletas baratas que podem ser feitas junto: voltagem dos 9 equipamentos,
`coluna_maxima_m` do HW-303B e do Tidal 55, `volume_filtragem_L` dos canisters
e a `faixa_ajuste_C` da Roxin na embalagem.

## 2026-09-07 (3o disparo, extra) — BLOCO 3b entregue: CASCA DO SITE, e o desembarque virou automatico

Sessao SEM ferramenta de memoria (estado lido de `ESTADO.md`). Disparo manual
pedido pelo Raphael as 11h52 BRT: rodar o 3b hoje, com `publicar: true`.

Pendencias de execucoes anteriores: NENHUMA. O `main` ja estava em `44ec496`
(Bloco 3), e as branches `claude/lucid-carson-w52jma` e `-sbd8tp` nao tinham
commit fora do `main`. A branch desta sessao nasceu de `origin/main`.

Entregue:
- `snippets/aquametria-casca.php` (616 linhas) — nome no Code Snippets
  "Aquametria Casca — identidade e estrutura do site", escopo global, ativo.
  Faz as seis coisas do briefing, sozinho, sem tema filho e sem construtor:
  (a) carrega Chivo, IBM Plex Sans e IBM Plex Mono do Google Fonts e injeta a
      paleta no `wp_head` (prioridade 20, depois do tema): papel de fundo,
      tinta no texto, lamina em link e botao, Chivo nos titulos, Plex Mono em
      numero e unidade. Alem das regras proprias, redefine as variaveis de
      preset do tema de blocos (`--wp--preset--color--base/contrast/primary/
      secondary` e as duas de fonte), que e o que realmente recolore um tema
      de blocos sem editar o tema;
  (b) `render_block` troca `core/site-title` e `core/site-logo` pelo logotipo
      inline em SVG — recipiente graduado, linha de enchimento em lamina,
      marcacoes escuras acima da agua e claras abaixo, sem peixe, sem bolha,
      sem mascote — seguido do wordmark "Aquametria" em Chivo 900. Trava
      estatica: se o tema imprimir os dois blocos, o segundo sai vazio em vez
      de duplicar a marca;
  (c) `render_block` troca `core/navigation` pelo menu proprio
      Calculadoras · Metodologia · Sobre;
  (d) cria, casando pelo slug, `inicio`, `calculadoras`, `metodologia` e
      `sobre`, e fixa `show_on_front=page` com `page_on_front=inicio`;
  (e) manda "Hello world!" e "Sample Page" para a LIXEIRA (`wp_trash_post`,
      nunca apagar), casando por slug E por titulo, nas duas linguas (o site e
      pt-BR, entao `ola-mundo` e `pagina-exemplo` tambem entram na lista), com
      guarda para nunca mandar a pagina inicial para a lixeira;
  (f) rodape proprio no `wp_footer` com a tagline "Calculadoras e dados
      tecnicos para dimensionar o seu aquario" e a nota de fontes.
- O texto das quatro paginas NAO ficou no banco do WordPress: cada pagina
  nasce com um shortcode (`[aquametria_home]`, `[aquametria_calculadoras]`,
  `[aquametria_metodologia]`, `[aquametria_sobre]`) e o conteudo mora no
  proprio snippet. Consequencia pratica: atualizar o snippet atualiza as
  paginas, e o conteudo continua versionado no repositorio, como manda a regra
  de ouro. A home explica o site em tres linhas e lista as 8 calculadoras.
- A pagina `metodologia` publica o quadro dos 8 status de constante com a
  contagem (42 constantes: 24 divergente-fontes-br, 8 pendente, 3
  fabricante-via-busca, 3 transcrita-varejo, 1 fisica, 1 verificada-fabricante,
  1 norma-via-secundaria, 1 convencao-editorial) e a lista dos 7 numeros que a
  Aquametria se recusa a publicar, com o motivo de cada um. Se um dia o banco
  de constantes for publicado como `dados`, a pagina conta ao vivo pela option
  `aquametria_dados_constantes-calculadoras` em vez do instantaneo.
- `manifest.json` revisao 3: o snippet entra com **`publicar: true`** e sha256
  `20e197fc…`, e **`desembarque.aprovado` virou `true`**, com a data e a
  observacao da decisao (so conteudo programatico em escala continua preso).
- `README.md` da ilha, `snippets/README.md` e `conteudo/README.md` atualizados:
  a nova regra de desembarque e a obrigacao de toda calculadora publicada
  aparecer no hub.

Verificacao feita antes de marcar `publicar: true`:
- `php -l` de verdade (PHP 8.4): sem erro de sintaxe.
- Teste de fumaca com o WordPress simulado por stubs: os 4 shortcodes rendem
  (4053, 3442, 5249 e 1987 bytes), `wp_head` sai com 5292 bytes, `wp_footer`
  com 658, `render_block` troca os tres blocos e devolve `core/paragraph`
  intacto, a estrutura cria 4 paginas com 1 unico `flush_rewrite_rules`, manda
  os dois posts padrao para a lixeira e nao toca no rascunho de politica de
  privacidade. **Segunda passada: 0 insercoes** — idempotencia confirmada.
- Render visual em Chromium (Playwright), 1100 px e retina: cabecalho, home,
  cards, metodologia e rodape conferidos; o logotipo le como recipiente
  graduado no tamanho real de cabecalho.

Duas decisoes que valem para os proximos blocos:
1. **O hub e obrigatorio.** A lista das 8 calculadoras vive em
   `aquametria_casca_calculadoras()` com `estado` em `em-construcao` ou
   `publicada`, e passa pelo filtro `aquametria_calculadoras`. Publicar a C1
   sem virar o estado dela na casca deixa a calculadora orfa: o bloco 4 tem
   que mexer nos dois arquivos.
2. **Conteudo institucional mora em shortcode do snippet**, nao em Markdown de
   `conteudo/`. `conteudo/` continua sendo o lugar dos artigos-ancora e das
   paginas de calculadora, que sao texto longo com fonte citada.

Nao registrado na memoria: esta sessao nao expoe a ferramenta de memoria,
entao `/areas/projeto-aquametria.md` NAO foi atualizado. Copiar esta entrada
para la (e o estado novo em `ESTADO.md`).

Proximo passo desbloqueado: **Bloco 4 — C1, a calculadora de litragem**, que e
o nucleo e o estado compartilhado (`localStorage`, chave `aquametria.aquario`).
Ao publica-la, virar o `estado` da C1 para `publicada` na casca e bumpar
`AQUAMETRIA_CASCA_VERSAO`.

### Desembarque desta execucao (07/09/2026, ~15h20 BRT)

Push direto em `main` funcionou (`44ec496..c9e8999`), sem PR. Cinco minutos
depois, `raw.githubusercontent.com` ja servia a revisao 3 com
`aquametria-casca` em `publicar: true` (conferido por WebFetch).

**Sync NAO acionado pela nuvem:** o WebFetch em
`aquametria.com.br/?aquametria_sync=...&forcar=1` voltou `EGRESS_BLOCKED`,
como o ESTADO.md ja previa para o dominio do site. O WP-Cron do proprio site
aplica sozinho em ate 30 minutos, sem intervencao. Nada a fazer alem de
esperar.

URLs para o Raphael conferir depois que o WP-Cron rodar:
- `https://aquametria.com.br/` — home: logotipo, menu, as tres linhas e os 8 cards
- `https://aquametria.com.br/calculadoras/` — hub
- `https://aquametria.com.br/metodologia/` — quadro de status e as 7 recusas
- `https://aquametria.com.br/sobre/`
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — log do Sync (deve
  mostrar `snippets/aquametria-casca: ok` e `revisao 3`)

"Hello world!" e "Sample Page" vao para a LIXEIRA, nao para o apagador: se
alguma coisa der errado, e so restaurar. Se a estrutura precisar ser refeita a
mao, um administrador logado abre `https://aquametria.com.br/?aquametria_casca=refazer`.

---

## 2026-09-07 (4o disparo, correcao) — Sync v1.1.0 e casca v1.0.1

**Nao e bloco novo.** Disparo extra de correcao urgente: o site puxou a revisao
3 e caiu com "Ha um erro critico no seu site". O bloco 4 (C1, litragem)
continua sendo o proximo passo e NAO foi executado aqui.

### Diagnostico (feito fora desta sessao, confirmado no site)
A causa foi o proprio `snippets/aquametria-sync.php` (v1.0.0), que falava a API
antiga do Code Snippets. Na versao instalada (3.10.2):

1. a classe do modelo e `Code_Snippets\Model\Snippet` — `new \Code_Snippets\Snippet()` e fatal;
2. `\Code_Snippets\save_snippet()` devolve o OBJETO Snippet, nao o id — `$id = save_snippet(...)` vira 0/erro;
3. `save_snippet()` de um snippet marcado ativo roda `test_snippet_code()`, que da `eval` no codigo na mesma requisicao;
4. o validador (`Code_Snippets\Utils\Validator`) recusa com "Cannot redeclare function X" quando o snippet ja esta carregado naquela requisicao.

Consequencia que vale para SEMPRE (ja escrita na fase 4b do `ESTADO.md`):
**toda funcao de nivel superior de qualquer snippet da ilha precisa estar dentro
de `if ( ! function_exists( 'nome' ) ) { ... }`** — sem isso, atualizar um
snippet ativo falha ou o deixa inativo em silencio. Vale para a casca e para
todas as calculadoras futuras.

### O que foi entregue

**`snippets/aquametria-sync.php` → v1.1.0** (edicoes cirurgicas, arquivo nao reescrito):
- cabecalho e `AQUAMETRIA_SYNC_VERSAO` em `1.1.0`;
- `aquametria_sync_aplicar_snippet()` detecta a classe do modelo com
  `class_exists()` (`Model\Snippet`, com queda para a antiga) e instancia
  `new $classe()`; se nenhuma existir, devolve erro em vez de fatal;
- grava **inativo** e so entao chama `activate_snippet()`, porque gravar ativo
  faz o plugin dar `eval` no codigo na mesma requisicao; le o retorno como
  objeto (`$ret->id`) com queda para inteiro; releu e confere `active` depois
  de ativar, e **relata** ("gravado (#id) mas NAO ativado: ...") em vez de
  fingir sucesso;
- `aquametria_sync_executar()` envolve o despacho dos tres aplicadores em
  `try/catch ( \Throwable )` — um item quebrado vira linha de log, nao derruba
  o sync inteiro.

**`ferramentas/proteger-funcoes.php`** (nova; ferramenta de bancada, **nao entra
no manifest**): le um snippet e envolve cada funcao de nivel superior em
`if ( ! function_exists( ... ) )`, pulando closures. Uso:
`php ferramentas/proteger-funcoes.php entrada.php saida.php`.

> Ponto em aberto para a proxima execucao: a instrucao deste disparo foi
> explicita — "NAO vai para o manifest" — e foi seguida a risca. Mas o manifest
> tem uma lista `ferramentas` (que o Sync **nao** consome; ele so le `snippets`,
> `conteudo` e `dados`) onde a ferramenta irma `validar-produtos.py` esta
> registrada. Registrar `proteger-funcoes.php` la seria inofensivo e mais
> consistente; fica para o Raphael decidir.

Rodada nos dois snippets: **10 funcoes protegidas no sync** e **14 na casca**,
exatamente o esperado. Conferido que, fora os involucros, nenhuma linha de
codigo mudou. A casca virou **v1.0.1** (so a protecao das funcoes; nenhuma
mudanca de comportamento).

### Verificacao
- `php -l` **de verdade** (com `<?php` prefixado antes de lintar, porque o
  arquivo comeca em `/**` e o lint passaria trivialmente sem isso) nos dois
  snippets: limpo.
- `sha256` recalculado do arquivo final commitado, nao herdado.

| arquivo | sha256 |
| --- | --- |
| `snippets/aquametria-sync.php` | `b72a007c022f60127a36dff34cfbfb552a8b2ba7086041901b8f567b3856e931` |
| `snippets/aquametria-casca.php` | `387e16d5abe5775311eeafec5fc5bcb65567f87c2eea3291e43df4d9655e7980` |

### Manifest
`revisao` = **4**, `atualizado_em` = `2026-09-07`. `aquametria-casca` continua
`publicar: true`. **`aquametria-sync` passou a `publicar: true`** (mantendo
`ativo: true`): a partir da v1.1.0 o Sync pode se atualizar sozinho, e como ele
se pula pelo nome (`AQUAMETRIA_SYNC_NOME_PROPRIO`), isso e inofensivo e deixa o
arquivo rastreado. A `descricao` dele, que ainda dizia "publicar=false e so
registro de procedencia", foi corrigida.

### Sync do site
**Nao acionado nesta execucao, de proposito** — quem aciona e o Cowork, que ja
esta com o navegador aberto. O container da nuvem tambem nao alcanca o dominio
(`EGRESS_BLOCKED`).

Proximo passo desbloqueado (inalterado): **Bloco 4 — C1, a calculadora de
litragem**, o nucleo e o estado compartilhado (`localStorage`, chave
`aquametria.aquario`). Ao publica-la, virar o `estado` da C1 para `publicada`
na casca e bumpar `AQUAMETRIA_CASCA_VERSAO`.

Sem ferramenta de memoria nesta sessao: `/areas/projeto-aquametria.md` NAO foi
atualizado; esta entrada e o `ESTADO.md` sao o registro.

## 2026-09-07 (5o disparo, correcao visual) — rodape duplicado

Nao foi bloco novo: disparo extra para corrigir o que o Raphael viu no site
depois de a casca entrar no ar (revisao 4 aplicada as 16h36). **Ficaram dois
rodapes empilhados**: primeiro o do tema Twenty Twenty-Five, com o credito
"Twenty Twenty-Five · Criado com WordPress", e logo abaixo o rodape escuro da
Aquametria.

### Causa
`aquametria-casca.php` v1.0.1 imprimia o rodape proprio no hook `wp_footer`
(prioridade 20) e nao removia o do tema. Em tema de blocos o rodape e a
template part `footer` (`core/template-part` com `attrs['slug'] === 'footer'`),
renderizada DENTRO do fluxo do conteudo — por isso ela sai acima de qualquer
coisa impressa em `wp_footer`.

### Correcao — casca v1.0.2
- O rodape virou funcao: `aquametria_casca_rodape_html()` (protegida com
  `function_exists`, como todas as outras), acompanhada de
  `aquametria_casca_rodape_impresso()`, que guarda em `static` se o rodape ja
  saiu nesta requisicao.
- **Caminho principal:** o filtro `render_block` que ja existia passou a tratar
  `core/template-part` com slug `footer` (ou `rodape`) e devolve
  `aquametria_casca_rodape_html()` no lugar do rodape do tema — substituicao,
  nao empilhamento.
- O `add_action( 'wp_footer', ... )` que imprimia o rodape foi trocado por uma
  **rede de seguranca**: so imprime se `aquametria_casca_rodape_impresso()` for
  falso (tema sem template part de rodape, ou filtro que nao pegou).
- **Cinto de seguranca em CSS**, para o caso de o filtro nao pegar:
  `.wp-site-blocks > footer.wp-block-template-part .wp-block-group:has(a[href*="wordpress.org"]){display:none;}`
  esconde o credito do WordPress, e
  `body:has(.aqm-rodape) .wp-site-blocks > footer.wp-block-template-part:not(:has(.aqm-rodape)){display:none;}`
  esconde a template part de rodape que nao seja a nossa, quando a nossa ja
  esta na pagina.
- **Residuo extra corrigido na mesma passada:** `core/site-tagline` agora e
  substituido por vazio no `render_block` — era por onde a tagline padrao do
  WordPress ("Just another WordPress site") podia aparecer. Nao ha titulo
  duplicado nem menu do tema sobrando: `core/site-title`, `core/site-logo` e
  `core/navigation` ja eram substituidos desde a v1.0.0, e as quatro paginas
  institucionais nao imprimem `<h1>` proprio (o titulo vem do tema).

O rodape da Aquametria continua com a tagline, o paragrafo de procedencia e a
linha "Metodologia · Sobre · Aquametria 2026". Nenhum credito de tema.
`AQUAMETRIA_CASCA_VERSAO` foi de `1.0.0` (a constante estava atrasada em relacao
ao cabecalho) para `1.0.2`, o que faz a casca remontar a estrutura uma vez —
idempotente, sem duplicar nada.

### Verificacao
- `ferramentas/proteger-funcoes.php` rodado no arquivo final: saida IDENTICA ao
  arquivo (nenhuma funcao desprotegida), 16 funcoes conferidas uma a uma.
- `php -l` de verdade (com `<?php` prefixado, porque o arquivo comeca em `/**`):
  limpo.
- `sha256` recalculado do arquivo final commitado:
  `f8f3d1a06e325b458ff48ec01079e099bf2049e435ba9c27bbeb791a7e896479`.

### Manifest
`revisao` = **5**, `atualizado_em` = `2026-09-07`, `aquametria-casca` continua
`publicar: true` e `ativo: true`; a `descricao` passou a dizer que a casca
substitui o rodape do tema.

Sync **nao acionado** por esta sessao, conforme a instrucao do disparo — quem
aciona e o Cowork.

Proximo passo desbloqueado (inalterado): **Bloco 4 — C1, a calculadora de
litragem**, o nucleo e o estado compartilhado (`localStorage`, chave
`aquametria.aquario`). Ao publica-la, virar o `estado` da C1 para `publicada` na
casca e bumpar `AQUAMETRIA_CASCA_VERSAO`.

Sem ferramenta de memoria nesta sessao: `/areas/projeto-aquametria.md` NAO foi
atualizado; esta entrada e o `ESTADO.md` sao o registro.

## 2026-09-07 (6º disparo, tarefa extraordinária) — links de afiliado da Shopee no banco

Não foi bloco novo da fila: tarefa extraordinária pedida no disparo, que desbloqueia
a monetização. Os links foram gerados pelo Raphael no painel Shopee Afiliados em
07/09/2026, com `Sub_id 1 = aquametria` e `Sub_id 2` = o código da calculadora.

### O que entrou no banco

Campo novo `afiliado` em **todos os 16 produtos** — 10 com link, 6 com o motivo de
não terem. Ele fica logo antes de `fontes[]` em cada registro:

| Calculadora | Produtos com link |
|---|---|
| C3 filtro | Eheim classic 250 (2213), Seachem Tidal 55 |
| C5 aquecedor | Roxin HT-1300 Q3 100 W (anúncio 127 V), 200 W (110 V), 300 W (220 V) |
| C12 mídia | Seachem Matrix 1 L, Eheim SUBSTRAT pro 1 L |
| C15 iluminação | Ista I-401 45 cm, Chihiros WRGB II Pro 60, SunSun ADE-400c |

**Sem anúncio do produto na Shopee em 07/09/2026** (só peças de reposição e
lâmpadas UV), gravados com `"plataforma": null` e o motivo: SunSun HW-303B,
Atman AT-3338, Atman AT-3338S e Eheim Jäger 200 W. Enquanto não houver link, eles
não entram no bloco de produto de nenhuma calculadora.

### Três decisões que mudaram o pedido

1. **Preço não foi para o arquivo de produto.** O pedido dizia guardar
   `preco_referencia` no produto; o esquema do Bloco 3 proíbe (regra V7: nenhum
   campo de preço dentro de `produtos-*.json`, porque preço é série temporal e
   apodrece em semanas), e o validador reprovaria. Os 10 valores viraram **10
   cotações datadas** em `dados/produtos-cotacoes.json`, cada uma com loja, data,
   condição, disponibilidade, voltagem do anúncio, título do anúncio, comissão
   quando informada e o campo `origem_leitura`, que diz que a leitura foi do
   painel pelo operador — não da página pela Aquametria (o egresso da nuvem barra
   `shopee.com.br`). É a mesma informação, no lugar onde ela pode ser auditada.
2. **O link da Ista não foi colado no registro que existia.** O anúncio é da
   luminária de **45 cm** (7,6 W, 810 lm); o registro do banco era a de **60 cm**
   (35 W, 3717 lm). São produtos diferentes: colar o link ali faria a C15 prometer
   3717 lm e entregar 810. Entrou o registro `ista-i-401-45`, com ficha própria
   (Aquarius Hobby, nível varejo, lida por busca porque o domínio dá
   EGRESS_BLOCKED), e o de 60 cm ficou sem link, com o motivo escrito.
3. **O LED genérico "Newpet Slim 30–60 cm" não virou produto.** É outro produto,
   de outro revendedor, e a busca de 07/09 não achou ficha com potência e lúmen
   de fabricante ou varejo especializado — só anúncio de marketplace, que pelo
   esquema (nível 6) não sustenta número técnico. O link ficou em
   `dados/afiliados-sem-produto.json`, com o que o desbloqueia. Link sem
   especificação verificada não pode ser sugerido por calculadora.

### Troca de registro na iluminação

`aquario-projetado-x1-fr-60w` **saiu** do banco (pedido do disparo: não tem anúncio
real na Shopee). Entrou no lugar `chihiros-wrgb-ii-pro-60`, com as specs refeitas
por duas fontes de varejo especializado que concordam entre si — Green Aqua
(74 W, 6630 lm, aquários de 60 a 80 cm, 60 LEDs WRGB, IP43, controle por app
Bluetooth) e Aquasabi (600 × 140 × 18 mm) — ambas lidas por resultado de busca,
porque `chihiros.eu` devolveu EGRESS_BLOCKED. O PAR de 50–60 citado pelo varejo
vem "no substrato", sem distância em cm: sem distância o PPFD é inútil e a regra
V5 o rejeita, então não foi gravado. A voltagem não é declarada por nenhuma das
fontes — e voltagem é requisito para SUGERIR — então ele entra como ficha, não
como sugestão.

O registro removido, transcrito para o caso de voltar (também está no histórico do
git, commit `08d84dc`):

```json
{
  "id": "aquario-projetado-x1-fr-60w", "entidade": "iluminacao",
  "marca": null, "linha": "X1-FR", "modelo": "X1-FR 60 W Wi-Fi", "variante": "60 W",
  "nomes_alternativos": ["Luminaria X1-FR 60W 5000 lumens"],
  "gtin": null, "disponibilidade_br": "vendido", "voltagem": null,
  "tipo": "led-pendente", "potencia_w": 60, "fluxo_lm": 5000,
  "temperatura_cor_k": null, "espectro": null,
  "ppfd_declarado": null, "ppfd_distancia_cm": null,
  "comprimento_luminaria_cm": null, "comprimento_aquario_cm": null,
  "regulagem": "app", "volume_atendido_declarado_L": null,
  "fontes": [{ "origem": "varejo", "status": "transcrita-varejo",
    "referencia": "Aquario Projetado (varejo BR especializado), ficha da luminaria X1-FR 60 W com 5000 lumens e controle Wi-Fi",
    "url": "https://www.aquarioprojetado.com/luminaria-x1-fr-60w-5000-lumens-wi-fi-luminaria-para-aquario-plantado",
    "verificado_em": "2026-09-07",
    "campos": ["potencia_w", "fluxo_lm", "regulagem", "tipo"],
    "observacao": "Ficha de varejo. Confira a embalagem." }],
  "conflitos": [], "verificado_em": "2026-09-07", "status_registro": "parcial",
  "observacao": "Tem lumen, nao tem comprimento: cai na validacao V13 e nao pode ser sugerido. 83 lm/W."
}
```

### Regra nova: V15, e o relatório que ela abriu

O esquema virou **v2**: o campo `afiliado` está documentado (`plataforma`, `url`,
`sub_id_1`, `sub_id_2`, `rel`, `verificado_em`, `anuncio_shopee`,
`voltagem_anuncio`, `motivo`), com as regras de renderização (`rel="sponsored"`,
`target="_blank" rel="noopener"`, aviso visível de comissão, preço sempre com data)
e a proibição de link apontando para outra variante. `ferramentas/validar-produtos.py`
ganhou a regra **V15**: todo produto tem `afiliado`; com plataforma preenchida
exige URL https, os dois `sub_id`, o título do anúncio e `rel: "sponsored"`, e
proíbe qualquer campo de preço lá dentro; com plataforma `null` exige o motivo.

O relatório do validador passou a separar, por calculadora, **apto com link** de
**apto sem link**. O que ele mostra hoje é o trabalho que sobra:

```
c12-midia-filtrante    3 com link, 0 apto(s) sem link, 4 barrado(s)
c15-iluminacao         1 com link, 0 apto(s) sem link, 4 barrado(s)
c3-vazao-filtro        0 com link, 2 apto(s) sem link, 3 barrado(s)
c5-aquecedor-delta     0 com link, 0 apto(s) sem link, 4 barrado(s)
c7-consumo-custo       7 com link, 6 apto(s) sem link, 1 barrado(s)
16 produtos, 10 cotacoes, 0 erro(s), 2 aviso(s)
```

**Ter link não basta.** A C15 hoje só consegue sugerir UM produto (a Ista de
45 cm) e a C5, ZERO. A C5 continua em zero porque os três Roxin
não declaram `faixa_ajuste_C` nem voltagem — e voltagem de anúncio não conta, que
é exatamente por que ela foi para `voltagem_anuncio` e não para o campo `voltagem`:
anúncio de marketplace é nível 6 e não sustenta número técnico. A C3 tem dois
produtos aptos (Atman) que não têm link, e dois com link (Eheim 2213, Tidal 55)
barrados por voltagem e coluna máxima. **A coleta que destrava dinheiro agora é
voltagem e `faixa_ajuste_C` de fabricante, não mais link.**

### Verificação
- `python3 ferramentas/validar-produtos.py`: **16 produtos, 10 cotações, 0 erros,
  2 avisos** (os dois avisos são antigos: eficiência implausível do Tidal 55 e
  faixa de 13,3× do Eheim Jäger).
- Todo JSON reaberto com `json.load` depois de gravado.
- `sha256` de todos os arquivos alterados recalculado do arquivo final commitado.

### Manifest
`revisao` = **6**, `atualizado_em` = `2026-09-07`. Hashes atualizados de
`produtos-filtro`, `produtos-aquecedor`, `produtos-iluminacao`, `produtos-midia`,
`produtos-cotacoes` (agora 10 registros), `esquema-produtos` e
`modelo-banco-produtos`; entrada nova `afiliados-sem-produto`. Tudo continua
`publicar: false` — é dado interno, não vai para o site sozinho.

Próximo passo desbloqueado (inalterado): **Bloco 4 — C1, a calculadora de
litragem**, o núcleo e o estado compartilhado (`localStorage`, chave
`aquametria.aquario`). Ao publicá-la, virar o `estado` da C1 para `publicada` na
casca e bumpar `AQUAMETRIA_CASCA_VERSAO`. A C1 não tem bloco de produto (litragem
não vende equipamento); o primeiro bloco de produto com link será o da C3.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-07 (6º disparo, bloco do dia) — BLOCO 4 começa: C1, a calculadora de litragem

Primeira calculadora no ar. Snippet, página e itens de manifest com `publicar: true`.

### O que foi entregue
- `snippets/aquametria-calculadora-litragem.php` — snippet **Aquametria
  Calculadora de Litragem**, escopo front-end, v1.0.0, shortcode
  `[aquametria_calculadora_litragem]`.
- `conteudo/calculadora-de-litragem.md` — a página, com front matter, o
  shortcode no corpo e a explicação metodológica.
- `manifest.json` revisão **7**, os dois itens com `publicar: true` e sha256
  conferido do arquivo final.

### Decisões que a construção fixou (valem para C3, C5, C12, C15…)

1. **Todo o cálculo é JavaScript no navegador.** O site está atrás do cache de
   página da hospedagem: HTML que dependesse da query string seria servido
   errado para o visitante seguinte. Como consequência, a página é estática e o
   permalink é lido e escrito pelo próprio JS (`history.replaceState`).
2. **A calculadora se anuncia no hub, em vez de a casca listá-la.** O snippet
   registra `add_filter( 'aquametria_calculadoras', ... )` e vira o `estado` da
   C1 para `publicada`. Ganho: nenhuma edição da casca, nenhum bump de
   `AQUAMETRIA_CASCA_VERSAO`, e desativar o snippet devolve o cartão para "em
   construção" sozinho. **É este o caminho para as próximas** — a casca já
   previa o filtro, ninguém tinha usado.
3. **A chave do estado compartilhado é `aquametria.aquario`** (com ponto), como
   manda a tarefa. A especificação do Bloco 2 dizia `aquametria_aquario`; ela
   foi corrigida para a chave publicada, que é a que vale.
4. **Vírgula decimal é entrada válida.** Ninguém digita "80.5" no Brasil. Os
   campos são `text` com `inputmode="decimal"` e a leitura troca vírgula por
   ponto.
5. **Litro sai inteiro a partir de 100 L**, com uma casa abaixo disso. Precisão
   falsa (109,47 L) mente sobre a incerteza de um volume que nem desconta
   substrato.

### O que a página recusa, e diz por quê
Não desconta substrato. `substrato-densidade` (1 a 2 kg/L contra 1 kg ≈ 1 L, 100 %
de diferença) e `substrato-porosidade` (nenhuma fonte publica) estão `pendente`,
e constante pendente é proibida em fórmula. A tela declara a consequência — o
volume real fica **superestimado** — e publica a tabela de direção do erro:
seguro para filtro, aquecedor e mídia; **inseguro** para lotação e dosagem. Fica
registrado o protocolo de medição própria que libera o desconto.

### Dois defeitos do Sync que a primeira página em Markdown expôs (v1.1.1)
- **O front matter era impresso na página.** `aquametria_sync_md()` não o
  descartava; a página teria começado com "titulo:", "slug:", "publicar: true".
  Agora o bloco `---…---` do topo é cortado antes da conversão.
- **O shortcode saía dentro de `<p>`.** `<div>` dentro de `<p>` é HTML inválido:
  o navegador fecha o parágrafo no meio e a página fica remendada. Linha que só
  tem shortcode agora sai como bloco próprio.
- De quebra, **toda tabela vinda de Markdown agora sai dentro de um bloco que
  rola** — uma tabela de três colunas empurrava a página inteira para o lado no
  celular.

### Verificação (o que foi realmente rodado)
- `php -l` de verdade nos dois snippets (com `<?php` prefixado, porque o arquivo
  começa em `/**`): limpo.
- `ferramentas/proteger-funcoes.php` nos dois: saída **idêntica** ao arquivo —
  nenhuma função de nível superior desprotegida.
- **Teste de fumaça em PHP com stubs de WordPress**: o filtro do hub vira só a
  C1 para `publicada` e deixa a C3 em construção; o shortcode devolve 28 KB de
  HTML na primeira chamada e string vazia na segunda (uma instância por página);
  nenhum id duplicado; 26 `<div>` abertas e 26 fechadas; acentos preservados.
- **Teste em navegador de verdade** (Chromium via Playwright), 9 casos: cálculo
  com vidro (80 × 40 × 40, 8 mm → 128 L brutos, 118 L internos, 109 L reais);
  vírgula decimal e desconto de rochas; sem espessura (diz "sem número" e avisa
  que a lâmina saiu superestimada); medidas internas (bruto = interno); erro de
  unidade (800 cm barrado, saída escondida); lâmina maior que a altura interna
  (limitada ao máximo físico, com aviso); caminho inverso (100 L com 80 × 40 →
  31,3 cm de altura, e a água que caberia); permalink reabrindo com as entradas;
  estado retomado do `localStorage` em nova visita. **Zero erro de console.**
- **Conversão do Markdown pelo próprio Sync**: front matter removido, shortcode
  fora do `<p>`, tabela convertida, 6 `<h2>`, 2 links internos.
- **Página final montada (conteúdo + shortcode) em 390 px de largura**: sem
  rolagem horizontal do documento depois da correção da tabela.

### Desembarque
Automático, como decidido em 07/09/2026. Depois do push em `main`, o Sync precisa
ser acionado (WebFetch da nuvem costuma cair no bloqueio de egresso; se cair,
fica para o WP-Cron, que roda a cada 30 minutos). URLs a conferir:
`https://aquametria.com.br/calculadora-de-litragem/` e o hub
`https://aquametria.com.br/calculadoras/`, onde o cartão da C1 deve passar de
"Em construção" para "Abrir calculadora".

Próximo passo desbloqueado: **C3 — vazão do filtro e turnover**, que é a primeira
com bloco de produto (e a primeira a usar os links de afiliado gravados hoje).
Ela lê `aquametria.aquario` do navegador. Atenção ao que o validador já mostra:
dos filtros com link, o Eheim 2213 e o Tidal 55 estão barrados por falta de
voltagem e coluna máxima — sem coletar isso, o bloco de produto da C3 nasce vazio.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como nas execuções anteriores — o container da nuvem não
alcança o site, só o GitHub. O `raw.githubusercontent.com` **já serve a revisão
7** (conferido nesta sessão), então o WP-Cron do próprio site, que roda a cada 30
minutos, aplica sozinho. Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

Depois disso, conferir:
- `https://aquametria.com.br/calculadora-de-litragem/` — a calculadora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C1 deve ter virado
  "Abrir calculadora";
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

---

## 08/09/2026 — Bloco 4: C3, a calculadora de vazão do filtro, no ar (com o primeiro bloco de produto)

**Disparo extra**, autorizado pelo Raphael, pedindo a C1. A C1 já estava no `main`
(commits `0989345` e `4cf5a8f`, execução das 20h47 UTC de 07/09) — a referência
local é que estava velha. Como o bloco pedido estava entregue, esta execução fez
**o próximo passo desbloqueado: a C3**, que é a primeira calculadora com bloco de
produto e a primeira a usar os links de afiliado gravados ontem.

### O problema que precisou ser resolvido antes da calculadora

O validador dizia, no início da sessão: `c3-vazao-filtro — 0 com link`. Os dois
únicos filtros com link de afiliado estavam barrados por campo faltante, e sem
eles o bloco de produto da C3 nasceria vazio. Foi resolvido com **coleta, não com
afrouxamento de regra**:

- **Eheim classic 250 (2213)**: ganhou `voltagem: ["110"]`, com fonte de varejo BR
  (Pró-Aquarista e Bixo da Água anunciam a versão 110 V). Nenhum anúncio brasileiro
  visto declara a versão 220 V, então o campo registra só o que tem fonte — e o
  cartão de produto obriga o aviso de conferir a voltagem no anúncio, porque o
  anúncio de afiliado não a declara.
- **Seachem Tidal 55**: ganhou `voltagem: ["110","220"]` (Biotopos 110 V,
  Amazon.com.br 220 V) e saiu de `revalidar` para `completo`.
- **A correção de modelo que isso revelou**: `coluna_maxima_m` estava marcada como
  obrigatória para todo filtro, mas **hang-on não tem recalque a vencer** — ele fica
  pendurado na borda. Exigir o campo dele era defeito do esquema, não dado faltando.
  Entrou `coluna_maxima_nao_se_aplica`, e a obrigatoriedade virou condicional ao tipo
  (`obrigatorio_se_tipo: [canister, sump]`), legível pelo validador.
- **A regra V10** (eficiência acima de 120 L/h por W é implausível) ficou restrita a
  canister e sump: o Tidal 55 declara 1000 L/h com 6 W — 167 L/h por W — porque
  hang-on trabalha a coluna quase zero. O limite tinha sido calibrado para canister.

Resultado: a C3 passou de 0 para **4 filtros sugeríveis** (Eheim 2213, Tidal 55,
Atman AT-3338 e AT-3338S), 2 deles com link. O SunSun HW-303B segue barrado por
não ter coluna máxima publicada por nenhuma fonte.

### A decisão editorial desta execução (regra V16)

A execução anterior tinha deixado implícito que produto sem link de afiliado não
entra no bloco. Isso é ordenar por comissão pelo caminho inverso, e contraria a
regra do projeto ("a ordem é por adequação técnica ao resultado, jamais por
comissão"). Ficou escrito como regra de validação:

> **V16.** Link de afiliado NÃO entra em critério de sugestão. A lista de produtos
> de uma calculadora é montada e ordenada só por adequação técnica ao resultado;
> produto tecnicamente apto é mostrado tenha ou não link, e quem tem link ganha o
> botão de loja, marcado como patrocinado.

Na prática: os dois Atman aparecem na lista, no lugar que a adequação técnica manda,
com a frase "ainda não temos link de loja para este modelo".

### O que foi entregue

**`snippets/aquametria-calculadora-vazao.php`** (novo, v1.0.0) — shortcode
`[aquametria_calculadora_vazao]`. Lê o volume real que a C1 guardou em
`localStorage`, devolve a faixa em L/h com o critério e a fonte de cada extremo,
os cartões por banda (piso do fabricante · leitura conservadora BR · regra de bolso
BR, ou plantado), o volume mínimo do sump quando marcado, o caminho inverso, o
veredito do filtro que a pessoa já tem, o quadro de fontes e o permalink citável.
Anuncia-se sozinho no hub pelo filtro `aquametria_calculadoras`.

**O bloco de produto**, que é a novidade estrutural: nasce dentro da resposta, como
consequência do cálculo. Cada cartão mostra a placa da marca com a vazão, **o
turnover que aquele filtro entrega naquele aquário** (não no volume genérico do
catálogo), a ficha com a fonte e a data, e o botão da loja com
`rel="sponsored noopener" target="_blank"` quando existe link. O aviso de comissão
é obrigatório e visível dentro do bloco. Sem filtro que atenda a faixa, o bloco
não aparece e a tela diz quantos filtros o banco tem e por que nenhum serviu.
**Preço não entra**: snippet é código que fica meses no ar e preço envelheceria na
tela; a política está escrita na página de divulgação.

**`conteudo/calculadora-de-vazao-do-filtro.md`** — a metodologia: por que a resposta
é faixa e não número, o argumento dos dois lados, o que a calculadora não faz (fator
de perda de carga e turnover marinho, ambos pendentes por falta de fonte), o
protocolo do balde no lugar do fator inventado, a coluna máxima como corte, e as
três regras do bloco de produto.

**`conteudo/divulgacao-de-afiliados.md`** (página nova) — exigida pelo primeiro
bloco de produto e pela autorregulamentação publicitária brasileira. Declara o link
de afiliado, transcreve a V16 na íntegra, mostra a escada de fontes e admite o
tamanho atual do programa.

**Ligações, para nenhuma página nascer órfã:** a casca (v1.0.3) passou a linkar a
divulgação no rodapé de todo o site; a C1 (v1.0.1, snippet e página) passou a
**linkar** a C3, que antes só citava; a C3 aponta de volta para a C1, o hub, a
metodologia e a divulgação. O hub já mostra C1 e C3 como publicadas.

**`ferramentas/gerar-catalogo-filtros.py`** (nova) — o site não lê o repositório em
tempo de execução, então o banco de filtros viaja dentro do PHP. Este gerador
reescreve o trecho entre `CATALOGO-INICIO` e `CATALOGO-FIM` a partir de
`dados/produtos-filtro.json`, aplicando o `minimo_para_sugerir` do esquema. É o que
impede as duas cópias de divergirem.

**Sync v1.1.2** — o conversor de Markdown não entendia citação em bloco e imprimia
o `>` escapado no meio do parágrafo. As duas páginas novas usam citação (a fórmula
do protocolo do balde e a regra V16), então o conversor foi corrigido, com estilo
próprio na casca.

### Verificação (o que foi realmente rodado)
- **`php -l` de verdade** nos quatro snippets (com `<?php` prefixado): limpo.
- **`ferramentas/proteger-funcoes.php`** nos quatro: saída idêntica ao arquivo —
  nenhuma função de nível superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 16 produtos, **0 erro**, 1 aviso conhecido
  (a faixa de 13,3x do Eheim Jager, que é conteúdo da C5, não defeito).
- **Teste de fumaça em PHP com stubs de WordPress**: o hub vira C1 e C3 para
  `publicada` e deixa as outras seis em construção; o shortcode devolve 42 KB na
  primeira chamada e string vazia na segunda; nenhum id duplicado; 21 `<div>`
  abertas e 21 fechadas, 5 `<ul>` e 5 fechadas; acentos preservados; catálogo com
  4 filtros; aviso de comissão e link da divulgação presentes.
- **Teste em navegador de verdade** (Chromium via Playwright), 12 casos: caso base
  (110 L comunitário → 190 a 1.100 L/h, Eheim e Tidal na lista, Eheim entregando
  4,0 x/h); **atributos do link de afiliado** (`sponsored noopener` + `_blank` em
  todos, aviso de comissão visível); perfil plantado mudando o teto para 550 L/h;
  coluna de 1,6 m barrando o Eheim de 1,5 m com o motivo na tela; filtro por tipo;
  **estado vindo da C1** (volume 109,5 preenchido, cálculo automático, e a mescla
  preservando medidas e apelido da C1 enquanto a C3 acrescenta o dela); permalink
  por query string; caminho inverso; **aquário de 15 L sem produto que atenda** (o
  bloco não aparece e a tela explica); sump; erro de unidade escondendo a saída;
  convite para a C1 quando não há estado; 390 px sem rolagem horizontal.
  **Zero erro de console.**
- **Conversão do Markdown pelo próprio Sync** nas três páginas: front matter
  removido, shortcode fora do `<p>`, tabela em bloco que rola, citação em bloco
  correta, 6/5/6 `<h2>`, links internos presentes.
- **sha256 do manifest conferido contra os arquivos finais commitados**: todos batem.

### Desembarque
Automático. Manifest na revisão 8. Depois do push em `main`, o Sync precisa ser
acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-vazao-do-filtro/` — a calculadora nova;
- `https://aquametria.com.br/divulgacao-de-afiliados/` — a página de afiliados;
- `https://aquametria.com.br/calculadoras/` — o cartão da C3 deve ter virado
  "Abrir calculadora";
- `https://aquametria.com.br/calculadora-de-litragem/` — deve ter ganhado o link
  para a C3;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

Próximo passo desbloqueado: **C5 — potência do aquecedor por delta térmico**. Atenção
ao que o validador já mostra: os quatro aquecedores do banco estão barrados
(`voltagem` nos quatro, `faixa_ajuste_C` nos três Roxin, que está em conflito
varejo-contra-varejo). Sem essa coleta, o bloco de produto da C5 nasce vazio — e o
caminho é o mesmo desta execução: coletar com fonte antes de escrever a calculadora.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 8** (conferido nesta
sessão, sem atraso de cache), então o WP-Cron do próprio site, que roda a cada 30
minutos, aplica sozinho. Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

## 2026-09-08 (8º disparo) — BLOCO 4: C5, a potência do aquecedor, no ar com o artigo-âncora pareado

Sessão SEM ferramenta de memória (estado lido de `ESTADO.md` e deste registro).
Sem Application Password, o site não foi tocado: trabalho 100 % no repositório.
Egresso: `WebSearch` funciona; `WebFetch` cai em `EGRESS_BLOCKED` em qualquer
domínio que não seja o GitHub — inclusive Cobasi, tentado hoje. Por isso toda
ficha coletada nesta execução entrou como `transcrita-varejo` ou
`fabricante-via-busca`, com a observação de reconferir.

### O bloqueio real não era a calculadora, era o banco

A execução anterior deixou o aviso: os quatro aquecedores do banco estavam
barrados pelo validador. Faltava `voltagem` nos quatro e `faixa_ajuste_C` nos
três Roxin, esta última em conflito varejo-contra-varejo. Escrever a C5 sem
resolver isso entregaria uma calculadora com bloco de produto sempre vazio.

Então a coleta veio primeiro, e mudou o tamanho do banco:

**Voltagem, o campo que barrava tudo.** As duas linhas são vendidas no Brasil
em 110 V e em 220 V, na mesma potência — Cobasi publica duas fichas do Roxin
HT-1300, uma por tomada; Tudo de Bicho, WorldFish, AquaMaeda, Aquarioz e
Peixinho e Cia repetem; a Pró-Aquarista publica Thermocontrol 100 W 110 V,
250 W 110 V e 300 W 220 V. O campo virou `["110","220"]` nas duas linhas, com a
ressalva escrita na própria fonte: **o que ela sustenta é que EXISTE versão para
as duas tomadas**, não que um anúncio específico seja de uma delas. Daí o cartão
de produto obrigar o aviso de conferir a voltagem, dizendo qual versão o anúncio
que conferimos abria.

**O banco foi de 4 para 9 aquecedores**: Eheim Jäger 50, 100, 150 e 200 W e
Roxin HT-1300/Q3 25, 50, 100, 200 e 300 W. Cobre de 25 a 300 W, que é a faixa
onde mora o aquarismo brasileiro doméstico. O validador saiu de **0 de 4 aptos
para 9 de 9** na `c5-aquecedor-delta` (3 com link de afiliado, 6 sem — e, pela
V16, os seis sem link aparecem do mesmo jeito, só sem botão de loja).

### A regra V17, que é a decisão editorial desta execução

A faixa de ajuste da linha Roxin aparece publicada de dois jeitos no varejo:
22 a 34 °C numas fichas, 16 a 32 °C noutras. As duas são varejo, ou seja, do
mesmo nível. A regra antiga mandava zerar o campo — e zerar o campo tirava das
sugestões o aquecedor mais vendido do Brasil, por excesso de escrúpulo.

Ficou escrita a regra V17 no esquema (versão 3):

> Quando duas fontes do MESMO nível discordam sobre um intervalo, publica-se a
> **interseção** delas: o maior dos mínimos e o menor dos máximos. Não é média
> nem escolha de fonte — é a única faixa que todas as fontes concordam que o
> aparelho cobre. Exige `valor_conservador` e `derivacao` no conflito, e a
> calculadora que usar esse valor **tem de dizer na tela** que a faixa é a
> conservadora e por quê. Interseção vazia continua sendo `campo-vira-null`.

No caso do Roxin: 22 a 32 °C. Na prática, quem quer 30 °C para acará-disco vê o
Roxin na lista; quem quer 33 °C não vê, e lê o motivo; quem quer 20 °C para
kinguio também não vê, porque a faixa conservadora começa em 22 °C. É menos do
que o aparelho talvez faça, e é exatamente tudo o que as fontes sustentam.

Junto veio a **V18**: aquecedor sugerido tem de alcançar a temperatura-alvo
dentro da faixa que o registro sustenta. No bloco de produto da C5, duas
barreiras de segurança vêm ANTES da adequação técnica — a voltagem da tomada e o
termostato chegar ao alvo. O validador aprendeu a conferir a interseção de
verdade (se o `valor_conservador` não for a interseção dos valores em conflito,
é erro) e o `minimo_para_sugerir` aceita a alternativa `conflito:campo`.

### O achado, que virou o artigo

Ao levantar a linha Eheim Jäger inteira para completar a constante
`eheim-jager-linha-comercial`, apareceu o volume declarado potência a potência:

| Modelo | Volume declarado | W/L no teto |
|---|---|---|
| 25 W | 20 a 25 L | 1,00 |
| 50 W | 25 a 50 L | 1,00 |
| 75 W | 50 a 75 L | 1,00 |
| 100 W | 75 a 100 L | 1,00 |
| 125 W | 100 a 125 L | 1,00 |
| 150 W | 125 a 150 L | 1,00 |
| 200 W | 300 a 400 L | 0,50 |

Um vírgula zero, seis vezes seguidas. **O "1 W por litro" que a web brasileira
repete sem citar ninguém não veio de física: veio da prateleira.** O catálogo do
fabricante nomeia cada aparelho pelo volume que dá exatamente 1 W/L, e a regra
de bolso leu a caixa e transformou o rótulo em lei. Isso explica por que fontes
que não se citam repetem o mesmo número.

E a régua quebra em três lugares, todos registrados como conflito no banco:
o 200 W sai da série (0,50 W/L); o catálogo Eheim declara esse mesmo 200 W para
30 a 400 L (treze vezes); e o Jäger de 150 W aparece declarado para 125-150 L
numa ficha e para 200-300 L noutra, as duas de varejo, o dobro de diferença.

De quebra, a constante ficou completa: faltavam as potências de **125 W e
250 W**, que eram justamente os dois dos "9 tamanhos" que a coleta do Bloco 2
não tinha achado.

### O que foi entregue

**`snippets/aquametria-calculadora-aquecedor.php`** (novo, v1.0.0) — shortcode
`[aquametria_calculadora_aquecedor]`. Pede o volume real (herdado da C1) e **a
temperatura mínima do cômodo onde o aquário fica**, que é a entrada que nenhuma
outra calculadora brasileira pede. Devolve a faixa de potência com o nome do
autor em cada extremo e faz uma coisa que nenhuma fonte faz: **separa as regras
que se aplicam ao caso das que não se aplicam, e mostra as duas listas** — saber
qual regra não vale para você é parte da resposta. Traz o degrau da linha
comercial, o confronto com o volume da caixa, o caminho inverso, o quadro de
fontes e o permalink citável. Anuncia-se sozinha no hub pelo filtro
`aquametria_calculadoras`.

**O que ela se recusa a fazer, escrito na página:** não publica a via física
`P = U · A · ΔT` (falta `u-vidro-aquario`, pendente); não corrige por tampa — o
campo existe e muda o TEXTO, nunca o número, porque quantificar a perda pela
lâmina livre é exatamente a constante que falta; não usa mínima por cidade
(`temperatura-minima-por-cidade`, pendente); e **não extrapola a regra de bolso
acima de 10 °C de ΔT**, que é o limite que a única fonte com delta declarado
afirmou — acima disso a tela diz com essas palavras que nenhuma fonte cobre o
caso e entrega a faixa genérica como PISO. Com ΔT ≤ 0 não devolve número nenhum
e explica por quê.

**`conteudo/calculadora-de-potencia-do-aquecedor.md`** — a metodologia: a tabela
das quatro constantes com a condição que cada autor declarou, por que a caixa do
aquecedor não dimensiona, o que a calculadora não faz e por quê, o que é
critério editorial declarado (mirar no degrau que cobre o topo; dois aquecedores
acima de 150 W, que é argumento de modo de falha e não de eficiência) e a
explicação da faixa conservadora.

**`conteudo/quantos-watts-de-aquecedor-para-aquario.md`** — o artigo-âncora
pareado, o primeiro do projeto. Não repete a calculadora: mostra de onde o
"1 W por litro" veio, onde a régua quebra, o caso Belém contra Curitiba (cinco
vezes mais ΔT para a mesma resposta da regra), o que as quatro fontes brasileiras
dizem e não dizem, a fórmula que ainda não podemos publicar e por quê, e seis
recomendações práticas. Linka a calculadora no primeiro terço; a calculadora
linka de volta.

**Correção na C1 (v1.0.2), dívida que a C5 tornaria pior:** `guardar()`
SUBSTITUÍA o estado compartilhado em vez de mesclar — voltar à C1 para corrigir
uma medida zerava a vazão que a C3 tinha calculado e o clima que a C5 tinha
perguntado. Agora mescla, e `recuperar()` aceita estado sem `medidas`, que é
como a C3 e a C5 gravam.

**Sync v1.1.3** — duas coisas. O conversor passou a entender bloco de código
cercado por crases triplas (a fórmula do artigo sairia com as crases impressas).
E passou a converter **link relativo à raiz**: antes só link `https` virava
`<a>`, e link relativo saía com os colchetes no meio do texto — defeito
silencioso, porque não é erro de sintaxe nenhum e só aparece lendo a página no
ar. Foi pego pelo teste de conversão, não por leitura.

**Ligações, para nenhuma página nascer órfã:** a C1 (v1.0.2) e a C3 (v1.0.1)
passaram a LINKAR a C5, no snippet; a C5 aponta de volta para a C1, a C3, o hub,
a metodologia, a divulgação de afiliados e o artigo pareado; o artigo aponta para
as três calculadoras e para a metodologia. O hub já mostra C1, C3 e C5 como
publicadas, sozinho.

**Ferramentas novas:** `gerar-catalogo-aquecedores.py` (mantém sincronizadas as
duas cópias do banco, já que o site não lê o repositório em tempo de execução, e
carrega a faixa conservadora do V17 quando o campo ficou null);
`render-para-teste.php` (monta qualquer shortcode numa página HTML solta com
WordPress falso, carregando todos os snippets menos o Sync — também é teste de
convivência entre calculadoras); `teste-navegador-c5.mjs` (os 15 cenários).

### Verificação (o que foi realmente rodado)
- **`php -l` de verdade** nos cinco snippets (com `<?php` prefixado): limpo.
- **`ferramentas/proteger-funcoes.php`** nos cinco: saída idêntica ao arquivo —
  nenhuma função de nível superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 21 produtos, **0 erro**, 1 aviso
  conhecido (o V11 do Jäger 200 W, que é conteúdo da página, não defeito).
  `c5-aquecedor-delta`: 9 aptos, 0 barrados.
- **Teste de fumaça em PHP com stubs de WordPress**: o hub vira C1, C3 e C5 para
  `publicada`; o shortcode devolve 62 KB na primeira chamada e string vazia na
  segunda; 38 ids, nenhum duplicado; div, ul, form, table, li e p balanceados;
  acentos preservados; catálogo com 9 aquecedores, todos com voltagem e faixa de
  ajuste; aviso de comissão e link da divulgação presentes; nenhuma superglobal
  de servidor.
- **Teste em navegador de verdade** (Chromium via Playwright), 15 casos: caso
  base (110 L, alvo 26 °C, mínima 20 °C → 110 a 165 W, degrau comercial de
  200 W, 3 produtos); **atributos do link de afiliado** (`sponsored noopener` +
  `_blank` + https, aviso de comissão visível, aviso de voltagem em todo cartão
  com link); voltagem 220 V filtrando a lista e avisando que o anúncio conferido
  era de 110 V; **alvo de 33 °C barrando o Roxin pelo teto conservador de 32 °C**
  com o motivo na tela; **alvo de 20 °C barrando pelo piso conservador de 22 °C**;
  ΔT de 14 °C dizendo que nenhuma fonte cobre e marcando a regra do delta como
  não aplicável; região Sul entrando na conta (teto vai a 220 W); ΔT ≤ 0 sem
  número nenhum; espécie preenchendo o alvo pelo meio da faixa com a fonte
  citada; aquário de 900 L sem produto que atenda (o bloco some e a tela
  explica); **mescla do `localStorage`** preservando as medidas da C1 e a vazão
  da C3 enquanto a C5 acrescenta clima, voltagem e potência-alvo; permalink;
  caminho inverso; erros de campo obrigatório e de unidade; 390 px sem rolagem
  horizontal. **Zero erro de console.**
- **Conversão do Markdown pelo próprio Sync** nas cinco páginas: front matter
  removido, shortcode fora do `<p>`, tabelas em bloco que rola, citação em bloco,
  bloco de código, nenhuma crase solta, links convertidos, tags balanceadas.
- **sha256 do manifest conferido contra os arquivos finais commitados**: 25 itens,
  0 divergências.

### Desembarque
Automático. Manifest na revisão 9. Depois do push em `main`, o Sync precisa ser
acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/` — a calculadora nova;
- `https://aquametria.com.br/quantos-watts-de-aquecedor-para-aquario/` — o artigo-âncora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C5 deve ter virado "Abrir calculadora";
- `https://aquametria.com.br/calculadora-de-litragem/` e
  `https://aquametria.com.br/calculadora-de-vazao-do-filtro/` — devem ter ganhado o link para a C5;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

Próximo passo desbloqueado: **C12 — mídia filtrante**, pareada com o artigo dela.
Atenção ao que o validador já mostra: três filtros (Atman AT-3338, AT-3338S e
Seachem Tidal 55) estão sem `volume_filtragem_L` e por isso barrados na C12, e o
banco de mídia tem só dois registros. O caminho é o mesmo das duas últimas
execuções: **coletar com fonte antes de escrever a calculadora** — é a coleta que
decide se o bloco de produto nasce cheio ou vazio. A C12 é o vácuo de conteúdo
nº 1 do levantamento e já tem duas âncoras de fabricante que conflitam por duas
vezes (Seachem Matrix, 1,25 mL/L numa leitura da copy e 2,6 mL/L noutra) mais os
12 mL/L de cesto do Eheim 2213.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 9** (conferido nesta
sessão, sem atraso de cache: 5 snippets e 5 páginas com `publicar: true`), então
o WP-Cron do próprio site, que roda a cada 30 minutos, aplica sozinho. Para
acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

---

## 2026-09-08 (9º disparo) — BLOCO 4: C12, a mídia filtrante, no ar com o artigo-âncora pareado

Bloco entregue: **C12 — mídia filtrante**, quarta calculadora do lote, pareada
com o artigo `quanta-midia-biologica-o-aquario-precisa`. É o **vácuo de conteúdo
nº 1** do levantamento do Bloco 1 — e era o vazio que a própria página "Sobre"
do site cita como um dos motivos de a Aquametria existir.

### A coleta veio antes da calculadora, de novo, e foi ela que decidiu tudo

A execução anterior deixou o diagnóstico certo: o banco tinha **duas** âncoras
de dosagem, as duas da Seachem, e três filtros barrados por falta de
`volume_filtragem_L`. Uma calculadora com duas leituras da mesma marca não é
comparação, é um duelo interno. A primeira hora foi coleta.

**Quatro dosagens declaradas por fabricante, onde havia duas** (todas colhidas
por busca — o egresso continua bloqueado para `seachem.com`, `jbl.de` e as lojas
brasileiras — e reconfirmadas em varejo especializado que replica a mesma ficha):

| Constante nova | Valor | Fonte |
|---|---|---|
| `jbl-micromec-dosagem` | 5,00 mL/L | JBL: 650 g para 200 L, e a mesma embalagem é vendida como 1 L |
| `ocean-tech-bio-glass-dosagem` | 12,50 mL/L | Ocean Tech: 1 L para cada 80 L |
| `seachem-matrixcarbon-dosagem` | 0,625 mL/L | Seachem: 250 mL para 400 L, "vários meses" |
| `seachem-purigen-dosagem` | 0,25 mL/L | Seachem: 100 mL para 400 L, até 6 meses |

Mais `seachem-tidal-55-midia` (1,2 L de mídia para 200 L = 6,0 mL/L de mídia
TOTAL), que dá o par do `eheim-classic-250-2213` na segunda família de âncoras.

**O achado que virou o artigo.** A Ocean Tech é a **única marca brasileira** que
publica mL de mídia por litro de água — e ela pede **dez vezes** o que a Seachem
pede para a mesma função. A hipótese óbvia (mídias diferentes, áreas diferentes)
morre na aritmética: área declarada × dosagem declarada = área entregue por litro
de **água**, e ela vai de 0,88 m² (Seachem) a 7,5 (JBL) a 18,8 (Ocean Tech) —
**21 vezes**. Pior: a marca que declara MAIS área por litro de mídia (Ocean Tech,
1.500 m²/L) é a que pede DEZ VEZES mais mídia que a que declara menos (Seachem,
>700 m²/L). Se a área fosse o critério, a relação seria a inversa. Nenhuma das
quatro publica método de medição. É o eixo do artigo e é original: não achamos
ninguém, em português, cruzando essas duas colunas.

**O segundo achado, de brinde:** a Seachem discorda de si mesma em dois níveis.
Como fabricante de mídia diz que 1,25 mL/L de Matrix bastam; como fabricante de
filtro põe 6,0 mL/L de espaço de mídia no Tidal 55. E, dentro da mesma copy do
Matrix, "250 mL para 200 L" (1,25 mL/L) contra "1 L para 100 galões" (2,64 mL/L).

**Volume útil de mídia dos filtros** (`volume_filtragem_L`, que destravava a C12):
Tidal 55 com 1,2 L do próprio fabricante; Atman AT-3338 e AT-3338S com ficha de
varejo **ambígua**, e a ambiguidade virou conteúdo. A frase "3 cestos de 17x17x6
com capacidade de 1,6 litros de mídia" pode ser 1,6 L no total ou por cesto
(4,8 L) — e a geometria (1,73 L brutos por cesto) apoia a leitura por cesto. No
modelo irmão a mesma frase dá 3,5 L em cestos de 21×21×7 cm, que têm 3,09 L
brutos e **não comportam** 3,5 L: aqui só a leitura do conjunto fecha. A mesma
frase, dois modelos, leituras opostas apoiadas pela própria geometria declarada.
Registrado como `conflitos[]` com `publicar-os-dois`, e a tela mostra as duas.
O SunSun HW-303B continua barrado: nenhuma fonte publica a capacidade dos cestos.

### O que foi entregue

**`snippets/aquametria-calculadora-midia.php` (v1.0.0, 1.675 linhas)** — o
shortcode `[aquametria_calculadora_midia]`. As âncoras **não são digitadas no
JavaScript**: saem do catálogo embutido, que sai do banco de produtos. Mídia nova
com dosagem declarada entra na tabela sozinha no próximo gerador — não há como as
duas cópias divergirem em silêncio.

O que ela entrega: a faixa de mídia biológica (para 110 L, de 140 mL a 1,38 L)
dizendo com todas as letras que **a faixa é 10 vezes larga porque os fabricantes
discordam 10 vezes, não porque a conta seja imprecisa**; as duas tabelas de
âncoras, separadas porque respondem perguntas diferentes; e **o teto físico** —
quanto do cesto do filtro escolhido cada dosagem ocuparia, com barra e
porcentagem, avisando quando a camada biológica sozinha estoura ("o problema não
é a mídia, é o filtro"). Essa conta é trivial e não a encontramos publicada em
português. Mais: ordem das camadas, camada química nas duas unidades que não
conversam, calendário de trocas com datas calculadas a partir da última
manutenção, TPA, gatilhos de nitrato, e o caminho inverso.

**O que ela se recusa a fazer, escrito na tela:** não escolhe uma dosagem; não
reparte o cesto em porcentagens (`proporcao-entre-camadas-do-cesto`, pendente —
publica a ORDEM, que tem fonte); não converte grama em mililitro no carvão
(`densidade-aparente-carvao-ativado`, pendente — mas a FREQUÊNCIA compara sem
conversão: a regra BR manda trocar de 4 a 10 vezes mais que o fabricante do
carvão); não compara marcas por área de superfície; não dimensiona mídia sem
dosagem declarada (o Eheim Substrat pro sai no cartão sem número de compra,
dizendo por quê); e não estima validade de mídia biológica.

**`conteudo/calculadora-de-midia-filtrante.md`** — a metodologia: as duas tabelas
com atribuição, o teto físico, as fichas ambíguas do Atman destrinchadas, a lista
de recusas e o aviso obrigatório sobre lavar mídia biológica publicado como
**mecanismo explicado** (cloro existe para matar bactéria; a colônia leva semanas;
por isso a substituição é parcial; para a sujeira grossa, use a água da TPA).

**`conteudo/quanta-midia-biologica-o-aquario-precisa.md`** — o artigo-âncora, o
segundo do projeto. Não repete a calculadora: desenvolve o paradoxo da área, a
Seachem contra si mesma, o caso do carvão, e a **crítica de fundo** — todas as
quatro dosagens são por litro de ÁGUA, mas o trabalho da mídia depende da amônia
que entra, ou seja, da carga de peixes, que nenhuma declaração pergunta. Fechar
isso exigiria `taxa-de-nitrificacao-por-area` (pendente, registrada). Linka a
calculadora no primeiro terço; a calculadora linka de volta.

**Constantes:** 42 → 50. Cinco novas com fonte e três **pendências declaradas**
(proporção entre camadas, densidade do carvão, taxa de nitrificação), que existem
no registro justamente para dizer o que a C12 não publica e por quê.

**Banco:** 21 → 25 produtos. Mídias de 2 para 6 (JBL MicroMec, Ocean Tech Bio
Glass, Seachem MatrixCarbon, Seachem Purigen — todas sem link de afiliado, porque
a geração do link curto é manual no painel Shopee e fica fora desta sessão; pela
regra V16 elas saem no cartão do mesmo jeito, sem botão de loja). Três filtros
ganharam `volume_filtragem_L`.

**Ligações, para nenhuma página nascer órfã:** a C1 (v1.0.3), a C3 (v1.0.2) e a
C5 (v1.0.1) passaram a LINKAR a C12 nos painéis de ligação; a casca (v1.0.4) teve
o resumo da C12 no hub reescrito de "duas âncoras" para as quatro reais; a C12
aponta de volta para C1, C3, C5, hub, metodologia, divulgação de afiliados e o
artigo pareado.

**Ferramentas novas:** `gerar-catalogo-midias.py` (escreve DOIS blocos no mesmo
snippet, porque a C12 consome os dois bancos, e carrega a segunda leitura dos
campos em conflito para a tela publicar as duas) e `teste-navegador-c12.mjs`
(19 cenários).

### Verificação (o que foi realmente rodado)
- **`php -l` de verdade** nos seis snippets (com `<?php` prefixado): limpo.
- **`ferramentas/proteger-funcoes.php`** nos quatro snippets tocados: saída
  idêntica ao arquivo — nenhuma função de nível superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 25 produtos, **0 erro**, 1 aviso
  conhecido (o V11 do Jäger 200 W, que é conteúdo da página, não defeito).
  `c12-midia-filtrante`: 4 aptos com link, 6 sem link, 1 barrado (o SunSun, por
  falta de `volume_filtragem_L` — e a tela diz isso).
- **Teste de fumaça estrutural**: 45 ids, nenhum duplicado; div, ul, li, form,
  table, p, tbody, span e a todos balanceados; acentos preservados; nenhuma
  superglobal de servidor no HTML; aviso de comissão e link da divulgação
  presentes; `rel="sponsored noopener"` no JS; nenhum preço cravado.
- **Teste em navegador de verdade** (Chromium via Playwright), **19 cenários, todos
  passando**: caso base; as quatro âncoras com atribuição e link de fonte; a
  segunda família de âncoras; teto físico num Eheim classic 250 (Seachem 5 %,
  Ocean Tech 46 %); **teto estourado** (600 L num Tidal 55, com "Não cabe" e "o
  problema é o filtro"); as duas leituras da ficha do Atman na tela; volume de
  mídia digitado à mão, com o critério editorial declarando que a medida é da
  pessoa; ordem das camadas com a recusa da proporção; camada química com as duas
  unidades e a recusa da conversão; calendário de trocas com datas calculadas
  (perlon 08–16/09, carvão 16/09–01/10, cerâmica 01/03–01/09 de 2027); TPA e
  nitrato; **o aviso obrigatório** sobre lavar mídia; bloco de produto com 4
  mídias (6 com química marcada); **atributos do link de afiliado** (`sponsored
  noopener` + `_blank` + https nos dois links); **mescla do `localStorage`**
  preservando medidas da C1, clima da C5 e vazão da C3; permalink; caminho
  inverso; erros de entrada; 390 px sem rolagem horizontal. **Zero erro de
  console.**
- **Teste da C5 rodado de novo** depois de tocar o snippet dela: todos os 15
  cenários continuam passando (sem regressão pela ligação nova).
- **Conversão do Markdown pelo próprio Sync** nas sete páginas: front matter
  removido, shortcode fora do `<p>`, tabelas dentro do bloco que rola, nenhuma
  crase solta, nenhum link markdown por converter, tags balanceadas.
- **sha256 do manifest conferido contra os arquivos finais commitados**: 30 itens,
  0 divergências.

### Desembarque
Automático. Manifest na **revisão 10**. Depois do push em `main`, o Sync precisa
ser acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-midia-filtrante/` — a calculadora nova;
- `https://aquametria.com.br/quanta-midia-biologica-o-aquario-precisa/` — o artigo-âncora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C12 deve ter virado "Abrir calculadora", com o resumo novo;
- `https://aquametria.com.br/calculadora-de-litragem/`, `/calculadora-de-vazao-do-filtro/` e
  `/calculadora-de-potencia-do-aquecedor/` — devem ter ganhado o link para a C12;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

**Próximo passo desbloqueado: C15 — iluminação e fotoperíodo**, pareada com o
artigo dela. Atenção ao que o validador já mostra: dos 5 registros de iluminação,
**4 estão barrados** — três por falta de `voltagem` (Aquários do Rio LED 60 cm,
Chihiros WRGB II Pro 60, ISTA IL-401-60) e um por falta de `fluxo_lm` (SunSun
ADE-400C). O caminho é o mesmo das três últimas execuções: **coletar com fonte
antes de escrever a calculadora**, porque é a coleta que decide se o bloco de
produto nasce cheio ou vazio. E há uma armadilha própria da C15 registrada na
especificação: `ppfd-por-litragem` está **pendente**, e a regra V5 exige que
`ppfd_declarado` e `ppfd_distancia_cm` andem juntos — PPFD sem distância declarada
não entra. A constante `iluminacao-lumen-por-litro` tem três fontes que chamam as
mesmas faixas pelos mesmos nomes com números diferentes, que é exatamente o
padrão que a C12 acabou de aprender a publicar em tabela com atribuição.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 10** (conferido
nesta sessão, sem atraso de cache: 6 snippets e 7 páginas com `publicar: true`),
então o WP-Cron do próprio site, que roda a cada 30 minutos, aplica sozinho.
Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

**Uma coisa depende do Raphael, e não bloqueia nada.** As quatro mídias novas
(JBL MicroMec, Ocean Tech Bio Glass, Seachem MatrixCarbon e Seachem Purigen)
entraram no banco **sem link de afiliado**, porque a geração do link curto é
feita à mão no painel Shopee Afiliados, fora desta sessão. Pela regra V16 elas
já aparecem no bloco de produto, com a quantidade calculada e a ficha completa,
só sem botão de loja — a página está correta e completa do jeito que está. Mas
são quatro cartões monetizáveis parados: hoje só o Seachem Matrix e o Eheim
Substrat pro têm link na C12. Gerar os quatro links (Sub_id_2 = `C12`) e colar
em `dados/produtos-midia.json` é trabalho de cinco minutos no painel, e a
próxima execução pega sozinha. O mesmo vale para os 6 aquecedores e as 2
luminárias que já estão aptos e sem link desde as execuções anteriores.

---

## 2026-09-08 (10º disparo) — BLOCO 4: C15, a iluminação e o fotoperíodo, no ar com o artigo-âncora pareado

Bloco entregue: **C15 — iluminação e fotoperíodo**, quinta calculadora do lote,
pareada com o artigo `quantos-lumens-por-litro-aquario-plantado`. É o maior
cluster empatado do levantamento do Bloco 1 (83 consultas, junto com o C10).

### De novo, a coleta veio antes da calculadora — e de novo era o bloqueio real

A execução anterior deixou o diagnóstico: dos 5 registros de iluminação, **4
estavam barrados** — três por `voltagem`, um por `fluxo_lm`. Com 1 luminária
sugerível, o bloco de produto nasceria vazio. A primeira hora foi coleta, toda
por resultado de busca (o egresso da nuvem continua barrando `proaquarista.com.br`,
`aquariosdorio.com.br` e as demais lojas brasileiras — o WebFetch devolve
`EGRESS_BLOCKED`, e as fichas entram marcadas como `transcrita-varejo` lida por
busca, com o pedido de conferir a embalagem).

O que a coleta trouxe:

| Registro | O que faltava | O que a ficha declarou em 08/09 |
|---|---|---|
| `ista-il-401-60` | voltagem | bivolt (110/220 V), cobre aquário de 56 a 66 cm, peça de 56 × 12 × 4,6 cm, IRC > 95 % |
| `aquarios-do-rio-led-60cm` | voltagem | bivolt, cobre 55 a 75 cm com suportes reguláveis, timer com até 3 fotoperíodos e nascer/pôr do sol |
| `wfish-wf-h600-wrgb` (novo) | — | 36 W, bivolt, WRGB, peça de 56,7 × 8 cm, cobre 60 a 65 cm; **sem lúmen em fonte alguma** |
| `chihiros-wrgb-ii-pro-60` | voltagem | **nada**: nenhuma fonte declara. Continua barrada, e tem link de afiliado |
| `sunsun-ade-400c` | lúmen | **nada**: nenhuma loja publica. Continua barrada, e tem link de afiliado |

Resultado: **3 aptas de 6** (contra 1 de 5), 1 delas com link. Duas luminárias
que TÊM link de afiliado seguem barradas — e isso virou conteúdo de tela, não
constrangimento escondido: a lista dos barrados é publicada na página, com o
motivo de cada um e a frase "link não promove produto barrado".

### O achado que virou o artigo: a régua usa a unidade errada

O lúmen é ponderado pela sensibilidade do olho humano, que pesa o verde e
desconta azul e vermelho profundos — que são exatamente as duas faixas em que a
clorofila trabalha. Consequência incômoda para a regra de lm/L: **a luminária
projetada para planta tende a marcar MENOS lúmens que uma calha branca de mesmo
consumo, e a régua a considera pior.** O nosso banco é coerente com isso — a
Chihiros WRGB II Pro 60 dá 89,6 lm/W e a calha branca Ista IL-401 dá 106 lm/W —
e o artigo apresenta os dois números como **indício, não demonstração**, porque
dois produtos não provam padrão nenhum.

**E a trilha do PPFD termina antes do Brasil.** Procurando a tabela de PAR da
linha WRGB II Pro para o banco, chegamos ao fórum de suporte da própria
Chihiros — marca cujo argumento de venda é PAR: a resposta oficial é que **não
existe teste de PAR oficial** e que o usuário procure medições no YouTube. Ou
seja, a ausência brasileira não é preguiça de blogueiro: o fabricante não
publica. `ppfd-por-litragem` continua `pendente`, agora com URL e data, e a
página publica esse motivo em vez de só dizer "não temos fonte".

### O segundo achado: o nome não é o tamanho da peça

O varejo brasileiro nomeia luminária por centímetro, e o centímetro do nome nem
sempre é o da peça. A Ista vendida como "IL-401 60 cm" mede **56 cm** na ficha
de dimensões da mesma página. Registrado como `conflitos[]` (nome comercial,
origem `marketplace-anuncio`, contra ficha de varejo — `nivel-mais-alto-vence`),
e a calculadora mostra os dois números no cartão.

Disso saiu a **decisão editorial desta execução**, que fecha uma pendência
aberta desde o Bloco 3 (`pendencia_de_criterio` da entidade iluminação):

> **A Aquametria NÃO converte comprimento de peça em cobertura de aquário.**
> Nos 5 registros que declaram os dois números, o teto declarado vai de **1,15 a
> 1,59 vez** o comprimento da peça (41 cm cobrindo 65; 60 cm cobrindo 66) e o
> piso de 0,92 a 1,17. Não há razão constante a extrair, e fabricar uma média
> serviria para recomendar luminária que deixa as pontas na sombra.

Virou a constante `cobertura-luminaria-declarada` (status `convencao-editorial`,
com a `derivacao` escrita), o `minimo_para_sugerir` da `c15-iluminacao` passou a
exigir `comprimento_aquario_cm` **declarado**, e o esquema foi para a versão 4.
O efeito da convenção é só barrar sugestão: ela nunca cria número.

### O que foi entregue

**`snippets/aquametria-calculadora-iluminacao.php` (v1.0.0)** — o shortcode
`[aquametria_calculadora_iluminacao]`, escopo global, anunciado no hub pelo
filtro `aquametria_calculadoras`. O que ele põe na tela:

- **A faixa de lúmens** no volume da pessoa, pela faixa consolidada do nível
  escolhido (baixa 10–20, média 20–40, alta 40–60+ lm/L) — e, ao lado, **a
  tabela das três leituras brasileiras**, com o nome de quem publicou cada uma.
  A divergência é calculada e dita: 2,0 vezes sobre o rótulo "baixa".
- **Faixa aberta no nível alto**: uma das fontes escreve "acima de 40 lm/L" e
  para aí. A resposta sai com "+" em vez de um teto inventado.
- **Os quatro regimes de fotoperíodo**, com o da pessoa marcado, e a frase que
  falta em toda tabela copiada: hora a mais não compensa lúmen a menos.
- **O bloco de CO2 com os dois limites que se sobrepõem** (útil 15–35 mg/L,
  risco acima de 30–35) publicados como sobreposição, mais o drop checker; e o
  aviso obrigatório quando o nível alto é escolhido **sem** CO2.
- **Aviso de lâmina acima de 45 cm**, que é onde lm/L começa a mentir por não
  saber a profundidade.
- **Painel de consumo**: kWh/mês do fotoperíodo escolhido (física pura) e reais
  **só com a tarifa que o visitante digita** — tarifa de energia não é publicada
  aqui, e a tela diz por quê.
- **Bloco de produto** com a cobertura de comprimento como barreira, a lista
  publicada dos barrados, e um caso que mostra o preço das regras: a luminária
  mais cara do banco tem link de afiliado e **não** é sugerida.
- **Caminho inverso** (tenho X lúmens, que aquário isso cobre em cada nível).

**`conteudo/calculadora-de-iluminacao.md`** — página-âncora com o shortcode, a
tabela das três leituras, as três coisas que a calculadora faz de diferente, as
quatro que ela recusa fazer com o motivo de cada uma (com a tabela de peça ×
cobertura), as regras do bloco de produto e as seções de fotoperíodo, CO2 e
profundidade.

**`conteudo/quantos-lumens-por-litro-aquario-plantado.md`** — o artigo pareado,
com o eixo da unidade errada, a trilha do PPFD que termina na própria Chihiros,
o que o varejo declara no lugar (centímetros), a armadilha do nome, onde as três
fontes **concordam**, seis recomendações práticas e as três coletas que faltam
— incluindo a recusa de publicar fator de conversão de lux para PPFD, que
depende do espectro e não tem fonte.

**Banco e ferramentas:** `dados/produtos-iluminacao.json` (6 registros, 0 erro
no validador), `dados/constantes-calculadoras.json` (51 constantes),
`dados/esquema-produtos.json` v4, `ferramentas/gerar-catalogo-iluminacao.py`
(escreve DOIS blocos no snippet: os aptos e os barrados com motivo) e
`ferramentas/teste-navegador-c15.mjs` (21 cenários).

**Nenhuma página nasce órfã:** C1 (v1.0.4), C3 (v1.0.3), C5 (v1.0.2) e C12
(v1.0.1) passaram a linkar a C15 no painel de ligações, cada uma com o motivo
técnico da ligação. A casca não precisou ser tocada: a C15 vira "publicada" no
hub pelo próprio filtro, e o resumo do cartão é reescrito pelo snippet.

**Uma decisão de arquitetura pequena e que vale para as próximas:** o banco de
produtos é escrito **sem acento** (convenção do repositório) e a tela sai
**acentuada**. Então o gerador manda a **estrutura** do conflito (campo, valor,
origem) e quem escreve a frase é o JavaScript do snippet. Texto de banco não vai
para a tela.

### Verificação (o que foi realmente rodado)

- **`php -l` de verdade** nos 7 snippets, e `ferramentas/proteger-funcoes.php`
  devolvendo saída idêntica ao arquivo em todos — nenhuma função de nível
  superior desprotegida.
- **`ferramentas/validar-produtos.py`**: 26 produtos, **0 erro**, 1 aviso
  conhecido (o V11 do Jäger 200 W, que é conteúdo da página). `c15-iluminacao`:
  1 apto com link, 2 aptos sem link, 3 barrados.
- **Teste em navegador de verdade** (Chromium via Playwright), **21 cenários e
  mais de 60 verificações, todos passando**: caso base; as 9 linhas da tabela de
  leituras com as três fontes nomeadas; a divergência de 2,0 vezes no rótulo
  "baixa"; a faixa aberta do nível alto com "+"; o aviso de luz alta sem CO2; a
  sobreposição dos limites de CO2 e o drop checker; os quatro regimes; o aviso
  de lâmina de 55 cm; a recusa de listar produto sem o comprimento do aquário; o
  bloco de produto (dois cartões, ordenados pela proximidade do meio da faixa, o
  conflito nome-contra-ficha publicado no cartão, o modelo de 810 lm barrado
  pela cobertura com o motivo na tela); a lista dos três barrados; os atributos
  do link de afiliado (`sponsored noopener`, `_blank`, https); o aviso de
  comissão e o link da divulgação; o caso sem nenhuma luminária que cubra 120 cm;
  o consumo (5,0 kWh/mês e R$ 4,79 com tarifa de R$ 0,95) e a recusa de publicar
  tarifa padrão; o caminho inverso; a **mescla do `localStorage`** preservando
  medidas da C1, vazão da C3 e clima da C5; o permalink e a reconstrução por
  query string; os erros de entrada; 390 px sem rolagem horizontal.
  **Zero erro de console.**
- **Testes da C5 e da C12 rodados de novo** depois de tocar os dois snippets:
  todos os cenários continuam passando (sem regressão pelas ligações novas).
- **Conversão do Markdown pelo próprio Sync** nas duas páginas novas: front
  matter removido, shortcode fora do `<p>`, as duas tabelas de cada página
  dentro do bloco que rola, nenhuma crase solta, nenhum link markdown por
  converter, tags balanceadas, acentos preservados.
- **sha256 do manifest conferido contra os arquivos finais commitados**: todos
  os itens, 0 divergências.

### Desembarque

Automático. Manifest na **revisão 11**. Depois do push em `main`, o Sync precisa
ser acionado; o WebFetch da nuvem cai no bloqueio de egresso, então fica para o
WP-Cron, que roda a cada 30 minutos. URLs a conferir:
- `https://aquametria.com.br/calculadora-de-iluminacao/` — a calculadora nova;
- `https://aquametria.com.br/quantos-lumens-por-litro-aquario-plantado/` — o artigo-âncora;
- `https://aquametria.com.br/calculadoras/` — o cartão da C15 deve ter virado "Abrir calculadora";
- `/calculadora-de-litragem/`, `/calculadora-de-vazao-do-filtro/`,
  `/calculadora-de-potencia-do-aquecedor/` e `/calculadora-de-midia-filtrante/`
  — devem ter ganhado o link para a C15;
- `https://aquametria.com.br/wp-json/aquametria/v1/status` — o log do Sync.

**Próximo passo desbloqueado: C2 — peso do aquário cheio e carga no piso**,
pareada com o artigo dela. É a próxima da ordem depois da C15. Duas travessas
já conhecidas, registradas na especificação: (a) a C2 **não publica espessura de
vidro** nem veredito de "a laje aguenta" — falta tensão admissível e coeficiente
de segurança citáveis; (b) a carga de projeto da NBR 6120 está no corpus como
`norma-via-secundaria` (norma paga, não lida direto), e a tela precisa dizer isso
com essas palavras. O que a C2 tem de sólido é a aritmética: volume × densidade
+ vidro + substrato + rochas, e a carga por metro quadrado comparada com a de
projeto. O padrão das quatro últimas execuções continua valendo: **a coleta vem
antes da calculadora**.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

### Nota de desembarque (mesma execução)

**Sync não acionado pela nuvem**: `WebFetch` em `aquametria.com.br` devolveu
`EGRESS_BLOCKED`, como em todas as execuções anteriores — o container só alcança
o GitHub. O `raw.githubusercontent.com` **já serve a revisão 11** (conferido
nesta sessão, sem atraso de cache: 7 snippets e 9 páginas com `publicar: true`,
incluindo `calculadora-de-iluminacao` e `quantos-lumens-por-litro-aquario-plantado`),
então o WP-Cron do próprio site, que roda a cada 30 minutos, aplica sozinho.
Para acionar na hora, basta abrir no navegador:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`

**O que depende do Raphael, e não bloqueia nada.** A dívida de links de afiliado
cresceu e agora tem um caso que dói: das 3 luminárias que a C15 consegue sugerir,
só a Ista I-401 45 cm tem link — o LED 60 cm dos Aquários do Rio e a Ista IL-401
60 cm entram no cartão sem botão de loja, e a IL-401 é justamente a que mais
aparece, porque cobre a faixa de aquário mais comum (56 a 66 cm). Somando com o
que já estava parado: 4 mídias, 6 aquecedores e agora 2 luminárias aptas e sem
link. Gerar os links no painel Shopee Afiliados (Sub_id_2 = `C15` para as
luminárias) e colar em `dados/produtos-*.json` é trabalho de minutos, e a
próxima execução pega sozinha.

E o inverso também está registrado: **duas luminárias que TÊM link continuam
barradas** — a Chihiros WRGB II Pro 60 (nenhuma fonte declara voltagem) e a
SunSun ADE-400c (nenhuma loja publica lúmen). Elas não são sugeridas, e a página
diz isso na cara, com o motivo. Uma foto da embalagem de qualquer uma das duas
resolveria o campo que falta.

---

## 2026-09-08 (11º disparo, correção urgente) — o Sync não se atualiza sozinho: nasceu o atualizador

**Fila normal interrompida a pedido do Raphael.** A C2 (peso e carga no piso) fica
para a próxima execução. Esta rodada resolveu um defeito visível no site e, mais
importante, o gargalo estrutural que o produziu.

### O defeito

O Raphael abriu `https://aquametria.com.br/calculadora-de-litragem/` e viu o front
matter YAML do arquivo Markdown impresso **dentro do corpo da página**:
"— id: calculadora-de-litragem tipo: pagina titulo: … publicar: true —", com a lista
de fontes virando lista com marcadores. Os `---` viraram travessão porque o
`wptexturize` do WordPress converte três hifens em em-dash.

### A causa, confirmada nesta sessão

O repositório estava **certo**. O que roda no site é que estava velho.

- `ilhas/aquametria/snippets/aquametria-sync.php` está na v1.1.3 desde 08/09 e corta
  o front matter em `aquametria_sync_md()` desde a **v1.1.1** (07/09).
- O snippet "Aquametria Sync" **ativo no site** é a **v1.1.0**, colada à mão pelo
  Raphael em 07/09.
- Rodei o conversor da v1.1.3 sobre os 9 arquivos reais de `conteudo/`: **nenhum
  resíduo de YAML em nenhum deles**. O lado do repositório nunca produziu o defeito.

E o motivo de a correção nunca ter chegado ao site é estrutural, não um esquecimento:

> **O Sync se pula a si mesmo de propósito.** Em `aquametria_sync_aplicar_snippet()`,
> a checagem `$nome === AQUAMETRIA_SYNC_NOME_PROPRIO` devolve "pulado". Isso protege o
> site — o Sync não se reescreve no meio da própria execução — e, como efeito colateral
> permanente, **nenhuma correção no próprio Sync chega ao site sozinha**.

Quatro versões do conversor de Markdown (1.1.1, 1.1.2, 1.1.3 e agora a 1.1.4) ficaram
só no repositório sem ninguém notar, porque o log do Sync dizia "aplicado com sucesso"
— e dizia a verdade. As páginas *foram* aplicadas. Pelo conversor velho.

### 1. Sync v1.1.4 — o corte do front matter ficou tolerante

A regex antiga (`/\A---\n.*?\n---\n?/s`) exigia o arquivo perfeito. Três variações que
**não aparecem no editor** a derrotavam em silêncio, e uma delas produz exatamente a
tela que o Raphael viu:

| Variação | O que acontecia antes |
| --- | --- |
| BOM no começo do arquivo | o BOM fica antes do `---` e o corte não casa |
| quebra de linha antiga, só `\r` | o arquivo inteiro vira uma linha só |
| espaço ou tabulação à direita do `---` | o corte não casa e o YAML sai como parágrafo |

Agora o conversor tira o BOM, normaliza `\r\n` **e** `\r` sozinho, e aceita espaço ou
tabulação à direita dos dois delimitadores. O `---` legítimo no meio do texto continua
intocado (é caso de teste).

**`ferramentas/teste-conversor-markdown.php`** (novo) roda o conversor do próprio
snippet Sync sobre todos os arquivos de `conteudo/` e recusa qualquer resíduo de
metadado no HTML — chaves como `publicar:`, `verificado_em:`, `slug:`, HTML que comece
por separador, primeiro bloco que não seja texto — mais as oito variações de front
matter acima. **17 casos, 0 falhas.**

### 2. O ATUALIZADOR — a entrega estrutural

**`snippets/aquametria-atualizador-sync.php`**, nome no Code Snippets
**"Aquametria Sync — atualizador do Sync"**, escopo global, ativo, `publicar: true`.

Como o **nome é diferente** do nome do Sync, a v1.1.0 que está no site vai instalá-lo e
ativá-lo pelo caminho que já funciona. E a única coisa que ele faz é reescrever o Sync
a partir do repositório. Cada trava existe por um motivo:

- **sha256 contra o manifest, antes de qualquer coisa.** Divergiu, aborta e registra —
  nunca grava código não verificado.
- **Coerência de versão:** o arquivo tem de declarar a mesma versão que o manifest
  anuncia. Manifest desatualizado não vira gravação.
- **Sintaxe de verdade, sem executar o código:** `token_get_all( $codigo, TOKEN_PARSE )`
  faz o parse completo e levanta `ParseError` em código quebrado. É o mais perto de um
  `php -l` que dá para fazer dentro do WordPress sem `eval` — e `eval` aqui seria
  justamente o erro que derrubou o site em 07/09.
- **Backup, e a releitura que prova que ele existe:** grava o código atual em
  `aquametria_sync_backup_codigo` (com versão, id do snippet, sha e data) e **relê a
  option** comparando o tamanho. Sem backup confirmado, não prossegue.
- **Gravação pelo caminho que a v1.1.0 já usa e que sabidamente funciona:**
  `Code_Snippets\Model\Snippet`, `save_snippet()` lido como **objeto**, gravação
  **INATIVA** primeiro e `activate_snippet()` depois, tudo em `try/catch`. Nunca
  `new \Code_Snippets\Snippet()`.
- **A verificação é uma REQUISIÇÃO NOVA.** Nesta requisição o código velho continua
  carregado na memória do PHP, então perguntar à constante não prova nada. Ele busca
  `/wp-json/aquametria/v1/status` e confere `versao_sync`. Não bateu, ou o endpoint
  devolveu erro, **restaura o backup automaticamente**. Loopback mudo (o site fechado
  para si mesmo) conta como **inconclusivo** e mantém o código novo: derrubar a versão
  nova por falta de prova seria pior que mantê-la, e fica escrito no log.
- **No máximo uma vez por hora**, por WP-Cron, e só quando a versão do manifest difere
  da que está rodando. A marca de tentativa é gravada **antes** de tentar, para que uma
  falha no meio não vire laço.
- **Log legível** em `GET /wp-json/aquametria/v1/atualizador` (público, só o log).
  Gatilho manual: `/?aquametria_atualizar_sync=TOKEN&forcar=1`, com o mesmo token do Sync.

**`ferramentas/teste-atualizador-sync.php`** (novo) exercita tudo isso com WordPress e
Code Snippets falsos, **um processo por cenário** — a versão instalada é uma constante,
e constante não muda dentro do mesmo processo. **9 cenários, 0 falhas:**

| Cenário | O que tem de acontecer |
| --- | --- |
| feliz | grava inativo, ativa, verifica, marca o conteúdo, registra o sha aplicado |
| sha divergente | aborta sem gravar e sem sequer criar backup |
| sintaxe quebrada | aborta sem gravar |
| versão mentirosa | manifest anuncia 9.9.9, arquivo declara outra: aborta |
| verificação falha | **restaura o backup** e o site volta à 1.1.0 |
| loopback mudo | mantém o código novo e diz que a verificação foi inconclusiva |
| já atualizado | não reescreve nada |
| janela de 1 h | nem chega a baixar o manifest |
| Sync ausente | aborta — reescreve, não instala do zero |

### 3. Reaplicação das páginas que estão no ar com o YAML sujo

Feita **pelo próprio atualizador**, porque este container não alcança o site. Depois de
atualizar o Sync com sucesso, ele apaga o `sha256` registrado de cada item `conteudo:*`
em `aquametria_sync_estado` e zera a revisão — é isso que obriga a reaplicação, já que o
Sync pula arquivo cujo sha já foi aplicado — e agenda um evento avulso do sync para 60
segundos depois. Ele **não** roda o sync na mesma requisição: ali quem está carregado é
o conversor velho, que reescreveria o mesmo defeito. O teste confere que só os itens de
conteúdo perdem o sha (o de snippet fica) e que nada disso acontece quando houve
reversão.

### 4. Regra permanente (gravada em ESTADO.md, seção da fase 4b)

> **O snippet Sync não se atualiza sozinho, por desenho.** Toda correção no próprio Sync
> chega ao site pelo snippet atualizador, nunca por colagem manual do Raphael. Mexeu em
> `snippets/aquametria-sync.php`? Suba a versão no cabeçalho **e** o campo `versao` do
> item `aquametria-sync` no manifest — sem isso o atualizador não vê motivo para agir.

> **Depois de publicar qualquer página vinda de `conteudo/`, buscar a URL no ar e
> conferir que o corpo começa pelo TEXTO, não por metadado.** Nunca confie no "aplicado
> com sucesso" do log: em 08/09 o log estava certo e a página estava errada, e quem viu
> o defeito foi o Raphael, não a rotina.

O campo `versao` entrou no `esquema.snippets` do manifest, documentado.

### Verificação (o que foi realmente rodado)

- **`php -l` de verdade** nos 8 snippets, e `ferramentas/proteger-funcoes.php` devolvendo
  saída idêntica ao arquivo em todos — nenhuma função de nível superior desprotegida.
- **`teste-conversor-markdown.php`**: 17 casos, 0 falhas. As 9 páginas reais saem sem
  nenhum resíduo de YAML, e as 8 variações de front matter são cortadas.
- **`teste-atualizador-sync.php`**: 9 cenários, 0 falhas (tabela acima).
- **Simulação do Sync DO SITE aplicando a revisão 12**, com Code Snippets falso: ele se
  pula pelo nome, **cria o "Aquametria Sync — atualizador do Sync"** e o ativa, aplica os
  outros 6 snippets e as 9 páginas, e **todas as 9 páginas começam por `<p>` com texto de
  verdade**. É a prova de que o caminho de entrega funciona com a v1.1.0 que está no ar.
- **sha256 do manifest recalculado e conferido** contra os arquivos finais commitados:
  todos os itens, 0 divergências.

### Desembarque

Manifest na **revisão 12**. `WebFetch` em `aquametria.com.br` continua devolvendo
`EGRESS_BLOCKED` — este container só alcança o GitHub —, então **não consegui confirmar
a página no ar nesta sessão**. A sequência que o site executa sozinho, sem ninguém tocar
em nada:

1. o WP-Cron do Sync (a cada 30 min) vê a revisão 12 e **instala o atualizador**;
2. o cron do atualizador (de hora em hora, primeira volta ~3 min depois de ativado) vê
   a v1.1.4 no manifest contra a v1.1.0 instalada, grava, ativa, verifica e marca as
   páginas para reaplicação;
3. o evento avulso do Sync, 60 s depois, reaplica as 9 páginas **com o conversor novo**.

Para acionar na hora, na ordem:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ `https://aquametria.com.br/?aquametria_atualizar_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ o mesmo `?aquametria_sync=…&forcar=1` de novo.

**A CONFERIR (fica para a próxima execução, e é a primeira coisa a fazer):**
`https://aquametria.com.br/wp-json/aquametria/v1/status` tem de responder
`"versao_sync":"1.1.4"`; `https://aquametria.com.br/wp-json/aquametria/v1/atualizador`
mostra o log do atualizador; e o corpo de `/calculadora-de-litragem/`,
`/calculadora-de-vazao-do-filtro/`, `/calculadora-de-potencia-do-aquecedor/`,
`/calculadora-de-midia-filtrante/`, `/calculadora-de-iluminacao/` e
`/quantos-lumens-por-litro-aquario-plantado/` tem de começar pelo texto, não por
metadado.

**Próximo passo desbloqueado: C2 — peso do aquário cheio e carga no piso**, pareada com
o artigo dela, depois de conferir as URLs acima. As duas travessas continuam as mesmas:
a C2 não publica espessura de vidro nem veredito de "a laje aguenta" (falta tensão
admissível e coeficiente de segurança citáveis), e a carga de projeto da NBR 6120 está
no corpus como `norma-via-secundaria`, o que a tela precisa dizer com essas palavras.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-08 (3ª execução do dia) — CORREÇÃO CRÍTICA: as cinco calculadoras não calculavam

Fila normal de blocos interrompida. O Raphael abriu as páginas no navegador, com o
console aberto, e viu o que nenhum teste desta ilha via: **nenhuma das cinco
calculadoras publicadas funcionava**. A C2 fica para a próxima execução.

### Defeito 1 (o grave) — o WordPress escapava os `&&` e matava o script inteiro

Confirmado no repositório antes de mexer em qualquer coisa: os cinco snippets
montavam o `<style>` e o `<script>` **dentro** do valor que o shortcode devolve
(`$h .= '<script id="aquametria-c3-script">' . $js . '</script>';`). Tudo que volta
do shortcode ainda atravessa os filtros de texto do conteúdo, que trocam cada `&`
por `&#038;`. O primeiro `&&` do script virava `&#038;&#038;`, o navegador parava
com `SyntaxError` e a calculadora inteira morria: o formulário nunca calculava, os
contêineres `aqm-cN-saida` e `aqm-cN-produtos` ficavam com a classe `-oculto` — eles
nascem ocultos no HTML, quem os revela é o script — e **o bloco de produto com os
links de afiliado nunca aparecia**. Clicar em "Calcular" só fazia submit nativo do
formulário. A casca escapou porque já imprimia o CSS dela no `wp_head`.

**Correção, que passa a ser o padrão de toda calculadora futura:** o shortcode
devolve só o HTML. O estilo sai no `wp_head` (sem piscar sem estilo, com
`has_shortcode()` decidindo se a página usa) e o comportamento sai no `wp_footer`,
registrado pelo próprio shortcode quando ele roda. Ambos fora dos filtros de
conteúdo. Nenhuma linha de cálculo mudou — mudou o lugar de onde o script sai.
As cinco foram para a v1.1.0.

### Defeito 2 — slug que o hub publicava e que dava 404

`aquametria_casca_calculadoras()` trazia `'slug' => 'calculadora-de-aquecedor'` para
a C5, cuja página é `/calculadora-de-potencia-do-aquecedor/`. O slug certo só chegava
ao hub pelo filtro da própria C5; bastava ela não carregar para o hub publicar 404.
Corrigido o valor **e** a estrutura: a casca (v1.1.0) resolve o endereço de cada
página pelo `_aquametria_id` que o Sync grava — identidade canônica, que sobrevive
ao WordPress ter trocado o slug — e **só vira link se a página existir publicada**.
Sem página, sai o selo "Em construção" ou o rótulo sem link, nunca um 404.

Descoberta na mesma trilha: `wp_insert_post()` **renomeia `post_name` em silêncio**
quando o endereço já está ocupado (acrescenta `-2`), e o Sync respondia "ok" do
mesmo jeito — o log dizia uma coisa e o site tinha outra. Sync v1.1.5: cada página
aplicada devolve o permalink real, o slug divergente sai com ATENÇÃO no log e o
estado guarda `slug_ok:false`, que o endpoint de status publica.

### Defeito 3 — front matter

Do lado do repositório está resolvido e conferido: `teste-conversor-markdown.php`,
17 casos, 0 falhas, e as 9 páginas reais saem sem resíduo de YAML.
`teste-atualizador-sync.php`, 9 cenários, 0 falhas. **Não foi possível confirmar no
ar**: o `WebFetch` para `aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessão,
como nas anteriores. Fica como primeira conferência da próxima execução que
alcançar o site.

### Por que nenhum teste tinha pego isso — e o que mudou

`ferramentas/render-para-teste.php` mentia. Tratava `add_action` como no-op e não
aplicava o escape de `&`, então o script saía inline no HTML de teste e tudo passava
enquanto o site estava quebrado. Agora ele monta a página como o WordPress monta:
`wp_head`, conteúdo **já passado pelo escape de `&`**, `wp_footer`.

Três redes novas, todas com **controle negativo conferido** — reprovam o código
defeituoso e aprovam o corrigido:

- `ferramentas/teste-escape-shortcode.php` — 45 afirmações, 5 calculadoras. Com o
  `<script>` de volta dentro do retorno do shortcode, ele acusa **26 ocorrências de
  `&#038;`** na C1 e reprova.
- `ferramentas/teste-navegador-cinco.mjs` — executa o cálculo das cinco num Chromium
  de verdade: clica em Calcular, confere que a resposta sai do oculto, que há número
  na tela, que a página não recarregou (submit nativo era o sintoma) e que o bloco de
  produto traz link `sponsored` + `noopener` + `_blank` com aviso de comissão.
- `ferramentas/conferir-slugs.py` — compara front matter, manifest, constantes
  `AQUAMETRIA_C*_SLUG`, o catálogo do hub na casca e todo link de raiz escrito em
  snippet ou conteúdo. Devolvendo o slug errado à casca, ele acusa exatamente a linha
  do defeito 2.

### Verificação (o que foi realmente rodado)

- `php -l` nos 8 snippets e nas ferramentas PHP: 0 erros.
- `proteger-funcoes.php` nos 8 snippets: saída idêntica ao arquivo — nenhuma função
  de nível superior desprotegida.
- `teste-escape-shortcode.php`: 45 afirmações, 0 falhas. Controle negativo reprova.
- **`teste-navegador-cinco.mjs`: as cinco calculam em Chromium de verdade.** C1
  118 L; C3 180 a 1.000 L/h com 2 links de afiliado; C5 100 a 150 W com 1 link;
  C12 125 mL a 1,25 L com 2 links; C15 2.000 a 4.000 lúmens. Todo link com
  `rel="sponsored noopener"` e `target="_blank"`, e aviso de comissão no bloco.
- `teste-navegador-c5/c12/c15.mjs` (os de cada calculadora): passam. A única falha é
  "erro de console", que é a Google Fonts barrada pelo proxy do container
  (`ERR_CONNECTION_RESET`), não defeito da calculadora.
- `teste-conversor-markdown.php`: 17 casos, 0 falhas.
- `teste-atualizador-sync.php`: 9 cenários, 0 falhas. Ele tinha a versão `1.1.4`
  cravada e reprovava a cada correção do Sync; agora lê a versão do próprio snippet.
- `validar-produtos.py`: 26 produtos, 0 erros, 1 aviso já conhecido (V11, eheim-jager-200w).
- `conferir-slugs.py`: 9 slugs concordam, nenhum link publicado aponta para página
  inexistente. Controle negativo reprova.
- sha256 do manifest recalculado dos arquivos finais commitados.

Nota sobre a C15: ela responde **sem bloco de produto**, de propósito. As três
luminárias do catálogo estão barradas por não declararem lúmen ou voltagem, e a
página publica esse motivo. É a regra da ilha funcionando — resposta sem produto é
melhor que produto errado —, não defeito.

### Desembarque

Manifest na **revisão 13**. `WebFetch` em `aquametria.com.br` continua devolvendo
`EGRESS_BLOCKED`, então **o Sync não foi acionado por esta sessão e nada foi
conferido no ar**. A sequência que o site executa sozinho: o WP-Cron do Sync vê a
revisão 13, o atualizador leva o Sync à v1.1.5, e as calculadoras v1.1.0 e a casca
v1.1.0 entram pelos itens de snippet.

Para acionar na hora, na ordem:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ `https://aquametria.com.br/?aquametria_atualizar_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
→ o mesmo `?aquametria_sync=…&forcar=1` de novo.

**A CONFERIR no ar, e é a primeira coisa da próxima execução** — para cada uma das
cinco URLs (`/calculadora-de-litragem/`, `/calculadora-de-vazao-do-filtro/`,
`/calculadora-de-potencia-do-aquecedor/`, `/calculadora-de-midia-filtrante/`,
`/calculadora-de-iluminacao/`): HTTP 200, **zero `&#038;` no HTML**, corpo começando
pelo texto e não por metadado, e o `<script>` da calculadora vindo depois do
conteúdo. Mais `/wp-json/aquametria/v1/status` respondendo `"versao_sync":"1.1.5"`.

**Próximo passo desbloqueado: C2 — peso do aquário cheio e carga no piso**, pareada
com o artigo dela, depois de conferir as URLs acima. As travessas da C2 continuam as
mesmas: não publica espessura de vidro nem veredito de "a laje aguenta" (falta tensão
admissível e coeficiente de segurança citáveis), e a carga de projeto da NBR 6120
está no corpus como `norma-via-secundaria`, o que a tela precisa dizer com essas
palavras.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-08 (3ª execução do dia) — Correção cirúrgica: o fonte estava são, o site é que não recebeu

Disparo manual com correção dirigida. **O diagnóstico do pedido estava errado num
ponto decisivo, e vale registrar o porquê, porque é a diferença entre consertar e
quebrar.**

### O que o pedido dizia e o que era verdade

O pedido dizia que o arquivo `snippets/aquametria-calculadora-litragem.php` no
`main` continha 4 ocorrências literais de entidade dentro do JavaScript, copiadas
do HTML servido. **Não continha.** As 4 ocorrências estavam nos COMENTÁRIOS de PHP
que descrevem o defeito da manhã — texto de documentação, invisível para o
navegador. A correção da manhã (commit `78a1567`, 14h23 UTC) já havia limpado o
JavaScript.

A prova, medida nesta execução no código-fonte do `main`:

- `php ferramentas/render-para-teste.php` nas cinco calculadoras (o render que
  IMITA o escape de `&` do WordPress): **zero `&#038;` nas cinco**.
- `node --check` em cada bloco `<script>` renderizado: **as cinco passam**.
- `teste-navegador-cinco.mjs` em Chromium de verdade: **as cinco calculam**, sem
  `SyntaxError`, resposta sai do oculto, C3 com 2 links de afiliado, C5 com 1,
  C12 com 2, C15 sem produto de propósito. C1 118 L · C3 180 a 1.000 L/h · C5 100
  a 150 W · C12 125 mL a 1,25 L · C15 2.000 a 4.000 lúmens.

**A armadilha:** o pedido mandava trocar toda ocorrência de `&amp;`, `&lt;`,
`&gt;` e `&quot;` dentro de bloco de JavaScript pelo caractere. Executar isso ao
pé da letra teria destruído a função `esc()` das cinco calculadoras — a cadeia
`.replace(/&/g, '&amp;').replace(/</g, '&lt;')…` é código correto, e trocar
aquelas entidades pelo caractere transforma o escape de HTML em identidade. Foi o
que NÃO se fez.

### Então por que o Raphael viu o defeito às 15h02?

Porque o site está servindo o snippet ANTIGO. **O container da nuvem não alcança
`aquametria.com.br`** — desta vez a impossibilidade foi medida com duas
ferramentas independentes: `WebFetch` devolve `EGRESS_BLOCKED` e `curl` devolve
`CONNECT tunnel failed, response 403` no gateway de saída. Não é preferência de
ferramenta; é bloqueio de rede. Pelo mesmo motivo o front matter (`publicar:
true`) continua impresso no corpo das cinco páginas: o Sync do site ainda é a
v1.1.0, e a v1.1.5 que corta o front matter está no repositório desde as 13h31.

### O que esta execução entregou

1. **`ferramentas/conferir-entidades.mjs`** — o portão que faltava, com controle
   negativo conferido. Proíbe entidade NUMÉRICA em todo o fonte de `snippets/`
   (não há uso legítimo: texto acentuado vai em UTF-8 direto), proíbe entidade
   dentro de `<script>`/`<style>` renderizado com lista de exceção explícita para
   a cadeia de `esc()`, roda `node --check` em cada bloco de script sem engolir
   exceção, e confere que o script sai depois do conteúdo. Corrompendo um `&&`
   dentro de `aquametria_c1_js()`, ele reprova nos três níveis e reproduz o
   `SyntaxError` exato do console do Raphael.
2. **Comentários limpos nas cinco calculadoras.** As entidades escritas por
   extenso na documentação saíram e viraram palavras. Eram inofensivas para o PHP
   e péssimas para o diagnóstico: foi lendo um `grep` que acusava comentário que
   se concluiu que o fonte estava corrompido. Agora o `grep -rn -E '&#[0-9]+;'
   snippets/` devolve **zero**, e zero quer dizer alguma coisa.
3. **Casca v1.2.0 — apelidos de endereço.** `/calculadora-de-aquecedor-de-aquario/`
   (o endereço que o Raphael pediu e levou 404) e mais 21 apelidos plausíveis
   redirecionam **301** para a página canônica, e só quando ela existe publicada —
   trocar um 404 por outro seria pior. Com `ferramentas/teste-apelidos.php`, 59
   afirmações, controle negativo conferido.
4. **Regra permanente em `ESTADO.md`:** ao corrigir um snippet, o ponto de partida
   é SEMPRE o código-fonte do repositório, nunca o HTML servido pelo site nem uma
   cópia dele — o HTML servido pode conter entidades escapadas que, copiadas de
   volta para o fonte, corrompem o código de forma permanente e silenciosa. Junto,
   as duas travas que ela implica: entidade numérica é sempre corrupção, e
   busca-e-troca cega de entidade nomeada quebra o `esc()`.

Manifest na **revisão 14**.

### Verificação (o que foi realmente rodado)

`php -l` nos 9 arquivos PHP: 0 erros · `proteger-funcoes.php` nos 8 snippets:
nenhuma função de nível superior desprotegida · `conferir-entidades.mjs`: 0 falhas
· `teste-apelidos.php`: 59 afirmações, 0 falhas · `conferir-slugs.py`: 9 slugs
concordam · `teste-conversor-markdown.php`: 17 casos, 0 falhas ·
`teste-escape-shortcode.php`: todas passaram · `teste-atualizador-sync.php`: 9
cenários, 0 falhas · `validar-produtos.py`: 26 produtos, 0 erros, 1 aviso conhecido
· `teste-navegador-cinco.mjs`: as cinco calculam em Chromium · sha256 do manifest
recalculado dos arquivos finais.

### A VERIFICAÇÃO FINAL NÃO PÔDE SER FEITA — e isto não é sucesso

O pedido exigia medir, para cada uma das cinco URLs no ar: HTTP 200, contagem de
`&#038;` igual a zero, ausência de `publicar: true` no corpo, e `<script>` depois
do conteúdo. **Nenhum desses quatro números foi medido no ar, porque este
container não alcança o site.** Os números acima são do render local, que imita o
escape do WordPress — são a melhor evidência disponível daqui, e não substituem a
página servida. Marcar esta tarefa como concluída seria repetir exatamente o que
as três execuções anteriores fizeram.

### O que destrava, e é coisa de dez segundos no navegador do Raphael

Abrir, nesta ordem, esperando cada uma responder:

1. `https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
   — o Sync velho instala o snippet "Aquametria Sync — atualizador do Sync";
2. `https://aquametria.com.br/?aquametria_atualizar_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
   — o atualizador leva o Sync da v1.1.0 para a v1.1.5;
3. o mesmo endereço do passo 1 de novo — a v1.1.5 reaplica as cinco páginas sem
   front matter, os cinco snippets de calculadora e a casca v1.2.0.

Depois, `https://aquametria.com.br/wp-json/aquametria/v1/status` deve dizer
`"versao_sync":"1.1.5"` e `"revisao":14`. Sem isso, o site também se cura sozinho
pelo WP-Cron (Sync a cada 30 min, atualizador de hora em hora) na primeira visita
que a página receber — só que ninguém conferiu, e é essa a diferença.

**Próximo passo desbloqueado:** conferir as cinco URLs no ar (assim que houver
alcance ou assim que o Raphael acionar) e, com elas limpas, seguir para o **bloco
4 — C2, peso do aquário cheio e carga no piso**, pareada com o artigo dela. As
travessas da C2 continuam: não publica espessura de vidro nem veredito de "a laje
aguenta", e a carga de projeto da NBR 6120 entra rotulada como
`norma-via-secundaria`, com essas palavras na tela.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi
atualizado; esta entrada e o `ESTADO.md` são o registro.

## 2026-09-09 (1ª execução do dia) — BLOCO 4b, leva 1: o banco saiu de 26 para 36 produtos e a C3 dobrou de catálogo

Primeira execução da fila reordenada em 08/09: **o banco tem prioridade sobre calculadora
nova**, porque é ele que limita o tamanho legítimo do site e é ele que faz o bloco de produto
aparecer. Esta execução entregou a primeira leva da expansão.

### O que o diagnóstico da fila dizia e o que era verdade

A fila descrevia o banco com "15 produtos e 9 dos 13 equipamentos elétricos sem VOLTAGEM", e a
C5 com "0 de 4 sugeríveis". **Medido no `main` no começo desta execução: 26 produtos, e a
voltagem já estava fechada em todos menos um** (`chihiros-wrgb-ii-pro-60`). A C5 já sugeria 9
aquecedores, 3 deles com link. O item 4b(a) estava, na prática, concluído pelas execuções de
07 e 08/09 — o texto da fila é que ficou velho. Então esta execução foi direto para o 4b(b),
ampliar o catálogo, e para os campos que ainda barravam sugestão.

### Entregue

**Dez produtos novos, todos com ficha completa e fonte nomeada com data:**

| id | o que é | por que entrou |
|---|---|---|
| `atman-hf-0400` | hang-on, 440 L/h, 6,0 W, até 90 L | primeira opção do banco para 30 a 90 L |
| `atman-hf-0600` | hang-on, 650 L/h, 8 W, até 150 L | faixa de 100 a 150 L, que só tinha canister |
| `atman-hf-0800` | hang-on, 900 L/h, 8,3 W, até 250 L | alternativa barata ao canister de 250 L |
| `atman-at-3336` | canister CF-800, 800 L/h, 20 W, 1,8 m, 180 a 250 L | irmão menor do AT-3338 que já estava no banco |
| `sunsun-hw-603b` | mini canister, 400 L/h, 6 W, 2,3 L de mídia, até 80 L, coluna 0,85 m | **o item que faltava**: primeiro canister de verdade para aquário pequeno, e o primeiro filtro pequeno com volume útil de mídia — entra na C3 e na C12 |
| `sunsun-hw-302` | canister, 1000 L/h, 18 W, até 250 L | registro `parcial` de propósito: sem voltagem e sem coluna, NÃO é sugerido |
| `atman-at-100` | 100 W, quartzo, 20 a 34 °C, 25 cm, até 100 L | linha AT inteira faltava no banco |
| `atman-at-150` | 150 W, 27 cm, até 150 L | " |
| `atman-at-200` | 200 W, 30 cm (conflito: 32 cm), até 200 L | " |
| `atman-at-300` | 300 W, 37 cm, até 300 L | " |

**Um campo fechado que destravou um filtro inteiro:** o `sunsun-hw-303b` (1400 L/h, o de maior
vazão do banco) estava barrado da C3 desde 07/09 por não ter altura máxima de recalque. Nenhuma
loja brasileira publica esse número; o varejo especializado estrangeiro (PetzLifeWorld e Aqua
Nature) transcreve a etiqueta: **2,0 m de coluna e mangueira de 16 mm**. Com isso ele saiu de
`parcial` para `completo` e passou a ser sugerível.

**O que a expansão mudou, medido:**

- filtros: 5 → 11 registros; **catálogo embutido da C3: 5 → 10 filtros**
- aquecedores: 9 → 13 registros; **catálogo embutido da C5: 9 → 13**
- catálogo de filtros da C12 (os que declaram volume útil de mídia): 4 → 5
- banco inteiro: 26 → 36 produtos, 0 erro no validador, 1 aviso já conhecido (V11, eheim-jager-200w)

### O achado que mais importa para a Sentinela Estratégica

**Ampliar o catálogo REDUZIU, no curto prazo, o número de links de afiliado na tela.** Medido em
Chromium, no caso de 100 L comunitário, a C3 antes mostrava 3 cartões com 2 links (Eheim classic
250 e Seachem Tidal 55); agora mostra 5 cartões com 1 link, porque os produtos novos — sem link
ainda — se encaixam melhor tecnicamente e passam à frente do Tidal 55. Isso é a regra do projeto
funcionando exatamente como escrita (**ordem por adequação técnica, JAMAIS por comissão**), e é
também a prova de que a geração de link virou o gargalo da receita: **10 produtos entraram
esperando `afiliado.url`**, e quem gera é a Sentinela Estratégica, no painel da Shopee, até 10
por semana. Se ela gerar exatamente estes dez, cada faixa de volume passa a ter cartão com botão.

Prioridade sugerida para a próxima geração de links, por quanto tráfego a faixa recebe:
`atman-hf-0400`, `atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`,
`atman-at-200`, `atman-hf-0800`, `atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`.

### Dois testes que estavam errados, e o erro é instrutivo

O `teste-navegador-c5.mjs` afirmava `3 produtos na lista` e o `teste-navegador-c12.mjs`
afirmava `4 filtros na tabela`. **Números cravados que reprovavam a cada produto novo** — quer
dizer, testes que penalizavam o trabalho que a fila manda fazer. Os dois passaram a conferir o
que a regra realmente diz: a C5 exige **de 3 a 5 cartões** (a regra do bloco de produto) e a
C12 exige que a tabela **não murche e não repita linha** (ela publica todo filtro do banco que
declare volume útil de mídia, então cresce por desenho).

### Procedência: o que dá para sustentar e o que não dá

Toda ficha nova entrou como `transcrita-varejo`, com loja nomeada, URL e data. **Nenhum manual
de fabricante foi lido direto: o egresso da nuvem bloqueia `WebFetch` em todos os domínios
tentados** (aquametria.com.br, petzlifeworld.in), e só a busca funciona. Isso está escrito em
cada `fontes[]`, campo a campo, e a reconfirmação no manual fica registrada como coleta aberta.

Três coisas foram deliberadamente NÃO preenchidas, por falta de fonte:
- **voltagem do `sunsun-hw-302`** — nenhuma fonte vista publica. Fica `null`, e o filtro não é
  sugerido. Nunca chutar 110 nem 220: aparelho na tomada errada queima.
- **voltagem do `chihiros-wrgb-ii-pro-60`** — continua aberta; a busca não achou a fonte de
  alimentação declarada, e a C15 segue publicando essa luminária na lista de barradas com o motivo.
- **`volume_filtragem_L` dos hang-on e do AT-3336** — nenhuma fonte publica o volume útil do
  cesto, então eles servem à C3 e à C7, e não à C12.

Faixa de temperatura da linha Atman AT (20 a 34 °C): a escala aparece repetida modelo a modelo
nas fichas de varejo (AT-100, AT-150 e AT-300 conferidos), e está registrada como boilerplate de
lojista, não como manual — a reconfirmar.

### Verificação (o que foi realmente rodado)

`php -l` nos 8 snippets e nas 5 ferramentas PHP: 0 erros · `proteger-funcoes.php` nos 8
snippets: saída idêntica ao arquivo, nenhuma função de nível superior desprotegida ·
`conferir-entidades.mjs`: 0 falhas, zero entidade numérica no fonte, `node --check` passa nos 5
blocos de script, script depois do conteúdo nas 5 · `validar-produtos.py`: **36 produtos, 0
erros**, 1 aviso conhecido · `teste-navegador-cinco.mjs` em Chromium de verdade: **as cinco
calculam** — C1 118 L · C3 180 a 1.000 L/h com 5 cartões · C5 100 a 150 W com 5 cartões · C12
125 mL a 1,25 L · C15 2.000 a 4.000 lúmens sem bloco de produto, de propósito; todo link com
`rel="sponsored noopener"`, `target="_blank"` e aviso de comissão · `teste-navegador-c5.mjs` e
`teste-navegador-c12.mjs`: 1 falha cada, e é a mesma de sempre — Google Fonts barrada pelo proxy
do container (`ERR_CONNECTION_RESET`), não defeito da calculadora · `teste-escape-shortcode.php`,
`teste-conversor-markdown.php` (17 casos), `teste-atualizador-sync.php` (9 cenários),
`teste-apelidos.php` (59 afirmações) e `conferir-slugs.py` (9 slugs): 0 falhas · sha256 do
manifest recalculado de todos os arquivos finais commitados.

Manifest na **revisão 15**.

### Desembarque — e o que NÃO foi conferido

`WebFetch` em `https://aquametria.com.br/wp-json/aquametria/v1/status` devolveu
`EGRESS_BLOCKED` de novo, exatamente como em 07 e 08/09. **Então o Sync não foi acionado por
esta sessão e nada foi medido no ar.** O site se aplica sozinho pelo WP-Cron (Sync a cada 30
min); para acionar na hora:
`https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`.

Os três snippets que mudaram (C3, C5, C12) carregam só o catálogo embutido novo — nenhuma linha
de lógica foi tocada, e é por isso que os testes de navegador continuam sendo a evidência
relevante.

**Próximo passo desbloqueado: 4b, leva 2** — continuar a expansão rumo aos 60 itens, com três
alvos claros nesta ordem: (a) **iniciar o banco de espécies, item 4b(c)**, que é o que destrava o
eixo aberto "quantos litros para X peixes" e não depende de link de afiliado nenhum; (b) fechar
`fluxo_lm` do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` e a voltagem do Chihiros, os três
únicos itens que hoje barram a C15 — é a calculadora publicada com o catálogo mais fraco; (c)
mais filtros e aquecedores de marcas ainda ausentes (Ocean Tech, Hopar, Boyu, Sarlo Better),
com atenção às faixas de 200 a 400 L. Depois da leva 2 vem o **4c, o retrofit de visibilidade em
IA** nas cinco calculadoras publicadas.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi atualizado; esta
entrada e o `ESTADO.md` são o registro.

---

## 09/09/2026 — Bloco 4b(c): nasce o banco de espécies, e ele contradiz a regra de bolso do nicho

**Disparo automático das 05h10 (3ª execução do dia). Sessão SEM ferramenta de memória:** o estado
veio de `ESTADO.md`, `REGISTRO.md` e `README.md`, e o que iria para a memória está aqui.

### Ponto de partida medido

`git fetch origin main` primeiro, como manda a regra. `main` em `e70ffc0` (leva 1 do 4b, 36
produtos), branch `claude/lucid-carson-ayi8ca` no mesmo commit, nenhum PR aberto, nada pendente de
merge. O próximo passo que a leva 1 deixou escrito era **4b(c), iniciar o banco de espécies**, e foi
o que esta execução fez — bloco único, sem adiantar o (b) nem o (c) da fila de produtos.

### Por que espécie antes de mais produto

O item (a) da leva 2 estava certo em vir primeiro por um motivo que ficou mais claro construindo:
**espécie não depende de link de afiliado.** Os dez produtos que a leva 1 acrescentou estão parados
esperando a Sentinela Estratégica gerar link na Shopee; o banco de espécies não espera ninguém, e é
ele que destrava o eixo que a Bússola verificou ABERTO na SERP brasileira — "quantos litros para X
peixes" — enquanto "melhor filtro para aquário de X litros" já foi tomado por três fazendas de
conteúdo. Espécie é o multiplicador que não tem gargalo externo.

### Entregue

**Três arquivos novos, manifest na revisão 16:**

| arquivo | o que é |
|---|---|
| `dados/esquema-especies.json` | contrato formal da entidade `especie`: campos, unidades, vocabulário, escada de fontes, `dominio_por_campo` e as regras E1 a E14 |
| `dados/especies-agua-doce.json` | 12 espécies com ficha completa e fonte por campo |
| `ferramentas/validar-especies.py` | as regras E1 a E14 em código, mais o relatório de quem já passa em cada portão |

**As 12 espécies, escolhidas por serem as mais vendidas no varejo brasileiro e por cobrirem a faixa
útil de porte:** neon (*P. innesi*), cardinal (*P. axelrodi*), guppy (*P. reticulata*), platy
(*X. maculatus*), betta (*B. splendens*), coridora bronze (*C. aeneus*), paulistinha (*D. rerio*),
rasbora arlequim (*T. heteromorpha*), acará-bandeira (*P. scalare*), barbo-sumatra
(*P. tetrazona*), kinguio (*C. auratus*) e otocinclo (*O. vittatus*).

Faixa coberta: **de 2,2 cm (neon) a 48 cm (kinguio)**. Frentes mínimas declaradas: **45, 60, 80, 90
e 100 cm** — cinco degraus, o que já é malha suficiente para páginas de volume sem repetir número.

### Três decisões de modelagem que valem para sempre

**1. Não existe fabricante de peixe, então a escada é outra.** No banco de produtos o topo é o
manual do fabricante. Aqui o topo é base científica (FishBase) e compêndio de aquarismo (Seriously
Fish) — e as duas não competem: uma é melhor em biologia, a outra em manutenção. Por isso o esquema
tem a tabela **`dominio_por_campo`**: biologia (porte, família, distribuição) decide pela base
científica; manutenção (frente mínima, cardume, temperamento) decide pelo compêndio. Sem essa
tabela, "nível mais alto vence" daria à FishBase a última palavra sobre tamanho de aquário, que não
é o assunto dela.

**2. Em conflito de campo de BEM-ESTAR o conservador é o MAIOR — o oposto do banco de produtos,
e está escrito no esquema exatamente assim.** Errar espaço para menos custa a vida do animal; errar
para mais custa espaço. A regra E9 executa isso: conflito em `cardume_minimo`,
`comprimento_minimo_aquario_cm`, `base_minima_cm` ou `altura_minima_cm` cujo `valor_conservador` não
seja o maior dos valores é ERRO, não aviso.

**3. Litro não se grava.** A fonte declara frente e base em centímetros, nunca litro. O litro é
derivado pela calculadora, com a altura que a pessoa informar. A regra E7 detecta litro que bate com
`base × altura` para qualquer altura de 25 a 60 cm e reprova como derivado gravado à mão.

### O achado editorial: o banco contradiz a regra de bolso, com fonte

A regra brasileira de "1 cm de peixe por litro" não sobrevive a nenhum destes três registros, e é
por isso que eles entraram na leva 1:

- **Paulistinha:** 3,8 cm de peixe pedindo **90 × 30 cm de base** pelo compêndio. Nenhuma regra
  proporcional a comprimento chega nesse número, porque o que manda é velocidade de natação, não
  massa.
- **Acará-bandeira:** único registro com **altura mínima declarada, 50 cm**. Um aquário de 100 L em
  formato baixo não atende um adulto. Litro não descreve o problema; a fonte declara
  100 × 40 × 50 cm.
- **Coridora bronze:** peixe de fundo, o que limita é a **área da base (80 × 30 cm)**, não o volume.
  60 L em coluna alta não servem; 60 L espalhados servem.

Junte-se a eles o **betta**: a fonte de manutenção declara base de 45 × 30 cm para UM macho, e o
varejo brasileiro vende o peixe em pote de menos de 2 L. A ficha existe para publicar essa distância
com fonte e data ao lado, não para opinar.

E o **kinguio**, que é o registro deliberadamente incômodo: 48 cm de comprimento máximo, 100 cm de
frente mínima, 30 a 40 anos de vida, e a fonte de manutenção falando explicitamente em nanismo
severo quando o peixe é criado em aquário de 30 × 20 cm.

### Um caso que virou regra de segurança: temperatura que é tolerância

A FishBase publica **0 a 41 °C** para o kinguio. Isso é a faixa de TOLERÂNCIA da espécie na
natureza, não recomendação de manutenção — e alimentar a C5 com ela produziria dimensionamento de
aquecedor sem sentido. O esquema ganhou o campo `temperatura_e_tolerancia` e a **regra E13**: faixa
com amplitude maior que 20 °C sem esse campo marcado é ERRO. Com ele marcado, o registro sai do
`minimo_para_sugerir` da C5 automaticamente. Hoje o kinguio é o único registro nessa condição, e o
validador imprime isso na tela.

### Procedência: o que dá para sustentar, e o que não dá

**Nenhuma página foi lida direto.** O egresso da nuvem devolveu `EGRESS_BLOCKED` para
`fishbase.se`, `fishbase.org`, `seriouslyfish.com` e `en.wikipedia.org`, todos testados hoje — o
mesmo bloqueio de 07 e 08/09, agora confirmado também para as fontes de espécie. Só a busca
atravessa.

Por isso o esquema escreveu a **regra de atribuição por busca**, que é o que separa colher de
inventar: um número só entra pelos níveis 3 e 5 da escada quando a busca foi **restrita ao domínio
da fonte** (`allowed_domains`) ou quando o resumo atribui o número à fonte pelo nome. Número que
aparece em resumo de busca aberta, sem dono, **não entra no banco**. Foi assim que as 24 buscas
desta execução foram feitas, e está registrado campo a campo em cada `fontes[]`.

O limite dessa técnica apareceu no cardinal, e ficou publicado como conflito em vez de escondido:
**duas leituras da MESMA página da FishBase, no mesmo dia, devolveram 2,5 cm SL e 3,0 cm SL.** Não é
divergência entre autores — é o teto de colher número por resumo sem poder abrir a página. O banco
publica os dois e usa o maior, porque em lotação errar o porte para menos é o lado que lota demais.

### Quatro coisas deliberadamente NÃO preenchidas

- **`dificuldade`** — julgamento editorial, não fonte. Fica `null` na leva inteira, em vez de virar
  opinião com cara de dado.
- **`familia`** — nenhuma busca devolveu a família atribuída, e taxonomia sem fonte não entra.
- **`comportamento`** — só 5 dos 12 registros têm uma frase de fonte que sustente o campo (platy,
  paulistinha, betta, acará-bandeira e barbo-sumatra). Nos outros 7 fica `null`. Por isso o campo
  **não é obrigatório** e não entra no mínimo de sugestão: quem sustenta lotação é `convivencia`,
  não temperamento inventado.
- **`volume_minimo_declarado_L`** — nenhuma fonte declarou litro. Vide regra E7.

### O guppy é o achado que mais surpreendeu

**O peixe mais vendido do Brasil não tem ficha própria no compêndio de referência.** A busca
restrita ao `seriouslyfish.com` encontrou ficha de *P. wingei*, *P. sphenops*, *P. velifera* e
*P. latipinna* — de todas as irmãs — e nenhuma de *P. reticulata*. O registro ficou com **uma fonte
só**, e por isso é `parcial` e não passa no portão de página de espécie.

Isso gerou a **regra E14**: `status_registro` `completo` exige pelo menos **duas fontes de url
distinta**. Uma só leitura não se confere a si mesma, ainda mais num banco inteiro colhido por
busca. Fechar a segunda fonte do guppy é tarefa da próxima leva.

### Verificação (o que foi realmente rodado)

`python3 ferramentas/validar-especies.py`: **12 espécies, 0 erro, 0 aviso** · **12 testes negativos
com o banco deliberadamente corrompido**, um por regra, cada um conferido para reprovar com o código
certo: E1 (id fora do nome científico), E2 (obrigatório faltando), E3 (campo sem fonte), E4 (status
incoerente com a origem), E5 (varejo sustentando manutenção), E7 (litro derivado gravado à mão), E8
(min > max), E9 (conservador que não é o maior), E10 (conflito sem status), E12 (solitário com
cardume), E13 (tolerância disfarçada de recomendação) e E14 (completo com fonte única) — todos
saíram com código 1 e a mensagem correta, e o banco foi restaurado byte a byte depois · JSON dos três
arquivos relido e validado · `python3 ferramentas/validar-produtos.py`: **36 produtos, 0 erro**,
1 aviso já conhecido (V11, `eheim-jager-200w`) — o banco de produtos não foi tocado e continua são ·
sha256 recalculado dos três arquivos novos e gravado no manifest.

**Nenhum snippet foi alterado, nenhum arquivo mudou de `publicar: false` para `true`.** Este bloco é
de dados: as três entradas novas do manifest nascem com `publicar: false`, como todas as outras de
`dados/`. Logo **não houve desembarque, o Sync não foi acionado e nada foi medido no ar** — e não
havia o que medir, porque nenhuma página do site mudou. As cinco calculadoras publicadas continuam
exatamente como a execução anterior as deixou.

### Próximo passo desbloqueado

**4b, leva 3**, nesta ordem:

1. **Ampliar o banco de espécies para 25 a 30 registros**, agora que o contrato existe e o validador
   roda. Alvos que a leva 1 deixou de fora e o mercado brasileiro pede: molinésia, espada, colisa,
   mato-grosso, rodóstomo, tricogaster, apistograma, ancistrus (o cascudo que todo mundo compra sem
   saber o porte adulto) e camarão *Neocaridina*. Fechar junto a **segunda fonte do guppy** e a
   **família** dos 12 registros atuais.
2. **Fechar `fluxo_lm`** do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` e a **voltagem do Chihiros**
   — os três únicos itens que barram a C15, hoje a calculadora publicada com o catálogo mais fraco.
3. Mais filtros e aquecedores de marcas ausentes (Ocean Tech, Hopar, Boyu, Sarlo Better), com
   atenção às faixas de 200 a 400 L.

Depois da leva 3 vem o **4c, retrofit de visibilidade em IA** nas cinco calculadoras publicadas —
tabela de exemplos pré-renderizada, resposta antes da explicação, JSON-LD e procedência na frase.

**Para a Sentinela Estratégica:** continuam **10 produtos esperando `afiliado.url`**, na ordem que a
leva 1 sugeriu (`atman-hf-0400`, `atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`,
`atman-at-200`, `atman-hf-0800`, `atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`). Nada mudou
nisso hoje: espécie não tem link de afiliado, por desenho.

---

## 09/09/2026 — Bloco 4b leva 3: o banco de espécies vai a 25, e uma regra nova impede que espelho conte como conferência

**Disparo automático (4ª execução do dia). Sessão SEM ferramenta de memória:** o estado veio de
`ESTADO.md`, `REGISTRO.md` e `README.md`, e o que iria para a memória está aqui.

### Ponto de partida medido

`git fetch origin main` primeiro. `main` em `14e5df2` (leva 4b(c), 12 espécies), branch
`claude/lucid-carson-eze5qq` no mesmo commit, nenhum PR aberto, nada pendente de merge. O próximo
passo escrito pela execução anterior era **4b leva 3, item 1: ampliar o banco de espécies para 25 a
30 registros, fechar a família dos 12 e a segunda fonte do guppy**. Foi o que esta execução fez —
bloco único, sem adiantar produto nem retrofit.

### Entregue: 12 → 25 espécies, e família em todos os 25

**Treze registros novos**, escolhidos para cobrir o que faltava de porte e de frente mínima, não
para engordar contagem:

| espécie | porte | frente mínima | por que entrou |
|---|---|---|---|
| espada (*Xiphophorus hellerii*) | 16,0 cm TL ♀ | **120 cm** | o irmão do platy que pede o dobro de aquário |
| molinésia (*Poecilia sphenops*) | 12,0 cm SL ♀ | — | exige água DURA e alcalina (pH 7,5–8,2) |
| colisa (*Trichogaster lalius*) | 9,5 cm TL | 60 cm | os 60 cm são para UM CASAL, não para um macho |
| tricogaster (*Trichopodus trichopterus*) | 15,0 cm SL | 100 cm | o gurami grande do lote |
| mato-grosso (*Hyphessobrycon eques*) | 4,0 cm SL | **80 cm** | a própria base científica o classifica como agressivo |
| rodóstomo (*Hemigrammus rhodostomus*) | 5,0 cm TL | 90 cm | cardume de 10 e 26,5–29 °C: o mais exigente do banco |
| ramirezi (*Mikrogeophagus ramirezi*) | 4,2 cm SL | 60 cm | 27–30 °C com pH 5,0–6,0; território por casal |
| ancistrus (*Ancistrus cirrhosus*) | 8,9 cm SL | 60 cm | o cascudo que todo mundo compra sem saber o porte |
| tetra-negro (*Gymnocorymbus ternetzi*) | 7,5 cm SL | 75 cm | 20–26 °C, dispensa aquecedor em boa parte do BR |
| coridora-panda (*Corydoras panda*) | 3,8 cm SL | **45 cm** | o menor requisito do banco: sustenta a página de 30–40 L |
| botia-palhaço (*Chromobotia macracanthus*) | 30,5 cm TL | **180 cm** | vendido como filhote de 4 cm |
| tetra-brilhante (*Hemigrammus erythrozonus*) | 3,3 cm TL | 60 cm | o registro mais bem sustentado da leva |
| oscar (*Astronotus ocellatus*) | 45,7 cm TL | **150 cm** | 10 a 20 anos de vida; teto de porte do banco |

**Faixa coberta agora: 2,2 cm (neon) a 48 cm (kinguio), com 45,7 cm de porte declarado por fonte de
manutenção no oscar. Frentes mínimas declaradas: 45, 60, 75, 80, 90, 100, 120, 150 e 180 cm — nove
degraus.** Era isso que faltava para a malha de páginas de volume não repetir número: cada degrau é
uma página de "aquário de X" com espécie real por trás.

**Família fechada nos 12 registros da leva 1**, o campo que ficou `null` inteiro na leva passada por
falta de atribuição. Agora os 25 têm família com fonte e url.

### A regra nova, e o defeito que ela pegou em flagrante

Fechar a família do guppy trouxe a mesma ficha da FishBase pelo **outro domínio** — a leva 1 citou
`fishbase.org`, a coleta de hoje devolveu `fishbase.se`. Duas urls distintas. E a regra E14, escrita
na leva 1, dizia exatamente isto: *"completo exige pelo menos duas fontes com url distinta"*.

**O guppy teria passado de `parcial` a conferido sem ninguém ter conferido nada.** É o pior tipo de
defeito de dado: silencioso, plausível e auto-infligido por uma regra bem-intencionada.

Daí a **regra E15: espelho não confere espelho.** Antes de contar fontes distintas, o validador
colapsa os domínios que leem o mesmo corpo de conhecimento — `fishbase.se` e `fishbase.org` viram
`fishbase`. Registro com duas urls e um corpo só sai com aviso e **não conta como conferido**, nem no
E14 nem no `minimo_para_sugerir`. O guppy continua parcial, que é o que ele é: o peixe mais vendido
do Brasil segue sem ficha própria no compêndio de referência, e a segunda fonte dele tem de vir de
outro corpo — coleta ainda em aberto.

**Segunda mudança de esquema, menor: emenda ao E10.** Dois registros novos são ao mesmo tempo
incompletos e divergentes (a molinésia, sem frente mínima e com porte conflitante; o tricogaster, sem
convivência e com faixa térmica conflitante). O E10 exigia status `conflito`, o E2 exigia `parcial`,
e os dois não cabiam no mesmo campo. Completude e divergência são fatos **ortogonais**; como
`status_registro` carrega um campo só, vale o mais restritivo, e `parcial` é mais restritivo que
`conflito` porque barra a página. O E10 passou a aceitar `parcial` quando há campo obrigatório
faltando — sem esconder o conflito, que continua declarado em `conflitos[]`.

### Ferramenta nova: os testes negativos viraram código

A leva 1 fez 12 testes negativos **à mão** e descreveu o resultado no registro. Isso não sobrevive à
próxima sessão: ninguém re-roda o que não é um comando. Nasceu
`ferramentas/testar-validador-especies.py` — corrompe uma cópia do banco de propósito, **uma
corrupção por regra, E1 a E15**, roda o validador contra a cópia e exige que a regra certa reprove
com o código certo. No fim confere que o banco real não foi tocado. O validador passou a aceitar um
caminho no argv só para isso.

Resultado hoje: **15 testes, 15 pegaram o defeito, 0 falha.** Inclusive o E15, testado com a
corrupção exata que motivou a regra: trocar o compêndio por um espelho da base e ver se o registro
passa por conferido. Não passa.

### Cinco achados editoriais desta leva

1. **A espada contra o platy.** Dois vivíparos da mesma família, vendidos lado a lado na mesma loja:
   o compêndio pede 60 cm de frente para um e **120 cm** para o outro. Nenhuma regra de bolso de
   litro por centímetro de peixe produz esse par.
2. **O mato-grosso é agressivo segundo a própria base científica** — a seção de aquário da FishBase
   diz "aggressive" — e o compêndio pede 80 × 30 cm de base para um peixe de 4 cm. É vendido no
   Brasil como tetra pacífico de aquário comunitário.
3. **O botia-palhaço fecha o argumento do kinguio.** Vendido como filhote de 4 cm, chega a 30,5 cm, e
   as duas fontes só divergem sobre se o mínimo é 150 ou **180 cm** de frente. Nenhuma admite aquário
   de sala. É o par que sustenta a página "peixes que a loja vende e o aquário não comporta".
4. **A coridora-panda repete a lição da bronze em outra espécie:** o que limita peixe de fundo é a
   **área da base** (45 × 30 cm), não o volume. E sua faixa térmica, 20–25 °C, é mais fria que a do
   neon e a do cardinal — o trio que a loja vende junto não fecha em temperatura.
5. **O rodóstomo e o paulistinha não se encontram:** 26,5–29 °C contra 18–24 °C, sem sobreposição
   nenhuma. Com fonte dos dois lados, é a prova de que "comunitário" não é critério de convivência.

### A taxonomia está em revisão, e o banco publica o que a fonte publicou

Colhido hoje, o mesmo dia e a mesma base devolveram **famílias diferentes para peixes do mesmo
grupo**: os *Paracheirodon*, o *Gymnocorymbus ternetzi* e o *Hemigrammus erythrozonus* vieram como
**Acestrorhamphidae** (tetras americanos), enquanto o *Hyphessobrycon eques* e o *Hemigrammus
rhodostomus* vieram como **Characidae**. O banco não uniformiza: publica o que cada ficha publicou,
com url e data, e diz isso no campo `nota_taxonomia`.

Três registros já aparecem na fonte sob gênero novo — *Corydoras aeneus* como **Osteogaster aenea**,
*Corydoras panda* como **Hoplisoma panda** e *Hemigrammus rhodostomus* como **Petitella rhodostoma**.
O id do banco segue o nome com que o comércio brasileiro vende, e o nome novo entra em
`sinonimos_cientificos`: é assim que a busca do leitor casa com a ficha. **Consequência prática: este
banco envelhece por revisão taxonômica, não por preço** — e é por isso que o prazo de revalidação
dele é de 365 dias, e não dos 180 do banco de produtos.

### Quatro registros barrados, e por quê — nenhum número foi estimado

- **molinésia:** falta `comprimento_minimo_aquario_cm`. A ficha do compêndio tem a seção, nenhuma
  busca restrita devolveu o número, e frente de aquário não se estima.
- **tricogaster:** falta `convivencia`. Nenhuma fonte declara cardume, grupo, casal ou harém; o
  compêndio fala de territorialidade entre machos, que é outra coisa.
- **ancistrus:** falta `temperatura_C`. As faixas das espécies irmãs do gênero (*A. triradiatus*,
  *A. ranunculus*) apareceram na busca e **não foram copiadas**: parâmetro de água de espécie vizinha
  é chute com cara de dado. Some-se o limite taxonômico, maior: o compêndio publica o cascudo do
  comércio como *Ancistrus* sp. '3', espécie **ainda não descrita**, apenas comparada a *cirrhosus*.
- **guppy:** uma fonte só, agora por corpo e não por url (E15).

Também ficaram fora da leva, deliberadamente: o **camarão *Neocaridina davidi***, porque o compêndio
de referência não cobre invertebrado e o que a busca devolveu foi artigo científico, que não é nível
da escada; e o **acará-disco (*Symphysodon aequifasciatus*)**, porque nenhuma das duas fontes
devolveu frente mínima atribuída — entraria como registro barrado, e registro barrado não é entrega.

### Verificação (o que foi realmente rodado)

`python3 ferramentas/validar-especies.py`: **25 espécies, 0 erro, 1 aviso** — e o aviso é o E15 no
guppy, que é a regra funcionando, não defeito · `python3 ferramentas/testar-validador-especies.py`:
**15 testes negativos, 15 pegaram, 0 falha**, banco real conferido intacto no fim ·
`python3 ferramentas/validar-produtos.py`: **36 produtos, 0 erro**, 1 aviso já conhecido (V11,
`eheim-jager-200w`) — o banco de produtos não foi tocado · JSON dos três arquivos relido e validado ·
**sha256 de TODOS os itens do manifest reconferido contra o arquivo em disco, não só dos que
mudaram** — nenhum divergente.

**Nenhum snippet foi alterado, nenhum arquivo mudou de `publicar: false` para `true`.** Bloco de
dados: as entradas de `dados/` e `ferramentas/` nascem e continuam com `publicar: false`. Logo **não
houve desembarque, o Sync não foi acionado e nada foi medido no ar** — e não havia o que medir,
porque nenhuma página do site mudou. As cinco calculadoras publicadas continuam exatamente como a
execução anterior as deixou. Manifest na **revisão 17**.

### Próximo passo desbloqueado

**4c, o retrofit de visibilidade em IA nas cinco calculadoras publicadas** — é a próxima da fila e
agora está desbloqueada: a fila manda o 4c "logo após o 4b", e o banco já passou dos 25 registros de
espécie que a leva 3 pedia. Uma ou duas calculadoras por execução, com tabela de exemplos
pré-renderizada no HTML cobrindo 30/60/100/150/200/300 L, resposta-antes-da-explicação no topo,
JSON-LD (`WebApplication`) e procedência na própria frase, mais a verificação de sempre no navegador
e a contagem de `&#038;` **só dentro dos blocos `<script>`**. Sugestão de ordem: **C3 (vazão) e C5
(aquecedor) primeiro**, porque são as duas com bloco de produto e link no ar — é onde a citação por
IA encosta em receita.

Ficam para depois, na mesma prioridade em que estavam:
1. Restante do 4b(b): mais filtros e aquecedores das marcas ausentes (Ocean Tech, Hopar, Boyu, Sarlo
   Better), faixas de 200 a 400 L, e `fluxo_lm` do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` mais a
   voltagem do Chihiros — os três itens que barram a C15.
2. Fechar os quatro registros de espécie barrados e a segunda fonte do guppy, que agora exige **outro
   corpo**, não outro espelho.
3. Depois do 4c, a **malha de links** — e ela já tem dado por trás: nove degraus de frente mínima com
   espécie real, que é exatamente o que o portão de 3 itens de banco por página exige.

**Para a Sentinela Estratégica:** continuam **10 produtos esperando `afiliado.url`**
(`atman-hf-0400`, `atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`, `atman-at-200`,
`atman-hf-0800`, `atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`). Nada mudou nisso hoje: espécie
não tem link de afiliado, por desenho.

Sem ferramenta de memória nesta sessão: `/areas/projeto-aquametria.md` NÃO foi atualizado; esta
entrada e o `ESTADO.md` são o registro.

## 2026-09-09 — BLOCO 4c, leva 1: a C3 e a C5 passaram a servir RESPOSTA no HTML

Disparo extra das 10h25 BRT, a pedido do Raphael, para começar o 4c em vez de esperar a madrugada.
Sessão SEM ferramenta de memória: o estado foi lido de `ESTADO.md` e do `REGISTRO.md`, e é neles que
esta entrada fica. Manifest da **revisão 17 para a 18**.

### O defeito que a Sentinela mediu, dito sem eufemismo

Em 09/09 pela manhã a Sentinela Técnica abriu as treze páginas da ilha e contou **JSON-LD zero em 13
de 13**. Nenhum `WebApplication`, nenhum `Product`, nenhum `FAQPage`. A regra de primeira classe que o
Raphael fixou em 08/09 — ser recomendado pelas IAs vale tanto quanto ranquear no Google — não tinha
sido implementada em lugar nenhum.

E havia um defeito maior por baixo, que a regra do Raphael já nomeava: **todo o cálculo desta ilha é
JavaScript no navegador**, de propósito, porque o site está atrás do cache de página da hospedagem.
A consequência que ninguém tinha medido é que quem lê a página por HTTP sem executar script — um
crawler de IA, e também o visitante que não quer preencher formulário — recebia **um formulário
vazio**. Cinco calculadoras publicadas, nenhum número servido. Não havia o que citar.

### O que foi entregue, nas duas que já vendem

**C3, vazão do filtro** (`snippets/aquametria-calculadora-vazao.php`, v1.0.3 → **1.2.0**) e
**C5, potência do aquecedor** (`snippets/aquametria-calculadora-aquecedor.php`, v1.0.2 → **1.2.0**).
Foram escolhidas primeiro porque são as duas com bloco de produto e link de afiliado no ar: é onde a
citação por IA encosta em receita.

**(a) Resposta antes da explicação.** Um bloco novo, `aquametria_cN_resposta_direta_html()`, que sai
ANTES do formulário e diz o número, o critério e a procedência na mesma frase — porque um modelo cita
PASSAGEM, não página, e passagem sem fonte dentro dela não sobrevive ao recorte. A da C3 abre assim:

> Um aquário de 100 litros de água real, comunitário, pede um filtro de 180 a 1.000 L/h — de 1,76 a
> 10 renovações do volume por hora. O piso é o único extremo que vem de quem fabrica filtro: o Eheim
> classic 250 (2213) declara 440 L/h para aquários de até 250 litros, o que dá 1,76 renovações por
> hora (ficha coletada pela Aquametria em 07/09/2026).

A da C5 fecha com a frase que é a tese da página: **a pergunta que decide o número não é o volume do
aquário, é quanto o cômodo esfria na noite mais fria do ano.**

**(b) Tabela de exemplos pré-renderizada**, `aquametria_cN_exemplos_html()`, cobrindo 30, 60, 100,
150, 200 e 300 L, resolvida em PHP no servidor e servida no HTML. A C3 publica três colunas — faixa
comunitária, mira de carga média e faixa de plantado. A C5 publica os **dois cenários de frio**: até
10 °C de diferença, onde vale a ReefFlow, e acima disso, onde só sobram as regras sem condição
declarada — e ali a faixa vai marcada como **PISO**, com essas palavras, porque esticar o número da
ReefFlow para além dos 10 °C que ela declarou seria inventar constante.

**(c) JSON-LD**, `aquametria_cN_imprimir_jsonld()`, um bloco por página com `@graph` de dois nós:
`WebApplication` (com `applicationCategory`, `featureList` de 8 itens, `isAccessibleForFree`, `offers`
a preço zero, `softwareVersion` e `publisher`) e `FAQPage` com **8 perguntas em cada página** — seis
por volume, mais duas de método. Cada resposta carrega número e fonte, e cada uma existe, com o mesmo
número, na tabela servida: FAQPage que promete o que a página não mostra é lixo, e lixo detectável.

**Onde o JSON-LD sai importa tanto quanto o que ele diz.** Ele sai no `wp_head`, e nunca dentro do
retorno do shortcode, **pelo mesmo motivo que o script sai no `wp_footer` desde 08/09**: o retorno do
shortcode atravessa os filtros do `the_content`, que trocam cada `&` pela entidade numérica dele. Isso
matou o JavaScript das cinco calculadoras em 08/09 e quebraria o JSON exatamente do mesmo jeito.

### O conserto que o 4c obrigou, e que vale para as próximas levas

Pré-renderizar a tabela criou um perigo que não existia: **o mesmo número passando a viver em dois
lugares** — no JavaScript que calcula e no PHP que serve a tabela. Dois lugares divergem em silêncio,
e divergir aqui significaria a página contradizer a calculadora que está logo abaixo dela.

Então as constantes compartilhadas saíram do JavaScript e passaram a nascer no PHP, viajando para o
script como variável impressa no rodapé, do mesmo jeito que o catálogo de produtos já viajava:

| Antes (só no JS) | Agora (nasce no PHP) | Chega ao script como |
|---|---|---|
| bandas de turnover da C3 | `aquametria_c3_bandas()` | `AQM_C3_BANDAS` |
| regras de W/L da C5 | `aquametria_c5_regras()` | `AQM_C5_REGRAS` |
| linha comercial da C5 | `aquametria_c5_linha_comercial()` | `AQM_C5_LINHA` |

Para não errar na transcrição, o array PHP da C5 foi **gerado a partir do literal JavaScript
original**, e depois foi conferido que o JSON que o PHP emite é **idêntico** ao literal que estava lá.
Nenhuma fórmula mudou; mudou de onde os números vêm.

### Ferramenta nova nº 1: o teste que mede o que a Sentinela mediu

`ferramentas/teste-navegador-visibilidade-ia.mjs`. Abre a página num Chromium de verdade **com o
JavaScript DESLIGADO** — e é isso que faz o teste valer. Com script ligado, qualquer número na tela
pode ter sido desenhado pela calculadora; desligado, o que aparece é o que um crawler de IA recebe.

Confere, por calculadora: JSON-LD presente e fazendo parse; `WebApplication` com nome, categoria,
`featureList`, `isAccessibleForFree` e `publisher`; `FAQPage` com pelo menos seis perguntas, toda
resposta com texto, com número, e longa o bastante para ser citada; a tabela de exemplos existindo no
HTML servido e cobrindo os seis volumes; o bloco de resposta direta vindo ANTES do formulário, com
número e data de verificação. E uma asserção que fecha o círculo: **o número que a tabela servida dá
para 100 L tem de ser o mesmo que a calculadora devolve para 100 L.**

Confere também o inverso, que é fácil errar em nome do SEO: sem JavaScript, o contêiner de resultado
tem de continuar **oculto**. Número de resultado vazando para o HTML servido seria número sem
entrada — pior que formulário vazio, porque seria mentira em vez de silêncio.

### Ferramenta nova nº 2: a proteção das funções finalmente se confere

Existia só `ferramentas/proteger-funcoes.php`, que **reescreve** o arquivo. Ferramenta que reescreve
não serve como verificação antes do commit, e a regra do projeto pede a verificação. Nasceu
`ferramentas/conferir-protecao-funcoes.py`, que só confere e nomeia função e linha quando falha
(pulando docblock entre o guarda e a função, que era o falso positivo óbvio).

### Verificação — o que foi realmente rodado, com número

- `php -l` nos dois snippets: sem erro de sintaxe.
- `python3 ferramentas/conferir-protecao-funcoes.py snippets/*.php`: **8 snippets, 147 funções, todas
  dentro de `function_exists`**.
- `node ferramentas/teste-navegador-cinco.mjs`: **as CINCO calculadoras executadas em Chromium, tudo
  passou** — nenhum SyntaxError, resposta saindo do estado oculto, bloco de produto com link
  `sponsored`/`noopener`/`_blank` e aviso de comissão. A C3 devolveu **180 a 1.000 L/h** para 100 L
  comunitário e a C5 devolveu **100 a 150 W** para 100 L com alvo 26 °C e mínima 18 °C — que é
  exatamente o que as tabelas pré-renderizadas publicam para 100 L. A leva não quebrou a C1, a C12
  nem a C15.
- `node ferramentas/teste-navegador-visibilidade-ia.mjs`: **46 asserções, 46 passaram**, com o
  JavaScript desligado.
- Contagem de `&#038;` **extraindo só os blocos `<script>`**, que é o teste certo: **zero** nos dois
  snippets. O `&amp;` que aparece 1x é o da função `esc()` da própria calculadora, legítimo.
- JSON emitido pelo PHP conferido contra o literal JavaScript original: **idêntico** nos três casos
  (`AQM_C3_BANDAS`, `AQM_C5_REGRAS`, `AQM_C5_LINHA`).
- `python3 ferramentas/validar-produtos.py`: 36 produtos, 0 erro, 1 aviso conhecido (V11,
  `eheim-jager-200w`) · `python3 ferramentas/validar-especies.py`: 25 espécies, 0 erro, 1 aviso
  conhecido (E15, guppy). Nenhum dos dois bancos foi tocado hoje.
- **sha256 de TODOS os 48 itens do manifest reconferido contra o arquivo em disco**, não só dos que
  mudaram: nenhum divergente. Só dois snippets mudaram de hash, que são os dois esperados.

### NÃO CONCLUÍDO, e é preciso dizer com essas palavras

**O Sync não foi acionado e a revisão aplicada no site NÃO foi conferida.** O egresso desta sessão
para `aquametria.com.br` continua bloqueado pelo proxy da nuvem (`EGRESS_BLOCKED`), o mesmo bloqueio
registrado em 08/09. Então:

- o bloco está **commitado e no `main`**, que é onde ele conta como entregue pelo Passo 0;
- mas ele **não está confirmado no ar**. Não foi possível bater a revisão de
  `https://aquametria.com.br/wp-json/aquametria/v1/status` contra a **18** do manifest.

Isso é exatamente o cenário do Passo 0b: o desenho é PULL, o WP-Cron do WordPress só dispara quando
alguém VISITA o site, e site novo sem tráfego não tem cron. Em 09/09 de manhã o site estava **seis
revisões atrás** do repositório sem ninguém ter percebido. **Alguém precisa acionar o Sync**: abrir
`https://aquametria.com.br/?aquametria_sync=<chave>&forcar=1` (a chave está na memória e não entra
neste arquivo, que pode virar público) e, uns cinco minutos depois, conferir que
`/wp-json/aquametria/v1/status` diz revisão 18. A Sentinela Técnica das 11h30 roda no Chrome do
Raphael e alcança o site; esta sessão não alcança.

Enquanto isso não for feito, **o 4c está entregue no repositório e não está no ar.**

### Próximo passo desbloqueado

**4c, leva 2: C12 mídia filtrante e C15 iluminação**, com exatamente o mesmo desenho — resposta
direta, tabela pré-renderizada de 30 a 300 L, JSON-LD `WebApplication` + `FAQPage`, procedência na
frase, e toda constante que apareça nos dois lugares nascendo no PHP. Ao publicar, **acrescentar o
caso novo em `teste-navegador-visibilidade-ia.mjs`**: o teste é a única parte desta leva que
sobrevive à sessão.

Depois, **leva 3: C1 litragem e os três artigos-âncora** (nos artigos, `FAQPage`; e a `Organization`
com `sameAs` na home, que mora na casca e ainda não existe).

Continuam na fila, sem mudança: o resto do 4b (mais filtros e aquecedores de Ocean Tech, Hopar, Boyu e
Sarlo Better nas faixas de 200 a 400 L; `fluxo_lm` do `sunsun-ade-400c` e do `wfish-wf-h600-wrgb` e a
voltagem do Chihiros, os três que barram a C15; os quatro registros de espécie barrados e a segunda
fonte do guppy, que agora exige outro CORPO e não outro espelho); os dois ajustes menores do 4d
(categoria de verdade para os artigos, que hoje caem em `/category/uncategorized/`, e o subtítulo em
branco quando o bloco de produto da C15 sai vazio); e só depois a malha de links.

**Dois achados desta leva que valem para a fila do 4b, porque a tabela nova os tornou visíveis:**

1. **A partir de 300 L a faixa da C5 passa do maior degrau da linha de referência (300 W)**, e a
   resposta honesta passou a ser "mais de um aparelho" — que também é o mais seguro, por modo de
   falha do termostato. Está publicado na tabela, com essas palavras.
2. **O buraco de catálogo que a Sentinela apontou agora está escrito na página.** A 100 L o degrau
   comercial é 150 W, e nenhum dos aquecedores com link de afiliado do banco é de 150 W (são 100, 200
   e 300 W). A calculadora responde certo e não tem o que vender. É perda de venda direta, e reforça
   o 4b(c).

**Para a Sentinela Estratégica:** continuam **10 produtos esperando `afiliado.url`** — `atman-hf-0400`,
`atman-hf-0600`, `sunsun-hw-603b`, `atman-at-100`, `atman-at-150`, `atman-at-200`, `atman-hf-0800`,
`atman-at-3336`, `atman-at-300`, `sunsun-hw-303b`. Nada mudou nisso hoje: esta leva não tocou o banco.
O `atman-at-150` merece prioridade — é justamente o degrau de 150 W que falta na faixa de 100 L.

---

## 2026-09-09 — LOTE DE BANCO: 21 anúncios com link e IMAGEM, e o campo `imagem` nasce de verdade

Execução extraordinária, disparada com um lote colhido à mão no painel da Shopee às ~10h50 BRT:
21 produtos novos com link de afiliado, preço e foto, na mesma passada. O bloco 4c fica para a
próxima; este é o bloco do banco, e ele muda **o que as calculadoras têm para vender**.

### Ponto de partida medido

Antes deste lote: 36 produtos, 10 cotações, 12 links de afiliado, **zero imagens**. A C15
iluminação tinha **uma** luminária sugerível com link (Ista I-401 45 cm, 810 lm, que não cai em
faixa nenhuma útil) e a C5 tinha três aquecedores com link — 100, 200 e 300 W —, com a **janela de
110 a 150 W vazia**, que é justamente a que a Sentinela mediu num aquário de 108 L.

### Entregue

- **56 produtos** (era 36) e **31 cotações** (era 10). 21 links novos, 21 imagens novas.
- **Iluminação: 6 → 16 registros.** Entrou a linha Soma WRGB inteira (S-200 a S-1200, cobrindo de
  20 a 130 cm de aquário) e duas Chihiros A-Series (A901 e A451M).
- **Aquecedor: 13 → 23 registros.** 7 Maxxi, o RS-50, o Ocean Tech Warmer X-5 150 W e o Sicce
  Scuba Contactless 150 W. O Roxin Q3 50 W, que já era apto e estava **sem link**, ganhou link e
  imagem.
- **O campo `imagem` deixou de ser placeholder.** No esquema (versão 4 → 5) ele tem subcampos
  (`url`, `largura`, `altura`, `fonte`, `coletado_em`, `alt`, `motivo_sem_medida`), vocabulário de
  fonte e regras de tela. Está preenchido nos 21 do lote e **explicitamente `null`** nos outros,
  para a falta ser contável.
- **Duas regras novas no validador, e elas rodam:** `V19` (imagem exige https, fonte do
  vocabulário, data e `alt` de no mínimo 20 caracteres; imagem NUNCA aparece em `fontes[]`, porque
  é dado comercial) e `V20` (aviso: produto com link e sem foto — hoje são **10**, todos da coleta
  de 07 e 08/09).

### O que isso destravou, com número

| Calculadora | Sugeríveis COM link, antes | Depois |
|---|---|---|
| C5 aquecedor | 3 (100, 200, 300 W) | **5** — entra o **Ocean Tech Warmer X-5 150 W** e o **Roxin Q3 50 W** |
| C15 iluminação | 1 | **3** — entram a **Chihiros A901** (8.200 lm) e a **A451M** (3.500 lm) |

**A janela de 110 a 150 W fechou.** O Warmer X-5 150 W é o único do lote com os quatro campos que
a C5 exige (potência, volume declarado, faixa de ajuste e voltagem) — 20 a 34 °C, 29 cm, tubo de
quartzo, 110 e 220 V, tudo de varejo especializado (Aquaricamp, Aquaripesca, Barbusfish, Pet
Patão). O catálogo embutido na C5 foi de 13 para 14 itens e o de 150 W deixou de ser só Atman e
Eheim sem link.

### A regra das duas camadas de procedência, aplicada com consequência

O lote veio com potência, voltagem, volume e lúmen **declarados no anúncio**. Nada disso virou dado
técnico. O que entrou como técnico foi reconferido em varejo especializado, campo a campo — e a
diferença apareceu três vezes:

1. **Chihiros A451M:** o anúncio declara **3.850 lm**; a ficha de varejo declara **3.500 lm**. O
   banco publica 3.500 e guarda os 3.850 em `afiliado.observacao`, para a tela poder avisar.
2. **As 8 Soma ficaram `parcial` por um campo só: `fluxo_lm`.** Nem a marca nem as nove lojas
   brasileiras conferidas publicam lúmen de nenhum modelo da linha. Elas entram no banco com
   potência, tamanho de peça, cobertura declarada e bivolt — e a C15, que dimensiona por lm/L,
   **não sugere nenhuma**: aparecem na lista de barrados, com o motivo escrito.
3. **Voltagem: 9 dos 10 aquecedores novos ficaram com `voltagem: null`.** O varejo localizado
   publica a linha Maxxi e o RS-50 em 110 V, e parte dos anúncios com link abre 220 V. Voltagem
   errada queima o aparelho e nenhuma fonte de nível 2 a 5 confirma versão por versão, então a
   Aquametria não afirma nenhuma das duas. O Sicce Scuba Contactless 150 W tem a **melhor ficha do
   lote** (15 a 35 °C, 120 a 180 L, dupla proteção contra funcionamento a seco) e para exatamente
   nisso: um campo.

### Um conflito real, publicado em vez de resolvido na média

O Warmer X-5 150 W é vendido no Brasil com **três tetos diferentes de volume**: até 150 L, até
130 L e até 100 L. A ficha publica **o mais baixo (100 L)**, que é a única afirmação que as três
leituras sustentam, e `conflitos[]` guarda as três com atribuição — a tela mostra as três. Não
muda quem é sugerido (o critério da C5 é a janela de potência), muda o que a ficha diz.

### Dois defeitos de tela consertados antes de aparecerem

- O gerador da C5 imprimia `None a 100 L` quando o varejo declara teto sem piso ("até 100 L"), que
  é a forma dominante no Brasil. Agora imprime `até 100 L` (função `faixa_em_texto`).
- A C15 imprimiria `cobre 90 a 90 cm` para a Chihiros A901, porque o fabricante declara **um**
  comprimento e não uma faixa. Agora imprime `exatamente 90 cm` (função `cobertura`). Transformar
  peça de 90 cm em faixa mais larga seria inventar cobertura, então a A901 só é sugerida para
  aquário de 90 cm mesmo — e a A451M só para 45 cm.

### Verificação (o que foi realmente rodado)

- `python3 ferramentas/validar-produtos.py` → **56 produtos, 31 cotações, 0 erro, 12 avisos**
  (10 são o V20 novo — link sem foto; 1 é o V11 do Eheim 200 W, antigo; 1 era o V14 do Sicce, e o
  status foi corrigido para `completo`).
- `python3 ferramentas/gerar-catalogo-aquecedores.py` → 14 itens embutidos, 5 com link.
- `python3 ferramentas/gerar-catalogo-iluminacao.py` → 5 itens embutidos, 3 com link, 11 barrados
  com motivo.
- `php -l` nos dois snippets tocados → sem erro.
- `python3 ferramentas/conferir-protecao-funcoes.py` e `conferir-slugs.py` → ok.
- **Imagem NÃO pôde ser conferida por esta sessão:** `down-bs-br.img.susercontent.com` devolve
  `EGRESS_BLOCKED`, como todo domínio de loja. Por isso `largura` e `altura` estão `null` com
  motivo, e o cartão vai reservar o espaço por CSS (`aspect-ratio: 1/1` + `object-fit: contain`),
  que não salta o layout qualquer que seja a proporção real. **Quem consegue conferir se as 21
  fotos carregam é a Sentinela Técnica, que roda no Chrome.**

### Próximo passo desbloqueado

**Bloco 4e — a vitrine.** O banco agora tem foto, e é o que faltava para o cartão de produto
parecer comércio: rolagem horizontal com `scroll-snap`, cartão que é link de verdade, promessa
acima da dobra e barra fixa no celular. As 21 imagens só chegam ao visitante nesse bloco.

Depois dele, o **4c leva 2** (JSON-LD e tabela pré-renderizada na C12 e na C15), que era o próximo
antes deste lote.

**Para a Sentinela Estratégica**, em ordem de retorno:

1. **Lúmen da linha Soma** — 8 produtos com link e foto, todos barrados por um número que nenhuma
   loja brasileira publica. Se a Soma responder por e-mail ou se alguém fotografar a caixa,
   destravam 8 vendas de uma vez, cobrindo de 20 a 130 cm.
2. **Voltagem confirmada em ficha** dos 7 Maxxi, do RS-50 e do Sicce — 9 links parados por um
   campo.
3. **Imagem dos 10 antigos** (`eheim-classic-250-2213`, `seachem-tidal-55`, `roxin-ht-1300-q3-100w`,
   `-200w`, `-300w`, `chihiros-wrgb-ii-pro-60`, `ista-i-401-45`, `sunsun-ade-400c`,
   `seachem-matrix-1l`, `eheim-substrat-pro-1l`): já vendem, e vão para a vitrine sem foto.
4. Continuam **10 produtos esperando `afiliado.url`** — a lista da leva anterior não mudou.

### NÃO CONCLUÍDO — o Sync não foi acionado, e agora são DUAS revisões paradas

Esta sessão **não alcança o site**: `aquametria.com.br` devolve `EGRESS_BLOCKED` no proxy de saída,
tanto na URL do Sync quanto em `/wp-json/aquametria/v1/status`. Não foi possível acionar o
desembarque nem conferir a revisão aplicada, então **este bloco está entregue no `main` e não está
no ar** — exatamente como a revisão 18 da leva anterior.

**O repositório está na revisão 19. O site está pelo menos oito revisões atrás.** Alguém com
navegador precisa abrir a URL do Sync com `&forcar=1` (a chave está na memória e não entra neste
arquivo, que pode virar público) e, uns cinco minutos depois, conferir que
`/wp-json/aquametria/v1/status` diz **revisão 19**. A Sentinela Técnica das 11h30 roda no Chrome do
Raphael e alcança o site; esta sessão, não.

Enquanto isso não for feito, o que está no ar continua sem as 21 fotos, sem os 20 produtos novos,
sem o aquecedor de 150 W que fecha a janela da C5 e sem as duas Chihiros da C15.

## 2026-09-09 — Bloco 4c, leva 1b: a tabela pre-renderizada passou a dizer QUAL produto atende

Disparo encadeado, autorizado pelo Raphael para antecipar a entrega em um dia. O pedido do
disparo era executar o 4c na C3 e na C5. **Ao ler o `main` antes de trabalhar, o 4c dessas duas
ja estava entregue** na revisao 18 — JSON-LD, tabela pre-renderizada de 30 a 300 L, resposta antes
da explicacao e procedencia dentro da frase, tudo conferido em Chromium com o JavaScript
desligado. Refazer seria trabalho perdido.

O que NAO estava entregue era justamente o item novo do pedido: **a coluna com o produto que
atende cada faixa**. Foi esse o bloco desta execucao, e ele e a metade do 4e-B que cabe dentro do
4c — a pessoa passa a saber que sai dali com produto ANTES de preencher qualquer campo.

### O defeito que a coluna corrige, dito sem eufemismo

A tabela servida respondia ao leitor e **nao respondia ao comprador**. Quem chegava com "que
filtro comprar para 100 litros" via a faixa de L/h e nada mais: a recomendacao de produto so
existia depois de preencher o formulario inteiro e rolar ate o fim do resultado. No celular isso
e pior, porque o formulario ocupa a tela toda. E, para um modelo de linguagem, a pagina inteira
nao continha uma unica indicacao de compra citavel.

### Entregue, nas duas calculadoras

- **Uma coluna nova na tabela**, uma celula por volume. Cada celula traz o modelo, a
  especificacao QUE FEZ ELE ENTRAR ("650 L/h — 6,5 renovacoes/h nos 100 L"; "150 W — 110 ou
  220 V"), a procedencia e a data na mesma frase, e o link de loja quando existe
  (`rel="sponsored noopener"`, `target="_blank"`).
- **O criterio e o MESMO do script**, e isso e verificavel: a funcao `escolher()` do JavaScript
  ganhou espelho em PHP (`aquametria_c3_produtos_exemplo`, `aquametria_c5_produtos_exemplo`) —
  vazao dentro da faixa e ordem pela distancia ate o meio dela na C3; potencia dentro da faixa,
  com teto no degrau comercial, e ordem pela distancia ate o topo na C5. **Comissao nao ordena
  nada** (regra V16).
- **A linha do comprável, rotulada como o que e.** O modelo que atende melhor quase sempre e um
  que o banco ainda nao conseguiu link — hoje, 4 das 6 linhas da C3 e 5 das 6 da C5. Sem isso a
  tabela mostrava seis nomes que ninguem sabe onde comprar. Entao, quando o primeiro nao tem
  link, sai embaixo, escrito "Com link hoje, na mesma faixa", **o primeiro da mesma ordem** que
  tem. A ordem nao muda; muda o que a tela conta.
- **Bloco vazio nunca sai mudo.** A faixa de 30 L da C3 nao tem filtro nenhum no banco (o menor
  e de 400 L/h, e a faixa vai ate 300 L/h), e a celula escreve isso com os dois numeros. Silencio
  parece defeito.
- **Aviso de publicidade proprio, junto da tabela** — nao basta o do bloco de resultado, que so
  aparece depois do calculo e nao existe sem JavaScript. Diz a palavra comissao, diz que a ordem
  e por adequacao tecnica, diz por que nao publicamos preco e linka a pagina de divulgacao.
- **FAQPage ganhou as perguntas de COMPRA**, uma por volume: C3 de 8 para 13 perguntas, C5 de 8
  para 14. Cada resposta nomeia o mesmo modelo e o mesmo numero que a tabela serve — FAQPage que
  promete o que a pagina nao mostra e lixo detectavel.

### Tres ressalvas que a coluna obrigou a escrever, e que sao o conteudo

1. **A C5 nao filtra por voltagem nem por temperatura-alvo na tabela**, porque a tabela nao
   conhece nenhum dos dois — e sao exatamente as duas barreiras de seguranca do formulario
   (V18). Aquecedor na voltagem errada queima. Entao a celula publica a voltagem que a ficha
   declara, ou a frase de que ela nao esta confirmada, e o aviso abaixo da tabela diz em negrito
   para conferir a voltagem antes de comprar. Nao se chuta 110 nem 220.
2. **A linha de 300 L da C5 avisa que a faixa passa do maior degrau da linha de referencia** e
   que ali a resposta e mais de um aparelho — senao a ultima coluna contradiria a coluna ao lado,
   que ja dizia isso.
3. **Quando o volume declarado pelo fabricante e menor que o do exemplo, a celula diz.** Acontece
   hoje uma vez: o Seachem Tidal 55 e o unico filtro com link na faixa de 300 L, e a ficha dele
   declara ate 200 L. Ele entra pela vazao; a declaracao de volume nao cobre o caso, e quem le
   precisa saber disso antes de clicar.

### A correcao do campo `imagem` — dado bom que quase foi jogado fora

O disparo trouxe uma correcao, e ela estava certa: **nao conseguir BUSCAR um arquivo nao e
evidencia de que a URL esteja errada.** As 21 URLs de foto foram colhidas do painel de afiliados
da Shopee, no navegador do Raphael, em 09/09/2026. O que esta bloqueado e o egresso da nuvem, que
barra `down-bs-br.img.susercontent.com` como barra todo dominio de loja.

Conferido no `main`: **nenhuma imagem tinha sido anulada** — as 21 estao la, com `url`, `fonte`,
`coletado_em` e `alt`. O que faltava era o lugar de registrar a falta de conferencia sem mexer no
dado. Foi criado:

- `imagem.verificado_em` (null hoje) e `imagem.motivo_sem_verificacao`, no esquema (versao 5 → 6)
  e nos 21 registros, com o motivo escrito por extenso e nomeando quem consegue conferir: **a
  Sentinela Tecnica, que roda no Chrome.**
- **Regra V21 do validador**, para isto nao depender de ninguem lembrar: imagem sem
  `verificado_em` tem de dizer por que. Testada nos dois sentidos — com o motivo, 0 erro; sem o
  motivo, erro apontando o produto.
- A regra escrita no esquema, em uma frase, para a proxima sessao: **jogar fora dado bom por
  falta de meio de conferencia e a pior troca possivel.**

### Verificacao (o que foi realmente rodado, com numero)

- `php -l` nos dois snippets → sem erro. `conferir-protecao-funcoes.py` → 8 snippets, todas as
  funcoes dentro de `function_exists`. `conferir-slugs.py` → ok.
- `validar-produtos.py` → **56 produtos, 31 cotacoes, 0 erro, 11 avisos** (os mesmos 10 do V20,
  link sem foto, mais o V11 antigo do Eheim 200 W).
- `teste-navegador-visibilidade-ia.mjs`, em Chromium **com JavaScript DESLIGADO** → **tudo
  passou**, nos dois arquivos. O teste ganhou os casos deste bloco: uma celula de produto por
  volume, **nenhuma muda** (celula com menos de 20 caracteres reprova), todo link da tabela
  `sponsored` + `noopener` + aba nova e **com texto** (teclado e leitor de tela), e o aviso de
  comissao presente junto da tabela.
- `teste-navegador-cinco.mjs` (JavaScript LIGADO, as cinco calculadoras) → tudo passou, incluindo
  **zero `&#038;` no HTML servido** e os links de afiliado do bloco de resultado.
- `teste-navegador-c5.mjs` → **15 casos, todos passaram**, incluindo as duas barreiras de
  seguranca e o celular de 390 px **sem rolagem horizontal** com a tabela mais larga (ela rola
  dentro do proprio `-rolagem`, nao empurra a pagina).
- Dois consertos no proprio ferramental, para os testes nao mentirem:
  - o `teste-navegador-c5.mjs` procurava `.aqm-c5-aviso-afiliado` sem escopo e passou a achar
    DOIS elementos — quebrava por ambiguidade, nao por defeito. Agora confere os dois avisos, um
    por um, e diz qual e qual;
  - o caso "console limpo" reprovava por **13 falhas de rede**: o egresso da nuvem barra
    `fonts.googleapis.com` e `fonts.gstatic.com`, que a casca carrega de verdade e que carregam
    no navegador do Raphael. Falha de rede agora sai contada e nomeada a parte, e o caso mede o
    que ele existe para medir: **erro de script**. Um teste que reprova sempre treina a proxima
    sessao a ignorar o resultado dele, que e o pior estrago possivel.

### NAO CONCLUIDO — o Sync continua fora de alcance, e agora sao TRES revisoes paradas

`aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessao, tanto na URL do Sync quanto em
`/wp-json/aquametria/v1/status`. **Nao foi possivel acionar o desembarque nem conferir a revisao
aplicada.** Este bloco esta entregue no `main` e **nao esta no ar**, como as revisoes 18 e 19.

**O repositorio esta na revisao 20. O site estava na 11 na ultima medicao (08/09, 13h03).** Nove
revisoes de diferenca. O que esta no ar hoje nao tem: as 21 fotos, os 20 produtos novos, o
aquecedor de 150 W que fecha a janela da C5, as duas Chihiros da C15, o JSON-LD, a tabela
pre-renderizada e agora a coluna de produto.

Quem alcanca o site e a **Sentinela Tecnica das 11h30, que roda no Chrome do Raphael**. Basta
abrir a URL do Sync com `&forcar=1` (a chave esta na memoria e nao entra neste arquivo, que pode
virar publico) e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisao 20**.

### Proximo passo desbloqueado

**Bloco 4e — a vitrine**, agora com a metade B ja meio-caminho andada: a promessa antes do
formulario existe em forma de tabela com produto, e falta o resto — cartao com FOTO em rolagem
horizontal com `scroll-snap`, linha de promessa no topo, barra fixa no celular, e rolagem
automatica ate o resultado. As 21 imagens do banco so chegam ao visitante nesse bloco.

Depois dele, o **4c leva 2** (JSON-LD e tabela pre-renderizada na C12 e na C15) e o 4c leva 3
(C1 e os tres artigos).

**Para a Sentinela Estratégica**, sem mudanca desde a leva anterior: lumen da linha Soma (8
produtos com link e foto barrados por um numero), voltagem confirmada dos 7 Maxxi, do RS-50 e do
Sicce (9 links parados por um campo), imagem dos 10 antigos que ja vendem, e 10 produtos
esperando `afiliado.url`.

## 2026-09-09 (terceira execucao do dia) — A DUPLA CONDICAO: a C3 para de recomendar filtro que ela mesma diz que nao serve

Disparo manual do Raphael, com tres itens vistos por ele na C3 NO AR (aquario de 189,6 L,
plantado, carga media). Os tres foram feitos nesta execucao, antes da fila normal.

### Item 1 — o defeito grave, e ele era de credibilidade e nao de calculo

O primeiro produto recomendado era o **Atman HF-0600**, e o cartao dele escrevia, logo abaixo do
nome: "O fabricante declara que ele atende ate 150 L — o seu volume passa disso, e a declaracao do
fabricante nao cobre o seu caso." A pagina recomendava em PRIMEIRO lugar um filtro que ela mesma
dizia nao servir.

A causa era a que o Raphael suspeitou: a elegibilidade olhava so a VAZAO (650 L/h caem na faixa
334-948 L/h daquele aquario) e ignorava o volume atendido declarado pelo fabricante.

A regra nova esta escrita no esquema do banco como **V22** e implementada nos DOIS lados da C3, o
PHP que serve a tabela e o JavaScript que calcula na tela:

- entra nos recomendados so quem passa nas **duas** condicoes — vazao dentro da faixa **E** volume
  do visitante dentro do volume declarado pelo fabricante (o corte vale nas duas pontas: modelo
  declarado "a partir de 180 L" tambem nao cobre um aquario de 100 L);
- fabricante que **nao declara** volume entra, com a ressalva escrita no cartao;
- fabricante que declara e nao cobre **sai dos recomendados** e vai para uma secao SEPARADA,
  abaixo, rotulada "Atendem a vazao, mas o fabricante nao cobre esse volume". Nunca misturado,
  nunca em primeiro lugar. Some quando nao ha ninguem nela.

A funcao `aquametria_c3_volume_ressalva` mudou de assunto junto: como recomendado nao fura mais o
volume, o que sobra para ressalvar e o outro caso, o fabricante que nao declara volume nenhum.

### Item 2 — o topo da lista

A ordem passou a ter **tres degraus**: (1) elegibilidade tecnica dupla; (2) adequacao tecnica entre
os elegiveis, que e a distancia ate o meio da faixa; (3) so como DESEMPATE entre itens
**tecnicamente equivalentes**, quem tem link de loja aparece antes.

"Tecnicamente equivalente" precisava de um numero, senao o desempate come a ordem tecnica: dois
filtros sao equivalentes quando as distancias deles ate o meio da faixa caem no **mesmo decimo da
largura da faixa**. E convencao editorial da Aquametria, declarada na tela e no codigo, nao
constante de fabricante. A regra V16 do esquema foi reescrita para dizer exatamente isso e para
repetir o que continua proibido: taxa de comissao nao e comparada em lugar nenhum, produto pior
nunca sobe por pagar mais, e "produto sem link de loja aparece do mesmo jeito" continua valendo —
muda a POSICAO de quem ja era equivalente, nao a presenca de ninguem.

**Numero medido, e ele importa:** no caso exato do Raphael (189,6 L, PLANTADO) a faixa e estreita
(334 a 948 L/h, decimo de 61 L/h) e nenhum par de filtros cai no mesmo degrau — o desempate nao
dispara, e o topo continua sendo o Atman AT-3336, que ainda nao tem link. Isso nao e o desempate
falhando: e ele fazendo o que foi mandado fazer, que e nao passar na frente da adequacao tecnica.
O que resolve esse caso e link para o AT-3336, e isso e trabalho da Sentinela Estrategica. No mesmo
volume em perfil COMUNITARIO, onde a faixa vai a 1.896 L/h e cinco modelos caem no mesmo decimo, o
desempate dispara e o topo virou quatro itens com link (Eheim 2217 nas duas voltagens, Seachem
Tidal 55, SunSun HW-702B), com o Atman AT-3338 sem link caindo para quinto.

### Item 3 — o lote de filtro e midia colhido a mao no painel da Shopee

Entraram **8 filtros novos** com link e imagem, mais a imagem de 3 registros que ja vendiam
(Eheim classic 250, Seachem Tidal 55, Seachem Matrix 1 L) e **8 cotacoes** novas.

O que o lote virou depois de conferido contra a escada de fontes — e aqui esta a parte que importa,
porque as specs vieram do ANUNCIO e anuncio de marketplace (nivel 6) sustenta so existencia,
nomenclatura e preco, **nunca numero tecnico**. Cada numero abaixo foi reconferido em varejo BR
especializado por resultado de busca (nivel 5), que e o que o egresso da nuvem permite:

- **Eheim classic 600 (2217), 127 V e 220 V** — registros SEPARADOS, porque voltagem e chave de
  compatibilidade e cada anuncio vende uma versao so. 1000 L/h, 20 W, coluna de 2,25 m, ate 600 L,
  repetidos por AquaMaeda, Pro-Aquarista, Fazenda Submersa e AquaBetta; a voltagem de cada versao
  sai do titulo da loja BR que a vende. **Os dois entraram no catalogo da C3 como completos, com
  link E foto.** Sao os primeiros do banco a fechar a faixa acima de 200 L vendendo.
- **SunSun HW-702B 220 V** — 1000 L/h para ate 200 L (Pet Hobby), coluna de 1,4 m (Wiltec), UV de
  9 W (Pet Hobby e Aqua Mais), 220 V (Aqua Mais). **Entrou no catalogo da C3, com link e foto.**
- **Ocean Tech CT-1000-3** — 1000 L/h, 15 W, ate 200 L confirmados por quatro lojas BR. Ficou
  `parcial`: falta coluna maxima (o "1,4 m" das fichas e COMPRIMENTO DE CABO, nao recalque) e falta
  voltagem — o varejo vende o mesmo modelo em 110/127 V e em 220 V e nenhuma fonte diz qual versao
  este anuncio abre.
- **SunSun HW-702A** — mesma ficha do B, sem UV. `parcial` por UM campo: voltagem. O anuncio abre
  110 V, e isso ficou em `afiliado.voltagem_anuncio`, que e onde voltagem de anuncio mora.
- **SunSun XBL-600** — 500 L/h, 7 W, ate 150 L (Pet Hobby). `parcial` por UM campo: voltagem. As
  fichas dizem que sai em 110 V **ou** em 220 V e que NAO e bivolt, sem dizer qual e a deste
  anuncio. Chutar 110 ou 220 e proibido aqui, e queima aparelho.
- **Maxxi Pro MP-600** e **Aquaverso APK-600** — `parcial` com NENHUM numero tecnico. A busca nao
  achou ficha de fabricante nem de varejo especializado para nenhum dos dois; o que aparece com
  600 L/h na linha Maxxi e o hang-on HF-800, que e outro modelo, e a loja oficial da Aquaverso
  (lojaaquaverso.com.br) devolve EGRESS_BLOCKED. Os 600 L/h do titulo do anuncio ficaram onde
  valem, que e no anuncio. O campo `tipo` tambem ficou null nos dois: "mini canister de pendurar" e
  nomenclatura de anuncio, e `tipo` e campo tecnico aqui porque e ele que decide se a C3 cobra
  altura de coluna do modelo.

**Placar do lote: 3 de 8 ja vendem dentro do resultado da C3; 5 esperam UM ou DOIS campos** — 4
esperam so voltagem, 2 esperam vazao. Todos os 8 tem foto e link no banco.

Uma coisa que a lista de nomes tornou necessaria: com o Eheim 2217 no banco duas vezes, a tela
mostrava dois itens de nome identico. O nome de tela passa a carregar a voltagem quando o registro
declara uma so — "Eheim classic 600 (2217) (127 V)" —, no cartao, na tabela servida e no FAQ.

### Verificacao (o que foi realmente rodado, com numero)

- `php -l` no snippet da C3 → sem erro. `conferir-protecao-funcoes.py` → sai 0, todas as funcoes
  novas (`aquametria_c3_cobre_volume`, `_degrau_adequacao`, `_ordenar`, `_produtos_fora_do_volume`,
  `_fora_do_volume_frase`, `_nome_produto`) dentro de `function_exists`. `conferir-slugs.py` → ok.
- `validar-produtos.py` → **64 produtos, 39 cotacoes, 0 erro, 9 avisos**. Os erros que apareceram na
  primeira passada foram consertados no dado, nao afrouxando a regra: o HW-702B saiu de `completo`
  para `parcial` (potencia_w e obrigatorio da entidade e ficou null porque a unica ficha que a
  publica diz 24 W no titulo e 15 W na descricao, e somar 15 W de bomba com 9 W de UV para chegar
  aos 24 seria derivacao nossa), e o MP-600 e o APK-600 perderam o `tipo`, que nenhuma fonte
  acima de anuncio sustentava. O aviso V14 do XBL-600 fica de proposito: falta voltagem, que nao
  esta na lista de obrigatorios da entidade mas esta no minimo da C3, e a observacao do registro
  diz isso com essas palavras.
- `gerar-catalogo-filtros.py` → **13 filtros no catalogo da C3** (eram 10), 6 com link (eram 3).
- **`teste-navegador-c3-dupla-condicao.mjs`, arquivo NOVO** → 16 casos, todos passaram, em Chromium
  de verdade, executando o caso do Raphael. Ele confere o que este bloco promete: nenhum recomendado
  com volume declarado que nao cubra o aquario, o HF-0600 fora dos recomendados e dentro da secao
  separada, a secao rotulada e ABAIXO no HTML, o desempate por link so entre itens do mesmo degrau,
  e todo botao de loja `sponsored` + `noopener` + aba nova com texto. Duas decisoes de desenho do
  teste, e as duas existem para ele nao mentir: (a) ele roda um SEGUNDO caso, o mesmo volume em
  perfil comunitario, porque no plantado a faixa e estreita demais para dois filtros cairem no mesmo
  degrau e o desempate nunca dispararia — teste que nao exercita a regra nao prova a regra; (b) ele
  casa cada linha da tela com a ficha do catalogo embutido e **reprova quando nao acha**, em vez de
  filtrar os orfaos e passar em silencio (foi exatamente o que quase aconteceu quando o nome de tela
  ganhou a voltagem).
- `teste-navegador-visibilidade-ia.mjs`, em Chromium **com JavaScript DESLIGADO** → tudo passou nos
  dois arquivos, incluindo as 6 celulas de produto da tabela servida e os 6 links `sponsored`.
- `teste-navegador-cinco.mjs` (JavaScript ligado, as cinco calculadoras) → tudo passou.

### NAO CONCLUIDO — o Sync continua fora de alcance, e agora sao QUATRO revisoes paradas

`aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessao, tanto na URL do Sync com `&forcar=1`
quanto em `/wp-json/aquametria/v1/status`. **Nao foi possivel acionar o desembarque nem conferir a
revisao aplicada.** Este bloco esta entregue no `main` e **nao esta no ar**, como as revisoes 18,
19 e 20.

**O repositorio esta na revisao 21. O site estava na 11 na ultima medicao (08/09, 13h03).** Dez
revisoes de diferenca. O que esta no ar hoje NAO tem: a dupla condicao (ou seja, **a C3 no ar
continua recomendando em primeiro lugar o Atman HF-0600 para o aquario de 189,6 L do Raphael**),
o desempate por link, as 24 fotos, os 28 produtos novos, o aquecedor de 150 W que fecha a janela
da C5, as duas Chihiros da C15, o JSON-LD e a tabela pre-renderizada.

Quem alcanca o site e a **Sentinela Tecnica das 11h30, que roda no Chrome do Raphael**. Basta abrir
a URL do Sync com `&forcar=1` (a chave esta na memoria e nao entra neste arquivo, que pode virar
publico) e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisao 21**.

### Proximo passo desbloqueado

O Raphael disse "nao adiante o proximo bloco — eu disparo em seguida". O que estava na fila
continua sendo o **4e, a vitrine**: cartao com FOTO em rolagem horizontal com `scroll-snap`, linha
de promessa no topo, barra fixa no celular e rolagem automatica ate o resultado. As 24 imagens do
banco (21 da leva anterior mais 3 desta) so chegam ao visitante nesse bloco — hoje elas existem no
dado e nao aparecem na tela.

**Para a Sentinela Estrategica**, a fila de link cresceu e mudou de forma. O que trava venda hoje,
em ordem de dano: (1) **voltagem** de 4 registros novos que ja tem link E foto e nao podem ser
sugeridos por causa de um campo — HW-702A, XBL-600 e CT-1000-3 (que tambem precisa da coluna) —,
mais os 9 antigos na mesma situacao; (2) **link para o Atman AT-3336**, que e o primeiro
recomendado do caso real do Raphael e nao tem onde comprar; (3) vazao com fonte para o MP-600 e o
APK-600; (4) lumen da linha Soma, imagem dos que vendem sem foto.

---

## 2026-09-09 (redisparo das 12h) — BLOCO 4d: a casca no celular ganha menu, e o site ganha ícone próprio

**Antes de mais nada, sobre a execução que falhou.** O disparo das 12h20 (sessão
`cse_01R1msCiPtLH1iFvqdgmUfLT`) morreu às 12h26 sem empurrar nada, e esta execução
**não achou rastro do que a matou**: não há branch `claude/*` divergente, não há PR
aberto e o `main` estava intacto na revisão 21 — ou seja, ela morreu antes de commitar
qualquer coisa, e não deixou trabalho pela metade para recuperar. Não sei a causa e não
vou inventar uma. O que ficou de aprendizado prático desta execução, e que pode ser a
causa: o bloco 4e inteiro (vitrine em quatro calculadoras + promessa + barra fixa +
rolagem) é grande demais para uma execução; o payload do redisparo mandou entregar em
partes, e foi o que foi feito.

**Entregue: os dois itens de casca do bloco 4d, no mesmo snippet, como pedido.**
Manifest revisão **22**, casca na versão **1.3.0**.

### (1) Menu hambúrguer no celular

Abaixo de 782 px — a mesma quebra que o próprio WordPress usa para decidir que a tela
virou celular — o menu vira sanfona atrás de um botão. Acima disso nada muda: é a mesma
fileira de links de sempre.

**A decisão que governa o resto, e que é de indexação, não de layout:** os três links
saem **sempre** no HTML servido, dentro de `<nav>`, e o botão não gera link nenhum — ele
só mostra e esconde o que já está lá. Quem esconde a lista no celular é o seletor
`.aqm-nav-caixa[data-aqm-menu]`, e esse atributo quem põe é o JavaScript do rodapé.
**Sem JavaScript o atributo não existe, a regra de CSS não casa e o menu não some**:
volta a ser a lista visível que o site tinha antes desta versão. Esconder por padrão e
contar com o script para revelar teria trocado um defeito de celular por um defeito de
visibilidade em IA — que é regra de primeira classe do projeto desde 08/09.

O que o botão carrega: `aria-expanded` que muda de verdade, `aria-controls` apontando
para o id do `<nav>` (id **contado**, porque o filtro `render_block` pode trocar mais de
um bloco `core/navigation` na mesma página e `aria-controls` para id repetido não
controla nada), fecho no **Escape** com o foco devolvido ao botão, fecho no clique fora,
e reset ao alargar a janela — sem esse último o `aria-expanded` continuaria dizendo
"aberto" para o leitor de tela depois de o menu já ter virado fileira.

O script sai no **`wp_footer`**, nunca dentro do retorno de shortcode. É a regra que
nasceu do defeito de 08/09/2026, e ela vale para a casca do mesmo jeito que vale para
calculadora.

### (2) Ícone próprio do site

`remove_action( 'wp_head', 'wp_site_icon', 99 )` tira o ícone que o WordPress imprime
sozinho — sem isso o site sairia com dois e o navegador escolheria o errado. No lugar
entram três, todos como data URI dentro do snippet, **nada sobe para a biblioteca de
mídia**: o SVG da aba (`rel="icon" type="image/svg+xml"`, 464 bytes), um PNG de 32 px
como `alternate icon` para quem não desenha SVG na aba (186 bytes), e o
`apple-touch-icon` de 180 px para o iOS (3.238 bytes), mais `theme-color` na tinta da
marca.

O desenho é o mesmo do logotipo: o recipiente graduado com a linha de enchimento, em
tinta #0D1B22 e lâmina #0E7C8C. Sem peixe, sem bolha, sem wordmark — a 16 px o wordmark
vira borrão e o que sobrevive é o recipiente.

Duas decisões de desenho, cada uma com motivo: **o SVG da aba tem canto arredondado e o
PNG do iOS não tem**, porque o iOS aplica a própria máscara e canto arredondado por baixo
de máscara vira borda dupla; e o PNG passa por redução de paleta para 64 cores, o que o
levou de 9.124 para 3.238 bytes sem mudar nada do que se vê — o desenho tem três cores, e
o PNG truecolor estava carregando milhares de tons de borda que viravam 12 KB de base64
dentro do snippet.

**`ferramentas/gerar-favicon.php`, arquivo novo:** o desenho não se edita à mão no
snippet. Ele é gerado entre os marcadores `FAVICON-INICIO` e `FAVICON-FIM`, pelo mesmo
motivo que o catálogo de produtos é gerado dentro das calculadoras — desenho mantido em
dois lugares diverge em silêncio.

### O ferramental que este bloco obrigou a criar

Nenhum teste do projeto olhava para o **cabeçalho**: o `render-para-teste.php` monta
página de calculadora, cujo corpo é o retorno de um shortcode, e o cabeçalho da
Aquametria não vem de shortcode nenhum — vem do filtro `render_block`. Então nasceram:

- **`ferramentas/render-casca-para-teste.php`**, que monta a página como o tema de blocos
  monta: `wp_head`, o cabeçalho vindo do filtro, o conteúdo (esse sim passando pelo
  escape de `&` dos filtros de conteúdo) e `wp_footer`.
- **`ferramentas/teste-navegador-casca.mjs`**, **31 asserções, todas passaram** em
  Chromium de verdade: HTML servido (três `<a href>` dentro do `<nav>`, `aria-controls`,
  zero `&#038;` dentro de `<script>`), desktop a 1100 px (botão escondido, três links
  visíveis), celular a 390 px (abre, fecha no Escape com foco devolvido, abre no Enter,
  Tab chega ao primeiro link **com endereço de verdade**, clique fora fecha, alargar
  reseta o `aria-expanded`), **celular com o JavaScript DESLIGADO** (os três links
  continuam visíveis e o botão não aparece) e os ícones medidos por `naturalWidth`: SVG
  desenha, PNG do iOS tem 180×180, alternativo tem 32×32, e o ícone do WordPress sumiu do
  `wp_head`.
- Três acréscimos ao `render-para-teste.php`, todos compatíveis com o que já existia:
  `apply_filters` passou a repassar argumentos extras (o `render_block` recebe dois),
  `get_posts` passou a consultar um mapa `__paginas` (vazio por padrão — sem ele a casca
  serve `<span>` em vez de `<a>`, de propósito, e o teste estaria conferindo o caso
  errado), e nasceram `remove_action` de verdade mais um `wp_site_icon` de mentira
  registrado no `wp_head` na prioridade do core: é ele que permite **provar** que a casca
  tirou o ícone do WordPress de lá.

### Verificação (o que foi realmente rodado)

- `php -l` nos três arquivos novos/alterados → sem erro.
- `conferir-protecao-funcoes.py` nos 8 snippets → **sai 0**, 22 funções da casca dentro
  de `function_exists`.
- `teste-navegador-casca.mjs` → **31 de 31**.
- `teste-navegador-cinco.mjs` (as cinco calculadoras, JavaScript ligado) → tudo passou.
- `teste-navegador-visibilidade-ia.mjs` (JavaScript desligado) → tudo passou.
- `teste-apelidos.php` → 59 afirmações, 0 falha. `conferir-slugs.py` → ok.
- sha256 do manifest conferido contra os arquivos: **0 divergentes**.
- Inspeção visual em Chromium a 390 px e a 1100 px: o menu aberto e o cabeçalho de
  desktop foram fotografados e olhados, não só medidos.

### NÃO CONCLUÍDO — o Sync continua fora de alcance, e agora são CINCO revisões paradas

`aquametria.com.br` devolve `EGRESS_BLOCKED` nesta sessão, tanto na URL do Sync com
`&forcar=1` quanto em `/wp-json/aquametria/v1/status`. **Não foi possível acionar o
desembarque nem conferir a revisão aplicada.** Este bloco está entregue no `main` e
**não está no ar**, como as revisões 18, 19, 20 e 21.

**O repositório está na revisão 22. O site estava na 11 na última medição (08/09,
13h03).** Quem alcança o site é a **Sentinela Técnica das 11h30, que roda no Chrome do
Raphael**: basta abrir a URL do Sync com `&forcar=1` e, uns cinco minutos depois,
conferir que `/wp-json/aquametria/v1/status` diz **revisão 22**.

### Próximo passo desbloqueado

**BLOCO 4e — A VITRINE**, inteiro, e ele é grande: cartão de produto com foto em rolagem
horizontal com `scroll-snap` (sem biblioteca, cartão que é `<a>` de verdade), linha de
promessa acima do formulário, barra fixa no rodapé do celular enquanto o resultado está
fora da tela, e rolagem automática até o resultado com `scroll-margin-top`. As 24 imagens
do banco só chegam ao visitante nesse bloco. **Se não couber numa execução, entregar por
calculadora** — começando pela C3, que é a que tem mais itens com foto e link (6 de 13).

## 2026-09-09 — Reorganizacao do Arquipelago aplicada (execucao excepcional, sem bloco da fila)

- Disparo excepcional: a fila de blocos da Aquametria ficou parada de proposito.
  Nenhum snippet foi tocado, nada foi publicado e o Sync **nao** foi acionado.
- O Arquipelago deixou de ter uma Fundacao por ilha e passou a ter **uma
  Fundacao com despachante**, que escolhe a ilha mais atrasada a cada execucao:
  - criado o `ARQUIPELAGO.md` na raiz, contrato comum a todas as ilhas;
  - criado o `ilhas/aquametria/PROMPT.md`, com o que e so desta ilha
    (identidade, endpoints, quem verifica, memoria e fila de blocos);
  - acrescentado ao topo do `ESTADO.md` desta ilha o cabecalho YAML que o
    despachante le (`estado: viva`, `prioridade: 2`,
    `ultima_execucao: 2026-09-09T16:00Z`, `bloco_atual: "4c"`), sem tirar
    nenhuma linha do que ja existia;
  - criada a segunda ilha, `ilhas/robometria/`, com pastas, `manifest.json` na
    revisao 0, `README.md`, `PROMPT.md`, `ESTADO.md` e `REGISTRO.md`;
  - criado o modelo de ilha nova em `ilhas/_modelo/`;
  - o `README.md` da raiz ganhou a secao que explica a estrutura nova.
- **Proximo passo da Aquametria: sem mudanca — continua o bloco 4c**, retrofit
  de visibilidade em IA, na ordem C3 e C5, depois C12 e C15, depois C1 e os
  artigos. A partir de agora a fila desta ilha mora em
  `ilhas/aquametria/PROMPT.md`, e as regras comuns no `ARQUIPELAGO.md` da raiz.

## 2026-09-09 — Fila reordenada pela meta de trafego organico (execucao excepcional, sem bloco da fila)

- Decisao do Raphael em 09/09/2026: a Aquametria so conta como completa quando
  estiver **entrando trafego organico** — pagina indexada, aparecendo em busca e
  recebendo visita. Nao e numero de calculadora publicada e nao e a primeira venda.
- A fila de `ilhas/aquametria/PROMPT.md` foi reescrita por essa meta: T1 medir a
  indexacao, T2 limpar o que atrapalha a indexacao, T3 banco de dados (especies
  primeiro), T4 malha de paginas, T5 artigos-ancora, T6 prospeccao do widget,
  T7 schema e visibilidade em IA, T8 vitrine de produto. C2, C7 e C8 saem da fila
  por ora — ferramenta nova nao traz trafego enquanto as que existem nao estiverem
  indexadas.
- Execucao excepcional: nenhum snippet foi tocado, nada foi publicado, o Sync
  **nao** foi acionado e nenhum arquivo da Robometria ou o `ARQUIPELAGO.md` foi
  alterado. O cabecalho do `PROMPT.md` (identidade, endpoints, quem verifica,
  memoria) ficou intacto.
- **Proximo passo: bloco T1** — medir a indexacao no Search Console e gravar a
  primeira secao de `dados/indexacao.md`.

## 2026-09-09 (mutirão, bloco 1 de N) — T3(a): o banco de espécies vai a 36, e duas recusas viram conteúdo

**Bloco entregue: T3(a), banco de espécies, leva 3.** 25 → **36 registros**, manifest na
**revisão 23**. Validador `validar-especies.py`: **0 erro**, 1 aviso antigo (o espelho do guppy).

### O que entrou

| id | porte | temperatura | frente mínima | status |
|---|---|---|---|---|
| `hyphessobrycon-amandae` (tetra ember) | 2,0 cm SL | 24–28 °C | — | parcial |
| `danio-margaritatus` (rasbora galáxia) | 2,1 cm SL | — | — | parcial |
| `tanichthys-albonubes` (peixe-neve) | 4,0 cm TL | 18–22 °C | 60 cm | parcial |
| `corydoras-paleatus` (coridora pimenta) | 6,6 cm SL | 18–23 °C | 61 cm | conflito |
| `nannostomus-beckfordi` (peixe-lápis) | 6,5 cm SL | 24–26 °C | 60 cm | parcial |
| `corydoras-sterbai` | 6,8 cm SL | 21–25 °C | 45 cm | **completo** |
| `melanotaenia-boesemani` (arco-íris) | 9,0 cm SL | 27–30 °C | 120 cm | conflito |
| `trichopodus-leerii` (gurami pérola) | 12,0 cm TL | 24–28 °C | 120 cm | parcial |
| `symphysodon-aequifasciatus` (acará-disco) | 13,7 cm SL | 26–30 °C | 120 cm | parcial |
| `pethia-conchonius` (barbo rosado) | 14,0 cm TL | 18–22 °C | 80 cm | parcial |
| `trichogaster-chuna` (gurami mel) | **recusado** | 22–28 °C | 60 cm | parcial |

Quem passa no portão de página de espécie subiu de **21 para 24**; a C8 (lotação) de 22 para 28;
a C5 de 23 para 33. A faixa de porte agora vai de 2,0 a 48,0 cm e as frentes mínimas declaradas
ganharam um décimo degrau (45 cm), que é o menor do banco.

### As duas recusas, que são o conteúdo mais valioso desta leva

**1. O porte do gurami mel foi RECUSADO por implausibilidade.** A busca restrita à FishBase
devolveu **13,7 cm TL em duas formulações independentes** — e 13,7 cm é o mesmo número que a
mesma busca tinha acabado de devolver para o acará-disco. O comércio brasileiro vende o gurami
mel a 4–5 cm, e a **própria ficha se contradiz** ao recomendar aquário mínimo de 60 cm para um
peixe que teria 13,7 cm. `porte_adulto_cm` ficou `null` com o motivo escrito no registro.
**Precedente que este bloco fixa: número atribuído que contradiz a própria ficha não entra só
porque tem dono.** A regra de atribuição do esquema garante que colher não é inventar; ela não
garante que a colheita esteja certa, e é por isso que a plausibilidade continua sendo trabalho
de quem grava.

**2. O `Poecilia wingei` (guppy endler) ficou de FORA**, e o motivo foi gravado no campo novo
`especies_recusadas[]` do banco: a busca devolveu porte, família e distribuição, mas nenhuma
faixa de temperatura e nenhum tamanho mínimo de aquário, em três formulações. Sem temperatura o
registro não serve nem à página de espécie nem à C5 — sobraria uma ficha que só repete o nome.

E uma terceira recusa, menor: a temperatura da rasbora galáxia. Os 22–24 °C que a busca devolveu
são a temperatura **do hábitat medida no campo**, e a fonte diz isso com essas palavras. Hábitat
não é faixa de manutenção; publicar um como o outro seria trocar uma medida por outra.

### Divergência publicada, não resolvida na média

Dois conflitos novos, os dois em campo de bem-estar, os dois resolvidos pelo MAIOR (regra própria
deste banco, oposta à do banco de produtos):

- **`melanotaenia-boesemani`, frente mínima: FishBase diz 80 cm, Seriously Fish diz 120 cm.** 50%
  de diferença, e não é arredondamento. Vale 120. São **120 cm de frente para um peixe de 9 cm** —
  a maior exigência já registrada aqui em relação ao porte, e o exemplo mais limpo de por que
  "1 cm de peixe por litro" não dimensiona nada. Cardume: 5 (FishBase) contra 6 (Seriously Fish) →
  vale 6; o "de preferência mais" da fonte não é número e não foi gravado.
- **`corydoras-paleatus`, frente mínima: 60 contra 61 cm** — este é só o arredondamento das 24
  polegadas, e o registro diz isso em vez de esconder a diferença.

### O que a coleta ensinou sobre o canal

O egresso continua fechado: `fishbase.se`, `fishbase.org`, `seriouslyfish.com` e
`en.wikipedia.org` devolveram **EGRESS_BLOCKED** de novo em 09/09/2026, e o mesmo vale para
`aquametria.com.br`. Toda coleta desta leva saiu de **busca restrita ao domínio**, níveis 3 e 5
da escada. O que mudou é que agora existe um caso documentado de a busca restrita devolver número
errado com atribuição certa — e é por isso que a nota de procedência do arquivo continua dizendo
que a leitura direta é uma coleta em aberto, não um capricho.

Três espécies novas ficaram em UM corpo de fonte só (`symphysodon-aequifasciatus`,
`pethia-conchonius`, `nannostomus-beckfordi`): a busca restrita ao Seriously Fish devolveu a ficha
mas nenhum número dela, e o número das congêneres do gênero foi **recusado** — número de outra
espécie não é fonte, ainda que o resumo da busca o ofereça de bandeja.

## 2026-09-09 (mutirão, bloco 2) — T3(a2): a C15 ganha quatro luminárias, e o buraco de lúmen é confirmado como estrutural

**Bloco entregue: T3(a2), catálogo de iluminação.** Banco de produtos de 64 para **68 registros**,
`produtos-iluminacao.json` de 16 para **20**, C15 de **5 para 9 luminárias aptas**, snippet da C15
na **1.1.1** (só o catálogo embutido mudou; nenhuma linha de cálculo foi tocada), manifest na
**revisão 24**. Validador de produtos: **0 erro**.

### O que entrou, e por que foi a Chihiros A-Series

| id | W | lm | lm/W | aquário |
|---|---:|---:|---:|---|
| `chihiros-a-series-a301` | 18 | 2.800 | 155,6 | 30 cm |
| `chihiros-a-series-a361` | 21 | 3.450 | 164,3 | 36 cm |
| `chihiros-a-series-a601` | 39 | 5.800 | 148,7 | 60 cm |
| `chihiros-a-series-a801` | 50 | 7.200 | 144,0 | 80 cm |

Não entrou por ser marca boa: entrou porque é **a única linha do catálogo que declara fluxo
luminoso em toda a escada de tamanhos**, e fluxo é exatamente o campo que barra a C15. Os quatro
números foram colhidos por busca atribuída ao fabricante e **reconferidos numa segunda formulação
independente**, que devolveu os mesmos valores; a eficácia dos quatro cai entre 144 e 164 lm/W,
uma família coerente com a A451M (130 lm/W, marinha, mais azul) e a A901 (149 lm/W) que já
estavam no banco. Os quatro entram **sem `afiliado.url`** — quem gera link é a Sentinela
Estratégica —, com `plataforma: null` e o motivo escrito, e ficam `parcial` por um campo só:
`disponibilidade_br`, que só varejo brasileiro sustenta e não foi conferido para estes tamanhos.
A A1201 (120 cm) foi tentada e **não entrou**: a busca devolveu a dimensão da peça e não devolveu
o fluxo. Registro sem o campo que a calculadora exige não é ganho de catálogo, é ruído.

### O buraco de lúmen da C15 é ESTRUTURAL, e agora está medido duas vezes

As oito luminárias Soma cobrem de 20 a 130 cm, **todas com link de afiliado e voltagem fechada**,
e continuam barradas por um campo só: `fluxo_lm`. A coleta de 09/09 já tinha registrado que nem a
marca nem nove lojas brasileiras publicam lúmen; **esta execução reconferiu por busca
independente e confirmou**: as fichas de varejo declaram watt, comprimento, contagem de LEDs por
cor, espessura, peso e comprimento do fio — e nenhuma declara lúmen. O anúncio da Shopee também
não. Junte a SunSun ADE-400c e a WFish WF-H600 e são **dez luminárias barradas pelo mesmo campo**.

Isto não é falha de coleta, é um fato do mercado: **a C15 dimensiona por lm/L, e o meio do mercado
brasileiro não publica lm.** Enquanto isso valer, ampliar o catálogo de iluminação com marca
brasileira não aumenta a receita da C15 em nada — os produtos entram e ficam na lista de
barrados. As saídas possíveis, nenhuma delas decidida aqui: (a) importar marca que declara fluxo,
que foi o que este bloco fez; (b) a C15 passar a aceitar um segundo caminho de dimensionamento
com fonte (PPFD declarado a distância declarada, que o esquema já prevê); (c) medição própria,
que hoje não existe. **Estimar lúmen a partir do watt continua proibido** — seria inventar
constante, e a eficácia medida no próprio banco varia de 89,6 a 164,3 lm/W, quase o dobro.

### T3(b), voltagem: duas tentativas, nenhum número, e é assim que tem de ser

- **Chihiros WRGB II Pro 60** (tem link de afiliado, cobre 60 a 80 cm): busca restrita ao domínio
  do fabricante em três formulações não devolveu a tensão de entrada da fonte. `voltagem`
  continua `null` e o produto continua barrado.
- **Sicce Scuba Contactless 150 W** — o aquecedor da ficha mais completa do banco, e justamente o
  que cairia na janela de 110 a 150 W que a Sentinela mediu vazia a 108 L: a busca restrita a
  `sicce.com` devolveu a faixa de ajuste (15 a 35 °C), a linha de 50 a 400 W e o modo de economia,
  e **não devolveu a tensão**. Continua `null`.

Somados aos sete registros Maxxi (cujo anúncio declara a tensão, mas anúncio de marketplace é
nível 6 e **nunca** sustenta campo técnico) e ao RS-50 sem marca, são **dez elétricos com
`voltagem: null`**, cada um com o motivo no registro. Nenhum foi chutado. A regra "nunca chute 110
nem 220" custou dez produtos neste banco, e continua certa: aquecedor ligado na tensão errada
queima, e a Aquametria não tem como pedir desculpa depois.

## 2026-09-09 (mutirão, bloco 3) — T3(c): a cobertura de faixa deixou de ser opinião e virou medida

**Bloco entregue: T3(c), catálogo geral — mas com o critério novo.** O Raphael descartou a meta
de "60 produtos" hoje; o critério passou a ser **cobertura**: nenhuma faixa que as calculadoras
conseguem produzir pode sair com menos de 3 produtos elegíveis (seção 14.3 do `ARQUIPELAGO.md`).
Este bloco construiu o instrumento que mede isso e publicou a primeira medição. Manifest na
**revisão 25**.

### `ferramentas/varrer-cobertura.mjs`, arquivo novo

Ele **não reimplementa regra de seleção nenhuma**, e essa é a decisão que importa. Reescrever a
seleção de produto em Python criaria uma segunda cópia da regra, que divergiria da calculadora em
silêncio — exatamente o defeito que os geradores de catálogo existem para impedir. Em vez disso a
calculadora **de verdade** roda num Chromium de verdade, é preenchida ponto a ponto ao longo da
faixa de entrada declarada, em cada combinação de condição que a tela oferece, e o que se conta é
o cartão que apareceu. 87 faixas medidas em 486 pontos.

### A primeira medição, em `dados/cobertura-de-faixa.md` (arquivo histórico, nunca sobrescrito)

| | faixas | vazias | com 1 ou 2 | cumprem |
|---|---:|---:|---:|---:|
| **total** | 87 | 18 | 28 | 41 |

E o detalhe é mais duro que o total:

- **A C15 não cumpre o critério em NENHUMA das 22 faixas.** O melhor resultado em toda a escada de
  30 a 120 cm é **duas** luminárias; oito faixas saem vazias. Acima de 80 cm não há nada, em
  nenhum nível de exigência. Não é tamanho de catálogo: são 20 luminárias e 11 barradas pelo
  mesmo campo.
- **A C5 fica sem nenhum aquecedor de 310 a 400 L**, nas quatro combinações de delta e tomada — o
  banco não tem aparelho acima de 300 W. E entrega dois (um abaixo do piso) de 30 a 50 L e de 210
  a 300 L.
- **Descoberta lateral da C5:** trocar a tomada de 110 para 220 V **não muda uma linha sequer**.
  Todos os aquecedores aptos declaram as duas tensões, então a barreira de voltagem hoje não
  elimina ninguém — ela só elimina os dez registros que estão com `voltagem: null`. A barreira de
  segurança está certa e continua; o que ela custa hoje é catálogo, não sugestão.
- **A C3 tem um buraco na ENTRADA: de 20 a 40 L não há filtro nenhum**, nos três perfis
  comunitários. É o aquário de começo, que é justamente por onde mais gente chega pela busca. No
  perfil plantado o buraco vai até 170 L, porque a dupla condição corta mais fundo.
- **A C12 cumpre em toda a faixa, mas exatamente no piso:** 3 mídias de 20 a 400 L nos três
  perfis. Não é folga — qualquer mídia que saia do banco derruba a calculadora abaixo do critério.

### A lista de compras que estes números determinam

1. Luminária com fluxo declarado **acima de 80 cm** (C15 vazia em toda a faixa alta).
2. Aquecedor **acima de 300 W** (C5 vazia de 310 a 400 L).
3. Filtro de **baixa vazão, 150 a 400 L/h**, para 20 a 40 L (C3 vazia na entrada).
4. Luminária com fluxo declarado de **30 a 55 cm** para exigência alta.
5. Aquecedor de **250 W** e um segundo de **25 a 50 W**.
6. Uma **quarta mídia biológica**, para a C12 sair do piso.

Isto substitui qualquer meta de número redondo: o banco não precisa de 60 itens, precisa destes
seis buracos fechados. Um produto que não fecha nenhuma faixa descoberta não é prioridade, por
melhor que seja a comissão.

### Um teste que estava vermelho antes deste mutirão

`teste-navegador-c15.mjs` fixava em **3** o número de luminárias barradas. O lote de anúncios de
09/09 tinha levado esse número a **11** (as oito Soma, mais SunSun, WFish e Chihiros), e a
asserção ficou vermelha sem que nada tivesse quebrado — a contagem já era 11 **antes** de este
bloco tocar em qualquer coisa. Número de catálogo não é contrato de tela: o que a tela promete é
que **toda** barrada aparece com o motivo. A asserção passou a conferir isso, e o comentário no
teste registra o porquê. É a mesma correção que a C5 já tinha recebido na contagem de cartões, e
vale como regra: **teste que fixa tamanho de catálogo reprova a cada coleta bem-sucedida.**

E um segundo vermelho, do mesmo tipo: **`teste-navegador-c15.mjs`, `-c5` e `-c12` reprovavam por
falha de REDE**, não de código. O `render-para-teste` serve um `file://` e a casca pede a folha do
Google Fonts, que o egresso deste container barra — o console enchia de
`net::ERR_CONNECTION_RESET` e a asserção "nenhum erro de console" ficava vermelha. O
`teste-navegador-cinco.mjs` já filtrava exatamente isso desde 08/09/2026
(`!/ERR_(CONNECTION|NAME|INTERNET)/`); os três testes por calculadora estavam sem o filtro. Agora
têm, com o comentário dizendo por quê. O sinal que importa — `pageerror`, `SyntaxError`, o defeito
do `&&` escapado que derrubou as cinco calculadoras em 08/09 — continua inteiro: o filtro só
descarta falha de carregamento de recurso externo.

### NÃO CONCLUÍDO — o Sync continua fora de alcance, e agora são OITO revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** nesta sessão, tanto na URL do Sync com `&forcar=1`
quanto em `/wp-json/aquametria/v1/status`, testados nas duas pontas da execução. **Não foi
possível acionar o desembarque nem conferir a revisão aplicada**, e por isso nenhum destes três
blocos pode ser dado por "no ar" — só por "no `main`".

**O repositório está na revisão 25. A última medição do site, em 08/09 às 13h03, dizia 11.** Quem
alcança o site é a **Sentinela Técnica das 11h30, que roda no Chrome do Raphael**: basta abrir a
URL do Sync com `&forcar=1` e, uns cinco minutos depois, conferir que
`/wp-json/aquametria/v1/status` diz **revisão 25**. Enquanto isso não acontecer, o que mudou no ar
foi nada — nem as calculadoras da revisão 24, nem o catálogo novo da C15.

O que ESTE bloco muda no site, quando o Sync rodar: só a C15, que passa a poder sugerir quatro
luminárias a mais. O banco de espécies e o arquivo de cobertura são `publicar: false` e não vão
para o site por desenho — são insumo de página futura e lista de compras, não conteúdo.

### Próximo passo desbloqueado

**T1 — medir a indexação no Search Console**, que continua sendo o primeiro bloco da fila e
depende do Chrome do Raphael (Site Kit no wp-admin), não da nuvem. Ele é o que autoriza ou barra a
T4, a malha de páginas.

Enquanto a T1 não roda, o que a nuvem consegue fazer sozinha, em ordem de valor, é o que a
varredura de cobertura acabou de nomear: **fechar as seis faixas descobertas**, começando pela
luminária acima de 80 cm com fluxo declarado e pelo aquecedor acima de 300 W. Não é mais "ampliar
o banco": é fechar buraco medido, e agora existe o instrumento que diz quando o buraco fechou.

### Números do mutirão de 09/09/2026 (resposta às três perguntas do disparo)

- **Blocos entregues: 4** — o contrato (14.9 / 14.6 / 14.3), T3(a) espécies, T3(a2) iluminação
  com T3(b) voltagem dentro, e T3(c) cobertura. Todos no `main`.
- **Faixas ainda descobertas, por calculadora** (87 medidas ao todo):
  - **C15 — 22 de 22 fora do critério**, sendo 8 vazias. Nenhuma faixa cumpre.
  - **C5 — 12 de 32 fora**, sendo 4 vazias (310 a 400 L nas quatro combinações).
  - **C3 — 12 de 30 fora**, sendo 4 vazias (20 a 40 L nos três perfis comunitários, e 20 a 70 L
    no plantado).
  - **C12 — 0 de 3 fora**, mas as três exatamente no piso de 3.
- **Produtos esperando link de afiliado: 29** de 68 (39 já têm link) — 9 aquecedores, 9 filtros,
  7 luminárias (4 delas as Chihiros que nasceram hoje) e 4 mídias. Pela regra V16 todos já são
  sugeridos pela adequação técnica; o cartão sai sem botão de loja.

## 2026-09-09 (execução da noite) — T3: a leva de FECHAMENTO DE FAIXA, e a primeira vez que o buraco medido foi a lista de compras

Primeira execução da Aquametria depois que `dados/cobertura-de-faixa.md` passou a existir, e a
primeira em que a fila não veio de julgamento: veio da varredura. O bloco anterior mediu 87 faixas
e deixou uma ordem de compra escrita. Esta execução atacou os dois primeiros itens dela —
**luminária acima de 80 cm com fluxo declarado** e **aquecedor acima de 300 W** — e não escolheu
mais nada por conta própria.

Manifest revisão 27. C5 na 1.3.1, C15 na 1.1.2. Banco de 68 para **78 produtos**.

### O que entrou, e por que exatamente isto

**Quatro aquecedores, e o banco passa dos 300 W pela primeira vez.** A varredura mediu a C5 VAZIA
de 310 a 400 L nas quatro combinações de delta e tomada, por uma razão simples: o banco parava em
300 W e a janela de potência a 400 L começa em 400 W. Entraram:

| id | W | ajuste | volume declarado | o que ele fecha |
|---|---|---|---|---|
| `hopar-j-226-400w` | 400 | 18 a 34 °C | até 500 L | o único degrau de 400 W do levantamento |
| `hopar-j-226-500w` | 500 | 17 a 35 °C | até 500 L | acima de 350 L |
| `oceantech-warmer-x-5-250w` | 250 | 20 a 34 °C | até 260 L | tira do piso a faixa de 210 a 300 L |
| `oceantech-warmer-x-5-500w` | 500 | 20 a 34 °C | até 500 L (4 leituras) | acima de 350 L |

A **Hopar é marca nova no banco**, e entrou por cobertura, não por marca: das fichas conferidas, é
a única que publica um degrau de 400 W. Nenhum dos quatro tem link de afiliado — quem gera link é
a Sentinela Estratégica, e pela regra V16 os quatro já são sugeridos pela adequação técnica, com o
cartão saindo sem botão de loja.

**Seis luminárias, a família Chihiros WRGB II inteira.** A C15 não cumpria o critério em faixa
nenhuma das 22 medidas, e saía vazia em toda a escala acima de 80 cm. A escolha da família tem dois
motivos e **nenhum deles é marca**: ela declara fluxo luminoso em toda a escada de tamanhos — que é
o campo que barra a C15 — e declara **cobertura em FAIXA** (90 a 110 cm, 120 a 140 cm) em vez de um
comprimento cravado. Esse segundo ponto é o que resolve o buraco de verdade: as duas Chihiros
A-Series que já estavam no banco declaram 80 cm e 90 cm exatos, então 95, 100, 105 e 110 cm saíam
sem nenhuma opção mesmo com elas lá.

| id | lm | W | aquário coberto | status |
|---|---|---|---|---|
| `chihiros-wrgb-ii-pro-90` | 9250 | 110 | 90 a 110 cm | completo |
| `chihiros-wrgb-ii-90` | 8400 | 100 | 90 a 110 cm | conflito (publicado) |
| `chihiros-wrgb-ii-slim-90` | 3600 | 69 | 90 a 110 cm | parcial (falta comprimento da peça) |
| `chihiros-wrgb-ii-120` | 11000 | 130 | 120 a 140 cm | completo |
| `chihiros-wrgb-ii-slim-120` | 4800 | 90 | 120 a 140 cm | completo |
| `chihiros-wrgb-ii-pro-120` | — | — | 120 a 140 cm | parcial, e é o caso mais desconfortável |

### O achado que vale dinheiro: um campo colhido para um produto destravou outro

A `chihiros-wrgb-ii-pro-60` estava no banco desde 07/09/2026, **com link de afiliado**, e barrada
pela C15 por um campo só: `voltagem`. A página da calculadora publicava isso como exemplo do que as
regras custam — "a luminária mais cara do banco tem link e não é sugerida".

Catalogando a família WRGB II para cobrir os aquários grandes, a declaração apareceu: o varejo
brasileiro especializado (AquaBetta) anuncia **dois membros diferentes da linha** como bivolt, no
próprio título, e a ficha da série descreve a alimentação como entrada de 100 a 240 V por fonte
externa de 12 V. Não é inferência de voltagem, que a ilha proíbe — é declaração de varejo sobre a
linha, e a família inteira acende pela mesma fonte externa.

**Resultado: a C15 foi de 3 para 4 luminárias sugeríveis COM link, sem que nada mudasse no produto.**
E fica a regra: quando um campo barra vários registros, colher esse campo para a linha vale mais que
colher dez produtos novos.

Consequência que a mesma execução foi obrigada a pagar: **duas páginas no ar diziam algo que deixou
de ser verdade.** `conteudo/calculadora-de-iluminacao.md` e
`conteudo/quantos-lumens-por-litro-aquario-plantado.md` afirmavam que a Chihiros não é sugerida por
falta de voltagem. As duas foram corrigidas na mesma passada, e a correção virou conteúdo melhor que
o original: o exemplo não deixou de existir, ele foi **resolvido**, e a história de como — um campo
que apareceu, nunca uma exceção aberta para um produto que rende comissão — é exatamente o que
separa a Aquametria de uma fazenda de conteúdo. Página que contradiz o próprio catálogo é o defeito
de julgamento que a Sentinela procura, e ele não sobrevive a uma execução aqui.

### Duas regras de banco que este bloco fixou

**EMENDA À V12: `parcial` vale junto com `conflitos[]` quando falta obrigatório.** É a mesma emenda
que o banco de espécies já tinha no E10, e o caso que a obrigou é a `chihiros-wrgb-ii-pro-120`: a
Fazenda Submersa declara **7.700 lm com 130 W** e a Green Aqua declara **11.170 lm com 138 W** para
o mesmo aparelho — 45 % de diferença no fluxo, duas lojas especializadas do mesmo nível da escada.
Empate de nível faz o campo virar null (`campo-vira-null`), e campo null deixa o registro `parcial`.
Ou seja, **o conflito é a CAUSA da incompletude**, e exigir status `conflito` ali obrigaria o banco
a declarar completo o que não está. Completude e divergência são fatos ortogonais, `status_registro`
carrega um campo só, e vale o mais restritivo. A V12 também passou a reprovar o inverso: status
`conflito` sem nenhum conflito declarado. Esquema na **versão 7**.

O caso é desconfortável de propósito e fica publicado por isso: é a única luminária de 120 cm da
família que uma loja brasileira anuncia, tem link em potencial, e **mesmo assim não é sugerida**.
Se a diferença for versão do produto, é a loja que precisa dizer qual está vendendo; se for erro de
transcrição, é a prova de que o número que dimensiona iluminação no Brasil não passa por conferência
nenhuma. Desempata quem tiver a caixa na mão.

**Anúncio de marketplace continua não sustentando campo técnico, e agora com custo medido.** O
título do anúncio do Hopar J-226 400 W diz "até 400 L"; o varejo especializado diz "até 500 L". Não
é empate: nível 6 não sustenta número técnico. A ficha publica o 500 e registra o 400 com
atribuição, para o leitor saber que a divergência existe.

### O achado editorial: entre 300 W e 500 W o mercado brasileiro não tem degrau

Procurando o aquecedor que fecharia a faixa, a busca devolveu 300 W e 500 W em todas as linhas, e
**400 W em uma só** (Hopar J-226). A janela de potência a 310 L vai de 310 a 465 W. Ou seja: para o
aquário de 310 a 333 litros existe, no Brasil, **exatamente um** aparelho único possível — e acima
disso a resposta honesta continua sendo dois aquecedores, que é também o arranjo mais seguro por
modo de falha do termostato, coisa que a C5 já dizia na tela desde 08/09/2026 sem saber que estava
descrevendo uma lacuna de catálogo do país inteiro.

### Ferramenta nova, e ela nasceu de um defeito medido

`ferramentas/atualizar-manifest.py` recalcula o sha256 de todo item do manifest e sobe a revisão
quando algum mudou. Não é conveniência: **na primeira execução ele achou QUATRO itens com sha
vencido** — `render-para-teste.php`, `teste-navegador-c5.mjs`, `-c12.mjs` e `-c15.mjs` —, todos
alterados em execuções anteriores sem que ninguém atualizasse o registro. Nos quatro casos é
ferramenta de bancada com `publicar: false`, então o site não quebrou. O mesmo esquecimento num item
publicável faz o Sync recusar o arquivo no ar e a revisão do site ficar para trás **em silêncio**,
que é exatamente o defeito da seção 4 do `ARQUIPELAGO.md`. O passo manual que a gente esquece é o
passo que vira ferramenta.

Ele também lista o que está na pasta e fora do manifest, e isso expôs uma inconsistência que fica
anotada como dívida: das 21 ferramentas, 14 estão no manifest e 7 não, sem critério visível —
`conferir-slugs.py`, `varrer-cobertura.mjs`, `teste-navegador-casca.mjs`, `render-casca-para-teste.php`,
`gerar-favicon.php`, `proteger-funcoes.php` e os três `README.md` de pasta.

### Dois testes que estavam medindo a coisa errada

**`conferir-entidades.mjs` estava VERMELHO desde 09/09 de manhã, e não era defeito de código.** Ele
passava **todo** bloco `<script>` por `node --check` — inclusive o `<script type="application/ld+json">`
que nasceu com o JSON-LD do bloco 4c. JSON não é JavaScript: um objeto literal solto é sintaxe
inválida, então C3 e C5 reprovavam desde que ganharam visibilidade em IA. Agora cada bloco é
conferido pelo verificador da linguagem dele, e o JSON-LD passa por `JSON.parse`, que aqui é **mais
severo** que `node --check` seria: um `&#038;` no meio de uma string escapada quebra a análise, que
é exatamente o defeito de 08/09/2026 reaparecendo no lugar novo. Saída passou a contar `jsonld_ok`
à parte de `js_ok`. Falhas: 3 → 0.

Na mesma varredura saiu a terceira ocorrência da regra "entidade em comentário também sai": a casca
1.3.0, escrita ontem, voltou a escrever a entidade por extenso num comentário explicando o defeito.
Trocada pela descrição em palavras.

**`teste-navegador-c15.mjs` reprovou em 5 asserções, e três delas eram o buraco que este bloco
fechou.** É a terceira vez que a ilha tropeça no mesmo padrão, então vale escrito de uma vez:
*teste que fixa tamanho de catálogo, ou que exige que um buraco continue aberto, reprova exatamente
o trabalho que a fila manda fazer.* O que mudou:

- `duas luminárias sugeridas` (contagem fixa) → **pelo menos uma**, porque a Pro 60 destravada passou
  a cobrir os 60 cm do caso.
- `Chihiros barrada por voltagem` → caiu. Ela media um defeito de coleta nosso, não uma promessa da
  tela. No lugar entraram duas asserções que são contrato de verdade: a linha Soma inteira (oito
  registros, todos COM link) aparece na lista de barradas, e **nenhuma barrada sai sem motivo
  escrito**.
- `nenhum produto cobre um aquário de 120 cm` → trocado para **115 cm**, com o porquê no comentário:
  120 cm deixou de ser buraco nesta execução, e 115 cm é o buraco que sobrou, porque as peças do
  mercado declaram 90 a 110 ou 120 a 140 e ninguém declara o meio. Quando 115 cm for coberto, troque
  de novo em vez de afrouxar a asserção — o que se testa ali é a tela dizer a verdade quando não tem
  o que sugerir.

### A medida, e ela é o ponto do bloco

Varredura rodada de novo com o **mesmo instrumento e o mesmo eixo** (`varrer-cobertura.mjs`,
Chromium de verdade, 486 pontos). Comparação por PONTO medido, não por linha de tabela — as linhas
agrupam pontos contíguos de mesma contagem e se re-segmentam a cada medição, então contar linhas
não compara com nada.

| | manhã | noite |
|---|---:|---:|
| pontos que cumprem o critério | 312 de 486 | **379 de 486** |
| pontos abaixo do piso de 3 | 81 | 73 |
| pontos VAZIOS | 93 | **34** |

| | ok | abaixo de 3 | VAZIA |
|---|---:|---:|---:|
| C3 (manhã e noite) | 131 | 13 | 12 |
| C5 manhã | 64 | 52 | 40 |
| **C5 noite** | **128** | **28** | **0** |
| C12 (manhã e noite) | 117 | 0 | 0 |
| C15 manhã | 0 | 16 | 41 |
| **C15 noite** | **3** | **32** | **22** |

**A C3 e a C12 devolveram número IDÊNTICO nas duas medições.** Não é detalhe: o banco delas não foi
tocado, então a repetição exata é o controle que prova que o instrumento é estável e que a diferença
na C5 e na C15 veio do banco, não da medida.

**A C5 não tem mais nenhum ponto vazio de 20 a 400 L.** Era o buraco número 2 da lista de compras, e
está fechado. **A C15 cumpriu o critério pela primeira vez desde que existe**, em dois degraus: 60 a
65 cm na exigência média e 90 cm na alta.

### O que a medição nova ensinou, e que a anterior não sabia pedir

**A exigência BAIXA virou o pior caso da C15, por inversão.** De 85 a 120 cm ela sai vazia
justamente porque as luminárias que entraram são potentes DEMAIS: a faixa de lúmens que a exigência
baixa pede fica abaixo do que uma WRGB II de 90 a 130 W entrega. A compra que falta não é "mais
luminária grande" — é **barra econômica de 100 a 120 cm com lúmen declarado**. A lista de compras da
manhã pedia o oposto, e teria sido gasto errado se seguida às cegas. É o argumento da seção 14.3 do
contrato funcionando: cobertura se mede, não se estima.

**Aquecedor acima de 300 W saiu da lista de compras.** A faixa está coberta e o único trecho magro
(310 a 330 L, com um aparelho) é lacuna do mercado brasileiro, não do banco — comprar mais não
fecha, e a tela já explica.

### NÃO CONCLUÍDO — o Sync continua fora de alcance, e agora são QUINZE revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** nesta sessão, testado no fim da execução em
`/wp-json/aquametria/v1/status`. **Não foi possível acionar o desembarque nem conferir a revisão
aplicada**, então nada deste bloco pode ser dado por "no ar" — só por "no `main`".

**O repositório está na revisão 27. A última medição do site, em 08/09 às 13h03, dizia 11.** Quem
alcança o site é a Sentinela Técnica das 11h30, que roda no Chrome do Raphael: basta abrir a URL do
Sync com `&forcar=1` e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisão 27**.

O que este bloco muda no site quando o Sync rodar: a C5 passa a sugerir aquecedor acima de 300 W, a
C15 passa a sugerir luminária para aquário de 90 a 140 cm e volta a sugerir a Chihiros WRGB II Pro 60
(que tem link), e duas páginas param de afirmar algo que deixou de ser verdade. O banco em si é
`publicar: false` e não vai para o site por desenho.

### Verificação desta execução (seção 8 do `ARQUIPELAGO.md`)

- `php -l` nos 8 snippets: limpo. `conferir-protecao-funcoes.py`: limpo.
- `conferir-entidades.mjs`: **0 falhas** (eram 3, e as 3 eram do próprio instrumento — ver acima).
- `conferir-slugs.py`: 9 slugs concordam, nenhum link publicado aponta para página inexistente.
- `teste-conversor-markdown.php`: 17 casos, 0 falha. `teste-apelidos.php`: 59 afirmações, 0 falha.
- `teste-escape-shortcode.php`: todas as afirmações passaram.
- `validar-produtos.py`: **78 produtos, 39 cotações, 0 erro**, 9 avisos (todos conhecidos: V20 de
  produto com link e sem foto, e o V11 do Jäger 200 W, que é conteúdo da página).
- **`teste-navegador-c5.mjs`: 15 cenários em Chromium real, todos passaram.**
- **`teste-navegador-c15.mjs`: 78 asserções em Chromium real, todas passaram** depois das correções
  descritas acima.
- **C1, C3 e C12 não foram re-testados no navegador de propósito, e dá para provar por quê:**
  `git diff` mostra os três snippets **byte a byte idênticos**. Só C5, C15 e um comentário da casca
  mudaram. Além disso, a varredura de cobertura re-executou a C3 e a C12 inteiras num Chromium de
  verdade e devolveu o número idêntico ao da manhã, o que é um teste de regressão melhor que
  re-rodar as asserções.
- Site no ar: **não conferido** — egresso bloqueado, registrado acima como não concluído.

### Produtos esperando link de afiliado: 39 de 78

Metade do banco. Por entidade: 13 luminárias, 13 aquecedores, 9 filtros e 4 mídias. Os 10 que
entraram hoje estão todos nessa conta. Pela regra V16 todos já são sugeridos pela adequação técnica;
o cartão sai sem botão de loja. **Este número é trabalho pendente de verdade, e é da Sentinela
Estratégica** — não consome execução da Fundação, então nunca compete por fila.

### Próximo passo desbloqueado

**T1 — medir a indexação no Search Console** continua sendo o primeiro bloco da fila e continua
dependendo do Chrome do Raphael (Site Kit no wp-admin), não da nuvem. É ele que autoriza ou barra a
T4, a malha de páginas, que é o motor de tráfego da ilha.

O que a nuvem consegue fazer sozinha, agora com a lista de compras corrigida pela medição da noite:
**luminária de exigência baixa (lúmen modesto) de 85 a 120 cm**, que é a faixa vazia mais larga que
sobrou e que a medição da manhã nem enxergava; depois luminária com lúmen declarado de 30 a 55 cm; e
filtro de baixa vazão para 20 a 40 L, que é a entrada da C3 e continua vazia desde a manhã.

---

## 09/09/2026 — 21h a 22h UTC · Fundação · despacho da Sentinela (itens 1 e 3), T2 e o par C15 do T7

**Revisão do repositório: 27 → 29.** A ilha foi escolhida pela regra da seção 1 do
`ARQUIPELAGO.md` na SEGUNDA tentativa: a primeira reserva foi da Robometria e o push perdeu a
corrida para outra execução da Fundação que reservou a mesma ilha no mesmo minuto. Rebase, volta ao
passo 2, Aquametria reservada às 21h18. **A reserva por commit funcionou exatamente como projetada** —
é o primeiro registro de duas execuções simultâneas se cruzando, e nenhuma das duas trabalhou em
ilha alheia.

### Item 1 do despacho (= T2): `/category/uncategorized/` no sitemap

A causa de raiz não estava no sitemap: **está no Sync**, que grava artigo com `wp_insert_post` e
nunca atribui categoria — então o WordPress despeja tudo na padrão. Consertar pelo Sync exigiria
passar pelo atualizador (caminho mais longo e mais arriscado, e o Sync se pula a si mesmo por
desenho), então o conserto foi feito pelo lado que **se auto-corrige**: um snippet novo,
`aquametria-seo-tecnico` v1.0.0, que varre a categoria padrão a cada carregamento enquanto ela tiver
post dentro. Artigo novo que o Sync criar amanhã cai na mesma varredura.

O que ele faz: (a) cria a categoria "Métodos", move para ela todo post da categoria padrão e **troca
a categoria padrão**, para o problema não voltar pela porta que o criou; (b) tira do
`wp-sitemap.xml` o provedor de autores sempre, e o de taxonomias enquanto nenhuma categoria estiver
curada; (c) manda `noindex, follow` para arquivo por data, autor, tag, categoria não curada (a "sem
categoria" inclusive), anexo, busca e 404 — **pelo filtro `wp_robots` do próprio núcleo**, e não
imprimindo meta na mão, porque duas metas "robots" na mesma página o Google resolve pelo lado mais
restritivo; (d) desliga a página de anexo pelo interruptor do núcleo; (e) **não toca em página,
artigo nem home.**

**A categoria "Métodos" nasce FORA do sitemap e com `noindex`, de propósito** — e essa foi a decisão
que exigiu mais cuidado, porque os itens 1 e 2 do despacho se contradizem na superfície: o item 1
manda criar categoria de verdade, o item 2 proíbe URL nova até 16/09. A saída que atende os dois é
tirar os artigos da "sem categoria" **sem pedir ao Google que indexe a categoria nova**. Quando a
leitura de 16/09 liberar e a listagem tiver texto próprio (seção 14.4), basta acrescentar `metodos`
em `aquametria_seo_categorias_no_sitemap()`: entra no sitemap e sai do `noindex` na mesma linha.

### Item 3 do despacho: a regra das ilhas que não se interligam

Escrita na seção 10 do `ARQUIPELAGO.md`, que era a condição para apagar o item — e apagada de lá no
mesmo commit, como o despacho manda. A regra ficou escrita pelo motivo, não pelo par: público sem
sobreposição, arquipélago é economia de fábrica e não rede de links, e a exceção futura exige nomear
as duas ilhas e justificar pelo leitor.

### T7, par C15 — e o achado que muda o tamanho do bloco seguinte

A C15 recebeu as **três** peças da seção 5 que faltavam nela, não só o JSON-LD: resposta antes da
explicação, tabela de exemplos pré-renderizada e JSON-LD (`WebApplication` + `FAQPage` de 15
perguntas). Seis aquários de 30 a 120 cm resolvidos em PHP com as mesmas regras do script — `lm()` e
`litros()` espelhados função a função, porque tabela servida que contradiz a calculadora logo acima
dela é pior que tabela nenhuma.

**Três das seis linhas dizem que NENHUMA luminária do banco atende**, com o motivo escrito. Não é
defeito: é a faixa vazia que a varredura de cobertura já tinha medido, agora visível na página em
vez de escondida atrás de um formulário. Bloco de produto vazio é portão (seção 7) — mas silêncio
parece defeito, e por isso a célula explica.

**O achado, e ele custa tempo de quem pegar o próximo bloco:** medindo para escrever isto, ficou
claro que **nem a C12 nem a C1 servem tabela de exemplos, e nenhuma das duas tem resposta direta no
topo**. O T7 nessas duas não é "acrescentar schema", é o pacote inteiro — planeje como bloco de
calculadora. O molde está pronto na C15.

### Verificação desta execução (seção 8 do `ARQUIPELAGO.md`)

- `php -l` nos 9 snippets: limpo, **com controle negativo** — como os snippets não têm `<?php` no
  topo, `php -l` cru passaria mesmo com erro de sintaxe; o lint foi feito com o marcador prefixado e
  um erro proposital foi injetado para provar que o instrumento acusa.
- `conferir-protecao-funcoes.py`: 9 snippets, todas as funções dentro de `function_exists`.
- `teste-seo-tecnico.php` (novo): **28 afirmações, 0 falha.** Exercita as duas metades do risco — o
  que tem que sair do índice sai, e **o que não pode sair fica**. Um `noindex` sobrando numa
  calculadora seria um defeito muito pior do que o consertado aqui.
- `teste-navegador-c15.mjs`: **78 afirmações em Chromium real, TUDO PASSOU, console limpo.**
- **O teste de navegador pegou dois defeitos meus, em duas rodadas**, e vale registrar porque é
  exatamente para isso que ele existe: eu tinha reusado `.aqm-c15-aviso-afiliado` e depois
  `.aqm-c15-fontes` nos elementos novos, e cada reuso quebrou um localizador que o teste usa em modo
  estrito. Nenhum dos dois é erro de sintaxe, e nenhum apareceria em `php -l`. Viraram classes
  próprias (`aqm-c15-aviso-tabela`, `aqm-c15-exemplos`) com o estilo herdado pela lista de seletores.
- `conferir-entidades.mjs`: 0 falhas. **C15 passou a `jsonld_ok=1`** (eram C3 e C5 só). Zero
  entidade `&#038;` dentro de `<script>` nas cinco calculadoras.
- JSON-LD analisado como JSON de verdade: 2 nós (`WebApplication`, `FAQPage`), 15 perguntas, cada
  resposta conferida contra o número que a tabela servida mostra.
- `validar-produtos.py`: 78 produtos, 0 erro, 9 avisos conhecidos. `conferir-slugs.py`: limpo.
- `teste-conversor-markdown.php` (17 casos), `teste-apelidos.php` (59 afirmações),
  `teste-escape-shortcode.php`: 0 falha.

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são DEZOITO revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** de novo, testado em
`/wp-json/aquametria/v1/status`. **O Sync não foi acionado e a revisão aplicada não foi conferida**,
então nada desta execução pode ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 29; a última medição do site, em 08/09 às 13h03, dizia 11.** E o egresso não
bloqueia só o site: `chihirosaquaticstudio.com` também foi recusado, o que **torna o T3 (catálogo)
inexecutável da nuvem** — produto novo exige ficha de fabricante com fonte e data, e inventar dado
técnico é proibido. Foi por isso que esta execução fez despacho + T2 + T7, e não banco.

**O que destrava tudo é um gesto de trinta segundos no Chrome do Raphael:** abrir a URL do Sync com
`&forcar=1` e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz **revisão
29**. Depois disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem `/category/uncategorized/`,
e essa URL servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução. Por marca: 10 Atman, 10 Chihiros, 4 Eheim, 3
Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Roxin, Ista, WFish, JBL e um sem marca.

**O número "20 sem loja possível" do item 4 do despacho está VENCIDO e não deve ser repetido.** Ele
foi medido quando a Shopee era o único programa; o Mercado Livre entrou em 09/09 justamente porque a
Shopee não vende Eheim, Atman canister, Chihiros e JBL — que são **24 dos 39** desta lista. Quem
refizer essa medição precisa do painel do Mercado Livre aberto, e isso é da Sentinela estratégica,
não da Fundação.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4.
2. **T7, par C12** — trabalho de repositório, não depende de egresso. Agora se sabe que é bloco
   inteiro de calculadora (tabela + resposta direta + JSON-LD), com o molde pronto na C15.
3. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear os sites de fabricante.

---

## 09/09/2026 — execução das 23h17Z: T7, par C12 — a calculadora de mídia deixou de ser um formulário vazio para quem não executa JavaScript

**Bloco:** T7 (visibilidade em IA), par C12. Escolhido por ser o primeiro da fila que **não depende do
egresso**: o T1 continua dependendo do Chrome do Raphael e o T3 (catálogo) segue barrado enquanto a
nuvem não alcançar site de fabricante. Manifest **revisão 30**, C12 na versão **1.2.0**.

A ilha foi sorteada pela regra da seção 1 do `ARQUIPELAGO.md`. **A primeira tentativa foi na
Robometria e o push da reserva foi RECUSADO**: outra execução (`session_013a11...`) commitou a
reserva dela 13 segundos antes. Rebase, volta ao passo 2, e a Aquametria era a próxima elegível.
A reserva por commit funcionou exatamente como o contrato promete — duas execuções simultâneas, zero
atropelo, sem force push.

### O que entrou, e por que é bloco de calculadora e não retoque de schema

O registro anterior já tinha medido isto e vale confirmar: **o T7 na C12 não era "acrescentar
JSON-LD"**. A página não tinha nenhuma das três peças da seção 5. Entraram as três:

- **(a) Resposta antes da explicação** (`aquametria_c12_resposta_direta_html`, bloco `aqm-c12-direta`,
  ANTES do formulário). Frase autossuficiente com número, unidade, quem declarou e data — escrita
  para sobreviver a ser citada por um modelo que leu só aquele parágrafo. 2.052 caracteres, quatro
  parágrafos: a faixa em 100 L, por que a ilha não escolhe nem tira média, o teto físico, e o que a
  conta não sabe.
- **(b) Tabela de exemplos pré-renderizada** (`aquametria_c12_exemplos_html`), seis aquários de 30 a
  300 L resolvidos no PHP, cinco colunas: a faixa da mídia biológica do piso ao teto com o nome de
  quem sustenta cada extremo; a mídia TOTAL que quem vende filtro reserva; o **teto físico**; e a
  mídia do banco para comprar, com a quantidade pela dosagem daquele fabricante e quanto rende a
  embalagem.
- **(c) JSON-LD no `wp_head`** — nunca dentro do retorno do shortcode, pelo mesmo motivo que o script
  sai no rodapé. `WebApplication` com `featureList` de 8 itens e `FAQPage` com **15 perguntas**, cada
  resposta carregando o mesmo número que a tabela servida mostra.

**Nenhuma fórmula mudou, e nenhuma dosagem foi escolhida.** Tudo que a tabela mostra sai de espelhos
em PHP das funções do próprio script — `mL()`, `litros()`, `pct()`, `ancorasBio()`, `ancorasFiltro()`
—, função a função, porque tabela servida que contradiz a calculadora logo acima dela é pior que
tabela nenhuma. As âncoras continuam saindo do catálogo embutido, que sai do banco: mídia nova com
dosagem declarada entra na tabela servida sozinha no próximo gerador.

### O achado desta execução: quatro das seis linhas NÃO CABEM no filtro

A coluna do teto físico é a que não existe em português, e pré-renderizá-la tornou visível uma coisa
que a calculadora só dizia depois de a pessoa preencher o formulário: **a dosagem mais generosa não
cabe no filtro em quatro dos seis volumes da escada.** Em 100 L ocupa 104 % do cesto do Seachem Tidal
55; em 150 L, 156 %; em 200 L, 208 %; em 300 L, 107 % do cesto do Atman AT-3338S. Só 30 e 60 L
sobram folga (16 % e 33 % do SunSun HW-603B). O critério da célula é o da seção 7: entre os filtros
que o fabricante **declara** para aquele volume, o de menor volume declarado — que é o que a pessoa
realmente compraria, e é a leitura mais apertada. Filtro que o fabricante não declara para o volume
não entra na célula nem em último lugar.

### Três defeitos que o teste pegou, e nenhum apareceria em `php -l`

1. **Uma resposta do FAQPage não carregava número** ("Encher o cesto do filtro é melhor?"). FAQPage
   sem número é FAQPage-lixo, e é lixo detectável. Ganhou o caso medido de 200 L (2,50 L ocupando
   208 % de um cesto de 1,2 L) e as 6 posições da ordem das camadas.
2. **A tabela imprimia "30,0 L" e o teste exigia "30 L".** Aqui quem estava certo era a tabela: o
   `litros()` do script devolve uma casa decimal abaixo de 100 L, e é isso que a calculadora escreve
   quando a pessoa digita 30. **Exigir "30 L" cravado reprovaria a tabela por ser FIEL ao script**,
   que é o oposto do que o teste existe para garantir. Quem cedeu foi o teste.
3. **A C15 tinha as três peças desde a revisão 29 e mesmo assim ficava FORA do teste que as mede.**
   O bloco de resposta direta dela usava `aqm-c15-citar` — a MESMA classe da caixa de citação do
   resultado, duas coisas diferentes com o mesmo nome — e o painel de exemplos não tinha onde o teste
   pendurar o localizador. Peça entregue sem teste é peça que a próxima sessão quebra sem ninguém
   notar.

### O verde falso que estava no ferramental desde 09/09 de manhã

`conferir-protecao-funcoes.py` recebe os arquivos por argumento. **Chamado sem argumento, ele varria
uma lista vazia e saía 0 em silêncio.** Verde falso é pior que vermelho: treina a próxima sessão a
confiar num instrumento que não olhou para nada. Agora, sem argumento, ele varre os snippets da
própria ilha e diz quantos; e sem achar arquivo nenhum, **reprova em vez de aprovar**. Controle
negativo conferido: desprotegendo uma função de propósito, ele acusa a linha e sai 1.

**Regra que fica, e é a terceira vez que a ilha tropeça em alguma versão dela:** instrumento que pode
sair 0 sem ter medido nada não é instrumento. Todo verificador desta ilha precisa reprovar quando não
mede — nunca aprovar por omissão.

### Verificação desta execução (seção 8 do `ARQUIPELAGO.md`)

- `php -l` nos 9 snippets: limpo, **com controle negativo** — como os snippets não têm `<?php` no
  topo, o lint foi feito com o marcador prefixado e um erro proposital foi injetado para provar que o
  instrumento acusa.
- `conferir-protecao-funcoes.py`: 9 snippets, **214 funções** (34 na C12, eram 22), todas dentro de
  `function_exists`, **com controle negativo**.
- `teste-navegador-visibilidade-ia.mjs`: **124 afirmações em Chromium real com o JavaScript
  DESLIGADO, 0 falha**, agora nas QUATRO calculadoras que têm as três peças (eram 46 afirmações em
  duas). É o teste que mede o que esta execução entregou: com o script desligado, a tabela e a
  resposta direta são a única coisa citável que a página serve.
- `teste-navegador-c12.mjs`: **84 cenários em Chromium real, todos passaram, console limpo** — a
  calculadora continua calculando, o teto físico continua estourando onde deve, o bloco de produto
  continua aparecendo dentro da resposta e o celular de 390 px continua sem rolagem horizontal.
- `conferir-entidades.mjs`: 0 falhas. **C12 passou a `jsonld_ok=1`** (eram C3, C5 e C15). Zero
  entidade numérica dentro de `<script>` nas cinco calculadoras. Falta só a C1.
- JSON-LD analisado como JSON de verdade: 2 nós, 15 perguntas, e conferido item a item que o número
  do FAQ para 100 L (`125 mL a 1,25 L`) é o MESMO que a tabela servida mostra e o mesmo que a
  calculadora devolve.
- `teste-escape-shortcode.php`, `teste-conversor-markdown.php` (17 casos), `teste-apelidos.php` (59
  afirmações), `conferir-slugs.py`: 0 falha.
- `validar-produtos.py`: 78 produtos, 0 erro, avisos conhecidos. `validar-especies.py`: 36 espécies,
  0 erro, 1 aviso conhecido (E15 do guppy).
- `atualizar-manifest.py`: 4 arquivos com sha novo, **revisão 30**, 0 item com sha vencido.

### O que ficou medido para quem pegar o próximo bloco

**Os testes de navegador desta ilha levam DEZENAS de minutos na nuvem, e o motivo não é o teste.**
Cada `page.goto()` espera o `load`, e o `load` espera as fontes do Google, que o egresso barra até o
timeout de 30 s — por navegação. O teste da C12 sozinho faz mais de vinte navegações. Rodar três em
paralelo é PIOR, não melhor: três Chromiums disputam a mesma máquina e todos rastejam. **Rode um de
cada vez.** Isso não é defeito de código e não reprova nada — mas é a diferença entre uma execução
que verifica e uma que desiste de verificar, e é assim que verificação morre.

### A quarta asserção vencida, achada rodando o teste que a seção 8 exige

`teste-navegador-cinco.mjs` reprovou a C15 em **"bloco de produto oculto, como manda a regra do
banco — apareceu"**. Não era regressão desta execução: o diff inteiro da C15 aqui são DUAS classes CSS
acrescentadas a `div`, e classe não faz bloco de produto aparecer. O caso trazia `semProduto: true`
com este comentário escrito pelo próprio autor: *"Vira semProduto:false no dia em que o banco tiver
luminária apta."* **Esse dia foi 09/09**, na leva de catálogo que deu voltagem à Chihiros WRGB II Pro
60 e levou a C15 de 3 para 9 aptas. Ninguém voltou ao teste.

Em vez de virar o booleano — que apodrece de novo no próximo movimento de catálogo — a afirmação
deixou de dizer QUAL dos dois estados a página deve ter. **Os dois são legítimos, e quem decide qual é
hoje é o catálogo, não o teste.** Passou a afirmar a PROMESSA de cada estado: bloco visível tem de
estar bem formado (todo link que existir com `sponsored`, `noopener` e aba nova, mais aviso de
comissão); bloco oculto tem de dizer por que não sugere e não pode vazar link.

E como `every()` sobre lista vazia passa por vácuo, entrou uma afirmação de CONJUNTO: **nenhuma
calculadora é obrigada a ter link** — a ordem é por adequação técnica e catálogo maior chega a
*reduzir* links na tela, então exigir link por página seria pedir que o banco não melhorasse — mas as
cinco juntas não podem ficar sem nenhum, porque aí não é catálogo, é encanamento quebrado. Deu **7
links bem marcados**, e a C15 agora serve bloco de produto com 1 link: a lacuna fechou de verdade.

Manifest **revisão 31**. `teste-navegador-cinco.mjs`: **56 afirmações, 0 falha, as cinco calculando
em Chromium real** — que é o mínimo que a seção 8 exige quando a sessão não alcança o site.
`teste-navegador-c15.mjs` rodado de novo depois das duas classes novas: **78 afirmações, tudo passou,
console limpo.**

**Quatro asserções vencidas em duas execuções seguidas, todas do mesmo tipo.** Vale escrever a regra
de uma vez: *afirmação que descreve o ESTADO do catálogo — quantos itens, qual buraco está aberto,
qual produto está barrado — vence sozinha e reprova o trabalho da fila. Afirme a promessa, nunca o
estado.*

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são VINTE revisões paradas

`aquametria.com.br` devolveu **EGRESS_BLOCKED** de novo, testado em `/wp-json/aquametria/v1/status`.
**O Sync não foi acionado e a revisão aplicada não foi conferida**, então nada desta execução pode
ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 31; a última medição do site, em 08/09 às 13h03, dizia 11.**

**O que destrava tudo continua sendo um gesto de trinta segundos no Chrome do Raphael:** abrir a URL
do Sync com `&forcar=1` e, uns cinco minutos depois, conferir que `/wp-json/aquametria/v1/status` diz
**revisão 31**. Depois disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem
`/category/uncategorized/`, e essa URL servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução. Por marca: 10 Atman, 10 Chihiros, 4 Eheim, 3
Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Roxin, Ista, WFish, JBL e um sem marca.
Continua valendo o registrado em 09/09: o número "20 sem loja possível" está VENCIDO e não deve ser
repetido, porque foi medido quando a Shopee era o único programa. Refazer essa medição exige o painel
do Mercado Livre aberto, e isso é da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4.
2. **T7, leva 3: a C1 e depois os três artigos.** É o último par de calculadora sem as três peças —
   `conferir-entidades.mjs` mostra a C1 como a única com `jsonld_ok=0`. Mesmo molde, agora com DOIS
   exemplos prontos (C15 e C12) e com o teste de visibilidade já preparado para receber o caso novo:
   basta acrescentar a C1 em `CASOS`, com o eixo e a âncora dela.
3. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## 2026-09-10, 11h19Z–11h40Z — T7, leva 3: a C1 fecha o retrofit de visibilidade em IA

Ilha reservada às 11h19Z pelo commit de reserva, como manda a seção 1 do `ARQUIPELAGO.md`. A
Robometria estava reservada havia um minuto por outra execução e caiu fora pela regra dos 40 minutos;
sobrou a Aquametria, que também era a de `ultima_execucao` mais antiga entre as elegíveis.

Bloco escolhido: **T7, leva 3 — a C1**. O T1 continua sendo o primeiro da fila e continua dependendo
do Chrome do Raphael, então o que estava desbloqueado era este.

### O que a C1 ganhou

Snippet `aquametria-calculadora-litragem.php` na **v1.2.0**, manifest na **revisão 32**. As três peças
da seção 5, de uma vez: **resposta antes da explicação** no topo (2.126 caracteres, com os três
volumes de um aquário concreto e a data de verificação dentro da frase), **tabela pré-renderizada**
com seis aquários e **JSON-LD** (`WebApplication` + `FAQPage` de nove perguntas) no `wp_head`, nunca
dentro do retorno do shortcode. **Nenhuma linha de cálculo mudou**: tudo que a tabela imprime é
espelho em PHP do `fmt()`, do `litros()` e do ramo de `calcular()` que ela representa.

Com isso o `conferir-entidades.mjs` deixa de ter alguma calculadora em `jsonld_ok=0`: são **5 de 5**.

### A decisão que este bloco tomou, e que não estava no molde

O molde da C15 e da C12 respondia como montar as peças, não **em que eixo** a tabela é indexada. A C3,
a C5 e a C12 indexam por litro; a C15 por centímetro, porque luminária é vendida por centímetro. A
tentação era cravar litro na C1, que é *a calculadora de litros*.

Seria errado, e por um motivo que vale para toda ilha: **na C1 o litro é a SAÍDA.** Quem abre esta
página tem a fita métrica na mão e não sabe o volume — se soubesse, não precisaria da calculadora.
Uma tabela indexada por litro responderia à pergunta que a pessoa ainda não consegue fazer. O eixo
ficou o comprimento da frente, na mesma escada da C15 (30, 45, 60, 80, 90 e 120 cm), que é como o
aquário e a luminária são vendidos. **Regra que sai daqui: o eixo da tabela pertence à pergunta, não
ao formato da ferramenta.**

Segunda decisão, esta sobre produto: **a tabela da C1 não tem link de loja, e diz por quê.** Litragem
é geometria, e geometria não escolhe produto — quem escolhe filtro, aquecedor, mídia e luminária são
as calculadoras que leem este volume, e é lá que o bloco de produto nasce dentro da resposta, como
consequência do cálculo. A seção 7 do contrato manda dizer ao visitante por que o bloco está vazio, e
o aviso da tabela faz isso em vez de deixar silêncio, que parece defeito.

Terceira: as medidas e a espessura de cada linha são **ENTRADAS do exemplo**, exatamente como os
volumes de 30 a 300 L são entradas nas tabelas da C3 e da C5 — não são catálogo de fabricante e não
são recomendação de vidro. A nota da tabela declara isso com todas as letras, porque a Aquametria não
dimensiona vidro e uma coluna de espessura sem essa frase seria lida como conselho.

### Verificação (seção 8), com número medido

- `php -l` limpo; `conferir-protecao-funcoes.py` ok — toda função de nível superior dentro de
  `function_exists`.
- `conferir-entidades.mjs`: **0 falhas**, C1 agora com `jsonld_ok=1`, `entidade_038_no_documento=0`,
  script depois do conteúdo. (O `numéricas_no_documento=1` da C1 é o `&#039;` de "lâmina d'água" no
  rótulo do campo, fora de `<script>` — já era assim antes e é legítimo.)
- `teste-navegador-visibilidade-ia.mjs` com a C1 acrescentada em `CASOS`: **155 afirmações, 0 falha,
  JavaScript DESLIGADO** nas cinco calculadoras.
- `teste-navegador-cinco.mjs`: **56 afirmações, 0 falha**, as cinco calculando em Chromium real, 7
  links de afiliado bem marcados no conjunto.
- `teste-escape-shortcode.php` e `conferir-slugs.py`: ok.

### O teste novo, e por que ele foi escrito assim

`ferramentas/teste-navegador-c1-tabela.mjs` — **28 afirmações, JavaScript LIGADO**. Ele põe a tabela
servida contra a própria calculadora: lê as seis linhas do HTML, extrai da coluna do aquário as
medidas e a espessura que geraram cada linha, digita essas entradas no formulário e compara os três
volumes e a lâmina. Deu igual nas seis linhas (22,5/20,9/18,8 · 40,5/37,6/33,8 · 63,0/58,3/53,2 ·
128/118/109 · 182/170/158 · 300/278/261), console sem erro de página.

Ele **não guarda número esperado nenhum**, de propósito. Quatro asserções venceram sozinhas em duas
execuções seguidas nesta ilha, todas do mesmo tipo, e a regra que ficou escrita foi: *afirme a
promessa, nunca o estado*. A promessa aqui é "a tabela servida não contradiz a calculadora" — mudar
as medidas de exemplo, a borda livre ou o arredondamento não reprova nada, e é assim que ele
sobrevive à próxima execução.

Uma asserção nasceu passando por engano e foi consertada antes do commit: a que confere se todo
volume citado na resposta direta existe na tabela usava `includes()`, e `"1 L"` é substring de
`"261 L"`. Passou a comparar por token. Com a comparação certa, a frase que citava a divergência de
densidade do substrato como "1 kg ≈ 1 L" ficou sem lastro na tabela — e a saída certa não era
afrouxar o teste, foi escrever "1 kg como um litro" por extenso, que é um número de fonte externa e
não um volume que esta página calcula. Três volumes citados, três com lastro.

### Uma contradição da própria página, corrigida no caminho

A abertura de `conteudo/calculadora-de-litragem.md` afirmava que a diferença entre a etiqueta e a água
real "passa de 15 %". Com o aquário que ela mesma cita (80 × 40 × 40 cm, vidro de 8 mm, lâmina no
valor inicial), a conta dá **14,9 %** — 128 L na etiqueta contra 109 L de água. Não passava de 15 %:
chegava a 15 %. A frase agora dá os dois números e o percentual exato. É defeito pequeno e é
exatamente o tipo que a tabela pré-renderizada expõe, porque põe o número ao lado da afirmação.

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são VINTE E UMA revisões paradas

`aquametria.com.br/wp-json/aquametria/v1/status` devolveu **EGRESS_BLOCKED** nesta execução também,
testado com `?v=` novo para furar o cache. **O Sync não foi acionado e a revisão aplicada não foi
conferida**, então nada deste bloco pode ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 32; a última medição do site, em 08/09 às 13h03, dizia 11.**

O que destrava continua sendo o mesmo gesto de trinta segundos no Chrome do Raphael: abrir a URL do
Sync com `&forcar=1` e, uns cinco minutos depois, conferir que o `/status` diz **revisão 32**. Depois
disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem `/category/uncategorized/`, e essa URL
servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução, e este bloco não mexeu em catálogo. Por marca: 10
Chihiros, 10 Atman, 4 Eheim, 3 Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Ista, WFish,
Roxin, JBL e um sem marca. Continua valendo o registrado em 09/09: o número "20 sem loja possível"
está VENCIDO e não deve ser repetido, porque foi medido quando a Shopee era o único programa. Refazer
essa medição exige o painel do Mercado Livre aberto, e isso é da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4.
2. **T7, o que sobrou: os 3 artigos.** Com as cinco calculadoras fechadas, é o único resto do
   retrofit. Atenção ao que NÃO se copia do molde: artigo não tem formulário, então resposta direta e
   JSON-LD valem, mas tabela pré-renderizada só entra se o artigo tiver número próprio para pôr nela.
   Tabela decorativa é pior que nenhuma.
3. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## 2026-09-10, 13h20Z — T7 leva 4: os 3 artigos-âncora fecham o retrofit de visibilidade em IA

**Bloco:** T7, o resto que sobrava depois da leva 3. Manifest **revisão 33**.
**Ilha reservada às 13h20Z**, depois de a Robometria ter sido levada por uma execução paralela na
mesma corrida de push — o mecanismo de reserva da seção 1 do contrato funcionou exatamente como
descrito: push recusado, `fetch` e `rebase`, e a escolha caiu na ilha seguinte sem atropelo nenhum.

### O que entrou no ar (no `main`, não no site — ver o fim desta entrada)

- **`snippets/aquametria-artigos.php` v1.0.0**, snippet novo, `publicar: true`, escopo front-end.
- Uma linha `[aquametria_artigo_resposta]` no topo de cada um dos três artigos de `conteudo/`:
  `quantos-watts-de-aquecedor-para-aquario.md`, `quanta-midia-biologica-o-aquario-precisa.md` e
  `quantos-lumens-por-litro-aquario-plantado.md`. Nenhuma linha de texto dos artigos foi reescrita.
- **`ferramentas/teste-navegador-artigos.mjs`** e **`ferramentas/render-artigo-para-teste.php`**,
  arquivos novos, `publicar: false`.
- Uma linha em `ferramentas/render-para-teste.php`: o slug da página de teste virou global.

Com isso o retrofit da seção 5 do `ARQUIPELAGO.md` cobre **8 de 8 páginas** de ferramenta e artigo.
A Sentinela Técnica mediu JSON-LD **zero em 13 de 13** páginas em 09/09; hoje as oito que têm
conteúdo próprio servem JSON-LD, resposta antes da explicação e tabela de números no HTML servido.

### Três decisões de projeto, e a razão de cada uma

**1. Artigo se reconhece pelo SLUG, calculadora pelo shortcode.** Não dá para descobrir a página de
um artigo por `has_shortcode()`: artigo não tem formulário. O snippet lê o `post_name` e compara com
o registro dos três slugs — os mesmos do front matter e do manifest. Amarrar o JSON-LD à presença do
shortcode da resposta direta seria pior: a página perderia o schema no dia em que alguém tirasse o
bloco do topo. Vale para toda ilha: **página de conteúdo se identifica pelo endereço; página de
ferramenta, pelo shortcode que ela carrega.**

**2. TABELA PRÉ-RENDERIZADA NÃO SE INVENTA — e este bloco recusou inventar três.** O `PROMPT.md`
já avisava, e o material confirmou: os três artigos JÁ serviam tabela própria no HTML servido, escrita
em Markdown e convertida pelo Sync — a linha comercial Eheim Jäger com o 1,00 W/L em seis degraus, as
quatro dosagens de mídia com a área que cada uma entrega por litro de água, e as três réguas de lm/L
lado a lado. Acrescentar uma tabela nossa por cima seria decoração, e o portão da seção 5 é **servir
resposta citável**, não servir uma tabela. O que o teste passou a exigir é que a tabela que o artigo
já tinha continue no HTML, com cabeçalho e pelo menos três linhas, e com número em toda ela.

**3. A resposta direta de artigo não é a de calculadora.** A da calculadora resolve um caso de
exemplo. A do artigo tem de entregar a **tese com número**, porque é ela que vai ser citada fora de
contexto por um modelo que leu só aquele bloco. As três, em três parágrafos cada, com fonte nomeada e
data dentro da frase:

- **C5:** não existe um watts-por-litro que valha para o Brasil inteiro; a única fonte do
  levantamento de 04/09/2026 que declara condição (ReefFlow) sustenta 1,0 a 1,5 W/L para até 10 °C, o
  que dá 100 a 150 W num aquário de 100 L; e o "1 W por litro" veio da prateleira, porque a linha
  Eheim Jäger nomeia cada aparelho pelo volume que dá exatamente 1,00 W/L em seis degraus seguidos.
- **C12:** as quatro dosagens declaradas vão de 1,25 a 12,50 mL/L — dez vezes —, a área entregue por
  litro de água vai de 0,88 a 18,8 m² (vinte e uma vezes) e na direção **contrária** ao argumento de
  venda, e nenhuma das quatro pergunta quantos peixes há no aquário.
- **C15:** "baixa" é 10, 15 ou 20 lm/L conforme a fonte, o que num aquário de 100 L é a diferença
  entre 1.000 e 2.000 lúmens; e a régua é frágil por definição, porque o lúmen desconta o azul e o
  vermelho profundos, que são as faixas da clorofila.

### O teste novo, e as duas afirmações que valem o arquivo

`ferramentas/teste-navegador-artigos.mjs` — **108 afirmações, JavaScript DESLIGADO**, que é o que um
crawler de IA recebe. Confere o nó `Article` (headline dentro do limite do schema, título completo em
`alternativeHeadline`, description, idioma, datas, autor, publisher, a consulta que a página mira e
`citation` com data em toda fonte), o `FAQPage` (oito perguntas por artigo, nenhuma resposta curta
demais para ser citada, toda resposta com número), o bloco do topo (corpo, data, fonte nomeada dentro
da frase, links de verdade e a posição **antes** do primeiro título de seção), a tabela que o artigo
já tinha, e o portão de entidade numérica contado **só dentro dos blocos de script**.

Mas o que faz o arquivo valer são duas afirmações de **coerência entre as duas metades da mesma
página**: *todo número da resposta direta existe no corpo do artigo* e *toda resposta do FAQPage
carrega ao menos um número que o corpo sustenta*. **Nenhum número esperado fica gravado no teste.**
Corrigir um dado com fonte melhor não reprova nada — desde que o topo e o FAQ mudem junto, que é
exatamente o defeito que ele existe para pegar. É o desenho do `teste-navegador-c1-tabela.mjs`
aplicado a texto em vez de formulário, e a terceira aplicação da regra que esta ilha já pagou caro
para escrever: **afirme a promessa, nunca o estado.**

Um detalhe de implementação que vale para quem copiar isto em outra ilha: o corpus dos artigos
escreve milhar com espaço fino ("6 630 lm") e o registro do snippet escreve com ponto ("6.630"). São
o mesmo número, e sem normalizar isso o teste reprovaria por **tipografia**, que é ruído. Datas saem
da comparação antes da extração, porque procedência não precisa (nem deve) aparecer no corpo.

### Controle negativo conferido, nos dois sentidos — e um defeito real pego antes do commit

- A página **como estava antes deste bloco** (sem JSON-LD e sem o bloco do topo) dá **15 falhas**.
- Trocar **um único número** da resposta direta por um que o artigo não sustenta é reprovado pelo
  valor: `FALHA todo numero da resposta direta existe no corpo do artigo — sem lastro: 1,7`.
- E o teste pegou um defeito de verdade antes do commit: a resposta do FAQ da C12 sobre troca parcial
  de mídia não carregava número nenhum. A saída certa não foi afrouxar a regra — foi amarrar a
  resposta às quatro dosagens que a própria página publica.

### Verificação da seção 8, item a item

- `php -l` nos 10 snippets e nos dois PHP de bancada: sem erro.
- `conferir-protecao-funcoes.py`: **158 funções em 10 snippets**, todas dentro de `function_exists` —
  as 11 do arquivo novo incluídas.
- `conferir-entidades.mjs`: **0 falhas**. Fonte limpo nos 10 snippets, e nas 5 calculadoras
  `jsonld_ok=1`, `entidade_038_no_documento=0`, script depois do conteúdo.
- `teste-conversor-markdown.php`: **17 casos, 0 falha** — o corpo dos três artigos continua começando
  por texto, sem resíduo de front matter, com a linha do shortcode saindo fora do `<p>`.
- `conferir-slugs.py`: 9 slugs concordando entre `conteudo/`, manifest e snippets; nenhum link
  publicado apontando para página inexistente.
- `teste-navegador-artigos.mjs`: **108 afirmações, 0 falha**, mais os dois controles negativos.
- **Regressão:** `teste-navegador-visibilidade-ia.mjs` rodado de novo nas 5 calculadoras — tudo
  passou. O snippet novo registra um `wp_head` global, e era isso que precisava ser provado inócuo
  fora das três páginas de artigo.
- `validar-produtos.py`: 78 produtos, 39 cotações, **0 erro** (9 avisos conhecidos).
  `validar-especies.py`: 36 espécies, 0 erro, 1 aviso conhecido (o E15 do guppy).
- `atualizar-manifest.py`: 7 itens com sha novo, **revisão 33**.

### NÃO CONCLUÍDO — o site continua fora de alcance, e agora são VINTE E DUAS revisões paradas

`aquametria.com.br/wp-json/aquametria/v1/status` devolveu **EGRESS_BLOCKED** nesta execução também,
testado com `?v=` novo para furar o cache duplo. **O Sync não foi acionado e a revisão aplicada não
foi conferida**, então nada deste bloco pode ser dado por "no ar" — só por "no `main`".

**Repositório na revisão 33; a última medição do site, em 08/09 às 13h03, dizia 11.**

O gesto que destrava continua sendo o mesmo, de trinta segundos, no Chrome do Raphael: abrir a URL do
Sync com `&forcar=1` e, uns cinco minutos depois, conferir que o `/status` diz **revisão 33**. Depois
disso, a medição do item 1 do despacho: `wp-sitemap.xml` sem `/category/uncategorized/`, e essa URL
servindo `noindex`.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança — nenhum produto entrou nesta execução e este bloco não tocou em catálogo. Por marca: 10
Chihiros, 10 Atman, 4 Eheim, 3 Ocean Tech, 3 SunSun, 2 Hopar, 2 Seachem, 1 cada de Ista, WFish, Roxin
e JBL, e 1 sem marca. Continua valendo o registrado em 09/09: o número "20 sem loja possível" está
**VENCIDO** e não deve ser repetido, porque foi medido quando a Shopee era o único programa. Refazer
essa medição exige o painel do Mercado Livre aberto, e isso é da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T1 — medir a indexação no Search Console.** Continua sendo o primeiro da fila e continua
   dependendo do Chrome do Raphael. É ele que autoriza ou barra a T4, e a leitura de 16/09 depende
   dele para dizer por que a leva de 08/09 não indexou.
2. **T8 — a vitrine, começando pela C3.** É o primeiro bloco de construção que não cria URL nova,
   então ele respeita o item 2 do despacho da Sentinela (nenhuma página nova até 16/09) e é o que
   sobra de maior na fila agora que o T7 fechou. A C3 é a que tem mais itens com foto e link.
3. **A `Organization` com `sameAs` na home, que mora na casca**, é o resíduo do item 3 da seção 5 do
   contrato e NÃO foi feita aqui de propósito: a Aquametria não tem perfil externo nenhum (o Raphael
   não aparece em ilha nenhuma, por decisão de projeto), então `sameAs` sairia vazio ou inventado.
   Quando o widget em lojas (T6) der o primeiro perfil externo real, aí ela nasce com lastro. Fica
   registrado para a próxima execução não achar que foi esquecimento.
4. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## EXECUÇÃO DE 10/09/2026, 17h15Z — o despacho da Sentinela de 10/09 fechou nos três itens de código

Manifest **revisão 35**, conferida no `/status` do site. Três itens do despacho numa execução, cada um
verificado no ar antes do seguinte começar, como o modo mutirão pede.

### Item 1 — as 13 URLs do sitemap passaram a servir `<meta name="description">`

Era o defeito mais caro da ilha: o `<head>` trazia 6 elementos `<meta>` e nenhum deles era a
description, em nenhuma das 13 URLs, e também não havia uma única tag `og:`. Sem description quem
escreve o resumo do resultado é o Google, recortando um pedaço qualquer do corpo — e numa página de
calculadora o pedaço costuma ser o rótulo de um campo de formulário.

O snippet `aquametria-seo-tecnico` subiu para **1.1.0** e imprime `description`, `og:title`,
`og:description`, `og:type`, `og:locale`, `og:site_name`, `og:url` e `twitter:card`.

**A decisão que vale para toda ilha: o texto não mora no snippet.** Ele mora onde a página mora — no
front matter de cada arquivo de `conteudo/`, no campo `meta_descricao` que já existia e que nada lia,
e, para as quatro páginas da casca (que nascem do snippet e não têm arquivo em `conteudo/`), em
`dados/metas-seo.json`. Duas fontes porque são dois tipos de página, mas **nenhuma página aparece nas
duas**. Quem junta e escreve o mapa entre os marcadores `METAS-INICIO` e `METAS-FIM` é
`ferramentas/gerar-metas-descricao.py`, o mesmo desenho do favicon: texto mantido em dois lugares
diverge em silêncio.

O gerador **recusa gravar** — e não grava nada — se algum texto sair de 120 a 160 caracteres, se dois
forem iguais (description repetida devolve ao Google o sinal de duplicata, que é pior do que não ter),
se um slug do sitemap ficar sem descrição, ou se aparecer descrição para slug que não está na lista
das 13. Com `--conferir` ele não grava: só reprova se o snippet estiver desatualizado, e por isso pode
rodar como portão antes do commit.

**Página fora do mapa não ganha descrição inventada** — o snippet simplesmente não imprime nada.
Description errada escrita por nós seria pior que o recorte automático do Google, porque pareceria
intencional.

**Sem `og:image`, de propósito.** A ilha não tem imagem de compartilhamento: o favicon é um SVG de
32 px embutido como data URI, e `og:image` exige URL absoluta de arquivo real. Declarar uma imagem que
não existe faz o cartão quebrar em vez de não aparecer. Ela entra quando a vitrine do T8 der à ilha a
primeira imagem própria hospedada.

Medido no ar depois do Sync, nas 13 URLs: **13 de 13 em HTTP 200, exatamente uma description em cada,
6 tags `og:` em cada, texto diferente em todas.**

### Item 3 — os três links internos que respondiam 301

O despacho dizia "o link está dentro do snippet das calculadoras". Estava, mas a causa não era o HTML
delas: **`aquametria_casca_url_se_existir()` só procurava em `post_type` `page`, e os três
artigos-âncora são `post`.** As duas vias da função falhavam, quem chamava caía no último recurso —
`home_url('/<slug>/')` —, e esse endereço existe e responde **301** para `/2026/09/08/<slug>/`.

Consertar no HTML de cada calculadora teria fechado os três casos e deixado o quarto artigo nascer com
o mesmo defeito. A casca subiu para **1.3.1** com uma terceira via, que busca por `post_name` em
`post_type` `post` e devolve o permalink real. Os três links escritos no próprio Markdown foram para a
URL canônica na mesma passada.

**O `conferir-slugs.py` aprendeu a diferença entre página e artigo** e agora reprova nos dois sentidos:
artigo linkado sem o prefixo de data, e página linkada com ele. Ele aceita **qualquer** data bem
formada em vez de cravar `2026/09/08`, senão reprovaria sozinho no dia em que nascesse o quarto artigo.
O portão foi conferido com teste negativo — os três casos pegos, inclusive o de uma linha só carregando
os dois defeitos ao mesmo tempo, que a primeira versão deixava passar.

Medido no ar: os **16 endereços internos** servidos pelas 13 páginas respondem **200, nenhum 301**.

### Item 2 — a C5 parou de se contradizer no bloco de produto

O despacho ofereceu dois caminhos e não escolheu, porque elegibilidade é da Fundação. **A escolha foi:
a elegibilidade está certa e não muda.**

Aquecedor não se vende em 160 W. O teto da lista é, de propósito, o degrau comercial que cobre o topo
da faixa — e a própria página anuncia isso duas telas acima ("na prateleira, isso vira um aquecedor de
200 W"). O que mentia era o **rótulo**: um título dizendo "Aquecedores que atendem essa potência" sobre
um aparelho que a linha ao lado declara fora da faixa é contradição na cara do leitor.

A C5 subiu para **1.4.0**, e tudo o que mudou é rótulo. A lista se parte em dois grupos com cabeçalho e
frase próprios — "Dentro da faixa calculada — 110 a 160 W" e "O degrau comercial acima — 200 W", este
dizendo por que ele está ali e o que a sobra de potência significa num aparelho com termostato. O cartão
sem link de loja parou de dizer "aparece aqui porque atende ao seu número" quando o aparelho é o degrau
acima. O cartão do degrau acima diz "acima dos" em vez de "contra os", porque o desacordo já foi
explicado no título do grupo e repetir "contra" faria a página parecer estar se desdizendo.

**E o lado que quase escapou: a tabela pré-renderizada.** É ela que um modelo de linguagem lê sem
JavaScript, e é dela que sai a citação fora de contexto. A tabela escolhe o modelo mais próximo do topo
da faixa, e em **2 das 6 linhas** (30 L e 60 L) o mais próximo é justamente o degrau comercial acima.
A célula agora diz isso, e o cabeçalho da coluna deixou de prometer "que atende".

**A ordem não mudou, e nenhuma fórmula, constante ou faixa foi tocada.** Continua sendo a distância até
o topo da faixa dentro de cada grupo, e quem cabe na faixa vem antes. Comissão não ordena nada (V16).

### O que ficou como portão, e não como conserto

Três consertos, três portões — porque conserto sem portão volta:

- `ferramentas/gerar-metas-descricao.py --conferir` reprova se o snippet estiver fora de dia com as
  descrições, ou se alguma sair da faixa de caracteres.
- `ferramentas/conferir-slugs.py` reprova artigo linkado sem data e página linkada com data.
- O **caso 15b** do `teste-navegador-c5.mjs` reproduz a entrada exata do despacho (108 L, mínima 16 °C,
  alvo 26 °C, 220 V, tampado) e lê a **ordem do DOM**: nenhum cartão acima do teto pode estar sob
  cabeçalho que diz "atendem", todo cartão acima tem que estar sob o do degrau comercial, quem cabe na
  faixa vem antes, e o cartão acima não repete as frases de quem cabe.

### Verificação

`php -l` nos 10 snippets; proteção de funções ok nos 10; `teste-seo-tecnico` com **177 afirmações**
(eram 28) e zero falha, incluindo o HTML que sai impresso no `<head>`; `teste-apelidos` 59/0;
`teste-conversor-markdown` 17/0; `teste-atualizador-sync` 9/0; `conferir-entidades` zero falha nas
cinco calculadoras; `teste-navegador-casca` inteiro em Chromium; `teste-navegador-c5` com os 15 casos
antigos mais o 15b, console limpo; `teste-navegador-visibilidade-ia` nas cinco calculadoras com o
JavaScript **desligado**, tudo passou; validadores de produto (78 produtos, 0 erro) e de espécie (36
espécies, 0 erro). No ar, depois do Sync: revisão 35 no `/status`, 13 de 13 URLs em 200, zero `&#038;`
dentro de `<script>`, corpo nunca começando por metadado YAML.

**A ronda seguinte é quem aprova.** Quem constrói não aprova o próprio conserto — foi por confundir
isso que cinco calculadoras ficaram horas quebradas no ar em 08/09.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança: nenhum produto entrou nesta execução e nenhum dos três blocos tocou em catálogo. Desses
39, **7 estão sem anúncio achado na plataforma** (o campo `motivo` diz "sem anúncio" ou que a busca não
encontrou) e **32 só aguardam a Sentinela estratégica gerar o link** — para esses a loja existe. Esta é
a leitura que substitui o número "20 sem loja possível", **VENCIDO** desde 09/09 porque foi medido
quando a Shopee era o único programa; refazer a medição de verdade exige o painel do Mercado Livre
aberto, e isso continua sendo da Sentinela estratégica.

### Próximo passo desbloqueado

1. **T8 — a vitrine, começando pela C3.** Agora é o maior bloco de construção que sobrou e não cria URL
   nova, então respeita o item 5 do despacho (nenhuma página nova até 16/09). A C3 é a que tem mais
   itens com foto e link.
2. **T1 — medir a indexação no Search Console.** Continua dependendo do Chrome do Raphael ou da
   credencial da conta de serviço no ambiente. É ele que autoriza ou barra a T4, e a leitura de 16/09
   depende dele para dizer por que a leva de 08/09 não indexou.
3. **A `Organization` com `sameAs` na home** segue pendente de propósito, pelo mesmo motivo de sempre:
   a Aquametria não tem perfil externo nenhum, então `sameAs` sairia vazio ou inventado. Nasce quando o
   T6 der o primeiro perfil externo real.
4. **T3 (catálogo) segue barrado da nuvem** enquanto o egresso bloquear sites de fabricante.

---

## EXECUÇÃO DE 10/09/2026, 19h17Z — T8: a VITRINE nasce na C3

Bloco entregue: **T8, a vitrine de produto**, na C3. É a primeira vitrine do Arquipélago inteiro, e a
C3 veio primeiro porque é a calculadora com mais itens de banco com foto **e** link ao mesmo tempo —
sem isso a vitrine nasceria como um layout bonito sem nada para mostrar.

O despacho da Sentinela de 10/09 não pedia nada de código nesta execução: os itens 1, 2 e 3 foram
cumpridos na execução das 17h15Z e aguardam a conferência da ronda seguinte. O item 4 é registro de
receita (reportado no fim desta entrada) e o item 5 proíbe página nova até 16/09 — **o T8 não cria
URL nenhuma**, e por isso é o maior bloco de construção que cabia hoje.

### O que a vitrine é, e por que ela não é a lista que já existia

A lista de produtos da C3 já era boa: ficha técnica completa, procedência com endereço e data,
elegibilidade dupla. Mas ficha técnica é o que convence **depois** que a pessoa decidiu comparar. O
que faltava era o que convence antes — e no celular, onde a ficha ocupa três telas, "antes" é a única
chance que existe.

A vitrine é um carrossel de cartões, `scroll-snap` em CSS puro, sem biblioteca nenhuma. Cada cartão
carrega foto, marca, modelo, **a especificação que fez o produto entrar** ("1.000 L/h — atende os 190 L
do seu aquário"), a cotação com a data da coleta e o botão da loja. Ela vem **antes** da ficha e antes
da procedência, que é o que o contrato 7 passou a exigir depois da cicatriz da Robometria de 10/09: a
prova de onde veio o número fica, mas ela existe para ser conferida, não para ser o único clique de
compra da página.

### Duas vitrines, porque são dois leitores

A vitrine **pintada** pelo script mostra o aquário de quem está lendo. A vitrine **servida** no HTML,
para o caso de referência de 100 litros, existe pelo mesmo motivo da tabela de exemplos: um modelo de
linguagem e um crawler não executam JavaScript, e vitrine que só nasce no clique é vitrine que só o
comprador que já chegou vê. As duas saem da mesma função de cartão em cada linguagem — duas marcações
para o mesmo cartão viram dois CSS e, mais cedo do que se pensa, duas aparências.

### A decisão que valeu a versão inteira: preço passou a sair, e sai datado

Até a 1.4.0 esta página dizia, em três lugares, que não publicava preço. A razão era boa — preço muda
toda semana e número velho na tela é pior que nenhum — e resolvia o problema errado. **O que o contrato
proíbe (seção 7) é preço CRAVADO COMO ATUAL.** Cotação com a data ao lado é exatamente o que a seção 6
pede da vitrine, e é o que o banco já guardava em `dados/produtos-cotacoes.json` desde 07/09.

As três frases foram reescritas na mesma versão, e não na seguinte. Página que mostra preço e diz que
não publica preço se contradiz — que é a classe de defeito que a C5 acabou de pagar no item 2 do
despacho desta mesma semana.

### O que a medição no ar pegou, e o repositório não pegaria

Depois do Sync da revisão 36, medindo a página **no ar**: a vitrine estava lá, certa, e **duas páginas
de conteúdo continuavam afirmando o contrário**. O corpo da própria C3 dizia "Não publicamos preço
nesta página" três parágrafos acima de cinco cartões com preço, e a página de divulgação dizia "nas
páginas de calculadora não publicamos preço nenhum" e "não usamos foto de loja". Nenhum teste pegaria
isso: os três textos estavam corretos ontem, e nenhuma regra objetiva sabe que hoje deixaram de estar.

Foi a leitura da página como um leitor leria — o que a seção 12 do contrato manda a Sentinela fazer, e
que aqui a Fundação fez sobre o próprio trabalho antes de dar o bloco por entregue. Corrigido na
revisão 37. **A ronda seguinte é quem aprova, como sempre.**

### As três decisões de desenho que valem para a próxima ilha que montar vitrine

1. **Cartão sem link não é link.** O contrato manda que os cartões sejam âncoras de verdade e não `div`
   com `onclick`. Produto sem link de loja não tem para onde apontar, então sai como `div`, com o lugar
   do botão reservado e escrito "link de loja em breve" — que é literalmente o que o contrato 7 manda a
   ferramenta fazer enquanto `afiliado.url` estiver vazio.
2. **Produto sem foto não some.** Sai com espaço reservado neutro, na posição que a adequação técnica
   lhe deu. Neste caso não é hipótese: o primeiro cartão da vitrine servida de 100 L é o Atman HF-0600,
   sem foto e sem link. Perder a recomendação certa por falta de imagem é trocar o certo pelo bonito.
3. **Largura e altura não se inventam.** O banco não mediu as imagens (o egresso da nuvem barra o CDN
   da Shopee) e a Aquametria não grava dimensão que não mediu. Em vez de chutar um par de números para
   satisfazer a letra da regra, o cartão reserva o espaço com `aspect-ratio: 1/1` e `object-fit:
   contain` — o layout não salta qualquer que seja a proporção real, que é a coisa que a regra existe
   para garantir. Quando o banco trouxer medida, os atributos saem sozinhos: o código já os imprime
   quando existem.

### O que NÃO entrou, de propósito

**Não há `Product`/`Offer` no JSON-LD desta página.** `Offer.price` afirma preço ATUAL, e o que temos é
cotação de uma data. Declarar schema de oferta com número velho seria mentir em formato de máquina, que
é pior do que mentir em texto, porque ninguém revisa. O `WebApplication` e o `FAQPage` continuam como
estavam.

**A `og:image` continua fora.** A vitrine não deu à ilha imagem própria hospedada: as fotos são dos
anúncios, servidas pelo CDN da Shopee. `og:image` exige URL absoluta de arquivo nosso, e declarar uma
que não é nossa é pedir para o cartão quebrar no dia em que o anúncio sair do ar.

### Os portões que nasceram junto

Conserto sem portão volta, e vitrine é o bloco da página que mais tenta voltar errado — ela mostra
foto, preço e botão, que são exatamente as três coisas que empurram uma página a vender o que paga mais
em vez do que atende.

- **`ferramentas/teste-navegador-c3-vitrine.mjs`**, 38 afirmações, nas duas metades da página: a vitrine
  SERVIDA com o JavaScript **desligado** e a PINTADA com ele ligado. A afirmação central é que **a ordem
  da vitrine seja idêntica à da lista técnica** — se um dia alguém ordenar a vitrine por comissão, por
  preço ou por "quem tem foto", o teste reprova. Ele não guarda número esperado nenhum: lê
  `AQM_C3_CATALOGO` e confere a tela contra o dado.
- **O gerador do catálogo recusa gravar imagem sem `alt`** e para se achar qualquer chave de comissão
  viajando para dentro do snippet. Comissão não aparece na tela e não ordena nada — agora isso é
  verificado, não prometido.
- Mede também o celular em 390 px: rolagem até o resultado **só no envio explícito** (sequestrar a
  rolagem de quem acabou de abrir a página é o oposto de ajudar), barra fixa enquanto o resultado está
  fora da tela, barra sumindo quando ele entra e desligando no botão Limpar.

### Um teste que precisou de conserto, e o motivo importa

O `teste-navegador-cinco.mjs` reprovou a C3 com seis `ERR_TUNNEL_CONNECTION_FAILED` — as cinco fotos da
Shopee e uma fonte. Ele já filtrava `ERR_CONNECTION`, `ERR_NAME` e `ERR_INTERNET`; nunca tinha visto a
variante do proxy porque nenhuma página da ilha carregava imagem externa antes de hoje. O filtro foi
estendido, e só para erro de rede: erro de script continua reprovando. Quem confere que a URL da foto é
a do banco é o teste da vitrine, por dado; quem confere que a imagem **abre** é a Sentinela Técnica, no
Chrome. Deixar o erro ali faria o teste reprovar todo dia por um motivo que não é defeito — e teste que
reprova sempre é teste que ninguém lê.

Uma afirmação do `teste-navegador-visibilidade-ia.mjs` foi **renomeada**, não afrouxada: chamava-se "o
aviso da tabela explica por que não publica preço" e media, na verdade, que o aviso não fica mudo sobre
preço. Deixou de ser verdade no nome quando a C3 passou a publicar cotação datada. Nome de teste treina
a próxima sessão.

### Verificação

`php -l` nos 10 snippets; proteção de funções ok nos 10 (47 funções na C3); `teste-seo-tecnico` 177/0;
`teste-apelidos` 59/0; `teste-conversor-markdown` 17/0; `teste-atualizador-sync` 9/0; `teste-escape-shortcode`
ok; `conferir-entidades` zero falha nas cinco; `conferir-slugs` ok nos dois sentidos;
`gerar-metas-descricao --conferir` em dia com as 13; validador de produtos 78/0 erro; validador de
espécies 15/0. No navegador, um teste de cada vez: `c3-vitrine` 38/0, `c3-dupla-condicao` tudo passou,
`visibilidade-ia` nas cinco com JavaScript desligado, `cinco`, `casca`, `c1-tabela`, `c5`, `c12`, `c15`
e `artigos` — todos passaram.

No ar, depois do Sync: **revisão 37 no `/status`**, igual à do manifest; **13 de 13 URLs do sitemap em
HTTP 200, nenhum redirecionamento**;
**zero `&#038;` dentro de `<script>`** (12 blocos; as 4 ocorrências da página inteira são da casca do
tema, e contar na página inteira é teste errado); o corpo começa pela linha de promessa e não por
metadado YAML; o script vem do rodapé; a tabela de exemplos e a vitrine servida aparecem no HTML
servido, com 7 cartões, 5 âncoras `sponsored noopener` em aba nova, 5 imagens com `alt` e
`loading="lazy"`, 2 espaços reservados e 5 cotações datadas.

### Produtos esperando link de afiliado: 39 de 78

Sem mudança no total: nenhum produto entrou no banco nesta execução. Desses 39, **7 estão sem anúncio
achado na plataforma** e **32 só aguardam a Sentinela estratégica gerar o link** — para esses a loja
existe. No catálogo da C3 especificamente, **8 dos 13 filtros esperam link**, e o banco tem foto para
32 dos 78 produtos.

**Item 4 do despacho, medido de novo com a vitrine no ar:** o topo continua sem link de loja. Na vitrine
servida de 100 L o primeiro cartão é o Atman HF-0600, sem link e sem foto, e os dois seguintes com link
vêm depois. **A ordem não mudou e não vai mudar por isso** — o desbloqueio é banco melhor ou segundo
programa de afiliado, e isso é decisão do Raphael. O que a vitrine acrescentou ao problema é que agora
ele é visível: o cartão sem link mostra "link de loja em breve" no lugar do botão, em vez de o leitor
descobrir a ausência depois de rolar a ficha inteira.

### Próximo passo desbloqueado

1. **T8 nas outras calculadoras**, na ordem C5, C15, C12 — a C5 é a que tem mais itens com foto e link
   depois da C3 (11 dos 14 aquecedores com link têm foto). O código da vitrine é o mesmo desenho, e as
   três frases de preço de cada uma se reescrevem junto com ela, nunca depois.
2. **T1 — medir a indexação no Search Console.** Continua dependendo do Chrome do Raphael ou da
   credencial da conta de serviço no ambiente. É ele que autoriza ou barra a T4, e a leitura de 16/09
   depende dele para dizer por que a leva de 08/09 não indexou.
3. **Acentuar o `alt` das imagens dos outros bancos.** O `alt` é texto de tela — leitor de tela lê,
   crawler lê — e nos bancos de aquecedor, iluminação e mídia ele ainda está sem acento, como estava no
   de filtros até hoje. Vai junto com a vitrine de cada calculadora, porque cada mudança de banco pede
   regerar e reverificar o snippet daquela calculadora.
4. A `Organization` com `sameAs` na home segue pendente de propósito: a Aquametria não tem perfil
   externo nenhum. Nasce quando o T6 der o primeiro.

---

## EXECUÇÃO DE 10/09/2026, 21h17Z — T8: a VITRINE chega à C5, e a regra de reserva de ilha funcionou pela primeira vez

### A execução começou perdendo uma corrida, e isso é notícia boa

Pela seção 1 do `ARQUIPELAGO.md`, a ilha desta execução seria a **Robometria**: `ultima_execucao` mais
antiga (17h17Z) e `prioridade: 1`. A reserva foi escrita, commitada e o push foi **recusado** — outra
execução tinha reservado a mesma ilha às 21h15Z, um minuto antes. O procedimento da regra 5 foi seguido
à risca: `reset --hard` no commit da reserva, releitura dos cabeçalhos, e a ilha passou a ser a
**Aquametria** (19h17Z, a mais antiga das que sobraram). **É a primeira vez que a reserva por commit
impediu duas execuções de trabalhar na mesma ilha**, e ela impediu do jeito mais barato possível: quem
perde a corrida do push não conserta nada, só escolhe outra ilha. Fica registrado que o mecanismo é
real, e não teoria.

### O que foi entregue: C5 v1.5.0, manifest revisão 38

A **vitrine de produto nasce na calculadora de potência do aquecedor** — a segunda do Arquipélago,
depois da C3. Carrossel de cartões em `scroll-snap` de CSS puro, sem biblioteca, com foto, marca,
modelo, a especificação que fez o produto entrar, a cotação **com a data da coleta** e o botão de loja.
Vem **antes** da ficha técnica e da procedência (contrato 7). Duas vitrines por página: a pintada,
dentro do resultado, e uma **servida no HTML** para o aquário de referência de 100 L, que é o que um
crawler de IA recebe.

Vieram junto, na mesma versão, três coisas que a seção 6 do contrato pedia e esta página não tinha:
a **linha de promessa** antes do formulário, a **barra fixa do celular** enquanto o resultado está fora
da tela, e a **rolagem até o resultado** ao calcular — o mesmo desenho da C3, portado com o
`IntersectionObserver` e o `prefers-reduced-motion` incluídos.

### O que a C5 tem e a C3 não tinha, e é a lição desta execução

**A lista da C5 é partida em dois grupos** desde a 1.4.0 — "Dentro da faixa calculada" e "O degrau
comercial acima" —, e um cartão de vitrine não comporta cabeçalho de grupo: enfiar um `<h4>` dentro de
um trilho horizontal quebraria o `scroll-snap`. Copiar a C3 de olhos fechados teria produzido cartões
bonitos dizendo "atende os 108 L do seu aquário" sobre um aparelho que a linha ao lado declara **fora**
da faixa — ou seja, teria **reencenado em foto e botão de loja** exatamente a contradição que o item 2
do despacho da Sentinela mandou consertar nesta mesma semana.

A saída foi pôr a distinção na frase do próprio cartão: quem cabe diz *"150 W — dentro dos 110 a 160 W
que os 108 L pedem"*; o degrau acima diz *"200 W — degrau comercial acima dos 160 W do topo"*. E a
**sequência é calculada uma vez só** em `pintarProdutos()` e passada para `pintarVitrine()`, em vez de
recalculada dos dois lados: recalcular a mesma ordem em dois lugares é combinar de divergir depois, e
aqui divergir significa um cartão com foto e botão aparecendo antes de quem a ficha técnica pôs na
frente. O portão novo mede isto por afirmação própria — o **grupo** de cada cartão tem de ser o mesmo
que a lista técnica deu a ele.

### O número que o PROMPT.md tinha errado, e por quê

O `PROMPT.md` justificava a C5 como a próxima da fila porque "11 dos 14 aquecedores com link têm foto".
O número está certo e a conclusão estava errada: ele foi medido no **banco**, e a vitrine desenha o
**catálogo**. Dos 27 aquecedores do banco, só **18** passam no `minimo_para_sugerir` — e **9 dos 11 que
têm foto são justamente os que ficam de fora**, por não declararem volume atendido, faixa de ajuste ou
voltagem. Medido depois de regerar: **a vitrine da C5 tem foto em 2 dos 18**, contra 5 de 13 na C3.

Isso não mudou nada na entrega — produto sem foto **não some** da vitrine, sai com o espaço reservado
neutro, porque perder a recomendação técnica certa por falta de imagem é trocar o certo pelo bonito —,
mas muda como se escolhe a próxima calculadora. A regra foi escrita no `PROMPT.md`: **conte foto e link
depois do portão de elegibilidade, nunca antes**, e a medida certa é a linha "vitrine: N de M com link,
K com foto" que os geradores agora imprimem.

### Preço passa a sair, e as frases que diziam o contrário foram reescritas junto

Até a 1.4.0 esta página dizia, em dois lugares, que não publicava preço. A razão era boa — preço muda
toda semana — mas resolvia o problema errado: o que a seção 7 proíbe é preço **cravado como atual**, e
cotação com a data ao lado é o que a seção 6 pede da vitrine. As duas frases foram reescritas **na mesma
versão** em que a vitrine entrou, mais a `conteudo/divulgacao-de-afiliados.md`, que ainda dizia que só a
calculadora de vazão mostrava cotação. Página que mostra preço e diz que não publica preço se
contradiz, e contradição na cara do leitor é o defeito que a 1.4.0 acabou de consertar.

A C12 e a C15 continuam dizendo que não publicam preço, e ali a frase **é verdadeira** — elas ainda não
têm vitrine. Cada uma se reescreve na versão em que a vitrine chegar, nunca depois.

### O gerador do catálogo e o banco

`ferramentas/gerar-catalogo-aquecedores.py` ganhou os dois campos que o gerador dos filtros já tinha, com
os mesmos portões: `imagem` **recusa gravar** URL sem `alt` (imagem sem texto alternativo na vitrine é
defeito de acessibilidade que ninguém vê passar), `preco` sai de `dados/produtos-cotacoes.json` sempre
como faixa com a data **mais antiga** da coleta, e o gerador **para** se achar qualquer chave de
comissão viajando para dentro do snippet. `largura` e `altura` viajam como estão no banco, inclusive
`null`: a Aquametria não grava dimensão que não mediu, e o cartão reserva o espaço com `aspect-ratio`.

Os **11 `alt`** do banco de aquecedores foram acentuados (`submersível`, `aproximação`), como já tinham
sido os do banco de filtros. Faltam os de iluminação e de mídia, e vão junto com a vitrine de cada uma.

Não há `Product`/`Offer` no JSON-LD desta página, e é de propósito: `Offer.price` afirma preço **atual**,
e o que temos é cotação de uma data. Declarar schema de oferta com número velho seria mentir em formato
de máquina, que é pior do que mentir em texto, porque ninguém revisa.

### Verificação

`php -l` nos 10 snippets; proteção de funções ok nos 10 (**47 funções** na C5); `conferir-entidades`
zero falha, com `entidade_038_no_documento=0` nas cinco; `conferir-slugs` ok nos dois sentidos;
`gerar-metas-descricao --conferir` em dia com as 13; `teste-seo-tecnico` 177/0; `teste-apelidos` 59/0;
`teste-conversor-markdown` 17/0; `teste-atualizador-sync` 9/0; `teste-escape-shortcode` ok; validador de
produtos 78 produtos, 0 erro.

No navegador, um teste de cada vez: **`teste-navegador-c5-vitrine.mjs`, o portão novo, APROVADO em 44
afirmações** — as duas metades da página, a servida com o JavaScript **desligado** e a pintada com ele
ligado; **`teste-navegador-c5.mjs` (15 cenários, entre eles o 15b do despacho de 10/09) passou inteiro**;
`teste-navegador-visibilidade-ia.mjs` **155 afirmações, zero falha**, nas cinco calculadoras com o
JavaScript desligado; `teste-navegador-cinco.mjs` **56 afirmações, "tudo passou"** nas cinco.

### No ar, medido depois do Sync

**Revisão 38 no `/status`**, igual à do manifest, aplicada às 21h40Z — 18 itens aplicados, 14 aguardando
desembarque. O Sync precisou de **duas chamadas**: a primeira, às 21h36Z, ainda leu a revisão 37 do
`raw.githubusercontent`, cujo edge servia uma cópia de 260 s (`max-age=300`). Não é defeito, é o cache
duplo da seção 4 do contrato — e fica registrado que **a espera é do lado do raw, não do WordPress**:
o `curl` daqui já via a 38 enquanto o servidor da HostGator ainda via a 37.

A página `https://aquametria.com.br/calculadora-de-potencia-do-aquecedor/` responde **HTTP 200**;
**`softwareVersion` 1.5.0** no JSON-LD; **zero `&#038;` dentro de `<script>`** (12 blocos; as 4
ocorrências da página inteira são da casca do tema, e contar na página inteira é teste errado); o corpo
começa pelo título e pela linha de promessa, não por metadado YAML; o script vem do rodapé; a tabela de
exemplos e a **vitrine servida** aparecem no HTML servido, com **5 cartões**, 1 âncora
`sponsored noopener` em aba nova, 1 imagem com `alt` e `loading="lazy"`, **4 espaços reservados neutros**
e 1 cotação datada. A frase "não publicamos preço" **não existe mais** nesta página.

### Produtos esperando link de afiliado: 39 de 78 no banco, 13 de 18 no catálogo da C5

Sem mudança no total do banco: nenhum produto entrou nesta execução. **No catálogo que a C5 publica, 5
dos 18 aquecedores têm link** e 13 esperam — trabalho da Sentinela estratégica, não da Fundação. Desses
13, todos têm loja possível: são modelos vendidos no varejo brasileiro, só sem link gerado. **Três dos
que já têm link não têm foto** (Roxin HT-1300/Q3 de 100, 200 e 300 W): são os avisos V20 do validador, e
a URL da foto só sai do painel da Shopee, no navegador do Raphael.

**Item 4 do despacho, medido de novo com a vitrine da C5 no ar:** na entrada do próprio despacho (108 L,
mínima 16 °C, alvo 26 °C) a lista sai com 5 aparelhos e **só o terceiro tem link** — Atman AT-150 e
Eheim Jäger 150 W vêm antes, os dois sem link, e o Ocean Tech Warmer X-5 150 W é o único com botão de
loja e com foto. **A ordem não mudou e não vai mudar por isso.** O que a vitrine acrescentou é que a
ausência agora é visível no lugar mais caro da página: o primeiro cartão mostra "link de loja em breve"
onde estaria o botão, em vez de o leitor descobrir a falta depois de rolar a ficha inteira.

### Próximo passo desbloqueado

1. **T8 na C15, depois na C12.** Antes de escolher, rode o gerador daquele banco e leia a linha
   "vitrine: N de M com link, K com foto" — a lição desta execução é que essa conta só vale **depois**
   do portão de elegibilidade. As frases de preço daquela calculadora se reescrevem na MESMA versão da
   vitrine, e o `alt` daquele banco se acentua **antes** de regerar o catálogo.
2. **T1 — medir a indexação no Search Console.** Continua dependendo do Chrome do Raphael ou da
   credencial da conta de serviço no ambiente. É ele que autoriza ou barra a T4, e a leitura de 16/09
   depende dele para dizer por que a leva de 08/09 não indexou.
3. **Item 5 do despacho continua de pé:** nenhuma página nova até 16/09. Esta execução não criou URL
   nenhuma — a vitrine e a barra do celular moram dentro de páginas que já existiam.
4. A `Organization` com `sameAs` na home segue pendente de propósito: a Aquametria não tem perfil
   externo nenhum. Nasce quando o T6 der o primeiro.

## 2026-09-11 11h16Z — Bloco T8 na C15: a terceira vitrine do Arquipélago, e um defeito de rótulo que só apareceu lendo a página

**O bloco.** A vitrine de produto chegou à calculadora de iluminação (C15 v1.3.0,
manifest na revisão 39). Mesmo desenho da C3 e da C5, copiado e não reinventado:
uma função de cartão em PHP (`aquametria_c15_vitrine_cartao_html`) e o espelho
dela em JavaScript (`vitrineCartao`), com a MESMA marcação; duas vitrines por
página — a pintada dentro do resultado e a **servida** no HTML, porque crawler de
IA não executa JavaScript; e a vitrine **antes** da ficha e da procedência
(contrato 7). A sequência é calculada UMA vez em `pintarProdutos()` e passada
para `pintarVitrine()`: calculador de ordem duplicado é combinar de divergir
depois.

**O ACHADO, e é o que vale mais que a vitrine.** Lendo o resultado como um leitor
leria — que é o único jeito de pegar este tipo de coisa — a C15 se contradizia no
cartão da lista técnica, no ar desde a 1.2.0. O nível de **alta exigência tem a
faixa ABERTA por cima**: a fonte aquarioturbinado publica "acima de 40 lm/L" e
não diz até onde, então o filtro aceita qualquer fluxo acima do piso. Só que a
frase do cartão dizia, para TODO mundo que passasse, "fica dentro da faixa de 40
a 60 lm/L que este nível pede" — e num aquário de 60 cm com 57,6 L a Chihiros
WRGB-II Pro 60 entrega **115,1 lm/L**. Afirmar que 115 está dentro de 40 a 60 é a
contradição do item 2 do despacho da Sentinela de 10/09 em outra roupa.

**A elegibilidade NÃO mudou e a ordem NÃO mudou** — a mesma escolha que a C5 fez
em 10/09, e pelo mesmo motivo: a régua estava certa, o rótulo é que mentia. A
lista passou a ter dois grupos, "dentro do intervalo que as três fontes publicam"
e "acima do teto da leitura mais alta, na parte da faixa que a fonte deixou
aberta", cada um com a frase que diz a verdade sobre ele, e quem cai no segundo
**mostra o lm/L que realmente entrega**. O grupo também foi para o DOM
(`aqm-c15-produto-acima`), que é por onde o portão confere se o cartão da vitrine
diz o mesmo grupo que a lista técnica. A distinção viaja na frase do cartão
porque trilho de `scroll-snap` não comporta cabeçalho de grupo — lição da C5,
copiada.

**Preço passou a sair, e sai datado.** As duas frases do snippet que diziam "não
publicamos preço" foram reescritas na MESMA versão, mais a página
`conteudo/calculadora-de-iluminacao.md` e o parágrafo da
`conteudo/divulgacao-de-afiliados.md`: página que mostra preço e diz que não
publica preço se contradiz. O que a seção 7 proíbe é preço **cravado como atual**;
cotação com data ao lado é o que ela permite. Continua sem `Product`/`Offer` no
JSON-LD, de propósito: `Offer.price` afirma preço de hoje, e o que temos é
cotação de uma data — mentir em formato de máquina é pior, porque ninguém revisa.

**Vieram junto as três dívidas da seção 6** que a C5 pagou em 10/09: linha de
promessa antes do formulário, barra fixa do celular enquanto o resultado está
fora da tela, e rolagem até o resultado ao calcular.

**A ESCOLHA DO AQUÁRIO DE REFERÊNCIA VIROU CONTEÚDO, porque calar o motivo seria
colher cereja.** A vitrine servida usa um aquário de 90 × 45 × 45 cm (170 L) em
alta exigência, e o parágrafo abaixo dos cartões diz por quê: varrendo os seis
aquários da tabela nos três níveis, **este é o único caso em que três luminárias
do banco cobrem o vidro E caem dentro do intervalo publicado**. Nos níveis baixo
e médio a lista sai vazia em quase todos os tamanhos — não porque a conta erre,
mas porque o catálogo brasileiro de luminária com lúmen declarado é curto
justamente na faixa de 10 a 40 lm/L. Isso é **faixa descoberta medida** (seção
14.3) e é a lista de compras do banco de iluminação, não estatística. Medido
célula a célula (seis aquários × três níveis = 18 células): **9 das 18 têm algum
produto**, e **1 única** tem três ou mais DENTRO do intervalo publicado — a de
90 cm em alta exigência, que é por isso a referência da vitrine servida. Das
outras oito não vazias, quatro só têm itens acima do teto da leitura mais alta,
e três têm um produto só. **Nenhuma célula de nível baixo tem produto abaixo de
120 cm.**

**O gerador ganhou o portão dos outros dois** (`gerar-catalogo-iluminacao.py`):
`imagem` só viaja com URL **e** `alt` — url sem alt PARA o gerador —, `preco` vem
de `produtos-cotacoes.json` como faixa com a data mais antiga, e qualquer chave
de comissão no item barra a gravação. Os 10 `alt` do banco de iluminação foram
**acentuados** (a dívida que o PROMPT registrava; falta agora só o de mídia).

**MEDIDO, e corrige de novo o mesmo erro de leitura que a C5 ensinou:** a vitrine
da C15 tem **4 de 15 com link, 2 com foto, 4 com cotação datada**. O banco de
iluminação tem 10 registros com foto — mas 8 deles são as Soma, que não declaram
lúmen e por isso nem chegam ao catálogo. Conte foto e link **depois** do portão
de elegibilidade; a linha "vitrine: N de M" no fim do gerador existe para isso.
**11 das 15 luminárias do catálogo esperam link de afiliado.**

**Receita (item 4 do despacho de 10/09, que é registro e não pedido de mudança de
ordem).** No caso do teste (60 cm, alta exigência) os três primeiros da lista não
têm link e o quarto tem; na vitrine servida (90 cm, alta) o primeiro não tem e o
segundo tem. O topo continua sendo o espaço mais caro da página. Nenhum dos 11
sem link é "sem loja possível hoje" por impedimento conhecido — todos são Chihiros
e similares vendidos no Brasil; o que falta é a geração do link, que tem teto de
calendário e é da Sentinela estratégica.

**Verificação (seção 8), toda ela antes de dar o bloco por entregue:**
- `php -l` limpo nos 11 snippets; `conferir-protecao-funcoes.py` ok (41 funções
  da C15, todas dentro de `function_exists`); `conferir-slugs.py` ok.
- `validar-produtos.py`: 78 produtos, 39 cotações, **0 erro**, 9 avisos (todos
  V20/V14/V11 já conhecidos).
- `teste-navegador-c15-vitrine.mjs`, **novo, 55 afirmações, tudo passou**.
- `teste-navegador-c15.mjs`: **78 afirmações, tudo passou**.
- `teste-navegador-visibilidade-ia.mjs`: **155 afirmações**, tudo passou.
- `teste-navegador-cinco.mjs`: **56 afirmações**, tudo passou.
- Zero `&#038;` DENTRO de `<script>` (medido nos blocos `<script>`, não na página
  inteira); `&amp;` `&lt;` `&gt;` `&quot;` uma vez cada, que é o `esc()` da própria
  calculadora.
- 0 px de rolagem horizontal a 390 px, com a página medida em **155 KB** — a
  asserção de tamanho entrou no teste justamente por causa da cicatriz da
  Robometria: render de bancada que serve metade mede 0 px por não ter o que
  estourar.

**TRÊS TESTES NEGATIVOS, porque teste que mede a si mesmo é teste verde que não
mede nada:** (1) o rótulo voltando a dizer "dentro dos" para todo mundo — três
portões reprovaram, e a saída mostrou literalmente "6.630 lm — 115,1 lm/L, dentro
dos 40 a 60 lm/L", que é o defeito que estava no ar; (2) a vitrine reordenando
para pôr quem tem link na frente — o portão central reprovou; (3) o produto sem
foto sumindo da vitrine servida — reprovou por sobrar menos de três cartões.
Mais um no gerador: apagar o `alt` da A901 fez o script recusar gravar.

**Um caso de teste errado foi corrigido no caminho, e a correção é informação:**
a primeira versão do portão de lista vazia usava "60 cm no nível médio". Reprovou
com razão — ali a lista fica sem ninguém DENTRO da faixa, mas ainda tem os
**reguláveis**, que são modelos acima do teto com dimmer declarado. Lista vazia de
verdade é outra coisa, e o caso passou a ser um aquário de 115 cm, que nenhuma
luminária do banco declara cobrir.

**Uma trava de teste foi afrouxada, e só depois de medir:** `ERR_TUNNEL` e
`ERR_PROXY` entraram na lista de erros de rede que o `teste-navegador-c15.mjs`
ignora, ao lado de `ERR_CONNECTION`/`NAME`/`INTERNET` que já estavam lá desde
08/09. Motivo medido: as ÚNICAS duas requisições que falham nesta página são a
folha do Google Fonts (que vem da casca) e a foto da A901 no CDN da Shopee (que a
vitrine servida pede) — as duas de domínio externo, as duas fora do alcance da
nuvem, as duas vivas no navegador do Raphael. `pageerror` continua reprovando
sempre, e nenhum outro tipo de erro é filtrado.

**Próximo passo desbloqueado:** T8 na C12 (mídia filtrante), que é a última da
fila de vitrines — na C1 provavelmente não nasce, porque litragem é geometria e
geometria não escolhe produto. Antes dela, acentuar os `alt` do banco de mídia e
copiar para `gerar-catalogo-midias.py` o mesmo portão de `alt`/`preco`/comissão
que os outros três geradores já têm. E fica anotado para o T3: a **faixa
descoberta de 10 a 40 lm/L** do banco de iluminação é a lista de compras de
catálogo mais urgente desta entidade, medida célula a célula neste bloco.

**NO AR E CONFERIDO (seção 4 do `ARQUIPELAGO.md`), 11/09/2026 12h21Z.** A nuvem
alcançou o domínio: `curl` no Sync devolveu **revisão 39, 18 aplicados, 14
aguardando desembarque**, e o `/status` confirma `revisao: 39`, **igual à do
manifest**. Medido na URL no ar (`/calculadora-de-iluminacao/?v=1226`, com
quebra-cache):
- **HTTP 200**, 216 KB servidos.
- **Zero `&#038;` DENTRO dos 12 blocos `<script>`** — e 4 na página inteira, que
  é justamente por que contar na página inteira é o teste errado. `&amp;` `&lt;`
  `&gt;` `&quot;` uma vez cada dentro do script: é o `esc()` da calculadora.
- O corpo começa por texto ("Pular para o conteúdo… Calculadora de iluminação e
  fotoperíodo: quantos lúmens o seu aquário pede"), **nunca por metadado YAML**.
- O script vem do **rodapé**, depois de todo o conteúdo do shortcode.
- A **tabela de exemplos** e a **vitrine servida com 3 cartões** aparecem no HTML
  servido; a vitrine servida vem **antes** do quadro de fontes e a pintada vem
  **antes** da lista técnica (contrato 7).
- Rodapé diz **versão 1.3.0**; `<meta name="description">` presente; JSON-LD
  presente; **zero ocorrência de "não publicamos preço"** e **1 cotação datada**.
- Os três cartões servidos dizem, cada um, o lm/L que entregam: 49,4 / 48,2 /
  54,4 lm/L, os três dentro dos 40 a 60 publicados — que é o que o grupo de cima
  significa agora.

## 2026-09-11, 15h16Z — A VOZ CHEGA À HOME E AO HEADER (casca 1.4.1, revisão 42)

**Bloco:** despacho do Raphael de 11/09/2026, seção 15 do `ARQUIPELAGO.md` — prioridade máxima, antes de qualquer bloco da fila. Junto veio o item (i) do 16.8: o `ARVORE.md` da ilha.

### O que mudou na tela

- **A home parou de abrir pelo manifesto.** Até a 1.3.1 a primeira linha era *"A Aquametria dimensiona aquário com número que tem fonte"*. A frase não era falsa; ela falava da fábrica para a fábrica. Agora a home abre pela pergunta mais frequente da ilha — *"Quantos litros tem o seu aquário?"* — com as três medidas nomeadas, porque quem chega aqui chegou com uma fita métrica na mão.
- **Os oito cartões viraram a pergunta que a pessoa digita.** "Potência do aquecedor por delta térmico" virou "Quantos watts de aquecedor você precisa?"; "Vazão do filtro e turnover" virou "Qual filtro dá conta do seu aquário?". **Nenhum código, slug ou URL mudou** — a seção 12.1 proíbe mover endereço de página publicada, e este bloco não moveu nenhum.
- **Nasceu a prateleira de guias**, no fim da home, no molde GUIA do `VOZ.md`.
- **O menu diz "Como a gente calcula"** no lugar de "Metodologia", e o título das quatro páginas da casca passou a ser sincronizado — só nas que carregam `_aquametria_casca`, e sem tocar em `post_name`.

### As três decisões de desenho que valem para as outras ilhas

**1. A prateleira de guias não guarda cópia de título nenhum.** A casca pergunta pelo filtro `aquametria_guias` e quem responde é o snippet dos artigos. Guia novo aparece na home sozinho. É a mesma escolha do hub de calculadoras, e existe pela cicatriz de 11/09: o número digitado que era verdade no dia em que foi escrito e virou mentira em silêncio no dia em que o banco cresceu. A frase "5 de 8 já estão no ar" é contada, e o portão conta de novo e compara.

**2. A camada de prova se declara no MARKUP, não se adivinha pela vizinhança.** "Procedência" é palavra proibida na voz e obrigatória na prova, e as duas são a mesma palavra. A saída não é heurística melhor: a página marca a prova com a classe `aqm-prova`, o portão **retira** esses blocos e proíbe o termo em todo o resto. Para a declaração não virar porta dos fundos, os blocos marcados são contados (no máximo dois por página), nenhum pode conter o H1 ou o primeiro parágrafo, e nenhum pode abrir a página. É a lição do Clube do Mosaico aplicada antes de doer aqui.

**3. A régua do portão mora no portão.** `teste-voz.mjs` escreve a própria lista de termos proibidos, à mão, a partir do `VOZ.md`. Ela não é importada de um JSON que o snippet também leia — se as duas metades lessem a mesma lista, apagar um termo dela faria as duas errarem juntas e o teste continuaria verde. E toda afirmação sobre o que a página diz é medida **no corpo**, entre `<main>` e `</main>`: no HTML inteiro o termo apareceria dentro do próprio JSON-LD.

### O que a medição achou sem procurar

**O `<title>` da home vinha da tagline do WordPress, e nunca ninguém a tinha tocado.** A linha que a pessoa lê no resultado de busca — a mais lida da página inteira — ainda dizia *"Aquametria – Calculadoras e dados técnicos para dimensionar o seu aquário"*, escrita quando a ilha nasceu. Nenhum portão do projeto olhava para ela: o `teste-voz.mjs` da primeira versão media o corpo, e o `<title>` não é corpo. A casca passa a gravar a opção `blogdescription`, na mesma família de `page_on_front`, e a bancada passou a montar o `<title>` **como o núcleo do WordPress monta** — `<nome do site> – <blogdescription>` na home, `<título da página> – <nome do site>` na interna. Bancada que compõe o título de outro jeito é bancada que serve o que o site não serve.

**A tabela de constantes da `/metodologia/` rolava na horizontal no celular, e está no ar assim desde que a página existe.** 67 px a 360 px, 37 px a 390 px. A causa é discreta e vale para toda ilha: o conversor de Markdown do Sync embrulha **toda** tabela vinda de `conteudo/` num bloco que rola, mas esta tabela é impressa direto pelo shortcode e por isso nunca passou por lá. Nenhum teste do projeto media largura nas páginas da casca — o `teste-navegador-casca.mjs` monta o cabeçalho com um corpo falso, de propósito, porque o que ele mede é o menu. **Não foi este bloco que quebrou; foi este bloco que passou a medir.** Consertado na mesma versão, e o gate reprovou antes e passou depois — que é o teste negativo desta trava, observado ao vivo.

**A C15 seria a única a ficar com o texto antigo.** Ela é a única calculadora que sobrescreve o resumo do cartão pelo filtro `aquametria_calculadoras`. Quem lesse só a casca veria os oito cartões reescritos e nunca saberia que um deles é descartado no ar. Achado pela varredura, não pela leitura do código. (C15 v1.3.1, e nada além desse texto mudou nela.)

### Verificação — seção 8 inteira

| portão | afirmações | resultado |
|---|---|---|
| `teste-voz.mjs` (novo) | 86 | 0 falha |
| `teste-navegador-casca-paginas.mjs` (novo) | 28 | 0 falha, **0 px de rolagem nas 24 medições** |
| `mutacoes-voz.py` (novo) | 11 mutações | **11 reprovadas** |
| `teste-navegador-casca.mjs` | 43 | 0 falha |
| `teste-navegador-cinco.mjs` | 56 | 0 falha |
| `teste-navegador-visibilidade-ia.mjs` | 155 | 0 falha |
| `teste-navegador-artigos.mjs` | 108 | 0 falha |
| `teste-seo-tecnico.php` | 177 | 0 falha |
| `conferir-slugs.py` · `validar-produtos.py` · `conferir-protecao-funcoes.py` | — | 0 erro |

`php -l` limpo nos dez snippets. Corpo medido: home 3.760 caracteres, `/calculadoras/` 2.495, `/metodologia/` 4.249, `/sobre/` 1.616 — as quatro acima do piso de ~1.500 da seção 8.

**A mutação que mais vale é a número 3**, a porta dos fundos: embrulhar a home inteira na classe que declara camada de prova. Ela não escreve nada de errado na tela — só desliga a regra. Se passasse, a marca `aqm-prova` valeria zero.

### O `ARVORE.md`

Quatro seções de nível 1 (`/calculadoras/`, `/peixes/`, `/equipamentos/`, `/guias/`), as categorias de nível 2 com o nome que a pessoa usa, e o pai de cada página existente. **Nenhuma categoria tem hoje as 3 filhas com dado real que a 16.5 exige**, então nenhuma nasce agora — e duas travas independentes de calendário (item 5 do despacho da Sentinela e o T2 deste `PROMPT.md`) seguram qualquer URL nova até a leitura de 16/09. O arquivo diz isso por escrito, com a ordem das levas para quando destravar.

### Receita e pendências

- **39 dos 78 produtos esperam link de afiliado.** Quem gera é a Sentinela estratégica, no navegador do Raphael.
- Item 4 do despacho de 10/09 (o topo da lista sem link de loja) e item 5 (nenhuma página nova até 16/09) continuam de pé, e este bloco não criou nenhuma URL.
- As páginas de `conteudo/` ainda falam na voz antiga: elas são reescritas ao passar pela ronda, como manda a 15.5.

**Próximo passo desbloqueado:** breadcrumb com `BreadcrumbList` e blocos "Veja também" (16.4) em toda página que já existe. Nenhum dos dois cria URL, então os dois cabem antes de 16/09. O breadcrumb nasce com o nível 2 em texto, sem link, porque a categoria ainda não existe — estado de transição declarado no `ARVORE.md`, não desenho.

## 2026-09-11, 17h38Z — A arvore da secao 16 chega as treze paginas no ar

**Entregue:** `snippets/aquametria-casca.php` v1.5.0, manifest na revisao 43,
`/status` respondendo 43 e as treze URLs abertas e medidas no ar as 17h37Z.
Fecha o que o despacho do Raphael de 11/09 deixou de pe depois do bloco da voz
— e fecha **sem criar uma URL**, que era a condicao para caber antes da leitura
de 16/09.

- **A TRILHA, em doze das treze.** A home nao tem, como manda o 16.3. O nivel 2
  sai em TEXTO enquanto a categoria nao existe: e o estado de transicao que o
  `ARVORE.md` ja declarava, e nao ha nada a lembrar no dia em que ela nascer,
  porque quem resolve o endereco de todo degrau e `url_se_existir()`.
- **O BREADCRUMBLIST PUBLICA MENOS QUE A TELA, DE PROPOSITO.** Numa calculadora
  a trilha na tela mostra quatro degraus e o schema publica tres, sem a
  categoria. Nao e esquecimento e foi a decisao mais dificil do bloco: um
  `ListItem` do meio sem `item` invalida a lista inteira para o Google, e lista
  invalida e lista ignorada — o schema "mais completo" publicaria **menos** com
  cara de publicar mais. A mutacao 4 e exatamente essa porta dos fundos, e o
  portao amarra os itens do schema aos degraus LINKADOS da tela, para a relacao
  nao poder derivar em silencio.
- **AS IRMAS SAO DERIVADAS, NUNCA DIGITADAS.** De 2 a 4 por pagina (16.4c),
  tiradas do mesmo registro que alimenta o hub, com afinidade declarada: mesma
  categoria primeiro, ordem do mapa depois. Lista escrita a mao envelheceria no
  dia em que a proxima calculadora entrasse no ar — e a frase que linka a mae
  (16.4b) traz a contagem **contada**, conferida contra os cartoes com link do
  hub, nunca perguntada ao snippet.
- **O GUIA AINDA NAO TEM FRASE DE MAE, e o portao cobra a AUSENCIA dela.**
  `/guias/` nao existe; frase apontando para la seria link morto. Cobrar a
  ausencia e o que impede a proxima execucao de "consertar" isso com um
  endereco inventado — a mutacao 14 e essa tentacao, e ela reprova.

**A BANCADA MEDIA METADE DA PAGINA.** Nasceu `ferramentas/render-pagina-completa.php`
porque dos tres renderizadores que havia, um montava so as quatro paginas da
casca e os outros dois montavam corpo **sem cabecalho e sem H1** — e a trilha
nasce justamente entre o cabecalho e o H1. Medir a arvore em qualquer um dos
tres seria afirmar sobre o que nao existe, que e a cicatriz que a Robometria
pagou tres vezes. Uma pagina por processo, como as outras bancadas desta ilha.

**O QUE AS MUTACOES ACHARAM — e uma delas era buraco de verdade no portao.**
Com cinco calculadoras no ar, **nenhuma pagina chega a ter cinco irmas
candidatas**: trocar o teto de 4 por 5 no snippet nao mudava uma virgula do que
o site serve, e o portao ficava verde nas duas versoes. A faixa "de 2 a 4"
estava sendo conferida contra um mundo que nunca passa de 4 — grade que nao
pisa na borda, so que desta vez a borda nao existia no mundo. A saida foi a
bancada **fabricar** a borda: o modo `todas` do renderizador poe C2, C7 e C8 no
ar, a pagina passa a ter sete candidatas e ai o teto tem o que cortar. E a
unica afirmacao do portao que mede um mundo que nao e o de hoje, e esta
declarada como tal.
Outras tres mutacoes passaram por serem **inertes**, nao por o portao ser cego:
tirar a trava do `render_block` nao duplica nada porque o bloco so renderiza uma
vez na requisicao, e tirar `is_front_page()` nao poe trilha na home porque o
slug da home nao esta na arvore. As tres foram reescritas ate morder de
verdade. **14 de 14 reprovadas** na rodada final.

**UM LIMITE DECLARADO, porque fingir que nao existe seria pior:** se alguem
mudar a categoria de uma calculadora no snippet **e** no `ARVORE.md` na mesma
passada, este portao nao ve — nao ha terceira fonte no repositorio que diga de
que categoria uma calculadora e. Categoria e decisao editorial. As mutacoes 1 e
2 cobrem o caso de UMA das metades mudar, que e o que acontece por descuido.

**VERIFICACAO (secao 8):** `teste-arvore.mjs` 288 afirmacoes com regua propria,
lendo o `ARVORE.md` para cobrar que documento e codigo digam a mesma coisa;
14 de 14 mutacoes reprovadas; 224 medicoes em Chromium nas treze paginas em
360/390/781/782/783/1200 px, **0 px de rolagem horizontal** e console limpo;
`teste-voz`, `teste-seo-tecnico` (177), `conferir-slugs` e
`conferir-protecao-funcoes` sem falha; `php -l` limpo nos 10 snippets.
**No ar as 17h37Z:** 13 de 13 em HTTP 200, 175 afirmacoes medidas no HTML
servido — zero `&#038;` dentro de `<script>` nas treze, trilha sempre antes do
H1 e uma so por pagina, nenhum degrau apontando para pagina inexistente,
`BreadcrumbList` valido nas doze.

**ACHADO REGISTRADO, fora do escopo deste bloco.** A medicao de orfa nasceu
errada e o erro valeu a pena: a primeira versao contava so os links do `<main>`
e reprovou `/sobre/` com zero. O defeito era da **regua**, nao da pagina —
`/sobre/` esta no menu e no rodape das treze, entao o robo acha, que e o que o
16.4(f) existe para garantir. Mas contar a pagina inteira sozinho nao mede nada,
porque o menu faz tres paginas passarem sempre. Viraram duas afirmacoes com
nomes diferentes: o 16.4(f) literal, no HTML servido, para as treze; e a
promessa do cluster, no CORPO, para as oito paginas da arvore. O que fica
registrado e que **`/sobre/` e a unica das treze que nenhum corpo cita** — nao e
defeito desta entrega, e assunto de pauta (secao 17).

**39 dos 78 produtos esperam link de afiliado** (nao mudou: este bloco nao tocou
em catalogo). Nao houve memoria disponivel nesta execucao (`/areas` nao existe
no ambiente); o estado vive no `ESTADO.md` desta pasta.

**Proximo passo desbloqueado:** `pauta.md` (secao 17) ainda nao existe nesta
pasta, entao o proximo bloco que nao cria URL e a **reescrita na voz das paginas
de `conteudo/`**, que o despacho da voz deixou marcada como pendente ("as de
conteudo/ ainda nao foram"). Tudo que cria URL — as oito paginas de nivel 1 e 2,
a troca de pai e de slug, a leva de malha — espera a leitura de 16/09.

## 2026-09-11, 19h44Z — A VOZ CHEGA ÀS NOVE PÁGINAS DE conteudo/, e o título publicado vinha de outro lugar

**Bloco entregue:** casca 1.5.1, artigos 1.2.0, manifest na revisão 48, `/status`
conferido, as treze URLs abertas no ar. Nenhuma URL mudou — a condição da leitura
de 16/09 continua respeitada.

### O que o despacho da voz tinha deixado escrito à mão

"Cada página existente continua sendo reescrita na voz ao passar pela ronda — as
de `conteudo/` ainda não foram." Pendência escrita à mão não é portão, e foi
assim que **as cinco calculadoras seguiram no ar com o H1 começando por
"Calculadora de"** — a única forma de título que o `VOZ.md` proíbe pelo nome — e
**oito dos nove `<title>` passando de 65 caracteres** (120, 128, 97…). Nada disso
precisava de olho humano; precisava de alguém medindo.

### UM NOME POR PÁGINA

O degrau da trilha e o H1 ficam a uma linha um do outro na tela e, em 8 das 9
páginas, diziam nomes diferentes: a trilha dizia "Quantos litros tem o seu
aquário?" e o H1, logo abaixo, "Calculadora de litragem: quantos litros tem o seu
aquário". A casca **já tinha** a voz certa nos rótulos desde 11/09; o que nunca
foi tocado foi o `titulo` das páginas. Então os nove títulos passaram a ser o
rótulo que a casca já publicava — nada foi inventado, uma divergência foi
removida — e existe agora uma afirmação que cobra a igualdade.

Nos três guias os títulos longos com parêntese sumiram e a manchete virou o nome
único. Eles foram escolhidos para **não canibalizar a ferramenta do mesmo
assunto**: o guia do aquecedor é "Por que o 1 W por litro erra para o mesmo lado"
e a ferramenta é "Quantos watts de aquecedor você precisa?" — a ferramenta
responde a pergunta, o guia responde o porquê. Era escolher entre duas opções
defensáveis, e a Fundação escolheu: perde-se a cabeça da consulta no `<title>` do
guia, que continua no slug, nos H2 e na `meta_descricao`.

### PROCEDÊNCIA NÃO ABRE PÁGINA

Os três artigos abriam por fabricante e data de coleta — "Coletadas em 08/09/2026
e atribuídas ao próprio fabricante: Seachem Matrix, 1,25 mL por litro…" — **sem um
único termo da lista de proibidas aparecer**. Lista de palavra não pega isso.

A caixa da resposta direta passou a ter duas camadas: o primeiro parágrafo
responde à pessoa na língua dela, e a procedência desce um parágrafo, **dentro da
mesma caixa**, marcada com `aqm-prova`. A seção 5 continua inteira — quem cita a
caixa leva a fonte junto — e a 15.2 passa a valer. Cinco páginas abriam falando da
internet em vez de falar com quem entrou ("Pergunte na internet brasileira
quantos watts…"); agora abrem pela resposta, em segunda pessoa.

### O DEFEITO QUE SÓ O AR MOSTROU, e era a família inteira

Depois do primeiro desembarque, **168 afirmações medidas no ar acharam o que 293
afirmações verdes na bancada não podiam ver**: o corpo das nove páginas trocou e
**os nove títulos não**.

Duas fontes para o mesmo dado. Quem grava `post_title` é o Sync, e o Sync lê
`titulo` do `manifest.json`; o front matter do `.md` ele nem abre. A bancada
inteira renderizava do `.md`. E `atualizar-manifest.py` só recalculava `sha256` —
`titulo` **nunca** foi reespelhado desde que o arquivo existe. Resultado: bancada
verde, Sync respondendo "18 aplicado(s)", e o H1 e o `<title>` das nove
continuando os de antes.

Três consertos, e o do meio é o que fecha a família e não só este caso:
1. `atualizar-manifest.py` relê o título do front matter e o reespelha, imprimindo
   cada troca (8 nesta passada). O front matter manda.
2. **`render-pagina-completa.php` passou a ler o título do MANIFEST.** A bancada
   agora lê a mesma fonte que o site: manifest atrasado aparece na primeira
   medição, não depois do desembarque.
3. `conferir-slugs.py` cobra manifest == front matter e nomeia a ferramenta a
   rodar. Provado mordendo: com o título velho de volta no manifest, reprova.

De quebra, `render-pagina-completa.php` servia `\&quot;` num H1 que no ar sai com
aspas curvas — o front matter é YAML e a aspa interna vem escapada. Calibrar o
portão da voz nessa string seria medir o que não existe.

### A LISTA DE MUTAÇÕES MENTIU POR UMA RODADA, pelo mesmo motivo

Três mutações editavam o título no `.md` e ficaram **inertes** no instante em que
a bancada mudou de fonte: 18 de 20, verdes sem medir nada. Agora mutam o
manifest, que é a fonte que publica, e as três reprovam pela regra que existem
para medir. Antes disso, outras duas já haviam passado por serem inertes — mutar
o `titulo` do snippet dos artigos não move o H1 (ele vem do front matter), e
trocar meia frase deixava "você" no resto do parágrafo. **Mutação que não morde
não prova nada, e o jeito de descobrir é ela ficar verde.**

### VERIFICAÇÃO

- `teste-voz.mjs`: de **4 para 13 páginas** e de **86 para 293 afirmações**. As
  nove de `conteudo/` montadas pelo `render-pagina-completa.php`, um processo por
  página. Régua nova: procedência não abre página (fabricante e data de leitura
  fora do primeiro parágrafo), degrau da trilha igual ao H1, H1 único na ilha,
  `<title>` ≤ 65, âncora interna pela consulta do destino, segunda pessoa no
  primeiro parágrafo — **com o limite desta última declarado no próprio teste**:
  ela não pega manifesto que diga "você" na primeira linha. Quem julga manifesto
  é a ronda (15.4).
- `mutacoes-voz.py`: de 11 para **20 mutações, 20 reprovadas**.
- `teste-arvore.mjs`, `teste-seo-tecnico.php` (177), `conferir-slugs.py`,
  `conferir-protecao-funcoes.py` (10 snippets) e `validar-produtos.py` (78
  produtos, 0 erro) sem falha. `php -l` limpo nos 10 snippets.
- Chromium: **224 medições** nas treze páginas em 360/390/781/782/783/1200 com 0
  px de rolagem, mais os três artigos no `teste-navegador-artigos.mjs`.
- **NO AR, às 19h44Z:** 13 de 13 em HTTP 200, **160 afirmações medidas no HTML
  servido, 0 falha** — nove H1 novos, nove `<title>` dentro de 65, trilha e H1
  iguais nas nove, nenhum fabricante e nenhuma data no primeiro parágrafo, zero
  `&#038;` dentro de `<script>`.
- 39 dos 78 produtos esperam link de afiliado (**não mudou**; este bloco não tocou
  em catálogo). Pauta da seção 17: `pauta.md` ainda não existe nesta pasta — 0
  temas escritos, 0 na fila, 0 recusados.
- `package.json` entrou na pasta declarando a dependência da bancada
  (`playwright`), que esta execução descobriu pelo erro. O Chromium não se baixa:
  já vem em `/opt/pw-browsers`.

### Próximo passo desbloqueado

A voz fechou em toda página que existe. **Tudo que cria URL continua travado até a
leitura de 16/09** (item 5 do despacho da Sentinela e o T2 deste arquivo), e a
`pauta.md` da seção 17 ainda não existe nesta pasta. Sobram, sem criar URL: o
banco de espécies (T3d), que destrava "quantos litros para X peixes"; o catálogo
de iluminação por faixa (T3a); e a vitrine nas calculadoras que ainda não a têm.
O T3d é o de maior valor porque é o eixo que a Bússola verificou aberto.

## 2026-09-11 (21h) — T3d leva 4: o banco de especies ganhou PROFUNDIDADE, e o canal de coleta ganhou duas regras

Bloco escolhido pela rotacao da secao 1 (a ilha estava com a `ultima_execucao`
mais antiga das tres; nenhuma tinha despacho com item acionavel em aberto — os
que restam na Aquametria e na Robometria sao os travados ate 16/09 e a metade
humana do Search Console). Reserva por commit feita as 21h18Z e aceita no
primeiro push.

**Nenhuma especie nova, e isso foi a decisao.** O banco tinha 36 registros e 12
deles eram barrados no portao de pagina de especie por campo faltando, nao por
falta de peixe. Acrescentar o 37o registro nao destrava nada; fechar campo
destrava. Resultado medido pelo proprio validador: **pagina de especie de 24
para 27 aptos, C8 de 28 para 29**, com 0 erro.

**O que foi colhido (busca RESTRITA ao dominio, niveis 3 e 5 da escada):**

- **Tetra ember** (`hyphessobrycon-amandae`), que era o pior registro do banco:
  o Seriously Fish devolveu, atribuidos a ESTA especie pelo nome, a base minima
  (45 x 30 cm), a faixa de manutencao (20 a 28 C), o cardume (8 a 10) e o
  temperamento. Os tres campos que faltavam fecharam, e com o compendio entrando
  como segundo corpo o E14 fechou junto. O menor peixe do banco (2,0 cm) passou a
  ser tambem o de menor frente declarada (45 cm) — o piso util do eixo "quantos
  litros para X peixes".
- **Peixe-neve** (`tanichthys-albonubes`): segundo corpo de fonte, e duas
  divergencias publicadas em `conflitos[]` em vez de escondidas. A temperatura de
  manutencao desceu de 18–22 para 14–22 C e o cardume subiu de 5 para 10. O
  cardume importa mais do que parece: com 60 cm de frente declarada, 5 peixes dao
  12 cm por individuo e 10 dao 6 cm — a mesma especie com o dobro de densidade,
  dependendo de qual fonte a pagina citar.
- **Peixe-lapis** (`nannostomus-beckfordi`): segundo corpo, registro completo. O
  `observacao` diz com precisao o que o segundo corpo confere (a convivencia, e
  so ela) e o que ele NAO confere — nenhum numero desta ficha foi corroborado
  por um segundo corpo, e isso ficou escrito.

**AS DUAS REGRAS NOVAS, e elas sao do canal, nao do banco.** Enquanto o egresso
barrar as fontes (reconferido hoje nos quatro dominios, por `curl` e por
`WebFetch`, com o site da propria ilha respondendo 200 na mesma passada — e
politica de rede, nao a intermitencia de tunel da secao 20), todo numero entra
por resumo de busca. E resumo de busca tem dois vicios, os dois medidos hoje:

1. **A CONGENERE.** Quando a ficha da especie alvo nao publica o campo, o resumo
   oferece o numero da especie IRMA do mesmo genero **sem avisar que trocou de
   ficha**. Aconteceu tres vezes numa unica execucao: a base de 80 x 30 cm de uma
   *Celestichthys* oferecida como a do danio celestial, a base do *T.* sp.
   'Vietnam' oferecida como a do peixe-neve (segunda vez — a coleta de 09/09 caiu
   na mesma oferta), e a base das congeneres de *Nannostomus* oferecida como a do
   peixe-lapis. **Numero sem o nome da especie do lado e recusa, nao dado**, e
   agora cada registro grava qual numero foi oferecido e recusado, para a proxima
   coleta nao repetir a busca perdida.
2. **REPRODUZIR NAO E CONFERIR.** O porte de 13,7 cm TL do gurami mel voltou
   identico em duas formulacoes de busca hoje — e a recusa de 09/09 estava certa.
   Cheguei a ela por conta propria, sem ter lido a nota, e pelo mesmo caminho: o
   que derruba o numero e a **contradicao interna da fonte**, que declara 13,7 cm
   e, na mesma ficha, aquario minimo de 60 cm, enquanto para o *T. leerii*, de
   12,0 cm, a mesma base declara 120 cm. Tres reproducoes em duas datas nao
   compram uma conferencia.

**E16, a guarda executavel.** `esquema-especies.json` foi para a versao 3 e o
validador ganhou a regra: **todo numero de campo tem de aparecer no texto de
alguma fonte que declara aquele campo**, em algarismo ou por extenso. O campo e o
numero que a maquina usa; a `referencia` e a transcricao do que a fonte disse —
sao duas escritas independentes do mesmo fato, e quando divergem alguem
transcreveu, digitou ou editou um lado so. E a mesma familia de defeito que a
Robometria achou comparando duas copias da mesma regua, com uma diferenca que faz
a comparacao valer: **aqui as duas copias sao mesmo independentes.**

**A REGRA QUE FOI DESCARTADA, e o motivo importa mais que a que ficou.** A
primeira ideia foi cobrar coerencia entre porte e frente minima: peixe maior,
frente maior. Medi antes de escrever e o banco tem **87 dessas "inversoes", quase
todas legitimas** — o betta de 6,5 cm pede 45 cm porque e sedentario, o
paulistinha de 3,8 cm pede 90 cm porque nada muito. Quem manda na frente e a
natacao, nao o comprimento. A regra teria enchido o portao de ruido e ensinado a
ignora-lo.

**E o E16 nasceu VERDE, entao teve de provar que morde.** Quatro corrupcoes
deliberadas novas em `testar-validador-especies.py`: numero trocado, um lado do
intervalo trocado, a largura da base trocada, e — a que prova que a leitura por
extenso e real e nao um buraco que aprova qualquer coisa — o cardume da
coridora-panda de 6 para 7, onde a fonte escreve "pelo menos SEIS" por extenso.
**19 testes negativos, 19 reprovando.**

**VERIFICACAO:** `validar-especies.py` 36 especies, 0 erro, 1 aviso (o E15 do
guppy, que fica de pe de proposito — ver abaixo); `testar-validador-especies.py`
19 de 19; `validar-produtos.py` e `conferir-slugs.py` sem falha; os tres JSON
reparseados. **Nada foi ao ar e nao havia o que ir:** os quatro arquivos tocados
sao `publicar: false`. O manifest subiu para a **revisao 50** e o `/status` foi conferido no ar batendo
em 50, com 18 aplicados e 0 falha — ver a nota de processo abaixo, porque o
caminho ate la quase virou um diagnostico errado.

**TRES COLETAS RECONFERIRAM 09/09 E DERAM O MESMO RESULTADO** — a verificacao
separada no TEMPO, que e o que a secao 19.4(c) do contrato pede: o guppy nao tem
ficha propria no compendio (so forum, e forum nao e compendio com bibliografia,
entao o aviso E15 dele nao sai por busca — sai por leitura direta ou por um
terceiro corpo); a ficha do molly no compendio esta publicada INCOMPLETA, com a
secao de dimensoes vazia, o que explica por que a frente minima nao vem e avisa
que procurar de novo pelo mesmo caminho nao adianta; e o gurami de tres pintas
recebeu a oferta de um arranjo "um macho para 2 ou 3 femeas" que foi recusada
porque a propria fonte o apresenta como arranjo de REPRODUCAO, nao de manutencao.
Harem de desova nao e convivencia de aquario comunitario.

**NOTA DE PROCESSO — O `/status` ATRASA ~5 MINUTOS DEPOIS DO PUSH, E ISSO NAO E
DEFEITO.** Medido nesta execucao porque quase virou diagnostico errado. Depois do
push com o manifest na revisao 50, o Sync foi acionado e respondeu 200 dizendo
**revisao 48** — a anterior. Tres acionamentos seguidos disseram 48; o quarto,
`21:34:33Z`, disse 50, e o `/status` passou a bater com o manifest (18 aplicados,
0 falha). A causa esta no proprio snippet: `AQUAMETRIA_SYNC_BASE` aponta para
`raw.githubusercontent.com/.../main/`, e o `wp_remote_get` manda
`Cache-Control: no-cache` — que instrui o servidor de origem, **nao o CDN do
raw**, que serve a versao anterior por alguns minutos. O `no-cache` no codigo da
a impressao de que isso ja esta resolvido, e nao esta.

**Como ler isso na proxima vez:** Sync respondendo 200 com a revisao ANTERIOR,
logo depois de um push, e cache de CDN — espere e reacione, nao reescreva nada.
E a mesma forma do `000` lido como bloqueio de rede na semana passada (secao 20
do contrato) e do fundo preto do logo do Clube do Mosaico: **sintoma lido como
causa, e o diagnostico errado se propaga porque a execucao seguinte le o
`ESTADO.md` da anterior como fato.** O jeito de nao cair nisso e o que foi feito
aqui: reacionar o Sync em intervalo e olhar a serie, em vez de concluir na
primeira leitura.

**Receita:** 39 dos 78 produtos seguem esperando link de afiliado; este bloco nao
tocou catalogo. **Pauta (secao 17):** `pauta.md` ainda nao existe — 0 escritos, 0
na fila, 0 recusados.

Proximo passo desbloqueado: com 27 especies aptas a pagina e 29 alimentando a
C8, o eixo "quantos litros para X peixes" tem banco suficiente — mas **tudo que
cria URL continua travado ate a leitura de 16/09** (item 5 do despacho da
Sentinela e o T2 deste arquivo). O proximo bloco sem URL nova e a **vitrine da
C12** (T8), a unica calculadora que ainda nao a tem; antes de escrever uma linha
dela, procurar na C12 a faixa que nao tem um dos dois lados, que foi o que a C15
ensinou. Depois, o catalogo de iluminacao por faixa (T3a).

## 2026-09-11, 23h — T8: a VITRINE chega a C12, e a ficha para de dar dois numeros para o mesmo fato

**O bloco:** a quarta e ultima vitrine da ilha (C3, C5 e C15 ja tinham; a C1 nao
recebe, porque litragem e geometria e geometria nao escolhe produto). Nenhuma
URL nova, como manda o item 5 do despacho da Sentinela de 10/09. C12 v1.3.0,
manifest na revisao 52, esquema de produtos na versao 8.

**O QUE A C12 TINHA DE PROCURAR ANTES DE ESCREVER UM CARTAO — e nao era o que a
C15 tinha.** A C15 ensinou a procurar "a faixa que nao tem um dos dois lados",
porque la o nivel de alta exigencia abre em 40 lm/L e a fonte nao fecha. Aqui
nao existe faixa aberta: **nenhuma midia e eliminada pelo volume do aquario**, e
por isso a regua da C15 para escolher o aquario de referencia ("a celula com tres
a cinco produtos") nao discrimina nada nesta pagina — todas as celulas dao a
mesma lista, so muda a quantidade. O que existe aqui e outra coisa, e e pior de
ver: **uma midia que responde METADE da pergunta.** O Eheim SUBSTRAT pro entra
pela area declarada (450 m²/L), o fabricante nao publica dosagem por litro
nenhuma, e ele e **uma das duas unicas midias com link de loja**. Um cartao de
vitrine com um numero ao lado do nome dele faria o leitor achar que o numero e
dele. O cartao dele sai sem numero, com a borda tracejada, com a recusa escrita
por extenso, e o grupo vai para o DOM (`aqm-c12-vt-grupo-sem-dose`) para o portao
poder cobrar que o cartao diga o mesmo grupo que a lista tecnica.

**O DEFEITO QUE JA ESTAVA NO AR, e que so apareceu ao ler o cartao como um leitor
leria.** A ficha de cada midia dizia *"Uma embalagem atende, pela declaracao do
fabricante: ate 200 L de aquario"*. Isso e verdade para a JBL, cuja embalagem de
1 L **e** a dose inteira. Para o Seachem Matrix e quatro vezes menos que a
verdade: a dose declarada e "250 mL para 200 L" e a embalagem de 1 L sao QUATRO
doses, entao ela rende 800 L. E a tabela pre-calculada da MESMA pagina ja dizia
800 L, porque ela derivava por embalagem ÷ dosagem. **Dois numeros para o mesmo
fato, quatro vezes de diferenca, um deles no produto que abre a lista e tem link
de loja.** A causa e a forma classica: `volume_atendido_declarado_L.max` e, em 5
de 5 registros, **uma segunda copia do denominador da dosagem** — e copia nao
confere copia; ela so da a um numero um segundo significado que ninguem declarou.

**O conserto e mecanico, nao redacional.** (1) A regra **V21** do
`esquema-produtos.json` (versao 7 → 8) cobra que `volume_atendido_declarado_L.max`
seja o denominador da dosagem, porque os dois sao a mesma declaracao; o validador
a executa. (2) O rendimento da embalagem virou campo **derivado** no gerador
(`rende_L = embalagem × 1000 ÷ dosagem`), nunca digitado no banco (V4). (3) A
ficha passou a ter DUAS linhas com nomes diferentes: "o fabricante declara que
250 mL para 200 L atendem ate 200 L de agua" e "uma embalagem de 1,00 L, nessa
dosagem, rende ate 800 L — conta nossa". A pagina de conteudo da C12 ganhou o
paragrafo que explica isso, porque a distincao e conteudo, nao rodape.

**A vitrine.** Desenho copiado da C3/C5/C15 e nao reinventado: uma funcao de
cartao em PHP e o espelho dela em JavaScript com a MESMA marcacao; a sequencia
calculada UMA vez em `sequenciaProdutos()` e passada para `pintarVitrine()`
(calculador de ordem duplicado e combinar de divergir depois); a vitrine ANTES da
ficha e da procedencia (contrato 7); duas vitrines por pagina, a pintada e a
SERVIDA no HTML. **O aquario de referencia da servida e 60 L, e o motivo esta
publicado na propria pagina:** varridos os seis casos da tabela, 30 e 60 L sao os
unicos em que a dosagem do TETO da faixa ainda cabe no cesto do filtro que o banco
declara para aquele volume (16,3% e 32,6%); de 100 L em diante a camada biologica
sozinha estoura o cesto (104%, 156%, 208% e 107%). Entre os dois que cabem, o
maior. Servir vitrine para um caso em que a propria pagina diz "nao cabe" seria
vender o que ela desaconselha — e escolher o caso calando o motivo seria colher
cereja.

**Preco entrou junto, como o T8 manda:** cotacao com data nos cartoes (Matrix
R$ 73,90 e Eheim R$ 285,00, Shopee, cotados em 07/09/2026), lidos de
`produtos-cotacoes.json` pelo gerador — e **as duas frases de "nao publicamos
preco" foram reescritas na mesma versao**, no aviso de publicidade e no rodape da
tabela, porque pagina que mostra preco e diz que nao publica preco se contradiz.
A pagina `divulgacao-de-afiliados.md` tambem parou de enumerar quais calculadoras
ja tem vitrine: a frase virou "toda calculadora que recomenda produto tem
vitrine; a unica sem e a de litragem, e a pagina dela diz por que" — enumeracao
digitada e a forma que envelhece em silencio.

**O `alt` do banco de midia foi acentuado** (era o ultimo dos quatro bancos sem
isso) e o gerador de midias ganhou o portao que os outros tres ja tinham: imagem
com url e sem alt **para** a geracao, em vez de sair calada.

**VERIFICACAO.** `ferramentas/teste-navegador-c12-vitrine.mjs`, novo, com **84
afirmacoes, regua propria** (ele le `AQM_C12_MIDIAS` e recalcula mL, embalagens e
rendimento sozinho, sem chamar uma linha da pagina) e **varredura da entrada
inteira**: 15 volumes, incluindo as bordas de arredondamento de embalagem
(80/81 da Ocean Tech, 200/201 da JBL, 800/801 do Matrix) e os dois extremos.
`ferramentas/mutacoes-c12-vitrine.py`: **11 mutacoes deliberadas, 11 reprovadas**
— entre elas as duas metades do defeito original (o rendimento voltando a ser o
volume da dose, e a ficha voltando a chamar a dose de "uma embalagem"), a vitrine
ordenada por quem tem link, a servida ordenada por preco, o `ceil` virando
`round`, a midia sem foto sumindo da vitrine, a vitrine descendo para depois da
procedencia, o preco perdendo a data, o cartao sem link virando ancora falsa, e a
V21 no validador. **A mutacao roda numa COPIA e quem julga e o portao do
repositorio limpo** — portao copiado junto poderia ser afrouxado pela propria
mutacao que deveria reprova-lo.
Resto da bancada: `teste-navegador-c12.mjs` 84 afirmacoes (uma asercao trocada —
ela cobrava que NAO houvesse preco na tela, e agora cobra que todo preco venha
com a data da coleta), `teste-voz.mjs` aprovado nas 13 paginas,
`teste-navegador-visibilidade-ia.mjs` 155 afirmacoes com o JavaScript DESLIGADO,
`teste-arvore.mjs` 290 afirmacoes, `validar-produtos.py` 78 produtos 0 erro 9
avisos, `validar-especies.py` 36 especies 0 erro 1 aviso, `conferir-slugs.py` sem
falha, `php -l` limpo nos dez snippets, e 390 px sem rolagem horizontal.

**Receita:** 39 dos 78 produtos seguem esperando link de afiliado (nao mudou;
este bloco nao tocou catalogo). Das quatro midias biologicas, 2 tem link e 1 tem
foto — e a que **tem** link e justamente a que a pagina nao dimensiona, o que
torna o cartao honesto dela mais importante que o bonito. As quatro midias sem
link (JBL MicroMec, Ocean Tech Bio Glass, MatrixCarbon, Purigen) tem loja
possivel hoje: sao vendidas na Shopee, e o que falta e a geracao do link, que e
da Sentinela estrategica no navegador do Raphael.

**Pauta da secao 17:** `pauta.md` ainda nao existe nesta pasta — 0 escritos, 0 na
fila, 0 recusados.

**Proximo passo desbloqueado:** com a vitrine fechada nas quatro calculadoras que
recomendam produto, o T8 acaba. Sem criar URL (item 5 do despacho segue de pe ate
a leitura de 16/09), o proximo e o **catalogo de iluminacao por faixa (T3a)** — e
a licao deste bloco vale para ele: antes de escrever, procurar no banco de destino
o campo que e copia de outro campo, porque e ali que a tela inventa um significado
que o fabricante nao declarou.

---

## 2026-09-12 — FECHADO o item 5 do despacho da Sentinela de 10/09 (congelamento ate 16/09)

O item 5 do despacho da Sentinela de 10/09/2026 proibia pagina nova ate a leitura
de 16/09, por causa de zero impressao. **Ele esta suspenso desde 12/09/2026**, pela
secao 21 do `ARQUIPELAGO.md` (o piso da rampa): a Aquametria tem 13 URLs publicadas
e esta ABAIXO do piso de 40 URLs — abaixo do piso, zero impressao nao e informacao
e nao trava, adia nem reduz leva nenhuma.

O historico acima fica como esta: as entradas de 10, 11 e 12/09 que dizem "item 5
segue de pe" descrevem o que valia naquele dia. O campo `congelamento` no cabecalho
do `ESTADO.md` e o que vale agora.

## 2026-09-12, 16hZ — T3a: A PRATELEIRA VAZIA ERA UM SINÔNIMO (C15 1.4.0, esquema 9, revisão 53)

**O bloco começou medindo, e o que a medição achou não era o que a fila esperava.**
O `ESTADO.md` mandava fazer o "catálogo de iluminação por faixa", e a `FILA DE BLOCOS`
descrevia o problema como falta de produto: "hoje são 3 luminárias e a única com link
não cai em faixa nenhuma". Esse texto é de 09/09 e o banco tem 26 registros desde
11/09. Antes de colher uma linha, nasceu `ferramentas/varrer-c15-banco.py` — uma régua
que lê `dados/produtos-iluminacao.json` e `dados/esquema-produtos.json` direto e
reimplementa a regra publicada da C15, sem navegador. Ela responde o que o
`varrer-cobertura.mjs` não responde: quantas luminárias **sobreviveriam** a cada faixa,
inclusive nas faixas que saem vazias, onde a tela não tem cartão para contar e portanto
não diz por quê.

**O DEFEITO, e ele estava no ar.** O mesmo banco escrevia o mesmo fato de duas maneiras.
Seis registros da família Chihiros WRGB II gravavam `regulagem: "aplicativo"`. A irmã
`chihiros-wrgb-ii-pro-60`, colhida na MESMA leva e da MESMA fonte, gravava `"app"` — que
é o valor que o vocabulário do esquema declara. E o `podeRegular()` do JavaScript tinha
uma TERCEIRA cópia da lista, digitada dentro da função, testando `'app'`. Medido no HTML
servido por curl antes de qualquer mudança: o catálogo no ar trazia 5 `"aplicativo"` e 1
`"app"`. Consequência: das 8 luminárias do catálogo que declaram regulagem, 5 eram
invisíveis para o ramo dos "reguláveis" — e a página **afirmava sobre elas** que "não
declara regulagem de intensidade". Afirmação que o próprio banco desmentia, porque ele
lista `regulagem` entre os campos que a fonte sustenta; e que o próprio cartão desmentia
duas linhas abaixo, onde a ficha imprimia `Regulagem: aplicativo`. A página negava e
afirmava o mesmo fato no mesmo cartão.

**Por que a família WRGB II é justamente a que importa:** é ela que cobre 90 a 140 cm.
Com o ramo morto, exigência baixa e média acima de 90 cm saíam com prateleira vazia — e
a leitura fácil dessa prateleira vazia, que a fila já tinha feito, é "falta produto".
Faltava um caractere.

**NENHUM PORTÃO VIA, e essa é a parte que vale mais que o defeito.** Três portões verdes
ao mesmo tempo: (1) o validador nunca leu a chave `vocabulario` do esquema — a declaração
estava lá desde o começo e nenhuma regra a executava, então 0 erro por três dias; (2) o
teste de navegador media a lista "dentro da faixa", que é onde o defeito NÃO aparece; e
(3) o ramo dos reguláveis, que era o ramo quebrado, nunca executava. **Ramo que não roda
é código que teste nenhum protege, por mais afirmações que o teste tenha** — e nenhuma
contagem de afirmações revela isso. O que revelou foi uma régua que varreu a entrada
inteira e contou quantos estados chegam a cada ramo.

**É a V21 com a roupa trocada.** Em 11/09 a C12 pagou por um campo que era CÓPIA de outro
campo, dando a um número um segundo significado que ninguém declarou. Aqui não é um valor
com dois significados: é um significado com duas grafias. Nos dois casos, cópia não
confere cópia.

**O QUE FOI FEITO**

1. **Banco** (nenhum número novo): os 6 registros passaram a gravar `"app"`. É grafia, não
   dado — nenhuma fonte foi reinterpretada, e a razão está escrita na `observacao` de cada
   um e na `descricao` do arquivo.
2. **Esquema, versão 9:** o campo `regulagem` ganhou `regula_intensidade`, que é a fonte
   **única** da classificação "quais comandos abaixam o brilho". `temporizador` fica de fora
   (liga e desliga em horário, não abaixa brilho) e `nenhuma` também.
3. **Regra V23, e ela é de uma família nova.** As outras conferem o VALOR de um campo; a V23
   confere que o valor pertence ao VOCABULÁRIO que o esquema declara — em qualquer entidade,
   sem lista mantida à mão dentro do validador. A V23b cobra o outro lado: subconjunto
   declarado não pode nomear valor que o vocabulário não tem, senão descreve um estado
   inalcançável. **Declaração que nenhum portão lê é comentário.**
4. **C15 1.4.0:** o `podeRegular()` não guarda mais lista nenhuma — lê `AQM_C15_REGULA`, que
   o gerador de catálogo escreve a partir do esquema. Três lugares liam a mesma lista; agora
   um declara e dois leem. O gerador **recusa gravar** se a chave sumir do esquema, porque
   lista vazia faria a C15 negar toda regulagem em silêncio — o mesmo defeito com o sinal
   trocado.
5. **A frase aprendeu a diferença entre três silêncios**, que era o defeito de fundo:
   campo vazio quer dizer que **a Aquametria não colheu**; `nenhuma` quer dizer que **o
   fabricante declara** que a peça não tem; e um valor que regula é o terceiro estado. A
   página dizia os três com a mesma frase, e com isso atribuía ao fabricante um silêncio que
   era nosso. A ficha passou de "não declarada" para "não colhemos este campo".

**O QUE ISSO MOVEU, medido:** 32 dos 69 estados da varredura passam a servir cartão
regulável (47 cartões), contra quase nenhum antes. As faixas que cumprem o critério de 3
produtos da seção 14.3 foram de 1 para 3 — **sem um registro novo no catálogo**. A série
de cobertura em `dados/cobertura-de-faixa.md` ganhou a medição de 12/09 com uma coluna
nova, "+ regulável", porque contar só quem cai dentro da faixa mede metade da prateleira.

**O QUE CONTINUA SENDO FALTA DE PRODUTO DE VERDADE**, e agora está separado do que era
defeito: 50 a 55 cm, 85 cm e 115 cm em toda exigência (vãos entre as coberturas declaradas
das famílias que temos), e 30 a 55 cm com fluxo alto. Nenhuma regulagem conserta isso.
11 dos 26 registros seguem barrados por `fluxo_lm`, 8 deles Soma com link de afiliado.

**DEFEITO DE ETIQUETA ACHADO DE QUEBRA, e três dos quatro não eram deste bloco.**
`atualizar-manifest.py` ganhou a conferência que o Clube do Mosaico escreveu hoje, no
mesmo dia e por conta própria: a versão do manifest tem de bater com a CONSTANTE do
snippet. Ela reprovou quatro de uma vez — C12 (manifest 1.2.0, constante 1.3.0), artigos
(1.1.0 contra 1.2.0), C15 (a minha) e, ao contrário das outras, a **casca**: o manifest
dizia 1.5.0 e a constante está em **1.4.1**. As etiquetas do manifest foram acertadas pela
regra (a constante manda). **A casca fica como item aberto e NÃO foi tocada aqui:** o
cabeçalho dela documenta as versões 1.5.0 (a árvore das treze páginas) e 1.5.1 (o degrau
da trilha da divulgação), e a constante nunca recebeu nenhuma das duas. Como
`aquametria_casca_montar()` só remonta a estrutura quando a constante muda, subir esse
número dispara uma remontagem no site — decisão que pertence a um bloco que toque a casca,
não a um bloco de iluminação. O que está errado hoje é o relato: o site imprime
`casca 1.4.1` enquanto todo registro diz 1.5.1.

**VERIFICAÇÃO.** `teste-navegador-c15-regulagem.mjs`, novo: 335 afirmações, régua própria
(lê o JSON do banco e do esquema, nunca `AQM_C15_CATALOGO` nem `aquametria_c15_catalogo()`),
varrendo 69 estados — comprimento de 30 a **140** cm de 5 em 5 nos três níveis, indo até 140
de propósito porque é a borda superior da cobertura declarada da família WRGB II. Tudo
medido no CORPO da saída, nunca no HTML inteiro: a frase proibida aparece legitimamente
dentro da documentação do próprio snippet. Uma afirmação nova que só existe porque a régua
a tornou verdadeira: **faixa aberta não produz cartão regulável** — na exigência alta o teto
não existe, então nada está "acima do teto", e um regulável ali significaria que alguém
fechou a faixa aberta sem dizer. Regressões sem uma falha: `teste-navegador-c15.mjs`,
`teste-navegador-c15-vitrine.mjs`, `teste-voz.mjs` (13 páginas), `teste-arvore.mjs`,
`teste-navegador-visibilidade-ia.mjs` (com o JavaScript desligado), `validar-produtos.py`
(78 produtos, 0 erro, 9 avisos — os mesmos 9 de antes), `validar-especies.py` (36, 0 erro),
`testar-validador-especies.py` (19 testes), `conferir-slugs.py`, `conferir-protecao-funcoes.py`
e `php -l` em todos os snippets e renderizadores.

**REDE, reconferida nesta execução como manda a seção 20.2:** `aquametria.com.br` em 200 e
`/status` respondendo; `chihirosaquaticstudio.com` e `ista-asia.com` em `000` por política de
egresso, repetido 4 vezes, com o domínio da ilha em 200 na mesma passada — é política, não a
intermitência de túnel da seção 20. **`WebSearch` funciona**, e é por ele que este banco
inteiro foi construído (busca restrita ao domínio da fonte, níveis 3 e 5 da escada). Foi
assim que a coleta desta execução confirmou, no site do fabricante, que a linha WRGB II é
comandada por aplicativo — o que sustentou a normalização em vez de adivinhá-la.

39 dos 78 produtos esperam link de afiliado (não mudou; este bloco não tocou catálogo).
Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

**NO AR às 16h18Z**, e em UM disparo: `/status` na revisão **53**, igual à do manifest,
18 aplicados. 15 afirmações medidas no HTML **servido** por curl, 15 aprovadas — 200;
zero `&#038;` dentro de `<script>`; `AQM_C15_REGULA` servido e igual à lista do esquema;
**zero `"aplicativo"` sobrando no catálogo**; a família WRGB II servindo `"app"`;
`podeRegular()` lendo a fonte única e sem cópia digitada no corpo da função; a frase
colapsada sumida do JavaScript servido; as três frases de silêncio no ar; e a versão
1.4.0 impressa na tela. As 13 URLs da ilha em 200.

**As mutações precisaram de duas rodadas, e as três que passaram na primeira ensinaram
mais que as dez que reprovaram.** (a) Mutar o **gerador** não muda nada enquanto ninguém
o roda — o catálogo já estava escrito dentro do snippet; a mutação passou a regerar na
cópia. (b) A **ficha** não era medida, só a frase da lista, então devolver "não declarada"
para o campo vazio passava batido; nasceu a afirmação da ficha. (c) Devolver a lista
digitada ao `podeRegular()` **com os mesmos valores** é inerte para qualquer medição de
resultado, porque o resultado é idêntico — e tentar fazê-la morder mudando também o
esquema não resolve, já que quem julga é o portão do repositório LIMPO e a régua volta a
concordar. O que essa mutação ameaça não é um valor, é a **estrutura**; então o portão
passou a medir a estrutura do `podeRegular()` servido: que ele lê `AQM_C15_REGULA` e que
não guarda valor de vocabulário digitado. É a mesma lição da seção 8 sobre perdoar por
presença de palavra — quando o certo e o errado produzem o mesmo texto, quem decide é a
estrutura. **13 de 13 na segunda rodada**, com 358 afirmações no portão.

**PRÓXIMO.** O T3a fecha aqui na parte que era defeito. O que sobrou dele é compra de dado
e está nomeado (50 a 55 cm, 85 cm, 115 cm, e fluxo alto de 30 a 55 cm), mas **não dá para
colher luminária nova sem fonte que declare lúmen** — é o buraco estrutural do varejo
brasileiro, já medido três vezes. Com o congelamento da seção 21 suspenso, o caminho que
move a meta desta ilha (tráfego orgânico) é o **T4**, a primeira leva de malha de 5 a 10
URLs, com o banco de espécies de 36 registros destravando "quantos litros para X peixes".
E a lição deste bloco vale para ela: antes de escrever, procurar no banco de destino o
campo que diz a mesma coisa de duas maneiras, porque é ali que um ramo inteiro da página
morre sem ninguém ver.

## 2026-09-12 17h39Z — A ILHA PASSA A MEDIR: GA4 na casca (1.6.0, revisao 54)

**MARCO ZERO DA SERIE DE AUDIENCIA: 12/09/2026.** E a data que o despacho pede
para a secao 21 e para a serie de `dados/audiencia.md`. Toda leitura de GA4 desta
ilha anterior a este dia mede a ausencia da tag, nao a ausencia de visita — e a
frase e literal da secao 5 do `ARQUIPELAGO.md`.

Bloco: o despacho de prioridade ALTA de 12/09/2026 (`dados/despachos.md`), a parte
da Aquametria. Nenhuma URL nova, nenhum registro novo de banco, nenhum numero novo
de calculadora.

### O QUE ENTROU

A tag do Google entra no `wp_head` **pela casca**, nunca por plugin (secao 11.7),
com o ID de medicao da ilha (`G-8Y26XFZF39`) em **constante no topo do arquivo**.

**Prioridade 23, e o numero e a regra escrita em codigo.** O despacho manda
imprimir "o mais cedo possivel" E proibe entrar antes do `<title>`, da meta
descricao ou do JSON-LD — duas metades que so fecham num numero. Quem ja estava no
`wp_head` desta ilha: 1 (`<title>`, do nucleo), 3 (meta descricao e `og:`), 5
(icone do site), 20 (fontes e paleta; JSON-LD das cinco calculadoras e dos tres
artigos) e 22 (`BreadcrumbList`). Entao 23 e o mais cedo que sobra depois do
ultimo JSON-LD. Isso nao vive so no comentario: uma afirmacao le a prioridade de
**todo** `add_action('wp_head')` dos snippets da ilha e cobra que a do gtag seja a
maior — no dia em que uma calculadora nova registrar JSON-LD numa prioridade
acima de 23, o portao reprova antes de a pagina existir.

**Um parametro so na URL, de proposito.** O `esc_url()` escapa `&`, e o defeito de
08/09/2026 que derrubou cinco calculadoras foi o E-comercial virando `&#038;`. Com
`?id=` e nada mais, nao existe segundo parametro para escapar. Uma mutacao
deliberada acrescenta `l=dataLayer&` de volta, e o portao reprova.

Sem banner de consentimento (secao 22.4). Quem declara a medicao e a pagina de
transparencia da ilha, `/divulgacao-de-afiliados/`, que ganhou a secao "O que a
gente mede da sua visita" — a frase que o despacho pede, mais o que a medicao NAO
tem (sem pixel de rede social, sem remarketing, sem dado que identifique quem le).
**A ilha nao tem pagina de privacidade**, e isso esta nomeado em "o que fica
aberto" mais abaixo: a frase foi para a pagina que hoje faz esse papel, porque
criar pagina nova seria alargar um despacho que pediu uma frase.

### A VERSAO DA CASCA SE ACERTA AQUI, E O ITEM NAO ERA DE ETIQUETA

A constante `AQUAMETRIA_CASCA_VERSAO` estava em **1.4.1** enquanto o cabecalho do
proprio arquivo, o `manifest.json` e todo este registro documentavam a **1.5.0**
(a arvore das treze paginas) e a **1.5.1** (o degrau da trilha da divulgacao). As
duas foram ao ar de verdade; o que nunca subiu foi o numero, e o site imprimia
"casca 1.4.1" enquanto todo relato dizia 1.5.1. Como `aquametria_casca_montar()`
so remonta a estrutura quando a constante muda, subir o numero dispara remontagem
— e por isso o acerto esperava um bloco que **tocasse** a casca. Este e ele. A
remontagem e idempotente (nao duplica pagina, nao reescreve pagina editada a mao,
e a limpeza do tema padrao esta travada pela opcao `aquametria_casca_limpeza`),
entao o custo foi uma passada de opcoes. A 1.6.0 carrega as tres coisas.

### O ACHADO QUE MUDOU O BLOCO, E ELE ESTAVA NO AR HA DIAS

O despacho abre dizendo que **nenhuma** ilha tem tag no ar. Para a Aquametria isso
era **falso**, e quem mostrou foi o proprio medidor novo rodado ANTES de escrever
codigo, para provar que ele sabia distinguir o site sem tag do site com tag (77
falhas, como devia). No meio delas: as **treze paginas ja serviam**
`gtag/js?id=GT-PL9DD7KW`, posto pelo plugin **Google Site Kit** — legitimo nesta
ilha, porque a secao 11.7 o deixa opcional e a conexao OAuth foi do Raphael.

Tres consequencias, e a primeira e a licao de metodo:

1. **RODAR O PORTAO NOVO CONTRA O SITE ANTIGO E O QUE ACHOU ISTO.** Trava que so
   e vista depois do desembarque nao tem chance de contar o que o site ja servia.
   Custa um comando e foi o unico motivo de este achado existir.
2. **O PORTAO NAO LOCALIZA A TAG PELA PALAVRA `googletagmanager` — LOCALIZA PELO
   ID DA ILHA.** Na primeira versao do medidor, **tres afirmacoes de ordem deram
   verde com a nossa tag ausente**, porque a posicao que elas leram era a da tag
   do Site Kit. E a cicatriz da secao 8 na hora de escolher o localizador, a mesma
   familia do "conte `&#038;` dentro do `<script>`, nunca na pagina inteira":
   quando o texto legitimo e o que se quer medir sao a mesma palavra, quem decide
   e o identificador, nunca a vizinhanca.
3. **FICA UM ITEM QUE E HUMANO E MUDA NUMERO.** `GT-PL9DD7KW` e um Google Tag, e
   para onde ele roteia so se le logado: `www.googletagmanager.com` responde `000`
   por politica de egresso deste ambiente (repetido duas vezes, com o dominio da
   ilha em 200 na mesma passada — politica, nao a intermitencia de tunel da secao
   20). **Se ele rotear para a propriedade 553860444, a pagina vista chega DUAS
   vezes e a serie da secao 5 nasce dobrada.** A tag do Site Kit **nao foi tocada**
   por esta execucao, de proposito: desligar medicao que o Raphael montou, sem
   saber o que ela alimenta, nao e conserto de bloco — e a ressalva esta escrita no
   despacho, para a primeira leitura de `dados/audiencia.md` sair com ela ao lado.
   A Robometria, que fechou a parte dela as 17h23Z, **nao** tem o Site Kit
   servindo tag; isto e so da Aquametria, a primeira ilha, onde o Site Kit entrou
   pelo checklist antigo.

De quebra, medido na mesma passada e registrado sem conserto: o Site Kit tambem
serve `googlesitekit-events-provider-content-events-*.js` nas treze paginas
publicas. A secao 11.7 reserva a pagina publica para a casca; o medidor novo
nomeia o plugin em vez de calar, e nao reprova, porque quem o serve nao e a casca.

### VERIFICACAO

- `ferramentas/teste-ga4.py` **novo, 216 afirmacoes, 0 falha**, 13 paginas, **um
  processo cada**. Regua propria no sentido que importa: **o ID esperado e lido do
  `PROMPT.md` da ilha, nunca do snippet.** Perguntar ao snippet qual e o ID certo
  aprovaria o ID da ilha vizinha — e tag com ID errado **mede** em silencio, sem
  uma linha de defeito, gravando sessao na propriedade de outra ilha por meses.
  Uma terceira testemunha entra quando existe: o `dados/despachos.md` nomeia o ID
  de cada ilha, e a afirmacao cobra que os tres concordem.
- `ferramentas/mutacoes-ga4.py` **novo, 13 deliberadas, 13 reprovadas — e DUAS
  passaram na primeira rodada.** As duas eram a mesma licao da C15 de hoje: o que
  elas ameacam nao e um valor, e a ESTRUTURA, entao o resultado servido fica
  identico byte a byte e nenhuma medicao de resultado pode ver. (a) Devolver o ID
  **literal** para dentro da funcao, longe da constante — que e exatamente o que o
  despacho proibe, e o defeito do `podeRegular()`, que guardava uma segunda copia
  da lista do esquema. (b) Derrubar a guarda de constante ausente: ela nao e ramo
  morto, porque o bloco de constantes do topo esta todo dentro de
  `if ( ! defined( 'AQUAMETRIA_CASCA_VERSAO' ) )` — uma copia antiga da casca ja
  carregada define a VERSAO, o bloco e pulado, o `GA4_ID` nunca nasce e o PHP 8
  mata a pagina inteira por uma tag de medicao. O portao passou a medir as duas
  pela estrutura do bloco servido. Duas mutacoes atacam a REGUA e nao o site (o
  `PROMPT.md` perdendo a linha do ID, e o `PROMPT.md` divergindo do snippet): se o
  portao lesse o ID da constante, as duas passariam.
- `ferramentas/conferir-ga4-no-ar.py` **novo, 168 afirmacoes no HTML SERVIDO, 0
  falha**, nas 13 URLs. **A lista de URLs vem do sitemap no ar**, nunca digitada:
  pagina nova entra na medicao sozinha. Conferido em cada uma: 200, um carregador
  com o ID da ilha e um so, `async`, `?id=` sem segundo parametro, um bloco de
  configuracao, o ID configurado **exatamente uma vez** (dois `config` para o mesmo
  destino dobrariam a pagina vista), a tag dentro do `<head>`, depois do `<title>`,
  depois da meta descricao e depois do ultimo JSON-LD, nenhum script de outro
  dominio alem do Google, e zero `&#038;` dentro de `<script>`.
- **No ar as 17h39Z:** `/status` na **revisao 54**, igual a do manifest, 18
  aplicados, **UM disparo**. Rede reconferida como manda a secao 20.2: o dominio
  da ilha em 200 tres vezes.
- Regressoes sem uma falha: `php -l` em todos os snippets e ferramentas;
  `conferir-protecao-funcoes.py` (35 funcoes da casca, todas protegidas);
  `teste-voz.mjs` nas 13 paginas; `teste-arvore.mjs`; `teste-seo-tecnico.php` (177
  afirmacoes); `teste-navegador-visibilidade-ia.mjs` com o JavaScript DESLIGADO;
  `teste-navegador-casca-paginas.mjs` (6 larguras, 0 px de rolagem, console
  limpo); `validar-produtos.py` (78 produtos, 0 erro, os mesmos 9 avisos);
  `validar-especies.py` (36, 0 erro); `conferir-slugs.py`. A pagina que eu editei
  foi medida a parte em Chromium a 360/390/781/782/783/1200 px: **0 px de rolagem
  horizontal** nas seis.

### RECEITA E PAUTA, como o despacho de 10/09 item 4 cobra em todo bloco

39 dos 78 produtos esperam link de afiliado — **nao mudou**, este bloco nao tocou
catalogo. Pauta da secao 17: `pauta.md` ainda nao existe — 0 escritos, 0 na fila,
0 recusados.

### O QUE FICA ABERTO, nomeado em vez de esquecido

1. **Para onde `GT-PL9DD7KW` roteia** — humano, e muda numero (acima).
2. **O Tempo Real do GA4 confirmando a propria visita**, que e a terceira metade
   do "pronto quando" do despacho. Nao e da Fundacao neste ambiente:
   `GOOGLE_SA_B64`, `GOOGLE_SA_JSON` e `GOOGLE_SA_FILE` estao **ausentes**, entao
   `ferramentas/ga4.py` nao le, e `www.googletagmanager.com` responde `000`. E do
   navegador do Raphael, ou de uma execucao com a credencial no ambiente — igual
   ao reenvio do sitemap.
3. **A ilha nao tem pagina de privacidade.** A frase do despacho foi para
   `/divulgacao-de-afiliados/`, que e a pagina de transparencia que existe hoje.
   Pagina nova e URL nova, com portao de 1.500 caracteres de corpo, lugar na
   arvore, `BreadcrumbList` e meta propria — bloco, nao frase. Fica na fila.
4. **O `atualizar-manifest.py` desta ilha nao espelha o grupo `ferramentas`**: ele
   avisa "fora do manifest" e **segue**, em vez de reprovar como faz com a versao
   divergente. As tres ferramentas deste bloco foram inventariadas (manifest na
   **revisao 55**, `publicar: false` nas tres, `/status` reconferido), e sobram
   **18 arquivos fora**: 15 ferramentas antigas — entre elas `teste-voz.mjs`,
   `teste-arvore.mjs` e `render-pagina-completa.php`, que sao portoes principais
   desta ilha — mais tres `README.md` e o `dados/indexacao.md`. O
   `atualizar-manifest.py` do Clube do Mosaico aprendeu hoje a cobrar as duas
   direcoes e a PARAR; portar a regra para ca so faz sentido junto com a entrada
   dos 18, porque uma trava que reprova de saida travaria todo manifest desta ilha
   ate alguem escrever 18 descricoes honestas — e descricao de enchimento e pior
   que ausencia. E da mesma familia do "numero de tela nasce contado": inventario
   pela metade nao mente sobre nenhuma pagina, mente sobre com o que esta ilha se
   verifica.

### PROXIMO PASSO DESBLOQUEADO

**T4 — a primeira leva de malha, de 5 a 10 URLs.** Segue sendo o unico caminho que
move a meta desta ilha, que e trafego organico: 13 URLs nao competem por nada. O
banco de especies com 36 registros destrava "quantos litros para X peixes", que a
Bussola verificou ABERTO e e o maior volume de busca da ilha. A ilha esta ABAIXO
do piso da secao 21 (13 URLs, piso de 40), entao a leva sai no ritmo normal, sem
esperar medicao — presa ao teto de 10 URLs por leva e 3 levas por semana (21.4),
ao portao de dado da secao 13 e a classificacao de SERP da 14.9.

E a partir de hoje a leva nasce **medida**: a tag esta no ar, entao a pergunta
"esta leva trouxe visita, e de onde" tem resposta em `ferramentas/ga4.py` no dia
em que a credencial existir — em vez de ser opiniao, como foi para as treze
primeiras.

---

## 2026-09-12, 22hZ — T4 LEVA 2: a categoria `/peixes/tetras/` FECHA em 7 de 7, e três defeitos que já estavam no ar saem junto (peixes 1.1.0, casca 1.7.3, manifest revisão 62)

**O QUE FOI AO AR.** Quatro URLs novas no eixo `/peixes/`, todas de nível 3 sob
`/peixes/tetras/`: **tetra ember** (`hyphessobrycon-amandae`), **tetra-brilhante**
(`hemigrammus-erythrozonus`), **rodóstomo** (`hemigrammus-rhodostomus`) e
**tetra-negro** (`gymnocorymbus-ternetzi`). Com elas a categoria fecha — as 7
espécies que o banco sustenta com duas fontes de corpos distintos têm ficha — e a
ilha vai de **18 para 22 URLs**. Nenhum endereço foi movido. Revisão 61 aplicada
no `/status` em **um** disparo; revisão 62 é a deste fecho.

SERP das quatro consultas classificada em 12/09/2026, antes de a página nascer,
cada uma com o `porque` escrito no registro do snippet (14.9). As quatro são
ALVO. A mais disputada é a do tetra-negro, que tem a Petz no top — e segue ALVO
porque um domínio forte não é "quase tudo", e o que ele serve é blog de varejo
sem número atribuído: a mesma página de resultados dá 60 L, 70 L e 112 L.

**O BLOCO COMEÇOU PELO CONSERTO, e a seção 18.5 é quem manda nisso.** Antes de
escrever a primeira linha, a medição no ar das cinco URLs da leva 1 devolveu
**zero `<meta name="description">` e zero tag `og:`** — com as 13 antigas
servindo a delas normalmente, que é o que prova que o defeito não era do snippet
de SEO. A causa: a lista de páginas do `gerar-metas-descricao.py` era **digitada**,
com um comentário prometendo que "página nova entra aqui no mesmo commit — a
recusa é o alarme". Alarme digitado não dispara sozinho. Agora a lista vem do
**próprio snippet que cria as páginas** (`ferramentas/listar-paginas-do-eixo.php`)
e o gerador recusa nas duas direções: página sem texto e texto sem página. Três
controles negativos, incluindo o caso real — registrar uma página nova e esquecer
a descrição. As 9 URLs do eixo servem description e `og:` no ar, medido.

**DUAS REGRAS DE ESCOPO DE AFIRMAÇÃO, as duas descobertas ao renderizar a leva 2.**

1. **BASE não é FRENTE.** A frase mestra da ficha terminava sempre em *"e a fonte
   declara a BASE, não o litro"*. Era verdade nas três fichas da leva 1 — as três
   têm `base_minima_cm` — e é **falsa em 14 dos 36 registros** do banco, onde a
   fonte declara só o comprimento mínimo e nunca disse uma palavra sobre o fundo.
   O rodóstomo é o primeiro caso publicado: uma coleta limpa em 12/09, restrita ao
   domínio, devolveu *"no mínimo 90 cm de comprimento"* e nada mais — e a mesma
   busca ofereceu um fundo "típico de tetras sul-americanos" que **não entrou**,
   porque resposta que não cita o documento é paráfrase (seção 8). Agora a página
   diz COMPRIMENTO, não serve as duas tabelas que dependem do fundo, e **declara a
   ausência e a causa** em vez de encolher calada. Sumiço silencioso de tabela é a
   forma disfarçada do "silêncio parece defeito" da seção 7.
2. **Espécie de cardume sem o número do cardume não vira ficha.** O título deste
   eixo é "quantos litros para um cardume de X" e a linha mestra abre pela frase
   que nomeia o cardume mínimo; sem o número, o código caía num ramo que escrevia
   a frase sem ele e abria a tabela em **um** exemplar, numa página que duas telas
   abaixo diz que a espécie só vive em grupo. A régua já existia no esquema, no
   portão da C8, desde que o banco nasceu — faltava a página cobrar o mesmo.

**CATÁLOGO E FICHA VIRARAM DUAS RÉGUAS COM DOIS NOMES, e o erro do meio do
caminho vale mais que o acerto.** A primeira versão pôs a regra do cardume no
portão do **catálogo**, e a contagem da seção caiu de 27 para 26: a coridora
sterbai sumiu da contagem, da tabela da categoria e da lista de quem divide a
mesma água — **três lugares onde o dado dela é bom** — para resolver um problema
de outra página. Apertar o portão errado tira da tela informação verdadeira.
Agora o esquema declara `catalogo-de-especies` (27 dos 36) e `pagina-especie`
(o catálogo mais a regra do cardume, 26 dos 27), e o gerador imprime as duas
listas, registro por registro.

**O BANCO: o tetra-negro deixou de ter buraco.** `cardume_minimo` era `null` com
a observação dizendo que *"nenhuma das duas fontes declara"*. Dizia isso porque a
coleta de 09/09 tinha perguntado outra coisa, não porque a fonte fosse muda: duas
passadas restritas à FishBase em 12/09, com perguntas diferentes e **nenhuma
carregando o número que se queria confirmar**, devolveram "grupos de 5 ou mais" e
o aquário mínimo de 60 cm. A mesma resposta trouxe, sem ser perguntada, porte
7,5 cm, pH 6,0–8,0, dH 5–19 e 20–26 °C, idênticos ao que o registro já guardava
desde 09/09 — que é a conferência de que a busca leu a ficha desta espécie. O
60 cm entra como **divergência** contra os 75 cm do Seriously Fish, e o publicado
continua 75: as duas réguas do esquema apontam para o mesmo lado, o que é raro —
a tabela `dominio_por_campo` põe o compêndio acima da base científica em campo de
manutenção, e a assimetria de custo manda ficar com o maior.

**ACENTUAÇÃO: `nomes_populares_br` é TEXTO DE TELA, e o banco inteiro estava sem
acento.** O resto do arquivo é nota interna e é escrito sem acento de propósito;
este campo nasceu sem acento por arrasto e ficou três levas assim, invisível
porque as três primeiras fichas (tetra neon, neon cardinal, mato-grosso) são
nomes que o português não acentua. **Já estava no ar:** a tabela de companheiros
da página do tetra neon servia `peixe-lapis` e `acara-bandeira`. 24 nomes em 15
dos 36 registros acentuados, com tabela **declarada** no esquema e regra **E17**
no validador — declarada e não heurística, porque "parece que falta acento" é a
adivinhação por vizinhança que a seção 8 proíbe. O que ela não pega está escrito
no próprio esquema. Três controles negativos em `testar-validador-especies.py`.

**ARREDONDAMENTO: as duas réguas discordavam e concordaram por sorte.** O Python
e o C arredondam o meio para o par (`'%.1f' % 47.25` → `47,2`) e o
`number_format` do PHP para cima (`47,3`). Durante a leva 1 as duas concordaram em
295 afirmações porque **nenhum número daquelas três fichas caiu no meio**. A leva
2 pôs três na tela de uma vez — 45 × 30 × 35 / 1000 = 47,25 L no ember, 15 × 3,3
× 1,5 = 74,25 L no brilhante e 5 × 7,5 × 1,5 = 56,25 L no negro. Quem está certo
é a página, e isso é decisão e não empate desfeito para o teste ficar verde:
"arredonda para cima no 5" é o que se ensina na escola brasileira.

**A RODA DAS IRMÃS — o defeito que só a conferência NO AR viu (casca 1.7.3).**
Com sete filhas e um teto de quatro irmãs, a casca varria o mapa do começo e
parava nas quatro primeiras: **toda página escolhia as mesmas quatro do topo**, e
rodóstomo e tetra-negro não eram irmãs de ninguém. No ar elas ficaram com **um**
link interno apontando para elas, o da mãe, contra os sete da primeira da lista —
e o 16.4(f) cobra dois. Teto com ordem fixa não reparte: concentra. Agora a lista
começa **depois de mim e dá a volta**; cada página é citada por exatamente quatro
irmãs, medido no ar, e a ordem da roda continua sendo a da intenção de busca, que
é a afinidade que o 16.4(c) pede. Era inerte com três fichas e passou três blocos.
**E a contagem de links de entrada desceu para a bancada**: ela só existia no
`conferir-peixes-no-ar.py`, e é por isso que o defeito foi descoberto depois do
desembarque. A próxima leva reprova antes de publicar.

**TRÊS LISTAS DIGITADAS VIRARAM CONTAGEM**, e as três são a mesma cicatriz
("número de tela nasce contado") aplicada a um portão em vez de a uma frase: a
lista de páginas do gerador de descrições, o `13 === count( $metas )` do
`teste-seo-tecnico.php` (que continuou **verde** enquanto cinco URLs iam ao ar sem
description, porque 13 ainda era 13) e o `18 URLs no sitemap` do conferidor no ar.

**`conferir-entidades` estava VERMELHO DE FORMA PERMANENTE** e ninguém tinha
notado: ele varria o fonte inteiro e acusava a casca por ela **documentar**, num
comentário de bloco, a cicatriz de 08/09/2026 — para explicar o defeito, o
comentário precisa escrever a entidade. Portão sempre vermelho é portão que
ninguém lê, que é a versão barulhenta do portão que envelhece calado. Agora ele
tira os comentários PHP antes de contar, e só antes de contar: o portão 2, que
mede o que o navegador **recebe**, não foi tocado. Controle negativo feito.

**VERIFICAÇÃO — 0 falha em tudo.** `teste-peixes` **732 afirmações** (era 295),
agora sobre nove páginas, um processo por página, com a aritmética recomputada do
banco e a comparação célula a célula; `mutacoes-peixes` **32 de 32** (eram 24),
com oito novas — e uma delas **passou na primeira escrita**, porque afrouxar a
régua do cardume não muda nada num mundo onde nenhuma ficha depende dela: teve de
**produzir o mundo**, registrando a coridora sterbai junto, e virou duas mutações
que medem metades diferentes. `teste-voz` **518 afirmações em 22 páginas** (era
422 em 18); `teste-navegador-arvore` **392 medições em 22 páginas × 6 larguras**
(era 258 em 13), 0 px de rolagem horizontal; `teste-seo-tecnico` 285; `teste-ga4`
360 — e foi ele que pegou o manifest declarando casca 1.7.2 com a constante em
1.7.3; `validar-especies` 36 registros, 0 erro; `testar-validador-especies` 22;
`teste-arvore`, `apelidos` 59, conversor 17, escape, atualizador 9,
`conferir-slugs`, `php -l`, `conferir-protecao-funcoes`, `conferir-entidades`; e
as baterias antigas de mutação rodadas inteiras para provar que nenhuma virou
inerte — voz 20/20, árvore 14/14, GA4 13/13, C15 13/13, C12 11/11.

**NO AR, às 22hZ:** `conferir-peixes-no-ar.py` **227 afirmações, 0 falha** (era
103), com a lista de URLs vinda do índice do sitemap e não digitada — as nove em
200, a aritmética conferida célula a célula no que o **servidor** devolve, cada
degrau do `BreadcrumbList` respondendo 200, a description medida no ar em todas as
nove, e as 22 páginas varridas para provar que nenhuma é órfã.

**RECEITA:** 39 dos 78 produtos seguem esperando link de afiliado. Este bloco não
tocou catálogo. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0 na
fila, 0 recusados.

### ABERTO E NOMEADO

1. **Para onde `GT-PL9DD7KW` roteia** — humano, e a página vista pode estar
   chegando duas vezes. Não mudou.
2. **O Tempo Real do GA4** não se lê deste ambiente por falta de `GOOGLE_SA_B64`.
   Não mudou.
3. **A ilha não tem página de privacidade.** Não mudou, e com a tag do GA4 no ar
   e links de afiliado publicados isso passa a ser dívida de verdade, não detalhe.
4. **O `atualizar-manifest.py` avisa "fora do manifest" e SEGUE.** Sobram 22
   arquivos fora — 21 ferramentas mais os README e o `dados/indexacao.md`. O
   `listar-paginas-do-eixo.php` deste bloco **entrou**. O resto do diagnóstico do
   bloco anterior continua valendo.

### PRÓXIMO PASSO DESBLOQUEADO

**`/peixes/corydoras/` — e a contagem mudou.** O `ESTADO.md` anterior dizia "4
espécies do banco passando no portão"; são **3** (panda, paleatus, aeneus), porque
a coridora sterbai declara convivência "grupo" **sem número** e o portão de página
agora cobra isso. Três é exatamente o mínimo do 16.5, então a categoria nasce —
mas sem folga nenhuma, e a leva seria de 4 URLs (a categoria e as três fichas).
**Duas saídas, e a primeira é melhor:** colher o cardume mínimo da sterbai por
busca restrita, do mesmo jeito que o do tetra-negro foi colhido hoje, e a
categoria nasce com 4 filhas e folga; ou publicar com 3.

Antes disso, vale conferir se a leitura de 16/09 já tem o que responder: as nove
URLs do eixo são as únicas desta ilha com três níveis, mãe publicada e
`BreadcrumbList` de quatro degraus. **Mas isso não trava leva nenhuma** — a ilha
tem 22 URLs, está abaixo do piso de 40 da seção 21, e abaixo do piso zero
impressão não é informação. Teto da 21.4 nesta semana: **2 levas de 3 usadas**.

## 2026-09-12, 23hZ — T4 LEVA 3: nasce `/peixes/corydoras/`, e a segunda categoria separa o declarado do digitado (peixes 1.2.0, manifest revisão 63)

**O QUE FOI AO AR.** Cinco URLs novas no eixo `/peixes/`: a categoria
`/peixes/corydoras/` e as **quatro** fichas dela — coridora bronze
(`corydoras-aeneus`), coridora pimenta (`corydoras-paleatus`), coridora panda
(`corydoras-panda`) e coridora sterbai (`corydoras-sterbai`). A ilha vai de **22
para 27 URLs**. Nenhum endereço das levas 1 e 2 foi movido, e a casca **não foi
tocada** (segue 1.7.3): o eixo inteiro mora no snippet das páginas, e a segunda
categoria não pediu uma linha de casca — o mapa dela já vinha pelo filtro
`aquametria_peixes`.

SERP das cinco consultas classificada em 12/09/2026, **antes de a página nascer**,
cada uma com o `porque` no registro do snippet (14.9). As cinco são ALVO, e a da
categoria é a mais frouxa que este eixo já mediu: o top 7 tem um **post de grupo
do Facebook** e um site que não é de aquarismo, e a mesma página de resultados dá
54 L "para a maioria das espécies", 40 L para um grupo de 3 e **"7 litros por
cada coridora que você adicionar"** — que é exatamente a conta per capita que
esta ilha se recusa a fazer desde a leva 1, publicada ali como se fosse regra.

**A CATEGORIA NASCEU COM 4 FILHAS E NÃO COM 3, E ISSO FOI TRABALHO DE COLETA.**
O `ESTADO.md` anterior deixou a conta escrita: seriam **3** elegíveis (panda,
paleatus, aeneus), o mínimo exato do 16.5, porque o `corydoras-sterbai` declarava
convivência "grupo" e nenhuma fonte dizia de quantos. Ele apontava as duas saídas
e dizia qual era melhor — colher o cardume por busca restrita, como o do
tetra-negro foi colhido. Foi o que este bloco fez, em três passadas:

1. **FishBase, restrita ao domínio.** Devolveu "grupos de 5 ou mais, aquário
   mínimo de 60 cm" — e disse, **na mesma resposta**, que a ficha da sterbai não
   traz isso e que o cuidado "é presumido igual ao das outras Corydoras".
   **Recusado.** É a segunda vez que esta espécie recebe essa oferta (a primeira
   está no registro de 09/09) e a segunda vez que ela é recusada: presunção
   declarada pela própria fonte continua sendo número de outra espécie.
2. **Seriously Fish, restrita ao domínio, sem o número dentro da consulta.** A
   ficha da própria espécie declara que ela deve ser mantida sempre em grupo e que
   **um grupo de pelo menos seis é o melhor**. É o número.
3. **A passada de conferência de identidade**, com pergunta diferente: devolveu,
   sem ser perguntada, a base de 18 × 12 × 12 pol — os **mesmos 45 × 30 cm** que o
   registro já guardava desde 09/09, da mesma ficha. É a prova de que a busca leu
   a página certa, e é o controle que o tetra-negro estreou ontem.

**Por que o 09/09 tinha errado, e não foi descuido:** a passada daquele dia leu a
sentença do aquário ("grande o bastante para um grupo pequeno", sem número) e não
a sentença do grupo. Mesma página, outra frase. O registro agora guarda as duas
fontes e diz qual frase sustenta qual campo.

**A frase do compêndio é de alcance genérico** ("o gênero vai melhor em grupo"), e
o banco a aceita pelo mesmo motivo que **já a aceitava na coridora-panda e na
coridora-bronze**: quem a publica é a ficha da espécie, e a custódia é o elo que
decide. Ler a mesma sentença como declaração em duas irmãs e como generalidade
nesta seria a ilha escolhendo a leitura pelo resultado. O `convivencia` da sterbai
passou de "grupo" para "cardume" pela mesma razão — as duas irmãs classificam a
sentença idêntica assim, e três "cardume" ao lado de um "grupo" numa tabela
comparativa é incoerência sem fato por baixo.

**O DEFEITO QUE ESTE BLOCO PRODUZIU E O PORTÃO PEGOU ANTES DO AR.** A primeira
renderização de `/peixes/corydoras/` serviu **"São 4 tetras"**. A contagem estava
certa — 4 é o número derivado do banco — e o **substantivo** é que mentia: a
palavra "tetras" estava escrita no meio do HTML, ao lado de uma contagem
derivada. É a forma mais silenciosa do número de tela que envelhece, porque ali
nem número era, e a trava que existia media justamente a contagem. Agora `plural`
e `linha_mestra` moram na declaração da categoria, junto do `criterio`, e a
abertura das coridoras diz o que precisava dizer: **coridora é peixe de fundo, e
peixe de fundo se mede pelo chão** — quantos centímetros de base o grupo tem para
vasculhar, não quantos litros cabem em cima.

**TRÊS RÉGUAS ERAM MUNDOS DE UM ELEMENTO SÓ ESCRITOS COMO SE FOSSEM O MUNDO.**
Não são números velhos — é a mesma família das três listas digitadas que a leva 2
converteu, numa forma mais discreta, e as três teriam reprovado a segunda
categoria da ilha **sem apontar defeito nenhum**:

- `CATEGORIA = "tetras"` no `teste-peixes.py`, com a afirmação
  `registradas == [CATEGORIA]`. A régua não dizia "as categorias registradas são
  estas": dizia "só existe UMA". Virou `CATEGORIAS`, com o rótulo declarado ao
  lado das espécies.
- A categoria era cobrada a apontar para **todas** as fichas do eixo. Com a
  segunda no ar, isso passou a exigir que `/peixes/tetras/` linkasse as coridoras
  — pedindo justamente o cluster ralo que o 16.6 proíbe. Agora cobra as filhas
  dela **e** que nenhuma ficha de outra categoria vaze para lá.
- O `conferir-peixes-no-ar.py` montava o endereço de toda ficha como
  `/peixes/tetras/<slug>/`. Do jeito antigo ele teria procurado a coridora panda
  debaixo de tetras, não teria achado, e **o alarme apontaria para o lugar
  errado**: acusaria o desembarque de não ter acontecido quando o que estava
  errado era a régua. Mesma família do "18 URLs" digitado que a leva 2 consertou
  nesta mesma função, dois parágrafos acima.

**E UMA AFIRMAÇÃO NOVA, que só passou a poder falhar hoje: A MÃE É A DELA.**
Enquanto o eixo teve uma categoria só, "linka a mãe" e "linka a mãe certa" eram a
mesma frase. Com duas, o erro que a folga deixaria passar é mudo: uma ficha de
coridora registrada com `'pai' => 'tetras'` iria **ao ar funcionando**, com a
trilha, o breadcrumb e a frase de mãe inteiros, apontando para a categoria errada.

**DUAS MUTAÇÕES PERDERAM O CHÃO, E O MOTIVO É UMA BOA NOTÍCIA.** Com a sterbai
colhida, `podem virar ficha` passou de **26 de 27 para 27 de 27** — e com isso o
banco deixou de ter um caso que discrimine o portão de página do de catálogo. As
duas mutações que registravam a sterbai como ficha para provar a recusa teriam
virado inertes de um jeito especialmente traiçoeiro: continuariam **reprovando**,
agora por slug duplicado no registro, e o placar seguiria verde medindo outra
coisa. Foram reescritas para PRODUZIR O MUNDO — tirar o número de quem o tem, uma
no **banco** e outra no **catálogo do snippet**, porque as duas metades falham por
motivos diferentes. **Régua que depende de um caso raro do banco morre no dia em
que o banco melhora.**

**A TRAVA ANTI-INÉRCIA DISPAROU DUAS VEZES NESTE BLOCO, e as duas contam algo.**
(1) A âncora `'porque' => 'Medido em 12/09/2026: o top 7` passou a casar **duas**
vezes, porque a SERP da categoria nova também tem sete resultados: primeira vez
que a recusa dispara por **crescimento do conteúdo** e não por troca de bancada.
(2) A âncora da mutação nova da sterbai casava também com a **coridora panda**,
que tem o mesmo cardume (6), a mesma frente (45 cm) e a mesma convivência — o
porte entrou na âncora, e sem ela as duas seriam mutadas de uma vez com o mesmo
placar verde.

**E UMA INÉRCIA HERDADA, CONSERTADA DE VEZ.** O `mutacoes-ga4.py` fixava
`'AQUAMETRIA_CASCA_VERSAO', '1.7.2'`. A casca está em 1.7.3 desde a leva 2, então
a bateria **abortava ali** — e as mutações seguintes, entre elas a que mede se o
portão lê o ID do snippet em vez da própria régua, **nunca rodavam**. Ela já
nascera com 1.6.0 e fora reapontada para 1.7.0 no mesmo dia, com um comentário
avisando que era "a primeira a virar INERTE quando a casca sobe de número" — e
envelheceu mais duas vezes. **Um SABOTADOR pode ler o estado atual; uma RÉGUA
não**, e é a confusão entre os dois papéis que prendia aquela linha a um
calendário. Virou `rebaixa_versao_da_casca()`, que rebaixa o número seja ele qual
for e continua recusando operar se não achar a constante. Quem afirma o que é
certo segue sendo o `teste-ga4.py`, com régua própria.

**VERIFICAÇÃO NA BANCADA, 0 falha.** `teste-peixes.py` **1206** afirmações (eram
732), um processo por página, aritmética recomputada do banco e comparada célula a
célula; `mutacoes-peixes.py` **35 de 35 reprovadas** (eram 32); `teste-voz.mjs`
**638** em 27 páginas (eram 518 em 22); `teste-navegador-arvore.mjs` **498**
medições em 27 páginas × 6 larguras (eram 392 em 22), 0 px de rolagem;
`teste-seo-tecnico.php` **330** (eram 285); `teste-ga4.py` **440** (eram 360);
`validar-especies.py` 36 registros, 0 erro, o mesmo aviso E15 de sempre;
`testar-validador-especies.py` 22; `teste-arvore`, apelidos 59, conversor 17,
escape, atualizador 9, `conferir-slugs`, `php -l` em tudo,
`conferir-protecao-funcoes`. Baterias antigas rodadas inteiras para provar que
nenhuma virou inerte: voz 20/20, árvore 14/14, GA4 13/13, c15-regulagem 13/13
e c12-vitrine 11/11.

**RECEITA:** 39 dos 78 produtos seguem esperando link de afiliado. Este bloco não
tocou catálogo de produto — espécie não é produto, e a página diz isso em vez de
calar (seção 7). **Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos,
0 na fila, 0 recusados.

## 2026-09-13, 11hZ — T3d: O GURAMI MEL ENTRA NO CATÁLOGO, e o número que a base científica publica continua RECUSADO (peixes 1.2.1, manifest revisão 64, nenhuma URL nova)

**POR QUE ESTE BLOCO E NÃO UMA LEVA.** O teto da 21.4 é de três levas de URL por
semana por ilha, e a semana já usou as três (levas 1, 2 e 3 do T4, todas em
12/09). O que falta neste eixo agora não é página, é **banco**: quatro categorias
do `ARVORE.md` estão vazias e nenhuma chegava às três filhas do 16.5. Coleta por
busca restrita cabe numa execução, não publica endereço nenhum e é o que faz a
leva da semana que vem nascer pronta — foi o que o estado anterior deixou escrito
como próximo passo, e é o que esta execução fez.

**O QUE ENTROU NO BANCO, e os dois números vieram da ficha da PRÓPRIA espécie.**

1. **`trichogaster-chuna` (gurami mel) — `porte_adulto_cm` 5,5 cm SL.** O
   compêndio declara 55 mm SL na ficha da espécie, e o número voltou **igual em
   duas passadas independentes**, nenhuma delas carregando o número dentro da
   consulta — a cicatriz da sterbai, aplicada antes de o dado entrar.
2. **`trichogaster-chuna` — `cardume_minimo` 4, com a faixa declarada de 4 a 6.**
   A mesma ficha diz que a espécie **não é gregária no sentido dos peixes de
   cardume**, que precisa da interação com os seus e que a compra de "não menos
   que 4 a 6 exemplares" é recomendada; e diz mais, que o grupo forma hierarquia
   com dominante enxotando rival na hora da comida. O campo guarda o **piso que a
   fonte declara**, que é 4; a ficha que nascer daqui serve a **faixa**, nunca o
   piso sozinho, e tem material próprio para explicar a diferença.
3. **`trichopodus-trichopterus` — `origem_geografica`**, que estava `null` desde
   09/09: bacia do Mekong (Laos, Yunnan, Tailândia, Camboja e Vietnã), pela base
   científica, que é quem manda em campo de biologia. **Não era o alvo da
   passada** — veio junto com a busca que foi atrás da convivência e não a achou.
   É a mesma lição que o pano de microfibra escreveu na Robometria ontem:
   varredura feita para UM alvo devolve vizinhos.

**O NÚMERO QUE A FISHBASE PUBLICA PARA O GURAMI MEL CONTINUA RECUSADO, E ESTA É A
QUARTA VEZ.** 13,7 cm TL voltou em 09/09 (duas formulações), em 11/09 (outras
duas, por uma execução que não conhecia a nota) e hoje. **Reproduzir não é
conferir**, e o que o derruba não é a implausibilidade de quem lê: é a
contradição interna da própria ficha, que declara aquário mínimo de **60 cm**
para este peixe enquanto a **mesma base** declara **120 cm** para o *T. leerii*,
de 12,0 cm. O que mudou hoje é que a recusa deixou de ser leitura solitária: a
ficha da mesma espécie no compêndio declara 55 mm, duas vezes.

**A DECISÃO DE DOMÍNIO, escrita porque ela parece contrariar a tabela e não
contraria.** `dominio_por_campo` põe a base científica na frente em campo de
biologia, e ela continua na frente. Mas a `ordem` dela não termina na base: ela
segue para o compêndio. Quando o valor da base é **recusado**, quem sustenta o
campo é o próximo corpo que o declara — e recusar não é "não achar".

**O CAMINHO ÓBVIO ERA REGISTRAR UM CONFLITO, E ELE ESTARIA ERRADO.** `conflitos[]`
é a estrutura dos valores que o banco **aceita** como declarados: quem consome é
`aquametria_peixes_porte_faixa()`, que junta o valor do campo com **todo** valor
de conflito e entrega `[min, max]` — e a lotação usa o **maior**, de propósito,
porque errar o porte para menos é o lado que lota demais. Gravar 13,7 ali
publicaria na tela um gurami mel de 13,7 cm: exatamente o número que quatro
passadas recusaram, entrando pela porta dos fundos da estrutura que existe para
ser honesta. **Número recusado não é divergência — é número que não entrou.** A
divergência fica na observação do registro, com atribuição, com o porquê, e sem
alimentar conta nenhuma.

**E DUAS RECUSAS QUE NÃO VIRARAM CAMPO, medidas hoje em dois corpos.** O gurami
pérola (`trichopodus-leerii`) e o tricogaster (`trichopodus-trichopterus`)
continuam sem `convivencia`. O compêndio, perguntado de duas maneiras diferentes
em cada um, declara temperamento, longevidade, forma de cor e montagem — e não
declara o arranjo social; a base científica declara os 120 cm, o ar obrigatório e
o ninho de bolhas, e também não declara. **A TENTAÇÃO VEIO NOMEADA:** a busca
ofereceu, sem ser perguntada, o número das **congêneres** — "não menos que 4 a 6"
do próprio gurami mel e "não menos que 6" do gurami-chocolate — dizendo com todas
as letras que a ficha do pérola não traz isso. É a regra da congênere do esquema,
e ela custou o empréstimo de um número que teria fechado a categoria com folga.
Preferimos o mínimo exato do 16.5 com dado da espécie certa.

**O QUE ISSO DESTRAVA, e está medido no `ARVORE.md`:** `/peixes/bettas/` (rótulo
"Bettas e gouramis") passa a ter **três** espécies elegíveis — betta
(`solitario`), colisa-anão (`casal`) e gurami mel (`grupo`) —, que é o mínimo
exato do 16.5. As outras três categorias vazias ficaram **nomeadas com o que
falta**: ciclídeos anões tem 1 (o banco não tem outro ciclídeo ANÃO), plecos tem 1
e o cascudo está a UM campo (`temperatura_C`), vivíparos tem 2 e guppy e molly
estão a um campo cada (E15 no guppy, `comprimento_minimo_aquario_cm` no molly).

**O QUE MUDOU NO AR SEM UMA URL NOVA.** O catálogo embutido no snippet foi de
**27 para 28** espécies, e isso muda **nove páginas publicadas**: oito ganham a
linha do gurami mel na tabela de quem divide a faixa de temperatura (22 a 28 °C,
interseção, 5,5 cm, 60 cm), e a do mato-grosso — a única que não publica lista de
companheiro, por ser declarada agressiva — passa a contar "28 espécies do banco"
onde contava 27. **Nenhum nome dessa tabela é link**, então espécie sem página não
cria endereço inexistente. O snippet subiu para **1.2.1** sem uma linha de código
mudada: só o bloco entre `CATALOGO-INICIO` e `CATALOGO-FIM`.

**VERIFICAÇÃO NA BANCADA, 0 falha.** `validar-especies.py` 36 registros, 0 erro,
o mesmo aviso E15 de sempre (guppy); `testar-validador-especies.py` 22;
`teste-peixes.py` **1206** afirmações, um processo por página;
`mutacoes-peixes.py` **35 de 35 reprovadas**; `teste-navegador-arvore.mjs` **498**
medições em 27 páginas × 6 larguras, 0 px de rolagem; `teste-voz.mjs`,
`teste-arvore.mjs`, `teste-seo-tecnico.php` 330, `teste-ga4.py` 440,
`conferir-entidades.mjs` 0 falha, `conferir-slugs.py`, apelidos 59, conversor 17,
escape, atualizador 9, `conferir-protecao-funcoes.py`, `php -l` em tudo. Baterias
antigas rodadas inteiras para provar que nenhuma virou inerte: voz 20/20, árvore
14/14, GA4 13/13.

**NO AR às 11h34Z, em UM disparo.** `/status` na **revisão 64**, igual à do
`manifest.json`, 19 aplicados. `conferir-peixes-no-ar.py` com **356** afirmações,
0 falha, com a aritmética conferida célula a célula no que o servidor devolve. E a
metade que só este bloco tinha para provar, medida no HTML servido e não na
bancada: a linha do gurami mel está na tabela do tetra neon e a frase da sterbai o
cita entre os vizinhos; a página do mato-grosso serve "das **28** espécies do
banco".

**REDE (20.2):** a ilha respondeu 200 nas duas passadas do começo da execução. O
egresso para `fishbase.se` e `seriouslyfish.com` segue fechado **por política** —
o proxy nomeia `connect_rejected`, reconferido hoje com `curl` —, e é por isso que
esta coleta, como todo o banco desta ilha, sai por **busca restrita ao domínio**,
com "a confirmar na ficha" escrito em cada fonte.

**RECEITA:** 39 dos 78 produtos seguem esperando link de afiliado. Este bloco não
tocou catálogo de produto. **Pauta da seção 17:** `pauta.md` ainda não existe — 0
escritos, 0 na fila, 0 recusados.

## 2026-09-13, 21h21Z–22hZ — O PLATI VARIATUS ENTRA NO BANCO E A CATEGORIA DOS VIVÍPAROS ALCANÇA O MÍNIMO DO 16.5 (peixes 1.5.0, manifest revisão 74, nenhuma URL nova)

**POR QUE ESTE BLOCO E NÃO A LEVA 4.** O estado anterior deixou escrito, como
próximo passo, "LEVA 4 = /peixes/bettas/ com as três fichas, DESTRAVADA AGORA
porque a semana virou em 14/09". **A semana não tinha virado.** Esta execução
rodou às 21h21Z de 13/09, que é domingo, com o teto da 21.4 ainda em 3 de 3
levas gastas — as levas 1, 2 e 3 do T4, todas em 12/09. A frase anterior falava
do futuro no presente, e quem a lesse ao pé da letra publicaria leva fora do
teto. Vale registrar como forma de defeito, porque ela é barata de escrever e
caríssima de obedecer: **próximo passo que embute uma data futura tem de dizer a
CONDIÇÃO, não o veredito** — "a partir de 14/09, quando o teto zerar" em vez de
"destravada agora". O que sobrou de trabalho legítimo era o mesmo do bloco das
11hZ: banco e preparação de categoria, que não publicam endereço nenhum.

**TERCEIRA ILHA TENTADA.** A robometria foi reservada às 21h16Z e a
clubedomosaico às 21h19Z por outras execuções, e os dois pushes de reserva desta
foram recusados por cerca de um minuto cada. O passo 5 manda voltar ao passo 2, e
foi o que aconteceu duas vezes; nenhum force push. Antes de escolher, os três
`PROMPT.md` foram lidos: nenhuma ilha tinha despacho aberto para a Fundação, então
a 18.1 não se aplicou e valeu a rotação da seção 1.

### O que entrou no banco

`xiphophorus-variatus` (plati variatus), o 37º registro. Com ele a família
Poeciliidae vai de **2 para 3** espécies aptas no portão de página, e
`/peixes/vivaparos/` passa a poder nascer — mínimo exato do 16.5, sem folga, na
mesma posição em que a `bettas` está. O catálogo embutido foi regerado, de 28
para 29 espécies.

**No ar e medido:** a página da seção servia "28 espécies" e passou a servir
"29", e o plati variatus já aparece na tabela de quem divide a mesma água da
ficha do tetra neon.

### O CONTROLE QUE AUTORIZOU GRAVAR A FRENTE MÍNIMA — o miolo deste bloco

Na mesma sessão, o resumo de busca atribuiu **"aquário mínimo de 60 cm" a TRÊS
espécies diferentes em passadas diferentes**: *P. sphenops*, *P. velifera* e esta.
Isso é impressão digital de vazamento de congênere, e gravar um número desse
cluster sem controle seria gravar eco com cara de leitura. A plausibilidade não
serve de juiz, e "a espécie vizinha também tem 60" seria motivo para **recusar**,
não para aceitar.

O que separou leitura de eco foi **perguntar pelo campo de uma espécie cuja
verdade a ilha já tem**: o espada (`xiphophorus-hellerii`), que a base científica
declara com **80 cm** — número diferente de 60, devolvido na hora. Ou seja: a
fonte publica valor por espécie e a busca o distingue. E a passada que devolveu
os 60 cm do variatus devolveu, **na mesma resposta**, a faixa de 15 a 25 °C, que
não é a do congênere (18 a 25 °C) — prova de que estava lendo a seção de aquário
da ficha certa. **A régua que sai disto vale para toda coleta desta fábrica:
quando um número suspeito de vazamento não pode ser lido direto, pergunte à mesma
fonte um valor que você JÁ CONHECE; se ela devolver o valor conhecido e ele for
diferente, ela distingue.** É controle, não fé.

### Duas recusas medidas, e as duas ficam escritas

- ***Poecilia latipinna*** (molinésia de vela). Nenhum dos dois corpos declara
  frente mínima: o compêndio responde "o aquário deve ser o maior possível,
  porque em aquário pequeno o desenvolvimento da dorsal do macho fica
  prejudicado", que é conselho e não dimensão, e a base não entregou a seção de
  aquário em duas passadas. **Duas armadilhas caíram junto:** a faixa de 24 a
  28 °C que voltou atribuída ao compêndio era de **artigo científico de terceiro
  domínio** ("maintained under standardized conditions"), que é condição de
  experimento e não recomendação de manutenção; e a de 20 a 28 °C da base é a do
  **ambiente subtropical** da espécie, isto é tolerância, que a C5 não pode usar.
- ***Poecilia velifera*** (molinésia veleira). Recusada por dois campos, os dois
  por congênere: a frente é o "60 cm" do cluster acima, sem controle; e a única
  recomendação de arranjo que a busca devolveu vinha declarada, com essas
  palavras, "para espécies de molinésia **relacionadas** como a *P. latipinna*".

### A parede do molly mudou de natureza, e isso é o que a próxima tentativa precisa saber

As passadas de 09/09 e 11/09 procuraram a frente mínima no **compêndio**, cuja
seção de dimensões desta espécie a própria fonte publica vazia, e a observação do
registro concluía: "não é limite da busca, é buraco da fonte; procurar de novo
pelo mesmo caminho não vai achar". Estava certa sobre o caminho dela e faltava o
outro: **a base científica**, que tem seção de aquário e é quem sustenta esse
mesmo campo para o platy e para o variatus. Ninguém tinha perguntado a ela.

Foi perguntado, duas passadas limpas, e **a base também não entrega**: devolveu,
nas duas, o número da espécie vizinha. Então a situação mudou de "a fonte da vez
tem buraco" para "**os dois corpos foram perguntados e nenhum entregou**", e o
desbloqueio do molly passou a depender da leitura direta — o despacho de egresso
aberto para o Raphael, que cita este peixe pelo nome. É a mesma família do "o
endereço que você testa sai da prosa, o que vale está no banco" (seção 4), agora
aplicada ao CORPO e não ao endereço: **a prosa que descreve um bloqueio descreve o
caminho de quem falhou, e o caminho não perguntado não aparece nela.**

### Uma correção de prosa no banco, achada de carona

A observação do espada dizia "o compêndio pede 60 cm de frente para um e 120 cm
para o outro". O sujeito estava errado na metade dos 60: **quem declara os 60 cm
do platy é a base científica**, e isso está no `campos[]` da fonte dele; os
120 × 30 cm do espada são do compêndio. Não muda número nenhum e muda o que a
frase afirma — a família do "afirmação em bloco tem o escopo do que foi medido".
Os 80 cm que a base declara para o espada ficam escritos ali **sem virar
`conflitos[]`**, porque conflito é a estrutura dos valores que o banco ACEITA e a
faixa de frente usa o MAIOR: gravar 80 não mudaria a resposta e publicaria um
segundo número sem necessidade.

### A classificação de SERP da 14.9, feita antes de a página existir — as três são ALVO

- **"quantos litros para platy"** — top 8 com **um** domínio forte de varejo (blog
  da Cobasi) e sete entre loja, blog e ficha estrangeira. A mesma página de
  resultados dá 40 L, 30 L para um trio, 50 L para comunitário, 80 L e 60 L para
  seis; nenhum atribui o número a fonte nomeada e nenhum publica a base. Um
  domínio forte não é "quase tudo" (14.9), e o que ele serve é blog de varejo sem
  procedência.
- **"quantos litros para peixe espada"** — top 10 de blog, loja e um blogspot de
  2013, dando 60 L para grupo e 100 L para casal. **É a consulta mais valiosa da
  categoria, e agora por medição:** a SERP brasileira recomenda 60 L para o peixe
  que o compêndio declara com **120 cm de frente**. A observação do registro dele
  já dizia "é o peixe que mais aparece em aquário de 60 L no Brasil e o que menos
  cabe nele" — era leitura de quem escreveu, e passou a ser SERP medida.
- **"quantos litros para plati variatus"** — a SERP responde com páginas do
  **outro peixe**: o resultado editorial de cima é a ficha do *X. maculatus* e o
  resumo mistura os números dos dois. A SERP trata as duas espécies como uma, e a
  mesma fonte que sustenta este banco as separa em **dois** campos ao mesmo tempo
  (7,0 contra 6,0 cm TL, e 15 a 25 contra 18 a 25 °C). É o buraco mais limpo que
  esta categoria tem para ocupar.

### O critério da categoria nasceu SEM contagem, e a primeira versão dele tinha o defeito

A primeira versão do `criterio` dos vivíparos dizia quais duas espécies estavam de
fora e por quê, nomeando as duas. Está tudo verdadeiro hoje — e **é afirmação de
ESTADO escrita hoje para ser publicada na leva de amanhã**. No dia em que o molly
ou o guppy entrarem, a frase fica falsa com cara de conferida: é o "número de tela
nasce contado, nunca digitado" em forma de prosa, e é pior que o número, porque
ninguém procura contagem dentro de um parágrafo.

O texto final afirma a **regra** — a família serve de critério e o gênero não (e
diz por quê: plati e espada são o mesmo gênero e pedem frentes que diferem em duas
vezes, enquanto plati e molinésia são gêneros diferentes e pedem água da mesma
dureza); o que entra é o vivíparo cujos sete campos os dois corpos sustentam; e a
frente de quem está a um campo de distância **não** é completada pela da espécie
vizinha. E termina remetendo a contagem ao bloco que a conta abaixo da tabela.
A `bettas` tem a mesma forma de frase digitada ("as cinco espécies do banco são
Osphronemidae") e fica anotado que ela é da mesma família de defeito.

### A RÉGUA DA PRIMEIRA VIDA DE UMA CATEGORIA, que não existia

Uma categoria deste eixo tem **duas vidas**. Antes da leva ela é só declaração:
rótulo, `linha_mestra` e `criterio` escritos, `especies` vazio, nenhuma página no
registro. Depois da leva ela é uma URL, e aí o `teste-peixes.py` inteiro passa por
ela — trilha, tabela, irmãs, schema, voz.

**A primeira vida nunca foi medida.** A `bettas` recebeu critério e linha mestra
às 13h17Z de hoje e **nada** conferia que eles estavam lá, nem que a família que
aquele texto declara como critério tem no banco as três filhas que o 16.5 exige —
que são exatamente as duas coisas que decidem se a leva pode nascer. A preparação
da leva era prosa conferida a olho.

Nascem `medir_categoria_preparada()` no `teste-peixes.py` (**1222 para 1246
afirmações**) e `ferramentas/listar-categorias-do-eixo.php`, irmão do
`listar-paginas-do-eixo.php` e nascido pelo mesmo motivo um nível acima: quem sabe
o que o eixo tem é o próprio eixo. Ele **não lê o banco**, de propósito — quem
recomputa o banco é o teste, com a régua dele; se as duas metades lessem a mesma
coisa, errariam juntas. O que a régua cobra:

1. **Preparação inteira ou nenhuma** — critério e linha mestra declarados juntos,
   ou nenhum dos dois. Meia preparação vai ao ar como página sem a primeira linha
   que explica por que ela junta o que junta.
2. **Categoria sem critério não nasce** (14.4), medido contra o REGISTRO, que é
   quem cria a página.
3. **A lista de espécies é da leva, não da preparação** — nas duas direções.
   Preencher antes faria a mãe publicar contagem de categoria que o 16.5 ainda não
   deixou nascer.
4. **O 16.5 medido na preparação** — a família que o critério declara tem 3 ou
   mais espécies aptas no banco. Vale para `bettas` e `vivaparos`, e é a
   afirmação que protege a leva: se o banco cair, reprova aqui e não na hora de
   publicar.
5. **A razão de frente que o critério publica** (o "duas vezes"), recomputada do
   banco. Prosa com número de banco dentro é número digitado.
6. **A promessa do critério é cumprível** — ele termina remetendo a contagem para
   outro bloco da página, e quem prova que aquele bloco existe é o corpo de uma
   categoria que já está no ar.

**MUTAÇÕES: 46 de 46 reprovadas, 0 inertes** (eram 39). As sete novas são desta
família, cada uma reprovada pela afirmação que ela mira, e **quatro produzem o
mundo**, porque o estado que elas quebram não existe no repositório de hoje: não
há categoria preparada com lista cheia, nem família preparada abaixo do mínimo do
16.5. Nasceu junto `banco_json()` no arquivo de mutações, que edita o banco pela
**estrutura** e não por texto — `"harem"` aparece em quatro espécies, e a troca
por texto atingiria as quatro e mediria outra coisa.

### Verificação

**Bancada, 0 falha:** `validar-especies` (37 registros, 1 aviso conhecido, o E15 do
guppy), `teste-peixes` 1246, `teste-arvore`, `teste-voz`, `teste-seo-tecnico` 339,
`teste-datas-schema` 78, `conferir-slugs`, `validar-produtos`,
`conferir-protecao-funcoes`, `php -l` em tudo. **Mutações:** peixes 46/46, arvore
14/14. **Não rodaram** (medem superfícies que este bloco não tocou): voz, ga4,
datas, dimensão, privacidade e as vitrines.

**No ar às 21h42Z, em UM disparo**, rodados DEPOIS do Sync: `conferir-peixes-no-ar`
358 e `conferir-datas-e-voz-no-ar` 170, 0 falha nas duas, mais a leitura direta do
número da tela (28 → 29).

**Rede, medida pela 20.2 no começo:** site e `/status` em 200; o CDN de imagem da
Shopee em `connect_rejected` nas três passadas, **com a URL lida do BANCO e não da
prosa**, como a seção 4 manda — por isso a dimensão das 24 imagens segue nula com
o motivo declarado.

### O cabeçalho do ESTADO.md estava quebrado como YAML, e foi consertado aqui

A seção 2 do contrato registrou o defeito às 19h58Z de hoje — aspas duplas dentro
de um escalar de aspas duplas derrubam o documento — e mediu **dois dos três**
`ESTADO.md` do arquipélago quebrados. Este era um deles, e a execução que mediu
não podia consertar: a seção 3 proíbe editar arquivo de ilha que não se reservou.
**O conserto não foi tirar as aspas**, que voltaria a quebrar no dia em que
alguém escrevesse uma: `bloco_atual` e `congelamento` passaram a ser **escalar de
bloco** (o `|` do YAML), que não escapa nada. Conferido com `yaml.safe_load`
**antes** do commit, que é o que a seção 2 passou a exigir — e o script de
fechamento só grava se o cabeçalho parsear.

### Receita e pauta

**Receita, sem mudança:** 39 dos 78 com ficha de loja, **0 com piso**, 78 sem
piso; dos 39 sem ficha, 9 não têm loja possível hoje. Nenhum produto entrou ou
saiu do banco — espécie não é produto, e a página diz isso em vez de calar.
**Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0
recusados.

### Dívida nova e nomeada

**A página de categoria não consegue dizer na tela quem ficou de fora do catálogo
e por quê**, porque o catálogo embutido só carrega quem PASSA no portão — os
barrados não existem no snippet. A prestação de contas da seção 7 está cumprida
para quem está na tabela e não para quem não está. O conserto é o gerador escrever
também a lista dos barrados com o motivo de cada um, e ele muda a tela das três
categorias de uma vez: merece bloco próprio, e está na ordem do próximo passo.

### Próximo passo

1. **LEVA 4 = `/peixes/bettas/`** com as três fichas, **a partir de 14/09**,
   quando o teto da 21.4 zerar. A categoria está preparada desde as 13h17Z e
   agora a preparação tem régua.
2. **A leva seguinte = `/peixes/vivaparos/`** com platy, espada e plati variatus.
   Este bloco a deixou pronta pelo mesmo padrão: banco fechado, critério escrito,
   SERP classificada.
3. **A lista dos barrados na tela** — a dívida acima.
4. **A escada na tela**, quando houver `url_busca`, em bloco inteiro nas quatro
   calculadoras de uma vez.

---

## 2026-09-14 15h18Z–15h52Z — O PISO DE BUSCA CHEGA NA TELA (despacho do Raphael de 14/09, inteiro)

**Versões:** C3 1.6.0, C5 1.6.0, C12 1.4.0, C15 1.5.0 · manifest **revisão 84** ·
`/status` conferido na 84 em **um disparo**, 20 aplicados. Nenhuma URL nova,
nenhuma URL mudou, nenhum produto entrou ou saiu do banco.

### A escolha da ilha — segunda tentada

Pela **18.1**, duas ilhas tinham o **mesmo** despacho do Raphael de 14/09 aberto
no topo do `PROMPT.md`, escrito às 14h59Z pelo commit que corrigiu a seção 7:
aquametria e robometria. Empate de destinatário e de data, então valeu o
desempate da seção 1 — a robometria tinha `ultima_execucao` mais antiga (13h54Z
contra 14h34Z) e **meu push de reserva foi recusado por cerca de um minuto**,
outra execução a reservou às 15h17Z. Voltei ao passo 2 como manda o passo 5, sem
force push, e reservei a aquametria às 15h18Z. Nenhum branch `claude/*` e nenhum
PR aberto para mesclar. Rede pela **20.2** antes de trabalhar: home em 200 e
`/status` na revisão 82, igual à do manifest, em **uma** passada.

### O defeito, e por que ele vale para toda ilha

**Não era falta de dado.** Os 78 itens dos quatro bancos tinham a palavra-chave
da busca escrita desde 13/09, em `afiliado.url_busca_produto`, e **nenhum snippet
a lia**. O piso da 25.2 existia no repositório e não existia na tela — a distância
exata que a seção 4 do contrato paga mais caro. Trinta e nove produtos chegavam
na página com **"link de loja em breve"** no lugar do botão, que é a frase que a
seção 7 corrigida em 14/09 passou a proibir.

### Os cinco itens do despacho

1. **A busca crua já existia, com o nome que o contrato manda.** O despacho pediu
   `afiliado.url_busca_bruta`; a 25.4-b batizou esse campo de
   `afiliado.url_busca_produto` em 13/09. **Não nasceu um segundo campo** — duas
   cópias da mesma decisão é o defeito que a Robometria pagou de manhã com a
   tabela de artigos de publicador.
2. **`degrau: 4` e `conferido_em: 2026-09-14` nos 39 itens que só têm piso.** Isso
   exigiu **reescrever a V24**, e a correção é de régua, não de dado: ela amarrava
   o degrau a `plataforma`, isto é, ao **anúncio próprio**, e por isso tornava
   impossível gravar justamente o degrau que a 25.2 chama de piso — página de
   busca não tem anúncio próprio por definição. Ela reprovou os 39 no minuto em
   que o piso foi gravado, e reprovou **estando os 39 certos**.
3. **`afiliado.intestavel` nasceu**, derivado de ter `url` e não ter `url_produto`:
   **39 de 39**. Até hoje a dívida vivia dentro da prosa de
   `motivo_sem_url_produto`, e prosa não se conta. O validador cobra a bandeira
   nos dois sentidos.
4. **As quatro calculadoras pararam de servir a frase proibida.** Todo cartão das
   quatro vitrines é âncora: com anúncio escolhido aponta para a ficha e carrega a
   busca numa **linha discreta embaixo**, fora da âncora (âncora dentro de âncora
   não é HTML válido); sem anúncio, a busca sobe e vira o botão. O `rel` sai do
   que o link **é** — `sponsored` para quem paga comissão, `nofollow` para a busca
   **crua**, que não paga — e o selo do cartão diz qual é qual.
5. **Os números deste relatório são contados**, e estão abaixo.

### Três desvios de consolo morreram junto

A célula da tabela da C3 e da C5, e a resposta do FAQ das duas, ofereciam **outro**
produto quando o recomendado não tinha link ("Com link hoje, na mesma faixa: …").
Era a única coisa nessas páginas em que a presença de link de afiliado mexia no
que o leitor via — ou seja, **promover por link**, que a seção 7 proíbe com todas
as letras. Com o piso, o caso que justificava o consolo deixou de existir, e as
três saídas de cada célula viraram uma.

### O portão que faltava media só o repositório

`ferramentas/teste-escada-compra.py` ganhou a **seção 4**: renderiza as quatro
calculadoras, arranca `<style>` e `<script>` e confere o `href` de cada cartão
contra o **banco** — nunca contra o catálogo embutido no snippet, que é cópia do
banco e erraria junto com ele. São **644 afirmações**, eram 522. E nasceu
`ferramentas/conferir-escada-no-ar.py`, o irmão que faz a mesma medição no HTML
que o site serve (**107 afirmações**).

**Mutações: 23 de 23 reprovadas pela regra que as nomeia**, de 14 para 23. A
primeira escrita da **mutação 18 PASSOU**, e o defeito era dela e não do portão:
ela trocava o texto de um ramo que o banco de hoje nunca percorre. Mutação que não
muda o HTML servido não mede nada, do mesmo jeito que régua escrita para um mundo
que nunca aconteceu nasce sem poder falhar. Reescrita para **produzir o mundo**,
ela reprova.

### Verificação — 0 falha

**Bancada:** teste-escada-compra 644, validar-produtos (78 produtos, 0 erro, 9
avisos conhecidos), teste-peixes 2256, teste-seo-tecnico 411, teste-ga4 568,
teste-datas-schema 102, teste-apelidos 59, teste-dimensao-imagem 36,
validar-especies (37 registros, o mesmo aviso E15 do guppy),
testar-validador-especies 24, conferir-slugs, conferir-protecao-funcoes,
teste-conversor-markdown 18, teste-atualizador-sync 9, teste-escape-shortcode,
`php -l` limpo nos cinco snippets.
**Navegador:** teste-navegador-c3-vitrine, c5-vitrine, c12-vitrine, c15-vitrine e
c3-dupla-condicao — todos **TUDO OK** depois de reescritos para a escada nova.
**No ar:** `/status` na revisão 84 igual à do manifest, em um disparo. As quatro
URLs em **200**, **zero `&#038;` dentro de `<script>`** nas quatro, **zero "link de
loja em breve"** no corpo das quatro. `conferir-escada-no-ar` com **107 afirmações,
0 falha**.

### Receita, contada e nomeada (item 5 do despacho)

- **78 de 78** itens com piso escolhido (`url_busca_produto`) e com
  `conferido_em: 2026-09-14`.
- **39 de 78** ganharam `degrau: 4` — são exatamente os que não têm ficha.
- **39 de 78** têm ficha de afiliado (`url`), e os **39** estão marcados
  `intestavel: true`: link encurtado sem a URL crua, inconferível pela 25.4-b.
- **0 de 78** têm `url_busca` (o piso **encurtado**, que renderia comissão).
  Continua sendo trabalho da Sentinela estratégica, em lotes de 5, no navegador
  do Raphael — e pela 25.2 isso **nunca** bloqueia página.
- **No ar, nas quatro vitrines servidas: 19 cartões — 9 pela ficha, 10 pelo piso,
  0 sem saída de compra.**

**Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0
recusados.

### Próximo passo

1. **LEVA 5 do eixo `/peixes/` está entregue**; a próxima leva do eixo **não está
   pronta**, e é decisão de banco: `/peixes/ciclideos-anoes/` tem 1 elegível e
   `/peixes/plecos-e-limpa-vidros/` tem 1, longe do mínimo de três do 16.5. O salto
   maior disponível é a própria `vivaparos` indo de 3 para 5 fichas, e ele depende
   do despacho de egresso aberto para o Raphael (molly e guppy).
2. **A lista dos barrados na tela** — a dívida nomeada no bloco anterior, que muda
   a tela das três categorias de uma vez.
3. **Quando houver `url_busca` encurtada**, nada precisa ser construído: o piso
   troca de crua para afiliada sozinho, porque `aquametria_cN_compra()` já prefere
   `url_busca` quando ela existe. O que muda é o selo do cartão, e ele já é
   derivado.

---

## 2026-09-15 11h16Z–11h43Z — A ILHA PASSA A PURGAR O CACHE DO HOSPEDEIRO (despacho de prioridade ALTA da Fundação, fechado)

**Versões:** casca **1.10.0** · manifest **revisão 88** · `/status` conferido na
88, em **dois disparos de Sync** (11h33:55Z e 11h34:02Z) — e os dois por regra,
não por sintoma. Nenhuma URL nova, nenhuma URL mudou, **nenhuma palavra de
nenhuma página mudou**.

### A escolha da ilha — pela 18.1, não pela rotação

Os cinco `ESTADO.md` parseiam em `yaml.safe_load` e os cinco tinham
`executando_desde: null`, que pela **1.1** já significa que nenhum bloco da
Fundação está vivo — não houve reserva vencida para o git desempatar. Pela
rotação da seção 1 a vez seria da **ohmetria** (21h20Z, contra as 22h16Z desta).
O que furou a fila foi o despacho de **prioridade ALTA da Fundação** em
`dados/despachos.md`, aberto em 14/09, cujo texto termina com **"Falta a
aquametria"**; a **18.5** diz que na dúvida entre fechar despacho e começar bloco
novo, fecha o despacho. Reserva aceita **de primeira** às 11h16Z. Outras duas
execuções reservaram ohmetria às 11h17Z e jornadafly às 11h25Z, sem colisão.
Nenhum branch `claude/*` com commit à frente do `main` e nenhum PR aberto.

**Rede pela 20.2, antes de trabalhar:** home em **200** e `/status` na revisão
**87**, igual à do manifest, em **três passadas**.

### O que o despacho supunha sobre esta ilha estava meio certo

Ele registrou, medindo a **home** em 14/09, que a aquametria "não traz a
assinatura" `<!--Generated by Endurance Page Cache-->` e que "não foi medido
página por página" — deixando no ar a hipótese de que talvez ela não tivesse a
camada. Medido aqui nas **40 URLs do sitemap**, com cabeçalho e corpo na **mesma
requisição** (`curl -D - -o`, como a seção 4 exige depois de uma conclusão errada
ter custado quatro revisões na robometria):

- a assinatura realmente **não** aparece no corpo — em nenhuma das 40;
- e `x-server-cache: true` aparece **nas 40**, com `x-proxy-cache` (HIT/MISS) e
  `cache-control: max-age=7200`.

**A ausência da assinatura nunca foi prova de ausência do cache.** Era a régua
procurando um comentário no corpo quando a camada se anuncia no **cabeçalho** —
a mesma família do `conferir-no-ar.py` que aprovou a revisão 37 da robometria com
167 afirmações verdadeiras sobre uma página de horas antes. Por isso a seção 1 da
ferramenta nova afirma **sobre o cabeçalho**: ilha que deixar de ter cache no
hospedeiro tem de fazer a régua falar, não emudecer.

### O achado, e ele é maior que o bloco: `realpath('')` não é `false`

**`realpath('')` devolve o DIRETÓRIO DE TRABALHO ATUAL em PHP.** A função portada
da robometria contém a raiz certa — o caminho real tem de começar pelo caminho
real da raiz — e com os dois argumentos vazios ela compara o diretório atual
**consigo mesmo**, aprova, e a recursão esvazia de onde o processo está rodando.

**Na primeira execução do portão novo ela apagou a pasta inteira desta ilha: 117
arquivos.** Recuperados na hora com `git checkout`, porque o repositório é o
lugar do trabalho (seção 3); num servidor não haveria de onde recuperar. O caso
que a disparou era um `afirmar( true, 'caminho vazio não derruba a função' )` —
uma afirmação que não afirmava nada, escrita para cobrir o caminho degenerado, e
que acabou sendo a única do arquivo que mediu alguma coisa de verdade.

**No site nada disso acontecia**, e isso tem de ser dito com a mesma clareza: o
único chamador monta o caminho a partir de `WP_CONTENT_DIR` e já exigia
`'' !== $pasta && is_dir( $pasta )`. O defeito era da **função**, não do caminho
de produção — e é exatamente o tipo de defeito que **só aparece quando alguém
escreve o portão**, que é o motivo de o portão existir.

**A lição de método:** a guarda estava escrita como "o caminho real tem de estar
DENTRO da raiz real", que é a pergunta certa — e `realpath()` respondeu por um
caminho que nunca foi pedido. **Guarda que confia numa função de biblioteca para
dizer "isto não existe" herda todos os valores que essa função devolve quando a
entrada é degenerada.** Mesma família do número de tela digitado da seção 8, um
nível abaixo: aqui o que *parece medido* é a impossibilidade, não o número.

O conserto é uma linha, recusando o vazio **antes** da comparação — e ela só
sobrevive porque o caso 5 do portão reproduz o acidente numa pasta sacrificável.
A **robometria** e a **clubedomosaico** publicaram a mesma função sem a linha e
sem portão nenhum; virou despacho **NORMAL** em `dados/despachos.md`, com o patch
e os dois arquivos prontos para copiar. NORMAL e não ALTA porque nas três ilhas o
chamador de produção já é seguro: é risco guardado, não sangramento. A seção 3
proíbe editar ilha que não se reservou.

### A purga entregou, e a atribuição é do relógio

- **11h18Z**, antes do bloco: a home servia `expires: 13:17:13` — entrada criada
  às **11h17:13**, que só venceria sozinha às **13h17:13**.
- **11h34:02Z**: segundo Sync, já com a casca 1.10.0 carregada.
- **11h34:09Z**: a home serve `expires: 13:34:09` — **entrada recriada às
  11h34:09** — e `x-proxy-cache` saiu de **HIT** para **MISS**.

O vencimento por tempo está **descartado pelo relógio** (faltavam quase duas
horas), e sobra a purga. Continua sendo **atribuição e não prova**, como na
robometria, e é a causa mais forte que se tem sem acesso ao painel.

**Os dois disparos de Sync foram por regra, não por sintoma:** a descoberta da
clubedomosaico diz que no Sync que **instala** a casca o PHP já carregado é o
anterior, então nenhuma purga roda nele.

### O que este bloco NÃO pode afirmar

A seção 4 cobra de todo bloco publicável pelo menos uma afirmação, medida no HTML
servido, **sobre a coisa que ele mudou** — senão "verificado no ar" quer dizer só
que o site existe. Este bloco **não muda uma palavra de uma página**: ele instala
a purga e o portão dela. Não existe texto novo no ar para afirmar sobre, e
inventar um seria a régua que certifica a página de ontem com o sinal trocado. O
que ele mudou é a **concordância** entre o canônico e o recém-gerado, e é sobre
ela que a seção 2 da ferramenta nova afirma, nas 40 URLs.

### Dívida de cabeçalho encontrada e corrigida de passagem

O `bloco_atual` que estava no `ESTADO.md` descrevia a **preparação** da leva 6 e
a revisão **86**, enquanto a execução das 21h18Z de 14/09 fechou **dois** blocos e
terminou na revisão **87** com 40 URLs. O commit de fecho subiu `urls_publicadas`
e `ultima_execucao` e **não reescreveu a prosa**. Pelo mesmo motivo, o campo
`congelamento` ainda dizia "36 URLs publicadas": remedido no sitemap, são **40** —
e a ilha continua **abaixo do piso** assim mesmo, porque a 21.1 pede 40 URLs **e**
21 dias desde a primeira indexação, e a metade do tempo só fecha em 30/09/2026.
Quem escreve o campo `piso` é a leitura semanal da Sentinela (21.6); a Fundação lê
sem recalcular de cabeça. **Cabeçalho que só o olho lê envelhece calado** — é o
que a seção 2 já diz do YAML, um nível acima.

### Verificação

**Bancada, 0 falha:** `teste-purga-cache` **21 afirmações** (novo),
`mutacoes-purga-cache` **8 baterias, todas decidindo certo, ZERO inertes** (novo),
`teste-seo-tecnico` 447, `teste-apelidos` 59, `teste-peixes` 2683,
`testar-validador-especies` 24, `teste-conversor-markdown` 18,
`teste-atualizador-sync` 9, `teste-escape-shortcode`, `validar-especies` 39
registros / 0 erro / 1 aviso (o E15 do guppy, que já existia), `conferir-slugs`,
`conferir-protecao-funcoes` (45 funções na casca, todas dentro de
`function_exists`), `php -l` limpo nos cinco snippets.

**No ar:** `/status` na **revisão 88**, igual à do manifest.
`conferir-cache-do-host` **43 afirmações, 0 falha** sobre as 40 URLs do sitemap,
com **maior atraso de 0 s** até o canônico concordar (orçamento declarado de
360 s, o dobro dos 166 s medidos na robometria). `conferir-peixes-no-ar` **707
afirmações, 0 falha**.

**O que ficou rodando e fechou depois** — corrigido às 11h53Z, e a correção vale
mais que o número: quando este parágrafo foi escrito, a bateria de mutações da
ilha passava de 20 minutos sem fechar e foi registrada como "não vista verde
aqui". Ela fechou em seguida, e o resultado **não era todo verde**:
`mutacoes-peixes` 90 de 90, `mutacoes-arvore` 14 de 14, `mutacoes-escada` 23 de
23, `mutacoes-datas` 12 de 12, `mutacoes-dimensao` 14 de 14, `mutacoes-ga4` 13 de
13, `mutacoes-privacidade` 23 afirmações 0 falha — e **`mutacoes-voz` VERMELHA**,
com duas mutações inertes. Ver a correção das 11h59Z, logo abaixo.

### As três ferramentas novas

1. **`ferramentas/conferir-cache-do-host.py`** — o "pronto quando" do despacho.
   Põe o canônico contra a quebra de cache em toda URL do sitemap; a lista
   **nasce do sitemap**, nunca digitada, e sitemap vazio **reprova** em vez de
   aprovar zero página. Compara o que o **leitor vê** (marcação fora, entidade
   desfeita, espaço juntado), não bytes — a chave aparece no canonical e em todo
   link interno. Cabeçalho e corpo saem da **mesma requisição**. Quando há
   desacordo, repete dentro de um orçamento **declarado** e **imprime o atraso**:
   janela conhecida vira número, e só o que passa dela reprova.
2. **`ferramentas/teste-purga-cache.php`** — constrói as armadilhas **em disco**
   numa pasta temporária (pasta irmã, `..`, pasta cujo nome apenas *começa* pelo
   da raiz, link simbólico para fora, raiz inexistente, caminho vazio), cada uma
   com uma **testemunha** do lado de fora. Afirmação sobre o que foi apagado é
   metade da prova; a que importa é a afirmação sobre o que **continua lá**.
3. **`ferramentas/mutacoes-purga-cache.py`** — sete mutações mais o **mundo
   intacto**, que tem de passar. Cada mutação declara a **frase** que espera ouvir
   de volta, porque reprovar não é a mesma coisa que reprovar pelo motivo certo.
   Uma delas mediu uma coisa que não se supunha: com o `is_link` desligado, quem
   protege o **alvo** do link não é aquele ramo e sim a contenção — o que sobra
   quebrado é o próprio link, que fica no disco servindo cache velho.

### Próximo passo

1. **A fila de construção desta ilha não andou de propósito** (18.2: correção não
   consome a vez de um bloco). O que estava desbloqueado continua: a **lista dos
   barrados na tela**, que muda a tela das categorias de uma vez, e os
   **artigos-âncora** — os dois sem criar URL de malha.
2. **O teto da 21.4 zera em 21/09/2026**; a semana que começou em 14/09 fechou em
   3 de 3 levas. Até lá, bloco que cria URL de malha não cabe.
3. **A próxima leva do eixo `/peixes/` depende de banco**, não de teto:
   `/peixes/plecos-e-limpa-vidros/` tem 1 elegível contra o mínimo de três do
   16.5.
4. **Para a próxima execução que reservar robometria ou clubedomosaico**: o
   despacho NORMAL de `dados/despachos.md` já traz o patch de uma linha e os dois
   arquivos para copiar. É barato e fecha o mesmo buraco nas outras duas.

---

## 2026-09-15 11h49Z–11h56Z — CORREÇÃO: `mutacoes-voz` estava vermelha com duas mutações inertes

**Nenhuma versão mudou, nenhum snippet mudou, nada foi ao ar.** O que mudou foi
uma régua: `ferramentas/mutacoes-voz.py`, de **20 mutações alcançadas** para
**27 de 27 reprovadas pelo portão**.

### Como apareceu

A bateria de mutações desta ilha foi posta para rodar durante o bloco do cache e
só fechou **depois** que a execução foi dada por encerrada. Seis baterias
voltaram verdes; `mutacoes-voz` voltou **vermelha**, com `ALVO SUMIU` e a frase
que a própria ferramenta escreve: *"a mutação não pode ser aplicada, então ela
não prova nada. Atualize esta lista junto com o código."*

**Não é defeito do bloco do cache** — ele não tocou `aquametria-peixes.php`, e o
diff dos dois commits prova isso. É dívida anterior: as duas mutações citavam o
literal `'Para um cardume mínimo de ' . esc_html( $card )`, que **deixou de
existir** quando a abertura das fichas passou a sair do mapa do arranjo
(`$arranjo['minimo']`) para cobrir solitário, casal e harém, nas levas 4 e 5.

**A ferramenta se comportou exatamente como foi desenhada**, e é isso que faz a
dívida ser barata: `troca()` levanta `SystemExit` quando o alvo some, em vez de
substituir nada e seguir verde. O custo de ela falhar alto foi a bateria morrer
na mutação 21 — **as 7 últimas nunca eram alcançadas**, e nenhuma delas estava
sendo medida havia dois dias. O custo de ela *não* falhar alto teria sido pior:
duas mutações verdes para sempre, provando nada.

### O que se atualiza é o ALVO, nunca o que a mutação afirma

As duas continuam afirmando o item 4 do despacho da Sentinela de 13/09 — a
primeira frase da ficha **não cita quem declarou** e **nunca perde o número**.
Só o endereço no código mudou.

### A reescrita errou uma vez, e o erro é a armadilha do conserto

A primeira versão de "a abertura perde o número e vira conselho sem medida"
tirava apenas o número do **cardume** e deixava os "cm de frente" de pé. O portão
**aprovou** — com razão: a frase continuava trazendo uma medida. Ficou registrado
no próprio arquivo, porque é a armadilha de reescrever mutação inerte:
**mutação que passa não acusa portão fraco quando o defeito que ela monta não é o
defeito que ela nomeia.** "Conselho sem medida" exige tirar os **dois** números,
como a versão original tirava. Com os dois fora, o portão reprova.

### Verificação

`mutacoes-voz` **27 de 27 reprovadas, exit 0**, com as mutações 21 e 25 — as duas
que estavam mortas — decidindo certo. `php -l` limpo em
`aquametria-peixes.php`, que **não foi tocado**: a mutação só escreve em cópia
temporária.

### Uma nota de cabeçalho, para não repetir

A reserva desta correção foi escrita como **11h59Z** quando o relógio marcava
**11h49Z** — dez minutos no futuro. A direção é conservadora (a 1.1 leria a ilha
como ocupada por mais tempo, nunca por menos), mas é número errado num campo que
decide escolha de ilha. Corrigido no fecho. Carimbo de reserva se lê do relógio,
não da memória de quem escreve.

## 2026-09-22 10h16Z–11h5xZ — T4 LEVA 7: a SÉTIMA categoria do eixo, e a primeira leva que não custou uma coleta (peixes 1.11.0, manifest revisão 89)

**Quatro URLs novas** — `/peixes/danios-e-rasboras/` e as fichas do **paulistinha**,
da **rasbora arlequim** e do **tanictis**. A ilha vai de 40 para 44 URLs. Teto da
21.4 na semana que começou em 21/09: **1 de 3 levas**, 4 de 10 URLs.

### A escolha da ilha: pelo foco, não pela rotação

`foco.md` nomeia a aquametria desde 21/09/2026, então pela **1.2** não houve
escolha a fazer — a rotação da seção 1 está suspensa. A ilha estava com
`executando_desde: null`, que pela **1.1** já significa que nenhum bloco da
Fundação está vivo, e a reserva foi aceita de primeira às 10h16Z. Nenhum PR
aberto; as 88 branches `claude/*` do repositório não têm commit fora do `main`.
Nenhum despacho **ALTO** em ilha no ar e quebrada para furar o foco: os abertos
de `dados/despachos.md` são todos NORMAL, e a metade desta ilha do despacho da
purga de cache nasceu aqui e está fechada. Rede pela **20.2** antes de trabalhar:
home em 200 e `/status` na revisão 88, igual à do manifest, em **três passadas**.

### O que esta leva ensina, e é diferente das seis anteriores

**Ela não custou uma coleta.** As levas 1 a 6 começaram todas por banco: o cardume
da sterbai, o porte do gurami mel, o aquário do apistogramma. As três espécies
desta passavam nos **dois** portões do esquema desde **11/09/2026** — estavam no
catálogo, na contagem da seção e na lista de quem divide a mesma água. Não
faltava dado nenhum.

**O que faltava era o LUGAR.** O `ARVORE.md` fechava o eixo em *"Seis, e só
estas"*, e seis levas seguidas leram essa linha como o limite do **eixo** quando
ela era o limite do **documento**. Onze espécies elegíveis ficaram sem página por
isso; oito continuam, e agora estão contadas.

### O número de categorias deixou de ser digitado

A afirmação dos cartões em `ferramentas/teste-peixes.py` cobrava `len(cartoes) ==
6`, com a palavra "seis" no rótulo, e o `ARVORE.md` dizia "Seis, e só estas" na
mesma linha. **Nenhum dos dois era derivado do outro**, então a sétima categoria
reprovou numa régua **sem apontar defeito nenhum** — o oposto do que um portão
serve para fazer, e a terceira vez que este eixo registra o mesmo formato de
defeito (o `registradas == [CATEGORIA]` da leva 2 e a data de SERP digitada da
leva 4).

Consertado pelo desenho que o `teste-arvore.mjs` já usava: nasceu
`categorias_do_arvore()`, que **lê a tabela da seção 3 do `ARVORE.md`**. O
documento manda, e categoria que entrar no código sem entrar nele reprova. Quem
acrescentar a oitava mexe numa tabela, e só nela.

### A regra que a linha mestra escreveu: número de medidas diferentes não se compara

A primeira escrita da linha mestra dizia **"o MENOR destes três é o que pede o
MAIOR aquário"** — a frase mais forte que esta página poderia publicar, e a que
mais se parece com a tese do eixo inteiro. **Ela não se sustenta.** O porte do
paulistinha está declarado em **SL** (3,8 cm, o corpo sem a cauda) e o do tanictis
em **TL** (4,0 cm, com ela); convertidos para a mesma régua os dois podem trocar
de lugar, e a página estaria publicando como medição uma comparação que nenhuma
das duas fontes fez.

A versão publicada diz o que a tabela paga **com qualquer régua**: os três portes
cabem num intervalo de pouco mais de um centímetro, a frente mínima vai de 60 a
90 cm, e a frente **por indivíduo** varia em três vezes (18 cm no paulistinha, 12
na rasbora arlequim, 6 no tanictis — leitura, nunca multiplicada, pela recusa da
leva 1). E a advertência de medida sai **na tela**, na língua do leitor: a coluna
de porte serve para ler cada linha, não para ordenar as linhas entre si.

**É a mesma família da regra da congênere: parece medição e é vizinhança.**

### O critério: a segunda categoria do eixo em que nem a família nem o gênero servem

E ela falha pelo lado **contrário** ao da `ciclideos-anoes`. Lá a família trazia
peixe demais — Cichlidae carrega o oscar de 45,7 cm. Aqui ela deixa peixe **de
fora**: o tanictis é a única **Tanichthyidae** do banco, família só dele, e
filtrar por Danionidae o excluiria de uma página em que o próprio banco já o
coloca — o segundo nome popular brasileiro dele é `paulistinha-da-montanha`, que
é o nome do peixe da linha de cima com um sobrenome.

O que serve é o nome que a pessoa digita, e nesta categoria ele é **verificável
dentro do banco**: os quatro registros declarados são exatamente os que trazem
`danio`, `rasbora` ou `paulistinha` entre os nomes populares, e nenhum outro
registro traz. Critério que se confere com uma varredura, não com a leitura de
quem escreve.

**A rasbora galáxia é declarada e barrada**, e é a barrada mais distante do eixo
inteiro: faltam-lhe **quatro** campos (frente mínima, convivência, temperatura e
o segundo corpo de fonte), contra o campo único do molly e do guppy na leva 5.
Sem declará-la a frase de lista fechada diria que todo danio e toda rasbora do
banco já tem página.

### A SERP das quatro consultas, classificada em 22/09/2026 (14.9)

**ALVO nas quatro.** Top ocupado por página de produto de loja, blog de loja e de
pesca, portal genérico de aquarismo e dois Blogspots (2008 e 2010) — nenhuma
fazenda de domínio forte, nenhum fabricante, nenhum marketplace. Os quatro
conjuntos se contradizem **dentro da própria página de resultados** e nenhum
atribui número a fonte nomeada: paulistinha 40/50/60–80 L; rasbora arlequim 80 L
contra 40 L para dez; tanictis 20/30/50/54/100 L com cardume de 3, 5 e 10.

**O achado é a consulta da categoria**, e é a maior contradição interna que este
eixo já mediu numa SERP só: o mesmo conjunto de resultados diz que danios "podem
viver em aquários de apenas 10 litros" **e** que o paulistinha — que é um danio —
precisa de 40 L. Quatro vezes, sobre o mesmo peixe, na mesma tela. É a
justificativa de a página de categoria existir em vez de três fichas soltas.
Tudo em `dados/indexacao.md`.

### Dois defeitos que já estavam no ar saíram junto, e os dois são da mesma família

**(1) A linha mestra de `/peixes/ciclideos-anoes/` falava em terceira pessoa** —
"o que dobra o **aquário**" —, contra o `VOZ.md`, e estava assim **desde
14/09/2026**. Ninguém viu porque a leva 6 acrescentou as quatro URLs ao
`teste-peixes.py` e **esqueceu do `teste-voz.mjs`**, que tem lista escrita à mão e
não avisa quem falta: o portão ficou **oito dias verde medindo 36 das 40 páginas
do site**. As duas listas dele ganharam as levas 6 e 7, e ele passou de 36 para
**44 páginas — o site inteiro, pela primeira vez**. A afirmação da linha mestra
não mudou; mudou uma palavra, e é a que a régua cobra.

**(2) A tabela de levas de `dados/indexacao.md` estava em 4 linhas para 6 levas.**
Ela existe para a leitura semanal **não precisar abrir código**, então tabela
incompleta ali é a leitura semanal lendo um eixo de 12 URLs como se fosse de 20.
As linhas das levas 5 e 6 foram **copiadas** do registro do snippet e do
`REGISTRO.md` — é índice, e índice não reclassifica SERP.

**As duas são lista escrita à mão que a leva seguinte tem de lembrar de
alimentar, e que não avisa quando alguém esquece.** Apareceram no mesmo dia, em
dois arquivos diferentes, e é o mesmo formato do número digitado que a régua dos
cartões carregava. A do `teste-peixes.py` foi consertada na raiz (passou a ler o
documento); as outras duas continuam à mão, e isso fica escrito aqui em vez de
virar promessa.

### Um nome por página, em toda superfície — e este veio de LER, não de régua

A tabela da categoria dizia **peixe-neve** na mesma linha em que o link dizia
**tanictis**: dois nomes para um peixe, a uma coluna de distância. Nenhuma das
réguas pega isso, porque as duas palavras estão certas. O nome de tela é o
**primeiro** nome popular do banco (`aquametria_peixes_nome`), e quem decidiu o
vencedor foi a medição de SERP desta execução, não o gosto: a prateleira
brasileira vende a espécie como **tanictis** (Pró-Aquarista, Kauar, Fazenda
Submersa, Barretos, Aquarium Crystal). Os quatro nomes continuam no banco — a
espécie é vendida com os quatro, e é isso que reparte a própria SERP —, e
**nenhuma fonte foi tocada**: mudou a ORDEM, que é o que decide a tela.

### A categoria OITAVA não é possível hoje, e agora isso está contado

Varridos o catálogo embutido e as listas declaradas das sete categorias:
**31 elegíveis, 23 com ficha própria, 8 sem categoria nenhuma** — oscar, kinguio,
botia-palhaço, arco-íris boesemani, peixe-lápis, otocinclo, acará-bandeira e
barbo sumatra. **Nenhuma família entre as oito chega a três**, que é o mínimo do
16.5: 2 Cichlidae, 2 Cyprinidae e cinco famílias de um registro cada.

**O caminho mais curto para a oitava é um campo só**, e vale escrever porque é a
diferença entre um bloco e três: uma categoria de **acarás** tem o acará-bandeira
e o oscar já elegíveis, e o **acará-disco** está barrado por UM motivo (`duas
fontes distintas`). O segundo caminho, "barbos", **não fecha**: o sumatra é
elegível, o barbo rosado está a um campo, e não existe um terceiro barbo no banco.

### Verificação

`teste-peixes.py` **3158 afirmações, 0 falha** · `mutacoes-peixes.py` **90 de 90
reprovadas, zero inerte** · `teste-voz.mjs` **44 páginas, TUDO OK** ·
`teste-arvore.mjs` 0 falha · `validar-especies.py` 39 registros, 0 erro (1 aviso
conhecido, o E15 do guppy) · `testar-validador-especies.py` 24 testes, 0 falha ·
`teste-escada-compra.py` 644 · `teste-ga4.py` 696 · `teste-datas-schema.py` 102 ·
`teste-dimensao-imagem.py` 36 · `teste-purga-cache.php` 21 — todos 0 falha ·
`conferir-slugs.py` e `conferir-protecao-funcoes.py` limpos · `php -l` nos 11
snippets.

**No ar:** Sync acionado às 11h06Z (revisão 89, 20 aplicados), `/status`
conferido na revisão **89** às 11h07Z, igual à do manifest, e as quatro URLs
novas em **HTTP 200**. `ferramentas/conferir-peixes-no-ar.py`: **811 afirmações,
0 falha** — nenhuma página órfã, as quatro novas com **3 links internos** cada.
Lidas no HTML servido: `CollectionPage+ItemList+BreadcrumbList` na mãe e
`Article+FAQPage+BreadcrumbList` nas três fichas, `meta description` nas quatro,
zero `&#038;` dentro de `<script>`, e a ficha do tanictis declarando
**COMPRIMENTO** e não BASE, que é o que a fonte dela sustenta.

### Itens esperando link de afiliado (item 5 do despacho da Sentinela de 13/09)

**78 itens seguem sem `url_busca` encurtada** e **zero** deles está sem saída de
compra: o piso da 25.2 (a busca crua) cobre os 78. Quem encurta é a Sentinela
estratégica no navegador do Raphael. Esta leva não tocou em produto nenhum.

### Próximo passo desbloqueado

A oitava categoria do eixo `/peixes/` custa **uma coleta de um campo**: a segunda
fonte do `symphysodon-aequifasciatus` (acará-disco), que fecha `/peixes/acaras/`
com o acará-bandeira e o oscar, no mínimo exato do 16.5. Alternativa sem coleta
nenhuma: `T5` (artigos-âncora) e `T6` (prospecção do widget), que não criam URL
de malha e não gastam leva do teto.

## 2026-09-22 13h20Z–14h10Z — AS LISTAS ESCRITAS À MÃO DESTE EIXO DEIXAM DE EXISTIR: o portão da voz pergunta a quem publica, a bancada varre a pasta, o índice de levas ganha portão — e a coleta do acará-disco é medida e RECUSADA (manifest revisão 91, nenhuma URL nova, e uma correção na página de privacidade no ar)

**A ESCOLHA DA ILHA: PELO FOCO, NÃO PELA ROTAÇÃO.** O `foco.md` nomeia a
aquametria desde 21/09/2026, então pela 1.2 não houve escolha a fazer. A ilha
estava com `executando_desde: null` — que pela 1.1 já significa que nenhum bloco
da Fundação está vivo —, a execução anterior fechou às 11h18Z, e a reserva foi
aceita de primeira às 13h20Z. Nenhum branch `claude/*` com commit não mesclado e
nenhum PR aberto. Nenhum despacho ALTO em ilha no ar e quebrada para furar o
foco. Rede pela 20.2 antes de trabalhar: home em **200** em três passadas e
`/status` na revisão **89**, igual à do `manifest.json`.

**POR QUE ESTE BLOCO, E NÃO A LEVA 8.** A leva 7 fechou dizendo que a oitava
categoria do eixo custa **uma coleta de um campo** — a segunda fonte do
acará-disco, que fecharia `/peixes/acaras/` com o acará-bandeira e o oscar. A
coleta foi feita nesta execução, **e foi recusada** (a seção abaixo conta o que
ela achou e por quê). Sem ela não há leva 8, e o que sobrou de mais caro na fila
era o que a própria leva 7 deixou escrito e em aberto: **duas listas escritas à
mão que a leva seguinte tem de lembrar de alimentar, e que não avisam quando
alguém esquece.** As duas foram fechadas aqui, e uma terceira — a maior — foi
achada no caminho.

### 1. O PORTÃO DA VOZ DEIXOU DE TER LISTA DIGITADA

O `teste-voz.mjs` media 44 páginas porque alguém escreveu 44 nomes em três
listas à mão. Foi o que deixou as quatro URLs da leva 6 **oito dias no ar sem a
régua da voz**, com o portão verde o tempo todo medindo 36 das 40 páginas do
site. A saída é a mesma que a leva 7 deu à contagem de categorias do
`teste-peixes.py`: **perguntar a quem publica.**

- **`ferramentas/listar-paginas-da-casca.php`** nasceu, no molde dos dois
  listadores do eixo: imprime em JSON o que `aquametria_casca_definicao_paginas()`
  cria no WordPress — as quatro da casca e, desde a 1.7.0, o eixo inteiro que
  entra pelo filtro `aquametria_paginas`.
- As três listas do portão sumiram. As páginas da casca são as que a casca
  declara e **não** estão no registro do eixo; as de `conteudo/` saem do
  `manifest.json` (o que o Sync publica, com `publicar: true`); as do eixo saem
  do `listar-paginas-do-eixo.php`; e **a régua severa da ficha** — a que cobra a
  abertura pelo número e a distinção BASE/COMPRIMENTO — sai do campo `especie`
  do registro, que é quem sabe qual página serve uma espécie.
- **E não é o "filtro esperto" que o comentário antigo recusava, com razão.** Ele
  recusava adivinhar a lista por PREFIXO DE SLUG, que é heurística de vizinhança.
  Aqui nada é adivinhado: a lista é a do publicador.
- **A seção de COBERTURA é o que dá dentes.** No fim do arquivo a pergunta é
  feita de novo, do zero, a quem publica, e comparada com o conjunto que os laços
  de fato abriram — não com as listas do alto. Quem trocar a derivação por uma
  lista digitada, ou publicar uma leva sem passar por aqui, **reprova nessa
  linha**. Medido: 44 páginas publicadas, 44 abertas.

### 2. A BANCADA DESTA ILHA NASCEU, E ELA ACHOU DOIS PORTÕES QUE NINGUÉM RODAVA

A terceira lista escrita à mão é de um andar acima e é a que vigia as outras: **a
lista de quais réguas rodar**. Cada execução a enumerava de cabeça e a escrevia
no `REGISTRO.md` como prova. `ferramentas/bancada.py` foi portado do molde da
robometria (18/09/2026) com as convenções desta ilha — e **calibrado contra as
linhas que os portões DAQUI imprimem**, não contra as de lá: a régua do veredito
roda sozinha antes de qualquer portão (17 afirmações) e reprova a bancada inteira
se ela mesma estiver errada.

Ele varre `ferramentas/` e classifica pelo nome. **Portão novo entra na bancada
no dia em que é escrito.** Portão sem convenção é DENUNCIADO; portão cujo texto
discorda do código de saída é INERTE e aparece nomeado no fim.

**O QUE A PRIMEIRA PASSADA ACHOU, e é o motivo de o arquivo existir:**
`mutacoes-c12-vitrine.py` e `mutacoes-c15-regulagem.py` reprovaram por
`ERR_MODULE_NOT_FOUND: playwright`. Eles não são bancada de repositório: montam o
HTML e entregam a um `teste-navegador-*.mjs`, que abre Chromium de verdade — e
**nenhuma execução desde 14/09/2026 os tinha rodado**, porque a lista escrita de
cabeça não os incluía. A classificação passou a perguntar ao ARQUIVO quem dirige
o navegador (quem nomeia um `teste-navegador-` ou importa `playwright`), em vez
de confiar no prefixo: falha de ambiente lida como defeito da ilha é o que faz a
próxima execução desconfiar da bancada inteira.

### 3. O ÍNDICE DE LEVAS DO `dados/indexacao.md` GANHOU PORTÃO

Era a segunda lista que a leva 7 nomeou e deixou aberta: a tabela ficou com
**quatro linhas para seis levas** por oito dias, e ela existe justamente para a
leitura semanal não precisar abrir código. `ferramentas/conferir-indice-de-levas.py`
pergunta ao registro do snippet quais páginas o eixo publica e exige que cada uma
apareça no índice, **pelo endereço ou pela consulta-alvo exata que o próprio
registro declara**. Ele não julga o texto da linha e não reclassifica SERP: recusa
o silêncio.

**E a tabela estava partida em TRÊS.** As linhas das levas 5, 6 e 7 estavam
separadas do cabeçalho por linha em branco — em Markdown isso são três tabelas, e
as duas de baixo, sem cabeçalho, saem da tela como texto solto. Foi remontada sem
uma palavra mudada, e as **sete consultas abreviadas por reticências** ("...tetra
brilhante") passaram a trazer a consulta inteira: a abreviação era do olho, e o
índice agora tem portão. Controle negativo conferido nas duas metades: apagar a
linha da leva 7 reprova nomeando as quatro páginas dela; reabrir a linha em
branco reprova por "2 blocos de tabela".

### 4. A COLETA DO ACARÁ-DISCO FOI FEITA E FOI RECUSADA — por ESCOPO, não por falta de número

O Seriously Fish, colhido por busca **restrita ao endereço da ficha da espécie**
(o egresso devolveu `EGRESS_BLOCKED` para `www.seriouslyfish.com` também hoje,
reconferido por WebFetch), declara para o disco **um aquário de 120 × 45 × 45 cm,
255 L — para alguns juvenis ou um casal reprodutor**. A frase saiu igual em três
formulações diferentes da busca, então a atribuição está firme.

**E ela não entra.** O registro publica outro arranjo: `convivencia: cardume` com
`cardume_minimo: 5`, da FishBase. Gravada em `base_minima_cm`, essa base sairia na
ficha como o chão que o cardume de cinco adultos pede — afirmação que a fonte não
faz. É a mesma família da regra que a leva 7 escreveu, *número de medidas
diferentes não se compara*, com uma diferença: **aqui o que muda não é a régua, é
de quem se fala.** Os outros três campos pretendidos caem junto:
`altura_minima_cm` e `volume_minimo_declarado_L` saem da MESMA frase e carregam o
mesmo escopo; `alimentacao` seria classificação NOSSA de uma descrição de dieta,
não palavra da fonte; e `comportamento` (tímido, assustadiço) não cabe no
vocabulário fechado do esquema.

**A RECUSA PASSOU A TER ONDE MORAR, e é a lição que sobra.** Até hoje coleta
recusada vivia em prosa — na `observacao` do registro, no `PROMPT.md` ("falta
`temperatura_C` do cascudo, recusada em duas coletas"), no `REGISTRO.md` da
execução. **Prosa não se conta e prosa não avisa:** a execução seguinte repete a
mesma busca, gasta a mesma passada e chega à mesma recusa — ou, pior, acha o
número, não acha o motivo da recusa e grava. Nasceu `coletas_recusadas` no esquema
de espécies (mesmo argumento que fez nascer o `afiliado.intestavel` em 14/09), com
a regra **E19** e **quatro testes negativos** no `testar-validador-especies.py`,
que foi de 24 para 28 testes. A regra com dentes é a última: **campo recusado que
hoje está preenchido obriga a entrada a dizer quem o superou e quando** — sem
isso, a recusa e o dado diriam coisas contrárias sobre o mesmo campo, e a mais
nova venceria em silêncio.

**O que destrava `/peixes/acaras/`, então, não é a mesma busca de novo:** ou um
segundo corpo que declare campo de manutenção para o arranjo que o registro
publica (grupo de cinco ou mais), ou um campo de ESCOPO no esquema, que deixe a
base declarada viajar com o arranjo a que ela se refere. O caminho do escopo vale
por si e é maior do que parece: **o oscar carrega o mesmo problema resolvido em
prosa desde 09/09/2026** — a base de 150 × 60 cm que o compêndio declara é para UM
adulto, e isso está na `observacao`, não em campo.

### 5. E A BANCADA NOVA ACHOU UM DEFEITO NO AR NO PRIMEIRO DIA — a página de privacidade

`conferir-privacidade-no-ar.py` existe desde 13/09/2026, estava **VERMELHO**, e
nenhuma execução o rodava: ele não estava na lista que cada uma escrevia de
cabeça. A falha: **o site linka `shopee.com.br` desde 14/09/2026** — a busca crua
que virou o piso da 25.2 — e a página de privacidade listava só
`s.shopee.com.br`, o link curto do anúncio escolhido. Oito dias com um endereço
servido fora de uma lista que a própria página promete completa, numa página cuja
tese é *"o que está afirmado aqui foi medido"*.

Remedido hoje nas **44** URLs do sitemap: quatro endereços que carregam sozinhos
(`www.googletagmanager.com`, `fonts.googleapis.com` e `fonts.gstatic.com` em 44 de
44; `down-bs-br.img.susercontent.com` em 4 de 44) e **dois** de clique
(`s.shopee.com.br` e `shopee.com.br`, os dois em 4 de 44). A tabela saiu de "27 de
27" para "44 de 44", o parágrafo do quinto endereço virou o dos **dois** com a
diferença entre eles escrita para quem lê, e a medição de cookie passou a ser a de
hoje, nas 44, com a primeira declarada pela data. **Manifest revisão 91, Sync às
14h02Z, e o portão conferido no ar depois: 21 afirmações, 0 falha.**

É o argumento inteiro deste bloco numa página só: **régua que ninguém roda é régua
que não existe** — e o custo dela não é teórico, é uma página institucional
incompleta no ar por oito dias.

### O que ficou medido e NÃO foi consertado (18.3)

**Dezoito ferramentas estão fora do `manifest.json`**, entre elas `teste-voz.mjs`,
`teste-arvore.mjs`, `mutacoes-voz.py` e os renderizadores da bancada. O
`atualizar-manifest.py` avisa isso em toda passada — "fora do manifest: ..." — e o
aviso vem sendo lido e não atendido. **É a quarta lista da mesma família**, e com
a bancada varrendo a pasta ela deixou de decidir o que RODA; continua decidindo o
que a ilha declara ter. Fica nomeada aqui em vez de virar promessa.

### Verificação

**A BANCADA INTEIRA, num comando só, e é a primeira vez nesta ilha:**
`python3 ferramentas/bancada.py` → **APROVADO: 29 portões, 0 falha**, com a régua
do próprio veredito medida antes (17 afirmações) e `php -l` nos 11 snippets da
pasta. Um a um, do que ela imprimiu:

`teste-peixes.py` **3158 afirmações, 0 falha** · `mutacoes-peixes.py` **90 de 90
reprovadas** · `teste-voz.mjs` **TUDO OK nas 44 páginas** · `mutacoes-voz.py`
**30 de 30 reprovadas** (eram 27) · `teste-arvore.mjs` 0 falha ·
`mutacoes-arvore.py` 14 de 14 · `validar-especies.py` 39 registros, **0 erro**, 1
aviso conhecido (o E15 do guppy) · `testar-validador-especies.py` **28 testes, 0
falha** (eram 24) · `teste-escada-compra.py` 644 · `mutacoes-escada.py` 23 de 23 ·
`teste-ga4.py` 696 · `mutacoes-ga4.py` 13 de 13 · `teste-datas-schema.py` 102 ·
`mutacoes-datas.py` 12 de 12 · `teste-dimensao-imagem.py` 36 ·
`mutacoes-dimensao.py` 14 de 14 · `teste-purga-cache.php` 21 ·
`mutacoes-purga-cache.py` 8 baterias, zero inertes · `mutacoes-privacidade.py` 23 ·
`teste-apelidos.php` 59 · `teste-seo-tecnico.php` 483 · `teste-atualizador-sync.php`
9 cenários · `teste-conversor-markdown.php` 18 casos · `teste-escape-shortcode.php`
todas · `conferir-entidades.mjs`, `conferir-slugs.py`, `conferir-protecao-funcoes.py`
e `conferir-indice-de-levas.py` limpos · `validar-produtos.py` com o aviso V20
conhecido.

**Fora da passada, e a bancada imprime os nomes em vez de os esquecer:** seis que
abrem o site (`--no-ar`) e dezoito que precisam de Chromium (`--navegador`), entre
eles os dois `mutacoes-*` que esta execução reclassificou.

**NO AR, depois do Sync da revisão 91 às 14h02Z** (`/status` conferido na **91**,
igual à do `manifest.json`): `conferir-peixes-no-ar.py` **811 afirmações, 0
falha** · `conferir-escada-no-ar.py` **107, 0 falha** (5 cartões: 1 pela ficha, 4
pelo piso da 25.2, 0 sem saída) · `conferir-datas-e-voz-no-ar.py` **326, 0 falha**
· `conferir-privacidade-no-ar.py` **21, 0 falha** — eram 20 com **1 falha** antes
da correção desta execução · `conferir-cache-do-host.py` **47, 0 falha**, com
atraso de 0 s até o canônico concordar (orçamento de 360 s) ·
`conferir-ga4-no-ar.py` limpo, com a nota conhecida do `google-site-kit` nas 44
páginas.

### Itens esperando link de afiliado (item 5 do despacho da Sentinela de 13/09)

**78 itens seguem sem `url_busca` encurtada** e **zero** deles está sem saída de
compra: o piso da 25.2 (a busca crua) cobre os 78. Quem encurta é a Sentinela
estratégica no navegador do Raphael. Este bloco não tocou em produto nenhum.

### Próximo passo desbloqueado

**`/peixes/acaras/` continua fechada, e agora se sabe por quê.** A oitava
categoria do eixo não custa mais "uma coleta": a coleta foi feita e o que ela
trouxe não cabe no esquema sem mentir sobre escopo. O que destrava é **um segundo
corpo que declare manutenção para o arranjo do registro** (grupo de cinco ou
mais) **ou um campo de ESCOPO no esquema**, que deixe a base declarada viajar com
o arranjo a que se refere — e esse segundo caminho vale por si, porque o oscar
carrega o mesmo problema resolvido em prosa desde 09/09/2026. Quem for tentar lê
`coletas_recusadas` do `symphysodon-aequifasciatus` antes de gastar a passada.

**Sem coleta nenhuma, e sem gastar leva do teto:** `T5` (artigos-âncora) e `T6`
(prospecção do widget), que é a única alavanca de link do projeto e está parada
desde que subiu de prioridade.

**Mecânico, curto e já medido:** as **18 ferramentas fora do `manifest.json`**, que
o `atualizar-manifest.py` nomeia em toda passada. E, no dia em que houver
`playwright` instalado nesta nuvem, `python3 ferramentas/bancada.py --navegador`:
são 18 portões que ninguém roda desde 14/09/2026, e dois deles reprovaram hoje só
por falta do pacote.
