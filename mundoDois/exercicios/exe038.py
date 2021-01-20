#  EXERCICIO 038

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O número {} é maior do que o número {}.'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior do que o número {}.'.format(num2, num1))
else:
    print('Não existe valor maior. Os dois números são iguais!')
