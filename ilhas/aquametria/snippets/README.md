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
