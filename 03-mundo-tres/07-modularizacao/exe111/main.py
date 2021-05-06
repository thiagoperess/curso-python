# EXERCÍCIO 111 -  TRANSFORMANDO MÓDULOS EM PACOTES

# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# SOLUÇÃO

from utilidadescev.moeda import resumo

price = float(input('Qual o preço do produto? R$ '))
resumo(price, 50, 12)