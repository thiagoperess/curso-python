# EXERCÍCIO 107 - EXERCITANDO MÓDULOS EM PYTHON

# Crie um módulo chamado moeda.py que tenha as funções incorporadas:
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# SOLUÇÃO

def aumentar(percent, preco):
    res = preco + (preco * percent / 100)
    return res


def diminuir(percent, preco):
    res = preco - (preco * percent / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res

