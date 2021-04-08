# EXERCÍCIO 098 - FUNÇÃO DE CONTADOR

# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# SOLUÇÃO

from time import sleep

def counter(start, finish, steps):

    if steps < 0:
        steps *= -1
    if steps == 0:
        steps = 1

    print(f'A contagem do {start} ao {finish} foi de {steps} em {steps}.')
    print('-'*35)
    sleep(0.5)

    if start < finish:
        count = start
        while count <= finish:
            print(f'{count}', end=' ')
            sleep(0.5)
            count += steps
        sleep(0.5)
        print('FIM')
        print('-'*35)
        sleep(0.5)
    else:
        count = start

        while count >= finish:
            print(f'{count}', end=' ')
            sleep(0.5)
            count -= steps
        sleep(0.5)
        print('FIM')
        print('-'*35)
        sleep(0.5)


# programa principal
counter(1, 10, 1)
counter(10, 0, 2)
print('Agora é sua vez de contar:')
print('-'*35)
first = int(input('Início: '))
last = int(input('Fim: '))
measure = int(input('Passo: '))
counter(first, last, measure)

