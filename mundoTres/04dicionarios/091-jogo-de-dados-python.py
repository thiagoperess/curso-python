# EXERCÍCIO 091 - JOGO DE DADOS EM PYTHON

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# SOLUÇÃO

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    "Player 1": randint(1, 6),
    "Player 2": randint(1, 6),
    "Player 3": randint(1, 6),
    "Player 4": randint(1, 6)
}
print('Os dados foram arremessados!!!')
sleep(1.5)
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} em seu dado.')
    sleep(1)
print('-='*20)
print('== RANKING GERAL ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
