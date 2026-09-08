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
