# EXERCÍCIO 062 - SUPER PROGRESSÃO ARITMÉTICA V3.0

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# SOLUÇÃO

print('='*21)
print('GERADOR DE PROGRESSÃO ARITMÉTICA')
print('='*21)

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
count = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('FIM')
print('Progressão finalizada com {} termos'.format(count))
