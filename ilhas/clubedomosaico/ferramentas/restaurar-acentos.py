#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devolve os acentos as strings do banco que CHEGAM A TELA.

    python3 ferramentas/restaurar-acentos.py .            # so mostra
    python3 ferramentas/restaurar-acentos.py . --gravar   # aplica

POR QUE ISTO EXISTE. O bloco 4 publicou a primeira ferramenta da ilha e a
primeira coisa que o render de bancada mostrou foi "Silicone Acetico
Construcao" e "o fabricante declara ceramica e azulejo" — portugues errado,
vindo do banco, servido ao visitante e ao Google. O banco nasceu sem acento
porque foi digitado a partir de busca, e ate aqui ele so era lido por
ferramenta; no dia em que uma PAGINA passou a servi-lo, o defeito virou texto
no ar. A Robometria pagou exatamente isto em 11/09/2026, com 121 strings.

A OPERACAO E PROVADAMENTE DIACRITICO-ONLY, e e o `--provar` que garante:
reduzido a sem-diacritico, o banco depois desta ferramenta e byte a byte igual
ao banco antes dela. Sem essa prova, "restaurar acento" e uma porta aberta para
reescrever declaracao de fabricante — que e a unica coisa que este banco nao
pode deixar acontecer.

AS DUAS EXCECOES, declaradas aqui em vez de escondidas no mapa:
  1. `nome_comercial` dos cinco rejuntes vinha em CAIXA BAIXA ("rejunte
     acrilico quartzolit"), que nao e nome de produto, e virou nome proprio.
     Isso NAO e diacritico, entao esta na lista `CAIXA` e o --provar a
     desconsidera nomeadamente — uma por uma, nunca por regra geral.
  2. O "e" atono nao se resolve por palavra ("e" conjuncao e "e" verbo sao a
     mesma letra). As frases em que ele aparece estao em `FRASES`, inteiras.

O QUE A FERRAMENTA IMPRIME: cada troca que fez, com o campo e o id do produto.
Espelho que nao imprime o que trocou envelhece calado (secao 8 do contrato).
"""

import json
import os
import re
import sys
import unicodedata

CAMPOS_DE_TELA = ("marca", "fabricante", "nome_comercial")
LISTAS_DE_DECLARACAO = (
    "indicado_para", "nao_usar_em", "nao_recomendado_em",
    "nao_indicado_para", "ambientes_declarados", "resistencias_declaradas",
)

# Palavra sem acento -> palavra com acento. So palavras em que a forma acentuada
# e a UNICA leitura possivel em portugues; qualquer ambiguidade vai para FRASES.
PALAVRAS = {
    # AS DEZ DE 02/10/2026, quando a tupla ARQUIVOS passou a ver os cinco
    # bancos: foram as unicas, das 118 palavras que o aviso acusou, cuja forma
    # acentuada e a UNICA leitura possivel. As outras 108 nao precisam de
    # acento (selador, verniz, fosco, montagem), sao marca (Suvinil, Coral,
    # AkzoNobel), sao estrangeiras (fetch, egress, marketplace) ou sao codigo
    # (VDEC). Elas foram para `_CONHECIDAS`, uma a uma, porque aviso que grita
    # 118 palavras nao e aviso.
    "acrilica": "acrílica", "anuncio": "anúncio", "catalogo": "catálogo",
    "codigo": "código", "corroboracao": "corroboração",
    "execucao": "execução", "propria": "própria", "revisao": "revisão",
    "secao": "seção", "tres": "três",

    "acetico": "acético", "acidos": "ácidos", "acrilico": "acrílico",
    "agua": "água", "aluminio": "alumínio", "aquarios": "aquários",
    "area": "área", "areas": "áreas", "ate": "até",
    "calcario": "calcário", "ceramica": "cerâmica", "ceramicas": "cerâmicas",
    "ceramico": "cerâmico", "cimenticio": "cimentício", "condicao": "condição",
    "construcao": "construção", "cortica": "cortiça", "corrosivel": "corrosível",
    "corrosiveis": "corrosíveis", "dominio": "domínio", "encadernacao": "encadernação",
    "epoxi": "epóxi", "especiais": "especiais", "formula": "fórmula",
    "imersao": "imersão", "impermeavel": "impermeável", "latao": "latão",
    "liberacao": "liberação", "liquido": "líquido", "marmore": "mármore",
    "materia": "matéria", "media": "média", "mencao": "menção",
    "metalico": "metálico", "nao": "não", "pagina": "página",
    "papelao": "papelão", "plastico": "plástico", "plasticos": "plásticos",
    "proprio": "próprio", "resistencia": "resistência", "rodapes": "rodapés",
    "sao": "são", "sobreposicao": "sobreposição", "superficies": "superfícies",
    "tecnica": "técnica", "tecnico": "técnico", "variacao": "variação",
    "vedacao": "vedação",

    # AS QUARENTA E UMA DE 02/10/2026, NO BLOCO 4c — a frase do fabricante de
    # `acabamento` passou a ser servida inteira, e ate aqui ela nunca tinha
    # sido lida por ninguem alem de uma ferramenta. Cada uma entrou porque a
    # forma acentuada e a UNICA leitura possivel em portugues; o que apenas
    # PARECE faltar acento (acabado, pronto, total, secas, horizontais) ficou
    # de fora e esta em `_CONHECIDAS`.
    "acrilicas": "acrílicas", "aderencia": "aderência", "aplicacao": "aplicação",
    "apos": "após", "atraves": "através", "carvao": "carvão",
    "demao": "demão", "demaos": "demãos", "devera": "deverá",
    "diluicao": "diluição", "diluivel": "diluível", "emboco": "emboço",
    "formacao": "formação", "funcao": "função", "indispensavel": "indispensável",
    "infiltracoes": "infiltrações", "intemperies": "intempéries",
    "maquinas": "máquinas", "metalicas": "metálicas", "minimo": "mínimo",
    "molhaveis": "molháveis", "necessarias": "necessárias", "oleo": "óleo",
    "otima": "ótima", "papeis": "papéis", "pelicula": "película",
    "penetracao": "penetração", "poliester": "poliéster", "presenca": "presença",
    "pressao": "pressão", "protecao": "proteção", "rapida": "rápida",
    "realcando": "realçando", "residuos": "resíduos", "sera": "será",
    "superficie": "superfície", "trafego": "tráfego", "transito": "trânsito",
    "elasticas": "elásticas", "acao": "ação", "pos": "pós",

    # AS DUAS QUE O AVISO ACUSOU NO BANCO DOS VIZINHOS. Elas moram em
    # `propriedades.*.valor` da `alicate` e da `pastilha` — campo que passou a
    # ser de tela em 02/10/2026 —, e nenhuma pagina as serve HOJE. Entram
    # agora porque a categoria delas nasce depois e, quando nascer, a frase ja
    # esta certa: foi a ordem inversa que criou este arquivo.
    "flexivel": "flexível", "manutencao": "manutenção",
}

# Frases inteiras, para o que palavra nenhuma resolve.
FRASES = {
    "imersao continua em meio liquido": "imersão contínua em meio líquido",
    "material de imprensa do fabricante (2018) — NAO e ficha tecnica":
        "material de imprensa do fabricante (2018) — NÃO é ficha técnica",
    "materia do blog do proprio fabricante — e onde aparece a mencao a PASTILHAS entre os revestimentos, que o boletim nao trouxe":
        "matéria do blog do próprio fabricante — é onde aparece a menção a PASTILHAS entre os revestimentos, que o boletim não trouxe",
}

# Caixa alta de nome proprio. NAO e diacritico: cada uma esta escrita inteira,
# e o --provar as desconsidera nomeadamente.
CAIXA = {
    "rejunte acrilico quartzolit": "Rejunte Acrílico Quartzolit",
    "rejunte ceramicas quartzolit": "Rejunte Cerâmicas Quartzolit",
    "rejunte epoxi quartzolit": "Rejunte Epóxi Quartzolit",
    "rejunte piscinas quartzolit": "Rejunte Piscinas Quartzolit",
    "rejunte porcelanatos e ceramicas quartzolit": "Rejunte Porcelanatos e Cerâmicas Quartzolit",
}

# OS CINCO BANCOS, E ATE 02/10/2026 ESTA LINHA VIA DOIS.
#
# Defeito achado em 02/10/2026 pela execucao que coletou os tres acabamentos:
# esta tupla trazia so `materiais-colas` e `materiais-rejuntes`, os dois bancos
# que existiam no dia em que a ferramenta nasceu. Pastilhas, alicates e
# acabamento nasceram depois e NUNCA foram varridos — a ferramenta cujo motivo
# de existir e "o banco chega a tela e portugues errado no ar e defeito" nao
# olhava tres quintos do banco, e nada acusava, porque ela sempre fechava com
# "0 trocas" nos arquivos que ela via. E a mesma familia da mutacao inerte de
# 28/09: regua que nao alcanca aprova em silencio. O `--provar` continua sendo
# o que garante que o alcance maior nao virou reescrita de declaracao: ele
# roda sobre tudo que a tupla nomeia.
ARQUIVOS = ("materiais-colas.json", "materiais-rejuntes.json",
            "materiais-pastilhas.json", "materiais-alicates.json",
            "materiais-acabamento.json")


def sem_diacritico(texto):
    return "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))


def acentuar(texto):
    if texto in CAIXA:
        return CAIXA[texto]
    if texto in FRASES:
        return FRASES[texto]

    def troca(m):
        p = m.group(0)
        alvo = PALAVRAS.get(p.lower())
        if alvo is None:
            return p
        if p.isupper():
            return alvo.upper()
        if p[0].isupper():
            return alvo[0].upper() + alvo[1:]
        return alvo

    return re.sub(r"[A-Za-zÀ-ÿ]+", troca, texto)


def percorrer(material):
    """Devolve [(caminho, valor_atual, setter)] de tudo que chega a tela."""
    saida = []
    for campo in CAMPOS_DE_TELA:
        if isinstance(material.get(campo), str):
            saida.append((campo, material[campo],
                          lambda v, c=campo: material.__setitem__(c, v)))
    decl = material.get("declaracoes") or {}
    for lista in LISTAS_DE_DECLARACAO:
        valores = decl.get(lista)
        if not isinstance(valores, list):
            continue
        for i, v in enumerate(valores):
            if isinstance(v, str):
                saida.append(("declaracoes.%s[%d]" % (lista, i), v,
                              lambda nv, l=valores, j=i: l.__setitem__(j, nv)))
    # O OBJETO `protecao` E O VALOR DE TEXTO DAS PROPRIEDADES ENTRARAM EM
    # 02/10/2026, NO DIA EM QUE A PRIMEIRA PAGINA DO GUIA PASSOU A SERVI-LOS.
    #
    # E exatamente o caso que o cabecalho deste arquivo descreve: "o banco
    # nasceu sem acento porque foi digitado a partir de busca, e ate aqui ele
    # so era lido por ferramenta; no dia em que uma PAGINA passou a servi-lo, o
    # defeito virou texto no ar". A categoria `acabamento` guarda a declaracao
    # do fabricante em `protecao.literal_do_fabricante` — campo que nenhuma
    # outra categoria tem, criado em 25/09/2026 —, e o bloco 4c publica essa
    # frase inteira, entre aspas, em cada ficha de produto.
    #
    # O QUE FICOU DE FORA, E A REGRA E A MESMA DE SEMPRE: so entra campo que
    # CHEGA A TELA. O `declarado_como` de uma propriedade e a procedencia de um
    # numero e nenhuma pagina desta ilha o imprime — as paginas imprimem o
    # NUMERO, com a unidade, e o link da fonte. O `motivo` de propriedade nula
    # e prosa de execucao para a proxima passada ler. Nenhum dos dois e tela, e
    # acentuar o que nao e lido e alargar a superficie sem ganho.
    prot = material.get("protecao") or {}
    for campo in ("literal_do_fabricante", "trecho_que_declara_o_momento"):
        if isinstance(prot.get(campo), str):
            saida.append(("protecao.%s" % campo, prot[campo],
                          lambda v, c=campo, pr=prot: pr.__setitem__(c, v)))
    for nome_prop, prop in (material.get("propriedades") or {}).items():
        if isinstance(prop, dict) and isinstance(prop.get("valor"), str):
            saida.append(("propriedades.%s.valor" % nome_prop, prop["valor"],
                          lambda v, pp=prop: pp.__setitem__("valor", v)))
    for fid, fonte in (material.get("fontes") or {}).items():
        if isinstance(fonte.get("tipo"), str):
            saida.append(("fontes.%s.tipo" % fid, fonte["tipo"],
                          lambda v, f=fonte: f.__setitem__("tipo", v)))
    return saida


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    gravar = "--gravar" in sys.argv
    # O `--provar` E NOVO EM 02/10/2026, E ELE ERA PROMETIDO DESDE 11/09.
    #
    # O cabecalho deste arquivo diz, desde o dia em que ele nasceu, "A OPERACAO
    # E PROVADAMENTE DIACRITICO-ONLY, e e o `--provar` que garante". O codigo
    # nunca teve esse argumento: `sys.argv` era lido so para `--gravar`, e
    # `--provar` passava direto, ignorado em silencio, imprimindo o mesmo
    # relatorio e dando a impressao de ter provado. Achado em 02/10/2026 pela
    # execucao que AMPLIOU o alcance da ferramenta de dois bancos para cinco —
    # e e justamente essa prova que torna a ampliacao segura, porque o que ela
    # impede e "restaurar acento" virar reescrita de declaracao de fabricante.
    provar = "--provar" in sys.argv
    trocas = 0
    violacoes = []
    sem_mapa = set()

    for nome in ARQUIVOS:
        caminho = os.path.join(raiz, "dados", nome)
        with open(caminho, encoding="utf-8") as fh:
            dados = json.load(fh)

        for material in dados.get("materiais", []):
            for campo, valor, setter in percorrer(material):
                novo = acentuar(valor)
                if novo != valor:
                    trocas += 1
                    # A PROVA, nas duas excecoes NOMEADAS do cabecalho: CAIXA e
                    # FRASES mudam mais que diacritico de proposito (caixa alta
                    # em nome de produto), e por isso sao desconsideradas pelo
                    # nome, nunca por tolerancia de regra.
                    if (valor not in CAIXA and valor not in FRASES
                            and sem_diacritico(novo) != sem_diacritico(valor)):
                        violacoes.append((material["id"], campo, valor, novo))
                    print("  %-34s %-38s %s  ->  %s" % (material["id"], campo, valor, novo))
                    setter(novo)
                    valor = novo
                # PROVA: o que sobrou sem acento e palavra que o mapa nao conhece.
                for palavra in re.findall(r"[A-Za-zÀ-ÿ]+", valor):
                    if len(palavra) < 4 or palavra.lower() in ("para", "pdf"):
                        continue
                    if sem_diacritico(palavra) == palavra and palavra.lower() not in _CONHECIDAS:
                        sem_mapa.add(palavra.lower())

        if gravar:
            with open(caminho, "w", encoding="utf-8") as fh:
                json.dump(dados, fh, ensure_ascii=False, indent=2)
                fh.write("\n")

    print("\n  %d trocas%s" % (trocas, " GRAVADAS" if gravar else " (nada gravado; use --gravar)"))
    if sem_mapa:
        print("  palavras sem acento que o mapa nao conhece (confira uma a uma):")
        print("    " + ", ".join(sorted(sem_mapa)))
    if violacoes:
        print("\n  REPROVADO: %d troca(s) mudaram mais que diacritico e nao estao"
              " nas excecoes nomeadas:" % len(violacoes))
        for ident, campo, antes, depois in violacoes:
            print("    %s / %s: %r -> %r" % (ident, campo, antes, depois))
        return 1
    if provar:
        print("  PROVA: aprovada — reduzidas a sem-diacritico, as %d trocas sao"
              " byte a byte iguais as strings de antes (fora as excecoes"
              " nomeadas CAIXA e FRASES)." % trocas)
    return 0


# Palavras que EXISTEM sem acento em portugues e nao devem ser acusadas. A lista
# e explicita de proposito: o aviso so vale se ele nao gritar o tempo todo.
_CONHECIDAS = set("""
alcalinas algas alimento alta alvenaria ambiente ambientes anodizado antigo antimofo
aparece apresenta aramado assentamento azulejo baixa biocida blog boletim borracha
cimento cobre colagem comercial completamente compensado comum concreto contato
contra cortado couro decorativos densidade dele desta dias exija expandido externa
externo fabricante fachada ferro fibras fungos galvanizada gesso granito imprensa
industrial interna interno internos laminado laminados lido madeira manchas marca
material medida meio metais metal molduras molhada molhadas naturais neutro
outros ouro papel pastilhas pedra pedras pintadas piscinas piso pisos placa placas
polietileno policarbonato polipropileno poliestireno porcelana porcelanatos porosas
porosos prata produto protect quimicamente raios recomendado rejunte residencial
resistente revestimentos silicone sobre sobreposto submersa submersas submerso
sol tecido tecnologia tela temperado temperatura tijolo trouxe uso usado vento
vidro zinco cascola cascorez durepoxi extra extraforte formica formiplac henkel
loctite perstop quartzolit saint gobain tekbond weber argamassa cimentcola branca
esquadria natural revisada arquivo busca ajuda consumo exemplo publicados
aberto agentes algicida alguns aquecidas brsa celsius certos chapa chuva cola
entre especiais espelhos estrutural externas fechado ficha graus horas internas
onde paredes proteger tipos tratada materiais
aberta adesivo alimentos azulejista azulejos banheiros bebedouros brasil
brilhante bronze campo canal carregando civil cobertas consultas cortador
corte cozinhas cristal curvo declara declarada delas dentro diferentes
distribuidor distribuidora empresa entrada fachadas fosca fosco fundo
garagens geral importador importadora inclusive industriais institucional
interior lavabos lavanderias lida linha lisas loja ltda manual medido
mercado metalizado modernas montagem mosaico nenhuma nesta nunca passadas
pastilha pela produtos protetor reconferido resina restrita reto roldanas
saunas selador seladora sustenta tintas torques tradicionais valor varandas
verniz vitrificadas vitrines
acrilex acrilfix akzonobel coral cortag maxx pastilhart shopee suvinil vonder
blocked curl drywall egress fetch glass gourmet halls marketplace mosaic open
spas strip vdec
duas duro
ajuste allen cabos carbono chave forjado hexagonal plastificados tipo
acabado acabamento adequado aerossol agitado agitar aguardar aparente aplicado
aplicar apresentar aproximado argamassas artesanato ascendente aspecto
atingida aumentando base bonitos branco carros casa causadas cera
churrasqueiras cobertura como conjunto decorativo deixa dependendo depois
desde deseja desejada desenho destinado deve diluido diluir disperso diversas
documentos elevada enchimento especificada espessura espuma estar estruturas
expostos externos feita ferramentas fibrocimento final firme forem fotos
grande hidrofugante horizontais ideal impedir impermeabiliza impermeabilizante
indicada indicado intervalo isenta isopor laca lajes layouts leve limpa limpo
litro madeiras maior mais menor minerais minutos monocomponente muito negativa
nitrocelulose novas observado obter oferece pastel pelo permeabilidade pessoas
pigmentado pintura pinturas plantas pode poder possam preservar projeto pronta
pronto protege protegendo quaisquer quantas quanto quem realizada reboco
recomenda rende rendimento revestimento rolo seca secagem secas seco selagem
sempre sendo silano siloxano sistemas stains substrato substratos sujeitos
telhas teor textura texturacrill texturizado thinner tijolos tonalidade toque
total totalmente trabalho trabalhos transparente tratamento umidade uniformiza
uniformizar vernizes vista
""".split())


if __name__ == "__main__":
    sys.exit(main())
