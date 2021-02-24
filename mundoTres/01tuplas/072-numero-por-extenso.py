# EXERCÍCIO 072 - NÚMERO POR EXTENSO

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# SOLUÇÃO

count = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = int(input('Digite um número: '))
    if 0 <= number <= 20:
        break
    print('Tente novamente!', end=' ')
print(f'Você digitou o número {count[number]}.')

while True:
    answer = str(input('Quer continuar? [S/N] '))
    if answer not in 'Ss':
        break
    else:
        while True:
            number = int(input('Digite um número: '))
            if 0 <= number <= 20:
                break
            print('Tente novamente!', end=' ')
        print(f'Você digitou o número {count[number]}.')
print('Obrigado e volte sempre!!')
