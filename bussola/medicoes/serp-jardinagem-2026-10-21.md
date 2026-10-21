---
titulo: SERP paramétrica e informacional do nicho de JARDINAGEM — 21 consultas
medido_em: 2026-10-21
ferramenta: WebSearch da nuvem (índice sem geolocalização BR), dois passes por consulta (standard + extended)
recorte: Brasil, português, Google
medido_por: rodada 007 da Bússola, quatro coletores em paralelo
paginas_abertas: 0 — o egresso da nuvem recusa CONNECT para host .com.br
publicar: false
---

# SERP de jardinagem — 21 consultas, 4 famílias

Esta é a evidência da rodada 007. A leitura e o veredito estão em `bussola/rodadas/007.md`.

## AVISO DE INSTRUMENTO — leia antes de qualquer número

**Nenhuma página foi aberta.** Os quatro coletores tentaram `curl -sL` em 24 hosts brasileiros distintos
(petz.com.br, jardineiro.net, plantasevoce.com.br, cpt.com.br, agenteagricola.com.br, miniwebtool.com,
rosadodesertofortaleza.com.br, blog.plantei.com.br, jardim.biz, tudojardim.com, emporiotambo.com.br,
cultivarjardinagem.com.br, hortasemquintal.com.br, agron.com.br, jdv.com.br, guiadojardim.com,
orquideasnoape.com.br, entre outros) e **todos** devolveram `connect_rejected` no proxy (HTTP 000 ou 403 CONNECT).
Portanto **toda a coluna TIPO foi inferida de domínio, slug e título** — nunca do conteúdo.

**Consequência que vale para as 21 consultas:** a coluna `especialista-com-ficha` é **zero por não-medição, não por
ausência**. E, pela 30.8, **busca afirma presença, nunca ausência**: onde está escrito "não apareceu na busca",
leia exatamente isso. **Nenhuma destas 21 SERPs pode ser chamada de aberta.** Zero resultado de YouTube, de fórum e
de instituição em 42 buscas é sinal do instrumento, não do mercado: em jardinagem o carrossel de vídeo é quase
garantido em "como fazer muda" e em "como cuidar".

A coluna "dedicada" é `sim` ou `não medido`, nunca `não` — ler slug erra (30.8).

---

## Família A — "como fazer muda de X" (5 consultas) · 184.250 buscas/mês medidas no Planejador

| consulta | S_par | ocupantes dominantes do top-10 | especialista com ficha | fazenda/portal |
|---|---|---|---|---|
| como fazer muda de rosa do deserto | **2** | folhavitoria (1º), petz/blog (2º, título exato), uai `?p=82351`, catracalivre, tribunadejundiai, ellasmagazine, casaeconstrucao.org, psicopedagogia.com.br | não apareceu | **8 de 10** |
| como fazer muda de orquídea | **2** | **lojadomecanico.com.br/blog (1º — varejo de ferramentas respondendo jardinagem)**, tribunadejundiai, petz ×2, litoralmania, tupi.fm, orquideasnoape (2019), catracalivre, giulianaflores, hbatools2 | não apareceu | 5 de 10 |
| como fazer muda de alecrim | **1** | quintoandar.com.br/guias (1º), tudogostoso, **catracalivre com TRÊS URLs distintas**, tupi.fm, tribunadejundiai, jardimdocoracao, tudosobreplantas (2015), manualdojardim (2020) | não apareceu | **7 de 10** |
| como fazer muda de zamioculca | **2** | petz (1º, título exato), bandab `?p=`, diariodonordeste, tudogostoso, digitei.com, folhabv `?p=`, folhavitoria `-g4`, leouve `-g4`, jdv `-g4`, obemdito `-g4` | não apareceu | **9 de 10** |
| como fazer muda de jabuticaba | **2** | petz (1º, título exato), uai, correiobraziliense, agron.com.br `/como-10/`, gazetabrasilia, decorfacil, casaeconstrucao.org, cidesp, casaefesta, umcomo | não apareceu | 8 de 10 |

**Mediana S_par da família: 2.** Ocupantes de fora do Brasil: 1 provável em 50 linhas (casa.umcomo.com.br).

**Dois padrões estruturais desta família:**
1. **Nove URLs de cinco consultas terminam em `-g4`** (litoralmania, acordacidade, folhavitoria, leouve, jdv,
   obemdito). É uma **rede de conteúdo sindicalizado** empurrando a mesma pauta de jardinagem para portais
   regionais. Molde de fazenda operando dentro de portal de notícia: mesma pauta, muitos domínios, zero medição
   própria. Vale contar como **um ocupante**, não como seis concorrentes — e ele é imbatível em quantidade.
2. **Petz aparece em 4 das 5 consultas com o slug no título exato.** É o ocupante mais consistente do nicho.

---

## Família B — "como plantar X" (5 consultas) · 177.210 buscas/mês medidas no Planejador

O coletor desta família rodou duas camadas por consulta e **registrou a discordância entre elas**, que é o achado
mais importante da família: a consulta literal devolve portal de notícia; a consulta ampliada revela o cinturão de
especialista de nicho já indexado (jardineiro.net, plantanovaso, hortasemquintal, jardimdocoracao, guiadasplantas,
casajardimsintonia, cpt.com.br, agenteagricola). **O concorrente real do nicho existe e está indexado.**

| consulta | S_par (camada literal) | ocupantes dominantes | fazenda/portal |
|---|---|---|---|
| como plantar morango | **3** | tribunadejundiai, tudogostoso, revistaoeste, petz ×2, correiobraziliense ×2, tupi.fm, terrabrasilnoticias | 7 de 9 |
| como plantar girassol | **3** | **eos.com/pt/blog (1º — SaaS agrícola estrangeiro traduzido)**, ecycle, tudogostoso, tribunadejundiai ×2, petz ×2, revistaoeste, em.com.br | 7 de 9 |
| como plantar orquídea em vaso | **3** | **correiobraziliense com TRÊS URLs**, **petz com TRÊS URLs**, ecycle ×2, diariodonordeste | 6 de 9 |
| como plantar quiabo | **4** | tupi.fm ×2, em.com.br ×2, uai ×2, correiobraziliense ×2, tudogostoso — **7 das 9 do mesmo conglomerado (Diários Associados)** | **9 de 9** |
| como plantar uva em vaso | **4** | **petz com SEIS URLs** (AMP e `?p=` duplicados), correiobraziliense ×3 | 3 de 9 |

**Mediana S_par da família: 3.** Ocupantes de fora do Brasil: 2 em 90 linhas (eos.com, hortasbiologicas.pt).

**A ressalva que o próprio coletor escreveu, e que esta rodada acata:** *"as notas S_par acima estão calculadas
sobre a camada literal e provavelmente são otimistas por um ponto — com a camada ampliada pesando, morango,
girassol e orquídea tendem a 2-3, não 3."*

**Achado de conglomerado, novo na Bússola:** Estado de Minas (`em.com.br`), UAI, Correio Braziliense e Super Rádio
Tupi — **todos do grupo Diários Associados** — mais Tribuna de Jundiaí, TudoGostoso e Revista Oeste operam fazenda
editorial de jardinagem em escala, com várias páginas por consulta e títulos variados sobre o mesmo molde
("macio e sem fiapos", "pulgões longe"). São o ocupante dominante desta família.

---

## Família C — PARAMÉTRICA de insumo, "qual X para qual planta" (6 consultas) · **é a nota que decide**

Esta é a metade que uma ferramenta da ilha responderia, e portanto a que a seção 3 manda usar como S_par do nicho.

| consulta | S_par | ocupantes dominantes | calculadora instalada? |
|---|---|---|---|
| substrato para rosa do deserto | **1** | rosadodesertofortaleza/guiasubstrato, petz, decorfacil, ciporosadodeserto ×2, floraviva, **casaefesta ×2**, **melhoresparacomprar.com.br "Qual o Melhor substrato caseiro para rosa do deserto"** | não nesta SERP |
| adubo para zamioculca | 5 | **9 de 9 caça-clique**: tudogostoso ×2, bandab ×2, folhabv, tupi.fm, catracalivre, terrabrasilnoticias, tribunadejundiai | não |
| adubo para frutíferas em vaso | **3** | **br.my-best.com (1º, fazenda japonesa)**, catracalivre, extra/casasbahia/pontofrio (3 URLs do MESMO produto Forth Frutas, id 1570074729), tudogostoso, noticiasagricolas, correiobraziliense, olhardigital | não nesta SERP |
| qual adubo para orquídea | **1** | **br.my-best.com (1º)**, tupi.fm, **petz com TRÊS URLs**, **buscamelhores.com.br "Qual o Melhor Adubo para Orquídea Cattleya" (uma página por espécie)**, tnh1, **portalinsights.com.br/perguntas-frequentes/qual-adubo-a-orquidea-gosta (banco de FAQ, uma página por pergunta)** | não |
| adubo npk 10 10 10 para que serve | **1** | **faq.blackpilado.com.br com TRÊS URLs (uma página por fórmula: 10-10-10, 08-20-20, 8-20-20)**, **psicopedagogia.com.br com o título exato**, extra/casasbahia (mesmo id), magazineluiza ×2 (página de busca), comprerural | não nesta SERP, **sim no nicho** |
| qual o tamanho do vaso para cada planta | **1** | **petz com CINCO das 10 vagas**, agazeta, ojs.ceres.ufv.br (PDF), br.my-best.com, zoom.com.br, mercadolivre.com.br/blog | **sim, no eixo vizinho (litragem)** |

**Mediana S_par da família: 1. Média 2,0.** Ocupantes de fora do Brasil: 3, todos `br.my-best.com` (mybest Inc., Japão).

### O achado mais pesado da rodada: a resposta paramétrica central já está em máquina, em português

**Eixo "quanto adubo aplicar" — MORTO.** Calculadora indexada em pt-BR, dono brasileiro, mais fazenda de
calculadora traduzida já com `/br/` feito:

| URL | dono | português |
|---|---|---|
| textei.com.br/ferramentas/calculadora-adubo | Textei (BR) | nativo |
| agrododia.com.br/adubacao-npk.html | Agro do Dia (BR) | nativo |
| plantaselar.com.br/calculadora-adubo/ | Plantas e Lar (BR) | nativo |
| miniwebtool.com/br/calculadora-de-fertilizante-npk/ | MiniWebtool (EUA) | traduzida, slug em pt |
| miniwebtool.com/br/fertilizer-calculator-npk/ | MiniWebtool (EUA) | traduzida (2ª URL do mesmo tool) |
| miniwebtool.com/br/calculadora-de-fertilizante-para-gramado/ | MiniWebtool (EUA) | traduzida |

**Eixo "quantos litros de terra no vaso" — MORTO.** Seis máquinas indexadas em pt:
`ploys.com.br/curso-biopaisagismo/calculadora-de-terra-para-vasos` (BR) ·
`calculadoradomundo.com.br/jardim/terra-vegetal` (BR) · `acalculadoras.com.br/biologia/terra-vegetal/` (BR) ·
`casaejardim.portaltvcariri.com.br/calculadoras/substrato/` (BR) · `omnicalculator.com/pt/biologia/solo-para-vasos`
(Omni Calculator, Polônia — traduzida) · `pt.jardineriaon.com/calcular-pote-litros` (Espanha — traduzida).

**Eixo "espaçamento de plantio / mudas por m²" — MORTO.** `omnicalculator.com/pt/biologia/espacamento-entre-plantas`
e `calculover.com/pt-br/environment/agriculture/plant-spacing/`.

**Única ficha técnica tabelada achada em 8 buscas:** `agropos.com.br/tabela-de-adubacao/` — e é de terceiro, não de
fabricante.

**Os três eixos que a busca NÃO mostrou maquinizados:** (a) proporção de mistura de substrato por espécie — existe
em espanhol (`hacecuentas.com/calculadora-sustrato-mezcla-proporciones`) e não apareceu em pt-BR; (b) tamanho de
vaso por espécie; (c) qual fórmula NPK para qual planta (existe como tabela estática na AgroPós, não como máquina).
**Mas os três estão em SERPs cujo S_par medido é 1** — a vaga de máquina está livre e a vaga de SERP não está.

---

## Família D — nome de planta e cuidado (5 consultas) · 14.600 ("como cuidar") + 8.840 ("tipos de") + cabeças

| consulta | S_par | ocupantes dominantes | fora do BR |
|---|---|---|---|
| rosa do deserto | **2** | madeiramadeira, westwing, correiobraziliense, blog.plantei, plantasevoce, pepalantusambiental, casaefesta, antoniettasp, **cultivarjardinagem.com.br/rosa-do-deserto/ (título exato)**, ecycle, tribunadejundiai ×2, folhavitoria, tnh1 ×2, diariodonordeste | 0 de 17 |
| samambaia | **3** | blog.leroymerlin (1º), ecycle, ikebanaflores, brasil.perfil, blog.plantei, petz, ciclovivo, plantasevoce, brotacompany · **o termo seco sangra para o rio e a cidade satélite do DF** | 4 de 17 |
| tipos de samambaia | **1** | tribunadejundiai, blog.cobasi, wikipédia, petz, emporiotambo, blog.plantei, **tudojardim.com/tipos-de-samambaias/ e jardim.biz/tipos-de-samambaia/ (título exato, uma com ano no título)** | 0 de 15 |
| como cuidar de suculenta | **1** | blog.cobasi, idealista.pt, blog.leroymerlin, plantinhasuculenta, jardineiro.net, brotacompany, bonsaiurbano, cbzoo, cultivarjardinagem, ecycle ×2, correiobraziliense, sodimac.cl, **concursosnobrasil.com com QUATRO variações do mesmo título**, chavesnamao | 3 de 18 |
| plantas para apartamento pouca luz | **1** | ndmais, crusoe, enfeitedecora, ellasmagazine, **pacpme.com.br ×2**, brisajardim, **terrabrasilnoticias ×2**, substack, itatiaia, idealista.pt, **tupi.fm ×2**, revistaoeste, em.com.br, correiobraziliense, catracalivre | 1 de 18 |

**Mediana S_par da família: 1.**

O caso de `concursosnobrasil.com` — um site de concursos públicos ocupando **quatro posições** com quatro variações
do mesmo título sobre suculenta — é a fazenda em estado puro, e está na família de consulta de maior volume de
cabeça do nicho.

---

## Agregado das 21 consultas

| família | consultas | volume/mês medido | mediana S_par | leitura |
|---|---|---|---|---|
| A — como fazer muda de X | 5 | 184.250 | **2** | rede `-g4` + Petz no título exato |
| B — como plantar X | 5 | 177.210 | **3** (otimista por ~1) | fazenda editorial dos Diários Associados |
| C — paramétrica de insumo | 6 | ≈ 19.700 (exemplos medidos) | **1** | fazenda no título exato + máquina já instalada |
| D — nome de planta e cuidado | 5 | 23.440 + cabeças | **1** | fazenda com título exato em 3 de 5 |

**S_par do nicho, pela seção 3 (a nota é a da busca PARAMÉTRICA): 1.**

## Nomes novos de fazenda que esta rodada encontrou

Agrupados por molde, para a próxima rodada reconhecer o seguinte:

- **Rede de conteúdo sindicalizado de jardinagem** (marcador `-g4` no fim do slug, mesma pauta em muitos portais
  regionais): `litoralmania.com.br`, `acordacidade.com.br`, `leouve.com.br`, `jdv.com.br`, `obemdito.com.br`,
  `folhabv.com.br`, `bandab.com.br`, `gazetabrasilia.com.br`, `tnh1.com.br`, `ndmais.com.br`, `itatiaia.com.br`,
  `agazeta.com.br`, `crusoe.com.br`, `ellasmagazine.com.br`, `diariodonordeste.verdesmares.com.br`,
  `tribunadejundiai.com.br`, `folhavitoria.com.br`.
- **Conglomerado publicando fazenda editorial de jardinagem** (várias páginas por consulta, títulos variados sobre
  o mesmo molde): `em.com.br/emfoco/`, `uai.com.br`, `correiobraziliense.com.br/cbradar/`, `tupi.fm`,
  `tudogostoso.com.br/noticias/`, `revistaoeste.com`, `catracalivre.com.br/noticias/`, `ecycle.com.br`.
- **Domínio sem relação com o nicho respondendo jardinagem (parasita puro)**: `psicopedagogia.com.br` (adubo
  10-10-10 e muda de rosa do deserto), `concursosnobrasil.com` (suculenta, 4 posições), `pacpme.com.br`,
  `cbzoo.com.br`, `lojadomecanico.com.br/blog` (1º lugar em muda de orquídea), `hbatools2.com.br`,
  `blog.7mboots.com.br`, `capitalist.com.br`, `chavesnamao.com.br`, `quintoandar.com.br/guias/` (já listado),
  `projetoagathaedu.com.br` (já listado).
- **Banco de FAQ ou de glossário gerado, uma página por pergunta ou por valor de parâmetro**:
  `faq.blackpilado.com.br` (já listado — aqui com 3 URLs numa SERP), `portalinsights.com.br/perguntas-frequentes/`
  (já listado), `mapaagro.com.br/glossario/`, `vocepergunta.com` (já listado).
- **Fazenda de ranking com edição brasileira**: `br.my-best.com` (já listado; 1º lugar em 3 das 6 paramétricas),
  `melhoresparacomprar.com.br` e `buscamelhores.com.br` (já listados — aqui com página por espécie).
- **Fazenda de jardinagem com título exato de consulta**: `casaeconstrucao.org`, `jardinagem.casaefesta.com`,
  `cultivarjardinagem.com.br`, `tudojardim.com`, `jardim.biz`, `decorfacil.com`, `digitei.com` (já listado),
  `cidesp.com.br` (já listado), `enfeitedecora.com`, `terrabrasilnoticias.com`, `essaseoutras.com.br`,
  `passoapasso.com`, `casajardimsintonia.com.br`, `pepalantusambiental.com.br`, `antoniettasp.com.br`,
  `casa.umcomo.com.br`, `agron.com.br`, `hortasbiologicas.pt`.
- **Calculadora servindo o parâmetro central do nicho** (o molde da nota 0 proposta na 006): `textei.com.br`,
  `agrododia.com.br`, `plantaselar.com.br`, `ploys.com.br`, `calculadoradomundo.com.br`, `acalculadoras.com.br`,
  `casaejardim.portaltvcariri.com.br`, `calculover.com/pt-br`, `miniwebtool.com/br` (já listado),
  `omnicalculator.com/pt` (já listado), `pt.jardineriaon.com`, `hacecuentas.com` (já listado).

## Ressalvas

1. **Zero página aberta, 24 hosts recusados pelo egresso.** Toda classificação é de domínio, slug e título.
2. **O instrumento não é a SERP brasileira.** Afirma presença; não afirma ausência de ninguém (30.8).
3. **Posição é ordem de devolução, não posição no Google.** Duplicatas AMP e `?p=` do mesmo artigo foram contadas
   como linhas separadas porque vieram separadas — leia como **um host**, não como vários.
4. **Resposta de IA no topo e bloco de vídeo não são mensuráveis daqui.** Em "como cuidar de" e "tipos de" o
   desconto de clique por painel de IA é **presumido e não medido**. Só navegador em IP brasileiro resolve.
5. **Nenhuma consulta recebeu S_par 0**, e dois coletores registraram que as consultas de vaso e de NPK estão a um
   passo dela: a máquina que responde o parâmetro já existe indexada em pt-BR, só ainda não ranqueou nessas frases
   exatas no índice medido. Pela **letra** da régua atual (nota 0 = "calculadora de grande varejista instalada"),
   nada disso dispara 0 — pela **proposta de régua por função** registrada na 006, dispararia.
6. **Classificações em dúvida, registradas:** `ciporosadodeserto.com.br` e `rosadodesertogoias.com.br` podem ser
   viveiros (`loja`) e não blogs; `agron.com.br` pode ser `especialista-com-ficha` real e o slug `/como-10/` pode
   ser legado; `floraviva.com.br`, `decorfacil.com`, `labra.com.br` (fabricante de vasos) e `ecycle.com.br` são
   borda. `brasil.perfil.com` é do grupo argentino Perfil com edição brasileira, contado como fora do Brasil.
7. **Candidatos a `especialista-com-ficha` que uma leitura de navegador pode reclassificar** — e que subiriam
   S_par nas famílias A, B e D: `jardineiro.net`, `cpt.com.br` (título com nome científico), `agenteagricola.com.br`
   ("Guia da Semente à Colheita"), `plantinhasuculenta.com.br`, `plantasevoce.com.br`, `emporiotambo.com.br`,
   `blog.plantei.com.br`, `agropos.com.br`.
