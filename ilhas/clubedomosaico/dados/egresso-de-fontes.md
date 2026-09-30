# O QUE ESTA NUVEM ALCANCA DAS FONTES DESTA ILHA

**GERADO por `ferramentas/medir-egresso.py` — nao edite a mao.** A lista de hosts e derivada de
`dados/*.json` (mais o apex e o `www.` de cada um, que nenhum banco cita e sem os quais nao ha
diagnostico); medido em **2026-09-30 10:36Z**, 3 passadas por host, com `clubedomosaico.com.br` como controle.

> **A PERGUNTA QUE ESTE ARQUIVO RESPONDE NAO E "o dominio esta liberado": e "a fonte chega".**
> As duas discordaram em 30/09/2026 e a diferenca custou quatro blocos. Apex liberado que
> redireciona para `www.` recusado entrega **zero** — e ao mesmo tempo `403 ao CONNECT`, que o
> repositorio afirmava em quatro lugares, era **falso** para os mesmos dominios. Os dois vereditos
> tem de sair juntos ou nenhum dos dois serve.

## POR DOMINIO REGISTRAVEL — e o apex ao lado do `www.`, que e onde o diagnostico mora

| dominio registravel | apex | `www.` | entrega? | URLs de fonte nos bancos |
|---|---|---|---|---|
| `acrilex.com.br` | recusado | recusado | **nao** | 6 |
| `arauco.com.br` | recusado | recusado | **nao** | 0 |
| `berneck.com.br` | recusado | recusado | **nao** | 0 |
| `brasilit.com.br` | recusado | recusado | **nao** | 0 |
| `camara.leg.br` | recusado | recusado | **nao** | 1 |
| `cascola.com.br` | responde, sem entrega | recusado | **nao** | 2 |
| `cortag.com` | recusado | recusado | **nao** | 3 |
| `cultura.gob.es` | recusado | recusado | **nao** | 1 |
| `dexco.com.br` | recusado | recusado | **nao** | 0 |
| `duratex.com.br` | recusado | recusado | **nao** | 0 |
| `eternit.com.br` | recusado | recusado | **nao** | 0 |
| `faecpr.edu.br` | recusado | recusado | **nao** | 1 |
| `fasbam.edu.br` | recusado | recusado | **nao** | 1 |
| `glassmosaic.com.br` | recusado | recusado | **nao** | 12 |
| `guararapes.com.br` | recusado | recusado | **nao** | 0 |
| `henkel-adhesives.com` | recusado | recusado | **nao** | 0 |
| `henkel.com.br` | recusado | recusado | **nao** | 1 |
| `isoeste.com.br` | recusado | recusado | **nao** | 0 |
| `leroymerlin.com.br` | recusado | recusado | **nao** | 0 |
| `loctite.com.br` | responde, sem entrega | recusado | **nao** | 0 |
| `meli.la` | recusado | recusado | **nao** | 4 |
| `pastilhart.com.br` | recusado | recusado | **nao** | 2 |
| `quartzolit.weber` | responde, sem entrega | recusado | **nao** | 19 |
| `sagradafamilia.org` | recusado | recusado | **nao** | 1 |
| `sarasa.com.br` | recusado | recusado | **nao** | 1 |
| `spacesarchives.org` | recusado | recusado | **nao** | 1 |
| `tekbond.com.br` | responde, sem entrega | recusado | **nao** | 5 |
| `termotecnica.ind.br` | recusado | recusado | **nao** | 0 |
| `unl.pt` | recusado | recusado | **nao** | 1 |
| `vonder.com.br` | recusado | recusado | **nao** | 3 |
| `wikipedia.org` | recusado | recusado | **nao** | 2 |
| `clubedomosaico.com.br` | alcanca | alcanca | **sim** | 27 |
| `mercadolivre.com.br` | alcanca | alcanca | **sim** | 4 |
| `shopee.com.br` | alcanca | alcanca | **sim** | 117 |

### A PORTA ESTA PELA METADE, E E ESSE O FATO NOVO

Nestes 4 dominios o **apex responde** e o **`www.` e recusado** — e os sites redirecionam
tudo para `www.`, entao **nada chega**:

- `cascola.com.br` — CONNECT estabelecido, servidor responde **301** e manda para `www.cascola.com.br`, recusado.
- `loctite.com.br` — CONNECT estabelecido, servidor responde **301** e manda para `next.henkel-adhesives.com`, recusado.
- `quartzolit.weber` — CONNECT estabelecido, servidor responde **301** e manda para `www.quartzolit.weber`, recusado.
- `tekbond.com.br` — CONNECT estabelecido, servidor responde **301** e manda para `www.tekbond.com.br`, recusado.

**O que isto quer dizer, em uma frase:** o dominio entrou na lista **sem o curinga**, e a 20.1
manda os dois — `<dominio>` **e** `*.<dominio>`. Falta a metade que serve para algo.

## DETALHE POR HOST

| host | veredito | por que | citado em |
|---|---|---|---|
| `acrilex.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | materiais-acabamento.json |
| `arauco.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `berneck.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `blog.sagradafamilia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `brasilit.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `camara.leg.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `cortag.com` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | materiais-alicates.json |
| `cultura.gob.es` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `dexco.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `duratex.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `en.wikipedia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `eternit.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `faecpr.edu.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `fasbam.edu.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `glassmosaic.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | materiais-pastilhas.json |
| `guararapes.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `henkel-adhesives.com` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `henkel.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `isoeste.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `leroymerlin.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `meli.la` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | materiais-colas.json, materiais-rejuntes.json |
| `next.henkel-adhesives.com` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | fontes-pedidas.json (campo `dominio`), fontes-pedidas.json (exigido em prosa) |
| `pastilhart.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `pt.wikipedia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `run.unl.pt` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `sagradafamilia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `sarasa.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `spacesarchives.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `termotecnica.ind.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | esquema-banco.json (campo `dominios_em_000`) |
| `unl.pt` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `vonder.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `wikipedia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.acrilex.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.arauco.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.berneck.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.brasilit.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.camara.leg.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.cascola.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | constantes.json, materiais-colas.json |
| `www.cortag.com` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.cultura.gob.es` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `www.dexco.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.duratex.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.eternit.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.faecpr.edu.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `www.fasbam.edu.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.glassmosaic.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.guararapes.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.henkel-adhesives.com` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.henkel.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | constantes.json, materiais-colas.json |
| `www.isoeste.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.leroymerlin.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.loctite.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.meli.la` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.pastilhart.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | materiais-pastilhas.json |
| `www.quartzolit.weber` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | constantes.json, materiais-acabamento.json, materiais-colas.json, materiais-rejuntes.json |
| `www.sagradafamilia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.sarasa.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.spacesarchives.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.tekbond.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | constantes.json, materiais-colas.json |
| `www.termotecnica.ind.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.unl.pt` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www.vonder.com.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | materiais-alicates.json |
| `www.wikipedia.org` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | _nenhum banco o cita (irmao medido)_ |
| `www2.camara.leg.br` | **bloqueado** | o CONNECT e recusado nas 3 passadas (politica de egresso) | tecnicas.json |
| `cascola.com.br` | **liberado_mas_sem_entrega** | o CONNECT passa e o servidor responde 301, mas ele redireciona para `www.cascola.com.br`, que o egresso recusa — nada chega | _nenhum banco o cita (irmao medido)_ |
| `loctite.com.br` | **liberado_mas_sem_entrega** | o CONNECT passa e o servidor responde 301, mas ele redireciona para `next.henkel-adhesives.com`, que o egresso recusa — nada chega | fontes-pedidas.json (campo `dominio`), fontes-pedidas.json (exigido em prosa) |
| `quartzolit.weber` | **liberado_mas_sem_entrega** | o CONNECT passa e o servidor responde 301, mas ele redireciona para `www.quartzolit.weber`, que o egresso recusa — nada chega | _nenhum banco o cita (irmao medido)_ |
| `s.shopee.com.br` | **liberado_mas_sem_entrega** | o CONNECT passa e o servidor responde 307, mas ele redireciona para `shope.ee`, que o egresso recusa — nada chega | materiais-acabamento.json, materiais-alicates.json, materiais-colas.json, materiais-pastilhas.json, materiais-rejuntes.json |
| `tekbond.com.br` | **liberado_mas_sem_entrega** | o CONNECT passa e o servidor responde 301, mas ele redireciona para `www.tekbond.com.br`, que o egresso recusa — nada chega | _nenhum banco o cita (irmao medido)_ |
| `cf.shopee.com.br` | **alcancavel** | responde 200 com 42 bytes | materiais-acabamento.json, materiais-alicates.json, materiais-colas.json, materiais-rejuntes.json |
| `clubedomosaico.com.br` | **alcancavel** | responde 200 com 93181 bytes | esquema-banco.json (campo `dominios_em_000`), pecas.json |
| `mercadolivre.com.br` | **alcancavel** | responde 403 com 2585 bytes | _nenhum banco o cita (irmao medido)_ |
| `shopee.com.br` | **alcancavel** | responde 200 com 198160 bytes | materiais-acabamento.json, materiais-alicates.json, materiais-colas.json, materiais-pastilhas.json, materiais-rejuntes.json |
| `www.clubedomosaico.com.br` | **alcancavel** | responde 200 com 93181 bytes | _nenhum banco o cita (irmao medido)_ |
| `www.mercadolivre.com.br` | **alcancavel** | responde 403 com 2585 bytes | materiais-colas.json, materiais-rejuntes.json |
| `www.shopee.com.br` | **alcancavel** | responde 302 e redireciona para `shopee.com.br`, que tambem e alcancavel | _nenhum banco o cita (irmao medido)_ |

## O PEDIDO, DERIVADO DA MEDICAO (20.1 e 20.3)

A **20.1** manda acrescentar o dominio **e o curinga**. Caminho: `claude.ai/code` -> seletor de
ambiente -> Nuvem -> engrenagem -> Dominios permitidos. As linhas, uma por linha:

```
acrilex.com.br
*.acrilex.com.br
arauco.com.br
*.arauco.com.br
berneck.com.br
*.berneck.com.br
brasilit.com.br
*.brasilit.com.br
cascola.com.br
*.cascola.com.br
cortag.com
*.cortag.com
dexco.com.br
*.dexco.com.br
duratex.com.br
*.duratex.com.br
eternit.com.br
*.eternit.com.br
glassmosaic.com.br
*.glassmosaic.com.br
guararapes.com.br
*.guararapes.com.br
henkel-adhesives.com
*.henkel-adhesives.com
henkel.com.br
*.henkel.com.br
isoeste.com.br
*.isoeste.com.br
leroymerlin.com.br
*.leroymerlin.com.br
loctite.com.br
*.loctite.com.br
pastilhart.com.br
*.pastilhart.com.br
quartzolit.weber
*.quartzolit.weber
tekbond.com.br
*.tekbond.com.br
termotecnica.ind.br
*.termotecnica.ind.br
vonder.com.br
*.vonder.com.br
```

**Por que cada um esta na lista** — e nenhum esta por precaucao:

- `acrilex.com.br` — citado por `materiais-acabamento.json`.
- `arauco.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `berneck.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `brasilit.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `cascola.com.br` — citado por `constantes.json`, `materiais-colas.json`.
- `cortag.com` — citado por `materiais-alicates.json`.
- `dexco.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `duratex.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `eternit.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `glassmosaic.com.br` — citado por `materiais-pastilhas.json`.
- `guararapes.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `henkel-adhesives.com` — citado por `fontes-pedidas.json (campo `dominio`)`, `fontes-pedidas.json (exigido em prosa)`.
- `henkel.com.br` — citado por `constantes.json`, `materiais-colas.json`.
- `isoeste.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `leroymerlin.com.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `loctite.com.br` — citado por `fontes-pedidas.json (campo `dominio`)`, `fontes-pedidas.json (exigido em prosa)`.
- `pastilhart.com.br` — citado por `materiais-pastilhas.json`.
- `quartzolit.weber` — citado por `constantes.json`, `materiais-acabamento.json`, `materiais-colas.json`, `materiais-rejuntes.json`.
- `tekbond.com.br` — citado por `constantes.json`, `materiais-colas.json`.
- `termotecnica.ind.br` — citado por `esquema-banco.json (campo `dominios_em_000`)`.
- `vonder.com.br` — citado por `materiais-alicates.json`.

**Enquanto essas linhas nao entrarem, nenhuma execucao da Fundacao le a frase literal do
fabricante** nesses dominios — e insistir e gastar bloco para reescrever o mesmo motivo, que
foi o que aconteceu quatro vezes entre 26/09 e 29/09.

## BLOQUEADO E NAO PEDIDO — porque nenhum trabalho pendente depende dele

Estes hosts tambem nao chegam. Sao **referencia de conteudo ja lida e ja citada** (a fonte esta
gravada no banco com a data em que foi lida), nao fonte de coleta em aberto. Entram aqui para
ninguem os confundir com os de cima, e **pedido longo e pedido que nao se atende**:

- `blog.sagradafamilia.org` — tecnicas.json.
- `camara.leg.br` — nenhum banco o cita (irmao medido).
- `cultura.gob.es` — nenhum banco o cita (irmao medido).
- `en.wikipedia.org` — tecnicas.json.
- `faecpr.edu.br` — nenhum banco o cita (irmao medido).
- `fasbam.edu.br` — tecnicas.json.
- `pt.wikipedia.org` — tecnicas.json.
- `run.unl.pt` — tecnicas.json.
- `sagradafamilia.org` — nenhum banco o cita (irmao medido).
- `sarasa.com.br` — tecnicas.json.
- `spacesarchives.org` — tecnicas.json.
- `unl.pt` — nenhum banco o cita (irmao medido).
- `wikipedia.org` — nenhum banco o cita (irmao medido).
- `www.camara.leg.br` — nenhum banco o cita (irmao medido).
- `www.cultura.gob.es` — tecnicas.json.
- `www.faecpr.edu.br` — tecnicas.json.
- `www.fasbam.edu.br` — nenhum banco o cita (irmao medido).
- `www.meli.la` — nenhum banco o cita (irmao medido).
- `www.sagradafamilia.org` — nenhum banco o cita (irmao medido).
- `www.sarasa.com.br` — nenhum banco o cita (irmao medido).
- `www.spacesarchives.org` — nenhum banco o cita (irmao medido).
- `www.unl.pt` — nenhum banco o cita (irmao medido).
- `www.wikipedia.org` — nenhum banco o cita (irmao medido).
- `www2.camara.leg.br` — tecnicas.json.

## O QUE NAO SE PEDE POR DESENHO

- `cf.shopee.com.br` — CDN de imagem de anuncio, nao e fonte de dado.
- `clubedomosaico.com.br` — e a propria ilha, ja liberada.
- `meli.la` — encurtador do Mercado Livre, nao e fonte de dado.
- `s.shopee.com.br` — encurtador de link de afiliado, nao e fonte de dado.
- `shopee.com.br` — marketplace — o link nasce pela Open API (25.6), nao por leitura de pagina.
- `www.mercadolivre.com.br` — marketplace — etiqueta de afiliado, nao e fonte de dado.

