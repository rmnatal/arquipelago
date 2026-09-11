#!/usr/bin/env python3
"""Deriva do banco os fatos que a CASCA publica sobre si mesma.

    python3 ferramentas/gerar-casca-fatos.py            # mostra
    python3 ferramentas/gerar-casca-fatos.py --gravar   # escreve dados/casca-fatos.json

POR QUE ESTE ARQUIVO EXISTE
---------------------------
A pagina de metodologia publica a escada de fontes com uma coluna "Temos hoje",
e essa coluna e uma AFIRMACAO SOBRE O BANCO: ela diz em quais degraus a ilha se
apoia e quais estao vazios. Ate 11/09/2026 ela estava digitada dentro do
snippet — `'existe' => false` no nivel 2 — enquanto QUATRO fontes do banco se
declaravam nivel 2. As duas metades nunca se falavam, entao nenhuma podia
corrigir a outra, e a contradicao ficou no ar sem que ninguem tivesse como
perceber.

E o mesmo defeito que o bloco 5 ja tinha nomeado no artigo-ancora: numero que e
a afirmacao da pagina nao pode estar digitado no HTML, porque passa a mentir em
silencio no dia em que o banco muda. A saida e a mesma: o gerador deriva o fato,
o snippet so escreve a frase.

POR QUE UM ARQUIVO NOVO, E NAO LER O BANCO NO SITE
--------------------------------------------------
`pecas.json` e `modelos-robo.json` tem `publicar: false` de proposito — sao 245
KB de banco cru que o site nao precisa carregar em option. Entao o fato viaja
derivado e pequeno, como `a1-fatos.json` e `a2-fatos.json` ja viajam.

A CONTAGEM E SO DE REGISTRO PUBLICAVEL, e isso importa: a coluna fala do que a
ilha publica, nao do que ela guarda. Fonte presa a registro excluido do banco
nao sustenta nada na tela e nao pode aparecer na confissao.

E ELA LE TODAS AS ORIGENS, NAO SO O BANCO DE PECAS
---------------------------------------------------
A primeira versao deste gerador contava `pecas.json` e `modelos-robo.json` e
declarava, com ar de medicao, que a ilha nao tinha fonte editorial — quando ela
tem seis, em `constantes.json`, usadas pela R2 em TODA resposta de Pa. Teria
trocado um numero digitado errado por um numero medido errado, que e pior,
porque este parece conferido.

As constantes nao carregam `nivel`, carregam `tipo`. A ponte entre os dois nao
mora aqui: mora no esquema, em `escada_de_fontes.onde_moram_as_fontes`, para ser
uma regra declarada e revisavel em vez de um dicionario escondido numa
ferramenta.

A SECAO 4 DA METODOLOGIA ENTROU AQUI EM 11/09/2026, e por dois motivos
--------------------------------------------------------------------
O primeiro e o mesmo de sempre: os sete numeros da tabela "O que medimos sobre a
nossa propria cobertura" estavam DIGITADOS dentro de robometria_casca_numeros(),
e um deles ja tinha deixado de ser verdade — a linha "pares peca x modelo, todos
declarados" dizia 33 e o banco de hoje tem 32 pelo criterio que a propria frase
anuncia. O par que sobrava aponta para um modelo `excluido_do_banco`: ele existe
no arquivo e o site nunca serve. Contar o que a ilha GUARDA numa frase que fala
do que ela PUBLICA e a mesma familia de defeito do cartao que dizia zero.

O segundo e um defeito latente que a Sentinela ja tinha nomeado e que nunca
disparou por sorte: a funcao lia `get_option('robometria_dados_cobertura-r1')`
para corrigir quatro dos numeros, e `cobertura-r1` tem `publicar: false` no
manifest — a option NUNCA existe no site. Quer dizer: no ar, os sete numeros
sempre vieram do valor digitado, e o caminho "derivado" era decoracao. Estavam
certos porque alguem os copiou a mao no dia certo. Agora eles viajam dentro de
casca-fatos.json, que e publicavel, e o caminho digitado deixou de existir.

A DATA DA MEDICAO E A DA VARREDURA, NUNCA A DO BANCO. O `gerado_em` de
cobertura-r1.json e herdado do banco (a data em que as pecas foram colhidas).
Publicar um pelo outro daria ao leitor uma data que nao e a do numero.

E O GERADOR RECUSA COBERTURA VELHA. Os numeros de cobertura da R1 vem de
cobertura-r1.json, que e derivado por outra ferramenta; se o banco andou e ele
nao, publicariamos medicao de ontem com data de hoje. Entao os dois numeros
baratos que da para recontar aqui — modelos e pecas publicaveis — sao
reconferidos contra o banco, e divergencia RECUSA a geracao em vez de gravar.
"""

import collections
import datetime
import json
import sys

ARQUIVOS = ('dados/pecas.json', 'dados/modelos-robo.json')
ESQUEMA = 'dados/esquema-banco.json'
COBERTURA_R1 = 'dados/cobertura-r1.json'


def medir_o_banco():
    """Os numeros da secao 4 da metodologia, contados no banco commitado.

    A REGUA DE CADA UM ESTA ESCRITA AQUI, e nao em quem consome o numero:
      marcas              marcas distintas que aparecem em registro publicavel
      modelos_publicaveis registros de modelo com status publicavel
      pecas_publicaveis   registros de peca com status publicavel
      pares_declarados    par (peca publicavel, modelo publicavel) com selo
                          declarada_fabricante. As DUAS pontas publicaveis: par
                          que aponta para modelo excluido do banco nao chega a
                          tela nenhuma
      esperando_link      registro publicavel (modelo ou peca) com afiliado.url
                          vazio — a contagem que a secao 7 do contrato manda
                          reportar em todo bloco
    """
    modelos = json.load(open('dados/modelos-robo.json', encoding='utf-8'))['registros']
    pecas = json.load(open('dados/pecas.json', encoding='utf-8'))['registros']

    modelos_pub = [r for r in modelos if r.get('status') == 'publicavel']
    pecas_pub = [r for r in pecas if r.get('status') == 'publicavel']
    ids_pub = {r['id'] for r in modelos_pub}

    pares = 0
    for peca in pecas_pub:
        for c in peca.get('compatibilidade') or []:
            if c.get('selo') == 'declarada_fabricante' and c.get('modelo') in ids_pub:
                pares += 1

    itens = modelos_pub + pecas_pub
    esperando = sum(1 for r in itens if not (r.get('afiliado') or {}).get('url'))

    return {
        'marcas': len({r['marca'] for r in itens if r.get('marca')}),
        'modelos_publicaveis': len(modelos_pub),
        'pecas_publicaveis': len(pecas_pub),
        'pares_declarados': pares,
        'itens_publicaveis': len(itens),
        'esperando_link': esperando,
    }


def cobertura_da_r1(medido):
    """O que so a varredura da R1 sabe, lido de cobertura-r1.json — e conferido.

    Devolve (numeros, recusas). Recusa nao e aviso: com ela, nada e gravado.
    """
    with open(COBERTURA_R1, encoding='utf-8') as f:
        cob = json.load(f)

    resumo = cob.get('resumo') or {}
    cruz = (cob.get('cruzamento_com_a_r2') or {}).get('contagem') or {}

    recusas = []
    if resumo.get('modelos_publicaveis') != medido['modelos_publicaveis']:
        recusas.append(
            'cobertura-r1.json diz %r modelos publicaveis e o banco tem %d — '
            'rode ferramentas/cobertura-r1.py de novo'
            % (resumo.get('modelos_publicaveis'), medido['modelos_publicaveis'])
        )
    soma = sum(int(v) for v in cruz.values()) if cruz else -1
    if soma != medido['modelos_publicaveis']:
        recusas.append(
            'o cruzamento com a R2 soma %d modelos e o banco tem %d'
            % (soma, medido['modelos_publicaveis'])
        )

    faltando = [c for c in ('celulas_total',) if c not in resumo]
    if faltando:
        recusas.append('cobertura-r1.json sem os campos %s' % ', '.join(faltando))

    numeros = {
        'r1_responde': resumo.get('modelos_que_respondem'),
        'r1_vazia': resumo.get('modelos_com_entrada_vazia'),
        'celulas': resumo.get('celulas_total'),
        'celulas_sem_resposta': (resumo.get('celulas') or {}).get('vazia'),
        'as_duas': cruz.get('as_duas'),
    }
    for chave, valor in numeros.items():
        if not isinstance(valor, int):
            recusas.append('cobertura-r1.json nao tem %s' % chave)

    return numeros, recusas


def main():
    gravar = '--gravar' in sys.argv

    with open(ESQUEMA, encoding='utf-8') as f:
        escada = json.load(f)['escada_de_fontes']

    contagem = collections.Counter()
    por_origem = collections.Counter()
    fora_do_vocabulario = []

    origem_do_nivel = {d['nivel']: d['origem'] for d in escada['niveis']}

    for arquivo in ARQUIVOS:
        with open(arquivo, encoding='utf-8') as f:
            banco = json.load(f)
        for registro in banco['registros']:
            if registro.get('status') != 'publicavel':
                continue
            for fid, fonte in (registro.get('fontes') or {}).items():
                nivel = fonte.get('nivel')
                contagem[nivel] += 1
                por_origem[(nivel, fonte.get('origem'))] += 1
                if origem_do_nivel.get(nivel) != fonte.get('origem'):
                    fora_do_vocabulario.append(
                        '%s/%s/%s: nivel %s declara origem %r, e a escada diz %r'
                        % (arquivo, registro['id'], fid, nivel,
                           fonte.get('origem'), origem_do_nivel.get(nivel))
                    )

    # As constantes: mesma escada, outro arquivo, e a ponte tipo -> nivel e
    # declarada no esquema, nao aqui.
    onde = escada['onde_moram_as_fontes']
    ponte = onde['tipo_de_constante_para_nivel']
    with open('dados/constantes.json', encoding='utf-8') as f:
        constantes = json.load(f)['constantes']
    for constante in constantes:
        if constante.get('status') != 'publicavel':
            continue
        tipo = constante.get('tipo')
        if tipo not in ponte:
            fora_do_vocabulario.append(
                'dados/constantes.json/%s: tipo %r nao esta na ponte declarada no esquema'
                % (constante.get('id'), tipo)
            )
            continue
        nivel = ponte[tipo]
        if nivel is None:
            continue
        contagem[nivel] += 1
        por_origem[(nivel, origem_do_nivel.get(nivel))] += 1

    if fora_do_vocabulario:
        print('RECUSADO: fonte com nivel e origem que nao batem com a escada.')
        for linha in fora_do_vocabulario:
            print('  ' + linha)
        return 2

    niveis = []
    for degrau in escada['niveis']:
        niveis.append({
            'nivel': degrau['nivel'],
            'origem': degrau['origem'],
            'fontes_no_banco': contagem.get(degrau['nivel'], 0),
            'existe_hoje': contagem.get(degrau['nivel'], 0) > 0,
        })

    medido = medir_o_banco()
    cobertura, recusas = cobertura_da_r1(medido)
    if recusas:
        print('RECUSADO: a cobertura da R1 nao bate com o banco de hoje.')
        for linha in recusas:
            print('  ' + linha)
        return 2

    hoje = datetime.date.today().isoformat()
    medicao = dict(medido)
    medicao.update(cobertura)
    medicao['medido_em'] = hoje

    fatos = {
        'id': 'casca-fatos',
        'ilha': 'robometria',
        'entidade': 'medicao',
        'gerado_por': 'ferramentas/gerar-casca-fatos.py',
        'gerado_em': hoje,
        'o_que_e': (
            'Fatos que a casca publica sobre o proprio banco. Hoje: a coluna "Temos hoje" da '
            'escada de fontes, na pagina de metodologia. Contagem so de registro publicavel.'
        ),
        'por_que_derivado': (
            'Ate 11/09/2026 a coluna estava digitada dentro do snippet e contradizia o banco: '
            'ela dizia que a ilha nao tinha nenhuma fonte de nivel 2 enquanto quatro fontes se '
            'declaravam nivel 2. Afirmacao da pagina sobre o banco se conta no banco.'
        ),
        'onde_foi_contado': onde['arquivos_com_fontes_de_nivel_explicito'] + ['dados/constantes.json'],
        'total_de_fontes': sum(contagem.values()),
        'niveis': niveis,
        'medicao': medicao,
        'reguas_da_medicao': {
            'marcas': 'marcas distintas em registro publicavel de modelo ou peca',
            'modelos_publicaveis': 'registros de dados/modelos-robo.json com status publicavel',
            'pecas_publicaveis': 'registros de dados/pecas.json com status publicavel',
            'pares_declarados': (
                'par (peca publicavel, modelo publicavel) com selo declarada_fabricante. '
                'As duas pontas publicaveis: par que aponta para modelo excluido do banco '
                'nao chega a tela nenhuma'
            ),
            'esperando_link': 'registro publicavel, modelo ou peca, com afiliado.url vazio',
            'r1_responde': 'cobertura-r1.json, modelos_que_respondem',
            'r1_vazia': 'cobertura-r1.json, modelos_com_entrada_vazia',
            'celulas': 'cobertura-r1.json, celulas_total (modelo x tipo de peca)',
            'celulas_sem_resposta': 'cobertura-r1.json, celulas.vazia',
            'as_duas': 'cobertura-r1.json, cruzamento_com_a_r2.contagem.as_duas',
            'medido_em': 'a data desta varredura, nunca a data em que o banco foi colhido',
        },
    }

    for n in niveis:
        print('  nivel %d %-24s %3d fonte(s)  existe_hoje=%s'
              % (n['nivel'], n['origem'], n['fontes_no_banco'], n['existe_hoje']))
    print('  total: %d fontes em registro publicavel' % fatos['total_de_fontes'])
    print('\n  medicao da secao 4 da metodologia:')
    for chave in sorted(medicao):
        print('    %-22s %s' % (chave, medicao[chave]))

    if gravar:
        with open('dados/casca-fatos.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(fatos, ensure_ascii=False, indent=2) + '\n')
        print('\ngravado: dados/casca-fatos.json')
    else:
        print('\n(nada gravado — rode com --gravar)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
