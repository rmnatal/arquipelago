# AUDIÊNCIA — Clube do Mosaico

Série de leituras do GA4 desta ilha, pela seção 5 do `ARQUIPELAGO.md`.

**Regra da série, e ela é a razão deste arquivo existir:** uma linha nova por
leitura, **nunca sobrescrevendo a anterior** — igual a `dados/indexacao.md`.
Zero sessão é dado e entra na série. "Não consegui medir" também é dado, desde
que diga **por quê** — e as duas coisas não são a mesma, que é justamente o que
esta ilha não conseguia distinguir até hoje.

Leitura: `python3 ferramentas/ga4.py clubedomosaico --dias 7` (na raiz do
repositório), com a credencial da conta de serviço no ambiente. Quem grava a
série é a **Sentinela**, na ronda; a Fundação só abriu o arquivo com o marco
zero abaixo.

- Propriedade GA4: `553922792` · conta `Arquipélago` (`407777291`)
- ID de medição: **G-0K5PY39HV7** · fluxo "Clube do Mosaico — site" (`15766180417`)

---

## MARCO ZERO — 12/09/2026

**A medição desta ilha começou em 12/09/2026, às 17h37 UTC**, com a casca 1.7.0
(manifest revisão 13) servindo a tag no `wp_head` das onze páginas. Antes desta
data e hora **não existe dado**, e isso não é uma lacuna da série: é a série
começando. A seção 21 vai precisar deste marco para saber a partir de quando o
zero é informação.

**O que o zero media antes.** Esta ilha nasceu em 10/09/2026 e serviu nove, e
depois onze, URLs sem tag nenhuma. Qualquer leitura feita antes de hoje teria
devolvido zero, e o zero teria medido **a ausência da tag**, nunca a ausência de
visita. A seção 5 manda o relatório dizer qual dos dois é — e até hoje a resposta
desta ilha era sempre o primeiro.

---

## LEITURAS

| data | dias | sessões | usuários | canais | IA (sessões) | quem leu |
|---|---|---|---|---|---|---|
| 2026-09-12 | — | **não medido** | — | — | — | Fundação |

**2026-09-12 — não medido, e o motivo tem duas metades, as duas medidas.**
A leitura não foi feita nesta execução, e nenhuma das duas causas é "não tentei":

1. **Sem credencial no ambiente.** `ferramentas/ga4.py` exige `GOOGLE_SA_B64`,
   `GOOGLE_SA_JSON` ou `GOOGLE_SA_FILE`, e nenhuma das três está definida no
   ambiente desta rotina (conferido: zero variável `GOOGLE*`). A conta de serviço
   é Leitor na conta `Arquipélago`, então é só a variável que falta — não é
   permissão.
2. **`www.googletagmanager.com` está fora da lista de egresso.** O gateway
   responde **403 ao CONNECT**, cinco vezes seguidas, enquanto
   `clubedomosaico.com.br` responde 200 na mesma passada. Não é a intermitência
   de túnel da seção 20.2: é política. Consequência prática, e ela é maior do
   que parece: **nenhuma verificação de tag feita por navegador a partir da
   nuvem pode funcionar** enquanto esse host estiver barrado, porque o navegador
   não baixaria o `gtag.js`.

Pela seção 4 e pela 18.4, isso deixa **um** dos três critérios do despacho em
aberto nesta ilha — o Tempo Real. Os outros dois (a tag no HTML servido com o ID
certo, e o `/status` batendo com o manifest) foram medidos e estão fechados.

**O que fecha o item, e é uma linha de configuração, não código:**
`www.googletagmanager.com` e `*.google-analytics.com` na rede Personalizada do
ambiente das rotinas, junto com os domínios das ilhas que já estão lá; e a
credencial da conta de serviço na variável de ambiente. Enquanto isso não
acontece, quem consegue confirmar o Tempo Real é o Raphael, abrindo o site no
Chrome dele.

**O que NÃO se faz enquanto isso:** mandar um evento pelo Measurement Protocol
para "confirmar" que a medição funciona. Seria inventar a visita que se queria
comprovar e sujar esta série com uma sessão que nunca existiu. Zero medido é
dado; zero fabricado é mentira.
