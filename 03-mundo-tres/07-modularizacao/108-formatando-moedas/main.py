import moeda

price = float(input('Qual o preço do produto? R$ '))
percent = int(input('Qual percentual? '))
print(f'Aumentando {moeda.coin(price)} em {percent}% temos {moeda.coin(moeda.aumentar(percent, price))}')
print(f'Diminuindo {moeda.coin(price)} em {percent}% temos {moeda.coin(moeda.diminuir(percent, price))}')
print(f'O dobro de {moeda.coin(price)} é {moeda.coin(moeda.dobro(price))}')
print(f'A metade de {moeda.coin(price)} é {moeda.coin(moeda.metade(price))}')
