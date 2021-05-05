# EXERCÍCIO 109 - FORMATANDO MOEDAS EM PYTHON V2

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando
# se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# SOLUÇÃO

def aumentar(percent=0, preco=0, formato=False):
    res = preco + (preco * percent / 100)
    return res \
        if formato is False \
        else coin(res)


def diminuir(percent=0, preco=0, formato=False):
    res = preco - (preco * percent / 100)
    return res \
        if formato is False \
        else coin(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res \
        if not formato \
        else coin(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res \
        if not formato \
        else coin(res)


def coin(preco=0, cipher='R$ '):
    return f'{cipher}{preco:.2f}'.replace('.', ',')
