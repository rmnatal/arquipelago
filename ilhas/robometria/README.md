# Ilha: Robometria

Segunda ilha do Projeto Arquipelago. Nicho: robo aspirador — compatibilidade
de pecas e consumiveis (qual filtro HEPA, escova lateral e mop servem em qual
modelo) e dimensionamento (Pa de succao por tipo de piso e pelo, autonomia por
m2). Marca: Robometria. O Raphael nao aparece: sem rosto, sem video, sem forum,
sem trafego pago, sem link pago.

Leia o `ARQUIPELAGO.md` da raiz antes de qualquer coisa: ele carrega as regras
comuns a todas as ilhas. O `PROMPT.md` desta pasta tem so o que e daqui.

## Regra de ouro

**Todo codigo e todo conteudo do site mora aqui, neste repositorio.**
Nada e escrito direto no WordPress. O WordPress e apenas o destino: o
snippet Sync instalado no site le o `manifest.json` desta pasta e aplica o
que estiver marcado para publicar. Se algo existe so no WordPress, esta
errado — traga para ca primeiro.

## Estrutura

| Pasta | O que guarda |
|---|---|
| `snippets/` | PHP dos snippets do Code Snippets (ferramentas, widget, endpoints) |
| `conteudo/` | Artigos-ancora, paginas e paginas programaticas, em Markdown |
| `dados/` | Banco normalizado de modelos, pecas e constantes tecnicas, em JSON/CSV |
| `manifest.json` | Indice que o snippet Sync consome |
| `ferramentas/` | Scripts do repositorio (validacao do banco, geradores, testes). NUNCA vao para o site |

## Estado da infraestrutura

O dominio robometria.com.br foi registrado em 09/09/2026 e ja e dominio
adicional no cPanel da HostGator, com raiz propria; os nameservers ns604 e
ns605.hostgator.com.br estao apontados no registro.br. **O WordPress ainda nao
existe** e o snippet de Sync ainda nao foi escrito. Enquanto isso, os blocos 1,
2 e 3 — buscas parametricas, especificacao das ferramentas e modelo do banco —
sao de pesquisa e modelagem e rodam sem infraestrutura nenhuma. Falta de
WordPress nao e `bloqueada_por`.

## Contrato do manifest

`manifest.json` lista `snippets`, `conteudo`, `dados` e `ferramentas`. O bloco
`esquema` documenta os campos de cada entrada. Dois campos governam a
publicacao:

- `publicar` — `true` faz o Sync aplicar o item no site. O desembarque desta
  ilha e automatico para ferramenta, pagina-ancora, artigo e snippet, por forca
  da secao 10 do `ARQUIPELAGO.md`; so conteudo programatico em escala continua
  `false`.
- `sha256` — o Sync confere o hash depois de gravar. Nunca confie na ausencia
  de erro: em hospedagem compartilhada o ModSecurity pode matar a gravacao em
  silencio.

Ao alterar qualquer item, incremente `revisao` e atualize `atualizado_em`.

## Procedencia

Nenhuma constante, especificacao, compatibilidade ou preco entra sem fonte do
fabricante e data de verificacao. Isso vale para `dados/` e para toda tabela em
`conteudo/`.

**Compatibilidade de peca e o produto desta ilha.** Uma informacao errada aqui
destroi a confianca inteira, que e o unico ativo que separa o Arquipelago das
fazendas de conteudo. Toda afirmacao de compatibilidade carrega fonte do
fabricante e data na propria frase, nao so no rodape da tabela.

## Identidade visual

Aprovada pelo Raphael em 09/09/2026 e descrita em geometria no `PROMPT.md`
desta pasta: paleta de sete valores com o vermelho `#CC3311` como cor de sinal
(um uso por tela), Archivo nos titulos, IBM Plex Sans no texto, IBM Plex Mono
em todo numero, unidade e codigo de peca. O simbolo e o **encaixe** — anel
aberto mais peca com lingueta — porque o assunto da ilha e o encaixe. Nunca um
robo desenhado.
