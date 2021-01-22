# EXERCICIO 042 - ANALISANDO TRIÂNGULOS V2.0

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# EQUILÁTERO: todos os lados iguais;
# ISÓSCELES: dois lados iguais, um diferente;
# ESCALENO: todos os lados diferentes.

# SOLUÇÃO:

print('-=' * 12)
print('Analisador de triâgulos')
print('-=' * 12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and \
        r2 < r3 + r1 and \
        r3 < r2 + r1:
    print('Estas retas \033[1;32mPODEM\033[m formar um triângulo!')
    if r1 == r2 and \
            r1 == r3 and \
            r2 == r3:
        print('Estas retas formam um triâgulo Equilátero.')
    elif r1 == r2 and r1 != r3 or \
            r2 == r3 and r2 != r1 or \
            r3 == r1 and r3 != r2:
        print('Estas retas formam um triângulo Isósceles.')
    elif r1 != r2 and r1 != r3 or \
            r2 != r3 and r2 != r1 or \
            r3 != r1 and r3 != r2:
        print('Estas retas formam um triângulo Escaleno')
else:
    print('Estas retas \033[1;31mNÃO PODEM\033[m formar um triângulo')
