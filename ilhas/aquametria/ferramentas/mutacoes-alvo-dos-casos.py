#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MUTACOES DELIBERADAS CONTRA O ALVO DOS CASOS do portao do banco de especies.

    python3 ferramentas/mutacoes-alvo-dos-casos.py

ESTE E O UNICO ARQUIVO DESTA ILHA QUE MUTILA O PORTAO E NAO O CODIGO. As outras
mutacoes afrouxam uma regra em `validar-especies.py` e exigem que
`testar-validador-especies.py` reprove. Aqui o mutante E o
`testar-validador-especies.py`: cada mutacao afrouxa UMA das duas travas que o
retrofit de 15/10/2026 pos nele — o `alvo` obrigatorio e a guarda da linha de
base — ou anula UMA corrupcao, e a rodada tem de REPROVAR com codigo de saida 1
e sem traceback.

POR QUE ELE EXISTE, E A CAUSA FOI MEDIDA E NAO SUPOSTA. Ate 15/10/2026 o
`alvo` era opcional e so 11 dos 51 casos o tinham. Sem ele o portao perguntava
apenas "a marca da regra apareceu na saida?" — e o banco LIMPO ja emite quatro
avisos de pe (E15 em poecilia-reticulata, E21 em symphysodon-aequifasciatus e em
apistogramma-agassizii, E25 em pethia-conchonius). Resultado medido naquele dia:
com as corrupcoes do E21 e do E15 **completamente anuladas**, o portao imprimiu
"pegou" nas duas e saiu com **codigo 0, 51 testes, 0 falhas**. Dois casos
aprovavam emprestando a linha de um vizinho, e nada acusava.

A FAMILIA E A MESMA DO ACHADO DA VESPERA no portao do `search-console.py`
("bloco ausente satisfazia o `not in` por acidente") e a mesma que fez duas
mutacoes do `mutacoes-porte-maximo.py` SOBREVIVEREM: APROVAR POR FALTA DE
EVIDENCIA. Portao que aceita a linha de qualquer registro nao mede o registro
que ele corrompeu.

UMA MUTACAO AQUI PODE PRECISAR DE DUAS EDICOES, e a secao 8 do ARQUIPELAGO.md
diz quando: a trava cujo mundo nao existe hoje so se mede com a mutacao que
**produz o mundo**. Tirar a exigencia do alvo nao quebra nada enquanto as 51
corrupcoes forem reais — e por isso a mutacao 7 tira a exigencia E anula a
corrupcao, reproduzindo inteiro o defeito medido em 15/10. Esta e a unica
mutacao de duas edicoes, e a segunda edicao e o mundo, nunca uma segunda regra.
"""
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTAO = "ferramentas/testar-validador-especies.py"


def troca(arquivo, pares, vezes=1):
    """Substituicoes exatas que RECUSAM operar se o alvo nao estiver la.

    E a trava contra a mutacao inerte: alvo que nao existe mais nao quebra nada e
    a mutacao passa por engano — 18 de 20 mutacoes desta ilha viraram inertes de
    uma vez em 11/09/2026, quando a bancada trocou de fonte.
    """
    def aplicar(base):
        caminho = os.path.join(base, arquivo)
        texto = open(caminho, encoding="utf-8").read()
        for de, para in pares:
            if texto.count(de) != vezes:
                raise SystemExit("MUTACAO INERTE: %r aparece %d vez(es) em %s, esperava %d"
                                 % (de, texto.count(de), arquivo, vezes))
            texto = texto.replace(de, para, vezes)
        open(caminho, "w", encoding="utf-8").write(texto)
    return aplicar


# as duas corrupcoes de `aviso` cujo vizinho a linha de base ja acusa, anuladas
ANULA_E21 = ("def c_e21_arranjo_acima_do_chao(b):",
             "def c_e21_arranjo_acima_do_chao(b):\n    return  # MUTACAO: corrupcao anulada")
ANULA_E15 = ("def c_e15(b):",
             "def c_e15(b):\n    return  # MUTACAO: corrupcao anulada")

MUTACOES = [
 ("1. o alvo de um caso e apagado",
  "a obrigatoriedade do alvo. Caso sem alvo nao diz que registro a corrupcao "
  "toca, e regra nao medida nao se distingue de regra que passa",
  troca(PORTAO, [('("E21", "arranjo publicado acima do chao declarado", c_e21_arranjo_acima_do_chao, "aviso",\n     "trichogaster-lalius"),',
                  '("E21", "arranjo publicado acima do chao declarado", c_e21_arranjo_acima_do_chao, "aviso"),')])),

 ("2. o alvo do E25 aponta para o registro que a linha de base ja acusa",
  "a guarda da linha de base. Com o alvo no pethia-conchonius, que o banco limpo "
  "ja acusa de pe, o caso aprovaria sem corrupcao nenhuma — alvo e tudo. E a "
  "metade que o alvo sozinho NAO alcanca",
  troca(PORTAO, [('("E25", "maximo e comum em reguas declaradas diferentes", c_e25_duas_reguas, "aviso",\n     "puntius-titteya"),',
                  '("E25", "maximo e comum em reguas declaradas diferentes", c_e25_duas_reguas, "aviso",\n     "pethia-conchonius"),')])),

 ("3. o alvo do E20 aponta para um vizinho que a MESMA regra acusa noutro caso",
  "que o alvo mede o REGISTRO e nao so a regra. O poecilia-reticulata e acusado "
  "pelo E20 no caso seguinte desta mesma lista, entao um alvo trocado entre dois "
  "casos da mesma regra e o erro mais facil de cometer relendo este arquivo",
  troca(PORTAO, [('("E20", "base dos dois lados sem chao_declarado_para", c_e20_sem_chao, "erro",\n     "apistogramma-agassizii"),',
                  '("E20", "base dos dois lados sem chao_declarado_para", c_e20_sem_chao, "erro",\n     "poecilia-reticulata"),')])),

 ("4. a corrupcao do E21 e anulada",
  "o alvo do caso que SOBREVIVIA. A linha de base tem dois `aviso [E21]`, e sem "
  "alvo este caso dizia 'pegou' com a corrupcao anulada. E a mutacao que mede o "
  "retrofit de 15/10 em pessoa",
  troca(PORTAO, [ANULA_E21])),

 ("5. a corrupcao do E15 e anulada",
  "o mesmo, no segundo registro: a linha de base tem `aviso [E15] "
  "poecilia-reticulata`, e a corrupcao anulada do corydoras-panda passava",
  troca(PORTAO, [ANULA_E15])),

 ("6. a corrupcao de um caso de ERRO e anulada (controle)",
  "o controle da familia: o E8 nao tem vizinho na linha de base, entao este caso "
  "ja reprovava ANTES do retrofit. Ele esta aqui para provar que anular uma "
  "corrupcao morde por si, e que o que as mutacoes 4 e 5 mediram foi o alvo",
  troca(PORTAO, [('def c_e8(b):',
                  'def c_e8(b):\n    return  # MUTACAO: corrupcao anulada')])),

 ("7. a afirmacao deixa de cobrar o REGISTRO e cobra so a regra, E a corrupcao do E21 e anulada",
  "a subtracao da linha de base, que e a trava ESTRUTURAL do retrofit. Esta "
  "mutacao SOBREVIVEU na primeira escrita de 15/10, quando a afirmacao era uma "
  "string montada ('ERRO  [E20] <alvo>:') procurada no texto: trocar a string "
  "pela marca pelada devolvia a brecha inteira. Com a afirmacao feita sobre as "
  "linhas NOVAS — medidas menos a linha de base —, a linha do vizinho nao pode "
  "satisfazer caso nenhum nem mesmo com a cobranca do registro afrouxada, porque "
  "ela foi subtraida antes. E a unica mutacao de duas edicoes, e a segunda PRODUZ "
  "o mundo (secao 8): afrouxar a cobranca nao quebra nada enquanto as 51 "
  "corrupcoes forem reais",
  troca(PORTAO, [('        pegou = procurada in novas',
                  '        pegou = any(r == regra for _, r, _ in novas)'),
                 ANULA_E21])),
]


def main():
    print("== mutacoes contra o alvo dos casos do portao de especies ==")
    falhas = []
    for titulo, porque, aplicar in MUTACOES:
        base = tempfile.mkdtemp(prefix="aqm-alvo-mut-")
        copia = os.path.join(base, "ilha")
        shutil.copytree(RAIZ, copia, symlinks=True,
                        ignore=shutil.ignore_patterns("node_modules", ".git", "__pycache__"))
        aplicar(copia)
        # sys.dont_write_bytecode no filho: a mutacao troca poucos caracteres e o
        # .pyc do original pode sobreviver a validacao de mtime + tamanho do
        # Python, que custou um diagnostico inteiro em 15/10/2026 no portao do
        # search-console.py.
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, os.path.join(copia, PORTAO)],
                           capture_output=True, text=True, cwd=copia, env=env)
        reprovou = r.returncode == 1
        limpo = "Traceback" not in (r.stdout + r.stderr)
        ok = reprovou and limpo
        print("  %-70s %s" % (titulo, "reprovou" if ok else "SOBREVIVEU"))
        if not ok:
            detalhe = "codigo de saida %d" % r.returncode
            if not limpo:
                detalhe += " e traceback (o portao morreu em vez de reprovar)"
            print("      %s" % detalhe)
            print("      para que a trava serve: %s" % porque)
            falhas.append(titulo)
        shutil.rmtree(base, ignore_errors=True)

    print("\n== resultado ==")
    print("  %d mutacao(oes), %d sobrevivente(s)" % (len(MUTACOES), len(falhas)))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
