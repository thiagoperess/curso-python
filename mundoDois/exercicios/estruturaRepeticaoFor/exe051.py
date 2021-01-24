# EXERCICIO 051 - PROGRESSÃO ARITMÉTICA

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

# SOLUÇÃO

print('='*21)
print('PROGRESSÃO ARITMÉTICA')
print('='*21)

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, decimo + razao, razao):
    print(c, end=' → ')
print('FIM')
