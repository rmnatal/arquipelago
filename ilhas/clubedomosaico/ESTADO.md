---
ilha: clubedomosaico
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 12
primeira_indexacao: desconhecida
ultima_execucao: 2026-09-14T21:17Z
executando_desde: 2026-09-14T23:19Z
bloco_atual: |
  A PAGINA DO PICASSIETE NASCE E O DESPACHO DO RAPHAEL DE 14/09 FECHA (casca 1.11.0, tecnicas 1.0.0, manifest revisao 34, /status conferido na 34 em UM disparo com 12 aplicados). UMA URL nova: /como-fazer/o-que-e-mosaico-picassiete/, a primeira filha da Escola. Nenhuma peca entrou ou saiu. Dois blocos numa execucao, pelo mutirao da secao 13, o primeiro verificado inteiro antes do segundo.

  A ESCOLHA DA ILHA: SEGUNDA TENTADA. Os cinco ESTADO.md parseiam e os cinco tinham executando_desde null, que pela 1.1 ja significa que nao ha bloco da Fundacao vivo. Pela 18.1, TRES ilhas tinham despacho aberto do Raphael de 14/09 (clubedomosaico, ohmetria e jornadafly), empate de data, e a rotacao da secao 1 desempatou: clubedomosaico com ultima_execucao 18h45Z, a mais antiga das tres. O primeiro push de reserva foi RECUSADO, mas NAO porque alguem pegou esta ilha: outra execucao reservou a aquametria as 21h18Z e o main andou. Voltei ao passo 2 sem force push e a reserva foi aceita. Nenhum branch claude e nenhum PR aberto para mesclar. Rede pela 20.2: home 200 e /status na revisao 33, igual a do manifest, em TRES passadas.

  BLOCO A — O PORTAO DA FAMILIA DAS TECNICAS CONTAVA A CATEGORIA QUE A PAGINA NAO RECOMENDA, e por isso lia ZERO com cinco itens atras dele. Ele contava so TESSELA: quantos produtos da categoria pastilha o banco tem com o tipo que a tecnica cita. As duas unicas tecnicas com material declarado apontam para caco de azulejo e caco de louca, e caco de prato NAO TEM FABRICANTE — o portao leria zero para sempre, por mais coleta que acontecesse. So que a pagina de uma tecnica nao recomenda caquinho: ela responde COM O QUE COLAR o caquinho, que e o eixo desta ilha e e produto com fabricante, declaracao datada e link.
  A conta passou a ser as pastilhas da tessela declarada MAIS as colas que o fabricante declara elegiveis para ela, medida pela regua da F2 que ja existia no validar-banco. Trencadis 5, Picassiete 5, e direto, indireto e bizantino seguem em ZERO, cada um com o motivo escrito — regua que abre tudo nao mede nada.
  AS DUAS METADES DA MESMA SECAO DISCORDAVAM, E QUEM DECIDIA ERA A QUE TINHA NUMERO: o item 6 da ARVORE 4b ja dizia, desde as 18h45Z, que o caminho era ligar a tecnica a cola; o item 3 da MESMA secao contava caco. E a familia da V24 da aquametria, consertada poucas horas antes no mesmo dia — regua amarrada a um campo que o caso certo nunca preenche reprova o mundo inteiro e parece rigor.
  NASCEU tecnica-x-material.py, que deriva o arquivo IMPORTANDO a conta do validar-banco em vez de reescreve-la, e mutacoes-tecnica-x-material.py, que afirma o NUMERO e nao o veredito — porque a mutacao mais perigosa desta familia e a que INFLA a conta e fica verde por ter aberto. 9 mutacoes, 9 certas. UMA EXPECTATIVA MINHA ESTAVA ERRADA e a bancada corrigiu: previ 5 colas e 2 estados onde eram 4 e 6. Ficou registrada no arquivo, porque e o proprio argumento a favor de afirmar numero em vez de veredito.
  OS OUTROS DOIS PORTOES TAMBEM DECIDIAM ERRADO. A 16.5 nao se aplica a uma pagina que nasce filha DIRETA de /como-fazer/. E 'nenhum numero autoriza leva nova' e o OPOSTO do que a secao 21.1 manda para ilha abaixo do piso — esta tem 11 URLs e piso abaixo escrito no cabecalho. Virou a 21.8 do contrato: e a SEGUNDA ilha a ler a 21 ao contrario, depois da aquametria em 12/09, e a armadilha e que 'a serie nao autoriza' e 'a serie proibe' nao sao a mesma frase.

  BLOCO B — A PAGINA. /como-fazer/o-que-e-mosaico-picassiete/, nivel 3 com mae de nivel 1 direto, o mesmo estado de transicao das duas ferramentas. NAO e /tecnicas/Picassiete/ como o despacho pediu, e a 16.1 proibe pagina solta na raiz desde 11/09.
  ELA NAO DECIDE NADA: quem escolhe a cola e cdm_f2_celula_cola, chamada para o caquinho de louca. 45 celulas de 9 superficies por 5 lugares, servidas no HTML e recalculadas a cada requisicao, sem uma segunda copia da decisao. Texto, definicao e fontes saem do banco, que passou a publicar.
  A PRESTACAO DE CONTAS FECHA COM O BANCO: das 7 colas, 5 entram na vitrine e as 2 que ficam de fora sao nomeadas com TODAS as causas que o calculo separou. Isso foi conserto dentro do proprio bloco: a primeira versao escrevia so o balde maior, e o Durepoxi cai por silencio em 25 celulas E entra com ressalva em 20 — dizer so o silencio seria afirmar algo falso em 20 delas.
  E ELA SE RECUSA A RESPONDER O REJUNTE, com a causa medida: ele se decide pela largura da junta em milimetro e nenhuma fonte colhida sobre Picassiete declara essa folga. Onze das 45 celulas dizem, com todas as letras, que nao ha cola que o fabricante sustente.
  A CASCA SUBIU PARA 1.11.0 POR UM MOTIVO DE MALHA, nao de vitrine: com um link so, vindo da mae, a pagina nasceria ORFA pela 16.4-f e o portao pegou isso. A Escola e a home passaram a listar as tecnicas em bloco proprio, separado dos tutoriais — tecnica e 'o que e isso', tutorial e 'como se faz', e junta-las faria a Escola prometer um passo a passo que a pagina nao entrega.
  O BANCO DE TECNICAS GANHOU ACENTOS, e isso so virou defeito no dia em que uma PAGINA passou a servi-lo: 'louca', 'xicara', 'monumento historico'. Vieram junto as aspas tipograficas, porque aspa reta vira entidade e o filtro do WordPress a escapa de novo, servindo a entidade crua na tela. A troca tem prova: reduzido a sem-diacritico, o arquivo e identico fora de 10 frases do campo leitura, reescritas de proposito e declaradas uma a uma.

  VERIFICACAO, 0 falha. BANCADA: teste-tecnicas 52 afirmacoes com o esperado das 45 celulas vindo de cobertura.json (a regua em Python — duas metades independentes, em linguagens diferentes), teste-casca 549, teste-f2 111, teste-f1, teste-loja, teste-atelie, teste-leads, teste-prestacao-rejunte, validar-banco, validar-pastilhas, cobertura --conferir, tecnica-x-material --conferir, php -l limpo nos sete snippets. MUTACOES: 9 da pagina, 9 da conta e as 14 do banco de tecnicas, todas decididas certo. NO AR: conferir-tecnica-no-ar.py, 23 afirmacoes sobre o HTML SERVIDO, incluindo o endereco canonico comparado com o mesmo endereco sem cache nos marcadores deste bloco — a trava do cache do hospedeiro, que o /status nao enxerga.
  UMA SECAO DO TESTE FOI APAGADA PELO PROPRIO AUTOR: a primeira versao do teste-tecnicas tinha uma secao 8 que imprimia ok sem medir nada. Ela virou a nona mutacao da pagina, que produz o mundo sem banco e exige a pagina HONESTA — dizendo que nao mediu e sem servir a grade.
ultima_ronda: 2026-09-12T14:43Z
bloqueada_por: null
---

# Estado da ilha CLUBE DO MOSAICO

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: clubedomosaico.com.br, registrado no registro.br em 10/09/2026.
- Hospedagem: domínio adicional criado no cPanel da HostGator em 10/09/2026 (br604, raiz própria `/clubedomosaico.com.br`), mesmo plano das outras ilhas, custo extra zero.
- DNS: nameservers ns604/ns605.hostgator.com.br apontados no registro.br em 10/09/2026, ~11h20 BRT. Zona no br604 com A = 108.179.253.218. Propagação pendente no momento deste commit.
- Search Console: propriedade `sc-domain:clubedomosaico.com.br` criada; TXT `google-site-verification=KWnwrQz3FOTs0Bln_y9EpjPhjJrWKwzpT2fi68L-2uA` gravado na zona (serial 2026091004). Verificação falhou na primeira tentativa porque o Google ainda via o DNS do registro.br — repetir depois da propagação.
- WordPress: instalado em 10/09/2026 14h51 BRT via Softaculous (7.1 pt-BR, instalação limpa, admin não é "admin"); SSL emitido na madrugada de 11/09; plugins da lista curta ativos em 11/09.
- Snippet de Sync: "Clube do Mosaico Sync" v1.1.5, snippet #5, ATIVO desde 11/09/2026; primeiro sync leu a revisão 3 (0 aplicados, 5 aguardando desembarque). Endpoints no PROMPT.md.
- Logo: logo completo e favicon subidos pelo Raphael na biblioteca de mídia em 11/09/2026 (URLs no PROMPT.md). **O logo completo é o do cabeçalho, transparente, a 52 px e sem texto ao lado, desde 11/09 20h35Z.** Em `identidade/logo/` ficam os favicons e a lótus solta (esta, truncada, só faria falta em ícone pequeno).
- E-mail da artesã (usuário `artesa` e notificações de lead): mina196@hotmail.com
- **Medição (GA4): LIGADA em 12/09/2026 17h37Z**, pela casca 1.7.0 — `gtag` no `wp_head`
  na prioridade 8, ID `G-0K5PY39HV7` (propriedade `553922792`). É o **marco zero** da
  série em `dados/audiencia.md`: antes dessa hora não existe dado, e o zero de qualquer
  leitura anterior media a ausência da tag, nunca a ausência de visita.
- **PENDÊNCIA DO RAPHAEL, e não bloqueia bloco nenhum:** o **Site Kit by Google 1.187.0**
  está instalado e ativo nesta ilha e **não mede nada** (medido no HTML servido: zero
  `gtag(`, zero ocorrência do ID; só deixa uma meta `generator` e um `dns-prefetch`).
  Conectá-lo ao GA4 pelo wp-admin criaria um **segundo dono da tag** e passaria a contar
  toda sessão duas vezes, sem nada mudar na tela. O caminho limpo é desinstalá-lo — a
  seção 11 já o declara opcional desde 10/09/2026, porque a medição do Search Console é
  pela API. Quem acusa a contagem dupla, se ela acontecer, é o `conferir-no-ar.py`.
- **REDE — item aberto que é configuração, não código:** `www.googletagmanager.com`
  responde **403 ao CONNECT** no ambiente das rotinas (política de egresso, medida cinco
  vezes com o domínio da ilha em 200 na mesma passada). Enquanto esse host e
  `*.google-analytics.com` não entrarem na rede Personalizada, **nenhuma verificação de
  tag por navegador a partir da nuvem funciona**, e o Tempo Real do GA4 só o Raphael
  confirma, no Chrome dele. Falta também a credencial da conta de serviço
  (`GOOGLE_SA_B64`) no ambiente, sem a qual `ferramentas/ga4.py` não lê a série.
- Casca: snippet "Clube do Mosaico Casca" **v1.5.0**, `publicar: true` no manifest (revisão 9),
  snippet #6 no Code Snippets. **No ar e conferido nas dez URLs em 11/09/2026 22h05Z.**
- Ferramenta F2: snippet "Clube do Mosaico F2 — qual cola e qual rejunte" **v1.0.0**,
  snippet **#7**, criado pelo Sync em 11/09/2026 22h03Z. Serve
  `/materiais/qual-cola-usar-no-mosaico/`, a primeira página de nível 3 da ilha.
- **O banco virou dado PUBLICADO nesta execução**: `esquema-banco`, `materiais-colas` e
  `materiais-rejuntes` passaram a `publicar: true` e viraram option no site. Até aqui eles
  eram pesquisa, e o caminho vivo de `cdm_casca_numeros()` — o que lê a option — **nunca
  tinha existido no ar**, exatamente o defeito latente que a Robometria encontrou em
  11/09/2026. Agora os números da tela vêm do banco servido, não do instantâneo digitado.

## O que já foi entregue
- 14/09/2026 21h17Z — **A ESCOLA GANHA A PRIMEIRA FILHA, E O DESPACHO DO RAPHAEL DE
  14/09 FECHA INTEIRO.** Casca **1.11.0**, snippet novo `clubedomosaico-tecnicas`
  **1.0.0**, manifest na revisão **34**, `/status` com revisão 34 em UM disparo
  com 12 aplicados. **Uma URL nova:** `/como-fazer/o-que-e-mosaico-picassiete/` —
  a ilha vai de 11 para **12** URLs publicadas, e 12 estão no sitemap (11 páginas
  mais a peça; `/atelie/` e `/materiais/como-sabemos/` seguem `noindex` e fora).
  **O endereço não é o que o despacho pediu**, e a diferença tem regra: a 16.1
  proíbe página solta na raiz, e o slug é a consulta que a pessoa digita.
  **O QUE DUAS EXECUÇÕES TINHAM DADO COMO IMPOSSÍVEL ERA ERRO DE LEITURA DE RÉGUA,
  não falta de dado.** Os três portões que elas mediram decidiam errado: um
  contava caco de prato — que não tem fabricante — quando o que a página
  recomenda é a **cola** do caco, e são cinco; outro cobrava a 16.5 de uma página
  que nasce filha direta; o terceiro dizia que nenhum número autoriza leva nova,
  o oposto do que a 21.1 manda para ilha abaixo do piso. Esse virou a **21.8** do
  contrato, porque é a segunda ilha a lê-lo ao contrário.
  **A página não decide nada:** quem escolhe a cola é a régua da F2, chamada para
  o caquinho de louça — 45 células servidas no HTML e recalculadas a cada
  requisição. Onze delas dizem que não há cola que o fabricante sustente, e a
  página **se recusa** a responder o rejunte, com a causa medida.
  **Duas dívidas de texto do banco viraram defeito no ar e foram pagas no mesmo
  bloco:** o banco de técnicas estava sem acento (era lido só por ferramenta até
  hoje) e com aspa reta, que o filtro do WordPress escapa duas vezes e serve como
  entidade na tela. A troca dos acentos tem prova de que foi só de diacrítico.
  **O que só uma pessoa mede:** se a tabela de 9 × 5 se lê bem num telefone. A
  Fundação mediu o HTML servido, a rolagem horizontal declarada e os cabeçalhos
  de linha e coluna; **ninguém tocou a tela.**
- 14/09/2026 11h18Z — **O DESPACHO DO RAPHAEL DE 14/09 SAIU INTEIRO, MENOS UMA COISA QUE
  NÃO É CONSERTO.** Ateliê **1.3.0**, loja **1.2.0**, casca **1.9.2**, manifest na revisão **30**, `/status`
  com revisão 30. **Nenhuma URL nova, nenhuma página criada.**
  **A ILHA TEM A PRIMEIRA PEÇA DE VERDADE:** a artesã cadastrou "Quadro flores do campo"
  em 13/09 16h46 (quatro fotos, R$ 500, pronta entrega) — e `/v1/loja` diz
  `publicadas: 1, rascunhos: 0`.
  **O 404 que ela viu ao publicar não era regra de reescrita: era o nome do parâmetro.**
  O painel carregava o id em `?peca=`, e `peca` é o tipo de conteúdo com `query_var`;
  para o núcleo `/atelie/?peca=24` é "a peça de slug 24", que não existe, e o tema serve o
  404 dele — com a foto em preto e branco do Twenty Twenty-Five, que é a que ele descreveu.
  Atingia **sete** voltas do painel, não só publicar. O parâmetro é `cdm_peca` desde agora,
  e um portão varre o snippet comparando toda chave de URL com as variáveis públicas do
  WordPress. No lugar do 404 há faixa de "Peça publicada!" com "Ver no site" (só quando a
  peça está mesmo no ar) e "Cadastrar outra peça".
  Mais: `Selecione…` no lugar de `Escolha` em toda lista, com `required` nas duas que ligam
  a peça ao site e `formnovalidate` no rascunho; a técnica **Picassiete** na lista (a rota
  dizia `tecnica: 4` e diz **5** — o que faltava era a versão da Loja subir, não a linha);
  e a **galeria** da ficha com miniatura quadrada, seta, ampliar em `<dialog>` e zoom, sem
  uma linha de biblioteca.
  **`dados/pecas.json` nasceu** (seção 24), com a peça de verdade dentro.
  **E um defeito que só o ar tinha:** a primeira versão das setas saiu publicada com um
  `</p>` órfão colado no `</button>`, porque o `wpautop` usa etiqueta de bloco como
  fronteira de parágrafo e `button` não é bloco. A régua do `teste-loja` olhava só um lado
  e passou verde. Agora ela olha os dois, nomeia qual apareceu, e o `conferir-atelie-no-ar`
  procura as cinco marcas do estrago no HTML servido.
  **O que ficou aberto, e não é conserto:** `/tecnicas/Picassiete/` não nasceu porque
  **nenhuma** técnica desta ilha tem página — as taxonomias são `public => false` por
  orçamento de rastreamento. É bloco de malha, e está na frente da fila.
  **O que só uma pessoa mede:** o dedo dela na galeria, num telefone.
  **E um terceiro defeito achado na própria conferência, que ninguém escreveu:**
  `/author/artesa/` entrou sozinho no `wp-sitemap.xml` quando a artesã publicou a
  primeira peça — o provedor `users` do núcleo só lista autor que TEM conteúdo. É
  página fina que repete a `/loja/` e um endereço que **confirma o login dela**.
  Casca **1.9.2** tira o provedor; no ar o sitemap foi de 12 para **11 URLs**.
- 12/09/2026 23h13Z — **BLOCO 4d, O CORTE: A ILHA TEM UM ATELIÊ.** Dois snippets novos
  (`clubedomosaico-loja.php` 1.0.0 = snippet **#9**, `clubedomosaico-atelie.php` **1.0.1** =
  snippet **#10**, criados pelo Sync), casca **1.9.0**, manifest na revisão **16**,
  `/status` conferido às 23h13Z (revisão 16) e às 23h28Z (revisão 17, depois do conserto
  dos botões de foto), cada uma em UM disparo com 9 itens aplicados. **Uma URL nova:**
  `/atelie/`, que é `noindex` e fora do sitemap — a ilha vai de 11 para 12 páginas
  publicadas, e só 11 estão no índice.

  **O e-mail de acesso da artesã saiu às 23h13m23s Z** para mina196@hotmail.com, com o
  botão único "Criar minha senha e entrar". Isso é **medido**, não presumido: a rota
  `/wp-json/clubedomosaico/v1/atelie` (protegida pelo token do Sync) devolve o relato que
  o `init` gravou, com a hora em UTC e o que o `wp_mail` respondeu. Uma tentativa, sem
  erro. **O que `wp_mail` true significa e o que não significa:** o servidor aceitou a
  mensagem. Ele **não** diz que ela passou do filtro de spam da Hotmail — e o `PROMPT.md`
  manda tratar queda em spam como **bloqueio da ilha**, não como detalhe (adendo 3, na linha que
  começa por "Enviar por `wp_mail` com `From:`"). *(A citação era "a linha 178", que já apontava
  para outro assunto: número de linha envelhece a cada edição do arquivo, então a referência passa
  a ser pela frase. Corrigido pelo Pente Fino em 14/09/2026.)*

  **A senha dela não existe para a Fundação, e isso é desenho.** O snippet gera uma senha
  aleatória e a **descarta sem imprimir** em log, e-mail ou option; o que chega a ela é o
  link. Portanto o portão do despacho — entrar como `artesa` e cadastrar uma peça de teste
  — **não pode ser cumprido de ponta a ponta pela nuvem**, e fabricar um jeito seria
  quebrar a única coisa que protege a conta de uma pessoa de verdade. O portão foi partido
  em duas metades **declaradas** no cabeçalho do `teste-atelie.php`.

  **A senha é criada em `/atelie/`, não no `wp-login.php`** — único desvio consciente da
  especificação de 10/09, e a favor dela: a chave continua sendo a nativa, a tela é a
  nossa, e ao terminar ela já entra logada.

- 12/09/2026 21h19Z — **BLOCO 3d: a categoria PASTILHA do banco**, em
  `dados/materiais-pastilhas.json` (10 SKUs, casca **1.8.0**, manifest na revisão 15,
  `/status` conferido). Nenhuma URL nova. Três campos nascem `null` com motivo escrito —
  peças por placa, passo de fábrica e peso unitário — e é isso que o arquivo tem de mais
  útil: **nenhum fabricante brasileiro publica quantas pastilhas vêm numa placa**, e a
  divisão que a SERP inteira faz não fecha (em 6 dos 10 não dá inteiro; nos outros 4 exige
  junta zero). O peso da caixa de um dos itens **passa do teto físico do vidro maciço**, o
  que prova que embalagem está contada dentro — então peso de caixa não vira peso de
  produto em tela nenhuma. Junto veio o conserto de um portão que **nunca tinha rodado**:
  `validar-banco.py` calculava o passo com o lado da pastilha no lugar do lado da placa, e
  só podia disparar quando a categoria deixasse de estar vazia. Medem isso
  `ferramentas/validar-pastilhas.py` (139 afirmações, um processo por item) e
  `ferramentas/mutacoes-pastilhas.py` (12 de 12, **6 invisíveis para o portão do esquema**).
  A varredura da 14.3 foi refeita: categorias do vocabulário sem um item caíram de 5 para 4.
- 11/09/2026 22h05Z — **BLOCO 4: A F2, a primeira ferramenta da ilha, no ar em
  `/materiais/qual-cola-usar-no-mosaico/`** (snippet `clubedomosaico-f2.php` v1.0.0,
  casca 1.5.0, manifest na revisão 9, `/status` conferido). Primeira página de **nível 3**
  da ilha. A resposta é servida pelo **servidor** — formulário GET para a própria página,
  nenhuma linha de decisão em JavaScript —, então cada uma das 45 combinações de base ×
  ambiente é HTML servido de verdade e não existe régua duplicada entre PHP e JS. O estado
  com parâmetro sai com `noindex, follow`; quem entra no índice é a âncora, uma só, e o
  canonical fica com o `rel_canonical()` do núcleo (imprimir o nosso serviria dois).
  A elegibilidade é recomputada das declarações dos fabricantes pelas regras do
  `esquema-banco.json`, conferida contra as matrizes escritas à mão no bloco 3.
  O bloco de compra vem antes da procedência em todo cartão, mesmo com os dez itens sem
  link. Vieram junto `ferramentas/teste-f2.php` (72 afirmações, varrendo os 45 estados de
  cola e os 60 de rejunte, um processo cada), `ferramentas/mutacoes-f2.py` (20 mutações),
  `ferramentas/restaurar-acentos.py` e `ferramentas/atualizar-manifest.py`.
- 11/09/2026 20h35Z — **O LOGO DELE, INTEIRO, NO CABEÇALHO** (casca 1.4.0, manifest na revisão 8,
  `/status` conferido). Fecha o despacho do Raphael de 11/09 (2) inteiro, os cinco itens na mesma
  execução: `<img>` do logo completo a 52 px com link para a home e **sem texto ao lado**, barra de
  84 px, lótus solta fora do cabeçalho, `VOZ.md` corrigido no molde de casca LOJA. O `srcset` serve
  as reduções que o próprio WordPress gerou do upload dele (41 KB no lugar de 1,26 MB num espaço de
  78 px) e o `src` continua sendo a URL exata do despacho. Veio junto
  `ferramentas/conferir-no-ar.py`, que mede o HTML **servido** com régua própria (102 afirmações,
  nenhuma falha), e seis mutações novas no `mutacoes-voz-e-cabeca.py` — 24 de 24 reprovadas.
- 11/09/2026 19h40Z — **A ÁRVORE DA SEÇÃO 16** (casca 1.3.0, manifest na revisão 7,
  `/status` conferido). `ARVORE.md` com os três níveis e o lugar das nove páginas;
  trilha visível em oito delas (a home não tem, 16.3); `BreadcrumbList` nas mesmas
  oito; cluster "Veja também" ligando LOJA, GUIA e ESCOLA. **Nenhuma URL mudou e
  nenhuma precisou:** esta ilha já nascera com a árvore certa na estrutura — as três
  seções eram nível 1, a única página de nível 2 já tinha mãe desde 1.2.0 e as quatro
  da raiz são as que a 16.1 admite ali. Sem 301, sem mudança de sitemap. Veio junto
  `ferramentas/mutacoes-arvore.py` (19 mutações, 19 reprovadas) e a bancada aprendeu a
  **fabricar duas bordas que o mundo ainda não tem**: o degrau de trilha sem página e a
  página com exatamente uma irmã. `teste-casca.php` foi de 198 para 327 afirmações.
- 11/09/2026 — **Bloco 3b: a casca da ilha**, em `snippets/clubedomosaico-casca.php` v1.0.0
  (manifest na revisão 4, `publicar: true`, `ativo: true`). Oito páginas por shortcode: início,
  loja, materiais, como-fazer, sobre, contato, divulgação de afiliados e privacidade. ~~Cabeçalho e
  rodapé pretos~~ **Cabeçalho CLARO e rodapé escuro** com miolo branco *(esta linha dizia "cabeçalho
  e rodapé pretos", que é o mundo anterior a 11/09 e é exatamente a causa que a seção logo abaixo
  deste arquivo nomeia: "o logo sumiu em 1.1.0 porque o cabeçalho era preto e o wordmark dentro do
  arquivo é vinho #69030C". Corrigido pelo Pente Fino em 14/09/2026)*, menu sanfona acessível, favicon próprio embutido a partir do PNG
  entregue, JSON-LD Organization + WebSite. Vieram junto quatro ferramentas de bancada:
  `gerar-favicon.php`, `render-para-teste.php`, `teste-casca.php` (127 afirmações) e
  `teste-navegador-casca.mjs` (33 medições em Chromium).
- 10/09/2026 — Pesquisa de palavras-chave e SERP (na memória `/areas/projeto-clube-do-mosaico.md`) e estratégia aprovada em conversa (artifact "Clube do Mosaico").
- 10/09/2026 — **Bloco 3: modelo do banco** em `dados/esquema-banco.json`, a categoria
  COLA em `dados/materiais-colas.json` (5 registros) e o verificador
  `ferramentas/validar-banco.py`. Manifest na revisão 3, `publicar: false`, sem Sync.
  Sem coleta nova: os 5 registros vêm inteiros do bloco 2, com a mesma fonte e a mesma data.
  O verificador recomputa as 18 células da matriz da F2 a partir das declarações e bate com a
  tabela publicada no esquema; três mutações provaram que ele falha quando deve.

- 10/09/2026 — **Bloco 2: especificação das duas ferramentas** em
  `dados/especificacao-calculadoras.md` e **constantes de fabricante** em
  `dados/constantes.json` (manifest na revisão 2, `publicar: false`, sem Sync). 11 constantes
  coletadas direto do domínio de cada fabricante e 6 pendências nomeadas com o documento
  exato que fecha cada uma. A F2 (cola e rejunte) vem antes da F1, como o bloco 1 mandou.
- 10/09/2026 — **Bloco 1: corpus de buscas** em `dados/corpus-buscas.md` (manifest na revisão 1, `publicar: false`). Três clusters com a SERP classificada consulta a consulta em aberta/tomada/armadilha, coletada por busca web da nuvem. Ordem da fila definida por intenção × chance de primeira página: colas/F2 antes de rejuntes/F1, alicates antes de pastilhas, `/tecnicas/bizantino` como única cabeça de volume alto com chance real. Confirmadas como TOMADAS e fora da fila: `curso de mosaico` (escolas reais — a ilha não vende curso), `presente artesanal` (Elo7) e `vaso centro de mesa` (Leroy).

## O que a coleta do bloco 1 já provou, e que muda o desenho das ferramentas
- **A SERP de rejunte responde a pergunta errada.** Todo resultado é de obra (0,2–0,4 kg/m², "1 kg faz 3 m²"), calculado com azulejo grande. Peça de artesanato usa pastilha de 1×1 ou 2×2 cm e não é medida em m². A F1 não vai competir com essas páginas: ela responde outra coisa.
- **A regra cola × base circula sem procedência.** Madeira → cola branca, vidro → silicone, alvenaria → argamassa aparece em blog (FazFácil, Vila do Artesão) sem fabricante, sem código, sem data e sem separar interno/externo/molhado. Abre a F2 e ao mesmo tempo **proíbe** usar a SERP como fonte dela: o bloco 2 coleta de Quartzolit, Tekbond, Loctite e Cascola.
- **As lojas vendem pastilha em três unidades diferentes** — 100 peças (Shopee), 100 gramas (Bazar Horizonte), placa 30×30 com 225 (Boutique dos Azulejos). Converter peça ↔ grama ↔ placa é número próprio da ilha e não existe na SERP.

## O que o bloco 2 provou, e que decide como as ferramentas nascem
- **A ficha do próprio fabricante do silicone acético desmonta a prática corrente do
  mosaico brasileiro.** A ficha BRSA004 do Silicone Acético Construção Tekbond (revisada em
  10/2025) lista **espelho, concreto, cimento, tijolo, calcário, superfície alcalina,
  superfície pintada ou porosa, acrílico, aquário, metal corrosível e imersão contínua**
  entre as superfícies em que o produto não deve ser usado. Vaso de cimento, caco de espelho
  e peça de área molhada são exatamente o que o blog manda colar com silicone acético. Isso
  torna a elegibilidade da F2 **mecânica**: basta uma restrição bater com a entrada para o
  produto sair dos recomendados, com a frase do fabricante e a data na tela.
- **O par acético/neutro é do mesmo fabricante**, então a F2 diz "não use A, use B" sem sair
  de uma fonte só: o Silicone Neutro Tekbond é declarado para espelho, concreto, alvenaria e
  pedra, que são justamente as restrições do acético.
- **O número que abre a F1 existe e é grande.** Aplicando a fórmula publicada pela própria
  Quartzolit ao tamanho real da pastilha de artesanato, pastilha de 1×1 cm com 4 mm de
  espessura e junta de 2 mm consome **2,80 kg/m²** de rejunte — sete a catorze vezes os
  0,2–0,4 kg/m² que a primeira página do Google publica, porque a SERP inteira calcula com
  azulejo de obra. O bloco 1 tinha suspeitado; o bloco 2 mediu.
- **A placa 30×30 com 225 pastilhas não é pastilha de 1×1 cm.** O passo é 30/√225 = 2,00 cm,
  ou seja, pastilha nominal de 2 cm. É o erro que a artesã comete ao comparar preço entre
  loja que vende por peça e loja que vende por placa.
- **A espessura da pastilha não é constante de fabricante** — nenhum fabricante de pastilha
  de artesanato padroniza — então virou campo de entrada com aviso, e cada linha da tabela
  de exemplos declara a espessura que usou.

## O que o bloco 3 provou, e que corrige a matriz escrita à mão no bloco 2
- **A cimentcola AC-II não tem declaração de SUBSTRATO.** A especificação a recomendava para
  base de cimento citando que ela é declarada para "área interna e externa" — mas isso é
  ambiente, não superfície de aplicação. As únicas superfícies que a coleta nomeou
  ("cerâmicas e placas de pedra natural de até 120 × 120 cm") são a **peça assentada**. Sem
  essa declaração ela não é recomendação primária em base nenhuma, e quem responde à base de
  cimento é o silicone neutro, que declara concreto e alvenaria com todas as letras.
  Pendência nomeada: `cimentcola-substrato-declarado`.
- **Cerâmica e vidro em ambiente comum são empate, não escolha.** O mesmo fabricante declara
  cerâmica para o acético *e* para o neutro, e nenhum dos dois declara o ambiente. A página
  lista os dois como equivalentes; fingir uma preferência que a fonte não sustenta é o começo
  de ordenar por comissão.
- **Em sol e chuva o acético não fica "em segundo lugar": fica fora.** Ambiente de exposição
  continuada exige declaração explícita de resistência — só o neutro declara chuva e raios UV.
- **MDF molhado e externo têm resposta.** A especificação dizia "a ilha não recomenda" porque
  só tinha olhado PVA e acético; o neutro declara madeira entre os substratos que veda, e
  chuva e UV entre as resistências. O PVA sai desses ambientes por delimitação do próprio
  fabricante ("ambientes internos"), não por proibição inventada.
- **O par acético/metal mostrou por que "conjunto mais estreito" precisa ser regra escrita.**
  A mesma ficha indica alumínio anodizado e proíbe metal corrosível, zinco e chapa
  galvanizada. Vence a proibição: quem monta mosaico não sabe dizer se a chapa dela é
  galvanizada.

## O que o bloco 3c provou, ao encher a categoria REJUNTE

- **Rejunte não é cola, e o esquema só tinha olhado cola.** Na cola, a lista do fabricante nomeia
  a **base** — a superfície sobre a qual se cola. No rejunte, a mesma lista nomeia a **tessela** e o
  **ambiente**: "cerâmicas, pastilhas de porcelana e de vidro" é o que vai ser rejuntado, nunca o
  vaso de cimento embaixo. Rejunte não toca a base. Por isso a categoria ganhou mapa de termos,
  regras e matriz próprios, e a variável que decide passou a ser a **largura da junta**.
- **O defeito latente que isso revelou, medido:** `computar_celula()` varria todos os materiais do
  banco sem olhar categoria. As 18 células da F2 passavam porque o banco só tinha cola; o primeiro
  rejunte gravado fez as 18 falharem de uma vez, cada uma acusando os cinco rejuntes como
  "eliminados por silêncio". O conserto tentador — colar os cinco ids nas 18 células — deixaria a
  matriz verde dizendo uma bobagem.
- **Um número falso que já estava NO AR:** o cartão "Rejuntes" do Guia trazia `no_banco => 0`
  digitado à mão, e a categoria acabara de ganhar cinco produtos. O `teste-casca` não viu porque
  conferia só a categoria cola — a única que existia quando ele foi escrito. A casca 1.1.0 passa a
  contar o banco por categoria, e o teste passa a cobrar as seis, nos dois sentidos: categoria sem
  arquivo mapeado reprova, e arquivo de banco sem cartão no Guia também.
- **Uma busca que se respondeu sozinha, apanhada no ato.** Uma consulta com o número `1,55` escrito
  dentro dela devolveu `1,55` como se fosse declaração do fabricante. Foi descartada: pergunta que
  carrega a resposta não mede nada. O CR por tipo de rejunte continua pendente — e isso virou
  limite declarado da F1, não "seria bom ter": a coluna de rejunte vale só para rejunte
  **cimentício**, porque o acrílico é pronto uso em pote de 1 kg e o epóxi é bicomponente, e o
  1,75 sai de um exemplo de pó.
- **O achado mais valioso é também o que não fecha.** O *rejunte piscinas quartzolit* é o único
  material do banco inteiro cujo fabricante nomeia **pastilha de vidro** em uso submerso — e mesmo
  assim não é recomendado em célula nenhuma: a faixa de junta dele não foi obtida, e o que ele
  declara é **água tratada quimicamente**, que é piscina, não a água parada de um vaso de jardim.
  A peça submersa segue sem cola declarada (só o Durepoxi, nível 4). A faixa continua descoberta, e
  a página diz exatamente o que já existe e o que falta.

## O que está travando
- **A rede foi RECONFERIDA em 11/09/2026 21h23Z, antes de trabalhar** (seção 20.2 do
  contrato), e de novo no desembarque: dois `curl` seguidos à home devolveram **200,
  200**, e o `/status`, o Sync, as dez páginas, o sitemap e as três URLs da imagem
  responderam. Nada de `000`, nada de 403. A ilha está no ar na **revisão 9**.
- **O SYNC PRECISOU DE TRÊS DISPAROS, e isso não é bloqueio: é cache de borda.** Os dois
  primeiros leram do `raw.githubusercontent` um `manifest.json` ainda na revisão 8
  enquanto já baixavam a casca nova, e a trava de `sha256` recusou aplicar — que é ela
  funcionando. O cache é por caminho, não por commit: o arquivo novo e o índice velho
  chegam em momentos diferentes, e o `?v=` que o Sync já acrescenta não resolveu. Esperar
  e repetir resolveu em poucos minutos. **O que não se pode é ler o primeiro
  "0 aplicado(s)" como entrega** — é exatamente a forma de "commit sem Sync" que a seção
  20 existe para impedir, com outra roupa.
- ~~**A rede foi RECONFERIDA em 11/09/2026 19h21Z, antes de trabalhar**~~ (seção 20.2 do
  contrato): três `curl` seguidos à home devolveram **200, 200, 200** — nenhum `000`, nenhum
  403. O Sync, o `/status`, as nove páginas e o sitemap também responderam. A ilha está no ar
  na **revisão 7**. Esta linha existe porque bloqueio que não é reconferido a cada execução
  vira permanente sozinho, e foi assim que esta ilha ficou dois dias fora do ar por um
  diagnóstico que ninguém retestou.
- ~~**A ILHA INTEIRA NÃO ESTÁ NO AR, e agora são DUAS revisões presas.**~~ **RESOLVIDO em
  11/09/2026 17h50Z, e o diagnóstico anterior estava errado.** A ilha ESTÁ no ar: o Sync foi
  acionado por `curl` desta execução, as revisões 4, 5 e 6 desembarcaram, e o `/status` devolve
  **revisão 6**, igual à do manifest. As nove URLs respondem 200.
  **O que aconteceu, porque isto vale mais que o conserto:** o primeiro `curl` desta execução à
  home devolveu `000`, exatamente como nas duas execuções anteriores — e **o mesmo comando,
  repetido minutos depois, devolveu 200**, assim como o Sync, o `/status`, as nove páginas e o
  sitemap. Era intermitência do túnel, não bloqueio de rede: `clubedomosaico.com.br` está, sim,
  na lista Personalizada do ambiente. Duas execuções anteriores leram um `000`, escreveram
  "403 ao CONNECT" e nunca reconferiram — e o bloqueio virou permanente sozinho, prendendo duas
  revisões desta ilha por dois dias.
  **A regra que fica:** bloqueio herdado se testa de novo a cada execução, e uma falha de rede
  só vira bloqueio depois de repetir. A seção 4 do contrato manda testar antes de presumir; falta
  a outra metade, que é testar de novo antes de continuar presumindo.
- ~~**A LÓTUS DO CABEÇALHO**~~ — **deixou de ser pendência em 11/09/2026, 20h35Z.** O cabeçalho
  serve o **logo completo** do Raphael, que já contém a lótus e o nome, e o despacho de 11/09 (2)
  proíbe texto ao lado dele. A lótus SOLTA continua truncada no repositório
  (`identidade/logo/lotus-512.png`: o `IDAT` declara 11.638 bytes num arquivo com 8.770, `IEND`
  colado no fim, e o `zlib` recusa o primeiro bloco), e isso agora não bloqueia nada — o lugar dela
  é ícone pequeno, não o cabeçalho. Quando chegar um PNG transparente de ≥ 512 px no mesmo caminho,
  `php ferramentas/gerar-marca.php .` embute e confere; a ferramenta recusa arquivo que não abre,
  sem canal alfa ou com canto opaco.
- **O DIAGNÓSTICO DE 1.2.0 ESTAVA ERRADO, e é a cicatriz que esta execução deixa escrita.** Três
  lugares do snippet e um do `VOZ.md` afirmavam que o arquivo do Raphael "tem fundo preto". Não
  tem: é transparente, e ele conferiu na biblioteca de mídia. O logo sumiu em 1.1.0 porque o
  **cabeçalho** era preto e o wordmark dentro do arquivo é vinho `#69030C` — defeito de onde o
  logo foi posto, nunca do arquivo. A 1.2.0 consertou a causa (clareou o cabeçalho) e, pela
  leitura errada do sintoma, tirou também o logo, que era a parte certa. **Sintoma não é causa, e
  um diagnóstico escrito com ar de fato se propaga por versões** — a mesma forma do `000` lido
  como bloqueio de rede na semana passada.
- **Caixa `contato@clubedomosaico.com.br` não existe ainda.** O adendo 3 do `PROMPT.md` pede que ela
  seja criada no cPanel (ou que o SPF/DKIM do domínio seja garantido) para o e-mail de lead do bloco
  4d chegar ao Hotmail da artesã. Não é trabalho da Fundação: exige o painel da hospedagem. Por isso
  a página `/contato/` publicada **não** anuncia endereço de e-mail — diz que o canal está sendo
  configurado, em vez de publicar um endereço que devolveria a mensagem.
- **Substrato da cimentcola AC-II** (achado do bloco 3): sem ele, a base de cimento fica
  respondida só pelo silicone neutro. Está no Boletim Técnico 2024-09 da Quartzolit, que a
  nuvem não abre. Não bloqueia publicação.
- Loja: depende da mãe do Raphael cadastrar peças na área da artesã (bloco 4d, snippet de CPT). O login é criado pelo snippet e entregue ao Raphael. Não bloqueia os blocos 1–3.
- CPC por consulta: o Planejador está na conta do Raphael, no navegador. Ficou declarado como ausente no corpus, nunca estimado. Coluna a preencher na primeira leitura semanal com o painel aberto.
- SERP de `colar de mosaico` e `mandala de mosaico`: não verificadas nesta execução, e estão escritas assim no corpus.
- **Coluna de gramas de cola da F1**: falta o consumo em kg/m² da cimentcola AC-II/AC-III e o
  rendimento do silicone por área (o fabricante declara por cordão). São as duas únicas
  pendências que bloqueiam publicação, e bloqueiam só essa coluna — a F1 sai sem ela dizendo
  por quê. As outras quatro pendências (CR por tipo de rejunte, secagem do Cascorez, ficha do
  Tekbond Espelho Fix, rejunte epóxi) são coleta, não bloqueio.
- **Duas faixas descobertas da F2, declaradas em vez de chutadas**: peça em contato
  permanente com água e base de plástico. A página vai dizer que não publica recomendação
  nesses dois casos.
- **A nuvem não abre PDF de fabricante.** `curl` e `WebFetch` para quartzolit.weber e
  tekbond.com.br voltaram `EGRESS_BLOCKED`/`connect_rejected`: a rede das rotinas libera os
  domínios das ilhas, `*.googleapis.com` e `github.com`, e nada mais. A coleta do bloco 2 foi
  feita por busca web restrita ao domínio de cada fabricante, e cada constante declara isso
  em `fonte_tipo`, com `conferir_no_pdf` marcando as que merecem segunda leitura. Se o
  Raphael quiser fechar essa lacuna, é acrescentar quartzolit.weber, tekbond.com.br,
  cascola.com.br e henkel.com.br à rede Personalizada do ambiente das rotinas.
- DNS/WordPress/Search Console seguem como no registro de 10/09. Nada disso trava os blocos 2 e 3, que não dependem de site.

## Pendências do Raphael (não travam)
- Nome, foto e perfis de redes sociais da artesã para o Sobre — decidido em 11/09/2026 que ela aparece.
  A casca já publica o Sobre com o bloco dela pronto: escreve "uma artesã", sem nome de fantasia e sem
  foto genérica, e o teste reprova se alguém inventar um nome. Chegando à pasta `identidade/artesa/`,
  entram também o `sameAs` do JSON-LD, que hoje está deliberadamente ausente.
- ~~**Domínio da ilha na rede Personalizada do ambiente das rotinas.**~~ **Não era isso.** A rede
  alcança a ilha; o que houve foi intermitência lida como bloqueio em duas execuções seguidas —
  ver "O que está travando". Nada a fazer, e nada a pedir ao Raphael por aqui.
- ~~**A lótus do cabeçalho**~~ — **não é mais pendência**: o cabeçalho leva o logo completo dele
  desde 20h35Z de 11/09. A lótus solta segue truncada no repositório e só faria falta em ícone
  pequeno; ver "O que está travando" e `identidade/logo/LEIA-ME.md`.
- **O tamanho do logo no cabeçalho, se ele quiser opinar.** A 52 px de altura (o número do
  despacho dele) o wordmark dentro do arquivo fica com ~8 px por linha: lê-se como logotipo, mas é
  pequeno. Caminhos, e a escolha é dele: subir para ~64 px, ou mandar uma versão horizontal do
  lockup (lótus ao lado do nome em vez de acima). Não trava nada.
- **Os hexadecimais do cabeçalho.** O despacho sugeriu `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A`;
  a casca serve os tokens aprovados por ele em 10/09 (`papel #FFFFFF`, `traço #E9DCD7`,
  `tinta #1F1715`, `coral #FC483B`), que são vizinhos de um a quatro passos. Um segundo branco a
  quatro unidades do primeiro é defeito, não identidade — mas se ele quiser exatamente aqueles
  valores, é uma linha. Registrado em 11/09 e de novo em 20h35Z.
