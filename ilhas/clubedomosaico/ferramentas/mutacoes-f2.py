#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a F2 de proposito, uma mutacao por vez, e exige que `teste-f2.php`
REPROVE cada uma.

    python3 ferramentas/mutacoes-f2.py

Por que este arquivo existe: teste verde que nunca foi visto reprovar nao mediu
nada (secao 8 do ARQUIPELAGO.md). O teste da F2 ficou verde na primeira rodada,
o que e bom sinal e prova nenhuma. Cada mutacao abaixo e uma forma PLAUSIVEL de
esta ferramenta ficar errada em silencio — a maioria e um caractere trocado, do
tipo que passa numa revisao de codigo.

A ARMADILHA QUE JA CUSTOU CARO EM TRES ILHAS: mutacao que nao acha o alvo no
arquivo e verde sem medir nada. Por isso toda mutacao que edita texto CONFERE
que trocou alguma coisa e explode se nao trocou. Mutacao que nao morde nao e
mutacao.

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
SNIPPET = os.path.join("snippets", "clubedomosaico-f2.php")


def editar(raiz, arquivo, velho, novo, vezes=1):
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as fh:
        texto = fh.read()
    if texto.count(velho) < vezes:
        raise AssertionError(
            "mutacao INERTE: %r aparece %d vez(es) em %s, esperava %d"
            % (velho, texto.count(velho), arquivo, vezes))
    with open(caminho, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(velho, novo, vezes))


def carregar(raiz, nome):
    with open(os.path.join(raiz, "dados", nome), encoding="utf-8") as fh:
        return json.load(fh)


def gravar(raiz, nome, dado):
    with open(os.path.join(raiz, "dados", nome), "w", encoding="utf-8") as fh:
        json.dump(dado, fh, ensure_ascii=False, indent=2)


# --------------------------------------------------------------- as mutacoes

def m_proibicao_deixa_de_vencer(raiz):
    """A regra 1 cai: o produto proibido pelo fabricante volta a ser candidato.

    E a mutacao mais cara do arquivo. Ela poe o silicone acetico de volta em
    espelho e em cimento — que e exatamente o que a SERP faz e a razao de esta
    pagina existir."""
    editar(raiz, SNIPPET,
           "\tif ( isset( $p['bases_proibidas'][ $base ] ) || isset( $p['ambientes_proibidos'][ $ambiente ] ) ) {\n\t\treturn array( 'proibido', 0 );",
           "\tif ( false ) {\n\t\treturn array( 'proibido', 0 );")


def m_silencio_vira_pode(raiz):
    """A regra 2 cai: base sem declaracao passa a valer como indicada.

    O defeito de blog, escrito em PHP: silencio do fabricante virando 'pode'."""
    editar(raiz, SNIPPET,
           "\tif ( ! isset( $p['bases_indicadas'][ $base ] ) ) {\n\t\treturn array( 'silencio', 0 );",
           "\tif ( false ) {\n\t\treturn array( 'silencio', 0 );")


def m_ambiente_critico_aceita_silencio(raiz):
    """A regra 4 cai so no ambiente critico — sol, chuva e imersao passam a
    aceitar silencio. E a mutacao sutil: 16 das 18 celulas continuam certas."""
    editar(raiz, SNIPPET,
           "\tif ( isset( $criticos[ $ambiente ] ) && ! isset( $p['ambientes_cobertos'][ $ambiente ] ) ) {\n\t\treturn array( 'silencio', 0 );",
           "\tif ( false && isset( $criticos[ $ambiente ] ) ) {\n\t\treturn array( 'silencio', 0 );")


def m_nivel_de_fonte_deixa_de_limitar(raiz):
    """A regra 5 cai: o Loctite Durepoxi, sustentado por material de imprensa,
    sobe de 'mencao com ressalva' para recomendacao."""
    editar(raiz, SNIPPET,
           "\tif ( $p['nivel'] > cdm_f2_nivel_maximo() ) {\n\t\treturn array( 'ressalva', $score );\n\t}\n\n\treturn array( 'recomendado', $score );",
           "\treturn array( 'recomendado', $score );")


def m_junta_abre_um_milimetro(raiz):
    """`<` vira `<=` na ponta de baixo da faixa de junta: um rejunte passa a
    servir uma folga que o fabricante nao declara. Um caractere."""
    editar(raiz, SNIPPET,
           "\tif ( $junta_mm < $p['junta_min'] || $junta_mm > $p['junta_max'] ) {",
           "\tif ( $junta_mm < $p['junta_min'] - 1 || $junta_mm > $p['junta_max'] ) {")


def m_faixa_pela_metade_vira_sem_limite(raiz):
    """A leitura errada mais tentadora do banco: faixa com uma ponta null tratada
    como 'sem limite'. Poe no ar o unico produto declarado para pastilha de vidro
    submersa — que e justamente o que a ilha NAO pode recomendar."""
    # A PRIMEIRA VERSAO DESTA MUTACAO FOI INERTE, e o motivo vale mais que ela:
    # ela trocava o `||` por `&&` e completava as pontas que faltavam. So que o
    # unico produto do banco sem faixa tem as DUAS pontas null, entao a guarda
    # trocada continuava pegando nele e nada mudava na tela. Mutacao que acha o
    # alvo e mesmo assim nao muda o que o site serve e verde sem medir nada — a
    # mesma familia do alvo que nao existe, e mais dificil de ver. Esta versao
    # desliga a guarda e completa as duas pontas, que e o erro plausivel de
    # verdade: ler faixa DESCONHECIDA como faixa ABERTA.
    editar(raiz, SNIPPET,
           "\tif ( null === $p['junta_min'] || null === $p['junta_max'] ) {\n\t\treturn array( 'fora_da_junta', 0 );\n\t}",
           "\tif ( null === $p['junta_min'] ) { $p['junta_min'] = 0; }\n\tif ( null === $p['junta_max'] ) { $p['junta_max'] = 99; }")


def m_categoria_some_da_pergunta(raiz):
    """A matriz da cola volta a varrer o banco inteiro, sem olhar categoria.

    E o defeito que o bloco 3c encontrou no validador: os cinco rejuntes voltam
    a aparecer como 'eliminados por silencio' numa decisao de COLAGEM, frase que
    nem sentido faz."""
    editar(raiz, SNIPPET,
           "\t\tif ( 'cola' !== ( isset( $m['categoria'] ) ? $m['categoria'] : '' ) ) {\n\t\t\tcontinue;\n\t\t}",
           "\t\tif ( false ) {\n\t\t\tcontinue;\n\t\t}")


def m_secao_do_que_nao_usar_some(raiz):
    """A secao que da razao de ser a pagina desaparece. A recomendacao continua
    certa — e e por isso que a mutacao vale: um teste que so olhasse o topo da
    lista aprovaria."""
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f2_fora_html( $e['base'], $e['ambiente'] );",
           "\t$html .= '';")


def m_tabela_pre_renderizada_some(raiz):
    """As tabelas saem do HTML servido e a ferramenta vira formulario vazio para
    um modelo de linguagem (secao 5 do contrato). A tela continua funcionando
    para quem tem navegador — que e o que faz o defeito ser invisivel."""
    editar(raiz, SNIPPET,
           "\t$html .= cdm_f2_tabela_cola_html();\n\t$html .= cdm_f2_tabela_rejunte_html();",
           "\t$html .= '';")


def m_compra_depois_da_procedencia(raiz):
    """A cicatriz da Robometria de 10/09/2026, refeita: a procedencia vira a
    primeira porta do cartao e o link de compra desce para baixo dela."""
    editar(raiz, SNIPPET,
           "\t$html .= '<span class=\"cdm-f2-compra\">';",
           "\t$fonte_antes = $fonte && ! empty( $fonte['url'] )\n\t\t? '<span class=\"cdm-f2-fonte\"><a href=\"' . esc_url( $fonte['url'] ) . '\" rel=\"nofollow noopener\">fonte</a></span>'\n\t\t: '';\n\t$html .= $fonte_antes;\n\t$html .= '<span class=\"cdm-f2-compra\">';")


def m_estado_com_parametro_entra_no_indice(raiz):
    """O `noindex` do estado com parametro cai, e as 45 combinacoes viram URL
    indexavel num dominio recem-nascido (secoes 14.1 e 14.4)."""
    editar(raiz, SNIPPET,
           "\tif ( $e['escolheu'] ) {\n\t\techo '<meta name=\"robots\" content=\"noindex, follow\">' . \"\\n\";\n\t}",
           "\tif ( false ) {\n\t\techo '<meta name=\"robots\" content=\"noindex, follow\">' . \"\\n\";\n\t}")


def m_faq_do_schema_promete_o_que_a_pagina_nao_diz(raiz):
    """Uma pergunta a mais no FAQPage que nao esta escrita na tela. E o jeito
    classico de FAQPage virar spam, e o jeito classico de ninguem notar."""
    editar(raiz, SNIPPET,
           "\tforeach ( cdm_f2_perguntas() as $p ) {\n\t\t$perguntas[] = array(",
           "\t$extra = cdm_f2_perguntas();\n\t$extra[] = array( 'pergunta' => 'Qual a melhor cola para mosaico?', 'resposta' => 'A melhor de todas.' );\n\tforeach ( $extra as $p ) {\n\t\t$perguntas[] = array(")


def m_script_volta_para_dentro_do_shortcode(raiz):
    """O defeito que derrubou cinco calculadoras da Aquametria em 08/09/2026: o
    <script> volta para dentro do retorno do shortcode e o filtro do conteudo o
    mata convertendo o E-comercial."""
    editar(raiz, SNIPPET,
           "\t$html .= '</div>';\n\n\treturn $html;\n} );",
           "\t$html .= '<script>var a = 1 && 2;</script>';\n\t$html .= '</div>';\n\n\treturn $html;\n} );")


def m_pagina_perde_a_mae(raiz):
    """A pagina nasce solta na raiz: sem `pai`, a URL deixa de mostrar a arvore
    (16.1) e a trilha perde o degrau do meio."""
    editar(raiz, SNIPPET,
           "\t\t'pai'      => 'materiais',",
           "")


def m_nome_diverge_entre_trilha_e_titulo(raiz):
    """A cicatriz da Aquametria de 11/09/2026: o degrau da trilha e o H1 passam a
    dizer nomes diferentes a uma linha de distancia um do outro."""
    editar(raiz, SNIPPET,
           "\t\t\t$lista[ $i ]['titulo'] = CDM_F2_TITULO;",
           "\t\t\t$lista[ $i ]['titulo'] = 'Seletor de cola e rejunte';")


def m_marca_em_dobro_no_nome(raiz):
    """A marca volta a ser colada em todo nome, e os rejuntes viram 'Quartzolit
    Rejunte Ceramicas Quartzolit' na tela."""
    editar(raiz, SNIPPET,
           "\tif ( '' === $marca || false !== mb_stripos( $nome, $marca ) ) {\n\t\treturn trim( $nome );\n\t}",
           "\tif ( '' === $marca ) {\n\t\treturn trim( $nome );\n\t}")


def m_acento_volta_a_sumir_no_banco(raiz):
    """O banco volta a servir portugues sem acento — o defeito que este bloco
    encontrou no ar da bancada. Uma string so, num produto so: o teste varre os
    45 estados justamente porque ela pode aparecer em um deles."""
    b = carregar(raiz, "materiais-colas.json")
    for m in b["materiais"]:
        if m["id"] == "tekbond-silicone-acetico-construcao":
            m["nome_comercial"] = "Silicone Acetico Construcao"
    gravar(raiz, "materiais-colas.json", b)


def m_faixa_descoberta_fica_em_branco(raiz):
    """A frase que declara a faixa descoberta some, e a celula sem resposta passa
    a nao dizer nada. Silencio parece defeito; o contrato manda dizer por que."""
    editar(raiz, SNIPPET,
           "Não temos cola para indicar em <strong>",
           "Veja as opções para <strong>")


def m_rotulo_de_base_some(raiz):
    """Uma base do vocabulario fica sem rotulo na tela. Ela sai do formulario e a
    combinacao correspondente deixa de ser respondida — sem erro nenhum."""
    editar(raiz, SNIPPET,
           "\t\t\t'metal'                        => 'Metal (lata, bandeja, moldura de metal)',\n",
           "")


def m_junta_para_em_dez(raiz):
    """O campo volta a parar em 10 mm, e quem tem folga de 11 cai calado no
    padrao de 2 mm — recebendo uma resposta que nao e a dele. Foi assim que este
    estado nasceu, e foi a varredura que o achou."""
    editar(raiz, SNIPPET, "$jun <= 12 ) ? $jun : 2,", "$jun <= 10 ) ? $jun : 2,")
    editar(raiz, SNIPPET, "for ( $i = 1; $i <= 12; $i++ ) {", "for ( $i = 1; $i <= 10; $i++ ) {")


MUTACOES = [
    ("proibicao do fabricante deixa de vencer", m_proibicao_deixa_de_vencer),
    ("silencio do fabricante vira 'pode'", m_silencio_vira_pode),
    ("ambiente critico passa a aceitar silencio", m_ambiente_critico_aceita_silencio),
    ("nivel de fonte deixa de limitar a recomendacao", m_nivel_de_fonte_deixa_de_limitar),
    ("faixa de junta abre 1 mm para baixo", m_junta_abre_um_milimetro),
    ("faixa de junta pela metade vira sem limite", m_faixa_pela_metade_vira_sem_limite),
    ("a categoria some da pergunta (rejunte na matriz da cola)", m_categoria_some_da_pergunta),
    ("a secao do que nao usar desaparece", m_secao_do_que_nao_usar_some),
    ("as tabelas pre-renderizadas saem do HTML servido", m_tabela_pre_renderizada_some),
    ("compra depois da procedencia no cartao", m_compra_depois_da_procedencia),
    ("estado com parametro entra no indice", m_estado_com_parametro_entra_no_indice),
    ("FAQPage promete pergunta que a pagina nao mostra", m_faq_do_schema_promete_o_que_a_pagina_nao_diz),
    ("<script> volta para dentro do shortcode", m_script_volta_para_dentro_do_shortcode),
    ("a pagina perde a mae e nasce na raiz", m_pagina_perde_a_mae),
    ("o nome diverge entre a trilha e o titulo", m_nome_diverge_entre_trilha_e_titulo),
    ("a marca sai em dobro no nome do produto", m_marca_em_dobro_no_nome),
    ("o acento volta a sumir numa string do banco", m_acento_volta_a_sumir_no_banco),
    ("a faixa descoberta deixa de ser declarada", m_faixa_descoberta_fica_em_branco),
    ("uma base do vocabulario fica sem rotulo", m_rotulo_de_base_some),
    ("o campo de junta volta a parar em 10 mm", m_junta_para_em_dez),
]


def rodar_teste(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "teste-f2.php"), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def main():
    base_rc, base_saida = rodar_teste(ILHA)
    if base_rc != 0:
        print("A F2 de verdade ja esta reprovada — conserte antes de mutar.")
        print("\n".join(l for l in base_saida.splitlines() if "FALHA" in l))
        return 1
    print("F2 intacta: APROVADA (como tem que estar antes de comecar)\n")

    passaram = []
    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-f2-")
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
                    if "FALHA" in linha:
                        primeira = " ".join(linha.split())[6:]
                        break
                print("  reprovou como devia: %-56s | %s" % (nome, primeira[:80]))
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
