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
pedra = pcOptions[0]
papel = pcOptions[1]
tesoura = pcOptions[2]
pcChoice = int(random.choice(pcOptions))

if humanChoice == 0 and pcChoice == 2 or \
    humanChoice == 1 and pcChoice == 0 or \
    humanChoice == 2 and pcChoice == 1:
    print('Eu escolhi {} e você {}! \n'
          'Você ganhou!! PARABÉNS!!'.format(humanChoice, pcChoice))
elif humanChoice == pcChoice:
    print('Eu escolhi {} e você {}! \n'
          'EMPATE! Jogue novamente!'.format(humanChoice, pcChoice))
else:
    print('Eu escolhi {} e você {}! \n'
          'Você perdeu!! Tente novamente!'.format(humanChoice, pcChoice))
