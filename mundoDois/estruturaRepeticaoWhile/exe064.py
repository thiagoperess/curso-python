# EXERCÍCIO 064 - TRATANDO VÁRIOS VALORES V1.0

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

# SOLUÇÕES

# 1
soma = count = num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    count += 1
    num = int(input('Digite um número [999 para parar]: '))
print('FIM')
print('Você digitou {} números e a soma deles foi {}.'.format(count, soma))

# 2
soma = count = num = 0
while num != 999:
    soma += num
    count += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma deles foi {}. \nFIM'.format(count-1, soma))
