# EXERCÍCIO 073 - TUPLAS COM TIMES DE FUTEBOL

# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# SOLUÇÃO

times = ('Palmeiras', 'Santos', 'Vasco', 'Grêmio',
         'Flamengo', 'Corinthians', 'Internacional',
         'Cruzeiro', 'São Paulo', 'Atlético Mineiro',
         'Botafogo', 'Fluminense', 'Coritiba', 'Bahia',
         'Goiás', 'Guarani', 'Sport', 'Chapecoense', 'Vitória')

print('=*' * 30)
print(f'Lista de Times: {times}')
print('=*' * 30)
print(f'Os cinco primeiros colocados são: {times[:5]}')
print('=*' * 30)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=*' * 30)
print(f'A ordem alfabética dos times é: {sorted(times)}')
print('=*' * 30)
print(f'O {times[-2]} está na {times.index("Chapecoense")+1}ª posição')
