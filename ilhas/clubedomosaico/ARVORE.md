# ÁRVORE DO CLUBE DO MOSAICO

Item (i) do 16.8 do `ARQUIPELAGO.md`, escrito em 11/09/2026 no bloco da árvore.

Este arquivo diz **onde cada página mora** e **quem é a mãe de quem**. É o mapa que os blocos seguintes seguem: breadcrumb, cluster de interlinkagem e leva de malha saem daqui, nunca da cabeça de quem executa. O código lê o mesmo mapa, e `ferramentas/teste-casca.php` cobra que os dois digam a mesma coisa — documento e código mantidos à mão em dois lugares divergem em silêncio (seção 8 do contrato).

Os nomes dos níveis são os do `VOZ.md`: quem decide como a seção se chama é a pessoa que digita, não a fábrica.

---

## 1. Os três níveis

**Nível 1 — a seção.** Três, uma por motor da ilha, e **as três já existem como página**:

| slug | motor | o que mora ali | existe hoje |
|---|---|---|---|
| `/loja/` | LOJA | as peças da artesã, margem cheia | **sim** |
| `/materiais/` | GUIA | as fichas de material, com afiliado | **sim** |
| `/como-fazer/` | ESCOLA | os passo a passo | **sim** |

Esta ilha nasce com vantagem sobre as duas primeiras: na Aquametria e na Robometria o nível 1 ainda é página inexistente, e a trilha sai com degrau em texto. Aqui os três degraus de topo são link de verdade desde o primeiro dia.

**Nível 2 — a categoria**, com o nome que a pessoa usa. **Categoria só nasce com 3 filhas de dado real** (16.5); até lá o cartão na mãe não é link e diz "em breve", **sem contagem de banco**.

**Nível 3 — a pergunta, a ficha ou a peça**, com as palavras que a pessoa digita.

Sem quarto nível. Fora da árvore ficam só a home, `/sobre/`, `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/` — exatamente a lista que a 16.1 admite na raiz.

---

## 2. `/materiais/` — o Guia

| nível 2 | slug | banco hoje | existe |
|---|---|---|---|
| Colas e adesivos | `/materiais/colas-e-adesivos/` | 5 itens | não |
| Rejuntes | `/materiais/rejuntes/` | 5 itens | não |
| Pastilhas e tesselas | `/materiais/pastilhas/` | 0 | não |
| Alicates e corte | `/materiais/alicates-e-corte/` | 0 | não |
| Bases | `/materiais/bases/` | 0 | não |
| Acabamento | `/materiais/acabamento/` | 0 | não |
| Como sabemos | `/materiais/como-sabemos/` | — | **sim** |

**Nenhuma das seis categorias atinge as 3 filhas com dado real hoje**, então nenhuma nasce agora — é a 16.5, e ela é o que impede a ilha de publicar seis páginas magras num domínio que ainda não indexou nada. Colas e Rejuntes têm banco, mas banco não é filha: filha é página de nível 3 publicada.

**Dois slugs mudaram neste bloco, e nenhuma URL se moveu**, porque nenhuma das duas páginas existe: `materiais/colas` virou `materiais/colas-e-adesivos` e `materiais/alicates` virou `materiais/alicates-e-corte`, que são os nomes escritos no `VOZ.md`. O registro da casca e o `VOZ.md` diziam coisas diferentes desde que a casca nasceu; o dia de acertar isso é o dia **antes** de a página existir, não depois.

`/materiais/como-sabemos/` é a única página de nível 2 no ar. Ela é a camada de prova da ilha (15.2), nasce `noindex` e fora do sitemap — está na árvore para ter mãe e trilha, não para disputar busca.

**As duas ferramentas (bloco 4)** são nível 3 e a mãe delas é `/materiais/` **direto**, dois níveis em vez de três — estado de transição declarado, não desenho, como o `/calculadoras/` da Aquametria. A categoria definitiva de cada uma se decide no bloco que as publica, e nem antes nem por este arquivo:

| ferramenta | slug | mãe | existe hoje | candidata a nível 2 |
|---|---|---|---|---|
| F2 — qual cola usar no mosaico, e qual rejunte | `/materiais/qual-cola-usar-no-mosaico/` | `/materiais/` | **sim**, desde 11/09/2026 | `colas-e-adesivos` |
| F1 — quantas pastilhas e quanto rejunte | `quantas-pastilhas-para-mosaico` | `/materiais/` | não | `pastilhas` ou `rejuntes` — a F1 atravessa as duas, e é por isso que a escolha espera o bloco que a publica |

**A F2 nasceu em `/materiais/` e não em `/materiais/colas-e-adesivos/`, e a escolha é do bloco que a publicou.** A categoria definitiva dela só pode nascer com três filhas de dado real (16.5), e hoje ela teria uma. Pôr a ferramenta debaixo de uma categoria que ainda não existe criaria um degrau de trilha sem endereço — e, pior, obrigaria a mover a URL no dia em que a categoria nascesse, o que a 12.1 proíbe para página com impressão registrada. A regra que fica para as próximas: **a mãe de hoje é a mãe que já tem endereço**, e a mudança de pai, quando vier, será uma decisão com 301 e sitemap reenviado, tomada olhando a posição da página.

## 3. `/loja/` — as peças

Nível 2 pelo tipo de peça, com o nome que a pessoa busca: `/loja/vasos/`, `/loja/colares/`, `/loja/quadros/`, `/loja/espelhos/`, `/loja/cachepos/`.

**Nenhuma nasce antes da primeira peça cadastrada.** O catálogo é cadastrado pela própria artesã no painel `/atelie/` (bloco 4d) e não vive no repositório — então aqui a 16.5 não é só uma contagem, é a diferença entre coleção e vitrine de mentira. Enquanto não houver peça, `/loja/` é página única com estado vazio honesto.

Nível 3 = a peça, com `Product` + `Offer`, preço real e prazo. Peça própria **nunca** leva `rel="sponsored"`.

## 4. `/como-fazer/` — a Escola

Nível 2 pelo tipo de peça que a pessoa vai fazer: `/como-fazer/vasos/`, `/como-fazer/quadros-e-espelhos/`, `/como-fazer/bijuteria/`, `/como-fazer/mesas-e-tampos/`.

Nível 3 = o tutorial, com a lista de materiais ligada ao Guia e o "prefere pronto?" ligado à Loja — é o cluster que fecha o ciclo comercial dos três motores.

**Nenhum tutorial existe hoje.** A `pauta.md` da seção 17 ainda não chegou a esta pasta; quando chegar, os guias entram por cluster (16.6), não um de cada categoria.

---

## 5. Onde mora cada página que existe HOJE

| página | nível | mãe | trilha na tela |
|---|---|---|---|
| `/` (home) | — | — | nenhuma (16.3) |
| `/loja/` | 1 | home | Início › Loja |
| `/materiais/` | 1 | home | Início › Materiais |
| `/como-fazer/` | 1 | home | Início › Como fazer |
| `/materiais/como-sabemos/` | 2 | `/materiais/` | Início › Materiais › Como sabemos |
| `/materiais/qual-cola-usar-no-mosaico/` | 3 | `/materiais/` | Início › Materiais › Qual cola usar no mosaico, e qual rejunte |
| `/sobre/` | raiz | — | Início › Sobre |
| `/contato/` | raiz | — | Início › Contato |
| `/divulgacao-de-afiliados/` | raiz | — | Início › Divulgação de afiliados |
| `/privacidade/` | raiz | — | Início › Privacidade |

**Nenhuma página mudou de endereço neste bloco, e nenhuma precisou mudar** — as três seções já eram nível 1, a única página de nível 2 já nascera com mãe em 1.2.0, e as quatro da raiz são as que a 16.1 admite ali. Por isso este bloco não tem 301 nenhum e o sitemap não muda: a árvore desta ilha estava certa na estrutura e faltava ficar **visível** (breadcrumb, schema, cluster), que é o que a 16.3 e a 16.4 pedem.

---

## 6. O cluster, e as duas coisas que ele NÃO faz

**16.4(a) — a mãe lista as filhas.** `/materiais/` lista as seis categorias (cartão "em breve" enquanto a página não existe), **lista as duas ferramentas** desde a casca 1.5.0 e cita `/materiais/como-sabemos/` no corpo. A listagem das ferramentas entrou no bloco 4, e a falta dela era invisível enquanto nenhuma existia: no dia em que a primeira nasceu, ela viraria página órfã pela 16.4(f), que cobra dois links internos e um deles da mãe. `/loja/` e `/como-fazer/` ainda não têm filha para listar, e listagem que promete o que não existe é pior que listagem curta.

**16.4(b) — a filha linka a mãe no breadcrumb e numa frase do corpo.** Vale para nível 2 e 3, cuja mãe é uma página de conteúdo. Para o nível 1 a mãe é a home, que já é link em toda página pela marca do cabeçalho e pelo primeiro degrau da trilha — cobrar uma frase no corpo apontando para a home seria cobrar ruído.

**16.4(c) — de 2 a 4 irmãs.** As três seções de nível 1 são irmãs entre si, então cada uma lista as outras duas: é o ciclo LOJA → GUIA → ESCOLA, e é o único cluster que a ilha tem matéria para fazer hoje. `/materiais/como-sabemos/` **não recebe bloco "Veja também"**, porque não existe uma segunda página de nível 2 para ser irmã dela — e irmã inventada é link morto. O portão mede as duas direções: página com 2 ou mais irmãs no ar **tem** que publicar o bloco; página com menos de 2 **não** pode publicar um.

**Por que o teto de 4 é medido mesmo sem haver 5 irmãs no mundo:** com três seções, nenhuma página chega a ter cinco candidatas, e trocar o teto de 4 por 5 não mudaria uma linha do que o site serve — grade que não pisa na borda (seção 8). A bancada, então, **fabrica a borda**: o modo `todas` põe as seis categorias do Guia no ar e aí `/materiais/como-sabemos/` tem cinco irmãs candidatas e o teto tem o que cortar.

**16.4(f) — nenhuma órfã.** Toda página do sitemap tem pelo menos dois links internos: as três seções vêm do menu e do corpo da home; `/sobre/` vem do menu e do rodapé; `/contato/`, `/divulgacao-de-afiliados/` e `/privacidade/` vêm do rodapé e do corpo de pelo menos uma página. `/materiais/como-sabemos/` está fora do sitemap por ser `noindex`, e mesmo assim é citada no corpo do Guia.

---

## 7. O `BreadcrumbList`, e por que ele publica menos do que a trilha mostra

O schema leva **só os degraus que têm endereço de verdade**, mais a página atual. Um `ListItem` do meio sem `item` invalida a lista inteira para o Google, e lista inválida é lista ignorada — o schema "mais completo" publicaria MENOS com cara de publicar mais.

Hoje isso não corta nada nesta ilha, porque os três degraus de nível 1 existem. **Ele existe para o dia em que uma categoria de nível 2 aparecer na trilha antes de ter página** — que é o estado normal das outras duas ilhas e será o desta assim que a primeira ficha de material nascer.

---

## 8. O que este bloco NÃO fez, de propósito

- **Não criou nenhuma URL.** As dez páginas de nível 2 desta árvore (seis do Guia, mais as da Loja e da Escola) esperam a 16.5, que é portão de dado e não de calendário.

> **ATUALIZAÇÃO DO BLOCO 4 — 11/09/2026.** Nasceu a primeira URL de nível 3 da ilha, `/materiais/qual-cola-usar-no-mosaico/`, e ela é a única. As dez páginas de nível 2 continuam esperando a 16.5. A F2 tem **uma** irmã no ar (`/materiais/como-sabemos/`), então ela **não** publica bloco "Veja também" — é a regra da seção 6 deste arquivo funcionando pela primeira vez num caso real, e a frase que linka a mãe (16.4b) sai no corpo da ferramenta, onde o cluster não chega. O primeiro **degrau de trilha sem página**, que a bancada fabricou em 11/09 para ter o que medir, continua sem caso real: os três degraus da trilha da F2 — Início, Materiais e ela mesma — têm endereço.
- **Não mexeu no sitemap.** Nenhuma página mudou de endereço, então não há nada a reenviar além do que já está enviado.
- **Não escolheu a categoria definitiva das duas ferramentas.** Quem publica a página escolhe o endereço dela; este arquivo registra as candidatas para a escolha não nascer do zero.
