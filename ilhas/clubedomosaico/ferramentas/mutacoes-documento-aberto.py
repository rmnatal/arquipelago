#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra, uma por vez, a declaracao `documento_aberto` dos cinco bancos de material e a
procedencia dela, e exige que `validar-banco.py` REPROVE cada mutacao.

    python3 ferramentas/mutacoes-documento-aberto.py

POR QUE ESTE ARQUIVO EXISTE. O campo nasceu no esquema v17 (12/10/2026) para as dez
fontes de `dados/tecnicas.json` e a divida ficou escrita com numero: os cinco bancos de
material respondiam "este documento foi aberto?" em PROSA, dentro do campo `tipo`, e
prosa nenhum portao le. A divida foi paga em 13/10/2026 — as 53 fontes declaram, e
`validar-banco.py` cobra o campo nelas. **Portao novo que nunca foi visto reprovar nao
mediu nada** (secao 8 do ARQUIPELAGO.md), e aqui o agravante tem nome: o que este campo
decide e o PEDIDO DE REDE ao Raphael (`ferramentas/medir-egresso.py`, `trava_coleta`).
Pedido errado nao atrasa um bloco: ele pede ao Raphael a porta errada e deixa a
pendencia que importa fora da lista, que foi exatamente o que aconteceu por 12 dias com
`dados/tecnicas.json`.

O QUE ESTA BATERIA NAO PROMETE, e isto fica dito antes das mutacoes para ninguem ler
verde como garantia: **nenhum portao desta ilha sabe se um documento foi aberto de
verdade.** Declarar `documento_aberto: true` numa fonte que ninguem abriu e mentira que
nao se cobre de dentro do repositorio — `mutacoes-tecnicas.py` ja registra isso, com um
caso que espera APROVA de proposito. O que se cobra aqui e a familia de defeito que
REALMENTE acontece: o campo faltando, o campo com tipo errado, e o valor saindo de
sincronia com a frase que o sustenta.

AS FAMILIAS:
  1. O CAMPO SOME — apagado de uma fonte, de um banco inteiro, ou nascendo ausente num
     SKU novo (que e como a divida nasceu: arquivo novo depois da regra).
  2. O CAMPO MENTE DE TIPO — string no lugar de booleano, `null` no lugar de booleano.
     `false` e o valor de 48 das 53 fontes, entao cobranca por VERDADE leria as 48 como
     campo faltando: e por isso que a cobranca e por presenca e tipo, e e isso que estas
     mutacoes vigiam.
  3. O VALOR E A PROVA SAEM DE SINCRONIA — o booleano vira e a procedencia fica velha,
     ou a procedencia nomeia fonte que nao existe mais, ou o bloco inteiro desaparece.

Cada mutacao roda numa COPIA da pasta da ilha, em `mkdtemp`. Nada aqui toca o
repositorio — e isso e de propósito, para esta bateria ficar FORA da lista de catorze que
`ferramentas/teste-rede-de-sinal.py` vigia.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCOS = ["acabamento", "alicates", "colas", "pastilhas", "rejuntes"]


def caminho_banco(raiz, banco):
    return os.path.join(raiz, "dados", "materiais-%s.json" % banco)


def editar_banco(raiz, banco, muda):
    caminho = caminho_banco(raiz, banco)
    with open(caminho, encoding="utf-8") as fh:
        d = json.load(fh)
    muda(d)
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def primeira_fonte(d):
    """O primeiro par (material, fonte_id) do banco, na ordem do arquivo."""
    for m in d["materiais"]:
        for fid in (m.get("fontes") or {}):
            return m, fid
    raise AssertionError("mutacao INERTE: banco sem fonte nenhuma")


# ---------------------------------------------- 1. o campo some

def m_campo_apagado_de_uma_fonte(raiz):
    """O caso mais simples, e o que a cobranca por presenca existe para pegar."""
    def muda(d):
        m, fid = primeira_fonte(d)
        if "documento_aberto" not in m["fontes"][fid]:
            raise AssertionError("mutacao INERTE: a fonte ja nao declarava")
        del m["fontes"][fid]["documento_aberto"]
    editar_banco(raiz, "rejuntes", muda)


def m_campo_apagado_do_banco_inteiro(raiz):
    """O mundo de ontem: um banco de material inteiro sem a declaracao. Era assim que os
    cinco estavam ate 13/10/2026, com a pergunta respondida so em prosa."""
    def muda(d):
        n = 0
        for m in d["materiais"]:
            for fid in (m.get("fontes") or {}):
                if m["fontes"][fid].pop("documento_aberto", "ausente") != "ausente":
                    n += 1
        if not n:
            raise AssertionError("mutacao INERTE: nenhuma fonte declarava")
    editar_banco(raiz, "acabamento", muda)


def m_sku_novo_nasce_sem_declarar(raiz):
    """A MUTACAO QUE JUSTIFICA O ARQUIVO, porque e a forma como a divida NASCEU e nao
    uma hipotese: `dados/tecnicas.json` foi criado em 14/09/2026, DEPOIS da lista de
    `GATILHOS` do `medir-egresso.py`, e ficou 12 dias fora do pedido de rede com a
    frase gerada ao lado jurando que suas fontes eram referencia 'JA LIDA'.

    Aqui o mesmo defeito volta na unidade em que ele volta de verdade: um SKU novo,
    copiado de um que existe, com a fonte sem o campo. Sem a cobranca de 13/10 no
    `validar-banco.py` isto passa verde, vai ao ar, e o host daquela fonte sai do
    pedido de rede sem ninguem decidir que ele devia sair."""
    def muda(d):
        m, fid = primeira_fonte(d)
        novo = json.loads(json.dumps(m))
        novo["id"] = m["id"] + "-sku-novo-de-bancada"
        for f in (novo.get("fontes") or {}).values():
            f.pop("documento_aberto", None)
        d["materiais"].append(novo)
    editar_banco(raiz, "pastilhas", muda)


# ---------------------------------------------- 2. o campo mente de tipo

def m_valor_vira_string(raiz):
    """`"nao"` no lugar de `False`. Uma cobranca escrita como `if not f.get(campo)`
    aceitaria `"nao"` (string nao vazia e verdadeira) e ainda leria o `False` legitimo
    das 48 como campo faltando: as duas metades erradas de uma vez."""
    def muda(d):
        m, fid = primeira_fonte(d)
        m["fontes"][fid]["documento_aberto"] = "nao"
    editar_banco(raiz, "colas", muda)


def m_valor_vira_null(raiz):
    """`null` e a forma elegante de nao responder, e o esquema ja decidiu que ela nao
    serve aqui: 'a ausencia do campo NAO vale como lido' vale igual para o nulo, porque
    quem le o campo decide PEDIDO DE REDE e 'nao sei' nao e uma porta para pedir."""
    def muda(d):
        m, fid = primeira_fonte(d)
        m["fontes"][fid]["documento_aberto"] = None
    editar_banco(raiz, "alicates", muda)


def m_valor_vira_numero(raiz):
    """`1` passa em qualquer teste de verdade e nao e booleano. Esta mutacao existe
    porque `isinstance(True, int)` e verdadeiro em Python e o contrario nao: um portao
    escrito com `isinstance(x, int)` aceitaria o 1, e o campo deixaria de ser legivel
    como declaracao para virar um numero que alguem interpreta."""
    def muda(d):
        m, fid = primeira_fonte(d)
        m["fontes"][fid]["documento_aberto"] = 1
    editar_banco(raiz, "rejuntes", muda)


# ---------------------------------------------- 3. o valor e a prova saem de sincronia

def m_booleano_vira_e_a_prova_fica_velha(raiz):
    """A SEGUNDA MUTACAO QUE JUSTIFICA O ARQUIVO, e a mais realista de todas: alguem
    vira `false` para `true` — por engano, ou porque leu a fonte de outro SKU — e deixa
    a frase que sustenta o valor como estava. O campo continua presente, continua
    booleano, e passa em toda cobranca de presenca e tipo. O que ele nao faz mais e
    bater com a propria procedencia, e e so por isso que da para pegar.

    E este e o defeito que TIRA host do pedido de rede: `true` nao soma ninguem, mas
    quem virou o valor acha que resolveu a pendencia, e a fonte continua sem ser lida."""
    def muda(d):
        m, fid = primeira_fonte(d)
        atual = m["fontes"][fid].get("documento_aberto")
        if not isinstance(atual, bool):
            raise AssertionError("mutacao INERTE: a fonte nao declara booleano")
        m["fontes"][fid]["documento_aberto"] = not atual
    editar_banco(raiz, "pastilhas", muda)


def m_procedencia_do_banco_inteiro_desaparece(raiz):
    """O bloco `de_onde_saiu_o_documento_aberto` sai do arquivo. Os 53 valores continuam
    la, e nenhum deles diz mais de onde saiu — que e o estado de 12/10, em que a resposta
    existia so na cabeca de quem a escreveu."""
    def muda(d):
        if "de_onde_saiu_o_documento_aberto" not in d:
            raise AssertionError("mutacao INERTE: o banco ja nao trazia o bloco")
        del d["de_onde_saiu_o_documento_aberto"]
    editar_banco(raiz, "colas", muda)


def m_procedencia_perde_uma_linha(raiz):
    """A fonte fica declarada e a procedencia dela sai da lista. Valor sem prova escrita
    e exatamente o que o campo nasceu para substituir."""
    def muda(d):
        m, fid = primeira_fonte(d)
        prov = d["de_onde_saiu_o_documento_aberto"]["por_fonte"]
        if fid not in prov:
            raise AssertionError("mutacao INERTE: a fonte ja nao tinha procedencia")
        del prov[fid]
    editar_banco(raiz, "acabamento", muda)


def m_procedencia_nomeia_fonte_morta(raiz):
    """A fonte e removida do material e a linha de procedencia dela FICA. Procedencia de
    fonte que nao existe mais e o mesmo defeito da lista de nomes de arquivo dentro de
    ferramenta: ela envelhece calada e quem a le acha que mediu alguma coisa."""
    def muda(d):
        m, fid = primeira_fonte(d)
        if len(m["fontes"]) < 2:
            # Nao se apaga a unica fonte de um material: o portao reprovaria por
            # "sem nenhuma fonte" e a mutacao mediria outra coisa.
            for outro in d["materiais"]:
                if len(outro.get("fontes") or {}) >= 2:
                    m = outro
                    fid = sorted(m["fontes"])[0]
                    break
            else:
                raise AssertionError("mutacao INERTE: nenhum material com 2+ fontes")
        del m["fontes"][fid]
    editar_banco(raiz, "rejuntes", muda)


def m_procedencia_perde_a_frase(raiz):
    """A linha fica com o valor e sem `a_frase`. Procedencia sem a frase e um carimbo:
    ela afirma que houve prova e nao diz qual."""
    def muda(d):
        m, fid = primeira_fonte(d)
        prov = d["de_onde_saiu_o_documento_aberto"]["por_fonte"]
        if fid not in prov:
            raise AssertionError("mutacao INERTE: a fonte nao tem procedencia")
        del prov[fid]["a_frase"]
    editar_banco(raiz, "pastilhas", muda)


MUTACOES = [
    ("o campo apagado de UMA fonte", m_campo_apagado_de_uma_fonte),
    ("o campo apagado do BANCO INTEIRO (o mundo de 12/10)", m_campo_apagado_do_banco_inteiro),
    ("SKU NOVO nasce sem declarar (e como a divida nasceu)", m_sku_novo_nasce_sem_declarar),
    ("o valor vira a string 'nao'", m_valor_vira_string),
    ("o valor vira null", m_valor_vira_null),
    ("o valor vira o numero 1 (isinstance(True, int) e verdadeiro)", m_valor_vira_numero),
    ("o booleano VIRA e a prova fica velha", m_booleano_vira_e_a_prova_fica_velha),
    ("a procedencia do banco inteiro desaparece", m_procedencia_do_banco_inteiro_desaparece),
    ("a procedencia perde UMA linha", m_procedencia_perde_uma_linha),
    ("a procedencia nomeia fonte MORTA", m_procedencia_nomeia_fonte_morta),
    ("a procedencia perde `a_frase`", m_procedencia_perde_a_frase),
]


def portao(raiz):
    r = subprocess.run([sys.executable, "-I", os.path.join("ferramentas", "validar-banco.py"), "."],
                       cwd=raiz, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def primeira_falha(saida):
    for linha in saida.split("\n"):
        if linha.strip().startswith("- "):
            return linha.strip()[2:]
    for linha in saida.split("\n"):
        if "ERRO" in linha:
            return linha.strip()
    return "(sem linha de erro)"


def main():
    rc, saida = portao(ILHA)
    if rc != 0:
        print("O banco de verdade ja esta reprovado — conserte antes de mutar.")
        print(primeira_falha(saida))
        return 1
    print("Banco intacto: APROVADO (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-docaberto-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as e:
                passaram.append("%s [%s]" % (nome, e))
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue
            rc, saida = portao(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
                continue
            print("  reprovou como devia: %-56s | %s"
                  % (nome[:56], primeira_falha(saida)[:70]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram"
          % (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    print("\nAPROVADO: as %d mutacoes reprovaram. E o que ESTA BATERIA NAO PROVA segue "
          "escrito no topo do arquivo:\nnenhum portao daqui sabe se um documento foi "
          "aberto de verdade — isso e procedencia, nao sintaxe." % len(MUTACOES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
