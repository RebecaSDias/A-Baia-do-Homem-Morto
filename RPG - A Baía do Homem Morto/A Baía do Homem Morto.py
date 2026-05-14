
import random
import time
import shutil
import re
import os
import pygame

#Aplicação da música no jogo.

def musicaprincipal():
    pygame.init()
    pygame.mixer.init()

    caminho_musica = os.path.join(os.path.dirname(__file__), "assets", "Tema.mp3")

    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

#Função para iniciar o jogo:

def iniciar_jogo():
    print("Jogo iniciado...")


#Cores ANSI - utilizadas

RESET      = '\033[0m'
vermelho   = '\033[91m'
verde      = '\033[92m'
amarelo    = '\033[93m'
azul       = '\033[94m'
roxo       = '\033[95m'
ciano      = '\033[96m'
branco     = '\033[97m'

vermelho_forte = '\033[31m'
verde_forte    = '\033[32m'
amarelo_forte  = '\033[33m'
azul_forte     = '\033[34m'
roxo_forte     = '\033[35m'
ciano_forte    = '\033[36m'

negrito    = '\033[1m'
sublinhado = '\033[4m'
invertido  = '\033[7m'

#Centralização

def _largura():
    return shutil.get_terminal_size((80, 20)).columns

def _limpar_ansi(texto):
    return re.compile(r'\x1b\[[0-9;]*m').sub('', texto)

def c(texto=""):
    """Imprime cada linha centralizada, respeitando códigos ANSI."""
    largura = _largura()
    for linha in texto.split("\n"):
        limpa = _limpar_ansi(linha)
        pad   = max(0, (largura - len(limpa)) // 2)
        print(" " * pad + linha)

def ci(prompt=""):
    """Input centralizado."""
    largura = _largura()
    limpa   = _limpar_ansi(prompt)
    pad     = max(0, (largura - len(limpa)) // 2)
    return input(" " * pad + prompt)


def c_ascii(texto):
    largura = shutil.get_terminal_size().columns
    ansi = re.compile(r'\x1b\[[0-9;]*m')

    linhas = texto.split("\n")
    largura_ascii = max(len(ansi.sub('', linha)) for linha in linhas)

    for linha in linhas:
        limpa = ansi.sub('', linha)
        espaco = (largura - largura_ascii) // 2
        print(" " * espaco + linha)

#ASCII usadas:

perola = """
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###########****++++====+*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######***+====--------=====+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######**++=---------------=====+#%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*#####**+=---:::::------------===+*%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%########**+=--::::-:::----------===+++#%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*####**+=---:::::::------------===++*#%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##***##**=----::::::::-------------=++**#%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##******+==-==---::::---------=---==++***#%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#******+=---#%#=-----------=-------=+*##**##%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*****++=---=@@##=--------===---::::-=+##*+++*#%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#***++++++==--%@@@+===--=--===----::::-=*#*+====*#%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#**++++++++==--+*+=--------=====----:::-+#*+=---==*%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++++++++====---::--------=======-----:-=**+=-----=*%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#**+++++++=====---------------=======------+*+==-----=*%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++++++======------------------=====-=----=*+=------=+#%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++++++====-==--------------------=====---==*++=-----==+##%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%#*++++===========--------------------=========*+==-----==+*##%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%*+++=============--------------------==+**===+**==-----===+**#%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%*++===========-=----------------------==+***+*+*++=-----====+**#%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%#*++=====-------------------:-::-------==+####*#*+==------===+++*#%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%#*+=====----------------::::::--:------=======-==------------==+*#%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%#*+====------------::::::::::::::-------------------:::::-----==*#%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%#*+=======--------------::::::::::-----------------------------==+#%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%*++**#***+++====-----------------------------------------------==+*#%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%*#%##%######**+++============--------------------------------=====+*#%%%%%%%
%%%%%%%%%%%%%%%%%%#%%%*##############**++++++++++=======--------------------------=====+=++*#%%%%%%%
%%%%%%%%%%%%%%%%###*##################**+++++++++++=====------------------------=======+++*##%%%%%%%
%%%%%%%%%%%%%%%#**########*###########**+++++=+++++=======--=--------------==========+++****%%%%%%%%
%%%%%%%%%%%%%#*+*###%##***###########**+++++==++==++=========--------------========++++***##%%%%%%%%
%%%%%%%%%%%%*+**###%#***############*+++++=====================------------========++++*##%%%%%%%%%%
%%%%%%%%%%#*+****#%**+*#**#####*###+++=============++=======--==-==-===-=======+====+++*###%%%%%%%%%
%%%%%%%%%#*=++**##****#*###*####***+=======+=====================--=======-===++====++*####%%%%%%%%%
%%%%%%%%%*++***###*#***###**#****++===============================-=-=========+===+=++*#%%%%%%%%%%%%
%%%%%%%%**++**##**##*##*###****#*+===========================================+====++**##%%%%%%%%%%%%
%%%%%%%*+****%***###*#**********+==========================================+====++++*#%%%%%%%%%%%%%%
%%%%%%*++***#=**##**************+========================-==-==================++***##%%%%%%%%%%%%%%
%%%%%#*+****+###***************+++=========================-=-======-===-=======++**##%%%%%%%%%%%%%%
%%%%%#++********++******#******+==========================-=-=---==-===-==-====+++*###%%%%%%%%%%%%%%
%%%%%++*+*#***************++*#++++=======================-==-----=======---=-=+++***##%%%%%%%%%%%%%%
%%%%*+*++%#**+************+*##++++++=========================--===========--==++****##%%%%%%%%%%%%%%
%%%%+*++#%++***##*****#****##***++++====+=================--=-================++****###%%%%%%%%%%%%%
%%%#**+##+++**##+******+**##**##+++===+++++++================================+++****####%%%%%%%%%%%%
%%%*++%*+*++**#++********#*++**++=====+++++++=+++=+======================-===+++++***###%%%%%%%%%%%%
%%#=+##+*+***#*++******+++++*++=======++=++++++++==++========================-=++******#%%%%%%%%%%%%⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀
Jogo feito por Rebeca Sirio Dias.
Supervisionado por um casal de papagaios raivosos, Pérola e Pequirito.

Agradecimentos a Professora Érica Lopes.

 """

titulo = """

                                 ____
                          __    |::::`*.
                     .-*``      |::::_.' _                    :
                                 ````     ``~.
          \ |   .'                                            .
       `. __  /                                 `~_
       _ /;O`. .'                                             :
        /\/`.o) _                                   `.
       /\/  //                                              . .
      /\/  //  \                       .          `   .       :  .-.
     /\/  //                            `.             :      '          .
    /\/  //                                         .   .            : .::
   /\/  :/                                  `.     :  . :  .  :      : ;'           .
_ /\/  /\\                                `          :: `   : :       `  ;       .
\'\/._/9 ))                               .     .    `". :  : .   ;     `       `
 )/  .( //                               ::              : .  :     :        .`
'..  ::':`-.___                           `       `.      : : : :" :  -. ;  `             ::
   `.`:::::::)#)                              :       " :`:"` :;;` : :: '.`               _.
     `.``:::/#/                                `   : `. "; ';`: ;;:"`   `.          .-` `
       `-**/#/                            :--.. _   " ::.`;:':`::':.;.`; :    .-`     :
     (\(\`~~`                      '       `     `` -._;.`::`.::.:"::.:_'. `` .   ;         :
     (._.)/            ,          .       ,           ": :::.:;;.;'.;;: " :" : .          ,  `
     (___)                    , . `  . :: , _ . _ ;"_:_"::.;;;`::"::;'_`;"_`._; __: _  .   -  .
  ````````````````````````````````````````````""""***---;;;;;;;;;;;;;;;;;;---***""""```````rscr
------------------------------------------------

 _____    _____     _          _        _____                        _____         _
|  _  |  | __  |___|_|___    _| |___   |  |  |___ _____ ___ _____   |     |___ ___| |_ ___
|     |  | __ -| .'| | .'|  | . | . |  |     | . |     | -_|     |  | | | | . |  _|  _| . |_
|__|__|  |_____|__,|_|__,|  |___|___|  |__|__|___|_|_|_|___|_|_|_|  |_|_|_|___|_| |_| |___|_|

"""

menu = """
  ╔───────────────────╗
  │ 1. Iniciar Jogo.  │
  │ 2. Ver classes.   │
  │ 3. Créditos.      │
  │ 4. Sair.          │
  ╚───────────────────╝
"""

#Custo de STAMINA:
#Stamina é consumida em combate e regenerada ao defender/usar item
#Crítico não custa extra, é recompensa por dano certo, defesa gera um pouco de stamina.

CUSTO_ATAQUE_NORMAL   = 10
CUSTO_ATAQUE_CRITICO  = 0
CUSTO_DEFENDER        = 5
REGENERACAO_DEFENDER  = 8

#Falas Pérola separadas por classe: inimigo comum, e boss.

falas_perola = [
    "𓅪 Pérola: Esse aí parece fraco!",
    "𓅪 Pérola: Cuidado!",
    "𓅪 Pérola: Ataca logo!",
    "𓅪 Pérola: EU FAÇO MELHOR!",
    "𓅪 Pérola: @#$%! SOCORRO!",
    "𓅪 Pérola: Vamos acabar com ele!"
]

falas_perola_boss = [
    "𓅪 Pérola: Que querido, neh?",
    "𓅪 Pérola: ADEUS!",
    "𓅪 Pérola: Já lutei contra piores, acho.",
    "𓅪 Pérola: Tudo bem fih?",
    "𓅪 Pérola: @#$%!*",
    "𓅪 Pérola: Sinto cheiro de problema."
]

def perola_fala(jogador):
    if hasattr(jogador, "inventario") and "Pérola 𓅪" in jogador.inventario:
        if random.random() < 0.4:
            c(ciano + random.choice(falas_perola) + RESET)

def perola_boss(jogador):
    if hasattr(jogador, "inventario") and "Pérola 𓅪" in jogador.inventario:
        c(ciano + random.choice(falas_perola_boss) + RESET)
        time.sleep(1)

def interagir_com_perola(jogador):
    if "Pérola 𓅪" not in jogador.inventario:
        c(vermelho + "⚠︎ Você não tem a Pérola no inventário." + RESET)
        return

    contador = getattr(jogador, "_perola_interacoes", 0) + 1
    jogador._perola_interacoes = contador

    if contador == 1:
        c(ciano + '𓅪 Pérola te olha de lado. "Tá me encarando, seu idiota?"' + RESET)
    elif contador == 2:
        c(ciano + "𓅪 ...Para com isso. Tô de olho em você." + RESET)
        c(ciano + "Pérola parece levemente irritada." + RESET)
    elif contador >= 3:
        jogador._perola_interacoes = 0
        c(ciano + '𓅪 "JÁ CHEGA! VOU ARRANCAR SUA ORELHA, SEU PALHAÇO!"' + RESET)
        time.sleep(0.8)
        c(vermelho + "˗ˏˋ Pérola te bica com força total! ˎˊ-" + RESET)
        c(" ")
        c(amarelo + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
        c(amarelo + "✮⋆˙ Easter Egg: A vingança da Pérola!" + RESET)
        c(amarelo + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
        jogador.vida = max(0, jogador.vida - 5)
        c(vermelho + f"𖦹 -5 de vida! Vida atual: {jogador.vida}/{jogador.vida_maxima}" + RESET)
        c(ciano + '𓅪 "Agora você aprendeu. RESPEITO. ARRR!"' + RESET)
        time.sleep(1)

#Armas por classe:

ARMAS_POR_CLASSE = {
    "Atirador": [
        {"nivel": 1,   "nome": "Pistola Enferrujada",    "bonus_dano": 0,    "tier": "Comum",    "preco_venda": 5},
        {"nivel": 5,   "nome": "Pistola do Corsário",    "bonus_dano": 5,    "tier": "Incomum",  "preco_venda": 25},
        {"nivel": 10,  "nome": "Pistola Dupla",          "bonus_dano": 10,   "tier": "Raro",     "preco_venda": 60},
        {"nivel": 15,  "nome": "Rifle Naval",            "bonus_dano": 18,   "tier": "Épico",    "preco_venda": 110},
        {"nivel": 20,  "nome": "Rifle de Elite",         "bonus_dano": 28,   "tier": "Lendário", "preco_venda": 175},
        {"nivel": 25,  "nome": "Canhão Portátil",        "bonus_dano": 40,   "tier": "Único",    "preco_venda": 260},
    ],
    "Corsário": [
        {"nivel": 1,   "nome": "Espada Curta",           "bonus_dano": 0,    "tier": "Comum",    "preco_venda": 5},
        {"nivel": 5,   "nome": "Sabre do Corsário",      "bonus_dano": 5,    "tier": "Incomum",  "preco_venda": 25},
        {"nivel": 10,  "nome": "Espada Naval",           "bonus_dano": 10,   "tier": "Raro",     "preco_venda": 60},
        {"nivel": 15,  "nome": "Lâmina do Capitão",      "bonus_dano": 18,   "tier": "Épico",    "preco_venda": 110},
        {"nivel": 20,  "nome": "Espada Lendária",        "bonus_dano": 28,   "tier": "Lendário", "preco_venda": 175},
        {"nivel": 25,  "nome": "Lâmina dos Condenados",  "bonus_dano": 40,   "tier": "Único",    "preco_venda": 260},
    ],
    "Bombardeiro": [
        {"nivel": 1,   "nome": "Bombas Improvisadas",    "bonus_dano": 0,    "tier": "Comum",    "preco_venda": 5},
        {"nivel": 5,   "nome": "Barril Explosivo",       "bonus_dano": 5,    "tier": "Incomum",  "preco_venda": 25},
        {"nivel": 10,  "nome": "Granada Pirata",         "bonus_dano": 10,   "tier": "Raro",     "preco_venda": 60},
        {"nivel": 15,  "nome": "Lançador de Bombas",     "bonus_dano": 18,   "tier": "Épico",    "preco_venda": 110},
        {"nivel": 20,  "nome": "Canhão de Ombro",        "bonus_dano": 28,   "tier": "Lendário", "preco_venda": 175},
        {"nivel": 25,  "nome": "Arsenal Explosivo",      "bonus_dano": 40,   "tier": "Único",    "preco_venda": 260},
    ],
    "Pactuário": [
        {"nivel": 1,   "nome": "Grimório Sombrio",       "bonus_dano": 0,    "tier": "Comum",    "preco_venda": 5},
        {"nivel": 5,   "nome": "Orbe Amaldiçoado",       "bonus_dano": 5,    "tier": "Incomum",  "preco_venda": 25},
        {"nivel": 10,  "nome": "Cajado Sombrio",         "bonus_dano": 10,   "tier": "Raro",     "preco_venda": 60},
        {"nivel": 15,  "nome": "Tomo Proibido",          "bonus_dano": 18,   "tier": "Épico",    "preco_venda": 110},
        {"nivel": 20,  "nome": "Cajado do Abismo",       "bonus_dano": 28,   "tier": "Lendário", "preco_venda": 175},
        {"nivel": 25,  "nome": "Relíquia do Abismo",     "bonus_dano": 40,   "tier": "Único",    "preco_venda": 260},
    ],
    "Pesquisador": [
        {"nivel": 1,   "nome": "Adaga Antiga",           "bonus_dano": 0,    "tier": "Comum",    "preco_venda": 5},
        {"nivel": 5,   "nome": "Lâmina Curta",           "bonus_dano": 5,    "tier": "Incomum",  "preco_venda": 25},
        {"nivel": 10,  "nome": "Adaga Rúnica",           "bonus_dano": 10,   "tier": "Raro",     "preco_venda": 60},
        {"nivel": 15,  "nome": "Lâmina do Conhecimento", "bonus_dano": 18,   "tier": "Épico",    "preco_venda": 110},
        {"nivel": 20,  "nome": "Arma Experimental",      "bonus_dano": 28,   "tier": "Lendário", "preco_venda": 175},
        {"nivel": 25,  "nome": "Artefato Antigo",        "bonus_dano": 40,   "tier": "Único",    "preco_venda": 260},
    ],
    "Espadachim": [
        {"nivel": 1,   "nome": "Espada Curta",           "bonus_dano": 0,    "tier": "Comum",    "preco_venda": 5},
        {"nivel": 5,   "nome": "Sabre Rápido",           "bonus_dano": 5,    "tier": "Incomum",  "preco_venda": 25},
        {"nivel": 10,  "nome": "Espada Balanceada",      "bonus_dano": 10,   "tier": "Raro",     "preco_venda": 60},
        {"nivel": 15,  "nome": "Lâmina Rápida",          "bonus_dano": 18,   "tier": "Épico",    "preco_venda": 110},
        {"nivel": 20,  "nome": "Espada Mestre",          "bonus_dano": 28,   "tier": "Lendário", "preco_venda": 175},
        {"nivel": 25,  "nome": "Lâmina Fantasma",        "bonus_dano": 40,   "tier": "Único",    "preco_venda": 260},
    ],
}

TIER_EMOJI = {
    "Comum":    "⚪",
    "Incomum":  "🟢",
    "Raro":     "🔵",
    "Épico":    "🟣",
    "Lendário": "🟠",
    "Único":    "🌟",
}

#LOJA - ITENS DE CURA

ITENS_CURA = {
    "Pequena Poção de Vida": {
        "descricao": "Recupera 20 pontos de vida.",
        "vida": 20,  "stamina": 0,  "cura_total": False, "preco": 15
    },
    "Poção de Vida": {
        "descricao": "Recupera 50 pontos de vida.",
        "vida": 50,  "stamina": 0,  "cura_total": False, "preco": 35
    },
    "Grande Poção de Vida": {
        "descricao": "Recupera 100 pontos de vida.",
        "vida": 100, "stamina": 0,  "cura_total": False, "preco": 50
    },
    "Kit Médico": {
        "descricao": "Recupera 75 de vida. Versão de combate do curandeiro.",
        "vida": 75,  "stamina": 0,  "cura_total": False, "preco": 45
    },
    "Rum do Pirata": {
        "descricao": "Recupera 30 de vida e 30 de stamina. Nada como um bom rum!",
        "vida": 30,  "stamina": 30, "cura_total": False, "preco": 20
    },
    "Elixir Antigo": {
        "descricao": "Restaura toda a vida e stamina. Raro e valioso.",
        "vida": 0,   "stamina": 0,  "cura_total": True,  "preco": 100
    },
}

ITENS_PACTUARIO = {
    "Fragmento Sombrio": {
        "descricao": "Recupera 30 de stamina mágica.",
        "stamina": 30, "bonus_dano": 0,  "buff_turnos": 0, "preco": 25
    },
    "Essência do Abismo": {
        "descricao": "Aumenta dano mágico em +15 por 3 turnos.",
        "stamina": 0,  "bonus_dano": 15, "buff_turnos": 3, "preco": 40
    },
    "Grimório Antigo": {
        "descricao": "Aumenta stamina mágica em +20 permanentemente.",
        "stamina": 20, "bonus_dano": 0,  "buff_turnos": 0, "preco": 30
    },
    "Cristal Amaldiçoado": {
        "descricao": "Recupera 40 de stamina mágica.",
        "stamina": 40, "bonus_dano": 0,  "buff_turnos": 0, "preco": 35
    },
    "Relíquia Sombria": {
        "descricao": "Buff temporário: +20 de dano por 2 turnos.",
        "stamina": 0,  "bonus_dano": 20, "buff_turnos": 2, "preco": 55
    },
    "Cartas Ciganas": {
        "descricao": "Recupera 60 de vida e 40 de stamina mágica.",
        "stamina": 40, "bonus_dano": 0,  "buff_turnos": 0, "preco": 80,
        "vida_extra": 60
    },
}

ITENS_DIVERSOS_INFO = {
    "Mapa Rasgado": {
        "descricao": "Um mapa antigo com rotas misteriosas.",
        "uso": "Revela uma dica sobre a próxima missão disponível."
    },
    "Mapa do Tesouro": {
        "descricao": "Indica a localização de um tesouro escondido.",
        "uso": "Ganha entre 30 e 80 moedas de ouro ao usar."
    },
    "Bússola Enferrujada": {
        "descricao": "Ainda aponta para o norte... mais ou menos.",
        "uso": "Aumenta em 20% a chance de fuga em combate por 3 turnos."
    },
    "Amuleto Pirata": {
        "descricao": "Um amuleto misterioso com poderes desconhecidos.",
        "uso": "Recupera 15 de vida e concede +5 de dano por 2 turnos."
    },
    "Rum Raro": {
        "descricao": "Um rum de qualidade excepcional. Cheira muito bem.",
        "uso": "Recupera 50 de vida e 20 de stamina. Melhor que o comum!"
    },
    "Charuto de Nassau": {
        "descricao": "Um charuto fino, selado com lacre dourado.",
        "uso": "Recupera 25 de stamina e concede +3 de dano pelo próximo combate."
    },
    "Dente de Tubarão Bênto": {
        "descricao": "Um dente de tubarão com uma runa entalhada.",
        "uso": "Aumenta em 15% a chance de crítico no próximo combate."
    },
    "Garrafa de Vinho de Lisboa": {
        "descricao": "Um vinho encorpado trazido do Velho Mundo.",
        "uso": "Recupera 40 de vida e 20 de stamina."
    },
}

#Portos:

PORTOS = {
    "Porto de Nassau":    {"nacao": "Britânico",  "custo_viagem": 0},
    "Porto de Tortuga":   {"nacao": "Francês",    "custo_viagem": 10},
    "Porto de Cartagena": {"nacao": "Espanhol",   "custo_viagem": 20},
    "Porto de Lisboa":    {"nacao": "Português",  "custo_viagem": 15},
}

#DONAS DA TAVERNA - FALAS E MISSÕES A CADA TAVERNA:

DONAS_TAVERNA = {
    "Nassau": {
        "nome": "Marge",
        "descricao": (
            " Uma mulher larga, de braços cruzados e olhar que já viu tudo.\n"
            " A taberna dela é a mais antiga de Nassau — e ela sabe de cada segredo\n"
            " que já foi sussurrado entre um gole e outro nessas paredes."
        ),
        "fala": (
            " 'Conheço o caminho para a Baía do Homem Morto.'\n"
            " 'Já vi piratas melhores que você tentarem.'\n"
            "> Ela acende um charuto sem tirar os olhos de você.\n"
            " 'Nenhum voltou para me contar como foi. Mas você... tem cara de sortudo.'\n"
            "> Ela empurra um charuto pela bancada com dois dedos.\n"
            " 'Leve. Acenda quando as coisas ficarem difíceis. Ajuda a pensar.'"
        ),
        "item": "Charuto de Nassau",
        "despedida": (
            "> Marge volta a limpar o balcão sem olhar para trás.\n"
            " 'Se você morrer lá, pelo menos terá fumado um bom charuto.'"
        ),
        "alianca": "Marge, a Dona da Taberna de Nassau",
    },
    "Tortuga": {
        "nome": "Céleste",
        "descricao": (
            " Alta, com cabelos cacheados presos por uma faca e um sorriso que some\n"
            " rápido demais para ser honesto. Fala com sotaque crioulo e gesticula muito.\n"
            " Ninguém sabe de onde ela veio — e ninguém ousa perguntar."
        ),
        "fala": (
            " 'Ah, mais um procurando a Baía...' — ela ri, mas sem alegria.\n"
            " 'Eu sei do caminho, oui. Aprendi com quem não voltou.'\n"
            "> Ela se inclina sobre o balcão, olhos escuros te avaliando.\n"
            " 'O mar ali não é água. É memória. E memória afoga.'\n"
            "> Ela desliza um dente de tubarão atravessado por uma cordinha fina.\n"
            " 'Meu avô pescou esse tubarão. A runa, gravei eu mesma. Vai precisar\n"
            "  de mais sorte do que coragem onde você vai.'"
        ),
        "item": "Dente de Tubarão Bênto",
        "despedida": (
            "> Céleste acende uma vela e murmura algo em crioulo que você não entende.\n"
            " 'Bonne chance, capitaine. O mar decide — não você.'"
        ),
        "alianca": "Céleste, a Dona da Taverna de Tortuga",
    },
    "Cartagena": {
        "nome": "Dolores",
        "descricao": (
            " Uma mulher de meia-idade com vestes escuras e um rosário enrolado no pulso.\n"
            " Fala pouco, observa muito. Dizem que ela já foi espiã da Coroa espanhola\n"
            " antes de desaparecer por dez anos — e reaparecer servindo rum em Cartagena."
        ),
        "fala": (
            "> Ela não levanta os olhos quando você se aproxima.\n"
            " 'A Baía.' — uma afirmação, não uma pergunta.\n"
            " 'Todo mundo que chega aqui com esse olhar vai para lá.'\n"
            "> Ela limpa um copo lentamente, depois te olha de frente.\n"
            " 'Eu servi a Coroa. Servi os piratas. Agora não sirvo ninguém.'\n"
            " 'Mas vou te dizer uma coisa de graça: o que guarda a Baía não tem\n"
            "  medo de ferro. Tem medo de quem não recua.'\n"
            "> Ela coloca um amuleto na sua mão sem cerimônia.\n"
            " 'Era do último que perguntou. Ele não voltou para reclamar.'"
        ),
        "item": "Amuleto Pirata",
        "despedida": (
            "> Dolores volta a rezar em silêncio, dedos no rosário.\n"
            " 'Vá com Deus. Ou com o Diabo. Tanto faz lá onde você vai.'"
        ),
        "alianca": "Dolores, a Dona da Taverna de Cartagena",
    },
    "Lisboa": {
        "nome": "Inês",
        "descricao": (
            " Uma senhora elegante, cabelos grisalhos presos com perfeição, mãos\n"
            " que nunca tremem ao verter vinho. Fala com a precisão de quem\n"
            " escolhe cada palavra antes de soltá-la. Dizem que foi cartógrafa\n"
            " antes de abrir a taverna — e que ainda desenha mapas à noite."
        ),
        "fala": (
            "> Ela te serve um copo de vinho antes mesmo de você sentar.\n"
            " 'De Lisboa partem todas as rotas. E para cá voltam todas as histórias.'\n"
            "> Ela se apoia no balcão, voz baixa e precisa.\n"
            " 'A Baía do Homem Morto está nos registros antigos que ninguém\n"
            "  mais lê. Estive lá uma vez — de longe. Não me aproximei.'\n"
            " 'O mar muda de cor perto da Baía. Fica verde escuro, quase preto.'\n"
            " 'Quando você ver isso, não olhe para baixo.'\n"
            "> Ela empurra uma garrafa lacrada pela bancada.\n"
            " 'Vinho do Douro. Envelhecido. Beba antes de entrar na Baía.\n"
            "  Se não beber, leve como lembrança de que já esteve em Lisboa.'"
        ),
        "item": "Garrafa de Vinho de Lisboa",
        "despedida": (
            "> Inês anota algo num caderno pequeno sem explicar o quê.\n"
            " 'Se você sobreviver, volte aqui. Quero ouvir o que tem lá dentro.\n"
            "  Não para o mapa — por curiosidade mesmo.'"
        ),
        "alianca": "Inês, a Dona da Taberna de Lisboa",
    },
}

#Lojas por porto, cada loja mostra itens diferentes.

LOJA_POR_PORTO = {
    "Porto de Nassau": {
        "Pequena Poção de Vida": ITENS_CURA["Pequena Poção de Vida"],
        "Poção de Vida":         ITENS_CURA["Poção de Vida"],
        "Rum do Pirata":         ITENS_CURA["Rum do Pirata"],
    },
    "Porto de Tortuga": {
        "Poção de Vida":         ITENS_CURA["Poção de Vida"],
        "Grande Poção de Vida":  ITENS_CURA["Grande Poção de Vida"],
        "Rum do Pirata":         ITENS_CURA["Rum do Pirata"],
        "Kit Médico":            ITENS_CURA["Kit Médico"],
    },
    "Porto de Cartagena": {
        "Kit Médico":            ITENS_CURA["Kit Médico"],
        "Grande Poção de Vida":  ITENS_CURA["Grande Poção de Vida"],
        "Elixir Antigo":         ITENS_CURA["Elixir Antigo"],
        "Rum do Pirata":         ITENS_CURA["Rum do Pirata"],
    },
    "Porto de Lisboa": {
        "Pequena Poção de Vida": ITENS_CURA["Pequena Poção de Vida"],
        "Poção de Vida":         ITENS_CURA["Poção de Vida"],
        "Kit Médico":            ITENS_CURA["Kit Médico"],
        "Grande Poção de Vida":  ITENS_CURA["Grande Poção de Vida"],
        "Elixir Antigo":         ITENS_CURA["Elixir Antigo"],
        "Rum do Pirata":         ITENS_CURA["Rum do Pirata"],
    },
}

LOJA_PACTUARIO_POR_PORTO = {
    "Porto de Nassau": {
        "Fragmento Sombrio":   ITENS_PACTUARIO["Fragmento Sombrio"],
        "Grimório Antigo":     ITENS_PACTUARIO["Grimório Antigo"],
    },
    "Porto de Tortuga": {
        "Fragmento Sombrio":   ITENS_PACTUARIO["Fragmento Sombrio"],
        "Essência do Abismo":  ITENS_PACTUARIO["Essência do Abismo"],
        "Cristal Amaldiçoado": ITENS_PACTUARIO["Cristal Amaldiçoado"],
    },
    "Porto de Cartagena": {
        "Cristal Amaldiçoado": ITENS_PACTUARIO["Cristal Amaldiçoado"],
        "Relíquia Sombria":    ITENS_PACTUARIO["Relíquia Sombria"],
        "Cartas Ciganas":      ITENS_PACTUARIO["Cartas Ciganas"],
    },
    "Porto de Lisboa": {
        "Fragmento Sombrio":   ITENS_PACTUARIO["Fragmento Sombrio"],
        "Essência do Abismo":  ITENS_PACTUARIO["Essência do Abismo"],
        "Grimório Antigo":     ITENS_PACTUARIO["Grimório Antigo"],
        "Cristal Amaldiçoado": ITENS_PACTUARIO["Cristal Amaldiçoado"],
        "Relíquia Sombria":    ITENS_PACTUARIO["Relíquia Sombria"],
        "Cartas Ciganas":      ITENS_PACTUARIO["Cartas Ciganas"],
    },
}

LOCALIZACAO_TERRA = "terra"
LOCALIZACAO_MAR   = "mar"

#CLASSES DISPONIVEIS PARA PERSONAGEM:

class Personagem:
    def __init__(self, nome, classe, vida, dano, stamina, nivel):
        self.nome           = nome
        self.classe         = classe
        self.vida_base      = vida
        self.dano_base      = dano
        self.stamina_base   = stamina
        self.vida           = vida
        self.vida_maxima    = vida
        self.dano           = dano
        self.stamina        = stamina
        self.stamina_maxima = stamina
        self.nivel          = nivel
        self.exp            = 0
        self.exp_necessaria = 100
        self.ouro           = 50
        self.inventario     = []
        self.habilidades    = []
        self.buff_dano      = 0
        self.buff_turnos    = 0
        self.bussola_ativa  = 0
        self.amuleto_ativo  = 0
        self.charuto_ativo  = 0
        self.dente_critico  = False
        self._perola_interacoes = 0

        self.arma_equipada = ARMAS_POR_CLASSE[classe][0]
        self.inventario.append(self.arma_equipada["nome"])

    def _cor_classe(self):
        return roxo if self.classe == "Pactuário" else azul

    def dano_total(self):
        bonus_amuleto = 5 if self.amuleto_ativo > 0 else 0
        bonus_charuto = 3 if self.charuto_ativo > 0 else 0
        return self.dano + self.arma_equipada["bonus_dano"] + self.buff_dano + bonus_amuleto + bonus_charuto

    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        c(amarelo + f"\n✧₊⁺ +{quantidade} EXP!" + RESET)
        while self.exp >= self.exp_necessaria:
            self.exp -= self.exp_necessaria
            self._subir_nivel()

    def _subir_nivel(self):
        self.nivel         += 1
        self.exp_necessaria = 100 + (self.nivel - 1) * 20
        ganho_vida    = 10
        ganho_dano    = 5
        ganho_stamina = 5
        self.vida_maxima    += ganho_vida
        self.vida            = self.vida_maxima
        self.dano           += ganho_dano
        self.stamina_maxima += ganho_stamina
        self.stamina         = self.stamina_maxima

        c(" ")
        c(amarelo + f" ◝(ᵔᗜᵔ)◜ LEVEL UP! Você chegou ao nível {self.nivel}!" + RESET)
        c(amarelo + f" ❤︎ Vida:    +{ganho_vida} → {self.vida_maxima}" + RESET)
        c(amarelo + f" 🗡 Dano:    +{ganho_dano} → {self.dano}" + RESET)
        c(amarelo + f" 🗲 Stamina: +{ganho_stamina} → {self.stamina_maxima}" + RESET)
        c(amarelo + f" ᝰ Próximo nível: {self.exp_necessaria} EXP" + RESET)
        c(" ")
        self._verificar_nova_arma()

    def _verificar_nova_arma(self):
        for arma in ARMAS_POR_CLASSE[self.classe]:
            if arma["nivel"] == self.nivel:
                emoji = TIER_EMOJI[arma["tier"]]
                c(amarelo + f"\n{emoji} NOVA ARMA DESBLOQUEADA: {arma['nome']} [{arma['tier']}]" + RESET)
                c(amarelo + f"   > Bônus de dano: +{arma['bonus_dano']}" + RESET)
                c(amarelo + "   > A arma anterior pode ser vendida em qualquer porto." + RESET)
                self.inventario.append(arma["nome"])
                self.arma_equipada = arma
                break

    def usar_item(self, nome_item):
        if nome_item not in self.inventario:
            c(vermelho + " ⚠︎ Item não encontrado no inventário." + RESET)
            return False

        cor = roxo if self.classe == "Pactuário" else azul

        if nome_item in ITENS_CURA:
            item = ITENS_CURA[nome_item]
            if item["cura_total"]:
                self.vida    = self.vida_maxima
                self.stamina = self.stamina_maxima
                c(cor + f" ⋆˙⟡ {nome_item} usado! Vida e Stamina totalmente restauradas!" + RESET)
                c(vermelho + f" ❤︎  Vida: {self.vida}/{self.vida_maxima}" + RESET)
                cor_st = roxo if self.classe == "Pactuário" else azul
                c(cor_st + f" 🗲  Stamina: {self.stamina}/{self.stamina_maxima}" + RESET)
            else:
                self.vida    = min(self.vida_maxima, self.vida + item["vida"])
                self.stamina = min(self.stamina_maxima, self.stamina + item["stamina"])
                c(cor + f" ⋆˙⟡ {nome_item} usado!" + RESET)
                c(vermelho + f" ❤︎  Vida: {self.vida}/{self.vida_maxima}" + RESET)
                cor_st = roxo if self.classe == "Pactuário" else azul
                c(cor_st + f" 🗲  Stamina: {self.stamina}/{self.stamina_maxima}" + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item in ITENS_PACTUARIO and self.classe == "Pactuário":
            item = ITENS_PACTUARIO[nome_item]
            self.stamina = min(self.stamina_maxima, self.stamina + item["stamina"])
            if item.get("buff_turnos", 0) > 0:
                self.buff_dano   = item["bonus_dano"]
                self.buff_turnos = item["buff_turnos"]
            vida_extra = item.get("vida_extra", 0)
            if vida_extra:
                self.vida = min(self.vida_maxima, self.vida + vida_extra)
            c(roxo + f" ˚☽˚.⋆ {nome_item} usado! {item['descricao']}" + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item in ITENS_DIVERSOS_INFO:
            return self._usar_item_diverso(nome_item)

        c(vermelho + " ⚠︎ Você não pode usar este item." + RESET)
        return False

    def _usar_item_diverso(self, nome_item):
        cor = roxo if self.classe == "Pactuário" else azul

        if nome_item == "Rum Raro":
            self.vida    = min(self.vida_maxima, self.vida + 50)
            self.stamina = min(self.stamina_maxima, self.stamina + 20)
            c(cor + f" 🍻 {nome_item} usado!" + RESET)
            c(vermelho + f" ❤︎  Vida: {self.vida}/{self.vida_maxima}" + RESET)
            c(cor + f" 🗲  Stamina: {self.stamina}/{self.stamina_maxima}" + RESET)
            c(branco + " 'Esse sim é um bom rum!' — diria qualquer pirata." + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Mapa do Tesouro":
            ouro = random.randint(30, 80)
            self.ouro += ouro
            c(" ")
            c(cor + f" 🗺 Você seguiu o Mapa do Tesouro e encontrou {ouro} moedas escondidas!" + RESET)
            c(amarelo + f" ⛃ Ouro total: {self.ouro}" + RESET)
            c(" ")
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Mapa Rasgado":
            c(" ")
            c(cor + "🗺 Você examina o Mapa Rasgado com atenção..." + RESET)
            c(" ")
            time.sleep(0.5)
            c(branco + "As marcações indicam rotas perigosas e portos esquecidos."  + RESET)
            c(azul   + "✦ Dica: Porto de Lisboa tem os melhores itens disponíveis." + RESET)
            c(azul   + "✦ Dica: Missões de mar concedem mais EXP que as terrestres." + RESET)
            c(branco + "(O mapa está muito rasgado para usar novamente.)" + RESET)
            c(" ")
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Bússola Enferrujada":
            self.bussola_ativa = 3
            c(cor + " ✵ Bússola Enferrujada ativada!" + RESET)
            c(cor + "   +20% de chance de fuga por 3 combates." + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Amuleto Pirata":
            self.vida          = min(self.vida_maxima, self.vida + 15)
            self.amuleto_ativo = 2
            c(cor + f" 𓂀 Amuleto Pirata ativado! +15 de vida | +5 de dano por 2 combates." + RESET)
            c(amarelo + f" ❤︎ Vida: {self.vida}/{self.vida_maxima}" + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Charuto de Nassau":
            self.stamina       = min(self.stamina_maxima, self.stamina + 25)
            self.charuto_ativo = 1
            c(cor + f" ᝰ▬▬ Charuto de Nassau aceso!" + RESET)
            c(cor + f" 🗲  Stamina: {self.stamina}/{self.stamina_maxima}" + RESET)
            c(cor + " +3 de dano no próximo combate. A fumaça te acalma." + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Dente de Tubarão Bênto":
            self.dente_critico = True
            c(cor + " 𓂁 Dente de Tubarão Bênto segurado com força!" + RESET)
            c(cor + " +15% de chance de acerto crítico no próximo combate." + RESET)
            c(branco + " A runa de Céleste brilha levemente." + RESET)
            self.inventario.remove(nome_item)
            return True

        if nome_item == "Garrafa de Vinho de Lisboa":
            self.vida    = min(self.vida_maxima, self.vida + 40)
            self.stamina = min(self.stamina_maxima, self.stamina + 20)
            c(cor + f" 🥂 Garrafa de Vinho de Lisboa aberta!" + RESET)
            c(vermelho + f" ❤︎  Vida: {self.vida}/{self.vida_maxima}" + RESET)
            c(cor + f" 🗲  Stamina: {self.stamina}/{self.stamina_maxima}" + RESET)
            c(branco + "    Encorpado. Suave. Inês tinha razão — é sofisticado." + RESET)
            self.inventario.remove(nome_item)
            return True

        c(vermelho + " ⚠︎ Este item não pode ser usado agora." + RESET)
        return False

    def status(self):
        emoji_tier = TIER_EMOJI[self.arma_equipada["tier"]]

        c(" ")
        c(branco + "  Perfil do marujo  " + RESET)
        c(branco + "└──────────────────┘" + RESET)
        c(branco + " ༺  ⚜  ༻ " + RESET)
        c(" ")
        c(branco + f"> Nome:   {self.nome}" + RESET)
        c(branco + f"> Classe: {self.classe}" + RESET)
        c(branco + f"> Nível:  {self.nivel}" + RESET)
        c(branco + f"> EXP:    {self.exp}/{self.exp_necessaria}" + RESET)
        c(branco + "  " + "─" * 30 + RESET)
        c(vermelho + f"❤︎ Vida: {self.vida}/{self.vida_maxima}" + RESET)
        c(vermelho + f"🗡 Dano: {self.dano_total()}" + RESET)
        c(branco    + f"🗲 Stamina:{self.stamina}/{self.stamina_maxima}" + RESET)
        c(branco + "  " + "─" * 30 + RESET)
        c(amarelo + f"Arma: {emoji_tier} {self.arma_equipada['nome']}" + RESET)
        c(amarelo + f"> Tier: {self.arma_equipada['tier']}" + RESET)
        c(branco + "  " + "─" * 30 + RESET)
        c(amarelo + f"⛃ Ouro: {self.ouro}" + RESET)
        c(branco + "  " + "─" * 30 + RESET)
        if self.inventario:
            c(branco + "> Inventário:" + RESET)
            for item in self.inventario:
                c(branco + f"   · {item}" + RESET)
            c(branco + "  " + "─" * 30 + RESET)
        if self.habilidades:
            c(azul + "> Habilidades:" + RESET)
            for hab in self.habilidades:
                c(azul + f"   · {hab}" + RESET)
        c(" ")


class Atirador(Personagem):
    def __init__(self, nome): super().__init__(nome, "Atirador", 80, 22, 90, 1)

class Corsario(Personagem):
    def __init__(self, nome): super().__init__(nome, "Corsário", 100, 18, 80, 1)

class Bombardeiro(Personagem):
    def __init__(self, nome): super().__init__(nome, "Bombardeiro", 90, 25, 60, 1)

class Pactuario(Personagem):
    def __init__(self, nome): super().__init__(nome, "Pactuário", 75, 20, 100, 1)

class Pesquisador(Personagem):
    def __init__(self, nome): super().__init__(nome, "Pesquisador", 85, 12, 95, 1)

class Espadachim(Personagem):
    def __init__(self, nome): super().__init__(nome, "Espadachim", 95, 20, 85, 1)

#INIMIGOS:

class Inimigo:
    def __init__(self, nome, tipo, vida, dano, recompensa_ouro, recompensa_exp):
        self.nome            = nome
        self.tipo            = tipo
        self.vida            = vida
        self.dano            = dano
        self.recompensa_ouro = recompensa_ouro
        self.recompensa_exp  = recompensa_exp

    def status(self):
        c(vermelho + f" ☠︎ {self.nome} apareceu! [{self.tipo}]" + RESET)
        c(vermelho + f"    Vida: {self.vida} | Dano: {self.dano}" + RESET)

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)


class Esqueleto(Inimigo):
    def __init__(self): super().__init__("Esqueleto", "Comum", 20, 8, 10, 15)

class Saqueador(Inimigo):
    def __init__(self): super().__init__("Saqueador", "Comum", 40, 10, 15, 20)

class BanditoCosteiro(Inimigo):
    def __init__(self): super().__init__("Bandido Costeiro", "Comum", 35, 9, 12, 18)

class Bebado(Inimigo):
    def __init__(self): super().__init__("Bêbado", "Comum", 25, 5, 5, 10)

class RatazanaPorto(Inimigo):
    def __init__(self): super().__init__("Ratazana do Porto", "Comum", 20, 6, 8, 12)

class Afogado(Inimigo):
    def __init__(self): super().__init__("Afogado", "Comum - Mar", 35, 9, 12, 18)

class Tubarao(Inimigo):
    def __init__(self): super().__init__("Tubarão", "Comum - Mar", 50, 14, 20, 25)

class Sereia(Inimigo):
    def __init__(self): super().__init__("Sereia", "Comum - Mar", 45, 12, 18, 22)

class TubaraoGigante(Inimigo):
    def __init__(self): super().__init__("Tubarão Gigante", "Comum - Mar", 80, 20, 35, 40)

class KrakenFilhote(Inimigo):
    def __init__(self): super().__init__("Kraken Filhote", "Comum - Mar", 80, 22, 40, 45)

class MoreiaGigante(Inimigo):
    def __init__(self): super().__init__("Moreia Gigante", "Comum - Mar", 70, 18, 30, 35)

class PolvoGigante(Inimigo):
    def __init__(self): super().__init__("Polvo Gigante", "Comum - Mar", 75, 17, 28, 33)

class CapitaoAmaldicado(Inimigo):
    def __init__(self): super().__init__("Capitão Amaldiçoado", "Sobrenatural", 80, 25, 50, 60)

class CorsarioMeioPeixe(Inimigo):
    def __init__(self): super().__init__("Corsário Meio Peixe", "Sobrenatural", 80, 22, 45, 55)

class PirataSemCabeca(Inimigo):
    def __init__(self): super().__init__("Pirata Sem Cabeça", "Sobrenatural", 75, 20, 40, 50)

class NavegadorEspectral(Inimigo):
    def __init__(self): super().__init__("Navegador Espectral", "Sobrenatural", 70, 18, 38, 48)

class CacadorRecompensa(Inimigo):
    def __init__(self): super().__init__("Caçador de Recompensas", "Humano", 65, 17, 35, 45)

class CapitaoRival(Inimigo):
    def __init__(self): super().__init__("Capitão Rival", "Humano", 80, 22, 50, 55)

class SoldadoNaval(Inimigo):
    VARIACOES = {"1": "Britânico", "2": "Francês", "3": "Espanhol", "4": "Português"}
    def __init__(self, nacionalidade="Britânico"):
        super().__init__(f"Soldado Naval {nacionalidade}", "Humano", 55, 14, 25, 30)
        self.nacionalidade = nacionalidade

class OficialCoroa(Inimigo):
    def __init__(self, nacionalidade="Britânico"):
        super().__init__(f"Oficial da Coroa {nacionalidade}", "Humano", 55, 18, 40, 45)
        self.nacionalidade = nacionalidade


class Chefe(Inimigo):
    def __init__(self, nome, vida, dano, recompensa_ouro, recompensa_exp, descricao):
        super().__init__(nome, "Chefe", vida, dano, recompensa_ouro, recompensa_exp)
        self.descricao = descricao

    def status(self):
        c(" ")
        c(vermelho + f" ☠︎  Chefe: {self.nome}" + RESET)
        c(branco   + f" {self.descricao}" + RESET)
        c(vermelho + f" Vida: {self.vida} | Dano: {self.dano}" + RESET)

class BarbaNegraChefe(Chefe):
    def __init__(self):
        super().__init__("Barba Negra", 300, 40, 200, 300,
            "No mar que eu comando, não há perdão — apenas o aço da minha vontade e o medo do meu nome!")

class AnneMaryChefe(Chefe):
    def __init__(self):
        super().__init__("Anne Bonny & Mary Read", 260, 35, 180, 270,
            "Não subestime uma mulher que dança com a morte, minha lâmina é minha lei!")

class ChingShihChefe(Chefe):
    def __init__(self):
        super().__init__("Ching Shih", 280, 38, 190, 285,
            "Nenhum vento, nenhuma onda e nenhum homem se opõe à frota que eu comando!")

class MobyDickChefe(Chefe):
    def __init__(self):
        super().__init__("Moby Dick", 400, 50, 250, 350,
            "Sou o eco das profundezas, o fantasma branco que rasga as ondas.")

class KrakenAncestralChefe(Chefe):
    def __init__(self):
        super().__init__("Kraken Ancestral", 300, 55, 300, 400,
            "O oceano é meu trono, e o medo, minha coroa.")

class FeiticeiraHalyssaChefe(Chefe):
    def __init__(self):
        super().__init__("Feiticeira Halyssa", 350, 45, 220, 320,
            "Nanm pase yo se chenn mwen… nan ba mwen, yo obeyi lwa mwen!")

#ESCALONAMENTO:

def escalar_inimigo(inimigo, nivel_jogador):
    fatores = {
        "Comum":        (0.40, 0.70),
        "Comum - Mar":  (0.45, 0.85),
        "Sobrenatural": (0.70, 1.00),
        "Humano":       (0.75, 1.00),
        "Chefe":        (1.20, 1.80),
    }
    minimo, maximo = fatores.get(inimigo.tipo, (0.50, 1.00))
    fator = random.uniform(minimo, maximo)
    inimigo.vida = int(inimigo.vida + (nivel_jogador - 1) * 10 * fator)
    inimigo.dano = int(inimigo.dano + (nivel_jogador - 1) * 2  * fator)
    return inimigo

def gerar_inimigo_comum(nivel_jogador):
    inimigos = [Esqueleto, Saqueador, BanditoCosteiro, Bebado, RatazanaPorto]
    return escalar_inimigo(random.choice(inimigos)(), nivel_jogador)

def gerar_inimigo_mar(nivel_jogador):
    inimigos = [Afogado, Tubarao, Sereia, TubaraoGigante, KrakenFilhote, MoreiaGigante, PolvoGigante]
    return escalar_inimigo(random.choice(inimigos)(), nivel_jogador)

def gerar_soldado(nivel_jogador):
    nac = random.choice(list(SoldadoNaval.VARIACOES.values()))
    return escalar_inimigo(random.choice([SoldadoNaval, OficialCoroa])(nac), nivel_jogador)

#REPUTAÇÃO:

class Reputacao:
    def __init__(self):
        self.infamia  = 0
        self.aliancas = []
        self._conquistas_infamia = set()

    MARCOS_INFAMIA = {
        10: {
            "titulo": "Corsário Procurado",
            "descricao": "Soldados Navais estão te procurando!",
            "beneficio": "Soldados ficam 10% mais fortes — mas sua lenda cresce.",
            "emoji": "⚠︎"
        },
        20: {
            "titulo": "O Flagelo dos Mares",
            "descricao": "Você virou o pirata mais procurado dos sete mares!",
            "beneficio": "Recompensas de ouro em combate aumentam em 15%.",
            "emoji": "♕"
        },
        35: {
            "titulo": "Terror da Coroa",
            "descricao": "Nenhum porto está seguro — guardas em alerta máximo!",
            "beneficio": "+20 de ouro bônus a cada vitória em combate.",
            "emoji": "☠︎"
        },
        50: {
            "titulo": "Lenda Amaldiçoada",
            "descricao": "Seu nome é sussurrado com medo em todos os portos.",
            "beneficio": "Inimigos comuns têm 20% de chance de fugir antes do combate.",
            "emoji": "𓂀"
        },
    }

    def adicionar_infamia(self, quantidade):
        anterior = self.infamia
        self.infamia += quantidade
        c(vermelho + f"  ☠︎  Sua infâmia aumentou! [{self.infamia}]" + RESET)
        c(" ")
        for marco, dados in self.MARCOS_INFAMIA.items():
            if anterior < marco <= self.infamia and marco not in self._conquistas_infamia:
                self._conquistas_infamia.add(marco)
                self._exibir_conquista(marco, dados)

    def _exibir_conquista(self, marco, dados):
        c(" ")
        c(amarelo + "═" * 40 + RESET)
        c(amarelo + f" {dados['emoji']}  CONQUISTA DE INFÂMIA DESBLOQUEADA!" + RESET)
        c(" ")
        c(amarelo + f" 🏳 Título: \"{dados['titulo']}\"" + RESET)
        c(branco  + f" 🗐 {dados['descricao']}" + RESET)
        c(azul    + f" ✦ Benefício: {dados['beneficio']}" + RESET)
        c(" ")
        c(amarelo + "═" * 40 + RESET)
        c(" ")

    def tem_conquista(self, marco):
        return marco in self._conquistas_infamia

    def adicionar_alianca(self, aliado):
        if aliado not in self.aliancas:
            self.aliancas.append(aliado)
            c(azul + f" ✧ Nova aliança formada: {aliado}!" + RESET)
            c(" ")

    def status(self):
        c(vermelho + f" ☠︎ Infâmia: {self.infamia}" + RESET)
        c(" ")
        if self._conquistas_infamia:
            marcos_ativos = sorted(self._conquistas_infamia)
            titulos = [self.MARCOS_INFAMIA[m]["titulo"] for m in marcos_ativos]
            c(amarelo + f"🏳 Títulos: {' | '.join(titulos)}" + RESET)
        c(azul + f" 🗝 Alianças: {', '.join(self.aliancas) if self.aliancas else 'Nenhuma ainda'}" + RESET)

#Sistema de COMBATE:

def iniciar_combate(jogador, inimigo, reputacao):
    c(" ")
    c(vermelho + "═" * 30 + RESET)
    c(vermelho + f" {jogador.nome} VS {inimigo.nome}!" + RESET)
    c(vermelho + "═" * 30 + RESET)
    c(" ")
    inimigo.status()
    perola_fala(jogador)
    if inimigo.tipo == "Chefe":
        perola_boss(jogador)
    time.sleep(1)

    if reputacao.tem_conquista(50) and inimigo.tipo in ("Comum", "Comum - Mar"):
        if random.random() < 0.20:
            c(roxo + f" 𓂀 {inimigo.nome} reconhece seu nome — e FOGE apavorado!" + RESET)
            c(branco + " Sua lenda amaldiçoada fala mais alto que qualquer arma." + RESET)
            return True

    if "ataque_surpresa" in jogador.habilidades:
        if random.random() < 0.30:
            dano_surpresa = jogador.dano_total() * 2
            inimigo.receber_dano(dano_surpresa)
            c(ciano + ' 𓅪 Pérola grita: "ATAQUE SURPRESA, OTÁRIO!"' + RESET)
            c(" ")
            _cor_dano = roxo if jogador.classe == "Pactuário" else vermelho
            c(_cor_dano + f" ⚔ Dano duplo: -{dano_surpresa}! Vida do inimigo: {inimigo.vida}" + RESET)
            c(" ")
            if not inimigo.esta_vivo():
                return _vitoria(jogador, inimigo, reputacao)

    turno = 1
    while jogador.vida > 0 and inimigo.esta_vivo():
        c(" ")
        c(azul + "─" * 30 + RESET)
        c(branco + f" Turno {turno}" + RESET)
        c(azul + "─" * 30 + RESET)
        c(vermelho + f"❤︎  {jogador.nome}: {jogador.vida}/{jogador.vida_maxima}" + RESET)

        cor_st = roxo if jogador.classe == "Pactuário" else azul
        aviso_st = vermelho + " ⚠︎ BAIXA!" + RESET if jogador.stamina < 15 else ""
        c(cor_st + f"🗲 Stamina: {jogador.stamina}/{jogador.stamina_maxima}" + RESET + aviso_st)

        c(azul + "─" * 30 + RESET)
        c(vermelho + f"☠  {inimigo.nome} | ❤︎: {inimigo.vida}" + RESET)
        c(azul + "─" * 30 + RESET)
        c(" ")

#Mostrar custo de stamina nas opções de combate.

        sem_stamina = jogador.stamina < CUSTO_ATAQUE_NORMAL
        aviso_atk   = vermelho + " [SEM STAMINA — dano reduzido]" + RESET if sem_stamina else ""

        c(branco + "╭─────────────────────────────╮" + RESET)
        c(branco + "        O que você faz?        " + RESET)
        c(branco + "├─────────────────────────────┤" + RESET)
        c(branco + f"1 > ⚔ Atacar [{CUSTO_ATAQUE_NORMAL} stamina]{aviso_atk}" + RESET)
        c(branco + f"2 > 🛡 Defender [recupera {REGENERACAO_DEFENDER} stamina]" + RESET)
        c(branco + "3 > 🂡 Usar item " + RESET)
        c(branco + "4 > ༄ Fugir     " + RESET)
        c(branco + "╰─────────────────────────────╯" + RESET)
        c(" ")

        acao = ci("> ")
        defendendo = False

        if acao == "1":
            _jogador_ataca(jogador, inimigo)
            perola_fala(jogador)

#Defender gera stamina.

        elif acao == "2":
            defendendo = True
            ganho = min(REGENERACAO_DEFENDER, jogador.stamina_maxima - jogador.stamina)
            jogador.stamina += ganho
            c(" ")
            c(azul + "🛡 Você assume posição defensiva!" + RESET)
            if ganho > 0:
                c(cor_st + f"🗲  +{ganho} stamina recuperada → {jogador.stamina}/{jogador.stamina_maxima}" + RESET)

        elif acao == "3":
            itens_uteis = [
                item for item in jogador.inventario
                if item in ITENS_CURA
                or (item in ITENS_PACTUARIO and jogador.classe == "Pactuário")
                or item in ITENS_DIVERSOS_INFO
            ]
            if not itens_uteis:
                c(" ")
                c(vermelho + " ✗ Nenhum item utilizável no inventário!" + RESET)
                continue
            c(" ")
            c(branco + " > Itens disponíveis:" + RESET)
            for i, item in enumerate(itens_uteis, 1):
                desc = ""
                if item in ITENS_CURA:
                    desc = ITENS_CURA[item]["descricao"]
                elif item in ITENS_PACTUARIO:
                    desc = ITENS_PACTUARIO[item]["descricao"]
                elif item in ITENS_DIVERSOS_INFO:
                    desc = ITENS_DIVERSOS_INFO[item]["uso"]
                c(azul + f"   {i}. {item} — {desc}" + RESET)
            c(azul + "   0. Cancelar" + RESET)
            escolha_item = ci("\n> ")
            try:
                escolha_item = int(escolha_item)
                if escolha_item == 0:
                    continue
                if 1 <= escolha_item <= len(itens_uteis):
                    jogador.usar_item(itens_uteis[escolha_item - 1])
                else:
                    c(vermelho + "Escolha inválida." + RESET)
                    continue
            except ValueError:
                c(vermelho + "Escolha inválida." + RESET)
                continue

        elif acao == "4":
            chance_fuga = 0.50
            if jogador.bussola_ativa > 0:
                chance_fuga = 0.70
            resultado_fuga = _tentar_fugir(jogador, inimigo, chance_fuga)
            if resultado_fuga is None:
                if jogador.bussola_ativa > 0:
                    jogador.bussola_ativa -= 1
                return None
        else:
            c(vermelho + "Ação inválida." + RESET)
            continue

        if inimigo.esta_vivo():
            _inimigo_ataca(inimigo, jogador, defendendo)

        if jogador.buff_turnos > 0:
            jogador.buff_turnos -= 1
            if jogador.buff_turnos == 0:
                jogador.buff_dano = 0
                c(" ")
                c(roxo + " ִ ࣪𖤐 O buff mágico se dissipou." + RESET)

        if not inimigo.esta_vivo():
            return _vitoria(jogador, inimigo, reputacao)

        if jogador.vida <= 0:
            return _derrota(jogador)

        turno += 1

    return False

#Stamina consumida no ataque; sem stamina = dano reduzido em 40%

def _jogador_ataca(jogador, inimigo):
    cor_ataque = roxo if jogador.classe == "Pactuário" else vermelho
    cor_st     = roxo if jogador.classe == "Pactuário" else azul

    sem_stamina = jogador.stamina < CUSTO_ATAQUE_NORMAL
    if not sem_stamina:
        jogador.stamina = max(0, jogador.stamina - CUSTO_ATAQUE_NORMAL)
    else:
        c(" ")
        c(vermelho + " ⚠︎ Sem stamina suficiente — ataque enfraquecido!" + RESET)

    dano           = jogador.dano_total()
    if sem_stamina:
        dano = int(dano * 0.60)

    chance_critico = 0.25 if jogador.dente_critico else 0.10
    critico        = random.random() < chance_critico

    if critico:
        dano = int(dano * 1.5)
        c(" ")
        c(cor_ataque + f" ✶ CRÍTICO! Você acerta {inimigo.nome} com tudo!" + RESET)
    else:
        c(" ")
        c(cor_ataque + f" ⚔ Você ataca {inimigo.nome}!" + RESET)

    dano = int(dano * random.uniform(0.90, 1.10))
    inimigo.receber_dano(dano)
    c(cor_ataque + f" Dano causado: -{dano} | Vida do inimigo: {max(0, inimigo.vida)}" + RESET)
    c(cor_st + f" 🗲  Stamina: {jogador.stamina}/{jogador.stamina_maxima}" + RESET)

    if jogador.dente_critico:
        jogador.dente_critico = False
        c(azul + " 𓂁 O brilho do Dente de Tubarão Bênto se apagou." + RESET)

    if jogador.charuto_ativo > 0:
        jogador.charuto_ativo -= 1
        if jogador.charuto_ativo == 0:
            c(azul + " ᝰ▬▬ O efeito do Charuto de Nassau se dissipou." + RESET)


def _inimigo_ataca(inimigo, jogador, defendendo):
    dano = int(inimigo.dano * random.uniform(0.85, 1.15))
    if defendendo:
        dano = dano // 2
        c(" ")
        c(azul   + f"🛡 Você se defende! {inimigo.nome} causa apenas {dano} de dano." + RESET)
    else:
        c(" ")
        c(vermelho + f"𖦹 {inimigo.nome} ataca você!" + RESET)
        c(vermelho + f"Dano recebido: -{dano}" + RESET)
    jogador.vida -= dano
    jogador.vida  = max(0, jogador.vida)
    c(vermelho + f"❤︎ Vida restante: {jogador.vida}/{jogador.vida_maxima}" + RESET)

    if jogador.amuleto_ativo > 0:
        jogador.amuleto_ativo -= 1
        if jogador.amuleto_ativo == 0:
            c(azul + " 𓂀 O efeito do Amuleto Pirata se dissipou." + RESET)


def _tentar_fugir(jogador, inimigo, chance=0.50):
    if inimigo.tipo == "Chefe":
        c(" ")
        c(vermelho + " ☠︎ Não há como fugir de um Chefe!" + RESET)
        return False
    if random.random() < chance:
        c(" ")
        c(azul + " ༄ Você conseguiu fugir!" + RESET)
        return None
    else:
        c(" ")
        c(vermelho + " ✗ Fuga falhou! O inimigo bloqueia seu caminho!" + RESET)
        return False


def _vitoria(jogador, inimigo, reputacao):
    c(" ")
    c(amarelo + "═" * 25 + RESET)
    c(amarelo + f"> {inimigo.nome} foi derrotado!" + RESET)
    c(amarelo + "═" * 25 + RESET)
    jogador.ganhar_exp(inimigo.recompensa_exp)
    ouro_ganho = int(inimigo.recompensa_ouro * random.uniform(0.85, 1.15))

    if reputacao.tem_conquista(20):
        bonus = int(ouro_ganho * 0.15)
        ouro_ganho += bonus

    if reputacao.tem_conquista(35):
        ouro_ganho += 20

    jogador.ouro += ouro_ganho
    c(amarelo + f" ⛃ +{ouro_ganho} moedas de ouro! Total: {jogador.ouro}" + RESET)

    #Stamina regenera parcialmente após vitória
    regen_stamina = min(15, jogador.stamina_maxima - jogador.stamina)
    if regen_stamina > 0:
        jogador.stamina += regen_stamina
        cor_st = roxo if jogador.classe == "Pactuário" else azul
        c(cor_st + f" 🗲  +{regen_stamina} stamina recuperada após o combate → {jogador.stamina}/{jogador.stamina_maxima}" + RESET)

    if random.random() < 0.30:
        drops_possiveis = ["Pequena Poção de Vida", "Poção de Vida", "Rum do Pirata", "Kit Médico"]
        item_drop = random.choice(drops_possiveis)
        jogador.inventario.append(item_drop)
        c(azul + f" 𐙚 Item encontrado: {item_drop}!" + RESET)
    return True


def _derrota(jogador):
    c(" ")
    c(vermelho + " ☠︎  " + RESET)
    c(vermelho + f" {jogador.nome} caiu em batalha..." + RESET)
    c(vermelho + " " + "=" * 25 + RESET)
    c(branco   + " Achou que o mar me teria? Renasci para cobrar!" + RESET)
    c(" ")
    c(azul + " 1 > Recomeçar do último porto visitado (perde 30% do ouro)" + RESET)
    c(azul + " 2 > Encerrar o jogo." + RESET)
    escolha = ci("\n> ")
    if escolha == "1":
        perda        = int(jogador.ouro * 0.30)
        jogador.ouro -= perda
        jogador.vida  = jogador.vida_maxima // 2
        #Também recupera parte da stamina ao renascer
        jogador.stamina = jogador.stamina_maxima // 2
        c(azul    + f" ⚓︎ Você acorda num porto próximo. Perdeu {perda} moedas." + RESET)
        c(" ")
        c(vermelho + f" ❤︎  Vida recuperada: {jogador.vida}/{jogador.vida_maxima}" + RESET)
        cor_st = roxo if jogador.classe == "Pactuário" else azul
        c(cor_st + f" 🗲  Stamina: {jogador.stamina}/{jogador.stamina_maxima}" + RESET)
        return False
    else:
        c(" ")
        c(branco + " Até a próxima, pirata. ﹏𓊝﹏" + RESET)
        c(" ")
        exit()

#ROTA PRINCIPAL: ROTA DOS CONDENADOS:

POOL_CHEFES_ROTA = [
    BarbaNegraChefe,
    AnneMaryChefe,
    ChingShihChefe,
    MobyDickChefe,
    KrakenAncestralChefe,
]

def rota_dos_condenados(jogador, reputacao):
    c(vermelho + " ╔═════════════════╗ " + RESET)
    c(vermelho + "   A Maré do Juízo  " + RESET)
    c(vermelho + " ╚═════════════════╝ " + RESET)
    c(branco   + " > Aqui, o oceano é juiz e carrasco." + RESET)
    c(branco   + " > A Maré do Juízo engole os fracos." + RESET)
    c(" ")
    c(branco   + " > A Baía te aguarda." + RESET)
    c(" ")
    time.sleep(2)

    ordem = POOL_CHEFES_ROTA.copy()
    random.shuffle(ordem)

    for i, ClasseChefe in enumerate(ordem):
        chefe = escalar_inimigo(ClasseChefe(), jogador.nivel)
        c(" ")
        c(vermelho + f" ☠︎  Chefe {i+1} de {len(ordem)}:" + RESET)
        c(" ")
        chefe.status()
        time.sleep(1)

        vitoria = iniciar_combate(jogador, chefe, reputacao)
        if not vitoria:
            c(vermelho + " ☠︎  Você foi derrotado antes de chegar à Baía..." + RESET)
            c(" ")
            return False

        if i < len(ordem) - 1:
            recuperacao  = jogador.vida_maxima // 2
            jogador.vida = min(jogador.vida_maxima, jogador.vida + recuperacao)
            c(azul + f"\n ꕀ A brisa do mar te dá forças." + RESET)
            c(vermelho + f" ❤︎  Vida recuperada: +{recuperacao} → {jogador.vida}/{jogador.vida_maxima}" + RESET)
            time.sleep(1)

    c(vermelho + " ╔═════════════════════════════╗" + RESET)
    c(vermelho + "   A Guardiã da Baía Desperta.  " + RESET)
    c(vermelho + " ╚═════════════════════════════╝" + RESET)
    c(branco   + " O chão treme, o mar se agita," + RESET)
    c(branco   + " os mortos marcham comigo." + RESET)
    c(" ")
    c(roxo     + " Halyssa aparece." + RESET)
    c(" ")
    time.sleep(2)

    halyssa = escalar_inimigo(FeiticeiraHalyssaChefe(), jogador.nivel)
    halyssa.status()
    vitoria = iniciar_combate(jogador, halyssa, reputacao)

    if vitoria:
        _final_do_jogo(jogador)
        return True

    c(vermelho + " ☠︎  Halyssa permanece de pé. A Baía não foi conquistada..." + RESET)
    c(" ")
    return False


def _final_do_jogo(jogador):
    c(vermelho + " ╔═══════════════════════════════╗" + RESET)
    c(vermelho + "   O mar sempre lembrará de você. " + RESET)
    c(vermelho + " ╚═══════════════════════════════╝" + RESET)
    c(branco  + f" {jogador.nome} está de pé na Baía do Homem Morto." + RESET)
    c(" ")
    c(branco  + " A Feiticeira Halyssa foi derrotada." + RESET)
    c(branco  + " A névoa se dissipa. O mar acalma." + RESET)
    c(branco  + " Ninguém sabia o que havia na Baía." + RESET)
    c(" ")
    c(branco  + " Agora só você sabe." + RESET)
    c(amarelo + f" ⚓︎ Nível final:      {jogador.nivel}" + RESET)
    c(" ")
    c(amarelo + f" ⛃ Ouro acumulado:  {jogador.ouro}" + RESET)
    c(azul    + f" 🗝 Habilidades:     {len(jogador.habilidades)} conquistadas" + RESET)
    c(ciano   + f" 𓅪 Pérola com você? {'Sim!' if 'Pérola 𓅪' in jogador.inventario else 'Não desta vez.'}" + RESET)
    c(branco  + " ☠︎ > Obrigado por jogar." + RESET)
    c(" ")
    c(azul    + " 𓆝 𓆟 𓆞 𓆝 𓆟 A Baía do Homem Morto." + RESET)
    exit()

#MISSÕES POR PORTO:

MISSOES_PORTO = {
    "Porto de Nassau": {
        "titulo": "O Contrabando de Nassau",
        "descricao": (
            "> Um mercador suspeito te aborda nas docas de Nassau.\n"
            "  'Preciso de alguém discreto para guardar esta carga por uma noite.\n"
            "    Nada de perguntas — e nada de abrir os caixotes.'\n"
            "   A noite cai, e alguém mais quer a carga também."
        ),
        "recompensa": {
            "tipo": "ouro_e_item",
            "ouro": 80,
            "item": "Rum Raro",
            "exp": 120,
            "descricao": "80 moedas + Rum Raro + 120 EXP"
        },
        "inimigos": lambda nivel: [escalar_inimigo(BanditoCosteiro(), nivel),
                                    escalar_inimigo(Saqueador(), nivel)],
        "narrativa_vitoria": (
            "> A carga foi protegida. O mercador paga sem fazer contato visual.\n"
            "  'Não nos vimos.' — e some pela viela.\n"
            "> Você encontra um Rum Raro dentro de um dos caixotes. Ninguém precisa saber."
        ),
    },
    "Porto de Tortuga": {
        "titulo": "A Aposta da Bêbada",
        "descricao": (
            "> Na taverna mais barulhenta de Tortuga, uma pirata embriagada\n"
            "  aposta seu tesouro numa briga de faca contra você.\n"
            "  'Se ganhar, é seu. Se perder, pago em rum!'\n"
            "> A plateia já faz apostas. Não há como recuar."
        ),
        "recompensa": {
            "tipo": "alianca_e_ouro",
            "ouro": 100,
            "exp": 150,
            "alianca": "A Bebuna de Tortuga",
            "descricao": "100 moedas + Aliança 'A Bebuna de Tortuga' + 150 EXP"
        },
        "inimigos": lambda nivel: [escalar_inimigo(CapitaoRival(), nivel)],
        "narrativa_vitoria": (
            "  'Hah! Boa luta, estranho.' — ela ri enquanto escarra no chão.\n"
            "  'Volta quando precisar de uma espada bêbada. Sou rápida mesmo assim.'\n"
            "> A plateia vai embora. Você ficou com o tesouro e uma aliada improvável."
        ),
    },
    "Porto de Cartagena": {
        "titulo": "O Espião da Coroa",
        "descricao": (
            "> Uma nota desliza por baixo da sua porta:\n"
            "  'Há um espião espanhol infiltrado nos piratas. Elimine-o.\n"
            "   Recompensa garantida. Venha ao armazém ao anoitecer.'\n"
            "   O armazém cheira a pólvora e traição."
        ),
        "recompensa": {
            "tipo": "item_raro",
            "item": "Amuleto Pirata",
            "exp": 180,
            "ouro": 60,
            "descricao": "Amuleto Pirata + 60 moedas + 180 EXP"
        },
        "inimigos": lambda nivel: [escalar_inimigo(OficialCoroa("Espanhol"), nivel),
                                    escalar_inimigo(SoldadoNaval("Espanhol"), nivel)],
        "narrativa_vitoria": (
            "> O espião cai. Nos seus bolsos: um amuleto de boa sorte — da Coroa.\n"
            "  Irônico. Você o guarda sem pensar muito sobre isso.\n"
            "> A recompensa chega sem remetente. Cartagena tem memória longa."
        ),
    },
    "Porto de Lisboa": {
        "titulo": "A Relíquia do Navegador",
        "descricao": (
            "> Um velho cartógrafo te mostra um mapa fragmentado de Lisboa.\n"
            "  'Meu neto levou a última peça para as ruínas do forte.\n"
            "   Não voltou. Vá buscá-lo — e a relíquia.'\n"
            "> As ruínas escondem coisas que não deveriam estar vivas."
        ),
        "recompensa": {
            "tipo": "item_e_infamia",
            "item": "Mapa do Tesouro",
            "exp": 200,
            "ouro": 70,
            "infamia": 3,
            "descricao": "Mapa do Tesouro + 70 moedas + 200 EXP + 3 infâmia"
        },
        "inimigos": lambda nivel: [escalar_inimigo(PirataSemCabeca(), nivel),
                                    escalar_inimigo(CapitaoAmaldicado(), nivel)],
        "narrativa_vitoria": (
            "> O neto estava vivo — amedrontado, escondido atrás de uma coluna.\n"
            "  A relíquia era um mapa. Você fica com uma cópia.\n"
            "  'O que você viu lá dentro?' o cartógrafo pergunta.\n"
            "> Você não responde. Algumas histórias não têm preço."
        ),
    },
}


def executar_missao_porto(nome_porto, jogador, reputacao):
    dados = MISSOES_PORTO.get(nome_porto)
    if not dados:
        return

    c(" ")
    c(amarelo + "═" * 30 + RESET)
    c(amarelo + f" ✦ Missão exclusiva de {nome_porto.upper()}" + RESET)
    c(amarelo + "═" * 30 + RESET)
    c(" ")
    c(branco + f" 🗐 {dados['titulo']}" + RESET)
    for linha in dados["descricao"].split("\n"):
        c(branco + linha + RESET)
    c(" ")
    time.sleep(1)

    recomp = dados["recompensa"]
    c(azul + f" ✦ Recompensa possível: {recomp['descricao']}" + RESET)
    c(" ")
    aceitar = ci("Aceitar a missão? (s/n): ").strip().lower()
    c(" ")
    if aceitar != "s":
        c(branco + " Você recusa. A oportunidade some como névoa." + RESET)
        return

    inimigos = dados["inimigos"](jogador.nivel)
    for i, inimigo in enumerate(inimigos, 1):
        c(vermelho + f" ⚔ Encontro {i}/{len(inimigos)}:" + RESET)
        c(" ")
        vitoria = iniciar_combate(jogador, inimigo, reputacao)
        if not vitoria:
            c(vermelho + " ☠︎  A missão falhou. Essa chance não voltará." + RESET)
            c(" ")
            return

    c(" ")
    c(azul + "─" * 30 + RESET)
    for linha in dados["narrativa_vitoria"].split("\n"):
        c(branco + linha + RESET)
    c(azul + "─" * 30 + RESET)

    jogador.ganhar_exp(recomp["exp"])
    jogador.ouro += recomp.get("ouro", 0)
    if recomp.get("ouro", 0) > 0:
        c(amarelo + f" ⛃ +{recomp['ouro']} moedas! Total: {jogador.ouro}" + RESET)

    item = recomp.get("item")
    if item:
        jogador.inventario.append(item)
        c(azul + f" 𐙚 Item único obtido: {item}!" + RESET)

    alianca = recomp.get("alianca")
    if alianca:
        reputacao.adicionar_alianca(alianca)

    infamia = recomp.get("infamia", 0)
    if infamia > 0:
        reputacao.adicionar_infamia(infamia)

    c(amarelo + f" ✮⋆˙ Missão única de {nome_porto} concluída!" + RESET)

#MISSÕES PRINCIPAIS

MISSOES_PRINCIPAIS = [
    {"id": 1, "titulo": "Fuga do Porto",        "local": LOCALIZACAO_TERRA,
     "descricao": "Algo deu errado. Guardas cercam cada saída, lanternas cortam a escuridão. Corra antes que seja tarde!",
     "nivel_minimo": 1,  "chefe": None},
    {"id": 2, "titulo": "Rumo ao Desconhecido", "local": LOCALIZACAO_MAR,
     "descricao": "O mar aberto te espera. Ondas traiçoeiras escondem perigos e segredos que ninguém contou.",
     "nivel_minimo": 2,  "chefe": None},
    {"id": 3, "titulo": "A Ilha Maldita",       "local": LOCALIZACAO_TERRA,
     "descricao": "A ilha guarda pistas sobre a Baía do Homem Morto.. e espíritos que nunca descansam.",
     "nivel_minimo": 3,  "chefe": None},
    {"id": 4, "titulo": "O Navio Fantasma",     "local": LOCALIZACAO_MAR,
     "descricao": "Um navio sem bandeira surge no nevoeiro. Nenhum sinal de vida.. mas algo se move a bordo.",
     "nivel_minimo": 5,  "chefe": NavegadorEspectral},
    {"id": 5, "titulo": "Porto Corrupto",       "local": LOCALIZACAO_TERRA,
     "descricao": "Informações valiosas estão escondidas no porto da Coroa. Segredos e armadilhas podem custar sua vida.",
     "nivel_minimo": 6,  "chefe": None},
    {"id": 6, "titulo": "A Tempestade",         "local": LOCALIZACAO_MAR,
     "descricao": "O céu escurece. Ondas gigantes e criaturas surgem no caos. Apenas os fortes sobrevivem.",
     "nivel_minimo": 8,  "chefe": None},
    {"id": 7, "titulo": "O Guardião das Águas", "local": LOCALIZACAO_MAR,
     "descricao": "Algo antigo bloqueia a Baía. Uma força colossal agita o mar… é o Kraken Ancestral.",
     "nivel_minimo": 17, "chefe": KrakenAncestralChefe},
]

def iniciar_missao_principal(missao, jogador, reputacao):
    c(" ")
    c(amarelo + f" 🗐 {missao['titulo']}" + RESET)
    c(azul    + f" ⟟  Local: {'🏝  Terra' if missao['local'] == LOCALIZACAO_TERRA else '♒︎ Mar'}" + RESET)
    c(" ")
    c(branco + f" > {missao['descricao']}" + RESET)
    c(" ")
    time.sleep(1)

    if jogador.nivel < missao["nivel_minimo"]:
        c(" ")
        c(vermelho + f" 🔒︎ Você precisa ser nível {missao['nivel_minimo']} para esta missão." + RESET)
        c(vermelho + f"    Seu nível atual: {jogador.nivel}" + RESET)
        return False

    encontros = random.randint(5, 7)
    for i in range(encontros):
        c(" ")
        c(vermelho + f" ⚔  Encontro {i+1}/{encontros}:" + RESET)
        if missao["local"] == LOCALIZACAO_TERRA:
            inimigo = gerar_inimigo_comum(jogador.nivel)
        else:
            inimigo = gerar_inimigo_mar(jogador.nivel)
        vitoria = iniciar_combate(jogador, inimigo, reputacao)
        if vitoria is False:
            return False

    if missao["chefe"]:
        c(" ")
        c(vermelho + " ☠︎  Um inimigo poderoso bloqueia seu caminho!" + RESET)
        chefe   = escalar_inimigo(missao["chefe"](), jogador.nivel)
        chefe.status()
        vitoria = iniciar_combate(jogador, chefe, reputacao)
        if vitoria is False:
            return False

    c(" ")
    c(amarelo + f" ✓ Missão '{missao['titulo']}' concluída!" + RESET)
    jogador.ganhar_exp(150 * missao["id"])
    return True

#MISSÕES SECUNDÁRIAS

def missao_taverna(jogador, reputacao, nome_porto="Nassau"):
    dados_dona = DONAS_TAVERNA.get(nome_porto, DONAS_TAVERNA["Nassau"])
    nome_dona  = dados_dona["nome"]

    c(" ")
    c(azul + f" 🍻 > A Taverna de {nome_porto}." + RESET)
    c(branco + " O cheiro de rum e fumaça te envolve assim que você entra." + RESET)
    c(branco + " Um velho marinheiro no canto te chama com um aceno." + RESET)
    time.sleep(1)

    attr_dona    = f"_dona_taverna_{nome_porto.replace(' ', '_').lower()}_falou"
    dona_ja_falou = getattr(jogador, attr_dona, False)

    c(" ")
    c(branco + " O que você faz?" + RESET)
    c(azul   + " 1 > Beber com o marinheiro" + RESET)
    c(azul   + " 2 > Jogar cartas com a tripulação" + RESET)
    if not dona_ja_falou:
        c(azul + f" 3 > Conversar com {nome_dona}  ✦ ela parece querer te dizer algo" + RESET)
    else:
        c(azul + f" 3 > Conversar com {nome_dona} [ela acena de longe com um sorriso cansado]" + RESET)
    escolha = ci("> ")

    if escolha == "1":
        c(" ")
        c(azul + " 🍻 Você bebe até quase cair! O marinheiro, agradecido, te dá um mapa velho." + RESET)
        jogador.inventario.append("Mapa Rasgado")
        c(azul + " 🗺 Item obtido: Mapa Rasgado" + RESET)
        jogador.ganhar_exp(30)

    elif escolha == "2":
        resultado = random.choice(["ganhou", "perdeu"])
        if resultado == "ganhou":
            c(" ")
            c(azul + " 🃁🂡🂱🃑 Você vence as cartas! A tripulação ri e te oferece uma aliança." + RESET)
            reputacao.adicionar_alianca("Tripulação da Taverna")
            jogador.ganhar_exp(40)
        else:
            c(" ")
            c(azul + " 🂡 Você perde feio. Mas um dos jogadores te passa um item." + RESET)
            jogador.inventario.append("Bússola Enferrujada")
            c(azul + " ✵ Item obtido: Bússola Enferrujada" + RESET)
            jogador.ganhar_exp(20)

    elif escolha == "3":
        if dona_ja_falou:
            c(branco + f" {nome_dona} te acena de longe com um sorriso cansado." + RESET)
            c(branco + " > Parece que não há mais histórias para contar desta vez." + RESET)
        else:
            c(azul + "─" * 40 + RESET)
            c(branco + f" {nome_dona} — Dona da Taverna de {nome_porto}" + RESET)
            c(azul + "─" * 40 + RESET)
            for linha in dados_dona["descricao"].split("\n"):
                c(branco + linha + RESET)
            time.sleep(1)

            for linha in dados_dona["fala"].split("\n"):
                c(branco + linha + RESET)
            time.sleep(1)

            item_dona = dados_dona["item"]
            jogador.inventario.append(item_dona)
            desc_item = ITENS_DIVERSOS_INFO.get(item_dona, {}).get("uso", "Item especial.")
            c(azul + f" 𐙚 Item obtido: {item_dona}" + RESET)
            c(azul + f" └ {desc_item}" + RESET)

            for linha in dados_dona["despedida"].split("\n"):
                c(branco + linha + RESET)

            reputacao.adicionar_alianca(dados_dona["alianca"])
            jogador.ganhar_exp(50)
            setattr(jogador, attr_dona, True)
    else:
        c(branco + " Você fica parado no canto observando. Nada acontece." + RESET)


def missao_saquear_navio(jogador, reputacao):
    c(vermelho + " ⚔ > Saquear Navio Mercante" + RESET)
    c(branco   + " Um navio mercante navega lento no horizonte." + RESET)
    c(azul     + " Você ordena o ataque!" + RESET)
    time.sleep(1)
    inimigo = escalar_inimigo(SoldadoNaval("Britânico"), jogador.nivel)
    vitoria = iniciar_combate(jogador, inimigo, reputacao)
    if vitoria:
        ouro = random.randint(50, 150)
        c(" ")
        c(amarelo + f" ⛃ Espólio saqueado: {ouro} moedas de ouro!" + RESET)
        jogador.ouro += ouro
        reputacao.adicionar_infamia(random.randint(3, 6))
        if reputacao.infamia >= 10:
            c(" ")
            c(vermelho + " ⚠︎ Uma fragata naval avistou o ataque e está vindo em sua direção!" + RESET)
            perseguicao = escalar_inimigo(OficialCoroa("Britânico"), jogador.nivel)
            iniciar_combate(jogador, perseguicao, reputacao)


def missao_explorar_ilha(jogador, reputacao):
    c(azul   + " 🏝 > Explorar Ilha Abandonada." + RESET)
    c(branco + " A ilha parece deserta, mas algo se move entre as árvores." + RESET)
    time.sleep(1)
    encontros = random.randint(5, 7)
    c(" ")
    c(branco + f" Você detecta {encontros} presença(s) na ilha." + RESET)
    for i in range(encontros):
        c(vermelho + f" 𓇢𓆸 Encontro {i+1}/{encontros}:" + RESET)
        inimigo = gerar_inimigo_comum(jogador.nivel)
        vitoria = iniciar_combate(jogador, inimigo, reputacao)
        if vitoria is False:
            return
    recompensa = random.choice([
        ("Rum Raro",               "🍻"),
        ("Mapa do Tesouro",        "🗺"),
        ("Amuleto Pirata",         "𓂀"),
        ("Moedas de Ouro Antigas", "⛃"),
    ])
    if recompensa[0] == "Moedas de Ouro Antigas":
        ouro_extra = random.randint(40, 100)
        jogador.ouro += ouro_extra
        c(" ")
        c(amarelo + f" ✧ Você encontrou um baú! {recompensa[1]} {ouro_extra} moedas de ouro antigas!" + RESET)
    else:
        c(" ")
        c(azul + f" ✧ Você encontrou um baú! Item obtido: {recompensa[1]} {recompensa[0]}" + RESET)
        jogador.inventario.append(recompensa[0])
    jogador.ganhar_exp(80)


def missao_duelo_deck(jogador, reputacao):
    c(vermelho + " ⚐ > Duelo no Deck." + RESET)
    c(branco   + " Um Capitão Rival desafia você para um duelo honrado." + RESET)
    c(" ")
    c(branco   + ' > "Só um de nós sai daqui de pé, seu cão sarnento!"' + RESET)
    time.sleep(1)
    inimigo = escalar_inimigo(CapitaoRival(), jogador.nivel)
    vitoria = iniciar_combate(jogador, inimigo, reputacao)
    if vitoria:
        reputacao.adicionar_infamia(2)
        reputacao.adicionar_alianca("Tripulação do Capitão Derrotado")
        c(amarelo + " 🎖 Sua reputação nos mares cresceu!" + RESET)


def missao_papagaio(jogador, reputacao):
    c(" ")
    c(ciano  + " 𓅪 > O Papagaio do Capitão." + RESET)
    c(branco + " Um velho pirata no canto da taverna está tentando se livrar de um papagaio." + RESET)
    c(branco + ' > "Esse maldito bicho não me deixa em paz!"' + RESET)
    time.sleep(1)
    c(" ")
    c(ciano + " O papagaio te olha com desconfiança." + RESET)
    c(ciano + ' 𓅪 "ARRR! %&$#?@!"' + RESET)
    time.sleep(1)
    c(" ")
    c(branco + " O que você faz?" + RESET)
    c(azul   + " 1 > Tentar ganhar a confiança do papagaio." + RESET)
    c(azul   + " 2 > Simplesmente pegar o papagaio no braço." + RESET)
    c(azul   + " 3 > Oferecer rum para o papagaio." + RESET)
    escolha = ci("\n> ")

    if escolha == "1":
        c(" ")
        c(ciano + ' 𓅪 "SOME DAQUI, SEU PATIFE! ARRR!"' + RESET)
        c(branco + " Você fica parado, firme, olhando nos olhos dele." + RESET)
        time.sleep(1)
        c(branco + " ..." + RESET)
        time.sleep(1)
        c(" ")
        c(ciano + ' 𓅪 "... mm.. Tudo bem!"' + RESET)
        c(ciano + " O papagaio pousa no seu ombro de má vontade." + RESET)
        c(azul  + " ✓ Pérola foi conquistada pela sua teimosia." + RESET)
    elif escolha == "2":
        c(" ")
        c(ciano + ' 𓅪 "QUE ABSURDO! FILHO DA %&$#?@!"' + RESET)
        c(branco + " Ele bica sua mão três vezes antes de aceitar o braço." + RESET)
        time.sleep(1)
        c(" ")
        c(ciano + ' 𓅪 "...tá bom.. estranho."' + RESET)
        c(azul  + " ✓ Pérola foi conquistada pela sua coragem (e dor)." + RESET)
        jogador.vida = max(1, jogador.vida - 2)
        c(vermelho + " 𖦹 Você perdeu 2 de vida pelas bicadas. Valeu a pena." + RESET)
    elif escolha == "3":
        resultado = random.choice(["aceitou", "jogou fora"])
        if resultado == "aceitou":
            c(ciano + ' 𓅪 "HMMMM... TUDO BEM, SEU BÊBADO."' + RESET)
            c(ciano + " O papagaio bebe o rum todo e pousa no seu ombro cantarolando algo impublicável." + RESET)
            c(azul  + " ✓ Pérola foi conquistada pelo rum." + RESET)
        else:
            c(ciano + ' 𓅪 "RUM BARATO?! QUE DESAFORO! VAI SE FERRAR!"' + RESET)
            c(ciano + " Ele joga o rum fora e te bica na orelha." + RESET)
            time.sleep(1)
            c(branco + " Mesmo assim, parece que decidiu que você é digno." + RESET)
            c(azul   + " ✓ Pérola foi conquistada por razões que só ela entende." + RESET)
            jogador.vida = max(1, jogador.vida - 1)
    else:
        c(branco + " Você recua. O papagaio ri. Literalmente." + RESET)
        c(ciano  + ' 𓅪 "COVARDE! ARRR! HA HA HA!"' + RESET)
        return

    time.sleep(1)
    c(" ")
    c(ciano + "── ⋆⋅☆⋅⋆ ──" + RESET)
    c(ciano + " 𓅪 PÉROLA ENTROU PARA O SEU GRUPO!" + RESET)
    c(ciano + "── ⋆⋅☆⋅⋆ ──" + RESET)
    c(" ")
    c(branco + " > Pérola é uma companheira especial." + RESET)
    c(branco + " > Ela não luta, mas intimida inimigos antes do combate," + RESET)
    c(branco + "   dando a você uma chance de ataque surpresa." + RESET)
    c(" ")
    c(amarelo + " > Habilidade desbloqueada: ✶ ATAQUE SURPRESA" + RESET)
    c(amarelo + "   → 30% de chance de dar dano duplo no primeiro turno." + RESET)
    c(" ")
    c(ciano + " > •ﻌ• EASTER EGG: Interaja com a Pérola 3 vezes seguidas no inventário" + RESET)
    c(ciano + "   para descobrir o que acontece... se ousar." + RESET)
    c(" ")
    jogador.inventario.append("Pérola 𓅪")
    jogador.habilidades.append("ataque_surpresa")
    jogador.ganhar_exp(60)
    reputacao.adicionar_alianca("Pérola")
    time.sleep(1)
    c(ciano + ' 𓅪 "NÃO ACHA QUE SOMOS AMIGOS, SEU VERME. ARRR."' + RESET)

#LOJA PRINCIPAL:

def visitar_loja(jogador, nome_porto="Porto de Nassau"):
    while True:
        c(azul + f" 🛍  Loja do {nome_porto}" + RESET)
        c(amarelo + f" ⛃ Seu ouro: {jogador.ouro}" + RESET)
        c(" ")

        itens_cura_porto = LOJA_POR_PORTO.get(nome_porto, {})

        c(azul + " ╔─────────────────────────────────────────────╗" + RESET)
        c(azul + "   ✚  Itens de Cura" + RESET)
        c(azul + " ╠─────────────────────────────────────────────╣" + RESET)
        lista_cura = list(itens_cura_porto.items())
        for i, (nome, dados) in enumerate(lista_cura, 1):
            preco = dados["preco"]
            desc  = dados["descricao"]
            pode  = verde + "✓" + RESET if jogador.ouro >= preco else vermelho + "✗" + RESET
            c(f"   {i:2}. " + branco + f"{nome:<26}" + RESET + f" {amarelo}{preco:>3} ⛃{RESET} {pode}")
            c(azul + f"       └ {desc}" + RESET)

        lista_pactuario = []
        if jogador.classe == "Pactuário":
            itens_pact_porto = LOJA_PACTUARIO_POR_PORTO.get(nome_porto, {})
            if itens_pact_porto:
                c(roxo + " ╠─────────────────────────────────────────────╣" + RESET)
                c(roxo + "   ๋࣭ ⭑⚝  Itens do Pactuário (exclusivos)" + RESET)
                c(roxo + " ╠─────────────────────────────────────────────╣" + RESET)
                offset = len(lista_cura)
                lista_pactuario = list(itens_pact_porto.items())
                for j, (nome, dados) in enumerate(lista_pactuario, offset + 1):
                    preco = dados["preco"]
                    desc  = dados["descricao"]
                    pode  = verde + "✓" + RESET if jogador.ouro >= preco else vermelho + "✗" + RESET
                    c(f"   {j:2}. " + branco + f"{nome:<26}" + RESET + f" {amarelo}{preco:>3} ⛃{RESET} {pode}")
                    c(roxo + f"       └ {desc}" + RESET)

        total_itens = len(lista_cura) + len(lista_pactuario)
        op_vender = total_itens + 1
        op_sair   = total_itens + 2

        c(amarelo + f"   {op_vender}. 🗡 Vender arma antiga" + RESET)
        c(azul    + f"   {op_sair}. ← Voltar ao porto" + RESET)

        cor_final = roxo if jogador.classe == "Pactuário" and lista_pactuario else azul
        c(cor_final + " ╚─────────────────────────────────────────────╝" + RESET)

        escolha = ci("> ")
        try:
            escolha = int(escolha)
        except ValueError:
            c(vermelho + " Opção inválida." + RESET)
            continue

        if escolha == op_sair:
            c(azul + "\n ⚓︎ Até logo, pirata!" + RESET)
            break

        elif escolha == op_vender:
            vender_arma(jogador)

        elif 1 <= escolha <= len(lista_cura):
            nome_item, dados = lista_cura[escolha - 1]
            preco = dados["preco"]
            if jogador.ouro >= preco:
                jogador.ouro -= preco
                jogador.inventario.append(nome_item)
                c(" ")
                c(azul + f" ✓ {nome_item} comprado! ⛃ Ouro restante: {jogador.ouro}" + RESET)
            else:
                c(" ")
                c(vermelho + f" ✗ Ouro insuficiente! Faltam {preco - jogador.ouro} moedas." + RESET)

        elif lista_pactuario and len(lista_cura) < escolha <= total_itens:
            idx = escolha - len(lista_cura) - 1
            nome_item, dados = lista_pactuario[idx]
            preco = dados["preco"]
            if jogador.ouro >= preco:
                jogador.ouro -= preco
                jogador.inventario.append(nome_item)
                c(" ")
                c(roxo + f" ✓ {nome_item} comprado! ⛃ Ouro restante: {jogador.ouro}" + RESET)
            else:
                c(" ")
                c(vermelho + f" ✗ Ouro insuficiente! Faltam {preco - jogador.ouro} moedas." + RESET)
        else:
            c(vermelho + " Opção inválida." + RESET)


def vender_arma(jogador):
    armas_no_inventario = [
        item for item in jogador.inventario
        if any(item == a["nome"] for a in ARMAS_POR_CLASSE.get(jogador.classe, []))
        and item != jogador.arma_equipada["nome"]
    ]
    if not armas_no_inventario:
        c(" ")
        c(vermelho + " ⚠︎ Você não tem armas antigas para vender." + RESET)
        return
    c(" ")
    c(amarelo + " 🗡 Armas disponíveis para venda:" + RESET)
    for i, arma in enumerate(armas_no_inventario, 1):
        arma_info = next(a for a in ARMAS_POR_CLASSE[jogador.classe] if a["nome"] == arma)
        valor     = arma_info.get("preco_venda", max(10, arma_info["bonus_dano"] * 3))
        c(amarelo + f"   {i}. {arma} [{arma_info['tier']}] — {valor} ouro" + RESET)
    c(azul + "   0. Cancelar" + RESET)
    c(" ")
    escolha = ci(" Escolha para vender: ")
    try:
        escolha = int(escolha)
        if escolha == 0:
            return
        if 1 <= escolha <= len(armas_no_inventario):
            arma_vendida = armas_no_inventario[escolha - 1]
            arma_info    = next(a for a in ARMAS_POR_CLASSE[jogador.classe] if a["nome"] == arma_vendida)
            valor        = arma_info.get("preco_venda", max(10, arma_info["bonus_dano"] * 3))
            jogador.inventario.remove(arma_vendida)
            jogador.ouro += valor
            c(amarelo + f" ⛃ {arma_vendida} vendida por {valor} moedas! Ouro atual: {jogador.ouro}" + RESET)
        else:
            c(vermelho + " Opção inválida." + RESET)
    except ValueError:
        c(azul + " Cancelado." + RESET)

#Eventos aleátorios durante viagens no mar:

EVENTOS_MAR = [
    {
        "id": "naufragio",
        "titulo": "Naufrágio à Vista",
        "descricao": (
            " 𓆝 As ondas trazem destroços. Um navio naufragado boia no horizonte.\n"
            " Algo brilha entre os escombros..."
        ),
        "tipo": "tesouro",
    },
    {
        "id": "comerciante",
        "titulo": "Comerciante Flutuante",
        "descricao": (
            "𓊝 Uma jangada colorida se aproxima. Um homem de chapéu enorme acena.\n"
            " 'Ei! Compra alguma coisa, capitão? Tô no meio do oceano por um motivo!'"
        ),
        "tipo": "loja",
    },
    {
        "id": "tempestade",
        "titulo": "Tempestade Repentina",
        "descricao": (
            "⛈ O céu escurece em segundos. Ondas enormes sacudem o navio.\n"
            " A tripulação grita. Você agarra o leme com força."
        ),
        "tipo": "perigo",
    },
    {
        "id": "garrafa",
        "titulo": "Garrafa no Mar",
        "descricao": (
            " 𓆞 Uma garrafa lacrada boia perto do casco.\n"
            " Dentro há um bilhete dobrado e algo mais pesado..."
        ),
        "tipo": "tesouro",
    },
    {
        "id": "sereia_canto",
        "titulo": "Canto das Sereias",
        "descricao": (
            "♫ Uma melodia estranha vem das rochas. Bela demais para ser natural.\n"
            " Sereias. Você as reconhece — mas o canto ainda puxa sua mente."
        ),
        "tipo": "combate",
    },
    {
        "id": "navio_fantasma",
        "titulo": "Navio Sem Bandeira",
        "descricao": (
            "☠︎ Um navio escurecido surge no nevoeiro sem fazer ruído.\n"
            " Nenhuma bandeira. Nenhuma luz. Mas algo se move no convés."
        ),
        "tipo": "combate",
    },
    {
        "id": "ilha_secreta",
        "titulo": "Ilha Não Mapeada",
        "descricao": (
            "🏝 Uma ilha minúscula aparece onde o mapa diz que não há nada.\n"
            " Fumaça sobe de dentro da mata. Alguém esteve aqui recentemente."
        ),
        "tipo": "tesouro",
    },
    {
        "id": "pirata_amigo",
        "titulo": "Pirata Solitário",
        "descricao": (
            "𓊝 Um pequeno barco se aproxima com uma bandeira branca.\n"
            " Um pirata envelhecido acena. 'Faz tempo que não vejo alma viva!'"
        ),
        "tipo": "aliado",
    },
]


def _evento_tesouro(jogador, evento_id):
    if evento_id == "naufragio":
        ouro = random.randint(30, 90)
        itens_possiveis = ["Poção de Vida", "Rum do Pirata", "Mapa Rasgado", "Bússola Enferrujada"]
        item = random.choice(itens_possiveis)
        jogador.ouro += ouro
        jogador.inventario.append(item)
        c(azul    + f" 𐙚 Você vasculha os destroços e encontra {ouro} moedas e {item}!" + RESET)
        c(amarelo + f" ⛃ Ouro total: {jogador.ouro}" + RESET)

    elif evento_id == "garrafa":
        resultado = random.choice(["ouro", "item", "exp"])
        if resultado == "ouro":
            ouro = random.randint(20, 60)
            jogador.ouro += ouro
            c(azul    + f" ✦ O bilhete é um mapa parcial. Junto havia {ouro} moedas!" + RESET)
            c(amarelo + f" ⛃ Ouro total: {jogador.ouro}" + RESET)
        elif resultado == "item":
            item = random.choice(["Poção de Vida", "Amuleto Pirata", "Mapa do Tesouro"])
            jogador.inventario.append(item)
            c(azul + f" ✦ O bilhete é ilegível, mas dentro havia: {item}!" + RESET)
        else:
            jogador.ganhar_exp(50)
            c(azul + " ✦ O bilhete contém coordenadas e segredos náuticos. Você aprende algo valioso." + RESET)

    elif evento_id == "ilha_secreta":
        c(azul + " > Você desembarca cautelosamente..." + RESET)
        time.sleep(1)
        resultado = random.choice(["bau", "emboscada_leve"])
        if resultado == "bau":
            ouro = random.randint(50, 120)
            jogador.ouro += ouro
            item = random.choice(["Grande Poção de Vida", "Elixir Antigo", "Mapa do Tesouro"])
            jogador.inventario.append(item)
            c(amarelo + f" ✧ Você encontra um baú enterrado! {ouro} moedas + {item}!" + RESET)
            c(amarelo + f" ⛃ Ouro total: {jogador.ouro}" + RESET)
        else:
            c(vermelho + " ⚠︎ Era uma armadilha! Alguém vigiava o lugar." + RESET)
            c(azul     + " > Você consegue fugir, mas perde tempo e fôlego." + RESET)
            jogador.vida = max(1, jogador.vida - 10)
            c(vermelho + f" ❤︎  Vida: {jogador.vida}/{jogador.vida_maxima}" + RESET)


def _evento_loja(jogador):
    c(azul + " > O comerciante abre uma caixa amassada cheia de itens." + RESET)
    c(" ")

    itens_comerciante = {
        "Poção de Vida":         ITENS_CURA["Poção de Vida"],
        "Grande Poção de Vida":  ITENS_CURA["Grande Poção de Vida"],
        "Rum do Pirata":         ITENS_CURA["Rum do Pirata"],
        "Elixir Antigo":         ITENS_CURA["Elixir Antigo"],
    }

    while True:
        c(azul    + f" 🛍  Comerciante Flutuante | " + RESET + amarelo + f"⛃ Seu ouro: {jogador.ouro}" + RESET)
        lista = list(itens_comerciante.items())
        for i, (nome, dados) in enumerate(lista, 1):
            pode = verde + "✓" + RESET if jogador.ouro >= dados["preco"] else vermelho + "✗" + RESET
            c(f"   {i}. " + branco + f"{nome:<28}" + RESET + f" {amarelo}{dados['preco']:>3} ⛃{RESET} {pode}")
            c(azul + f"      └ {dados['descricao']}" + RESET)
        c(azul + "   0. Dispensar o comerciante" + RESET)

        escolha = ci("> ")
        try:
            escolha = int(escolha)
        except ValueError:
            c(vermelho + " Opção inválida." + RESET)
            continue

        if escolha == 0:
            c(branco + " > 'Até a próxima, capitão! Se o mar não me engolir!'" + RESET)
            break
        elif 1 <= escolha <= len(lista):
            nome_item, dados = lista[escolha - 1]
            if jogador.ouro >= dados["preco"]:
                jogador.ouro -= dados["preco"]
                jogador.inventario.append(nome_item)
                c(azul + f" ✓ {nome_item} comprado! ⛃ Ouro restante: {jogador.ouro}" + RESET)
            else:
                c(vermelho + f" ✗ Ouro insuficiente! Faltam {dados['preco'] - jogador.ouro} moedas." + RESET)
        else:
            c(vermelho + " Opção inválida." + RESET)


def _evento_perigo(jogador):
    c(" ")
    c(branco + " O que você faz?" + RESET)
    c(azul + " 1 > Enfrentar a tempestade de frente" + RESET)
    c(azul + " 2 > Tentar desviar pelo sul" + RESET)
    c(azul + " 3 > Ancorar e esperar passar" + RESET)
    escolha = ci("> ")

    if escolha == "1":
        dano = random.randint(15, 35)
        jogador.vida = max(1, jogador.vida - dano)
        ouro_bonus = random.randint(10, 40)
        jogador.ouro += ouro_bonus
        c(vermelho + f" 𖦹 A tempestade castiga o navio! -{dano} de vida." + RESET)
        c(amarelo  + f" ✦ Mas você manteve o rumo e ganhou {ouro_bonus} moedas de espólio flutuante!" + RESET)
        c(vermelho + f" ❤︎  Vida: {jogador.vida}/{jogador.vida_maxima}" + RESET)
    elif escolha == "2":
        if random.random() < 0.6:
            c(azul + " ༄ Você encontra uma rota tranquila. A tempestade passa longe." + RESET)
            jogador.ganhar_exp(20)
        else:
            dano = random.randint(8, 20)
            jogador.vida = max(1, jogador.vida - dano)
            c(vermelho + f" ✗ O desvio foi tarde demais. -{dano} de vida." + RESET)
            c(vermelho + f" ❤︎  Vida: {jogador.vida}/{jogador.vida_maxima}" + RESET)
    else:
        c(azul + " ⚓︎ Você ancora num recife e aguarda. A tempestade some em horas." + RESET)
        c(branco + " > Nenhum dano, mas você perdeu tempo e oportunidades." + RESET)


def _evento_aliado(jogador, reputacao):
    c(azul + " > O velho pirata oferece rum e começa a falar..." + RESET)
    time.sleep(1)
    resultado = random.choice(["dica", "alianca", "item"])
    if resultado == "dica":
        dicas = [
            "'O Elixir Antigo é vendido em Cartagena e Lisboa. Vale cada moeda.'",
            "'Cuidado com a Rota dos Condenados — leve itens de cura. Muitos.'",
            "'Comerciantes às vezes aparecem no meio do mar. Fique de olho.'",
            "'Porto de Lisboa tem os melhores itens. Mas a viagem custa 15 moedas.'",
        ]
        c(branco + f" 𓆝 {random.choice(dicas)}" + RESET)
        jogador.ganhar_exp(25)
    elif resultado == "alianca":
        reputacao.adicionar_alianca("O Velho Pirata do Mar Aberto")
        jogador.ganhar_exp(40)
        c(azul + " > Ele aperta sua mão com força. 'Se precisar de alguém no mar, grite meu nome.'" + RESET)
    else:
        item = random.choice(["Rum do Pirata", "Poção de Vida", "Bússola Enferrujada"])
        jogador.inventario.append(item)
        c(azul + f" 𐙚 Ele enfia um item na sua mão antes de remar de volta ao horizonte: {item}!" + RESET)


def evento_aleatorio_mar(jogador, reputacao):
    if random.random() > 0.55:
        return

    evento = random.choice(EVENTOS_MAR)

    c(" ")
    c(azul + "~" * 35 + RESET)
    c(azul + f" 𓆝 Evento no mar: {evento['titulo']}" + RESET)
    c(azul + "~" * 35 + RESET)
    for linha in evento["descricao"].split("\n"):
        c(branco + linha + RESET)
    c(" ")
    time.sleep(1)

    tipo = evento["tipo"]

    if tipo == "tesouro":
        _evento_tesouro(jogador, evento["id"])
    elif tipo == "loja":
        _evento_loja(jogador)
    elif tipo == "perigo":
        _evento_perigo(jogador)
    elif tipo == "combate":
        if evento["id"] == "sereia_canto":
            c(vermelho + " > Você resiste ao canto e parte para o ataque!" + RESET)
            inimigo = escalar_inimigo(Sereia(), jogador.nivel)
        else:
            c(vermelho + " > Você ordena que a tripulação se prepare para o abordagem!" + RESET)
            inimigo = escalar_inimigo(random.choice([NavegadorEspectral, CapitaoAmaldicado, CorsarioMeioPeixe])(), jogador.nivel)
        iniciar_combate(jogador, inimigo, reputacao)
    elif tipo == "aliado":
        _evento_aliado(jogador, reputacao)

    c(" ")


def entrar_porto(nome_porto, jogador, reputacao):
    dados_porto = PORTOS[nome_porto]
    nacao       = dados_porto["nacao"]
    custo       = dados_porto["custo_viagem"]

    if custo > 0:
        c(azul + f" ⚓︎ Viagem para o {nome_porto} [{nacao}] custa {custo} moedas." + RESET)
        if jogador.ouro < custo:
            c(vermelho + f" ✗ Ouro insuficiente! Você tem {jogador.ouro} moedas." + RESET)
            return False
        confirmar = ci(f" Pagar {custo} moedas para viajar? (s/n): ")
        if confirmar.lower() != "s":
            c(azul + " Viagem cancelada." + RESET)
            return False
        jogador.ouro -= custo
        c(amarelo + f" ⛃ Pago! Ouro restante: {jogador.ouro}" + RESET)

    if custo > 0:
        c(azul + f"\n ♒︎ Navegando para {nome_porto}..." + RESET)
        time.sleep(1)
        evento_aleatorio_mar(jogador, reputacao)

    c(azul + f" ⚓︎ Você chegou ao {nome_porto} [{nacao}]." + RESET)

    if reputacao.infamia >= 10:
        c(vermelho + f" ⚠︎ Soldados {nacao}s reconheceram você! Prepare-se para lutar!" + RESET)
        inimigo   = escalar_inimigo(SoldadoNaval(nacao), jogador.nivel)
        resultado = iniciar_combate(jogador, inimigo, reputacao)
        if resultado is None:
            c(azul + " ༄ Você se esgueira pelo porto depois de fugir." + RESET)
        return resultado is not False
    else:
        c(azul + " (ᵕ— —) Ninguém te reconhece. Você entra sem problemas." + RESET)
        return True

#MENU - VER CLASSES

def ver_classes():
    c(" ")
    c(azul + """
   ╭───────────-·-ˋˏ-༻𖤓༺-ˎˊ-·-───────────╮
""" + RESET)
    c(azul + "     ⌯⁍ Atirador" + RESET)
    c(branco + "        > Ataques à distância" + RESET)
    c(vermelho + "        Vida: 80  | Dano: 22" + RESET + azul + " | Stamina: 90" + RESET)
    c(" ")
    c(azul + "     🗡 Corsário" + RESET)
    c(branco + "        > Equilibrado e feroz" + RESET)
    c(vermelho + "        Vida: 100 | Dano: 18" + RESET + azul + " | Stamina: 80" + RESET)
    c(" ")
    c(azul + "    ✷ Bombardeiro" + RESET)
    c(branco + "       > Mestre de explosivos" + RESET)
    c(vermelho + "       Vida: 90  | Dano: 25" + RESET + azul + " | Stamina: 60" + RESET)
    c(" ")
    c(roxo + "   ⭑⚝ Pactuário" + RESET)
    c(branco + "       > Poderes das sombras" + RESET)
    c(vermelho + "       Vida: 75  | Dano: 20" + RESET + roxo + " | Stamina: 100" + RESET)
    c(roxo + "       + Loja exclusiva. ദ്ദി◝ ⩊ ◜.ᐟ" + RESET)
    c(" ")
    c(azul + "   ⋆˚࿔ Pesquisador" + RESET)
    c(branco + "      > Inteligência é força" + RESET)
    c(vermelho + "      Vida: 85  | Dano: 12" + RESET + azul + " | Stamina: 95" + RESET)
    c(" ")
    c(azul + "    ⚔︎ Espadachim" + RESET)
    c(branco + "      > Mestre das lâminas" + RESET)
    c(vermelho + "      Vida: 95  | Dano: 20" + RESET + azul + " | Stamina: 85" + RESET)
    c(" ")
    c(azul + """   ╰───────────-·-ˋˏ-༻𖤓༺-ˎˊ-·-───────────╯
""" + RESET)

#MENU - ESCOLHA SUA CLASSE:

def escolher_classe(nome):
    c(branco + """
╔───────────────────────────╗
│     Escolha sua classe    │
╠───────────────────────────╣
│  1 >  Atirador            │
│  2 >  Corsário            │
│  3 >  Bombardeiro         │
│  4 >  Pactuário           │
│  5 >  Pesquisador         │
│  6 >  Espadachim          │
╚───────────────────────────╝
""" + RESET)

    c(" ")
    escolha = ci("Digite o número da classe: ")
    classes = {
        "1": (Atirador,    branco + "⌯⁍  Atirador selecionado!"    + RESET),
        "2": (Corsario,    branco + "🗡  Corsário selecionado!"     + RESET),
        "3": (Bombardeiro, branco + "✷  Bombardeiro selecionado!"  + RESET),
        "4": (Pactuario,   roxo   + ".⭑⚝  Pactuário selecionado!" + RESET),
        "5": (Pesquisador, branco + "⋆˚࿔  Pesquisador selecionado!" + RESET),
        "6": (Espadachim,  branco + "⚔︎   Espadachim selecionado!"  + RESET),
    }

    if escolha in classes:
        Classe, mensagem = classes[escolha]
        jogador = Classe(nome)
        c(" ")
        c(mensagem)
        c("·༻𐫱༺·")
        c(" ")
    else:
        c(vermelho + " Escolha inválida! Criando Espadachim padrão." + RESET)
        jogador = Espadachim(nome)

    jogador.status()
    return jogador

#LOADING:

def loading():
    c(" ")
    largura = _largura()
    msg = " Iniciando Baía do Homem Morto"
    pad = max(0, (largura - len(msg) - 3) // 2)
    print(" " * pad + vermelho + msg, end="", flush=True)
    for _ in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print(RESET)
    c(" ")
    c(vermelho + " Jogo iniciado!" + RESET)
    c(" ")

#MENU E LOOP PRINCIPAL:

def _menu_missoes_principais(jogador, reputacao, missoes_concluidas):
    missao_7_concluida = 7 in missoes_concluidas
    rota_concluida     = "rota_dos_condenados" in missoes_concluidas

    c(" ")
    c(azul + "╔───────────────────────────╗" + RESET)
    c(azul + "    Missões Principais 𓊝    " + RESET)
    c(azul + "╚───────────────────────────╝" + RESET)

    for m in MISSOES_PRINCIPAIS:
        concluida  = m["id"] in missoes_concluidas
        disponivel = jogador.nivel >= m["nivel_minimo"]

        if concluida:
            status = amarelo + "✓" + RESET
        elif disponivel:
            status = azul + "ꗃ" + RESET
        else:
            status = vermelho + f"🔒︎ Nv{m['nivel_minimo']}" + RESET

        titulo_curto = m["titulo"][:22]
        c(branco + f" {m['id']}. {titulo_curto:<23}" + RESET + f" {status}")

    if rota_concluida:
        c(branco + " 8. A Rota dos Condenados " + RESET + amarelo + "✓" + RESET)
    elif missao_7_concluida:
        c(branco + " 8. A Rota dos Condenados " + RESET + azul + "ꗃ DISP." + RESET)
    else:
        c(branco + " 8. A Rota dos Condenados " + RESET + vermelho + "🔒︎ Nv.17" + RESET)

    c(" ")
    numero = ci("Escolha o número da missão (ou Enter para voltar): ")
    if numero == "":
        return

    if numero == "8":
        if not missao_7_concluida:
            c(vermelho + " 🔒︎ Conclua a missão 7 primeiro." + RESET)
        elif rota_concluida:
            c(amarelo + " ✓ Você já percorreu esse caminho." + RESET)
        else:
            resultado = rota_dos_condenados(jogador, reputacao)
            if resultado:
                missoes_concluidas.append("rota_dos_condenados")
        return

    try:
        numero = int(numero)
    except ValueError:
        return

    missao = next((m for m in MISSOES_PRINCIPAIS if m["id"] == numero), None)
    if not missao:
        c(vermelho + " Missão não encontrada." + RESET)
        return
    if numero in missoes_concluidas:
        c(amarelo + " ✓ Você já concluiu esta missão." + RESET)
        return
    if numero > 1 and (numero - 1) not in missoes_concluidas:
        missao_anterior = next((m for m in MISSOES_PRINCIPAIS if m["id"] == numero - 1), None)
        nome_anterior   = missao_anterior["titulo"] if missao_anterior else f"missão {numero - 1}"
        c(vermelho + f" 🔒︎ Conclua '{nome_anterior}' primeiro." + RESET)
        return

    sucesso = iniciar_missao_principal(missao, jogador, reputacao)
    if sucesso:
        missoes_concluidas.append(numero)
        c(" ")
        c(amarelo + f" ✮⋆˙ Missão '{missao['titulo']}' adicionada ao seu progresso!" + RESET)
        c(" ")


def _menu_missoes_secundarias(jogador, reputacao):
    while True:
        c(branco + """
╔─────────────────────────────────╗
│       Missões Secundárias       │
╠─────────────────────────────────╣
│  1 > Saquear Navio Mercante     │
│  2 > Explorar Ilha Abandonada   │
│  3 > Duelo no Deck              │
│  4 > O Papagaio do Cap. Morto   │
│  5 > Voltar                     │
╚─────────────────────────────────╝
        """ + RESET)

        sub = ci("> ")
        if sub == "1":
            missao_saquear_navio(jogador, reputacao)
        elif sub == "2":
            missao_explorar_ilha(jogador, reputacao)
        elif sub == "3":
            missao_duelo_deck(jogador, reputacao)
        elif sub == "4":
            if "Pérola 𓅪" in jogador.inventario:
                c(ciano + ' 𓅪 "JÁ ESTOU AQUI, SEU BURRO!"' + RESET)
            else:
                missao_papagaio(jogador, reputacao)
        elif sub == "5":
            break
        else:
            c(vermelho + " Opção inválida." + RESET)


def _menu_porto(jogador, reputacao, ultimo_porto, portos_visitados):
    c(azul + " ⚓︎ Portos Disponíveis:" + RESET)
    c(" ")
    portos = list(PORTOS.keys())
    for i, porto in enumerate(portos, 1):
        dados     = PORTOS[porto]
        nacao     = dados["nacao"]
        custo     = dados["custo_viagem"]
        atual     = amarelo + " ← atual" + RESET if porto == ultimo_porto else ""
        custo_str = verde + "Gratuito" + RESET if custo == 0 else amarelo + f"{custo} moedas" + RESET
        c(f"  {i}. " + branco + f"{porto} [{nacao}]" + RESET + f" — Viagem: {custo_str}{atual}")

    c(" ")
    c("༺𓆩⚓︎𓆪༻")
    c(" ")
    escolha = ci("Escolha um porto (ou Enter para voltar): ")
    c(" ")
    try:
        escolha         = int(escolha)
        porto_escolhido = portos[escolha - 1]
    except (ValueError, IndexError):
        return ultimo_porto

    sucesso = entrar_porto(porto_escolhido, jogador, reputacao)
    if not sucesso:
        return ultimo_porto

    if porto_escolhido not in portos_visitados:
        portos_visitados.add(porto_escolhido)
        executar_missao_porto(porto_escolhido, jogador, reputacao)

    while True:
        nome_curto = porto_escolhido.replace("Porto de ", "")
        dados_dona = DONAS_TAVERNA.get(nome_curto, DONAS_TAVERNA["Nassau"])

        c(" ")
        c(azul + f" ⚓︎ {porto_escolhido}" + RESET)
        c(vermelho + f" ⛃ Ouro: {jogador.ouro}" + RESET + vermelho + f" | ❤︎  Vida: {jogador.vida}/{jogador.vida_maxima}" + RESET)
        c(azul + f" 1 > 🛍  Visitar a Loja" + RESET)
        c(azul + f" 2 > 🍻 Ir à Taverna  (Dona: {dados_dona['nome']})" + RESET)
        c(azul + f" 3 > 𝗓𐰁𐰁 Descansar (recupera vida total — custa 20 ouro)" + RESET)
        c(azul + f" 4 > ༄ Partir" + RESET)
        acao = ci("> ")

        if acao == "1":
            visitar_loja(jogador, porto_escolhido)

        elif acao == "2":
            missao_taverna(jogador, reputacao, nome_curto)

        elif acao == "3":
            if jogador.ouro >= 20:
                jogador.ouro    -= 20
                jogador.vida     = jogador.vida_maxima
                #Descanso também restaura stamina
                jogador.stamina  = jogador.stamina_maxima
                c(azul    + " 𝗓𐰁𐰁 Você descansa e recupera toda a vida e stamina!" + RESET)
                c(vermelho + f" ❤︎  Vida: {jogador.vida}/{jogador.vida_maxima}" + RESET)
                cor_st = roxo if jogador.classe == "Pactuário" else azul
                c(cor_st + f" 🗲  Stamina: {jogador.stamina}/{jogador.stamina_maxima}" + RESET)
                c(amarelo + f" ⛃ Ouro: {jogador.ouro}" + RESET)
            else:
                c(vermelho + " ✗ Ouro insuficiente para descansar. (Precisa de 20 moedas)" + RESET)

        elif acao == "4":
            c(azul + f" ༄ Você parte do {porto_escolhido}. Boa viagem!" + RESET)
            break

        else:
            c(vermelho + " Opção inválida." + RESET)

    return porto_escolhido


def _ver_inventario(jogador):
    while True:
        c(" ")
        c(azul + " > Inventário." + RESET)
        if not jogador.inventario:
            c(branco + " Vazio." + RESET)
            return

        armas          = [i for i in jogador.inventario if any(i == a["nome"] for a in ARMAS_POR_CLASSE.get(jogador.classe, []))]
        itens_cura_inv = [i for i in jogador.inventario if i in ITENS_CURA]
        itens_magicos  = [i for i in jogador.inventario if i in ITENS_PACTUARIO]
        outros         = [i for i in jogador.inventario if i not in armas + itens_cura_inv + itens_magicos]

        todos_usaveis = []

        if armas:
            c(amarelo + " 🗡 Armas:" + RESET)
            for a in armas:
                equipada = amarelo + " ← equipada" + RESET if a == jogador.arma_equipada["nome"] else ""
                c(branco + f"   · {a}" + RESET + equipada)

        if itens_cura_inv:
            c(azul + " ✚ Itens de Cura:" + RESET)
            for i in itens_cura_inv:
                desc = ITENS_CURA[i]["descricao"]
                todos_usaveis.append(i)
                c(azul + f"   [{len(todos_usaveis)}] · {i}" + RESET + branco + f" — {desc}" + RESET)

        if itens_magicos:
            c(roxo + "  ๋࣭ ⭑⚝ Itens Mágicos (Pactuário):" + RESET)
            for i in itens_magicos:
                desc = ITENS_PACTUARIO[i]["descricao"]
                todos_usaveis.append(i)
                c(roxo + f"   [{len(todos_usaveis)}] · {i}" + RESET + branco + f" — {desc}" + RESET)

        if outros:
            c(azul + "\n ッ Outros:" + RESET)
            for i in outros:
                if i == "Pérola 𓅪":
                    todos_usaveis.append(i)
                    c(ciano + f"   [{len(todos_usaveis)}] · 𓅪 Pérola" + RESET + branco + " — sua companheira. Interaja com ela... se ousar." + RESET)
                elif i in ITENS_DIVERSOS_INFO:
                    desc = ITENS_DIVERSOS_INFO[i].get("uso", "Item especial.")
                    todos_usaveis.append(i)
                    c(azul + f"   [{len(todos_usaveis)}] · {i}" + RESET + branco + f" — {desc}" + RESET)
                else:
                    c(branco + f"   · {i}" + RESET)

        c(" ")
        c(azul + " [U] Usar/Interagir com item" + RESET)
        c(azul + " [V] Voltar ao menu" + RESET)
        c(" ")
        op = ci("> ").strip().upper()

        if op == "V" or op == "":
            break
        elif op == "U":
            if not todos_usaveis:
                c(vermelho + " Nenhum item utilizável no inventário." + RESET)
                continue
            c(branco + " Qual item usar? (número ou Enter para cancelar)" + RESET)
            try:
                idx = int(ci("> "))
                if 1 <= idx <= len(todos_usaveis):
                    nome_item = todos_usaveis[idx - 1]
                    if nome_item == "Pérola 𓅪":
                        interagir_com_perola(jogador)
                    else:
                        jogador.usar_item(nome_item)
                else:
                    c(vermelho + " Índice inválido." + RESET)
            except ValueError:
                c(azul + " Cancelado." + RESET)
        else:
            c(vermelho + " Opção inválida." + RESET)


def _ver_progresso(jogador, missoes_concluidas, reputacao):
    c(" ")
    c(azul + " 🗺 > Progresso da Jornada." + RESET)
    for m in MISSOES_PRINCIPAIS:
        icone = amarelo + "✓" + RESET if m["id"] in missoes_concluidas else branco + "⬜" + RESET
        c(f"  {icone} " + branco + f"{m['id']}. {m['titulo']}" + RESET)
    rota_ok = "rota_dos_condenados" in missoes_concluidas
    c(f"  {amarelo + '✓' + RESET if rota_ok else branco + '⬜' + RESET}  " + branco + " A Rota dos Condenados" + RESET)
    concluidas = len([m for m in missoes_concluidas if isinstance(m, int)])
    c(azul    + f" 📜 Progresso: {concluidas}/{len(MISSOES_PRINCIPAIS)} missões principais" + RESET)
    c(amarelo + f" ⤴︎ Nível: {jogador.nivel}/25" + RESET)
    c(amarelo + f" ⛃ Ouro acumulado: {jogador.ouro}" + RESET)
    reputacao.status()

#LOOP PRINCIPAL:

def loop_principal(jogador, reputacao):
    missoes_concluidas = []
    ultimo_porto       = "Porto de Nassau"
    portos_visitados   = set()

    while True:
        c(branco + "═" * 40 + RESET)
        c(branco + f" ☠  {jogador.nome}" + RESET + azul + f" | Nível {jogador.nivel}" + RESET + amarelo + f" | ⛃  {jogador.ouro} ouro" + RESET)
        c(vermelho + f" ❤︎  Vida: {jogador.vida}/{jogador.vida_maxima}" + RESET + azul + f" | ⟟ {ultimo_porto}" + RESET)
        c(branco + "═" * 40 + RESET)
        c(" ")
        c(branco + """
╔────────────────────────────╗
│   O que você quer fazer?   │
╠────────────────────────────╣
│  1 > Missões Principais    │
│  2 > Missões Secundárias   │
│  3 > Visitar Porto         │
│  4 > Ver Status            │
│  5 > Ver Inventário        │
│  6 > Ver Progresso         │
│  7 > Sair do Jogo          │
╚────────────────────────────╝
        """ + RESET)

        escolha = ci("> ")

        if escolha == "1":
            _menu_missoes_principais(jogador, reputacao, missoes_concluidas)
        elif escolha == "2":
            _menu_missoes_secundarias(jogador, reputacao)
        elif escolha == "3":
            ultimo_porto = _menu_porto(jogador, reputacao, ultimo_porto, portos_visitados)
        elif escolha == "4":
            jogador.status()
            reputacao.status()
        elif escolha == "5":
            _ver_inventario(jogador)
        elif escolha == "6":
            _ver_progresso(jogador, missoes_concluidas, reputacao)
        elif escolha == "7":
            confirmar = ci("Tem certeza que quer sair? (s/n): ")
            if confirmar.lower() == "s":
                c(azul + " ⚓︎ Até a próxima, pirata. ☠︎" + RESET)
                exit()
        else:
            c(vermelho + " Opção inválida." + RESET)

#INICIAR JOGO:

def iniciar_jogo():
    while True:
        c_ascii(vermelho + titulo + RESET)
        c(branco   + menu   + RESET)


        try:
            escolha = int(ci("Escolha uma opção: "))
        except ValueError:
            c(vermelho + " Digite um número válido." + RESET)
            continue

        if escolha == 1:
            loading()
            nome    = ci("Digite o nome do seu personagem: ")
            jogador = escolher_classe(nome)
            rep     = Reputacao()
            c(vermelho + " ⚓︎ Sua jornada começa agora. A Baía do Homem Morto te espera." + RESET)
            c(" ")
            time.sleep(1)
            loop_principal(jogador, rep)
            break

        elif escolha == 2:
            ver_classes()

        elif escolha == 3:
            c_ascii(ciano + perola + RESET)

        elif escolha == 4:
            c(branco + " Saindo do jogo." + RESET)
            break

        else:
            c(vermelho + " Opção inválida." + RESET)

#ENTRADA e MÚSICA PRINCIPAL:

if __name__ == "__main__":
    musicaprincipal()
    iniciar_jogo()