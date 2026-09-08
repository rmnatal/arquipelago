# conteudo/

Artigos-ancora, paginas e paginas programaticas, em Markdown, com front
matter YAML (`titulo`, `slug`, `tipo`, `cluster`, `fontes`, `verificado_em`).

- Cada tabela tecnica cita o manual do fabricante e leva data de verificacao.
- Pagina programatica so existe se tiver dado suficiente para ser util
  sozinha. Cauda longa vazia em dominio novo causa desindexacao em bloco.
- Desde 07/09/2026 o desembarque de artigo e pagina-ancora e automatico:
  eles saem com `publicar: true`. Pagina programatica em escala continua com
  `publicar: false`, esperando aprovacao do Raphael.

**Links internos.** Use URL absoluta (`https://aquametria.com.br/pagina/`) ou
relativa a raiz (`/pagina/`) — o conversor do Sync entende as duas desde a
v1.1.3. As paginas ja publicadas usam a absoluta, e vale seguir o mesmo padrao.
Link relativo escrito antes dessa versao saia com os colchetes impressos no
texto, sem erro nenhum: e o tipo de defeito que so aparece lendo a pagina no ar.

**O que o conversor do Sync entende hoje:** titulo (`#` a `######`), paragrafo,
lista com `-` e lista numerada, tabela com `|`, citacao em bloco com `>`, bloco
de codigo cercado por crases triplas, negrito, italico, `codigo` em linha, link,
e a linha que so tem um shortcode (que sai fora do `<p>`, porque `<div>` dentro
de `<p>` e HTML invalido). O front matter e descartado. Se voce precisar de algo
alem disso, ensine o conversor antes de escrever a pagina.

**Nenhuma pagina nasce orfa.** Ao publicar uma pagina, publique tambem o link
que aponta para ela de alguma pagina que ja existe — a calculadora irma, o hub,
o artigo pareado. Link interno so vale se for de mao dupla.
