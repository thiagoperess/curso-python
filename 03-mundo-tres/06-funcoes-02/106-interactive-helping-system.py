# EXERCÍCIO 106 - INTERACTIVE HELPING SYSTEM IN PYTHON

# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

# Importante: use cores.

# SOLUÇÃO

from time import sleep

colors = ('\033[m',         # sem cor
          '\033[0;30;41m',  # vermelho
          '\033[0;30;42m',  # verde
          '\033[0;30;43m',  # amarelo
          '\033[0;30;44m',  # azul
          '\033[0;30;45m',  # roxo
          '\033[7;30m'      # branco
          )


def helping(com):
    title(f'Acessando o manual do comando \'{com}\'', 4)
    print(colors[3], end='')
    help(com)
    print(colors[4], end='')
    sleep(2)


def title(msg, color=0):
    size = len(msg)
    print(colors[color], end='')
    print('~' * size)
    print(msg)
    print('~' * size)
    print(colors[0], end='')
    sleep(1)


command = ''
while True:
    title('SISTEMA DE AJUDA PYHELPING', 2)
    command = str(input('Função ou biblioteca > '))
    if command.upper() == 'FIM':
        break
    else:
        helping(command)
title('ATÉ LOGO', 1)
