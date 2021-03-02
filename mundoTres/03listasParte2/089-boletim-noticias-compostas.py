# EXERCÍCIO 089 - BOLETIM COM LISTAS COMPOSTAS

# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

# SOLUÇÃO

reportCard = []
while True:
    name = str(input('Nome do aluno: '))
    score1 = float(input('Nota 1: '))
    score2 = float(input('Nota 2: '))
    average = (score1 + score2) / 2
    reportCard.append([name, [score1, score2], average])
    option = str(input('Deseja cadastrar mais alunos? [S/N] ')).upper()
    if option not in 'S':
        break