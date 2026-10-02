# O cruzamento da 14.9 — os dois portoes no mesmo veredito

**GERADO por `ferramentas/cruzamento-14-9.py`. Nao edite a mao: `--conferir` regera e
compara.** As entradas sao `dados/filhas-do-guia.json` (o portao de DADO da secao 9,
derivado do banco) e `dados/serp-das-filhas.json` (o portao de SERP da 14.9, coletado por
busca). A 14.9 manda cruzar os dois — *"nunca de uma so"* — e ate 02/10/2026 ninguem
cruzava: uma metade era numero e a outra era prosa.

## O numero que manda

| veredito | recortes |
|---|---|
| `sem_nenhum_dos_dois` | 33 |
| `pode_nascer` | 5 |
| `espera_serp` | 3 |
| `espera_autoridade` | 1 |

**Podem nascer hoje, pelos DOIS portoes:** `acabamento`, `acabamento/impermeabilizante`, `acabamento/selador`, `acabamento/verniz`, `alicate/cortador_de_azulejo`

**Podem nascer, mas sem demanda medida:** nenhum

**Quando houver autoridade:** `pastilha/vidro`

**Dado verde e SERP nunca olhada** — o caso que mais custou nesta ilha, porque parece
passe livre: `alicate`, `pastilha`, `rejunte`

## A 16.5 — a mae de nivel 2 so nasce com 3 filhas, e filha nao e filha no dado: e no cruzamento

| categoria | filhas que o DADO autoriza | filhas que o CRUZAMENTO autoriza | veredito da mae | a mae pode nascer |
|---|---|---|---|---|
| `acabamento` | 3 | 3 | `pode_nascer` | **SIM** |
| `alicate` | 1 | 1 | `espera_serp` | nao |
| `apoio` | 0 | 0 | `sem_nenhum_dos_dois` | nao |
| `base` | 0 | 0 | `sem_nenhum_dos_dois` | nao |
| `cola` | 0 | 0 | `sem_nenhum_dos_dois` | nao |
| `pastilha` | 1 | 0 | `espera_serp` | nao |
| `rejunte` | 0 | 0 | `espera_serp` | nao |

## Recorte por recorte

| recorte | dado | itens | SERP | consultas medidas | veredito | o que falta |
|---|---|---|---|---|---|---|
| `acabamento` | `passa` | 10 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `acabamento/impermeabilizante` | `passa` | 3 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `acabamento/selador` | `passa` | 3 | `ABERTA` | 2 | **`pode_nascer`** | nada: os dois portoes abriram |
| `acabamento/verniz` | `passa` | 4 | `ABERTA` | 1 | **`pode_nascer`** | nada: os dois portoes abriram |
| `alicate` | `passa` | 6 | `SEM_MEDICAO` | 0 | **`espera_serp`** | olhar a SERP: o dado passa e ninguem classificou quem ocupa o top 10 |
| `alicate/cortador_de_azulejo` | `passa` | 3 | `ABERTA` | 3 | **`pode_nascer`** | nada: os dois portoes abriram |
| `alicate/martelinho` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `alicate/pinca_mosaico` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `alicate/torques` | `passa_na_contagem_sem_lastro` | 3 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) com fonte que sustente recomendacao primaria, e a SERP nunca foi olhada |
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
| `cola` | `passa_na_contagem_sem_lastro` | 7 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: um numero que a pagina calcule sobre 3 itens do mesmo recorte (a propriedade mais perto e `tempo_de_ajuste`), e a SERP nunca foi olhada |
| `cola/adesivo_para_espelho` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/cimentcola_acii` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/cimentcola_aciii` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/epoxi` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/pva` | `nao_passa` | 2 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 1 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/silicone_acetico` | `nao_passa` | 2 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 1 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `cola/silicone_neutro` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha` | `passa` | 13 | `SEM_MEDICAO` | 0 | **`espera_serp`** | olhar a SERP: o dado passa e ninguem classificou quem ocupa o top 10 |
| `pastilha/caco_azulejo` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/caco_espelho` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/ceramica` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/pedra` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/resina` | `nao_passa` | 0 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 3 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `pastilha/vidro` | `passa` | 13 | `TOMADA` | 2 | **`espera_autoridade`** | autoridade de dominio: quem ocupa a SERP e marketplace, loja ou fabricante |
| `rejunte` | `passa` | 5 | `SEM_MEDICAO` | 0 | **`espera_serp`** | olhar a SERP: o dado passa e ninguem classificou quem ocupa o top 10 |
| `rejunte/acrilico` | `nao_passa` | 1 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: 2 item(ns) de banco neste recorte, e a SERP nunca foi olhada |
| `rejunte/cimenticio` | `passa_na_contagem_sem_lastro` | 3 | `SEM_MEDICAO` | 0 | **`sem_nenhum_dos_dois`** | os dois: um numero que a pagina calcule sobre 3 itens do mesmo recorte (a propriedade mais perto e `liberacao_area_molhada_h`), e a SERP nunca foi olhada |
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

## Os numeros que a SERP nao publica e o banco desta ilha publica

E a resposta da 14.9 a pergunta *"por que ela consegue chegar as 10 primeiras"*, recorte
por recorte, com o numero na mao em vez do adjetivo.

- **`acabamento`** — a propria SERP recomenda a Resina Acrilica da Coral para peca de mosaico, e o fabricante EXCLUI superficie horizontal na mesma frase em que declara pedra — medido e gravado em 02/10/2026. Tampo e centro de mesa sao duas colecoes de uso da Loja desta ilha. Nenhum dos 10 resultados diz isso
- **`acabamento/impermeabilizante`** — `base_quimica` nos 3 impermeabilizantes do banco (duas resinas acrilicas e um silano-siloxano), com a frase do fabricante citada — contra `tinta betuminosa` sem marca e sem data. E a exclusao de superficie horizontal da Coral, que nenhum dos 10 menciona
- **`acabamento/selador`** — `tempo_de_secagem_h` nos 3 seladores do banco (6, 2 e 5 h) — e a separacao dos dois momentos, que e a propria definicao do esquema: `regras_da_categoria_acabamento` define selador pelo MOMENTO e nunca pelo substrato (versao 10). A SERP mistura os dois; o banco desta ilha nao pode
- **`acabamento/verniz`** — `acabamento_visual` e `pelicula` em 3 dos 4 vernizes, com `demaos_minimas` e `consumo_ml_m2` por registro — e a AUSENCIA medida pela 7b-ter: nenhuma frase de fabricante de `acabamento` nomeia vidro nem rejunte
- **`alicate/cortador_de_azulejo`** — espessura_maxima_de_corte_mm, declarada em 4 dos 6 itens de `alicate` com fonte de nivel 2 ou 3 — e a faixa descoberta da 7b-bis: o torques de mosaico para em 5 mm e 3 das 13 pastilhas do banco nao cabem

