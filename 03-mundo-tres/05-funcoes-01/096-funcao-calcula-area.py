# EXERCÍCIO 096 - FUNÇÃO QUE CALCULA A ÁREA

# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# SOLUÇÃO

def area():
    rectangulararea = width * height
    print(f'A área retangular de {width}x{height} é {rectangulararea}m².')


print('Controle de Terrenos')
print('='*20)
width = float(input('LARGURA: (m): '))
height = float(input('COMPRIMENTO (m): '))
print('-'*20)
area()


