# EXERCICIO 030

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# SOLUÇÃO

numero = int(input('Me diga um número qualquer: '))
if numero % 2 == 0:
    print('{} é um número PAR!'.format(numero))
else:
    print('{} é um número ÍMPAR'.format(numero))