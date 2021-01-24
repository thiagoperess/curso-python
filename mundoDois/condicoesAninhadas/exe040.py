# EXERCICIO 040 - AQUELE CLÁSSICO DA MÉDIA

# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

# SOLUÇÃO:

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você possui uma média {} e está\033[31m REPROVADO!'.format(media))
elif 5 <= media <= 6.9:
    print('Você possui uma média {} e está de\033[33m RECUPERAÇÃO!'.format(media))
elif media > 10:
    print('A média {} não está dentro dos valores válidos'.format(media))
else:
    print('Você possui uma média {} e está\033[32m APROVADO!\033[m PARABÉNS!!'.format(media))
