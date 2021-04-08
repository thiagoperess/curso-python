# EXERCÍCIO 078 - MAIOR E MENOR VALORES DA LISTA

# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

# SOLUÇÃO

numbers = []
for n in range(0, 5):
    numbers.append(int(input(f'Digite um número na {n+1}ª posição: ')))
print(f'A lista é: {numbers}.')

print(f'O maior número da lista é {max(numbers)} na posição de nº ', end='')
for i, v in enumerate(numbers):
    if v == max(numbers):
        print(f'{i+1} ', end='')
print()

print(f'O menor número da lista é {min(numbers)} na posição de nº ', end='')
for i, v in enumerate(numbers):
    if v == min(numbers):
        print(f'{i+1} ', end='')
print()
