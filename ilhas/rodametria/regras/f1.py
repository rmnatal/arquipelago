#!/usr/bin/env python3
"""
F1 — "ESSE ELETRICO PRECISA DE CNH?" — A REFERENCIA.

Este arquivo e o CEREBRO da F1: entrada -> resposta inteira, ja em frase
acentuada. O snippet PHP que vai ao ar e TRADUTOR dele, frase a frase, como
regras/f2.py e snippets/rodametria-f2.php fazem nesta mesma ilha. O motivo esta
na secao 8 do ARQUIPELAGO.md: quem confere escreve a propria regua, e o que e
FATO EXTERNO mora num lugar so — aqui, dados/constantes.json e
dados/municipios.json, lidos e nunca digitados.

POR QUE ESTE ARQUIVO NASCE SO EM 06/11/2026, NOVE DIAS DEPOIS DA ILHA.
A arvore de decisao esta escrita desde 28/10 (secao 1.3 de
dados/especificacao-calculadoras.md) e nao dependia de fonte nenhuma; os
NUMEROS dependiam. A `limiares-categoria-contran-996-2023` ficou `pendente` com
valor null por nove dias, com cinco dominios oficiais em 403 de egresso medidos
em 28/10, 29/10 e 05/11, e a consequencia estava declarada sem maquiar: *a F1
nao vai ao ar*. Em 05/11, ~23h3x de Brasilia, o Raphael abriu o PDF oficial do
Ministerio dos Transportes no Chrome dele e a secao 5 de
dados/fonte-oficial-f1.md foi preenchida campo por campo. ESTE ARQUIVO E O QUE
A APOSTA DA 1.3 COMPROU: nenhuma linha de logica foi escrita duas vezes, porque
nenhum limiar jamais foi literal no codigo.

AS TRES COISAS QUE A LEITURA OFICIAL MUDOU NA ESPECIFICACAO, e as tres estao
aqui com o texto do artigo ao lado, porque a especificacao foi escrita em 28/10
a partir de fonte de segunda mao e o texto discorda dela em tres pontos:

  1. A ARVORE DA 1.3 TERMINAVA EM `senao -> ciclomotor`, E O TEXTO NAO
     AUTORIZA ISSO. O inciso IV do art. 2o poe TETO no ciclomotor (4 kW e
     50 km/h) e os paragrafos 6o e 7o mandam o que passa dos limites do
     autopropelido para "ciclomotor, motocicleta, motoneta ou triciclo,
     conforme o caso". Entao existe uma QUARTA saida, `acima_do_ciclomotor`, e
     ela diz que a resolucao NAO decide qual das tres. Chamar de ciclomotor um
     veiculo de 5 kW seria afirmar o que a resolucao nao diz — a proibicao
     nominal do VOZ.md — na ilha cujo produto E a categoria legal.

  2. A TABELA DA 1.2 DIZIA `dispensa CNH e dispensa placa` NAS TRES LINHAS, E A
     RESOLUCAO NAO FALA DE CNH. Ela nao tem um artigo sobre habilitacao: decide
     a CATEGORIA e decide PLACA, REGISTRO, LICENCIAMENTO (arts. 12 e 13) e
     CAPACETE (art. 19 V). A habilitacao vem do CTB, que esta ilha NAO leu em
     fonte oficial — e o planalto.gov.br esta atras da mesma parede de egresso.
     Entao a F1 responde a categoria, responde a placa com o artigo, e CALA
     sobre CNH nomeando a causa. A constante
     `exigencia-de-habilitacao-por-categoria-ctb` nasceu `pendente` para esse
     silencio ter nome, e a proibicao esta escrita nela: as frases "dispensa
     CNH" e "precisa de habilitacao" ficam proibidas na tela enquanto ela for
     pendente. O VOZ.md traz as duas nos exemplos aprovados, escritos em 27/10,
     ANTES de alguem ter lido a resolucao — e o mesmo VOZ.md proibe
     nominalmente "qualquer frase que afirme o que a resolucao nao diz". Onde os
     dois lados dele divergem, manda a proibicao: ela e sobre FONTE, e o exemplo
     era sobre TOM.

  3. AS QUATRO ENTRADAS DA 1.1 NAO BASTAM PARA FECHAR O AUTOPROPELIDO. A alinea
     e do inciso II poe largura de 70 cm e distancia entre eixos de 130 cm, e a
     F1 nao pergunta nenhuma das duas. Em vez de crescer o formulario (que
     custaria pixel no orcamento da 32.5, medido), o veredito `autopropelido`
     sai com a condicao DITA e os dois numeros impressos. Veredito condicionado
     e dito e honesto; veredito que esconde a condicao e o erro permissivo.

E A RECUSA MORA EM FUNCAO PURA, nunca dentro do laco que a calcula: e a regra
do "produza o mundo" da secao 8. `classificar()` recebe os tres numeros e os
limiares JA RESOLVIDOS e devolve a categoria ou a recusa com causa nomeada — a
bancada a chama direto, com limiar FICTICIO (ferramentas/teste-f1.py usa
LIMIAR_AUTOPROP_W = 777, declarado ficticio no proprio caso, pela 1.6 da
especificacao), e por isso nenhum caso de teste afirma 1.000 nem 32.
"""

import json
import os
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
ILHA = os.path.dirname(AQUI)   # regras/ fica na raiz da ilha; ver regras/LEIA.md

ID_LIMIARES = "limiares-categoria-contran-996-2023"
ID_CONSEQUENCIAS = "consequencias-por-categoria-contran-996-2023"
ID_HABILITACAO = "exigencia-de-habilitacao-por-categoria-ctb"

# Os nomes dos limiares, referenciados por nome e NUNCA por literal — a decisao
# de engenharia da 1.3. A lista existe aqui para o portao poder cobrar que a
# constante traga todos; os VALORES nao estao aqui e nao podem estar.
NOMES_DOS_LIMIARES = (
    "LIMIAR_BIKE_W",
    "LIMIAR_BIKE_KMH",
    "LIMIAR_AUTOPROP_W",
    "LIMIAR_AUTOPROP_KMH",
    "LIMIAR_AUTOPROP_LARGURA_MM",
    "LIMIAR_AUTOPROP_ENTRE_EIXOS_MM",
    "LIMIAR_CICLOMOTOR_W",
    "LIMIAR_CICLOMOTOR_KMH",
)

ACELERADORES = ("manual", "so_pedal_assistido", "nao_declarado")

CATEGORIAS = ("bicicleta_eletrica", "autopropelido", "ciclomotor",
              "acima_do_ciclomotor")

NOME_DA_CATEGORIA = {
    "bicicleta_eletrica": "bicicleta elétrica",
    "autopropelido": "equipamento de mobilidade individual autopropelido",
    "ciclomotor": "ciclomotor",
    "acima_do_ciclomotor": "acima do ciclomotor",
}

# O ARTIGO DEFINIDO DE CADA NOME, E ELE NASCE AQUI PORQUE O NOME NAO O ENTREGA
# (11/11/2026).
#
# O campo `placa` da tabela da regra e um PEDACO DE ORACAO — "nao e sujeita a
# registro, licenciamento nem placa" — e ele concorda com o sujeito de quem o
# usa. Na tabela o sujeito e a linha; na resposta de `FAQPage` da home o sujeito
# era `o veiculo`, masculino, e a home servia "o veiculo nao e SUJEITA", nas
# duas camadas, com a resposta seguinte dizendo "ele nao e SUJEITO" tres linhas
# abaixo. Medido no ar as 19h2xZ de 11/11/2026.
#
# O CONSERTO E DA FRASE E NAO DO DADO: a frase passa a nomear a categoria de que
# fala, e para isso ela precisa do artigo. Derivar genero da cadeia do nome
# seria chute (`equipamento` e masculino e `bicicleta` e feminino, e nada no
# texto diz isso), e trocar o campo `placa` para o masculino consertaria a
# resposta e quebraria a linha da tabela — que e o jeito de este defeito voltar
# pela outra ponta.
ARTIGO_DA_CATEGORIA = {
    "bicicleta_eletrica": "a",
    "autopropelido": "o",
    "ciclomotor": "o",
    "acima_do_ciclomotor": "o",
}


# --------------------------------------------------------------------------
# OS MOLDES DE FRASE, NUM LUGAR SO.
#
# A pagina responde em DOIS lugares: o HTML pre-renderizado (que o PHP serve e
# que a visao geral de IA le sem preencher formulario) e a recomputacao no
# navegador quando a pessoa troca um campo. Se cada metade escrevesse a propria
# frase, a pagina diria duas coisas para a mesma entrada e nenhum portao veria
# — a cicatriz da secao 8 ("as duas metades nunca se falavam"), paga nesta ilha
# na F2 em 29/10/2026.
#
# Entao o molde e FATO EXTERNO as duas metades: mora aqui, viaja inteiro para
# dados/f1-respostas.json, e o navegador o preenche. O que continua escrito
# duas vezes de proposito e a DECISAO — qual molde vale em cada mundo.
#
# NENHUM MOLDE TRAZ DIGITO. Todo numero entra por `{}`, do limiar lido ou da
# entrada da pessoa. Molde com digito e o numero de tela digitado com outra
# roupa, e o conferidor da vitrine desta ilha ja pegou essa familia uma vez.
# --------------------------------------------------------------------------

MOLDES = {
    # ---- o veredito, um por categoria ----
    "veredito_bicicleta_eletrica": (
        "É bicicleta elétrica: {w} W de potência nominal e {kmh} km/h, "
        "só com pedal assistido — os três dentro do que a resolução "
        "pede ({lim_w} W e {lim_kmh} km/h)."
    ),
    "veredito_autopropelido": (
        "É autopropelido: {w} W de potência nominal e {kmh} km/h, dentro dos "
        "{lim_w} W e {lim_kmh} km/h da resolução — e com acelerador, que "
        "aqui pode."
    ),
    # TRES MOLDES PARA O CICLOMOTOR, UM POR CAUSA DE ESTOURO, e a razao e um
    # defeito que o smoke test deste proprio arquivo pegou em 06/11/2026: o
    # molde unico dizia "{w} W passa dos {lim} W (...) OU {kmh} km/h passa dos
    # {lim} km/h", e para 1.000 W com 45 km/h ele servia "1.000 W passa dos
    # 1.000 W" — que e FALSO — ao lado da metade verdadeira. Frase com "ou" nao
    # e frase imprecisa: ela afirma as DUAS metades, e uma delas estava errada.
    # A causa que o codigo separa, o texto separa (secao 7).
    "veredito_ciclomotor_por_potencia": (
        "É ciclomotor: {w} W de potência nominal passam dos {lim_autoprop_w} W "
        "que o autopropelido permite, e ainda cabem no teto do ciclomotor, que é "
        "{lim_w} W e {lim_kmh} km/h."
    ),
    "veredito_ciclomotor_por_velocidade": (
        "É ciclomotor: {kmh} km/h passam dos {lim_autoprop_kmh} km/h que o "
        "autopropelido permite, e ainda cabem no teto do ciclomotor, que é "
        "{lim_w} W e {lim_kmh} km/h."
    ),
    "veredito_ciclomotor_por_dois": (
        "É ciclomotor: {w} W passam dos {lim_autoprop_w} W e {kmh} km/h passam dos "
        "{lim_autoprop_kmh} km/h que o autopropelido permite — e os dois ainda "
        "cabem no teto do ciclomotor, que é {lim_w} W e {lim_kmh} km/h."
    ),
    # E O MESMO DEFEITO DO CICLOMOTOR, UM ANDAR ACIMA: tres causas de estouro,
    # tres frases. Com 5.000 W e 40 km/h, o molde unico dizia "5.000 W e 40 km/h
    # ficam acima de 4.000 W e 50 km/h" — e os 40 km/h NAO ficam.
    "veredito_acima_por_potencia": (
        "Passa do ciclomotor: {w} W de potência nominal ficam acima dos {lim_w} W "
        "que é o teto dele."
    ),
    "veredito_acima_por_velocidade": (
        "Passa do ciclomotor: {kmh} km/h ficam acima dos {lim_kmh} km/h que é o "
        "teto dele."
    ),
    "veredito_acima_por_dois": (
        "Passa do ciclomotor nos dois números: {w} W ficam acima dos {lim_w} W e "
        "{kmh} km/h ficam acima dos {lim_kmh} km/h, que são os tetos dele."
    ),

    # ---- o que a resolucao diz que a categoria exige ----
    "placa_nao_sujeito": (
        "A resolução diz, no {artigo}, que não é sujeito a registro, a "
        "licenciamento nem a emplacamento para circular nas vias."
    ),
    "placa_exigido": (
        "Pede placa: a resolução manda registrar e licenciar ({artigo}), e "
        "cobra capacete."
    ),
    "placa_nao_decidido": (
        "E aqui a resolução para: o {artigo} manda classificar como ciclomotor, "
        "motocicleta, motoneta ou triciclo, conforme o caso — e não diz qual, "
        "nem o que cada um exige. Qualquer um dos quatro é veículo de placa."
    ),

    # ---- a metade que esta ilha NAO responde, e ela e dita ----
    "habilitacao_pendente": (
        "Sobre habilitação esta página não responde, e o motivo é um "
        "só: a resolução que decide a categoria não tem artigo nenhum "
        "sobre CNH. Quem decide isso é o Código de Trânsito, e a gente ainda "
        "não leu o Código de Trânsito na fonte oficial — então não "
        "vai dizer aqui que dispensa, nem que exige."
    ),

    # ---- OS TRES NUMEROS QUE CIRCULAM, e esta e a resposta que faltava a quem
    #      chegou tendo lido OUTRO numero.
    #
    # O primeiro levantamento desta ilha mediu, em 28/10/2026, que o eixo da CNH
    # esta tomado por portal de transito e por noticia, e que as fontes NAO
    # discordam de tom: discordam do NUMERO. Tres pares foram colhidos para a
    # mesma pergunta. A leitura oficial de 05/11 desfez a contradicao, e o que
    # ela mostrou nao foi "o nosso numero esta certo": foi que DOIS dos tres
    # estao na resolucao, para categorias diferentes, e o terceiro nao esta la.
    #
    # Sem estas frases a pagina serve o numero certo e PARECE errada para quem
    # chegou com o outro na cabeca — e quem chega com o outro na cabeca e o
    # publico inteiro desta consulta. Por isso elas sao o produto da ilha e nao
    # enfeite: o desacordo e o que a pagina existe para resolver.
    #
    # NENHUM DOS TRES MOLDES TRAZ DIGITO. Os dois primeiros sao preenchidos com
    # o limiar LIDO da resolucao; o terceiro, com o par da constante
    # `numero-que-circula-como-limite-nacional`, que e `afirmacao_de_terceiro` e
    # nunca limiar.
    "numeros_que_circulam_abertura": (
        "Procurando a resposta desta pergunta a gente achou três pares de "
        "números diferentes, em páginas que todas se apresentam como quem sabe. "
        "Depois de ler a resolução, dois deles estão lá — e são de categorias "
        "diferentes, por isso não competem."
    ),
    "numeros_que_circulam_os_dois_oficiais": (
        "{lim_autoprop_w} W com {lim_autoprop_kmh} km/h é o teto da bicicleta "
        "elétrica e do autopropelido. {lim_ciclo_w} W com {lim_ciclo_kmh} km/h é "
        "o teto do ciclomotor, que é a categoria logo acima. Quem cita um dos "
        "dois sem dizer de qual categoria está falando não está errado no "
        "número: está errado no que o número separa."
    ),
    "numeros_que_circulam_o_terceiro": (
        "O terceiro par, {w_circula} W com {kmh_circula} km/h, não está na "
        "resolução. Ele aparece atribuído a {atribuido_a} e é repetido como se "
        "fosse {apresentado_como}. A gente não leu o ato dessa prefeitura, "
        "então não diz aqui qual é o limite de lá. O que esta página afirma "
        "sobre ele é só isto: esse par não é o limite da resolução."
    ),

    # ---- as ressalvas, cada uma com o caso medido atras ----
    "ressalva_dimensao_autopropelido": (
        "Falta um pedaço que esta conta não pergunta: a resolução também "
        "limita o autopropelido a {largura_cm} cm de largura e {eixos_cm} cm entre os "
        "eixos. Se o seu passa de um dos dois, ele sai desta categoria mesmo com a "
        "potência e a velocidade dentro."
    ),
    # A PRIMEIRA VERSAO DESTE MOLDE DIZIA "costuma ser o de PICO", E O PORTAO DE
    # AR A REPROVOU NO MINUTO EM QUE ELA FOI AO AR — a classe do quantificador
    # por extenso, que esta ilha paga desde 03/11/2026. E o portao estava certo
    # por um motivo melhor do que o de estilo: "costuma" e uma afirmacao sobre
    # FREQUENCIA, e esta pagina TEM a frequencia medida. Trocar a hesitacao pelo
    # numero contado deixou a frase mais forte, nao mais fraca — e e exatamente
    # o que a 1.4(a) pede com produto na mao.
    #
    # Os tres numeros entram por `{}`, CONTADOS do banco pelo gerador. Sem eles a
    # ressalva NAO SAI: frase que cita uma contagem sem a contagem e o numero de
    # tela digitado esperando a vez.
    "ressalva_pico_nenhum_nominal": (
        "O número grande do anúncio não é o que a regra lê: ela lê a potência "
        "NOMINAL, que fica na ficha. Dos {colhidos} anúncios que a gente colheu, "
        "{sem_rotulo} declaram um watt sem dizer se é nominal ou de pico, e "
        "NENHUM declara o nominal. Um deles se chama, letra por letra, "
        "“{titulo}”: são quatro coisas que a regra separa, num título só."
    ),
    # DOIS MOLDES, UM POR MUNDO, e a causa e a mesma que a clubedomosaico pagou
    # em 12/10/2026: um molde so servia "e 0 declaram o nominal" — o plural que
    # mente, com o agravante de que o mundo de hoje e justamente o do zero. O
    # molde de baixo e o mundo em que o varejo passar a publicar o nominal, e ele
    # nasce agora porque e o dia em que alguem o le; nascer depois seria escreve-lo
    # com o dado na mao, e o portao o exercita FABRICANDO o mundo.
    "ressalva_pico_com_nominal": (
        "O número grande do anúncio não é o que a regra lê: ela lê a potência "
        "NOMINAL, que fica na ficha. Dos {colhidos} anúncios que a gente colheu, "
        "{sem_rotulo} declaram um watt sem dizer se é nominal ou de pico, e "
        "{com_nominal} declaram o nominal. Um deles se chama, letra por letra, "
        "“{titulo}”: são quatro coisas que a regra separa, num título só."
    ),
    "ressalva_alteracao": (
        "E a categoria sai da ficha de fábrica, nunca do velocímetro: uma "
        "scooter adulterada foi flagrada a {kmh_flagrado} km/h com {kmh_fabrica} km/h "
        "de fábrica declarados. Mexer depois da compra tira o veículo da "
        "categoria em que ele foi vendido."
    ),
    "ressalva_assistencia_a_pe": (
        "Um detalhe que muda a resposta: a resolução deixa a bicicleta "
        "elétrica ter um modo de empurrar a pé, sem pedalar, até "
        "{kmh_pe} km/h. Se o acelerador do seu só serve para isso, ele não é "
        "o acelerador que tira a bike da categoria dela."
    ),

    # ---- as recusas: cada causa com frase propria (secao 7) ----
    "recusa_acelerador": (
        "Sem saber do acelerador não dá para classificar, e ele não é "
        "detalhe: acelerador manual tira o veículo da bicicleta elétrica mesmo "
        "com a potência abaixo do limite, e o autopropelido pode ter acelerador. "
        "É o campo que decide, não o que completa."
    ),
    "recusa_potencia": (
        "Falta a potência NOMINAL em watts — a da ficha, não a do título. "
        "Sem ela não há o que comparar com o limite da resolução."
    ),
    "recusa_velocidade": (
        "Falta a velocidade máxima de fábrica em km/h. A resolução usa as "
        "duas coisas juntas: potência E velocidade."
    ),
    "recusa_limiar_pendente": (
        "A conta está de pé e os limites não: o texto oficial da "
        "resolução não foi lido ainda, e esta página não publica limite "
        "de potência tirado de notícia."
    ),
    "recusa_nao_positivo": (
        "Potência e velocidade têm de ser maiores que zero para a conta "
        "existir."
    ),

    # ---- camada 2: a rua e municipal. Sempre impressa (1.2) ----
    "municipal_generica": (
        "A categoria é nacional; a rua é municipal. Cidade nenhuma do nosso "
        "banco está com o ato lido ainda, então o que vale aqui é o aviso "
        "geral: prefeitura pode pôr limite próprio de velocidade e de "
        "potência, e já vimos notícia de duas fazendo isso. Antes de "
        "comprar, confira a regra da sua."
    ),
    "municipal_desconhecido": (
        "A categoria é nacional; a rua é municipal — e {municipio} não "
        "está no nosso banco. Prefeitura pode pôr limite próprio de "
        "velocidade e de potência, então confira a regra da sua antes de "
        "comprar."
    ),
    "municipal_conhecido_pendente": (
        "A categoria é nacional; a rua é municipal. {municipio} aparece com "
        "limite próprio nas nossas leituras, mas a gente ainda não leu o ato "
        "da prefeitura — então não publica o número. Confira na "
        "prefeitura."
    ),
    "municipal_conhecido": (
        "A categoria é nacional; a rua é municipal: {municipio} limita a "
        "{limite_kmh} km/h, pelo ato que a gente leu."
    ),

    # ---- A PRESTACAO DE CONTAS DA TABELA DO BANCO (09/11/2026) ----
    #
    # ESTA FRASE ESTAVA ESCRITA A MAO DENTRO DO SNIPPET, com os tres numeros
    # interpolados em PHP e o plural FIXO — e o que ela servia no ar, medido as
    # 13h4xZ de 09/11/2026 na home, era *"De 14 anuncios colhidos, 0 declaram a
    # potencia nominal e 0 DAO para classificar"*. Dois plurais que mentem na
    # mesma frase, e e a cicatriz exata que a clubedomosaico pagou em 12/10/2026
    # e que a `frase_do_rotulo` desta ilha pagou NO AR na manha de hoje ("1 dos 6
    # DECLARAM um watt").
    #
    # E E O PADRAO DA IRMA DIVERGENTE, que o fecho da passada anterior nomeou e
    # deixou sem regua: a `frase_do_rotulo` ganhou cinco formas e a concordancia
    # de verbo; esta, que afirma a MESMA familia de contagem na MESMA ilha, nao
    # tinha forma nenhuma. Duas metades contando a mesma coisa, a trava numa so.
    #
    # DOIS EIXOS INDEPENDENTES, TRES FORMAS CADA, e e por isso que o molde e
    # COMPOSTO em vez de enumerado: 3 x 3 seriam nove moldes literais, e molde
    # que nunca roda e molde que envelhece calado. O que se escolhe por contagem
    # e o PEDACO; o corpo e um so.
    "prestacao_da_tabela": (
        "De {total} anúncios colhidos, {nominal} e {classifica}. Esse é o "
        "tamanho real do problema, e é por isso que esta ferramenta pergunta os "
        "números a você em vez de prometer uma lista pronta."
    ),
    # O eixo do watt NOMINAL. No zero o numero SAI da frase: "0 declaram" e o
    # plural que mente, e "nenhum declara" e a mesma informacao em portugues.
    "prestacao_nominal_nenhum": "nenhum declara a potência nominal",
    "prestacao_nominal_um": "{com_nominal} declara a potência nominal",
    "prestacao_nominal_varios": "{com_nominal} declaram a potência nominal",
    # O eixo da CLASSIFICACAO, e o verbo dele e irregular ("da"/"dao"), que e
    # justamente o que o plural fixo nao alcanca.
    "prestacao_classifica_nenhum": "nenhum dá para classificar",
    "prestacao_classifica_um": "{classificaveis} dá para classificar",
    "prestacao_classifica_varios": "{classificaveis} dão para classificar",
}


def molde_da_prestacao_da_tabela(com_nominal, classificaveis):
    """O molde JA CONJUGADO da prestacao de contas da tabela do banco.

    Devolve o corpo com os dois pedacos escolhidos pela CONTAGEM e com os
    numeros ainda em `{}`: quem imprime (PHP) troca cada chave pelo numero
    dentro do `<span class="rdm-num">`, para o numero continuar em Mono sem que
    a FORMA da frase seja decidida em dois lugares. A forma e decidida AQUI, e
    so aqui.

    Existe por um defeito medido no ar as 13h4xZ de 09/11/2026 na home desta
    ilha: *"De 14 anuncios colhidos, 0 declaram a potencia nominal e 0 dao para
    classificar"*. Ver o comentario dos moldes `prestacao_*`.
    """
    nominal = ("prestacao_nominal_nenhum" if com_nominal == 0
               else "prestacao_nominal_um" if com_nominal == 1
               else "prestacao_nominal_varios")
    classifica = ("prestacao_classifica_nenhum" if classificaveis == 0
                  else "prestacao_classifica_um" if classificaveis == 1
                  else "prestacao_classifica_varios")
    return MOLDES["prestacao_da_tabela"].format(
        total="{total}",
        nominal=MOLDES[nominal],
        classifica=MOLDES[classifica])

# OS FATOS DAS RESSALVAS MORAM EM dados/constantes.json, E NAO AQUI — e a
# historia disso vale a linha, porque e o melhor que aconteceu nesta passada.
# Eles NASCERAM aqui, num dicionario chamado FATOS_DAS_RESSALVAS, e o PORTAO
# DESTA PROPRIA FERRAMENTA os expulsou na primeira vez que rodou: a regua da 1.3
# varre o codigo da referencia procurando literal numerico dos limiares, e o
# `32` do caso de alteracao bateu com o LIMIAR_AUTOPROP_KMH. A regra "fato
# externo mora num lugar so" estava escrita no CABECALHO DO ARQUIVO QUE A
# VIOLAVA, e nenhum olho a viu — viu o portao, que compara o codigo com a
# constante em vez de ler o codigo.
#
# A coincidencia dos dois `32` tambem e dado, e esta registrada na constante: o
# caso medido e de uma scooter vendida com 32 km/h de fabrica, ou seja NO TETO
# do autopropelido, e foi flagrada a 73.
#
# Os tres ids ficam nomeados aqui porque a RESSALVA e da ferramenta; os VALORES
# nao estao e nao podem estar.
ID_ASSISTENCIA_A_PE = "assistencia-a-pe-contran-996-2023"
ID_ALTERACAO = "alteracao-pos-compra-caso-medido"
ID_WATT_SEM_ROTULO = "watt-sem-rotulo-no-titulo-caso-medido"

# A AFIRMACAO DE TERCEIRO QUE A PAGINA CONTRADIZ. Ela NAO entra na arvore, nao e
# limiar e nao decide categoria nenhuma — e por isso ela mora numa constante de
# tipo `afirmacao_de_terceiro`, onde a regua do codigo nao a confunde com limiar.
# A regra `numero_de_portal_nunca_vira_constante_legal` de dados/constantes.json
# continua inteira: o que esta ilha publica deste numero e que ele NAO e o da
# resolucao.
ID_NUMERO_QUE_CIRCULA = "numero-que-circula-como-limite-nacional"


def carregar_json(nome):
    with open(os.path.join(ILHA, nome), encoding="utf-8") as f:
        return json.load(f)


def carregar_constantes(caminho=None):
    """Le dados/constantes.json e devolve {id: registro}."""
    caminho = caminho or os.path.join(ILHA, "dados", "constantes.json")
    with open(caminho, encoding="utf-8") as f:
        bruto = json.load(f)
    return {c["id"]: c for c in bruto["constantes"]}


def constante_publicavel(constantes, cid):
    """Devolve o valor SO se a constante estiver publicavel; senao None.

    O status e LIDO do arquivo. Nenhuma lista de pendencias e escrita dentro
    deste codigo, porque lista escrita a mao envelhece calada no dia em que a
    constante destrava — e foi exatamente o que aconteceu em 06/11/2026 com o
    limiar desta ferramenta.
    """
    c = constantes.get(cid)
    if not c or c.get("status") != "publicavel":
        return None
    return c.get("valor")


def limiares_publicaveis(constantes):
    """Os limiares, ou None se a constante nao estiver publicavel.

    Devolve dict com os NOMES_DOS_LIMIARES. Limiar faltando na constante
    publicavel e DENUNCIA e nunca valor por omissao: a arvore referencia por
    nome, e nome que nao existe tem de estourar aqui, nao devolver None la
    dentro e classificar errado.
    """
    valor = constante_publicavel(constantes, ID_LIMIARES)
    if valor is None:
        return None
    if not isinstance(valor, dict):
        raise ValueError("%s publicavel com valor que nao e objeto: %r" % (ID_LIMIARES, valor))
    faltam = [n for n in NOMES_DOS_LIMIARES if n not in valor]
    if faltam:
        raise ValueError("%s publicavel sem os limiares %s" % (ID_LIMIARES, ", ".join(faltam)))
    return {n: Fraction(str(valor[n])) for n in NOMES_DOS_LIMIARES}


def consequencias_publicaveis(constantes):
    """O que a resolucao exige por categoria, ou None se nao publicavel."""
    valor = constante_publicavel(constantes, ID_CONSEQUENCIAS)
    if valor is None:
        return None
    faltam = [c for c in CATEGORIAS if c not in valor]
    if faltam:
        raise ValueError("%s publicavel sem as categorias %s" % (ID_CONSEQUENCIAS, ", ".join(faltam)))
    return valor


def habilitacao_publicavel(constantes):
    """O veredito de habilitacao, ou None enquanto a constante for pendente.

    Enquanto for None a F1 CALA sobre CNH, com frase propria. Esta funcao existe
    para que o dia em que o CTB for lido nao exija mexer na logica: hoje ela
    devolve None e a pagina imprime `habilitacao_pendente`.
    """
    return constante_publicavel(constantes, ID_HABILITACAO)


def frases_dos_numeros_que_circulam(constantes, limiares):
    """As tres frases que nomeiam os tres numeros colhidos, ou [] se faltar base.

    POR QUE ESTA FUNCAO EXISTE E NAO TRES PARAGRAFOS NO SNIPPET: a mesma
    explicacao e pedida em DOIS lugares — a dobra da pagina e a pergunta do
    `FAQPage`. A 32.4-c do ARQUIPELAGO.md foi escrita nesta ilha, em 06/11/2026,
    por causa de uma resposta de `FAQPage` que era prosa escrita a mao e serviu,
    na camada que a IA le, os dois defeitos que a camada visivel ja tinha
    consertado meia hora antes. A licao dela e literal: *o conserto de uma frase
    duplicada nao e consertar as duas, e a segunda deixar de existir*.

    DEVOLVE LISTA VAZIA, NUNCA FRASE PELA METADE. Sem limiar publicavel nao ha
    os dois numeros oficiais para nomear, e sem a constante de terceiro nao ha o
    terceiro — e uma explicacao de "tres numeros" que nomeia dois e exatamente o
    defeito que ela veio consertar: a dobra desta pagina dizia "tres numeros
    diferentes" e explicava dois, sem nomear nenhum, desde que a F1 foi ao ar.
    """
    if limiares is None:
        return []
    circula = constante_publicavel(constantes, ID_NUMERO_QUE_CIRCULA)
    if not isinstance(circula, dict):
        return []
    faltam = [k for k in ("potencia_w", "velocidade_kmh", "atribuido_a",
                          "apresentado_como") if circula.get(k) in (None, "")]
    if faltam:
        raise ValueError(
            "%s publicavel sem %s: a frase dos tres numeros nao sai pela metade"
            % (ID_NUMERO_QUE_CIRCULA, ", ".join(faltam)))
    return [
        MOLDES["numeros_que_circulam_abertura"],
        MOLDES["numeros_que_circulam_os_dois_oficiais"].format(
            lim_autoprop_w=_n(limiares["LIMIAR_AUTOPROP_W"]),
            lim_autoprop_kmh=_n(limiares["LIMIAR_AUTOPROP_KMH"]),
            lim_ciclo_w=_n(limiares["LIMIAR_CICLOMOTOR_W"]),
            lim_ciclo_kmh=_n(limiares["LIMIAR_CICLOMOTOR_KMH"]),
        ),
        MOLDES["numeros_que_circulam_o_terceiro"].format(
            w_circula=_n(Fraction(str(circula["potencia_w"]))),
            kmh_circula=_n(Fraction(str(circula["velocidade_kmh"]))),
            atribuido_a=circula["atribuido_a"],
            apresentado_como=circula["apresentado_como"],
        ),
    ]


# --------------------------------------------------------------------------
# A ARVORE, EM FUNCAO PURA. Entra numero, sai categoria ou recusa com causa.
#
# Os limiares entram JA RESOLVIDOS, de proposito: e o que permite ao portao
# fabricar o mundo com limiar FICTICIO e afirmar a ARVORE em vez dos numeros do
# mundo (1.6 da especificacao). Nenhum literal numerico de limiar aparece
# abaixo desta linha.
# --------------------------------------------------------------------------

def classificar(potencia_nominal_w, velocidade_max_kmh, acelerador, limiares):
    """Devolve {'classifica': bool, 'categoria': str|None, 'causa': str|None}.

    Ordem das recusas, e ela e a ordem do que DECIDE:
      1. limiar pendente  -> nao existe regra para comparar
      2. acelerador       -> o pivo (1.1); `nao_declarado` NUNCA cai no lado
                             permissivo por omissao
      3. potencia nominal -> ausente e diferente de pico (1.4a)
      4. velocidade       -> a resolucao usa as duas juntas
    """
    if acelerador not in ACELERADORES and acelerador is not None:
        raise ValueError("acelerador desconhecido: %r" % (acelerador,))

    if limiares is None:
        return {"classifica": False, "categoria": None, "causa": "limiar_legal_pendente"}

    if acelerador is None or acelerador == "nao_declarado":
        return {"classifica": False, "categoria": None, "causa": "acelerador_nao_declarado"}

    if potencia_nominal_w is None:
        return {"classifica": False, "categoria": None, "causa": "potencia_nominal_ausente"}

    if velocidade_max_kmh is None:
        return {"classifica": False, "categoria": None, "causa": "velocidade_max_ausente"}

    w = Fraction(str(potencia_nominal_w))
    kmh = Fraction(str(velocidade_max_kmh))
    if w <= 0 or kmh <= 0:
        return {"classifica": False, "categoria": None, "causa": "entrada_nao_positiva"}

    if (acelerador == "so_pedal_assistido"
            and w <= limiares["LIMIAR_BIKE_W"]
            and kmh <= limiares["LIMIAR_BIKE_KMH"]):
        cat = "bicicleta_eletrica"
    elif (w <= limiares["LIMIAR_AUTOPROP_W"]
            and kmh <= limiares["LIMIAR_AUTOPROP_KMH"]):
        cat = "autopropelido"
    elif (w <= limiares["LIMIAR_CICLOMOTOR_W"]
            and kmh <= limiares["LIMIAR_CICLOMOTOR_KMH"]):
        cat = "ciclomotor"
    else:
        # A QUARTA SAIDA, que a especificacao nao previa. Ver o cabecalho deste
        # arquivo, achado 1: os paragrafos 6o e 7o do art. 2o mandam o excedente
        # para "ciclomotor, motocicleta, motoneta ou triciclo, conforme o caso",
        # e o inciso IV poe teto no ciclomotor. Dizer "ciclomotor" aqui seria
        # afirmar o que a resolucao nao diz.
        cat = "acima_do_ciclomotor"

    return {"classifica": True, "categoria": cat, "causa": None}


def _molde_do_estouro(estourou_w, estourou_kmh, so_w, so_kmh, os_dois):
    """Qual molde vale, pela CAUSA do estouro. Funcao pura, tres saidas.

    Chamada so onde a arvore ja decidiu que houve estouro, entao `nenhum dos
    dois` e impossivel por construcao — e a assercao esta aqui e nao num
    comentario, porque chamador novo que a viole tem de estourar e nao escolher
    uma frase por omissao.
    """
    assert estourou_w or estourou_kmh, (
        "_molde_do_estouro chamado sem estouro: a arvore e este molde "
        "discordam, e um dos dois esta errado")
    if estourou_w and estourou_kmh:
        return os_dois
    return so_w if estourou_w else so_kmh


def _n(fr, casas=0):
    """Numero em portugues: milhar com ponto, decimal com virgula."""
    if casas == 0:
        inteiro = int(fr + Fraction(1, 2)) if fr >= 0 else -int(-fr + Fraction(1, 2))
        return "{:,}".format(inteiro).replace(",", ".")
    q = Fraction(10) ** casas
    arred = int(fr * q + Fraction(1, 2)) / float(q)
    s = ("{:,.%df}" % casas).format(arred)
    return s.replace(",", "\x00").replace(".", ",").replace("\x00", ".")


def _mm_para_cm(mm):
    """Milimetro para centimetro, e o divisor e DEZ.

    A primeira versao desta funcao dividia por CEM, e a pagina foi ao ar dizendo
    que a resolucao limita o autopropelido a "7 cm de largura e 13 cm entre os
    eixos" — em vez de 70 e 130. Nenhum portao viu: a conversao estava certa como
    codigo (nao quebrava nada), e nenhuma regua sabia quanto tem de dar. Quem viu
    foi LER A FRASE GERADA, e e por isso que o gerador imprime a resposta de
    exemplo. O portao da ferramenta passou a cobrar a conversao contra a propria
    aritmetica, com a regua escrita do outro lado (cm x 10 == mm).
    """
    return _n(Fraction(str(mm)) / 10)


def camada_municipal(municipio, municipios):
    """A camada 2 da 1.2, SEMPRE impressa. Tres estados, tres frases.

    Devolve (chave_do_molde, campos). `municipios` e a lista de registros ja
    lida — fato externo num lugar so —, para a bancada fabricar o municipio com
    ato LIDO, que o banco de hoje nao tem (os quatro registros sao `pendente`).
    """
    nome = (municipio or "").strip()
    if not nome:
        return "municipal_generica", {}

    alvo = nome.lower()
    for m in municipios:
        nomes = {str(m.get("nome", "")).lower(), str(m.get("id", "")).lower()}
        if alvo in nomes:
            if m.get("status") == "publicavel" and m.get("limite_velocidade_kmh") is not None:
                return "municipal_conhecido", {
                    "municipio": m.get("nome"),
                    "limite_kmh": _n(Fraction(str(m["limite_velocidade_kmh"]))),
                }
            # Municipio no banco mas com o ato NAO LIDO. Esta frase e diferente
            # da generica de proposito: ela diz que a cidade esta na nossa mira
            # e que o numero existe e nao foi lido, o que e informacao. Fundi-la
            # com a generica apagaria a diferenca que o banco mediu.
            return "municipal_conhecido_pendente", {"municipio": m.get("nome")}
    return "municipal_desconhecido", {"municipio": nome}


def responder(potencia_nominal_w, velocidade_max_kmh, acelerador,
              municipio=None, constantes=None, municipios=None,
              contagem_de_fichas=None):
    """A resposta inteira da F1, ja em frases acentuadas.

    DUAS CAMADAS QUE NUNCA SE MISTURAM NUMA FRASE (1.2): a categoria nacional e
    a rua municipal saem em listas separadas, e quem monta a tela as poe em
    blocos com titulo proprio.
    """
    constantes = constantes if constantes is not None else carregar_constantes()
    if municipios is None:
        municipios = carregar_json("dados/municipios.json")["registros"]

    lim = limiares_publicaveis(constantes)
    cons = consequencias_publicaveis(constantes)
    hab = habilitacao_publicavel(constantes)
    # O titulo LITERAL do caso da 1.4(a), lido da constante. `None` quando ela
    # nao esta publicavel, e ai a ressalva simplesmente NAO sai.
    titulo = constante_publicavel(constantes, ID_WATT_SEM_ROTULO)
    # A CONTAGEM DO BANCO, que a ressalva do pico cita. Ela vem de FORA porque
    # quem conta e o gerador (e o navegador a recebe no pacote): a referencia nao
    # abre o banco de veiculos para responder a UMA pessoa. `None` faz a
    # ressalva nao sair, em vez de sair com a contagem de ninguem.
    tem_contagem = (titulo is not None and isinstance(contagem_de_fichas, dict)
                    and all(k in contagem_de_fichas
                            for k in ("colhidos", "sem_rotulo", "com_nominal")))
    def _ressalva_pico():
        chave = ("ressalva_pico_com_nominal"
                 if int(contagem_de_fichas["com_nominal"]) > 0
                 else "ressalva_pico_nenhum_nominal")
        return MOLDES[chave].format(
            titulo=titulo,
            colhidos=_n(Fraction(str(contagem_de_fichas["colhidos"]))),
            sem_rotulo=_n(Fraction(str(contagem_de_fichas["sem_rotulo"]))),
            com_nominal=_n(Fraction(str(contagem_de_fichas["com_nominal"]))))

    veredito = classificar(potencia_nominal_w, velocidade_max_kmh, acelerador, lim)

    frases_categoria = []
    frases_ressalva = []

    if veredito["classifica"]:
        cat = veredito["categoria"]
        w = Fraction(str(potencia_nominal_w))
        kmh = Fraction(str(velocidade_max_kmh))

        if cat == "bicicleta_eletrica":
            frases_categoria.append(MOLDES["veredito_bicicleta_eletrica"].format(
                w=_n(w), kmh=_n(kmh),
                lim_w=_n(lim["LIMIAR_BIKE_W"]), lim_kmh=_n(lim["LIMIAR_BIKE_KMH"])))
        elif cat == "autopropelido":
            frases_categoria.append(MOLDES["veredito_autopropelido"].format(
                w=_n(w), kmh=_n(kmh),
                lim_w=_n(lim["LIMIAR_AUTOPROP_W"]), lim_kmh=_n(lim["LIMIAR_AUTOPROP_KMH"])))
            frases_ressalva.append(MOLDES["ressalva_dimensao_autopropelido"].format(
                largura_cm=_mm_para_cm(lim["LIMIAR_AUTOPROP_LARGURA_MM"]),
                eixos_cm=_mm_para_cm(lim["LIMIAR_AUTOPROP_ENTRE_EIXOS_MM"])))
        elif cat == "ciclomotor":
            # QUAL DOS DOIS ESTOUROU, medido e nunca afirmado pelos dois ao
            # mesmo tempo. Ver o comentario dos tres moldes.
            molde = MOLDES[_molde_do_estouro(
                w > lim["LIMIAR_AUTOPROP_W"], kmh > lim["LIMIAR_AUTOPROP_KMH"],
                "veredito_ciclomotor_por_potencia",
                "veredito_ciclomotor_por_velocidade",
                "veredito_ciclomotor_por_dois")]
            frases_categoria.append(molde.format(
                w=_n(w), kmh=_n(kmh),
                lim_autoprop_w=_n(lim["LIMIAR_AUTOPROP_W"]),
                lim_autoprop_kmh=_n(lim["LIMIAR_AUTOPROP_KMH"]),
                lim_w=_n(lim["LIMIAR_CICLOMOTOR_W"]), lim_kmh=_n(lim["LIMIAR_CICLOMOTOR_KMH"])))
        else:
            molde = MOLDES[_molde_do_estouro(
                w > lim["LIMIAR_CICLOMOTOR_W"], kmh > lim["LIMIAR_CICLOMOTOR_KMH"],
                "veredito_acima_por_potencia",
                "veredito_acima_por_velocidade",
                "veredito_acima_por_dois")]
            frases_categoria.append(molde.format(
                w=_n(w), kmh=_n(kmh),
                lim_w=_n(lim["LIMIAR_CICLOMOTOR_W"]), lim_kmh=_n(lim["LIMIAR_CICLOMOTOR_KMH"])))

        # O que a resolucao diz que a categoria exige. Sai da CONSTANTE, nunca
        # de literal aqui: consequencia legal no codigo e a mesma doenca que
        # limiar no codigo.
        if cons is not None:
            c = cons[cat]
            exig = c.get("registro_licenciamento_emplacamento")
            if exig == "nao_sujeito":
                frases_categoria.append(MOLDES["placa_nao_sujeito"].format(artigo=c.get("artigo")))
            elif exig == "exigido":
                frases_categoria.append(MOLDES["placa_exigido"].format(artigo=c.get("artigo")))
            else:
                frases_categoria.append(MOLDES["placa_nao_decidido"].format(artigo=c.get("artigo")))

        # A METADE QUE ESTA ILHA NAO RESPONDE, E ELA E DITA NA CAMADA 1, junto
        # do veredito, e nao escondida no rodape: a pessoa chegou perguntando
        # exatamente isso.
        if hab is None:
            frases_categoria.append(MOLDES["habilitacao_pendente"])

        # As duas ressalvas obrigatorias da 1.4, mais a do paragrafo 4o quando
        # o acelerador e que decidiu tirar o veiculo da bicicleta eletrica.
        #
        # CADA UMA SO SAI SE A CONSTANTE QUE A SUSTENTA ESTIVER PUBLICAVEL.
        # Ressalva que cita um caso sem o caso e afirmacao sem fonte, e o
        # silencio aqui e a mesma disciplina do `constante_publicavel`: nenhuma
        # lista de pendencias escrita a mao.
        if tem_contagem:
            frases_ressalva.append(_ressalva_pico())
        if (acelerador == "manual" and lim is not None
                and Fraction(str(potencia_nominal_w)) <= lim["LIMIAR_BIKE_W"]
                and Fraction(str(velocidade_max_kmh)) <= lim["LIMIAR_BIKE_KMH"]):
            pe = constante_publicavel(constantes, ID_ASSISTENCIA_A_PE)
            if pe is not None:
                frases_ressalva.append(MOLDES["ressalva_assistencia_a_pe"].format(
                    kmh_pe=_n(Fraction(str(pe)))))
        alt = constante_publicavel(constantes, ID_ALTERACAO)
        if alt is not None:
            frases_ressalva.append(MOLDES["ressalva_alteracao"].format(
                kmh_flagrado=_n(Fraction(str(alt["kmh_flagrado"]))),
                kmh_fabrica=_n(Fraction(str(alt["kmh_fabrica"])))))
    else:
        causa = veredito["causa"]
        chave = {
            "limiar_legal_pendente": "recusa_limiar_pendente",
            "acelerador_nao_declarado": "recusa_acelerador",
            "potencia_nominal_ausente": "recusa_potencia",
            "velocidade_max_ausente": "recusa_velocidade",
            "entrada_nao_positiva": "recusa_nao_positivo",
        }[causa]
        frases_categoria.append(MOLDES[chave])
        # A ressalva do pico vale na recusa TAMBEM, e ali ela vale mais: quem
        # nao sabe qual watt tem e exatamente quem precisa saber onde olhar.
        if (causa in ("potencia_nominal_ausente", "acelerador_nao_declarado")
                and tem_contagem):
            frases_ressalva.append(_ressalva_pico())

    chave_mun, campos_mun = camada_municipal(municipio, municipios)
    frases_municipal = [MOLDES[chave_mun].format(**campos_mun)]

    return {
        "entrada": {
            "potencia_nominal_w": (None if potencia_nominal_w is None
                                   else float(potencia_nominal_w)),
            "velocidade_max_kmh": (None if velocidade_max_kmh is None
                                   else float(velocidade_max_kmh)),
            "acelerador": acelerador,
            "municipio": municipio or "",
        },
        "classifica": veredito["classifica"],
        "categoria": veredito["categoria"],
        "categoria_nome": (NOME_DA_CATEGORIA[veredito["categoria"]]
                           if veredito["categoria"] else None),
        "causa_da_recusa": veredito["causa"],
        "tom": _tom(veredito),
        "frases_categoria": frases_categoria,
        "frases_municipal": frases_municipal,
        "estado_municipal": chave_mun,
        "frases_ressalva": frases_ressalva,
        "habilitacao_respondida": hab is not None,
    }


def _tom(veredito):
    """O tom da caixa de resposta, que a casca usa para escolher a cor.

    O DESIGN.md desta ilha reserva o ambar (#8F4A00) para o aviso, e o VOZ.md e
    literal: *"o ambar so no aviso de 'precisa de CNH' ou 'nao aguenta'"*. Como
    a F1 NAO afirma CNH enquanto o CTB nao for lido, o ambar aqui marca a
    categoria que PEDE PLACA — que e a metade da pergunta que a resolucao
    responde. Tom nao e enfeite: ele e a unica coisa que uma pessoa com pressa
    le antes da frase.
    """
    if not veredito["classifica"]:
        return "neutro"
    if veredito["categoria"] in ("ciclomotor", "acima_do_ciclomotor"):
        return "alerta"
    # `verde` e nao `bom`: o vocabulario dos tres tons e o da casca
    # (`rodametria_casca_caixa` aceita verde, alerta e neutro e cai em neutro
    # silenciosamente no que nao reconhece). A primeira versao devolvia `bom`, e
    # o resultado seria uma caixa NEUTRA em toda resposta que libera — defeito
    # que nao quebra nada e so apaga a informacao, que e o tipo que vive mais.
    return "verde"


# --------------------------------------------------------------------------
# A PRESTACAO DE CONTAS DA SECAO 7, EM FUNCAO PURA SOBRE O BANCO JA LIDO.
#
# A regra da 1.7: TODO veiculo do banco aparece EXATAMENTE UMA VEZ, num grupo
# com nome proprio e por CAUSA, e a soma fecha o banco — contada, nunca
# digitada. Os grupos da 1.7 sao quatro; este arquivo acrescenta `fora_do_banco`
# pela mesma razao que regras/f2.py: registro `excluido_do_banco` nao e
# candidato e tambem nao pode desaparecer da conta.
#
# E O NUMERO QUE ESTA FUNCAO MEDE E A TESE DA ILHA: em 06/11/2026 ela devolve
# `nao_declaram_nominal` com 14 de 17 e `cabem_na_categoria` com ZERO, porque
# NENHUM dos 17 registros declara potencia nominal. A vitrine da F1 nasce vazia
# e a pagina diz por que, com os nomes contados.
# --------------------------------------------------------------------------

def _valor(campo):
    """Campo do banco: ou {'valor': x, ...} ou o valor cru."""
    if isinstance(campo, dict):
        return campo.get("valor")
    return campo


def grupos_de_compra(registros, categoria_pedida, limiares):
    """Agrupa os registros por CAUSA, para a prosa e para a vitrine da F1."""
    g = {
        "cabem_na_categoria": [],
        "de_outra_categoria": [],
        "nao_declaram_nominal": [],
        "sem_saida_de_compra": [],
        "fora_do_banco": [],
    }
    for r in registros:
        if r.get("status") == "excluido_do_banco":
            g["fora_do_banco"].append(r)
            continue

        w = _valor(r.get("potencia_nominal_w"))
        kmh = _valor(r.get("velocidade_max_kmh"))
        acel = _valor(r.get("acelerador"))
        v = classificar(w, kmh, acel, limiares)

        if not v["classifica"]:
            # TODAS as causas de nao-classificacao caem no mesmo grupo de prosa,
            # e o grupo tem nome proprio: o que falta e sempre um campo que a
            # FICHA nao declara, e a frase da pagina nomeia qual. Separar em
            # quatro grupos de uma linha cada diria menos, nao mais.
            g["nao_declaram_nominal"].append(r)
            continue

        tem_saida = bool(((r.get("afiliado") or {}).get("url_busca")
                          or (r.get("afiliado") or {}).get("url_produto")))
        if not tem_saida:
            g["sem_saida_de_compra"].append(r)
            continue

        if v["categoria"] == categoria_pedida:
            g["cabem_na_categoria"].append(r)
        else:
            g["de_outra_categoria"].append(r)

    soma = sum(len(x) for x in g.values())
    assert soma == len(registros), (
        "prestacao de contas furada: %d agrupados de %d recebidos" % (soma, len(registros)))
    return g


if __name__ == "__main__":
    cs = carregar_constantes()
    lim = limiares_publicaveis(cs)
    print("limiares publicaveis:", "SIM" if lim else "NAO (constante pendente)")
    casos = [
        (500, 25, "so_pedal_assistido", ""),
        (500, 25, "manual", "Campinas"),
        (1200, 45, "manual", ""),
        (5000, 80, "manual", "Osasco"),
        (500, 25, "nao_declarado", ""),
        (None, 25, "manual", ""),
    ]
    for c in casos:
        r = responder(*c, constantes=cs)
        print("--", c, "->", r["categoria"] or ("RECUSA: " + r["causa_da_recusa"]))
        for f in r["frases_categoria"]:
            print("   ", f)
        for f in r["frases_municipal"]:
            print("  m:", f)
