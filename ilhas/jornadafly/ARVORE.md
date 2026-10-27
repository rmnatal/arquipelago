# ÁRVORE DA JORNADAFLY

Item (i) do 16.8 do `ARQUIPELAGO.md`, escrito em 27/10/2026. **Esta ilha era a única do arquipélago sem este arquivo** — a aquametria, a robometria e a clubedomosaico têm o seu desde 11/09/2026, e é esta ilha, a que está EM FOCO e cuja malha (5b) é o bloco aberto, que estava sem o mapa que a malha segue.

Este arquivo diz **onde cada página mora** e **quem é a mãe de quem**. Breadcrumb, cluster de interlinkagem e leva de malha saem daqui, não da cabeça de quem executa.

**A árvore desta ilha já existia em CÓDIGO antes deste documento, e o documento não a inventou: ele a leu.** `ferramentas/artigos-referencia.py` declara `NIVEL_1 = /guias/` e `NIVEL_2 = /guias/quanto-custa/` nas linhas 41 e 42, e o portão dele já cobra a trilha de quatro degraus, a mãe no corpo e a janela rotativa de irmãs. Onde este arquivo e aquele código discordarem, **o código é o que está entregue** e a divergência é defeito deste arquivo — é a lição que a robometria escreveu no dela: *documento e código mantidos à mão em dois lugares divergem em silêncio*.

Os nomes dos níveis são os do `VOZ.md` (16.1): quem chega aqui diz **experiência**, **quanto custa**, **guia**. Não existe `/entidades/` nem `/cruzamentos/`, porque ninguém digita isso.

**NADA DESTA ÁRVORE ESTÁ NO AR, e não podia estar.** Esta ilha não tem WordPress, não tem casca, não tem Sync e não tem `/status`: faltam os passos 2 a 8 da seção 11, que são de navegador e do Raphael. Toda coluna de "existe hoje" abaixo diz **não**, e as páginas que existem, existem **como regra** — referência em Python mais JSON com `publicar: false`.

---

## 1. Os três níveis

**Nível 1 — seção.** Duas hoje, uma pré-registrada:

| slug | o que mora ali | existe hoje |
|---|---|---|
| `/calculadoras/` | as três ferramentas: a F1, a F2 e a F3 | não — as três existem como regra |
| `/guias/` | os textos que explicam o porquê do número | não — os quatro artigos existem como regra |
| `/experiencias/` | a ficha de cada experiência, por cidade | **não, e não por falta de casca** — ver a seção 4 |

**Nível 2 — categoria**, com o nome que a pessoa usa. **Categoria só nasce com 3 filhas de dado real** (16.5); até lá o cartão na mãe não é link e diz "em breve", sem contagem de banco.

| nível 2 | mãe | filhas | passa a 16.5? |
|---|---|---|---|
| `/guias/quanto-custa/` | `/guias/` | os quatro artigos-âncora | **sim, com quatro** — é a única que passa hoje |
| `/experiencias/<cidade>/` | `/experiencias/` | as experiências daquela cidade | **não**: toda cidade do banco tem **uma** |

**Nível 3 — a pergunta ou a ficha**, com as palavras que a pessoa digita.

**Sem quarto nível** (16.1), e isto tem consequência direta no 5b — ver a seção 4.

---

## 2. Fora da árvore, na raiz

**São cinco, e são exatamente as cinco que a 21.7 nomeia** — a família fechada que fica **fora do teto de levas da 21.4**, porque nenhuma delas responde a uma busca. Publicá-las não é leva e não gasta leva. Nenhuma outra página da raiz entra nesta lista: o que não está aqui é malha e obedece ao teto.

| slug | por quê |
|---|---|
| `inicio` | a home. Sem breadcrumb (16.3). **Nesta ilha a home serve o formulário da F1**, por decisão do `VOZ.md` |
| `sobre` | a 16.1 admite na raiz |
| `contato` | a 16.1 admite na raiz |
| `divulgacao-de-afiliados` | a 16.1 admite na raiz |
| `politica-de-privacidade` | a 16.1 admite na raiz |

**A HOME SERVE O MESMO FORMULÁRIO QUE A F1, E AS DUAS NÃO PODEM SERVIR A MESMA RESPOSTA.** O `VOZ.md` manda que a home abra com *"Quanto custa, para quantas pessoas?"* e os campos de experiência, pessoas e padrão; e `artigos-referencia.py` manda os quatro artigos para `/calculadoras/quanto-custa-a-experiencia/?experiencia=…&versao=…`, no corpo e no botão **Calcular**. São dois endereços com o mesmo formulário, e a 14.4 proíbe duas URLs servindo o mesmo conteúdo.

**A regra, e ela é para o bloco 3b implementar:** a home serve o formulário **vazio** e nunca lê parâmetro; resposta com parâmetro mora **só** em `/calculadoras/quanto-custa-a-experiencia/`, e toda URL com parâmetro leva `canonical` para a mesma URL sem parâmetro. A home é porta de entrada, a calculadora é a página da resposta. É a mesma escolha que a robometria registrou para `/ferramentas/`, com a diferença de que aqui ela nasce decidida em vez de virar dívida.

**O RÓTULO DO MENU COLIDE COM O NOME DE UMA CATEGORIA, e o conserto é no rótulo, nunca no slug.** O `VOZ.md` define o menu como **Experiências · Quanto custa · Guias**, e a especificação 7.2 usou o item "Quanto custa" desse menu para justificar o slug `/guias/quanto-custa/`. Lidos juntos, dois dos três itens do menu caem no mesmo galho (`/guias/` e `/guias/quanto-custa/`) e **a calculadora — que é a página do dinheiro desta ilha — não está no menu**. O slug `/guias/quanto-custa/` fica como está, porque está entregue e o portão de `artigos-referencia.py` o cobra; o que muda é o rótulo do menu que aponta para a ferramenta, e ele é o que a ferramenta **faz**, não o nome dela: a 7.4 já decidiu que *"a consulta paramétrica é da ferramenta; a consulta crua é do guia"*, então o menu diz **"Quanto custa para o seu grupo"** e a trilha de um artigo diz `Início › Guias › Quanto custa › …`. Duas palavras iguais apontando para duas páginas é o defeito; o rótulo paramétrico o desfaz sem tocar em nenhuma URL.

---

## 3. Onde mora cada página que já existe COMO REGRA

Nenhuma está no ar. A coluna "mora em" é o arquivo do repositório que a produz.

| página | papel | mãe | mora em |
|---|---|---|---|
| `inicio` | home | — | 3b, não existe |
| `/calculadoras/quanto-custa-a-experiencia/` | F1, nível 3 | `/calculadoras/` | `ferramentas/f1-referencia.py` + `dados/f1-respostas.json` |
| `/calculadoras/quanto-custa-n-dias-em-cidade/` | F2, nível 3 | `/calculadoras/` | `ferramentas/f2-referencia.py` + `dados/f2-respostas.json` |
| `/calculadoras/o-passe-da-cidade-vale-a-pena/` | F3, nível 3 | `/calculadoras/` | `ferramentas/f3-referencia.py` + `dados/f3-respostas.json` |
| `/guias/quanto-custa/passeio-de-gondola-em-veneza/` | artigo, nível 3 | `/guias/quanto-custa/` | `dados/artigos-ancora.json` |
| `/guias/quanto-custa/subir-na-torre-eiffel/` | artigo, nível 3 | `/guias/quanto-custa/` | idem |
| `/guias/quanto-custa/ingresso-do-coliseu-de-roma/` | artigo, nível 3 | `/guias/quanto-custa/` | idem |
| `/guias/quanto-custa/angkor-pass-de-1-3-ou-7-dias/` | artigo, nível 3 | `/guias/quanto-custa/` | idem |

**OS SLUGS DAS TRÊS CALCULADORAS SÃO PROPOSTA DESTE ARQUIVO, E SÓ O DA F1 JÁ ESTÁ EM CÓDIGO.** `artigos-referencia.py` escreve `/calculadoras/quanto-custa-a-experiencia/` em três lugares; os da F2 e da F3 não estão escritos em nenhum arquivo e nascem aqui, derivados do rótulo que o `VOZ.md` dá a cada uma na home (*"Quanto custa N dias em…"*, *"O passe da cidade vale a pena para você?"*). Quem escrever a casca confere os três contra o código antes de publicar, e **muda este arquivo em vez de divergir dele**.

**OS QUATRO ARTIGOS SÃO UM POR EXPERIÊNCIA, E O BANCO TEM QUATRO EXPERIÊNCIAS.** A correspondência é 1 para 1: gôndola/Veneza, Torre Eiffel/Paris, Coliseu/Roma, Angkor Pass/Siem Reap. É isso que trava a seção `/experiencias/` hoje, e está medido na seção 4.

---

## 4. O 5b NÃO DEPENDE DA CASCA — ELE DEPENDE DE DADO, E AQUI ESTÁ O NÚMERO

**Esta seção corrige o que três execuções seguidas escreveram sem medir.** O `REGISTRO.md` de 23/10/2026 fechou dizendo *"o 3b (casca), o 5b (malha) e o 5c (free tour) dependem da casca"*, o `PROMPT.md` repete, e o `foco.md` lista os passos 2 a 8 da seção 11 como o gesto que *"destrava o ar: casca, snippet e sitemap, e com isso o 3b, o 5b, o 5c"*. **Para o 3b isso está certo. Para o 5b e o 5c está errado**, e o erro tem um custo nomeado: a execução que encontrar a casca pronta vai abrir a malha que o `PROMPT.md` prescreve — experiência → cidade → país — e publicar exatamente o cluster ralo que o bloco 5 já havia medido e recusado em 23/10.

**O 5b DO `PROMPT.md` CONTRADIZ A ESPECIFICAÇÃO 7.2 DA PRÓPRIA ILHA.** O bloco 5b manda agrupar por cidade; a 7.2, escrita quatro dias depois, diz com todas as letras: *"Agrupar por cidade teria sido o erro barato: cada cidade do banco tem **uma** experiência hoje, e categoria nasce com no mínimo três filhas — uma filha por categoria é cluster ralo, que não passa autoridade nenhuma."* Os dois textos estão no mesmo repositório mandando coisas opostas, e o mais novo é o que mediu.

**O QUE EU MEDI, em 27/10/2026, em `dados/experiencias.json`:**

| | contagem |
|---|---|
| experiências | **4** |
| cidades | **4** — Veneza, Siem Reap, Roma, Paris |
| experiências por cidade | **1, 1, 1 e 1** |
| países | **3** — Itália (2 cidades), Camboja (1), França (1) |
| `faixas_diarias` | **0** |
| `coberturas_de_passe` | **0** |

**As três camadas do 5b, uma a uma, contra a régua do contrato:**

- **Camada (1), ficha de experiência — JÁ ESTÁ ENTREGUE, com outro endereço.** Os quatro artigos-âncora do bloco 5 são um por experiência e respondem "quanto custa X" para as quatro. Uma ficha em `/experiencias/<cidade>/<experiencia>/` para as mesmas quatro seria a segunda página na mesma `consulta_alvo`, que a **7.4 proíbe** e o portão de `artigos-referencia.py` reprova. **A camada (1) não é trabalho pendente: ela é trabalho feito que o 5b não sabia que estava feito.**
- **Camada (2), página de cidade — TRAVADA POR DADO.** A 16.5 exige 3 filhas de dado real e a 14.4 exige 3 itens numa listagem. Toda cidade tem **uma** experiência. **Nenhuma das quatro nasce**, e nem a casca nem o Search Console mudam isso.
- **Camada (3), página de país — TRAVADA POR DADO E SEM NÍVEL ONDE MORAR.** Itália tem 2 cidades, Camboja 1, França 1: nenhuma chega a 3 (14.4). E, mesmo com dado, `/experiencias/<cidade>/<experiencia>/` já gasta os três níveis da 16.1, então o país só caberia promovendo-o a nível 1 (`/italia/`) — o que daria três seções de 1 a 2 itens cada, com a palavra que menos vende no topo da árvore de uma ilha cujo recorte é a experiência, não a geografia. **A camada (3) não entra nesta árvore**, e quem a quiser de volta reabre esta seção com dado na mão.
- **Camada (4), cruzamentos — JÁ ESTÁ ENTREGUE, e no lugar certo.** Experiência × número de pessoas é a F1, e cidade × dias é a F2: as duas são paramétricas e moram em `/calculadoras/`, pela 7.4. Como página, o cruzamento já é o artigo em `/guias/quanto-custa/`. **Não existe quarto nível, e não precisa existir.**

**CRITÉRIO PRÉ-REGISTRADO (1.2-b.4), escrito ANTES de o dado chegar — que é o que faz dele critério e não desculpa:**

1. **`/experiencias/<cidade>/` nasce** quando aquela cidade tiver **3 experiências** no banco com dado real, cada uma com preço datado e procedência (13 e 25.2). Antes disso, não nasce nenhuma.
2. **`/experiencias/` (seção) nasce** com a primeira cidade que passar no item 1 — nunca antes, porque seção que lista uma categoria é listagem de um item.
3. **A ficha de experiência só nasce para experiência SEM artigo próprio** em `/guias/quanto-custa/`. Enquanto a correspondência for 1 para 1, a ficha é a segunda página na mesma consulta e a 7.4 a reprova.
4. **A camada de país não nasce** enquanto a 16.1 der três níveis e a experiência os gastar. Se um dia nascer, nasce como nível 1 e com 3 cidades, nunca menos.
5. **Quem abrir qualquer um destes itens RECONTA o banco antes.** Esta tabela é o estado de 27/10/2026, e a contagem em prosa é a coisa que o `ARVORE.md` da robometria já errou duas vezes.

---

## 5. O 5c também é DADO, e o vocabulário já estava lá esperando

O cluster FREE TOUR é o recorte mais rentável que a ilha mediu — a Civitatis paga **€1 fixo por pessoa que comparece**, e o `PROMPT.md` chama o cluster de "a mina escondida". **E ele não depende da casca.**

Medido em 27/10/2026: `free_tour` está no **vocabulário** do `esquema-banco.json` (linha 135) e **zero registros do banco o usam**. É a mesma assinatura de `passe_de_cidade`, que o `PROMPT.md` já descreve como *"no vocabulário desde 14/09/2026 sem um registro que o use"*. Vocabulário sem lastro é o que o próprio `validar-banco.py` avisa.

**O 5c espera coleta**, e a coleta espera o egresso: `civitatis.com.br` está entre os nove domínios recusados, remedidos em 000 hoje. **Critério pré-registrado:** o cluster free tour nasce com **3 free tours de dado real** sob a mãe que o abrigar, cada um com operador nomeado, cidade e a regra da gorjeta já escrita em `constantes.json` — e nunca recomendando "free tour" sem escolher o operador, porque o `REGISTRO.md` já mediu que fazer isso **doa a conversão**.

---

## 6. Ordem das levas, quando destravar (16.6)

Primeiro a mãe e as **3 primeiras filhas de maior intenção de compra**, depois as irmãs, depois a próxima categoria. Nunca uma filha de cada categoria espalhada.

1. **`/guias/quanto-custa/` com as quatro filhas, mais `/calculadoras/` com a F1** — é a única leva que o dado de hoje autoriza. **São 8 URLs de malha**, contadas uma a uma: `/guias/`, `/guias/quanto-custa/`, os quatro artigos, `/calculadoras/` e a F1 — dentro do teto de 10 da 21.4. **A home não entra na conta**, pela 21.7, e as outras quatro páginas da raiz também não. A F1 vem na mesma leva porque os quatro artigos a linkam no corpo e no botão **Calcular**, e artigo que aponta para página inexistente é link morto na primeira leva da ilha.
2. **A F2 e a F3**, quando a coleta destravar — as duas publicam hoje menos do que sabem calcular, por falta de `faixas_diarias` e de passe.
3. **`/experiencias/<cidade>/`** — pelo critério da seção 4, nunca por calendário.
4. **O cluster free tour** — pelo critério da seção 5.

A rampa da seção 9 manda em tudo isto: leva de 5 a 10 páginas, medir, e só dobrar se indexou **e** apareceu. E a 14.9 pede a classificação de SERP das consultas-alvo **antes** de a página nascer — ela não foi feita nesta execução, porque esta nuvem não vê a SERP brasileira (30.8), e fica escrita aqui como pré-requisito da leva 1.

---

## 7. O que este bloco NÃO fez, e por quê

- **Nada foi ao ar, e não podia.** Sem WordPress não há casca, Sync, `/status` nem URL. Dizer que verifiquei no ar seria inventar.
- **Não nasceu portão nenhum.** A 31.2 só deixa nascer portão novo com defeito medido no ar que ele teria pegado, e o que esta execução achou é contradição de documento, não defeito servido. Quando a casca existir, quem a escrever faz o portão desta árvore do jeito que a robometria fez o dela — uma ferramenta que **lê este arquivo** e cobra que ele e o código digam a mesma coisa.
- **Não mudei o `NIVEL_2` de `artigos-referencia.py`.** Está entregue e com portão; mexer nele para resolver a colisão de rótulo seria reescrever código entregue por um problema que o rótulo resolve.
- **Não apaguei o 5b do `PROMPT.md`.** Corrigi o que ele diz e por que, e deixei o bloco de pé: a malha continua sendo trabalho da ilha — o que mudou é que ela espera **dado**, e o número que a destrava está escrito acima.
