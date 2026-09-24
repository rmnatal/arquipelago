#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O PORTAO NO AR DO ESPELHO — remede o GRUPO DE CONTROLE no CDN de verdade.

    python3 ferramentas/conferir-espelho-cdn.py

Este portao nao mede o site da ilha: mede a PREMISSA que permite esta ilha
publicar dimensao de foto hospedada num endereco que a nuvem nao alcanca.

---------------------------------------------------------------------------
A PREMISSA, E POR QUE ELA PRECISA DE UM PORTAO SO PARA ELA
---------------------------------------------------------------------------
O egresso desta nuvem barra `down-bs-br.img.susercontent.com`, que e de onde o
painel de afiliados copia a URL da foto. Desde 24/09/2026 esta ilha mede aquelas
fotos pelo ESPELHO — `cf.shopee.com.br/file/<mesmo id>`, que a nuvem alcanca.

Isso so vale porque os dois hosts servem o mesmo arquivo. **E isso e uma
afirmacao sobre a infraestrutura de outra empresa**, que pode mudar sem avisar
ninguem — e afirmacao sobre infra alheia que envelhece calada e a familia de
defeito que a secao 4 do contrato paga mais caro.

Entao ela nao fica suposta: fica MEDIDA, a cada passada, contra um grupo de
controle que esta ilha tinha guardado sem saber para que serviria.

---------------------------------------------------------------------------
O GRUPO DE CONTROLE
---------------------------------------------------------------------------
Sao as fotos do banco que cumprem as duas condicoes ao mesmo tempo:

  (a) estao hospedadas num host que esta nuvem NAO alcanca, e
  (b) ja tem largura e altura no banco.

Como a nuvem nao as alcanca, aquela dimensao so pode ter vindo de OUTRO
INSTRUMENTO — e veio: `naturalWidth` x `naturalHeight` lidos no Chrome do
Raphael pela ronda da Sentinela de 13/09/2026, do outro lado do bloqueio.

Sao oito hoje, e elas medem 265, 692, 726, 1000, 1001 e 1024. **Os numeros
tortos sao o portao**: um espelho que servisse miniatura padronizada devolveria
800x800 para todas, e as tortas ficariam vermelhas na primeira passada.

O grupo se monta sozinho do banco. Foto nova que a Sentinela medir no Chrome
entra nele sem ninguem se lembrar; e se ele UM DIA ficar vazio, este portao
reprova em vez de imprimir "0 de 0, tudo certo" — que e a maneira mais comum de
um portao morrer sem ninguem ver.
"""

import glob
import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    'regua_cdn', os.path.join(RAIZ, 'ferramentas', 'regua-cdn-shopee.py'))
regua = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(regua)

afirmacoes = 0
falhas = []


def ok(titulo, condicao, detalhe=''):
    global afirmacoes
    afirmacoes += 1
    if condicao:
        return True
    falhas.append('%s%s' % (titulo, (' — ' + detalhe) if detalhe else ''))
    return False


def banco():
    for caminho in sorted(glob.glob(os.path.join(RAIZ, 'dados', 'produtos-*.json'))):
        with open(caminho, encoding='utf-8') as f:
            dados = json.load(f)
        for p in dados.get('produtos') or []:
            yield os.path.basename(caminho), p


# ---------------------------------------------------------------------------
# QUEM E CONTROLE E QUEM NAO E — a distincao que este portao quase perdeu
# ---------------------------------------------------------------------------
# NA PRIMEIRA VERSAO, escrita horas atras em 24/09/2026, "controle" era toda
# foto em host bloqueado que tivesse dimensao. Aquilo estava certo enquanto as
# UNICAS fotos assim eram as 8 que a Sentinela mediu no Chrome — e deixou de
# estar certo no minuto seguinte, quando o `coletar-dimensao-imagens.py` mediu
# 24 fotos do mesmo host PELO ESPELHO. O portao passou a imprimir "32 fotos com
# dimensao medida por outro instrumento", e 24 daquelas 32 tinham sido medidas
# pelo proprio espelho que elas deveriam estar conferindo.
#
# **Nao era um numero errado: era uma PROVA diluida com as proprias conclusoes.**
# O portao continuaria ficando vermelho se o CDN mudasse (as 8 verdadeiras
# reprovariam), mas afirmaria quatro vezes mais evidencia do que tem — e
# evidencia inflada e como se para de desconfiar de uma premissa.
#
# A regra: **so e controle quem foi medido por OUTRO instrumento.** Quem
# escreve `medida_como` diz de onde o numero veio, e e esse campo que separa os
# dois — nao a presenca da dimensao.
MARCA_DO_ESPELHO = 'ESPELHO do CDN'

fotos = [(arq, p) for arq, p in banco() if (p.get('imagem') or {}).get('url')]
com_dimensao = [(a, p) for a, p in fotos if p['imagem'].get('largura') is not None]

def medida_pelo_espelho(produto):
    return MARCA_DO_ESPELHO in (produto['imagem'].get('medida_como') or '')

controle = [(a, p) for a, p in com_dimensao
            if regua.precisa_de_espelho(p['imagem']['url'])
            and not medida_pelo_espelho(p)]
pelo_espelho = [(a, p) for a, p in com_dimensao
                if regua.precisa_de_espelho(p['imagem']['url'])
                and medida_pelo_espelho(p)]
ja_alcancaveis = [(a, p) for a, p in com_dimensao
                  if not regua.precisa_de_espelho(p['imagem']['url'])]

print('%d fotos no banco, %d com dimensao' % (len(fotos), len(com_dimensao)))
print('GRUPO DE CONTROLE: %d fotos em host que esta nuvem nao alcanca e cuja '
      'dimensao veio de OUTRO instrumento' % len(controle))
print('  (mais %d medidas pelo proprio espelho: elas NAO sao controle, e '
      'remedi-las e teste de regressao do CDN, nao prova da premissa)\n'
      % len(pelo_espelho))

# PORTAO QUE MEDE ZERO COISAS PASSA SEMPRE. Se o banco perder o grupo de
# controle — por troca de CDN, por limpeza, por qualquer motivo —, a premissa do
# espelho deixa de ser conferivel, e isso e uma reprovacao e nao um silencio.
ok('o grupo de controle existe (sem ele a premissa do espelho nao se mede)',
   len(controle) >= 5, 'apenas %d foto(s) medida(s) por outro instrumento' % len(controle))

# E A PORTA DOS FUNDOS DA DEFINICAO ACIMA: "controle" esta definido por NEGACAO
# — nao menciona o espelho. Uma foto com `medida_como` VAZIO, ou com um texto
# qualquer, cairia no controle por omissao e diluiria a prova do mesmo jeito,
# so que sem ninguem conseguir ver. Entao o controle tem de dizer, em campo, de
# onde veio o numero: cada membro declara um instrumento, e o instrumento nao e
# esta ferramenta.
for arq, p in controle:
    como = (p['imagem'].get('medida_como') or '').strip()
    ok('%s: o controle DIZ de onde veio o numero' % p['id'], len(como) >= 40,
       'medida_como=%r — controle sem procedencia escrita nao e controle, e '
       'foto que ninguem sabe quem mediu' % como[:60])

for arq, p in controle:
    img = p['imagem']
    esperado = (img['largura'], img['altura'])
    L, A, alvo, erro = regua.medir_no_espelho(img['url'])
    if not ok('%s: o espelho responde' % p['id'], L is not None,
              'espelho=%s erro=%s' % (alvo, erro)):
        continue
    ok('%s: o espelho devolve %dx%d, igual ao que o Chrome mediu no host bloqueado'
       % (p['id'], esperado[0], esperado[1]),
       (L, A) == esperado,
       'espelho=%dx%d banco=%dx%d — A PREMISSA DO ESPELHO CAIU: o CDN deixou de '
       'servir o mesmo arquivo nos dois hosts, e toda dimensao medida por '
       'espelho neste banco passa a ser suspeita' % (L, A, esperado[0], esperado[1]))

# E O CONTROLE SO PROVA ALGUMA COISA SE FOR TORTO. Oito fotos todas de 1024x1024
# passariam por um espelho que servisse miniatura de 1024 — e o portao ficaria
# verde afirmando o contrario do que aconteceu.
tortos = {(p['imagem']['largura'], p['imagem']['altura']) for _, p in controle}
tortos = {t for t in tortos if t[0] not in (256, 512, 800, 1024, 2048)}
ok('o controle tem dimensao NAO redonda (senao ele nao distingue espelho de miniatura)',
   len(tortos) >= 2, 'dimensoes do controle: %s' % sorted(tortos))

# AS QUE JA ESTAO NO HOST ALCANCAVEL nao provam a premissa — elas nao atravessam
# fronteira nenhuma —, mas provam que a leitura de cabecalho continua certa.
print('\n%d fotos ja no host alcancavel (nao provam a premissa, provam a leitura)'
      % len(ja_alcancaveis))
for arq, p in ja_alcancaveis:
    img = p['imagem']
    esperado = (img['largura'], img['altura'])
    L, A, alvo, erro = regua.medir_no_espelho(img['url'])
    if not ok('%s: responde' % p['id'], L is not None, 'erro=%s' % erro):
        continue
    ok('%s: continua %dx%d' % (p['id'], esperado[0], esperado[1]),
       (L, A) == esperado, 'no ar=%dx%d banco=%dx%d' % (L, A, esperado[0], esperado[1]))

# AS MEDIDAS PELO ESPELHO SAO REMEDIDAS TAMBEM, com o rotulo certo: nao provam a
# premissa (foram medidas pelo instrumento que estao conferindo), mas pegam o CDN
# passando a servir outros bytes para o mesmo id — que e exatamente o risco que o
# controle existe para vigiar, so que sem valer como prova dele.
print('\n%d fotos medidas pelo espelho, remedidas como regressao' % len(pelo_espelho))
for arq, p in pelo_espelho:
    img = p['imagem']
    esperado = (img['largura'], img['altura'])
    L, A, alvo, erro = regua.medir_no_espelho(img['url'])
    if not ok('%s: o espelho responde' % p['id'], L is not None, 'erro=%s' % erro):
        continue
    ok('%s: continua %dx%d' % (p['id'], esperado[0], esperado[1]),
       (L, A) == esperado,
       'espelho=%dx%d banco=%dx%d — o CDN mudou os bytes deste id desde a medida'
       % (L, A, esperado[0], esperado[1]))

# E A DIRECAO QUE NENHUMA DAS DE CIMA PEGA: foto SEM dimensao cujo espelho
# responde e foto que esta esperando medida a toa. Nao e reprovacao — e a lista
# que a proxima passada de `coletar-dimensao-imagens.py` tem de zerar.
sem_dimensao = [p for _, p in fotos if p['imagem'].get('largura') is None]
print('\n%d foto(s) sem dimensao no banco' % len(sem_dimensao))
for p in sem_dimensao:
    print('   - %s' % p['id'])

print('\n%d afirmacoes, %d falha(s)' % (afirmacoes, len(falhas)))
for f in falhas:
    print('  FALHOU: %s' % f)
sys.exit(1 if falhas else 0)
