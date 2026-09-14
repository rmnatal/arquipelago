#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a PAGINA de tecnica de proposito, uma mutacao por vez, e exige que a
bancada reprove — ou, num caso, que a pagina fique HONESTA em vez de inventar.

    python3 ferramentas/mutacoes-tecnicas-pagina.py

POR QUE ESTE ARQUIVO EXISTE. `teste-tecnicas.php` nasceu junto com a pagina, e
regua que nasce junto com o codigo que ela mede e a situacao em que ninguem
ainda viu a regua FALHAR. Verde de primeira nao e elogio: e o estado em que
tanto faz se o portao mede alguma coisa (secao 8 do ARQUIPELAGO.md). Cada
mutacao abaixo e uma forma plausivel de esta pagina ficar errada em silencio.

O CASO QUE NAO E "REPROVA", e ele e o mais importante: com o banco de tecnicas
fora do ar, a pagina TEM de dizer que nao mediu, e nao pode servir a grade. O
teste sozinho nao mede isso — a bancada carrega as options na entrada do
processo, entao a ausencia e outro MUNDO e nao outra afirmacao. Aqui ela e
produzida, e o que se mede e o HTML: a frase honesta presente e a tabela
ausente. E a trava que a Robometria escreveu em 11/09/2026 depois de descobrir
que a option que alimentava os numeros dela nunca existira no site.

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

SNIPPET = "snippets/clubedomosaico-tecnicas.php"


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


# ------------------------------------------------------------------ mutacoes

def m_tessela_digitada_no_snippet(raiz):
    """A pagina para de ler o banco e passa a saber de cor qual e o caquinho, e
    o banco passa a dizer outro. E a forma classica de o texto e o dado
    divergirem em silencio: os dois continuam existindo e param de concordar."""
    trocar(raiz, SNIPPET,
           "\treturn $m ? (string) reset( $m ) : '';",
           "\treturn 'caco_louca';")
    b = json.load(open(os.path.join(raiz, "dados", "tecnicas.json"), encoding="utf-8"))
    for t in b["tecnicas"]:
        if t["id"] == "picassiette":
            t["materiais_tipicos"] = ["caco_espelho"]
    json.dump(b, open(os.path.join(raiz, "dados", "tecnicas.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


def m_uma_celula_cravada(raiz):
    """Uma celula da grade deixa de ser calculada e passa a ser escrita. Basta
    UMA: a pagina continua com cara de completa e mente sobre um cruzamento."""
    trocar(raiz, SNIPPET,
           "\t\t\t$c        = cdm_f2_celula_cola( $base, $ambiente, $tessela );",
           "\t\t\t$c        = cdm_f2_celula_cola( $base, $ambiente, $tessela );\n"
           "\t\t\tif ( 'espelho' === $base && 'interno_seco' === $ambiente ) "
           "{ $c['recomendados_topo'] = array( 'cascola-cascorez-extra' ); }")


def m_um_cartao_some_da_vitrine(raiz):
    """A vitrine deixa de servir um dos que a frase nomeia. E exatamente o
    defeito que a F2 desta ilha pagou em 12/09/2026, do avesso."""
    trocar(raiz, SNIPPET,
           "\tforeach ( $contas['dentro'] as $id ) {\n\t\t$onde = array();",
           "\tforeach ( array_slice( $contas['dentro'], 1 ) as $id ) {\n\t\t$onde = array();")


def m_recusa_so_com_a_causa_maior(raiz):
    """A recusa volta a nomear so o balde de maior contagem. O Durepoxi cai por
    silencio em 25 celulas E entra com ressalva em 20; dizer so o silencio faz
    a pagina afirmar que o fabricante nunca nomeia uma dessas superficies, o
    que e falso em 20 delas. E a secao 7: causa que o codigo separa, o texto
    separa."""
    trocar(raiz, SNIPPET,
           "\tarsort( $b );\n\t\t$causas = array();\n\t\tforeach ( $b as $nome => $n ) {\n\t\t\tif ( $n > 0 ) {",
           "\tarsort( $b );\n\t\t$causas = array();\n\t\tforeach ( array_slice( $b, 0, 1, true ) as $nome => $n ) {\n\t\t\tif ( $n > 0 ) {")


def m_busca_crua_vira_patrocinada(raiz):
    """O link que NAO rende comissao passa a se declarar patrocinado. Nao e
    detalhe de atributo: e mentir ao leitor sobre a unica coisa que ele tem o
    direito de saber sobre nos."""
    trocar(raiz, "snippets/clubedomosaico-f2.php",
           "\t\t\t. ' rel=\"nofollow noopener\" target=\"_blank\">Ver as opções na loja</a>';",
           "\t\t\t. ' rel=\"sponsored noopener\" target=\"_blank\">Ver as opções na loja</a>';")


def m_faq_do_schema_promete_a_mais(raiz):
    """O FAQPage ganha uma pergunta que a tela nao responde. E o caminho pelo
    qual FAQPage vira spam, e ele comeca sempre assim: alguem acrescenta no
    schema o que seria bom responder."""
    trocar(raiz, SNIPPET,
           "\tforeach ( cdm_tecnicas_faq() as $p ) {\n\t\t$perguntas[] = array(",
           "\t$extra = cdm_tecnicas_faq();\n"
           "\t$extra[] = array( 'pergunta' => 'Quanto custa fazer um mosaico Picassiete?',\n"
           "\t\t'resposta' => 'Depende da peça.' );\n"
           "\tforeach ( $extra as $p ) {\n\t\t$perguntas[] = array(")


def m_numero_da_frase_digitado(raiz):
    """A frase de resposta para de contar e passa a repetir um numero. Ele fica
    certo hoje e errado no dia seguinte a uma coleta — que e a cicatriz do
    cabecalho de pecas.json dizendo 32 com 35 no arquivo."""
    trocar(raiz, SNIPPET,
           "\t\t. 'Das <strong>' . (int) $contas['celulas'] . '</strong> combinações desta página, '",
           "\t\t. 'Das <strong>40</strong> combinações desta página, '")


def m_pagina_some_da_mae(raiz):
    """A pagina deixa de se registrar na Escola. Ela continua existindo e
    respondendo 200, e vira orfa — a 16.4(f) do contrato, que e o portao do
    teste-casca e nao o desta pagina."""
    trocar(raiz, SNIPPET,
           "add_filter( 'cdm_tecnicas_publicadas', function ( $lista ) {",
           "add_filter( 'cdm_tecnicas_publicadas_DESLIGADO', function ( $lista ) {")


def m_banco_fora_do_ar(raiz):
    """O item do manifest volta a `publicar: false` e a option some do site.

    ESTA NAO REPROVA POR REPROVAR: o que se exige e a pagina HONESTA. Ela tem de
    dizer que nao mediu e NAO pode servir a grade — inventar aqui seria publicar
    recomendacao de cola sem banco, que e a unica coisa que esta ilha nao pode
    fazer.
    """
    p = os.path.join(raiz, "manifest.json")
    m = json.load(open(p, encoding="utf-8"))
    for d in m["dados"]:
        if d["id"] == "tecnicas":
            d["publicar"] = False
    json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


MUTACOES = [
    ("a tessela e digitada no snippet e o banco diz outra", m_tessela_digitada_no_snippet, "reprova"),
    ("uma celula da grade e cravada a mao", m_uma_celula_cravada, "reprova"),
    ("um cartao some da vitrine que a frase nomeia", m_um_cartao_some_da_vitrine, "reprova"),
    ("a recusa volta a nomear so a causa maior", m_recusa_so_com_a_causa_maior, "reprova"),
    ("a busca CRUA passa a se declarar patrocinada", m_busca_crua_vira_patrocinada, "reprova"),
    ("o FAQPage promete pergunta que a tela nao responde", m_faq_do_schema_promete_a_mais, "reprova"),
    ("o numero da frase de resposta e digitado", m_numero_da_frase_digitado, "reprova"),
    ("a pagina some da listagem da mae (orfa)", m_pagina_some_da_mae, "reprova-na-casca"),
    ("o banco de tecnicas sai do ar", m_banco_fora_do_ar, "pagina-honesta"),
]


def rodar(raiz, teste):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", teste), raiz],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def corpo_da_pagina(raiz):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", "render-para-teste.php"),
                        raiz, "cdm_tecnica"], capture_output=True, text=True)
    if r.returncode != 0:
        return ""
    m = re.search(r"<main\b[^>]*>(.*?)</main>", r.stdout, re.S)
    return m.group(1) if m else r.stdout


def main():
    rc, saida = rodar(ILHA, "teste-tecnicas.php")
    if rc != 0:
        print("A pagina de verdade ja esta reprovada — conserte antes de mutar.")
        print(saida[-2000:])
        return 1
    print("pagina intacta: APROVADA (como tem que estar antes de comecar)\n")

    erradas = []
    for nome, mutar, esperado in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-tecpag-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)

            if esperado == "pagina-honesta":
                corpo = corpo_da_pagina(copia)
                honesta = "ainda não chegou ao site" in corpo
                sem_grade = "cdm-tec-tabela" not in corpo
                if honesta and sem_grade:
                    print("  ficou honesta como devia: %-42s | diz que nao mediu e NAO serve a grade" % nome)
                else:
                    erradas.append(nome + " (a pagina %s)" % (
                        "serviu a grade sem banco" if not sem_grade else "nao disse que ficou sem medicao"))
                    print("  INVENTOU (a trava NAO viu): %s" % nome)
                continue

            teste = "teste-casca.php" if esperado == "reprova-na-casca" else "teste-tecnicas.php"
            rc, saida = rodar(copia, teste)
            primeira = ""
            for linha in saida.splitlines():
                if linha.strip().startswith("FALHA"):
                    primeira = linha.strip()[5:].strip()
                    break
            if rc != 0:
                print("  reprovou como devia: %-42s | %s" % (nome, primeira[:80]))
            else:
                erradas.append(nome + " (PASSOU e devia reprovar em %s)" % teste)
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
