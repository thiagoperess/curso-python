# EXERCÍCIO 097 - UM PRINT ESPECIAL

# Faça um programa que tenha uma função chamada escreva(), que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# SOLUÇÃO

def escreva(text):
    tam = len(text) + 4
    print('~' * tam)
    print(f'  {text}')
    print('~' * tam)


escreva(str(input('Digite uma frase: ')))
escreva(str(input('Digite uma frase: ')))
escreva(str(input('Digite uma frase: ')))

