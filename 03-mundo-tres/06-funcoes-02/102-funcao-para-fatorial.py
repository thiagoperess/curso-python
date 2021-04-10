# EXERCÍCIO 102 - FUNÇÃO PARA FATORIAL

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# SOLUÇÕES

# 1

from math import factorial

def fatorial(num):
    '''
    -> Calcula o fatorial de algum número
    :param num: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor fatorial de um número 'num'.
    '''
    num = int(input('Digite um número: '))
    count = num
    fat = 1
    print(f'Calculando fatorial do número {num} ')
    option = 'Ss'
    option = str(input('Deseja mostrar o cálculo? [S/N] ')).upper()
    if option in 'S':
        print(f'O cálculo fatorial de {num}:')
        while count > 0:
            print(f'{count}', end='')
            print(' x ' if count > 1 else ' = ', end='')
            fat *= count
            count -= 1
        print(f'{fat}')
    else:
        fat = factorial(num)
        print(f'O fatorial de {num} é {fat}.')


fatorial(num=True)

# 2

def fatorial2(num, show=False):
    '''
    -> Calcula o fatorial de algum número
    :param num: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor fatorial de um número 'num'.
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


help(fatorial)
