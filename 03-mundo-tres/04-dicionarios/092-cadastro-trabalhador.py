# EXERCÍCIO 092 - CADASTRO DE TRABALHADOR EM PYTHON

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# SOLUÇÃO

from datetime import datetime
data = dict()
data['name'] = str(input('Nome: '))
nasc = int(input('Ano do nascimento: '))
data['age'] = datetime.now().year - nasc
data['ctps'] = int(input('CTPS nº (0 não tem): '))
if data['ctps'] != 0:
    data['admission'] = int(input('Ano contratação: '))
    data['salary'] = int(input('Salário: R$ '))
    data['retirement'] = data['age'] + ((data['admission'] + 35) - datetime.now().year)
for k, v in data.items():
    print(f'{k}, tem o valor {v}.')
