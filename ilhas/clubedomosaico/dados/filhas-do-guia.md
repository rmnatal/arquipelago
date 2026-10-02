# As filhas de nivel 3 do Guia — o portao de dado da secao 9, medido recorte por recorte

**GERADO por `ferramentas/filhas-do-guia.py` a partir de `dados/filhas-do-guia.json`.**
Nao edite este trecho a mao: `--conferir` regera e compara, e uma edicao manual reprova o
portao. O que se escreve a mao esta depois da fronteira, no fim do arquivo.

Minimo da secao 9: **3** itens. Nivel maximo de fonte para recomendacao primaria, lido do
esquema (versao 10): **3**.

## O numero que manda

| veredito | recortes |
|---|---|
| `passa` | 9 |
| `passa_na_contagem_sem_lastro` | 3 |
| `nao_passa` | 30 |

**Podem nascer hoje:** `acabamento`, `acabamento/impermeabilizante`, `acabamento/selador`, `acabamento/verniz`, `alicate`, `alicate/cortador_de_azulejo`, `pastilha`, `pastilha/vidro`, `rejunte`.

**Categorias que alcancam as 3 filhas da 16.5:** `acabamento`.

## Recorte por recorte

| recorte | itens | com lastro | numeros calculaveis | veredito |
|---|---|---|---|---|
| `acabamento` | 10 | 10 | `acabamento_visual` (5), `demaos_minimas` (5), `pelicula` (4), e mais 5 | `passa` |
| `acabamento/verniz` | 4 | 4 | `acabamento_visual` (3), `pelicula` (3) | `passa` |
| `acabamento/impermeabilizante` | 3 | 3 | `base_quimica` (3) | `passa` |
| `acabamento/selador` | 3 | 3 | `tempo_de_secagem_h` (3) | `passa` |
| `alicate` | 6 | 4 | `espessura_maxima_de_corte_mm` (4), `comprimento_maximo_de_corte_mm` (3), `diametro_do_rodel_mm` (3), e mais 1 | `passa` |
| `alicate/torques` | 3 | 1 | — | `passa_na_contagem_sem_lastro` |
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
| `rejunte` | 5 | 5 | `junta_max_mm` (4), `junta_min_mm` (4), `liberacao_area_molhada_h` (3) | `passa` |
| `rejunte/cimenticio` | 3 | 3 | — | `passa_na_contagem_sem_lastro` |
| `rejunte/flexivel` | 0 | 0 | — | `nao_passa` |
| `rejunte/acrilico` | 1 | 1 | — | `nao_passa` |
| `rejunte/epoxi` | 1 | 1 | — | `nao_passa` |

## O motivo, nos recortes que nao passam inteiros

- **`alicate/torques`** — 1 dos 3 itens sustentam recomendacao primaria (fonte de nivel <= 3); a secao 9 exige 3
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
- **`rejunte/cimenticio`** — 3 dos 3 itens sustentam recomendacao, e NENHUMA propriedade e declarada por 3 deles ao mesmo tempo — nao ha numero que a pagina calcule sobre o recorte inteiro
- **`rejunte/flexivel`** — o banco tem 0 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`rejunte/acrilico`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3
- **`rejunte/epoxi`** — o banco tem 1 item(ns) ativo(s) neste recorte e a secao 9 exige 3

<!-- DAQUI PARA BAIXO E BUSCA, NAO DERIVACAO: o gerador preserva. -->

## A classificação de SERP da 14.9 — medida em 30/09/2026, 13h5xZ, consulta por consulta

A 14.9 manda olhar a SERP da consulta-alvo **antes** de criar a página e classificar quem ocupa o
top 10. O portão de dado acima não responde isso, e nenhum dos dois sozinho decide: a 14.9 pede o
**cruzamento** de intenção de compra com chance real de primeira página.

### O INSTRUMENTO, ANTES DO RESULTADO — porque ele decide o que este arquivo pode afirmar

O canal de busca desta nuvem **é dos Estados Unidos**, declarado pela própria ferramenta (`US-only`).
Isso tem três consequências, e as três estão escritas aqui porque cada uma limita uma afirmação:

1. **Ele devolve resultado brasileiro quando a consulta é inequivocamente portuguesa**, e desvia para
   SERP espanhola quando a frase também é espanhola. Aconteceu de verdade nesta passada, e está
   registrado abaixo como consulta **NÃO MEDIDA**, não como consulta sem concorrente.
2. **Ele não dá a ORDEM da SERP brasileira.** Então este arquivo classifica **quem ocupa** os
   resultados, que é o que a 14.9 pede com essas palavras ("classifique quem ocupa o top 10"), e
   **não** afirma posição de ninguém. Onde há número de posição nesta ilha, ele vem do Search
   Console — e o acesso a `sc-domain:clubedomosaico.com.br` continua pendente com o Raphael.
3. **Marca dentro da consulta vicia a medição.** A primeira passada de `alicate` foi feita com
   `Vonder` e `Cortag` na frase, e voltou cheia de página de fabricante — o que era previsível e é
   defeito de quem escreveu a consulta. Está abaixo como NÃO MEDIDA, com o motivo, e refeita sem
   marca. É a trava de coleta da seção 8 ("nunca pôr na consulta o valor que se quer confirmar")
   aplicada à SERP em vez de ao dado.

### O RESULTADO, e ele INVERTE a ordem que a fila supunha

| recorte | consulta medida | quem ocupa | classificação |
|---|---|---|---|
| `pastilha/vidro` | `pastilhas de vidro para mosaico` | 9 de 9 marketplace e loja: Mercado Livre, Buscapé, Elo7 (2), Bazar Horizonte, Vetro Designer, Mosaico & Cia, Mosaico em Casa, Pastilhart | **TOMADA** |
| `pastilha/vidro` | `quantas pastilhas vem na caixa placa telada mosaico vidro medida` | 10 de 10 loja e obra: Elevato, MadeiraMadeira, Leroy Merlin PT, Telhanorte, Pastilhart (2), Mosaico em Casa, Gerador de Preços PT, Revestimentta, Eckofloor | **TOMADA, e é a ARMADILHA do revestimento** |
| `alicate/cortador_de_azulejo` | `cortador de azulejo manual para mosaico` | Amazon MX, Leroy Merlin ES, Bricodepot ES, Home Depot MX | **NÃO MEDIDA** — desvio de país |
| `alicate/cortador_de_azulejo` | `torquês cortador de azulejo para mosaico Vonder Cortag` | Mercado Livre (4), Anhanguera Ferramentas (2), cortag.com (2), vonder.com.br (2) | **NÃO MEDIDA** — marca na consulta, defeito meu |
| `alicate/cortador_de_azulejo` | `como cortar pastilha de vidro para mosaico qual ferramenta` | 8 de 10 blog e resposta genérica: Vila do Artesão, Obramax, FazFácil (2), Além da Rua Atelier (2012), Artesanato Benjoino (2010), O Portal das Maravilhas (2); só 2 de loja | **ABERTA** |
| `acabamento/verniz` | `verniz para peça de mosaico artesanal qual usar` | Portal de Artesanato, Artesanato Benjoino (2010), Carla Arte e Cor (2010), Artesanato Local (2010), Revista Oeste, em.com.br, Viva Decora, Como Fazer Artesanatos, Maluli Armarinhos | **ABERTA** |

### AS DUAS ABERTAS SÃO PERGUNTA; AS DUAS TOMADAS SÃO PRODUTO — e isso não é sobre a categoria

O achado desta passada não é qual categoria vale: é **qual FORMA de filha vale**. As duas consultas
que a SERP recusa são as que nomeiam o **produto** (`pastilhas de vidro para mosaico`, `quantas
pastilhas vem na caixa`); as duas que ela abre são as que fazem a **pergunta** (`como cortar pastilha
de vidro`, `verniz para peça de mosaico`). E a causa é visível no próprio resultado: quem vende
produto já ocupa a consulta de produto — Mercado Livre, Elo7, Telhanorte, Pastilhart — e **ninguém
ocupa a consulta de método**, onde o que existe é blogspot de 2010 e resposta sem número.

Isso conversa direto com a nota de alcance do arquivo gerado acima: a ferramenta mede os recortes que
o **vocabulário** nomeia, que são recortes de tipo, e declara ser um **piso**. A SERP acabou de dizer
que o piso mede a forma errada — as duas filhas publicáveis desta ilha hoje são perguntas, e a régua
de contagem delas é a mesma, só aplicada a um recorte que o vocabulário não nomeia.

### O QUE CADA UMA DAS DUAS ABERTAS TEM DE NÚMERO, E É NÚMERO QUE A SERP NÃO PUBLICA

- **`como cortar pastilha de vidro para mosaico`** — nenhum dos oito resultados editoriais dá
  **espessura máxima de corte em mm**. O banco desta ilha dá: `espessura_maxima_de_corte_mm` está
  declarada em **4** dos 6 itens de `alicate`, com fonte de nível 2 ou 3. E a página nasce com a
  faixa descoberta que a 7b-bis já mediu em 25/09: o torquês de mosaico para em **5 mm**, e **3 das
  13** pastilhas do banco (`glassmosaic-st5102` 6 mm, `pastilhart-af1500` 8 mm, `glassmosaic-ic02`
  8 mm) **não cabem** — três dos treze produtos cuja quantidade a F1 já calcula não têm ferramenta
  declarada que os corte. Resposta que nenhuma das oito páginas tem, e ela é um número com dono.
- **`verniz para peça de mosaico artesanal`** — nenhum dos nove dá demãos, consumo em ml/m² nem tempo
  de secagem, e a metade deles fala de verniz genérico de artesanato. O banco dá `acabamento_visual`
  e `pelicula` em 3 dos 4 vernizes, com `demaos_minimas` e `consumo_ml_m2` por registro. **E dá a
  ausência, que vale mais:** a 7b-ter mediu em 25/09 que **nenhuma** das sete frases de fabricante de
  `acabamento` nomeia **vidro** e **nenhuma** nomeia **rejunte** — as duas superfícies que a peça de
  mosaico pronta expõe. A página que nascer aqui responde "o fabricante não declara", com o nome dos
  sete, e é a única do buraco que diz isso em vez de recomendar por analogia.

### O QUE ESTA MEDIÇÃO **NÃO** AUTORIZA

- **Não autoriza publicar nada.** A 16.5 continua exigindo 3 filhas por categoria, e o arquivo gerado
  acima mostra que **nenhuma categoria** do Guia alcança 3 — nem somando todos os tipos do
  vocabulário. Duas filhas abertas não são três.
- **Não autoriza escrever a `pastilha/vidro`**, que é a de mais banco da ilha (13 itens, três números
  em 12 deles). O dado passa e a SERP recusa, e os dois vereditos saem juntos.
- **Não substitui o corpus.** `verniz` **não existe** em `dados/corpus-buscas.md` — não tem faixa de
  volume medida, e a 14.9 exige o cruzamento de intenção com chance. A intenção é clara (é produto
  que a artesã compra) e o volume é **desconhecido**, e isto fica escrito em vez de estimado.
- **Não contradiz o corpus de 10/09 em silêncio, e contradiz.** O corpus classificou `pastilhas de
  vidro para mosaico` como **ABERTA**, com a mesma evidência que esta passada leu como tomada
  (anúncio da Shopee, Bazar Horizonte, Art Glass). A diferença não é de dado, é de régua: o corpus
  chamou de aberta porque **ninguém responde a pergunta técnica**, e a 14.9 manda classificar **quem
  ocupa** — e quem ocupa é marketplace, que é o primeiro galho dela, o do "a página NÃO nasce agora".
  As duas leituras cabem na mesma SERP e **a 14.9 é a que decide se a página nasce**. Quem for mexer
  no corpus lê este parágrafo primeiro; o que está velho lá é o rótulo daquela linha, não a evidência.
