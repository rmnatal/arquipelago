#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGUA COMPARTILHADA: como cada arquivo de `ferramentas/` NOMEIA o irmao em
que ele age — literal no sitio do ato, literal alcancado por indirecao, ou nome
CONSTRUIDO que nao existe no texto.

Nao afirma nada sozinha e nao abre rede. Quem a exercita e o
`teste-alvos-de-portao.py`; quem a mutila e o `mutacoes-alvos-de-portao.py`.

POR QUE ESTE ARQUIVO EXISTE, e a data e 20/10/2026
---------------------------------------------------
O item 7 do fecho de 20/10/2026 (10h17Z), deixado sem conserto de proposito
pela 19.2. A `regua-classes-da-bancada.py` diz, na propria docstring, que **a
classe sai do TEXTO do arquivo e nao de executa-lo** — e deixou a pergunta
escrita em vez de a responder: *"quantos portoes desta pasta hoje nomeiam o
alvo deles por concatenacao ou variavel em vez de literal? A varredura por nome
e cega para todos eles, nos tres classificadores de uma vez."*

A pergunta vale porque os tres classificadores daquela regua sao, os tres, uma
varredura por nome:

  * `dirige_navegador()` procura a marca do navegador no texto;
  * `exercitada_por_portao()` procura o NOME do irmao no texto de quem o carrega;
  * `declara_sem_rede()` procura a declaracao no cabecalho.

Alvo cujo nome nunca e escrito no arquivo e invisivel para os tres de uma vez.

A RESPOSTA, E ELA TEM DUAS METADES QUE NAO SE PODE SOMAR
---------------------------------------------------------
**Nenhum ato desta pasta e invisivel hoje** — toda indirecao termina num
literal escrito no mesmo arquivo, entao a varredura por nome enxerga todos.
**E a indirecao EXISTE**: ha atos que so chegam ao literal por variavel,
parametro, chave de dicionario ou juncao de caminho. Para esses, a visibilidade
e um ACIDENTE do literal estar escrito ali por outro motivo — ninguem a
sustenta, e um renomeio que apague o literal a derruba em silencio.

Por isso esta regua conta as duas coisas separadas. `invisiveis()` e a que tem
dentes e tem de continuar vazia; `indiretos()` e registro, e o numero dele
mede o quanto da visibilidade de hoje e sorte.

A CONTA DE 20/10/2026, medida por esta regua na pasta desta ilha
-----------------------------------------------------------------
196 atos sobre irmao em 141 arquivos: **48 literais, 142 indiretos, 6
construidos** — e **ZERO invisiveis**. Dos 196, **148 sao visiveis so por
acidente**: o literal esta no arquivo, mas o ato nao passa por ele. 10 sitios
que falam da pasta ficaram por resolver, **nenhum deles uma carga**, e 40
arquivos (os `.mjs` e os `.php`) estao fora do alcance desta regua.

Estes numeros sao de uma DATA e envelhecem com a pasta — quem quiser o de hoje
roda `python3 ferramentas/regua-alvos-de-portao.py`, que os imprime. O que o
portao cobra nao e nenhum deles: e a propriedade de `invisiveis()` continuar
vazia, que nao envelhece.

A leitura, em uma frase: **a varredura por nome nao esta cega hoje, e ela nao
esta cega por sorte em tres de cada quatro atos.** Nao ha o que consertar — ha
o que impedir, e e por isso que esta regua nasceu com portao em vez de virar
numero num registro.

A POSICAO ERRA PARA BAIXO DE PROPOSITO
---------------------------------------
Quando um nome passa por molde com buraco (f-string, `%`, `.replace()`), esta
regua o chama de CONSTRUIDO mesmo que o pedaco literal esteja escrito ali ao
lado — ela nao executa molde nenhum e nao vai fingir que sabe o que sai. Quem
decide se ha buraco DE VERDADE e a coluna `visivel`, que e medida contra o
texto e nao inferida. Posicao e um piso; `visivel` e o fato.

O ATO, E SO ESTES TRES CONTAM
------------------------------
  * **carrega**: `spec_from_file_location(apelido, <alvo>)`, o idioma de carga
    desta pasta.
  * **invoca**: `subprocess.run([... <alvo> ...])` e as irmas.
  * **abre**: `open(<alvo>)` — e o que os `mutacoes-*` fazem com o portao que
    mutilam, e e ato sobre irmao tanto quanto os outros dois.

`open()` de JSON em `dados/` nao e ato sobre irmao e nao entra: os tres
classificadores nao perguntam nada sobre ele.

O LIMITE, escrito em vez de descoberto depois
----------------------------------------------
  * **So le PYTHON.** A arvore sintatica e a do Python, entao `.mjs` e `.php`
    desta pasta ficam de fora — e eles tambem agem sobre irmaos. Esta regua nao
    promete cobertura; promete que o que ela mede, mede sem adivinhar.
  * **Resolucao parcial e declarada, nunca aprovada em silencio.** Sitio cujo
    alvo esta fora do alcance da dobra de constantes sai em `nao_resolvidos()`,
    com o texto da expressao, do mesmo jeito que a 20.4 manda registrar o item
    que rolou para fora da janela do log em vez de aprovar com cara de
    completo. Carga nao resolvida e o caso perigoso e tem afirmacao propria no
    portao.
  * **A pasta e dado.** Quem le o disco e `ler_pasta()`; tudo o mais recebe
    `{nome: texto}`, para o portao poder encenar pasta que nao existe.
"""

import ast
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXTENSOES = ('.py', '.mjs', '.php')

# Os tres atos, pelo nome da chamada que os escreve nesta pasta.
CARGA = 'spec_from_file_location'
INVOCACOES = ('run', 'check_output', 'Popen', 'call', 'check_call')
LEITURA = 'open'

# Chamadas que so COMPOEM caminho: atravessa-las nao e indirecao, porque o nome
# continua escrito ali dentro.
COMPOSICAO = ('join', 'abspath', 'dirname', 'normpath', 'realpath', 'str', 'Path', 'resolve')

# Chamadas que PRODUZEM nome novo: o que sai delas pode nao existir no texto.
PRODUCAO = ('replace', 'format', 'lower', 'upper', 'strip')

# As tres posicoes de nome, da mais forte para a mais fraca.
LITERAL = 'literal'        # o nome esta escrito no proprio sitio do ato
INDIRETO = 'indireto'      # chega-se a ele por variavel, parametro ou chave
CONSTRUIDO = 'construido'  # sai de concatenacao, f-string, % ou .replace()


# Caracter de PADRAO, nunca de nome. `*.php` passa pelo teste de extensao e
# pelo de tamanho, e dai em diante e tratado como se fosse um arquivo: o sitio
# conta como RESOLVIDO e sai da lista do que nao resolveu, mas o "nome" nunca
# esta na pasta, entao o ato tambem nao entra na conta. O sitio DESAPARECE das
# duas listas de uma vez, que e a pior coisa que uma regua pode fazer.
#
# MEDIDO EM 20/10/2026 as 16h4xZ, e nao foi leitura: foi a `regua-alvos-em-php.py`
# nascendo com uma COPIA desta funcao e o portao dela reprovando no mundo
# `foreach ( glob( __DIR__ . '/*.php' ) as $f ) { require $f; }` — uma carga por
# varredura de pasta, que e idioma real desta pasta. Aqui o defeito estava
# ESCONDIDO por acidente de aritmetica: `*.py` tem 4 caracteres e o `> 4` o
# barrava; `*.php` tem 5 e passa. Dois `glob` de `snippets/*.php` desta pasta
# (na `bancada.py` e no `conferir-protecao-funcoes.py`) ja caiam nele, e nao
# mudavam a conta so porque nao falam de `ferramentas/`.
PADRAO = ('*', '?', '[')


def _base(s):
    """O ultimo degrau de um caminho literal, se ele parecer arquivo desta pasta."""
    if not isinstance(s, str):
        return None
    ultimo = s.replace('\\', '/').split('/')[-1]
    if any(c in ultimo for c in PADRAO):
        return None
    return ultimo if ultimo.endswith(EXTENSOES) and len(ultimo) > 4 else None


class Arquivo:
    """A arvore de UM arquivo, com o que e preciso para seguir um nome ate o
    literal: as atribuicoes, os parametros e os sitios de chamada de cada
    funcao deste mesmo arquivo. Nao atravessa fronteira de arquivo — quem
    quisesse isso estaria executando o codigo, e a regua nao executa nada."""

    def __init__(self, texto):
        self.texto = texto or ''
        self.arvore = ast.parse(self.texto)
        self.atribuicoes = {}
        for no in ast.walk(self.arvore):
            if isinstance(no, ast.Assign):
                for alvo in no.targets:
                    if isinstance(alvo, ast.Name):
                        self.atribuicoes.setdefault(alvo.id, []).append(no.value)
                    elif isinstance(alvo, (ast.Tuple, ast.List)):
                        for e in alvo.elts:
                            if isinstance(e, ast.Name):
                                self.atribuicoes.setdefault(e.id, []).append(no.value)
        self.funcoes = {n.name: n for n in ast.walk(self.arvore)
                        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        self.chamadas = {}
        for no in ast.walk(self.arvore):
            if isinstance(no, ast.Call) and isinstance(no.func, ast.Name):
                self.chamadas.setdefault(no.func.id, []).append(no)
        self.indice_do_parametro = {}
        self.dono = {}
        for nome, fn in self.funcoes.items():
            for i, a in enumerate(fn.args.args):
                self.indice_do_parametro[(nome, a.arg)] = i
            for no in ast.walk(fn):
                self.dono[id(no)] = nome

    # -----------------------------------------------------------------
    def resolver(self, no, prof=0, vistos=frozenset()):
        """-> {nome_de_arquivo: posicao}. Posicao e a MAIS FORTE encontrada."""
        if no is None or prof > 8:
            return {}
        if isinstance(no, ast.Constant):
            b = _base(no.value)
            return {b: LITERAL} if b else {}
        if isinstance(no, ast.JoinedStr):
            achados = {}
            for p in no.values:
                if isinstance(p, ast.Constant):
                    b = _base(p.value)
                    if b:
                        achados[b] = LITERAL
            # f-string com buraco produz nome que pode nao existir no texto
            if any(isinstance(p, ast.FormattedValue) for p in no.values):
                return self._rebaixar(achados, CONSTRUIDO) or {}
            return achados
        if isinstance(no, ast.BinOp):
            if isinstance(no.op, ast.Div):            # pathlib: base / 'x.py'
                return self._uniao(self.resolver(no.left, prof + 1, vistos),
                                   self.resolver(no.right, prof + 1, vistos))
            if isinstance(no.op, ast.Add):            # concatenacao
                junto = self.dobrar(no)
                if junto is not None:
                    b = _base(junto)
                    return {b: CONSTRUIDO} if b else {}
                return self._rebaixar(
                    self._uniao(self.resolver(no.left, prof + 1, vistos),
                                self.resolver(no.right, prof + 1, vistos)), CONSTRUIDO)
            if isinstance(no.op, ast.Mod):            # 'regua-%s.py' % x
                return self._rebaixar(self.resolver(no.left, prof + 1, vistos), CONSTRUIDO)
            return {}
        if isinstance(no, ast.Call):
            ultimo = ast.unparse(no.func).split('.')[-1]
            if ultimo in COMPOSICAO:
                achados = {}
                for a in no.args:
                    achados = self._uniao(achados, self.resolver(a, prof + 1, vistos))
                return achados
            if ultimo in PRODUCAO:
                alvo = no.func.value if isinstance(no.func, ast.Attribute) else None
                return self._rebaixar(self.resolver(alvo, prof + 1, vistos), CONSTRUIDO)
            return {}
        if isinstance(no, ast.Subscript):             # PAGINAS[ALVO] e MUTACOES[i]
            return self._rebaixar(self.resolver(no.value, prof + 1, vistos), INDIRETO)
        if isinstance(no, ast.BoolOp):            # caminho or <padrao>
            achados = {}
            for v in no.values:
                achados = self._uniao(achados, self.resolver(v, prof + 1, vistos))
            return achados
        if isinstance(no, ast.IfExp):             # o ternario que monta comando
            return self._uniao(self.resolver(no.body, prof + 1, vistos),
                               self.resolver(no.orelse, prof + 1, vistos))
        if isinstance(no, (ast.Tuple, ast.List, ast.Set)):
            achados = {}
            for e in no.elts:
                achados = self._uniao(achados, self.resolver(e, prof + 1, vistos))
            return achados
        if isinstance(no, ast.Dict):
            achados = {}
            for v in no.values:
                achados = self._uniao(achados, self.resolver(v, prof + 1, vistos))
            return achados
        if isinstance(no, ast.Name):
            if no.id in vistos:
                return {}
            vistos = vistos | {no.id}
            achados = {}
            for valor in self.atribuicoes.get(no.id, []):
                achados = self._uniao(achados, self.resolver(valor, prof + 1, vistos))
            dono = self.dono.get(id(no))
            if dono is not None and (dono, no.id) in self.indice_do_parametro:
                i = self.indice_do_parametro[(dono, no.id)]
                for ch in self.chamadas.get(dono, []):
                    if i < len(ch.args):
                        achados = self._uniao(achados, self.resolver(ch.args[i], prof + 1, vistos))
                    for kw in ch.keywords:
                        if kw.arg == no.id:
                            achados = self._uniao(achados, self.resolver(kw.value, prof + 1, vistos))
            return self._rebaixar(achados, INDIRETO)
        return {}

    def dobrar(self, no):
        """Concatenacao so de constantes -> a string inteira; senao None."""
        if isinstance(no, ast.Constant) and isinstance(no.value, str):
            return no.value
        if isinstance(no, ast.BinOp) and isinstance(no.op, ast.Add):
            e = self.dobrar(no.left)
            d = self.dobrar(no.right)
            if e is not None and d is not None:
                return e + d
        if isinstance(no, ast.Name):
            valores = self.atribuicoes.get(no.id, [])
            if len(valores) == 1:
                return self.dobrar(valores[0])
        return None

    @staticmethod
    def _uniao(a, b):
        saida = dict(a)
        for nome, pos in b.items():
            saida[nome] = _mais_forte(saida.get(nome), pos)
        return saida

    @staticmethod
    def _rebaixar(achados, posicao):
        return {nome: _mais_fraca(pos, posicao) for nome, pos in (achados or {}).items()}

    # -----------------------------------------------------------------
    def sitios(self):
        """[(tipo, linha, no_da_expressao_do_alvo)] dos tres atos."""
        fora = []
        for no in ast.walk(self.arvore):
            if not isinstance(no, ast.Call):
                continue
            inteiro = ast.unparse(no.func)
            ultimo = inteiro.split('.')[-1]
            if ultimo == CARGA and len(no.args) >= 2:
                fora.append(('carrega', no.lineno, no.args[1]))
            elif ultimo in INVOCACOES and 'subprocess' in inteiro and no.args:
                primeiro = no.args[0]
                alvos = primeiro.elts if isinstance(primeiro, ast.List) else [primeiro]
                for a in alvos:
                    fora.append(('invoca', no.lineno, a))
            elif ultimo == LEITURA and no.args:
                fora.append(('abre', no.lineno, no.args[0]))
        return fora

    def aponta_para_a_pasta(self, no, prof=0, vistos=frozenset()):
        """A expressao fala de `ferramentas/`, mesmo sem nomear arquivo nenhum?

        Sem isto, um `open(caminho)` de JSON e um `open(caminho)` de irmao
        seriam a mesma coisa para quem conta o que ficou sem resolver — e o
        relatorio encheria de ruido ate ninguem o ler."""
        if no is None or prof > 8:
            return False
        if isinstance(no, ast.Constant):
            return isinstance(no.value, str) and 'ferramentas' in no.value
        if isinstance(no, ast.Name):
            if no.id in vistos:
                return False
            vistos = vistos | {no.id}
            return any(self.aponta_para_a_pasta(v, prof + 1, vistos)
                       for v in self.atribuicoes.get(no.id, []))
        for filho in ast.iter_child_nodes(no):
            if self.aponta_para_a_pasta(filho, prof + 1, vistos):
                return True
        return False


_ORDEM = {LITERAL: 3, INDIRETO: 2, CONSTRUIDO: 1}


def _mais_forte(a, b):
    if a is None:
        return b
    return a if _ORDEM[a] >= _ORDEM[b] else b


def _mais_fraca(a, b):
    return a if _ORDEM[a] <= _ORDEM[b] else b


# ---------------------------------------------------------------------------
# A LEITURA DE UMA PASTA INTEIRA
# ---------------------------------------------------------------------------
def atos(arquivos):
    """[registro] de todo ato sobre irmao, em todo `.py` da pasta.

    registro = (quem, linha, tipo, alvo, posicao, visivel)

    `visivel` e a pergunta que os tres classificadores fazem, e e so esta:
    o nome do alvo esta escrito, como texto, no arquivo de quem age?
    """
    irmaos = {n for n in arquivos if n.endswith(EXTENSOES)}
    saida = []
    for quem in sorted(arquivos):
        if not quem.endswith('.py'):
            continue
        try:
            a = Arquivo(arquivos[quem])
        except SyntaxError:
            continue
        for tipo, linha, no in a.sitios():
            for alvo, posicao in sorted(a.resolver(no).items()):
                if alvo not in irmaos or alvo == quem:
                    continue
                saida.append((quem, linha, tipo, alvo, posicao, alvo in a.texto))
    return saida


def invisiveis(arquivos):
    """Atos sobre irmao cujo nome NAO esta escrito no arquivo de quem age.

    `[]` e a resposta de hoje, e e medicao e nao ausencia de medicao: toda
    indirecao desta pasta termina num literal. Deixa de ser `[]` no dia em que
    alguem montar o nome de um irmao — e aí os tres classificadores ficam cegos
    para aquele ato de uma vez so, que e o que o item 7 nomeou."""
    return [r for r in atos(arquivos) if not r[5]]


def indiretos(arquivos):
    """Atos que so chegam ao literal por variavel, parametro ou chave.

    Estes sao VISIVEIS hoje, e e por isso que nao reprovam nada. O numero e
    registro: ele mede quanto da visibilidade de hoje depende de um literal
    escrito ali por outro motivo."""
    return [r for r in atos(arquivos) if r[4] != LITERAL and r[5]]


def nao_resolvidos(arquivos):
    """Sitios de ato que falam da pasta e cujo alvo a regua nao resolveu.

    Sao o limite, nao a aprovacao: carga nao resolvida e o caso perigoso, e o
    portao a cobra em afirmacao propria."""
    saida = []
    for quem in sorted(arquivos):
        if not quem.endswith('.py'):
            continue
        try:
            a = Arquivo(arquivos[quem])
        except SyntaxError:
            continue
        for tipo, linha, no in a.sitios():
            if a.resolver(no):
                continue
            if tipo == 'carrega' or a.aponta_para_a_pasta(no):
                saida.append((quem, linha, tipo, ast.unparse(no)[:70]))
    return saida


def nao_lidos(arquivos):
    """Arquivos da pasta que esta regua NAO le: os `.mjs`, os `.php` e todo
    `.py` que nao parseia. Impressos porque limite calado vira cobertura
    imaginada."""
    saida = []
    for nome in sorted(arquivos):
        if not nome.endswith(EXTENSOES):
            continue
        if not nome.endswith('.py'):
            saida.append((nome, 'nao e Python'))
            continue
        try:
            ast.parse(arquivos[nome])
        except SyntaxError as e:
            saida.append((nome, 'nao parseia: %s' % e.msg))
    return saida


def ler_pasta(pasta=None):
    pasta = pasta or os.path.join(RAIZ, 'ferramentas')
    saida = {}
    for nome in sorted(os.listdir(pasta)):
        if nome.startswith('.'):
            continue
        try:
            with open(os.path.join(pasta, nome), encoding='utf-8', errors='replace') as f:
                saida[nome] = f.read()
        except OSError:
            continue
    return saida


if __name__ == '__main__':
    arquivos = ler_pasta()
    todos = atos(arquivos)
    inv = invisiveis(arquivos)
    ind = indiretos(arquivos)
    nr = nao_resolvidos(arquivos)
    nl = nao_lidos(arquivos)
    print('ALVOS DE PORTAO — %d arquivos em ferramentas/, %d atos sobre irmao'
          % (len(arquivos), len(todos)))
    por_posicao = {}
    for r in todos:
        por_posicao[r[4]] = por_posicao.get(r[4], 0) + 1
    for pos in (LITERAL, INDIRETO, CONSTRUIDO):
        print('  %-12s %d' % (pos, por_posicao.get(pos, 0)))
    print('\nATOS INVISIVEIS para a varredura por nome: %d' % len(inv))
    for quem, linha, tipo, alvo, pos, _ in inv:
        print('  %s:%d %s %s (%s)' % (quem, linha, tipo, alvo, pos))
    print('\nVISIVEIS SO POR ACIDENTE (indirecao que termina em literal): %d' % len(ind))
    for quem, linha, tipo, alvo, pos, _ in ind:
        print('  %s:%d %s %s' % (quem, linha, tipo, alvo))
    print('\nSITIOS QUE FALAM DA PASTA E NAO RESOLVERAM: %d' % len(nr))
    for quem, linha, tipo, txt in nr:
        print('  %s:%d %s %s' % (quem, linha, tipo, txt))
    print('\nFORA DO ALCANCE DESTA REGUA: %d arquivos (%d .mjs/.php, %d .py que nao parseiam)'
          % (len(nl), sum(1 for _, m in nl if m == 'nao e Python'),
             sum(1 for _, m in nl if m != 'nao e Python')))
    for nome, motivo in nl:
        if motivo != 'nao e Python':
            print('  %-40s %s' % (nome, motivo))
    raise SystemExit(0)
