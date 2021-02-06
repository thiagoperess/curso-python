# EXERCICIO 022 - ANALISADOR DE TEXTOS

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo sem espaços.
# Quantas letras tem o primeiro nome.

# SOLUÇÃO

nome = str(input('Qual seu nome? '))
print('Seu nome eu maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.strip())-1))
nome = nome.split()
print(str('Seu primeiro nome possui {} letras'.format(len(nome[0]))))