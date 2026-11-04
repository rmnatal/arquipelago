#!/usr/bin/env python3
"""
ATUALIZA O manifest.json DESTA ILHA — e IMPRIME CADA TROCA QUE FAZ.

Por que imprimir: a secao 8 do ARQUIPELAGO.md registra a cicatriz da Aquametria
de 11/09/2026, em que "a ferramenta que atualiza o manifest so recalculava
sha256: o `titulo` NUNCA era reespelhado", e o resultado foi o corpo de nove
paginas trocando no ar e os nove titulos nao. A regra que saiu de la e literal:
"a ferramenta que espelha um campo de uma fonte para outra imprime cada troca
que fez, senao o espelho envelhece calado".

A REVISAO SOBE SOZINHA quando alguma troca acontece, e nunca e digitada: revisao
digitada e a familia do numero de tela digitado. E DESDE 04/11/2026 O
`atualizado_em` SOBE COM ELA, no mesmo gesto — ver a secao do `atualizado_em`
mais abaixo.

DOIS CAMPOS SAO ESPELHADOS, E O SEGUNDO NASCEU EM 02/11/2026
===========================================================

  `sha256` — o conteudo do arquivo. Diz se o BYTE mudou.
  `versao` — a constante `*_VERSAO` que o proprio snippet define. Diz QUAL
             VERSAO aquele byte se declara ser.

O `versao` existe porque em 30/10/2026 esta ilha mediu o seguinte, e esta
escrito no REGISTRO.md daquele dia: o comentario da vitrine afirmava que
"`atualizar-manifest.py` casa esta constante com o campo `versao` do manifest"
e **nao casava, e nunca casou** — a palavra `versao` nao aparecia uma vez nesta
ferramenta e os itens de `snippets` nao tinham o campo. `RODAMETRIA_PRODUTO_VERSAO`
e `RODAMETRIA_F2_VERSAO` eram **lidas por ninguem**; so a da casca era viva,
porque e o gatilho de reinstalacao dela. Naquela passada o que saiu foi a frase
que prometia um portao inexistente, e o campo ficou pre-registrado como bloco,
porque mexer no manifest e mexer no CONTRATO DO SYNC — o unico canal desta ilha.

E a licao que o campo carrega e a da 32.5-d: **comentario que declara um
mecanismo parece conferido e nao mede nada.** Subir uma constante que ninguem le
e rastro, nao mecanismo. A partir deste campo, subi-la sem reespelhar REPROVA.

POR QUE A CONSTANTE E ACHADA NO ARQUIVO E NUNCA DERIVADA DO `id`
================================================================

Seria natural escrever `id.upper().replace('-', '_') + '_VERSAO'` e ler
`rodametria-institucional` como `RODAMETRIA_INSTITUCIONAL_VERSAO`. **Esse
constante nao existe:** o arquivo define `RODAMETRIA_INST_VERSAO`, abreviado.
Convencao derivada de cabeca acerta em tres dos quatro snippets desta ilha e
erra no quarto — e erraria CALADA, porque "constante ausente" pareceria "snippet
sem versao". Entao a ferramenta PERGUNTA AO ARQUIVO quem ele define, e:

  - zero `define( '..._VERSAO', '...' )` no snippet  -> DENUNCIA e sai 1;
  - mais de um                                       -> DENUNCIA e sai 1.

Nunca escolhe. Espelho que adivinha a fonte nao e espelho. E a ferramenta
IMPRIME o nome da constante que leu, para o espelho ser auditavel sem abrir o
PHP — mesma razao de imprimir a troca.

O `atualizado_em` — ITEM 5 DO DESPACHO DA RONDA DE 04/11/2026
===========================================================

O defeito medido: `manifest.json` dizia `atualizado_em: 2026-11-02` na revisao
**40**, publicada em 04/11. A revisao batia (`/status` em 40, manifest em 40); a
data ao lado dela era de dois dias antes. A secao 3 manda incrementar a revisao
**e** atualizar o `atualizado_em` no mesmo commit, e a execucao daquela manha
subiu a revisao deixando a data velha — porque a data era DIGITADA A MAO e a
revisao nao.

A regra aqui e a mesma da revisao: **data que sobe sozinha nao esquece.** Quando
esta ferramenta troca qualquer coisa, ela escreve `atualizado_em` com a data de
HOJE, lida do relogio na mesma passada, e IMPRIME a troca como imprime as outras.

E O `--conferir` NAO EXIGE "HOJE", de proposito: manifest em dia hoje continua em
dia amanha, e portao que reprova manifest certo e o caminho mais curto para
alguem ignora-lo (a licao da 20.5). O que ele exige e que o `atualizado_em` bata
com a data do **ultimo commit que tocou o manifest** — que e a frase do despacho
("igual a data do commit que subiu a revisao corrente"). Em clone RASO desta
nuvem o git pode nao ter esse commit; nesse caso o portao DIZ que nao pudo
conferir, em vez de aprovar com cara de completo (a licao do `git log` raso da
1.1).

Somente `snippets` tem versao: `conteudo` e `dados` sao arquivo de dado, nao
tem codigo e nao se declaram versao nenhuma.

    python3 ferramentas/atualizar-manifest.py            # escreve
    python3 ferramentas/atualizar-manifest.py --conferir  # nao escreve; falha se divergir
"""

import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)
MANIFEST = os.path.join(ILHA, "manifest.json")

# `define( 'RODAMETRIA_F2_VERSAO', '1.3.2' );` — com folga de espaco em toda
# junta, porque o PHP desta ilha e escrito com espaco dentro do parenteses.
VERSAO_RE = re.compile(
    r"""define\(\s*['"]([A-Z][A-Z0-9_]*_VERSAO)['"]\s*,\s*['"]([^'"]+)['"]\s*\)"""
)


def hoje():
    """A data de HOJE, do relogio, nunca digitada."""
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def data_do_ultimo_commit():
    """A data do ultimo commit que tocou o manifest, ou None se o git nao souber.

    None nao e "esta certo": e "nao pude conferir", e quem chama imprime isso.
    """
    try:
        r = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=format:%Y-%m-%d", "--", MANIFEST],
            cwd=ILHA, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    saida = (r.stdout or "").strip()

    return saida if re.match(r"^\d{4}-\d{2}-\d{2}$", saida) else None


def sha(rel):
    with open(os.path.join(ILHA, rel), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def versao_do_arquivo(rel):
    """Devolve (nome_da_constante, valor) lido do PHP, ou (None, motivo)."""
    with open(os.path.join(ILHA, rel), encoding="utf-8") as f:
        achados = VERSAO_RE.findall(f.read())
    if not achados:
        return None, ("nao define nenhuma constante `*_VERSAO` — o espelho nao "
                      "inventa versao, e derivar o nome do `id` erra calado "
                      "(RODAMETRIA_INST_VERSAO e abreviado)")
    if len(achados) > 1:
        return None, ("define %d constantes `*_VERSAO` (%s) e o espelho nao "
                      "escolhe entre elas"
                      % (len(achados), ", ".join(n for n, _ in achados)))
    return achados[0], None


def com_versao_depois_do_sha(item, valor):
    """Grava `versao` LOGO DEPOIS de `sha256`, preservando a ordem do resto.

    A ordem importa de verdade aqui: o `--conferir` compara o JSON reserializado
    com os BYTES do arquivo, entao chave que cai em lugar instavel faz o portao
    reprovar um manifest em dia.
    """
    novo = {}
    for chave, v in item.items():
        if chave == "versao":
            continue
        novo[chave] = v
        if chave == "sha256":
            novo["versao"] = valor
    if "versao" not in novo:          # item sem sha256: a versao vai no fim
        novo["versao"] = valor
    return novo


def main():
    conferir = "--conferir" in sys.argv
    m = json.load(open(MANIFEST, encoding="utf-8"))
    trocas = []
    denuncias = []
    constantes_lidas = []
    revisao_antiga = int(m.get("revisao", 0))

    for grupo in ("snippets", "conteudo", "dados"):
        itens = m.get(grupo, [])
        for i, item in enumerate(itens):
            rel = item["arquivo"]
            caminho = os.path.join(ILHA, rel)
            if not os.path.exists(caminho):
                denuncias.append("AUSENTE  %s:%s -> %s nao existe no repositorio"
                                 % (grupo, item["id"], rel))
                continue
            novo = sha(rel)
            if item.get("sha256") != novo:
                trocas.append("sha256   %s:%s  %s -> %s"
                              % (grupo, item["id"],
                                 (item.get("sha256") or "(vazio)")[:12], novo[:12]))
                item["sha256"] = novo

            if grupo != "snippets":
                continue

            lido, motivo = versao_do_arquivo(rel)
            if lido is None:
                denuncias.append("SEM VERSAO  %s:%s -> %s" % (grupo, item["id"], motivo))
                continue
            nome, valor = lido
            constantes_lidas.append("%s:%s  %s = %s" % (grupo, item["id"], nome, valor))
            if item.get("versao") != valor:
                trocas.append("versao   %s:%s  %s -> %s  (de %s)"
                              % (grupo, item["id"],
                                 item.get("versao") or "(nao tinha o campo)", valor, nome))
                itens[i] = com_versao_depois_do_sha(item, valor)

    if trocas:
        m["revisao"] = revisao_antiga + 1
        trocas.append("revisao  %d -> %d" % (revisao_antiga, m["revisao"]))
        # A DATA SOBE COM A REVISAO, no mesmo gesto e do relogio (item 5 do
        # despacho de 04/11/2026). Em `--conferir` nada e escrito: o bloco abaixo
        # compara o que esta no arquivo com o git e nunca com "hoje".
        if not conferir:
            data_nova = hoje()
            if m.get("atualizado_em") != data_nova:
                trocas.append("atualizado_em  %s -> %s"
                              % (m.get("atualizado_em") or "(vazio)", data_nova))
                m["atualizado_em"] = data_nova

    texto = json.dumps(m, ensure_ascii=False, indent=2) + "\n"

    if conferir:
        atual = open(MANIFEST, encoding="utf-8").read()
        if trocas or denuncias or atual != texto:
            print("REPROVADO: o manifest nao bate com os arquivos do repositorio.")
            for t in trocas + denuncias:
                print("  " + t)
            if not trocas and not denuncias and atual != texto:
                print("  formato   o arquivo nao esta na forma que esta ferramenta escreve")
            return 1
        for c in constantes_lidas:
            print("  versao lida de  " + c)

        do_git = data_do_ultimo_commit()
        if do_git is None:
            print("  atualizado_em   %s — NAO CONFERIDO contra o git (o ultimo commit do manifest "
                  "nao esta neste clone; a 1.1 avisa que esta nuvem clona raso)"
                  % (m.get("atualizado_em") or "(vazio)"))
        elif m.get("atualizado_em") != do_git:
            print("REPROVADO: `atualizado_em` %s e o ultimo commit do manifest e de %s."
                  % (m.get("atualizado_em") or "(vazio)", do_git))
            print("  A secao 3 manda subir a revisao E a data no MESMO commit. Rode esta "
                  "ferramenta sem --conferir, ou corrija a data para a do commit.")
            return 1
        else:
            print("  atualizado_em   %s, igual a data do ultimo commit do manifest" % do_git)

        print("APROVADO: manifest em dia, revisao %d, %d constante(s) de versao espelhada(s)."
              % (m["revisao"], len(constantes_lidas)))
        return 0

    if denuncias and not trocas:
        print("REPROVADO: nada escrito.")
        for d in denuncias:
            print("  " + d)
        return 1

    if not trocas:
        print("nada a trocar; revisao %d." % m["revisao"])
        for c in constantes_lidas:
            print("  versao lida de  " + c)
        return 0

    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write(texto)
    print("manifest atualizado:")
    for t in trocas:
        print("  " + t)
    for d in denuncias:
        print("  " + d)

    return 1 if denuncias else 0


if __name__ == "__main__":
    sys.exit(main())
