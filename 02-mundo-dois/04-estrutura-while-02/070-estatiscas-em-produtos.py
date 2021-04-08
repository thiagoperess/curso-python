# EXERCÍCIO 070 - ESTATÍSTICAS EM PRODUTOS

# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# SOLUÇÃO

total = over1000 = cheaper = count = 0
nameCheaper = ''
print('-'*30)
print('{:-^30}'.format(' SUPER BARATÃO '))
print('-'*30)
while True:
    productName = str(input('Digite o nome do produto: '))
    productPrice = float(input('Quanto custa? '))
    count += 1
    optClient = str(input('Deseja continuar [S/N]? '))
    total += productPrice
    if count == 1:
        cheaper = productPrice
        nameCheaper = productName
    else:
        if productPrice < cheaper:
            cheaper = productPrice
            nameCheaper = productName
    if productPrice > 1000:
        over1000 += 1
    if optClient in 'Nn':
        break
print(f'As compras deram um total de R${total:.2f}.\n'
      f'No total tivemos {over1000} produtos com preço superior a R$1000,00.\n'
      f'{nameCheaper} foi o produto mais barato e custou R${cheaper}.\n'
      f'FIM')
