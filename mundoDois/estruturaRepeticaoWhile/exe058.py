# EXERCICIO 058 - JOGO DA ADIVINHAÇÃO V2.0

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# SOLUÇÃO

from random import randint
shot = 0
computer = randint(0, 10)
print('Sou computador... Acabei pensar em um número entre 1 e 10.')
print('Será que você consegue adivinhar qual foi?')
hit = False
while not hit:
    player = int(input('Qual seu palpite? '))
    shot += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print('Ainda não, MAIS!!')
        else:
            print('Ainda não, MENOS!!')
print('Parabéns!!!\nAcertou com {} palpites'.format(shot))
