# EXERCÍCIO 099 - FUNÇÃO DESCOBRE O MAIOR

# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# SOLUÇÃO

from time import sleep


def bigger(*numbers):
    cont = bigger = 0
    print('Analisando os valores passados...')
    sleep(.5)
    for num in numbers:
        sleep(.5)
        print(f'{num}', end=' ')
        if cont == 0:
            bigger = num
        else:
            if num > bigger:
                bigger = num
        cont += 1
    sleep(.5)
    print(f'\nForam informados {cont} valores.')
    sleep(.5)
    print(f'O maior valor foi: {bigger}')


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()
