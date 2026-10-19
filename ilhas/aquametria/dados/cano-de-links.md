# Serie do CANO DE LINKS — Aquametria

Em que degrau da escada de compra (secao 25.1 do `ARQUIPELAGO.md`) cada
registro dos `dados/produtos-*.json` parou. Escreve aqui o
`ferramentas/conferir-cano-de-links.py --gravar`; quem confere e o mesmo
arquivo sem a opcao, e ele compara ITEM POR ITEM, nao pelo total.

**Secao nova vai no TOPO** (a serie cresce por cima, como `dados/posicoes.md`
e `dados/deriva-do-catalogo.md`) e secao antiga NUNCA e sobrescrita: a serie so
vale porque cresce. O bloco `json` de cada secao e a declaracao que o portao
le — o primeiro do arquivo e o que manda.

A frase de estado de cada item se le assim: `piso` e ter `afiliado.url_busca`
(o piso da 25.2, que nunca depende de ninguem), `ficha` e ter `url_produto` (o
degrau que paga comissao e o unico que o teste de vida da 25.4 alcanca),
`anuncio` e ter `url`, `degrau` e o degrau declarado (`-` e nulo) e
`intestavel` e a bandeira da 25.4-b.

Cano que muda **nao e defeito**: coleta nova, link que morreu e ficha que
chegou movem estes numeros por desenho. O que e defeito e cano que mudou e
ninguem contou — e era o que acontecia antes de 19/10/2026, quando a contagem
saia em relatorio datado que nada comparava com o do dia anterior.

## 2026-10-19 10:22Z

**78 registro(s)** em 5 banco(s) de produto.

| o que | quantos |
|---|---|
| sem `afiliado.url_busca` — o piso da 25.2 | **0** |
| sem `afiliado.url_produto` — a ficha que paga comissao | **42** |
| com `url` e **sem** `url_produto` — a divida da 25.4-b | **11** |
| com `intestavel: true` | **11** |

**Por `degrau`:** 3 = 36, 4 = 31, nulo = 11

```json
{
  "bancos": [
    "produtos-aquecedor.json",
    "produtos-cotacoes.json",
    "produtos-filtro.json",
    "produtos-iluminacao.json",
    "produtos-midia.json"
  ],
  "degraus": {
    "-": 11,
    "3": 36,
    "4": 31
  },
  "itens": {
    "aquecedor/atman-at-100": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/atman-at-150": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/atman-at-200": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/atman-at-300": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/eheim-jager-100w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/eheim-jager-150w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/eheim-jager-200w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/eheim-jager-50w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/hopar-j-226-400w": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/hopar-j-226-500w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/maxxi-m-050-anuncio-220v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/maxxi-m-100-anuncio-127v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/maxxi-m-150-anuncio-220v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/maxxi-m-200-anuncio-110v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/maxxi-m-200-anuncio-220v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/maxxi-m-300-anuncio-110v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/maxxi-m-300-anuncio-220v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/oceantech-warmer-x-5-150w": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "aquecedor/oceantech-warmer-x-5-250w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/oceantech-warmer-x-5-500w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/roxin-ht-1300-q3-100w": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "aquecedor/roxin-ht-1300-q3-200w": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "aquecedor/roxin-ht-1300-q3-25w": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "aquecedor/roxin-ht-1300-q3-300w": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "aquecedor/roxin-ht-1300-q3-50w": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "aquecedor/rs-50-50w": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "aquecedor/sicce-scuba-contactless-150w": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "filtro/aquaverso-apk-600": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/atman-at-3336": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "filtro/atman-at-3338": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "filtro/atman-at-3338s": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "filtro/atman-hf-0400": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/atman-hf-0600": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/atman-hf-0800": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/eheim-classic-250-2213": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/eheim-classic-600-2217-127v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/eheim-classic-600-2217-220v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/maxxi-pro-mp-600": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/oceantech-ct-1000-3": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/seachem-tidal-55": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/sunsun-hw-302": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "filtro/sunsun-hw-303b": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "filtro/sunsun-hw-603b": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/sunsun-hw-702a-anuncio-110v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/sunsun-hw-702b-220v": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "filtro/sunsun-xbl-600": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/aquarios-do-rio-led-60cm": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-a-series-a301": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-a-series-a361": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-a-series-a451m": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "iluminacao/chihiros-a-series-a601": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-a-series-a801": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-a-series-a901": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/chihiros-wrgb-ii-120": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-wrgb-ii-90": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-wrgb-ii-pro-120": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-wrgb-ii-pro-60": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "iluminacao/chihiros-wrgb-ii-pro-90": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-wrgb-ii-slim-120": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/chihiros-wrgb-ii-slim-90": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/ista-i-401-45": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "iluminacao/ista-il-401-60": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "iluminacao/soma-s-1000-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-1200-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-200-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-300-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-400-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-500-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-600-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/soma-s-800-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/sunsun-ade-400c": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "iluminacao/wfish-wf-h600-wrgb": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "midia/eheim-substrat-pro-1l": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "midia/jbl-micromec-1l": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "midia/ocean-tech-bio-glass-1l": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0",
    "midia/seachem-matrix-1l": "piso:1 ficha:0 anuncio:1 degrau:- intestavel:1",
    "midia/seachem-matrixcarbon-250ml": "piso:1 ficha:0 anuncio:0 degrau:4 intestavel:0",
    "midia/seachem-purigen-100ml": "piso:1 ficha:1 anuncio:1 degrau:3 intestavel:0"
  },
  "medido_em": "2026-10-19 10:22Z",
  "totais": {
    "intestaveis": 11,
    "registros": 78,
    "sem_url_busca": 0,
    "sem_url_produto": 42,
    "url_sem_url_produto": 11
  }
}
```

