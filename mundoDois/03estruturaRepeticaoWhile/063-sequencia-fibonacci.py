# EXERCÍCIO 063 - SEQUÊNCIA DE FIBONACCI

# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8

# SOLUÇÃO

print('-'*30)
print('     SEQUÊNCIA FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('A sequência Fibonacci é: ')
print('{} → {}'.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' → FIM')
