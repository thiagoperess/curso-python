# EXERCICIO 015

# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# SOLUÇÃO

dias = int(input('Quantos dias usados? '))
km = int(input('Quantos km foram rodados? '))
print('O valor total a ser pago é {:.2f}'.format(dias * 60 + km * 0.15))