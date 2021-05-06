# EXERCÍCIO 112 - ENTRADA DE DADOS MONETÁRIOS

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

# SOLUÇÃO

from utilidadescev.moeda import resumo
from utilidadescev.dado import leiaDinheiro

price = leiaDinheiro('Digite o preço: ')
resumo(price, 50, 12)
