#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGRA que decide se um anuncio SERVE a consulta de produto, e nada mais.

Mora sozinha, pelo mesmo motivo que `casar-anuncio.py` mora sozinha: e a regra
que `ferramentas/mutacoes-relevancia.py` ataca. Ferramenta que coleta e regra
que decide no mesmo arquivo viram uma bancada que mede a si mesma.

---------------------------------------------------------------------------
POR QUE ESTA REGRA EXISTE, com o numero que a pediu
---------------------------------------------------------------------------
A secao 30.2 do ARQUIPELAGO.md abre o portao da pagina de consulta de produto
com dado COMERCIAL: anuncio de Shopee e de Mercado Livre e fonte valida de
titulo, preco, foto, medida e quantidade. O que ela NAO diz — e nao tinha como
dizer — e que a busca da propria Shopee devolve, para a consulta
`pastilha para mosaico`, uma PLACA DE NUMERO DE CASA em primeiro lugar.

Medido em 09/10/2026, 20 ofertas da API para `pastilhas para mosaico`:

    7 placas de numero de casa (`Crie Casa`), que USAM mosaico e nao SAO material
    6 adesivos de parede e papel de parede, que imitam pastilha e nao sao pastilha
    1 torques (ferramenta, outra consulta desta mesma lista)
    1 placa de revestimento 30x30 para lavabo (obra, a armadilha do PROMPT.md)
    5 kits de pastilha de verdade, vendidos por contagem — os unicos que servem

**Quinze de vinte nao eram o produto.** Publicar os vinte numa pagina que
promete `pastilhas para mosaico` seria a ilha fazendo exatamente o que ela
existe para nao fazer: servir a lista do marketplace de volta, com o nome dela
em cima. O despacho do Raphael de 09/10/2026 pediu o contrario com estas
palavras — *"A galera que faz isso e ruim na internet, eu quero que voce seja o
melhor de todos."*

---------------------------------------------------------------------------
A REGRA, e ela e UMA so
---------------------------------------------------------------------------
Um anuncio SERVE a consulta quando as duas coisas valem:

1. **Cada grupo de `exige` tem ao menos um termo no titulo.** Grupo e OU dentro
   dele e E entre eles: `[["torques","alicate"],["mosaico"]]` quer dizer *(torques
   OU alicate) E mosaico*. Sinonimo que o vendedor digita no lugar do nosso nome
   entra como irmao no grupo, nunca como grupo novo.
2. **Nenhum termo de `recusa` aparece no titulo.** Recusa vence exigencia sempre:
   `Pastilha Espelhada ADESIVA` tem `pastilha` e tem `mosaico`, e nao e pastilha.

**A assimetria e de proposito, e e a da secao 10 do contrato.** Deixar entrar o
que nao e o produto estraga a pagina para quem chegou pela consulta; deixar de
fora um anuncio que servia custa um anuncio, e a pagina tem outros. Entao, na
duvida, a regra recusa — e cada recusa fica GRAVADA com o termo que a causou,
porque recusa sem motivo escrito e a mesma coisa que lista escolhida a dedo.

---------------------------------------------------------------------------
O QUE ELA NAO FAZ, para ninguem pedir isso a ela
---------------------------------------------------------------------------
- **Nao julga preco, loja nem nota.** Anuncio caro, barato ou de vendedor ruim
  serve ou nao serve pela mesma regra. Preco entra na FAIXA que a pagina publica.
- **Nao casa o anuncio com um registro do banco de fabricante.** Isso e
  `casar-anuncio.py`, e e outra pergunta: aqui ninguem pergunta QUAL produto e,
  so se ele e DO TIPO que a consulta pede.
- **Nao decide se a pagina nasce.** Isso e o cruzamento dos dois portoes (dado e
  SERP), e mora em `cruzamento-14-9.py`.
"""

import re
import unicodedata

# O marcador que separa DECLARACAO QUEBRADA de anuncio que nao casou. Ele e uma
# constante e nao uma frase solta porque a bancada o compara por igualdade: frase
# digitada nos dois lugares divergiria calada.
GRUPO_VAZIO = '<grupo de exigencia vazio na declaracao>'


def sem_acento(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto or '')
                   if unicodedata.category(c) != 'Mn')


def palavra(bruto):
    """Uma palavra comparavel: sem acento, minuscula, sem o plural obvio.

    O corte do `s` final em palavra de 5 letras ou mais e o mesmo de
    `casar-anuncio.py`, e ele e a correcao do PRIMEIRO defeito que o ensaio
    desta regra achou, em 09/10/2026: `exige: pastilha` nao casava com
    *"Kit com 900 **Pastilhas** para Mosaico, Artesanato"*, e `recusa: adesivo`
    nao casava com *"Kit 5 **Adesivos** Placa 30x30"*. O resultado era o pior
    possivel nas duas direcoes ao mesmo tempo — os CINCO kits de pastilha de
    verdade recusados, e as DUAS ofertas de obra e de adesivo aceitas, na mesma
    consulta.

    O corte e cego de proposito (`cristais` vira `cristai`), e isso nao quebra
    nada porque os DOIS lados da comparacao passam por aqui: o termo declarado
    e a palavra do titulo sao deformados igual. O que seria errado e normalizar
    so um dos lados.
    """
    p = sem_acento(bruto or '').lower()
    if len(p) >= 5 and p.endswith('s'):
        p = p[:-1]
    return p


def comparavel(texto):
    """O titulo numa forma em que `Torquês` e `torques` sao a mesma palavra.

    Sem acento, minusculo, sem plural, e todo caractere que nao e letra nem
    digito vira espaco — entao `30x30cm`, `30 x 30 cm` e `30X30` dao o mesmo
    campo de busca, e `2x2cm` nao esconde o `2` dentro de uma palavra maior.
    """
    return ' %s ' % ' '.join(
        palavra(p) for p in re.split(r'[^0-9A-Za-z]+', sem_acento(texto or '').lower()) if p)


def contem(titulo_comparavel, termo):
    """O termo aparece no titulo como PALAVRA (ou sequencia de palavras) inteira.

    Por que palavra inteira e nao `in` cru: `cola` esta dentro de `colar`, de
    `escola` e de `acrilico`, e `tela` esta dentro de `telha` — que nesta ilha
    e a diferenca entre a malha onde a pastilha vem presa e o alicate de
    azulejista. O `in` cru casaria pedaco de palavra e a regra passaria a
    aceitar e recusar por acidente de ortografia. Termo com espaco
    (`papel de parede`) continua funcionando, porque os dois lados foram
    normalizados do mesmo jeito.
    """
    alvo = ' '.join(
        palavra(p) for p in re.split(r'[^0-9A-Za-z]+', sem_acento(str(termo or '')).lower()) if p)
    if not alvo:
        return False
    return (' %s ' % alvo) in titulo_comparavel


def avaliar(titulo, declaracao):
    """SERVE ou nao, com o motivo escrito nas duas direcoes.

    `declaracao` e a entrada daquela consulta em `dados/consultas-de-produto.json`:
    `exige` (lista de grupos) e `recusa` (lista de termos).

    Devolve o dicionario que vai GRAVADO ao lado do anuncio no banco:

        {'serve': bool,
         'recusado_por': termo ou None,
         'exigencia_que_faltou': grupo ou None,
         'exigencias_atendidas': [termo que casou, por grupo]}

    Nenhum campo e opcional: anuncio aceito tambem diz POR QUE foi aceito, e e
    isso que faz a lista ser auditavel sem reabrir a Shopee.
    """
    campo = comparavel(titulo)

    # 1. A recusa roda PRIMEIRO e vence. Ver a assimetria no cabecalho.
    for termo in (declaracao.get('recusa') or []):
        if contem(campo, termo):
            return {
                'serve': False,
                'recusado_por': termo,
                'exigencia_que_faltou': None,
                'exigencias_atendidas': [],
            }

    # 2. Cada grupo de exigencia precisa de UM termo. Grupo vazio nao existe:
    #    ele passaria calado e tornaria a exigencia inteira decorativa.
    atendidas = []
    for grupo in (declaracao.get('exige') or []):
        termos = [t for t in (grupo or []) if str(t or '').strip()]
        if not termos:
            # GRUPO VAZIO E DECLARACAO QUEBRADA, nao titulo que nao casou, e as
            # duas coisas NAO podem sair com a mesma cara. A mutacao m05 de
            # 09/10/2026 mostrou por que este ramo precisa dizer algo proprio:
            # tirando-o, o `casou is None` logo abaixo derruba o grupo vazio do
            # mesmo jeito e com o mesmo diagnostico, entao o ramo era puro
            # enfeite — uma trava que a bancada nao tinha como medir porque ela
            # nao mudava nada. Com o marcador abaixo ele passa a separar
            # *"ninguem escreveu esta exigencia"* de *"este anuncio nao atende a
            # exigencia"*, que e a diferenca entre consertar o JSON e descartar
            # o anuncio.
            return {
                'serve': False,
                'recusado_por': None,
                'exigencia_que_faltou': [GRUPO_VAZIO],
                'exigencias_atendidas': atendidas,
            }
        casou = next((t for t in termos if contem(campo, t)), None)
        if casou is None:
            return {
                'serve': False,
                'recusado_por': None,
                'exigencia_que_faltou': termos,
                'exigencias_atendidas': atendidas,
            }
        atendidas.append(casou)

    # 3. Consulta sem nenhuma exigencia aceitaria o mundo. Falha fechada.
    if not atendidas:
        return {
            'serve': False,
            'recusado_por': None,
            'exigencia_que_faltou': ['<nenhuma exigencia declarada>'],
            'exigencias_atendidas': [],
        }

    return {
        'serve': True,
        'recusado_por': None,
        'exigencia_que_faltou': None,
        'exigencias_atendidas': atendidas,
    }
