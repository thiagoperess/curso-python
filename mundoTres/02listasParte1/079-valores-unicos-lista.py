# EXERCÍCIO 079 - VAL0RES ÚNICOS EM UMA LISTA

# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

# SOLUÇÃO

option = 'Ss'
numbers = []

while True:
    if option in 'Ss':
        num = int(input('Digite um número: '))
        if num not in numbers:
            numbers.append(num)
            print('Valor adicionado com sucesso!')
        else:
            print('Valor duplicado! Não adicionado!')
        option = str(input('Deseja continuar? [S/N] '))
    else:
        break
print(f'Os valores únicos digitados foram: {sorted(numbers)}')
