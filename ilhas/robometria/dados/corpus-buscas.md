---
titulo: Levantamento de buscas paramétricas — Robometria
bloco: 1
gerado_em: 2026-09-09
publicar: false
---

# Corpus de buscas — Robometria

Bloco 1 da fila. Levantamento de consultas reais do nicho de robô aspirador no
Brasil, agrupadas em clusters de ferramenta, com procedência marcada consulta
a consulta. Coletado via busca web (resultados de página, títulos de anúncio,
títulos de vídeo, fórum) em 09/09/2026 — não houve acesso a ferramenta de
volume de busca (Google Keyword Planner, Ubersuggest etc.), então **nenhum
número de volume mensal é citado aqui**. Onde o corpus de origem (Aquametria)
citava "N consultas", aquele número vinha de uma coleta com outra ferramenta;
aqui a métrica que existe é variedade de formulação e recorrência entre
fontes independentes, não contagem de busca.

Dois eixos, como manda o `PROMPT.md`, e eles **não se misturam** em nenhuma
ferramenta: compatibilidade é "essa peça serve no meu robô", dimensionamento
é "que robô/config serve na minha casa".

---

## 1. Eixo COMPATIBILIDADE (peça × modelo)

### Cluster A1 — Filtro (HEPA e de entrada)

| Consulta (formulação real ou próxima) | Procedência |
|---|---|
| "filtro robô aspirador Multilaser" | busca web — página oficial Multilaser + Amazon + Mercado Livre, todas competindo pelo mesmo termo |
| "filtro compatível robô aspirador Multilaser HO041" | título de anúncio, Magazine Escorrega ("Parceiro das Peças") |
| "filtro hepa robô aspirador Multilaser HO03/HO04" | página oficial Multilaser (nomeia o modelo no próprio título do produto) |
| "filtro hepa robô aspirador Positivo PRA500" | Mercado Livre, título de anúncio |
| "filtro hepa robô aspirador Positivo PRA8000 PRA2000" (mesmo filtro para os dois) | loja oficial Positivo — declara compatibilidade cruzada entre dois modelos |
| "filtro hepa robô aspirador Positivo PRA1000" | Techtudo, listagem de modelos |
| "quando trocar filtro robô aspirador" | Guia de Compras Brasil, artigo dedicado ao tema |
| "filtro hepa universal robô aspirador" (negativo — a fonte avisa contra) | roboaspiradortech.com.br, blog do nicho: "nunca compre filtro HEPA universal, pois filtros têm encaixes diferentes" |
| "filtro robô aspirador Xiaomi Mop 2 trocar a cada quanto tempo" | roboaspiradortech.com.br — recomenda 2–3 meses, checagem pelo app Mi Home |

**Achado do cluster:** cada fabricante nomeia o filtro pelo código do modelo
(HO041, PRA500, PRA8000/2000), e ao menos uma marca (Multilaser) já vende kit
com escova + filtro juntos — sinal de que o par "peça + modelo" é a unidade
de busca real, não a peça isolada. E existe alerta explícito, publicado por
um blog do próprio nicho, contra o "filtro universal": é exatamente o
problema que a Robometria existe para resolver com dado verificado por
modelo, em vez de counter-marketing genérico.

### Cluster A2 — Escova lateral

| Consulta | Procedência |
|---|---|
| "escova lateral robô aspirador compatível qual modelo" | busca web direta |
| "escova lateral Multilaser HO041 HO400 HO401 HO407 OB010" (uma peça para cinco modelos) | Multilaser — página de produto lista os códigos compatíveis |
| "kit escova lateral Xiaomi Mop 2 Lite" | Mercado Livre, título de anúncio |
| "escova lateral Positivo Casa Inteligente" | loja oficial Positivo |
| "escova lateral giratória Roomba série s" (kit com 3 unidades) | irobotloja.com.br |
| "escova lateral genérica V3 V5 A4 A6" (uma peça anunciada para quatro "modelos" sem marca clara) | Amazon — anúncio de terceiro, nomenclatura de modelo ambígua |
| "escova lateral robô aspirador não gira, como consertar" | dois sites de guia técnico (hundred-worries, techinfus) — sintoma, não compra, mas mesma intenção de compatibilidade/peça |
| "escova lateral quebrou robô aspirador onde comprar substituta" | busca web — retorna KaBuM, Electrolux, Positivo, Xiaomi, iRobot, cada um só vendendo a própria peça |

**Achado do cluster:** a compatibilidade cruzada existe de fábrica em alguns
casos (Multilaser: 1 escova para 5 códigos de modelo), mas cada marca só
vende a própria peça — não existe comparador cross-marca, que é exatamente o
buraco identificado pela Bússola. O anúncio "V3 V5 A4 A6" sem marca no título
é um sintoma do problema: o comprador não sabe de qual fabricante é o
"modelo" que está comprando peça para.

### Cluster A3 — Mop (pano de passar)

| Consulta | Procedência |
|---|---|
| "mop robô aspirador compatível modelo" | busca web direta |
| "MOP VDS MOPRALW-C" — peça original nomeada pelo código do robô (RALW-C) | loja oficial Velds |
| "robô aspirador com mop" (comparativo de modelos, não de peça) | Techtudo, Mundo Conectado — listas de produto, não de reposição |
| "reservatório de água robô aspirador quantos ml" (250 ml WAP W100, dado técnico junto da ficha) | blog WAP |

**Achado do cluster:** cluster mais fino que filtro e escova — a maior parte
do volume encontrado é sobre "qual robô comprar com mop" (dimensionamento/
compra), não sobre reposição da peça mop em si. Ainda assim, o padrão de
nomear a peça pelo código do robô (RALW-C → MOPRALW-C) se repete.

### Cluster A4 — Bateria

| Consulta | Procedência |
|---|---|
| "bateria robô aspirador Xiaomi durabilidade" | busca web, blog roboaspiradortech.com.br |
| "quanto tempo dura bateria robô aspirador" | casadoseletrodomesticos.com.br |
| "bateria Roomba solução de problemas, limpar placa de contato" | bateriasrobot.com.br — loja especializada em bateria de robô aspirador (existência da loja é sinal de demanda de reposição) |
| "quando recarregar robô aspirador, bateria em 20-30%" | tudopra.casa |

**Achado do cluster:** existe pelo menos uma loja brasileira dedicada
somente a bateria de robô aspirador (bateriasrobot.com.br) — evidência
comercial direta de que reposição de bateria é uma consulta recorrente, mas
o corpo de conteúdo em torno dela é técnico-genérico (mAh, ciclo de carga),
não comparador de compatibilidade.

---

## 2. Eixo DIMENSIONAMENTO (Pa, m², autonomia, pelo)

### Cluster B1 — Pa (potência de sucção)

| Consulta | Procedência |
|---|---|
| "quantos Pa preciso robô aspirador pelo de cachorro" | busca web direta |
| "o que é Pa no robô aspirador" | Canaltech — artigo explicativo, ranking alto |
| "quantos Pa robô aspirador pelo de gato" | O Cafezinho, variação da mesma pergunta |
| "robô aspirador para pelo de cachorro" (top 10, sem número de Pa na intenção, mas o conteúdo devolve faixa) | TechInsider |
| "1500 Pa serve para pelo de cachorro" (piso liso, sujeira leve) | mundoconectado.com.br |
| "4000 Pa robô aspirador pet" (recomendação "grande diferencial" para pet) | fonte agregada (o mesmo artigo que resume 1500/4000) |
| "Xiaomi S40 vs H40 mesmo 10000 Pa qual compensa" | YouTube, comparação de modelo específico no mesmo patamar de Pa |

**Achado do cluster:** há divergência de faixa entre fontes brasileiras —
uma cita 1.500 Pa como suficiente para pelo leve em piso liso, outra cita
4.000 Pa como "diferencial" para pet em geral, uma terceira fala em 2.000–
3.000 Pa como "básico" e 4.000–6.000 como "pisos mistos e carpete curto".
Não há consenso numérico único — é candidato natural a ferramenta que
mostra a faixa com o critério de cada fonte, no mesmo padrão de honestidade
por atribuição que a Aquametria usa em C3 e C5 (nunca escolher um número
só, mostrar o desacordo).

### Cluster B2 — Cobertura por m²

| Consulta | Procedência |
|---|---|
| "robô aspirador para quantos m2" | busca web direta |
| "quantos m2 um robô aspirador limpa" | aprouter.com.br, artigo dedicado ao tema |
| "robô aspirador para 80 m2 apartamento pequeno" | busca web direta — vários guias de compra |
| "robô aspirador que passa pano em casa de 200 m2" | Canaltech |
| "robô entrada até 80 m2, intermediário 100-150 m2, premium 150-200+ m2" (faixas por categoria de produto) | mundoconectado.com.br |
| "Electrolux ERB44 cobre até 162 m2 por carga de 2 horas" (dado de fabricante citado por terceiro) | fonte agregada |
| "Mi Vacuum-Mop Essential 2500 mAh até 90 m2" | fonte agregada — fabricante declara mAh, terceiro converte em m² |

**Achado do cluster:** o "m² por carga" que circula é quase sempre número
solto do fabricante (ou de terceiro resumindo o fabricante), sem a conta
que liga bateria (mAh) → autonomia (min) → área coberta (m²) considerando
tipo de piso e obstáculo. Esse é o espaço da ferramenta (b) do PROMPT.md:
dimensionador de sucção e autonomia por área, tipo de piso e pelo — hoje
cada marca anuncia seu próprio número final sem mostrar a conta.

### Cluster B3 — Autonomia / bateria por área

| Consulta | Procedência |
|---|---|
| "robô aspirador autonomia bateria quantos m2 por carga" | busca web direta |
| "bateria 1000-1500 mAh = 45-90 min; 5200 mAh = 180 min" (relação capacidade × tempo) | fonte agregada de busca web |
| "apartamento 60-80 m2, mínimo aceitável 90 minutos de autonomia" | forumdacasa.com / agregado de fórum |
| "robô aspirador Ropo até 150 m2" | mercadolivre.com.br, blog de review |
| "robô aspirador Xiaomi 90 a 150 minutos por carga" | tudopra.casa |

**Achado do cluster:** mesma dispersão do cluster B2 — minutos de autonomia
e m² de cobertura aparecem sempre como dado fechado do fabricante, nunca
como fórmula que o visitante possa aplicar ao layout real da própria casa
(quantidade de cômodos, obstáculo, tipo de piso). Cauda longa de "para
[metragem] m² preciso de quanto" é grande e mal servida.

### Cluster B4 — Fórum e vídeo (guia de compra geral, cauda cruzada)

| Consulta | Procedência |
|---|---|
| "clube do hardware robô aspirador qual comprar apartamento" | fórum — forumdacasa.com, discussão de usuário real |
| "para apartamento 60 m2, 40-50 min de limpeza sem recarregar, autonomia até 90 min" | relato de usuário em fórum (agregado na busca) |
| "checar disponibilidade de peça de reposição (escova, filtro) antes de comprar" | recomendação explícita de usuário de fórum — compatibilidade e dimensionamento já aparecem juntos na cabeça de quem compra, mesmo sendo eixos diferentes na ferramenta |
| "qual robô aspirador comprar sem erro 2026" | YouTube, título de vídeo-guia |
| "melhores robôs aspiradores até R$2000, mapeamento e passa pano" | YouTube, título de vídeo-guia |
| "robôs aspiradores com base autolimpante para comprar" | YouTube, título de vídeo-guia |

**Achado do cluster:** a família "melhor robô aspirador" (que o PROMPT.md
manda não atacar de frente) domina o YouTube e os guias de compra
genéricos — confirma o diagnóstico da Bússola. Mas dentro dela aparece, de
forma recorrente e não atendida, o conselho de "cheque a peça de reposição
antes de comprar" — ponte natural da Robometria para a família de compra
sem competir com ela de frente.

---

## 3. Separação dos dois eixos — por que nunca se misturam numa ferramenta

- **Compatibilidade** responde "essa peça [código/tipo] serve no meu robô
  [marca+modelo]?" — leitura por catálogo de peça × modelo, banco de
  compatibilidade, sem cálculo numérico.
- **Dimensionamento** responde "que Pa/autonomia/robô serve na minha casa
  [m², tipo de piso, pelo de pet]?" — leitura por fórmula/faixa, com número
  calculado.
- As duas intenções aparecem juntas na cabeça do comprador (cluster B4), mas
  nenhuma fonte do corpus mistura as duas num só resultado — cada ferramenta
  deve resolver uma pergunta e linkar para a outra, nunca fundir os dois
  formulários.

---

## 4. O que este bloco não fecha (segue para o Bloco 2)

- Nenhuma fonte publica a fórmula "mAh → minutos → m²" com a conta explícita;
  todo número de autonomia/cobertura encontrado é declaração fechada do
  fabricante. Isso confirma o vácuo de conteúdo do eixo B e define o
  primeiro achado que o dimensionador (ferramenta b) deve publicar.
- Não foi possível medir volume de busca real (sem acesso a Google Keyword
  Planner, Ubersuggest ou similar nesta coleta). O Bloco 2 pode reabrir esse
  ponto se uma ferramenta de volume ficar disponível; até lá, a priorização
  de ferramenta usa recorrência entre fontes independentes como critério, não
  contagem de busca mensal.
- Lista de modelos e códigos de peça citados (Multilaser HO041/HO400/HO401/
  HO407/OB010, HO03/HO04, HO011/HO012; Positivo PRA500/PRA1000/PRA8000/
  PRA2000; Xiaomi Mop/Mop 2/Mop 2 Lite/S20/S40/H40; iRobot Roomba série s;
  Velds RALW-C; WAP W90/W100/W400; Electrolux ERB44) é ponto de partida para
  o banco de modelos do Bloco 3 — nenhum dado técnico (Pa, autonomia,
  voltagem) deve ser copiado deste arquivo para o banco sem reconfirmar na
  fonte primária (fabricante) e datar a verificação, por força da seção 10
  do `ARQUIPELAGO.md`.

**Próximo passo desbloqueado:** Bloco 2 — especificação das ferramentas
(`dados/especificacao-calculadoras.md` + `dados/constantes.json`), usando os
dois eixos acima como esqueleto: (a) localizador de peça compatível por
modelo, (b) dimensionador de sucção/autonomia por área, piso e pelo.
