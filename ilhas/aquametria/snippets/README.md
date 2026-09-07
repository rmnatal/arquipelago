# snippets/

PHP dos snippets do plugin Code Snippets. Um arquivo por snippet, nome do
arquivo igual ao `id` no manifest.

Convencoes que o playbook (fase 4b) exige:

- O arquivo comeca com `/**` — o plugin poe o `<?php`.
- Todo PHP passa em `php -l` de verdade antes do commit.
- Nome de snippet descritivo e obvio, nunca numerado.
- Texto que vai para a tela sai acentuado.
- Evite a superglobal `$_SERVER` literal: em hospedagem compartilhada o
  ModSecurity mata a gravacao em silencio. Contorno: `add_query_arg( array() )`.
- Depois de gravar, releia o snippet e confira `code.length` contra o
  enviado e que `code_error` e `null`.

Gravacao: `POST /wp-json/code-snippets/v1/snippets`, ativacao por `/activate`.

## Snippets registrados

| id | nome no Code Snippets | papel |
|---|---|---|
| `aquametria-sync` | Aquametria Sync | puxa o manifest e aplica o que tem `publicar: true`. Nunca se aplica a si mesmo |
| `aquametria-casca` | Aquametria Casca — identidade e estrutura do site | paleta, tipografia, logotipo, menu, as quatro paginas institucionais e o rodape |

A casca guarda a lista de calculadoras em `aquametria_casca_calculadoras()` e a
publica pelo filtro `aquametria_calculadoras`. **Toda calculadora nova precisa
aparecer no hub**: ou muda `estado` para `publicada` nessa lista (bumpando
`AQUAMETRIA_CASCA_VERSAO`), ou o snippet da propria calculadora se registra pelo
filtro. Calculadora no ar que nao esta no hub e defeito.

Alem de `php -l`, todo snippet novo passa por um teste de fumaca com o
WordPress simulado por stubs (chamar os shortcodes, disparar `wp_head`,
`wp_footer`, `render_block` e a rotina de estrutura duas vezes para conferir
idempotencia) antes de entrar no manifest com `publicar: true`.
