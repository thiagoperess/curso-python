# EXERCICIO 054 - GRUPO DA MAIORIDADE

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# SOLUÇÃO:

import datetime
currentYear = datetime.date.today().year
under18 = 0
over18 = 0
for everyone in range(1, 8):
    birth = int(input('Em que ano nasceu a {}ª pessoa? '.format(everyone)))
    age = currentYear - birth
    if age < 18:
        under18 += 1
    else:
        over18 += 1
print('Ao todo tivemos {} pessoas maiores e {} pessoas menores'.format(over18, under18))
