#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a varredura da secao 14.3 de proposito, uma mutacao por vez, e exige que
`cobertura.py --conferir` ou `conferir-cobertura.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-cobertura.py

Por que este arquivo existe: o portao da cobertura nasceu verde, com 128 afirmacoes e
zero falha, e teste verde que nunca foi visto reprovar nao mediu nada (secao 8 do
ARQUIPELAGO.md). Neste caso ha um agravante: o numero que ele produz — "45 de 45 faixas
de cola saem sem os 3 elegiveis que a secao 14.3 exige" — vai virar decisao de que bloco
a ilha faz em seguida. Numero medido errado e pior que numero digitado errado, porque
parece conferido.

ELE MEDE UMA SEGUNDA COISA, e e a razao de o bloco existir: para cada mutacao, ele roda
TAMBEM os portoes que ja existiam antes desta varredura — `validar-banco.py`, que confere
as 27 celulas escritas a mao do esquema, e `teste-f2.php`, que varre os 105 estados
servidos mas afirma sobre o TEXTO da pagina, nao sobre quem e elegivel. A mutacao que os
dois antigos deixam passar e a unica prova de que a varredura acrescentou alguma coisa;
mutacao que qualquer portao pega ja estava coberta e nao justifica arquivo novo.

AS FAMILIAS:
  1. A REGUA DO SITE MUDA E O CENSO NAO — inclusive num pedaco da faixa onde a grade
     escrita a mao nao pisa (junta de 7 a 9 mm, que o esquema nunca visita de proposito,
     porque ele pisa so nas bordas declaradas).
  2. A FAIXA MUDA — o campo encolhe, ou o saneamento para de sanear.
  3. O ARQUIVO DO CENSO MENTE — resumo digitado, estado apagado, causa em branco,
     categoria vazia declarada com item dentro.
  4. O PROPRIO MEDIDOR AFROUXA — o superconjunto que mede a borda para de passar da
     borda, e a regra de quem conta como elegivel muda calada.

Cada uma roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F2 = os.path.join("snippets", "clubedomosaico-f2.php")
FAIXA = os.path.join("ferramentas", "faixa-da-f2.php")
CENSO = os.path.join("ferramentas", "cobertura.py")
JSON_CENSO = os.path.join("dados", "cobertura.json")


def editar(raiz, arquivo, velho, novo, vezes=1):
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()
    if texto.count(velho) < vezes:
        raise AssertionError(
            "mutacao INERTE: %r aparece %d vez(es) em %s, esperava %d"
            % (velho[:60], texto.count(velho), arquivo, vezes))
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(velho, novo, vezes))


def editar_censo(raiz, muda):
    caminho = os.path.join(raiz, JSON_CENSO)
    with open(caminho, encoding="utf-8") as fh:
        censo = json.load(fh)
    muda(censo)
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(censo, ensure_ascii=False, indent=2) + "\n")


# ---------------------------- 1. a regua do site muda e o censo nao

def m_junta_afrouxa_so_no_vao_da_grade(raiz):
    """A MUTACAO QUE JUSTIFICA O ARQUIVO. O teto da faixa de junta deixa de valer
    para 7, 8 e 9 mm — e so para eles.

    A grade escrita a mao do esquema pisa em 1, 2, 3, 4, 5, 6, 10 e 11 mm, escolhidos
    para encostar nas bordas declaradas pelos fabricantes. E uma grade boa, e e por isso
    que ela e o exemplo perfeito: 7, 8 e 9 mm ficam num vao onde nenhum extremo cai,
    entao nenhuma celula escrita a mao passa por ali. Com este afrouxamento, tres estados
    que o site serve passam a recomendar rejunte que o fabricante nao cobre — e os 27
    cruzamentos antigos continuam verdes, porque nenhum deles olha para la."""
    editar(raiz, F2,
           "\tif ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {",
           "\tif ( $junta_mm < $p['junta_min'] || ( $junta_mm > $p['junta_max'] && ( $junta_mm < 7 || $junta_mm > 9 ) ) ) {")


def m_silencio_vira_recomendacao(raiz):
    """A regra 2 da cola cai: base sem declaracao passa a valer como indicada. E o
    defeito mais caro que esta ilha pode ter — silencio do fabricante virando 'pode' —
    e ele infla a cobertura exatamente onde ela e zero."""
    editar(raiz, F2,
           "\tif ( ! isset( $p['bases_indicadas'][ $base ] ) ) {\n\t\treturn array( 'silencio', 0 );",
           "\tif ( false && ! isset( $p['bases_indicadas'][ $base ] ) ) {\n\t\treturn array( 'silencio', 0 );")


def m_ambiente_critico_do_rejunte_cai(raiz):
    """A regra 2 do rejunte cai: ambiente critico deixa de exigir declaracao explicita,
    e quem nunca falou de agua passa a ser recomendado dentro dela.

    ESTA MUTACAO SUBSTITUI UMA QUE NAO MORDIA, e a razao vale ser lida antes da proxima
    coleta. A primeira versao derrubava a regra **3** (quem delimita ambiente fica fechado
    nele) e PASSOU — nao por buraco no portao, e sim porque, com o banco de hoje, a regra
    3 do rejunte e codigo morto: das cinco fichas, so o acrilico declara ambiente
    (`areas internas e externas`), e nos estados em que a regra 3 o cortaria a regra 2 ja
    o tinha cortado antes, porque `contato_permanente_agua` e critico e as resistencias
    dele param em `areas molhadas`. Mutacao inerte e teste verde com outro nome (secao 8),
    entao ela saiu daqui — mas a regra 3 NAO saiu do snippet: ela e a que vai decidir no
    dia em que entrar um rejunte que delimite ambiente, e e ai que esta mutacao deve
    voltar a existir."""
    editar(raiz, F2,
           "\t$criticos = cdm_f2_criticos_rejunte();\n\tif ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {",
           "\t$criticos = cdm_f2_criticos_rejunte();\n\tif ( false && isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {")


def m_ressalva_vira_recomendacao_no_site(raiz):
    """A regra 5 da cola cai no site: fonte fraca passa a recomendar. O censo continua
    contando sem ressalva, entao as duas metades discordam.

    A ancora leva o comentario da regra junto de proposito: a linha do `if` e IDENTICA
    na cola e no rejunte, e sem o comentario a mutacao trocaria a primeira que aparecer —
    ou as duas — em vez da que ela diz que troca."""
    editar(raiz, F2,
           "\t/* 5 — nível de fonte limita a recomendação primária. */\n\tif ( $p['nivel'] > cdm_f2_nivel_maximo() ) {",
           "\t/* 5 — nível de fonte limita a recomendação primária. */\n\tif ( false && $p['nivel'] > cdm_f2_nivel_maximo() ) {")


# ---------------------------------------------------- 2. a faixa muda

def m_campo_da_junta_encolhe(raiz):
    """O campo passa a aceitar so ate 10 mm. O censo continua com 60 estados de
    rejunte enquanto a ferramenta serve 50 — varredura sobre faixa que nao existe
    mais."""
    editar(raiz, F2, "( $jun >= 1 && $jun <= 12 )", "( $jun >= 1 && $jun <= 10 )")


def m_saneamento_aceita_qualquer_base(raiz):
    """O saneamento para de sanear a base. Sem isto a faixa nao tem borda: qualquer
    coisa que chegue na URL vira um estado, e o censo nunca fecha."""
    editar(raiz, F2,
           "'base'     => isset( $rot['base'][ $base ] ) ? $base : 'ceramica_esmaltada_porcelana',",
           "'base'     => $base ? $base : 'ceramica_esmaltada_porcelana',")


# ------------------------------------------------- 3. o arquivo do censo mente

def m_resumo_digitado(raiz):
    """Alguem 'corrige' a contagem no arquivo em vez de no banco. E o cartao '0 no
    banco' desta ilha outra vez: numero de tela que nasceu digitado."""
    editar_censo(raiz, lambda c: c["resumo"]["cola"].__setitem__("estados_com_o_minimo", 45))


def m_resumo_computado_errado(raiz):
    """O GERADOR passa a contar errado — "com o minimo" conta >= 2 em vez de >= 3.

    ELA REGENERA O ARQUIVO DEPOIS DE MUTAR, e isso nao e detalhe: e o que torna esta a
    unica mutacao do censo que `--conferir` nao pega. As outras editam o JSON a mao, entao
    a regeneracao diverge e acusa "arquivo velho" — trava boa, e trava que nao mede nada
    aqui. O caso real e este: alguem mexe no gerador, roda `cobertura.py` e commita as
    duas coisas juntas. A regeneracao passa a bater consigo mesma, o censo fica coerente
    por dentro, e o numero que vai para o REGISTRO.md esta errado. Quem ve e a conferencia
    que RECONTA os estados a partir das listas, do outro lado da ponte — e a cicatriz da
    secao 8: quem confere nao pode chamar a regua de quem produziu o dado.

    Simular sem regenerar seria a mutacao reprovando pelo portao errado, que foi
    exatamente o defeito que o mutacoes-ga4.py desta ilha teve que reescrever em 12/09."""
    editar(raiz, CENSO,
           '"estados_com_o_minimo": sum(1 for n in contagens if n >= MINIMO_DA_SECAO_14_3),',
           '"estados_com_o_minimo": sum(1 for n in contagens if n >= MINIMO_DA_SECAO_14_3 - 1),')
    rc, saida = _rodar(raiz, ["python3", "ferramentas/cobertura.py"])
    if rc != 0:
        raise AssertionError("a regeneracao do censo mutado falhou: %s" % saida.strip()[:120])


def m_estado_apagado(raiz):
    """Um estado some do censo. A soma continua parecendo certa para quem le so o
    resumo."""
    def muda(c):
        c["estados"]["cola"].pop()
    editar_censo(raiz, muda)


def m_causa_em_branco(raiz):
    """Uma faixa descoberta deixa de dizer por que esta descoberta. A secao 7 do
    contrato cobra que a causa que o codigo separa o texto separe."""
    def muda(c):
        c["faixas_descobertas"]["cola"][0]["por_que"] = ""
    editar_censo(raiz, muda)


def m_categoria_vazia_mentindo(raiz):
    """O censo declara vazia uma categoria que tem itens. E a mesma familia do
    'Temos hoje' digitado da Robometria: a afirmacao sobre o proprio banco."""
    def muda(c):
        c["banco_hoje"]["categorias_do_vocabulario_sem_nenhum_item"].append("cola")
    editar_censo(raiz, muda)


def m_quantos_elegiveis_inflado(raiz):
    """A contagem de um estado deixa de bater com a lista que ela conta."""
    def muda(c):
        c["estados"]["rejunte"][0]["quantos_elegiveis"] += 1
    editar_censo(raiz, muda)


# --------------------------------------------- 4. o proprio medidor afrouxa

def m_superconjunto_nao_passa_da_borda(raiz):
    """O superconjunto que mede a faixa para de passar por cima dela. O teto medido
    vira o fim da regua, e a faixa passaria a ser 'ate 12' por coincidencia. O medidor
    tem obrigacao de recusar medir assim."""
    editar(raiz, FAIXA, "$SUPER_MAX = 20;", "$SUPER_MAX = 12;")


def m_ressalva_conta_como_elegivel(raiz):
    """A definicao de elegivel muda no censo, calada: mencao com ressalva passa a
    contar. A cobertura sobe sem um produto novo entrar no banco, e o site continua
    servindo o que servia."""
    editar(raiz, CENSO,
           'return sorted(celula["recomendados_topo"] + celula["elegiveis_abaixo_do_topo"])',
           'return sorted(celula["recomendados_topo"] + celula["elegiveis_abaixo_do_topo"] + celula["mencionados_com_ressalva"])')


MUTACOES = [
    ("a faixa de junta afrouxa SO em 7, 8 e 9 mm (o vao da grade escrita a mao)", m_junta_afrouxa_so_no_vao_da_grade),
    ("silencio do fabricante vira recomendacao (regra 2 da cola cai)", m_silencio_vira_recomendacao),
    ("ambiente critico do rejunte deixa de exigir declaracao (regra 2 cai)", m_ambiente_critico_do_rejunte_cai),
    ("fonte fraca vira recomendacao no site (regra 5 da cola cai)", m_ressalva_vira_recomendacao_no_site),
    ("o campo da junta encolhe de 12 para 10 mm", m_campo_da_junta_encolhe),
    ("o saneamento aceita qualquer base vinda da URL", m_saneamento_aceita_qualquer_base),
    ("o resumo do censo e digitado em vez de contado", m_resumo_digitado),
    ("o GERADOR conta errado e regenera coerente com o proprio defeito", m_resumo_computado_errado),
    ("um estado some do censo", m_estado_apagado),
    ("uma faixa descoberta fica sem causa", m_causa_em_branco),
    ("o censo declara vazia uma categoria que tem itens", m_categoria_vazia_mentindo),
    ("quantos_elegiveis deixa de bater com a lista que ele conta", m_quantos_elegiveis_inflado),
    ("o superconjunto para de passar por cima da faixa", m_superconjunto_nao_passa_da_borda),
    ("mencao com ressalva passa a contar como elegivel, calada", m_ressalva_conta_como_elegivel),
]


def _rodar(raiz, cmd):
    r = subprocess.run(cmd, cwd=raiz, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def portao_novo(raiz):
    """A varredura da 14.3, nas duas metades. Reprovar em qualquer uma e reprovar."""
    rc1, s1 = _rodar(raiz, ["python3", "ferramentas/cobertura.py", "--conferir"])
    rc2, s2 = _rodar(raiz, ["php", "ferramentas/conferir-cobertura.php", "."])
    return (rc1 or rc2), s1 + s2


def portoes_antigos(raiz):
    """O que ja existia antes deste bloco: as 27 celulas escritas a mao e a varredura
    de TEXTO das duas ferramentas."""
    rc1, _ = _rodar(raiz, ["python3", "ferramentas/validar-banco.py", "."])
    rc2, _ = _rodar(raiz, ["php", "ferramentas/teste-f2.php", "."])
    return rc1 or rc2


def primeira_falha(saida):
    for linha in saida.splitlines():
        if "FALHA" in linha:
            return " ".join(linha.split())[6:]
    return ""


def main():
    rc, saida = portao_novo(ILHA)
    if rc != 0:
        print("A cobertura de verdade ja esta reprovada — conserte antes de mutar.")
        print(primeira_falha(saida))
        return 1
    print("Cobertura intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    so_o_novo = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-cob-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [" + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue
            rc, saida = portao_novo(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
                continue
            antigos = portoes_antigos(copia)
            marca = "   [so a varredura viu]" if antigos == 0 else ""
            if antigos == 0:
                so_o_novo.append(nome)
            print("  reprovou como devia: %-64s | %s%s"
                  % (nome[:64], primeira_falha(saida)[:52], marca))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram"
          % (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    print("%d delas NENHUM portao antigo pegou — e o que a varredura acrescentou:"
          % len(so_o_novo))
    for nome in so_o_novo:
        print("  - %s" % nome)
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
