# EXERCÍCIO 085 - LISTA COM PARES E ÍMPARES

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# SOLUÇÃO

# com lista única

number = [[], []]
value = 0
for i in range(0, 7):
    value = int(input(f'Digite o {i+1}º valor: '))
    if value % 2 == 0:
        number[0].append(value)
    else:
        number[1].append(value)
print(f'Os números pares foram: ', end='')
print(sorted(number[0]))
print(f'Os valores ímpares foram: ', end='')
print(sorted(number[1]))

# com mais de uma lista

# oddList = []
# evenList = []
# numberList = []
# for i in range(0, 7):
#     numbers = int(input('Digite um número: '))
#     numberList.append(numbers)
#     if numbers % 2 == 0:
#         evenList.append(numbers)
#     else:
#         oddList.append(numbers)
# print(f'Os números pares foram: ', end='')
# print(sorted(evenList))
# print(f'Os números ímpares foram: ', end='')
# print(sorted(oddList))

