# As filhas de nivel 3 do Guia — o portao de dado da secao 9, medido recorte por recorte

**GERADO por `ferramentas/filhas-do-guia.py` a partir de `dados/filhas-do-guia.json`.**
Nao edite este trecho a mao: `--conferir` regera e compara, e uma edicao manual reprova o
portao. O que se escreve a mao esta depois da fronteira, no fim do arquivo.

Minimo da secao 9: **3** itens. Nivel maximo de fonte para recomendacao primaria, lido do
esquema (versao 16): **3**.

## O numero que manda

| veredito | recortes |
|---|---|
| `passa` | 11 |
| `passa_na_contagem_sem_lastro` | 1 |
| `nao_passa` | 30 |

**Podem nascer hoje:** `acabamento`, `acabamento/impermeabilizante`, `acabamento/selador`, `acabamento/verniz`, `alicate`, `alicate/cortador_de_azulejo`, `alicate/torques`, `pastilha`, `pastilha/vidro`, `rejunte`, `rejunte/cimenticio`.

**Categorias que alcancam as 3 filhas da 16.5:** `acabamento`.

## Recorte por recorte

| recorte | itens | com lastro | numeros calculaveis | veredito |
|---|---|---|---|---|
| `acabamento` | 10 | 10 | `acabamento_visual` (5), `demaos_minimas` (5), `pelicula` (4), e mais 5 | `passa` |
| `acabamento/verniz` | 4 | 4 | `acabamento_visual` (3), `pelicula` (3) | `passa` |
| `acabamento/impermeabilizante` | 3 | 3 | `base_quimica` (3) | `passa` |
| `acabamento/selador` | 3 | 3 | `tempo_de_secagem_h` (3) | `passa` |
| `alicate` | 6 | 6 | `espessura_maxima_de_corte_mm` (4), `comprimento_maximo_de_corte_mm` (3), `diametro_do_rodel_mm` (3), e mais 2 | `passa` |
| `alicate/torques` | 3 | 3 | `tamanho_polegadas` (3) | `passa` |
| `alicate/cortador_de_azulejo` | 3 | 3 | `comprimento_maximo_de_corte_mm` (3), `diametro_do_rodel_mm` (3), `dimensoes_mm` (3), e mais 1 | `passa` |
| `alicate/pinca_mosaico` | 0 | 0 | — | `nao_passa` |
| `alicate/martelinho` | 0 | 0 | — | `nao_passa` |
| `apoio` | 0 | 0 | — | `nao_passa` |
| `apoio/espatula` | 0 | 0 | — | `nao_passa` |
| `apoio/desempenadeira` | 0 | 0 | — | `nao_passa` |
| `apoio/oculos` | 0 | 0 | — | `nao_passa` |
| `apoio/luva` | 0 | 0 | — | `nao_passa` |
| `apoio/pinca` | 0 | 0 | — | `nao_passa` |
| `apoio/marcador` | 0 | 0 | — | `nao_passa` |
| `base` | 0 | 0 | — | `nao_passa` |
| `base/mdf_cru` | 0 | 0 | — | `nao_passa` |
| `base/ceramica_crua` | 0 | 0 | — | `nao_passa` |
| `base/cimento` | 0 | 0 | — | `nao_passa` |
| `base/isopor_estrutural` | 0 | 0 | — | `nao_passa` |
| `base/moldura` | 0 | 0 | — | `nao_passa` |
| `cola` | 7 | 3 | — | `passa_na_contagem_sem_lastro` |
| `cola/pva` | 2 | 1 | — | `nao_passa` |
| `cola/silicone_acetico` | 2 | 1 | — | `nao_passa` |
| `cola/silicone_neutro` | 1 | 0 | — | `nao_passa` |
| `cola/cimentcola_acii` | 1 | 1 | — | `nao_passa` |
| `cola/cimentcola_aciii` | 0 | 0 | — | `nao_passa` |
| `cola/epoxi` | 1 | 0 | — | `nao_passa` |
| `cola/adesivo_para_espelho` | 0 | 0 | — | `nao_passa` |
| `pastilha` | 13 | 12 | `m2_por_caixa` (12), `peso_caixa_kg` (12), `placas_por_caixa` (12) | `passa` |
| `pastilha/vidro` | 13 | 12 | `m2_por_caixa` (12), `peso_caixa_kg` (12), `placas_por_caixa` (12) | `passa` |
| `pastilha/ceramica` | 0 | 0 | — | `nao_passa` |
| `pastilha/pedra` | 0 | 0 | — | `nao_passa` |
| `pastilha/caco_azulejo` | 0 | 0 | — | `nao_passa` |
| `pastilha/caco_espelho` | 0 | 0 | — | `nao_passa` |
| `pastilha/resina` | 0 | 0 | — | `nao_passa` |
| `rejunte` | 5 | 5 | `junta_max_mm` (5), `junta_min_mm` (5), `liberacao_area_molhada_h` (4) | `passa` |
| `rejunte/cimenticio` | 3 | 3 | `junta_max_mm` (3), `junta_min_mm` (3), `liberacao_area_molhada_h` (3) | `passa` |
| `rejunte/flexivel` | 0 | 0 | — | `nao_passa` |
| `rejunte/acrilico` | 1 | 1 | — | `nao_passa` |
| `rejunte/epoxi` | 1 | 1 | — | `nao_passa` |

## As filhas em forma de PERGUNTA — a mesma regua, declaradas em `dados/perguntas-do-guia.json`

A pergunta **nao afrouxa o portao**: no recorte de tipo a secao 9 cobra tres coisas separadas
(3 itens, 3 com lastro, um numero sobre 3); na pergunta as tres COINCIDEM, porque o recorte
dela e o conjunto dos itens que declaram o numero com lastro. Minimo e teto de nivel sao os
mesmos, lidos dos mesmos lugares. **E ela nao decide se a categoria ganhou filha** — a 16.5 se
fecha por CONSULTA, e isso e do `cruzamento-14-9.py`.

| pergunta | categoria | numero | itens | tipos que atravessa | veredito |
|---|---|---|---|---|---|
| `pergunta:alicate-espessura-de-corte` | `alicate` | `espessura_maxima_de_corte_mm` | 4 | `cortador_de_azulejo`, `torques` | `passa` |
| `pergunta:rejunte-largura-da-junta` | `rejunte` | `junta_min_mm` | 5 | `acrilico`, `cimenticio`, `epoxi` | `passa` |
| `pergunta:pastilha-placa-ou-caixa` | `pastilha` | `placas_por_caixa` | 12 | `vidro` | `passa` |

- **`pergunta:alicate-espessura-de-corte`** — consulta-alvo: *como cortar pastilha de vidro para mosaico qual ferramenta*
- **`pergunta:rejunte-largura-da-junta`** — consulta-alvo: *da para colar os caquinhos bem juntos no mosaico ou precisa deixar espaco para o rejunte*
  - cobre a categoria inteira (5 de 5 itens ativos), e isso e o esperado: a mae
    de nivel 2 e indice e esta pergunta e a pagina de nivel 3 que responde.
- **`pergunta:pastilha-placa-ou-caixa`** — consulta-alvo: *da para comprar so uma placa de pastilha de vidro para mosaico ou precisa levar a caixa fechada*
  - atravessa um tipo so, e ainda assim nao coincide com ele: o recorte da
    pergunta e menor que o do tipo, porque parte dos itens nao declara o numero.

## O motivo, nos recortes que nao passam inteiros

- **`alicate/pinca_mosaico`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`alicate/martelinho`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio/espatula`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio/desempenadeira`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio/oculos`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio/luva`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio/pinca`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`apoio/marcador`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`base`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`base/mdf_cru`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`base/ceramica_crua`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`base/cimento`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`base/isopor_estrutural`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`base/moldura`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola`** — 3 dos 7 itens sustentam recomendacao, e NENHUMA propriedade e declarada por 3 deles ao mesmo tempo — nao ha numero que a pagina calcule sobre o recorte inteiro
- **`cola/pva`** — o banco tem 2 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola/silicone_acetico`** — o banco tem 2 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola/silicone_neutro`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola/cimentcola_acii`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola/cimentcola_aciii`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola/epoxi`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`cola/adesivo_para_espelho`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`pastilha/ceramica`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`pastilha/pedra`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`pastilha/caco_azulejo`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`pastilha/caco_espelho`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`pastilha/resina`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`rejunte/flexivel`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`rejunte/acrilico`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`rejunte/epoxi`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3

<!-- DAQUI PARA BAIXO E BUSCA, NAO DERIVACAO: o gerador preserva. -->

## A classificação de SERP da 14.9 — ELA SAIU DAQUI EM 02/10/2026, E VIROU DADO

Até 02/10/2026 esta seção era uma **tabela em prosa** com as seis consultas medidas em
30/09, e era a metade de SERP do cruzamento que a 14.9 exige. Ela foi movida, inteira e sem
perda, para dois lugares — e o motivo é o que este arquivo mais paga:

- **O dado coletado** está em `dados/serp-das-filhas.json`: consulta por consulta, com quem
  ocupa escrito pelo nome, a data da medição, os três limites do canal (país, ordem, marca
  na consulta), as cinco classificações e o número que a SERP não publica. As dez medições
  de lá incluem as seis de 30/09, **sem uma palavra alterada**, mais as quatro de `acabamento`
  de 02/10.
- **O cruzamento** está em `dados/cruzamento-14-9.md`, gerado por
  `ferramentas/cruzamento-14-9.py` a partir deste arquivo **e** daquele. Ele é o portão: dá
  **um** veredito por recorte, conta a 16.5 pelas filhas que o cruzamento autoriza (que não
  são as que o dado autoriza) e deriva o pedido de faixa de volume ao Raphael.

**Por que mover.** Este arquivo diz de si mesmo, no cabeçalho do gerador, que *"não
classifica SERP"* — e a classificação morava aqui embaixo, numa seção que o gerador
preserva **sem ler**. Prosa não cruza com número: entre 30/09 e 02/10 a pergunta "o 4c pode
nascer?" exigia abrir dois arquivos e fazer a conta na cabeça, e o `ESTADO.md` de 02/10 às
13h17Z teve de escrever **à mão** o aviso *"o portão de DADO abriu, o de SERP é outro"* para
a execução seguinte não ler passe livre. Aviso à mão é o que o portão novo substitui.

**E o veredito que o cruzamento devolveu no primeiro dia em que existiu:** `acabamento` é a
primeira categoria do Guia a passar os **dois** portões, na mãe e nas três filhas — o 4c está
liberado ali. E `pastilha` ficou com **1 filha no dado e 0 no cruzamento**, porque
`pastilha/vidro` é a de mais banco da ilha e a SERP dela é marketplace. Nenhum dos dois
arquivos de entrada mostra isso sozinho; é exatamente o que o cruzamento existe para ver.
