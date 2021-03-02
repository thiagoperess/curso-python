# EXERCÍCIO - PALPITES PARA A MEGA SENA

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# SOLUÇÃO


from random import randint
while True:
    option = int(input('Quantas apostas você quer fazer? '))
    print('Sua(s) aposta(s) são:')
    for opt in range(option):
        list1 = []
        for i in range(0, 6):
            list1.append(randint(1, 60))
        print(list1)
    if option == option:
        break
print('Desejo boa sorte em sua aposta!!')
