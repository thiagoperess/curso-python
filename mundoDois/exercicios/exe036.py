# EXERCICIO 036 - APROVANDO EMPRÉSTIMO

# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele não pode execeder 30% do salário, ou então, o empréstimo será negado.

# SOLUÇÃO

valorCasa = float(input('Valor da casa: R$ '))
salarioComprador = float(input('Digite seu salário: R$ '))
tempoPagando = int(input('Em quantos anos você quer pagar? '))
parcelaImovel = valorCasa / tempoPagando / 12

if parcelaImovel <= salarioComprador * 0.3:
    print('Para comprar uma casa de R$ {:.2f} em {} anos, a valor da parcela será R$ {:.2f}.\n'
          'Seu empréstimo foi \033[1;32mAPROVADO\033[m!'.format(valorCasa, tempoPagando, parcelaImovel))
else:
    print('Para comprar em casa de R$ {:.2f} em {} anos, o valor da parcela será de R$ {:.2f}.\n'
          'Seu empréstimo foi \033[1;31mNEGADO\033[1m!'.format(valorCasa, tempoPagando, parcelaImovel))
