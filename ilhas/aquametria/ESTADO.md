# ESTADO da ilha Aquametria — cópia da memória para sessões SEM ferramenta de memória

Gerado em 06/09/2026 a partir de /areas/projeto-aquametria.md e /areas/aquametria-corpus-buscas.md.
Regra: se a sessão TEM ferramenta de memória, a memória manda e este arquivo é só espelho. Se NÃO tem, este arquivo é o estado — leia-o, trabalhe, e atualize-o junto com REGISTRO.md no fim.
Credenciais NÃO ficam neste arquivo (repositório pode virar público). A Application Password do WordPress está só na memória.

## Identidade
- Nicho: aquarismo — calculadoras de dimensionamento e banco de dados técnico. 1º colocado da Bússola.
- Marca: Aquametria. Site: https://aquametria.com.br (WordPress 7.1 pt-BR, HTTPS ok desde 06/09/2026). Admin: aquametria_gestor.
- Nome institucional: "-metria" (ciência de medir). O Raphael NÃO aparece: sem rosto, vídeo, fórum, tráfego pago ou link pago. Autoridade = metodologia + procedência + widget instalado em lojas.
- Visual: instrumento de precisão; símbolo = recipiente graduado com linha de enchimento e escala. Sem peixe, bolha ou rosto.
- Cores: tinta #0D1B22 · lâmina #0E7C8C · papel #F4F7F7 · superfície #FFFFFF · traço #DDE5E6 · legenda #5C7075 · alerta #B5762A. Tipografia: Chivo (display), IBM Plex Sans (texto), IBM Plex Mono (dado/unidade). Implementadas no snippet da casca desde 07/09/2026 — reaproveitar as variáveis CSS `--aqm-*` em vez de repetir hex.

## Stack e infra (feito em 06/09/2026)
- HostGator Plano M, servidor br604, nginx na frente + mu-plugin "Caching" da HostGator (cache de página) → provavelmente sem plugin de cache extra.
- Plugin Code Snippets 3.10.2 ativo (REST /wp-json/code-snippets/v1/snippets). NUNCA WPCode. Sem construtor de página, sem plugin de SEO (sai por snippet), sem Wordfence.
- REST + Application Password funciona (header Authorization não é cortado). MAS o container da nuvem NÃO alcança o site por HTTP (proxy de saída bloqueia) — só GitHub. Descoberto em 07/09: `WebSearch` FUNCIONA na sessão da nuvem, mas `WebFetch` é bloqueado por domínio (seachem.com devolveu EGRESS_BLOCKED) — então número de fabricante colhido só por busca entra com status `fabricante-via-busca`, a reconfirmar. Por isso o desenho é PULL: a nuvem grava neste repositório; o snippet "Aquametria Sync" no site puxa manifest.json + arquivos do raw.githubusercontent.com e aplica só itens com publicar=true, conferindo sha256.
- Monetização: Shopee Afiliados aberto. Amazon Associados SÓ quando houver tráfego (regra 3 vendas/180 dias). Ticket típico R$380, comissão ~R$42.

## Blocos
- BLOCO 1 CONCLUÍDO (04/09): 480 consultas paramétricas em 15 clusters (abaixo).
- BLOCO 2 CONCLUÍDO (07/09): 8 calculadoras especificadas em `dados/especificacao-calculadoras.md`, com o registro de constantes em `dados/constantes-calculadoras.json` (42 entradas, cada uma com fonte, data e status). As 8: C1 litragem (núcleo), C2 peso e carga no piso, C3 vazão/turnover, C5 aquecedor por delta térmico, C7 consumo e custo, C8 lotação, C12 mídia filtrante, C15 iluminação. Confirmado: C10 é banco de fichas, não calculadora; C14 foi absorvida pela C12; C13 (dosagem) NÃO entra no lote inicial (risco letal + só 2 dosagens verificadas no fabricante + o volume superestimado da C1 erra para overdose).
- Regras que o Bloco 2 fixou e que valem para os próximos: (a) toda constante tem id no JSON e status; constante `pendente` é PROIBIDA em fórmula publicada; (b) toda resposta é faixa com critério e constante em cada extremo, mais permalink citável; (c) quando as fontes divergem, a resposta publica a divergência e a atribuição, nunca a média; (d) onde falta fonte, a página explica por que não publica número — é isso que diferencia a Aquametria dos blogs.
- BLOCO 3 CONCLUÍDO (07/09, 2º disparo): modelo do banco de produtos em `dados/modelo-banco-produtos.md`, contrato formal em `dados/esquema-produtos.json`, dados em `dados/produtos-filtro.json` (5), `produtos-aquecedor.json` (4), `produtos-iluminacao.json` (4), `produtos-midia.json` (2) e `produtos-cotacoes.json` (0, vazio de propósito), com o validador `ferramentas/validar-produtos.py` (regras V1 a V14; hoje 15 produtos, 0 erros, 3 avisos). Decisões que valem para os próximos blocos: (a) procedência é por CAMPO, cada `fontes[]` diz quais campos sustenta; (b) variante de produto é registro próprio (Atman AT-3338 x AT-3338S muda 4 campos); (c) preço saiu do produto e virou série temporal com loja e data — nada entra sem data de leitura; (d) voltagem é requisito de SUGESTÃO (C3, C5, C15), não da ficha; (e) escada de 6 níveis de fonte, e em empate de nível o campo vira null; (f) derivado (turnover, W/L, lm/W, mL/L) nunca é gravado, só calculado.
- Achados do Bloco 3, com fonte nos registros: turnover implícito declarado pelos próprios fabricantes vai de 1,76 x/h (Eheim 2213) a 10,0 (Atman AT-3338S no piso da faixa) — os fabricantes divergem entre si por 5,7 vezes; eficiência de filtro de 34,3 a 166,7 L/h por W; a linha Roxin HT-1300/Q3 declara 0,67, 1,0 e 0,86 W/L nos três tamanhos (e deixa um vão sem modelo entre 200 e 250 L); 9 dos 13 equipamentos elétricos não declaram voltagem, então hoje a C5 e a C15 sugeririam ZERO produtos; 3 das 4 luminárias declaram lúmen (83 a 106 lm/W); Seachem Matrix (>700 m²/L) e Eheim SUBSTRAT pro (~450 m²/L) não publicam método de medição.
- BLOCO 3b CONCLUÍDO (07/09, 3º disparo): CASCA DO SITE em `snippets/aquametria-casca.php` — nome no Code Snippets "Aquametria Casca — identidade e estrutura do site", escopo global, ativo, `publicar: true` no manifest (revisão 3). Ele injeta paleta e tipografia sobre o tema ativo (inclusive redefinindo `--wp--preset--color--*` e `--wp--preset--font-family--*`, que é o que recolore um tema de blocos sem editá-lo), troca `core/site-title`/`core/site-logo` pelo logotipo SVG (recipiente graduado + wordmark Chivo) e `core/navigation` pelo menu Calculadoras · Metodologia · Sobre, cria as páginas `inicio`/`calculadoras`/`metodologia`/`sobre` com `show_on_front=page`, manda "Hello world!" e "Sample Page" para a LIXEIRA e imprime o rodapé com a tagline. Idempotente (2ª passada = 0 inserções), verificado em `php -l` e em teste de fumaça com WordPress simulado por stubs.
- **DESEMBARQUE APROVADO em 07/09/2026** (decisão do Raphael: "pode rodar sem a minha aprovação; se eu não gostar de algo peço pra alterar"). `desembarque.aprovado = true` no manifest. Calculadora, página-âncora, artigo e snippet de site saem com `publicar: true` sem consultar ninguém. SÓ continua com `publicar: false` esperando aprovação: conteúdo programático em escala (dezenas de páginas de cauda longa de uma vez).
- Duas regras novas que a casca criou: (a) **toda calculadora publicada precisa entrar no hub** — lista `aquametria_casca_calculadoras()` no snippet da casca, com `estado` em `em-construcao` ou `publicada`, mais o filtro `aquametria_calculadoras`; publicar calculadora sem virar o estado dela deixa a página órfã; (b) **conteúdo institucional mora em shortcode do snippet da casca** (`[aquametria_home]`, `[aquametria_calculadoras]`, `[aquametria_metodologia]`, `[aquametria_sobre]`), não em Markdown de `conteudo/` — assim editar o snippet edita a página, sem passar pelo editor do WordPress. `conteudo/` continua sendo o lugar dos artigos-âncora e das páginas de calculadora.
- PRÓXIMO: BLOCO 4 — **CONSTRUÇÃO E PUBLICAÇÃO DAS CALCULADORAS, uma por execução**, na ordem C1 litragem → C3 vazão/turnover → C5 aquecedor → C12 mídia → C15 iluminação → C2 peso e carga → C7 consumo → C8 lotação. Cada uma = snippet PHP com shortcode (formulário + cálculo + resposta em faixa com critério e fonte, JS e CSS inline, sem dependência externa) + página em `conteudo/` (Markdown com front matter e o shortcode no corpo) + itens no manifest com `publicar: true` e sha256 correto + o `estado` virado para `publicada` na casca (bumpando `AQUAMETRIA_CASCA_VERSAO`). A C1 é o estado compartilhado: grava em `localStorage`, chave `aquametria.aquario`, e as outras leem de lá. Depois das calculadoras vêm os artigos-âncora (12 a 15 textos; a tabela de turnover por fabricante e a série W/L da Roxin já são dois artigos com dado próprio) e então a lista de prospecção do widget.
- Depois do Bloco 4: Bloco 5 (lista de prospecção do widget) — a única alavanca de link do projeto.
- Entregas vão como arquivos em ilhas/aquametria/ (dados/, conteudo/, snippets/, ferramentas/) + item no manifest.json (publicar=false até o desembarque). Antes de commitar mudança no banco de produtos, rodar `python3 ferramentas/validar-produtos.py` na pasta da ilha.
- Regra de entrega fixada pelo Raphael em 07/09/2026: o bloco só conta como entregue quando está no `main`. Push direto em `main` funciona neste repositório (foi assim que o Bloco 2 entrou).
- Dívida técnica anotada: `dados/constantes-calculadoras.json` (Bloco 2) está sem acentuação; os arquivos do Bloco 3 já saem acentuados no texto de tela. Normalizar antes do desembarque.

## Regras de gravação de snippet (fase 4b do playbook — lições pagas na Real 21)
- Code Snippets moderno é app React; o editor do DOM não é fonte da verdade. Gravação sempre por REST: POST /wp-json/code-snippets/v1/snippets/{id}.
- Nunca confie na ausência de erro: releia o snippet depois de gravar, confira code.length e code_error === null. (DELETE de snippet por REST já devolveu 200 sem apagar.)
- ModSecurity mata gravação em SILÊNCIO: evitar a superglobal $_SERVER literal (usar add_query_arg(array())) e "User-agent:" escrito por extenso.
- Snippet começa com /** — o plugin põe o <?php. Todo PHP passa em php -l; JS embutido em node --check.
- Backup antes de editar: link action=clone (nasce INATIVO, sufixo [CLONE]). Dois ativos com as mesmas funções = fatal.
- Texto para tela sai acentuado (UTF-8). Nome de snippet descritivo e óbvio, nunca numerado.

## Portão (desembarque)
- Publicar em escala nunca é autônomo. A Fundação deixa pronto (publicar=false) e para. Página programática só existe com dado suficiente para ser útil sozinha.

---

# CORPUS DO BLOCO 1 — 480 consultas em 15 clusters (levantado em 04/09/2026)
Fontes: ~100 buscas no Google e ~70 páginas BR (Aquariofilia.Net, AquaPeixes, Brasil Reef, AquaOnline, Aquarismo Paulista, Aquário Vivo, Peixes e Aquarismo, Aquários Sobrinho, Escola de Aquário, Grupo Sarlo, Cobasi, Petz, fabricantes). [obs] = fraseado literal colhido; [var] = variação sobre padrão observado.

## Os 15 clusters (nº de consultas)
- C1 Litragem e volume útil (25) — "aquário de {C}x{L}x{A} quantos litros", inverso litros→medidas, desconto de substrato, bruta x real
- C2 Peso do aquário cheio e espessura do vidro (11) — "quanto pesa aquário de {N} litros", "laje/móvel aguenta", "espessura para {N} litros"
- C3 Vazão, turnover e dimensionamento de filtro (65) — "melhor filtro para aquário de {N} litros" é o padrão mais replicado da web BR; inverso "filtro de {X} l/h serve para quantos litros"; "{modelo} até quantos litros"
- C4 Circulação, sump e bomba de retorno (13) — nicho marinho
- C5 Potência do aquecedor e delta térmico (34) — "quantos watts para {N} litros", "{n} W por litro", ambiente {Ta}°C → alvo {Tw}°C, região/estação
- C6 Resfriamento (9) — cooler, chiller, verão
- C7 Consumo elétrico e custo mensal (11) — {W}w × {h}/dia × tarifa
- C8 Lotação, bioload e aquário mínimo (57) — "quantos {espécie} em {N} litros" é a maior cauda longa do nicho
- C9 Cardume mínimo e proporção macho/fêmea (7)
- C10 Compatibilidade par a par e comunitário (83) — "{espécie A} pode viver com {espécie B}", "parâmetros ideais para {espécie}"
- C11 Ciclagem: cronograma, dose de amônia, diagnóstico (30)
- C12 Mídia filtrante: volume, ordem, troca (14)
- C13 Dosagem: condicionador, sal, medicamento, KH, fertilizante (32)
- C14 TPA: percentual ↔ litros, frequência, tolerância térmica (6)
- C15 Iluminação, fotoperíodo, CO2, substrato, algas (83)

## Decisões de arquitetura que saíram do levantamento
- Calculadora devolve FAIXA com critério de cada extremo e a fonte. As fontes BR divergem em quase todo cluster (turnover 3x a 10x; lm/L 10-20 vs 20 para o mesmo "baixa"; sal grosso com 3 valores em 5 fontes). Mostrar a divergência É a metodologia.
- C1 é o núcleo: litragem alimenta 8 dos 15 clusters → ESTADO DE AQUÁRIO compartilhado, não 15 formulários isolados.
- C10 é BANCO: fichas de espécie normalizadas (temperatura, pH, GH, tamanho adulto, cardume mínimo, agressividade, zona de nado) + interseção de faixas. Melhor cauda longa e candidato natural a widget de loja.
- Modelos de equipamento aparecem nas buscas (Sunsun HW-303B, Atman AT-3338/HF-800, Seachem Tidal 35/55, Roxin Q3/Q5, Hopar J-226/3028, Boyu FEF-230, Eheim Classic 2213/Jager). O banco de produtos responde metade das consultas.

## Três vácuos de conteúdo confirmados
1. Quantidade de MÍDIA BIOLÓGICA por litragem/vazão (C12) — nenhuma fonte BR publica número.
2. Potência de aquecedor por DELTA TÉRMICO real (C5) — todos repetem "1 W/L"; fontes: 1 W/L genérico, 1,3 (eHow), 2 no Sul (Casa da Ada), 1-1,5 até 10°C de delta (ReefFlow). Calculadora que pede a mínima da cidade é inédita no BR.
3. DUREZA DA ÁGUA DA TORNEIRA por cidade brasileira (C13) — exige coleta própria.
- Menor: CICLO DE TRABALHO do aquecedor (C7) — fontes citam 8h/dia (Seu Pet Saudável) e 10h/dia (Grupo Sarlo), todos multiplicam por 24h.

## Procedência das constantes de DOSAGEM (C13 — risco letal)
- VERIFICADAS no fabricante: Mbreda Micronutri 1 ml/10 L brutos semanal (mbreda.com.br); Veromar Teste KH — amostra 5 mL, 1 gota = 0,5 °dKH, dKH = gotas ÷ 2.
- Rótulo transcrito em varejo (só com aviso "confira a embalagem"): Tetra AquaSafe 2 gotas/L (50/100 ml) e 5 ml/38 L (250 ml); Labcon Aqualife 1 gota/L a cada 48h; Seachem Stability 5 ml/40 L dia 1 e 5 ml/80 L dias 2-7.
- PENDENTES, não viram constante: Seachem Prime (5 ml/200 L, "até 5x"); sal grosso (3 valores em 5 fontes); banho de sal (10-15 g/L 20min vs 5 g/L 15min); azul de metileno (concentração nunca declarada); bicarbonato para KH; amoníaco para fishless; todo o catálogo Alcon/Labcon (site bloqueia leitura automatizada).
- Conflito grave: substrato "1 a 2 kg por litro" (guiadoaquarismo) vs 1 kg ≈ 1 L (peixeseaquarismo) — 100% de diferença.

## Constantes com fonte já colhidas (reconfirmar no Bloco 2)
- Turnover: 5-10x/h (Aquarismo Paulista, AquaOnline); 4-5x (my-best BR); 3-5x plantado (AquaPeixes). Sump ≥ 20% do volume (AquaOnline).
- Lotação: 1 cm/L (clássica, criticada); 1,5-4 L por cm; regra dos 10%; kinguio 100 L + 40 L por adicional (Aquarismo Paulista); oscar 100 L + 100 L por peixe.
- TPA: 10-30% (Escola de Aquário), 25-30% semanal (Aquário Vivo), máx 50%, água nova com ≤1°C de diferença (>2°C choque).
- Nitrato: >40 ppm troca urgente; ≤20 ppm sensíveis (Aquário Vivo); 5-10 ppm plantado (aquariosplantados).
- Iluminação lm/L baixa/média/alta: 20/30-40/60 (peixeseaquarismo); 10-20/20-40/>40 (aquarioturbinado); 15/30/60 (aquariosplantados). Fotoperíodo 6-8h low tech, 8-10h high tech, 5-6h contra alga, 4-6h ciclagem. Kelvin 6500-8000.
- CO2: 15-35 mg/L seguro, >30-35 tóxico; drop checker azul/verde/amarelo (CO2Art).
- Carvão ativado 1-2 g/L, trocar 15-30 dias; perlon semanal a quinzenal; cerâmica regenerar 6-12 meses (Aquarismo Paulista).
- Temperatura por espécie (Petz): betta 24-28, kinguio 18-24, guppy 23-26, disco 26-30, tetra 26-30, bandeira 24-28. Barbo sumatra pH 5,0-8,0 / 20-28°C; paulistinha 18-28°C (Aquarismo Paulista).
- Ordem das mídias no canister (AquaPeixes): cerâmica/argila → perlon → carvão → perlon → cerâmica → perlon.


---

# CONSTANTES VERIFICADAS NO BLOCO 2 (07/09/2026) — acréscimo ao corpus

Todas com id, fonte, url, data e status em `dados/constantes-calculadoras.json`.

## Achados de fabricante que nenhuma fonte BR do corpus confronta
- **Turnover:** Eheim classic 250 (2213) — 440 L/h nominais para até 250 L, coluna máx. 1,5 m, 8 W, cesto 3,5 L, volume de filtragem 3,0 L, Substrat Pro de fábrica. Isso dá **1,8 renovações/h**, contra as 5-10 x/h das regras de bolso BR: divergência de 3 a 6 vezes. Virou o eixo da C3.
- **Aquecedor:** Eheim Jäger — linha 25 a 300 W (9 tamanhos, 20 a 1000 L), ajuste 18-34 °C ±0,5 °C, e o modelo de **200 W declarado para 30 a 400 L** (faixa de 13x). Serve para escolher potência comercial, nunca para dimensionar.
- **Mídia (vácuo nº 1):** Seachem Matrix — "250 mL para 200 L" (1,25 mL/L) E "1 L para 100 gal" (2,6 mL/L), as duas leituras da própria copy do fabricante, conflitando por 2x; >~700 m²/L de área. Somado ao Eheim 2213 (3,0 L de filtragem para 250 L = **12 mL/L** de cesto), são as primeiras âncoras BR de mL de mídia por litro com fonte de fabricante. A página de seachem.com está bloqueada pelo egresso: reconfirmar por foto de rótulo no varejo BR.

## Novas constantes fora do aquarismo
- **Vidro float:** massa específica 2500 kg/m³ = **2,5 kg/m² por mm** de espessura (1 m² de 4 mm = 10 kg). Fonte: Cebrace / Saint-Gobain Sekurit, convergente em duas fontes do setor.
- **Carga de piso (ABNT NBR 6120:2019, via fontes secundárias — norma paga):** 1,5 kN/m² (~153 kgf/m²) dormitório/sala/cozinha/sanitário; 2,0 área de serviço; 3,0 corredor com acesso público. CRÍTICO: é carga distribuída de projeto, não autoriza carga concentrada de aquário. A C2 dá o número e manda consultar engenheiro — nunca "pode" ou "não pode".

## Recusas registradas (não usar em fórmula até ter fonte)
Coeficiente U do vidro do aquário · porosidade e densidade do substrato (as fontes conflitam 100 %) · espessura de vidro por litragem · "regra dos 10 %" de lotação (a fonte não define a base) · PPFD por litragem · tarifa de energia · mínima por cidade · as 7 dosagens pendentes do C13 (Prime, sal grosso, banho de sal, azul de metileno, bicarbonato, amoníaco, catálogo Alcon/Labcon).
