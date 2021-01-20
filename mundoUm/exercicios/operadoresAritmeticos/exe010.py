# EXERCICIO 010

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# SOLUÇÃO

carteira = float(input("Quantos reais você tem? "))
conversao = carteira / 5.21
print('Você pode trocar seus R$ {:.2f} por U$ {:.2f} dólares'.format(carteira, conversao))