# EXERCICIO 053 - DETECTOR DE PALÍNDROMO

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# SOLUÇÃO

frase = str(input('Digite uma frase: ')).replace(" ", "").upper()
palindromo = frase[::-1].strip().replace(" ", "").upper()

print('{} escrito ao contrário é {}.'.format(frase, palindromo))

if frase == palindromo:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo!')
