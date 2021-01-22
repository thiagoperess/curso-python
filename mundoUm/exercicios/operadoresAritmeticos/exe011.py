# EXERCICIO 011 - PINTANDO PAREDE

# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# SOLUÇÃO

largura = int(input('Qual a largura? '))
altura = int(input('Qual a altura? '))
mtQds = largura * altura
qtdTinta = mtQds / 2
print('A parede possui {}m² e precisa de {}L de tinta para sua pintura'.format(mtQds, qtdTinta))