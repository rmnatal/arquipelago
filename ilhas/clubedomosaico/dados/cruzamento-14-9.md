# O cruzamento da 14.9 — os dois portoes no mesmo veredito

**GERADO por `ferramentas/cruzamento-14-9.py`. Nao edite a mao: `--conferir` regera e
compara.** As entradas sao `dados/filhas-do-guia.json` (o portao de DADO da secao 9,
derivado do banco) e `dados/serp-das-filhas.json` (o portao de SERP da 14.9, coletado por
busca). A 14.9 manda cruzar os dois — *"nunca de uma so"* — e ate 02/10/2026 ninguem
cruzava: uma metade era numero e a outra era prosa.

## O numero que manda

| veredito | recortes |
|---|---|
| `sem_nenhum_dos_dois` | 31 |
| `pode_nascer` | 11 |

**Podem nascer hoje, pelos DOIS portoes:** `acabamento`, `acabamento/impermeabilizante`, `acabamento/selador`, `acabamento/verniz`, `alicate`, `alicate/cortador_de_azulejo`, `alicate/torques`, `pastilha`, `pastilha/vidro`, `rejunte`, `rejunte/cimenticio`

**Podem nascer, mas sem demanda medida:** nenhum

**Quando houver autoridade:** nenhum

**Dado verde e SERP nunca olhada** — o caso que mais custou nesta ilha, porque parece
passe livre: nenhum

## A 16.5 — a mae de nivel 2 so nasce com 3 filhas, e filha se conta por CONSULTA

Duas correcoes de leitura, nesta ordem. **02/10/2026:** 3 filhas que passam no DADO nao sao 3
filhas que podem nascer — por isso a coluna do cruzamento. **07/10/2026:** filha nao se conta
por RECORTE, e por **consulta aberta**. As filhas em forma de PERGUNTA entram na conta, e na
mesma conta pergunta e tipo que miram a MESMA consulta valem **uma** filha: duas paginas na
mesma consulta nao sao duas filhas, sao a mesma pagina duas vezes. A consulta da mae nao
conta — ela e a pagina de nivel 2, nao filha de si mesma.

| categoria | filhas no DADO | filhas no CRUZAMENTO (tipos) | perguntas | **filhas por CONSULTA** | veredito da mae | a mae pode nascer |
|---|---|---|---|---|---|---|
| `acabamento` | 3 | 3 | 0 | **3** | `pode_nascer` | **SIM** |
| `alicate` | 2 | 2 | 1 | **2** | `pode_nascer` | nao |
| `apoio` | 0 | 0 | 0 | **0** | `sem_nenhum_dos_dois` | nao |
| `base` | 0 | 0 | 0 | **0** | `sem_nenhum_dos_dois` | nao |
| `cola` | 0 | 0 | 0 | **0** | `sem_nenhum_dos_dois` | nao |
| `pastilha` | 1 | 1 | 0 | **1** | `pode_nascer` | nao |
| `rejunte` | 1 | 1 | 1 | **2** | `pode_nascer` | nao |

### A FILA DAS MAES, ordenada por quanto FALTA e nao por quantos tipos tem dado verde

Esta tabela nasceu em 09/10/2026, e a causa dela tem data e custo. Ate 08/10 a pergunta
"qual e o proximo bloco" era respondida pelo `caminho_mais_barato_para_as_3_filhas` de
`filhas-do-guia.json`, que conta **tipo com dado verde**. A execucao de 08/10 leu dali que a
`alicate` estava a UMA filha com TRES itens a coletar e escolheu o bloco por isso. Pela conta
que decide a 16.5 — a desta pagina — a `alicate` estava a **duas**, e os tres itens eram de um
tipo que a propria ilha havia fechado no dia anterior como **nao coletavel neste canal**. A
conta da 16.5 mora aqui; a fila dela passa a morar aqui tambem.

| categoria | filhas por CONSULTA | faltam | o que a proxima filha custa |
|---|---|---|---|
| `acabamento` | 3 | **0** | nada: a 16.5 esta fechada por consulta |
| `alicate` | 2 | **1** | MEDIR SERP NAO E CAMINHO AQUI, e isto e medido e nao suposto: a(s) unica(s) candidata(s) com dado verde e sem consulta propria — `alicate/cortador_de_azulejo`, `pergunta:alicate-espessura-de-corte` — ja teve(ram) 8 tentativa(s) de consulta propria medida(s) e falhada(s) por instrumento, com o motivo de cada uma em `serp-das-filhas.json`. A 1 filha(s) que falta(m) custa(m) ITEM DE BANCO ou PERGUNTA NOVA, e antes de escrever consulta nova leia `o_canal_e_os_limites_dele` naquele arquivo — a consulta de uma filha nunca pede o numero (limite 5). |
| `rejunte` | 2 | **1** | ITEM DE BANCO ou PERGUNTA NOVA: toda candidata com dado verde desta categoria ja tem consulta aberta propria, entao a 1 filha(s) que falta(m) nao sai(em) de medir SERP. Qual tipo ainda e coletavel esta em `filhas-do-guia.json`, no campo `tipos_fechados_por_canal` da categoria — tipo fechado por canal NAO e caminho. |
| `pastilha` | 1 | **2** | ITEM DE BANCO ou PERGUNTA NOVA: toda candidata com dado verde desta categoria ja tem consulta aberta propria, entao a 2 filha(s) que falta(m) nao sai(em) de medir SERP. Qual tipo ainda e coletavel esta em `filhas-do-guia.json`, no campo `tipos_fechados_por_canal` da categoria — tipo fechado por canal NAO e caminho. |
| `apoio` | 0 | **3** | ITEM DE BANCO ou PERGUNTA NOVA: toda candidata com dado verde desta categoria ja tem consulta aberta propria, entao a 3 filha(s) que falta(m) nao sai(em) de medir SERP. Qual tipo ainda e coletavel esta em `filhas-do-guia.json`, no campo `tipos_fechados_por_canal` da categoria — tipo fechado por canal NAO e caminho. |
| `base` | 0 | **3** | ITEM DE BANCO ou PERGUNTA NOVA: toda candidata com dado verde desta categoria ja tem consulta aberta propria, entao a 3 filha(s) que falta(m) nao sai(em) de medir SERP. Qual tipo ainda e coletavel esta em `filhas-do-guia.json`, no campo `tipos_fechados_por_canal` da categoria — tipo fechado por canal NAO e caminho. |
| `cola` | 0 | **3** | ITEM DE BANCO ou PERGUNTA NOVA: toda candidata com dado verde desta categoria ja tem consulta aberta propria, entao a 3 filha(s) que falta(m) nao sai(em) de medir SERP. Qual tipo ainda e coletavel esta em `filhas-do-guia.json`, no campo `tipos_fechados_por_canal` da categoria — tipo fechado por canal NAO e caminho. |

**A proxima mae do Guia e a `alicate`**, a 1 filha(s) por consulta. MEDIR SERP NAO E CAMINHO AQUI, e isto e medido e nao suposto: a(s) unica(s) candidata(s) com dado verde e sem consulta propria — `alicate/cortador_de_azulejo`, `pergunta:alicate-espessura-de-corte` — ja teve(ram) 8 tentativa(s) de consulta propria medida(s) e falhada(s) por instrumento, com o motivo de cada uma em `serp-das-filhas.json`. A 1 filha(s) que falta(m) custa(m) ITEM DE BANCO ou PERGUNTA NOVA, e antes de escrever consulta nova leia `o_canal_e_os_limites_dele` naquele arquivo — a consulta de uma filha nunca pede o numero (limite 5).

### O QUE JA FOI MEDIDO E FALHOU — nao repita a consulta

Tentativa de consulta propria classificada `NAO_MEDIDA` em `serp-das-filhas.json`, por
candidata. Ate 09/10/2026 a fila acima nao as contava, e por isso prometia `a coisa mais
barata que existe nesta categoria` para candidata cuja consulta propria ja havia falhado
cinco vezes. Antes de escrever consulta nova, leia `o_canal_e_os_limites_dele` naquele
arquivo: a consulta-alvo de uma filha **nunca pede o numero** (limite 5).

| categoria | candidata | tentativas | consultas que falharam |
|---|---|---|---|
| `alicate` | `alicate/cortador_de_azulejo` | **4** | cortador de azulejo manual para mosaico (2026-09-30) · torques cortador de azulejo para mosaico Vonder Cortag (2026-09-30) · ate quantos milimetros o cortador manual de azulejo corta pastilha de mosaico (2026-10-07) · qual ferramenta corta caquinho de azulejo e pastilha para mosaico artesanal espessura (2026-10-07) |
| `alicate` | `pergunta:alicate-espessura-de-corte` | **4** | ate quantos milimetros de espessura o alicate corta pastilha e caquinho para mosaico artesanal (2026-10-07) · alicate de mosaico artesanal ate quantos milimetros de caquinho ele corta vidro ceramica (2026-10-09) · alicate de mosaico corta pastilha de quantos milimetros de espessura (2026-10-09) · alicate de mosaico ou torques espessura maxima de azulejo que corta mm artesanato (2026-10-09) |

**Consultas disputadas por mais de uma candidata** — cada uma delas vale UMA filha, e e
aqui que a conta por recorte inflava:

- `alicate` — *como cortar pastilha de vidro para mosaico qual ferramenta* e disputada por `alicate/cortador_de_azulejo`, `pergunta:alicate-espessura-de-corte`

## As filhas em forma de PERGUNTA, cruzadas

Elas vem medidas no portao de DADO por `filhas-do-guia.py`, pela mesma regua dos recortes de
tipo, e se ligam a SERP pela **consulta**, nao pelo nome do recorte — consulta e consulta, e
onde ela foi arquivada e acidente de quem mediu primeiro.

| pergunta | categoria | itens | SERP | veredito | consulta-alvo tambem creditada a | o que falta |
|---|---|---|---|---|---|---|
| `pergunta:alicate-espessura-de-corte` | `alicate` | 4 | `ABERTA` | **`pode_nascer`** | `alicate/cortador_de_azulejo` | nada: os dois portoes abriram |
| `pergunta:rejunte-largura-da-junta` | `rejunte` | 5 | `ABERTA` | **`pode_nascer`** | — | nada: os dois portoes abriram |
| `pergunta:pastilha-placa-ou-caixa` | `pastilha` | 12 | `TOMADA` | **`espera_autoridade`** | — | autoridade de dominio: quem ocupa a SERP e marketplace, loja ou fabricante |

- **`pergunta:alicate-espessura-de-corte`** — consulta-alvo: *como cortar pastilha de vidro para mosaico qual ferramenta*
- **`pergunta:rejunte-largura-da-junta`** — consulta-alvo: *da para colar os caquinhos bem juntos no mosaico ou precisa deixar espaco para o rejunte*
- **`pergunta:pastilha-placa-ou-caixa`** — consulta-alvo: *da para comprar so uma placa de pastilha de vidro para mosaico ou precisa levar a caixa fechada*

## Recorte por recorte

| recorte | dado | itens | SERP | consultas medidas | veredito | o que falta |
|---|---|---|---|---|---|---|
| `acabamento` | `passa` | 10 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `acabamento/impermeabilizante` | `passa` | 3 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `acabamento/selador` | `passa` | 3 | `ABERTA` | 2 | **`pode_nascer`** | nada: os dois portoes abriram |
| `acabamento/verniz` | `passa` | 4 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `alicate` | `passa` | 6 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `alicate/cortador_de_azulejo` | `passa` | 3 | `ABERTA` | 5 | **`pode_nascer`** | nada: os dois portoes abriram |
| `alicate/martelinho` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `alicate/pinca_mosaico` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `alicate/torques` | `passa` | 3 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `apoio` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `apoio/desempenadeira` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `apoio/espatula` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `apoio/luva` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `apoio/marcador` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `apoio/oculos` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `apoio/pinca` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `base` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `base/ceramica_crua` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `base/cimento` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `base/isopor_estrutural` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `base/mdf_cru` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `base/moldura` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola` | `passa_na_contagem_sem_lastro` | 7 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: um numero que a pagina calcule sobre 3 itens do mesmo recorte (a propriedade mais perto e `tempo_em_aberto`), e a SERP nunca foi olhada |
| `cola/adesivo_para_espelho` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/cimentcola_acii` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/cimentcola_aciii` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/epoxi` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/pva` | `nao_passa` | 2 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 1 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/silicone_acetico` | `nao_passa` | 2 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 1 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/silicone_neutro` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha` | `passa` | 13 | `ABERTA` | 2 | **`pode_nascer`** | nada: os dois portoes abriram |
| `pastilha/caco_azulejo` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/caco_espelho` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/ceramica` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/pedra` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/resina` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/vidro` | `passa` | 13 | `ABERTA` | 2 | **`pode_nascer`** | nada: os dois portoes abriram |
| `rejunte` | `passa` | 5 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `rejunte/acrilico` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `rejunte/cimenticio` | `passa` | 3 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `rejunte/epoxi` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `rejunte/flexivel` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |

## O pedido de faixa de volume, derivado — nao digitado

A 14.9 cruza intencao com chance. A chance esta medida na SERP; a **intencao** se mede
por faixa de volume, e o Planejador de palavras-chave esta na conta do Raphael, no
navegador dele. Onde a faixa falta, esta ferramenta nao estima: ela deriva o pedido. **So
consulta ABERTA entra** — faixa de consulta que nao vai nascer e numero que ninguem usa.

| consulta | exigida pelo recorte | veredito do recorte |
|---|---|---|
| `acabamento para peca de mosaico artesanal qual produto passar depois do rejunte` | `acabamento` | `pode_nascer` |
| `como impermeabilizar peca de mosaico para ficar no jardim na chuva` | `acabamento/impermeabilizante` | `pode_nascer` |
| `precisa passar selador na base antes de colar mosaico em MDF ou ceramica` | `acabamento/selador` | `pode_nascer` |
| `selar vaso de ceramica antes de fazer mosaico artesanato precisa selador` | `acabamento/selador` | `pode_nascer` |
| `verniz para peca de mosaico artesanal qual usar` | `acabamento/verniz` | `pode_nascer` |
| `como cortar pastilha de vidro para mosaico qual ferramenta` | `alicate/cortador_de_azulejo` | `pode_nascer` |
| `quanto tempo esperar para molhar peca de mosaico depois do rejunte cimenticio` | `rejunte/cimenticio` | `pode_nascer` |
| `como cortar pastilha de vidro para mosaico qual ferramenta` | `pergunta:alicate-espessura-de-corte` | `pode_nascer` |
| `da para colar os caquinhos bem juntos no mosaico ou precisa deixar espaco para o rejunte` | `pergunta:rejunte-largura-da-junta` | `pode_nascer` |

## Os numeros que a SERP nao publica e o banco desta ilha publica

E a resposta da 14.9 a pergunta *"por que ela consegue chegar as 10 primeiras"*, recorte
por recorte, com o numero na mao em vez do adjetivo.

- **`acabamento`** — a propria SERP recomenda a Resina Acrilica da Coral para peca de mosaico, e o fabricante EXCLUI superficie horizontal na mesma frase em que declara pedra — medido e gravado em 02/10/2026. Tampo e centro de mesa sao duas colecoes de uso da Loja desta ilha. Nenhum dos 10 resultados diz isso
- **`acabamento/impermeabilizante`** — `base_quimica` nos 3 impermeabilizantes do banco (duas resinas acrilicas e um silano-siloxano), com a frase do fabricante citada — contra `tinta betuminosa` sem marca e sem data. E a exclusao de superficie horizontal da Coral, que nenhum dos 10 menciona
- **`acabamento/selador`** — `tempo_de_secagem_h` nos 3 seladores do banco (6, 2 e 5 h) — e a separacao dos dois momentos, que e a propria definicao do esquema: `regras_da_categoria_acabamento` define selador pelo MOMENTO e nunca pelo substrato (versao 10). A SERP mistura os dois; o banco desta ilha nao pode
- **`acabamento/verniz`** — `acabamento_visual` e `pelicula` em 3 dos 4 vernizes, com `demaos_minimas` e `consumo_ml_m2` por registro — e a AUSENCIA medida pela 7b-ter: nenhuma frase de fabricante de `acabamento` nomeia vidro nem rejunte
- **`alicate`** — espessura_maxima_de_corte_mm por TIPO de alicate. A medicao de 30/09 em `alicate/cortador_de_azulejo` ja tinha achado o mesmo buraco na filha; aqui ele aparece na MAE, e com a tabela ferramenta x material que o corpus de 10/09 pediu na linha 92 e que ninguem publicou
- **`alicate/cortador_de_azulejo`** — espessura_maxima_de_corte_mm, declarada em 4 dos 6 itens de `alicate` com fonte de nivel 2 ou 3 — e a faixa descoberta da 7b-bis: o torques de mosaico para em 5 mm e 3 das 13 pastilhas do banco nao cabem
- **`alicate/torques`** — espessura_maxima_de_corte_mm por tipo de videa. A SERP publica a REGRA qualitativa (roldana para vidro, reta para ceramica) e nenhum dos dez publica o limite em mm — que e o lastro que este recorte precisa e que 2 dos 3 itens do banco ainda nao sustentam
- **`pastilha`** — pastilhas por m2 e por peca, por medida de pastilha e largura de junta — que e exatamente o que a F1 desta ilha calcula e serve em /materiais/quantas-pastilhas-para-mosaico/. A SERP de `pastilha` nao publica o numero, mas quem a ocupa vende o produto: aqui o buraco de numero NAO abre a consulta
- **`rejunte`** — gramas de rejunte por area, por largura de junta e por espessura de pastilha — a F1 desta ilha ja o devolve (264 g para o cilindro 20x30 com junta de 2 mm, conferido na mao em 02/10) — e o cruzamento de tipo de rejunte x ambiente x largura de junta, que a F2 ja resolve e que nenhum dos nove publica
- **`rejunte/cimenticio`** — liberacao_area_molhada_h POR PRODUTO, da declaracao do fabricante — que e exatamente a propriedade que o portao de dado deste recorte cobra como lastro. A SERP publica numero de obra, de terceiro e contraditorio; a ilha publicaria numero do fabricante, por item, com a frase citada
- **`pergunta:alicate-espessura-de-corte`** — espessura_maxima_de_corte_mm, declarada em 4 dos 6 itens de `alicate` com fonte de nivel 2 ou 3 — e a faixa descoberta da 7b-bis: o torques de mosaico para em 5 mm e 3 das 13 pastilhas do banco nao cabem
- **`pergunta:alicate-espessura-de-corte`** — o limite em mm por TIPO de ferramenta, declarado pelo FABRICANTE. O que a SERP devolveu foi numero de VENDEDOR e de grandeza trocada: Rubi 15 mm de `capacidade de corte` (loja espanhola), Mejix 19 mm de ABERTURA DA GARRA (que nao e espessura de corte), Sumer 8 mm de revestimento e vidro (pagina de produto brasileira). Tres numeros, tres grandezas, nenhum fabricante brasileiro.
- **`pergunta:rejunte-largura-da-junta`** — a faixa de junta em milimetros que cada rejunte cobre — `junta_min_mm` e `junta_max_mm`, declaradas por 5 de 5 rejuntes deste banco com fonte de nivel 2 nos cinco, e com as tres faixas separando os tres tipos: acrilico de 1 a 4 mm, epoxi de 1 a 5 mm, cimenticio de 2 a 10 mm. A faixa descoberta que a pagina tem de DIZER, pela 14.3, e o piso de 2 mm dos tres cimenticios: quem encosta os caquinhos nao tem rejunte cimenticio no banco que o atenda, e os dois que chegam a 1 mm sao o acrilico e o epoxi.
- **`pergunta:pastilha-placa-ou-caixa`** — quanto vem numa caixa de pastilha de vidro e qual e o menor lote que o fabricante fecha. Medido no banco em 08/10/2026: `placas_por_caixa` de 10 a 22 e `m2_por_caixa` de 0,85 a 2,09, declarados por 12 dos 13 itens ativos com fonte de nivel 3. O numero nao foi servido porque a SERP e TOMADA, e ele fica escrito aqui para quem for publicar nao recoletar.

