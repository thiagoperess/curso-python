# EXERCICIO 058 - JOGO DA ADIVINHAÇÃO V2.0

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

# SOLUÇÃO

from random import randint
from time import sleep
shot = 0
computer = randint(0, 10)
print('Sou seu computador...')
sleep(1.5)
print('Acabei pensar em um número entre 1 e 10.')
sleep(1.5)
print('Será que você consegue adivinhar qual foi?')
sleep(1.5)
hit = False
while not hit:
    player = int(input('Qual seu palpite? '))
    shot += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            sleep(1)
            print('Ainda não, MAIS!!')
        else:
            sleep(1)
            print('Ainda não, MENOS!!')
sleep(1)
print('Parabéns!!!\nAcertou com {} palpites'.format(shot))
