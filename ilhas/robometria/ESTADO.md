---
ilha: robometria
estado: nascendo
prioridade: 1
ultima_execucao: 2026-09-09T19:38Z
executando_desde: 2026-09-09T21:16Z
bloco_atual: "3c"
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
- 09/09/2026 — **Bloco 3 entregue: o modelo do banco existe e é verificável.**
  `dados/esquema-banco.json` (contrato das entidades MARCA, MODELO_ROBO, PEÇA e
  COTAÇÃO), `dados/marcas.json` (4), `dados/modelos-robo.json` (17) e
  `dados/pecas.json` (8 peças, **10 pares peça × modelo, todos declarados pelo
  fabricante e nenhum inferido**), mais `ferramentas/validar-banco.py`, que roda
  sem rede e reprova o banco quando alguma invariante do esquema é violada.
  Manifest na revisão 3.

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
- **Não tirou a taxa de cobertura m²/min de `pendente`.** Continua havendo um
  único par (minutos, m²) declarado por fabricante — os 162 m² em até 120 min do
  ERB44. Faltam pelo menos quatro pares, de marcas diferentes.

## O que está travando

Nada que pare a fila. Os blocos 1, 2 e 3 eram de pesquisa e modelagem e estão
entregues; **`bloqueada_por` continua `null`** e continua sendo erro marcar
bloqueio por causa de infraestrutura.

O bloco **3b, casca do site, é o primeiro que depende do WordPress**: ele só
começa quando houver Sync, e o Sync só nasce no wp-admin. Enquanto isso, o
trabalho desbloqueado é **3c — expandir o banco**, e ele vem antes do bloco 6
(prospecção do widget) por um motivo medido, não por gosto: hoje só **dois**
modelos do banco têm `pa_declarado`, então a lista de recomendados da R2 sairia
praticamente vazia em qualquer entrada. Faixa descoberta é a única urgência de
catálogo (seção 14.3), e número redondo de itens não é critério.

Nada desta pasta está publicado, e isso é esperado: os sete itens do manifest
estão com `publicar: false` porque são pesquisa, e o Sync ainda não existe. A
seção 4 do contrato (o site fica para trás em silêncio) passa a valer nesta ilha
no dia em que o snippet entrar. Itens esperando link de afiliado: **18** (12
modelos e 6 peças) — o campo `afiliado.url` já nasce presente e vazio em todos.

Uma coleta segue em aberto, e não é bloqueio: o egresso HTTP direto está fechado
(`multilaser.com.br`, `suporte.multilaser.com.br`, `lamina.multilaser.com.br`,
`arquivos.multilaser.com.br`, `mi.com` e `manuals.plus` devolveram
EGRESS_BLOCKED em 09/09/2026), então tudo foi colhido por busca restrita ao
domínio, com o canal declarado campo a campo. A leitura direta das páginas de
peça, das lâminas e dos manuais em PDF é trabalho a fazer, não dependência
humana.
