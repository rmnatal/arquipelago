# dados/

Banco normalizado que alimenta as calculadoras e as paginas programaticas.

Entidades previstas: `filtro` (vazao L/h), `aquecedor` (potencia W),
`iluminacao`, `midia` filtrante, `especie` e `constante` (fatores usados
nas formulas).

Cada registro carrega a origem do dado e a data em que foi conferido.
Constante sem fonte do fabricante nao entra — nem para "provisoriamente".

Divergencia entre fontes nao se resolve por media. O esquema define quatro
tratamentos: `publicar-os-dois`, `nivel-mais-alto-vence`, `campo-vira-null` e,
desde 08/09/2026, `intersecao-conservadora` (regra V17) — que vale so para campo
de intervalo com fontes do MESMO nivel em conflito, e publica a intersecao dos
intervalos, ou seja, a afirmacao mais fraca que todas as fontes sustentam. Nao e
media nem escolha: e o que ninguem discorda. A calculadora que usar esse valor
tem de dizer na tela que a faixa e a conservadora e por que.

Depois de qualquer mudanca em `produtos-*.json`, rode
`ferramentas/validar-produtos.py` **e** o gerador de catalogo da calculadora
afetada: a copia do banco que viaja dentro do snippet nao se atualiza sozinha.
