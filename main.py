# anunciar vencedor e reiniciar
def anunciarVencedor():
    global pontuacaoJogador, pontuacaoMicro
    if pontuacaoJogador >= 3 or pontuacaoMicro >= 3:
        if pontuacaoJogador > pontuacaoMicro:
            basic.show_string("Voce venceu!" + str(pontuacaoJogador) + " em" + str(pontuacaoMicro))
        else:
            basic.show_string("Eu ganhei!" + str(pontuacaoMicro) + " em" + str(pontuacaoJogador))
        pontuacaoJogador = 0
        pontuacaoMicro = 0
        basic.pause(650)
        mostrarMensagem()
# Reiniciar jogo

def on_logo_pressed():
    mostrarMensagem()
    basic.pause(650)
    desafio()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global palpiteJogador
    # Qual o palpite do jogador?
    palpiteJogador += 1
    if palpiteJogador > ate:
        palpiteJogador = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def desafio():
    global palpiteJogador, CHECK, bitGuessed
    palpiteJogador = 0
    CHECK = False
    bitGuessed = randint(de, ate)
    basic.show_leds("""
        . # # # .
                . # . # .
                . . # # .
                . . # . .
                . . # . .
    """)
def showBadGuess():
    global pontuacaoJogador, pontuacaoMicro
    # Bad Game- One of us guessed a Zero. The other gets a point automatically
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    if bitGuessed == 0:
        # Jogador marca ponto
        pontuacaoJogador += 1
    else:
        # micr:bit marca ponto
        # 
        pontuacaoMicro += 1
def mostrarMensagem():
    basic.clear_screen()
    basic.show_string("Adivinhe 0-" + str(ate) + "!")

def on_button_pressed_b():
    global CHECK
    CHECK = True
    while CHECK == True:
        if bitGuessed > 0 and palpiteJogador > 0:
            if palpiteJogador == bitGuessed:
                mostraVitoria()
            else:
                mostraPerda()
        else:
            showBadGuess()
        anunciarVencedor()
        basic.pause(800)
        desafio()
input.on_button_pressed(Button.B, on_button_pressed_b)

def mostraPerda():
    global pontuacaoMicro
    # You guessed wrong!
    basic.show_number(palpiteJogador)
    basic.show_leds("""
        . . . # .
                # # # # #
                # # # # #
                . . # . .
                . . . . .
    """)
    basic.show_number(bitGuessed)
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # #
                . # # # .
                . . # . .
    """)
    pontuacaoMicro += 1
def mostraVitoria():
    global pontuacaoJogador
    # You guessed RIGHT! YAY!
    basic.show_number(palpiteJogador)
    basic.show_leds("""
        . . . . .
                # # # # #
                # # # # #
                . . . . .
                . . . . .
    """)
    basic.show_number(bitGuessed)
    basic.show_leds("""
        . . # . .
                . # # # .
                # # # # #
                . . # . .
                . . # . .
    """)
    pontuacaoJogador += 1
bitGuessed = 0
CHECK = False
palpiteJogador = 0
pontuacaoMicro = 0
pontuacaoJogador = 0
ate = 0
de = 0
mensagem = ""
de = 0
ate = 10
mostrarMensagem()
basic.pause(650)
desafio()