# EXERCICIO 018 - SENO, COSSENO E TANGENTE

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# SOLUÇÃO

import math
angulo = float(input('Qual o angulo que você está querendo? '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {} possui um seno de {:.2f}, '
      '\nCosseno de {:.2f} e \nTangente de {:.2f}.'.format(angulo, seno, cosseno, tangente))
