# Serie de DERIVA DO CATALOGO DE ESPECIES — Aquametria

Quanto o `snippets/aquametria-peixes.php` do repositorio difere do que
`ferramentas/gerar-catalogo-especies.py` produz do banco de hoje. Escreve aqui
o `ferramentas/conferir-deriva-do-catalogo.py --gravar`; quem confere e o mesmo
arquivo sem a opcao, e ele compara LINHA POR LINHA, nao pelo total.

**Secao nova vai no TOPO** (a serie cresce por cima, como `dados/posicoes.md`) e
secao antiga NUNCA e sobrescrita: a serie so vale porque cresce. O bloco `json`
de cada secao e a declaracao que o portao le — o primeiro do arquivo e o que
manda.

Deriva **nao e defeito**: e valor de banco que ainda nao desembarcou, e ela
desembarca junto com a primeira leva que regerar o catalogo. O que e defeito e
deriva que ninguem contou.


## 2026-10-21 10:36Z

**Deriva ZERO**: o snippet do repositorio e o que o gerador produz do
banco de hoje dizem a mesma coisa. Nada a desembarcar.

```json
{
  "linhas": {},
  "medido_em": "2026-10-21 10:36Z",
  "total_de_linhas": 0
}
```

## 2026-10-16 19:34Z

**74 linha(s) de deriva**, agrupadas por linha repetida:

- `34 x` `+						'porte_e_maximo_registrado',`
- `4 x` `+						'convivencia',`
- `4 x` `+					'campos' => array(`
- `4 x` `+					'corpo' => 'Seriously Fish',`
- `4 x` `+					'em' => '2026-10-16',`
- `4 x` `+					),`
- `4 x` `+				),`
- `4 x` `+				array(`
- `3 x` `+						'comprimento_minimo_aquario_cm',`
- `1 x` `+						'temperatura_C',`
- `1 x` `+					'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: a base de 60 x 30 cm (24 x 12 in) deve ser a menor considerada, porque a especie tem de ser mantida em numero; peixe de cardume, pacifico e proprio para aquario comunitario.',`
- `1 x` `+					'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: base de 100 x 40 cm (39 x 16 in), e um aquario de 100 x 40 x 50 cm deve ser o menor considerado; temperatura de 24 a 30 C, pH 6,0 a 7,4, dureza 0 a 15 dGH; ciclideo em geral pacifico que pode implicar com os da propria especie, por isso melhor mantido em pequenos grupos.',`
- `1 x` `+					'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: base de aquario de 60 x 30 cm (24 x 12 in); peixe de cardume, pacifico e proprio para aquario comunitario.',`
- `1 x` `+					'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: o tipo social declarado na ficha e CARDUME (shoal), e o selvagem forma cardume em agua lenta e abrigada, entre raizes e pedras.',`
- `1 x` `+					'url' => 'https://www.seriouslyfish.com/species/paracheirodon-innesi/',`
- `1 x` `+					'url' => 'https://www.seriouslyfish.com/species/pterophyllum-scalare/',`
- `1 x` `+					'url' => 'https://www.seriouslyfish.com/species/symphysodon-aequifasciatus/',`
- `1 x` `+					'url' => 'https://www.seriouslyfish.com/species/trigonostigma-heteromorpha',`

```json
{
  "linhas": {
    "+\t\t\t\t\t\t'comprimento_minimo_aquario_cm',": 3,
    "+\t\t\t\t\t\t'convivencia',": 4,
    "+\t\t\t\t\t\t'porte_e_maximo_registrado',": 34,
    "+\t\t\t\t\t\t'temperatura_C',": 1,
    "+\t\t\t\t\t'campos' => array(": 4,
    "+\t\t\t\t\t'corpo' => 'Seriously Fish',": 4,
    "+\t\t\t\t\t'em' => '2026-10-16',": 4,
    "+\t\t\t\t\t'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: a base de 60 x 30 cm (24 x 12 in) deve ser a menor considerada, porque a especie tem de ser mantida em numero; peixe de cardume, pacifico e proprio para aquario comunitario.',": 1,
    "+\t\t\t\t\t'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: base de 100 x 40 cm (39 x 16 in), e um aquario de 100 x 40 x 50 cm deve ser o menor considerado; temperatura de 24 a 30 C, pH 6,0 a 7,4, dureza 0 a 15 dGH; ciclideo em geral pacifico que pode implicar com os da propria especie, por isso melhor mantido em pequenos grupos.',": 1,
    "+\t\t\t\t\t'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: base de aquario de 60 x 30 cm (24 x 12 in); peixe de cardume, pacifico e proprio para aquario comunitario.',": 1,
    "+\t\t\t\t\t'referencia' => 'Seriously Fish — ficha da especie, releitura de 16/10/2026: o tipo social declarado na ficha e CARDUME (shoal), e o selvagem forma cardume em agua lenta e abrigada, entre raizes e pedras.',": 1,
    "+\t\t\t\t\t'url' => 'https://www.seriouslyfish.com/species/paracheirodon-innesi/',": 1,
    "+\t\t\t\t\t'url' => 'https://www.seriouslyfish.com/species/pterophyllum-scalare/',": 1,
    "+\t\t\t\t\t'url' => 'https://www.seriouslyfish.com/species/symphysodon-aequifasciatus/',": 1,
    "+\t\t\t\t\t'url' => 'https://www.seriouslyfish.com/species/trigonostigma-heteromorpha',": 1,
    "+\t\t\t\t\t),": 4,
    "+\t\t\t\t),": 4,
    "+\t\t\t\tarray(": 4
  },
  "medido_em": "2026-10-16 19:34Z",
  "total_de_linhas": 74
}
```

