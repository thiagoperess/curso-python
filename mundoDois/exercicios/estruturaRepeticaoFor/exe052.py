# EXERCICIO 052 - NÚMEROS PRIMOS

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# SOLUÇÃO

cont = 0
num = int(input('Digite um número: '))

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[33m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi disível {} vezes.'.format(num, cont))

if cont == 2:
    print('Portanto, este é um número primo.')
else:
    print('Logo, este não é um número primo.')
