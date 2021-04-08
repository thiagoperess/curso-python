# EXERCÍCIO 084 - LISTA COMPOSTA E ANÁLISE DE DADOS

# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# SOLUÇÃO

mainList = []
tempList = []
maxWeight = minWeight = 0
while True:
    tempList.append(str(input('Digite o nome: ')))
    tempList.append(int(input('Digite o peso: ')))
    if len(mainList) == 0:
        maxWeight = minWeight = tempList[1]
    else:
        if tempList[1] > maxWeight:
            maxWeight = tempList[1]
        if tempList[1] < minWeight:
            minWeight = tempList[1]
    mainList.append(tempList[:])
    tempList.clear()
    option = str(input('Deseja continuar? [S/N] ')).upper()
    if option not in 'S':
        break
print('-=' * 30)
print(f'No total foram cadastradas {len(mainList)} pessoas.')
print(f'O maior peso foi de {maxWeight} Kg. Peso de ', end='')
for ml in mainList:
    if ml[1] == maxWeight:
        print(f'{ml[0]}.')
print(f'O menor peso foi de {minWeight} Kg. Peso de ', end='')
for ml in mainList:
    if ml[1] == minWeight:
        print(f'{ml[0]}.')
