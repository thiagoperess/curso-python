# EXERCICIO 045 - GAME JOKENPÔ

# Crie um programa que faça o computador jogar Jokenpô com você.

# SOLUÇÃO:

print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

import random
humanChoice = int(input('Qual é sua jogada? '))
pcOptions = [0, 1, 2]
pcChoice = int(random.choice(pcOptions))
print('Escolhi {}.'.format(pcChoice))

if humanChoice == 0 and pcChoice == 2 or \
    humanChoice == 1 and pcChoice == 0 or \
    humanChoice == 2 and pcChoice == 1:
    print("Você ganhou!! PARABÉNS!!")
elif humanChoice == pcChoice:
    print('EMPATE! Joguem novamente!')
else:
    print('Você perdeu!! Tente novamente!')
