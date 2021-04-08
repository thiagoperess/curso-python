# EXERCÍCIO 094 - UNINDO DICIONÁRIOS E LISTAS

# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas;
# B) A média de idade;
# C) Uma lista com as mulheres;
# D) Uma lista de pessoas com idade acima da média.

# SOLUÇÃO

people = list()
person = dict()
soma = average = 0
while True:
    person.clear()
    person['name'] = str(input('Nome: '))
    while True:
        person['gender'] = str(input('Sexo [F/M]: ')).upper()[0]
        if person['gender'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F!')
    person['age'] = int(input('Idade: '))
    soma += person['age']
    people.append(person.copy())
    while True:
        option = str(input('Quer continuar? [S/N] ')).upper()[0]
        if option in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if option == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(people)} pessoas.')
average = soma / len(people)
print(f'B) A média de idade é de {average:.0f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in people:
    if p['gender'] in 'Ff':
        print(f'{p["name"]}', end=' ')
print()
print('D) As pessoas com idade acima da média são ', end='')
for p in people:
    if p['age'] > average:
        print(f'{p["name"]}', end=' ')
