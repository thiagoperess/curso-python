# EXERCICIO 019 - SORTEANDO UM ITEM NA LISTA

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# SOLUÇÃO

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos = [n1, n2, n3, n4]
escolhidx = str(random.choice(alunos))
print('X Alunx sorteadx foi: {}'.format(escolhidx))