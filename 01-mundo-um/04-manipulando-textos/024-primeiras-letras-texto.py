# EXERCICIO 024 - VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO

# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

# SOLUÇÃO

cidade = str(input('Digite a cidade que você mora: ')).strip()
print(cidade[:5].lower() == 'santo')