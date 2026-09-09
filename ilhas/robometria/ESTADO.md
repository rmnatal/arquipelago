---
ilha: robometria
estado: nascendo
prioridade: 1
ultima_execucao: 2026-09-09T23:16Z
executando_desde: null
bloco_atual: "3c segunda leva — pa_declarado fora da Electrolux (concluida); banco na revisao 5"
ultima_ronda: null
bloqueada_por: null
---

# Estado da ilha Robometria

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura

- **Domínio:** robometria.com.br, registrado em 09/09/2026.
- **Hospedagem:** domínio adicional já criado no cPanel da HostGator, com raiz
  própria — mesmo plano da Aquametria, custo extra zero.
- **DNS:** nameservers `ns604.hostgator.com.br` e `ns605.hostgator.com.br`
  apontados no registro.br.
- **DNS propagado em 09/09/2026** — o domínio resolve para 108.179.253.218
  (br604-ip04.hostgator.com.br), o mesmo servidor da Aquametria.
- **WordPress: INSTALADO em 09/09/2026, 16h17 BRT**, via Softaculous, em
  https://robometria.com.br, na raiz do domínio. Versão 7.1, idioma pt_BR,
  instalação limpa (nenhum plugin de brinde do Softaculous). Usuário
  administrador não é `admin`. Credenciais foram por e-mail ao Raphael e não
  entram neste arquivo. **Medido no navegador do Raphael pela sessão de
  conversa** — a Fundação estava certa em não escrever isto sem medir.
- **SSL: PENDENTE.** O AutoSSL da HostGator ainda não emitiu certificado; o
  navegador recusa a conexão. O cPanel desta conta não expõe a aba de status
  do AutoSSL, então não há como forçar — ele roda sozinho, tipicamente em
  algumas horas. Enquanto isso o wp-admin não abre (o site nasceu em https),
  e isso trava **só** os passos de navegador: plugins, snippet de Sync,
  Search Console. Há uma checagem automática a cada 40 min que retoma a
  seção 11 do passo 6 em diante assim que o certificado sair.
- **ARMADILHA:** testar TLS pela nuvem não vale — o proxy de saída intercepta
  e apresenta certificado próprio, então a nuvem diz "SSL OK" enquanto o
  Chrome mostra erro. Certificado só se confere no navegador.
- **Snippet de Sync:** ainda não existe. Depende do wp-admin, que depende do
  certificado.
- **Search Console: propriedade de domínio `sc-domain:robometria.com.br` criada e VERIFICADA em 09/09/2026** (TXT `google-site-verification=xvI914rD2M69UhAao_MF2csPC3XAKKSUmol9JU-xxwg` gravado no Editor de Zona DNS; passo 4b da seção 11). Falta só submeter o sitemap, o que depende do wp-admin, que depende do certificado. `dados/indexacao.md` nasce com a primeira medição, que vai ser zero.
- **Identidade visual:** aprovada pelo Raphael em 09/09/2026. Paleta, tipografia
  e a geometria do símbolo estão no `PROMPT.md` desta pasta.

Sem credenciais neste arquivo.

## O que já foi entregue

- 09/09/2026 — pasta da ilha criada dentro da reorganização do Arquipélago em
  uma única Fundação que escolhe a ilha de cada execução (seção 1 do contrato).
- 09/09/2026 — **Bloco 1**: `dados/corpus-buscas.md`, levantamento de buscas
  paramétricas separado nos eixos compatibilidade (filtro, escova lateral, mop,
  bateria) e dimensionamento (Pa, m², autonomia, pelo de pet), com procedência
  marcada consulta a consulta. Sem ferramenta de volume de busca nessa coleta —
  o arquivo diz isso em vez de inventar número.
- 09/09/2026 — **Bloco 2**: `dados/especificacao-calculadoras.md` e
  `dados/constantes.json`. As duas ferramentas âncora especificadas ponta a
  ponta — **R1**, localizador de peça compatível por modelo, e **R2**,
  dimensionador de sucção e autonomia — com entrada, saída, elegibilidade,
  tabela de exemplos pré-renderizada, JSON-LD e classificação de SERP da
  consulta-alvo. 21 constantes, cada uma com classe de fonte, URL, canal de
  coleta e data.
- 09/09/2026 — **Bloco 3c, segunda leva: a R2 deixou de sair vazia.**
  `pa_declarado` passou de **2 para 11 modelos publicáveis**, em 3 marcas, cobrindo de
  **1.400 a 10.000 Pa** numa escala contínua. 33 modelos (eram 24) e 5 marcas (eram 4),
  com a WAP entrando no banco. Esquema na versão 3, manifest na revisão 5,
  `validar-banco.py` APROVADO com três invariantes novas mais a conferência das contagens
  do cabeçalho — e todas foram testadas quebrando o banco de propósito numa cópia.

- 09/09/2026 — **Bloco 3c entregue: o banco saiu do modelo e virou cobertura.**
  24 modelos (eram 17), 18 peças (eram 8) e **33 pares peça × modelo declarados**
  (eram 10). Esquema na versão 2, manifest na revisão 4, `validar-banco.py`
  APROVADO com cinco invariantes novas — e as cinco foram testadas quebrando o
  banco de propósito numa cópia, para provar que reprovam.
- 09/09/2026 — **Bloco 3 entregue: o modelo do banco existe e é verificável.**
  `dados/esquema-banco.json` (contrato das entidades MARCA, MODELO_ROBO, PEÇA e
  COTAÇÃO), `dados/marcas.json` (4), `dados/modelos-robo.json` (17) e
  `dados/pecas.json` (8 peças, **10 pares peça × modelo, todos declarados pelo
  fabricante e nenhum inferido**), mais `ferramentas/validar-banco.py`, que roda
  sem rede e reprova o banco quando alguma invariante do esquema é violada.
  Manifest na revisão 3.

### O que a SEGUNDA LEVA do 3c descobriu, e muda a estratégia inteira

1. **A lacuna de Pa está fechada, e a que sobrou é de OUTRO tipo.** A varredura da faixa
   de entrada da R2 de ponta a ponta (seção 14.3), gravada em `cobertura_de_faixa_r2`,
   mostrou que 5 das 6 faixas passam no portão de 3 itens. Sobraram duas coisas: acima de
   **6.000 Pa** só há 2 elegíveis, e — o achado que só aparece olhando a varredura inteira
   — **toda faixa acima de 3.000 Pa é 100% Xiaomi**, faixa de pet inclusive. Contar
   elegíveis diz que está resolvido; olhar a composição diz que não. Numa ilha que se
   vende como comparador **cross-marca**, a faixa que mais vende não pode ser catálogo de
   uma marca só.
2. **Quem declara sucção alta no Brasil é essencialmente a Xiaomi.** Electrolux e Multi
   não publicam Pa em canal nenhum (as duas declaram *níveis*), e a WAP só publica na
   parte barata da linha: 1.400 Pa no W400, e nada no topo W1000, que declara "três modos
   de sucção". Isso é fato de mercado medido, não impressão — e é conteúdo publicável na
   página de metodologia, porque nenhum comparador diz isso.
3. **A lacuna de m² não é de esforço, é de mercado — e isso vira conteúdo.** Xiaomi, WAP,
   Multi e Positivo foram varridas modelo a modelo e **nenhuma** declara área coberta em
   m². Só a Electrolux declara. Não adianta coletar mais: o número não está publicado. A
   `taxa-cobertura-m2-por-min` segue proibida em fórmula, e a recusa da R2 deixa de ser
   uma pendência envergonhada e passa a ser a resposta: quando um site promete "atende até
   120 m²" para um robô cujo fabricante só declarou minutos, esse número foi inventado
   por alguém.
4. **Divergência de especificação não é só de peça — e o PRA500 provou.** O mesmo canal do
   fabricante declara **1600 Pa na ficha e 2000 Pa no texto de venda da MESMA página**.
   Não há nível mais alto para desempatar, e a média (1800) é a única saída proibida.
   Valeu 1600, porque o erro caro é o do lado alto: publicar 2000 faz alguém comprar um
   robô fraco demais por recomendação nossa. Isso forçou `divergencias[]` e `resolucao` a
   existirem também em `MODELO_ROBO`, na versão 3 do esquema.
5. **Faixa e tolerância declaradas resolvem para o lado caro, nunca para o meio.** O
   fabricante quase nunca dá número: dá "de 5 a 6 horas" ou "130 minutos ±10%". A versão 3
   escreveu a regra por campo — Pa e autonomia para **baixo**, tempo de recarga para
   **cima** — e `declarado_como` guarda a faixa inteira, para a página citar a faixa e não
   o número escolhido.
6. **A WAP é a melhor chance de NÍVEL 2 que a ilha já teve.** É a única marca que publica
   um manual em PDF por modelo, em endereço próprio e estável, com revisão e data no nome
   do arquivo. Hoje `EGRESS_BLOCKED`; no dia em que abrir, sobe o banco inteiro da marca
   de uma vez. A ilha ainda não tem **nenhuma** fonte de nível 2.

### O que o Bloco 3c descobriu, e muda a estratégia de coleta

1. **A Electrolux não publica sucção em Pa. Em canal nenhum.** Loja oficial,
   página de conteúdo, portal de cuidados e canal de parceiros: todos declaram
   **níveis** de sucção (mínimo, médio, máximo), nunca pascal. Veículos
   editoriais citam "4.000 Pa" para a linha, mas pela escada de fontes editorial
   **nunca** sustenta especificação de aparelho — então o número ficou de fora,
   de propósito. **Consequência prática:** `pa_declarado` continua em 2 de 19
   modelos publicáveis, e insistir na Electrolux não vai resolver. O campo tem
   que vir de Xiaomi, Multi, WAP e Positivo. Isso corrige a suposição do bloco
   anterior, que tratava a Electrolux como fonte de maior rendimento.
2. **A Electrolux não vende filtro de robô avulso — vende o Kit Performance.**
   Quem procura "filtro do ERB10" compra o **KPCEL01**. Foi isso que obrigou o
   esquema a ganhar o tipo de peça `kit` com `composicao[]`: sem ele a R1 não
   responderia a própria consulta-alvo. E é o KPCEL01 que finalmente dá dono à
   vida útil de 6 meses do manual, que desde o Bloco 3 era um número sem peça.
3. **A dispersão da cobertura virou conteúdo.** O banco tem agora dois pares
   (minutos, m²) declarados: 162 m² em até 2h no ERB44 (1,35 m²/min) e 166 m² em
   até 1h40 na família ERB60/61/62/80 (1,66 m²/min). São **23% de diferença
   dentro da mesma marca** — e é o melhor argumento de que taxa geral não existe.
   A constante `taxa-cobertura-m2-por-min` **continua proibida em fórmula
   publicada**, agora com dois números do próprio fabricante sustentando o
   porquê. Faltam pares de **marcas diferentes**: são 2 declarações de 1 marca, e
   o critério pede 5 de marcas diferentes.
4. **"Compatibilidade não se herda" apareceu no catálogo do próprio fabricante.**
   O ERB80 está na lista da escova rotativa central e **não** está na do filtro
   HEPA com espuma nem na do Kit Performance do ERB60/61/62. A R1 não pode
   completar lista por analogia, e agora a ilha tem o exemplo para mostrar.
5. **Armadilha da R1, escrita antes de custar caro:** o **PRA500** é literalmente
   a consulta-alvo da especificação, e as três peças novas da Positivo declaram
   **PRA800 e PRA2000**, sem citá-lo. Pelo conjunto mais estreito, a resposta
   certa para o PRA500 é "não encontramos peça declarada". Dizer que serve seria
   exatamente o erro caro desta ilha.

### As três decisões que este bloco fixa

1. **`variante_de_hardware` é campo de primeira classe.** O fabricante vende
   duas baterias diferentes para o **mesmo** código de modelo: a PR10127
   ("Versão A") e a PR8116 ("Mars HO041 versão B"). Saber que o robô é um HO041
   **não basta** para acertar a peça. Consequência escrita na especificação da
   R1: quando o modelo tem mais de uma variante conhecida, a ferramenta mostra
   as duas e explica como a pessoa descobre qual é a dela — devolver uma só
   seria adivinhar, que é o defeito que esta ilha existe para não cometer.
2. **Todo número é `{valor, fonte, declarado_como}`.** Número solto não entra:
   sem a transcrição do texto do fabricante, a página parafraseia em vez de
   citar, e a frase citável com procedência é justamente o que a seção 5 do
   contrato exige. Onde o fabricante não declara, o valor é `null` **com
   motivo** — e o motivo vai para a tela com essas palavras.
3. **Categoria é portão, e o verificador o aplica.** Registro com
   `categoria != robo` não pode ser `publicavel`, e o `validar-banco.py` falha
   se alguém tentar.

## O que este bloco descobriu, e vale dinheiro

- **Pendência do Bloco 2 resolvida:** HO011 e HO012 são aspirador de pó
  **vertical e de mão 2 em 1** (127 V/1000 W e 220 V/700 W, pelos títulos das
  páginas do próprio fabricante), **não** robôs. Logo o filtro PR684 não é peça
  de robô e ficou excluído, com a fonte, para nenhuma execução futura recolhê-lo
  de novo.
- **Quatro modelos novos com categoria confirmada pelo fabricante**: HO407
  (Duster), OB010 (ObaDuster), HO243 (Hydra / Acqua Solution, 90 min declarados)
  e HO411 (Midnight, com lâmina oficial em PDF esperando o egresso abrir).
- **Duas peças novas**: o pano PR10342, que fecha o cluster A3 do corpus (mop),
  que até agora não tinha nenhum item; e a bateria PR8116.
- **Duas divergências resolvidas pelo conjunto mais estreito**, com as duas
  declarações publicadas: o filtro PR10205 (dois canais do fabricante discordam
  sobre o OB010) e a bateria PR8116, cuja divergência está **dentro de uma única
  página** — o título promete "Mars, Moon e Duster" e o endereço da mesma página
  diz "Mars HO041 versão B".
- **O PRA800 tem 2.800 Pa** e portanto fica **abaixo** dos dois limiares que as
  fontes editoriais recomendam para casa com pet (3.000 Pa no Mundo Conectado,
  4.000 Pa no Canaltech). É um caso limpo da regra de elegibilidade da seção 7:
  ele não pode encabeçar a lista de uma consulta com pet.

## O que este bloco deliberadamente NÃO fez

- **Não converteu W em Pa.** O HO041 declara 30 W de potência e nenhum Pa.
  Potência não é sucção e não existe conversão: `pa_declarado` ficou null com
  esse motivo escrito.
- **Não emprestou vida útil de um fabricante para a peça de outro.** O único
  número de fabricante que a ilha tem é o do manual da Electrolux (6 meses para
  o filtro HEPA do ERB10/ERB11/ERB20) e ele vale para **aqueles** modelos. As
  peças da Multi ficaram com `vida_util_declarada` null e motivo.
- **Não coletou nenhuma imagem.** O campo `imagem{}` existe em todo registro,
  com a forma completa e `url` null — o egresso barra os domínios de fabricante
  e de varejo, então não há como baixar nem medir o arquivo. Pela seção 6 do
  contrato, isso **não** elimina o registro da vitrine: ele aparece com espaço
  reservado neutro e o nome em destaque.
- **Não tirou a taxa de cobertura m²/min de `pendente`** — e o Bloco 3c também
  não tirou, de propósito. Os pares declarados passaram de 1 para 2, mas os dois
  são da **mesma marca** e discordam em 23% entre si. O critério pede 5 pares de
  marcas **diferentes**, e continua valendo: publicar a média seria a única saída
  proibida pela seção 10 do contrato.

## O que está travando

Nada que pare a fila. Os blocos 1, 2 e 3 eram de pesquisa e modelagem e estão
entregues; **`bloqueada_por` continua `null`** e continua sendo erro marcar
bloqueio por causa de infraestrutura.

O bloco **3b, casca do site, é o primeiro que depende do WordPress**: ele só
começa quando houver Sync, e o Sync só nasce no wp-admin.

**O trabalho desbloqueado continua sendo 3c, mas o alvo mudou de novo — e desta
vez porque a lacuna anterior fechou.** A R2 não sai mais vazia: `pa_declarado`
está em **11 de 28** modelos publicáveis, em 3 marcas, de 1.400 a 10.000 Pa. O
que sobrou está medido em `cobertura_de_faixa_r2` e é de outra natureza: acima de
**6.000 Pa** só há 2 elegíveis (o portão pede 3), e **toda faixa acima de 3.000
Pa é 100% Xiaomi**. Faixa descoberta continua sendo a única urgência de catálogo
(seção 14.3) — e agora a concentração de marca anda junto dela, porque uma ilha
que promete comparação cross-marca não entrega isso com um catálogo de uma marca
só na faixa que mais vende.

Nada desta pasta está publicado, e isso é esperado: os sete itens do manifest
estão com `publicar: false` porque são pesquisa, e o Sync ainda não existe. A
seção 4 do contrato (o site fica para trás em silêncio) passa a valer nesta ilha
no dia em que o snippet entrar. Itens esperando link de afiliado: **44** (28
modelos e 16 peças) — o campo `afiliado.url` já nasce presente e vazio em todos.
Subiu de 35 para 44 nesta leva, e isso é trabalho pendente de verdade, não
estatística: pela seção 7 do contrato, quem gera link é a Sentinela estratégica,
no navegador do Raphael, com teto de calendário — o cano enche em paralelo e não
compete com a fila da Fundação.

Uma coleta segue em aberto, e não é bloqueio: o egresso HTTP direto está fechado
(`multilaser.com.br`, `suporte.multilaser.com.br`, `lamina.multilaser.com.br`,
`arquivos.multilaser.com.br`, `mi.com`, `manuals.plus`, `loja.electrolux.com.br`,
`content.electrolux.com.br` e, medido nesta execução, também
`www.mi.com`, `loja.wap.ind.br`, `mais.conteudo.wap.ind.br` e
`static.positivocasainteligente.com.br` devolveram EGRESS_BLOCKED em
09/09/2026), então tudo foi colhido por busca restrita ao domínio, com o canal
declarado campo a campo. A leitura direta das páginas de peça, das lâminas e dos
manuais em PDF é trabalho a fazer, não dependência humana — e os manuais da WAP
são o alvo de maior retorno, porque são a única chance de NÍVEL 2 que a ilha tem
hoje. A ilha inteira está em nível 3 e 4: **nenhuma fonte de nível 2 ainda.**
