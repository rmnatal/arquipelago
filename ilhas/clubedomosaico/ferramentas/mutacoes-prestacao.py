#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a prestacao de contas do rejunte de proposito, uma mutacao por vez, e
exige que `teste-prestacao-rejunte.php` REPROVE cada uma.

    python3 ferramentas/mutacoes-prestacao.py

Por que este arquivo existe: o portao da prestacao de contas nasceu VERDE
depois do conserto do despacho de 12/09/2026, e teste verde que nunca foi visto
reprovar nao mediu nada (secao 8 do ARQUIPELAGO.md). As duas primeiras mutacoes
sao os DOIS DEFEITOS ORIGINAIS, escritos de volta: se alguma delas passar, o
portao nao protege nada do que foi despachado.

O QUE ESTE ARQUIVO PROCURA, e que e a armadilha propria desta familia de
defeito: nenhuma mutacao abaixo quebra a pagina. Todas deixam a ferramenta
respondendo, bonita, com numero certo e frase bem escrita. O que elas quebram e
a CORRESPONDENCIA entre o que a pagina afirma e o que ela lista — que e
exatamente o tipo de defeito que passa por revisao humana e por teste de HTTP
200, e que so uma regua propria pega.

Cada uma roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F1 = os.path.join("snippets", "clubedomosaico-f1.php")
F2 = os.path.join("snippets", "clubedomosaico-f2.php")


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


# ------------------------------------ os dois defeitos do despacho, de volta

def m_f1_volta_a_culpar_a_folga(raiz):
    """O DEFEITO 1 DO DESPACHO, literal: a recusa volta a culpar a folga, em
    bloco, sem olhar qual foi a causa. E a frase que a Sentinela leu no ar em
    12/09/2026 com `onde=externo_exposto`, enquanto a folga cabia."""
    editar(raiz, F1,
           "$html .= '<p class=\"cdm-f1-faixa\">Nenhum ' . esc_html( $nome_tipo ) . ' do nosso banco serve para essa peça '\n"
           "\t\t\t. ( $lugar ? esc_html( $lugar ) : '' ) . ', com ' . $mm . ' de folga.</p>';",
           "$html .= '<p class=\"cdm-f1-faixa\">Nenhum rejunte do nosso banco declara folga de ' . $mm . '. '\n"
           "\t\t\t. 'Ou a folga que você quer está fora da faixa que os fabricantes publicam, ou o produto não declara essa largura.</p>';")


def m_f2_a_frase_volta_a_nomear_so_o_topo(raiz):
    """O DEFEITO 2 DO DESPACHO, literal: a frase volta a nomear so o topo e a
    vitrine continua servindo os elegiveis abaixo dele. Um a recomendar, quatro
    a vender — o estado exato que a Sentinela mediu."""
    editar(raiz, F2,
           "\t\tif ( $celula['elegiveis_abaixo_do_topo'] ) {\n"
           "\t\t\t$segundos = cdm_f2_rejunte_nomes( $celula['elegiveis_abaixo_do_topo'] );",
           "\t\tif ( false && $celula['elegiveis_abaixo_do_topo'] ) {\n"
           "\t\t\t$segundos = cdm_f2_rejunte_nomes( $celula['elegiveis_abaixo_do_topo'] );")


def m_f1_a_prestacao_so_sai_quando_a_lista_esta_vazia(raiz):
    """O BURACO QUE O PROPRIO PORTAO ACHOU no conserto, antes do desembarque: a
    prestacao de contas volta a sair so quando nao ha produto para listar, e o
    terceiro cimenticio some da tela sem que nada diga por que.

    A PRIMEIRA VERSAO DESTA MUTACAO NAO MORDEU, e vale registrar por que: ela
    condicionava a linha de `fora_lugar`, e com o banco de hoje `fora_lugar` e
    `do_tipo` NUNCA sao verdadeiros ao mesmo tempo — os dois cimenticios tem a
    mesma faixa e as mesmas declaracoes, entao ou os dois servem ou os dois
    caem. O estado em que o defeito aparece e o de `sem_faixa`: o rejunte
    piscinas fica de fora em TODA combinacao, inclusive quando a lista de cima
    tem produto. Mutacao tem de escolher o alvo que existe no mundo do banco,
    nao o que parece simetrico no codigo."""
    editar(raiz, F1,
           "\tif ( $sem_faixa ) {\n"
           "\t\t$html .= '<p class=\"cdm-f1-faixa\">De '",
           "\tif ( $sem_faixa && ! $do_tipo ) {\n"
           "\t\t$html .= '<p class=\"cdm-f1-faixa\">De '")


# --------------------------------------------- a contabilidade, sabotada

def m_f2_o_grupo_de_ressalva_volta_a_ser_invisivel(raiz):
    """O QUINTO ESTADO SOME de novo.

    ESTA E A MUTACAO QUE QUASE SAIU INERTE, e a licao e a mesma que a Robometria
    pagou em 11/09: hoje o banco nao tem rejunte de fonte fraca, entao apagar a
    linha do grupo de ressalva nao muda UM BYTE da tela. Para ela morder e
    preciso PRODUZIR O MUNDO em que o defeito aparece — e nas duas metades, ou
    ela reprova pelo motivo errado: o snippet le o nivel das `fontes` do banco,
    e a regua deste portao le o nivel dos perfis escritos a mao. Rebaixar so uma
    faria o teste acusar divergencia entre banco e esquema, que e outro defeito,
    e a trava da ressalva continuaria nao medida."""
    rebaixar_o_epoxi(raiz)
    editar(raiz, F2,
           "\tif ( $celula['mencionados_com_ressalva'] ) {\n"
           "\t\t/* O QUINTO ESTADO",
           "\tif ( false && $celula['mencionados_com_ressalva'] ) {\n"
           "\t\t/* O QUINTO ESTADO")


def rebaixar_o_epoxi(raiz):
    """O mundo em que existe rejunte elegivel sustentado so por fonte fraca: as
    duas fontes do epoxi caem para o nivel 5, no banco E no perfil escrito a
    mao. Nada mais muda — ele continua cobrindo 1 a 5 mm e declarando os mesmos
    ambientes, entao ele passa nas regras 1 a 3 e cai so na regra 4."""
    banco = os.path.join(raiz, "dados", "materiais-rejuntes.json")
    with open(banco, encoding="utf-8") as fh:
        d = json.load(fh)
    achou = False
    for m in d["materiais"]:
        if m["id"] == "quartzolit-rejunte-epoxi":
            for f in m.get("fontes", {}).values():
                f["nivel"] = 5
                achou = True
    if not achou:
        raise AssertionError("mutacao INERTE: nao achei as fontes do rejunte epoxi no banco")
    with open(banco, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)

    esq = os.path.join(raiz, "dados", "esquema-banco.json")
    with open(esq, encoding="utf-8") as fh:
        e = json.load(fh)
    achou = False
    for p in e["perfis_esperados_do_rejunte"]["perfis"]:
        if p["id"] == "quartzolit-rejunte-epoxi":
            p["nivel"] = 5
            achou = True
    if not achou:
        raise AssertionError("mutacao INERTE: nao achei o perfil do rejunte epoxi no esquema")
    with open(esq, "w", encoding="utf-8") as fh:
        json.dump(e, fh, ensure_ascii=False, indent=1)


def m_f2_a_tabela_volta_a_contar_so_dois_grupos(raiz):
    """A tabela pre-renderizada — a metade que um modelo de linguagem le sem
    formulario — volta a esquecer um grupo no "fora", e as NOVE linhas param de
    somar os 5 rejuntes do banco.

    O alvo e o grupo de faixa nao obtida, e nao o de ressalva, pelo motivo que a
    mutacao do quinto estado ja ensinou: ressalva esta vazia com o banco de
    hoje, entao apagar a contagem dela nao mudaria numero nenhum na tabela. O
    rejunte piscinas, sim, esta fora em todas as nove linhas."""
    editar(raiz, F2,
           "\t\tif ( $t_sem ) {\n"
           "\t\t\t$fora[] = count( $t_sem ) . ' porque a faixa de folga dele não foi obtida';",
           "\t\tif ( false && $t_sem ) {\n"
           "\t\t\t$fora[] = count( $t_sem ) . ' porque a faixa de folga dele não foi obtida';")


def m_f2_a_vitrine_ganha_um_produto_que_a_frase_nao_nomeia(raiz):
    """O empurrao classico: a vitrine passa a servir tambem quem foi eliminado
    pelo lugar. A frase continua honesta, a lista nao — e o bloco de compra e o
    espaco mais caro da pagina."""
    editar(raiz, F2,
           "\t\tforeach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'] ) as $id ) {\n"
           "\t\t\t$p      = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );",
           "\t\tforeach ( array_merge( $celula['recomendados_topo'], $celula['elegiveis_abaixo_do_topo'], $celula['eliminados_por_ambiente'] ) as $id ) {\n"
           "\t\t\t$p      = cdm_f2_perfil_rejunte( $banco['materiais'][ $id ] );")


def m_f1_o_sem_faixa_vira_fora_pela_folga(raiz):
    """O produto cuja faixa a gente NUNCA conseguiu volta a ser reportado como
    se a folga nao coubesse. E afirmar sobre uma declaracao que nao foi lida —
    a diferenca entre nao ter dado e ter dado que exclui."""
    editar(raiz, F1,
           "\t\tif ( null === $p['junta_min'] || null === $p['junta_max'] ) {\n"
           "\t\t\t$sem_faixa[] = $id;\n"
           "\t\t} else {\n"
           "\t\t\t$fora_folga[] = $id;\n"
           "\t\t}",
           "\t\t$fora_folga[] = $id;")


def m_f1_a_linha_de_outro_tipo_volta_a_falar_so_de_folga(raiz):
    """A metade que produzia a contradicao: a linha de outro tipo volta a
    prometer so a folga, enquanto a celula ja filtrou tambem pelo lugar."""
    editar(raiz, F1,
           "De outro tipo, e que servem nessa folga e nesse lugar: ",
           "De outro tipo, mas dentro dessa folga: ")


def m_f1_a_acusacao_de_lugar_perde_o_nome(raiz):
    """A pagina para de dizer que quem exclui e o LUGAR. Ela nao passa a mentir
    — ela para de explicar, que e o estado em que o defeito original nasceu."""
    editar(raiz, F1,
           "' é o LUGAR, não a folga: ' . $mm . ' cabe na faixa que o fabricante publica para '",
           "' está fora desta combinação: ' . $mm . ' não resolve para '")


def m_f2_a_faixa_nao_obtida_vira_fora_pela_folga(raiz):
    """O gemeo da mutacao da F1, agora na F2: o produto cuja faixa a gente nunca
    conseguiu volta a ser contado como se o fabricante tivesse publicado uma
    faixa que nao cobre a folga.

    ESTA MUTACAO SUBSTITUI uma que nao media nada. A anterior desligava o ramo
    "so o lugar exclui" da frase de recusa — e aquele ramo era INALCANCAVEL com
    o banco de hoje, porque o rejunte piscinas cai sempre no balde da folga e
    nenhuma combinacao tem o lugar como causa unica. Uma mutacao sobre codigo
    morto e verde sem medir nada; o conserto foi tirar o ramo morto da pagina e
    apontar a mutacao para a distincao que existe."""
    editar(raiz, F2,
           "\t\tif ( null === $p['junta_min'] || null === $p['junta_max'] ) {\n"
           "\t\t\t$sem_faixa[] = $id;\n"
           "\t\t} else {\n"
           "\t\t\t$fora_folga[] = $id;\n"
           "\t\t}",
           "\t\t$fora_folga[] = $id;")


def m_o_segundo_e_promovido_a_primeiro(raiz):
    """A PROMOCAO SILENCIOSA, e e ela que so a regua propria pega: quem cobre a
    folga e nao tem o lugar declarado pelo fabricante passa a sair na frase
    principal, como se o fabricante o tivesse nomeado. A pagina fica impecavel —
    frase e vitrine concordam, a prestacao de contas fecha, o banco todo esta
    nomeado. O que muda e a autoridade da recomendacao, que e o produto da ilha.

    ESTA MUTACAO SUBSTITUI uma tentativa anterior que nao media nada: a versao
    antiga desligava a afirmacao da regua dentro do proprio teste, sem tocar em
    nenhuma pagina — e um teste que aprova uma pagina correta esta certo, nao
    furado. Porta dos fundos se mede com defeito de verdade na tela, e pedindo
    que a trava seja a unica capaz de ve-lo.

    E ELA PASSOU NA PRIMEIRA RODADA POR ERRO DE ALVO, que e a armadilha que o
    `mutacoes-f1.py` ja nomeia: a linha do score e IDENTICA, byte a byte, em
    `cdm_f2_avaliar_cola()` e em `cdm_f2_avaliar_rejunte()`, e a substituicao
    pegou a primeira — mutou a cola, que este portao nao mede, e o verde foi
    honesto. Por isso o alvo abaixo carrega a linha ANTERIOR, que e a unica
    diferenca entre as duas funcoes naquele ponto: `fora_do_ambiente` e do
    rejunte, `silencio` e da cola."""
    editar(raiz, F2,
           "\t\treturn array( 'fora_do_ambiente', 0 );\n"
           "\t}\n\n"
           "\t$score = 2 + ( isset( $p['ambientes_cobertos'][ $ambiente ] ) ? 2 : 0 );",
           "\t\treturn array( 'fora_do_ambiente', 0 );\n"
           "\t}\n\n"
           "\t$score = 4;")


MUTACOES = [
    ("F1 volta a culpar a folga em bloco (defeito 1 do despacho)", m_f1_volta_a_culpar_a_folga),
    ("F2 volta a nomear so o topo com quatro na vitrine (defeito 2)", m_f2_a_frase_volta_a_nomear_so_o_topo),
    ("F1 so presta contas quando a lista esta vazia", m_f1_a_prestacao_so_sai_quando_a_lista_esta_vazia),
    ("F2 volta a esconder o grupo de ressalva", m_f2_o_grupo_de_ressalva_volta_a_ser_invisivel),
    ("a tabela pre-renderizada volta a contar so dois grupos", m_f2_a_tabela_volta_a_contar_so_dois_grupos),
    ("a vitrine ganha um produto que a frase nao nomeia", m_f2_a_vitrine_ganha_um_produto_que_a_frase_nao_nomeia),
    ("F1 reporta como fora-pela-folga quem nao tem faixa", m_f1_o_sem_faixa_vira_fora_pela_folga),
    ("a linha de outro tipo volta a falar so de folga", m_f1_a_linha_de_outro_tipo_volta_a_falar_so_de_folga),
    ("a acusacao de lugar perde o nome", m_f1_a_acusacao_de_lugar_perde_o_nome),
    ("F2 conta como fora-pela-folga quem nao tem faixa", m_f2_a_faixa_nao_obtida_vira_fora_pela_folga),
    ("o segundo e promovido a primeiro na frase", m_o_segundo_e_promovido_a_primeiro),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-prestacao-rejunte.php"), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A prestacao de contas de verdade ja esta reprovada — conserte antes de mutar.")
        print("\n".join(l for l in base_saida.splitlines() if "FALHA" in l))
        return 1
    print("Prestacao de contas intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-prest-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [" + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue
            rc, saida = rodar_teste(copia)
            if rc == 0:
                passaram.append(nome)
                print("  PASSOU (a trava NAO viu): %s" % nome)
            else:
                primeira = ""
                for linha in saida.splitlines():
                    if "->" in linha:
                        primeira = " ".join(linha.split())[3:]
                        break
                print("  reprovou como devia: %-58s | %s" % (nome, primeira[:76]))
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
