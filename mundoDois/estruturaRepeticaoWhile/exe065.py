# EXERCÍCIO 065 - MAIOR E MENOR VALORES

#  Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores
#  e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# SOLUÇÃO

count = 0
soma = 0
opt = 'sS'
while opt in 'sS':
    num = int(input('Digite um número: '))
    opt = str(input('Deseja continuar digitando valores? [s/n]'))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
media = soma / count
print('Você digitou {} números e a média foi {}'.format(count, media))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}.'.format(menor))
print('FIM')
