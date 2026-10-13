#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutacoes de `medir-espelho.py`: prova que o autoteste dele NAO E INERTE.

    python3 ferramentas/mutacoes-espelho.py .

POR QUE ESTA BATERIA EXISTE. Em 13/10/2026 o `medir-espelho.py` furava DUAS das quatro travas
que ele mesmo declara, e passava no proprio autoteste com 24 de 24: as travas falhavam em
lugares que o autoteste nao media. A identidade do documento saia da PRIMEIRA linha da pagina
1 (o cabecalho corrido, texto de molde) em vez da linha com que o documento nomeia o produto,
e a derivacao do inventario varria o `canal-de-espelho.json` que ela gera, devolvendo a lista
digitada como derivada. Autoteste verde sobre a metade medida e exatamente o que esta bateria
existe para nao deixar acontecer de novo.

COMO ELA TRABALHA, e e de proposito: ela copia o `medir-espelho.py` para um `tempfile.mkdtemp(`,
muta a COPIA e roda o `--autoteste` da copia. Nada no repositorio e tocado — a cicatriz do
`mutacoes-par.py` de 09/10/2026, que deixou um snippet mutado no `main`, esta escrita no
PROMPT.md desta ilha. A chamada e `mkdtemp(` e nao `TemporaryDirectory()` por um motivo que nao
e de gosto: o `teste-rede-de-sinal.py` classifica as baterias por CHAMADA de `mkdtemp(`, e uma
bateria que trabalha em copia mas nao fala a palavra da regua entra na lista errada — a lista
das que podem sujar a arvore.

E CADA MUTACAO DECLARA A FRASE QUE ESPERA OUVIR DE VOLTA. Reprovar nao e a mesma coisa que
reprovar PELO MOTIVO CERTO: sem a frase, uma mutacao pode disparar outra trava, sair vermelha
e nunca ter medido a sua.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = sys.argv[1].rstrip("/") if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
ALVO = os.path.join(RAIZ, "ferramentas", "medir-espelho.py")

# (nome, de, para, tem_de_reprovar, frase_que_a_quebra_tem_de_ouvir, por_que)
MUTACOES = [
    ("a regra VELHA de volta: identidade = primeira linha da pagina 1",
     '    return {"familia_do_documento": "molde_nao_reconhecido", "cabecalho_corrido": linhas[0],\n'
     '            "produto_declarado": None, "o_que_o_cabecalho_e": "nao_comparavel"}',
     '    return {"familia_do_documento": "molde_nao_reconhecido", "cabecalho_corrido": linhas[0],\n'
     '            "produto_declarado": linhas[0], "o_que_o_cabecalho_e": "nao_comparavel"}',
     True, "FALHA i08",
     "molde desconhecido voltando a cair no cabecalho e o defeito em estado puro"),

    ("a ordem invertida: marca de pagina antes de FISPQ",
     '    if any(MARCA_FISPQ.search(l) for l in linhas[:5]):',
     '    if False and any(MARCA_FISPQ.search(l) for l in linhas[:5]):',
     True, "FALHA i04",
     "e a armadilha de ordem: a FISPQ tambem tem marca de pagina, e ela vem DEPOIS do produto"),

    ("o produto do boletim lido do cabecalho em vez da linha de baixo",
     '            produto = linhas[i + 1] if i + 1 < len(linhas) else None',
     '            produto = cabecalho',
     True, "FALHA i01",
     "e o defeito medido em 1338838.pdf: cabecalho de molde servindo de identidade"),

    ("o veredito do cabecalho sempre `nomeia_o_mesmo_produto`",
     '    return "nomeia_OUTRO_produto"',
     '    return "nomeia_o_mesmo_produto"',
     True, "FALHA i02",
     "divergencia que nunca acusa e pior que coluna ausente: ela afirma que bate"),

    ("o veredito do cabecalho sempre `nomeia_OUTRO_produto`",
     '    if a in b or b in a:\n        return "nomeia_o_mesmo_produto"',
     '    if False:\n        return "nomeia_o_mesmo_produto"',
     True, "FALHA i01",
     "a trava tem de morder nos DOIS lados da fronteira, nao so num"),

    ("a FISPQ sem produto caindo de volta no cabecalho",
     '        return {"familia_do_documento": "fispq", "cabecalho_corrido": linhas[0],\n'
     '                "produto_declarado": produto,',
     '        return {"familia_do_documento": "fispq", "cabecalho_corrido": linhas[0],\n'
     '                "produto_declarado": produto or linhas[0],',
     True, "FALHA i07",
     "ausencia se ve; identidade errada nao, e e por isso que `None` e o valor certo"),

    ("a derivacao volta a varrer o arquivo que ela gera",
     'GERADOS_QUE_NAO_SAO_BANCO = (\n    "canal-de-espelho.json",\n)',
     'GERADOS_QUE_NAO_SAO_BANCO = (\n)',
     True, "FALHA d02",
     "e a trava 1 inteira: sem isto a lista digitada volta como derivada, citada pelo gerado"),

    ("o corte de linha util em 0: `FISPQ` solto passa a ser cabecalho",
     '        if len(linha) > 8:\n            saida.append(linha)',
     '        if len(linha) > 0:\n            saida.append(linha)',
     True, "FALHA i04",
     "o corte nao e estetica: e ele que tira numero de pagina solto e sujeira de layout — e"
     " esta mutacao SO morde porque o autoteste passou a cobrar o `cabecalho_corrido` tambem;"
     " na primeira versao dela a bateria saiu verde e o buraco era do autoteste"),

    ("MUNDO QUE TEM DE PASSAR: mexer num comentario nao muda veredito nenhum",
     "# Os casos de identidade.",
     "# Os casos de identidade (comentario mutado de proposito).",
     False, None,
     "bateria que reprova qualquer edicao nao mede nada; esta tem de sair verde aqui"),
]


def roda(caminho_do_script, trabalho):
    r = subprocess.run([sys.executable, caminho_do_script, trabalho, "--autoteste"],
                       capture_output=True, text=True, timeout=180)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    original = open(ALVO, encoding="utf-8").read()
    print("Mutacoes de medir-espelho.py — a copia e mutada em mkdtemp, o repositorio nao e tocado")
    trabalho = tempfile.mkdtemp(prefix="mutacoes-espelho-")
    try:
        copia = os.path.join(trabalho, "medir-espelho.py")
        shutil.copy(ALVO, copia)
        cod, saida = roda(copia, trabalho)
        if cod != 0:
            print("  FALHA 00  o autoteste da COPIA LIMPA tem de passar antes de qualquer mutacao")
            print(saida[-1500:])
            return 1
        # A ULTIMA ocorrencia, nunca a primeira: o texto dos casos tem "1 de 3" dentro, e
        # pegar a primeira faz a bateria anunciar "1 de 3" como se fosse o total.
        base = re.findall(r"\d+ de \d+", saida)
        print("  ok    00  a copia limpa passa  %s" % (base[-1] if base else "?"))

        falhas = 0
        for i, (nome, de, para, reprova, frase, porque) in enumerate(MUTACOES, 1):
            if de not in original:
                print("  FALHA %02d  o alvo da mutacao NAO EXISTE mais no arquivo: %s" % (i, nome))
                print("            (mutacao inerte e pior que mutacao ausente — ela sai verde calada)")
                falhas += 1
                continue
            with open(copia, "w", encoding="utf-8") as fh:
                fh.write(original.replace(de, para, 1))
            cod, saida = roda(copia, trabalho)
            reprovou = cod != 0
            ok = reprovou == reprova
            disse = (frase in saida) if (frase and reprovou) else (frase is None)
            ok = ok and disse
            falhas += 0 if ok else 1
            print("  %-5s %02d  %-64s -> %s%s"
                  % ("ok" if ok else "FALHA", i, nome[:64],
                     "REPROVOU" if reprovou else "passou",
                     "" if disse else "  [NAO disse %r]" % frase))
            if not ok:
                print("            esperado: %s%s" % ("REPROVAR" if reprova else "PASSAR",
                                                      " dizendo %r" % frase if frase else ""))
            print("            %s" % porque)
            shutil.copy(ALVO, copia)
    finally:
        shutil.rmtree(trabalho, ignore_errors=True)

    total = len(MUTACOES)
    print("  %d de %d" % (total - falhas, total))
    return 0 if falhas == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
