# EXERCÍCIO 086 - Matriz em Python

# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

# SOLUÇÃO

numberList = []
for i in range(0, 9):
    number = int(input(f'Digite o {i+1}º número: '))
    numberList.append(number)
print(numberList[:3])
print(numberList[3:6])
print(numberList[6:])

