# EXERCÍCIO 071 - SIMULADOR DE CAIXA ELETRÔNICO

# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# SOLUÇÃO
import time
print('-'*30)
print('{:-^30}'.format(' BEM VINDO AO DEVCASH '))
print('-'*30)
value = int(input('Qual valor você deseja sacar? R$ '))
total = value
totBill = 0
bill = 50
while True:
    if total >= bill:
        total -= bill
        totBill += 1
    else:
        if totBill > 0:
            print(f'Total de {totBill} cédula(s) de R$ {bill}')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totBill = 0
        if total == 0:
            break
print('-'*30)
print('MUITO OBRIGADO E VOLTE SEMPRE')
print('-'*30)
