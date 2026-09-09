# Registro de execucoes — Robometria

Log append-only da Fundacao. Cada execucao escreve aqui o bloco entregue e
o proximo passo desbloqueado, e espelha o mesmo resumo em
`/areas/projeto-robometria.md` na memoria.

## 2026-09-09 — Pasta da ilha criada

- Criada a pasta `ilhas/robometria/` com `snippets/`, `conteudo/`, `dados/`,
  `ferramentas/`, `manifest.json` (revisao 0, nenhum item, nada marcado para
  publicar), `README.md`, `PROMPT.md`, `ESTADO.md` e este registro.
- A pasta nasceu junto com a reorganizacao do Arquipelago em uma unica
  Fundacao com despachante: as regras comuns passaram para o `ARQUIPELAGO.md`
  da raiz e o que e desta ilha ficou no `PROMPT.md` daqui.
- Infraestrutura no dia da criacao: dominio robometria.com.br registrado em
  09/09/2026, dominio adicional ja criado no cPanel da HostGator com raiz
  propria, nameservers ns604 e ns605.hostgator.com.br apontados no
  registro.br. WordPress ainda NAO instalado, aguardando propagacao de DNS;
  snippet de Sync ainda nao existe. Identidade visual aprovada em 09/09/2026.
- **Proximo passo: bloco 1 — levantamento de buscas parametricas** em
  `dados/corpus-buscas.md`, separando o eixo de compatibilidade (peca x
  modelo) do de dimensionamento (Pa, m2, autonomia), com procedencia marcada
  consulta a consulta. Nao depende de site nem de WordPress.

## 2026-09-09 — Bloco 1: corpus de buscas parametricas

- Criado `dados/corpus-buscas.md` (revisao 1 do manifest) com o levantamento
  de buscas do nicho robo aspirador, coletado por busca web em 09/09/2026
  (paginas oficiais de fabricante, marketplaces, foruns, titulos de video).
  Sem acesso a ferramenta de volume de busca nesta coleta — o arquivo registra
  essa limitacao explicitamente em vez de inventar contagem.
- Dois eixos separados, sem mistura em nenhuma ferramenta: **compatibilidade**
  (cluster A1 filtro, A2 escova lateral, A3 mop, A4 bateria) e
  **dimensionamento** (cluster B1 Pa, B2 cobertura em m2, B3 autonomia por
  carga, B4 forum/video de guia de compra geral).
- Achados principais: (1) cada fabricante nomeia a peca pelo codigo do proprio
  modelo e nao existe comparador cross-marca — confirma o buraco que a
  Bussola identificou; (2) um blog do proprio nicho ja alerta contra "filtro
  HEPA universal" por causa de encaixe diferente por modelo — a Robometria
  resolve isso com dado verificado por modelo; (3) Pa recomendado para pet
  diverge entre fontes brasileiras (1.500 a 6.000 Pa, sem consenso) — vira
  ferramenta de faixa com criterio, no mesmo padrao da Aquametria; (4) nenhuma
  fonte publica a formula mAh -> minutos -> m2 com a conta explicita, so
  numero fechado do fabricante — e o vacuo de conteudo que o dimensionador
  (ferramenta b) deve ocupar.
- Lista inicial de modelos/codigos de peca para o Bloco 3 (nenhum dado tecnico
  copiado para banco ainda, precisa reconfirmar na fonte primaria e datar):
  Multilaser HO041/HO400/HO401/HO407/OB010, HO03/HO04, HO011/HO012; Positivo
  PRA500/PRA1000/PRA8000/PRA2000; Xiaomi Mop/Mop 2/Mop 2 Lite/S20/S40/H40;
  iRobot Roomba serie s; Velds RALW-C; WAP W90/W100/W400; Electrolux ERB44.
- `manifest.json` foi para revisao 1: item `corpus-buscas` em `dados`, com
  `publicar: false` (e pesquisa, ainda nao vira pagina) e sha256 conferido.
- **Proximo passo: bloco 2 — especificacao das ferramentas**
  (`dados/especificacao-calculadoras.md` + `dados/constantes.json`), usando os
  dois eixos deste corpus como esqueleto: (a) localizador de peca compativel
  por modelo, (b) dimensionador de succao e autonomia por area, piso e pelo.
  Continua sem depender de WordPress nem de dominio.
