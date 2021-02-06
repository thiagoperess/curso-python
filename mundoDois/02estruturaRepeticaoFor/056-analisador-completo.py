# EXERCICIO 056 - ANALISADOR COMPLETO

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:

# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

# SOLUÇÃO

ageSum = 0
ageAverage = 0
maxAgeMan = 0
oldName = ''
women20minus = 0

for c in range(1, 5):

    print('---- {}ª PESSOA ----'.format(c))

    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip()
    ageSum += age

    if c == 1 and gender in 'Mm':
        maxAgeMan = age
        oldName = name
    if gender in 'Mm' and age > maxAgeMan:
        maxAgeMan = age
        oldName = name
    if gender in 'Ff' and age < 20:
        women20minus += 1
ageAverage = ageSum / 4

print('A média de idade do grupo é de {} anos'.format(ageAverage))
print('O homem mais velho se chama {} e tem {} anos'.format(oldName, maxAgeMan))
print('Ao todo são {} mulheres com menos de 20 anos'.format(women20minus))
