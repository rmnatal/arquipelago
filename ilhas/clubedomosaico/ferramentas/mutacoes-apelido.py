#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra de proposito o apelido de endereco COM NIVEL (casca 1.22.0), uma
mutacao por vez, e exige que `teste-casca.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-apelido.py

POR QUE ESTE ARQUIVO EXISTE, e a causa tem data. A secao 8 do ARQUIPELAGO.md diz
que trava verde que nunca foi vista reprovar nao mediu nada. O mecanismo de
apelido desta ilha e de 11/09 e passou quase um mes servindo 301 para quatro
enderecos de UM segmento — e nenhuma bancada jamais o viu reprovar, porque a
unica afirmacao sobre ele cobrava a RECUSA de caminho com nivel. A recusa estava
errada, e so se descobriu isso medindo no ar em 09/10: os enderecos abandonados
desta ilha (os tres desenhos da camada de colecao da Loja, M9 do Pente Fino de
21/09) TEM nivel, e o unico mecanismo que podia alcanca-los recusava a familia
inteira numa linha.

O QUE SE MEDE AQUI e exatamente o que torna um 301 pior que o 404 que ele
substitui: redirecionar endereco que EXISTE (tira pagina do ar), redirecionar
para endereco que NAO existe (301 para 404), casar caminho por prefixo ou por
string inteira (manda o visitante para a Loja a partir de qualquer endereco que
comece por `loja/`), e sombrear o caminho de pagina que AINDA NAO NASCEU — o
caso com nome: `materiais/pastilhas` e slug reservado da categoria G-PASTILHAS
do Guia, que a 16.5 ainda nao autoriza, e um apelido ali ficaria verde hoje e
tiraria a categoria do ar no dia em que ela nascesse.

Cada mutacao roda numa COPIA da pasta da ilha, em mkdtemp. Nada aqui toca a
arvore de verdade — e por isso este arquivo NAO aparece em
`grep -L 'mkdtemp\\|copytree' ferramentas/mutacoes-*.py`.
Ferramenta de bancada: nunca vai para o site.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = os.path.join("snippets", "clubedomosaico-casca.php")
TESTE = os.path.join("ferramentas", "teste-casca.php")


def ler(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as fh:
        return fh.read()


def gravar(raiz, rel, texto):
    with open(os.path.join(raiz, rel), "w", encoding="utf-8") as fh:
        fh.write(texto)


def trocar(raiz, rel, de, para, quantas=1):
    """Troca e AFIRMA que trocou. Mutacao que nao se escreve e mutacao que
    passa por engano, e passar por engano se conta como falha da trava."""
    texto = ler(raiz, rel)
    achados = texto.count(de)
    assert achados == quantas, "esperava %d ocorrencia(s) de %r, achei %d" % (quantas, de[:60], achados)
    gravar(raiz, rel, texto.replace(de, para))


# ------------------------------------------------------------------ mutacoes

def m_apelido_sombreia_categoria_reservada(raiz):
    """O caso com nome: a categoria G-PASTILHAS do Guia tem o slug
    `materiais/pastilhas` reservado e ainda nao nasceu (a 16.5 nao autoriza).
    Um apelido ali fica verde hoje e tira a categoria do ar no dia em que ela
    nascer — que e o pior dia possivel para descobrir isto."""
    trocar(raiz, CASCA,
           "\t$mapa['loja/colecao'] = 'loja';",
           "\t$mapa['loja/colecao'] = 'loja';\n\t$mapa['materiais/pastilhas'] = 'materiais';")


def m_apelido_sombreia_categoria_no_ar(raiz):
    """A irma da de cima, no caso que doi hoje e nao amanha:
    `materiais/acabamento` e a UNICA categoria do Guia publicada."""
    trocar(raiz, CASCA,
           "\t$mapa['loja/colecao'] = 'loja';",
           "\t$mapa['loja/colecao'] = 'loja';\n\t$mapa['materiais/acabamento'] = 'materiais';")


def m_apelido_sombreia_a_ferramenta_pelo_caminho(raiz):
    """A ferramenta da cola e a pagina que mais ranqueia nesta ilha, e o
    caminho dela tem nivel. Sombrea-la e perder a unica posicao de primeira
    pagina que esta ilha conquistou por consulta de compra."""
    trocar(raiz, CASCA,
           "\t$mapa['loja/colecao'] = 'loja';",
           "\t$mapa['loja/colecao'] = 'loja';\n\t$mapa['materiais/qual-cola-usar-no-mosaico'] = 'materiais';")


def m_apelido_sombreia_filha_de_tres_degraus(raiz):
    """O sombreamento que a comparacao por SLUG deixaria passar: a filha mora em
    tres degraus e o portao tem de medir o caminho inteiro."""
    trocar(raiz, CASCA,
           "\t$mapa['loja/colecao'] = 'loja';",
           "\t$mapa['loja/colecao'] = 'loja';\n\t$mapa['materiais/acabamento/verniz-para-peca-de-mosaico'] = 'materiais';")


def m_destino_que_nao_existe(raiz):
    """301 para endereco que nao existe e pior que o 404 original — e o proprio
    comentario da secao 1b diz isso desde 11/09."""
    trocar(raiz, CASCA,
           "\t$mapa['loja/colecao'] = 'loja';",
           "\t$mapa['loja/colecao'] = 'loja';\n\t$mapa['loja/novidades'] = 'colecao-que-nunca-nasceu';")


def m_apelido_sem_barra_na_tabela_com_nivel(raiz):
    """As duas tabelas tem reguas diferentes, e misturar as duas e como o
    portao perde a regua: apelido de um segmento na tabela com nivel nunca
    seria alcancado pela resolucao, porque ela so consulta esta tabela quando o
    caminho pedido TEM barra. Apelido que nunca dispara parece configurado."""
    trocar(raiz, CASCA,
           "\t$mapa['loja/colecao'] = 'loja';",
           "\t$mapa['loja/colecao'] = 'loja';\n\t$mapa['colecoes'] = 'loja';")


def m_apelido_com_barra_na_tabela_de_um_segmento(raiz):
    """O espelho da de cima: apelido com nivel escrito na tabela de UM segmento
    tambem nunca dispara, e e o engano mais provavel de quem nao leu as duas."""
    trocar(raiz, CASCA,
           "\t\t'quem-somos'                 => 'sobre',",
           "\t\t'quem-somos'                 => 'sobre',\n\t\t'loja/novidades'             => 'loja',")


def m_casamento_por_prefixo(raiz):
    """A forma mais plausivel de errar a resolucao: casar por prefixo em vez de
    por caminho inteiro. Manda para a Loja todo endereco que COMECE por um
    apelido conhecido — inclusive `/loja/vasos/azul/grande/`, que ninguem
    escreveu em documento nenhum."""
    trocar(raiz, CASCA,
           "\t$mapa = cdm_casca_apelidos_de_caminho();\n\n\treturn isset( $mapa[ $caminho ] ) ? $mapa[ $caminho ] : '';",
           "\t$mapa = cdm_casca_apelidos_de_caminho();\n\n\tforeach ( $mapa as $chave => $destino ) {\n\t\tif ( 0 === strpos( $caminho, $chave ) ) { return $destino; }\n\t}\n\n\treturn '';")


def m_normalizacao_pela_string_inteira(raiz):
    """`sanitize_title( 'loja/vasos' )` devolve `lojavasos`. Normalizar a string
    inteira em vez de degrau por degrau faz o mapa parar de casar com tudo — e o
    sintoma e silencioso: nenhum erro, so 404 de volta."""
    trocar(raiz, CASCA,
           "\t$partes = explode( '/', trim( (string) $caminho, '/' ) );\n\t$limpas = array();",
           "\t$partes = array( sanitize_title( trim( (string) $caminho, '/' ) ) );\n\t$limpas = array();")


def m_a_tabela_com_nivel_fica_vazia(raiz):
    """O desembarque que esquece o mapa: o mecanismo aprende nivel e nenhum
    endereco entra. Verde em tudo, e os tres desenhos do M9 continuam em 404."""
    trocar(raiz, CASCA,
           "\t$termos = array( 'vasos', 'colares', 'quadros', 'centro-de-mesa', 'presentes', 'jardim' );",
           "\t$termos = array();")


def m_um_termo_do_m9_cai(raiz):
    """O M9 nomeia seis termos. Cinco nao sao seis, e quem conferir pelo olho
    nao ve a diferenca."""
    trocar(raiz, CASCA,
           "'vasos', 'colares', 'quadros', 'centro-de-mesa', 'presentes', 'jardim'",
           "'vasos', 'colares', 'quadros', 'centro-de-mesa', 'presentes'")


def m_so_o_desenho_do_tipo_de_peca_entra(raiz):
    """Metade do achado do M9: entra o desenho do ARVORE.md e fica fora o do
    PROMPT.md com o segmento `colecao`. Endereco abandonado pela metade."""
    trocar(raiz, CASCA,
           "\t\t$mapa[ 'loja/colecao/' . $termo ]   = 'loja';",
           "\t\t/* mutacao: o desenho com `colecao` nao entra */")


def m_so_o_desenho_com_colecao_entra(raiz):
    """A outra metade, pelo outro lado."""
    trocar(raiz, CASCA,
           "\t\t$mapa[ 'loja/' . $termo ]           = 'loja';",
           "\t\t/* mutacao: o desenho pelo tipo de peca nao entra */")


def m_degrau_vazio_vira_degrau(raiz):
    """`//loja///vasos//` chega assim de link quebrado de terceiro. Degrau vazio
    que entra no caminho normalizado faz o mapa nunca casar."""
    trocar(raiz, CASCA,
           "\t\tif ( '' !== $parte ) {\n\t\t\t$limpas[] = $parte;\n\t\t}",
           "\t\t$limpas[] = $parte;")


MUTACOES = [
    ("apelido sombreia a categoria RESERVADA do Guia", m_apelido_sombreia_categoria_reservada),
    ("apelido sombreia a categoria do Guia que esta NO AR", m_apelido_sombreia_categoria_no_ar),
    ("apelido sombreia a FERRAMENTA que mais ranqueia", m_apelido_sombreia_a_ferramenta_pelo_caminho),
    ("apelido sombreia filha de TRES degraus", m_apelido_sombreia_filha_de_tres_degraus),
    ("301 para destino que nao existe", m_destino_que_nao_existe),
    ("apelido SEM barra na tabela com nivel", m_apelido_sem_barra_na_tabela_com_nivel),
    ("apelido COM barra na tabela de um segmento", m_apelido_com_barra_na_tabela_de_um_segmento),
    ("a resolucao casa por PREFIXO em vez de caminho inteiro", m_casamento_por_prefixo),
    ("a normalizacao usa a string inteira em vez de degrau", m_normalizacao_pela_string_inteira),
    ("a tabela com nivel fica VAZIA", m_a_tabela_com_nivel_fica_vazia),
    ("um dos seis termos do M9 cai", m_um_termo_do_m9_cai),
    ("so o desenho pelo tipo de peca entra", m_so_o_desenho_do_tipo_de_peca_entra),
    ("so o desenho com o segmento `colecao` entra", m_so_o_desenho_com_colecao_entra),
    ("degrau vazio entra no caminho normalizado", m_degrau_vazio_vira_degrau),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, TESTE), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A casca de verdade ja esta reprovada — conserte antes de mutar.")
        print(base_saida[-2000:])
        return 1
    print("casca intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-apelido-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)
            rc, saida = rodar_teste(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if linha.strip().startswith("FALHA"):
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia: %-54s | %s" % (nome, primeira[:92]))
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
