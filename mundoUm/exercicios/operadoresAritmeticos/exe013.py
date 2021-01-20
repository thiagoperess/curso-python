# EXERCICIO 013

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# SOLUÇÃO

salario = int(input('Qual o salário do funcionário? '))
aumento = salario * 15 / 100
novoSalario = salario + aumento
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(salario, novoSalario))