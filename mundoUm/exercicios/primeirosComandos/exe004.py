# EXERCICIO 004

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele:

# SOLUÇÃO:

a = input("Digite algo: ")
print('O tipo primitivo da palavra é: '.format(a), type(a))
print('O tipo só tem espaços? ', a.isspace())
print('O tipo é numérico? ', a.isnumeric())
print('O tipo é alfabético? ', a.isalpha())
print('O tipo é alfanumérico? ', a.isalnum())
print('O tipo é UPPERCASE? ', a.isupper())
print('O tipo é LOWERCASE?', a.islower())
print('Está Capitalizada? ', a.istitle())
