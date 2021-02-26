# EXERCÍCIO 082 - DIVIDINDO VALORES EM VÁRIAS LISTAS

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

# SOLUÇÃO

evenList = []
oddList = []
numbersList = []
option = 'S'
while True:
    if option in 'S':
        numbers = int(input('Digite um número: '))
        option = str(input('Deseja continuar? [S/N] ')).upper().strip()
        numbersList.append(numbers)
    else:
        break
    if numbers % 2 == 0:
        evenList.append(numbers)
    else:
        oddList.append(numbers)
print(f'Os valores inseridos na lista foram {numbersList}')
print(f'Os números pares são {sorted(evenList)}')
print(f'Os números impares são {sorted(oddList)}')
