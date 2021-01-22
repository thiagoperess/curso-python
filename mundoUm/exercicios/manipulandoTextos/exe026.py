# EXERCICIO 026 - PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# SOLUÇÃO

frase3 = str(input('Digite a frase: ')).lower().strip()
print('A frase tem {} letras {}.'.format(frase3.count('a'), 'a'))
print('A primeira letra A apareceu na frase na posição {}'.format(frase3.find('a')+1))
print('A última letra A apereceu na frase na posição {}'.format(frase3.rfind('a')+1))