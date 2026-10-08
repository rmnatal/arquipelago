#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito a promessa numerica do `<title>` e a `description` das
quatro paginas de SERP, uma mutacao por vez, e exige que a bancada REPROVE cada
uma.

    python3 ferramentas/mutacoes-promessa-do-titulo.py

POR QUE ESTE ARQUIVO EXISTE. O bloco de 02/10/2026 fechou o BLOCO A do despacho
do Raphael de 24/09: o `<title>` de tres paginas passou a trocar a marca por um
numero contado, e as quatro `description` entraram na faixa de 120 a 160. As
travas nasceram verdes na primeira execucao, e a secao 8 do ARQUIPELAGO.md diz o
que isso vale: trava que ninguem viu reprovar nao mediu nada.

E AQUI ELAS SAO PIORES QUE O NORMAL, porque DUAS DELAS SAO SILENCIOSAS POR
DESENHO. A trava do teto e a trava do banco que nao chegou nao falham: elas
devolvem a marca e a pagina continua valida. Quem nao exercita as duas nao tem
como saber se a promessa saiu do ar — e promessa que desaparece sozinha e
exatamente o defeito que a Robometria nomeou ao escrever a mesma trava em 17/09.

A PROMESSA MUDOU DE NATUREZA EM 08/10/2026, E ESTE ARQUIVO COM ELA. Ate 07/10
as duas promessas eram INVENTARIO — "7 colas para 9 bases", "12 pecas
calculadas": numeros contados, numeros certos, e nenhum deles e o que a pessoa
procurou. A leitura semanal de 07/10 mediu as duas paginas na primeira pagina do
Google com ZERO clique pela TERCEIRA semana seguida, com as posicoes
MELHORANDO, e as Propostas 1 e 2 dela mandaram entregar A RESPOSTA. Agora o
titulo da F2 nomeia a COLA que o banco indica em mais casos e o da F1 serve a
FAIXA de pastilhas. As seis mutacoes novas da F2 e as duas da F1 existem porque
promessa que nomeia produto tem uma superficie de erro que promessa de contagem
nao tinha: o nome pode ser digitado, o lider pode ser contado errado, e o empate
pode ser desempatado por acidente de ordenacao.

AS MUTACOES QUE MAIS VALEM AQUI NAO SAO AS OBVIAS. Sao estas:

  * o NUMERO DIGITADO no lugar do contado — a frase continua bonita, continua na
    faixa, e mente no dia em que o banco muda. E a familia de defeito que esta
    ilha mais pagou;
  * o NOME DA PAGINA cedendo o lugar em vez da marca — o `<title>` e o H1
    passariam a dizer nomes diferentes a uma linha de distancia, que foi o que a
    Aquametria pagou em 11/09/2026;
  * a PAGINA PARADA ganhando promessa — o Trencadis fica como estava por ordem
    escrita, para a leitura seguinte ter com o que comparar. Trocar as quatro de
    uma vez nao e zelo: e tornar a proxima medicao ilegivel.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio nem
o site. Ferramenta de bancada: nunca vai para o site.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = os.path.join("snippets", "clubedomosaico-casca.php")
F1 = os.path.join("snippets", "clubedomosaico-f1.php")
F2 = os.path.join("snippets", "clubedomosaico-f2.php")
TEC = os.path.join("snippets", "clubedomosaico-tecnicas.php")

BANCADAS = ("teste-casca.php", "teste-f1.php", "teste-f2.php", "teste-tecnicas.php")


def ler(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as fh:
        return fh.read()


def gravar(raiz, rel, texto):
    with open(os.path.join(raiz, rel), "w", encoding="utf-8") as fh:
        fh.write(texto)


def trocar(raiz, rel, antigo, novo, vezes=1):
    texto = ler(raiz, rel)
    if antigo not in texto:
        raise AssertionError("mutacao nao achou o alvo em %s: %r" % (rel, antigo[:70]))
    gravar(raiz, rel, texto.replace(antigo, novo, vezes))


# ------------------------------------------------------------------ mutacoes

def m_nome_do_lider_digitado(raiz):
    """O NOME DA COLA escrito a mao dentro do molde, em vez de vir do banco. E a
    mutacao que importa na promessa nova: a frase continua bonita, continua na
    faixa, e no dia em que outra cola liderar ela mente — exatamente a familia
    de defeito que esta ilha mais pagou, agora com nome de produto no lugar do
    numero."""
    trocar(raiz, F2,
           "\t\tstrtr( '{nome}, {fatia}%', array( '{nome}' => $lider['curto'] ) ),",
           "\t\tstrtr( '{nome}, {fatia}%', array( '{nome}' => 'Silicone Neutro' ) ),")


def m_lider_conta_os_segundos(raiz):
    """O lider passa a contar tambem os cartoes de SEGUNDA LINHA. A tela serve
    `cdm-f2-segundo` justamente porque aquilo nao e a recomendacao — contar os
    dois faz a promessa do resultado da busca prometer mais do que a pagina
    entrega, e e invisivel para quem le a frase."""
    trocar(raiz, F2,
           "\t\t\t\tforeach ( $c['recomendados_topo'] as $id ) {\n\t\t\t\t\tif ( ! isset( $casos[ $id ] ) ) {",
           "\t\t\t\tforeach ( array_merge( $c['recomendados_topo'], $c['elegiveis_abaixo_do_topo'] ) as $id ) {\n\t\t\t\t\tif ( ! isset( $casos[ $id ] ) ) {")


def m_empate_nao_e_recusado(raiz):
    """A recusa do EMPATE sai. Com duas colas no mesmo numero de casos, a pagina
    passa a nomear uma delas por desempate de ordenacao — uma afirmacao que ela
    nao faz, escolhida por acidente de `arsort`.

    ESTA MUTACAO PASSOU NA PRIMEIRA PASSADA DE 08/10/2026, e e por isso que
    `cdm_f2_lider_do_mapa()` existe. O banco de hoje tem 162 contra 28: sem
    empate possivel, a recusa era silenciosa e a mutacao saia invisivel. A
    decisao foi extraida para uma funcao pura e a bancada passou a FABRICAR a
    borda, chamando-a com um mapa empatado. Agora a mutacao e vista."""
    trocar(raiz, F2,
           "\treturn $quantos_no_topo > 1 ? '' : (string) $ids[0];",
           "\treturn $quantos_no_topo > 99 ? '' : (string) $ids[0];")


def m_lider_sem_fatia(raiz):
    """A FATIA sai do titulo e sobra "Silicone Neutro" sozinho — a afirmacao em
    bloco com escopo maior do que o medido que a secao 7 do contrato nomeia. A
    cola lidera 80% dos casos respondidos, nao todos."""
    trocar(raiz, F2,
           "\t\tstrtr( '{nome}, {fatia}%', array( '{nome}' => $lider['curto'] ) ),\n\t\tarray( 'fatia' => $lider['fatia'] )",
           "\t\tstrtr( '{nome} em {fatia} casos', array( '{nome}' => $lider['curto'] ) ),\n\t\tarray( 'fatia' => $lider['casos'] )")


def m_fatia_arredonda_para_cima(raiz):
    """A fatia passa a arredondar para CIMA: 80,2% viraria 81%, e a promessa do
    resultado da busca diria um numero que a varredura nao contou."""
    trocar(raiz, F2, "'fatia'       => (int) floor(", "'fatia'       => (int) ceil(")


def m_faixa_da_description_sem_portao(raiz):
    """O teto de 160 da description da F2 deixa de ser portao. Com nome de lider
    longo a frase estoura, o Google corta no meio, e nada acusa."""
    trocar(raiz, F2,
           "\t\tif ( $n < 120 || $n > 160 ) {\n\t\t\t$com_numero = '';\n\t\t}",
           "\t\tif ( $n < 0 ) {\n\t\t\t$com_numero = '';\n\t\t}")


def m_teto_ignorado(raiz):
    """TRAVA 1 desligada: a promessa entra mesmo estourando o teto."""
    trocar(raiz, CASCA,
           "\t\tif ( mb_strlen( $com_promessa, 'UTF-8' ) <= CDM_CASCA_TITULO_TETO ) {\n\t\t\treturn $com_promessa;\n\t\t}",
           "\t\treturn $com_promessa;")


def m_teto_afrouxado(raiz):
    """TRAVA 1 afrouxada de 65 para 120 — o titulo cabe e o Google corta."""
    trocar(raiz, CASCA, "define( 'CDM_CASCA_TITULO_TETO', 65 );", "define( 'CDM_CASCA_TITULO_TETO', 120 );")


def m_zero_vira_promessa(raiz):
    """TRAVA 2 desligada: banco que nao chegou publica "0 colas" na SERP."""
    trocar(raiz, CASCA,
           "\t\tif ( ! is_numeric( $valor ) || (float) $valor <= 0 ) {",
           "\t\tif ( ! is_numeric( $valor ) ) {")


def m_molde_cru_escapa(raiz):
    """A recusa do molde com chave sobrando sai, e "{colas}" vai para a SERP."""
    trocar(raiz, CASCA,
           "\tif ( false !== strpos( $frase, '{' ) ) {\n\t\treturn '';\n\t}",
           "\tif ( false !== strpos( $frase, '{{' ) ) {\n\t\treturn '';\n\t}")


def m_o_nome_cede_o_lugar(raiz):
    """A promessa toma o lugar do NOME em vez do lugar da marca."""
    trocar(raiz, CASCA,
           "\t$partes['site'] = $cauda;",
           "\t$partes['title'] = $promessa;\n\t$partes['site'] = $cauda;")


def m_trencadis_ganha_promessa(raiz):
    """A pagina que fica parada ganha promessa — e a proxima leitura perde a
    referencia contra a qual comparar."""
    trocar(raiz, TEC,
           "\tif ( empty( $registro['picassiette'] ) || $registro['picassiette']['slug'] !== $slug ) {\n\t\treturn $p;\n\t}\n\n\t$c = cdm_tecnicas_contas( 'picassiette' );",
           "\t$qual = '';\n\tforeach ( array( 'picassiette', 'trencadis' ) as $cand ) {\n\t\tif ( ! empty( $registro[ $cand ] ) && $registro[ $cand ]['slug'] === $slug ) {\n\t\t\t$qual = $cand;\n\t\t}\n\t}\n\tif ( '' === $qual ) {\n\t\treturn $p;\n\t}\n\n\t$c = cdm_tecnicas_contas( $qual );")


def m_picassiete_volta_aos_192(raiz):
    """A description mais longa das quatro volta ao ar, fora da faixa."""
    trocar(raiz, TEC,
           "'description_molde' => 'Mosaico Picassiete: o mosaico de louça quebrada, e com o que colar o caquinho em cada superfície — {colas} colas em {celulas} casos, pela declaração do fabricante.',",
           "'description_molde' => 'Mosaico Picassiete: o que é o mosaico de louça quebrada e com o que colar o caquinho em cada superfície — cerâmica, vidro, espelho, MDF, cimento ou metal — dentro de casa ou no sol e na chuva, em {colas} de {celulas}.',")


def m_trencadis_volta_aos_189(raiz):
    """A quarta description volta a estourar a faixa de 160."""
    trocar(raiz, TEC,
           "'description'  => 'Trencadís: o mosaico de caco quebrado a martelo, o nome ligado a Gaudí, e com o que colar o caco de azulejo ou de louça em cada superfície.',",
           "'description'  => 'Trencadís: o que é o mosaico de caco quebrado a martelo, de onde vem o nome ligado a Gaudí, e com o que colar caco de azulejo ou de louça em cerâmica, vidro, espelho, MDF, cimento ou metal.',")


def m_a_home_ganha_promessa(raiz):
    """A casca passa a declarar promessa para a home, que nao foi medida."""
    trocar(raiz, CASCA,
           "function cdm_casca_promessa_do_titulo( $slug ) {\n\t$slug = (string) $slug;",
           "function cdm_casca_promessa_do_titulo( $slug ) {\n\t$slug = (string) $slug;\n\tif ( 'inicio' === $slug ) {\n\t\treturn '17 paginas no ar';\n\t}")


def m_segundo_montador_de_titulo(raiz):
    """Uma segunda camada pendura o proprio `document_title_parts` — e assim que
    a etiqueta de robo desta ilha chegou a sair dobrada em 25/09."""
    texto = ler(raiz, F1)
    gravar(raiz, F1, texto + "\nadd_filter( 'document_title_parts', function ( $p ) { return $p; } );\n")


def m_faixa_da_f1_de_outra_conta(raiz):
    """A faixa da F1 passa a ser calculada sem a sobra de 10% que a tabela usa —
    a promessa deixa de ser a da tabela servida."""
    trocar(raiz, F1,
           "\t\t$r = cdm_f1_calcular( $p['forma'], $p['medidas'], $p['lado_mm'], $p['junta_mm'], $p['espessura_mm'], 10, 'cimenticio' );\n\t\tif ( empty( $r['pastilhas'] ) ) {",
           "\t\t$r = cdm_f1_calcular( $p['forma'], $p['medidas'], $p['lado_mm'], $p['junta_mm'], $p['espessura_mm'], 0, 'cimenticio' );\n\t\tif ( empty( $r['pastilhas'] ) ) {")


def m_promessa_da_f1_volta_ao_inventario(raiz):
    """A promessa da F1 volta a contar PECAS em vez de prometer a faixa. O numero
    continua contado e continua certo — e volta a dizer o tamanho da tabela em
    vez do que a pagina responde, que e o defeito que a Proposta 2 de 07/10
    mandou consertar."""
    trocar(raiz, F1,
           "\treturn cdm_casca_preencher_promessa( '{min} a {max} pastilhas', array( 'min' => $f['min'], 'max' => $f['max'] ) );",
           "\treturn cdm_casca_preencher_promessa( '{pecas} peças calculadas', array( 'pecas' => $f['quantas'] ) );")


def m_faixa_da_f1_invertida(raiz):
    """O minimo e o maximo trocam de lugar na promessa da F1: "960 a 23
    pastilhas". Os dois numeros sao contados, os dois estao certos, e a frase e
    impossivel — e nenhuma trava que olha SO para digito a pegaria."""
    trocar(raiz, F1,
           "'{min} a {max} pastilhas', array( 'min' => $f['min'], 'max' => $f['max'] )",
           "'{min} a {max} pastilhas', array( 'min' => $f['max'], 'max' => $f['min'] )")


def m_colas_contadas_com_o_banco_inteiro(raiz):
    """As colas passam a ser o tamanho do banco inteiro — e o banco traz os
    rejuntes. E a frase "10 dos 5 itens" que esta ilha serviu no ar em 12/09."""
    trocar(raiz, F2,
           "\t\tif ( 'cola' === ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {\n\t\t\t$n++;\n\t\t}",
           "\t\t$n++;\n\t\tif ( false ) {\n\t\t\t$n++;\n\t\t}")


def m_frase_sem_numero_curta(raiz):
    """A saida da TRAVA 2 vira uma frase de 50 caracteres — o Google descarta a
    curta e escreve a dele, e a linha que decide o clique deixa de ser nossa."""
    trocar(raiz, F2,
           ": 'Qual cola e qual rejunte usar no mosaico, pela declaração do próprio fabricante: cerâmica, vidro, espelho, MDF, cimento, metal ou madeira.';",
           ": 'Qual cola usar no mosaico.';")


def m_sem_banco_fica_sem_etiqueta(raiz):
    """A saida da TRAVA 2 desaparece e a pagina fica sem description nenhuma no
    mundo em que o desembarque do dado falhou."""
    trocar(raiz, F2,
           "\treturn '' !== $com_numero\n\t\t? $com_numero\n\t\t: 'Qual cola e qual rejunte usar no mosaico",
           "\treturn $com_numero;\n\t$nunca = ( '' !== $com_numero )\n\t\t? $com_numero\n\t\t: 'Qual cola e qual rejunte usar no mosaico")


def m_f1_promete_fonte_sem_banco(raiz):
    """A F1 passa a prometer "a medida que o fabricante publica" mesmo quando o
    banco do fabricante nao chegou ao site."""
    trocar(raiz, F1, "$com_numero = cdm_f1_banco_chegou() ? cdm_casca_preencher_promessa(",
           "$com_numero = true ? cdm_casca_preencher_promessa(")


MUTACOES = [
    ("o NOME da cola digitado no molde em vez de vir do banco", m_nome_do_lider_digitado),
    ("o lider conta os cartoes de SEGUNDA linha", m_lider_conta_os_segundos),
    ("o EMPATE no topo deixa de ser recusado", m_empate_nao_e_recusado),
    ("a FATIA sai do titulo e a cola sobra sozinha", m_lider_sem_fatia),
    ("a fatia arredonda para CIMA", m_fatia_arredonda_para_cima),
    ("o teto de 160 da description da F2 deixa de ser portao", m_faixa_da_description_sem_portao),
    ("TRAVA 1 desligada: promessa entra estourando o teto", m_teto_ignorado),
    ("TRAVA 1 afrouxada de 65 para 120", m_teto_afrouxado),
    ("TRAVA 2 desligada: zero vira promessa", m_zero_vira_promessa),
    ("molde cru com chave sobrando vai para a SERP", m_molde_cru_escapa),
    ("o NOME da pagina cede o lugar em vez da marca", m_o_nome_cede_o_lugar),
    ("a pagina parada (Trencadis) ganha promessa", m_trencadis_ganha_promessa),
    ("a description do Picassiete volta aos 192 caracteres", m_picassiete_volta_aos_192),
    ("a description do Trencadis volta aos 189 caracteres", m_trencadis_volta_aos_189),
    ("a home ganha promessa que ninguem mediu", m_a_home_ganha_promessa),
    ("uma segunda camada monta o proprio <title>", m_segundo_montador_de_titulo),
    ("a faixa da F1 sai de outra conta que nao a da tabela", m_faixa_da_f1_de_outra_conta),
    ("a promessa da F1 volta ao inventario de pecas", m_promessa_da_f1_volta_ao_inventario),
    ("o minimo e o maximo trocam de lugar na faixa da F1", m_faixa_da_f1_invertida),
    ("as colas contadas com o banco inteiro, rejuntes dentro", m_colas_contadas_com_o_banco_inteiro),
    ("a frase sem numero da TRAVA 2 fica curta demais", m_frase_sem_numero_curta),
    ("sem banco, a pagina fica sem description nenhuma", m_sem_banco_fica_sem_etiqueta),
    ("a F1 promete a fonte do fabricante sem o banco do fabricante", m_f1_promete_fonte_sem_banco),
]


def rodar_bancadas(raiz):
    """Devolve (reprovou, quem_reprovou). Para na primeira que reprova: o que
    interessa e SE a mutacao foi vista, e por quem."""
    for teste in BANCADAS:
        r = subprocess.run(["php", os.path.join(raiz, "ferramentas", teste), raiz],
                           capture_output=True, text=True)
        if r.returncode != 0:
            primeira = ""
            for linha in (r.stdout + r.stderr).splitlines():
                if linha.strip().startswith("FALHA"):
                    primeira = " ".join(linha.split())[6:]
                    break
            return True, "%s | %s" % (teste, primeira[:80])
    return False, ""


def main():
    reprovou, quem = rodar_bancadas(ILHA)
    if reprovou:
        print("A ilha de verdade ja esta reprovada — conserte antes de mutar.")
        print("  " + quem)
        return 1
    print("as quatro bancadas intactas: APROVADAS (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-promessa-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)
            reprovou, quem = rodar_bancadas(copia)
            if reprovou:
                print("  reprovou como devia: %-62s | %s" % (nome, quem))
            else:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
        except AssertionError as erro:
            passaram.append("%s (a mutacao nao conseguiu ser escrita: %s)" % (nome, erro))
            print("  MUTACAO INVALIDA: %s — %s" % (nome, erro))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram" %
          (len(MUTACOES), len(MUTACOES) - len(passaram), len(passaram)))
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
