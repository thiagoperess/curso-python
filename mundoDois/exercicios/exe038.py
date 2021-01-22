#  EXERCICIO 038 - COMPARANDO NÚMEROS

# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é o maior;
# O segundo valor é o maior;
# Não existe valor maior, os dois números são iguais.

# SOLUÇÃO:

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O número {} é maior do que o número {}.'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior do que o número {}.'.format(num2, num1))
else:
    print('Não existe valor maior. Os dois números são iguais!')
