# EXERCICIO 008 - CONVERSOR DE MEDIDAS

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# SOLUÇÃO:

medida = float(input('qual a distância em metros? '))
cm = medida * 100
mm = medida * 1000
print('A medida de {} em centrímetros é {} e a medida em milímetros é {}'.format(medida, cm, mm))
