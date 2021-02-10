# EXERCÍCIO 068 - JOGO DO PAR OU ÍMPAR

# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# SOLUÇÃO

import time
import random
victory = 0
print('Vamos jogar PAR ou ÍMPAR!!')

while True:

    player = int(input('Digite um número: '))
    pc = random.randint(0, 11)
    total = pc + player
    optPlayer = str(input('Par ou ímpar [P/I]? ')).upper()

    print('Estou pensando em algum número...')
    time.sleep(1)
    print(f'Você jogou {player} e eu joguei {pc}. \nO total foi {total}')
    time.sleep(1)
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR!')
    if total % 2 == 0 and optPlayer in 'P':
        print('Você venceu')
    else:
        if total % 2 == 1 and optPlayer in 'I':
            print('Você venceu')
        else:
            print('Você perdeu')
            break

    victory += 1
    time.sleep(1)
    print('Vamos jogar novamente!')
print(f'GAME OVER!!!\nVocê venceu {victory} vezes.')
