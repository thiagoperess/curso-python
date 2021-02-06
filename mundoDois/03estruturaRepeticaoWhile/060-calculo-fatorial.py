# EXRECÍCIO 060 - CÁLCULO DE FATORIAL

# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# SOLUÇÕES

from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fat = factorial(num)
print('O fatorial de {} é {}'.format(num, fat))

num = int(input('Digite um número: '))
count = num
fat = 1
print('Calculando {}!'.format(num))
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fat *= count
    count -= 1
print('{}'.format(fat))
