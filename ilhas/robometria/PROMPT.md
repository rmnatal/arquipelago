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

## Endpoints desta ilha
- Sync: `https://robometria.com.br/?robometria_sync=lho9XAzCjAjHdXGHUEOQUMq1faJBN0vx&forcar=1`
- Status: `https://robometria.com.br/wp-json/robometria/v1/status`
- O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador (a copiar da Aquametria quando for preciso).
- Search Console: propriedade de domínio `sc-domain:robometria.com.br`, verificada. Sitemap `https://robometria.com.br/wp-sitemap.xml` enviado em 10/09/2026.
- **Quem aciona o Sync é a própria Fundação, por `curl`, ao fim de cada bloco publicável** (seção 4 do contrato; a nuvem alcança o site desde 10/09/2026). Commit sem Sync não está no ar.

## Memória a carregar
`/areas/projeto-robometria.md`, `/areas/fabrica-de-sites.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/areas/arquipelago-bussola.md` (rodada 003, que aprovou este nicho), `/topics/dev-conventions.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## DESPACHO DA SENTINELA — 10/09/2026 (medição pela nuvem)

**Isto tem prioridade sobre a fila.** Aplique antes de qualquer bloco, verifique pela seção 8 do contrato, registre no `REGISTRO.md` como "despacho de 10/09 — item N cumprido" e apague daqui o item cumprido no mesmo commit.

**O item 0 saiu daqui em 10/09/2026, cumprido** (a procedência era a única porta de compra da R1; virou a quinta decisão de desenho do bloco 4, abaixo). **Restou só a metade humana do item 1**, e ela não é da Fundação.

1. ~~**Os sitemaps respondem HTTP 404 com XML válido no corpo.**~~ **METADE DE CÓDIGO CUMPRIDA em 10/09/2026, 15h49Z** (casca 1.0.1, manifest revisão 9). A causa era a própria casca mandar "Hello world!" para a lixeira: sem nenhum post publicado, a consulta principal das rotas `index.php?sitemap=…` volta vazia e o `handle_404()` do núcleo carimba 404 antes de o XML sair. Consertado pelo filtro `pre_handle_404`, que só age em requisição de sitemap. **Medido no ar:** `wp-sitemap.xml` e `wp-sitemap-posts-page-1.xml` devolvem **200**, `/pagina-que-nao-existe-mesmo/` continua **404** (o conserto não vazou), e `wp-sitemap-posts-post-1.xml` segue 404 porque esta ilha não tem post nenhum — de propósito, e ele não está no índice.
   **FALTA A METADE HUMANA, e ela não é da Fundação:** reenviar o sitemap no Search Console (Sitemaps → enviar `https://robometria.com.br/wp-sitemap.xml`) para ele sair de "Não foi possível buscar". Exige o navegador do Raphael ou credencial de conta de serviço que este ambiente ainda não tem. **Enquanto isso não acontecer, nenhuma leva de malha (bloco 5b) nasce** — a rampa da seção 14 é inexecutável sem medição.

## FILA DE BLOCOS

**1. LEVANTAMENTO DE BUSCAS PARAMÉTRICAS.** Consultas reais do nicho no Brasil, agrupadas em clusters de ferramenta, com procedência marcada consulta a consulta (autocomplete, buscas relacionadas, fórum, YouTube). Grave em `dados/corpus-buscas.md`. Separe explicitamente o eixo de **compatibilidade** (peça × modelo) do de **dimensionamento** (Pa, m², autonomia). Não depende de site nem de domínio.

**2. ESPECIFICAÇÃO DAS FERRAMENTAS.** `dados/especificacao-calculadoras.md` + `dados/constantes.json`. As duas ferramentas âncora prováveis: (a) localizador de peça compatível por modelo; (b) dimensionador de sucção e autonomia por área, tipo de piso e pelo. Saída é sempre **faixa com critério e fonte**, nunca número seco.

**3. MODELO DO BANCO.** Entidades: **MODELO DE ROBÔ** (marca, linha, Pa, autonomia em minutos, tipo de navegação, voltagem, base de autoesvaziamento sim/não) · **PEÇA** (tipo, código do fabricante, modelos compatíveis, vida útil declarada) · **MARCA**. O campo `imagem` entra desde já (seção 6 do `ARQUIPELAGO.md`) — a Aquametria descobriu tarde que o banco não tinha e travou a vitrine.

**3b. CASCA DO SITE — ENTREGUE em 10/09/2026** (`snippets/robometria-casca.php` v1.0.0,
manifest na revisão 7). Identidade sobre o tema ativo, logo SVG do encaixe, menu hambúrguer
acessível, favicon próprio, JSON-LD Organization + WebSite, e **cinco** páginas — início,
ferramentas, metodologia, sobre e divulgação de afiliados (esta última nasceu junto porque
o aviso de comissão precisa estar publicado antes do primeiro link, não depois).

**3b ENTREGUE E NO AR em 10/09/2026, 14h11 UTC.** Sync acionado pela nuvem: `/status` responde
**revisão 7**, snippet `robometria-casca` aplicado (#6), a home serve o título da ilha, o sitemap
de páginas lista início, ferramentas, metodologia, sobre e divulgação-de-afiliados, e o sitemap
de posts está vazio ("Hello world" saiu). Próximo bloco da fila é o 3c.

**Antes de mexer na casca, rode `php ferramentas/teste-casca.php .`** — 59 medições, sem
site e sem rede, e é a única verificação da seção 8 que esta ilha consegue executar sozinha
(a nuvem não alcança robometria.com.br). Ele confere o que a seção 8 pede e mais a
identidade: paleta fechada, nenhum gradiente, a varredura ausente do corpo porque é cor de
sinal, e **cada número da tela conferido contra o banco commitado** — quem expandir o banco
e não atualizar o instantâneo da casca vê o teste reprovar em vez de o site publicar número
que o repositório não sustenta. Na primeira rodada ele já pegou o nome da superglobal de
servidor escrito dentro de um *comentário*, que o ModSecurity casa do mesmo jeito e faria a
gravação falhar em silêncio no wp-admin.

**3c. EXPANDIR O BANCO — não depende de site.** O modelo já existe e o
`ferramentas/validar-banco.py` já reprova o que estiver fora do contrato; o que falta é
cobertura. **A urgência não é número de itens** (a seção 14.3 do `ARQUIPELAGO.md`
descartou meta redonda): é faixa descoberta. Produto novo entra com `afiliado.url`
presente e vazio, e a execução reporta quantos itens esperam link.

A primeira leva do 3c (09/09/2026) fechou as lacunas (c) e (d) da ordem original. A
**segunda leva (09/09/2026, 23h16Z) fechou a lacuna do `pa_declarado`**: de 2 para **11
modelos publicáveis**, em 3 marcas, de 1.400 a 10.000 Pa — a R2 deixou de sair vazia.

A **terceira leva (10/09/2026, 11h17Z) varreu a entrada da R1**, que nunca tinha sido
varrida, e o resultado **reordenou esta lista**. A medição está em
`dados/cobertura-r1.json` e se refaz sozinha com
`python3 ferramentas/cobertura-r1.py --gravar`. **A ordem que vale agora, da maior para a
menor:**

(a) **PEÇAS COM CÓDIGO DA XIAOMI E DA WAP — a urgência número 1, e ela só apareceu no
cruzamento das duas varreduras.** Esta linha estava em ÚLTIMO lugar até 10/09/2026.
Medido: das 28 entradas publicáveis, só **3** são atendidas pelas DUAS ferramentas da
ilha. A R2 atende 8 modelos (Xiaomi, WAP, PRA500) em que a R1 sai **vazia**; a R1 atende
12 (Electrolux, Multi) em que a R2 sai vazia. **O funil está partido na emenda:** a ilha
ganha a visita pela R2 ("quantos Pa para pelo de cachorro"), a pessoa compra, volta meses
depois procurando o filtro daquele robô — que é a consulta de maior intenção de compra do
nicho e a razão de a R1 existir — e recebe "não localizamos declaração do fabricante".
Este é também o único lado **coletável** da emenda: o lado simétrico (Pa da Electrolux e
da Multi) já foi medido como inexistente no mercado brasileiro.
(b) **FAIXA DESCOBERTA E CONCENTRAÇÃO DE MARCA na R2.** Medição em
`cobertura_de_faixa_r2`, dentro de `dados/modelos-robo.json`: acima de **6.000 Pa** só
existem 2 elegíveis (o portão da seção 9 pede 3), e **toda faixa acima de 3.000 Pa é 100%
Xiaomi** — inclusive a de pet, que é a que vende. Não se conserta afrouxando
elegibilidade: conserta-se achando Pa de **outra marca** nessa faixa. Continua sendo
trabalho de verdade; caiu para segundo porque (a) rende nas duas ferramentas de uma vez e
(b) só rende numa.
(c) **MANUAIS EM PDF DA WAP — a melhor porta de entrada para o NÍVEL 2 da escada de
fontes.** A WAP publica um manual por modelo em `mais.conteudo.wap.ind.br`, com revisão e
data no nome do arquivo. Hoje o domínio devolve `EGRESS_BLOCKED`; no dia em que abrir,
esses PDFs sobem o banco inteiro da marca de nível 3 para nível 2 de uma vez, trazem o Pa
dos modelos que a loja declara só como "três modos de sucção" **e**, pela varredura da
R1, são a chance de tirar W400, W1000 e W310 do vazio duplo. Toda a ilha está em nível 3
ou 4 — nenhuma fonte de nível 2 ainda.
(d) **pares (minutos, m²): a lacuna mudou de natureza e NÃO é mais coleta.** Ficou medido
que Xiaomi, WAP, Multi e Positivo **não declaram m² em canal nenhum** — só a Electrolux
declara. Não adianta procurar mais: o número não está publicado. A
`taxa-cobertura-m2-por-min` continua `pendente` e **proibida em fórmula**, e a recusa
virou conteúdo: a R2 mostra os minutos, diz que o fabricante não declara área e explica
por que não chuta.

**ANTES de colher qualquer coisa para o 3c, rode `python3 ferramentas/cobertura-r1.py` e
`ferramentas/validar-banco.py`.** As duas varreduras são o que separa "acrescentei um
item" de "tirei uma entrada do vazio" — e foi contando itens, em vez de varrer, que a
lacuna da R1 ficou escondida atrás de "33 pares declarados".

**4. FERRAMENTAS**, uma por execução, já nascendo com JSON-LD, tabela de exemplos pré-renderizada, resposta antes da explicação e procedência na frase. **Não deixe retrofit para depois** — foi o que custou dias na Aquametria.

**4 e 4e — A R1 ESTÁ NO AR desde 10/09/2026** (`snippets/robometria-r1.php`,
hoje **v1.1.0**, manifest revisão 10, `/status` conferido). Endereço:
`https://robometria.com.br/qual-peca-serve-no-meu-robo-aspirador/`. **A próxima
ferramenta é a R2**, e ela nasce com as mesmas **cinco** decisões, que deixaram de ser
opinião e viraram o jeito desta ilha:

1. **A resposta é servida pelo SERVIDOR.** Formulário GET para a própria página, resposta
   montada em PHP. Sem JavaScript a ferramenta funciona por completo, e cada consulta tem
   a resposta inteira no HTML servido. Não repita o desenho de calculadora que só calcula
   no navegador: para um modelo de linguagem, aquilo é um formulário vazio.
2. **A regra mora na implementação de referência, e o PHP não a reescreve.**
   `ferramentas/gerar-r1.py` importa `cobertura-r1.py`, deriva os fatos para
   `dados/r1-respostas.json` (que o Sync leva para uma option) e o snippet só escreve a
   frase, acentuada. `ferramentas/teste-r1.php` compara **as 188 frases** das duas
   implementações ignorando acento: elas batem por construção, não por sorte. **A R2 tem
   que ganhar a mesma dupla**, e a referência dela ainda não existe.
3. **O caso-âncora é escolhido por regra, nunca a dedo**, e sai no HTML sem clique nenhum
   — é ele que um modelo de linguagem lê como resposta.
4. **Consulta não vira URL indexável:** `?modelo=…` sai com `noindex,follow` e canônica
   para a página limpa (seção 14.1). Domínio novo não tem orçamento de rastreamento para
   centenas de combinações.
5. **A PORTA DE COMPRA VEM ANTES DA PROVA DE PROCEDÊNCIA, e existe antes do link**
   (v1.1.0, 10/09/2026 — item 0 do despacho, hoje cumprido). A R1 estreou com um único
   link clicável por peça, e ele ia para a loja do fabricante: a página ficou impecável
   de procedência e perfeita para a Electrolux. Agora o bloco "Onde comprar estas peças"
   vem antes, com o aviso de comissão dentro dele; a procedência é link de texto "fonte"
   com `rel="nofollow noopener"`, nunca um botão e sem fundo no CSS; e o bloco **nasce
   mesmo sem link**, reservando o lugar com "Link de loja em breve" — esconder o bloco
   enquanto o cano de links enche devolveria a procedência ao papel de única porta
   clicável, que é exatamente o defeito. Quando não há o que recomendar, o bloco não
   lista **e a página diz por quê**. `teste-r1.php` mede os cinco pontos (seção 13 dele),
   e a R2 nasce com isso, não com retrofit.

**E o achado que só apareceu LENDO a resposta como um leitor lê:** a página se
contradizia na mesma tela, dizendo "a Electrolux declara o filtro X compatível com o
ERB60" e, na frase seguinte, "a Electrolux não vende o filtro avulso para este modelo".
"Não vende avulso" é afirmação sobre o catálogo inteiro do modelo — frase que só o
resultado inteiro sustenta não pode ser escrita olhando uma peça de cada vez. **A R2 tem
frases da mesma família** ("nenhum modelo atende a sua metragem"): escreva-as depois de
montar o resultado inteiro, não durante.

**5. ARTIGOS-ÂNCORA** pareados com cada ferramenta, na mesma execução.

**O DA R1 ESTÁ NO AR desde 10/09/2026** (`snippets/robometria-a1.php` v1.0.0, manifest
revisão 11): `https://robometria.com.br/filtro-universal-de-robo-aspirador/`. Ele fechou a
malha da R1 nos dois sentidos — duas listagens (home e hub), três irmãs, e a R1 v1.1.1
apontando de volta. **O artigo da R2 nasce junto com a R2, na mesma execução**, e herda as
três decisões que este bloco fixou:

1. **A tese do artigo é derivada, nunca digitada.** `ferramentas/gerar-a1.py` deriva os
   números do banco para `dados/a1-fatos.json`, e a frase de abertura tem DUAS formas,
   escolhidas pela contagem. Um artigo cuja tese é um número e que traz esse número dentro
   do HTML passa a mentir em silêncio no dia em que o banco cresce — e "em silêncio" é o
   ponto: ninguém relê artigo publicado.
2. **A DESCRIÇÃO DO JSON-LD E A RESPOSTA DO FAQPage SÃO PARTE DA TESE, não embrulho.** O
   defeito só apareceu ao plantar uma peça multimarca numa cópia do banco: a página visível
   se corrigia e o JSON-LD continuava afirmando o que deixara de valer. Numa ilha cuja seção
   5 diz que ser recomendado pela IA vale tanto quanto ranquear, **contradizer-se no canal
   que a IA lê é pior do que na tela**. Todo artigo novo deriva os três lugares juntos.
3. **O artigo não repete a ferramenta.** Sem formulário: a consulta é da ferramenta, e duas
   páginas respondendo a mesma coisa competem entre si no índice (seção 14.4).

**A PROVA DE QUE UMA TRAVA REPROVA É PARTE DO BLOCO.** As travas novas do `teste-a1.php`
foram medidas quebrando o banco de propósito numa cópia — números adulterados nos fatos e
uma peça multimarca plantada. Trava que nunca foi vista reprovando é trava não medida.

**5b. MALHA DE PÁGINAS.** Camadas: (1) ficha de peça; (2) ficha de modelo de robô; (3) página de parâmetro ("robô para 80 m²", "robô acima de 4.000 Pa"); (4) cruzamentos (modelo × peça, marca × tipo de peça, parâmetro × modelo).

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas brasileiras de robô aspirador e assistência técnica com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Específico desta ilha
- **Compatibilidade de peça é o produto desta ilha.** Uma informação errada aqui destrói a confiança inteira. Toda afirmação de compatibilidade carrega fonte do fabricante e data na própria frase.
- Amazon paga 8% em Eletrodomésticos, mas a conta **não** deve ser aberta até haver tráfego: a regra das 3 vendas em 180 dias começa no cadastro. A Shopee já está aberta e serve todas as ilhas.
- **WordPress, casca, a primeira ferramenta e o primeiro artigo estão no ar desde 10/09/2026** (manifest revisão 11). Os blocos 1, 2, 3, 3b, 4, 4e e 5 estão feitos. **O próximo é o 3c alvo (a)** — peça com código da Xiaomi e da WAP, o único lado coletável da emenda entre as duas ferramentas —, **se a rede alcançar o fabricante**; se não alcançar, o próximo é a **R2**, que já tem as cinco decisões de desenho fixadas pela R1 e ainda não tem implementação de referência.
- **Antes de mexer em qualquer snippet, rode os TRÊS testes de bancada:** `php ferramentas/teste-casca.php .` (64 medições), `php ferramentas/teste-r1.php .` (90) e `php ferramentas/teste-a1.php .` (53). Eles são a única verificação da seção 8 que roda sem depender do site. O segundo compara as 188 frases publicadas contra a implementação de referência; o terceiro **recalcula a tese do artigo em PHP, direto do banco, sem olhar para o que o gerador em Python escreveu** — duas contas independentes que batem são medição, uma conta sozinha é o que o autor achou.
- **A PORTA DE COMPRA TEM UM DONO SÓ, e ele é a casca.** `robometria_casca_porta_de_compra`, `robometria_casca_rotulo_da_loja`, `robometria_casca_fonte_link` e `robometria_casca_css_vitrine` valem para toda página desta ilha que recomenda item; a R1 delega para elas. Página nova que recomenda produto **chama estas funções**, nunca escreve as suas. Os pesos visuais do botão de compra e do link de procedência são regra do Arquipélago (seção 7), não estilo local: com uma cópia por página, bastaria alguém ajustar uma delas para a ilha voltar — numa página só, e sem ninguém notar — ao defeito de 10/09/2026.
- **Página nova entra no catálogo da casca pelo FILTRO dela**, `robometria_ferramentas` para ferramenta e `robometria_artigos` para artigo. A casca nunca ganha uma cópia da página dentro; é assim que a home e o hub listam qualquer coisa nova sem serem editados de novo, e é o que garante as duas listagens que a seção 9 exige.
- **O BANCO ESTÁ EM ASCII, E AGORA ISSO APARECE NA TELA.** Enquanto o banco só alimentava medição, acento faltando em `nome_na_fonte`, `publicador` e `o_que_muda` não custava nada; com a R1 no ar, esse texto é citado dentro da resposta publicada ("Aspirador Robo", "identificada como 'Versao A'"). O que a ilha escreve sai acentuado; o que ela cita sai como o banco tem — e o banco tem errado. É trabalho de dados, e o lugar barato de fazê-lo é junto da próxima leva de coleta, quando esses registros já forem ser tocados.
- **O KIT DECLARADO NÃO TEM PORTA DE COMPRA, E ISSO SE DESTRAVA POR DADO.** Na
  consulta ERB30 + filtro, a Electrolux declara um Kit Performance compatível com
  o modelo e a página não oferece compra dele: a composição do kit não foi
  transcrita, então a página não sabe se ele contém filtro, e vender kit debaixo
  de "qual filtro serve no meu robô" seria recomendar em primeiro lugar um
  produto que a própria página diz não saber se serve (seção 7). **Não afrouxe a
  regra: transcreva a composição dos kits na próxima leva do 3c** — o dado abre
  a porta de compra sozinho, e hoje são os kits que concentram o que a Electrolux
  declara para os modelos mais novos.
- **UMA FONTE ESTÁ NO NÍVEL 2 E A ESCADA DIZ QUE O NÍVEL 2 NÃO EXISTE.** `pecas.json/electrolux-kpcel01/f-manual` declara `nivel: 2`, e a escada da página de metodologia define nível 2 como "manual, lâmina ou página oficial **LIDA direto**" e publica "temos hoje: —". Aquele manual veio por busca restrita a `manuals.plus`, um terceiro, sem leitura direta. Uma das duas afirmações está errada. **A R1 não publica número de nível de fonte** de propósito, para a contradição não ir para a tela antes de alguém decidir — e a decisão é de regra: *manual do fabricante hospedado por terceiro, colhido por busca, é nível 2 ou não?*
