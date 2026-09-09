---
ilha: robometria
estado: nascendo
prioridade: 1
ultima_execucao: 2026-09-09T19:23Z
executando_desde: null
bloco_atual: "3"
bloqueada_por: null
---

# Estado da ilha Robometria

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura

- **Domínio:** robometria.com.br, registrado em 09/09/2026.
- **Hospedagem:** domínio adicional já criado no cPanel da HostGator, com raiz
  própria — mesmo plano da Aquametria, custo extra zero.
- **DNS:** nameservers `ns604.hostgator.com.br` e `ns605.hostgator.com.br`
  apontados no registro.br. Aguardando propagação.
- **WordPress:** ainda **NÃO instalado**. A instalação espera a propagação do
  DNS.
- **Snippet de Sync:** ainda não existe. Enquanto ele não existir, nada desta
  pasta chega a lugar nenhum — o que é esperado, porque não há site.
- **Identidade visual:** aprovada pelo Raphael em 09/09/2026. Paleta, tipografia
  e a geometria do símbolo estão no `PROMPT.md` desta pasta.

Sem credenciais neste arquivo.

## O que já foi entregue

- 09/09/2026 — pasta da ilha criada dentro da reorganização do Arquipélago em
  uma única Fundação com despachante. Nenhum bloco da fila foi executado ainda.
- 09/09/2026 — **Bloco 1 entregue**: `dados/corpus-buscas.md` com o
  levantamento de buscas paramétricas, separado nos eixos compatibilidade
  (filtro, escova lateral, mop, bateria) e dimensionamento (Pa, m², autonomia,
  pelo de pet), procedência marcada consulta a consulta (busca web, página de
  fabricante, marketplace, fórum, YouTube). Sem acesso a ferramenta de volume
  de busca nesta coleta — o arquivo diz isso explicitamente em vez de inventar
  número. Lista inicial de modelos e códigos de peça (Multilaser HO041 e
  variantes, Positivo PRA500/PRA1000/PRA8000/PRA2000, Xiaomi Mop/Mop 2/S20/
  S40/H40, iRobot Roomba série s, Velds RALW-C, WAP W90/W100/W400, Electrolux
  ERB44) fica registrada para o Bloco 3, mas nenhum dado técnico foi copiado
  para banco — precisa reconfirmação na fonte primária antes disso.
- 09/09/2026 — **Bloco 2 entregue**: `dados/especificacao-calculadoras.md` e
  `dados/constantes.json` (manifest na revisão 2). As duas ferramentas âncora
  estão especificadas ponta a ponta — **R1**, localizador de peça compatível
  por modelo, e **R2**, dimensionador de sucção e autonomia — com entrada,
  saída, elegibilidade, tabela de exemplos pré-renderizada, JSON-LD e a
  classificação de SERP da consulta-alvo de cada uma, como manda a seção 14.9
  do contrato. 21 constantes gravadas, cada uma com classe de fonte, URL,
  canal de coleta e data.
- Três decisões de projeto que este bloco fixa: (1) a R1 **nunca infere
  compatibilidade** — cada par peça × modelo sai com um de três selos
  (`declarada_fabricante`, `declarada_terceiro`, `nao_declarada`), e o selo
  aparece na frase; (2) **divergência de compatibilidade resolve pelo conjunto
  MAIS ESTREITO**, ao contrário da regra do banco de espécies da Aquametria,
  que resolve pelo maior — a assimetria de custo decide a direção, porque aqui
  errar para o lado largo faz alguém comprar peça que não encaixa; (3) a R2
  publica **ciclos e tempo real até terminar** a partir de dado declarado, em
  vez de inventar uma taxa de m² por minuto.

## O que este bloco deliberadamente NÃO fez

- **Não criou a taxa de cobertura m²/min.** O banco tem um único par (minutos,
  m²) declarado por fabricante — os 162 m² em até 120 min do Electrolux ERB44.
  Um ponto não é um coeficiente, então a constante entrou com status `pendente`
  e **proibida dentro de fórmula publicada**, por força da seção 10 do
  contrato. Sai de pendente com 5 pares declarados, de marcas diferentes, e
  ainda assim publica faixa com a dispersão à mostra, nunca a média.
- **Quatro números ficaram `nao_publicavel` por atribuição incerta** (a faixa
  de 5.000–10.000 Pa para carpete, o mínimo de 3.000 Pa para piso frio e a vida
  útil da escova lateral): apareceram em resumo agregado de busca sem que desse
  para dizer qual veículo os publica. Número sem autor identificado não vai para
  a tela.
- **O filtro PR550 (HO03/HO04) foi excluído do banco**: é peça de aspirador de
  pó 2 em 1, não de robô. Ficou registrado justamente para a próxima execução
  não recolhê-lo de novo achando que é robô.
- **Correção no corpus do Bloco 1:** `PRA8000` não existe em canal oficial
  nenhum; a linha da Positivo é PRA500, PRA800, PRA1000 e PRA2000. Vale
  `PRA800`, e nenhum dado técnico foi herdado do nome errado.

## O que está travando

Nada. A falta de WordPress **não** é bloqueio: os blocos 1 (feito), 2 (feito) e
3 (modelo do banco) são de pesquisa e modelagem e rodam sem infraestrutura. Por
isso `bloqueada_por` continua `null`.

Nada desta pasta está publicado, e isso é esperado: os três itens do manifest
estão com `publicar: false` porque são pesquisa, e o site ainda não existe. Não
há Sync para acionar nem `/status` para conferir — a seção 4 do contrato passa a
valer nesta ilha quando houver WordPress.

Uma coleta segue em aberto, e não é bloqueio: o egresso HTTP direto está fechado
(`multilaser.com.br` e `manuals.plus` devolveram EGRESS_BLOCKED em 09/09/2026),
então tudo foi colhido por busca restrita ao domínio. A leitura direta das
páginas de peça e dos manuais em PDF é trabalho a fazer, não dependência humana.
