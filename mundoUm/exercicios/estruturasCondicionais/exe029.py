# EXERCICIO 029

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

# SOLUÇÃO

velocidade = float(input('Marca registrada no radar: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade de 80Km/h!')
    print('Por ter atingido a velocidade, foi aplicada uma multa de R${}'.format(multa))
else:
    print('Pode passar e boa viagem!')
