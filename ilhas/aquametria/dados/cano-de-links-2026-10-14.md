# Cano de links — contagem de 2026-10-14

Contado por `ferramentas/contar-cano-de-links.py` sobre os quatro `dados/produtos-*.json` deste repositório. **Nenhuma rede foi aberta e nenhum link foi testado** — teste de vida é outro portão (seção 25.4 do `ARQUIPELAGO.md`). Fecha o item 3 do despacho da Sentinela de 07/10/2026, que pedia um arquivo datado com quatro números contados em vez dos números de 02 e 05/10 repetidos.

## Os quatro números que o despacho pediu

| o que | quantos |
|---|---|
| registros nos quatro bancos de produto (o que esta ilha chama de publicável) | **78** |
| sem `afiliado.url_busca` — o piso da 25.2, que nunca depende de ninguém | **0** |
| sem `afiliado.url_produto` — a ficha, o degrau que paga comissão | **42** |

**Distribuição por `afiliado.degrau`:**

| degrau | quantos |
|---|---|
| 3 | 36 |
| 4 | 31 |
| ausente (campo `degrau` nulo) | 11 |

## As duas colunas que o despacho não pediu, e que explicam as de cima

| o que | quantos |
|---|---|
| com `afiliado.url` (link de anúncio) e **sem** `url_produto` | **11** |
| com `afiliado.intestavel: true` | **11** |

## Por banco

| banco | registros | sem `url_busca` | sem `url_produto` |
|---|---|---|---|
| `produtos-aquecedor.json` | 27 | 0 | 18 |
| `produtos-filtro.json` | 19 | 0 | 5 |
| `produtos-iluminacao.json` | 26 | 0 | 15 |
| `produtos-midia.json` | 6 | 0 | 4 |

**Os sem `url_produto`, um por um:** `aquecedor/roxin-ht-1300-q3-25w`, `aquecedor/eheim-jager-50w`, `aquecedor/roxin-ht-1300-q3-50w`, `aquecedor/rs-50-50w`, `aquecedor/atman-at-100`, `aquecedor/eheim-jager-100w`, `aquecedor/roxin-ht-1300-q3-100w`, `aquecedor/atman-at-150`, `aquecedor/eheim-jager-150w`, `aquecedor/sicce-scuba-contactless-150w`, `aquecedor/atman-at-200`, `aquecedor/eheim-jager-200w`, `aquecedor/roxin-ht-1300-q3-200w`, `aquecedor/oceantech-warmer-x-5-250w`, `aquecedor/atman-at-300`, `aquecedor/roxin-ht-1300-q3-300w`, `aquecedor/hopar-j-226-500w`, `aquecedor/oceantech-warmer-x-5-500w`, `filtro/sunsun-hw-303b`, `filtro/atman-at-3338`, `filtro/atman-at-3338s`, `filtro/atman-at-3336`, `filtro/sunsun-hw-302`, `iluminacao/chihiros-wrgb-ii-pro-120`, `iluminacao/ista-i-401-45`, `iluminacao/chihiros-a-series-a301`, `iluminacao/chihiros-a-series-a361`, `iluminacao/aquarios-do-rio-led-60cm`, `iluminacao/chihiros-a-series-a451m`, `iluminacao/ista-il-401-60`, `iluminacao/chihiros-a-series-a601`, `iluminacao/chihiros-a-series-a801`, `iluminacao/chihiros-wrgb-ii-slim-90`, `iluminacao/chihiros-wrgb-ii-pro-60`, `iluminacao/chihiros-wrgb-ii-slim-120`, `iluminacao/chihiros-wrgb-ii-90`, `iluminacao/chihiros-wrgb-ii-pro-90`, `iluminacao/chihiros-wrgb-ii-120`, `midia/seachem-matrix-1l`, `midia/eheim-substrat-pro-1l`, `midia/jbl-micromec-1l`, `midia/seachem-matrixcarbon-250ml`

