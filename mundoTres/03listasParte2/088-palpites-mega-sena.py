# EXERCÍCIO 088 - PALPITES PARA A MEGA SENA

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# SOLUÇÕES

# 1ª

from time import sleep
from random import randint
while True:
    option = int(input('Quantas apostas você quer fazer? '))
    print('Sua(s) aposta(s) são:')
    for opt in range(option):
        list1 = []
        for i in range(0, 6):
            list1.append(randint(1, 60))
        print(sorted(list1))
        sleep(1)
    if option == option:
        break
print('Desejo boa sorte em sua aposta!!')

# 2ª

from time import sleep
from random import randint
listOne = []
bets = []
print('-=' * 20)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-=' * 20)
option = int(input('Quantos jogos você deseja fazer? '))
total = 1
while total <= option:
    cont = 0
    while True:
        number = randint(1, 60)
        if number not in listOne:
            listOne.append(number)
            cont += 1
        if cont >= 6:
            break
    listOne.sort()
    bets.append(listOne[:])
    listOne.clear()
    total += 1
sleep(1)
print('-=' * 5, f'SORTEANDO {option} JOGOS', '-=' * 5)
sleep(1)
for i, row in enumerate(bets):
    print(f'JOGO {i+1}: {row}')
    sleep(1)
print('-=' * 20)
sleep(1)
print(f'{"BOA SORTE EM SUA APOSTA!":^40}')
print('-=' * 20)
