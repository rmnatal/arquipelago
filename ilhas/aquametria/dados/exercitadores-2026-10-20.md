# QUANTOS ARQUIVOS EXERCITAM CADA FUNÇÃO DE `ferramentas/` — 20/10/2026

**Quem pediu:** o item 4 do PRÓXIMO PASSO do fecho de 20/10/2026 (16h18Z), escrito pela
execução que acabou de pagar o preço do defeito do `_base`:

> *"o defeito do `_base` só foi achado porque um SEGUNDO leitor exercitou a mesma função
> sobre outra linguagem — ele estava dormindo havia dias com um caller só. **Quantas
> funções compartilhadas de `ferramentas/` têm hoje um único exercitador?** Quem a tomar
> conta primeiro, antes de propor conserto nenhum."*

**Quem mede:** `ferramentas/regua-exercitadores.py`. **Quem a exercita:**
`ferramentas/teste-exercitadores.py`. **Quem a mutila:**
`ferramentas/mutacoes-exercitadores.py`.

Os números abaixo são de uma DATA e envelhecem com a pasta — quem quiser o de hoje roda
`python3 ferramentas/regua-exercitadores.py`, que os imprime todos.

---

## 1. A CONTA

| o que | quanto |
|---|---|
| arquivos em `ferramentas/` | 148 |
| `.py` que a régua lê | 107 |
| funções de **topo** definidas neles | 842 |
| sítios de exercício na pasta | 6.532 |
| — por **chamada** (`nome(...)`, `M.nome(...)`) | 4.148 |
| — por **referência** (o nome como valor) | 1.913 |
| — **por nome** (o nome como texto) | 471 |
| **funções ÓRFÃS** (nenhum sítio, em nenhuma das três formas) | **0** |
| funções **compartilhadas** (de arquivo que um irmão carrega) | 241 |
| — com **1** exercitador | **96** |
| — com 2 | 103 |
| — com 3 ou mais | 42 |
| das 95, **sem nenhum leitor de fora** (só o próprio arquivo) | **92** |

**A RESPOSTA, em uma frase:** **96 funções compartilhadas desta pasta têm hoje um
exercitador só, e 92 delas não têm leitor de fora nenhum** — ou seja, estão num arquivo
que irmãos carregam, logo são alcançáveis, e irmão nenhum as alcança. Essa é a condição
exata em que o `_base` dormiu.

**Por classe de arquivo**, porque não é tudo régua:

| classe | compartilhadas | com 1 exercitador |
|---|---|---|
| `regua-*` | 150 | **35** (em 12 arquivos; só **4** têm leitor de fora) |
| `teste-*` | 44 | 31 |
| `coletar-*` | 24 | 14 |
| `conferir-*` | 19 | 14 |
| `validar-*` | 4 | 2 |

As **35 de `regua-*`** são a resposta que importa: régua é código que nasceu para ser
lido por dois. As de `teste-*` e `conferir-*` são compartilhadas por acidente de carga
(o `conferir-peixes-no-ar.py` carrega o `teste-peixes.py`, o `teste-coleta-shopee.py`
carrega o `coletar-shopee.py`) e um exercitador nelas é desenho normal.

**POR QUE A CONTA SUBIU DE 95 PARA 96 ENTRE A SONDAGEM E O FECHO, e isto não é correção
de erro:** a sondagem leu a pasta **antes** de a régua, o portão e as mutações desta
passada existirem; o fecho leu a pasta **com** eles. A `regua-exercitadores.py` é
carregada pelo portão, logo as funções dela são compartilhadas e entram na conta — cinco
delas com um exercitador só. **Régua que se mede mede a si mesma**, e esconder isso daria
um número mais bonito e menos verdadeiro.

---

## 2. O PRIMEIRO ACHADO FOI DA PRÓPRIA PERGUNTA: CONTAR SÓ A CHAMADA ERRA 82 VEZES

A primeira sondagem contou `nome(...)` e devolveu **82 funções órfãs**. **As 82 eram
falsas.** As `c_e1` … `c_e28` do `testar-validador-especies.py` não são chamadas em lugar
nenhum — entram numa tupla de casos (`("E1", "id que nao corresponde...", c_e1, "erro",
"peixe-zebra")`) e quem as chama é o laço. O mesmo vale para as mutações do
`mutacoes-purga-cache.py` e do `mutacoes-c15-regulagem.py`.

**É o idioma de toda bancada desta pasta**, e uma varredura por chamada é cega para ele.
Por isso a régua conta três formas e `orfas()` exige a ausência das três. Ela erra de
propósito para o lado de **não acusar**: string solta igual ao nome de uma função é prova
fraca, e prova fraca não basta para chamar código de morto — mas basta para não o acusar.

---

## 3. O ACHADO QUE A CONTA PRODUZIU: **CINCO** `ler_pasta()`, EM **DUAS** VERSÕES QUE DISCORDAM

`ler_pasta()` é a função mais copiada desta pasta. Estava definida **cinco** vezes, cada
cópia com **um** exercitador — o próprio arquivo:

| arquivo | lê quais arquivos | `errors="replace"` |
|---|---|---|
| `regua-alvos-de-portao.py` | todos, menos os que começam por `.` | **sim** |
| `regua-alvos-em-php.py` | idem (byte a byte igual à de cima) | **sim** |
| `regua-classes-da-bancada.py` | idem | **sim** |
| `regua-constantes-de-snippet.py` | só `.py`, `.mjs`, `.php` | **NÃO** |
| `regua-teto-do-titulo.py` | só `.py`, `.mjs`, `.php` | **NÃO** |

**A divergência é de COMPORTAMENTO e foi medida, não lida.** Numa pasta com um `.py` que
traz o byte `0xe9` (o `é` em latin-1, que é o jeito realista de isto acontecer numa ilha
que escreve português acentuado):

```
regua-alvos-de-portao.py           OK  -> 2 arquivos
regua-alvos-em-php.py              OK  -> 2 arquivos
regua-classes-da-bancada.py        OK  -> 2 arquivos
regua-constantes-de-snippet.py     MORREU -> UnicodeDecodeError: byte 0xe9
regua-teto-do-titulo.py            MORREU -> UnicodeDecodeError: byte 0xe9
```

**E o `except OSError` do corpo não o pega**: `UnicodeDecodeError` é `ValueError`. As duas
cópias morrem de traceback, não de veredito — e a `regua-teto-do-titulo.py` é **carregada
por SETE irmãos** (`conferir-titulo-no-ar.py`, `regua-classes-da-bancada.py`,
`regua-constantes-de-snippet.py`, `teste-classes-da-bancada.py`,
`teste-promessa-do-titulo.py`, `teste-teto-do-titulo.py`,
`teste-titulos-das-duas-fontes.py`). Um arquivo salvo na codificação errada levaria sete
portões a traceback, enquanto três réguas irmãs seguiriam trabalhando, e a bancada
reportaria traceback no lugar de veredito.

**CONSERTADO NESTA PASSADA**, nas duas cópias, com a nota do motivo dentro de cada uma.
**E a propriedade passou a ser cobrada**: a metade 3 do `teste-exercitadores.py`
**DESCOBRE** as cópias pela árvore sintática e exige que cada uma sobreviva ao byte torto
— nenhuma linha do portão nomeia um arquivo. A mutação **15** prova que isso morde: ela
põe uma **sexta** cópia na pasta de sombra, com o buraco de ontem, e o portão a reprova
sem ninguém a ter listado. A mutação **14** desfaz o conserto de hoje e também reprova.

**É a família exata do `_base`, um andar acima:** lá era uma cópia com o defeito da irmã;
aqui são cinco cópias e duas versões. E as duas versões conviveram sem ninguém notar
porque cada uma tinha um leitor só, e um leitor nunca discorda de si mesmo.

---

## 4. O LIMITE QUE ESTA RÉGUA TEM, E ELE ESTÁ MEDIDO EM VEZ DE SER DESCOBERTO DEPOIS

**A régua não tem ESCOPO.** Um `ast.Name` em contexto de leitura conta como sítio, e ela
não sabe se aquele `texto` é a função `texto()` de outro arquivo ou uma variável local
chamada `texto`. Medido: **61 dos 484** nomes distintos de função de topo desta pasta são
**também** nome de variável ou parâmetro em algum arquivo — `texto` em 55 arquivos,
`linha` em 30, `corpo` em 25, `valor` e `campo` em 21.

**A consequência, dita com todas as letras:** função cujo nome é uma palavra comum de
variável **nunca** será acusada de órfã por esta régua, porque a variável de outro arquivo
já conta como sítio. `orfas()` é, para esses 61 nomes, uma lista que não pode acusar. Para
os outros 423, ela acusa.

**Por que não se conserta hoje:** separar os dois pede análise de escopo por arquivo e por
função, que é outro bloco. A alternativa — exigir que o sítio esteja num arquivo que
CARREGA quem define — foi medida e é pior: ela devolveria as 82 órfãs falsas da seção 2,
porque referência em tupla de casos mora no próprio arquivo.

**Os outros três limites, declarados no cabeçalho da régua:** (1) ela **só lê Python** —
os 21 `.php` e os 20 `.mjs` desta pasta têm função e têm exercitador, e não entram; (2)
**só função de topo** — método de classe pediria resolução de tipo, que é executar o
código; (3) **nome homônimo em dois arquivos**, quando o sítio não está em quem define nem
em quem carrega, vai para `ambiguos()` e **não é atribuído a ninguém** — são **706** sítios
em **19** nomes, e `main` é definido em **77** arquivos desta pasta.

---

## 5. OS TRÊS DESFECHOS PRÉ-REGISTRADOS PARA AS **35** DE `regua-*`

Escritos ANTES de qualquer conserto, pela 1.2-b.4: *critério escrito depois do dado é
critério dobrado para caber no dado que veio.*

1. **Apagar a cópia** — quando a função existe em duas ou mais réguas, a certa importa e
   as outras morrem. Foi o conserto do `_base` em 20/10 e é o desfecho de maior valor; o
   `ler_pasta()` é o próximo candidato nomeado, e ele agora tem cinco cópias e **uma**
   propriedade cobrada, que é o pré-requisito para unificar sem perder comportamento.
2. **Pôr o segundo leitor** — quando a função é uma só e o segundo exercitador é barato
   de escrever (uma afirmação que a chame por outro caminho, ou um `--autoteste`). Vale
   para as **6** da `regua-alvos-em-php.py` (`_resolver`, `_dobras`, `_fala_da_pasta`,
   `_nomes_por_variavel`, `_proprio`, `_com_pasta_no_disco`), que nasceram ontem e cujo
   único leitor é a própria régua.
3. **Declarar que um leitor basta** — quando a função é privada por desenho e o segundo
   leitor seria cerimônia. Neste caso a decisão vai escrita no arquivo que a possui, e
   não aqui: *"um exercitador, de propósito, porque X"*.

**O que NÃO é desfecho:** cobrar o número no portão. Está escrito na docstring do
`teste-exercitadores.py` e vale repetir: ajudante privado chamado de um lugar só é desenho
correto na maior parte dos casos, e cobrar o número faria deste portão a lista digitada
que esta pasta já pegou três vezes — a do `teste-voz.mjs`, a da tabela de levas do
`dados/indexacao.md` e a dos alvos do `teste-arvore`.

---

## 6. O QUE ESTA MEDIÇÃO NÃO AUTORIZA

- **Não autoriza dizer que a pasta não tem código morto.** Autoriza dizer que **nenhuma
  função de topo de `.py` desta pasta está sem sítio nas três formas**, com o furo de
  escopo da seção 4 nomeado e contado. Função dentro de classe, função dentro de função,
  e tudo em `.php` e `.mjs`, não foram medidos.
- **Não autoriza nenhuma URL nova.** Bloco de instrumento, dentro do congelamento de
  título e meta de 14/10, e o teto da 21.4 segue **zerado**.
- **Não autoriza ler as 96 como 96 defeitos.** São 96 funções em que um defeito teria hoje
  um leitor só para o contradizer. Quantas delas têm defeito, ninguém mediu — e a seção 5
  é como se mede, uma a uma.
