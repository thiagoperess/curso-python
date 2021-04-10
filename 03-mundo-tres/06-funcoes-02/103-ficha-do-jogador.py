# EXERCÍCIO 103 - FICHA DO JOGADOR

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar
# a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# SOLUÇÃO

def report(play='<desconhecido>', goals=0):
    print(f'O jogador {play} fez {goal} gol(s).')


name = str(input('Nome do jogador: '))
goal = str(input('Quantidade de gols: '))
if goal.isnumeric():
    goal = int(goal)
else:
    goal = 0
if name.strip() == '':
    report(goals=goal)
else:
    report(name, goal)
