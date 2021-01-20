# EXERCICIO 012

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# SOLUÇÃO

produto = float(input('Qual o preço do produto? '))
desconto = produto * 5 / 100
precoFinal = produto - desconto
print('O preço novo com desconto de R$ {:.2f} é R$ {:.2f}.'.format(desconto, precoFinal))
