# Ilha: Clube do Mosaico

Terceira ilha do Projeto Arquipelago. Nicho: mosaico artesanal — loja de pecas
proprias, guia de materiais com afiliado e escola de tecnicas.

Contrato curto desta pasta:

- **O que a ilha faz, o que ela nao faz e a fila de blocos estao no
  [`PROMPT.md`](PROMPT.md) desta pasta.** Leia o `ARQUIPELAGO.md` da raiz antes
  dele: o `ARQUIPELAGO.md` carrega as regras comuns a todas as ilhas e o
  `PROMPT.md` tem so o que e daqui.
- **O estado vivo — infraestrutura, o que ja foi entregue e o que esta
  travando — esta no [`ESTADO.md`](ESTADO.md) desta pasta.** E ele que diz em
  que bloco a ilha esta e por que ela esta parada, quando estiver.
- O historico append-only de cada execucao fica no [`REGISTRO.md`](REGISTRO.md).

## Estrutura

| Pasta | O que guarda |
|---|---|
| `snippets/` | PHP dos snippets do Code Snippets (ferramentas, widget, endpoints) |
| `conteudo/` | Artigos-ancora, paginas e paginas programaticas, em Markdown |
| `dados/` | Banco normalizado de materiais, pecas, tecnicas e constantes, em JSON/CSV |
| `identidade/` | Arquivos de identidade visual fornecidos pelo Raphael (logo) |
| `manifest.json` | Indice que o snippet Sync consome |

**Todo codigo e todo conteudo do site mora aqui, neste repositorio.** Nada e
escrito direto no WordPress: o snippet Sync le o `manifest.json` desta pasta e
aplica o que estiver marcado para publicar.
