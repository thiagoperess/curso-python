# EXERCICIO 025 - PROCURAND0 UMA STRING DENTRO DA OUTRA

# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# SOLUÇÃO

nome = str(input('Digite o nome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
