# EXERCÍCIO 075 - ANÁLISE DE DADOS EM UM TUPLA

# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# SOLUÇÃO

number = (int(input('Digite um número: ')),
          int(input('Digite um número: ')),
          int(input('Digite um número: ')),
          int(input('Digite um número: ')))
print(f'Você digitou os valores {number}.')
print(f'O número 9 aparece {number.count(9)} vezes.')

if 3 in number:
    print(f'O valor 3 apareceu na {number.index(3) + 1} posição.')
else:
    print('O valor 3 não foi digitado.')

print(f'Os números pares digitados foram: ', end='')
for n in number:
    if n % 2 == 0:
        print(n, end=' ')
