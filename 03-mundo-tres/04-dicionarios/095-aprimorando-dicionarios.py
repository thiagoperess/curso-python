# EXERCÍCIO 095 - APRIMORANDO OS DICIONÁRIOS

# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# SOLUÇÃO

time = list()
soccerMatches = list()
player = dict()
while True:
    player.clear()
    player['nome'] = str(input('Qual o nome do jogador? '))
    total = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    soccerMatches.clear()
    for c in range(0, total):
        soccerMatches.append(int(input(f'Quantos gols na {c+1}º partida? ')))
    player['goals'] = soccerMatches[:]
    player['total'] = sum(player['goals'])
    time.append(player.copy())
    while True:
        option = str(input('Quer continuar? [S/N] ')).upper()[0]
        if option in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if option == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for data in v.values():
        print(f'{str(data):<15}', end='')
    print()
print('-'*40)
while True:
    searchPlayer = int(input('Mostrar dados de qual jogador? (999 para finalizar) '))
    if searchPlayer == 999:
        break
    if searchPlayer >= len(time):
        print('ERRO! Jogador não indexado! Tente novamente.')
    else:
        print(f'O LEVANTAMENTO DO JOGADOR {time[searchPlayer]["nome"]}')
        for i, g in enumerate(time[searchPlayer]['goals']):
            print(f' No jogo {1+i} fez {g} gols')
    print('-'*40)
print("<< VOLTE SEMPRE >>")
