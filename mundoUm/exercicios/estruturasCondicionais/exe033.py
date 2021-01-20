# EXERCICIO 033

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# SOLUÇÃO

valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
valor3 = int(input('Valor 3: '))

# verificando quem é o MENOR
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

# verificando quem é o MAIOR
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))