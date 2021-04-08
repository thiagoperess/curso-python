# EXERCÍCIO 087 - MAIS SOBRE MATRIZ EM PYTHON

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# SOLUÇÕES

# 1ª

evenSum = []
numberList = []
for i in range(0, 9):
    number = int(input(f'Digite o {i+1}º número: '))
    numberList.append(number)
    if number % 2 == 0:
        evenSum.append(number)
print('=-'*20)
print(f'{"MATRIZ PYTHON V2.0":^40}')
print('=-'*20)
print(numberList[:3])
print(numberList[3:6])
print(numberList[6:])
print('=-'*20)
print(f'A soma dos números pares foi {sum(evenSum)}')
print(f'A soma dos valores da 3ª coluna foi {numberList[2] + numberList[5] + numberList[8]}')
print(f'O maior da segunda linha foi ', end='')
print(max(numberList[3:6]))

# 2ª

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
evenSum = columnSum = maxRdColumn = 0

for row in range(0, 3):
    for col in range(0, 3):
        matrix[row][col] = int(input(f'Digite um valor para [{row}, {col}]: '))
for row in range(0, 3):
    for col in range(0, 3):
        print(f'[{matrix[row][col]:^5}]', end='')
        if matrix[row][col] % 2 == 0:
            evenSum += matrix[row][col]
    print()
print('=-'*20)
print(f'A soma dos valores pares é {evenSum}.')
for row in range(0, 3):
    columnSum += matrix[row][2]
for col in range(0, 3):
    if col == 0:
        maxRdColumn = matrix[1][col]
    elif matrix[1][col] > maxRdColumn:
        maxRdColumn = matrix[1][col]
print(f'A soma dos valores da terceira coluna é {columnSum}')
print(f'O maior valor da segunda linha é {maxRdColumn}.')
