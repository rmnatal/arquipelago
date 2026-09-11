# ÁRVORE DA ROBOMETRIA

Item (i) do 16.8 do `ARQUIPELAGO.md`, escrito em 11/09/2026 no bloco da árvore — o item que o despacho do Raphael de 11/09 deixou de pé depois do bloco da voz.

Este arquivo diz **onde cada página mora** e **quem é a mãe de quem**. É o mapa que os blocos seguintes seguem: breadcrumb, cluster de interlinkagem e leva de malha saem daqui, não da cabeça de quem executa. `ferramentas/teste-arvore.php` lê este arquivo e cobra que ele e o código digam a mesma coisa — documento e código mantidos à mão em dois lugares divergem em silêncio.

Os nomes dos níveis são os do `VOZ.md`: quem chega aqui diz peça, sucção, modelo. Não existe `/entidades/` nem `/cruzamentos/` nesta ilha, porque ninguém digita isso.

---

## 1. Os três níveis

**Nível 1 — seção.** Quatro, e só estas:

| slug | o que mora ali | existe hoje |
|---|---|---|
| `/pecas/` | a peça que serve: a ferramenta de compatibilidade e as categorias por tipo de peça | não |
| `/succao/` | quanta sucção e quanto tempo: a ferramenta de dimensionamento e os cruzamentos de piso, pelo e metragem | não |
| `/modelos/` | a ficha de cada robô, por marca — o que o fabricante declarou dele | não |
| `/guias/` | os textos que explicam o porquê do número | não |

**Nível 2 — categoria**, com o nome que a pessoa usa. **Categoria só nasce com 3 filhas de dado real** (16.5); até lá o cartão na mãe não é link e diz "em breve", sem contagem.

| nível 2 | mãe | filhas previstas |
|---|---|---|
| `/pecas/filtros/` | `/pecas/` | filtro por modelo e por marca |
| `/pecas/escovas-laterais/` | `/pecas/` | escova lateral por modelo |
| `/pecas/escovas-principais/` | `/pecas/` | escova rotativa central por modelo |
| `/pecas/mops/` | `/pecas/` | pano e suporte por modelo |
| `/pecas/baterias/` | `/pecas/` | bateria por modelo |
| `/succao/pisos-e-pelo/` | `/succao/` | quantos Pa por tipo de piso e por pelo |
| `/succao/metragem-e-autonomia/` | `/succao/` | quantos ciclos por metragem |
| `/modelos/electrolux/` | `/modelos/` | ficha por modelo da marca |
| `/modelos/multi/` | `/modelos/` | idem |
| `/modelos/positivo/` | `/modelos/` | idem |
| `/modelos/xiaomi/` | `/modelos/` | idem |
| `/modelos/wap/` | `/modelos/` | idem |
| `/guias/pecas/` | `/guias/` | os textos sobre peça e compatibilidade |
| `/guias/succao/` | `/guias/` | os textos sobre sucção, autonomia e metragem |

**`/pecas/reservatorios/` não está na lista de propósito.** O tipo "reservatório" existe no vocabulário do banco e não tem **nenhuma** peça declarada — é o mesmo motivo pelo qual ele já saiu do seletor da ferramenta. Categoria sem filha é página fina, e página fina em domínio novo gasta orçamento de rastreamento (14.1).

**Nível 3 — a pergunta ou a ficha**, com as palavras que a pessoa digita.

Sem quarto nível.

---

## 2. Fora da árvore, na raiz

| slug | por quê |
|---|---|
| `inicio` | a home. Sem breadcrumb (16.3) |
| `sobre` | a 16.1 admite na raiz |
| `divulgacao-de-afiliados` | a 16.1 admite na raiz |
| `metodologia` | ver o veredito abaixo |
| `ferramentas` | ver o veredito abaixo — é a **mãe de transição**, não uma página de raiz permanente |

**VEREDITO SOBRE `/metodologia/` — fica na raiz.** A lista da 16.1 (home, sobre, contato, divulgação de afiliados, privacidade) nomeia uma **família**: a página institucional, que fala da casa e não do assunto. A metodologia é dessa família — é o "como trabalhamos" ao lado do "quem somos" —, e pô-la dentro de uma seção de tópico a faria filha de um assunto que ela não tem. A Aquametria resolveu do mesmo jeito em 11/09/2026, e duas ilhas resolvendo diferente o mesmo caso seria a fábrica decidindo por gosto.

**VEREDITO SOBRE `/ferramentas/` — fica hoje, e é a única página desta ilha com prazo de validade.** Ela é um hub que lista as duas ferramentas, que é exatamente o que uma página de nível 1 faz. Enquanto `/pecas/` e `/succao/` não existem, ela é a **mãe de transição** das duas ferramentas: dá a elas um degrau de trilha com endereço de verdade, em vez de um degrau em texto apontando para o vazio. No dia em que as duas seções nascerem, ela passa a servir a mesma listagem que elas — duas URLs com o mesmo conteúdo, que a 14.4 proíbe — e **é retirada com 301 para a home**, que nesta ilha já é a ferramenta (molde FERRAMENTA do `VOZ.md`). Isso não acontece neste bloco: hoje ela é a mãe, e retirar a mãe antes de a substituta existir deixaria as duas ferramentas sem trilha.

---

## 3. Onde mora cada página de hoje

| página | papel | mãe de hoje | mãe de destino | irmãs de hoje |
|---|---|---|---|---|
| `inicio` | home | — | — | — |
| `ferramentas` | seção (transição) | — | — | — |
| `metodologia` | raiz | — | — | — |
| `sobre` | raiz | — | — | — |
| `divulgacao-de-afiliados` | raiz | — | — | — |
| `qual-peca-serve-no-meu-robo-aspirador` | filha | `/ferramentas/` | `/pecas/` | a outra ferramenta |
| `quantos-pa-o-robo-aspirador-precisa` | filha | `/ferramentas/` | `/succao/` | a outra ferramenta |
| `filtro-universal-de-robo-aspirador` | filha | `/guias/` (não existe) | `/guias/pecas/` | o outro guia |
| `quantos-m2-o-robo-aspirador-limpa-por-carga` | filha | `/guias/` (não existe) | `/guias/succao/` | o outro guia |

---

## 4. O que este bloco fez, e o que ele NÃO fez

**FEITO** (casca 1.3.0, 11/09/2026), e **nenhuma URL nova**:

- **Trilha** (16.3) nas oito páginas que não são a home, sempre entre o cabeçalho e o H1.
- **`BreadcrumbList`** em JSON-LD, levando só os degraus com endereço de verdade.
- **"Veja também"** (16.4c) nas quatro páginas de conteúdo, com as irmãs derivadas.
- **Frase que linka a mãe** (16.4b) nas duas ferramentas, com a contagem **contada**.
- **O par ferramenta ↔ guia** (16.4d) fechado nos dois sentidos — faltava um lado, ver abaixo.

**NÃO FEITO, e por quê:** as quatro páginas de nível 1 e as quatorze de nível 2 são dezoito URLs novas, e esta ilha não publica leva de malha enquanto o sitemap não for reenviado no Search Console (metade humana do despacho da Sentinela de 10/09; a rampa da seção 14 é inexecutável sem medição). Trocar o pai e o slug das páginas existentes espera o mesmo destravamento, e leva 301 quando acontecer.

**Quatro coisas que quem vier depois precisa saber:**

1. **O degrau sem endereço sai em TEXTO, nunca em link, e não entra no JSON-LD.** A trilha de um guia mostra quatro degraus na tela (Início › Guias › Peças › o título) e o `BreadcrumbList` publica dois. Não é esquecimento: `ListItem` do meio sem `item` invalida a lista inteira para o Google, e lista inválida é lista ignorada — o schema "mais completo" publicaria MENOS com cara de publicar mais. Quando `/guias/` nascer, ela entra nos dois lados de uma vez, porque quem resolve o endereço é `robometria_casca_url_se_existir()`.
2. **As irmãs são derivadas, nunca digitadas.** Saem do mesmo registro que alimenta o hub e a prateleira de artigos. Ferramenta ou artigo novo vira irmã de todo mundo sozinho, e página que não existe publicada não entra — irmã é link, e link morto não é cluster.
3. **Hoje cada mãe tem duas filhas, então cada filha tem UMA irmã — e a 16.4(c) pede de 2 a 4.** É estado de transição declarado, não desenho: o mínimo de duas é alcançado no dia em que a terceira filha de uma mãe nascer. O portão cobra "todas as irmãs publicadas, teto de 4" e a bancada **fabrica a borda** (um catálogo de seis filhas) para provar que o teto corta — grade que nunca pisa na borda é amostra com nome de grade.
4. **A frase de mãe só sai com mãe publicada.** As duas ferramentas a têm, porque `/ferramentas/` existe; os dois guias não a têm, porque `/guias/` não existe, e o portão cobra a AUSÊNCIA dela justamente para ninguém fechar isso com um endereço inventado.

**O DEFEITO QUE A VARREDURA DE LINKS ACHOU SEM PROCURAR:** medindo qual página cita qual no CORPO, a ferramenta de sucção linkava o guia do filtro universal e **não linkava o guia dela**, o de metros quadrados por carga — que é justamente o texto que explica de onde vem o número de área por carga que ela usa. O par da 16.4(d) estava aberto de um lado só, e ninguém tinha como ver, porque o link existia (para o outro guia) e nenhum teste perguntava se era o guia CERTO. Agora o par sai do catálogo de artigos, pelo campo `ferramenta`, e o portão cobra os dois sentidos.

**E um achado que fica registrado, fora do escopo:** `/sobre/` é a única das nove páginas que nenhum CORPO de outra cita — ela vive do menu e do rodapé, que estão em todas, então não é órfã pelo 16.4(f). Mas é a única sem citação editorial, e isso é assunto de pauta (seção 17), não de casca. A Aquametria tem exatamente o mesmo achado, o que sugere que é do molde da casca e não da ilha.

---

## 5. Ordem das levas, quando destravar (16.6)

Primeiro a mãe e as **3 primeiras filhas de maior intenção de compra**, depois as irmãs, depois a próxima categoria. Nunca uma filha de cada categoria espalhada.

1. `/pecas/` + `/pecas/filtros/` com as 3 primeiras filhas — é o cluster de maior intenção de compra da ilha ("filtro para robô X" termina numa peça que se compra), e é onde o banco tem mais pares declarados.
2. `/succao/` + `/succao/pisos-e-pelo/` — a segunda ferramenta ganha a mãe própria e `/ferramentas/` é retirada com 301.
3. `/guias/` + `/guias/pecas/`, com os temas da `pauta.md` (seção 17) que apontam para a ferramenta de peças.
4. `/modelos/<marca>/` — por último, e só depois de o cluster de peças estar indexado: ficha de modelo compete com o fabricante e com o marketplace (14.2, item 4), então ela só nasce onde carrega um número que eles não dão.

**O menu, quando as seções existirem.** O `VOZ.md` descreve Peças · Modelos · Guias. Hoje ele é Peças · Sucção · Como conferimos, porque esses três são onde a pessoa resolve o problema e os outros sairiam como `<span>`. Quando `/pecas/` e `/succao/` nascerem, os dois primeiros rótulos passam a apontar para as SEÇÕES em vez das ferramentas — mesmo rótulo, endereço melhor — e `/guias/` entra no lugar de "Como conferimos", que volta para o rodapé. `/modelos/` não entra no menu: ele é a camada de entidade, alcançada pela ferramenta de sucção e pelas fichas, e um menu de quatro itens em celular é uma lista, não um menu.

A rampa da seção 9 manda em tudo isto: leva de 5 a 10 páginas, medir em `dados/indexacao.md`, e só dobrar se indexou **e** apareceu.
