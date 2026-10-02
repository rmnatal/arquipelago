#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra as paginas do GUIA de proposito, uma mutacao por vez, e exige que a
bancada reprove — ou, em tres casos, que ela APROVE um mundo que o banco de
hoje nao tem.

    python3 ferramentas/mutacoes-guia.py

POR QUE ESTE ARQUIVO EXISTE. `teste-guia.php` nasceu junto com as quatro
paginas, e regua que nasce junto com o codigo que ela mede e a situacao em que
ninguem ainda viu a regua FALHAR. Verde de primeira nao e elogio: e o estado em
que tanto faz se o portao mede alguma coisa (secao 8 do ARQUIPELAGO.md). Cada
mutacao abaixo e uma forma plausivel de uma destas paginas ficar errada em
silencio.

OS TRES CASOS QUE NAO SAO "REPROVA":

  1. COM O BANCO DE ACABAMENTO FORA DO AR, a pagina TEM de dizer que nao mediu
     e NAO pode servir ficha de produto nenhuma. O teste sozinho nao mede isso
     — a bancada carrega as options na entrada do processo, entao a ausencia e
     outro MUNDO e nao outra afirmacao.

  2. SEM O SNIPPET DA F2, a pagina sai INTEIRA e diz que a lista de onde
     comprar esta fora do ar. O bloco de compra desta pagina e da F2 por
     decisao (uma escada de quatro degraus, um dono), e saida degradada que
     nunca foi produzida nasce errada sem poder falhar — foi exatamente isso
     que a F1 descobriu em 29/09/2026 nas duas vitrines dela.

  3. COM UM FABRICANTE NOMEANDO VIDRO, a frase da lacuna TEM de parar de dizer
     que ninguem nomeia vidro, e a pagina continua passando. Este e o ramo que
     o banco de hoje nao pisa: nenhum dos dez acabamentos nomeia vidro, entao a
     frase sai sempre igual e ninguem sabe se ela e derivada ou cravada. O
     mundo e fabricado aqui.

Cada mutacao roda numa COPIA da pasta da ilha. Nada aqui toca o repositorio.
Ferramenta de bancada: nunca vai para o site.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ILHA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SNIPPET = "snippets/clubedomosaico-guia.php"

# A pagina usada para medir o HTML nos casos que nao passam pelo teste. O id
# esta escrito aqui de proposito — ler o registro do snippet faria a mutacao
# que mexe no registro medir a si mesma.
TAG_DA_MAE = "cdm_guia_acabamento"
TAG_DE_UMA_FILHA = "cdm_guia_impermeabilizante"


def ler(raiz, caminho):
    with open(os.path.join(raiz, caminho), encoding="utf-8") as fh:
        return fh.read()


def gravar(raiz, caminho, texto):
    with open(os.path.join(raiz, caminho), "w", encoding="utf-8") as fh:
        fh.write(texto)


def trocar(raiz, caminho, velho, novo):
    texto = ler(raiz, caminho)
    if velho not in texto:
        raise AssertionError("mutacao nao achou o trecho em %s: %r" % (caminho, velho[:60]))
    gravar(raiz, caminho, texto.replace(velho, novo, 1))


def banco(raiz):
    return json.load(open(os.path.join(raiz, "dados", "materiais-acabamento.json"), encoding="utf-8"))


def gravar_banco(raiz, b):
    json.dump(b, open(os.path.join(raiz, "dados", "materiais-acabamento.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


# ------------------------------------------------------------------ mutacoes

def m_cobertura_cravada(raiz):
    """O numero da cobertura deixa de ser contado e passa a ser escrito. E a
    forma mais barata de a pagina mentir: ela continua com cara de medida, o
    denominador continua certo, e o numerador e uma lembranca de ontem."""
    trocar(raiz, SNIPPET,
           "\t\t'nomeadas'              => $nomeadas,",
           "\t\t'nomeadas'              => 13,")


def m_denominador_digitado(raiz):
    """As 15 superficies deixam de sair do vocabulario e viram um numero no
    codigo. No dia em que o esquema ganhar um valor, a pagina publica uma
    fracao com o denominador do mundo anterior — e ninguem ve, porque 15 e um
    numero plausivel."""
    trocar(raiz, SNIPPET,
           "\t$n_sup      = count( $sup['base'] ) + count( $sup['tessela'] );",
           "\t$n_sup      = 15;")
    e = json.load(open(os.path.join(raiz, "dados", "esquema-banco.json"), encoding="utf-8"))
    e["vocabularios"]["base"].append("ceramica_crua")
    json.dump(e, open(os.path.join(raiz, "dados", "esquema-banco.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


def m_relogio_empresta_o_intervalo(raiz):
    """O relogio passa a somar mesmo sem o intervalo entre demaos declarado,
    chutando 4 horas. E o erro que o proprio banco nomeia dentro do
    `quartzolit-fundo-selador`: emprestar demao de um produto a outro."""
    trocar(raiz, SNIPPET,
           "\tif ( ! is_numeric( $intervalo ) ) {\n\t\treturn null;\n\t}",
           "\tif ( ! is_numeric( $intervalo ) ) {\n\t\t$intervalo = 240;\n\t}")


def m_relogio_sem_a_linha_que_recusa(raiz):
    """O produto sem as tres parcelas deixa de receber a linha que diz por que
    nao ha conta. A pagina nao mente — ela fica MUDA, e silencio em tabela
    comparativa le-se como 'nao se aplica'."""
    trocar(raiz, SNIPPET,
           "\t} else {\n\t\t$html .= '<p class=\"cdm-guia-relogio cdm-guia-sem-conta\">O fabricante não declara as três partes da espera",
           "\t} elseif ( false ) {\n\t\t$html .= '<p class=\"cdm-guia-relogio cdm-guia-sem-conta\">O fabricante não declara as três partes da espera")


def m_um_produto_some_da_mae(raiz):
    """A mae deixa de mostrar um dos dez. A prestacao de contas da secao 7 diz
    que cada item da categoria consultada aparece exatamente uma vez — ou na
    frase que o recomenda, ou numa linha que diz por que ele nao esta."""
    trocar(raiz, SNIPPET,
           "\t\t\tforeach ( $cf['itens'] as $chave ) {\n\t\t\t\t$html .= cdm_guia_ficha_do_produto_html( $banco['itens'][ $chave ] );",
           "\t\t\tforeach ( array_slice( $cf['itens'], 1 ) as $chave ) {\n\t\t\t\t$html .= cdm_guia_ficha_do_produto_html( $banco['itens'][ $chave ] );")


def m_ancora_vira_saiba_mais(raiz):
    """A mae passa a linkar as filhas com o nome curto em vez da consulta-alvo.
    A 16.4(a) proibe isso com todas as letras — o texto-ancora e o que diz ao
    buscador do que a filha trata, e 'Selador' nao e o que ninguem digita."""
    trocar(raiz, SNIPPET,
           "\t\t\t$html .= '<li><h3>' . cdm_casca_link_html( $f['slug'], $f['consulta'] ) . '</h3>'",
           "\t\t\t$html .= '<li><h3>' . cdm_casca_link_html( $f['slug'], $f['curto'] ) . '</h3>'")


def m_filha_perde_a_frase_que_linka_a_mae(raiz):
    """A filha fica so com a trilha apontando para a mae. A 16.4(b) pede as
    duas — e a trilha sozinha passaria numa regua desatenta, que e justamente
    por que a afirmacao do teste apaga os `<nav>` antes de procurar."""
    trocar(raiz, SNIPPET,
           "\t\t$html .= '<p>Esta é uma das três etapas do '\n\t\t\t. cdm_casca_link_html( $mae['slug'], 'acabamento da peça de mosaico' )",
           "\t\t$html .= '<p>Esta é uma das três etapas do '\n\t\t\t. esc_html( 'acabamento da peça de mosaico' )")


def m_frase_da_lacuna_cravada(raiz):
    """A frase que diz o que falta deixa de ser derivada e passa a ser uma
    lista escrita. Ela continua CERTA hoje — e e esse o ponto: ela so fica
    errada no dia em que um fabricante novo nomear vidro, e nesse dia ninguem
    vai estar olhando para esta linha."""
    trocar(raiz, SNIPPET,
           "\tforeach ( array( 'vidro', 'espelho' ) as $chave ) {\n\t\tif ( in_array( $chave, $lac['base'], true ) ) {\n\t\t\t$nomes[] = cdm_guia_rotulo( 'base', $chave );\n\t\t}\n\t}",
           "\t$nomes[] = 'vidro comum';")
    # e o mundo em que ela fica errada: um fabricante passa a nomear vidro.
    b = banco(raiz)
    for m in b["materiais"]:
        if m["id"] == "coral-resina-acrilica":
            m["protecao"]["bases_do_vocabulario_que_a_frase_nomeia"].append("vidro")
            m["protecao"]["bases_do_vocabulario_que_a_frase_NAO_nomeia"].remove("vidro")
    gravar_banco(raiz, b)


def m_busca_crua_vira_patrocinada(raiz):
    """O link que NAO rende comissao passa a se declarar patrocinado. Nao e
    detalhe de atributo: e mentir ao leitor sobre a unica coisa que ele tem o
    direito de saber sobre nos. A trava mora na F2, que e a dona da escada, e
    esta mutacao prova que ela alcanca a ficha do Guia tambem."""
    b = banco(raiz)
    for m in b["materiais"]:
        m["afiliado"]["url"] = ""
        m["afiliado"]["url_busca"] = ""
    gravar_banco(raiz, b)
    trocar(raiz, "snippets/clubedomosaico-f2.php",
           "rel=\"nofollow noopener\" target=\"_blank\">Ver as opções na loja</a>';",
           "rel=\"sponsored noopener\" target=\"_blank\">Ver as opções na loja</a>';")


def m_uma_pagina_a_mais_sem_autorizacao(raiz):
    """Nasce uma quinta pagina, de um recorte que o cruzamento da 14.9 NAO
    autoriza. E a forma mais provavel de esta familia crescer errado: o banco
    tem itens, o recorte parece pronto, e ninguem abre o veredito."""
    trocar(raiz, SNIPPET,
           "\t\t'selador' => array(\n\t\t\t'tipo'     => 'selador',",
           "\t\t'pastilha_vidro' => array(\n"
           "\t\t\t'tipo'     => 'pastilha_vidro',\n"
           "\t\t\t'slug'     => 'materiais/acabamento/pastilhas-de-vidro',\n"
           "\t\t\t'titulo'   => 'Pastilhas de vidro para mosaico',\n"
           "\t\t\t'curto'    => 'Pastilhas',\n"
           "\t\t\t'consulta' => 'pastilhas de vidro para mosaico',\n"
           "\t\t\t'resumo'   => 'As pastilhas de vidro do banco.',\n"
           "\t\t\t'linha_mestra' => 'As pastilhas de vidro do banco desta ilha.',\n"
           "\t\t\t'description'  => 'Pastilhas de vidro para mosaico: o que cada fabricante declara sobre o produto, com a frase dele e a data da leitura aqui.',\n"
           "\t\t\t'o_que_e'  => 'Pastilha de vidro e a tessela mais comum do mosaico.',\n"
           "\t\t\t'o_que_nao_e' => 'O que ela nao e: caco de espelho.',\n"
           "\t\t\t'faq_propria' => array(),\n"
           "\t\t),\n"
           "\t\t'selador' => array(\n\t\t\t'tipo'     => 'selador',")


def m_uma_filha_some_do_registro(raiz):
    """Uma filha autorizada pelo cruzamento deixa de ter pagina. E o estado em
    que esta ilha passou quatro execucoes com o 4c: o recorte estava pronto e
    ninguem publicou. A trava e a SEGUNDA direcao da afirmacao do cruzamento,
    e e ela que faz a familia nao parar calada."""
    texto = ler(raiz, SNIPPET)
    ini = texto.index("\t\t'verniz' => array(")
    fim = texto.index("\t\t'impermeabilizante' => array(")
    gravar(raiz, SNIPPET, texto[:ini] + texto[fim:])


def m_banco_fora_do_ar(raiz):
    """O item do manifest volta a `publicar: false` e a option some do site.

    ESTA NAO REPROVA POR REPROVAR: o que se exige e a pagina HONESTA. Ela tem
    de dizer que nao mediu e NAO pode servir ficha de produto — inventar aqui
    seria publicar recomendacao de acabamento sem banco.
    """
    p = os.path.join(raiz, "manifest.json")
    m = json.load(open(p, encoding="utf-8"))
    for d in m["dados"]:
        if d["id"] == "materiais-acabamento":
            d["publicar"] = False
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def m_sem_o_snippet_da_f2(raiz):
    """A F2 sai do ar. A pagina tem de sair INTEIRA, com os produtos e os
    numeros, dizendo que a lista de onde comprar e que esta fora."""
    os.remove(os.path.join(raiz, "snippets", "clubedomosaico-f2.php"))


def m_um_fabricante_passa_a_nomear_vidro(raiz):
    """O mundo em que a lacuna encolhe. A pagina tem de PASSAR e a frase tem de
    parar de dizer que ninguem nomeia vidro comum."""
    b = banco(raiz)
    for m in b["materiais"]:
        if m["id"] == "coral-resina-acrilica":
            m["protecao"]["bases_do_vocabulario_que_a_frase_nomeia"].append("vidro")
            m["protecao"]["bases_do_vocabulario_que_a_frase_NAO_nomeia"].remove("vidro")
    gravar_banco(raiz, b)


MUTACOES = [
    ("o numero da cobertura e cravado no codigo", m_cobertura_cravada, "reprova"),
    ("o denominador (15 superficies) e digitado", m_denominador_digitado, "reprova"),
    ("o relogio empresta o intervalo que falta", m_relogio_empresta_o_intervalo, "reprova"),
    ("o produto sem conta fica MUDO em vez de recusar", m_relogio_sem_a_linha_que_recusa, "reprova"),
    ("um dos dez produtos some da mae", m_um_produto_some_da_mae, "reprova"),
    ("a mae linka a filha com o nome curto, nao com a consulta", m_ancora_vira_saiba_mais, "reprova"),
    ("a filha perde a frase do corpo que linka a mae", m_filha_perde_a_frase_que_linka_a_mae, "reprova"),
    ("a frase da lacuna vira lista escrita a mao", m_frase_da_lacuna_cravada, "reprova"),
    ("a busca CRUA passa a se declarar patrocinada", m_busca_crua_vira_patrocinada, "reprova"),
    ("nasce uma pagina que o cruzamento NAO autoriza", m_uma_pagina_a_mais_sem_autorizacao, "reprova"),
    ("uma filha autorizada some do registro", m_uma_filha_some_do_registro, "reprova"),
    ("o banco de acabamento sai do ar", m_banco_fora_do_ar, "pagina-honesta"),
    ("o snippet da F2 sai do ar", m_sem_o_snippet_da_f2, "pagina-sem-loja"),
    ("um fabricante passa a nomear vidro", m_um_fabricante_passa_a_nomear_vidro, "mundo-que-passa"),
]


def rodar(raiz, teste):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", teste), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def corpo_da_pagina(raiz, tag):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "render-para-teste.php"),
                        raiz, tag], capture_output=True, text=True)
    if r.returncode != 0:
        return ""
    m = re.search(r"<main\b[^>]*>(.*?)</main>", r.stdout, re.S)
    return m.group(1) if m else r.stdout


def main():
    rc, saida = rodar(ILHA, "teste-guia.php")
    if rc != 0:
        print("As paginas de verdade ja estao reprovadas — conserte antes de mutar.")
        print(saida[-2000:])
        return 1
    print("paginas intactas: APROVADAS (como tem que estar antes de comecar)\n")

    erradas = []
    for nome, mutar, esperado in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-guia-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)

            if esperado == "pagina-honesta":
                corpo = corpo_da_pagina(copia, TAG_DA_MAE)
                honesta = "ainda não chegou ao site" in corpo
                sem_ficha = "cdm-guia-cartao" not in corpo
                if honesta and sem_ficha:
                    print("  ficou honesta como devia: %-50s | diz que nao mediu e NAO serve ficha" % nome)
                else:
                    erradas.append(nome + " (a pagina %s)" % (
                        "serviu ficha sem banco" if not sem_ficha else "nao disse que ficou sem medicao"))
                    print("  INVENTOU (a trava NAO viu): %s" % nome)
                continue

            if esperado == "pagina-sem-loja":
                corpo = corpo_da_pagina(copia, TAG_DE_UMA_FILHA)
                inteira = "cdm-guia-cartao" in corpo and "combinações de produto e superfície" in corpo
                avisa = "lista de onde comprar está fora do ar" in corpo
                sem_botao = "cdm-f2-compra" not in corpo
                if inteira and avisa and sem_botao:
                    print("  degradou como devia:      %-50s | pagina inteira, sem botao, com o aviso" % nome)
                else:
                    erradas.append(nome + " (inteira=%s avisa=%s sem_botao=%s)" % (inteira, avisa, sem_botao))
                    print("  DEGRADOU ERRADO: %s" % nome)
                continue

            if esperado == "mundo-que-passa":
                rc, saida = rodar(copia, "teste-guia.php")
                corpo = corpo_da_pagina(copia, TAG_DE_UMA_FILHA)
                # SO A FRASE DA LACUNA. "vidro comum" aparece tambem na ficha do
                # produto que passou a nomear vidro — procurar no corpo inteiro
                # mediria o oposto do que esta mutacao quer saber.
                m = re.search(r"Entre o que ningu.m deste grupo nomeia est.(.*?)</p>", corpo, re.S)
                fala_de_vidro = bool(m) and "vidro comum" in m.group(1)
                if 0 == rc and not fala_de_vidro:
                    print("  passou como devia:        %-50s | a lacuna do vidro sumiu sozinha" % nome)
                else:
                    erradas.append(nome + " (rc=%d, ainda fala de vidro comum=%s)" % (rc, fala_de_vidro))
                    print("  NAO PASSOU (a frase da lacuna nao e derivada): %s" % nome)
                continue

            rc, saida = rodar(copia, "teste-guia.php")
            primeira = ""
            for linha in saida.splitlines():
                if linha.strip().startswith("FALHA"):
                    primeira = linha.strip()[5:].strip()
                    break
            if rc != 0:
                print("  reprovou como devia:      %-50s | %s" % (nome, primeira[:66]))
            else:
                erradas.append(nome + " (PASSOU e devia reprovar)")
                print("  PASSOU (a trava NAO viu): %s" % nome)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d decididas certo, %d erradas" %
          (len(MUTACOES), len(MUTACOES) - len(erradas), len(erradas)))
    if erradas:
        print("\nAS ERRADAS SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in erradas:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
