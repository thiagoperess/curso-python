# EXERCÍCIO 069 - ANÁLISE DE DADOS DO GRUPO

# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# SOLUÇÕES

# 1

# everybody = 0
# over18 = 0
# men = 0
# women20 = 0
# optPlayer = 'sS'
# while True:
#     print('CADASTRE UMA PESSOA:')
#     age = int(input('Digite a idade: '))
#     gender = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
#     if gender not in 'MmFf':
#         print('Resposta inválida!')
#     else:
#         optPlayer = str(input('Deseja continuar? [S/N] '))
#         everybody += 1
#         if optPlayer not in 'SsNn':
#             print('Digite uma opção válida!')
#         if gender in 'Ff' and age < 20:
#             women20 += 1
#         if gender in 'Mm':
#             men += 1
#         if age >= 18:
#             over18 += 1
#         if optPlayer in 'Nn':
#             break
# print(f'Temos {over18} pessoas com mais de 18 anos.\n'
#       f'Temos {men} homens no total.\n'
#       f'Temos {women20} mulheres com menos de 20 anos.\n'
#       f'No total foram registradas {everybody} pessoas.\n'
#       f'FIM.')

# 2

everybody = women20 = men = over18 = 0

while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [F/M]: ')).strip().upper()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    everybody += 1
    if sex in 'F' and age < 20:
        women20 += 1
    if sex in 'M':
        men += 1
    if age >= 18:
        over18 += 1
    if resp in 'N':
        break
print(f'Temos {over18} pessoas com mais de 18 anos.\n'
      f'Temos {men} homens no total.\n'
      f'Temos {women20} mulheres com menos de 20 anos.\n'
      f'No total foram registradas {everybody} pessoas.\n'
      f'FIM.')
