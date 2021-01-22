# EXERCICIO 043 - INDICE DE MASSA CORPORAL

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

# SOLUÇÃO:

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você possui um IMC de {:.2f} e está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Você possui um IMC de {:.2f} e está no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Você possui um IMC de {:.2f} e está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Você possui um IMC de {:.2f} e atingiu a obesidade'.format(imc))
else:
    print('Você precisa se cuidar, pois com o IMC de {:.2f}, está com Obesidade Mórbida'.format(imc))