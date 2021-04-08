# EXERCÍCIO 080 - LISTA ORDENADA SEM REPETIÇÕES

# Crie um programa onde o usuário possa digitar cinco
# valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

# SOLUÇÕES

numberList = []
for n in range(0, 5):
    number = int(input(f'Digite o {n+1}º valor: '))
    if n == 0 or number > numberList[-1]:
        numberList.append(number)
        print('Adicionado ao final da lista')
    else:
        position = 0
        while position < len(numberList):
            if number <= numberList[position]:
                numberList.insert(position, number)
                print(f'Adicionado a lista na {position+1}ª posição.')
                break
            position += 1
print('-' * 30)
print(f'Os valores digitados em ordem foram: {numberList}')

# UTILIZANDO SORT:

# numbers = []
# for n in range(0, 5):
#     numbers.append(int(input(f'Digite o {n+1}º valor: ')))
# print(f'Lista de valores ordenada: {sorted(numbers)}')
