#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra DE PROPOSITO a regua do espelho e exige que a bancada reprove.

    python3 ferramentas/mutacoes-cdn-shopee.py

O portao medido e `ferramentas/teste-cdn-shopee.py`; o codigo e
`ferramentas/regua-cdn-shopee.py`. Cada mutacao roda numa copia da pasta.

POR QUE ESTE ARQUIVO EXISTE: o `teste-cdn-shopee.py` nasceu VERDE na primeira
passada, e portao que nasce verde nao provou nada — foi escrito depois de a
regua ja ter sido experimentada a mao, entao passar era o esperado e nao era
evidencia. Quem diz se ele mede alguma coisa e esta lista.

AS PORTAS DOS FUNDOS QUE INTERESSAM NESTA REGUA sao as duas que devolvem um
NUMERO PLAUSIVEL em vez de um erro: trocar largura por altura numa ilha em que
toda foto e quadrada, e fazer o espelho perder a extensao — as duas passariam
despercebidas em producao por muito tempo.
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ILHA = Path(__file__).resolve().parent.parent
REGUA = 'ferramentas/regua-cdn-shopee.py'
PORTAO = 'ferramentas/teste-cdn-shopee.py'


def troca(arquivo, velho, novo):
    def aplicar(base: Path):
        p = base / arquivo
        s = p.read_text(encoding='utf-8')
        if velho not in s:
            raise SystemExit('ALVO SUMIU em %s: %r\n'
                             'Mutacao que nao encontra o alvo nao mede nada e '
                             'passaria por reprovada.' % (arquivo, velho[:70]))
        p.write_text(s.replace(velho, novo, 1), encoding='utf-8')
    return aplicar


MUTACOES = [
    # 1. O ESPELHO PERDE A REPRESENTACAO. E a porta dos fundos mais perigosa:
    #    o endereco sem extensao RESPONDE 200 e serve o JPEG, entao a coleta
    #    nao quebra — ela passa a medir o JPEG e a escrever o numero como se
    #    fosse do WebP que o visitante recebe.
    ('o espelho deixa de preservar a extensao',
     troca(REGUA,
           "    return 'https://%s/file/%s%s' % (HOST_ALCANCAVEL, id_do_arquivo(url), extensao(url))",
           "    return 'https://%s/file/%s' % (HOST_ALCANCAVEL, id_do_arquivo(url))")),

    # 2. HOST DESCONHECIDO PASSA A TER ESPELHO. Sem a recusa, qualquer URL vira
    #    um endereco no CDN da Shopee — que pode responder 200 servindo outra
    #    imagem.
    ('host fora do CDN deixa de ser recusado',
     troca(REGUA, "    if host not in HOSTS_DE_IMAGEM:",
           "    if False:")),

    # 3. LARGURA E ALTURA TROCADAS NO JPEG. Em ilha de foto quadrada isto nao
    #    aparece em lugar nenhum — nem na tela, nem no `/status`, nem na ronda.
    ('o JPEG troca largura por altura',
     troca(REGUA, "                altura, largura = struct.unpack('>HH', dados[i + 5:i + 9])",
           "                largura, altura = struct.unpack('>HH', dados[i + 5:i + 9])")),

    # 4. LARGURA E ALTURA TROCADAS NO PNG, que guarda na ordem inversa do JPEG.
    ('o PNG troca largura por altura',
     troca(REGUA, "        largura, altura = struct.unpack('>II', dados[16:24])",
           "        altura, largura = struct.unpack('>II', dados[16:24])")),

    # 5. O WEBP VP8X ESQUECE O +1. O formato guarda largura-1, e um erro de um
    #    pixel nunca seria visto por olho nenhum.
    ('o WebP VP8X perde o +1 da largura',
     troca(REGUA, "            return (int.from_bytes(dados[24:27], 'little') + 1,",
           "            return (int.from_bytes(dados[24:27], 'little'),")),

    # 6. O WEBP VP8 PERDE A MASCARA DE 14 BITS. Os dois bits altos sao a escala,
    #    nao a dimensao; sem a mascara a largura sai multiplicada as vezes.
    ('o WebP VP8 perde a mascara de 14 bits',
     troca(REGUA, "            return (struct.unpack('<H', dados[26:28])[0] & 0x3FFF,",
           "            return (struct.unpack('<H', dados[26:28])[0],")),

    # 7. O VP8L LE OS BITS NA ORDEM ERRADA — largura e altura sao 14 bits cada
    #    dentro do mesmo inteiro, e trocar o deslocamento troca os lados.
    ('o WebP VP8L troca os 14 bits de cada lado',
     troca(REGUA, "            return ((v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1)",
           "            return (((v >> 14) & 0x3FFF) + 1, (v & 0x3FFF) + 1)")),

    # 8. LIXO VIRA DIMENSAO. A pagina de erro do proxy comeca com `<`, e um
    #    leitor que devolvesse um par para ela encheria o banco de caixa errada.
    ('o que nao e imagem passa a devolver um par',
     troca(REGUA, "    if not dados:\n        return None",
           "    if not dados:\n        return (800, 800)")),

    # 9. A URL JA ALCANCAVEL VOLTA A SER ESPELHADA, virando `/file/file/<id>`.
    ('o espelho do espelho volta a ser montado',
     troca(REGUA, "    if host == HOST_ALCANCAVEL:\n        return url",
           "    if False:\n        return url")),

    # 10. A EXTENSAO DEIXA DE SER RECONHECIDA EM MAIUSCULA, e `FOTO.WEBP` vira
    #     um id com a extensao grudada — endereco que responde 404.
    ('a extensao maiuscula deixa de ser reconhecida',
     troca(REGUA, "    baixo = nome.lower()", "    baixo = nome")),

    # 11. A TENTATIVA UNICA. A 20.2 manda repetir antes de chamar de bloqueio;
    #     com uma so, uma intermitencia do tunel vira `motivo_sem_medida`
    #     escrito como se fosse diagnostico.
    ('a repeticao da secao 20.2 desaparece',
     troca(REGUA, "def medir_no_espelho(url, timeout=30, tentativas=3):",
           "def medir_no_espelho(url, timeout=30, tentativas=1):")),
]


def preparar(tmp: str) -> Path:
    destino = Path(tmp) / 'ilha'
    shutil.copytree(ILHA, destino, ignore=shutil.ignore_patterns('.git'))
    return destino


def main():
    # CONTROLE POSITIVO: o portao tem de estar VERDE na arvore real antes de
    # qualquer mutacao. Sem ele, um portao quebrado faria as 11 passarem por
    # reprovadas — que e o defeito que este arquivo existe para impedir nos
    # outros, e que ja aconteceu nesta ilha com `mutacoes-coleta-shopee.py`.
    r = subprocess.run([sys.executable, PORTAO], cwd=ILHA,
                       capture_output=True, text=True)
    if r.returncode != 0:
        print('CONTROLE POSITIVO FALHOU: o portao ja esta vermelho sem mutacao '
              'nenhuma. Nada abaixo mede coisa alguma.')
        print(r.stdout[-2000:])
        return 1
    print('controle positivo: portao verde na arvore real')

    sobreviventes = []
    for i, (nome, aplicar) in enumerate(MUTACOES, 1):
        with tempfile.TemporaryDirectory() as tmp:
            base = preparar(tmp)
            aplicar(base)
            r = subprocess.run([sys.executable, PORTAO], cwd=base,
                               capture_output=True, text=True)
            if r.returncode == 0:
                sobreviventes.append(nome)
                print('  %2d. SOBREVIVEU  %s' % (i, nome))
            else:
                print('  %2d. reprovada   %s' % (i, nome))

    print('\n%d mutacoes, %d reprovadas, %d sobreviventes'
          % (len(MUTACOES), len(MUTACOES) - len(sobreviventes), len(sobreviventes)))
    return 1 if sobreviventes else 0


if __name__ == '__main__':
    sys.exit(main())
