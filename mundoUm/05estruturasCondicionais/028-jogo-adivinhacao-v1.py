# EXERCICIO 028 - JOGO DA ADIVINHAÇÃO V1.0

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# SOLUÇÃO

import random
numero = int(input('Digite um número de 0 a 5: '))
computador = random.randint(0, 5)
if numero == computador:
    print('Você acertou!! PARABÉNS!!')
else:
    print('Você errou! TENTE DE NOVO!')
print('PROCESSANDO...')
print('Computador: Pensei no número {}'.format(computador))
