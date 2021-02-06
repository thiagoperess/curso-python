# EXERCICIO 031 - CUSTO DA VIAGEM

# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

# SOLUÇÃO

distancia = int(input('Qual foi a distância que você viajou? '))
if distancia > 200:
    print('Você deve pagar R${:.2f} pela viagem!'.format(distancia * 0.45))
else:
    print('Você deve pagar R${:.2f} pela viagem!'.format(distancia * 0.50))