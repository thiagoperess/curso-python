# EXERCÍCIO 086 - MATRIZ EM PYTHON

# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

# SOLUÇÕES

# 1ª

numberList = []
for i in range(0, 9):
    number = int(input(f'Digite o {i+1}º número: '))
    numberList.append(number)
print(numberList[:3])
print(numberList[3:6])
print(numberList[6:])

# 2ª

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for col in range(0, 3):
        matrix[row][col] = int(input(f'Digite um valor para [{row}, {col}]: '))
for row in range(0, 3):
    for col in range(0, 3):
        print(f'[{matrix[row][col]:^5}]', end='')
    print()
