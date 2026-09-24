#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A REGUA DA LISTA DE PROSPECCAO DO WIDGET — o que a lista pode afirmar.

Nao e portao. E a regua que tres arquivos carregam: `validar-prospeccao.py`
(o portao sobre o arquivo de verdade), `teste-prospeccao.py` (a bancada, sobre
casos sinteticos) e `gerar-prospeccao.py` (a producao, que escreve o `.md`).
Mora num arquivo proprio pelo motivo que esta ilha ja pagou varias vezes: regua
escrita duas vezes erra em um dos lados, e o lado errado fica verde.

POR QUE ELA NASCEU EM 24/09/2026
--------------------------------
O bloco T6 (secao 14.7 do contrato) e a UNICA alavanca de link deste projeto, e
estava parado desde que subiu de prioridade. A leitura semanal de 23/09 apontou
para ele com todas as letras: `/peixes/tetras/` esta em "Discovered - currently
not indexed" havia 11 dias, nao e falta de descoberta nem `noindex`, e a alavanca
que sobra e sinal externo.

E O INSTRUMENTO DESTA NUVEM E UM SO, o que decide tudo o que esta escrito aqui:
o egresso responde 403 no CONNECT para todo dominio fora da lista de permitidos
(medido tres vezes em 24/09/2026, com aquametria.com.br em 200 nas mesmas tres),
e o WebFetch devolve EGRESS_BLOCKED. Ninguem abre o site de ninguem daqui. O que
existe e BUSCA — o nivel 3 da escada de coleta desta ilha, que e como este banco
inteiro foi construido, e nao um atalho.

AS QUATRO REGRAS QUE ISSO IMPOE, e todas elas sao sobre NAO AFIRMAR DEMAIS
-------------------------------------------------------------------------
  1. NAO EXISTE `false` NOS CAMPOS DE FATO. Busca sabe afirmar presenca, nunca
     ausencia: um dominio nao aparecer na consulta de calculadora nao prova que
     ele nao tem calculadora — prova que a busca nao o mostrou. Entao
     `vende_equipamento`, `publica_conteudo` e `ja_tem_calculadora` sao `true`
     (com evidencia) ou `null` (= nao medido). `false` e RECUSADO.
  2. EVIDENCIA TEM DE SER DO DOMINIO QUE ELA SUSTENTA. O host do
     `resultado_url` tem de terminar no dominio do candidato. E a trava
     anti-invencao: resultado que fala de outro site nao prova nada sobre este,
     e sem esta regra a lista aceitaria qualquer URL colada em qualquer linha.
  3. A PRIORIDADE NAO SE ESCREVE, SE CALCULA. A lista diz o numero e o portao
     RECALCULA dos campos medidos; se os dois discordarem, o portao fica
     vermelho. E a mesma doenca que a `bancada.py` matou um andar acima: lista
     escrita a mao envelhece calada. Quem mudar um campo medido nao precisa
     lembrar de mexer na prioridade — ela vem do campo.
  4. O QUE NAO FOI MEDIDO TEM DE DIZER QUE NAO FOI. `contato` e `plataforma`
     sao `null` nesta passada, e `null` exige MOTIVO escrito. Campo vazio sem
     motivo e onde a proxima passada inventa um e-mail.

E A PORTA DOS FUNDOS QUE FICOU FECHADA JUNTO, aprendida no portao do espelho do
CDN em 24/09/2026, quatro horas antes: `abriu_no_navegador` ausente NAO vale como
`false`. Se o campo pudesse faltar, a lista ganharia um estado em que ninguem
sabe se alguem abriu o site — e "ninguem abriu" e justamente a limitacao que
este arquivo existe para deixar visivel. Ausencia e reprovacao, nao omissao
tolerada.
"""

# O TETO POR TIPO. O que esta medido e o tipo; o teto e JUIZO, e esta escrito
# aqui para poder ser contestado em vez de ficar na cabeca de quem ordenou.
#   loja          -> 1. A oferta do widget e "uma ferramenta que recomenda
#                    equipamento, ao lado do equipamento que voce vende".
#   fabricante    -> 2. Vende pouco direto ao leitor, mas declara faixa e e
#   distribuidora     fonte de dado; alcança lojas em vez de leitores.
#   conteudo      -> 2. Tem onde publicar e nao tem o que vender: a ferramenta
#                    ajuda a pagina, nao o caixa.
#   rede-pet      -> 3. Rede nacional tem equipe editorial propria, fornecedor
#                    homologado e juridico. Dominio novo nao atravessa isso.
#   desconhecido  -> 3. Prospeccao que nao sabe com quem fala escreve texto
#                    errado. Nao saber e motivo para descer, nunca para chutar.
TETO_POR_TIPO = {
    'loja': 1,
    'fabricante': 2,
    'distribuidora': 2,
    'conteudo': 2,
    'rede-pet': 3,
    'desconhecido': 3,
}

CAMPOS_DE_FATO = ('vende_equipamento', 'publica_conteudo', 'ja_tem_calculadora')
CAMPOS_COM_EVIDENCIA = ('dominio', 'tipo') + CAMPOS_DE_FATO
INSTRUMENTOS = ('busca', 'navegador', 'curl')

# Dominio que NAO e site proprio. Vitrine dentro de marketplace ou de rede
# social nao serve de alvo de prospeccao por dois motivos independentes: o link
# de la nao passa autoridade (e `nofollow` por politica da plataforma) e a
# pagina nao e da loja, e sim da plataforma — ela nao pode instalar nada.
NAO_E_SITE_PROPRIO = (
    'mercadolivre.com.br', 'mercadolivre.com', 'shopee.com.br', 'amazon.com.br',
    'americanas.com.br', 'magazineluiza.com.br', 'elo7.com.br', 'olx.com.br',
    'instagram.com', 'facebook.com', 'youtube.com', 'tiktok.com',
    'wa.me', 'linktr.ee',
)


def prioridade(candidato):
    """A prioridade CALCULADA. Nunca a escrita no arquivo.

    A base sai do cruzamento que a secao 14.9 manda usar — intencao de compra x
    chance real —, traduzido para o que a busca consegue medir: quem vende o
    equipamento que as calculadoras dimensionam TEM interesse; quem publica
    conteudo proprio TEM onde por a ferramenta. As duas juntas e a unica
    combinacao que chega a 1.

    E quem JA TEM calculadora cai para 3 seja quem for: ninguem instala a
    ferramenta de outro tendo a propria. Este e o achado que reordenou a lista
    inteira em 24/09/2026, e por isso e a PRIMEIRA linha da funcao.
    """
    if candidato.get('ja_tem_calculadora') is True:
        base = 3
    elif candidato.get('vende_equipamento') is True and candidato.get('publica_conteudo') is True:
        base = 1
    elif candidato.get('vende_equipamento') is True or candidato.get('publica_conteudo') is True:
        base = 2
    else:
        base = 3
    teto = TETO_POR_TIPO.get(candidato.get('tipo'), 3)
    return max(base, teto)


def host_de(url):
    """O host de uma URL, sem esquema, sem porta, sem caminho, minusculo."""
    resto = url.split('://', 1)[-1]
    return resto.split('/', 1)[0].split('?', 1)[0].split('@')[-1].split(':', 1)[0].lower()


def do_dominio(url, dominio):
    """O host da URL e o dominio, ou subdominio dele?

    `loja.forfish.com.br` conta para `forfish.com.br` — subdominio proprio e
    site proprio. `forfish.com.br.exemplo.com` NAO conta, e e por isso que a
    comparacao e por rotulo e nao por `endswith` de texto cru.
    """
    host = host_de(url)
    dominio = dominio.lower()
    return host == dominio or host.endswith('.' + dominio)


def campos_afirmados(candidato):
    """Os campos que a linha AFIRMA, e que por isso precisam de evidencia."""
    return [c for c in CAMPOS_COM_EVIDENCIA
            if candidato.get(c) is not None and not (c == 'tipo' and candidato.get(c) == 'desconhecido')]


def erros_de_evidencia(alvo, dominio, rotulo):
    """As afirmacoes sobre UMA lista de evidencia. Devolve lista de mensagens."""
    erros = []
    evidencias = alvo.get('evidencia')
    if not isinstance(evidencias, list) or not evidencias:
        return ['%s: sem lista de evidencia' % rotulo]
    for i, ev in enumerate(evidencias):
        onde = '%s evidencia[%d]' % (rotulo, i)
        campos = ev.get('campos')
        if not isinstance(campos, list) or not campos:
            erros.append('%s: nao diz que campos sustenta' % onde)
        instrumento = ev.get('medido_como')
        if instrumento not in INSTRUMENTOS:
            erros.append('%s: instrumento desconhecido (%r)' % (onde, instrumento))
        elif instrumento != 'busca' and not ev.get('medido_por'):
            # Esta nuvem nao tem navegador e nao alcanca o egresso. Evidencia que
            # diz ter vindo de um dos dois tem de nomear QUEM mediu, senao e uma
            # afirmacao sem instrumento — o defeito que a 1.1 e a 20.2 pagam.
            erros.append('%s: %r sem `medido_por`; esta nuvem nao tem esse instrumento' % (onde, instrumento))
        if not ev.get('consulta'):
            erros.append('%s: sem a consulta que a produziu' % onde)
        if not ev.get('resultado_titulo'):
            erros.append('%s: sem o titulo do resultado' % onde)
        if not ev.get('medido_em'):
            erros.append('%s: sem data' % onde)
        url = ev.get('resultado_url')
        if not url:
            erros.append('%s: sem a URL do resultado' % onde)
        elif not do_dominio(url, dominio):
            erros.append('%s: a URL %s nao e do dominio %s' % (onde, url, dominio))
    return erros


# ---------------------------------------------------------------------------
# O `.md` E GERADO, NUNCA ESCRITO
# ---------------------------------------------------------------------------
# Duas fontes para o mesmo fato divergem — esta ilha mediu isso em 24/09/2026,
# quando o titulo de 38 paginas morava em dois arquivos e nada conferia se eles
# concordavam. Entao a lista de prospeccao tem UMA fonte (o JSON) e o `.md` sai
# dela por esta funcao. O portao regera em memoria e compara: `.md` editado a
# mao fica vermelho.
ROTULO_PRIORIDADE = {
    1: 'PRIORIDADE 1 — as tres condicoes medidas',
    2: 'PRIORIDADE 2 — uma condicao medida, ou teto de tipo',
    3: 'PRIORIDADE 3 — ja tem calculadora, tipo que nao atravessa, ou nada medido',
}


def _sim(valor):
    return 'sim' if valor is True else 'nao medido'


def render_md(dados):
    """O `.md` inteiro, a partir do JSON. Mesma fonte, uma so."""
    L = []
    L.append('# PROSPECCAO DO WIDGET — bloco T6, secao 14.7 do contrato')
    L.append('')
    L.append('> **ARQUIVO GERADO por `ferramentas/gerar-prospeccao.py` a partir de**')
    L.append('> **`dados/prospeccao-widget.json`. Nao edite a mao:** o portao')
    L.append('> `validar-prospeccao.py` regera este texto e compara, e edicao a mao')
    L.append('> fica vermelha. Mude o JSON e rode o gerador.')
    L.append('')
    L.append('Atualizado em **%s**. Nada aqui vai para o ar (`publicar: false`).' % dados['atualizado_em'])
    L.append('')
    L.append('## O QUE MEDIU ISTO, E O QUE ELE NAO ALCANCA')
    L.append('')
    L.append(dados['por_que_ninguem_abriu'])
    L.append('')
    L.append('**Ninguem abriu nenhum site: %s.** Entao `contato` e `plataforma` estao'
             % ('correto' if dados['ninguem_abriu_nenhum_site'] else 'FALSO'))
    L.append('`null` em todas as linhas, com o motivo escrito em cada uma. O proximo passo')
    L.append('desta lista NAO e da Fundacao: e abrir cada dominio num navegador, confirmar')
    L.append('canal de contato e plataforma, e so entao escrever a abordagem.')
    L.append('')
    L.append(dados['por_que_nao_existe_false'])
    L.append('')
    L.append('## O ACHADO QUE REORDENOU A LISTA')
    L.append('')
    ocupantes = dados['ocupantes_da_serp_de_calculadora']
    dominios_candidatos = {c['dominio'] for c in dados['candidatos']}
    lojas_com_calculadora = [o for o in ocupantes if o['dominio'] in dominios_candidatos]
    L.append('A consulta de calculadora de aquario em portugues do Brasil ja tem **%d**' % len(ocupantes))
    L.append('dominios publicando ferramenta — e **%d** deles e loja de aquarismo desta lista.'
             % len(lojas_com_calculadora))
    L.append('Os outros sao site de conteudo, fazenda de calculadora e um dominio de outro')
    L.append('nicho inteiro. Isso vale nas duas direcoes, e as duas estao medidas:')
    L.append('')
    L.append('- **Para a prospeccao:** loja que ja construiu a propria calculadora nao')
    L.append('  instala a de ninguem, e cai para prioridade 3 por regra, nao por opiniao.')
    L.append('  Das %d lojas prospectadas, %d tem calculadora medida.'
             % (sum(1 for c in dados['candidatos'] if c['tipo'] == 'loja'),
                sum(1 for c in dados['candidatos'] if c['tipo'] == 'loja' and c['ja_tem_calculadora'] is True)))
    L.append('- **Para a oferta:** a ferramenta que falta na loja brasileira de aquarismo e')
    L.append('  justamente esta. O espaco existe porque quase ninguem do lado do comercio')
    L.append('  a tem — e nao porque ninguem tentou.')
    L.append('')
    for nivel in (1, 2, 3):
        linhas = [c for c in dados['candidatos'] if c['prioridade'] == nivel]
        L.append('## %s' % ROTULO_PRIORIDADE[nivel])
        L.append('')
        if not linhas:
            L.append('*Nenhum candidato neste nivel.*')
            L.append('')
            continue
        L.append('| dominio | tipo | vende equipamento | publica conteudo | ja tem calculadora |')
        L.append('|---|---|---|---|---|')
        for c in sorted(linhas, key=lambda x: x['dominio']):
            L.append('| `%s` | %s | %s | %s | %s |' % (
                c['dominio'], c['tipo'], _sim(c['vende_equipamento']),
                _sim(c['publica_conteudo']), _sim(c['ja_tem_calculadora'])))
        L.append('')
        for c in sorted(linhas, key=lambda x: x['dominio']):
            L.append('**%s** (`%s`) — %s' % (c['nome'], c['dominio'], c['porque']))
            L.append('')
    L.append('## QUEM JA OCUPA A SERP DE CALCULADORA')
    L.append('')
    L.append('Medido pelas tres consultas de calculadora desta passada. Nao e lista de')
    L.append('alvo: e o mapa de quem ja esta la, e serve tanto para a oferta do widget')
    L.append('quanto para quem for ler SERP depois.')
    L.append('')
    L.append('| dominio | o que publica |')
    L.append('|---|---|')
    for o in sorted(ocupantes, key=lambda x: x['dominio']):
        L.append('| `%s` | %s |' % (o['dominio'], o['o_que_publica']))
    L.append('')
    L.append('## O QUE ESTA LISTA NAO E')
    L.append('')
    L.append('- **Nao e lista de link para publicar.** Nenhuma linha daqui vira link no')
    L.append('  site. A secao 10 do contrato proibe troca de link, PBN e diretorio, e a')
    L.append('  unica alavanca permitida e o widget INSTALADO por quem quis instalar.')
    L.append('- **Nao e diagnostico da 21.5.** O item 2 do despacho da Sentinela pede um')
    L.append('  diagnostico de consulta e SERP escrito DEPOIS da leitura semanal de')
    L.append('  30/09/2026, e sobre as consultas `quantos litros para <especie>`. As tres')
    L.append('  consultas desta passada sao de CALCULADORA, para a prospeccao. Escrever o')
    L.append('  diagnostico agora seria escrever o critério antes do dado.')
    L.append('- **Nao e contato.** Ninguem foi abordado, e a Fundacao nao abre conta, nao')
    L.append('  escreve e-mail e nao fala com loja nenhuma.')
    return '\n'.join(L) + '\n'
