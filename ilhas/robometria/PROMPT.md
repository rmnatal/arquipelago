# ILHA: ROBOMETRIA — robô aspirador

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha.

## Identidade
- Nicho: robô aspirador — **compatibilidade de peças e consumíveis** (qual filtro HEPA, escova lateral e mop servem em qual modelo) e **dimensionamento** (Pa de sucção por tipo de piso e pelo, autonomia por m²).
- Domínio: robometria.com.br, registrado em 09/09/2026. Segunda ilha do Arquipélago.
- Paleta: grafite `#16191D` (tinta) · varredura `#CC3311` (marca, **cor de sinal**: um uso por tela) · piso `#F2F1EF` (fundo) · superfície `#FFFFFF` · traço `#DFDCD6` · legenda `#6B6862` · alerta `#A26A00` (ressalva técnica — âmbar, nunca vermelho, porque vermelho é a marca).
- Tipografia: **Archivo** (títulos) · **IBM Plex Sans** (texto) · **IBM Plex Mono** (todo número, unidade e código de peça, com `tabular-nums`). Texto corrido nunca vai em Mono.
- Símbolo: **anel aberto + peça com lingueta que encaixa nele** — o assunto da ilha é o encaixe, então o símbolo é o encaixe. **Nunca um robô desenhado.** Anel: círculo de raio 15 em viewBox 48, traço 3, com corte de 50° à direita (`M37.59 17.66 A15 15 0 1 0 37.59 30.34`). Peça: `M41 16 h6 v16 h-6 v-4 h-3 v-8 h3 z`, preenchida na cor varredura — é o único vermelho da marca.
- Assinatura: `ROBO` em Archivo 700 + `METRIA` em Archivo 400, coladas, sem espaço. Nunca no mesmo peso, nunca separadas, nunca inclinada.
- Identidade aprovada pelo Raphael em 09/09/2026.

## O buraco que esta ilha existe para ocupar
A Bússola verificou em 07/09/2026: a busca **comercial** ("melhor robô aspirador") está tomada por fazendas (analisamelhor, melhores.com, melhorroboaspirador). A busca de **compatibilidade** está fragmentada entre páginas de peça de fabricante (Multilaser, iRobot, Positivo, Oster, Xiaomi) e **não existe nenhum comparador cross-marca**. É esse o eixo.

**Nunca ataque de frente a família "melhor robô aspirador 2026."** Ataque "qual filtro serve no meu robô X", "escova lateral compatível com Y", "quantos Pa preciso para pelo de cachorro", "qual robô para 80 m²".

## Memória a carregar
`/areas/projeto-robometria.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (rodada 003, que aprovou este nicho), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## FILA DE BLOCOS

**1. LEVANTAMENTO DE BUSCAS PARAMÉTRICAS.** Consultas reais do nicho no Brasil, agrupadas em clusters de ferramenta, com procedência marcada consulta a consulta (autocomplete, buscas relacionadas, fórum, YouTube). Grave em `dados/corpus-buscas.md`. Separe explicitamente o eixo de **compatibilidade** (peça × modelo) do de **dimensionamento** (Pa, m², autonomia). Não depende de site nem de domínio.

**2. ESPECIFICAÇÃO DAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`. As duas ferramentas âncora prováveis: (a) localizador de peça compatível por modelo; (b) dimensionador de sucção e autonomia por área, tipo de piso e pelo. Saída é sempre **faixa com critério e fonte**, nunca número seco.

**3. MODELO DO BANCO.** Entidades: **MODELO DE ROBÔ** (marca, linha, Pa, autonomia em minutos, tipo de navegação, voltagem, base de autoesvaziamento sim/não) · **PEÇA** (tipo, código do fabricante, modelos compatíveis, vida útil declarada) · **MARCA**. O campo `imagem` entra desde já (seção 6 do `ARQUIPELAGO.md`) — a Aquametria descobriu tarde que o banco não tinha e travou a vitrine.

**3b. CASCA DO SITE** — só depois que o WordPress existir. Snippet de identidade e estrutura: fontes, CSS da paleta, logo SVG inline, menu hambúrguer, favicon próprio, páginas início/ferramentas/metodologia/sobre, rodapé. Tudo conforme a seção 6 do `ARQUIPELAGO.md`, com a paleta e o símbolo desta ilha.

**3c. EXPANDIR O BANCO — não depende de site.** O modelo já existe e o
`ferramentas/validar-banco.py` já reprova o que estiver fora do contrato; o que falta é
cobertura. **A urgência não é número de itens** (a seção 14.3 do `ARQUIPELAGO.md`
descartou meta redonda): é faixa descoberta. Produto novo entra com `afiliado.url`
presente e vazio, e a execução reporta quantos itens esperam link.

A primeira leva do 3c (09/09/2026) fechou as lacunas (c) e (d) da ordem original. A
**segunda leva (09/09/2026, 23h16Z) fechou a lacuna (a)**: `pa_declarado` saiu de 2 para
**11 modelos publicáveis**, em 3 marcas, cobrindo de 1.400 a 10.000 Pa — a R2 deixa de
sair com lista vazia. **A ordem que resta, da maior para a menor:**

(a) **FAIXA DESCOBERTA E CONCENTRAÇÃO DE MARCA — a urgência agora, e ela só apareceu
porque a varredura foi feita.** A medição está em `cobertura_de_faixa_r2`, dentro de
`dados/modelos-robo.json`. Duas coisas: acima de **6.000 Pa** só existem 2 elegíveis (o
portão da seção 9 pede 3), e **toda faixa acima de 3.000 Pa é 100% Xiaomi** — inclusive a
faixa de pet, que é a que vende. Uma ilha que se vende como comparador **cross-marca** não
pode ter a faixa mais cara ocupada por uma marca só. Não se conserta afrouxando
elegibilidade: conserta-se achando Pa de **outra marca** nessa faixa.
(b) **MANUAIS EM PDF DA WAP — a melhor porta de entrada para o NÍVEL 2 da escada de
fontes.** A WAP publica um manual por modelo em `mais.conteudo.wap.ind.br`, com revisão e
data no nome do arquivo. Hoje o domínio devolve `EGRESS_BLOCKED`; no dia em que abrir,
esses PDFs sobem o banco inteiro da marca de nível 3 para nível 2 de uma vez e trazem o Pa
dos modelos que a loja declara só como "três modos de sucção". Toda a ilha está em nível 3
ou 4 — nenhuma fonte de nível 2 ainda.
(c) **pares (minutos, m²): a lacuna mudou de natureza e NÃO é mais coleta.** Ficou medido
que Xiaomi, WAP, Multi e Positivo **não declaram m² em canal nenhum** — só a Electrolux
declara. Não adianta procurar mais: o número não está publicado. A
`taxa-cobertura-m2-por-min` continua `pendente` e **proibida em fórmula**, e a recusa
virou conteúdo: a R2 mostra os minutos, diz que o fabricante não declara área e explica
por que não chuta.
(d) **peças da Xiaomi e da WAP com código**, que a R1 precisa e que a busca restrita ainda
não devolveu.

**4. FERRAMENTAS**, uma por execução, já nascendo com JSON-LD, tabela de exemplos pré-renderizada, resposta antes da explicação e procedência na frase. **Não deixe retrofit para depois** — foi o que custou dias na Aquametria.

**4e. VITRINE DE PRODUTO** dentro do resultado, desde a primeira ferramenta. O cartão diz a especificação que fez o produto entrar: "filtro HEPA H13 — compatível com o seu E10".

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta, na mesma execução.

**5b. MALHA DE PÁGINAS.** Camadas: (1) ficha de peça; (2) ficha de modelo de robô; (3) página de parâmetro ("robô para 80 m²", "robô acima de 4.000 Pa"); (4) cruzamentos (modelo × peça, marca × tipo de peça, parâmetro × modelo).

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de robô aspirador e assistência técnica com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Específico desta ilha
- **Compatibilidade de peça é o produto desta ilha.** Uma informação errada aqui destrói a confiança inteira. Toda afirmação de compatibilidade carrega fonte do fabricante e data na própria frase.
- Amazon paga 8% em Eletrodomésticos, mas a conta **não** deve ser aberta até haver tráfego: a regra das 3 vendas em 180 dias começa no cadastro. A Shopee já está aberta e serve todas as ilhas.
- **Enquanto não houver WordPress**, trabalhe os blocos 1, 2 e 3, que são de pesquisa e modelagem. Não fique bloqueada esperando infraestrutura — e não marque `bloqueada_por` por causa disso.
