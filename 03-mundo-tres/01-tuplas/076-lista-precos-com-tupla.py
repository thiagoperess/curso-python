# EXERCÍCIO 076 - LISTA DE PREÇOS COM TUPLAS

# Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.

# SOLUÇÃO

listing = ('Lapis', 1.60,
           'Borracha', 2,
           'Caderno', 5.50,
           'Caneta', 2.69,
           'Estojo', 5.90,
           'Régua', 4.80,
           'Durex', 2.50,
           'Mochila', 50.80,
           'Pirocóptero', 2.90)

print('-' * 35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-' * 35)
for item in range(0, len(listing)):
    if item % 2 == 0:
        print(f'{listing[item]:.<25}', end=' ')
    else:
        print(f'R$ {listing[item]:>5.2f}')
print('-' * 35)
