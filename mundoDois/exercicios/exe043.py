# EXERCICIO 043

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você possui um IMC de {:.2f} e está abaixo do peso'.format(imc))
elif 18.5 <= imc <= 25:
    print('Você possui um IMC de {:.2f} e está no peso ideal'.format(imc))
elif 25 <= imc <= 30:
    print('Você possui um IMC de {:.2f} e está com sobrepeso'.format(imc))
elif 30 <= imc <= 40:
    print('Você possui um IMC de {:.2f} e atingiu a obesidade'.format(imc))
else:
    print('Você precisa se cuidar, pois com o IMC de {:.2f}, está com Obesidade Mórbida'.format(imc))