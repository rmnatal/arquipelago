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

A primeira leva do 3c foi entregue em 09/09/2026 e **fechou as lacunas (c) e (d)** da
ordem original: Positivo e Xiaomi já respondem na R1, e o Kit Performance **KPCEL01** deu
dono à vida útil de 6 meses do manual da Electrolux. **A ordem que resta, da maior para a
menor:**

(a) **`pa_declarado` — a maior urgência, e o alvo mudou.** Sem esse campo nenhum modelo
passa na elegibilidade da R2 e a lista de recomendados sai vazia; hoje são **2 de 19**
modelos publicáveis. **Não procure na Electrolux:** ficou medido que ela não publica Pa em
canal nenhum — declara *níveis* de sucção, e editorial não sustenta especificação de
aparelho. O campo tem que vir de **Xiaomi, Multi, WAP e Positivo**.
(b) **pares (minutos, m²) de marcas DIFERENTES.** São eles que tiram a constante
`taxa-cobertura-m2-por-min` de `pendente`. O banco tem 2 declarações e as duas são
Electrolux, discordando 23% entre si — o critério pede 5, de marcas diferentes. Mais um par
da Electrolux não resolve.
(c) **peça declarada para o PRA500**, que é a consulta-alvo da R1 e hoje não tem nenhuma:
as três peças da Positivo declaram PRA800 e PRA2000 sem citá-lo. Enquanto não houver
declaração, a resposta certa é "não encontramos" — nunca a peça do PRA800.
(d) **composição dos kits do ERB44 e do ERB30**, hoje no banco com a composição em aberto:
a R1 pode dizer QUE servem e ainda não O QUE vem dentro.

**4. FERRAMENTAS**, uma por execução, já nascendo com JSON-LD, tabela de exemplos pré-renderizada, resposta antes da explicação e procedência na frase. **Não deixe retrofit para depois** — foi o que custou dias na Aquametria.

**4e. VITRINE DE PRODUTO** dentro do resultado, desde a primeira ferramenta. O cartão diz a especificação que fez o produto entrar: "filtro HEPA H13 — compatível com o seu E10".

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta, na mesma execução.

**5b. MALHA DE PÁGINAS.** Camadas: (1) ficha de peça; (2) ficha de modelo de robô; (3) página de parâmetro ("robô para 80 m²", "robô acima de 4.000 Pa"); (4) cruzamentos (modelo × peça, marca × tipo de peça, parâmetro × modelo).

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de robô aspirador e assistência técnica com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Específico desta ilha
- **Compatibilidade de peça é o produto desta ilha.** Uma informação errada aqui destrói a confiança inteira. Toda afirmação de compatibilidade carrega fonte do fabricante e data na própria frase.
- Amazon paga 8% em Eletrodomésticos, mas a conta **não** deve ser aberta até haver tráfego: a regra das 3 vendas em 180 dias começa no cadastro. A Shopee já está aberta e serve todas as ilhas.
- **Enquanto não houver WordPress**, trabalhe os blocos 1, 2 e 3, que são de pesquisa e modelagem. Não fique bloqueada esperando infraestrutura — e não marque `bloqueada_por` por causa disso.
