#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MUTACOES DO ATELIE — bloco 4d, 12/09/2026.

O painel da artesa e a primeira coisa desta fabrica que uma pessoa de fora vai
usar, e e a area de UMA pessoa: as mutacoes aqui nao sao sobre numero errado na
tela, sao sobre acesso, senha e dado de alguem. Duas familias, e as duas contam:

  AS QUE ABREM PORTA — o bloqueio do wp-admin que para de bloquear, o papel que
  ganha capacidade demais, o nonce que para de ser conferido, a peca de outra
  pessoa que ela passa a poder apagar, o endpoint que fica publico.

  AS QUE VAZAM SEGREDO — a senha que aparece em e-mail ou log, o link de
  redefinicao que vai para o Raphael, o "esqueci a senha" que responde diferente
  para e-mail que existe e revela quem tem conta no site.

Regras herdadas: alvo tem de ser UNICO (senao a mutacao edita a coisa errada e
passa verde), e cada mutacao roda os portoes que podem ve-la — `teste-atelie.php`
(novo) e `teste-casca.php` (antigo, que e quem sabe de noindex e sitemap) — com a
saida marcando as que SO o novo pegou. E "nao compila" e separado de "reprovou",
porque codigo que nem carrega nao e evidencia de trava nenhuma.

Uso:  python3 ferramentas/mutacoes-atelie.py
"""

import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
SNIPPET = os.path.join("snippets", "clubedomosaico-atelie.php")


def trocar(raiz, arquivo, antes, depois, vezes=1):
    caminho = os.path.join(raiz, arquivo)
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()
    achou = texto.count(antes)
    assert achou == vezes, "alvo aparece %d vez(es), esperava %d: %s" % (achou, vezes, antes[:60])
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.replace(antes, depois))


# ------------------------------------------------- familia 1: as que abrem porta

def m01(r):
    """O bloqueio do wp-admin para de bloquear. Ela abre um menu "Posts / Midia /
    Ferramentas" e o despacho esta descumprido mesmo que nada quebre."""
    trocar(r, SNIPPET, "	wp_safe_redirect( cdm_atelie_url(), 302 );\n\texit;\n} );",
           "	return;\n} );")


def m02(r):
    """A barra do WordPress volta a aparecer para ela no site."""
    trocar(r, SNIPPET, "	return cdm_atelie_e_artesa() ? false : $mostrar;",
           "	return $mostrar;")


def m03(r):
    """O papel ganha `edit_others_pecas`. E a ausencia mais importante do arquivo
    virando presenca: ela passa a poder editar peca de qualquer pessoa."""
    trocar(r, SNIPPET, "		'edit_published_pecas'    => true,",
           "		'edit_published_pecas'    => true,\n\t\t'edit_others_pecas'       => true,")


def m04(r):
    """O papel ganha `manage_options`: ela vira administradora do site sem que a
    palavra apareca em lugar nenhum."""
    trocar(r, SNIPPET, "		'read'                    => true,",
           "		'read'                    => true,\n\t\t'manage_options'          => true,")


def m05(r):
    """O papel perde `upload_files`. Sem isso ela nao consegue por foto — e sem foto
    a peca nao publica. O painel fica inteiro e inutil."""
    trocar(r, SNIPPET, "		'upload_files'            => true,\n", "")


def m06(r):
    """O nonce de salvar para de ser conferido: qualquer formulario em qualquer site
    passa a poder criar peca na loja dela."""
    trocar(r, SNIPPET, """		if ( ! wp_verify_nonce( cdm_atelie_post( 'cdm_nonce' ), 'cdm_atelie_salvar' ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'nonce' ) ) );
			exit;
		}
		$id      = (int) cdm_atelie_post( 'cdm_peca', '0' );""",
        """		$id      = (int) cdm_atelie_post( 'cdm_peca', '0' );""")


def m07(r):
    """A dona da peca deixa de ser conferida: `cdm_atelie_minha_peca()` devolve
    qualquer peca. E o caminho por onde publicar, pausar e apagar passam a valer
    para a peca de outra pessoa."""
    trocar(r, SNIPPET, """	if ( ! current_user_can( 'edit_post', $id ) ) {
		return null;
	}
""", "")


def m08(r):
    """A guarda de sessao cai: quem nao entrou passa a poder agir."""
    trocar(r, SNIPPET, """	if ( ! is_user_logged_in() || ! current_user_can( 'edit_pecas' ) ) {
		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'entre' ) ) );
		exit;
	}
""", "")


def m09(r):
    """A chave de redefinicao para de ser validada: qualquer texto na URL passa a
    trocar a senha dela."""
    trocar(r, SNIPPET, """		$usuaria = check_password_reset_key( $chave, $login );
		if ( is_wp_error( $usuaria ) ) {
			wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'chave' ) ) );
			exit;
		}""",
        """		$usuaria = get_user_by( 'login', $login );""")


def m10(r):
    """Apagar deixa de ir para a lixeira e passa a apagar de verdade. Ela aperta com
    o dedo num telefone; a peca tem de dar para voltar."""
    trocar(r, SNIPPET, "		wp_trash_post( $id );", "		wp_delete_post( $id, true );")


def m11(r):
    """A rota de conferencia do acesso fica publica: o estado da conta de alguem
    (existe, papel, quando o e-mail saiu) passa a sair para qualquer um."""
    trocar(r, SNIPPET, """		'permission_callback' => function ( $pedido ) {
			if ( ! function_exists( 'cdm_loja_token_esperado' ) ) {
				return false;
			}
			$esperado = cdm_loja_token_esperado();
			$vindo    = (string) $pedido->get_param( 'token' );

			return '' !== $esperado && '' !== $vindo && hash_equals( $esperado, $vindo );
		},""",
        """		'permission_callback' => '__return_true',""")


def m12(r):
    """A escolha deixa de ser conferida contra a lista: qualquer texto entra como
    base ou disponibilidade, e a ficha passa a imprimir o que alguem mandar."""
    trocar(r, SNIPPET, """			case 'escolha':
				$opcoes = isset( $def['opcoes'] ) ? $def['opcoes'] : array();
				$valor  = isset( $opcoes[ $bruto ] ) ? $bruto : '';
				break;""",
        """			case 'escolha':
				$valor = $bruto;
				break;""")


# ------------------------------------------------ familia 2: as que vazam segredo

def m13(r):
    """A SENHA ALEATORIA VAI PARA O E-MAIL. E a mutacao mais grave do arquivo: a
    senha existe para ser descartada sem nunca ser escrita em lugar nenhum."""
    trocar(r, SNIPPET, "		unset( $descartada );",
           "		update_option( 'cdm_atelie_senha_inicial', $descartada );")


def m14(r):
    """O link de criar senha passa a ir no aviso do Raphael. O despacho de 11/09
    proibe isso com todas as letras: o link chega so na caixa dela."""
    trocar(r, SNIPPET, "			. '<br><br>O link de senha não vai nesta mensagem, de propósito: ele chega só na caixa dela.</p>'",
           "			. '<br><br>Link: ' . esc_url( $link ) . '</p>'")


def m15(r):
    """O e-mail de acesso passa a sair em TODO init: a Hotmail vê dezenas de
    mensagens iguais e manda tudo para o spam — e caixa de spam aqui e uma pessoa
    esperando na frente do filho sem conseguir entrar."""
    trocar(r, SNIPPET, """	if ( is_array( $marca ) && isset( $marca['para'] ) && $agora === $marca['para'] && ! empty( $marca['enviado'] ) ) {
		return;
	}
""", "")


def m16(r):
    """O "esqueci a senha" passa a responder diferente para e-mail que existe,
    entregando quem tem conta no site a quem perguntar."""
    trocar(r, SNIPPET, """		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => 'enviado' ) ) );
		exit;
	}""",
        """		wp_safe_redirect( cdm_atelie_url( array( 'aviso' => $usuaria ? 'enviado' : 'login' ) ) );
		exit;
	}""")


def m17(r):
    """O e-mail manda para o wp-login.php em vez do painel. E a decisao 3 do
    snippet invertida: a primeira tela que ela ve na vida deste site passa a ser
    uma tela com a marca do WordPress e um medidor de forca de senha."""
    trocar(r, SNIPPET, """	return cdm_atelie_url( array(
		'criar-senha' => $chave,
		'quem'        => $usuaria->user_login,
	) );""",
        """	return home_url( '/wp-login.php?action=rp&key=' . $chave . '&login=' . rawurlencode( $usuaria->user_login ) );""")


def m18(r):
    """O e-mail do relato de conferencia para de ser mascarado: o endereco inteiro
    de uma pessoa passa a sair num log de rotina."""
    trocar(r, SNIPPET, "				'email'          => cdm_atelie_email_mascarado( CDM_ATELIE_EMAIL ),",
           "				'email'          => CDM_ATELIE_EMAIL,")


# ------------------------------------------- familia 3: as que quebram para ela

def m19(r):
    """O painel entra no indice. E a area de uma pessoa; ela passa a ser achavel no
    Google e a gastar orcamento de rastreamento de um dominio de dois dias."""
    trocar(r, SNIPPET, "		'noindex'  => true,\n\t\t'camada'   => 'privada',", "")


def m20(r):
    """A camada deixa de ser declarada: o `noindex` fica, mas a razao dele nao — e
    a ilha volta a nao saber distinguir bastidor de metodo de area de pessoa."""
    trocar(r, SNIPPET, "		'camada'   => 'privada',\n", "")


def m21(r):
    """O preco vira `type=number`, que recusa a virgula. Ela digita 180,50, o campo
    fica vermelho, e ninguem no telefone dela vai adivinhar que e para usar ponto."""
    trocar(r, SNIPPET, """			$h .= '<input id="' . esc_attr( $idhtml ) . '" name="' . esc_attr( $campo ) . '" type="text" ';
			$h .= 'inputmode="decimal" value="' . esc_attr( $valor ) . '">';""",
        """			$h .= '<input id="' . esc_attr( $idhtml ) . '" name="' . esc_attr( $campo ) . '" type="number" step="0.01" ';
			$h .= 'value="' . esc_attr( $valor ) . '">';""")


def m22(r):
    """O DEFEITO QUE ESTE BLOCO REALMENTE TEVE, escrito de volta: a direcao da foto
    num campo escondido. Campo escondido e enviado seja qual for o botao apertado,
    entao o ▶ manda "para tras" junto e a foto anda para o lado errado."""
    trocar(r, SNIPPET, """					$h .= '<button type="submit" name="cdm_acao" value="foto_tras" class="cdm-at-fbotao" title="Mover para trás">';
					$h .= '<span aria-hidden="true">◀</span><span class="cdm-at-so-leitor"> mover para trás</span></button>';
				}
				if ( $i < $total - 1 ) {
					$h .= '<button type="submit" name="cdm_acao" value="foto_frente" class="cdm-at-fbotao" title="Mover para frente">';""",
        """					$h .= '<button type="submit" name="cdm_acao" value="foto_mover" class="cdm-at-fbotao" title="Mover para trás">';
					$h .= '<span aria-hidden="true">◀</span><span class="cdm-at-so-leitor"> mover para trás</span></button>';
					$h .= '<input type="hidden" name="cdm_direcao" value="tras">';
				}
				if ( $i < $total - 1 ) {
					$h .= '<button type="submit" name="cdm_acao" value="foto_mover" class="cdm-at-fbotao" title="Mover para frente">';""")


def m23(r):
    """O prazo sobrevive a troca para pronta entrega, e a ficha passa a dizer duas
    coisas contraditorias na mesma linha."""
    trocar(r, SNIPPET, """	if ( 'sob_encomenda' !== cdm_loja_meta( $peca_id, '_cdm_disponibilidade' ) ) {
		delete_post_meta( $peca_id, '_cdm_prazo_dias' );
	}
""", "")


def m24(r):
    """O script volta para dentro do retorno do shortcode — a cicatriz de
    08/09/2026 que derrubou cinco calculadoras da Aquametria."""
    trocar(r, SNIPPET, "	$h .= '</form></div>';\n\n\treturn $h;\n}\n}\n\nadd_shortcode( 'cdm_atelie'",
           "	$h .= '</form></div>';\n\t$h .= '<script>var a=1&&2;</script>';\n\n\treturn $h;\n}\n}\n\nadd_shortcode( 'cdm_atelie'")


def m25(r):
    """A peca nasce publicada em vez de rascunho: ela toca em Nova peca, escreve o
    nome, e a peca pela metade ja esta no ar."""
    trocar(r, SNIPPET, "				'post_status'    => 'draft',\n\t\t\t\t'post_author'    => get_current_user_id(),",
           "				'post_status'    => 'publish',\n\t\t\t\t'post_author'    => get_current_user_id(),")


def m26(r):
    """A recusa de publicar perde o motivo: a tela passa a dizer que nao deu, sem
    dizer o que falta. E a diferenca entre "o botao nao funciona" e "falta a foto"."""
    trocar(r, SNIPPET, """			if ( $motivos ) {
				update_post_meta( $id, '_cdm_recusa', $motivos );
				wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id, 'aviso' => 'falta' ) ) );
				exit;
			}""",
        """			if ( $motivos ) {
				delete_post_meta( $id, '_cdm_recusa' );
				wp_safe_redirect( cdm_atelie_url( array( 'estado' => 'editar', 'peca' => $id, 'aviso' => 'falta' ) ) );
				exit;
			}""")


MUTACOES = [
    ("01 o bloqueio do wp-admin para de bloquear", m01),
    ("02 a barra do WordPress volta para ela", m02),
    ("03 o papel ganha edit_others_pecas", m03),
    ("04 o papel ganha manage_options", m04),
    ("05 o papel perde upload_files", m05),
    ("06 o nonce de salvar para de ser conferido", m06),
    ("07 a dona da peca para de ser conferida", m07),
    ("08 a guarda de sessao cai", m08),
    ("09 a chave de redefinicao para de ser validada", m09),
    ("10 apagar deixa de ir para a lixeira", m10),
    ("11 a rota de conferencia fica publica", m11),
    ("12 escolha invalida passa a ser gravada", m12),
    ("13 a senha aleatoria e guardada em option", m13),
    ("14 o link de senha vai no aviso do Raphael", m14),
    ("15 o acesso e reenviado em todo init", m15),
    ("16 esqueci-a-senha revela quem tem conta", m16),
    ("17 o e-mail manda para o wp-login.php", m17),
    ("18 o e-mail da rota para de ser mascarado", m18),
    ("19 o painel entra no indice", m19),
    ("20 a camada privada deixa de ser declarada", m20),
    ("21 o preco vira type=number (recusa a virgula)", m21),
    ("22 a direcao da foto volta ao campo escondido", m22),
    ("23 o prazo sobrevive a troca de disponibilidade", m23),
    ("24 o script volta para dentro do shortcode", m24),
    ("25 a peca nasce publicada em vez de rascunho", m25),
    ("26 a recusa de publicar perde o motivo", m26),
]


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
    for portao in ("teste-atelie.php", "teste-casca.php"):
        rc, saida, _ = rodar(ILHA, portao)
        if rc != 0:
            print("O portao %s ja esta reprovado — conserte antes de mutar." % portao)
            print(primeira_falha(saida))
            return 1
    print("Os dois portoes intactos: APROVADOS (como tem que estar antes de comecar)\n")

    passaram = []
    so_o_novo = []
    quebradas = []

    for nome, mutar in MUTACOES:
        tmp = tempfile.mkdtemp(prefix="mut-atelie-")
        copia = os.path.join(tmp, "ilha")
        shutil.copytree(ILHA, copia)
        try:
            try:
                mutar(copia)
            except AssertionError as erro:
                passaram.append(nome + " [INERTE: " + str(erro) + "]")
                print("  INERTE (nao achou o alvo): %s" % nome)
                continue

            rc_novo, saida_novo, quebrou_novo = rodar(copia, "teste-atelie.php")
            rc_velho, saida_velho, quebrou_velho = rodar(copia, "teste-casca.php")

            if quebrou_novo or quebrou_velho:
                quebradas.append(nome)
                print("  NAO COMPILA (nao e evidencia de trava): %s" % nome)
                continue

            if rc_novo == 0 and rc_velho == 0:
                passaram.append(nome)
                print("  PASSOU (nenhuma trava viu): %s" % nome)
                continue

            marca = ""
            if rc_novo != 0 and rc_velho == 0:
                so_o_novo.append(nome)
                marca = "  <-- SO o portao NOVO viu"
            qual = saida_novo if rc_novo != 0 else saida_velho
            print("  reprovou como devia: %-50s | %s%s" % (nome, primeira_falha(qual)[:56], marca))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d mutacoes, %d reprovadas, %d passaram, %d nao compilaram" %
          (len(MUTACOES), len(MUTACOES) - len(passaram) - len(quebradas), len(passaram), len(quebradas)))
    if so_o_novo:
        print("\nAS QUE SO O PORTAO NOVO PEGOU (%d) — e o que justifica ele existir:" % len(so_o_novo))
        for nome in so_o_novo:
            print("  - %s" % nome)
    if passaram:
        print("\nAS QUE PASSARAM SAO O RESULTADO DO TESTE, nao um detalhe:")
        for nome in passaram:
            print("  - %s" % nome)
        return 1
    if quebradas:
        print("\nAS QUE NAO COMPILARAM precisam ser reescritas.")
        for nome in quebradas:
            print("  - %s" % nome)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
