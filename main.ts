// anunciar vencedor e reiniciar
function anunciarVencedor () {
    if (pontuacaoJogador >= tentativas || pontuacaoMicro >= tentativas) {
        if (pontuacaoJogador > pontuacaoMicro) {
            basic.showString("Voce venceu!" + pontuacaoJogador + " em" + pontuacaoMicro)
        } else {
            basic.showString("Eu ganhei!" + pontuacaoMicro + " em" + pontuacaoJogador)
        }
        pontuacaoJogador = 0
        pontuacaoMicro = 0
        basic.pause(650)
        mostrarMensagem()
    }
}
// Reiniciar jogo
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    mostrarMensagem()
    basic.pause(650)
    desafio()
})
input.onButtonPressed(Button.A, function () {
    // Qual o palpite do jogador?
    palpiteJogador += 1
    if (palpiteJogador > ate) {
        palpiteJogador = 0
    }
})
function desafio () {
    palpiteJogador = 0
    jogoIniciado = false
    palpiteMicro = randint(de, ate)
    basic.showLeds(`
        . # # # .
        . # . # .
        . . # # .
        . . # . .
        . . # . .
        `)
}
function mostrarMensagem () {
    basic.clearScreen()
    basic.showString("Adivinhe 0-" + ate + "!")
}
function mostrarPalpiteRuim () {
    // Bad Game- One of us guessed a Zero. The other gets a point automatically
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    if (palpiteMicro == 0) {
        // Jogador marca ponto
        pontuacaoJogador += 1
    } else {
        // micr:bit marca ponto
        // 
        pontuacaoMicro += 1
    }
}
input.onButtonPressed(Button.B, function () {
    jogoIniciado = true
    while (jogoIniciado == true) {
        if (palpiteMicro > 0 && palpiteJogador > 0) {
            if (palpiteJogador == palpiteMicro) {
                mostraVitoria()
            } else {
                mostraPerda()
            }
        } else {
            mostrarPalpiteRuim()
        }
        anunciarVencedor()
        basic.pause(800)
        desafio()
    }
})
function mostraPerda () {
    // You guessed wrong!
    basic.showNumber(palpiteJogador)
    basic.showLeds(`
        . . . . .
        # # # # #
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.showNumber(palpiteMicro)
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . # # # .
        . . # . .
        `)
    pontuacaoMicro += 1
}
function mostraVitoria () {
    // You guessed RIGHT! YAY!
    basic.showNumber(palpiteJogador)
    basic.showLeds(`
        . . . # .
        # # # # #
        . . # . .
        # # # # #
        . # . . .
        `)
    basic.showNumber(palpiteMicro)
    basic.showLeds(`
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        `)
    pontuacaoJogador += 1
}
let palpiteMicro = 0
let jogoIniciado = false
let palpiteJogador = 0
let pontuacaoMicro = 0
let pontuacaoJogador = 0
let ate = 0
let de = 0
let tentativas = 0
tentativas = 3
de = 0
ate = 10
mostrarMensagem()
basic.pause(650)
desafio()
