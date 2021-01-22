# EXERCICIO 035 - ANALISANDO TRIÂNGULO V1.0

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# SOLUÇÃO

print('-='*12)
print('Analisador de triâgulos')
print('-='*12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 \
        and r2 < r3 + r1 \
        and r3 < r2 + r1:
    print('Estas retas \033[1;32mPODEM\033[m formar um triângulo!')
else:
    print('Estas retas \033[1;31mNÃO PODEM\033[m formar um triângulo')
