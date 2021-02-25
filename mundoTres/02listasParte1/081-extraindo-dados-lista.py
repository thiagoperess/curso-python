# EXERCÍCIO 081 - EXTRAINDO DADOS DE UMA LISTA

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# SOLUÇÃO

option = 'Ss'
numbers = []

while True:
    if option in 'Ss':
        numbers.append(int(input('Digite um número: ')))
        option = str(input('Deseja continuar? [S/N] '))
    else:
        break

print(f'Foram digitados no total {len(numbers)} valores.')
print(f'Os valores digitados em ordem decrescente: {sorted(numbers, reverse=True)}')

if 5 in numbers:
    print(f'O número 5 apareceu na {numbers.index(5) + 1}ª posição da lista.')
else:
    print('O número 5 não consta na lista.')
