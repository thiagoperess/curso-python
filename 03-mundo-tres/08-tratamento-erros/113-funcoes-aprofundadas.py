# EXERCÍCIO 113 - FUNÇÕES APROFUNDADAS EM PYTHON

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# SOLUÇÃO

def readInt(msg):
    while True:
        try:
            num = int(input('Digite o número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário preferiu não digitar\033[m')
            return 'nenhum'
        else:
            return num


def readFloat(msg):
    while True:
        try:
            num = float(input('Digite o número real: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário preferiu não digitar\033[m')
            return 'nenhum'
        else:
            return num


numInt = readInt('Digite o número: ')
numFloat = readFloat('Digite o número: ')
print(f'O valor inteiro foi {numInt} e o valor real foi {numFloat}')
