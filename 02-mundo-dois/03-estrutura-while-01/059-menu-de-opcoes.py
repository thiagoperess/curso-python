# EXERCÍCIO 059 - CRIANDO UM MENU DE OPÇÕES

# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

# SOLUÇÃO

import time

firstNum = int(input('Primeiro valor: '))
secondNum = int(input('Segundo valor: '))
option = 0

while option != 5:
    print('''Escolha uma opção:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair''')
    option = int(input('\n>>>> Qual deseja? '))
    if option == 1:
        print('A soma entre os números {} e {} é {}'
              .format(firstNum, secondNum, firstNum + secondNum))
    elif option == 2:
        print('O produto dos números {} e {} é {}'
              .format(firstNum, secondNum, firstNum * secondNum))
    elif option == 3:
        list1 = [firstNum, secondNum]
        print('O número {} é maior que o número {}'
              .format(max(list1), min(list1)))
    elif option == 4:
        firstNum = int(input('Primeiro valor: '))
        secondNum = int(input('Segundo valor: '))
    elif option > 5:
        print('Opção inválida!! Digite uma opção existente!')
    print('=-='*12)

print('Finalizando.')
time.sleep(1)
print('Finalizando..')
time.sleep(1)
print('Finalizando...')
time.sleep(1)
print("Fim do programa! Volte sempre!")
