# EXERCÍCIO 061 - PROGRESSÃO ARITMÉTICA V2.0

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# SOLUÇÃO

print('='*21)
print('GERADOR DE PROGRESSÃO ARITMÉTICA')
print('='*21)

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
count = 1
while count < 11:
    print('{} → '.format(termo), end='')
    termo += razao
    count += 1
print('FIM')
