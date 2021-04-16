# EXERCÍCIO 108 - FORMATANDO MOEDAS EM PYTHON

# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

# SOLUÇÃO

def aumentar(percent=0, preco=0):
    res = preco + (preco * percent / 100)
    return res


def diminuir(percent=0, preco=0):
    res = preco - (preco * percent / 100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def coin(preco=0, cipher='R$ '):
    return f'{cipher}{preco:.2f}'.replace('.', ',')


