#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a casca 1.2.0 de proposito, uma mutacao por vez, e exige que
`teste-casca.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-voz-e-cabeca.py

Por que este arquivo existe: as travas do bloco do despacho — cabecalho claro,
portao de voz, camada de prova, denominador contado, noindex, PNG que abre —
ficaram verdes na primeira execucao. Verde na primeira execucao e bom sinal e
prova nenhuma: a secao 8 do ARQUIPELAGO.md diz que trava que ninguem viu
reprovar nao mediu nada.

As mutacoes que mais valem aqui NAO sao as obvias. Sao tres:

  * a PORTA DOS FUNDOS da camada de prova — embrulhar a pagina inteira na classe
    que declara prova, ou declarar uma segunda pagina como pagina de prova.
    Quem escreve o portao de voz por estrutura precisa provar que a estrutura
    nao pode ser declarada a vontade, senao o portao se desliga sozinho;
  * a FRASE QUE JUNTA DOIS NUMEROS CERTOS — trocar o denominador de volta para a
    categoria cola devolve ao ar "10 dos 5 itens", que foi o defeito real;
  * o PNG QUE PARECE IMAGEM — trocar o favicon embutido por bytes cortados, que
    e o que o lotus-512.png e hoje.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCA = os.path.join("snippets", "clubedomosaico-casca.php")


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

def m_cabecalho_volta_ao_preto(raiz):
    """A reclamacao do Raphael, refeita: o cabecalho volta a ser um bloco preto."""
    trocar(raiz, CASCA,
           "header.wp-block-group,body .wp-block-template-part header{background:var(--cdm-papel)",
           "header.wp-block-group,body .wp-block-template-part header{background:var(--cdm-noite)")


def m_cabecalho_separa_por_sombra(raiz):
    """Linha de 1 px vira sombra — a secao 6 proibe, e a olho quase nao muda."""
    trocar(raiz, CASCA,
           "border-bottom:1px solid var(--cdm-traco);box-shadow:none;",
           "box-shadow:0 6px 18px rgba(31,23,21,.18);")


def m_menu_branco_esquecido(raiz):
    """O caso REAL de quem troca so o fundo: o texto do menu fica branco no branco."""
    trocar(raiz, CASCA,
           ".cdm-nav a,.cdm-nav .cdm-sem-link{font-family:var(--cdm-texto);font-weight:500;font-size:.95rem;color:var(--cdm-tinta)",
           ".cdm-nav a,.cdm-nav .cdm-sem-link{font-family:var(--cdm-texto);font-weight:500;font-size:.95rem;color:var(--cdm-papel)")


def m_logo_de_fundo_preto_volta(raiz):
    """O arquivo com fundo preto volta ao cabecalho claro — retangulo escuro."""
    trocar(raiz, CASCA,
           "$html .= '<span class=\"cdm-marca-nome\">clube do mosaico</span>';",
           "$html .= '<img src=\"' . esc_url( CDM_CASCA_LOGO_URL ) . '\" alt=\"Clube do Mosaico\">';")


def m_home_volta_a_ser_inicio(raiz):
    """O titulo da home volta a ser a palavra Inicio, que e o H1 que o tema imprime."""
    trocar(raiz, CASCA,
           "'inicio'                  => array( 'titulo' => 'Mosaico feito à mão, uma peça por vez'",
           "'inicio'                  => array( 'titulo' => 'Início'")


def m_titulo_para_de_sincronizar(raiz):
    """O defeito POR TRAS do Inicio: a pagina nasce com um titulo e fica com ele.

    Mutacao silenciosa — o H1 servido continua certo numa instalacao nova, e so
    quem ja tem a pagina no ar carrega o titulo velho para sempre."""
    trocar(raiz, CASCA,
           "if ( $nossa && trim( (string) $pagina->post_title ) !== $def['titulo'] ) {",
           "if ( false && trim( (string) $pagina->post_title ) !== $def['titulo'] ) {")


def m_ficha_tecnica_na_home(raiz):
    """A frase que o VOZ.md proibe pelo nome, de volta ao primeiro paragrafo."""
    trocar(raiz, CASCA,
           "$html .= '<p>Vaso, cachepô, quadro, espelho, colar:",
           "$html .= '<p>A ficha técnica BRSA004 lista as superfícies proibidas. Vaso, cachepô, quadro, espelho, colar:")


def m_termo_de_manual_no_titulo(raiz):
    """Termo da lista de proibidas na linha de abertura do Guia."""
    trocar(raiz, CASCA,
           "<p class=\"cdm-linha-mestra\">Antes do primeiro caco, duas perguntas: sobre o que você vai colar, e onde a peça vai ficar.</p>",
           "<p class=\"cdm-linha-mestra\">Especificação de aderência por substrato: o parâmetro que decide a tessela.</p>")


def m_porta_dos_fundos_pagina_inteira(raiz):
    """A PORTA DOS FUNDOS: embrulhar o Guia inteiro na classe da camada de prova.

    Sem contar os blocos e sem medir onde eles comecam, o portao de voz se
    desligaria com uma linha e nenhuma palavra mudaria na tela."""
    texto = ler(raiz, CASCA)
    alvo = "add_shortcode( 'cdm_materiais', function () {\n\t$n = cdm_casca_numeros();\n\n\t$html  = '<div class=\"cdm-bloco\">';"
    assert alvo in texto, "alvo do embrulho nao encontrado"
    texto = texto.replace(alvo, alvo + "\n\t$html .= '<div class=\"cdm-prova\">';", 1)
    texto = texto.replace("\t$html .= '</div>';\n\n\treturn $html;\n} );\n\n/**\n * /materiais/como-sabemos/",
                          "\t$html .= '</div></div>';\n\n\treturn $html;\n} );\n\n/**\n * /materiais/como-sabemos/", 1)
    gravar(raiz, CASCA, texto)


def m_porta_dos_fundos_segunda_pagina_de_prova(raiz):
    """A outra porta: declarar a home tambem como camada de prova."""
    trocar(raiz, CASCA,
           "'inicio'                  => array( 'titulo' => 'Mosaico feito à mão, uma peça por vez', 'conteudo' => '[cdm_home]' ),",
           "'inicio'                  => array( 'titulo' => 'Mosaico feito à mão, uma peça por vez', 'conteudo' => '[cdm_home]', 'camada' => 'prova' ),")


def m_prova_antes_do_texto(raiz):
    """A prova sobe para o topo do Guia: vira a voz da pagina em vez do rodape dela."""
    texto = ler(raiz, CASCA)
    inicio = texto.index("\t$html .= '<div class=\"cdm-prova\">';\n\t$html .= '<h2>Como sabemos</h2>';")
    fim = texto.index("\t$html .= '</div>';\n\t$html .= '</div>';\n\n\treturn $html;\n} );", inicio)
    bloco = texto[inicio:fim] + "\t$html .= '</div>';\n"
    texto = texto[:inicio] + texto[inicio + len(bloco):]
    ancora = "\t$html  = '<div class=\"cdm-bloco\">';\n\t$html .= '<div class=\"cdm-abertura\">';\n\t$html .= '<p class=\"cdm-linha-mestra\">Antes do primeiro caco"
    assert ancora in texto
    texto = texto.replace(ancora, "\t$html  = '<div class=\"cdm-bloco\">';\n" + bloco + "\t$html .= '<div class=\"cdm-abertura\">';\n\t$html .= '<p class=\"cdm-linha-mestra\">Antes do primeiro caco", 1)
    gravar(raiz, CASCA, texto)


def m_denominador_volta_para_a_categoria(raiz):
    """O DEFEITO REAL, refeito: "10 dos 5 itens esperam link".

    Os dois numeros continuam certos sozinhos. E exatamente por isso que so um
    teste que olha a FRASE — e nao cada metade — enxerga."""
    trocar(raiz, CASCA,
           "$html .= '<p>Hoje o banco tem ' . cdm_casca_num( $n['itens_no_banco'] ) . ' itens de fabricante",
           "$html .= '<p>Hoje o banco tem ' . cdm_casca_num( $n['materiais_cola'] ) . ' itens de fabricante")


def m_total_digitado(raiz):
    """O total da ilha volta a ser digitado, e fica certo hoje e errado amanha."""
    trocar(raiz, CASCA,
           "\t$n['itens_no_banco'] = 0;\n\tforeach ( $bancos as $chave ) {\n\t\t$n['itens_no_banco'] += (int) $n[ $chave ];\n\t}",
           "\t$n['itens_no_banco'] = 12;")


def m_noindex_na_pagina_errada(raiz):
    """`noindex` indevido: o Guia sai do indice sem ninguem ver na tela."""
    trocar(raiz, CASCA,
           "'materiais'               => array( 'titulo' => 'Materiais', 'conteudo' => '[cdm_materiais]' ),",
           "'materiais'               => array( 'titulo' => 'Materiais', 'conteudo' => '[cdm_materiais]', 'noindex' => true ),")


def m_pagina_de_prova_volta_ao_sitemap(raiz):
    """A pagina de bastidor volta a gastar orcamento de rastreamento."""
    trocar(raiz, CASCA,
           "'pai' => 'materiais', 'noindex' => true, 'camada' => 'prova' ),",
           "'pai' => 'materiais', 'camada' => 'prova' ),")


def m_filha_sem_mae(raiz):
    """Pagina de nivel 2 sem mae declarada: nasce solta na raiz."""
    trocar(raiz, CASCA,
           "'pai' => 'materiais', 'noindex' => true, 'camada' => 'prova' ),",
           "'noindex' => true, 'camada' => 'prova' ),")


def m_favicon_cortado(raiz):
    """O PNG embutido vira bytes cortados — o estado em que o lotus-512.png esta.

    A trava velha ("existe e comeca com a assinatura de PNG") aprova isto."""
    texto = ler(raiz, CASCA)
    achado = re.search(r"define\( 'CDM_CASCA_ICONE_PNG_32', '([^']+)' \);", texto)
    assert achado, "nao achei o favicon embutido"
    cortado = achado.group(1)[: int(len(achado.group(1)) * 0.6)]
    gravar(raiz, CASCA, texto.replace(achado.group(1), cortado, 1))


def m_pagina_fina(raiz):
    """A pagina mais curta perde o miolo e vai para o sitemap magra.

    A primeira versao desta mutacao cortava caracteres de uma pagina com folga —
    mutacao que nao mede nada. Esta corta a MENOR das nove, que e a Loja."""
    texto = ler(raiz, CASCA)
    inicio = texto.index("\t$html .= '<div class=\"cdm-secao\">';\n\t$html .= '<h2>Como a compra vai funcionar</h2>';")
    fim = texto.index("\t$html .= '</ul></div>';", inicio) + len("\t$html .= '</ul></div>';\n")
    gravar(raiz, CASCA, texto[:inicio] + texto[fim:])


def m_bancada_mede_um_processo_so(raiz):
    """A cicatriz da bancada: as nove paginas voltam a ser montadas no mesmo
    processo, e oito delas perdem o rodape em silencio."""
    trocar(raiz, os.path.join("ferramentas", "teste-casca.php"),
           "\t$html_por_pagina[ $tag ] = cdm_render_em_processo_proprio( $raiz, $tag );",
           "\t$html_por_pagina[ $tag ] = cdm_teste_pagina( $tag );")


MUTACOES = [
    ("cabecalho volta ao preto", m_cabecalho_volta_ao_preto),
    ("cabecalho separa por sombra em vez de linha", m_cabecalho_separa_por_sombra),
    ("fundo trocado e texto do menu esquecido no branco", m_menu_branco_esquecido),
    ("logo de fundo preto volta ao cabecalho claro", m_logo_de_fundo_preto_volta),
    ("a home volta a se chamar Inicio", m_home_volta_a_ser_inicio),
    ("o titulo para de sincronizar (o defeito por tras do Inicio)", m_titulo_para_de_sincronizar),
    ("ficha tecnica de volta ao primeiro paragrafo da home", m_ficha_tecnica_na_home),
    ("termo de manual na linha de abertura do Guia", m_termo_de_manual_no_titulo),
    ("PORTA DOS FUNDOS: pagina inteira embrulhada como prova", m_porta_dos_fundos_pagina_inteira),
    ("PORTA DOS FUNDOS: segunda pagina declarada como prova", m_porta_dos_fundos_segunda_pagina_de_prova),
    ("a camada de prova sobe para antes do texto", m_prova_antes_do_texto),
    ("denominador volta para a categoria (10 dos 5 itens)", m_denominador_volta_para_a_categoria),
    ("total da ilha digitado a mao", m_total_digitado),
    ("noindex na pagina errada", m_noindex_na_pagina_errada),
    ("pagina de bastidor volta ao sitemap", m_pagina_de_prova_volta_ao_sitemap),
    ("filha de nivel 2 sem mae declarada", m_filha_sem_mae),
    ("PNG embutido cortado pela metade", m_favicon_cortado),
    ("a menor pagina fica fina", m_pagina_fina),
    ("bancada volta a medir nove paginas num processo so", m_bancada_mede_um_processo_so),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-casca.php"), raiz],
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
        tmp = tempfile.mkdtemp(prefix="mut-")
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
                print("  reprovou como devia: %-56s | %s" % (nome, primeira[:90]))
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
