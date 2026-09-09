# ILHA: AQUAMETRIA — aquarismo

Leia o `ARQUIPELAGO.md` da raiz antes deste arquivo. Ele carrega todas as regras comuns; aqui fica só o que é desta ilha.

## Identidade
- Nicho: aquarismo — calculadoras de dimensionamento e banco técnico.
- Domínio: https://aquametria.com.br (no ar desde 06/09/2026). Primeira ilha do Arquipélago.
- Paleta: tinta `#0D1B22` · lâmina `#0E7C8C` · papel `#F4F7F7` · superfície `#FFFFFF` · traço `#DDE5E6` · legenda `#5C7075` · alerta `#B5762A`.
- Tipografia: **Chivo** (títulos) · **IBM Plex Sans** (texto) · **IBM Plex Mono** (números, com `tabular-nums`).
- Símbolo: instrumento de precisão — recipiente graduado com linha de enchimento. **Sem peixe, sem bolha, sem mascote.**

## Endpoints desta ilha
- Sync: `https://aquametria.com.br/?aquametria_sync=kgbErDOIVAFWUtUzutHGrKevVgmWGVjz&forcar=1`
- Status: `https://aquametria.com.br/wp-json/aquametria/v1/status`
- O Sync se pula a si mesmo por desenho: correção nele chega pelo snippet atualizador.

## Quem verifica esta ilha
- **Sentinela técnica**, todo dia 11h30 BRT, **no Chrome do Raphael**: abre cada página, executa cada calculadora e lê o console. Disparo dela com defeito descrito **tem prioridade sobre a fila**.
- **Sentinela estratégica**, quartas: funil, indexação, vendas, Shopee, backlink.

## Memória a carregar
`/areas/projeto-aquametria.md`, `/areas/aquametria-corpus-buscas.md`, `/areas/playbook-nascimento-projeto.md` (fase 4b), `/topics/dev-conventions.md`, `/areas/fabrica-de-sites.md`. Sem memória, **não pare**: o estado está em `ESTADO.md`, `REGISTRO.md` e `README.md` desta pasta.

---

## FILA DE BLOCOS

Reordenada em 09/09/2026. O gargalo de tamanho é o **banco**; o de citabilidade é o **schema**; o de conversão é a **apresentação do produto**. Calculadora nova não é prioridade.

**1–3b. Buscas paramétricas, especificação, banco e casca — CONCLUÍDOS.** Não refaça.

**4. Calculadoras publicadas e verificadas rodando: C1, C3, C5, C12, C15.** Faltam C2 peso, C7 consumo, C8 lotação — só **depois** de 4c, 4e e 4b.

**4c. RETROFIT DE VISIBILIDADE EM IA — em andamento.** Medição da Sentinela: JSON-LD zero em 13 de 13 páginas. Duas calculadoras por execução: (a) JSON-LD; (b) tabela de exemplos pré-renderizada para 30/60/100/150/200/300 L; (c) resposta antes da explicação; (d) procedência na frase. Ordem: C3 e C5, depois C12 e C15, depois C1 e os artigos.

**4e. VITRINE DE PRODUTO E INTENÇÃO DE COMPRA EXPLÍCITA.** Layout aprovado pelo Raphael em 09/09/2026. Regras gerais na seção 6 do `ARQUIPELAGO.md`; o específico desta ilha:
- Bloqueio de dado a resolver primeiro: preencher `imagem` para os itens que já têm `afiliado.url`, usando a foto do próprio anúncio da Shopee. Se a nuvem não alcançar o CDN da Shopee, **guarde a URL com `verificado_em: null`** e deixe a Sentinela confirmar no navegador — não anule o campo.
- Cartão diz a especificação que fez o produto entrar: "440 L/h — atende os 190 L do seu aquário".
- Linha de promessa no topo: "calcule a vazão do seu aquário e veja quais filtros atendem, com a faixa e a fonte de cada um". Curto, sem exclamação, sem tom de anúncio.
- A tabela de exemplos do 4c já resolve metade disso: inclua nela a coluna do produto que atende cada faixa. Serve ao humano e à IA na mesma passada.

**4b. EXPANSÃO DO BANCO EM ESCALA. 2 a 3 execuções.**
- (a) **A C15 iluminação não vende nada.** Catálogo tem 3 luminárias e a única com link (Ista I-401, 45 cm, 810 lm) não cai em faixa nenhuma. Encha o catálogo de 30 a 120 cm cobrindo baixa/média/alta exigência, com lúmen e voltagem de fonte do fabricante.
- (b) **Fechar a voltagem** dos elétricos que faltam, com fonte e data. Não fechou: `voltagem: null` com o motivo. **Nunca chute 110 ou 220.**
- (c) **Ampliar o catálogo geral** com ficha completa. Referência: pelo menos 60 itens. A Sentinela mediu que a C5 a 108 L pede 110–150 W e os três aquecedores com link são 100/200/300 W — nenhum na janela. Buraco assim é perda de venda direta.
- (d) **Iniciar o banco de espécies (C10)** — ficha, não calculadora: temperatura, pH, porte adulto, espaço mínimo, comportamento, com fonte. Destrava "quantos litros para X peixes", eixo que a Bússola verificou ABERTO.
- (e) Produto novo entra sem `afiliado.url`; quem gera o link é a Sentinela estratégica (até 10 por semana). Deixe o campo pronto e reporte quantos esperam link.

**4d. DOIS AJUSTES MENORES** — encaixe em qualquer execução, não gastam um bloco:
- Os 3 artigos vivem em `/2026/09/08/<slug>/` e caem em `/category/uncategorized/`, que está no sitemap. Crie categoria de verdade.
- Padronize a mensagem de bloco de produto vazio.

**5. ARTIGOS-ÂNCORA** pareados com cada calculadora nova, na mesma execução (mesma pesquisa). Toda tabela técnica cita o manual do fabricante e leva data.

**5b. MALHA DE PÁGINAS.** Camadas: ficha de produto · ficha de espécie · página de volume · cruzamentos. **Eixo:** as fazendas já tomaram "melhor filtro para aquário de X litros" — priorize "quantos litros para X peixes" e "quantos watts de aquecedor". Portão e rampa na seção 9 do `ARQUIPELAGO.md`.

**6. LISTA DE PROSPECÇÃO DO WIDGET** — lojas de aquarismo brasileiras com site próprio, `publicar: false`. É a **única** alavanca de link do projeto.

## Link interno obrigatório
Toda calculadora linka as outras que consomem o mesmo estado, a metodologia, o artigo pareado e as páginas de entidade.
