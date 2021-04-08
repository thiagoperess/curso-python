# EXERCÍCIO 100 - FUNÇÕES PARA SORTEAR E SOMAR

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# SOLUÇÃO

from random import randint
from time import sleep


def sortition(lista):
    print('Sorteando os valores da lista:')
    sleep(.6)
    for cont in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num}', end=' ')
        sleep(1)
    print('\nPRONTO!')


def sumPair(lista):
    summation = 0
    for value in lista:
        if value % 2 == 0:
            summation += value
    pairs = list()
    for pair in lista:
        if pair % 2 == 0:
            pairs.append(pair)

    sleep(1)
    print(f'A lista apresentada foi: {lista} ')
    sleep(1)
    print(f'Os números pares foram: {pairs}')
    sleep(1)
    print(f'E a soma de seus valores foi {summation}.')


numbers = list()
sortition(numbers)
sumPair(numbers)
