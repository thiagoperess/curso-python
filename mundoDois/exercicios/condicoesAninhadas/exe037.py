#EXERCICIO 037 - CONVERSOR DE BASES NUMÉRICAS

# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
#
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# SOLUÇÃO:

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('{} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Digite uma opção válida!')
