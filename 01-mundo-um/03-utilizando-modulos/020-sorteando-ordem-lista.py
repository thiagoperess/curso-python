# EXERCICIO 020 - SORTEANDO UMA ORDEM NA LISTA

# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# SOLUÇÃO

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem de apresentação do trabalho será {}.'.format(alunos))