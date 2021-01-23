# EXERCICIO 039 - ALISTAMENTO MILITAR

# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# SOLUÇÃO:

from datetime import date
anoAtual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, anoAtual))
if idade == 18:
    print('Você tem {} e está no ano de se alistar.'.format(idade))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))
else:
    print('Você ainda não precisa se alistar. Mas deverá fazê-lo em {} anos.'.format(18 - idade))
    print('Seu alistamente será em {}.'.format(nascimento + 18))
