# EXERCÍCIO 114 - SITE ESTÁ ACESSÍVEL

# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# SOLUÇÃO

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o Pudim!')