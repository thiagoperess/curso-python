# EXERCÍCIO 090 - DICIONÁRIO EM PYTHON

# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# SOLUÇÃO

student = dict()
student['name'] = str(input('Nome do alunx: '))
student['average'] = float(input(f'Média de {"name"}: '))
if student['average'] >= 7:
    student['situation'] = 'Aprovado'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Recuperação'
else:
    student['situation'] = 'Reprovado'
print(f'X alunx {student["name"]}'
      f' ficou com média {student["average"]} '
      f'e sua situação é {student["situation"]}')
