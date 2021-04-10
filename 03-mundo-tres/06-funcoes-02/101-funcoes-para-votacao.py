# EXERCÍCIO 101 - FUNÇÕES DE VOTAÇÃO

# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# SOLUÇÃO


def voto(year):
    from datetime import date
    currentYear = date.today().year
    age = currentYear - year
    if age < 16:
        return f'Com {age} anos NÃO VOTA!'
    elif 16 <= age < 18 or age >= 65:
        return f'Com {age} anos, seu voto é OPCIONAL!'
    elif 18 < age < 65:
        return f'Com {age} anos seu voto é OBRIGATÓRIO!!'


ages = int(input('Em que ano você nasceu? '))
print(voto(ages))
