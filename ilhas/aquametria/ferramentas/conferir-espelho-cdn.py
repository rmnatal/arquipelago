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


fotos = [(arq, p) for arq, p in banco() if (p.get('imagem') or {}).get('url')]
controle = [(arq, p) for arq, p in fotos
            if p['imagem'].get('largura') is not None
            and regua.precisa_de_espelho(p['imagem']['url'])]
ja_alcancaveis = [(arq, p) for arq, p in fotos
                  if p['imagem'].get('largura') is not None
                  and not regua.precisa_de_espelho(p['imagem']['url'])]

print('%d fotos no banco, %d com dimensao' % (len(fotos), len(controle) + len(ja_alcancaveis)))
print('GRUPO DE CONTROLE: %d fotos em host que esta nuvem nao alcanca '
      'e que ja tem dimensao medida por outro instrumento\n' % len(controle))

# PORTAO QUE MEDE ZERO COISAS PASSA SEMPRE. Se o banco perder o grupo de
# controle — por troca de CDN, por limpeza, por qualquer motivo —, a premissa do
# espelho deixa de ser conferivel, e isso e uma reprovacao e nao um silencio.
ok('o grupo de controle existe (sem ele a premissa do espelho nao se mede)',
   len(controle) >= 5, 'apenas %d foto(s) no controle' % len(controle))

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
