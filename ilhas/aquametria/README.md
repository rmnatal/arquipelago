# Ilha: Aquametria

Primeira ilha do Projeto Arquipelago. Nicho: aquarismo — calculadoras de
dimensionamento e banco de dados tecnico. Marca: Aquametria. O Raphael nao
aparece: sem rosto, sem video, sem forum, sem trafego pago, sem link pago.

## Regra de ouro

**Todo codigo e todo conteudo do site mora aqui, neste repositorio.**
Nada e escrito direto no WordPress. O WordPress e apenas o destino: o
snippet Sync instalado no site le o `manifest.json` desta pasta e aplica o
que estiver marcado para publicar. Se algo existe so no WordPress, esta
errado — traga para ca primeiro.

## Estrutura

| Pasta | O que guarda |
|---|---|
| `snippets/` | PHP dos snippets do Code Snippets (calculadoras, widget, endpoints) |
| `conteudo/` | Artigos-ancora, paginas e paginas programaticas, em Markdown |
| `dados/` | Banco normalizado de produtos e constantes tecnicas, em JSON/CSV |
| `manifest.json` | Indice que o snippet Sync consome |
| `ferramentas/` | Scripts do repositorio (validacao do banco, geradores de catalogo, testes). NUNCA vao para o site |

## Casca do site

`snippets/aquametria-casca.php` e o snippet que da cara de Aquametria ao tema
ativo: paleta, tipografia, logotipo em SVG, menu, rodape e as quatro paginas
institucionais (`inicio`, `calculadoras`, `metodologia`, `sobre`), cujo texto
mora em shortcodes do proprio snippet — editar o snippet edita as paginas.
Ele e idempotente e manda "Hello world!" e "Sample Page" para a lixeira, nunca
para o apagador. **Toda calculadora publicada precisa entrar na lista de
`aquametria_casca_calculadoras()`** (ou se registrar pelo filtro
`aquametria_calculadoras`), senao some do hub.

Desde a versao 1.3.0 (09/09/2026) ela tambem cuida de duas coisas de celular e de
aba:

- **Menu sanfona abaixo de 782 px.** Os tres links saem SEMPRE no HTML servido,
  dentro de `<nav>`; quem esconde a lista e o seletor
  `.aqm-nav-caixa[data-aqm-menu]`, e esse atributo quem poe e o JavaScript do
  rodape. **Sem JavaScript o menu nao some** — volta a ser a fileira de links,
  que e o que o crawler de IA recebe. Nao inverta isso.
- **Icone do site.** A casca tira o `wp_site_icon` do WordPress do `wp_head` e
  publica o recipiente graduado da marca como data URI (SVG na aba, PNG de 32 px
  alternativo, `apple-touch-icon` de 180 px). Nada sobe para a biblioteca de
  midia. **O desenho nao se edita a mao no snippet**: ele mora entre os
  marcadores `FAVICON-INICIO` e `FAVICON-FIM` e sai de

  ```
  php ferramentas/gerar-favicon.php .            # so o snippet
  php ferramentas/gerar-favicon.php . /tmp/i.png # e uma copia para olhar
  ```

E a casca tem teste de navegador proprio, porque o cabecalho nao vem de
shortcode nenhum — vem do filtro `render_block`, e o `render-para-teste.php`
monta pagina de calculadora:

```
php ferramentas/render-casca-para-teste.php . > /tmp/casca.html
node ferramentas/teste-navegador-casca.mjs /tmp/casca.html
```

Ele confere o menu no desktop e no celular (clique, Escape com o foco de volta no
botao, Enter, Tab, clique fora, alargar a janela), o mesmo celular **com o
JavaScript desligado** — onde os tres links tem de continuar visiveis — e mede os
tres icones por `naturalWidth`, alem de conferir que o icone do WordPress sumiu do
`wp_head`.

## Contrato do manifest

`manifest.json` lista `snippets`, `conteudo` e `dados`. O bloco `esquema`
documenta os campos de cada entrada. Dois campos governam a publicacao:

- `publicar` — `true` faz o Sync aplicar o item no site. Desde 07/09/2026 o
  desembarque e automatico para snippet de site, calculadora, pagina-ancora e
  artigo; so conteudo programatico em escala continua `false` esperando o
  Raphael (`desembarque.aprovado` no manifest guarda essa decisao).
- `sha256` — o Sync confere o hash depois de gravar. Nunca confie na
  ausencia de erro: em hospedagem compartilhada o ModSecurity pode matar a
  gravacao em silencio.

Ao alterar qualquer item, incremente `revisao` e atualize `atualizado_em`.

## Procedencia

Nenhuma constante, especificacao ou preco entra sem fonte do fabricante e
data de verificacao. Isso vale para `dados/` e para toda tabela em
`conteudo/`.

No banco de produtos a procedencia e por CAMPO, nao por registro: cada
produto lista em `fontes[]` quem sustenta cada campo, com url, data e nivel
de confianca. O modelo completo esta em `dados/modelo-banco-produtos.md` e o
contrato formal em `dados/esquema-produtos.json`.

## Antes de commitar mudanca no banco de produtos

```
cd ilhas/aquametria && python3 ferramentas/validar-produtos.py
```

E o banco de especies tem validador proprio, com regras proprias:

```
cd ilhas/aquametria && python3 ferramentas/validar-especies.py
```

Sai 0 sem erro, 1 com erro. O script confere as regras V1 a V18 do esquema
(campo sem fonte, derivado gravado a mao, preco dentro do arquivo de produto,
conflito sem status, PPFD sem distancia, status incoerente, link de afiliado mal
formado, intersecao conservadora que nao e a intersecao) e imprime quais produtos
cada calculadora consegue sugerir. Avisos nao reprovam: viram tarefa de coleta.

**O banco viaja dentro do snippet.** O site nao le este repositorio em tempo de
execucao, entao cada calculadora com bloco de produto carrega uma copia do banco
no proprio PHP, entre os marcadores `CATALOGO-INICIO` e `CATALOGO-FIM`. Depois de
mexer em `dados/produtos-*.json`, rode o gerador da calculadora afetada, ou as
duas copias divergem em silencio:

```
python3 ferramentas/gerar-catalogo-filtros.py       # C3
python3 ferramentas/gerar-catalogo-aquecedores.py   # C5
python3 ferramentas/gerar-catalogo-midias.py        # C12 (midias E filtros)
python3 ferramentas/gerar-catalogo-iluminacao.py    # C15 (aptas E barradas)
```

Os geradores da C3 e da C5 imprimem no fim a linha `vitrine: N de M com link de
loja, K com foto`. **Essa e a medida certa de quanto uma calculadora tem para
mostrar numa vitrine**, e nao a contagem no banco: o banco tem registros que o
`minimo_para_sugerir` barra, e em 10/09/2026 a C5 mostrou por que isso importa —
11 dos 27 aquecedores do banco tem foto, e so 2 dos 18 do catalogo, porque 9 dos
com foto sao justamente os barrados. Conte depois do portao, nunca antes.

O gerador da C15 tambem escreve DOIS blocos, mas por outro motivo: o das
luminarias APTAS e o das BARRADAS com o motivo de cada uma, porque a C15 publica
essa lista na tela — quem nao pode ser sugerido, e por que, e o conteudo daquela
entidade. E ele manda a ESTRUTURA do conflito de comprimento, nunca o texto: o
banco e escrito sem acento e a tela sai acentuada, entao a frase e escrita no
JavaScript do snippet. Texto de banco nunca vai para a tela.

O gerador da C12 escreve DOIS blocos no mesmo snippet, porque ela consome os
dois bancos: as midias (`produtos-midia.json`) para o bloco de produto e a
dosagem, e os filtros que declaram `volume_filtragem_L` (`produtos-filtro.json`)
para o teto fisico do cesto. Mexeu em qualquer um dos dois, rode este tambem.

## Antes de marcar uma calculadora como publicar=true

Alem do `php -l` de verdade e do `ferramentas/proteger-funcoes.php`, a
calculadora passa por um navegador antes de ir ao ar:

```
npm i --no-save playwright@1.56.1
php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor > /tmp/c5.html
node ferramentas/teste-navegador-c5.mjs /tmp/c5.html

php ferramentas/render-para-teste.php . aquametria_calculadora_midia > /tmp/c12.html
node ferramentas/teste-navegador-c12.mjs /tmp/c12.html

php ferramentas/render-para-teste.php . aquametria_calculadora_iluminacao > /tmp/c15.html
node ferramentas/teste-navegador-c15.mjs /tmp/c15.html
```

O `render-para-teste.php` monta a pagina com funcoes falsas do WordPress (o
calculo todo e JavaScript no navegador, entao nao falta nada) e carrega todos os
snippets menos o Sync — o que tambem testa a convivencia entre as calculadoras.

E, desde 09/09/2026, uma calculadora tambem passa pelo teste de **visibilidade
em IA** — o que a Sentinela Tecnica mediu a mao naquele dia e encontrou zero em
13 de 13 paginas:

```
node ferramentas/teste-navegador-visibilidade-ia.mjs /tmp
```

Ele abre a pagina com o **JavaScript DESLIGADO**, que e o que um crawler de IA
recebe, e e a unica prova honesta de que o numero esta no HTML servido e nao foi
desenhado pela calculadora depois. Confere JSON-LD que faz parse, `WebApplication`
com `applicationCategory`/`featureList`/`isAccessibleForFree`/`publisher`,
`FAQPage` com respostas que carregam numero, a tabela de exemplos cobrindo 30,
60, 100, 150, 200 e 300 L, o bloco de resposta direta ANTES do formulario — e
que, sem JavaScript, o container de resultado continua **oculto**: numero de
resultado sem entrada seria pior que formulario vazio.

E a protecao das funcoes se confere sem reescrever o arquivo:

```
python3 ferramentas/conferir-protecao-funcoes.py snippets/*.php
```

`ferramentas/proteger-funcoes.php` TRANSFORMA o arquivo, entao nao serve como
verificacao antes do commit. Este sai 0 sem problema e 1 com problema, nomeando
a funcao e a linha.

## Cobertura de faixa: a medida que substituiu "60 produtos"

A secao 14.3 do `ARQUIPELAGO.md` diz que o tamanho do banco nao e um numero
redondo, e sim **cobertura**: nenhuma faixa que as calculadoras conseguem
produzir pode sair com menos de 3 produtos elegiveis. Quem mede isso e

```
php ferramentas/render-para-teste.php . aquametria_calculadora_vazao      > /tmp/c3.html
php ferramentas/render-para-teste.php . aquametria_calculadora_aquecedor  > /tmp/c5.html
php ferramentas/render-para-teste.php . aquametria_calculadora_midia      > /tmp/c12.html
php ferramentas/render-para-teste.php . aquametria_calculadora_iluminacao > /tmp/c15.html
node ferramentas/varrer-cobertura.mjs /tmp > /tmp/cobertura.md
```

Ele abre cada calculadora num Chromium de verdade e a preenche **ponto a ponto**
ao longo da faixa de entrada declarada, em cada combinacao de condicao que a
tela oferece, e conta os cartoes de produto que apareceram. **Nao reimplementa
regra de selecao nenhuma**, e isso e o ponto: uma segunda copia da regra em
Python divergiria da calculadora em silencio, que e o mesmo defeito que os
geradores de catalogo existem para impedir.

A saida e markdown e vai para `dados/cobertura-de-faixa.md`, que e **historico**:
cada medicao vira uma secao nova, nunca sobrescreve a anterior. Faixa vazia ou
com menos de 3 itens nao e erro de codigo — e a **lista de compras do banco**, e
e ela que decide qual produto vale coletar em seguida. Produto que nao fecha
nenhuma faixa descoberta nao e prioridade, por melhor que seja a comissao.

## Visibilidade em IA: onde ela mora no codigo

A regra de primeira classe do projeto (08/09/2026) diz que toda pagina precisa
ser legivel e citavel por um modelo de linguagem, nao so rastreavel pelo
Googlebot. Nas calculadoras isso se traduz em tres funcoes por snippet, e uma
regra sobre onde cada coisa sai:

| Funcao | O que entrega | Onde sai |
|---|---|---|
| `aquametria_cN_resposta_direta_html()` | O numero, o criterio e a procedencia na propria frase, ANTES do formulario | retorno do shortcode |
| `aquametria_cN_exemplos_html()` | Tabela de 30/60/100/150/200/300 L resolvida no PHP | retorno do shortcode |
| `aquametria_cN_imprimir_jsonld()` | `WebApplication` e `FAQPage` | **`wp_head`** |

O JSON-LD sai no `wp_head` **pelo mesmo motivo que o script sai no `wp_footer`**:
o retorno do shortcode atravessa os filtros do `the_content`, que trocam cada
`&` pela entidade numerica dele — e isso quebraria o JSON tanto quanto quebrou o
JavaScript em 08/09/2026.

**A tabela pre-renderizada e a calculadora nao podem divergir.** Por isso as
constantes que as duas usam moram no PHP e viajam para o script como variavel:
`AQM_C3_BANDAS` na C3, `AQM_C5_REGRAS` e `AQM_C5_LINHA` na C5. Nada de faixa
escrita duas vezes. O teste de visibilidade confere isso de fato: compara o
numero da tabela servida para 100 L com o numero que a calculadora devolve para
100 L.
