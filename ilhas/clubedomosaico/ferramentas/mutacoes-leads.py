#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DOS LEADS — adendo 3 do bloco 4d, 13/09/2026.

Cada mutacao e um defeito ESCRITO DE VOLTA no snippet de Leads (ou nos dois
snippets que ele toca). Portao que nao reprova nao vale o arquivo que ocupa.

AS REGRAS HERDADAS, e o que muda neste bloco:

  (a) ALVO QUE NAO E UNICO EDITA A COISA ERRADA E PASSA VERDE. Toda troca confere
      que a string aparece EXATAMENTE uma vez; quando nao aparece, a mutacao e
      marcada INERTE — e mutacao inerte e teste verde com outro nome.

  (b) MUTACAO QUE UM PORTAO ANTIGO JA PEGAVA NAO JUSTIFICA PORTAO NOVO. Cada uma
      roda o portao NOVO (`teste-leads.php`) e dois ANTIGOS (`teste-loja.php` e
      `teste-atelie.php`), e a saida marca as que SO o novo viu.

  (c) A MUTACAO QUE PRODUZ O MUNDO. Algumas travas so significam algo num mundo
      que o banco de hoje nao tem. A m18 e uma dessas: para medir que o nome
      DECLARADO da artesa entra na mensagem, ela precisa declarar um.

  (d) CODIGO QUEBRADO DE UM JEITO ERRADO NAO REPROVA — ele nem carrega. A saida
      separa "reprovou" de "nao compila", porque as duas parecem iguais no codigo
      de retorno e so a primeira e evidencia de que a trava funciona.

  (e) NOVA AQUI, e e a que mais importa neste bloco: ESTE E O PRIMEIRO SNIPPET
      DESTA ILHA QUE GUARDA DADO DE PESSOA. Sete das mutacoes abaixo nao medem se
      a tela esta bonita — medem se nome e telefone de uma cliente vazam para a
      URL, para o repositorio, para o indice do Google ou para quem nao e a
      artesa. Uma trava de privacidade que ninguem quebra de proposito e uma
      trava que ninguem sabe se funciona.

Uso:  python3 ferramentas/mutacoes-leads.py
"""

import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
LEADS = os.path.join("snippets", "clubedomosaico-leads.php")
LOJA = os.path.join("snippets", "clubedomosaico-loja.php")
ATELIE = os.path.join("snippets", "clubedomosaico-atelie.php")


def trocar(raiz, arquivo, antes, depois, vezes=1):
    """Troca `antes` por `depois`, exigindo que `antes` apareca exatamente `vezes`."""
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()
    achou = texto.count(antes)
    assert achou == vezes, "alvo aparece %d vez(es), esperava %d: %s" % (achou, vezes, antes[:70])
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.replace(antes, depois))


# --------------------------------------------------------------- as mutacoes

def m01(r):
    """O CPT dos interessados volta a aparecer no wp-admin. Nome e telefone de
    cliente numa lista do painel do WordPress e a area que a artesa nunca deveria
    ver, e que qualquer plugin de listagem passa a enxergar junto."""
    trocar(r, LEADS, "'show_ui'             => false,", "'show_ui'             => true,")


def m02(r):
    """O tipo vira publico. Com `public` true, cada interessado ganha um endereco
    e o nome de uma pessoa passa a ter URL propria."""
    trocar(r, LEADS, "'public'              => false,", "'public'              => true,")


def m03(r):
    """O tipo entra na API REST do nucleo. E a porta dos fundos da decisao 6:
    a copia dos leads e o CSV na mao dela, nunca um endpoint."""
    trocar(r, LEADS, "'show_in_rest'        => false,", "'show_in_rest'        => true,")


def m04(r):
    """O tipo volta para a busca do site. Procurar pelo proprio nome no campo de
    busca do site e achar o pedido que se fez e a forma mais silenciosa do
    vazamento."""
    trocar(r, LEADS, "'exclude_from_search' => true,", "'exclude_from_search' => false,")


def m05(r):
    """O NOME VOLTA A VIAJAR NA URL — a decisao 4 escrita de volta. O redirecionamento
    leva o nome em vez da chave, e ele vai parar no historico, no Referer e no log
    de acesso."""
    trocar(r, LEADS,
           "wp_safe_redirect( $url . '?cdm_lead=' . rawurlencode( $chave ) . '#cdm-quero' );",
           "wp_safe_redirect( $url . '?cdm_lead=' . rawurlencode( $chave ) . '&nome=' . rawurlencode( $nome ) . '#cdm-quero' );")


def m06(r):
    """A confirmacao para de conferir DE QUAL PECA ela e. Uma chave valida colada
    na ficha de outra peca passa a dizer "Pronto, Ana!" ali."""
    trocar(r, LEADS,
           "\tif ( (int) $peca_id !== (int) ( $guardado['peca'] ?? 0 ) ) {\n\t\treturn null;\n\t}",
           "\tif ( false ) {\n\t\treturn null;\n\t}")


def m07(r):
    """Qualquer chave fabrica a tela de enviado: o formato deixa de ser conferido
    e o transient some da conta. Digitar `?cdm_lead=x` passa a valer um envio."""
    trocar(r, LEADS,
           "\tif ( '' === $chave || ! preg_match( '/^[A-Za-z0-9]{12,40}$/', $chave ) ) {\n\t\treturn null;\n\t}",
           "\tif ( '' === $chave ) {\n\t\treturn null;\n\t}\n\tif ( true ) {\n\t\treturn array( 'nome' => 'Alguem', 'peca' => (int) $peca_id );\n\t}")


def m08(r):
    """O consentimento deixa de ser obrigatorio no servidor. O `required` do HTML
    continua la e a tela parece igual — e o formulario de qualquer outro site
    passa a poder gravar lead sem autorizacao nenhuma."""
    trocar(r, LEADS,
           "\tif ( '1' !== cdm_atelie_post( 'cdm_ok' ) ) {\n\t\t$volta( 'ok' );\n\t}",
           "\tif ( false ) {\n\t\t$volta( 'ok' );\n\t}")


def m09(r):
    """O texto do consentimento deixa de ser GRAVADO junto do lead. Fica o carimbo
    de hora sem o que a pessoa autorizou — que e metade do que a LGPD pede, e a
    metade inutil."""
    trocar(r, LEADS,
           "\tupdate_post_meta( $id, '_cdm_consentimento', array(\n\t\t'em'    => current_time( 'mysql' ),\n\t\t'texto' => cdm_leads_texto_consentimento(),\n\t) );",
           "\tupdate_post_meta( $id, '_cdm_consentimento', array(\n\t\t'em'    => current_time( 'mysql' ),\n\t) );")


def m10(r):
    """O nonce para de ser conferido. Qualquer pagina de qualquer site passa a
    poder postar leads aqui."""
    trocar(r, LEADS,
           "\tif ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_lead_' . $id ) ) {\n\t\t$volta( 'nonce' );\n\t}",
           "\tif ( false ) {\n\t\t$volta( 'nonce' );\n\t}")


def m11(r):
    """O honeypot passa a AVISAR o robo em vez de sair calado. E o unico erro que
    ensina quem esta do outro lado a contornar a trava."""
    trocar(r, LEADS,
           "\tif ( '' !== cdm_atelie_post( 'cdm_cep' ) ) {\n\t\t$volta( '' );\n\t}",
           "\tif ( '' !== cdm_atelie_post( 'cdm_cep' ) ) {\n\t\t$volta( 'nome' );\n\t}")


def m12(r):
    """O teto de envios por hora sobe de 5 para 5000 — na pratica, sai. A tela
    continua identica e so um robo descobre."""
    trocar(r, LEADS, "\tdefine( 'CDM_LEADS_TETO', 5 );", "\tdefine( 'CDM_LEADS_TETO', 5000 );")


def m13(r):
    """O limite passa a ser GLOBAL em vez de por endereco: o hash some da chave.
    Cinco envios de um robo calam o formulario para todo mundo."""
    trocar(r, LEADS,
           "\treturn (int) get_transient( 'cdm_lead_lim_' . $hash ) >= CDM_LEADS_TETO;",
           "\treturn (int) get_transient( 'cdm_lead_lim_global' ) >= CDM_LEADS_TETO;")


def m14(r):
    """O endereco de quem enviou passa a ser guardado EM TEXTO PURO na chave do
    transient, em vez do hash. O adendo proibe, e e o tipo de dado que ninguem
    percebe que esta guardado ate precisar apagar."""
    trocar(r, LEADS,
           "\tif ( function_exists( 'wp_hash' ) ) {\n\t\treturn substr( wp_hash( 'cdm-lead|' . $ip ), 0, 32 );\n\t}",
           "\tif ( function_exists( 'wp_hash' ) ) {\n\t\treturn $ip;\n\t}")


def m15(r):
    """O telefone e gravado DO JEITO QUE FOI DIGITADO, sem canonizar. Dois pedidos
    da mesma pessoa, um com parentese e outro sem, viram duas pessoas — que e
    exatamente o que a regra da Real 21 existe para impedir."""
    trocar(r, LEADS,
           "\t$zap = cdm_leads_wa_canonico( cdm_atelie_post( 'cdm_zap' ) );",
           "\t$zap = preg_replace( '/\\D+/', '', cdm_atelie_post( 'cdm_zap' ) );")


def m16(r):
    """O DDI 55 e acrescentado mesmo quando ja veio. O numero fica com 15 digitos
    e o `wa.me` da artesa aponta para um telefone que nao existe."""
    trocar(r, LEADS,
           "\tif ( 13 === strlen( $so ) && '55' === substr( $so, 0, 2 ) ) {\n\t\t$so = substr( $so, 2 );\n\t}",
           "\tif ( false ) {\n\t\t$so = substr( $so, 2 );\n\t}")


def m17(r):
    """O celular de 9 digitos para de exigir o 9 na frente. A borda da regra some
    e um fixo digitado errado vira celular valido."""
    trocar(r, LEADS,
           "\tif ( 9 === strlen( $assinante ) && '9' !== substr( $assinante, 0, 1 ) ) {\n\t\treturn '';\n\t}",
           "\tif ( false ) {\n\t\treturn '';\n\t}")


def m18(r):
    """PRODUZ O MUNDO: a funcao do nome da artesa volta a ler o `first_name` da
    usuaria — que e o defeito REAL que o portao pegou em 13/09, porque o Atelie
    grava ali o texto de espera "Artesã". A mensagem passa a dizer "Aqui é
    Artesã" para uma cliente de verdade."""
    trocar(r, LEADS,
           "\t$nome = trim( (string) get_option( 'cdm_artesa_nome', '' ) );",
           "\t$u = function_exists( 'cdm_atelie_usuaria' ) ? cdm_atelie_usuaria() : null;\n\t$nome = ( $u && isset( $u->first_name ) ) ? trim( (string) $u->first_name ) : '';")


def m19(r):
    """O `wa.me` do e-mail aponta para o numero da ARTESA em vez do da cliente.
    O e-mail continua com a cara certa e o botao abre uma conversa dela com ela
    mesma."""
    trocar(r, LEADS,
           "\treturn 'https://wa.me/' . $so . '?text='",
           "\treturn 'https://wa.me/' . ( function_exists( 'cdm_loja_whatsapp' ) ? cdm_loja_whatsapp() : $so ) . '?text='")


def m20(r):
    """A disponibilidade da mensagem passa a INVENTAR quando o campo esta vazio:
    peca sem disponibilidade gravada vira "pronta". E a frase que a artesa vai
    mandar para alguem, com um dado que ninguem declarou."""
    trocar(r, LEADS,
           "\treturn '';\n}\n}\n\nif ( ! function_exists( 'cdm_leads_mensagem_para_cliente' ) ) {",
           "\treturn 'Ela está pronta, já feita.';\n}\n}\n\nif ( ! function_exists( 'cdm_leads_mensagem_para_cliente' ) ) {")


def m21(r):
    """O e-mail perde o rodape que diz POR QUE ele chegou. Sem ele a mensagem
    parece mala direta e a Hotmail trata como tal."""
    trocar(r, LEADS,
           "\t$h .= 'Este e-mail foi enviado pelo Clube do Mosaico porque um cliente pediu para verificar disponibilidade.';",
           "\t$h .= 'Clube do Mosaico.';")


def m22(r):
    """O Raphael volta a receber copia de TODO lead, sem a option. O adendo e
    explicito no contrario, e e dado de pessoa indo para uma caixa a mais sem
    ninguem ter pedido."""
    trocar(r, LEADS,
           "\t$copia = sanitize_email( (string) get_option( 'cdm_email_leads_copia', '' ) );",
           "\t$copia = sanitize_email( (string) get_option( 'cdm_email_leads_copia', 'raphaeh9@gmail.com' ) );")


def m23(r):
    """O e-mail que falha passa a DERRUBAR o lead: a gravacao acontece depois do
    aviso e so se ele der certo. No dia em que a Hotmail recusar, o pedido da
    cliente some sem deixar rastro — e a aba Interessados existe justamente para
    esse dia."""
    trocar(r, LEADS,
           "\t$lead_id = cdm_leads_gravar( $peca, $nome, $zap, $origem );\n\tif ( $lead_id <= 0 ) {\n\t\t$volta( 'peca' );\n\t}\n\n\tcdm_leads_contar_envio( $hash );\n\tcdm_leads_notificar( $lead_id, $peca );",
           "\t$lead_id = cdm_leads_gravar( $peca, $nome, $zap, $origem );\n\tif ( $lead_id <= 0 ) {\n\t\t$volta( 'peca' );\n\t}\n\n\tcdm_leads_contar_envio( $hash );\n\tif ( ! cdm_leads_notificar( $lead_id, $peca ) ) {\n\t\twp_delete_post( $lead_id, true );\n\t\t$volta( 'peca' );\n\t}")


def m24(r):
    """O NOME DA PESSOA VOLTA PARA O TITULO DO REGISTRO. E o campo que aparece em
    qualquer listagem futura do WordPress, e o unico que nao precisa estar la."""
    trocar(r, LEADS,
           "\t\t'post_title'  => 'Interesse: ' . (string) $peca->post_title,",
           "\t\t'post_title'  => 'Interesse: ' . (string) $peca->post_title . ' — ' . $nome,")


def m25(r):
    """A aba Interessados deixa de conferir a capacidade antes de gravar o estado.
    Nonce sem capacidade protege do site de fora e nao da pessoa errada logada."""
    trocar(r, LEADS,
           "\t\tif ( ! current_user_can( 'edit_pecas' ) ) {\n\t\t\twp_safe_redirect( cdm_atelie_url( array( 'estado' => 'interessados', 'aviso' => 'nonce' ) ) );\n\t\t\texit;\n\t\t}",
           "\t\tif ( false ) {\n\t\t\twp_safe_redirect( cdm_atelie_url( array( 'estado' => 'interessados', 'aviso' => 'nonce' ) ) );\n\t\t\texit;\n\t\t}")


def m26(r):
    """O CSV troca o ponto-e-virgula pela virgula. No Excel em portugues a
    planilha inteira cai numa coluna so, e a copia da secao 24 vira um arquivo
    que ela nao consegue abrir."""
    trocar(r, LEADS, "\t$saida .= implode( ';', $cab ) . \"\\r\\n\";",
           "\t$saida .= implode( ',', $cab ) . \"\\r\\n\";")


def m27(r):
    """O CSV perde o BOM. O Excel le UTF-8 como Latin-1 e todo nome com acento
    chega torto na tela dela."""
    trocar(r, LEADS, "\t$saida = \"\\xEF\\xBB\\xBF\";", "\t$saida = '';")


def m28(r):
    """A aspa dentro de um campo do CSV para de ser duplicada. Um nome de peca com
    aspas quebra a coluna a partir dali."""
    trocar(r, LEADS,
           "\t\t\t$escapados[] = '\"' . str_replace( '\"', '\"\"', (string) $c ) . '\"';",
           "\t\t\t$escapados[] = '\"' . (string) $c . '\"';")


def m29(r):
    """O estado com `?cdm_lead=` deixa de sair do indice. Cada envio passa a poder
    virar uma URL indexada da mesma ficha — e a peca, que e a pagina que vende,
    passa a disputar consigo mesma."""
    trocar(r, LEADS,
           "\t\techo '<meta name=\"robots\" content=\"noindex, follow\">' . \"\\n\";",
           "\t\treturn;")


def m30(r):
    """O `<details>` vira uma `<div>` com um `<button>` que so o JavaScript abre.
    Com o script desligado o formulario deixa de existir — a secao 22.8 escrita
    de volta."""
    trocar(r, LEADS,
           "\t$h .= '<details class=\"cdm-lead\"' . $aberto . '>';\n\t$h .= '<summary class=\"cdm-botao cdm-lead-abre\">Verificar disponibilidade</summary>';",
           "\t$h .= '<div class=\"cdm-lead\" hidden>';\n\t$h .= '<button class=\"cdm-botao cdm-lead-abre\" type=\"button\">Verificar disponibilidade</button>';")


def m31(r):
    """O honeypot sai do caminho do teclado mas fica VISIVEL: perde a classe que o
    esconde. Uma pessoa passa a ver um campo pedindo para nao ser preenchido."""
    trocar(r, LEADS, "\t$h .= '<p class=\"cdm-lead-hp\" aria-hidden=\"true\">';",
           "\t$h .= '<p aria-hidden=\"true\">';")


def m32(r):
    """O formulario pede e-mail tambem. O adendo diz "Nada mais. Sem e-mail, sem
    CEP" — todo campo a mais e um dado de pessoa guardado sem motivo e uma pessoa
    a menos que termina de preencher."""
    trocar(r, LEADS,
           "\t$h .= '<p class=\"cdm-lead-consente\">';",
           "\t$h .= '<p class=\"cdm-lead-campo\"><label for=\"cdm-lead-mail-' . $id . '\">Seu e-mail</label>';\n\t$h .= '<input id=\"cdm-lead-mail-' . $id . '\" name=\"cdm_email\" type=\"text\"></p>';\n\t$h .= '<p class=\"cdm-lead-consente\">';")


def m33(r):
    """A LOJA PARA DE APLICAR O FILTRO e volta a servir o padrao. E a cicatriz de
    12/09 desta ilha escrita de volta: quem atende vira funcao morta e a ficha
    volta a dizer que o contato nao foi publicado, sem ninguem notar."""
    trocar(r, LOJA, "\t$html .= apply_filters( 'cdm_peca_acao', $padrao, $peca, array(",
           "\t$html .= $padrao; $ignorado = ( array(")


def m34(r):
    """O ATELIE PARA DE APLICAR o filtro das telas. A aba Interessados continua
    aparecendo na navegacao e nao abre — o pior dos dois estados, porque promete."""
    trocar(r, ATELIE, "\t\t$tela = apply_filters( 'cdm_atelie_tela', '', $estado, $usuaria );",
           "\t\t$tela = '';")


def m35(r):
    """A navegacao entre abas passa a aceitar QUALQUER estado da URL como aba.
    `?estado=qualquer-coisa` vira ponto de extensao de quem nao se declarou."""
    trocar(r, ATELIE, "\tif ( '' !== $estado && isset( $abas[ $estado ] ) ) {",
           "\tif ( '' !== $estado ) {")


def m36(r):
    """O painel ganha uma capacidade nova no papel `artesa`. Nao e defeito de
    comportamento e e defeito de contrato: o `conferir-atelie-no-ar.py` mede que o
    papel tem exatamente as sete do bloco anterior, e a decisao 7 deste snippet
    existe para isso nao mudar por acidente."""
    trocar(r, ATELIE, "\t\t'edit_pecas'              => true,",
           "\t\t'edit_pecas'              => true,\n\t\t'ler_interessados'        => true,")


MUTACOES = [
    ("01 o CPT de interessados volta ao wp-admin", m01),
    ("02 o tipo vira publico (cada lead ganha URL)", m02),
    ("03 o tipo entra na REST do nucleo", m03),
    ("04 o tipo volta para a busca do site", m04),
    ("05 PRIVACIDADE: o nome volta a viajar na URL", m05),
    ("06 a confirmacao nao confere de qual peca e", m06),
    ("07 qualquer chave fabrica a tela de enviado", m07),
    ("08 o consentimento deixa de ser exigido no servidor", m08),
    ("09 LGPD: o texto autorizado nao e mais gravado", m09),
    ("10 o nonce para de ser conferido", m10),
    ("11 o honeypot avisa o robo", m11),
    ("12 o teto de 5 por hora vira 5000", m12),
    ("13 o limite vira global (um robo cala o site)", m13),
    ("14 PRIVACIDADE: o IP e guardado em texto puro", m14),
    ("15 o telefone e gravado sem canonizar", m15),
    ("16 o DDI 55 duplica", m16),
    ("17 BORDA: o celular de 9 nao precisa mais do 9", m17),
    ("18 PRODUZ O MUNDO: o nome volta a sair do first_name", m18),
    ("19 o wa.me do e-mail aponta para a artesa", m19),
    ("20 a disponibilidade e inventada quando falta", m20),
    ("21 o e-mail perde o rodape que diz por que chegou", m21),
    ("22 o Raphael volta a receber copia de todo lead", m22),
    ("23 e-mail que falha apaga o lead", m23),
    ("24 PRIVACIDADE: o nome volta para o titulo do registro", m24),
    ("25 a aba grava estado sem conferir capacidade", m25),
    ("26 o CSV troca ponto-e-virgula por virgula", m26),
    ("27 o CSV perde o BOM", m27),
    ("28 o CSV nao duplica a aspa", m28),
    ("29 o estado com parametro volta ao indice", m29),
    ("30 22.8: o formulario passa a depender de JavaScript", m30),
    ("31 o honeypot fica visivel", m31),
    ("32 o formulario passa a pedir e-mail", m32),
    ("33 a Loja para de aplicar o filtro", m33),
    ("34 o Atelie para de aplicar o filtro das telas", m34),
    ("35 qualquer ?estado vira aba", m35),
    ("36 o papel artesa ganha capacidade nova", m36),
]

PORTAO_NOVO = "teste-leads.php"
PORTOES_ANTIGOS = ["teste-loja.php", "teste-atelie.php"]


def rodar(raiz, portao):
    r = subprocess.run(["php", os.path.join(raiz, "ferramentas", portao), raiz],
                       capture_output=True, text=True)
    saida = r.stdout + r.stderr
    nao_compila = ("Parse error" in saida) or ("Fatal error" in saida)
    return r.returncode, saida, nao_compila


def primeira_falha(saida):
    for linha in saida.splitlines():
        if "FALHA" in linha:
            return " ".join(linha.split())[6:]
    return ""


def main():
    passaram, quebradas, so_o_novo, inertes = [], [], [], []

    print("MUTACOES DOS LEADS — %d defeitos escritos de volta\n" % len(MUTACOES))
    print("Portao novo: %s | antigos: %s\n" % (PORTAO_NOVO, ", ".join(PORTOES_ANTIGOS)))

    for nome, fn in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="cdm-mut-leads-")
        copia = os.path.join(tmp, "ilha")
        try:
            shutil.copytree(ILHA, copia)
            try:
                fn(copia)
            except AssertionError as e:
                inertes.append(nome)
                print("  INERTE (alvo nao e unico, nao mede nada): %s — %s" % (nome, e))
                continue

            rc_novo, saida_novo, quebrou = rodar(copia, PORTAO_NOVO)
            rcs_velhos, saidas_velhas = [], []
            for p in PORTOES_ANTIGOS:
                rc, saida, q = rodar(copia, p)
                rcs_velhos.append(rc)
                saidas_velhas.append(saida)
                quebrou = quebrou or q

            if quebrou:
                quebradas.append(nome)
                print("  NAO COMPILA (nao e evidencia de trava): %s" % nome)
                continue

            if rc_novo == 0 and all(rc == 0 for rc in rcs_velhos):
                passaram.append(nome)
                print("  PASSOU (nenhuma trava viu): %s" % nome)
                continue

            marca = ""
            if rc_novo != 0 and all(rc == 0 for rc in rcs_velhos):
                so_o_novo.append(nome)
                marca = "  <-- SO o portao NOVO viu"
            qual = saida_novo if rc_novo != 0 else saidas_velhas[rcs_velhos.index(
                next(rc for rc in rcs_velhos if rc != 0))]
            print("  reprovou como devia: %-50s | %s%s" % (nome, primeira_falha(qual)[:56], marca))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    reprovadas = len(MUTACOES) - len(passaram) - len(quebradas) - len(inertes)
    print("\n%d mutacoes, %d reprovadas, %d passaram, %d nao compilaram, %d inertes" %
          (len(MUTACOES), reprovadas, len(passaram), len(quebradas), len(inertes)))
    if so_o_novo:
        print("\nAS QUE SO O PORTAO NOVO PEGOU (%d) — e o que justifica ele existir:" % len(so_o_novo))
        for nome in so_o_novo:
            print("  - %s" % nome)
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
    if inertes:
        print("\nAS INERTES precisam de alvo novo: mutacao que nao edita nada e")
        print("teste verde com outro nome.")
        for nome in inertes:
            print("  - %s" % nome)
    return 1 if (passaram or quebradas or inertes) else 0


if __name__ == "__main__":
    sys.exit(main())
