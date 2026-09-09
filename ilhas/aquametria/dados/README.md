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

## Banco de especies (desde 09/09/2026)

`especies-agua-doce.json` guarda a entidade `especie`, com contrato proprio em
`esquema-especies.json` e validador proprio em
`ferramentas/validar-especies.py` (regras E1 a E14). Rode-o antes de todo
commit que toque o arquivo:

```
python3 ferramentas/validar-especies.py
```

Ele existe separado do banco de produtos porque as regras nao sao as mesmas.
Tres diferencas que valem a leitura antes de mexer:

- **Nao existe fabricante de peixe.** A escada de fontes troca "manual do
  fabricante" por base cientifica (FishBase) e compendio de aquarismo
  (Seriously Fish), e a tabela `dominio_por_campo` diz qual das duas manda em
  qual campo: biologia com a base, manutencao com o compendio. Sem isso,
  "nivel mais alto vence" daria a FishBase a ultima palavra sobre tamanho de
  aquario, que nao e o assunto dela.
- **Em conflito de campo de bem-estar o conservador e o MAIOR**, o oposto do
  banco de produtos. Errar espaco para menos custa a vida do animal; errar
  para mais custa espaco.
- **Litro nao se grava.** A fonte declara frente e base em centimetros; o
  litro e derivado pela calculadora com a altura que a pessoa informar. Litro
  gravado a mao e defeito, e a regra E7 detecta.
