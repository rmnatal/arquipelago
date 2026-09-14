---
ilha: ohmetria
estado: nascendo
prioridade: 1
piso: abaixo            # abaixo | atingido — ver seção 21 do ARQUIPELAGO.md
urls_publicadas: 0
primeira_indexacao: null
ultima_execucao: null
executando_desde: 2026-09-14T17:17Z
bloco_atual: |
  NASCEU EM 14/09/2026 pela aprovação do Raphael, sobre o dossiê da rodada 004 da Bússola (`bussola/dossies/som-automotivo/`), índice 4,00 — 1º da fila.
  NENHUM BLOCO EXECUTADO AINDA. O próximo é o BLOCO 1 (levantamento de buscas paramétricas), que **não depende de domínio nem de site** e pode rodar hoje.
  ATENÇÃO: o domínio ainda NÃO foi registrado. A disponibilidade foi confirmada em 14/09 no registro.br (`{"status":0,"fqdn":"ohmetria.com.br"}`), mas o passo 1 da seção 11 é do RAPHAEL e não foi feito. Não marque `bloqueada_por` por causa disso — os blocos 1, 2, 3 e 3c não precisam de infraestrutura.
bloqueada_por: null
---

# Estado da ilha OHMETRIA

Espelho legível do estado do projeto. **Nunca guarde credencial aqui.**

## Infraestrutura
- Domínio: **`ohmetria.com.br` — PENDENTE DE REGISTRO.** Disponibilidade confirmada em 14/09/2026 (`registro.br/v2/ajax/avail/raw/ohmetria.com.br` → `status: 0` = livre). **Passo 1 da seção 11 do `ARQUIPELAGO.md`, e é do Raphael: só ele tem CPF e cartão.**
- Hospedagem: domínio adicional no mesmo plano da HostGator, **com raiz própria** `/home3/<usuário>/ohmetria` — nunca compartilhando raiz com outra ilha. Pendente.
- Nameservers: `ns604` e `ns605.hostgator.com.br`, **só DEPOIS do domínio adicional existir no cPanel** — invertendo a ordem o registro.br recusa. Pendente.
- Search Console: propriedade de **Domínio** (não prefixo de URL), **antes do WordPress**. Pendente.
- WordPress: pendente.
- Snippet de Sync: `Ohmetria Sync`, token novo gerado na hora. Pendente.
- Etiquetas do Mercado Livre: `ohmetriaf1`, `ohmetriaf2`, `ohmetriaf3` — **ainda não existem** na conta RMNATAL. Criar etiqueta funciona por script; **gerar o link, não** (reCAPTCHA — é trabalho do Raphael, seção 7).

## O que já foi entregue
Nada ainda. A ilha nasceu hoje.

## O que está travando
Nada trava o trabalho. O domínio pendente só adia os blocos que precisam de site (3b em diante); os blocos 1, 2, 3 e 3c rodam sem infraestrutura e são exatamente os primeiros da fila.
