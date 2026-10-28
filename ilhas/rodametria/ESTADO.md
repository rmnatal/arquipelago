---
ilha: rodametria
estado: nascendo
prioridade: 1
piso: abaixo
primeira_indexacao: null
ultima_execucao: 2026-10-28T16:40Z   # BLOCO 3 ENTREGUE: o MODELO DO BANCO — `dados/esquema-banco.json` (versao 1, tres entidades, escada de oito niveis), 24 registros (17 veiculos, 3 pecas, 4 municipios), `validar-banco.py`, `derivar-banco.py`, `mutacoes-banco.py` (66 casos, 0 falha) e `bancada.py`. O ACHADO E UM NUMERO: ZERO veiculo com potencia nominal declarada contra 14 com um watt SEM ROTULO — a F1 fica sem entrada mesmo com os limiares na mao. No caminho, DOIS defeitos: a tabela 1.6 da especificacao chama de "W nominal" uma coluna que nenhuma fonte rotulou (errata), e o PIVO da F1 nasceu `null` em dois registros, pego pela primeira rodada do proprio validador. A HORA SAIU DO `date -u` NA MESMA LINHA DE COMANDO QUE A GRAVA, nunca digitada.
executando_desde: null   # limpo as 2026-10-28T16:40Z pela propria execucao que reservou as 16h19Z de 28/10 (commit 4a14f00). Reserva NAO renovada pela 1.1 porque o bloco nao passou de 40 minutos entre a reserva e o primeiro commit de trabalho.
bloco_atual: |
  BLOCO 3 ENTREGUE — O MODELO DO BANCO, com portao e bateria no mesmo bloco. `esquema-banco.json`
  versao 1: entidades VEICULO, PECA e MUNICIPIO, escada de fontes de OITO niveis, divergencia que
  resolve para o lado RESTRITIVO (oposto da Aquametria, mesma direcao da Robometria — o erro caro
  aqui e o permissivo), e os grupos de prestacao de contas das tres ferramentas conferidos como
  INVARIANTE e nao como intencao. 24 registros, montados SO do que ja estava colhido no
  repositorio: nenhuma rede tocada para monta-los, nenhum numero digitado de cabeca.
  NADA FOI AO AR E NADA PODIA: zero registro `publicavel`, e a causa e uma so e esta em cada
  `motivo_do_status` — ninguem tem saida de compra, e a 25.2 nao admite publicavel sem piso. O
  `manifest.json` segue na revisao 1 com os tres grupos vazios. Canal conferido mesmo assim:
  /status em revisao 1, igual ao manifest, `ultimo` as 16:13:31 e ZERO linha de FALHA depois das
  13h40 — o cron de 30 min esta vivo e o canal esta sao (20.5: revisao igual com log de agora e o
  estado certo, nao cache).
  BANCADA 0 FALHA: validar-banco APROVADO, derivar-banco --conferir APROVADO (todo energia_wh bate
  com V x Ah), mutacoes-banco APROVADO com 66 casos — 4 mundos que TEM de passar (o banco de hoje,
  o banco VAZIO, um publicavel completo no degrau 3 com par colhido, um no degrau 4 com url vazia),
  62 quebras cada uma declarando a frase que espera ouvir, e o AUTOTESTE da propria bateria (um
  validador que aprova tudo tem de faze-la reprovar). SETE das 62 sao MORTES DO ESQUEMA pela 26.2:
  apagam chave DO ESQUEMA e exigem que o portao MORRA, nunca que aprove calado. A mais instrutiva e
  a da sentinela — sem `valor_sentinela_de_ausencia` o banco de HOJE reprova, o que prova que
  aquela linha sustenta peso. E a bancada tem regua propria, medida no dia em que nasceu: denunciou
  um portao inerte de mentira e um arquivo sem convencao de nome.
  O ACHADO DO BLOCO E UM NUMERO, e ele vale mais que o esquema: `veiculos_com_nominal_declarado` =
  0, contra 14 com um watt SEM ROTULO. O PROMPT.md ja dizia a regra ("anuncio que so diz 1000W no
  titulo nao alimenta a F1"); aplicada aos 17 registros ela virou MEDICAO, e a medicao e mais dura:
  NENHUMA das fontes colhidas diz se o watt e nominal ou de pico — nem Extra, nem Casas Bahia, nem
  o painel da Shopee, nem o do Mercado Livre. CONSEQUENCIA: o despacho ALTA de 28/10 destrava a
  FORMULA da F1 e NAO destrava a ENTRADA. O que falta alem da resolucao e a ficha que diz qual dos
  dois watts e o nominal — nivel 4 da escada, hoje VAZIO, porque nenhum dominio de fabricante desta
  ilha foi tentado por execucao nenhuma. E coleta, nao ferramenta, e e o proximo passo mais caro.
  O DADO QUE NAO CABIA, e e a segunda decisao de engenharia: o esquema nasceu com
  `potencia_nominal_w` e `potencia_pico_w` e SUPUNHA que todo watt colhido e um dos dois. Nao e. O
  caso esmagador do varejo e UM WATT SO, SEM ROTULO, e as duas saidas disponiveis mentiriam — jogar
  o numero no nominal classifica pelo anuncio (o que esta ilha existe para nao fazer), descarta-lo
  apaga o unico watt que a fonte declarou. Nasceu `potencia_declarada_sem_rotulo_w`: nunca
  classifica, e e o numero que a tela mostra na ressalva 1.4(a).
  SEVERIDADE DE FONTE E POR CAMPO, PELA ASSIMETRIA DE CUSTO. A primeira escada dizia, como a da
  Robometria, que nivel 6 a 8 nao sustenta campo tecnico NENHUM — e reprovava campo certo: Wh =
  V x Ah e identidade, e o anuncio que escreve "60 V 20 Ah" declara a BATERIA, nao desempenho.
  Errar ali custa uma faixa de km larga; errar na categoria legal manda alguem para a rua sem
  habilitacao. `niveis_minimos_por_campo`: nivel 5 ou melhor nos tres campos da F1 mais
  carga_max_kg; nivel 6 aceito em tensao, amperagem, autonomia, aro, peso e nos watts que nao
  classificam; nivel 8 nao sustenta nada. RESULTADO: F2 e F3 com candidato real no dia um (2 com Wh
  derivado, 3 com carga de ficha) e F1 com zero, cada um pelo SEU motivo, escrito.
  TERCEIRA ENTIDADE QUE A LISTA DO PROMPT.md NAO TINHA: MUNICIPIO. A 1.1 da especificacao da TRES
  estados ao campo `municipio` da F1 e o do meio exige um banco que ninguem mandou existir. Os
  quatro sao `pendente`, e a consequencia esta escrita sem maquiar: HOJE a camada 2 da F1 tem DUAS
  saidas em vez de tres, e as duas imprimem a mesma frase. Pela 20.3 medi os quatro dominios de
  prefeitura (campinas, rio, joinville, sjc): 000 nas TRES passadas, com dois controles em 200 nas
  mesmas tres — 12 bloqueios contra 6 verdes, `connect_rejected` do egresso. MESMA PAREDE do gov.br:
  o que esta ilha nao alcanca nao e um site, e o dominio .gov.br. Despacho NORMAL novo, e a forma
  (a) dele e uma linha so, `*.gov.br`, que fecha os DOIS despachos de hoje.
  PROXIMO PASSO: a coleta em ficha de FABRICANTE, antes da casca — e o primeiro passo dela e a 20.3
  outra vez, medir o egresso contra os dominios dos fabricantes antes de escrever regra que os exija.
ultima_ronda: null
bloqueada_por: null
rede: ok em 2026-10-28   # 20.2 REMEDIDA as 16h19Z pelo bloco 3, nao herdada do campo: `https://rodametria.com.br/` e `/wp-sitemap.xml` os dois em 200 nas TRES passadas. O que NAO passa, MEDIDO AS 16h3xZ pela 20.3 porque este bloco escreveu a regra que exige a fonte: campinas.sp.gov.br, rio.rj.gov.br, joinville.sc.gov.br e sjc.sp.gov.br em 000 nas tres passadas, com rodametria.com.br e aquametria.com.br em 200 nas MESMAS tres (12 bloqueios contra 6 controles verdes, `connect_rejected` = recusa de politica). Somados aos cinco hosts oficiais do despacho ALTA de 28/10 (gov.br, in.gov.br, planalto.gov.br, contran.gov.br, lex.com.br), o bloqueio tem UM nome: o dominio .gov.br. Segue de pe o de 13/10: dspace.ups.edu.ec e stdjet.scienceandtechnology.com.vn em ENOTFOUND | CANAL DE DESEMBARQUE SAO: /status em revisao 1 igual ao manifest, `ultimo` as 16:13:31, zero FALHA depois das 13h40
---

# Estado da ilha RODAMETRIA

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: **`rodametria.com.br` — REGISTRADO E PAGO pelo Raphael em 27/10/2026** (RDAP oficial lido no Chrome dele às 16h41 de Brasília: `status: active`, registro 27/10/2026 19:31Z, expira em 27/10/2028, nameservers ainda `a.auto.dns.br` / `b.auto.dns.br`). Passo 1 da seção 11 cumprido.
- Hospedagem: domínio adicional no mesmo plano da HostGator, raiz própria. **FEITO** — o domínio serve HTML próprio.
- Nameservers `ns604` / `ns605.hostgator.com.br`: **FEITO** — o DNS delegou e o domínio resolve.
- Search Console (propriedade de Domínio): **não medido daqui** (é navegador do Raphael).
- WordPress: **NO AR desde 27/10/2026 às 22h17Z**, medido em 28/10 às 10h17Z pela execução do bloco 1 —
  `https://rodametria.com.br/` devolve 200, `<title>Rodametria - Mobilidade elétrica</title>`, tema de blocos cru,
  **nenhuma página publicada**, `/wp-sitemap.xml` sem URL nenhuma. `/nao-existe-xyz/` devolve 404 de verdade, então
  a porta de entrada da seção 29 está sã nesta primeira leitura.
- Snippet de Sync: `Rodametria Sync`, token novo na hora. **Pendente** — `/wp-json/rodametria/v1/status` devolve 404.
- Lista de Domínios permitidos (seção 20): **FEITO para o domínio da ilha** — o egresso desta nuvem alcança
  `rodametria.com.br`. **Falta `gov.br`**, que é a fonte da F1: despacho ALTA de 28/10 em `dados/despachos.md`.

## O que já foi entregue
- Dossiê, ficha, identidade aprovada (símbolo V9, assinatura H1), `DESIGN.md`, `VOZ.md` e `logo.svg` — 27/10/2026, pela Bússola. Nenhuma URL publicada.
- **BLOCO 1 — `dados/corpus-buscas.md`**, 28/10/2026: quatro eixos, 19 consultas com procedência medida consulta a
  consulta, a **S_par medida** (era a primeira tarefa de leitura que o dossiê deixou) e a contagem do vazamento da
  busca da nuvem **por eixo** (zero fora do Brasil no eixo da regra; quase total no de autonomia e no de peças).
  Nenhuma URL publicada — bloco de dado, `publicar: false`.

## O que está travando
- **A fonte oficial da F1.** O texto da Resolução Contran nº 996/2023 no `gov.br` é **negado pelo egresso desta
  nuvem** (`connect_rejected`, e `ENOTFOUND www.gov.br` na busca de página), medido em 28/10 às 10h4xZ. O bloco 2
  pode ser escrito inteiro, mas a constante central nasce `publicavel: false`. Despacho **ALTA** de 28/10 em
  `dados/despachos.md`. **Isto NÃO é `bloqueada_por`** (seção 11, passo 4): travou uma fonte, não a ilha.
- **A SERP dos eixos de autonomia, carga e peças**, que a busca da nuvem não vê (30.8) — despacho NORMAL de 28/10.
- Os passos 4b a 9 da seção 11 que faltam (Search Console, snippet de Sync, plugins, conta de serviço) são trabalho
  de navegador do Raphael. **O WordPress e o DNS já saíram dessa lista** — ver a Infraestrutura acima.
- Os blocos 2 e 3 não dependem de site, e o 2 é o próximo.
