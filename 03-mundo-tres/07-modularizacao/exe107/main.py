import moeda

price = float(input('Qual o preço do produto? R$ '))
percent = int(input('percent: '))
print(f'Aumentando R$ {price:.2f} em {percent}%, temos R$ {moeda.aumentar(percent, price):.2f}')
print(f'Diminuindo R$ {price:.2f}, em {percent}%, temos R$ {moeda.diminuir(percent, price):.2f}')
print(f'O dobro de R$ {price:.2f} é R$ {moeda.dobro(price):.2f}')
print(f'A metade de R$ {price:.2f} é R$ {moeda.metade(price):.2f}')


