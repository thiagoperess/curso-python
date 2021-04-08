# EXERCÍCIO 077 - CONTANDO VOGAIS COM TUPLAS

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# SOLUÇÃO

words = ('python', 'tensorflow', 'pandas', 'numpy',
         'scipy', 'matplotlib', 'seaborn', 'plotly',
         'scikit-learn', 'pytorch', 'keras', 'Scrapy')

for w in words:
    print(f'\nNa palavra {w} temos ', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
