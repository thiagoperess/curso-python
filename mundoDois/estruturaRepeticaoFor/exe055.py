# EXERCICIO 055 - MAIOR E MENOR DA SEQUÊNCIA

# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

# SOLUÇÕES

bigger = 0
smaller = 0
for p in range(1, 6):
    weight = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        bigger = p
        smaller = p
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight
print('O maior peso lido foi {}Kg.'.format(bigger))
print('O menor peso lido foi {}Kg.'.format(smaller))

# FAZENDO A MESMA COISA COM MIN E MAX EM UMA LISTA

list = []
for p in range(1, 6):
    weight = float(input('Peso da {}ª pessoa: '.format(p)))
    list += [weight]
print('O maior peso lido foi {}Kg.'.format(max(list)))
print('O menor peso lido foi {}Kg.'.format(min(list)))
