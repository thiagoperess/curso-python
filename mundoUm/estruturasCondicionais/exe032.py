# EXERCICIO 032 - ANO BISSEXTO

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# SOLUÇÃO

import datetime
ano = int(input('Qual o ano deseja analisar? '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 \
        and ano % 100 != 0 \
        or ano % 400 == 0:
    print('O ano de {} é um ano BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é um ano BISSEXTO!'.format(ano))
