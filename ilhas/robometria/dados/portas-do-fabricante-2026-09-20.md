# AS PORTAS DO FABRICANTE — medicao de 2026-09-20

Gerada por `ferramentas/medir-portas-do-fabricante.py`, para o **despacho do
Raphael de 19/09/2026** (foto do fabricante para os publicaveis sem imagem).
**Nenhum numero desta pagina foi digitado:** os registros saem dos dois arquivos
de banco, as portas saem de `fontes{}.url` e `canal_brasileiro.valor` de cada
registro, a especie de cada porta sai de `dados/marcas.json`, e o estado de cada
host sai de uma consulta de DNS mais um `curl`, host a host.

## O placar

| | |
|---|---|
| publicaveis sem foto (o alvo do despacho) | **66** |
| registros com ao menos uma porta gravada no banco | 66 |
| hosts distintos que essas portas usam | 14 |
| registros em "bloqueado por rede" | **64** |
| registros em "porta nao declarada em marcas.json" | **1** |
| registros em "so porta de terceiro — 25.3 proibe" | **1** |

## Os hosts, um a um

| host | DNS | HTTP | veredito | registros que dependem dele |
|---|---|---|---|---|
| `www.mi.com` | resolve | 000 | bloqueado por rede | 26 |
| `loja.electrolux.com.br` | resolve | 000 | bloqueado por rede | 8 |
| `br.roborock.com` | resolve | 000 | bloqueado por rede | 6 |
| `www.multilaser.com.br` | resolve | 000 | bloqueado por rede | 6 |
| `us.roborock.com` | resolve | 000 | bloqueado por rede | 5 |
| `loja.wap.ind.br` | resolve | 000 | bloqueado por rede | 4 |
| `www.multilaserempresas.com.br` | resolve | 000 | bloqueado por rede | 4 |
| `manuals.plus` | resolve | 000 | bloqueado por rede | 3 |
| `www.positivocasainteligente.com.br` | resolve | 000 | bloqueado por rede | 3 |
| `loja.meupositivo.com.br` | resolve | 000 | bloqueado por rede | 2 |
| `suporte.multilaser.com.br` | resolve | 000 | bloqueado por rede | 2 |
| `blog.wap.ind.br` | resolve | 000 | bloqueado por rede | 1 |
| `content.electrolux.com.br` | resolve | 000 | bloqueado por rede | 1 |
| `lamina.multilaser.com.br` | resolve | 000 | bloqueado por rede | 1 |

## A lista de 17/09 contra as portas que o banco usa

O despacho de 17/09/2026 registra cinco hosts abertos na lista de dominios
permitidos do ambiente. Esta secao compara aquela lista com os hosts que as
paginas dos 66 registros realmente usam — e a diferenca nao e detalhe:
pagina de produto raramente mora no `www` institucional da marca.

| | |
|---|---|
| hosts da lista de 17/09 | 5 |
| desses, usados por alguma porta dos 66 | 2 |
| hosts usados pelas portas que NUNCA estiveram na lista | **11** |

**32 dos 66 registros nao tem NENHUMA porta na lista de 17/09** — para eles,
a lista daquele dia, mesmo intacta, nunca teria bastado.

| host que falta abrir | registros que dependem dele |
|---|---|
| `loja.electrolux.com.br` | 8 |
| `br.roborock.com` | 6 |
| `us.roborock.com` | 5 |
| `loja.wap.ind.br` | 4 |
| `www.multilaserempresas.com.br` | 4 |
| `www.positivocasainteligente.com.br` | 3 |
| `loja.meupositivo.com.br` | 2 |
| `suporte.multilaser.com.br` | 2 |
| `blog.wap.ind.br` | 1 |
| `content.electrolux.com.br` | 1 |
| `lamina.multilaser.com.br` | 1 |

Na lista de 17/09 e sem uso por porta nenhuma dos 66: `mais.conteudo.wap.ind.br`, `www.electrolux.com.br`, `www.positivotecnologia.com.br`.

**Fora da lista de abrir, de proposito:** `manuals.plus`. Sao paginas de TERCEIRO
(manual hospedado por agregador), e a 25.3 proibe a foto que viria de la.
Abrir esses hosts nao move o despacho um registro.

## O residuo, registro a registro

| registro | marca | tipo | veredito | porta |
|---|---|---|---|---|
| `electrolux-erb10` | electrolux | robo | bloqueado por rede | https://loja.electrolux.com.br/robo-apirador-de-po-electrolux-home-e-speed-experience-com-autonomous-technology-erb10/p |
| `electrolux-erb11` | electrolux | robo | bloqueado por rede | https://loja.electrolux.com.br/robo-apirador-de-po-electrolux-home-e-speed-experience-com-autonomous-technology-erb11/p |
| `electrolux-erb20` | electrolux | robo | so porta de terceiro — 25.3 proibe | https://manuals.plus/m/a7d2cf5766298ebb7449842933ed52fe8a527804e53e3684a681bae94bdf7a78 |
| `electrolux-erb30` | electrolux | robo | bloqueado por rede | https://loja.electrolux.com.br/robo-apirador-de-po-electrolux-home-e-power-experience-com-autonomous-technology--erb30-/p |
| `electrolux-escova-rotativa-central-erb60-erb61-erb62-erb80` | electrolux | escova principal | bloqueado por rede | https://loja.electrolux.com.br/escova-rotativa-central-electrolux-para-robos-aspiradores-erb60--erb61--erb62-e-erb80/p |
| `electrolux-filtro-hepa-espuma-erb44-erb60-erb61-erb62` | electrolux | filtro | bloqueado por rede | https://loja.electrolux.com.br/filtro-hepa-com-espuma-electrolux-para-robos-aspiradores-erb44--erb60--erb61-e-erb62/p |
| `electrolux-kit-performance-erb44` | electrolux | kit | bloqueado por rede | https://loja.electrolux.com.br/kit-performance-electrolux-para-robo-aspirador-erb44/p |
| `electrolux-kit-performance-erb60-erb61-erb62` | electrolux | kit | bloqueado por rede | https://loja.electrolux.com.br/kit-performance-electrolux-para-robos-aspiradores-erb60--erb61-e-erb62/p |
| `electrolux-pano-microfibra-erb60-erb61-erb62-erb80` | electrolux | mop | bloqueado por rede | https://loja.electrolux.com.br/pano-de-microfibra-electrolux-para-robos-aspiradores-erb60--erb61--erb62-e-erb80/p |
| `multi-ho041` | multi | robo | bloqueado por rede | https://www.multilaserempresas.com.br/produto/eletroportateis-para-sua-casa/lar/aspiradores/aspirador-de-po-robo-mars-varre-+-aspira-+-passa-pano-bivolt-com-30w-e-bateria-recarregavel--vermelhopreto-multi--ho041/HO041/ |
| `multi-ho243` | multi | robo | bloqueado por rede | https://suporte.multilaser.com.br/produtos/aspirador-robo-acqua-solution-ho243/duvidas-frequentes |
| `multi-ho400` | multi | robo | bloqueado por rede | https://www.multilaserempresas.com.br/produto/eletroportateis-para-sua-casa/lar/aspiradores/aspirador-de-po-robo-mars-varre--aspira-e-passa-pano-bivolt-e-bateria-recarregavel-multi-home--ho400/HO400/ |
| `multi-ho407` | multi | robo | bloqueado por rede | https://www.multilaser.com.br/aspirador-robo-3-em-1-varre-aspira-e-passa-pano-duster-multi-ho407out/p |
| `multi-ho411` | multi | robo | bloqueado por rede | https://lamina.multilaser.com.br/ho411.pdf |
| `multi-ob010` | multi | robo | bloqueado por rede | https://www.multilaserempresas.com.br/produto/eletroportateis-para-sua-casa/lar/aspiradores/aspirador-robo-3-em-1-varre--aspira-e-passa-pano-obaduster-obabox--ob010/OB010/ |
| `multi-pr10124` | multi | escova lateral | bloqueado por rede | https://www.multilaser.com.br/escova-lateral-para-aspirador-robo-ho041-e-ob010/p |
| `multi-pr10127` | multi | bateria | bloqueado por rede | https://www.multilaser.com.br/bateria-p-aspirador-robo-ho041-versao-a-pr10127/p |
| `multi-pr10342` | multi | mop | bloqueado por rede | https://www.multilaser.com.br/pano-para-aspirador-robo-ob010/p |
| `multi-pr10343` | multi | filtro | bloqueado por rede | https://www.multilaser.com.br/filtro-para-aspirador-robo-ob010-pr10343/p |
| `multi-pr8116` | multi | bateria | bloqueado por rede | https://www.multilaserempresas.com.br/produto/eletroportateis-para-sua-casa/lar/aspiradores/bateria-para-aspirador-robo-mars-ho041-versao-b--pr8116/PR8116/ |
| `positivo-11206519` | positivo | escova principal | bloqueado por rede | https://www.positivocasainteligente.com.br/escova-central-para-smart-robo-aspirador-laser-pra800-e-autolimpante-pra2000-11206519/p |
| `positivo-11206540` | positivo | mop | porta nao declarada em marcas.json | https://loja.meupositivo.com.br/mop-para-smart-robo-aspirador-laser-pra800-e-autolimpante-pra2000-11206540/p |
| `positivo-pra2000` | positivo | robo | bloqueado por rede | https://www.positivocasainteligente.com.br/smart-robo-aspirador-wifi-autolimpante-pra2000-positivo-casa-inteligente-11206197/p |
| `positivo-pra500` | positivo | robo | bloqueado por rede | https://www.positivocasainteligente.com.br/exclusivo-smart-robo-aspirador-wi-fi-plus/p |
| `roborock-mop-q8-max` | roborock | mop | bloqueado por rede | https://us.roborock.com/products/mop-cloth-2pcs-for-roborock-q7-series-s6-series-s5-series-e-series |
| `roborock-mop-qrevo-curv` | roborock | mop | bloqueado por rede | https://us.roborock.com/products/roborock-mop-cloth-4pcs-for-qrevo-curv-and-qrevo-edge |
| `roborock-mop-qrevo-master` | roborock | mop | bloqueado por rede | https://us.roborock.com/products/roborock-mop-cloth-4pcs-for-q-revo |
| `roborock-mop-s8-maxv-ultra` | roborock | mop | bloqueado por rede | https://us.roborock.com/products/roborock-edgewise-mop-cloth-2pcs-for-s8-maxv-ultra-s8-max-ultra |
| `roborock-mop-saros-10r-z70` | roborock | mop | bloqueado por rede | https://us.roborock.com/products/roborock-mop-cloth-4pcs-for-saros-10r-and-saros-z70 |
| `roborock-q8-max` | roborock | robo | bloqueado por rede | https://br.roborock.com/pages/q8-max-plus |
| `roborock-qrevo-curv` | roborock | robo | bloqueado por rede | https://br.roborock.com/pages/roborock-qrevo-curv-series |
| `roborock-qrevo-master` | roborock | robo | bloqueado por rede | https://br.roborock.com/pages/roborock-qrevo-master |
| `roborock-s8-maxv-ultra` | roborock | robo | bloqueado por rede | https://br.roborock.com/pages/s8-maxv-ultra |
| `roborock-saros-10r` | roborock | robo | bloqueado por rede | https://br.roborock.com/pages/roborock-saros-10r |
| `roborock-saros-z70` | roborock | robo | bloqueado por rede | https://br.roborock.com/pages/roborock-saros-z70 |
| `wap-escova-direita-w300` | wap | escova lateral | bloqueado por rede | https://loja.wap.ind.br/escova-direita-para-robo-aspirador-de-po-wap-robot-w300/p |
| `wap-escova-esquerda-w300` | wap | escova lateral | bloqueado por rede | https://loja.wap.ind.br/escova-esquerda-para-robo-aspirador-de-po-wap-robot-w300/p |
| `wap-escova-frontal-wsmart` | wap | escova lateral | bloqueado por rede | https://loja.wap.ind.br/escova-frontal-para-robo-aspirador-de-po-wap-robot-wsmart/p |
| `wap-w300` | wap | robo | bloqueado por rede | https://loja.wap.ind.br/robo-aspirador-de-po-wap-robot-w300/p |
| `wap-wsmart` | wap | robo | bloqueado por rede | https://blog.wap.ind.br/lancamento-robo-aspirador-wap-robot-wsmart/ |
| `xiaomi-b106gl-bx` | xiaomi | escova lateral | bloqueado por rede | https://www.mi.com/global/product/xiaomi-robot-vacuum-s20-accessories/specs/ |
| `xiaomi-b106gl-lw` | xiaomi | filtro | bloqueado por rede | https://www.mi.com/sg/product/xiaomi-robot-vacuum-s10-accessories/specs/ |
| `xiaomi-b106gl-zx` | xiaomi | escova principal | bloqueado por rede | https://www.mi.com/sg/product/xiaomi-robot-vacuum-s10-accessories/specs/ |
| `xiaomi-d106-tb` | xiaomi | mop | bloqueado por rede | https://www.mi.com/global/product/xiaomi-robot-vacuum-s20-accessories/specs/ |
| `xiaomi-e10` | xiaomi | robo | bloqueado por rede | https://www.mi.com/br/product/xiaomi-robot-vacuum-e10/specs/ |
| `xiaomi-e10c` | xiaomi | robo | bloqueado por rede | https://www.mi.com/global/product/xiaomi-robot-vacuum-e10c/specs/ |
| `xiaomi-e12` | xiaomi | robo | bloqueado por rede | https://www.mi.com/es/product/xiaomi-robot-vacuum-e12/specs/ |
| `xiaomi-escova-lateral-mop-2` | xiaomi | escova lateral | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11406/ |
| `xiaomi-escova-lateral-mop-2-lite` | xiaomi | escova lateral | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11405/ |
| `xiaomi-escova-principal-h40-s40` | xiaomi | escova principal | bloqueado por rede | https://www.mi.com/global/product/xiaomi-robot-vacuum-h40-and-s40-brush/ |
| `xiaomi-escova-principal-mop-2` | xiaomi | escova principal | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11406/ |
| `xiaomi-escova-principal-mop-2-lite` | xiaomi | escova principal | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11405/ |
| `xiaomi-filtro-mop-2` | xiaomi | filtro | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11406/ |
| `xiaomi-filtro-mop-2-lite` | xiaomi | filtro | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11405/ |
| `xiaomi-mop-2` | xiaomi | robo | bloqueado por rede | https://www.mi.com/br/product/mi-robot-vacuum-mop-2/ |
| `xiaomi-mop-2-lite` | xiaomi | robo | bloqueado por rede | https://www.mi.com/br/product/mi-robot-vacuum-mop-2-lite/ |
| `xiaomi-mop-mop-2` | xiaomi | mop | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11406/ |
| `xiaomi-mop-mop-2-lite` | xiaomi | mop | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11405/ |
| `xiaomi-mop-s10` | xiaomi | mop | bloqueado por rede | https://www.mi.com/sg/product/xiaomi-robot-vacuum-s10-accessories/specs/ |
| `xiaomi-reservatorio-mop-2` | xiaomi | reservatorio | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11406/ |
| `xiaomi-reservatorio-mop-2-lite` | xiaomi | reservatorio | bloqueado por rede | https://www.mi.com/global/support/faq/details/KA-11405/ |
| `xiaomi-s10` | xiaomi | robo | bloqueado por rede | https://www.mi.com/br/product/xiaomi-robot-vacuum-s10/specs/ |
| `xiaomi-s12` | xiaomi | robo | bloqueado por rede | https://www.mi.com/es/product/xiaomi-robot-vacuum-s12/specs/ |
| `xiaomi-s20` | xiaomi | robo | bloqueado por rede | https://www.mi.com/br/product/xiaomi-robot-vacuum-s20/specs/ |
| `xiaomi-s40-pro` | xiaomi | robo | bloqueado por rede | https://www.mi.com/global/product/xiaomi-robot-vacuum-s40-pro/specs/ |
| `xiaomi-x20` | xiaomi | robo | bloqueado por rede | https://www.mi.com/global/product/xiaomi-robot-vacuum-x20/specs/ |

