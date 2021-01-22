# EXERCICIO 016 - QUEBRANDO UM NÚMERO

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# SOLUÇÃO

import math
num = float(input('Digite um número: '))
truncado = math.trunc(num)
print('O número {} tem a parte inteira {}'.format(num, truncado))