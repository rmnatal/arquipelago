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
| `ferramentas/` | Scripts do repositorio (validacao do banco). NUNCA vao para o site |

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

Sai 0 sem erro, 1 com erro. O script confere as regras V1 a V14 do esquema
(campo sem fonte, derivado gravado a mao, preco dentro do arquivo de produto,
conflito sem status, PPFD sem distancia, status incoerente) e imprime quais
produtos cada calculadora consegue sugerir. Avisos nao reprovam: viram tarefa
de coleta.
