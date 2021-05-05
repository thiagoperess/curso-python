# EXERCÍCIO 110 - REDUZINDO AINDA MAIS SEU PROGRAMA

# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

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


def resumo(preco=0, taxaAum=10, taxaRed=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{coin(preco)}')
    print(f'Dobro do valor: \t{dobro(preco, True)}')
    print(f'Metade do valor: \t{metade(preco, True)}')
    percentAum = aumentar(preco, taxaAum)
    aumentoReal = percentAum + preco
    print(f'{taxaAum}% de aumento: \t{coin(aumentoReal)}')
    print(f'{taxaRed}% de redução: \t{diminuir(preco, taxaRed, True)}')
