# EXERCICIO 058 - JOGO DA ADIVINHAÇÃO V2.0

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

# SOLUÇÃO

from random import randint
from time import sleep
shot = 0
computer = randint(0, 10)
print('Sou seu computador...')
sleep(1.5)
print('Acabei pensar em um número entre 0 e 10.')
sleep(1.5)
choose = str(input('Será que você consegue adivinhar qual foi? [s/n]: '))[0]
if choose in 'sS':
    sleep(1)
    print('Quem não arrisca não petisca, certo?! Boa sorte!')
    hit = False
    while not hit:
        sleep(1)
        player = int(input('Qual seu palpite? '))
        shot += 1
        if player == computer:
            hit = True
        else:
            if player < computer:
                sleep(0.5)
                print('Ainda não, MAIS!!')
            else:
                sleep(0.5)
                print('Ainda não, MENOS!!')
    sleep(1)
    print('Parabéns!!!')
    sleep(1)
    print('Acertou com {} tentativas'.format(shot))
else:
    sleep(1)
    print('Tudo bem!! Quem sabe na próxima')
print('FIM')
