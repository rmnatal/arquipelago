#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le a LARGURA e a ALTURA REAIS de cada imagem do banco, no arquivo servido.

    python3 ferramentas/medir-imagens.py .            # so mede e mostra
    python3 ferramentas/medir-imagens.py . --gravar   # grava no banco

POR QUE ELE EXISTE, e a razao e uma so: o esquema do banco declara
`imagem.largura` e `imagem.altura` como inteiros desde que nasceu, e a fonte
legitima da foto — o feed de afiliado da Shopee, secao 25.3 do ARQUIPELAGO.md —
**nao declara dimensao nenhuma**. As tres imagens que chegaram em 13/09/2026
entraram sem os dois campos e o `validar-banco.py` reprovou, como devia.

Havia dois caminhos e um deles era ruim. O ruim era **afrouxar o esquema** para
aceitar dimensao ausente: os dois campos existem para a pagina reservar a caixa
da foto antes de ela chegar, e caixa sem medida e o salto de layout que a secao
22.4 chama de defeito de desempenho. O outro caminho era **medir**, e este
arquivo e ele — a nuvem alcanca `cf.shopee.com.br` (200 em duas passadas, medido
em 13/09/2026, como a 20.2 manda antes de declarar qualquer coisa sobre rede).

A DIFERENCA QUE ISSO FAZ, e ela e a regra desta fabrica: 800x800 lido do arquivo
servido e um DADO; 800x800 digitado porque "imagem de e-commerce costuma ser
quadrada" e um chute com cara de dado. O segundo passaria no validador igual.

COMO ELE LE, e por que nao usa biblioteca: o ambiente das rotinas nao tem Pillow,
e instalar uma dependencia para ler dois inteiros de um cabecalho seria trocar
uma linha de codigo por um risco de ambiente. Os tres formatos que um feed de
loja serve tem a dimensao no comeco do arquivo, em posicao fixa e documentada.

O QUE ELE NUNCA FAZ: inventar. Se o download falhar, se o formato nao for
reconhecido ou se os bytes acabarem no meio do cabecalho, o item fica **sem** os
dois campos e a linha sai como FALHOU — e o `validar-banco.py` continua
reprovando, que e o certo. Rede fechada nao vira numero.
"""

import json
import os
import struct
import subprocess
import sys


def baixar(url, tentativas=2):
    """Os bytes da imagem, ou None. Duas passadas, pela secao 20.2 do contrato:
    uma falha de rede so vira bloqueio depois de repetir na mesma execucao."""
    for _ in range(tentativas):
        r = subprocess.run(
            ["curl", "-s", "--max-time", "30", "-L", url],
            capture_output=True,
        )
        if r.returncode == 0 and len(r.stdout) > 64:
            return r.stdout
    return None


def dimensao(dados):
    """(largura, altura) lidas do cabecalho, ou None se nao der para ler."""
    if dados[:8] == b"\x89PNG\r\n\x1a\n" and dados[12:16] == b"IHDR":
        largura, altura = struct.unpack(">II", dados[16:24])
        return int(largura), int(altura)

    if dados[:2] == b"\xff\xd8":
        # JPEG: caminhar de marcador em marcador ate um SOF, que carrega as duas
        # dimensoes. Os SOF de 0xC4, 0xC8 e 0xCC NAO sao quadro: sao tabela de
        # Huffman, JPEG estendido e tabela aritmetica. Confundi-los e o erro
        # classico deste parser, e ele devolveria numero errado em silencio.
        i = 2
        fim = len(dados)
        while i + 9 < fim:
            if dados[i] != 0xFF:
                i += 1
                continue
            marcador = dados[i + 1]
            if marcador in (0xD8, 0x01) or 0xD0 <= marcador <= 0xD7:
                i += 2
                continue
            tamanho = struct.unpack(">H", dados[i + 2:i + 4])[0]
            if 0xC0 <= marcador <= 0xCF and marcador not in (0xC4, 0xC8, 0xCC):
                altura, largura = struct.unpack(">HH", dados[i + 5:i + 9])
                return int(largura), int(altura)
            i += 2 + tamanho
        return None

    if dados[:4] == b"RIFF" and dados[8:12] == b"WEBP":
        marca = dados[12:16]
        if marca == b"VP8X":
            largura = int.from_bytes(dados[24:27], "little") + 1
            altura = int.from_bytes(dados[27:30], "little") + 1
            return largura, altura
        if marca == b"VP8 ":
            return (struct.unpack("<H", dados[26:28])[0] & 0x3FFF,
                    struct.unpack("<H", dados[28:30])[0] & 0x3FFF)
        if marca == b"VP8L":
            bits = int.from_bytes(dados[21:25], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        return None

    return None


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    gravar = "--gravar" in sys.argv

    manifest = json.load(open(os.path.join(raiz, "manifest.json"), encoding="utf-8"))
    medidas, falhas, pulados = 0, 0, 0

    print("MEDINDO AS IMAGENS DO BANCO — largura e altura lidas do arquivo servido\n")

    for item in manifest.get("dados", []):
        caminho = os.path.join(raiz, item["arquivo"])
        # SO JSON: o manifest tambem indexa `.md` (corpus de buscas,
        # especificacao), e um `json.load` neles explodiria antes de medir a
        # primeira imagem. O filtro le o campo `formato` que o proprio manifest
        # declara, nunca a extensao do nome.
        if item.get("formato") != "json" or not os.path.exists(caminho):
            continue
        banco = json.load(open(caminho, encoding="utf-8"))
        lista = "materiais" if "materiais" in banco else ("itens" if "itens" in banco else "")
        if not lista:
            continue

        mexeu = False
        for registro in banco[lista]:
            imagem = registro.get("imagem")
            if not isinstance(imagem, dict) or not imagem.get("url"):
                continue
            if isinstance(imagem.get("largura"), int) and isinstance(imagem.get("altura"), int):
                pulados += 1
                continue

            dados = baixar(imagem["url"])
            lida = dimensao(dados) if dados else None
            if not lida:
                falhas += 1
                print("  FALHOU  %-42s %s" % (
                    registro["id"],
                    "download vazio" if not dados else "formato nao reconhecido"))
                continue

            largura, altura = lida
            print("  medida  %-42s %d x %d px" % (registro["id"], largura, altura))
            medidas += 1
            if gravar:
                # A ORDEM DOS CAMPOS SEGUE A DO ESQUEMA, para o diff do banco
                # ficar legivel: url, largura, altura, fonte, coletado_em, alt.
                nova = {"url": imagem["url"], "largura": largura, "altura": altura}
                for chave in ("fonte", "coletado_em", "alt"):
                    if chave in imagem:
                        nova[chave] = imagem[chave]
                for chave, valor in imagem.items():
                    if chave not in nova:
                        nova[chave] = valor
                registro["imagem"] = nova
                mexeu = True

        if mexeu:
            with open(caminho, "w", encoding="utf-8") as fh:
                json.dump(banco, fh, ensure_ascii=False, indent=2)
                fh.write("\n")

    print("\n%d medida(s), %d falha(s), %d ja tinham as duas%s" % (
        medidas, falhas, pulados, " (GRAVADO)" if gravar and medidas else ""))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
