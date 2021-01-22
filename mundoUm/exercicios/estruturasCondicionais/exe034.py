# EXERCICIO 034 - AUMENTOS MÚLTIPLOS

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

# SOLUÇÃO

salario = float(input('Digite seu salário: '))
if salario >= 1250:
    print('Você ganhou um aumento de R$ {:.2f}, referentes a 10% de {:.2f}'
          .format(salario * 10 / 100, salario))
else:
    print('Você ganhou um aumento de R$ {:.2f}, referentes a 15% de {:.2f}'
          .format(salario * 15 / 100, salario))
