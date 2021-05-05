import moeda

price = float(input('Qual o preço do produto? R$ '))
percent = int(input('Qual percentual? '))
print(f'Aumentando {moeda.coin(price)} em {percent}% temos {moeda.aumentar(percent, price, True)}')
print(f'Diminuindo {moeda.coin(price)} em {percent}% temos {moeda.diminuir(percent, price, True)}')
print(f'O dobro de {moeda.coin(price)} é {moeda.dobro(price, True)}')
print(f'A metade de {moeda.coin(price)} é {moeda.metade(price, True)}')
