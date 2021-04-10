# EXERCÍCIO 104 - VALIDANDO ENTRADA DE DADOS EM PYTHON

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante à função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# SOLUÇÃO

def readInt(msg):
    ok = False
    value = 0
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return value


number = readInt('Digite um número: ')
print(f'Você acabou de digitar o número {number}.')


