#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra as PAGINAS de tecnica de proposito, uma mutacao por vez, e exige que a
bancada reprove — ou, em dois casos, que ela APROVE um mundo que o banco de hoje
nao tem.

    python3 ferramentas/mutacoes-tecnicas-pagina.py

POR QUE ESTE ARQUIVO EXISTE. `teste-tecnicas.php` nasceu junto com a pagina, e
regua que nasce junto com o codigo que ela mede e a situacao em que ninguem
ainda viu a regua FALHAR. Verde de primeira nao e elogio: e o estado em que
tanto faz se o portao mede alguma coisa (secao 8 do ARQUIPELAGO.md). Cada
mutacao abaixo e uma forma plausivel de uma destas paginas ficar errada em
silencio.

OS DOIS CASOS QUE NAO SAO "REPROVA":

  1. COM O BANCO DE TECNICAS FORA DO AR, a pagina TEM de dizer que nao mediu, e
     nao pode servir a grade. O teste sozinho nao mede isso — a bancada carrega
     as options na entrada do processo, entao a ausencia e outro MUNDO e nao
     outra afirmacao. Aqui ela e produzida, e o que se mede e o HTML: a frase
     honesta presente e a tabela ausente. E a trava que a Robometria escreveu em
     11/09/2026 depois de descobrir que a option que alimentava os numeros dela
     nunca existira no site.

  2. COM DOIS CAQUINHOS QUE DECIDEM DIFERENTE, a pagina tem de servir DUAS
     tabelas e passar. Este e o caminho que o banco de hoje nao exercita: o
     trencadis declara caco de azulejo e caco de louca, e os dois caem do mesmo
     lado da unica conta em que o caquinho entra (a condicao de superficie
     porosa), entao o mundo real so pisa no ramo de UMA tabela. Grade que nao
     pisa na borda nao e grade (secao 8): a borda e fabricada aqui, trocando um
     dos caquinhos por caco de espelho, que nao absorve. E logo abaixo vem a
     mutacao que prova que a trava do OUTRO lado morde — a pagina servindo uma
     tabela so nesse mesmo mundo.

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

# A pagina usada para medir o HTML nos casos que nao passam pelo teste: a
# primeira do registro. O id esta escrito aqui de proposito — ler o registro do
# snippet faria a mutacao que mexe no registro medir a si mesma.
TAG_DA_PRIMEIRA = "cdm_tecnica_picassiette"


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


def banco_tecnicas(raiz):
    return json.load(open(os.path.join(raiz, "dados", "tecnicas.json"), encoding="utf-8"))


def gravar_banco_tecnicas(raiz, b):
    json.dump(b, open(os.path.join(raiz, "dados", "tecnicas.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


def declarar_caquinhos(raiz, id_tecnica, caquinhos):
    b = banco_tecnicas(raiz)
    for t in b["tecnicas"]:
        if t["id"] == id_tecnica:
            t["materiais_tipicos"] = caquinhos
    gravar_banco_tecnicas(raiz, b)


# ------------------------------------------------------------------ mutacoes

def m_tessela_digitada_no_snippet(raiz):
    """A pagina para de ler o banco e passa a saber de cor qual e o caquinho, e
    o banco passa a dizer outro. E a forma classica de o texto e o dado
    divergirem em silencio: os dois continuam existindo e param de concordar."""
    trocar(raiz, SNIPPET,
           "\t$m = ( isset( $t['materiais_tipicos'] ) && is_array( $t['materiais_tipicos'] ) ) ? $t['materiais_tipicos'] : array();",
           "\t$m = array( 'caco_louca' );")
    declarar_caquinhos(raiz, "picassiette", ["caco_espelho"])


def m_so_o_primeiro_caquinho(raiz):
    """A 1.0.0 de volta: com dois caquinhos declarados, a pagina resolve so o
    primeiro. Ela continua certa sobre o caco de azulejo e fica muda sobre o de
    louca, sem uma linha de aviso — e o leitor que veio pelo segundo recebe uma
    resposta que ninguem disse que nao era dele."""
    trocar(raiz, SNIPPET,
           "\treturn $saida;\n}\n}",
           "\treturn $saida ? array( $saida[0] ) : $saida;\n}\n}")


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
           "\tforeach ( $contas['dentro'] as $id_cola ) {\n\t\t$onde = array();",
           "\tforeach ( array_slice( $contas['dentro'], 1 ) as $id_cola ) {\n\t\t$onde = array();")


def m_recusa_so_com_a_causa_maior(raiz):
    """A recusa volta a nomear so o balde de maior contagem. O Durepoxi cai por
    silencio em 25 celulas E entra com ressalva em 20; dizer so o silencio faz
    a pagina afirmar que o fabricante nunca nomeia uma dessas superficies, o
    que e falso em 20 delas. E a secao 7: causa que o codigo separa, o texto
    separa."""
    trocar(raiz, SNIPPET,
           "\t\tarsort( $b );\n\t\t$causas = array();\n\t\tforeach ( $b as $nome => $n ) {",
           "\t\tarsort( $b );\n\t\t$causas = array();\n\t\tforeach ( array_slice( $b, 0, 1, true ) as $nome => $n ) {")


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
           "\tforeach ( cdm_tecnicas_faq( $id ) as $p ) {\n\t\t$perguntas[] = array(",
           "\t$extra = cdm_tecnicas_faq( $id );\n"
           "\t$extra[] = array( 'pergunta' => 'Quanto custa fazer um mosaico assim?',\n"
           "\t\t'resposta' => 'Depende da peça.' );\n"
           "\tforeach ( $extra as $p ) {\n\t\t$perguntas[] = array(")


def m_numero_da_frase_digitado(raiz):
    """A frase de resposta para de contar e passa a repetir um numero. Ele fica
    certo hoje e errado no dia seguinte a uma coleta — que e a cicatriz do
    cabecalho de pecas.json dizendo 32 com 35 no arquivo."""
    trocar(raiz, SNIPPET,
           "\t\t. 'Das <strong>' . (int) $contas['celulas'] . '</strong> combinações desta página, '",
           "\t\t. 'Das <strong>40</strong> combinações desta página, '")


def m_as_duas_paginas_com_o_mesmo_shortcode(raiz):
    """As duas paginas voltam a servir `[cdm_tecnica]`, como na 1.0.0.

    Esta e a mutacao que mede o motivo de a 1.1.0 existir, e ela e traicoeira:
    no SITE as duas paginas continuariam certas, porque o atalho resolve pelo
    endereco servido. Quem quebra e a BANCADA — ela descobre quem esta medindo
    casando o shortcode com a definicao de paginas, entao com um shortcode so
    ela mediria a primeira duas vezes e a segunda nenhuma, e continuaria verde.
    Regua que mede a pagina errada e pior que regua ausente."""
    trocar(raiz, SNIPPET,
           "\t\t\t'conteudo' => '[cdm_tecnica_' . $id . ']',",
           "\t\t\t'conteudo' => '[cdm_tecnica]',")


def m_segunda_pagina_some_do_registro(raiz):
    """A segunda tecnica sai do registro do snippet e o banco continua com a
    bandeira `pagina_publicada` levantada. As duas metades ficam certas
    sozinhas: o site publica uma pagina a menos sem erro nenhum, e o
    validar-banco continua cobrando o portao de 3 itens de uma pagina que nao
    existe mais."""
    texto = ler(raiz, SNIPPET)
    inicio = texto.index("\t\t'trencadis' => array(")
    fim = texto.index("\t);\n}\n}", inicio)
    gravar(raiz, SNIPPET, texto[:inicio] + texto[fim:])


def m_dois_caquinhos_que_decidem_diferente(raiz):
    """O MUNDO QUE O BANCO DE HOJE NAO TEM, e ele tem de PASSAR.

    O trencadis passa a declarar caco de louca (que absorve) e caco de espelho
    (que nao absorve). A unica conta em que o caquinho entra na regua da F2 e a
    condicao de superficie porosa, entao as duas grades DIVERGEM — em 4 das 45
    celulas, medido — e a pagina tem de servir DUAS tabelas, com o nome do
    caquinho em cima de cada uma. Se ela servir uma so, o teste reprova; se
    servir duas, este mundo prova que o ramo existe e funciona."""
    declarar_caquinhos(raiz, "trencadis", ["caco_louca", "caco_espelho"])


def m_dois_caquinhos_diferentes_numa_tabela_so(raiz):
    """O mesmo mundo de cima, e agora o agrupamento e quebrado: tudo cai num
    grupo so. A pagina serve UMA tabela para dois caquinhos que decidem
    diferente — que e afirmar sobre um material o que foi medido no outro."""
    declarar_caquinhos(raiz, "trencadis", ["caco_louca", "caco_espelho"])
    trocar(raiz, SNIPPET,
           "\t\t$chave = cdm_tecnicas_assinatura_da_grade( $grade );",
           "\t\t$chave = 'um-grupo-so';")


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
    ("a pagina resolve so o PRIMEIRO caquinho declarado", m_so_o_primeiro_caquinho, "reprova"),
    ("uma celula da grade e cravada a mao", m_uma_celula_cravada, "reprova"),
    ("um cartao some da vitrine que a frase nomeia", m_um_cartao_some_da_vitrine, "reprova"),
    ("a recusa volta a nomear so a causa maior", m_recusa_so_com_a_causa_maior, "reprova"),
    ("a busca CRUA passa a se declarar patrocinada", m_busca_crua_vira_patrocinada, "reprova"),
    ("o FAQPage promete pergunta que a tela nao responde", m_faq_do_schema_promete_a_mais, "reprova"),
    ("o numero da frase de resposta e digitado", m_numero_da_frase_digitado, "reprova"),
    ("as duas paginas voltam a servir o MESMO shortcode", m_as_duas_paginas_com_o_mesmo_shortcode, "reprova"),
    ("a segunda pagina some do registro e o banco nao sabe", m_segunda_pagina_some_do_registro, "reprova"),
    ("dois caquinhos que decidem diferente numa tabela so", m_dois_caquinhos_diferentes_numa_tabela_so, "reprova"),
    ("a pagina some da listagem da mae (orfa)", m_pagina_some_da_mae, "reprova-na-casca"),
    ("dois caquinhos que decidem diferente, duas tabelas", m_dois_caquinhos_que_decidem_diferente, "mundo-que-passa"),
    ("o banco de tecnicas sai do ar", m_banco_fora_do_ar, "pagina-honesta"),
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
    rc, saida = rodar(ILHA, "teste-tecnicas.php")
    if rc != 0:
        print("As paginas de verdade ja estao reprovadas — conserte antes de mutar.")
        print(saida[-2000:])
        return 1
    print("paginas intactas: APROVADAS (como tem que estar antes de comecar)\n")

    erradas = []
    for nome, mutar, esperado in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-tecpag-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            mutar(copia)

            if esperado == "pagina-honesta":
                corpo = corpo_da_pagina(copia, TAG_DA_PRIMEIRA)
                honesta = "ainda não chegou ao site" in corpo
                sem_grade = "cdm-tec-tabela" not in corpo
                if honesta and sem_grade:
                    print("  ficou honesta como devia: %-48s | diz que nao mediu e NAO serve a grade" % nome)
                else:
                    erradas.append(nome + " (a pagina %s)" % (
                        "serviu a grade sem banco" if not sem_grade else "nao disse que ficou sem medicao"))
                    print("  INVENTOU (a trava NAO viu): %s" % nome)
                continue

            if esperado == "mundo-que-passa":
                rc, saida = rodar(copia, "teste-tecnicas.php")
                corpo = corpo_da_pagina(copia, "cdm_tecnica_trencadis")
                tabelas = corpo.count('<table class="cdm-tec-tabela"')
                if 0 == rc and 2 == tabelas:
                    print("  passou como devia:        %-48s | 2 tabelas servidas" % nome)
                else:
                    erradas.append(nome + " (rc=%d, %d tabelas — esperado rc=0 e 2 tabelas)" % (rc, tabelas))
                    print("  NAO PASSOU (o ramo das duas tabelas nao esta de pe): %s" % nome)
                continue

            teste = "teste-casca.php" if esperado == "reprova-na-casca" else "teste-tecnicas.php"
            rc, saida = rodar(copia, teste)
            primeira = ""
            for linha in saida.splitlines():
                if linha.strip().startswith("FALHA"):
                    primeira = linha.strip()[5:].strip()
                    break
            if rc != 0:
                print("  reprovou como devia:      %-48s | %s" % (nome, primeira[:70]))
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
