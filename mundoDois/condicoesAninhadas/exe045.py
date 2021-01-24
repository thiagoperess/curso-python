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
itens = ('Pedra', 'Papel', 'Tesoura')
pcChoice = int(random.choice(pcOptions))

if humanChoice == 0 and pcChoice == 2 or \
        humanChoice == 1 and pcChoice == 0 or \
        humanChoice == 2 and pcChoice == 1:

    print('Você jogou {}'.format(itens[humanChoice]))
    print('Computador jogou {}'.format(itens[pcChoice]))
    print('Você ganhou!! PARABÉNS!!'.format(humanChoice, pcChoice))

elif humanChoice == pcChoice:

    print('Você jogou {}'.format(itens[humanChoice]))
    print('Computador jogou {}'.format(itens[pcChoice]))
    print('EMPATE! Jogue novamente!'.format(humanChoice, pcChoice))

elif pcChoice == 0 and humanChoice == 2 or \
        pcChoice == 1 and humanChoice == 0 or \
        pcChoice == 2 and humanChoice == 1:

    print('Você jogou {}'.format(itens[humanChoice]))
    print('Computador jogou {}'.format(itens[pcChoice]))
    print('Você perdeu!! Tente novamente!'.format(humanChoice, pcChoice))

else:
    print('Não te entendi. Digite uma opção válida!')
