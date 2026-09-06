# ESTADO da ilha Aquametria — cópia da memória para sessões SEM ferramenta de memória

Gerado em 06/09/2026 a partir de /areas/projeto-aquametria.md e /areas/aquametria-corpus-buscas.md.
Regra: se a sessão TEM ferramenta de memória, a memória manda e este arquivo é só espelho. Se NÃO tem, este arquivo é o estado — leia-o, trabalhe, e atualize-o junto com REGISTRO.md no fim.
Credenciais NÃO ficam neste arquivo (repositório pode virar público). A Application Password do WordPress está só na memória.

## Identidade
- Nicho: aquarismo — calculadoras de dimensionamento e banco de dados técnico. 1º colocado da Bússola.
- Marca: Aquametria. Site: https://aquametria.com.br (WordPress 7.1 pt-BR, HTTPS ok desde 06/09/2026). Admin: aquametria_gestor.
- Nome institucional: "-metria" (ciência de medir). O Raphael NÃO aparece: sem rosto, vídeo, fórum, tráfego pago ou link pago. Autoridade = metodologia + procedência + widget instalado em lojas.
- Visual: instrumento de precisão; símbolo = recipiente graduado com linha de enchimento e escala. Sem peixe, bolha ou rosto.
- Cores: tinta #0D1B22 · lâmina #0E7C8C · papel #F4F7F7 · superfície #FFFFFF · traço #DDE5E6 · legenda #5C7075 · alerta #B5762A. Tipografia: Chivo (display), IBM Plex Sans (texto), IBM Plex Mono (dado/unidade).

## Stack e infra (feito em 06/09/2026)
- HostGator Plano M, servidor br604, nginx na frente + mu-plugin "Caching" da HostGator (cache de página) → provavelmente sem plugin de cache extra.
- Plugin Code Snippets 3.10.2 ativo (REST /wp-json/code-snippets/v1/snippets). NUNCA WPCode. Sem construtor de página, sem plugin de SEO (sai por snippet), sem Wordfence.
- REST + Application Password funciona (header Authorization não é cortado). MAS o container da nuvem NÃO alcança o site por HTTP (proxy de saída bloqueia) — só GitHub. Por isso o desenho é PULL: a nuvem grava neste repositório; o snippet "Aquametria Sync" no site puxa manifest.json + arquivos do raw.githubusercontent.com e aplica só itens com publicar=true, conferindo sha256.
- Monetização: Shopee Afiliados aberto. Amazon Associados SÓ quando houver tráfego (regra 3 vendas/180 dias). Ticket típico R$380, comissão ~R$42.

## Blocos
- BLOCO 1 CONCLUÍDO (04/09): 480 consultas paramétricas em 15 clusters (abaixo).
- PRÓXIMO: BLOCO 2 — especificar 5 a 8 calculadoras: entradas, fórmula, faixas de saída, fonte de cada constante, produtos sugeridos. C1 (litragem) = estado compartilhado entre calculadoras; C10 (compatibilidade) = banco de fichas, não calculadora. Saída SEMPRE em faixa com critério e fonte, nunca número seco. Dosagem (C13) só vira calculadora se pedir marca/concentração como entrada.
- Depois: Bloco 3 (modelo do banco de produtos) → Bloco 4 (12-15 artigos-âncora) → Bloco 5 (lista de prospecção do widget).
- Entregas vão como arquivos em ilhas/aquametria/ (dados/, conteudo/, snippets/) + item no manifest.json (publicar=false até o desembarque).

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
