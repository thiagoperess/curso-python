# EXERCICIO 049 - TABUADA V2.0

# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

# SOLUÇÕES

# primeira
m = -1
n = int(input('Digite um número para ver a tabuada: '))
for c in range(11):
    m += 1
    r = n * m
    print('{} X {:2} = {:2}'.format(n, m, r))

# segunda
num = int(input('Digite um número para ver a tabuada: '))
for c in range(11):
    print('{} X {:2} = {:2}'.format(num, c, num * c))
