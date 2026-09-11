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

Desde 09/09/2026 (esquema versao 7) vale a EMENDA A V12, gemea da que o banco de
especies ja tinha no E10: um registro pode estar `parcial` E ter `conflitos[]`.
Completude e divergencia sao fatos ortogonais, `status_registro` carrega um campo
so, e vale o mais restritivo — `parcial` barra a sugestao, `conflito` so obriga a
tela a publicar a divergencia. Acontece quando o proprio conflito e a CAUSA da
incompletude: duas fontes do mesmo nivel discordam, o tratamento
`campo-vira-null` esvazia o campo, e o campo vazio deixa o registro parcial.

Depois de qualquer mudanca em `produtos-*.json`, rode
`ferramentas/validar-produtos.py` **e** o gerador de catalogo da calculadora
afetada: a copia do banco que viaja dentro do snippet nao se atualiza sozinha.
E depois de mexer em QUALQUER arquivo listado no manifest, rode
`python3 ferramentas/atualizar-manifest.py`, que recalcula os sha256 e sobe a
revisao. Sha vencido no manifest faz o Sync recusar o item no ar sem avisar
ninguem — em 09/09/2026 havia quatro assim, todos esquecidos a mao.

## Banco de especies (desde 09/09/2026)

`especies-agua-doce.json` guarda a entidade `especie`, com contrato proprio em
`esquema-especies.json` e validador proprio em
`ferramentas/validar-especies.py` (regras E1 a E16). Rode-o antes de todo
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

Duas regras nasceram em 11/09/2026, da leva 4, e as duas existem por causa do
CANAL de coleta, nao do banco. Enquanto o egresso barrar `fishbase.se`,
`fishbase.org` e `seriouslyfish.com`, todo numero entra por resumo de busca
restrita ao dominio — e resumo de busca tem dois vicios medidos:

- **A congenere.** Quando a ficha da especie alvo nao publica o campo, o resumo
  oferece o numero da especie IRMA do mesmo genero sem avisar que trocou de
  ficha. Aconteceu com o `Tanichthys albonubes` (veio a base do *T.* sp.
  'Vietnam'), com o `Nannostomus beckfordi` e com o `Danio margaritatus`, nas
  duas datas de coleta. **Numero sem o nome da especie do lado e recusa, nao
  dado**, e o registro grava no `observacao` qual numero foi oferecido e
  recusado — e o que impede a proxima coleta de cair na mesma oferta.
- **Reproduzir nao e conferir.** O porte de 13,7 cm TL do gurami mel voltou
  identico em tres formulacoes de busca, em duas datas, e continua recusado.
  Quem o derruba e a contradicao interna da fonte, nao a contagem de repeticoes.

A regra **E16** e a parte executavel disso: todo numero de campo tem de aparecer
no texto de alguma fonte que declara aquele campo, em algarismo ou por extenso.
Campo e `referencia` sao duas escritas independentes do mesmo fato — quando
divergem, alguem transcreveu, digitou ou editou um lado so.
