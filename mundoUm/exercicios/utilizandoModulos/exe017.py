# EXERCICIO 017 - CATETOS E HIPOTENUSA

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# SOLUÇÃO

# com cálculo matemático da hipotenusa
c1 = float(input('Primeiro cateto: '))
c2 = float(input('segundo cateto: '))
hipotenusa = (c1 ** 2 + c2 ** 2) ** (1/2)
print('Com os catetos {} e {}, a hipotenusa deve medir {:.2f}'.format(c1, c2, hipotenusa))

# hipotenusa importando módulo
import math
c1 = float(input('Primeiro cateto: '))
c2 = float(input('segundo cateto: '))
hipotenusa = math.hypot(c1, c2)
print('Com os catetos {} e {}, a hipotenusa deve medir {:.2f}'.format(c1, c2, hipotenusa))

