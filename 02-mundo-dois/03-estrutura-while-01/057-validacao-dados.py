# EXERCICIO 057 - VALIDAÇÃO DE DADOS

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# SOLUÇÃO

sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sex not in "MmFf":
    sex = str(input("Dados inválidos! Por favor, informe seu sexo: "))
print('Sexo {} registrado com sucesso!'.format(sex.upper()))
