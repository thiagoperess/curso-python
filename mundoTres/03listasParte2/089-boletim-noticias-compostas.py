# EXERCÍCIO 089 - BOLETIM COM LISTAS COMPOSTAS

# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

# SOLUÇÃO

from time import sleep
reportCard = []
while True:
    student = str(input('Nome do aluno: '))
    firstTest = float(input('Nota 1: '))
    secondTest = float(input('Nota 2: '))
    average = (firstTest + secondTest) / 2
    reportCard.append([student, [firstTest, secondTest], average])
    option = str(input('Deseja cadastrar mais alunos? [S/N] ')).upper()
    if option not in 'S':
        break
print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 20)
for i, s in enumerate(reportCard):
    print(f'{i:<4}{s[0]:<10}{s[2]:<8.1f}')
while True:
    print('-=' * 20)
    individualNotes = int(input('Mostrar as notas de quais alunos? (999 interrompe): '))
    if individualNotes == 999:
        sleep(1)
        print('FINALIZANDO PROGRAMA')
        break
    if individualNotes <= len(reportCard) - 1:
        sleep(1)
        print(f'As notas de {reportCard[individualNotes][0]} são {reportCard[individualNotes][1]}')
        sleep(1)
sleep(1)
print('VOLTE SEMPRE!!')
