# Registro de execucoes — Clube do Mosaico

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e o
proximo passo desbloqueado.

09/10/2026 16h16Z–17h0xZ — AS OITO PÁGINAS PELO NOME DO PRODUTO ESTÃO NO AR, E OS PORTÕES ACHARAM TRÊS DEFEITOS DE RÉGUA E NENHUM DE PÁGINA

**A ilha foi de 21 para 29 URLs**, `/status` e manifest na **revisão 72**, casca **1.21.0** e um snippet
novo (`produto` 1.0.0). É o item que faltava do despacho do Raphael de 09/10 (3): a passada das 14h05Z
abriu os dois portões e não alcançou a casca; ela está de pé agora.

1. **OS DOIS COMANDOS DA 29 RODARAM ANTES DE TUDO.** `conferir-no-ar.py` **APROVADO, 524 afirmações,
   0 falha** (21 de 21 URLs em 200, as três da 29.2 em 200, caminho virgem em 404).
   `leitura-do-visitante.py` **REPROVADO com EXATAMENTE 1 defeito**: o soft 404 da borda, pendência do
   Raphael desde 29/09 — vermelho esperado, com dono escrito. **Zero defeito novo.** Rede pela 20.2:
   200 nas TRÊS passadas, com `aquametria.com.br` em 200 nas mesmas.

2. **A ESCOLHA DA ILHA: FOCO, SEM CORRIDA.** `foco.md` nomeia a **clubedomosaico**, então pela 1.2 não
   houve rotação. `executando_desde` estava `null`, que pela 1.1 já significa que nenhum bloco da
   Fundação está vivo — os commits de 14h50Z e 14h54Z são **de ronda da Sentinela**, e a 1.1 diz com
   essas palavras que commit de ronda **não reserva nada**. Reserva aceita às 16h16Z no primeiro push,
   e **renovada às 16h52Z** porque o bloco passou de 40 minutos (a 1.1 manda reescrever o campo).
   O despacho da Sentinela de hoje não tinha nada para a Fundação cumprir.

3. **AS DUAS METADES, E POR QUE ELAS NÃO PODEM SER UM ARQUIVO SÓ.** `dados/paginas-de-produto.json` é
   **DECLARADO** e escrito à mão — título, `description`, a resposta em duas frases, o que é e o que
   não é, o "qual escolher" por uso, o dado fino e as perguntas, na voz do `VOZ.md`.
   `dados/vitrine-de-produto.json` é **GERADO** por `ferramentas/gerar-vitrine-de-produto.py`. Prosa
   dentro de arquivo gerado é reescrita pela coleta seguinte; número dentro de arquivo escrito à mão
   envelhece calado. **Os dois erros já foram pagos nesta ilha, e a separação é o conserto.**

4. **NENHUM PREÇO É DIGITADO NA PROSA.** A camada declarada traz moldes — `{MIN}`, `{MAX}`, `{N}`,
   `{UNIDADE}`, `{SOBRE}`, `{DATA}` — e quem os enche é o snippet, da vitrine. A bancada **reprova se a
   camada declarada trouxer "R$" em lugar nenhum**, e a mutação 16 prova que ela morde. E o
   preenchimento tem **DOIS modos**: espaço inquebrável na tela, espaço normal no JSON-LD. `&nbsp;`
   publicado como texto da resposta é diferença que **nenhuma revisão humana vê** — na tela as duas
   saem idênticas.

5. **O GERADOR RECALCULA O NÚMERO PRÓPRIO DAS OFERTAS QUE ENTRAM** e o confere contra o resumo da
   coleta; discordando, ele **não grava**. Sai com código 1 também quando uma consulta que publica
   chega com menos de **TRÊS** ofertas (o piso da 30.2) ou com oferta sem link de afiliado com o
   `sub_id` desta ilha. `--conferir` regera e compara, e é por ele que o arquivo não pode ser editado
   à mão (mutação 18).

6. **O CAMPO `nota` NÃO VAI AO AR, e a ausência é MEDIDA.** Das 58 ofertas que servem, **31 vêm com
   `"0"`** e uma com `"1"`, e **nenhum arquivo desta ilha diz o que o campo significa** — não se sabe
   se é estrela de 1 a 5 nem se `0` quer dizer "sem avaliação". Servido na tela, isso publica "produto
   péssimo" em mais da metade da lista e **"nota 1" num produto que a própria página recomenda**. A
   30.2 lista o que o anúncio sustenta — título, preço, foto, medida e quantidade declaradas — e
   `nota` não está nela. **Número cuja régua ninguém escreveu é significado inventado**, então ele não
   chega nem à vitrine. Quando alguém medir o campo, ele entra na tabela de uma vez.

7. **A TABELA NÃO TEM AS COLUNAS QUE O DESPACHO PEDIU, E A DIFERENÇA É HONESTIDADE.** Ele pede "tipo,
   medida, quantidade, preço, para que serve". **`tipo`, `medida` e `para que serve` não existem como
   campo em nenhum anúncio da coleta** — e o próprio despacho escreve, duas linhas abaixo, que o que o
   anúncio sustenta é "título, preço, foto, medida e quantidade declaradas". Então a tabela serve o que
   foi medido, **diz na tela que o anúncio não declara os outros**, e o "para que serve" sai no "qual
   escolher", escrito por quem leu os anúncios. Preencher coluna com palavra tirada do título seria
   inventar dado comercial com cara de tabela.

8. **TRÊS DEFEITOS DE RÉGUA, achados pelos portões, e NENHUM era de página:**
   - **o `nivel` da árvore.** Declarei **2**, lendo "nível 2" do despacho como contagem de barras — e
     nesta casca `nivel` é o lugar na **ÁRVORE FINAL**, escrito com essas palavras no registro das
     ferramentas. Resultado: **48 afirmações vermelhas**, com as oito entrando como irmãs dos seis
     cartões de prateleira e da camada de prova, a trilha com três degraus contra dois do mapa e cada
     página se listando como irmã de si mesma. **O precedente que o próprio despacho cita** —
     `/como-fazer/o-que-e-mosaico-picassiete/` — é `nivel => 3`. Corrigido para 3.
   - **a régua de shortcode do `teste-casca.php` não aceitava HÍFEN**, pela **TERCEIRA vez na mesma
     linha** (o dígito faltou em 14/09, com `[cdm_f2]`). As oito entravam na tabela de caminhos com
     caminho **VAZIO**, e trilha, `BreadcrumbList` e cluster eram medidos contra o nada. A nota que já
     estava ali dizia a lição: *"régua estreita demais não é régua frouxa: é régua que mede outra
     coisa"*.
   - **TRÊS LACUNAS DE PORTÃO, e quem as achou foram mutações que PASSARAM.** A bancada procurava a
     data em **qualquer lugar** da tela, e a procedência imprime a data por fora do molde — então a
     resposta podia perder a dela e o verde continuava. Procurava "Shopee" em **qualquer frase**,
     quando a 30.2 a quer na **procedência**. E a contagem de órfã ficava verde **sem o link da mãe**,
     porque as sete irmãs já davam sete — e a 16.4(f) nomeia justamente o link **da mãe**. Os três
     portões nasceram por causa delas.

9. **A MALHA, e nenhuma órfã.** `/materiais/` lista **as oito** com a âncora igual à consulta (16.4-a,
   nunca "saiba mais"); a home leva **TRÊS**, e quem as escolheu foi a **faixa de volume medida** em
   10/09/2026 — `pastilhas para mosaico`, `pastilhas de vidro para mosaico` e `alicate para mosaico`
   são as únicas das oito na faixa de 100 a 1.000 buscas/mês. **Intenção aqui tem número medido, não
   gosto.** As duas listas entram por **pontos de extensão novos da casca 1.21.0**
   (`cdm_materiais_secoes` e `cdm_home_secoes`), e não por a casca listar as oito à mão: foi ela mesma
   que escreveu em 1.5.0 que *"casca editada por bloco de ferramenta é casca que sai do ar por defeito
   de ferramenta"*. Cada página linka as **sete irmãs**, a F1, a **cola que JÁ ranqueia** (sem segunda
   URL, pela 30.4) e a loja do ateliê. **A pinça virou ÂNCORA dentro do alicate**, não página — a
   30.4 aplicada, porque ela devolve o mesmo alicate de duas consultas irmãs.

10. **O PISO DA 30.2 É PORTÃO DE VERDADE, medido num mundo FABRICADO.** `base-de-mdf` e `rejunte`
    nascem com **exatamente três** ofertas — o mínimo, não uma folga. Num mundo com duas, a bancada
    mede que a página do rejunte **sai do ar**, que **as outras sete continuam de pé** (portão que
    derruba demais é tão ruim quanto o que não derruba) e que **a mãe deixa de linká-la**, sem link
    para 404. Está escrito aqui para a próxima coleta não descobrir isso no ar.

11. **O DADO FINO DO REJUNTE SAI ANTES DA TABELA**, porque a resposta dele diz "vale ler o aviso abaixo
    antes de olhar o preço": das três ofertas, **uma é rejunte metálico dourado de 1 kg**, de outra
    categoria, e **duas são anúncio de revendedor sem marca de fabricante**. A página diz com essas
    palavras que **R$ 313,09 não é o teto do rejunte de mosaico**. Aviso depois do número é aviso
    perdido, e a mutação 23 prova que o portão vê.

12. **BANCADA E MUTAÇÃO.** `teste-produto.php`: **306 afirmações, 0 falha**, uma página por processo.
    `teste-casca.php` foi de **744 para 1024** verificações — as oito entraram nos trinta e tantos
    portões que valem para toda página da ilha. `mutacoes-produto.py`: **25 de 25 reprovando**, em
    `mkdtemp`. **`git status` conferido e a bancada rodada DE NOVO depois da bateria**, pela regra que
    a `mutacoes-par.py` escreveu com sangue hoje de manhã.

13. **O QUE ESTE BLOCO NÃO FEZ, dito para ninguém procurar depois:** não mediu a SERP de cada consulta
    nova — o canal devolve página de **busca interna** de varejista em vez do top 10 orgânico, e as
    oito publicam pelo veredito **herdado do recorte**, o que está escrito no `ESTADO.md` como a
    seção 2 do despacho autoriza. E não avisou o Search Console: `GOOGLE_SA_B64` segue **ausente** do
    ambiente desta rotina, pela **sétima** execução seguida, e está em `dados/despachos.md` desde
    07/10.

14. **O DESEMBARQUE DERRUBOU O GUIA, E O PORTÃO PEGOU — o defeito mais caro desta execução foi meu, não
    do despacho.** O Sync foi acionado com `forcar=1`, que reaplica **todos** os snippets e não só os que
    mudaram. O Sync grava cada um inativo e reativa em seguida, e o Code Snippets **recusou reativar o
    Guia**: `gravado (#13) mas NÃO ativado: o código não passou na validação`. A causa está escrita no
    próprio Sync, linha 326 — `activate_snippet()` executa o código, e o snippet **já estava carregado
    naquela requisição**. Oito dos nove reativaram.
    **O EFEITO NO AR era casca sem miolo:** `/materiais/acabamento/` e as três filhas seguiram
    respondendo **200**, com `<title>`, trilha e `canonical` certos, e no lugar do corpo o shortcode
    **CRU** `[cdm_guia_acabamento]`, sem `<meta name="description">`. **200 não é sinal de página viva**,
    e esta é a terceira vez que esta ilha paga por isso — as duas anteriores foram a página de
    estacionamento da HostGator.
    **QUEM PEGOU: o `conferir-no-ar.py`**, com **2 falhas em 524 afirmações**, e a segunda nomeou as
    quatro URLs. Se eu tivesse fechado a execução no `200` das oito páginas novas, quatro páginas do Guia
    ficariam vazias no ar sem ninguém ver.
    **O CONSERTO:** manifest à revisão **73** e Sync acionado. Na falha de ativação o Sync faz `return`
    **antes** de gravar o sha do item (linha 342 contra 355), então `snippet:guia` ficou **sem sha** — e é
    isso que um sync comum reaplica; com o Guia já **inativo**, `activate_snippet()` executa num mundo em
    que as funções dele não estão carregadas, e a validação passa. O sync comum não rodou de primeira
    porque ele sai cedo quando a revisão do manifest é igual à gravada (linha 472) e a revisão 73 ainda
    não havia propagado no `raw.githubusercontent.com`; com o Guia já caído, `forcar=1` resolveu.
    **CONFERIDO NO AR:** as quatro servem `cdm-guia` no corpo, **uma** `description` cada e **zero**
    shortcode cru. **O código do Guia não foi tocado** — os nove snippets passam no `php -l`, passam no
    wrap `if(false){...}` que o Code Snippets usa para validar, e as funções dos nove estão **todas**
    guardadas por `function_exists`. Está em `dados/consertos.md` para a ronda seguinte reconferir, e
    virou **aviso de topo** no `PROMPT.md`.

15. **O SEGUNDO VERMELHO DO MESMO PORTÃO ERA FONTE NOVA, NÃO LINK ESTRANHO:** `[afiliado] todo encurtador
    de Shopee servido está no banco` acusou **58 estranhos de 76 servidos**. Ele montava o banco de links
    **só** de `materiais-*.json`, e os 58 vêm de `vitrine-de-produto.json`, que nasceu hoje. **O portão
    estava certo em acusar** — ele não conhecia a fonte. A fonte entrou nele; **a exigência não saiu**,
    que é a diferença entre ensinar o portão e afrouxá-lo. O arquivo é GERADO e tem portão próprio, então
    link que chega nele passou pela regra de relevância e tem `sub_id_1` desta ilha.

**PRÓXIMO PASSO DESBLOQUEADO:** a ilha está em **29 URLs** e o piso da 21.1 pede **40** — faltam
**11**. O teto da 21.4 estava **SUSPENSO só em 09/10** pelo despacho (2) do Raphael e **volta inteiro
a partir de 10/10**, aqui e em toda ilha. O caminho natural é a **leva de malha** que o Guia já sabe
servir (as categorias `rejuntes`, `pastilhas`, `alicates-e-corte` e `bases` têm banco e esperam a
16.5), e **não** mais páginas de consulta de produto: das 16 consultas, oito publicaram e as outras
oito saíram com causa medida, então esta família está **fechada** até a próxima coleta.

09/10/2026 14h05Z–15h5xZ — OS DOIS PORTÕES DA SEÇÃO 30 ABRIRAM NA MESMA PASSADA, E A MEDIÇÃO DERRUBOU METADE DA LISTA DO PRÓPRIO DESPACHO

Nenhuma URL nova (a ilha segue em **21**), nenhuma leva do teto da 21.4 gasta, nenhum Sync e nenhuma
revisão nova (o `/status` segue na **71**) — este bloco é portão, regra e dado de repositório. Os dois
arquivos de dado nascem `publicar: false` e por isso não viraram option.

1. **OS DOIS COMANDOS DA 29 RODARAM ANTES DE TUDO, e a porta está de pé.** `conferir-no-ar.py`
   **APROVADO com 524 afirmações e 0 falha** (21 de 21 URLs do sitemap em 200, as três da 29.2 em 200,
   caminho inexistente em 404 na página desta ilha). `leitura-do-visitante.py` **REPROVADO com
   EXATAMENTE 1 defeito**: o soft 404 da borda, pendência do Raphael desde 29/09 — vermelho esperado,
   com dono escrito. **Zero defeito novo.** Rede pela 20.2: 200 nas TRÊS passadas, com
   `aquametria.com.br` em 200 nas mesmas.

2. **A ESCOLHA DA ILHA: FOCO, SEM CORRIDA.** `foco.md` nomeia a **clubedomosaico** desde 24/09, então
   pela 1.2 não houve rotação a aplicar. `executando_desde` estava **null**, que pela 1.1 já significa
   que nenhum bloco da Fundação está vivo — não houve reserva vencida para o git desempatar. Os
   commits de 13h40Z a 13h44Z na pasta da ilha eram **inserção de despacho**, não bloco. Reserva
   escrita às **14h05Z** e aceita de primeira.

3. **O PORTÃO COMERCIAL DA 30.2 ABRIU, E ERA ELE QUE TRANCAVA AS OITO PÁGINAS.** As 16 consultas do
   item 2 foram colhidas uma a uma na **API de afiliado da Shopee** — a credencial **já estava** no
   ambiente desta rotina, ao contrário da `GOOGLE_SA_B64` —, 20 ofertas por consulta. **OITO abrem o
   portão** com 3+ produtos reais e número próprio **calculado**: torques 19 ofertas (R$ 68,99 a
   R$ 248,25), cortador de vidro 9, espelho 9, alicate 5, **pastilhas 5 com PREÇO POR PASTILHA** (a
   única consulta em que o anúncio declara quantidade), pastilha de vidro 5, base de MDF 3, rejunte 3.

4. **A MEDIÇÃO DERRUBOU OITO DAS DEZESSEIS — e isso é o item 2 obedecido, não contrariado**, porque ele
   mandava *"tira o que a medição derrubar"*. **CINCO são ARMADILHA dentro da Shopee**, e é sempre a
   mesma causa: no vocabulário de lá a palavra `mosaico` pertence ao **quadro decorativo de várias
   placas** e ao **papel de parede que imita azulejo**, não ao caquinho. `tela`, `mandala` e `kit
   mosaico` devolveram 20 de 20 em quadro; `azulejo`, 20 de 20 em papel de parede na primeira leitura;
   `material`, quadro mais **FORMA 3D de gesso** — molde de ABS para fundir placa que *imita* mosaico,
   família que nenhum documento desta ilha tinha visto. **Duas delas o PROMPT.md já listava como
   armadilha desde 10/09, medidas no Google: a armadilha é a MESMA dentro da loja.** **TRÊS são
   intenção de LOJA** (`vaso`, `colar` e o próprio `azulejo` devolvem peça acabada, que é o que a
   artesã vende — afiliado ali mandaria o visitante comprar de um concorrente dela). **UMA sai por
   canibalização da 30.4** (`pinça` devolve o mesmo alicate de duas consultas irmãs).

5. **O ENSAIO DA 25.3 ACHOU O DEFEITO, E ELE ERRAVA NOS DOIS SENTIDOS NA MESMA CONSULTA.** A regra não
   cortava **plural**: `exige: pastilha` não casava com *"Kit com 900 **Pastilhas**"* e `recusa:
   adesivo` não casava com *"Kit 5 **Adesivos**"*. Em `pastilhas para mosaico` os **CINCO kits de
   verdade eram recusados** e **DUAS ofertas — uma de obra, uma de adesivo — eram aceitas**. Corrigido
   com o corte nos **dois lados** da comparação. Gravar sem ensaiar faria a página de maior intenção de
   compra nascer servindo revestimento de lavabo.

6. **A COLETA CONTRADISSE O QUE EU JÁ TINHA ESCRITO, e a prosa cedeu ao número em três lugares.** Eu
   havia declarado o `rejunte` fora do portão por ter só 2 ofertas e **servem 3** — passou a publicar,
   com o dado **FINO** dito com essas palavras. E `azulejo`, `mandala` e `vaso` tiveram a prosa
   reescrita porque a coleta gravada trouxe outro conjunto que a primeira leitura. A causa está medida
   e virou linha no topo da declaração: **a API devolve conjuntos DIFERENTES entre chamadas**, então o
   número de uma consulta é o de **uma coleta datada** e nunca o catálogo da Shopee.

7. **O PORTÃO DA SERP ABRIU PELA RÉGUA DA 30.5, E FOI CALCULADO EM VEZ DE REESCRITO.**
   `recalibrar-30-5.py` classifica cada **ocupante** do top 10 já medido nos três tipos que a 30.5
   manda contar contra os dez que ela manda não contar, e chama `dominado` **6 ou mais das 10 vagas**.
   `pastilha/vidro` **TOMADA → ABERTA** (1 de 10 contam), `pastilha` → **ABERTA** (2 de 10),
   `alicate/torques` → **ABERTA** (1 de 10). O cruzamento foi de `espera_autoridade` **3 para ZERO** e
   `pode_nascer` **8 para 11**. Remedir cinco vereditos à mão seriam cinco chances de puxar o resultado
   para o lado de quem quer publicar — e quem remedia era a mesma execução que queria as páginas.

8. **QUEM FAZ O "ANTES DE VALER" ACONTECER É UMA FUNÇÃO, e sem ela nada disso valeria.**
   `classe_que_vale()` no cruzamento prefere `classificacao_30_5` quando ela existe; `classificacao`
   fica **intacta** e é procedência. Sem essa função a recalibração seria um campo bonito que nenhum
   portão lê — a família de defeito mais paciente desta ilha.

9. **A PARTE QUE NÃO ME BENEFICIA, escrita de propósito.** **DUAS** das cinco medições TOMADA **não**
   foram remedidas: são **pergunta de embalagem com intenção de obra**, não nome de produto, e a 30.5
   fala de consulta de produto. Uma delas continuaria TOMADA de todo jeito — Telhanorte com 4 páginas,
   Extra com 3 e MadeiraMadeira com 2 são **nove vagas de varejo grande**. Na mesma disciplina,
   `Pastilhart` foi classificado como fabricante que **CONTA** mesmo sendo de nicho, e `Culturamix`
   como **fazenda de conteúdo**: as duas leituras pesam **contra** publicar.

10. **A BATERIA DE MUTAÇÃO ACHOU TRÊS TRAVAS QUE A BANCADA NÃO MEDIA, e uma era um ramo REDUNDANTE da
    própria regra.** A **m05** mostrou que tirar o ramo do grupo de exigência vazio **não mudava o
    veredito**, porque o ramo seguinte derrubava igual. O conserto **não foi apagar o ramo**: foi dar a
    ele um **diagnóstico próprio** — grupo vazio é **declaração quebrada**, não anúncio que não casou, e
    as duas coisas não podem sair com a mesma cara. A **m06** pegou uma fixação que **parecia medir e
    não media**: `tela` dentro de `telha` não é substring; `cola` dentro de `colar` é. **BANCADA 72
    afirmações, 0 falha. MUTAÇÕES 10 de 10 reprovando.** E a bateria trabalha em `mkdtemp` — o aviso do
    topo do `PROMPT.md` obedecido no mesmo dia em que foi escrito.

11. **ONZE SHA VENCIDOS NO MANIFEST**, achados de passagem e consertados, **com os nomes gravados
    porque escrever o sha novo apaga o sinal**: `corpus-buscas`, `cruzamento-14-9` (dado e ferramenta),
    `serp-das-filhas`, `materiais-rejuntes`, `materiais-alicates`, `filhas-do-guia` (dado, md e
    ferramenta), `filhas-do-guia-md`, `mutacoes-cobertura` e `mutacoes-par`. Mesma família que a entrada
    de `perguntas-do-guia` nomeou em 08/10 com **nove**.

12. **DADO DE UMA FONTE SÓ, dito na cara.** O Mercado Livre respondeu **403 nas TRÊS passadas**, com o
    CONNECT aceito pelo proxy e o 403 vindo do balanceador dele (`awselb/2.0`, `rps: w403`), enquanto
    `clubedomosaico.com.br` e `shopee.com.br` deram 200 nas mesmas. **Não é a rede da seção 20: é o
    anti-robô deles.** Está escrito no banco para nenhuma página dizer "o mercado" querendo dizer "a
    Shopee".

13. **DEPOIS DE FECHAR A EXECUÇÃO EU PISEI NO PRÓPRIO PÉ, e quem viu foi uma CONTAGEM e não um
    portão.** Rodei `--gravar --so torques-para-mosaico --sem-link` para atualizar uma linha de prosa
    do arquivo gerado, e isso **substituiu o bloco daquela consulta por uma coleta nova sem link**: os
    **19 links de afiliado** da página de maior intenção de compra da ilha sumiram do banco **em
    silêncio**. Se eu não tivesse contado por outro motivo, o despacho reescrito estaria prometendo à
    próxima execução que *"o link de afiliado já está gerado nas oito"* — e na do torquês não estaria.
    **Promessa de banco escrita em prosa e desmentida pelo banco é a família de defeito que esta ilha
    mais paga.** Links restaurados (58 no total, as oito consultas com link em todos os anúncios que
    servem), e o conserto é **falha fechada e não cuidado**: recoleta de consulta que já tem link
    agora **RECUSA** `--sem-link`, nomeando quantos links seriam apagados, e exige escolher entre
    regerar e `--descartar-links`. Provado que morde — a mesma linha que causou o estrago agora sai com
    `RECUSADO` e o banco fica intacto.

14. **E A MESMA CONTAGEM MOSTROU UMA AMBIGUIDADE que ia enganar a próxima execução:**
    `resumo.abre_o_portao_da_30_2` diz TRUE em **ONZE** consultas e apenas **OITO** publicam, porque
    ele é só o portão de **DADO**. As três diferenças são `pinça` (canibalização da 30.4), `azulejo` e
    `colar` (intenção de LOJA). O arquivo gerado passa a dizer isso no próprio cabeçalho, com os três
    nomes: **contar só o portão é publicar três páginas que a própria ilha decidiu não ter.**

**O QUE NÃO SAIU, e o despacho (3) foi REESCRITO pela 18.3 deixando só isto: a CASCA.** Faltam os itens
1, 4, 6 e 7 do original, e os quatro são a **mesma obra** — uma régua nova no motor do Guia que
renderize página de consulta de produto, com bancada e mutação. Esta passada abriu os dois portões e
**não alcançou `snippets/`**. A tabela das **oito páginas elegíveis**, com faixa de preço e número
próprio de cada uma, está no `PROMPT.md` para a próxima execução não remedir nada.

**PRÓXIMO PASSO DESBLOQUEADO:** a régua de página de consulta de produto no motor do Guia, e ela começa
sem nenhuma pergunta aberta de dado — as oito páginas têm os dois portões verdes, o número próprio
calculado e o link de afiliado já gerado. **Duas delas (`base-de-mdf` e `rejunte`) nascem no limite,
com exatamente 3 ofertas**, e isso está escrito para não ser descoberto no ar.

---

09/10/2026 13h1xZ — O PORTÃO DA 14.9 FECHOU A PROPOSTA 3 NA PRIMEIRA PERGUNTA, E A MESMA PASSADA ACHOU A FILA PROMETENDO, OUTRA VEZ, UM CAMINHO QUE A PRÓPRIA ILHA JÁ MEDIU E FECHOU

Nenhuma URL nova (a ilha segue em **21**), nenhuma leva do teto da 21.4 gasta, nenhum Sync e nenhuma
revisão nova (o `/status` segue na **71**) — este bloco é régua e dado de repositório, não option.
**Cinco arquivos mudaram e o `git status` não nomeou nenhum sexto.**

1. **OS DOIS COMANDOS DA 29 RODARAM ANTES DE TUDO, e a porta está de pé.** `conferir-no-ar.py`
   **APROVADO com 524 afirmações e 0 falha** (21 de 21 URLs do sitemap em 200, as três da 29.2 em
   200, caminho inexistente em 404 na página desta ilha). `leitura-do-visitante.py` **REPROVADO com
   EXATAMENTE 1 defeito**: o soft 404 da borda — origem 404, borda 1ª leitura 404 e 2ª 200, com
   `x-proxy-cache HIT` e `max-age=7200`. É a pendência do Raphael desde 29/09, vermelho esperado com
   dono escrito. **Zero defeito novo.** Rede pela 20.2: `clubedomosaico.com.br` em 200 nas TRÊS
   passadas, com `aquametria.com.br` em 200 na mesma.
2. **A PROPOSTA 3 FOI AO PORTÃO E PAROU NA PRIMEIRA PERGUNTA — E O CRITÉRIO ERA PRÉ-REGISTRADO.** O
   `ESTADO.md` de 11h5xZ escolheu o bloco e escreveu, **antes de qualquer medição**, que se a SERP
   viesse TOMADA a execução pararia ali. Veio TOMADA. **Parou ali.** Três passadas, com quem ocupa
   escrito pelo nome, em `dados/corpus-buscas.md` (cluster 2).
3. **A LINHA QUE DECIDIU NÃO É O TERMO GORDO: É O MOSAICO.** `quadro divino espirito santo mosaico
   artesanal` devolveu OLX, Mercado Livre, Magazine Luiza, Casas Bahia, Extra, agregador de Shopee e
   Holyart IT — e a **Casas Bahia vende um `Mosaico do Espírito Santo com anjos 120x140cm` por
   R$ 6.872,40, na primeira página**. Não é o caso de `vaso de mosaico`, em que a SERP devolve
   cerâmica lisa e sobra brecha; aqui o varejo já serve **exatamente** o produto, com preço e
   parcela. Zero página editorial em dez.
4. **E A CONSULTA NUA — A QUE TEM AS 4 IMPRESSÕES — NÃO PÔDE SER MEDIDA, e isso vale mais que o
   "não".** `quadro divino espirito santo` devolveu PDF de reza da UNEMAT, iconografia da UFMG, lição
   de EBD, Scripta Theologica ES, EWTN ES, coromoto.it e a arquidiocese de Toronto. **Nenhum
   resultado comercial e nenhum de mosaico.** As 4 impressões em 39,2 vêm de uma consulta cuja
   primeira página é de **devoção, não de compra** — subir nela levaria a peça da artesã para uma
   SERP de reza. O endereço não é difícil: é o lugar errado.
5. **O QUE SOBROU VIVO NÃO É A PROPOSTA 3, E NÃO FOI CHAMADO DE PROPOSTA 3 CUMPRIDA.** A consulta de
   **método** (`como fazer quadro do divino espirito santo em mosaico de caquinho passo a passo`)
   mediu **ABERTA** — top 10 de PDF escolar, matéria de 2026 sobre piso de caquinho e tutorial sem
   número. Mas é **outra consulta**, sem faixa e sem impressão, e o critério de pronto da proposta era
   `quadro divino espirito santo` entrar na banda 11 a 20. Chamá-la de cumprida seria critério dobrado
   para caber no dado que veio (1.2-b.4). Virou pedido de faixa ao Raphael e candidata do bloco 5 (os
   doze tutoriais-âncora, que já têm *quadro* na lista).
6. **DEPOIS DE PARAR, A MESMA RÉGUA FOI APONTADA PARA A FILA — E A FILA ESTAVA MENTINDO DE NOVO, 24
   HORAS DEPOIS DE SER CONSERTADA.** A tabela de 09/10 manhã imprimia, para a `alicate`:
   *"Medir uma consulta nova para uma delas é a coisa mais barata que existe nesta categoria."* No dia
   em que essa frase nasceu, o **mesmo arquivo que a régua lê** já guardava **CINCO** medições
   `NAO_MEDIDA` de consulta própria nessa categoria — quatro do `alicate/cortador_de_azulejo` (30/09 e
   07/10) e uma da `pergunta:alicate-espessura-de-corte`. **`NAO_MEDIDA` custava ZERO na conta do
   custo.** É a mesma família de ontem, uma camada acima: lá o custo infinito estava em prosa numa
   pendência de banco; aqui estava em dado, no arquivo que a régua abre, e a régua não o somava.
7. **E O ARQUIVO JÁ DIZIA POR QUE ELAS FALHAM, COM DOIS DIAS DE IDADE.** O
   `limite_5_consulta_que_pede_a_medida`, de 07/10, fecha com todas as letras: *"a consulta-alvo de
   uma filha NUNCA pede o número."* A pergunta desta categoria carrega como **assunto** exatamente o
   número (`espessura_maxima_de_corte_mm`). **ESTA EXECUÇÃO GASTOU TRÊS PASSADAS PARA REDESCOBRIR
   ISSO** — as três pediam o milímetro na frase e as três desviaram. Está escrito aqui porque é o
   mesmo defeito que a 20.2 nomeia: **bloqueio herdado de DOCUMENTO também se reteste antes de ser
   respeitado — e também se LEIA antes de ser repetido.** Quatro execuções já anotaram "esbarra no
   egresso" sem abrir a fonte que estava em casa; esta anotou o avesso, e abriu a fonte depois de
   gastar a medição.
8. **MAS AS TRÊS PASSADAS NÃO FORAM PERDIDAS: UMA DELAS ACHOU UM LIMITE QUE NÃO EXISTIA, E ELE NÃO É
   DESVIO DE PAÍS.** Nasceu o **`limite_6_homonimo_intra_portugues`**: `pastilha` ao lado de `corte`
   ou `espessura` é, em português do Brasil, o **inserto de usinagem** — `pastilha de corte por
   fresagem`. A SERP saiu ferramentaria industrial, com Hoffmann Group e RS Online publicando mm de
   capacidade de corte de **fio de eletrônica**. **Nenhuma âncora de artesanato desfaz isso, porque
   não há país errado a consertar:** o resultado é brasileiro e português e é de outro assunto. Os
   limites 4 e 5 não cobriam este caso. A regra prática que fica: para medir corte nesta ilha a
   consulta nomeia `caquinho`, `azulejo` ou `tessela`, **nunca `pastilha`**, e não pede milímetro.
9. **A FECHADURA É DERIVADA, E AQUI NÃO SE DIGITOU UM NÚMERO.** Ontem a fechadura precisou de dois
   campos novos escritos à mão (`fechada_por_canal`, `recortes_fechados`). Hoje não precisou de
   nenhum: a tentativa falhada **já é dado**, com data e motivo, no arquivo que a régua abre.
   `tentativas_que_falharam()` deriva e `mae_pode_nascer()` divide o custo em **três** ramos — ninguém
   tentou (a promessa barata fica), uma tentou (promete a outra e **nomeia a fechada com um "não
   tente"**), todas tentaram (a promessa barata **morre** e sobra ITEM DE BANCO ou PERGUNTA NOVA,
   apontando o limite 5). A `alicate` saiu de *"a coisa mais barata que existe"* para **8 tentativas
   medidas e falhadas, nomeadas uma a uma com data**.
10. **FALHA-FECHADA NOVA, e ela é sobre o próprio conserto:** `NAO_MEDIDA` **sem motivo escrito**
    passa a reprovar o `--conferir`. Fechar caminho sem dizer por que é pior que não fechar — a
    execução seguinte não teria como saber se a consulta era ruim ou se o canal não alcança. Medido:
    apagando um motivo em memória, o portão acha 1; no disco, 10 de 10 têm motivo.
11. **E A TENTATIVA DO VIZINHO NÃO CONTA COMO DA PERGUNTA.** A pergunta herda a **classe** da consulta
    compartilhada (é o que a correção de 07/10 estabeleceu), e não pode herdar a **falha** de uma
    consulta que não é dela — senão o conserto fecharia caminho por contágio e o erro teria só trocado
    de lado. Tem caso próprio na bancada.
12. **NENHUM VEREDITO MUDOU, e isso é a confirmação e não um consolo.** O diff do
    `cruzamento-14-9.md` tem **zero** linha de `veredito`, zero linha de recorte e zero linha de
    pergunta alterada: 42 recortes, `pode_nascer` 8, `espera_autoridade` 3, `sem_nenhum_dos_dois` 31,
    iguais aos de manhã. **A próxima mãe do Guia continua sendo a `rejunte`**, a 1 filha. A régua não
    afrouxou nem apertou portão nenhum — ela parou de **recomendar** o caminho que a ilha já mediu
    como fechado. Mesma assinatura do 0 de 42 de ontem.
13. **O CUSTO DA PRÓXIMA FILHA NUNCA TINHA SIDO MEDIDO POR NADA, e era a frase que ESCOLHE o bloco.**
    Os 46 casos do autoteste cobriam as 4×5 combinações do veredito, a 16.5 e as perguntas — **e nem
    um deles tocava `o_que_a_proxima_filha_custa`**. É por isso que ela mentiu duas vezes em dois dias
    sem nada acusar. Agora tem **6 casos**, e o primeiro deles é o **mundo sem tentativa falhada como
    controle do experimento**: lá a frase antiga é a certa e tem de continuar saindo, senão o conserto
    teria virado uma trava sobre tudo. Bancada em **52 casos, 0 falha** (eram 46).
14. **O FIXTURE GANHOU O CAMPO QUE O REAL TEM.** `_medicao()` não escrevia `motivo` nem `medida_em`, e
    o portão novo lê os dois. Mundo fabricado sem a forma do mundo medido é verde sobre nada — foi
    exatamente o defeito que a bancada de ontem achou nos três `.md`.
15. **A RESSALVA SAIU DO JSON PARA O `.md`, DENTRO DO QUE O `--conferir` COMPARA.** Nasceu a seção
    **"O QUE JÁ FOI MEDIDO E FALHOU — não repita a consulta"**, com categoria, candidata, contagem e
    **a consulta de cada tentativa com a data**. A lição é a do item 7 de ontem: ressalva que mora só
    no JSON não viaja com o número, e quem escolhe bloco lê o `.md`. Aqui vale mais ainda, porque o
    que essas linhas dizem é literalmente "não tente de novo".
16. **O DESPACHO DE 07/10 FICA INTEIRO, retestado e não herdado (18.4).** `env | grep -c GOOGLE_SA`
    devolve **0** e `search-console.py --ilha clubedomosaico` devolve *"Sem credencial"*. **Quinta
    execução a medir em vez de copiar a frase** — e está escrito no `PROMPT.md` que, daqui em diante,
    cinco medições idênticas não são cinco informações: a próxima mede uma vez e segue.
17. **BANCADA.** `cruzamento-14-9.py --autoteste` **52 de 52**; `--conferir` **aprovado**, com a
    afirmação nova ("toda medição NAO_MEDIDA diz por que falhou", 10 medidas);
    `filhas-do-guia.py --autoteste` **53 de 53** e `--conferir` aprovado nas quatro afirmações;
    `validar-banco.py` **OK** e `validar-pastilhas.py` **OK, 0 item com falha**. Nenhum snippet PHP
    foi tocado e nenhum arquivo de banco mudou — `teste-f2`, `teste-tecnicas`, `teste-casca` e
    `teste-guia` foram rodados de todo jeito, pela lição do item 13 de hoje (a bancada roda DEPOIS,
    nunca só antes), e o `git status` nomeou **exatamente** os cinco arquivos deste bloco.
18. **O QUE ESTE BLOCO DEIXA DESBLOQUEADO, e é a fila consertada que decide.** A `rejunte` continua a
    **1 filha por consulta**, e o custo dela é **ITEM DE BANCO ou PERGUNTA NOVA** — não é medir SERP,
    porque toda candidata com dado verde dela já tem consulta aberta própria, e `acrilico` e `epoxi`
    estão fechados por canal desde 08/10. A `alicate` **não é mais o caminho barato** e agora diz por
    quê, com oito datas. Antes de escrever consulta nova em qualquer categoria: a consulta-alvo de uma
    filha **não pede o número** (limite 5) e **não diz `pastilha` perto de `corte`** (limite 6).

09/10/2026 10h5xZ — A RÉGUA QUE ESCOLHE O BLOCO ESTAVA MENTINDO, E ELA JÁ TINHA MANDADO UMA EXECUÇÃO COLETAR O QUE ESTA ILHA MEDIU COMO IMPOSSÍVEL

*(Esta entrada tem uma SEGUNDA METADE, fechada às 11h5xZ e commitada depois do primeiro push: a
verificação do próprio bloco — as baterias de mutação rodadas depois do commit — achou DOIS defeitos
que não eram do bloco, e um deles ia para o ar. A reserva foi reescrita para 11h30Z pela 1.1 antes de
mexer em qualquer coisa. As duas metades estão abaixo, na ordem em que aconteceram.)*

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h16Z**, push da reserva aceito na primeira
tentativa (`232c0a1`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com `executando_desde:
null`, que pela **1.1** já basta — e o último commit na pasta era de **19h47Z de ontem**, quinze horas
atrás. `git fetch origin main` trouxe `0758d62..1245e2a` (forçada do lado do remoto); a branch
`claude/dreamy-mccarthy-vevxx3` estava **idêntica ao `main`**, zero commits de diferença, e não havia PR
aberto — nada a mesclar. Pela **18.1** nenhuma outra ilha tem despacho **ALTO** em ilha no ar e quebrada,
que é a única coisa que fura o foco.

**A REDE PELA 20.2, retestada e não herdada:** `clubedomosaico.com.br` em **200 nas três passadas**, com
`aquametria.com.br` em 200 na mesma passada.

**A PORTA DE ENTRADA ESTÁ DE PÉ, e os dois comandos da 29 rodaram antes de qualquer coisa, como o
`PROMPT.md` manda.** `conferir-no-ar.py` **APROVADO: 524 afirmações, 0 falha** — 21 de 21 URLs do sitemap
em 200, as três da 29.2 em 200 e caminho inexistente em 404 na página desta ilha. O reparo de ontem às
19h2xZ **segurou**. `leitura-do-visitante.py` fechou **REPROVADO com EXATAMENTE 1 defeito**, o soft 404 da
borda do hospedeiro — pendência do Raphael desde 29/09, vermelho esperado e com dono escrito. **Zero
defeito novo.**

**Nenhuma URL nova** (a ilha segue em **21**), **nenhuma leva do teto da 21.4 gasta** e **nada publicado no
site**: este bloco é régua e dado de repositório, não option, então não houve Sync nem revisão nova — o
`/status` segue na **71**.

## O BLOCO QUE A FILA MANDAVA FAZER ERA PROIBIDO POR ESTE MESMO ARQUIVO, E A CONTRADIÇÃO TEM UM DIA DE IDADE

O item 14 do `bloco_atual` de ontem diz, com todas as letras, que o próximo bloco é **ITEM DE BANCO**:
*"a `alicate` está a UMA filha das três da 16.5, e essa filha é `alicate/martelinho` com TRÊS itens a
coletar — derivado em `caminho_mais_barato_para_as_3_filhas`, **não escolhido por mim**"*. O `PROMPT.md`
repete isso em três lugares.

**E o `PROMPT.md` também diz, três vezes, para NÃO fazer isso.** Em **07/10/2026** — um dia antes — a
execução que varreu Cortag e Vonder fechou `alicate/martelinho` e `alicate/pinca_mosaico` como
*"coleta IMPOSSÍVEL neste canal"*, com a pendência `martelinho-e-pinca-nao-tem-fabricante-neste-canal`, a
frase *"Não busque outra vez em Cortag e Vonder"* e a instrução *"não reabrir `martelinho` nem
`pinca_mosaico` (medidos e fechados hoje)"*.

**NENHUMA DAS DUAS EXECUÇÕES FOI DESATENTA, E É ISSO QUE IMPORTA.** A de 08/10 fez exatamente o que esta
ilha manda fazer: em vez de escolher de cabeça, leu um campo **derivado** —
`resumo.por_categoria_do_guia.alicate.caminho_mais_barato_para_as_3_filhas` de
`dados/filhas-do-guia.json` — e o campo respondia `faltam_filhas: 1`, `itens_de_banco_a_coletar: 3`, em
`alicate/martelinho`. **O menor número do arquipélago inteiro.** O campo estava derivado e estava errado,
porque custo infinito escrito em PROSA entra numa lista ordenada por custo como se fosse zero.

## AS DUAS METADES ERRADAS, as duas com número

**(1) O CUSTO NÃO É 3 ITENS, É INFINITO NESTE CANAL — e ficou medido por um canal a mais do que em 07/10.**
Duas passadas novas, escritas de forma diferente, nenhuma carregando o valor que se queria confirmar
(seção 8): a primeira pediu os **rótulos** da ficha em `cortag.com`, `cortag.com.br`, `vonder.com.br` e
**`tramontina.com.br`** — e a Tramontina é um fabricante que a varredura de 07/10 **não tinha olhado**, ou
seja é exatamente o *"fabricante NOVO"* que o campo `o_que_mudaria_isto` pedia. O que ela publica é
`Martelo Pedreiro 2 Cortes 500 g` (SKU 40458000), que não nomeia mosaico, pastilha nem tessela. A segunda
pediu os nomes da ferramenta de verdade — `martelina`, `tagliolo`, `bigorna`, `tessela` — nos dois
fabricantes do banco mais Tramontina, Starrett, Lee Tools e Momfort: **zero produto com qualquer um desses
nomes nos seis domínios**. E uma terceira, **sem restrição de domínio**, procurando fabricante brasileiro
de martelina para mosaico, devolveu ateliê de mosaico, matéria de jornal e vendedor italiano de eBay —
**nenhum fabricante brasileiro, nenhuma ficha**. A causa de 07/10 fica medida por um canal a mais e por
dois nomes a mais, e **não é de coleta**: a martellina com o tagliolo é ferramenta artesanal de
mosaiquista, e a declaração de fabricante que o portão exige não é publicada por ninguém nesse mercado.

**(2) A `alicate` NÃO ESTAVA A UMA FILHA, ESTAVA A DUAS — e quem já dizia isso era o outro arquivo.** A
correção de **07/10** está escrita no `cruzamento-14-9.md`: *"a 16.5 se fecha por CONSULTA, não por
recorte"*. Contado por consulta, a `alicate` tem **UMA** filha, não duas: `alicate/torques` está em
`espera_autoridade` (a SERP dele é **TOMADA** desde 05/10) e a `pergunta:alicate-espessura-de-corte` mira
a **mesma** consulta do `alicate/cortador_de_azulejo`. **Duas páginas na mesma consulta não são duas
filhas.** O `caminho_mais_barato` contava **tipo com dado verde**; a 16.5 conta **consulta aberta**. São
perguntas diferentes, e só uma delas decide se a mãe nasce.

## O CONSERTO: A FECHADURA DEIXOU DE SER PROSA, E A FILA MUDOU DE ARQUIVO

**`dados/materiais-alicates.json`** — a pendência de 07/10 ganhou dois campos **lidos por máquina**:
`fechada_por_canal: true` e `recortes_fechados: ["alicate/martelinho", "alicate/pinca_mosaico"]`, com o
motivo de os dois existirem escrito ao lado deles. Prosa não é lida por máquina nenhuma, e foi o silêncio
dessa fechadura que gastou a execução de ontem.

**`ferramentas/filhas-do-guia.py`** — `recortes_fechados_por_canal()` varre os `materiais-*.json` e lê as
fechaduras; `fechados_de_bancos()` é a metade **pura** dela, separada do disco para a bancada poder
fabricar a pendência malformada. O caminho mais barato **exclui** os recortes fechados e, quando sobram
menos tipos abertos do que filhas faltando, responde `IMPOSSIVEL por tipo NESTE CANAL` **nomeando a
pendência e o arquivo dela**. **FALHA-FECHADA nas duas direções:** pendência que declara
`fechada_por_canal` sem nomear recorte **explode**, e recorte nomeado que não existe no vocabulário do
esquema **explode no `montar`** — porque um `alicate/martelino` com typo deixaria de proteger **em
silêncio**, que é a mesma família de defeito que a função existe para fechar.

**E A RESSALVA PASSOU A VIAJAR COLADA NO NÚMERO.** Todo `caminho_mais_barato_para_as_3_filhas` agora tem,
ao lado, `o_que_este_caminho_NAO_decide`: *"ESTE NÚMERO É POR RECORTE DE TIPO E É UM PISO, NUNCA A CONTA
DA 16.5 … Escolher bloco só com o número daqui já custou a execução de 08/10/2026."* Era a **ausência**
dessa frase, no JSON, que deixou `faltam_filhas: 1` ser lido como "a 16.5 está a uma filha". **E a seção
inteira do caminho mais barato, que até hoje morava SÓ no JSON, passou a sair no `.md`** — com a ressalva
em citação em cima da tabela, dentro do que `--conferir` regera e compara.

**`ferramentas/cruzamento-14-9.py`** — a pergunta *"qual é o próximo bloco"* não tinha resposta honesta em
arquivo nenhum, e passou a ter no único arquivo com as **duas** metades. Cada categoria ganhou
`filhas_que_faltam_por_consulta` e `o_que_a_proxima_filha_custa`, e o `.md` ganhou **A FILA DAS MÃES**,
ordenada por quanto falta. **O custo não é um número só, de propósito:** filha que falta pode custar **uma
CONSULTA MEDIDA** (quando já existe candidata com dado verde sem consulta própria) ou **ITEM DE BANCO**
(quando toda candidata já tem a sua). Chamar as duas de "falta uma filha" foi o que mandou uma execução
coletar o impossível.

## E A RÉGUA NOVA ACHOU A MESMA ARMADILHA NA CATEGORIA SEGUINTE, NO MESMO COMMIT

**Com o `martelinho` fora do caminho, a tabela que a própria régua acabou de gerar pôs a `rejunte` no
topo: "faltam 2 filhas, 4 itens a coletar em `rejunte/acrilico` (2) e `rejunte/epoxi` (2)". E essa coleta
também está medida e fechada, desde 05/10.** Está no `PROMPT.md` com estas palavras: *"AS DUAS FILHAS QUE
FALTAM NO `rejunte` NÃO ESTÃO A UMA COLETA DE SKU, E O BLOQUEIO TEM NOME NOVO: É ÍNDICE DE BUSCA, NÃO
EGRESSO. **NÃO REPITA A COLETA.**"* — com sete portas medidas em três passadas: `www.quartzolit.weber` em
**403**, sete domínios de fabricante em `000` por falha de **DNS** (inclusive por WebFetch, `ENOTFOUND`),
as três escapatórias (`web.archive.org`, `r.jina.ai`, `docs.google.com`) fechadas, e o espelho da Telha
Norte sem como ser navegado — arquivo por nome conhecido, 14 documentos, nenhum de acrílico nem de epóxi.
**A causa não é de coleta:** a faixa de junta mora em **boletim técnico**, e boletim técnico é o que este
canal não indexa. Foi essa a diferença medida contra a `acabamento`, que saiu de zero por busca porque
Acrilex, Coral e Suvinil publicam a declaração na própria página de produto.

**Então os DOIS menores números do arquipélago eram canais fechados, não um.** `alicate/martelinho` (3
itens) e `rejunte/acrilico` + `rejunte/epoxi` (4) — o primeiro e o segundo lugar da lista ordenada por
custo. Nasceu a pendência `rejunte-acrilico-e-epoxi-por-tipo-nao-fecham-neste-canal` em
`dados/materiais-rejuntes.json`, com `fechada_por_canal` e `recortes_fechados`, e a `rejunte` passou a
responder `IMPOSSIVEL por tipo NESTE CANAL` também. **Uma régua que só tivesse consertado o martelinho
teria mandado a próxima execução coletar rejunte.**

## A FILA QUE SAIU DA RÉGUA NOVA, E ELA DESMENTE A FILA ANTIGA EM TODAS AS LINHAS

| categoria | filhas por CONSULTA | faltam | o que a próxima filha custa |
|---|---|---|---|
| `acabamento` | 3 | **0** | nada: a mãe está no ar desde 02/10 |
| `rejunte` | 2 | **1** | ITEM DE BANCO ou PERGUNTA NOVA — e as **três** portas estão medidas e fechadas (a coleta por tipo desde 05/10, agora em campo lido por máquina) |
| `alicate` | 1 | **2** | **CONSULTA MEDIDA, não item de banco**: `cortador_de_azulejo` e a pergunta têm dado verde e disputam uma consulta só |
| `apoio`, `base`, `cola`, `pastilha` | 0 | **3** | item de banco ou pergunta nova |

**A `alicate` era anunciada como "a mais barata do arquipélago e a única a UMA filha". Ela é a terceira da
fila, está a duas filhas, e o que ela precisa é de BUSCA, não de coleta.** O tipo que a fila mandava
coletar não aparece mais em caminho nenhum.

## O QUE A PASSADA ACHOU DE PASSAGEM E NÃO GRAVOU, as duas registradas na pendência

**(1) A Cortag publica um `Kit Mosaico` com tabela de especificação** (SKU 61363, EAN 7897451413632, corte
diagonal 11 × 11 cm, espessura de corte 6 mm, largura 15 cm). **Kit não é tipo do vocabulário**, então ele
não fecha filha nenhuma — e quem o gravar um dia lê primeiro o que a Robometria aprendeu com os kits de
filtro: kit declara a composição e não substitui o item avulso.

**(2) A ARMADILHA DE 07/10 FOI RECONFIRMADA PELO AVESSO.** A página de **linha** `Tenazas` serve uma tabela
com *"Espessura de Corte 8 mm"* ao lado dos **três** SKUs 60857, 60858 e 61341 de uma vez, e a própria
leitura devolveu que *"a tabela não deixa claro se os 8 mm valem para os três modelos"*. É número de
**linha**, exatamente como a frase de 5 mm que a pendência `torques-curvo-e-roldanas-podem-ser-o-mesmo`
fechou em 07/10 — e gravar 8 mm no `cortag-torques-mosaico-roldanas` **contradiria** os 5 mm que o mesmo
fabricante declara **por produto**. Não foi gravado.

## O QUE A BANCADA ACHOU DE MIM, E ERA O MESMO DEFEITO QUE A RÉGUA NOVA CONSERTA

Os **três** fixtures de `.md` do `filhas-do-guia.py` **explodiram** na primeira passada, e com a mensagem
certa: eles montam um vocabulário **fabricado** e chamavam `montar()` sem fechadura, então a função ia ler
as pendências **reais do disco** contra um mundo fabricado e a falha-fechada mordia. **A régua nova acusou
o fixture, não o contrário** — mundo fabricado tem fechadura fabricada, e os três passaram a receber
`fechados={}`. É a mesma lição do bloco de ontem, pelo caso 19-b: fixture que não chama a função que ele
mede fica verde sobre um mundo que ninguém escreveu.

## O DEFEITO MAIS CARO QUE ESTA PASSADA ACHOU NÃO É DELA, E ESTAVA NO SNIPPET QUE O SITE SERVE

**Uma bateria de mutações morta por sinal deixa o arquivo MUTADO no repositório, e eu peguei isso
acontecendo.** Quando a bancada foi remedida, o `teste-f2.php` passou de **0 falhas para 3** e o
`teste-tecnicas.php` de **APROVADO para REPROVADO** — sem eu ter tocado em nenhum dos dois. O `git diff`
mostrou a causa em quatro linhas: `snippets/clubedomosaico-f2.php` estava com a **regra 8 movida para
depois da regra 2 e devolvendo `silencio` no lugar de `ambiente_do_substrato`**. É exatamente a troca de
causa que esta ilha mais paga, e é a que o bloco de 07/10 consertou em 29 células.

> **A CULPADA QUE ESTA ENTRADA NOMEOU PRIMEIRO ESTAVA ERRADA, E A CORREÇÃO É DO MESMO DIA.** As duas
> frases acima diziam `mutacoes-f1.py`, porque foi ela que imprimiu "Terminated". **Ela roda em
> `mkdtemp` e não pode sujar a árvore.** Quem sujou foi a **`mutacoes-par.py`, mutação `t03`** — cujo
> docstring é, literalmente, *"A ORDEM TROCA: a regra 8 passa a rodar DEPOIS da 2 … a página passa a
> dizer `o fabricante não fala desta superfície` sobre uma superfície que ele declara"* —, e o texto
> `velho`/`novo` dela é **idêntico byte a byte** ao que estava no disco. Ela está entre as **catorze**
> que trabalham em cima do repositório; `cobertura`, `f1`, `f2` e `rejunte` são as **quatro** que usam
> `mkdtemp`. **A lição é a correção, não o erro:** "toda bateria de mutação é perigosa" é falso e a
> frase verdadeira é derivada — `grep -L 'mkdtemp\|copytree' ferramentas/mutacoes-*.py`.

**O que isso custaria se eu não tivesse remedido:** o arquivo entraria no commit, e o próximo bloco
publicável chamaria o Sync e o site passaria a dizer *"o fabricante não fala desta superfície"* em células
em que ele fala. **O portão que o pegou foi rodar a bancada DE NOVO depois das mutações, não antes** — e
o `git status` foi quem nomeou o arquivo. Restaurado por `git checkout`, e as duas bancadas voltaram a
**0 falha** e **APROVADO**.

**E A CAUSA DE CÓDIGO É DE UMA LINHA: `finally` NÃO RODA QUANDO O PROCESSO MORRE POR SINAL.** A
`mutacoes-par.py` restaura num `finally` e restaura **byte a byte** (ela até confere isso no fim, por
causa da cicatriz de 06/10 sobre o `sha256` do manifest). Mas `timeout` e `pkill` mandam **SIGTERM**, e
SIGTERM encerra o processo sem passar pelo `finally`. **Consertado nesta passada:**
`restaura_em_sinal()` captura SIGTERM, SIGINT e SIGHUP, restaura e sai com `128+N`, que é a convenção
que o `timeout` devolveria.

**E FOI MEDIDO MATANDO A BATERIA DE PROPÓSITO**, no estágio em que ela mexe no snippet (*"A TELA E A
FRASE — quem pega e o render da F2"*): ela imprimiu *"INTERROMPIDA por sinal 15 — os 3 arquivo(s) foram
RESTAURADOS byte a byte antes de sair"*, o `git status` voltou **limpo**, e `teste-f2` (174),
`teste-tecnicas` (139) e `teste-casca` (744) voltaram verdes. **Handler que ninguém viu restaurar não
restaurou nada**, e é por isso que o item da fila para as outras treze manda matar cada uma.

**A METADE QUE NENHUM CÓDIGO RESOLVE fica como regra, porque SIGKILL não é capturável:** depois de rodar
bateria de mutação, **confira `git status` e rode a bancada DE NOVO, nunca só antes**. Foi esse portão —
e não o `finally` — que pegou o estrago de hoje. Está no aviso do topo do `PROMPT.md`, com a lista
derivada em vez de decorada.

## E A MESMA VERIFICAÇÃO ACHOU UM GUARDA MORTO HÁ TRÊS DIAS, O PIOR DOS QUINZE PARA ESTAR MORTO

**`mutacoes-cobertura.py` devolveu `mutacao INERTE` na mutação `silencio do fabricante vira recomendacao
(regra 2 da cola cai)`** — a âncora que ela procura no snippet não existe mais, então a mutação não
mutava nada e a bateria passava sem medir. E o docstring dela diz o que estava desprotegido: *"É o
defeito mais caro que esta ilha pode ter — silêncio do fabricante virando 'pode' — e ele infla a
cobertura exatamente onde ela é zero."*

**DESDE QUANDO, com commit:** `ec97792`, **06/10/2026 às 20h37Z** — o commit que trouxe a **REGRA 8**
acrescentou `&& ! isset( $p['bases_indicadas_so_em'][ $base ] )` ao `if` da regra 2 e o partiu em duas
linhas. A âncora era a versão de uma linha. **Três dias e quinze horas inerte.**

**O GUARDA CAIU EXATAMENTE SOBRE O CÓDIGO QUE ESTAVA SENDO MEXIDO, e isso é o achado:** a regra 8 é a
regra que separa `ambiente_do_substrato` de `silencio`, e foi a mesma edição que a trouxe que matou a
mutação que vigia o silêncio. **E o estrago que eu peguei hoje era nesse mesmo trecho.** O guarda estava
no chão enquanto o código que ele vigia era editado.

**POR QUE NINGUÉM VIU, e não é desatenção:** `editar()` **levanta** `mutacao INERTE` — a bateria
detecta sozinha. O que falta é alguém rodando: ela leva **mais de quinze minutos** e **não está na lista
que a ronda diária roda**. O `REGISTRO.md` de 08/10 lista `guia`, `arvore`, `degrau`, `motivo-degrau-4` e
`acabamento`, e a `cobertura` não está em nenhuma lista desde 06/10. **Bancada lenta que ninguém roda é
bancada que não existe**, e a desta é a que vigia o defeito mais caro da ilha.

**CONSERTADO E CONFERIDO:** a âncora passou a ser as **duas** linhas inteiras com o `&&` dentro, e a
bateria devolve *"reprovou como devia: silencio do fabricante vira recomendacao (regra 2 da cola cai)"*,
com **zero** ocorrência de `INERTE` na passada. Se a condição crescer outra vez, a âncora quebra outra
vez e `editar()` acusa — o que está certo; o que não pode é a acusação não ser lida.

## PRESTAÇÃO DE CONTAS

**NENHUM VEREDITO MUDOU, e isso é a confirmação e não um consolo:** o `git diff` do
`filhas-do-guia.json` não tem uma linha de `veredito` nem de `itens_no_banco`. A régua não afrouxou nem
apertou o portão — ela parou de **recomendar** o caminho que a própria ilha já havia medido como fechado.
É coerente com o que o bloco de ontem mediu com 0 de 42: *"o portão desta ilha nunca foi travado por QUAL
campo ele lê; ele é travado por QUANTOS itens o banco tem"*.

**BANCADA:** `filhas-do-guia --autoteste` **53 casos, 0 falha** (eram 46 — **SETE casos novos**, e os sete
sobre a fechadura: o tipo fechado sai do caminho e a frase nomeia a pendência; o **mesmo mundo sem
fechadura continua dando caminho**, que é o controle do experimento, porque régua que exclui sempre
excluiria o certo também; com tipo aberto suficiente o caminho sai sem o fechado dentro e **dizendo** que
ele ficou fora; todo número carrega a ressalva; categoria já alcançada não muda de forma; e as **duas
falha-fechadas** explodindo). `cruzamento-14-9 --autoteste` **46 casos, 0 falha**. `--conferir` nos dois,
**aprovado**. `validar-banco` e `validar-pastilhas` OK. `teste-casca.php` **744**, `teste-guia.php`
**123**, `teste-tecnicas.php` **139**, `teste-f2.php` **174**, `teste-prestacao-rejunte.php` 540 estados da
F2 e 180 da F1, `teste-atelie`, `teste-loja` e `teste-leads` aprovados. Mutações: `guia` 18/18, `arvore`
29/29, `degrau` 8/8, `motivo-degrau-4` 10/10, `acabamento` 14/14.

**O DESPACHO DE 07/10 FICA INTEIRO, retestado e não herdado:** `search-console.py --ilha clubedomosaico`
devolve *"Sem credencial"* e `env | grep -c GOOGLE_SA` devolve **0**. Quarta execução a medir em vez de
copiar a frase. Os itens 2 e 3 são leitura de Search Console, o 4 é sessão do Shopee Afiliados no Chrome
do Raphael, e a Proposta 3 é bloco e não correção.

## O PRÓXIMO PASSO DESBLOQUEADO — E ELE NÃO É DO GUIA

**É a PROPOSTA 3 da leitura semanal: `quadro do Divino Espírito Santo`.** Com a fila consertada, o Guia
não tem URL barata: a `rejunte` está a uma filha com as três portas fechadas, a `alicate` a duas consultas
medidas, e as outras quatro a três filhas. **A Proposta 3 é a única URL desta ilha que não depende da
16.5** — ela não é filha de nível 3 do Guia —, tem a **única demanda de COMPRA medida** que o Arquipélago
já encontrou (três consultas, 4 impressões, posição média 39,2, todas caindo em
`/loja/quadro-divino-espirito-santo/`) e **o teto da 21.4 está livre**: a última leva foi o 4c em 02/10,
sete dias atrás. O bloco começa pela classificação de SERP da **14.9**, e se ela vier **TOMADA** o bloco
para aí e escreve isso — consulta de produto mediu TOMADA quatro vezes nesta ilha. O critério de pronto é
o da própria leitura: a consulta entrar na **banda 11 a 20** em `dados/posicoes.md`.

08/10/2026 19h4xZ — A ILHA ESTAVA FORA DO AR PELA TERCEIRA VEZ, E O BLOCO DO PORTÃO RESPONDEU A PERGUNTA COM UM ZERO QUE DERRUBA A PRÓPRIA PREMISSA

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **19h17Z**, push da reserva aceito na primeira
tentativa (`9f53306`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com `executando_desde:
null`, que pela **1.1** já basta, e o último commit na pasta era de **16h46Z**, duas horas e meia atrás.
`git fetch origin main` trouxe a atualização do `main` (`0758d62..13508f4`, forçada do lado do remoto); a
branch `claude/dreamy-mccarthy-zoowz1` estava **idêntica ao `main`** e sem PR aberto — nada a mesclar.
Pela **18.1** li o topo do `PROMPT.md` antes de qualquer coisa: nenhuma outra ilha tem despacho **ALTO** em
ilha no ar e quebrada, que é a única coisa que fura o foco.

## A PORTA DE ENTRADA CAIU PELA TERCEIRA VEZ, E QUEM A PEGOU FOI O COMANDO QUE MORA NO CAMINHO DO BLOCO

**O `PROMPT.md` desta ilha manda rodar os dois comandos da 29 ANTES de qualquer bloco, e foi essa linha que
pegou a queda — não a ronda.** `python3 ferramentas/conferir-no-ar.py .` **REPROVOU com 349 falhas em 513
afirmações**: **20 das 21 URLs do sitemap em 404**, mais `/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`, as
três da **29.2**. Só a raiz respondia 200, porque ela é o documento raiz e não depende de reescrita. Medido
em **três passadas** com `aquametria.com.br` em 200 nas mesmas três, como a **20.2** manda antes de chamar
rede de diagnóstico.

**A ASSINATURA É IDÊNTICA ÀS DUAS ANTERIORES, nas seis grandezas**, lida pela rota da **29.3** antes de
qualquer reparo: `.htaccess` da raiz com **1.057 bytes**, **um bloco só (`NFD EPC`)**, `tem_wordpress:
false`, **8 linhas de reescrita**, arquivo gravável, `mod_rewrite: true`, `regras_no_banco: 115`. O
`permalink_structure` também estava **inalterado** — conferi contra a linha que este mesmo `REGISTRO.md` já
guardava, em vez de achar que `/%year%/%monthnum%/%day%/%postname%/` fosse sintoma novo. **Nenhum sintoma
novo é o achado:** fecha a última hipótese barata, a de que as duas primeiras quedas fossem acidente de uma
transição já passada.

**REPARADA pela 29.3**, porque a **29.5** escreve que *"o reparo continua valendo enquanto o chamado não
tiver resposta — ilha caída esperando fornecedor é pior que ilha reparada duas vezes"*: **1.057 → 1.580
bytes**, **8 → 15 linhas de reescrita**, `tem_wordpress` **false → true**. **Conferido no ar depois, pela
19.4(a):** duas passadas com quebra de cache em 200 nas seis URLs e **404 em caminho inexistente**, e então
o `conferir-no-ar.py` inteiro em **APROVADO, 524 afirmações, 0 falha**. O `leitura-do-visitante.py` fechou
**REPROVADO com EXATAMENTE 1 defeito**, o soft 404 da borda — pendência do Raphael desde 29/09, vermelho
esperado e com dono escrito. **Zero defeito novo.**

**O QUE NÃO É MEU, E ESTÁ ESCRITO ONDE ELE OLHA:** pela **19.4(b)** a terceira queda na mesma raiz é
**chamado na HostGator**, não um quarto reparo. O chamado está em `dados/despachos.md` desde 05/10 e
**continua sem resposta**; acrescentei a terceira coluna da tabela, a janela nova (entre **07/10 20h35Z** e
**08/10 19h2xZ**, a mais estreita das três, e a primeira que cabe num dia) e o fato que torna o chamado
urgente: **o intervalo entre quedas encurtou de 11 dias para 3**. A terceira linha da série está em
`dados/consertos.md`, como a entrada de 05/10 pré-registrou com estas palavras. **Avisei o Raphael.**

## O BLOCO: `geometria` É `propriedade` PARA O PORTÃO DA SEÇÃO 9? A RESPOSTA É ZERO, E O ZERO É MAIOR QUE A PERGUNTA

**A pergunta estava escrita por duas execuções e nenhuma a tinha aberto.** A decisão foi **pré-registrada no
`PROMPT.md` antes de qualquer número** — *"`geometria` entra no portão SÓ se os campos dela tiverem a mesma
procedência por campo que `propriedades` têm"* —, e o passo 1 mandava **medir primeiro e decidir depois**.
Medi, e o número responde mais do que a decisão perguntava.

**`geometria` NÃO ENTRA, e por dois motivos independentes, não por um:**
1. **Procedência: 0 de 52.** Os 13 itens de `pastilha` têm **52 números de geometria preenchidos** e
   **nenhum** declara `fonte_id`. E não é desleixo de coleta: o esquema declara os subcampos como escalares
   (`number|null`), então **não existe onde escrever a fonte**. `propriedades` tem
   `formato_de_cada_campo: "{valor, unidade, fonte_id, declarado_como}"`; `geometria` não tem nada disso.
2. **Consequência: 0 de 42.** Rodei a régua da seção 9 num mundo em que `geometria` conta como propriedade e
   **nenhum dos 42 recortes muda de veredito**. `pastilha` e `pastilha/vidro` **já passam** — eles ganhariam
   cinco números e nenhum veredito.

**E ISSO DERRUBA A PREMISSA QUE ESCOLHEU O BLOCO, escrita duas vezes no `PROMPT.md`:** que este era *"o único
bloco desbloqueado que pode mudar um veredito de `nao_passa` para `pode_nascer` sem coletar nada"*. **Não
pode.** A razão é aritmética e vale para qualquer campo futuro: os campos fora de `propriedades` só existem
em categorias cujos recortes **já passam**, e os **30 recortes em `nao_passa` reprovam por falta de ITEM** —
que promover campo nenhum cria. **O portão desta ilha nunca foi travado por QUAL campo ele lê; ele é travado
por QUANTOS itens o banco tem.** É o mesmo tipo de descoberta que o `medir-egresso.py` desta ilha pagou em
30/09: a pergunta estava bem formulada e mirava o lugar errado.

**A SURPRESA, e ela não estava na pergunta:** generalizei a régua para **todo** campo de `MATERIAL` que
carrega número fora de `propriedades`, derivado do registro e não de uma lista de nomes — e apareceram
**seis**. `venda[].quantidade` tem **22 de 23 números com procedência por campo dentro do teto de nível 3**:
é o **único** campo fora de `propriedades` que já cumpre o critério pré-registrado, e **muda 0 vereditos**
também. Admiti-lo custaria nada e renderia nada.

**E O ACHADO QUE FAZ O FILTRO DE PROCEDÊNCIA SER CARGA E NÃO ENFEITE, com número:** `afiliado` e `imagem`
**virariam** a `cola` de `passa_na_contagem_sem_lastro` para `passa`. O único obstáculo entre eles e o portão
é a exigência de fonte por campo — e os números deles são `afiliado.degrau` e `imagem.largura`/`altura`,
**números que a ilha produziu, não que o fabricante declarou**. Sem o filtro, a `cola` nasceria publicando
como "número calculado próprio" o degrau de afiliado ou a largura em pixels da foto. **O filtro não estava
protegendo `geometria` de nada; estava segurando a `cola`.**

**E A `cola` ENSINOU A TERCEIRA COISA, dentro do próprio banco:** ela é o único recorte a um número de
passar, e as **três ofertas de `saco`** que parecem três declarações são **três embalagens do MESMO
produto** (`quartzolit-cimentcola-externo-acii`). A régua conta **ITEM**, nunca oferta — contar oferta
publicaria uma página comparando um produto com ele mesmo três vezes. Virou mutação com esse nome.

## POR QUE ISSO É RÉGUA E NÃO UM ARQUIVO DATADO EM `dados/`

A resposta de hoje depende do banco de hoje, e o banco cresce toda semana. **Medição escrita à mão envelhece
calada** — a família de defeito que esta ilha já pagou no `urls_publicadas` e no manifest com SHA mentiroso.
Então a medição virou seção **derivada** do `filhas-do-guia.json`/`.md`,
`os_numeros_que_o_portao_NAO_VE`, e `--conferir` reprova quando o número muda.

**Três decisões de desenho, e as três têm motivo medido:**
- **O mundo medido é o mais permissivo que existe**, de propósito: **todo** número entra com fonte
  **fabricada** no nível do teto, inclusive quem já tem `fonte_id` de verdade. Usar a fonte real aqui daria a
  leitura mais errada possível — campo com fonte nível 6 mudaria **menos** vereditos que campo sem fonte
  nenhuma, e "o portão não vê" passaria a depender de quão ruim é a fonte que ele também não vê. Mundo mais
  permissivo nunca muda **menos** vereditos que o real, então **zero aqui é zero em toda leitura mais
  estreita** — por unidade, por tipo ou por nível. Conferi à mão nas duas variantes de `venda` (cega à
  unidade e por unidade) antes de escolher: zero nas duas.
- **As duas perguntas saem separadas** (seção 7, nunca misturar causas): "quanto o portão não vê" e "esse
  campo tem procedência" são colunas diferentes, e o **cruzamento** é o veredito. É o que faz
  `afiliado`/`imagem` (mudam, sem procedência) e `venda` (não muda, com procedência) terem vereditos
  diferentes em vez de um booleano.
- **Falha-fechada com gatilho estreito:** `--conferir` reprova quando um campo tiver procedência por campo
  dentro do teto **E** mudar algum veredito — exatamente o mundo em que a decisão de hoje deixa de valer.
  Campo que ganha procedência e não muda nada **não** reprova: alarme sem consequência é o que faz portão ser
  ignorado.

**O caminho colapsa o índice da lista** (`venda[].quantidade`), **booleano não é número** (`True` é `1` em
Python, e contar bandeira mediria outra coisa), e `fontes` fica fora porque os números dela são o **nível**,
isto é, a régua, não o dado.

## O QUE A BANCADA ACHOU, E ELA ACHOU ALGO QUE EU NÃO IA VER

**46 casos fabricados, 0 falha** (eram 40). **Seis mutações novas**, e a mais importante é a que prova que a
régua **sabe responder diferente de zero**: o mesmo campo que fica fora sem procedência **REPROVA o mundo**
quando ganha procedência dentro do teto. Régua que responde "0 de 42" sem essa mutação é indistinguível de
uma função que soma nada — é a família do bloco 3d desta ilha, *"função de portão que nunca rodou é função
morta"*. As outras cinco: campo sem procedência que mudaria veredito fica fora com o veredito dizendo isso;
**procedência pior que o teto não conta** (o teto do esquema morde fora de `propriedades` também); campo com
procedência que não muda nada **não** reprova; três ofertas do mesmo item não são três declarações; e
booleano não entra na medição.

**E A BANCADA ACHOU UM DEFEITO MEU, pelo caso 19-b:** os três fixtures de `.md` montavam o `d` **à mão**, e
por isso renderizavam a seção nova **vazia** — a bancada ficaria verde sobre um trecho de documento que
ninguém nunca viu escrito. **O próprio comentário do caso 19-b já avisava disso, por escrito, desde 07/10**,
sobre a seção das perguntas. Os três passaram a montar o `d` por uma função única que chama o `montar()`, e o
19-b passou a cobrar a seção nova **na tela**. Com isso, seção nova no `montar()` quebra os três fixtures de
uma vez, que é o alarme certo.

## O QUE ESTE BLOCO NÃO FEZ, e os quatro estavam escritos como proibição

**Nenhuma URL nova** (a ilha segue em **21**), **nenhuma leva do teto da 21.4 gasta**, **nada publicado no
site** — este bloco é régua de repositório, não option: mudar a régua de elegibilidade e publicar em cima
dela na mesma passada seria medir o portão com a página que ele autorizou. Não escrevi quinta consulta de
`pastilha`, não reescrevi a pergunta de método dela e não tentei a terceira filha da `rejunte` por coleta.
O `cruzamento-14-9.py` foi regerado no mesmo commit, como o passo 4 do bloco exige, e **saiu idêntico** —
que é a confirmação de que nenhum veredito mudou.

**O DESPACHO DE 07/10 FICA INTEIRO, retestado e não herdado (18.5 + seção 4):** `search-console.py` devolve
*"Sem credencial"* e `env | grep -c GOOGLE_SA` devolve **0**. Terceira execução do dia a medir o mesmo em vez
de copiar a frase. Os quatro itens exigem Search Console ou sessão logada do Shopee Afiliados.

**BANCADA INTEIRA VERDE:** casca **744**, guia **123**, técnicas **139**, F1 **228**, F2 **174**,
prestação-rejunte 540 estados da F2 e 180 da F1, atelie, loja **208** e leads **211** aprovados,
`validar-banco` e `validar-pastilhas` OK, `filhas-do-guia --conferir` e `cruzamento-14-9 --conferir`
fechando. Mutações: **filhas-do-guia 46/46**, guia 18/18, árvore 29/29, degrau 8/8, motivo-degrau-4 10/10,
acabamento 14/14.

## O PRÓXIMO BLOCO, e a medição de hoje decidiu qual ele é

**NÃO é mais régua: é ITEM DE BANCO.** A pergunta do portão está respondida e a resposta diz onde o gargalo
mora — **30 dos 42 recortes reprovam por falta de item**, e nenhuma mudança de régua move isso. O caminho
mais barato já está derivado no próprio arquivo, em `caminho_mais_barato_para_as_3_filhas`: a `alicate` está
a **1 filha** das 3 da 16.5, e essa filha é `alicate/martelinho` com **3 itens a coletar**. É o único lugar
onde três registros novos viram uma **mãe de nível 2** — que é URL nova de verdade, e não mais uma régua.

08/10/2026 16h4xZ — O GUIA DEIXA DE SER DE UMA CATEGORIA SÓ: A CATEGORIA VIRA DECLARAÇÃO E A FAMÍLIA DE NÚMEROS VIRA RÉGUA

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **16h17Z**, push da reserva aceito na primeira
tentativa (`48ac93e`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta — e o último commit na pasta era de **13h35Z**, duas
horas e quarenta minutos atrás, fora da janela dos 40 minutos nos dois critérios. `git fetch origin main`
trouxe 3 commits (`0758d62..45ab260`); a branch `claude/dreamy-mccarthy-gvxr19` estava **idêntica ao
`main`** e sem PR aberto — nada a mesclar. **Rede pela 20.2:** `/` em **200** nas três passadas, e o
`/status` pela rota REST (`/wp-json/clubedomosaico/v1/status`) respondendo — o `/status` cru devolve 404 e
**não é endereço desta ilha**, está escrito no `PROMPT.md`.

**O DESPACHO CONTINUA INALCANÇÁVEL, E EU RETESTEI EM VEZ DE HERDAR A FRASE (18.5 + seção 4).** Os quatro
itens da leitura semanal de 07/10, reescritos pela 18.3 hoje às 13h2xZ, exigem Search Console ou sessão
logada do Shopee Afiliados. **Medido de novo nesta execução:** `python3 ferramentas/search-console.py
--ilha clubedomosaico` devolve *"Sem credencial: defina GOOGLE_SA_B64, GOOGLE_SA_JSON ou GOOGLE_SA_FILE"* e
`env | grep -c GOOGLE_SA` devolve **0**. Despacho inalcançável não é despacho fechado: fica como está, com
a linha de tentativa, e a execução foi para a fila.

**O BLOCO FOI O DA FILA, e ele estava nomeado pelo próprio ramo (4) do bloco anterior:** o snippet do Guia
deixar de ser de uma categoria só. É trabalho de código, não de medição, e **toda** segunda mãe vai
exigi-lo de qualquer jeito.

1. **NADA MUDOU NA TELA, E ISSO É O PORTÃO DESTE BLOCO.** Antes de tocar numa linha, as quatro páginas do
   Guia foram renderizadas e guardadas; depois do refactor, renderizadas de novo e comparadas. As quatro
   saíram **idênticas byte a byte** — 48.498, 34.551, 36.041 e 35.094 bytes. Refactor que muda a tela é
   refactor que não foi medido, e "eu não quis mudar nada" não é medição.

2. **O QUE ESTAVA ERRADO E AINDA NÃO DOÍA.** O nome `acabamento` estava escrito em **três** lugares que não
   eram o registro editorial: a option do banco, cravada dentro de `cdm_guia_banco()`
   (`clubedomosaico_dados_materiais-acabamento`), as contas e o corpo da página. Com uma categoria isso não
   é defeito — é a forma mais curta de escrever. Com a segunda, é a página da mãe nova servindo os números
   da **primeira**, e servindo-os **calada**, porque o banco era um só e ninguém o escolhia.

3. **A CATEGORIA PASSOU A DECLARAR DOIS CAMPOS, e os dois têm motivo medido.** `banco` é o id do dado no
   `manifest.json`, que é exatamente o nome da option que o Sync grava; ele **não é derivado** do nome da
   categoria de propósito, porque o banco da `rejunte` chama-se `materiais-rejuntes`, **no plural**, e
   derivar daria `materiais-rejunte`, que não existe. Derivação que acerta por sorte do idioma é a mesma
   família do campo ausente lido como `null` — ela espera o dia em que o nome não combina. `regua` é qual
   **família de números** a categoria publica, e é o que não se generaliza: a cobertura declarada e o
   relógio das demãos existem porque o esquema dá ao `acabamento` um bloco `protecao`; o `rejunte` tem
   faixa de junta e liberação de área molhada, que não são a mesma conta com outro nome.

4. **A RÉGUA TEM SEIS PAPÉIS, E A LISTA MORA NUMA FUNÇÃO SÓ:** `contas`, `moldes`, `resposta`, `ponte`,
   `achado` e `item`. A espinha monta a moldura — linha mestra, lista de filhas, o que é e o que não é,
   produto por produto, FAQ, JSON-LD, CSS — e chama a régua nos seis pontos em que a página fala de número
   ou de vizinhança. **A palavra `acabamento` só aparece em três lugares agora:** na declaração, no
   registro das páginas e dentro da régua do acabamento.

5. **E ELA FALHA FECHADA, que é a metade que importa.** `cdm_guia_pronta()` confere os seis papéis **um a
   um**, não "tem régua": régua com cinco papéis serviria a página com um buraco no meio, e buraco em
   página de tabela lê-se como "não se aplica". Categoria sem régua, sem banco declarado ou com um papel
   faltando serve o aviso honesto de que a medição não chegou — a mesma trava do banco fora do ar, um nível
   acima: lá falta o dado, aqui falta quem saiba contá-lo.

6. **A BANCADA PASSOU A SER POR CATEGORIA, E ISTO IMPORTA MAIS QUE O REFACTOR.** A régua independente do
   `teste-guia.php` lia `dados/materiais-acabamento.json` **por nome**. Então a página de uma segunda mãe
   seria conferida contra o banco da **primeira** e passaria com os números errados — **verde que mede
   outra coisa, que é o pior resultado possível** (seção 8). Agora ela lê o banco **declarado** pela
   categoria de cada página, a conta é escolhida pela família (`$REGUAS_DA_BANCADA`, indexada pela régua e
   não pela categoria), e **categoria publicada cuja família não tem régua independente aqui REPROVA**, com
   o nome dela na tela. Seção **1-b** nova, e o total subiu de **110 para 123** afirmações.

7. **A LACUNA QUE SOBRAVA, E ELA FOI FECHADA COM UM TERCEIRO CAMINHO.** Página e bancada tiram o id do
   banco da **mesma** declaração — então trocar o `banco` de uma categoria pelo de outra passaria **verde**:
   as duas leriam o mesmo arquivo errado e concordariam. Quem acusa é a lista de itens de
   `dados/filhas-do-guia.json`, que varre **todos** os `dados/materiais-*.json` e rotula cada item pela
   categoria do esquema. A afirmação nova cobra que os ativos do banco declarado sejam **exatamente** os
   itens que o cruzamento dá àquela categoria: 10 no banco, 10 no recorte.

8. **MUTAÇÕES: 18 DECIDIDAS CERTO DE 18 (eram 14).** As quatro novas: **(a)** uma segunda categoria é
   declarada sem régua — reprova, nomeando os seis papéis que faltam; **(b)** o `banco` do `acabamento`
   passa a apontar para `materiais-rejuntes` — reprova, pela lista do cruzamento; **(c)** a régua perde o
   papel `achado` — a página tem de ficar **honesta**, e fica; **(d)** o banco é **renomeado** junto com o
   arquivo, o id do manifest e a declaração — e aqui a exigência é que **nada mude**: a bancada passa e o
   corpo das páginas sai **byte a byte** o mesmo. Modo novo no arredor das mutações, o `mundo-identico`.

9. **E A MUTAÇÃO QUE NÃO QUEBRA NADA ACHOU UM NOME VELHO DE VERDADE** — dentro da própria bancada:
   `gui_raiz_com_preparo()`, o helper que fabrica o mundo em que um verniz tem instrução de preparo, abria
   `dados/materiais-acabamento.json` **pelo nome**. No dia do renome ele morreria, e morreria **dentro do
   instrumento de medição**, que é o pior lugar para um nome velho morar. Passou a ler
   `cdm_guia_categorias()['acabamento']['banco']`. **Foi a mutação positiva que achou, não a negativa** —
   as que reprovam medem o que já se desconfia; a que exige o mundo idêntico mede o que ninguém olhou.

10. **DESEMBARQUE E VERIFICAÇÃO NO AR.** Sync acionado por `curl`, **revisão 71** aplicada às 16h39Z (15
    aplicados, snippet **#13** atualizado), `/status` conferido na 71. **Os dois comandos da porta de
    entrada (seção 29.2):** `conferir-no-ar.py` **APROVADO**, 524 afirmações no HTML servido, **0 falha**;
    `leitura-do-visitante.py` **REPROVADO com exatamente 1 defeito**, o soft 404 da borda do hospedeiro
    (toda URL inexistente responde 404 na 1ª leitura e 200 na 2ª, `x-proxy-cache HIT`, `max-age=7200`) —
    **pendência do Raphael desde 29/09, registro e não portão**. As 21 URLs do sitemap chegam inteiras a
    quem não quebra o cache. **Nenhum defeito novo.**

11. **A BANCADA INTEIRA, VERDE:** casca 744, guia 123, técnicas 139, F1 228, F2 174, prestação-rejunte 540
    estados da F2 e 180 da F1, ateliê, loja e leads aprovados, `validar-banco` e `validar-pastilhas` OK,
    `filhas-do-guia` e `cruzamento-14-9` fechando com `--conferir`. Mutações: guia 18/18, árvore 29/29,
    degrau 8/8, motivo-degrau-4 10/10, acabamento 14/14.

12. **A SEGUNDA MÃE AINDA NÃO PODE NASCER, E O BLOCO NÃO PROMETIA ISSO.** A `rejunte` tem **2** filhas por
    consulta e a 16.5 pede 3; as três portas da terceira estão medidas e fechadas em 05 e 07/10 (não há
    terceiro número com lastro, os boletins estão em `www.quartzolit.weber` em 403, e o espelho da Telha
    Norte é arquivo por nome conhecido sem acrílico nem epóxi). **O código deixou de ser o impedimento; o
    impedimento é dado** — e essa é a diferença entre as duas frases.

**PRÓXIMO PASSO DESBLOQUEADO:** a pergunta que **duas** execuções já deixaram escrita e nenhuma abriu —
**`geometria` é `propriedade` para o portão da seção 9?** O que responderia a pergunta de método da
`pastilha` é `placa_lado_a_cm` e `espessura_mm`, que moram em `geometria`, e o portão lê **só**
`propriedades`: 13 de 13 itens em cinco campos **invisíveis** para a régua que decide se um recorte tem
número. É o único bloco desbloqueado que pode mudar um veredito de `nao_passa` para `pode_nascer` **sem
coletar nada** — não depende de rede, credencial, sessão logada nem de boletim atrás de 403. A decisão está
**pré-registrada** no `PROMPT.md`, antes do número: geometria só entra se os campos dela tiverem a mesma
procedência **por campo** que `propriedades` têm; se não tiverem, o veredito é que o portão está **certo**
e a `pastilha` não tem número de método — e aí a categoria fecha por dado, não por desistência.

---

08/10/2026 13h2xZ — A FORMA DA CONSULTA SEGUE A NATUREZA DO NÚMERO: A `pastilha` ESTÁ TOMADA, E A CAUSA NÃO É A FRASE

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h17Z**, push da reserva aceito na primeira
tentativa (`9b1543e`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta — e o último commit na pasta era de **11h03Z**, duas
horas e catorze minutos atrás, fora da janela dos 40 minutos nos dois critérios. `git fetch origin main`
trouxe 3 commits; a branch `claude/dreamy-mccarthy-j8tuu5` estava **idêntica ao `main`** e sem PR aberto —
nada a mesclar. **Rede pela 20.2:** `/` em **200** na primeira tentativa. Reserva **renovada às 13h32Z**
pela 1.1, porque o bloco passou de 40 minutos.

**O DESPACHO NÃO ERA ALCANÇÁVEL, E EU CONFERI ISSO EM VEZ DE HERDAR A FRASE (18.5 + seção 4).** A leitura
semanal de 07/10 deixou quatro itens, reescritos pela 18.3 em 08/10 com um motivo só para os quatro: a
ferramenta que cada um exige não está aqui. **Retestei antes de respeitar:** `python3
ferramentas/search-console.py --ilha clubedomosaico` devolve *"Sem credencial: defina GOOGLE_SA_B64,
GOOGLE_SA_JSON ou GOOGLE_SA_FILE"* e `env | grep -c GOOGLE_SA` devolve **0**. Os itens 2 e 3 são leitura de
Search Console, o 4 é sessão do Shopee Afiliados, e a Proposta 3 é URL nova que a própria leitura manda
entrar como bloco. **Despacho inalcançável não é despacho fechado**: ele fica como está, e esta execução
foi para a fila.

**O BLOCO FOI O DA FILA**, escrito em 07/10 às 19h5xZ, e ele tinha quatro passos e dois ramos. Antes de
começar, medi o estado real em vez de ler a prosa — o `REGISTRO.md` de 10h4xZ fecha dizendo que o bloco
desbloqueado era *"a segunda mãe do Guia, que desde 07/10 é a `rejunte` e está a uma filha, por
`junta_min_mm` e `junta_max_mm`"*, e isso **não bate** com a fila: aquela pergunta da junta JÁ é uma das
duas filhas que a `rejunte` tem. O `cruzamento-14-9.py` deu o número: `rejunte` com **2** filhas por
consulta e a 16.5 pede 3, com as três portas da terceira medidas e fechadas em 07/10. A fila estava certa,
o resumo do registro estava solto, e é a lição que esta ilha já escreveu com outras palavras —
**relatório velho também mente**.

1. **A PERGUNTA ESTÁ DECLARADA E PASSOU O PORTÃO DE DADO.** `pergunta:pastilha-placa-ou-caixa` em
   `dados/perguntas-do-guia.json`, apontando `placas_por_caixa`, com a consulta-alvo e a `ancora_a_mao`
   escritas à mão. A régua contou **12 dos 13** itens ativos declarando o número com fonte de nível 3, o
   conjunto **não coincide** com o recorte de tipo (a `pastilhart-af1500` é a única sem número de caixa
   nenhum, os três campos nulos) e a âncora **não caiu**. `veredito: passa`.

2. **E ELA É A PRIMEIRA PERGUNTA DESTA ILHA QUE NÃO EXISTE POR ATRAVESSAR TIPOS.** A `pastilha` tem um tipo
   só com banco (`vidro`, 13 itens), então a justificativa dela é a outra metade da 14.9: o recorte de
   TIPO `pastilha/vidro` **passa** o portão de dado e **reprova** no de SERP, com duas consultas de produto
   TOMADAS, e a mãe também. A pergunta troca o recorte sem trocar o banco — era a única forma que restava.

3. **A SERP VOLTOU TOMADA, E A FORMA NÃO SALVOU A CONSULTA.** A frase foi escrita na forma exata que abriu
   o `rejunte` seis dias antes (*"dá para … ou precisa …"*), sem pedir medida (limite 5) e sem nomear marca
   (limite 3). **Mediu no Brasil** — zero desvio, o limite 1 não tem parte nisto — e **nove dos dez
   resultados são página de produto da mesma pastilha de vidro**, em Telha Norte, Extra e MadeiraMadeira; o
   décimo é item de licitação de portal de compra pública. Zero fórum, zero vídeo, zero blog, zero resposta
   genérica. Quarta consulta TOMADA na categoria, **primeira em forma de pergunta**.

4. **A CAUSA ESTÁ NO NÚMERO, NÃO NA FRASE, e é o achado desta execução.** As únicas propriedades que passam
   o portão da seção 9 na `pastilha` são `placas_por_caixa`, `m2_por_caixa` e `peso_caixa_kg` — **os três
   são números de CAIXA, isto é, comerciais** —, e não existe frase honesta que um número de caixa responda
   e que não seja uma pergunta de compra. Quem vende já ocupa a consulta de compra. No `rejunte` o número é
   `junta_min_mm`, que é número de **gesto**, e é por isso que a pergunta do gesto cabia nele. Está escrito
   como leitura no `serp-das-filhas.json`, em `a_forma_da_consulta_segue_a_natureza_do_numero`, com a regra
   prática: **antes de escrever a próxima pergunta de qualquer categoria, olhe o número primeiro.**

5. **ISTO DERRUBA UMA LEITURA QUE TINHA CINCO ACERTOS SEGUIDOS.** `as_abertas_sao_pergunta_e_as_tomadas_sao_produto`
   diz que a forma da consulta decide: produto fecha, pergunta abre. Acertou cinco vezes e **errou na
   sexta**, e o erro ensina mais que os cinco acertos — a forma não é livre, ela segue a natureza do número
   que a página tem para entregar. A leitura antiga fica **sem uma palavra alterada** no arquivo, com a
   nova ao lado: foi ela que escolheu o experimento, e o que ela mediu continua certo.

6. **UMA SEGUNDA MEDIÇÃO, DE PROPÓSITO, PARA SEPARAR DUAS CAUSAS (seção 7 do `ARQUIPELAGO.md`).** Se a
   `pastilha` fosse tomada só por a pergunta ser de compra, uma pergunta de MÉTODO limpa deveria abrir.
   Medi *"preciso soltar as pastilhas da tela para fazer mosaico em vaso redondo ou cola a placa inteira"*
   — nenhuma palavra de compra, nenhum número, nenhuma marca. Voltou **NAO_MEDIDA por desvio PARCIAL de
   país**, forma nova neste arquivo: 1stDibs italiano, patente da OEPM espanhola, patente americana,
   fabricante francês e três páginas de um fórum inglês, junto de dois brasileiros genéricos (um artigo de
   2009) e duas páginas de produto. O núcleo é bilíngue pelo **limite 4** — `mosaico`, `placa` e `vaso`
   cabem inteiros em italiano e em espanhol —, e a consulta **não pede medida**, então não é caso do limite
   5. **São DUAS portas com DOIS motivos diferentes**, e nenhuma se abre reescrevendo a frase.

7. **E A TERCEIRA COISA, QUE É DE ESQUEMA E NÃO CONSERTEI DE PASSAGEM:** o que responderia *"soltar da tela
   ou não"* é `placa_lado_a_cm` e `espessura_mm`, que moram em **`geometria`** — e o portão da seção 9 lê
   **só `propriedades`**. A `pastilha` tem **13 de 13** em cinco campos de geometria, invisíveis para a
   régua. Não é defeito do portão: é a pergunta *"geometria é propriedade?"*, e ela muda o veredito de TODO
   recorte desta ilha. Fica escrita na fila como bloco próprio, não como linha de carona.

8. **DOIS DEFEITOS DE ESPELHO ACHADOS E FECHADOS DE CARONA, e os dois são a mesma família do que a execução
   de 10h4xZ nomeou nos nove sha vencidos.** (a) `dados/perguntas-do-guia.json` **não estava no
   manifest**: nasceu em 07/10 fora do espelho, e duas execuções o mudaram sem o atualizador imprimir uma
   linha — **arquivo fora do manifest não tem sha para vencer**, e envelhece sem nem a chance de ser
   acusado. Entrou, com `publicar: false` e o motivo escrito na própria entrada. (b) O campo `registros` do
   `serp-das-filhas` dizia **10** havendo **22** medições: seis passadas de 07/10 e 08/10 entraram sem que
   ninguém o reescrevesse, e o atualizador confere sha e **não contagem**. Corrigido, com a correção
   escrita no campo `fonte` e com a razão: resumo velho lido como fato é o defeito que este repositório
   mais paga (seção 4).

9. **O QUE EU REESCREVI COM A INDENTAÇÃO ERRADA E DESFIZ ANTES DE COMMITAR, porque diff de 1.101 linhas
   para 2 registros não é revisável.** A primeira gravação do `serp-das-filhas.json` saiu com `indent=1` e
   o arquivo era `indent=2`: 1.101 linhas mudadas, das quais 56 reais. Conferi que nada havia sido perdido
   comparando o JSON antigo com o novo campo por campo, repus a indentação original e regravei o sha. O
   diff final é **144 inserções e 14 remoções** nos seis arquivos.

**NADA FOI AO AR, E ISSO NÃO É OMISSÃO:** os cinco arquivos mudados são `publicar: false`, nenhum HTML e
nenhum snippet foram tocados, o manifest segue na **revisão 70** e **não houve Sync a acionar**. Bloco de
medição não produz desembarque.

**PORTA DE ENTRADA (seção 29), os dois comandos:** `conferir-no-ar.py` **APROVADO, 524 afirmações, 0
falha** — as 21 URLs do sitemap chegam inteiras também a quem não quebra o cache, e o sitemap serve XML
pela borda. E `leitura-do-visitante.py` fechou **REPROVADO com exatamente 1 defeito**: 22 URLs lidas sem
quebra de cache, 0 em janela de cache, e o único vermelho é o **soft 404 da borda** (origem 404, borda 404
na 1ª leitura e 200 na 2ª, `max-age=7200`). É o **vermelho esperado, com dono escrito** — pendência do
Raphael desde 29/09, registro e não portão —, e o que importava conferir era que ele não ficasse vermelho
por **outro** motivo: não ficou.

**BANCADA:** casca **744**, F1 **228**, F2 **174**, guia **110**, técnicas **139**,
`teste-prestacao-rejunte` 5 afirmações com 540 estados da F2 e 180 da F1, `validar-banco` e
`validar-pastilhas` verdes, `filhas-do-guia --autoteste` **40 de 40** e `--conferir` aprovado (inclusive a
tabela da seção 2 do `ARVORE.md` nas duas direções), `cruzamento-14-9 --autoteste` **46 de 46** e
`--conferir` aprovado. **Nenhuma bancada de mutação rodou, e o motivo é que nenhuma linha de código foi
tocada** — mutação sobre código intocado não mede nada (seção 8).

**NENHUMA URL NOVA — a ilha segue em 21, e esta é a SÉTIMA execução seguida sem URL nova.** Está medido
contra o piso: **21 contra as 40 da seção 21**, `piso: abaixo`. A 21.8 não autoriza e não proíbe leva nesta
ilha. O argumento de crescimento da fila fica escrito pela sétima vez, e agora com um número atrás dele: as
quatro portas baratas do Guia que podiam virar URL sem código estão **todas medidas e fechadas** — é por
isso que o próximo bloco é código.

**PRÓXIMO PASSO DESBLOQUEADO:** o **snippet do Guia deixar de ser de uma categoria só**, que é o ramo (4)
que o próprio bloco de 07/10 escreveu para o caso TOMADA. É trabalho de código, não espera dado nenhum, e
**toda** segunda mãe vai exigi-lo. Depois dele a segunda mãe é a `rejunte`, a uma filha da 16.5. E o
veredito das duas trocas de promessa de 08/10 continua sendo da **leitura de 14/10**, pelo critério que a
Proposta 1 escreveu — **não troque o título de nenhuma das quatro antes disso**.

08/10/2026 10h4xZ — A PROMESSA DA SERP DEIXOU DE SER INVENTÁRIO E PASSOU A SER A RESPOSTA: O TÍTULO NOMEIA A COLA, E O NOME SAI DO BANCO

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h18Z**, push da reserva aceito na primeira
tentativa (`0467165`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta — e a 1.1 não precisou do git. `git fetch origin main`
trouxe 3 commits; a branch `claude/dreamy-mccarthy-7649y6` estava **idêntica ao `main`** e sem PR aberto —
nada a mesclar. **Rede pela 20.2:** `/` em **200** na primeira tentativa, sem repetição necessária.
Reserva **renovada às 10h45Z** pela 1.1, porque o bloco passou de 40 minutos.

**O BLOCO FOI O DESPACHO, NÃO A FILA (18.5).** A leitura semanal de 07/10 deixou quatro itens e três
propostas; as **Propostas 1 e 2** são as únicas que uma execução da Fundação alcança daqui, e são o item
que a própria leitura chama de **"maior ROI do arquipélago inteiro"**. Saíram no **mesmo commit**, como a
Proposta 2 mandava: *"mesma ação da proposta 1, no mesmo commit, para as duas serem medidas juntas contra
a parada"*.

1. **O QUE MUDOU, E O PONTO NÃO É O TEXTO: É A NATUREZA DA PROMESSA.** Até hoje as duas páginas prometiam
   **inventário** — `7 colas para 9 bases` e `12 peças calculadas`. Os quatro números são contados e os
   quatro estão certos, e **nenhum deles é o que a pessoa procurou**. Agora:
   `/materiais/qual-cola-usar-no-mosaico/` serve `… – Silicone Neutro, 80%` e
   `/materiais/quantas-pastilhas-para-mosaico/` serve `… – 23 a 960 pastilhas`. As duas `description`
   passaram a **começar pela resposta**, em vez de repetir a pergunta. **Nenhuma URL mudou, nenhum H1
   mudou** (conferido no ar: os dois `<h1>` são os mesmos de ontem) e o **Picassiete não foi tocado**.

2. **A PRIMEIRA TROCA FOI MEDIDA, E É ELA QUE JUSTIFICA A SEGUNDA.** O BLOCO A trocou as promessas em
   02/10. A leitura de 07/10 mediu o resultado: as três páginas **subiram** (7,8 → 7,1 · 9,1 → 6,3 · 7,0 →
   4,7), as impressões quase **triplicaram** (30 → 81), e **o clique continuou em zero nas três**. Posição
   subindo com clique em zero não é ranqueamento — é a promessa do resultado, e foi isto que a Proposta 1
   nomeou com estas palavras.

3. **O NOME DA COLA SAI DO BANCO, e é a metade que mais vale.** `cdm_f2_cola_mais_indicada()` (nova) varre
   os **mesmos 270 casos** da `cdm_f2_cobertura()`, pela **mesma** `cdm_f2_celula_cola()`, e conta **só os
   `recomendados_topo`** — cartão de segunda linha sai com a classe `cdm-f2-segundo` justamente porque não
   é a resposta, e contá-lo faria a promessa prometer mais do que a tela entrega. Resultado medido:
   **Tekbond Silicone Neutro em 162 dos 202 casos respondidos**; o segundo é o Cascola PL500, com 28.
   **No dia em que outra cola liderar, o título e a meta mudam com ela.** Nome de produto escrito dentro do
   molde seria a família de defeito que esta ilha mais pagou, com nome no lugar do número.

4. **O TÍTULO LEVA O NOME CURTO E A META O NOME INTEIRO, e isso é aritmética de teto, não estilo.** Sobram
   **21 caracteres** no teto de 65 depois do nome desta página, e `Tekbond Silicone Neutro` tem **23**. O
   título leva o `nome_comercial` (`Silicone Neutro`, 15) e fecha em **64**; a `description`, que tem 160
   de espaço, leva o nome com a marca e fecha em **145**. O título da F1 ficou em **63**, um caractere a
   menos que a promessa anterior.

5. **A FATIA DE 80% ENTROU PELA SEÇÃO 7, e sem ela o título seria mentira de escopo.** A cola lidera 162
   dos 202 casos **respondidos**, não todos os 270 e não todos os respondidos. `Silicone Neutro` sozinho na
   SERP seria a afirmação em bloco com escopo maior do que o medido — a mesma régua que obrigou a coluna da
   condição a existir na tabela desta própria página.

6. **TRÊS RECUSAS NOVAS, TODAS FALHA-FECHADA:** banco que não chegou (trava 2 da casca: a marca volta ao
   fim do título); **empate no topo** (duas colas no mesmo número não são "a resposta", são duas); e frase
   **fora da faixa de 120 a 160** (o nome do líder vem do banco e pode crescer — "Cascola Adesivo de
   Montagem PL500 Interior" tem 42 caracteres, é a **segunda** mais indicada deste banco, e estouraria a
   faixa).

7. **A BANCADA DA F2 PASSOU A REELEGER O LÍDER POR CONTA PRÓPRIA.** Ela varre os 270 estados servidos,
   conta os `<li class="cdm-f2-cartao">` **sem** `cdm-f2-segundo` por `<h3>`, cruza com as colas ativas do
   arquivo e elege o líder **sem nunca chamar a função do snippet**. Se as duas escritas discordarem — no
   nome, na contagem ou na fatia —, a bancada reprova antes de o ar ver. É o mesmo desenho que a seção 6b
   já tinha para os três números do inventário, agora para um NOME.

8. **NASCEU O MUNDO `nome_longo=1`, E ELE EXISTE PORQUE AS DUAS TRAVAS DE TETO NÃO MORDEM HOJE.** O líder
   tem 15 caracteres: com o teto de 160 e o de 65 arrancados, a página sai **igual** e a bancada continua
   **verde**. O novo mundo renomeia as colas na option (nunca no arquivo) e cobra as duas saídas — o título
   volta à marca e a `description` cai na frase sem número, as duas medidas no HTML servido. **Trava que
   ninguém viu disparar não mediu nada** (seção 8), e aqui o preço de não medir é uma `description` cortada
   no meio no único lugar desta ilha que ninguém de dentro lê.

9. **A BANCADA DE MUTAÇÕES ACHOU DOIS FUROS MEUS, E OS DOIS FORAM CONSERTADOS NA MESMA EXECUÇÃO. O
   RESULTADO FINAL DA PASSADA LIMPA: 23 MUTAÇÕES, 22 REPROVADAS, 1 PASSOU** — e a que passou é a que foi
   **retirada**, porque mutava código que ninguém mais lê. Os dois furos abaixo.

9a. **O PRIMEIRO FURO: A RECUSA DO EMPATE ERA SILENCIOSA.**
   A mutação *"o EMPATE no topo deixa de ser recusado"* **PASSOU**: com 162 contra 28 não há empate
   possível no banco de hoje, então arrancar a recusa não muda uma letra da página e **nenhuma trava a
   via**. O conserto não foi apertar a afirmação: foi **extrair a decisão para uma função pura**,
   `cdm_f2_lider_do_mapa()`, e fazer a bancada **fabricar a borda** — cinco afirmações que a chamam com
   mapa empatado, mapa vazio, empate entre dois, primeiro lugar a um caso de distância e candidato único.
   É o mesmo caminho que o `mutacoes-divulgacao.py` teve de abrir em 29/09, quando a sétima mutação nasceu
   inerte. **Esta é a segunda vez que esta ilha paga o mesmo preço por trava silenciosa, e as duas foram
   achadas por mutação, não por leitura.**

9b. **O SEGUNDO FURO: EU DEIXEI CÓDIGO MORTO ATRÁS DE MIM, E A MUTAÇÃO ERA O ÚNICO JEITO DE DESCOBRIR.** A
   mutação *"as colas contadas com o banco inteiro, rejuntes dentro"* **PASSOU**. Ela mutava
   `cdm_f2_quantas_colas()`, e o **único** lugar que lia aquele número era a `description` que citava "7 colas
   em 270 casos" — a frase que **esta mesma execução** trocou pelo nome da cola líder. A chave ficou sem
   leitor nenhum, e a mutação passou a mutar um número que **nada publica**. **O conserto certo não era um
   portão novo:** portão sobre número que ninguém serve é verde sobre nada, e *"mutação que não morde é teste
   verde com outro nome"* (seção 8). A chave `colas`, a função `cdm_f2_quantas_colas()` e a mutação **saíram
   juntas**, com o motivo escrito nos dois arquivos, e a F2 foi para **1.13.2**. **Nenhuma linha do HTML
   servido mudou** (conferido: título e meta idênticos antes e depois). A regra que a mutação guardava — a
   frase *"10 dos 5 itens"* que esta ilha serviu no ar em 12/09, de contar um denominador que não é o da
   afirmação — **continua guardada** pela prestação de contas da seção 7 na `teste-f2.php`, que conta as colas
   **ativas do arquivo** e cobra cada uma em exatamente um lado da página, nos 270 estados.

9c. **O QUE A PASSADA LIMPA NÃO MEDIU, dito em vez de maquiado:** a retirada da mutação e a remoção do código
   morto aconteceram **depois** da passada que as mediu. Não rodei uma terceira passada completa, e o motivo
   é que ela não mediria nada de novo: a remoção apagou **código sem leitor** e tirou **uma** entrada do
   registro; as outras 22 mutações e os alvos delas não foram tocados, e as **22 reprovaram** naquela mesma
   passada. As cinco bancadas e os dois validadores foram rodados **depois** da remoção e estão verdes.

10. **O DEFEITO 1 DE 23/09 ESTÁ RISCADO, no despacho de 23/09, neste commit.** O item pedia três coisas;
    duas fecharam em 25/09 e a terceira — a linha de `/author/mosaico_gestor/` sair de `dados/posicoes.md`
    — esperou **três leituras**, porque a de 30/09 não aconteceu e a conta da Sentinela não tinha acesso à
    propriedade. A leitura de 07/10 teve o acesso e mediu: a página de autor **sumiu da tabela de páginas
    da Search Console**. O despacho daquela leitura escreve *"quem fechar o próximo bloco risca aquele item
    no mesmo commit"* — é este. **O mesmo buraco segue aberto nas irmãs**, e isso está escrito junto do
    risco para ninguém ler o risco como mais do que ele é.

11. **O DESPACHO FOI REESCRITO PELA 18.3, E OS QUATRO ITENS QUE FICARAM TÊM O MOTIVO MEDIDO, NÃO SUPOSTO.**
    `python3 ferramentas/search-console.py --ilha clubedomosaico` devolve *"Sem credencial: defina
    GOOGLE_SA_B64, GOOGLE_SA_JSON ou GOOGLE_SA_FILE"* — **a variável não está no ambiente desta rotina**, e
    os itens 2 e 3 são leitura de Search Console. O item 4 exige sessão logada do Shopee Afiliados. A
    Proposta 3 é URL nova e a própria leitura escreve que ela *"entra na fila como bloco, não como
    correção"*. **A leitura de 07/10 diz que "a leitura pela nuvem passou a funcionar nesta ilha" e as duas
    coisas não se contradizem:** o acesso que faltava era o da conta de serviço **à propriedade**, e foi
    dado; o que falta aqui é a **credencial no ambiente das rotinas**. Outro problema, do mesmo dono, e
    está em `dados/despachos.md`.

12. **O QUE NÃO ADIANTA TENTAR DAQUI, escrito no despacho para a próxima execução não gastar a vez:**
    adivinhar as 6 URLs em 404 sondando endereços do desenho antigo com `curl` **não serve como lista**,
    porque nesta ilha toda URL inexistente responde **404 na 1ª leitura e 200 na 2ª** por 2 horas (o soft
    404 da borda, pendência do Raphael desde 29/09). Uma varredura de candidatos devolveria 200 para
    endereços que não existem e a lista sairia errada nos dois sentidos. **A lista tem UMA fonte.**

13. **O MANIFEST CARREGAVA NOVE SHA VENCIDOS, E O ATUALIZADOR OS IMPRIMIU.** A execução de 07/10 mudou
    `dados/filhas-do-guia.*`, `dados/cruzamento-14-9.md`, `dados/serp-das-filhas.json` e as duas
    ferramentas delas, e fechou dizendo *"manifest segue na 67 e não houve Sync a acionar"* — o sha deles
    ficou velho. Todos os nove são **`publicar: false`** (conferido um por um antes do Sync), então nada
    de pesquisa foi ao ar por acidente: o Sync aplicou os dois snippets e os dados que já eram
    publicáveis. **Espelho que não imprime o que trocou envelhece calado** — e foi o próprio
    `atualizar-manifest.py` quem mostrou.

**NO AR E CONFERIDO (seção 8 e 18.4):** Sync disparado por `curl` às **10h46Z**, `/status` e `manifest.json`
na revisão **70** (três disparos: 68 com a troca das promessas, 69 com a função pura, 70 com a remoção do código morto). Os quatro `<title>` e as quatro `description` lidos com quebra de cache e
`Accept-Encoding: identity`: as duas trocadas servem o texto novo, as duas paradas servem o de antes, letra
por letra. `conferir-no-ar.py`: **524 afirmações, 0 falha** (eram 519 em 29/09).

**BANCADA:** casca **744**, F1 **228**, o mesmo de ontem, F2 **174** (eram 162), guia 110, técnicas 139,
`teste-prestacao-rejunte` 540 estados da F2 e 180 da F1, `validar-banco` e `validar-pastilhas` verdes,
`filhas-do-guia --autoteste` 40 de 40, `cruzamento-14-9 --autoteste` 46 de 46.

**NENHUMA URL NOVA — a ilha segue em 21, e esta é a SEXTA execução seguida sem URL nova.** Isto não é
descuido e está medido contra o piso: **21 contra as 40 da seção 21**, `piso: abaixo`. A 21.8 não autoriza
e não proíbe leva nesta ilha, e **correção fura a fila mas não consome a vez de um bloco** (18.2). O
argumento de crescimento da fila continua de pé e fica escrito aqui pela sexta vez.

**PRÓXIMO PASSO DESBLOQUEADO:** o veredito das duas trocas é da **leitura de 14/10**, pelo critério que a
própria Proposta 1 escreveu — 1 ou mais cliques em 7 dias, **ou** zero nas duas trocadas E zero na parada,
que também é resultado. **Os dois `<title>` servidos hoje estão copiados em `dados/posicoes.md`** para a
leitura não precisar reconstituí-los. **Não troque o título de nenhuma das quatro antes de 14/10:** seriam
três trocas em doze dias e a série ficaria ilegível. O bloco de construção que está desbloqueado é o da
fila — a **segunda mãe do Guia**, que desde 07/10 é a `rejunte` e está **a uma filha**, por `junta_min_mm`
e `junta_max_mm` declaradas por 5 de 5 rejuntes com fonte de nível 2 nos três tipos, sem SKU, sem PDF e
sem coleta.

07/10/2026 19h5xZ — A FILHA EM FORMA DE PERGUNTA ENTROU NO PORTÃO, E A 16.5 PASSOU A CONTAR CONSULTA: A `alicate` TEM UMA FILHA, NÃO TRÊS, E A SEGUNDA MÃE DO GUIA É A `rejunte`

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **19h18Z**, push da reserva aceito na primeira
tentativa (`30a3269`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta, e o último commit na pasta era de **16h37Z** — duas
horas e meia atrás, fora da janela dos 40 minutos. `git fetch origin main` trouxe 2 commits; a branch
`claude/*` estava **idêntica ao `main`** e sem PR aberto — nada a mesclar. **Rede pela 20.2:**
`https://clubedomosaico.com.br/` em **200**, primeira tentativa.

**Nenhum despacho aberto para a Fundação.** O único item do despacho de 07/10 continua sendo o teste de vida
da 25.4, e ele diz com todas as letras que é **19.2**, do Raphael. Li o topo do `PROMPT.md` pela **18.1**
antes de escolher o bloco.

**O BLOCO ERA O DA FILA**, escrito às 16h5xZ pela execução anterior: a terceira filha da `alicate` em forma
de PERGUNTA, medida *"chamando a régua de `filhas-do-guia.py` em vez de reescrevê-la"*, e depois a mãe
`/materiais/alicates-e-corte/` com as 3 filhas — **4 URLs, 21 → 25**. **A primeira metade saiu inteira. A
segunda estava errada na conta da 16.5, e o erro é de uma família que esta ilha já nomeou: contar recorte
onde o que escasseia é consulta.** Nenhuma URL nova (segue em **21**), nada no ar mudou, manifest segue em
**67** e não houve Sync a acionar — este é um bloco de régua e de medição.

## O que mudou

**`dados/perguntas-do-guia.json` (novo).** As filhas em forma de PERGUNTA, declaradas. O que se digita é
decisão de **nome**, no mesmo lugar e pelo mesmo motivo que o `PONTE_SLUG_CATEGORIA` é a única coisa digitada
no `filhas-do-guia.py`: o id, a categoria, **a propriedade que carrega o número**, a consulta-alvo e uma
`ancora_a_mao`. **Nenhum número, nenhum item e nenhum veredito.** Duas perguntas entraram:
`pergunta:alicate-espessura-de-corte` (`espessura_maxima_de_corte_mm`) e `pergunta:rejunte-largura-da-junta`
(`junta_min_mm`).

**`ferramentas/filhas-do-guia.py`.** `carregar_perguntas()`, `medir_perguntas()` e `resumo_das_perguntas()`,
medindo pela **mesma** régua: mesmo `MINIMO_DA_SECAO_9`, mesmo `propriedades_com_lastro()`, mesmo teto lido
do esquema. O recorte de uma pergunta é derivado — os itens **ativos** da categoria que declaram a
propriedade com lastro. A seção nova entrou no `.json`, no `.md` e **no `--conferir`**, que passou a cobrar
as duas chaves novas e a derrubar a execução quando uma `ancora_a_mao` divergir da derivação. Autoteste de
**27 para 40 casos**; 13 novos, 12 só pelo portão novo.

**`ferramentas/cruzamento-14-9.py`.** `serp_da_pergunta()`, `cruzar_perguntas()` e
`o_que_falta_na_pergunta()`; a pergunta se liga à SERP **pela consulta**, não pelo nome do recorte — e por
isso herda a classificação de uma medição arquivada sob outro recorte, o que é exatamente o caso desta ilha.
`mae_pode_nascer()` reescrita: a 16.5 passou a contar **consultas abertas distintas**, fora a da mãe, com as
perguntas dentro da conta e a consulta disputada saindo nomeada. Autoteste de **32 para 46 casos**.

**`dados/serp-das-filhas.json`.** Três medições novas (17 → 20) e o **`limite_5`** do canal.

**`ARVORE.md`.** Seção **2b**, com o quadro por categoria derivado do cruzamento.

## A pergunta não afrouxou o portão, e isto está no código

No recorte de tipo a seção 9 cobra **três** coisas separadas: 3 itens no recorte, 3 deles com lastro, e uma
propriedade declarada por 3 ao mesmo tempo. Na pergunta as três **coincidem**, porque o recorte dela não é
um tipo do vocabulário: é o conjunto dos itens que declaram o número com lastro. Contar "itens no recorte"
ali seria contar a mesma coisa duas vezes e dizer que o portão ficou mais largo. Quem ler "um veredito em
vez de três" tem de ler esta frase junto, e ela está no cabeçalho da seção nova e na página gerada.

## A CORREÇÃO: a 16.5 se fecha por CONSULTA, e por sete dias esta ilha contou RECORTE

O item da fila somava três filhas para a `alicate`. Duas coisas estavam erradas, as duas mensuráveis:

- **`alicate/torques` não é filha.** O DADO dela abriu às 16h37Z de hoje, e a **SERP é `TOMADA`** desde
  05/10 — 7 de 10 são loja de ferramenta ou fabricante na página do próprio torques. Veredito do cruzamento:
  `espera_autoridade`. O `ARVORE.md` já escrevia, desde 02/10, que *"filha não é filha no dado: é no
  cruzamento"* — e a fila somou no dado.
- **A pergunta não é uma SEGUNDA filha ao lado de `alicate/cortador_de_azulejo`: é a MESMA.** As duas miram
  `como cortar pastilha de vidro para mosaico qual ferramenta`, medida ABERTA em 30/09, cujo próprio campo
  `numero_que_a_serp_nao_publica` nomeia `espessura_maxima_de_corte_mm` *"declarada em 4 dos 6 itens de
  `alicate`"*. A consulta era da pergunta desde o começo; o tipo estava sentado nela porque foi quem mediu
  primeiro.

**Recorte não é o que escasseia. Consulta é.** Duas páginas na mesma consulta não são duas filhas: são a
mesma página duas vezes, disputando a própria consulta. O quadro derivado de hoje:

| categoria | filhas no DADO | no CRUZAMENTO (tipos) | perguntas | **por CONSULTA** | a mãe pode nascer |
|---|---|---|---|---|---|
| `acabamento` | 3 | 3 | 0 | **3** | **SIM** — e é o controle do experimento |
| `rejunte` | 1 | 1 | 1 | **2** | não, falta **uma** |
| `alicate` | 2 | 1 | 1 | **1** | não |
| `pastilha` | 1 | 0 | 0 | **0** | não |
| `cola`, `base`, `apoio` | 0 | 0 | 0 | **0** | não |

A `acabamento` é o caso que exige que a régua nova **aprove** a mãe que já está no ar — três consultas
distintas, nenhuma igual à da mãe —, e ela aprova. Régua que não aprova o certo vai reprovar trabalho bom, e
esta ilha pagou isso hoje de manhã com o `--autoteste` do próprio `filhas-do-guia.py`.

## A SEGUNDA MÃE DO GUIA MUDOU DE CATEGORIA, E A PERGUNTA É QUEM A MOVEU

A fila dizia que `rejunte` custava **4 itens de banco** e que a coleta estava fechada por boletim em PDF.
Verdade **por tipo**: `acrilico` tem 1 item e `epoxi` tem 1, e o caminho de SKU novo foi fechado com nome em
05/10. A pergunta passa por fora: `junta_min_mm` e `junta_max_mm` são declaradas por **5 de 5** rejuntes,
com fonte de **nível 2** nos cinco, atravessando os **três** tipos — acrílico 1–4 mm, epóxi 1–5 mm,
cimentício 2–10 mm. **Ela reúne cinco onde nenhum tipo reúne três**, que é literalmente o caso que o
`filhas-do-guia.py` descreve desde 30/09. Nenhum SKU, nenhum PDF, nenhuma coleta.

E a consulta dela foi medida hoje e **ABRIU**: *"dá para colar os caquinhos bem juntos no mosaico ou precisa
deixar espaço para o rejunte"*. Nove resultados únicos — quatro matérias de decoração sobre caquinho, dois
manuais de assentamento de um **kit** de fabricante (que dá `1 cm a 3 cm` para aquele kit, não para
caquinho), uma calculadora de consumo, uma tese e uma ficha espanhola. **Zero marketplace, zero página de
produto de rejunte**, e nenhum dos nove diz de quantos milímetros é a junta que um rejunte de prateleira
cobre. A faixa descoberta que a página terá de **dizer** (14.3) já está no campo: o piso dos três
cimentícios é **2 mm**, então quem encosta os caquinhos não tem cimentício neste banco que o atenda — os
dois que chegam a 1 mm são o acrílico e o epóxi.

## O LIMITE 5 DO CANAL, e ele derruba a regra prática que o limite 4 escreveu seis horas antes

O limite 4, de hoje às 16h5xZ, fechou dizendo: *"para medir corte nesta ilha, ancore em `alicate`, nunca em
`cortador de azulejo`"*. Esta execução fez exatamente isso — *"até quantos milímetros de espessura o
**alicate** corta pastilha e **caquinho** para **mosaico artesanal**"*, a âncora pedida mais duas expressões
que não existem em espanhol — **e desviou igual**: ManoMano e MosaicShop da Espanha, Mercado Livre do Chile,
Truper e Sears do México, e no Brasil só agregador de preço (Zoom, Bondfaro) e portal de compra pública.

**A variável não é a âncora: é PEDIR O NÚMERO.** A prova vem dos dois lados e de **duas categorias**:

| consultas que PEDEM a medida | consultas que NÃO pedem |
|---|---|
| 5, todas desviadas: três de corte (30/09 e duas hoje de manhã), a de hoje no alicate e *"rejunte para junta fina de **1 mm**"*, que trouxe Grupo Puma, Isaval, Anfapa e o Gerador de Preços, todos da Espanha | 3, todas medidas no Brasil: a mãe do alicate, `como cortar pastilha de vidro para mosaico qual ferramenta` e a do caquinho de hoje |

A causa é **estrutural** e já estava escrita do outro lado deste mesmo arquivo: quem publica medida é o
fabricante, em documento técnico, e o corpus de documento técnico que este canal alcança é ibérico e
mexicano. O campo `numero_que_a_serp_nao_publica` é essa frase pelo avesso — se o número **não** está na
SERP brasileira, a consulta que o exige sai do Brasil para achar quem o tem. **A regra que fica, para toda
categoria: a consulta-alvo de uma filha NUNCA pede o número. Ela faz a pergunta da artesã, e o número é o
que a PÁGINA entrega** — é assim que a F1 e a F2 são.

## O boletim do rejunte piscinas foi aberto outra vez, e o que se procurava não está lá

`classificacao_normativa` tem lastro em **2 de 3** registros que a declaram e seria o terceiro número do
`rejunte` a **um campo** de distância. O boletim no espelho da Telha Norte (`1200003.pdf`, 3 páginas,
revisão de agosto de 2017) foi baixado (HTTP 200, 860 KB) e lido: **zero ocorrência de `tipo I`, `tipo II`,
`NBR` ou `14992`**. O campo fica ausente **por medição**, não por esquecimento, e os outros quatro boletins
seguem em `www.quartzolit.weber` com **403**. Não procure de novo neste documento.

## O que não foi feito, de propósito

**Nada foi publicado.** A mãe `/materiais/alicates-e-corte/` não nasce com 1 filha (**16.5**), e filha
sozinha pendurada em `/materiais/` é o cluster ralo que a **16.6** proíbe — decisão desta ilha, escrita no
item 3 desta fila desde 02/10. **Quinta execução seguida sem URL nova**, e o argumento de crescimento da
fila continua de pé: 21 URLs contra as 40 do piso da seção 21.

## Bancada

Tudo verde, e nada no ar mudou de comportamento porque nenhum snippet foi tocado:
`validar-banco.py` OK · `validar-pastilhas.py` 0 falhas · `filhas-do-guia.py --autoteste` **40 de 40** e
`--conferir` APROVADO (json, md e a tabela da seção 2 do `ARVORE.md` nas duas direções) ·
`cruzamento-14-9.py --autoteste` **46 de 46** e `--conferir` APROVADO · `teste-guia.php` 110 ·
`teste-casca.php` 744 · `teste-f1.php` 228 · `teste-f2.php` 162 · `teste-tecnicas.php` 139 ·
`teste-prestacao-rejunte.php` 5 afirmações sobre 540 estados da F2 e 180 da F1.

## Próximo passo desbloqueado

**Medir a SERP de uma pergunta de MÉTODO na `pastilha`** — a categoria com mais banco da ilha (13 itens) e a
única com número sobrando: `m2_por_caixa`, `peso_caixa_kg` e `placas_por_caixa` têm lastro em **12 dos 13** e
não servem a nenhuma página. Ela está em `espera_autoridade` porque as **duas** consultas medidas nela são de
**produto**, e a leitura `as_abertas_sao_pergunta_e_as_tomadas_sao_produto` já acertou cinco vezes. Se abrir,
o Guia passa a ter **duas** categorias a uma filha da mãe. Se vier TOMADA, está medido que a `pastilha` não
é alcançável por pergunta neste canal — e o bloco seguinte é o snippet do Guia deixar de ser de **uma
categoria só**, que é código e não medição, e que toda segunda mãe vai exigir de qualquer jeito.

---

07/10/2026 16h5xZ — O PORTÃO DE `alicate/torques` ABRIU SEM UM ÚNICO SKU NOVO; A MÃE NÃO FOI PUBLICADA PORQUE FALTOU UMA FILHA, E A TERCEIRA NÃO É UM TIPO: É UMA PERGUNTA

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **16h17Z**, push da reserva aceito na primeira
tentativa (`06bfcd6`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta — a reserva é escrita ANTES do trabalho —, e o último
commit na pasta era de **14h58Z**, a ronda diária, que pela 1.1 **não reserva nada**. `git fetch origin main`
trouxe 2 commits; a branch `claude/*` estava **idêntica ao `main`** e nenhum PR aberto — nada a mesclar.
**Rede pela 20.2:** `https://clubedomosaico.com.br/` em **200**.

**Nenhum despacho aberto para a Fundação.** O de 07/10 tem **um** item, e ele diz com todas as letras que o
teste de vida da 25.4 *"NÃO É DA FUNDAÇÃO, É DO RAPHAEL"*, por ser escolha entre opções defensáveis (**19.2**).
Li o topo do `PROMPT.md` pela **18.1** antes de escolher.

**O BLOCO ERA O DA FILA**, escrito às 14h2xZ pela execução anterior: a segunda categoria do Guia pelo
`alicate`, com coleta de **5 itens de banco** (2 de `torques`, 3 de `martelinho`), para `alicate` alcançar as
3 filhas da **16.5** e publicar mãe + 3 filhas — **4 URLs, 21 → 25**. A primeira metade saiu por um caminho
muito mais barato do que o escrito; a segunda está **medida como impossível neste canal**; e a mãe **não foi
publicada**, que é o item sendo obedecido e não abandonado.

## O que mudou

`dados/materiais-alicates.json`: os **três** registros de `torques` ganharam `tamanho_polegadas` de **nível
3** (8" no `corte-reto`, 7,5" no `corte-curvo`, 8" no de roldanas) e os dois que estavam com
`codigo_fabricante: null` ganharam a referência do próprio fabricante (**60857** e **60858**). Com isso
`alicate/torques` foi de **1 de 3** itens com lastro para **3 de 3**, e passou a ter uma propriedade declarada
pelos três — que é a segunda metade do portão da seção 9. `alicate` foi de **1 de 4** para **2 de 4** tipos,
e a tabela da seção 2 do `ARVORE.md` foi acertada junto (o `--conferir` a reprovou antes de eu a olhar).

`ferramentas/filhas-do-guia.py`: o fixture da autoteste saiu de `rejunte: 0 de 4` para `1 de 4` e de
`alicate: 1 de 4` para `2 de 4`. `dados/serp-das-filhas.json`: duas medições novas e o
`limite_4_nome_de_recorte_bilingue`. Manifest **67**. **Nenhum snippet alterado, nenhuma URL nova, nenhuma
página criada** — a ilha segue em **21**.

## O achado: o que mudou não foi a porta, foi o que se pede pela fresta

`cortag.com` continua **`EGRESS_BLOCKED`**, remedido hoje por `curl` (**000**) e por **WebFetch**
(`EGRESS_BLOCKED`) — a parede é a mesma para os dois, como o `canal_de_espelho` do esquema já dizia. O que
mudou foi **o pedido**: toda passada anterior pediu a **DESCRIÇÃO** do produto, e a busca **mistura a prosa
dos três torqueses irmãos**. Foi isso que derrubou as passadas de 25/09, e está escrito em
`corte.observacao` daqueles registros com a conclusão certa: *"frase de linha não é frase de produto"*.

A **TABELA DE ESPECIFICAÇÃO** é outra coisa, e a diferença é o método: ela é **por SKU** e **se
autoconfere**, porque cada EAN fecha com a própria referência — 60857 → 7897451468571, 60858 →
7897451468588, 61341 → 7897451413410. Um resumo que estivesse misturando irmãos não produziria três EANs
distintos e coerentes. **Três leituras consistentes:** duas passadas no domínio escritas de formas
diferentes e uma corroboração independente de **canal de varejo** (nível 6) que escreve as **mesmas** duas
medidas, 8" e 7,5", sem ter sido perguntada por elas juntas. A corroboração **não promove** nada: o que
sustenta o campo é a tabela. **A regra que fica, e vale para toda categoria de FERRAMENTA deste banco:
quando o egresso fecha a página do fabricante, a tabela de especificação ainda passa; a prosa, não.**

## E ela fechou de carona a pendência que era load-bearing para o próprio portão

`torques-curvo-e-roldanas-podem-ser-o-mesmo` estava **ABERTA** desde 25/09 e se declarava *"a mais
importante deste arquivo"*: perguntava se `cortag-torques-azulejista-corte-curvo` e
`cortag-torques-mosaico-roldanas` eram duas entradas de catálogo do mesmo produto. **São dois**, separados
por **três** campos independentes: referência (60858 / 61341), EAN e **tamanho** (7,5" / 8"). EAN distinto é,
por definição, unidade comercial distinta — não é inferência nossa, é a função do código.

Isso não é detalhe de arquivo. **Se fossem o mesmo, o registro do curvo viraria `descartado`, o recorte
`torques` cairia para 2 itens — abaixo do mínimo de 3 — e o portão que este bloco acabou de abrir estaria
aberto sobre um registro duplicado.** Fechar a pendência **antes** de contar os três é o que separa portão
medido de portão que deu sorte, e eu só notei que ela era load-bearing depois de contar. E a suspeita se
**explicou** em vez de só cair: a frase de 5 mm é igual nos dois porque é texto de **linha** — exatamente a
razão pela qual ela não podia ser gravada em nenhum dos dois. A pendência e o defeito de coleta de 25/09
tinham a **mesma causa** e se resolvem pelo mesmo lado.

## `martelinho` não é coleta difícil: é coleta impossível neste canal

O item dizia que os 5 itens eram baratos porque *"o dado real de um alicate é medida, material e mecanismo,
que página de fabricante e ficha de marketplace publicam — nenhum deles precisa de PDF"*. **O argumento
acerta o tipo do dado e erra a existência da página.** Os dois fabricantes deste banco foram varridos por
busca restrita ao domínio: **Cortag** não faz martelinho de mosaico nem pinça — faz `Martelo de Borracha`
(declarado para porcelanato, cerâmica e pedra natural, e é martelo de **assentar**, não de cortar) e
`Martelo Tipo Unha` (carpintaria); **Vonder** não faz nenhum dos dois, e o único resultado dela com a
palavra é **armadilha**: `Pino rebatedor para martelinho de ouro`, que é funilaria de automóvel.

**A causa não é de coleta:** o martelinho de mosaico é a martellina com o tagliolo, ferramenta artesanal de
mosaiquista, não produto de indústria de ferramenta de construção. No Brasil ele circula por marketplace e
ateliê — **nível 6**, que sustenta preço, embalagem, peso e imagem e **nunca** campo técnico. Não é que a
página não foi achada: é que a declaração de fabricante que o portão exige **não é publicada por ninguém
nesse mercado**. Gravado como `martelinho-e-pinca-nao-tem-fabricante-neste-canal`, com a instrução de **não
buscar outra vez** em Cortag e Vonder. O que mudaria isto é **fabricante novo no banco**.

## A mãe não foi publicada, e isso é o item sendo obedecido

O item manda, textualmente: *"confere que `alicate` passou a 3 filhas — **se não passou, para aí e escreve
quanto faltou**, porque publicar categoria com 2 filhas é o que a 16.5 proíbe"*. Faltou **uma**. Categoria
vazia ou rala indexada é página fina que **derruba o resto**, e essa é a razão da regra.

## A terceira filha existe, e a autorização estava escrita dentro do próprio portão

`filhas-do-guia.py`, no campo `o_que_este_arquivo_mede_e_o_que_ele_NAO_alcanca`, diz textualmente que filha
de nível 3 **também pode ter forma de PERGUNTA** em vez de forma de tipo, que *"uma pergunta atravessa tipos
e pode reunir 3 itens onde nenhum tipo sozinho reúne"*, que o arquivo é **PISO e nunca teto**, e que *"um
`nao_passa` aqui não proíbe a pergunta, proíbe o tipo"* — e que **as duas filhas que esta ilha já publicou
são assim** (a F1 e a F2). **A fila inteira de `alicate` foi escrita contando tipos**, e o quadro de 14h2xZ
que escolheu este bloco tirou o número do campo `caminho_mais_barato_para_as_3_filhas`, que só conhece tipos.

**E o número da pergunta já está no banco:** `espessura_maxima_de_corte_mm` é declarada com fonte de nível
≤ 3 por **4 itens**, atravessando os dois tipos — o torques de roldanas em **5 mm** (único do banco cuja
declaração nomeia **vidro**) e os três Vonder em **10 mm** (que **não** nomeiam vidro em lugar nenhum).
Quatro é maior que três. E é a **única** propriedade deste banco que atravessa tipo, conferido:
`tamanho_polegadas` tem 3 e são só torques; `dimensoes_mm`, `comprimento_maximo_de_corte_mm` e
`diametro_do_rodel_mm` têm 3 e são só cortadores.

## As duas SERP em `NAO_MEDIDA` foram medidas e continuam `NAO_MEDIDA` — a causa trocou de dono

Duas passadas novas em `alicate/cortador_de_azulejo`: uma **sem marca**, pedindo o milímetro, e uma ancorada
**de propósito** em `caquinho` e `mosaico artesanal`, duas expressões que só existem no Brasil. **As duas
desviaram de país** — Truper e Sears do México, El Corte Inglés e patente do OEPM da Espanha. A segunda é o
**controle do experimento**: se âncora brasileira resolvesse, ela tinha de medir, porque carrega duas.

Entrou como **`limite_4_nome_de_recorte_bilingue`**: consulta cujo **núcleo** cabe inteiro em espanhol desvia
por mais brasileira que seja a moldura, e `cortador de azulejo` e `pastilha` cabem. **A prova pelo outro
lado está no mesmo arquivo:** a consulta da mãe, `qual alicate usar para cortar pastilha de mosaico
artesanal`, mediu **ABERTA de primeira** em 05/10, porque `alicate` não é palavra espanhola. **Regra: para
medir corte nesta ilha, ancore em `alicate`, nunca em `cortador de azulejo`.** A consequência que custa: o
recorte `alicate/cortador_de_azulejo` passa o portão de **dado** (3 itens, 4 números) e segue **sem SERP
medida** — ele não é mensurável por este canal com o próprio nome. Três passadas bastam.

## Uma bancada vermelha no `main` há dois dias, achada de passagem

`filhas-do-guia.py --autoteste` fechava **REPROVADO, 2 falhas de 27**, e uma delas era o caso que exige que
o portão **APROVE a tabela certa** — régua que não aprova o certo é régua que vai reprovar trabalho bom.
Confirmado pré-existente com `git stash`, antes de eu tocar em nada. **Causa única:** o fixture é escrito
**à mão de propósito** (para não chamar a função que ele mede) e carregava `rejunte: 0 de 4`, defasado desde
**05/10**, quando a faixa de junta do rejunte piscinas chegou pelo boletim; a segunda falha era o mesmo
fixture, montado pelo caso do slug fora da ponte. **O comentário do próprio arquivo previu isto** — *"quem
mudar o banco e vir este caso falhar não tem defeito para procurar: tem dois números para reescrever"*.

**Por que ninguém viu:** `filhas-do-guia.py --autoteste` **não está na lista de bancadas que a ronda diária
roda**, e a tabela do `ARVORE.md`, que carrega a mesma informação, **tem quem a confira** (`--conferir`) e
foi corrigida no próprio dia 05/10. A cópia à mão não tinha. Hoje: **APROVADO, 27 de 27**. *(Fica a pergunta
para a ronda, e ela não é despacho: esta bancada precisa entrar na lista dela.)*

## Verificação

Bancada inteira verde e **nada no ar mudou de comportamento**, porque nenhum snippet foi tocado: validador
do banco, `validar-pastilhas`, `teste-guia` **110**, `teste-casca` **744**, `teste-f1` **228**, `teste-f2`
**162**, `teste-tecnicas` **139**, `teste-prestacao-rejunte` (540 estados da F2 e 180 da F1),
`filhas-do-guia --autoteste` **27 de 27** e `--conferir` fechando a tabela do `ARVORE.md` **nas duas
direções**. Manifest **67** desembarcado pelo Sync e `/status` conferido na **67**.

## Próximo passo desbloqueado

**A terceira filha de `alicate`, em forma de PERGUNTA**, sobre os 4 itens que declaram
`espessura_maxima_de_corte_mm` — e com ela a mãe `/materiais/alicates-e-corte/` e as 3 filhas, **4 URLs, 21
→ 25**. A SERP diz que é exatamente a página que falta no nicho, nas duas medições que existem: a da mãe
(**ABERTA**, 100–1.000/mês) registra que *"NENHUM dos dez compara as quatro ferramentas que o próprio nicho
nomeia"*, e a de `alicate/torques` registra que a SERP publica a regra **qualitativa** (roldana para vidro,
reta para cerâmica) e que **nenhum dos dez publica o limite em mm**. O mesmo buraco medido por dois lados.
O achado que a página serve **já está pago**: o teto de 5 mm do único torques que declara vidro cruza com
`materiais-pastilhas.json` e **3 das 13 pastilhas do banco não cabem** (`st5102` 6 mm, `af1500` 8 mm,
`ic02` 8 mm) — faixa descoberta da 14.3, para a tela **dizer** em vez de calar, e hoje escrita só no banco.
O bloco inteiro está na fila do `PROMPT.md`, com o que ele **não** deve fazer.

---

07/10/2026 14h16Z — O MESMO DEFEITO UM ANDAR ABAIXO: A REGRA 3 DO REJUNTE DIVIDIA O BALDE COM A REGRA 2 E SERVIA A FRASE DELA; BALDE PRÓPRIO EM **DUAS** TELAS, 8 ENTRADAS EM 8 DOS 60 ESTADOS

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h17Z**, push da reserva aceito na primeira
tentativa (`5c6e190`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta — a reserva é escrita ANTES do trabalho, então `null`
significa que nenhum bloco da Fundação está vivo; o último commit na pasta era de **11h08Z**, duas horas
antes, e era o fecho da execução anterior. `git fetch origin main` trouxe 5 commits; a branch `claude/*`
estava **idêntica ao `main`** e nenhum PR aberto — nada a mesclar. **Rede pela 20.2:**
`https://clubedomosaico.com.br/` em **200** e o `/status` na revisão **65**, igual à do `manifest.json` que a
execução anterior deixou. **Reserva RENOVADA às 13h37Z pela 1.1.**

**Nenhum despacho aberto para a Fundação.** O de 05/10 tem os itens 1 e 2 **CUMPRIDOS** e o item 3 se declara
método endereçado ao Raphael; o item 2 do de 30/09 é o soft 404 da borda, que já é do hospedeiro e das duas
ilhas. Li o topo do `PROMPT.md` pela **18.1** antes de escolher.

**O BLOCO ERA O DA FILA, escolhido por escrito e com o número medido pela execução anterior**, às 11h0xZ: o
balde `eliminados_por_ambiente` do rejunte carregava **duas causas sob uma frase só**. E a primeira coisa que
esta execução fez foi **remedir**, com uma reimplementação independente das quatro regras lida do esquema —
não do validador. Os três números bateram: **8 entradas em 8 estados pela regra 3**, **59 em 28 pela regra
2**, **7 estados carregando as duas**.

## O que mudou

Esquema **v16**: a `3_ambiente_declarado_DELIMITA` do rejunte era uma frase de uma linha e virou dicionário
com balde, ordem e travas; nasceu `regras_do_balde_do_ambiente_do_produto_do_rejunte` com o único produto que
delimita ambiente hoje e **cinco âncoras ponta a ponta**; as nove células da `matriz_esperada_do_rejunte`
foram reescritas **à mão** e bateram com a recomputação sem uma divergência. **F2 1.12.0**, **F1 1.7.0**,
`teste-f2.php` de 160 para **162** afirmações, `teste-prestacao-rejunte.php` com a quarta régua separada e a
F1 cobrada nas duas direções, `cobertura.py` carregando os dois baldes, e
`ferramentas/mutacoes-ambiente-do-produto-do-rejunte.py` nova (**21 de forma + 7 de tela, 5 falsos
positivos**). Nenhuma URL nova (segue em **21**), nenhuma página criada.

## 1. O BALDE DA REGRA 2 FOI RENOMEADO, E ISSO A BATERIA DA COLA NÃO PRECISOU FAZER

Na cola, o balde da regra 2 já se chamava `eliminados_por_silencio` — nome preciso. Aqui ele se chamava
`eliminados_por_ambiente`, e **o nome ficou falso no instante em que passou a existir um segundo balde de
ambiente**: as duas causas são "por ambiente", e um nome que descreve as duas não distingue nenhuma. Ele
passa a ser `eliminados_por_ambiente_critico`. **Renomeado, não apagado** — a mesma convenção que a v14 usou
em `substratos_que_o_documento_declara`; quem procurar o nome velho está lendo história.

## 2. SÃO **DUAS** TELAS, E ERA ISSO QUE A COLA NÃO TINHA

A célula do rejunte é lida pela F2 **e pela F1**, que serve a vitrine de rejunte por folga. As duas serviam a
frase errada, com palavras diferentes: a F2 dizia *"Fora porque o fabricante não declara este lugar"*; a F1,
*"o que ele não declara é peça ao ar livre"*. **Conserto que chegasse a uma só trocaria uma tela mentindo por
duas telas discordando** — e é isso que a `t06` da bateria guarda. O bloco de travas do esquema cobra
`secao_propria_na_F2` **e** `secao_propria_na_F1`, em campos separados, e a `m07` e a `m08` medem as duas.

## 3. A MATRIZ NUNCA SERIA A RÉGUA DESTA REGRA, E O NÚMERO MOSTRA POR QUÊ

Das nove células da `matriz_esperada_do_rejunte`, a regra 3 toca **duas**: `2 mm × externo_exposto` e
`3 mm × contato_permanente_agua`. A grade dela foi escolhida pelas **bordas de junta** — 1, 2, 4, 5, 10 e 11
mm —, e grade escolhida por borda de junta não cobre regra de ambiente. As cinco âncoras existem para pisar
nos estados que ela não visita, e quatro das cinco são estados que a matriz não tem.

## 4. A ÂNCORA PRÓPRIA DESTA REGRA É A DO ESTADO **SEM A OUTRA CAUSA**

Em **7 dos 8** estados a regra 2 também morde, e ali a frase errada se esconde atrás da certa. O oitavo é
`1 mm × contato_permanente_agua`: o balde da regra 2 está **VAZIO** e o da 3 tem o acrílico. Naquele estado,
se a tela servir "o fabricante não declara este lugar", a frase só pode ser sobre o acrílico e só pode ser
falsa. **Estado sem a outra causa é onde a frase errada não tem onde se esconder** — e o validador cobra que
exista uma âncora assim.

## 5. E A FUSÃO MAIS PROVÁVEL AQUI NÃO É COM O SILÊNCIO: É COM A FAIXA DE JUNTA

Na cola, a âncora anti-fusão media o balde do silêncio. Aqui a regra 1 roda **antes** da 3, e de 5 mm para
cima o acrílico sai por **folga**, não por lugar. Quem implementar "produto que delimita ambiente e não cobre
o lugar vai para o balde novo" põe no balde quem **nem cabe na folga** — e a elegibilidade continua idêntica
nos 60 estados. A âncora de `5 mm × externo_exposto` é essa, a `t05` é a mutação dela, e a `m14` é a trava
que impede a âncora de sair da tabela.

## 6. TRÊS COISAS QUE A BATERIA ACHOU NAS RÉGUAS DESTE PRÓPRIO BLOCO, as três antes do commit

**(a) A `m15` PASSOU, e a trava da "âncora que passa" estava fraca.** Ela contava âncora com o balde novo
vazio — e com isso a âncora **anti-fusão de 5 mm já ocupava o lugar da que passa**, porque ali o balde está
vazio mesmo: o produto saiu pela folga. Apagar a única âncora em que o acrílico aparece **recomendado**
deixava a tabela verde, e com ela uma regra 3 que tirasse o produto dos três ambientes que o fabricante
declara. **Balde vazio não prova que a regra deixa passar: prova que ela não morde ali, e as duas coisas se
separam exatamente no produto que outra regra já tirou.** A trava passou a exigir um delimitador em
`recomendados_topo`.

**(b) A `m17` PASSOU, e achou que `ambientes_declarados` ILEGÍVEL desliga a regra 3 em silêncio.** Ela dava
`áreas internas` ao epóxi para criar um segundo delimitador. O literal não está no
`mapa_de_termos_do_rejunte`, então `ambientes_delimitados` ficou **vazio**, a regra 3 não se aplicou, e o
único efeito foi um **`aviso`**. E nos outros dois campos de declaração um termo ilegível **encolhe** o
produto — ele deixa de cobrir um ambiente e perde pontos, e aviso basta. Em `ambientes_declarados` ele
**alarga**: perder a leitura da frase que FECHA o produto é o mesmo que não ter a frase. Virou **erro** no
validador, a `m17` passou a usar um literal que o mapa conhece, e a **`m21`** nasceu do achado.

**(c) A `t01` e a `t03` mutavam a régua da COLA.** As duas linhas que elas procuravam —
`return array( 'ambiente_do_produto', 0 );` e `$lits = $p['literais_delimitacao'];` — existem **duas vezes**
no arquivo, idênticas, e a da cola vem antes. A bancada ficou vermelha pelo motivo errado, que numa bateria é
pior que verde, porque conta como mutação pega. As duas foram reancoradas no bloco que só existe na régua do
rejunte. **Marcador que existe nas duas réguas não mede nenhuma das duas** — é a mesma família da cicatriz
que a `t03` da bateria da cola e a `t04` da `mutacoes-par.py` já tinham escrito, com outro literal.

**E a `fp4` saiu INERTE**, apanhada pelo canário de inércia: ela reescrevia o literal com o **mesmo valor**
que já estava lá. Virou outra coisa — o delimitador aprendendo uma declaração que confirma um ambiente que
ele já cobre. E fica escrito por que o conserto óbvio não servia: acrescentar um segundo literal de ambiente
ao registro **tem de reprovar**, porque o perfil escrito à mão carrega `literais_delimitacao`.

## 7. UM CONSUMIDOR PERDIA O BALDE E UMA MUTAÇÃO IRMÃ IA QUEBRAR

`cobertura.py` servia *"o fabricante nao declara este ambiente"* no censo dos 60 estados, e os **8** da regra
3 estão todos entre as `faixas_descobertas` — então a causa saía errada em 8 de 8. Agora o censo carrega os
dois baldes e a `causa_do_rejunte` compõe até três frases. E a
`m_f2_a_vitrine_ganha_um_produto_que_a_frase_nao_nomeia`, da `mutacoes-prestacao.py`, nomeava o balde velho
**no texto de substituição**: deixada como estava ela continuaria aplicando (a busca é no código não mutado)
e produziria PHP com chave inexistente — **bancada vermelha pelo motivo errado**. Ela passou a empurrar os
dois baldes.

## 8. E A FRASE SAIU DA TELA COM O SUJEITO ERRADO, lida no render antes do commit

A primeira versão dizia *"Rejunte Acrílico Quartzolit — a Saint-Gobain Weber **cabe nessa folga**"*: quem
cabe na folga é o produto, não o fabricante. Nenhum portão lê concordância, e as duas bancadas estavam
verdes. Corrigida para *"— cabe nessa folga, e a Saint-Gobain Weber fechou o produto inteiro em outros
lugares"*. **Portão que mede presença de frase não mede frase que não se lê.**

## O que NÃO mudou, e é o que explica o bloco inteiro

**A elegibilidade é idêntica em 60 de 60 estados.** `recomendados_topo`, `elegiveis_abaixo_do_topo`,
`mencionados_com_ressalva` e `eliminados_por_faixa_de_junta` não se movem. As 8 entradas saíram de uma lista
de eliminados para outra. **Trocar de balde não muda número nenhum, e é por isso que toda régua desta ilha
atravessou o defeito desde 10/09/2026: todas mediam CONCORDÂNCIA entre o banco e a página, e as duas
concordavam dizendo a mesma coisa errada.** Portão que compara listas de elegíveis nunca pegaria isto; só
portão que compara FRASES pega — e desta vez em duas telas.

## O próximo bloco, e ele é o primeiro de CRESCIMENTO depois de quatro de portão

Está escrito no `PROMPT.md`: a **segunda categoria do Guia, pelo `alicate`** — **coleta de 5 itens de
banco** (2 em `alicate/torques`, 3 em `alicate/martelinho`), depois as SERPs, depois mãe + 3 filhas: **4
URLs, e a ilha vai de 21 para 25.**

**E ao escolhê-lo esta execução achou que DUAS frases desta fila estavam erradas pelo mesmo motivo — a
16.5, que ninguém tinha contado.** O item 3 da fila, de 02/10, diz que *"o que destrava a
`alicate/cortador_de_azulejo` é medir a SERP de `alicate` — busca, não coleta"*. **Medir a SERP não destrava
nada:** a 16.5 exige **3 filhas com dado real** para a página de nível 2 nascer, e `alicate` tem **1**. SERP
medida numa categoria de uma filha dá categoria que não pode ser publicada. A primeira versão desta própria
entrada repetia o erro e dizia "mãe + 2 filhas, 21 para 24" — **corrigida antes do commit, contando as
filhas de todas as sete categorias** em `resumo.por_categoria_do_guia` de `dados/filhas-do-guia.json`, um
campo que o `filhas-do-guia.py` já escrevia e que nenhuma execução tinha lido inteiro.

**E o mais barato na conta não é o mais barato na realidade.** O `rejunte` pede **4** itens contra **5** do
`alicate` — e os 4 dele são `rejunte/acrilico` e `rejunte/epoxi`, cujo dado que falta é **faixa de junta**,
que mora em **boletim técnico**, e a medição de 05/10 às 19h3xZ fechou essa porta com nome e escreveu *"NÃO
REPITA A COLETA"*. Os 5 do `alicate` são **ferramenta, não química**: medida, material e mecanismo, que
página de fabricante e ficha de marketplace publicam. **Contagem de itens não é custo; custo é de onde o
dado vem.**

**E uma linha que o próximo bloco carrega de carona, medida aqui:** a trava do literal ilegível em
`ambientes_declarados` que a `m17` fez nascer existe **só para o rejunte** — ela mora dentro do
`if rejuntes`. A cola tem três produtos com `ambientes_declarados` e **os três literais traduzem hoje**,
então o buraco é **latente, não ativo**. É uma linha de código e uma mutação, não um bloco.

07/10/2026 11h05Z — A REGRA 3 MANDAVA PARA O BALDE DO SILÊNCIO QUEM O FABRICANTE DECLARA, E A PÁGINA DIZIA QUE ELE NÃO FALA; O BALDE PRÓPRIO FECHA 29 ENTRADAS EM 24 CÉLULAS, SEM UM CAMPO NOVO

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h17Z**, push da reserva aceito na primeira
tentativa (`0ffb01f`). Pela **1.2** não houve escolha a fazer: o `foco.md` nomeia esta ilha e a rotação da
seção 1 está suspensa. O cabeçalho estava com `executando_desde: null`, que pela **1.1** já basta — a reserva
é escrita ANTES do trabalho, então `null` significa que nenhum bloco da Fundação está vivo e não houve reserva
vencida para o git desempatar; o último commit na pasta era de **06/10 às 21h50Z**, doze horas e meia antes,
e era o fecho da execução anterior. `git fetch origin main` trouxe 20 commits; a branch `claude/*` local
estava **idêntica ao `main`** e nenhum PR aberto — nada a mesclar. **Rede pela 20.2:**
`https://clubedomosaico.com.br/` em **200** nas três passadas, com `aquametria.com.br` em 200 nas mesmas três.
**Reserva RENOVADA às 10h46Z pela 1.1**, porque o bloco passou de 40 minutos: a bateria nova sozinha leva mais
que isso.

**Nenhum despacho aberto para a Fundação.** O de 05/10 tem os itens 1 e 2 **CUMPRIDOS** e o **item 3** se
declara método endereçado ao Raphael (o anti-robô da Shopee fecha a sessão em 4 a 6 fichas) — li o topo do
`PROMPT.md` antes de escolher, pela 18.1, e não há item acionável. Então o bloco foi **o da fila**, e ele
estava escolhido por escrito, com o número medido, pela execução de 06/10 às 20h4xZ.

Nenhuma URL nova (segue em **21**), nenhuma página criada, nenhum link de afiliado gerado, nenhum teto da
21.4 gasto, nenhuma coleta nova e **nenhum campo novo no banco**. Esquema **v15**, **F2 1.11.0**,
`teste-f2` de 149 para **159** afirmações, bateria `mutacoes-ambiente-do-produto.py` nova.

## O DEFEITO, E POR QUE ELE ATRAVESSOU 27 DIAS E TODA RÉGUA DESTA ILHA

A **regra 3** (`3_ambiente_declarado_DELIMITA`) existe desde o bloco 3 e **sempre eliminou certo**: produto
com `ambientes_declarados` não vazio só é elegível nos ambientes que declara. O que estava errado não era a
eliminação — era **para onde ela mandava o produto**. Ela devolvia `silencio`, e o balde do silêncio serve,
na tela, esta frase:

> *"O fabricante simplesmente não fala desta superfície, e silêncio não vira 'pode'."*

E o fabricante fala. A **regra 2 roda ANTES da 3**, então quem chega na 3 **já passou pela 2 com a base
declarada em `indicado_para`**. O que ele fez foi delimitar o **ambiente do produto inteiro**, que é outro
fato e outra frase.

**É o mesmo defeito que a REGRA 8 consertou um andar acima em 06/10 e é SETE VEZES MAIOR** — 29 entradas
contra 4. A diferença entre as duas é só **onde o qualificador mora**: na 8 ele vem colado no substrato,
dentro da frase que nomeia a superfície (`Alvenarias de blocos (...) em paredes internas`); na 3 ele é
**campo do produto** e vale para todas as superfícies dele (`uso interno`).

**POR QUE NENHUMA RÉGUA O VIU, e esta é a lição do bloco:** todas as réguas desta ilha mediam
**CONCORDÂNCIA** entre o que o banco calcula e o que a página serve — a matriz de 45 células, o censo de 270
estados, as oito bancadas PHP, as 26 baterias de mutação. **As duas concordavam.** As duas diziam a mesma
coisa errada. Trocar de balde **não muda nenhum número**: a lista de recomendados, a de elegíveis abaixo, a
de ressalva e a de proibição são **idênticas em 45 de 45 células** antes e depois deste bloco. Portão que
compara listas de elegíveis nunca pegaria isto. Só portão que compara **frases**, e frase se mede no HTML
servido.

## O NÚMERO, MEDIDO À MÃO ANTES DE O VALIDADOR RODAR — E ELE SÃO DOIS NÚMEROS, NÃO UM

A derivação não passou pela régua: é o cruzamento das **três linhas de `ambientes_declarados` do banco** com
as **bases que cada produto declara SEM qualificador**.

| produto | literal | vale só em | bases declaradas | entradas |
|---|---|---|---|---|
| `cascola-pl500-adesivo-de-montagem` | `uso interno` | `interno_seco` | 6 (cerâmica, cimento, mdf, metal, plástico, vidro) | **24** |
| `cascola-cascorez-extra` | `ambientes internos` | `interno_seco` | 1 (`mdf_madeira`) | **4** |
| `quartzolit-cimentcola-externo-acii` | `área interna e externa` | 4 ambientes (todos menos imersão) | 1 (`cimento_concreto`) | **1** |

**29 entradas em 24 CÉLULAS DISTINTAS, e os dois números são verdadeiros sobre coisas diferentes.** O
registro de 06/10 escreveu "29 células"; são **29 pares (produto × célula)**, e as 4 do Cascorez e a 1 da
cimentcola **caem dentro das 24 do PL500**, porque as bases delas estão entre as seis dele. A linha
`por_que_29_e_nao_24` existe no esquema para a próxima execução não procurar cinco células que nunca
existiram — e o validador recomputa os **dois** números, em campos separados, porque trocar um pelo outro
ficaria verde se fosse um só.

**E a derivação se provou sozinha ao ser aplicada:** cada uma das 29 foi conferida como **presente em
`eliminados_por_silencio`** antes de sair dele. As 24 células reescritas bateram com a recomputação do
validador **sem uma divergência**.

## O MOLDE FOI COPIADO, NÃO INVENTADO — E UMA COISA ELE NÃO FEZ DE PROPÓSITO

O `PROMPT.md` mandava copiar o molde construído duas vezes em 06/10 (regras 7 e 8), e é o que foi feito:
balde próprio (`eliminados_por_ambiente_do_produto`), frase própria que **cita o literal de
`ambientes_declarados`** e não o nosso vocabulário (26.3, **quarta** aplicação), a regra escrita com a
**ordem** (ela não mudou de lugar: continua entre a 8 e a 4), as células da matriz reescritas à mão antes do
validador, e bateria com as duas direções e trava de falso positivo.

**E o que ele NÃO fez, porque o `PROMPT.md` proibiu com todas as letras:** juntar a regra 3 com a 8 num balde
só. São frases diferentes para fatos diferentes — *"ela declara esta superfície, e declara com o lugar dentro
da frase"* é sobre a SUPERFÍCIE; *"ela declara esta superfície, e delimitou o produto inteiro a outros
lugares"* é sobre o PRODUTO. Os dois baldes **nunca carregam o mesmo produto na mesma célula**, porque a 8
roda antes e quem ela pega sai por ela — e isso é **invariante varrida nas 45**, não promessa escrita.

## O QUE A TELA DIZ AGORA, E A DIFERENÇA ENTRE AS DUAS FRASES NA MESMA SEÇÃO

Em `mdf_madeira` × `externo_abrigado` (varanda coberta, caco de azulejo), a seção "o que não usar" passou a
dizer, em parágrafo próprio e em cor de legenda como os outros quatro:

> **Cascola PL500 Adesivo de Montagem** — a Cascola declara esta superfície, e delimitou o produto inteiro a
> outros lugares: ela escreve *uso interno*. Então ele fica de fora deste caso — não por proibição e não
> porque ela tenha ficado calada sobre a superfície, e a diferença importa: ela falou da superfície, e disse
> onde o produto pode ir.

A seção tem **cinco causas** agora, e nenhuma é mais importante que as outras — o que muda é a frase. **E o
CSS do balde da regra 8 entrou junto:** ele nasceu em 06/10 **sem regra própria** e vinha saindo em cor de
corpo, o que o fazia parecer a resposta em vez da ressalva. Uma linha, os dois no mesmo seletor.

## DOIS CONSUMIDORES PERDIAM OS DOIS BALDES, E O DA REGRA 8 JÁ PERDIA DESDE 06/10 — COM O NÚMERO

Mover 29 entradas para fora do silêncio **sem trazê-las para os consumidores** repetiria o defeito um dia
depois e sete vezes maior. Ao abri-los, o buraco de ontem estava lá:

- **`ferramentas/cobertura.py`** (o censo de 270 estados) não carregava `eliminados_por_ambiente_do_substrato`:
  em **24 dos 270 estados** a cimentcola caía nele e **desaparecia de toda causa** — não estava no silêncio
  (certo) e não estava em lugar nenhum (errado). Os dois baldes entraram, e `causa_da_cola()` ganhou as duas
  frases, **depois** das anteriores na ordem, porque as duas são as **menos acionáveis** do censo: quem cai
  nelas não tem conserto do lado de quem lê a página.
- **`snippets/clubedomosaico-tecnicas.php`** (a grade de 45 células por caquinho) tinha o mesmo buraco, e o
  comentário do balde da peça, escrito dois dias antes, já havia nomeado a família: *"balde que o cálculo
  separa e a grade não carrega é produto que a tela pode esquecer sem ninguém ver"*.
- **`ferramentas/teste-tecnicas.php`** passou a contar os dois baldes. Sem isso, tirar 29 entradas do silêncio
  **baixaria a contagem de silêncio da página sem nada cobrar a contagem nova**, e o portão ficaria verde
  sobre uma página que perdeu uma frase.

**Medido depois, no censo regerado:** **144 dos 270** estados de cola carregam o balde da regra 3 (174
entradas) e **24** carregam o da regra 8. **E ZERO `por_que` mudou nos 270** — em toda célula afetada já havia
outro produto no silêncio ou na proibição, então a frase do censo não mentia: ela estava **incompleta**. Dito
assim porque a diferença importa.

## O QUE A BATERIA NOVA ACHOU NAS MINHAS PRÓPRIAS RÉGUAS — DUAS COISAS, E AS DUAS ANTES DO COMMIT

**(1) A `m01` PASSOU: a trava do bloco ausente ficou sem ninguém do outro lado.** Ela foi escrita junto com as
outras travas de forma, no topo do `validar-banco.py`, onde `materiais` **ainda não existe** — o arquivo
morreu com `NameError`. Movi a lista de produtos para a seção das âncoras e **deixei para trás um `if` sem
nada do outro lado**: apagar o bloco inteiro do esquema não reprovava nada. É a direção desta regra escrita no
próprio defeito — **perder o balde não muda elegibilidade, muda a FRASE, e frase não tem portão natural.**
Consertada, a m01 reprova com a mensagem inteira.

**(2) A `m14` PASSOU E NÃO ERA DEFEITO — ela mudou de lado.** Escrita como "nasce o termo do quarto
delimitador", ela acrescentava ao mapa um termo com `ambiente` e esperava reprovação. Ninguém a pegou, **e com
razão**: termo que registro nenhum cita **não delimita nada**, exatamente como o termo com qualificador que
ninguém cita é falso positivo na `mutacoes-par.py` (fp3). Virou a **fp5** aqui. **Mutação que passa com razão
não se conserta para reprovar: ela troca de lado.** O que produz o mundo é a metade do REGISTRO, e ela não
precisava da outra — o literal `ambientes internos` já está no mapa desde que o Cascorez entrou.

**E uma coisa que a bateria mediu sobre si mesma:** a âncora anti-fusão que escrevi à mão listava **três**
produtos em `eliminados_por_silencio` de `espelho` × `interno_seco` — os três que delimitam ambiente, que era o
que ela existia para provar — e o balde daquela célula tem **cinco**: o Durepoxi e o Acético Maxx também não
declaram espelho. O validador a reprovou na primeira passada. **Âncora de um balde tem de trazer o balde
INTEIRO**, senão ela mede a presença de quem o autor lembrou, não a lista que a tela serve. Corrigida, com o
motivo escrito ao lado dela no esquema.

**E DOIS MARCADORES DE MUTAÇÃO ERAM RUINS, os dois pela mesma razão e a razão já estava escrita.** A `t03`
procurava o literal cru `uso interno` para provar que ele saiu da tela, e **a mutação PASSOU**: a frase *"o
produto é declarado para uso interno"* está no **FAQ desta mesma página**, no JSON-LD e no `<dd>`, e continua
lá depois da mutação. A `t04` tinha o mesmo problema com `madeira`, que é o próprio rótulo da base. **Marcador
que existe nos DOIS lados da mutação não mede nada** — e é a cicatriz exata que a `t04` da `mutacoes-par.py`
escreveu **um dia antes**, com outro literal. Os dois passaram a procurar a citação inteira, com a tag dentro,
e o da `t04` foi **medido na tela mutada** antes de ser escrito, não suposto.

## A ESPECIFICAÇÃO TAMBÉM NOMEAVA A CAUSA ERRADA, E ELA É LIDA POR QUEM ESCREVE BLOCO

`dados/especificacao-calculadoras.md`, seção 1.3, linha de **MDF/madeira × molhado ou externo**, dizia *"o
fabricante do PVA não declara uso externo nem resistência a água, e a ilha não transforma silêncio em
recomendação"*. A eliminação está certa; a palavra **silêncio** está errada pelo mesmo motivo que estava na
tela — o fabricante do PVA **declara** MDF em `indicado_para` e **escreve `ambientes internos`**. Acertada, com
nota datada ao lado da tabela. **Nenhum portão lê essa prosa** (conferido: só o `validar-banco.py` cita o
arquivo, e numa linha de comentário sobre geometria de placa), então não é régua — é **relatório velho, e
relatório velho também mente**, que é a lição que a execução de 06/10 deixou escrita neste mesmo `PROMPT.md`.

## A BANCADA, E ELA TEM UMA METADE QUE NÃO RODOU E ESTÁ NOMEADA

**Verde e rodado:** `validar-banco.py` (as 45 células da F2, com a linha nova do resumo — **29 entradas em 24
células, 3 produtos que delimitam, 5 âncoras**), `cobertura.py` regerado e `--conferir` verde nos 270 + 60
estados, `teste-f2.php` de 149 para **160** afirmações, e a bateria nova
`mutacoes-ambiente-do-produto.py`: **16 de 16 de forma reprovadas, 12 só pelo portão novo; 6 de 6 de tela;
5 de 5 falsos positivos passaram.** A `mutacoes-par.py` da regra 8 foi **reconferida** depois das mudanças e
segue **17 de 17, 5 de 5, 4 de 4**. As duas baterias da técnica, que este bloco tocou, fecham **14 de 14
decididas certo** cada uma (`mutacoes-tecnicas-pagina.py` e `mutacoes-tecnicas.py`).

**As oito bancadas PHP irmãs, reconferidas:** casca **744**, guia **110**, técnicas **139** (depois do
conserto), loja APROVADO, leads APROVADO, f1 **228**, ateliê APROVADO, prestação-rejunte **5** sobre 540+180
estados.

**AS 22 BATERIAS DE MUTAÇÃO RESTANTES NÃO RODARAM, e ficam nomeadas em vez de resumidas:** cobertura,
tecnica-x-material, pastilhas, apoio, base, rejunte, acabamento, degrau, forma-do-degrau, motivo-degrau-4,
batismo, casamento, f1, arvore, voz-e-cabeca, promessa-do-titulo, divulgacao, prestacao, loja, leads, atelie e
ga4. Somam ~350 mutações e a varredura inteira é de horas. O que elas cobrem é regressão de blocos
ANTERIORES; o que **este** bloco mexeu está coberto pela `mutacoes-ambiente-do-produto`, pela
`mutacoes-par` e pelas duas da técnica, que rodaram. **Escrever "todas verdes" sem as ter rodado seria
afirmação com escopo maior do que o medido.**

## O DESEMBARQUE E A CONFERÊNCIA NO AR, PELA 18.4

**Sync acionado pela própria Fundação às 11h02Z: revisão 65, 15 de 15 aplicados, ZERO linha divergente** — e o
que fecha é o log sem divergência, não o número da revisão (cicatriz de 06/10, quando a revisão 63 subiu com
três sha divergentes e um `/status` verde sobre página velha). `/status` na **65**, igual à do `manifest.json`.

- `conferir-no-ar.py`: **APROVADO, 524 afirmações no HTML servido, 0 falha.**
- `leitura-do-visitante.py`: **REPROVADO com EXATAMENTE 1 defeito**, o soft 404 na borda — o vermelho esperado
  do hospedeiro e do Raphael desde 29/09 (404 na 1ª leitura, 200 na 2ª). **Nenhum defeito novo.**

**E A ENTREGA LIDA NO AR, NAS TRÊS PONTAS**, em `/materiais/qual-cola-usar-no-mosaico/`, com quebra de cache e
`Accept-Encoding: identity`:

1. **`mdf_madeira` × `externo_abrigado`** (a regra morde) — os **dois** Cascola no balde novo, cada um citando
   o literal dele: *"a Henkel declara esta superfície, e delimitou o produto inteiro a outros lugares: ela
   escreve **ambientes internos**"* e *"... ela escreve **uso interno**"*. E o parágrafo do **silêncio** da
   mesma célula passou a nomear **só** a cimentcola e o Acético Maxx — os dois Cascola **saíram** dele, que era
   exatamente onde eles estavam.
2. **`mdf_madeira` × `interno_seco`** (a regra passa) — **nenhum** parágrafo de ambiente. A regra não morde no
   lugar que o fabricante declara.
3. **`alvenaria_tijolo` × `externo_abrigado`** (a regra 8) — **só** o parágrafo da regra 8, citando as duas
   frases do boletim com o lugar dentro delas. **Os dois baldes não se cruzam e as frases são diferentes**,
   lido na página e não por régua.

## O PRÓXIMO BLOCO ESTÁ ESCOLHIDO E É O MESMO DEFEITO UM ANDAR ABAIXO, NO REJUNTE — COM O NÚMERO MEDIDO

Varrido nos **60 estados** da F2 de rejunte (12 larguras de junta × 5 lugares) nesta mesma execução: o balde
`eliminados_por_ambiente` do rejunte carrega **DUAS causas** sob **uma frase só**, *"Fora porque o fabricante
não declara este lugar"*.

- **Regra 3 (delimitação):** **8 entradas em 8 estados**, todas do `quartzolit-rejunte-acrilico`, que escreve
  `áreas internas e externas` em `ambientes_declarados`. Para essas oito a frase é **a mesma mentira que a cola
  servia**: ele declara, e declarou outro lugar.
- **Regra 2 do rejunte (ambiente crítico exige declaração explícita):** **59 entradas em 28 estados**, em
  quatro produtos. Para essas a frase está **certa**.
- **E 7 dos 60 estados carregam as DUAS ao mesmo tempo**, no mesmo parágrafo, sem o leitor poder saber qual
  frase vale para qual produto.

**É menor que o da cola (8 contra 29) e é o mesmo molde**, já construído três vezes: balde próprio, frase
própria que cita o literal de `ambientes_declarados`, a ordem escrita, âncoras à mão e bateria com as duas
direções. **Sai inteiro numa execução só.**

**E uma coisa que o próximo bloco NÃO deve fazer:** reaproveitar as funções da cola. O rejunte tem régua
própria **de propósito** e a razão é de conteúdo antes de método — na cola a lista do fabricante nomeia a
BASE sobre a qual se cola; no rejunte, a TESSELA que será rejuntada e o ambiente. Rejunte não toca a base.

**E o que NÃO é bloco e destrava quatro registros de uma vez** (herdado, segue valendo): `*.quartzolit.weber`
na lista de rede (`dados/despachos.md`, ABERTOS). O `www.` já responde **403**, então o curinga pode entrar e o
403 ficar — 403 é decisão do fabricante, não da rede do Raphael.

**E A TERCEIRA COISA QUE A BATERIA ACHOU NA MINHA PRÓPRIA RÉGUA É A MAIS IMPORTANTE DE TODAS: a `t05`
PASSOU, com a bancada VERDE.** Ela troca a frase do balde da regra 3 pela da regra 8, **palavra por palavra** —
e **juntar as duas frases é exatamente o que o `PROMPT.md` deste bloco proibiu com todas as letras**. A seção
10 que eu havia escrito media a **presença** do nome do produto, do literal e a ausência da palavra do
silêncio; os três continuam ali depois da fusão, então ela aprovou. **Era a única coisa que nenhuma afirmação
olhava, e era a coisa que o bloco existia para não fazer.** Virou afirmação nas **duas direções** (a frase
característica de cada balde: a da 3 fala do PRODUTO, a da 8 fala da frase que nomeia o SUBSTRATO), e com ela
o `teste-f2` foi de 159 para **160**. **Régua que mede presença não mede troca de frase** — e esta ilha acabou
de pagar isso duas vezes no mesmo dia, uma na tela e uma na bancada.

## E A PÁGINA DA TÉCNICA ESTAVA PUBLICANDO UMA LISTA DE CAUSAS INCOMPLETA DESDE 06/10 — ACHADO PELO PORTÃO NOVO

Com os dois baldes contados, `teste-tecnicas.php` **reprovou**, e com razão. Em
`/como-fazer/o-que-e-picassiete/`, a recusa da **Argamassa Cimentcola Externo AC-II** dizia *"o fabricante não
declara essa superfície em **36** das 45; ... no caquinho desta técnica em **5** das 45"* — **41 de 45**, e as
**4** que faltavam eram o balde da regra 8, nascido em 06/10 e nunca carregado por esta grade. Além disso,
**uma** das 36 estava sob a causa errada (é a célula que hoje virou `amb_produto`).

**Nenhum portão viu porque a afirmação que soma confere o TAMANHO DO BANCO, não a soma das causas de cada
produto** — 7 colas nomeadas é 7 colas nomeadas, mesmo que uma delas publique 41 de 45 células.

A página passa a servir **as quatro causas, somando 45 de 45**:

> **Argamassa Cimentcola Externo AC-II Quartzolit** — o fabricante não declara essa superfície em **35** das 45;
> o próprio fabricante escreve que não se usa esse produto no caquinho desta técnica em **5** das 45; o
> fabricante declara essa superfície com o lugar dentro da frase, e o lugar não é esse em **4** das 45; o
> fabricante declara essa superfície e delimitou o produto inteiro a outros lugares em **1** das 45.

A lista digitada de baldes do snippet das técnicas tinha **cinco** e a grade já carregava o sexto; agora são
**sete**, com frase própria para cada. `teste-tecnicas` volta a **APROVADO, 139 verificações**.

---

06/10/2026 20h42Z — O BOLETIM DECIDE AMBIENTE POR SUBSTRATO E O BANCO DECIDIA POR PRODUTO; A REGRA 8 FECHA OS TRÊS BLOQUEIOS DE UMA VEZ, E O TERCEIRO SAIU SEM CAMPO NOVO

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **19h17Z**, push da reserva aceito na primeira
tentativa (`67577b7`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta; o último commit na pasta era de **17h45Z**, uma hora
e meia antes, e era o fecho da execução anterior. Nenhuma branch `claude/*` à frente do `main` e nenhum PR
aberto. **Rede pela 20.2:** `https://clubedomosaico.com.br/` em **200** nas três passadas, com
`aquametria.com.br` em 200 nas mesmas três. **Reserva RENOVADA às 20h21Z pela 1.1**, porque o bloco passou
de 40 minutos — a bancada desta ilha sozinha leva mais que isso.

**Nenhum despacho aberto para a Fundação** — o de 05/10 tem os itens 1 e 2 fechados e o 3 se declara
método endereçado ao Raphael. Então o bloco foi **o da fila**: o candidato **(b)**, escolhido por escrito
pela execução de 17h45Z e o único dos dois que restava.

Nenhuma URL nova (segue em **21**), nenhuma página criada, nenhum link de afiliado gerado, nenhum teto da
21.4 gasto, nenhuma coleta nova. Esquema **v14**, **F2 1.10.0**, manifest e `/status` conferidos na mesma
revisão, Sync acionado pela própria Fundação.

## O QUE O BLOCO ERA, E A PRIMEIRA COISA QUE ELE FEZ FOI LER O CAMPO

O candidato (b) estava escrito como "o campo de par substrato × ambiente, decisão de esquema". Lido o
campo que o nomeava — `materiais-colas.json / quartzolit-cimentcola-externo-acii / fontes /
bt-cimentcola-externo-2016-05 / substratos_que_o_documento_declara_e_que_NAO_foram_gravados` —, ele já
trazia a leitura inteira da seção 4.1 do boletim, feita em 05/10 e confirmada em 06/10: **três frases de
substrato, e DUAS delas com o lugar colado dentro da frase.**

- `Emboço, alvenaria e contrapiso em áreas internas, curados há pelo menos 14 dias, conforme NBR 13.754.`
- `Paredes de concreto curado há 180 dias.`
- `Alvenarias de blocos vazados de concreto, de blocos silicocalcários e de blocos de concreto celular em paredes internas, conforme a Norma Técnica NBR 13.754.`

**O banco decidia ambiente por PRODUTO** (`declaracoes.ambientes_declarados`, regra 3) **e o documento o
decide por SUBSTRATO.** Sem campo para o par havia duas saídas e as duas mentiam, em direções opostas:
deixar as três frases fora de `indicado_para` manteve a argamassa **eliminada por silêncio nas 45 células
de 10/09 a 06/10** — 26 dias dizendo ao leitor que a Quartzolit não fala de concreto, quando ela fala com
número de norma dentro; gravá-las sem o qualificador faria a F2 recomendar argamassa de assentamento em
`alvenaria_tijolo` + `externo_abrigado`, que nesta ilha é **muro de mosaico ao ar livre**, caso em que o
documento não declara nada.

## A DECISÃO DE ESQUEMA, E ELA FOI DE ONDE O CAMPO MORA ANTES DE SER DE FORMA

O par **não** virou campo do registro. Ele é **tradução**, e tradução desta ilha mora num lugar só e
auditável (26.2): o campo novo é `ambiente_que_qualifica_a_base`, numa linha de
`mapa_de_termos_do_fabricante.termos`, e **a fronteira da frase é a fronteira do par** — nada de
sub-parsear a sentença. Gravar o par dentro do registro criaria a segunda cópia da mesma declaração, que é
exatamente o que a execução de 17h45Z pagou no campo da sobra.

**A REGRA 8** roda **entre a 1 e a 2**: depois da 1 porque proibição continua sendo a afirmação mais forte
(o Silicone Acético Construção indica E proíbe `alvenaria`, e tem de sair pela proibição); **antes da 2**
porque a 2 é a regra do SILÊNCIO e aqui não há silêncio — ele falou desta superfície, e falou colando um
lugar na frase. Quem cai nela vai para um balde próprio, `eliminados_por_ambiente_do_substrato`, com seção
e frase próprias na tela. É a **quarta causa** de não-recomendação da resposta da cola, e a quinta no total
com a da peça.

**E A METADE QUE SE ERRA É A UNIÃO.** O qualificador estreita **só o par que a própria frase cria**; ele
nunca estreita outra frase do mesmo fabricante. `cimento_concreto` é declarada pelas paredes de concreto
**sem** qualificador, então fica declarada larga — nos quatro ambientes que o produto delimita.
`alvenaria_tijolo` é declarada **só** por frases qualificadas, então vale só em `interno_seco`.
Implementação que INTERSECTA publica menos do que ele escreveu; a que ignora o qualificador publica mais.
**As duas direções têm mutação própria** (t04 e t01), e é por isso que esta régua virou bateria em vez de
duas afirmações a mais.

## O TERCEIRO BLOQUEIO CAIU SEM CAMPO NOVO, E ERA ISSO QUE "JUSANTE" QUERIA DIZER

A cura de 180 dias estava gravada desde 05/10 e **fora da tela**. A execução de 17h45Z mediu, varrendo os
45 estados um render por estado: **zero** serviam a frase. O motivo é que o bloco de `preparo` só alcança
quem a página **recomenda** — e o produto era eliminado por silêncio em todas as 45. Com o substrato
gravado, a cura entrou **junto com a recomendação**, em dois lugares e nenhum deles novo:

1. a **citação da declaração que fez o produto entrar**, que a F2 serve desde a 1.0.0 — e a declaração é,
   literalmente, `Paredes de concreto curado há 180 dias`;
2. o **bloco de preparo**, que serve a frase do documento inteira, incluindo a instrução que nomeia OUTRO
   produto abaixo dos 180 dias.

**A cura NÃO virou regra de elegibilidade, e isso é decisão escrita e não esquecimento:** ela não tem valor
em vocabulário nenhum e a F2 não pergunta a idade da peça. Transformá-la em regra exige pergunta nova na
ferramenta, que é decisão de interface e bloco próprio. Enquanto não for, a cura é TEXTO — texto citado do
fabricante, no mesmo bloco da recomendação, que é o que esta ilha tem de mais honesto a oferecer sobre uma
condição que ela não mede.

## O QUE MUDOU NO AR: DEZ CÉLULAS, E UMA DELAS MUDOU DE CAUSA SEM MUDAR DE CONTEÚDO

As dez (as cinco de `cimento_concreto` e as cinco de `alvenaria_tijolo`) foram **derivadas à mão das
declarações ANTES de o validador rodar uma vez**, e as dez bateram com a recomputação sem uma divergência.

- `cimento_concreto` × interno_seco: a AC-II **empata com o PL500** em score 4 e a página lista os dois
  como equivalentes — a `ordem_entre_os_elegiveis` proíbe desempatar por gosto.
- `cimento_concreto` × interno_molhado, externo_abrigado: a AC-II **assume o topo sozinha** (4 contra 2 do
  neutro, que declara a base e não declara ambiente).
- `cimento_concreto` × externo_exposto: **empate com o neutro**, as duas passando pela regra 4 por motivos
  diferentes — ela porque `área interna e externa` cobre o exposto, ele porque declara chuva e UV.
- `cimento_concreto` × contato_permanente_agua: **a célula não mudou e a CAUSA mudou.** A AC-II continua em
  `eliminados_por_silencio` e não está mais ali por não declarar substrato: agora declara, e quem a tira é
  a **regra 3**. Fica escrito no próprio esquema que esta célula passou a ter DUAS causas no mesmo balde, e
  que separá-las é o próximo campo que esta ilha vai querer — não é defeito de hoje e não se conserta sem
  bloco.
- `alvenaria_tijolo` × interno_seco: a AC-II **assume o topo**, e é a única das cinco desta base em que ela
  aparece. Fecha a divergência que a seção 1.3 da especificação carregava desde o bloco 3.
- `alvenaria_tijolo` × os outros quatro: **REGRA 8**, com a frase própria.

**E A QUINTA ÂNCORA DA MATRIZ DA PEÇA MUDOU DE LADO, que era o que ela existia para medir.** Escrita de
manhã, quando a AC-II era silêncio nas 45, ela cobrava `eliminados_por_proibicao_da_peca` VAZIO em
`cimento_concreto` × `interno_seco` × `pastilha_vidro`. À noite a argamassa entrou na célula com score 4 e
a **regra 7 a tirou**, pelos dois grupos que ela declara. O `recomendados_topo` não se mexeu: continua só o
PL500. A frase que a regra 7 deixou escrita no dia em que nasceu era exatamente esta — *"com ele, o dia em
que o substrato entrar não será o dia em que a F2 passar a mandar colar pastilha de vidro com argamassa que
proíbe revestimento especial"*.

## TRÊS DEFEITOS ACHADOS PELO CAMINHO, E NENHUM DELES ERA DO BLOCO

**(1) O "TROQUE POR ISTO" DA REGRA 7 OFERECIA UM CAQUINHO QUE O MESMO PRODUTO PROÍBE — e estava no ar desde
hoje de manhã.** A saída era calculada sobre os grupos que **morderam aquele caquinho**, não sobre os que o
produto **declara**. Com `pastilha de cerâmica` no formulário, só `revestimento_especial` morde, e a saída
calculada sobre ele sozinho oferecia `caquinho de louça ou prato` — que `baixa_absorcao_de_agua`, o outro
grupo da mesma argamassa, proíbe. **A página mandava trocar um caquinho proibido por outro caquinho
proibido, com o nome do fabricante embaixo.** Não apareceu antes porque o mundo não se movia: o único
produto com proibição de peça elegível até hoje declarava UM grupo, e com um grupo as duas contas dão o
mesmo número. **Campo que só erra quando o mundo se move parece certo até o mundo se mover** — e quem o
pegou foi uma afirmação que a própria regra 7 escreveu de manhã e que nunca tinha tido um mundo em que
morder.

**(2) A SEÇÃO 5 DO `teste-f2.php` MEDIA A CAMADA ERRADA.** Ela parte da matriz escrita à mão (declaração:
regras 1 a 5 e 8) e compara com a página servida (que é a declaração MENOS as regras 7 e 6) — e descontava
só a regra 6. Faltava desde que a 7 nasceu, de manhã, e era invisível porque nenhum produto com proibição
de peça era elegível em célula nenhuma. As quatro células de cimento falharam de uma vez, cada uma
acusando que a tela não recomendava quem a matriz manda. **A matriz estava certa e a tela estava certa: era
a régua que media a camada errada.** Agora ela desconta as duas, na ordem do esquema, e cobra as duas
metades — que caiu da recomendação e que apareceu na página.

**(3) O `recorte_do_documento` DO `preparo` AFIRMAVA UMA COISA QUE METADE DELE DESMENTIA.** Escrito às
14h10Z, ele dizia que as **duas** frases de alvenaria com qualificador de ambiente `ficaram fora`, com o
motivo certo (*"citá-lo pela metade na tela seria decidi-lo sem campo"*). Só que `em áreas internas`
**nunca ficou fora**: ela é a PRIMEIRA sentença do literal servido desde aquela hora, com o qualificador
dentro. Só a terceira frase tinha de fato ficado fora. Como a página não recomendava ninguém ali, a frase
falsa foi invisível em vez de inofensiva. **Mesma família do defeito da sobra, seis horas depois: prosa de
registro copiada da anterior sem ninguém abrir o campo ao lado.** A terceira frase entrou no literal
(a v14 deu o campo que faltava) e a prosa foi corrigida para dizer o que o recorte faz.

## A BATERIA ACHOU DOIS BURACOS NAS MINHAS PRÓPRIAS RÉGUAS, E UM DELES ERA UMA FIXTURE QUE DESLIGAVA A RÉGUA

**A m12 PASSOU na primeira rodada.** Dar qualificador a um termo de `nao_indicado_para` não mudava nada —
porque a leitura da proibição é **ampliativa de propósito**, e é assim que ela tem de ser. Passar verde
aqui é pior do que parece: o campo fica **gravado, sem efeito e sem uma palavra**, e a próxima execução o
lê como *"proibido só naquele lugar"*, que é o avesso do que a régua faz. É a família inteira de defeitos
desta ilha num campo só. A trava nova é no **USO** e não no mapa: o mesmo literal pode ser indicação num
produto e proibição noutro, e recusá-lo no mapa tiraria o campo de quem tem direito a ele.

**E A `fp2` REPROVOU, e a reprovação estava certa.** A primeira versão dela alargava o qualificador para os
CINCO ambientes dizendo que *"isso é o mesmo que não ter qualificador"*. É — e nesse mundo a REGRA 8 nunca
morde, e a trava dos dois lados da matriz do par reprova com razão: tabela de âncoras que nunca morde não
mede regra nenhuma. **Não era falso positivo: era uma fixture que neutralizava a própria régua e chamava a
reprovação de defeito.** Trocada por um qualificador de DOIS ambientes, que exerce a união entre duas
frases qualificadas do mesmo produto e deixa a regra mordendo em três células. **Fixture que desliga o
portão é o jeito mais limpo de desligar um portão sem apagar uma linha.**

## O DESEMBARQUE, E O SYNC PRECISOU DE TRÊS ACIONAMENTOS

Manifest **63**, `/status` conferido na **63**, Sync acionado pela própria Fundação. **A primeira
chamada aplicou 12 de 15 e recusou TRÊS com `sha256 divergente`** — `snippets/f2`, `dados/esquema-banco`
e `dados/materiais-colas`, exatamente os três arquivos deste bloco. O manifest novo chegou e os arquivos
novos não: é a janela de cache do espelho que serve os blobs, e ela não se resolve por insistência cega
mas por insistência MEDIDA. Acionado em laço até o log não trazer mais nenhuma linha divergente: **15 de
15 aplicados às 20h42**.

**Fica escrito porque é a cicatriz do próprio ESTADO.md de 05/10, um nível abaixo:** lá treze sha estavam
vencidos no manifest porque ninguém acionou o Sync; aqui o Sync foi acionado e **o `/status` na revisão
certa não quer dizer que os arquivos subiram.** `revisão 63` com três divergentes é um `/status` verde
sobre uma página velha. O que fecha é o log sem `sha256 divergente`, não o número da revisão.

## A VERIFICAÇÃO NO AR (18.4), com o critério que o próprio bloco declarou

- `conferir-no-ar.py`: **APROVADO, 524 afirmações, 0 falha** (eram 508 antes da 25/09; a contagem é da
  ilha, não deste bloco).
- `leitura-do-visitante.py`: **REPROVADO com exatamente 1 defeito, o soft 404 na borda** — 404 na 1ª
  leitura e 200 na 2ª, com `x-proxy-cache: HIT` e `max-age=7200`. É o vermelho ESPERADO, do hospedeiro e
  do Raphael desde 29/09, e **nenhum defeito novo**.
- **A entrega, aberta no ar e lida:** em `cimento` + `fora de casa mas abrigado` + `caco de azulejo`, a
  página recomenda a argamassa e serve, no mesmo bloco, `Paredes de concreto curado há 180 dias. Se curado
  há 28 dias, utilize cimentcola flexível quartzolit.` — a cura E o produto que o fabricante manda usar
  abaixo dela. Em `alvenaria, tijolo ou pedra` + o mesmo lugar e o mesmo caquinho, a mesma argamassa sai
  no parágrafo da REGRA 8, citando as duas frases dele e dizendo, com as nossas palavras, que este caso
  não é aquele lugar.

## E O QUE A REGRA 8 DEIXOU À VISTA É UM DEFEITO MAIOR QUE ELA, COM O NÚMERO MEDIDO

**A REGRA 3 MANDA PARA O BALDE DO SILÊNCIO QUEM O FABRICANTE DECLARA, E A PÁGINA DIZ QUE ELE NÃO FALA.**
A frase da seção do silêncio é *"O fabricante simplesmente não fala desta superfície, e silêncio não vira
'pode'"*, e ela sai hoje sobre produtos cujos fabricantes **falam da superfície** e apenas delimitaram o
ambiente do produto inteiro. **Medido nas 45 células: 29 delas**, em três produtos.

| produto | células | desde |
|---|---|---|
| `cascola-pl500-adesivo-de-montagem` | **24** | 10/09/2026 |
| `cascola-cascorez-extra` | 4 | 10/09/2026 |
| `quartzolit-cimentcola-externo-acii` | 1 | hoje, e por ela a célula não mudou de conteúdo e mudou de causa |

É **o mesmo defeito que este bloco consertou um andar acima**, com uma diferença só: na regra 8 o
qualificador vinha colado no substrato, e na regra 3 ele é campo do produto. E é **sete vezes maior** —
4 células contra 29. Não é defeito de hoje: as 28 primeiras estão no ar desde o dia em que o PL500 e o
Cascorez entraram no banco, e passaram por toda régua desta ilha sem que nenhuma as visse, porque todas
mediam concordância entre a matriz e a tela — e as duas concordavam, dizendo a mesma coisa errada.

**Por que não saiu nesta execução:** é bloco, pelo mesmo molde construído duas vezes hoje — balde próprio,
frase própria citando o literal de `ambientes_declarados`, matriz da F2 reescrita nas células afetadas e
bateria —, e sai inteiro numa execução só. Está nomeado na fila do `PROMPT.md` como o próximo, e a célula
`cimento_concreto` × `contato_permanente_agua` do esquema já carrega a frase que o aponta.

## A VARREDURA DAS IRMÃS DEPOIS DO DESEMBARQUE, E ELA ACHOU DUAS MUTAÇÕES INERTES

**A `mutacoes-f2.py` fechou VERMELHA na primeira passada, e não por defeito do código: por DUAS mutações
INERTES**, as duas apontando para linhas que este bloco mudou.

- `silencio do fabricante vira 'pode'` — a condição da regra 2 ganhou a segunda metade
  (`&& ! isset( $p['bases_indicadas_so_em'][ $base ] )`), pela REGRA 8, e a âncora velha deixou de existir.
- `a saida 'troque o caquinho' volta a ser digitada` — a linha alvo passou a ler
  `cdm_f2_proibe_grupos_de_peca( $m )` em vez de `$grupos`, que é exatamente o conserto do defeito que
  este bloco achou no ar.

**É o corolário que a seção 8 escreve e que a execução de 17h45Z já tinha pago na `mutacoes-f1`:
mutação que não morde é teste verde com outro nome.** As duas foram reapontadas com o motivo escrito ao
lado, e a primeira teve o alvo ampliado para a condição INTEIRA de propósito — trocar só a primeira
metade deixaria a regra 2 de pé pela segunda, e a mutação mediria meia regra. O `if ( false )` não toca a
regra 8, que fica acima daquela linha e tem mutação própria em `ferramentas/mutacoes-par.py`.

**A bancada DESTE bloco, toda verde e toda rodada:** `validar-banco` (45 celulas da F2, 9 do rejunte, 54
pares da regra 6, 18 da regra 7, **1 par qualificado e 5 ancoras da regra 8**), `teste-f2` de 145 para
**149** afirmacoes, `mutacoes-par` **17 de 17** de forma com 13 so pelo portao novo + **5 de 5** de tela +
**4 de 4** falsos positivos, e `mutacoes-f2` **71 de 71** depois da reapontada. As oito bancadas PHP
irmas reconferidas e verdes: casca 744, guia 110, tecnicas 139, loja 208, leads 211, f1 228,
prestacao-rejunte 5 sobre 540+180 estados, atelie APROVADO.

**E A TECNICAS CAIU DE 140 PARA 139 AFIRMACOES, o que parece perda de cobertura e nao e — medido, nao
suposto.** Rodei a bancada no `HEAD` anterior, num worktree, para comparar linha a linha: a afirmacao que
desapareceu e `a recusa de quartzolit-cimentcola-externo-acii nomeia TODAS as causas que o calculo
separou`, na pagina do **Picassiete**. Ela e por produto RECUSADO, e a argamassa deixou de ser recusada
ali: a pagina passou de 5 para **6 cartoes** de cola e de 9 para **11** links que rendem comissao. Na
pagina do Trencadis ela continua recusada e a afirmacao continua, agora nomeando DUAS causas em vez de
uma (`silencio 36, peca 5`). **A entrega alcancou duas paginas que nao eram o alvo do bloco.**

**AS 24 BATERIAS DE MUTACAO RESTANTES NAO FORAM RODADAS NESTA EXECUCAO, e ficam nomeadas em vez de
resumidas:** cobertura, tecnica-x-material, tecnicas, tecnicas-pagina, guia, pastilhas, apoio, base,
rejunte, acabamento, degrau, forma-do-degrau, motivo-degrau-4, batismo, casamento, f1, arvore,
voz-e-cabeca, promessa-do-titulo, divulgacao, prestacao, loja, leads, atelie e ga4. Elas somam ~380
mutacoes e varias rodam bancada que renderiza uma pagina por estado; a varredura inteira e coisa de horas.
**Escrever `CATORZE DE CATORZE` aqui sem as ter rodado seria a afirmacao em bloco com escopo maior do que
o medido — o defeito que esta ilha paga mais vezes.** O que elas cobrem e regressao de blocos ANTERIORES;
a regra que este bloco mexeu (a 2, a 7 e a ordem entre elas) esta coberta pela `mutacoes-f2`, que rodou e
fechou 71 de 71.

## O PRÓXIMO BLOCO, E ELE É UM DEFEITO QUE ESTE BLOCO ACHOU NO AR, NÃO UMA IDEIA

**A REGRA 3 MANDA PARA O BALDE DO SILÊNCIO QUEM O FABRICANTE DECLARA, E A PÁGINA DIZ QUE ELE NÃO FALA.**
A frase que a seção do silêncio serve é *"O fabricante simplesmente não fala desta superfície, e silêncio
não vira 'pode'"* — e ela sai, hoje, sobre produtos cujos fabricantes **falam da superfície** e apenas
delimitaram o AMBIENTE do produto inteiro. É exatamente o defeito que a REGRA 8 acabou de consertar um
andar acima, com a diferença de que ali o qualificador estava colado no substrato e aqui ele é campo do
produto.

É o mesmo molde já construído duas vezes hoje: um balde próprio
(`eliminados_por_ambiente_do_produto`), uma frase própria citando o literal do `ambientes_declarados`, a
matriz da F2 reescrita nas células afetadas, e bateria. **A diferença de tamanho é que ele mexe em mais
células que a regra 8**, porque a regra 3 já estava em uso desde o bloco 3 — o PL500 e o Cascorez
delimitam ambiente desde 10/09.

**E uma coisa que NÃO é bloco e continua destravando quatro registros de uma vez:** `*.quartzolit.weber`
na lista de rede (`dados/despachos.md`, ABERTOS), com a ressalva de que o `www.` já responde **403** —
403 é decisão do fabricante, não da rede do Raphael.

**O que o `gesso acartonado (drywall)` espera continua sendo decisão do Raphael**, e é a ÚNICA das quatro
ocorrências da lacuna de vocabulário que este bloco não fechou: `vocabularios.base` não tem valor para
gesso, e mexer na lista suspensa da F2 mexe em página com impressão.

---

06/10/2026 16h19Z — A SOBRA QUE O VENDEDOR PEDE ESTAVA GRAVADA HÁ SEIS DIAS E NENHUMA TELA A LIA; O ACHADO NÃO FOI O CAMPO, FOI O NOME DELE — E DUAS FRASES DO REPOSITÓRIO SOBRE ESTA ILHA ERAM FALSAS

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **16h19Z**, push da reserva aceito na primeira
tentativa (`c6683f3`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta; o último commit na pasta era de **14h45Z**, 94
minutos antes, e era o fecho da execução anterior. Nenhum PR aberto, nenhuma branch `claude/*` à frente
do `main`. **Rede pela 20.2:** `https://clubedomosaico.com.br/` em **200**.

**Nenhum despacho aberto para a Fundação** — o de 05/10 tem os itens 1 e 2 fechados e o 3 declara no
próprio texto que é método endereçado ao Raphael; o de 30/09 tem o 1 cumprido e o 2 é do Raphael (soft
404 da borda); o de 28/09 e o do Raphael de 24/09 estão fechados inteiros. Valeu a fila, e a fila
trazia **o próximo bloco escolhido por escrito pela execução de 14h10Z: o candidato (a),
`propriedades.sobra_declarada_pct` na F1, a partir dos 10% da AF1500**.

## A PRIMEIRA COISA QUE ESTE BLOCO FEZ FOI DESCOBRIR QUE O CAMPO QUE ELE IA CRIAR JÁ EXISTIA

O item 10 do `bloco_atual` e o item (a) da fila diziam que `propriedades.sobra_declarada_pct` seria
**campo novo**, lido por ferramenta de cálculo, e que o número "não foi gravado como propriedade nesta
execução de propósito". Os mesmos dizeres estavam em **dois campos de prosa do próprio registro** da
AF1500 (`preparo.o_que_a_parafrase_perdia` e
`fontes.pagina-produto-af1500.o_que_a_abertura_de_06_10_mudou.a_linha_QUE_A_PARAFRASE_TINHA_APAGADO`).

**Medido antes de escrever uma linha de código:** `propriedades.sobra_recomendada_pct` existe no
`pastilhart-af1500` desde **30/09/2026**, commit **`66f99ef`**, com `valor: 10`, `unidade: "%"`,
`fonte_id` e `declarado_como`. É o mesmo número, com outro nome.

**O que o bloco teria feito se obedecesse ao que estava escrito:** gravado a MESMA declaração **duas
vezes**, uma das duas vazia — porque quem cria campo para um número que já tem não traz o número, traz
a chave. E a tela que lesse a chave vazia publicaria **ausência sobre um dado que o banco tem**. Duas
chaves para a mesma declaração são duas listas do mesmo vocabulário: envelhecem separadas. Por isso o
primeiro entregável deste bloco não é tela, é **nome**: `regras_do_campo_sobra_declarada` no esquema
v13 escreve que o nome é UM, e o validador **reprova** `sobra_declarada_pct`, `sobra_pct` e
`sobra_sugerida_pct` como chave de propriedade.

## A SEGUNDA FRASE FALSA ERA A PREMISSA DO BLOCO: ESTA FERRAMENTA NÃO SUGERE 15%, SUGERE 10%

O `PROMPT.md`, o `ESTADO.md` e o próprio registro repetiam, em três lugares, que *"a F1 pergunta a
sobra ao visitante sugerindo 15%"* — e a premissa inteira do bloco vinha daí: um número nosso
divergindo do dele, "um número que não é de ninguém".

**Medido no `selected` do seletor servido:** `<option value="10" selected>10% de sobra (o comum)`. O
padrão é **10%**, igual ao que o distribuidor pede, e o rótulo da opção já dizia "o comum". O 15 era o
**parâmetro de teste da ronda de 05/10** (`&sobra=15` na URL do exemplo dela), lido como padrão por
quem leu o relatório dela. Três lugares do repositório copiaram a leitura errada do número de outro.

**O bloco continua valendo e muda de forma, e a forma nova é mais difícil:** não há divergência a
resolver, há **coincidência a explicar**. Dois números iguais parecem um número só, e o leitor que vê
"10% (o comum)" não tem como saber se aquilo é declaração de alguém ou escolha nossa. A tela passa a
dizer que são dois: o nosso 10% é pelo **lote de cor** que muda entre duas compras, o dele é por
**corte e ajuste na aplicação**.

## O QUE FOI AO AR

Esquema **v13** (`regras_do_campo_sobra_declarada`, com `quem_pode_declarar` em três classes), **F1
1.6.0**, e o `render-para-teste.php` corrigido.

1. **O BLOCO DE CONFRONTO**, `cdm-f1-sobra-declarada`, servido no lado de quem declara: cita a linha
   dele **entre aspas e inteira**, nomeia quem a escreveu, oferece **refazer a conta** com o número
   dele (link que preserva o resto do estado), e nunca o toma como padrão.
2. **A ATRIBUIÇÃO É A METADE QUE MAIS IMPORTA, e é a 26.3 com um número dentro.** Quem pede os 10% é a
   **Pastilhart, que importa e distribui a marca** — não quem fabrica a pastilha. A palavra sai do
   campo `declarada_por` do banco, nunca do código; o campo `fabricante` daquele registro traz
   *"(importadora e distribuidora, não fabricante)"* dentro da prosa, e deduzir a atribuição dali seria
   a heurística por vizinhança que a seção 8 proíbe. A fonte é **nível 5**, acima do teto **3** da
   escada: menção **com a ressalva escrita**, nunca recomendação.
3. **A COLUNA `Sobra que ele pede`** na tabela dos treze produtos, com a ausência visível em doze —
   porque tabela que só mostrasse quem declara faria o leitor ler o silêncio como "não precisa".
4. **A RESPOSTA DO FAQ** sobre sobra deixou de ser texto fixo e passa a nomear quem declarou e a
   explicar a coincidência. É a frase que um modelo de linguagem cita sozinho (seção 5), então a
   procedência vai **dentro** dela.
5. **O ESTADO DEGRADADO TAMBÉM FOI DECIDIDO:** sem a F2 no ar não há escada, e a classificação passa a
   devolver `teto_de_fonte: null`. O bloco **continua saindo** — citar a linha dele e dizer quem a
   escreveu não depende de escada nenhuma — e diz, na tela, que hoje a página não afirma se a fonte
   sustenta recomendação. Uma régua para as duas telas, nunca uma segunda escrita no lugar.

## UM DEFEITO QUE O BLOCO ACHOU NA CAMADA DE PROVA DESTA MESMA PÁGINA, E ELE É O GÊMEO DO DE ONTEM

A camada "Como sabemos" da F1 publicava *"Nenhum documento de fabricante foi aberto linha a linha
daqui"*. Era verdade quando foi escrita. Em **05/10/2026** o boletim técnico do **Rejunte Piscinas
Quartzolit** foi aberto e lido página a página pelo canal de espelho — e ele está em
`materiais-rejuntes.json`, que é **um dos dois bancos que esta página lê** (é de lá que sai o
coeficiente CR).

**É o mesmo defeito que a F2 pagou no bloco de 14h10Z de hoje, na mesma família e pelo mesmo motivo:**
disclosure velho mente, e nenhuma régua o recontava porque ele era **prosa, não número**. Medido:
**2 de 53** fontes do banco carregam o marcador `tipo_de_origem`. A frase virou conta derivada de
`cdm_casca_numeros()`, servida só pela **via viva**; com o instantâneo a página diz onde a leitura foi
feita e não afirma quantidade nenhuma. A bancada passou a cobrar as duas direções.

## A BANCADA ACHOU TRÊS DEFEITOS NAS MINHAS PRÓPRIAS RÉGUAS, E É POR ISSO QUE ELA EXISTE

A bateria nova (`mutacoes-sobra.py`) reprovou a primeira versão das afirmações **três vezes**, e as
três eram defeitos de régua, não de código:

| o que reprovou | a régua errada | o conserto |
|---|---|---|
| contagem de "não publicada" deu 13 onde o arquivo diz 12 | contava a frase na **tabela inteira**, e a coluna "A caixa" usa a mesma frase para a mesma ausência — a AF1500 é justamente um item sem caixa publicada | o índice da coluna sai do `<th>`, lido na hora, e a contagem é **dentro da coluna** |
| mutação que torna o declarante **fabricante** | a afirmação procurava a palavra `fabricante` no texto — e o nome que a tela usa vem do banco ("a própria fábrica da pastilha", sem a palavra) | cobra a **ausência da ressalva** que não se aplica, não a presença de uma palavra |
| mutação que cria o **segundo** declarante | a régua pegava o primeiro item que não declara e usava o lado DELE, afirmando sobre quatro itens a partir de um; e a consulta de teste cravava `sobra=15`, que é justo o que o segundo declarante pede — o teste cobrou um link na tela em que o link não deve existir | o lado sem declarante é propriedade do **lado**; e a sobra da consulta é derivada do dado, escolhida **depois** de olhar o declarado |

E uma quarta coisa que a bateria **mudou de ideia** sobre si mesma: a primeira versão exigia que toda
mutação de banco deixasse a bancada **vermelha**, e duas passaram verdes — trocar 10% por 20% e baixar
a fonte para nível 3. Não eram buracos: eram as afirmações **derivadas** seguindo o mundo. Exigir
vermelho ali seria exigir que a régua reprovasse a **melhora**, que é a cicatriz da régua amarrada a um
degrau. **Mundo que muda não é defeito.** A cobrança certa, e é a dobradiça deste bloco inteiro, é
outra: a **página servida** tem de mudar quando o banco muda, e a bancada tem de continuar verde. Tela
que repete texto fixo parecido com o dado fica **idêntica** — e foi exatamente esse o estado de 30/09 a
06/10.

Também caiu, no `teste-f1.php`, a afirmação "o banco tem UM declarante de sobra hoje": isso é tabela de
estado esperado **digitada**, e envelheceria calada no dia em que o segundo vendedor publicasse sobra.
No lugar ficou a afirmação de **acordo** — o número que a página publica contra o número contado do
arquivo, os dois lados derivados.

## A BANCADA DE BANCADA: O RENDER DE TESTE SERVIA MENOS QUE O SITE, EM UMA LINHA

`add_query_arg($a)` da bancada devolvia `'/'` **sempre**, ignorando os parâmetros. Bastou enquanto o
único chamador era o `action` do formulário, que não passa nada. O link de refazer a conta chegaria à
bancada como `/#resposta`: um link que no ar leva a outro estado e aqui não leva a nenhum, com o teste
dando verde. Corrigido para o que o WordPress faz — a URL atual com os parâmetros por cima.

## OS NÚMEROS

| bateria | antes | agora |
|---|---|---|
| `teste-f1.php` | 210 afirmações | **228** |
| `mutacoes-sobra.py` | — | **13 de forma** (13 só pelo portão novo) + **5 de tela** + 3 falsos positivos em 0 |
| `validar-banco.py` | OK | **OK**, com a linha nova: 1 registro com sobra em forma de ir à tela, declarada por `distribuidor` |

**AS BATERIAS DE MUTAÇÃO IRMÃS, reconferidas depois do desembarque — e a reapontada é a que importa:**
`mutacoes-f1` **47 de 47 reprovadas, 0 passaram, nenhuma inerte** (na primeira passada, antes do reapontamento,
ela **abortou** na mutação inerte); `mutacoes-pastilhas` **14 de 14** (é o banco que este bloco editou);
`mutacoes-preparo` **16 de 16**, 12 só pelo portão novo, com os 3 estados legítimos passando (é o esquema que
este bloco editou). **E as dez restantes fecharam também, todas verdes:** f2 **71 de 71**, apoio 24, base 20, rejunte 16,
guia 14 decididas certo, acabamento 14, degrau 8 (1 só pelo portão novo), forma-do-degrau 5 (4 só pelo portão
novo, com as 2 formas legítimas de catálogo passando), motivo-degrau-4 10 (10 só pelo portão novo), batismo 16,
voz-e-cabeça 24. **Catorze de catorze.**

## E A ÚLTIMA PASSADA DAS IRMÃS ACHOU UM DEFEITO DA BANCADA QUE NENHUM PORTÃO PODIA VER, PORQUE ELE É DE BYTE

`mutacoes-apoio.py` e `mutacoes-base.py` restauravam os arquivos de verdade **re-serializando** o original
guardado em memória — `json.dump` seguido de `fh.write("\n")` — em vez de devolver os bytes que estavam no
disco. E os dois arquivos que elas tocam, `esquema-banco.json` e `materiais-pastilhas.json`, **não terminavam em
quebra de linha**.

O resultado é a assinatura do defeito que esta ilha mais paga: passada **verde**, conteúdo **idêntico**,
`validar-banco` **OK**, nada vermelho em lugar nenhum — e o repositório sujo com dois arquivos cujo `sha256`
mudou sem uma palavra mudar. **O manifest guarda esse sha e o Sync o compara.** A próxima execução que rodasse
`atualizar-manifest.py` veria dois arquivos "trocados", gravaria shas novos e desembarcaria um no-op; ou, pior,
commitaria um sha que o site depois acusa divergente — que é exatamente o `sha256 divergente` que a execução de
14h10Z de hoje viu e atribuiu, com razão, à borda do CDN.

**Foi medido aqui porque eu ia commitar os dois arquivos assim.** O `git status` acusou, e a conferência mostrou
o que importava: o `HEAD` batia com o manifest e com o que o site aplicou na revisão 62, e o **disco divergia**.
Descartei a mudança de disco em vez de regravar o manifest, porque o lado certo era o que já estava no ar.

**O conserto:** as duas baterias tiram retrato dos **bytes** de todo arquivo do repositório que tocam e devolvem
os bytes; `grava()` fica para o mundo **fabricado**, que nasce e morre na passada. E `restaura_bytes` levanta
exceção quando o retrato não existe — o que fez a primeira versão do conserto **parar na hora**, dizendo o nome
do arquivo que faltava (`materiais-pastilhas.json`, que a `apoio` também muta), em vez de restaurar pela metade
e me deixar achar que tinha consertado. Conferido rodando as duas de novo: **24 e 20 verdes, e a árvore limpa
depois**.

**E de carona, o `atualizar-manifest.py` pegou um descuido meu desta mesma execução:** ao reapontar a
`mutacoes-f1.py` eu deixei no manifest o sha de uma versão que já não existia. É a cicatriz escrita no cabeçalho
daquela ferramenta — *"quem mexesse numa ferramenta de bancada deixava para trás uma etiqueta que dizia o hash
de uma versão que não existe mais"* —, e ela pegou quem a escreveu. Três shas regravados, **sem bumpar a
revisão**: nenhum dos três arquivos é servido, o site segue na 62 e o manifest segue na 62.

**As onze baterias irmãs reconferidas depois do bloco:** f2 145/145, casca 744/744, guia 110/110,
técnicas 140/140, loja 208/208, leads 211/211, prestação-rejunte 5/5 sobre 540 estados da F2 e 180 da
F1, ateliê APROVADO, batismo 62/62, casamento 42/42. `validar-banco` OK.

## O QUE ESTE BLOCO NÃO FEZ

Nenhuma URL nova (segue em **21**), nenhuma página criada, nenhum link de afiliado gerado, nenhum teto
da 21.4 gasto, nenhuma coleta nova. **Nenhum número novo nasceu de propriedade:** os 10% já estavam
gravados — o que nasceu foram os quatro subcampos que faltavam para eles poderem ir à tela com a
atribuição certa.

## O PRÓXIMO BLOCO

**O candidato (b) da fila, e agora ele é o único dos dois que sobrou: o campo de par substrato ×
ambiente.** Está medido em `materiais-colas.json / quartzolit-cimentcola-externo-acii / fontes /
bt-cimentcola-externo-2016-05 / substratos_que_o_documento_declara_e_que_NAO_foram_gravados`. É decisão
de esquema — bloco, não linha — e é ele que destrava a cura de 180 dias da cimentcola AC-II, que segue
gravada e fora da tela: o terceiro bloqueio é **jusante** dele, como a execução de 14h10Z mediu.

**E uma coisa que NÃO é bloco e destrava quatro registros de uma vez:** `*.quartzolit.weber` na lista
de rede (`dados/despachos.md`, ABERTOS), com a ressalva de que o `www.` já responde **403** — 403 é
decisão do fabricante, não da rede do Raphael.

**E uma lição de método para quem vier:** três lugares deste repositório afirmavam 15% sobre uma
ferramenta cujo padrão servido é 10%, e dois afirmavam que um campo não existia estando ele gravado no
`main`. Nenhuma das cinco frases foi medida antes de ser escrita; todas foram copiadas da anterior. É a
mesma família do "disclosure velho mente", um andar acima: **relatório velho também mente, e o custo
dele é um bloco inteiro desenhado sobre a premissa errada.** O que salvou este foi o primeiro comando —
abrir o registro antes de escrever o campo.

---

06/10/2026 14h10Z — NOVE DECLARAÇÕES DE FABRICANTE ESTAVAM GRAVADAS E NENHUMA TELA AS SERVIA; AGORA CINCO ESTÃO NO AR, E AS QUATRO QUE DEU PARA CONFERIR ESTAVAM ERRADAS

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h18Z**, push da reserva aceito na primeira
tentativa (`f9b03dd`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta; o último commit na pasta era de **12h34Z**, 43
minutos antes, e era o fecho da execução anterior. Nenhum PR aberto, nenhuma branch `claude/*` à
frente do `main`. **Rede pela 20.2:** `https://clubedomosaico.com.br/` em **200** nas três passadas.

**Nenhum despacho aberto para a Fundação** — o de 05/10 tem os itens 1 e 2 fechados e o 3 declara no
próprio texto que não é dela; o de 30/09 tem o 1 cumprido e o 2 é do Raphael (soft 404 da borda); o de
28/09 e o do Raphael de 24/09 estão fechados inteiros. Valeu a fila, e a fila trazia **o próximo bloco
escolhido por escrito pela execução de 12h34Z: a F2 e o Guia servirem `preparo`**.

## O BURACO NÃO ERA UM CAMPO ERRADO: ERA UM CAMPO SEM NENHUM PORTÃO E SEM NENHUMA TELA

De 10/09 a 06/10/2026, **nove registros** carregaram `preparo` como **string solta** — sem fonte, sem
forma, fora do esquema (o único `preparo` que o esquema declarava era o `substrato.preparo_declarado`
da categoria `base`, que é outro campo de outra categoria) — e **nenhum dos nove snippets** desta ilha
lia a palavra. Nove declarações de fabricante lidas, gravadas e descartadas em silêncio, que é o
defeito que esta ilha já mediu com quatro outros nomes.

**E o preço tinha endereço escrito no próprio banco.** Em `materiais-colas.json /
quartzolit-cimentcola-externo-acii / fontes / bt-cimentcola-externo-2016-05` estava registrado, com
estas palavras, que a cura de 180 dias não podia ser gravada porque *"o campo `preparo` não resolve:
ele existe neste esquema e a F2 NÃO o serve em lugar nenhum"*. Um terço do substrato daquela argamassa
estava parado atrás de uma frase que nenhuma tela servia.

## O ACHADO, E ELE NÃO ERA O ESPERADO: 4 DE 4 PARÁFRASES PERDIAM INFORMAÇÃO DO DOCUMENTO

O bloco ia ser "a tela passa a ler o campo". Ao conferir o campo contra os documentos, virou outra
coisa. **Quatro** das nove frases puderam ser conferidas em 06/10 — três páginas de produto por HTTP
(`www.cascola.com.br` e `www.pastilhart.com.br`, 200 nas três passadas) e um boletim em PDF pelo canal
de espelho. **As quatro perderam informação da fonte, cada uma de um jeito:**

| registro | o que a paráfrase fez |
|---|---|
| `cascola-cascorez-extra` | **FECHOU** uma lista que o fabricante deixou aberta: *"passadeiras automáticas ou manualmente, utilizando pincel, rolo, etc."* virou *"Aplicação com pincel ou rolo"* |
| `pastilhart-af1500` | apagou o **motivo** da desempenadeira de borracha (*"para evitar riscos"*) e **uma linha inteira com número**: *"Compre 10% a mais para cortes e ajustes"* |
| `cascola-pl500-adesivo-de-montagem` | apagou a condição de superfície porosa — que o fabricante escreve **dentro** do preparo — e o motivo dela (*"já que o produto seca por evaporação da água"*) |
| `quartzolit-rejunte-piscinas` | apagou **sete das oito** frases da seção 3.1, entre elas uma que o registro **irmão** (`quartzolit-rejunte-ceramicas`) carrega inteira |

**Quatro de quatro.** Uma paráfrase servida entre aspas seria a instrução dele menos a parte que a
gente deixou cair, com o nome dele embaixo — a **26.3** ao contrário. Por isso a paráfrase **não sobe**,
e isso foi medido e não escolhido.

## O QUE FOI ENTREGUE

- **Esquema v12**, `regras_do_campo_preparo`: o campo é **objeto** com **três estados** —
  DECLARADO (`literal_do_fabricante` + `fonte_id` + `lido_em` + `recorte_do_documento` +
  `como_a_tela_chama_o_documento`), SÓ NOSSA LEITURA (`nossa_leitura` + `motivo_sem_literal` na forma
  `CAUSA (<classe>)`) e NADA. A tela serve **só** o primeiro. A lista de categorias que exigem o campo
  (`cola`, `rejunte`) mora **no esquema**, pela **26.2**.
- **Banco:** 13 registros migrados. **CINCO ganharam literal lido HOJE** — Cascorez, PL500, AF1500, o
  boletim do rejunte piscinas e o da cimentcola externo. **OITO ficaram sem**, com a causa
  classificada: `host-recusa` (4) para Tekbond e Quartzolit, em **403 nas três passadas**, e
  `nao-coletado` (4). **DUAS das sem-literal ganharam `fonte_id` DERIVADO** — o texto gravado é, palavra
  por palavra, o campo `preparo` de uma constante de `dados/constantes.json`, cujo `fonte_url` casa com
  uma fonte do registro. Derivação, não palpite: nelas falta o 403 cair, não descobrir a procedência.
- **A dívida que o banco tinha escrito NÃO foi paga, e eu escrevi que tinha sido antes de medir.** A
  cura de 180 dias da cimentcola AC-II está **gravada** e **não está na tela**. Varredura dos 45
  estados de cola, um render por estado: **zero** servem a frase. O produto é **eliminado por
  silêncio** nas 45 células, porque `indicado_para` não nomeia nenhuma base do vocabulário — e não
  nomeia porque **o substrato não foi gravado**. O bloco de preparo só alcança quem a página
  **recomenda**, e instrução sem indicação seria receita de usar o que a gente acabou de dizer que
  não serve. **A F2 servir `preparo` era necessário e não suficiente: o terceiro bloqueio é JUSANTE
  do segundo, não irmão dele.** A frase de 05/10 (*"ou a F2 passa a servir `preparo` na resposta, e a
  cura vira texto na tela"*) acertou o mecanismo e errou a ordem — e esta execução **repetiu a
  própria lição que o registro de 05/10 deixou escrita**: acreditou na promessa do campo em vez de
  varrer os 45 estados. Medido e corrigido no mesmo commit, com afirmação nova em `teste-f2.php` que
  fixa o estado nos **dois** sentidos (hoje cobra zero; no dia em que o substrato entrar ela cai, e o
  comentário diz que a queda é a entrega).
- **F2 1.9.0:** `cdm_f2_preparo()` (os três estados) e `cdm_f2_preparo_html()` / `cdm_f2_preparo_provas()`,
  nas **duas** respostas — a da cola e a do rejunte. Quem **não** tem a instrução aparece **pelo nome**,
  com a causa: lista que só mostra quem passou faz o leitor ler ausência como *"não precisa de preparo"*.
- **Guia 1.1.0:** a ficha do produto serve o preparo logo abaixo da frase de onde o produto vai. Hoje é
  **código dormente** — nenhum dos dez itens de `acabamento` tem o campo — e por isso a bancada o mede
  num **mundo fabricado**.
- **Casca 1.20.0:** `cdm_casca_numeros()` passa a contar os documentos do banco e quantos foram abertos
  página a página (**2 de 53**).
- **Bancadas, todas rodadas e verdes:** `ferramentas/mutacoes-preparo.py` (**16 de 16 reprovadas, 12
  só pelo portão novo, 0 falso positivo**); `teste-f2.php` 136 → **145** afirmações, `teste-guia.php`
  106 → **110**, `teste-casca.php` 741 → **744**, mais `teste-f1` (210), `teste-tecnicas` (140) e
  `teste-prestacao-rejunte` (540 estados da F2 e 180 da F1). As **onze** baterias irmãs reconferidas
  depois do bloco: f2 71/71, voz-e-cabeça 24/24, apoio 24/24, base 20/20, rejunte 16/16, batismo
  16/16, guia 14/14 decididas certo, acabamento 14/14, pastilhas 14/14, motivo-degrau-4 10/10, degrau
  8/8 e forma-do-degrau 5/5 com os dois catálogos legítimos passando.
- **E no ar, depois do Sync:** `conferir-no-ar.py` **APROVADO, 524 afirmações medidas no HTML servido,
  0 falha**, e `leitura-do-visitante.py` com as 21 URLs chegando inteiras a quem não quebra o cache. O
  único vermelho dele é o **soft 404 da borda**, que é do Raphael desde 29/09 e está medido como
  registro, não como portão (origem 404; borda 1ª 404 e 2ª 200, `x-proxy-cache HIT`, `max-age=7200`).
- **Duas baterias irmãs precisaram de remendo, e as duas QUEBRARAM em vez de passar verde** quando o
  campo mudou de forma — que é o comportamento certo de uma mutação que aponta para um caminho. A
  `mutacoes-apoio` 16 e 17; a 17 ainda trocou de alvo com o motivo escrito, porque no durepoxi ela
  passaria a medir o portão do **preparo** em vez do portão do **apoio**.
- **E a `mut-voz` devolveu o `esquema-banco.json` com uma quebra de linha final que o commit não
  tinha.** Conteúdo idêntico, conferido por comparação de JSON — e sha256 diferente, o que deixaria o
  manifest vencido sem uma linha de conteúdo ter mudado. A forma em bytes foi restaurada.

## TRÊS COISAS QUE O BLOCO ACHOU NO CAMINHO, E NENHUMA ERA SOBRE PREPARO

**(1) A camada de prova da F2 publicava um disclosure que havia virado mentira.** A frase dizia
*"Nenhum PDF de fabricante foi aberto linha a linha: a leitura foi feita no domínio de cada um, em 10 e
11/09/2026"*. Era verdade quando foi escrita. Em **05 e 06/10** dois boletins foram abertos e lidos
página a página — e é de um deles que sai a instrução de preparo que esta página agora serve. A frase
envelheceu calada, na única camada da página cujo produto inteiro é o rigor, e **nenhuma régua a
recontava porque ela era prosa, não número**. Virou conta, derivada do banco, servida só pela via viva
(`numeros_vivos`); com o instantâneo a página diz **onde** a leitura foi feita e não afirma quantidade.
Mesma família dos 28 botões da casca 1.18.0.

**(2) A trava dos blocos de prova do `teste-casca.php` media o acaso do dia em que foi escrita.** Ela
cobrava **no máximo DOIS** `cdm-prova` por página, e o 2 era o retrato de uma página com duas camadas.
Com a resposta do rejunte ganhando prova própria — que a **15.2** pede: a prova desce um parágrafo,
dentro da mesma caixa — a página passou a ter **três legítimas** e a trava reprovou. O que ela queria
impedir, nas palavras dela, é *"embrulhar a página inteira na marca"*, e isso não é quantidade: é
**seção**. A régua passou a ser estrutural — **entre dois blocos de prova tem de existir uma abertura de
seção** — com o teto de tamanho de 50% intacto e um teto absoluto de 5. Conferido que ela morde: duas
provas na mesma seção reprovam.

**(3) A prestação de contas do rejunte pegou o bloco novo em 1.017 erros.** A regra do despacho da
Sentinela de 12/09 é que **todo rejunte do banco é nomeado exatamente UMA VEZ** na resposta, e
`teste-prestacao-rejunte.php` recomputa isso nos 540 estados. O bloco de preparo nasceu **dentro** da
seção e nomeou os produtos uma segunda vez. Instrução de aplicação não é prestação de contas: o bloco
virou **seção irmã**, fora da fronteira que a bancada lê. **Portão de outra regra achando o defeito do
bloco novo é a bancada pagando por si mesma.**

E uma quarta, menor e com nome: a **varredura de apoio** reprovou nas duas direções no mesmo instante,
porque `preparo` virou objeto e a frase do fabricante mudou de caminho. Com ela nasceu
`subcampos_que_NAO_sao_frase_do_fabricante` no esquema — a varredura desce no objeto e **não** pode ler
`nossa_leitura`, `motivo_sem_literal`, `recorte_do_documento` nem as notas. A lista é de **caminho
completo**, nunca de prefixo: prefixo genérico apagaria o campo inteiro da varredura, inclusive a
frase dele, que é o defeito oposto e o pior dos dois. E o bloco **cortou uma frase do fabricante por
alguns minutos** — a obs. da desempenadeira saiu do literal da cimentcola como "tabela" e o termo
ficou só em prosa nossa; cegar a varredura no mesmo gesto em que se corta a declaração é a definição do
defeito que a seção existe para impedir. A frase voltou e a ocorrência foi listada.

## O QUE ESTE BLOCO NÃO FEZ, dito porque a tentação é dizer que fez

- **O substrato da cimentcola AC-II continua fora.** A cura virou texto na tela, que era o terceiro
  bloqueio; o segundo — substrato cujo qualificador é de **ambiente** — segue aberto e é decisão de
  esquema.
- **Nenhum número novo nasceu de propriedade.** Os 10% de sobra da AF1500, as 72 h do rejunte piscinas
  e os 15 minutos de repouso estão na **frase dele**, não em `propriedades`. Número de propriedade exige
  fonte por valor e é lido por ferramenta de cálculo — gravá-los é bloco, não linha.
- **Nenhuma URL nova.** A ilha segue em **21**.
- **Nenhum link de afiliado gerado**, nenhum teto da 21.4 gasto.

## O PRÓXIMO BLOCO, e ele tem dois candidatos medidos — o primeiro é o barato

**(a) `propriedades.sobra_declarada_pct` na F1, a partir dos 10% da AF1500.** É a **única** sobra
declarada por fabricante que esta ilha tem lida, e a F1 pergunta a sobra ao visitante **sugerindo 15%**
— um número que não é de ninguém. Hoje a declaração dele está na tela como frase e **não** entra na
conta. Quem fizer: o campo exige fonte por valor (é `propriedades`), a F1 tem de dizer **de quem** é o
número quando usar o declarado, e a bateria tem de medir o estado em que o produto escolhido **não**
declara sobra, que é o de 40 dos 41 registros.

**(b) O campo de par substrato × ambiente, ou uma regra 8 lida como a 7 lê o grupo.** É o segundo
bloqueio do substrato da AC-II, está medido em
`materiais-colas.json / quartzolit-cimentcola-externo-acii / fontes / bt-cimentcola-externo-2016-05 /
substratos_que_o_documento_declara_e_que_NAO_foram_gravados`, e é decisão de esquema — bloco, não linha.

**E uma terceira coisa que NÃO é bloco e destrava quatro registros de uma vez:** `*.quartzolit.weber`
na lista de rede. Quatro das oito paráfrases sem literal são da Quartzolit e duas delas já têm o
documento nomeado. Está em `dados/despachos.md`, nos ABERTOS, e a ressalva nova é que o `www.` já
responde **403** — então o curinga pode entrar e o 403 ficar, porque 403 é decisão do fabricante e não
da rede do Raphael.

---

06/10/2026 12h34Z — A REGRA 7 NASCEU PARA DESTRAVAR UMA ARGAMASSA E O QUE ELA ACHOU FOI UM DEFEITO NO AR, EM OUTRO PRODUTO

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h17Z**, push da reserva aceito na primeira
tentativa (`ef54546`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta; o último commit na pasta era de **05/10 às 20h12Z**,
14 horas antes. Nenhum PR aberto, nenhuma branch `claude/*` à frente do `main`. **Rede pela 20.2:**
`https://clubedomosaico.com.br/` em **200** nas três passadas.

**Nenhum despacho aberto para a Fundação.** O de 05/10 tem os itens 1 e 2 fechados e o 3 declara, no
próprio texto, que não é trabalho da Fundação; o de 30/09 tem o item 1 cumprido e o 2 é do Raphael
(soft 404 da borda); o de 28/09 e o do Raphael de 24/09 estão fechados inteiros. Então valeu a fila, e
a fila trazia **o próximo bloco escolhido por escrito pela execução de 05/10: a REGRA 7**.

## O QUE A REGRA 7 É, E POR QUE ELA PRECISAVA DE BLOCO

A execução de 05/10 abriu o boletim do `cimentcola externo quartzolit` e achou, na seção 4.1, a
declaração de substrato que a pendência `cimentcola-substrato-declarado` esperava desde 10/09. Ela
**não gravou**, e escreveu o motivo: a seção 3 do mesmo boletim proíbe *"revestimentos especiais"* — e
pastilha de vidro é revestimento especial. As cinco regras de elegibilidade decidem sobre **base** e
**ambiente**; a sexta lê a tessela por um campo só (`exige_superficie_porosa`). **Não existia campo
para proibição que fala da PEÇA que se cola.**

Agora existe, e segue o molde da regra 6 inteiro, porque o molde é o que a **26.2** e a **26.3**
pedem: a lista mora no esquema (`grupos_de_tessela_proibidos`), a classificação de quais caquinhos
caem no grupo é **nossa**, e a tela diz as duas coisas em orações separadas. Com uma inversão
deliberada e escrita: **a `regra_da_direcao` é o avesso da de `superficies_porosas`.** Lá a lista
decide quem GANHA recomendação e a dúvida fica fora; aqui ela decide quem PERDE, e a assimetria da
seção 10 inverte com ela — classificar de menos publica recomendação proibida, classificar de mais
custa uma recomendação verdadeira. As duas travas de "a lista sumiu" também são opostas: sem
`superficies_porosas` todo produto com condição é reprovado; sem `grupos_de_tessela_proibidos` todo
produto que declara grupo sai de TODO caquinho. Nos dois casos a direção é a mesma — não recomendar.

## E O QUE ELE ACHOU NÃO TEM NADA A VER COM A ARGAMASSA

**Escrever a lista achou um defeito que estava servido desde 11/09/2026.** O **Tekbond Silicone
Acético Construção** escreve `espelhos` em `nao_usar_em`, e essa frase era lida como **base e só como
base**: na base `espelho` o produto saía proibido, certo. Mas a F2 pergunta o caquinho desde a 1.0.0, e
em **cerâmica + caco de espelho + externo abrigado** a página servia esse silicone no **TOPO** da
recomendação, empatado com o Maxx e com o neutro. O ácido acético da cura ataca a prata e a pintura de
proteção do espelho — e é por isso que a **mesma Tekbond** vende um silicone **neutro** declarando
`espelhos` entre os usos dele. **O banco tinha as duas metades desde 10/09 e nenhuma regra para
juntá-las.**

**A parte que vale mais que a regra:** a **âncora escrita à mão da regra 6**, de 13/09/2026, declarava
`tekbond-silicone-acetico-construcao` no topo de `vidro` + `caco de espelho`. Ou seja: a régua
independente da seção 8 tinha o defeito escrito como **resultado esperado**. Ela fez o que promete —
nunca concordou com o código por cópia — e não podia pegar isto: as duas metades estavam certas sobre a
regra 6 e as duas eram cegas para a mesma frase. **Portão independente mede divergência entre as
metades; nunca a lacuna que as duas têm.** A âncora foi corrigida com esse parágrafo escrito dentro
dela, não apagada.

## O QUE MUDOU NO AR, EM NÚMERO

- A **F2 1.8.0** tira o acético de **6 estados** base × lugar × caquinho (todos com caco de espelho), e
  em cada um deles ele sai num bloco próprio (`cdm-f2-peca-fora`) com a frase do fabricante citada e a
  classificação atribuída a nós.
- O **censo da seção 14.3** mexeu, e é a medida honesta do que estava contado errado:
  `estados_com_o_minimo` da cola vai de **28 para 25** e `estados_descobertos` de **242 para 245**.
  Três estados estavam acima do piso contando um produto que o fabricante proíbe no caquinho.
- A **tabela pré-renderizada** — a metade da página que um modelo de linguagem lê sem preencher
  formulário — passa a dizer, em 4 linhas, com que caquinho a indicação **não** vale, com a frase
  literal do fabricante. Sem isso a linha "cerâmica, no sol e na chuva: use Tekbond Silicone Acético
  Construção" valia para qualquer caquinho.

## O SUBSTRATO DA CIMENTCOLA **NÃO** ENTROU, E ISSO É MEDIÇÃO, NÃO DESÂNIMO

A frase de 05/10 era: *"Fechada ela, o substrato entra e a cimentcola AC-II passa a ser recomendação
primária em duas bases."* **A regra 7 fechou e o substrato continua fora.** Ao ler as três frases da
seção 4.1 que **já estavam gravadas no repositório desde 05/10**, a proibição de peça se revelou **um
de três bloqueios**:

| bloqueio | estado em 06/10 | o que falta |
|---|---|---|
| proibição declarada sobre a PEÇA | **FECHADO** | nada — é a regra 7 |
| o qualificador de **ambiente** vem colado no substrato (`em áreas internas`, `em paredes internas`) e o banco decide ambiente por PRODUTO | aberto | campo de par (substrato + ambiente), ou uma regra 8 lida como a 7 lê o grupo |
| o substrato sem qualificador de ambiente tem qualificador de **CURA** (`paredes de concreto curado há 180 dias`; abaixo disso o próprio boletim manda usar outro produto, nomeado) | aberto | a F2 servir `preparo` na resposta — o campo existe no esquema e **nenhuma linha do snippet o lê** (conferido por varredura em 06/10) |

O segundo e o terceiro são caros justamente nesta ilha: `alvenaria_tijolo` + `externo_abrigado` é um
muro de mosaico ao ar livre, e `cimento_concreto` aqui não é parede de obra — é vaso e tampo que a
artesã acabou de fazer, muito abaixo dos 180 dias. Gravar o substrato sem os dois publicaria
recomendação primária para o caso **mais comum** da ilha exatamente onde o fabricante indica outro
produto. E o custo de não gravar é baixo e conhecido: essa base já é respondida pelo silicone neutro,
que declara concreto e alvenaria com todas as letras.

**Por que a promessa de 05/10 errou:** ela não leu a própria citação. O campo
`substratos_que_o_documento_declara_e_que_NAO_foram_gravados` já tinha, palavra por palavra, as três
frases que mostram os outros dois bloqueios. Isso está escrito dentro do campo, agora, com os dois
bloqueios medidos e com o campo que cada um pede.

## A CLASSIFICAÇÃO É NOSSA, ENTÃO A DÚVIDA FICA ESCRITA

Três grupos nasceram, e cada caquinho do vocabulário tem motivo escrito nos dois lados de cada um:

- **`espelho`** (do acético, `espelhos`) → só `caco_espelho`. Pastilha de vidro fica **fora**, e não por
  tolerância: o que o acético ataca é a prata, e a própria Tekbond indica `vidro não laminado` para
  este produto **na mesma lista** de onde `espelhos` foi proibido.
- **`revestimento_especial`** (da AC-II) → `pastilha_vidro`, `pastilha_ceramica`, `caco_espelho`. A
  pastilha de cerâmica entrou **pela regra da direção**, e a dúvida está escrita: pastilha é formato, e
  o mesmo documento indica `revestimentos cerâmicos de até 60x60 cm`. `caco_azulejo` e `pedra` ficam
  fora porque o **mesmo documento os indica nominalmente** — classificar como especial o que ele indica
  seria inventar proibição.
- **`baixa_absorcao_de_agua`** (da AC-II) → `pastilha_vidro`, `caco_espelho`, `caco_louca`. A louça
  entrou pela direção, com a dúvida nomeada: `louça` cobre de faiança de absorção alta a porcelana
  abaixo de 1%, e quem quebra um prato em casa não sabe qual tem na mão.

**E a tensão com `superficies_porosas` está escrita em vez de escondida:** aquela lista chama
`caco_louca` de **porosa** e esta o põe num grupo de **baixa absorção**. Não é contradição e não se
resolve escolhendo uma. A primeira pergunta se a **face que recebe a cola** absorve água — o pé do
prato e a quebra expõem massa —, porque é dela que depende um adesivo que seca por evaporação. A
segunda pergunta a **classe de absorção do corpo** da peça, que é o que a frase do fabricante de
argamassa mede. Um caquinho pode ser poroso na quebra e vitrificado no corpo, e as duas leituras estão
certas ao mesmo tempo.

## A ASSIMETRIA QUE A REGRA 7 **NÃO** RESOLVEU, E NÃO DEVIA

Dois silicones **acéticos** da mesma Tekbond estão no banco. Só **um** escreve `espelhos` na lista do
que não se deve tocar; o **Maxx** tem `nao_usar_em` vazio. A regra 7 tira só o que declara. Estender a
declaração de um produto para o irmão dele seria inventar declaração — o avesso exato do que a regra 2
proíbe do outro lado do balcão. Então a página continua podendo recomendar o Maxx para caco de
espelho, e isso está **nomeado, não escondido**: o pedido do boletim técnico do Maxx entrou em
`dados/fontes-pedidas.json`. As duas portas da Tekbond respondem **403** desta nuvem (medido hoje, nas
duas URLs do registro do acético).

## UMA MUTAÇÃO PASSOU, E ELA É A SEGUNDA LIÇÃO DO BLOCO

A primeira rodada da bateria fechou **70 de 71**, e a que passou foi *"a recusa da regra 7 some e a
página volta a negar a declaração"*: apagar do snippet o ramo que serve a frase de recusa da regra 7
**não reprovou nada**. O motivo é que **esse ramo não é alcançado hoje** — nas seis células em que a
regra 7 morde, sempre sobra alguém recomendado, então a frase nunca chega à tela. É a mesma família do
`else` que ficou **código morto para o portão** na regra 6 até a matriz escrita à mão ir de 18 para 45
células em 13/09/2026 — e naquela vez o código morto estava **no ar dizendo a frase errada** em quatro
estados.

Duas coisas saíram daí, e nenhuma é "aceitar que não dá para medir":

1. **A asserção foi escrita agora**, cobrando a causa certa no dia em que a célula esvaziar: se a regra
   7 tirar o último sobrevivente, a página tem de dizer *"não dá para indicar cola aqui com esse
   caquinho"* e **não pode** dizer *"nenhum dos adesivos do nosso banco é declarado"*.
2. **A mutação passou a PRODUZIR O MUNDO** em que a asserção morde: dá o grupo `espelho` ao Maxx e ao
   neutro — que é exatamente o mundo que a pendência nomeada do Maxx diz que pode chegar com um
   documento —, e aí a célula esvazia.

E a asserção nova **achou o próprio erro dela** ao ser medida nesse mundo: ela procurava a frase com
minúscula inicial e a página a serve com maiúscula. Duas voltas, e a segunda só existiu porque a
primeira produziu o mundo em vez de confiar na leitura. A mutação também teve de ser corrigida: por um
instante ela escrevia `nao_usar_em: ["espelhos"]` nos dois produtos, e isso tirava o neutro da **base**
`espelho` pela regra 1 — a reprovação passava a vir da **trava vizinha** (a matriz das 45 células), não
do ramo apagado. Mutação reprovada pela trava vizinha é verde que prova que ALGUMA trava existe, nunca
que ESTA existe.

## O PORTÃO VERMELHO QUE ERA ANTERIOR A ESTE BLOCO, E ELE É DA MESMA FAMÍLIA

`mutacoes-tecnicas-pagina.py` não estava na bancada da execução anterior, e ela fechava **13 de 14**
— conferido contra o `main` com `git archive`, para não atribuir a este bloco o que já estava
quebrado. A que passava troca o `rel` da busca crua de `nofollow` para `sponsored`: chamar de
patrocinado um link que **não paga comissão**, que é mentir ao leitor sobre a única coisa que ele tem
o direito de saber sobre nós.

**A causa não era a mutação: era a afirmação passar MEDINDO VAZIO.** A página de técnica não serve
nenhum botão de degrau 4, porque os sete itens de cola do banco têm `url` ou `url_busca`. Então
`0 === $crua_errada` era verdade de graça, e a medida imprimia *"0 links de busca crua"* como
aprovação. É a mesma cicatriz que o `teste-f2.php` já carrega escrita desde 25/09: **caso que o banco
pode deixar de produzir tem de ser PRODUZIDO, não esperado** — e é a mesma do ramo da recusa da regra
7, duas seções acima, no mesmo dia.

O conserto foi o mundo `so_crua=1`, e ele custou duas voltas medidas, as duas escritas no arquivo:
`$_GET['so_crua']` não alcança porque aquele bloco mora dentro do guarda de linha de comando de
`render-para-teste.php` e este teste o inclui por `require`; e produzir o mundo **no próprio
processo** também não alcança, porque o banco que a F2 serve vem de um `static` dentro de
`cdm_f2_banco()` que as oito seções acima já carregaram. **Mundo produzido depois da primeira leitura
não alcança quem já leu.** Com `exec`, como o `teste-f2.php` faz: `teste-tecnicas` vai a **140
afirmações**, mede **5 botões** de busca crua, e a bateria fecha **14 de 14**.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Nenhuma URL nova.** Segue em 21. Nenhuma página criada.
- **Não inventou proibição para o Maxx**, pelo motivo acima.
- **Não gravou o substrato da AC-II**, pelos dois bloqueios medidos.
- **Não criou campo de cura nem de par substrato×ambiente.** Os dois são decisão de esquema e são
  bloco; o barato dos dois (a F2 servir `preparo`) vale para o banco inteiro, não só para este
  registro, e por isso não cabe de carona aqui.

## O PRÓXIMO PASSO, MEDIDO E NÃO ESCOLHIDO DE CABEÇA

**A F2 e o Guia passarem a servir `preparo` na resposta.** Varredura de 06/10 nos nove snippets: a
palavra `preparo` **não aparece em nenhum deles**, e **9 dos 41 registros** do banco têm o campo
preenchido com frase de fabricante — o acético ("limpar com álcool ou acetona; cortar o bico a 45
graus"), o Cascorez, o PL500, a AF1500 e cinco rejuntes da Quartzolit ("deixar em REPOUSO por 15
minutos antes de usar", "juntas de até 3 mm devem ser molhadas com água limpa antes"). **São nove
declarações de fabricante lidas, gravadas e descartadas em silêncio** — o defeito que esta ilha já
mediu quatro vezes com outros nomes. Não é só a cura da cimentcola: vale para o banco inteiro, e é o
que destrava **um terço** do substrato da AC-II. Um dos nove
(`quartzolit-rejunte-porcelanatos-e-ceramicas`) tem `preparo: "Nao coletado nesta execucao."` — isso é
motivo, não texto de fabricante, e a tela não pode servi-lo; separar os dois estados é parte do bloco.

## A MEMÓRIA QUE O `PROMPT.md` MANDA CARREGAR NÃO EXISTE NESTE AMBIENTE

Dito porque a próxima execução vai tentar de novo: os caminhos de `## Memória a carregar`
(`/areas/projeto-clube-do-mosaico.md` e os outros cinco) **não existem** nesta nuvem — não há `/areas`
e não há diretório de memória. Medido em 06/10/2026. O próprio `PROMPT.md` prevê isso com todas as
letras (*"Sem memória, não pare: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta
pasta"*), então o próximo passo desbloqueado foi escrito **no repositório**, nos dois lugares que a
seção 1, passo 7 alcança: o item 10 do `bloco_atual` no `ESTADO.md` e a fila do `PROMPT.md`.

## BANCADA DESTA EXECUÇÃO

validar-banco OK (41 materiais, 45 celulas da F2, 9 do rejunte, 54 pares da regra 6 com 5 ancoras, **18 pares da regra 7 com 5 ancoras e 3 grupos**, 17 de 17 com motivo de degrau 4, 14 casamentos, 7 batismos), validar-pastilhas 189 afirmacoes 0 falha, **teste-f2 136** (era 127: 9 novas da regra 7), teste-f1 210, teste-guia 106, teste-prestacao-rejunte 5 (540 estados da F2 e 180 da F1), **teste-tecnicas 140** (era 137), teste-casca 741, teste-loja 208, teste-atelie APROVADO, teste-leads 211, teste-batismo 62, teste-casamento 42, cobertura --conferir OK, filhas-do-guia --conferir OK (regerado: a unica linha que mudou foi a versao do esquema, 10 para 11), tecnica-x-material --conferir OK, medir-espelho --autoteste 24 de 24, medir-egresso --autoteste 36 de 36. MUTACOES: **mutacoes-f2 71 de 71** (era 51; 20 novas da regra 7), **mutacoes-tecnicas-pagina 14 de 14** (era 13 de 14 no main, e o conserto esta descrito acima), mutacoes-f1 47, mutacoes-rejunte 16, mutacoes-batismo 16, mutacoes-arvore 29, mutacoes-guia 14, mutacoes-pastilhas 14, mutacoes-degrau 8, mutacoes-forma-do-degrau 5, mutacoes-cobertura 14 (identica ao main, 9 delas so pelo portao novo), mutacoes-motivo-degrau-4 10. NO AR, depois do desembarque na revisao 59: conferir-no-ar.py **524 afirmacoes, 0 falha**, e leitura-do-visitante.py REPROVADO com **exatamente 1 defeito, o esperado** — o soft 404 da borda, do hospedeiro, com o Raphael desde 29/09 (22 URLs lidas, 0 em janela de cache, nenhum motivo NOVO de vermelho).

---

05/10/2026 19h5xZ — O ESPELHO NÃO É UM HOST, É UMA FAMÍLIA; E ELE PAGOU A PRIMEIRA DÍVIDA DE `conferir_no_pdf` DESTA ILHA

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **19h17Z**, push da reserva aceito na primeira
tentativa (`2a2c507`). Pela **1.2** não houve escolha a fazer. O cabeçalho estava com
`executando_desde: null`, que pela **1.1** já basta, e o último commit na pasta era de **16h45Z** —
2h32 antes, portanto nem o git tinha o que desempatar. Nenhum PR aberto; a branch `claude/*` desta
sessão estava sincronizada com o `main` e sem commit à frente. **Rede pela 20.2, retestada e não
herdada:** três passadas, `clubedomosaico.com.br` em **200** nas três, com `aquametria.com.br` em 200
nas mesmas três.

**O DESPACHO DE HOJE ESTAVA FECHADO PARA A FUNDAÇÃO** antes de eu começar: os itens 1 e 2 saíram às
16h3xZ e o item 3 se declara método endereçado ao Raphael. Então a execução foi para a fila.

## O BLOCO QUE A FILA MANDAVA, E POR QUE ELE NÃO EXISTE

A fila mandava coletar **2 itens de banco** para `rejunte/acrilico` e **2** para `rejunte/epoxi`, com
a frase de seis horas antes: *"não é mais procura de número — é coleta de SKU"*. **A coleta foi
tentada e o bloqueio tem nome novo: é ÍNDICE DE BUSCA, não egresso.** Medido, não presumido:

| porta | três passadas |
|---|---|
| `*.vteximg.com.br` e `*.vtexassets.com` | **ABERTAS**, 9 de 9 hosts conversaram |
| `www.quartzolit.weber` | **403** — e o repositório o tinha como `connect_rejected` desde 30/09 |
| `portokoll`, `rejuntamix`, `bautech`, `kerakoll`, `mapei`, `votomassa`, `eucatex` | `000`, falha de **DNS** |
| `web.archive.org`, `r.jina.ai`, `docs.google.com` | `000` — as três escapatórias fechadas |
| `www.telhanorte.com.br`, `*.vtexcommercestable.com.br`, `*.myvtex.com` | `000` — **não há como navegar o espelho** |

**E WebFetch não é caminho alternativo:** ele falha no DNS (`getaddrinfo ENOTFOUND`) nos mesmos hosts.
A parede é a mesma para `curl` e para WebFetch, e isso estava não medido.

Quatro consultas diferentes procuraram o boletim do rejunte acrílico e do epóxi nas duas famílias de
CDN. **Zero.** O inventário inteiro do canal são **14 documentos**, e nenhum é dos dois. Então *"o
egresso não abre PDF de fabricante"* e *"eu não sei o nome do arquivo"* são **bloqueios diferentes**, e
quatro blocos desta ilha escreveram os dois com a mesma frase. Está escrito na fila do `PROMPT.md`
para a próxima execução não repetir a coleta.

## O QUE SAIU NO LUGAR, E É O MESMO VEIO

### 1. A EXPLICAÇÃO DO ACHADO DE 13h2xZ ESTAVA ERRADA, E A EXPLICAÇÃO ERRADA ESTREITA A PORTA

O bloco de 13h2xZ descobriu que o boletim da Quartzolit abre pelo CDN da Telha Norte e escreveu, no
esquema, que a razão era a Telha Norte ser *"varejista do próprio grupo Saint-Gobain"*. **Não é.**
`leroymerlin`, `mkpcoral`, `cec`, `balaroti`, `chatuba` e `tumelero` respondem igual no mesmo CDN e
nenhum é do grupo. O que está liberado é o **sufixo**, e são dois. O achado ficou; a explicação caiu —
e ela custava, porque quem acreditasse nela não tentaria o CDN de nenhuma outra loja, e a Coral, que
não é Saint-Gobain, serve boletim pelo mesmo caminho.

Virou ferramenta: **`ferramentas/medir-espelho.py`**, com `--autoteste` (**24 casos, 24 de 24**),
gerando `dados/canal-de-espelho.json` e `.md`. Ela sonda **quatro grupos e não um** — a família, os
hosts de **descoberta**, as **escapatórias** e o **fabricante** —, com três passadas e controle
obrigatório, e dá **dois vereditos por host**, pela lição do `medir-egresso.py`: conversar não é
entregar. O caso vivo é o `www.quartzolit.weber` em 403. **A trava que mais importa é a que lê `400` do
CDN como host RESPONDENDO** — ler 400 como bloqueio é o mesmo erro que ler 000 como bloqueio em 11/09,
e um autoteste guarda isso. E o inventário **se confere lendo o documento**: cada PDF é aberto e a
identidade sai da **página 1**, nunca do nome do arquivo.

### 2. A PRIMEIRA DÍVIDA DE `conferir_no_pdf` FOI PAGA — ERAM 46 FONTES

O boletim do **`cimentcola externo quartzolit`** (revisado em **maio de 2016**) foi aberto e lido
página a página, e com ele:

- **`cimentcola-consumo-e-tempo-em-aberto` saiu de "falta número" para número escrito:** consumo de
  **±3,5 / ±4,5 / ±8 kg/m²** por faixa de área e **tempo em aberto ≥20 min**. Mais os do **AC-III**,
  do boletim do `cimentcola flexível` (±4 / ±4,5 / ±8,5 kg/m², ≥20 min), que ficaram em
  `dados/constantes.json` e **não** no banco, porque **não existe registro de AC-III** — o valor
  `cimentcola_aciii` está no vocabulário e zero itens o usam.
- **O que a pendência pedia e NENHUM dos dois boletins declara:** o *tempo de pega*. Eles declaram
  maturação (*"deixe repousar por 15 minutos"*) e vida útil da mistura (*"use a argamassa em até 2h30
  após a mistura"*), e chamar qualquer das duas de tempo de pega seria inventar a propriedade pedida.
- **`nao_indicado_para` estava VAZIO** e ganhou as três proibições da seção 3.
- **A embalagem ganhou o saco plástico de 5 kg**, que o banco não tinha — e é o único formato deste
  produto que não é formato de obra, o que responde à própria `observacao` do registro.
- **Uma divergência de tamanho, resolvida pelos dois critérios no mesmo sentido:** a página de produto
  (nível 3) diz *"até 120 x 120 cm"* e o boletim (nível 2) diz *"até 60x60 cm"*. Vence o boletim pela
  escada **e** pelo conjunto mais estreito. Fica em `divergencias[]` com a ressalva de que o espelho
  não prova vigência — e com o motivo de o erro barato ser o escolhido.

### 3. A DECISÃO QUE ESTE BLOCO TOMOU E NÃO ESCONDEU

A pendência `cimentcola-substrato-declarado` **mudou de natureza e continua aberta**. O documento a
responde inteira, na seção 4.1, e **nada disso foi gravado, de propósito**: gravar só essa metade faria
a F2 recomendar esta argamassa em `cimento_concreto` e `alvenaria_tijolo` para quem respondeu
**pastilha de vidro** — e o MESMO boletim proíbe *"revestimentos especiais"*, que é o que pastilha de
vidro é. As cinco regras decidem sobre BASE e AMBIENTE; a sexta lê a tessela por **um** campo. **Não
existe campo para proibição que fala da PEÇA que se cola.** A declaração ficou escrita inteira em
`substratos_que_o_documento_declara_e_que_NAO_foram_gravados` — para não repetir o defeito de
*declaração lida e descartada em silêncio*, que esta ilha já mediu em quatro lugares, o `drywall`
deste mesmo boletim sendo o quarto.

### 4. O BATISMO ACUSOU UM CAMPO CERTO PELA SEGUNDA VEZ NO MESMO DIA, E A LINHA DE HOJE O CONSERTOU

Ao entrar sem `tipo_de_origem`, a fonte nova fez a trava do batismo ler `908487.pdf` — código do
varejista — e reprovar `Argamassa Cimentcola Externo AC-II Quartzolit`. **Falso positivo pelo mesmo
mecanismo do rejunte piscinas, oito horas antes.** A linha escrita hoje em
`origens_que_NAO_batizam_e_por_que` resolveu, e **se provou sozinha**: a regra já existia e a segunda
aplicação dela foi a prova que a primeira não teve. O `nome_comercial` **não** foi corrigido, e o
motivo é medido: ele é entrada da regra de casamento, este registro está no degrau 2 com `url_produto`
de catálogo casado pelo nome, e trocar o nome sem reconferir os 14 casamentos é mexer no que paga
comissão para ganhar tipografia. Fica nomeado, com o documento em casa.

## TRÊS PORTAS MEDIDAS DE CARONA

- **`www.pastilhart.com.br` responde 200 nas três passadas**, e o registro de 28/09 dizia que *"não
  entrou nem no apex"*. A página do `pastilhart-af1500` foi **aberta e lida** (167 KB): as **cinco**
  declarações de ambiente e os **três** números de geometria **conferiram, zero divergência**. A coleta
  por busca de 12/09 estava certa — e isso também é resultado: a 20.2 não serve só para achar erro. **O
  nível não subiu e não devia:** nível é natureza da fonte, nunca alcance dela, e confundir as duas
  faria toda fonte subir de nível no dia em que a rede abrisse.
- **O primeiro preço que esta ilha vê numa fonte alcançável** está medido (R$ 49,00 à vista, de R$
  71,89, estoque 30). `dados/cotacoes.json` segue não existindo: criá-lo é decidir formato, validade do
  preço e como a tela mostra preço datado, e a seção 7 é dura nisso. Bloco, não linha.
- **A pista da FISPQ está FECHADA, e a resposta é NÃO.** Os dois arquivos que o bloco de 13h2xZ deixou
  nomeados são a FISPQ do **Osmocolor ST** e a do **Pentox Cupim**, as duas da Montana Química; uma
  terceira, achada hoje, é a do **Piso Sobre Piso Interno Quartzolit**. Nenhuma é a do epóxi.
  `regras_da_categoria_apoio` continua travada onde estava, e ninguém precisa gastar bloco nela de novo.

## DOIS PORTÕES ESTAVAM VERMELHOS NO `main` ANTES DESTE BLOCO, E FORAM CONSERTADOS

Conferido contra o `main` com `git archive`, para não atribuir a mim o que já estava quebrado:
`cobertura.py --conferir` **já reprovava** e `filhas-do-guia.py --conferir` **já reprovava** a linha de
`/materiais/rejuntes/` do `ARVORE.md` (dizia `0 de 4`, a derivação diz `1 de 4` desde 13h2xZ de hoje).
Os dois regerados/corrigidos. **O portão de `filhas-do-guia` compara o documento com a derivação e NÃO
reescreve a tabela** — então linha errada ali fica errada até alguém olhar, e é por isso que ela passou
por duas execuções.

**E o `cobertura.json` velho estava ESCONDENDO UM GANHO, não um erro** — que é a forma de defeito mais
fácil de nunca olhar. Regerado, a categoria `rejunte` vai de **12 para 22** estados com o mínimo (e de
48 para 38 descobertos, e o maior número de elegíveis num estado de 4 para 5). Os 10 estados novos são
consequência direta da faixa de junta do `rejunte piscinas` que o bloco de 13h2xZ fechou: o produto
deixou de ser eliminado por faixa e passou a ser elegível onde o ambiente o autoriza. **O trabalho tinha
sido feito às 13h2xZ e o número que o mostra ficou seis horas fora do repositório.** Portão derivado que
não é regerado no mesmo commit mede o mundo de antes — e aqui ele subavaliava a própria ilha.

## DESEMBARQUE E VERIFICAÇÃO NO AR

**Sync acionado pela própria Fundação, na mesma execução** — a lição de 16h17Z de hoje, com todas as
letras: *"quem fecha bloco publicável aciona o Sync na mesma execução, mesmo quando o bloco só mexeu em
dado"*, porque dado desta ilha É página. **Revisão 58 aplicada às 20h03:20Z, 15 itens aplicados**, e o
`/status` lê **58**, igual à do `manifest.json`.

**No ar, depois do desembarque:** `conferir-no-ar.py` com **524 afirmações e 0 falha**. E
`leitura-do-visitante.py` — o segundo comando, o que lê como o Google lê, sem quebra de cache —
**REPROVADO com exatamente 1 defeito, e é o esperado**: o soft 404 da borda (1ª leitura 404, 2ª 200,
`x-proxy-cache HIT`, `max-age=7200`), que é do hospedeiro, está com o Raphael desde 29/09 e tem dono
escrito. **22 URLs lidas, 0 em janela de cache, e nenhum motivo NOVO de vermelho** — que é a única
coisa que esse portão proíbe.

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` **OK**, com a matriz das 45 células recomputada depois de cada escrita ·
`validar-pastilhas.py` **189 afirmações, 0 falha** · `teste-f2.php` **127** · `teste-f1.php` **210** ·
`teste-prestacao-rejunte.php` **5** (540 estados da F2 e 180 da F1) · `teste-guia.php` **106** ·
`mutacoes-f2.py` **51 de 51** · `mutacoes-f1.py` **47 de 47** · `mutacoes-batismo.py` **16 de 16** (era
14 em 05/10 às 16h3xZ: a bateria cresceu sozinha com a fonte de PDF nova, então ela cobre o caso novo
em vez de ignorá-lo) · `mutacoes-degrau.py` **8** · `mutacoes-forma-do-degrau.py` **5** ·
`mutacoes-pastilhas.py` **14** · `mutacoes-rejunte.py` **16 de 16** · `mutacoes-arvore.py` **29 de 29**
· `medir-espelho.py --autoteste` **24 de 24** · `medir-egresso.py --autoteste` **36 de 36** ·
`cobertura.py --conferir`, `filhas-do-guia.py --conferir` e `cruzamento-14-9.py --conferir` **verdes**
(os dois primeiros estavam vermelhos no `main`).

## O QUE ESTE BLOCO NÃO MUDOU, DITO PORQUE A TENTAÇÃO É DIZER QUE MUDOU

**Nenhum pixel do que o site serve.** A matriz de 45 células da F2 foi recomputada pelo
`validar-banco.py` depois de cada escrita e bate com as declarações; os gates derivados dão
exatamente o mesmo resultado que dão no `main` (`pode_nascer` em 8, `espera_autoridade` em 2, as
mesmas 10 filhas no portão de dado). O que mudou é a **verdade do banco** e a **dívida nomeada** — não
a recomendação.

## O PRÓXIMO PASSO DESBLOQUEADO, E ELE ESTÁ ESCOLHIDO

**A REGRA 7:** proibição declarada sobre a **peça** elimina o produto para as tesselas que a ilha
classifica naquele grupo. Lista no esquema (molde de `superficies_porosas`), classificação **nossa** e
a tela proibida de dizer que o fabricante classificou (**26.3**), nas **duas** implementações
(`validar-banco.py` e o snippet da F2 em PHP), com matriz esperada e bateria. Fechada ela, o substrato
entra e a **cimentcola AC-II passa a ser recomendação primária em duas bases** — o primeiro produto
novo na matriz da F2 desde 13/09. Depois dela, e já com documento em casa, o **SKU de AC-III**.

**O que continua fora do alcance daqui:** o curinga `*.quartzolit.weber` (com a ressalva nova de que o
`www.` já responde 403, então o curinga pode entrar e o 403 ficar — 403 é decisão do fabricante, não da
rede do Raphael), o acesso do `sentinela@` ao Search Console, e a faixa de volume das consultas
abertas. Os três estão na lista dele e nenhum é pré-requisito do passo acima.

**A memória da ilha não foi atualizada porque ela não existe neste ambiente:** `/areas/` não está
montado, conferido nesta execução. O `PROMPT.md` desta ilha já prevê isso, e é nele que o próximo passo
ficou escrito.

05/10/2026 16h17Z — O DESPACHO DE 05/10 SAI PELOS DOIS ITENS DA FUNDAÇÃO, E O PORTÃO DA F2 VOLTA A MORDER

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **16h17Z**, push da reserva aceito na primeira
tentativa (`8fc16e1`). Pela **1.2** não houve escolha a fazer: o foco nomeia esta ilha e a rotação da seção 1
está suspensa. O cabeçalho estava com `executando_desde: null`, o que pela **1.1** já basta — reserva se escreve
ANTES do trabalho, então `null` significa que nenhum bloco da Fundação está vivo, e não houve reserva vencida
para o git desempatar. O último commit na pasta era de **15h08Z**, 69 minutos antes, e era commit de **ronda da
Sentinela**, que pela 1.1 não reserva nada. Nenhum PR aberto; a branch `claude/dreamy-mccarthy-abrxrs` estava no
mesmo commit do `main`. **Rede pela 20.2:** três passadas, raiz em **200** nas três.

**Nenhuma URL nova** (a ilha segue em **21**), **nenhuma leva da 21.4 gasta**. O que esta execução publicou foi
**dado**, não página: manifest **56 → 57** e Sync acionado, com o `/status` conferido na 57.

## O QUE ESTA EXECUÇÃO FEZ: O DESPACHO DA RONDA DE HOJE, PELOS DOIS ITENS QUE SÃO DA FUNDAÇÃO

O despacho das 14h55Z tem três itens. O **3** está escrito, no próprio despacho, como *"não é trabalho da
Fundação e não é defeito do site"* — é o achado de método sobre o teto de 4 a 6 fichas por sessão do anti-robô da
Shopee, e ele é endereçado ao Raphael. Sobraram o **1** e o **2**, e pela **18.2** os dois saíram na mesma
execução.

## ITEM 1 — O DE DINHEIRO: O BANCO SABIA E O SITE NÃO. **CUMPRIDO, E CONFERIDO NO AR**

**O defeito foi medido antes de eu tocar em nada**, com quebra de cache e `Accept-Encoding: identity`, exatamente
onde o despacho disse que estava: em
`/materiais/qual-cola-usar-no-mosaico/?base=ceramica_esmaltada_porcelana&onde=contato_permanente_agua&caco=pastilha_vidro&junta=6`
a página servia *"Não temos rejunte para indicar com 6 mm de junta dentro da água"* — célula **vazia** — e, uma
linha abaixo, *"De Rejunte Piscinas Quartzolit a gente não conseguiu a faixa de junta que o fabricante publica,
então ele não entra em recomendação nenhuma"*. O `main` tinha a faixa desde a manhã: `junta_min_mm: 2` e
`junta_max_mm: 10`, do boletim de agosto de 2017, lidos e gravados pela execução de 13h18Z. **A página estava
fazendo uma afirmação sobre o nosso próprio trabalho, e a afirmação tinha ficado falsa três horas antes.**

**A causa era uma só e o despacho a nomeou certo:** `/status` na revisão **56**, último desembarque **02/10
19h52**. Commit sem Sync não é entrega (seções 4 e 20.2).

**E O ATRASO NÃO ERA SÓ DO REJUNTE — ESTE É O ACHADO DE CARONA, E ELE É MAIOR QUE O ITEM.** Rodando o
`atualizar-manifest.py`, **13 sha estavam vencidos**, e **dez deles são de commits de HOJE**, das duas execuções
anteriores (`0463fc9` e `552a629`): `cruzamento-14-9`, `serp-das-filhas`, `egresso-de-fontes` (os dois arquivos),
`filhas-do-guia` (os dois), `medir-egresso` e `mutacoes-batismo`, além do `esquema-banco` e do
`materiais-rejuntes`. **Não era um dado parado: era a manhã inteira parada.** O `bloco_atual` da execução de
13h18Z diz, com todas as letras, *"nada publicado e NENHUM Sync acionado"* — ela sabia, escreveu, e o conserto
ficou para quem viesse depois. O mesmo conserto fecha os dez.

**Manifest 56 → 57**, `atualizado_em: 2026-10-05`, Sync acionado por `curl` às **16h36Z**: revisão 57, *"15
aplicado(s), 13 aguardando desembarque [forçado]"*.

**NOTA DE PAPEL, PORQUE ELA MUDA O QUE A SENTINELA PODE FAZER:** a ronda de hoje **tentou** acionar o Sync e foi
**recusada por aquele ambiente**, com a classificação de *deploy em produção*; pela **19.4(a)** o conserto virou
despacho. Daqui, no papel de Fundação, o mesmo acionamento passou — é o fecho de bloco que a seção 4 manda fazer.
**O que a ronda escreveu continua valendo como achado:** enquanto o acionamento for recusado ao papel dela, a
**19.1** e a **19.3** são letra morta para a Sentinela em todo defeito que dependa de desembarque, e ela vai
despachar em vez de consertar. Isso é limite de ambiente, não de regra, e está em "Precisa do Raphael" no
`PAINEL.md`.

**OS QUATRO CRITÉRIOS DE PRONTO QUE O ITEM DECLAROU (18.4), medidos um por um no ar, com quebra de cache:**

| critério | medido |
|---|---|
| (a) `/status` com `revisao` > 56 e `ultimo` de 05/10 ou depois | **revisão 57**, `ultimo` 2026-10-05 16:36:21 |
| (b) `junta=6` deixa de dizer "Não temos rejunte para indicar" e **nomeia** o Piscinas | *"o rejunte é Rejunte Piscinas Quartzolit"*, com *"Cobre junta de 2 a 10 mm"* e a declaração de uso submerso citada. **Zero** ocorrência da frase antiga |
| (c) "a gente não conseguiu a faixa de junta" ausente nas três entradas | **0** em `junta=3`, **0** em `junta=5`, **0** em `junta=6` |
| (d) `junta=3` lista o Piscinas ao lado do Epóxi | *"o rejunte é Rejunte Epóxi Quartzolit e Rejunte Piscinas Quartzolit — o fabricante nomeia este lugar nos dois"* |

A célula que estava **vazia** passou a ter recomendado, e a pergunta em que isso mais importa — dentro da água o
tempo todo — passou a nomear justamente o produto que o fabricante fez para ficar dentro da água.

## ITEM 2 — O DEGRAU 2 QUE ERA ANÚNCIO DE VENDEDOR. **CUMPRIDO, E COM PORTÃO NOVO**

**A escolha era da Fundação pela 19.2**, e o despacho pôs as duas opções defensáveis na mesa. **Escolhi descer o
degrau com o motivo escrito**, e não trocar o `url_produto` por uma `/p/MLB...` do Mercado Livre. O motivo é
medido e não de gosto: a **25.4-b.1** manda reescolher o par **inteiro** — `url` e `url_produto` da mesma oferta,
na mesma chamada —, e o **item 3 do mesmo despacho** acabou de medir que o anti-robô da Shopee fecha a sessão em
4 a 6 fichas e que a Sentinela é proibida de resolver CAPTCHA. **Rotular o que o link É está sempre disponível;
casar um catálogo que ninguém conferiu, não** — e inventar procedência é o defeito que esta ilha mais paga.

`quartzolit-rejunte-acrilico`: `degrau` **2 → 3**, com `por_que_este_degrau_da_25_1` escrito. A escada fecha
**1:1 2:4 3:19 4:17** em 41 — **o degrau 2 saiu de 5 para 4**, como o item pediu que fosse dito explicitamente, e
o 3 subiu de 18 para 19.

**ONDE A JUSTIFICATIVA FOI ESCRITA, E POR QUE NÃO FOI NO LUGAR ÓBVIO:** o campo
`por_que_este_degrau_da_25_1` mora **dentro de `casamento`** nos 36 registros que passaram pelo
`casar-anuncio.py`, ao lado da `loja`, do `shop_id` e do `titulo_do_anuncio` que o sustentam. Este registro é um
**dos cinco de 13/09/2026**, escolhidos antes de a regra de casamento existir — e o esquema já diz que a ausência
de `casamento` neles é **história e não defeito**. Escrever um bloco `casamento` só para a justificativa caber
seria **inventar procedência que ninguém mediu**. O campo entrou no nível de `afiliado`, documentado no esquema
com a trava de onde **não** escrevê-lo: em registro que tenha `casamento`, porque duas cópias da mesma frase em
níveis diferentes é a segunda fonte que envelhece calada (seção 4).

**O PORTÃO NOVO, e ele é a TERCEIRA CAMADA DA MESMA FAMÍLIA.** A linhagem, escrita porque ela é o argumento:

- **28/09** — o degrau tem de estar **escrito** (`mutacoes-degrau.py`);
- **30/09** — o degrau 4 tem de dizer **por que** parou ali (`mutacoes-motivo-degrau-4.py`);
- **05/10** — o degrau escrito tem de **descrever a URL que está ao lado dele**.

Os dois primeiros olham o campo. **Nenhum dos três dias olhou se o número gravado corresponde ao link**, e foi
por esse buraco que o registro passou dez dias com `degrau: 2` carregando
`shopee.com.br/product/1462074750/58262414865`. A régua nova é a **forma da URL**, nunca a prosa ao lado dela,
porque forma de URL é objetiva e prosa envelhece calada: degrau 2 exige a `/p/MLB...` do Mercado Livre, reprova
explicitamente o `produto.mercadolivre.com.br/MLB-..._JM` que a **25.1** nomeia com todas as letras, e degrau 3
exige `url_busca`, que a 25.1 escreve dentro do próprio degrau.

**E A METADE SILENCIOSA DO ACHADO, que a forma da URL não pega:** a mesma `shop_id` da Shopee não pode carregar
dois degraus. Ser **loja oficial do fabricante** (degrau 1) ou **vendedor comum** (degrau 3) é propriedade da
**loja**, não do produto — então dois registros da mesma loja em degraus diferentes têm, com certeza, um dos dois
errado. A loja `1462074750` estava **degrau 3** no `quartzolit-borracha-liquida-elastica`, com o nome dela
escrito no campo (*"a loja Edu Tintas Ltda e vendedor comum"*), e **degrau 2** no rejunte acrílico. **O banco
sabia a resposta num registro e dizia outra coisa no outro.** Hoje: **15 lojas da Shopee lidas, 0 com mais de um
degrau**.

**A BATERIA (`mutacoes-forma-do-degrau.py`): 5 de 5 reprovadas, 4 SÓ pelo portão novo.** A quinta
(degrau 3 sem `url_busca`) o portão antigo já pegava, e está escrito assim no relatório dela — mutação pega pelo
portão errado não prova portão nenhum. Duas **produzem o mundo** que o banco não tem: a forma
`-i.<shop>.<item>`, que um portão lendo só `/product/` não veria em metade dos registros, e a loja com dois
degraus, que o conserto de hoje acabou de tirar do banco.

**E ELA MEDE O FALSO POSITIVO, o que é novo entre as irmãs.** Escrevi a régua primeiro exigindo o rótulo do
produto no caminho da URL — e isso **reprovaria catálogo de verdade**, porque a `/p/MLB...` também existe na
forma curta sem rótulo, que é a que o próprio Mercado Livre devolve ao compartilhar. **Portão que reprova o link
certo é desligado pela primeira pessoa com pressa, e aí deixa de medir qualquer coisa.** A bateria passou a
afirmar que as duas formas legítimas **passam**, e as duas passam.

**O QUE ESTE CONSERTO NÃO MUDA, dito porque a tentação é dizer que mudou:** **nenhum snippet lê
`afiliado.degrau`** — conferido grepando os oito. A vitrine da F2 desempata por presença de `url`, não por
degrau. Então este item corrige a **verdade do banco** e a contagem que mede durabilidade, e **não um pixel do
que o site serve**. O ganho é o que a 25.1 existe para dar: a leitura semanal deixa de ler um link perecível como
durável, e a ordenação da 25.2-b deixa de ter um dado errado embaixo.

## A METADE DO ITEM 2 QUE EU **NÃO** FIZ, E O MOTIVO ESTÁ MEDIDO (18.3)

O item 2 pede duas regras no validador. A primeira entrou. A segunda — *"reprovar `etiqueta_ml` não nulo com
`programa` diferente de `mercadolivre`"* — **não entrou, e não é esquecimento.**

**Contei antes de escrever régua: 21 dos 41 registros** do banco têm `etiqueta_ml` preenchida com `programa:
shopee`. Não é um registro desalinhado: são 4 colas, 13 pastilhas e 4 rejuntes. **A regra, como está escrita,
reprovaria 21 — e o próprio critério de pronto do item ("rodado no banco desta ilha, imprimir zero reprovação")
seria inalcançável.**

**E o campo não é defeito, é rótulo pré-atribuído.** A seção 7 diz: *"uma etiqueta por par ilha × ferramenta"* —
`clubedomosaicof1` e `clubedomosaicof2` são as etiquetas das **duas ferramentas desta ilha**, não de um programa.
E o `REGISTRO.md` de 13/09/2026 guarda a decisão: o validador cobrava a forma `clubedomosaico-<codigo>`, que é
uma etiqueta **impossível de criar**, e **23 registros foram corrigidos de propósito** para a forma sem hífen,
nos dois programas. **Zerar o campo num registro só o tornaria o único incoerente dos 21.**

Isto é a **19.2** funcionando como ela promete: *"sintoma não é causa; quem vê o sintoma costuma errar a causa"*.
O despacho acertou o degrau — que era defeito de verdade, e caro — e leu a etiqueta ao lado dele como parte do
mesmo defeito. Era outra coisa. **Não reverti conserto de Sentinela nenhum** (nada havia sido consertado nessa
metade); o que fica escrito, pela **19.6**, é por que a régua pedida não nasceu.

## O PORTÃO DA F2 ESTAVA VERMELHO E BLOQUEAVA A BATERIA INTEIRA — E A CAUSA FOI A LACUNA QUE FECHOU HOJE

**Isto não estava em despacho nenhum: apareceu ao rodar o portão antes de publicar, que é o que a seção 13
manda.** `teste-f2.php` fechava **1 falha em 127 afirmações**, e `mutacoes-f2.py` se recusava a começar — *"a F2
de verdade já está reprovada, conserte antes de mutar"*. **As 51 mutações da F2 estavam paradas**, e nenhuma
ronda veria isso, porque a ronda mede a tela e não a bancada.

**A afirmação que falhava era um canário, e ele morreu de a notícia ser boa.** A régua era: varra o banco, ache o
produto com `junta_min_mm` ou `junta_max_mm` em `null`, e exija que ele **nunca** apareça recomendado nos 60
estados. Ao lado dela, `! empty( $sem_faixa )` — *"o banco tem produto com faixa de junta não obtida, e ele é
medido"* — existia justamente para provar que havia o que varrer. **Quando o boletim do Piscinas foi aberto hoje
e a faixa entrou no banco, o último produto sem faixa desapareceu:** o canário reprovou, e o portão de verdade
virou **vácuo** — zero produto varrido, zero estado medido, e **verde**.

**E a mutação `faixa pela metade vira sem limite` ficou INERTE pelo mesmo motivo** — ela completa as pontas
`null`, e sem ponta `null` no banco não há o que completar. O comentário dentro dela avisa, de uma versão
anterior, que *"mutação que acha o alvo e mesmo assim não muda o que o site serve é verde sem medir nada — a
mesma família do alvo que não existe, e mais difícil de ver"*. **Foi exatamente isso que aconteceu com ela
outra vez, e por um conserto que estava certo.**

**O conserto não foi apagar o canário — foi parar de depender da sorte do banco.** A bancada passa a
**sintetizar** o produto sem faixa, numa cópia do repositório (só `manifest.json`, `snippets/` e `dados/`, que é
tudo o que o `render-para-teste.php` lê da raiz), clonando **o registro mais perigoso que existe** — o único
declarado para pastilha de vidro submersa — com as duas pontas em `null` e outro nome. O molde é escolhido **por
id nomeado** e a bancada **morre com erro** se ele sair do banco: molde escolhido por posição mudaria de produto
sem ninguém ver, e o portão passaria a medir outra coisa calado.

**E ele mede as DUAS direções**, porque sintético que o render engole em silêncio seria o mesmo vácuo com outra
roupa: **(a)** o nome nunca aparece em recomendação em nenhum dos **60** estados, e **(b)** ele **aparece** na
lista do que ficou de fora, com a frase que declara a faixa não obtida — prova de que o render leu o registro em
vez de descartá-lo antes da conta. Hoje: **60 de 60 estados** na direção (b).

**Resultado: `teste-f2.php` 127 afirmações, 0 falhas** — e o portão passou a medir **60 estados** onde media
**zero**. **A mutação inerte voltou a morder:** `faixa de junta pela metade vira sem limite` reprovou, e reprovou
**pela afirmação nova**.

## UM NÚMERO DE BATERIA QUE ENVELHECEU CALADO, E ELE NÃO ERA MEU

Ao escrever o portão novo no esquema, conferi o número da bateria irmã e ele não batia. O esquema dizia
`mutacoes-degrau.py (8 mutacoes, 4 que so o portao novo ve)`. **Medido hoje: 1, não 4.** E medido **com o meu
portão desligado e com a árvore de antes desta execução** (`git stash`), para não me dar por inocente sem provar:
**era 1 antes de eu tocar em nada**. Não é regressão do portão de 05/10 — é o banco que cresceu, e sete das oito
mutações passaram a ser pegas também por portões vizinhos. A linha do esquema foi corrigida **com a medição e com
a data**, em vez de ser reescrita em silêncio. **Número de bateria escrito num arquivo de esquema é número que
envelhece calado**, e este envelheceu.

## PORTÕES DESTA EXECUÇÃO

| portão | resultado |
|---|---|
| `validar-banco.py` | **OK** — 41 itens, escada 1:1 2:4 3:19 4:17, 15 lojas da Shopee lidas, **0** com mais de um degrau |
| `teste-f2.php` | **127 afirmações, 0 falhas** (era 1 falha) |
| `mutacoes-forma-do-degrau.py` (nova) | **5 de 5**, 4 só pelo portão novo, **0 falso positivo** |
| `mutacoes-degrau.py` | 8 de 8 |
| `mutacoes-motivo-degrau-4.py` | 10 de 10, as 10 só pelo portão novo |
| `mutacoes-casamento.py` | 5 de 5 no banco |
| `teste-casamento.py` | 42 afirmações, 0 falhas |
| `validar-pastilhas.py` | 189 afirmações, 0 item com falha |
| `mutacoes-f2.py` | **51 mutações, 51 reprovadas, 0 passaram** (estava BLOQUEADA antes desta execução) |
| `conferir-no-ar.py` | **APROVADO — 524 afirmações no HTML servido, 0 falhas** |
| `leitura-do-visitante.py` | **REPROVADO por 1 defeito, e é o esperado com dono escrito**: 22 URLs lidas, 0 em janela de cache, e o único defeito é o soft 404 na borda (1ª leitura 404, 2ª 200), do hospedeiro, pendente com o Raphael desde 29/09. **Não ficou vermelho por nenhum outro motivo** |
| YAML do `ESTADO.md` (seção 2) | parseia e os **oito** campos presentes |

## O PRÓXIMO PASSO DESBLOQUEADO

O despacho de 05/10 fica no `PROMPT.md` **só com o item 3**, que ele mesmo declara método endereçado ao Raphael —
ou a Open API de Afiliados passa a responder o estado do anúncio, ou a **25.4** ganha a linha que diz quantos
itens por ronda são possíveis e em que ordem. **Enquanto não houver uma das duas, nenhuma ronda deve escrever "N
de N vivos" sobre um banco que não conseguiu varrer** — e isso é o item falando, não eu.

**A ilha fica sem despacho acionável pela Fundação**, então a próxima execução volta à fila normal do `PROMPT.md`.
O que decide se cabe leva de malha é o **teto da 21.4**, e quem abrir o próximo bloco lê o teto antes de escolher.

**E FICA UM AVISO DE PROCESSO, que é a lição desta execução e não é regra nova:** as duas execuções da manhã
fecharam escrevendo "nenhum Sync acionado" e deixaram **dez** sha vencidos para trás. Nenhum portão do
repositório vê isso — o `main` fica verde, o commit parece entrega, e quem paga é a página. **Quem fecha bloco
publicável aciona o Sync na mesma execução**, mesmo quando o bloco "só mexeu em dado": nesta ilha dado É página,
porque as ferramentas leem o banco a cada requisição.

---

05/10/2026 13h18Z — O NÚMERO QUE FALTAVA ESTAVA NUM PDF QUE A ILHA DAVA POR FECHADO; O EGRESSO NUNCA BARROU PDF, BARRA HOST

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h18Z**, push da reserva aceito na primeira
tentativa (`3a34f4e`). Os cinco `ESTADO.md` do `main` estavam com `executando_desde: null` — pela **1.1** isso
já basta, não houve reserva vencida para o git desempatar. Nenhum PR aberto; a branch `claude/dreamy-mccarthy-hbaqap`
estava no mesmo commit do `main`. Pela **18.1**, o topo do `PROMPT.md` antes de escolher bloco: o despacho de
30/09 tem o item 1 cumprido e o item 2 (soft 404 na borda) **aberto e não sendo da Fundação**; o de 23/09 tem a
metade que falta esperando **clique de gente**, não código. Nada da Fundação fura a fila.

**Nenhuma URL nova** (a ilha segue em **21**), **nenhuma leva da 21.4 gasta**, **nada publicado**, **nenhum Sync
acionado** — esta execução não escreveu página. Manifest e `/status` seguem na **revisão 56**.

## A PORTA DE ENTRADA, ANTES DO BLOCO (seções 20.2 e 29.2) — DE PÉ

Ao contrário de três horas antes: `/` **200**, `/wp-sitemap.xml` **200**, `/robots.txt` **200**, `/wp-json/`
**200**, e caminho inexistente em **404**. O reparo do `.htaccess` feito às 10h3xZ continuava segurando.

## O BLOCO: `rejunte/cimenticio` PASSOU OS DOIS PORTÕES

A fila de 10h3xZ deixou a frase mais útil que esta ilha já recebeu de uma execução anterior: *"a filha
`rejunte/cimenticio` está a UM número de passar — `liberacao_area_molhada_h`, que é declaração de fabricante"*.
Era exatamente isso. Dos 3 itens do recorte, dois já declaravam **24 h** com essas palavras; o
`quartzolit-rejunte-piscinas` não declarava nada, e o motivo escrito no campo dizia que a página de produto não
traz o dado.

**Traz o boletim técnico — e ele foi aberto.** `telhanorte.vteximg.com.br/arquivos/1200003.pdf`, *"Boletim
Técnico – rejunte piscinas quartzolit"*, 3 páginas, *"Documento revisado em agosto de 2017"*, lido página a
página. O que ele fechou neste registro:

| campo | era | virou | a frase do fabricante |
|---|---|---|---|
| `junta_min_mm` | `null`, *"NÃO obtida"* | **2** | *"Juntas de assentamento: de 2 a 10 mm."* |
| `junta_max_mm` | `null`, *"NÃO obtida"* | **10** | a mesma |
| `liberacao_area_molhada_h` | ausente | **96** | *"3.5. Liberação: Outros ambientes: 4 dias da execução."* |
| `classificacao_normativa` | ausente | `null` **com ausência medida** | zero ocorrências de NBR, norma ou tipo I/II nas 3 páginas |
| `liberacao_imersao_dias` | 4, nível 3 | 4, **nível 2** | *"Encher com água a piscina: Após 4 dias de execução."* |

**O 96 h é a única leitura desta passada que não é transcrição, e ela está escrita no próprio campo.** A seção
3.5 do boletim tem duas linhas e só duas: encher a piscina (4 dias) e *"outros ambientes"* (4 dias). O
fabricante **não escreve "área molhada" para este produto**. "Outros ambientes" é a liberação de tudo o que não
é encher a piscina, e área molhada é um desses — então 4 dias são 96 h por aritmética, não por escolha. Ficou
registrado com `leitura` e `por_que_isto_nao_e_esticar_a_frase`, porque este mesmo registro já barrou duas
leituras parecidas (*"gravar 3 mm como máximo INVERTERIA a frase"*, *"virar pode usar em peça de água seria
ESTICAR a frase"*) e a diferença importa: ali o registro faria o fabricante dizer o que ele não disse; aqui se
lê uma frase GERAL no caso particular que ela declaradamente cobre, e o número que sai é o **mais conservador
dos três do recorte** — os irmãos liberam em 24 h e este em 96 h. Quem publicar a comparação cita a frase de
cada um, nunca só o número: dois são "área molhada" do fabricante e o terceiro é "outros ambientes" lido como tal.

**Resultado nos portões:** `ferramentas/filhas-do-guia.py` e `ferramentas/cruzamento-14-9.py` (autoteste 32 de
32, `--conferir` aprovado) levam `rejunte/cimenticio` de `espera_dado` a **`pode_nascer`**, e `dados/cruzamento-14-9.md`
foi regerado pelo portão.

## O QUE A FAIXA DE JUNTA MUDOU NA FERRAMENTA QUE JÁ ESTÁ NO AR — 7 das 9 células da F2

Esta é a metade que não estava prevista. O rejunte piscinas tinha a faixa de junta em `[null, null]` e por isso
a **regra 1** o eliminava de **toda** a grade. Com `[2, 10]`, **sete das nove células** mudaram, e todas pela
mesma causa:

| célula | mudança |
|---|---|
| **3 mm × `contato_permanente_agua`** | o piscinas sobe ao **topo**, ao lado do epóxi |
| **6 mm × `contato_permanente_agua`** | a célula **estava VAZIA** e passa a ter um recomendado |
| 2 mm × `interno_seco` · 10 mm × `externo_abrigado` | entra como elegível abaixo do topo |
| 4 e 5 mm × `interno_molhado` · 2 mm × `externo_exposto` | continua eliminado, mas **por ambiente**, não por junta — outra frase na tela |

**A observação da célula de 3 mm tinha previsto este bloco, com todas as letras:** *"o único produto do banco
cujo fabricante nomeia pastilha de VIDRO debaixo d'água, o rejunte piscinas, é justamente o que não pode ser
recomendado, porque a faixa de junta dele não foi obtida. Ter o dado quase todo não é ter o dado."* As
observações das 7 células foram reescritas à mão, uma a uma — a matriz é escrita à mão de propósito e seria
mentira deixar o texto velho debaixo do número novo. **Nenhuma regra foi tocada: a matriz mudou porque o banco
soube mais.**

## O ACHADO QUE VALE MAIS QUE O BLOCO: O EGRESSO NUNCA BARROU PDF — ELE BARRA HOST

Três blocos seguidos pararam escrevendo alguma forma de *"o egresso não abre PDF de fabricante"*, e o pedido de
rede ao Raphael sempre foi *"liberem o domínio do fabricante"*. **Ninguém tinha medido um host de TERCEIRO.**

| host | medido hoje |
|---|---|
| `telhanorte.vteximg.com.br` | **ABRE** — dois boletins Quartzolit baixados e lidos inteiros |
| `cdn.obramax.com.br` | `EGRESS_BLOCKED` |
| `bd-sp.canaldapeca.com.br` | `EGRESS_BLOCKED` |
| `www.quartzolit.weber` | 403, como em 29/09 e 30/09 |

Está no esquema, em `escada_de_fontes.canal_de_espelho`, **com o que ele não autoriza**: espelho **não vira
nível 1** (do espelho sai o documento, não a garantia de que a revisão lida é a vigente — a de lá é de agosto de
2017), e espelho **não batiza**. O pedido do curinga `*.quartzolit.weber` continua de pé e continua sendo o
caminho do nível 1; ele só deixou de ser a única porta.

**E o segundo boletim só foi aberto para medir o host.** `arquivos/1463217.pdf` é a argamassa colante *super
formatos quartzolit* e **não entrou em banco nenhum** — um arquivo lido não prova um canal, dois no mesmo host
provam que a porta é do host.

## DOIS PORTÕES MORDERAM NO CAMINHO, E OS DOIS ESTAVAM CERTOS

**1. A trava do batismo (26.2) reprovou `Rejunte Piscinas Quartzolit`** dizendo que o fabricante não escreve
`Rejunte` nem `Piscinas` no batismo dele. **A trava estava certa e a premissa dela é que não vale aqui:** o
esquema diz que *"o nome do arquivo de um boletim É o fabricante escrevendo o nome do produto"* — verdade no
servidor do fabricante, falsa no espelho, onde o arquivo se chama `1200003.pdf`, código do varejista. O
fabricante batiza **dentro** do documento, no título da página 1. Falso positivo da pior espécie: acusa o campo
certo e manda a próxima execução estragar um batismo correto. Consertado declarando
`tipo_de_origem: documento-pdf-do-fabricante-em-espelho-de-terceiro` na fonte, **fora** de `origens_que_batizam`,
com o motivo escrito nos dois lugares. **E guardado por duas mutações novas** em `mutacoes-batismo.py`, uma por
ponta — `m11` (o código deixa de ler o `tipo_de_origem` declarado) e `d05` (a origem de espelho entra na lista
das que batizam). A bancada foi de 14 para **16, 16 reprovadas, nenhuma passou**. Sem elas a decisão de hoje
não teria ninguém a medindo.

**2. `medir-egresso.py` sondava a RAIZ do host, nunca a fonte citada** — e por isso ele dizia `telhanorte`
**400** no exato host de onde esta execução baixou dois PDFs. A abertura do próprio arquivo gerado diz: *"a
pergunta que este arquivo responde não é 'o domínio está liberado': é 'a fonte chega'"*. A sonda passou a ser a
**URL que o banco cita**, com a raiz só para os hosts irmãos que nenhum banco cita. É a mesma lição que o
arquivo já ensina um andar acima, um degrau mais fundo: **medir CONNECT não é medir entrega, e medir a RAIZ não
é medir a FONTE.**

**E o conserto da sonda produziu um defeito MEU, achado medindo o próprio conserto e corrigido antes do
commit.** Com a sonda na raiz, um `403` ali ainda podia significar *"o host atende, o arquivo talvez venha"*,
e `entrega()` chamava isso de `alcancavel`. Com a sonda na **fonte citada** isso deixou de valer: a primeira
remedição publicou **`www.quartzolit.weber` como `alcancavel`** — 403 na própria URL de boletim que **19
campos** deste banco citam. Seria escrever no arquivo o **oposto** do que ele existe para medir, e justamente a
frase que quatro execuções pagaram caro para desfazer. A regra passou a olhar o código **quando a sonda é a
fonte**: `>= 400` vira `liberado_mas_sem_entrega` ("o host atende e a fonte não chega"); irmão sondado na raiz
continua medindo o domínio. **Sete casos fabricados novos** guardam exatamente essa fronteira (200, 301, 403,
404, 500 na fonte; 400 e 403 na raiz), e o autoteste foi de **29 para 36**.

**E a sonda certa achou uma fonte que a ilha dava por perdida:** `www.pastilhart.com.br` responde **200** na
URL que o banco de pastilhas cita — ele estava na lista de pedidos ao Raphael, medido pela raiz, e **sai dela**.
`pastilhart.com.br` era um dos dois domínios cuja ausência o bloco das pastilhas registrou.

**E o pedido ao Raphael trocou de conteúdo, o que é a parte que vale.** Ele continua com 21 domínios, mas
**duas linhas saíram e duas entraram**, e as que entraram são justamente as que a ilha mais pede:

| | domínio | por quê |
|---|---|---|
| **saiu** | `vteximg.com.br` | `telhanorte.vteximg.com.br`, o host que o banco cita, **entrega** |
| **saiu** | `pastilhart.com.br` | `www.pastilhart.com.br` responde **200** na URL citada |
| **entrou** | `quartzolit.weber` | 403 **na URL de boletim que 19 campos citam** — nunca chegou, e a régua velha o chamava de alcançável |
| **entrou** | `tekbond.com.br` | mesmo caso |

**A régua antiga mantinha fora do pedido os dois domínios que seguram o nível 1 do banco inteiro**, porque um
403 na raiz contava como "o host responde". O pedido que está com o Raphael desde 29/09 pedia o curinga por
prosa; agora a lista **derivada** o pede também, e pelos dois lados do mesmo domínio.

## PORTÕES DESTA PASSADA

`validar-banco.py` **verde** (41 materiais, 9 células de rejunte, 7 batismos conferidos, zero AVISO) ·
`mutacoes-batismo.py` **16 de 16** · `mutacoes-rejunte.py` **16 de 16** · `mutacoes-casamento.py` **5 de 5** ·
`cruzamento-14-9.py --autoteste` **32 de 32** · `medir-egresso.py --autoteste` **36 de 36** (era 29) ·
`conferir-no-ar.py` **APROVADO, 524 afirmações, 0 falha** — a ilha segue inteira no ar, e o único vermelho é o
soft 404 na borda, que é do Raphael desde 29/09.

## O PRÓXIMO PASSO, E ELE MUDOU DE NATUREZA

A procura de **propriedade** acabou: `espera_dado` zerou no `rejunte`. O que segura a segunda categoria do Guia
é a **16.5**, que cobra 3 filhas, e o `rejunte` tem **1**. `rejunte/acrilico` e `rejunte/epoxi` têm **1 item de
banco cada** e precisam de **2 mais cada uma**, e depois a SERP de cada recorte. **É coleta de SKU**, igual à
que a `acabamento` fez em 25/09 e 02/10 — não é mais procura de número.

**A pista medida e não aberta:** o mesmo host de espelho serve **FISPQ** (`arquivos/101494.pdf`,
`arquivos/90387.pdf`). A FISPQ do epóxi é nomeada em `regras_da_categoria_apoio` como a única coisa que segura o
primeiro SKU de `apoio`, e a `base` para na mesma porta. Não foram abertas e não se sabe de que produto são.

05/10/2026 10h18Z — A PORTA DE ENTRADA CAIU DE NOVO, E O BLOCO PROVOU ERRADA A FRASE QUE O MANDOU

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h18Z** e push da reserva aceito na primeira
tentativa (`1edd3e9`). Os cinco `ESTADO.md` do `main` real estavam com `executando_desde: null`, que pela **1.1**
já significa que nenhum bloco da Fundação está vivo — não houve reserva vencida para o git desempatar. Nenhum PR
aberto; a branch `claude/dreamy-mccarthy-mj47ht` estava no mesmo commit do `main`. Pela **18.1** li o topo do
`PROMPT.md` desta ilha antes de escolher bloco: o despacho de 30/09 tem o item 1 **cumprido** e o item 2 (soft
404 na borda) **aberto e não sendo da Fundação**.

**Nenhuma URL nova** (a ilha segue em **21**), **nenhuma leva da 21.4 gasta**, **nada publicado** e **nenhum
Sync acionado** — esta execução não escreveu página. Manifest e `/status` seguem na **revisão 56**.

## A PORTA DE ENTRADA, ANTES DO BLOCO (seção 20.2) — E ELA ESTAVA NO CHÃO

O `curl` da 20.2 devolveu **200 na raiz nas três passadas**, e **se eu tivesse parado nele teria construído
em cima de uma ilha fora do ar.** O `/status` por caminho bonito devolveu **404** nas mesmas três — e foi esse
desencontro que abriu o resto:

| endereço | código às 10h17Z |
|---|---|
| `/` | **200** |
| `?rest_route=/clubedomosaico/v1/status` | **200** |
| `/wp-json/clubedomosaico/v1/status` | **404** |
| `/wp-json/` · `/wp-sitemap.xml` · `/robots.txt` | **404** · **404** · **404** |
| `/materiais/acabamento/` (e as outras 20 do sitemap) | **404** |

**É a 29.1 escrita como aconteceu:** o Sync é query na raiz, o `/status` é alcançável por `?rest_route=`, a
bancada roda sem rede — **todo portão desta fábrica entra pela porta que continuou aberta**, e a porta que o
Google usa estava fechada. As **três páginas que estão na primeira página do Google** entre elas.

**O diagnóstico por dentro do servidor** (rota da 29.3) deu a assinatura **byte por byte** da queda de 24/09:

| campo | 1ª queda (24/09) | **2ª queda (05/10)** | depois do reparo |
|---|---|---|---|
| bytes | 1.057 | **1.057** | 1.580 |
| blocos `# BEGIN` | só `NFD EPC` | **só `NFD EPC`** | `NFD EPC` + `WordPress` |
| `tem_wordpress` | false | **false** | true |
| linhas de reescrita | 8 | **8** | 15 |

E o que ele **descartou de saída**: `raiz_gravavel: true`, arquivo legível e gravável, `got_mod_rewrite(): true`,
**115 regras de reescrita no banco**. Pela **29.4**, isto separa os dois mundos com número: **não é
`AllowOverride`** — se o arquivo estivesse gravado e correto e as URLs continuassem em 404, aí sim seria o
hospedeiro; aqui o arquivo está gravado e **errado**, e o reparo funciona na hora.

**Reparado** com `&reparar=1` e **conferido no ar pela 19.4(a)**, com quebra de cache: **21 de 21** URLs em
**200**; `/wp-sitemap.xml` em 200 com `application/xml` e XML de sitemap de verdade; `/robots.txt` em 200 e
`text/plain`; `/wp-json/` em 200 e `application/json`; `/nunca-existiu-abc123/` em **404 na página desta ilha**.
`conferir-no-ar.py`: **524 afirmações, 0 falha**. `leitura-do-visitante.py`: **REPROVADO pelo único defeito de
29/09** — o soft 404 na borda, vermelho esperado com dono escrito — e **nenhum defeito novo**.

## A JANELA, QUE É O NÚMERO MAIS CARO DESTA PASSADA: ATÉ 2 DIAS E 14 HORAS

Última prova de vida em **02/10 19h57Z** (fecho do 4c, conferido no ar); queda medida em **05/10 10h17Z**.
Nenhuma ronda rodou na janela: `ultima_ronda` estava em **02/10 14h51Z**. **A decisão do Raphael de 28/09 — que
manda a ronda técnica rodar em TODA ilha no ar, em foco ou fora, e que nasceu exatamente da 1ª queda desta ilha —
não foi executada.** Não há como estreitar a janela daqui: o instrumento que diria quando o Google viu 404 é a
Search Console, e o ambiente **não tem** `GOOGLE_SA_B64` (pendência que já é despacho aberto desde 12/09, não
item novo).

## PELA 19.4(b), ESTE DEFEITO JÁ NÃO É PARA CONSERTAR DAQUI — E QUEM DISSE ISSO FOI A PRÓPRIA ILHA

A entrada de **24/09** em `dados/consertos.md` pré-registrou o desfecho com estas palavras: *"Se o defeito
voltar, a 19.4(b) vale com força dobrada (...) e aí o caminho é chamado na HostGator sobre o `.htaccess` da raiz
de `/clubedomosaico.com.br`, não mais um reparo."* **Voltou, na mesma raiz, com a mesma assinatura.** O chamado
está aberto em `dados/despachos.md` com prioridade **ALTA**, endereçado ao Raphael — a Fundação não abre conta,
não contrata e não fala com fornecedor —, e leva pronto o que dizer, inclusive os quatro campos que descartam
permissão e `AllowOverride` e as **duas datas** a perguntar (24/09 e 02–05/10). **O reparo desta passada foi
feito porque a ilha estava caída AGORA**; ele mantém a ilha no ar e **não substitui o chamado**.

## O ACHADO QUE MATOU UM PORTÃO ANTES DE ALGUÉM O CONSTRUIR

**O `.htaccess` é reescrito a cada requisição.** Três leituras da rota de diagnóstico, espaçadas pelos meus
próprios ~20 segundos, devolveram `mtime` **10:23:49 → 10:24:10 → 10:24:31** — o arquivo acompanhando o relógio
de quem lê. Duas consequências, e as duas foram para a **29.5**:

1. **"mtime recente" nunca vai delatar esta falha.** O arquivo parece recém-salvo **todos os dias**, inclusive
   nos dias em que está errado. O portão que qualquer um escreveria primeiro — vigiar a data do arquivo da porta
   de entrada — **vigiaria ruído**. Quem for vigiar a porta vigia o **conteúdo**: quais blocos `# BEGIN`
   existem. É a família do "número de tela digitado" da seção 8 — o sinal que parece medição e não mede nada.
2. **O reescritor preserva o que encontra**, e o bloco do WordPress sobreviveu às três reescritas medidas depois
   do reparo. Junto com (1): o arquivo é reescrito centenas de vezes por dia e **todas as reescritas copiam
   fielmente o estado anterior** — logo a perda **não é desgaste gradual**. Existe **um** evento que gravou o
   arquivo sem o bloco, e todas as reescritas seguintes propagaram a ausência. **Procura-se um evento com hora,
   não um processo** — e isso é o que estreita a causa que a 29.5 declara sem nome.

## O BLOCO: A SERP DAS TRÊS MÃES DO GUIA, E `espera_serp` ZEROU

Escolhido pela fila: o item do 4c nomeava *"medir a SERP de `alicate` — busca, não coleta"* como o que destrava a
segunda categoria do Guia, *"o mesmo vale para `pastilha` e `rejunte`"*. **É medição, não construção**: não cria
URL, não gasta leva da 21.4 e não precisa de Sync — e pela **18.5** era o que cabia numa passada que começou
achando a ilha fora do ar.

`dados/serp-das-filhas.json` foi de **10 para 15** medições (três mães + duas filhas), e
`dados/cruzamento-14-9.md` foi **regerado pelo portão**, nunca pela mão: `--autoteste` **32 casos, 0 falha**;
`--conferir` **APROVADO**. **Não há mais nenhum recorte em "dado verde e SERP nunca olhada"** — o estado que o
próprio arquivo chamava de *"o caso que mais custou nesta ilha, porque parece passe livre"*.

| recorte | antes | agora | o que falta agora |
|---|---|---|---|
| `alicate` (mãe) | `espera_serp` | **`pode_nascer`** | nada nela: os dois portões abriram |
| `rejunte` (mãe) | `espera_serp` | **`pode_nascer`** | nada nela: os dois portões abriram |
| `pastilha` (mãe) | `espera_serp` | `espera_autoridade` | autoridade: 7 de 9 são loja, fabricante ou marketplace |
| `rejunte/cimenticio` | `sem_nenhum_dos_dois` | **`espera_dado`** | **UMA coisa:** `liberacao_area_molhada_h` nos 3 itens |
| `alicate/torques` | `sem_nenhum_dos_dois` | `sem_nenhum_dos_dois` | SERP **TOMADA** (7 de 10 lojas): **não é** o caminho |

## E O BLOCO PROVOU ERRADA A FRASE QUE O MANDOU — a parte que a próxima execução precisa ler

A fila dizia, em 02/10: *"O que a destrava é medir a SERP de `alicate`, e com ela a segunda categoria do Guia
sai com a mesma leva de quatro."* **Não saiu.** A frase confundiu dois portões: a mãe estava de fato em
`espera_serp`, mas o que a **16.5** cobra são **3 filhas no cruzamento** — e **as filhas não param na SERP,
param no DADO**. `alicate` e `rejunte` foram as duas para `pode_nascer` e **nenhuma das duas pode nascer**:
`alicate` tem 1 filha no cruzamento e `rejunte` tem 0.

**O caminho mais curto trocou de dono: é o `rejunte`, não o `alicate`.** A mãe já passa os dois portões, e
`rejunte/cimenticio` está a **um número** de passar — os 3 itens já existem e falta `liberacao_area_molhada_h`
neles, declaração de fabricante, o mesmo tipo de lastro que a `acabamento` juntou **por busca** em 25/09. As
outras duas filhas de `rejunte` (`acrilico`, `epoxi`) têm 1 item cada e precisam de 2 mais cada uma. Já o
`alicate/torques`, que parecia o atalho óbvio, **saiu TOMADA** — e isso é informação negativa que poupa a
próxima passada de tentar.

## A ARMADILHA DE CONSULTA QUE FICOU MEDIDA, E ELA DECIDE O QUE SE ESCREVE

`rejunte para mosaico` **cru** cai na SERP de **obra** — o corpus de 10/09 já tinha medido: cálculo de piso,
Viva Decora, Omni. A **pergunta sobre peça artesanal** cai numa SERP com **ZERO marketplace, ZERO loja e ZERO
fabricante em 10 de 10**, a mais aberta que esta ilha já mediu. São **duas SERPs vizinhas**, e a frase da página
decide em qual ela aterrissa: quem escrever `rejunte` mira a pergunta da peça, nunca o termo cru.

**E a margem está escrita no `motivo`, porque ela é fina:** 8 dos 10 respondem obra, e o décimo é a **biografia
de uma pessoa na Wikipedia**. Isso é **SERP rala, não SERP conquistada** — o único resultado que fala do assunto
desta ilha é um blog de mosaico, e é só ele que sustenta `ABERTA` em vez de `ABERTA_SEM_INTENCAO_NA_SERP`, cuja
definição exige que **nenhum** fale.

## A LEITURA DO ARQUIVO ACERTOU PELA QUARTA VEZ, COM UM REFINAMENTO

`as_abertas_sao_pergunta_e_as_tomadas_sao_produto` previu `alicate/torques` (consulta que nomeia o produto → 7
lojas) e previu `pastilha`. **O refinamento é que forma de pergunta NÃO basta:** `qual pastilha escolher para
fazer mosaico artesanal` **é** pergunta e saiu **TOMADA**, porque quem vende pastilha vende exatamente para
mosaico. **O que decide é se o vendedor do produto mira ESTE nicho.** No rejunte ele mira obra — e é por isso
que a pergunta do artesanato ficou vazia. Está escrito no `motivo` das medições.

## O QUE ESTA EXECUÇÃO NÃO FEZ, DE PROPÓSITO

- **Não publicou página nem acionou o Sync.** Medição não cria URL; o manifest segue na 56.
- **Não estimou faixa de volume.** As faixas das três mães vieram de `dados/corpus-buscas.md` (Planejador, conta
  do Raphael); a de `rejunte/cimenticio` ficou **`null`**, nunca estimada — o pedido de faixa já é despacho
  aberto e subiu de 6 para **7** consultas.
- **Não coletou SKU** para fechar as filhas de `rejunte`. Isso é o próximo bloco, e agora ele tem alvo único.
- **Não abriu o chamado na HostGator** nem falou com fornecedor: virou despacho ALTA para o Raphael.
- **Não tocou em nenhuma outra ilha.** Reserva é por ilha (seção 1).

## BANCADA DESTA EXECUÇÃO

`cruzamento-14-9.py --autoteste` **32 casos, 0 falha** · `--conferir` **APROVADO** · `conferir-no-ar.py` **524
afirmações, 0 falha** · `leitura-do-visitante.py` **22 URLs, 1 defeito** (o soft 404 da borda, de 29/09, com
dono escrito) · cabeçalho do `ESTADO.md` por `yaml.safe_load` com **teste de presença dos 8 campos: YAML ok**.

## PRÓXIMO PASSO DESBLOQUEADO

**Fechar `rejunte/cimenticio` pelo dado:** `liberacao_area_molhada_h` nos 3 itens que já existem, por busca, com
`literal_do_fabricante` — exatamente o método que tirou a `acabamento` do zero em 25/09. Com ele a filha sai de
`espera_dado` para `pode_nascer`, e então faltam **2 filhas** para a mãe `rejunte` cumprir a 16.5 e a segunda
categoria do Guia nascer com a leva de quatro. **O que NÃO falta mais é SERP** — em recorte nenhum.

---

02/10/2026 19h16Z — O BLOCO 4c: A PRIMEIRA CATEGORIA DO GUIA NASCEU, E NASCEU COM AS TRÊS FILHAS

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **19h16Z** e push da reserva aceito na
primeira tentativa (`e52777e`). `executando_desde` estava `null` e o último commit da ilha era de
16h56Z, duas horas e vinte antes — pela 1.1, ilha livre sem desempate.

**Quatro URLs novas**, a ilha vai de **17 para 21**. Casca na **1.19.0** sem mudança; snippet novo
`Clube do Mosaico Guia` **1.0.0**; manifest na **revisão 56**.

## A PORTA DE ENTRADA, ANTES DO BLOCO (seção 20.2)

`https://clubedomosaico.com.br/` em **200** na primeira tentativa. A ronda técnica da Sentinela
tinha fechado às 14h51Z com 17 de 17 URLs em 200 e zero defeito novo; este bloco não remediu o que
ela mediu há quatro horas.

## O BLOCO: `acabamento`, a mãe e as três filhas

**Quem escolheu a categoria não foi esta execução — foi o `cruzamento-14-9.py`**, escrito às 16h2xZ
de hoje. `acabamento` é o único recorte desta ilha em que os **dois** portões da 14.9 abriram ao
mesmo tempo, na mãe **e** nas três filhas:

| recorte | dado (seção 9) | SERP (14.9) | veredito |
|---|---|---|---|
| `acabamento` | passa, 10 itens | ABERTA | **pode_nascer** |
| `acabamento/selador` | passa, 3 itens | ABERTA | **pode_nascer** |
| `acabamento/verniz` | passa, 4 itens | ABERTA | **pode_nascer** |
| `acabamento/impermeabilizante` | passa, 3 itens | ABERTA | **pode_nascer** |

As quatro saem numa leva só porque é o que a **16.6** manda — *"primeiro a mãe e suas 3 primeiras
filhas"*, nunca uma filha de cada categoria espalhada —, e porque a **16.5** só deixa a mãe nascer
com três filhas. A `alicate/cortador_de_azulejo`, que também está em `pode_nascer`, **ficou de
fora**: a mãe dela está em `espera_serp` e uma filha sozinha pendurada em `/materiais/` seria
cluster ralo, que é exatamente o que a 16.6 proíbe.

**A ÁRVORE DESTA ILHA SERVE TRÊS SEGMENTOS PELA PRIMEIRA VEZ.** As quatro páginas de nível 3 que
existiam antes — as duas ferramentas e as duas técnicas — vivem em dois segmentos por estado de
transição declarado: a categoria delas não existia quando nasceram, e a 12.1 proíbe mover URL
publicada. Este é o primeiro bloco em que a **categoria nasce antes da filha**, e por isso o
primeiro que não precisa do estado de transição. Endereços:

- `/materiais/acabamento/` — nível 2, mãe `/materiais/`
- `/materiais/acabamento/selar-a-base-antes-de-fazer-mosaico/`
- `/materiais/acabamento/verniz-para-peca-de-mosaico/`
- `/materiais/acabamento/impermeabilizar-peca-de-mosaico/`

## O NÚMERO CALCULADO DA SEÇÃO 9, E ELE NÃO FOI ESCOLHIDO PARA PREENCHER O PORTÃO

É a **cobertura declarada**: das **15 superfícies** que o vocabulário do esquema nomeia (9 bases e 6
caquinhos), quantas a frase do próprio fabricante de cada produto alcança — e, portanto, quantas ele
não alcança. Contado, por página, do banco:

| página | produtos | combinações | nomeadas | superfícies alcançadas |
|---|---|---|---|---|
| `acabamento` (mãe) | 10 | 150 | **13** | 4 de 15 |
| `selador` | 3 | 45 | **4** | 3 de 15 |
| `verniz` | 4 | 60 | **2** | 1 de 15 |
| `impermeabilizante` | 3 | 45 | **7** | 3 de 15 |

**Este número é literalmente o que a medição de SERP de hoje chamou de "o número que a SERP não
publica".** Os dez resultados que ocupam a consulta de impermeabilizante dizem *emulsão de
silicone*, *tinta betuminosa duas ou mais demãos* e *silicone ou verniz*: tipo de produto, sem
marca, sem produto e sem número. Nenhum deles diz **sobre o quê** o fabricante escreveu que o
produto pode ir. A ausência medida é o produto desta ilha.

**O SEGUNDO NÚMERO É O RELÓGIO**, aritmética desta ilha sobre três declarações, no mesmo desenho dos
gramas de rejunte da F1: `(demãos − 1) × intervalo entre demãos + secagem final`. Ele fecha em
**2 dos 10** produtos e **só neles** — o Selador Acrílico da Coral (1 demão, 5 h) e a Resina Acrílica
da Coral (3 demãos, 4 h entre elas, 12 h final: **20 horas**). Nos outros oito falta uma das
parcelas e a página **diz que o fabricante não declara**, em vez de emprestar o número do vizinho de
prateleira — que é o erro escrito dentro do próprio `quartzolit-fundo-selador`, no registro dele.

## O QUE ESTAS PÁGINAS SE RECUSAM A FAZER, E A RECUSA É CONTADA

Nenhuma linha deste snippet **escolhe produto para uma base**. Não é omissão: é o esquema.
`regras_da_categoria_acabamento` diz, desde 25/09, que acabamento não entra na matriz base ×
ambiente, porque *"acabamento não adere duas coisas uma na outra e não se escolhe por ambiente
declarado"* — e por isso todo registro da categoria nasce com as seis listas de `declaracoes`
vazias, o que é portão no `validar-banco.py`. Montar uma régua de "qual verniz para qual peça" em
cima de declarações que não falam de peça de mosaico seria inventar a recomendação.

E a lacuna é **derivada**, não escrita: o vidro, a pastilha de vidro e o rejunte entram na frase
porque a conta diz que faltam. No dia em que um fabricante nomear vidro, a frase do vidro some
sozinha — e **a bateria de mutações fabrica esse dia e exige que ela suma**.

## A DÍVIDA QUE ESTE BLOCO ACHOU NO CAMINHO, E ELA NÃO ERA DESTA CATEGORIA

**O banco de `acabamento` nunca tinha sido lido por uma página, e por isso estava sem acento.**
`ferramentas/restaurar-acentos.py` existe desde 11/09 exatamente para isto, e o cabeçalho dele diz
com estas palavras: *"o banco nasceu sem acento porque foi digitado a partir de busca, e até aqui
ele só era lido por ferramenta; no dia em que uma PÁGINA passou a servi-lo, o defeito virou texto no
ar"*. Hoje foi esse dia. `CAMPOS_DE_TELA` via `marca`, `fabricante` e `nome_comercial`, e a
declaração do fabricante de `acabamento` mora em `protecao.literal_do_fabricante` — campo que
nenhuma outra categoria tem, criado em 25/09.

- O alcance cresceu para `protecao.literal_do_fabricante`, `protecao.trecho_que_declara_o_momento` e
  `propriedades.*.valor`. O `declarado_como` e o `motivo` **ficaram de fora de propósito**: a página
  publica o **número**, não a frase de onde ele saiu, e acentuar o que ninguém lê é alargar a
  superfície sem ganho.
- **41 palavras** entraram no mapa, uma a uma, só aquelas cuja forma acentuada é a única leitura
  possível; **164** foram para `_CONHECIDAS` porque não precisam de acento. **21 trocas gravadas**,
  e o `--provar` aprovou: reduzidas a sem-diacrítico, as 21 são byte a byte iguais às de antes.
- Duas das trocas são de **outros bancos** (`flexível` na pastilhart, `manutenção` na cortag): elas
  não chegam à tela hoje, mas o campo passou a ser de tela e a categoria delas nasce depois — foi a
  ordem inversa que criou aquela ferramenta.
- O aviso de palavras fora do mapa fecha hoje em **zero**, pela primeira vez.

## DOIS PORTÕES DA ILHA ESTAVAM CRAVADOS NO "HOJE", E OS DOIS FORAM DERIVADOS

Os dois reprovaram a casca por ela estar **certa** — e os dois reprovariam qualquer bloco que fizesse
a ilha crescer:

1. **`nenhum cartao de categoria e link hoje (16.5)`**, cravado em `0 === $viraram_link`. A 16.5 não
   diz "nenhum cartão abre"; ela diz que cartão **sem página** não vira link. Agora o esperado é a
   contagem de categorias que têm página declarada, e ela cresce sozinha.
2. **`os blocos de recusa sao poucos e contados`**, com teto **4**, que era o retrato de uma ilha de
   nove páginas. Ele teria reprovado esta leva por existir — quatro páginas novas, uma recusa cada,
   todas legítimas. Virou **no máximo um bloco de recusa por página**, medido por página.

**E UMA MUTAÇÃO ESTAVA INERTE DESDE 28/09, achada de passagem:** `noindex na pagina errada`, em
`mutacoes-voz-e-cabeca.py`, casava a entrada da página `materiais` escrita em **uma linha só**; na
casca 1.16.0, de 28/09, aquela entrada ganhou o campo `descricao` e virou várias linhas. É a mesma
família — e o mesmo dia — do que o bloco de 28/09 achou em `mutacoes-arvore.py`. O conserto é não
casar mais a linha inteira.

## AS DUAS BANCADAS NOVAS, E O QUE A SEGUNDA ACHOU NA PRIMEIRA

- **`ferramentas/teste-guia.php`** — **106 afirmações, 0 falha**. O portão da 14.9 **nos dois
  sentidos** (nenhuma página sem autorização **e** nenhum recorte autorizado sem página, que é a
  metade que impede a família de parar calada); a cobertura e o relógio recontados do JSON cru por um
  caminho que não chama uma linha do snippet, conferidos contra o número **na tela**; a prestação de
  contas da seção 7; a 16.4(a) com a consulta-alvo como texto-âncora e a 16.4(b) com a mãe linkada no
  **corpo**, fora dos `<nav>`; o `rel` de cada link derivado do que o link **é**; a frase da lacuna.
- **`ferramentas/mutacoes-guia.py`** — **14 mutações, 14 decididas certo**. Onze reprovam, uma fica
  honesta (banco fora do ar), uma degrada (F2 fora do ar) e uma **passa** (um fabricante nomeia vidro
  e a lacuna some sozinha).
- **E a bateria achou TRÊS buracos na bancada recém-escrita, na primeira passada**, que é o motivo de
  ela existir: (a) a frase da lacuna podia virar lista escrita à mão e passar; (b) a busca **crua**
  podia se declarar `sponsored` e passar — a régua media "tem rel", não "tem o rel certo"; (c) a
  própria mutação do vidro media o corpo inteiro em vez da frase. Os três viraram portão.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Nenhuma das quatro declara promessa no `<title>`.** A alavanca da 12.1 é para a banda de posição
  4 a 10: título que promete número numa página que já está na primeira página e não é clicada. Estas
  nascem hoje, sem impressão e sem posição — não há CTR a consertar. O portão que cobra a lista
  inteira de páginas com promessa, nas duas direções, foi quem apontou isso.
- **A faixa de volume das consultas continua `null`.** O Planejador é do Raphael e o pedido está em
  `dados/despachos.md`. Ela não decide se a página nasce; decide a ordem da leva (1.2-b.3) — e a
  execução das 16h2xZ já tinha escrito que quem publicasse o 4c podia publicar sem ela e **não podia
  estimá-la**.
- **Nenhuma URL antiga se moveu**, nenhum 301, nenhum `<title>` e nenhuma `description` existente
  foram tocados: a janela de comparação do BLOCO A, que fecha em **08/10**, continua limpa.

## O DESEMBARQUE E A VERIFICAÇÃO NO AR (seção 8 e 18.4)

Sync acionado por `curl` às **19h52Z**: *revisão 56, 15 aplicados*, `snippets/guia: ok (snippet #13
criado)`. `/status` na **revisão 56**, igual à do `manifest.json`. As quatro URLs novas em **200**,
com quebra de cache. `conferir-no-ar.py` **APROVADO: 524 afirmações medidas no HTML servido, 0
falha** — agora sobre **21** URLs do sitemap, com as quatro novas dentro da faixa de 120–160 na
`description`, no teto de 65 no `<title>`, com JSON-LD, `BreadcrumbList` e sem `&#038;` dentro de
`<script>`. O soft 404 na borda **continua** e segue com o Raphael desde 29/09: registro, não portão.

**E um rótulo do próprio `conferir-no-ar.py` estava cravado**, achado na saída desta verificação:
quatro linhas diziam *"as 17 URLs"* com a medida ao lado dizendo **21**, na mesma linha. O portão
sempre varreu `_urls_sitemap` inteiro e estava **certo** — só o texto envelheceu. Mas rótulo que
discorda da medida ao lado é o que faz alguém ler "17" e não contar. Passou a sair do `len()`.

As cinco baterias de mutação que este bloco podia ter quebrado foram rodadas e as cinco fecham
verdes: `mutacoes-arvore` 29/29, `mutacoes-voz-e-cabeca` **24/24 depois do conserto das três
inertes**, `mutacoes-promessa-do-titulo` 19/19, `mutacoes-acabamento` 14/14 e `mutacoes-guia` 14/14.

## PRÓXIMO PASSO DESBLOQUEADO

**Medir a SERP das três mães em `espera_serp` — `alicate`, `pastilha` e `rejunte`.** É o estado que
parece passe livre (dado verde, SERP nunca olhada) e é o trabalho mais barato que sobrou nesta fila:
é **busca, não coleta**. Com a SERP de `alicate` medida, a `alicate/cortador_de_azulejo` — que já
está em `pode_nascer` — ganha mãe e a segunda categoria do Guia pode sair com a mesma leva de
quatro. O caminho agora é um comando: `python3 ferramentas/cruzamento-14-9.py` depois de escrever a
medição em `dados/serp-das-filhas.json`, e o veredito sai calculado.

02/10/2026 16h17Z — O PORTÃO DE SERP DEIXOU DE SER PROSA, E O 4c DE `acabamento` ESTÁ LIBERADO PELOS DOIS PORTÕES

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **16h17Z** e push da reserva aceito na
primeira tentativa (`2d16710`). Manifest e `/status` seguem na **revisão 55**: este bloco **não
mudou nada que o Sync publique** — nenhuma URL nova (a ilha segue em **17**), nenhum endereço,
nenhum `<title>` e nenhuma `description`. A janela de comparação do BLOCO A continua limpa e o
veredito dele segue de **08/10**. Por isso não houve acionamento do Sync: não havia o que
desembarcar.

## A PORTA DE ENTRADA, ANTES DO BLOCO (seção 29.2)

`conferir-no-ar.py` **APROVADO: 524 afirmações, 0 falha**, antes de qualquer mudança. As 17 URLs do
sitemap em 200, as 17 descriptions na faixa de 120–160, os títulos no teto de 65, `/status` igual ao
`manifest.json`. O soft 404 na borda **continua** — registro e não portão, com dono escrito desde
29/09.

## O BLOCO: O CRUZAMENTO DA 14.9 VIROU PORTÃO, E ELE ABRIU O 4c NUMA CATEGORIA

**O que a execução das 13h17Z deixou escrito, palavra por palavra:** *"o portão de DADO abriu, o de
SERP é outro. (...) Quem publicar o 4c cruza os dois, como a 14.9 manda."* Este bloco cruzou — e
descobriu que **cruzar era o problema**, não o resultado.

**O DIAGNÓSTICO, e ele é de arquitetura:** as duas metades da 14.9 existiam desde 30/09 e nunca se
encontraram num veredito. O portão de **dado** da seção 9 era número derivado do banco
(`dados/filhas-do-guia.json`). O portão de **SERP** era **prosa**, numa seção de
`dados/filhas-do-guia.md` que o gerador preserva **sem ler** — e o próprio cabeçalho daquele gerador
diz, de si mesmo, que *"não classifica SERP"*. **Prosa não cruza com número.** O custo é datado: a
pergunta "o 4c pode nascer?" exigia abrir dois arquivos e fazer a conta na cabeça, e o `ESTADO.md`
das 13h17Z teve de escrever **à mão** o aviso para a execução seguinte não ler passe livre. Aviso à
mão é o que um portão substitui.

**A MEDIÇÃO QUE FALTAVA — duas filhas que nunca tiveram SERP olhada, e a mãe também não.** Quatro
consultas novas, com os três limites do canal respeitados (frase inequivocamente portuguesa, nenhuma
marca dentro da consulta, e sem afirmar posição de ninguém, porque este canal não dá ordem):

| recorte | consulta | quem ocupa | classe |
|---|---|---|---|
| `acabamento` (a mãe) | *acabamento para peça de mosaico artesanal qual produto passar depois do rejunte* | Catraca Livre, Benjoino (2010), NeuralWord, **mosaico.arq.br (4, e é obra)**, Artesanato Passo a Passo, Portal das Maravilhas, Artesanato Local (2010) | **ABERTA** |
| `acabamento/selador` | *precisa passar selador na base antes de colar mosaico em MDF ou cerâmica* | 9 dos 10 são **pintura de parede** | **ABERTA, SEM INTENÇÃO NA SERP** |
| `acabamento/selador` | *selar vaso de cerâmica antes de fazer mosaico artesanato precisa selador* | Cenário Tocantins, Viva Decora, Sua Decoração, umComo, Terra, Limpeza.com, Wikipedia | **ABERTA** |
| `acabamento/impermeabilizante` | *como impermeabilizar peça de mosaico para ficar no jardim na chuva* | forumdacasa.com PT (2), Benjoino (2010), FazFácil (2), Casas Jardim, Redelease, soudal.pt | **ABERTA** |

**Zero marketplace nas quatro.** E a classe da segunda linha **é nova**, e nasceu da medição em vez
de ter sido escolhida: `ABERTA_SEM_INTENCAO_NA_SERP` diz que ninguém ocupa **porque nenhum resultado
do top 10 fala da pergunta desta ilha** — a SERP respondeu o nicho vizinho da pintura de parede.
Chance alta e intenção **não provada**, que é literalmente a metade *"chance alta sem intenção"* que
a 14.9 nomeia e que a legenda de três classes do corpus não sabia descrever. Ela entrou na legenda.

**O QUE FOI CONSTRUÍDO, e é o que fica depois do veredito de hoje:**

- **`dados/serp-das-filhas.json`** — a metade **coletada**, agora em dado: dez medições, com quem
  ocupa escrito pelo nome, data **por medição**, os três limites do canal declarados, as cinco
  classificações e o número que a SERP não publica. **As seis medições de 30/09 foram movidas para
  cá sem uma palavra alterada.**
- **`ferramentas/cruzamento-14-9.py`** — o portão. Lê as duas metades de arquivos diferentes e
  devolve **um** veredito por recorte, dos seis que **calcula e nunca escreve**: `pode_nascer`,
  `pode_nascer_sem_demanda_medida`, `espera_autoridade`, `espera_dado`, `espera_serp`, `nunca`.
  Bancada: **`--autoteste` com 32 casos fabricados, 0 falha**, e `--conferir` que regera e compara.
- **`dados/cruzamento-14-9.md`** — a saída, derivada e não digitada.
- **A segunda verdade foi apagada:** a tabela de SERP em prosa saiu de `dados/filhas-do-guia.md` e o
  que ficou ali é um ponteiro para os dois arquivos novos, com o motivo. **Uma fonte por campo.**

## O VEREDITO: `acabamento` É A PRIMEIRA CATEGORIA DO GUIA A PASSAR OS DOIS PORTÕES

| recorte | dado | SERP | veredito |
|---|---|---|---|
| `acabamento` (a mãe, que é o 4c) | `passa`, 10 itens | ABERTA | **`pode_nascer`** |
| `acabamento/verniz` | `passa`, 4 itens | ABERTA | **`pode_nascer`** |
| `acabamento/selador` | `passa`, 3 itens | ABERTA | **`pode_nascer`** |
| `acabamento/impermeabilizante` | `passa`, 3 itens | ABERTA | **`pode_nascer`** |
| `alicate/cortador_de_azulejo` | `passa`, 3 itens | ABERTA | **`pode_nascer`** |
| `pastilha/vidro` | `passa`, 13 itens | TOMADA | `espera_autoridade` |

Dos 42 recortes: **5 `pode_nascer`**, 1 `espera_autoridade`, 3 `espera_serp`, 33
`sem_nenhum_dos_dois`. **A ordem da 7b — banco, depois as filhas de nível 3, só então a mãe de nível
2 — foi percorrida inteira numa categoria pela primeira vez desde 12/09.**

## O ACHADO QUE VALE MAIS QUE O VEREDITO: A 16.5 CONTA FILHA, E FILHA NÃO É FILHA NO DADO

A 16.5 exige 3 filhas de nível 3 para a mãe nascer, e até hoje "filha" era lida na contagem do
**dado**. O cruzamento põe as duas contagens lado a lado e elas **discordam**:

| categoria | filhas que o DADO autoriza | filhas que o CRUZAMENTO autoriza |
|---|---|---|
| `acabamento` | 3 | **3** → a mãe pode nascer |
| `pastilha` | 1 | **0** |

**A `pastilha` é a de mais banco da ilha** — 13 itens, três números em 12 deles — e a filha dela que
passa no dado é justamente a que a SERP recusa. Pela contagem do dado ela estava a **duas** filhas da
mãe; pelo cruzamento, a **três**. Nenhum dos dois arquivos de entrada mostra isso sozinho, e o caso
tem autoteste próprio na bateria (`3 filhas verdes no dado e 2 no cruzamento`, mais o caso da **mãe
TOMADA com 3 filhas abertas**, que sem o portão faria a mãe nascer para uma SERP de marketplace).

**E três recortes ficaram com `espera_serp` — `alicate`, `pastilha` e `rejunte`, as três mães: dado
verde e SERP nunca olhada.** Esse veredito existe por nome próprio porque é **o estado que parece
passe livre**. Medir as três é busca, não coleta de banco: é o trabalho mais barato que sobrou nesta
fila.

## O DEFEITO QUE A PRÓPRIA EXECUÇÃO ACHOU, ANTES DE QUALQUER COMMIT

A primeira versão do `cruzamento-14-9.py` cravava, no veredito `sem_nenhum_dos_dois`, a frase *"os
dois: nem 3 itens de banco, nem SERP medida"* — e ela era **FALSA** em `alicate/torques` e
`rejunte/cimenticio`, que **têm** 3 itens e param por lastro e por número comum, não por contagem.
Achado lendo o documento gerado, não por portão. Corrigido extraindo `falta_no_dado()`, que **deriva**
a frase da distância que o portão de dado já mediu, e agora as duas saem certas: *"2 itens com fonte
que sustente recomendação primária"* e *"um número que a página calcule sobre 3 itens do mesmo
recorte (a propriedade mais perto é `liberacao_area_molhada_h`)"*. **A lição é a de sempre nesta
ilha: frase cravada envelhece calada; frase derivada não.**

## O PEDIDO AO RAPHAEL É DERIVADO, E A FAIXA NÃO FOI ESTIMADA

Nenhuma das **seis** consultas abertas tem faixa de volume. O Planejador está na conta dele, a nuvem
não abre painel autenticado, e o campo ficou **`null` nos dez registros** em vez de preenchido por
palpite — que é o que o cabeçalho do `corpus-buscas.md` já proibia para o CPC desde 10/09. O pedido
entrou em `dados/despachos.md` com a lista **derivada pela ferramenta**, consulta por consulta, com o
recorte que a exige; e só consulta ABERTA entra, porque faixa de consulta que não vai nascer é número
que ninguém usa. O portão confere sozinho: `Pedido de faixa ao Raphael: N` encolhe quando o número
chega, **não quando alguém edita a lista**.

**E está escrito que não é bloqueio:** a faixa **não decide se a página nasce** — decide a **ORDEM da
leva**, que é o que a 1.2-b.3 manda sair da medição e não da rotação. Quem pegar o 4c de `acabamento`
pode publicar sem ela.

## O RÓTULO VELHO QUE O CRUZAMENTO DERRUBOU NO CORPUS

A medição de 30/09 deixou escrito que o corpus classificava `pastilhas de vidro para mosaico` como
**ABERTA** com a **mesma evidência** que a régua da 14.9 lê como **TOMADA**, e mandava: *"quem for
mexer no corpus lê este parágrafo primeiro"*. **Mexido hoje:** o rótulo daquela linha virou
`~~ABERTA~~ → TOMADA`, com a evidência **intacta** e a diferença entre as duas réguas escrita na
própria linha — o corpus chamou de aberta porque ninguém responde a pergunta técnica, e a 14.9 manda
classificar **quem ocupa**, que é o galho do *"a página NÃO nasce agora"*. **O achado do bloco de
10/09 continua inteiro; o que ele nunca foi é autorização para a página nascer.** E as cinco consultas
de `acabamento` entraram na seção 1E, com a SERP **citada** daqui e a fonte no JSON novo.

## BANCADA

`conferir-no-ar.py` **524 afirmações, 0 falha** (antes do bloco) · `validar-banco.py` verde, 41
materiais · `validar-pastilhas.py` 189 afirmações, 0 falha · `cobertura.py --conferir` OK ·
`filhas-do-guia.py --conferir` aprovado nas três pernas e `--autoteste` 27 casos 0 falha ·
`cruzamento-14-9.py --conferir` aprovado e **`--autoteste` 32 casos 0 falha** · mutações:
acabamento 14, base 20, apoio 24, degrau 8, motivo-degrau-4 10, batismo 14, casamento 5, árvore 29,
pastilhas 14, cobertura 14 — **todas reprovaram, nenhuma passou** · `atualizar-manifest.py --gravar`
com os 5 sha impressos, e ele **acusou a ferramenta nova fora do manifest** antes de eu a registrar,
que é o portão dele funcionando.

O soft 404 na borda **continua** e segue com o Raphael desde 29/09 — vermelho esperado, com dono.

---

02/10/2026 13h17Z — A PRIMEIRA CATEGORIA DO GUIA A ALCANÇAR AS 3 FILHAS DA 16.5, E QUATRO FERRAMENTAS QUE MEDIAM MENOS DO QUE PROMETIAM

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h17Z** e push aceito na primeira
tentativa. Manifest e `/status` na **revisão 55**. **NENHUMA URL NOVA** — a ilha segue em 17 —, e
**nenhum `<title>` e nenhuma `description` foram tocados**: a janela de comparação do BLOCO A
continua limpa e o veredito dele segue de **08/10**.

## A PORTA DE ENTRADA, ANTES DE QUALQUER BLOCO (seção 29.2)

Rede pela **20.2**, antes de trabalhar: `clubedomosaico.com.br` em **200**; o `/status` da rota REST
em **200** na revisão 54, igual à do manifest daquele momento. `conferir-no-ar.py`: **524 afirmações,
0 falha** na origem. `leitura-do-visitante.py` segue **REPROVADO pelo soft 404 da borda** — 404 na 1ª
leitura, 200 na 2ª com `x-proxy-cache HIT` e `max-age=7200` —, que é **vermelho esperado, com dono
escrito** desde 29/09 e fora do alcance de qualquer snippet daqui. **Nenhum defeito novo.**

## O BLOCO: O PRÓXIMO PASSO QUE O REGISTRO DE 30/09 DEIXOU ESCRITO, E ELE SAIU INTEIRO

O registro de 30/09 às 13h17Z fechou nomeando o passo: *"coletar **1 impermeabilizante e 2
seladores** fecha as **3 filhas de `acabamento`**, que é a categoria mais barata do Guia, e é o que
abre a primeira mãe de nível 2 desta ilha — o **4c**, parado desde 12/09"*. Saiu, e saiu inteiro.

**Entraram três registros**, por busca restrita ao domínio do fabricante, **duas passadas por SKU,
escritas de forma diferente e nenhuma delas carregando um valor** — as consultas pediram os
**rótulos** da ficha ("indicado para", "demãos", "rendimento", "secagem", "diluição", "composição",
"não indicado para"), que é o método que a categoria usou em 25/09:

| registro | tipo | o que a frase do fabricante nomeia |
|---|---|---|
| `suvinil-seladora-para-madeira` | selador | **`mdf_madeira`** — "superfícies internas não molháveis de madeira" |
| `coral-selador-acrilico` | selador | `alvenaria_tijolo` — "as mais diversas superfícies de alvenaria" |
| `coral-resina-acrilica` | impermeabilizante | `cimento_concreto`, `alvenaria_tijolo` e a tessela **`pedra`** |

**O NÚMERO QUE MOVEU, e ele é o portão e não a contagem:** `acabamento/selador` saiu de **1 para 3**
itens e `acabamento/impermeabilizante` de **2 para 3**, os dois **com lastro** (fonte de nível ≤ 3) e
os dois **com número calculável sobre o recorte inteiro** — `tempo_de_secagem_h` nos três seladores
(6 h, 2 h e 5 h) e `base_quimica` nos três impermeabilizantes (duas resinas acrílicas e um
silano-siloxano). Com `acabamento/verniz`, que já passava, **são 3 filhas de 3**, e
`dados/filhas-do-guia.json` registra `acabamento` como a **única categoria do Guia que alcança as 3
da 16.5**. Recortes que podem nascer hoje: de 7 para **9**.

**E os três NASCERAM NO DEGRAU 3, não no 4.** `coletar-shopee.py --ensaio` casou anúncio para os três
na primeira tentativa, e `--gravar` deu `url`, `url_produto` e **foto medida** a cada um — o caminho
normal de registro novo que o item 5 da fila já tinha deixado pronto, sem uma linha de código nova.
Banco em **41 materiais**, escada **1:1 · 2:5 · 3:18 · 4:17**, e o `motivo_sem_ficha` do degrau 4
segue em **17 de 17** porque nenhum dos três entrou lá.

## A DECISÃO DE ESQUEMA SAIU ANTES DA COLETA, QUE É O QUE A 1.2-b.4 EXIGE

A passada de 30/09 deixou a pergunta escrita como **pré-requisito**: *"quem coletar decide antes se
selador de alvenaria cabe em `regras_da_categoria_acabamento`, que é decisão de esquema e não de
coleta"*. **Decidido, e por escrito antes dos três registros entrarem — esquema na versão 10.** Cabe,
e o motivo não é tolerância: a seção define selador pelo **MOMENTO** ("na base ANTES de colar"), nunca
pelo substrato, e `alvenaria_tijolo` e `cimento_concreto` são **dois dos nove** valores de
`vocabularios.base` desta ilha. Recusar selador de alvenaria deixaria essas duas bases sem preparo
declarado **por decisão de esquema, não por falta de fonte**. O que não muda é
`o_que_esta_categoria_NAO_pode_sustentar`, e a trava disso não é a decisão: é a lista
`bases_do_vocabulario_que_a_frase_NAO_nomeia`, que cobre o vocabulário inteiro e não deixa o silêncio
passar. **Critério escrito depois do dado é critério dobrado para caber no dado que veio.**

## DOIS ACHADOS DE DECLARAÇÃO, E ELES VALEM MAIS QUE A CONTAGEM QUE FECHARAM

- **O selador deixou de ser um item que não serve MDF.** A observação de 25/09 estava escrita no
  dado: *"a categoria `selador` entra no banco com UM item, e ele não serve a base que a ilha mais
  usa"*. O `suvinil-seladora-para-madeira` é o **primeiro acabamento deste banco a nomear
  `mdf_madeira`** — a base mais comum da peça do ateliê. A faixa descoberta da categoria passou a ter
  dono.
- **A primeira frase de acabamento a nomear uma TESSELA, e ela vem com uma EXCLUSÃO.** A Resina
  Acrílica da Coral nomeia **`pedra`** ("pedras naturais"), e nenhum dos sete anteriores nomeava
  tessela nenhuma. No mesmo parágrafo o fabricante escreve que **não se recomenda o uso em superfícies
  horizontais** — e **tampo de mesa e centro de mesa são duas das coleções de uso da Loja desta
  ilha**. Nenhuma frase publicada pode indicar esse produto para peça horizontal, e o motivo é
  declaração do fabricante, não cautela nossa. É o lado que esta ilha quase nunca consegue citar.

**O QUE CONTINUA ABERTO, e agora está medido em dez em vez de sete:** das **dez** frases de
fabricante desta categoria, **zero nomeiam `vidro`** e **zero nomeiam rejunte** — as duas superfícies
que a peça de mosaico pronta expõe. A pendência `acabamento-nenhum-nomeia-vidro-nem-rejunte` fica
aberta, com uma tessela a menos de buraco.

## QUATRO DEFEITOS ACHADOS DE PASSAGEM, OS QUATRO DE ALCANCE, OS QUATRO NO MESMO COMMIT

Nenhum deles foi procurado; os quatro apareceram porque o bloco de hoje passou por eles. E os quatro
são da mesma família: **ferramenta que mede menos do que promete, e fecha verde.**

1. **`gerar-links-afiliado.py` datava os links com uma constante de 25/09.** A linha era
   `HOJE = '2026-09-25'`, digitada no dia em que a ferramenta nasceu, e é ela que vira
   `url_busca_gerada_em`. **Os três links encurtados de hoje nasceram datados de sete dias antes de
   existirem.** Não é cosmético: a 25.4-b manda reconferir palavra-chave que envelhece, e quem
   reconfere escolhe **pela data**. A data agora sai do relógio, em UTC.
2. **`restaurar-acentos.py` varria DOIS dos cinco bancos.** A tupla `ARQUIVOS` trazia só
   `materiais-colas` e `materiais-rejuntes`, os dois que existiam quando ela nasceu; **pastilhas,
   alicates e acabamento nunca foram varridos**, e nada acusava, porque ela sempre fechava "0 trocas"
   nos arquivos que ela via. Com os cinco: **47 trocas GRAVADAS**, e entre elas texto que estava **no
   ar** — `Verniz Acrilico Brilhante`, `Cortador de ceramicas e azulejos manual`,
   `Saint-Gobain ... Construcao Ltda.`. É a mesma família da mutação inerte de 28/09: **régua que não
   alcança aprova em silêncio.** Dez palavras entraram no mapa (as únicas, de 118 acusadas, cuja forma
   acentuada é a única leitura possível) e as outras 108 foram para `_CONHECIDAS` uma a uma, porque
   aviso que grita 118 palavras não é aviso.
3. **O `--provar` dessa mesma ferramenta estava prometido no cabeçalho e NÃO EXISTIA no código.** O
   cabeçalho diz desde 11/09 *"A OPERAÇÃO É PROVADAMENTE DIACRÍTICO-ONLY, e é o `--provar` que
   garante"*, e `sys.argv` era lido **só** para `--gravar`: `--provar` passava direto, ignorado em
   silêncio, imprimindo o mesmo relatório e dando a impressão de ter provado. **E é justamente essa
   prova que torna a ampliação do item 2 segura**, porque o que ela impede é "restaurar acento" virar
   reescrita de declaração de fabricante. Implementado — e **conferido que ele REPROVA de verdade**,
   adulterando o mapa numa cópia em `/tmp` e vendo a única violação ser acusada pelo nome. Portão que
   nunca reprovou nada não é portão.
4. **`mutacoes-base.py` e `mutacoes-apoio.py` estavam VERMELHAS no `main`, pela segunda vez em dois
   dias e pela mesma causa.** O comentário dentro delas conta a primeira: o aperto do degrau, em
   29/09, reprovava o **mundo fabricado** antes de qualquer mutação. A leva de 30/09 que subiu o
   esquema para a **versão 9** tornou `motivo_sem_ficha` obrigatório, com forma, para todo item no
   degrau 4 sem ficha — e as duas voltaram a cair, **dois dias**, sem ninguém as vendo. O que elas
   deixam sem medição não é pouco: **`base` e `apoio` são as duas únicas categorias sem SKU**, portanto
   as únicas cujos portões não têm banco real que os exercite. **Medido vermelho no `main` limpo**
   (`git stash`) antes de qualquer mudança desta execução, para não chamar de meu o que era de antes.
   Consertadas **derivando** o campo do estado fabricado em vez de cravá-lo, que é o que impede a
   terceira morte: **20 de 20** e **24 de 24**.

## E O PORTÃO CORRIGIU O DOCUMENTO, NÃO A MÃO

`filhas-do-guia.py --conferir` **reprovou** a tabela da seção 2 do `ARVORE.md`: ela dizia
`7 itens | 1 de 3` para `/materiais/acabamento/` e a derivação dizia `10 | 3 de 3`. As duas direções
foram medidas. O documento foi para 10 e 3 de 3, e a seção 7b-ter ganhou a atualização que diz, com
todas as letras, que **o parágrafo "o 4c continua fechado" é de 25/09 e deixou de descrever o mundo**
— e também que o selador já não é mais o item que não serve MDF. A régua fabricada da bancada
(`tabela()`, escrita à mão de propósito, para não chamar a função que ela mede) foi atualizada no
mesmo movimento, com a linha dizendo o preço disso: quem mudar o banco e vir aquele caso falhar não
tem defeito para procurar, tem dois números para reescrever.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Não criou nenhuma URL, e o portão de dado abrir não autoriza criar.** A **14.9** exige o
  cruzamento de intenção de compra com chance real de primeira página, e a medição de SERP de 30/09
  (em `dados/filhas-do-guia.md`) diz que as filhas publicáveis desta ilha hoje têm forma de
  **pergunta** e não de tipo: `verniz para peça de mosaico artesanal` está **ABERTA** e `pastilhas de
  vidro para mosaico` está **TOMADA**. Além disso **`verniz` não existe em `dados/corpus-buscas.md`**
  — sem faixa de volume medida. **Dois vereditos saem juntos ou nenhum dos dois serve.**
- **Não tocou em `<title>` nem em `description`** de nenhuma das 17 URLs. O BLOCO A espera a leitura
  da janela 23→30/09 por ordem escrita do Raphael, e a janela segue limpa.
- **Não inventou nome comercial.** Os três têm a caixa do **título** da página de produto (nível 3), e
  por `batismo_do_fabricante.origens_que_batizam` **só PDF batiza** — então os três ficam **fora do
  escopo da trava, com o motivo escrito em `motivo_do_batismo_pela_pagina`** em vez de aprovados em
  silêncio. `batismos conferidos` segue em 7.
- **Não escreveu `fabricante` de cabeça.** O da Suvinil ficou **null com motivo**: a marca trocou de
  dono e as duas passadas devolveram marca, não razão social. O da Coral é **AkzoNobel**, lido no
  próprio domínio do fabricante (`coral.com.br/content/dam/akzonobel-flourish/coral/`), com a razão
  social da entidade brasileira registrada como não obtida.
- **Não converteu rendimento em consumo** em nenhum dos três. Os fabricantes declaram m²/L e o campo
  pede mL/m²; converter é aritmética desta ilha, e o esquema proíbe a conversão nesse campo com essas
  palavras. Ficaram null **com motivo**, que é pergunta feita e respondida.
- **Não mexeu no egresso.** Reteste da **20.2** nesta execução: `loja.suvinil.com.br`,
  `suvinil.com.br`, `coral.com.br`, `vedacit.com.br`, `sayerlack.com.br` e `montanaquimica.com.br`
  em **000** por `curl` e **EGRESS_BLOCKED** por fetch; `www.quartzolit.weber` em **403**. Todo campo
  dos três carrega `conferir_no_pdf: true`, como os sete de 25/09.

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` verde: **41 materiais**, escada **1:1 · 2:5 · 3:18 · 4:17** (soma 41), degrau 4
com motivo **17 de 17**, itens sem saída de compra **0**, piso não rastreável **0**, casamentos
reconferidos **14**. `filhas-do-guia.py --autoteste` **27 casos fabricados, 0 falha** e `--conferir`
**aprovado**, nas duas direções. `cobertura.py` regerado e `--conferir` **OK**, com `mutacoes-cobertura` verde. `mutacoes-promessa-do-titulo` **19 de 19**. Mutações:
acabamento **14**, batismo **14**, casamento **17** (12 na regra + 5 no banco), degrau **8**, motivo-degrau-4 **10**, pastilhas
**14**, árvore **29 de 29**, **base 20 de 20** e **apoio 24 de 24** (as duas que estavam vermelhas).
`teste-batismo` **62**, `teste-casamento` **42**, `validar-pastilhas` verde. PHP: casca **601**, F2
**127**, técnicas **137**, F1 24 estados com processo próprio, Loja, Ateliê, Leads e Prestação
**aprovados** — **zero falha**. `restaurar-acentos --provar` **aprovada**, 47 trocas diacrítico-only.

## DESEMBARQUE E VERIFICAÇÃO NO AR

Push aceito na **primeira tentativa** (`1e2c211..50fc063`). Sync acionado **depois** do push, que é a
ordem certa porque ele lê o `manifest.json` do `main` pelo `raw.githubusercontent`.

**E a primeira leva de Sync NÃO entregou, por um motivo que vale escrever:** o Sync leu o manifest na
revisão **54** — a anterior — e devolveu **`sha256 divergente — não aplicado`** justamente nos três
bancos que este bloco mudou (`materiais-acabamento`, `materiais-alicates`, `materiais-pastilhas`). Não
era defeito do bloco nem do Sync: é o **cache do `raw.githubusercontent`**, que serviu o manifest
velho enquanto os arquivos de dado já vinham novos. Seis disparos ao longo de **cerca de quatro
minutos** e meio, e o sexto leu **55**. A lição operacional, para a próxima execução não diagnosticar
isto como sha errado: **`sha256 divergente` logo depois do push é cache de manifest até prova em
contrário — o reteste é um disparo, e a 20.2 já manda repetir antes de chamar de bloqueio.** Nesse
intervalo o ar ficou coerente, e não meio aplicado: o Sync recusa o par que não fecha, então os três
bancos continuaram servindo o estado anterior até o manifest novo chegar.

**Sync na revisão 55** às **14h13:46**, **14 aplicados** e 11 aguardando desembarque, com
`dados/materiais-acabamento`, `materiais-alicates`, `materiais-pastilhas` e `dados/esquema-banco`
todos em `ok`. `/status` devolvendo **55**, igual à do manifest.

**E no ar depois do desembarque: `conferir-no-ar.py` com 524 afirmações e 0 falha**, medido antes e
depois. O único vermelho da borda continua sendo o **soft 404 do hospedeiro**, com dono escrito desde
29/09.

**A correção de acento foi CONFERIDA NA TELA, não só no dado**, porque era disso que ela se tratava:
`/materiais/quantas-pastilhas-para-mosaico/` serve agora **`catálogo`** e **zero** ocorrências de
`catalogo` — antes deste bloco ela servia a palavra sem acento, e serviu assim por 21 dias sem que a
ferramenta que existe para isso olhasse aquele banco.

**A memória da ilha não foi atualizada porque ela não existe neste ambiente:** `/areas/` não está
montado, conferido nesta execução com `find`. O `PROMPT.md` desta ilha já prevê isto — *"Sem memória,
não pare: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta"* — e é onde o próximo
passo ficou escrito.

- **Próximo passo desbloqueado, e ele é uma ESCOLHA e não mais uma espera:** o 4c tem o portão de
  **dado** aberto em `acabamento` (3 de 3), e o que falta para publicar é o portão de **SERP** da
  14.9. As duas pontas estão medidas e discordam da fila: a filha de mais banco (`pastilha/vidro`,
  13 itens, três números) está **TOMADA** por marketplace, e a de SERP mais aberta
  (`verniz para peça de mosaico artesanal`) **não tem faixa de volume** em
  `dados/corpus-buscas.md`. Então o próximo bloco é um dos dois, e os dois são da Fundação: **(a)**
  medir `verniz` e os termos de acabamento no corpus, acrescentando-os a `dados/corpus-buscas.md`
  com faixa, concorrência e classificação de SERP — é o que falta para a 14.9 poder ser cruzada e
  não depende de ninguém; ou **(b)** levar a mesma régua de 3 itens a um recorte em forma de
  **pergunta** em vez de tipo, que é o que o próprio `filhas-do-guia.md` diz ser a forma que esta
  ilha publica (a F1 e a F2 são assim) — a régua já está na ferramenta para ser chamada em vez de
  reescrita. **(a) vem antes de (b)**, porque (b) sem faixa de volume publicaria escolhendo pelo
  dado que temos e não pela demanda, e foi por isso que a 14.9 existe.
- **O que continua fora do alcance daqui, e os dois seguem com o Raphael:** a leitura da janela
  23→30/09 (acesso do `sentinela@` a `sc-domain:clubedomosaico.com.br`, ou `GOOGLE_SA_B64` no
  ambiente), que é o veredito do BLOCO A e segue marcado para **08/10**; e o **curinga** de egresso
  dos domínios de fabricante, que trava o primeiro SKU de `base` e de `apoio` — a lista derivada,
  domínio por domínio, está em `dados/egresso-de-fontes.md`. O soft 404 da borda é o terceiro, aberto
  desde 29/09. **Nenhum dos três é pré-requisito do passo acima.**

02/10/2026 11:5xZ — A MARCA CEDEU O LUGAR AO NÚMERO NAS TRÊS QUE O GOOGLE JÁ MOSTRA

Manifest e `/status` na **revisão 54**, conferidos no ar. **Nenhuma URL nova** (a ilha segue
em 17), nenhum endereço mudou, nenhuma linha de corpo mudou. O que mudou é a etiqueta onde o
clique se decide: o `<title>` de **três** páginas e a `description` de **quatro**.
`conferir-no-ar.py`: **524 afirmações, 0 falha.** Bancada: teste-casca 601, teste-f1 210,
teste-f2 127, teste-tecnicas 137, teste-loja e teste-leads aprovados, 0 falha.

**O BLOCO desta execução é o BLOCO A do despacho do Raphael de 24/09**, que pela 18.1 vem
antes de tudo nesta ilha e que esperava uma coisa só: a janela de medição de **30/09**.
Hoje é 02/10 e ela fechou. No mesmo movimento saiu o **item 4 (metade)** do despacho da
Sentinela de 28/09 — a `description` é a outra metade da mesma promessa de SERP, e separar
as duas é exatamente o que o BLOCO A existia para impedir. Com isso **os despachos de 24/09
e de 28/09 estão fechados inteiros.**

## O QUE ESTÁ NO AR, E O QUE NÃO MUDOU

| página | `<title>` servido | nº | `description` | nº |
|---|---|---|---|---|
| qual-cola | …e qual rejunte **– 7 colas para 9 bases** | 64 | …7 colas em 270 casos…, e os 68 que a gente ainda não responde | 143 |
| quantas-pastilhas | …rejunte comprar **– 12 peças calculadas** | 64 | …12 peças já calculadas, de 23 a 960 pastilhas… | 139 |
| picassiete | …e como colar **– 7 colas em 45 casos** | 62 | …7 colas em 45 casos, pela declaração do fabricante | 150 |
| trencadís | …colar o caco – Clube do Mosaico (**INTOCADO**) | 62 | …o caco de azulejo ou de louça em cada superfície | 139 |

**O NOME DA PÁGINA NÃO FOI TOCADO EM NENHUMA DAS QUATRO**, e isso é a parte que mais importa:
o que cede o lugar é a **marca**, 16 caracteres de carimbo no fim de um título que está na
primeira página e não é clicado — numa ilha com **zero clique orgânico medido**, ninguém a
procura pelo nome. O `<h1>` servido continua `Qual cola usar no mosaico, e qual rejunte`, e a
promessa aparece **uma vez** no HTML inteiro: dentro do `<title>`. É a regra "UM NOME POR
PÁGINA" que esta ilha herdou da cicatriz que a Aquametria pagou em 11/09, e o caminho é o
precedente da Robometria de 17/09, portado: a casca **1.19.0** monta o título uma vez e quem
tem promessa a **declara** pelo filtro `cdm_promessa` — o mesmo contrato de camadas que a
`description` tem desde 28/09 e a etiqueta de robô desde 25/09.

## O TRENCADÍS FICOU PARADO, E A AUSÊNCIA DELE É A DECISÃO

O despacho de 23/09 manda, com estas palavras, *"deixe uma página parada para a próxima
leitura ter com o que comparar"*. Ele não declara promessa, e o portão mede isso nas **duas
direções** — promessa onde tem de haver, marca onde tem de ficar. Só a `description` dele
mudou, de 189 para 139, que era o que o item 4 cobrava. **Trocar as quatro de uma vez não é
zelo: é tornar a próxima medição ilegível**, e é o mesmo argumento que a Robometria escreveu
ao dar promessa a três cabeças e a nenhuma outra.

## NENHUM NÚMERO É DIGITADO, E A VARREDURA É A MESMA DA TELA

Os três números da `qual-cola` saem de `cdm_f2_cobertura()` — e ela **não é nova por
capricho**: a varredura de base × lugar × caquinho já existia dentro da seção "o que a gente
ainda não responde", contando ali e em lugar nenhum mais. Agora ela é contada **uma vez e
lida por três** (a seção da tela, a promessa do título e a `description`). Contar a mesma
coisa em três lugares é a família de defeito que esta ilha mais pagou: duas metades contando
a mesma coisa sem nunca se falarem. No dia em que o banco mudar, a promessa do resultado da
busca e a confissão do fim da página mudam **juntas**.

## TRÊS TRAVAS, E DUAS SÃO SILENCIOSAS POR DESENHO

1. Promessa que estoura o teto de **65** devolve a marca — promessa cortada no meio pelo
   Google é pior que promessa nenhuma.
2. Número que não chegou, ou **zero**, recusa o molde **inteiro**. Zero entra na recusa
   porque "0 colas" é uma frase verdadeira que não serve, e no resultado da busca ela custa
   o clique que o bloco existe para ganhar.
3. A bancada reprova quem **declara** promessa e serve título sem dígito.

As duas primeiras **não falham**: elas devolvem a marca e a página continua válida. Trava
silenciosa sem quem a conte é como a promessa desaparece do ar sem ninguém ver — então a
bancada ganhou o mundo **`sem_banco=1`**, que apaga as options de material e faz a trava 2
disparar **na página**, não só na função pura. Bateria nova
`ferramentas/mutacoes-promessa-do-titulo.py`: **19 mutações, 19 reprovadas, 0 passaram.**

## O ACHADO DE BANCADA, E ELE É O MAIOR DESTA EXECUÇÃO

**A bancada servia um `<title>` que nenhuma afirmação media.** Até hoje o
`render-para-teste.php` punha `<title>Clube do Mosaico — teste</title>` em **toda** página —
um rótulo fixo, igual nas dezessete. O bloco de hoje mexe exatamente nessa etiqueta, e régua
que não alcança o que o bloco muda é régua que nasce cega (seção 8). Agora a bancada monta o
título pelo caminho do WordPress: partes, filtro `document_title_parts`, separador. **O
separador não é escolha nossa:** o núcleo junta com `" - "` e o `wptexturize` dele troca o
hífen cercado de espaço por travessão — `&#8211;`, medido no ar hoje. A conta do teto é em
caracteres **decodificados**, a mesma régua da `description`: `&#8211;` conta 1, não 7.

## E A RÉGUA NOVA NASCEU REPROVANDO PÁGINA CERTA

O portão de `<title>` do `conferir-no-ar.py` cobrou o teto de 65 nas **17** e reprovou
**quatro títulos de peça da Loja**, entre 71 e 79 caracteres
(`/loja/quadro-nossa-senhora-aparecida/`, 79, é o maior). Não é defeito: o formato é o que o
despacho do Raphael de **10/09** escreveu, e a primeira observação do despacho de **28/09** já
tinha decidido que *"a régua de 64 é da aquametria e não do contrato"* — recomendação, não
defeito. A régua foi consertada antes de o despacho fechar: o teto é portão nas páginas cujo
título a **casca** monta, e na peça o número é **medido e impresso, nunca reprovado**, no
mesmo desenho do soft 404 de borda. É a quinta vez que esta família aparece no Arquipélago, e
a lição não muda: **portão que não sabe sobre o que decide acusa a coisa errada.**

## O QUE ESTA EXECUÇÃO NÃO PODE FECHAR, E POR QUE ISSO É INFORMAÇÃO

**A leitura semanal de 30/09 não aconteceu.** A ronda diária técnica daquele dia rodou
(14h53Z, nas três ilhas no ar) e fechou sem defeito de página aqui; a estratégica não foi
disparada, e em 01/10 não houve execução nenhuma. A série de `dados/posicoes.md` tem **uma
linha**, a de 23/09.

**E isso não impediu a troca de hoje, por uma razão medida e não conveniente:** a janela
23→30/09 está **fechada e congelada** no Search Console, e nada servido em 02/10 reescreve
aquela semana. A ordem do BLOCO A era não misturar duas causas **dentro** daquela janela.
Fora dela, esperar não protege nada — protelaria a única alavanca medida desta ilha por uma
leitura que a Fundação **não tem como fazer**: a conta `sentinela@` não tem acesso a
`sc-domain:clubedomosaico.com.br`, e o pedido está aberto desde 23/09.

**Então duas coisas foram para `dados/despachos.md`, na lista de ABERTOS:** o acesso da conta
`sentinela@` (que vivia só dentro deste `PROMPT.md` desde 23/09) e o pedido de **ler a janela
de 7 dias que termina em 30/09** — a última semana inteira com o título antigo, e por isso a
única base de comparação limpa que vai existir. A semana 30/09→07/10 já nasce misturada: dois
dias de título velho e cinco de novo. **O veredito continua de 08/10**, como o BLOCO A manda,
e nada aqui declara vitória nem derrota.

## O QUE SOBRA ABERTO NESTA ILHA, em uma linha cada

- **Soft 404 na borda** (item 2 do despacho de 30/09): do hospedeiro, com o Raphael desde
  29/09, medido também na robometria. `leitura-do-visitante.py` fecha REPROVADO por esse
  **único** defeito — vermelho esperado, com dono escrito.
- **A decisão do `tipo_de_casamento: "equivalente"`** para as 13 pastilhas: do Raphael, em
  `dados/despachos.md`, com a medição de 30/09 atrás dela.
- **Os quatro itens que dependem da leitura semanal**: a linha de `/author/` sair de
  `posicoes.md`, o formato `clubedomosaico-f2---` no Relatório de cliques, o CTR da
  `qual-cola` e o primeiro clique orgânico. Nenhum é trabalho de máquina.

## PRÓXIMO PASSO DESBLOQUEADO

Com os despachos de 24/09 e 28/09 fechados e o de 30/09 sem item de Fundação, **a fila volta
a ser fila**: o próximo bloco é de construção, sob o teto da 21.4 (10 URLs por leva, 3 levas
por semana) e com `piso: abaixo` (17 de 40 URLs). A semana está com **zero leva gasta** — a
última URL nova desta ilha é de 14/09. E a 18.5 não bloqueia mais nada: não há defeito de
página no ar.

---

30/09/2026 16:3xZ — OS DOZE DIZIAM COMO A CHAVE FOI MONTADA E CALAVAM O QUE A ESCADA RESPONDEU

Manifest e `/status` na **revisão 53**, conferidos no ar. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudaram: o **BLOCO A** do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09 segue
limpa — o veredito dele é de 08/10 e a troca de título espera a leitura semanal, que
ainda não aconteceu hoje. `conferir-no-ar.py`: **519 afirmações, 0 falha.**

**O bloco desta execução é o item 1 do DESPACHO DA SENTINELA de 30/09**, e pela 18.1
ele é o único item da ilha que não depende da leitura semanal: o BLOCO A espera 30/09,
o item 4 (metade) do despacho de 28/09 espera o BLOCO A, e os quatro itens do despacho
de 23/09 esperam a leitura. **Nada foi construído, por 18.5: verificação antes de
construção.**

## O QUE O DESPACHO PEDIA, E POR QUE NÃO ERA ZELO DE ARQUIVO

Dos 38 registros do banco, **17 estão no degrau 4** — servem a página de busca, que é
o piso da 25.2. Cinco escreviam por que pararam ali; **doze traziam só
`motivo_da_chave`**, texto como `"familia: medida"`, que conta como a chave foi
MONTADA e não o que a escada de palavra-chave devolveu. Os dois estados eram a mesma
tela, e a 25.4-b.4 diz o preço disso: "não casou" tem causas que parecem uma — produto
que ninguém anuncia (só o mercado resolve) ou candidato barrado por trava (resolve-se
com trava melhor ou com um registro de variante que falta) — e **contadas juntas viram
um número que não diz o que fazer.**

## O QUE FOI MEDIDO, E A FERRAMENTA QUE NÃO PODIA SER O COLETOR

`ferramentas/medir-degrau-4.py` desceu a escada **inteira** pela Open API (25.6) para
os dezessete, com a regra de casamento de `casar-anuncio.py` **importada, nunca
copiada**. Ela não para no primeiro degrau que casa, ao contrário do coletor: quem mede
quer a escada toda, senão o motivo fala de um degrau e cala os outros três.

**Ela não grava `url` em nenhuma hipótese, e é isso que a deixa medir as 13 pastilhas.**
O `coletar-shopee.py` as exclui por `FORA = ('dados/materiais-pastilhas.json',)`, e com
razão: subir o degrau delas dependeria de `afiliado.tipo_de_casamento: "equivalente"`,
que é decisão do Raphael. **Mas medir não é agir** — e foi por confundir os dois que
elas ficaram de 13/09 a 30/09 carregando a frase *"elas nem foram tentadas"*, que é
exatamente a família de defeito que a 25.4-b.3 nomeia: motivo que diz "nem tentamos"
manda a execução seguinte não tentar, e fica assim por quanto tempo ninguém olhar.
**Dezessete dias, aqui.**

## A REPARTIÇÃO, QUE É O QUE O DESPACHO PEDIA — E ELA NÃO É A DA 25.4-b.4

| causa medida | quantos | de quem é a dívida |
|---|---|---|
| `marca-nao-anunciada` | **13** | do Raphael. Nenhuma oferta da escada traz a marca: degraus 1 e 2 (marca + código, marca + nome comercial) devolvem **zero** e os largos devolvem catálogo de outras marcas. Pede a decisão do casamento por atributo, não trava melhor |
| `candidato-barrado-nome` | **2** | nossa. `quartzolit-protetor-para-fachadas` e `cortag-torques-azulejista-corte-curvo` |
| `candidato-barrado-variante` | **2** | nossa. `quartzolit-fundo-selador` e `cascola-pl500-adesivo-de-montagem` |

**A 25.4-b.4 previa duas causas e a medição achou três**, e a terceira é a que mais
importa: `marca-nao-anunciada` não é "produto não anunciado" (a Shopee **tem** o
produto Glass Mosaic, anunciado como CG10/CG21/CG33) nem "candidato barrado por trava
que se pode melhorar" — é **pedido de decisão**. Somada a qualquer das outras duas, o
pedido ao Raphael desaparece dentro de uma dívida técnica que não é dele. Por isso o
relatório do validador imprime a repartição, e não só o total.

**E a medição confirmou, por máquina, o diagnóstico que estava escrito à mão em 29/09**
em `dados/links-afiliado-pendentes.md` — os três da Quartzolit e o da Cortag caíram como
dívida de nome ou de variante, nenhum como produto inexistente. Aquela tabela tinha sido
escrita lendo ensaio com o olho; hoje a classificação saiu do laudo da regra, sem
ninguém olhar, e caiu nos mesmos lugares.

## O ERRO DESTA EXECUÇÃO, ESCRITO PORQUE VALE MAIS QUE O ITEM

A **primeira versão do classificador** decidia a causa pela trava que barrou o
candidato, e o ensaio das 17 devolveu **17 de 17 na mesma classe** — precisamente o
número que não diz nada de que o despacho reclamava. A causa do erro: em
`casar.compativel` as cinco travas correm **em ordem** e a primeira que falha encerra o
julgamento, e a trava 5b (o título tem de trazer o `nome_comercial` inteiro) quase
sempre falha antes de qualquer trava de irmão ser avaliada. **"Nenhuma trava de irmão
foi acionada" media a ordem do código, não o mundo.**

O conserto foi trocar a pergunta: o que separa as causas é a **trava 1** — algum
anúncio da escada traz a marca deste registro? Zero oferta em toda a escada é
`nao-anunciado`; oferta sem a marca é `marca-nao-anunciada`; oferta **com** a marca é
dívida nossa, e aí a trava que barrou diz se é de nome ou de variante. **Régua que mede
a ordem em que o portão pergunta nunca reprova o portão.**

E uma segunda honestidade, na hora de batizar as classes: a primeira versão chamava uma
delas de `candidato-barrado-batismo`, afirmando que o nosso `nome_comercial` é que
estava errado. Para a Quartzolit é verdade (seção 26), para o torques da Cortag **não**
— lá o `nome_comercial` está certo e os anúncios são de corte RETO. A trava 5b não
distingue as duas leituras, então o rótulo passou a ser `candidato-barrado-nome` e o
campo diz, com todas as letras, que quem consertar tem de abrir o anúncio.

## O PORTÃO, E ELE COBRA A FORMA E NUNCA O TEXTO

`validar-banco.py` reprova registro no degrau 4 sem ficha cujo `motivo_sem_ficha` não
esteja na forma da 25.4-b.3: `CAUSA (<classe>): ... || ULTIMA TENTATIVA <AAAA-MM-DD>:
...`. A causa não se reescreve; a tentativa, sim, a cada passada. O relatório passou a
imprimir **`degrau 4 com motivo escrito: 17 de 17`** — que é o critério de pronto que o
despacho declarou — e a repartição por classe abaixo dele.

**Bateria nova:** `ferramentas/mutacoes-motivo-degrau-4.py`, **10 mutações, 10
reprovadas, as 10 só pelo portão novo** (desligado por
`CDM_SEM_PORTAO_MOTIVO_DEGRAU_4=1`). Atacam uma metade da forma por vez: o campo
ausente, a prosa de uma metade só que era a forma de 29/09 e passava, a causa sem
classe, a classe escrita em prosa com maiúscula (duas grafias da mesma causa viram duas
causas e a repartição soma errado **sem reprovar**), a tentativa sem data, a data em
formato brasileiro — legível e não ordenável — e a causa vazia dentro da forma certa.
Duas **produzem o mundo** que o banco não tem: ficha achada com link não encurtado, e
item que **cai** do degrau 3 de volta para o 4 quando o anúncio sai do ar. As duas
recontam `itens_esperando_link` do cabeçalho, porque sem isso era o portão do CABEÇALHO
que as pegava — e **mutação pega pelo portão errado não prova portão nenhum**: era
assim que as duas apareciam como "outro portão já pegava" na primeira rodada.

`dados/esquema-banco.json` foi para a **v9**, declarando a forma, as quatro classes,
quem escreve e quem cobra.

## BANCADAS, TODAS VERDES

`validar-banco` · `validar-pastilhas` · `mutacoes-degrau` 8/8 · `mutacoes-casamento`
17/17 · `teste-casamento` 42 · `mutacoes-pastilhas` 14/14 · `teste-casca` 591 ·
`teste-f1` 24 estados · `teste-f2` 119 · `teste-loja` · `teste-atelie` · `teste-leads` ·
`teste-tecnicas` 123 · `conferir-cobertura` 353 · `conferir-no-ar` **519 afirmações, 0
falha**. `leitura-do-visitante` continua **REPROVADO pelo soft 404 da borda**, que é do
hospedeiro, está com o Raphael desde 29/09 e hoje também foi medido na robometria.

## O PRÓXIMO PASSO DESBLOQUEADO

**Nada da Fundação, até a leitura semanal de 30/09 acontecer.** Os quatro itens que
restam nesta ilha dependem todos dela, e é uma dependência escrita, não uma escolha:

1. **BLOCO A** (Raphael, 24/09) — título e meta das três páginas de primeira página.
   Espera a leitura de 30/09 por ordem do próprio despacho; o retrato "antes" já está
   gravado em `dados/posicoes.md` desde 29/09.
2. **Item 4 (metade) do despacho de 28/09** — a faixa de 120 a 160 nas quatro
   `description` acima de 160. Espera o BLOCO A, porque é a outra metade da mesma
   promessa de SERP.
3. **Itens 1 e 2 e Propostas 1 e 3 do despacho de 23/09** — os quatro só fecham com
   número da leitura semanal: a saída de `/author/` de `dados/posicoes.md`, o formato
   `clubedomosaico-f2---` no Relatório de cliques, o CTR de `qual-cola` e o primeiro
   clique orgânico.
4. **Item 2 do despacho de 30/09** — o soft 404 da borda. É do hospedeiro e não se
   conserta daqui.

**E um pedido novo ao Raphael, que esta execução não inventou e sim mediu:** a decisão
do `tipo_de_casamento: "equivalente"` para as 13 pastilhas deixou de ser uma frase
antiga e passou a ser uma linha de banco com medição de hoje atrás dela. São 13 dos 17
itens do degrau 4 — a maior fatia da dívida de conversão desta ilha — e o caminho pelo
código está **medido como fechado**, não apenas inexplorado.


29/09/2026 19:16Z — O BATISMO DO FABRICANTE JÁ ESTAVA NO REPOSITÓRIO, E O EGRESSO NÃO ERA O QUE TRAVAVA

Manifest e `/status` na **revisão 50**, conferidos no ar. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudaram: o BLOCO A do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09 segue
limpa. O que mudou foi o **banco** — e, desta vez, um campo do banco que ninguém
tinha lido.

**A escada da 25.1 saiu de `1:1 · 2:5 · 3:14 · 4:18` para `1:1 · 2:5 · 3:15 · 4:17`**,
e a página de divulgação passou de *"Em 20 o botão é a ficha do produto e em 18 é a
busca"* para **21 e 17**, sem ninguém digitar número: ela conta dos registros.

## ESTE BLOCO CONTRADIZ O QUE A EXECUÇÃO ANTERIOR ESCREVEU, E A CORREÇÃO VALE MAIS QUE O ITEM

O `REGISTRO.md` das 16h17Z de hoje fechou dizendo, sobre os três registros da
Quartzolit presos no degrau 4:

> *"TRÊS são da Quartzolit e o defeito NÃO é do link: é do BANCO. (...) Consertar é
> COLETA, na página do fabricante, e esbarra no mesmo egresso do item 3 acima:
> `quartzolit.weber` em 403, na lista do Raphael."*

**Não esbarra.** O batismo do fabricante estava dentro do próprio registro desde
25/09, em `fontes[].url`: o endereço do boletim técnico, cujo **nome de arquivo** é o
fabricante escrevendo o nome do produto.

```
BT_Borracha Líquida Elástica Quartzolit_REV110624.pdf
```

O registro chamava-se *"impermeabilizante borracha liquida elastica quartzolit"*. A
palavra `impermeabilizante` **não está no boletim**: ela veio do **caminho** da página
de produto — `/impermeabilizantes-quartzolit/impermeabilizantes-para-paredes-externas-e-fachadas/`
—, que é a **prateleira** do fabricante, não o nome do produto. A ilha colou a
classificação dentro do batismo, que é a seção 26 exatamente ao contrário.

**O egresso continua fechado e continua travando `base` e `apoio`.** Este item não era
dele, e quatro execuções seguidas anotaram "esbarra no egresso" sem abrir a fonte que
já estava em casa. Vale como aviso mais do que como conserto: *bloqueio herdado de um
documento é retestado antes de ser respeitado* (seção 20.2) — e isso vale para o
bloqueio herdado do `REGISTRO.md` tanto quanto para o do `ESTADO.md`.

## A REGRA JÁ ERA DO BANCO; O QUE FALTAVA ERA ALGUÉM APLICÁ-LA A ESTE CAMPO

`escada_de_fontes`, do `dados/esquema-banco.json`, diz desde o bloco 3: *"em conflito,
o nível mais alto vence e o outro fica registrado em `divergencias[]`"*. O registro
citava **duas** fontes do mesmo fabricante — boletim técnico (nível 2) e página de
produto (nível 3) — e elas **discordam sobre o nome**. O banco já mandava o nível 2
vencer. Nenhum portão media isso para `nome_comercial`, porque até hoje de manhã nada
comparava esse campo com um texto de fora: `casar-anuncio.py` foi o primeiro, e o que
ele achou foi um campo do próprio banco escrito no papel errado.

A divergência ficou **gravada** no registro, com as duas declarações, os dois níveis e
a resolução escrita — não foi corrigida em silêncio.

## DUAS RÉGUAS MAIS LARGAS FORAM MEDIDAS E DESCARTADAS ANTES DESTA

Isto é o que evita que a trava nasça grande e morra ignorada:

1. *"o batismo tem de caber na URL da melhor fonte"* — reprova **20 dos 38**, e quase
   todos são honestos: página de produto de fabricante tem endereço genérico, e
   `Verniz Acrilico Brilhante` não está no dele.
2. *"o batismo não começa com a palavra que a ilha usa para classificar"* — reprova
   **20 dos 38**, entre eles `Verniz Acrilico Brilhante` (tipo `verniz`) e
   `Rejunte Cerâmicas Quartzolit` (categoria `rejunte`). O fabricante batiza pelo tipo
   o tempo todo.

A terceira, a que ficou, mede **7 registros** — os que citam PDF de fabricante — e
reprova **1**, com **zero falso positivo**. Trava larga que a próxima execução aprende
a ignorar não é trava.

## A COMPARAÇÃO TEM DE SABER QUE O SERVIDOR DO FABRICANTE MUTILA O NOME DO ARQUIVO

Duas mutilações, as duas medidas neste banco: ele **apaga a letra acentuada inteira**
(`Boletim_Tcnico` por "Técnico", `rejunte_epxi_quartzolit.pdf` por "Rejunte Epóxi") e
**cola as palavras** (`RejuntePorcelanatoseCeramicas`). Uma comparação ingênua
reprovaria `Rejunte Epóxi Quartzolit` e `Rejunte Porcelanatos e Cerâmicas Quartzolit`,
que são batismos **certos**. E a **marca** fica fora da cobrança: ela mora no campo
dela, e o fabricante nem sempre a repete no nome do arquivo.

## A BATERIA OBRIGOU A BANCADA A FABRICAR DUAS BORDAS — DE NOVO, E PELO MESMO MOTIVO

A primeira rodada deu **7 de 10** na regra: duas mutações passaram com a bancada verde,
e as duas atacavam travas que **nenhum registro de hoje exercita**.

- **A palavra vazia.** Cobrar `de` num batismo cujo arquivo não o traz reprovaria um
  nome certo — mas o `para` de *"Verniz Protetor para Pisos"* está escrito no próprio
  arquivo, então a trava nunca era exercitada. A bancada passou a fabricar o par.
- **O separador.** O fabricante pode partir no arquivo o que o batismo escreve junto
  (`AC2` virando `AC_2`); nenhum arquivo deste banco faz isso hoje.

**Bancada que só mede o banco de hoje envelhece junto com ele** — a mesma frase do
bloco das 16h17Z, e a segunda vez em um dia que a bateria a cobra.

## O QUE MEDE ISSO

- `ferramentas/batismo-do-fabricante.py` — a regra sozinha, sem rede e sem gravação,
  pelo mesmo motivo de `casar-anuncio.py`: quem a usa e quem a ataca precisam da mesma
  função.
- `ferramentas/teste-batismo.py` — **59 afirmações, 0 falha**, sobre os registros reais
  em **cópia** (bancada que escreve no banco para se provar estraga o que mede).
- `ferramentas/mutacoes-batismo.py` — **14 de 14 reprovadas**: 10 na regra (duas delas
  **apertando** a régua, porque folga deliberada que ninguém mede alguém aperta por
  zelo na leitura seguinte) e 4 no esquema/banco, entre elas a que a **26.2** exige por
  escrito — apagar a chave da lista.
- `validar-banco.py` ganhou a linha `batismos conferidos .... 7`.
- Esquema na **versão 8**, com `batismo_do_fabricante`. A lista de quais fontes batizam
  mora **no esquema**, nunca dentro da régua (26.2).

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

**`quartzolit-fundo-selador` e `quartzolit-protetor-para-fachadas` continuam em
minúsculas**, e agora com o motivo escrito no registro: a única fonte deles é a página
de produto, e o batismo chega pelo **slug** do endereço, que soletra as palavras e
**perde a tipografia**. Capitalizar dali seria palpite sobre como o fabricante escreve
— palpite com cara de declaração do fabricante é o que a seção 26 existe para impedir.
Os dois ficam fora do escopo da trava, com o motivo no laudo, não aprovados em silêncio.

**E os outros três do degrau 4 continuam onde estavam**, cada um com o dono que a
execução anterior já tinha nomeado certo: as **treze pastilhas** dependem de
`tipo_de_casamento: "equivalente"` e são do Raphael; a **torquês de corte curvo da
Cortag** foi remedida com quatro chaves novas nesta execução e **a Shopee não anuncia
esse produto** — as chaves de "corte curvo" devolvem a torquês de **mosaico**, que já é
outro registro do banco, e casar as duas seria a armadilha 5 da 25.7; o **Cascola
PL500** continua caindo na trava do nome comercial inteiro, e afrouxá-la para ele
passar é critério dobrado para caber no dado (1.2-b.4).

## O QUE APARECE NA TELA, E O QUE NÃO APARECE

A prova servida é a frase da página de divulgação: **21 e 17**. O nome corrigido em si
**não aparece em página nenhuma hoje** — os sete materiais de acabamento estão no
banco e `/materiais/` lista a categoria como *"Em breve"*, porque a ficha de categoria
é o bloco **4c** e ele não nasceu. Dizer que o conserto "foi ao ar" sem essa ressalva
seria contar meia verdade.

## NO AR, E UMA FALHA QUE NÃO ERA DA ILHA

`conferir-no-ar.py` **519 afirmações, 0 falha**; `conferir-tecnica-no-ar.py` **54 e 0**;
`conferir-atelie-no-ar.py` **197 e 0**. O soft 404 da borda continua reprovando a leitura
do visitante por **1** defeito — é do hospedeiro, está pendente com o Raphael e não mudou.
O desembarque aplicou **na primeira chamada** (revisão 50, 14 aplicados).

O ateliê chegou a fechar vermelho, e o vermelho era meu: **`conferir-atelie-no-ar.py` toma
o TOKEN como primeiro argumento**, e todas as outras ferramentas desta ilha tomam a raiz
(`conferir-no-ar.py .`). Chamei com `.` por hábito, o ponto foi para a rota protegida, e o
401 que voltou era a rota **recusando corretamente** uma palavra errada. Custou uma
passada de diagnóstico. Virou trava em vez de nota: a ferramenta agora **recusa um
argumento que seja caminho** em vez de transformá-lo em credencial, e diz como se chama.
Nada do site foi tocado.

- **Próximo passo desbloqueado:** continua sendo a leitura de **30/09**, que libera o
  **BLOCO A** (CTR das três páginas de primeira página, veredito em 08/10) e, com ele, a
  metade que falta do item 4 da Sentinela de 28/09. O que **não** depende dela: (a) o
  egresso de fabricante, que trava `base` e `apoio` e está na lista do Raphael — e que
  este bloco confirma ser o travamento **de verdade** daquelas duas, não uma herança de
  documento; (b) a decisão de `tipo_de_casamento: "equivalente"` das treze pastilhas,
  que é do Raphael; (c) **a ficha de categoria de acabamento (bloco 4c)**, que é o que
  daria página ao que este bloco corrigiu — e que, pela 21.4, é leva de malha e deve
  esperar a leitura de 30/09 fechar a janela de medição.

---

29/09/2026 16:17Z — DEZ MATERIAIS SAEM DO PISO DA 25.2 E GANHAM FICHA DE PRODUTO, COM A PROVA DO CASAMENTO GRAVADA E RECONFERIDA POR PORTÃO

Manifest e `/status` na **revisão 49**, conferidos no ar. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudaram: o BLOCO A do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09 segue
limpa. O que mudou foi o **banco**, e o que o banco mudou apareceu na tela.

**A escada da 25.1 saiu de `1:1 · 2:5 · 3:4 · 4:28` para `1:1 · 2:5 · 3:14 · 4:18`.**
Vinte dos trinta e oito materiais servem agora a FICHA do produto; dezoito servem o
piso da 25.2, a página de busca. E a página de divulgação, que conta isso ao leitor,
passou de *"Em 10 o botão é a ficha do produto e em 28 é a busca"* para **20 e 18**,
sem ninguém digitar número nenhum — ela conta dos registros.

## POR QUE ISTO NÃO TINHA SIDO FEITO ANTES, E A RESPOSTA ESTAVA ESCRITA NO PRÓPRIO BANCO

O cabeçalho de `materiais-acabamento.json` dizia, desde 25/09, com todas as letras:
*"Nenhum tem ficha de produto (`url` vazio): ficha exige casamento de item, que a
25.7 proíbe sem prova de que o anúncio é daquele SKU."* O de `materiais-alicates.json`
dizia o mesmo em outras palavras. **Não era preguiça nem esquecimento: era uma
recusa correta.** A 25.7 é explícita — *casamento errado no banco é pior que
casamento nenhum, porque parece dado* — e escolher um anúncio pelo olho, item a
item, é exatamente a mão humana sem portão que fez os dezesseis `sub_id` nascerem
deslocados em 13/09.

**O que faltava não era trabalho: era o portão.** Este bloco construiu o portão, e
só então usou.

## A REGRA, E ELA MORA SOZINHA NUM ARQUIVO PARA PODER SER ATACADA

`ferramentas/casar-anuncio.py` não fala com a rede e não grava nada. É só a regra —
separada de propósito, porque quem a **usa** (`coletar-shopee.py`) e quem a **ataca**
(`mutacoes-casamento.py`) precisam da mesma função. Regra copiada em dois lugares é
regra que a bateria mede num lugar e o banco usa no outro.

São **seis travas mais a unicidade**, e todas as sete têm de passar:

1. **A marca aparece no título.** Sem ela, `verniz acrílico brilhante` é o catálogo
   de meio Brasil.
2. **A cabeça do título é o produto** — as quatro primeiras palavras trazem algo do
   nome comercial. É a armadilha 1 da 25.7 traduzida para este nicho: *"Kit 3
   Pincéis para aplicar Verniz Acrilex Brilhante"* tem o verniz no meio e um pincel
   na cabeça, e quem compra leva pincel.
3. **O título separa o registro de cada irmão** (outro registro da mesma marca).
4. **O título NÃO traz o que é do irmão**, quando o irmão é do mesmo tipo.
5. **Nenhuma palavra de armadilha** — `kit`, `combo`, `usado`, `apostila`. A lista
   **não** tem `manual`, e isso é medição e não esquecimento: três registros deste
   banco são *"Cortador de cerâmicas e azulejos MANUAL"*.
6. **O título traz o nome comercial inteiro.**

E por cima delas, a **unicidade**: o anúncio casa quando UM registro passa. Dois
passando é a armadilha 5 da 25.7 — no máximo um está certo e não há como dizer
qual, então os dois caem.

## A TRAVA 6 NASCEU NO ENSAIO, E ELA É A QUE VALE A LEITURA

O primeiro ensaio casou **13 de 15** e um dos treze estava **errado**:
`quartzolit-fundo-selador` casou com *"Selador PU30 Cinza Quartzolit 600g"*, que é
um selante de poliuretano e não o fundo selador acrílico de parede.

As cinco travas não viram nada, e o motivo é mecânico: elas comparam o registro com
os **irmãos**, e nenhum irmão da Quartzolit disputa a palavra `selador`. **Token que
nenhum irmão tem nunca era exigido de ninguém** — a palavra `fundo`, que é o produto
inteiro, era a única coisa que separava o certo do errado e era exatamente a que
ninguém cobrava. O buraco não era do irmão: era de não cobrar do título o nome que o
fabricante deu ao produto.

A trava 6 custou **três casamentos** — caiu de 13 para 10. É o lado certo de errar, e
está escrito para poder ser discordado.

## O QUE O ENSAIO MEDIU, COPIADO DA SHOPEE E NÃO IMAGINADO

A chave `verniz acrilico brilhante acrilex` devolveu oito anúncios. **Dois**
identificam um registro só. Os outros seis são o catálogo da armadilha 5:

    Verniz para Couro Acrilex 100ml Fosco Semibrilho Brilhante     <- fosco E brilhante
    Verniz Acrilico Acrilex 100ml / 250ml / 500ml (Fosco ou Brilhante)
    Verniz Acrilex Acrilfix Fosco, SemiBrilho ou Brilhante Spray
    Verniz Vitral Acrilex 100ml Incolor Brilhante Madreperola     <- outro produto

O terceiro é o que obrigou a trava 4 a existir na forma que tem. Ele traz `acrilfix`
e `brilhante`, e o banco **não tem** um `acrilfix fosco` para disputá-lo — então uma
regra que só exigisse os tokens do registro o aprovaria. **Quem escreve "Fosco,
SemiBrilho ou Brilhante" está vendendo a escolha, e a escolha não é um SKU.** Por
isso a regra proíbe o título de trazer o que é do irmão, e não só exige o que é dele.

## OS CINCO QUE NÃO SUBIRAM, E O ACHADO QUE VALE MAIS QUE OS DEZ LINKS

| registro | o que segurou |
|---|---|
| `quartzolit-borracha-liquida-elastica` | o `nome_comercial` é uma descrição, não o batismo do fabricante |
| `quartzolit-protetor-para-fachadas` | idem |
| `quartzolit-fundo-selador` | idem — e aqui a trava 6 **evitou** o casamento errado |
| `cortag-torques-azulejista-corte-curvo` | as chaves devolvem o anúncio de corte **reto**; sem a palavra `curvo` o título não separa os dois irmãos |
| `cascola-pl500-adesivo-de-montagem` | uma letra de gênero: o anúncio é *"Cola **Adesiva** Montagem Cascola Monta E Fixa Interior Pl500"* e o registro diz *"**Adesivo** de Montagem"* |

**Três dos cinco são da Quartzolit e têm o mesmo defeito, e ele não é da regra: é do
banco.** `impermeabilizante borracha liquida elastica quartzolit`, `protetor para
fachadas`, `fundo selador quartzolit` — minúsculas, com a marca repetida dentro, e
uma frase que **nós** escrevemos para descrever o produto. A seção 26 do contrato diz
que *o vocabulário da ilha classifica pela função e o fabricante batiza pela posição*,
e `nome_comercial` é o lado do FABRICANTE.

Nenhum portão via isso porque, até hoje, **nada comparava esse campo com um texto de
fora**. A regra de casamento foi a primeira a comparar — e o que ela achou não foi um
anúncio: foi um campo do próprio banco escrito no papel errado. Consertar os três é
coleta na página do fabricante, e o egresso a `quartzolit.weber` continua em 403.

**E o Cascola não foi consertado de propósito.** Afrouxar a trava para aceitar
`adesiva` onde o registro diz `adesivo` faria a régua passar por causa deste item, que
é critério dobrado para caber no dado que veio — a 1.2-b.4 nomeia isso. Fica o motivo
escrito em `afiliado.motivo_sem_ficha`, com as chaves tentadas e quantas ofertas cada
uma devolveu, para a próxima execução saber se vale retentar.

**As treze pastilhas não foram tentadas.** Elas dependem da decisão de
`afiliado.tipo_de_casamento: "equivalente"` descrita em `dados/links-afiliado-pendentes.md`,
e ela é do Raphael. A regra não as alcança e não deveria: a Shopee não anuncia a
codificação da Glass Mosaic.

## A ESCADA DE PALAVRA-CHAVE DESTA ILHA NÃO É A DA 25.6 AO PÉ DA LETRA, E ISSO ESTÁ ESCRITO

A 25.6 nasceu na Robometria, onde o degrau 1 é *"o código do fabricante sozinho"* —
e lá funciona porque `ERB10` é digitado no título pelo vendedor de reposição. Aqui os
códigos são `61341`, `68.51.050.000`, `REV110624`, `BRSA005`: **SKU interno de
catálogo industrial**, que nenhum vendedor de Shopee escreve. Código sozinho aqui casa
com o mundo, que é a armadilha 3 da 25.7. A escada desta ilha é marca + código, depois
marca + nome comercial, depois a chave de hoje, depois marca + os dois primeiros
tokens. **O degrau em que cada um casou fica gravado**, porque casar pelo código e
casar pela chave larga não valem o mesmo — e um deles casou pelo código: a torquês de
mosaico da Cortag, com `61341` no título do anúncio.

## O DEGRAU DA 25.1 NUNCA FOI CHUTADO PARA CIMA

Todos os dez entraram no **degrau 3**, anúncio de vendedor comum. Nenhum virou degrau
1, e a régua é dupla: o nome da loja tem de trazer a marca do fabricante **e** uma
palavra de loja oficial. `arteciaoficial` tem "oficial" e **não** é a Acrilex —
revendedor que se chama oficial é revendedor. Errar para baixo custa uma ressalva mais
dura na tela; errar para cima faz a metodologia declarar um rigor que a ilha não tem.

## DEZ FOTOS, E É A PRIMEIRA VEZ QUE ESTE BANCO GANHA IMAGEM SEM O FABRICANTE

O egresso a `acrilex.com.br`, `cortag.com`, `vonder.com.br` e `quartzolit.weber`
continua fechado, e continua na lista do Raphael. O que mudou é que agora existe um
anúncio **provadamente** daquele produto, e a foto dele é legítima. Largura e altura
saíram dos primeiros bytes do arquivo servido, por `ferramentas/medir-imagens.py`, que
já existia e **não foi reescrito** — a API não devolve dimensão, e caixa de foto sem
medida é o salto de layout da 22.4. Foto que não pôde ser medida não entra. Itens sem
imagem caíram de 35 para 25.

## O PORTÃO DO OUTRO LADO: A PROVA SE RECONFERE, NÃO SE ACREDITA

A prova ficou gravada em `afiliado.casamento`, com o título do anúncio que a produziu.
**Título gravado que ninguém reconfere é decoração, não procedência.** Então
`validar-banco.py` ganhou um portão que não lê o campo: ele passa o título gravado pela
regra **viva** de `casar-anuncio.py`, contra o banco inteiro, e reprova quando ela deixa
de identificar aquele registro. No dia em que alguém afrouxar a regra, renomear um
registro ou acrescentar um irmão que o título também descreve, o casamento para de valer
e o validador acusa. É a seção 4 do contrato aplicada ao banco: o resumo não pode
sobreviver ao fato.

O esquema foi para a **versão 7**, com `casamento` e `motivo_sem_ficha` escritos — e a
ausência de `casamento` nos cinco registros de 13/09 é declarada como **história, não
defeito**: a ficha deles veio por outro caminho, antes de a regra existir.

## AS DUAS BORDAS QUE A BATERIA OBRIGOU A BANCADA A FABRICAR

A primeira rodada de `mutacoes-casamento.py` deu **10 de 12**: duas mutações passaram
com a bancada verde, e as duas são travas que **nenhum registro do banco de hoje
exercita**.

- **A metade positiva da trava 3** só é a única a salvar quando o nome comercial de um
  registro cabe inteiro no do irmão e o único separador dos dois é o código. Isso não
  existe neste banco; existe no dia em que um fabricante lançar a versão "Spray" do que
  já vende. A bancada passou a fabricar esse par, e a mutação reprova.
- **A unicidade** só morde no **lote**: um anúncio que vende dois produtos de marcas
  diferentes não são irmãos um do outro, então as travas 3 e 4 não se olham. E o lote
  tem de começar pela palavra que os dois dividem, senão nem chega lá — a primeira
  versão desse título juntava a torquês da Cortag com o cortador da Vonder, e a **trava
  2 sozinha** já derrubava a Vonder, porque a cabeça do título era a torquês. Dois
  **vernizes** de marcas diferentes é o caso real.

**Bateria que só mede o banco de hoje envelhece junto com ele.**

## BANCADA E BATERIA

`ferramentas/teste-casamento.py`: **42 afirmações**, todas sobre títulos **reais**
devolvidos pela Open API em 29/09/2026, copiados byte a byte — com acento, com caixa
errada, com espaço duplo e com uma quebra de linha no meio de um deles, que é como o
vendedor escreveu. Título inventado mede a regra contra a imaginação de quem a escreveu.

`ferramentas/mutacoes-casamento.py`: **17 mutações em duas metades, 17 de 17
reprovadas**. Doze atacam a regra — cada trava cai uma vez, e **uma delas APERTA em vez
de afrouxar**, pondo `manual` nas armadilhas, porque régua que reprova o certo custa
tanto quanto régua que aprova o errado. Cinco atacam o **banco** e medem o portão novo
do validador: o título vira o do irmão, fica vazio, a ficha some, um campo de
procedência some, e — a que mais importa — **o banco muda e a prova caduca sem ninguém
tocar no campo**. As cinco reprovaram pelo portão do casamento, nenhuma por outro.

## O QUE NÃO FOI CLICADO, E POR QUÊ

Nenhum link desta ilha foi aberto. A 25.8 é explícita: o salto do encurtador é onde a
Shopee **conta** o clique, e autoclique com a etiqueta `clubedomosaico` apaga
justamente o primeiro clique orgânico que a leitura de 30/09 vai procurar. A prova de
vida de cada anúncio é a API tê-lo devolvido nesta passada, e está escrita assim, com
essas palavras, dentro de cada `casamento`.

## DE PASSAGEM, UM ALARME FALSO QUE VALE SER REGISTRADO

`conferir-atelie-no-ar.py` fechou com **1 falha** numa passada — *"com token a rota
responde 401"* — e a falha era da chamada, não do site: a ferramenta lê `argv[1]` como
**token**, e ela foi chamada com `.`, que é o argumento que quase todas as outras desta
ilha recebem como caminho. Chamada sem argumento ela fecha em **184 afirmações, 0 falha,
3 puladas**, exatamente como em 28/09. Fica escrito porque um 401 lido como defeito faria
a execução seguinte caçar um bug que não existe.

## BANCADAS E O AR

Casca **591**, F2 119, F1 200, Loja 208, Técnicas 123, Ateliê 289, Leads 211, Prestação
5 — zero falha. Validador do banco verde, com a linha nova **casamentos reconferidos:
10**. `validar-pastilhas.py` verde. `teste-casamento.py` 42 e 0.
**No ar: `conferir-no-ar.py` com 519 afirmações e 0 falha**, `conferir-tecnica-no-ar.py`
com 54 e 0, `conferir-atelie-no-ar.py` com 184 e 0. O soft 404 da borda continua
REPROVANDO a leitura do visitante por **1** defeito — é do hospedeiro, está pendente com
o Raphael e não mudou.

**O desembarque levou duas tentativas e isso é registro, não defeito:** a primeira
chamada do Sync leu a **revisão 48** com o `raw` do GitHub já servindo a **49** — cache
de borda do próprio GitHub, não do WordPress, que anexa `?v=time()` em toda leitura. A
segunda, dois minutos depois, aplicou. **Commit sem Sync não é entrega, e Sync que
responde não é entrega: o que é entrega é o número na tela.** Quem provou foi a página
de divulgação dizendo 20 e 18.

- **Próximo passo desbloqueado:** continua sendo a leitura de **30/09**, que libera o
  **BLOCO A** (CTR das três páginas de primeira página, veredito em 08/10) e, com ele, a
  metade que falta do item 4 da Sentinela de 28/09 — as duas são a mesma promessa de SERP
  nas mesmas páginas. O que **não** depende dela: (a) o egresso de fabricante, que trava
  `base` e `apoio` e está na lista do Raphael; (b) a decisão de
  `tipo_de_casamento: "equivalente"` das **treze pastilhas**, que é a maior fatia dos 18
  que restam no degrau 4 e é dele; (c) **os três `nome_comercial` da Quartzolit escritos
  como descrição em vez do batismo do fabricante** — item novo, achado por este bloco, que
  é coleta e não decisão, e que hoje esbarra no mesmo egresso de (a).

---

29/09/2026 13:17Z — A PÁGINA DE DIVULGAÇÃO DIZIA AO LEITOR QUE 28 BOTÕES NÃO RENDIAM COMISSÃO, E OS 28 SAEM COM `rel="sponsored"`

Casca **1.18.0**, manifest e `/status` na **revisão 48**. Nenhuma URL nova, nenhum
endereço mudou, nenhum `<title>` e nenhuma `description` mudou — o BLOCO A do
despacho do Raphael de 24/09 continua intocado e a janela de medição de 30/09
segue limpa. O que mudou é o TEXTO de uma página que não rankeia e cujo produto
inteiro é dizer a verdade sobre dinheiro.

## O DEFEITO, E ELE ESTAVA NO AR HÁ QUATRO DIAS

`/divulgacao-de-afiliados/` servia, hoje de manhã, esta frase:

> *"Quando ainda não existe [link de afiliado para o produto], o botão leva você
> para a **busca daquele produto na loja**, e essa busca **não é link de
> afiliado**: ninguém nos paga por aquele clique."*

**É falso para 28 dos 38 materiais do banco.** O `url_busca` desses 28 é um
encurtador `s.shopee.com.br/...` com `sub_id_1 = clubedomosaico` — link de
afiliado, que rende comissão. O validador mede `piso nao rastreavel = 0` desde
25/09, e `conferir-no-ar.py` contou hoje **29 encurtadores servidos** nas 17
URLs, **todos com `rel="sponsored"`**.

**A DIREÇÃO DO ERRO É O QUE O TORNA GRAVE, e ela é a rara.** O defeito comum de
site de afiliado é esconder do buscador a relação paga. Aqui era o contrário: a
ilha **declarava** a relação paga ao Google, no atributo, e a **negava** a quem
lê, no texto — na única página do site cujo produto inteiro é a divulgação.

## NINGUÉM MENTIU: A FRASE ENVELHECEU SOZINHA, E ISSO TEM DATA

- **14/09/2026** — a busca CRUA subiu para o botão (f2 1.5.0, degrau 4 da 25.1).
  A frase nasceu nesse dia e **era verdadeira**: busca crua leva à mesma loja e
  não paga nada. Escrevê-la foi zelo, não descuido.
- **16/09/2026** — a Open API de afiliados entrou (25.6 do contrato). Encurtar
  deixou de exigir o painel do Raphael e virou uma chamada de rede.
- **25/09/2026** — o BLOCO 0 regerou os links pela API e **os 38 itens ganharam
  busca encurtada**. A frase ficou falsa nesse instante, e ninguém a tocou.

É a seção 4 do contrato na forma mais pura — o texto fica para trás em silêncio
—, com o agravante de que o texto era uma **afirmação sobre dinheiro**.

## E A CONTA EMBAIXO TINHA DUAS PARCELAS DE TRÊS

A mesma página publicava: *"os **38** materiais do banco têm, todos, um caminho
de compra. Em **10** deles esse caminho é um link de afiliado (…); em **0** ele é
a busca na loja, que não rende nada."*

**10 + 0 = 10, de 38.** Os 28 do meio — a busca encurtada — não apareciam em
parcela nenhuma, e **nenhum dígito estava visivelmente errado**. É assim que uma
classificação inteira some de uma página sem nenhum número parecer falso: a
conta tinha duas parcelas porque o mundo tinha dois estados em 14/09, e ganhou o
terceiro sem ninguém recontar as parcelas.

## POR QUE NENHUM PORTÃO VIA, E É ESTRUTURAL

O texto mora na **casca** e o `rel` mora na **F2**. Nenhuma régua comparava os
dois — e o docbloco da própria `cdm_f2_compra_html()` já dizia, desde 14/09, que
*"a busca ENCURTADA (…) é link de afiliado e rende comissão"*. **O código sabia
e a página não.** Duas verdades em dois snippets, sem nada entre elas.

## O QUE FOI CONSTRUÍDO

**A página** passa a nomear os **três** estados do botão, dizendo quais dois são
afiliado: ficha do produto (afiliado), busca daquele produto (afiliado, e a
palavra "também" está lá de propósito) e busca sem rastreio (não afiliado, e é o
único botão do site sem a marca de patrocinado). A conta passa a ter **três
parcelas que fecham no total**.

**E ela só sai pela via viva.** O instantâneo de `cdm_casca_numeros()` é de 14/09
e ainda declara `piso_nao_rastreavel => 15` num banco que tem zero; publicá-lo
hoje repetiria o defeito que esta versão conserta. Quando os cinco bancos não
chegaram, a seção fica com a **regra** — que é o que o leitor tem direito de
saber — e sem a contagem. **Estatística velha envelhece; disclosure velho mente**,
e essa é a distinção que justificou não seguir a convenção de "não mexer no
instantâneo" com um `if` em vez de um dígito.

**O portão (teste-casca, seção 15c) não guarda a resposta: ele pergunta ao
código.** Para cada um dos três estados, monta o `afiliado` à mão, chama
`cdm_f2_compra_html()`, lê se o `rel` emitido é `sponsored`, acha o `<li>`
correspondente na página pelo marcador do próprio texto e exige que as duas
classificações **batam**. No dia em que a escada mudar de novo, quem falha é o
par — não o lado que alguém lembrou de atualizar.

**A régua no ar** (`conferir-no-ar.py`) mede a mesma coisa no HTML servido: a
frase aposentada ausente, as três parcelas com os números **recontados dos
registros** (nunca dos cabeçalhos que a tela lê), e o `rel` de **cada** link de
loja das 17 URLs — 29 encurtadores, 29 patrocinados, 0 busca crua se dizendo
patrocinada.

## A MUTAÇÃO QUE PASSOU, E ELA VALE MAIS QUE AS SETE QUE REPROVARAM

`ferramentas/mutacoes-divulgacao.py`, oito mutações. Na primeira rodada **uma
passou**: *"a parcela da busca troca de fonte"* — trocar
`esperando_link - piso_nao_rastreavel` por `esperando_link` sozinho. Com
`piso_nao_rastreavel` em **0** os dois dão o mesmo número, e a trava **nasceu
inerte**: ela mediria o acaso de hoje, não a regra. O defeito que essa mutação
escreve só aparece no dia em que um item perder o rastreio — que é exatamente o
dia em que a página voltaria a contar como pago um clique que não paga.

A bancada passou a **fabricar esse dia** (regra 2 da seção 8: a grade inclui a
borda): um item de alicate perde a busca encurtada, e a conta tem de sair
10 · 27 · 1. Com a borda, **8 de 8 reprovaram**.

## DE PASSAGEM, UM MARCADOR DE PURGA QUE O PRÓPRIO BLOCO INVALIDOU

O portão de cache da seção 12 compara origem e canônico por **marcadores** de
texto, e o marcador de `/divulgacao-de-afiliados/` era o título antigo da seção.
Trocar o título derrubou o portão na primeira passada — e ele reprovou **como
devia**: marcador é o texto que só existe depois da revisão nova, então ele muda
junto com o bloco ou para de medir purga. Atualizado no mesmo commit.

## BANCADAS E O AR

Casca **591** afirmações (eram 587; as novas são o portão do par, as três
parcelas e a borda), F2 119, Técnicas 123, F1, Loja, Ateliê, Leads e Prestação
verdes, validador do banco verde. `mutacoes-divulgacao.py` 8 de 8 reprovadas.
**No ar: `conferir-no-ar.py` com 519 afirmações e 0 falha** (eram 508).
`leitura-do-visitante.py` continua REPROVADO por **1** defeito, o mesmo de hoje
de manhã — o soft 404 da borda, que é do hospedeiro e está pendente com o
Raphael. A borda já serve o texto novo: lida **sem** quebra de cache, a página
traz o título novo e as três parcelas.

- **Próximo passo desbloqueado:** continua sendo a leitura de **30/09**, que
  libera o **BLOCO A** (CTR das três páginas de primeira página, veredito em
  08/10) e, com ele, a metade que falta do item 4 da Sentinela de 28/09 — as duas
  são a mesma promessa de SERP nas mesmas páginas. O que **não** depende dela
  continua sendo o egresso de fabricante, que trava `base` e `apoio` e está na
  lista do Raphael. **E entra um item novo de valor comercial, que não depende
  de nenhum dos dois:** 28 dos 38 materiais estão no degrau 4 da 25.1 (busca, que
  converte pior que ficha) — entre eles as **13 pastilhas**, que são a vitrine da
  F1. Subir degrau é trabalho de API da Shopee, que esta nuvem alcança; o que
  falta nas pastilhas é a decisão de `afiliado.tipo_de_casamento: "equivalente"`
  descrita em `dados/links-afiliado-pendentes.md`, e ela é do Raphael.

---

29/09/2026 11:12Z — A LEITURA DO VISITANTE, E ELA ACHOU UM DEFEITO NO AR NA PRIMEIRA VEZ QUE OLHOU

Bloco de instrumento, escolhido por eliminação e com a eliminação escrita: hoje é
**29/09**, véspera da leitura, e o BLOCO A do despacho do Raphael de 24/09 proíbe
mexer na promessa de SERP das páginas que rankeiam até 30/09. A metade aberta do
item 4 da Sentinela de 28/09 espera o BLOCO A pela 18.1; os itens 1 e 2 de 23/09
têm a última condição na leitura de amanhã; e `base` e `apoio` esperam **canal**,
não decisão — o que foi **remedido** nesta execução, e continua fechado: o egresso a
`quartzolit.weber`, `tekbond`, `loctite`, `cascola` e `pastilhart` devolve **403 ao
CONNECT** (política de egresso), cinco domínios, cinco tentativas, com o domínio da
ilha em 200 na mesma passada. **Quarto bloco seguido parando nessa porta**, e agora
com o pedido escrito, que é o que faltava (ver "O que depende do Raphael").

**NENHUM ARQUIVO PUBLICÁVEL MUDOU, e por isso não houve Sync.** Manifest e `/status`
seguem na **revisão 47**. Nenhuma URL nova, nenhum endereço mudou, nenhum `<title>`,
nenhuma `description` e nenhum texto de página mudou. O ar está exatamente como
estava — que é a condição que o despacho do Raphael impõe a esta véspera.

## O ACHADO, E ELE NÃO ESTAVA ESCONDIDO: ESTAVA ESCRITO AQUI HÁ QUATRO DIAS

O BLOCO C, em 25/09, mediu e escreveu, com todas as letras:

> *"`conferir-no-ar.py` gruda `?v=<agora>` em toda URL — e está certo, porque nasceu
> para provar que o Sync aplicou a revisão nova. O preço é que **ele nunca vê o que o
> visitante vê**. Cache servindo página velha para gente de verdade passa por baixo
> das 488 afirmações dele sem encostar em nenhuma."*

Ficou **quatro dias sem instrumento**. Esta execução construiu o instrumento e, na
primeira passada, ele achou um defeito que está no ar agora.

## O DEFEITO, MEDIDO E REPETIDO ANTES DE VIRAR AFIRMAÇÃO (20.2)

**Toda URL que não existe nesta ilha responde 404 na primeira leitura e 200 na
segunda**, por duas horas.

| leitura | resposta |
|---|---|
| 1ª (cache sem a entrada) | **404**, `cache-control: no-cache, must-revalidate, max-age=0, no-store, private` — a **origem**, e ela está **certa** |
| 2ª em diante, por 2h | **200**, `x-proxy-cache: HIT`, `x-server-cache: true`, `max-age=7200`, corpo = a página de **404 desta ilha** |

**Como foi provado que é mecanismo e não coincidência:** uma URL **virgem**, com o
relógio no nome, nunca lida por ninguém — 1ª **404**, 2ª **200**, 3ª **200**. E as
três URLs inexistentes lidas uma vez minutos antes, todas 404 na primeira, davam
**200** na segunda. Mais cinco leituras seguidas de uma delas: 200, 200, 200, 200,
200. Com quebra de cache, na mesma janela: 404, 404, 404.

**É SOFT 404.** 200 com corpo de erro faz o Google contar a URL como existente. Quem
lê uma URL duas vezes é exatamente o Googlebot, e o orçamento de rastreamento é o
recurso escasso da 14.1 — esta ilha tem **15 URLs ainda não indexadas**. É a mesma
família, e a mesma causa, do outro achado do BLOCO C: *"o rastreador nunca recebe
redirecionamento"*. A camada de cache responde antes do WordPress.

**POR QUE NENHUM PORTÃO DAQUI VIA.** As 504 afirmações do `conferir-no-ar.py` passam
por `buscar()`, e `buscar()` gruda a quebra de cache. **Todas mediam a origem.** A
afirmação `[rota] caminho inexistente responde 404` passa, e está **certa**: a origem
responde 404. O defeito mora na camada da frente, e até hoje nada daqui a lia.

## O QUE FOI CONSTRUÍDO

`ferramentas/leitura-do-visitante.py` — lê as **17 URLs do sitemap sem quebra de
cache**, que é a leitura que se parece com a do Google, e termina na sonda de 404
pela borda.

- **A régua é função pura** e tem `--autoteste` com **11 casos fabricados, um por
  ramo** (11 de 11, zero falha). A varredura fechou em 17 esperado e zero defeito nas
  URLs, e esta ilha já escreveu em 25/09 que *"passada limpa em portão que nunca
  acusou nada não prova nada"*.
- **A sonda leva sufixo novo a cada passada**, e isso não é detalhe: com URL fixa ela
  mediria a entrada de cache que a **passada anterior** criou, e acusaria a si mesma
  para sempre.
- **O visitante é lido PRIMEIRO**, antes da origem: a quebra de cache aquece a borda,
  e medi-la depois de aquecer mediria o instrumento, não o site.
- O `conferir-no-ar.py` **importa** essa régua em vez de copiá-la — uma terceira
  reimplementação de "o visitante recebeu a ilha" não acrescentaria independência, só
  uma cópia para envelhecer calada (é o mesmo motivo escrito em `cobertura.py`). Foi
  de **504 para 508 afirmações, 0 falha**.

## AS DUAS POLÍTICAS, E NENHUMA DELAS É NOVA

**A ferramenta REPROVA** — fecha em `REPROVADO: 18 URL(s) lidas, 1 defeito(s)`, e é
para ficar vermelha até a pendência fechar. **O portão de entrega REGISTRA**, com o
número, a data e o dono na linha. A jurisprudência é desta ilha, de 14/09, e está
escrita no próprio `conferir-no-ar.py`: portão vermelho que nenhuma execução consegue
fechar *"se aprende a ignorar, que é pior do que não ter portão"*. **No dia em que o
Raphael fechar, a linha vira portão** trocando `ok(True` por `ok(_borda_404_ok` — e
isso está escrito no arquivo, ao lado da linha, não só aqui.

**O que impediu a outra saída fácil, e vale registrar:** a primeira tentação era fazer
a afirmação reprovar de qualquer jeito, "para não deixar passar". Isso travaria toda
execução futura desta ilha num vermelho que nenhuma delas pode consertar — o cache é
do hospedeiro, roda antes do PHP, e a origem já manda `no-store`, que ele ignora.

## O RETRATO "ANTES" DO BLOCO A, QUE ERA O ÚNICO PEDAÇO DELE QUE NÃO ESPERAVA

O BLOCO A manda, textualmente: *"Gravar em `dados/posicoes.md` o título e a meta ANTES
da troca, na mesma linha da série, para haver com o que comparar depois."* Estava por
fazer, e **depois da troca não teria como ser remontado** — o HTML servido não guarda
o que servia ontem. Gravado, **medido pela borda** (a leitura do Google), com contagem
em caracteres decodificados:

| URL | `<title>` | nº | `description` | nº |
|---|---|---|---|---|
| `/materiais/qual-cola-usar-no-mosaico/` | Qual cola usar no mosaico, e qual rejunte – Clube do Mosaico | 60 | … pela declaração do próprio fabricante … | 183 |
| `/materiais/quantas-pastilhas-para-mosaico/` | Quantas pastilhas e quanto rejunte comprar – Clube do Mosaico | 61 | … a conta da pastilha pequena e não a do azulejo de obra | 165 |
| `/como-fazer/o-que-e-mosaico-picassiete/` | O que é mosaico Picassiete, e como colar – Clube do Mosaico | 59 | … com o que colar o caquinho em cada superfície … | 192 |
| `/como-fazer/o-que-e-trencadis/` | O que é trencadís, e com o que colar o caco – Clube do Mosaico | 62 | … de onde vem o nome ligado a Gaudí … | 189 |

**O que o retrato já diz para quem escrever o BLOCO A depois de 30/09:** nenhum dos
quatro `<title>` promete um número, e nenhuma das quatro `description` promete a
faixa — as duas alavancas que a 12.1 nomeia para a banda de 4 a 10 estão **inteiras
por usar**. E os quatro títulos cabem em 64 com folga de **2 a 5 caracteres**: quem
for enfiar um número ali vai ter de tirar palavra, e a candidata é a marca no fim,
que foi o caminho do precedente da robometria.

## MEDIDO NESTA EXECUÇÃO

- `conferir-no-ar.py`: **508 afirmações, 0 falha** (eram 504).
- `leitura-do-visitante.py --autoteste`: **11 de 11**, 0 falha.
- `leitura-do-visitante.py`: 17 URLs esperado, **0 janela de cache aberta**, **1
  defeito** — a sonda de 404.
- `teste-casca.php` **569**, `teste-loja.php` **208**, `validar-banco.py` OK,
  `varrer-canonicas.py --autoteste` **11 de 11**. Zero falha.
- Cabeçalho do `ESTADO.md` em `yaml.safe_load`: **ok**.
- Rede da ilha pela 20.2 no começo da execução: `/` **200**, `wp-sitemap.xml` **200**,
  `/wp-json/clubedomosaico/v1/status` **revisão 47**.

## O QUE DEPENDE DO RAPHAEL — três coisas, e duas já estavam abertas

1. **NOVA: o soft 404 da borda.** No cPanel da HostGator, cache de página que não
   guarde resposta 404. Está no `ESTADO.md` e em `dados/consertos.md`, com o comando
   que reconfere.
2. **O egresso aos domínios de fabricante** (20.1 e 20.3), e é o que destrava o
   primeiro SKU de `base` e de `apoio` — **quarto bloco seguido parando aqui**.
   `quartzolit.weber`, `tekbond.com.br`, `loctite.com.br`, `cascola.com.br` e
   `pastilhart.com.br` respondem **403 ao CONNECT**. O caminho está na 20.1:
   `claude.ai/code` → seletor de ambiente → Nuvem → engrenagem → Domínios permitidos.
   **Sem PDF de fabricante não sai FISPQ de epóxi nem `dureza_shore_a`**, e as duas
   categorias já têm regra, portão e bateria verde esperando só a frase.
3. **O acesso da conta `sentinela@` ao Search Console** desta propriedade, que
   continua aberto desde o BLOCO C e é o que tira a nota de rodapé da leitura de
   30/09.

## PRÓXIMO PASSO

**A leitura de 30/09 é amanhã**, e ela destrava de uma vez o BLOCO A (agora com o
retrato "antes" já gravado, que era pré-requisito dele), a faixa de `description` das
quatro travadas, a terceira condição do item 1 de 23/09 e a segunda metade do item 2.
O que sobra antes disso continua sendo **canal**, não decisão.

**Memória:** `/areas` e `/topics` não existem neste ambiente — conferido, como em
execuções anteriores. O estado está no `ESTADO.md`, neste registro e no `PROMPT.md`.

28/09/2026 19:42Z — A LINHA DA PEÇA ENTRA NA ÁRVORE, E O QUE FALTAVA NÃO ERA A LINHA: ERA A CHAVE

Item 4 da lista de desbloqueados do `PROMPT.md` ("a linha da peça na tabela do
`ARVORE.md` — é conserto de TESTE, não de documento"). Casca **1.17.0**, Loja
**1.4.0**, manifest na revisão **47**.

**Por que este item e não outro:** hoje é 28/09 e **todo** o resto da fila desta
ilha espera 30/09. O BLOCO A do despacho do Raphael de 24/09 espera a leitura de
30/09 por ordem escrita dele; a metade aberta do item 4 do despacho da Sentinela
de 28/09 (a faixa de 120 a 160 nas quatro páginas que já tinham `description`)
espera o BLOCO A pela 18.1; os itens 1 e 2 do despacho de 23/09 têm a última
condição na leitura de 30/09; e as duas categorias vazias que sobram (`base` e
`apoio`) já têm decisão de campo e portão — o que falta nelas é **canal**, não
decisão: frase literal de fabricante que esta nuvem consiga citar, e o egresso
de PDF continua fechado. Este item não toca em nenhuma das páginas que estão na
primeira página do Google, não cria URL nova e não mexe em `<title>` nem em
`description` de nada — então é o único que podia sair hoje sem misturar causa
na janela de medição que o Raphael mandou preservar.

**A DECISÃO QUE O `ARVORE.md` DEIXOU ESCRITA PARA A FUNDAÇÃO (19.2), E QUAL FOI.**
A seção 5 daquele arquivo tinha duas opções defensáveis: ou o filtro da Loja
passa a chavear por `CDM_LOJA_BASE . '/' . $slug`, ou a tabela declara a exceção
e o portão passa a admiti-la. **Escolhida a primeira**, e o que decidiu não foi
gosto: foi um **segundo defeito** que só existe com o slug nu e que a segunda
opção não consertaria.

**O SEGUNDO DEFEITO, MEDIDO NA BANCADA ANTES DE QUALQUER CONSERTO:** peça cujo
slug bate com o de uma página da raiz servia a trilha **daquela página**. Peça
chamada `sobre` saía com `Início › Sobre` — sem o nome da peça na trilha — e o
`BreadcrumbList` levava a URL de `/sobre/`. O mesmo com `privacidade` e
`contato`. A causa é a ordem: `cdm_casca_slug_atual()` remonta o caminho pela
definição de PÁGINAS, casando por último nível, e a peça é tipo próprio. Com o
caminho inteiro a colisão deixa de existir **por construção** — `loja/sobre` não
é `sobre`. Uma exceção documentada continuaria sendo uma exceção no código.

**O CONSERTO, E ELE TEM DUAS PONTAS E UMA FUNÇÃO SÓ.** `cdm_loja_caminho_da_peca()`
monta o caminho, e dela saem as duas declarações: a chave do filtro `cdm_arvore`
(onde a peça mora) e a resposta do filtro novo `cdm_caminho_atual` da casca (qual
página está sendo servida). As duas pontas montando a própria string são a
**origem** do defeito, não o conserto dele: se uma mudasse de formato e a outra
não, a trilha da peça sumiria da tela sem cor nenhuma. O `teste-loja.php` cobra
que só **um** lugar do snippet monte o caminho, e que as duas declarações passem
pela função.

**A PRIMEIRA ESCRITA DO CONSERTO ERROU, E O ERRO ESTÁ AQUI PORQUE A MUTAÇÃO DELE
FICOU:** o filtro nasceu **depois** do laço da definição de páginas. O caso comum
ficou verde na hora — `loja/vaso-azul-com-flores` — e a colisão continuou de pé
inteira, porque o laço casava `sobre` e retornava antes de o filtro ser chamado.
Medido, não deduzido: a régua de colisão reprovou. O filtro passou a falar
**antes**, e a mutação `o filtro do caminho fala DEPOIS do laco das paginas`
existe para ninguém reverter isso sem ver.

**O PORTÃO TEM TRÊS PERNAS, E NENHUMA SOBRA** (item 21 do `teste-casca.php`):

| perna | o que cobra | o que ela impede |
|---|---|---|
| documento → código | a linha da tabela existe no mapa, **com a peça servida** | a divergência silenciosa de sempre |
| documento → realidade | o slug da linha está em `dados/pecas.json` | portão vazio: a bancada fabrica a peça com o slug que a tabela pedir, então linha inventada passaria |
| realidade → código | **todas** as 5 peças da cópia pousam em `loja/<slug>`, nível 2, mãe `loja` | a tabela com uma linha virar álibi para as outras quatro |

**O número de peças não foi digitado no documento**, e isso é decisão: quem
publica peça é a artesã, no dia que ela quiser, e tabela escrita pela Fundação
que precise de commit a cada peça nova nasce velha. A tabela nomeia a **âncora**
(`/loja/quadro-flores-do-campo/`, a primeira que ela publicou, em 14/09) e o
portão conta o resto contra a cópia da seção 24. Hoje são cinco, e as cinco são
medidas.

**E a decisão declarada no filtro continua de pé, com portão próprio:** fora de
uma requisição de peça, `/loja/` **não** tem filha no mapa. Sem essa afirmação o
conserto preguiçoso — declarar todas as peças sempre — passaria, e encheria a
lista de irmãs de `/loja/` de peça, que é outra decisão e não é a de hoje.

**UMA MUTAÇÃO PRÉ-EXISTENTE ESTAVA INERTE, E O ACHADO É DO MESMO DIA.**
`dois slugs com o mesmo ultimo nivel` casava com a entrada `'sobre'` escrita em
UMA linha da definição de páginas; a casca **1.16.0**, de algumas horas antes
nesta mesma quarta, quebrou a entrada em várias linhas quando a `description`
ganhou dono. A mutação parou de achar o alvo e passou a se declarar INVÁLIDA — e
a bancada conta inválida como "passou", então a trava dos slugs repetidos ficou
**sem ninguém a vendo**, justamente a trava que sustenta a premissa do caminho
remontado. Conferido que já estava inerte **antes** deste bloco. O alvo agora é a
**abertura** da entrada, que não depende de quantos campos ela tem. É a mesma
cicatriz que `m_pagina_de_prova_deixa_de_ser_citada` registra em comentário desde
12/09, e ela voltou.

**As baterias.** `ferramentas/mutacoes-arvore.py` foi de 21 para **29 mutações,
29 reprovadas, 0 passaram** — as oito novas: o slug nu de volta, uma ponta só
mudando de formato, o filtro falando depois do laço, a tabela nomeando peça que
não existe, mãe divergente na linha da peça, a linha sumindo da tabela, toda peça
entrando servida ou não, e só a peça da tabela sendo atendida.

**Bancadas:** `teste-casca` 569 (eram 563), `teste-loja` 208 (eram 196), e
`leads`, `atelie`, `f1`, `f2`, `tecnicas`, `prestacao-rejunte` sem falha.

**O DESEMBARQUE, e a régua que ele exigiu.** Revisão **47** no ar às 19h48Z, 14 aplicados; `/status`
na 47 e a rota pública da loja servindo `versao_loja: 1.4.0`. **E o `conferir-no-ar.py` não media a
trilha — nenhuma linha dele falava dela**, o que para este bloco seria conferir tudo menos o que
mudou. Entraram três afirmações, medidas no HTML servido das 5 peças: a trilha existe (a chave nova
não a apagou), ela é `Início › Loja › <nome da peça>` com o degrau atual sem link e com
`aria-current`, e o `BreadcrumbList` sobe por `/loja/` com a numeração sem buraco. **5 de 5 nas
três.** O total foi de 501 para **504 afirmações, 0 falha**.

*(O Sync leu a revisão 46 em três disparos seguidos antes de pegar a 47: é o cache de borda do
`raw.githubusercontent.com`, que serviu 47 para esta nuvem e 46 para o servidor do site por alguns
minutos. Repetido até passar, como a 20.2 manda — não é bloqueio, e fica registrado porque a próxima
execução que vir "revisão anterior" logo depois de empurrar vai querer saber que isso é esperado.)*

**Uma afirmação que escrevi e apaguei no mesmo bloco, registrada porque o erro é
da família que esta ilha mais paga:** a primeira versão da régua de colisão do
`teste-loja.php` terminava em `|| true`. Ela passava sempre e não media nada —
portão que nunca pode reprovar. Foi trocada pela medição real: a página `/sobre/`
de verdade continua respondendo `sobre`, que é o outro lado da borda e o que
impede o conserto de ter mandado toda página singular para baixo de `/loja/`.

- **Nenhuma URL nova, nenhuma URL mudou de endereço, nenhum texto de página
  mudou.** O que muda no ar é a chave interna do mapa e a trilha das peças em
  caso de colisão de slug — que hoje não acontece em nenhuma das cinco.
- Próximo passo: **a leitura de 30/09** destrava, de uma vez, o BLOCO A do
  despacho do Raphael de 24/09, a faixa de `description` das quatro páginas
  travadas, a terceira condição do item 1 de 23/09 (`/author/` sair de
  `dados/posicoes.md`) e a segunda metade do item 2 (o formato
  `clubedomosaico-f2---` no Relatório de cliques). Antes disso, o que sobra na
  fila é **canal**, não decisão: `base` e `apoio` esperam frase literal de
  fabricante, e é o terceiro bloco seguido parando na mesma porta (PDF).

10/09/2026 — pasta da ilha criada pelas mãos, a pedido da sessão de conversa

- Criada a pasta `ilhas/clubedomosaico/` com `snippets/`, `conteudo/`,
  `dados/`, `identidade/logo/`, `manifest.json` (revisao 0, nenhum item, nada
  marcado para publicar), `README.md`, `PROMPT.md`, `ESTADO.md` e este
  registro.
- `snippets/clubedomosaico-sync.php` gerado a partir de
  `ilhas/robometria/snippets/robometria-sync.php`, sem outra alteracao alem da
  troca de nome da ilha. Passou em `php -l`.
  sha256: `0b893702fd4614928adeddabdf51465f7214304798640041c6a277f2fcfd0649`
- Proximo passo: bloco 1 — corpus de buscas em `dados/corpus-buscas.md`. Nao
  depende de site nem de WordPress.

10/09/2026 15:21Z — BLOCO 1 ENTREGUE: corpus de buscas

- `dados/corpus-buscas.md` criado com os tres clusters da ilha
  (materiais/ferramentas, pecas prontas, aprender), a SERP classificada
  consulta a consulta em aberta/tomada/armadilha pela regra da secao 14.9, e a
  ordem da fila derivada do cruzamento intencao de compra x chance de primeira
  pagina. Manifest na revisao 1; `publicar: false`, entao **nao houve Sync
  nesta execucao** — a secao 4 do contrato so exige acionar o Sync em bloco que
  mexe em conteudo publicavel, e este nao mexeu.
  sha256: `5580e5fa9084b4c06da3bb26e8e2088936b9cffbb65ca60f1b4de243f14db695`
- Procedencia separada em duas coletas, e assim escrita no arquivo: a faixa de
  volume veio do Planejador na conta do Raphael (10/09, via `PROMPT.md`, nao
  refeita aqui); a SERP foi coletada nesta execucao por busca web da nuvem, com
  os ocupantes do top 10 nomeados. **CPC nao foi coletado e esta declarado como
  ausente, nunca estimado** — a fila do bloco 1 pedia CPC e ele nao existe sem
  o painel autenticado.
- Tres achados medidos que mudam o desenho das ferramentas:
  (1) toda a SERP de rejunte responde a pergunta de OBRA (0,2-0,4 kg/m2, azulejo
  grande) e portanto esta ERRADA para peca de artesanato com pastilha de 1x1 cm
  — a F1 nao compete com essas paginas, responde outra coisa;
  (2) a regra cola x base ja circula em blog, mas sem fabricante, codigo, data
  nem separacao interno/externo/molhado — abre a F2 e ao mesmo tempo proibe usar
  a SERP como fonte dela;
  (3) as lojas vendem pastilha em tres unidades diferentes (100 pecas, 100 g,
  placa 30x30 com 225), entao converter peca <-> grama <-> placa e numero
  proprio da ilha.
- Tomadas, e por isso FORA da fila: `curso de mosaico` (top 10 sao escolas reais
  com professora e turma; a ilha nao vende curso), `presente artesanal` (Elo7) e
  `vaso centro de mesa` (Leroy). `mosaico bizantino` entrou como alvo: faixa
  1k-100k com a primeira pagina em portugues ocupada por resultado em espanhol.
- Concorrente nomeado para a leitura semanal acompanhar: `mosaico.arq.br`, que
  vende peca artesanal e curso — o mais parecido com esta ilha inteira.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente).
  O estado vive no `ESTADO.md` desta pasta, como manda o `PROMPT.md`.
- Proximo passo desbloqueado: **bloco 2** — `dados/especificacao-calculadoras.md`
  e `dados/constantes.json`, comecando pela F2 (seletor de cola e rejunte), que
  o corpus mostrou ser a de maior intencao e menor concorrencia. Constante so
  com fonte de fabricante e data (Quartzolit, Tekbond, Loctite, Cascola); sem
  fonte, `pendente` e fora de formula publicada. Nao depende de site.

10/09/2026 19:30Z — BLOCO 2 ENTREGUE: especificacao das duas ferramentas + constantes

- `dados/constantes.json` (11 constantes de fabricante, 6 pendencias nomeadas) e
  `dados/especificacao-calculadoras.md` (contrato de construcao da F1 e da F2). Manifest na
  revisao 2; os dois com `publicar: false`, entao **nao houve Sync nesta execucao** — a
  secao 4 do contrato so exige Sync em bloco que mexe em conteudo publicavel.
  sha256 constantes: `99c6c5cb7130fc0428bb15312226c74ced0b51fa79cc95c3ca4de7f45dca1e39`
  sha256 especificacao: `1189ad6f0fc3e21ed046acc7d2215e0c947f267b1557b07b1c87a05edb58fa7a`
- **Procedencia, e o limite dela, declarados item a item.** A coleta foi por busca web
  restrita ao dominio de cada fabricante (quartzolit.weber, tekbond.com.br, cascola.com.br,
  henkel.com.br). `curl` e `WebFetch` para esses dominios voltaram `EGRESS_BLOCKED` /
  `connect_rejected` — a rede das rotinas libera os dominios das ilhas, `*.googleapis.com` e
  `github.com` —, entao os PDFs de boletim tecnico **nao foram abertos linha a linha**. Cada
  constante diz isso em `fonte_tipo` e marca `conferir_no_pdf`. **Nada de blog, loja ou
  agregador entrou**: o bloco 1 tinha medido que a regra cola x base circula na SERP sem
  fabricante, codigo nem data, e a fila proibiu usar a SERP como fonte da F2.
- **O achado que decide a F2:** a ficha BRSA004 do Silicone Acetico Construcao Tekbond
  (revisada em 10/2025) lista espelho, concreto, cimento, tijolo, calcario, superficie
  alcalina, superficie pintada ou porosa, acrilico, aquario, metal corrosivel e imersao
  continua entre as superficies em que o produto NAO deve ser usado — que sao exatamente os
  casos em que o mosaico artesanal brasileiro usa silicone acetico por indicacao de blog.
  Isso torna a elegibilidade da secao 7 **mecanica**: basta uma restricao bater com a entrada
  para o produto sair dos recomendados e ir para a secao rotulada, com a frase do fabricante
  e a data. E o par acetico/neutro sendo do mesmo fabricante, a F2 diz "nao use A, use B" sem
  sair de uma fonte so.
- **O achado que decide a F1:** aplicando a formula publicada pela propria Quartzolit
  (`((A+B) x E x L x CR)/(A x B)`, CR 1,75 no exemplo do fabricante) ao tamanho real da
  pastilha de artesanato, pastilha de 1x1 cm com 4 mm de espessura e junta de 2 mm consome
  **2,80 kg/m2** de rejunte — 7 a 14 vezes os 0,2-0,4 kg/m2 que a primeira pagina do Google
  publica com azulejo de obra. A tabela pre-renderizada de 12 pecas tipicas ja esta calculada
  no arquivo. Segundo numero proprio: a placa 30x30 com 225 pastilhas tem passo 30/raiz(225)
  = 2,00 cm, ou seja, **nao e pastilha de 1x1 cm** — e o erro de quem compara preco entre
  loja que vende por peca e loja que vende por placa.
- **O que NAO foi publicado, de proposito.** A espessura da pastilha virou campo de entrada,
  nao constante, porque nenhum fabricante de pastilha de artesanato a padroniza. A coluna de
  gramas de cola da F1 nasce vazia com explicacao na tela: falta o consumo em kg/m2 da
  cimentcola e o rendimento do silicone por area (o fabricante declara por cordao), e as duas
  estao em `pendentes`. A F2 declara duas faixas DESCOBERTAS — peca em contato permanente com
  agua e base de plastico — em vez de preencher no chute. A conversao grama <-> peca fica
  pendente por SKU, para o banco MATERIAL do bloco 3 coletar com data.
- A especificacao ja carrega o bloco de compra obrigatorio ANTES da prova de procedencia,
  pela cicatriz da Robometria de 10/09: nenhuma das duas ferramentas vai ao ar sem ele, mesmo
  com `afiliado.url` vazio, e a ilha reporta quantos itens esperam link.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como no
  bloco 1. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 3** — modelo do banco (MATERIAL, PECA, TECNICA). A
  especificacao ja nomeou os campos que as duas ferramentas exigem de MATERIAL: categoria
  cola (com a lista de restricoes declaradas por produto), rejunte (com faixa de junta) e
  pastilha (com lado, espessura e unidade de venda). Nao depende de site. Depois dele, o
  bloco 4 fica dependendo so do WordPress existir.

10/09/2026 23:16Z — BLOCO 3 ENTREGUE: modelo do banco + categoria COLA + verificador

- `dados/esquema-banco.json` (modelo das entidades MATERIAL, PECA, TECNICA e da serie
  temporal COTACAO), `dados/materiais-colas.json` (5 registros da categoria cola) e
  `ferramentas/validar-banco.py`. Manifest na revisao 3; tudo com `publicar: false`, entao
  **nao houve Sync nesta execucao** — a secao 4 do contrato so exige Sync em bloco que mexe
  em conteudo publicavel, e a ilha ainda nao tem WordPress.
  sha256 esquema: `862f84b64ed9005ab00dc2c97335e470c1c44d63b63d025e51e93be77e50ed33`
  sha256 colas:   `0df9a40da7343f2a96675aaf4c9b0bc8506fed008fc6781afa6f37b9d62a090d`
  sha256 validador: `ac3f1f6001ea405f26303b3ecf6a82092329926701070ee686eb61909db27f3a`
- **NENHUM dado novo foi coletado, e isso e proposital.** Os 5 registros de cola sao a
  transposicao campo a campo do que o bloco 2 ja tinha colhido em `dados/constantes.json`,
  com a mesma fonte, o mesmo tipo de documento e a mesma data. O que o bloco acrescenta e
  ESTRUTURA: a lista literal do fabricante virou campo COM PESO — indicado, proibido, nao
  recomendado, delimita ambiente, resiste a ambiente — e por isso a matriz da F2 passou a ser
  RECOMPUTADA em vez de lida.
- **O verificador nao e enfeite.** Ele recomputou as 18 celulas base x ambiente pelas cinco
  regras de elegibilidade e bateu com a tabela publicada no esquema. Tres mutacoes provaram
  que ele falha quando deve: apagar `espelhos` da lista de restricoes da ficha BRSA004
  (2 erros, o acetico deixa de ser eliminado no espelho), promover o press release do
  Durepoxi de nivel 4 para 3 (20 erros, ele invade os recomendados de 8 celulas) e criar
  `dados/pecas.json` (1 erro: PECA nao vive no repositorio).
- **QUATRO ACHADOS que corrigem a matriz que o bloco 2 tinha escrito a mao**, e por isso a
  secao 1.3 da especificacao ganhou uma nota dizendo que quem manda agora e o esquema:
  (1) **a cimentcola AC-II nao tem declaracao de SUBSTRATO** — a especificacao a recomendava
  para base de cimento citando que ela e declarada para "area interna e externa", que e
  AMBIENTE; as unicas superficies nomeadas na coleta ("ceramicas e placas de pedra natural de
  ate 120 x 120 cm") sao a PECA ASSENTADA. Ela sai dos recomendados de todas as celulas, e
  quem responde base de cimento e o silicone neutro, que declara concreto e alvenaria com
  todas as letras;
  (2) **ceramica e vidro em ambiente comum sao EMPATE** entre acetico e neutro — o mesmo
  fabricante declara ceramica para os dois e nenhum declara o ambiente —, entao a pagina
  lista os dois em vez de fingir uma preferencia que a fonte nao sustenta;
  (3) **em sol e chuva o acetico nao fica "em segundo lugar", fica FORA**: ambiente de
  exposicao continuada exige declaracao explicita, e so o neutro declara chuva e raios UV;
  (4) **MDF molhado e externo TEM resposta** — o neutro declara madeira entre os substratos
  que veda —, ao contrario do "a ilha nao recomenda" da especificacao, que so tinha olhado
  PVA e acetico. O PVA sai desses ambientes por DELIMITACAO do proprio fabricante
  ("ambientes internos"), nunca por proibicao inventada.
- **O que o esquema tem de proprio desta ilha**, e que nao foi copiado de Aquametria nem de
  Robometria: o campo que decide a recomendacao e NEGATIVO (a lista de restricoes vale mais
  que a de indicacoes); existem TRES estados de declaracao e nao dois, porque silencio nao e
  proibicao e foi o Cascorez que obrigou isso; a escada de fontes tem um nivel 4 criado para
  material de imprensa, que e o que mantem a peca submersa como faixa DESCOBERTA mesmo com o
  Durepoxi declarando secar debaixo d'agua; e PECA e a unica entidade do Arquipelago que NAO
  e arquivo do repositorio — o validador falha de proposito se alguem criar `dados/pecas.json`.
- **Uma correcao de entrada para o bloco 4:** a secao 1.2 da especificacao tem so "vidro",
  mas a matriz distingue vidro comum de vidro LAMINADO — e a distincao decide o produto
  (o acetico e proibido no laminado). O formulario precisa da pergunta, escrita em portugues
  de gente: "o vidro tem uma pelicula entre duas camadas?".
- 5 itens esperando link de afiliado e 5 sem imagem — os cinco da categoria cola. Geracao de
  link e da Sentinela estrategica, no navegador, e nunca da Fundacao.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos
  blocos 1 e 2. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **as categorias REJUNTE e PASTILHA do banco**, que nao dependem
  de site e que o esquema ja deixou com os campos nomeados (rejunte com faixa de junta;
  pastilha com lado anunciado, passo de fabrica, espessura e unidade de venda). O bloco 3b
  (casca) e o bloco 4 (ferramentas) continuam dependendo so de o WordPress existir.

11/09/2026 — sessão de conversa: decisões do Raphael gravadas — artesã aparece com nome/foto/redes; botão Verificar disponibilidade + leads por e-mail; acesso do painel vai direto para a artesã.

11/09/2026 11:49Z — BLOCO 3b ENTREGUE: a casca da ilha (commitada e verificada; NAO esta no ar)

- `snippets/clubedomosaico-casca.php` v1.0.0, manifest na revisao 4 com `publicar: true` e
  `ativo: true`. Oito paginas criadas e mantidas por shortcode: inicio, loja, materiais,
  como-fazer, sobre, contato, divulgacao-de-afiliados e privacidade. Cabecalho e rodape pretos
  com o miolo branco, menu sanfona com aria-expanded/aria-controls, favicon proprio no lugar do
  icone do WordPress, JSON-LD Organization + WebSite em toda pagina, apelidos com 301 e a trava
  do sitemap 404.
  sha256 casca: `9b678bcffd00fc75261a6769d64777c2b6d1be1e3fb56e02398bd9d627753001`
- Ferramentas de bancada que nasceram junto, nenhuma publicada no site:
  `ferramentas/gerar-favicon.php`, `ferramentas/render-para-teste.php`,
  `ferramentas/teste-casca.php` e `ferramentas/teste-navegador-casca.mjs`.

- **O QUE ESTA CASCA TEM DE PROPRIO**, e que nao foi copiado de Aquametria nem de Robometria:
  (1) **a marca e uma imagem ENTREGUE, nao um desenho do snippet.** As duas primeiras ilhas
  desenham o simbolo em SVG dentro do codigo; aqui o logo foi feito por gente e o `PROMPT.md`
  proibe redesenhar, vetorizar ou escrever o nome ao lado do arquivo, que ja traz o wordmark. O
  teste reprova se aparecer um `<svg>` de logotipo ou se o nome for repetido em texto dentro do
  bloco da marca.
  (2) **tres motores, tres catalogos.** Loja, Guia e Escola nao cabem num catalogo de
  "ferramentas": a casca tem `cdm_casca_ferramentas()`, `cdm_casca_categorias_do_guia()` e
  `cdm_casca_tutoriais()`, e o cartao de categoria do Guia diz **quantos itens ela tem no banco**
  em vez de um "em breve" generico — e esse numero que separa promessa de trabalho feito.
  (3) **a Loja tem estado vazio honesto, e ele e testado nos DOIS estados.** O catalogo de pecas
  vive no CPT que a artesa alimenta (bloco 4d) e nunca no repositorio, entao hoje a Loja mostra
  "em breve, e sem peca de mentira ate la". O teste simula o CPT com duas pecas e exige que a
  vitrine apareca e o estado vazio suma — sem isso, uma vitrine que nunca mostra peca nenhuma
  passaria despercebida.
  (4) A casca nasce com a **trava do sitemap 404** que a Robometria so descobriu depois de
  publicar: ilha sem post publicado faz o `wp-sitemap.xml` sair com o XML certo e status 404.

- **VERIFICACAO** (secao 8): `php -l` limpo; `teste-casca.php` com **127 afirmacoes** e
  `teste-navegador-casca.mjs` com **33 medicoes** num Chromium de verdade — rolagem horizontal
  **0 px** em 360/390/781/782/783/1200 px nas oito paginas, o botao do menu aparecendo e sumindo
  na borda exata dos 782 px, contraste 21:1 no cabecalho e no rodape e 17,6:1 no corpo (formula da
  WCAG escrita dentro do proprio teste), e a **mesma pagina com o JavaScript DESLIGADO** servindo
  os quatro links do menu visiveis e o corpo inteiro, que e o que o crawler de IA recebe.

- **QUINZE MUTACOES DELIBERADAS, e o que elas custaram.** Treze reprovaram de primeira. **Duas
  passaram**, as duas na mesma trava — a de escassez inventada —, e reescreve-la duas vezes foi o
  trabalho mais util do bloco:
  1. A 1a versao procurava o termo no corpo inteiro com excecao para algumas negacoes escritas a
     mao. Reprovou a pagina Sobre, que diz com todas as letras que **nao** publica selo de mais
     vendido. Regua que reprova a frase certa.
  2. A 2a versao separava o corpo em frases e perdoava a frase com qualquer negacao. A mutacao
     "a ficha tecnica do silicone acetico mais vendido do Brasil lista ... entre as superficies em
     que o produto **nao** deve ser usado" **passou**: o "nao" da frase negava outra coisa.
     Perdoar por presenca de palavra e adivinhar.
  3. A 3a versao, que ficou: a pagina **declara no markup** qual bloco e recusa
     (`class="cdm-nao-fazemos"`), o teste retira esses blocos e proibe o termo em todo o resto. E
     para a declaracao nao virar porta dos fundos, exige que **todo bloco marcado ABRA negando** —
     porque a mutacao seguinte enfiou "Peca mais vendido, ultimas unidades!" dentro do bloco de
     recusa e passou enquanto a regra so pedia negacao em algum lugar dele.
- **A 2a versao, antes de ser reprovada, achou um defeito de verdade escrito pela propria
  Fundacao**: a home chamava o produto de "o silicone acetico **mais vendido** para construcao" —
  numero de venda que esta ilha nunca mediu e nao pode afirmar (secao 7). Corrigido para o nome do
  produto. E a trava de "a pagina medida tem tamanho de pagina" reprovou duas paginas finas demais
  para o indice de um dominio novo (como-fazer com 971 e contato com 1194 caracteres de corpo); as
  duas ganharam conteudo real, tirado do banco e nao de enchimento, e hoje tem 2.716 e 1.813.

- **O DESEMBARQUE NAO ACONTECEU, e isso nao e detalhe.** `curl` para
  `https://clubedomosaico.com.br/...` devolveu **000**, e o `$HTTPS_PROXY/__agentproxy/status`
  registrou `connect_rejected: gateway answered 403 to CONNECT` para
  `clubedomosaico.com.br:443` as 11h19Z. A secao 4 do contrato manda testar antes de presumir
  bloqueio — foi testado, duas vezes, e falhou. Entao **a casca esta no `main` e nao esta no ar**:
  o site continua servindo o tema padrao do WordPress. O item fica aberto e e de uma linha: acionar
  o Sync da ilha e conferir no `/status` que a revisao aplicada e a **4**. Quem tiver o dominio na
  rede Personalizada do ambiente faz isso em um minuto. "Aplicado com sucesso" nao foi dito aqui
  porque nao foi medido.

- 5 itens do banco esperando link de afiliado e 5 sem imagem — os mesmos cinco da categoria cola,
  inalterados: este bloco nao coletou dado nenhum, e nao devia.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos blocos
  1, 2 e 3. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 4 — a ferramenta F2** (seletor de cola e rejunte), que o
  esquema do bloco 3 ja deixou especificado com as 18 celulas recomputadas e as regras de
  elegibilidade executaveis. Ela agora tem casca para viver dentro, catalogo que a lista e pagina
  de divulgacao de afiliados ja publicada, que era o que faltava. Alternativa que nao depende de
  nada: as categorias REJUNTE e PASTILHA do banco.

11/09/2026 13:47Z — BLOCO 3c ENTREGUE: a categoria REJUNTE do banco, e os tres defeitos
que ela revelou (commitado e verificado; a ilha continua NAO estando no ar)

- `dados/materiais-rejuntes.json` com **5 rejuntes Quartzolit** — ceramicas, porcelanatos e
  ceramicas (BT 2024), acrilico, epoxi e piscinas —, mais a regua propria deles no esquema
  (`versao_esquema` 2) e `ferramentas/mutacoes-rejunte.py`. Manifest na revisao 5; a casca
  subiu para 1.1.0.
  sha256 rejuntes:  `ver manifest.json` (recalculado nesta execucao junto com esquema,
  constantes, especificacao, validador, teste-casca e casca)
- **Por que este bloco e nao a F2, que o registro anterior indicava.** A F2 se chama
  "seletor de cola E REJUNTE" e o banco tinha **zero** rejuntes: metade da resposta dela
  sairia cravada na prosa do snippet em vez de recomputada da declaracao, que e exatamente o
  que o esquema do bloco 3 existe para impedir. E o desembarque esta bloqueado por rede, entao
  um bloco publicavel nasceria sem poder ser conferido no ar (secao 8: nao se marca sucesso
  sem medir). O REGISTRO do 3b ja nomeava esta alternativa.

- **O QUE A CATEGORIA DESCOBRIU SOBRE O PROPRIO BANCO: rejunte nao e cola.** Na cola, a lista
  do fabricante nomeia a **base** — a superficie sobre a qual se cola. No rejunte, a mesma
  lista nomeia a **tessela** e o **ambiente**: "ceramicas, pastilhas de porcelana e de vidro"
  e o que vai ser rejuntado, nunca o vaso de cimento embaixo. Rejunte nao toca a base. Por
  isso a categoria ganhou `mapa_de_termos_do_rejunte` (que traduz para ambiente e tessela,
  nunca para base), `regras_de_elegibilidade_do_rejunte`, `perfis_esperados_do_rejunte` e
  `matriz_esperada_do_rejunte` — e a variavel que decide passou a ser a LARGURA DA JUNTA.
  Uma diferenca de regra que vale ser lida antes de discordar: o rejunte tem **tres** ambientes
  criticos e a cola tem dois, e o que entra e `interno_molhado`. Nao e inconsistencia, e
  geometria: a cola fica escondida atras da tessela e a agua chega nela por ultimo; o rejunte e
  a superficie exposta, a agua fica parada em cima dele e e nele que o mofo cresce.

- **DEFEITO 1 — latente, e medido antes de consertado.** `computar_celula()` varria TODOS os
  materiais do banco sem olhar categoria. As 18 celulas da F2 passavam so porque o banco so
  tinha cola: o primeiro rejunte gravado fez **as 18 falharem de uma vez**, cada uma acusando
  os cinco rejuntes como "eliminados por silencio" — frase sem sentido para um produto que
  nunca foi candidato a colar nada. O conserto tentador seria colar os cinco ids nas 18
  celulas do esquema: a matriz voltaria ao verde dizendo uma bobagem. O conserto certo foi
  declarar `categoria_considerada: cola` na matriz e conferir isso em codigo, com trava de
  regressao que reprova rejunte em qualquer lista da matriz da F2.

- **DEFEITO 2 — um numero FALSO que ja estava NO AR.** O cartao "Rejuntes" do Guia trazia
  `'no_banco' => 0` digitado a mao, no mesmo dia em que a categoria ganhou cinco produtos. O
  `teste-casca` nao viu porque conferia so a categoria **cola**, a unica que existia quando ele
  foi escrito — a mesma familia da cicatriz da secao 8 do contrato: regua que so mede a metade
  que ja existia. Casca **1.1.0**: `cdm_casca_numeros()` passa a contar o banco por categoria,
  e os totais de "esperando link" e "sem imagem" da ilha so assumem a via viva do Sync quando
  TODOS os bancos chegaram (somar metade das categorias daria um total menor e com cara de
  verdadeiro). O teste passa a cobrar as **seis** categorias e nos dois sentidos: categoria do
  Guia sem arquivo de banco mapeado reprova, e arquivo de banco sem cartao no Guia tambem —
  dado colhido que a tela nunca mostra e trabalho jogado fora.

- **DEFEITO 3 — de metodo, e apanhado no proprio ato.** Uma busca feita com o numero `1,55`
  escrito DENTRO da consulta devolveu `1,55` como se fosse declaracao do fabricante. Foi
  descartada: pergunta que carrega a resposta nao mede nada. Uma segunda, com pergunta limpa,
  generalizou o 1,75 do cimenticio sem citar documento do epoxi, e ainda inventou uma
  justificativa para o numero — tambem descartada. A pendencia `rejunte-CR-por-tipo` continua
  aberta e **virou limite declarado da ferramenta**, nao um "seria bom ter": dos cinco produtos,
  o acrilico e monocomponente pronto uso em pote de 1 kg e o epoxi e bicomponente fracionado, e
  o CR 1,75 sai de um exemplo de **po**. A coluna de rejunte da F1 passa a dizer na tela que
  vale para rejunte CIMENTICIO.

- **O ACHADO DE MAIOR VALOR E TAMBEM O QUE ELE NAO RESOLVE.** O *rejunte piscinas quartzolit*
  e o unico material do banco inteiro cujo fabricante nomeia **"pastilhas de porcelana e de
  vidro"** em uso submerso — a tessela do mosaico no ambiente mais critico do vocabulario. E
  mesmo assim ele NAO e recomendado em celula nenhuma, por dois motivos que a pagina diz com
  todas as letras: (1) a faixa de junta dele nao foi obtida — a unica mencao e de PROCEDIMENTO,
  "juntas com ate 3 mm devem ser molhadas antes", e ler 3 mm como maximo inverteria a frase do
  fabricante —, entao a regra 1 o mantem fora; e (2) o que ele declara e **agua TRATADA
  quimicamente**, que e piscina, e nao a agua parada de uma fonte ou de um vaso de jardim.
  O lado do rejunte ganhou resposta de verdade (o epoxi: junta de 1 a 5 mm, liberacao em 7
  dias, boletim 2018-01, nivel 2), mas **peca submersa precisa de cola tambem**, e a unica
  declaracao de colagem submersa da ilha continua sendo o press release do Durepoxi, nivel 4.
  A faixa fica declarada como descoberta. Meia resposta escrita como meia resposta ainda e a
  resposta mais util da pagina; meia resposta escrita como resposta inteira e o defeito.

- **VERIFICACAO** (secao 8): `php -l` limpo; `validar-banco.py` com 18 celulas de cola + 9 de
  rejunte + 5 perfis, todos conferidos contra o que esta escrito **A MAO** no esquema, escrito
  antes de rodar o validador; `teste-casca.php` com **137** afirmacoes (eram 127); 33 medicoes
  em Chromium de verdade, 0 px de rolagem em 360/390/781/782/783/1200 px nas oito paginas, com
  a trava 0 confirmando que as paginas medidas tem tamanho de pagina (corpo de 1.557 a 5.915
  caracteres).
- **QUATORZE MUTACOES DELIBERADAS, todas reprovadas.** Doze em `mutacoes-rejunte.py` (junta com
  1 mm a mais, faixa pela metade, faixa invertida, faixa inventada para o rejunte piscinas,
  epoxi perdendo a piscina, ambiente generico cobrindo sol e chuva, grade deixando de pisar na
  borda de 4 mm, rejunte voltando a entrar na matriz da cola, fonte de blog sustentando
  recomendacao, rejunte sem perfil escrito, cabecalho mentindo sobre itens esperando link) mais
  duas na casca (o zero cravado de volta no cartao, e categoria do Guia sem arquivo mapeado).
  **A que mais vale e a decima segunda:** ela tira a declaracao do banco E ajusta o perfil
  esperado no esquema junto, que e como um editor de verdade mexeria nas duas metades — as duas
  passam a errar juntas e a conferencia de perfil deixa de ver. Quem viu foi a **matriz**, que
  continuava esperando o epoxi no topo da celula de 3 mm submersa. E a prova de que a matriz
  nao e enfeite da conferencia de perfil, e a resposta local a cicatriz da secao 8.
- A grade da matriz do rejunte pisa **exatamente** em 1, 2, 4, 5 e 10 mm — os extremos
  declarados pelos cinco produtos — e em 6 e 11, logo depois do ultimo. Grade de passo fixo nao
  separaria "ate 4" de "ate 5", e o validador reprova se alguem tirar uma borda da grade.

- **10 itens esperando link de afiliado e 10 sem imagem**: os 5 de cola, inalterados, mais os 5
  de rejunte. Geracao de link e da Sentinela estrategica, no navegador, nunca da Fundacao.
- **O DESEMBARQUE CONTINUA NAO ACONTECENDO, e agora sao DUAS revisoes presas (4 e 5).** `curl`
  para o Sync e para o `/status` devolveu **000** as 13h46Z, e o `$HTTPS_PROXY/__agentproxy/status`
  registrou `connect_rejected: gateway answered 403 to CONNECT` para `clubedomosaico.com.br:443`.
  **A medicao que aponta a causa, e que nao existia no registro de 11h49Z:** na mesma execucao,
  `aquametria.com.br` e `robometria.com.br` responderam **200**. Nao e a nuvem que nao alcanca
  site nenhum — e o dominio da ilha 3 que nunca entrou na lista Personalizada do ambiente, que
  foi montada quando so existiam duas ilhas. E conserto de um minuto, do Raphael, no seletor de
  ambiente. Nao foi marcado em `bloqueada_por` de proposito: a ilha tem trabalho de sobra que
  nao depende do site, e marca-la bloqueada a tiraria da fila.
- Nao houve memoria disponivel nesta execucao (`/areas` nao existe no ambiente), como nos blocos
  1, 2, 3 e 3b. O estado vive no `ESTADO.md` desta pasta.
- Proximo passo desbloqueado: **bloco 4 — a ferramenta F2**, que agora tem as DUAS metades no
  banco e ganhou uma entrada nova, escrita no esquema e na especificacao: a **largura da junta em
  milimetros** ("quanto espaco voce deixa entre uma pastilha e outra?"), sem a qual nao ha como
  escolher rejunte. Alternativa que nao depende de rede nem de site: as categorias **PASTILHA** e
  **ALICATE** — mas atencao, a PASTILHA e de outra natureza, porque os campos que ela exige (passo
  de fabrica, espessura, peso unitario, unidade de venda) nao existem em boletim de fabricante e
  sim em anuncio de loja, nivel 5 e 6 da escada, e nenhum desses dominios foi testado ainda.

11/09/2026 17:55Z — DESPACHO DO RAPHAEL CUMPRIDO E CONFERIDO NO AR: cabeçalho claro, a voz da ilha, e a home que deixou de ser manifesto (casca 1.2.0, manifest na revisão 6, `/status` conferido)

- **A reclamação era uma coisa só, não duas.** *"Muito ruim o fundo preto no
  header, o logo sumiu, queria algo mais clean."* O logo sumia porque o arquivo
  entregue tem **fundo preto** com wordmark vinho — e o cabeçalho era preto
  porque era a única cor em que aquele arquivo aparecia. Trocar só o fundo
  faria o logo virar um retângulo escuro em cima do branco; trocar só o logo
  deixaria o bloco preto que ele reprovou. Os dois saem juntos ou nenhum sai.
- **O cabeçalho:** papel `#FFFFFF` com linha de 1 px em `#E9DCD7` (a linha da
  seção 6 do contrato, no lugar de sombra), menu em `#1F1715` peso 500 com
  passagem em coral, painel do menu sanfona também claro, `theme-color` branco.
  Medido **no navegador**, não no texto do CSS: `rgb(255, 255, 255)` de fundo e
  `rgb(31, 23, 21)` no menu, nas nove páginas. A paleta **não** ganhou cor nova:
  o despacho sugeria `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A`, e os quatro são
  vizinhos de um a quatro passos dos tokens já aprovados em 10/09. Um segundo
  coral a quatro unidades do primeiro é defeito, não identidade — então valeram
  papel, traço, tinta e coral da ilha. Se o Raphael quiser exatamente aqueles
  hexadecimais, é uma linha.
- **A marca virou o wordmark "clube do mosaico" em TEXTO**, na tipografia da
  identidade (Outfit 600, vinho, minúsculas de verdade e não `text-transform`,
  para quem usa leitor de tela ouvir o nome como ele é escrito). Contraste
  medido no navegador: 17,62:1 do menu e 12,97:1 do wordmark sobre o cabeçalho.
- **O ACHADO QUE NÃO ESTAVA SENDO PROCURADO, e que muda o desenho:**
  `identidade/logo/lotus-512.png` — o símbolo transparente que o despacho manda
  usar no cabeçalho claro — está **TRUNCADO no repositório**. O chunk `IDAT`
  declara 11.638 bytes num arquivo que tem 8.770, com um `IEND` colado no fim.
  Não é imagem cortada pela metade: tentei recuperar o pedaço que existisse e o
  `zlib` recusa o **primeiro** bloco ("invalid code lengths set"), então não sai
  um único pixel. Publicá-lo teria trocado o logo sumido por um ícone de imagem
  quebrada, que é pior porque parece descuido em vez de obra em andamento. A
  metade que existe do par foi ao ar; a lótus fica pendente com o Raphael.
  `ferramentas/gerar-marca.php` nasceu para embuti-la e **recusa** arquivo que
  não abre — confere chunk a chunk, cobra canal alfa e cantos transparentes, e
  sai com código 1 sem tocar no snippet. Rodada hoje: recusou, com o número de
  bytes que faltam na mensagem.
- **A HOME (molde LOJA do `VOZ.md`, seção 15 do contrato).** Abria com três
  parágrafos de método, e o terceiro era a ficha técnica de um silicone com
  código de documento e lista de superfícies proibidas. **Duas dessas frases
  estão literalmente na lista de "Proibidas" do `VOZ.md`** — não é coincidência:
  a lista foi escrita para proibir aquele texto. Agora a home abre por "Mosaico
  feito à mão, uma peça por vez", segue com a vitrine (estado vazio honesto,
  reescrito curto), o bloco "Vai fazer o seu? A gente ajuda a escolher o
  material" e a artesã fechando a página. O número e a fonte **não sumiram do
  site**: mudaram de lugar.
- **A home deixou de se chamar "Início"** — e o defeito por trás disso é que
  valia mais: `garantir_paginas()` nunca sincronizava título, então a página
  nascia com o título da definição e ficava com ele para sempre. Era assim que
  "Início" sobrevivia às versões da casca. Agora sincroniza, **sem tocar em
  `post_name`** (seção 12.1: URL publicada não se move). De quebra, a casca
  passou a gravar `blogname` e `blogdescription` como já gravava
  `page_on_front`: o `<title>` da home no resultado de busca agora diz "Clube do
  Mosaico – Mosaico feito à mão, uma peça por vez", que é a mesma frase da
  página e do rodapé. É a lição da Aquametria de 11/09 aplicada antes de doer.
- **O GUIA perdeu sete seções de bastidor**, que não foram jogadas fora: mudaram
  para **`/materiais/como-sabemos/`**, primeira página de nível 2 desta ilha
  (seção 16), com mãe declarada, `noindex` e fora do sitemap. Ela ficou com
  4.340 caracteres de corpo — não é página fina. No Guia ficaram as seis
  prateleiras, com os resumos reescritos na voz, e o único achado que muda a mão
  de quem faz: silicone acético não serve em espelho nem em cimento, e o neutro
  do mesmo fabricante serve.
- **"Hoje 10 dos 5 itens esperam link" SAIU DO AR.** Os dois números estavam
  certos sozinhos — 10 itens esperando link no banco inteiro, 5 adesivos na
  categoria cola — e a frase que os juntou era impossível. Foi exatamente por
  isso que nenhum teste viu: cada metade era conferida separada. O denominador
  passou a ser `itens_no_banco`, somado das categorias, e a página de
  divulgação parou de **afirmar por escrito** que não há link nenhum: agora é a
  subtração entre o que existe e o que espera.

**VERIFICAÇÃO — 198 afirmações na bancada (eram 137), 54 medições em Chromium, 19 mutações, e a conferência no ar.**

- **A bancada estava medindo oito das nove páginas pela metade, e ninguém
  sabia.** A trava nova de "página inteira" reprovou de primeira: o rodapé saía
  só na primeira página. A causa é um `static` legítimo em
  `cdm_casca_rodape_impresso()` (e outro em `cdm_casca_marca_html()`), que
  existe para o rodapé não sair duas vezes na MESMA página — no site um processo
  é uma requisição e ele está certo. Numa varredura de nove páginas em
  sequência, ele faz o rodapé aparecer na primeira e sumir nas oito seguintes,
  **sem erro nenhum**. É a terceira vez que o Arquipélago paga por isso, e a
  regra do contrato já estava escrita: varredura de muitos estados roda **um
  processo por estado**. O teste passou a fazer isso. E a conferência de "página
  inteira" deixou de ser um número redondo de bytes (que eu não consigo calibrar
  sem o site no ar, e número redondo não é critério) e virou a lista do que uma
  página desta ilha obrigatoriamente carrega: folha, JSON-LD, menu, comando do
  menu, favicon, rodapé e H1.
- **19 mutações deliberadas em `ferramentas/mutacoes-voz-e-cabeca.py`, 19
  reprovadas — mas DUAS passaram na primeira rodada**, e são o resultado do
  teste:
  1. *"o título para de sincronizar"* passou porque a bancada monta o H1 a
     partir da **definição**, e a definição está certa. O defeito mora no outro
     lado, no caminho que atualiza a página que já existe — e medir o H1 servido
     nunca poderia vê-lo. Trava nova: o teste simula o site real de hoje (as
     páginas existem, com os títulos velhos) e afirma sobre o que a casca **manda
     gravar**, inclusive que nenhuma gravação toca `post_name` e que página que
     não é da casca não tem o título reescrito.
  2. *"noindex na página errada"* passou porque o teste conferia que a etiqueta
     sai nas páginas **declaradas** — o que é verdade mesmo quando alguém declara
     a página errada. Conferir a declaração contra ela mesma é a mesma forma do
     teste que mede a si mesmo. Régua nova, vinda de fora: só a página de camada
     de prova pode sair do índice, e nenhuma página do menu pode.
- **As duas mutações que mais valem são as portas dos fundos do portão de voz**,
  e as duas reprovam: embrulhar o Guia inteiro na classe que declara camada de
  prova, e declarar uma **segunda** página como página de prova. Sem contar os
  blocos, medir onde eles começam e exigir que a página de prova seja uma só, o
  portão se desligaria com uma linha e nenhuma palavra mudaria na tela — que é
  exatamente a porta que a Aquametria achou ao tentar quebrar o próprio portão.
- **NO AR às 17h55Z:** `/status` com revisão 6, igual à do manifest. 9 de 9 URLs
  em 200, a nova inclusive. Zero `&#038;` dentro de `<script>` nas nove
  (contado só dentro dos blocos de script). Um rodapé por página. O `H1` da home
  é a frase da voz e nenhuma das três frases proibidas aparece no corpo dela. O
  Guia diz "10 itens de fabricante" e não diz "10 dos 5". `/materiais/como-sabemos/`
  serve `noindex` e **está fora** do `wp-sitemap-posts-page-1.xml`, enquanto
  `/materiais/` continua dentro — as duas direções medidas.
- **A REDE ALCANÇA ESTA ILHA, e o bloqueio anterior era diagnóstico não
  reconferido.** O `ESTADO.md` dizia "403 ao CONNECT para clubedomosaico.com.br,
  segunda execução seguida" e duas revisões presas. Nesta execução o primeiro
  `curl` à home devolveu `000` — e **o mesmo comando, repetido minutos depois,
  devolveu 200**, assim como o Sync, o `/status`, as nove páginas e o sitemap. A
  falha era intermitente, não bloqueio. A lição fica escrita: bloqueio que não é
  reconferido a cada execução vira permanente sozinho, e prendeu duas revisões
  desta ilha por duas execuções.

**10 dos 10 itens do banco ainda esperam link de afiliado; 10 sem imagem.** Este
bloco não tocou catálogo.

**Próximo passo:** a árvore da seção 16 inteira — `ARVORE.md` da ilha, mãe para
toda página existente, breadcrumb com `BreadcrumbList` e blocos "Veja também"
(16.4). `/materiais/como-sabemos/` já nasceu dentro dela e serve de primeiro
caso. Nenhuma categoria de nível 2 do Guia tem as 3 filhas que a 16.5 exige,
então nenhuma nasce agora. Depois disso, o bloco 4 (a ferramenta F2).

---

## 11/09/2026 19h40Z — A ÁRVORE DA SEÇÃO 16, e nenhuma URL se moveu

Casca **1.3.0**, manifest na **revisão 7**. Bloco nomeado como próximo passo pela
execução das 17h55Z e pelo despacho do Raphael de 11/09, cuja última linha dizia
que a árvore era o bloco seguinte.

**O que foi entregue**

- **`ARVORE.md`** (item i do 16.8): os três níveis com slug, onde mora cada uma
  das nove páginas que existem, o que está travado e por quê. É o mapa que os
  blocos seguintes seguem — e o teste lê este arquivo para cobrar que documento e
  código digam a mesma coisa, porque duas metades mantidas à mão em lugares
  diferentes divergem em silêncio.
- **Trilha (16.3)** em oito das nove páginas; a home não tem, que é o que a regra
  manda. Ela nasce entre o cabeçalho e o H1, pelo filtro do bloco
  `core/post-title`, com cinto de segurança no `the_content` para o caso de a
  página não ter aquele bloco.
- **`BreadcrumbList`** em JSON-LD nas mesmas oito.
- **Cluster "Veja também" (16.4c)** nas três seções de nível 1, cada uma listando
  as outras duas: é o ciclo LOJA → GUIA → ESCOLA, que é a razão de esta ilha ter
  três motores num domínio só.

**ESTA ILHA NASCEU COM A ÁRVORE CERTA E NÃO SABIA.** Nenhuma página mudou de
endereço neste bloco, e nenhuma precisou: as três seções já eram nível 1, a única
página de nível 2 já nascera com mãe em 1.2.0, e as quatro da raiz são exatamente
as que a 16.1 admite ali. Por isso **não há um 301 sequer e o sitemap não muda** —
o que faltava era a árvore ficar **visível** (trilha, schema, cluster), que é o
que a 16.3 e a 16.4 pedem. Nas outras duas ilhas o nível 1 ainda é página
inexistente e a trilha sai com degrau em texto; aqui os três degraus de topo são
link de verdade desde o primeiro dia.

**AS DUAS COISAS ERRADAS QUE ESTE BLOCO ACHOU SEM PROCURAR**

1. **O registro do Guia e o `VOZ.md` discordavam nos slugs de duas categorias**
   desde que a casca nasceu: o código dizia `materiais/colas` e `materiais/alicates`,
   o `VOZ.md` dizia `colas-e-adesivos` e `alicates-e-corte`. Nada no repositório
   cobrava os dois juntos, e a divergência só apareceria no dia em que a página
   nascesse — quando já seria URL publicada, que não se move. **O dia de acertar
   é o dia ANTES de a página existir.** Corrigido para o nome do `VOZ.md`, que é
   quem manda no nome do nível (seção 15.1), e agora há trava: todo slug de
   categoria do Guia tem que ser um nome escrito no `VOZ.md`.
2. **O cartão da categoria que ainda não abre publicava contagem de banco** —
   "5 no banco, ficha em construção". O número era certo e era contado do arquivo;
   o problema é outro, e a 16.5 o nomeia: cartão que não é link diz "em breve",
   **sem contagem**. É promessa com número colada num lugar que não se pode
   visitar. O número não sumiu do site: continua na camada de prova do Guia e na
   página Como sabemos (15.2), contado, que é onde quem quer conferir confere.
   O campo `no_banco` continua existindo e continua sendo cobrado contra o
   arquivo — o que mudou foi ele deixar de ir para a TELA daquele cartão.

**O SCHEMA PUBLICA MENOS DO QUE A TRILHA MOSTRA, de propósito.** Um `ListItem`
intermediário sem `item` invalida o `BreadcrumbList` inteiro para o Google, e
lista inválida é lista ignorada — então o schema "mais completo", que levaria
também o degrau sem página, publicaria MENOS com cara de publicar mais. Hoje isso
não corta nada nesta ilha, porque os três degraus de nível 1 existem: a via foi
escrita para o dia em que a primeira ficha de material nascer antes da categoria
dela, que é o estado normal das outras duas ilhas.

**A BANCADA ESTAVA MEDINDO FORA DE ORDEM, e a própria trava pegou.** A primeira
versão do render rodava `the_content` **antes** do bloco de título. No site a
ordem é a inversa — o `core/post-title` renderiza primeiro —, e por isso a trilha
nasce acima do H1. Na bancada invertida o cinto de segurança de prioridade 9
disparava, a trilha caía dentro do corpo, e **oito páginas foram reprovadas por
um defeito que só existia na bancada**. Quarta vez que o Arquipélago paga por
render que serve diferente do site; desta vez a conta veio em minutos porque a
trava media a POSIÇÃO da trilha, não a presença dela.

**AS DUAS MUTAÇÕES QUE PASSARAM, E POR QUE ELAS VALIAM MAIS QUE AS DEZESSETE QUE
REPROVARAM.** `ferramentas/mutacoes-arvore.py` quebra a árvore de propósito, uma
mutação por vez. Na primeira rodada, 17 de 19 reprovaram — e as duas que passaram
não passaram por a trava ser fraca: passaram por serem **inertes**.

- *"degrau de trilha vira link morto"* trocava o `<span>` do degrau sem página por
  um `<a>`. Só que **nenhuma página desta ilha tem degrau sem página hoje**, então
  o ramo nunca é executado e o site servido é byte a byte o mesmo.
- *"cluster publicado com uma irmã só"* baixava o piso de 2 para 1 irmã. Só que
  nenhuma página desta ilha tem **exatamente uma** irmã no ar — elas têm zero ou
  duas.

É a cicatriz da grade que não pisa na borda, com a borda faltando no **mundo** e
não no teste. A saída foi a mesma do modo `todas` do render: **a bancada fabrica
a borda**, aqui pelo filtro `cdm_arvore`, que é o mesmo por onde uma página nova
entrará no mapa de verdade. As duas situações fabricadas são as duas que esta
ilha vai ter — a ficha nascendo antes da categoria, e uma categoria com uma irmã
só. Com elas, as 19 de 19 reprovam.

**VERIFICAÇÃO em bancada:** `teste-casca.php` com **327 afirmações** (eram 198),
um processo por página; `php -l` limpo nos dois snippets; `validar-banco.py`
aprovado; `mutacoes-arvore.py` 19 de 19 reprovadas; `mutacoes-voz-e-cabeca.py`
19 de 19 e `mutacoes-rejunte.py` 12 de 12 continuam reprovando (nada deste bloco
afrouxou trava anterior).

**NO AR às 19h40Z:** Sync acionado por `curl`, `/status` com **revisão 7**, igual
à do manifest. **9 de 9 URLs em 200** e **117 afirmações medidas no HTML
SERVIDO**, sem uma falha:

- zero `&#038;` dentro de `<script>` nas nove (contado só dentro dos blocos de
  script, 7 na home e 8 nas outras);
- trilha em 8 de 9, sempre **antes do H1** e **uma só por página**; a home não
  tem, e também não publica `BreadcrumbList`;
- nenhum degrau aponta para página inexistente; a trilha de
  `/materiais/como-sabemos/` tem os três degraus e o do meio **linka** a mãe;
- `BreadcrumbList` nas oito, todo `ListItem` com `item`, posições de 1 a n sem
  buraco, e a relação que importa conferida uma a uma: **os itens do schema são
  os degraus linkados da trilha mais a página atual**;
- "Veja também" em 3 de 9 — exatamente as três seções, com 2 irmãs cada, nenhuma
  irmã morta e nenhuma página se listando como irmã de si mesma;
- os **6 cartões** de categoria do Guia servem "Em breve", **sem um dígito** e
  **sem serem link** (16.5), enquanto a camada de prova continua publicando 5
  colas e 5 rejuntes contados do banco;
- o `wp-sitemap-posts-page-1.xml` continua com as mesmas 8 URLs, e
  `/materiais/como-sabemos/` continua fora dele.

**10 dos 10 itens do banco ainda esperam link de afiliado; 10 sem imagem.** Este
bloco não tocou catálogo. Da pauta da seção 17: **nenhum tema escrito, nenhum na
fila, nenhum recusado** — `pauta.md` ainda não existe nesta pasta.

**Próximo passo:** o **bloco 4 — a ferramenta F2** ("qual cola e qual rejunte
para a sua peça"), que é a primeira página de nível 3 desta ilha e o primeiro
caso real do degrau de trilha sem página, já coberto pela borda fabricada na
bancada. Ela nasce com o bloco de compra da seção 7 junto, mesmo com
`afiliado.url` vazio, e com a mãe `/materiais/` declarada no `ARVORE.md`. Só
depois dela uma categoria de nível 2 chega perto das 3 filhas que a 16.5 exige.

---

## 11/09/2026, 20h35Z — O LOGO DELE, INTEIRO, NO CABEÇALHO (despacho do Raphael de 11/09 (2), cumprido inteiro)

**Casca 1.4.0, manifest na revisão 8, `/status` com revisão 8.** Despacho de
prioridade máxima, e a seção 18.2 manda ele sair inteiro: os **cinco itens**
saíram nesta execução, não um por passada.

**O que o cabeçalho serve agora:** `logo-clube-do-mosaico.png` em `<img>` de
52 px de altura, com link para a home e **nenhuma letra ao lado**. O nome está
desenhado dentro da imagem; escrevê-lo de novo seria a marca em dobro na tela e
anunciada duas vezes por leitor de tela. Por isso não existe `<span>` nenhum ali
e quem carrega o nome para quem não vê a imagem é o `alt`. A barra do cabeçalho
subiu de 72 para 84 px, e abaixo de 600 px o logo desce para 44 px — com 52, ele
e o botão do menu não cabem na mesma linha a 360 px.

### A afirmação que sustentava a versão anterior estava errada

Estava escrita em **três lugares do snippet e um do `VOZ.md`** desde 1.2.0: *"o
arquivo entregue tem fundo preto"*. **Não tem** — é transparente, e o Raphael
conferiu na biblioteca de mídia. O logo sumiu em 1.1.0 porque o **cabeçalho** era
preto e o wordmark dentro do arquivo é vinho `#69030C`: defeito de **onde o logo
foi posto**, nunca do arquivo. A 1.2.0 consertou a causa — clareou o cabeçalho —
e, pela leitura errada do sintoma, tirou junto o logo, que era a parte certa.

Fica escrito porque a forma se repete: **sintoma não é causa, e um diagnóstico
escrito com ar de fato se propaga por versões**. É o mesmo desenho do `000` lido
como bloqueio de rede na semana passada, que prendeu duas revisões desta ilha por
dois dias até alguém repetir o comando.

### 1,26 MB num espaço de 78 px — e por que isso não é "processar o logo"

O arquivo dele é o original de 1536×1024 e a marca ocupa 78×52 px na tela.
Servi-lo cru seria 1,26 MB em toda página de um domínio recém-nascido, e
orçamento de rastreamento é a primeira coisa que o Google mede num domínio assim.
**Não se redesenha nem se gera nada** — o `PROMPT.md` proíbe, e tem razão: o
`src` continua sendo a URL exata que o despacho mandou usar, e o `srcset` oferece
as reduções que o **próprio WordPress** gerou do upload dele (`-300x200` com
41 KB, `-768x512` com 175 KB), com `sizes="78px"`. Mesma imagem, mesmo recorte,
mesma origem; quem ignorar o `srcset` baixa o original e vê a mesma coisa. Medido
no navegador: a escolhida foi a de 41 KB.

### As mutações, que é onde o teste vira teste

Seis novas, e a antiga **"logo de fundo preto volta ao cabeçalho claro" foi
aposentada**: ela media o mundo ao contrário — lá o defeito era o logo *entrar*,
aqui é ele *sair*. Mutação que edita a regra antiga vira **inerte** quando a
regra muda de lado, e inerte é verde sem medir nada.

**Duas passaram na primeira rodada, pelo mesmo motivo de sempre:** não acharam o
alvo, porque as linhas do `<img>` foram escritas na mutação sem as duas
tabulações que o arquivo tem. Mutação que não consegue ser escrita é verde que
não mediu nada. Reescritas, as duas morderam: `0x0` de medida declarada e `alt`
vazio.

**A que mais vale da leva é a porta dos fundos do `srcset`:** o `src` fica certo
no código e outra imagem entra no lugar do logo por um atributo que ninguém lê. O
portão passou a cobrar que **todo candidato seja o mesmo arquivo com sufixo de
tamanho**.

### Verificação

Bancada: `teste-casca.php` de **327 para 347 afirmações**, um processo por página
— o `static` de `cdm_casca_marca_html()` é exatamente o mecanismo que faria o logo
sair na home e sumir nas outras oito numa bancada de um processo só, e agora há
uma afirmação por página cobrando isso. `mutacoes-voz-e-cabeca.py` de 19 para
**24 mutações, 24 reprovadas**; `mutacoes-arvore.py` 19/19 e `mutacoes-rejunte.py`
12/12 seguem reprovando; `validar-banco.py` aprovado; `php -l` limpo. **63
medições em Chromium** nas nove páginas em 360/390/781/782/783/1200 com 0 px de
rolagem, incluindo a caixa de **78×52 px desenhada pelo motor de layout** — que é
a diferença entre "a regra de 52 px está escrita no CSS" e "o logo tem 52 px na
tela".

**No ar, às 20h35Z: 9 de 9 URLs em 200 e 102 afirmações medidas no HTML
SERVIDO**, nenhuma falha, por `ferramentas/conferir-no-ar.py`, que nasceu nesta
execução. Ele tem **régua própria**: a URL do logo e a medida 78×52 estão
literais dentro dele, copiadas do despacho, não lidas da constante da casca —
senão as duas metades errariam juntas. Mediu, em cada uma das nove: o `src` é o
arquivo dele, zero texto dentro da marca, `alt` com o nome, medida declarada, o
logo uma vez só, o wordmark em texto de 1.2.0 fora da página, zero `&#038;`
dentro de `<script>`, a folha servida mandando 52 px e o cabeçalho ainda claro.
As três URLs da imagem respondem PNG.

**O critério de pronto que ele escreveu era de olho, e foi conferido de olho:** a
home **servida** foi desenhada em Chromium com os bytes reais da imagem, e o logo
foi ampliado pixel a pixel. A lótus e o nome "clube do mosaico" embaixo, nítidos
sobre o branco, sem texto duplicado ao lado.

### Duas coisas registradas para ele poder discordar

1. **A 52 px o wordmark dentro do logo fica com ~8 px por linha.** Lê-se como
   logotipo, mas é pequeno — o arquivo é um lockup empilhado e 52 px é o número
   do próprio despacho. Os dois caminhos (subir para ~64 px, ou uma versão
   horizontal do lockup) são escolha dele, não da Fundação.
2. **Os hexadecimais sugeridos no despacho continuam fora**, como em 11/09:
   `#FBF7F4`, `#EEE8E4`, `#111` e `#E8483A` são vizinhos de um a quatro passos
   dos tokens que ele aprovou em 10/09. Um segundo branco a quatro unidades do
   primeiro é defeito, não identidade. Se ele quiser exatamente aqueles valores,
   é uma linha.

**10 dos 10 itens do banco seguem esperando link de afiliado; 10 sem imagem.**
Este bloco não tocou catálogo. Da pauta da seção 17: **nenhum tema escrito,
nenhum na fila, nenhum recusado** — `pauta.md` ainda não existe nesta pasta.

**Próximo passo:** o **bloco 4 — a ferramenta F2**, primeira página de nível 3
desta ilha e o primeiro caso real do degrau de trilha sem página, já coberto pela
borda fabricada na bancada. Nasce com o bloco de compra da seção 7 junto, mesmo
com `afiliado.url` vazio, e com a mãe `/materiais/` declarada no `ARVORE.md`.

## 11/09/2026, 22h05Z — BLOCO 4: A F2 NO AR, a primeira ferramenta da ilha

**Entregue:** `/materiais/qual-cola-usar-no-mosaico/` — snippet
`clubedomosaico-f2.php` v1.0.0, casca 1.5.0, manifest na revisão 9,
`/status` com revisão 9. Primeira ferramenta do Clube do Mosaico e
primeira página de **nível 3** da ilha.

### A decisão que decide todas as outras: a resposta é servida pelo SERVIDOR

O formulário é um `GET` para a própria página e o PHP monta a resposta.
**Não existe uma linha de decisão em JavaScript** — o script do rodapé só
evita o recarregamento quando a pessoa troca uma opção, e a página funciona
inteira sem ele. Duas coisas saem de graça dessa escolha, e as duas são
cicatriz do Arquipélago:

1. **Todo estado da entrada é HTML servido de verdade.** A seção 5 do contrato
   diz que ferramenta que calcula no navegador mostra a um modelo de linguagem
   um formulário vazio; aqui qualquer uma das 45 combinações de base × ambiente
   é uma página com a resposta escrita nela.
2. **Não há régua duplicada entre PHP e JS para as duas se separarem em
   silêncio.** Era o caminho mais curto para o defeito clássico de duas metades
   que erram juntas — ou pior, separado.

O preço é URL com parâmetro, e ele é pago na mesma linha: estado com parâmetro
sai com `noindex, follow` e `canonical` para o endereço limpo. Quem entra no
índice é a página-âncora, uma só, e ela carrega as duas tabelas inteiras
(seções 14.1 e 14.4).

### A elegibilidade é recomputada, nunca digitada

As cinco regras da cola e as quatro do rejunte estão em
`dados/esquema-banco.json` e agora têm **duas implementações independentes**:
`ferramentas/validar-banco.py` em Python e o snippet em PHP. As duas são
conferidas contra as matrizes escritas **à mão** no bloco 3 — 18 células de
base × ambiente e 9 de folga × ambiente. A categoria continua sendo parte da
pergunta: a régua da cola decide sobre **base**, a do rejunte sobre **largura
de junta**, e rejunte não toca a base.

### O QUE O RENDER MOSTROU NO PRIMEIRO SEGUNDO, e que nenhum teste procurava

A primeira página montada na bancada dizia **"Silicone Acetico Construcao"** e
**"o fabricante declara ceramica e azulejo"**. O banco inteiro estava sem
acento — 122 strings de tela, escritas assim desde o bloco 2, porque foram
digitadas a partir de busca e porque **até aqui nenhuma página as servia**. No
dia em que uma página passou a servi-las, o defeito virou texto no ar. É a
mesma coisa que a Robometria pagou em 11/09/2026, com 121 strings.

`ferramentas/restaurar-acentos.py` devolveu os acentos em **68 trocas**, e a
operação é **provada diacrítico-only**: reduzidos a sem-diacrítico, os dois
arquivos do banco depois dela são byte a byte iguais aos de antes — com cinco
exceções **declaradas e conferidas uma a uma**, que são os `nome_comercial` dos
rejuntes, escritos em caixa baixa ("rejunte acrilico quartzolit") e promovidos
a nome próprio. A ferramenta imprime cada troca que faz: espelho que não
imprime o que trocou envelhece calado.

De quebra, a tela dizia **"Quartzolit Rejunte Cerâmicas Quartzolit"** — os
cinco rejuntes têm a marca dentro do nome comercial e as cinco colas não.

### A VARREDURA ACHOU UM ESTADO QUE A FERRAMENTA NÃO ACEITAVA

A grade conferida do rejunte pisa em **11 mm** de propósito: é o primeiro valor
depois do maior extremo que algum fabricante declara. O campo do formulário
parava em 10, então quem tem folga de 11 caía **calado** no padrão de 2 mm e
recebia uma resposta que não era a dele. O campo foi para 12 mm e o estado
passou a responder a verdade: nenhum rejunte do banco cobre essa folga.

### As quatro mutações que passaram, e os três buracos que elas abriram

`ferramentas/mutacoes-f2.py` nasceu com 20 mutações e, na primeira rodada,
**quatro passaram**. Nenhuma passou por a trava ser frouxa — as quatro passaram
por a trava medir o lugar errado:

1. **A lista do silêncio nunca era conferida.** A mutação que fazia a matriz da
   cola varrer o banco inteiro punha os cinco rejuntes na decisão de *colagem*
   como "eliminados por silêncio" — frase sem sentido — e o teste só olhava o
   topo e os proibidos. Agora a lista é cobrada **nos dois sentidos**: o que
   falta e o que sobra.
2. **O rejunte só era medido na FRASE, e a frase só nomeia o topo.** Duas
   mutações de faixa de junta punham o produto indevido como elegível *abaixo*
   do topo, onde ele aparece no cartão e não na frase. Recomendar em segundo
   lugar o que o fabricante não declara é recomendar.
3. **Marca em dobro não aparece em teste de conter.** "Rejunte Cerâmicas
   Quartzolit" está *dentro* de "Quartzolit Rejunte Cerâmicas Quartzolit", então
   procurar por conter aprova o nome errado que engloba o certo. A régua passou
   a ser de igualdade, e direta: para todo produto cujo nome já carrega a marca,
   a composição "&lt;marca&gt; &lt;nome&gt;" não pode existir em lugar nenhum do corpo.

E uma quinta, que é a lição mais fina do bloco: **a mutação da faixa pela
metade era INERTE**, e não por não achar o alvo. Ela trocava um `||` por `&&` e
completava as pontas que faltavam — só que o único produto sem faixa tem as
**duas** pontas nulas, então a guarda trocada continuava pegando nele e nada
mudava na tela. Mutação que acha o alvo e mesmo assim não muda o que o site
serve é verde sem medir nada, e é mais difícil de ver que a mutação que não
acha o alvo. Reescrita, ela morde.

### Dois defeitos de régua na bancada que existia

- **`[a-z_]+` não casa com `cdm_f2`.** O `teste-casca.php` mapeava shortcode →
  caminho com essa expressão, e o dígito fazia falta: a página da primeira
  ferramenta da ilha entrava na tabela com caminho **vazio**, e a trilha dela, o
  `BreadcrumbList` dela e o cluster dela passavam a ser medidos contra o nada.
  Régua estreita demais não é régua frouxa: é régua que mede outra coisa.
- **O portão da 16.5 media o cartão errado.** "Cartão de categoria não vira link
  enquanto a categoria não existir" contava TODO cartão do corpo, e no dia em
  que a primeira ferramenta virou link ele reprovou a home e o Guia por um
  cartão que está certo. As duas listagens ganharam classe própria.

### O que a página diz que não sabe

Duas faixas continuam **declaradas** como descobertas, em vez de preenchidas no
chute: **base de plástico** e **peça em contato permanente com água**. E a
página passou a separar uma coisa que não é a mesma: *declaração vaga não é
silêncio*. Dizer "o fabricante não fala" de um produto cujo fabricante escreveu
"certos tipos de plástico" seria falso — ele falou, e falou de um jeito que não
decide. As duas saem em parágrafos diferentes, com a frase dele.

O tempo de espera do PVA também virou texto: o campo existe no banco com o
motivo escrito, e a página diz que não publica o número em vez de simplesmente
não ter a seção. Ausência de seção é indistinguível de "não importa".

### Duas mudanças pequenas na casca, e nenhuma a mais (1.5.0)

1. `cdm_casca_definicao_paginas()` ganhou o filtro **`cdm_paginas`**. Era o
   único registro da casca sem filtro; sem ele, toda ferramenta nova obrigaria a
   editar a casca — e casca editada por bloco de ferramenta é casca que sai do
   ar por defeito de ferramenta.
2. **`/materiais/` passou a listar as ferramentas** (16.4a). Ela é a mãe das
   duas e não as listava; enquanto nenhuma existia isso não aparecia, e no dia
   em que a primeira nasce a falta vira página órfã. **E a listagem vem ANTES
   das seis prateleiras**: as seis são cartão "em breve" e nenhuma abre, então
   deixá-las no topo punha seis cartões mortos na frente do único caminho vivo
   da página — que é justamente o que termina numa recomendação de compra.

### VERIFICAÇÃO

- `ferramentas/teste-f2.php`: **72 afirmações**, régua própria, **um processo
  por estado** — os **45** estados de cola e os **60** de rejunte, mais a
  âncora e os estados com parâmetro. Zero falha.
- `ferramentas/mutacoes-f2.py`: **20 mutações, 20 reprovadas**.
- `ferramentas/teste-casca.php`: **367 verificações**, nenhuma falha, agora
  incluindo a página nova nos portões de voz, prova, escassez, trilha, árvore,
  página fina e entidade dentro de `<script>`.
- `ferramentas/validar-banco.py`: aprovado, com a matriz batendo com as
  declarações depois da restauração dos acentos.
- `php -l` limpo nos três snippets.
- Chromium em 360/390/781/782/783/1200 px nas doze páginas (as nove da casca,
  a âncora da F2 e dois estados dela com parâmetro): **78 medições, 0 px de
  rolagem horizontal**.
- **NO AR, às 22h05Z:** o Sync aplicou os 5 itens (snippet `f2` criado como #7,
  casca atualizada e os três arquivos do banco virando option pela primeira
  vez), o `/status` devolve **revisão 9**, e `ferramentas/conferir-no-ar.py`
  mediu **145 afirmações no HTML SERVIDO, zero falha** — as 10 URLs em 200, a
  tabela pré-renderizada servida, o JSON-LD servido, e os quatro casos de
  coerência (espelho, cimento em sol e chuva, MDF e vidro laminado) com o
  silicone acético **na seção do que não usar** e nunca na recomendação.
  O sitemap passou de 8 para **9 URLs**, a F2 recebe **dois links internos** (a
  home e a mãe) e a trilha serve os três degraus com endereço de verdade.

  **O Sync precisou de três disparos, e a razão vale registrar:** os dois
  primeiros leram do `raw.githubusercontent` um `manifest.json` ainda na revisão
  8 enquanto já baixavam a casca nova — "sha256 divergente, não aplicado", que é
  a trava funcionando. Cache de borda por caminho, não por commit: o arquivo
  novo e o índice velho chegam em momentos diferentes. Esperar e repetir
  resolve; o que não se pode é ler o primeiro "0 aplicados" como entrega.

### Números da ilha, contados

**10 dos 10 itens do banco esperam link de afiliado; 10 estão sem imagem** —
este bloco não tocou catálogo, e nenhum dos dez tem loja possível hoje. Da
pauta da seção 17: **nenhum tema escrito, nenhum na fila, nenhum recusado** —
`pauta.md` ainda não existe nesta pasta.

**Próximo passo:** a **F1**, em `/materiais/quantas-pastilhas-para-mosaico/`,
com a mesma mãe. A especificação está pronta desde o bloco 2, com a correção do
bloco 3c: a coluna de rejunte vale só para rejunte **cimentício** e a de gramas
de cola sai **vazia com explicação**, porque faltam o consumo por área da
cimentcola e o rendimento por área do silicone. Ela reaproveita da F2 o registro
de página pelo filtro, o desenho de resposta servida pelo servidor com `noindex`
no estado com parâmetro, o cartão de compra e o padrão de teste com varredura
da entrada inteira.

## 12/09/2026, 00h05Z — BLOCO 4, SEGUNDA PARTE: A F1 NO AR — e a casca que não deixava a página nascer

**Entregue:** `/materiais/quantas-pastilhas-para-mosaico/`, a segunda ferramenta
da ilha (`snippets/clubedomosaico-f1.php` 1.0.0, casca **1.6.0**, manifest na
revisão **11**, `/status` com revisão 11 às 00h05Z). Nível 3, mãe `/materiais/`,
a mesma escolha da F2 e pelo mesmo motivo.

### Por que esta página ganha, e é a única que responde isto

O bloco 1 mediu que a primeira página inteira de "rejunte para mosaico" responde
à pergunta da **obra** — 0,2 a 0,4 kg/m², "1 kg faz 3 m²" —, e esses números
foram calculados com azulejo grande. A **mesma fórmula do fabricante**, aplicada
à pastilha de 1×1 cm com folga de 2 mm, dá **2,8 kg/m²**: 3,8 vezes o azulejo de
10 cm e 2 vezes o piso de 20. A página não disputa aquelas — ela responde outra
pergunta, e serve as duas contas **lado a lado, na mesma tabela**, para a
diferença ficar verificável em vez de afirmada.

### As cinco decisões, e a cicatriz que cada uma evita

1. **A conta é do servidor**, como na F2: o formulário é um GET para a própria
   página, não existe uma linha de decisão em JavaScript, e todo estado é HTML
   servido de verdade. O preço é URL com parâmetro, pago na mesma linha —
   `noindex, follow` no estado com parâmetro, e quem entra no índice é a âncora.
2. **A geometria é nossa; o consumo é do fabricante.** Área por forma (o cone
   pela **geratriz**, nunca pela altura — num vaso bojudo a diferença passa de
   10% e sempre para menos) e contagem pelo passo são aritmética e não dependem
   de banco nenhum. Os gramas saem da fórmula publicada pela Quartzolit com o
   coeficiente **lido do registro do rejunte cerâmicas**, nunca digitado.
3. **A correção do bloco 3c está na tela.** O 1,75 vem de um exemplo de rejunte
   cimentício **em pó**; o acrílico é pronto uso em pote e o epóxi é
   bicomponente. A ferramenta recusa calcular para os dois e nomeia o que falta.
   E recusa também **se o banco trouxer dois coeficientes diferentes**: escolher
   um deles calado é a mesma invenção com outra roupa.
4. **A régua do rejunte tem dono.** `cdm_f2_celula_rejunte()` é chamada daqui em
   vez de reescrita; a F1 só filtra pelo tipo escolhido. Duas implementações da
   mesma decisão no mesmo site é o defeito que a Robometria pagou comparando
   duas cópias da mesma régua.
5. **A sobra vai na pastilha e não no rejunte**, e arredonda para cima. Lote
   novo de pastilha muda de cor: faltar dez peças no fim é pior que sobrar dez.
   O saco de rejunte não tem esse problema.

### O QUE QUASE PASSOU: a página respondeu 404 com o Sync dizendo revisão 10

O Sync aplicou seis itens, criou o snippet #8, escreveu revisão 10 no `/status`
— e `conferir-no-ar.py` devolveu **37 falhas**, todas a mesma: a URL da F1 não
existia. **Commit sem verificação no ar não é entrega**, e foi a régua que disse
isso, não a leitura do log.

A causa é da casca, e é fina: `cdm_casca_montar()` voltava na primeira linha
quando `get_option('cdm_casca_estrutura')` era igual a `CDM_CASCA_VERSAO`. A
1.5.0 tinha acabado de criar o filtro `cdm_paginas` **exatamente** para que uma
ferramenta nova registrasse a própria página sem ninguém editar a casca — e a
guarda deixava esse mecanismo inerte: página nova entrava na definição, a versão
da casca continuava a mesma, a montagem não rodava, a página nunca nascia. **A
F2 escapou porque nasceu junto com a 1.5.0** e foi de carona na troca de versão.
Mecanismo que só é exercitado de verdade na segunda vez que alguém o usa.

**Casca 1.6.0:** a chave passa a ser a versão **mais um resumo do mapa de
páginas** (slug, título, mãe e shortcode de cada uma). Página nova, título
trocado ou mãe trocada mudam a impressão e a estrutura se remonta sozinha no
primeiro carregamento depois do Sync — sem humano logado, sem `?cdm_casca=refazer`
e sem tocar na casca. Remontar é barato e seguro porque `garantir_paginas()` só
cria o que falta. O portão 21b do `teste-casca.php` **mede o mecanismo, nunca a
versão**: um teste que olhasse `CDM_CASCA_VERSAO` teria ficado verde com o
defeito no ar, que foi o que aconteceu por um bloco inteiro.

### O cluster mudou de estado sozinho — e duas mutações antigas pararam de morder

Com a terceira filha de `/materiais/` no ar, a F2 e a `/materiais/como-sabemos/`
passaram a ter **duas irmãs** e as três publicam "Veja também". Ninguém editou
nada: as irmãs são derivadas do mapa, e a regra da seção 6 do `ARVORE.md`
funcionou pela primeira vez no sentido inverso — antes ela **proibia** o bloco,
agora ela o **exige**.

O efeito colateral foi o achado do dia, e são dois casos diferentes:

- **"irmã escolhida fora da mãe" passou** porque o portão do cluster contava
  quantas irmãs saíam e se estavam no ar, **nunca de onde elas vinham**. A
  mutação morria por efeito colateral — estourava a contagem — e o efeito sumiu
  quando havia mais páginas no ar. **Trava frouxa de verdade**, e agora toda
  irmã listada tem a mãe recomputada do mapa. Trava que reprova por efeito
  colateral é trava que um dia para de reprovar.
- **"a página fora do sitemap perde a citação" passou** porque o cluster novo
  liga a camada de prova sozinho. Aqui a trava **não** afrouxou: ela mudou de
  dono. E o que mudou de dono ganhou trava própria — a citação **no texto**,
  medida com o cluster e a trilha fora da conta, porque o que se mede ali é
  escolha editorial, não geração automática.

### O que a página diz que não sabe

A linha de **gramas de cola** nasce vazia com o motivo escrito (o fabricante do
silicone declara rendimento por cordão, não por área, e o consumo por área da
cimentcola não foi obtido). A **pastilha não tem banco**: o cartão de compra tem
o lugar reservado dizendo que está vazio, em vez de sumir. E **sem o banco a
página continua respondendo área e pastilhas** e diz que não publica os gramas —
a bancada mede esse estado de propósito, porque página degradada é uma página
válida, com cabeçalho, rodapé e prosa, e foi assim que a Robometria mediu três
páginas pela metade sem ninguém acusar.

### Verificação

- `ferramentas/teste-f1.php`: **67 afirmações**, régua aritmética escrita fora do
  snippet, um processo por estado. Varre 24 combinações de forma × caquinho, 36
  de folga × tipo de rejunte, as cinco sobras, quatro espessuras, cinco lugares,
  e as bordas fabricadas: vão maior que a moldura, folga que nenhum fabricante
  cobre, caquinho irregular, banco ausente e **banco com outro coeficiente**.
- `ferramentas/mutacoes-f1.py`: **27 de 27 reprovadas.** Duas passaram na
  primeira rodada e as duas viraram afirmação nova — o CR digitado dentro do
  snippet **com o valor certo** (invisível para qualquer teste sobre a tela de
  hoje; só troca de banco o revela) e a vitrine ignorando o tipo escolhido
  (continua sendo subconjunto do que a F2 aprova, então a trava de subconjunto
  não a via).
- `teste-casca.php` de **367 para 409** com a página nova nos portões de voz,
  prova, trilha, árvore e página fina; `mutacoes-arvore.py` **20 de 20**;
  `teste-f2.php` 72 e `validar-banco.py` sem regressão; `php -l` limpo nos
  quatro snippets; os três JSON reparseados.
- Chromium em 360/390/781/782/783/1200 nas **14 páginas** — três delas estados
  da F1, incluindo o da medida que não fecha —, **88 medições, 0 px de rolagem**.
  **A medição foi feita com a casca 1.5.0**, antes do conserto da remontagem, e
  fica dito assim de propósito: o que a prova valer tem que ser o que foi
  medido. O que sustenta ela continuar valendo é uma segunda medida, não uma
  suposição — o HTML servido das 14 páginas é **byte a byte idêntico** entre a
  1.5.0 e a 1.6.0, porque a 1.6.0 só troca a chave que decide *quando* a
  estrutura é remontada e não imprime uma linha na tela (a constante de versão
  nem aparece no HTML). Uma terceira rodada do navegador foi tentada e morreu no
  túnel de rede, que estava derrubando as conexões de fonte.
- **No ar, às 00h05Z:** `conferir-no-ar.py` com **194 afirmações medidas no HTML
  servido, zero falha**. As 11 URLs em 200, as três tabelas pré-renderizadas
  servidas, JSON-LD `WebApplication` + `FAQPage`, canonical na âncora e
  `noindex` em todo estado com parâmetro, e **quatro contas conferidas contra o
  que foi calculado à mão** (vaso 942 cm²/720/264 g, tampo 2.827/588/594 g,
  esfera 1.257/960/352 g, moldura 900/188/189 g). O sitemap passou de 9 para
  **10 URLs**.
- **Defeito de etiqueta consertado de quebra:** o manifest dizia casca 1.4.0
  enquanto o arquivo definia 1.5.0. O sha estava certo — o Sync aplicou os bytes
  certos e o site nunca esteve errado —, envelheceu a **etiqueta**, que é por
  onde qualquer relatório lê o que está no ar. Nenhum portão lia essa metade;
  agora `atualizar-manifest.py` compara a versão do manifest com a constante do
  snippet e **recusa gravar** quando os dois se separam. Foi ele que acusou a
  1.6.0 antes deste commit.

### Números da ilha, contados

**10 dos 10 itens do banco esperam link de afiliado; 10 estão sem imagem** —
este bloco não tocou catálogo, e nenhum dos dez tem loja possível hoje. Da pauta
da seção 17: **nenhum tema escrito, nenhum na fila, nenhum recusado** —
`pauta.md` ainda não existe nesta pasta.

**Próximo passo:** as **fichas de categoria de material** (bloco 4c). A 16.5
continua valendo — categoria só nasce com três filhas de dado real —, e hoje
Colas e Rejuntes têm banco de cinco itens cada e **uma** filha cada (as duas
ferramentas). O caminho mais curto para destravar `/materiais/colas-e-adesivos/`
e `/materiais/rejuntes/` é a leva de fichas de produto, que são nível 3 com dado
real: cinco colas e cinco rejuntes já cadastrados, cada ficha com a declaração
do fabricante, a faixa, a fonte e o cartão de compra. A ilha está **abaixo do
piso** da seção 21 (10 URLs, 21 dias não passaram), então a leva sai no ritmo
normal, de 5 a 10 URLs, sem esperar medição.

12/09/2026 15h55Z — DESPACHO DA SENTINELA DE 12/09 CUMPRIDO INTEIRO (itens 1 e 2)

- **Os dois itens eram o mesmo defeito com duas roupas**, e foi por isso que o
  conserto virou UMA regra em vez de dois remendos: a página falava de menos
  produtos do que listava, ou nomeava a causa errada por quem ficou de fora. A
  regra subiu para o `ARQUIPELAGO.md` seção 7, porque vale para toda ilha:
  **todo item do banco é nomeado exatamente uma vez em cada resposta** — na
  frase que o recomenda, e aí ele está na vitrine, ou numa linha que diz por que
  ele não está — e **o bloco de compra serve exatamente o que a frase nomeia**.
  Junto com ela foi a metade complementar: **a recusa nomeia a causa que a
  página mediu, nunca oferece hipótese**, e **afirmação em bloco tem o escopo
  do que foi medido**.

- **ITEM 2 (F2, `clubedomosaico-f2.php` 1.0.0 → 1.1.0).** A frase dizia "o
  rejunte é Rejunte Acrílico Quartzolit", singular e definitiva, e a vitrine
  logo abaixo servia QUATRO cartões. Agora a frase tem duas linhas — a
  recomendação e os que também servem, com o que os separa escrito (o fabricante
  não nomeia o lugar; a régua do rejunte só transforma silêncio em exclusão nos
  ambientes críticos) — e a vitrine serve exatamente esses. Os que ficaram de
  fora ganharam uma linha cada: fora pela folga (com a faixa publicada), fora
  pelo lugar, fonte de imprensa e **faixa não obtida**.
  **Dois achados dentro do item**, e nenhum dos dois estava no despacho:
  (a) o grupo `mencionados_com_ressalva` não era impresso em lugar nenhum —
  vazio com o banco de hoje, invisível para sempre no dia em que enchesse;
  (b) "faixa não obtida" estava sendo contada como "a folga não cabe", que é
  afirmar sobre uma declaração que ninguém leu — o rejunte piscinas não publica
  faixa, e a página dizia que ele não cobria 2 mm. Esse mesmo defeito tinha
  tornado INALCANÇÁVEL um ramo da frase de recusa que eu mesma acabara de
  escrever ("só o lugar exclui"): com o piscinas eternamente no balde da folga,
  aquele caso nunca acontece. Ramo morto saiu; quem diz a causa são as linhas.

- **ITEM 1 (F1, `clubedomosaico-f1.php` 1.0.0 → 1.1.0).** A recusa culpava
  SEMPRE a folga, inclusive quando a folga cabia e quem excluía era o lugar — e
  com a linha de "outro tipo" logo abaixo dizendo "dentro dessa folga", a página
  negava e afirmava o mesmo fato em duas frases seguidas. Agora são três causas
  com nome próprio, produtos nomeados e a faixa que o fabricante publica; e
  quando a causa é o lugar a página diz "é o LUGAR, não a folga", o que não é
  suposição: quem cai pelo lugar passou pela trava da folga antes.
  **A outra metade do defeito não estava no despacho e só a tela mostrava:**
  `strtok( $rotulo, ' —' )` cortava no primeiro espaço e devolvia só "Rejunte",
  então a frase afirmava sobre o banco INTEIRO ("Nenhum rejunte do nosso
  banco…") o que valia no máximo para o tipo escolhido.

- **O PORTÃO ACHOU UM BURACO NO PRÓPRIO CONSERTO, antes do desembarque.** A
  primeira versão da F1 só prestava contas quando a lista voltava vazia: em 27
  estados ela listava dois cimentícios e não dizia uma palavra sobre o terceiro.
  É o item 2 um andar acima — produto do banco que some da tela sem que nada
  diga por quê. A prestação de contas passou a sair sempre.

- **PORTÃO NOVO: `ferramentas/teste-prestacao-rejunte.php`.** Régua própria,
  recomputada aqui a partir dos `perfis_esperados_do_rejunte` escritos à mão e
  das regras 1 a 4 do esquema — nada nele chama `cdm_f2_celula_rejunte()`,
  `cdm_f2_avaliar_rejunte()` nem `cdm_f2_perfil_rejunte()`. Varre **540 estados
  da F2** (9 bases × 5 lugares × 12 folgas), **180 da F1** (3 tipos × 5 lugares
  × 12 folgas) e as **9 linhas da tabela pré-renderizada**, um processo por
  estado, com as folgas indo de 1 a 12 para pisar nas bordas (1 e 11 estão fora
  de todo extremo declarado; 2, 4, 5 e 10 são extremos exatos). 5 afirmações, 0
  falha.

- **`ferramentas/mutacoes-prestacao.py`: 11 mutações, 11 reprovadas.** As duas
  primeiras são os dois defeitos do despacho escritos de volta. **Quatro delas
  não morderam na primeira rodada, e as quatro ensinaram coisa diferente:**
  (1) a que condicionava a linha de `fora_lugar` mirava um estado que o banco de
  hoje não produz — os dois cimentícios têm faixa e declarações iguais, então ou
  os dois servem ou os dois caem; o estado que existe é o de `sem_faixa`;
  (2) a do grupo de ressalva não mudava um byte enquanto o banco não tivesse
  fonte fraca, e precisou **produzir o mundo** nas DUAS metades (o nível nas
  `fontes` do banco, que o snippet lê, e o nível no perfil escrito à mão, que a
  régua lê) — rebaixar só uma faria o teste reprovar pelo motivo errado;
  (3) a da tabela mirava o grupo de ressalva, vazio, e teve de mirar o de faixa
  não obtida, que está fora em todas as nove linhas;
  (4) a da promoção silenciosa **passou por erro de alvo**: a linha do score é
  idêntica byte a byte em `cdm_f2_avaliar_cola()` e em `cdm_f2_avaliar_rejunte()`,
  e a substituição pegou a primeira — mutou a cola, que este portão não mede, e
  o verde foi honesto. O alvo agora carrega a linha anterior, que é a única
  diferença entre as duas funções naquele ponto.

- **DOIS DEFEITOS MECÂNICOS CONSERTADOS NA MESMA PASSADA (seção 19).** O
  manifest declara `sha256` no grupo `ferramentas` desde que nasceu e **nenhuma
  linha o recalculava**: `render-para-teste` e `teste-casca` estavam com a
  etiqueta de uma versão que não existe mais, de blocos anteriores. E a lista
  conhecia **9 das 18 ferramentas** do disco — entre as ausentes, `teste-f1.php`
  e `teste-f2.php`, que são os dois portões principais da ilha. Bancada não vai
  para o site, então nada disso quebraria uma página; quebrava a capacidade de
  qualquer relatório dizer com o que esta ilha se verifica.
  `atualizar-manifest.py` passou a espelhar o grupo e a cobrar as duas direções
  (ferramenta no disco fora do manifest agora reprova). 16 sha recalculados.

- **VERIFICAÇÃO.** `php -l` limpo nos três snippets; `teste-prestacao-rejunte`
  5 afirmações 0 falha em 729 estados; `teste-f1` 67; `teste-f2` 72;
  `teste-casca` 409; `validar-banco` sem regressão; mutações antigas intactas
  (f1 27/27, f2 20/20, rejunte 12/12, árvore 20/20 — nenhuma virou inerte);
  Chromium em 360/390/781/782/783/1200 nas **16 páginas** renderizadas (as 11 da
  casca mais os 5 estados de ferramenta que este bloco mudou), **98 medições, 0
  px de rolagem lateral**.
  **UMA AFIRMAÇÃO ANTIGA FOI REESCRITA, e isso é parte da entrega:** o
  `teste-f1.php` cobrava a string `'do nosso banco declara folga'` para os 11 e
  12 mm — que é a frase DO DEFEITO. Afirmação que fixa o texto de hoje vira
  trava contra o conserto de amanhã; ela passou a cobrar a intenção (a página
  diz que nenhum serve E diz que a causa é a folga).

- **NO AR às 15h51Z: revisão 12 no `/status`, igual à do manifest, 6 aplicados,
  UM disparo** — sem o atraso de CDN dos blocos anteriores. `conferir-no-ar.py`
  mediu **231 afirmações no HTML servido, 0 falha**, e ele ganhou as afirmações
  do despacho escritas nas palavras do próprio despacho: as 6 combinações do
  item 1 (externo_exposto e contato_permanente_agua × 2, 4 e 10 mm) sem a frase
  antiga, dizendo que a exclusão é do lugar e nomeando o lugar; os 5 rejuntes do
  banco contados um a um em 3 respostas do item 2; e as 9 linhas da tabela
  somando 5.

- **Receita:** 10 dos 10 itens do banco continuam esperando link de afiliado e
  10 seguem sem imagem; este bloco não tocou catálogo, e nenhum dos dez tem loja
  possível hoje. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0
  na fila, 0 recusados.

- **PRÓXIMO PASSO:** o bloco **4c**, fichas de categoria de material
  (`/materiais/pastilhas/`, `/alicates/`, `/colas/`, `/rejuntes/`, `/bases/`,
  `/acabamento/`). A regra nova da seção 7 nasce com ele em vez de ser
  descoberta depois: ficha de categoria é, por definição, uma página que fala de
  TODOS os itens de uma categoria do banco, então a prestação de contas dela é a
  própria página — e o portão desta execução já sabe medir isso. A ilha está
  ABAIXO DO PISO da seção 21 (11 URLs, 21 dias não passaram), então a leva sai
  no ritmo normal, de 5 a 10 URLs, sem esperar medição.

---

## 12/09/2026 17h37Z — A TAG DO GA4 NO AR: a ilha começa a ser medida

**Despacho ALTA de 12/09/2026 para a FUNDAÇÃO** (`dados/despachos.md`), na parte
desta ilha. Casca **1.7.0**, manifest na **revisão 13**, `/status` com revisão 13
às 17h37Z, em **UM disparo**.

- **O MARCO ZERO DESTA ILHA É 12/09/2026 17h37Z.** Antes disso não existe dado de
  audiência, e isso é a metade que faltava para a seção 5 ser executável: a ilha
  nasceu em 10/09 e serviu nove, depois onze URLs **sem tag nenhuma**. Qualquer
  leitura feita até hoje devolveria zero, e aquele zero media **a ausência da
  tag** — nunca a ausência de visita. A seção 5 manda o relatório dizer qual dos
  dois é; até hoje a resposta desta ilha era sempre o primeiro.

- **A prioridade 8 no `wp_head` não é gosto, é o único número que cabe.** O
  despacho pede a tag o mais cedo possível **e** proíbe que ela passe na frente
  do `<title>`, da meta descrição e do JSON-LD. As duas metades juntas dão
  exatamente 8: depois do robots (4), do ícone (5), do `Organization` (6) e da
  trilha (7), e **antes da folha de fontes (20)**, que é o único recurso
  bloqueante desta casca. O `async` faz o resto — o LCP desta ilha é texto.

- **O ID é constante no topo e é conferido antes de ser impresso.** ID de medição
  digitado no meio do código é ID que alguém copia junto com a casca para a ilha
  4 e só descobre trocado quando o relatório do mês vier somando duas ilhas.
  `cdm_casca_ga4_html()` só devolve markup se o ID casar com `G-` + maiúsculas e
  dígitos: meia tag no ar não mede nada **e** ainda faz o console falar.

- **A página de Privacidade mudou na mesma versão, e isso não foi zelo.** Ela
  prometia, com todas as letras, que "se um dia houver medição de audiência, esta
  página será atualizada *antes* de ela ser ligada, com a data da mudança".
  Ligar a medição e deixar a promessa de pé seria publicar uma frase falsa na
  página que existe justamente para não ter nenhuma. Sem banner de consentimento
  (22.4).

- **ACHADO QUE NÃO É DESTE BLOCO, E É PARA O RAPHAEL: o Site Kit by Google
  1.187.0 está instalado e ativo nesta ilha e não mede nada.** Medido no HTML
  servido **antes** de mudar qualquer coisa: zero ocorrência de `gtag(` e zero do
  ID da ilha; o que ele deixa na página é uma meta `generator` e um
  `dns-prefetch`. Plugin desconectado ocupando uma linha de `<head>`. O risco não
  é hoje: no dia em que alguém o conectar pelo wp-admin, a propriedade ganha um
  **segundo dono de tag** e toda sessão passa a ser contada duas vezes **sem uma
  coisa mudar na tela**. Quem acusa isso é uma afirmação nova do
  `conferir-no-ar.py`, que conta os inicializadores de `gtag` no HTML servido.

- **DEFEITO MECÂNICO CONSERTADO NA MESMA PASSADA (seção 19), e ele mordeu esta
  execução.** `atualizar-manifest.py` parava no **primeiro** achado, e o `return`
  do descasamento de versão escondeu a conferência de ferramenta órfã: o
  `mutacoes-ga4.py` recém-escrito ficou fora do manifest **sem uma linha de
  aviso**, numa execução em que a versão do snippet acabara de subir — que é
  exatamente quando ferramenta nova nasce. O portão existia, estava certo e era
  **inalcançável**: a conferência que roda primeiro escondia a que interessava.
  As quatro conferências agora acumulam e a lista sai inteira.

- **VERIFICAÇÃO.** `teste-casca.php` de **409 para 539 afirmações**, 0 falha, com
  a **ordem** medida e não só a presença — portão que só pergunta "existe gtag na
  página?" fica verde com a tag no lugar errado, que é o único jeito de esta
  mudança fazer mal. `mutacoes-ga4.py` novo: **14 de 14 reprovadas**, em três
  famílias (a tag some ou sai pela metade; a tag fica e está errada — ID de outra
  ilha, ID digitado ao lado da constante, `config` discordando do `src`, tag
  dobrada, que é o caso Site Kit; e a tag certa no lugar errado — sem `async`,
  antes do JSON-LD, depois das fontes). **Uma mutação reprovou pelo portão errado
  na primeira rodada e foi reescrita:** ela trocava a frase nova da privacidade
  *pela* velha, então morria na trava da frase nova e deixava sem medida a trava
  que interessa — a que mede a **ausência** da promessa antiga. Agora ela
  acrescenta o parágrafo velho sem tirar o novo, que é como isso acontece de
  verdade. Regressões sem uma falha: f1 67, f2 72, prestação 5 em 729 estados,
  `validar-banco`, e as mutações antigas (f1 27/27, f2 20/20, rejunte 12/12,
  árvore 20/20, voz 24/24, prestação 11/11) — nenhuma virou inerte. `php -l` limpo.

- **NO AR às 17h37Z:** `conferir-no-ar.py` de **231 para 334 afirmações** no HTML
  **servido**, 0 falha. As onze URLs com a tag uma vez só dentro do `<head>`, o
  ID desta ilha, o `async`, o `config` batendo com o `src`, a ordem conferida no
  que o **servidor** serve, o `gtag` como **único** script de terceiro, **um**
  inicializador e não dois, e a página de Privacidade com a frase nova, a data, e
  a promessa antiga **medida como ausente**.

- **O TERCEIRO CRITÉRIO DO DESPACHO FICOU ABERTO, e não por falta de tentativa.**
  O Tempo Real do GA4 não foi confirmado. Duas causas independentes, as duas
  medidas e **repetidas na mesma execução**, como a seção 20.2 exige:
  1. **Sem credencial.** `ferramentas/ga4.py` pede `GOOGLE_SA_B64`,
     `GOOGLE_SA_JSON` ou `GOOGLE_SA_FILE`, e o ambiente desta rotina não tem
     nenhuma das três (zero variável `GOOGLE*`). A conta de serviço já é Leitor
     na conta `Arquipélago`: falta a **variável**, não a permissão.
  2. **`www.googletagmanager.com` está fora da lista de egresso.** 403 ao
     CONNECT, cinco vezes, com `clubedomosaico.com.br` em 200 na mesma passada —
     é **política**, e não a intermitência de túnel da seção 20.2, e a regra é
     nomear o host barrado em vez de insistir. A consequência é maior que o item:
     **nenhuma verificação de tag por navegador a partir da nuvem pode funcionar**
     enquanto esse host estiver barrado, porque o navegador não baixaria o
     `gtag.js`. De quebra, o Chromium não atravessa este túnel nem para o domínio
     liberado (`ERR_CONNECTION_RESET` em 3 tentativas, `ws_closed_mid_exchange` no
     proxy, `curl` em 200 no mesmo minuto).

- **Nasceu mesmo assim `ferramentas/conferir-tag-no-navegador.mjs`**, que abre a
  ilha num navegador e mede o **disparo saindo** (o `tid`, o código que o Google
  devolve, **um** `page_view`, o console limpo). O `conferir-no-ar.py` usa `curl`
  e `curl` não executa uma linha de JavaScript: ele prova que a tag **está** na
  página e nunca que a visita **chega** na propriedade. O arquivo diz no próprio
  cabeçalho que **nunca foi visto aprovando**, porque ferramenta que ninguém viu
  rodar é promessa.

- **O que fecha o item é configuração, não código:** `www.googletagmanager.com` e
  `*.google-analytics.com` na rede Personalizada do ambiente das rotinas, junto
  com os domínios das ilhas que já estão lá, e a credencial da conta de serviço
  na variável de ambiente. Até lá, quem confirma o Tempo Real é o Raphael, no
  Chrome dele. **E o que NÃO se fez, escrito para ninguém ter a ideia:** mandar
  um evento pelo Measurement Protocol para "confirmar" a medição seria inventar a
  visita que se queria comprovar e sujar a série com uma sessão que nunca
  existiu. Zero medido é dado; zero fabricado é mentira.

- **`dados/audiencia.md` nasceu** com o marco zero e com esta não-medição escrita
  como linha da série — que é o que a seção 5 manda quando não se conseguiu medir.

- **Receita:** 10 dos 10 itens do banco seguem esperando link de afiliado e 10
  sem imagem; este bloco não tocou catálogo. Pauta da seção 17: `pauta.md` ainda
  não existe — 0 escritos, 0 na fila, 0 recusados.

- **PRÓXIMO PASSO:** o bloco **4c**, fichas de categoria de material, que já era
  o próximo antes deste despacho furar a fila e continua sendo. A ilha está
  ABAIXO DO PISO da seção 21 (11 URLs), então a leva sai no ritmo normal, de 5 a
  10 URLs, sem esperar medição — e agora, pela primeira vez, com a série de
  audiência correndo por baixo dela.

12/09/2026 19:21Z — A VARREDURA DA SEÇÃO 14.3: o 4c não estava esperando ser escrito, estava esperando banco — e agora isso é um número

- **O bloco começou como 4c e virou a medição que o 4c pedia.** O `ESTADO.md`
  vinha dizendo, execução após execução, que o próximo passo eram as **seis
  fichas de categoria de material** (`/materiais/pastilhas`, `/alicates`,
  `/colas`, `/rejuntes`, `/bases`, `/acabamento`). O `ARVORE.md` já dizia, desde
  11/09, que nenhuma delas podia nascer pela **16.5** — categoria só nasce com 3
  filhas de dado real, e Colas e Rejuntes têm **uma** cada. As duas frases
  conviviam porque nenhuma era falsa. O que faltava era o segundo portão, que
  ninguém tinha medido: **a seção 14.3**, que proíbe faixa de ferramenta sair com
  menos de 3 produtos elegíveis. Sem esse número, a próxima execução escolheria
  entre escrever seis páginas magras e adiar de novo, sem critério.

- **O QUE A VARREDURA MEDIU, de ponta a ponta e pela primeira vez.** Dos **45**
  estados de cola que a F2 serve, **ZERO** chegam aos 3 elegíveis que a 14.3
  exige; o teto é **2** e **13** não servem nenhum produto. Dos **60** estados de
  rejunte, **12** chegam, **48** não, e **25** não servem nenhum. E **5 das 7
  categorias do vocabulário não têm um único item no banco**: `pastilha`,
  `alicate`, `base`, `acabamento`, `apoio`. A consequência é mais dura do que a
  16.5 sozinha: com o banco de hoje **nem as filhas de nível 3 de cola podem
  nascer**, porque nenhum recorte da categoria reúne os 3 itens que o portão de
  dado da seção 9 cobra. Não é falta de texto — é falta de produto.

- **TRÊS FONTES, E NENHUM NÚMERO DIGITADO.** (1) A **faixa** vem de
  `ferramentas/faixa-da-f2.php`, que a mede **provocando o próprio snippet**: põe
  cada valor de um superconjunto deliberadamente maior em `$_GET`, chama
  `cdm_f2_entrada()` — a mesma função que saneia a consulta de quem visita — e
  fica com o que sobreviveu. Faixa digitada mediria a faixa que alguém lembrou e
  ficaria verde no dia em que o campo da junta mudasse de teto. O medidor
  **recusa medir** quando o superconjunto não passa por cima nem por baixo da
  faixa (teto medido igual ao teto da régua não é teto, é o fim da régua) e
  quando o saneamento aceita um valor inventado. (2) A **régua** é a de
  `validar-banco.py`, importada: ela recompõe a elegibilidade das **declarações**
  pelas regras do esquema e foi escrita no bloco 3 **antes** de existir uma linha
  do snippet PHP. Reimplementá-la aqui uma terceira vez não acrescentaria
  independência nenhuma — acrescentaria uma cópia para envelhecer calada. (3) O
  que o **site serve** é conferido por `ferramentas/conferir-cobertura.php`, que
  anda os mesmos estados chamando o snippet, **um processo por estado**.

- **O CRUZAMENTO PASSOU DE 27 PARA 105 ESTADOS, e esse é o ganho estrutural do
  bloco.** A régua Python e a régua PHP são duas implementações da mesma regra, e
  até hoje elas só se encontravam nas **27** células escritas à mão do esquema —
  18 de cola e 9 de rejunte — de **105** que as ferramentas servem. Os outros
  **78** nunca tinham sido comparados com nada: se as duas metades divergissem
  ali, o censo diria um número e a página serviria outro, e nenhum portão veria.
  Hoje as duas concordam nos 105. `conferir-cobertura.php`: **128 afirmações, 0
  falha**.

- **MUTAÇÕES: 14 escritas, 14 reprovadas, e 9 delas NENHUM portão antigo pegou.**
  O script roda, para cada mutação, também `validar-banco.py` e `teste-f2.php`, e
  marca as que só a varredura viu — mutação que qualquer portão antigo pega já
  estava coberta e não justificaria arquivo novo. A que melhor mostra o buraco:
  **a faixa de junta afrouxa só em 7, 8 e 9 mm**. A grade escrita à mão do
  esquema pisa em 1, 2, 3, 4, 5, 6, 10 e 11 mm, escolhidos para encostar nas
  bordas declaradas — é uma grade boa, e é exatamente por isso que 7, 8 e 9 caem
  num vão onde nenhum extremo mora. Com esse afrouxamento o site passa a
  recomendar rejunte que o fabricante não cobre, e os 27 cruzamentos antigos
  continuam verdes.

- **DUAS MUTAÇÕES FORAM REESCRITAS DEPOIS DE PASSAR, e as duas ensinaram algo.**
  (a) A que derrubava a **regra 3 do rejunte** (quem delimita ambiente fica
  fechado nele) passou — e não por buraco no portão: **com o banco de hoje essa
  regra é código morto.** Das cinco fichas, só o acrílico declara ambiente
  (`áreas internas e externas`), e nos estados em que a regra 3 o cortaria a
  regra 2 já o tinha cortado antes, porque `contato_permanente_agua` é crítico e
  as resistências dele param em `áreas molhadas`. A regra **fica no snippet** — é
  ela que vai decidir no dia em que entrar um rejunte que delimite ambiente — mas
  a mutação saiu, porque mutação inerte é teste verde com outro nome. (b) A do
  **gerador contando errado** reprovava pelo portão errado: ela mutava
  `cobertura.py` sem regenerar o JSON, então caía em "arquivo velho" em vez de na
  recontagem. O caso real é alguém mexer no gerador, rodar e commitar as duas
  coisas juntas — aí a regeneração bate consigo mesma e só a recontagem do lado
  PHP vê. Reescrita assim, ela passou a cair em `cola: "com o mínimo" bate com a
  contagem`, que é o portão que ela existe para medir.

- **REDE, reconferida como a seção 20.2 manda.** Os domínios de fabricante estão
  **fora da lista de egresso**: `colormix.com.br`, `vidrotil.com.br` e
  `quartzolit.weber` responderam `000` por `curl` em **duas passadas da mesma
  execução**, com `clubedomosaico.com.br` em **200** nas duas. É política, não a
  intermitência de túnel. **Mas isso NÃO bloqueia a coleta de banco:** o canal de
  busca alcança os mesmos fabricantes, foi assim que o bloco 3c colheu os cinco
  rejuntes, e foi reconfirmado nesta execução. Escrever "coleta bloqueada por
  rede" aqui seria repetir o diagnóstico que custou dois dias a esta ilha em
  11/09.

- **NADA FOI AO AR, e isso é desenho, não pendência.** Nenhum arquivo publicável
  mudou: os três snippets estão byte a byte como estavam, nenhuma URL nasceu e
  nenhuma mudou. `dados/cobertura.json` entra com `publicar: false` — o site não
  precisa dele, e publicá-lo criaria uma segunda fonte do mesmo número dentro do
  site. Portanto **não houve Sync nesta execução**, pela mesma leitura da seção 4
  que valeu no bloco 1. Manifest na **revisão 14**, com as quatro ferramentas
  novas e o censo inventariados — o portão de ferramenta órfã de
  `atualizar-manifest.py` acusou as quatro antes de qualquer commit, que é para
  isso que ele foi consertado ontem.

- **REGRESSÃO SEM UMA FALHA:** `php -l` em todos os snippets e ferramentas,
  `validar-banco` (10 materiais, 18 + 9 células recomputadas), `teste-casca`
  (539), `teste-f1` (67, 24 estados um processo cada), `teste-f2` (72),
  `teste-prestacao-rejunte` (5 afirmações sobre 540 estados da F2 e 180 da F1).
  O `teste-casca` importa em especial porque ele **lê o `ARVORE.md`** para cobrar
  que documento e código digam a mesma coisa, e este bloco escreveu uma seção
  nova lá. As sete baterias de mutação antigas foram rodadas inteiras para provar
  que **nenhuma virou inerte**: árvore 20/20, F1 27/27, F2 20/20, GA4 14/14,
  prestação 11/11, rejunte 12/12, voz e cabeça 24/24 — **128 mutações, 128
  reprovadas**.

- **Receita:** 10 dos 10 itens do banco seguem esperando link de afiliado e 10
  sem imagem; este bloco não tocou catálogo. Pauta da seção 17: `pauta.md` ainda
  não existe — 0 escritos, 0 na fila, 0 recusados.

- **PRÓXIMO PASSO, e agora ele tem ordem e motivo.** **Banco antes de página.** A
  categoria `pastilha` é a primeira, e não por gosto: a F1 responde "quantas
  pastilhas comprar" e a ilha não tem **uma** pastilha no banco, então a
  ferramenta de maior intenção de compra da ilha calcula uma quantidade e não tem
  o que vender — é a faixa descoberta mais cara da seção 14.3 e o buraco que
  nenhuma coleta de cola ou de rejunte fecha. Depois dela, cola, onde o teto de 2
  elegíveis por estado diz que faltam produtos. **Só então** as filhas de nível 3
  por cluster (16.6), e **só então** a mãe de nível 2, que é o 4c. A coleta vai
  pelo canal de busca, com as travas da seção 8: nunca pôr na consulta o valor
  que se quer confirmar, e fonte que não cita o documento é paráfrase.

12/09/2026 21:19Z — BLOCO 3d ENTREGUE: a categoria PASTILHA nasce no banco, e com ela o número que os fabricantes não publicam

- **Por que este bloco e não o 4c.** O `ESTADO.md` da execução anterior deixou a
  ordem escrita e o motivo junto: **banco antes de página**, e `pastilha` é a
  primeira das cinco categorias que a varredura da seção 14.3 achou com ZERO
  itens — a F1 responde "quantas pastilhas comprar" e a ilha não tinha **uma**
  pastilha para vender. Nenhuma URL nasceu ou mudou.

- **O QUE ENTROU:** `dados/materiais-pastilhas.json`, 10 SKUs de dois lugares
  distintos da escada de fontes. Nove da **Glass Mosaic** (fabricante, nível 3):
  linha Cristal 2,5 cm (K2501, K2502, MIX2510) e 3 cm (K117, K77, K66), linha
  Fosca 2 cm (A11, A61) e linha Strip 1,2 cm (ST5102). Um da **Pastilhart**
  (AF1500, 1,5 cm) — e ele entra em **nível 5**, não 3, porque a empresa se
  declara "importadora e distribuidora" na própria página institucional. É o
  único item do arquivo que declara ambiente, inclusive piscina, justamente o
  campo que mais pesaria numa recomendação: ter o dado e **não poder recomendar
  com ele** é o resultado certo da escada, não um defeito da coleta.

- **A COLETA, e as travas da seção 8.** Busca restrita ao domínio, como nos
  blocos 2, 3 e 3c. `curl` e `WebFetch` para glassmosaic.com.br,
  pastilhart.com.br, vidrotil.com.br, colormix.com.br e jatoba.ind.br devolveram
  `000`/`EGRESS_BLOCKED` em **duas passadas** da mesma execução, com
  clubedomosaico.com.br em **200 nas duas** — é política de egresso e não a
  intermitência de túnel que custou dois dias a esta ilha em 11/09 (seção 20.2).
  **Nenhuma consulta plantou o valor que se queria confirmar:** as buscas
  pediram os RÓTULOS da ficha ("tamanho, espessura, tamanho placa, placas caixa,
  peso caixa"), nunca um número.

- **TRÊS CAMPOS NASCEM NULL, E É O QUE ESTE ARQUIVO TEM DE MAIS ÚTIL.**
  - **Peças por placa — nenhum fabricante declara**, e é exatamente o número de
    que a F1 precisa para converter placa em peça. A SERP inteira preenche o
    buraco dividindo o lado da placa pelo lado da pastilha. **A divisão não
    fecha:** 29,2 / 3,0 = 9,73 e 32,3 / 2,0 = 16,15 não são inteiros — em 6 dos
    10 itens. E onde ela fecha, fecha errado por outro motivo: 30,0 / 2,5 = 12
    exige **junta zero** na placa telada, e placa sem junta é placa que não se
    rejunta. As duas leituras possíveis do número anunciado — lado da PEÇA e
    passo do MÓDULO — não podem valer ao mesmo tempo no catálogo de um mesmo
    fabricante. Então `pastilhas_por_placa` e `passo_de_fabrica_cm` ficam null,
    com o motivo escrito, e a régua **reprova** quem os preencher.
  - **Peso unitário — e aqui o próprio catálogo se entrega.** Dividindo peso da
    caixa pela metragem sai um kg/m², que se compara com o teto físico do vidro
    maciço (espessura × densidade). A linha Cristal de 4 mm dá 8,9 e 9,4 kg/m²
    contra teto de 10,0: cabe, e a folga é a junta. A linha Strip de 6 mm dá
    **16,9 contra teto de 15,0 — passa do teto**, o que só pode ser embalagem,
    tela e papel contados junto. Portanto **peso de caixa não vira peso de
    produto em tela nenhuma**, e o item fica no banco com `divergencias` e
    `resolucao` escritas em vez de ser descartado: descartar o caso que não
    fecha é apagar a prova.

- **O DEFEITO QUE ESTE BLOCO ENCONTROU NA PRÓPRIA RÉGUA, e que só podia aparecer
  agora.** O `validar-banco.py` checava o passo de fábrica com
  `lado_anunciado_cm / raiz(N)` — o lado da **pastilha** no lugar do lado da
  **placa**. Com o exemplo do próprio `especificacao-calculadoras.md` (placa
  30×30 com 225 pastilhas → passo 2,00 cm) a conta certa é 30/raiz(225); a que
  estava escrita dava 1/15 = 0,07 cm. **Nunca disparou porque a categoria
  pastilha tinha zero itens** — função de portão que nunca rodou é função morta,
  a mesma família que a Robometria nomeou em 11/09. Consertado, e a geometria do
  `esquema-banco.json` ganhou os campos que a fórmula precisava
  (`placa_lado_a_cm`, `placa_lado_b_cm`, `formato`), mais a recusa de aplicar
  L/raiz(N) em placa que não é quadrada — o caso da linha Strip, 28,6 × 31,2.

- **A CASCA 1.8.0, e por que o banco foi publicado nesta passada.** Option que
  nenhuma página lê é caminho morto, e caminho morto envelhece calado. Então
  `materiais-pastilhas` entra em `cdm_casca_numeros()` junto de colas e rejuntes
  **na mesma revisão**: o cartão "Pastilhas e tesselas" do Guia deixa de servir
  um zero digitado, a tabela do "Como sabemos" ganha a linha e a frase passa a
  nomear as **três** categorias — item que a soma conta e a frase não nomeia é a
  prestação de contas pela metade que o despacho da Sentinela de 12/09 fechou nas
  ferramentas. **Nenhuma URL nova:** `/materiais/pastilhas/` continua sem página
  (16.5 pede 3 filhas de nível 3), e o cartão só vira link quando a página
  existir — quem decide isso é `cdm_casca_url_se_existir()`, não a lista.

- **VERIFICAÇÃO.** `ferramentas/validar-pastilhas.py`, **139 afirmações, 0
  falha**, um processo por item, com a régua escrita à mão no próprio arquivo e
  nunca lida do banco que ela mede. Ela fez duas descobertas que a leitura não
  faria: (a) **o catálogo não tem uma regra única de arredondamento** — a caixa
  da Fosca cobre 2,086583 m² e sai "2,086" num SKU (corte) e "2,09" no irmão
  (arredondamento); uma régua que exigisse uma das duas reprovaria metade da
  linha sem haver erro de dado, e uma que aceitasse tolerância frouxa não mediria
  nada, então ela aceita **exatamente** as duas operações e **diz qual foi usada
  em cada item**; (b) a aritmética das fichas fecha na terceira casa em todos os
  10, o que é o que sustenta que os três números de cada ficha são do mesmo
  produto. `ferramentas/mutacoes-pastilhas.py`: **12 escritas, 12 reprovadas**, e
  **6 delas nenhum portão antigo viu** — entre elas a mutação que "produz o
  mundo", promovendo o distribuidor a fabricante, que sem tocar em mais nada faz
  1,5 cm passar de zero para um elegível.

- **A COBERTURA POR TAMANHO, que é o eixo pelo qual a F1 escolhe pastilha**, e é
  o número que este bloco deixa para o próximo: dos quatro tamanhos que a
  ferramenta oferece, só **um** chega aos 3 elegíveis da seção 14.3 — 2,5×2,5 com
  3; 2×2 com 2; **1×1 com ZERO** e irregular com zero. E 1×1 é o tamanho de **7
  das 12 linhas** da tabela pré-renderizada da F1: ele não aparece em catálogo de
  fabricante nenhum, só em armarinho e marketplace, vendido **a peso** ("100
  gramas") ou por contagem solta — nível 6, que sustenta preço e nada mais. É a
  mesma pendência da conversão grama↔peça vista pelo outro lado.

- **Receita:** 20 dos 20 itens do banco esperam link de afiliado e 20 estão sem
  imagem (eram 10 e 10; os 10 novos entram todos assim, e nenhuma foto foi
  colhida porque o egresso não alcança os domínios). Pauta da seção 17:
  `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

- **NO AR, 21h58Z, em UM disparo do Sync:** `/status` na revisão 15, igual à do
  manifest; 7 itens aplicados. `ferramentas/conferir-no-ar.py` passou de 334 para
  **339 afirmações, 0 falha**, porque ganhou a seção que este bloco tornou
  necessária: **a prestação de contas do banco medida no HTML servido.** A frase
  do Guia publica um total e a repartição dele, e agora tem TRÊS parcelas em vez
  de duas — no ar ela diz "20 itens de fabricante, sendo 5 colas, 5 rejuntes e 10
  pastilhas, e 20 deles ainda esperam link". A régua não lê a frase do snippet:
  lê os **arquivos de banco do repositório**, um a um, e cobra quatro coisas
  distintas — o total servido bate com a soma dos arquivos; as parcelas somam o
  total que **a própria frase** publica (defeito diferente do primeiro: uma frase
  pode estar internamente certa e desatualizada, e foi o outro caso que pôs no ar
  "hoje 10 dos 5 itens"); **toda categoria com arquivo de banco é nomeada** na
  frase, que é o que impede a próxima categoria de entrar na soma e ficar fora do
  texto; e o número de itens esperando link bate com os cabeçalhos. Testada por
  negação antes de ser dada por boa: com o banco adulterado para 9 pastilhas, as
  três afirmações que deviam cair caíram.

12/09/2026 23:20Z — BLOCO 4d, O CORTE DO DESPACHO: A ILHA TEM UM ATELIÊ

- **Por que este bloco e não a ordem de banco que o estado anterior deixou.** O
  despacho do Raphael de 12/09, 18h20 BRT, tem prioridade MÁXIMA e prazo, e o prazo
  é amanhã: ele vai à casa dos pais no domingo 13/09 ensinar a própria mãe a
  cadastrar as peças dela. É a primeira vez que alguém de fora da máquina vai usar o
  que esta fábrica constrói, e é a mãe dele. A seção 18.1 diz que despacho aberto do
  Raphael vence qualquer rotação; a execução das 21h26Z tinha subido a prioridade da
  ilha para 1 sem escrever despacho, mas o despacho estava em `dados/despachos.md`,
  aberto, com prioridade máxima.

- **Dois snippets novos, e a separação não é organização — é o Sync desembarcando um
  sem o outro.** Se o painel tiver defeito, a loja no ar não cai com ele; se a loja
  mudar, ela não perde o acesso.
  - `snippets/clubedomosaico-loja.php` **1.0.0** = snippet **#9** (criado pelo Sync):
    CPT `peca`, taxonomias `colecao` e `tecnica`, a ficha pública em `/loja/<slug>/`,
    a vitrine com foto e o endpoint de cópia da seção 24.
    sha256: `769be91f7e43...`
  - `snippets/clubedomosaico-atelie.php` **1.0.1** = snippet **#10**: papel `artesa`,
    a usuária e o e-mail de acesso, `/atelie/` com login, lista e formulário.
  - `snippets/clubedomosaico-casca.php` **1.9.0**: UMA linha de mudança, o filtro
    `cdm_vitrine_de_pecas`.
  Manifest na revisão **17**; `/status` conferido às 23h13Z (revisão 16) e de novo
  depois do conserto de 1.0.1.

- **OS CINCO ITENS DO CORTE SAÍRAM.** (1) CPT `peca` com `show_ui` FALSE — ela nunca
  vê o wp-admin, e isso é requisito escrito dele — mais o papel `artesa` com sete
  capacidades e o bloqueio duplo; (2) a usuária criada e **o e-mail de acesso enviado
  às 23h13m23s Z**; (3) `/atelie/` com login e tela inicial; (4) o formulário de peça
  em uma tela, no celular; (5) a ficha pública com `Product`+`Offer` e a `/loja/`
  listando. **Uma URL nova**, `/atelie/`, que é `noindex`: a ilha vai de 11 para 12
  páginas publicadas e continua com 11 no índice.

- **O que ficou FORA, por escrito no próprio despacho:** o formulário "Verificar
  disponibilidade" e o CPT `lead_peca` (adendo 3 de 11/09), a aba Interessados, a
  exportação CSV, "Meus dados", o feed do Merchant Center e as páginas de técnica e
  de coleção.

- **A METADE DO PORTÃO QUE A FUNDAÇÃO NÃO CUMPRE, e por que fabricar um jeito seria
  pior que não cumprir.** O despacho manda entrar em `/atelie/` como `artesa` e
  cadastrar uma peça de teste. A senha dela **não existe** em lugar nenhum a que a
  nuvem tenha acesso: o snippet gera uma senha aleatória e a descarta sem imprimir em
  log, e-mail ou option, e o que chega a ela é um link na caixa dela. Gravar a senha
  ou criar um segundo acesso para "poder testar" quebraria a única coisa que protege
  a conta de uma pessoa de verdade. O portão foi partido em duas metades
  **declaradas** no cabeçalho do `teste-atelie.php`, e a metade da LARGUra — os 360
  px que o despacho escreve dentro do portão — foi cumprida num Chromium de verdade,
  porque essa uma máquina mede melhor que um humano.

- **A senha é criada em `/atelie/` e não no `wp-login.php`** — único desvio
  consciente da especificação de 10/09, e a favor dela: o fluxo nativo manda o link
  para uma tela com a marca do WordPress e um medidor de força de senha, que é a
  definição literal do que o portão reprova. A CHAVE continua nativa
  (`check_password_reset_key` e `reset_password`); a TELA é a nossa, com o logo dela,
  e ao terminar ela já entra logada.

- **Reordenar foto é botão ◀ ▶ e não arrastar-e-soltar**, contra o que a
  especificação pedia, por duas razões que valem mais que a especificação: arrastar
  depende de JavaScript (portão 22.8) e de precisão de dedo, e ela vai cadastrar de
  um celular.

- **O QUE OS PORTÕES ACHARAM, e nenhum foi achado lendo código:**
  1. **O `teste-casca` reprovou o painel, e estava certo.** Ele cobrava que a ÚNICA
     página fora do índice fosse a camada de prova. O painel sai do índice por outro
     motivo, e as duas razões exigem tratamentos OPOSTOS — a de prova TEM de ser
     citada por outra página, esta NÃO pode ser citada por nenhuma. Nasceu a camada
     `privada`, declarada no markup e cobrada nas duas direções. A exceção pelo nome
     do slug foi recusada: seria a heurística por vizinhança que a seção 8 proíbe.
  2. **Dois filtros que eu escrevi e ninguém aplicava**, achados antes de rodar uma
     linha: um em `cdm_vitrine_de_pecas` que a casca não aplicava, e um em
     `clubedomosaico_status` que o Sync não aplica porque **ele se pula a si mesmo por
     desenho**. Portão que nunca roda é função morta. O primeiro virou filtro de
     verdade na casca (a única mudança da 1.9.0), o segundo virou rota pública.
  3. **A direção da foto num campo escondido.** Campo `hidden` é enviado seja qual
     for o botão apertado, então o botão "para frente" mandava "para trás" junto e a
     foto andava para o lado errado. Virou `value` do próprio botão, e a mutação 22 é
     esse defeito escrito de volta.
  4. **Os botões de foto tinham 38 px** — achado pelo medidor de navegador a 360 px,
     e invisível em leitura de código e no HTML servido, porque só o motor de layout
     sabe o tamanho que o botão ficou tendo. São os menores do painel e os que ela
     mais vai apertar com o dedo. Viraram 44, na versão **1.0.1**, depois de a 1.0.0
     já estar no ar.
  5. **O canonical da BANCADA** dizia `/vaso-azul/` e o site diz
     `/loja/vaso-azul/` — defeito da bancada, mesma família de "a bancada e o site
     lendo fontes diferentes para o mesmo campo".
  6. **A description abria cinco frases em minúscula depois de ponto**, visto ao
     renderizar a primeira ficha, não em revisão de código.
  7. **O piso de tamanho de página do `teste-loja` estava cravado em 40 KB**,
     calibrado na F2 que carrega uma ferramenta inteira, e REPROVAVA fichas corretas
     de 26 KB. Passou a ser DERIVADO de `/contato/` na mesma bancada: piso inventado
     reprova o certo.
  8. **Código morto que a mutação expôs:** um `str_replace` de `%0D%0A` que nunca
     podia disparar, porque `rawurlencode` de `\n` já devolve `%0A`. Saiu do snippet,
     e a mutação saiu com ele.
  9. **NO AR, e este foi o mais humilhante:** o conferidor contou 6 cartões de peça
     numa Loja com ZERO peça publicada, e os 6 eram os seletores da própria folha de
     estilo. É literalmente o erro que a seção 8 nomeia — medir no HTML inteiro em vez
     de no CORPO — cometido por quem tinha acabado de escrever uma bancada que faz
     isso certo. A bancada media no corpo, o conferidor no ar não, e **nada obrigava
     os dois a concordarem**.
  10. **Três réguas minhas erradas no medidor de navegador:** o piso de 200
     caracteres de corpo, emprestado da regra de página fina que existe para página
     de ÍNDICE, reprovava a tela de entrar, a lista e a de criar senha — as três
     estão certas, porque tela de ação boa tem pouco texto; e duas réguas do painel
     aplicadas na FICHA da peça, que não tem formulário (o botão dela é um link
     `wa.me`) e que mostra foto grande e título na primeira tela, exatamente o que o
     `DESIGN.md` manda. **Apertar o portão errado reprova o desenho certo** — é a
     mesma lição que a Aquametria escreveu em 12/09 sobre catálogo e ficha.
  11. **O `/loja/<peça>/` na tabela do `ARVORE.md`** foi reprovado pelo portão da
     casca, com razão: ele cobra que toda linha daquela tabela exista no código, e
     molde não é página. Foi para a prosa da seção 3b.

- **VERIFICAÇÃO, 0 falha.** `teste-casca` 546 (era 539); `teste-loja` **140, novo**,
  com 72 estados da ficha em processo próprio; `teste-atelie` **209, novo**, com 9
  telas em processo próprio; `teste-navegador-atelie.mjs` **91 medições, novo**, em 6
  páginas × 5 larguras num Chromium de verdade, com um contexto de
  `javaScriptEnabled: false` para medir a 22.8 de verdade; `teste-f1` 67, `teste-f2`
  72, `teste-prestacao-rejunte` 5 sobre 720 estados, `conferir-cobertura` 128,
  `validar-banco` e `validar-pastilhas` aprovados, `php -l` em tudo (com `<?php`
  prefixado, porque o snippet desta ilha nasce sem a tag).

- **MUTAÇÕES.** `mutacoes-loja` **23 de 23** reprovadas, **22 que só o portão novo
  pega**; `mutacoes-atelie` **26 de 26**, **23 que só o novo pega**. E **quatro
  passaram na primeira passada**, as quatro lacunas reais do meu portão: duas porque
  ele media TELAS e nunca DISPARAVA os ganchos (`admin_init` e o filtro da barra não
  aparecem em HTML nenhum), uma porque a varredura da senha NOMEAVA dois lugares onde
  procurar e a mutação gravou num terceiro, e uma porque eu conferia a função de
  mascarar o e-mail sem conferir se a rota a CHAMAVA. As nove baterias antigas
  rodadas inteiras, nenhuma inerte: árvore 20, cobertura 14, f1 27, f2 20, ga4 14,
  pastilhas 12, prestação 11, rejunte 12, voz-e-cabeça 24.

- **NO AR.** `/status` na revisão 16 igual à do manifest às 23h13Z, em UM disparo, 9
  itens aplicados, snippets #9 e #10 criados pelo Sync; e a revisão 17 depois do
  conserto de 1.0.1. `conferir-atelie-no-ar.py` **novo, 33 afirmações, 0 falha, 1
  pulada**: `/atelie/` em 200 servindo a tela de entrar, com `noindex`, FORA do
  sitemap (varrido pelo índice e pelos sub-mapas), ZERO links para ela nas oito
  páginas públicas, e o corpo sem dizer "WordPress", "wp-admin" ou "wp-login" uma
  vez; a rota RECUSANDO sem token (401) **antes** de ser usada com token; as sete
  capacidades presentes e NENHUMA das oito proibidas; o e-mail MASCARADO na resposta.
  A pulada é a ficha da peça, porque não há peça publicada — e esse é o estado certo
  hoje. `conferir-no-ar.py` também rodado: 339 afirmações, 0 falha.

- **O QUE FALTA, E SÓ UM HUMANO FAZ:** confirmar que o e-mail **chegou** na caixa de
  mina196@hotmail.com. `wp_mail` devolveu true, o que diz que o servidor **aceitou** a
  mensagem, não que ela passou do filtro de spam da Hotmail — e a linha 178 do
  `PROMPT.md` manda tratar queda em spam como **bloqueio da ilha**. E o dedo dela na
  tela.

- **A option `cdm_whatsapp` continua VAZIA**, e por isso a ficha da peça serve, no
  lugar do botão, a frase de que o contato ainda não foi publicado — em vez de um
  número inventado. É o primeiro item da fila e é de UMA linha.

- **Próximo passo, com ordem e motivo:** (a) a option `cdm_whatsapp`, que é o que
  transforma a ficha da peça em venda e não depende de bloco nenhum; (b) o adendo 3
  inteiro (`lead_peca`, notificação por e-mail, aba Interessados, CSV), que era o
  corte de hoje e volta à fila agora que o painel está de pé; (c) a ordem de BANCO
  que o estado anterior deixou e que continua valendo — fechar 2×2 na categoria
  pastilha, que está a UM item dos 3 da 14.3, depois a vitrine de pastilha da F1,
  depois a categoria cola.

- **ESTA EXECUÇÃO FOI O CASO QUE PRODUZIU A SEÇÃO 1.1 DO CONTRATO**, escrita por OUTRA
  execução enquanto esta trabalhava, e o registro dela é útil aqui porque ela nos
  salvou: o bloco durou 65 minutos, a reserva de 22h25Z venceu a janela de 40 minutos
  do passo 3, e uma quarta execução da Fundação teria pegado esta ilha por estar
  "livre" pela letra da regra. Se tivesse pegado, teria rodado o item 2 do despacho e
  mandado um **segundo e-mail de acesso para a mãe do Raphael** — e o segundo
  invalida o link do primeiro, na véspera do dia marcado. Ela não pegou porque
  escreveu a regra antes de agir: reserva vencida se reconfere no git, e commit na
  pasta da ilha nos últimos 40 minutos significa ilha VIVA.
  **A 1.1 também manda quem passa de 40 minutos reescrever `executando_desde` no
  próximo commit, e esta execução NÃO fez isso** — a regra não existia quando ela
  começou, e o commit intermediário das 23h13Z manteve o relógio de 22h25Z. Fica
  escrito para a próxima: renovar é uma linha, e é o que faz a execução seguinte não
  precisar do git para saber.

- **Segundo desembarque, e o que ele provou de quebra:** a revisão 17 subiu às 23h28Z
  com a casca do painel em 1.0.1, e o `/atelie/` no ar serve `min-height:2.75rem` nos
  botões de foto. E a rota de conferência mostrou `tentativas: 1` com a MESMA hora de
  envio — ou seja, **o segundo Sync não reenviou o e-mail de acesso**. A guarda por
  option funcionou exatamente onde precisava funcionar: e-mail repetido para a Hotmail
  é o caminho mais curto para a caixa de spam, e caixa de spam aqui é uma pessoa
  esperando na frente do filho sem conseguir entrar.

13/09/2026 11:56Z — ADENDO 3 ENTREGUE: os leads da Loja, e tres defeitos herdados que sairam junto

**O BLOCO.** O adendo 3 de 11/09/2026 — o formulario "Verificar disponibilidade",
o CPT `lead_peca`, a notificacao por e-mail, a aba Interessados e a exportacao
CSV — ficou FORA do corte do despacho de 12/09 **por escrito**, e voltou a fila
agora que o painel esta de pe. Saiu inteiro. Snippet novo
`clubedomosaico-leads.php` 1.0.0 (snippet #11, criado pelo Sync), `loja` 1.1.0,
`atelie` 1.1.0, manifest na revisao 18, `/status` conferido as 11h56Z **em UM
disparo**, 10 itens aplicados.

**O QUE MUDOU NA FICHA DA PECA.** O botao principal deixou de ser um `wa.me`
direto e passou a ser "Verificar disponibilidade": um `<details>` que abre um
formulario de **dois campos** — nome e WhatsApp, e nada mais, como o adendo
manda ("Sem e-mail, sem CEP") — com o texto de consentimento e o link para
`/privacidade/`. Envia, grava o lead, manda o aviso para
`mina196@hotmail.com` com um botao que abre a conversa **com o cliente**,
mensagem ja escrita, e volta para a peca dizendo "Pronto, {nome}!".

**AS SETE DECISOES, e a cicatriz que cada uma evita** (estao inteiras no
cabecalho do snippet; aqui o resumo):

1. **Terceiro snippet, nao um pedaco da Loja.** O Sync desembarca um sem o
   outro — e este e o primeiro arquivo desta ilha que guarda DADO DE PESSOA.
2. **A Loja aplica `cdm_peca_acao`, e ele e aplicado de verdade.** A cicatriz e
   de 12/09, aqui mesmo: dois `add_filter` sem ninguem do outro lado. Por isso
   os portoes medem os DOIS lados — que a Loja CHAMA, e que o que volta aparece
   no corpo servido. Sem o snippet de Leads no ar, a ficha volta ao que servia
   ontem, e nao quebra.
3. **Funciona com o JavaScript desligado** (22.8). O unico script e a mascara do
   telefone, e ela e enfeite: quem canoniza e o PHP.
4. **O nome da pessoa nao viaja na URL.** O POST guarda a confirmacao num
   transient de 10 minutos e redireciona com uma CHAVE aleatoria — o nome nao
   entra no historico, no Referer nem no log de acesso, e quem nao enviou nada
   nao consegue fabricar a tela de "enviado".
5. **O estado com parametro sai `noindex`**, pela mesma razao da F2.
6. **O lead NAO vai para o repositorio.** A copia da secao 24 para a PECA e o
   endpoint `/v1/pecas`; para o LEAD e o CSV dentro do painel, na mao dela. Nao
   ha rota REST de lead — e o portao mede a AUSENCIA, no banco e no ar.
7. **A aba nao cria capacidade nova.** As mesmas sete de ontem: quem pode editar
   as pecas pode ver quem perguntou por elas.

**O DEFEITO QUE O PORTAO PEGOU ANTES DO AR, e a forma dele vale mais que o
conserto.** `cdm_leads_nome_da_artesa()` nasceu lendo o `first_name` da usuaria e
descartando o valor quando ele fosse a palavra "artesa" — uma **lista de palavras
proibidas**, exatamente a heuristica por vizinhanca que a secao 8 do contrato
proibe. Falhou na primeira medicao pelo motivo mais previsivel: o que o snippet
do Atelie grava ali e `Artesã`, com til e cedilha, e nenhuma lista de palavras
acerta a grafia de um texto de espera que ela nao escreveu. A mensagem teria dito
**"Aqui é Artesã"** para uma cliente de verdade. A saida nao foi uma lista melhor:
o nome publico passou a ser **DECLARADO** na option `cdm_artesa_nome`, que nasce
vazia — e vazia significa uma coisa so, que a identidade de `identidade/artesa/`
ainda nao chegou, que e o mesmo estado que o `PROMPT.md` ja manda a pagina Sobre
respeitar.

**O QUE O NAVEGADOR ACHOU, e nenhum apareceria em leitura de codigo.** (a) O
botao "Quero esta peca" saia com **43 px** — um pixel abaixo do alvo de toque,
o mesmo defeito dos botoes de foto do painel em 12/09 e do mesmo jeito, porque so
o motor de layout sabe a altura que o botao ficou tendo. (b) O `select` de estado
da aba saia com 34 px e fonte de 15 px — abaixo de 16 px o iPhone da zoom sozinho
ao tocar no campo e a tela pula. (c) **A aba Interessados vazia nao tinha uma
unica acao**: uma tela sem saida, e o portao a chamou de beco. Ganhou "+ Nova
peca" e "Ver minhas pecas".

**TRES REGUAS DO NAVEGADOR MEDIAM A COISA ERRADA, e as tres teriam reprovado
codigo certo.** (1) `getBoundingClientRect()` de um elemento dentro de um
`<details>` FECHADO **nao devolve zero** neste Chromium — o conteudo e escondido
por `content-visibility`, que pula a pintura e preserva a caixa; medindo altura,
"antes" e "depois" davam o mesmo numero. Quem decide e `details.open`, e ele e a
prova da 22.8 porque o clique acontece num contexto com o JavaScript
**desligado**. (2) O alvo de toque era medido no proprio campo, e o alvo de um
checkbox e o **rotulo** que o liga; e um honeypot, que esta fora da vista, fora do
teclado e fora do leitor de tela, tem caixa de layout e era cobrado. As duas
exclusoes sao ESTRUTURAIS, declaradas no markup — nunca pelo nome do campo. (3)
"existe formulario E todo formulario POSTa" era uma afirmacao so, e reprovou a aba
vazia, que legitimamente nao tem formulario nenhum. Virou duas: todo formulario
PRESENTE POSTa, e a tela tem pelo menos um lugar onde agir.

**OS TRES DEFEITOS HERDADOS, achados ao rodar os portoes ANTES de construir
(secao 18.5).** A execucao das 02h33Z de 13/09 gravou os links de afiliado e nao
rodou portao nenhum:

- **DOIS BANCOS ESTAVAM COMMITADOS FORA DO MANIFEST.** `materiais-colas.json` e
  `materiais-rejuntes.json` divergiam do `sha256` do manifest desde 12/09 — os
  **dez links de afiliado estavam no repositorio e nao estavam no ar**. E a secao
  4 na forma mais pura: o site fica para tras em silencio. O manifest deste bloco
  os levou junto, e o `/status` na revisao 18 e a prova.
- **O PROGRAMA DO MERCADO LIVRE ESTAVA GRAVADO COMO `mercado_livre`** e o
  esquema declara `mercadolivre`. O `validar-banco.py` reprovava; ele nao tinha
  sido rodado. Corrigido no banco, que e o lado errado — o esquema e a
  declaracao.
- **AS REGUAS DA F1 E DA F2 MEDIAM UM MUNDO COM ZERO LINK.** Elas cobravam a
  frase "Link de loja em breve" no corpo da ancora, e isso era verdade so
  enquanto NENHUM item tivesse link. Na noite em que as dez colas e rejuntes
  ganharam link, as duas reprovaram **sem defeito nenhum embaixo** — a ilha tinha
  melhorado e a regua chamou isso de erro. E a familia que a Aquametria nomeou em
  12/09: **regua que depende de um caso raro do banco morre no dia em que o banco
  melhora.** As tres (bancada da F1, bancada da F2 e a conferencia no ar) passaram
  a medir o COMPORTAMENTO nos dois lados — item sem link reserva o lugar, item com
  link serve o botao patrocinado —, e a bancada ganhou um mundo produzido de
  proposito (`sem_links=1`) para poder medir o lado que o banco de hoje nao tem.

**VERIFICACAO NA BANCADA, 0 falha:** teste-leads **175 NOVO** (8 estados de
pagina, um processo cada), teste-loja 147 (era 140), teste-atelie 209,
teste-casca 546, teste-f1 70 (era 67), teste-f2 74 (era 72),
teste-prestacao-rejunte 5 sobre 720 estados, conferir-cobertura 128,
validar-banco aprovado, validar-pastilhas aprovado, `php -l` em tudo.
**NAVEGADOR:** teste-navegador-atelie **124 medicoes** em 7 paginas x 5 larguras,
0 falha, 0 px de rolagem lateral em todas.
**MUTACOES:** mutacoes-leads **36 de 36 reprovadas, 34 que so o portao novo
pega**. Sete delas sao de PRIVACIDADE — o nome na URL, o IP em texto puro, o nome
no titulo do registro, o tipo publico, o tipo na REST, o tipo na busca, a copia
para o Raphael sem option — porque trava de privacidade que ninguem quebra de
proposito e trava que ninguem sabe se funciona. **QUATRO PASSARAM NA PRIMEIRA
PASSADA, e eram quatro buracos reais do meu portao:** o IP guardado em texto puro
(o portao media que o limite funcionava e nao COM O QUE ele o fazia), o e-mail que
falha apagando o lead (o stub da bancada esquecia de apagar, entao a contagem nao
mudava), a acao da aba sem conferir capacidade (o portao media a TELA e nunca as
ACOES) e o despacho de um estado que ninguem registrou como aba (so mensuravel
PRODUZINDO um atendente intrometido).

**NO AR as 11h56Z, em UM disparo:** `/status` na revisao 18, igual a do manifest,
10 itens aplicados, snippet #11 criado. `conferir-no-ar.py` 339 afirmacoes, 0
falha, as 11 URLs intactas. `conferir-atelie-no-ar.py` 37 afirmacoes (era 33), 0
falha, 2 puladas — e as sete capacidades do papel `artesa` continuam sendo
exatamente sete, com nenhuma das oito proibidas, que era a razao da decisao 7.
Medido no ar tambem: a folha do snippet de Leads sai no `/atelie/` (ele esta
ATIVO) e `/v1/leads`, `/v1/lead_peca` e `/v1/interessados` respondem **404** —
lead nao sai por endpoint.

**O QUE NAO FOI MEDIDO NO AR, e e pulada declarada, nao aprovada:** o formulario
so existe em pagina de peca e **nao ha peca publicada**. Ele esta medido na
bancada, em 8 estados, e no navegador a 360 px; no ar, so quando a artesa
publicar a primeira peca. Esta escrito assim no proprio `conferir-atelie-no-ar.py`.

**UMA CONSEQUENCIA QUE VALE DIZER:** a option `cdm_whatsapp` **deixou de decidir
se a peca tem como ser pedida**. Ela estava vazia e por isso a ficha servia a
frase de que o contato nao foi publicado; agora o caminho de venda e o
formulario, que nao depende de numero nenhum. O item "a option de uma linha"
sai da lista do que trava a venda — continua util para um botao direto no
futuro, mas nao bloqueia mais nada.

**PROXIMO, com ordem e motivo:** (a) **"Meus dados"** dentro do painel, que e o
que torna a option `cdm_email_leads` editavel por ela e fecha o unico pedaco do
adendo 3 que ficou em codigo — a option existe e funciona, mas so por
`update_option`; (b) a ordem de BANCO que o estado anterior ja deixava: fechar
2x2 na categoria pastilha, que esta a UM item dos 3 da 14.3, depois a vitrine de
pastilha da F1, depois a categoria cola; (c) o feed do Merchant Center, que
**depende de haver peca publicada** e por isso nao e escolha de fila e sim de
espera. E um item que so um humano fecha, o mesmo de ontem: confirmar que o
e-mail de acesso CHEGOU na caixa da Hotmail.

**A REVISÃO 19, no ar às 12h16Z, e por que houve um segundo desembarque.** Foram **dois disparos**: o primeiro leu do `raw` um manifest ainda na revisão 18 (o cache é por caminho, seção 4), e o segundo, um minuto depois, aplicou os 10 itens. `/status` na 19, `conferir-no-ar.py` 339 afirmações e `conferir-atelie-no-ar.py` 37, zero falha nos dois. Três coisas só
apareceram depois de o primeiro estar no ar:

- **O CSV podia ser EXECUTADO pela planilha dela.** O campo `nome` é digitado por
  qualquer pessoa que abra a ficha de uma peça na internet, e planilha trata
  célula que começa por `=`, `+`, `-` ou `@` como **fórmula** — um nome escrito
  como `=HYPERLINK(...)` vira um link clicável dentro do arquivo que a artesã
  abre. As aspas do CSV protegem a **coluna**, não a leitura; o que protege é um
  apóstrofo na frente. Duas mutações novas medem os dois erros possíveis: não
  escapar, e escapar tudo (que devolve o verde e quebra a leitura).
- **O `From: contato@` que o adendo pede aponta para uma caixa que não existe.**
  A mesma linha do adendo diz que a casca "precisa criar a conta `contato@` no
  cPanel OU garantir SPF/DKIM", e isso é do Raphael e não foi feito. Muita
  hospedagem recusa enviar com remetente que não é caixa local, e aí o lead fica
  gravado e a artesã não fica sabendo dele até abrir o painel. Agora, se a
  primeira tentativa falhar, vai uma **segunda com o remetente padrão do
  WordPress** — o mesmo que entregou o e-mail de acesso dela em 12/09 — e o
  caminho usado fica **gravado no lead**, para a ronda ver que o `contato@` não
  está de pé em vez de descobrir pela ausência.
- **Não deu para conferir SPF/DKIM daqui.** `dns.google` e `cloudflare-dns.com`
  respondem **403 ao CONNECT por política de egresso**, em duas passadas cada,
  como a 20.2 manda testar antes de declarar. Não é intermitência de túnel: é a
  lista Personalizada da rede das rotinas, que tem os domínios das ilhas,
  `googleapis` e `github`, e nenhum resolvedor de DNS. Fica declarado, não
  presumido.

**Números finais, com as duas revisões dentro.** Bancada: teste-leads **184**,
teste-loja 147, teste-atelie 209, teste-casca 546, teste-f1 70, teste-f2 74,
teste-prestacao-rejunte 5 sobre 720 estados, conferir-cobertura 128 — 0 falha em
todas. Navegador: 124 medições em 7 páginas × 5 larguras, 0 falha. Mutações:
**mutacoes-leads 40 de 40 reprovadas, 38 que só o portão novo pega, 0 inertes**.
**As onze baterias antigas rodadas inteiras, para provar que nenhuma virou
inerte: árvore 20, ateliê 26, cobertura 14, F1 27, F2 20, GA4 14, loja 23,
pastilhas 12, prestação 11, rejunte 12 e voz-e-cabeça 24 — 203 mutações, 203
reprovadas, 0 passaram, 0 inertes.**

## 13/09/2026 — "MEUS DADOS": a aba onde ela manda no que só existia em código

Ateliê **1.2.0**, Leads **1.1.0**, manifest na **revisão 20**. **Nenhuma URL
nova.** Fecha o último pedaço do adendo 3 que tinha ficado por fazer — a option
`cdm_email_leads` existia, funcionava, e só a Fundação podia mexer nela — e
cumpre a linha do `PROMPT.md` que promete desde 10/09 que "ela troca a senha em
Meus dados dentro do painel".

**A ABA TEM TRÊS SEÇÕES, e a divisão entre elas é a decisão do bloco.** "Seu
acesso" mostra o e-mail da conta **como texto**; "Sua senha" troca a senha; e
"Avisos de interessados" — que **não é deste arquivo** — traz o endereço para
onde vai o aviso e o nome que assina a mensagem do WhatsApp.

- **A TROCA DE SENHA NÃO PEDE A SENHA ATUAL, e isso é escolha e não esquecimento.**
  O WordPress não pede na tela de perfil dele, e aqui a razão é mais forte que a
  dele: **ela entrou na conta por um link de e-mail** e pode legitimamente não
  saber a senha que quer trocar. Pedi-la trancaria a porta justamente para quem
  tem a chave. O que protege a ação é sessão autenticada + nonce, e o custo de
  errar para este lado é conhecido e menor — quem já está dentro da sessão dela
  já podia publicar, apagar e exportar os interessados. Se um dia houver mais de
  uma pessoa no ateliê, a linha se reabre; está escrita no cabeçalho do snippet.

- **O E-MAIL DA CONTA APARECE E NÃO SE EDITA.** É o endereço para onde vai o link
  de recuperar a senha; um dedo errado num teclado de celular a deixaria de fora
  da própria conta, sem ninguém do outro lado para socorrer no domingo. Aparecer
  responde a única pergunta que ela vai fazer sobre esse endereço ("para onde vai
  o link?"); virar campo é risco sem ganho. O portão mede as duas metades: que o
  endereço **aparece** e que **não existe `<input>` com ele**.

- **QUEM LÊ A OPTION É QUEM A ESCREVE — e por isso nasceu um terceiro ponto de
  extensão.** `cdm_email_leads` e `cdm_artesa_nome` são lidas **só** pelo snippet
  de Leads, então os campos delas nascem lá e chegam à tela pelo filtro
  `cdm_atelie_meus_dados`, do mesmo jeito e pela mesma razão que a aba
  "Interessados" chega pelo `cdm_atelie_abas`: **o Sync desembarca um snippet sem
  o outro**, e uma tela que promete um campo cujo dono não está no ar é a
  divergência silenciosa que esta ilha já pagou duas vezes. **Cada seção é um
  formulário próprio**, com nonce e gravação próprios — nada de um caminho de
  salvar compartilhado onde o campo de um dono sobrescreve o do outro por
  descuido. E a borda do cartão não é enfeite: é o que diz onde um formulário
  acaba e o outro começa, para ela não apertar "Trocar a senha" achando que
  salvou os dois.

- **O VAZIO CONTINUA SIGNIFICANDO O QUE SIGNIFICAVA, e agora a tela DIZ isso.**
  E-mail em branco é "avise no endereço padrão"; nome em branco é "a identidade
  da artesã ainda não chegou", e a mensagem assina "do Clube do Mosaico". Os dois
  campos escrevem embaixo o que o branco faz e **qual é o estado de hoje**, em
  vez de deixar ela adivinhar se esqueceram de preencher ou se é assim mesmo. E
  branco **grava** branco em vez de ser ignorado: sem isso ela não teria como
  desfazer um endereço digitado por engano.

- **E-MAIL INVÁLIDO NÃO DERRUBA O QUE FUNCIONAVA.** O antigo fica de pé e a tela
  diz que não deu. A direção sai da assimetria de custo, como manda a seção 10:
  trocar um endereço que recebe por um que não existe é o aviso do interessado
  sumindo sem ninguém perceber.

**A GUARDA DE `defined()` NO SNIPPET DE LEADS não é paranoia, é a ordem do
desembarque:** este arquivo pode chegar ao ar minutos antes do Ateliê 1.2.0, que
é quem declara `CDM_ATELIE_ABA_DADOS`. Sem ela, um POST daquela ação levaria erro
fatal do PHP no lugar da tela. Com ela, a ação simplesmente não existe enquanto o
outro lado não chega — que é o mesmo que já acontece com a seção, porque o filtro
não é aplicado.

**O QUE A BANCADA GANHOU, e ela é a metade que dá sentido ao filtro:** o
`render-para-teste.php` passou a **produzir o mundo em que um snippet não
desembarcou** (`sem_leads=1`), na mesma família do `sem_links` de 13/09. "A tela
não promete o que o dono ausente não entrega" é uma afirmação que **só pode ser
medida com o dono ausente**, e não há como produzir essa ausência lendo código —
só deixando de carregar o arquivo. O portão mede os dois lados: com o Leads no
ar a seção aparece; sem ele, ela some **e a troca de senha continua inteira**.

**DUAS MUTAÇÕES PASSARAM NA PRIMEIRA PASSADA, e as duas eram buraco de portão —
não de código.** É o resultado do teste, não um detalhe:

1. **`34 quem não está logada troca a senha dela`.** Todas as afirmações da aba
   rodavam **com a artesã logada**, e por isso nenhuma delas via a guarda de
   sessão cair. A mutação removeu `is_user_logged_in()` e `current_user_can()` da
   ação e ficou verde. **Um portão que só mede o caminho feliz da recusa mede a
   recusa errada.** O conserto foi medir a ação deslogada e logada-sem-capacidade
   — o nonce da bancada é determinístico, e é isso que torna a medição possível:
   quem está de fora consegue calculá-lo, que é exatamente o mundo contra o qual
   a capacidade protege.
2. **`48 a tela para de dizer para onde os avisos vão hoje`.** A régua cobrava o
   endereço na tela **com a option vazia** — e aí "hoje" e "o padrão" são o mesmo
   texto, então a frase "deixe em branco para usar mina196@..." satisfazia a
   régua sem a tela dizer nada sobre o estado atual. **Régua que só distingue
   quando os dois valores diferem tem de ser medida onde eles diferem:** a
   afirmação mudou de lugar e passou a rodar depois de gravar um endereço
   diferente do padrão.

**E UMA MUTAÇÃO ANTIGA TINHA VIRADO INERTE nesta mesma passada** — a `24 o script
volta para dentro do shortcode`. O alvo dela era "o `</form></div>` que vem antes
do `add_shortcode`", e o Ateliê 1.2.0 pôs duas funções entre um e outro. **Alvo
de mutação que depende da vizinhança morre no dia em que o vizinho se muda**, e
mutação inerte não mede nada — ela conta como "passou". Reescrita com âncora no
próprio fim do formulário da peça.

**UM DEFEITO MENOR CONSERTADO DE PASSAGEM:** o piso de 8 caracteres da senha
estava escrito três vezes na tela de criar senha (o `strlen`, dois `minlength` e
a frase de ajuda). Virou `CDM_ATELIE_SENHA_MINIMA`, uma vez, para as duas telas
não poderem divergir.

**VERIFICAÇÃO NA BANCADA, 0 falha:** `teste-atelie` **251** (era 209),
`teste-leads` **210** (era 184), `teste-casca` 546, `teste-loja` 147, `teste-f1`
70, `teste-f2` 74, `teste-prestacao-rejunte` 5 sobre 720 estados,
`conferir-cobertura` 128, `validar-banco` aprovado, `validar-pastilhas` aprovado,
`php -l` em tudo. **NAVEGADOR:** `teste-navegador-atelie` **128 medições em 8
páginas × 5 larguras**, 0 falha, 0 px de rolagem — a tela nova passou de primeira
no alvo de toque e na fonte de 16 px, porque reusa `.cdm-at-campo` e
`.cdm-at-botao` em vez de inventar botão.

**MUTAÇÕES: 262 em 12 baterias, 262 reprovadas, 0 passaram, 0 inertes.**
`mutacoes-atelie` de 26 para **37** e `mutacoes-leads` de 40 para **48** — as 19
novas atacam a aba pelas duas famílias de sempre: as que **abrem porta** (o nonce
que some, a capacidade que some, o piso da senha que cai, o segundo campo que
deixa de ser conferido) e as que **vazam segredo** (a senha no endereço de volta,
o e-mail da conta virando campo). As dez baterias antigas rodadas inteiras:
árvore 20, cobertura 14, F1 27, F2 20, GA4 14, loja 23, pastilhas 12, prestação
11, rejunte 12 e voz-e-cabeça 24.

**NO AR às 14h04Z, e foram TRÊS revisões e quatro disparos, por um motivo que não
era o cache.** `/status` na **revisão 22** igual à do manifest, 10 aplicados,
`conferir-no-ar.py` **339** afirmações e `conferir-atelie-no-ar.py` **45** (era
37), 0 falha nos dois, as 11 URLs intactas, e as sete capacidades do papel
`artesa` continuam sendo exatamente sete. A marca do código novo foi medida **no
corpo servido**, não no log do Sync: `.cdm-at-secao` só existe no Ateliê 1.2.0, e
a folha do painel sai no `/atelie/` mesmo deslogada — é a diferença entre "o
manifest diz que subiu" e "o site está servindo". Medido também que
`?estado=meus-dados` deslogada cai na tela de entrar, sai `noindex`, e **não
serve** `trocar_senha`, `cdm_email_leads`, `cdm_artesa_nome` nem o e-mail dela.

**PULADA DECLARADA, não aprovada:** a aba só existe para quem entrou, e a
Fundação não entra — a senha da artesã não existe para a nuvem, por desenho. O
que está medido no ar é a versão servida e a ausência do que não pode vazar; o
dedo dela na tela de 360 px continua sendo a metade do domingo.

### O QUE ESTA EXECUÇÃO ENCONTROU E NÃO ERA DELA — dois commits mexeram no banco desta ilha enquanto ela estava reservada

**Isto é o achado mais caro do bloco, e não é sobre "Meus dados".** Os commits
`4e69738` (a escada do link de compra, seção 25 nova do contrato) e `35412c1` (o
`url_produto` do teste de vida) chegaram ao `main` às 13h36Z e depois, editaram
`dados/materiais-colas.json` e `dados/materiais-rejuntes.json` e **não tocaram no
`manifest.json`**. Lido no `/status`, três vezes seguidas: `"materiais-colas:
sha256 divergente — não aplicado"`. **Os dez links novos, o `url_produto` e as
três fotos estavam no repositório e fora do ar** — a seção 4 na forma mais pura, e
a segunda vez no mesmo dia (a execução das 11h56Z tinha achado exatamente isto).

O `4e69738` também deixou **11 erros de esquema**, nenhum dos quais sobreviveria a
um `validar-banco.py` de segundos: `mercado_livre` em três itens onde o
vocabulário declara `mercadolivre` (**o mesmo defeito de 12/09, de volta**),
`imagem` sem `largura`/`altura`, e os contadores de cabeçalho dizendo "nenhuma
foto foi coletada" com três fotos coletadas.

**A LARGURA E A ALTURA DA FOTO: havia dois caminhos, e o cômodo era o errado.** O
feed de afiliado da Shopee — que a seção 25.3 nomeia como a fonte legítima da foto
— **não declara dimensão**. O caminho cômodo era afrouxar o esquema para aceitar
os dois campos ausentes; e ele estaria errado, porque os dois campos existem para
a página **reservar a caixa da foto antes de ela chegar**, e caixa sem medida é o
salto de layout que a seção 22.4 chama de defeito de desempenho. O outro caminho
era **medir**: `cf.shopee.com.br` responde 200 em duas passadas (medido, não
presumido), e nasceu `ferramentas/medir-imagens.py`, que lê a dimensão do
cabeçalho do arquivo servido — JPEG, PNG e WebP, sem biblioteca, porque instalar
Pillow para ler dois inteiros seria trocar uma linha de código por um risco de
ambiente. **1024×1024, 1024×1024 e 768×768, lidas.** `800x800` digitado porque
"foto de e-commerce costuma ser quadrada" passaria no validador exatamente igual —
e seria chute com cara de dado, que é o defeito mais caro que esta fábrica tem.
Download que falha vira `FALHOU` e o item **continua reprovando**: rede fechada
nunca vira número.

**E a metade que não tem conserto do lado da Fundação está em `dados/despachos.md`:**
a reserva por commit da seção 1 funcionou como escrito — esta execução perdeu a
robometria e a aquametria e pegou a clubedomosaico às 13h19Z —, e **uma terceira
sessão editou o banco desta ilha assim mesmo**. A reserva protege contra quem a
lê; não existe para quem entra pela porta do dado. Hoje custou dois rebases e duas
revisões a mais; o custo caro é o do próprio 1.1, dois trabalhos concorrentes na
ilha da artesã no dia em que ela ia aprender a usar o painel. É decisão do
Raphael.

**PRÓXIMO, com ordem e motivo:** (a) a ordem de BANCO que o estado anterior já
deixava — fechar 2×2 na categoria pastilha, que está a UM item dos 3 da 14.3,
depois a vitrine de pastilha da F1, depois a categoria cola; (b) o `url_busca` do
degrau 3 e o segundo link discreto que a seção 25.2 manda pôr embaixo do botão —
os campos chegaram ao banco e **a página ainda não os serve**, então hoje a escada
existe no dado e não na tela; (c) o feed do Merchant Center, que depende de haver
peça publicada e por isso não é escolha de fila e sim de espera. O que só um
humano fecha continua o mesmo: confirmar que o e-mail de acesso CHEGOU na caixa da
Hotmail, e o `contato@clubedomosaico.com.br` que ainda não existe como caixa.

---

## 13/09/2026, 15h18–15h45Z — A ESCADA DA SEÇÃO 25 CHEGA À TELA (f2 1.2.0, manifest revisão 23)

**Terceira ilha tentada nesta execução, e isso é a seção 1 funcionando.** A aquametria foi
reservada às 15h16Z e a robometria às 15h17Z por outras duas execuções; o push da minha
reserva da aquametria foi recusado por cerca de um minuto. O passo 5 manda voltar ao passo 2
e escolher outra ilha, e foi o que aconteceu — sem force push, sem atropelo.

**O bloco é o item (b) que a execução anterior deixou escrito**, palavra por palavra: *"o
`url_busca` do degrau 3 e o segundo link discreto que a seção 25.2 manda pôr embaixo do
botão — os campos chegaram ao banco e a página ainda não os serve, então hoje a escada
existe no dado e não na tela."* Ele venceu a ordem de BANCO que vinha antes na fila porque a
25.2 não é preferência de fila: ela diz que **não existe item publicável sem piso** e que a
página com piso no banco **nunca** diz "em breve". Dez itens estavam nesse estado.

### O que mudou na tela

Nasce `cdm_f2_compra_html()`, dona dos três estados do bloco de compra. **A F1 reusa o mesmo
cartão**, então os dois lugares que servem produto nesta ilha desceram a escada de uma vez:

1. **Com ficha** — a ficha é o botão ("Ver na loja") e a busca desce para a linha discreta
   "Veja todos disponíveis aqui", palavra por palavra como a 25.2 a escreve. As duas convivem
   de propósito: ficha converte melhor, e a busca é a saída de quem chegou num anúncio
   esgotado. O degrau 3 é justamente o que quebrou quatro links em doze horas em 13/09.
2. **Só com busca** — a busca **sobe e vira o botão**, com texto próprio: "Ver as opções na
   loja". O texto muda junto com o papel, e não por estilo: o botão abre uma **lista**, e
   prometer "Ver na loja" ali seria o leitor clicar esperando a ficha do que a página acabou
   de recomendar.
3. **Sem nada** — sobra "Link de loja em breve", e ele deixa de ser estado de espera para ser
   **defeito contado**.

**Por que é função própria e não um `if` dentro do cartão:** a escada é regra do Arquipélago
e o cartão é desenho da ilha. Quem for servir a vitrine de pastilha da F1, a ficha do Guia ou
a página da peça **chama a função** em vez de reescrever quatro degraus que discordariam em
silêncio. O portão mede isso contando a **classe emitida** nos snippets — e não a frase
legível, porque a primeira versão dessa régua contou a frase e reprovou o próprio comentário
que a explica.

### Os três mundos produzidos, e por que `sem_links=1` mudou de significado

O banco de hoje só produz o estado 1, então medir os outros dois no banco de hoje seria medir
o caminho que nenhum cartão percorre — verde com a função quebrada, e o dia em que importasse
seria o dia em que um link morresse.

`sem_links=1` **apaga a ficha e deixa o piso de pé**, que é exatamente o estado 2. Até a
1.1.0 esse mundo produzia "em breve"; depois da 1.2.0, produzir "em breve" nele **é o
defeito**. A afirmação antiga reprovou na primeira rodada, e essa reprovação é a mudança
funcionando. Nasceu `sem_piso=1` para o vazio de verdade.

**A ordem das três réguas importa, e é o que as torna três:** (a) sozinha passaria numa
função que ignora a ficha e serve só a busca; (b) sozinha passaria numa que serve a busca por
cima da ficha; e (c) pega o erro mais provável de quem escreve isto com pressa — deixar o "em
breve" no lugar do piso —, **o único que (a) e (b) aprovariam juntas.**

### O banco aprende o que a seção 25 criou

O esquema não conhecia `url_produto`, `url_busca`, `url_busca_produto`, `degrau` nem
`conferido_em`, e a observação dele ainda mandava a página dizer "em breve" e declarava que
gerar link *"é da Sentinela estratégica, no navegador, e nunca da Fundação"*. As duas frases
são **anteriores à 25.2** e foram **reescritas, não acrescentadas**: deixadas ali, o esquema
contradiria o campo vizinho, e contradição no dado é pior que lacuna porque tem cara de
decisão. O `validar-banco.py` passa a exigir `url_produto` de quem tem link (25.4-b: link
cuja saúde ninguém consegue conferir), a cobrar o degrau, e a **contar** os itens sem piso num
campo novo de cabeçalho, `itens_sem_piso`, reconferido contra o arquivo.

**Os dez sem piso são as pastilhas, e o motivo é medido e não suposto.** Gerar o link de busca
exige a **sessão logada** do painel de afiliado da Shopee, que mora no navegador do Raphael.
Desta nuvem o `custom_link` responde **200 em duas passadas** e serve uma casca de JavaScript
**sem o formulário** — zero ocorrência de `custom_link` e de `sub_id` no HTML servido. **Não é
bloqueio de rede** (a seção 4 manda testar duas vezes antes de chamar de bloqueio, e o teste
foi feito): é falta de sessão, e criar conta ou tocar na conta dele está fora do que esta
camada faz. **Não virou erro duro do validador de propósito** — portão vermelho que ninguém
consegue fechar é portão que se aprende a ignorar; contado e declarado, ele é o número que a
ilha reporta em todo bloco, que foi exatamente o desenho que fez os dez links nascerem em
13/09. **No dia em que os dez `url_busca` forem colados, nenhuma linha de código muda.**

### Uma mutação antiga tinha virado inerte em cada bateria, e inerte conta como passou

O alvo das duas era a linha que **abria** o `<span>` do bloco de compra dentro do cartão, e a
refatoração mudou o vizinho: a abertura desceu para a função nova. As duas acharam zero
ocorrência e foram contadas como PASSOU. É a mesma família da mutação 24 desta ilha em 12/09
— **alvo que depende da vizinhança morre quando o vizinho se muda.** As duas apontam agora
para a **chamada** da função, que é o que governa a ordem hoje.

### Um achado de outra ilha, fechado

A ronda da Aquametria de 13/09 escreveu, por não haver outro canal, que o endpoint de cópia da
seção 24 desta ilha **existia** e devolvia 401, mas que o nome do parâmetro de autenticação
não estava documentado em lugar nenhum — então a cópia da 24 não acontecia e não ia acontecer.
O parâmetro é `token` e o valor é **o mesmo token do Sync**. A URL completa e literal entrou em
"Endpoints desta ilha", conferida desta nuvem: HTTP 200, `{"total":0,"pecas":[]}`. **Zero peça
é resposta, não falha** — o `dados/pecas.json` nasce no dia em que a artesã cadastrar a
primeira.

### A regra nova que subiu para o contrato (seção 1.1)

A 1.1 manda descartar a ilha com commit na pasta nos últimos 40 minutos e **não diz commit de
quem**. Lida ao pé da letra, ela manda a Fundação ignorar por 40 minutos exatamente a ilha que
a **Sentinela** acabou de tocar — que é a ilha com despacho novo, a primeira da 18.1. As duas
regras se contradiziam. O que a 1.1 mede é **execução da Fundação viva**, e `executando_desde:
null` já prova que não há bloco em andamento, **porque a reserva é escrita antes do trabalho**.

### Verificação

**Bancada, 0 falha:** `teste-f2` 87 afirmações (era 74), `teste-f1` 72 (era 70), `teste-casca`
546, `teste-loja` 147, `teste-leads` 211, `teste-atelie`, `teste-prestacao-rejunte` 5 sobre
720 estados, `conferir-cobertura` 128, `validar-banco` APROVADO, `php -l` em tudo.
**Mutações:** f2 **26 de 26** reprovadas, f1 **27 de 27**, **0 inertes** nas duas depois do
conserto dos dois alvos. **Navegador:** 63 medições em 9 páginas × 6 larguras, 0 px de
rolagem, console limpo — e entre as nove está o **mundo produzido em que a busca é o botão**,
porque alvo de toque de botão novo não se mede no mundo onde ele não aparece.

**No ar às 15h40Z, em UM disparo:** `/status` na revisão **23**, igual à do `manifest.json`, 10
aplicados; `conferir-no-ar` **351 afirmações, 0 falha**, com a escada medida **cartão a cartão
no HTML servido** (6 cartões na F2 e 2 na F1, todos com as duas portas) e a marca do código
novo — a classe `cdm-f2-busca` — no corpo servido, que é a diferença entre "o manifest diz que
subiu" e "o site está servindo".

**A primeira versão dessa régua no ar reprovou a página certa**, e vale registrar: ela comparou
as linhas discretas da tela com o número de itens do **banco**, e a âncora serve 6 cartões de
um banco de 10 porque publica um **caso de referência**, não o catálogo. Régua de página medida
com régua de banco. O banco continua na medição, mas no papel certo: dizer o que a tela **não
pode** ter.

**PRÓXIMO, com ordem e motivo:** (1) a ordem de BANCO que já estava escrita e **agora não tem
mais nada na frente** — fechar 2×2 na categoria pastilha, que está a UM item dos 3 da 14.3,
depois a vitrine de pastilha da F1, que já nasce com a escada pronta, depois a categoria cola;
(2) os dez `url_busca` das pastilhas, no minuto em que houver sessão — é copiar e colar no
banco, sem uma linha de código; (3) o feed do Merchant Center, que é espera e não escolha de
fila. O que só um humano fecha continua o mesmo: confirmar que o e-mail de acesso chegou na
caixa da Hotmail, e o `contato@clubedomosaico.com.br` que ainda não existe como caixa.

13/09/2026 17:50Z — O 2×2 FECHA O MÍNIMO DA 14.3, E A FAIXA SOBRE A QUAL A COBERTURA ERA PUBLICADA ESTAVA FALTANDO UM TAMANHO

- **Por que este bloco.** Era a ordem de banco que o estado anterior deixou escrita
  e que não tinha mais nada na frente: fechar 2×2 na categoria pastilha, que estava
  a UM item dos 3 da seção 14.3. Nenhum despacho aberto nesta ilha, nenhum defeito
  da 19.1 registrado pela ronda. **Nenhuma URL nova, nenhum snippet reescrito,
  nenhuma página criada** — manifest na revisão **24**.

- **As três fichas que o bloco 3d deixou pela metade entraram inteiras**, e a
  pendência `pastilha-fichas-colhidas-pela-metade` está FECHADA: **A37** (2×2,
  placa 32,3, 3 mm, 20 placas, 2,086 m², 13 kg), **102** (2,5×2,5, placa 31,7,
  4 mm, 20 placas, 2,01 m², 18 kg) e **IC02** (2,3×2,3, placa 30,0, 8 mm, 10
  placas, 0,9 m², 16 kg). O banco vai de 10 para **13** itens, e **a A37 é o
  terceiro elegível de 2×2**: o tamanho passa de 2 para 3 e cumpre o mínimo da
  14.3. Era o único buraco de cobertura desta ilha que dependia de coleta e não
  de decisão.

- **Coleta.** Busca restrita ao domínio, **duas passadas por SKU** com consultas
  escritas de forma diferente e **nenhuma delas carregando um valor** — as duas
  pediram os rótulos da ficha. As três voltaram idênticas nas duas. O egresso foi
  remedido antes, como a 20.2 manda: `glassmosaic.com.br` e `www.pastilhart.com.br`
  em 000 por `connect_rejected` (política) em duas passadas, com
  `clubedomosaico.com.br` em 200 nas mesmas duas. Por isso `conferir_no_pdf: true`
  nos três, como nos dez anteriores.

- **O ACHADO DO BLOCO NÃO É DO DADO — É DO PRÓPRIO PORTÃO, e ele muda o que a ilha
  vinha publicando sobre si mesma.** O `validar-pastilhas.py` carregava os tamanhos
  da F1 numa constante de **quatro** linhas, com o comentário "os tamanhos que a F1
  oferece". **A F1 oferece cinco:** `cdm_f1_pastilhas_disponiveis()` serve 1×1,
  **1,5×1,5**, 2×2, 2,5×2,5 e o caquinho irregular. A cópia nasceu certa e
  envelheceu calada.

  **O custo não era cosmético.** A seção 14.3 manda varrer "a faixa de entrada de
  cada ferramenta de ponta a ponta", e a cobertura saía publicada sobre quatro
  linhas de uma faixa de cinco: **um tamanho que a ferramenta serve nunca apareceu
  no relatório do buraco.** E logo esse — 1,5 cm é o lado do `pastilhart-af1500`, o
  único item do banco sustentado por distribuidor (nível 5). A **mutação 07** desta
  bateria diz, com todas as letras, que promover o distribuidor "faz 1,5 cm passar
  de zero para um elegível": uma afirmação sobre uma linha que o relatório não
  tinha. Ela reprovava pelo nível na régua por item, e a outra metade nunca foi
  medida.

- **Nasce `ferramentas/tamanhos-da-f1.php`**, irmão do `faixa-da-f2.php`. Ele **não
  lê o código: provoca a ferramenta.** As chaves saem de
  `cdm_f1_pastilhas_disponiveis()`, que é a declaração da própria F1, e cada uma
  passa por `cdm_f1_entrada()` — a MESMA função que saneia a consulta de quem
  visita — para provar que sobrevive ao saneamento. As duas metades falham por
  motivos diferentes: tamanho que a tela lista e o saneamento derruba é tamanho que
  a ferramenta não aceita. **8 afirmações, com a borda dentro delas:** uma chave
  inventada tem de ser recusada, e o padrão do saneamento tem de ser um tamanho que
  a tela lista. É a mesma família do "número de tela nasce contado, nunca digitado"
  da seção 8 e da lista de tipos que a Robometria tirou de dentro da régua hoje de
  manhã pela seção 26: **lista dentro da régua envelhece calada, e o sintoma é o
  portão verde.**

- **As duas primeiras mutações de CÓDIGO desta bateria (13 e 14)** nasceram junto, e
  existem porque a bateria só sabia mexer no banco — portão que só mede o dado não
  vê o defeito que mora na régua. A 13 faz o padrão do saneamento cair num tamanho
  que a tela não lista; a 14 faz o saneamento aceitar qualquer chave. As duas
  **produzem um mundo que o banco não tem como produzir**, que é o que a seção 8
  exige de quem escreve régua nova, e as duas reprovaram.

- **O que os três itens ensinaram sobre o catálogo.** (1) O **102** tem a mesma
  pastilha anunciada de 2,5 cm dos três K e placa de **31,7** contra 30,0 — prova,
  dentro do catálogo de um fabricante só, de que **o lado da placa não se deduz do
  lado da pastilha**; quem completasse um campo pelo vizinho de mesmo tamanho
  erraria 1,7 cm por placa. O próprio endereço o classifica em `uncategorized`,
  então o nome comercial não carrega linha: inventar uma seria atribuir ao
  fabricante uma classificação que ele não publicou. (2) O **IC02** é o único item
  do banco cuja aritmética de ficha fecha **exata** (10 × 30 × 30 = 0,90 m², sem
  corte nem arredondamento), e o lado dele, 2,3 cm, não é nenhum dos cinco do
  seletor — como já acontecia com 3,0, 1,5 e 1,2. Virou pendência nova,
  `pastilha-tamanho-fora-do-seletor-da-f1`: **6 dos 13 itens** têm lado que a F1 não
  oferece, e o que eles medem não é defeito de coleta, é o quanto o seletor é mais
  pobre que o mercado. (3) A **A37** fecha a metragem por CORTE (2,086) e a irmã A61
  por ARREDONDAMENTO (2,09) na mesma caixa — a régua já aceitava exatamente as duas
  operações e diz qual foi usada em cada item, então a A37 entrou sem uma linha nova
  de tolerância.

- **Receita, e o número PIOROU de propósito.** `itens_sem_piso` sobe de 10 para
  **13**, contado do arquivo pelo validador e nunca digitado. Os três novos entram
  sem `url_busca` pelo mesmo motivo medido ontem e hoje: gerar o link de busca exige
  a **sessão logada** do painel de afiliado da Shopee, que mora no navegador do
  Raphael, e isso não é bloqueio de rede. **Inventar um endereço para o contador não
  subir seria trocar defeito contado por defeito escondido.** No dia em que os treze
  forem colados, nenhuma linha de código muda — a escada de ontem já serve os três
  estados.

- **VERIFICAÇÃO NA BANCADA, 0 falha:** `validar-pastilhas` **189 afirmações** (era
  139) em 13 itens, um processo cada, 8 delas vindas da faixa medida na F1;
  `validar-banco` APROVADO com 23 materiais; `cobertura` 128; `teste-casca` 546;
  `teste-f2` 87; `teste-f1` 72; `teste-loja`, `teste-leads` e `teste-atelie`
  aprovados; `prestacao-rejunte` 5 sobre 720 estados; `php -l` em tudo.
  **MUTAÇÕES:** pastilhas **14 de 14** (12 no banco e as 2 novas no código), 0
  inertes; cobertura **14 de 14**, 9 que só a varredura vê; f1 **27 de 27** e f2
  **26 de 26**, 0 inertes nas duas — as antigas rodadas inteiras para provar que
  nenhuma morreu com o banco maior. **NAVEGADOR:** 63 medições em 9 páginas × 6
  larguras, 0 px de rolagem, console limpo, e a passada com o JavaScript
  **desligado** (portão 22.8) inteira.

- **As baterias que esta execução NÃO rodou, ditas pelo nome:** prestação, árvore,
  loja, leads, ateliê, rejunte, voz-e-cabeça e ga4. Elas medem superfícies que este
  bloco não tocou, e a de prestação sozinha passa de vinte minutos (720 estados por
  mutação). Ficam para quem mexer naquelas superfícies. Dizer quais é o mínimo:
  "rodei as mutações" sem a lista é a mesma promessa vazia que o número digitado.

- **NO AR às 17h47Z, em DOIS disparos**, e o primeiro é o caso que a seção 4
  documenta: às 17h42Z o Sync leu um manifest ainda na revisão 23 **enquanto já
  baixava o banco novo** e recusou com `"materiais-pastilhas: sha256 divergente —
  não aplicado"`. A trava fez o que devia; o segundo disparo aplicou. `/status` na
  **revisão 24**, igual à do manifest. `conferir-no-ar` **351 afirmações, 0 falha**,
  com a prestação de contas do banco medida no HTML SERVIDO: a página do Guia serve
  **"23 itens de fabricante, sendo 5 colas, 5 rejuntes e 13 pastilhas, e 13 deles
  ainda esperam link"** — total batendo com a soma dos arquivos do repositório,
  parcelas somando o total que a própria frase publica, e toda categoria com arquivo
  de banco nomeada.

- **ABERTO E NOMEADO:** (a) os 13 `url_busca` das pastilhas, que dependem da sessão
  do painel da Shopee; (b) `url_busca_produto` em 10 de 10 itens com busca (25.4-b)
  — a URL crua se perdeu e não se recupera sem clicar; (c) **1×1 continua com ZERO**
  e é o tamanho de 7 das 12 linhas da tabela pré-renderizada da F1 — não existe em
  catálogo de fabricante, só em armarinho e marketplace vendido a peso, e é a
  pendência mais cara da categoria; (d) **1,5×1,5 aparece pela primeira vez no
  relatório e sai com ZERO**, porque o único item daquele lado é de nível 5; (e)
  peças por placa segue null nos 13, agora com 9 de 13 sem divisão inteira; (f) a
  ilha não tem peça publicada, então ficha, formulário no ar e feed do Merchant
  Center continuam esperando a artesã; (g) `contato@clubedomosaico.com.br` ainda não
  existe como caixa. Pauta da seção 17: `pauta.md` ainda não existe — 0 escritos, 0
  na fila, 0 recusados.

- **PRÓXIMO, com ordem e motivo:** (1) **a vitrine de pastilha da F1**, que agora não
  tem mais nada na frente e ficou mais barata do que estava —
  `cdm_f1_pastilha_sem_banco_html()` ainda diz "ainda não temos as pastilhas no
  nosso banco", o 2×2 e o 2,5×2,5 têm os 3 elegíveis da 14.3 para servir, a escada
  de compra já está pronta, e a faixa por onde ela vai filtrar agora é **medida** em
  vez de digitada; falta decidir o que a tela diz nos três tamanhos que continuam em
  zero e nos 6 itens cujo lado o seletor não oferece, que é a pendência nova; (2) a
  categoria **cola**, que é a faixa mais descoberta da ilha (45 estados varridos, 0
  com o mínimo, teto de 2 elegíveis); (3) os 13 `url_busca`, no minuto em que houver
  sessão — é copiar e colar no banco, sem uma linha de código.

---

## 13/09/2026, 19h17–20hZ — A VITRINE DE PASTILHA DA F1 (f1 1.2.0, manifest revisão 25)

**Terceira ilha tentada nesta execução, de novo, e de novo é a seção 1 funcionando.** A
aquametria foi reservada às 19h18Z e a robometria às 19h16Z por outras duas execuções — o meu
push da reserva da aquametria foi recusado por cerca de um minuto, e o da robometria também.
O passo 5 manda voltar ao passo 2 e escolher a próxima da ordem; sem force push, sem atropelo.
Antes de escolher, conferi os três `PROMPT.md`: **nenhuma ilha tem despacho aberto para a
Fundação** (a 18.1 não se aplicou), então valeu a rotação normal da seção 1.

**O bloco é o item (1) que a execução anterior desta ilha deixou escrito**, e ele não tinha
mais nada na frente: *"a vitrine de pastilha da F1 — `cdm_f1_pastilha_sem_banco_html()` ainda
diz 'ainda não temos as pastilhas no nosso banco'"*.

### O defeito era de OMISSÃO, e ele tinha data

A frase nasceu verdadeira em 11/09/2026. Em **12/09** o bloco 3d gravou dez pastilhas; em
**13/09** entraram outras três. O arquivo está com `publicar: true` desde 12/09, a casca lê
ele em `cdm_casca_numeros()` e o cartão do Guia publica a contagem — e **nenhuma linha de
código da F1 abria o banco**. Dado no banco e tela sem leitor é o mesmo defeito que a F2
tinha com o `url_busca` até 13/09 de manhã; aqui era mais caro, porque esta é a ferramenta
cuja pergunta **é** "quantas pastilhas comprar", e ela respondia sem ter o que vender.

### O que decide uma pastilha não é o que decide uma cola

Primeira coisa que o código novo declara, e é a cicatriz da "categoria nova herda a régua da
antiga em silêncio" (seção 8), que esta ilha já pagou quando o primeiro rejunte fez as 18
células da cola falharem de uma vez. A cola se escolhe por base × ambiente; o rejunte, pela
folga. **A pastilha entrou no banco pela GEOMETRIA** — o próprio arquivo diz isso e diz por
quê: o fabricante não nomeia substrato nem ambiente na ficha dela. Então a elegibilidade tem
três travas, **nesta ordem**, e a ordem é o que faz cada frase de recusa poder ser verdadeira:

1. **o LADO** (o que a pessoa escolheu, ou digitou no caquinho irregular);
2. **o FORMATO** — o seletor oferece pastilha quadrada e o banco tem um strip retangular de
   1,2 cm. Quem cai aqui já passou pelo lado, então "o lado é o mesmo" não é suposição;
3. **a FONTE** — nível <= 3 pela escada do esquema. É por isso que **1,5 cm sai com ZERO
   tendo um item**: a causa é a fonte (distribuidor), não o tamanho, e a tela diz qual das duas.

**Prestação de contas (seção 7):** as quatro listas são disjuntas e somam o banco inteiro,
contado do arquivo. Todo item aparece **uma vez** — no cartão que o recomenda ou numa linha
que diz por que ele não está. Uma frase por causa, cada uma nomeando quem caiu por ela.

### A PENDÊNCIA DO SELETOR FECHOU POR UM TERCEIRO CAMINHO — e o número dela estava errado

O banco abriu em 13/09 a pendência `pastilha-tamanho-fora-do-seletor-da-f1` dizendo **6 dos
13**. São **5**. Ela listava o AF1500 de 1,5 cm entre os lados que o seletor não tem, porque
foi escrita a partir da frase "a F1 oferece quatro tamanhos — 1x1, 2x2, 2,5x2,5 e a tessela
irregular". **A F1 oferece cinco, e o quinto é justamente 1,5 cm** — foi esse o defeito que
`ferramentas/tamanhos-da-f1.php` achou na régua de manhã, e **a prosa da pendência herdou a
mesma lista vencida no mesmo dia**. Lista digitada envelhece calada em qualquer arquivo,
inclusive num que descreve o problema. Os cinco são os três K de 3,0 cm, o ST5102 de 1,2 cm e
o IC02 de 2,3 cm, contados do cruzamento do banco com `cdm_f1_pastilhas_disponiveis()`.

A pendência propunha duas saídas e **nenhuma das duas foi tomada**: opção nova no seletor
prometeria cobertura da 14.3 que não existe, e servir tamanho aproximado seria recomendar 3,0
a quem pediu 2,5 com a conta de 2,5. Havia um terceiro caminho, e ele **já estava construído**:
o campo do **caquinho irregular** aceita qualquer lado de 0,3 a 10 cm e é o único da
ferramenta em que o lado é digitado. A vitrine casa pelo lado em milímetros, então quem digita
3 recebe os três K de 3,0 cm com a conta do próprio lado dele. A tela nomeia os lados que o
seletor não lista e manda a pessoa para lá.

### O CARTÃO FALA EM PLACA, E ISSO É ESCOLHA DECLARADA

Converter "N pastilhas" em "M placas" exigiria quantas pastilhas vêm na placa, e **nenhum dos
treze fabricantes publica**: a divisão ingênua não fecha em 9 dos 13 e, nos outros 4, fecha
exigindo folga zero — placa que não se rejunta. Área, sim, se converte sem supor nada: a
placa cobre o próprio tamanho, seja qual for o arranjo das peças dentro dela. Então o cartão
diz quantas **placas** a peça pede, com a sobra escolhida dentro e arredondando para cima
pelo mesmo motivo da contagem de peças — e a página diz, na cara, que a peça ela não converte.

### A ESCADA DA SEÇÃO 25 FOI CHAMADA, NÃO COPIADA

`cdm_f2_compra_html()` nasceu em 13/09 dizendo, no próprio comentário, que a vitrine de
pastilha da F1 a chamaria em vez de reescrevê-la. Foi o que aconteceu. Hoje os treze caem no
**terceiro** degrau — sem ficha e sem piso —, e isso é defeito declarado da 19.1, não estado
de espera: o cartão reserva o lugar, e o número está contado no banco (`itens_sem_piso: 13`).

### A TABELA PRÉ-RENDERIZADA EXISTE POR UM MOTIVO ARITMÉTICO

O estado-âncora desta página é caquinho de **1 cm**, e 1 cm tem **zero** elegível. Sem a
tabela do banco inteiro, a única URL indexada desta ferramenta — a sem parâmetro, a que o
Google e as IAs leem — **não citaria um único produto do nosso catálogo de pastilha**. A
vitrine responde a quem escolheu um lado; a tabela responde a quem só chegou. Treze linhas,
cada item uma vez, com uma coluna "está no formulário?" que publica a cobertura da 14.3 item
por item, em vez de a deixar só na bancada.

E a frase que explica o zero de 1 cm — "não aparece em catálogo de fabricante nenhum; quem
vende é armarinho e marketplace, a peso ou por peça solta" — **só sai no lado de 1 cm e só
quando ele está vazio**. Ela é verdadeira hoje, e é isso que a tornava perigosa.

### A BANCADA, E O QUE ELA ACHOU NELA MESMA

`teste-f1.php` foi de **72 para 182 afirmações**, 0 falha. A régua da classificação é escrita
**neste arquivo**, em PHP, lendo `dados/materiais-pastilhas.json` do disco — não chama nenhuma
função do snippet. A grade varre os cinco tamanhos do seletor, os três lados que só o caquinho
irregular alcança e um lado que não existe em ninguém, um processo por estado.

`mutacoes-f1.py` foi de 27 para **40 mutações, 40 reprovadas, 0 inertes**. A primeira rodada
teve **três que passaram, e as três eram resultado**:

1. **"vão maior que a moldura passa e a área fica negativa"** reprovava desde 12/09 e passou a
   escapar **por causa deste bloco**: a afirmação procurava "não fecha" no corpo INTEIRO, e a
   camada de prova nova passou a dizer que a divisão do lado da placa "não fecha" em quase
   todos os itens. A agulha foi encontrada numa seção que nada tem a ver com a recusa — o mesmo
   defeito que a seção 8 registra como "a conferência achava o texto dentro do próprio
   JSON-LD". Ela passou a medir **no bloco da resposta**. E a afirmação vizinha tinha um furo
   mais antigo: `-\d+ cm²` nunca casaria com **"-1.100 cm²"**, que é exatamente o que a página
   serve quando a guarda cai. Só pegava área negativa de três dígitos.
2. **"as placas esquecem a sobra"** passou porque a grade não pisava na borda: no vaso de
   15 × 20 a sobra de 10% não muda o número de placas, e o `ceil` engole a diferença. Nasceu a
   seção **4c**, com uma peça de 44,5 × 40 cm escolhida para a sobra atravessar o degrau (2 / 2
   / 3 placas em 0 / 10 / 20%) — e uma afirmação que cobra que os degraus sejam **diferentes**,
   senão a peça escolhida não mediria a sobra.
3. **"a frase do 1 cm passa a sair sempre"** passou porque nada media o ESCOPO dela. Ela é
   verdadeira no lado de 1 cm e seria uma afirmação sobre um mercado que ninguém olhou em
   qualquer outro lado. Agora a régua cobra que ela saia **se e somente se** o lado pedido é
   10 mm e ele está vazio.

**TRÊS MUNDOS NOVOS no `render-para-teste.php`**, e cada um existe porque o banco de hoje não
consegue produzir o caso — "todo caso que o ESQUEMA permite e o banco ainda não tem é um caso
que a régua precisa tratar hoje" (seção 8):

- **`com_piso=1`** escreve `url_busca` em quem não tem. Sem ele, a mutação que faz o cartão de
  pastilha **reimplementar** a escada em vez de chamar `cdm_f2_compra_html()` produz uma tela
  **idêntica byte a byte** — os treze estão sem piso, então os dois caminhos caem no terceiro
  degrau. A cópia só mentiria no dia em que o Raphael colasse os links, com um portão verde ao
  lado. Essa mutação reprova **só** neste mundo.
- **`strip_fraco=1`** rebaixa a fonte do único item não quadrado para nível 5, fazendo-o cair
  pelas DUAS travas. É o único jeito de provar a ORDEM declarada: com um item por balde,
  qualquer ordem produz a mesma tela.
- **`um_de_1cm=1`** clona um item para o lado de 1 cm e exige que a frase do mercado
  desapareça.

**Navegador:** 83 medições em 13 páginas × 6 larguras (360, 390, 781, 782, 783, 1200), **0 px
de rolagem lateral** nos três estados novos da F1, console limpo, contraste de 12,97:1 a
21:1, e a passada com o **JavaScript desligado** inteira (portão 22.8) — a vitrine é servida
pelo servidor e não tem uma linha de decisão em JavaScript.

**Outras baterias rodadas inteiras, 0 falha:** casca 546, f2 87, loja 147, leads 211, atelie
aprovado, cobertura 128, validar-pastilhas 189, validar-banco aprovado, `php -l` em tudo. As
que NÃO rodaram, e vale dizer quais: prestação de rejunte (720 estados, passa de vinte
minutos), árvore, rejunte, voz-e-cabeça, ga4 e as mutações de pastilhas, cobertura, f2, loja,
atelie e leads — elas medem superfícies que este bloco não tocou.

**NO AR às 19h54Z, em UM disparo.** `/status` na revisão **25**, igual à do manifest, 10
aplicados. `conferir-no-ar.py` foi de 351 para **365 afirmações, 0 falha**, medidas no HTML
SERVIDO depois do Sync — a tabela do banco com 13 linhas e os treze códigos, o estado-âncora
dizendo que não tem 1 cm com a causa, o estado de 2 cm com três cartões nomeados e o lugar do
link reservado nos três, e o caquinho irregular de 3 cm alcançando os três K que o seletor não
lista. A régua dele também é própria: os treze códigos estão escritos literais no arquivo.

**Um detalhe do próprio commit, para não parecer descuido:** o nome da pendência entre acentos
graves foi comido pelo shell na mensagem de commit, e a linha saiu "fecha a pendencia  —".
Não há force push nesta fábrica (seção 3), então a mensagem fica como está; o nome é
`pastilha-tamanho-fora-do-seletor-da-f1` e a história inteira está acima.

**ABERTO E NOMEADO, ao fim deste bloco:** (a) os **13** `url_busca` das pastilhas, que dependem
da sessão logada do painel de afiliado da Shopee — no dia em que forem colados, **nenhuma linha
de código muda**, e o `com_piso=1` já prova que a tela sabe subir o degrau; (b) `url_busca_produto`
em 10 de 10 itens com busca (25.4-b); (c) **1x1 continua com ZERO elegível** e é o tamanho de 7
das 12 linhas da tabela pré-renderizada da F1 — agora a página diz isso na cara, mas o buraco
é o mesmo e é o mais caro da categoria; (d) 1,5x1,5 sai com zero por FONTE, não por tamanho;
(e) peças por placa segue null nos 13, e é a pendência que faz o cartão falar em placa; (f) a
ilha não tem peça publicada, então ficha, formulário no ar e feed do Merchant Center continuam
esperando a artesã; (g) contato@clubedomosaico.com.br ainda não existe como caixa.

**Pauta da seção 17:** `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.

**PRÓXIMO, com ordem e motivo:** (1) **a categoria COLA**, que é a faixa mais descoberta da
ilha — 45 estados varridos, **0 com o mínimo** da 14.3, teto de 2 elegíveis; é a única
categoria em que a ferramenta responde e o banco não tem o que vender, e agora não tem mais
nada na frente. (2) **A ORDEM DAS DUAS VITRINES na F1**: hoje "Qual rejunte cabe nessa folga"
vem antes de "E onde comprar a pastilha", ordem herdada de quando o bloco da pastilha era uma
frase de espera. O H1 da página nomeia a pastilha primeiro e a resposta também; mover é
decisão de desenho e merece bloco próprio, não um `swap` no meio de outro. (3) **1x1 de
fabricante**, que é a pendência mais cara da categoria pastilha — a busca alcança os domínios,
o egresso é que não. (4) os 13 `url_busca`, no minuto em que houver sessão: é copiar e colar.

### O ACHADO QUE NÃO ERA DESTE BLOCO: o cabeçalho de estado não é YAML válido

Ao validar o próprio cabeçalho antes de fechar (porque ele ficou grande e eu quis ter certeza),
descobri que **a seção 2 do contrato manda o cabeçalho ser YAML e nada nunca conferiu que ele
PARSEIA**. Passando os três `ESTADO.md` do arquipélago por `yaml.safe_load` às 19h58Z:
**dois dos três estavam quebrados**. A causa é a mesma e nasceu do crescimento saudável do
arquivo — o `bloco_atual` passou de `"4c"` para prosa de milhares de caracteres entre aspas
duplas, e aspas duplas dentro de um escalar de aspas duplas derrubam o documento; uma barra
invertida solta também, porque `\d` é escape desconhecido em YAML de aspas duplas.

- **clubedomosaico**: estava inválido e foi consertado no mesmo commit (aspas internas viraram
  simples, e a regex citada saiu por extenso).
- **aquametria**: inválido, na coluna 1910 do `bloco_atual`. Reservada por outra execução às
  19h18Z, e a seção 3 proíbe editar ilha que não se reservou → virou **despacho** em
  `dados/despachos.md`.
- **robometria**: válido.

Ninguém tinha visto porque quem lê o cabeçalho hoje é a Fundação, com `grep` e com o olho, e as
duas coisas atravessam YAML quebrado sem reclamar. **Cabeçalho que só o olho lê é cabeçalho sem
portão.** A metade que vale para toda ilha foi escrita onde regra nova mora, uma vez: a
**seção 2 do `ARQUIPELAGO.md`**, com o comando de uma linha e a convenção de aspas simples.

13/09/2026 21:19Z — BLOCO 3e ENTREGUE: A CATEGORIA COLA GANHA OS DOIS PRODUTOS DAS FAIXAS DE ZERO, E A F2 APRENDE A CONDIÇÃO DE SUPERFÍCIE (regra 6)

**A ilha desta execução foi a terceira tentativa.** A robometria foi reservada às
21h16Z por outra execução — o push da minha reserva foi recusado por cerca de um
minuto, o passo 5 da seção 1 manda voltar ao passo 2, e nenhum force push
aconteceu. Antes de escolher, os três `PROMPT.md` foram lidos: **nenhuma ilha
tinha despacho aberto para a Fundação**, então a 18.1 não se aplicou e valeu a
rotação da seção 1. A clubedomosaico era a de `ultima_execucao` mais antiga entre
as livres (19h17Z), com prioridade 1.

**O QUE ESTE BLOCO FOI BUSCAR, e estava escrito no `ESTADO.md` desde as 19h17Z:**
a categoria COLA era a faixa mais descoberta da ilha. O censo da seção 14.3 media
**45 estados, 0 com o mínimo de 3 elegíveis, teto de 2**. Era a única categoria em
que a ferramenta responde e o banco não tinha o que vender.

## A rede, medida antes de trabalhar (seção 20.2)

`clubedomosaico.com.br` e o `/status` em 200. O egresso a fabricante segue
fechado e foi **remedido em duas passadas** antes de ser respeitado, como manda a
seção 4: `quartzolit.weber`, `tekbond.com.br`, `cascola.com.br`, `henkel.com.br`,
`bra.sika.com` e `brascola.com.br` responderam `000` nas duas, com o domínio da
ilha em 200 como controle na mesma janela. O WebFetch devolveu `EGRESS_BLOCKED`
para o mesmo domínio. **O canal que sobrou é exatamente o que a escada de fontes
do esquema chama de nível 2 e 3: busca restrita ao domínio do fabricante, sem
abrir o PDF** — e foi por ele que os dois produtos entraram.

## Os dois produtos, e por que cada um fecha uma faixa

**Tekbond Silicone Acético Maxx (BRSA005)** — o primeiro produto do banco que
pode ser **recomendado em contato permanente com água**. Até hoje essa faixa
tinha zero elegíveis nas nove bases, e a única declaração de colagem submersa da
ilha era press release de 2018 (`loctite-durepoxi`, nível 4, abaixo do mínimo de
3). A declaração de aquário e piscina está na página de produto do fabricante,
nível 3, e cumpre a regra 4 (ambiente crítico exige declaração explícita).

**Cascola Adesivo de Montagem PL500 Interior** — o primeiro indicado **sobre
plástico**. O único que falava de plástico dizia "certos tipos de plástico", que
não nomeia tipo nenhum e por isso nunca virou indicação; aqui o fabricante lista
"plásticos" sem qualificador.

**O QUE FOI RECUSADO DE PROPÓSITO, nos dois:**

- No Maxx, **vidro NÃO entrou**. É um silicone de aquário e aquário é de vidro, e
  a tentação de traduzir "fabricação e reparo de aquários" em base VIDRO é a
  heurística por vizinhança que a seção 8 proíbe. "Aquários" é aplicação e entra
  como AMBIENTE, que é o que ela mede. As outras oito bases seguem descobertas
  dentro da água, e a página diz isso.
- No PL500, a frase *"ideal para adesão de rodapés, peças decorativas, azulejos,
  ladrilhos, molduras, canaletas, cantoneiras, maquetes, mosaicos"* **não entrou
  em `indicado_para`**, embora contenha "azulejos", que o mapa traduz como BASE.
  É a lista do que se COLA, nunca a do que se cola SOBRE — o mesmo erro que este
  banco já pegou na cimentcola AC-II. **"Mosaicos" está escrito lá pelo próprio
  fabricante e mesmo assim não virou declaração de substrato: virou citação.**

## A regra 6, e por que ela precisou existir

O PL500 declara **"ao menos uma das superfícies deve ser porosa, já que o produto
seca por evaporação da água"**. Isso não é base e não é ambiente: é o **PAR de
superfícies coladas**. Sem tratá-la, a página mandaria colar pastilha de vidro em
vaso de plástico com um adesivo que não teria por onde curar — recomendar em
primeiro lugar um produto que a própria página diz não servir, que a seção 7
chama de defeito GRAVE.

Nasce a **regra 6 do esquema (versão 3)**: a primeira régua de cola que olha o
CAQUINHO. A entrada existia desde a F2 1.0.0 e nenhuma régua de cola a lia — o
mesmo defeito que a F1 tinha com o banco de pastilhas e a F2 com o `url_busca`.

**TRÊS DECISÕES DECLARADAS NO CÓDIGO:**

1. **A ordem.** A condição roda DEPOIS das cinco e ANTES da ordenação por score.
   Rodar depois da ordenação deixaria célula sem topo com elegíveis na mão: em
   `vidro` + `caquinho de espelho` o produto com condição é o PRIMEIRO colocado,
   e quem sobe no lugar dele são os dois silicones que estavam abaixo. É uma das
   cinco âncoras escritas à mão no esquema.
2. **A causa tem grupo próprio.** Quem cai pela condição não vai para o balde do
   silêncio. Não é proibição (o fabricante não proíbe) e não é silêncio (ele
   falou, e falou desta superfície). Misturar seria a mistura de causas que a
   seção 7 proíbe desde 12/09/2026, escrita nesta mesma ilha.
3. **A atribuição sai dividida ao meio (seção 26.3).** A **condição** é do
   fabricante; a classificação de **quais superfícies são porosas** é da ilha. A
   página escreve as duas metades em orações separadas — *"a Henkel escreve ao
   menos uma das superfícies deve ser porosa; quem diz que pastilha de cerâmica é
   a superfície porosa deste caso somos nós, não ela"* — e o portão mede a
   separação.

**A lista mora no esquema, nunca na régua (seção 26.2)**, com as duas direções
cobradas: a união de porosas e não porosas tem de ser IGUAL ao vocabulário, e as
duas listas disjuntas. A direção da dúvida está escrita: **na dúvida, NÃO
porosa** — cerâmica esmaltada entra como não porosa mesmo sabendo que o biscoito
por baixo do esmalte é poroso, porque quem escolhe "cerâmica ou porcelana" na F2
está colando sobre a face esmaltada.

## O ACHADO QUE QUASE FOI COMMITADO, e foi um portão que o pegou

A ficha técnica BRSA005 foi **localizada e não lida** (o PDF não abre desta
nuvem). Ela tinha sido gravada dentro de `fontes`, "para a próxima execução saber
onde ir", com o nível 2 dela. **O nível de um material é o MELHOR dos níveis das
fontes**, então aquela linha promoveu o produto inteiro de 3 para 2 sem que uma
declaração dele viesse da ficha — e a linha de prova da tela passou a atribuir a
declaração a um documento que ninguém abriu. Quem viu foi o portão de acentuação
da F2, que reprovou a palavra `tecnica` chegando à tela vinda do campo `tipo`
daquela fonte.

Seção 10 do contrato: **o nível é o do elo MAIS FRACO, e inflar o próprio nível
de fonte é o defeito mais caro numa fábrica que vende procedência.** O endereço
ficou, em campo próprio — `fonte_localizada_nao_lida` —, e nasceu a trava:
`fontes` é o que SUSTENTA o registro, e fonte que declara não sustentar campo
nenhum é recusada pelo validador com o motivo escrito.

## O OUTRO ACHADO, de carona, e ele estava numa régua

O validador cobrava etiqueta do Mercado Livre no formato `clubedomosaico-<código>`
— **uma etiqueta IMPOSSÍVEL de criar**. A seção 7 do `ARQUIPELAGO.md` foi
corrigida em 13/09/2026 MEDINDO o painel: só minúsculas e números, sem hífen, no
máximo 30 caracteres. A régua ficou para trás e aprovava os **23 registros** do
banco que carregavam a forma com hífen. Portão verde sobre um valor que não
existe do outro lado. Os 23 registros e a régua foram corrigidos no mesmo commit.

## O DEFEITO QUE ESTE BLOCO CRIOU E CONSERTOU NO AR: prosa que envelhece calada

A seção "Duas coisas que a gente ainda não responde" era **duas frases escritas à
mão**, e as duas eram exatas no dia em que nasceram. Os dois produtos as fizeram
mentir no mesmo dia — **no ar, em voz de confissão**, que é pior, porque frase de
honestidade é a última de que alguém desconfia. O conserto não foi reescrever a
prosa: a seção passou a ser **CONTADA a cada requisição**, varrendo a entrada
inteira (base × lugar × caquinho) e publicando *"esta página responde 270
combinações; em 68 delas a gente ainda não tem cola para indicar"*.

**Mais três listas digitadas caíram no mesmo bloco**, e a quarta foi pega pelo
portão que eu mesmo tinha acabado de escrever: a resposta do FAQ e a frase
*"trocando por X, ele voltaria a servir"* traziam os nomes dos caquinhos porosos
escritos à mão. Essa última é a única frase da página que diz à pessoa **o que
fazer para a peça não descolar**, e digitada ela erraria do jeito caro. As duas
passaram a sair das mesmas listas que a régua usa.

**A tabela pré-renderizada ganhou a coluna da condição.** Sem ela, a linha
"plástico, dentro de casa: use Cascola PL500" sairia servida no HTML como se
valesse sempre — e ela só vale com caquinho poroso. É a metade que um modelo de
linguagem lê sem preencher formulário, e é onde a afirmação sem escopo custa mais.

**Na casca, três números entraram na via viva**: `celulas_matriz`,
`celulas_com_saida` e `celulas_sem_saida` eram os únicos do instantâneo que
nenhuma linha recontava, e a página de metodologia — cujo único produto é o rigor
— passou a publicar que a ilha tinha duas combinações sem saída num dia em que
ela não tinha nenhuma. A frase também ganhou o ESCOPO do que ela mediu, e aponta
para a ferramenta, que tem a conta com as três dimensões.

## A verificação, em números

**Banco:** `validar-banco.py` APROVADO — 25 materiais, 18 células da F2
recomputadas, 9 do rejunte, **54 pares da regra 6 com 5 âncoras ponta a ponta**.
As 18 células da matriz foram **derivadas à mão** das declarações dos dois
produtos ANTES de o validador rodar; as 32 divergências que ele acusou bateram
uma a uma com a derivação.

**Bancada, 0 falha:** teste-f2 de 87 para **102 afirmações**, com varredura da
entrada INTEIRA — 270 estados, um processo cada —, incluindo a **prestação de
contas da cola** que a ilha nunca teve: 1.890 nomeações (7 colas contadas do
arquivo × 270 respostas), cada item em exatamente UM lado. teste-casca 546,
teste-f1 182, teste-loja 147, teste-leads 211, teste-atelie, validar-pastilhas,
prestação de rejunte (540 estados da F2 e 180 da F1), `php -l` em tudo.
`conferir-cobertura.php` **353 afirmações, 0 falha**: a régua do censo e a do
snippet dão o mesmo elegível nos 270 estados de cola e nos 60 de rejunte.

**Censo da 14.3, o número deste bloco:** a cola sai de **45 estados varridos, 0
com o mínimo, teto 2** para **270 varridos, 28 com o mínimo de 3, teto 4**. Os
com zero elegíveis são 68, e é esse o número que a página publica.

**Navegador:** a bateria rodou sobre os quatro estados novos da F2, com a passada
de JavaScript desligado inteira.

**Mutações:** a bateria rodou inteira **três vezes**, e as três passadas
produziram achado. **Quatro resultados**, e os quatro valem mais que o verde:
- Uma mutação antiga **virou INERTE** quando a assinatura de `cdm_f2_fora_html()`
  ganhou a tessela. Mutação que não morde é teste verde com outro nome; foi
  reapontada.
- Uma **PASSOU**, e o motivo era meu: eu declarei o portão errado. Ela edita o
  snippet e eu mandei o validador do banco julgá-la, e o validador não lê uma
  linha de PHP. Ganhou o portão certo, e ganhou uma **gêmea do lado do Python**,
  porque duas implementações da mesma regra precisam das duas mutações.
- A trava que ela deveria ter acionado **não existia**. A afirmação que faltava —
  *"produto proibido sai no bloco da proibição, nunca no da condição"* — nasceu e
  descobriu-se **verde sem poder falhar**: o banco tem um produto com condição e
  ele não é proibido em base nenhuma. Nasceu com ela a mutação que **produz o
  mundo**, criando o par proibido-com-condição que o banco de hoje não tem.
- Na passada seguinte, **uma segunda PASSOU**: apagar a coluna da condição da
  tabela pré-renderizada deixava o portão inteiro verde. O defeito era real e o
  `conferir-no-ar.py` o pegava — **mas defeito pego pela regra VIZINHA prova que
  ALGUMA trava existe, nunca que ESTA existe**, e é por isso que cada mutação
  deste bloco declara qual portão tem de reprová-la. Enquanto a bancada não
  medisse, a tabela podia perder a coluna e só o desembarque diria. A afirmação
  nasceu, com régua própria (o literal do fabricante lido do banco em disco), e
  a mutação foi reaplicada sozinha para ver a trava reprová-la antes da passada
  final: **6 linhas da tabela indicam produto com condição, e as 6 publicam a
  condição literal.**

**Resultado final, medido depois do fechamento e corrigido aqui: 44 mutações, 44 reprovadas,
0 passaram, 0 inertes.** A entrada acima foi escrita quando a terceira passada estava em 31 de
44, e era isso que ela dizia — o número menor, que era o medido naquele minuto. A bateria
terminou em seguida, no mesmo container, e este parágrafo é a correção. **Escrever o número
menor e corrigi-lo custa um commit; escrever 44 antes de vê-lo seria a única coisa que esta
fábrica não perdoa.**

## Receita e dívida, contadas do arquivo

7 colas no banco (eram 5). **Os dois novos nascem SEM PISO**, e isso é dívida
contada, não estado de espera: a palavra-chave de busca dos dois está escrita em
`afiliado.url_busca_produto`, e o que falta é o encurtamento, que exige a sessão
logada do painel de afiliado — medido nesta execução às 21h (o
`affiliate.shopee.com.br` serve casca de JavaScript sem sessão). **No dia da
sessão são duas colagens e nenhuma linha de código muda.** A ilha vai a 25 itens
de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem.

## Aberto e nomeado

- (a) **A matriz escrita à mão cobre 18 das 45 células de base × lugar.** As
  outras 27 são verificadas só pela varredura das páginas servidas, que mede a
  agregação e NÃO é régua independente de elegibilidade. Está dito dentro do
  próprio portão, em vez de escondido. O conserto é a matriz chegar a 45 — nunca
  o portão fingir que já mede o que não mede.
- (b) Os 15 `url_busca` dependem de uma sessão do painel da Shopee.
- (c) O egresso a fabricante segue fechado; a ficha BRSA005 está localizada e não
  lida, com o endereço guardado.
- (d) `1x1` de fabricante continua com zero elegível, e é o tamanho de 7 das 12
  linhas da tabela da F1.
- (e) A ilha não tem peça publicada, então ficha, formulário no ar e feed do
  Merchant Center esperam a artesã.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.

## UM DETALHE DO COMMIT, e desta vez ele virou regra do Arquipélago

A mensagem do commit deste bloco perdeu a palavra `fontes`: ela estava entre
crases dentro de aspas duplas, e o shell executou o que havia ali e colou a saída
vazia no lugar. A linha foi ao ar como *"saiu de \n depois que"*. **É a segunda
vez no mesmo dia e na mesma ilha** — às 19h17Z sumiu o nome de uma pendência,
pelo mesmo motivo, e a execução de então registrou o fato só aqui, no `REGISTRO`
da ilha. Registrado só aqui, o defeito repetiu.

A seção 3 proíbe force push, então as duas mensagens ficam como estão. O que
mudou é onde a lição foi escrita: **a regra nova está na seção 3 do
`ARQUIPELAGO.md`**, que é onde regra do Arquipélago mora e é lida por toda
execução de toda ilha — *crase não entra em mensagem de commit*, e a mesma
armadilha vale para `$` e `!` dentro de aspas duplas.

**PRÓXIMO, com ordem e motivo:** (1) **a matriz esperada da F2 de 18 para 45
células**, que é a independência que falta ao número que a página publica, e é o
único item aberto que este bloco criou; (2) a ordem das duas vitrines na F1, hoje
herdada de quando o bloco da pastilha era uma frase de espera; (3) `1x1` de
fabricante, a pendência mais cara da categoria pastilha; (4) os 15 `url_busca`,
no minuto em que houver sessão — e é copiar e colar.

---

# 13/09/2026, 23h18Z — A MATRIZ ESCRITA À MÃO VAI DE 18 PARA 45 CÉLULAS, E A PRIMEIRA COISA QUE ELA VÊ É UM DEFEITO NO AR

**F2 1.4.0 · esquema versão 3 · manifest revisão 27 · nenhuma URL nova, nenhuma
página criada.** Era o item (1) do PRÓXIMO da execução das 22h30Z, e o único item
aberto que aquele bloco tinha criado.

## A escolha da ilha, e ela foi a terceira tentada

Rotação da seção 1, sem despacho aberto para a Fundação em nenhum dos três
`PROMPT.md` (os três foram lidos antes de escolher, como a 18.1 manda). A
robometria era a de `ultima_execucao` mais antiga (21h16Z) e **meu push de reserva
foi recusado por cerca de um minuto** — outra execução a reservou às 23h18Z; a
aquametria caiu às 23h19Z pelo mesmo motivo. O passo 5 manda voltar ao passo 2, e
**nenhum force push aconteceu**. Sobrou a clubedomosaico, com `executando_desde:
null`, que pela **1.1** já significa que não há bloco da Fundação vivo — o git não
precisou desempatar, embora a ilha tivesse fechado bloco 6 minutos antes.

`dados/despachos.md` tem um despacho para a **FUNDAÇÃO (quem reservar a
aquametria)**: consertar o cabeçalho YAML dela. **Medido nesta execução, os três
`ESTADO.md` passam por `yaml.safe_load`** — a execução das 21h21Z da aquametria já
o cumpriu. Não é minha ilha para tocar, mas o "pronto quando" dele está satisfeito
e isso ficou escrito no despacho, com quem mediu.

## O que a dívida era, dita com o tamanho que ela tinha

A matriz `matriz_esperada_da_F2` é a **régua independente** da ferramenta: ela é
escrita à mão a partir das declarações dos fabricantes e nunca chama uma linha do
snippet, então as duas metades não erram juntas. Ela cobria **18 das 45 células**
de base × lugar. As outras 27 passavam só pela varredura das páginas servidas —
que mede a **agregação** e lê a MESMA implementação de elegibilidade dos dois
lados. Portão verde que não é régua.

**As 27 novas foram DERIVADAS À MÃO das declarações ANTES de o validador rodar uma
vez**, e a derivação ficou gravada antes da inserção. Resultado, dito com o número
que ele tem: **zero divergência** nas cinco listas das 27 — recomendados no topo,
elegíveis abaixo, proibidos, silêncio e menção com ressalva bateram produto a
produto com a recomputação. O que o validador cobrou foram **9 observações que
faltavam**, e ele estava certo: célula sem recomendação tem de dizer POR QUE, e
essa regra existia antes deste bloco.

## O ACHADO, e ele é o motivo de esta régua valer o que custa

**As 18 células antigas TODAS tinham recomendação.** Nenhuma delas era faixa
descoberta — ou seja, **a régua independente desta ilha nunca havia pisado numa
célula sem resposta**, que é justamente a metade em que a página vende honestidade
em vez de produto. Com as 45, **11 células são descobertas**, e o ramo do código
que as escreve deixou de ser código morto para o portão.

Ele estava errado, e **estava no ar**. Em quatro estados — **vidro, madeira,
alvenaria e metal em contato permanente com água** — a página servia:

> "Não temos cola para indicar em metal dentro da água. **Nenhum dos adesivos do
> nosso banco é declarado pelo próprio fabricante para esse caso** — e a gente
> prefere dizer isso a chutar o de sempre."

e, **duas seções abaixo, na mesma página**:

> "Existe menção a **Loctite Durepoxi**, mas o que sustenta isso é material de
> imprensa do fabricante, não documento de produto."

A primeira frase é **falsa**. A Henkel declara metal, alumínio, ferro, cobre e
latão E declara secar em condição submersa — as duas metades, no mesmo produto. O
que segura a recomendação é a **procedência da fonte**, que é régua NOSSA (regra
5), não o silêncio do fabricante, que seria fato dele. Trocar uma causa pela outra
é a mistura que a seção 7 do contrato proíbe — e ela é pior aqui do que em
qualquer outro lugar da página, porque está dentro da frase que o leitor recebe
como confissão de honestidade. É a mesma família do defeito que esta ilha já
consertou em 12/09 na prosa que envelhece calada, e da correção que a regra 6
obrigou em 13/09 ("o motivo não é falta de declaração").

**O conserto saiu inteiro, nas duas metades.** A frase-resposta ganhou um terceiro
ramo, e a **vitrine vazia** ganhou o dela — sem a segunda, a página consertaria a
resposta e repetiria a frase errada uma seção abaixo, em "nenhum produto do nosso
banco passa no que o fabricante declara". Defeito pego pela régua vizinha prova
que ALGUMA trava existe, nunca que ESTA existe, então cada metade tem mutação
própria.

**AS TRÊS CAUSAS DE UMA FAIXA DESCOBERTA, agora nomeadas uma a uma na tela:**
**silêncio** (ninguém declara a base — 7 células), **procedência** (alguém declara
as duas metades e a fonte é nível 4 — 4 células) e **ambiente delimitado** (o
fabricante declarou a base e delimitou o uso a outro ambiente — é o caso do
plástico fora do interno seco). O tipo do documento sai **lido do banco em disco**,
nunca digitado na frase: digitar "material de imprensa" ali mediria a frase contra
ela mesma.

## A PROVA DE QUE AS 27 CÉLULAS COMPRARAM ALGUMA COISA, medida nos dois mundos

Régua nova que só fica verde não provou nada. Nasceu a mutação **"o mapa perde a
pedra do epóxi"**, e ela é cirúrgica de propósito: tira do mapa de termos os dois
literais que o Durepoxi usa para alvenaria (*pedra* e *marmore*) e **não** os que o
Silicone Neutro usa (*pedras*, *alvenaria*). Assim o neutro continua respondendo e
o único efeito visível é o Durepoxi cair de menção com ressalva para silêncio nas
quatro células de alvenaria — **as quatro nascidas neste bloco**.

- **Com a matriz de 45:** o validador acusa **8 erros**, um par por célula.
- **Com as 18 de ontem, a mesma mutação:** validador **OK**, e `teste-f2` fecha em
  **107 afirmações, 0 falha**. O defeito passava inteiro, deixando só um AVISO de
  termo sem tradução — e aviso não reprova nada.

É a aritmética da cobertura dita sem eufemismo: **régua com buraco fica verde
exatamente dentro do buraco.**

## O que mudou na tela, além da frase

A **tabela pré-renderizada da cola foi de 18 para 45 linhas** — ela é montada a
partir da mesma matriz, e é a metade que um modelo de linguagem lê sem preencher
formulário. Cada linha continua **recomputada das declarações**, nunca lida do
campo escrito à mão ao lado dela: se o banco e a matriz se separarem, quem acusa é
o validador, e a tela nunca finge concordância copiando o esperado. Nenhuma URL
nova nasceu e nenhuma página foi criada.

## Três frases que envelheceram e foram reescritas em vez de ficarem

Prosa que descreve um problema também envelhece calada, e três arquivos diziam o
tamanho velho do buraco: o comentário do `teste-f2.php` que declarava a dívida
("cobre 18 das 45"), a docstring do `cobertura.py` que chamava a matriz de amostra,
e a da mutação do ambiente crítico ("16 das 18 células continuam certas"). As três
foram reescritas com o que se mede hoje — e a do `cobertura.py` **não** virou
"agora é dispensável": a matriz decide sobre base × ambiente e não olha o caquinho,
então a entrada da ferramenta continua tendo 270 estados e a pergunta daquela
varredura continua sendo uma contagem sobre os 270.

## A conferência no ar precisou nascer, e os 390 verdes mostram por quê

Depois do Sync, `conferir-no-ar.py` passou com **390 afirmações, 0 falha** —
**sem tocar uma linha do que mudou**. Nenhum dos casos que ela media era uma
célula SEM recomendação, então ela nunca tinha lido a frase que este bloco
consertou. É a cicatriz da robometria de 13/09 acontecendo aqui: verde que não
morde.

Nasceram **26 afirmações novas no ar**, em quatro estados e com régua escrita
literal no próprio arquivo (o nome do produto e o tipo do documento copiados da
fonte, nunca lidos do banco que monta a página): os **três** estados que
respondem por procedência (vidro, metal e alvenaria dentro da água) e o estado
**negativo**, sem o qual os outros três têm porta dos fundos — em espelho dentro
da água ninguém declarou nada, e ali a página TEM de dizer que ninguém declarou.
Sem ele, uma página que servisse a frase da procedência em toda faixa descoberta
passaria nos três primeiros. Mais a linha que conta as **45** da tabela servida,
com o 45 saindo do produto dos dois vocabulários, nunca digitado.

## A verificação, em números

- **`validar-banco`**: APROVADO — 25 materiais, **45 células da F2** (eram 18), 9
  do rejunte, 54 pares da regra 6 com 5 âncoras ponta a ponta.
- **Bancada, 0 falha:** `teste-casca` 546 · `teste-f2` **107** (eram 102, e agora
  varrendo 45 células em vez de 18) · `teste-f1` 182 · `teste-loja` 147 (72
  estados) · `teste-leads` 211 · `teste-atelie` aprovado · `teste-prestacao-rejunte`
  5 afirmações sobre 540 estados da F2 e 180 da F1 · `conferir-cobertura` 353 ·
  `validar-pastilhas` aprovado · `php -l` limpo em ferramentas e snippets.
- **Mutações:** `mutacoes-f2` de 44 para **47, com 47 reprovadas, 0 passaram e 0
  inertes** — a bateria inteira, rodada do zero sobre o estado final. As três
  novas são as deste bloco: a faixa descoberta voltando a negar a declaração, a
  vitrine vazia fazendo o mesmo uma seção abaixo, e a que só as 27 células novas
  pegam.
- **UMA PASSADA DA BATERIA FOI DESCARTADA E REFEITA, e o motivo fica escrito:**
  a primeira rodada aconteceu enquanto um `git stash` reverteu a árvore de
  trabalho por alguns segundos, para o commit de renovação da reserva. A bateria
  copia a pasta da ilha **a cada mutação**, então qualquer cópia feita naquela
  janela leu a ilha de ontem. Nenhum resultado dela foi aproveitado. Número que
  saiu de uma árvore que mudou no meio não é número medido.
- **No ar, depois do Sync:** `/status` na **revisão 27**, igual à do
  `manifest.json`, em UM disparo com 10 aplicados. `conferir-no-ar` de 390 para
  **416 afirmações, 0 falha**.

## Receita e dívida, contadas do arquivo

Nada mudou de receita neste bloco, e isso é a informação: **7 colas no banco, 25
itens de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem**. Os 15
`url_busca` continuam dependendo de uma sessão do painel da Shopee — a
palavra-chave já está escrita em `afiliado.url_busca_produto` nos 15, e no dia da
sessão são 15 colagens e nenhuma linha de código. Pauta da seção 17: `pauta.md`
ainda não existe — 0 escritos, 0 na fila, 0 recusados.

## Aberto e nomeado

- (a) **A dívida que este bloco fecha era a única que o bloco anterior tinha
  criado**, e ele não criou nenhuma no lugar dela. O que sobra da família é a
  metade do **rejunte**: `matriz_esperada_do_rejunte` tem 9 células de junta ×
  ambiente e continua sendo **amostra de borda**, escolhida para pisar nas faixas
  declaradas. É amostra de propósito e não é o mesmo caso da cola — lá a grade
  inteira é finita e pequena (45), aqui a junta é contínua.
- (b) Os 15 `url_busca` dependem de uma sessão do painel da Shopee.
- (c) O egresso a fabricante segue fechado; a ficha BRSA005 segue localizada e não
  lida, com o endereço guardado em `fonte_localizada_nao_lida`.
- (d) `1x1` de fabricante segue com zero elegível, e é o tamanho de 7 das 12
  linhas da tabela da F1.
- (e) A ilha não tem peça publicada, então ficha, formulário no ar e feed do
  Merchant Center esperam a artesã.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.

**PRÓXIMO, com ordem e motivo:** (1) **a ordem das duas vitrines na F1**, hoje
herdada de quando o bloco da pastilha era uma frase de espera — é o item mais
antigo da fila e o único que mexe em como a página apresenta produto; (2) **`1x1`
de fabricante**, a pendência mais cara da categoria pastilha, e a que sozinha
muda 7 das 12 linhas da tabela da F1; (3) **a matriz do rejunte de amostra para
grade**, se e quando a junta virar um vocabulário fechado — hoje ela é contínua e
a amostra de borda é a escolha certa, então isto é pergunta antes de bloco; (4)
os 15 `url_busca`, no minuto em que houver sessão — e é copiar e colar.

---

# 14/09/2026, 11h18Z — O 404 DEPOIS DE PUBLICAR NÃO ERA REGRA DE REESCRITA: ERA UM NOME QUE JÁ TINHA DONO

**Despacho do Raphael de 14/09, os quatro itens, e é o primeiro despacho desta
fábrica escrito a partir do que uma PESSOA encontrou usando o que ela construiu.**
A mãe dele recebeu o e-mail, criou a senha, entrou e cadastrou a primeira peça do
Arquipélago — "Quadro flores do campo", quatro fotos, R$ 500, pronta entrega. O que
vem abaixo é o que ela encontrou no caminho.

**Ilha escolhida pela 18.1, não pela rotação.** A clubedomosaico tinha o despacho do
Raphael mais recente e aberto no topo do `PROMPT.md`; a aquametria e a robometria
foram lidas antes de escolher e não tinham despacho aberto para a Fundação (o item
1 do de 10/09 da robometria é metade humana, no Search Console, e não é nossa). As
outras duas execuções da mesma janela registraram nos próprios commits que
perderam a corrida por esta ilha; nenhum force push aconteceu, dos dois lados.

## ITEM 1 — a causa não era a que o despacho supôs, e ele mandava confirmar

O despacho escreveu a hipótese e a marcou como hipótese: regras de reescrita do
CPT `peca` não descarregadas. **Medido antes de uma linha mudar, às 11h19Z:**
`/loja/quadro-flores-do-campo/` — a peça que ela publicou — responde **200**. A
regra de reescrita está de pé e nasce sozinha desde a Loja 1.0.0.

O que estava errado era **o nome de um parâmetro**. O painel carregava o id da peça
na URL como `peca`, e `peca` é o nome do TIPO DE CONTEÚDO, registrado com
`query_var` true — ou seja, uma variável PÚBLICA do WordPress. Para o núcleo,
`/atelie/?peca=24` não é "o painel com a peça 24": é "me dê a peça de slug 24", que
não existe, e o tema serve o 404 dele. As quatro medições, no ar, antes do
conserto:

| endereço | resposta |
|---|---|
| `/atelie/` | 200 |
| `/atelie/?aviso=publicada` | 200 |
| `/atelie/?peca=24` | **404** |
| `/atelie/?estado=editar&peca=24` | **404** |
| `/atelie/?estado=editar&cdm_peca=24` | 200 |

E a confirmação que fecha a frase dele: o corpo daquele 404 serve
`themes/twentytwentyfive/assets/images/404-image.webp`, com `alt="Pequena árvore
totara no topo acima de Long Point"`. **É a foto em preto e branco que ele viu.**

**Isto atingia mais que o publicar, e o despacho não sabia.** Seis voltas do painel
carregam o id — publicou, salvou rascunho, pausou, faltou um campo, atualizou fotos
— mais o link "Editar" da lista. **As sete caíam no mesmo 404.** Publicar era só o
caminho em que ela chegou primeiro.

**O conserto é o nome:** o parâmetro passou a ser `cdm_peca`, o mesmo prefixo que os
campos do POST deste painel já usam. Nenhum filtro tirando variável do núcleo no meio
do caminho — a colisão se resolve não colidindo. E como isso é uma regra que ninguém
enxerga lendo a linha (`'peca' => $id` parece certo), ela virou **portão**:
`teste-atelie.php` varre o snippet, extrai toda chave literal passada a
`cdm_atelie_url()`, resolve a constante do parâmetro de peça, e compara a lista
inteira com as variáveis públicas do WordPress — escritas à mão no teste, copiadas
de `WP::$public_query_vars`, mais o tipo e as duas taxonomias desta ilha. Quem
escrever uma chamada nova amanhã cai no portão sem precisar lembrar dele.

**A segunda metade do item 1**, que é o que ela devia ver no lugar do 404: a volta
para `/atelie/` já era PRG desde a 1.0.0 e continua sendo, agora com **faixa de
"Peça publicada!"**, botão **"Ver no site"** e botão **"Cadastrar outra peça"**. O
"Ver no site" **não é incondicional**: só nasce se a peça existe, é dela, está
PUBLICADA de verdade e tem endereço — a trava do núcleo devolve ao rascunho a peça
que não cumpre a regra de qualidade, então "publiquei" e "está no ar" são duas
coisas, e um botão que promete o site e cai num 404 seria o mesmo defeito, dentro
da tela que o conserta.

## ITEM 2 — "o que seria 'escolha'? Não tem nada"

Duas coisas erradas na mesma linha, e são independentes. **A palavra:** "Escolha"
nomeia uma opção que não existe; lida por quem não sabe o que é uma lista, é um item
como os outros. **O estado:** era `value=""` selecionável e inicial, então dava para
voltar a ela. Agora a primeira linha de toda lista de escolha do painel é
`<option value="" disabled hidden selected>Selecione…</option>` — instrução, não
item —, escrita por **uma função só**, porque foi exatamente dois lugares
escrevendo a mesma linha à mão que deixou "Escolha" sobreviver nos dois.

**A trava.** As duas listas que ligam a peça ao site — coleção e técnica — ganharam
`required`, e o botão **"Salvar e terminar depois" ganhou `formnovalidate`**: sem
essa palavra, o `required` transformaria guardar rascunho em refém de uma lista e
ela perderia o texto que já tinha escrito (decisão 5 do snippet). A frase que
aparece é do painel e não do navegador — "Escolha a técnica que você usou nesta
peça." —, trocada por `setCustomValidity`; com o JavaScript desligado sobra a do
navegador, que é seca mas trava do mesmo jeito, e travar é o que protege a peça
órfã. No servidor a régua já existia e não foi duplicada:
`cdm_loja_peca_publicavel()` recusa publicar sem coleção e sem técnica desde 12/09.

## ITEM 3 — Picassiete, e a prova de que o campo obrigava a mentir

A peça que ela cadastrou tem **"Picassiette" escrito na descrição por ela mesma** e
**"Trencadís" marcado no campo** — porque Picassiete não existia para marcar. É o
caso literal do campo que obriga a pessoa a responder o que não é.

A técnica entrou. **E a versão da Loja subiu com ela, que é a metade que faltava:**
`cdm_loja_termos_iniciais()` só é percorrida quando `CDM_LOJA_VERSAO` difere da
option `cdm_loja_termos` — termo novo sem versão nova é linha no repositório que
nunca vira linha na lista dela. Medido: antes deste bloco a rota pública `/v1/loja`
dizia `tecnica: 4`; depois do Sync diz **5**.

A distinção que o despacho mandou escrever está na **ajuda do campo**, que é onde ela
decide: *"Trincadís é caquinho de azulejo ou cerâmica, sem dar para reconhecer de
onde veio; Picassiete é caco de louça em que dá para reconhecer a peça original —
alça, bico, estampa. Também chamada pique-assiette."* O trincadís **fica**, como o
esclarecimento do mesmo dia manda.

**O slug gravado é `picassiette`, e isto é escolha registrada, não descuido.** O
despacho pediu `Picassiete`; o esclarecimento do mesmo dia diz que "entrou como
`picassiette`" e não o desfaz. As duas taxonomias desta ilha são registradas com
`rewrite` false, então o slug do TERMO não decide endereço nenhum hoje: no dia em
que houver página de técnica, `/tecnicas/Picassiete/` continua inteiramente
disponível, e quem decide o endereço é a malha, não este campo. Na tela, onde ela
lê, o nome é **"Picassiete"** — o `VOZ.md` manda na palavra.

## ITEM 4 — o comportamento do Real 21, com código nosso

O Raphael deu a referência e **mudou a instrução na mesma frase**: a galeria do
Real 21 é Elementor + Swiper, medido por ele em 14/09, e isso é construtor de página
mais biblioteca JavaScript — o que a 22.3 proíbe na página pública e a 11.7 proíbe
instalar. Copiar aquilo trocaria ranqueamento por beleza.

O que nasceu, todo ele sobre o HTML que já estava servido:

- **Foto grande em proporção fixa 4:5** com `object-fit: cover`. Era metade do "está
  muito feio": foto de celular vem em pé e deitada, e sem proporção fixa a página
  saltava de altura entre uma peça e outra.
- **Tira de miniaturas quadradas de verdade** — `aspect-ratio: 1/1` mais
  `object-fit: cover`, o quadrado é do CSS e o arquivo nunca é cortado. **Cada
  miniatura é um link para a âncora da foto**, então ela funciona com o JavaScript
  desligado: `#cdm-foto-3` rola o contêiner de `scroll-snap` sem uma linha de
  script. O `alt` delas é vazio de propósito — a foto grande já descreve a peça, e
  repetir faria o leitor de tela ler a peça inteira duas vezes.
- **Setas de 44 px**, botões de verdade com `aria-label` e `aria-controls`, que só
  rolam o contêiner. Aparecem no ponteiro e somem no toque, onde o dedo já arrasta.
- **Ampliar com `<dialog>` nativo**, X grande, `Esc` (que é do navegador) e clique
  fora. **Zoom** na ampliada com `transform: scale(2)` e origem no ponto tocado.
- **O endereço da foto grande viaja no HTML**, em `data-cdm-grande`: o zoom não é a
  foto pequena esticada, e o script **não busca nada** — que é o outro lado da 22.3.
- Tokens do `DESIGN.md` desta ilha, que ganhou a entrada "Galeria da ficha da peça"
  ANTES do código, como a 22.6 manda.

## O DEFEITO QUE SÓ O AR TINHA, E QUE EU PUBLIQUEI ANTES DE VER

Esta é a parte que vale mais que as quatro acima, porque ela é sobre o portão e não
sobre a tela.

A ficha é montada por `the_content`, e **o retorno desse filtro passa pelo
`wpautop`** — que usa as etiquetas de BLOCO como fronteira de parágrafo, embrulha
cada pedaço em `<p>…</p>`, e depois tira o `<p>` que encosta num bloco e o `</p>`
que vem logo depois de um. **`button`, `dialog`, `span`, `a` e `img` não são blocos
para ele.** A bancada desta ilha não tem WordPress: ela mede o HTML que a função
devolve, e o `wpautop` só existe no site.

Eu previ metade disso e errei a outra. A `<dialog>` foi para o `wp_footer` antes de
qualquer medição, e isso estava certo. As duas setas eu deixei soltas logo depois da
abertura do palco, achando que bastava não vir depois de um `</div>`. **Fui olhar o
HTML servido e ele trazia:**

```
<div class="cdm-gal-palco"><button …>‹</button><button …>›</button></p>
```

Um `</p>` órfão colado no `</button>`: a abertura do parágrafo foi removida por
encostar num `<div>` e o fechamento ficou, porque encostava num `</button>`. Nada
quebra na tela. O navegador engole. **E o portão tinha passado verde**, porque a
régua que eu tinha escrito olhava só um lado — etiqueta de linha DEPOIS de um
fechamento de bloco — e o defeito era do outro, ANTES de uma abertura.

A regra que sobra, e ela vale para tudo que esta ficha imprimir daqui para a frente:
**etiqueta que não é bloco nunca encosta numa fronteira de bloco, de nenhum dos dois
lados.** As setas passaram a morar dentro de um `<div class="cdm-gal-setas">` — uma
camada absoluta que cobre o palco, deixa o dedo passar e ancora as duas. A régua do
`teste-loja.php` passou a medir os dois lados e **nomeia qual** apareceu; a mutação
37 devolve exatamente o HTML que foi ao ar e a régua reprova dizendo
`antes de bloco: </button>`. E o `conferir-atelie-no-ar.py` passou a procurar as
cinco marcas do estrago — `<p><button`, `</button></p>`, `<p><dialog`,
`</dialog></p>`, `<p></dialog>` — **no HTML servido**, porque é lá que o `wpautop`
existe.

## A OUTRA COISA QUE O AR ENSINOU: a ficha é servida de cache por duas horas

Conferindo o conserto, a primeira leitura de `/loja/quadro-flores-do-campo/` veio
com `last-modified` de **13/09 17h01** e `cache-control: max-age=7200`, servindo a
ficha ANTERIOR — com a revisão 28 já aplicada e a rota `/v1/loja` já dizendo
`versao_loja: 1.2.0`. É a família da seção 4 do contrato com uma cara nova: o site
não ficou para trás, a CÓPIA que o visitante recebe ficou. O `conferir-atelie-no-ar.py`
já se protegia disso — o `buscar()` dele anexa `?v=<timestamp>` a toda URL, escrito
lá desde 12/09 — e foi o `curl` a mão desta execução que caiu no cache. Fica
registrado para a próxima passada: **`curl` a mão nesta ilha mede o cache, não o
site.**

## A verificação, em números

- **Bancada, 0 falha:** `teste-casca` **549** (eram 546), `teste-loja` **178** (eram 148),
  `teste-atelie` **288** (eram 251), `teste-leads` 211, `teste-f1` 182, `teste-f2`
  107, `teste-prestacao-rejunte` 5 sobre 540 e 180 estados, `conferir-cobertura` 353,
  `validar-banco` aprovado com 25 materiais e 45 células, `validar-pastilhas`
  aprovado, `php -l` limpo nos três snippets tocados.
- **Mutações:** `mutacoes-atelie` de 37 para **48**, com **48 reprovadas**, 0
  passaram, 0 inertes. `mutacoes-loja` de 23 para **36**, com **36 reprovadas**, 0
  passaram, 0 inertes. `mutacoes-arvore` de 20 para **21**, com **21 reprovadas**.
- **Duas mutações antigas foram consertadas, e as duas por causa deste bloco:** a 26
  do ateliê ficou INERTE porque o alvo dela citava `'peca' => $id`, que o conserto
  renomeou; a 33 da loja ficou INERTE porque a lupa saiu do retorno da ficha.
  Mutação inerte é teste verde com outro nome.
- **Uma afirmação foi endurecida depois de a mutação 25 passar limpa:** a régua da
  proporção fixa procurava `aspect-ratio:4/5` no documento inteiro, e o cartão da
  vitrine também tem essa linha — tirar a proporção da foto grande passava verde.
  Agora ela lê a declaração `.cdm-carrossel img{…}` isolada e imprime o conteúdo
  dela na medida. **Régua que procura no documento inteiro mede a existência da
  palavra, não a do comportamento.**
- **No ar:** `conferir-atelie-no-ar.py` **79 afirmações** (eram 65), 0 falha, 0
  pulada, com a seção 4d nova — o parâmetro, a faixa, a contagem de técnicas — e a
  galeria medida na ficha servida. `conferir-no-ar.py` **416 afirmações, 0 falha**,
  sem tocar uma linha do que mudou.
- **A própria afirmação de ar nasceu errada uma vez, e vale escrever:** a primeira
  versão procurava a FORMA `</button></p>` no HTML servido e reprovou a peça — só
  que essa forma tem versão legítima aqui, no formulário de lead
  (`<p class="cdm-lead-enviar"><button …></button></p>`), com a abertura escrita por
  nós. **O que separa o certo do errado não é a forma, é o BALANÇO.** A afirmação
  passou a contar `<p` e `</p>` dentro da região da galeria, onde a única abertura
  que existe é a da contagem de fotos: 1 abre, 1 fecha. Procurar a forma teria
  reprovado a página certa e, num dia com o formulário desligado, aprovado a errada.
- **A régua do `teste-loja` mudou de forma numa linha, e ela ENDURECEU:** até 13/09
  a afirmação era "a Loja não serve JavaScript nenhum", e ela media a coisa certa
  pelo motivo errado — o que a 22.8 protege não é a ausência de JavaScript, é a
  página FUNCIONAR sem ele. O que ela cobra agora: UM script, no rodapé, depois do
  conteúdo, e **nenhuma** ocorrência de `fetch(`, `XMLHttpRequest`, `import(`,
  `document.write`, `cdn.`, `swiper` ou `elementor` dentro dele.

## E UM TERCEIRO DEFEITO, ACHADO NA CONFERÊNCIA, QUE NINGUÉM ESCREVEU

Contando as URLs do `wp-sitemap.xml` para fechar o bloco, apareceu uma que não é
página desta ilha: **`/author/artesa/`**. Ela não foi escrita por ninguém e nenhuma
linha de código mudou para ela existir — **o provedor `users` do núcleo só lista
autor que TEM conteúdo publicado**, e até 13/09 esta ilha não tinha peça nenhuma.
No minuto em que a artesã publicou a primeira, o arquivo de autor dela entrou no
sitemap: **uma de doze URLs de um domínio de quatro dias.**

Duas razões para tirar, e cada uma bastaria. **É página fina e repetida** — o
arquivo do autor lista as peças publicadas, que é o que `/loja/` já faz com texto
editorial em volta, e orçamento de rastreamento é o recurso escasso da seção 14.1.
E **ele confirma o login dela**: o endereço carrega o `user_nicename`, que nesta
ilha é o mesmo `artesa` com que ela entra; este snippet e o do ateliê gastam
trabalho para a conta de uma pessoa de verdade não ficar exposta, e publicar o nome
de usuário num arquivo XML desfaz metade disso de graça.

Casca **1.9.2**: o provedor `users` sai, pelo mesmo mecanismo que a Aquametria já
media desde 10/09 — aqui ele só não existia porque não havia autor com conteúdo. A
régua entrou no `teste-casca.php` escrita à mão (o nome do provedor e a resposta
esperada estão na linha, não lidos do snippet) e cobra os dois lados: `users` sai,
`posts` e `taxonomies` ficam, para a remoção não vazar. Mutação nova na bateria da
árvore, **21 de 21 reprovadas**. **No ar: o sitemap foi de 12 para 11 URLs, e
nenhum arquivo de autor pede rastreamento.**

**E o `atualizar-manifest.py` fez o trabalho dele nesta passada**, o que é raro o
bastante para ficar escrito: ele **recusou gravar** a revisão 30 porque a versão da
casca no manifest (1.9.1) não batia com a constante do snippet (1.9.2). A recusa
veio antes do commit da revisão, não depois.

## A cópia da seção 24 nasceu, com peça de verdade dentro

`dados/pecas.json` existe desde hoje, com a peça que ela cadastrou: título, slug,
estado, descrição, campos, coleção, técnica e as quatro URLs de foto. Até 13/09 a
rota devolvia `total: 0`, e zero peça é resposta, não falha.

**Uma decisão de formato, e ela é o que faz a regra 24.2 funcionar:** o campo
`gerado_em` da rota **não entra na cópia**. Com ele dentro, toda passada da ronda
seria um commit, e a 24.2 manda commitar só quando o JSON MUDOU. Quando a cópia foi
tirada é o git que sabe — é para isso que ele serve. `publicar: false`, porque este
arquivo é cópia do site e nunca fonte dele; desembarcá-lo devolveria ao WordPress o
que veio de lá.

## Receita, contada do arquivo (nada mudou neste bloco)

7 colas, 25 itens de fabricante, 15 esperando link, 15 sem piso, 22 sem imagem. Os
15 `url_busca` seguem dependendo de UMA sessão do painel da Shopee. Pauta da seção
17: `pauta.md` ainda não existe — 0 escritos, 0 na fila, 0 recusados.
**A loja tem 1 peça publicada e 0 rascunhos**, e é a primeira linha de receita
própria do Arquipélago inteiro.

## Aberto e nomeado

- **(a) A página `/tecnicas/Picassiete/` NÃO nasceu, e o item 3 pedia.** Não é
  esquecimento e não é conserto: **nenhuma** técnica desta ilha tem página. As duas
  taxonomias são registradas `public => false` por decisão medida de orçamento de
  rastreamento (decisão 4 do snippet da Loja, 12/09) — taxonomia pública nasce com
  arquivo e põe de sete a doze URLs finas no sitemap de um domínio de quatro dias.
  Criar a página do Picassiete sozinha seria criar a família inteira por uma porta
  lateral. **Isto é bloco de malha, não item de despacho**, e ficou reescrito no
  `PROMPT.md` como o que falta.
- **(b) A metade humana do item 4 continua aberta:** o dedo dela na galeria, num
  telefone. A Fundação mediu o HTML servido, as marcas do `wpautop`, os
  `aria-label` e a proporção; **ninguém tocou a tela**. Isso fica como o que falta,
  nunca como conferido.
- (c) Os 15 `url_busca` dependem da sessão da Shopee.
- (d) O egresso a fabricante segue fechado e a ficha BRSA005 segue localizada e não
  lida.
- (e) `1x1` de fabricante segue com zero elegível, e é o tamanho de 7 das 12 linhas
  da tabela da F1.
- (f) `contato@clubedomosaico.com.br` ainda não existe como caixa.
- (g) A dívida de modelagem que o esclarecimento do Raphael registrou e mandou NÃO
  mexer agora: o campo "técnica" mistura MÉTODO (direto, indireto) com ESTILO
  (bizantino, trincadís, Picassiete), e ela pode marcar um achando que marcou o
  outro.

**PRÓXIMO, com ordem e motivo:** (1) **a família `/tecnicas/<slug>/`**, que é o que
sobrou do item 3 e agora tem peça publicada para linkar — e é decisão de malha, com
o orçamento de rastreamento na mesa; (2) **a ordem das duas vitrines na F1**, o item
mais antigo da fila e o único que mexe em como a página apresenta produto; (3) `1x1`
de fabricante, a pendência mais cara da categoria pastilha; (4) os 15 `url_busca`,
no minuto em que houver sessão.

---

# 14/09/2026, 13h21Z — A ORDEM DAS DUAS VITRINES DA F1: A PASTILHA VEM PRIMEIRO, E O TÍTULO DEIXA DE DEPENDER DE ESTAR EM SEGUNDO LUGAR

**F1 1.3.0, manifest revisão 31, `/status` conferido. NENHUMA URL nova, NENHUMA
página criada, NENHUM produto entrou ou saiu do banco.** Este é o item mais antigo
da fila desta ilha — o único que mexe em como a página apresenta produto — e foi o
`PRÓXIMO (2)` do fecho anterior depois que o `(1)`, a família `/tecnicas/`, ficou
nomeado como bloco de malha e não de conserto.

**A ESCOLHA DA ILHA: TERCEIRA TENTADA.** Nenhuma ilha tinha despacho aberto para a
Fundação no topo do `PROMPT.md` (os quatro achados da artesã de 14/09 saíram inteiros
na execução das 11h18Z e o que restou é bloco de malha; a aquametria e a robometria
não tinham despacho para a Fundação), então valeu a rotação da seção 1. A aquametria
tinha a `ultima_execucao` mais antiga (11h25Z) e meu push de reserva foi recusado —
outra execução a tomou às 13h19Z. A robometria (11h44Z) caiu do mesmo jeito,
reservada às 13h20Z. A clubedomosaico estava com `executando_desde: null`, que pela
1.1 já significa que não há bloco da Fundação vivo. Nenhum force push, e nada de
execução anterior para mesclar: local e remoto batiam com o `main`. Rede pela 20.2
antes de trabalhar: home em 200 e `/status` na revisão 30, igual à do manifest, em
UMA passada.

## O QUE ERA A ORDEM ERRADA, e por que ninguém a via
Até a 1.2.0 o bloco de compra do **rejunte** vinha antes do da **pastilha**. Não era
decisão: era herança. Quando a vitrine do rejunte nasceu, o lugar da pastilha era uma
frase de espera (`"ainda não temos as pastilhas no nosso banco"`), então o rejunte
era o único bloco de compra que a página tinha. A 1.2.0 encheu aquele lugar com treze
produtos e **manteve a sequência de chamada** — que é como uma ordem provisória
sobrevive a quem a tornou errada. Não havia régua nenhuma sobre ordem, e ordem que
ninguém mede não pode nem ser corrigida com confiança.

A pastilha vem primeiro porque as **três superfícies** que abrem a página falam dela:
o `<title>`, o H1 e a primeira frase da resposta (`"leva cerca de N pastilhas de X
cm"`, com o rejunte entrando como o segundo número). A seção 22.1 põe ranqueamento
antes de conversão antes de beleza; aqui as três apontam para o mesmo lado, porque
quem chega por "quantas pastilhas para mosaico" veio comprar pastilha, e o `VOZ.md`
desta ilha diz "produto primeiro". **Nada da 22.2 se moveu:** a resposta continua
antes da explicação, os DOIS blocos de compra continuam ANTES da camada de prova
(seção 7), e nenhuma URL, trilha, âncora ou JSON-LD mudou.

## O QUE A TROCA REVELOU, e é o que fez disto um bloco e não um swap
O título do bloco da pastilha era **"E onde comprar a pastilha"**. Aquele "E" é
conector: ele só faz sentido depois de outro bloco de compra, e é um título que
**mente quando a ordem muda**. Pior, a seção 5 pede frase autossuficiente, que
sobreviva a ser citada fora de contexto — e o título é justamente a frase que um
modelo de linguagem cita sozinho. Os dois títulos passaram a ser autossuficientes:
**"Onde comprar a pastilha"** e **"Qual rejunte cabe nessa folga"**, nenhum
dependendo da posição em que foi servido. Uma mutação escreve o "E" de volta, e ela é
o defeito de verdade: invisível para qualquer régua de ordem, porque a sequência fica
certa e só o título passa a prometer um bloco anterior que não existe mais.

## A FRONTEIRA DOS DOIS BLOCOS GANHOU NOME (cicatriz da Robometria de 13/09/2026)
A bancada e a conferência no ar extraíam cada vitrine pelo **texto do H2** — régua que
morre calada no dia em que o título muda, e que no estado degradado do rejunte (sem a
F2 no ar, o título é `"Onde comprar o rejunte"`) **nunca conseguiu extrair nada**.
Cada seção passou a declarar o que ela é na própria classe (`cdm-f1-vitrine-pastilha`
e `cdm-f1-vitrine-rejunte`), em **todas** as saídas, inclusive as degradadas.
Fronteira de teste é marcador escrito, nunca "a primeira coisa parecida com". As três
réguas que extraíam pelo título — `teste-f1.php`, `teste-prestacao-rejunte.php` e
`conferir-no-ar.py` — passaram a ler o marcador.

## O MUNDO SEM A F2 FOI PRODUZIDO PELA PRIMEIRA VEZ
A F1 chama a régua do rejunte da F2 em vez de escrever uma segunda (decisão 4 do
cabeçalho dela), e por isso tem DUAS saídas degradadas escritas de propósito — uma em
cada vitrine — que dizem "a lista está fora do ar" e mantêm a conta de pé. Elas
existiam desde 12/09/2026 **sem uma única afirmação encostando nelas**, e a do rejunte
serve um H2 diferente do normal, que era o que fazia a extração por título não achar
nada ali. Régua escrita para um mundo que nunca acontece nasce errada sem poder
falhar (seção 8). O render ganhou `sem_f2=1`, e a bancada agora mede esse mundo: a
conta continua, as duas vitrines dizem que a lista está fora do ar (uma cada), e
nenhum cartão de produto nem recusa é improvisado sem a régua que decide quem entra.

## O PORTÃO VERMELHO QUE JÁ ESTAVA NO main — a cópia da seção 24
Ao rodar a bancada inteira antes de fechar, `validar-banco.py` reprovava o
`dados/pecas.json` que a execução das 11h18Z criou (a cópia da primeira peça de
verdade, "Quadro flores do campo"). A régua era de 12/09 e dizia uma frase só: **o
arquivo não pode existir** — verdadeira enquanto o único jeito de ele aparecer fosse
alguém inventar o catálogo da artesã. Depois disso a **seção 24** entrou no contrato e
virou a mesa: dado que uma pessoa digita no WordPress nasce com cópia no repositório,
e o bloco não fecha sem ela. A proibição envelhecida passou a reprovar o repositório
por cumprir o contrato. A régua foi trocada: o que ela protege não é a ausência do
arquivo, é que ele seja **cópia e nunca fonte**. Três afirmações, e a do meio é a de
verdade: (1) o manifest o declara `publicar: false`; (2) **nenhum snippet o lê** —
medido no código que vai ao ar, com o comentário descartado —, porque peça inventada
só chega à tela se alguém servir o arquivo; (3) o arquivo tem a **forma da resposta do
endpoint** (id de post, URL no domínio da ilha, `total` que bate com a lista, e sem o
carimbo `gerado_em`, que a 24.2 mantém fora da cópia para a ronda não commitar a cada
passada). Quatro mutações novas na bateria do rejunte escrevem os quatro defeitos de
volta — cópia publicada, snippet lendo a cópia, total digitado, peça sem id.

## A VERIFICAÇÃO, EM NÚMEROS (bancada, 0 falha)
- **`teste-f1.php`**: nasceu a seção **4d** (ordem das duas vitrines) com 15 estados,
  um processo cada — marcador único, pastilha antes do rejunte, resposta antes das
  duas, as duas antes da prova, e nenhum título abrindo com conector, medido em 6
  títulos. Mais o mundo sem a F2 produzido. O arquivo foi de 190 para **211
  afirmações**.
- **`mutacoes-f1.py`**: de 40 para **46 mutações, 46 reprovadas, 0 passaram** — as
  seis novas: ordem invertida, o "E" de volta no título, a vitrine descendo para
  depois da prova (uma versão que reprova pela ordem, outra que preserva a ordem e só
  inverte compra x procedência), o marcador da pastilha sumindo, e o do rejunte
  sumindo SÓ na saída degradada.
- **`teste-prestacao-rejunte.php`**: 5 afirmações, 540 estados da F2 e 180 da F1, a
  extração do bloco do rejunte da F1 agora pelo marcador.
- **`validar-banco.py`**: OK, 25 materiais, 45 células da F2; a régua nova da cópia da
  seção 24 no ar.
- **`mutacoes-rejunte.py`**: de 12 para **16 mutações, 16 reprovadas** (as quatro
  novas da cópia da seção 24).
- **`validar-pastilhas.py`** 189, **`mutacoes-prestacao.py`** 11 de 11,
  **`mutacoes-cobertura.py`** 11 de 11, **`teste-casca.php`** 549, **`teste-f2.php`**
  107, **`teste-loja.php`** 178, **`teste-atelie.php`** aprovado, **`teste-leads.php`**
  211, **`conferir-cobertura.php`** 353, **`php -l`** limpo em tudo.

## NO AR (o desembarque)
Sync disparado UMA vez, revisao 31 com 10 aplicados; `/status` na revisao 31, igual
a do manifest. A F1 serve, no HTML servido, a vitrine da **pastilha antes** da do
rejunte, com os marcadores `cdm-f1-vitrine-pastilha` e `cdm-f1-vitrine-rejunte` e os
titulos **"Onde comprar a pastilha"** e **"Qual rejunte cabe nessa folga"** — nenhum
abrindo com conector. `conferir-no-ar.py`: **437 afirmacoes** (eram 416), 0 falha,
incluindo a ordem das duas vitrines medida em tres estados servidos.

## PROXIMO, com ordem e motivo
1. **A familia `/tecnicas/<slug>/`**, decisao de malha com o orcamento de rastreamento
   na mesa, e agora com peca publicada para linkar.
2. **`1x1` de fabricante**, a pendencia mais cara da categoria pastilha — sozinha muda
   7 das 12 linhas da tabela da F1.
3. **A categoria COLA**, 45 estados varridos e 0 com o minimo da 14.3.
4. Os 15 `url_busca`, no minuto em que houver sessao da Shopee.

14/09/2026 17:35Z — A FAMÍLIA DAS TÉCNICAS: o endereço é decidido, o banco da entidade TECNICA nasce, e a família NÃO nasce hoje

- **A escolha da ilha: SEGUNDA tentada.** Os cinco `ESTADO.md` estavam com
  `executando_desde: null`, que pela 1.1 já significa que não há bloco da
  Fundação vivo. Pela 18.1, ilha com despacho aberto do Raphael vem primeiro: a
  **ohmetria** tinha o despacho de nascimento de 14/09 e `ultima_execucao: null`,
  que é a mais antiga de todas. Reservei-a às 17h16Z e o push foi **RECUSADO**
  por segundos — outra execução gravou a reserva dela às 17h17Z (commit
  `a92f759`). Voltei ao passo 2 sem force push, como o passo 5 manda. Das que
  sobraram, nenhuma tinha despacho ABERTO para a Fundação: os de 14/09 da
  aquametria e da robometria estão marcados CUMPRIDOS e conferidos no ar, e o
  único item aberto do despacho da clubedomosaico é declarado pelo próprio texto
  como bloco de malha e não conserto. Valeu a rotação da seção 1 e a
  clubedomosaico tinha a `ultima_execucao` mais antiga (13h21Z). Reservada às
  17h18Z, push aceito.
- **Rede pela 20.2, antes de trabalhar:** home em 200 e `/status` na revisão 31,
  igual à do manifest, em UMA passada.
- **O BLOCO.** Era o item 1 da fila desta ilha desde 14/09 de manhã: a família
  `/tecnicas/<slug>/`, que o despacho do Raphael pediu pelo nome
  (`/tecnicas/Picassiete/`) e que a execução das 11h18Z classificou, com razão,
  como decisão de malha com o orçamento de rastreamento na mesa. **Decidido em
  `ARVORE.md`, seção 4b.**
- **O ENDEREÇO NÃO É A RAIZ, e essa metade é do contrato.** O
  `dados/corpus-buscas.md`, de 10/09/2026, escreveu o item 5 da fila como
  `/tecnicas/bizantino`. A seção 16.1 entrou em 11/09 e proíbe página solta na
  raiz além das cinco que ela nomeia. **O corpus estava certo no dia em que foi
  escrito e passou a contradizer o contrato no dia seguinte**, e ninguém viu
  porque a página nunca foi criada — é a mesma família do slug de categoria que
  o `VOZ.md` e a casca escreviam diferente até 11/09. Corrigido no corpus, com a
  nota de por quê. Nenhuma URL se moveu porque nenhuma existia.
- **A MÃE É `/como-fazer/`, e a técnica nasce filha DIRETA dela** — terceira
  aplicação de uma regra que este arquivo já tinha escrito duas vezes: *a mãe de
  hoje é a mãe que já tem endereço* (as duas ferramentas em `/materiais/`, a peça
  em `/loja/`). A categoria `/como-fazer/tecnicas/` fica registrada como
  candidata para o dia das três filhas (16.5).
- **POR QUE ELA NÃO NASCE HOJE — três portões, e os três medidos, nenhum
  opinião:** (1) seção 9, três itens de banco reais por página: **0 para 5 de 5
  técnicas**; (2) 16.5, três filhas: não há nenhuma; (3) 14.6 e 14.8, a rampa só
  é autorizada por número — e `dados/indexacao.md` tem **uma linha só**, de
  10/09/2026, escrita quando o WordPress ainda não existia (zero URL, zero
  impressão). **Nenhum número autoriza leva nova nesta ilha hoje**, de nenhuma
  família.
- **O ACHADO, e ele é mais estreito do que "falta banco":** as duas únicas
  técnicas cujo lado do material tem fonte (trencadís e picassiete) apontam para
  `caco_azulejo` e `caco_louca` — **caco de prato e de azulejo não têm
  fabricante**, e `caco_louca` nem sequer é valor possível de `tipo` para a
  categoria pastilha no vocabulário do esquema. Os 13 itens do banco de pastilhas
  são todos `pastilha_vidro`. A distância entre a técnica e o banco desta ilha é
  a distância entre o caco e o produto — e o caminho mais curto não é catalogar
  caco: é ligar a técnica à cola e ao rejunte, onde há 12 itens e uma ferramenta
  que já decide.
- **O QUE FOI ENTREGUE NO LUGAR DA PÁGINA: `dados/tecnicas.json`**, o banco da
  entidade TECNICA que o esquema previu em 12/09 e que nunca tinha nascido. Cinco
  técnicas, as mesmas cinco que a artesã pode marcar no ateliê, cada uma com
  definição sustentada por fonte de enciclopédia, museu ou instituição de ensino
  (Museo Nacional de Cerámica, Sagrada Família, Wikipedia, SPACES Archives,
  FASBAM, Câmara dos Deputados, repositório da Universidade Nova de Lisboa),
  consulta-alvo, SERP lida em 14/09/2026 com os domínios nomeados um a um, e
  `revisao_tecnica: pendente` — **porque nesta ilha a revisora existe e é a
  artesã**, e página que finge revisão que não houve é a única mentira que esta
  ilha pode contar sobre uma pessoa de verdade.
- **AS 10 FONTES FORAM COLHIDAS POR BUSCA E NENHUMA FOI ABERTA**, e isso está
  escrito em cada uma no campo `leitura`: `pt.wikipedia.org`, `britannica.com` e
  `google.com` devolveram `connect_rejected` às 17h30Z. É a regra do elo mais
  fraco da seção 10 aplicada à única entidade da ilha que não tem fabricante — e
  é o mesmo buraco de egresso que a escada de fontes já registrava do lado dos
  fabricantes, agora medido do lado das técnicas.
- **NADA FOI INVENTADO, e os campos vazios dizem por quê.** `junta_tipica_mm`
  nasce `null` em 5 de 5 porque nenhuma fonte declara folga em milímetro — e esse
  é justamente o campo que alimentaria o valor sugerido da F1. As três técnicas
  `opus_*` do vocabulário ficaram de fora com motivo: nenhuma é oferecida à
  artesã, então nenhuma peça poderia ser marcada com elas.
- **O PORTÃO QUE MEDE ISSO ESTAVA ESCRITO DESDE 12/09 E NUNCA TINHA RODADO.** A
  régua de TECNICA do `validar-banco.py` vivia imprimindo "tecnicas.json ainda
  não existe" — verde por ausência, que é função morta com outro nome. No dia em
  que o arquivo nasceu ela passou de primeira, e passar de primeira não é elogio:
  ela cobrava o que qualquer arquivo bem digitado teria. Passou a cobrar o que o
  esquema diz que esta entidade tem de especial: fonte obrigatória apontando para
  fonte que **existe**; origem dentro dos três níveis que o esquema aceita, lidos
  DO esquema e não recopiados; campo vazio exigindo o motivo ao lado; número só
  com fonte; e **o portão da família** — técnica não declara página com menos de
  3 itens de banco. A contagem por técnica passou a sair em toda execução.
- **`ferramentas/mutacoes-tecnicas.py`: 14 mutações, 14 decididas certo.** A
  bateria tem **os dois lados da fronteira** de propósito: 13 precisam reprovar e
  **uma precisa PASSAR** — a mesma página de técnica, com o lado do material
  resolvido, tem de abrir o portão. Sem ela ninguém saberia se o portão mede a
  contagem ou se apenas odeia o campo, e uma régua que reprova tudo nunca deixa a
  família nascer.
- **UM DESPACHO DO ARQUIPÉLAGO FECHADO SEM TRABALHO, e vale registrar por quê:**
  `dados/despachos.md` pedia que a próxima execução que reservasse esta ilha
  documentasse o parâmetro de autenticação do endpoint de peças. Ele **já estava
  documentado** no `PROMPT.md` desta ilha desde 13/09, com URL completa, nome do
  parâmetro e conferência no ar. Despacho fechado no destino não se apaga sozinho
  na origem; marcado como fechado lá.
- **UM DESVIO ENCONTRADO NO MAIN, de outra execução:** o commit `29099ba` das
  14h59Z — o que corrigiu a seção 7 do contrato — editou
  `ilhas/clubedomosaico/dados/especificacao-calculadoras.md`, arquivo de uma ilha
  que aquela execução **não tinha reservado** (seção 3: toque apenas na pasta da
  ilha que você reservou), e deixou o `sha256` do manifest desatualizado. O
  conteúdo da edição está certo e ficou; o sha foi recalculado aqui. É a mesma
  família da "outra metade que é do Raphael" já registrada em `despachos.md`: a
  reserva protege contra quem a lê.
- **VERIFICAÇÃO, 0 falha:** `validar-banco.py` aprovado com 25 materiais e a
  contagem nova por técnica (direto 0, indireto 0, bizantino 0, trencadis 0,
  picassiette 0); `mutacoes-tecnicas.py` 14 de 14; `mutacoes-rejunte.py` 16 de 16;
  `validar-pastilhas.py` 189; `teste-casca.php` 549 — incluindo o portão que
  cobra que documento e código digam a mesma coisa sobre a árvore, que a seção 4b
  nova não moveu.
- **NÃO HOUVE SYNC, e não é esquecimento:** nenhum arquivo `publicar: true` mudou
  neste bloco. `dados/tecnicas.json` nasce `publicar: false` porque nenhum snippet
  o lê — dado publicado que ninguém lê é a porta por onde uma cópia vira fonte sem
  ninguém decidir. A seção 4 só exige acionar o Sync em bloco que mexe em conteúdo
  publicável.
- **Próximo passo, e ele mudou de dono nesta execução:** a frase "link de loja em
  breve", que a seção 7 passou a proibir em 14/09/2026, **ainda está no ar nesta
  ilha** — `cdm_f2_compra_html()` a serve para todo item sem `url` e sem
  `url_busca`, e são **15 de 25** (13 pastilhas e 2 colas). É defeito no ar, e
  pela 18.5 vem antes de construção.

14/09/2026 18:45Z — A FRASE PROIBIDA SAI DA ILHA, e o desembarque parava numa camada que a purga não alcançava no primeiro Sync

- **Segundo bloco da mesma execução** (mutirão da seção 13: cada um passou pela
  verificação inteira antes do seguinte). O primeiro está na entrada anterior.
- **POR QUE ELE VEIO ANTES DE QUALQUER CONSTRUÇÃO NOVA (18.5):** fechando o bloco
  da família das técnicas, o `grep` de rotina achou `Link de loja em breve` sendo
  servido por `cdm_f2_compra_html()` — a frase que a **seção 7 do contrato passou
  a proibir em 14/09/2026**, no mesmo dia, e que a aquametria (39 itens) e a
  robometria (65 itens) tinham acabado de tirar das delas. Aqui eram **15 de 25**
  itens: 13 pastilhas e 2 colas, nos cartões da F2 e na vitrine de pastilha da F1,
  que chama a mesma função. Defeito no ar na ilha que eu tinha reservado.
- **O QUE FALTAVA NÃO ERA DECISÃO, ERA A TELA LER O CAMPO.** Dois dos 15 já tinham
  a palavra-chave da busca escrita em `afiliado.url_busca_produto` **desde 13/09**,
  e nenhuma linha de código a lia. É a mesma distância entre repositório e ar que a
  seção 4 do contrato paga mais caro, uma camada abaixo — e é literalmente o mesmo
  defeito que a aquametria nomeou hoje de manhã, na ilha ao lado.
- **A ESCADA DA SEÇÃO 25 GANHOU O DEGRAU 4** (f2 **1.5.0**): sem ficha e sem busca
  encurtada, a busca **crua** vira o botão. Ela sai `rel="nofollow noopener"` e
  **nunca** `sponsored`, e a decisão está registrada no código: `sponsored` é a
  declaração de uma relação **paga**, e ninguém paga por aquele clique. Chamar de
  patrocinado um link que não rende seria mentir ao leitor sobre a única coisa que
  ele tem o direito de saber sobre nós. O quinto estado — sem nenhuma das três —
  deixou de imprimir promessa: o bloco sai **vazio**, e quem impede esse item de
  chegar ao ar é o validador, com falha dura.
- **UMA PALAVRA-CHAVE ESTAVA ERRADA E MANDAVA PARA OUTRA ILHA.** O Silicone Acético
  Maxx buscava `silicone maxx tekbond **aquario**` — o nicho da Aquametria, copiado
  de lá junto com o padrão do campo. Quem faz mosaico chegaria na prateleira de
  aquário. Trocada por `silicone acetico maxx tekbond`. As 13 palavras-chave novas
  das pastilhas saíram de marca, código e o nome que a pessoa usa.
- **`itens_sem_piso` MORREU, e ele media a coisa errada.** Contava quem não tinha a
  busca **encurtada** e chamava isso de "sem piso" — duas perguntas coladas numa só,
  que davam o mesmo número **enquanto nenhum item tinha saída crua**: (1) o leitor
  tem para onde ir? e (2) esse clique rende comissão? Viraram duas contas:
  `itens_sem_saida_de_compra`, que agora é **erro duro** do validador e está em
  **0**, e `itens_com_piso_nao_rastreavel`, que é dívida de comissão e está em
  **15**. O campo velho é **recusado** pela régua: deixar o nome antigo conviver com
  o significado novo seria o pior dos mundos — o número continuaria batendo e
  diria outra coisa.
- **A PÁGINA DE DIVULGAÇÃO PASSOU A DIZER QUAL LINK PAGA E QUAL NÃO PAGA** (casca
  1.10.0), com seção própria e o "Estado de hoje" em duas contas. A frase "os links
  daqui são de afiliado" virou meia verdade no minuto em que a busca crua subiu
  para o botão.
- **O DESEMBARQUE E O CACHE: A PURGA SÓ VALE A PARTIR DO SEGUNDO SYNC.** Isto fecha
  o despacho de prioridade ALTA aberto na robometria, e o achado é maior que o
  despacho. A casca que **contém** a purga faz parte da carga que está sendo
  entregue: no Sync que a instala, o PHP já carregado é o **anterior**, então
  nenhuma purga roda. Medido minuto a minuto: às **17h40Z**, antes do bloco, as 11
  URLs serviam a assinatura do Endurance e o canônico **concordava** com a quebra
  de cache — não havia divergência, havia a janela. Às **18h29** o Sync da revisão
  32 aplicou com a casca 1.9.2 na memória, e aí o canônico ficou para trás: as duas
  páginas do bloco com entrada de 17h36Z e **a home com uma entrada de 13h53Z, do
  bloco anterior, velha havia cinco horas sem ninguém ver**. Às **18h34** um segundo
  Sync, já com a 1.10.0 carregada; poucos minutos depois o canônico servia o bloco
  novo nas onze URLs. São **duas camadas** e os cabeçalhos as nomeiam:
  `x-server-cache: true` e `x-proxy-cache` (nginx), com `max-age=7200`.
- **A AFIRMAÇÃO DO CACHE REPROVA PELA ORIGEM E RELATA O CANÔNICO**, e a escolha é
  deliberada: fazer o canônico reprovar transformaria toda entrega em duas horas de
  portão vermelho que ninguém consegue fechar, e portão assim se aprende a ignorar —
  que é pior do que não ter portão. Defeito de verdade é a **origem** não servir o
  bloco; canônico velho é janela, relatada com a hora da entrada e a da expiração.
- **DUAS RÉGUAS TINHAM PARADO DE MEDIR SEM FICAR VERMELHAS, e as duas foram
  consertadas:** (1) a mutação "cartão sem nenhum degrau some" procurava a classe da
  etiqueta proibida, que deixou de ser emitida — ela editava o snippet, o `if` nunca
  era verdadeiro, **nada sumia e a bateria ficava verde**; é a mutação inerte que a
  robometria nomeou hoje de manhã, aqui por outro caminho. (2) A soma dos degraus
  emitidos por um snippet só sobreviveu à mudança **dando o mesmo número por outra
  composição**: era 1 etiqueta + 1 botão de busca + 1 linha discreta = 3, virou 0 +
  2 + 1 = 3. Um degrau inteiro sumiu e outro nasceu com o portão verde ao lado.
  Agora cada degrau é contado pelo próprio marcador.
- **E TRÊS AFIRMAÇÕES QUE REPROVARAM UMA PÁGINA CERTA** foram reescritas por
  **escopo**, não afrouxadas: elas diziam da página inteira o que valia do cartão
  com ficha. É a mesma família da "afirmação em bloco com escopo maior do que o que
  foi medido" que a seção 7 do contrato nomeia.
- **VERIFICAÇÃO, 0 falha.** BANCADA: `teste-casca` 549, `teste-f2` 111 (eram 107),
  `teste-f1` 195, `teste-loja` 178, `teste-atelie`, `teste-leads` 211,
  `teste-prestacao-rejunte` 5 sobre 540 e 180 estados, `conferir-cobertura` 353,
  `validar-banco` aprovado, `validar-pastilhas` 189, `php -l` limpo.
  MUTAÇÕES: f1 46/46, **f2 50/50** (três novas: a busca crua declarando sponsored,
  a tela voltando a não ler o campo, e a crua passando na frente da ficha),
  rejunte 16/16, técnicas 14/14, pastilhas 14/14, cobertura 14/14, prestação 11/11.
- **NO AR:** revisão **33** no `/status`, igual à do manifest. `conferir-no-ar.py`
  com **450 afirmações** (eram 437), 0 falha. As 11 URLs em 200 e **zero**
  ocorrência da frase proibida; a vitrine de pastilha serve 3 botões de busca crua
  para os 3 elegíveis de 2 cm; a página de divulgação serve as duas contas.
- **Próximo passo, com ordem e motivo:** (1) o lado do material da família das
  técnicas — ligar técnica a cola e rejunte, que é onde esta ilha tem banco e
  ferramenta; (2) `1x1` de fabricante, que sozinho muda 7 das 12 linhas da tabela da
  F1; (3) a categoria COLA, 45 estados varridos e 0 com o mínimo da 14.3; (4) os 15
  `url_busca` encurtados, no minuto em que houver sessão do painel da Shopee — o
  piso já está na tela sem eles.

---

## 14/09/2026, 21h17Z — A PÁGINA DO PICASSIETE NASCE, e o que a impedia eram TRÊS RÉGUAS MAL LIDAS

**Ilha escolhida pela 18.1, segunda tentada.** Os cinco `ESTADO.md` parseavam em
`yaml.safe_load` e os cinco tinham `executando_desde: null`, que pela 1.1 já
significa que não há bloco da Fundação vivo — não houve reserva vencida para o
git desempatar. Três ilhas tinham despacho aberto do Raphael de 14/09
(clubedomosaico, ohmetria e jornadafly), empate de data, e a rotação da seção 1
desempatou: clubedomosaico com `ultima_execucao` 18h45Z, a mais antiga das três.
O primeiro push da reserva foi **recusado**, e não porque alguém pegou esta ilha:
outra execução reservou a aquametria às 21h18Z e o `main` andou. Voltei ao passo
2 sem force push, confirmei que a clubedomosaico seguia livre, e a reserva
passou. Rede pela 20.2, retestada e não herdada: home 200 e `/status` na revisão
33 — igual à do manifest — em três passadas.

### BLOCO A — o portão contava uma categoria que a página não recomenda

O despacho do Raphael de 14/09 tinha um item aberto: a página do Picassiete. Duas
execuções daquele dia responderam que ela não podia nascer, e a segunda delas
escreveu **três portões medidos** na `ARVORE.md` seção 4b. Os três decidiam
errado, e nenhum dos três erros era de dado — eram de leitura de régua:

**1. O portão de 3 itens de banco da seção 9 contava só TESSELA.** Ele perguntava
quantos produtos da categoria `pastilha` o banco tem com o tipo que a técnica
cita. As duas únicas técnicas com material declarado por fonte — trencadís e
Picassiete — apontam para `caco_azulejo` e `caco_louca`, e **caco de prato e de
azulejo não têm fabricante e nunca terão ficha de produto nesta ilha**. O portão
lia zero, e leria zero para sempre, por mais coleta que acontecesse.

Só que **a página de uma técnica não recomenda caquinho**. Ela responde *o que
comprar para colar aquele caquinho*, que é o eixo desta ilha escrito no
`PROMPT.md` — e isso é produto com fabricante, declaração datada e link de
afiliado. O item 6 da mesma seção 4b já dizia isso com todas as letras ("o
caminho mais curto não é catalogar caco: é ligar a técnica à cola e ao rejunte"),
enquanto o item 3 contava caco. **As duas metades da mesma seção discordavam, e
quem decidia era a que tinha número.**

É a mesma família da V24 da Aquametria, consertada poucas horas antes no mesmo
dia: uma régua que amarra o portão a um campo que o caso certo nunca preenche
reprova o mundo inteiro e **parece rigor**.

A conta passou a ser, escrita uma vez só, em `itens_de_banco_da_tecnica()` do
`validar-banco.py`: as pastilhas do banco cujo tipo é a tessela que a técnica
declara, **mais** as colas que o fabricante declara elegíveis para aquela tessela
em algum par base × ambiente do vocabulário. Resultado medido: trencadís **5**,
Picassiete **5**, e direto, indireto e bizantino seguem em **zero**, cada um com
o `motivo_sem_materiais` escrito dizendo por que não declara material. **Régua que
abre para todo mundo não mede nada** — é por isso que três das cinco continuam
fechadas, e é isso que separa conserto de porta dos fundos.

Três coisas ficaram deliberadamente fora da conta, e estão escritas no código:
menção com ressalva (fonte fraca demais para virar recomendação), o rejunte (a
régua dele decide por junta em milímetro e não olha a tessela; as cinco técnicas
têm `junta_tipica_mm` null) e qualquer comparação por texto.

**O que nasceu:** `ferramentas/tecnica-x-material.py`, que deriva
`dados/tecnica-x-material.json` **importando** a conta do validador em vez de
reescrevê-la — uma conta, dois leitores —, e
`ferramentas/mutacoes-tecnica-x-material.py`, com 9 mutações. Ela afirma o
**número**, não o veredito, e a razão é a mutação mais perigosa desta família: a
que **infla** a conta, faz o portão abrir mais cedo e continua verde porque
"abriu". Duas mutações inflam de propósito (contar ressalva; varrer todas as
tesselas em vez das declaradas) e são pegas pelo número.

**Uma expectativa minha estava errada e a bancada me corrigiu.** Na mutação que
encolhe a varredura para uma base só, previ que a união de colas ficaria em 5 e
os estados com o mínimo cairiam para 2 e 1; a medição devolveu 4, 6 e 3, e ela
estava certa. Ficou registrada dentro do arquivo, porque é o próprio argumento a
favor de afirmar número em vez de veredito: uma bateria que só perguntasse
"abriu ou fechou" teria passado nas duas contas, a minha e a certa.

**2. A 16.5 não se aplica.** Ela pede três filhas antes de a categoria nascer — e
a técnica de hoje nasce **filha direta** de `/como-fazer/`, não dentro de uma
categoria. A própria tabela do item 2 daquela seção já dizia isso.

**3. "Nenhum número autoriza leva nova" é o oposto do que a seção 21 manda.** A
21.1 é literal: abaixo do piso — 40 URLs publicadas e 21 dias desde a primeira
indexada —, zero impressão **não é informação** e **nunca** trava leva nenhuma.
Esta ilha tem 11 URLs e `piso: abaixo` escrito no cabeçalho, que é o campo que a
21.6 manda ler em vez de recalcular de cabeça. A armadilha é fina e por isso se
repete: quem lê a 14.8 ("é essa série que autoriza dobrar, manter ou parar") e
olha uma série de uma linha conclui corretamente que ela não autoriza nada — só
que **"não autoriza" e "proíbe" não são a mesma frase**. A Aquametria pagou isto
em 12/09 e a Clube do Mosaico em 14/09: duas ilhas, três dias. Virou a **21.8**
do `ARQUIPELAGO.md`, com a régua em duas perguntas na ordem.

### BLOCO B — a página, e ela não decide nada

`/como-fazer/o-que-e-mosaico-picassiete/`, nível 3 com a mãe de nível 1 direto —
o mesmo estado de transição em que a F2 e a F1 vivem desde o bloco 4. **Não é
`/tecnicas/Picassiete/`**, que foi o endereço que o despacho pediu: a 16.1 proíbe
página solta na raiz desde 11/09, e o slug é a consulta-alvo do banco.

**Nenhuma linha do snippet escolhe cola.** Quem escolhe é `cdm_f2_celula_cola()`,
a régua da F2 que está no ar desde 11/09, chamada aqui para o caquinho de louça.
A grade tem 45 células — 9 superfícies × 5 lugares —, é servida no HTML e é
recalculada a cada requisição. É a tabela pré-renderizada da seção 5 do contrato:
um modelo de linguagem lê os 45 casos sem preencher formulário nenhum. O texto, a
definição e as fontes saem de `dados/tecnicas.json`, que passou a `publicar: true`
porque agora existe snippet que o lê.

**A prestação de contas da seção 7 fecha com o banco:** das 7 colas, 5 entram na
vitrine e as 2 que ficam de fora são nomeadas em linha própria. **E isso virou
conserto dentro do próprio bloco:** a primeira versão escrevia só o balde de maior
contagem, e o Durepoxi cai por silêncio em 25 células **e** entra com ressalva em
20 — dizer só o silêncio faria a página afirmar que o fabricante nunca nomeia uma
daquelas superfícies, o que é falso em 20 delas. A seção 7 é explícita desde
12/09: causa que o código separa, o texto separa. Agora o código separa quatro
baldes e o texto separa quatro.

**A recusa:** a página não responde o rejunte, e diz por quê — ele se decide pela
largura da junta em milímetro, e nenhuma fonte colhida sobre Picassiete declara
essa folga. Onze das 45 células dizem, com todas as letras, que não há cola que o
fabricante sustente.

**A casca subiu para 1.11.0 por um motivo de malha, não de vitrine.** Com um link
só, vindo da mãe, a página nasceria **órfã** pela 16.4(f), e o portão do
`teste-casca` pegou isso na hora. A Escola e a home passaram a listar as técnicas
em **bloco próprio**, separado dos tutoriais: técnica é "o que é isso", tutorial é
"como se faz", e juntá-las faria a Escola prometer um passo a passo que a página
de técnica não entrega.

**Duas dívidas de texto do banco viraram defeito no ar e foram pagas aqui.** O
`dados/tecnicas.json` nasceu sem acento — "louca", "xicara", "monumento historico"
— porque até hoje só era lido por ferramenta; no dia em que uma **página** passou
a servi-lo, virou português errado na tela, que é exatamente a cicatriz que o
`restaurar-acentos.py` desta ilha existe para lembrar. Vieram junto as aspas
tipográficas: aspa reta vira `&#039;` no `esc_html` e o filtro de conteúdo do
WordPress escapa o `&` de novo, servindo a entidade crua ao leitor. A troca dos
acentos tem **prova**: reduzido a sem-diacrítico, o arquivo é idêntico ao de
antes, fora de 10 frases do campo `leitura` reescritas de propósito e declaradas
uma a uma.

### Verificação

**Bancada, 0 falha:** `teste-tecnicas.php` com **52** afirmações — e o esperado
das 45 células **não vem do snippet**: vem de `dados/cobertura.json`, gerado pela
régua em Python, que é implementação independente em outra linguagem, escrita no
bloco 3 antes de existir uma linha do PHP. Ele começa rodando
`cobertura.py --conferir`, porque régua velha aprova a página de ontem. Mais:
`teste-casca` 549, `teste-f2` 111, `teste-f1`, `teste-loja`, `teste-atelie`,
`teste-leads`, `teste-prestacao-rejunte`, `validar-banco`, `validar-pastilhas`,
`tecnica-x-material --conferir`, `php -l` limpo nos sete snippets.

**Mutações:** 9 da página, 9 da conta e as 14 do banco de técnicas — 32 no total,
todas decididas certo. A nona da página **não reprova por reprovar**: com o banco
fora do ar ela exige a página **honesta**, dizendo que não mediu e sem servir a
grade.

**Uma seção do teste foi apagada pelo próprio autor.** A primeira versão do
`teste-tecnicas.php` tinha uma seção 8 que imprimia `ok` sem medir nada — o
caminho sem banco não cabe num teste cuja bancada carrega as options na entrada do
processo. Ela virou aquela nona mutação, e o motivo de ter saído ficou escrito no
cabeçalho do arquivo: afirmação que não pode falhar é pior que afirmação ausente.

**No ar:** `ferramentas/conferir-tecnica-no-ar.py`, **23 afirmações sobre o HTML
que o site serve**. Ele reconta as 45 células contra o banco commitado, refaz a
prestação de contas na tela, confere a escada de compra e o `rel` de cada link, os
dois links internos que tiram a página da condição de órfã, o sitemap e o JSON-LD
servido. A seção 4 dele compara o **endereço canônico** com o mesmo endereço com
quebra de cache, por marcador e nunca por bytes — é a trava do cache do
hospedeiro, que o `/status` não enxerga. Sync da revisão 34 às 21h51Z, 12
aplicados em **um** disparo; canônico e versão sem cache iguais nos cinco
marcadores deste bloco.

### Próximo passo desbloqueado

**A segunda página de técnica: o trencadís.** Não sobrou portão — ela reúne os
mesmos 5 itens de banco, a SERP dela está classificada como ABERTA, e a máquina
inteira já existe. **Uma diferença que o Picassiete não tinha:** o trencadís
declara **duas** tesselas (`caco_azulejo` e `caco_louca`), e a página de hoje
resolve a primeira da lista — quem escrever decide se serve duas grades ou uma, e
diz qual na tela. O teto da 21.4 está longe: esta leva teve **uma** URL.

Depois dela, na ordem: a coleta das quatro categorias vazias do vocabulário
(`alicate`, `base`, `acabamento`, `apoio`), que é o que destrava o bloco 4c e que
nenhuma coleta de cola ou rejunte fecha; e a linha da peça na tabela da seção 5 do
`ARVORE.md`, que é conserto de **teste** e não de documento — o que falta está
escrito lá.

14/09/2026 23h19Z — A FAMILIA DAS TECNICAS VIRA FAMILIA: nasce a pagina do trencadis, e a grade passa a ser medida POR CAQUINHO (tecnicas 1.1.0, manifest revisao 35)

UMA URL nova: `/como-fazer/o-que-e-trencadis/`, a segunda filha da Escola e a
segunda e ultima que o portao da secao 4b do `ARVORE.md` autoriza hoje. Nenhuma
peca entrou ou saiu; nenhuma URL mudou de endereco.

- **A ESCOLHA DA ILHA: TERCEIRA TENTADA, DUAS PERDIDAS NA CORRIDA DO PUSH.** Os
  cinco `ESTADO.md` do `main` real tinham `executando_desde: null`, que pela 1.1
  ja significa que nao ha bloco da Fundacao vivo. Pela 18.1 li o topo dos cinco
  `PROMPT.md` antes da rotacao e **nenhuma ilha tem despacho aberto para a
  Fundacao**: os quatro itens do despacho da Sentinela de 14/09 na robometria
  estao CUMPRIDOS e o quinto e um achado de metodo endereçado ao Raphael (uma
  linha da 25.4 do contrato); os da ohmetria e da jornadafly sao despachos de
  NASCIMENTO, que carregam a fila inteira e nao cabem na 18.2; os desta ilha
  morreram conferidos no ar as 21h17Z. Sobrou a rotacao da secao 1. Pedi a
  robometria (19h17Z, a mais antiga) e o push foi recusado — outra execucao a
  reservou as 23h16Z e uma terceira reservou a jornadafly as 23h18Z. Voltei ao
  passo 2 sem force push e a clubedomosaico, que era a proxima da ordem (21h17Z),
  foi aceita as 23h19Z. Nenhum branch `claude/*` e nenhum PR aberto para mesclar.
- **REDE PELA 20.2, antes de trabalhar:** home em 200 e `/status` na revisao 34,
  igual a do manifest, em TRES passadas.

**O QUE O BLOCO ENTREGOU, e a parte que vale para as proximas paginas nao e a
pagina.** O `PROMPT.md` deixava uma escolha escrita para quem publicasse: *"o
trencadis declara DUAS tesselas e a pagina de hoje resolve a primeira — quem
escrever decide se serve duas grades ou uma, e diz qual na tela"*. **Ela nao foi
escolhida, foi medida.** O snippet passou a calcular **uma grade por caquinho** e
a **agrupar as que saem identicas**, celula a celula; as duas do trencadis saem
iguais nas 45, entao a pagina serve **uma** tabela e diz na tela que **comparou as
90** e por que elas empatam.

**A CAUSA, e ela e de uma linha da regua da F2:** o caquinho entra na decisao num
lugar so — `cdm_f2_condicao_cumprida()`, a condicao de superficie porosa que o
Cascola PL500 declara — e o esquema classifica `caco_azulejo` e `caco_louca` como
POROSOS os dois. Medido sobre `dados/cobertura.json`, que e a metade
independente: dos seis caquinhos do vocabulario, os **quatro porosos**
(`pastilha_ceramica`, `caco_azulejo`, `caco_louca`, `pedra`) tem as 45 celulas
**identicas entre si**, e os **dois que nao absorvem** (`pastilha_vidro`,
`caco_espelho`) divergem deles em **4 celulas**, sempre as mesmas quatro. **A
grade nao depende do caquinho: depende da CLASSE de porosidade dele.** Isso nao
virou frase escrita na pagina — a comparacao e recalculada a cada carregamento,
porque frase que resume uma medicao e a primeira coisa a envelhecer sozinha.

**O RAMO DAS DUAS TABELAS EXISTE E E MEDIDO, embora o banco de hoje nao o pise.**
`mutacoes-tecnicas-pagina.py` fabrica o mundo em que o trencadis declara
`caco_louca` e `caco_espelho` — um poroso e um nao —, exige **duas** tabelas e
exige que o teste **APROVE**; e a mutacao seguinte quebra o agrupamento no mesmo
mundo e exige que ele **REPROVE**. E a disciplina da borda fabricada: grade que
so pisa no caso que o banco tem hoje nao e grade.

**O SNIPPET DEIXOU DE SER UMA PAGINA (tecnicas 1.0.0 -> 1.1.0).** Id, slug e
titulo eram tres constantes; agora moram em `cdm_tecnicas_registro()` e cada
pagina tem **shortcode proprio** (`[cdm_tecnica_<id>]`). A razao nao e asseio: a
bancada descobre QUE pagina esta medindo casando o shortcode com a definicao de
paginas (`cdm_teste_caminho_da_pagina`), entao duas paginas com o mesmo shortcode
seriam medidas como uma so — a primeira duas vezes, a segunda nenhuma — e o verde
continuaria la. Esta medido pela mutacao `as duas paginas voltam a servir o MESMO
shortcode`. O `[cdm_tecnica]` da 1.0.0 continua registrado como atalho que resolve
pelo endereco servido, para o caso de a reescrita do conteudo da pagina nao pegar
no Sync.

**E `cdm_teste_paginas_no_ar()` PAROU DE LISTAR PAGINA DE TECNICA A MAO.** A
primeira entrou escrita; a segunda mostrou o custo na hora — a mae deixou de
listar a filha e as duas afirmacoes da 16.4(a) reprovaram num arquivo de bancada
que nada tem a ver com a pagina. A lista passou a sair do registro do snippet.

**DUAS REGUAS INERTES, ACHADAS DE PASSAGEM E CONSERTADAS NA MESMA EXECUCAO** — e
as duas sao da mesma familia, a de regua amarrada a um numero que o banco move:
- `dados/tecnicas.json` dizia de si mesmo `publicacao.publicar: false`, com o
  motivo *"nenhum snippet le este arquivo"*, escrito antes de existir pagina de
  tecnica — enquanto o manifest ja gravava a option que a pagina do Picassiete le
  desde 14/09. As duas metades estavam certas no dia em que foram escritas, que e
  sempre como esta divergencia nasce. Agora o `teste-tecnicas.php` exige que as
  duas digam a mesma coisa.
- A mutacao `slug de categoria foge do VOZ.md`, em `mutacoes-arvore.py`, estava
  amarrada a linha inteira da tabela do `ARVORE.md` com **"5 itens"** dentro. O
  banco de colas cresceu para 7, a mutacao parou de achar o alvo e essa trava
  ficou **inerte** — sem reprovar nada e sem acusar nada. O alvo passou a ser so
  o endereco: a bateria voltou de 20 para **21 mutacoes decididas**.

**O QUE A PAGINA DO TRENCADIS ENTREGA, e nao e o mesmo que a irma.** A definicao
e a origem catala vem do Museo Nacional de Ceramica (exposicao "Gaudi &
trencadis"); a resposta de com o que colar sai das 45 combinacoes de superficie e
lugar, 11 delas dizendo com todas as letras que nao ha adesivo que o fabricante
sustente. E ela tem uma **segunda recusa** que a do Picassiete nao tem: **o caco
de vidro comum**. As fontes citam vidro entre os cacos de Gaudi e o vocabulario
`material_tessela` desta ilha nao tem valor para caco de vidro de garrafa — tem
`caco_espelho`, que e vidro com prata atras e cai do outro lado da conta que
decide a cola. Responder pelo mais parecido seria trocar um material por outro no
meio de uma recomendacao, entao a pagina diz que nao responde e por que. Fica
como **divida de vocabulario**, nao como defeito de pagina.

**BANCADA, 0 falha:** teste-tecnicas **123** afirmacoes (era 52, e agora varre as
DUAS paginas), teste-casca 549, teste-f2 111, teste-f1 195,
teste-prestacao-rejunte 5 (540 estados da F2 e 180 da F1, um processo cada),
teste-loja, teste-atelie e teste-leads aprovados, validar-banco e
validar-pastilhas OK, `php -l` limpo. **MUTACOES:** mutacoes-tecnicas-pagina **14
de 14** (eram 9), mutacoes-tecnicas 14 de 14, mutacoes-tecnica-x-material 9 de 9,
mutacoes-arvore **21 de 21** (era 20 medindo e uma inerte). A bateria inteira da ilha foi rodada, nao so a do bloco: mutacoes-cobertura 14 de 14, mutacoes-voz-e-cabeca 24 de 24, mutacoes-pastilhas 14 de 14, mutacoes-rejunte 16 de 16, mutacoes-prestacao 11 de 11 — todas decidindo certo.

**NO AR:** Sync as 23h42Z, `/status` na revisao **35**, igual a do manifest, em UM
disparo com 12 aplicados. `conferir-tecnica-no-ar.py` **54 afirmacoes, 0 falha**,
agora varrendo as duas paginas e comparando uma com a outra — titulo, description
e primeiro paragrafo tem de ser diferentes, porque duas paginas geradas pelo mesmo
codigo sao o jeito mais facil de uma ilha publicar malha fina sem que nenhuma
medicao acuse. `conferir-no-ar.py` **450 afirmacoes, 0 falha**. O endereco
canonico ja servia o conteudo novo na primeira medicao, batendo com a versao com
quebra de cache nos cinco marcadores deste bloco.

**PROXIMO PASSO DESBLOQUEADO:** o eixo das tecnicas **ficou sem proxima pagina** —
as duas que o portao autoriza nasceram. As tres que seguem em ZERO (direto,
indireto, bizantino) sao trabalho de **FONTE**, nao de texto: nenhuma declara
material, e o bizantino e o de maior valor de indexacao da ilha. O que destrava
mais coisa continua sendo a **coleta das quatro categorias vazias do
vocabulario** (`alicate`, `base`, `acabamento`, `apoio`), que e o que abre o bloco
4c — e o canal de busca alcanca, o egresso direto aos dominios de fabricante nao.
A semana da 21.4 esta em **2 de 3 levas**, uma URL cada.

---

## 24/09/2026, 19h40Z — A ILHA ESTAVA FORA DO AR. A execução inteira foi levantá-la

**Primeira execução da Fundação depois de a ilha entrar em foco, e ela não criou
uma URL sequer.** O despacho do Raphael de 24/09 manda **medir antes de
construir**, e foi a medição de rede da seção 20.2 — o `curl` barato do começo de
execução — que achou o que nove dias de silêncio esconderam.

### O QUE FOI MEDIDO, às 19h20Z

**16 das 17 URLs do sitemap serviam a página de estacionamento da HostGator, com
404.** `/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`, `/loja/`,
`/materiais/quantas-pastilhas-para-mosaico/`, `/como-fazer/o-que-e-trencadis/`,
`/como-fazer/o-que-e-mosaico-picassiete/`, as cinco peças da Loja, mais
`/wp-sitemap.xml`, `/robots.txt` e `/wp-json/`. **Só a home respondia.** As três
páginas que a leitura semanal de 23/09 mediu na primeira página do Google —
posições 7,8 · 9,1 · 7,0 — estavam entre as mortas.

**O WordPress estava inteiro, e é isso que nomeia a causa.** A busca interna
(`/?s=picassiete`) renderizava, achava a página do picassiete e listava as URLs
de todas as outras; o Sync aplicava a revisão 35 sem erro; o `/status` respondia.
Tudo que é **arquivo de verdade** (`/`, `/index.php`, `/wp-login.php`) ou **query
na raiz** (`/?s=`, `/?rest_route=`) passava. **Todo caminho bonito morria ANTES de
chegar no PHP.**

Medido oito vezes por URL, determinístico. A irmã `aquametria`, no **mesmo IP**
(108.179.253.218), servia sitemap, robots e wp-json em 200 — então não era o
plano, não era o túnel e não era a rede desta nuvem.

### UMA MEDIÇÃO QUE ATRAPALHOU, e fica escrita porque atrapalharia de novo

Às 19h16 a `/materiais/qual-cola-usar-no-mosaico/` ainda respondia 200. Às 19h21,
depois de eu disparar o Sync, ela virou 404 como as outras. **Não foi o Sync que
quebrou a ilha** — ela já estava quebrada quando a medição começou. O que aquela
URL tinha era um HTML cacheado em disco, que é **arquivo de verdade** e por isso
passava pela porta fechada; a purga do Sync o apagou. Aquele cache expirava
sozinho às 20h09 (`max-age=7200` a partir de 18h09). Fica registrado para
ninguém ler a sequência como causa.

### A CAUSA, medida de dentro do servidor

A casca ganhou a **seção 6** e a rota
`?rest_route=/clubedomosaico/v1/rotas&token=<token do Sync>`, que devolve o
retrato do roteamento por dentro. Ela respondeu:

```
permalink_structure : /%year%/%monthnum%/%day%/%postname%/
regras_no_banco     : 115
mod_rewrite         : true
raiz_gravavel       : true
htaccess            : /home3/rapha921/clubedomosaico.com.br/.htaccess
                      existe, legivel, gravavel, 1057 bytes
blocos              : ["NFD EPC"]
tem_wordpress       : false
```

**O `.htaccess` tinha um bloco só — `NFD EPC`, o do Endurance Page Cache do
hospedeiro — e não tinha o `# BEGIN WordPress`.** Sem esse bloco o Apache não
manda para o `index.php` nada que não seja arquivo existente, e o WordPress
deixa de receber todo caminho bonito. Um arquivo, sete linhas ausentes, a ilha
inteira fora do índice.

### O REPARO, com o antes e o depois na mesma resposta

`&reparar=1` roda `flush_rewrite_rules( true )` — o mesmo que salvar
Configurações > Links permanentes, que é o conserto que a documentação do
WordPress manda fazer para este defeito:

```
antes   1057 bytes   blocos NFD EPC             tem_wordpress false   rewrite  8
depois  1580 bytes   blocos NFD EPC,WordPress   tem_wordpress true    rewrite 15
```

**As 17 URLs voltaram a 200 no minuto seguinte**, junto com `wp-sitemap.xml`,
`robots.txt`, `wp-json` e `/author/mosaico_gestor/`. A **F2 voltou a responder
consulta**: `?cdm_base=vidro&cdm_tessela=pastilha_vidro&cdm_ambiente=externo`
saiu de 404 com 2.361 bytes de página do hospedeiro para 200 com 121.077 bytes
da ferramenta. Enquanto a porta esteve fechada, quem chegasse pela busca em
"cola para mosaico", na posição 7,8, e preenchesse o formulário **recebia a
página de estacionamento da HostGator** — as duas ferramentas desta ilha são GET
para a própria página.

### E O CONSERTO DURA — medido, não suposto

A suspeita óbvia era `cdm_casca_purgar_cache()`, que apaga arquivo e roda a cada
Sync desde 14/09. **Não foi ela**, por dois argumentos e o segundo é mais forte
que o primeiro: (1) ela só esvazia `wp-content/endurance-page-cache/`, com
`realpath` conferido a cada nível da recursão, e nunca encosta na raiz; (2)
**depois do reparo, um Sync novo reescreveu o `.htaccess` (mtime novo, 1579
bytes) e MANTEVE o bloco do WordPress** — o EPC preserva o que encontra. As
quatro URLs reconferidas depois dessa purga continuaram em 200.

**A causa de origem continua sem nome, e fica escrito assim.** O que tem nome é o
sintoma, o portão que o pega e o reparo que o desfaz. Causa inventada seria a
próxima execução consertando a coisa errada.

### O PORTÃO QUE FALTAVA, e por que ele faltava

`conferir-no-ar.py` media 450 afirmações e **teria** acusado este defeito — ele
gruda quebra de cache em toda URL, então toda leitura dele já era uma URL com
query, que era exatamente a forma que morria. **O que faltou não foi
sensibilidade, foi alguém rodar:** a ilha passou de 15/09 a 24/09 sem bloco.

O que ele **não** cobria são as três URLs que o Google usa e que **nenhuma página
desta ilha linka** — e é por não serem linkadas que nunca entraram na lista de
nenhum portão. Entraram agora:

- `/wp-sitemap.xml` em 200 com `content-type` de XML, **e trazendo XML de sitemap
  de verdade** em vez da página do hospedeiro;
- `/robots.txt` em 200 e `text/plain`;
- `/wp-json/` em 200 e `application/json`;
- **o 404 que tem de ser 404**: caminho inexistente responde 404 **na página desta
  ilha**, não na do hospedeiro. Portão que só cobra 200 aprova um servidor que
  responde 200 para tudo.

**456 afirmações, 0 falha**, medidas no HTML servido, a ilha inteira.

### A REGRA SUBIU PARA O CONTRATO — seção 29 do `ARQUIPELAGO.md`

Porque o motivo vale para toda ilha, não só para esta: **todo portão desta
fábrica entra pela porta que continuou aberta.** O Sync é `/?<ilha>_sync=`, uma
query na raiz; o `/status` é rota REST; a bancada roda sem site e sem rede, por
desenho. O `/status` respondeu a revisão certa o tempo inteiro e a bancada fechou
verde — as duas coisas eram verdade e irrelevantes. Entrou nas **três linhas** do
mapa de leitura, porque regra que ninguém lê é regra morta.

### A CÓPIA DA SEÇÃO 24 ESTAVA TRÊS PEÇAS ATRASADA

A Loja tinha **1 peça no repositório e 5 no ar**. A artesã cadastrou quatro entre
15 e 16/09 — Quadro Divino Espírito Santo (15/09), Vaso com flores em cerâmica,
Quadro Nossa Senhora Aparecida e Bandeja em madeira (16/09) — e **nenhuma
execução passou aqui desde então para buscá-las**. É o dado que a 24 chama de
único que não se reconstrói a partir do repositório, e é o trabalho da mãe do
Raphael. Gravado em `dados/pecas.json`, **formatado e não numa linha só**: cópia
sem diff legível não é histórico, e histórico é o ganho que a 24.4 nomeia.

### O DESPACHO DO RAPHAEL DE 24/09, pela 18.3

**Saiu:** o **BLOCO D**. `urls_publicadas` passou de 13 para **17**, contado no
sitemap no ar às 19h33Z — 12 em `wp-sitemap-posts-page-1.xml` (`/`, `/loja/`,
`/materiais/`, `/como-fazer/`, `/sobre/`, `/contato/`,
`/divulgacao-de-afiliados/`, `/privacidade/`, `/materiais/qual-cola-usar-no-mosaico/`,
`/materiais/quantas-pastilhas-para-mosaico/`, `/como-fazer/o-que-e-mosaico-picassiete/`,
`/como-fazer/o-que-e-trencadis/`) e 5 em `wp-sitemap-posts-peca-1.xml`.
`primeira_indexacao` continua `desconhecida`, como o bloco manda.

**Ficou, reescrito no `PROMPT.md` com o motivo em uma linha:** o **BLOCO 0** (o
`sub_id` deslocado uma casa) e os **BLOCOS A, B e C**. A ilha estava fora do ar,
e a 18.5 manda verificação antes de construção.

**E uma coisa que o próximo bloco precisa saber:** o BLOCO A é sobre **CTR de três
páginas na primeira página do Google**, e essas três páginas passaram pelo menos
um dia servindo 404 ao Google. **A série de `dados/posicoes.md` tem um buraco que
não é de CTR.** Trocar título agora mistura duas causas na mesma janela de
medição — quem fizer o BLOCO A decide isso com o número de 30/09 na mão e escreve
qual leitura está usando.

**PRÓXIMO PASSO DESBLOQUEADO:** o **BLOCO 0** do despacho do Raphael — o `sub_id`
da Shopee gravado como `-clubedomosaico-F2--`, deslocado uma casa, com
`sub_id_1` vazio. É o primeiro da fila, não divide passada com nada, e agora tem
uma ilha de pé embaixo dele. Nenhuma página nova nesta passada; a semana da 21.4
continua em **2 de 3 levas**.

---

## 2026-09-25, 10h16Z → 10h45Z — BLOCO 0 DO DESPACHO DO RAPHAEL DE 24/09: OS 31 LINKS DE SHOPEE RENASCEM COM O `sub_id` NA CASA CERTA

**Ilha em foco** (`foco.md`, desde 24/09). Reserva às 10h16Z, commit `105746f`. Rede conferida antes de
trabalhar (20.2): home, `/materiais/`, `/wp-sitemap.xml`, `/como-fazer/`, `/loja/` e `/sobre/` em 200 — a
porta de entrada consertada ontem continua de pé, que é o que `dados/consertos.md` mandava reconferir.

### O DEFEITO, E POR QUE ONZE DIAS NÃO BASTARAM PARA ALGUÉM VER

O único clique desta ilha na janela 16→22/09 chegou ao Relatório da Shopee como `-clubedomosaico-F2--`:
cinco campos, o **primeiro vazio**, tudo deslocado uma casa. A seção 7 manda `sub_id_1` = nome da ilha e
`sub_id_2` = código da ferramenta, e sem o campo 1 o painel não responde *"qual ilha vendeu"*.

**O banco estava certo o tempo todo.** `sub_id_1: "clubedomosaico"` e `sub_id_2: "F1"/"F2"` estavam
gravados em todos os 25 registros desde 13/09, e o `validar-banco.py` cobrava isso num portão próprio.
O que ninguém media era o **link** — e os 16 links nasceram no painel `offer/custom_link`, com os cinco
campos preenchidos **à mão**. **Mão humana em cinco caixas de texto não tem portão; chamada de API tem.**
É a seção 4 de novo, com outro nome: o banco é o resumo e o link é o fato.

### O QUE FOI FEITO — 31 LINKS, PELA OPEN API

| o quê | quantos | de onde saiu |
|---|---|---|
| ficha de produto regerada | 6 | do `url_produto` já gravado, que é da Shopee — os dois campos vêm da mesma URL crua conhecida, e o par continua demonstrável (25.4-b.1) |
| busca encurtada regerada | 10 | palavra-chave **reescolhida inteira**, nunca grampeada ao link velho |
| busca encurtada NOVA | 15 | esperavam sessão do painel desde 13/09 |
| Mercado Livre | 4 | **não tocados** — outro programa, com `etiqueta_ml` própria e reCAPTCHA no gerador (25.6) |

**Os 15 que esperavam sessão são a 25.4-b.3 em ação.** O `motivo_sem_url_busca` deles dizia, desde 13/09,
que o encurtamento *"exige a sessão logada"*. Era verdade naquele dia e deixou de ser **três dias depois**,
quando a Open API entrou — e, enquanto esteve escrito, mandava toda execução seguinte **nem tentar**.

**Os 10 que tinham link e não tinham busca crua são a 25.4-b.1.** A tentação era buscar uma palavra-chave
nova e grampeá-la ao lado do link antigo: o campo ficaria preenchido e a dívida iria a zero. Seria fabricar
a aparência de um par que ninguém mediu. Os dois campos saíram da mesma passada, e o link velho foi
descartado, não remendado.

### O ACHADO QUE NÃO ESTAVA EM NENHUM BLOCO: AS TREZE CHAVES DAS PASTILHAS DEVOLVIAM ZERO

Conferindo as palavras-chave contra a API **antes** de gerar link — que é o que a 25.4-b manda, porque
*"busca não esgota, mas muda de nome"* — as **treze** das pastilhas devolveram **zero oferta**:
`Glass Mosaic <código> pastilha de vidro <medida>`. A marca não é anunciada por nome na Shopee e código de
catálogo não aparece em título de anúncio. **O piso levava a uma busca vazia**, que é exatamente o beco sem
saída que o degrau 4 da 25.1 existe para impedir — e estava assim desde 13/09, com o botão na tela, sem
que nada acusasse.

A descida da escada de palavra-chave da 25.6 parou na **família** (medida e acabamento), com o degrau
escrito em `motivo_da_chave` de cada registro: `pastilha de vidro cristal 2,5`, `pastilha de vidro 3x3`,
`pastilha de vidro 2x2`, `pastilha de vidro 2,3`, `pastilha de vidro 1,5x1,5` e, para o strip de 1,2 cm,
`pastilha de vidro placa 30x30`. **Dois degraus ficaram barrados e o motivo é da 25.7:** código sozinho
(`K2501` devolve grade traseira de aspirador **Karcher**) e `pastilha de vidro` pelado (devolve pastilha de
**freio**). O que sustenta a busca é a **medida** junto do substantivo.

**O que se perde na descida, dito sem maquiar:** a busca deixou de prometer *aquele código* e passou a
prometer a família. **É o que um piso é** — "ver outras ofertas", nunca "este produto". Nenhuma ficha,
nenhum preço e nenhuma foto saiu daí; casamento de item continua proibido pela 25.7.

Uma chave das dez reescritas também caiu: `argamassa cimentcola externo ac-ii quartzolit` devolveu zero —
a Shopee anuncia **AC-2/AC-3** e quase nunca escreve a numeração romana. Virou
`argamassa cimentcola externo quartzolit`. **As 25 palavras-chave do banco devolvem oferta hoje**, medido.

### OS PORTÕES, QUE SÃO O QUE IMPEDE ISSO DE VOLTAR

1. **`ferramentas/conferir-sub-id.py`** (raiz do repositório, vale para todas as ilhas). Gera um link de
   **bancada** e lê o `utm_content` do **301** do encurtador, **sem seguir o redirecionamento**:
   `bancada-t0---`. Esse é, letra por letra, o formato do Relatório de cliques.
   **E o link é de bancada de propósito:** o salto do encurtador é onde a Shopee conta o clique. Conferir
   os 31 links da ilha por esse caminho gravaria 31 cliques com a etiqueta `clubedomosaico`, justo na
   semana em que a leitura semanal procura o **primeiro clique orgânico** (proposta 3 de 23/09). O
   mecanismo se prova **uma vez**; os links da ilha saem certos **por construção**, pela mesma função.
2. **`conferir-no-ar.py` ganhou a seção "O link de afiliado servido"**: varre as URLs do sitemap e reprova
   se aparecer encurtador de Shopee que o banco não conhece — mais uma afirmação de que ela **encontra
   algum**, senão o portão aprovaria por vacuidade. Pega link velho sobrevivendo na tela depois de uma
   regeração, que é defeito **mudo**: o link antigo continua vivo na Shopee, nada dá 404, e a ilha só perde
   a atribuição.
3. **`validar-banco.py`: `piso não rastreável` e `busca sem endereço cru` deixaram de ser aviso e viraram
   ERRO DURO.** O próprio comentário do arquivo prometia isso *"no dia em que o número chegar a zero"*.
   Chegou. `ausente` continua diferente de `tentado-e-falhou` (25.2-b): registro com `motivo_sem_url_busca`
   escrito passa; o que não passa é o silêncio. **As duas mutações reprovaram.**
4. A regra subiu ao contrato como **seção 25.8**.

**A régua de 14/09 que media a dívida teve de mudar de objeto, e ficou com a história junto.** A afirmação
`[F1 2 cm]` contava **botões de busca CRUA**, um por elegível — e hoje reprovava, porque a vitrine passou a
servir o botão **encurtado** com `rel="sponsored"`. É a terceira vez que essa linha troca de objeto contando
o mesmo número: etiqueta "em breve" (até 14/09), busca crua (14/09→25/09), busca encurtada (desde hoje).
Ela agora cobra as duas metades — a encurtada apareceu **e** a crua sumiu — porque enquanto as duas puderem
conviver na mesma tela, um item sem piso rastreável passa escondido atrás do vizinho que tem.

### O QUE FOI MEDIDO NO AR (18.4)

- Sync forçado: **revisão 37**, 12 aplicados.
- `conferir-no-ar.py`: **459 afirmações, 0 falha**.
- Varredura das **17 URLs do sitemap** mais dois estados de ferramenta: **14 encurtadores servidos, 0
  desconhecido** — nenhum link deslocado sobrou na tela.
- `validar-banco.py`: 25 materiais, **itens SEM SAÍDA de compra 0**, **piso NÃO rastreável 0** (era 15),
  **busca sem endereço cru 0** (era 10).
- `validar-pastilhas.py` 189 afirmações · `mutacoes-pastilhas.py` 14/14 · `mutacoes-rejunte.py` 16/16.

### DE PASSAGEM

`dados/pecas.json` carregava `gerado_em`, trazido do endpoint pela execução de ontem: era o **único erro
vermelho** do `validar-banco.py`, e portão vermelho que ninguém fecha é portão que se aprende a ignorar.
Removido — o carimbo de hora fica fora da cópia pela 24.2, senão toda passada da ronda vira commit.

### O QUE **NÃO** FOI FEITO, E POR QUÊ

Nenhuma página nova, nenhuma URL nova: continuam **17**, e a semana da 21.4 continua em 2 de 3 levas.
Os **BLOCOS A, B e C** do despacho de 24/09 não foram tocados e estão reescritos no `PROMPT.md` pela 18.3 —
o BLOCO 0 dizia, com todas as letras, que **não divide passada com nada**. O BLOCO A depende do número de
30/09; o BLOCO B (filtro `wp_robots` para `/author/`) é o único que não espera dado nenhum.

**PRÓXIMO PASSO DESBLOQUEADO:** o **BLOCO B** — `/author/mosaico_gestor/` está indexada e tomou impressão na
posição 1,0. O caminho é o **filtro** `wp_robots` no snippet da casca, nunca uma segunda meta em paralelo
(lição trazida da Aquametria, escrita no próprio bloco), mais a saída do sitemap. Não depende de nenhum
número que ainda não chegou.

25/09/2026 14:10Z — BLOCOS B E C DO DESPACHO DE 24/09 ENTREGUES: a etiqueta de robô era quatro em paralelo, e o rastreador nunca recebe redirecionamento

- **A ILHA DESTA EXECUÇÃO NÃO FOI ESCOLHIDA, FOI IMPOSTA PELO FOCO.** `foco.md`
  nomeia a **clubedomosaico** desde 24/09, então pela 1.2 a rotação da seção 1
  está suspensa e não houve o que comparar. `executando_desde` estava `null`, que
  pela 1.1 já significa que nenhum bloco da Fundação estava vivo — não houve
  reserva vencida para o git desempatar. Nenhum PR aberto e a branch `claude/*`
  do repositório está mesclada (zero commits à frente do `main`). Reserva aceita
  às 13h17Z, no primeiro push.
- **REDE PELA 20.2, RETESTADA E NÃO HERDADA:** três passadas,
  `clubedomosaico.com.br` em **200** nas três, com `aquametria.com.br` em 200 nas
  mesmas três.
- **A ORDEM VEIO DO PRÓPRIO DESPACHO**, que já a tinha escrito: o BLOCO B não
  depende de dado que não chegou, o C é varredura e relatório, e **o A espera
  30/09** — trocar título antes do número de 30/09 misturaria duas causas na
  mesma janela, e o veredito dele é de 08/10. Pela 18.3 o despacho foi reescrito
  deixando só o A, com o motivo em uma linha.

**BLOCO B — E ELE ACHOU UM DEFEITO MAIOR DO QUE O QUE VEIO CONSERTAR.**

- O pedido era `/author/mosaico_gestor/`: 200, sem etiqueta, fora do sitemap, sem
  link de nenhuma página daqui — e mesmo assim indexado e servido na **posição
  1,0** na janela 15→21/09, disputando orçamento de rastreamento com 15 páginas
  NÃO indexadas desta mesma propriedade.
- **O que a primeira medição achou, antes de escrever uma linha de código:**
  `/materiais/como-sabemos/` já servia **DUAS** `<meta name="robots">` — a do
  núcleo (`max-image-preview:large`, aspas simples) e a da casca (`noindex,
  follow`, aspas duplas), injetada num `wp_head` paralelo. **Era exatamente a
  armadilha que o BLOCO B nomeia como lição da Aquametria**, e ela já estava no ar.
- **E não eram duas, eram quatro.** A F1, a F2 e o Leads faziam o mesmo, cada um
  para tirar do índice o estado COM PARÂMETRO da própria página. Medido no ar em
  `/materiais/qual-cola-usar-no-mosaico/?base=espelho&onde=interno_seco`, que é um
  estado da **melhor página desta ilha** (17 impressões na posição 7,8).
- **POR QUE NENHUM PORTÃO VIA:** todos mediam **SE** a frase `noindex` aparecia;
  **nenhum media QUANTAS etiquetas apareciam.** O idioma de contar já existia
  nesta ilha desde que o `teste-f2.php` nasceu — mas só para o `<link
  rel="canonical">` ("a ancora serve UM canonical"). Para o robô, nunca.
- **A IRONIA ESTAVA ESCRITA NO PRÓPRIO F2**, três linhas acima do `echo` que ele
  fazia: ele explica, com todas as letras, por que NÃO imprime o canonical —
  *"serviria DOIS canonicals (...) sujo numa página cujo propósito inteiro é ter
  UM endereço no índice"* — e fazia exatamente isso com a etiqueta de robô.
- **O CONSERTO, e é o caminho que o bloco manda:** a casca 1.13.0 declara a
  etiqueta pelo filtro `wp_robots` (prioridade 20, depois do núcleo) em vez de
  imprimi-la, e abriu `cdm_fora_do_indice` para quem quiser sair do índice
  **declarar a condição**. Quem imprime é a casca, uma vez, a partir de um vetor
  só. `max-image-preview` é retirada quando a página sai do índice, para o texto
  servido não depender da ordem dos filtros: sai exatamente `noindex, follow`.
- **TRÊS CONTEXTOS SAEM DO ÍNDICE**, e dois são os que a Sentinela mediu em 23/09:
  as páginas declaradas na definição, o **arquivo de autor** e a **busca interna**
  (`/?s=`), que respondia 200 sem etiqueta nas três ilhas. `follow` fica nos três —
  a página sai do índice e a malha não se corta.
- **CINCO RÉGUAS DESTA ILHA MEDIAM A ASPA DE QUEM ESCREVEU, NÃO A DIRETIVA**, e
  as duas famílias apareceram no mesmo dia. `teste-f1`, `teste-f2`, `teste-atelie`
  e duas afirmações do `conferir-no-ar` procuravam a frase literal com **aspas
  duplas**, que eram as do `echo` dos snippets. O `wp_robots()` do núcleo usa
  **aspas simples**. Resultado: três reprovaram código CERTO no dia do conserto, e
  **duas passavam A VAZIO** — `'name="robots"' not in html` é verdade em toda
  página de aspas simples, inclusive numa que saísse com `noindex` por engano. As
  cinco passaram a medir a DIRETIVA e a CONTAR as etiquetas.
- **A BANCADA PASSOU A EMULAR `wp_robots()`**, com o
  `wp_robots_max_image_preview()` do núcleo na prioridade 10 e as aspas simples do
  original. Sem isso ela reprovaria o conserto por não saber produzir o mecanismo
  novo — e a saída fácil seria afrouxar o teste.
- **CONFERIDO NO AR**, casca 1.13.0 / f1 1.3.1 / f2 1.5.1 / leads 1.1.1, manifest
  39 e `/status` na 39: `/author/`, `/materiais/como-sabemos/`, `/?s=mosaico`,
  `/atelie/` e os estados com parâmetro da F1 e da F2 servem **UMA** etiqueta com
  `noindex, follow`; a home, as 17 URLs do sitemap e as duas âncoras que rankeiam
  servem UMA e continuam **no** índice.

**BLOCO C — O RASTREADOR NUNCA RECEBE REDIRECIONAMENTO, E ISSO SÓ APARECEU PORQUE DUAS LEITURAS DISCORDARAM.**

- `ferramentas/varrer-canonicas.py` (nova) lê a canônica e a cadeia de
  redirecionamento de cada URL e classifica nas duas listas que o bloco pede, em
  `dados/indexacao.md`. **71 URLs: 71 em "esperado, nenhuma ação", 0 defeito.**
  Nenhuma correção aplicada, como o bloco manda.
- **A LISTA NÃO É DIGITADA:** as 17 vêm do `wp-sitemap.xml` no ar, mais `/author/`
  e as variações de cada uma (`http`, `www`, sem barra final) — os dois motivos do
  e-mail nascem de DUAS URLs para a mesma coisa, e varrer só a versão boa mediria
  o lado que nunca dá problema.
- **O ACHADO, e ele quase não foi feito:** a primeira conferência abriu
  `https://www.clubedomosaico.com.br/loja/` no `curl` e leu **200**; a varredura,
  que gruda `?v=<agora>`, leu **301** na mesma URL no mesmo minuto. Não é
  intermitência: são **dois respondedores**. Com a quebra de cache a pergunta
  chega ao WordPress, que redireciona certo; sem ela quem responde é o **cache de
  página**, que não sabe redirecionar. **O Googlebot não manda quebra de cache.**
  Medido em três passadas por URL e por leitura, porque uma leitura só não
  distingue cache frio de regra — a primeira leitura da home deu 301 cru, antes de
  a entrada esquentar, e as três seguintes deram 200.
- **Em 36 das 71 URLs as duas leituras discordam**, e a coluna nova da tabela as
  marca uma a uma.
- **ISSO EXPLICA UM MOTIVO E NÃO EXPLICA O OUTRO.** "Página alternativa com tag
  canônica adequada": explicado, e o despacho está certo em chamá-lo de
  comportamento esperado — o rastreador recebe 200 em cada variação e a canônica
  aponta para a versão boa. "Página com redirecionamento": **não explicado pelo
  que a ilha serve hoje**, o oposto do que esta execução esperava achar. A fonte
  provável é a vida anterior do domínio (há um `sitemap.xml` de 2019 na
  propriedade), e **a lista só existe dentro do Search Console**.
- **O PEDIDO AO RAPHAEL CONTINUA DE PÉ, e é o que destrava de verdade:** dar
  acesso de leitura à conta `sentinela@` em `sc-domain:clubedomosaico.com.br`.
  Sem ele, indexação e posição desta ilha só se leem no navegador dele.
- **O QUE ISSO CUSTA A QUEM MEDIR ESTA ILHA, e é maior que o BLOCO C:**
  `conferir-no-ar.py` gruda `?v=<agora>` em toda URL — e está **certo** em fazer
  isso, porque nasceu para provar que o Sync aplicou a revisão nova (seção 4). O
  preço é que **ele nunca vê o que o visitante vê**, e nenhuma linha dizia isso.
  Cache servindo página velha para gente de verdade passa por baixo das 488
  afirmações dele sem encostar em nenhuma. Mesma família da seção 29.
- **A FERRAMENTA TEM `--autoteste`**, 11 casos fabricados, um por ramo da régua:
  a varredura fechou em 71 esperado e ZERO defeito, e portão que nunca acusou nada
  é indistinguível de portão quebrado. Os sete ramos de defeito acusam; os quatro
  de "esperado" não. **E o autoteste já pagou:** a primeira passada chamou de
  DEFEITO a ausência de canônica em `/author/`, que é o comportamento padrão do
  núcleo em arquivo (só página singular recebe `rel_canonical()`) — trabalho
  inventado, que é o que a abertura do BLOCO C manda evitar.

**DE PASSAGEM, UMA BANCADA VERMELHA QUE NÃO ERA DESTE DESPACHO — E QUE TRAVAVA DUAS BATERIAS.**

- `teste-f1` (2 falhas) e `teste-f2` (1) estavam vermelhos no `main` **desde as
  10h40Z desta mesma data**, e com eles `mutacoes-f1` e `mutacoes-f2` se recusavam
  a rodar: *"a F1 de verdade já está reprovada — conserte antes de mutar"*.
  Confirmado como anterior rodando as duas em `82ced82`: 2 e 1 falhas, idênticas.
- **A CAUSA ERA A PRÓPRIA MELHORA DAQUELA EXECUÇÃO.** Os treze itens de pastilha
  subiram do degrau 4 (busca crua, `rel=nofollow`, que não rende nada) para o
  degrau 3 (`url_busca`, link de afiliado com `rel=sponsored`). As réguas cobravam,
  com número fixo, que os treze estivessem no degrau 4 — **e o comentário três
  linhas acima da própria afirmação já tinha escrito, em 14/09, que "uma régua
  presa a isso ficaria verde para sempre".** Prendeu-se assim mesmo, e ficou
  vermelha quando a ilha melhorou.
- **CONSERTADO SEM AFROUXAR:** o degrau de cada item passa a ser **derivado do
  banco**, e a régua cobra que o cartão sirva o botão do degrau em que o item
  está, um por recomendado, nos **três** degraus em vez de num só. O invariante
  que nunca mudou — nenhum item sem saída de compra, nenhuma promessa de "em
  breve" — continua cobrado igual.
- **E O DEGRAU 4 PASSOU A SER PRODUZIDO, NÃO ESPERADO:** nasceu o mundo
  `so_crua=1` no `render-para-teste.php`, que apaga a ficha e a busca encurtada e
  deixa a crua de pé. É onde o `rel=nofollow` da busca crua é conferido agora — o
  irmão `sem_piso` já tinha escrito essa mesma cicatriz sobre si mesmo em 14/09.
- **Os dois voltaram a verde e as duas baterias voltaram a rodar.**

**TRÊS MUTAÇÕES FICARAM INERTES NO CONSERTO, E AS TRÊS FORAM RETARGETADAS.**
`mutacoes-leads` 29, `mutacoes-f1` e `mutacoes-f2` apagavam o `echo` que deixou de
existir. Mutação inerte é o pior dos dois estados: a bateria continua verde
dizendo que mediu. O alvo novo é a declaração do `cdm_fora_do_indice`, e apagá-la
devolve o estado com parâmetro ao índice do mesmo jeito.

**MEDIDO NESTA EXECUÇÃO.** Bancada: `teste-casca` 555 (eram 549), `teste-f1` 196,
`teste-f2` 114, `teste-atelie`, `teste-leads`, `teste-loja`, `teste-tecnicas` e
`teste-prestacao-rejunte` — **todos 0 falha**. Mutações: `mutacoes-atelie` 48/48,
`mutacoes-leads` 48/48 e **0 inertes** (era 1), `mutacoes-voz-e-cabeca` 24/24,
`mutacoes-arvore` 21/21, `mutacoes-f1` 46/46 e `mutacoes-f2` 50/50 — **as duas
últimas voltaram a rodar nesta execução**, depois de se recusarem desde as 10h40Z. No ar: `conferir-no-ar.py` **488
afirmações, 0 falha** (eram 459). As afirmações novas da casca foram provadas não
inertes uma a uma, com quatro quebras: `max-image-preview` colada no `noindex`,
autor de volta ao índice, casca devolvendo markup em vez de diretiva, e tudo
saindo do índice — as quatro reprovam.

**PRÓXIMO PASSO DESBLOQUEADO:** o **BLOCO A** (CTR das três páginas de primeira
página), que **espera o número de 30/09** por ordem do próprio despacho. Até lá
esta ilha não tem item da Fundação aberto que não dependa de dado que ainda não
chegou. **O que depende do Raphael:** o acesso do `sentinela@` ao Search Console,
e a proposta de 301 de `http` para `https` em todo caminho, escrita em
`dados/indexacao.md` e **não aplicada**.

25/09/2026 16:16Z — BLOCO ENTREGUE: a categoria ALICATE sai de zero, e o teto de corte da ilha e 5 mm

- **O que este bloco e, e por que ele e este.** O despacho do Raphael de 24/09 esta fechado menos pelo
  BLOCO A, que **espera 30/09 por ordem do proprio despacho** — trocar titulo antes do numero de 30/09
  misturaria duas causas na mesma janela. Com isso a fila normal volta, e o que o `ESTADO.md` e o
  `ARVORE.md` vinham apontando ha treze dias como "o que destrava mais coisa" e a **coleta das quatro
  categorias vazias do vocabulario**. Comecei pela `alicate` por um motivo escrito, nao por gosto: o
  proprio `esquema-banco.json` diz, desde 11/09, que "as categorias rejunte, pastilha e alicate podem ser
  enchidas em qualquer execucao, **sem decisao nova** — o esquema ja diz que campo cada uma exige". As
  outras tres nao tem essa linha.
- **`dados/materiais-alicates.json`, seis SKUs.** Tres torqueses Cortag (mosaico com roldanas de metal
  duro, azulejista corte reto, azulejista corte curvo) e tres cortadores manuais Vonder (VDEC 51, 75 e
  90). `dados/cobertura.json` recontado pela propria `ferramentas/cobertura.py`: a lista
  `categorias_do_vocabulario_sem_nenhum_item` **cai de quatro para tres** — restam `base`, `acabamento`
  e `apoio`.
- **O ACHADO NAO ERA DESTE BLOCO, E CRUZA COM O BANCO QUE JA EXISTIA.** O torques de mosaico da Cortag e
  a **unica** ferramenta do arquivo cuja declaracao nomeia **vidro**, e ela para em **5 mm**. Os tres
  cortadores de bancada declaram *"pisos ceramicos e porcelanatos ate 10 mm"* e **nao nomeiam vidro em
  lugar nenhum** — nem na indicacao, nem no rodel de carboneto de tungstenio. Medido contra
  `materiais-pastilhas.json`: das **13** pastilhas do banco, todas de vidro, **10** cabem no teto e
  **tres nao** — `st5102` (6 mm), `af1500` (8 mm) e `ic02` (8 mm). **Para tres dos treze produtos cuja
  quantidade a F1 ja calcula, o banco de ferramentas nao tem uma declaracao de fabricante que sustente o
  corte.** Nao e falta de coleta: os quatro fabricantes alcancados publicam o teto deles. E faixa
  DESCOBERTA no sentido da 14.3, escrita na secao **7b-bis** do `ARVORE.md`.
- **A outra metade vale para as duas paginas de tecnica que ja estao no ar.** A frase do torques nomeia
  **pastilha** de vidro e de ceramica e **nao nomeia** caco de azulejo, caco de louca, caco de espelho
  nem pedra — e caco de louca e o material do **picassiete** e caco de azulejo o do **trencadis**. Pelo
  principio dos tres estados, para esses quatro o estado e `nao_declarado`: nem recomendar, nem proibir,
  e dizer que ninguem declarou.
- **A SECAO 8 PEGOU UMA CONSULTA MINHA CONTAMINADA, e ela ficou registrada no dado em vez de apagada.**
  Uma passada escrita com o prefixo `68.51` devolveu `68.51.075.000` e `68.51.090.000` — exatamente o que
  ela plantou. A passada limpa seguinte, sem numero nenhum, **nao devolveu referencia**. Os dois codigos
  ficaram **NULL** com o motivo escrito no registro. O do VDEC 51 (`68.51.050.000`) ficou porque veio de
  consulta que nao o carregava, e depois foi corroborado por canal independente: o titulo de um anuncio
  lido pela Open API, *"... VDEC 51, VONDER 6851050000"*. Duas passadas por SKU, escritas de forma
  diferente, pedindo sempre os ROTULOS da ficha e nunca um numero.
- **O PORTAO DESMENTIU A MINHA SUPOSICAO, e esse e o melhor pedaco da execucao.** O arquivo nasceu
  `publicar: false` com o motivo "option que nenhuma pagina le e caminho morto". Quem desmentiu foi o
  `teste-casca.php`: *"o cartao 'Alicates e corte' mostra o que o banco tem — tela 0 / banco 6"*. O
  cartao **G-ALICATES existe no Guia desde que a casca nasceu**, e o mapa `G-ALICATES =>
  materiais-alicates` ja estava escrito **dentro do proprio teste**, esperando o arquivo. O leitor
  existia; a suposicao e que estava errada. Casca **1.14.0** liga os dois.
- **E de passagem, a frase de prova do Guia ia publicar uma soma impossivel.** Ela anunciava o total do
  banco e enumerava **so tres** categorias: com a quarta entrando, teria ido ao ar *"o banco tem 31
  itens, sendo 7 colas, 5 rejuntes e 13 pastilhas"*. E a familia do *"hoje 10 dos 5 itens esperam link"*
  que esta ilha ja pagou uma vez. A frase passou a nomear a quarta, e a tabela da metodologia ganhou a
  linha.
- **E O SEGUNDO PORTAO REPROVOU A MINHA REDACAO, no ar.** `conferir-no-ar.py`: *"toda categoria com
  arquivo de banco e NOMEADA na frase — faltou: alicate"*. Eu tinha escrito "6 ferramentas de corte":
  total certo, parcelas somando certo, e **errado assim mesmo**, porque o cartao se chama "Alicates e
  corte" e numero que nao usa a palavra do cartao e numero que o leitor nao liga a lugar nenhum. Casca
  **1.14.1**: "6 alicates e cortadores".
- **TRAVA NOVA NO `gerar-links-afiliado.py`, escrita pela execucao que caiu nela.** Rodar `--escrever`
  para gravar **seis** registros novos regerou os **vinte e cinco** que ja estavam certos: URL encurtada
  nova para a mesma busca, sem um unico ganho. O custo so aparece depois — o banco passa a conhecer um
  encurtador que a pagina no ar ainda nao serve, e o `conferir-no-ar.py` reprova exatamente isso, entao a
  ilha ficaria vermelha ate o Sync publicar o banco novo, por causa de uma passada que nao pediu nada
  disso. Foi desfeito com `git checkout --`, **e mao nao e portao**. Agora registro cuja busca crua ja e
  a da tabela e cujo encurtador ja existe e **pulado**; `--regerar-tudo` continua existindo para o caso
  em que a chave mudou, que e o das treze pastilhas.
- **As seis chaves foram medidas na API ANTES de qualquer link nascer** — a licao das treze pastilhas, de
  25/09 de manha, aplicada ao contrario do que a causou. As **31** chaves do banco devolvem oferta, e os
  titulos batem com o produto. Uma desceu um degrau na hora: `torques azulejista corte curvo cortag`
  devolveu **ZERO** e desceu para a FAMILIA, com o degrau escrito em `motivo_da_chave`.
- **Tres pendencias nomeadas**, e a primeira e a que mais importa: nao da para saber, desta nuvem, se o
  torques de corte curvo e o de mosaico com roldanas sao **dois produtos ou duas entradas de catalogo do
  mesmo** — as URLs sao distintas mas a frase de 5 mm e a mesma palavra por palavra, e a busca por SKU do
  curvo devolve zero oferta enquanto a do outro devolve tres. O registro do curvo nasceu sem **nenhuma**
  propriedade tecnica, entao se a resposta for "e o mesmo", ele vira `descartado` com motivo e a
  categoria cai de 6 para 5 **sem perder um so campo verificado**.
- **O que este bloco NAO destravou:** o **4c continua fechado**, e por um motivo diferente do de 12/09.
  Nao e mais "a categoria alicate nao tem um unico item"; e a **16.5** — `/materiais/alicates/` precisa
  de 3 filhas de nivel 3 e nenhuma filha de alicate existe. E a contagem esconde uma distincao: dos tres
  registros de `tipo: torques`, **um so** carrega declaracao tecnica propria, entao por elegibilidade
  `cortador_de_azulejo` esta em 3 e `torques` esta em **1**.
- **Nenhuma URL nova.** As 17 continuam 17, e a semana da 21.4 continua onde estava.
- MEDIDO: `teste-casca` **555** e 0 falha (eram **4** quando o arquivo entrou sem leitor), `teste-f1` 196,
  `teste-f2` 114, `teste-loja` 178, `teste-leads` 211, `teste-tecnicas` 123, `teste-atelie` e
  `teste-prestacao-rejunte` aprovados, todos 0 falha; `validar-banco` **31 materiais**, 0 sem saida de
  compra, 0 piso nao rastreavel, 0 busca sem endereco cru; `cobertura` recontada; `mutacoes-f1` 46/46.
  Sync na revisao **41** e depois **42**, `conferir-no-ar` **488 afirmacoes**.
- Proximo passo: **as tres categorias que sobraram** (`base`, `acabamento`, `apoio`) — e elas **nao** tem
  a linha do esquema que a `alicate` tinha, entao cada uma comeca por decidir que campo exige. A de menor
  atrito e `acabamento` (verniz, impermeabilizante, selador), porque e quimico de fabricante com ficha
  tecnica publicada, que e o mesmo terreno das colas e dos rejuntes; `base` e `apoio` sao genericas e
  provavelmente sem fabricante que declare. E o **BLOCO A espera 30/09**, por ordem do despacho.


---

## 2026-09-25, 19h16Z → 20h58Z — A CATEGORIA ACABAMENTO SAI DE ZERO, E ELA FOI A PRIMEIRA QUE PRECISOU DECIDIR O CAMPO ANTES DE COLETAR

**Ilha em foco** (`foco.md`, desde 24/09). Reserva às 19h16Z, commit `2de100b` — `executando_desde` estava
`null` e o último commit da ilha era de 17h29Z, 106 minutos atrás, então não havia reserva vencida para o git
desempatar (1.1). Rede conferida antes de trabalhar (20.2): `clubedomosaico.com.br` em **200 nas três
passadas**.

**O DESPACHO ABERTO NÃO TINHA ITEM PARA HOJE, e isso foi verificado antes de escolher bloco.** O despacho do
Raphael de 24/09 está em **BLOCO A e mais nada**, e o próprio despacho manda o A **esperar 30/09** ("trocar
título antes do número de 30/09 misturaria duas causas na mesma janela"). Do despacho da Sentinela de 23/09,
o item 1 e o item 2 esperam a leitura de 30/09 e o item 3 está cumprido. Pela **18.5** a verificação vem antes
da construção; não havia o que verificar, e a fila assumiu.

**UMA PROPOSTA ESTAVA MARCADA COMO ABERTA COM A CONDIÇÃO DE FECHAMENTO JÁ CUMPRIDA.** A PROPOSTA 2 de 23/09
pedia que o Raphael respondesse sobre a ordem do foco, *"ou mantendo a aquametria com o motivo escrito em
`foco.md`, ou trocando"*. Ele trocou — em **24/09**, com o motivo escrito. A proposta ficou um dia inteiro
parecendo pendente. É a seção 4 do contrato outra vez, agora dentro do próprio `PROMPT.md`: resumo velho lido
como fato. Fechada nesta execução.

### O QUE FOI FEITO — SETE PRODUTOS, DE DOIS FABRICANTES, E NENHUM DELES NOMEIA O QUE A PEÇA EXPÕE

`dados/materiais-acabamento.json`: quatro vernizes (três da Acrilex, um boletim de piso da Quartzolit), dois
impermeabilizantes e um selador. A lista `categorias_do_vocabulario_sem_nenhum_item` de `dados/cobertura.json`,
recontada pela própria `cobertura.py`, **cai de três para DUAS** — restam `base` e `apoio`.

**O ACHADO, e ele é o motivo de o arquivo existir:** a peça de mosaico pronta expõe **duas** superfícies — a
**pastilha** (as 13 do banco são todas de vidro) e o **rejunte**. **Nenhuma das sete frases de fabricante
nomeia vidro. Nenhuma nomeia rejunte.** Os três vernizes de artesanato da Acrilex listam tela, madeira, papel,
cortiça, cerâmica, gesso e isopor; o verniz da Quartzolit é de **piso**, com liberação de tráfego de carro e
máquina; a borracha líquida é de fachada, telha e laje sem trânsito; o protetor para fachadas é hidrofugante
de revestimento mineral, churrasqueira de tijolo e pedra natural. Pelo princípio dos três estados, para vidro
e para rejunte o estado é `nao_declarado` nos sete: nem recomendar, nem proibir, e dizer que ninguém declarou.
É a faixa **DESCOBERTA** da 14.3 encontrada pela **superfície**, irmã da que a categoria alicate encontrou
pela **espessura** às 16h43Z do mesmo dia — e as duas apontam para o mesmo lugar: **fabricante de obra não
escreve sobre peça de artesanato, e fabricante de artesanato não escreve sobre mosaico.**

**A SEGUNDA METADE É SOBRE A BASE:** o único selador alcançado (`fundo selador quartzolit`) nomeia concreto,
emboço, reboco, pintura PVA ou acrílica e construção a seco, e **não nomeia MDF** — que é a base mais comum
da peça do ateliê e um dos cinco valores de `tipo_por_categoria.base`. A categoria `selador` nasce com um item
que não serve a base que a ilha mais usa, e isso está escrito no dado.

### A DECISÃO DE ESQUEMA, QUE É O QUE ESTE BLOCO TEVE DE DIFERENTE

A `alicate` de 16h43Z era nomeada pela linha do `esquema-banco.json` que autoriza encher uma categoria *"sem
decisão nova — o esquema já diz que campo cada uma exige"*. As três que sobravam **não são nomeadas nessa
linha**, e o `ESTADO.md` das 17h29Z registrou isso com todas as letras: *"cada uma começa por decidir que campo
exige"*. Esta execução tomou a decisão da `acabamento` e a escreveu em `regras_da_categoria_acabamento`
(esquema **versão 4**), em três partes:

1. **A matriz `base × ambiente` fica VAZIA.** Ela é o eixo pelo qual a F2 escolhe **cola** e **rejunte**;
   acabamento não adere nada e não se escolhe por ambiente declarado. Verniz dentro dela viraria candidato a
   colar peça.
2. **O que o fabricante declara mora no objeto `protecao`**, irmão do `corte` do alicate: a frase literal, a
   fonte, e as listas do que a frase **nomeia** e do que ela **NÃO nomeia** — cobrindo o vocabulário inteiro,
   porque o que não entra em nenhuma das duas é silêncio **não lido**, e é assim que faixa descoberta fica
   invisível. Mais `nomeia_rejunte`, que existe porque rejunte não é valor de `base` nem de `material_tessela`
   e mesmo assim é metade da superfície exposta.
3. **As propriedades têm NOME FIXO.** Nome livre é o que faz a segunda execução gravar `secagem_horas` onde a
   primeira gravou `tempo_de_secagem_h`, e aí nenhuma régua compara dois registros. `contato_com_alimento` é
   **obrigatório mesmo quando null**: centro de mesa e tampo são duas coleções desta loja, e campo ausente é
   pergunta que ninguém faz. Nos sete ele é null — ninguém declarou.

### AS DUAS MUTAÇÕES QUE ACHARAM BURACO ANTES DO COMMIT, E É O MELHOR PEDAÇO

`ferramentas/mutacoes-acabamento.py` nasceu junto com o portão, e duas das catorze **passaram** na primeira
rodada:

- **A 05 — momento de uso deduzido do mecanismo do produto.** O portão cobrava motivo no **silêncio**
  (`nao_declarado` sem `motivo_do_momento`) e não cobrava **nada na afirmação**: gravar
  `momento_de_uso: depois_de_rejuntar` num hidrofugante, porque "obviamente" é assim que se usa, passava com
  cara de declaração. Agora momento declarado exige `trecho_que_declara_o_momento`, **e o trecho tem de ser
  pedaço literal da frase do fabricante** — não uma segunda frase escrita por quem preencheu.
- **A 13 — a matriz `base × ambiente` preenchida num verniz.** A regra estava escrita desde que nasceu, em
  prosa, e **nenhuma régua a media**. Agora o `validar-banco` reprova acabamento com qualquer lista de
  `declaracoes` preenchida, e reprova lista vazia sem `motivo_declaracoes_vazias`.

A **07** é a que PRODUZ O MUNDO: faz um verniz **nomear vidro**, que é o estado que nenhum dos sete tem hoje e
do qual o achado central deste arquivo depende. Portão que só funciona enquanto a lista de "nomeia" estiver
vazia não mede a regra, mede o acaso.

**Segunda rodada: 14 de 14 reprovadas, 13 delas só o portão novo viu.**

### DOIS NÚMEROS QUE ESTA EXECUÇÃO SE RECUSOU A PUBLICAR

- **O rendimento da borracha líquida.** A frase colhida por busca diz *"18 kg rende no mínimo 70 m²/L"* —
  mistura a embalagem com a unidade e não fecha em nenhuma das duas leituras. Ficou `valor: null` com o motivo
  escrito, e virou a **mutação 12**.
- **As demãos e o consumo do fundo selador.** A mesma página de resultados devolve "duas demãos" (que é do
  **protetor para fachadas**, outro produto) e "350 mL/m² em duas demãos" (que é do **weber.floor selador de
  base**, produto de piso industrial). Emprestar número de um produto a outro é exatamente o que a regra das
  duas passadas existe para pegar.

### AS DUAS PALAVRAS-CHAVE QUE DESCERAM UM DEGRAU, MEDIDAS ANTES DE VIRAR LINK

As sete chaves foram conferidas na Open API (`--conferir-chaves`) **antes** de qualquer link nascer, que é a
lição das treze pastilhas aplicada ao contrário do que a causou. Duas devolveram **ZERO**: `fundo selador
quartzolit` (a palavra "fundo" não aparece em título de anúncio) e `protetor para fachadas quartzolit` (o
produto é de canal de obra e não é anunciado por esse nome). As duas desceram para a **família** —
`selador quartzolit` e `impermeabilizante fachada quartzolit`, três ofertas cada — com o degrau escrito no
`motivo_da_chave` de cada registro. **Sete links novos, 31 intocados**: a trava escrita às 16h43Z pela execução
que caiu nela segurou.

### A CASCA, E O PORTÃO QUE DESMENTIU A EXECUÇÃO PELA SEGUNDA VEZ NO MESMO DIA

O cartão "Acabamento" do Guia mostrava **0 com o banco em 7**, e a frase de prova anunciava o total do banco
enumerando só quatro categorias — com a quinta entrando, ela teria posto no ar *"o banco tem 38 itens, sendo 7
colas, 5 rejuntes, 13 pastilhas e 6 alicates"*, soma que não fecha. É a mesma família do *"hoje 10 dos 5 itens
esperam link"* que esta ilha já pôs no ar uma vez, e foi o `teste-casca.php` que a pegou, exatamente como
pegou a `alicate` três horas antes. **Casca 1.15.0**, manifest **43**.

### O QUE ESTE BLOCO NÃO É

- **Não é o BLOCO A** do despacho de 24/09, que espera 30/09 por ordem do próprio despacho.
- **Não publica página nenhuma.** A 16.5 exige 3 filhas de nível 3 por categoria e `/materiais/acabamento/`
  continua sem página. **As 17 URLs continuam 17** e a semana da 21.4 continua onde estava.
- **Não abriu o domínio de ninguém.** `acrilex.com.br`, `www.acrilex.com.br`, `corfix.com.br`,
  `www.quartzolit.weber`, `suvinil.com.br` e `vedacit.com.br` em **000 nas três passadas**, com o domínio da
  ilha em 200 nas três. Todo campo carrega `conferir_no_pdf: true`.
- **Não usou a loja da marca como fonte técnica.** A Suvinil publica um selador acrílico e uma seladora para
  madeira — que seriam os dois únicos registros a nomear MDF —, e as duas páginas que a busca devolveu são de
  `loja.suvinil.com.br`, **nível 5** na escada desta ilha, que não sustenta recomendação primária. Nenhuma das
  duas virou registro, e o motivo está escrito em `pendencias_desta_categoria`.

### MEDIDO

**Bancada, tudo sem rede:** `teste-casca` 555 (eram 4 falhas quando o arquivo entrou sem leitor), `teste-f1`
196, `teste-f2` 114, `teste-loja` 178, `teste-leads` 211, `teste-tecnicas` 123, `teste-atelie` e
`teste-prestacao-rejunte` aprovados — todos 0 falha. `validar-banco` com **38 materiais**, 0 sem saída de
compra, 0 piso não rastreável, 0 busca sem endereço cru; `validar-pastilhas` 189 afirmações, 0 item com falha.

**AS SETE BATERIAS DE MUTAÇÃO RODARAM INTEIRAS E NENHUMA MUTAÇÃO PASSOU:** `f1` 46/46, `f2` 50/50,
`pastilhas` 14/14, `cobertura` 14/14, `voz-e-cabeca` 24/24, `arvore` 21/21 e a nova **`acabamento` 14/14**,
com 13 das 14 vistas só pelo portão novo.

**No ar:** Sync forçado, `/status` na revisão **43**, `conferir-no-ar.py` com **488 afirmações e 0 falha**.
A frase servida em `/materiais/` foi lida à mão além do portão: *"Hoje o banco tem 38 itens de fabricante,
sendo 7 colas, 5 rejuntes, 13 pastilhas, 6 alicates e cortadores e 7 produtos de acabamento, e 28 deles ainda
esperam link de loja"* — as parcelas somam o total e as cinco categorias com arquivo de banco estão nomeadas.

*(A revisão ficou em 42 no primeiro Sync: o `--revisao 43` foi passado na passada do `atualizar-manifest.py`
que parou no descasamento de versão da casca, e a passada seguinte não o repetiu. O Sync aplicou os 14 itens
assim mesmo — ele compara sha, não número —, mas `/status` mostrando 42 depois de um bloco é a seção 4 outra
vez. Corrigido em commit próprio, e o número de verdade levou ~4 minutos para chegar por causa do cache do
raw do GitHub.)*

### O QUE DEPENDE DO RAPHAEL — três coisas, e nenhuma é da Fundação

1. **Acesso de leitura da conta `sentinela@`** em `sc-domain:clubedomosaico.com.br` no Search Console. É o que
   destrava a medição desta ilha, e está aberto desde 23/09.
2. **Autorizar, ou não, o 301 de `http` para `https` em todo caminho** — hoje só a home redireciona. A
   proposta está escrita em `dados/indexacao.md` e **não foi aplicada**, porque o BLOCO C proíbe aplicar sem
   autorização item por item.
3. **Acrescentar domínio de fabricante à rede Personalizada do ambiente** (20.1). Hoje `acrilex.com.br`,
   `quartzolit.weber`, `suvinil.com.br`, `corfix.com.br` e `vedacit.com.br` respondem `000`, e **todo o banco
   desta ilha é nível 2 ou 3 por causa disso**. Com os domínios abertos, o banco inteiro sobe para nível 1 e
   as tabelas de substrato dos boletins — que é exatamente onde a resposta sobre vidro e rejunte moraria —
   passam a ser legíveis.

### PRÓXIMO PASSO

As **duas** categorias que sobraram: `base` e `apoio`. As duas herdam o molde de
`regras_da_categoria_acabamento` sem herdar a decisão — cada uma ainda começa por decidir que campo exige. A
`base` é a de maior valor para esta ilha (ela é a primeira pergunta da F2 e de todo tutorial) e a de maior
risco: base de artesanato é genérica e provavelmente sem fabricante que declare, ao contrário do químico. E o
**BLOCO A** do despacho de 24/09 **espera 30/09**, por ordem do próprio despacho.

28/09/2026 10:16Z — BLOCO ENTREGUE: a categoria BASE decide o campo, e a decisão descobre que o vocabulário desta ilha não tem onde pousar TRÊS dos cinco tipos dela

- **A ilha em foco continua sendo esta** (`foco.md`, desde 24/09). Rede reconferida antes de trabalhar como manda
  a 20.2: home em **200**, `/status` em **200** na revisão **43**, e `ferramentas/conferir-no-ar.py .` com
  **488 afirmações e 0 falha** no HTML servido — a porta de entrada da seção 29 conferida antes de qualquer
  outra coisa, e ela estava de pé.
- **O bloco é o item 3 da fila** ("a coleta das categorias vazias"), na categoria `base`, e ele **não coletou
  SKU nenhum**. A metade que saiu é a que o próprio `ESTADO.md` de 25/09 dizia que vinha primeiro: *"cada uma
  ainda começa por decidir que campo exige"*. O motivo de a outra metade não ter saído está medido abaixo e
  está escrito no esquema, não só aqui.

## O ACHADO, E ELE NÃO ESTÁ NA FRASE DO FABRICANTE: ESTÁ DO NOSSO LADO DO BALCÃO

`vocabularios.tipo_por_categoria.base` declara **cinco** tipos — `mdf_cru`, `ceramica_crua`, `cimento`,
`isopor_estrutural`, `moldura`. `vocabularios.base`, que é o eixo pelo qual a **F2 decide cola e rejunte** e a
primeira pergunta que ela faz a quem chega, tem **nove** valores. Cruzando os dois, pela primeira vez:

- `mdf_cru` → **pousa** em `mdf_madeira`.
- `cimento` → **pousa** em `cimento_concreto`.
- `ceramica_crua` → **não tem valor**. O único valor de cerâmica no eixo é `ceramica_esmaltada_porcelana`, que é
  a cerâmica **vidrada**. Vaso de barro cru é o contrário: absorve água e absorve cola. A distinção já estava
  escrita à mão nesta ilha, em 25/09, na `observacao` do registro `acrilex-verniz-acrilico-brilhante` —
  *"Cerâmica crua e cerâmica esmaltada absorvem de maneira oposta, e o fabricante não separa as duas"*.
- `isopor_estrutural` → **não tem valor**, e este é o pior dos três, porque **a regra do que fazer já estava
  escrita no mesmo arquivo**. A linha `poliestireno expandido` de `termos_que_nao_traduzem` diz, com todas as
  letras: *"se virar base (isopor estrutural), entra no vocabulário primeiro"* — e `isopor_estrutural` **já era**
  um dos cinco tipos de `tipo_por_categoria.base`. A condição estava cumprida no próprio arquivo que a escreveu,
  e nada conferia as duas linhas juntas.
- `moldura` → **não é material**. A mesma moldura existe em madeira, MDF, metal e plástico, que são quatro
  valores do eixo. Tipo de base que pousa em quatro lugares ao mesmo tempo não descreve substrato: descreve
  **geometria**, e geometria nesta ilha é a **F1** (`area_moldura = L × A − l × a`), não a F2.

**O preço disso já estava pago no banco, antes desta seção existir.** Dois vernizes da Acrilex carregam `isopor`
e `gesso` **dentro da frase literal do fabricante** — e as duas palavras não existem em `vocabularios.base`.
Então a declaração foi lida, classificada e **descartada em silêncio**. A ilha já sabia ler SILÊNCIO de
fabricante (é o terceiro estado do esquema, e a alicate achou uma faixa pela ESPESSURA e a acabamento pela
SUPERFÍCIE). O que ela não sabia ler era **declaração de fabricante jogada fora por falta de vocabulário
nosso** — a mesma família, do nosso lado. É a terceira faixa descoberta desta ilha e a primeira encontrada pelo
VOCABULÁRIO.

## O QUE FOI ESCRITO, E COMO CADA PEDAÇO É MEDIDO

- **`ponte_do_tipo_para_o_vocabulario_base`** no `dados/esquema-banco.json` (esquema na **versão 5**): os cinco
  tipos, cada um em um de três estados — `pousa`, `sem_valor_no_vocabulario` (com `valor_proposto` e
  `o_que_falta`) ou `nao_e_material` (com `onde_ele_e`). Nenhum fica calado, e isso é portão.
- **`condicionais_do_mapa_de_termos`**, dentro da ponte: toda linha de `termos_que_nao_traduzem` que recusa o
  termo **sob condição** ("entra no vocabulário primeiro") aparece aqui com a condição **medida** e o `por_onde`.
  Duas linhas: `poliestireno expandido` (condição **cumprida**) e `gesso` (condição **não cumprida** — gesso não
  está em `tipo_por_categoria.base` nem no corpus como base de peça; a palavra aparece no banco do outro lado do
  balcão, como substrato de PINTURA na frase do fabricante). Condição escrita e nunca conferida é promessa, e
  uma delas já estava cumprida sem ninguém ver.
- **`regras_da_categoria_base`**: o campo novo é o objeto **`substrato`**, irmão do `corte` da alicate e da
  `protecao` do acabamento — frase literal, fonte, `valor_do_vocabulario_base` (UM valor, nunca lista, porque
  base é feita de um material só), `trecho_que_declara_o_material` obrigatório (herdado inteiro da mutação 05 do
  acabamento: *"disco MDF 20 cm" é nome comercial, e nome comercial não é declaração técnica*), as duas listas
  de **ambiente** cobrindo o vocabulário inteiro (a base é a única categoria cujo produto decide onde a peça
  pronta pode **viver**) e `preparo_declarado`, que é o selador do banco de acabamento visto do outro lado.
- **Propriedades de nome fixo**, e aqui elas são MEDIDA: `forma` (num vocabulário novo, `forma_da_base`, que é a
  lista das seis formas que a F1 calcula), diâmetros, lados, vãos da moldura, espessura, peso, densidade,
  `acabamento_de_fabrica` e **`absorcao_declarada` obrigatória mesmo null** — é a pergunta que decide a regra 6
  da F2 e a que separa barro cru de cerâmica esmaltada.
- **A regra que protege a F1 de si mesma:** a base é a única categoria cujo produto declara exatamente o que a
  F1 pergunta (forma e medidas), e medida colhida em anúncio de marketplace é **nível 6**, que sustenta preço,
  unidade e imagem. Medida de anúncio **nunca** entra em fórmula publicada nem na tabela pré-renderizada.

## O PORTÃO NASCEU ANTES DO DADO, E FOI A BATERIA QUE PROVOU QUE ELE MORDE

`ferramentas/mutacoes-base.py` é a primeira bateria desta ilha que **fabrica o próprio mundo**: ela escreve um
`dados/materiais-base.json` com cinco registros (um por tipo, cobrindo os três estados da ponte), confere que o
mundo certo **passa**, muta vinte vezes — treze no registro e **sete no esquema**, porque a ponte é um documento
que mede outro documento —, restaura tudo e **apaga o arquivo fabricado no fim**. Os textos de fabricante lá
dentro são inventados e marcados como tal; nenhum vai para o repositório.

**A mutação 05 PASSOU na primeira rodada, e ela é o defeito mais caro desta categoria:** o vaso de barro cru
gravado como `ceramica_esmaltada_porcelana`. O portão só consultava a ponte quando o **registro** declarava
`sem_valor_no_vocabulario` — e o caminho caro é o contrário, o registro gravando um valor de verdade num tipo
que a ponte diz que **não pousa**. Esse defeito **não deixa rastro**: some a faixa descoberta e nasce, no lugar
dela, uma recomendação de cola sobre uma superfície que absorve ao contrário da que foi respondida; o registro
fica verde, a ponte continua dizendo a verdade, e as duas nunca se encontram. Agora a ponte manda nas **duas
direções**. **Segunda rodada: 20 de 20 reprovadas, 19 só os portões novos viram.**

A mutação **14** é a que PRODUZ O MUNDO: ela **executa** a ponte (acrescenta `isopor_eps` a
`vocabularios.base`) e mede se o esquema acusa que a ponte envelheceu no mesmo commit em que o vocabulário
cresceu. Sem ela, a ponte viraria, ela própria, o *resumo velho lido como fato* da seção 4 do contrato.

## POR QUE NENHUM SKU FOI COLETADO, E ISSO ESTÁ NO ESQUEMA E NÃO SÓ AQUI

Egresso medido nesta execução, em três passadas, com `clubedomosaico.com.br` em **200** nas mesmas passadas
(seção 20.2 — é isso que separa bloqueio de rede de intermitência de túnel): **000** em `dexco.com.br`,
`duratex.com.br`, `guararapes.com.br`, `arauco.com.br`, `berneck.com.br`, `eternit.com.br`, `brasilit.com.br`,
`termotecnica.ind.br`, `isoeste.com.br` e `leroymerlin.com.br`.

**E a diferença em relação à acabamento, que correu com o mesmo bloqueio, é o CANAL e não a rede:** a acabamento
se sustentou na busca restrita ao domínio, que devolve a frase do fabricante sem abrir a página (nível 3). Nesta
execução o canal de busca disponível devolveu **resumo e tradução** das páginas de painel de MDF, não a frase do
fabricante. `literal_do_fabricante` é a viga de todo este esquema, e gravar paráfrase de resumo naquele campo é
a família do número de tela digitado: **parece conferido**. Então a decisão de campo saiu inteira, com portão e
bateria, e o primeiro SKU nasce na execução em que a frase do fabricante puder ser citada. Está escrito em
`regras_da_categoria_base.o_que_falta_para_coletar_o_primeiro_SKU`, não só neste registro.

## O QUE ESTE BLOCO DELIBERADAMENTE **NÃO** FEZ, E O MOTIVO É A JANELA DE MEDIÇÃO

Ele **não** acrescentou `ceramica_crua_barro` nem `isopor_eps` a `vocabularios.base`. Não é dúvida — é a 12.1 e
o BLOCO A do despacho de 24/09. Acrescentar valor ao eixo muda o que
`/materiais/qual-cola-usar-no-mosaico/` **serve**: a lista suspensa ganha duas opções, a contagem de
`cdm_f2_faixas_descobertas_html()` sai de 9 × 5 × 6 = **270** para 11 × 5 × 6 = **330** combinações, e as duas
bases novas entram na frase que a página já sabe dizer sozinha — *"Não indicamos cola nenhuma, em lugar nenhum,
para: …"* —, porque nenhum fabricante do banco as nomeia. Essa é a página de **posição 7,8**, a melhor do
Arquipélago inteiro, e o BLOCO A espera 30/09 exatamente para não misturar duas causas na mesma janela. Mexer no
corpo dela hoje misturaria três. **A máquina para dizer a verdade já existe na página; falta a decisão, e ela
está escrita, medida e pronta para sair inteira.**

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` verde (38 materiais, 0 sem saída de compra, 0 piso não rastreável), `cobertura.py` recontada
e **sem mudança** — continuam **duas** categorias sem nenhum item (`base`, `apoio`) —, `teste-casca.php` 555
verificações, `teste-f2.php` 114 afirmações, `teste-f1.php` 24 estados com processo próprio,
`teste-prestacao-rejunte.php` 5 afirmações sobre 540 estados da F2 e 180 da F1, `teste-tecnicas.php` 123
verificações. **E as baterias de mutação inteiras, porque a mudança foi no ESQUEMA e o esquema é lido por
quase todas:** `mutacoes-base.py` 20 de 20, `mutacoes-f2.py` 50 de 50, `mutacoes-arvore.py` 21 de 21,
`mutacoes-rejunte.py` 16 de 16, `mutacoes-cobertura.py` 14 de 14, `mutacoes-acabamento.py` 14 de 14,
`mutacoes-pastilhas.py` 14 de 14 e `mutacoes-tecnica-x-material.py` 9 de 9 — **158 mutações, nenhuma passando**.
E `conferir-no-ar.py` refeito no fecho: **488 afirmações, 0 falha**, o mesmo número da abertura, que é a prova de
que o site não foi tocado. **Nenhuma URL nova: as 17 continuam 17**, a semana da 21.4 continua
onde estava, e **não houve Sync** — nada do que este bloco mexeu é conteúdo publicável (seção 4).

## DE PASSAGEM, UMA MEDIÇÃO QUE DESMENTE UMA INSTRUÇÃO DO PRÓPRIO REPOSITÓRIO (item 4 da fila)

O item 4 da fila diz que a linha da peça no `ARVORE.md` é *"conserto de TESTE, não de documento"*, e a seção 5
daquele arquivo explica por quê: o mapa é por requisição e a peça só entra nele quando está sendo servida.
**Medido com a bancada nesta execução, servindo a peça de verdade: a explicação está certa e a conclusão está
incompleta.** O mapa ganha a chave **`quadro-flores-do-campo`** — slug nu, nível 2, mãe `loja` —, e **não**
`loja/quadro-flores-do-campo`. Toda outra entrada de nível 2 ou 3 é chaveada pelo **caminho inteiro**; a peça é a
única chaveada pelo slug nu, porque o filtro `cdm_arvore` da Loja escreve `$mapa[ $peca->post_name ]`. Na tela
funciona, e é por isso que ninguém viu: quem pede a trilha da peça passa o `post_name`. O que não funciona é
escrever a peça numa tabela que é **lida por caminho**.

**Isso deixa de ser conserto e vira decisão** — ou o filtro passa a chavear pelo caminho (e é código de snippet
que serve `/loja/quadro-flores-do-campo/`, página **no ar**, com peça publicada por uma pessoa de verdade), ou a
tabela declara a exceção e o portão passa a admiti-la. Escolher entre duas opções defensáveis não é da bancada
(19.2), e as duas mexem em coisa que está servindo. **Não foi executado nesta passada**, e está escrito na seção
5 do `ARVORE.md` para a próxima execução não redescobrir. `teste-casca.php` continua em 555 verificações e
`mutacoes-arvore.py` em 21 de 21 depois da nota.

- **Próximo passo desbloqueado:** a categoria **`apoio`**, que é a última das cinco e a única que ainda não tem
  decisão de campo nenhuma — e ela é a de menor risco de egresso, porque espátula, óculos e luva são EPI e
  ferramenta com ficha de fabricante do mesmo terreno da alicate, que já saiu de zero por busca. A `base`
  espera duas coisas, nesta ordem: (1) a decisão do Raphael sobre os dois valores novos do vocabulário, que só
  pode sair **depois** da leitura de 30/09; (2) o egresso de fabricante, que é o item 3 do "o que depende do
  Raphael" e resolve o banco inteiro junto. E o **BLOCO A** do despacho de 24/09 continua esperando 30/09, por
  ordem do próprio despacho.

---

# 28/09/2026 14h55Z — A CATEGORIA `APOIO` RECEBE A DECISÃO DE CAMPO, E COM ELA NENHUMA DAS SETE FICA SEM A SUA

Esquema na **versão 6**, casca **1.15.0 intocada**, manifest **44**, `conferir-no-ar.py` com **488
afirmações e 0 falha** no ar — o mesmo número da abertura, que é a prova de que o site não foi tocado.
**Nenhuma URL nova: as 17 continuam 17**, a semana da 21.4 continua onde estava.

## A ESCOLHA DA ILHA, E O QUE A FILA DEIXOU DE LADO

`foco.md` nomeia a **clubedomosaico** desde 24/09, então pela **1.2** não há escolha de ilha a fazer.
Reserva por commit às **13h20Z**, aceita na primeira tentativa. Nenhum PR aberto; a branch
`claude/dreamy-mccarthy-kf0p74` não tem commit além do `main`. Rede pela **20.2**, medida e não herdada:
três passadas, `clubedomosaico.com.br` em **200** nas três e `/wp-json/clubedomosaico/v1/status` em **200**
nas três.

Pela **18.1** li o topo do `PROMPT.md` antes de pegar bloco, e **os dois despachos abertos desta ilha não
têm item acionável hoje** — não por falta de fôlego, e sim por ordem escrita: o **BLOCO A** do despacho do
Raphael de 24/09 espera 30/09 pelo próprio texto dele; os itens **1** e **2** do despacho da Sentinela de
23/09 já fecharam a metade de máquina e têm a terceira condição de pronto na **leitura de 30/09**; o item
**3** foi fechado pelo Pente Fino nesta manhã. Então a fila normal, e nela o próximo passo estava escrito
com todas as letras pela execução das 10h16Z: **a categoria `apoio`**, a última das sete sem decisão de
campo.

## A FORQUILHA QUE DECIDE A CATEGORIA INTEIRA, E ELA NÃO É ARRUMAÇÃO

`apoio` é a única categoria desta ilha cujos tipos se dividem em dois ramos que **não se comparam entre
si**, e a divisão muda **o que o erro custa**. Espátula, desempenadeira, pinça e marcador agem sobre o
**material** — errar neles estraga a **peça**. Óculos e luva agem sobre a **pessoa** — errar neles machuca
**quem monta**. Uma lista só poria luva ao lado de desempenadeira como se a escolha fosse do mesmo tipo, e
não é: desempenadeira se escolhe pelo que ela toca, luva se escolhe pelo que ela impede de tocar em você.
É a assimetria de custo da seção 10 aplicada a um vocabulário que já existia e que ninguém tinha cruzado.

Vocabulário novo `ramo_do_apoio` e ponte `ponte_do_tipo_de_apoio_para_o_ramo`, irmã da ponte da `base`
escrita seis horas antes e pelo mesmo motivo. **Seis tipos, quatro na ferramenta e dois no EPI**, nenhum
calado, e o portão reprova registro cujo `servico.ramo` discorde da ponte — nas **duas** direções, que é a
trava que a mutação 05 da base ensinou.

## O PREÇO JÁ ESTAVA PAGO NO BANCO, PELA SEGUNDA VEZ NO MESMO DIA

**CINCO frases de fabricante, em QUATRO registros de TRÊS categorias diferentes, nomeiam um apoio — e
nenhuma tinha campo para onde ir.** Foram lidas, classificadas e descartadas em silêncio, exatamente como
`isopor` e `gesso` na manhã de hoje.

- **`pastilhart-af1500`** (pastilha), em `propriedades.assentamento_recomendado.declarado_como` e em
  `preparo`: *"desempenadeira de **borracha** para não riscar"*.
- **`cascola-cascorez-extra`** (cola), em `preparo`: *"Aplicação com **pincel** ou **rolo**"*.
- **`quartzolit-verniz-protetor-para-pisos`** (acabamento), em `protecao.literal_do_fabricante`:
  *"aplicar com **rolo de espuma de poliéster** limpo e seco"*.

**A primeira delas é a que desenhou o campo novo.** O fabricante da PASTILHA não nomeia só a ferramenta:
ele nomeia o **material dela**, e diz por quê. As 13 pastilhas do banco são todas de vidro. O que decide se
a peça sai riscada não é "desempenadeira", é "de borracha" — então o objeto `servico` tem
`material_de_contato` com vocabulário próprio, e o valor exige o **trecho literal** da frase que o declara.
Gravar só a ferramenta perderia exatamente a metade da declaração que importa.

## É A PRIMEIRA CATEGORIA CUJA DECLARAÇÃO VEM DO OUTRO LADO DO BALCÃO

Quem diz qual desempenadeira usar **não é o fabricante da desempenadeira**. Isso é novo nesta ilha e não
tinha onde ser guardado. Por isso o portão mais forte deste bloco **não olha registro de apoio nenhum**:
`exigencias_de_apoio_ja_declaradas_no_banco` varre as **outras** categorias, só nos campos que carregam
frase de fabricante (a nossa `observacao` fica de fora de propósito — varrer o registro inteiro leria o
nosso julgamento como declaração), e anda nas **duas direções**: ocorrência encontrada tem de estar
listada, e ocorrência listada tem de ser encontrada. Sem a segunda metade, uma linha sobreviveria à saída
do registro que a sustentava, e a seção viraria o *resumo velho lido como fato* da seção 4.

## O VOCABULÁRIO E A FRASE DOS FABRICANTES APONTAM PARA LADOS OPOSTOS

Dos **seis** tipos que `tipo_por_categoria.apoio` declara, **UM** aparece no banco (desempenadeira). Dos
**dois** termos que mais aparecem no banco (`pincel`, `rolo`), **ZERO** estão no vocabulário. E há uma
terceira metade que ninguém tinha cruzado: a propriedade `forma_de_aplicacao` da categoria acabamento
declara *"aerossol, rolo, pincel, trincha"* — e a **interseção dela com `tipo_por_categoria.apoio` é
VAZIA**. Duas metades contando a mesma coisa sem nunca se falarem, que é a família de defeito que esta ilha
mais nomeia.

`pincel` e `rolo` ficam como `sem_valor_no_vocabulario`, com `valor_proposto` e `o_que_falta` escritos, e
**não** entram hoje. E o motivo é diferente do que trava o vocabulário da `base`: nenhuma página lê
`tipo_por_categoria`, e a categoria tem zero itens, então isto **não** é a espera da leitura de 30/09 — é a
regra de crescimento, e só. Valor de vocabulário controlado nasce junto com o primeiro registro que o usa.

## O SILÊNCIO QUE ESTE BLOCO TRANSFORMOU EM NÚMERO

**38 registros, cinco ocorrências, TODAS no ramo `ferramenta_de_aplicacao`. O ramo
`equipamento_de_protecao_individual` tem ZERO:** nenhuma frase de fabricante no banco inteiro nomeia luva,
óculos ou qualquer proteção de quem monta.

Isso importa nesta ilha e não em qualquer uma, porque **a F2 recomenda os dois produtos em que a proteção
deixa de ser opcional**: `loctite-durepoxi` e `quartzolit-rejunte-epoxi` estão no banco e são servidos pela
ferramenta. A ilha recomenda epóxi a uma pessoa em casa e não tem **uma** declaração de fabricante sobre
proteção para pôr ao lado disso.

**O que o bloco NÃO fez, de propósito:** não escreveu recomendação de EPI nenhuma. Deduzir "epóxi pede
luva" do mecanismo do produto é afirmar pelo fabricante, que a seção 8 proíbe, e é o mesmo defeito que a
mutação 05 do acabamento pegou no `momento_de_uso`. O que ele fez foi tornar `risco_declarado`
**obrigatório mesmo null**, para que a primeira coleta responda *"ninguém declarou"* em vez de a pergunta
não ser feita. O que destrava é a FISPQ do epóxi — nível 1, em PDF no domínio do fabricante, o mesmo
egresso fechado que segura o primeiro SKU da `base`. **É o terceiro bloco seguido desta ilha a parar na
mesma porta.**

## UM VOCABULÁRIO QUE NÃO FOI REUSADO, E O MOTIVO É MEDIÇÃO E NÃO GOSTO

`momento_de_uso` já existia (`antes_de_colar`, `depois_de_rejuntar`, `ambos`, `nao_declarado`) e seria o
candidato óbvio para a etapa do apoio. **Ele não tem valor para o ato de COLAR** — porque nasceu para o
acabamento, que por definição nunca cola. E a Cascola declara o pincel e o rolo exatamente para colar.
Reusá-lo obrigaria todo aplicador de cola a responder a uma pergunta que não é a dele, e a resposta menos
errada seria falsa. Nasceu `etapa_da_montagem`, com o motivo escrito no campo, em vez de um valor torcido
para caber.

## AS DUAS COISAS QUE A BATERIA ACHOU ANTES DO COMMIT, E AS DUAS NO PORTÃO NOVO

`ferramentas/mutacoes-apoio.py` é a **segunda** bateria desta ilha que **fabrica o próprio mundo** — e a
primeira que também muta o **banco de verdade**, porque a declaração que importa mora nas outras
categorias. 24 mutações: 14 no mundo fabricado, **6 na AF1500, na Cascorez e no verniz de pisos**
(restaurados byte a byte no fim) e 4 no esquema.

- **A mutação 15** passou na primeira rodada. A varredura comparava os dois lados por `(registro, termo)`,
  e a AF1500 nomeia a desempenadeira em **dois campos** — então apagar **uma** das duas linhas passava
  verde: a outra cobria a que sumiu. **O texto da própria seção já dizia, com essas palavras, "a varredura
  mede CAMPO, não registro".** A prosa estava certa e o código não a cumpria, que é pior que prosa errada,
  porque quem lê acredita. A chave passou a ser `(registro, campo, termo)`.
- **A mutação 20** passou também. Trocar o estado de `aerossol` de `nao_e_ferramenta` para
  `sem_valor_no_vocabulario` satisfazia todos os campos que aquele estado exige — e a próxima execução
  criaria um tipo de apoio chamado `aerossol`, que é **embalagem**. O que separa `aerossol` de `pincel` e
  `rolo` é medível: **onde o termo aparece.** Os dois últimos aparecem em `preparo` e em
  `literal_do_fabricante`, que é prosa de fabricante; `aerossol` aparece uma vez só, em
  `propriedades.forma_de_aplicacao.valor`, que é um **slot do nosso próprio esquema**. Propor crescimento de
  vocabulário a partir de um campo que nós mesmos criamos não é ler declaração nenhuma. Agora o crescimento
  do vocabulário também se apoia em `literal_do_fabricante`, que é a viga deste esquema inteiro.

Segunda rodada: **24 de 24 reprovadas, e as 24 só o portão novo viu.**

## DE PASSAGEM, UMA FERRAMENTA NO DISCO FORA DO MANIFEST — E QUEM A ACHOU FOI O PRÓPRIO PORTÃO

`ferramentas/mutacoes-base.py` nasceu nesta manhã, às 10h16Z, e **não entrou no manifest**. O
`atualizar-manifest.py --gravar` **se recusou a gravar** enquanto a linha não existisse: *"FERRAMENTA NO
DISCO FORA DO MANIFEST"*. Entrou com descrição própria, e a linha dela diz que entrou tarde e por quem.

## BANCADA DESTA EXECUÇÃO

`validar-banco.py` verde (38 materiais, 0 sem saída de compra, 0 piso não rastreável), `cobertura.py`
recontada e **sem mudança** — continuam **duas** categorias sem nenhum item (`base`, `apoio`), porque
decisão de campo não é SKU —, `validar-pastilhas.py` 189 afirmações, `tecnica-x-material.py` reescrito sem
mudança, `teste-casca.php` 555 verificações, `teste-f2.php` 114 afirmações, `teste-f1.php` 196 sobre 24
estados com processo próprio, `teste-prestacao-rejunte.php` 5 afirmações sobre 540 estados da F2 e 180 da
F1, `teste-tecnicas.php` 123, `teste-loja.php` 178 sobre 72 estados e `teste-leads.php` 211 sobre 8.

**E as baterias de mutação inteiras, porque a mudança foi no ESQUEMA e o esquema é lido por quase todas:**
`mutacoes-apoio` 24/24, `mutacoes-base` 20/20, `mutacoes-f2` 50/50, `mutacoes-f1` 46/46, `mutacoes-arvore`
21/21, `mutacoes-rejunte` 16/16, `mutacoes-cobertura` 14/14, `mutacoes-acabamento` 14/14,
`mutacoes-pastilhas` 14/14 e `mutacoes-tecnica-x-material` 9/9 — **228 mutações, nenhuma passando**.

## DESEMBARQUE E VERIFICAÇÃO NO AR

O `dados/esquema-banco.json` é item **`publicar: true`** do manifest — a casca e a F2 leem a *option*
`clubedomosaico_dados_esquema-banco` em tempo de requisição. Então este bloco **é publicável**, e o Sync
foi acionado: **revisão 44 aplicada às 14h57Z, `/status` batendo com o manifest, um disparo só.**
*(A execução das 10h16Z escreveu a versão 5 do esquema sem subir a revisão e registrou "não houve Sync";
o site ficou na 43 desde 25/09. A subida para 44 desembarcou as duas de uma vez.)*

**A prova de que o desembarque NÃO mexeu na página da posição 7,8**, que é o que o BLOCO A exige até
30/09: `/materiais/qual-cola-usar-no-mosaico/` continua servindo **270 combinações** e **45** linhas na
tabela — `9 × 5 × 6`, os mesmos números de antes —, medido no endereço **canônico** e no mesmo endereço
**com quebra de cache**, que devolveram o mesmo número. As três chaves que a F2 lê do esquema
(`vocabularios.base`, `.ambiente`, `.material_tessela`, o `mapa_de_termos_do_fabricante` e as
`regras_de_elegibilidade`) **não foram tocadas**: a versão 6 só acrescenta chaves novas, e nenhuma página
percorre `vocabularios` de forma genérica. E `conferir-no-ar.py` refeito depois do Sync: **488 afirmações,
0 falha**, o mesmo número da abertura.

- **Próximo passo desbloqueado:** o que sobra das duas categorias vazias **não é mais decisão de campo, é
  CANAL**. `base` e `apoio` têm regra escrita, portão de pé e bateria verde, e as duas esperam a mesma
  coisa: uma frase de fabricante que esta nuvem consiga **citar literalmente** — o egresso direto está em
  000 e o canal de busca devolveu resumo e tradução nas duas tentativas de hoje. O item que resolve as
  duas junto é o **egresso de fabricante**, que já está na lista do que depende do Raphael. Enquanto isso,
  a fila útil desta ilha é a leitura de **30/09**: ela é a terceira condição de pronto dos itens 1 e 2 do
  despacho da Sentinela de 23/09, é o que libera o **BLOCO A** (CTR das três páginas de primeira página) e
  é o que autoriza a decisão do Raphael sobre os dois valores novos de `vocabularios.base`.

28/09/2026 16:17Z — DESPACHO DA SENTINELA DE 28/09 ENTREGUE, quatro itens inteiros e meio: cinco camadas, e DUAS contagens da ronda corrigidas pela medição

Revisão **46** no ar. *(A 45 levou o bloco; a 46 e a decisão da 25.2-b, escrita no `esquema-banco.json` depois de o manifest da 45 estar fechado — sha velho no manifest é commit sem entrega com um passo de silêncio a mais.)* Casca **1.16.0**, Loja **1.3.0**, F1 **1.4.0**, F2 **1.6.0**, Ateliê **1.4.0**,
Tecnicas **1.2.0**. Foi a primeira ronda diária técnica que esta ilha recebeu, e o despacho dela tinha
cinco itens; pela 18.2 correção sai inteira, e pela 18.3 o que sobrou está reescrito no `PROMPT.md` com o
motivo. A ilha estava livre (`executando_desde: null`), a rede respondeu 200 nas duas tentativas da 20.2, e
o despacho do Raphael de 24/09 não furou a fila porque o único bloco aberto dele (o **BLOCO A**) espera
30/09 por ordem do próprio despacho.

**O ACHADO QUE MUDA O QUE O ITEM 2 ERA.** A ronda escreveu que os estados com parâmetro de
`/materiais/qual-cola-usar-no-mosaico/` não saíam do índice e que a reconferência do conserto de 25/09
tinha falhado nessa metade. Falhou mesmo — mas a causa não é a que o nome do defeito sugere, e ela só
aparece lendo as **duas** ferramentas lado a lado: **elas liam a MESMA pergunta de dois jeitos opostos.**

- O `escolheu` da F1 pergunta `isset( $_GET['forma'] )` — **a presença** do parâmetro.
- O `escolheu` da F2 pergunta `isset( $rot['base'][ $base ] )` — **a validade do valor**.

As três URLs que a ronda mediu (`?base=ceramica&onde=externo`, `?base=mdf`,
`?base=ceramica&caco=louca&junta=fina&onde=interno`) têm os quatro **nomes de parâmetro reais** e **nenhum
valor que exista** no vocabulário — as chaves são `ceramica_esmaltada_porcelana`, `externo_exposto`,
`mdf_madeira`, `caco_louca`, e `junta` é número. Então a F2 respondia "não escolheu nada" e a página entrava
no índice com três endereços a mais. **E a F1 passou pelo motivo oposto e igualmente por acidente:** a régua
de 25/09 a mediu com `?forma=vaso&caquinho=medio`, em que `forma` foi enviado. Com `?caquinho=medio`
sozinho ela teria falhado igual. **Duas irmãs, cada uma acertando o portão da outra por sorte.**

O conserto separa as duas perguntas, e a separação é a parte que vale:

- **`escolheu` manda na TELA** e continua medindo o **valor**, nas duas. Valor fora do vocabulário volta ao
  padrão em silêncio e a página que sai é a âncora; dizer "você escolheu" sobre uma escolha que a página não
  honrou seria trocar um defeito de índice por um defeito de texto.
- **`cdm_fX_tem_parametro()` manda no `noindex`** e mede a **presença**. Para essa pergunta o valor não
  importa: `?base=lixo` é um endereço diferente servindo o MESMO HTML, que é a definição de duplicata — e o
  conjunto dos valores inválidos é **infinito**, enquanto o das escolhas válidas é finito.
- Só os parâmetros **da própria ferramenta**, nunca "qualquer query": `noindex` em toda URL com `?`
  alcançaria a paginação e a busca do núcleo, e tirar do índice página que rankeia é o lado caro da borda —
  esta ilha tem TRÊS páginas na primeira página do Google.

**E um buraco medido de brinde:** a lista de parâmetros da F1 estava escrita à mão dentro do `escolheu` e
nomeava `d`, `h`, `l` e `a` — **esquecendo o `d2`**, o diâmetro do fundo do cone, que existe desde que a
forma cônica existe. `cdm_f1_parametros()` agora deriva os campos de `cdm_f1_formas()`, e a bancada afirma
que toda medida de toda forma está na lista. `?d2=12` sai com `noindex` no ar.

**A SEGUNDA CONTAGEM CORRIGIDA — O ITEM 3 ERA 27 E SÃO 5.** A ronda contou 27 imagens com `alt=""` nas
cinco páginas de peça e pediu que "todas" ficassem com alt não vazio. Contadas de novo aqui, imagem por
imagem no HTML servido, elas se separam em duas famílias e a separação muda o conserto:

- **5 são a foto de DESTAQUE** (`attachment-post-thumbnail`, do bloco do núcleo, que lê
  `_wp_attachment_image_alt` da biblioteca de mídia). Nenhuma foto da artesã tem esse campo. É a foto
  **principal** de cada peça, a que `Product.image` aponta, e nesta ilha a foto **é** o produto — a própria
  `/loja/` diz "a foto é a da peça que você vai receber". **Este é o defeito.**
- **22 são as miniaturas da tira do carrossel**, e o `alt=""` delas é **deliberado**, com o motivo escrito em
  `cdm_loja_miniaturas_html()` desde que a tira nasceu: a miniatura repete a foto que já tem `alt`
  descritivo logo acima, e o nome do controle está no `<a>`, num `<span class="cdm-gal-so-leitor">`. Imagem
  decorativa que repete conteúdo vizinho leva `alt=""` — é a regra, não a exceção. **Preenchê-las para o
  número chegar a zero faria o leitor de tela ler a peça inteira duas vezes.** Régua que não sabe distinguir
  decorativo de descritivo cobra a piora, então a régua nova deixa a tira de fora **por nome**.

**O ALT AGORA SAI DE UMA FUNÇÃO SÓ.** Eram três lugares: o molde do carrossel escrevia
`<título>, mosaico em <base>, foto N`, o cartão da vitrine escrevia a mesma frase de novo, e o núcleo não
escrevia nada na foto de destaque. Agora os três chamam `cdm_loja_alt_da_foto()`, no formato que o despacho
recomenda — **técnica na frente da base**, porque quem olha a foto vê louça quebrada, não vê MDF. No ar:
`Vaso com flores em cerâmica — pica-sete (louça quebrada), foto 1`. Com uma foto só o "foto 1" não entra:
seria ruído lido em toda peça da vitrine. E o `alt` da artesã **sempre vence** — o filtro só entra quando o
campo está vazio.

**O ITEM 1 FOI CONSERTADO DOS DOIS LADOS, e o despacho tinha razão em exigir os dois.** O campo
`_cdm_medidas` de quatro peças trazia a unidade dentro do valor (`46x36cm`, `35cm de diâmetro`) e o molde
acrescentava ` cm` depois, nos **três** lugares que servem medida — a frase da ficha (que vira o
`description` do `Product`), o `additionalProperty` do JSON-LD e a linha do cartão. Consertar só o molde
deixaria o banco com quatro formatos; consertar só o dado deixaria o molde pronto para dobrar o próximo
valor que chegasse por outro caminho. Entraram: `cdm_loja_medida_normalizada()` (o que se grava),
`cdm_loja_medida_na_tela()` (o que se serve), a normalização no `/atelie/` na hora de salvar, e uma migração
idempotente presa a uma chave de option para as peças que já existiam. **No ar:** `40×28 cm`,
`35cm de diâmetro`, `46×36 cm`, `46cm de diâmetro`, `46×37 cm`.

**E O QUE ELAS NÃO FAZEM:** reescrever a frase da artesã. `35cm de diâmetro` é texto dela, tem **uma**
unidade, e sai como ela escreveu — o que se tira é a unidade REDUNDANTE, a do fim do valor, no lugar exato
onde o molde ia pôr a dele. Valor com uma unidade por dimensão (`12 cm x 5 cm`) fica **intocado**: tirar a
última daria `12 cm × 5`, que é pior que o defeito.

**O ITEM 4 É O QUE O PRÓPRIO DESPACHO DISSE QUE ERA:** *"não é o texto de uma página: é qual camada emite a
etiqueta e para quais tipos de página"*. E é o **mesmo desenho** que fez a etiqueta de robô sair dobrada em
25/09, com o sintoma **invertido** — lá o excesso, aqui a falta, e falta não tem cor na tela. Quem tinha
snippet próprio imprimia a sua num `wp_head` paralelo (as duas ferramentas, os dois tutoriais, as cinco
peças pela Loja) e as **oito páginas da casca não tinham quem imprimisse**. Agora **quem tem `description`
DECLARA pelo filtro `cdm_descricao`; quem imprime é a casca, uma vez.** As oito nasceram entre **121 e 143**
caracteres, nenhuma repetida, e a home é tratada à parte porque `cdm_casca_slug_atual()` devolve vazio na
frente do site — sem essa linha o conserto pularia justamente a URL mais visitada da ilha.

**O ITEM 5 e o portão que estava medindo a pergunta errada.** Os 13 itens (7 de acabamento, 6 de alicate)
estavam com `afiliado.degrau` em `null` servindo degrau 4 na tela, e o validador aprovava porque cobrava o
degrau de quem tinha `afiliado.url` — a ficha de produto. **Item que serve BUSCA não tem `url`**, então a
regra velha nunca alcançava o degrau 4, e o esquema dizia o mesmo em `obrigatorio_quando`. Agora o degrau é
cobrado de quem **serve** link, a escada é contada no relatório — **1:1 · 2:5 · 3:4 · 4:28, soma 38** — e
`ferramentas/mutacoes-degrau.py` (8 mutações nos **cinco** bancos, porque o buraco era do portão e não do
arquivo) reprova 8 de 8, **4 delas só pelo portão novo**. A regra antiga fica guardada no esquema em
`obrigatorio_quando_ate_28_09_2026`, porque ela explica um número do histórico.

**A SEGUNDA OBSERVAÇÃO DO DESPACHO FOI DECIDIDA**, como ela pedia: a **25.2-b nomeia um CONCEITO, não um
campo**. Nesta ilha o conceito tem **dois** campos e não um — `url_busca_gerada_em` declara o sucesso e
`motivo_sem_url_busca` declara o fracasso —, e o par cobre os dois desfechos que a regra nomeia. Um campo
`encurtamento_tentado_em` sozinho cobriria só o carimbo e diria "tentei" sem dizer o que aconteceu. Está
escrito em `dados/esquema-banco.json`, em `e_o_campo_de_tentativa_da_25_2_b`.

**O QUE NÃO SAIU, E O MOTIVO É DESPACHO DE PRIORIDADE MAIOR.** A **faixa** de 120 a 160 nas quatro páginas
que já tinham `description` — `qual-cola` (183), `quantas-pastilhas` (165), `picassiete` (192), `trencadis`
(189). **Três delas estão na primeira página do Google** e o **BLOCO A do despacho do Raphael de 24/09**,
que pela 18.1 vem antes deste, diz com todas as letras que espera **30/09**, porque *"trocar título antes do
número de 30/09 misturaria duas causas na mesma janela"*. A `description` é a outra metade da mesma promessa
de SERP. **E é por isso que o pedido de cumprir a Proposta 1 no mesmo movimento não foi obedecido:** fazer só
a `description` agora seria a pior das três opções — mexeria na janela de medição sem entregar a alavanca
inteira. A régua no ar **já mede as quatro** e **imprime o número delas** para não ser esquecido; fechar isto
depois de 30/09 é tirá-las da lista `TRAVADAS_ATE_30_09`.

**BANCADAS.** Casca 563, Loja 196, F1 200, F2 119, Tecnicas 123, Ateliê 289, Leads 211, Prestação 5 — zero
falha. Validador do banco verde. **E no ar: `conferir-no-ar.py` com 501 afirmações e 0 falha** (eram 488 na abertura; as 13 novas são as réguas dos quatro itens). **E cada régua nova foi provada contra o defeito que a fez nascer, não
contra o conserto:** revertida a condição da F2, a bancada reprova servindo
`<meta name='robots' content='max-image-preview:large' />` nas três URLs — o texto exato que a ronda mediu
no ar; revertida a da F1, ela reprova no `d2`. **A régua da unidade dobrada foi escrita ERRADA na primeira
tentativa e o próprio teste pegou:** com `\b` antes da unidade ela **não reconhecia** `46x36cm cm`, porque
entre o `6` e o `c` não há fronteira de palavra. É a família da régua de robô que media a **aspa** em vez da
diretiva, que esta ilha pagou em 25/09 — régua que não reconhece o defeito que a fez nascer aprova o
desastre calada. Agora ela exige o número na frente, e a bancada afirma as duas direções.

**E as mutações de `noindex` da F1 e da F2 estavam a caminho de virar INERTE**, que é o pior dos dois
estados: a bateria continuaria verde dizendo que mediu. Foram retargetadas para a condição nova e ganharam
uma **mutação nova** que escreve de volta a regressão exata de 28/09 — o `noindex` voltando a depender do
valor. **Rodadas no código final: F2 51 de 51 reprovadas, F1 47 de 47, Loja com as 37 pegas, degrau 8 de 8 —
zero passou, zero inerte, zero sem compilar.**

**E UMA BANCADA VERMELHA ACHADA DE PASSAGEM, QUE NÃO ERA DESTE DESPACHO.** `conferir-atelie-no-ar.py`
estava com **2 falhas** e as duas eram da régua, não do site: ela procurava a frase literal
`content="noindex, follow"` com **aspas duplas** — as do `echo` que o snippet do Ateliê fazia num `wp_head`
próprio — e quem imprime a etiqueta desde a casca **1.13.0** (25/09) é o `wp_robots()` do **núcleo**, com
aspas **simples**. O painel sai do índice corretamente e a régua o reprovava. **É exatamente a cicatriz que
`conferir-no-ar.py` pagou em 25/09** — *"a etiqueta de robô se mede pela diretiva e pela contagem, nunca
pela aspa"* — e o conserto daquele dia **passou ao lado desta bancada**, que ficou vermelha três dias sem
ninguém olhar. Pior que reprovar o certo: a mesma régua **passaria a vazio** num painel que saísse do índice
por engano, porque a frase com aspa dupla é falsa nos dois mundos. Agora ela mede a **diretiva** e **conta**
as etiquetas, como a irmã. **184 afirmações, 0 falha, 3 puladas** (as três dependem do token, e o token não
foi usado nesta execução).

- **Próximo passo desbloqueado:** a leitura de **30/09**. Ela continua sendo o que libera o **BLOCO A** (CTR
  das três páginas de primeira página, com o veredito em 08/10), e agora ela libera também a **metade que
  falta do item 4** — as duas são a mesma promessa de SERP nas mesmas páginas e saem no mesmo movimento, que
  é exatamente por isso que nenhuma das duas saiu hoje. O que **não** depende dela continua sendo o egresso
  de fabricante, que trava as duas categorias vazias (`base` e `apoio`) e está na lista do Raphael.

# 30/09/2026, 10h16Z — A PORTA DO EGRESSO NÃO ESTAVA FECHADA: ESTAVA PELA METADE, E QUATRO EXECUÇÕES A CHAMARAM DE FECHADA

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **10h16Z** com `executando_desde` e push
aceito na primeira tentativa. **NENHUMA URL NOVA** — a ilha segue em 17 —, **nenhum título e
nenhuma `description` mudaram**: o BLOCO A do despacho do Raphael de 24/09 continua intocado e a
janela de medição de 30/09 segue limpa. Manifest e `/status` na revisão **51**.

## A PORTA DE ENTRADA, ANTES DE QUALQUER BLOCO (seção 29.2)

`conferir-no-ar.py`: **519 afirmações, 0 falha** na origem. `leitura-do-visitante.py`:
**REPROVADO com 1 defeito, e é o esperado** — o soft 404 do hospedeiro (404 na 1ª leitura, 200 na
2ª, `x-proxy-cache: HIT`, `max-age=7200`), aberto em 29/09, com dono escrito e fora do alcance de
qualquer snippet daqui. **Nenhum defeito novo.** Rede pela 20.2: três passadas em
`clubedomosaico.com.br`, 200 nas três, com `aquametria.com.br` em 200 nas mesmas.

## O QUE ESTE BLOCO É, E POR QUE NÃO É O BLOCO A

O passo que o registro de 29/09 deixou nomeado como desbloqueado era **a leitura de 30/09** — é
hoje. **Ela não pode ser feita daqui, e agora isso está medido por dois lados independentes:** a
conta de serviço `sentinela@` não tem acesso a `sc-domain:clubedomosaico.com.br` (escrito em
`dados/search-console-2026-09-23.md` desde 23/09) **e a credencial não está neste ambiente** —
`GOOGLE_SA_B64`, `GOOGLE_SA_JSON` e `GOOGLE_SA_FILE` estão as três ausentes, conferido nesta
execução. Sem uma das duas, o BLOCO A e a metade que falta do item 4 do despacho de 28/09 (a faixa
de 120 a 160 nas quatro `description`) continuam travados, e **o veredito de 08/10 escorrega**.
Está no aviso ao Raphael.

**O que sobrava sem depender dela era o egresso de fabricante.** A 20.2 manda retestar bloqueio
herdado antes de respeitá-lo, e a lição da Quartzolit de 29/09 estendeu isso a bloqueio herdado de
**documento**. Foi o que esta execução fez — e a resposta não era nenhuma das duas que estavam
postas.

## O ACHADO: O APEX RESPONDE, O `www.` NÃO, E NENHUMA FONTE MORA NO APEX

Medido às **10h22Z**, e o que separa este relato de um palpite é o cabeçalho. Os apex
`quartzolit.weber`, `tekbond.com.br`, `cascola.com.br` e `loctite.com.br` devolvem
`HTTP/1.1 200 Connection Established` — **o CONNECT passa** — e em seguida o servidor **de
verdade** responde **301**, com `server: Apache` e `server: CloudFront`, data, `content-length` e
`location`. Os quatro domínios **entraram na lista de rede** entre 29/09 e hoje.

**E o ganho é zero.** Os quatro redirecionam tudo para o host `www.` (a Loctite para
`next.henkel-adhesives.com`), e esse host responde `connect_rejected` — política de egresso — nas
três passadas. As **36 URLs de boletim técnico** que os bancos desta ilha citam nesses domínios
estão **todas** em `www.`, incluindo os sete PDFs da Quartzolit e os dois da Tekbond.
`pastilhart.com.br` não entrou nem no apex.

**A frase que o repositório afirmava em quatro lugares — "403 ao CONNECT" — é FALSA hoje**, e a
frase oposta seria igualmente falsa. Os dois vereditos têm de sair juntos:

- Um portão que medisse só o CONNECT diria **"liberado"** e mandaria a próxima execução coletar o
  que não há como ler.
- Um que medisse só o código final diria **"bloqueado"** e esconderia que falta **uma linha**, não
  uma decisão.

**A 20.1 sempre mandou os dois**, `<domínio>` **e** `*.<domínio>`. O pedido de 29/09 foi atendido
só na primeira metade, e nenhuma das quatro execuções anteriores tinha o veredito
`liberado_mas_sem_entrega` para escrever.

## A FERRAMENTA, E AS QUATRO TRAVAS QUE SÃO CICATRIZ DESTA ILHA

`ferramentas/medir-egresso.py`, com saída em `dados/egresso-de-fontes.md` e `.json` (gerados, não
editáveis à mão). **`--autoteste`: 29 casos fabricados, 29 ok** — passada limpa em portão que nunca
acusou nada não prova nada, e o **caso 6** é exatamente o mundo de hoje.

1. **A lista não é digitada.** Os hosts saem de `dados/*.json`. Lista escrita à mão envelhece
   calada — foi assim que `urls_publicadas` ficou quatro dias defasado.
2. **Três passadas, nunca uma** (20.2). Host que responde em duas de três sai como
   **intermitente**, que é veredito e não erro: foi um `000` lido como bloqueio que prendeu esta
   ilha dois dias em 11/09.
3. **Controle obrigatório.** Se `clubedomosaico.com.br` não responder nas três, a medição é
   **VOID** e nada é gravado. Sem isso, queda de túnel escreveria "tudo bloqueado" com cara de
   fato.
4. **A entrega é calculada, nunca escrita.** Apex que só redireciona para host recusado sai como
   `liberado_mas_sem_entrega`, com o host que falta nomeado.

## TRÊS DEFEITOS DA PRÓPRIA FERRAMENTA, OS TRÊS ACHADOS POR ELA RODANDO E OS TRÊS ANTES DO COMMIT

**(1) A primeira versão não viu o achado do dia.** Ela media só os hosts que os bancos citam — e os
bancos citam `www.quartzolit.weber`, nunca o apex. Resultado: imprimiu `bloqueado` para os quatro
fabricantes e **o único fato novo do dia ficou invisível**. Portão que mede só o que o banco cita vê
só o lado que o banco já conhece. Corrigido medindo o **irmão** de cada host — o apex e o `www.` do
mesmo domínio registrável —, o que exigiu `dominio_registravel()` com sufixos de dois rótulos
(`com.br`, `leg.br`, `gob.es`), porque `www2.camara.leg.br` pelo "penúltimo rótulo" daria `leg.br`
e o pedido sairia errado. **Doze casos de autoteste só para isso.**

**(2) Ela lia a própria saída e se citava como fonte.** `egresso-de-fontes.json` nasce em
`dados/` e na passada seguinte apareceu em "citado em: egresso-de-fontes.json". É circular: o
portão passaria a se sustentar no que ele mesmo escreveu ontem, que é a seção 4 do contrato com
outra roupa.

**(3) `loctite.com.br` — o quarto domínio meio-aberto — ficou fora da medição de 36 hosts**, porque
`loctite` aparece nos bancos como **marca** e nunca como URL: nenhum SKU dele foi coletado. A 20.3
manda que quem escreve a regra que exige a fonte confira se a fonte está liberada, então a fonte
exigida em prosa teve de virar **dado**: `dados/fontes-pedidas.json`, onde cada linha aponta **quem
a exige** e a ferramenta **recusa** linha sem `exigido_por` — senão viraria lista de desejo. E o
gatilho teve de aprender a ler esse arquivo: na passada seguinte `loctite.com.br` saiu listado em
"bloqueado e **não pedido**", que é o absurdo de um portão não ler o arquivo escrito para ele ler.

**Um segundo extrator nasceu no caminho**, e a fonte que mais trava esta ilha só existe por causa
dele: os **dez** fabricantes de painel de MDF que `regras_da_categoria_base` nomeia estão em
**prosa**, num campo chamado `dominios_em_000`, e nenhum é URL. Campo cujo **nome** fala de domínio
passou a ser lido como lista de domínio — com trava, porque na primeira tentativa ele pediu rede
para **`validar-banco.py`** (dois rótulos, TLD de duas letras: tem a forma de um host e não é um).

## O PEDIDO, AGORA DERIVADO E COM DONO POR LINHA

**21 domínios, 42 linhas**, cada um com o arquivo que o exige, em `dados/egresso-de-fontes.md`. E o
que **não** se pede está escrito junto, com o motivo: marketplace (o link nasce pela Open API da
25.6, não por leitura de página) e as **16 referências de conteúdo já lidas e já citadas** —
Wikipédia, `camara.leg.br`, teses, museus. Elas também não chegam, e não se pedem: nenhum trabalho
pendente depende delas, e **pedido longo é pedido que não se atende**.

## A `base` NÃO É ALCANÇADA POR ESSA CORREÇÃO, E O NÚMERO DIZ POR QUÊ

Os dez fabricantes de painel — `dexco`, `duratex`, `guararapes`, `arauco`, `berneck`, `eternit`,
`brasilit`, `termotecnica`, `isoeste`, `leroymerlin` — estão em **000 no apex E no `www.`**, três
passadas, com o controle em 200. **Nenhum entrou na lista.** O primeiro SKU de `base` continua
esperando frase de fabricante que esta nuvem possa citar literalmente, e a correção de hoje não o
alcança. Para a `apoio` é o contrário: a FISPQ do epóxi mora justamente em `www.`, então **o curinga
a destrava**.

## DUAS BATERIAS VERMELHAS NO `main`, HAVIA UM DIA, E NINGUÉM AS ESTAVA VENDO

Achado de passagem, e **medido vermelho no `main` limpo antes de qualquer mudança desta execução**:
`mutacoes-base.py` e `mutacoes-apoio.py` fechavam com *"o mundo FABRICADO já está reprovado antes de
qualquer mutação. Portão que reprova o mundo certo não mede nada."*

**A causa é a melhora de ontem.** As duas nasceram em 28/09 com `"degrau": None` no mundo
fabricado, e isso era válido naquele dia. A leva de 29/09 às 16h17Z tornou o degrau **obrigatório**
para todo item que serve link de compra — e a partir dali as duas baterias passaram a se recusar a
rodar. **Não é vermelho inofensivo:** bateria que não roda deixa os portões novos das duas
categorias, 20 e 24 mutações, **sem ninguém medindo** — e foi por isso que o vermelho passou um dia
inteiro sem ser visto. É a mesma família do `conferir-atelie-no-ar.py`, que ficou três dias
vermelho por medir a aspa em vez da diretiva.

**O conserto não foi cravar `4`: foi calcular.** O mundo fabricado não tem `url_produto` e tem
`url_busca`, e a 25.1 diz que item que serve só busca é degrau 4 — então o degrau sai dos campos,
por duas constantes que são as mesmas que o mundo usa. Cravar o número deixaria a bateria à espera
do próximo aperto de regra para apagar-se outra vez. **De volta ao verde: `mutacoes-base` 20 de 20
reprovadas, `mutacoes-apoio` 24 de 24** — os números que o registro de 28/09 declarava.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Não coletou nenhum SKU.** A porta continua sem entregar; coletar hoje seria escrever paráfrase
  de resumo em `literal_do_fabricante`, que é a viga do esquema.
- **Não tocou em `<title>` nem em `description`** de nenhuma das 17 URLs. O BLOCO A espera o número
  de 30/09 por ordem escrita do Raphael, e a janela segue limpa.
- **Não afrouxou nenhuma régua** para o mundo fabricado passar. O degrau passou a ser derivado, não
  tolerado.

## DESEMBARQUE E VERIFICAÇÃO NO AR

Push aceito na primeira tentativa. Sync acionado **depois** do push, porque ele lê o
`manifest.json` do `main` pelo `raw.githubusercontent` — o disparo anterior ao push leu a revisão
**50** e foi descartado, que é a forma de "commit sem Sync não é entrega" da seção 20 com a ordem
invertida. Sync na **revisão 51**, 14 aplicados, e `/status` devolvendo **51**, igual à do manifest.

**BANCADA DESTA EXECUÇÃO.** Casca 591, Loja 208, F1 200, F2 119, Técnicas 123, Ateliê 289, Leads
211, Prestação 5 — **zero falha**. `validar-banco.py` verde (38 materiais, 0 sem saída de compra, 0
piso não rastreável, escada **1:1 · 2:5 · 3:15 · 4:17**, soma 38). `cobertura.py` recontada **sem
mudança** — seguem duas categorias em zero (`base`, `apoio`). Baterias: `mutacoes-degrau` 8 de 8,
`mutacoes-batismo` 14 de 14, `mutacoes-casamento` 5 de 5 no banco, `mutacoes-acabamento` 14 de 14,
`mutacoes-base` **20 de 20** e `mutacoes-apoio` **24 de 24** (as duas de volta ao verde nesta
execução). `medir-egresso.py --autoteste` **29 de 29**. **E no ar: `conferir-no-ar.py` com 519
afirmações e 0 falha**, medido antes e depois do desembarque.

**E A BATERIA MAIS LENTA DA ILHA FECHOU VERDE, depois do push:** `mutacoes-cobertura.py` roda
**dois portões inteiros por mutação** (`validar-banco.py` e `teste-f2.php`, este varrendo 105
estados), levou perto de uma hora e fechou em **14 mutações, 14 reprovadas, 0 passaram** — com o
mundo intacto saindo **APROVADO** antes de começar, que é exatamente a afirmação que estava falhando
em `mutacoes-base` e `mutacoes-apoio`. **Nove das 14 nenhum portão antigo pegou**, entre elas *"o
GERADOR conta errado e regenera coerente com o próprio defeito"* e *"o resumo do censo é digitado em
vez de contado"*. Ela não foi tocada por este bloco, e a árvore ficou limpa depois dela: os 14
bancos seguem parseando.

*(Esta frase substitui, no mesmo lugar, a que esta execução escreveu antes do push dizendo que a
bateria **não** terminara — e a substituição é o ponto, não um detalhe: naquele momento a frase
honesta era "não afirmo verde nem vermelho no que não vi fechar", e é ela que este parágrafo pôde
trocar por um número. Bancada que ainda roda se declara em aberto; nunca se arredonda para verde.)*

**E a reprodutibilidade do artefato foi conferida, não presumida:** re-derivados os hosts depois de
todas as edições do esquema, são **76**, os mesmos 76 que `dados/egresso-de-fontes.json` gravou,
sem nenhum a mais nem a menos. Arquivo gerado que não fecha com a própria derivação é o começo de
um número que ninguém sabe de onde veio.

- **Próximo passo desbloqueado: continua sendo a leitura de 30/09, e agora ela tem DOIS donos
  possíveis escritos** — o acesso da conta `sentinela@` a `sc-domain:clubedomosaico.com.br`, ou a
  credencial `GOOGLE_SA_B64` no ambiente das rotinas. Qualquer uma das duas serve; **nenhuma existe
  hoje**, e sem ela o BLOCO A e a faixa de `description` das quatro páginas ficam onde estão. O
  segundo item do Raphael é o **curinga** dos quatro domínios de adesivo mais o par de
  `pastilhart.com.br`, e esse destrava a `apoio` — a lista inteira, derivada, está em
  `dados/egresso-de-fontes.md`. **O que NÃO depende de ninguém:** nada na fila desta ilha. As três
  técnicas em zero esperam fonte, `base` espera dez domínios que não entraram, os 13 itens de
  pastilha no degrau 4 são decisão do Raphael (`tipo_de_casamento: "equivalente"`) e os dois da
  Quartzolit não têm anúncio único na Shopee. **É por isso que esta execução mediu em vez de
  construir, e não por falta de fôlego.**

# 30/09/2026, 13h17Z — O SEGUNDO DEGRAU DA 7b NUNCA TINHA SIDO CONTADO, E "NADA NA FILA" ERA UMA FRASE QUE NINGUÉM MEDIU

**Ilha em foco** (`foco.md`, desde 24/09), reservada às **13h17Z** com `executando_desde` e push
aceito na primeira tentativa. **NENHUMA URL NOVA** — a ilha segue em 17 —, **nenhum título e
nenhuma `description` mudaram**: o BLOCO A do despacho do Raphael de 24/09 continua intocado e a
janela de medição de 30/09 segue limpa. Manifest e `/status` na revisão **52**.

## A PORTA DE ENTRADA, ANTES DE QUALQUER BLOCO (seção 29.2)

`conferir-no-ar.py`: **519 afirmações, 0 falha** na origem. `leitura-do-visitante.py`:
**REPROVADO com 1 defeito, e é o esperado** — o soft 404 do hospedeiro (404 na 1ª leitura, 200 na
2ª), aberto em 29/09, com dono escrito e fora do alcance de qualquer snippet daqui. **Nenhum defeito
novo.** Rede pela 20.2: três passadas em `clubedomosaico.com.br`, 200 nas três, com
`aquametria.com.br` em 200 nas mesmas.

## O QUE ESTE BLOCO É, E POR QUE ELE CONTRADIZ AS DUAS EXECUÇÕES ANTERIORES

O registro das 10h16Z de hoje fechou dizendo, com todas as letras: *"O que NÃO depende de ninguém:
**nada na fila desta ilha**."* O de 29/09 dissera o equivalente. **Esta execução derrubou a frase**,
e o caminho foi o que a própria ilha já tinha escrito duas vezes como lição: a **20.2** manda
retestar bloqueio herdado antes de respeitá-lo, e a 7b-ter de 25/09 estendeu isso a bloqueio herdado
de **documento** — *"quatro execuções anotaram 'esbarra no egresso' sem abrir a fonte que estava em
casa"*.

**Primeiro, o que era bloqueio de verdade e continua sendo, conferido e não herdado:** a leitura de
30/09 não sai desta nuvem. `GOOGLE_SA_B64`, `GOOGLE_SA_JSON`, `GOOGLE_SA_FILE` e
`GOOGLE_APPLICATION_CREDENTIALS` estão **as quatro ausentes** (a execução anterior mediu três; a
quarta também não existe), e o acesso do `sentinela@` a `sc-domain:clubedomosaico.com.br` segue
pendente com o Raphael. Então o **BLOCO A** e a metade que falta do item 4 do despacho de 28/09
seguem travados, e **o veredito de 08/10 escorrega**. Nada disso mudou.

**Segundo, o que não era bloqueio:** a ordem da seção 7b do `ARVORE.md` — *"Banco. (...) Só então as
filhas de nível 3, por cluster. Só então a mãe de nível 2, que é o 4c."* — está escrita desde
12/09/2026, e o **segundo degrau nunca foi MEDIDO**. O que existia era *"nenhuma filha de alicate
existe"*, que diz o que falta e **não diz o que já dá**. Entre "o 4c está fechado" e "quais páginas
podem nascer amanhã" há uma **contagem**, e ela nunca tinha sido feita. Fazê-la não dependia de
ninguém: nem de rede, nem de credencial, nem de decisão do Raphael.

## A FERRAMENTA, E O QUE ELA MEDE QUE NENHUMA OUTRA MEDIA

`ferramentas/filhas-do-guia.py` aplica o portão **inteiro** da seção 9 — *"pelo menos 3 itens de
banco reais **e** um número calculado próprio por página"* — a cada recorte que o vocabulário do
esquema admite no Guia. **A segunda metade nunca tinha sido contada nesta ilha.** O `cobertura.py`
conta itens elegíveis por **faixa das ferramentas**, que é outra pergunta; contar se existe um número
que a página consegue calcular **sobre 3 itens do mesmo recorte** é o que decide se a página compara
três produtos ou mostra um número e duas lacunas.

**Nada é digitado.** Os 42 recortes saem de `vocabularios.tipo_por_categoria` (categoria inteira mais
cada tipo), o teto de nível de fonte sai de
`escada_de_fontes.nivel_minimo_para_recomendacao_primaria`, e os itens saem dos
`dados/materiais-*.json`. Recorte digitado mediria os recortes que alguém lembrou, e ficaria verde no
dia em que o vocabulário crescesse — que é justamente o que acontece aqui, onde a regra de
crescimento faz valor novo nascer junto com o primeiro registro que o usa.

**TRÊS VEREDITOS, NUNCA UM BOOLEANO,** e a razão é a lição que o `medir-egresso.py` desta mesma ilha
pagou às 10h22Z de hoje: *"os dois vereditos saem juntos ou nenhum dos dois serve."* Um portão que
olhasse só a **contagem** diria que `alicate/torques` passa (três registros) e mandaria escrever uma
página que compara um produto com dois silêncios; um que olhasse só a **declaração** esconderia que
falta uma frase de fabricante, não um produto. Então: `passa`, `passa_na_contagem_sem_lastro`,
`nao_passa`.

**E a régua reproduziu, sem ser mandada, o exemplo que o próprio esquema nomeia:** o
`loctite-durepoxi` sai da contagem de lastro porque sua única declaração tem fonte de **nível 4**
(press release) — que é textualmente o caso que a `regra 5` do esquema escreveu para explicar a
própria regra. Régua que reencontra sozinha o exemplo da regra é régua que está lendo a regra, e não
a lembrança dela.

## O NÚMERO: 7 PASSAM, 3 PASSAM SÓ NA CONTAGEM, 32 NÃO PASSAM — E NENHUMA CATEGORIA ALCANÇA A 16.5

Passam: `acabamento`, `acabamento/verniz`, `alicate`, `alicate/cortador_de_azulejo`, `pastilha`,
`pastilha/vidro`, `rejunte`. Os de nível de **tipo** — que são os que podem ser filha — são **três**,
e são **um por categoria**: `acabamento/verniz`, `alicate/cortador_de_azulejo`, `pastilha/vidro`.

**Por isso nenhuma categoria do Guia alcança as 3 filhas da 16.5**, nem somando todos os tipos que o
vocabulário lhe dá. A mãe de nível 2 continua fechada — e agora por um **número**, não por uma frase.
O achado por trás do número: **o banco desta ilha é largo entre categorias e fino dentro de cada
uma**, então o 16.5 não se abre coletando em qualquer lugar; ele se abre coletando **dentro de uma**.

## A LISTA DE COMPRAS, QUE É O QUE SEPARA "NÃO PASSA" DE "NÃO SE SABE O QUE FALTA"

A lição é do `cobertura.py` desta ilha: *"O que falta nessa varredura é a lista de compras do banco —
e o número final aparece sozinho."* Por categoria, itens a coletar para ter as três filhas:
**`acabamento` 3** (1 impermeabilizante + 2 seladores) · `rejunte` 5 · `alicate` 5 · `cola` 6 ·
`pastilha` 6 · `base` 9 · `apoio` 9.

**A distância conta o MAIOR buraco, nunca a soma** — um item novo com número declarado fecha os três
de uma vez, e somar faria a lista pedir o triplo.

**E ela separa SKU novo de campo vazio,** que não custam a mesma coisa: `rejunte/cimenticio` está a
**um campo** de um registro que **já mora no banco** — `liberacao_area_molhada_h` no
`quartzolit-rejunte-piscinas` —, não a um produto novo.

## A CLASSIFICAÇÃO DE SERP DA 14.9 INVERTEU A ORDEM QUE A FILA SUPUNHA

A 14.9 manda olhar a SERP **antes** de criar a página. Feita nesta passada, consulta a consulta, em
`dados/filhas-do-guia.md`, abaixo de uma fronteira que o gerador **preserva** (busca não é derivação,
e regenerar o arquivo não pode apagar o que custou busca).

**As duas ABERTAS são PERGUNTA; as duas TOMADAS são PRODUTO.**

- `como cortar pastilha de vidro para mosaico qual ferramenta` → **8 de 10** são blog e resposta
  genérica sem número: Vila do Artesão, Obramax, FazFácil (2), Além da Rua Atelier (**2012**),
  Artesanato Benjoino (**2010**), O Portal das Maravilhas (2). **ABERTA**, e é o galho da 14.9 escrito
  ao pé da letra.
- `verniz para peça de mosaico artesanal qual usar` → Portal de Artesanato, três blogspots de
  **2010**, Revista Oeste, em.com.br, Viva Decora, Como Fazer Artesanatos. **ABERTA**.
- `pastilhas de vidro para mosaico` → **9 de 9** marketplace e loja: Mercado Livre, Buscapé, Elo7 (2),
  Bazar Horizonte, Vetro Designer, Mosaico & Cia, Mosaico em Casa, Pastilhart. **TOMADA.**
- `quantas pastilhas vem na caixa placa telada mosaico vidro medida` → **10 de 10** loja e obra,
  Leroy Merlin PT e Telhanorte inclusive. **TOMADA, e é a ARMADILHA do revestimento** que o corpus de
  10/09 já tinha nomeado — agora com evidência nova.

**A leitura, e ela não é sobre categoria:** quem vende produto **já ocupa** a consulta de produto, e
**ninguém ocupa** a consulta de método. Consequência dura para a fila: a filha de mais banco da ilha
— `pastilha/vidro`, 13 itens, três números em 12 deles — **passa no dado e a SERP recusa.** E a
ferramenta já dizia, na própria nota de alcance, que mede recorte de **tipo** e é um **piso**; a SERP
acabou de dizer que o piso mede a forma errada, e que as filhas publicáveis são **perguntas**, cuja
régua de contagem é a mesma.

## O QUE CADA ABERTA TEM DE NÚMERO QUE A SERP NÃO PUBLICA

- **Cortar pastilha de vidro:** nenhum dos oito resultados editoriais dá **espessura máxima de corte
  em mm**. O banco dá, em 4 dos 6 itens de `alicate`, com fonte de nível 2 ou 3. E a página nasce com
  a faixa descoberta que a 7b-bis mediu em 25/09: o torquês de mosaico para em **5 mm** e **3 das 13**
  pastilhas do banco não cabem (6, 8 e 8 mm) — três dos treze produtos cuja quantidade a F1 já calcula
  não têm ferramenta declarada que os corte.
- **Verniz:** nenhum dos nove dá demãos, consumo em ml/m² nem secagem. O banco dá. **E dá a ausência,
  que vale mais:** a 7b-ter mediu que **nenhuma** das sete frases de fabricante de `acabamento` nomeia
  **vidro** e **nenhuma** nomeia **rejunte** — as duas superfícies que a peça pronta expõe.

## DOIS DEFEITOS DO MEU PRÓPRIO INSTRUMENTO, E OS DOIS ESTÃO NO ARQUIVO EM VEZ DE ESCONDIDOS

1. **O canal de busca desta nuvem é dos EUA**, declarado pela própria ferramenta. Uma consulta
   (`cortador de azulejo manual para mosaico`) voltou com SERP **espanhola** — Amazon MX, Leroy ES,
   Bricodepot ES, Home Depot MX. Está marcada **NÃO MEDIDA**, não "consulta sem concorrente
   brasileiro". E daí sai o limite do arquivo inteiro: ele classifica **quem ocupa**, que é o que a
   14.9 pede com essas palavras, e **não afirma posição de ninguém** — posição, nesta ilha, vem do
   Search Console, cujo acesso está pendente.
2. **Eu pus `Vonder` e `Cortag` dentro da consulta**, e ela voltou cheia de página de fabricante. Era
   previsível e o defeito é meu: é a trava de coleta da seção 8 — *"nunca pôr na consulta o valor que
   se quer confirmar"* — aplicada à SERP em vez de ao dado. Também **NÃO MEDIDA**, com o motivo, e
   refeita sem marca. Foi a passada sem marca que achou a consulta aberta.

## E CONTRADIZ O CORPUS DE 10/09 COM TODAS AS LETRAS, EM VEZ DE EM SILÊNCIO

O corpus classificou `pastilhas de vidro para mosaico` como **ABERTA**, com a **mesma** evidência que
esta passada leu como **tomada** (anúncio da Shopee, Bazar Horizonte, Art Glass). A diferença não é de
dado, é de **régua**: o corpus chamou de aberta porque *ninguém responde a pergunta técnica*, e a 14.9
manda classificar **quem ocupa** — e quem ocupa é marketplace, que é o primeiro galho dela, o do "a
página NÃO nasce agora". As duas leituras cabem na mesma SERP, e **a 14.9 é a que decide se a página
nasce**. Está escrito no arquivo, com a instrução de quem for mexer no corpus ler aquele parágrafo
primeiro: o que está velho lá é o **rótulo** daquela linha, não a evidência.

## A TABELA DO `ARVORE.md` DIZIA ZERO EM DUAS CATEGORIAS QUE SAÍRAM DE ZERO HÁ CINCO DIAS

A seção 2 do `ARVORE.md` trazia `0` em `Alicates e corte` e em `Acabamento`. As duas saíram de zero em
**25/09** — 6 e 7 itens —, e **as próprias seções 7b-bis e 7b-ter do mesmo arquivo registram isso três
telas abaixo**. É a seção 4 do contrato dentro de um documento que já tinha a correção escrita: em
prosa, e não na tabela que se lê primeiro.

Corrigida, com coluna nova (`tipos que passam o portão da 9`) para a tabela parar de responder a
pergunta errada — **banco não é filha**, e era o número do banco que ela mostrava ao lado de uma coluna
chamada "existe".

**E aqui eu cometi, e consertei, o defeito que esta ilha mais nomeia:** escrevi que as colunas eram
*"derivadas de `dados/filhas-do-guia.json`"* **tendo digitado os números à mão** — número de tela que
parece conferido. Agora `--conferir` confere a tabela contra a derivação, **nas duas direções**: cada
linha tem de bater no número de banco e na forma `N de M`, e **toda categoria do vocabulário com nível
2 tem de ter linha**. Slug fora da ponte é ignorado de propósito, porque a tabela tem linhas que não
são categoria de banco (`/materiais/como-sabemos/`) e reprovar por elas faria o portão brigar com o
documento certo.

## TRÊS DEFEITOS DA PRÓPRIA FERRAMENTA, OS TRÊS ACHADOS POR ELA RODANDO E OS TRÊS ANTES DO COMMIT

1. **Um `motivo` contava a lista errada:** dizia *"os 7 itens sustentam recomendação"* para a `cola`,
   onde **3** sustentam — ele imprimia o total do banco no lugar da contagem de lastro. Frase de
   diagnóstico com o número errado é pior que frase ausente: ela é o que a próxima execução cita.
2. **"Pode fechar completando registro existente" prometia uma coleta e eram seis.** Para a `cola`,
   dizia que faltava `tempo_de_ajuste` em **6 registros que já moram no banco** — verdade literal que
   se lê como um campo a preencher, quando a propriedade era declarada por **um** item só. Número que
   existe num registro só não está *perto* de ser número da página: ele ainda tem de ser
   **construído**, e construir não é completar. A promessa passou a valer só a **um** registro de
   distância, e sobrou exatamente um caso no banco real — o do Rejunte Piscinas.
3. **O gerador não era idempotente.** O trecho preservado chegava com a quebra de linha que o separava
   da fronteira, e `A("")` punha outra: o arquivo ganhava **uma linha vazia por passada** e
   `--conferir` reprovava o arquivo que a passada anterior havia escrito. Achado porque eu rodei
   `--conferir` depois de gerar, e não porque eu o li. **Gerador que não é idempotente é gerador que
   não fecha com a própria derivação** — e o caso 18 do autoteste agora gera três vezes e compara.

## UM CAMPO OBRIGATÓRIO FALTAVA NO CABEÇALHO DESTA ILHA, E A SEÇÃO 1 LÊ ESSE CAMPO

Ao fechar o cabeçalho, `bloqueada_por` **não existia** nele — e a seção 2 do contrato o exige desde que
ela existe. Conferido que já faltava antes desta execução (`git show HEAD`), e medido nos **seis**
`ESTADO.md` do repositório, o `_modelo` incluído: **os seis parseiam** em `yaml.safe_load` e **dois
estavam incompletos** — esta ilha sem `bloqueada_por`, a `ohmetria` sem `bloqueada_por` **e** sem
`ultima_ronda`. O molde está certo desde 21/09; as ilhas nascidas antes dele não foram acertadas.

**Por que isso é a seção 1 lendo a si mesma errada:** o passo 3 manda descartar ilha *"com
`bloqueada_por` preenchido"*. Com o campo **ausente**, `grep` e olho concluem "não está preenchido" e
acertam por acidente; um parser com `d["bloqueada_por"]` **morre**; e `d.get()` trata ausência como
`null` sem nunca dizer que o campo não existe. As três leituras concordam **hoje** porque o valor certo
é mesmo `null`, e discordam no primeiro dia em que uma ilha for bloqueada de verdade. **Campo ausente
que se comporta como o valor certo é a forma mais paciente de defeito: ele espera o dia em que o valor
certo muda.**

Consertado **nesta ilha** e escrito no contrato: a régua da seção 2, que desde 13/09 conferia se o
cabeçalho **parseia**, passa a conferir **presença** na mesma linha. **Não toquei na `ohmetria`** —
reserva é por ilha, e consertar cabeçalho de ilha que não se reservou é a colisão que a seção 1 existe
para impedir. O defeito dela está nomeado no contrato para a próxima execução que a reservar não
precisar redescobri-lo.

## O QUE ESTE BLOCO NÃO FEZ, DE PROPÓSITO

- **Não criou nenhuma URL, e não podia:** a 16.5 exige 3 filhas por categoria e nenhuma categoria tem
  3. Duas filhas abertas não são três.
- **Não coletou nenhum SKU.** A coleta das 3 de `acabamento` é o bloco seguinte, e a seção 13 proíbe
  empilhar dois blocos numa passada sem a verificação inteira de cada um.
- **Não tocou em `<title>` nem em `description`** de nenhuma das 17 URLs. O BLOCO A espera o número de
  30/09 por ordem escrita do Raphael, e a janela segue limpa.
- **Não escreveu volume de busca que não mediu:** `verniz` **não existe** em `dados/corpus-buscas.md`,
  então a filha de SERP mais aberta da ilha é a que **não tem faixa de volume**. A 14.9 exige o
  cruzamento de intenção com chance; a intenção é clara (é produto que a artesã compra) e o volume está
  escrito como **desconhecido**, nunca estimado.
- **Não afrouxou nenhuma régua** para o banco de hoje passar. Onde a régua mordeu, o conserto foi na
  régua ou na frase — nunca no limiar.

## BANCADA DESTA EXECUÇÃO

`filhas-do-guia.py --autoteste`: **27 casos fabricados, 0 falha** — 19 sobre a medição (entre eles o
teto lido do esquema nas duas direções, fonte órfã, valor nulo, registro inativo, e a distância que
conta o maior buraco e não a soma), **5 jeitos diferentes de reprovar uma tabela de `ARVORE.md`
fabricada** mais os 2 que ela tem de aprovar, e a idempotência em três passadas. `--conferir`:
**aprovado**, e roda duas vezes seguidas sem reprovar o próprio arquivo.

`validar-banco.py` verde (38 materiais, escada **1:1 · 2:5 · 3:15 · 4:17**, soma 38).
`cobertura.py --conferir` OK. `mutacoes-arvore.py` **29 de 29 reprovadas**. Casca **591**, Loja
**208**, F1 **200**, F2 **119**, Técnicas **123**, Ateliê, Leads e Prestação aprovados — **zero
falha**. `conferir-no-ar.py` **519 afirmações, 0 falha**, antes e depois do desembarque.

## DESEMBARQUE E VERIFICAÇÃO NO AR

Push aceito na **primeira tentativa** (`307dcd1..b2e39c0`). Sync acionado **depois** do push, porque
ele lê o `manifest.json` do `main` pelo `raw.githubusercontent` e disparo anterior ao push leria a
revisão 51 — é a forma de "commit sem Sync não é entrega" da seção 20 com a ordem invertida. **Sync na
revisão 52** às 13h43:41, 14 aplicados e 11 aguardando desembarque, e `/status` devolvendo **52**,
igual à do manifest. Os dois arquivos novos de `dados/` nascem com `publicar: false` e por isso estão
entre os que aguardam — eles são medição, não conteúdo de página.

**E no ar depois do desembarque: `conferir-no-ar.py` com 519 afirmações e 0 falha**, medido antes e
depois. O único vermelho da borda continua sendo o soft 404 do hospedeiro, com dono escrito.

**A memória da ilha não foi atualizada porque ela não existe neste ambiente:** `/areas/` não está
montado, conferido nesta execução. O `PROMPT.md` desta ilha já prevê isto com estas palavras — *"Sem
memória, não pare: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta"* — e é onde
o próximo passo ficou escrito.

- **Próximo passo desbloqueado, e desta vez ele é da FUNDAÇÃO e não de ninguém de fora:** coletar **1
  impermeabilizante e 2 seladores** fecha as **3 filhas de `acabamento`**, que é a categoria mais
  barata do Guia, e é o que abre a primeira mãe de nível 2 desta ilha — o **4c**, parado desde 12/09.
  **Confirmado alcançável nesta passada**, e não presumido: selador com rendimento em m²/demão, número
  de demãos e tempo de secagem declarados existe em página de fabricante. **E o resultado reproduziu o
  achado da 7b-ter antes de eu coletar nada:** o selador do Coral nomeia reboco, bloco, concreto, gesso
  e fibrocimento e **não nomeia MDF** — a base mais comum da peça do ateliê. Quem coletar decide antes
  se selador de alvenaria cabe em `regras_da_categoria_acabamento`, que é decisão de esquema e não de
  coleta. **O que continua fora do alcance daqui:** a leitura de 30/09 (acesso do `sentinela@` ou
  `GOOGLE_SA_B64`), que trava o BLOCO A e a faixa de `description` das quatro páginas, e o **curinga**
  de egresso, que trava `base` e `apoio`. Os dois estão na lista do Raphael e nenhum dos dois é
  pré-requisito do passo acima.
