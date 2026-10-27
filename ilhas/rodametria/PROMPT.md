# ILHA: RODAMETRIA — mobilidade elétrica

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha. **Nunca copie regra do `ARQUIPELAGO.md` para cá.**
O dossiê que aprovou esta ilha é `bussola/dossies/rodametria/DOSSIE.md`, e a ficha é `bussola/oportunidades/rodametria.md` — leia os dois na primeira execução e não repita o que eles já mediram. **A ficha manda sobre o dossiê** onde os dois divergirem: o dossiê foi escrito antes da regra só-Shopee (BUSSOLA.md 0.8 e 0.9) e trata o Mercado Livre como porta principal; a ficha, reaprovada às 14h29, põe o patinete só-Shopee no centro.

## Identidade
- Nicho: **acertar os três números antes de comprar um veículo elétrico** — potência e velocidade (precisa de CNH e placa?), bateria (quantos km faz?) e carga máxima (aguenta o meu peso?). O eixo paramétrico, não "patinete" como categoria comercial.
- Domínio: `rodametria.com.br`, **registrado e pago pelo Raphael em 27/10/2026**. Ilha nº 6 do Arquipélago.
- **Tokens, símbolo e assinatura moram em `DESIGN.md`**, nesta pasta, e é de lá que a casca renderiza (seção 22.6). Onde este arquivo e o `DESIGN.md` discordarem, vale o `DESIGN.md`. Resumo: tinta `#13212B` · verde `#0A6B4C` (um uso forte por tela fora da marca) · piso `#F6F8F7` · superfície `#FFFFFF` · traço `#D3DAD7` · legenda `#4A5A66` · alerta `#8F4A00`; Alfa Slab One só no nome da marca, Barlow Semi Condensed nos títulos, Barlow no texto, JetBrains Mono em todo número e unidade.
- Símbolo: **V9**, aprovado pelo Raphael em 27/10/2026 — patinete elétrico de frente com asas curvas e raios verdes. **É exceção aprovada por ele à regra "símbolo nunca é o objeto desenhado"**; o registro das recusas está no `DESIGN.md`. Assinatura horizontal **H1**.
- O site vende **mobilidade elétrica**, nunca só "patinete": a assinatura diz `MOBILIDADE ELÉTRICA`.

## O buraco que esta ilha existe para ocupar
Medido em 27/10/2026 no Chrome do Raphael (`bussola/dossies/rodametria/DOSSIE.md`, seção b): as seis cabeças de compra do nicho (`moto eletrica` 823 mil, `bicicleta eletrica` 673 mil, `scooter eletrica` 301 mil, `patinete eletrico` 246 mil, `bike eletrica` 201 mil, `motos eletricas para adultos` 201 mil buscas/mês) têm **SERP mista e não tomada**: só o Mercado Livre como varejo grande fixo, o resto é loja pequena de marca, YouTube, Instagram, OLX e Reddit; **sem carrossel de compras**, com visão geral de IA; **nenhuma fazenda da lista e nenhuma calculadora** de CNH, autonomia ou carga na primeira página. **O que isso decide:** a ilha entra pela ferramenta que ninguém tem (F1, CNH), e as páginas pelo nome do produto (seção 30) disputam as cabeças.

## Endpoints desta ilha
- Sync: `<preencher quando o WordPress existir>`
- Status: `<preencher quando o WordPress existir>`

---

## DESPACHO DO RAPHAEL — 27/10/2026 — ESTA ILHA NASCE AGORA

Aprovada por ele na conversa em 27/10/2026 ("vamos em frente", e "Já pode então executar, vai ser a próxima ilha"). **Domínio já registrado e pago** — o passo 1 da seção 11 está cumprido.

**A infraestrutura dos passos 2 a 8 da seção 11 (domínio adicional no cPanel, nameservers, Search Console, WordPress, SSL, plugins) é trabalho de NAVEGADOR e está com o Raphael e a conversa dele — não é sua.** Enquanto o site não responde, você trabalha o que não depende de site. **Não marque `bloqueada_por` por falta de site** (seção 11, passo 4).

**FOCO:** desde 27/10/2026 às 17h18 (Brasília) `foco.md` nomeia a RODAMETRIA, por decisão do Raphael — foco total e absoluto. Comece pelo bloco 1.

**A regra de dinheiro desta ilha (BUSSOLA.md 0.8 e 0.9):** a conta que aprovou é **só Shopee** — patinete elétrico adulto (ticket mediano R$ 2.329, comissão mediana 10%, medidos no painel em 27/10/2026) e peças/acessórios. **Scooter, moto e bicicleta elétrica entram com link do Mercado Livre como bônus, só para o que a Shopee não vende**, nunca como sustentação. Quando o mesmo produto existe nos dois, o link é o da Shopee (seção 7). Amazon fora de tudo.

## FILA DE BLOCOS

**Antes de montar a fila, leia a seção 14 do `ARQUIPELAGO.md`.** Os blocos 1, 2 e 3 não dependem de site.

**1. LEVANTAMENTO DE BUSCAS.** `dados/corpus-buscas.md`, com procedência consulta a consulta. Três eixos que não se misturam: (a) **CNH e placa** — potência, velocidade, acelerador × pedal assistido, a regra; (b) **autonomia** — tensão, amperagem, Wh, peso, relevo; (c) **carga e tamanho** — peso máximo, altura do guidão, aro. Mais o eixo de **produto pelo nome** (seção 30): as seis cabeças da tabela acima e as caudas medidas (`patinete eletrico adulto` 49,5 mil, `scooter eletrica 1000w` 33,1 mil, `moto eletrica 1000w` 14,8 mil). **Primeira tarefa de leitura:** abrir no Chrome a SERP das consultas-ponte (`bicicleta eletrica precisa de cnh`, `autonomia patinete eletrico`) — o dossiê deixou S_par não medida.

**2. ESPECIFICAÇÃO DAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`. Ordem obrigatória **F1, F2, F3**:
- **F1 — "Esse elétrico precisa de CNH?"** Entrada: potência nominal (W), velocidade máxima (km/h), acelerador ou só pedal assistido. Saída: categoria (bicicleta elétrica · autopropelido · ciclomotor) pela **Resolução Contran nº 996/2023** e os modelos do banco que cabem na categoria. **A constante central (1.000 W, 32 km/h e as dimensões do autopropelido) só vira `publicavel` depois de lida no texto oficial do gov.br, com data** — a resolução ganhou fase nova de vigência em 2026, e o dossiê a citou pelo noticiário.
- **F2 — "Quantos km ele faz de verdade?"** Entrada: V, Ah, peso de quem pilota, relevo. Saída: Wh e faixa de autonomia, ao lado da autonomia declarada. A fórmula de consumo por km fica aberta, com fonte.
- **F3 — "Aguenta o meu peso?"** Entrada: peso + carga. Saída: elegíveis pela carga máxima declarada, e os de fora com o motivo (seção 7).
Saída sempre faixa com critério e fonte.

**3. MODELO DO BANCO.** VEÍCULO (`categoria`, `potencia_nominal_w`, `potencia_pico_w`, `velocidade_max_kmh`, `acelerador`, `tensao_v`, `amperagem_ah`, `energia_wh`, `autonomia_declarada_km`, `carga_max_kg`, `aro`, `peso_kg`, preço com data, `afiliado.programa`, `afiliado.url_busca_produto`, `afiliado.url_produto`, `imagem`) · PEÇA (câmara, pneu, carregador por tensão, bateria por V/Ah, capacete, cadeado). Todo campo com `fonte_url`, `fonte_tipo`, `data_leitura`. **Potência nominal e pico são campos diferentes**: anúncio que só diz "1000W" no título não alimenta a F1 sem a ficha dizer qual dos dois é.

**3b. CASCA** — depois do WordPress. Molde FERRAMENTA da seção 32, a F1 é a home ("Esse patinete precisa de CNH?"). A home desenhada e aprovada no canvas de identidade está descrita no `DESIGN.md`.

**4. FERRAMENTAS**, uma por execução, com JSON-LD, tabela pré-renderizada, resposta antes da explicação, bloco de compra antes da procedência.

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta.

**5b. PÁGINAS PELO NOME DO PRODUTO** (seção 30) para as seis cabeças, e depois a malha.

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de mobilidade elétrica com site próprio, `publicar: false`.

## Específico desta ilha
- **O dado que é o produto da ilha é a categoria legal.** Errar "dispensa CNH" num veículo que é ciclomotor manda a pessoa para a rua sem habilitação. A F1 nunca afirma além do que a resolução diz, sempre cita a resolução e a data, e trata potência de pico como insuficiente para classificar.
- **Shopee:** `Sub_id 1` = `rodametria`; `Sub_id 2` = código da ferramenta. Na Shopee, scooter e moto elétrica aparecem com 0 vendas e preços incoerentes (R$ 1.255 a R$ 15.000 para o mesmo modelo) — não entram como recomendação.
- **Mercado Livre:** etiquetas `rodametriaf1`, `rodametriaf2`, `rodametriaf3`, ainda não criadas. Janela de atribuição do ML: 24 horas (Termos, item 1.6, lido em 27/10/2026) contra 7 dias da Shopee.
- **O tom:** `VOZ.md` manda na palavra, `DESIGN.md` manda na forma.
