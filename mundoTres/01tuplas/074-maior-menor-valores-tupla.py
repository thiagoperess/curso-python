# EXERCÍCIO 074 - MAIOR E MENOR VALORES EM TUPLA

# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

# SOLUÇÃO
import time
from random import randint
numbers = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
time.sleep(1)
print('Os números sorteados foram: ', end='')
time.sleep(1)
for n in numbers:
    print(f'{n} ', end='')
    time.sleep(1)
print(f'\nO maior valor foi {max(numbers)}')
time.sleep(1)
print(f'O menor valor foi {min(numbers)}')
time.sleep(1)
print('FIM!')

