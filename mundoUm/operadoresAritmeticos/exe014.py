# EXERCICIO 014 - CONVERSOR DE TEMPERATURAS

# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# SOLUÇÃO

c = float(input('Qual a temperatura em ºC? '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))