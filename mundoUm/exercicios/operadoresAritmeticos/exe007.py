# EXERCICIO 007

# Desenvolva um programa que leia as duas notas de um aluno e mostre sua média:

# SOLUÇÃO:

nota1 = int(input("Primeira nota do aluno: "))
nota2 = int(input("Segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print("A média final é: {:.2f}".format(media))
